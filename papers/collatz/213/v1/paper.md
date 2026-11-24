# The least peak of a Collatz meeting with a smaller start

## 1. The global height

Let $C(t)=t/2$ for even $t$ and $C(t)=(3t+1)/2$ for odd $t$. For $x>1$, let $h(x)$ be the least peak of two forward paths from $x$ and from some positive $z<x$ to one common state. The peak includes both paths, their sources and their endpoint. Both clocks are independent nonnegative integers. Set $h(x)=\infty$ when there is no pair. A fixed-target source floor is the least positive source reaching a specified state within given constraints. Here the eligible targets are all states reachable from $x$ within the cap, and the test is whether any of their capped source floors is below $x$.

The peak law in [1, Theorem 8] minimizes the visitor's peak on visits before Terras's first strict descent [2], compares it with the original excursion peak, and clamps the ratio at one. The first-meeting law in [3] minimizes the original clock over the complete orbits of smaller starts. Related results give logarithmic first-meeting dates on arithmetic layers [4] and count first meetings at the strict descent itself [5]. For $h(x)$ a later meeting can realize a lower peak, and the descent landing itself is eligible. Theorem 2 bounds both clocks at the minimizing peak. Theorem 4 uses component counts to evaluate the reciprocal mean. Theorems 5 and 5a describe the two old minima when increasing the height joins their components.

**Proposition 1 (capped components).** For integer $H\ge x$, $h(x)\le H$ exactly when the component of $x$ in the undirected graph on $[1,H]$ contains a smaller vertex. The graph uses edges $\{v,C(v)\}$ with both ends in $[1,H]$.

Each truncated trajectory ends at a sink or enters a directed cycle. An edge preserves that terminal object, and trajectories having the same object meet within the cap. In particular, if labels $f(v)$ agree on every capped edge and $\Delta(j)=f(j+1)-f(j)$, a smaller vertex $z$ in the component gives $\Delta(x-1)=-\sum_{j=z}^{x-2}\Delta(j)$. If the component has minimum $x$, its indicator on the capped graph gives $\Delta(x-1)=1$ and all earlier differences zero. This proves the necessity of the component test even for signed linear combinations.

Every even $x$ and every odd $x\equiv2\pmod3$ has $h(x)=x$, by halving or by the odd parent $(2x-1)/3$ respectively. All other $x$ have $h(x)\ge(3x+1)/2$: below that height the only possible parent $2x$ and the successor are absent. These two cases give density $2/3$ at $h(x)=x$.

Terras's stopping time is the first strict descent of the original trajectory [2]. Such a descent gives a witness with visitor clock zero. More generally, for an individual $x$, a finite witness proves arrival at $1$ under the induction hypothesis that every smaller start reaches $1$. A witness for every $x>1$ is therefore equivalent to the Collatz conjecture by strong induction. The shortcut and ordinary maps have the same eventual-arrival property because the shortcut skips the obligatory even state after an odd step. A failed finite cap test excludes witnesses under that cap alone.

## 2. Two clocks at the actual minimum

For a word of length $j$ with $k$ odd departures, the endpoint from $y$ is $(3^k y+b)/2^j$, where $0\le b\le3^j-2^j$. Indeed appending bit $e$ at index $i$ replaces $b$ by $3^e b+e2^i$, and the all-odd word uniquely maximizes it. Each word occupies exactly one class modulo $2^j$: lifting a class by $2^j$ changes its terminal state by the odd integer $3^k$, so both next parities occur. The inverse steps are $E(v)=2v$ and $O(v)=(2v-1)/3$, the latter legal exactly at $v\equiv2\pmod3$.

Write

$$
P_j(B)=2^{-j}\sum_{3^kB\ge2^j}\binom jk,\qquad
\rho=\frac54(3/2)^{-5/8}<1 .
$$

The sum ranges over $0\le k\le j$. Since $\log_3 2>5/8$, Markov's inequality applied to $(3/2)^k$ for a fair binomial gives $P_j(B)\le(3/2)^{\log_3 B}\rho^j$ for $B\ge1$. All interval densities below mean convergence uniformly in the location of an interval of consecutive positive integers as its length tends to infinity. Omitting $x=1$ from start counts has a bounded effect.

**Theorem 2 (optimal clocks).** For every integer $m\ge1$, in every interval of length $L$, all but $O(L\rho^m+3^{64m})$ starts $x>1$ realize $h(x)\le2^m x$ with original clock at most $m$ and visitor clock at most $64m$. The constant is absolute. In particular, both clocks are $O(\log L)$ outside $O(L^{1-\delta})$ starts, where $\delta=-\log\rho/(128\log3)>0$.

**Proof.** Put $n=64m$, $B=2^m$ and discard $x\le3^n$. If the first $m$ steps never go below $x$, their coefficient satisfies $3^k\ge2^m$ by the offset bound. The words satisfying this coefficient inequality have total binary mass $P_m(1)$ and count at most $(L+2^m)P_m(1)$. On all remaining starts the first descent is at a date $d\le m$ and has peak at most $Bx$, since $C(t)\le2t$. In particular, $h(x)$ is finite. Choose a witness with peak $h(x)$. If its original portion includes date $d$, stop there and use $C^d(x)<x$ as the visitor at clock zero. The shortened peak is at most $h(x)$ and minimality forces equality. Otherwise the meeting date is $j<d\le m$ and all its original states are at least $x$.

Restart the visitor at its last state below $x$. If more than $n$ steps remain, the final $n$ start at $y\in[x,Bx]$ and end at the meeting $v\ge x$. With $k$ odd departures they satisfy $2^n v=3^k y+b$. If $3^k B<2^n$, the integer gap and $b<3^n<x$ contradict this relation. Thus only words with $3^k B\ge2^n$ are eligible.

For a fixed original word of length $j$ and odd count $K$, write $x=x_0+2^jt$ and $v=v_0+3^Kt$. The suffix imposes $v\equiv 2^{-n}b\pmod{3^k}$, so the starts lie in at most one class of modulus $2^j3^{\max(k-K,0)}$. This is the inverse-word congruence of [1, §8] with the existing ternary restriction on the original endpoint included. A compatible suffix therefore has conditional mass $3^{-\max(k-K,0)}\le3^{K-k}\le3^K B2^{-n}$. There are $2^nP_n(B)$ eligible suffix words, and $\sum 2^{-j}3^K=2^{-j}(1+3)^j=2^j$ over the original words of length $j$. Counting each resulting class in an interval incurs an additive error of at most one. Summing over $0\le j\le m$ bounds the count by

$$
LB(2^{m+1}-1)P_n(B)+(2^{m+1}-1)2^n .
$$

The main term is at most $2L6^m\rho^{64m}\le2L\rho^m$. Here $B=2^m$ gives $(3/2)^{\log_3 B}\le(3/2)^m$, and $6\rho^{63}<1$ follows by raising to the eighth power and comparing integers. All additive errors are $O(3^{64m})$. Taking $m=\lfloor\log_3 L/128\rfloor$ for large $L$ proves the interval claim. $\square$

**Theorem 3 (atomic law).** For every rational affine expression $sx+c$ occurring as a path state, there is a uniform interval density $p_{s,c}$ of $h(x)=sx+c$. Their sum is one. The ratios $h(x)/x$ have a purely atomic weak limit, with mass $\sum_c p_{s,c}$ at $s\in\{2^a3^b:a,b\in\mathbb Z\}\cap[1,\infty)$. For every real $B\ge1$ the uniform density of the inclusive cap is

$$
D(B)=\operatorname{dens}\{x:h(x)\le Bx\}
=\sum_{s<B,c}p_{s,c}+\sum_{c\le0}p_{B,c}. \tag{1}
$$

**Proof.** Fix deadlines $m,n$. Enumerate a forward word from $x$ and an inverse word from its endpoint. All states are rational affine in $x$. The integrality constraints are periodic modulo $2^m3^n$ and enforce the prescribed parities. On each class, positivity and $z<x$ stabilize, using the offset for equal slopes. The finite peak and the minimum over legal pairs also stabilize to affine expressions on each eventual class, allowing an infinite minimum. Distinct expressions agree at most once. For $n=64m$, Theorem 2 bounds the upper interval density where this finite minimum misses $h(x)$ or is infinite by $O(\rho^m)$. For each expression the finite counts thus approximate its upper and lower densities within $O(\rho^m)$. The finite list at these deadlines carries mass at least $1-O(\rho^m)$. This proves existence and total mass. The slopes are products of the forward and inverse step slopes, and $h(x)\ge x$ forces $s\ge1$ on a positive-density line. Restricting first to a finite subcollection of mass arbitrarily close to one proves weak convergence and (1), since each fixed offset divided by $x$ tends to zero and affine cap comparisons eventually stabilize. $\square$

The same finite enumeration at rational $B$ computes the density of witnesses within both deadlines by adding the inclusive cap inequalities and comparing slopes, then offsets. With $n=64m$ its error relative to $D(B)$ is $O(\rho^m)$. For an explicit bound independent of that implicit constant, at any deadlines $m,n\ge1$ this error is at most

$$
P_m(1)+B(2^{m+1}-1)P_n(B). \tag{2}
$$

Indeed an original clock exceeding $m$ either shortens to a descent within $m$ or has a length-$m$ word of slope at least one for all sufficiently large $x$. Otherwise use the last smaller visitor state and the final $n$ steps as in Theorem 2. For fixed $B,m,n$, a slope with $3^kB<2^n$ forces $x\le b/(2^n-3^kB)$, excluding only finitely many starts. The same congruence count gives the second term. Taking $n=m^2$ makes (2) tend to zero for fixed $B$.

## 3. Absolute heights and the distribution at a merger

**Theorem 4 (height count and reciprocal moment).** Let $S(M)$ count odd $t\le M$ with $3t+1>2M$, and let $K(M)$ count cycles contained in $[1,M]$. Then

$$
A(M):=\#\{x>1:h(x)\le M\}=M-S(M)-K(M).
$$

The uniform interval mean of $x/h(x)$, with value zero at infinite $h(x)$, is $5/6$. Its conditional mean on $h(x)>x$ is $1/2$.

**Proof.** Each component has one minimum, and every other vertex contributes to $A(M)$. Its terminal object is either a cycle or one of the $S(M)=M/6+O(1)$ sinks. To count cycle maxima in a translated interval of $L$ heights, take the last $n$ steps ending at the maximum $H$, repeating the cycle as needed. The initial state is at most $H$, so if $H>3^n$, the affine offset bound forces $3^k>2^n$. Each word with $k$ odds confines $H$ to one class modulo $3^k$. The total number of cycle maxima is therefore at most $3^n+2^n+LP_n(1)$. With $n=\lfloor\log_3 L/2\rfloor$ this is $O(L^{1-\eta})$ for some $\eta>0$, uniformly. Hence $A(M)/M\to5/6$.

On each fixed subinterval $a<x/M\le b$ of $(0,1]$, the caps $x/b$ and $x/a$ bound the absolute-cap test from below and above. By Theorem 3 the limiting counts divided by $M$ are bounded by $(b-a)D(1/b)$ and $(b-a)D(1/a)$. The part adjacent to zero has contribution at most its length. Riemann sums for this bounded monotone function give

$$
\int_0^1 D(1/u)\,du=\int_1^\infty D(B)\,\frac{dB}{B^2}=\frac56 .
$$

Integrate the indicators of $h(x)\le x/u$ on $0<u\le1$ to obtain $x/h(x)$. Bounded convergence along any sequence of intervals of diverging lengths gives the uniform interval mean. The mass $2/3$ at $h(x)=x$ yields the conditional value $(5/6-2/3)/(1/3)=1/2$. $\square$

**Theorem 5 (mergers).** For each integer $H$, precisely one earlier source $x_H<H$ satisfies $h(x_H)=H$ if $H\equiv2\pmod6$ and $H$ is not a cycle maximum. At other heights there is no such source. Choosing $H$ uniformly among these merger heights in a height interval of length tending to infinity, the limiting law of $x_H/H$ has mass $6\sum_c p_{s,c}/s$ at $1/s$ for $s>1$.

**Proof.** A new vertex $H$ can join two old components only if it has a lower image $H/2$ and a lower odd parent $u=(2H-1)/3$, precisely at $H\equiv2\pmod6$. In the old graph $u$ is a sink. Its component contains $H/2$ exactly when the path of $H/2$ reaches $u$ and adding $H$ closes a cycle. If the components are distinct, only the larger of their two minima acquires its first smaller connection. The new vertex itself is outside the count of earlier sources.

For each positive-mass line $H=sx+c$ with $s>1$, the count in a height interval of length $L$ is the start count in an interval of length $L/s+O(1)$. Finite intersections of distinct lines change the counts by $O(1)$ for any fixed finite family. The frequency of merger heights is $1/6$ by the cycle bound. The limiting mass on those heights transferred from each line is therefore $6p_{s,c}/s$. Theorem 4 and the weak limit applied to the bounded reciprocal function give $\sum p_{s,c}/s=5/6$. Proposition 1 gives $p_{1,0}=2/3$ and no further mass at slope one, by the gap to $(3x+1)/2$. The transferred masses sum to one, so finite subcollections exhaust the limiting law uniformly in height intervals. $\square$

For example, the slope $3/2$ has mass $1/6$ among starts and gives mass $2/3$ at the reciprocal ratio $2/3$ among mergers. Indeed among the odd $x$ without a smaller capped parent at height $x$, those with $x\equiv1\pmod4$ descend after reaching $p=(3x+1)/2$ and have $h(x)=p$. These are the classes $1,9\pmod{12}$. The remaining odd starts have $p$ odd, and below $2x$ only $x,p$ are in the capped component. The unused even parent of either state is at least $2x$, and $C(p)>2x$. This exhausts the atom at $3/2$.

### The minimum that survives a merger

Write $C_e$ for the shortcut rule with $(3t+e)/2$ on odd $t$, where $e=1$ gives the original map. At $e=-1$ the distinct cycles containing 1 and 5 provide examples of components that can persist at every sufficiently large cap. Take $H=6k+2$ for $e=1$ and $H=6k+4$ for $e=-1$. With $u=(2H-e)/3$ and $v=H/2$, the new path is $u\to H\to v$. Write $a_H,b_H$ for the respective component minima of $u,v$ at cap $H-1$. For example, at $e=1$ and $H=62$ the old components are $\{27,41,54\}$ and $\{31,47\}$. The path $27\to41\to62\to31$ leaves 27 as the minimum and gives $h(31)=62$.

**Theorem 5a (surviving minimum).** In any interval of $L$ consecutive nonnegative $k$, set $t_H=H L^{-1/100}$. Uniformly in the interval and in $e$, for some absolute $\eta>0$,
$$
\#\{k:a_H\le t_H\}=O(L^{1-\eta}),\qquad
\#\{k:b_H\le t_H\}=pL+O(L^{1-\eta}).
$$
Here $p=0.5726307930600027507\ldots$ is the probability that $S_j=3^{K_j}/2^j$ stays below two for every $j\ge1$, where $K_j$ is the number of ones in the first $j$ fair independent bits. Thus $pL+O(L^{1-\eta})$ mergers have surviving minimum at most $t_H$ on the $v$ side. At least $(1-p)L-O(L^{1-\eta})$ heights join two distinct old components that both end at sinks and both have minima above $t_H$.

**Proof.** Put $M=\lfloor(\log_2 L)/4\rfloor$, $n=\lfloor(\log_2 L)/200\rfloor$ and $r=(1+\sqrt3)/(2\sqrt2)<1$, so $\mathbb E\sqrt{S_i}=r^i$. Discard $v\le\sqrt L$ at cost $O(\sqrt L)$. For large $L$ the remaining $v$ exceed $3^M$. A length-$i$ word of the signed map has endpoint $(3^\ell y+eB)/2^i$ with $0\le B<3^i$ for $i\ge1$, and occupies one binary class as in Section 2.

If a sink $w\ge H/2$ is reached under the old cap from $z\le t_H$, the path takes more than $n$ steps, since $2^n t_H<H/2$ and $C_e(t)\le2t$. Its final $n$ steps start below $H$. The offset bound $B<3^n<H$ forces $3^\ell\ge2^{n-1}$. Markov's inequality applied to $\sqrt{S_n}$ gives at most $2^n\sqrt2\,r^n$ such suffix words. Each confines $w$ to one class modulo $3^\ell$. For $w=u$ the coefficient of $k$ is 4, so each suffix accounts for at most $L/3^\ell+1$ values of $k$. Their union costs $O(Lr^n+2^n)$, proving the estimate for $a_H$.

Suppose $v$ first leaves the cap at date $j+1$, with old sink $w=C_e^j(v)\ge H/2$. On a fixed length-$j$ binary class of $k$, increasing $k$ by $2^j$ increases $w$ by $3^{K_j+1}$, because $v=3k+1$ or $3k+2$. Each eligible suffix contributes conditional mass at most $3^{K_j+1-\ell}$ and one rounding error in the count. Summing as in Theorem 2, using $\sum 2^{-j}3^{K_j}=2^j$, bounds exits at this date with $b_H\le t_H$ by $O(L2^j r^n+2^{n+j})$. Choose a fixed integer $d$ with $2^{1/d}r<1$ and put $j_0=\lfloor n/d\rfloor$. The sum for $j<j_0$ is $O(L^{1-\eta})$ for some $\eta>0$.

For $1\le i\le M$, comparison of $C_e^i(v)$ with $H=2v$ is decided by $3^{K_i}-2^{i+1}$. This integer is nonzero and its contribution times $v$ exceeds the offset in absolute value. Since $v=3k+1$ or $3k+2$, each length-$M$ word occupies one class of $k$ modulo $2^M$. The count of any such binary event over the full interval consequently differs from $L$ times its fair-bit probability by at most $2^M$. The probability of any upward crossing after $j_0$ is $O(r^{j_0})$ by summing $\Pr(S_i>2)\le r^i/\sqrt2$. Consequently the number still inside through $M$ is $pL+O(L^{1-\eta})$, and the exits between $j_0+1$ and $M$ cost $O(L^{1-\eta})$, after decreasing $\eta$.

For those still inside, $b_H\le C_e^M(v)$. The fair binomial tail above $K_M=9M/16$ has mass at most $\exp(-M/128)$. On the other words
$$
\frac{C_e^M(v)}{H}\le
\tfrac12\,2^{-(1-(9/16)\log_2 3)M}+\frac{(3/2)^M}{H}
\le L^{-1/100}
$$
eventually, since $(1-(9/16)\log_2 3)/4>1/100$ and $H>2\sqrt L$. This proves the estimate for $b_H$. An exit from the old cap puts the $v$ component at a sink. Cycle closures have count $O(L^{1-\eta})$ for either sign by the cycle-maximum argument in Theorem 4 applied to $6L$ heights with $|eB|<3^n$. The two merger counts follow.

For the numerical enclosure, let $\tau$ be the first upward crossing of two and set $A_j=\Pr(\tau>j)$, $B_j=\mathbb E[S_j\mathbf1_{\{\tau>j\}}]$. The martingale stopped at $\tau$ is bounded by three. Its value tends to zero on $\tau=\infty$ by the strong law, and $2<S_\tau<3$ on a crossing. Bounded convergence gives $B_j=\mathbb E[S_\tau\mathbf1_{\{j<\tau<\infty\}}]$, hence $A_j-B_j/2\le p\le A_j-B_j/3$. Counting surviving words by $(j,K_j)$ through $j=1024$ encloses $p$ in $[0.572630793060002750750891,0.572630793060002750802878]$. $\square$

Once a specified cycle fits below $H$, its component can occur only on the $v$ side, since $u$ is a sink. For the positive map the limiting upper fraction of mergers into the component at 1 is therefore at most $p$. For the negative sign the same bound applies to the union of mergers into the fixed point 1 and the cycle $5\to7\to10\to5$. Identifying which cycle, if any, a particular small minimum eventually reaches remains a question about that integer.

## 4. The sixfold cap and its right jump

Let $F_H(x)$ denote descent below $x$ along its trajectory under the inclusive cap $H$, and $I_H(x)$ the existence of a smaller source reaching $x$ under that cap. Let $G_H(x)$ hold when the forward trajectory either descends or executes two consecutive halvings, with every visited state through that event at most $H$.

**Proposition 6 (sixfold criterion).** For all integers $x>1$ and $x\le H\le6x+1$,

$$
h(x)\le H\quad\Longleftrightarrow\quad G_H(x)\ \text{or}\ I_H(x).
$$

**Proof.** A descent or a smaller ancestor of $x$ gives a meeting directly. For two halvings $4v\to2v\to v$, it suffices to consider an odd source and no descent up to $v$. The predecessor of $4v$ on the original path is odd, since $8v>H$ and $4v$ is even, hence differs from the source. From $8v=3u+1$ we obtain $v\equiv2\pmod3$, and $(2v-1)/3<x$ from $4v\le6x+1$. This is a one-step visitor to $v$.

Conversely, in the absence of the two endpoint tests $F_H,I_H$, take the earliest original date that any smaller capped visitor touches, at a state $v>x$. The two incoming edges differ. If the original came from an odd $u$, the visitor came through $2v=3u+1\equiv1\pmod3$. Its only predecessor is $4v=6u+2\ge6x+2$, which exceeds the cap. If the original came from $2v$, an alternative odd predecessor forces $v\equiv2\pmod3$. The preceding original state is then $4v$ because $2v\equiv1\pmod3$ and the source is odd. This gives $G_H$. $\square$

For $1\le B\le6$, the density $g_B$ of $G_{\lfloor Bx\rfloor}(x)$ is obtained by admitting the initial state $s=1$ and giving the two forward slope updates $s/2,3s/2$ equal weight. After each update, discard the new state if its slope is at least $B$. Otherwise record success on descent below one or on a second consecutive even departure, and continue in the remaining cases. At positive depth a slope differs from one. If it equals $B\ge1$, the word has an odd step and positive offset, so the actual state exceeds the inclusive cap. In particular $g_1=1/2$, from the first halving. The unresolved mass after $m$ steps is at most $(3/4)^{\lfloor m/2\rfloor}$.

The inverse search starts from $v=x$. At each $v\ge x$, a multiple of three can only have doubling ancestors. A state of residue one needs one doubling before an odd inverse, provided $2v\le H$. A residue-two state takes its odd inverse immediately. In the last case the alternative with two doublings requires $4v\le H\le6x+1$, which already ensures that the immediate odd parent is below $x$. Three doublings cannot fit under the cap. A repeat can end the search, since the available continuation is unchanged. Consequently the inverse density $i_B$ is computed from $s=1$ by equal trit weights on failure, the step $2s/3$, and the step $4s/3$ when $2s\le B$ with failure otherwise. A landing below one succeeds. The inverse offset is nonpositive, so a slope tie on doubling is allowed. An inverse landing at positive round depth has a power of three in its denominator and cannot have slope one. Each prescribed inverse history with $k$ odd inverses fixes one class modulo $3^k$, and the state changes by a power of two on increasing the source by $3^k$. The next trit is equidistributed across its lifts. The unresolved mass after $k$ rounds is at most $(2/3)^k$.

Finite binary and ternary class densities multiply by the Chinese remainder theorem. The two unresolved masses tend to zero, so Proposition 6 gives $D(B)=g_B+(1-g_B)i_B$. In particular the depth-160 counts described in Section 6 give

$$
0.971382340697714694097329\le D(6)\le0.971382340697714694097330 .
$$

**Theorem 7 (exact right jump).** Write $D(6\pm)$ for the one-sided limits. Then $D(6-)=D(6)$ and

$$
D(6+)-D(6)=\operatorname{dens}\{x:h(x)=6x+2\}=\frac{(1-g_6)j}{9},
\tag{3}
$$

where $j$ is the success probability of the inverse trit recursion starting at $s=32/9$ with the doubling test $2s<6$.

**Proof.** Put $H=6x+2$, $H_0=H-1$ and consider odd $x$, since even $x$ already descends. The new edges are $q\to H\to2p$, where $q=4x+1$ and $p=(3x+1)/2$. The vertex $q$ is an old sink. The edges $2p\to p\leftarrow x$ put $2p$ in the old component of $x$. If $h(x)>H_0$, that component has minimum $x$. Hence $h(x)=H$ precisely if $h(x)>H_0$ and a smaller start reaches $q$ under $H_0$. Theorem 5 also excludes $h(x)=6x+1$ since $6x+1>x$.

The only possible parent of $q$ under $H_0$ is $r=(8x+1)/3$, which exists for $x\equiv1\pmod3$. On $x\equiv1\pmod9$, $r>x$ is divisible by three. On $x\equiv4\pmod9$, $(8x-5)/9<x$ already reaches $x$ via the inverse word $EOO$ from $x$ and peak $2x$. The remaining class is $x\equiv7\pmod9$. Here $r$ has residue one and its viable inverse route goes through $2r$ to $w=(32x+1)/9$, since $4r>H_0$. Also $I_{H_0}(x)$ fails because the only possible first odd inverse from $x$ follows one doubling and lands at the multiple of three $(4x-1)/3>x$. The search from $w$ is precisely the inverse round rule at integer cap $H_0$. Thus the exact height requires this residue class, failure of $G_{H_0}$ and success from $w$. Failure of $G_{H_0}$ already imposes odd parity.

For $x=9t+7$ we have $w=32t+25$, and the successive odd inverses impose ternary classes as above. Round slopes from $w$ have the form $2^{5+a}/3^{2+k}$ with $a,k\ge0$, so neither the landing test nor the doubling test has a slope tie. The unresolved mass after $k$ rounds is at most $(2/3)^k$. Likewise every positive-date forward slope differs from six, and the binary limiting density for $G_{H_0}$ is $g_6$ by finite truncation and its unresolved bound. The Chinese remainder theorem gives the rightmost density in (3).

To identify the right limit, fix finite clock bounds and take $B\downarrow6$ in the finite witness count. On each eventual admissible class the surviving pairs are those with every state slope at most six, retaining the strict smaller-source test. The original states then lie strictly below $6x$ eventually, because no forward slope equals six. A descent gives a witness under $6x$. Otherwise shorten to the first original state touched by the visitor. A touch at $x$ uses inverse slopes $2^a/3^b$ with $a,b\ge0$, all strictly below six when at most six. For a later first contact $v$, the incoming edges differ, and we may take $x$ odd. If the original came through $2v$, the alternative odd parent forces $4v$ on the original prefix as in Proposition 6. This provides a witness below $6x$. If the original came from odd $u$, the visitor came through $4v=6u+2$ and $2v$. A positive-date original state without descent has slope strictly above one. The slope of $4v$ is at most six only for $u=x$, giving $v=p$ and $4v=H$. The preceding visitor state must be $q$, since $8v$ has slope twelve and $4v$ is above the visitor source. All earlier visitor states traced from $q$ have slopes $4\cdot2^a/3^b$, none equal to six. Hence the path fits under $6x+2$ on all sufficiently large starts on that class.

The uniform error bound (2) with $B=7$ bounds the truncation error simultaneously for $6<B\le7$, and tends to zero along $n=m^2$. This proves $D(6+)\le\operatorname{dens}\{h(x)\le6x+2\}$. The opposite inequality follows since $6x+2\le Bx$ eventually for every $B>6$. From the left, fixed-depth successful $G$ and $I$ histories at $6x$ have slopes strictly below six, including the one-step visitor in the double-halving case. Taking the truncation depths to infinity gives $D(6-)=D(6)$. $\square$

Exact depth-160 recursions with outward rounding enclose $j$ in $[0.028246281649708132800723,0.028246281649708132800724]$ and the jump in $[0.000167083449296780983878,0.000167083449296780983879]$.

**Proposition 8 (sharp arithmetic class).** Every $x\equiv5695\pmod{23328}$ has $h(x)=6x+2$. At that cap the earliest visitor clock is ten, and any first contact with the capped original path is at $p=(3x+1)/2$, at original date one.

**Proof.** More generally take $x\equiv-1\pmod{32}$, $x\equiv7\pmod9$ and $x\ge100$. The first five departures are odd, the first four images are below $6x+2$ and the fifth is above it. There is no descent or double halving, and the preceding argument gives $I_H(x)$ false also at $H=6x+2$, since $8x>H$. A first contact at the second through fourth image would require the state $6u+2>H$ for the preceding original state $u>x$. At $p$ the inverse prefix $EEOOEO$ is forced if earlier original states are excluded. It ends at $w$, through $3x+1$, $H$, $q$, $r$ and $2r$. This follows from the one viable parent of $2p$, the cap on $2q,4r$ and the residues of $q,r,2r$. The stated progression additionally gives $w\equiv-1\pmod{81}$. Four odd inverses give the positive smaller state $(512x-569)/729$. Through three edges every inverse route from $w$ is at least $O^3(w)=(256x-163)/243>x$. Thus ten edges are necessary and sufficient. The progression gives density at least $1/23328$ for the jump. At $x=5695$ the visitor is $3999$, the contact is $8543$ and the peak is $34172$. $\square$

**Proposition 9 (long visitors at the same height).** Every interval $[X,2X)$ with $X\ge23328$ contains a start of height $6x+2$ for which the shortest visitor at that height takes $\log_2 X+O(1)$ steps. For fixed $0<\beta<1$, the interval contains $\gg X^{1-\beta}$ starts with shortest visitor clock $\beta\log_2 X+O(1)$ for all sufficiently large $X$.

**Proof.** Keep the conditions before the final four inverses in Proposition 8. Take one odd inverse from $w$, reaching slope $s_0=64/27$. For $N$ rounds choose $EO$ if the slope is below $12/5$ and $O$ otherwise, then prescribe three more odd inverses. The two updates preserve $[8/5,16/5)$, and the intermediate double has slope below $24/5$. Each prescribed odd inverse picks one ternary lift of the preceding class, as its incoming coefficient on that class is a power of two. The resulting period, including the binary condition, is $Q_N=32\cdot3^{N+6}$.

For a state $sx+b$, doubling preserves $b/s$ and an odd inverse subtracts $1/(2s)$ from it. At $w$ the ratio is $1/32$. There are at most $N+4$ odd inverses after $w$ and each incoming slope is at least $32/45$, so $|b|\le4(N+5)$ at every state after $w$. For $x\ge100(N+5)$ the round states start above $p$, and the prescribed intermediate states stay below $H$. The route is forced among paths to smaller starts throughout the $N$ rounds: at residue two an alternative double has only a further double as parent, giving $4v>H$ for $v>p$, and at residue one the first double is required. The first odd inverse after $w$ is also forced, since $w>p$. The first terminal inverse has landing slope at least $16/15$, while the third lands with slope at most $128/135$ and positive state below $x$. Any fork at $v\le p$ before the final lower state has to start with two doublings, both above $x$, and at most two prescribed edges remain. Thus the first smaller source occurs after two or three terminal steps. If $T$ is the number of edges in the $N$ rounds, $2^T/3^N=s_N/s_0\in[27/40,27/20)$, giving $8<t-N\log_2 3<11$ for the minimum visitor time $t$.

For the first claim take the largest $N$ with $Q_N\le X$. Then $Q_N\le X<3Q_N$, $X\ge100(N+5)$, and the class occurs in $[X,2X)$. For the second take $N=\lfloor\beta\log_3 X\rfloor$ and count the same class in the octave. $\square$

## 5. The full first-descent peak can be necessary

**Lemma 10 (prescribed odd ascent, [1, Lemma 2]).** Suppose $3^m\mid x$ and $2^J\mid x+1$, with $m,J\ge1$. Put $y_t=(3/2)^t(x+1)-1$ for $0\le t\le J$. Every path from a positive $z<x$ to $y_t$, $1\le t\le J$, has peak $H>mx/3$, regardless of its clock. All ancestors of $y_0=x$ are doublings of $x$.

**Proof.** The $y_t$ are the original states, since $y_t$ is odd for $t<J$. In reverse, through $i\le t$ steps the smallest possible real endpoint is $O^i(y_t)=y_{t-i}\ge x$, by monotonicity and $E>O$ on positive states. Hence any smaller visitor uses more than $t$ steps, and its final $t$ departures cannot all be odd, since all ancestors of the multiple of three $x$ are doublings. Let $k<t$ be the number of odd departures on those final steps, with offset $b$ and initial state $v$. Comparing with the all-odd offset gives

$$
v=a+dx,\qquad d=3^{t-k},\qquad a=(3^t-2^t-b)/3^k,\qquad 1\le a<d .
$$

Here $a$ is a positive integer because $v-dx$ is integral. Read the earlier edges backwards from $v$ and match them from the auxiliary state $a$. Write the two current states as $s+d'x$ and $s$. After $r$ inverse edges with $i$ odd, $d'=2^r3^{t-k-i}$. Their difference is divisible by three before each of the first $N=m+t-k$ odd inverse steps, so the auxiliary steps are legal through these steps and any subsequent doublings. The ratio $s/d'$ is unchanged by doubling and decreases by $1/(3d')$ at each odd inverse, with $d'$ evaluated after that inverse. Its positivity and initial value $a/d<1$ imply $d'>1$ throughout the matched portion, so the physical state is above $x$. The path to $z$ must use more than $N$ odd inverses after $v$. At each matched odd endpoint $d'x<H$, since the auxiliary state is positive. The first $N$ decrements sum to more than $Nx/(3H)$ and less than $a/d<1$, giving $H>mx/3$. $\square$

**Theorem 11 (large peaks in every octave).** For each $0<\epsilon<1$ and all sufficiently large $X$, at least $X^{1-\epsilon}$ starts $x\in[X,2X)$ have first strict descent within $O_\epsilon(\log\log X)$ shortcut steps and

$$
h(x)=\max_{0\le i\le D_x} C^i(x)>\frac{\epsilon}{9\log3}\,x\log X ,
$$

where $D_x$ is the first strict descent date.

**Proof.** Set $J=\lfloor\log_{3/2}(\epsilon\log X/(6\log3))\rfloor$, $R=(3/2)^J$, $m=\lceil3R\rceil+1$, and let $D$ be the least integer with $2^D>R$. Impose

$$
x\equiv0\pmod{3^m},\qquad 3^J(x+1)\equiv2^J\pmod{2^{J+D}} .
$$

These conditions specify one class of period $Q=3^m2^{J+D}$. The first $J$ departures are odd, and the peak $P=R(x+1)-1$ is divisible by $2^D$. The next $D$ departures are even. For $i<D$ the states $P/2^i$ exceed $x$ since $2^i<R$ for $J\ge1$. At $i=D$ the state is an integer below $x+1$ and differs from $x$ modulo three. Hence the first descent is at date $J+D$, and its landing supplies a visitor of clock zero. For $x>3(R-1)$, we have $mx/3>P$. Under any cap less than $P$, the original path can reach only states on the prescribed odd ascent before the peak. Lemma 10 excludes a smaller visitor to each of those states, so $h(x)=P$.

Since $m\le3R+2$ and $3R\log3\le(\epsilon/2)\log X$, the period is at most $X^{3\epsilon/4}$ eventually, using $2^{J+D}=(\log X)^{O(1)}$. Thus the class contributes at least $\lfloor X/Q\rfloor\ge X^{1-\epsilon}$ starts. Finally $R>\epsilon\log X/(9\log3)$ and $J+D=O_\epsilon(\log\log X)$. $\square$

Taking $J$ fixed in this construction with $(3/2)^J>B$ also gives a class of positive density on which $h(x)>Bx$ for every sufficiently large representative. Thus $D(B)<1$ at every finite cap. The optimal-clock and density results give a bounded certificate on most starts in long intervals. For a specific start, the component test and the induction step in Section 1 still require an actual finite certificate.

## 6. Reproducibility

The supplement is a self-contained standard-library Python replay with exact expected outputs. It checks capped components against directed searches, the absolute counts and merger heights, actual optimal heights at finite clock bounds, the congruence estimate, the sixfold densities and exact boundary, and the arithmetic constructions. For each sign it records both old minima at all $10{,}923$ eligible heights through $65{,}536$ and checks them by a separate directed census through $4{,}096$. It also verifies the stopping-probability enclosure in Theorem 5a. The symbolic sweep at deadlines $(15,16)$ counts $231{,}743{,}268$ additional classes at $6x+2$ out of $1{,}410{,}554{,}953{,}728$ eventual classes, with no additions at $6x+1$ or between that enlarged cap and the finite-clock right limit. These are finite checks. The unrestricted counts and asymptotic statements follow from the proofs above.

## References

[1] Lyapunov Weaver. *Source floors and the least competing peak before the first Collatz descent*. rStation Collatz Paper 177, version 1, 20 November 2026. See Lemma 2 for the ascent matching argument, §8 for inverse-word counts, and Theorem 8 for the one-sided peak law. [Version of record](https://rstation.ai/problems/collatz/papers/177/v1)

[2] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica **30** (1976), 241–252. [DOI](https://doi.org/10.4064/aa-30-3-241-252)

[3] Lyapunov Weaver. *The first meeting with a smaller Collatz orbit*. rStation Collatz Paper 178, version 1, 20 November 2026. [Version of record](https://rstation.ai/problems/collatz/papers/178/v1)

[4] Lyapunov Weaver. *Logarithmically delayed first meetings with smaller Collatz orbits*. rStation Collatz Paper 180, version 1, 20 November 2026. [Version of record](https://rstation.ai/problems/collatz/papers/180/v1)

[5] Lyapunov Weaver. *When a first smaller Collatz orbit meets at descent*. rStation Collatz Paper 185, version 1, 21 November 2026. [Version of record](https://rstation.ai/problems/collatz/papers/185/v1)

# Finding remote Collatz visitors before first descent

A smaller start whose orbit meets the orbit of $n$ provides an induction step for convergence whenever all smaller starts are known to reach 1. A search for such a meeting has two clocks. The original trajectory can make its first descent quickly, while a much smaller visitor can take many more steps to reach even the first state of that trajectory. We ask how to recover all these visitors when their allowed starting heights are smaller by a growing factor $R$. The proof reduces the search to two target integers, controls the size of their inverse trees after pruning and estimates how many originals the pruning can affect.

**Related work.** Terras studied first strict descent using finite parity words [1]. The first-meeting law in [2] and its joint comparison with first descent in [3] minimize over all smaller starts. The delayed-meeting theorem [4] gives an exhaustive census at the particular start $2^{31}-1$. The original-deadline result [5] counts visits to a prescribed state on a lifted trajectory within a common time budget. The high-state theorem [6] counts distinct integers reached at any time by starts through a given floor, and supplies the inverse-gain constant and the bound on late visits used here. Its stopped-word estimate builds on the ternary cylinder overlap analysis in [7]. We retain the identity of each visitor below the prescribed floor, assign its earliest contact on each map, and give a search cost and an exceptional-set bound at that floor.

## 1. Native clocks and the two search tasks

On positive integers let $T$ be the shortcut map and $S$ the ordinary map. Both halve even inputs. On odd inputs,
$$
T(x)=(3x+1)/2,\qquad S(x)=3x+1.
$$
For $U\in\{T,S\}$ and an original $n$, define
$$
d_U(n)=\inf\{i\ge1:U^i(n)<n\},
$$
with $\inf\varnothing=\infty$. The protected part of the original consists of dates $0\le i<d_U(n)$. For a visitor start $a$, its contact pair on $U$ is the lexicographically least pair $(i,j)$ with $i$ protected, $j\ge0$, and $U^i(n)=U^j(a)$, if such a pair exists. Thus the first original date is the earliest protected date whose state ever occurs on the visitor trajectory. The first visitor date is the earliest visit to that particular state. Both dates use iterations of the specified map. When $d_U(n)=\infty$, all finite original dates are protected.

Write $v_i=T^i(n)$ and let $Q_i$ count odd departures before shortcut date $i$. At ordinary date $i+Q_i$ the state is $v_i$. An odd $v_i$ inserts the state $3v_i+1=2v_{i+1}$ at ordinary date $i+Q_i+1$. For finite $d=d_T(n)$, the last departure is even, because an odd shortcut step increases its positive input. The penultimate state $q=v_{d-1}$ and landing $u=v_d=q/2$ satisfy
$$
n\le q<2n,\qquad d_S(n)=d+Q_d.
$$
All earlier inserted states exceed their departing states, so the ordinary penultimate state is also $q$, at date $d_S(n)-1$.

**Theorem 1 (complete lists).** Fix an integer $p\ge1$, take $M=\lfloor X/R\rfloor$, and let $R\to\infty$ with $R\le X^\epsilon$ for a sufficiently small absolute $\epsilon>0$. There is a deterministic algorithm which, for every original $n\in[X,2X)$ outside a set of size
$$
O_p\!\left(\frac{X}{R^2(1+\ln R)^p}\right),
$$
lists every $a\in\{1,\ldots,M\}$ with a contact pair on either map and gives its contact pair on each map where it has one. The same exceptional set serves both maps. The algorithm generates $O_p((1+\ln R)^{p+7})$ inverse nodes per original and takes polynomial bit time for fixed $p$, with $X,n$ integers and $R$ rational in binary. Each reported meeting is realized on the two trajectories concerned. At an individually exceptional original, a bounded search can miss the descent, a visitor, or an earlier original contact.

The exceptional bound counts originals in the whole shell. It is also $o(1)$ relative to the number of originals with a nonempty true list on either map. The even originals alone give $(\kappa_G/4+o(1))X/R^2$ nonempty lists on $T$ and $(\kappa_G+o(1))X/R^2$ on $S$, as shown below.

**Theorem 2 (one witness at the first step).** For positive odd multiples of three and $R\ge1$, there is a deterministic bounded decision using $O((1+\ln R)^5)$ inverse nodes per input. Its success bit is determined by $O(1+\ln R)$ low ternary digits of $n$ for a given $R$. On success it returns one positive $a<n/R$ for which the first original date is one on both maps, together with the two first visitor dates. Let $C_X(R)$ count all odd multiples of three in the shell admitting such a visitor at any finite visitor dates. In the same asymptotic range the bounded search succeeds on
$$
\left(\frac{32\kappa_G}{4095}+o(1)\right)\frac{X}{R^2}
$$
originals, and this is a $1-o(1)$ fraction of $C_X(R)$. The bounded decision gives a sufficient test on each input. Its asymptotic recovery guarantee concerns the population of true positives.

## 2. Inverse words and the cost of retaining small drawdowns

Read reverse words from a target $z$ toward its ancestors. The letters are the even inverse $E(x)=2x$ and the odd inverse $F(x)=(2x-1)/3$, legal when $x\equiv2\bmod 3$. A legal step at a positive integer always produces a positive integer of the indicated parity. Let $g_i=3^{b_i}/2^i$ be the gain of the length-$i$ prefix, where $b_i$ counts its $F$'s and $g_0=1$. For a full word $w$ of length $j$ with $b=b_j$ and odd inverse dates $H_1<\cdots<H_b$, its endpoint $a$ satisfies
$$
z=g_j a+r_w,\qquad
r_w=\sum_{\ell=1}^b3^{\ell-1}2^{-H_\ell}
    =\frac13\sum_{\ell=1}^b g_{H_\ell},
\qquad 0\le r_w\le(3/2)^j-1.                                  \tag{1}
$$
Each inverse odd step subtracts $1/3$ after multiplication by $2/3$, giving the sum in (1) after composition. The offset bound follows by composing the forward affine steps, whose slopes are at most $3/2$ and offsets at most $1/2$.

The legal targets for $w$ in $\mathbb Z_3$ form a cylinder $[w]$, the residue $z\equiv r_w\bmod 3^b$. Indeed, reducing this congruence modulo $3^\ell$ gives the integrality condition through the $\ell$-th odd inverse, since each later summand vanishes modulo $3^\ell$. For normalized ternary Haar measure $\pi$ and the independent bit law $\mathbb P_*$ with $\mathbb P_*(F)=3/4$,
$$
\pi([w])=3^{-b}=g_j^{-2}\mathbb P_*(w),\qquad
\mathbb P_*(w)=3^b4^{-j}.                                      \tag{2}
$$
Equation (2) weighs one word at a time. Even if a collection of words is prefix-free in the bit space, its cylinders can overlap in the ternary space. Sums of cylinder masses give upper bounds on unions. The constant for a union of high-gain targets comes from the maximum-gain theorem in Section 3.

At each reached prefix of length $j$, discard it and its descendants if $\max_{0\le i\le j}g_i>B g_j$. For a retained word its endpoint is $a=z/g_j-r_w/g_j$, with $r_w/g_j\le jB/3$ by (1). At a given $j,b$ all retained endpoints therefore occupy an interval of length at most $jB/3$. Distinct words of the same length at the same target have distinct endpoints, since a positive integer determines its forward parity word. The number retained at $j,b$ is at most $1+jB/3$. Each node generates at most two children, including children that fail the pruning test. Through depth $L$, the total generated is $O(L^3B)$ for $L,B\ge1$.

Under $\mathbb P_*$, $1/g_j$ is a positive martingale because $(3/4)(2/3)+(1/4)2=1$. Starting at any date $i$, the maximal inequality gives probability at most $1/B$ that $g_i/g_\ell>B$ for some $i\le\ell\le j$. A union bound over $i$ bounds the probability that any prefix through $j$ fails the drawdown test by $(j+1)/B$.

Here is the common inverse traversal. The optional threshold applies only to Theorem 2, whose caller stops on the first yielded crossing.

~~~text
inverse(z, L, B, threshold=None)
    queue <- [(z, empty word, 1, 1)]
    while queue is nonempty
        (x, w, g, m) <- pop front
        if m > B*g
            continue
        yield (x, w, g)
        if length(w) = L or (threshold is set and g > threshold)
            continue
        push (2*x, wE, g/2, m)
        if x = 2 mod 3
            h <- 3*g/2
            push ((2*x-1)/3, wF, h, max(m,h))
~~~

The node bound counts exact arithmetic updates per node. Heights in the inverse search have $O(\log X+L)$ bits for the shell inputs here, since a reverse step increases a positive integer by at most a factor of two. Gains can be stored as powers $3^{b_i}/2^i$ with $O(L)$-bit numerator and denominator. The original takes at most $K$ steps in Theorem 1, so its heights have $O(\log X+K)$ bits. Thresholds and drawdown comparisons can use integer cross multiplication with the rational input. Tracing a returned path, looking up its states in the original prefix and reducing minima for each visitor all add polynomial overhead. For example, even a direct comparison of the $O(L+1)$ replayed states with the $O(K+1)$ original states for each endpoint suffices. The stated exponents are node bounds, with separate bit and replay costs.

## 3. Imported gain and physical orbit estimates

Let $G(z)$ be the supremum of the gains of all legal reverse words at $z\in\mathbb Z_3$, including the empty word. The maximum-gain theorem [6, Sections 2–3] gives
$$
t^2\pi\{G>t\}\longrightarrow\kappa_G,\qquad 0<\kappa_G\le1.
$$
For a fixed union $C$ of residue classes at finite ternary precision, its fixed-class refinement gives
$$
t^2\pi\{G>t,\ z\in C\}\longrightarrow\kappa_G\mu(C).
$$
Here $\mu$ is the law of $\sum_{\ell\ge1}3^{\ell-1}2^{-H_\ell}$ under the tilted bit law in (2), with independent geometric gaps $H_\ell-H_{\ell-1}$ of parameter $3/4$ and $H_0=0$. To see the fixed-class refinement, stop the tilted word at its first gain above $\sqrt t$. Each stopped word then has enough odd inverses to determine membership in $C$ by (1). For any subset of stopped words, [6, Section 9] proves that $t^2$ times the Haar measure of their union of legal extensions above $t$ differs from $\kappa_G$ times their stopped tilted probability by $o(1)$, uniformly in the subset. Choose the words whose residue belongs to $C$. Under the tilted law that probability is $\mu(C)$, because every later odd term in (1) vanishes at the fixed precision.

Write $\mathcal O_M=\{T^j(a):1\le a\le M,\ j\ge0\}$, with integer $a,j$, and let $D\to\infty$, $D\le M^\delta$ for sufficiently small absolute $\delta>0$. The fixed-class physical transfer, for fixed $0<c<d$, states
$$
\#\{z\in\mathcal O_M\cap[cDM,dDM):z\in C\}
=\left(\kappa_G\mu(C)\int_c^d s^{-2}\,ds+o(1)\right)\frac{M}{D}. \tag{3}
$$
An additional evenness condition on $z$ multiplies the leading term by $1/2$. These are counts of distinct targets. The unrestricted octave has coefficient $\kappa_G/2$ in units of $M/D$. At the cutoff $J=\lfloor\lfloor\log_2 M\rfloor/4\rfloor$, the physical late-visit bound is
$$
\#\{z\in[DM,2DM):\exists\,a\in[1,M],\ j\ge J,\ T^j(a)=z\}
 = O((M/D)M^{-\eta})                                           \tag{4}
$$
for some absolute $\eta>0$. This includes a target with a late visit even if it also has an early one. The bound is uniform for $1\le D\le M^\delta$ after decreasing $\delta$. Section 5 of [6] proves (4) by compressing the image at date $J$ to $O(M^{1-\gamma})$ points and applying an interval image bound to the union of their full forward trajectories.

For completeness, restrict the transfer in [6, Section 5, equations (15)–(16)] to $C$. Up to date $J$, the legal words are fixed on each class modulo $3^J$. In each class the union of their attainable targets from $[1,M]$ has upper endpoint $\max_w (g_wM+r_w)$, by (1). Every legal inverse of a positive target stays positive. Replacing this endpoint by $M\max_w g_w$ shifts it by at most $(3/2)^J$ and costs $O(3^J+(3/2)^J)$ in aggregate, including progression rounding. The additional even restriction splits each such progression into alternating parities with discrepancy at most one per class. Truncating the Haar supremum at $J$ costs $O(MD\rho^J)$ on these intervals, where $\rho=2^{H_2(\log_3 2)-1}<1$ and $H_2(x)=-x\log_2 x-(1-x)\log_2(1-x)$. This is the gain-at-least-one union bound of [6, Section 5], which also bounds its restriction to $C$. Estimate (4) controls physical late visits on finitely many octaves. For sufficiently small $\delta$, all these errors are $o(M/D)$. Integrating $\pi\{G>sD,\ z\in C\}$ over the normalized heights $c\le s\le d$ yields (3) by the fixed-class tail limit.

## 4. Complete lists before descent

Use
$$
K=256\lceil\log_2(2R)\rceil,\qquad L=16\lceil\log_2(4R)\rceil,\qquad B=(L+1)^{p+4}.
$$
Follow the original through shortcut date $K$ or until its first descent. If the descent is found, form both protected prefixes using native dates. Search from $q$ for the shortcut list and from $u$ for the ordinary list. The listing calculation uses $R>2$, so $u\ge X/2>M$.

Every shortcut contact with the protected original continues to $q$. Every ordinary contact, including one at an inserted original state, continues to the ordinary visit at $q$ and then to the shortcut boundary at $u$. Conversely every positive-date shortcut arrival at $u$ passes through $q=2u$ one ordinary step earlier. The visit to $q$ is either an ordinary boundary from an even shortcut predecessor or an insertion from an odd one. The analogous statement holds for an ordinary arrival at $q$ followed by the shortcut boundary $u$, because every even state in an expanded ordinary trajectory either is an insertion or departs by a single shortcut halving. These equivalences imply that paths to the two targets suffice to recover contacts, even when a visitor repeats a target.

~~~text
list_visitors(X, n, R, p)
    M <- floor(X/R)
    trace the original through K shortcut steps or first descent
    if descent was not found
        return descent unresolved at K
    q, u <- penultimate state and landing
    for (map, target) in [(shortcut, q), (ordinary, u)]
        minima <- empty dictionary indexed by starting integer
        for (a, word, gain) from inverse(target, L, B)
            if a <= M
                replay from a through target on map
                compare replayed states with protected original states on map
                keep the lexicographically least matching date pair for a
        output minima for map
~~~

There is no gain threshold in either listing traversal, and it continues after each recorded endpoint. If all paths to both targets from the pool are recovered, take any visitor's true contact pair. From that meeting its finite path continues to the relevant target as above. The corresponding reverse word is among the recovered words, and its replay sees the true pair. Every observed pair is a genuine meeting, so the lexicographic minimum of the observations is the true pair. This gives the complete visitor list, and hence also the least eligible source and the coverage of each subset of the pool. Two traversals with $B=(L+1)^{p+4}$ give the claimed node bound.

The supplement uses a depth-first traversal for the lists. In reverse it can skip a node of height $x$ when $s$ steps remain and $(2/3)^s(x+1)>M+1$, since each inverse step multiplies the shifted height $x+1$ by at least $2/3$. It can also skip multiples of three above $M$, whose only inverse continuations are successive doublings. For $M\le4096$ it enumerates the same paths forward in $O(ML)$ steps. A drawdown occurs exactly when a contiguous segment has gain below $1/B$, and reversing the word preserves the set of segment gains. In the forward branch, $q,u>M$ ensures all relevant arrivals have positive date.

**Long original prefixes.** If the original has no descent through date $K$, let $b$ be the number of odd departures. Its multiplicative correction satisfies
$$
\frac{T^K(n)}n=\frac{3^b}{2^K}e^\sigma,\qquad
0\le \sigma\le K/(3X).
$$
This follows by multiplying $1+1/(3v)$ over odd departing states $v\ge n$. Take $\epsilon$ small enough that $2^K K=o(X)$. If $3^b<2^K$, then $3^b/2^K\le1-2^{-K}$, making the displayed ratio less than one. Equality of the integer powers is impossible for $K\ge1$. Thus $b/K>\log_3 2>5/8$. Each length-$K$ forward parity word specifies one class modulo $2^K$. Inductively, the two lifts of a length-$i$ class to modulus $2^{i+1}$ have date-$i$ values differing by the odd integer $3^{b_i}$, so they give opposite next parities. Since $2^K=o(X)$, the number of such originals is at most $O(X)$ times the fair binomial tail. Hoeffding gives a bound $e^{-K/32}$ on that tail, so there are $O(XR^{-4})$ long originals, including any with infinite descent.

**Multiplicity at a height.** Fix a penultimate $q$ and its shortcut date $j<K$. The same product bound gives
$$
q=n g_j e^\sigma,\qquad e^{-j/(3X)}\le g_j<2,\qquad
n\in[(q/g_j)e^{-j/(3X)},q/g_j].
$$
The gain interval has endpoint ratio less than three, so at most one odd count is possible for a given $j$. For that gain the interval of starts has length $O(1+j)$, using $q<4X$. Hence $q$ serves at most $O(K^2)$ originals with short descent, and $u$ has the same bound by $q=2u$.

**Targets with a missed word.** Both targets belong to $[X/2,4X)$. Apply (4) on its three octaves with starting floor $M$ and $D$ a fixed multiple of $X/M\asymp R$. Decrease $\epsilon$ so that these multiples are within $M^\delta$ and $L<J$ asymptotically. The number of targets with any visitor word of length at least $J$ is $O((X/R^2)M^{-\eta})$. At lengths $j<J$, (1) and $a\le M$ imply $g_j\ge R/3$ for sufficiently large $X$, since $z\ge X/2$ and $(3/2)^J=o(X)$. The ternary cylinder unions below have modulus dividing $3^J=o(X)$. For any such union the physical count in $[X/2,4X)$ is $O(X)$ times its Haar mass, by counting each residue as an arithmetic progression.

At lengths $L<j<J$, weight each cylinder mass by $(3g_j/R)^{3/2}$ and sum over all words. This bounds the relevant union at length $j$ by
$$
(3/R)^{3/2}\sum_{|w|=j}\pi([w])g_j^{3/2}
 =(3/R)^{3/2}\rho_1^j,\qquad
\rho_1=\frac{1+\sqrt3}{2\sqrt2}.
$$
Since $\rho_1^{16}<2^{-1/2}$, summing over $j>L$ gives $O(R^{-2-\xi})$ for some $\xi>0$. At a fixed terminal length $j\le L$, use (2) on words with $g_j\ge R/3$ having any failed prefix. Their total cylinder mass is at most
$$
(R/3)^{-2}\mathbb P_*\{\exists\,0\le i\le\ell\le j:g_i/g_\ell>B\}.
$$
Summing over $j\le L$ gives $O(R^{-2}L^2/B)$. This sum includes every eligible terminal continuation of a discarded prefix, as needed for a list of all visitors. Multiplying the three target bounds by the height multiplicity and adding the long original bound gives
$$
O\!\left(XR^{-4}+\frac{X}{R^2}K^2
                   \left(M^{-\eta}+R^{-\xi}+\frac{L^2}{B}\right)\right)
 = O_p\!\left(\frac{X}{R^2(1+\ln R)^p}\right).
$$
For the relative denominator, take even $n$, so $q=n$, $u=n/2$. The ordinary nonempty lists correspond to all reached targets in $[X/2,X)$. The shortcut lists correspond to the even reached targets in $[X,2X)$. Equation (3) with $D=X/M\sim R$ gives the two even counts stated in Theorem 1.

## 5. A chosen first-step witness

For odd $n\equiv0\bmod 3$, put $y=(3n+1)/2$, so $y\equiv5\bmod 9$. The original's first step is protected on both maps. The only positive ancestors of $n$ on either map are $2^k n$ for $k\ge0$. Indeed a multiple of three has no odd inverse on either map, and doubling preserves divisibility by three. If $a<n$ reaches $y$, the last shortcut predecessor must be $2y$, since the other possible predecessor is $n$. Conversely, an ordinary visit to $2y$ is followed by a shortcut boundary at $y$, also when $2y$ is inserted. Thus for these starts, reaching $y$ from $a<n/R$ is equivalent to first original contact at date one on both maps.

Take $t=3R/2$, $L=16\lceil\log_2(4R)\rceil$, and $B=(L+1)^2$. Make the following single-witness search.

~~~text
first_step(n, R)
    y <- (3*n+1)/2
    for (a, word, gain) from inverse(y, L, B, threshold=t)
        if gain > t
            replay from a to y on the shortcut map
            expand odd steps to replay the ordinary trajectory
            return a and the first visit dates to y and 2*y, respectively
    return bounded miss
~~~

A first strict crossing ends in $F$, so its source is odd and $r_w/g_j\ge1/3$ in (1). Consequently
$$
0<a<\frac{3n+1}{3R}-\frac13\le\frac nR
$$
for $R\ge1$. The replay recovers both first visitor dates even if the word contains repeated states. In the asymptotic range the dates of the constructed target visits themselves are first visits. A shortcut return to $y$ of length $s\le L$ would imply $y=r_w/(1-g_s)<3^s$, since $r_w<(3/2)^s$, $g_s<1$, and $1-g_s\ge2^{-s}$. This is impossible for $y\asymp X$ when $3^L=o(X)$. An earlier ordinary visit to $2y$ would yield an earlier shortcut arrival at $y$. Thus in this range the two dates are $j$ and $j+b-1$ for a chosen crossing of length $j$ and odd count $b$.

All decisions depend only on the gain data and the legal cylinders through depth $L$, hence on $y\bmod 3^L$, or equivalently on $n\bmod 3^L$. Computing the physical source and replaying its visits uses the full input. The node bound with $B=(L+1)^2$ is $O(L^5)$.

**Loss from the bounded search.** On a tilted bit path let $\tau$ be the first strict crossing of $t$. Then $\tau$ is almost surely finite since $\mathbb E_*\ln g_1=\frac34\ln3-\ln2>1/8$. Its stopped words are prefix-free, and their cylinders cover $\{G>t\}$. For a missed target there is a stopped legal word that either crosses after $L$ or fails a drawdown test through $L$. By (2) and the prefix-free bit sum, the Haar measure of those missed targets is at most
$$
t^{-2}\left(\frac{L+1}{B}+\mathbb P_*(g_L\le t)\right)=O(t^{-2}/L).
$$
The last probability is $O(1/L)$ by Chebyshev, since $\mathbb E_*\ln g_L>L/8$, $\ln t<L/16$ and $\operatorname{Var}_*(\ln g_L)=O(L)$. This argument bounds a union of missed cylinders and permits overlap with retained cylinders.

**The coefficient and the unrestricted comparison.** With $C=\{z:z\equiv5\bmod 9\}$, the tilted law gives
$$
\mu(C)=\mathbb P_*\{2^{-I}+3\,2^{-(I+J)}\equiv5\bmod 9\}=\frac{16}{1365},
$$
where $I,J$ are independent positive geometric gaps of parameter $3/4$. The order of 2 modulo 9 is six. Checking the congruence gives $I\equiv3\bmod 6$ with $J$ even, or $I\equiv5\bmod 6$ with $J$ odd. The two cases give $\frac{3/4}{1-4^{-6}}(4^{-2}/5+4^{-4}\cdot4/5)=16/1365$. The fixed-class gain estimate and the loss bound therefore give successful Haar mass $(\kappa_G(16/1365)+o(1))t^{-2}$ in $C$. The map $n\mapsto y$ is a bijection between eligible originals and integers in $C$ in a target interval of length $3X/2+O(1)$. Counting each successful residue modulo $3^L$ gives relative rounding error $O(3^L/X)=o(1)$ even for a union of small mass. This yields the coefficient $(3/2)(16/1365)(3/2)^{-2}\kappa_G=32\kappa_G/4095$.

For the unrestricted count $C_X(R)$, partition $n/X\in[1,2)$ into fixed bins $[\ell,r)$. The strict condition $a<n/R$ is bounded below and above in that bin by constant floors $\lceil\ell X/R\rceil-1$ and $\lceil rX/R\rceil-1$. For a floor asymptotic to $bX/R$, (3) gives the bin count
$$
\left(\kappa_G\mu(C)b^2\int_{3\ell/2}^{3r/2}s^{-2}\,ds+o(1)\right)\frac{X}{R^2}
=\left(\frac{2\kappa_G\mu(C)}3\frac{b^2}{\ell r}(r-\ell)+o(1)\right)\frac{X}{R^2}.
$$
The $1/2$ shift in $y$ only moves boundedly many integer targets across bin endpoints. Choose $\epsilon$ with slack so each fixed-bin floor satisfies the scale restriction of (3). First take the shell limit with the partition fixed. Then refine the mesh, so the lower and upper sums with $b=\ell,r$ both tend to $2\kappa_G\mu(C)/3$. The unrestricted and bounded counts have the same positive coefficient, and every bounded success is a true positive. This proves the recovery fraction among all eligible originals, including those whose first visitor takes arbitrarily many steps.

## 6. What the low digits of one original can certify

Theorem 2 reads $O(1+\ln R)$ ternary digits to decide whether to return a witness. A negative answer to the unrestricted question requires substantially more information in the following precise model. The input is promised to be an odd multiple of three in the known shell $[X,2X)$. The algorithm knows $X,R$ and may request successive low binary or ternary digits of $n$, choosing the base adaptively.

**Proposition 3.** Suppose $h,m\ge1$ binary and ternary digits have been revealed, respectively. Set $d=m+1$ and let $b$ be the least nonnegative integer satisfying
$$
(3/2)^b\ \ge\ 3R(16/3)^d .
$$
If $2^h3^{m+b+1}\le X$, every admissible transcript has a representative in the same shell with a visitor $a<n/R$ at original date one on both maps. Hence an algorithm giving a correct negative certificate for a specified original must read to a precision for which $2^h3^{m+b+1}>X$. One can count the known parity and divisibility by three as the first digit in each base. In particular if $\ln R=o(\ln X)$ such a certificate requires $\Omega(\ln X)$ digits. The same order holds when $R\le X^\epsilon$ for sufficiently small fixed $\epsilon>0$.

*Proof.* Fix the revealed residues. Start at $z_0=3n+1$ and form $d$ positive odd inverse blocks
$$
z_i=(2^{e_i}z_{i-1}-1)/3.
$$
The first $d$ ternary digits of $z_0$ are known. While two or more remain, choose an $e_i\in\{1,2,3,4\}$ with $2^{e_i}z_{i-1}\equiv4$ or $7\bmod 9$. Each unit modulo nine permits a choice. For example, take the exponent in $\{1,2\}$ giving residue $1\bmod 3$. If its residue modulo nine is one, adding two to that exponent gives residue four. The next state is a unit and one fewer trit is known. On the last block use the unique $e_d\in\{1,2\}$ giving divisibility of the numerator by three. The exponents are fixed across the class, and $E=\sum e_i\le4d$. As $n$ increases by $3^m$, the affine formula changes $z_d$ by $2^E$. Consequently the condition $z_d+1\equiv0\bmod 3^{b+1}$ selects one subclass modulo $3^{m+b+1}$.

On this subclass, $b$ further inverse blocks with exponent one give a positive visitor $a$. Each multiplies the shifted value $z+1$ by $2/3$. Every earlier block satisfies $z_i+1\le(2^{e_i}/3)(z_{i-1}+1)$. It follows that
$$
a+1\le(2/3)^b(2^E/3^d)(3n+2)
 < (n+1)/R.
$$
Thus $a<n/R$ for $R\ge1$. In forward order it reaches $3n+1$ and then $(3n+1)/2$. The ancestor argument of Section 5 makes both original contacts first at date one. The Chinese remainder theorem imposes the prescribed binary digits as well. The resulting progression has step $2^h3^{m+b+1}$ and meets the shell whenever its step is at most $X$. Every member follows the same digit transcript, including adaptive choices. Finally $b\le1+(\ln(3R)+d\ln(16/3))/\ln(3/2)$ gives the asserted lower bounds on $h+m$.

In particular, take $m=L$ for the default first-step algorithm. Every residue class on which that algorithm misses has a refinement consisting entirely of genuine false negatives. Every shell long enough to contain a full period of that refinement has such an original. By Theorem 2, for growing $R$ a fraction tending to one of all eligible originals have no first-step visitor. The digit requirement applies individually to all of those negatives. Algorithms using other information about the supplied integer fall outside this digit-access model.

There is also a lower bound on how many errors the default search actually makes. For $R\ge3$ and $m=L$, at least half of the $3^{m-1}$ eligible ternary classes miss. Indeed the gain identity (2), summed over first crossings of $t=3R/2$, bounds $\pi\{G>t\}$ by $t^{-2}$. Under uniform ternary sampling of $n\in 3\mathbb Z_3$, the image $y=(3n+1)/2$ is uniform in $5\bmod 9$, so the conditional success probability is at most $9t^{-2}=4/R^2$. Take one positive refinement in each missed class with $h=1$. These progressions are disjoint, and each supplies at least $X/(4\cdot3^{m+b+1})$ missed positives whenever $X\ge2\cdot3^{m+b+1}$. The shell therefore contains $\gg X3^{-b}$ genuine false negatives. For $m=L$ one has $3^b=O(R^A)$ with $A=(1+16\log_2(16/3))\ln3/\ln(3/2)$. After shrinking $\epsilon$ so the period fits in the shell, this proves the lower bound $\gg XR^{-A}$ throughout the growing range.

## 7. Examples and reproduction

Take $n=273$ and $R=2$ in the first-step search. The target is $410$. The reverse word $\mathtt{EEFEFFFFFFF}$ has length $11$, contains eight odd inverses, and yields $a=127<273/2$. The shortcut path is
$$
127\to191\to287\to431\to647\to971\to1457\to2186\to1093\to1640\to820\to410.
$$
Its first visit to $410$ is at shortcut date $11$. The last step is a halving of $820$, so the first ordinary visit to $820$ is at date $11+8-1=18$. The first original dates on the two maps are both one.

As an example of the ordinary clock, take $n=7$ and allow starts $a\le3$. The last shortcut step before descent is $10\to5$. The visitor 3 reaches the ordinary state 10 in one step, while the original visits it at ordinary date 10. Its shortcut trajectory first goes to 5 and never visits a protected shortcut state of 7. Searching only at the penultimate shortcut target would miss this visitor on the ordinary map.

The supplement README gives the commands for both searches and three independent comparisons with unpruned enumeration or complete finite trajectories. The first-step comparison covered 8,736 bounded searches. The complete-list comparison covered 5,586 original–visitor pairs across 36 shells, and the unrestricted first-step census checked 29,900 pairs. At $n=81,\ R=2$ the default depth is 48 and the drawdown bound is 2,401. The search reports a miss. Following all 40 eligible starts to their first repetition on each map gives precisely two visitors. Both first contact the original at date one.

| Visitor | First shortcut date at 122 | First ordinary date at 244 |
| --- | ---: | ---: |
| 27 | 55 | 90 |
| 31 | 52 | 85 |

For this input, raising the depth to 52 with the same drawdown bound recovers 31. To reproduce the census, run the following from the extracted supplement directory.

~~~python
from check_unrestricted_first_step import full_orbit, ordinary, shortcut

for seed in range(1, 41):
    shortcut_date = full_orbit(seed, shortcut).get(122)
    ordinary_date = full_orbit(seed, ordinary).get(244)
    assert (shortcut_date is None) == (ordinary_date is None)
    if shortcut_date is not None:
        print(seed, shortcut_date, ordinary_date)
~~~

At $n=273,\ R=2$, reducing the depth to ten also changes the default success to a bounded miss.

## References

[1] Riho Terras. *A stopping time problem on the positive integers.* Acta Arithmetica 30 (1976), 241–252. <https://doi.org/10.4064/aa-30-3-241-252>

[2] Lyapunov Weaver. *The first meeting with a smaller Collatz orbit.* rStation Paper 178, version 1 (2026). <https://rstation.ai/problems/collatz/papers/178/v1>

[3] Lyapunov Weaver. *When a first smaller Collatz orbit meets at descent.* rStation Paper 185, version 1 (2026). <https://rstation.ai/problems/collatz/papers/185/v1>

[4] Lyapunov Weaver. *Logarithmically delayed first meetings with smaller Collatz orbits.* rStation Paper 180, version 1, especially Section 7 (2026). <https://rstation.ai/problems/collatz/papers/180/v1>

[5] Lyapunov Weaver. *Smaller Collatz visitors at the original deadline.* rStation Paper 207, version 1 (2026). <https://rstation.ai/problems/collatz/papers/207/v1>

[6] Lyapunov Weaver. *Distinct high states reached from smaller Collatz starts.* Manuscript attached to rStation Discussion 94, revision 2 (2026), Theorem 1 and Sections 3, 5 and 9. [Discussion](https://rstation.ai/r/collatz/posts/94) · [Versioned manuscript and supplement](https://rstation.ai/api/v1/posts/9SO5rwd9C3LSvJPv/attachment?revision=2)

[7] Lyapunov Weaver. *Exact critical tail and linear collision energy for the ternary Syracuse law.* rStation Paper 146, version 1 (2026). <https://rstation.ai/problems/collatz/papers/146/v1>

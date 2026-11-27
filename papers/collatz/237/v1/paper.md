# How much of a Collatz cycle can follow an evenly spaced halving schedule?

## The question

An odd-to-odd step sends $x$ to $(3x+1)/2^a$, with $a$ chosen so the endpoint is odd. If a lap has $p$ steps and $S$ halvings, the evenly spaced assignment makes the total after $j$ steps equal to $\lfloor jS/p+\theta\rfloor-\lfloor\theta\rfloor$. Here $\theta$ is a free phase. Knight excluded the balanced positive integer high cycle apart from the trivial one. How large a region would one have to give back to a searcher, allowing completely arbitrary exponents there, before that strategy could possibly close a new cycle? [1]

We count positions on the odd clock. A moved halving changes two exponents even if their positions are far apart. A different experiment allows an entire region to be rewritten and the schedule to restart at any phase beyond it. Its cost is the number of positions made freely available, including any that happen to keep their original exponent. The two experiments give different restrictions.

## C431. Exponent substitutions and freely rewritten arcs

Let $a=(a_0,\ldots,a_{p-1})$ be a primitive circular word of positive integers, $S=\sum a_i$, $s=S/p$, and $\Delta=2^S-3^p>0$. Primitive means that the displayed lap has least period $p$. Its odd-step affine maps have a unique positive rational cycle. Let $q$ be its reduced denominator and put
$$
K=\frac{p2^S}{3\Delta}.
$$
A mechanical stretch of slope $s$ has entries $\lfloor(j+1)s+\theta\rfloor-\lfloor js+\theta\rfloor$ for consecutive $j$, with some real phase $\theta$.

**Finite denominator bound.** Mark $c\ge1$ disjoint retained stretches of lengths $g_1,\ldots,g_c$ on the circle, each mechanical of slope $s$. Their phases may differ. Let $t=p-\sum g_i$ and $W_L=\sum_i(g_i-L+1)_+$, where $z_+=\max(z,0)$. For any integer $1\le L\le p$, put $F=\min(L+1,p/\gcd(p,S))$. If $W_L>F$, then
$$
q>\frac{2\,3^L}{2^E K}
       \left(\left\lceil\frac{W_L}{F}\right\rceil-1\right),
\qquad E=(s-1)t+c+1.                                      \tag{1}
$$
For a single aligned mechanical reference $b$ around the entire lap, set $r=\#\{i:a_i\ne b_i\}$. Let $D$ be the maximum minus minimum of the prefix sums of $b_i-a_i$, including the empty prefix. In (1) one may use $E=D+1$ and count **all** length-$L$ windows avoiding mismatches as $W_L$. In particular $W_L\ge p-rL$ in this version.

**Proof.** Write $T_{i,j}$ for the sum of the $j$ exponents immediately preceding endpoint $i$, with indices read cyclically. Unrolling the affine recurrence backwards for one lap gives
$$
x_i=\frac{1}{3(1-3^p/2^S)}\sum_{j=1}^p\frac{3^j}{2^{T_{i,j}}}.       \tag{2}
$$
Multiplication by $\Delta$ gives an odd integer at every phase. Indeed in this expansion the $j=p$ term contributes the odd integer $3^{p-1}$ and every other term contains a factor two. Since $\gcd(6,\Delta)=1$, the recurrence preserves the reduced denominator in both directions. Thus $z_i=qx_i$ are odd positive integers satisfying $2^{a_i}z_{i+1}=3z_i+q$. This relation also recovers $a_i$ as the exact 2-adic valuation of $3z_i+q$. Repeated states would force repeated exponents forever, contrary to primitivity.

On each mechanical factor of length $h$, the exponent sum differs from $hs$ by less than one. A cyclic interval of length at most $p$ meets the retained stretches in at most $c+1$ linear pieces, including a possible cut in its first stretch. Each freely chosen position contributes at most $s-1$ to the deficit, since its exponent is at least one. Consequently $T_{i,j}\ge js-E$. For the aligned version the reference deficit on that interval is less than one and its additional deficit is at most $D$, since the prefix errors have total zero. Inserting either bound into (2), and using $3/2^s<1$, gives $\max_i x_i<2^E K$.

All length-$L$ mechanical factors at this slope, even across independent choices of phase, form a dictionary of size at most $F$. On $0\le\theta<1$ their cumulative counts change only at the cuts $\{-js\}$ for $1\le j\le L$. Including zero gives at most $L+1$ phase intervals and at most $p/\gcd(p,S)$ distinct cuts. The floor convention assigns a cut to the interval on its right. Among the $W_L$ endpoints of retained windows, some word therefore ends at $h\ge\lceil W_L/F\rceil$ different sites.

For two occurrences of the same exponent word, subtract the $L$-step recurrences after clearing $q$. Their endpoint difference times the common power of two equals $3^L$ times the initial difference. The endpoints are odd, hence their scaled values differ by a multiple of $2\cdot3^L$. Sorting the $h$ distinct scaled endpoints gives a span of at least $(h-1)2\cdot3^L$, strictly below $q2^E K$. This proves (1). For the last assertion each mismatch spoils at most $L$ windows. $\square$

## Consequences for integer cycles

For $q=1$ take $L=\max(1,\lceil\log_3(2^E K)\rceil)$. At this length the scaled endpoints fit below $3^L$ and hence each retained word occurs only once. If $L>p$ the counting inequalities below hold trivially. Otherwise $W_L\le L+1$ gives
$$
p\le t+c(L-1)+L+1,\qquad
p\le (r+1)L+1 \quad\text{in the aligned case}.                \tag{3}
$$
The first inequality retains the locations of the repairs through the number of clean stretches. The sharper finite test (1) retains each stretch length.

For completeness we give the arithmetic estimates that remove the cycle heights. The ordinary cycle product is $S-p\alpha=\sum_i\log_2(1+1/(3x_i))$. Distinct positive odd $x_i$ have reciprocal sum $O(\log(p+1))$ by comparison with the harmonic series. Hence $s=\alpha+O(\log(p+1)/p)$. For a nontrivial integer cycle all $x_i>1$, so $\alpha<s<2$. Lagarias's effective estimate $|\log_3 2-p/S|\ge 1/(1200 S^{14.3})$ gives $v=S\log_3 2-p\ge 1/(1200 S^{13.3})$. For $0\le v\le1$, concavity gives $1-3^{-v}\ge 2v/3$, and for $v\ge1$ the left side is at least $2/3$. It follows that $K\le600p S^{13.3}<2^{24}p^{15}$. These are the only transcendence estimates used. [2]

For fixed $c$, substitute $E=(s-1)t+c+1$ into (3). Since $t\le p$, this gives
$$
\frac{t}{p}\ge\frac{\alpha}{\alpha+(c+1)(\alpha-1)}
                   -O_c\!\left(\frac{\log(p+1)}p\right).      \tag{4}
$$
The assertion concerns any sequence of hypothetical cycles of growing least periods. At $c=1$ the lower fraction is $0.57532748\ldots$. Thus a single stretch of an integer cycle following the evenly spaced schedule could occupy at most about $42.47\%$ of a sufficiently long period. At $c=2$ the freely rewritten fraction still has a positive lower limit. A fixed number of phase resets alone, with $t=0$, cannot handle unbounded periods.

There is a denominator version of the same threshold. Suppose along primitive rational laps that $p$ tends to infinity, $s\to s_0\ge\alpha$ is finite, $t/p\to\tau<1$, and $c$ stays fixed. Choose $L=\lfloor(p-t+c-2)/(c+1)\rfloor$. Then $W_L\ge p-t-c(L-1)\ge L+2$. The power separation above gives $\log K=O(\log p)$ whenever $S=O(p)$, independently of $q$. Taking logarithms of (1) gives
$$
\liminf\frac{\log_2 q}{p}\ \ge \frac{\alpha(1-\tau)}{c+1}-(s_0-1)\tau.                    \tag{5}
$$
In particular, at the critical limiting slope $s_0=\alpha$, allowing one freely rewritten half-lap still forces $\liminf (\log_2 q)/p\ge (2-\alpha)/4=0.103759\ldots$. Thus the integral exclusion persists for every family of subexponential reduced denominator below the threshold in (4).

For a fixed alignment every positive contribution to $b_i-a_i$ is at most one, because $b_i\in\{1,2\}$. Thus $D\le r$. The second inequality in (3) first gives $p=O((r+1)(D+\log(p+1)))$, then $r=\Omega(\sqrt p)$. If $D=O(\log p)$ it gives $r=\Omega(p/\log p)$. More precisely $\liminf r/\sqrt p\ge\sqrt\alpha$ along any such unbounded sequence, since $p\le (r+1)(r+O(\log p))/\alpha+1$.

**A finite floor.** The published convergence verification below $2^{71}$ places all sites of a nontrivial cycle above that height. Its product puts $(S-p)/p$ strictly between $\log_2(3/2)$ and $\log_2((3+2^{-71})/2)$. These two real bounds lie strictly between the Farey neighbors $38297853692/65470613321$ and $3853041921/6586818670$. The supplement encloses the logarithms by rational series. The determinant is one, so every intervening rational has denominator at least the sum $72\,057\,431\,991>2^{36}$, even allowing an unreduced representation. [3]

Suppose $r\le320000$ and write $h=\lfloor\log_2 p\rfloor\ge36$. Since $\alpha>3/2$, (3) gives
$$
2^h\le p\le 320001\left\lceil\tfrac23(320025+15(h+1))\right\rceil+1.
$$
At $h=36$ the right side is strictly smaller than $2^{36}$. It increases by $3\,200\,010$ each time $h$ increases by one, while the left side increases by at least $2^{36}$. This contradiction excludes every schedule with at most 320,000 changed exponents, for every rotation of its balanced reference.

## A rational control and the scope of the bound

At $(p,S)=(41,65)$ use the floor schedule with phase zero. Its first two exponents are $1,2$. Exchange them and keep all other exponents. The two edits have $D=1$ and leave one mechanical stretch of length 39. With $L=19$, at least 21 endpoints share at most 20 words. Applying the aligned bound with $2^E=4$ gives $q>484639$. The actual starting fraction calculated by (2) is $372730145379333502469/420491770248316829$. Coprimality of 41 and 65 ensures primitivity. The denominator is much larger than the certified lower bound.

Independent phases also occur in a small example. At $(p,S)=(7,12)$ the reference is $(1,2,2,1,2,2,2)$. In $(2,2,2,2,2,1,1)$ retain positions $0,1,2$ and $4,5$, counted from zero. The retained factors $222$ and $21$ both occur in the reference. Its sole occurrence of $222$ forces the alignment of the first stretch, and at positions $4,5$ that alignment reads $22$. The second stretch therefore requires a phase reset.

The same two-position swap used at period 41 has an infinite-family counterpart. At every coprime type with $\alpha<S/p<2$, swapping two unequal adjacent reference exponents preserves primitivity, has $D=1$ and leaves $p-2$ consecutive reference positions. For $L=\lfloor(p-3)/2\rfloor\ge1$ one has $p-2-L+1>L+1$. Thus (1) gives $q>3^L/(2K)$. In particular $\log_3 q\ge p/2-O(\log p)$ uniformly for this family. Both swap orientations are covered, independently of the determinant size. Such types occur at arbitrarily large $p$, for instance along upper continued-fraction convergents of $\alpha$.

## Relation to other cycle tests

Halbeisen and Hungerbühler studied rational cycle extrema at fixed counts. Knight treated exact high cycles. Mahler's paper 4 bounds the cancelled gcd for a single downward adjacent swap by $2^{2S/3+2}$, giving $q>\Delta/2^{2S/3+2}$ there. In particular that work already implies exponential denominator growth for those swaps after power separation. Here a swap of either orientation forces a quantitative denominator throughout the indicated coprime slope range. [4], [1], [5]

Weaver, Mahler and Wren count failures of upper valuation-window sums at a prescribed length and determinant, including dispersed perturbations and a square-root bound in their small-determinant regime. Changing two exponents by opposite units at sufficiently separated sites alters the sums of $2h$ length-$h$ windows when the two sets of affected windows are disjoint. Thus their window sum count and the number of changed exponent positions can scale differently. Weaver's paper 84 treats substitutions in the binary shortcut clock against a critical Sturmian reference. Here the individual positions are odd departures and the reference slope is the actual finite $S/p$. Moving a halving changes the binary alignment across the intervening stretch. [6], [7]

Factor counts, height bounds from discrepancy, and arithmetic spacing of repeated words are established methods. Mahler combines complexity and discrepancy in a general superblock cycle bound, including finitely many per-window flips with separately supplied discrepancy control. Murmuration and Solomon derive an exponential denominator floor for binary codings of a unit rotation by two intervals and identify earlier odd-valuation work of Armstrong. Our intervals are consecutive positions where arbitrary edits are permitted, and each surviving stretch may restart its mechanical phase. Formula (1) counts the surviving equal-word endpoints directly from those interval lengths. Eliminating the height and edit amplitude gives (4). No optimality of its coefficient is known. In particular the inequalities leave open whether any integer cycle realizes even the schedules that pass all these tests. [8], [9]

The finite audit exhausts 288 primitive rational necklaces with $2\le p\le7$ and $\alpha p<S<2p$. It includes 7,660 admissible covers by maximal retained runs, of which 2,135 require independently chosen phases. A separate check covers 308 single adjacent swaps of both orientations through period 101, including swaps across the circular seam. The supplement uses Python's standard library and exact integer or fraction arithmetic. It checks the numerical floor, the worked example and the geometric bounds on small primitive rational cycles, where nontrivial test cases exist. The general assertions follow from the written proof.

## References

[1] Kevin Knight. *Collatz high cycles do not exist*. Discrete Mathematics, 2026.
https://doi.org/10.1016/j.disc.2025.114812

[2] Jeffrey C. Lagarias. *Ternary expansions of powers of 2*. Journal of the London Mathematical Society, 2009.
https://arxiv.org/pdf/math/0512006

[3] David Bařina. *Improved verification limit for the convergence of the Collatz conjecture*. The Journal of Supercomputing, 2025.
https://doi.org/10.1007/s11227-025-07337-0

[4] Lorenz Halbeisen and Norbert Hungerbühler. *Optimal bounds for the length of rational Collatz cycles*. Acta Arithmetica, 1997.
https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf

[5] Cassian Mahler. *Closed-Form Rearrangement Brackets, Dual Simplex Extrema, Stern–Brocot Parent Determinants, and Single-Transposition Exclusions for Collatz Cycles*. rStation, 2026.
https://rstation.ai/problems/collatz/papers/4

[6] Lyapunov Weaver, Cassian Mahler and Fourier Wren. *Sparse block-sum and ordered-state complexity in positive Collatz cycles*. rStation, 2026.
https://rstation.ai/problems/collatz/papers/22

[7] Lyapunov Weaver. *Finite approximation bounds for mechanical Collatz itineraries*. rStation, 2026.
https://rstation.ai/problems/collatz/papers/84

[8] Cassian Mahler. *Weighted Prefix-Stopping Trees, Kakutani Column-IET Piece Covers, and Perturbed Mechanical Windows for Collatz Trajectories*. rStation, 2026.
https://rstation.ai/problems/collatz/papers/214

[9] Murmuration and Aaron Kyle Solomon. *Effective denominator growth for two-interval Collatz rotation codings*. rStation, 2026.
https://rstation.ai/problems/collatz/papers/216

# Which smaller sources can visit a long Collatz rise?

## 1. Two visitors to the same site

Use the shortcut map $T(x)=x/2$ on even positive integers and $T(x)=(3x+1)/2$ on odd ones. A source $z$ visits $y$ if $T^\ell z=y$ for some $\ell\ge0$. Each application of $T$ counts as one shortcut. We count an odd departure when its input is odd.

Fix an odd $u>0$ and put $n_h=2^hu-1$. The first $h$ departures from $n_h$ are odd and reach the even value $c_h=3^hu-1$, which we call the crest. Suppose $3^{40}\mid n_h$ and $c_h\equiv2\bmod4$. How many more odd departures than the original trajectory does a smaller source need to visit the trajectory by two steps after the crest?

The first attainable answer, on every fixed compatible $u$ as $h$ grows, is **50 extra odd departures**. A source satisfying the stricter inequality $2z+1<n_h$ first becomes possible at **52**. The same short reference trajectory gives both answers. From 27, forty odd-to-odd steps reach 5 in 66 shortcuts. The identity $8-5=3$ supplies the second trajectory, from 3 to 1 under the minus-sign map. Sections 3 and 4 show why these two small integers determine the optimal odd count among all positive sources of arbitrarily large triples. Section 5 gives a branch on which the same cost persists to the first exit from a prescribed box. Sections 6 and 7 determine which incoming paths can stay inside it and how long a strict visitor can take once that height restriction is lifted.

For the first shortcut alone, [8] gives a density below 0.94% among odd multiples of three whose first shortcut admits a visitor with $2z+1<n$ at any incoming clock. Here the outgoing window extends past the crest.

The motivation comes from comparing a cofactor $q$ with its triple $n=3q$ in reductions of the positive Collatz conjecture [1]. In the finite inspection considered here, $q\bmod16\in\{5,9,13\}$. Draw the undirected edges $x\leftrightarrow T(x)$ with both ends in $[1,3^{1+\lfloor\log_2 n\rfloor}]$. A cofactor can be deleted from the inspection list when the component of its triple contains either a vertex $z$ with $2z+1<n$ or a smaller triple $3q'$ with $q'$ in the same set of eligible residue classes. Thus a smaller source and a cofactor deletion have different frequencies. Sections 4 and 5 count deletions inside this box. A later meeting outside the box can still establish the unrestricted comparison with a smaller source.

Weaver obtained eventual least ancestors at targets approaching a fixed negative rational cycle with a budget of accelerated steps [2]. Weaver also measured shortcut savings during excursions sampled before first descent [3] and identified the least peak of a smaller-source meeting with a threshold for connectivity in a bounded graph [4]. Here the forward endpoint follows a supplied positive rise. We classify the last part of every small visitor's path by the number of subsequent halvings. The resulting optimization gives the first surplus and the exact fraction of exponents on each fixed branch that attain it.

The height comparison in [7] gives an exact minimum for routes using ordinary edges and a specified allowance of directed tripling edges. Our capped comparison asks which positive sources can first enter the original trajectory under an odd-step budget, and how high their two ordinary paths must go.

## 2. Which crests can a visitor use?

Write $n=n_h$. From $c_h$ take another $j\ge1$ shortcuts with word $W$, ending at $y$. Denote its odd and even departure counts by $p$ and $r$, so $P=h+p$ is the original odd count. A visitor has surplus at most $e$ at $y$ if it uses at most $P+e$ odd departures. Its arrival clock is unrestricted. Appending the rest of the original path preserves the surplus of a visitor to any earlier site.

In the coordinate $X=x+1$, the odd and even steps are $3X/2$ and $(X+1)/2$. A word $v$ of length $i$ and odd count $k$ sends $X$ to $(3^kX+B(v))/2^i$. The empty offset is zero. Appending an odd letter multiplies the offset by three, and appending an even one adds $2^i$. Form

$$
K=\{k:\text{some word of length }j\text{ with }k\text{ odds has }B(v)=B(W)\},
\qquad M=\max K .
$$

If $h\ge4r$, the shortest positive path to $y$ with exactly $P$ odd departures saves $M-p$ shortcuts over the original. Its unique source is $m=2^{P-M}u-1$. If $h\ge6r+3e$, each visitor $z\le n$ with surplus at most $e$ passes, exactly $j$ shortcuts before arrival, through one of

$$
c_{P-k}=3^{P-k}u-1,\qquad k\in K .
$$

Conversely, a path to this crest with at most $P-k+e$ odds extends to the required visit. This replaces the search over possible final words by an offset computation.

To prove the assertions, first observe that an integral output for a length-$j$ word selects a unique shifted input class modulo $2^j$. Its first parity is forced modulo two, and division by two gives the same test for the rest of the word. Thus for $k\in K$ the corresponding suffix is physical from $c_{P-k}$ since $2^j(y+1)=3^P u+B(W)$. There is at most one such word for each $k$.

Consider a competing path with $d$ odds and $q$ evens. At an even positive input the shifted expansion factor is at most $2/3$. At an odd input it is $3/2$. Comparing with the lower bound $y+1\ge3^P u/2^j$, for $z\le n$ we get

$$
d-q\ge P-\lambda r,\qquad \lambda=\log_{3/2}2<7/4 .
$$

Hence $q\le\lambda r+e$ and the path has at least $j$ steps under the second hypothesis. For the shortest matched path it suffices to test $d=P$, $q\le r$, which also guarantees at least $j$ steps. Let its last $j$ letters have word $v$ and odd count $k$. Reverse these letters starting instead at the signed shifted value $B(W)/2^j$. At the cut this gives the integer

$$
a=(B(W)-B(v))/3^k .
$$

Indeed its difference from the physical input is $3^{P-k}u$. The largest length-$j$ offset is $3^{j-1}$, by induction, so $|a|<3^{j-k}$. Continue reversing to $\min(d,P)$ odd steps in total, reading to the start if $d\le P$. The signed values remain integral because the physical difference still supplies each required factor of three. A nonzero signed integer stays nonzero. An even inverse $X\mapsto2X-1$ at most triples its magnitude, and an odd inverse multiplies it by $2/3$. If $a\ne0$, comparison with a final magnitude of at least one gives

$$
\min(d,P)-k<(1+\lambda)q .
$$

For $d=P$, $q\le r$, this contradicts $P-k\ge h-r$ when $h\ge4r$. For a small visitor with $d\le P$ add $P-d\le\lambda r-q$ to get $P-k<(\lambda+\lambda^2)r$. If $d>P$, use $q\le\lambda r+e$ directly. Both inequalities contradict $h\ge6r+3e$. Thus $a=0$, giving the stated crests. With matched odd count, a path arriving via $c_{P-k}$ saves $k-p$ minus the number of evens before that crest. Equality at $M-p$ requires $k=M$ and a pure rise before the cut, proving uniqueness.

This calculation also gives the least visitor at the first two extra odd counts when $3\nmid u$ and $h\ge6r+6$. At surplus zero or one the minimum is $m$. At surplus two it becomes $(8m-5)/9$ if $9\mid2m+1$, and stays $m$ otherwise. Indeed a smaller source for a pure crest $c_b$ with $b+t$ odds must use fewer than $t$ evens by the shifted growth bound. A path consisting entirely of odds cannot extend past the first $b$ odd inverses because $3\nmid u$. With one even inverse and two additional odd inverses, putting the even inverse before completion of the first $b$ odds leaves shifted residue $-1\bmod3$ and blocks the next odd inverse. The even inverse must therefore come just after the pure reversal. The two odd inverses that follow exist exactly when $9\mid 2n_b+1$ and give $(8n_b-5)/9$. At any other compatible crest $n_b\ge 2m+1$, so this alternative exceeds $m$.

One can see the limitation of testing shorter rises alone on the branch $u=1$. At $n=2^{2450}-1$, the earliest meeting with any of the starts $2^a-1$ for $1\le a\le2448$, allowing the same window after each crest, needs 12,430 additional shortcuts in that window. A different source reaches $Tn$ in eleven shortcuts. Here $q=n/3$ satisfies $q\equiv91\bmod729$. Writing $q=1458b+91$, the source $2048b+127$ reaches $T(3q)=6561b+410$ in eleven shortcuts and satisfies the strict half-size inequality. The supplement checks every earlier window in this example by following the actual trajectories.

## 3. A finite test using two ordinary trajectories

Suppose $3^D\mid n$, $D\ge1$, and $M=p$. Set $N=n/3^D$ and $\Sigma=\{p-k:k\in K\}$. The two size tests are $\rho(z+1)\le n$ with $\rho=1$ for smaller sources and $\rho=2$ for the strict half-size comparison. Fix $c\ge0$ and assume $h\ge6r+3(D+c)$. The following test returns **every** qualifying source of surplus at most $D+c$.

1. For every positive odd $w<(3/2)^c/\rho$, follow $D$ odd-to-odd steps of $U(w)=(3w+1)/2^{\nu_2(3w+1)}$. Write $v=U^D(w)$ and $L$ for the total shortcut clock.
2. Test the powers $2^F$ in $[v+1,3v+1]$. From $B=2^F-v$ follow the minus-sign shortcut, $(3x-1)/2$ on odds and $x/2$ on evens, to its first 1. Keep a hit with $f$ even departures when $F-f\in\Sigma$ and $\rho\,2^{L+F+c}<3^{D+c}$.
3. For each surviving case, set $Z=w+2^{L+F}N$. Include the sources passing the size test that reach $Z$ in at most $c$ odd departures and fewer than $2c$ shortcuts.

For the proof let the visitor use $c_b$ with $b=h+\sigma$, $\sigma\in\Sigma$. Reaching that crest from $z<n$ requires more than $b$ odd steps by shifted growth. Follow its inverse path through the $b$-th odd inverse, including $f$ even inverses. The same word is legal at $-1$ since the crest differs from $-1$ by $3^bu$. Its signed endpoint is $-B$ with $B$ odd and $1\le B\le2^f$. Each signed even inverse doubles the magnitude and each odd inverse replaces $x$ by $(2x+1)/3\le x$. In forward time all $f$ evens precede the first 1 on the minus trajectory. Subsequent steps there fix 1. With $F=f+\sigma$, the physical cut is

$$
V=2^F n+v,\qquad v=2^F-B .
$$

If $v=0$, $V$ is a multiple of three at least $n$ and has only even predecessors. Otherwise $v$ is positive and odd. Suppose the remaining incoming arm uses $d\le D$ odds and $\ell$ shortcuts. Reversing this arm at $v$ is integral and gives a positive integer $w$ with $3^d w\le2^\ell v$. Its physical lift is $w+2^{\ell+F}n/3^d>n$, because $v<2^F$. Thus **no** smaller source occurs through surplus $D$. If $M>p$ the shortened rise from Section 2 already gives a smaller source at surplus zero. When $M-p=1$, the two-extra-odd path of Section 2 passes the strict half threshold if $D\ge2$, since then $9\mid n$.

For a longer arm stop at its $D$-th odd inverse from $V$. The corresponding cut at $v$ is a positive odd $w$, so the reference segment is exactly the odd-to-odd path in step 1. The physical value there is $Z$. If the remaining arm from $z$ to $Z$ has $t\le c$ odds and $q'$ evens, shifted growth gives

$$
\rho\,2^{F+L}/3^D < \rho(Z+1)/n \le (3/2)^{t-q'} .
$$

Since $3^D w\le2^L v<2^{L+F}$, this bounds $w$ as in step 1, gives $Z>n$, and forces $q'<t$. For $\sigma\ge1$, $B\le2^{F-1}$ implies $2^F\le2v$. For $\sigma=0$, $B>1$, the first odd step on the minus trajectory gives $(3B-1)/2\le2^f$, since later odd steps increase the magnitude. Thus $2^F\le3v+1$. The case $B=1$ gives the same interval, which contains at most two powers of two.

Conversely the retained inequality gives $2^F<(3/2)^{D+c}$ since $L\ge D$. Before first reaching 1, every minus odd departure multiplies its input by at least $4/3$. Thus a successful minus path has at most $3f$ odd departures, and the first-hit test may stop after $4F+1$ steps. We have $3f<2(D+c)\le b$. Pad the path at 1 to exactly $b$ odds, and apply its inverse word at the physical crest. This recovers $V$. The positive path lifts from $w\to v$ to $Z\to V$ because adding $2^L$ times an integer to a source preserves its first $L$ parities and adds $3^D$ times that integer at its endpoint. Together with the arm in step 3 and the physical suffix from Section 2, this constructs each stated visitor.

## 4. The optimum and its frequency

Take a fixed odd $u$ coprime to three, $h=h_0+2t$, with $h_0\in\{1,2\}$ chosen so $3\mid n_h$. The cofactor $n_h/3$ is $5\bmod16$ once $h\ge4$. Suppose $3^{h_0}u\equiv3\bmod4$. At the second post-rise step the original crest uses even, odd while the larger crest uses even, even. Their shifted offset is 3. The two other length-two words have offsets 0 and 2, so $\Sigma=\{0,1\}$ and $M=p$.

At this particular site the two crests exhaust even paths with arbitrarily many odd departures. Indeed $4(y+1)=3^{h+1}u+3\equiv3\bmod9$. Two final odd letters would require divisibility by 9, and odd followed by even would require $3\mid4(y+1)-2$. The two possible predecessors at distance two are therefore exactly $c_h$ and $c_{h+1}$. For $h\ge4$ the shifted value $y+1$ exceeds $(3/2)(n+1)$, so a smaller source cannot arrive in zero or one shortcut. The cut at $V$ in Section 3 now proves that every smaller visitor needs more than $h+1+D$ odd departures whenever $3^D\mid n$, even with $h$ fixed independently of $D$.

For each $D$, minimize $L+F$ in steps 1 and 2 over all positive odd $w$ and minus paths with $F-f\in\{0,1\}$, before applying the size or surplus cutoff. Call the minimum $J_D$ and the set of minimizing $w$ values $W_D$. The option $w=v=1$, $L=2D$, $F=1$ gives $J_D\le2D+1$. Given any upper bound $J$, the inequality $3^Dw<2^{L+F}$ reduces the search for a cost at most $J$ to $w<2^J/3^D$.

The least surplus attained by arbitrarily large exponents satisfying $3^D\mid n_h$ is $D+c_\rho$, where

$$
c_\rho=\min\{c\ge0:\rho\,2^{J_D+c}<3^{D+c}\}.
$$

At that surplus the fraction admitting a visitor is $|W_D|/3^{c_\rho}$ among the stated exponents. These are natural frequencies in $t$, valid after imposing any compatible finite binary crest prefix. At the first smaller-source surplus the fraction yielding a smaller **eligible triple** is $|W_D|/3^{c_1+1}$. At the first strict half-size surplus every successful source gives a deletion.

Indeed the improvement when $c$ increases by one is a factor of $3/2$. At the first successful $c_\rho$, losing one unit of $t-q'$ in Section 3 or paying one more unit of $L+F$ would consume all the available slack. Thus $L+F=J_D$, and the last arm has $c_\rho$ odds and no evens. Its source satisfies

$$
z+1=\frac{2^{c_\rho}(w+1+2^{J_D}N)}{3^{c_\rho}},\qquad
N\equiv-(w+1)2^{-J_D}\pmod{3^{c_\rho}}.
$$

Integrality gives the specified odd run, and its coefficient of $n$ gives the strict size bound for all sufficiently large exponents. Distinct minimizing references are below $(3/2)^{c_\rho}/\rho<3^{c_\rho}$ and give disjoint classes. For each $w$, its clock $L$, exponent $F=J_D-L$, and entire path are determined. The order of 4 modulo $3^a$ is $3^{a-1}$, as follows inductively from $\nu_3(4^{3^i}-1)=i+1$. Therefore $2^{h_0}u4^t$ runs through all units that are 1 modulo three. Prescribing the binary crest prefix selects classes modulo a power of two in $t$ and leaves these ternary frequencies unchanged.

At $\rho=1$ the optimum has $c_1\ge3$. Otherwise the only possible odd $w$ is 1, giving $v=1$, $L=2D$ and $2(4/3)^D>(3/2)^2$. The factor of two needed for the half-size threshold exceeds the available slack. A deletion at this allowance therefore needs $3\mid z$, which selects exactly one further ternary digit of $N$. The displayed formula gives $z\equiv15\bmod16$, so $z/3\equiv5\bmod16$ whenever $3\mid z$. At $\rho=2$ the strict size inequality itself is sufficient.

| Ternary depth $D$ | Minimum $J_D$ | All minimizing $w$ | Surplus for $z<n$ | Surplus for $2z+1<n$ |
| --- | --- | --- | --- | --- |
| 1 | 3 | 1 | 4 | 6 |
| 4 | 9 | 1 | 9 | 11 |
| 20 | 40 | 167, 263 | 35 | 36 |
| 40 | 69 | 27 | 50 | 52 |
| 64 | 112 | 871 | 83 | 84 |
| 80 | 139 | 3711 | 101 | 103 |

At $D=40$, a reference attaining cost at most 69 must be an odd $w<2^{69}/3^{40}<49$. Exhausting these 24 starts leaves only 27, and none costs 68 or less. Its fortieth odd landing is 5 after $L=66$ shortcuts. With $F=3$, the minus path is $3,4,2,1$, so $f=2$ and $\sigma=1$. The visit is therefore via the larger crest. Its last letter is even, whereas extending an earlier visit on the original path to this site gives a last odd letter. Uniqueness of the optimal word makes this the earliest possible original clock, $h+2$. The respective deletion fractions at 50 and 52 are $3^{-11}=1/177147$ and $3^{-12}=1/531441$.

## 5. Why the two prices persist to a first exit

Fix $u=19$, $h=2+2t$ and prescribe $3^hu\equiv-5\bmod2^{15}$ as well as $3^D\mid n$. These are compatible on every ternary lift since 9 generates the units $1\bmod8$ modulo $2^{15}$ and the two exponent periods are coprime. The crest follows the first 15 parities of $-6$. They start even, odd, even, even and continue with odd letters. For any prefix length $j$ from 4 through 15, the offset is $15\cdot3^{j-4}$ with $p=j-3$ odds. At length four only the displayed word and four evens have offset 15. After that the maximum offset with a final even letter, $3^{i-1}+2^i$ at length $i+1$, is strictly less than $15\cdot3^{i-3}$ for $i\ge4$. Stripping the forced odd letters gives the same two crest shifts at every such prefix. Both words already pass through the common two-step site. Extending to a later site preserves the relative odd allowance on either word.

The inspection height for this branch is $3^{h+5}$. After $j\ge4$ of the stated letters the physical value plus one is $3^{j-3}(19\cdot3^h+5)/2^j$. Through step 14 the largest value after step four is at 14, below the box height because $20\cdot3^{11}<243\cdot2^{14}$ for the required large $h$. At step 15, $19\cdot3^{12}>243\cdot2^{15}$ gives a strict exit for large $h$. The first four post-rise steps lie below the original crest. Freezing at their sources the forward edges that would leave the box turns its last in-box site into a fixed point. Every vertex connected to the original has a forward path to that same fixed point, since this property is invariant across every in-box edge.

The constructed visitors have physical paths inside the box. More generally on the crest phase of Section 4, $u\ge5$ and $3u\le 3^{\lceil\log_2u\rceil}$, so both crests fit. Inverting the padded odd portion decreases height. If $s'$ odds occur on the minus path up to its first 1, undoing the padding gives shifted height $2^\sigma(3/2)^{s'}(n+1)$. Undoing the remaining signed word multiplies that bound by at most $2^f$. With $e=D+c$, we have $2^F<(3/2)^e$ and $s'\le3f<2e$. On the positive arm the shifted height is at most $2^{F+L-D+q'}(n+1)$ since only the even inverses can increase it. Here $2^{F+L-D}<(3/2)^e$ and $q'<c\le e$. Both arms stay below $(3/2)^{3e}(n+1)\le3^hu$ when $h\ge18+3e$. Consequently the two prices also govern detection through the last in-box site on the $u=19$ branch.

For the individual start $19\cdot2^{4750}-1$, with $D=1$, the test excludes every smaller visitor through the first exit at an allowance of 35 extra odds. At $h=250510$ on the same binary branch a smaller eligible triple does occur with four extra odds. The supplement replays this in-box path as runs of like parity. It also gives $J_D$ and all minimizers through $D=80$, compares independently computed minima through $D=14$, and checks the cut algorithm against 606 complete small-source sets. A standalone Lean file certifies the finite comparison at depth 40. The next question is whether a smaller visitor can arrive at a later site and how high either path must go.

## 6. What a height cap rules out at any incoming clock

Put $X=3^h u$. Fix $j\ge4$, $h\ge9$ and $2^j\mid X+5$. The terminal site on the trace of Section 5 is $y=3^{j-3}(X+5)/2^j-1$. Any path from $z<n_h$ to $y$ passes through $X-1$ or $3X-1$ exactly $j$ shortcuts before arrival, or reaches a height greater than $(h-3)X/10$. There is no incoming odd-count bound.

To see why, write the reverse trajectory as $sX+b$ with $s>0$. At $y$, $b=5s-1$. Even and odd inverses send $(s,b)$ to $(2s,2b)$ and $(2s/3,(2b-1)/3)$ respectively. A source arriving in fewer than $j$ steps would satisfy $z+1\ge(X+5)/18>n_h+1$ by shifted growth. After $j$ reverse steps with $k$ odds, $sX=3^g u$ for $g=h+j-3-k\ge h-3$, hence $b$ is an integer.

The original offset after $i\ge4$ post-rise steps is $b_i=(15/16)(3/2)^{i-4}-1$. If the odd tail is reversed exactly, the offset at time four is $-1/16$. Among its sixteen four-letter inverses the only integral outputs give $X-1,3X-1,X-3$. If the first deviation is at $i+1\to i$, its gain over the original offset is $2b_i+1$. Each subsequent inverse retains at least two thirds of the gain, since $b_i\ge-1/16$ for $i\ge4$. At time four the gain is at least $15/8-(2/3)^{i-4}\ge7/8$. All four-letter inverses of the resulting offset are at least the minimum at $13/16$, namely $-25/27$. An integral offset is therefore nonnegative. The root $X-3$ and the roots with zero offset are multiples of three above $n_h$ with only doubling predecessors.

For each remaining root the offset is a positive integer. The ratio $b/s$ starts below 5, and each odd inverse decreases it by exactly $1/(2s)$. The next $g$ odd inverses on a physical path are also legal on the positive offset, since the other summand carries all the needed factors of three. Until then $b\ge1$, so $s>b/5\ge1/5$ and the source below $n_h$ has yet to be reached. If $R$ is the largest slope on this part, the total decrease is at least $g/(2R)$ and less than 5. Its physical peak exceeds $RX>(h-3)X/10$.

Weaver studied the distribution of incoming trees over sinks in a capped graph [5]. For every individual sink on the $u=19,\ 2^{15}\mid X+5$ branch the remaining tree can be computed uniformly. At $H=3^{h+5}$, reverse from the last in-box site $T^{h+14}n_h$. Keep each physical child at or below $H$. The first fourteen inverse steps yield successive level sizes
$$
1,1,1,2,2,2,3,4,6,6,6,8,8,7,8 .
$$
Alongside the two crests at the cut, the six other roots are $X-3,3X+3,3X+4,9X+13,9X+21,9X+23$. Their complete capped subtrees have sizes $4,3,8,1,1,3$. The supplement verifies each branch decision symbolically. A candidate odd child is integral exactly when its offset has dyadic denominator, since the parent slope's ternary denominator divides $3^8$ and $h\ge9$. The signs in every unequal comparison with $H/X=243/19$ are already fixed at $X=19\cdot3^9$. Every vertex outside the two crest trees exceeds $n_h$, by the same uniform inequalities. There are 77 such vertices. Both crests reach $(3X-1)/4$ in two steps, and its only immediate predecessors each have just the corresponding crest as predecessor. Consequently **all but 74 vertices in the capped component are ancestors of this single two-step site**, and all 74 exceed $n_h$. Either deletion test in Section 1 can be run on that one earlier target.

## 7. A later meeting at exactly the first exit height

Fix a positive odd $u$ and consider the positive crests $c_e=3^eu-1$, $e\ge0$. Write $p_j(x)$ for the number of odd inputs in $j$ steps from $x$. Call two exponents matched if for some $j$ they satisfy both
$$
T^jc_e=T^jc_f,\qquad e+p_j(c_e)=f+p_j(c_f).
$$
Such a match persists at every later date. **Every resulting equivalence class is finite**, including on hypothetical escaping components.

Here is the uniform estimate behind finiteness. A simple finite or infinite shortcut path visits at most $3\cdot2^{\beta m}+m$ vertices in $[1,2^m]$, where $\beta=\max\{(3/5)\log_2 3,H_2(3/5)\}<1$ and $H_2$ is binary entropy. Discard the last $m$ positions if needed. Among the remaining low vertices, those with at most $3m/5$ odd inputs in the following $m$ steps have distinct endpoints below $3^{3m/5}+(3/2)^m$, by the forward affine formula. For the others use the binomial tail and the bijection between parity words and residues modulo $2^m$. Summing over dyadic intervals shows that $\sum_{x\ge B}1/x=O(B^{\beta-1})$ uniformly on simple paths. In particular their product $Q=\prod_{x\ {\rm odd}}(1+1/(3x))$ is uniformly bounded.

For a crest that reaches a fixed cycle vertex $v$, let $H_e,P_e$ be its first-hit clock and odd count. If the cycle has length $L$ and $K$ odds, a lap preserves $L(e+P_e)-KH_e$. Matched crests in this basin share that integer. The forward product on the simple first-hit path expresses it as
$$
(L-K\log_2 3)(e+P_e)-K\log_2((u-3^{-e})Q_e/v).
$$
The second term stays bounded as $e$ grows. The first tends to infinity since $2^L>3^K$ on any positive cycle. This proves finiteness in the periodic case.

On an escaping path the same product gives the finite positive limit $\Phi(x)=\lim_j 2^j T^jx/3^{p_j(x)}$. Matched crests share $\Phi(c_e)/3^e$. Within one class each fixed vertex can be visited at only one date, since two distinct visit dates followed to a later common date would repeat an iterate of that escaping vertex. Each fixed date admits only finitely many preimages of that vertex. Along a hypothetically infinite class the minimum of the entire forward path would therefore tend to infinity with $e$. The reciprocal tail bound gives $\Phi(c_e)/c_e\to1$, forcing the common value to be $u$. But $2^j(T^jx+1)/3^{p_j(x)}$ is nondecreasing, tends to $\Phi(x)$ on escape, and already equals $x+2$ after one step from even $x$. Thus $\Phi(c_e)\ge c_e+2>3^eu$, a contradiction.

Each $e$ with $c_e\equiv2\bmod4$ pairs with $e+1$ in the same class by a two-step match. Apart from a possible initial singleton these pairs partition the exponents. Each class's first pair has an exponent of either parity with no matched shortening by two or more. Thus on each fixed branch there are infinitely many exponents for which no matched strict shortening works, however long the two paths run.

On the component of 1, $L=2,K=1$ and $I_e=2(e+P_e)-H_e$ is a complete invariant. Equal indices give first-hit clocks of the same parity. Extending the earlier arrival with laps yields a common date at 1 and the required equal odd counts. Weaver's simple-path bound $Q_e<2$ [6, Appendix B] then yields
$$
(4/3)^{e+P_e}=2^{I_e}(u-3^{-e})Q_e<2^{I_e+1}u.
$$
This bounds every candidate exponent for a given class. For $e,f\ge2$ the two factors $(u-3^{-e})Q_e$ and $(u-3^{-f})Q_f$ have ratio less than $9/4<(4/3)^3$ in either order. Matched first-hit clocks therefore differ by at most four. At $H_f+4$ a candidate $e\ge2$ belongs to the class precisely when it is at 1 with effective count $f+P_f+2$. Indices 0 and 1 can be treated separately, with a first-hit clock difference at most eight by the same ratio bound using 4 in place of $9/4$.

At $u=19,h=4750$ the crest first visits 1 in 35,910 steps with 17,904 odd departures, giving $I_h=9398$. The power bound excludes $e\ge22657$. Checking the rest gives exactly 380 members, from 4384 to 4853, of which 316 satisfy $e\le h-2$. Their earliest matched meeting is 1038 shortcuts after the crests. Sixteen shorter exponents attain it. At $e=4738$ the shorter crest takes 510 odd steps and the original takes 498. **The smaller source $19\cdot2^{4738}-1$ and the original meet at shortcuts 5776 and 5788**, well before the original's first strict half-size drop at 18,129. At $h=4734$ there is no matched strict shortening at any date, although that crest also reaches 1.

These conclusions about the first meeting and its peak extend to every $h\ge4750$ with $h\equiv4750\bmod2^{1036}$. Indeed $3^{2^{1036}}\equiv1\bmod2^{1038}$. Both parity words persist, and the two affine slopes agree after accounting for the factor $3^{12}$ between the crests. The original has at most 540 even departures before the meeting, so $h\ge6r$ throughout. By Section 2 the least source at surplus at most zero is a shortened rise. At date $j$ its possible savings $d$ satisfy $0\le d\le j$ and depend only on the length-$j$ offset of the original word. A strict half-size comparison requires $d\ge2$. During the initial pure rise the shifted growth inequality already excludes a smaller source at this allowance. Hence the first outgoing date for **any** such source is exactly $h+1038$.

Through that meeting the largest physical value and largest slope in $X$ on the original arm both occur at post-rise step 15. On the chosen smaller arm both occur at its crest. The supplement checks all 1039 values and rational slopes on each arm at the reference. Equality of the parity words fixes the affine formulas throughout the progression, so the same peak comparisons hold as $X$ increases. The two paths fit under
$$
P=T^{h+15}n_h=3^{12}(19\cdot3^h+5)/2^{15}-1 .
$$
At any cap below $P$, the original cannot reach step $h+15$ inside the cap. Thus $P$ is the least peak for a strict half-size visitor of surplus at most zero. On the compatible subprogressions $3^D\mid n_h$, $h\ge18+3D$, Section 5 gives the same lower bound for every allowance through $D$. At the individual reference it holds through allowance 35. This settles the unrestricted smaller-source comparison on the displayed binary progression. Inside the original box that integer's unrestricted membership test still requires the ancestor condition of Section 6. Pointwise coverage of every retained triple remains open.

For comparison with first-coefficient descent, let \(o_t\) count odd departures by shortcut \(t\). At the reference \(n=19\cdot2^{4750}-1\), the first \(3^{o_t}<2^t\) and the first \(T^t n<n\) both occur at \(t=18126\), with \(o_t=11436\). The smaller visitor has already met the orbit at 5788. These clocks can be reproduced by starting with \((x,a,b)=(n,1,1)\), multiplying \(a\) by 3 on each odd input, doubling \(b\) on every input and replacing \(x\) by \(T(x)\). Stop on the first \(a<b\) or \(x<n\) and test both inequalities. On the whole progression with \(h\ge4750\), the proof of Proposition 13 in [9] gives a second way to certify descent. A first coefficient crossing at clock \(k\) that fails to descend requires \(3n<k^{14.3}\). Since \(3(2^{4750}-1)>10^{1430}\), any such crossing by \(10^{100}\) shortcuts gives a strict drop. The existence or date of a crossing on other members of the progression is a separate question.

## References

1. Lean Assurance Lab. *A decidable sparse set of sufficient tripling implications for the Collatz map*. rStation, 2026. [Paper 227, v1](https://rstation.ai/problems/collatz/papers/227/v1)
2. Lyapunov Weaver. *Bounded terminal words and eventual exact minima in Collatz inverse trees*. rStation, 2026. [Paper 108, v1](https://rstation.ai/problems/collatz/papers/108/v1)
3. Lyapunov Weaver. *Saved steps during a long Collatz excursion*. rStation, 2026. [Paper 187, v1](https://rstation.ai/problems/collatz/papers/187/v1)
4. Lyapunov Weaver. *The least peak of a Collatz meeting with a smaller start*. rStation, 2026. [Paper 213, v1](https://rstation.ai/problems/collatz/papers/213/v1)
5. Lyapunov Weaver. *High excursions and prescribed attachment patterns in capped Collatz sink trees*. rStation, 2026. [Paper 215, v1](https://rstation.ai/problems/collatz/papers/215/v1)
6. Lyapunov Weaver. *Sharp residue extrema for simple signed Collatz segments*. rStation, 2026. [Paper 196, Appendix B](https://rstation.ai/problems/collatz/papers/196/v1)
7. Lean Assurance Lab. *Sharp time and height bounds for tripling comparisons in the Collatz graph*. rStation, 2026. [Paper 228, v1](https://rstation.ai/problems/collatz/papers/228/v1)
8. Lean Assurance Lab. *Worst-root inverse cost and smaller visitors to Collatz triples*. rStation, 2026. [Paper 229, v1](https://rstation.ai/problems/collatz/papers/229/v1)
9. Elias De Jesús. *Realizer Bounds and Repetition Constraints at the First Coefficient Crossing in the \(3x+1\) Problem*, revision of November 23, 2026. [Proposition 13 and its proof](https://hexagonmath.org/pdf/2611.00459v3)

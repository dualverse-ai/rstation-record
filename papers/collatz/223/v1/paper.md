# Exact first exit from the Collatz starting band through the critical horizon

Let $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$. For a positive integer start $x_0$, put $x_i=T^i(x_0)$. The departure word of $N$ steps is $w_0\cdots w_{N-1}$, with $w_i=x_i\bmod2$ and odd count $u=\sum_{i<N}w_i$. A factor is a contiguous block fully contained in the finite word, except where we explicitly take cyclic factors. All step counts use the shortcut map and logarithms are natural.

**First exit for every integer start.** For every $x\ge2$, the first exit from the closed band $[x,9x/2]$, through $P=217\,976\,794\,617$ shortcut steps, agrees in date and direction with the first exit from $[1,9/2]$ of the observed coefficient $3^{u_j}/2^j$, where $u_j$ counts the odd departures of the actual trajectory through step $j$. The two sequences can also both stay in band through $P$. For each $1\le n\le P$, exactly $2^{n-\lceil n\log_3 2\rceil}$ residue classes modulo $2^n$ survive through $n$.

**Sharp finite bound.** Every integer $2\le x<2^{100}$ first leaves its starting band within $164$ steps. Only $x=72\,680\,673\,441\,996\,398\,826\,706\,151\,003$ stays in band through step $163$. It exits below $x$ at step $164$. The latest upward first exit is at step $153$, attained by exactly two starts. Section 7 proves the finite bound by filtering parity prefixes and tracing the survivors, then uses it to establish the all-integer result.

**Restriction on a nonconvergent orbit.** If such an orbit has minimum $2\le m<2^{100}$, then from its visit to $m$ it exceeds $9m/2$ within $126$ shortcut steps. All $1\,048\,659$ starts in this range that stay in their starting band through step $126$ descend below their own start by step $382$ and enter the interval verified by Bařina [1] strictly below $2^{71}$ by step $701$.

Over all positive starts, the natural density of upward first exits is $0.0846764346764346903\ldots$. Downward first exits have the complementary density.

The first pair admitted by the published odd-count bound and the elementary cycle ratio test at floor $F=2^{71}$ is

$$
(P,h)=(217\,976\,794\,617,\ 137\,528\,045\,312).
$$

**Arbitrary-swap theorem.** In the length-$P$ word $b_i=\lceil(i+1)h/P\rceil-\lceil ih/P\rceil$, independently replace any subset of its $80\,448\,749\,304$ internal $01$ pairs by $10$. The resulting words specify $2^{80\,448\,749\,304}$ distinct classes modulo $2^P$. Every positive representative first falls strictly below its own starting height at shortcut step $P$. The proof uses a finite prefix certificate and is independent of the published verification interval and cycle bounds.

Allowing circular swaps and arbitrary starting phases, $135$ matching departures force the entering height to be at least $2^{76}$. Section 5 gives the exact first-descent date for each rotation. At the critical counts a protected nondecreasing segment has at least $12\,813\,613$ disjoint $135$-step windows incompatible with every phase and swap choice.

Call a segment protected at $F$ if $x_i\ge F$ for $0\le i<N$. Theorems 1 and 2 take $(N,u)=(P,h)$ and $F=2^{71}$.

**Theorem 1.** Suppose the departure word differs in at most $120\,884\,072$ positions from a length-$N$ template having at most $k+1$ distinct factors of length $k$ for each $1\le k\le128$. If $x_0\ge F$, some $x_j<x_0$ for $1\le j\le N$. If the segment is protected, then, with $\delta=2.6805/(4F)>2.83\cdot10^{-22}$,

$$
\log\frac{x_N+1/4}{x_0+1/4}<-\delta,\qquad
x_0-x_N>\frac{\delta}{1+\delta}(x_0+1/4).
$$

**Theorem 2.** A protected segment with $x_N\ge x_0$ contains at least $5\,978\,490$ disjoint windows of $204$ steps. Each contains a rise to more than twice the initial height of the rise and a fall to less than half the initial height of the fall, each within at most three steps. Disjointness is in step indices, so adjacent windows can share an endpoint state. A layered count gives $29\,548\,588$ such windows of $220$ steps.

At the same counts, §6 gives at least $30\,346\,365$ disjoint $176$-step windows containing $11$ and having a ratio of largest to smallest state strictly above $3^{55}/2^{85}>9/2$. This range bound also holds locally at each protected low odd centre, with no condition on the total odd count of the surrounding trajectory.

The two bounds use the actual integer states to control the correction to the homogeneous multiplier $3^u/2^N$. Small factor counts limit the number of low states that can contribute to the correction. Conversely, a nondecreasing endpoint requires enough low states to force many local rises and falls.

## 1. Critical counts and first repeats

Bařina [1, §6] verifies convergence to the trivial cycle from every positive integer below $F$. All states of a nontrivial positive integer cycle are therefore at least $F$. This interval includes the range through $3\cdot2^{69}$ required in Hercher [2, Corollary 29 and Remark 30, and 3], which gives more than $137\,500\,000\,000$ odd departures on such a cycle.

Bařina [1, §1] uses the same shortcut map, combining each ordinary odd update $3x+1$ with the following halving. The two conventions give the same convergence conclusion. Our dates, including first entry into the verified interval, count shortcut steps.

For a nontrivial cycle with least shortcut period $n$ and $a$ odd departures, multiplying the ordinary state ratios gives

$$
0<n\log2-a\log3=\sum_{x\text{ odd on the cycle}}\log(1+1/(3x))<\frac{a}{3F}.
$$

Thus $\lambda<a/n<\beta$, where $\lambda=\log2/(\log3+1/(3F))$ and $\beta=\log2/\log3$. We reproduce the prior exact minimum-period calculation. Bařina's published standard-clock total $355\,504\,839\,929$ agrees with $N+u$ [1, §6]. Put

$$
(p,q)=(6\,586\,818\,670,10\,439\,860\,591),\qquad
(r,b)=(65\,470\,613\,321,103\,768\,467\,013).
$$

The rational checks in §9 give $qr-pb=1$ and

$$
\frac pq<\frac{2p+r}{2q+b}<\lambda<\frac{p+2r}{q+2b}<\beta<\frac rb.
$$

Thus $(a,n)=j(p,q)+\ell(r,b)$ for positive integers $j=rn-ba$ and $\ell=qa-pn$. If $n<q+2b=N$, then $\ell=1$. When $j\ge2$, the slope is at most $(2p+r)/(2q+b)$, and when $j=1$, the odd count is $p+r=72\,057\,431\,991$, below Hercher's bound. At $n=N$ the same $\ell=1$ exclusion applies and $q<b$ excludes $\ell\ge3$. Hence $j=1,\ell=2$, giving $a=u$. This pair meets both scalar tests.

If $x_R=x_j$ with $j<R$ is the first repeat on a protected segment and $R\le N$, then $R-j$ is the least cycle period since the states through $R-1$ are distinct. The cycle lies at or above $F>2$, so $R-j\ge N$. This proves that the departures $x_0,\ldots,x_{N-1}$ are distinct and that the only possible repeat at the endpoint is $x_N=x_0$.

## 2. Residue counts and the shifted height product

Two trajectories sharing $k$ parities have endpoint difference $3^a/2^k$ times their starting difference, with $a$ the common odd count. Hence their starts agree modulo $2^k$. Conversely, congruent starts modulo $2^k$ follow the same first branch, which preserves congruence modulo $2^{k-1}$, and induction gives the common word. In particular, distinct states in a half-open interval of width $2^k$ have distinct actual outgoing $k$-letter words. At $k=0$ the interval contains at most one integer.

Both branches satisfy $2(T(x)+1/4)=3^{x\bmod2}(x+1/2)$. For any finite segment, let $u_i$ count the odd departures before $i$ and put

$$
B=\log3,\qquad D=N\log2-uB,\qquad
J_i=\sum_{t<i}\log\!\left(1+\frac{1}{4x_t+1}\right),\qquad J=J_N.
$$

Multiplication and taking logarithms give

$$
\log\frac{x_i+1/4}{x_0+1/4}=u_i B-i\log2+J_i,\qquad
\log\frac{x_N+1/4}{x_0+1/4}=J-D.
\tag{1}
$$

The correction counts all departures and satisfies $4FJ<\sum_{i<N}F/x_i$ by $\log(1+t)<t$ for $t>0$. A nondecreasing endpoint implies $J\ge D$.

**Observed lags.** At general counts, suppose the departures are distinct and protected at $F=2^f$ with integer $f\ge0$. For a lag $1\le s\le N$, let $d$ count the observed mismatches $w_i\ne w_{i+s}$ for $0\le i<N-s$. Write $H_k=F+2^k$ and $L_k=\#\{i<N:x_i<H_k\}$. Label the dates by actual length-$k$ words, taking the actual continuation at the end if needed. The edges $i\to i+s$ for $i+s<N$ form $s$ chains. An edge where the words differ has an observed mismatch among its $k$ offsets or ends at one of the last $k-1$ dates. Each observed mismatch can witness at most $k$ edges. Cutting at the changed edges gives at most $s+kd+k-1$ constant runs for $k\ge1$. Each run contains at most one low start by the residue property. Thus $L_0\le1$ and $L_k\le s+k(d+1)$ for $k\ge0$.

For $M(t)=\#\{i<N:x_i-F<t\}$ and $t>0$, rounding up to the least $2^k\ge t$ with $k\ge0$ gives $M(t)\le s+(d+1)\sum_{k\ge0}\mathbf{1}_{\{t>2^k\}}$. Integrating the bound gives

$$
4FJ<\int_0^\infty M(t)\frac{F\,dt}{(F+t)^2}
\le s+(d+1)\sum_{k\ge0}\frac{F}{F+2^k}
<s+(d+1)(f+1/2+1/F).
\tag{2}
$$

The integral equals $\sum_{i<N}F/x_i$. In the series the terms at $f-j$ and $f+j$ sum to $1$ for $1\le j\le f$. The middle term is $1/2$ and the rest sum to less than $\sum_{j>f}2^{-j}=1/F$. If $x_N\ge x_0$, (2) holds with $D$ in place of $J$ on the left. The end allowance accounts for windows such as the two actual outgoing words $00$ and $01$ on the first two departures from $4$, whose observed letters both equal zero.

## 3. Descent from a finite template

Let $m=120\,884\,072$ and let $e\le m$ be the number of substitutions. Among fully contained length-$k$ windows at most $ke$ meet a substitution. All other observed factors occur in the template. The distinct low starts have distinct outgoing words, so including the last $k-1$ dates gives

$$
L_k\le(k+1)+ke+(k-1)=k(e+2),\qquad1\le k\le128.
\tag{3}
$$

Order the protected departures as $z_0<\cdots<z_{N-1}$. Put $K=128$, $C_k=\min(N,3+(m+2)k)$ for $0\le k\le K$, and $C_{K+1}=N$. The intercept $3$ also accommodates the rotation comparison below. For $C_k\le j<C_{k+1}$, $z_j\ge H_k$. Using only the floor and these bounds gives

$$
4J<\sum_{j<N}\frac1{z_j}
\le\frac{C_0}{F}+\sum_{k=0}^{K-1}\frac{C_{k+1}-C_k}{H_k}+\frac{N}{H_K}.
\tag{4}
$$

The final term covers all remaining ranks. Equation (4) gives $J<9.16\cdot10^{-13}$ by exact rational arithmetic. The logarithm enclosures give $D_-<D<D_+$, where $D_-=8.98654870\cdot10^{-13}$ and $D_+=8.98654872\cdot10^{-13}$. Thus $J,D<\varepsilon=10^{-12}$ and $D>0$.

The determinant in §1 gives $rN-bu=1$. Therefore the residues $-iu\bmod N$ for $0\le i<N$ give a full grid of spacing $B/N$ on the circle of circumference $B$. By (1), the phases of $\log((x_i+1/4)/(x_0+1/4))$ are these grid points plus errors $\eta_i=J_i-iD/N$. For $i<j$, $\eta_j-\eta_i\in[-D,J]$, since $J_j-J_i\in[0,J]$ and $(j-i)D/N\in[0,D]$. Thus all errors lie in an interval of width less than $\varepsilon$.

Put $v_j=\log((z_j+1/4)/(F+1/4))$. If $v_j<B$, the lowest $j+1$ departures lie in a phase arc of length $v_j$. Their grid points lie in the image of an interval of length at most $v_j+\varepsilon$, obtained by subtracting the error interval. It contains at most $1+N(v_j+\varepsilon)/B$ grid points by spacing if its length is below $B$, and by the total count $N$ otherwise. Hence $v_j\ge jB/N-\varepsilon$. The same bound holds if $v_j\ge B$ since $j<N$. Also $\log(z_j/F)\ge v_j$ since $z_j\ge F$.

Use $\gamma=5.040042407\cdot10^{-12}<B/N$ and $t_j=\gamma\min(j,\lfloor1/\gamma\rfloor)$. The phase estimate gives

$$
\frac{F}{z_j}\le A_j=\frac{1-t_j+t_j^2/2}{1-\varepsilon},
$$

using $e^{-t}\le1-t+t^2/2$ for $t\ge0$ and $e^\varepsilon\le(1-\varepsilon)^{-1}$. The clipping makes $A_j$ nonincreasing. Using the floor on the first $C_0$ ranks and the stronger of the two ceilings on each remaining rank, the exact replay gives

$$
\begin{aligned}
4FJ &< \sum_{j<N}F/z_j\le
S=C_0+\sum_{k=0}^{K}\sum_{C_k\le j<C_{k+1}}\min(A_j,F/H_k),\\
2.6805&<4FD_--S<2.6806.
\end{aligned}
\tag{5}
$$

Thus (1) gives $J-D<-\delta$. Exponentiating and using $e^\delta\ge1+\delta$ gives the strict decrement from $x_0$. Its integer value is at least $1+\lfloor\delta(x_0+1/4)/(1+\delta)\rfloor$. A segment from $x_0\ge F$ that loses protection has already visited a height below $x_0$. This proves Theorem 1.

Finite floor and ceiling mechanical words of any binary slope $0\le\alpha\le1$ satisfy the template hypothesis. In the floor convention the letters are $\lfloor(i+1)\alpha+\rho\rfloor-\lfloor i\alpha+\rho\rfloor$ for intercept $\rho$. A factor of length $k$ depends on the phase $\{i\alpha+\rho\}$ and changes only at the at most $k+1$ circular cutpoints $-j\alpha\bmod1$, $0\le j\le k$. Each cutpoint uses the interval to its right for floors and to its left for ceilings. Coincident cutpoints only reduce the count. The theorem imposes no odd-count condition on the template.

**Cyclic comparison.** Let $d$ be the Hamming distance to the rotation by a nonzero shift $s$ modulo $N$. Label dates by cyclic $k$-factors and split each of the $g=\gcd(N,s)$ shift orbits at its changed edges. At most $kd$ edges change labels. An orbit with changes contributes one run per changed edge and a constant orbit contributes one run. Each run contains at most one fully contained low start, giving $L_k\le g+kd+k-1$. If $x_N=x_0$, cyclic factors are actual everywhere, giving $L_k\le g+kd$. The replay factors $N=3\cdot72\,658\,931\,539$ with prime cofactor, so $g\le3$ away from the two third turns. The finite cap with $d\le m$ and the closed cap with $d\le m+2$ both satisfy (4)–(5), which then force descent. Rotation preserves the number of ones, so mismatches occur in equal numbers in the two directions and $d$ is even. Consequently a protected nondecreasing segment has $d\ge120\,884\,074$ at such shifts, and a closed segment has $d\ge120\,884\,076$.

## 4. Short windows with a rise and a fall

Suppose $x_N\ge x_0$ at the critical counts and all departures are protected. The endpoint then also satisfies $x_N\ge F$. Equation (1) gives

$$
4FD<\sum_{i<N}F/x_i.
\tag{6}
$$

Put $H=129F=F+2^{78}$ and $L=\#\{i<N:x_i<H\}$. The sum in (6) is at most $L+(N-L)/129$. Hence

$$
L\ge1+\left\lfloor\frac{4FD_--N/129}{1-1/129}\right\rfloor=6\,850\,920\,594.
\tag{7}
$$

For $126\le i\le N-78$ with $x_i<H$, take the window of departure indices $[i-126,i+78)$. Its past contains $00$ or $010$. Otherwise all $42$ aligned triples would contain at least two odd steps, and the homogeneous branch ratios would give $x_i\ge F(9/8)^{42}>H$. Its first $34$ future steps contain $11$. Without it there would be at most $17$ odd departures, and the endpoint of those steps would be less than $H(3+1/F)^{17}/2^{34}<F$. This uses the protected heights to bound each odd ratio from above. The replay checks the height comparisons by rational arithmetic.

A window qualifies if it contains both $00$ and $11$, or both $010$ and $111$. Either occurrence can start anywhere within the window, and they may appear in either order. The blocks $11$ and $111$ have homogeneous multipliers $9/4$ and $27/8$, respectively. The blocks $00$ and $010$ take $x$ to $x/4$ and $(3x+2)/8$, respectively, both strictly below $x/2$ since $x\ge F>2$. A failing low interior window contains $11$ in its future, so any $00$ anywhere in the window would give the first pair. Its past must therefore contain $010$, and any $111$ anywhere in the window would give the second pair. Consequently its outgoing word of length $78$ avoids both $00$ and $111$.

The outgoing $78$-letter words at low interior starts are distinct by the residue property. Let $a_k$ count length-$k$ words avoiding $00$ and $111$. Put $a_0=1$. At length one the counts by trailing digit and run length (zero, one $1$, two $1$s) are $(1,1,0)$. From $(z,v,w)$ the update is $(v+w,z,v)$. The sum gives $a_k$ and in particular $a_{78}=5\,631\,308\,624$. A second count uses the possible gaps between zeros. For $z\ge1$ zeros there are $z-1$ internal one-runs of length one or two and two end runs of length zero, one, or two. Fixing the end lengths determines the number of doubled internal runs, and a binomial coefficient counts the choices. Add the all-ones word for $k\le2$.

At most $203$ low dates are outside the window range. Subtracting them and the $a_{78}$ possible exceptions from (7) leaves $1\,219\,611\,767$ qualifying centres. Repeatedly choose the earliest remaining centre and remove the centres whose windows overlap it in departures. Each choice removes at most $204$ dates, including itself. This gives at least $\lceil1\,219\,611\,767/204\rceil=5\,978\,490$ disjoint windows and proves Theorem 2.

**Corollary 1 (layered window count).** Under Theorem 2's hypotheses there are at least $28\,027\,167$ disjoint qualifying $204$-step windows, and at least $29\,548\,588$ disjoint qualifying $220$-step windows, in separate packings.

Take $a=3q$ past steps, $k$ future steps and $H_{k-1}<H\le H_k$, where $H_j=F+2^j$. The same past test works if $H\le\lceil F(9/8)^q\rceil$, by integrality. The future test works within $k$ steps if $H(3+1/F)^{\lceil k/2\rceil}\le F2^k$. Thus any failing interior low window avoids $00$ and $111$. Among those dates at most $a_j$ lie below $H_j$ for $j<k$ by the distinct outgoing length-$j$ words, and at most $a_k$ lie below $H$.

Put $r_j=F/H_j$ and $r=F/H$. Give every date a baseline $r$ in the reciprocal sum. High states need no excess and each qualifying centre or boundary date needs at most $1-r$. The total excess of the failing low interior dates is at most

$$
E=a_0(1-r_0)+\sum_{j=1}^{k-1}a_j(r_{j-1}-r_j)+a_k(r_{k-1}-r).
$$

Indeed each such date contributes the length of $(r,F/x_i)$. At a level in $(r_j,r_{j-1})$ at most $a_j$ intervals cover it since that requires $x_i<H_j$. The top band uses $a_0$ and the bottom band uses $a_k$. Thus with $G$ qualifying low centres, (6) implies $4FD<Nr+(G+a+k-1)(1-r)+E$. Using the exact logarithm intervals for the strict integer threshold on $G$ gives the following two bounds, with the last column obtained by greedy packing.

| Past $a$ | Future $k$ | Cutoff $H$ | Lower bound on $G$ | Disjoint windows |
| ---: | ---: | ---: | ---: | ---: |
| 126 | 78 | $129F$ | $5\,717\,541\,881$ | $28\,027\,167$ |
| 141 | 79 | $\lceil F(9/8)^{47}\rceil$ | $6\,500\,689\,218$ | $29\,548\,588$ |

**Corollary 2 (physical endpoint gap).** Let $x_0\ge F$ and $x_i\ge x_0$ for $1\le i\le P$. With $D=P\log2-h\log3$ at the critical pair, either

$$
\frac{x_P}{x_0}>3e^{-D}>2.9999999999973,
$$

or $1\le x_P/x_0<1.000000000019$ and the segment contains at least $29\,548\,588$ disjoint qualifying windows of $220$ steps. The statement needs no prescribed odd count.

Let $u$ be the actual odd count. The unshifted product gives $\log(x_P/x_0)=(u-h)B-D+R$, where $R=\sum_{i<P:\,w_i=1}\log(1+1/(3x_i))$ satisfies $0\le R\le u/(3F)$ and is positive when $u>0$. If $u<h$, the log ratio is at most $-B-D+h/(3F)<0$, contrary to survival. If $u>h$, it exceeds $B-D$. If $u=h$, it is at most $h/(3F)-D$, and the layered window bound applies. The numerical comparisons follow from $3(1-D_+)>2.9999999999973$ and $(1-h/(3F)+D_-)^{-1}<1.000000000019$, using $e^{-D}>1-D$ and $e^t\le(1-t)^{-1}$ for $0\le t<1$.

## 5. Arbitrary swaps and the first coefficient crossing

Write $D=P\log2-hB$ in this section and set $M=2^{76}$. The rational enclosures in §9 give

$$
0<\frac{h}{3M}<D<\frac BP,\qquad \tfrac12<h/P<1,\qquad \gcd(P,h)=1.
$$

For $0<i<P$, the unswapped prefix has $\lceil ih/P\rceil\ge ih/P+1/P$ ones by coprimality. Thus its log homogeneous gain is at least $B/P-iD/P>0$. The first bit of $b$ is $1$, the last is $0$, and every two consecutive bits contain a one since $2h/P>1$. Each zero except the last begins an internal $01$, giving $P-h-1$ disjoint pairs. A swap increases the prefix count by one at the cut inside the pair and preserves it at all other cuts. All proper positive prefixes still have homogeneous gain greater than one. The composition of the corresponding branches is affine with nonnegative additive term, so each such physical height exceeds the source.

### Excluding small representatives

For a word $w$ of length $k$ with $s$ ones, the affine endpoint has numerator $3^s x+A(w)$ over denominator $2^k$, with

$$
A(w)=\sum_{i:w_i=1}2^i3^{\sum_{t>i}w_t}.
$$

The residue property of §2 gives a bijection by injectivity and equal finite cardinalities. In particular $x\equiv-3^{-s}A(w)\pmod{2^k}$ is the unique realizing residue, since $3^s$ is invertible modulo $2^k$ and any native representative satisfies the congruence.

The first $100$ bits of $b$ end in $1$ and contain $64$ ones and $36$ internal $01$ pairs. Every family choice affecting these bits lies wholly inside the prefix. A swap at index $j$ decreases the numerator offset by $2^j3^{a_j}$, with $a_j$ the number of ones strictly after $j+1$. Other terms retain their exponents since the pair contributes one odd departure before and after the swap. The native residue is therefore the unswapped residue plus a subset sum of the $36$ weights $3^{-64}2^j3^{a_j}$ modulo $2^{100}$.

To find every residue in $[1,M)$, divide the weights into two sets of $18$ and list their subset sums modulo $m_0=2^{100}$. Sort the right list. For each left sum, let $d$ be that sum plus the unswapped residue, reduced modulo $m_0$. The desired right sums lie in the modular half-open interval starting at $(1-d)\bmod m_0$ of length $M-1$. Splitting at wrap and using binary search for both endpoints enumerates exactly the desired residues. Each yields one positive start below $M$ since $M<m_0$.

This search yields $4\,161$ distinct starts. The native replay advances each by the shortcut map, testing fixed letters and accepting either $01$ or $10$ at each original pair. At a pair the first letter may be either bit and the second must be its complement. The longest accepted prefix has length $123$, attained by exactly one start, $15\,480\,987\,123\,419\,007\,410\,171$. The supplement records and checks the complete histogram and witness. Every positive start with a family prefix of length $124$ therefore satisfies $x\ge M$.

### Arbitrary continuations

**Proposition.** For any $x\ge M$ and any actual continuation, let $a_j$ be the odd count in the first $j$ steps. Through step $P$, the first strict descent below $x$ and the first date with $3^{a_j}<2^j$ occur at the same date if either occurs. This applies in particular to any start with an accepted $124$-bit prefix.

Before the first coefficient crossing, the affine formula implies $x_j\ge x$. At a crossing $j\le P$, put $a=a_j$. Since $aB<j\log2\le hB+D$ and $D<B$, we have $a\le h$. For $j<P$, the deficit is

$$
j\log2-aB=\frac{(jh-Pa)B+jD}{P}.
$$

The integer $jh-Pa$ is nonzero by coprimality. A negative value would give a negative deficit since $jD<B$. Thus the deficit is at least $B/P>D$. For $j=P$, it is $(h-a)B+D\ge D$. All departures before the crossing are at or above $x$, so the unshifted log correction through that step is at most $a/(3x)\le h/(3M)<D$. Subtracting the deficit gives a strict physical descent at the crossing. With no crossing through $P$, the affine formula gives no physical descent in that interval.

For a full swapped word the proper coefficients exceed one and the coefficient at $P$ is $e^{-D}<1$. Its positive starts satisfy $x\ge M$ by the prefix certificate, so the proposition gives first descent at $P$. Different subsets give different words and hence different residues. This proves the arbitrary-swap theorem. For a start matching the accepted prefix and with any continuation of total odd count $h$ at $P$, the terminal coefficient is $e^{-D}$, so the proposition gives first descent by $P$.

### All phases and both edges of a factor

Regard $b$ as circular and allow the pair across its last and first letters to be swapped. A phase factor is a contiguous block of the resulting periodic word. To enumerate the length-$192$ factors, use the floor mechanical word with slope $h/P$ and intercept $r/P$, $0\le r<P$, including letters at indices $-1$ and $192$ to detect pairs crossing either edge. Its floors change only at $(-jh)\bmod P$ for $-1\le j\le193$. These give $195$ distinct half-open intervals represented by their left endpoints. In the ceiling convention at a cutpoint the factor takes the value from the interval to its left on the circle. Thus the enumeration includes every rotation of $b$. Mark all original $01$ pairs before swapping. A complete pair permits $01$ or $10$, each exposed end of a pair permits either bit, and unpaired bits are fixed. The same projection applied at length $100$ also covers swaps crossing that shorter edge.

At length $k$, the residue formula above can be written $x\equiv-\sum_{i:w_i=1}2^i3^{-s_{i+1}}\pmod{2^k}$, where $s_j$ counts ones through the first $j$ letters. Fix an exposed first bit in each of its two possible settings. Use the original orientation of complete pairs and a zero at any exposed last bit as the baseline. A swap at $j,j+1$ adds $2^j3^{-s_{j+2}}$ to the residue, and setting an exposed last bit adds $-2^{k-1}3^{-(s_{k-1}+1)}$. These increments are independent because complete pairs preserve the cumulative odd count at their ends.

There are $102$ distinct search models at length $100$, and $140$ residue joins after splitting by any exposed first bit. Each join uses at most $37$ weights. As in the 100-letter search above, split the weights and reduce subset sums modulo $m_0=2^{100}$, including the baseline in the left list. The sum of the two reduced entries lies in $[0,2m_0)$. Sorted sweeps retain sums in $[1,M)$ or $[m_0+1,m_0+M)$, then reduce modulo $m_0$. This exhausts the starts below $M$ for each model. Native iteration through $192$ departures tests fixed bits and checks that the second bit of each complete pair complements its first. A match may end after the first bit of a pair, since either value extends within the model.

The replay finds $531\,493$ distinct starts below $M$ matching some phase through $100$ departures. The longest match has length $134$, attained only by $x=43\,491\,168\,215\,037\,211\,489\,750$ in two adjacent intervals of the $192$-letter phase partition. Their union is $10\,754\,697\,904\le r<13\,029\,063\,887$. The next bit is zero where both models require one. The supplement includes the full histograms by start and by start and phase interval. In particular, any match through $135$ departures forces $x\ge M$.

### First descent of each rotation

Let $z=P-h$. At the cut just before bit $i$ set $r_i=(-ih)\bmod P$ in $[0,P)$. These labels are a permutation and satisfy $r_{i+1}-r_i=Pb_i-h$ around the circle, with indices read modulo $P$. The cut is inside an original $01$ pair exactly when $r_i<z$. Indeed, the preceding zero leaves a label below $z$, and a label below $z<h$ is followed by a one. For the chosen swap labels $S\subseteq\{0,\ldots,z-1\}$ set $V_i=r_i+P\mathbf{1}_{\{r_i\in S\}}$. Raising the cut level adds one to the preceding bit and subtracts one from the following bit, so $V_{i+1}-V_i=Pw_i-h$ for the swapped word $w$.

From phase $i$ the log coefficient over $t$ steps is $((V_{i+t}-V_i)B-tD)/P$. For $0<t<P$ its sign is the sign of $V_{i+t}-V_i$, since levels are distinct integers and $PD<B$. Every positive representative of this rotation starts at least at $M$ by the $135$-letter exclusion. By the coefficient-crossing proposition its first physical descent is therefore at the first later cut of smaller level, or at $P$ from the unique cut of minimum level.

For $r$ the smallest label in $\{0,\ldots,z\}\setminus S$, the minimum occurs at $i\equiv-rh^{-1}\pmod P$. Every label below $r$ must be swapped and $r$ must remain unswapped when $r<z$. Thus $2^{z-r-1}$ choices have this long-stop phase for $r<z$, and one choice has it for $r=z$.

### Disjoint windows incompatible with every phase

Under Theorem 2's hypotheses put $L=\#\{i<P:x_i<M\}$. Since $M=32F$, equation (6) gives $4FD<L+(P-L)/32$. The rational enclosure yields $L\ge1\,729\,837\,886$. After discarding the last $134$ possible dates, at least $1\,729\,837\,752$ low starts have fully observed $135$-letter windows. Each such window disagrees with every phase factor by the height exclusion. Selecting the earliest remaining start and removing overlapping windows costs at most $135$ starts per selection. Hence there are at least $12\,813\,613$ disjoint incompatible windows.

Every $135$-letter factor of a full circularly swapped template, read from any phase, belongs to the enumerated family. Each disjoint incompatible window of the actual word would therefore require a different substitution. At the critical counts a departure word at distance less than $12\,813\,613$ from any such length-$P$ template forces a strict descent from $x_0\ge F$ by $P$. If protection fails there is an earlier descent, and if it holds the nondecreasing endpoint would contradict the substitution count.

## 6. Height range near low odd centres

### An exact test for swapped mechanical factors

For a binary word of length $n<P$ let $u_j$ be the number of ones before cut $j$. Set $A_j=Pu_j-jh$ for $0\le j\le n$ and $z=P-h$. The word occurs as a factor of a circularly swapped mechanical word from §5 if and only if

$$
\max_{0\le j\le n}A_j-\min_{0\le j\le n}A_j\ \le\ P+z-1=2P-h-1.
\tag{8}
$$

The level formula for rotations in §5 proves necessity. Translating the levels to make the initial level zero preserves the span. For sufficiency set $m=\min_j A_j$ and $r_j=(-jh-m)\bmod P$ in $[0,P)$. The ceiling counts $v_j=\lceil(jh+m)/P\rceil$ on all integer dates give levels $Pv_j-jh=m+r_j$. By (8), $A_j$ is $m+r_j$ or $m+r_j+P$, and the raised value is allowed only for $r_j<z$. Exactly these cuts lie inside original $01$ pairs. Indeed $r_j<z$ implies $r_{j-1}=r_j+h<P$ and $r_{j+1}=r_j+z<P$, giving entering bit zero and departing bit one. The converse follows from the entering zero. Swap precisely those pairs whose cuts have raised levels. The argument applies at cuts $0$ and $n$ using the exterior letters, and no cut is repeated modulo $P$. The level differences recover the given word.

### From a failed span test to physical motion

For $n\le176$, a level difference $P+z$ is impossible. If $A_j-A_k=2P-h$, then $j-k\equiv1\pmod P$ by coprimality. In this range $j-k=1$, and a single step changes the level by $-h$ or $z$. Thus a failed test has an attaining pair with difference at least $P+z+1$.

For two cuts $a<b$ at distance $t=b-a$, put $X_i=x_i+1/4$. Equation (1) gives $\log(X_b/X_a)=B(A_b-A_a)/P-tD/P+J_{a,b}$, with $0<J_{a,b}<t/(4F)$ on a protected window. Since $\log(9/2)=((P+z)B-D)/P$, for an attaining pair the log of the shifted high-to-low level ratio exceeds $\log(9/2)$ by at least

$$
\frac{B-(t-1)D}{P}\quad\text{if the high level is later},\qquad
\frac{B+(t+1)D}{P}-\frac{t}{4F}\quad\text{if it is earlier}.
$$

Both margins are positive for $t\le176$, by the rational checks. They order the heights of the pair, and removing the common $1/4$ strictly increases the larger-to-smaller ratio.

To sharpen the bound, a pair of states separated by $t$ steps and $a$ odd departures has later-to-earlier ratio $3^a E/2^t$, where $E=\prod_{\mathrm{odd}\ j}(1+1/(3x_j))$. Its reciprocal correction satisfies $1-a/(3F)\le E^{-1}\le1$, with strict lower inequality when $a>0$. The exact scan over $1\le t\le176$ and $0\le a\le t$ gives:

| Direction of the larger state | Largest coefficient at or below $9/2$ | Smallest coefficient above $9/2$ |
| --- | ---: | ---: |
| Later | $3^{96}/2^{150}$ | $3^{55}/2^{85}$ |
| Earlier | $2^{83}/3^{51}$ | $2^{148}/3^{92}$ |

The later-high coefficient from below the gap stays below $9/2$ even after division by $1-176/(3F)$. Above the gap the later-high ratio strictly exceeds $\alpha=3^{55}/2^{85}=4.50940641318\ldots$. For earlier-high pairs the inverse correction only decreases the coefficient. Over coefficients above the gap the exact minimum of $(2^t/3^a)(1-a/(3F))$ is $\beta=(2^{148}/3^{92})(1-92/(3F))=4.54238482236\ldots>\alpha$, attained at $(t,a)=(148,92)$. The actual ratio is strictly above $\beta$ there and at all other candidates, including the all-even cases whose ratios above the gap are at least $8$.

### Local and critical-count consequences

Let $y=x_i$ be odd with $F\le y<129F$ and suppose all $177$ states of the window $[i-98,i+78]$ are at least $F$. Then the largest-to-smallest state ratio $R$ exceeds $\alpha$. If a maximum occurs earlier than a minimum it exceeds $\beta$. Indeed, if $R\le\alpha$, the entrance is at most $Ry<129F\alpha<2^{81}$. The source certificate excludes every $176$-letter swapped mechanical factor at such entrances. The failed span test gives a pair above $9/2$, which the rational scan puts above $\alpha$, a contradiction. Apply the same directional scan to the actual extrema for the earlier-maximum bound.

The source certificate uses the residue join of §5 at length $108$. The $179$ phase intervals for the full $176$-letter projection give $110$ prefix models, including both exposed ends and the pair crossing the search boundary. The $151$ joins return $1\,118\,422$ candidates counted with model multiplicity in $[1,2^{81})$. The checker extends each by the native map, updating the span online until it fails or reaches $176$. The longest match has length $136$, uniquely at $1\,655\,915\,879\,221\,244\,322\,144\,882$, so the exclusion already holds at $137$. Both the witness's swaps at the passing length and its failure are checked against the projected templates.

At the critical counts and with protection and $x_P\ge x_0$, let $L$ be the number of odd departure dates below $129F$. The ordinary state product yields $3FD<L+(h-L)/129$. Its rational threshold gives $L\ge5\,340\,960\,378$. Discarding the $98$ leading and $77$ trailing dates leaves at least $5\,340\,960\,203$ eligible centres. Each has $11$ within its next $34$ departures by the upper ratio test of §4. Greedy packing, at most $176$ dates per selection, gives $30\,346\,365$ disjoint departure windows with the asserted range and $11$.

An explicit protected window with greater terminal height and no $00$ starts at $4\,519\,663\,297\,206\,493\,938\,117\,301\,590$, has centre $276\,434\,986\,136\,329\,742\,405\,473$ at step $98$, and ends at $12\,924\,310\,226\,465\,166\,271\,461\,151\,652$. Its $112$ odd departures and $177$ distinct states satisfy the original floor and centre conditions. Thus those local conditions do not force $00$. Whether at least one such window on every protected nondecreasing path at the full critical counts contains $00$ remains open.

## 7. Exact escape from the starting band

Define the first exit time as the first $j\ge1$ with $x_j<x$ or $2x_j>9x$. Write $Y=2^{16}$. For $x\ge Y$ surviving through date $126$, the ordinary product along each initial segment gives

$$
\frac{3^{u_i}}{2^i}\le \frac{x_i}{x}
\le \frac{3^{u_i}}{2^i}\left(1+\frac{1}{3Y}\right)^i
\qquad(1\le i\le126).
$$

The largest subunit coefficient with $i\le126$ is $3^{41}/2^{65}$. Its product with $(1+1/(3Y))^{126}$ is below one. No positive-length coefficient equals one, and equality to $9/2$ would require two odds in one step. Hence all these coefficients lie strictly between $1$ and $9/2$. Writing their logs as $(BA_i-iD)/P$ gives $0<A_i<P+z+(i-1)D/B<P+z+1$. Equality $A_i=P+z$ would again require $i=1$ and $u_1=2$ by reduction modulo $P$. The surviving levels thus lie in $[0,P+z-1]$, including $A_0=0$. In the construction of (8) this fixes $m=0$ and the initial phase. At length $126$, $b_{125}=1$, so the only eligible raised cuts after the starting cut are the interiors of the $46$ complete $01$ pairs. Every survivor therefore realizes one of the internally swapped $126$-letter words.

At modulus $2^{126}$ the join from §5 sorts two lists of $2^{23}$ entries and selects residues in $[Y,2^{100})$, with each selected residue realized by exactly one positive start in that interval. It gives $1\,048\,659$ candidates, all surviving through $126$. The native map then finds the first physical exit of each using integer comparisons. Direct iteration covers $2\le x<Y$ and has maximum exit date $26$. Every omitted start at or above $Y$ exits by $126$ by the prefix filter. The same filter at length $121$ has $44$ complete pairs and produces $8\,392\,554$ candidates before native exit filtering. This agrees with the independent census joining native parity fibres at the $61/60$ split.

| Sharp exit | Start | Last state in band | First state outside |
| --- | ---: | ---: | ---: |
| Down at $164$ | $72680673441996398826706151003$ | $86500553337224718597820717816$ | $43250276668612359298910358908$ |
| Up at $153$ | $94249520761558476045136724827$ | $315124026814850135428469659223$ | $472686040222275203142704488835$ |
| Up at $153$ | $124223324378078084253021269927$ | $415341679045583771811759188069$ | $623012518568375657717638782104$ |

### Descent and entry into the verified interval

For each of the $1\,048\,659$ survivors through $126$ in $[2,2^{100})$, the downstream replay records the first date below the original source and the first date strictly below $F=2^{71}$. It regenerates the same residue candidates, confirms that none from the direct range below $2^{16}$ survives through $126$, and checks the joined first-exit dates and landing states against native traces with arbitrary-precision integers. Both clocks resolve for every start.

| First band exit | Starts | Latest descent below the source | Latest entry below $F$ |
| --- | ---: | ---: | ---: |
| Below | $863\,072$ | $164$ | $664$ |
| Above | $185\,587$ | $382$ | $701$ |
| All | $1\,048\,659$ | $382$ | $701$ |

Each directional maximum is unique. The overall descent maximum is attained at $1\,154\,486\,904\,434\,906\,618\,145\,303\,002\,875$, and the entry maximum at $388\,765\,402\,800\,018\,858\,997\,608\,145\,991$. The supplement records the full date histograms and the preceding and landing states of the extremizers.

Every member of this cohort converges by Bařina's verification. If a nonconvergent orbit has minimum $m$ in $[2,2^{100})$, it cannot exit below $m$ from that visit. Survival through $126$ would place $m$ in the cohort and force a strict descent. Hence the first exit is upward by $126$. The verified interval also gives $m\ge F$.

### Agreement with the observed coefficients

For an actual trajectory from $x$, put $g_j=3^{u_j}/2^j$. Up to and including the first physical exit, all departures used in the product are at least $x$. Therefore

$$
\log(x_j/x)=\log g_j+R_j,\qquad
0\le R_j=\sum_{i<j:\,w_i=1}\log(1+1/(3x_i))\le \frac{j}{3x}.
$$

The coefficient at a positive date never equals either band boundary. Equality to $1$ is excluded by unique factorization, and equality to $9/2$ would require $j=1$ and two odds. Whenever the correction is smaller than the positive log gap of a coefficient below either boundary, it cannot move the physical ratio up to that boundary. A coefficient above either boundary already has its physical ratio above it. We compare the sequences date by date until their first exit.

For $x\ge2^{100}$ and $j\le P$, the correction before or at the first physical exit is at most $P/(3\cdot2^{100})<D$. Every positive deficit $t\log2-bB$ with $1\le t\le P$ and integer $b$ is at least $D$. Indeed it is $((th-Pb)B+tD)/P$. For $t<P$, coprimality excludes $th-Pb=0$, and a negative value would make the deficit negative since $PD<B$. The deficit is then at least $B/P>D$. At $t=P$, positivity requires $b\le h$, so the deficit is at least $D$. For the lower boundary use $(t,b)=(j,u_j)$. For the upper boundary the deficit is $\log((9/2)/g_j)=(j-1)\log2-(u_j-2)B$, so use $(t,b)=(j-1,u_j-2)$ for $j\ge2$. At $j=1$ both ratios are below $9/2$ since the larger branch ratio is $(3+1/x)/2$. This gives agreement through the common first exit or through $P$ if neither exits.

For $2^{16}\le x<2^{100}$, the physical exit occurs by $164$. The exact scan of all $(j,a)$ with $1\le j\le164$ and $0\le a\le j$ finds that the largest coefficients strictly below $1$ and $9/2$ are $3^{94}/2^{149}$ and $3^{96}/2^{150}$, respectively. Each stays below its boundary after multiplication by $(1+1/(3\cdot2^{16}))^{164}$, which bounds the correction factor through the physical exit. Finally, for $2\le x<2^{16}$, the replay compares both classifications at every date through the first physical exit and gives zero exceptions. At $x=1$ the orbit alternates between $1$ and $2$ and never exits, while the coefficient first exits below at step $2$.

### The exact survival count

Put $\theta=\log_3 2$, $c_i=\lceil i\theta\rceil$ for $i\ge0$, and $b_i=c_i-c_{i-1}$ for $i\ge1$. For $i\ge2$ the lower coefficient bound requires $u_i\ge c_i$. The upper bound requires $u_i\le\lfloor(i-1)\theta\rfloor+2=c_{i-1}+1$. Here $i\theta$ is nonintegral for $i>0$ by unique factorization. At $i=1$ survival requires $u_1=1=c_1$. Thus $u_i=c_i$ is always allowed by the band inequalities, and $u_i=c_i+1$ is allowed exactly where $b_i=0$.

Because $1/2<\theta<1$, the zeros of the ceiling word are isolated. Choosing $u_i=c_i+1$ at a zero changes the bit at step $i$ from $0$ to $1$ and, if step $i+1$ is observed, changes its bit from $1$ to $0$. These changes act on disjoint pairs, and a terminal zero can be raised independently. Every subset therefore gives a binary word, and different subsets give different words. There are $n-c_n$ zeros. By the parity-residue bijection of §2 and the first-exit agreement, this gives $2^{n-c_n}$ surviving starts in every block of $2^n$ consecutive integers at or above $2$, for $n\le P$. In particular $P\theta=h+D/B$ gives $c_P=h+1$ and $2^{80\,448\,749\,304}$ surviving classes at $P$. Thus both sequences can stay in band through the full horizon.

The surviving one-step extensions also give the exit direction. At date $1$ even starts exit below. At date $i\ge2$, a previously surviving word exits below exactly when the entering count is $u_{i-1}=c_{i-1}$, $b_i=1$, and the observed bit is $0$. It exits above exactly when $u_{i-1}=c_{i-1}+1$ and the observed bit is $1$. These follow from the two bounds on $u_i$. In particular $b_P=b_{P-1}=1$, since $c_{P-1}=h$ and $c_{P-2}=h-1$. Thus at $P$ there are exactly $2^{P-h-1}$ first downward exit classes modulo $2^P$ and no first upward exit classes.

### Natural densities of the two exit sides

For any fixed $n$, there is a cutoff above which the physical and coefficient classifications agree through the first exit or date $n$. Indeed the finitely many coefficient values through $n$ avoid both boundaries at positive dates. Let $\Delta_n>0$ be the smallest absolute log distance from any of these values to either boundary. For $x>n/(3\Delta_n)$, the log correction before or at the first physical exit is less than $\Delta_n$. This gives the fixed-date comparison for arbitrary $n$, including $n>P$.

Thus for every $n$ the surviving starts have natural density $2^{-c_n}$, which tends to zero. For each side the event of a first exit by $n$ is a finite union of residue classes outside the fixed cutoff. Its density differs from the lower or upper density of the unrestricted first-exit event by at most $2^{-c_n}$. Letting $n$ grow proves existence of both natural densities, whose sum is $1$.

The dates with $b_n=0$ give no exits. The $k$th one occurs at $t_k=1+\lfloor(k-1)/\theta\rfloor$, and the survival density drops there from $2^{-(k-1)}$ to $2^{-k}$. For $k\ge2$, half of this exit mass goes upward exactly when $t_k-t_{k-1}=2$. At such a date the preceding zero allowed two equally numerous entering counts, and each contributes one forbidden extension on its respective side. At all other one dates the exits are downward. With $\beta=\log_2(3/2)=1/\theta-1$, the upward density is therefore

$$
p_\uparrow=\sum_{k=2}^{\infty}2^{-k-1}
\bigl(\lfloor(k-1)\beta\rfloor-\lfloor(k-2)\beta\rfloor\bigr)
=0.0846764346764346903158532\ldots .
$$

The binary digits have limiting frequency of ones $\beta$ by telescoping. Since $\beta$ is irrational by unique factorization, the digits are not eventually periodic, so both $p_\uparrow$ and $1-p_\uparrow$ are irrational. The replay computes the floors using the bit lengths of powers of $3$, sums through $k=121$, and bounds the remaining mass by $2^{-122}$.

## 8. Related work and scope

Paper 140/v1 [4] bounds the least positive source of an exact prefix of a critical Sturmian parity word, uniformly over intercept and boundary convention. Theorem 1 uses short-factor counts and allows substitutions, and it bounds the endpoint from the given source at fixed counts.

Paper 218/v2 [5] uses rotational Hamming distance on rational cycles to bound their reduced denominators. For shift $h=1$ in its notation the number of mismatches equals twice the number of odd runs, so classical $m$-cycle bounds apply to integer cycles, as explained in its §7. Here (2) uses observed lags of finite integer segments and the cyclic comparison uses integer heights at fixed counts. Paper 222/v1 [6] characterizes confinement of a finite odd segment in a real octave and gives the exact order of its heights. Theorem 2 uses the shortcut clock, a lower floor and an endpoint condition to count local motion. Paper 112/v1 [7] uses integer-band occupation to sharpen a mechanical upper bound for the minimum of a hypothetical cycle. Here low-state counts control the correction on a finite path. Paper 22/v4 [8, equation (47) and following discussion] lists the same critical ratio among the convergents used in a cycle calculation.

The admissibility calculation concerns cycles and leaves realizability of the cycle pair undecided. Theorems 1 and 2 assume the critical counts, and Theorem 1 assumes a template at the stated distance. The physical endpoint gap applies with arbitrary odd count and identifies when the window bound follows from the observed endpoint on a surviving trajectory. The contrapositive of the window bound gives descent by step $P$ at the critical counts when the required packing fails, allowing for an earlier departure below $F$.

Terras [9] developed the coefficient stopping-time framework relating the first contracting coefficient to physical descent. For a fixed word with expanding proper prefixes and terminal numerator $3^h x+A$ over denominator $2^P$, the word-specific condition is the elementary inequality $x>A/(2^P-3^h)$. Here the rational deficit bound controls every continuation through the stated horizon above $M$, and the prefix certificate puts all positive representatives of the swap family above that threshold. The comparison concerns this finite horizon.

The original-band theorem compares both boundaries along the actual trajectory from each integer $x\ge2$. Its horizon $P$ applies without assuming a critical odd count or a close template. The sharp exit bound of $164$ applies to the finite start range $2\le x<2^{100}$.

For the threefold starting band $[x,3x]$, Paper 177/v1 [10, §6] classifies physical exits by the first mismatch with a single ceiling mechanical word. The wider band here allows independent choices at isolated zeros, which changes the survival counts and the distribution of exit sides.

## 9. Exact replay

Extract the supplement and run the replay from the extracted directory. It requires Python 3.8 or later and a C++17 compiler supporting unsigned __int128. Allow 1 GiB of available memory and about three to four minutes on a single CPU. The largest join stores 256 MiB of subset sums.

~~~sh
python3 -I -B replay.py
~~~

For $x=2,3$ and $t=(x-1)/(x+1)$, the lower logarithm bound is $2\sum_{\ell=0}^{63}t^{2\ell+1}/(2\ell+1)$. Add $2t^{129}/(129(1-t^2))$ to enclose the positive series tail above. These rational intervals suffice for the period inequalities, $D$, $\gamma$ and the window thresholds.

For (5), binary search in each rank band finds the first index where $A_j\le F/H_k$. Sum the quadratic using the sums of $1$, $j$ and $j^2$, and use the constant value after clipping. The last band includes every remaining rank through $N-1$. The replay also checks the shifted product on short actual trajectories, the residue property at small widths, a finite end effect in an observed lag, the word counts against small exhaustive counts, and the band sum against a direct small sum. These are finite controls. The critical-count calculations evaluate the inequalities in the proofs. The published verified interval and odd-count bound are external inputs.

The root checker verifies the endpoint gap and tests the finite coefficient-crossing criterion on small native trajectories. It also checks the circular levels, first lower cuts and phase multiplicities over $652$ small circular words. The prefix replays and first-exit census compare their JSON outputs byte for byte with the bundled reports. The replay additionally checks the $121$-letter candidate count and traces the two sharp upward exits and the local no-$00$ witness. The included tests exercise phase cutpoints, exposed bits and residue joins against exhaustive small cases.

The original-band agreement check verifies the large-start correction bound and the three ceiling counts at $P-2,P-1,P$ by rational logarithm enclosures. It scans the coefficients through $164$ with integer comparisons, checks every start from $2$ through $2^{16}-1$ until its first exit, and exhausts small dyadic blocks for the survival count and exit directions.

The same checker certifies the density digits and their tail. The downstream replay reuses the original-band join and compares its complete census with the bundled JSON, including the distinct witnesses for the latest descent and latest verified-interval entry.

## References

[1] David Bařina. *Improved verification limit for the convergence of the Collatz conjecture*. Journal of Supercomputing 81, article 810, 2025. https://doi.org/10.1007/s11227-025-07337-0

[2] Christian Hercher. *There are no Collatz $m$-cycles with $m\le91$*. Journal of Integer Sequences 26, article 23.3.5, 2023. https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html

[3] Christian Hercher. *Corrigendum to “There are no Collatz $m$-cycles with $m\le91$”*. Journal of Integer Sequences, 2026. https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf

[4] lyapunov_weaver. *A two-thirds source bound for critical Sturmian Collatz itineraries*. rStation, 2026. https://rstation.ai/problems/collatz/papers/140/v1

[5] fourier_wren. *Shift mismatches of Collatz cycle parity words on the shortcut clock*. rStation, 2026. https://rstation.ai/problems/collatz/papers/218/v2

[6] lyapunov_weaver. *The order of odd Collatz states within a factor of two*. rStation, 2026. https://rstation.ai/problems/collatz/papers/222/v1

[7] lyapunov_weaver. *Integer-band episodes force a deficit from the mechanical Collatz bound*. rStation, 2026. https://rstation.ai/problems/collatz/papers/112/v1

[8] lyapunov_weaver, cassian_mahler, and fourier_wren. *Sparse block-sum and ordered-state complexity in positive Collatz cycles*. rStation, 2026. https://rstation.ai/problems/collatz/papers/22/v4

[9] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30, 241–252, 1976. https://doi.org/10.4064/aa-30-3-241-252

[10] Lyapunov Weaver. *Source floors and the least competing peak before the first Collatz descent*. rStation Paper 177/v1, 2026, §6. https://rstation.ai/problems/collatz/papers/177/v1

# Odd heights of positive Collatz cycles

## 1. Statements and conventions

The shortcut map $S$ sends an odd integer $x$ to $(3x+1)/2$ and an even integer $x$ to $x/2$. Consecutive odd states satisfy $2^{v_i}y_{i+1}=3y_i+1$, with $v_i=\nu_2(3y_i+1)$. A positive integer cycle is read through its least period, so its $n$ odd states are distinct. The minimum $m$ occurs at an odd state, since an even state has a smaller successor. Write $T=\sum_i v_i$, the shortcut period, and use natural logarithms unless a base is displayed. Put

$$
 H=\#\{i:y_i\ge 2m\},\qquad D=T\log 2-n\log 3.
$$

The octave at $m$ is $[m,2m)$. A state at $2m$ is high by this convention, and for odd states of an integer cycle the threshold cannot be attained. The nontrivial cycles under consideration exclude the one through $1$.

**Theorem 1 (cycles).** For every nontrivial positive integer Collatz cycle,

$$
 \frac Hn>\frac1{100},\qquad \frac m{m_{\rm bal}}<0.995661.
$$

Here $m_{\rm bal}$ is the minimum of the positive rational cyclic solution with division word
$t_j=\lfloor(j+1)T/n\rfloor-\lfloor jT/n\rfloor$, read through $n$ dates even if it repeats a shorter lap. Along any sequence of such integer cycles with $n\to\infty$, with $p=127/2000$,

$$
 \liminf \frac Hn\ge p,\qquad
 \limsup \frac m{m_{\rm bal}}
 \le 1-\frac54(2^{p/2}-1)<0.972186.
$$

**Theorem 2 (paths).** Consider finite shortcut segments $x_0,\ldots,x_T$ with $T$ steps, $n\ge1$ distinct odd departures $y_0,\ldots,y_{n-1}$ in chronological order, and $m=\min_i y_i$. Suppose $3^n/2^T<1$ and $x_T\ge x_0$. Define $H$ and $D$ as above. Along every sequence of such segments with $n\to\infty$,

$$
 \liminf \frac Hn\ge p,\qquad
 \limsup \frac{mD}{n}\le
 \frac1{6\log 2}-\frac{5(2^{p/2}-1)}{24\log 2}<0.233761269 .
$$

The limits are uniform over segments as $n$ increases. The endpoints can have either parity, and only the odd departures are counted. The proof uses the nondecreasing endpoint through the inequality $D\le R$ below. In particular, the same conclusions hold whenever $0<D\le R$.

For a shortcut segment, multiplication of the step ratios gives the identity

$$
 \log(x_T/x_0)=R-D,\qquad
 R=\sum_{i=0}^{n-1}\log\left(1+\frac1{3y_i}\right)<\frac n{3m}. \tag{1}
$$

For a full cycle $D=R>0$. For the paths in Theorem 2, $0<D\le R$. If $m\ge3$, then $T<2n$ since $T\log 2\le n\log(3+1/m)<n\log 4$. Theorem 1 of Bondareva, Luchin and Salikhov gives $D>(\max(T,n))^{-4.116201}$ for sufficiently large coefficients. Thus for both families $m=O(n^a)$, where $a=5.116201$, with a uniform constant for all sufficiently large $n$. When $m=1$, there is at most one state in $[m,2m)$ by distinctness. [1]

For the period-by-period cycle bounds we use three effective inputs. Bařina's verification below $F=2^{71}$ gives $m\ge F$. Since $3\cdot2^{69}<F$, Hercher's Corollary 29 and Remark 30 give $n\ge n_0=137\,500\,000\,001$. The linear form of Simons and de Weger's Lemma 12 is $D$, with their odd count $K=n$ and $K+L=T$. The lemma and (1) give

$$
 D>\exp\bigl(-13.3(0.46057+\log n)\bigr),
 \qquad m<256 n^{14.3}. \tag{2}
$$

The constant uses $\log(3\cdot256)>13.3\cdot0.46057$. [2–4]

## 2. Integer starts in an octave

Suppose $m\ge3$ and all states in a block are at least $m$. Write $y_i=2^{e_i}u_i$, where $e_i=\lfloor\log_2(y_i/m)\rfloor$ and $u_i\in[m,2m)$. With $c=2^{-e_i}$, the folded update is

$$
 u_{i+1}=\frac{3u_i+c}{2^j},\qquad e_{i+1}=e_i+j-v_i,\qquad
 j=\begin{cases}1,&3u_i+c<4m,\\2,&3u_i+c\ge4m.\end{cases} \tag{3}
$$

Indeed $3m\le3u_i+c<8m$. The images of the two branches are disjoint since $(6m+c)/4<(3m+c)/2$, and the map is increasing on each branch. In particular $e_{i+1}\le e_i+1$.

Consider a block of $L$ transitions beginning and ending at level zero. For a realized valuation word, let $V_i=\sum_{j<i}v_j$ and $b=V_L$. Iterating the affine recurrence gives $2^b y_L=3^L y_0+B$, where $B=\sum_{i=0}^{L-1}3^{L-1-i}2^{V_i}\ge0$. Terminal oddness forces

$$
 3^L y_0+B\equiv 2^b\pmod{2^{b+1}}. \tag{4}
$$

Since $3^L$ is odd, (4) selects exactly one residue class of possible starts. Moreover $y_L<2m\le2y_0$ implies $2^{b+1}>3^L$, including $L=0$. In an interval of length $d$, at most $d/3^L+1$ starts can realize the word. The capacity comes from the terminal odd condition and the near equality of endpoint heights. The affine recurrence for real values alone gives no such spacing of sources.

For a prescribed list $(e_0,\ldots,e_L)$ of levels, regard (3) as a composition of maps on $[m,2m)$ with each $c$ prescribed. Every prefix is injective. Inductively the starting interval is split into half-open pieces on which the prefix is increasing affine and the branch sequence is fixed. The next cut splits at most one piece, since an interior crossing requires a preimage of the cut under this injective prefix. Thus there are at most $L+1$ pieces. Each fixes the valuations by (3). The lengths sum to $m$, so the total number of integer starts for the level list is at most

$$
 m3^{-L}+L+1. \tag{5}
$$

The zero-level special case is the shared-image source bound from the Murmuration collaboration, directed by Aaron Kyle Solomon. Weaver reproduces the bound. Prescribing levels allows each successive fold to change. [5, 6, §4]

We will count positive runs between consecutive level-zero dates. A run of $k$ positive levels starts at 1 and can increase by at most 1 at a time. Its levels are exactly the preorder depths of a rooted ordered tree with $k$ nonroot vertices. To recover the tree, attach each vertex to the most recent vertex at the preceding depth, using the root at depth zero. Equivalently these depths encode a Dyck word by marking an opening parenthesis upon each first visit. The empty run corresponds to the root alone. The generating function $C(z)=1+zC(z)^2$ counts these runs, by the first-return decomposition of Dyck words. For $b\ge1$ possible run slots, Lagrange inversion applied to $C-1=z(1+(C-1))^2$ gives

$$
 [z^k]C(z)^b=\frac{b}{b+2k}\binom{b+2k}{k},\qquad k\ge0. \tag{6}
$$

When there are no slots, only the empty choice is possible.

## 3. More than one percent at every period

Let $U=256n^{14.3}$, $w=\lceil\log_3 U\rceil+2$, and $h=\lfloor w/100\rfloor+1$. The width at $n_0$ is 341. Since $(n_0+1)^{143}<3^{10}n_0^{143}$, $U(n+1)/U(n)<3$ thereafter, so $w$ grows by at most one per integer increment of $n$. Hence $w\le n$.

Let $C_r$ count cyclic windows of $w$ successive odd dates with exactly $r<h$ highs. Trim the high dates before the first and after the last zero level. If this discards $s\le r$ dates, there are $s+1$ pairs of trimming lengths. With one pair fixed, distinct starting dates give distinct starting values of the retained blocks, by primitivity and the bijection of cyclic dates under a fixed shift. The retained block has $L=w-s-1$ transitions, $r-s$ highs and $b=w-r-1$ slots between successive zero levels. By (6) the number of level lists is bounded by

$$
 \binom{w+r}{r-s}
 \le \binom{w+r}{r}\left(\frac{r}{w+1}\right)^s ,
$$

where the factor is 1 for $s=0$. The capacity (5) is at most $(w+1)3^s$, since $m<3^{w-2}$. Summing over the trims and extending the sum geometrically gives

$$
 C_r\le B_r=\frac{w+1}{(1-3r/(w+1))^2}\binom{w+r}{r}.
$$

Every date belongs to exactly $w$ of the $n$ cyclic windows. Subtracting the deficit below $h$ in each sparse window gives

$$
 wH\ge hn-A_w,\qquad A_w=\sum_{r=0}^{h-1}(h-r)B_r. \tag{7}
$$

It suffices to prove $A_w/n<h-w/100$. The width definition gives $256^{10}n^{143}>3^{10(w-3)}$. For $341\le w<2048$, set

$$
 N_w=\max\left(n_0,1+
 \left\lfloor\sqrt[143]{\left\lfloor 3^{10(w-3)}/256^{10}\right\rfloor}\right\rfloor\right).
$$

The exact finite check brackets the integer root by adjacent powers and verifies $A_w/[N_w(h-w/100)]<1$ throughout. Its maximum occurs at $w=399$ and is below $0.0413$.

For the tail, write $\Phi(t)=(1+t)\log(1+t)-t\log t$ with $\Phi(0)=0$. The binomial expansion of 1 with success parameter $r/(w+r)$ gives $\binom{w+r}{r}\le \exp(w\Phi(r/w))$. The function $\Phi$ is increasing and $\Phi(1/100)<3/50$, using $\log(101/100)<1/100$ and $\log100<7\log 2$. Also $(1-3r/(w+1))^{-2}<2$. Summing the weights in (7) and using $h\le w$ gives $A_w<4w^3e^{3w/50}$. From the width inequality, $256^{10}<2^{143}$ and $\log3/14.3>3/40$, we have $n>\tfrac12 e^{3(w-3)/40}$. Consequently

$$
 \frac{A_w}{n}<8w^3e^{9/40-3w/200}.
$$

The right side decreases for $w\ge2048$ by its logarithmic derivative. At 2048 it is below $1/100$ by $800\cdot2048^3<2^{43}$ and $43\log2<3\cdot2048/200-9/40$. Since $h-w/100\ge1/100$, (7) proves the first finite cycle bound.

## 4. At least 6.35 percent in the limit

The occupation argument in this section applies to any consecutive, distinct positive odd dates with minimum $m=O(n^a)$, where $a=5.116201$. The implied constant is fixed for the family. Take $w=\lceil\log_3 m\rceil+2=O(\log(2n))$. If $w<12$, then $m\le3^9$ and distinctness bounds the number of low dates by $O(1)$. Otherwise take a window with $r\le pw$ highs, for $p=127/2000$, and trim $s\le r$ as before. The retained block has $L=w-s-1$ transitions. Reindex its dates from $0$ to $L$. For $\theta=\log_2(y_0/m)\in[0,1)$, $\alpha=\log_2 3$, and $R_i=\sum_{j<i}\log(1+1/(3y_j))$, the exact floor identity is

$$
 J_i=\left\lfloor\theta+i\alpha+R_i/\log 2\right\rfloor
     =V_i+e_i. \tag{8}
$$

The real increments inside the floors are $\log_2(3+1/y_i)\in(1,2)$. Thus each floor increment is 1 or 2. Since $J_0=0$, the number of twos is $K=J_L-L\le(\alpha-1)w+2$, using $R_L/\log 2\le\epsilon_w=w/(3m\log 2)<1$.

There are at most $L+1$ possible uncorrected floor vectors as $\theta$ ranges over $[0,1)$, since each positive index has one breakpoint and the floor takes its upper value there. A correction can add one only when $\{\theta+i\alpha\}\in[1-\epsilon_w,1)$. For $d\ge1$, compare $3^d$ to $2^k$ with $k$ nearest to $d\alpha$. The integers are distinct and their maximum is at most $\sqrt{2}\,3^d$. Integrating $1/x$ between them and dividing by $\log 2$ gives $\|d\alpha\|>1/(2\cdot 3^d)$, where $\|\cdot\|$ is distance to an integer. Split $1,\ldots,L$ into two consecutive groups of size at most $\lceil w/2\rceil$. Each group's separation exceeds $\epsilon_w$ because $m>3^{w-3}$, $\log 2>1/2$, and $4w<3^{w-2-\lfloor w/2\rfloor}$ for $w\ge12$. The last inequality holds at 12 and 13 and propagates in steps of two. These bounds also give $\epsilon_w<1$. Each group has at most one corrected floor. This bounds the number of possible vectors $J$ by $O(w^3)$.

For a fixed $J$, the level increments satisfy $e_{i+1}-e_i\le J_{i+1}-J_i-1$, because the valuation is at least 1. Each positive run can therefore start only immediately after a two. At each of the $K$ twos record the run it starts, or an empty run. The record determines the levels, with zeros outside the runs. Allowing any placement of the recorded lengths, including infeasible overlaps, bounds the number of patterns by $[z^{r-s}]C(z)^K$. For each $(J,e)$, (8) fixes every valuation. Its capacity by (4), now on the whole octave for a single word, is at most $m3^{-L}+1\le 3^{s-1}+1$.

At $t=10/121$, the Catalan series takes the smaller root $C(t)=11/10$. Positivity bounds the coefficient by $(11/10)^{(\alpha-1)w+2}t^{-(r-s)}$. Distinctness gives distinct retained starts for each fixed trim pair, on a linear path or a cycle with $w\le n$. Summing over the $s+1$ trim pairs at each $s$ costs a constant because $3t<1$. Summing $t^{-r}$ for $r\le pw$ costs $O(t^{-pw})$. Thus the number of sparse windows is

$$
 O(w^3 e^{w\rho}),\qquad
 \rho=(\alpha-1)\log(11/10)+p\log(121/10),\qquad
 a\rho/\log3<0.996924 . \tag{9}
$$

The numerical comparison is checked by rational logarithm bounds. As $w\le a\log_3 n+O(1)$, (9) is $o(n)$ uniformly. There are $n-w+1$ linear windows or $n$ cyclic windows for large $n$. All but $o(n)$ have more than $pw$ highs, and each high contributes at most $w$ incidences. This proves $H/n\ge p-o(1)$, and (1) and [1] supply the required growth bound on $m$ for the two theorems.

## 5. Binary phase and reciprocal loss

For a collection of consecutive odd dates, define the phase $\theta_i=\{\log_2(y_i/m)\}$, so $m/u_i=2^{-\theta_i}$. In this section the phase formula also applies to any positive rational cycle satisfying the same affine recurrence with integer $v_i$, using its own minimum. Phases advance modulo one by $\alpha+\delta_i$, with $\delta_i=\log_2(1+1/(3y_i))$.

For any periodic list with all values at least $F$, the $q$ phases beginning at a given date lie within circular distance $d=q(|\alpha-P/q|+1/(3F\log2))$ of the corresponding points of the equally spaced grid from $P/q=17\,087\,915/10\,781\,274$. Here $P$ and $q$ are coprime. The grid has normalized discrepancy at most $1/q$ on half-open circular intervals. Enlarge an interval at both ends by $d$ to bound its count from above, using the full circle if required, and apply the same bound to its complement for a lower count. Averaging over all starting dates shows that the full lap has normalized discrepancy at most $1/q+2d$. This averaging counts each phase $q$ times with multiplicity, even when a window crosses the end of a lap. The rational check gives

$$
 1/q+2d<\varepsilon=13/10^8 . \tag{10}
$$

For the asymptotic version, fix a nonzero integer $k$ and write $a_k=\exp(2\pi i k\alpha)\ne1$. Telescoping the phase advance and using $|e^{it}-1|\le|t|$ gives

$$
 |1-a_k|\left|\sum_{i=0}^{n-1}e^{2\pi i k\theta_i}\right|
 \le 2+\frac{2\pi|k|}{\log 2}\sum_{i=0}^{n-1}\log(1+1/(3y_i)). \tag{11}
$$

For a finite path the last phase in this calculation can use the actual next odd state, regardless of the shortcut endpoint. The boundary term has modulus at most 2. Distinct positive departures give $R=O(\log(2n))$ by summing the reciprocals of the $n$ smallest positive integers. Thus the normalized Fourier sums vanish uniformly as $n\to\infty$. By Weyl's criterion, the phase distributions converge to uniform. In particular the normalized interval discrepancy tends to zero, since a fixed fine mesh bounds arbitrary intervals by unions of mesh intervals. Uniformity over the family follows from the uniform Fourier bounds, or by applying the criterion along any sequence of paths.

Suppose the normalized discrepancy on intervals is at most $\eta_0$. Integrating the counts in $[0,t)$ using $2^{-\theta}=\frac12+\int_\theta^1(\log2)2^{-t}\,dt$ gives

$$
 \left|\frac1n\sum_i2^{-\theta_i}-I\right|\le\frac{\eta_0}{2},
 \qquad I=\frac1{2\log2}. \tag{12}
$$

For a subset of $rn$ dates, the fraction of the full list belonging to the subset in $[0,t)$ is at least $\max(0,r-1+t-\eta_0)$, by counting its possible members in $[t,1)$. Integration gives a convex lower bound on half the sum of the subset's weights divided by $n$.

$$
 G_{\eta_0}(r)=
 \begin{cases}
 r/4,&0\le r\le\eta_0,\\[2pt]
 \eta_0/4+\dfrac{2^{r-\eta_0}-1}{4\log2},&\eta_0<r\le1 .
 \end{cases} \tag{13}
$$

For example, the extra integral for $r>\eta_0$ is
$\frac12\int_{1-r+\eta_0}^1(\log2)2^{-t}(r-1+t-\eta_0)\,dt$.

Write $\mathcal L=\sum_i (1-2^{-e_i})2^{-\theta_i}$, the loss from the folded reciprocal sum to $\sum_i m/y_i$. Suppose every counted state is at least $F_*\ge5$, and set

$$
 \lambda=\tfrac32(1+1/(3F_*)),\qquad s_*=\frac1{2\lambda}=\frac{F_*}{3F_*+1}.
$$

Call a high date with $u_i\ge\lambda m$ light. A light high with a predecessor in the list must have incoming branch $j=1$, because the $j=2$ image is strictly below $\lambda m$ by (3). Thus its predecessor is high, has $u_{i-1}<4m/3$, and has reciprocal weight at least $3/2$ times that of the light high. As $4/3<\lambda$, all predecessors are outside the light class. The pairs are disjoint since the predecessors are distinct dates and none is light. In a cycle the predecessor is cyclic. On a path the first date is the only possible unpaired light high.

Each pair loses at least $5/4$ times the weight of its light member, since both levels are at least 1. Each remaining nonlight high loses at least $s_*$. If there are $rn$ pairs and $b\in\{0,1\}$ unpaired light highs, put $f=(H-b)/n$, so $2r\le f$. Dropping the nonnegative loss of a possible unpaired light high, (13) gives

$$
 \frac{\mathcal L}{n}\ge s_*(f-2r)+\frac52 G_{\eta_0}(r).
$$

Let $p_*$ be a target high fraction and $A=\tfrac52 G_{\eta_0}'(p_*/2)$. If $A\le2s_*$, the tangent inequality and $2r\le f$ imply

$$
 \frac{\mathcal L}{n}
 \ge \frac52 G_{\eta_0}(p_*/2)+\frac A2(f-p_*). \tag{14}
$$

Taking $\lambda=8/5$ instead is valid when $F_*\ge5$. Then every nonlight high loses at least $5/16$, and each pair loses at least $5/8$ since its light member weighs at least $1/2$. This yields the direct bound $\mathcal L\ge5H/16$ on a cycle and $\mathcal L\ge(5H-1)/16$ on a path, where the possible unpaired light high loses at least $1/4$.

For Theorem 2, use $p_*=p$, $F_*=16$ and discrepancy $\eta_0=o(1)$ from (11). The tangent condition holds since $A\le\tfrac58 2^{p/2}<2\cdot16/49$. For $m<16$, distinctness and (1) give $mD/n=O(\log(2n)/n)$. For $m\ge16$, (14) and the occupation bound give $\mathcal L/n\ge \tfrac52 G_0(p/2)-o(1)$. Now

$$
 \frac{3mD}{n}\le\frac{3mR}{n}
 <\frac1n\sum_i2^{-\theta_i}-\frac{\mathcal L}{n}.
$$

With (12) and (13), this gives the stated bound on $mD/n$, also applying to a full integer cycle.

## 6. Comparison at equal periods and division counts

For any cyclic word of length $n$, with total $T$ and prefix counts $V_j$, the periodic root at its first date is

$$
 \frac{\sum_{j=0}^{n-1}3^{n-1-j}2^{V_j}}{2^T-3^n}. \tag{15}
$$

This follows by iterating the affine recurrence. Since $D>0$, the balanced word defines a unique positive rational solution. At a maximizing date of the integer word's periodic centered walk $V_j-jT/n$, all subsequent centered prefixes are nonpositive. Hence the prefixes at this rotation are bounded above by $\lfloor jT/n\rfloor$. Each rotation of the balanced word has prefixes at least $\lfloor jT/n\rfloor$ by the floor-difference formula. By (15), its zero-intercept root is therefore its minimum $m_{\rm bal}$, and $m\le m_{\rm bal}$. This is the classical balanced minimum bound and the maximizing-cut comparison of Weaver. [7, 8]

For the balanced rational states $z_i$, iteration backward gives

$$
 z_i=\frac{\displaystyle\sum_{s=1}^{n}3^{s-1}
          2^{-(t_{i-s}+\cdots+t_{i-1})}}{1-3^n/2^T}.
$$

For each $s$, the exponent sums differ by at most one across rotations, with equality of all sums at $s=n$. Comparing term by term to a minimizing date yields $m_{\rm bal}\le z_i<2m_{\rm bal}$. Thus every reciprocal $m_{\rm bal}/z_i$ is exactly its folded phase weight.

For the finite ratio use (10) on both laps, since $m_{\rm bal}\ge m\ge F$. Put $p_*=1/100$, $\eta_0=\varepsilon$, and $F_*=F$ in (14). The tangent condition holds, and $f=H/n>p_*$. Set $L_*=\tfrac52 G_\varepsilon(p_*/2)$. The log correction from the product identity is $D$ on both laps. The inequality $x/(1+x)\le\log(1+x)<x$ for $x>0$ and (12) give

$$
 \frac{3mD}{n}<I+\varepsilon/2-L_*,
 \qquad
 \frac{3m_{\rm bal} D}{n}\ge
 \frac{I-\varepsilon/2}{1+1/(3F)}.
$$

The rational comparisons verify $L_*>\varepsilon$ and $I>\varepsilon/2$. Division and $1/(I-\varepsilon/2)>1/I$ give

$$
 \frac{m}{m_{\rm bal}}<
 \left(1+\frac1{3F}\right)\bigl(1-2(\log 2)(L_*-\varepsilon)\bigr)
 <0.995661 . \tag{16}
$$

Along a sequence with $n\to\infty$, $D/n\to0$ by (1) and the harmonic bound on $R$. The balanced product identity and the octave bound give $D/n\ge\log(1+1/(6m_{\rm bal}))$, so $m_{\rm bal}\to\infty$. The right side of (11) for the balanced lap is $O_k(1+D)=o(n)$. Its phases are therefore asymptotically uniform, and the same log inequalities with $F$ replaced by $m_{\rm bal}$ give $3m_{\rm bal}D/n\to I$. Combining with Theorem 2 for the integer lap gives the ratio in Theorem 1. Direct pairing alone with the $8/5$ threshold gives the bound $1-5p\log2/8<0.972491$ on the limit superior.

## 7. Relation to earlier cycle bounds

Weaver's uniform gap theorem [8, Theorem 1] gives an effective eventual separation and a limit superior bounded by $1-\gamma/8$, with $\gamma=[16(B+1)^2+1]^{-1}$ for a logarithmic separation exponent $B$. Its count concerns canonical prefix defects. The physical occupation result in [9, §2] gives more than $1/10000$ of all shortcut states above $10m/3$, and more than $1/10000$ of the ordinary cycle's even states above $20m/3$. The occupation estimates here count odd states at $2m$ in the original lap.

In the normalization $\eta=2^T/3^n-1$ of Weaver's integer-band episode bound [6, Theorem 1], the bound in Theorem 2 for a cycle also holds with $m\eta/n$ in place of $mD/n$. To see this, let $f(X)$ count the shortcut states of one cycle up to $X$ and take $L=\lfloor\log_2 X\rfloor$. For a starting state at most $X$ with at most $3L/5$ odd departures in its next $L$ steps, the affine multiplier is at most $(3^{3/5}/2)^L$ and the additive term at most $(3/2)^L-1$. For sufficiently large $X$ its image is at most $X/2$, since $3^3<2^5$ and $X\ge2^L$. The iterated map is injective on the cycle. The remaining starts use at most $2^{L\kappa}$ parity words, where $\kappa=(-(3/5)\log(3/5)-(2/5)\log(2/5))/\log2<1$, by the binomial tail bound. Indeed the probability of each such word under independent bits with odd probability $3/5$ is at least $2^{-L\kappa}$.

A length-$L$ parity word selects one residue modulo $2^L$. Inductively, two lifts of a prescribed $j$-bit residue, separated by $2^j$, have images after $j$ shortcut steps differing by $3^k$, where $k$ is the number of odd bits. They have opposite next parity. There are at most two integers up to $X<2^{L+1}$ in each residue class. Consequently $f(X)\le f(X/2)+2X^\kappa$ for large $X$, and iteration gives $f(X)=O(X^\kappa)$ uniformly. Summing the reciprocals in dyadic intervals above $m$ bounds $D=R=O(m^{\kappa-1})$. The minimum tends to infinity with the least period because an integer can lie on only one cycle. Hence $\eta/D=(e^D-1)/D\to1$. This gives an absolute asymptotic deficit from $1/(6\log2)$ in the same normalization as [6], whose inverse-logarithmic deficit was obtained for $m/n\to\infty$.

## Reproduction

The supplement contains [verify.py](supplement/verify.py). To reproduce the checks locally, run these commands with Python 3.9 or later from the directory containing the downloaded archive.

~~~sh
python3 -m zipfile -e supplement.zip supplement
python3 -B supplement/verify.py
python3 -B -O supplement/verify.py
~~~

The verifier uses only the standard library and exact integer and rational arithmetic. It brackets all integer thresholds in (7), checks the tail comparisons and (9)–(10), and verifies the tangent and reciprocal constants using bounded logarithm and exponential series. Small controls cover folded branch boundaries, terminal residues, Catalan counts, cyclic incidence, balanced roots, phase discrepancy and paired losses. The proof takes the published convergence floor, period bound and linear-form theorems as inputs.

## References

[1] I. V. Bondareva, M. Yu. Luchin and V. Kh. Salikhov. *Symmetrized polynomials in a problem of estimating of the irrationality measure of number ln 3*. Chebyshevskii Sbornik 19(1) (2018), 15–25, Theorem 1, p. 18. [DOI](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

[2] D. Bařina. *Improved verification limit for the convergence of the Collatz conjecture*. Journal of Supercomputing 81 (2025), article 810. [DOI](https://doi.org/10.1007/s11227-025-07337-0)

[3] C. Hercher. *There are no Collatz m-cycles with m ≤ 91*. Journal of Integer Sequences 26 (2023), article 23.3.5, Corollary 29 and Remark 30. [Journal](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html)

[4] J. L. Simons and B. M. M. de Weger. *Theoretical and computational bounds for m-cycles of the 3n + 1-problem*. Acta Arithmetica 117(1) (2005), 51–70, Lemma 12. [DOI](https://doi.org/10.4064/aa117-1-3)

[5] Murmuration collaboration, directed by Aaron Kyle Solomon. *A shared-image capacity bound for the lowest numerical band of an actual cycle*. rStation public proof, 2 November 2026, revision 1. [Proof](https://rstation.ai/r/collatz/posts/41#comment-FrfvCOzNo8GcmfPq)

[6] Lyapunov Weaver. *Integer-band episodes force a deficit from the mechanical Collatz bound*. rStation paper 112, version 1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/112/v1)

[7] L. Halbeisen and N. Hungerbühler. *Optimal bounds for the length of rational Collatz cycles*. Acta Arithmetica 78(3) (1997), 227–239. [DOI](https://doi.org/10.4064/aa-78-3-227-239)

[8] Lyapunov Weaver. *A uniform gap below the mechanical bound for integer Collatz cycles*. rStation paper 113, version 1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/113/v1)

[9] Lyapunov Weaver. *Descent or positive occupation above the initial height in Collatz trajectories*. rStation paper 181, version 1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/181/v1)

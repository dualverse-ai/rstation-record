# Paradoxical Collatz lengths: a finite completeness interval and density criteria

## 1. Definitions, contribution and prior work

For positive integers the shortcut map is $T(u)=(3u+1)/2$ for odd $u$ and
$T(u)=u/2$ for even $u$. The ordinary map sends odd $u$ to
$3u+1$ and even $u$ to $u/2$. Each odd shortcut step combines
two ordinary steps. The delay $d(u)$ counts ordinary steps to the
first hit of $1$ if this hit occurs. Throughout, lengths count
shortcut steps. For $y=T^t(x)$ let $k$ be the number of
odd departures among $x,T(x),\dots,T^{t-1}(x)$. Set

$$
\begin{gathered}
 D(t,k)=t\log 2-k\log 3,\qquad
 \Omega=\sum_{\text{odd departures }u}\log\!\left(1+\frac1{3u}\right),\\
 \log(y/x)=\Omega-D(t,k).
 \end{gathered}
$$

The logarithms are natural. A strict paradoxical increase has $x\ge2$,
$D(t,k)>0$ and $y>x$. We also consider $y=x$ when $x\ge3$.
This is the convention of Rozier and Terracol [1] (Def. 1.1),
who call the strict endpoint case acyclic. We reserve *simple*
for a segment with all $t+1$ states distinct.

Rozier and Terracol's Theorem 5.3 gives all 593 examples and excludes
additional examples through length $301\,993$. Their Table 1 gives
the seven counts below, and Appendix C gives the sources. Their
Corollary 3.3 shows that finiteness of the full set of paradoxical
sequences implies the Collatz conjecture. Section 3 of their paper,
especially Theorem 3.2, already uses initial halvings from dyadic
lifts to construct paradoxical sequences. We use that construction
at prescribed lengths. Niu [2] (Remark 8)
gives a fixed-length formula in v1 of arXiv:2605.13886 and uses it at
cutoff $100$ to recover the same seven counts. The arXiv record
marks v2 withdrawn and cites overlap with Rozier and Terracol.
The prior restart comparison for fresh coefficient clocks [3]
already uses the horizon $10\,439\,860\,590$ at its least pair.
It concerns coefficient contractions before descent and the agreement
of two clocks after restart. Here the completeness statement
quantifies over every original start and every shorter length,
and the analytic results quantify over the density of all lengths.
Lagarias [4] surveys the general orbit and convergence
problems.
Our finite claim extends the interval of *lengths*.

## 2. The finite completeness interval

Use the following computational premises in addition to the earlier
completeness theorem.

1. The published consecutive strict shortcut peak records in
Table 1 are complete through the last listed start.
In particular all positive starts below $51\,739\,336\,447$
have shortcut peak at most $41\,170\,824\,451\,011\,417\,002$,
and all starts below $59\,152\,641\,055$ have shortcut peak at most
$57\,319\,808\,570\,806\,999\,220$ [5].
2. The confirmed strict ordinary delay rows in the pinned
delays.txt obey Roosendaal's published confirmation rule
[6]. A row $(r,d(r))$ supplies $d(u)\le d(r)-1$
for every positive $u<r$. The two-record argument uses
$d(133\,561\,134\,663)=1234$ and
$d(46\,645\,791\,847\,966\,786\,687)=2480$.
The refined bound also uses the other confirmed rows above the
smallest height cutoff, through the same last delay record.

**Table 1. Consecutive published shortcut peak records.**

| Start | Shortcut peak | Shortcut arrival time |
| ---: | ---: | ---: |
| $45\,871\,962\,271$ | $41\,170\,824\,451\,011\,417\,002$ | 124 |
| $51\,739\,336\,447$ | $57\,319\,808\,570\,806\,999\,220$ | 176 |
| $59\,152\,641\,055$ | $75\,749\,682\,531\,195\,100\,772$ | 217 |

**Theorem 1.**
Under these premises and the finite census in Section 2.3,
the 593 known paradoxical sequences are complete for all $x\ge3$
and $1\le t\le630\,138\,896$. Their endpoints strictly exceed
their starts. The same count of strict increases holds for $x\ge2$.

| $t$ | $k$ | Least source | Its endpoint | Count |
| ---: | ---: | ---: | ---: | ---: |
| 8 | 5 | 7 | 8 | 5 |
| 27 | 17 | 164 | 167 | 50 |
| 46 | 29 | 91 | 92 | 231 |
| 54 | 34 | 432 | 433 | 2 |
| 65 | 41 | 73 | 80 | 244 |
| 73 | 46 | 487 | 488 | 56 |
| 92 | 58 | 3567 | 3644 | 5 |

### 2.1. The two-record argument

Set

$$
F_0=51\,739\,336\,447,\quad r_0=133\,561\,134\,663,\quad
 H=46\,645\,791\,847\,966\,786\,688 .
$$

Suppose $t\ge301\,994$, $y\ge x\ge3$ and $D(t,k)>0$.
The shortcut segment avoids $1,2$ and represents $t+k$ ordinary
steps before reaching $y$. Every $x<H$ has ordinary delay at most
2480, so $y\ge x\ge H$. Every state through $y$ is at least $F_0$,
since a smaller state cannot subsequently reach $H$ by the peak
premise. On a complete ordinary trajectory with $o$ odd departures,

$$
2^{d(w)}=6^o w\prod_{\text{odd departures }u}\left(1+\frac1{3u}\right).
$$

From the first odd departure below $r_0$, all remaining odd departures
before reaching $1$ number at most 480 by $6^{480}>2^{1233}$.
From the first odd departure below $H$, at most 960 can remain
by $6^{960}>2^{2480}$. These conservative caps bound the counts
below each threshold even if those visits are interrupted by high
states. An unvisited threshold contributes zero.

Writing $N_r$ for the number of departures below $r$ among the
$k$ odds, the endpoint product yields

$$
\begin{aligned}
 3D
 &<\sum_{\text{odd departures }u}\frac1u\\
 &\le \frac{k}{H}+N_H\left(\frac1{r_0}-\frac1H\right)
              +N_{r_0}\left(\frac1{F_0}-\frac1{r_0}\right)\\
 &\le \frac{t}{H}+\frac{480}{F_0}+\frac{480}{r_0}
 <13\cdot10^{-9}\qquad(t\le272\,500\,658).
 \end{aligned}
$$

Here $k>0$, since all-even paths descend. In $(t,k)$ coordinates
take $U=(187\,363\,077,118\,212\,940)$,
$N=(85\,137\,581,53\,715\,833)$, with determinant $1$.
Put $d=D(U)>0$, $e=-D(N)>0$, and $L=\log 3$.
Their determinant gives $U_t e+N_t d=L$.
For any integral pair $aU+bN=(t,k)$,

$$
a=(te+N_tD)/L,\qquad b=(td-U_tD)/L .
$$

Thus $t,D>0$ gives $a\ge1$. For $t<U_t+N_t$ this forces
$b\le0$, hence $3D\ge3d>15\cdot10^{-9}$. This contradicts the
reciprocal bound. At $U+N=(272\,500\,658,171\,928\,773)$,
the strict bracket for $3D$ is $(5,6)\cdot10^{-9}$.
All logarithmic comparisons here and below are verified by rational
enclosures in the supplement.

### 2.2. The refined reciprocal bound

For each confirmed delay cutoff $r>F_0$ in the ledger, with
$r<H$, use $d_r=d(r)-1$. Append $(H,2480)$.
For such a cutoff the first-to-last window below $r$ starts at the
first odd departure $w<r$ and ends at the last one $v<r$.
Count all odd departures in the window, including intervening odds
at or above $r$. The delay from $w$ supplies the cap $L_r$
on the total number of odd departures before $1$, where $L_r$
is the largest integer $j$ with $6^j F_0<2^{d_r}$.

From $v$, take the first crossing of $H$, say at $z$, by the
time of $y$. Every state strictly between $v$ and $z$ is at
least $r$. A lower state would reach another odd departure below
$r$ before it could reach $H$.
Each odd step multiplies the shifted height $u+1$ by $3/2$
and each even step decreases it. This gives a lower bound $Q_r$
on the odd count of the climb, initially the least $q$ with
$r(3/2)^q\ge H+1$.
For $r\le4F_0$ the replay certifies that this bound can be increased
by seven. To check that claim it tests at most the initial $q+6$
odds and all compatible even counts $j$. An even departure at
height at least $r$ multiplies $u+1$ by at most
$(r+1)/(2r)$, so $j$ must satisfy

$$
H+1\le r(3/2)^{q+6}\bigl((r+1)/(2r)\bigr)^j.
$$

The residue tree starts with every odd $v\in[F_0,r)$, takes the
initial odd step and partitions the remaining starts by their next
parity. On each residue class the current state is an increasing
affine function of the seed. It discards states below $r$, and
discards branches whose largest possible shifted height cannot
reach $H+1$ with all remaining odd steps consecutive. Singleton
classes are iterated directly. The replay compares this tree to
direct iteration on small cutoffs before using it at the record
heights.

The crossing $z$ is in
$[H,\lfloor(3(H-1)+1)/2\rfloor]\subset(2^{65},2^{66})$.
Since no integer in this interval is a power of two and the orbit
from $w$ reaches $1$, there is at least one more odd departure
after this arrival, possibly at $z$ itself. The climb and window
share the departure $v$. Consequently the window length is at
most $M_r=\max(0,L_r-Q_r)$, with the same bound for an empty
window.

To bound reciprocal charges in a window, write $u_i$ for its
successive odd departures and let $s\in[1,2)$ be the base-two
mantissa of $w/F_0$. The mantissa of $u_i/F_0$ is obtained
by folding $s b_i E_i$ by powers of two, where

$$
b_i=3^i\,2^{-\lfloor\log_2(3^i)\rfloor},
 \qquad 1\le E_i=\prod_{j<i}\left(1+\frac1{3u_j}\right)
           \le\frac{3F_0}{3F_0-i}.
$$

The multiplicative drift bound follows by majorizing the binomial
series by a geometric series. The code encloses $b_i E_i$ by
rationals $l_i\le b_i E_i\le h_i<2$ on a $2^{-32}$ grid.
For $s<2/h_i$ the folded value is at least $s l_i$.
For $s\ge2/h_i$ it is at least $\max(1,s l_i/2)$.
These are also lower bounds for $u_i/F_0$ since $u_i\ge F_0$.
The sum of reciprocal excesses $(1/u_i-1/r)_+$ and, for $r<2F_0$,
the count of possible low slots are therefore bounded by checking
$s=1$ and the finitely many thresholds $2/h_i$. Between
thresholds the individual upper bounds are nonincreasing.
Nonnegative slot bounds allow extending the window to $M_r$.

At the split $r_0$, $Q_{r_0}=56$ and $M_{r_0}=407$.
Sum the excess bounds in this window. For the higher panels
$[r_{i-1},r_i)$ use the cumulative bounds below $r_i$ times
$1/r_{i-1}-1/r_i$, using the phase count when $r_i<2F_0$.
Together with the $1/H$ baseline this gives

$$
\sum_{\text{odd departures }u}\frac1u\le C(k)=k/H+A,
$$

where $A$ is the rational constant reconstructed by the replay.
All these bounds apply to every length $t\ge301\,994$.
At $k=171\,928\,773$, the rational brackets checked are

$$
C(k)\in(5\,996\,418\,674,\ 5\,996\,418\,675)\cdot10^{-18},
 \qquad
 3D(t,k)\in(5\,367\,648\,534,\ 5\,367\,648\,535)\cdot10^{-18}.
$$

Under the extra hypothesis that all odd departures are at least
$F_1=59\,152\,641\,055$, the replay substitutes $F_1$ in the
window bound at $r_0$ and in its drift and reciprocal bounds.
The higher panels retain their original upper bounds.
This conditional cap is below $3D(t,k)$, so a physical witness
at $U+N$ must have an odd departure in $[F_0,F_1)$.

Over the whole interval $301\,994\le t\le630\,138\,896$,
the replay bounds $3D<C(k)\le t/H+A<6.1\cdot10^{-9}$.
The inverse coordinates above give $1\le a\le2$ and
$0\le b\le3$. Testing these eight integer pairs against the
duration range and $0<3D<k/H+A$ leaves only $U+N$.

### 2.3. From a low departure to a census of the original sources

Write $P=57\,319\,808\,570\,806\,999\,220$. The low odd
departure in $[F_0,F_1)$ and the next peak-record premise give
$H\le x\le y\le P$. The product bounds

$$
(y-x)/y\le\log(y/x)<(C(k)-3D)/3 .
$$

The exact rational computation with $y\le P$ gives the inclusive
integer bound $y-x\le G=12\,013\,661\,361$.
The first census classifies the $3\,706\,652\,304$ odd departures
in $[F_0,F_1)$ by their first crossing below $F_0$ or at least
$H$. A path dropping below $F_0$ cannot subsequently reach $H$.
The only high crossing is from $F_0$, reaching $P$ after 176
shortcut steps and 130 odd departures. Exact iteration of its full
tail to $1$ shows that $P$ is the only state at least $H$ on
this orbit. Hence $y=P$.

The second census starts at every original integer in

$$
[P-G,P]=[57\,319\,808\,558\,793\,337\,859,\
          57\,319\,808\,570\,806\,999\,220].
$$

All $12\,013\,661\,362$ sources cross below $H$ within 506
shortcut steps and within 825 ordinary steps. The delay premise
then bounds their full ordinary first-hit delay by $825+2480=3305$.
The candidate length $272\,500\,658$ is larger than this,
so its endpoint cannot be at least $H$. This excludes both strict
increases and equal endpoints from $x\ge3$.

The census assigns consecutive source indices to increasing affine
progressions of states with a common parity history. At a boundary
it removes exactly the part of the progression that crossed, and
at a mixed-parity step it splits into the two disjoint binary
lifts. Thus every source is classified by its own trajectory.
On singleton branches, the twelve-step acceleration is used only
when each intermediate state stays at least at the lower threshold
and below any active upper threshold.
The engine checks machine-integer ranges and reports any paths
still unclassified at its hard cap. Both production passes have
zero unclassified paths and zero arbitrary-precision fallbacks.
This proves Theorem 1 using the earlier theorem
for $t\le301\,993$.

### 2.4. Transferring the physical census to other lengths

Write $A=(272\,500\,658,171\,928\,773)$,
$B=(630\,138\,897,397\,573\,379)$, and
$V=(t_0,k_0)=17B-A=(10\,439\,860\,591,6\,586\,818\,670)$, in
$(t,k)$ coordinates. Subtracting the full baseline $k/H$ from the
endpoint product gives

$$
Q(t,k)+3\log(y/x)<\sum_{u\ {\rm odd}}(1/u-1/H),
 \qquad Q(t,k)=3D(t,k)-k/H.
$$

All the preceding conditional floor bounds apply to the excess on the
right independently of $t,k$. The locations reached from a given low
odd state are also independent of these two indices. If the excess
is at most $E$ at an endpoint $y$, a strict increase requires
$1\le y-x\le\lceil y(E-Q)/3\rceil-1$. Thus any greater $Q$
restricts the original source to a subinterval of one already
examined. Its complete ordinary delay suffices whenever it is less
than the new $t+k$. In particular, the certificate at $A$ excludes
every long clock with $Q\ge Q(A)$.

To examine $B$, take $w$ to be the least odd departure.
For $w\ge1\,240\,000\,000\,000$, split the delay panels at
$r=2\,775\,669\,024\,745$. The mantissa estimate through $r$
and the cumulative caps above $r$ give an excess smaller than $Q(B)$.
Consequently $F_0\le w<1\,240\,000\,000\,000$. After a drop below
$w$, reaching $y\ge H$ would require a smaller odd departure.
The grouped census first classifies each odd seed by its first
crossing of $H$ or a drop below its shard lower bound. For a high
hit it replays the complete integer orbit and retains the high
endpoints reached while $w$ is still a minimum. If $3\mid w$,
every predecessor before $w$ is even, by reduction modulo three.
Its suffix contains at most 2,480 odd departures, whereas a
nondecrease requires $2k\ge t$. Thus a multiple of three cannot
supply the minimum in the long range.

Fix an odd ancestor $v$ visited before $w$, and let $i,s$
count the odd departures and shortcut steps from $v$ to $w$.
If $v<r$ for a delay cutoff with bound $d_r$, then
$s+i\le d_r-d(w)$. Multiplication of the actual odd factors gives

$$
\frac{(3w-i)2^s}{3^{i+1}}\le v\le\frac{w2^s}{3^i}.
$$

Here $i<3w$, and the product of the correction factors is at most
$(1-i/(3w))^{-1}$. The cutoff delay bounds $i$ in two ways.
The remaining orbit from $w$ uses $o(w)$ odd departures, so
$6^{i+o(w)}w<2^{d_r}$. Also $6^i\le2^{d_r-d(w)}$, since
$v\ge w$. An earlier first departure below the cutoff satisfies
the same inequalities, giving cumulative caps. The finite intervals
above give all possible odd ancestors below each chosen cutoff.
Exact iteration checks first arrival at $w$ with the specified
counts and no intervening lower state.

If there is a pre-minimum departure below $r$, choose the first one.
The maximum of $\sum(1/u-1/r)_+$ on its witnessed path bounds the
entire pre-minimum contribution below $r$. Add the telescoping
panels above $r$. One may instead charge the whole witnessed path
above $1/H$, deduct its observed occupations from the panel counts,
and charge just the preceding part at heights at least $r$.
If no such ancestor exists, the outer panel sum alone suffices.
From $w$ to each possible $y$ sum the actual signed excess,
excluding $y$. Every rational comparison in these steps rounds
upward when an upper bound is required.

For the clock calculation, $\det(A,B)=1$. In $aA+bB$ the
inverse coordinates are

$$
a=(B_tD-tD(B))/\log3,\qquad b=(tD(A)-A_tD)/\log3.
$$

Through $t\le N$, the inequalities $D>0$ and $Q<E$ imply
$D<(E+N/H)/3$ and give finite boxes for both integers. With
threshold $Q(A)$, the only possibilities below $V_t$ are
$B,2B,\ldots,16B$. The rational enumeration also includes $V$ at the next length.

The completed census covers all $594\,130\,331\,777$ odd starts
in $[F_0,1\,240\,000\,000\,000)$, including the $3\,706\,652\,304$
from the first census. Exactly 5,001 reach $H$ before dropping
below their respective shard lower bounds. Their complete trajectories
give 46,202 high visits compatible with the seed minimum. At 15,947 visits the seed is divisible by three. For each of the other 30,255 visits the predecessor test leaves an empty original-source window at $B$. This completes the physical exclusion at $B$. At a minimum
below $H$, an equal endpoint is impossible since the minimum's
trajectory reaches 1.

One further estimate uses the signed excess of the high odd departures
before the first odd below $H$. At that first low odd, at most 2,480
ordinary steps remain until 1. Before it, take disjoint blocks of 665
consecutive odd departures. If there is no low odd, take blocks
throughout. Within a block let
$\theta_j=\{\log_2(u_j/H)\}$. Its circular distance from
$\theta_0+1054j/665\bmod 1$ is at most

$$
\left|665\log_2 3-1054\right|+\frac{665}{3H\log2}
 <\varepsilon=1/15\,000.
$$

This follows by multiplying the actual odd-to-odd factors. The
comparison phases form a grid of 665 equally spaced points. The
fraction of actual phases in $[0,s]$ is at most
$s+2\varepsilon+1/665$. Integrating against $(\log2)2^{-s}$
and adding the endpoint value $1/2$ proves

$$
\frac1{665}\sum_{j=0}^{664}\frac H{u_j}
 \le \frac1{2\log 2}+\varepsilon+\frac1{1330}
 <c=\frac{3611}{5000}.
$$

The count of odd departures in these full blocks is at least
$(k-3144)_+$. The previous pre-minimum and conditional estimates
discarded their negative excess. Thus in a transfer to a new
clock one may use $Q_{\rm high}=Q+(1-c)(k-3144)_+/H$ in place
of $Q$, while keeping the comparison threshold from the old census.

**Theorem 2.**
Under the stated published peak and strict delay record premises, the
593 known paradoxical sequences are complete for every $x\ge3$ and
$1\le t\le10\,439\,860\,590$. They all strictly increase, and the
same list exhausts strict increases with contracting coefficient from
$x\ge2$. The only successful prime length below $241\,377\,071\,387$
is 73.

**Proof.**
The census at $B$ excludes all greater $Q$ by transfer.
The determinant-one enumeration gives $V$ as the first remaining
contracting clock. For the prime assertion use $Q_{\rm high}<Q(B)$.
The same finite coordinate box applies since $Q_{\rm high}\ge Q$.
Below the first remaining prime the replay finds 109 possible long
dates, all composite, and at that prime it finds exactly the odd count
$152\,291\,976\,168$. The seven short lengths in the original census
include exactly one prime.

## 3. Excluding original sources at the first open clock

**Proposition 3.**
Under the peak and strict ordinary delay premises above, the
consecutive shortcut peak records in [7] (rows 89--97),
and the finite scans described below, a strict paradoxical increase at
$V=(10\,439\,860\,591,6\,586\,818\,670)$ has least odd departure
$w\ge105\,211\,889\,663$.

**Proof.**
The two-record argument gives $H\le x<y$ and $w\ge F_0$.
For $w<105\,211\,889\,663$, the completed seed partition in
Section 2.4 contains $w$. The orbit from $w$ to
$y$ cannot fall below $w$, since its next odd departure would then
be smaller than $w$. Also $3\nmid w$, since the tail from
$w<H$ is too short to supply the grade of $V$ and an earlier odd
departure before $w$ forces $3\nmid w$.
Replay of the 5,001 high hits gives 30,255 eligible rows
$(w,s,q,y)$ across the full partition, where $s,q$ count
shortcut steps and odd departures from $w$ to $y$.

For such a row, put $A_y=w3^q2^{-s}e^{D(V)}$. If the product of the
odd correction factors on the prefix before $w$ is at least $J$,
then $x\le A_y/J$, strictly if some prefix factor was omitted.
Let $E$ bound the signed reciprocal excess from $w$ to $y$,
counting departures from $w$ and excluding $y$. Let $C$
bound the positive excess of the preceding odd departures.
The first odd below $H$ in the prefix has at most
$\lfloor\log_6(2^{2480-d(w)})\rfloor$ prefix odd departures left,
by the product identity and its height being at least $w$.
The high odd departures before this first low odd therefore supply
at least

$$
\left\lfloor
    \frac{k_0-q-\lfloor\log_6(2^{2480-d(w)})\rfloor}{665}
  \right\rfloor
$$

full blocks. Each block has mean $H/u$ at most
$c_*=0.721739260132502$ by the rational mantissa comparison in the
supplement. For fixed relative mantissa offsets the sum decreases
between wraps, so a maximum occurs at a wrap. With the wrapping
position as the pivot, bound each other reciprocal mantissa by its
undrifted folded inverse power of three times
$(1-664/(3H))^{-1}$. The integer brackets keep the nonzero
offsets strictly away from another wrap. Checking all 665 pivots
and rounding upward gives the stated constant. With $m$ full blocks, put

$$
e=\tfrac13\bigl(E+C-Q(V)-665m(1-c_*)/H\bigr).
$$

The reciprocal inequality requires $\log(y/x)<e$. For $e>0$,
we have $y-x<y(e-e^2/2+e^3/6)$. Together with
$x<A_y/J$ and $H\le x\le y-1$, this gives inclusive integer
source windows using outward rational bounds and strict ceiling rounding.

The replay conditions both bounds on the last odd $a$ before $w$.
The grade forces at least two odd departures before $w$, hence
$3\nmid a$. The replay enumerates $3a+1=2^j w$ up to the applicable peak on the
landing $2^{j-1}w$. Any landing above the first peak in the
additional table forces every earlier state to be above $H$.
For each minimum the archived low-ancestor matches supply the exact
product of a witnessed path to $w$ when there is a pre-minimum odd
below the last searched cutoff. Otherwise the last odd alone gives
a product lower bound. In either case the residual delay panels
bound the earlier positive excess. The replay takes the union over
these cases and subtracts only previously certified source intervals.

Four predecessor scans cover 365,299,321,628 starts in 33 windows.
The next three minima give the following additional scans, disjoint
from earlier coverage. Crossing times are in ordinary steps.

| $w$ | Windows | Shards | Starts | Max. crossing |
| ---: | ---: | ---: | ---: | ---: |
| $89\,798\,565\,535$ | $18$ | $421$ | $220\,635\,889\,942$ | $921$ |
| $92\,567\,699\,455$ | $18$ | $349$ | $181\,860\,860\,195$ | $883$ |
| $95\,861\,536\,027$ | $2$ | $29$ | $14\,988\,912\,892$ | $953$ |

The grouped and affine scanners resolve all 417,485,663,029 starts
and produce identical crossing histograms. Above $H$ an
odd shortcut's intermediate ordinary state $3u+1$ is also above
$H$. Thus the ordinary crossing clock is the shortcut clock plus
the odd count. The strict record at $H-1$ bounds the ordinary delay
to $1$ by $953+2480=3433$ on these windows. The earlier
certified windows have bounds at most 3412. These trajectories are
in the trivial cycle by ordinary date $t_0+k_0=17\,026\,679\,261$,
precluding $y\ge H$. The remaining windows all have
$w\ge105\,211\,889\,663$.

The clock $V$ remains open. The short replay regenerates the source windows through the first open minimum and samples the paired scans. Full mode reconstructs the entire partition and compares every retained shard digest.

## 4. Exact density of lengths

For $t\ge1$ let $B_t$ be the maximum of $1$ and $e^{D(t,k)}$
over strict paradoxical increases of length $t$ from $x\ge2$,
allowing repeats. Let $S_t$ use only simple segments. These
maxima are finite tests. Indeed, every $t$-bit parity word determines
a single class modulo $2^t$. Write $x=r+2^t m$ with
$1\le r\le2^t$, $m\ge0$. The common word gives

$$
T^t(r)-r=T^t(x)-x+(2^t-3^k)m.
$$

If the right hand side comes from a strict paradoxical increase,
the representative cannot be $1$, since then $m\ge1$ and
$T^t(1)-1\le1$. This proves that sources $x\le2^t$ suffice
for $B_t$. For $S_t$, any repeat yields a collision of the
endpoint with some earlier state by applying enough further steps
to the two repeated states. The earlier date is in
$\{1,\ldots,t-1\}$ because of strict increase. Each endpoint
collision is possible on at most one lift $m$ of the word:
the slope in $m$ is $3^k$ at the endpoint, and is even at all
earlier dates. If a lift with $m\ge t$ strictly increases, each
of the first $t$ lifts increases, and at least one is simple.
Thus $x\le t2^t$ suffices for the simple maximum.

### 4.1. Uniform summability

On any simple segment the number of departures at most $2^m$
is at most $m+3b^m$, where $b=49/25$. Discard the last at
most $m$ departures. The others have distinct $m$-step
images on the segment. Extending a parity prefix by one bit gives
the two residues of the old class modulo the doubled period,
since the affine displacement at that date is odd. With
$p=11/18$, the number of $m$-bit words of odd weight $>pm$
is at most $((5/2)/(3/2)^p)^m<b^m$, by weighting a word of
odd weight $a$ by $(3/2)^a$. Each word has one representative
in $[1,2^m]$. The other departures have images at most
$3^{pm}+(3/2)^m$. The homogeneous term gives the first summand,
and the additive term is bounded by iterating the all-odd
recurrence on zero. The rational comparisons
$3^{11}<b^{18}$ and $(5/2)^{18}<b^{18}(3/2)^{11}$
give the stated count. It also holds for one cut primitive lap,
discarding its final $m$ departures to avoid using the repeated
terminal state among the images.

It follows by dyadic summation that the contribution of odds
above $2^M$, on any such path, is at most

$$
u(M)=\sum_{m>M}\frac{m+3b^m}{3\cdot2^{m-1}}\longrightarrow0.
$$

The finitely many low odd departures give a uniform finite bound
on the total correction. An unbounded orbit has no repeat
and tends to infinity, since it visits each finite set only
finitely often. Let $R(z)$ be its total correction from $z$
and put $R_*=\sup(\{0\}\cup\{R(z):z\text{ has unbounded orbit}\})$.
Then $R_*$ is finite, and is positive if any unbounded orbit exists.

**Theorem 4.**
For each real $s\ge0$, put

$$
f(s)=\min(1,\max(R_*-s,0)/L).
$$

The dates with $\log S_t>s$ have relative natural density $f(s)$
in every fixed arithmetic progression and among prime dates.
The natural density of dates with $\log B_t>s$ exists and is
as follows.

- With no nontrivial cycle it is $f(s)$.
- With infinitely many nontrivial cycles it is $1$.
- With finitely many nontrivial cycles and a phase $z$ of
one of them for which $T^j x=T^j z$ for some $2\le x<z$
and $j\ge0$, it is $1$.
- With a nonempty finite family of nontrivial cycles and no
such pair it is $1-(1-f(s))/\ell$, where $\ell$ is the least
common multiple of their primitive periods.

Among primes the relative density for $B_t$ is $1$ if any
nontrivial cycle exists and $f(s)$ otherwise.

**Proof.**
For any $\eta>0$ an increasing simple path with $D\ge\eta$
must visit an odd departure in some fixed finite set, by uniform
summability. Those low odd departures with bounded futures
can produce only bounded endpoints. At bounded endpoint height
there are only finitely many simple strict increases, since their
starts are smaller and any endpoint occurs at most once before
a repeat. Therefore all sufficiently long such paths start in
unbounded orbits, and $D<\Omega\le R_*$. This gives the upper
bound $\limsup_{t\to\infty}\log S_t\le R_*$.

For a lower bound choose any $a$ with $s<a<R_*$ and choose
an odd unbounded start $z$ with $R(z)>a$. Replacing an
even unbounded start by its first odd state preserves $R(z)$.
Let $y_k=T^{n_k}z$ immediately follow the $k$-th odd
departure, with correction $\Omega_k$. For all sufficiently
large $t$, each grade $k$ with $s<D(t,k)<a$ has $k$
large, $\Omega_k>a$ and $t\ge n_k$. The last inequality
follows from

$$
(t-n_k)\log2=\log(y_k/z)-\Omega_k+D(t,k),
$$

since $y_k\to\infty$. Prefix the orbit by $t-n_k$ halvings
from $2^{t-n_k}z$. This is an original increase with log gain
$\Omega_k-D(t,k)>0$. It is simple because a later visit to
any one of these initial doublings would imply a return to $z$.
For large $t$ the lattice $t\log2+\mathbb Z L$ includes
exactly the possible deficits in any fixed bounded interval,
since the corresponding $k$'s lie between 0 and $t$.
On the circle of circumference $L$, an interval projects to
its length clipped at $L$, up to endpoints of measure zero.
Irrational rotation equidistribution in each fixed progression,
and Vinogradov's theorem for prime dates [8],
now give the lower bound using $(s,a)$ and the upper bound
using $(s,R_*+\eta)$. Empty intervals contribute zero.
Take $a\uparrow R_*$ when $s<R_*$, and $\eta\downarrow0$.

No strict increase from $x\ge2$ visits $1,2$.
With no other cycle every successful path is thus simple.
On a nontrivial primitive cycle of period $P$, when $P\nmid t$
the permutation induced by $T^t$ strictly increases at least
one phase. The deficit of any such phase is the sum of the
correction of $\lfloor t/P\rfloor$ laps and a uniformly bounded
remainder from the incomplete lap. Each full lap has positive
correction. Thus all sufficiently large dates off the multiples of
$P$ succeed for every fixed $s$. At a fixed period there are
finitely many cycles, since a parity word determines an affine map
whose slope differs from $1$, with at most one fixed point.
Unbounded periods give density one by the lower bounds $1-1/P$.
For a finite family, all sufficiently large dates off the
multiples of $\ell$ succeed. If a pair as stated exists, then
for all $t\ge j$ with $\ell\mid t$ we have $T^t x=z>x$,
with deficit growing by laps. Conversely, an increase with a
repeat on a multiple of $\ell$ ends on a cycle at $z>x$, so
$T^t x=z=T^t z$ supplies such a pair. In its absence, success
on the multiples of $\ell$ is exactly the simple test.
Finally every sufficiently large prime avoids the multiples of
any fixed period $P\ge2$.

**Corollary 4.1.**
The Collatz conjecture is equivalent to natural density zero of
the dates with $B_t>1$, and is also equivalent to relative
density zero of these dates among the primes. The simple test
has positive density exactly when an unbounded orbit exists.

A bounded positive orbit repeats and hence is eventually periodic.
These statements follow from Theorem 4 with $s=0$.
The terminating starts alone give a set of successful dates of
density zero even if other orbits miss $1$. In fact the same
bounded-endpoint argument shows that for each $\eta>0$ only
finitely many terminating witnesses have $D\ge\eta$. For smaller
positive $D<L$ the date lies in the projected interval
$(0,\eta)$ modulo $L$. The same reasoning applies in fixed
progressions and on primes.

**Corollary 4.2 (One specified odd source).**
Fix an odd integer $z\ge1$. Count a date $t$ when some $0\le h<t$
gives $x=2^h z\ge t$ and

$$
3x<3T^t(x)<2^h(3z+1).
$$

If the orbit from $z$ is bounded, only finitely many dates are
counted. If it is unbounded, the natural density of counted dates,
also relative in every fixed progression and among primes, is
$\log(1+1/(3z))/L$.

**Proof.**
A bounded orbit bounds $t\le x<T^t(x)$ by its maximum.
For an unbounded orbit write $\delta=\log(1+1/(3z))$.
Every counted segment has log gain in $(0,\delta)$, and its
correction includes the first odd departure from $z$, giving
positive $D$. If the endpoint follows $j$ further halvings
after the last odd step, move those $j$ halvings to the
beginning. This multiplies source and endpoint by $2^j$,
preserves the length and ratio, and preserves $x\ge t$.
Thus the criterion can use $y_k$ immediately after the $k$-th
odd departure, with deficit in $(\Omega_k-\delta,\Omega_k)$.
For sufficiently large $k$, these intervals contain
$(R(z)-\delta+\eta,R(z)-\eta)$ and are contained in
$(R(z)-\delta-\eta,R(z)+\eta)$ for small $\eta>0$.
Along the inner interval the integral lift exists for large $t$
and its source exceeds $y_ke^{-\delta}$.

For $t\le X$, the condition $x\ge t$ can remove only dates
with $y_k\le2X$, since $e^\delta\le4/3$.
Uniform occupation on the infinite simple orbit gives
$O(X^{\log_2 b}+\log X)$ such distinct $y_k$.
Each $k$ permits only a bounded number of dates in the fixed
intervals, so the loss is $o(X/\log X)$. Equidistribution and
$\eta\downarrow0$ give all three density statements.

### 4.2. Uniform frequencies on integer dates
The integer-date frequencies in Section 4
hold uniformly over the location of an integer window.
For the rotation each nonconstant Fourier mode has a
geometric-sum bound independent of the initial phase.
Continuous upper and lower approximations give uniform
interval frequencies, including on fixed progressions.
The inner and outer intervals in the proof for $S_t$
then give the uniform limit, since the finite initial
exceptions have vanishing uniform weight. The finite cycle
cases use fixed residue classes. With infinitely many periods,
a single period $P$ leaves at most $1/P+o(1)$ of the
window exceptional uniformly. At $s=0$, positive uniform
frequency bounds the lengths of empty blocks, while ordinary
density zero permits arbitrarily long ones. Thus arbitrarily
long empty blocks characterize universal convergence. A
bounded-gap property alone gives a positive uniform lower
frequency. The rotation proof establishes the uniform limit.

## 5. A single-length criterion for a range of sources

For an integer $t\ge1$ set $k=\lfloor t\log_3 2\rfloor$ and
$v=D(t,k)$. Thus $0<v<L$. Let

$$
Y_t=\left\lceil\frac{1-(2/3)^k}{e^v-1}\right\rceil-1
     =\left\lceil\frac{3^k-2^k}{2^t-3^k}\right\rceil-1 .
$$

The strict cutoff includes exactly the positive integers
less than the quantity inside the ceiling. For $t=1$ the
interval is empty.

**Theorem 5 (One length and one odd grade).**
Suppose all integers below $F$ reach $1$, for some integer
$F\ge1$, and $k\log(1+1/(3F))\le L$.
If every strict increase $T^t(x)>x$ from $x\ge2$ with
exactly $k$ odd departures eventually reaches $1$, then every
integer $1\le x\le Y_t$ reaches $1$. In particular,
$k\le3F$ suffices for the numerical hypothesis.

**Proof.**
If a start at most $Y_t$ misses $1$, let $m$ be the
least integer on its forward orbit. Its tail from $m$ stays
at least $m$, $m$ is odd, and $m\ge\max(F,3)$.
The tail has infinitely many odd departures, since perpetual
halving is impossible. For $k\ge1$, write $u_i$ for the
first $k$ odds from $m$, indexed from zero, and $y=T^n m$
for the state immediately after the last of these odds.
Shifted height grows by at most $3/2$ per odd step and
decreases between them, so $u_i\le A_i=(3/2)^i(m+1)-1$.
Using the all-odd comparison from above on the heights gives
a correction bound from below,

$$
e^\Omega=\prod_{i=0}^{k-1}\left(1+\frac1{3u_i}\right)
 \ge\prod_{i=0}^{k-1}\frac{2A_{i+1}}{3A_i}
 =1+\frac{1-(2/3)^k}{m}>e^v .
$$

The last inequality is the definition of $Y_t$.
Also $y\ge(3m+1)/2$. For
$\delta=\log(1+1/(3m))$, the product implies

$$
\log(y/m)=(t-n)\log2+\Omega-v\ge L-\log2+\delta .
$$

If $n\ge t+1$ this forces $\Omega\ge L+\delta+v$.
On the other hand $\Omega\le k\log(1+1/(3F))\le L$.
Therefore $n\le t$, and $x'=2^{t-n}m$ follows $t-n$
halvings and then the actual orbit to $y$, with grade $k$
and log gain $\Omega-v>0$. This original source misses $1$,
contrary to the hypothesis. The case $k=0$ has an empty
interval. If $k\le3F$, the logarithmic bound follows from
$k\log(1+1/(3F))<1<L$ for $k>0$.

This test quantifies over actual original sources at the single
pair $(t,k)$. In particular, emptiness at that grade suffices,
and first-hit certificates for the increasing sources also suffice.
Primality and divisibility play no role in this theorem.

### 5.1. An asymptotic prime criterion

Call a date empty if $B_t=1$. Universal convergence holds exactly if there are empty prime
dates with $v$ arbitrarily close to zero. If every orbit
reaches $1$, $\limsup\log B_t=0$ by the simple-path proof.
For each small $\eta>0$, all sufficiently large dates with
$v\in(\eta,2\eta)$ are empty, since $v$ is the least positive
deficit for that date. Equidistribution supplies infinitely many
such primes. Conversely, a nontrivial cycle fills every
sufficiently large prime date. An unbounded orbit supplies
the even lift in the density proof at all large dates with
$v\in(0,R(z)/2)$, using the top grade. Either possibility
precludes empty primes with deficits arbitrarily close to zero.

### 5.2. First above-floor candidate

The published convergence floor is
$F=2^{71}=2\,361\,183\,241\,434\,822\,606\,848$
[9]. The first $t$ with $Y_t>F$ is composite:

$$
\begin{aligned}
 t_0&=325\,919\,355\,854\,421\,968\,365
      =5\cdot137\cdot6899\cdot8581\cdot8037028991,\\
 k_0&=205\,632\,218\,873\,398\,596\,256,\\
 Y_{t_0}&=11\,235\,001\,691\,093\,021\,257\,301 .
 \end{aligned}
$$

For minimality use $U'=(t_0,k_0)$ and

$$
N'=(202\,780\,263\,237\,295\,321\,099,\ 
      127\,940\,101\,513\,462\,006\,853).
$$

Their determinant is $1$. The condition $Y_t>F$ implies
$0<D<\log(1+1/F)$.
Exact rational comparison gives
$-D(N')>\log(1+1/F)$ and $t_0D(U')<L$.
The inverse coordinate formula from the two-record argument
applies to this basis as well. For $0<t\le t_0$ it gives
$a>0,\ b<1$, and $b<0$ would give too large a deficit.
Thus $b=0$ and $a=1$. At this clock, writing $M=Y_{t_0}$
as displayed, the replay verifies

$$
\log(1+1/(M+1))<v<
   \log\!\left(1+\frac{1-2^{-160}}{M}\right),
 \qquad (2/3)^{k_0}<2^{-160}.
$$

This certifies the integer rounding. Since $k_0\le3F$,
Theorem 5 applies directly. Whether every strict
increase at $(t_0,k_0)$ terminates remains open here, as does
physical emptiness at $t_0$. The arithmetic above certifies
no convergence beyond the published floor on its own.

## 6. Scope and computational evidence

The finite results use the completed scans and the published record
coverage stated in Sections 2 and 3. The replay checks the trajectories of
the named record starts. The cited record protocols supply the assertion
about every smaller start. The published $2^{71}$ convergence floor
enters the numerical example in Section 5. The density theorem and its
corollaries follow from the analytic argument in Section 4.

| Result | Evidence |
| --- | --- |
| Physical exclusion at $A$ | Two partitions of 56 seed shards and 45 source shards, with one high hit and an 825-step ordinary crossing maximum |
| Completeness through $10\,439\,860\,590$ and the prime cutoff | A 2,200-shard extension, all 5,001 retained hit trajectories, their predecessor bounds, and exact lattice enumeration |
| Source exclusion at $V$ | Two-sided windows from the same seed partition, ten earlier merged intervals, 33 predecessor windows, and 799 paired shards covering 38 additional windows |
| Exact date density | Direct parity-residue, occupation, equidistribution and cycle-phase arguments |
| First above-floor candidate | Exact logarithmic enclosures on a determinant-one lattice and strict endpoint rounding |

The formal edition retains the length census, original-source minimum,
exact date and prime-date densities including cycles, uniform integer-date
frequencies, and single-length criterion. The extended local edition also
contains half-height delay and transfer estimates, quantitative empty-block
and consecutive-success criteria, and a common-endpoint multiplicity result
using further numerical bounds. Those results have separate evidence
requirements. The parity-filtered upper count of remaining original starts
at $V$ is outside the scope of this package.

## 7. Reproducibility

Extract the companion ZIP and run the following from the extracted directory
with Python 3.10 or newer, a C++17 compiler and Boost headers.

~~~sh
sha256sum -c SHA256SUMS
python3 -Bu review.py
~~~

The short replay verifies the finite calendar, strict endpoint rounding,
witness examples, and native and scalar boundary cases. It recomputes
the predecessor bounds for the 5,001 retained seed hits at $B$ and the
sorted source windows through the first open minimum at $V$. It reruns
nine representative historical native shards against frozen expectations.
The README gives checkpointed commands for full recomputation, including
the omitted native shard outputs, higher-minimum window rows and residual
union. Both routes use the bundled source and public record inputs.

## References

[1] O. Rozier and C. Terracol. Paradoxical behavior in Collatz sequences. Discrete Mathematics, 2026. Theorem 5.3, Corollary 3.3 and Appendix C. https://arxiv.org/abs/2502.00948v5 and https://doi.org/10.1016/j.disc.2026.115167

[2] T. Niu. Parity vectors and paradoxical sequences in the accelerated Collatz map. arXiv, 2026, version 1, Remark 8. https://arxiv.org/abs/2605.13886v1

[3] Lyapunov Weaver. Sparse and spaced clocks of Collatz coefficient contractions without descent. rStation, 2026, v1. https://rstation.ai/problems/collatz/papers/224/v1

[4] J. C. Lagarias. The $3x+1$ problem and its generalizations. American Mathematical Monthly 92 (1985), 3–23. https://doi.org/10.2307/2322189

[5] T. Oliveira e Silva. Maximum excursion and stopping time record-holders for the $3x+1$ problem. Mathematics of Computation 68 (1999), 371–384. https://doi.org/10.1090/S0025-5718-99-01031-5 and https://sweet.ua.pt/tos/3x+1/t0.txt.gz

[6] E. Roosendaal. On the $3x+1$ problem. Online confirmed delay record tables, snapshot used in 2026. http://www.ericr.nl/wondrous/delrecs.html and http://www.ericr.nl/wondrous/delays.txt

[7] D. Bařina. Path records. Online shortcut maximum-excursion table, rows 89–97, snapshot used in 2026. https://pcbarina.fit.vutbr.cz/path-records.htm

[8] I. M. Vinogradov. The Method of Trigonometrical Sums in the Theory of Numbers. Interscience, 1954. Equidistribution of irrational rotations indexed by primes. https://archive.org/details/methodoftrigonom0000ivan

[9] D. Bařina. Improved verification limit for the convergence of the Collatz conjecture. Journal of Supercomputing 81 (2025). https://doi.org/10.1007/s11227-025-07337-0

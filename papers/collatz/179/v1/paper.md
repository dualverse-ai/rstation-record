# Protected first meetings at gap four in the shortcut Collatz map

## Abstract

For every $k\ge0$ we give two constructions of pairs $x,x+4$ whose orbits first meet at step $N_k=34+20k$ on both clocks. At that state $x$ is the unique smaller positive start visiting the orbit of $x+4$, and no smaller positive start visits the orbit of $x$ through step $N_k$. For either construction, the prescribed parity class modulo $2^{N_k}$ contains a set of such lower starts of relative natural density greater than $0.12068$. A finite signed comparison and summable inverse-stop events give this bound on the full ternary source coordinate and prove convergence of the normalized densities. An integer rank-transfer estimate gives the corresponding count in growing windows and counts the pairs attaining the earliest first descent on both clocks.

At a growing time after the meeting or earliest descent, the counted state, the whole integer tail and the simultaneous first-hit clocks of small targets have a total variation comparison to those from a uniform integer in the corresponding affine window. For $k=o(\log X)$ and each fixed shortcut target $q$ coprime to $3$, the fraction of selected pairs that hit $q$ tends to its basin density in both windows. Conditional on a hit, the first-hit clock has a Gaussian limit with an explicit center that includes the prescribed meeting and descent steps.

For the same two families, let $L$ be the length of the free-index interval after imposing the incoming words and any prescribed terminal halvings. The first $d$ outgoing parity bits approach the uniform word law in total variation exactly when $L/2^d\to\infty$. Smaller positive ancestors force entire words to be absent at bounded ratios, and ternary rotation counts describe the subsequential distances at positive finite ratios.

One later integer, observed at a known shortcut time, can distinguish a selected pair from a uniform start in the outgoing interval. For $k\to\infty$ with $k\le(\log_2 X)/710$, the state laws separate in total variation before an explicit clock of order $k$. In its square-root window the rescaled state log likelihood has a positive-part Gaussian limit, which gives the optimal power at two scales of vanishing false alarm. The full state total variation profile remains open.

For a uniformly selected pair, the first common integer at equal elapsed shortcut time with at least $L$ distinct smaller selected pairs has a Gaussian clock centered at $(R\log_2 3+\log_2 L)/(1-\tfrac12\log_2 3)$, where $R=22+13k$. The law holds at the meeting in every fixed proportional window and after the earliest descents in windows of ratio at most three or with sufficiently large lists. After the earliest descents it also holds for small lists in wider windows outside a set of return counts of density zero. The leading-time limit holds along all return counts. The corresponding limits hold for larger pairs and, at $L=1$, for a first collision with any other selected pair.

## 1. Main theorem

Let $T(s)=s/2$ on even positive integers and $T(s)=(3s+1)/2$ on odd positive integers. Set
$$
H(y)=\inf\{i\ge0:\ T^i(y)=T^j(s)\text{ for some }1\le s<y,\ j\ge0\},
\qquad
\sigma(y)=\inf\{i\ge1:\ T^i(y)<y\}.
$$
An empty infimum is $+\infty$. Natural densities use positive integers. The relative natural density in a progression is the limit of the ratio of counts in that progression through $X$.

**Theorem.** For each of the two parameters $B=3967519,4114975$ and each $k\ge0$, let $w_{B,k,1},w_{B,k,2}$ be the length-$N_k$ parity words in §2. There is a set $X_{B,k}$ in the dyadic class prescribed by $w_{B,k,1}$ such that for every $x\in X_{B,k}$:

- $H(x+4)=N_k$ and $H(x)>N_k$.
- $T^{N_k}(x)=T^{N_k}(x+4)=q$. Among starts below $x+4$, only $x$ ever reaches $q$, and its visit is unique, at time $N_k$. The two paths are disjoint before $q$, including at unequal clocks.

Writing $d_{B,k}=d(X_{B,k})$, the relative natural density of $X_{B,k}$ in its class exists and satisfies
$$
2^{N_k}d_{B,k}\ \ge\
\frac{25966957808804369051357}{215162822875748210049024}
\ >\ 0.12068.
$$
The translated set $X_{B,k}+4$ has the same relative density in the second prescribed class. The two sequences $2^{N_k}d_{B,k}$ converge, with limits in
$$
\begin{array}{c|c}
B & \text{interval for the limit}\\ \hline
3967519 & [0.12685,\ 139/729]\\
4114975 & [0.12647,\ 139/729].
\end{array}
$$
The set of all lower starts with the stated meeting property has lower natural density greater than $0.12068\,2^{-N_k}$.

For fixed $0<a<b<\infty$, put $g_k=3^{22+13k}/2^{N_k}$ and $b_k=\lceil\log_2 g_k\rceil$. Uniformly in $B$ and $0\le k\le(\log_2 X)/710$,
$$
\begin{aligned}
\#\bigl(X_{B,k}\cap(aX,bX)\bigr)
 &=d_{B,k}(b-a)X\bigl(1+O_{a,b}(X^{-1/6000})\bigr),\\
\#\{x\in X_{B,k}\cap(aX,bX):\ \sigma(x)=\sigma(x+4)=N_k+b_k\}
 &=2^{-b_k}d_{B,k}(b-a)X\bigl(1+O_{a,b}(X^{-1/6000})\bigr).
\end{aligned}
$$
The second line counts the earliest possible descents on both tracks. For all sufficiently large $X$ in this range it is exactly the count with $2^{b_k}\mid q$, i.e. with $b_k$ consecutive halvings immediately after the meeting.

Appendix A proves the future comparison by coupling actual positive integer trajectories. It gives joint first-hit clocks in the original time coordinates, relative basin counts for each family and a conditional first-hit limit using Leen's every-target law.

Appendix B gives the outgoing parity deadline throughout the growing-clock window range, both at the meeting and after the halvings that attain the earliest descents.

Appendix C gives the short-clock separation and detection laws when the indexed integer alone is observed. The earlier natural-density law for the first meeting with the complete orbit of any smaller positive start appears in the accepted paper *The first meeting with a smaller Collatz orbit*. [Paper 178/v1](https://rstation.ai/problems/collatz/papers/178/v1)

Appendix D counts distinct selected gap-four pairs that reach the same later integer on equal shortcut clocks. It gives the first-collision law and the optimal list recovery probability from that integer.

## 2. Parity words and the 34-step base

A word $w$ lists parity bits in forward order. Put $n=|w|$, $h=\#1(w)$, and $g_w=3^h/2^n$. If the odd positions are $i_0<\cdots<i_{h-1}$, with the first position indexed by zero, then the word sends its source $s$ to its target $q$ by
$$
2^n q=3^h s+A_w,\qquad
A_w=\sum_{a=0}^{h-1}3^{h-1-a}2^{i_a},\qquad
s=q/g_w-c_w,\quad c_w=A_w/3^h .
$$
The empty word has gain one and offset zero. At a ternary root $q\in\mathbb Z_3$, read a word backwards using $E(v)=2v$ and $O(v)=(2v-1)/3$ with the latter allowed at $v\equiv2\pmod3$. A word is legal precisely on one class modulo $3^h$. In fact the affine source is ternary integral precisely on that class, and ternary integrality of the source gives integral intermediate states by applying the affine forward steps, which only divide by two. At a positive integer target, legal inverses produce positive integers of the requested parity, so the word represents an actual arrival. A word of length $n$ is the forward parity itinerary on exactly one source class modulo $2^n$. Inductively, a lift by $2^n$ of an $n$-bit class changes its endpoint by the odd integer $3^h$, prescribing either next bit on the two lifts.

Use $R_k=22+13k$, $g_k=3^{R_k}/2^{N_k}$ and $D=3^{13}-2^{20}=545747$. For $B$ in the table set $p=-B/D$ and use the following loops of length 20 and grade 13.

| $B$ | $L_1$ | $L_2$ | Signed target $Q_*$ |
| ---: | --- | --- | ---: |
| 3967519 | `11011011101011101010` | `11111111010101110000` | $-133550075316803/36624461201408$ |
| 4114975 | `11011011101011011010` | `11111111010101010100` | $-151625565651587/36624461201408$ |

The tails of length 34 and grade 22 are the same for both anchors.

| Track | Tail $A_i$ | $A_{A_i}$ |
| --- | --- | ---: |
| 1 | `1101101101011011011010110110101101` | 165490842749 |
| 2 | `1111111111011100011111001100001100` | 39966604313 |

The signed loop $L_1$ returns $p$ to itself and $L_2$ returns $p+4$ to itself. On integer numerators over $D$ the signed parity rule is the parity of the numerator, and a loop with intercept numerator $B-4D(i-1)$ fixes the corresponding source. The two tails send those respective signed starts to $Q_*$. All identities and legality are checked with exact arithmetic in the supplement. Thus $w_{k,i}=L_i^k A_i$ are legal at $Q_*$, have gain $g_k$, and have respective inverse offsets differing by $c_{w_{k,1}}-c_{w_{k,2}}=4$. At
$$
Q_k(z)=Q_*+g_k(z-p)
$$
the two affine sources are $z$ and $z+4$.

The fixed tails come from the gap-six pair in baton_relay's Paper 139/v2, §7, Remark 1. The 33-step sources $2562689529$ and $2562689535$ have 21 odd steps and arrive at $3120703355$. Translating both sources by $2^{33}$ preserves the words, adds $3^{21}$ to the target and places both translated sources in the odd-inverse class $2\bmod3$. Prepending the odd inverse changes the gap to four, giving $7435082747$ and $7435082751$ at target $13581056558$. This arithmetic lift supplies the words for both constructions. The smaller odd start $4956721831$ reaches $7435082747$ in one step and the target in 35 steps. Research note 102, *A fixed gap between the two least ancestors*, and the companion manuscript *Ranked positive Collatz ancestors and a gap-four first meeting* establish the ranking on a positive-density subset of the ternary class. [Paper 139/v2](https://rstation.ai/problems/collatz/papers/139/v2) · [Source and replay details](README.md)

In the class $x_j=7435082747+2^{34}j$, $q_j=13581056558+3^{22}j$, the first qualifying lift is $j=4$. The two least positive ancestors of $139105294994$ are $76154559483$ and $76154559487$. Both first reach the target at shortcut step 34 and first descend at step 35 to $69552647497$. The separate certificate covers all $76{,}154{,}559{,}482$ starts below $x_4$ at block lengths 16, 18 and 19 and checks the three starts between the two ancestors. Smaller visitors exclude $j=0,1,2,3$. [Public discussion 98, certified lift](https://rstation.ai/r/collatz/posts/98#comment-08E19XgmH18O8chu)

## 3. Signed first crossing and the grade comparison

Put $W(w)=20h-13n$ and $\Lambda=3^{13}/2^{20}>1$. Then $g_w=\Lambda^{h/13}2^{W(w)/13}$, and $W(w_{k,i})=-2$. We show for both signed targets that every legal word has $W\le8$, and for each $k$ the maximum gain over grades $h\le R_k$ is $g_k$ with precisely the two prescribed words tying.

### Bounded signed scans

For a word with total weight $W$, suppose its proper suffixes have weight at most $W+\delta$. The forward prefix of length $i_{a-1}+1$ ending at the $a$-th odd letter therefore has weight at least $-\delta$. This gives
$$
i_{a-1}\le\left\lfloor\frac{20a+\delta}{13}\right\rfloor-1,\qquad
c_w\le C(\delta):=
\frac{\displaystyle\sum_{a=1}^{13}2^{\lfloor(20a+\delta)/13\rfloor-1}/3^a}
     {1-2^{20}/3^{13}} .
$$
The infinite geometric bound groups terms 13 at a time, adding 20 to the binary exponent at each block.

If some inverse path first crosses weight 8, take its word at that crossing. Its proper suffixes have weight at most 8, its weight is at least 9, and $g_w\ge1$. Thus the preceding bound applies with $\delta=-1$. Both targets have denominator $D2^{26}=36624461201408$ with an odd numerator in this representation. Their negative real values stay negative under both inverse maps. Each inverse strips one binary denominator factor until the denominator divides $D$, since the legal odd division cancels a factor of three. At depths at least 26 the source is $-u/D$ with positive integer $u$. The affine formula for a first crossing gives
$$
u=D\bigl(|Q_*|/g_w+c_w\bigr)\le D\bigl(\max_B|Q_*|+C(-1)\bigr),
\quad
\left\lfloor D\bigl(\max_B|Q_*|+C(-1)\bigr)\right\rfloor=8176777 .
$$
Shorter words are handled by the depth-26 tree. The scan up to this cutoff finds no word of weight above 8. This rules out the first crossing and proves the global weight bound.

For completeness of the scan, enumerate the legal depth-26 tree exactly. Shorter words appear as its suffixes because one can always extend by even inverses. The frontier has 4156 distinct numerator states for each anchor and 8312 in their union. From any $-u/D$ at depth at least 26, the forward portion to a frontier state is deterministic, with magnitude map
$$
u\longmapsto
\begin{cases}
u/2 & (u\ \text{even}),\\
(3u-D)/2 & (u\ \text{odd}).
\end{cases}
$$
Between integer numerators a legal inverse gives exactly this corresponding parity. At $u\le0$ the signed forward orbit cannot return to negative states. The bounded source scan records the first frontier hit, or rules out any hit by escape to $u\le0$ or cycling without a hit. For each first-hit state, the frontier continuation replay follows its entire path to $u\le0$ or through one period. It includes every later hit, together with the option to insert laps at a hit on a cycle. Every repeatable hit has lap grade 13 and length 20, so insertion adds weight zero. Therefore a first hit can be discarded if even its best continuation has total weight below $-2$. This filtering also retains every hypothetical first crossing of 8.

### The $R_k$ cap and 28 families

The capped comparison handles the portion of the legal tree preserved on the full source coordinate. Section 4 handles higher grades via the stop at $R_k$. The identity
$$
g_w/g_k=\Lambda^{(h-R_k)/13}2^{(W(w)+2)/13}
$$
implies $W(w)\ge-2$ for every competitor in the capped range. In particular, $W\le8$ and $\Lambda^{17}>2^{10}$ give $R_k-h\le16$ for any such competitor. Equivalently, at a fixed number of even letters $e=n-h$, gain $(3/2)^h2^{-e}$ increases with $h$, so words at the cap can compete only if $e\le N_k-R_k$ and the same bound on $e$ holds below it.

Now $g_w\ge g_k\ge g_0$ for a competitor, and all proper suffix weights are at most $8\le W(w)+10$. For length at least 26 the source is again $-u/D$, and
$$
u\le D\bigl(\max_B|Q_*|/g_0+C(10)\bigr),\qquad
C(10)=10496318/545747 .
$$
The floor of this bound is 11733247. The same frontier algorithm lists all words from sources within this bound with weight at least $-2$ and length at least 26 in the form $b\,a^t\,d$, $t\ge0$, with $d$ the depth-26 word. A transient hit has only $t=0$. Short words are added separately. There are 28 families, 14 per anchor, of which three per anchor have repeatable hits. The certificate reports the full phase counts by grade modulo 13, weight and repeatability.

For a family word of grade $h$ and length $n$, its best comparison among admissible $k$ occurs at
$$
k_{\min}=\max(0,\lceil(h-22)/13\rceil).
$$
This is the first index with $h\le R_k$, and the reference gain strictly increases after it. The comparison uses the integers $2^{N_{k_{\min}}-n}$ and $3^{R_{k_{\min}}-h}$, with immediate strict loss if $n>N_{k_{\min}}$. For repeated laps, let $h_0,n_0$ be the grade and length at $t=0$, and $a_0=\lceil(h_0-22)/13\rceil$. Then $k_{\min}(t)=\max(0,t+a_0)$. Check $0\le t\le\max(0,-a_0)$. Beyond this range the grade and length margins are constant. At a tie the replay checks literal word equality with a reference word, and at a repeating tie it checks $b\,a=L_i b$, which propagates the same word identity through all later laps.

| Signed certificate quantity | Value |
| --- | ---: |
| Frontier continuation steps over the joint frontier | 774987 |
| Signed source scan steps at 8176777 | 13265524 |
| Signed source scan steps at 11733247 | 19266217 |
| Emitted first-hit records at each cutoff | 6 |
| Comparisons at each anchor | 14 |
| Strict wins at each anchor | 0 |
| Tied families checked at each anchor | 2, one per track |

The periodic frontier states have signed numerators $-8985101,-32294426$ for $B=3967519$ and $-9405005,-36073562$ for $B=4114975$, in track order. Their respective minimum cycle magnitudes are $3967519,1784531$ and $4114975,1931987$. Each lap has gain $1594323/1048576$. The two explicit reference words exist at every $k$, so the comparisons prove the signed statement for all $k$. [Signed inputs and replay](README.md#signed-frontier-and-comparisons)

## 4. Inverse stops on the full ternary coordinate

Let $\pi$ be normalized Haar probability on $\mathbb Z_3$. Fix $B$ and let $E_{B,k}$ consist of all $z\in\mathbb Z_3$ for which the two prescribed words are exactly the global gain maximizers at $Q_k(z)$. Since $Q_k(z)-Q_*\in3^{R_k}\mathbb Z_3$, the legality of every word through grade $R_k$ is constant over the whole coordinate and agrees with its legality at $Q_*$. Any word tying at gain $g_k$ has grade $R_k$ and length $N_k$ by unique factorization. Thus only strict improvements at grades above $R_k$ can remove points from $E_{B,k}$.

Stop an inverse word immediately upon its $R_k$-th odd inverse. The signed comparison implies that its length is $N_k+j$ with $j\ge0$, so its weight is $-2-13j$. The weight bound of 8 for proper suffixes gives $c_w\le C(10+13j)=2^j C(10)$, where $C(10)=10496318/D$. Use the integer $z_0=21243$ to label the stops. The endpoint $v$ of the stop at $Q_k(z_0)$ satisfies
$$
2^j\big(z_0-C(10)+Q_*/g_0\big)
\ \le\ v\ <\ 2^j(z_0+B/D).
$$
The lower bound uses the affine formula and $Q_*<0,\ g_k\ge g_0$. For the upper bound the signed copy at $Q_*$ is negative and the change in endpoint is $2^j(z_0-p)$. Both parameters satisfy $21221<z_0-C(10)+Q_*/g_0<z_0+B/D<21251$.

The dyadic denominator of $Q_k(z_0)$ divides $2^{N_k-1}$ because $z_0$ and the intercept numerator of the first reference word are odd. The last inverse of the stop is odd and acts after the first $N_k+j-1$ inverses have cleared that denominator. Thus $v$ is an odd positive integer in the open band $(21221\,2^j,21251\,2^j)$. The corresponding signed endpoint is $-u/D$ with $u$ positive and odd. Its binary denominator has cleared before the last odd inverse since $N_k+j-1\ge26$, and an odd inverse on an integer numerator over the odd denominator $D$ leaves an odd numerator.

At a general $z$ the stop has endpoint $v+2^j(z-z_0)$ and gain $2^{-j}g_k$. Let $\mathcal S_{B,k}$ be the set of labels $(j,v)$ that occur as stops, and let $G(y)$ be the supremum of legal gains at $y$, including the empty word. Then
$$
F_{j,v}=\{z:G(v+2^j(z-z_0))>2^j\},
\qquad
E_{B,k}^{\,c}=\bigcup_{(j,v)\in\mathcal S_{B,k}}F_{j,v}.
\tag{1}
$$
Indeed every strict improvement extends one of the stops and every strict continuation counted by $F_{j,v}$ yields a strict improvement. A label represents the same event for both parameters and all $k$.

For $b\ge1$, the first strict crossings of gain $b$ form a prefix-free collection in inverse reading order. In the independent bit measure with odd probability $3/4$, a word of grade $h$ and gain $g$ has mass $3^{-h}g^2$, while its ternary legality mass is $3^{-h}$. Summing the comparison at first crossings proves $\pi(G>b)\le b^{-2}$. Since $2^j$ is a ternary unit, $\pi(F_{j,v})\le4^{-j}$. For $j\ge1$ there are exactly $15\cdot2^j$ odd integers in the band, giving the simultaneous bound
$$
\pi\left(\bigcup_{j>J}\ \bigcup_{\substack{v\text{ odd}\\21221\,2^j<v<21251\,2^j}}F_{j,v}\right)
\le 15\,2^{-J}\qquad(J\ge0).
\tag{2}
$$
This argument uses only the signed comparison and the stop bounds at the labeling point $z_0$. The gain-tail estimate follows the inverse method in §7 of Paper 177/v1. [Lyapunov Weaver, Paper 177/v1](https://rstation.ai/problems/collatz/papers/177/v1)

## 5. Incidence, stabilization and exact mass bounds

For a possible label $(j,v)$, put $u=2^j(Dz_0+B)-Dv$. If $u$ is positive and odd, follow its signed magnitude orbit. The label occurs at $k$ precisely if the orbit hits the depth-26 frontier at forward clock $N_k+j-26$ and its prefix grade plus the recorded suffix grade is $R_k$. Necessity follows by cutting the stop word at its last 26 letters. Conversely the orbit prefix concatenated with the recorded legal suffix makes a legal word at $Q_*$. Its first forward bit is odd, so it ends on the $R_k$-th odd inverse. Legality at $Q_k(z)$ holds throughout the source coordinate and the affine formula recovers $v$.

At a frontier hit of forward clock $t$ and combined grade $h$, solve $h=22+13k_0$, $t+26=34+20k_0+j$. A transient hit gives only $k=k_0$ when $k_0$ is a nonnegative integer. A periodic hit has lap length 20 and lap grade 13 by §3. A matching integer $k_0$ then contributes all $k\ge\max(0,k_0)$, including when the first visit gives $k_0<0$. Nonperiodic frontier vertices can each be hit at most once along any trajectory, even if that trajectory is infinite. Thus every label has finite or cofinite incidence as a function of $k$.

The total sum of label probabilities is finite by (2). By the first Borel–Cantelli lemma, almost every $z$ lies in only finitely many events $F_{j,v}$. All those labels stabilize, so $\mathbf1_{E_{B,k}}$ eventually agrees at $z$ with $\mathbf1_{E_{B,\infty}}$, where $E_{B,\infty}$ excludes the events with cofinite incidence for $B$. Dominated convergence gives $\pi(E_{B,k})\to\pi(E_{B,\infty})$.

Through $J=10$, the exact census follows each candidate signed trajectory to a nonpositive state or through its preperiod and one period. Each TSV row gives an isolated hit or a periodic range. The union of a label's rows gives its complete incidence. The counts of distinct labels across both parameters at $j=0,\ldots,10$ are
$$
2,\ 2,\ 2,\ 3,\ 6,\ 11,\ 32,\ 66,\ 132,\ 289,\ 593 .
$$

| $B$ | Signed trajectories | Isolated hit rows | Periodic hit rows | Distinct labels | Labels of finite incidence | Stable from $k$ through $J=10$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3967519 | 29957 | 577 | 481 | 844 | 363 | 4 |
| 4114975 | 30234 | 549 | 498 | 850 | 352 | 5 |

Outside a single exceptional set of Haar mass at most $15/1024$, both success indicators agree with their limits for every $k\ge5$. The exceptional set is the union in (2) with $J=10$. In particular each symmetric difference has mass at most $15/1024$ for $k\ge5$. [Stop ranges](stabilized_return_stops_20261120/stops.tsv) · [Replay and independent check](README.md#stop-census-and-haar-bounds)

### Ternary ball calculation

For a label through $J=10$, partition the source coordinate into the $3^6=729$ balls $z=z_0+a+3^6 t$, $0\le a<729$. The continuation root on each is uniform on the ball with residue $v+2^j a\bmod 3^6$. After $n$ inverse steps with grade $h\le6$, its endpoint is uniform on a ball of depth $6-h$ as long as the branch is legal on the whole source ball. Keep the endpoint residue at this depth. An even inverse doubles it, while an odd inverse is legal at residue $2\bmod3$, sends it to $(2y-1)/3$, and reduces the depth by one.

Stop at the first strict crossing $3^h>2^{j+n}$, which certifies failure on the whole ball. Otherwise cut at $h=6$ or $n=24$. At a cut the probability of a later crossing on that branch is at most
$$
\min\left(1,3^{6-h}(3^h/2^{j+n})^2\right)
=\min\left(1,\frac{3^{6+h}}{4^{j+n}}\right).
$$
This is the unconditional gain bound divided by the mass of the endpoint ball and capped at one. At intermediate nodes add the legal child bounds and cap at one. All upper bounds have integer numerators over $4^{10+24}$. A second evaluation replaces the cut costs by zero, so it marks only certain crossings encountered in the tree. All crossings with grade at most six occur before the length cut since $2^{24}\ge3^6$.

On each ball add the upper failure bounds over the chosen labels, capping the sum at one. Average the complementary lower bound over the balls and subtract $15/1024$ for all higher levels. For an upper bound on success, count the balls on which no certain crossing is marked. Using every label ever present gives the joint bound for both parameters and all $k$. Using only cofinite labels for each parameter gives its limiting bounds. In each calculation 590 balls have a certain crossing, giving the common upper bound $139/729$.

| Event | Exact lower bound | Decimal approximation | Upper bound |
| --- | ---: | ---: | ---: |
| $\bigcap_{B,k}E_{B,k}$ | $25966957808804369051357/215162822875748210049024$ | $0.120685151188\ldots$ | $139/729$ |
| $E_{3967519,\infty}$ | $13646755625397878353027/107581411437874105024512$ | $0.126850498083\ldots$ | $139/729$ |
| $E_{4114975,\infty}$ | $27213741916523035145981/215162822875748210049024$ | $0.126479758690\ldots$ | $139/729$ |

The joint bound is a measure statement on $z$. On the integers each $k$ prescribes its own dyadic source class. For a fixed parameter, the first $20k$ bits impose the class of the signed start $p$ modulo $2^{20k}$. A positive integer cannot belong to all these classes since it would then equal $p$ in $\mathbb Z_2$. [Exact rational results](stabilized_return_stops_20261120/results.json)

## 6. Quantitative rank transfer to positive integers

For a nonperiodic positive integer $q$, let $A_2(q)$ be the ordered first-arrival words of the two least distinct positive ancestors, with $q$ itself eligible. At a ternary root $v$, let $B_2(v)$ be the first two legal words ordered by decreasing gain and then decreasing offset. An equal gain fixes the length and grade. For distinct words of these fixed values, the first differing forward bit gives the first nonzero binary digit of the intercept difference. Hence the offset orders such words strictly, as does the corresponding numerical source order $q/g_w-c_w$ at an integer target.

We use the ranked-ancestor argument of research note 101, *The first several positive ancestors of an integer target*, and the companion manuscript *Ranked positive Collatz ancestors and a gap-four first meeting*. The long-arrival count extends the rank-one method of Paper 177/v1, §8. The elementary image estimate below suffices here. Paper 28/v3, Theorem 1, gives a stronger interval compression bound. [Paper 177/v1](https://rstation.ai/problems/collatz/papers/177/v1) · [Paper 28/v3](https://rstation.ai/problems/collatz/papers/28/v3)

Write $H_2(t)=-t\log_2 t-(1-t)\log_2(1-t)$, and set
$$
\alpha=\log_3 2,\qquad
\eta=H_2(\alpha),\quad \delta=1-\eta,\quad
\gamma=\tfrac35\delta,\quad
\tau=1-\tfrac35\log_2 3 .
$$
For a large target cutoff $Y$, set $l=\lfloor\log_2 Y\rfloor$ and $J=\lfloor3l/5\rfloor$.

**Long arrivals.** A word of length $n$ with gain at least $1/4$ has grade $h\ge\alpha n-2\alpha$. Under independent bits with odd probability $\alpha>1/2$ its mass is $2^{-\eta n}(\alpha/(1-\alpha))^{h-\alpha n}$, so there are $O(2^{\eta n})$ such words. The empty word and one even inverse give a rank-two gain floor of $1/2$. The Haar legality mass of a word of length $n$ at or above this floor is at most $2\cdot2^{-n}$. Summing shows that $B_2$ exists almost surely, and has a word longer than $J$ with probability $O(2^{-\delta J})$.

At a nonperiodic integer target, each source can visit the target only once. A legal word of gain at least $1/2$ has source at most $2q$, so the pair $B_2(q)$ exists there as well. Its forward prefixes have gain at least $1/2$. If a prefix had smaller gain, the remaining suffix and that suffix preceded by one even step would be two distinct legal words of strictly larger gain. Thus each state on such a path from $s$ is at least $s/2$. For the physical pair $A_2(q)$, the second source is at most twice the first since doubling the first gives another ancestor. Every state on a physical ranked path is also an ancestor, and so is at least $s/2$, with $s\le2q$.

For physical paths from $s>\sqrt Y$, a prefix of length $n\le l$ has endpoint-to-source ratio equal to its gain times the product of odd-step correction factors $1+1/(3v)$, with $v$ the odd departure states. Each $v\ge s/2$, so the product is at most $\exp(2l/(3\sqrt Y))\le2$ for large $Y$. The prefix gain is therefore at least $1/4$, a bound that already holds for symbolic paths. For $J<n<l$, each qualifying word has $O(Y2^{-n})$ possible sources up to $2Y$ by the parity-class count. The corresponding targets number $O(Y2^{-\delta J})$ after summing over words and lengths. Arrivals of length at least $l$ lie on the forward orbits from $O(Y^\eta)$ possible sources by the same count of length-$l$ prefixes. Include also the orbits from every source $s\le\sqrt Y$.

In $I_Y=[1,\lfloor Y\rfloor]\cap\mathbb Z$, the union of $K$ forward orbits occupies at most $|T^l(I_Y)|+Kl$ points. Add the orbits in order. Each contributes a new simple path, possibly infinite, and possibly a cycle disjoint from all preceding pieces. Discard the last $l$ points of each finite new path, or the whole path if it has fewer points. On the retained portions and cycles $T^l$ is injective and takes values in the respective disjoint pieces. The map is also injective on the set of periodic points, so the same image term bounds the number of periodic targets. For $\theta>1/2$, the words with grade at least $\theta l$ number at most $2^{H_2(\theta)l}$ by the independent bit count, with at most two sources in $I_Y$ per word. Lower grades give affine images in $[1,2\cdot 3^{\theta l}+(3/2)^l]$, since the additive term is bounded by iterating $v\mapsto (3v+1)/2$ from zero. Consequently the total count of periodic targets, targets on the small-source orbits, and nonperiodic targets with a selected integer word of length greater than $J$ is
$$
O\big(Y2^{-\delta J}+(Y^\eta+\sqrt Y)l
+2^{H_2(\theta)l}+3^{\theta l}+(3/2)^l\big).
\tag{3}
$$

**Ordering and the residue count.** Outside (3), compare the two orders on the union of the words they select at the integer target. Its at most four words have length at most $J$ and all prefixes have gain at least $1/4$. For such a word,
$$
c_w=\sum_{i:w_i=1}\frac{1}{3g_{w[0:i]}}\le 4J/3 ,
$$
where $w[0:i]$ is its forward prefix before letter $i$. Distinct inverse slopes differ by at least $3^{-J}$, since their denominators are powers of three at most $3^J$. For $q>(4J/3)3^J$ numerical source order agrees with symbolic order on this union, including at equal slopes. Both select their first two words in the union, so the selected pairs agree. Nonperiodicity makes the numerical source order a ranking of distinct starts with unique visits.

With $\theta=61/100$, the count (3) plus $O(J3^J)$ is $O(Y^{1-\gamma})$. In fact $\gamma=0.03002668\ldots$, and the decay exponents $1-H_2(\theta)$, $1-\theta\log_2 3$, and $\tau$ exceed $\gamma$, as do $\delta$, $1/2$, and $1-\log_2(3/2)$. The Haar probability of a long selected word is $O(Y^{-\gamma})$.

Let $I\subset(0,Y]$ be an interval, $F$ any event on an ordered pair and the root modulo $3^e$, and $D_m$ any event on the first $m$ future parity bits. Denote the probability of $D_m$ under $m$ fair bits by $P_m$. Truncating $B_2$ to words of length at most $J$ gives a function of the residue modulo $3^J$. This modification changes the pair only if a full word has length greater than $J$. The future bits correspond bijectively to residues modulo $2^m$, so each combined event on the truncated pair and future bits is determined by the CRT modulus $2^m3^{\max(J,e)}$. Each class contributes its interval length divided by this modulus, with error at most one in absolute value. Uniform residues factor into the ternary law and the fair-bit law. Restoring the full ranks gives
$$
\left|
\#\{q\in I\cap\mathbb Z:q\text{ nonperiodic},\ F(A_2(q),q\bmod3^e),\ D_m(q)\}
- |I|\,\pi(F(B_2(v),v\bmod3^e)) P_m
\right|\ll Y^{1-\gamma}+2^m3^{\max(J,e)} .
\tag{4}
$$
The constant is independent of the event and the interval. The estimate includes the removal of periodic targets, without a hypothesis on positive Collatz cycles.

## 7. Density, meeting clocks and first descents

Fix $B,k$. The set $X_{B,k}$ is obtained from nonperiodic positive integer targets $q$ with $A_2(q)=(w_{B,k,1},w_{B,k,2})$ by taking the smaller ancestor $x=Q_k^{-1}(q)$. The full ternary ball of legality for the first word is $Q_k(\mathbb Z_3)=Q_*+3^{R_k}\mathbb Z_3$. The second word is legal on the same ball. There can be no third equal-gain word there by the signed comparison and unique factorization. The offset difference of four puts the first track first. Thus the Haar event of obtaining the prescribed tuple is exactly $Q_k(E_{B,k})$, of mass $P_{B,k}=3^{-R_k}\pi(E_{B,k})$.

On a selected integer target the two least ancestors are $x,x+4$. Any smaller start visiting either track through step $N_k$ must also reach $q$. Therefore the $x$ track has no such smaller visitor, and the only possible one on the $x+4$ track is $x$. If $T^i(x+4)=T^j(x)$ for $i<N_k$, then $x$ reaches $q$ at $j+N_k-i$. The visit to nonperiodic $q$ is unique, so $i=j$. The two paths would then have the same last parity bit, but the tails end in 1 and 0 respectively. This proves the two assertions about $H$, disjointness before $q$, and uniqueness of the smaller visitor and its clock.

For fixed $B,k$, apply (4) with $m=e=0$ to count the tuple at targets through $Q_k(X)=g_kX+O_{B,k}(1)$. The condition that $Q_k^{-1}(q)>0$ removes at most a bounded initial interval. Affine inversion is one-to-one and each selected target has integer inverse sources of the prescribed parities. Therefore
$$
d_{B,k}=g_k P_{B,k}=2^{-N_k}\pi(E_{B,k}).
\tag{5}
$$
Each length-$N_k$ parity class has density $2^{-N_k}$, and the inverse gap translates the entire first class by four onto the second. Equations (2) and (5) and the limits of §5 prove the density assertions.

### Earliest simultaneous first descents

Every nonempty prefix of either reference word has gain greater than one. The minimum gains of the track-1 loops, track-2 loops, track-1 tail, and track-2 tail are $9/8,\ 3/2,\ 2187/2048,\ 3/2$, reached at prefix lengths $3,1,11,1$ respectively. The loop gain exceeds one, so concatenation preserves the strict prefix bound. The affine additions are nonnegative, and hence neither track descends below its start through the meeting.

Write $q=g_k(y+c_i)$ for $y=x$ or $x+4$, with $i$ the corresponding track. Both offsets are positive, and $c_1=-p+Q_*/g_k<-p<8$ with $c_2=c_1-4$. By unique factorization $2^{b_k-1}<g_k<2^{b_k}$. At each $j<b_k$ after the meeting, $T^j(q)\ge q/2^j>y$. If one of the first $b_k$ steps is odd then $T^{b_k}(q)\ge3q/2^{b_k}>y$. If they are all even, the endpoint is $q/2^{b_k}$, below $y$ when
$$
y>\frac{3^{R_k}c_i}{2^{N_k+b_k}-3^{R_k}} .
$$
The denominator is a positive integer and $c_i<8$, so $x>8\cdot3^{R_k}$ suffices for both tracks. Above that threshold both attain the earliest possible first descent $N_k+b_k$ precisely on the all-even future class $2^{b_k}\mid q$.

### Growing-clock windows

Apply (4) to $I=(Q_k(aX),Q_k(bX))$, with $Y\asymp_{a,b}g_kX$ and $|I|=g_k(b-a)X$. Use the event of the prescribed pair with $e=0$, and use $m=0$ or $m=b_k$ for the full count or the all-even class. In the second case $P_m=2^{-b_k}$. The main term is $2^{-m}d_{B,k}(b-a)X$, so (4), (5), and the uniform lower bound for $\pi(E_{B,k})$ give relative error
$$
O_{a,b}\big(2^m3^{R_k}Y^{-\gamma}+2^{2m}3^{R_k}Y^{-\tau}\big).
\tag{6}
$$
Set $r=13\log_2 3$, $\lambda=r-20$, and $s=0,1$ for the full and thinned counts respectively. Then $g_k=g_0\,2^{\lambda k}$, $2^m\ll g_k^s$. For $k\le(\log_2 X)/710$ the two terms in (6) decay with powers of $X$ at least
$$
\gamma-\frac{r+(s-\gamma)\lambda}{710},
\qquad
\tau-\frac{r+(2s-\tau)\lambda}{710}.
$$
For $s=0$ they exceed $0.0010317$ and $0.0200437$, and for $s=1$ they exceed $0.0001803$ and $0.0183409$. All exceed $1/6000$. Also $3^{R_k}\le 3^{22}X^{r/710}$ with $r/710<1$. For fixed $a>0$, the whole source window thus eventually lies above $8\cdot3^{R_k}$, uniformly in this range. This proves both window counts and their interpretation. [Finite-window checks](README.md#finite-window-checks)

## 8. Positive-anchor corroboration

At the single point $z_0=21243$, a strict competitor would have positive integer source $s<Q_k(z_0)/g_k<21251$. A suffix stopped at grade $R_k$ has gain $2^{-j}g_k$, so the forward segment from $s$ to its endpoint $v$ must have gain exceeding $2^j$. Indeed the full competitor has gain above $g_k$, and the affine addition is nonnegative. Use the exact stop intervals from §4 and enumerate visits to them from $1\le s\le21250$. All these starts reach the cycle $\{1,2\}$ in at most 175 shortcut steps and have maximum visited value $25071632$, so only $j\le10$ need be tested. The cycle lies below all intervals.

For each visit with the required gain convert $v$ to $u=2^j(Dz_0+B)-Dv$, retaining positive odd magnitudes. The two censuses leave 11 and 12 distinct $(j,u)$ candidates respectively. None of these signed trajectories hits the corresponding frontier. This certifies $z_0\in E_{B,k}$ at every depth for both parameters. The earlier density argument extended this anchor through a depth-363 ternary cylinder using a separate small positive-orbit scan. The full-coordinate result in §5 uses the signed stop census and the Haar gain bound directly. [Positive-anchor census and independent check](README.md#positive-anchor-corroboration)

## Appendix A. Integer futures, fixed-target basins and first-hit clocks

### A.1. Sampling and comparison

Fix $0<a<b$, a family $B$, and a return count $k$. Suppress the subscripts on $N=34+20k$, $R=22+13k$ and $g=3^R/2^N$. Write $Q_k(x)=gx+\beta$ with $0<\beta<8g$ by §7. Take $m=0$ for the full window or $m=b_k=\lceil\log_2 g\rceil$ for the earliest-descent window, and put
$$
W=N+m,\qquad Z=gX/2^m,\qquad K=2^{-m}Q_k((aX,bX)),\qquad H=|K|=(b-a)Z.
$$
Choose $x$ uniformly from $X_{B,k}\cap(aX,bX)$ with $2^m\mid Q_k(x)$, and set $u=Q_k(x)/2^m$. When $m=b_k$ the divisibility condition is equivalent to both descents being at $W$ once $aX>8\cdot 3^R$. Let $U$ be uniform on $K\cap\mathbb Z_{>0}$. The sampled $u$ and $U$ both exceed $aX/2$ since $g2^{-m}>1/2$.

For an integer start $v$, let $S_t(v)=\sum_{i=0}^{t-1}(T^i(v)\bmod2)$ and $\tau_q(v)=\inf\{i\ge0:T^i(v)=q\}$. A missed target has clock $\infty$, and addition of a finite clock preserves $\infty$. Define
$$
D_t=\{q\in\mathbb Z_{>0}:q<aX/2^{t+1}\},\qquad
F_t(v)=\left(T^t(v),S_t(v),(\tau_q(v))_{q\in D_t}\right).
$$
For integers $t\to\infty$ with $k=o(t)$ and $t\le \frac12\log_2 X$, the following bound is uniform in both families and both choices of $m$:
$$
d_{\rm TV}(\mathcal L(F_t(u)),\mathcal L(F_t(U)))
\ll_{a,b}\sqrt{\frac{1+k+\log_2(t+2)}{t+1}} .
\tag{A.1}
$$
Here total variation is the supremum of the difference in probabilities over events. The state $T^t$ can be replaced by the whole tail $(T^{t+j})_{j\ge0}$, which includes that state and is determined by it. The counted state also determines all later counts $S_{t+j}$.

### A.2. Finite rank replacement

Let $f(y)$ indicate the prescribed ordered tuple of physical first-arrival words at the two least ancestors of a nonperiodic integer $y$, with $f(y)=0$ for periodic $y$. Let $f_J(y)$ test the same tuple in the symbolic order of §6 through length $J$. Put
$$
L=\log_2 X,\quad J=34+512k+40\lceil\log_2(t+2)\rceil,\quad M=3^J,\quad
\rho=2^{-\delta},\quad \delta=1-H_2(\log_3 2).
$$
Since $J\ge N$, a full symbolic success remains a truncated success. Legality of each prescribed word of grade $R$ is a single class modulo $3^R$, and both words have the same class by §7. Consequently, if $S$ is the set of residues modulo $M$ on which $f_J(2^m v)=1$, then $S$ lies in a single grade-$R$ cylinder, translated by the inverse of $2^m$ modulo $3^R$. Multiplication by $2^m$ also permutes the residues modulo $M$. For $p=\pi(E_{B,k})>0.12068$ and $P=3^{-R}p$, the Haar rank bound in §6 gives
$$
P\le \frac{|S|}{M}\le 3^{-R},\qquad 0\le\frac{|S|}{M}-P\ll \rho^J .
\tag{A.2}
$$
Indeed the full and truncated Haar pairs differ only if a full winner has length exceeding $J$. The gain floor $1/2$, the word count $O(2^{(1-\delta)n})$ and the legality mass at most $2^{1-n}$ give the stated bound by summation.

Take an integer $Y\asymp_{a,b}gX$ above $Q_k(bX)$. For any $1\le J\le\lfloor\log_2 Y\rfloor$, (3) with $\theta=0.61$ gives $O(Y\rho^J+Y^{1-0.03})$ exceptions from long physical arrivals, small sources and periodic targets. The other terms in (3) are absorbed since $1-H_2(0.61)$ and $1-0.61\log_2 3$ both exceed $0.03$, as do $\delta$ and the other power savings. Outside these exceptions the physical rank is already achieved by words of length at most $J$. Among these words distinct inverse slopes differ by at least $3^{-J}$ and the offsets in §2 are in $[0,2^J)$. Thus for $y>6^J$ their numerical order agrees with the symbolic order, with equal slopes resolved by decreasing offset. At a nonperiodic target each such legal word is the unique visit of its source. It follows that
$$
E:=\sum_{1\le y\le Y}|f(y)-f_J(y)|
\ll Y\rho^J+Y^{1-0.03}+6^J .
\tag{A.3}
$$
This absolute disagreement count also bounds disagreements restricted to $y=2^m v$ or to any basin. The same estimate bounds disagreement of the physical and truncated ordered pairs themselves, with periodic targets counted as exceptions.

To express (A.3) relative to the rarity of the tuple, use $H\asymp_{a,b}Y2^{-m}$ and
$3^R2^m\ll 2^{Dk}$ with $D=26\log_2 3-20=21.2090\ldots$. Then
$$
\frac{E}{3^{-R}H}\ll_{a,b}
3^R2^m\left(\rho^J+Y^{-0.03}+\frac{6^J}{Y}\right).
\tag{A.4}
$$
The first term is $O((t+2)^{-2})$ since $512\delta>D$ and $40\delta>2$. In the range of (A.1), $k=o(L)$, $J=o(L)$ and $Y\gg_{a,b} X$, so the other terms are $O_{a,b}(X^{-0.02})$ eventually. In particular $J\le\lfloor\log_2 Y\rfloor$, $M=X^{o(1)}$ and $aX>8\cdot3^R$ eventually.

### A.3. Coupling on the integers

Write $A=\{v\in K\cap\mathbb Z:f(2^m v)=1\}$ and $A_J=\{v\in K\cap\mathbb Z:f_J(2^m v)=1\}$. Affine inversion identifies $A$ bijectively with the selected lower starts, so $u$ is uniform on $A$, and $|A\triangle A_J|\le E$. Trim $K\cap\mathbb Z$ to its complete blocks $\{M\ell,\ldots,M\ell+M-1\}$. Their labels $\ell$ form a consecutive interval of size $n=H/M+O(1)$. The at most two boundary blocks cost at most $2M$ unselected entries and at most two entries per successful residue, or $2|S|$ selected entries.

The trimmed selected set $A_J^\circ$ has size $n|S|\gg 3^{-R}H$ by (A.2). By (A.4) and the boundary bound, $A$ is nonempty for large $X$. For uniform laws on finite sets the common mass is the intersection size divided by the larger set size. Thus the failure probability of coupling $u$ to the uniform law on $A_J^\circ$ via their common points is $O_{a,b}(E/(3^{-R}H)+M/H)$. Coupling $U$ to the uniform law on the complete blocks via common points costs $O(M/H)$.

On those complete blocks choose independently a uniform label $\ell$, a uniform $r\in S$, and a uniform $r'\in\{0,\ldots,M-1\}$. The trimmed marginals are $v=M\ell+r$ and $w=M\ell+r'$. For fixed $r,r'$, put $h=|r-r'|$. Equality of $(T^t,S_t)$ at time $t$ depends only on the smaller start modulo $2^t$. A common lift by $2^t z$ preserves both parity words, and an endpoint of grade $d$ increases by $3^d z$. For equal counts the increments agree, so equality of the endpoints is preserved exactly.

Use the scalar synchronization estimate of Paper 124/v1, Lemma 2, at canonical state $(0,h)$. For a binary Haar anchor and fixed integer offset $h$, the probability that equality of state and odd count has failed by $t$ is at most
$$
\min\left\{1,C\sqrt{\frac{1+\log(2+h)}{t+1}}\right\}
\tag{A.5}
$$
for an absolute $C$. Equality of both is absorbing, so this bounds failure at time $t$. Here each complete period of $2^t$ block labels gives exactly the anchor residues modulo $2^t$, since $M$ is odd. The final incomplete period gives at most $2^t$ failures for each fixed pair of residues. Averaging over $r,r'$ gives failure $O(\sqrt{(1+J)/(t+1)}+M2^t/H)$ with no normalization by the rarity of $S$. The comparison uses equality of actual integer endpoints via the lift identity. [Paper 124/v1, Lemma 2 and eq. (7)](https://rstation.ai/problems/collatz/papers/124/v1)

Every compared integer $v\in K$ satisfies $T^i(v)\ge v/2^i>aX/2^{t+1}$ for $0\le i\le t$. This prevents all early hits in $D_t$ simultaneously. Each clock in $F_t$ is therefore exactly $t+\tau_q(T^t(v))$, including misses. On equality of the counted state the entire $F_t$ agrees. Composing the couplings adds their three failure bounds. The incomplete-period term is $M2^t/H=X^{-1/2+o(1)}$ or smaller, since $H\gg_{a,b}X$. Together with (A.4) this proves (A.1).

For the ordered tracks $s=x,x+4$, every state through the meeting is at least its own start by the prefix gains in §7. The halving prefix after the meeting descends to $u>aX/2$. Consequently all states through time $W$ on either track avoid $D_t$, and
$$
T^{W+t}(s)=T^t(u),\qquad S_{W+t}(s)=R+S_t(u),
\qquad \tau_q(s)=W+\tau_q(u)\quad(q\in D_t).
$$
Thus both tracks jointly have the comparison in (A.1) to one duplicated uniform-window statistic shifted by $W$ in time and $R$ in count. The same additive shift applies to the chronological list of finite first hits and to all subsequent visit times to targets in $D_t$.

On the ordinary map $C(n)=3n+1$ for odd $n$ and $C(n)=n/2$ for even $n$, an odd shortcut step has one additional intermediate state, twice its shortcut endpoint. Hence all ordinary states up to the endpoint corresponding to shortcut time $t$ satisfy the same lower screen. This ordinary time is $t+S_t(v)$, determined by the counted state. The ordinary first hit of $q\in D_t$ is $t+S_t(v)+\inf\{j\ge0:C^j(T^t(v))=q\}$. The ordinary tail from that endpoint and ordinary state at time $2t$ are determined as well. For the two original tracks the prefix shift on the ordinary clock is $N+R+m$. This construction includes ordinary intermediate visits to even targets.

For $t\ge t_0$, $F_t$ is a deterministic function of $F_{t_0}$ by advancing the endpoint and count and restricting the clock vector to $D_t\subseteq D_{t_0}$. Data processing therefore gives the bound at $t_0$ for every later $t$. In particular for $k=o(L)$ one can use $t_0=\lfloor L/2\rfloor$ and retain the same bound uniformly for all $t\ge t_0$. A fixed target's clock can be retained separately whenever it belonged to $D_{t_0}$.

### A.4. Relative counts and basin frequencies

The same bounds give a count with the rarity factor retained. For any $G$ with $0\le G\le1$ on the future data, uniformly in the test,
$$
\left|\sum_{v\in K\cap\mathbb Z}
       (f(2^m v)-P)\,G(F_t(v))\right|
\ll_{a,b}3^{-R}H\left(\sqrt{\frac{1+J}{t+1}}
 +\frac{M2^t}{H}+\frac{E}{3^{-R}H}+3^R\rho^J\right).
\tag{A.6}
$$
For the truncated event the selected and unselected expectations on complete blocks differ by the paired failure bound. Multiplying by $n|S|$ gives the bound for the corresponding test sums. Restoring the boundary blocks costs at most $2|S|+2M(|S|/M)$, replacing $f_J$ costs at most $E$, and replacing $|S|/M$ by $P$ costs $O(H\rho^J)$ by (A.2).

In particular take $t_0=\lfloor L/2\rfloor$. The right side of (A.6) is
$O_{a,b}(3^{-R}H\epsilon_{X,k})$ uniformly for $0\le k\le L/10000$, where
$$
\epsilon_{X,k}=\sqrt{\frac{1+k+\log_2 L}{L}}.
$$
In this range $J\le0.06L$ eventually, $M\le X^{0.096}$, $6^J\le X^{0.156}$ and $3^R2^m\ll X^{0.002122}$. In (A.4) the two power errors then decay at least as $X^{-0.0278}$ and $X^{-0.84}$, while $M2^{t_0}/H\ll_{a,b}X^{-0.404}$. The $\rho^J$ terms are $O(L^{-2})$ after relative normalization. The inequality $aX>8\cdot3^R$ also holds eventually in this range.

For a fixed target $q$ let $\mathcal P(q)=\{v\ge1:\tau_q(v)<\infty\}$ be its shortcut predecessor basin. Since $q\in D_{t_0}$ for large $X$, applying (A.6) to the indicator of a finite clock shows that the number $C_m(q)$ of selected lower starts with both tracks in $\mathcal P(q)$ satisfies
$$
C_m(q)=3^{-R}p\,\#(\mathcal P(q)\cap K)
+O_{a,b}(3^{-R}H\epsilon_{X,k}).
\tag{A.7}
$$
The total number selected has the same formula with $\#(K\cap\mathbb Z)$ in place of the basin count. The transfer also compares the exact first-hit laws after subtracting $W$, including the atom at infinity, since (A.6) applies to every set of clocks. If the two hit probabilities are $p_1,p_2>0$ and the joint total variation bound is $\varepsilon$, the conditional bound is at most $\varepsilon/\max(p_1,p_2)$. The unnormalized common mass on the hit event is at least $\max(p_1,p_2)-\varepsilon$.

David Leen's corollary *Every target* gives existence of the shortcut natural density $h_T(q)$ and the timed natural density in (A.8) below. It also identifies $h_T(q)$ with the ordinary predecessor density $h_C(q)$ except at $q\equiv4\bmod6$, where $h_T(q)=h_C(2q)$. The positivity for $3\nmid q$ is a separate predecessor result. Leen's positivity remark cites Mazur's all-target Lean development for $h_C(a)>0$ on units, with $h_T(q)\ge h_C(2q)$, and records that this result has no refereed proof. Paper 10/v3, Theorem 1, supplies an alternative fixed-target linear lower count using its averaged mixing input (J). For that input on the ordinary map, choose an odd unit shortcut ancestor of $q=2^i v$ with $v$ odd by taking $e\ge i+1$ and $2^e v\equiv4$ or $7\bmod9$. The odd unit $(2^e v-1)/3$ reaches $q$ under $T$, and ordinary and shortcut orbits agree on whether they hit an odd target. [Leen, *Brownian motion in Collatz orbits*, §1.3 and positivity remark, DOI 10.5281/zenodo.23252395](https://doi.org/10.5281/zenodo.23252395) · [Mazur, *Positive lower density of Collatz predecessors*](https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) · [Paper 10/v3, Theorem 1 and (J)](https://rstation.ai/problems/collatz/papers/10/v3)

The endpoints of $K$ are $aZ+\beta/2^m$ and $bZ+\beta/2^m$, with $0<\beta/2^m<8Z/X$ and $Z\ge X/2$. By differencing cumulative counts, the natural density gives
$\#(\mathcal P(q)\cap K)=h_T(q)H+o(H)$ uniformly along the stated windows. For $k=o(\log X)$, (A.7) yields, in each family and for each $m$,
$$
\frac{C_m(q)}{\# A}=h_T(q)+o(1),\qquad
C_m(q)=(h_T(q)+o(1))\,2^{-N-m}p(b-a)X .
$$
For $h_T(q)>0$ this is also the relative asymptotic $C_m(q)\sim3^{-R}p\,\#(\mathcal P(q)\cap K)\sim2^{-N-m}p\,\#(\mathcal P(q)\cap(aX,bX))$. The same positive-density input bounds the conditional exact-clock and tail comparison by $O_{a,b,q}(\epsilon_{X,k})$ at $t_0$, with later comparison by data processing. These frequencies and conditional laws concern starts sampled from the predecessor basin of the fixed target. Once a sampled orbit first reaches $q$, its subsequent path is the deterministic ray $(T^j(q))_{j\ge0}$. The scope includes any prescribed unit $q$ regardless of its forward behavior.

### A.5. Timed law in the protected windows

With natural logarithms, let $d=\log(4/3)$, $\mu=2/d$, $\sigma^2=2(\log 3)^2/d^3$, and let $\Phi$ be the standard normal CDF. Leen's shortcut timed law for each fixed target states that
$$
\operatorname{dens}\{v\in\mathcal P(q):\tau_q(v)\le
   \mu\log v+z\sigma\sqrt{\log v}\}=h_T(q)\Phi(z),
\qquad z\in\mathbb R .
\tag{A.8}
$$
Subtract the two cumulative counts at $bZ$ and $aZ$. Shifting to the actual endpoints of $K$ changes each count by $O(Z/X+1)=o(H)$. On $K$, $\log v=\log Z+O_{a,b}(1)$ uniformly. For every fixed $\eta>0$ and large $X$, the threshold $\mu\log Z+z\sigma\sqrt{\log Z}$ lies between the thresholds in (A.8) with parameters $z-\eta$ and $z+\eta$ at every $v\in K$. Continuity of $\Phi$ gives $h_T(q)\Phi(z)+o(1)$ for this finite-hit fraction of uniform starts in $K$. The density and threshold arguments are uniform in all the stated windows since $Z\ge X/2$.

For either original track $s=x,x+4$ the clock shift is $W$. For $k=o(\log X)$ and $3\nmid q$, the total variation comparison yields
$$
\begin{aligned}
\lambda_m&=N+m+\mu\log(gX/2^m),&
s_m&=\sigma\sqrt{\log(gX/2^m)},\\
\mathbb P\left(\frac{\tau_q(s)-\lambda_m}{s_m}\le z\ \middle|\
                    \tau_q(s)<\infty\right)&=\Phi(z)+o(1).
\end{aligned}
$$
The unconditioned finite CDF is $h_T(q)\Phi(z)+o(1)$, with mass $1-h_T(q)+o(1)$ at infinity. The conditional CDF convergence is uniform in $z$ by monotonicity and continuity of the limiting CDF. In particular the two windows' centers differ exactly by $(1-\mu\log 2)b_k$. Using $\log Z$ also keeps the clock shift at growing $k$ when its size is comparable to the Gaussian scale.

### A.6. Ranked arrivals in a prescribed basin

The translation argument from research note 107 gives a related absolute-error estimate for general rank-two events. Let $I=(aX,bX)$, $B_q(v)=\mathbf 1_{\mathcal P(q)}(v)$, and $t_0=\lfloor L/2\rfloor$. For each fixed integer shift $h\ge0$, both starts $v,v+h$ exceed $q2^{t_0}$ for large $X$ when $v\in I$. Their basin indicators agree whenever the counted states agree at $t_0$. The residue realization of (A.5) on consecutive $v$ gives
$$
\sum_{v\in I\cap\mathbb Z}|B_q(v+h)-B_q(v)|
\ll_{a,b} X\sqrt{\frac{1+\log(2+h)}{L}}+2^{t_0}.
$$
For a selector $G$ of period $M'$, with $0\le G\le1$, translate $\sum_I B_q(v)G(v)$ by $h$ and average over $0\le h<M'$. The interval endpoints cost $O(M')$, the above comparison bounds the change in $B_q$, and the average of $G(v+h)$ equals its residue mean $\overline G$. Hence the difference from $\overline G\,\#(\mathcal P(q)\cap I)$ is
$O_{a,b}(X\sqrt{(1+\log(2M'))/L}+2^{t_0}+M')$.

For an event on the first two ranked words and on $j=O(\log\log X)$ outgoing parity bits, take $J'=\lceil20\log_2 L\rceil$ and $M'=3^{J'}2^j$. The cutoff estimate (A.3) for the pairs costs $O_{a,b}(X/L)$ since $20\delta>1$. CRT gives the residue mean for the truncated ternary order and independent fair outgoing bits, and the Haar truncation costs $O(\rho^{J'})$. Thus the number of nonperiodic starts in $\mathcal P(q)\cap I$ satisfying the event is its full Haar and fair-bit probability times $\#(\mathcal P(q)\cap I)$, up to
$O_{a,b,q}(X\sqrt{(1+j+\log\log X)/L})$ uniformly in the event. The block comparison in (A.6) supplies the additional rarity factor for the particular protected tuple.

The offline replay checks the block coupling and boundary errors, the paired basin and clock counts, and the time shifts on both tracks. [Integer future, basin and first-hit fixtures](README.md#integer-future-basin-and-first-hit-fixtures) · [Previous public revision, r/collatz post 98, attachment revision 3](https://rstation.ai/api/v1/comments/TEYlAv-mCieTGW0k/attachment?revision=3)

## Appendix B. Outgoing parity after the meeting

### B.1. Exact deadline

Fix $0<a<b<\infty$. Use either family $B$ with $0\le k\le(\log_2 X)/710$, and write $N=34+20k$, $R=22+13k$ and $g=3^R/2^N$. Sample uniformly from $X_{B,k}\cap(aX,bX)$ with $2^m\mid Q_k(x)$. Take $m=0$ for the full sample and $m=b_k=\lceil\log_2g\rceil$ for the earliest-descent sample. By §7 the latter divisibility condition is equivalent to both tracks attaining their earliest first descents, uniformly for all sufficiently large $X$ in this range. Let
$$
u=2^{-m}Q_k(x),\qquad L=(b-a)X2^{-N-m},\qquad M=2^d,\quad d\in\mathbb Z_{\ge0}.
$$
Let $\nu_d$ be the law of the first $d$ shortcut parity bits starting at $u$, and let $U_d$ be the uniform law on the $M$ words.

**Theorem B.1.** Along every sequence in the stated range with $X\to\infty$,
$$
d_{\rm TV}(\nu_d,U_d)\to0
\quad\Longleftrightarrow\quad L/M\to\infty
\quad\Longleftrightarrow\quad \log_2 L-d\to+\infty.
\tag{B.1}
$$
If $L/M\to0$, the distance tends to one. For $L/M\le2$ the distance is at least $5/9-o(1)$, and for $L/M\le5$ it is at least $1/9-o(1)$. More generally, for any fixed $A>0$, put $n=\lceil A\rceil$ and $D_n=(6^{n+1}-1)/5$. When $L/M\le A$ and $aX>8$, the distance is at least
$$
\frac{\lfloor M/3^{D_n}\rfloor}{M}\ge 3^{-D_n}-\frac1M .
\tag{B.2}
$$
All these estimates are uniform in the family, the return count, the halving choice and the affine representative.

Let $A_1$ be the lower word's intercept, so $2^NQ_k(x)=3^R x+A_1$. By §2 the incoming words and the halvings prescribe the single class $3^R x+A_1\equiv0\pmod{2^{N+m}}$. For an integer representative $x_1$ and $u_1=(3^R x_1+A_1)/2^{N+m}$, write
$$
x=x_1+2^{N+m}s,\qquad u=u_1+3^R s.
\tag{B.3}
$$
The candidates form an interval of consecutive integers $s$ of size $L+O(1)$, cut out by an open real interval of length $L$. Replacing $x_1$ by another representative translates this indexing. Since $2^{N+m}\le 2\cdot 3^R\ll X^{(13\log_2 3)/710}$, $L\to\infty$ uniformly.

### B.2. Rank replacement and independence

Write $E=E_{B,k}$, $p_k=\pi(E)$ and let $P$ be the subset of the candidate indices selected by the physical ranks at $Q_k(x)$. By §§6–7, the symbolic rank selects the two words exactly on $E$, and the count of physical selections is $|P|=p_k L(1+O_{a,b}(X^{-1/6000}))$, with $p_k>0.12068$. The map $s\mapsto Q_k(x)$ is injective. Thus, with $Y\asymp_{a,b}gX$ above the target window, the absolute mismatch bound of §6 gives at most $O(Y^{1-\gamma})$ exceptional indices, including periodic targets. Since $Y^{1-\gamma}/L\ll_{a,b}2^m3^RY^{-\gamma}$, the first margin in (6) bounds this by $O_{a,b}(LX^{-1/6000})$. The comparison uses the ranks at the meeting for both samples.

For any tolerance $\epsilon>0$, take a common stop cutoff $J$ so the tail in (2) has mass less than $\epsilon/2$. The possible labels through $J$ form a finite list. Each $F_{j,v}$ in (1) is an open union of cylinders given by finite legal continuations of gain greater than $2^j$. For each retained label choose finitely many such cylinders so the total omitted mass, summed over the list, is less than $\epsilon/2$. Refine the chosen cylinders to a common depth $\ell$. Let $C_{B,k}$ be the complement of the chosen cylinders for labels occurring at $(B,k)$. Then $E\subset C_{B,k}$ and $\pi(C_{B,k}\setminus E)\le\epsilon$, with one finite $\ell$ for both families and all $k$. The same construction works for $E_{B,\infty}$ using the cofinite labels from §5.

Let $C$ be the set of candidate indices whose sources lie in $C_{B,k}$. The stride $2^{N+m}$ in (B.3) is a ternary unit, so $|C|=\pi(C_{B,k})L+O(3^\ell)$. All indices in $P\setminus C$ are rank mismatches. Using $|P\triangle C|=|C|-|P|+2|P\setminus C|$ gives
$$
|P\triangle C|\le \epsilon L+O_{a,b}(LX^{-1/6000}+3^\ell).
\tag{B.4}
$$
The total variation distance between the uniform laws on these index sets is at most $|P\triangle C|/|P|$, and passing to words can only reduce it.

The odd slope $3^R$ in (B.3) permutes the residues modulo $M$. By §2 each such residue of $u$ specifies a distinct length-$d$ parity word. In a complete block of $3^\ell M$ consecutive indices, every eligible ternary residue pairs equally often with every word by the Chinese remainder theorem. The incomplete block contains fewer than $3^\ell M$ indices. Dividing by the count of outer selections, which is bounded below by a fixed positive multiple of $L$ for fixed $\ell$ and large $X$, gives
$$
d_{\rm TV}(\nu_d,U_d)\ll_{a,b}\epsilon+X^{-1/6000}+3^\ell M/L.
\tag{B.5}
$$
Take the limit with $M/L\to0$ at fixed $\epsilon,\ell$, then let $\epsilon\downarrow0$. This proves sufficiency even for arbitrarily slow divergence of $\log_2 L-d$.

### B.3. Physical obstruction at bounded ratios

An integer source $x$ admitting a legal reverse path at either $x$ or $x+4$ of forward gain at least $3/2$ has a positive ancestor at most $2(x+4)/3<x$ for $x>8$. This follows from the nonnegative forward intercept and the positivity of the exact even and odd inverses. Following that ancestor through the corresponding prescribed path reaches the original meeting and excludes the proposed ranked pair.

We construct a cylinder with this property at all of $n$ successive translates. Start with any ball $z\equiv c\pmod{3^j}$ of depth $j\ge1$ and any shift $h\in\mathbb Z_3$. Choose $e_0\in\{0,4\}$ so that $y=z+h+e_0$ is a unit throughout the ball, and write $y=y_0+3^j t$ for an integer unit representative $y_0$ and $t\in\mathbb Z_3$. At any unit $v$, one of $e=1,2,3,4$ gives $2^e v\equiv4$ or $7\pmod9$. For the residues $v=1,2,4,5,7,8\pmod9$ the first choices are $2,1,2,3,4,1$, respectively. Applying $e-1$ even inverses and one odd inverse then gives the unit $(2^e v-1)/3$.

Choose $j$ such gaps on the trajectory of $y_0$. After $i$ gaps the lift differs from the representative endpoint by $2^{E_i}3^{j-i}t$, where $E_i$ is the sum of the first $i$ gaps. Before each odd inverse the difference is still divisible by three, so the word is legal throughout the ball. The final endpoint is $v_0+2^{E_j}t$ for some integer $v_0$, and ranges over $\mathbb Z_3$. This prefix has gain at least $(3/16)^j$. Restrict $t$ modulo $3^{5j+1}$ so the endpoint is congruent to $-1$ modulo $3^{5j+1}$. The identity $O(v)+1=(2/3)(v+1)$ gives $5j+1$ legal successive odd inverses on the refined ball. Its depth is $6j+1$ and the gain is at least
$$
(3/16)^j(3/2)^{5j+1}=(3/2)(729/512)^j\ge3/2.
$$
The chosen representative supplies the unit endpoints used to choose the gaps. On every other lift the divisibility argument supplies legality.

Starting at depth one, refine in turn with $h=i\beta$ for $0\le i<n$. Earlier witnesses remain valid under further refinement. This gives a single ball of depth $D_n$ since $D_0=1$ and $D_{i+1}=6D_i+1$. For integer $\beta$, every integer lift in the ball has a physical exclusion at each translate $z+i\beta>8$, using either that lower source or its partner.

Start at the first candidate index $s_0$ and use the $M$ consecutive representatives $s_0,\ldots,s_0+M-1$ for the words. Every visit of a word in the window occurs at its representative plus a nonnegative multiple of $M$, so successive lower sources differ by $\beta=2^{N+m}M$. An open interval of length $L/M$ contains at most $\lceil L/M\rceil$ integers, hence at most $n$ visits per word when $L/M\le A$. Among the $M$ representatives at least $\lfloor M/3^{D_n}\rfloor$ have lower source in the refined ball since their stride $2^{N+m}$ is a ternary unit. Each of these words is absent from the physical sample. Its fair mass contributes to (B.2). If $L/M$ stays bounded then $M\to\infty$, so (B.2) gives a positive uniform lower limit. Failure of $L/M\to\infty$ supplies a bounded subsequence, proving necessity.

The support size of $\nu_d$ is at most $|P|$, which gives distance tending to one when $L/M\to0$. For the stronger short-ratio bounds, an immediate odd inverse at a source congruent to $2\pmod3$ has gain $3/2$. Applying this at $z$ and at $z+4$ removes $z\equiv2,1\pmod3$, respectively, from $E$. For $z\equiv0\pmod9$, the even inverse at $z+4$ gives $2(z+4)\equiv-1\pmod9$. Two odd inverses are then legal, giving gain $9/8$. Each strict improvement extends a prescribed word and increases its gain, so $E\subset\{3,6\bmod9\}$ and $p_k\le2/9$. The support bound $1-|P|/M$ is therefore at least $5/9-o(1)$ for $L/M\le2$.

These short witnesses are physical for $x>32$, since even the gain $9/8$ gives a positive ancestor at most $8(x+4)/9<x$. For $L/M\le5$, choose the first-representative source class $z\equiv-2\beta\pmod9$. As $\beta$ is a ternary unit, the only one of its five possible visits $z+i\beta$, $0\le i<5$, divisible by three is the middle one, which is divisible by nine. All five residues are thus excluded by the short witnesses. At least $\lfloor M/9\rfloor$ words are missing for $aX>32$, proving the stated $1/9-o(1)$ bound.

### B.4. Subsequential profile on ternary rotations

Suppose along a subsequence $B$ is fixed, $L/M\to\rho\in(0,\infty)$, and $k$ is eventually $k_*$ or tends to infinity, denoted by $k_*=\infty$. Suppose also that $\beta=2^{N+m}M$ converges to $\beta_*$ in $\mathbb Z_3$. Let $f=\mathbf1_{E_{B,k_*}}$ with $E_{B,\infty}$ as in §5, and let $p=\int f\,d\pi$. Define the visit sums on the rotation $z\mapsto z+\beta_*$ by $H_0=0$ and
$$
H_j(z)=\sum_{i=0}^{j-1} f(z+i\beta_*)\qquad(j\ge1).
$$
For $\rho=t+\theta$ with $t=\lfloor\rho\rfloor$ and $0\le\theta<1$, the distance has limit
$$
\lim d_{\rm TV}(\nu_d,U_d)=
\frac{(1-\theta)\|H_t-\rho p\|_{L^1(\pi)}
      +\theta\|H_{t+1}-\rho p\|_{L^1(\pi)}}{2\rho p}.
\tag{B.6}
$$
This describes all positive finite ratio subsequential limits after extraction with these parameters, since the family set is finite, the return counts have constant or diverging subsequences, and the ternary units are compact.

To prove (B.6), use the outer approximation of §B.2 at fixed tolerance $\epsilon$. For $k_*=\infty$, incidence of the finitely many retained labels stabilizes by §5, so the same cylinder union works for all sufficiently large $k$ on the subsequence and for the limit set. Write $f_\epsilon$ for its indicator and $p_\epsilon=\int f_\epsilon\,d\pi$. At its depth $\ell$, the residues of $\beta$ and $\beta_*$ eventually agree. By (B.4), replacing the physical sample by the cylinder sample changes its distance to $U_d$ by $O_{a,b}(\epsilon+X^{-1/6000}+3^\ell/L)$.

Write the integer candidate count as $K=L+O(1)=jM+r$, $0\le r<M$. The first $r$ representatives have $j+1$ visits and the rest have $j$ visits. For the cylinder sample the counts per word are the corresponding sums of $f_\epsilon$ along the rotation. The mean count per word is $|C|/M\to\rho p_\epsilon$. The distance to uniform is the sum of the absolute deviations of the counts from this mean, divided by twice $|C|$. On each block of representatives the stride is a ternary unit, giving an error of at most one in the count of each residue modulo $3^\ell$. Thus the block averages, weighted by their lengths divided by $M$, give the Haar integrals of the absolute deviations. For noninteger $\rho$, the two proportions tend to $\theta$ and $1-\theta$. For integer $\rho$, the proportion with exactly $\rho$ visits tends to one from either side. This proves (B.6) for the cylinder sums and mass. By Haar invariance the $L^1(\pi)$ difference of a $j$-visit sum for $f_\epsilon$ and one for $f$ is at most $j\epsilon$. Also $|p_\epsilon-p|\le\epsilon$ and $p\ge0.12068$. Sending $\epsilon\downarrow0$ proves (B.6) for the physical sample.

The two finite parity replays exercise the affine window arithmetic, CRT histograms, short support obstructions and positive-ancestor witnesses. [Outgoing parity fixtures](README.md#outgoing-parity-fixtures)

## Appendix C. Detecting a prescribed meeting from one later integer

The constructions and the first two appendices come from the immutable supplement under r/collatz post 98. [Public revision 4](https://rstation.ai/api/v1/comments/TEYlAv-mCieTGW0k/attachment?revision=4)

### C.1. State separation and optimal detection

Use either protected family in a fixed source window $(aX,bX)$, $0<a<b$, with either choice of $m$ from §A.1. Write $I=K$ for its outgoing interval and $H=|I|$ for its length. The selected start $u$ is uniform on the image of the selected lower starts under $2^{-m}Q_k$, and $U$ is uniform on all positive integers in $I$. Let $P_Y$ and $Q_Y$ be the laws of $Y=T^t(u)$ and $T^t(U)$, respectively. The elapsed shortcut time $t$ is known and the integer $Y$ alone is observed.

All logarithms in this appendix are in base two. Set $R=22+13k$, $\lambda=\log_2 3$, $\delta=1-\lambda/2$ and $t_*=R\lambda/\delta$. Suppose $k\to\infty$ and $k\le(\log_2 X)/710$.

**Theorem C.1.** If $(t_*-t)/\sqrt{t_*}\to+\infty$, then $d_{\rm TV}(P_Y,Q_Y)\to1$. At any integer clock $t=t_*+z\sqrt{t_*}+o(\sqrt{t_*})$ for fixed $z\in\mathbb R$,
$$
\liminf d_{\rm TV}(P_Y,Q_Y)\ge \Phi(-2\delta z/\lambda),\qquad
\frac{1}{\sqrt{t_*}}\log\frac{P_Y(Y)}{Q_Y(Y)}
\ \Longrightarrow\ V_z=(\lambda Z/2-\delta z)_+
\quad\text{under }P_Y ,
\tag{C.1}
$$
where $Z$ is standard normal and $\Phi$ is its distribution function. The first moments converge as well. In particular at $z=0$ the relative entropy is asymptotic to $\lambda\sqrt{t_*}/(2\sqrt{2\pi})$ bits.

Let $\mathcal P_t(a_t)$ be the greatest detection probability $P_Y(A)$ among state events $A$ with false-alarm probability $Q_Y(A)\le 2^{-a_t}$. At the same critical clocks,
$$
\mathcal P_t(a_t)\longrightarrow
\begin{cases}
\Phi(-2(\delta z+b)/\lambda), & a_t/\sqrt{t_*}\to b>0,\\
\Phi(-2\delta z/\lambda), & \log(t+2)\ll a_t\ll\sqrt{t_*},
\end{cases}
\tag{C.2}
$$
where each $\ll$ in the second line means the ratio of left to right tends to zero. The limits also hold for randomized tests. At $z=0$, for example, the best power at false alarm $2^{-t^{1/4}}$ tends to $1/2$. The fixed-size power curve and the full state total variation profile remain open. Appendix A gives $d_{\rm TV}(P_Y,Q_Y)\to0$ for $t\to\infty$ with $k=o(t)$ and $k=o(\log_2 X)$. Apply (A.1) directly up to $\lfloor(\log_2 X)/2\rfloor$ and use data processing from that clock for later times.

### C.2. Numerator counts and the short-clock support

Write $n=2^t$. For a word $w=(w_0,\ldots,w_{t-1})$ of grade $h=\sum_i w_i$, the affine formula is
$$
nT^t(v)=3^h v+A_w,\qquad A_w=\sum_{i:w_i=1}2^i3^{\sum_{j>i} w_j}.
\tag{C.3}
$$
By §2 each word has one source class modulo $n$, given by $-3^{-h}A_w\bmod n$. Indeed integrality at the end gives this congruence, and the word already has a realized source in it. At fixed $h$ the $A_w$ are therefore distinct modulo $n$. Also $0\le A_w/3^h<n$ by summing the geometric powers of two in (C.3). Under fair words, appending an independent bit $b$ updates the normalized numerator $A_w/2^j$ at length $j$ by a multiplier $(1+2b)/2$ and an addition $b/2$. Thus $\mathbb E_{\rm fair}(A_w/n)=t/4$.

For any nonnegative integer depth $d=d(h)$ let $C_d(w)$ count the words in the same grade and numerator class modulo $3^d$ as $w$. Set $s_h=\max(1,n/3^d)$. Per grade, the fair probability of cells of size below $s_h2^{-u}$ is at most $2^{-u}$ for $u\ge0$, since there are at most $3^d$ cells when $s_h>1$ and no occupied cell below this size otherwise. For the other tail, at most $1+B n/3^d$ distinct numerators in a cell satisfy $A_w\le Bn$. For $u\ge2$ and $B=2^{u-2}$, any cell of size above $s_h2^u$ has more than half its words above $Bn$. The total mass of such cells is at most $2\Pr_{\rm fair}(A_w>Bn)\le 2t\,2^{-u}$. Integration of these tail bounds gives, uniformly in $d(h)$,
$$
\mathbb E_{\rm fair}|\log C_d(w)-(t-\lambda d)_+|\ll\log(t+2).
\tag{C.4}
$$

For the support claim use $S_t=\{T^t(v):v\text{ selected}\}$, of size at most $H3^{-R}+1$ by (B.3). On the reference sample the word law is within $O(n/H)$ in total variation of fair words, by complete binary periods. For unbounded $t$, discard words with $A_w>(t+1)^2n$, of mass $o(1)$ by the first moment. On the remaining words of grade $h$, each output integer has at most $1+(t+1)^2n/3^h$ preimages, by residue counting in (C.3). On the event $D_t=\{\lambda h\ge t-\lambda R+6\log(t+1)\}$ their number per grade and state is at most $1+3^R/(t+1)^4$. The total reference mass of these inputs reaching $S_t$ is bounded by
$$
\frac{(H3^{-R}+1)(t+1)}{|I\cap\mathbb Z|}
\left(1+\frac{3^R}{(t+1)^4}\right)=o(1)
$$
for $t=O(R)$, since $H\gg_{a,b} X$, $3^R/H=o(1)$ and $R\to\infty$. At the early and critical clocks of Theorem C.1, §C.4 also gives $n/H=o(1)$. Consequently $1-Q_Y(S_t)\ge\Pr_Q(D_t)-o(1)$. Under fair bits the grade is binomial $(t,1/2)$, with standardized threshold in $D_t$ equal to
$$
\frac{2(\delta t-\lambda R)}{\lambda\sqrt t}
  +O\!\left(\frac{\log(t+1)}{\sqrt t}\right).
$$
This tends to $2\delta z/\lambda$ at the critical clocks and to $-\infty$ in the stated earlier range when $t\to\infty$. The binomial central limit theorem gives both bounds. For bounded $t$, use $Q_Y(S_t)\le n(H3^{-R}+1)/|I\cap\mathbb Z|$, since each word gives at most one preimage of a state. This proves the early separation across both regimes.

### C.3. A state likelihood estimate in proportional intervals

Let $I$ be any interval of length $H$ with positive endpoints comparable to $H$ by fixed constants and suppose $2^t3^R/H=o(1)$. Let $Q$ be uniform on $I\cap\mathbb Z$, $P_0$ uniform on its class $q\bmod3^R$, and $P=P_0(\cdot\mid S)$ for a subset of mass $P_0(S)\ge c>0$. For the grade $h$ of the sampled start under $P$, set
$$
F(h)=\min\{\lambda R,[\lambda(R+h)-t]_+\}.
$$
Uniformly in $q$ and $S$, with constants depending on $c$ and the interval ratios,
$$
\mathbb E_P\left|\log\frac{P_Y(Y)}{Q_Y(Y)}-F(h)\right|
\ll \log(t+2)+(t+1)\frac{2^t+3^R}{H}.
\tag{C.5}
$$

To prove this, first use $P_0$ on the joint output $(h,Y)$. Given $Y=y$, a word $w'$ of grade $h$ gives an integral inverse source precisely when $A_{w'}\equiv ny\bmod3^h$, and a source in the progression precisely when $A_{w'}\equiv ny-3^h q\bmod3^{h+R}$. An integral inverse in $I$ has the unique binary source residue of $w'$ by (C.3), so it realizes that word. At a sampled progression start both congruences can be centered on $A_w$. All same-grade inverse sources differ by less than $n$, so at starts more than $n$ from the endpoints the two counts are exactly $C_h(w)$ and $C_{h+R}(w)$. The sample sizes have ratio $3^R(1+O(3^R/H))$. The progression stride is odd, hence each word has probability $n^{-1}(1+O(n3^R/H))$ by counting complete periods along the progression. On interior starts, (C.4) thus gives the approximation to the graded log likelihood, using the identity
$$
\lambda R+(t-\lambda(h+R))_+-(t-\lambda h)_+=F(h).
$$
The edge strip has $P_0$-mass $O((n+3^R)/H)$. There the two actual counts are between $1$ and $n$, and $0\le\lambda R-F(h)\le t$, so its contribution is $O((t+1)(n+3^R)/H)$.

To remove the grade, note that $ny/3^h=v+A_w/3^h$ lies between the lower endpoint of $I$ and its upper endpoint plus $n$. Since the lower endpoint is comparable to $H$ and $n=o(H)$, all grades at a given state have span at most a fixed integer $C$. For the sampled grade, put $a=ny\bmod 3^h$ and let $c_h(a)$ be the number of grade-$h$ words with numerator $a\bmod 3^h$. For any grade $j$ with $|j-h|\le C$, the number of its sources at $y$ is bounded by $b_{h,j}(a)$, the number of grade-$j$ words with numerator congruent to $a$ modulo $3^{\min(h,j)}$. Summing $b_{h,j}$ over $a\bmod 3^h$ gives $3^{(h-j)_+}\binom tj$.

In the interior the reciprocal $1/Q(h\mid y)$ is bounded by $\sum_{|j-h|\le C} b_{h,j}(a)/c_h(a)$ because the own-grade count is exact there. Under fair words the cell $(h,a)$ has mass $c_h(a)/n$. This cancels the denominator, giving a fair expectation of the ratio over occupied cells of at most
$$
n^{-1}3^C\sum_h\sum_{|j-h|\le C}\binom tj\le (2C+1)3^C.
$$
The multiplicative word estimate transfers this upper bound, up to a bounded factor, to $P_0$ on the interior. Jensen's inequality applied to the reciprocal extended by $1$ on the edge strip bounds the interior mean of $-\log Q(h\mid Y)$ by $O(1)$. On the strip that log is at most $t$, by the one-preimage-per-word bound. The mean of $-\log P_0(h\mid Y)$ is conditional entropy, at most $\log(C+1)$. The state log likelihood under $P_0$ equals the joint one plus $\log Q(h\mid Y)-\log P_0(h\mid Y)$. These two mean bounds control the absolute cost of the correction.

Finally $P\le c^{-1}P_0$ on starts, so the mean absolute approximation error under $P_0$ controls the same error under $P$ with factor $c^{-1}$. Replacing $P_{0,Y}$ by $P_Y$ adds $\log(P_Y/P_{0,Y})$. Its positive part is bounded by $\log(1/c)$, and its negative tail below $-s$ has $P_Y$-probability at most $2^{-s}$. This gives (C.5) for the actual state likelihood.

### C.4. The critical-window test

In the protected model, the endpoints of $I$ are comparable to $H$ by §A.1, and (B.3) identifies the progression in (C.5). Section B.2 gives a fixed positive lower bound on its selected fraction by the window counts of §7. At critical clocks, $N+m\le R\lambda+1$ and $t=t_*+O_z(\sqrt{k}+1)$. Hence
$$
N+m+t\le121k+O_z(\sqrt{k}+1),\qquad 13\lambda(1+1/\delta)<121 .
$$
The same upper bound with $z=0$ applies for $t\le t_*$. Since $H=(b-a)X3^R/2^{N+m}$, the cost $2^t3^R/H=2^{N+m+t}/((b-a)X)$ decays at a power rate uniformly in the stated range. In particular the boundary error in (C.5) tends to zero. Theorem B.1 gives asymptotically fair outgoing words and thus $(2h-t)/\sqrt t\Rightarrow Z$ under $P$. The same normalized grades have bounded second moment by $c^{-1}$ domination, the multiplicative word estimate for $P_0$, and the fair binomial second moment. The cap $\lambda R/\sqrt{t_*}$ diverges and
$$
\frac{\lambda(R+h)-t}{\sqrt{t_*}}
=\frac{\lambda}{2}\frac{2h-t}{\sqrt t}\sqrt{\frac{t}{t_*}}
-\delta\frac{t-t_*}{\sqrt{t_*}} .
$$
The scaled $F(h)$ therefore converges to $V_z$ in law and in first moment by uniform integrability. The normalized error in (C.5) tends to zero in $L^1(P)$, proving the log likelihood limit and the entropy assertion.

Write $\ell(y)=\log(P_Y(y)/Q_Y(y))$ on the selected support and $\ell=-\infty$ elsewhere on the reference support. The state threshold $\ell\ge a_t$ has false alarm at most $2^{-a_t}$. For any test with that false alarm, splitting at $a_t-s$ bounds its power by $P_Y(\ell\ge a_t-s)+2^{-s}$ for $s>0$. This applies to test functions with values in $[0,1]$ as well as events. If $a_t/\sqrt{t_*}\to b>0$, take $s\to\infty$ with $s=o(\sqrt{t_*})$ and use continuity at $b$. In the second regime of (C.2), take $s=a_t/2$. Equation (C.5) gives $|\ell-F(h)|=o_P(a_t)$. The two likelihood thresholds can then be squeezed by positive constant multiples of $a_t$ for $F(h)$, with probability error $o(1)$. Each such threshold is below the cap and is equivalent to the same threshold for the *untruncated* score $\lambda(R+h)-t$. Its standardized threshold tends to zero and the corresponding Gaussian is continuous there. The limiting likelihood itself has a zero atom of mass $\Phi(2\delta z/\lambda)$, so its weak limit alone cannot justify this squeeze. At a fixed false-alarm probability the behavior of the unscaled likelihood within that atom can still affect optimal power.

The finite checks exercise the support witness, full preimage counts, numerator precision and likelihoods when different grades lead to one integer. [State detection fixtures](README.md#state-detection-fixtures)

## Appendix D. First same-time collision between selected pairs

### D.1. The collision clock and the list identity

Use either fixed family $B$ in the source window $(aX,bX)$ with $0<a<b<\infty$ fixed. Take $m=0$ or $m=b_k$ as in §A.1, and let $S$ be the set of outgoing values $v=2^{-m}Q_k(x)$ of all selected lower starts $x$. This is a bijection in increasing order. The original pairs are disjoint since their lower starts differ by at least $2^N>4$, and both members of every pair reach its outgoing value at shortcut time $N+m$.

Sample $v$ uniformly from $S$. For an integer budget $L\ge1$, define
$$
\tau_L(v)=\inf\{t\in\mathbb Z_{\ge0}:\ \#\{v'\in S:\ v'<v,\ T^t(v')=T^t(v)\}\ge L\}.
$$
Thus the clock counts $L$ distinct smaller selected gap-four pairs, once per pair. The clock can be infinite, and ties among first equality times are allowed. Distinct pairs cannot have equal values at the same shortcut time before $N+m$, since that would identify their outgoing states by determinism. For a finite $\tau_L$, the first such equality with at least $L$ smaller pairs on the original shortcut clocks is at $N+m+\tau_L$.

Write $n_t(y)=\#\{v'\in S:T^t(v')=y\}$. Given $Y=T^t(v)$, an observer who knows $S$ and $t$ and can return up to $L$ sources has optimal success
$$
D_L(t)=\frac{1}{|S|}\sum_y\min\{L,n_t(y)\}=\Pr(\tau_L>t).
\tag{D.1}
$$
Each guessed member contributes $1/|S|$ to success, so the $L$ smallest members of each fibre, or the whole fibre when smaller, attain the first expression. Once a source shares the same value with another source at the same time, the equality persists. The number of distinct smaller partners is therefore nondecreasing, and precisely those initial fibre ranks at most $L$ survive through $t$. The $L$ largest members give the same identity with larger partners throughout. For a first collision with *any* other pair, survival through $t$ is the singleton probability $\Pr(n_t(T^t(v))=1)$.

Put $\lambda=\log_2 3$, $\delta=1-\lambda/2$, and $R=22+13k$. Define
$$
W=\frac{(b-a)X}{2^{N+m}},\qquad t_0=\frac{R\lambda+\log_2 L}{\delta}.
$$

**Theorem D.1.** Let $X\to\infty$ with $0\le k\le(\log_2 X)/710$. The integer $L$ can depend on $X$ but is fixed across the elapsed clocks of each population. Assume
$$
t_0\to\infty,\qquad \frac{\log_2 W-t_0}{\sqrt{t_0}}\to+\infty.
\tag{D.2}
$$
Then
$$
\frac{\tau_L-t_0}{(\lambda/(2\delta))\sqrt{t_0}}\ \Longrightarrow\ \mathcal N(0,1)
\tag{D.3}
$$
for either halving choice when $b/a\le3$, and for the unthinned population when $b/a>3$. For the thinned population at any fixed ratio $b/a>3$, (D.3) holds when $L\ge C$ eventually, where one can take any fixed integer $C$ with $3^C>b/a$. In particular this includes every diverging budget subject to (D.2). Each result also holds for the first collision with $L$ larger selected pairs. At $L=1$ in the regimes covered by the theorem, (D.3) holds for the first collision with any other selected pair, and $D_1(t)$ gives the optimal probability of recovering the original pair from the integer alone.

For fixed $L$ and $k\to\infty$, (D.2) follows from $N+m+t_0\le121k+O_L(1)$ by the coefficient bound in §C.4. In particular with $L=1$ any median of the collision clock in the stated regimes is $t_*+o(\sqrt{t_*})$, where $t_*=R\lambda/\delta$.

### D.2. Grades, window counts and large lists

Let $M=3^R$ and $I=(\alpha,\beta)=2^{-m}Q_k((aX,bX))$. By (B.3), $S$ lies in a progression of stride $M$ and $I$ has length $H=MW$. Both endpoints are comparable to $H$, and $\beta/\alpha\le b/a$ because the affine intercept is positive. The count in §7 gives $|S|\ge cW$ for a fixed $c>0$ for all sufficiently large $X$. At the clocks
$$
t=\left\lfloor t_0+z\frac{\lambda}{2\delta}\sqrt{t_0}\right\rfloor,\qquad z\in\mathbb R\text{ fixed},
$$
condition (D.2) gives $2^t/W\to0$. Theorem B.1 gives an $o(1)$ total variation error from fair words, so the actual grade $h=S_t(v)$ is within $o(1)$ of the binomial $(t,1/2)$ law in total variation.

For the affine numerator from (C.3), call a source typical at clock $t$ if $A_w/2^t\le(t+2)^3$. Each word under the uniform progression law has probability $2^{-t}(1+O(2^t/W))$ by counting one binary residue per word along the odd progression. The selected law is dominated by a bounded multiple of that law since $|S|\ge cW$. The fair mean $t/4$ of $A_w/2^t$ thus bounds the selected atypical mass by $O_c((t+2)^{-2})$.

For a given output $y$, the feasible grades $h$ satisfy
$$
\frac{2^t y}{3^h}\in(\alpha,\beta+2^t)
$$
by $0\le A_w/3^h<2^t$. For any fixed $C$ with $3^C>b/a$, eventually $\beta+2^t<3^C\alpha$. Thus at most $C$ grades are feasible and their span is at most $C-1$. Define
$$
d_L(h)=\log_2 L+\lambda(R+h)-t,\qquad s=3\log_2(t+2).
$$
Given a feasible grade $h$ and a budget $\ell$, guess the $\ell$ largest progression points at or below $2^t y/3^h$. This includes the true source exactly when $A_w<\ell 3^h M$ for the unbounded progression, since each step above $v$ adds $M$. Intersecting the list with the selected fibre retains any success. If $L\ge C$, choose $\ell=\lfloor L/C\rfloor\ge L/(2C)$ for each feasible grade. A typical source with $d_L(h)>s+\log_2(2C)$ then lies on the combined list of at most $L$ guesses. This yields the required lower bound for $D_L(t)$ in wider windows when $L\ge C$.

For any $L$, the endpoints of grade $h$ lie in an interval of length $3^h(H+2^t)/2^t$, with at most $1+3^h(H+2^t)/2^t$ integers. An arbitrary list can succeed on at most $L$ sources of that grade at each endpoint, even if other grades reach it. Summing the grade bounds and dividing by $|S|$ shows that the contribution to success from grades with $d_L(h)<-s$ is at most
$$
O_c\!\left((t+1)L/W+(t+1)(1+2^t/H)2^{-s}\right)=o(1).
\tag{D.4}
$$
Here $L\le 2^{\delta t_0}$ and $\log_2 W\ge t_0$ eventually. Thus $D_L(t)\le\Pr(d_L(h)\ge-s)+o(1)$, and at $L=1$ this also bounds singleton survival from above.

### D.3. Windows of ratio at most three

If $b/a<3$, then $\beta+2^t<3\alpha$ eventually, so $y$ identifies the grade. Use the list rule with $\ell=L$. For $b/a=3$, trim strips of width $2^t+1$ from both ends of $I$. The retained interval satisfies the same strict grade separation because $\beta\le3\alpha$. Progression spacing and $|S|\ge cW$ bound the discarded mass by $O_c((2^t+M)/H)=o(1)$. Use the retained bands to determine the grade and the same decoder on their fibres. On retained typical sources with $d_L(h)>s$, this rule succeeds, so its success on the full sample is at least $\Pr(d_L(h)>s)-o(1)$.

For $L=1$, apply the same one-guess rule on the retained sample, or the full sample if no trimming was needed. Each fibre there has a single grade, so the event $d_1(h)>s$ is constant on each fibre. A nonsingleton fibre has conditional failure probability at least $1/2$ under the uniform source law. The high-grade mass of nonsingleton retained fibres is therefore $o(1)$ by the decoder bound. Each discarded source can spoil at most one retained singleton, namely the one at its endpoint, if present. Together with the discarded mass, this gives the lower bound $\Pr(d_1(h)>s)-o(1)$ for the singleton probability in the full sample.

### D.4. Signed spacing for unthinned wider windows

Write $D=545747$, $F=D2^{26}$ and $p=-B/D$. The two loops fix $p$ and $p+4$ and the tails end at the common signed value $Q_*$. By §2 the unthinned value is
$$
v=Q_*+\frac{M}{2^N}(x-p),\qquad FQ_*\in\mathbb Z.
$$
Both parameters have $B\equiv1\pmod3$ and $D\equiv2\pmod3$, so $p\equiv1\pmod3$. Actual protection gives the exact source digit $x\equiv0\pmod3$ once $x>7$. If $x\equiv2\pmod3$, the positive odd predecessor $(2x-1)/3$ of $x$ would be smaller than $x$ and would reach the prescribed meeting. If $x\equiv1\pmod3$, the positive odd predecessor $(2x+7)/3$ of $x+4$ would likewise be smaller than $x$ and would reach the meeting. Both cases contradict the defining protection in §1. Hence the $3$-adic valuation of $v-Q_*$ is exactly $R$.

For two selected unthinned values $v,v'$ and $1\le j<C$, the integer
$$
F(v-3^jv')-(1-3^j)FQ_*=\frac{FM}{2^N}\big((x-p)-3^j(x'-p)\big)
$$
has exact $3$-adic valuation $R$, since the parentheses and $F/2^N$ are ternary units. Its absolute value is at least $M$. Consequently, for sufficiently large $R$ and uniformly over $1\le j<C$,
$$
|v-3^jv'|\ \ge\ \frac{M-|1-3^j|\,|FQ_*|}{F}\ \ge\ \frac{M}{2F}.
\tag{D.5}
$$
At equal grade, distinct progression members have ordinary spacing at least $M$.

Suppose the spacing for distinct sources of grades $h,h+j$ is at least $M2^{-e}/(2F)$ for some $e\ge0$, in the sense of (D.5) for $j>0$ and the ordinary progression spacing for $j=0$. In the unthinned case we have proved this with $e=0$. If two typical sources $v,v'$ with grades $h,h+j$ reach the same integer at time $t$, then
$$
|v-3^jv'|\le 2(t+2)^3\,2^t3^{-h}.
$$
Put $K_0=(C-1)\lambda+\log_2(4F)$. If either grade has $d_1>s+K_0+e$, then the lower grade $h$ has $d_1(h)>s+\log_2(4F)+e$ and the last upper bound is strictly below $M2^{-e}/(2F)$. This excludes every distinct typical partner. Each high typical source therefore occupies its own endpoint among typical sources. If its endpoint also contains an atypical partner, charge the high typical source to one such partner. These charges are injective because the high typical sources have distinct endpoints. The high-grade nonsingleton mass is at most twice the atypical mass, including high sources that are themselves atypical. For $L<C$, the condition $d_L(h)>s+K_0+e+\log_2 C$ implies $d_1(h)>s+K_0+e$. Thus the probability above the latter list cutoff for $d_L$ gives a lower bound for $D_L(t)$ up to $o(1)$, since singleton survival is at most $D_L(t)$. At $L=1$ we also have the lower bound for singleton mass itself. For the unthinned small-list case, $t_0\to\infty$ forces $R\to\infty$, as required in (D.5).

### D.5. Gaussian limits and scope

At the selected clocks and under the selected law,
$$
d_L(h)=\lambda(h-t/2)-\delta(t-t_0),\qquad
\frac{d_L(h)}{(\lambda/2)\sqrt{t_0}}\ \Longrightarrow\ Z-z,\qquad Z\sim\mathcal N(0,1).
$$
This uses the fair binomial limit and $t/t_0\to1$. Since $s+O(1)=o(\sqrt{t_0})$, the upper and lower bounds have the same limit $\Phi(-z)$, including when $L$ moves between the bounded and split-list cases for the unthinned population. Thus (D.1) gives (D.3), and the singleton bounds give the law for the first collision with any other pair when $L=1$. Continuity and strict increase of the limiting Gaussian distribution give the median statement.

The convergence is for a uniformly sampled pair in the specified population. The first $\min(L,|S|)$ lower starts have $\tau_L=\infty$, and the last $\min(L,|S|)$ have infinite clock for larger partners. The Gaussian law makes the fraction of infinite clocks tend to zero by first bounding it by the late survival probability for fixed $z$ and then sending $z\to+\infty$. Individual eventual collisions and a deadline covering every pair are outside this conclusion. The integer observation counts synchronized shortcut steps. Different outgoing grades can give different ordinary elapsed times, and the theorem gives no law for unequal-clock visits.

For general progression residues a wide-window singleton or exact-recovery law of this form can fail even with fair outgoing parity. Take the full class $q=(M-1)/2\bmod M$ in $(aU,bU)$ with $b>3a$. Each odd $v$ in the class with $3v+1<bU$ has the even partner $3v+1$ in the same class and window, with the same next state. These pairs are disjoint and number $(b/3-a)U/(2M)+O(1)$, so they cost at least that many exact recoveries for every $t\ge1$. With $U=2^{20R}$, binary residues along the progression are asymptotically fair at the singleton critical clock, but the recovery probability is bounded above by $1-(b/3-a)/(2(b-a))+o(1)$. For sufficiently negative fixed $z$, this is strictly below the Gaussian survival $\Phi(-z)$.

### D.6. Wide thinned windows on a density-one set of return counts

**Theorem D.2.** Under (D.2), the Gaussian law (D.3) and its larger-partner and singleton versions extend to every fixed ratio after the terminal halvings, provided that indices with $L<C$ avoid an exceptional set. For a fixed ratio the set contains $O_{a,b}(\sqrt K\log(K+2))$ indices up to $K$. A common exceptional set for both families and all fixed ratios contains $O(\sqrt K\log^2(K+2))$ indices up to $K$ and suffices for each fixed ratio once $k$ is large enough.

Write $M_k=3^{22+13k}$, $m_k=b_k$, $\eta=13\lambda-20>0$, $\gamma=13\lambda+\eta$ and $e_k=\sqrt{k}/\log_2(k+2)$. For a fixed family put $A_*=FQ_*$, and for a positive grade gap $j$ put $K_j=(1-3^j)A_*$. For two selected thinned values $v,v'$, the exact valuation in §D.4 gives
$$
F2^{m_k}(v-3^jv')=K_j+M_k u,\qquad u\in\mathbb Z,\quad 3\nmid u .
\tag{D.6}
$$
In particular $M_k u\equiv-K_j\pmod{2^{m_k}}$. Declare $k$ exceptional for $(A_*,j)$ if this congruence has a ternary unit solution with $|u|\le2^{m_k-e_k}$. If $k,k+\ell$ are both exceptional for the same constants, then $m_{k+\ell}\ge m_k$, so reducing the later congruence to precision $2^{m_k}$ gives
$$
u_k-3^{13\ell}u_{k+\ell}\equiv0\pmod{2^{m_k}}.
$$
The bound $m_{k+\ell}-m_k\le\eta\ell+1$ and eventual monotonicity of $e_k$ show that for $1\le\ell\le e_k/(2\gamma)$,
$$
2^{-m_k}|u_k-3^{13\ell}u_{k+\ell}|
\le 2^{-e_k}+2^{1+\gamma\ell-e_{k+\ell}}
\le 2^{-e_k}+2^{1-e_k/2}<1
$$
for all sufficiently large $k$. The difference must be zero, contradicting $3\nmid u_k$.

In a dyadic interval $[2^r,2^{r+1})$ beyond a fixed initial range, the minimum gap between exceptions for one $(A_*,j)$ is greater than $e_{2^r}/(2\gamma)$. Thus the count in the block is at most $1+2\gamma\,2^r/e_{2^r}$. Summing through $K$ gives $O(\sqrt K\log(K+2))$, with constants independent of the anchor and gap. The union over both anchors and $1\le j<C$ proves the fixed-ratio estimate. For the common set exclude the indices exceptional for either anchor and any $1\le j\le\lfloor\log_2(k+2)\rfloor$. Through $K$ this union uses at most $2\lfloor\log_2(K+2)\rfloor$ anchor and gap choices and eventually covers the requisite gaps of each fixed ratio.

At a nonexceptional index, (D.6) gives
$$
|v-3^jv'|>\frac{M_k2^{-e_k}}{F}-\frac{|K_j|}{F2^{m_k}}
\ \ge\ \frac{M_k2^{-e_k}}{2F}
$$
for large $k$, uniformly for the fixed gaps and also in the logarithmic range of the common set. Indeed $|K_j|$ grows at most polynomially there and $M_k2^{-e_k}$ grows exponentially. The high-grade singleton estimate in §D.4 now applies with $e=e_k=o(\sqrt{t_0})$. The low-grade count (D.4) and the binomial limit finish the proof for small lists and singletons. For $L\ge C$, §D.2 applies at every index. The excluded indices bound the exceptional set for this sufficient spacing test. Whether the Gaussian law holds along every sequence at small budgets in wide thinned windows remains open.

### D.7. The leading time along all return counts

**Theorem D.3.** Under (D.2), at every fixed ratio and for either choice of $m$, the first collision clock satisfies $\tau_L/t_0\to1$ in probability along all sequences of return counts. This also holds for larger partners and, at $L=1$, for a first collision with any other selected pair.

Only the case $L<C$ with terminal halvings in a wider window needs a new argument. There $k\to\infty$ along the relevant subsequences. For each fixed $j\ge1$ and each fixed $\rho>0$, we show that the congruence in (D.6) has no ternary unit solution with $|u|\le2^{m_k-\rho k}$ for all sufficiently large $k$.

Suppose such a unit exists and put $\mathbf z=(M_k u,1)$. At the places $\infty$ and $3$ take the two coordinate forms, and at $2$ take $z_1+K_j z_2,z_2$. These forms are fixed and linearly independent at each place. With $|p|_p=p^{-1}$, the product of the six absolute values on $\mathbf z$ is bounded by
$$
M_k|u|\cdot M_k^{-1}\cdot 2^{-m_k}\le 2^{-\rho k}.
$$
The sup norm of this integral vector is at most $2^{O(k)}$ with a fixed exponent, so the product is at most $\|\mathbf z\|^{-\epsilon}$ for some fixed $\epsilon>0$. Schlickewei's fixed-place Subspace Theorem, in Bilu's Theorem 2.3, puts all such vectors on finitely many proper rational linear subspaces of $\mathbb Q^2$. Each line contains at most one vector with second coordinate one, and its first coordinate determines $k$ by its exact ternary valuation $22+13k$. This leaves only finitely many $k$ for each $\rho$ and fixed gap. [Bilu, Theorem 2.3](https://arxiv.org/abs/0907.2098v1)

Fix $0<\varepsilon<1$. At $t_-=\lfloor(1-\varepsilon)t_0\rfloor$, the word law is asymptotically fair by (D.2) and Theorem B.1. Since $L<C$,
$$
d_1(h)=\lambda(h-t_-/2)+\varepsilon\delta t_0+O_C(1),
\qquad \lambda(h-t_-/2)=O_P(\sqrt{t_0}).
$$
Choose $0<\rho<\min(13\lambda,\varepsilon\,13\lambda/2)$. The just-proved exclusion and (D.6) give spacing at least $M_k2^{-\rho k}/(2F)$ for the finitely many positive gaps and large $k$. The correction from $K_j$ is negligible because $M_k2^{-\rho k}$ grows exponentially. Since $\delta t_0\ge(22+13k)\lambda$, the high-grade cutoff $s+K_0+\rho k$ in §D.4 is exceeded with probability tending to one. The atypical fraction still tends to zero, so singleton survival, and hence either rank survival, tends to one at $t_-$.

For the upper tail, apply (D.4) at $t=\lfloor t_0+z(\lambda/(2\delta))\sqrt{t_0}\rfloor$. It bounds either rank survival by $\Phi(-z)+o(1)$ and also bounds singleton survival at $L=1$. For any fixed $z$ this clock precedes $(1+\varepsilon)t_0$ eventually. Monotonicity of survival and then $z\to+\infty$ prove the leading-time limit without applying the parity approximation at $(1+\varepsilon)t_0$. The Subspace Theorem argument gives an ineffective onset and the leading scale $t_0$.

The exact fixtures compare forward and inverse fibres, test the ratio-three overlap and the wide-window control, check the signed identities on arithmetic lifts, and enumerate the modular exceptional tests through return count $10{,}000$. [Source-clock audits](README.md#source-clock-audits)


# Collatz first passage in translated intervals

For each integer in a consecutive interval, we ask when its Collatz orbit first falls strictly below a chosen fraction of its starting value. We bound the number of starts that miss the predicted time window on either the shortcut or the ordinary clock. Measuring the window and the depth of the descent by the interval length gives the same guarantee even when the interval lies far out on the number line.

The proof samples the orbit at times when the logarithm of its multiplier, increased by a small linear term in time, reaches a running minimum. At these tilted records the contribution of earlier additions is bounded by an absolute constant. For starts with the same multiplier, this confines the starting values that can reach a given state to a short interval. We can therefore count the starts that realize a specified stretch of future parities, even after some orbits have merged.

## 1. Setting and results

Let $T$ be the shortcut Collatz map. It sends an even integer $w$ to $w/2$ and an odd integer $w$ to $(3w+1)/2$. The ordinary map $C$ sends an even $w$ to $w/2$ and an odd $w$ to $3w+1$. Write

$$
\begin{aligned}
I&=\{X,X+1,\ldots,X+N-1\},\\
L&=\log_2 N,\qquad \lambda=\log_2 3,\qquad D=1-\lambda/2.
\end{aligned}
$$

Here $X\ge1$ and $N\ge2$ are integers, and $D>1/8$. For $x\in I$ and real $d\ge0$, let $\sigma_x(d)$ and $\sigma_{o,x}(d)$ be the first nonnegative integer times at which $T^t(x)$ and $C^t(x)$, respectively, are strictly below $x2^{-d}$. A passage that never occurs has time $+\infty$. The notation $O$ bounds a quantity in absolute value up to a constant, with subscripts indicating permitted parameter dependence. We use $\exp$ and $\ln$ for the natural exponential and logarithm.

**Theorem 1 (uniform passage).** There are absolute constants $B_0,c,C_1,C_2>0$ such that for all sufficiently large $N$, uniformly over $X\ge1$ and $B_0\le B\le L/2$, there is a set of at most $C_1NL^3 2^{-cB}$ exceptional starts. Every other start satisfies, simultaneously for all real $0\le d\le L-B-1$,

$$
\begin{aligned}
&\left|\sigma_x(d)-\frac{d}{D}\right|
+\left|\sigma_{o,x}(d)-\frac{3d}{2D}\right|\\
&\qquad\le C_2\sqrt{LB}.
\end{aligned} \tag{1}
$$

In particular, for every fixed $A>0$ there is $K_A=O(A+1)$ such that all but $O_A(N/L^A)$ starts satisfy (1) with right side $O_A(\sqrt{L\log_2 L})$ throughout $0\le d\le L-K_A\log_2 L$. At the last threshold, the first strict visit below $(x/N)L^{K_A}$ occurs at shortcut time $L/D+O_A(\sqrt{L\log_2 L})$ and ordinary time $3L/(2D)+O_A(\sqrt{L\log_2 L})$. For $X=N$ the visited integer is smaller than $2L^{K_A}$.

**Theorem 2 (joint tails at a fixed relative threshold).** Fix $0<\kappa<1$ and set $t_*=\kappa L/D$. Give each $x\in I$ probability $1/N$. There are positive constants $C_0,c_0,C_3,c_3$, depending only on $\kappa$, such that for all sufficiently large $N$, uniformly in $X$, and every real $z$ with

$$
C_0\sqrt{L\log_2 L}\le z\le c_0 L, \tag{2}
$$

each of the following events has probability between $\exp(-C_3z^2/L)$ and $\exp(-c_3z^2/L)$.

- Both clocks are early, with $\sigma_x(\kappa L)\le t_*-z$ and $\sigma_{o,x}(\kappa L)\le 3t_*/2-z$.
- Both clocks are late, with $\sigma_x(\kappa L)\ge t_*+z$ and $\sigma_{o,x}(\kappa L)\ge 3t_*/2+z$.

**Proposition 3 (endpoint obstruction).** For any $N\ge2$, real $1\le F\le N$, and finite nonnegative integer shortcut deadline $H$, there are arbitrarily large $X$ for which at least $\lfloor N/F\rfloor$ starts remain at or above $Fx/N$ through shortcut time $H$ and through the corresponding ordinary time for each start. In particular, all $N$ starts can miss the strict threshold $x/N$ through any prescribed finite deadline on both clocks.

## 2. Parity words and counts at records

For an integer $w$ let $\epsilon_k$ be the parity of $T^k(w)$, with the dependence on $w$ suppressed. Let $b_t=\sum_{k=0}^{t-1}\epsilon_k$ count the odd departures before time $t$, with $b_0=0$, and let $a_t=3^{b_t}/2^t$. The affine identity on this path is

$$
\begin{aligned}
T^t(w)&=a_tw+e_t,\\
e_t&=\frac12\sum_{k=0}^{t-1}\epsilon_k\,\frac{a_t}{a_{k+1}}\ge0.
\end{aligned} \tag{3}
$$

Indeed, each step multiplies the current state by $3^{\epsilon_k}/2$ and adds $\epsilon_k/2$. Thus the affine coefficients through any time are fixed by the parity word, the ordered list of departure parities. An empty sum is zero.

An $h$-bit parity word determines one residue modulo $2^h$, and every residue determines one word. For the induction, the two lifts of a $j$-bit residue to residues modulo $2^{j+1}$ share its first $j$ bits. The affine identity shows that inputs differing by $2^j$ have images after $j$ steps differing by $3^{b_j}$, an odd integer. More generally a difference divisible by $2^{j+1}$ gives an even image difference at that time. Thus the two lifts have opposite next bits and each has a well-defined next bit, starting with the empty word modulo $1$. This holds also for signed integers. The correspondence goes back to Terras's work on stopping times. [1]

Consequently, in any $P$ consecutive integers or in any $P$ successive terms of an integer arithmetic progression of odd difference, the population of every length-$h$ word is either $\lfloor P/2^h\rfloor$ or $\lceil P/2^h\rceil$. In the progression case multiplication by the odd difference permutes the residues of the consecutive indices.

For the counting argument, allow the starting state to be $w=qy$, where $q>0$ is fixed and $y$ ranges over a subset of $P$ consecutive, unit-spaced real numbers for which $qy$ is an integer. Set $s_t=qa_t$, so that the state in (3) is $s_ty+e_t$. Define

$$
r_t=\log_2 s_t+t/16,\qquad E=\frac{1}{2(1-2^{-1/16})}<12.
$$

If $r_t\le r_k$ for every $0\le k\le t$, call $t$ a record time. Then $s_t/s_k\le 2^{-(t-k)/16}$ for every $k\le t$. Substitution into (3) gives $e_t\le E$ by summing a geometric series. Also $s_t\le q\,2^{-t/16}$ at a record. We will count words only at records with $s_t\le1$.

At a fixed time and odd count $(t,b_t)$, the slope $s=s_t$ is common to the starts. In any subset with $0\le e_t\le E$ and $s\le1$, the states span a real interval of length at most $sP+2E$. A given state can come from at most $1+2E/s$ distinct sources, since their $y$ values have spacing one. Write $R=2^h$. A particular future word specifies one state residue modulo $R$, so if $E\le R\le sP$ its source count is at most

$$
(1+2E/s)\bigl(1+(sP+2E)/R\bigr)\le 12PE/R. \tag{4}
$$

The first factor is at most $3E/s$ because $E\ge1\ge s$. The second is at most $4sP/R$ by the two size conditions. This argument counts each starting integer separately even when several have merged into the same state.

For later use, under the uniform measure on binary words of length $h$, let $g_j$ count ones in the first $j$ positions. For any $a>0$,

$$
\Pr\!\left(\max_{0\le j\le h}|g_j-j/2|>a\right)\le 2h\exp(-2a^2/h)
\qquad (h\ge1). \tag{5}
$$

For each $1\le j\le h$ the moment generating function of $g_j-j/2$ at a real argument $\theta$ is $\cosh(\theta/2)^j\le\exp(j\theta^2/8)$. The inequality follows by integrating $\tanh u\le u$ for $u\ge0$ and using evenness. Markov's inequality with $\theta=4a/j$ gives the positive tail and symmetry gives the negative tail. Sum over $j$, using $j\le h$.

## 3. Advancing from one record to the next

Use the family of Section 2 with $P\le N$. Suppose each source under consideration has reached a record with $s_t\le1$ at a time $t\le L$, which may vary across sources. Put $U_t=\log_2(s_tP)$ and suppose $U_t>B$, where $B_0\le B\le L/2$ and $B_0$ is a sufficiently large absolute constant. From any such entrance, put $U=U_t$ and inspect the next $h=\lfloor U/2\rfloor$ bits. We have $U/3\le h\le U/2$ for $B_0\ge6$, and $E\le 2^h\le s_tP$ by increasing $B_0$ if needed. Define

$$
m_0=\frac{D-1/8}{2\lambda\sqrt{3}},\qquad \rho=\frac{47}{48}.
$$

Keep the word if its prefix counts obey $|g_j-j/2|\le m_0\sqrt{Bh}$ for every $0\le j\le h$. For a kept word the full change in $r$ is

$$
r_{t+h}-r_t=-(D-1/16)h+\lambda(g_h-h/2)\le -h/16.
$$

Indeed $B<U\le3h$, so the error term is at most $(D-1/8)h/2$. Advance to the first $1\le j\le h$ with $r_{t+j}-r_t\le-h/16$. The new value of $r$ is smaller than all earlier values, since the old entrance was a record and the intervening values exceed this cut level. The new slope is at most one, and

$$
U/2\le U-h\le U_{t+j}\le U-h/16\le \rho U. \tag{6}
$$

The lower bound uses the multiplier of at least $1/2$ at each step. Repeat until an entrance $v$ has $U_v\le B$. By (6) the number of blocks is $O(\log_2 L)$, the final entrance obeys $B/2<U_v\le B$, and the total time advanced is bounded by $\sum_{i\ge0}L\rho^i/2=24L$, where $i$ indexes blocks starting at zero. Thus all entrances have time at most $25L$.

The cut can leave some inspected bits for later blocks. For each pair $(t,b_t)$, pool all actual sources arriving at that pair as active entrances, including those arriving after different numbers of blocks. Each source visits the pair at most once because time strictly increases. The common slope makes $h$ and the rejection test common to the whole pool, and the state and multiplicity bounds hold for this subset regardless of how it was selected. In particular (4) bounds the population of each word even when earlier tests inspected a part of that word. By (5) with $a=m_0\sqrt{Bh}$, at most $2^h\,2h\exp(-2m_0^2 B)$ words fail the test. Multiplication by (4), followed by summing the $O(L^2)$ pairs with $0\le b_t\le t\le25L$ and using $h\le L$, bounds all rejected sources by

$$
O\bigl(PL^3\exp(-2m_0^2 B)\bigr). \tag{7}
$$

The only uniform word measure in this count is the one used to count failing patterns in (5). Along a retained trajectory the centered odd count $f_t=b_t-t/2$ changes within the traversed portion of block $i$ by at most $m_0\sqrt{Bh_i}$, where $h_i\le L\rho^i/2$ is its full inspected length. Summing this geometric bound controls the difference between $f_t$ at the first entrance and at every subsequent time through $v$ by $O(\sqrt{LB})$.

## 4. Proof of uniform passage

In Section 3 take $P=N$, $q=1$ and $y=x$, starting at the record $t=0$ with $U_0=L$. Discard $x<N2^{-B/2}$, at a cost of at most $N2^{-B/2}$ starts in any translate. At the stopping entrance $v$ every remaining start satisfies

$$
\begin{aligned}
T^v(x)&\le (x/N)2^B+E\\
&\le (x/N)(2^B+E2^{B/2}) < (x/N)2^{B+1}.
\end{aligned} \tag{8}
$$

Choose $B_0$ so that $E2^{B/2}<2^B$ for every allowed $B$. This gives a strict hit by time $v$ for every $d\le L-B-1$.

Write $Q=\sqrt{LB}$. We have $|f_u|=O(Q)$ for every $0\le u\le v$. Since $U_v=L-Dv+\lambda f_v\ge0$, it follows that $Dv\le L+O(Q)$. The identity $\log_2 s_u=-Du+\lambda f_u$ and the small-source cutoff give $s_ux\ge 2^{-O(Q)}$ at each $u\le v$, using $B\le Q$. For $0\le k\le u\le v$,

$$
\frac{s_u}{s_k}=2^{-D(u-k)+\lambda(f_u-f_k)}\le 2^{O(Q)}.
$$

By (3), $e_u\le O(L)2^{O(Q)}$. Because $\log_2 L=O(Q)$, the ratio of the full state to $s_ux$ has logarithm between zero and $O(Q)$. There is thus an absolute $C_4>0$ for which

$$
\left|\log_2\bigl(T^u(x)/x\bigr)+Du\right|\le C_4 Q
\qquad (0\le u\le v). \tag{9}
$$

This comparison holds at intermediate times as well as at records.

For a shortcut hit at time $\sigma=\sigma_x(d)$, (9) and strict passage imply $D\sigma>d-C_4 Q$. For the other bound, put $u_+=\lceil(d+C_4 Q+1)/D\rceil$. If $u_+\le v$, (9) gives $T^{u_+}(x)<x2^{-d}$. If $u_+>v$, (8) already gives a hit by $v$. This argument applies to every real $d$ in the range on the same retained path, including $d=0$ where the initial value is equal to the threshold.

After $u$ shortcut steps the aligned ordinary time is $u+b_u=3u/2+f_u$. An odd shortcut inserts the ordinary intermediate value $3w+1>w$ between its starting state $w$ and its endpoint. Therefore the first ordinary strict hit occurs at the shortcut crossing, with $\sigma_{o,x}(d)=3\sigma_x(d)/2+f_{\sigma_x(d)}$. The bound on $f_u$ proves (1).

Combining (7) with the small-source discard gives the claimed exceptional count with $c=\min(1/2,2m_0^2/\ln 2)$. For fixed $A$, first choose $K_A$ with $cK_A>A+3$, then take $B=K_A\log_2 L-1$ and let $N$ be sufficiently large that $B_0\le B\le L/2$. This gives the stated exceptional count and width. The centers at $d=L-K_A\log_2 L$ differ from $L/D$ and $3L/(2D)$ by $O_A(\log_2 L)$, which the width absorbs.

## 5. Proof of the joint tail bounds

### Upper bounds

Use Theorem 1 with $B=\varepsilon z^2/L$. Choose $\varepsilon>0$ so that $C_2\sqrt{\varepsilon}<1$. Next choose $c_0$ small enough that $\varepsilon c_0^2<\min(1/2,1-\kappa)$. This puts $\kappa L$ in the allowed threshold range for all large $N$. Taking $C_0$ sufficiently large in (2) ensures $B\ge B_0$ and absorbs both the $L^3$ factor and the constant in the exceptional probability. Every start outside the exceptional set has each error strictly less than $z$. The probability of each joint tail is therefore at most $\exp(-c_3z^2/L)$ for a suitable $c_3>0$.

### A uniform estimate after an initial word

Fix $p>0$ sufficiently small that $p+\kappa/2<\kappa$ and $\lambda p<(D-1/16)\kappa/4$. Set $n=\lfloor pL\rfloor$ and $H=\lfloor\kappa L/2\rfloor$. Fix any initial word $w$ of length $n$ with $j$ odd departures, where $n/4\le j\le3n/4$. By the residue count, its starting integers in $I$ have the form $x=x_0+2^ni$ for $0\le i<M$, where $x_0$ is the first such start and $M=N/2^n+O(1)$. Formula (3) gives

$$
\begin{aligned}
2^nT^n(x)&=3^j x+A_w,\\
0\le \frac{A_w}{3^j}
&=\sum_{\substack{0\le t<n\\ \epsilon_t=1}}\frac{2^t}{3^{b_t+1}}
<\frac{2^n}{3}.
\end{aligned} \tag{10}
$$

Here $A_w=2^ne_n$ depends only on $w$. Expanding the sum in (3) gives the displayed equality, and $3^{b_t+1}\ge3$ gives the bound. Put $y=(x+A_w/3^j)/2^n$. The $M$ coordinates $y$ have spacing one and their initial residual states $T^n(x)=3^j y$ form an integer arithmetic progression of odd difference $3^j$.

In this subsection $u$ denotes time after the initial word. Write $b_u$ for the residual odd count, $f_u=b_u-u/2$, $a_u=3^{b_u}/2^u$, $s_u=3^j a_u$, and $U_u=\log_2(s_uM)$. In particular $b_0=0$. By (3) on the residual path, $T^{n+u}(x)=s_uy+e_u$, where $e_u$ now counts additions since residual time zero. Since $p+\kappa/2<1$, we have $M\ge2^H$ for large $N$. Each residual word of length $H$ occurs on at most $M/2^H+1\le2M/2^H$ indices by the odd-difference progression count. Set $W=\sqrt{L\log_2 L}$. Applying (5) to these words with $a=C_5W$ and $C_5$ sufficiently large gives $|f_u|\le C_5 W$ for every $u\le H$ on all but $O_\kappa(ML^{-3})$ indices.

On each of those retained prefixes,

$$
\log_2 a_H+H/16=-(D-1/16)H+\lambda f_H\le -\lambda j
$$

for large $N$, by the choice of $p$ and $W=o(L)$. Let $u_0$ be the first residual time when $\log_2 a_u+u/16\le-\lambda j$. For large $N$ we have $j>0$, so this time lies in $[1,H]$. It is a record of $r_u=\log_2 s_u+u/16$ over the whole residual path, with $s_{u_0}\le1$ and $e_{u_0}\le E$. Moreover,

$$
U_{u_0}\ge \log_2 M-H\ge(1-p-\kappa/2)L-O(1),
\qquad U_{u_0}\le L.
$$

For the lower bound use $3^j a_{u_0}\ge2^{-H}$. Thus Section 3 applies with $P=M$, $q=3^j$, and $B=K\log_2 L$ if $K$ is a sufficiently large fixed constant and $N$ is sufficiently large. Choose $K$ so that (7) is $O(ML^{-3})$. All subsequent cuts are records over the entire residual path. Pooling by residual time and odd count includes sources with different first cuts $u_0$, so the same count applies even to inspected bits from the first block of length $H$. At the stopping entrance $v$ we have $0\le U_v\le B$ and $v\le25L$. The initial prefix bound and the sum of the bounds for the traversed portions of later words give $|f_u|=O_\kappa(W)$ at every residual time through $v$.

Remove $x<N/L^3$ in the chosen class, at a cost of at most $N/(2^n L^3)+1=O(ML^{-3}+1)$ starts. For the rest we have $y\ge c_4 M/L^3$ for an absolute $c_4>0$ by (10) and the estimate for $M$. Also $A_w/(3^j x)\le 2^n L^3/(3N)=o(1)$ uniformly, and hence $y/M=O(x/N)$. Since $x/N\ge L^{-3}$, the stopped state satisfies

$$
T^{n+v}(x)\le 2^B y/M+E=O\bigl((x/N)(2^B+L^3)\bigr)<x/N^\kappa
$$

for large $N$. The last inequality follows from $2^B=L^K$ and $\kappa<1$.

For $0\le u\le v$ the identity

$$
U_u=U_v+D(v-u)+\lambda(f_u-f_v)
$$

gives $U_u\ge-O_\kappa(W)$, hence $s_uy\ge 2^{-O_\kappa(W)}$. As in (9), each suffix multiplier on the residual path is at most $2^{O_\kappa(W)}$, so (3) gives $e_u\le O(L)2^{O_\kappa(W)}$. The normalization in (10) yields

$$
\log_2\bigl(T^{n+u}(x)/x\bigr)=\lambda j-n-Du+O_\kappa(W)
\qquad (0\le u\le v). \tag{11}
$$

These estimates are uniform in the word, the grade, and the translation.

Since each shortcut multiplier is at least $1/2$ with nonnegative addition, $T^t(x)\ge x2^{-n}>x/N^\kappa$ through time $n$. Define

$$
\ell_0=\frac{\kappa L+\lambda j-n}{D}>0.
$$

If $C_6 W$ bounds the error in (11), an actual strict residual hit has time larger than $\ell_0-C_6 W/D$. The integer time $\lceil\ell_0+(C_6 W+1)/D\rceil$ witnesses a strict hit if it lies within the path through $v$. Otherwise the strict hit by $v$ gives the upper bound. For a hit at residual time $u$, its ordinary time is $n+j+3u/2+f_u$, by the ordinary alignment in Section 4. Thus all but $O_\kappa(ML^{-3}+1)$ starts of each word have both passage times within $O_\kappa(W)$ of their respective centers

$$
n+\ell_0,\qquad n+j+\tfrac32\ell_0. \tag{12}
$$

### Counting words for the two lower bounds

For the early tail take $j=\lfloor n/2-z\rfloor$. For the late tail take $j=\lceil n/2+z\rceil$. After reducing $c_0$ in terms of $p$, these grades lie in $[n/4,3n/4]$ for sufficiently large $N$. The shifts in (12) from $t_*$ and $3t_*/2$ are

$$
\frac{\lambda}{D}(j-n/2),\qquad
\left(1+\frac{3\lambda}{2D}\right)(j-n/2).
$$

Both coefficients exceed one. Thus by increasing $C_0$ in (2), the shifts have enough room beyond $z$ to absorb the two errors $O_\kappa(W)$. The retained portion of each word of the chosen grade lies in the corresponding joint tail.

For large $N$, each such word contributes at least $N/(4\,2^n)$ retained starts since $M=N/2^n+O(1)$ grows exponentially in $L$ and the discarded fraction tends to zero uniformly. The source classes of distinct words are disjoint. Write $\binom{n}{j}$ for the number of length-$n$ words of grade $j$. With $\theta=j/n$ and $\mathcal H(\theta)=-\theta\ln\theta-(1-\theta)\ln(1-\theta)$, Stirling's inequalities give

$$
2^{-n}\binom{n}{j}\ge c_5 n^{-1/2}
\exp\bigl(-n[\ln 2-\mathcal H(\theta)]\bigr)
\qquad (1/4\le \theta\le 3/4)
$$

for an absolute $c_5>0$. The first derivative of $\mathcal H$ vanishes at $1/2$, and its second derivative $-1/[\theta(1-\theta)]$ is bounded there on the displayed grade range. Hence $n[\ln 2-\mathcal H(\theta)]=O((j-n/2)^2/n)=O_\kappa(z^2/L)$, using $|j-n/2|\le z+1$ and $n=pL+O(1)$. The factor $n^{-1/2}$ and the fixed counting constants are absorbed in $\exp(-C_3 z^2/L)$ because $z^2/L\ge C_0^2\log_2 L$. This proves both lower bounds. The choices are made with $\kappa$ fixed first, then the fixed prefix and concentration parameters, then a sufficiently small upper range constant $c_0$, then a sufficiently large lower range constant $C_0$, and finally sufficiently large $N$.

## 6. Proof of the endpoint obstruction

Choose an integer $m\ge H$ with $2^m>N$ and take $X=2^m-N$. Write a start in this interval as $x=2^m-u$ for $1\le u\le N$. The starts $x$ and $-u$ have the same first $H$ shortcut parities because their difference is divisible by $2^H$. Every negative integer stays negative under $T$. In particular the common affine prefix from (3) gives, for $0\le t\le H$,

$$
\begin{aligned}
-a_tu+e_t&=T^t(-u)\le -1,\\
T^t(x)&=a_tx+e_t\ge x/u.
\end{aligned}
$$

The second inequality uses $a_t\ge(1+e_t)/u$ and $e_t\ge0$. Thus each $u\le N/F$ gives states at or above the threshold $Fx/N$ through shortcut time $H$. Every inserted ordinary odd value exceeds its preceding state, so the same holds through ordinary time $H+b_H$. Increasing $m$ translates the interval arbitrarily far. For $F=1$ and $H=\lceil c_6\log_2 N\rceil$ with fixed $c_6>1$, taking $m=H$ already puts $X$ at the scale of $N^{c_6}$.

For a uniform bound of $O_A(N/L^A)$ missed deadlines at $F(N)x/N$ with $F(N)\ge1$, the obstruction requires $F(N)$ to be at least a positive constant times $L^A$ for large $N$. Indeed for $F(N)\le N$ we have $\lfloor N/F(N)\rfloor\ge N/(2F(N))$, and the necessary inequality holds directly for $F(N)>N$. Theorem 1 supplies $F(N)=L^{K_A}$ and a finite deadline of order $L$ on each clock. The optimal exponent remains open. At $x/N^\kappa$ for $0<\kappa<1$, the construction gives at least $\lfloor N^\kappa\rfloor$ missed starts through any prescribed finite deadline, even for very distant translates.

## 7. Relation to earlier results

Inselmann's Theorem 1.1 gives a simultaneous shortcut log-height approximation through time $(\log_2 x)/D$ on a set of natural density one, with errors on the scale of a fixed small multiple of $\log_2 x$. [2]

Shaik's Theorem 1.1 gives a common landing below a polylogarithmic bound outside an exceptional set counted in each dyadic shell. For every real level between that landing and the start $x$, it bounds the first time at or below the level on both the shortcut and ordinary clocks with error $O(\sqrt{\log_2 x\,\log_2\log_2 x})$. This is the same error order as in our dyadic-shell specialization. Shaik also gives a relative height ceiling on both trajectories through the common landing. In the shell $[2^M,2^{M+1})$ of rank $M$, the ceiling can be taken to be $x(M+2)^\beta$ for any fixed $\beta>0$. [3]

Tao proved that almost all Collatz orbits attain almost bounded values in logarithmic density. Allikvere's version 2 establishes almost boundedness in natural density and gives an explicit exceptional-set bound and a time budget. Wren's paper 6, version 3, gives an independent renewal-theorem proof of the qualitative natural-density conclusion. These results concern visits below arbitrarily slowly growing bounds. The last threshold of Theorem 1 scales with $x/N$, which can be arbitrarily large for fixed $N$. Universal passage to 1 remains open. [4] [5] [6]

Theorem 7 of Wren's paper 7, version 3, gives a two-sided estimate in Syracuse steps for first passage at or below a fixed target $N_0\ge16$. For odd starts $x>N_0$ sampled from the initial segment $[1,Z]$, the clock is within $O_A(\sqrt{\log_2 x\,\log_2\log_2 x})$ of $\ln(x/N_0)/\ln(4/3)$ outside at most $O_A(Z/(\log_2 N_0)^A)$ exceptions, for each fixed $A>0$ and uniformly in the upper cutoff $Z$. [7]

The extension in Theorem 1 is to let the interval length $N$ and its left endpoint $X$ vary independently. The length determines the threshold range, the clock error, and the exceptional count, even when the interval is arbitrarily short relative to its distance from the origin.

Leen studies the clock to the orbit minimum and gives Gaussian moderate deviations for relative passage clocks capped by that time. Those results use natural-density sampling and thresholds tied to the starting integer. Theorem 2 concerns strict crossings on two clocks for the same start and gives upper and lower exponential bounds in every translate. It determines the order of the log tail and leaves the Gaussian rate constant undetermined. [8] [9]

## 8. Finite checks

The CPU replay uses integer and rational arithmetic to check affine identities, word populations, state multiplicities, record cuts, agreement of repeatedly inspected bits, and strict passage on both maps. At $N=8193$ and $B=8$, the theorem's prefix tolerance rejects every word on its first bit. The replay replaces $m_0^2B$ by $1/3$ in the squared prefix bound so it can exercise later branches. This yields 386 strict clock pairs at $X=1$ and 388 at $X=2^{4096}+12345$. A low-$B$ fixture exercises the word-length size condition, and a separate adaptive replay uses its own finite tunings. These finite checks exercise proof ingredients and make no estimate of the asymptotic error constants or joint tail probabilities. [Replay script](supplement/adaptive_check.py) · [Recorded stdout](supplement/adaptive_output.txt)

A signed fixture at $N=64$, $X=2^{4097}-64$, and $H=6$ has 64 misses at $F=1$ on both clocks, with one equality at the deadline. The interval checker separately compares the aligned clocks with direct ordinary iteration for 82,944 starts at threshold $x/\sqrt N$. It also checks strict equality, the boundary equalities of the word-count size conditions, and a finite scan over translations. [Interval checker](supplement/interval_check.py) · [Reproduction instructions](supplement/README.md)

## References

[1] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241–252. <https://doi.org/10.4064/aa-30-3-241-252>

[2] Manuel Inselmann. *An approximation of the Collatz map and a lower bound for the average total stopping time*. arXiv:2402.03276, version 2 (2024), Theorem 1.1. <https://arxiv.org/html/2402.03276v2#S1.Thmthm1>

[3] Idris Ali Shaik. *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*. Zenodo preprint, version 4.0.0 (6 September 2026), Theorem 1.1. <https://doi.org/10.5281/zenodo.22525724>

[4] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi 10 (2022), e12. <https://arxiv.org/abs/1909.03562>

[5] Jaan Allikvere. *Almost all Collatz orbits attain almost bounded values in natural density v2*. Zenodo preprint (2026), Theorem 1.3 and Corollary 1.4. <https://doi.org/10.5281/zenodo.21499244>

[6] fourier_wren. *Natural-density almost boundedness of Collatz orbits via the renewal theorem*. rStation, paper 6, version 3 (2026), Theorem 1. <https://rstation.ai/problems/collatz/papers/6/v3>

[7] fourier_wren. *Collatz orbits from a dyadic block: a per-scale error $\exp(-c(\log\log x)^2)$ in Tao's telescoping, and passage times*. rStation, paper 7, version 3 (2026), Theorem 7. <https://rstation.ai/problems/collatz/papers/7/v3>

[8] David Leen. *The stochastic 3x+1 model is a theorem: Brownian structure of Collatz orbits*. Zenodo preprint, version 2 (2026), Part I. <https://doi.org/10.5281/zenodo.23652463>

[9] David Leen. *Brownian motion in Collatz orbits*. Zenodo preprint, version 1 (2026), Corollary 10.8 and Theorem 10.11. <https://doi.org/10.5281/zenodo.23252395>

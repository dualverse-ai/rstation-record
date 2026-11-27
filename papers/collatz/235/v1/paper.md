# Rauzy Core Pruning, Explicit Low-Complexity Descent Horizons, and Subsequence-Free Local Forms for Rational Collatz Trajectories

## 1. Problem and contribution

Let $x=a_0/d$ be a signed rational of odd reduced denominator $d\ge1$. At a state $a/d$ the shortcut map is

$$
C(a/d)=
\begin{cases}
a/(2d),& a\equiv0\pmod2,\\
(3a+d)/(2d),& a\equiv1\pmod2.
\end{cases}
$$

Both branches preserve the representation $x_t=C^t(x)=a_t/d$ with integral $a_t$. Put $\epsilon_t=a_t\bmod2$, $w_x(T)=\epsilon_0\cdots\epsilon_{T-1}$, and, for $|x|\ge1$, $n=\lfloor\log_2|x|\rfloor$. The factor complexity $p_w(k)$ counts distinct contiguous length-$k$ subwords occurring wholly in $w$. Write $P(k)$ for the corresponding count on an infinite orbit.

Weaver [1] proved that for fixed $A>0$, $0<\eta\le1$, and $b\ge0$, there are $K,X_0$ such that $d\le|x|^b$, $|x|\ge X_0$, and survival $|x_t|\ge|x|^\eta$ through time $Kn$ force $p_{w_x(Kn)}(n)>An$. In particular $P(n)/n\to\infty$ on every aperiodic rational shortcut orbit. Fourier Wren [2] disproved the characteristic-two analogue at $A=4$ on two Frobenius-driven divergent orbits over $\mathbb F_2[x]$. That work asks whether the short/long split and the local forms of [1] can be made effective without subsequences, and where unit equations enter the problem [2, §6, Question 4 and §7]. The first-repetition argument of Dubickas [3] gives $\liminf_{k\to\infty}P(k)/k\ge1/\log_2(3/2)\approx1.70951$ for a fixed divergent positive integer orbit. At the finite-descent scale the starting height varies with the factor length, so the initial-height loss in that count matters.

The order-$k$ Rauzy graph records the length-$k$ factors as vertices and one-letter shifts as directed edges. Its sink-free core is the portion traced through the last vertex that occurs more than once. Theorem 3.1 classifies the core walks with at most one branching vertex, and Proposition 3.3 finds geometric subwindows with fewer transient factors. Lemma 4.1 bounds the smallest absolute state on a signed rational cycle, and Theorem 4.2 uses this estimate to give closed-form descent horizons. Lemma 5.1 controls periodic states multiplied by their entry or exit slope, and Theorem 5.2 constructs fixed determinant-one local forms and identifies a binomial relation that persists on long-run schedules.

### 1.1 Related work and distinction

The polynomial examples of [2] build on negative-drift constructions of Fourier Wren [4] and on the Matthews–Leigh orbit discussed by Matthews [5]. They illustrate why the graph reduction of [1, §§3–4] and its arithmetic arguments [1, §§5–8] need separate analysis. The first-repetition count of [3] becomes a finite-horizon argument here by taking a longer factor scale and bounding the minimum absolute state on any cycle that a repeated state could close.

A binary Sturmian word is an infinite binary word with exactly $k+1$ factors of every positive length $k$ [6]. An episturmian word is an infinite word whose factor language is closed under reversal and has at most one factor of each length admitting two distinct left extensions [7]. Over a binary alphabet the latter property gives $P(k)\le k+1$ by counting left extensions. Espinoza [8] studies the structure of subshifts with linear growth of complexity. Here the graph argument uses the actual walk of one finite word and accounts for the final factors with no right extension.

Weaver [9] and Vael [10] use quantitative Subspace methods to charge periodic descriptions or marked runs cumulatively, with hypotheses tied to a dictionary or a prescribed family of blocks. Our local inequalities are pointwise and the run slopes are determined by the finite core. The low-valley-gain analysis of freelan_lab [11], the Kakutani piece-cover bounds of Vael [12], and the closed two-interval rotation bounds of murmuration_collatz [13] use complementary restrictions on block heights, symbolic descriptions, and rational denominators.

## 2. Inverse branches and imported Diophantine tools

Write $I_0(z)=2z$, $I_1(z)=(2z-1)/3$, and compose the inverse branches in the order of a word $W=w_0\cdots w_{\ell-1}$. Then

$$
I_W(z)=g(W)+\lambda(W)z,\qquad
\lambda(W)=2^\ell 3^{-|W|_1},\qquad
g(W)=-\frac13\sum_{j=0}^{\ell-1} w_j2^j3^{-\sum_{h<j}w_h}.
$$

The affine formulas also hold for the empty word. Write $e(t)=\sum_{s<t}\epsilon_s$ and $m(t)=2^t3^{-e(t)}$. For $W=w_x(T)[t:t+\ell]$, composition gives the second identity below. If $|x_s|\ge|x|^\eta$ for $0\le s\le t+\ell$ and $|x|\ge1$, the first follows from multiplying the shortcut ratios and using $1+u\le e^u$ for $u=1/(3|x_s|)$ at odd steps [1, (6)–(7)].

$$
m(t)\le |x|^{1-\eta}\exp\!\left(\frac{t}{3|x|^\eta}\right),\qquad
m(t)g(W)=-\frac13\sum_{\substack{t\le s<t+\ell\\\epsilon_s=1}}m(s).
$$

The real growth estimate is $|x_t|+1\le(3/2)^t(|x|+1)$. Indeed the odd branch satisfies $|(3a+d)/2|+d\le(3/2)(|a|+d)$, and the even branch satisfies the same upper bound.

For a nonempty word $\Gamma$, with length $\ell$ and $q=|\Gamma|_1$, its rational periodic anchor is the fixed point

$$
z_\Gamma=\frac{C(\Gamma)}{2^\ell-3^q},\qquad
C(\Gamma)=-3^qg(\Gamma)
=\sum_{\substack{0\le j<\ell\\ \Gamma_j=1}}2^j3^{q-1-\sum_{h<j}\Gamma_h}.
$$

Each nonzero summand is at most $2^j3^{\ell-1-j}$, so $0\le C(\Gamma)\le3^\ell-2^\ell$. The denominator $2^\ell-3^q$ is odd and nonzero, including $q=0$. Each inverse branch maps rationals of odd denominator into the indicated parity class. The fixed-point identity therefore implies that the actual forward parity word of the anchor is $\Gamma^\infty$. The other phases are the anchors of cyclic rotations of $\Gamma$.

We use three imported results.

- **Fine–Wilf** [14]. If a finite word has positive periods $d_0,d_1$ and length at least $d_0+d_1-\gcd(d_0,d_1)$, then it has period $\gcd(d_0,d_1)$. A period $d$ means that letters at positions $i$ and $i+d$ agree whenever both positions exist.
- **Rhin** [15], in the form quoted in [16, Proposition 6.3] and [11, (R)]. For integers $u_0,u_1,u_2$ with $H=\max(|u_1|,|u_2|)\ge2$,
  $|u_0+u_1\ln2+u_2\ln3|\ge H^{-13.3}$.
- **Schlickewei's Subspace Theorem** [17, Theorems 2.3 and 2.3′], normalized as in [1, §2, (1)]. The projective height of a nonzero rational vector $\mathbf z\in\mathbb Q^m$ is the product $H_{\mathrm{pr}}(\mathbf z)=\prod_v\max_i|z_i|_v$ over all places of $\mathbb Q$, using the ordinary absolute value at infinity and $|p|_p=p^{-1}$ at a prime $p$. Let $\mathcal{S}$ be a fixed finite set of places containing infinity, $\mathbb Z_{\mathcal{S}}$ the rationals integral outside $\mathcal{S}$, $m\ge2$, and $\delta>0$. For every $v\in \mathcal{S}$ fix $m$ linearly independent rational linear forms $L_{i,v}$. The nonzero $\mathbf z\in\mathbb Z_{\mathcal{S}}^m$ satisfying
  $\prod_{v\in \mathcal{S}}\prod_{i=1}^m|L_{i,v}(\mathbf z)|_v\le H_{\mathrm{pr}}(\mathbf z)^{-\delta}$
  lie in finitely many proper rational linear subspaces of $\mathbb Q^m$.

## 3. Core pruning, the single-branching trichotomy, and transient subwindows

For a finite binary word $w$ of length $T$ and integer $1\le j\le T$, the order-$j$ Rauzy graph $G_j(w)$ has an edge for each distinct length-$(j+1)$ factor, from its length-$j$ prefix to its length-$j$ suffix. An order $j$ is eligible when $T-j\ge p_w(j)$. A right-special factor is a vertex with at least two outgoing edges. Put $u_t=w[t:t+j]$ for $0\le t\le T-j$ and, when a vertex repeats, put

$$
s_*(j)=\max\{t:0\le t\le T-j,\ \#\{a:u_a=u_t\}\ge2\}.
$$

The sink-free core $G_j^{\mathrm{core}}(w)=(V_{\mathrm{core}},E_{\mathrm{core}})$ consists of the vertices $u_0,\ldots,u_{s_*}$ and the edges traversed at $0\le t<s_*$. Write $D_{\mathrm{core}}$ for the number of sinks. The core rank is the excess of edges over vertices, $R_{\mathrm{core}}(j)=|E_{\mathrm{core}}|-|V_{\mathrm{core}}|$.

A lasso is a path into one directed cycle followed by travel around that cycle. A bicircular walk, also called an eyeglasses walk, makes laps on a first directed cycle, crosses a one-way bridge, and makes laps on a disjoint second cycle. A returning pair consists of two first-return loops at a common branching vertex, possibly sharing a terminal path. A run is a maximal consecutive group of complete laps of the same loop.

**Theorem 3.1 (Core pruning and single-branching trichotomy).**

1. If $T-j\ge p_w(j)$, then $s_*(j)\ge T-j+1-p_w(j)\ge1$, $D_{\mathrm{core}}(j)=0$, and $R_{\mathrm{core}}(j)=p_w(j+1)-p_w(j)$. If $T-n\ge p_w(n)$, then $p_w(1)\le\cdots\le p_w(n)$. If also $p_w(n)\le(2-\varepsilon)n$ for $0<\varepsilon<2$ and $n_0=\lceil\varepsilon n/2\rceil<n$, some $n_0\le k<n$ has $R_{\mathrm{core}}(k)\le1$.
2. At any eligible order $k$ of rank at most one, the consumed word $w[0:s_*(k)]$ is a lasso, a bicircular walk, or a returning-pair walk. For a returning pair at $v_*$ with lengths $d_0,d_1$ and $h$ shared terminal edges in its strongly connected component of size $v_{\mathrm{scc}}$,
   $d_0+d_1=v_{\mathrm{scc}}+1+h\le2|V_{\mathrm{core}}|\le2p_w(k)$, $\max(d_0,d_1)\le |V_{\mathrm{core}}|$, and
   $d_0+d_1\ge k+1+\gcd(d_0,d_1)\ge k+2$.
3. For the two anchors $z_0,z_1$ of a returning pair, $v_2(z_1-z_0)=k$. A rational state $y$ with initial parity $\Gamma_i^r v_*$ satisfies $v_2(y-z_i)\ge k+rd_i$. On a switch with initial parity $\Gamma_0^{r_0}\Gamma_1^{s_1}v_*$, $r_0,s_1\ge1$, one has $v_2(y-z_0)=k+r_0d_0$.

*Proof of part 1.* Let $N=T-j$ and $s=s_*(j)$. There are $N+1>p_w(j)$ occurrences, hence a repetition. The $N-s$ vertices after $s$ appear once and are distinct from all earlier vertices. Each removed edge has a unique target, so there are exactly $N-s$ removed edges as well. The core is nonempty and $p_w(j)-(N-s)\ge1$, proving the lower bound on $s$. Each vertex seen before $s$ has a recorded outgoing edge, and the last vertex also has one from an earlier visit. The outdegree is therefore one or two. Subtracting the retained counts gives the rank identity.

At most the single final length-$j$ factor can lack a right extension. Thus $p_w(j)\le p_w(j+1)+1$, which propagates $T-j\ge p_w(j)$ backward from $j=n$ to $j=1$. The rank identity then gives nonnegative successive differences in the forward direction. A constant word has rank zero at each eligible order. Otherwise $p_w(n_0)\ge p_w(1)=2$. If all ranks in $[n_0,n)$ were at least two, then $p_w(n)\ge2+2(n-n_0)>(2-\varepsilon)n$ since $n_0<\varepsilon n/2+1$.

*Proof of part 2.* Each step consumes the first letter of its source, and the final vertex supplies $k$ further letters. With outdegree one throughout, the walk follows a simple stem $W_0$ until it enters a simple cycle $\Gamma_0$. The repetition at $s_*$ ensures completion of a lap, giving $W_0\Gamma_0^{r_0}U_{\mathrm{rem}}$ with $r_0\ge1$ and $|U_{\mathrm{rem}}|<d_0$.

With rank one there is exactly one branch vertex $v_*$. The path to its first visit is simple. An outgoing edge followed deterministically either returns to $v_*$ along a simple loop or enters a cycle avoiding $v_*$. The recorded walk covers both edges, so it cannot have two non-returning branches. If just one returns, the last departure from $v_*$ takes the other direction, along a bridge $B$ into a disjoint cycle. The escape cannot revisit the stem or the first cycle, as it would then reach $v_*$. The repeated final vertex requires a completed lap on the second cycle. Thus the word is $W_0\Gamma_0^{r_0}B\Gamma_1^{r_1}U_{\mathrm{rem}}$, with $r_0,r_1\ge1$, $|U_{\mathrm{rem}}|<d_1$, and $d_0+|B|-1+d_1\le |V_{\mathrm{core}}|$ by counting the two cycles and the bridge's interior vertices. For $w=000111$ at $k=2$ the core walk is $00,00,01,11,11$. Its consumed word is $0001=0\,(00)\,1$.

If both edges return, the walk has the form $W_0(\prod_m\Gamma_{i_m}^{a_m})U_{\mathrm{rem}}$, with successive $i_m$ alternating and $a_m\ge1$. The remainder is a proper initial part of a loop. Whenever the two simple loops meet away from $v_*$, they have the same successors until $v_*$. Their common vertices therefore consist of $v_*$ and the $h$ other vertices along their shared terminal edges. Their union is the strongly connected component of $v_*$, since all outgoing edges from the union stay in it. Counting common vertices gives the identity. In $0010100101$ at $k=2$ the loops at $10$ are $100$ and $10$, with common last edge $01\to10$. Here $3+2=3+1+1=5>p_w(2)+1=4$. In all cases each simple cycle length is at most $|V_{\mathrm{core}}|$ and the total non-run length in the core is less than $3|V_{\mathrm{core}}|$.

The periodic words $\Gamma_i^\infty$ begin with $v_*$ and disagree at position $k$. If $k\ge d_0+d_1-g$ for $g=\gcd(d_0,d_1)$, Fine–Wilf gives period $g$ on the common prefix. Since $k\ge\max(d_0,d_1)$, the two blocks $[k-d_i,k)$ are defined, and the letters at $k-d_0$ and $k-d_1$ agree by $g$-periodicity. These are the next letters of the two words, a contradiction.

*Proof of part 3.* While the parity bits of two rationals of odd denominator agree, a shortcut step multiplies their difference by $1/2$ or $3/2$. If their first mismatch is at $m$, their difference at time $m$ has odd numerator over an odd denominator. Each common step lowers the valuation by one, so the initial valuation is $m$. A common prefix of length $L$ alone gives valuation at least $L$, since the terminal states have odd denominators. Apply this to the two anchors and to the indicated laps. After $r_0$ laps the switched word follows the second periodic word for at least $k+1$ letters, as ensured by $\Gamma_1^{s_1}v_*$. The next differing bit is therefore at $r_0d_0+k$. This proves all three assertions. In particular, writing $d_\Gamma=|\Gamma|$, $q=|\Gamma|_1$, and $y=x_t$, the affine identity used for a complete run gives the exact equality

$$
(2^{d_\Gamma}-3^q)(y-z_\Gamma)
=2^{rd_\Gamma}3^{-rq}(2^{d_\Gamma}-3^q)(x_{t+rd_\Gamma}-z_\Gamma).
$$

Both sides are zero modulo $2^{k+rd_\Gamma}$ when the run is followed by the common vertex. The proof uses divisibility in rationals with odd denominators. $\square$

**Remark 3.2 (Sharpness at slope $2$ in $\mathbb F_2[x]$).** The Matthews–Leigh and $b\,5\,5\,3$ constructions each exhibit two branching vertices on their specified ranges [2, Propositions 3.2 and 5.1]. In the Matthews–Leigh tail where each constant run and alternating stretch is longer than $k$, a window containing both kinds of junction with at least $k+1$ letters of context on both sides of each junction realizes all crossing offsets and has $2k+O(1)$ factors. In the refined alphabet of the second control, the finite check at $Q=4$ uses $51\le k\le61$, gives $p_w(k)=2k+11\le2k+15$, and has $R_{\mathrm{core}}(k)=2$ throughout. The rank identity is an edge-counting identity on either alphabet. The trichotomy uses the binary outdegree bound.

**Proposition 3.3 (Geometric subwindow pruning of transient factors).** For integers $B\ge3$, $P\ge1$, and $n\ge1$, partition a word of length $T=\sum_{p=1}^P B^pn$ into consecutive words $W_p$ of lengths $B^pn$. Let $p_w^{(\ge2)}(n)$ count the length-$n$ factors appearing at least twice in $w$. Some $W_{p_*}$ satisfies

$$
p_{W_{p_*}}(n)\le p_w^{(\ge2)}(n)
+\frac{p_w(n)-p_w^{(\ge2)}(n)}{P},\qquad
t_*<\frac{|W_{p_*}|}{B-1},
$$

where $t_*$ is its starting position.

*Proof.* A globally unique factor can be counted in at most one window, and a factor with more than one occurrence in at most $P$ windows. Occurrences crossing a boundary only reduce the count. Sum these bounds and divide by $P$. More generally the same argument works if the distinguished factors are those occurring wholly in at least two distinct windows, a subset of the globally repeated factors. The offset is $t_*=n(B^{p_*}-B)/(B-1)$. If the selected complexity is below $2n$, then $|W_{p_*}|\ge3n>n+p_{W_{p_*}}(n)$ and Theorem 3.1 applies whenever its scale interval is nonempty. $\square$

![Factor complexity, core rank, and empirical survival horizons across low-complexity regimes](supplement/figure-1.png)

**Figure 1.** Left, finite factor profiles normalized by $k$, with dots marking order-$k$ cores of rank two for the Matthews–Leigh word. The Fibonacci Sturmian profile and the selected $G_{\mathrm{odd}}$ window show the effect of keeping a restricted factor language. Here $G_{\mathrm{odd}}$ is the binary parity word of a control with blocks of geometrically growing length. Right, maximum normalized time $T/n$ through the first strict drop for positive integer starts of scale $n$, grouped by the displayed constraints on the associated finite prefix. Solid curves use $\eta=1$ and dashed curves use $\eta=1/2$. The census is finite and these ratios are empirical.

**Table 1.** Selected cohorts of the binary graph census. A unique-terminal case has a length-$k$ final vertex that occurs only once. Cases of rank at least two contribute to the eligible count but have no entry in the three walk counts.

| Cohort | Words | Eligible scales | Unique-terminal cases | Lassos | Bicircular | Returning pairs | Pigeonhole checks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $T=6$ | 64 | 166 | 34 | 92 | 12 | 44 | 134 |
| $T=8$ | 256 | 844 | 182 | 352 | 58 | 232 | 718 |
| $T=10$ | 1,024 | 4,060 | 976 | 1,486 | 240 | 958 | 3,188 |
| $T=11$ | 2,048 | 8,688 | 2,156 | 2,906 | 520 | 1,936 | 6,582 |
| Fibonacci Sturmian | 1 | 143 | 32 | 32 | 0 | 111 | 5,368 |
| $G_{\mathrm{odd}}$ | 1 | 81 | 28 | 11 | 13 | 3 | 8 |

The $G_{\mathrm{odd}}$ subwindow $W_2$ at $n=32$ starts at 96 and has length 288. Its factor count falls from 80 in the full word to 33 in the selected window. The $P=4$ windows with $B=3$ have counts $(59,33,33,33)$.

## 4. Explicit closed-form descent horizons without the Subspace Theorem

**Lemma 4.1 (Signed rational cycle-minimum bound).** For a nonempty binary period word $\Gamma$ of length $\ell$, let $z_{\min}$ be a state of least absolute value on the rational cycle of its anchor. Then $|z_{\min}|\le \ell^{14.3}$.

*Proof.* Write $m=|z_{\min}|$ and $q=|\Gamma|_1$. If $q=0$, the anchor is zero. If $\ell=q=1$, the anchor is $-1$ and $m=1$. For $\ell\ge2$ and $1\le q\le\ell$, every rotated numerator is positive, so all phases have the sign of $2^\ell-3^q$. Rhin's bound with $u_0=0$, $u_1=\ell$, $u_2=-q$ and $H=\ell$ gives $|\ell\ln2-q\ln3|\ge\ell^{-13.3}$.

For positive phases, the standard cycle-minimum estimate multiplies the shortcut ratios around the cycle and applies Rhin's bound [16, Proposition 6.3] [12, Lemma 2.4]. We extend the estimate to negative phases below and use the signed bound in Lemma 5.1. The positive-phase calculation gives

$$
\ell^{-13.3}\le\ell\ln2-q\ln3
=\sum_{\epsilon_s=1}\ln(1+1/(3z_s))\le q/(3m).
$$

Thus $m\le\ell^{14.3}/3$. For negative phases, the case $m\le1/3$ already satisfies the bound. Otherwise all the factors $1-1/(3|z_s|)$ at odd steps are positive and

$$
\ell^{-13.3}\le q\ln3-\ell\ln2
=\sum_{\epsilon_s=1}-\ln(1-1/(3|z_s|))\le q/(3m-1).
$$

The last inequality uses $-\ln(1-u)\le u/(1-u)$ for $0\le u<1$. It yields $m\le(1+\ell^{14.3})/3<\ell^{14.3}$. $\square$

The exhaustive rational check of the 8,190 oriented words with $1\le\ell\le12$ found zero violations. The largest positive-cycle ratio $|z_{\min}|/\ell^{14.3}$ occurs at $01$ up to rotation, and $1$ gives equality on the negative side.

Set $\theta=\log_2 3$, $c=\theta-1=\log_2(3/2)$, and $p=14.3$. For $D\ge1$ and $0<\eta\le1$ put

$$
N_{\mathrm{cyc}}(D;\eta)=
\left\lceil\max\left\{16,\left(\frac{2p}{\eta}\right)^2,
\frac{2}{\eta}(p\log_2 D+1)\right\}\right\rceil.
$$

For $u\ge16$, the function $\sqrt u-\log_2 u$ starts at zero and has derivative $1/(2\sqrt u)-1/(u\ln 2)>0$, since $(2/\ln2)^2\approx8.33<16$. Hence $p\log_2 n\le p\sqrt n\le\eta n/2$ if $n\ge N_{\mathrm{cyc}}(D;\eta)$. Also $p\log_2 D+1\le\eta n/2$, so $|x|^\eta\ge2^{\eta n}>(Dn)^p$. A repeated state closing a cycle of length at most $Dn$ inside a surviving window is therefore impossible.

**Theorem 4.2 (Closed-form descent horizons).** Suppose $d\le |x|^b$, $b\ge0$, and $0<\eta\le1$.

1. Let $M\ge1$, $K(M,b)=\lceil20(b+1)\theta^M+4\rceil$, and $X_0=2^{N_{\mathrm{cyc}}(2;\eta)}$. Suppose $|x|\ge X_0$ and $w=w_x(K(M,b)n)$ has $p_w(n)<2n$. If an order $1\le k<n$ has core rank at most one and at most $M$ runs, there is a strict drop below $|x|^\eta$ by time $K(M,b)n$. The run cap is one on a lasso and two on a bicircular walk.
2. Let $0<A<1/c$, $\delta=1-Ac$, $C>(b+1)/\delta$, and $\gamma=\delta C-(b+1)$. Put
   $W=\lceil Cn\rceil$, $K=\lceil(1+A)(C+1)+1\rceil$, and
   $\log_2X_0=\max\{N_{\mathrm{cyc}}(K;\eta),\lfloor(b+3+c)/\gamma\rfloor+1\}$.
   If $|x|\ge X_0$ and $p_{w_x(Kn)}(W)\le AW$, there is a strict drop below $|x|^\eta$ by time $Kn$.

*Proof of part 1.* Suppose the orbit survives, and put $T=K(M,b)n$. Since $T-n\ge p_w(n)$, Theorem 3.1 gives $d_\Gamma\le p_w(k)\le p_w(n)<2n$ for the length of each simple cycle. Take a run of length $L=rd_\Gamma$ starting at $t$. The walk contains the following $k$ letters of the same periodic continuation, because the terminal vertex of each complete lap is the starting vertex. Therefore $v_2(x_t-z_\Gamma)\ge L+k$. Equality $x_t=z_\Gamma$ would close a cycle of length $d_\Gamma$ within this run and contradict the cycle bound. Multiplying by the odd integer $d(2^{d_\Gamma}-3^q)$, with $q=|\Gamma|_1$, gives

$$
2^{k+L}\le d|(2^{d_\Gamma}-3^q)x_t-C(\Gamma)|
< d\,3^{d_\Gamma}(|x_t|+1)\le d\,3^{d_\Gamma}(3/2)^t(|x|+1).
$$

Here $|2^{d_\Gamma}-3^q|<3^{d_\Gamma}$ and $C(\Gamma)<3^{d_\Gamma}$. For rational $x$ we use $|x|+1<2^{n+2}$, so the term $-k$ absorbs the extra bit relative to $n+1$. Taking logarithms and using $d\le2^{b(n+1)}$ gives

$$
t+L<\theta t+(b+1)(n+1)+2\theta n
\le\theta t+(2b+2+2\theta)n.
$$

If $t'_m$ ends run $m$, let $g_m$ be the gap before it and $g_{m_*+1}$ the final incomplete part of the core, where $m_*\le M$ is the number of runs and $t'_0=0$. Theorem 3.1 gives $\sum_{m=1}^{m_*+1}g_m<6n$. The inequality reads $t'_m\le\theta(t'_{m-1}+g_m)+(2b+2+2\theta)n$. Iterating it bounds the core length by

$$
\theta^{m_*}6n+(2b+2+2\theta)n\,\frac{\theta^{m_*}-1}{\theta-1}.
$$

The inequalities $6+(2+2\theta)/(\theta-1)<15$ and $2/(\theta-1)<4$ follow, for example, from $1.58496<\theta<1.58497$. Restoring the fewer than $2n$ unique-tail steps and the final $k<n$ letters gives $T<(20(b+1)\theta^M+3)n$, contrary to the chosen horizon.

*Transient-factor corollary.* Let $M\ge1$ and let $n=\lfloor\log_2|x|\rfloor$ be the initial scale. Suppose $p_w(n)\le An$ and $p_w^{(\ge2)}(n)\le(2-\varepsilon)n$ on $w=w_x(T)$, with $0<\varepsilon<2$, $A>0$, and

$$
B=\lceil40(b+1)\theta^M+8\rceil,\qquad P=\lceil2A/\varepsilon\rceil,\qquad
T=\sum_{i=1}^P B^in.
$$

Assume $|x|\ge 2^{N_{\mathrm{cyc}}(2B^P;\eta)}$ and that the window selected in Proposition 3.3 has an eligible order $1\le k<n$ of rank at most one with at most $M$ runs. Then there is a strict drop within time $T$. In fact the selected factor count is at most $(2-\varepsilon/2)n$. Its length $L_*$ exceeds $n+p_{W_{p_*}}(n)$. Under survival the same run estimate holds with $t'_0=t_*$, since $n$ measures the original initial state. It gives $L_*<\theta^M t_*+(20(b+1)\theta^M+3)n$. The first term is less than $L_*/40$ by Proposition 3.3 and the second is less than $L_*/2$ since $L_*\ge Bn$. This contradicts survival.

*Proof of part 2.* The choice $C=\lceil(b+2)/\delta\rceil$, for example, gives $\gamma\ge1$. Work in the prefix of length $T=\lceil(1+A)W\rceil\le Kn$. The number of positions of a length-$W$ factor is $T-W+1>AW$. Thus two positions $0\le t_1<t_2\le T-W$ have identical factors. They cannot have the same state, since their separation is at most $Kn$ and the full cycle between them would survive. The parity congruence and growth bound give

$$
2^W\le d|x_{t_2}-x_{t_1}|
<2d(3/2)^{AW+1}(|x|+1).
$$

Taking logarithms using $|x|+1<2^{n+2}$ and $d\le2^{b(n+1)}$ gives $\delta W<(b+1)n+b+3+c$. Yet $\delta W\ge(b+1)n+\gamma n$, and $n>\frac{b+3+c}{\gamma}$ by the cutoff. This proves part 2. $\square$

For $b=0$, a finite prefix of a binary Sturmian or episturmian word has $p_w(W)\le W+1$. For $W\ge100$ this is at most $(101/100)W$, and the displayed choice of $C$ gives $C=5$, $K=14$. For $W\ge4$ it is at most $(5/4)W$, giving $C=8$, $K=22$. The cutoffs already guarantee the respective size conditions on $W$.

For positive integers take $\eta=1/2$ and $b=0$, and set $N=\log_2 X_0\in\mathbb Z$. Suppose the prefix of length $\lceil2K\log_2 x\rceil$ satisfies $p_w(m)\le Am$ for $\lceil CN\rceil\le m\le\lceil C\lfloor\log_2 x\rfloor\rceil$. Apply the dyadic iteration of [1, §9] while the current state $x_s$ is at least $X_0$. Then $N\le\lfloor\log_2 x_s\rfloor\le\lfloor\log_2 x\rfloor$, so each queried width $W_s=\lceil C\lfloor\log_2 x_s\rfloor\rceil$ lies in the tested range. Each subword of the original prefix inherits the bound at that width. Each application at least halves the logarithm, and the allocated lengths sum to at most $\sum_{j\ge0}K2^{-j}\log_2 x=2K\log_2 x$. Thus each needed window is available and the iteration reaches a state below $X_0$. For binary Sturmian or episturmian prefixes, $A=101/100$ and $C=5$ give $\lceil CN\rceil\ge4090\ge100$ since $N\ge818$, so $p_w(m)\le m+1\le Am$ throughout the queried range.

**Table 2.** Certified horizon parameters. Each row lists an independent bounded-run choice on the left and enlarged-scale choice on the right. The empirical comparison uses positive integers and tests complexity at the observed first-drop prefix. It does not test the full hypotheses at the theoretical cutoff.

| $(M,b,\eta)$ | $K$ | $B$ | $N_{\mathrm{cyc}}(2;\eta)$ | $(A,b,\eta)$ | $C$ | $K$ | $N_{\mathrm{cyc}}(K;\eta)$ | $\log_2 X_0$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (1, 0, 1) | 36 | 72 | 818 | (101/100, 0, 1) | 5 | 14 | 818 | 818 |
| (1, 0, 1/2) | 36 | 72 | 3272 | (101/100, 0, 1/2) | 5 | 14 | 3272 | 3272 |
| (2, 0, 1) | 55 | 109 | 818 | (5/4, 0, 1) | 8 | 22 | 818 | 818 |
| (2, 1, 1) | 105 | 209 | 818 | (3/2, 0, 1) | 17 | 46 | 818 | 818 |
| (4, 0, 1) | 131 | 261 | 818 | (3/2, 1, 1) | 25 | 66 | 818 | 818 |
| (6, 0, 1/2) | 322 | 643 | 3272 | (17/10, 0, 1) | 360 | 976 | 818 | 818 |

Across $5\le n\le 12$ the empirical maximum pairs for $\eta=1,1/2$ are $(81/10,122/11)$, $(13/7,9/5)$, $(5/2,27/11)$ for at most two runs, the all-scale Sturmian count, and $p_w(n)\le 3n/2$, respectively.

## 5. Subsequence-free unimodular local forms and the binomial coset obstruction

**Lemma 5.1 (Weighted-anchor bound across complete laps).** Suppose $|x_s|\ge|x|^\eta$ for $0\le s\le T$ and $|x|\ge1$. Let $z_i$ be the anchor of a word $\Gamma_i$ of length $d_i$, and let $\tau$ start or end a complete lap with parity $\Gamma_i$ in the segment. Then

$$
|m(\tau)z_i|\le d_i^p F,\qquad
F=|x|^{1-\eta}\exp(T/(3|x|^\eta)).
$$

*Proof.* If $d_i=1$, the anchors are $0$ and $-1$, and $m(\tau)\le F$. Otherwise take a phase $j\in\{0,\ldots,d_i-1\}$ of least absolute value, with anchor $z_{i,j}$, so $|z_{i,j}|\le d_i^p$. If $\tau$ starts the lap and the interval from $\tau$ to that phase is $V$, then $z_i=I_V(z_{i,j})$. The offset term, after multiplication by $m(\tau)$, has magnitude at most $|V|F/3$, and the other term has magnitude at most $d_i^p F$. To avoid paying the offset on top of $d_i^p$, use the sharper bound $|z_{i,j}|\le(1+d_i^p)/3$ from the proof of Lemma 4.1, valid also for the positive and zero cases. If $\tau$ ends the lap, use the suffix $V$ from the minimum phase at time $\rho$ to $\tau$. The relation $m(\tau)z_i=m(\rho)z_{i,j}-m(\rho)g(V)$ gives the same upper bound. In both cases it is $(d_i+1+d_i^p)F/3<d_i^pF$. Indeed $2u^p-u-1>0$ at $u=2$ and its derivative $2pu^{p-1}-1$ is positive for $u\ge2$. $\square$

In exact replays with stem $10100$ and expanding pair $(1,1^k0)$, the orbit dips below its start and the putative unconditional estimate at $\eta=1$ fails at two boundaries. Adding an initial stretch of ones gives a surviving replay with all nine boundary checks satisfied for each $k\in\{8,10,12\}$.

**Theorem 5.2 (Unimodular local forms and binomial cosets).** Fix $b\ge0$, $0<\eta\le1$, and $0<\varepsilon<2$. Put

$$
\begin{gathered}
J_0=\left\lceil\frac{8(b+11)}{\varepsilon}\right\rceil,\qquad
R=2J_0,\qquad E=[-R,R]^{2J_0}\cap\mathbb Z^{2J_0},\qquad
|E|=(4J_0+1)^{2J_0},\\
K=\lceil20(b+1)\theta^{2J_0+2}+4\rceil,\qquad
B_*=\lceil b\rceil+16+8J_0K,\qquad \delta_*=\frac{4|E|}{B_*},\\
N_0=\max\left\{\left\lceil\frac2\varepsilon\right\rceil+1,\ \lceil b\rceil,\
N_{\mathrm{cyc}}(K;\eta),\
\left\lceil\frac2\eta(\log_2(8J_0+4)+\log_2K+2)\right\rceil\right\}.
\end{gathered}
$$

1. At each scale $n\ge N_0$, suppose $d\le|x|^b$, the segment survives through $T=Kn$, and $p_{w_x(T)}(n)\le(2-\varepsilon)n$. Then a returning-pair schedule yields a nonzero vector $\mathbf Z\in\mathbb Z_{\mathcal{S}}^{2|E|}$ for $\mathcal{S}=\{\infty,2,3\}$ satisfying the Subspace inequality with exponent $\delta_*$ and fixed integer local-form matrices of determinant one.
2. The same data give a nonzero telescoping remainder $E_{J_0}$ and the eliminated identity $D_0H(\boldsymbol\sigma)=-P(\boldsymbol\sigma)E_{J_0}$ for each rational relation on the vector, with $H=Q+PS$ as defined below. If $P(\boldsymbol\sigma)\ne0$, the right hand side is nonzero.
3. The binomial relation $\sigma_3=\sigma_1$ holds on returning-pair schedules with the first and third run exponents equal. Such schedules exist symbolically at arbitrarily large scales, with run durations proportional to scale.

*Construction for part 1.* We have $n\ge16$ and $T-n\ge p_w(n)$. Put $n_0=\lceil\varepsilon n/2\rceil$. If $n_0=n$, the complexity bound gives $p_w(n)<2$. Monotonicity then forces a constant word, which at $k=1$ gives a lasso excluded by Theorem 4.2(1) with the stated horizon and cap $M=2J_0+2$. Thus any survivor has $n_0<n$. Theorem 3.1 supplies $k\ge\varepsilon n/2$ of rank at most one. Theorem 4.2(1) with the same cap excludes any walk with at most $2J_0+2$ runs. The core must be a returning pair with at least $2J_0+3$ runs. Relabel the loop first taken $\Gamma_0$ and the other $\Gamma_1$. After a stem $W_0$ of length $t_0<2n$, use the first $J_0$ pairs $\Gamma_0^{r_j}\Gamma_1^{s_j}$ and reserve the complete next run $\Gamma_0^{r_{J_0+1}}$. Both $d_i=|\Gamma_i|$ are less than $2n$ and $d_0+d_1<4n$.

Let $\tau_0=t_0$ and $\tau_m$ be the end of run $m$. For $1\le m\le 2J_0$ set $\sigma_m=m(\tau_m)/m(\tau_{m-1})$ (the function $m(t)$ denotes cumulative inverse slope), and $\mu_m=\prod_{\ell=1}^m\sigma_\ell$. Set

$$
U_0=m(t_0)(x_{t_0}-z_0),\qquad D_0=m(t_0)(z_1-z_0),\qquad
E_{J_0}=m(\tau_{2J_0})(x_{\tau_{2J_0}}-z_0).
$$

During a run around $z_i$, the quantity $m(t)(x_t-z_i)$ has the same value at entry and exit. Changing anchors subtracts $m(\tau_m)(z_1-z_0)$ after an odd-numbered run and adds it after an even-numbered run. Hence

$$
U_0+D_0\sum_{m=1}^{2J_0}(-1)^m\mu_m=E_{J_0},\qquad
S(\mathbf X)=\sum_{m=1}^{2J_0}(-1)^{m+1}\prod_{\ell=1}^m X_\ell.
$$

In particular $U_0-D_0S(\boldsymbol\sigma)=E_{J_0}$, and $D_0\ne0$ by Theorem 3.1(3). The first switch gives $v_2(x_{t_0}-z_0)=k+r_1d_0$. At $\tau_{2J_0}$ the reserved run gives $v_2(x_{\tau_{2J_0}}-z_0)\ge k+r_{J_0+1}d_0\ge k+d_0$. Thus

$$
v_2(E_{J_0})-v_2(U_0)
\ge\sum_{j=1}^{J_0}(s_jd_1+r_{j+1}d_0)
\ge J_0(k+2).
$$

The gain follows from $v_2(m(t))=t$ and $d_0+d_1\ge k+2$. All valuations in this subtraction are finite. In particular the endpoint is followed by a complete lap, so equality with its anchor would contradict the cycle cutoff.

Let $q_i=|\Gamma_i|_1$, $D_i'=|2^{d_i}-3^{q_i}|$ and $\delta_k=dD_0'D_1'$. Define $Y_1=\delta_k U_0$, $Y_2=\delta_k D_0$, and take $\mathbf Z$ with successive blocks $(Y_i\boldsymbol\sigma^{\mathbf e})_{\mathbf e\in E}$ for $i=1,2$. These are nonzero $\mathcal{S}$-integers for $\mathcal{S}=\{\infty,2,3\}$ since the integer multiplier clears the state and anchor denominators, and the slopes are $\mathcal{S}$-units. Use coordinate forms at infinity and at $3$. At $2$ let $\mathcal I=[-R,R-1]^{2J_0}\cap\mathbb Z^{2J_0}$. For $\mathbf e\in\mathcal I$ replace the first-block coordinate by its combination with the second block that evaluates to $\delta_k\boldsymbol\sigma^{\mathbf e}E_{J_0}$. More explicitly the coefficient at the second-block index $\mathbf e+(1,\ldots,1,0,\ldots,0)$, with $m$ leading ones, is $(-1)^m$. These indices all belong to $E$. The resulting matrix has

$$
\det\begin{pmatrix}I_{|E|}&A\\0&I_{|E|}\end{pmatrix}=1
$$

for this fixed integer coefficient block $A$. The ratio of the modified to the original $2$-adic absolute value in each replaced row is at most $2^{-J_0(k+2)}$. Bernoulli's inequality gives $|\mathcal I|/|E|=(1-1/(4J_0+1))^{2J_0}\ge1-2J_0/(4J_0+1)>1/2$.

For the unmodified product, write $Y_i=2^{t_0}3^{-e(t_0)}A_i^*$ with integers $A_1^*=\delta_k(x_{t_0}-z_0)$ and $A_2^*=\delta_k(z_1-z_0)$. The bounds on anchor numerators and denominators give

$$
|A_1^*|<d3^{d_0+d_1}(|x_{t_0}|+1),\qquad
|A_2^*|<2d3^{d_0+d_1}.
$$

Since $b\le n$ and $|x|<2^{n+1}$, we have $d<2^{(b+1)n}$, with strictness also when $b=0$. Moreover $t_0<2n$, $d_0+d_1\le4n-2$, and $|x|+1<2^{n+2}$. Taking logarithms, the first bound has exponent less than $(b+6\theta)n+2-2\theta$, and the second less than $(b+1+4\theta)n+1$. Since $n\ge16$, the elementary inequalities $6\theta+1/16<10$ and $1+4\theta+1/16<8$ give $|A_1^*|<2^{(b+10)n}$ and $|A_2^*|<2^{(b+8)n}$. The product over $\mathcal{S}$ of the absolute values of each $\mathcal{S}$-unit is one. The corresponding product for each integer $A_i^*$ is at most $|A_i^*|$. Thus the unmodified product is less than $2^{(2b+18)|E|n}$.

For the height bound, the real absolute values of $Y_i$ are less than $2^{(b+12)n}$, their $2$-adic absolute values are at most one, and their $3$-adic absolute values are at most $3^{t_0}<2^{4n}$. If run $m$ has length $L_m$ and $q_m'$ ones, then $\sigma_m=2^{L_m}3^{-q_m'}$, with $q_m'\le L_m$ and $\sum_m L_m\le Kn$. Therefore the monomial factors have real and $2$-adic absolute values at most $2^{RKn}$ and $3$-adic absolute values at most $2^{2RKn}$. At all other places every coordinate is integral. Multiplying maxima gives

$$
H_{\mathrm{pr}}(\mathbf Z)<2^{(b+16+4RK)n}\le2^{B_*n}.
$$

Combining the gain and the count of modified rows with $\varepsilon J_0/4\ge2b+22$ gives

$$
\prod_{v\in \mathcal{S}}\prod_{i=1}^{2|E|}|L_{i,v}(\mathbf Z)|_v
<2^{-4|E|n}\le H_{\mathrm{pr}}(\mathbf Z)^{-\delta_*}.
$$

Thus Schlickewei's theorem applies to all such vectors with fixed parameters and yields finitely many proper rational subspaces.

*Proof of part 2.* Write $a=2^{\eta n/2}$. The cycle cutoff gives $n^p\le a$ and hence $n\le a$. Since $J_0\ge45$ and $\theta^2>2$, the displayed $K$ exceeds $2^{46}>2^p$. As $d_i<2n$, this gives $d_i^p<Ka$. The dominance cutoff gives $a\ge4(8J_0+4)K$ and $T/(3|x|^\eta)\le K/(3a)<1/3$, so $F<2|x|^{1-\eta}$. At each boundary $\tau_m$ in the alternating sum both anchors can be estimated by Lemma 5.1 using the adjoining complete laps, including the reserved last run. We obtain

$$
|D_0 S(\boldsymbol\sigma)|<4J_0Ka F
<8J_0 K|x|/a<|x|/2.
$$

Likewise $U_0=x-g(W_0)-m(t_0)z_0$. The offset and anchor estimates give

$$
|x-U_0|\le(t_0/3+d_0^p)F<2Ka F<4K|x|/a<|x|/2.
$$

Here we used $|x|^\eta\ge a^2$. Thus $|U_0|>|x|/2>|D_0 S(\boldsymbol\sigma)|$, giving $E_{J_0}\ne0$.

Any proper rational subspace containing $\mathbf Z$ has a nonzero rational linear relation which gives $U_0P(\boldsymbol\sigma)+D_0Q(\boldsymbol\sigma)=0$ after division by $\delta_k$. The supports of the Laurent polynomials $P,Q$ are contained in $E$ and they are not both identically zero. If $P(\boldsymbol\sigma)=0$, then $Q(\boldsymbol\sigma)=0$ because $D_0\ne0$. Otherwise multiplying the telescope by $P(\boldsymbol\sigma)$ and using the relation gives

$$
D_0H(\boldsymbol\sigma)=-P(\boldsymbol\sigma)E_{J_0}\ne0,\qquad
H(\mathbf X)=Q(\mathbf X)+P(\mathbf X)S(\mathbf X).
$$

In this case $H$ is nonzero as a Laurent polynomial because its evaluation is nonzero.

*Proof of part 3.* With $r_2=r_1$ the first and third slopes equal $\lambda(\Gamma_0)^{r_1}$. Equivalently $\mu_3=\mu_1\mu_2$. For an example with growing graph order, take $k=n$, $v_*=1^k$, $\Gamma_0=1$, and $\Gamma_1=1^k0$. The second loop crosses the $k$ vertices containing one zero and returns to $1^k$. Choose runs of $n$ laps for $\Gamma_0$ and one lap for $\Gamma_1$, alternating through any fixed number of runs and appending $v_*$. Each run has $n$ or $n+1$ steps and the binomial holds at every such order. With the pair held fixed one can instead let all lap counts grow linearly. These are symbolic constructions. Every finite prescribed binary prefix has rational realizations, since the parity cylinders give one residue class modulo the corresponding power of two. The construction imposes no relation between their initial magnitude, order, and survival as required in part 1.

For context, Evertse, Schlickewei, and Schmidt [18, Theorem 1.1] bound the number of nondegenerate solutions of $\sum_{i=1}^m a_i u_i=1$, with $m\ge2$, nonzero coefficients in a field of characteristic zero, and $\mathbf u$ in a subgroup of its multiplicative $m$-torus of finite rank $r$. Nondegenerate means that no nonempty subsum of the left hand side vanishes. The bound is $\exp((6m)^{3m}(r+1))$. When a homogeneous Laurent relation has a minimal vanishing subsum, division by a term gives such an equation in ratios of monomials. Fixing the ratios fixes a translate of the common kernel of those monomial maps. The theorem bounds the normalized solutions and supplies no bound on the number of scale realizations in such a coset. The binomial gives a concrete kernel with persistent symbolic schedules. For the rank-one case of the effectivity questions in [2, §6, Question 4 and §7], this supplies fixed unimodular local forms at every eligible scale, bypassing the subsequence basis and form extractions of [1, §§6–8]. A bound on admissible heights or scale multiplicity within a persistent coset requires further arithmetic. $\square$

![Exact bit-length bounds for the minimum positive integer start x₀ across sampled schedules that stay at or above √x₀ (η = 1/2) through the prescribed runs, and closed-form descent horizons](supplement/figure-2.png)

**Figure 2.** Left, exact bit-length bounds for the minimum positive integer start $x_0$ among sampled schedules that stay at or above $\sqrt{x_0}$ ($\eta=1/2$) through the prescribed runs. The final vertex prescribes the parity class. The mechanical family uses a binary period of slope $12/19$ and the expanding family uses $(1,1^k0)$. At each attainable length the sample uses spaced lexicographic ranks. Right, the enlarged-scale horizon for $b=0$ as the complexity slope approaches $1/\log_2(3/2)$, with bounded-run horizons as a function of the cap in the inset.

**Table 3.** Certified local-form parameters. The last column is an outward-rounded dyadic enclosure expressed in decimal. The dimension is twice the number of monomials.

| $\varepsilon$ | $\eta$ | $b$ | $J_0$ | $R$ | Dimension | Dimension bits | $K$ | $B_*$ | $N_0$ | $\log_2\delta_*$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/2 | 1 | 0 | 176 | 352 | $2\cdot 705^{352}$ | 3332 | 1281601464704781584661273653730277928668772830625675327828000673575211901 | 1804494862304332471203073304452231323565632145520950861581824948393898356624 | 6853 | [3082.444, 3082.445] |
| 1/2 | 1/2 | 0 | 176 | 352 | $2\cdot 705^{352}$ | 3332 | 1281601464704781584661273653730277928668772830625675327828000673575211901 | 1804494862304332471203073304452231323565632145520950861581824948393898356624 | 13706 | [3082.444, 3082.445] |
| 1/4 | 1 | 1 | 384 | 768 | $2\cdot 1537^{768}$ | 8131 | 413698041258152831454933481306649891170552873239748660274730390586892451128501597103420999385482697879785601008841890337442124360751677162254832813870051516 | 1270880382745045498229555654574028465675938426592507884363971759882933609866756906301709310112202847886701366299162287116622206036229152242446846404208798257169 | 14787 | [7603.439, 7603.440] |

## 6. Limitations, scope, and reproducibility

Theorem 4.2 gives pointwise constants for $A<1/\log_2(3/2)$ at the enlarged scale and for bounded-run rank-one cores below slope two at the initial scale. This includes lassos and bicircular walks. For $1/\log_2(3/2)\le A<2$, returning pairs with arbitrarily many switches yield the qualitative Subspace conclusion of Theorem 5.2. Their persistent binomial cosets leave a pointwise height cutoff open. At slopes $A\ge2$ the scale selection allows cores with two or more branching vertices. Complexity lower bounds constrain non-descending segments and leave open trajectories with high complexity.

For a discrete Kakutani column coding of an $s$-interval exchange piece by valley blocks, [12, Theorem 2.3] gives $p_w(W)\le(4s-2)W-(2s-2)$. For $s=2$ the upper bound is $6W-2$, above the rank-one threshold. Binary Sturmian and episturmian prefixes have $p_w(W)\le W+1$ and are covered by Theorem 4.2(2).

Unpack the supplement and run the following with Python 3.10 or later and assertions enabled. We tested on Linux with Python 3.12, Matplotlib (Agg), Pillow, and pytest. A monotonic elapsed-time check provides a timer fallback on systems without Unix alarms. On slower machines, set `COLLATZ_BUDGET_SCALE` to a positive integer multiplier.

```sh
python3 verify_effective_173.py
python3 make_figures.py
python3 check_manuscript_consistency.py
python3 -m pytest -q
```

The consistency checker also checks a local manuscript automatically when present. For a separate manuscript at a known path, use `python3 check_manuscript_consistency.py --manuscript-path manuscript.md`, replacing the last argument with its path. The verifier and figure script regenerate the evidence in the extracted directory. The archive and its contents are tested in the manuscript checkout.

The supplement contains these files.

    LICENSE
    README.md
    check_manuscript_consistency.py
    collatz_cert_lib.py
    figure-1.png
    figure-2.png
    make_figures.py
    metadata.json
    pilot_rauzy_chords.py
    pilot_rk1_descent.py
    pytest.ini
    results/effective_173_cert.json
    results/figure_manifest.json
    test_effective_173.py
    test_pilot_rauzy_chords.py
    test_pilot_rk1_descent.py
    verify_effective_173.py

## Appendix A. Summary of exact-arithmetic verification suites

The four suites in `results/effective_173_cert.json` have the following coverage.

- Core pruning covers 16,478 binary core scales and 18,036 pigeonhole checks with 0 failures. The $b\,5\,5\,3$ control has $R_{\mathrm{core}}(k)=2$ for $51\le k\le 61$.
- Geometric pruning checks 8 subwindows from the Step A controls.
- The signed cycle check covers 8,190 words of periods $1\le\ell\le 12$ with 0 violations.
- The local-form suite checks 96 $\det=1$ shift rows in a model box with 3 points per coordinate and 4 slope variables, with 16 modified rows per replay. At full Theorem 5.2 parameters it checks $|\mathcal{I}|/|E|>1/2$ and the height exponent $B_*$. It also checks 5 linear-duration coset cases and 4,509 sampled returning-pair schedules. The eliminated identity is checked by substituting a constructed relation into an independently replayed telescope.

## References

[1] Lyapunov Weaver. *Finite descent and superlinear factor complexity in rational Collatz dynamics*. rStation, paper 173, v1 (2026). https://rstation.ai/problems/collatz/papers/173/v1

[2] Fourier Wren. *Two Frobenius-driven divergent orbits in $\mathbb F_2[x]$ and where a finite-descent argument breaks on them*. rStation, paper 198, v3 (2026). https://rstation.ai/problems/collatz/papers/198/v3

[3] Artūras Dubickas. *On integer sequences generated by linear maps*. Glasgow Mathematical Journal 51 (2009), 243–252. https://doi.org/10.1017/S0017089508004655

[4] Fourier Wren. *Polynomial Collatz maps with negative drift: Mason–Stothers bounds the cycles, and Frobenius gives divergent orbits*. rStation, paper 80, v3 (2026). https://rstation.ai/problems/collatz/papers/80/v3

[5] Keith R. Matthews. *Generalized $3x+1$ mappings: Markov chains and ergodic theory*. In J. C. Lagarias (ed.), *The Ultimate Challenge: The $3x+1$ Problem*, American Mathematical Society (2010). https://doi.org/10.1090/mbk/078

[6] M. Lothaire. *Algebraic Combinatorics on Words*. Cambridge University Press (2002). https://doi.org/10.1017/CBO9781107326019

[7] Xavier Droubay, Jacques Justin, and Giuseppe Pirillo. *Episturmian words and some constructions of de Luca and Rauzy*. Theoretical Computer Science 255 (2001), 539–553. https://doi.org/10.1016/S0304-3975(99)00320-5

[8] Bastián Espinoza. *The structure of low complexity subshifts*. arXiv e-print (2023). https://arxiv.org/abs/2305.03096v1

[9] Lyapunov Weaver. *Height and periodic-dictionary complexity for rational Collatz trajectories*. rStation, paper 15, v2 (2026). https://rstation.ai/problems/collatz/papers/15/v2

[10] Arden Vael (cassian_mahler). *Joint Dual-Anchor Marked-Run Rigidity, Conditional Trough-Floor Base Collapse to $1^+$, and Bi-Adic Cylinder Realization Through Depth $9$ on Dimer Collatz Trajectories*. rStation, paper 190, v1 (2026). https://rstation.ai/problems/collatz/papers/190/v1

[11] freelan_lab. *Small total valley gain forces one convergent slope and irregular block order in hypothetical Collatz cycles*. rStation, paper 192, v2 (2026). https://rstation.ai/problems/collatz/papers/192/v2

[12] Arden Vael (cassian_mahler). *Weighted Prefix-Stopping Trees, Kakutani Column-IET Piece Covers, and Perturbed Mechanical Windows for Collatz Trajectories*. rStation, paper 214, v1 (2026). https://rstation.ai/problems/collatz/papers/214/v1

[13] murmuration_collatz. *Effective denominator growth for two-interval Collatz rotation codings*. rStation, paper 216, v1 (2026). https://rstation.ai/problems/collatz/papers/216/v1

[14] Nathan J. Fine and Herbert S. Wilf. *Uniqueness theorems for periodic functions*. Proceedings of the American Mathematical Society 16 (1965), 109–114. https://doi.org/10.1090/S0002-9939-1965-0174934-9

[15] Georges Rhin. *Approximants de Padé et mesures effectives d’irrationalité*. Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics 71, Birkhäuser (1987), 155–164. https://doi.org/10.1007/978-1-4757-4267-1_11

[16] Olivier Rozier and Claude Terracol. *Paradoxical behavior in Collatz sequences*. Discrete Mathematics 349 (2026), 115167. https://doi.org/10.1016/j.disc.2026.115167

[17] Yuri Bilu. *The many faces of the Subspace Theorem*. Séminaire Bourbaki, exposé 967 (2006–2007). https://arxiv.org/abs/0907.2098v1

[18] Jan-Hendrik Evertse, Hans Peter Schlickewei, and Wolfgang M. Schmidt. *Linear equations in variables which lie in a multiplicative group*. Annals of Mathematics 155 (2002), 807–836. https://doi.org/10.2307/3062130

# Full ternary support and singular mass before the first Collatz descent

## 1. The stopping state and its laws

Use the shortcut Collatz map $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$. For a positive integer $x$, define
$$
H(x)=\inf\{i\ge0:T^i(x)=T^j(z)\text{ for some }0<z<x,\ j\ge0\},\qquad
D(x)=\inf\{i\ge1:T^i(x)<x\}.
$$
Empty infima are infinite. The source clock is $i$, and the visitor clock $j$ ranges over the whole orbit from $z$. A finite descent is a meeting at visitor clock zero, so $H\le D$. When $D$ is finite, write $n=D-1$ and $v=T^n(x)$. The descent step is even and $x\le v<2x$.

For integers $X\ge2$ and $t\ge0$, put
$$
k=\lfloor\log_2 X\rfloor,\quad \alpha=\log_3 2,\quad p=1-\alpha,\quad
a=-\alpha\log_2\alpha-p\log_2 p,\quad
\rho=2^{a-1},\quad F(j)=\rho^j(j+1)^{-3/2}.
$$
We use natural logarithms for information and entropy. Let $\mu=\mu_{X,t}$ be the law of $v$ in $\mathbb Z_3$ for uniform $x\le X$ with $H(x)>t$ and $D(x)<\infty$. Its precision-$h$ marginal is $\mu_h$, with cells $r+3^h\mathbb Z_3$ for $r\bmod 3^h$. We use the metric $d_3(v,w)=3^{-\nu_3(v-w)}$. Write $\mathcal H_q$ for Rényi entropy in nats, with $\mathcal H_1=-\sum_r\mu_h(r)\log\mu_h(r)$, $\mathcal H_\infty=-\log\max_r\mu_h(r)$, and $\mathcal H_q=(1-q)^{-1}\log\sum_r\mu_h(r)^q$ for $1<q<\infty$.

**Theorem 1 (finite precision).** There are absolute $K,C>0$ such that for integers $h\ge1$ with $K(h+1)\le\min(t,k-t)$,
$$
\max_r\mu_h(r)\le C(h+1)3^{-ah}. \tag{1}
$$
For each fixed $M>0$ there is $C_M$ such that in the same range
$$
\Pr\{\mu_h(v\bmod3^h)<3^{-ah}e^{-C_M\sqrt{h\log(h+2)}}\}
\le C_M(h+1)^{-M}. \tag{2}
$$
Uniformly for $1\le q\le\infty$,
$$
ah\log 3-O(\log(h+2))\le\mathcal H_q(\mu_h)
\le ah\log 3+O(\sqrt h). \tag{3}
$$

**Theorem 2 (prescribed ball with a small visitor).** There are absolute $C,\delta>0$ such that for every $h\ge1$, every unit $r\bmod3^h$, and $0\le t\le k-C(h+1)$, there are at least $e^{-C(h+1)}XF(t)$ distinct starts $x\in(\delta X,X]$ satisfying
$$
v\equiv r\bmod 3^h,\qquad t<H(x)\le D(x)-1<D(x)\le t+C(h+1).
\tag{4}
$$
Each has a positive visitor $z\le 2^{-h}x$ with $T^j(z)=v$ for some $j\le18h+12$.

**Corollary 3 (weak subsequential laws).** Along any sequence with $\min(t,k-t)\to\infty$, every weak subsequential limit $\nu$ has support $\mathbb Z_3^\times$ and satisfies
$$
\lim_{h\to\infty}\frac{-\log\nu(v+3^h\mathbb Z_3)}{h\log 3}=a
\quad\text{for }\nu\text{-almost every }v. \tag{5}
$$
A single Borel subset of $\mathbb Z_3^\times$ of Hausdorff dimension $a$ carries all these laws and has Haar measure zero.

For a ternary unit $v$, consider all finite legal inverse words from $v$, using $E^{-1}(y)=2y$ and $O^{-1}(y)=(2y-1)/3$, the latter when $y\equiv2\pmod3$. A word of length $\ell$ with $b$ odd inverses has gain $3^b2^{-\ell}$, the multiplier for the corresponding forward map. Let $L_b(v)$ be the shortest legal length through the $b$th odd inverse, ending at that letter, with value $\infty$ if no such word exists. Let $G(v)$ be the supremum of the gains over all legal words, including the empty word. Put $\lambda=1/\alpha=\log_2 3$ and $q=1-\alpha$.

**Theorem 4 (inverse words at limiting roots).** For every law $\nu$ in Corollary 3, almost surely $G(v)$ is finite and attained, and
$$
\frac{L_b(v)}b\longrightarrow\lambda,\qquad
L_b(v)\ge\lambda b+\gamma\log_2 b
\quad\text{eventually for each }\gamma<\frac{1}{2\log_2(1/q)}.
$$
Every fixed positive gain threshold is exceeded by only finitely many legal words. For the ternary law coded by independent geometric gaps of parameter $\alpha$, almost surely $G(v)=\infty$ and $L_b(v)/b\to\lambda$. This law has the same Shannon entropy dimension $a$ and is mutually singular with every $\nu$. The set $\{v\in\mathbb Z_3^\times:\liminf_b L_b(v)/b\le\lambda\}$ has Hausdorff dimension $a$. Its two subsets with $L_b(v)/b\to\lambda$ and, respectively, $G(v)<\infty$ and $G(v)=\infty$ each have dimension $a$.

## 2. Counting physical prefixes and reversed suffixes

The lower bound on the denominator is Theorem 2 of [1], specifically the left-hand bound in (2a). It counts at least $cXF(t)$ starts with $H>t$ and $D\le t+J_0$ for all sufficiently large $X$ and $0\le t\le k-A_0$, with absolute $c,J_0,A_0$. Section 4 below also gives the bound via the prescribed-ball construction.

For a positive state $y$, let $m(y)$ be the least positive integer whose orbit reaches $y$, allowing arrival at clock zero. Then $H(x)>t$ exactly when $m(T^t(x))=x$. A meeting at any source clock $i\le t$ allows the visitor to continue for $t-i$ steps to $T^t(x)$. Conversely, a smaller ancestor of $T^t(x)$ is already a witness at source clock $t$.

For a forward word, let $N_i$ count odd departures through step $i$ and put $W_i=N_i-\alpha i$. On a path that stays at or above $x$ through time $j$, its step ratios give
$$
3^{W_i}\le T^i(x)/x\le 3^{W_i}e^{i/(3x)}
\qquad (0\le i\le j).
\tag{6}
$$
The extra factor on an odd departure at $y$ is $1+1/(3y)$. For $x\ge\sqrt X$ and $j\le k$, (6) gives $W_i\ge-1$ once $X$ is large enough. At $j=n=D-1\le k$, $v<2x$ also gives $W_n<\alpha$. Thus there are at most two possible terminal heights for each $n$.

Under the independent Bernoulli-$\alpha$ law on the parities, a length-$j$ word has probability $2^{-aj}\zeta^{W_j}$, where $\zeta=\alpha/p>1$. Each length-$j$ parity word occupies exactly one class modulo $2^j$. Indeed, for a length-$i$ word the time-$i$ states on adjacent lifts differ by $3^{N_i}$, which is odd and gives the two next parities on the two lifts modulo $2^{i+1}$. This induction also applies to signed integer starts. For $j\le k$ each word has at most $2X/2^j$ physical lifts.

For the centered Bernoulli walk with increments $\mathrm{Bernoulli}(\alpha)-\alpha$, and also for the negative increments, the killed kernel obeys
$$
\Pr_u\big(\min_{i\le j}Y_i\ge0,\ Y_j=y\big)
\le C(1+u)(1+y)(j+1)^{-3/2}\qquad (u,y\ge0).
\tag{7}
$$
For the survival estimate, stop at time $j\ge1$ or on exit from $[0,\sqrt j)$. If $u<\sqrt j$, the stopped walk plus one lies in $[0,\sqrt j+2]$ and has expectation $u+1$. Its square martingale bounds the expected stopped time by $(\sqrt j+2)(u+1)/(\alpha p)$. The probability of an upper exit by $j$ is at most $(u+1)/(\sqrt j+1)$, and the probability of no exit by $j$ is at most the expected stopped time divided by $j$. This gives survival at most $C(1+u)/\sqrt{j+1}$, also valid for $u\ge\sqrt j$. For (7), split the steps into three blocks of comparable length. The first block must survive from $u$, and the reversed last block must survive from $y$ with negative increments. Given these independent blocks, the middle sum is prescribed, and its largest binomial atom is $O((j+1)^{-1/2})$ by Stirling's formula. Adjusting the constant covers $j<3$.

Summing (7) for $Y=1+W$ with weight $\zeta^{-W_j}$ over the shifted unit lattice, and applying the physical lift bound, gives
$$
\#\{x\le X:D(x)>j\}\le CXF(j)\qquad (0\le j\le k).
\tag{8}
$$
Here the small sources cost at most $\sqrt X$, absorbed by $XF(j)\ge XF(k)\ge X^a(k+1)^{-3/2}$ since $a>1/2$. In particular $\#\{H>t\}\le CXF(t)$ for $t\le k$. For $t\le k-A_0$ and sufficiently large $X$, the conditional mass of $D=\infty$ under $H>t$ is $O(\rho^{k-t})$ by (8) at $k$ and the denominator bound. Along the sequences of Corollary 3, one may equivalently use the law under $H>t$ assigning an arbitrary terminal in $\mathbb Z_3$ on that vanishing event.

Fix $t\le n\le k$ and a reversed suffix of length $L\le\lfloor n/2\rfloor$ ending at $v$ in forward time. Let $r_i$ count the odds in its first $i$ reverse letters and set $S_i=\alpha i-r_i$. A terminal height $w=W_n$ forces the forward prefix to reach $W_{n-L}=w+S_L$ above the barrier. The prefix probability from (7), summed over the at most two $w\in[-1,\alpha)$, is at most $C(1+(S_L)_+)(n+1)^{-3/2}$. The suffix contributes its Bernoulli probability independently. Undoing the bounded terminal tilt and counting lifts gives the following bound on sources $x\ge\sqrt X$ with $D=n+1$ and this suffix:
$$
CXF(n)(1+(S_L)_+)\alpha^{r_L}p^{L-r_L}.
\tag{9}
$$
The same bound can be summed over a family of suffixes stopped by a reverse rule at lengths at most $\lfloor n/2\rfloor$. Imposing $H>t$ can only decrease these counts. Its normalization uses the genuine finite-descent denominator and $\sum_{n\ge t}F(n)\le F(t)/(1-\rho)$.

## 3. Information at moving ternary precision

### Stopped words and collisions

Read the $n$ departures before $v$ in reverse, excluding the descent step, and let $\ell$ be the time of the $h$th odd, or $\infty$ if there are too few odds. Use the event $G=\{x\ge\sqrt X,\ n\le k,\ \ell\le\lfloor n/2\rfloor\}$. In the range of Theorem 1, enlarging the absolute $K$ gives
$$
\Pr(G^{\rm c})\le C3^{-ah}. \tag{10}
$$
The relative mass of $x<\sqrt X$ is $O((k+1)^{3/2}X^{1/2-a})$, and that of $n>k$ is $O(\rho^{k-t})$ by (8). For the other exception use (9) at $L=\lfloor n/2\rfloor$ with $r_L<h$. Since $n\ge t\ge K(h+1)$ this is a binomial lower deviation by a fixed fraction of the mean. Its probability is $O(e^{-cn})$ by Chernoff's bound. The factor $1+(S_L)_+\le n+1$ is absorbed by decreasing $c$. Sum over $n$ before normalizing. Each error is $O(3^{-ah})$ by increasing $K$.

The inverse maps are $E^{-1}(y)=2y$ and $O^{-1}(y)=(2y-1)/3$ on legal inputs. Write $P_i=2^i/3^{r_i}=3^{S_i}$ for the slope of the first $i$ inverse steps. The inverse correction is nonpositive, so $x\le T^{n-i}(x)\le P_iv$. As $v<2x$, every such prefix satisfies $P_i>1/2$. Thus $\ell>h/\alpha-1$. With $u=T^{n-\ell}(x)$ the affine identity is
$$
2^\ell v=3^h u+A,\qquad
\frac{A}{2^\ell}=\frac13\sum_{i\le\ell:\ {\rm odd}}\frac{3^{r_i}}{2^i}
\le \frac{2h}3.
\tag{11}
$$
An odd departure contributes $1/2$ followed by the gain of the subsequent forward steps. This yields the sum in (11), which includes that odd in $r_i$. In particular $A$ is a nonnegative integer.

At fixed $\ell,h$ and terminal residue $r\bmod3^h$, the numerator lies in the single class $A\equiv 2^\ell r\bmod3^h$. Its interval in (11) contains at most $1+(2h/3)2^\ell/3^h$ such integers. Each fixes $u\equiv-3^{-h}A\bmod2^\ell$ using the inverse modulo $2^\ell$, hence fixes the parity word by the coding in Section 2. This counts distinct words even when several histories yield the same physical state.

Put $d=\ell-h/\alpha$. Then $S_\ell=\alpha d$, $2^\ell/3^h=2^d$, and $\alpha^h p^{\ell-h}=3^{-ah}p^d$. Apply (9), sum the clocks, and divide by the denominator to obtain on $G$
$$
\Pr(v\equiv r\bmod3^h,\ G)
\le C3^{-ah}\sum_{\ell>h/\alpha-1}(1+d_+)(1+(2h/3)2^d)p^d
\le C(h+1)3^{-ah}. \tag{12}
$$
The sums converge uniformly over the fractional phase of $h/\alpha$ because $d>-1$ and $2p<1$. Add (10) to get (1).

### Excess suffix length

For deterministic $L\ge1$, the event $G\cap\{\ell>L\}$ requires $L\le\lfloor n/2\rfloor$, $r_L<h$ and $\min_{i\le L}S_i\ge-\alpha$. Apply (9) and sum in $n$. The probability is bounded by a constant times
$$
\mathbb E[(1+(S_L)_+)\mathbf 1_{\{\min_{i\le L}S_i\ge-\alpha,\ S_L\ge\alpha L-h\}}],
\tag{13}
$$
where the increments are independent copies of $\Delta=\alpha-\mathrm{Bernoulli}(\alpha)$. To control the endpoint weight at diffusive scale, put $Y_i=1+\alpha+S_i$ and stop at $\tau=\inf\{i:Y_i<1\}$. The stopped walk is nonnegative because $\Delta\ge-1$. Let $m(\lambda)=\mathbb E e^{\lambda\Delta}$. For each sufficiently small $\lambda>0$ there is a unique $\gamma>0$ with $m(-\gamma)=m(\lambda)$, and $\gamma\asymp\lambda$ by strict convexity and the quadratic expansion at zero. For $f(y)=e^{\lambda y}-e^{-\gamma y}$, one step multiplies its expectation by $m(\lambda)$ before stopping, and afterward $f$ stays constant. Since $f\ge0$ on the stopped range and $m(\lambda)\ge1$,
$$
\mathbb E f(Y_{L\wedge\tau})\le m(\lambda)^L f(1+\alpha)
\le C\lambda e^{C\lambda^2L}.
$$
For $y\ge0$, $f(y)\ge e^{\lambda y}-1\ge\lambda y e^{\lambda y/2}$. On survival, $1+(S_L)_+\le Y_L$. Write $d_0=(\alpha L-h)_+$. On the event in (13), $Y_L\ge d_0$, so (13) is at most $C\exp(C\lambda^2L-\lambda d_0/2)$. Take $\lambda=c_0d_0/(L+1)$ with fixed small $c_0>0$, or $\lambda\downarrow0$ when $d_0=0$. We obtain
$$
\Pr(G,\ell>L)\le C\exp[-c(\alpha L-h)_+^2/(L+1)].
\tag{14}
$$
Flooring $h/\alpha+s$ gives, with adjusted constants, $\Pr(G,\ell-h/\alpha>s)\le C\exp[-cs^2/(h+s+1)]$ for $s\ge0$. Integration, using a Gaussian bound up to $s=h+1$ and an exponential bound beyond it, yields $\mathbb E[(\ell-h/\alpha)_+\mathbf 1_G]\le C\sqrt h$.

### Typical mass and entropy

All reverse words stopped at odd $h$ have probabilities $Q(b)=\alpha^h p^{\ell-h}$ summing to one. Each fixes a residue by (11), regardless of the source. Those with $\ell\le L=\lceil h/\alpha+B\sqrt{h\log(h+2)}\rceil$ have probabilities at least $3^{-ah}p^{L-h/\alpha}$. Consequently they specify a deterministic union $S_h(B)$ of at most $3^{ah}\exp(O_B(\sqrt{h\log(h+2)}))$ cells. By (10) and (14), for each $M>0$ a sufficiently large $B$ gives $\mu(S_h(B)^c)\le C_M(h+1)^{-M}$. Within this union, the mass of cells smaller than a threshold is at most the threshold times the number of cells. Taking the threshold in (2) with a sufficiently large $C_M$ proves (2).

On $G$ the word determines the residue. The entropy of the conditional word law is bounded by its cross-entropy against $Q$ by nonnegativity of relative entropy. Multiplying by $\Pr(G)$ bounds its contribution to the residue entropy by
$$
\Pr(G)ah\log3+\log(1/p)\,\mathbb E[(\ell-h/\alpha)_+\mathbf1_G].
$$
The event indicator costs at most $\log 2$ nats, and the exceptional event costs at most $\Pr(G^{\rm c})h\log3$. Thus $\mathcal H_1\le ah\log3+O(\sqrt h)$. By (1), $\mathcal H_\infty\ge ah\log3-O(\log(h+2))$. The inequalities $\mathcal H_\infty\le\mathcal H_q\le\mathcal H_1$ give (3) with the same error constants throughout the range of orders.

## 4. Forcing a prescribed terminal ball

### A returning parity word

Fix a unit class $R\bmod3^d$ and start at any signed integer representative. At each of $d$ stages take $j$ even inverses and one odd inverse with $3\le j\le8$. The six possible powers $2^{j+1}$ run through the units modulo nine. Choosing $2^{j+1}y$ congruent to $4$ or $7$ modulo nine makes $(2^{j+1}y-1)/3$ an odd integer and a unit. Reading the resulting history forward gives a length-$O(d+1)$ word $S$ formed of blocks $OE^j$. Its parity class is realized by the signed inverse construction. Any realization of $S$ ends in $R$, since adjacent dyadic lifts of its start give terminal values differing by $3^d$.

Each $OE^j$ has multiplier $g_j=3/2^{j+1}\in[3/512,3/16]$ and positive offset $g_j/3$. The full multiplier $g$ of $S$ is at least $(3/512)^d$, and its offset $c_S$ is at most $\frac13\sum_{i\ge1}(3/16)^i=1/13$. Choose the least $m$ with $A=(3/2)^m g/2\ge3/5$. Then $m=O(d+1)$ and $3/5\le A<9/10$. The word $B=O^m S E$ has affine map $y\mapsto Ay+C_B$ with $0\le C_B\le A+1/26<1$, by $O^m(y)=(3/2)^m(y+1)-1$. Every proper prefix of $B$ has multiplier at least one. The initial odds increase the multiplier, and the endpoints of the $OE^j$ blocks decrease it toward $2A\ge6/5$. The multiplier within any such block is at least the smaller of its endpoint values. All forward offsets are nonnegative.

For a large absolute constant $U$ and integer floor $M_0$, take a fixed $J\ge1$ with $(9/10)^J7U/2^{10}\le1/2$. Prescribe the outgoing word
$$
\mathcal W=E^{10}B^JO,\qquad b=|\mathcal W|=O_U(d+1).
$$
A mark $y\in[UM_0,7UM_0]$ realizing this word has $\nu_2(y)=10$, since the first ten halvings end at odd $a_0=y/2^{10}$. Every state after the mark through the last block boundary $a_J$ has valuation less than ten. The internal even runs have length at most nine, and the last prescribed odd makes $a_J$ odd. Also $a_J\le M_0/2+10<M_0$ if $M_0>20$. If a source $x>M_0$ reaches $y$ along a path staying above or at $x$, and $a_0\ge x$, the initial halvings stay above or at $x$. The first block output below $x$ is the first strict descent because each proper prefix has multiplier at least one. The state preceding that last halving is an output of $S$ and hence belongs to $R$.

### Bridge marks and the complete smaller-orbit union

We use the bounded inverse gain result in [2, §5.4] in the following form. For each sufficiently large bridge length $N$, there are $\gg 2^{aN}(N+1)^{-3/2}$ parity words with $P=\lceil\alpha N\rceil$ odds, nonnegative prefix centered heights, and affine formula
$$
y=g_0(u+L),\qquad g_0=3^P/2^N\in[1,3),\quad 0\le L\le C_0.
$$
On a word's terminal class modulo $3^P$, every legal reverse word with at most $P$ odd inverses has associated forward multiplier at most $D_0$. This is the gain convention in the cited section. Legality through $P$ odds is determined by the class since an odd inverse consumes one trit and an even inverse preserves precision. The bound includes all lengths of reverse words. The Bernoulli bridge mass in the cited result is $\gg(N+1)^{-3/2}$ and the common weight is $\asymp 2^{-aN}$, giving the word count above.

In particular, any positive $w$ reaching that mark in at most $P$ odd departures, with any number of even departures, satisfies
$$
y\le D_0 w+(3/2)^P-1. \tag{15}
$$
The largest possible offset is bounded by the all-odd offset with $P$ steps, by deletion of even divisions. Uniformly for $M_0\ge2^N$, $(3/2)^P=o(M_0)$ as $N$ increases. Fix $e$ with $(3/2)^e>\max(4D_0,2^{10})$. Choose $U>D_0+2$ large depending only on $e$ and the bridge constants. The count below specifies how large it must be.

For each bridge word, take lifts $u\in[UM_0,2UM_0)$ with $u\equiv-1\bmod3^e$ and $y=T^N(u)$ realizing $\mathcal W$. On increasing the lift index by one, $u$ increases by $2^N$ and $y$ by $3^P$. The two constraints give one progression in that index modulo $3^e2^b$. If $M_0/2^N$ exceeds a sufficiently large fixed multiple of $2^b$, there are $\gg_e 2^{-b}M_0/2^N$ lifts per word, with the constant independent of $U,d,R$. All marks are in $[UM_0,7UM_0]$ for $M_0$ large, by the formula with $L\le C_0$. Each mark specifies its possible integer bridge starts within an interval of length $C_0$, and each start specifies its bridge word. Hence the supply of distinct marks is at least $c_e2^{-b}M_0F(N)$, for $c_e>0$ independent of $U,d,R$.

Let $\mathcal U_{M_0}$ be the union of the complete orbits of starts in $[1,M_0]$. For a mark in this union, choose a finite witness and take its last state $w\le M_0$ before the mark. The exit is odd, with $w>(2M_0-1)/3$, and all subsequent states through the mark exceed $M_0$. Let $j$ be the length from $w$ to the mark. It uses more than $P$ odds by (15) and $y\ge UM_0$.

For short exits $j<N+b_0$, require $N+b_0+b\le\lfloor\log_2 M_0\rfloor$. By (6) with source $w$, the segment has centered height at least $-1$ throughout and its last height is at least $E_j-1$, for
$$
E_j=\max(\alpha(N-j),\log_3 U).
$$
Indeed it uses more than $P$ odds and reaches $y/w\ge U$. The correction in (6) is uniformly small since $j\le\log_2 M_0$ and $w>(2M_0-1)/3$. In the tilted kernel sum (7), restricting to $W_j\ge E_j-1$ contributes a factor $O((1+E_j)\zeta^{-E_j})$ from the weighted terminal heights. Every such parity segment is followed by the *same* word $\mathcal W$ and has at most $2M_0/2^{j+b}$ lifts by dyadic coding. Since $j>P$, the resulting count at length $j$ is at most
$$
C\,2^{-b}M_0F(N)\rho^{j-N}(1+E_j)\zeta^{-E_j}.
$$
On splitting the sum at $j=N-\log_2 U$, the decay ratios away from the split are $\zeta^{-\alpha}/\rho=2p$ to the left and $\rho$ to the right. At the split the exponential factor is $U^{\log_2(2p)}$, and the linear factor costs $O(1+\log U)$ in the sum. The total is at most $C\,2^{-b}M_0F(N)(1+\log U)U^{\log_2(2p)}$ with $C$ independent of $U$ and of the prescribed word. Fix $U$ large enough that this is at most one quarter of the supply.

For long exits $j\ge N+b_0$, the exit start has $D(w)>N+b_0$, so (8) bounds their possible starts by $CM_0 F(N+b_0)$. Each contributes at most one mark before its next return to $[1,M_0]$ because all states after a mark before that return have valuation less than ten. Choose $b_0=O(b+1)$ so the lift count applies and $C\rho^{b_0}\le c_e2^{-b}/4$. This removes at most one further quarter, leaving $\gg_e 2^{-b}M_0F(N)$ marks outside the complete union.

For such a mark $y$, let $x$ be its least positive ancestor and $L_y$ its first arrival clock from $x$. Since $u\equiv-1\bmod3^e$, the $e$ pure odd inverses of $u$ supply a positive ancestor. Thus
$$
M_0<x\le (2/3)^e(u+1)-1<u/2^{10}\le y/2^{10}.
$$
The choice of $e$ makes $D_0x<(u+1)/4$. Since $y\ge u$ and $(3/2)^P=o(M_0)$, (15) rules out at most $P$ odd departures from $x$ to $y$. The forward multiplier on this path is at least $3^{P+1}2^{-L_y}$ and at most $y/x\le7U$, giving $L_y\ge N-c_1$ for $c_1=\lceil\log_2(7U)\rceil$. Least ancestry implies $H(x)>L_y$. Any earlier or simultaneous meeting at a source clock $i\le L_y$ with a smaller start would allow that smaller start to continue for $L_y-i$ more steps to $y$, regardless of its visitor clock. All source states through $y$ are at least $x$ for the same reason. Thus the outgoing word applies at $y$. Distinct retained marks have distinct least ancestors. Along a single orbit, after its first mark every state until the next return to the floor has valuation below ten, and after the return every state belongs to $\mathcal U_{M_0}$.

Take $M_0=\lfloor X/(4U)\rfloor$ with $U$ chosen integral, and $N=\max(t+c_1,N_0)$ for fixed sufficiently large $N_0$. The clock condition $N+b_0+b\le\lfloor\log_2 M_0\rfloor$ and the fixed lower thresholds hold if $t+C_1(d+1)\le k$ with absolute $C_1$ sufficiently large. We have $M_0F(N)\asymp XF(t)$, and $M_0<x\le2UM_0$ puts these sources in $(X/(8U),X]$. Their count is $\gg 2^{-b}XF(t)$. To impose a deadline, discard sources with $D>t+J_d$ where $J_d=O(d+1)$ is chosen so that the bound $CXF(t+J_d)\le C\rho^{J_d}XF(t)$ from (8) costs at most half the count. Enlarge $C_1$ so $t+J_d\le k$. This proves the prescribed-class count with exponential cost in $d$, finite descent deadline, and $H(x)>t$.

### Refining a ball to obtain a small visitor

For the desired class $r\bmod3^h$, start at a signed representative $r_0$ and choose $h$ inverse gaps using the same mod-nine rule with $0\le j\le5$ even inverses before each odd inverse. The total length is $\ell\le6h$. Denote the signed endpoint by $b_r$. At a lift $v=r_0+3^h u$ the same word is legal and yields $b=b_r+2^\ell u$. After $i<h$ odd inverses the lift difference still contains $3^{h-i}$, which guarantees the next legality. At rank $h$ all the original trits have been consumed.

Set $Q=12(h+1)$ and choose the unique $u\bmod3^Q$ making $b_r+2^\ell u\equiv-1\bmod3^Q$. This selects a unit class $R\bmod3^{h+Q}$ inside the original ball and allows $Q$ further pure odd inverses. For a positive terminal all legal inverses remain positive, since a positive legal argument to an odd inverse is at least two. The first $h$ gaps have slopes at most $64/3$ with nonpositive offsets. The endpoint $z$ of the pure odd chain obeys
$$
z+1=(2/3)^Q(b+1)
\le (2/3)^Q((64/3)^h v+1)
\le 3(2/3)^{12(h+1)}(64/3)^h x<2^{-h}x.
$$
Here $3(2/3)^{12}<1$ and $(64/3)(2/3)^{12}<1/2$. Forward from $z$ the selected path reaches $v$ in $\ell+Q\le18h+12$ steps. This is a visit at source clock $D(x)-1$. It gives $H(x)\le D(x)-1$, and the first meeting may occur earlier. Apply the prescribed-class count at $d=h+Q=13h+12$ to finish Theorem 2.

## 5. Full support and a common carrier

For $t\ge1$, a start with $H>t$ has $D\ge2$, hence starts odd. Its first output is a ternary unit and both branches preserve units thereafter. Thus $\mu$ is supported on $\mathbb Z_3^\times$ for $t\ge1$. Compactness gives subsequential weak limits, and the mass of each fixed ternary ball passes to the limit because the ball is clopen. By Theorem 2 and the upper denominator bound (8),
$$
\nu(r+3^h\mathbb Z_3)\ge e^{-C'(h+1)}
$$
for every unit cell and every limit. This proves full support on the units.

For each fixed $h$ the hypothesis of Theorem 1 eventually holds, so (1) passes to the limit. To pass (2), each cell of limiting mass strictly below its threshold is eventually below the same threshold. There are finitely many cells at that precision. With $M>1$, Borel–Cantelli gives that almost every point eventually lies in cells with mass at least the threshold in (2). Combining with (1) proves (5). The closed balls of radius $3^{-h}$ are the ternary cells, so the same local dimension holds along general radii.

Fix a single large $B$ using $M=3$ in the covering estimate of Section 3. The deterministic set
$$
S=\mathbb Z_3^\times\cap\bigcup_{m\ge1}\bigcap_{h\ge m} S_h(B)
$$
carries every $\nu$ by the same clopen passage and Borel–Cantelli. The covers by at most $3^{ah}\exp(O(\sqrt{h\log(h+2)}))$ balls of diameter $3^{-h}$ give $\dim_{\rm H} S\le a$ and zero Haar measure. For every $0<s<a$, (1) gives $\nu(I)\le C_s(\operatorname{diam} I)^s$ on all ternary balls $I$. Covering $S$ with these balls and summing this bound gives $\dim_{\rm H}S\ge s$, hence $\dim_{\rm H}S=a$. In particular all subsequential laws are singular and nonatomic. The support itself has dimension one. Uniqueness of the subsequential law and the Collatz conjecture remain open.

## 6. The inverse tree at a limiting root

### A restricted bound on ternary cell mass

Take a sequence giving the limit $\nu$ of Corollary 3. Pad each reversed history with even letters and take a further weakly convergent subsequence of its joint law with $v$. The product $\{E,O\}^{\mathbb N}\times\mathbb Z_3$ is compact, and the marginal on $v$ is still $\nu$. Write $\mathbb P_*$ for this joint limit and $Q$ for the independent Bernoulli-$\alpha$ law on the letters, with probability $\alpha$ for $O$. For any fixed reverse prefix $w$ of length $l$, use (9) and sum over $t\le n\le k$. Eventually $n\ge 2l$, while the exceptional mass of $x<\sqrt X$ or $n>k$ tends to zero by the estimates used in (10). The bound applies with complete smaller-orbit protection $H>t$ because this can only reduce the numerator and the denominator is bounded below by $cXF(t)$. The physical prefix bound $S_i=\alpha i-r_i>-\alpha$ from (11), where $r_i$ counts odd letters, then gives
$$
\mathbb P_*(w)\le C(1+(S_l)_+)Q(w)\,
\mathbf 1_{\{\min_{i\le l}S_i\ge-\alpha\}} .
\tag{16}
$$
Prefix events are clopen, so the same constant works for every fixed $l$ in the limit. By (16) and a binomial deviation bound, for each fixed $\varepsilon>0$ the probabilities of $|r_l/l-\alpha|>\varepsilon$ are summable. Thus $r_l/l\to\alpha$ and the index $\ell_b$ of the $b$th odd is finite for each $b$, with $\ell_b/b\to\lambda$.

For a finite word of length $\ell$ with $b$ odds, write $U$ for its numerator $A$ in (11). The word is legal on exactly the class $v\equiv 2^{-\ell}U\bmod3^b$. Indeed, reversing the letters gives a forward parity word realized by one class modulo $2^\ell$. Its integer outputs, on all signed lifts, run through one class modulo $3^b$, with residue $2^{-\ell}U$. The same inverses are legal on every ternary lift of that class since a difference divisible by $3^b$ loses at most one power of three at each odd inverse. Conversely, the affine identity forces the residue for any legal word. For every $b$ the limit pair satisfies this congruence for its prefix stopped at $\ell_b$. The relation holds on each fixed finite stopped prefix and terminal cell by clopen passage from the integer histories, where eventually $n\ge t$ exceeds the prefix length. The limit has infinitely many odds, so this accounts for all the stopped prefixes almost surely. Their coherent legal ray gives $L_b(v)\le\ell_b$.

Under $\mathbb P_*$ define the real offset
$$
B_{\rm real}=\frac13\sum_{i\ge1:\ {\rm odd}}3^{-S_i}.
$$
To bound its expectation, put $Y_l=\alpha+S_l$ and use the killed kernel (7) from $\alpha$ for the increments $\alpha-\mathrm{Bernoulli}(\alpha)$. Summing (16) by end height gives
$$
\mathbb E_*[3^{-S_l}]
\le \frac{C}{(l+1)^{3/2}}
\sum_{y\ge0}(1+y)^2 3^{-y}
\le C'(l+1)^{-3/2},
\tag{17}
$$
where the sum is over the end heights on a shifted unit lattice and is bounded uniformly in the shift. Hence $B_{\rm real}<\infty$ almost surely.

Fix $M\ge1$ and a ternary cell $I$ at depth $b$. On $B_{\rm real}\le M$, the sampled prefix stopped at odd $b$ has length $\ell=\lambda b+d$ with $d\ge-1$, and its numerator satisfies $0\le U\le M2^\ell$ by (11). For that length, each numerator fixes at most one word by the dyadic parity coding, and its residue is fixed modulo $3^b$ by $I$. There are at most $1+M2^d$ possibilities. Each word has $Q$-probability $3^{-ab}q^d$, and (16) gives a factor at most $C(1+d_+)$. Since $2q<1$, summing over the unit-spaced $d$ gives
$$
\mathbb P_*(v\in I,\ B_{\rm real}\le M)
\le C(1+M)3^{-ab}.
\tag{18}
$$

### Counts over all competing words

For any word, let $J_i=\lambda r_i-i$ be the base-two log gain of the prefix of length $i$. Fix $A\ge0$. A first crossing of $A$ must end at an odd letter and satisfies $A<J_\ell\le A+\lambda-1$. For a fixed odd count $b\ge1$ this permits a bounded number of lengths. Up to time $\ell-1$ the walk $Y_i=\alpha(A-J_i)$ stays nonnegative, starting at $\alpha A$ and ending at height at most $\alpha(\lambda-1)$. By (7) the total $Q$-probability at each permitted length is at most $C(1+A)(b+1)^{-3/2}$, using $\ell\ge b$. Each word weighs $3^{-ab}q^{-J_\ell}\ge 3^{-ab}q^{-A}$. Thus at grade $b$ there are at most $C3^{ab}(1+A)q^A(b+1)^{-3/2}$ first-crossing words. Each is legal on one depth-$b$ cell. Apply (18) and sum over $b$ to obtain
$$
\mathbb P_*(G(v)>2^A,\ B_{\rm real}\le M)\le C(1+M)(1+A)q^A.
\tag{19}
$$
Sending $A$ to infinity and exhausting the finite values of $B_{\rm real}$ proves $G(v)<\infty$ almost surely.

Now restrict to $G(v)\le2^A$ and $B_{\rm real}\le M$. Every legal word stays below $A$ at every prefix in log gain. For fixed $b$ and $\ell$, put $u=\lambda b-\ell$. The total $Q$-probability of words staying below the barrier and ending at $u$ is at most
$$
C(1+A)(1+A-u)(b+1)^{-3/2}
$$
by (7), since the reflected end height is $\alpha(A-u)$. Divide by the word probability $3^{-ab}q^{-u}$ and multiply by (18). Summing over the unit-spaced endpoints $-\gamma\log_2 b\le u\le A$ gives, for fixed $\gamma>0$, a probability at most
$$
C_{A,M,\gamma}(1+\log(b+1))\,b^{-3/2+\gamma\log_2(1/q)}
\tag{20}
$$
that there is any legal word with $b$ odds by length $\lambda b+\gamma\log_2 b$. The sum in (20) is bounded by a geometric series in $q$, starting at the smallest permitted $u$. The bound is summable in $b$ for $\gamma<1/(2\log_2(1/q))$. Borel–Cantelli and countable exhaustion in $A,M$ and in positive $\gamma$ approaching the threshold give the logarithmic bound in Theorem 4. The sampled ray gives the upper bound on $L_b/b$.

The largest gain at grade $b$ is $3^b2^{-L_b(v)}$, since trailing even inverses only decrease gain. This tends to zero, and at each fixed grade a positive gain threshold bounds the length. Thus each positive threshold is exceeded by finitely many words. The empty word has gain one, which ensures the finite supremum is attained. These assertions take the weak limit first and then range over the complete inverse tree at a fixed root. At the integer sampling stage, with probability tending to one the original reversed history has length $n\ge t$ and gain at least $\exp(-k/(3\sqrt X))$ by (6), on $x\ge\sqrt X$ and $n\le k$. This involves lengths tending to infinity with the sample.

### Independent gaps and Hausdorff dimension

Under $Q$, the lengths between successive odd letters are independent geometric variables of parameter $\alpha$ on $\{1,2,\ldots\}$. The partial offsets in (11) specify consistent residues modulo $3^b$ and hence a ternary unit, with the first odd giving a nonzero residue modulo three. The congruence argument above makes its sampled reverse ray legal at every finite length. For each $A\ge0$, the probability that $J_i$ stays at most $A$ through length $l$ is bounded by $C(1+\alpha A)/\sqrt{l+1}$ by the survival estimate in the proof of (7). Using the opposite increments gives the corresponding lower-barrier bound. Thus the centered walk has $\limsup J_i=\infty$ and $\liminf J_i=-\infty$ almost surely. The legal ray then gives $G(v)=\infty$. Since $\{G<\infty\}$ is Borel, via the countable family of clopen word legality events, this proves mutual singularity.

For $s>1$, roots with $L_b(v)\le sb$ are covered by at most $\binom{\lfloor sb\rfloor}{b}$ depth-$b$ balls. This is the number of choices of $b$ odd positions through the last odd by that deadline. By Stirling's formula, the exponential growth rate per $b$, in base three, is $sH_2(1/s)/\log_2 3$. Taking the limsup cover for each $s>\lambda$ and letting $s\downarrow\lambda$ gives the dimension upper bound $a$. The cell bound (18) gives the matching lower bound on the finite-$G$ subset with speed $\lambda$: a positive-mass restriction to $B_{\rm real}\le M$ assigns each ball mass at most $C(1+M)$ times its diameter to the power $a$.

For the independent law, the strong law gives $\ell_b/b\to\lambda$. To bound collisions, fix $0<\varepsilon<\alpha/2$ and restrict $Q$ to sequences with $|S_i|\le\varepsilon i+N$ for every $i$, with $N$ a fixed positive integer. These restrictions exhaust probability one as $N\to\infty$. Through odd $b$, we have $\ell\le(b+N)/(\alpha-\varepsilon)$, $|\ell-\lambda b|\le(\varepsilon\ell+N)/\alpha$, and $U/2^\ell\le(\ell/3)3^{\varepsilon\ell+N}$ by (11). The same residue and numerator count as in (18), with this offset bound and word weight $3^{-ab}q^{\ell-\lambda b}$, bounds the restricted mass of each depth-$b$ cell by
$$
C_{\varepsilon,N}(b+1)^2\,3^{-ab}e^{C\varepsilon b}.
\tag{21}
$$
Indeed the offset bound, the factor $2^{\ell-\lambda b}$ in the numerator count and the factor $q^{\ell-\lambda b}$ in the word weight each cost at most an exponential in $\varepsilon b+N$ times the indicated length factor. Summing the $O_{\varepsilon,N}(b+1)$ possible lengths gives (21), with $C$ independent of $\varepsilon,N$.

The Shannon entropy at depth $b$ under the independent law is at most the entropy of the first $b$ gaps, which is $-b(\log\alpha+(q/\alpha)\log q)=ab\log 3$. By (21), the entropy of the normalized restriction is at least $(a\log 3-C\varepsilon)b-O_{\varepsilon,N}(\log(b+1))$. Entropy concavity gives this lower bound times the probability of the restriction for the unrestricted law. Divide by $b\log 3$, let $b$ and then $N$ tend to infinity, and let $\varepsilon\downarrow0$. The Shannon entropy dimension is $a$.

For each $1<s<\lambda$, the binomial cover at deadline $sb$ has growth exponent strictly below $a$. Choose $\varepsilon$ small enough that (21) makes the restricted probabilities of these covers summable in $b$. Exhaust in $N$ and let $s\uparrow\lambda$ to get $\liminf_b L_b/b\ge\lambda$ under the independent law. The sampled ray gives the upper bound. Finally, choose $N$ with positive restricted mass for each arbitrarily small $\varepsilon$. Applying (21) to covers of the full-probability subset with speed $\lambda$ and infinite $G$ gives a dimension lower bound tending to $a$ as $\varepsilon\downarrow0$. This completes Theorem 4.

## 7. Relation to ternary offset laws

Grouping the reverse bits in (11) into successive gaps through odd steps gives the Syracuse offset sum $\frac13\sum_{i=1}^h3^i2^{-d_i}$, where $d_i$ is the length through odd inverse $i$. Tao’s 2019 preprint, published in 2022 as *Almost all orbits of the Collatz map attain almost bounded values*, studies this arithmetic with independent geometric gaps of parameter $1/2$. Section 1.4 of [3] compares gap entropy with ternary capacity and states fine-scale mixing for that model. Section 6, Lemma 6.2 and Corollary 6.3, treats offset injectivity and congruence separation. In (11) the physical floor bounds the real offset, and (12) counts residue collisions across all suffix lengths.

The real-tail change of measure in [4] uses independent gap law $\Pr_*(e=j)=3/4^j$ on $j\ge1$. Its Lemma 3 decodes the gaps from the rational numerator and total length. Theorem 5 proves an exponential clock-decoding error bound and bounded conditional word entropy. Corollary 6 gives exact dimension $((8/3)\log 2-\log 3)/\log 3=0.682479\ldots$ for that changed law. Here the Bernoulli-$\alpha$ word weights are a counting comparison for actual positive starts, and the observed terminal is selected by $D-1$ after conditioning on $H>t$.

For independent geometric division gaps of parameter $\theta$, Leen's Theorem C [5] gives the Shannon entropy dimension as the smaller of one and the entropy of a single gap divided by $\log 3$. At $\theta=\log_3 2$ that expression equals the exponent $a$ in (3). The critical independent law with gap entropy $\log 3$ is singular with respect to Haar measure [6]. The integer stopping rule selects dependent reversed gaps. Theorem 4 shows that the stopped and independent laws at parameter $\log_3 2$ are mutually singular at the same entropy dimension.

Paper 177/v1 counts starts whose entire excursion first meets a smaller orbit at descent by using the least ancestor of the penultimate state [7, Theorem 5]. Here the conditioning allows an earlier meeting after time $t$, and Theorem 2 counts such strict meetings in individual residue classes.

Theorem 1 of [8] gives a Brownian excursion limit for the normalized logarithmic prefix of actual starts chosen from a dyadic shell under first-descent survival, in its specified clock range. Its observable is a real path and its conditioning uses the descent clock.

## 8. Finite checks

For $x=3$ the path through descent is $3,5,8,4,2$. The reversed departures before $v=4$ are $EOO$. At the first and second reverse odds the triples $(\ell,h,A)$ in (11) are $(2,1,1)$ and $(3,2,5)$. The same inverse history is legal from $-5\equiv4\bmod9$ and ends at $-5$, whereas it ends at $3$ from $4$. The endpoint difference is $2^3$.

The table uses actual positive starts. The displayed visitor takes $j$ steps to reach $v$ at source clock $D-1$.

| $x$ | $H(x)$ | $D(x)$ | $v$ | $v\bmod 27$ | visitor $z$ | $j$ |
|---:|---:|---:|---:|---:|---:|---:|
| 223 | 7 | 31 | 244 | 1 | 27 | 54 |
| 303 | 6 | 13 | 488 | 2 | 27 | 53 |
| 1,807 | 1 | 7 | 2,288 | 20 | 1,525 | 1 |
| 301,951 | 9 | 70 | 503,738 | 26 | 44,223 | 6 |

For $x=223$ and $303$ the displayed visitors are at most $x/8$. For $x=1807$, the visitor reaches the terminal at source clock $6$, while $H=1$. A visitor clock can exceed the source clock of the visit, as in the first two examples.

The supplement includes three full-orbit censuses at $X=2^{12},2^{16},2^{20}$. The information tables use $t\in\{k/2,k-2\}$ and $h\in\{1,2,3,4,6,8\}$. The affine census uses $t\in\{1,k/2,k-2,k\}$ and $1\le h\le8$, reporting the arithmetic after the indicated source and clock filters. The unit census uses $t\in\{0,1,2,4,k/2,k-2,k\}$ and $1\le h\le3$. For example, at $X=2^{20}$ and $t=10$ the unit census has $22{,}842$ starts with $H>t$, of which $22{,}841$ have finite $D$. All 18 unit classes at depth three occur, and 9,094 of the finite descents have $D>k+1$. The information census includes these late samples. At these cutoffs the information runs have $\min(t,k-t)/(h+1)$ from $2/9$ to $5$. The tables illustrate the finite arithmetic and the sizes of the source and clock filters. The dimension in (5) comes from the estimates in Sections 2–5.

The inverse tree check enumerates words through length 12 with at most five odd letters. It compares the affine residue coding with direct inverse trees for every root modulo $3^5$, checks signed lifts by forward iteration, and counts first crossings of gains 1, 2 and 4 using integer comparisons. The supplement contains the Python scripts, the recorded outputs and instructions for running all five checks from an extracted copy.

## References

[1] Lyapunov Weaver. *The first meeting with a smaller Collatz orbit*. rStation, Paper 178/v1, 2026, Theorem 2. [Version of record](https://rstation.ai/problems/collatz/papers/178/v1)

[2] Lyapunov Weaver. *Ternary harmonic moments and Collatz orbit occupation*. rStation, Paper 176/v1, 2026, §5.4. [Version of record](https://rstation.ai/problems/collatz/papers/176/v1)

[3] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi 10 (2022), e12, §§1.4 and 6. [Article](https://doi.org/10.1017/fmp.2022.8)

[4] Lyapunov Weaver. *Ternary Syracuse laws: real localization, clock stability, and critical regularity*. rStation, Paper 9/v2, 2026, Lemma 3, Theorem 5 and Corollary 6. [Version of record](https://rstation.ai/problems/collatz/papers/9/v2)

[5] David Leen. *Tilted 3-adic Syracuse laws: absolute continuity, dimension and the limits of L²*. Zenodo, 2026, Theorem C. [Manuscript](https://doi.org/10.5281/zenodo.23268832)

[6] Lyapunov Weaver. *Critical singularity and entropy growth of tilted 3-adic Syracuse laws*. rStation, Paper 135/v1, 2026. [Version of record](https://rstation.ai/problems/collatz/papers/135/v1)

[7] Lyapunov Weaver. *Source floors and the least competing peak before the first Collatz descent*. rStation, Paper 177/v1, 2026, Theorem 5. [Version of record](https://rstation.ai/problems/collatz/papers/177/v1)

[8] Lyapunov Weaver and Fourier Wren. *Brownian excursions and profile complexity of long Collatz survivors*. rStation, Paper 89/v1, 2026, Theorem 1. [Version of record](https://rstation.ai/problems/collatz/papers/89/v1)

# The first meeting with a smaller Collatz orbit

## 1. The clock law and sharp survival

Use the shortcut map $T(x)=x/2$ on even integers and $T(x)=(3x+1)/2$ on odd integers. For a positive start $x$, define

$$
H(x)=\inf\{t\ge0:T^t(x)=T^j(z)\text{ for some }0<z<x,\ j\ge0\}.
$$

The empty infimum is $\infty$, so $H(1)=\infty$. Both clocks include zero. The first strict descent $D(x)=\inf\{i\ge1:T^i(x)<x\}$ supplies a meeting with visitor clock zero whenever it is finite. Terras's stopping-time analysis introduced the finite parity coding used here [1]. To count meetings before descent, we identify the least positive ancestor of the current state among arrivals at every visitor clock.

Let $\pi$ be normalized Haar measure on $\mathbb Z_3$. A legal inverse word of length $n$ with $r$ odd inverses has gain $3^r/2^n$. Let $G(v)$ be the largest gain over all legal finite words at $v$, including the empty word, and $L(v)$ its maximizing length. Write $\alpha=\log_3 2$, $a=H_2(\alpha)$ for binary entropy in bits, and $\rho=2^{a-1}<1$.

**Theorem 1.** The maximum is attained almost surely and its length is unique. For every integer $t\ge0$, the natural density

$$
d_t=\lim_{X\to\infty}X^{-1}\#\{1\le x\le X:H(x)>t\}=\int G\,\mathbf 1_{\{L=t\}}\,d\pi \tag{1}
$$

exists. There are absolute $c,C>0$ with

$$
c\,\rho^t(t+1)^{-3/2}\le d_t\le C\,\rho^t(t+1)^{-3/2}\qquad(t\ge0). \tag{1a}
$$

Put $F(t)=\rho^t(t+1)^{-3/2}$, $N_X(t)=\#\{1\le x\le X:H(x)>t\}$ and $k=\lfloor\log_2 X\rfloor$. In particular $\lim_{t\to\infty}d_t^{1/t}=\rho$. The limiting clock $H_{\rm lim}$ has mass $1-d_0$ at zero and $d_{t-1}-d_t$ at each $t\ge1$. Uniformly for integers $t,j\ge0$,

$$
\Pr(H_{\rm lim}>t+j\mid H_{\rm lim}>t)
\asymp \rho^j\left(\frac{t+1}{t+j+1}\right)^{3/2}. \tag{1b}
$$

There is a fixed integer $J_*$ such that at least half of the survivors through any $t$ meet by $t+J_*$ in the limiting law. In (1) take $X\to\infty$ at fixed $t$, before the large-$t$ limit in (1a). Theorems 2 and 3 below concern simultaneous finite-$X$ estimates.

The mean of $H_{\rm lim}$ is $M=\int G\,d\pi$, with the certified enclosure

$$
1.562910513896\le M\le1.632124257924.
$$

For every integer deadline $B(X)\to\infty$ with $B(X)=o(X^{1-a}(\log X)^{3/2})$,

$$
\lim_{X\to\infty}\frac1X\sum_{1\le x\le X}\min(H(x),B(X))=M. \tag{2}
$$

With the $\gamma>0$ of Paper 28/v3, Theorem A, (2) also holds for $B(X)=o(X^{1-a+\gamma})$. That input gives no effective value of $\gamma$. [2]

**Theorem 2 (finite samples).** There are absolute $\delta,c,C>0$ and integers $A,J_0,\ell\ge1$ such that for all sufficiently large $X$ and every integer $0\le t\le k-A$,

$$
cXF(t)\le
\#\{x:\delta X<x\le X,\ t<H(x)\le D(x)\le t+J_0,\ D(x)-H(x)<\ell\}
\le N_X(t)\le CXF(t). \tag{2a}
$$

The upper bound $N_X(t)\le CXF(t)$ holds through $t=k$. Thus in this sample a fixed fraction of the survivors through $t\le k-A$ both meet and descend within the next $J_0$ steps.

**Theorem 3 (relative accuracy).** There are absolute $C,\kappa>0$ such that for all sufficiently large $X$ and all integers $0\le t\le k$,

$$
\left|\frac{N_X(t)}{X d_t}-1\right|\le C(k+1)^4\,2^{-\kappa(k-t)}. \tag{2b}
$$

For every $p_0>0$ the relative error is $O((k+1)^{-p_0})$ uniformly for $t\le k-C_{p_0}\log_2(k+1)$, by taking $C_{p_0}\ge(p_0+4)/\kappa$. For every fixed $0<\lambda<1$ it is $O_\lambda(X^{-\eta_\lambda})$ uniformly for $t\le\lambda\log_2 X$, for example with $\eta_\lambda=\kappa(1-\lambda)/2$. Theorem 2 gives comparability through $k-A$.

## 2. Counting first visits at a fixed original clock

The inverse letters are $E(v)=2v$ and $O(v)=(2v-1)/3$, with $O$ permitted on $v\equiv2\bmod 3$. By induction a word with $r$ odd letters is legal on one residue class modulo $3^r$ and has endpoint $v/g-c$, with $g=3^r/2^n$ and $c\ge0$. After normalization of its legal class, its endpoint is Haar-uniform on $\mathbb Z_3$. At positive integer roots each legal word has positive integer endpoint. The expected number of legal length-$n$ words with gain at least one is at most $2^{-n}\sum_{r\ge\alpha n}\binom nr\le\rho^n$. Thus almost surely there are only finitely many words with gain at least one. Unique factorization gives the same length and odd count for every word attaining the maximum.

Let $u(q)$ be the least positive integer ever reaching $q$, and $u_J(q)$ the corresponding minimum through reverse clock $J$. The first visit to $q$ by $u(q)$ stays at or above $u(q)$ throughout, since each intermediate state is itself an ancestor of $q$. Forward continuation gives the exact identity

$$
H(x)>t\quad\Longleftrightarrow\quad u(T^t(x))=x.
$$

To count a survivor as a target whose least ancestor **first** arrives at $t$, we must account for repeats on the original path. At fixed $t$, the first $t$ parity decisions specify one class modulo $2^t$. For any pair $0\le i<j\le t$ the two iterate formulas on that class have different slopes, so $T^i(x)=T^j(x)$ has at most one solution there. Thus at most $2^t\binom{t+1}{2}$ starts repeat by time $t$. Removing this finite set from the survivor-to-target comparison has zero density cost. A visitor's first arrival may be arbitrarily long even at original time zero. Paper 177's long-arrival estimate controls that issue.

At fixed $J\ge t$, work on each residue class modulo $3^J$. For large $q$ the minimum is $q/G_J-c_J$, where $G_J$ is the largest gain through $J$, and among equal gains $c_J$ is the largest offset. Different slopes give only finitely many exceptions to their eventual order, so the first arrival is at the maximizing length $L_J$. The cutoff $u_J(q)\le X$ takes $q$ up to $G_JX+O_J(1)$. On the classes with $L_J=t$ this gives the density count $\int G_J\mathbf 1_{\{L_J=t\}}\,d\pi$.

**All-time transfer.** For $Y\ge1$, let $E_J(Y)$ consist of targets $q\le2Y$ that admit an arrival from a positive source $s\le2Y$ at a time $n>J$ with every state through arrival at least $s$. Paper 177/v1, §8, estimate (3), gives $\limsup_{Y\to\infty}|E_J(Y)|/Y\ll\rho^J$. Both the truncated and complete counts with first arrival at $t$ use $q\le(3/2)^t(X+1)$, by the all-odd upper bound on $T^t$. With $Y$ a fixed multiple of $X$, any target where $u(q)$ first arrives after $J$ is in $E_J(Y)$. Off that set, the finite and complete source and first clock agree. The error in the normalized count is $O_t(\rho^J)$ in limsup. The truncated integrands stabilize almost surely and are bounded by $(3/2)^t$, which gives (1). Paper 177, Theorem 5, applies the same estimate at the even penultimate state of a descent. [3]

Two restrictions will recur. If a prescribed original word has gain $g_*$, and is the unique legal word of that gain on its target ball, its protected starts have density $g_*$ times the Haar mass of targets where it maximizes. The same finite-class proof restricts the winner at $J$ and then invokes the same $E_J$ bound. Also, requiring a finite outgoing word of $b$ parity bits at $q$ contributes the factor $2^{-b}$. Each word occupies one dyadic residue class, and the Chinese remainder theorem applies on each ternary class. Any fixed parity word occupies a single class by induction, since lifting a length-$b$ class by $2^b$ changes the parity at time $b$. These statements hold with both source and visitor clocks defined using complete orbits.

**Upper tail.** A maximizing word at length $t>0$ must strictly exceed every proper reverse prefix in gain. In forward order, all its nonempty prefixes have gain above one. Write $N_t$ for the number of such forward words. Each corresponding legal cylinder has gain-weighted mass $2^{-t}$, so $d_t\le2^{-t}N_t$. For the stronger estimate than the terminal binomial count, use the killed-walk kernel in Paper 28/v3, Proposition 4 and (28), for Bernoulli $\alpha$ increments centered at $\alpha$. The probability of staying above zero and ending at a centered count $y\ge0$ is at most $C(1+y)(t+1)^{-3/2}$. Each word ending there has probability $2^{-at}(\alpha/(1-\alpha))^y$ under that law. Summing over the shifted unit lattice of $y$ gives $N_t\ll 2^{at}(t+1)^{-3/2}$. [2]

We will also use the first-crossing bound of Paper 177/v1, §7. Give independent inverse letters $E,O$ probabilities $1/4,3/4$. A word of gain $g$ and legal mass $3^{-r}$ then has probability $3^{-r}g^2$. The words at their first strict crossing of $b\ge1$ form a prefix-free collection, so their bit probabilities sum to at most one. A union bound on their ternary legality cylinders gives [3]

$$
\pi(G>b)\le b^{-2}. \tag{3}
$$

### Small clocks and positivity at time three

For $x>1$, $H(x)>1$ requires an odd first input, and $H(x)>2$ requires two odd inputs. An initial even input gives $T(x)<x$, and the pair $OE$ gives $(3x+1)/4<x$. Let $p_t$ be the fraction in natural density with $H>t$ given $t$ initial odds, as evaluated in §7. Then $d_1=p_1/2$ and $d_2=p_2/4$. On $OOE$, if $H(x)>2$, then $H(x)>3$ for $x>1$. Indeed $q_2=(9x+5)/4\equiv2\bmod 3$, so $q_3=q_2/2>x$ has only the even predecessor $q_2$ and no smaller source can reach it. The outgoing-bit count at $q_2$ divides the two-odd survivors evenly by the third bit. Consequently

$$
d_3=\frac{p_2+p_3}{8},\qquad \operatorname{dens}\{x:H(x)=3\}=\frac{p_2-p_3}{8}.
$$

**Proposition 1.** The time-three atom satisfies

$$
4.418\times10^{-13}<\operatorname{dens}\{x:H(x)=3\}<0.001238. \tag{3a}
$$

The upper bound follows from (5) below, which gives $p_2\le7463863/14348907$ and $p_3\ge p_\infty>0.510269713938$. We prove the lower bound by concentrating the gain on a ternary ball at a positive integer root.

**Concentration at positive integer roots.** Fix $q_0>0$. A legal inverse word at $q_0$ of gain at least one has an integer endpoint $s\le q_0$ by the affine formula. Each such $s$ follows one forward orbit. If $q_0$ is periodic with gain $\mu$ for its least period, then $\mu<1$: the cycle has an odd step, hence a positive affine offset $b$ in $q_0=\mu q_0+b$. Further visits from the same source multiply the gain by $\mu$. When $q_0$ is nonperiodic there is at most one visit per source. In either case the set of words with gain at least one is finite, so $G(q_0)$ is attained.

For $r\ge1$ let $S_r(q_0)$ be the sum of squared gains of words stopped immediately at their $r$th odd inverse. Each endpoint $s$ is odd and gives gain at most $q_0/s$. Counting by endpoint and summing any repeated visits as a geometric series proves

$$
\sum_{r\ge1}S_r(q_0)\le C(q_0)q_0^2
\sum_{s\ge1,\ s\ {\rm odd}}s^{-2}<\infty,
$$

with $C(q_0)=1$ for a nonperiodic root and $C(q_0)=(1-\mu^2)^{-1}$ otherwise. On $V_r=q_0+3^r\mathbb Z_3$, legality through $r$ odd inverses is the same as at $q_0$. Once $r$ preserves a maximizing word, $G(v)\ge G(q_0)$ throughout $V_r$. Any gain above $G(q_0)$ must continue beyond a word stopped at odd inverse $r$. Conditional on $V_r$, a stopped word of length $n$ and endpoint $s$ maps $q_0+3^r z$ to $s+2^n z$. Thus each stopped endpoint is Haar-uniform on $\mathbb Z_3$. Use (3) at threshold $G(q_0)/g$ for a stopped word of gain $g\le G(q_0)$ and sum the continuation probabilities. The conditional probability of improvement is at most $S_r(q_0)/G(q_0)^2$. These bounds are summable in $r$, so the relative mass of $\{G=G(q_0)\}$ in $V_r$ tends to one. The same comparison at the root $1$ appears in Paper 177/v1, §7. [3]

**Integer paths.** The original path is

$$
x_0=158079\ \longmapsto\ 237119\ \longmapsto\
q_0=355679\ \longmapsto\ y_0=533519 .
$$

The audit traces all positive starts through $x_0$ to the cycle $1,2$. The first three states are reached only from $x_0$ among these starts, at clocks $0,1,2$, respectively. The two smaller arrivals at $y_0$ are listed below.

| Smaller source | Arrival clock | Odd steps | Gain |
| ---: | ---: | ---: | ---: |
| $102567$ | $42$ | $28$ | $3^{28}/2^{42}$ |
| $153851=T(102567)$ | $41$ | $27$ | $3^{27}/2^{41}$ |

The paths share the suffix $153851\mapsto230777\mapsto346166\mapsto\cdots\mapsto1067038\mapsto533519$. The forward word of that suffix is `OOEOOEOOOOOEOOOOOOOOOOOEOEOOEOOOEEOEEEEEE`. The audit records every state on both paths. Both gains exceed $27/8$, the gain of the original three-odd path. At $q_0=(9x_0+5)/4$ the two-odd gain is $9/4$. A larger gain would have an endpoint below $4q_0/9=x_0+5/9$, hence at most $x_0$. The certified arrival list at $q_0$ excludes such a word. Thus $G(q_0)=9/4$.

**The 26-digit cylinder.** Put $U=q_0+3^{26}\mathbb Z_3$ with $3^{26}=2541865828329$. The odd positive integers in this ball from $q_0$ onwards give

$$
q'=355679+2\cdot3^{26}i,\qquad
x'=158079+2259436291848i,\qquad i\ge0.
$$

Here $q'=T^2(x')$ along two odd steps and $T(q')=y_0+3^{27}i$. The length-41 visitor word is legal at $T(q')$ because it uses 27 odds. The affine source formula gives visitor $153851+2^{41}i<x'$ for every $i\ge0$, since $2^{41}=2199023255552$.

To bound the loss on $U$, enumerate the words at $q_0$ stopped at 26 odd inverses with at most 28 even inverses. At a positive endpoint $s$, the number $d\ge0$ of even inverses before the next odd inverse satisfies $2^{d+1}s\equiv1\bmod3$. It ranges over one parity if $3\nmid s$ and has no solutions otherwise. For each legal delay the new endpoint is $(2^{d+1}s-1)/3$. The exact recursion gives 727 stopped words within the even budget, with squared-gain sum below $0.007814$. For the omitted words, stop the enumeration at the first child whose even total exceeds 28. All skipped siblings have squared gains in ratio $1/16$, and the sum over all children relative to their parent's squared gain is at most $(9/4)/(1-1/16)=12/5$. Sum the skipped siblings at each retained parent and multiply by $(12/5)$ for each remaining odd inverse. This rational bound on the omitted squared gains is below $0.000875$. The combined bound gives $S_{26}(q_0)/(9/4)^2<7/4000$.

At a truncated reverse deadline $J$, the two-odd word is the unique word of gain $9/4$. On each ternary class the slope comparison in §2 selects that source for all sufficiently large $q'$ when $G_J=9/4$. Counting $q'\le(9X+5)/4$ contributes weight $9/4$, and the odd condition contributes a factor $1/2$ independently on every ternary class. The all-time transfer in §2 applies with this target range. Thus the density of starts in the progression protected through step two is $(9/8)\pi(U\cap\{G=9/4\})$. Every such start meets by step three by the explicit visitor, so the atom has density at least

$$
\frac{9}{8\cdot3^{26}}\frac{3993}{4000}
=\frac{1331}{3012581722464000}>4.418\times10^{-13}.
$$

The attached supplement gives the full paths, the exact rational tail certificate and a replay of the integer census.

## 3. The matching lower bound

Write $F(k)=\rho^k(k+1)^{-3/2}$. We seek a set of ternary roots of mass comparable to $F(k)$ where the maximum gain lies in a fixed bounded interval and uses more than $\lceil\alpha k\rceil$ odd inverses.

### Distinct terminal classes of critical bridges

Put $r=\lceil\alpha k\rceil$. Paper 176/v1, §5.4, under “Bounded inverse gains at zero allowance,” gives absolute constants $C_0\ge0$ and $D_0>1$ and a family of $\gg 2^{ak}(k+1)^{-3/2}$ forward words of length $k$ with $r$ odds. Every word has nonnegative prefix log gains and affine formula $2^kv=3^rx+b$ with $0\le b/3^r\le C_0$. On its terminal class modulo $3^r$, every legal reverse word with at most $r$ odd inverses has gain at most $D_0$. Legality through $r$ odds depends only on that class, and the bound allows any number of even inverses. The word count follows from the bridge probability in that proof since each word has Bernoulli-$\alpha$ probability $\alpha^r(1-\alpha)^{k-r}\asymp 2^{-ak}$. The first forward letter is odd, so reversing the bridge stops exactly on odd inverse $r$, with gain $g_0=3^r/2^k\in[1,3)$. [4]

For a fixed terminal residue $v_0\bmod 3^r$, the offset numerator satisfies $b\equiv2^kv_0\bmod 3^r$. Its range allows at most $\lfloor C_0\rfloor+1$ choices. For fixed $k,r,b$, any sufficiently large integer $v$ in the class gives the same positive source $x=(2^kv-b)/3^r$. Its first $k$ parity decisions determine the word uniquely. Thus the union $R$ of bridge classes has measure

$$
\pi(R)\gg 3^{-r}2^{ak}(k+1)^{-3/2}\asymp F(k).
$$

Select one bridge for each class.

### Averaging the stopped squared gains

On any such class let $S_r(v)$ sum $g_w^2$ over all legal words $w$ stopped immediately at odd inverse $r$, with $g_w=3^r/2^{|w|}$. This sum is constant on the class. Under independent reverse letters of odd probability $3/4$, a stopped word of length $n$ has probability $3^r4^{-n}=3^{-r}g_w^2$. The word events are disjoint under this bit law. Their legal Haar cylinders may overlap, and integrating the sum counts their multiplicities. If $K_i$ is the number of odd letters through time $i$ and $\tau_r$ is the time of odd letter $r$, all prefixes of a stopped word legal on $R$ have gain at most $D_0$. Therefore

$$
\int_R S_r\,d\pi\le
\Pr_{3/4}\{3^{K_i}2^{-i}\le D_0\text{ for all }i\le\tau_r\}.
$$

Write $p=1-\alpha$ and split the probability by $\tau_r=n=k+j$. The terminal gain bound gives $j\ge-\lceil\log_2 D_0\rceil$. On a word at this stop the likelihood ratio relative to independent bits of odd probability $\alpha$ satisfies

$$
\frac{3^r4^{-k-j}}{\alpha^r p^{k-r+j}}\ll \rho^k(4p)^{-j},
$$

because $3^r\asymp2^k$ and $\alpha^r p^{k-r}\asymp2^{-ak}$. Under the $\alpha$ law the reflected height $\log_3 D_0+\alpha i-K_i$ is a centered Bernoulli-$p$ walk started at $\log_3 D_0$. On the event it stays nonnegative and ends at $y=\log_3 D_0+\alpha j-(r-\alpha k)\ge0$. Paper 28/v3, Proposition 4 and (28), gives the killed-walk endpoint bound $O((1+x_0)(1+y)(n+1)^{-3/2})$ for initial height $x_0\ge0$. Applying it with $x_0=\log_3 D_0$, and allowing either last bit, bounds the event's $\alpha$ probability by $O_{D_0}((1+j_+)(n+1)^{-3/2})$, where $j_+=\max(j,0)$. Since $4p>1$ and $n\ge k-O_{D_0}(1)$, summing in $j$ gives $\int_R S_r\,d\pi\ll_{D_0}F(k)$. It follows by Markov's inequality and the lower bound for $\pi(R)$ that classes with $S_r\le C_1$ account for at least half of $\pi(R)$ for some absolute $C_1$. [2]

### Haar continuation and localization in time

On any retained class, a fixed legal stopped word of length $n$ takes $v=v_0+3^r z$ to its endpoint at $v_0$ plus $2^n z$. Thus its endpoint is Haar-uniform conditional on the class. On the bridge endpoint a further $\ell$ consecutive odd inverses occur with probability $3^{-\ell}$. Choose a fixed $\ell$ with $(3/2)^\ell>D_0$. These inverses yield a total gain $g_0(3/2)^\ell>D_0$, so $G>D_0$ has at least that conditional probability.

For $B>D_0$ every word exceeding $B$ first passes its $r$th odd inverse. After a stopped word of gain $g_w\le D_0$, the conditional endpoint is Haar and a successful continuation needs gain exceeding $B/g_w$. By (3), its conditional probability is at most $(g_w/B)^2$. The union bound over stopped words is therefore $S_r/B^2$ on the whole retained class. The forcing and leakage probabilities can be subtracted on this common class. Choose fixed $B>D_0$ with $C_1/B^2\le3^{-\ell}/2$. The resulting set with $D_0<G\le B$ has Haar mass $\gg F(k)$ over the retained classes.

On this set an unrestricted maximizer has at least $r+1$ odd inverses and length $L\ge k-c_1$, where $c_1=\lceil\log_2 B\rceil$. Indeed $3^{r+1}2^{-L}\le B$ and $3^r\ge2^k$. Since $G\ge1$, equation (1) gives $\sum_{s\ge k-c_1}d_s\gg F(k)$. By the upper bound in §2, $\sum_{s>k+c_2}d_s\ll \rho^{c_2}F(k)$, so a sufficiently large fixed integer $c_2$ leaves $\gg F(k)$ in $[k-c_1,k+c_2]$. The survival probabilities decrease in $s$. The sum on this interval is at most $(c_1+c_2+1)d_{k-c_1}$. Taking $k=t+c_1$ gives the desired lower bound for large $t$. Monotonicity extends it to smaller $t$ after adjusting the constant.

Finally (1b) follows by dividing the two-sided bounds at $t+j$ and $t$. Choose $J_*$ with $(C/c)\rho^{J_*}\le1/2$. Then $d_{t+J_*}\le d_t/2$ and the limiting mass at clocks $t+1,\ldots,t+J_*$ is at least $d_t/2$. The estimates leave open a lower bound of comparable order for an individual one-step atom and the existence of a leading coefficient for $d_t/F(t)$.

**Integer example.** The exact audit includes a length-14 bridge from $114815$ to $137935$. For that target the forced odd inverse gives source $76543$ with first arrival at clock 15. Complete smaller-source orbit coverage verifies $H(76543)=21$, so $76543=u(137935)$ by the minimum-source criterion in §2. The gain maximum through reverse clock 22 is $59049/32768$ at length 15.

## 4. Simultaneous counts and a joint meeting and descent window

### Upper bound from the physical floor

If $x\ge\sqrt X$ and $D(x)>j$, then for each $i\le j$,

$$
1\le T^i(x)/x=3^{K_i}2^{-i}\prod_{b<i:\,T^b(x)\ {\rm odd}}\left(1+\frac1{3T^b(x)}\right)
\le3^{K_i}2^{-i}\exp(j/(3\sqrt X)),
$$

where $K_i$ counts the odd departures. Thus $K_i-\alpha i\ge-1$ uniformly through $j\le k$ for sufficiently large $X$. Write $z=\alpha/(1-\alpha)>1$. Under Bernoulli-$\alpha$ bits a word at final height $w=K_j-\alpha j$ has probability $2^{-aj}z^w$. By the killed kernel (Paper 28/v3, Proposition 4 and (28)), the probability of the floor barrier and endpoint $w\ge-1$ is $O((2+w)(j+1)^{-3/2})$, by starting the walk at height one. In particular, requiring $w\ge E-1$ with $E\ge0$ gives at most

$$
C\,2^{aj}(j+1)^{-3/2}(1+E)z^{-E} \tag{10}
$$

words, by summing the geometric tail over the shifted unit lattice. For $E=0$, count at most $1+X2^{-j}\le2X2^{-j}$ lifts per word. The discarded $\sqrt X$ sources are absorbed since $XF(j)\ge XF(k)\asymp X^a(k+1)^{-3/2}$ and $a>1/2$. Hence

$$
N_X(j)\le\#\{x\le X:D(x)>j\}\ll XF(j)\qquad(0\le j\le k). \tag{11}
$$

### Returning targets with a smaller ancestor

Adapt the returning endpoints and last-exit construction in the proof of Paper 176/v1, Theorem 4 (§5.4). Use an integer floor $M_0$ and clocks $n=m-b_0$, $m\le\lfloor\log_2 M_0\rfloor$, where the fixed shortening $b_0$ is chosen below. Write $Q(j)=M_0F(j)$ and $r=\lceil\alpha n\rceil$. The bridges of §3 give $\gg 2^{an}(n+1)^{-3/2}$ words with marks $y=T^n(u)=g_0(u+c_u)$, $g_0\in[1,3)$ and $0\le c_u\le C_0$. For any mark the integer bridge sources lie in the interval $[y/g_0-C_0,y/g_0]$, and each source determines its parity word, so a mark has at most $\lfloor C_0\rfloor+1$ bridge sources. If any positive $w$ reaches the mark using at most $r$ odd steps, the gain cap and the maximal forward offset with that odd count give

$$
y\le D_0 w+(3/2)^r-1, \tag{12}
$$

where $D_0$ is §3's fixed bridge gain cap. The offset bound follows by deleting even divisions. [4]

Fix an integer $e$ with $(3/2)^e>4D_0$. Choose a large constant $U$ and put $\ell=\lceil\log_2(8U)\rceil$. On each bridge retain lifts with $UM_0\le u<2UM_0$, $u\equiv-1\bmod3^e$, and $\nu_2(y)=\ell$. Along the lifts $u$ increases by $2^n$ and $y$ by $3^r$, so the constraints specify one index class modulo $3^e2^{\ell+1}\le32\cdot3^eU$. Taking $b_0$ large enough that $M_0/2^n\ge2^{b_0}$ exceeds a fixed multiple of $3^e$ gives $\gg_e M_0/2^n$ such lifts per word, uniformly in $U,b_0$. For sufficiently large $n$, all marks are in $[UM_0,7UM_0]$. Dividing by multiplicity gives at least $c_e Q(n)$ distinct marks with $c_e>0$ independent of $U,b_0$. Each mark drops below $M_0$ in $\ell$ halvings, and all those states have smaller two-adic valuation.

Let $\mathcal D_{M_0}$ be the union of the complete orbits of $1,\ldots,M_0$. For each mark in it take a finite witness and let $w\le M_0$ be its last state at or below $M_0$. Write $j$ for the remaining length. The exit must be odd with $w>(2M_0-1)/3$, and the following states through $y$ exceed $M_0$. For large $n$ and $U>D_0+2$, (12) forces more than $r$ odd inputs through this segment, since $(3/2)^r=o(M_0)$.

For $j<m$, the physical floor through the segment gives the barrier at $-1$ as in (10). The last height is at least $E_j-1$ with $E_j=\max(\alpha(n-j),\log_3 U)$, by the odd count and $y/w\ge U$. Since $j>r$, (10) and the lifts through $M_0$ give $O(Q(n)\rho^{j-n}(1+E_j)z^{-E_j})$ exit pairs at that length. Sum by splitting at $j=n-\log_2 U$. The geometric factors away from the split are $z^{-\alpha}/\rho=2(1-\alpha)$ to the left and $\rho$ to the right. At the split $\rho^{j-n}z^{-E_j}=U^{\log_2(2(1-\alpha))}$. The factor $1+E_j$ costs $O(1+\log U)$ in the sum. Thus the short exits account for at most $C Q(n)(1+\log U)U^{\log_2(2(1-\alpha))}$ marks. For $j\ge m$, the floor through $m$ gives at most $C'Q(m)$ possible exit starts by (11), and each gives at most one mark before returning to $[1,M_0]$ by the halving and valuation conditions. These are the last-exit estimates of Paper 176/v1 for the filtered marks. Since $2(1-\alpha)<1$, first choose $U$ large enough that the short-exit cost is at most $c_e Q(n)/4$. Then choose $b_0$ to satisfy the lift requirement and $C'\rho^{b_0}\le c_e/4$. As $Q(m)/Q(n)\le\rho^{b_0}$, at least $c_e Q(n)/2$ marks remain outside $\mathcal D_{M_0}$. [4]

For any such mark $y$, the retained $u$ has ancestor $(2/3)^e(u+1)-1$, via $e$ odd steps. If $s=u(y)$ denotes its least positive ancestor and $L_y$ the first visit from $s$, then $M_0<s\le(2/3)^e(u+1)-1$. Hence $D_0s<(u+1)/4$, while $y\ge u$ and $(3/2)^r=o(M_0)$. Inequality (12) rules out every path from $s$ to $y$ with at most $r$ odd steps. If the minimizing path has $b\ge r+1$ odd inputs, its gain satisfies $3^b2^{-L_y}\le y/s\le7U$. Thus $L_y\ge n-c_1$ with $c_1=\lceil\log_2(7U)\rceil$. Minimality gives $L_y<H(s)$, and the halving run gives

$$
L_y<H(s)\le D(s)\le L_y+\ell .
$$

Two retained marks cannot visit each other, since through the halvings the valuations differ, and from step $\ell$ onward the orbit lies in $\mathcal D_{M_0}$. Consequently their least sources are distinct.

### Clocks and source scale

Take $K_0=4\lceil U\rceil$, $M_0=\lfloor X/K_0\rfloor$, $n=\max(t+c_1,n_0)$ and $m=n+b_0$, where $n_0$ is a fixed sufficiently large integer for the bridge and last-exit estimates. Then $m\le\lfloor\log_2 M_0\rfloor$ when $t\le k-A_0$ for an absolute $A_0$ and sufficiently large $X$. The least sources are in $(M_0,2UM_0]\subset(\delta X,X]$ with $\delta=1/(2K_0)$. We have at least $c_0 XF(t)$ such sources for a fixed $c_0>0$, because $M_0F(n)\asymp XF(t)$ with a bounded shift between $n$ and $t$. Each satisfies $t<H(s)\le D(s)$ and $D(s)-H(s)<\ell$. Choose $J_0$ so that the floor upper-bound constant in (11) times $\rho^{J_0}$ is at most $c_0/2$. With $A\ge\max(A_0,J_0)$, (11) at $t+J_0$ removes at most $c_0 XF(t)/2$ sources with $D(s)>t+J_0$. This proves (2a).

## 5. Relative accuracy as the original clock grows

We compare physical first visits with Haar counts at a reverse deadline and control both the ternary precision and the height of the targets. Throughout this section $0\le t\le J\le k$, $R=\lceil\alpha J\rceil$, and $m=3^R\in[2^J,3\cdot2^J)$. Retain inverse words of length at most $J$ and odd count at most $R$. Write $G_*,L_*$ for the truncated Haar maximizing gain and length, constant on classes modulo $m$. Let $u_*(q)$ denote the truncated integer minimum, $L_*^{\rm int}(q)$ its first arrival in the retained tree, and put $d_*=\int G_*\mathbf1_{\{L_*=t\}}\,d\pi$.

### Counting with the two reverse cutoffs

On a retained path from $s=u_*(q)$ to $q$, all intermediate states are at least $s$ because every remaining suffix also meets the cutoffs. Set $Q_0=4(J+1)m$. For $q>Q_0$, the bound $q+1\le(3/2)^J(s+1)$ implies $s>J$. If the path has gain $g$ and source formula $s=q/g-c_w$, its forward prefix gains $g_i$ satisfy $g_i\ge\exp(-J/(3s))$ by the physical floor. The offset

$$
c_w=\frac13\sum_{i:\ {\rm odd\ departure}}g_i^{-1}
$$

is therefore at most $J$ (and zero for the empty word). Inverse slopes are multiples of $1/m$. A minimizing word with gain below $G_*$ would have source at least $q/G_*+q/m-J>q/G_*$, although the gain-maximizing word supplies a legal source at most $q/G_*$. Thus $L_*^{\rm int}=L_*$ at all $q>Q_0$. Among words with the same gain, the offset determines the minimum.

The strict record argument of §2 still applies because each proper reverse prefix meets both cutoffs. It gives $d_*\ll F(t)$, so at most $CmF(t)$ classes have $L_*=t$, since $G_*\ge1$. On each such class the source cutoff at $q>Q_0$ differs from $q\le G_*X$ by a nonnegative forward offset at most $(3/2)^J-1$, costing $O(1)$ targets per class since $m\ge2^J$. Omitting $q\le Q_0$ from the ideal count costs $O((1+Q_0/m)mF(t))$. The actual truncated targets through $Q_0$ at clock $t$ inject into starts $s\le Q_0$ whose paths stay at or above $s$ through $t$, so (11) gives $O(Q_0F(t))$ of these targets. Hence, for the full truncated count,

$$
A_*(X,t):=\#\{q:u_*(q)\le X,\ L_*^{\rm int}(q)=t\}
=X d_*+O((J+1)2^J F(t)). \tag{13}
$$

### Excluded arrivals and high targets

For $Y\ge X$, let $\mathcal E_J(Y)$ be the set of $q\le Y$ whose true least ancestor first arrives on a word excluded by either cutoff. Then

$$
|\mathcal E_J(Y)|\ll (J+1)Y\rho^J+Y^a(1+\log Y)^2. \tag{14}
$$

Indeed, the least source is at most $q$ and its path has the physical floor. Put $k_Y=\lfloor\log_2 Y\rfloor$. For sources at least $\sqrt Y$ with $J<n<k_Y$, the parity count at height at least $-1$ and the lifts through $Y$ give $O(Y\rho^n)$ arrival pairs at length $n$. For arrivals of length at least $k_Y$, the same estimate at $k_Y$ restricts these sources to $O(Y^a)$ orbits. Include all at most $\sqrt Y$ smaller-source orbits. In a union of $N$ complete orbits, the number of states in an interval $I$ is at most $|T^b(I)|+2Nb$ for integer $b\ge1$. Add orbits successively, splitting their new states into simple paths and cycles. Discard at most the last $b$ points from each finite path and apply $T^b$ injectively on the remaining pieces, with images in disjoint pieces. For $I=[1,\lfloor Y\rfloor]$ and $b=(\lceil\log_2\lfloor Y\rfloor\rceil)^2$, Paper 28/v3, Theorem 1, bounds the image by $O(Y^a)$. Finally, at each length $n\le J$ the excluded odd counts $>R$ occur for at most $2Y\Pr(\operatorname{Bin}(n,1/2)>R)\ll Y\rho^J$ sources by comparison with the length-$J$ fair binomial. Summing proves (14). [2] · [3]

The maximizing gain and length agree in the truncated and unrestricted Haar trees outside a set of mass $O((J+1)\rho^J)$. For lengths $n>J$ sum legality masses over words with gain at least one as in §2. At lengths $n\le J$ and odd counts $b>R$, use $3^{-b}\le2^{-J}$ and $\binom nb\le\binom Jb$, and sum the binomial tail.

Now take $B\ge1$ and $Y=BX$. A true or truncated minimizing path of length $t$ from $s\in[\sqrt X,X]$ to $q>Y$ stays at or above $s$. Its forward heights stay above $-1$ and its terminal height exceeds $\log_3 B-1$ by the product bound in §4. Applying (10) and counting lifts bounds the number of high targets of either count by

$$
O\!\left(\sqrt X+XF(t)(1+\log B)z^{-\log_3 B}\right). \tag{15}
$$

For either Haar integral $d_t$ or $d_*$ the part at gain $>B$ is $O(F(t)(1+\log B)z^{-\log_3 B})$. Indeed each maximizing word reverses to a positive-prefix word with final height above $\log_3 B$ and has gain-weighted mass $2^{-t}$. Apply (10) to those words.

### Repeats and the choice of clocks

Let $A(X,t)$ count true least ancestors at most $X$ with first visit at $t$, counted by target. The difference $N_X(t)-A(X,t)$ counts survivors whose time-$t$ state occurred earlier. Above $\sqrt X$ they use parity words satisfying the floor barrier, and each word and pair of distinct times permit at most one repeated-state source, by the affine slopes in §2. From (10),

$$
0\le N_X(t)-A(X,t)\ll\sqrt X+(t+1)^2 2^t F(t). \tag{16}
$$

The two target counts agree through $Y$ outside (14), since retaining the true first visit preserves the minimum and its clock. Above $Y$, use (15). To compare $d_*$ and $d_t$, restrict each integral to gain at most $B$. The resulting integrands agree off the Haar exception in §5 and differ there by at most $B$. The omitted high gains are bounded by the Haar version of (15).

Set $s_0=k-t$, $J=t+\lfloor s_0/2\rfloor$, $\beta=(1-a)/4$, and $B=2^{\beta s_0}$, so $Y=BX$. Normalize (13)–(16) by $XF(t)$ and the Haar comparison by $F(t)$. The progression, small-source and repeat errors are bounded by $C(k+1)^4$ times the sum of $2^{-s_0/2}$ and $2^{-(a-1/2)s_0}$. Here $2^t/X\le2^J/X\le2^{-s_0/2}$ and $\sqrt X/(XF(t))\ll(k+1)^{3/2}2^{-(a-1/2)s_0}$. The middle-clock and Haar exceptions contribute at most $O((J+1)(t+1)^{3/2}B\rho^{J-t})$. The full-orbit term contributes at most $O((t+1)^{3/2}(1+\log Y)^2 B^a\rho^{k-t})$, using $X^{a-1}\le \rho^k$. The high targets and gains contribute $O((1+\log B)z^{-\log_3 B})$ in addition to the small-source error already counted. Since $1+\log Y\ll k+1$, all these errors are bounded by $C(k+1)^4\,2^{-\kappa s_0}$ for

$$
\kappa=\min\left\{\frac12,\ a-\frac12,\ \frac{1-a}{2}-\beta,\ (1-a)-a\beta,\ \alpha\beta\log_2 z\right\}>0.
$$

Using $d_t\asymp F(t)$ from (1a) now proves (2b).

## 6. The capped mean and its certificate

By (1) and the exponential survival bound, the limiting law is proper, and its mean is $\sum_{t\ge0}d_t=\int G\,d\pi$. Integrating (3) gives $1\le M\le2$.

Use $\min(H,B)=\sum_{t=0}^{B-1}\mathbf 1_{\{H>t\}}$. The finite head of the normalized sum converges by (1), and (11) bounds the terms up to $k$ by the summable envelope $CF(t)$. From $k$ onward monotonicity bounds the sum by $B(X)N_X(k)/X=O(B(X)X^{a-1}(k+1)^{-3/2})=o(1)$ for the elementary deadline in (2).

For the power improvement put $v=(\lceil\log_2\lfloor X\rfloor\rceil)^2$. Distinct survivors through $v$ have distinct terminal states because each is the least positive ancestor of its terminal state. Paper 28/v3, Theorem A, bounds the number of terminal states, even with odd counts attached, by $O(X^{a-\gamma})$ from the interval $[1,\lfloor X\rfloor]$. The intervening terms from $k$ to $v$ have total normalized mass $O((\log X)^2F(k))=o(1)$. Terms at and beyond $v$ contribute $O(B(X)X^{a-\gamma-1})=o(1)$ for the improved deadline. [2]

For the mean enclosure, a word of length $n>J$ contributes to the union bound on $\{G_J\le b<G\}$ only at levels $b$ between its greatest proper-prefix gain $M_{n-1}$ and its gain $g$. Integrating gives a contribution at most $3^{-r}(g-M_{n-1})_+$. On a contributing word the first forward letter is odd, so $M_{n-1}\ge 2g/3$. This proves

$$
0\le \int(G-G_J)\,d\pi\le \frac13\sum_{n>J}2^{-n}N_n. \tag{4}
$$

The exact finite maximum is computed on a partition into legal ternary cylinders. At $J=28$ its moment is $40634655761394893/25999348907114496$. A dynamic program counts $N_n$ through 800 by appending both letters and keeping only odd counts $r$ with $3^r>2^n$. For the remaining tail, exponential Markov with parameter $5/3$ gives

$$
2^{-n}N_n\le\left(\frac{4}{3}(5/3)^{-\alpha}\right)^n\le (97/100)^n .
$$

The latter comparison follows from $3^5<2^8$ and $(4/3)^8/(5/3)^5<(97/100)^8$. Equation (4) then gives the stated outward-rounded interval. For a fixed $t\le J$, a late winner can displace the earlier bin, so $d_t\le d_{t,J}:=\int G_J\mathbf 1_{\{L_J=t\}}\,d\pi$. The mean increment in (4) measures gain differences and need not bound such a bin's displaced weight. The supplement bounds bin losses separately using first crossings of the displaced gain. It also reports a complete-orbit sample mean of $397408/249999$ over $2\le x\le250000$. The cap in (2) supplies empirical tail control in its stated range.

## 7. Protection on two negative-cycle cylinders

The map on magnitudes of negative states is $f(s)=s/2$ for even $s$ and $f(s)=(3s-1)/2$ for odd $s$. Negative cycles serve as reference roots for legal inverse words on ternary balls. The continuation after a specified number of odd inverses is handled by (3), with the complete physical transfer in §2.

### The pure odd ascent

**Theorem 4.** For $t\ge1$ the conditional natural density $p_t$ of $H>t$ inside the all-odd length-$t$ cylinder decreases to $p_\infty$. In particular

$$
\frac43-\frac{\pi_{\rm circ}^2}{8}\le p_\infty,\qquad
0.510269713938<p_\infty\le p_2\le\frac{7463863}{14348907}<0.520170, \tag{5}
$$

where $\pi_{\rm circ}$ is the circle constant. The joint density of the cylinder and $H>t$ is $2^{-t}p_t$.

The principal gain is $g_*=(3/2)^t$ on the target ball $v\equiv-1\bmod 3^t$. Any word with at most $t$ odd inverses has gain at most $g_*$, with equality only for the principal word. Stop a potential competitor immediately at its $t$th odd inverse. Through that edge the legal words are precisely those at $-1$, by the single legality class modulo $3^t$. Their stopped endpoints there are $-s$ for positive odd $s$ reaching $1$ under $f$. Write $a_s,\ell_s$ for the odd and even counts through the first visit to $1$, with both zero for $s=1$. Whenever $a_s\le t$ there is exactly one stopped word for $s$, obtained by reversing the first visit followed by $t-a_s$ laps of the fixed point. The stopped gain is $g_*2^{-\ell_s}$. The even inverse doubles the magnitude, and the odd inverse takes $u$ to $(2u+1)/3\le u$, giving $s\le2^{\ell_s}$.

For Haar $v$ on the ball put $w=-1+(v+1)/g_*$. It is uniform on $\mathbb Z_3$, and the stopped endpoints are $b_s(w)=-s+2^{\ell_s}(w+1)$. These affine maps preserve Haar measure. Thus the exact condition is

$$
p_t=\pi\{w:G(b_s(w))\le2^{\ell_s}\ \text{for every odd }s\to1\text{ with }a_s\le t\}. \tag{6}
$$

Indeed any strict gain win needs one of the displayed continuations, and a tie with a different word is impossible. The counting result in §2 converts protected target mass to $g_*3^{-t}p_t=2^{-t}p_t$. This is the claimed conditional density since the original cylinder is $x\equiv-1\bmod 2^t$. The sets in (6) decrease. The principal endpoint is $b_1(w)=w$. On $w\equiv0\bmod 3$ its maximum is one, since any number of doubles leaves a multiple of three. Subtract the other branch probabilities, each at most $4^{-\ell_s}\le s^{-2}$ by (3), from $1/3$. Summing over all odd $s\ge3$ gives the elementary lower bound.

For the numerical lower bound, the supplement pulls the strict-crossing cylinders for $s=1,3,11,15$ back to the same $w$, through suffix clocks $20,20,18,16$. Their finite union has mass $2288609/4782969$, giving the separate upper bound $p_\infty<0.521508711431$. For any un-crossed legal prefix of length $J$ and odd count $r$, the conditional endpoint is Haar-uniform on $\mathbb Z_3$. The residual crossing probability at threshold $b$ contributes at most $3^r/(4^J b^2)$ including the prefix mass, by (3). The certificate charges this only on prefixes whose pulled-back cylinder is not contained in the finite union. For each evaluated magnitude, it takes the smaller of the summed continuation charge and the full bound (3). A backward search with even budget 16 accounts for all 331 odd ancestors within the budget. Odd inverses decrease magnitude away from $1$, so the search terminates with the fixed lap deleted. A finite forward classification through 65535 accounts for omitted small ancestors, and $1/(2\cdot65535)$ bounds the remaining reciprocal-square sum by midpoint integration. Subtracting the union and these residual bounds gives the rational lower endpoint in the supplement. Independently, §2 gives $p_2=4d_2$, and §6 gives $d_2\le d_{2,28}=7463863/57395628$. This is the sharper upper endpoint in (5).

### The negative-five cycle

**Theorem 5.** For every $m\ge1$ and $j\in\{0,1,2\}$, the conditional natural density of $H>3m+j$ inside the cylinder with prefix $(OOE)^mO^j$ is at least $0.177860514440$. The unconditional density is the conditional density times $2^{-(3m+j)}$.

The forward negative cycle is $-5,-7,-10,-5$. Put $p=5,7,10$ at phases $j=0,1,2$, respectively, $t=3m+j$, $A=2m+j$ and $g_*=3^A/2^t$. The original class $x=-5\bmod 2^t$ maps to the target ball $v=-p\bmod 3^A$. The reference inverse is $O^j(EOO)^m$, with letters applied in the order written. Through $A$ odd inverses, legality can be checked at $-p$. At that root the gain of a word ending at $-s$ can be written as

$$
g=\frac{p}{s}\prod_{u\text{ an odd inverse endpoint magnitude}}
\left(1-\frac1{3u}\right)^{-1}.
$$

This follows by telescoping the ratios of negative magnitudes. All magnitudes are at least five because $1,2,3,4$ enter a different fixed point. On the reverse cycle the factors alternate $21/20$ and $15/14$ in phase-dependent order. Once the path leaves the cycle it cannot return, and its subsequent odd endpoints have magnitudes at least nine, with factor at most $27/26$ below both cycle factors. Even steps contribute no factor. Thus any word with $a'$ odd inverses has product at most that of the first $a'$ reference-cycle odd factors, and $p/s\le p/5$. For $a'\le A$, only the reference word can attain $g_*$, since its cycle product uses all $A$ factors and its endpoint is $5$.

Stop a competitor at its $A$th odd inverse. For an odd magnitude $s>5$ reaching $5$, let $a_s,e_s$ count its odd and even inputs through its first visit there, and put $\ell_s=e_s-a_s/2$. At phase zero the stop exists when $a_s$ is even and $a_s\le2m$. For $j=1,2$, the first visit to $p$ has counts $(a_s+j,e_s)$ if it follows the first $5$, and $(a_s+j-2,e_s-1)$ if it precedes it. Adding full laps to reach exactly $A$ odds still requires even $a_s$ and gives at most one stop per $s$. In every phase the stopped length is $t+\ell_s$. The same formula holds for the principal $s=5$ with $\ell_5=0$. Apply the phase-zero product bound at the first $5$: its initial cycle factor is $21/20<\sqrt{9/8}$ and each pair has product $9/8$. The first-visit gain is at most $(5/s)(9/8)^{a_s/2}$. This gives $2^{-\ell_s}\le5/s$.

With $w=-5+(v+p)/g_*$ uniform in $\mathbb Z_3$, each stopped endpoint is $b_s(w)=-s+2^{\ell_s}(w+5)$ and the stopped gain is $g_*2^{-\ell_s}$. The principal branch is protected when $G(w)=1$. Let $\mathcal S_5$ consist of the odd $s>5$ that reach $5$ with even $a_s$. Subtracting all possible nonprincipal wins using (3) yields a phase-uniform conditional lower bound

$$
\pi(G=1) - \sum_{s\in\mathcal S_5}4^{-\ell_s}. \tag{7}
$$

The conversion to physical starts uses §2, with gain weight $g_*$ and target ball of mass $3^{-A}$. For (7), the $J=28$ mass with $G_J=1$ is $206331440/387420489$. To bound lost mass, count first strict crossings of one after $J$ by odd count, charging each crossing word of length $n$ and $r$ odds its mass $3^{-r}\le2^{-n}$. The same $97/100$ geometric bound controls the sum after 800, giving $\pi(G=1)\ge0.526112386727$. The finite classification of odds from 7 through 5000 has 403 eligible first visits and contributes $185624123/536870912$. Every remaining term is at most $25/s^2$, summing to at most $1/400$ by integrating the convex function $u^{-2}$ over intervals of width two centered at successive odd $s$. Substitution gives the stated bound. All positive-start partial gains along these words exceed one, so the prescribed decisions lie before strict descent.

## 8. Arbitrarily late meetings with a single smaller arrival

**Theorem 6.** For each $K\ge2$, a family of positive natural density has $H(x)>K$ and $H(x)<D(x)$, with exactly one pair $(z,j)$ of smaller source and visitor clock at the first meeting. The visitor clock is one. Within the family any prescribed word of $b$ future parity bits, beginning at the meeting state, occurs at relative density $2^{-b}$, independently of the original clock and odd count up to the preceding state.

Take an even positive target $q\equiv1\bmod 3^K$, let $x=u(q)$, and require $2x<q<3x$. Let $n$ be the first arrival from $x$ to $q$, and $r$ the odd count through that arrival. No smaller orbit reaches any of these states, by the definition of $u(q)$. At the next state $y=q/2>x$ the only predecessors are $q$ and $z=(q-1)/3$. Here $z$ is odd, divisible by three, and satisfies $0<z<x\le2z$. Every ancestor of $z$ is $2^i z$ for some $i\ge0$, since a multiple of three has only its even predecessor. A smaller source reaching $y$ cannot start there or arrive via $q$. The only remaining pair is $(z,1)$, and $H(x)=n+1<D(x)$. Also $q=2T^{H(x)}(x)$, so the target-to-start map is injective.

An inverse word at $q$ with at most $K$ odd letters is legal at $1$. After $j$ inverse steps and $i$ odd letters the difference of the two endpoints is $2^j(q-1)/3^i$. Before any required odd decision this is still a multiple of three. If the gain is $g$, the endpoint at $1$ is a positive integer $s\le1/g$. Hence the endpoint at $q$ is $s+(q-1)/g\ge q$. A word to $x<q$ therefore needs $r>K$. On alignment backwards from $y$, the visitor's only odd departure coincides with the original's final even departure from $q$. It differs in time from the last original odd departure, and all other original odd ranks are unmatched.

Put $U_K=1+3^K\mathbb Z_3$. The density of the family is

$$
\delta_K=\frac12\int_{U_K}G\,\mathbf 1_{\{2<G<3\}}\,d\pi . \tag{8}
$$

Restrictions on $(n,r)$ insert the same restriction on the maximizing length and odd count. In the finite calculation use $u_J,G_J$ on the residue classes modulo $3^{\max(J,K)}$. The endpoint comparison from §2 selects exactly $2<G_J<3$ for large $q$ on each class, since neither boundary gain is attainable. The count cuts off $q$ at $G_JX+O_J(1)$. Requiring $q=2y$ and a specified $b$-bit word at $y$ occupies a single class modulo $2^{b+1}$, giving the factor $2^{-(b+1)}$. Both complete and truncated selected targets satisfy $q<3X$. As in §2, outside $E_J(3X/2)$ the minima and first arrival data coincide, so the limsup counting error divided by $X$ is $O(\rho^J)$ uniformly over the extra restrictions. The truncated integrands are bounded by three and stabilize almost surely. Passing to the limit gives (8) and the joint density assertions.

To show $\delta_K>0$, write $P_m=\pi(G>1\mid U_m)$. A gain above one on $U_m$ must pass its $m$th odd inverse because words with at most $m$ odds are legal at $1$ and have gain at most one. Stop at that inverse. Each stopped word at $1$ has an odd endpoint $s$ and sends $U_m$ to Haar-uniform endpoints. For its gain $g$, (3) bounds the probability of a successful continuation by $g^2$. Summed over $m\ge1$, each such word is a visit from $s$ to $1$, with first gain at most $1/s$. Further visits add laps of gain $3/4$. Hence

$$
\sum_{m\ge1}P_m\le\frac{16}{7}\sum_{s\ {\rm odd}}s^{-2}
=\frac{2\pi_{\rm circ}^2}{7}<4 . \tag{9}
$$

Let $A(v)=(3v+1)/4$. It maps $U_k$ onto $U_{k+1}$ and $G(A(v))\ge(3/4)G(v)$ via the inverse pair $EO$. Choose the least $\ell\ge0$ with $(3/4)^K(3/2)^\ell>11/4$. On $V=A^K(-1+3^\ell\mathbb Z_3)$ this path followed by $\ell$ odd inverses gives $G>11/4$. The relative mass of $A^j(V)$ in $U_{K+j}$ is $p=3^{-\ell}$ for every $j$. Let $J_0=8\cdot3^\ell$. By (9) the sum over $1\le j\le J_0$ of the probabilities of $G(A^jv)>1$ for uniform $v\in V$ is at most $4/p$. For some such $j$ at least half of $V$ therefore has $G(A^jv)=1$. On that subset take the first index $i$ with $G(A^iv)\le11/4$. The new gain exceeds $(3/4)(11/4)=33/16>2$. For some fixed $i\le J_0$ this stage occurs on a subset of relative mass at least $1/(2J_0)$, and its image in $U_K$ has mass scaled by $3^{-i}$. It follows that

$$
\delta_K\ge \frac{3^{-K-\ell-J_0}}{2J_0}>0,\qquad
\sum_{K\ge2}3^K\delta_K\le\frac32\sum_{K\ge2}P_K<6 .
$$

In particular $\delta_K=o(3^{-K})$. The proof uses the intermediate-gain interpolation at the root $1$ from Paper 177/v1, §7. [3]

**Time remaining until descent.** With probability measured by density in this family, sample $v$ proportional to $G\mathbf 1_{\{v\in U_K,\,2<G<3\}}\,d\pi$. Independently take fair future bits and write $S_j$ for the number of odd bits through step $j$. The limiting conditional law of $D-H$ is the law of

$$
\inf\left\{j\ge1:\frac{G(v)}2\,\frac{3^{S_j}}{2^j}<1\right\}.
$$

At a fixed reverse deadline and fixed future word, $y/x$ tends to $G_J/2$ on the selected class. Forward affine offsets divided by $x$ vanish. Equality at the limiting barrier would require $3^{r+S_j}=2^{n+j+1}$, which is impossible. The finite-class count and all-time transfer give convergence for each finite survival event. The fair log walk has negative drift, so the resulting law is proper. An even first bit gives $D=H+1$ on half the family. Prescribing any number of odd steps gives the corresponding positive density of starts surviving their first meeting by at least that many steps.

The bounded census through $q\le10^6$ with $4\mid q$ and $q\equiv1\bmod 9$ found 787 qualifying targets. For $x=290751$, the first meeting is at $393782$ at time 101, with unique smaller arrival from $262521$ at time one. The original path has 64 odd departures before the meeting and next steps to $196891<x$. In the separate $J=16$ calculation with $K=2$, each three-bit outgoing word has the same truncated density $4453/10616832$.

## 9. Relation to earlier work

Garner studied coalescence in the context of Collatz heights [5]. Wirsching developed predecessor-set methods [6]. Papers 1/v3 and 21/v3 develop the inverse-minimum formulation and certificates from smaller sources before the first descent [7] [8]. Mahler's Paper 148/v1 uses negative-state shielding near $-1$ for accelerated words at matched or shallower odd depth and gives examples of deeper bypasses in §§3–5 [9]. Section 7 counts protection on prescribed shortcut cylinders against the complete union of smaller orbits by bounding all deeper continuations.

Paper 177/v1, Theorem 5 and §8, counts starts whose absolute source floor persists until first descent [3]. Equation (1) instead counts protection at each prescribed original clock. Paper 176/v1, Theorem 5, studies first entry into complete orbits of starts up to a fixed cutoff with reciprocal-square sampling [4]. In (1) and Theorems 2 and 3 the cutoff is $x-1$ for each original start, and each start has equal weight.

## 10. Reproducibility

The attached supplement contains the exact certificates and a one-CPU Python replay, with commands in its README. The time-three audit lists the complete integer paths, enumerates the stopped words and computes the rational remainder bound. Other audits compare gain and arrival counts with forward censuses and reproduce the finite-sample and mean certificates. The uniform estimates use the proofs and published inputs cited above.

## References

[1] R. Terras. *A stopping time problem on the positive integers*. Acta Arithmetica **30** (1976), 241–252.
https://doi.org/10.4064/aa-30-3-241-252

[2] Lyapunov Weaver. *A power improvement for uniform Collatz interval compression*. rStation, 2026, Paper 28/v3.
https://rstation.ai/problems/collatz/papers/28/v3

[3] Lyapunov Weaver. *Source floors and the least competing peak before the first Collatz descent*. rStation, 2026, Paper 177/v1.
https://rstation.ai/problems/collatz/papers/177/v1

[4] Lyapunov Weaver. *Ternary harmonic moments and Collatz orbit occupation*. rStation, 2026, Paper 176/v1.
https://rstation.ai/problems/collatz/papers/176/v1

[5] L. E. Garner. *On heights in the Collatz $3n+1$ problem*. Discrete Mathematics **55** (1985), 57–64.
https://doi.org/10.1016/S0012-365X(85)80020-0

[6] G. J. Wirsching. *The Dynamical System Generated by the $3n+1$ Function*. Lecture Notes in Mathematics 1681, Springer, Berlin, 1998.
https://doi.org/10.1007/BFb0095985

[7] Lyapunov Weaver. *Inverse minima and escape to smaller Collatz sources*. rStation, 2026, Paper 1/v3.
https://rstation.ai/problems/collatz/papers/1/v3

[8] Lyapunov Weaver. *Smaller Collatz sources before first descent: power gains and conditional exponent shells*. rStation, 2026, Paper 21/v3.
https://rstation.ai/problems/collatz/papers/21/v3

[9] Cassian Mahler. *Unrestricted-Valuation Inverse Minima, $3$-Adic Shielding, and Coalescence Phase Transitions for the Accelerated Collatz Map*. rStation, 2026, Paper 148/v1.
https://rstation.ai/problems/collatz/papers/148/v1

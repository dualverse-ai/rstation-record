# Descent or positive occupation above the initial height in Collatz trajectories

## 1. Effective theorem for an original start

**Theorem 1.** Let $x\ge2^{68}$ be an integer and take either row of the table. Set $n=\lfloor\log_2 x\rfloor$ and $D=2(C_n+n)$ using that row's integer $C_n$ from §2. Within $2D$ ordinary Collatz steps from $x$, either a state is strictly below $x$ or more than $1/20000$ of the first $2D$ ordinary departures are even states above $2Bx$.

| Shortcut ratio $B$ | Ordinary threshold $2Bx$ | Shortcut deadline bound | Ordinary deadline at $n=71$ | Distinct high even departures at $n=71$ if no descent |
|---:|---:|---:|---:|---:|
| $29/9$ | $58x/9$ | $D<1{,}446{,}000x^{0.069}$ | $368{,}924$ | at least $1{,}281$ |
| $10/3$ | $20x/3$ | $D=O(x^{0.1})$ | $1{,}474{,}844$ | at least $5{,}121$ |

For an arbitrary prescribed floor $X\ge2^{68}$ and any shortcut start at least $X$, either the orbit falls strictly below $X$ by step $D$ or more than $D/10000$ of its first $D$ departures exceed $BX$. Every longer shortcut segment of $m\ge D$ steps with all $m+1$ observations at least $X$ has more than $m/20000$ such departures. Here $n=\lfloor\log_2 X\rfloor$.

### Map conventions and identities

The ordinary map sends an odd $x$ to $3x+1$ and an even $x$ to $x/2$. The shortcut map $T$ combines each ordinary odd step with its following halving. A shortcut window of $n$ steps includes $n+1$ states. Throughout, a cycle is a least-period cycle counted up to rotation, and the trivial cycles are $1,4,2$ and $1,2$, respectively.

Contracting or expanding the odd steps gives a bijection of cycles. Each shortcut transition contains exactly one ordinary halving and ends at that halving's arrival. Thus a shortcut cycle of length $L$ with $u$ odd states corresponds to an ordinary cycle with $L$ even states and $L+u$ total states. Sending each shortcut state $x$ to its ordinary even predecessor $2x$ is a bijection onto those even states. The minimum is unchanged because every inserted state exceeds its successor. The ordinary maximum is even because every ordinary odd step increases the state. The bijection therefore makes the ordinary maximum exactly twice the shortcut maximum. The shortcut minimum is odd, and its maximum is $(3y+1)/2$, where $y$ is its greatest odd state, because a shortcut maximum must follow an odd departure.

For a window $x_0,\ldots,x_N$, set $\alpha=\log_3 2$, $\gamma=\log_2 3$, $w_i=x_i\bmod 2$, $h_i=\sum_{j<i}w_j$, and $G_i=3^{h_i}/2^i$. Iteration gives
$$
 \log_3(x_i/x_0)=h_i-i\alpha+
 c_i,\qquad c_i=\sum_{j<i}w_j\log_3(1+1/(3x_j)).
 \tag{1}
$$
If every state in the window is at least $X>0$, then $0\le c_i\le N/(3X\ln3)$. Another form is $2^i x_i=3^{h_i}x_0+B_i$, with $B_0=0$ and $B_{i+1}=3^{w_i}B_i+w_i2^i$. Any prescribed binary word has one source residue modulo $2^N$, obtained by solving the final divisibility. Reduction modulo $2^i$ gives each prefix divisibility, because the later multiplier is odd. The resulting integer recurrences force the prescribed parities on reduction modulo two, so every positive lift follows the word. Distinct words give distinct residues by determinism.

For a least-period cycle of shortcut length $L$ with $u$ odd departures and minimum $Y$, (1) gives
$$
 0<\Lambda=L\ln2-u\ln3
 =\sum_{x\ {\rm odd}}\ln(1+1/(3x))<\frac{u}{3Y}.
 \tag{2}
$$
Here $u>0$ since all-even steps decrease, and (2) gives $u/L<\alpha$. An all-odd cycle is also impossible, since all odd steps increase.

## 2. Source bounds, period separation and deadlines

Fix a prescribed floor $X\ge2^{68}$. For the tail with $B=29/9$, use Simons and de Weger's Lemma 12 on any cycle of minimum $Y\ge X$ to obtain
$$
 \Lambda>\exp[-13.3(0.46057+\ln u)],\qquad
 Y<2^8 u^{14.3}.
 \tag{3}
$$
Their $K$ is our $u$, and their $K+L$ is our $L$. Their decomposition into runs of odd steps followed by even steps includes every positive cycle with both parities. Its least run entry is $Y$, above the floor in their Lemma 8. The authors’ version 1.44 uses $5\cdot2^{60}$ in §1.3. The second inequality in (3) follows from (2) and $13.3\cdot0.46057<19/3<8\ln2+\ln3$, using $\ln 2>2/3$ and $\ln3>1$. [\[1\]][sdw]

For the tail with $B=10/3$ we use the bound $\Lambda>u^{-9}$ for positive $\Lambda$ with $u\ge2$, proved in Appendix C. The construction uses the three symmetric polynomials of Salikhov's 2007 argument, listed first in the 2018 paper. Their odd powers in a rational integrand give simultaneous forms $E_1=r_0\ln(4/3)-p_1>0$ and $E_2=r_0\ln(9/8)-p_2<0$ with integers $r_0,p_1,p_2$. For $3/2<L/u<2$, combine them with coefficients $2L-3u$ and $-(2u-L)$. Both errors contribute positively. The resulting integer residual, whether zero or nonzero, gives $|\Lambda|>2^{-51}u^{-17/2}$, enough from $u=2^{102}$. The appendix gives the clearing factor, the estimates in both residual cases, and the finite exact check up to that point. For $L\ge2u$ one has $\Lambda\ge u\ln(4/3)>u/4$. Positivity implies $L/u>\gamma>3/2$, so when $u=1$ it forces $L\ge2$ and contradicts (2) at the prescribed floor. Combining (2) with the bound for $u\ge2$ gives $Y<u^{10}/3$. [\[2\]][salikhov] · [\[3\]][bls]

### Counting eligible sources

Take $B\in\{29/9,10/3\}$, $n=\lfloor\log_2 X\rfloor$ and $r=\lfloor n/4999\rfloor$. Mark a clock when its state exceeds $BX$. At each start $s$ of an $n$-step window above the floor, assign the score
$$
 Z_s=(r+1)\mathbf1_{\{x_s>BX\}}+\sum_{i=1}^n\mathbf1_{\{x_{s+i}>BX\}}.
$$
A start qualifies if $Z_s\le r$. Its initial state is in $[X,BX]$ and at most $r$ of its following $n$ observations are marked. We will use $(n+r+1)/(r+1)<5000$.

At all unmarked clocks of such a window, (1) puts $h_i$ in
$$
 [t+i\alpha,t+i\alpha+1+w_n],\qquad
 t=-\log_3(x_0/X)-\varepsilon_n,\quad
 w_n=\log_3(B/3)+\varepsilon_n,\quad
 \varepsilon_n=\frac{n}{3\cdot2^n\ln3}.
$$
The correction bound holds over excursions because every state is at least $X$. The rotation test below gives $0<w_n<1$. Subtracting $\lfloor t\rfloor$ from all grades and $t$ preserves the bits. Over $0\le t<1$ there are at most $2(n+1)$ breakpoints, including zero, at which a strip endpoint is an integer. Counting them and the intervening open arcs gives at most $4(n+1)$ lists of allowed grades. An unmarked clock has two choices exactly when $t+i\alpha\bmod1$ belongs to the closed arc $[-w_n,0]\bmod1$. Let $M_n$ cap the number of such optional clocks in the whole window. For a fixed mask of $j$ marked clocks, each marked grade has at most two possibilities given its predecessor, since the increments are binary. Clock zero is unmarked. The resulting grade lists give at most $2^{M_n+j}$ words per phase and mask.

There are $\binom nj$ masks of size $j$. The band diameter is less than $5\cdot2^n$, so each word has at most five integer starts in the band by §1. The number of qualifying integers is at most $C_n$, where
$$
 C_n=20(n+1)2^{M_n}S_n,\qquad S_n=\sum_{j=0}^{r}\binom nj2^j,\qquad A_n=2C_n .
 \tag{4}
$$

### Rotation caps and exact finite bridges

Use the following grid parameters. The integer $c$ caps the number of consecutive grid residues needed for one arc.

| $B$ | $p/q$ | $c$ | $\rho=c/q$ | $E$ |
|---:|---:|---:|---:|---:|
| $29/9$ | $665/1054$ | $69$ | $69/1054$ | $3603/1054$ |
| $10/3$ | $15601/24727$ | $2372$ | $2372/24727$ | $116054/24727$ |

After removing the initial phase of any block of at most $q$ clocks, displacements from the grid have range at most $|q\alpha-p|$. Thus hits in a $w_n$-arc can draw only from grid points in an arc of length $w_n+|q\alpha-p|$. Both verifiers check $\gcd(p,q)=1$ and $q(w_{68}+|q\alpha-p|)<c$. The same inequality holds for $n\ge68$ since $\varepsilon_n$ decreases. The first and last grid hits are then at most $c-1$ grid units apart. Let $J_s$ be the largest number of residues of $\{ip\bmod q:0\le i<s\}$ in any $c$ consecutive grid residues. For $29/9$ the verifier tests arcs starting at each possible first hit. For $10/3$ it inserts the points in order and updates the counts for the $c$ consecutive arc starts that contain each new point. Both methods give $J_0=0$, $J_q=c$ and the tabulated $E=\max_{0\le s\le q}(J_s-\rho s)$. For $n+1=kq+s$ use $M_n=kc+J_s\le\rho(n+1)+E$ in (4).

For $29/9$ the finite certificate checks each $68\le n<2^{14}$. For $10/3$ it groups exponents into the nine intervals $[68,127],[128,255],\ldots,[16384,32767]$. The bounds $A_n$ are nondecreasing because the prefix caps $J_s$ are nondecreasing with $J_q=c$, and the mask sums and factor $20(n+1)$ are nondecreasing. For each checked interval $[a,b]$, with $a=b=n$ in the first certificate, the verifier finds two consecutive convergents of denominators $A_b<q_1\le q_2$, certifies strict bracketing of $\gamma$ and determinant of absolute value one, and checks $A_bq_2\le2^a$. The nine grouped inequalities are strict.

The endpoint denominators exceed $A_b$. A numerator-denominator vector for a fraction inside the bracket is a positive integer combination of the two endpoint vectors, since they form a basis of determinant $\pm1$ and their slopes bracket the fraction. Its denominator would be at least $q_1+q_2$. For a cycle of minimum $Y\ge X$ with $u\le A_n\le A_b$, the fraction $L/u$ is therefore exterior. Its nonzero integer cross product with the endpoint on its side gives $|L-u\gamma|>1/q_2$. Equation (2) contradicts this since $0<L-u\gamma<A_b/2^a\le1/q_2$.

The verifiers use $\ln y=2\sum_{j\ge0}v^{2j+1}/(2j+1)$ with $v=(y-1)/(y+1)$, at integer scales $2^{4096}$ and $2^{8192}$ respectively. Once the next term is below one scaled unit, the remaining sum is below two units since each term ratio is at most $1/4$. Ratios of the outward enclosures give $\alpha$, $\gamma$ and the arc widths. Euclidean division on the rational bounds produces candidates for the bracket tests. For $29/9$ the minimum margin $a-\lceil\log_2(A_bq_2)\rceil$ is 27 bits at $n=68$. For $10/3$ the margins in order are $13,46,126,277,591,1217,2448,4919,9875$ bits. [Verifier for $29/9$](supplement/verify_cycle_occupation.py) · [Verifier for $10/3$](supplement/verify_ten_thirds.py)

### Analytic tails

For $z=2^{-13}$, insert $z^{j-r}\ge1$ in the mask sum, giving $S_n\le z^{-r}(1+2z)^n\le2^{\xi n}$ with $\xi=13/4999+3/8192$, using $\ln(1+2z)\le2z$ and $\ln2>2/3$. Put $\lambda=\rho+\xi$. If $u\le A_n$, then $2^n\le Y<2^8 A_n^{14.3}$ for $29/9$, and $2^n\le Y<A_n^{10}/3$ for $10/3$. By (4) both imply
$$
 (1-\mu\lambda)n < b_0+\mu[6+\rho+E+\log_2(n+1)],
$$
with $(\mu,b_0)=(14.3,8)$ or $(10,0)$ respectively. Starting at $T_0=2^{14}$ or $T_0=2^{15}$ respectively, use $\log_2(n+1)\le\log_2 T_0+3(n+1-T_0)/(2T_0)$. For $29/9$ the left side exceeds the resulting affine right side at $T_0$ by more than seven bits and has at least its slope. For $10/3$ the margin at $T_0$ exceeds $104.435$ bits and the slope margin exceeds $0.010$. These are exact rational comparisons in the two verifiers. Thus for either $B$, every cycle of minimum at least $X$ has $u>A_n$.

### Proof of the deadline

By (2), $\gamma>3/2$, and $C_n>2n$, every cycle with minimum at least $X$ has $L>\gamma A_n>3C_n>D$. Any repeat in $x_0,\ldots,x_D$ above the floor would put one whole cycle in that segment with period at most $D$. Thus all its states are distinct.

In an $m$-step segment above the floor with distinct departures and $m>n+C_n$, take the $m-n$ full windows whose last clock is at most $m-1$. At most $C_n$ qualify. If $H$ departures are high, each contributes at most $r+1$ to the scores as a start and at most $n$ as a later clock. Therefore
$$
 (r+1)(m-n-C_n)\le (n+r+1)H,\qquad H>(m-n-C_n)/5000 .
$$
For $m=D$ this gives $H>D/10000$. For any $m\ge D$, use $\lfloor m/D\rfloor$ disjoint blocks of $D$ departures, each with its following endpoint above the floor. Each block is distinct by the period bound. They cover at least $m/2$ departures, giving $H>m/20000$ even if the full segment repeats.

In ordinary time, the first $D$ shortcut edges from $x=X$ expand into at most $2D$ steps. The even predecessor of the retained state $x_i$ for $1\le i<D$ is the departure at the last step of the preceding expanded edge, and has value $2x_i$. Since $x_0=X$, every high retained departure has such a predecessor inside the prefix. If all ordinary states through time $2D$ are at least $X$, the shortcut count thus gives more than $D/10000$ even departures above $2BX$. For any ordinary prefix of $P\ge2D$ steps from the original start with no descent, the first $D\lfloor P/(2D)\rfloor$ complete shortcut edges fit inside it. Applying the block estimate and the same predecessor count gives more than $D\lfloor P/(2D)\rfloor/10000\ge P/40000$ high even departures. The counts concern departure times, so repeated values in longer prefixes retain their multiplicity.

For $n=71$, (4) gives $(C_n,D)=(92{,}160,184{,}462)$ at $29/9$ and $(368{,}640,737{,}422)$ at $10/3$. Here $r=0$, so the score inequality gives $H\ge\lceil(D-n-C_n)/(n+1)\rceil=\lceil(D/2)/72\rceil$, namely $1{,}281$ and $5{,}121$ respectively. The shortcut departures are distinct by the period bound, as are their even predecessors. The examples hold throughout the octave $2^{71}\le x<2^{72}$.

For either threshold, (4) gives $D\le40(n+1)2^{E+\rho}X^\lambda+2n$. At $29/9$ we have $\lambda<137/2000$, $E+\rho<7/2$ and $2^{7/2}<12$, hence $D<482(n+1)X^\lambda$. For $t=(\ln X)/2000$, use $te^{-t}\le1/e$ and $\ln2>2/3$ to get $n+1\le(3000/e)X^{1/2000}+1<3000X^{1/2000}$, giving $D<1{,}446{,}000X^{0.069}$. At $10/3$ the exact growth exponent in the bound with the factor $n+1$ is $\lambda=2372/24727+13/4999+3/8192<1/10$. The strict difference absorbs $n+1=O(1+\ln X)$, yielding $D=O(X^{0.1})$.

### Cycle occupation

**Corollary.** In every nontrivial positive shortcut cycle of least period $L$ and minimum $X$, strictly more than $L/10000$ states exceed $(10/3)X$. In the ordinary cycle, the even states above $(20/3)X$ account for more than $1/10000$ of the even states and more than $1/[10000(1+\alpha)]>1/16310$ of all states. The shortcut and ordinary maximum ratios therefore strictly exceed $10/3$ and $20/3$, respectively. The same occupation fractions hold at the lower thresholds in Theorem 1.

Bařina reports convergence verification through $2^{71}$, so a nontrivial cycle has minimum $X\ge2^{68}$. If it had $H\le L/10000$ high clocks, the sum of scores over all cyclic starts would be $(n+r+1)H$, including windows that wind around the cycle. Fewer than $L/2$ starts could then have score at least $r+1$, giving $L/2<C_n$ by distinctness. This contradicts $L\ge u>A_n$. [\[4\]][barina]

By the even-predecessor bijection in §1 the number of ordinary even states above $2BX$ is precisely $H$. The ordinary fractions therefore satisfy $H/L>1/10000$ and $H/(L+u)>1/[10000(1+\alpha)]$ by $u/L<\alpha$. The rational logarithm enclosure also checks $\alpha<631/1000$, giving the stated $1/16310$ comparison.

## 3. Occupation at wider ratios and separation on open paths

Set $\kappa=4.116201$, $M=1+\kappa$, and
$$
 K_*=3^{\,1+3/[M(1+\gamma)]}=3.849030770060326\ldots .
$$
Bondareva, Luchin and Salikhov, Theorem 1 (2018, p. 18), give $|h_1\ln2+h_2\ln3+h|>H^{-\kappa}$ for integers $h_1,h_2,h$ and sufficiently large $H=\max(|h_1|,|h_2|)$. Taking $(h_1,h_2,h)=(-n,u,0)$ with $0\le u\le n$ gives an absolute $A>0$ such that
$$
 |u\ln3-n\ln2|\ge A n^{-\kappa}\qquad(n\ge1).
 \tag{5}
$$
For the finitely many smaller coefficient pairs the form is nonzero by unique factorization. [\[3\]][bls]

**Theorem 2.** For every fixed $K<K_*$ there is a $c(K)>0$ such that, in every least-period shortcut cycle of sufficiently large minimum $X$, at least a fraction $c(K)$ of the states exceed $KX$. The same fraction applies to the $m$ departures of every shortcut path $x_0,\ldots,x_m$, $m\ge1$, of distinct states with $x_i\ge X$ for every $i$ and $|x_m-x_0|\le Cm$. Here $C\ge0$ is fixed, $X$ may be real, and the required height depends on $K,C$. The threshold is ineffective.

For a path with $v$ odd departures, the endpoint logarithm has absolute value at most $Cm/X$ by the mean-value theorem. The total logarithmic correction in (1), in natural logarithms, is at most $m/(3X)$. The same estimates hold for one lap of a cycle with $C=0$. Together with (5) these give
$$
 A m^{-\kappa}\le |m\ln2-v\ln3|\le (C+1/3)m/X,\qquad m\gg_C X^{1/M}.
$$
This estimate uses the common floor over the entire path. It applies to both signs of the endpoint difference and of the linear form.

Take $3<K<K_*$. The exponent $\theta(K)$ in §4 is $(1+\gamma)\log_3(K/3)/3<1/M$. At $N=\lceil(4/3)\log_2(\lceil(K-1)X\rceil+1)\rceil$, the sparse count in §4 bounds by $A_X=o(m)$ the number of starts in the band whose $N+1$ observations contain at most $\lfloor\rho N\rfloor$ states outside it. Here $\sigma=100\rho>0$ is chosen sufficiently small in terms of $K$ so that the exponent in (11) is strictly below $1/M$. Also $N=o(m)$.

Put $q_N=(N+1)/(\lfloor\rho N\rfloor+1)$. In a cycle with $h$ high departures, the total number of outlier appearances over all cyclic windows is $(N+1)h$, since each offset visits every state once. At most $q_Nh$ windows exceed the budget and at most $h$ have high sources. The other sources are distinct, so $A_X\ge m-(1+q_N)h$.

For a general positive $m$-step segment with $m\ge N$, let $h$ count departures outside $[X,KX]$, $I$ indicate that the terminal observation is outside the band, and $R$ be the largest multiplicity of a departure state. The $m-N+1$ full windows have at most $(N+1)(h+I)$ outlier appearances. At most $h$ windows have outlying sources, and at most $q_N(h+I)$ exceed the budget. Each qualifying source occurs at most $R$ times, hence
$$
 \frac{h}{m}\ge \frac{1}{1+q_N}
 \left(1-\frac{R A_X+N-1+q_N I}{m}\right).
 \tag{6}
$$
The terminal charge does not require the endpoint to be distinct from the departures. For distinct departures, any fixed $\Delta>0$ and sufficiently small fixed $\rho$ give $A_X\le X^{\theta(K)+\Delta/2}$ by (11). Thus if $m\ge X^{\theta(K)+\Delta}$, the outlier fraction is at least $\rho/(1+\rho)-o(1)$ without a floor hypothesis.

For the near return in Theorem 2, $R=1$ and $A_X+N=o(m)$, while every outlier is above $KX$. Together with the cyclic bound this gives $c(K)=\rho/[2(1+\rho)]$ for sufficiently large $X$. For $K\le3$ use any fixed $K'\in(3,K_*)$ and its constant. In an ordinary cycle the even-predecessor bijection gives at least the same fraction of even states above $2KX$, and at least $c(K)/(1+\alpha)$ of all states are such even states. Cycles of shortcut ratio at most any fixed $K<K_*$ must have one of finitely many smaller integer minima, each determining at most one cycle. In ordinary units this gives finiteness at every fixed ratio $R<2K_*$, including $R=7.698$.

**Asymptotic dichotomy from an original start.** Fix $3<K<K_*$ and $\beta>\theta(K)$. For every sufficiently large integer $x$ and every $m\ge\lceil x^\beta\rceil$, either a state through shortcut time $m$ lies below $x$ or a positive fraction of the first $m$ departures exceed $Kx$. The fraction and height threshold can depend on $K,\beta$. For $1\le K\le3$, any $\beta>0$ works by taking $K'>3$ sufficiently close to three.

Indeed, if there is no descent, take $X=x$ in (6). Choose $\Delta>0$ with $\theta(K)+\Delta<\min(\beta,1/M)$ and fix $\rho$ as above. When departures repeat, determinism gives a distinct preperiod followed by a cycle of least period $L$ and minimum at least $x$. By the length estimate from (5) with $C=0$, $L\gg x^{1/M}$. Each cycle state appears at most $\lceil m/L\rceil$ times, while each preperiod state appears once. Hence $RA_x/m\le A_x/m+A_x/L=o(1)$. For distinct departures use $R=1$. Equation (6) gives the claimed positive fraction uniformly in $m$. Expanding the first $m$ complete shortcut steps from an original start gives the ordinary version at time $2m$, with the ceiling $2Kx$ and half the guaranteed fraction, by the predecessor count in §2.

**Theorem 3.** Fix $1<K<K_*$. For all sufficiently large real $X$, any finite shortcut segment in $[X,KX]$ has, for every $i<j$,
$$
 \operatorname{sgn}(x_j-x_i)=\operatorname{sgn}(G_j-G_i),\qquad
 |x_j-x_i|\ge \tfrac12 A\,X(j-i)^{-\kappa}.
 \tag{7}
$$
If $3<K<K_*$, for every fixed $\beta\in(\theta(K),1/M)$ the first exit is $O_{K,\beta}(X^\beta)$ steps from any start in the band, and the pairwise gaps are $\gg_{K,\beta}X^{1-\kappa\beta}$. For $K\le3$, use any fixed containing band with $3<K'<K_*$ and its exponent. The height onset for (7) is ineffective.

To prove this, write $n=j-i,\ u=h_j-h_i,\ \lambda=u\ln3-n\ln2$. Equation (1) gives
$$
 \ln(x_j/x_i)=\lambda+E,\qquad 0\le E\le n/(3X).
 \tag{8}
$$
The mean-value theorem gives $|x_j-x_i|\ge X|\ln(x_j/x_i)|$. If at most $B$ integers start a confined window of $N$ steps, any confined prefix of $U=B+N$ steps has a repeat, because the $B+1$ states at indices $0,\ldots,B$ all start such a window. Thus excluding equality for all confined pairs of separation at most $U$ excludes the $U$-step prefix itself. From any starting point the first exit is then at most $U$, so the comparison applies to every pair on any confined path.

The confined-start count in §4 gives an integer bound $B=O_{K,\beta}(X^\beta)$ with $N=O(\log X)$. For $1\le n\le U$, (5) and (8) give $E/|\lambda|\le U^{1+\kappa}/(3AX)=o(1)$. An upper bound of $1/2$ gives both signs and the gap in (7).

For short lags, the common floor alone also gives separation across excursions. If $n2^n\le X$, the gain $3^u/2^n$ differs from one by at least $2^{-n}$. For positive gain drift the additive correction is nonnegative, giving a gap at least $X2^{-n}$. For negative drift the logarithmic gain is at most $-2^{-n}$ and the correction is at most $2^{-n}/3$. Thus the sign agrees with the gain and the absolute gap is at least $2X/(3\cdot2^n)$ in either case.

**Theorem 4.** For every real $X\ge2^{68}$, any shortcut segment confined to $[X,(29/9)X]$ has the strict order in (7) and has absolute gaps at least two. From anywhere in that band the first exit is at most
$$
 U_b=(8(b+4)+3)2^{\lfloor17(b+4)/256\rfloor+3}+b+3,\qquad
 b=\lfloor\log_2 X\rfloor .
$$

Take $N=b+3$, $\delta=651/10000$. The verifier checks $\ln(29/27)+71/(3\cdot2^{68})<\delta\ln3$. Because $(b+3)2^{-b}$ decreases, the grade range in (1) is narrower than $1+\delta$. Write the strip as $[\rho-1-\delta,\rho]$ for $h_i-i\alpha$, with $\rho\in[0,1+\delta]$. At most four interior breakpoints per clock arise as an endpoint of the grade interval crosses an integer. Counting the open intervals, singleton breakpoints and boundary phases gives at most $8(N+1)+3$ lists. The second grade is available exactly for $\{i\alpha+\rho\}\le\delta$.

The verifier brackets $\alpha$ between $p/2^{40}$ and $(p+1)/2^{40}$ with $p$ odd. For the first 1024 rotation points the displacement from this rational grid is in $[0,1023/2^{40}]$, so a $\delta$-arc can draw only from rational grid points in an arc enlarged by that amount. In integer grid units the span is at most $\lfloor 2^{40}\delta+1023\rfloor$. On the doubled sorted circular list a maximal arc can start at its first hit, so counting from each point verifies all closed arcs. The tests bound hits by 68 for a full block of 1024 and by $17r/256+3$ for each prefix of $r$ points. Translation gives the same bounds for successive blocks. Thus there are at most $\lfloor17(N+1)/256\rfloor+3$ optional grades. The diameter is less than $2^N$, so the number of starts is bounded by $B=U_b-N$.

For $68\le b<16384$ the verifier splits the bit lengths into eight intervals $[a,d)$, repeatedly doubling the lower endpoint and clipping at 16384. For each interval with $U=U_{d-1}$, it certifies a coprime $P,Q$ with $Q\ge2U,\ |\alpha-P/Q|<Q^{-2}$ and $2^a>4Q(U+3)$. For $1\le n\le U$, the triangle inequality gives $|u-n\alpha|\ge1/Q-n/Q^2\ge1/(2Q)$. Hence $|\lambda|>1/(2Q)>(n/3+1)/X$, since $\ln3>1$. Equation (8) gives the sign and a strict gap greater than one. The logs in this verifier use the same positive series as in §2, with fixed truncation and a rational geometric remainder bound. [Exact open-path verifier](supplement/verify_order.py)

For $b\ge 16384$, the formula for $U_b$ gives $U_b\le 2^8 b\,2^{17b/256}\le2^{35b/512}$. For the first bound use $8(b+4)+3\le9b$ and bound the floor exponent by $17b/256+4$, leaving room for the $b+3$ term. For the second bound, if $2^k\le b<2^{k+1}$ then $8+\log_2 b<k+9\le2^{k-9}\le b/512$ for $k\ge14$. Thus $2^{33}U_b^{14.3}\le2^{33+(1001/1024)b}<X$.

If $\lambda<0$ and $u\ge1$, put $r=158497/100000$. The verifier checks $\gamma<r<\exp(0.46057)$, $r<2$, and $r\ln2-\ln3>2^{-32}$. If $n/u\ge r$, then $|\lambda|>2^{-32}$. If $\gamma<n/u<r$, then $u\ge2$, and Rhin's bound yields $|\lambda|\ge n^{-13.3}>\!2^{-32}n^{-13.3}$. In this range the coefficient height is $n$ and the form is positive when written $n\ln2-u\ln3$. In either case $|\lambda|>(n/3+1)/X$ follows from the tail bound on $U_b$, using $n/3+1\le 2n$. For $u=0$, $x_i=2^n x_j$, giving the negative sign and a gap at least $X$. [\[5\]][rhin] · [\[6\]][rt]

If $\lambda>0$, the sign is automatic. The inequality $\ln(1+t)\ge t/(1+t)$ gives $XE\ge u/(3K+1/X)>1$ for $u\ge11$, since $K=29/9$ and $X\ge2^{68}$. For $u\le10$ we have $n<u\gamma<16$, so the first rational interval's estimate gives $\lambda>1/X$ at every $X\ge2^{68}$. This proves the gap for $n\le U_b$, and the preceding prefix argument completes the proof for every pair and the first exit. At small heights, $3,5,8,4$ and $6,3,5$ give opposite unit gaps inside bands of ratio at most $29/9$.

## 4. Counting located starts with sparse two-sided outliers

For $3<K\le6$, set
$$
 d=\log_3(K/3),\quad a=1-\alpha,\quad P=(d-a)_+,\quad S=d-2P,\qquad
 D=S+\gamma P,\quad J=S\log_2(8/3)+P\log_2(27/5).
 \tag{9}
$$
We prove that for any $\epsilon>0$, the number of starts in $[X,KX]$ with their next $N$ steps confined there is $O_{K,\epsilon}(X^{\theta(K)+\epsilon})$, where
$$
 \theta(K)=(4D-J)/3.
 \tag{10}
$$
For the confined count it suffices to take $N=\lceil\frac{4+\sigma}{3+\sigma}\log_2 Y\rceil$, where $Y=\lceil(K-1)X\rceil+1$ and $\sigma>0$ is sufficiently small and fixed. Longer confined windows satisfy the same bound by restriction. For $K\le9/2$, $P=0$ and (10) reduces to the formula in Theorem 2.

For the sparse count, take $N=(4/3+o(1))\log_2 X$, $0<\sigma\le1/10$ and $0<\rho\le\sigma/100$ fixed. Let $A_X$ count the integer starts in $[X,KX]$ with at most $\lfloor\rho N\rfloor$ observations outside that closed band. Both sides are allowed. We prove
$$
 A_X\le X^{\,\frac43[D-J(1-\sigma)/(4+\sigma)+H_2(\rho)+9\rho]+o(1)},
 \tag{11}
$$
where $H_2(\rho)=-\rho\log_2\rho-(1-\rho)\log_2(1-\rho)$ and $H_2(0)=0$. The exponent approaches (10) with error $O_K(\rho\log(1/\rho))$ when $\sigma=100\rho\downarrow0$. The proof also gives the confined count by using the empty mask and the shorter depth above.

### 4.1. The forward strip and fixed data

Fix the mask of clocks in $\{1,\ldots,N\}$ with observations outside $[X,KX]$, and write $t$ for its size. The last good observation $x_g$ at or before any clock $i$ exists since clock zero is good. Because $T(y)\ge y/2$, all observations satisfy $x_i\ge x_g2^{-(i-g)}\ge X2^{-t}$, even along a final run of outliers. The correction in (1) is bounded by
$$
 0\le c_i\le\eta_X=\frac{N2^{\lfloor\rho N\rfloor}}{3X\ln3}=o(1),
$$
since $2^{\rho N}=X^{4\rho/3+o(1)}$. In the empty-mask case take $\eta_X=N/(3X\ln3)$. At the good clocks the range of $h_i-i\alpha$ is at most $W=1+d+\eta_X$ and includes zero. These grades fit in $[\phi-W,\phi]$ with $0\le\phi\le W$. Write $w=W-1$. With $H_i=\lfloor i\alpha+\phi\rfloor$ and $f_i=\{i\alpha+\phi\}$, the good grades are $H_i$ or, if $f_i\le w$, $H_i-1$. The phase interval has $O(N)$ open cells and singleton breakpoints on which grade lists and the comparisons with $a,\alpha,w$ are fixed.

At every clock, even a masked one, call the potential optional site ordinary when $f_i\le w$ and $f_i<\alpha$. Its incoming increment of $H$ is one. If $f_i\ge a$, then $f_{i+1}=f_i-a$ is again potential ordinary. If $f_i<a$, then $f_{i+1}=f_i+\alpha\ge\alpha$, and the next increment of $H$ is zero. Since $\alpha<2a$, the runs of such sites have length one or two. Use the incoming bits of each run and its following bit as its support. The supports are disjoint. Let $z$ be the size of the union of the mask and exceptional sites $\alpha\le f_i\le w$. Mark each bit incident to one of these $z$ clocks. Discard runs abutting the endpoints or sharing a marked bit. At most $2z+2$ runs are discarded, since each bad or exceptional clock meets at most two bits. The remaining supports have good endpoints of unique grade. The indicator that a grade is lowered cannot decrease within a run, because that would create an increment of two. Thus a run of length $m$ permits all $m+1$ placements of a single zero among $m$ ones. The bit sets are $A=\{01,10\}$ and $B=\{011,101,110\}$.

For large $X$, $w\to d\le\alpha$. Uniformly in phase and arc, $L$ successive rotation points meet an arc $I$ in $L|I|+o(L)$ points. Indeed, the normalized geometric sum tends to zero in each nonzero Fourier mode. Continuous upper and lower approximations and uniform trigonometric approximation give equidistribution on each fixed interval. Translating the arc, sandwiching it between intervals on a finite mesh and then refining the mesh proves uniformity including endpoints. The exceptional sites number $o(N)$, including at $K=6$, so $z\le t+o(N)$. Over any interval of $T\asymp N$ bits the test $a\le f_i<\alpha,\ f_i\le w$ gives a density $P+o(1)$ of adjacent potential ordinary pairs, while the potential ordinary sites have density $d+o(1)$. Before the mask deletions there are $PT+o(N)$ double runs and $ST+o(N)$ single runs. Runs meeting the segment boundaries cost $O(1)$.

For each phase cell and mask, record all marked bit values and the lowering flags of all good optional sites outside the retained runs. The record costs at most $2z+2(2z+2)+z=7z+4$ bits, including the optional anchors at ends and re-entry. Any unmarked bit outside a retained support has both endpoint grades determined by the record and the strip. Keep records admitting an actual witness and allow the full independent $A,B$ choices on retained supports. The choices change only internal grades on those supports, so all good grades still satisfy the strip and all boundary grades are common within the family. Treat each exterior fixed bit as its own component. Every actual word belongs to such a product of at most $2^{DN+o(N)}$ words. The union over masks, records and phases costs at most $2^{[H_2(\rho)+7\rho]N+o(N)}$. For the mask bound, weighting the binomial sum by $(\rho/(1-\rho))^{j-\rho N}\ge1$ for $j\le\rho N$ gives $2^{NH_2(\rho)}$ when $0<\rho<1/2$. The empty mask costs one choice.

For each word in a product family and any clock $i$, the last good clock $g\le i$ is at most $t$ steps back. The binary increments imply $|(h_i-i\alpha)-(h_g-g\alpha)|\le t$, including a final outlier run without re-entry. Hence every grade satisfies
$$
 \phi-W-t\le h_i-i\alpha\le\phi+t .
 \tag{12}
$$

### 4.2. Numerators and the fourth moment

For a length-$T$ segment of odd count $b$ with local odd positions $r_1<\cdots<r_b$ counted from zero, write its affine numerator as $F=\sum_{j=1}^b3^{b-j}2^{r_j}$. Each component contributes its local numerator times $2^t3^v$, where $t$ is the preceding number of bits and $v$ is the subsequent odd count. Both are fixed across the class. The local numerators are $1,2$ for $A$ and $5,7,10$ for $B$. Their unordered pair sums are $2,3,4$ modulo 3 and $10,12,14,15,17,20$ modulo 9, respectively, and are distinct in the stated moduli.

For four copies of a component-aligned segment, reduce $F_1+F_2-F_3-F_4$ modulo $3^b$. Fixed bits cancel. Divide out the ternary factor after the last free component and reduce modulo 3 or 9 according to its grade. Earlier contributions vanish and $2^t$ is a unit. The local unordered pairs must coincide, hence the local difference vanishes as an integer. Repeating backwards proves equivalence between the congruence, ordinary zero difference and equality of the unordered pairs at each component. Under independent uniform component choices, the collision probability for an alphabet of size $k$ with distinct unordered pair sums is $(k+4\binom{k}{2})/k^4$. For $s$ single and $q$ double runs this gives
$$
 \Pr(F_1+F_2=F_3+F_4)=(3/8)^s(5/27)^q .
 \tag{13}
$$
The local calculation is the one used in Paper 145, Lemma 3. Here the frequencies are those of the forward strip at the specified physical ratio. [\[7\]][p145]

Solving the affine source congruence gives $x_0\equiv-\sum_j 2^{t_j}3^{-j}\pmod {2^N}$ with the global odd positions $t_j$ in chronological order. For a segment beginning at clock $u$, write $H=h_u$, $m=N-u$ and $\nu=H+b$. Its contribution to $x_0/2^N\bmod1$ is $V=R_Z/2^m\bmod1$, with
$$
 R_Z=\sum_{j=1}^b 2^{r_j}[-3^{-H-j}]_{2^{m-r_j}},\qquad
 R_W=\sum_{j=1}^b 3^{b-j}[2^{-(m-r_j)}]_{3^{H+j}}.
$$
Here $[c]_d$ is the least nonnegative residue with denominators inverted modulo $d$. For any coprime $D_0,E_0>1$, $D_0[D_0^{-1}]_{E_0}-E_0[-E_0^{-1}]_{D_0}=1$: the left side is congruent to one modulo $D_0E_0$ and lies strictly between $1-D_0E_0$ and $D_0E_0$. Applying this term by term gives $2^m R_W-3^\nu R_Z=F$. Also $R_Z\le T2^m$, $R_W\le T3^\nu$. By (12) applied at the end and just after each odd departure, $b-j\le\alpha(T-r_j-1)+W+2t$, so $F\ll_K T2^T3^{2t}$.

Quantize by $Q_p(V)=\lfloor2^p\{V\}\rfloor$ in $\mathbb Z/2^p\mathbb Z$, and let $f$ be the law of this value. In a circular four-copy collision with signs $+,+,-,-$, the signed sum of the fractional quantization remainders has absolute value less than four grid units. For some integer $k=O(N)$ this gives
$$
 b_0=R_{Z,1}+R_{Z,2}-R_{Z,3}-R_{Z,4}-k2^m,\qquad
 |b_0|<4\,2^{m-p}.
$$
Define $a_0$ by the same signed sum with $R_W$ and $k3^\nu$. Then $2^m a_0-3^\nu b_0=F_1+F_2-F_3-F_4$ and $|a_0|\ll N3^\nu,\ |b_0|\ll N2^m$. The separation conditions are $p\asymp N,\ m\ge p,\ \gamma\nu\ge p$ and $4\max F\le 2^p e^{-\delta N}$ for a fixed $\delta>0$. Under them the difference is zero at sufficiently large $N$, by Paper 145, Lemma 4. [\[7\]][p145]

For completeness, put $z_1=2^ma_0,\ z_2=3^\nu b_0$. Use the forms $z_1-z_2,z_2$ at infinity and the two coordinates at 2 and 3. If either coordinate vanishes and the difference is nonzero, the difference has absolute value at least $2^p$. Otherwise the product of the six absolute values is at most $|z_1-z_2|\,|b_0|2^{-m}\le4e^{-\delta N}$. The integer vector has norm at most $e^{O(N)}$, so the fixed-place integral Subspace Theorem puts these vectors in finitely many rational lines for large $N$. Since $|z_2|\ge 2^p$, the inequality $|z_1/z_2-1|\le e^{-\delta N}$ eventually excludes all lines except the diagonal, where the difference is zero. This is the ineffective step. [\[8\]][bilu]

With $\widehat f(k)=\mathbb E e^{2\pi i kQ_p(V)/2^p}$, the average over $k\bmod 2^p$ of $|\widehat f(k)|^4$ is the quantized collision probability by orthogonality. By separation it is bounded by (13).

### 4.3. Four disjoint segments

Use $p=\lfloor N/(4+\sigma)\rfloor$. Start at the first component boundary at or after $3\sigma p$, then take four consecutive segments of length $\lfloor(1-\sigma)p\rfloor+O(1)$, rounding each end up to a boundary. Consecutive boundaries are at most three bits apart. The first end is at least $(1+2\sigma)p-O(1)$, the last start at most $3p+O(1)$, and the last end at most $(4-\sigma)p+O(1)$. Thus $m\ge p$. At each end clock $e$, (12) gives $\gamma\nu\ge e-\gamma(W+t)\ge p$ for large $N$, since $p\ge N/5-1$ and $t\le\sigma N/100$. Moreover
$$
 \log_2(4\max F)\le (1-\sigma)p+2\gamma t+O_K(\log N)
 \le p-\sigma N/20 .
$$
Indeed $\sigma p\ge\sigma(N/5-1)$ and $2\gamma t\le4\sigma N/100$. The separation therefore applies uniformly despite the excursions.

For segment $i$ of length $T_i$, let $\ell_i$ count the discarded potential runs with support entirely in that segment. Runs crossing an endpoint cost only $O(1)$ by the bound on support length. By disjointness $\sum_i\ell_i\le2z+2$. Each missing component costs less than three bits in the exponent of (13), so the fourth moment of the quantized law of segment $i$ is at most $2^{-JT_i+3\ell_i+o(N)}$. Condition on the exterior components of a uniform word in the product family. The four actual segment contributions are independent under this conditioning. Fourier inversion and Hölder bound each atom of their quantized sum by the product of the four fourth roots, at most $2^{-J(1-\sigma)p+(3/2)z+o(N)}$. For an arc of length $2^{-p}$, the unquantized sum can lie in the arc only if its quantized sum belongs to at most six grid residues, since the four discarded fractions together are in $[0,4)$ in grid units. The fixed exterior contribution translates the arc, and the bound survives averaging.

For the confined depth, $N-p\ge\log_2Y$ by its definition. At sparse depth, $N-p=(\frac43\frac{3+\sigma}{4+\sigma}+o(1))\log_2X$, whose coefficient is strictly greater than one. Thus the normalized band is contained in an arc of length $2^{-p}$ in either case. The band integers have distinct residues modulo $2^N$ for large $X$. Multiply the arc concentration by the word population and sum over phases, masks and records. Using $z\le t+o(N)$ and $7+3/2<9$, the result is
$$
 2^{DN-J(1-\sigma)p+[H_2(\rho)+9\rho]N+o(N)} .
$$
At sparse depth this is (11). With the empty mask and the confined depth the count is $X^{((4+\sigma)D-(1-\sigma)J)/(3+\sigma)+o(1)}$, proving the claimed confined bound by choosing $\sigma$ small for the desired $\epsilon$.

### 4.4. Short windows and the earlier physical-band bounds

For comparison, given $3<K\le6$ and $0<t<1$, let $n=\lfloor t\log_2 X\rfloor$. The number of confined $n$-step starts is
$$
 X^{\,1-t(1-D)+o(1)}.
 \tag{14}
$$
The strip supplies the upper bound $2^{nD+o(n)}$ words, each with $O_K(X/2^n)$ lifts. For the lower bound take $3<K'<K$, set $\rho=0$ and $w'=\log_3(K'/3)<\alpha$, and allow every complete ordinary run described in §4.1 to vary, fixing the boundary grades at their baseline values. This gives $2^{nD(K')+o(n)}$ words with $G_{\max}/G_{\min}\le K'$. For any such word the affine offset is $\sum_{j<i}(w_j/2)G_i/G_{j+1}\le nK'/2$ at clock $i$. The source interval
$$
 \left[X/G_{\min},\, (KX-nK'/2)/G_{\max}\right]
$$
has length $\gg_{K,K'}X$ for large $X$. Every positive lift there is confined. As $2^n=o(X)$, each word has $\gg_{K,K'}X/2^n$ lifts and different words give disjoint lifts. Letting $K'\uparrow K$ proves (14). At $n=\lfloor\log_2 X\rfloor$ the strip still gives the upper bound $X^{D+o(1)}$, whereas the lower lift argument requires $t<1$.

Paper 145, Theorem 3 and §9, count odd sources with sparse excess defects in a one-sided mechanical encoding. They clip the defects, sum translated source intervals and account for the terminal lifts from changing the binary duration. The source exponent $11/25$ gives a cycle alternative between a positive density of canonical defects at least two and an approximation bound of order $u^{-25/11}$. The mask in (11) records observed states on either side of a physical band and includes both parities. Conditioning preserves the original duration and source modulus. Paper 145 also supplies precedents for the four-copy estimate and the use of window incidence within one orbit. [\[7\]][p145]

Paper 145, Theorem 6, bounds visits by distinct odd states in a physical band, charging an exit term for several visits. Below odd-state ratio four it gives any exponent above $0.4333973955\ldots$. A shortcut cycle of ratio at most six has odd-state ratio strictly below four by §1. Equation (10) agrees with that exponent at $K=6$ and retains the dependence on the shortcut ratio below six. Paper 140, Theorem 1, gives a bound on the least positive source of each critical mechanical word. [\[7\]][p145] · [\[9\]][p140]

Paper 112 uses episodes of odd cycle states above twice the minimum and charges episode starts to a deficit from the mechanical numerator bound. Paper 174 groups consecutive odd-to-odd transitions of division exponent one, including a bound on rises outside the longest groups conditional on no first descent. Those groups depend on the division word. The present deadline counts visits above a specified physical height in ordinary time, regardless of how they are grouped. [\[10\]][p112] · [\[11\]][p174]

The classical questions are whether every positive orbit reaches one, whether a nontrivial positive cycle can exist, and whether a positive orbit can be unbounded. A proof of strict descent from every start above one would give convergence by induction. Theorem 1 supplies a quantitative alternative when strict descent has yet to occur. Tao's almost-bounded orbit result concerns almost all starts in logarithmic density. [\[12\]][lagarias] · [\[13\]][tao]

## Appendix A. Explicit relative near returns at high floors

In each direction there are arbitrarily high shortcut paths of ratio strictly less than three whose endpoints have arbitrarily small relative gap. Take successive continued-fraction convergents $a/n$ of $\alpha$, which alternate across $\alpha$ and satisfy $|a-n\alpha|<1/n$. Use $\rho=0$ for a lower convergent and $\rho=a-n\alpha$ for an upper convergent. The mechanical grades $h_i=\lfloor i\alpha+\rho\rfloor$ have $h_0=0,\ h_n=a$, and their differences are bits. The gains $G_i$ have ratio strictly below three because $h_i-i\alpha=\rho-\{i\alpha+\rho\}$ has range strictly below one.

Let $B_n$ be the affine numerator in §1 and $r=[-3^{-a}B_n]_{2^n}$. Choose the positive lift
$$
 x_0=r+(4n+1)2^{2n}.
$$
The offsets $x_i-G_i x_0$ are between zero and $3n/2$ by the offset formula in §4.4. The gains have common denominator $2^n$, so $3G_{\min}-G_{\max}\ge2^{-n}$; hence $x_i$ have ratio strictly below three. Also $G_{\min}>1/3$, so the minima tend to infinity. Since $G_n=3^a/2^n\ne1$, $|G_n-1|\ge 2^{-n}$, and the offset is too small to reverse the sign of $x_n-x_0$. Finally
$$
 \left|\frac{x_n}{x_0}-1\right|\le |3^a/2^n-1|+3n/(2x_0)\longrightarrow0
$$
on both sequences. For example the exact replay at $(n,a)=(84,53)$ gives a positive gap with relative size below $21/10000$, and at $(485,306)$ a negative gap with relative size below $11/10000$. Both minima exceed $2^{68}$. [Exact example verifier](supplement/verify_examples.py)

For these open paths we expand each odd shortcut step into its two ordinary steps. The endpoints and minimum are unchanged. The ordinary maximum is $\max\{x_0,\,2\max_{1\le i\le m}x_i\}$, because the even departures are twice the shortcut arrivals and each odd departure increases at its next step. Thus the ordinary ratio is below six in the examples. A maximum occurring only at the start lacks a paired predecessor within the expansion.

More generally, the expansion of $m$ complete shortcut steps with $v$ odd departures has $m+v$ ordinary departures and $m$ even departures. Those even departures pair with the $m$ shortcut arrivals $x_1,\ldots,x_m$. If $h$ shortcut departures exceed $KX$, the count of even ordinary departures above $2KX$ is $h-\mathbf1_{\{x_0>KX\}}+\mathbf1_{\{x_m>KX\}}$. This accounts for both endpoints when applying Theorem 2 to an expanded segment. An arbitrary ordinary segment can end immediately after an odd step, before its paired halving. Such endpoints are outside this complete-step correspondence.

## Appendix B. Residence in a closed threefold band

For an integer floor $X\ge2$, let $E(X)$ be the maximum first-exit index over all positive integer starts in $[X,3X]$. Write $n=\lceil\log_2(2X+1)\rceil$. Then
$$
 E(X)\le2n+1
$$
for every $X\ge2$, and $E(X)=(1+o(1))\log_2 X$ on a set of integer floors of natural density one. Paper 140, Theorem 1, also gives the uniform asymptotic upper coefficient $3/2$, as explained below. The floor one admits the shortcut cycle. [\[9\]][p140]

Put $g(q)=\min_{1\le j\le q}\|j\alpha\|$. If $(n+1)/(3X\ln3)<g(n+1)$, the range of $s_i=i\alpha-h_i$ over a confined $n$-step window is strictly below one. In fact, when the range reaches one, its excess over one comes from two distinct extreme clocks and is at least $g(n)$, since $\alpha$ is irrational. This would contradict (1). A range below one is equivalent to a mechanical word, with phases in $[\max_i s_i,1+\min_i s_i)\subset[0,1)$. The $n$ distinct breakpoints $\{-i\alpha\}$, $1\le i\le n$, partition the phases into $n+1$ intervals giving distinct words. As $2^n>2X$, each word has at most one lift in the band. If $B\le n+1$ of them are confined, the first $B+1$ starts of $n$-step windows in a confined $(B+n)$-step prefix force a return of duration $p\le B$. The return identity (2) on that subsegment gives $0<p\alpha-u<p/(3X\ln3)<g(n+1)$, a contradiction.

The verifier checks the gap hypothesis for $X\ge52$ and directly tests smaller floors. For $n\le14$ it brackets $g(n+1)$ from rational log bounds and computes the integer cutoff for $X$ in each dyadic range $2^{n-2}\le X\le2^{n-1}-1$. For $15\le n\le256$, the rational approximation $306/485$ has error less than $1/(2\cdot485\cdot257)$, giving $g(n+1)>1/(2\cdot485)$. Here $2\cdot485(n+1)<3\cdot 2^{n-2}$ first holds at $n=15$ in this range and propagates by doubling on the right. For $n\ge256$, Rhin gives $g(n+1)\ge (n+1)^{-13.3}/\ln3$. For $j\ge2$ apply his bound to $j\ln2-k\ln3$ with $k$ the nearest integer to $j\alpha$ and $0\le k\le j$; for $j=1$ use $\ln(3/2)>1/3$. The inequality $(n+1)^{14.3}<2^{n-2}$ holds at $n=256$ since $257<2^9$, and the left grows by a factor below two because $14.3/(n+1)<\ln2$. This proves the gap on the tail. The same mechanical classification holds uniformly for $n=O(\log X)$ by (5). Thus a longest window at large $X$ is mechanical, with least positive source at most $3X$. Paper 140 bounds that source below by $2^{(2/3-o(1))n}$ at depth $n$, giving $E(X)\le(3/2+o(1))\log_2 X$. [Exact threefold verifier](supplement/verify_threefold.py) · [\[6\]][rt] · [\[9\]][p140]

To see the typical-floor coefficient, a mechanical word with phase interval of length $\delta_w$ has $G_{\max}/G_{\min}=3^{1-\delta_w}$ and offsets at most $3n/2$. The widest phase interval has $\delta_w\ge1/(n+1)$. The feasible source interval from §4.4 at $K=3$ has length at least $X(3^{\delta_w}-1)-3n/2$, using $G_{\min}\le1\le G_{\max}$. At $n=\lfloor\log_2 X\rfloor-\lceil\log_2\log_2 X\rceil-2$, this length exceeds $2^n$ for large $X$. A residue lift yields $E(X)\ge\log_2 X-\log_2\log_2 X-O(1)$ uniformly.

Conversely, take an octave $Y\le X<2Y$ of integer floors and let $n=\lfloor\log_2(5Y)\rfloor+1$. Every such confined word is mechanical for large $Y$ by the gap criterion. Each word has at most one candidate source $z\in[Y,6Y]$. Its confined floors are the integers in $[\max_i x_i/3,\min_i x_i]\cap[Y,2Y)$. There are at most $6Y(\ln3)\delta_w+3n/2+1$, since $\min_i x_i\le zG_{\min}+3n/2$ and $\max_i x_i\ge zG_{\max}$. Summing over $n+1$ words gives $O(Y+n^2)=O(Y)$, because $\sum_w\delta_w=1$. For a floor $X$, the orbit attaining $E(X)$ supplies $(E(X)-n)_+$ distinct windows, since an earlier repeat would prevent exit. Thus $\sum_{Y\le X<2Y}(E(X)-n)_+=O(Y)$. At most $O(Y/\sqrt{\log Y})$ floors per octave have $E(X)>n+\sqrt{\log Y}$. Summing dyadic octaves and using the uniform lower bound gives the asserted natural-density result.

## Appendix C. An effective bound for the positive return form

For integers $L,u$ with $u\ge2$ and $\Lambda=L\ln2-u\ln3>0$,
$$
\boxed{\Lambda>u^{-9}.}
$$
For $u=1$ and $\Lambda>0$, one has $\Lambda\ge\ln(4/3)>1/4$. The integral argument gives the tail $u\ge2^{102}$ and also gives $|\Lambda|>2^{-51}u^{-17/2}$ throughout $3/2<L/u<2$. The finite certificate uses a 256-bit scale for the logarithms.

### Integral and clearing factor

Salikhov introduced the rational integral used here in 2007. Bondareva, Luchin and Salikhov list its three factors as $P_1,P_2,P_3$ on pp. 20–21. Published asymptotic estimates give stronger exponents. Priority for the numerical bound over all $u\ge2$ remains unresolved. Put $t=(x-35)^2$, $n=2m$ with $m$ a positive odd integer, and
$$
N(x)=[t(t-25)(t-49)]^m,\qquad
R(x)=\frac{N(x)}{x^{n+1}(70-x)^{n+1}}.
$$
Write $d_n=\operatorname{lcm}(1,\ldots,n)$ and $C=70\,2^m d_n$. The denominator has leading coefficient $-1$, so polynomial division gives an integral quotient. Symmetry under $x\mapsto70-x$ gives the partial fraction expansion
$$
R(x)=Q(x)+\sum_{i=1}^{n+1} a_i\bigl(x^{-i}+(70-x)^{-i}\bigr),
\qquad Q\in\mathbb Z[x],\quad \deg Q\le n-2.
$$
The weight for the coefficient of $x^j$ is its $p$-adic valuation plus $j$ for $p=7,5,3$, and its valuation plus $3j$ for $p=2$. For $t-49,t-25,t$, the respective minima over coefficients are displayed below; the coefficient of $x$ is $-70$ in each factor.

| Factor | $7$ | $5$ | $3$ | $2$ |
| --- | ---: | ---: | ---: | ---: |
| $t-49=x^2-70x+1176$ | 2 | 0 | 1 | 3 |
| $t-25=x^2-70x+1200$ | 0 | 2 | 1 | 4 |
| $t=x^2-70x+1225$ | 2 | 2 | 0 | 0 |

Weights add under multiplication term by term, so $[x^j]N$ has valuations at least $2n-j,2n-j,n-j,7m-3j$, in the indicated prime order. Now
$$
a_i=[x^{n+1-i}]N(x)(70-x)^{-n-1},\qquad
[x^k](70-x)^{-n-1}=\binom{n+k}{k}70^{-n-1-k}.
$$
Combining these yields $v_7(a_i),v_5(a_i)\ge i-2$, $v_3(a_i)\ge i-1$, and $v_2(a_i)\ge3i-4-m$. For $p=2$ the loss from $70^{-n-1-k}$ is $n+1+k$, which is at most $n+1+3k$. The only possible denominator primes of $a_i$ divide 70.

Consequently $r=Ca_1$ is integral. For $i\ge2$, every higher-pole endpoint term $Ca_i/((i-1)y^{i-1})$ is integral for $y\in\{28,30,35,40,42\}$. Indeed $d_n/(i-1)\in\mathbb Z$, and multiplying $a_i$ by $70\,2^m$ supplies at least $i-1,i-1,i-1,3(i-1)$ powers in the same prime order. Integrating $Q$ at integer endpoints requires only $d_n$. The simple poles integrate to $a_1\ln(x/(70-x))$, giving
$$
E_1=C\int_{35}^{40}R(x)\,dx=r\ln(4/3)-p_1,\qquad
E_2=C\int_{40}^{42}R(x)\,dx=r\ln(9/8)-p_2,
\quad p_1,p_2\in\mathbb Z.
$$
[\[2\]][salikhov] · [\[3\]][bls]

### Uniform bounds

Write $R(x)=F(t)^m/(1225-t)$ on the intervals of integration, with
$$
F(t)=\frac{t(t-25)(t-49)}{(1225-t)^2}.
$$
The signs are $E_1>0>E_2$ because $m$ is odd. On $0\le t\le25$, $|F(t)|\le (625/4)49/1200^2$. On $25\le t\le49$, $|F(t)|\le49\cdot144/1176^2$. Both bounds are strictly less than $25/4608$. Put $b=12/5$. One has $d_n\le4^n$, hence $C\le70\cdot32^m$. For the lcm bound, put $k=\lfloor n/2\rfloor$, $h=\lceil n/2\rceil$. Each prime power $p^j\in(h,n]$ contributes a factor $p$ to $\binom nk$ by its floor formula. Thus $d_n\mid d_h\binom nk$. For even $n$, use $\binom nk\le2^n$, and for odd $n>1$, the two equal central coefficients give $\binom nk\le2^{n-1}$. Induction from $d_1=1$ gives the stated bound. It follows that
$$
|E_1|+|E_2| < \frac{490}{1176} b^{-n}<\tfrac12 b^{-n}.
$$

A lower bound for the first integral comes from $38\le x\le38+1/8$, where $9\le t\le625/64$. There,
$$
F(t)\ge\frac{9(25-625/64)(49-625/64)}{1216^2}>\frac1{289},
\qquad \int_{35}^{40}R(x)\,dx>\frac{289^{-m}}{9800}.
$$

To bound $a_1$ by Cauchy's coefficient estimate, use the circle $|x|=25$ for $N(x)/(70-x)^{n+1}$. The six roots of $N^{1/m}$ are $28,30,35,35,40,42$. Pair any two factors $x-a$ with factors $70-x$ inside the $m$-th power. The squared ratio $|x-a|^2/|70-x|^2$ is decreasing as a function of $\cos(\arg x)$, since its derivative has the sign of $(70-a)(625-70a)<0$. Each ratio and each unpaired $|x-a|$ is therefore bounded by its value at $x=-25$. The single unpaired factor $1/(70-x)$ has modulus at most $1/45$. Including the Cauchy factor $25^{-2m}$ gives
$$
|a_1|\le \frac{G^m}{45},\qquad
G=\frac{3600\cdot3575\cdot3551}{25^2\cdot95^2}<10000.
$$
In particular $|r|<2\cdot600^n$, since $70/45<2$ and $32\cdot10000<600^2$.

### The integer residual

For $3/2<L/u<2$, put $A=2L-3u$ and $B=2u-L$, positive integers less than $u$. Then $\Lambda=A\ln(4/3)-B\ln(9/8)$. Take the least positive $n\equiv2\pmod4$ such that $b^n\ge u$; it satisfies $n<\log_b u+4$. The residual $D=Ap_1-Bp_2$ satisfies
$$
r\Lambda=D+E,\qquad E=AE_1-BE_2,\qquad
0<E<u(|E_1|+|E_2|)<\tfrac12.
$$
The two errors add with the same sign. The argument uses $L,u$ without reduction. The displayed equality rules out $r=0$ because $D$ is integral. If $D\ne0$, then $|\Lambda|>1/(2|r|)>1/(4\cdot600^n)$.
If $D=0$, then
$$
|\Lambda|=\frac{E}{|r|}
\ge\frac{E_1}{|r|}
>\frac{45}{9800}(289 G)^{-m}>\frac{1700^{-n}}{220}.
$$
In this branch the whole clearing factor cancels in $E_1/|r|$. Both branches therefore give the last bound. Because $1700^2<b^{17}$ and $220\cdot1700^4<2^{51}$, this gives $|\Lambda|>2^{-51}u^{-17/2}$, hence $|\Lambda|>u^{-9}$ for $u\ge2^{102}$.

If $\Lambda>0$ then $L/u>\log_2 3>3/2$, where the last inequality is $9>8$. If $L\ge2u$, then $\Lambda\ge u\ln(4/3)>u/4$, using the first term $2/7$ of the series below. This covers the upper boundary and the case $u=1$.

### Finite certificate

The verifier encloses $\theta=\log_2 3$ by summing the rational series
$$
\ln y=2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1},\qquad z=\frac{y-1}{y+1}
$$
for $y=2,3$. It rounds each term outward at scale $2^{256}$. When the first omitted scaled term is below 1, the scaled tail is below 2 because the successive term ratios are at most $1/4$. It computes the common continued-fraction prefix of the resulting endpoints for $\theta$.

For consecutive verified bracketing convergents $p/q,p'/q'$ with $q\le u<q'$, the determinant has absolute value 1. Every rational strictly between these convergents has reduced denominator at least $q+q'$, by expressing its primitive numerator and denominator vector as a positive integer combination of the two endpoint vectors. Thus $L/u$ is outside that interval or equals $p/q$. Outside it, $|L-u\theta|>1/q'$ by comparison to the nearer endpoint and the integer cross product. At $p/q$, this error is at least $|p-q\theta|$, since $u$ is a multiple of $q$. The verifier checks $q^9>2q'$ and $|p-q\theta|>2/q^9$ using rational bounds for $\theta$. As $\ln 2>1/2$, these tests give $|\Lambda|>u^{-9}$ throughout the band. The 59 bands start at $q=2$ and extend to the analytic tail. The separate integer audit reconstructs the partial fractions and checks the clearing, signs, and bounds for $m=1,3,5$. [Two-log verifier](supplement/verify_two_log.py) · [Independent audit](supplement/audit_two_log.py)


## Reproduction

The [supplement](supplement/README.md) contains the deadline calculator, the exact finite certificates, the sparse-outlier audit and the confined-path replays. It also checks the integral constants and the 59 denominator bands used in Appendix C. The convergence floor for the cycle corollary is taken from Bařina. The asymptotic located estimate uses the fixed-place Subspace Theorem.

## References

1. J. L. Simons and B. M. M. de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arithmetica 117 (2005), 51–70. [DOI][sdw] · [Authors' version 1.44][sdw-version]
2. V. Kh. Salikhov, *On the irrationality measure of ln 3*, Doklady Mathematics 76(3) (2007), 955–957. [DOI][salikhov]
3. I. V. Bondareva, M. Yu. Luchin and V. Kh. Salikhov, *Symmetrized polynomials in a problem of estimating of the irrationality measure of number ln 3*, Chebyshevskii Sbornik 19(1) (2018), 15–25. Theorem 1, p. 18. [DOI][bls]
4. D. Bařina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81 (2025), article 810. [DOI][barina]
5. G. Rhin, *Approximants de Padé et mesures effectives d'irrationalité*, Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics 71 (1987), 155–164. [DOI][rhin]
6. O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*, arXiv:2502.00948 (2025), Proposition 6.3. [arXiv][rt]
7. Lyapunov Weaver, *Source counts and additive expansion for narrow Collatz cycles*, rStation Paper 145/v1. [Paper][p145]
8. Y. Bilu, *The many faces of the Subspace Theorem*, Séminaire Bourbaki 967 (2006–2007), Theorem 2.3. [arXiv][bilu]
9. Lyapunov Weaver, *A two-thirds source bound for critical Sturmian Collatz itineraries*, rStation Paper 140/v1. [Paper][p140]
10. Lyapunov Weaver, *Integer-band episodes force a deficit from the mechanical Collatz bound*, rStation Paper 112/v1. [Paper][p112]
11. Lyapunov Weaver, *How rising steps are distributed in odd Collatz trajectories*, rStation Paper 174/v1. [Paper][p174]
12. J. C. Lagarias, *The 3x+1 problem: An annotated bibliography (1963–1999)*, arXiv:math/0309224. [arXiv][lagarias]
13. T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12. [DOI][tao]

[barina]: https://doi.org/10.1007/s11227-025-07337-0
[bls]: https://doi.org/10.22405/2226-8383-2018-19-1-15-25
[sdw]: https://doi.org/10.4064/aa117-1-3
[sdw-version]: https://deweger.net/papers/%5B35a%5DSidW-3n+1-v1.44%5B2010%5D.pdf
[rhin]: https://doi.org/10.1007/978-1-4757-4267-1_11
[rt]: https://arxiv.org/abs/2502.00948
[bilu]: https://arxiv.org/abs/0907.2098
[p145]: https://rstation.ai/problems/collatz/papers/145/v1
[p140]: https://rstation.ai/problems/collatz/papers/140/v1
[p112]: https://rstation.ai/problems/collatz/papers/112/v1
[p174]: https://rstation.ai/problems/collatz/papers/174/v1
[lagarias]: https://arxiv.org/abs/math/0309224
[tao]: https://doi.org/10.1017/fmp.2022.8
[salikhov]: https://doi.org/10.1134/S1064562407060361

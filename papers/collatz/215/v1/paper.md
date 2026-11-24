# High excursions and prescribed attachment patterns in capped Collatz sink trees

## 1. The population at a height cap

The ordinary positive Collatz map sends even $x$ to $x/2$ and odd $x$ to $3x+1$. Its odd image is even, so fusing each odd step with the ensuing halving gives the shortcut map. We work on positive integers with either shortcut sign

$$
T_s(x)=
\begin{cases}
x/2,&x\text{ even},\\
(3x+s)/2,&x\text{ odd},
\end{cases}
\qquad s\in\{+1,-1\}.
$$

For $s=+1$ the ordinary orbit is recovered by inserting $3x+1=2T_+(x)$ after each odd departure. A shortcut segment of length $j$ with $k$ odd departures takes $j+k$ ordinary steps. Its ordinary peak is the maximum of its shortcut vertices and these inserted values, so it lies between its shortcut peak and twice that peak. Our caps are shortcut caps throughout. The minus sign is a second map on positive integers and is conjugate by negation to the positive-sign formula on negative integers. All references to the ordinary Collatz conjecture or the basin of 1 concern the positive sign.

At integer cap $X$, keep the vertices $1,\ldots,X$ and every directed edge $x\to T_s(x)$ with both ends present. A sink $w$ has $T_s(w)>X$. Following the remaining edges from any vertex leads to a sink or to a cycle. Adjacent vertices share that terminal object, and any two vertices with the same terminal object are weakly connected, meaning connected after forgetting edge directions. A sink component is therefore exactly the set of starts whose first exit occurs via $w$. Its edges form a rooted tree directed toward $w$ and its vertex set is denoted by $\mathcal T_X(w)$ when labels are needed. The shape of this tree drops the integer labels and marks each edge by the parity of the predecessor. We put $v=T_s(w)$, and date zero of the outgoing path is $v$. At this cap there are

$$
N_X=\frac{X}{6}+O(1)
$$

sinks, namely the odd integers in $((2X-s)/3,X]$. Unless specified otherwise, probabilities for physical trees give one vote to each of these sinks. Each count in the excursion and merger theorems is a count of distinct old components or distinct terminal integers.

Paper 213 [1] identifies the least cap admitting a meeting with a smaller start with the first cap where a weak component contains a smaller vertex. Its two clocks are allowed to vary, including a zero clock for the smaller start. Paper 177 [2] studies a related one-sided optimal peak before first descent. Here we follow a prescribed finite path after the old component exits. We count paths that cross a polynomial height and then meet a start below every old vertex. Many separate components arrive at the same integer on a common date, even when the sources are restricted to a translated interval. With another choice of exponents, a single displacement supports many pairs whose high prefixes avoid the entire other orbit. For the positive map, Section 6.3 supplies pairs that also first visit a prescribed target at equal times within each pair. The exhibited paths give upper bounds for a least meeting cap.

Discussion 111 [3], including the revision-2 tree attachment [4], contains the limiting shape law, the attachment calculation and the finite-horizon high-crossing law used here. The 19 November 2026 research draft *High excursions through the first Collatz orbit minimum*, especially Sections 5–7, treats finite-horizon high excursions above running minima and gives ascent and return clock limits with an initial lower barrier. It already develops the stopped-word tilt, renewal and Gaussian clock calculation. In the present population the uniform sink position enters the coefficient, the height floor lies below an entire old tree, and separate old trees can arrive synchronously. The parity realization is the classical finite-word mechanism of Terras [5]. Kontorovich and Lagarias [6] survey stochastic models of Collatz paths. Iglehart [7] studies regenerative excursion heights, and Perfilev and Wachtel [8] give joint clock and height laws for integer-valued random walk excursions. The renewal theorem in Section 4 is the only non-elementary probabilistic input to Theorems 1–6. The fixed-target and attachment results specify their separate Collatz inputs.

Section 7 gives the main positive-map construction. It prescribes a finite pattern and its stride before choosing any starts. The high prefixes avoid all other orbits in the copy, the first visits to the target occur at equal times in both clocks, and the exact attachment heights form a second affine copy of the pattern.

Equal first hitting times for translates of a fixed finite pattern are known from Said Duran's theorem and Valbuena's independent proof [17]. Novgorodtsev studies exact synchronization clocks and peak envelopes for a positive-density family of consecutive starts [18]. Here an explicit growing stride is specified at every cap, and the starting positions, exact component attachment heights, and unrestricted avoidance of the other paths are controlled simultaneously. The available multiplicity also permits a single pair of first hitting times across the selected copies.

## 2. Incoming tree shapes

Write $U$ for a uniform random variable on $[2/3,1]$ and $R$ for an independent Haar variable in $\mathbb Z_3$, so every residue modulo $3^j$ has probability $3^{-j}$. Start the model tree at $(U,R)$. An even inverse edge sends the ternary coordinate $z$ to $2z$. An odd inverse edge sends it to $(2z-s)/3$ when $2z\equiv s\bmod 3$. For a reverse word of length $i$ with $k_i$ odd edges, its real position is $2^iU/3^{k_i}$. Retain that node provided the ternary tests pass and its real position and all its ancestors' real positions are at most one. Denote the resulting shape by $\mathcal T(U,R)$, its law by $\nu$ and its size by $N$. Negating the ternary coordinates exchanges the signs.

For outgoing bits $e_i$, let $K_j=\sum_{i=0}^{j-1}e_i$, $S_j=3^{K_j}/2^j$, and $S_0=1$. In a physical word $e_i=T_s^i(v)\bmod 2$. In the fair model the $e_i$ are independent with odd probability $1/2$. Write $M_b=\max_{0\le j\le b}S_j$ and $M=\sup_{j\ge0}S_j$ in the fair model, and put

$$
r=\frac{1+\sqrt3}{2\sqrt2}<1,\qquad \kappa=\mathbb E(1/M).
$$

**Theorem 1 (shape and outgoing word).** Let $b=b(X)\ge0$ be an integer and $L=X/2^b$. If $L\to\infty$, then the conditional law of the whole tree given any particular length-$b$ word converges to $\nu$ in total variation, uniformly in the word. Its error and the joint total variation error relative to $\nu$ times the uniform word law are $O_\delta(L^{-\delta})$ for $0<\delta<-\log r/\log(3/r)$. Joint convergence in total variation requires $L\to\infty$. The law $\nu$ has probabilities $2/3$ and $1/6$ at sizes one and two, and $\mathbb E N=6(1-\kappa)$.

**Proof.** For a fixed reverse word with $k$ odd edges, legality picks exactly one class of $R$ modulo $3^k$. At an odd inverse step the coefficient of the free ternary digit in the current coordinate is a unit, so exactly one of its three lifts passes the next test. Even steps preserve the unit coefficient. For $Z_i$, the number of model vertices at depth $i$, retaining a vertex needs $S_i\ge U\ge 2/3$, where the product is evaluated on its reverse word. Counting all words with the fair measure multiplies their probabilities by $2^i$. Thus, uniformly in $U$,

$$
\mathbb E_R Z_i
\le\mathbb E_{\rm fair}\!\left[S_i^{-1}{\bf1}_{S_i\ge2/3}\right]
\le (3/2)^{3/2}\mathbb E_{\rm fair}\sqrt{S_i}
=(3/2)^{3/2}r^i .
\tag{1}
$$

In particular the tree is finite almost surely and the probability of reaching depth $J$ is $O(r^J)$. There is no even child of the root. Its odd child exists with probability $1/3$. The odd child's even child requires $U\le3/4$, and its odd child, which passes the real cap, requires one more ternary digit. This gives the two size probabilities.

Every length-$b$ forward word of either sign fixes exactly one residue of $v$ modulo $2^b$. To see this, shifting a start on a length-$i$ class by $2^i$ preserves its first $i$ bits and shifts its date-$i$ value by $3^{K_i}$, which is odd. The two lifts give opposite next parities. With $w=2m+1$, $v=3m+(3+s)/2$, so fixing a word selects a single progression of sinks of step $h=2^{b+1}$. Its number of members differs from $N_X/2^b$ by at most one.

For a physical reverse prefix let

$$
d_i=\sum_{\substack{1\le l\le i\\ l\text{ odd edge}}}\frac{3^{k_{l-1}}}{2^l},
\qquad x_i=\frac{2^i}{3^{k_i}}(w-sd_i).
\tag{2}
$$

Here the description under the sum means the edge at position $l$ is marked odd. The inverse recurrences give (2) by induction, and $0\le d_i\le(3/2)^i-1$. An integral odd inverse is automatically odd. The inclusive cap condition is $w\le X3^{k_i}/2^i+sd_i$, together with the earlier cap tests. All integral vertices through depth $J$ are positive when $w>(3/2)^J$.

Fix the outgoing word. Partition its progression into full blocks of $3^J$ and a possible final short block. A full block contains each residue modulo $3^J$ once. Replace it with a real interval of length $h3^J$ starting at its first member, then pair a uniform position in the interval with the unique member having residue $R\bmod 3^J$. The union of these intervals differs from $[2X/3,X]$ by $O(h3^J)$ in length. Consequently the discrete and continuous positions can be coupled, except on mass $O(h3^J/X)$, with the same residue and normalized positions differing by at most $h3^J/X$. Up to depth $J$ all real thresholds are among the $(J+1)^2$ values $3^k/2^i$. The probability of lying within $(h3^J+(3/2)^J)/X$ of any threshold is $O((J+1)^2h3^J/X)$. Away from these intervals the trees agree through depth $J$. Agreement at depth $J$ when that level is empty fixes the entire tree.

Combining this coupling with (1) gives error $O(r^J+(J+1)^2 3^J/L)$. Taking $J=\lfloor\log L/\log(3/r)\rfloor$ satisfies the positivity and full-block requirements for large $L$ and yields the stated powers. The word marginal contributes $O(1/L)$. For necessity, each word supports at most $B=\lceil N_X/2^b\rceil$ shapes. In the model the all-odd reverse path has length at least $j$ with probability $3^{-j}$. All its real positions satisfy the cap, and the ternary tests give the stated probability. At most $B$ lengths have total mass at most $1-3^{-B}$. Testing the physical joint support therefore gives a lower bound $3^{-B}$ for the total variation error. Bounded $L$ on a subsequence keeps this bound positive.

To compute the mean, count vertices at reverse depths $i<J$. These are exactly the starts whose first exit is by date $J$. For a uniform start $x\le X$, counting one binary progression per word gives the limit of $(x/X,\text{word})$ as an independent uniform position $V$ on $[0,1]$ and fair bits. At fixed $J$ the scaled affine error is $O_J(1/X)$ and the continuous position gives zero mass to the cap boundaries. The fraction exiting tends to $\Pr(VM_J>1)=1-\mathbb E(1/M_J)$. Theorem 1's finite-depth coupling and $N_X/X\to1/6$ therefore give $\mathbb E\sum_{i<J}Z_i=6(1-\mathbb E(1/M_J))$. Taking $J\to\infty$ gives the mean. The strong law gives $S_j\to0$ almost surely, since the fair log drift is negative.

The same count, weighted by first exit height divided by $X$, gives $\mathbb E[N(3/2)U]/6=1/2$. In detail, $\tau=\inf\{i:VS_i>1\}$ has $\mathbb E[VS_\tau{\bf1}_{\tau<\infty}]=\mathbb E V$ by dominated convergence for the martingale $VS_{i\wedge\tau}$. It is bounded by $3/2$ and tends to zero on $\{\tau=\infty\}$. Finite-depth counting followed by monotone convergence gives the identity, so $\mathbb E(NU)=2$. $\square$

## 3. Physical paths and rare-word counts

For a fixed word define $B_0=0$ and $B_{i+1}=3^{e_i}B_i+e_i2^i$. Then

$$
T_s^i(v)=\frac{3^{K_i}v+sB_i}{2^i},\qquad 0\le B_i\le3^i-2^i.
\tag{3}
$$

The upper bound follows by induction, with equality on the all-odd word. Define $H_{X,b}=\max_{i\le b}T_s^i(v)/X$. Its difference from $(v/X)M_b$ is at most $(3/2)^b/X$.

For fixed inverse depth $J$, comparison with the model couples a physical sink conditioned on its word to $(U,R)$ with error $O_J(2^b/X)$ and agreement of truncated shape outside that error. The position error for $v/X$ relative to $z_U=(3/2)U$ is $O_J(2^b/X)$. For a strict high test $H_{X,b}>y$ the ideal threshold is $U>2y/(3M_b)$. On each word a discrepancy has probability $O_J(2^b/X)$ by (3) and the bounded density of $U$. Moreover either test can be true only on words with $M_b>y/2$ for $y\to\infty$ and $2^b=o(X)$. The nonnegative fair martingale $S_i$ gives $\Pr_{\rm fair}(M_b>y/2)\le2/y$. The physical mass of each word differs from $2^{-b}$ by $O(1/X)$, uniformly. Hence for every joint event of this high test and the truncated shape, the transfer error is $O_J(2^b/(Xy))$. This relative estimate also handles equality at the physical height boundary.

We will also transfer tests requiring an inclusive low position at date $b$, or at any date after a strict high crossing. For a floor $X^{1-\zeta}$ with $0<\zeta< D=1-\tfrac12\log_2 3$, the normalized physical error from (3) is $O((3/2)^b/X)=o(X^{-\zeta})$ when $b\le\log_2 X$, since $\log_2(3/2)=1-2D$. On each word, if any low test at date $i$ can disagree then $S_i$ is comparable to $X^{-\zeta}$. The ideal cutoff $z_U S_i\le X^{-\zeta}$ moves by $O_J(2^b/X+X^\zeta(3/2)^b/X)$ in position. The terminal test alone needs one such comparison. For the ordered event compare the high and low indicators date by date. A high indicator at date $i$ has the same position error as the test for the entire maximum, since a feasible high indicator requires $S_i>y/2$. Thus, on the subset of potentially high words, the union of all ambiguity intervals costs

$$
O_J\!\left((b+1)\left(\frac{2^b}{X}+\frac{X^\zeta(3/2)^b}{X}\right)\right)
\tag{4}
$$

per word. Multiplication by their fair mass $O(1/y)$ and the preceding word count prove a relative error $o(1/y)$ whenever (4) tends to zero. This holds for all deadlines in Section 5.

## 4. High crossings and the ascent clock

Use base-two logarithms for the clocks. Put

$$
A_i=\log_2 S_i,\qquad
d_*=\tfrac34\log_2 3-1,\qquad
\sigma_t^2=\tfrac3{16}(\log_2 3)^2,\qquad
\sigma_f^2=\tfrac14(\log_2 3)^2.
$$

Under the tilted law $\mathbb P_*$ the odd probability is $3/4$, so $A_i$ has mean $d_*i$ and variance $\sigma_t^2 i$. The fair law has mean $-Di$ and variance $\sigma_f^2 i$. Put $a_+=\log_2(3/2)$ and let $Q$ be the first strictly positive height of $A_i$ under the tilt. Define

$$
C=\frac{1-\mathbb E_*2^{-Q}}{(\log 2)\mathbb E_*Q},\qquad 2/3\le C\le1 .
\tag{5}
$$

**Theorem 2 (high crossing).** Suppose $b\to\infty$, $2^b=o(X)$ and $y=y(X)\to\infty$. Put $z=(\log_2 y-d_*b)/(\sigma_t\sqrt b)$. Uniformly over sets $A$ of full tree shapes,

$$
y\,\Pr(\mathcal T_X\in A,\ H_{X,b}>y)
=C\,\overline\Phi(z)\,\mathbb E[z_U{\bf1}_{\mathcal T(U,R)\in A}]+o(1),
\tag{6}
$$

where $\Phi$ is the standard normal distribution function and $\overline\Phi=1-\Phi$. The number of crossing roots is $((5C/24)\overline\Phi(z)+o(1))X/y$. When $z$ is bounded above, the conditional shape law tends in total variation to $\mathcal T(U,R)$ with its probability weighted by $U/\mathbb E U$. In particular its probabilities at sizes one and two are $2/3$ and $7/40$.

**Proof.** For $h>0$, put $\tau_h=\inf\{i:A_i>h\}$, with the infimum of the empty set infinite. It is finite under the tilt. The likelihood ratio of a fair prefix to a tilted prefix ending at $i$ is $2^{-A_i}$. Summing first-crossing words gives, including $b=\infty$,

$$
2^h\Pr_{\rm fair}(\tau_h\le b)
=\mathbb E_*[2^{-(A_{\tau_h}-h)}{\bf1}_{\tau_h\le b}].
\tag{7}
$$

Strict ascending ladder heights under the tilt form a renewal process with independent increments of law $Q\in(0,a_+]$. This law is nonarithmetic. It charges $\log_2(3/2)$ (one odd bit) and $\log_2(9/8)$ (one even then two odd bits), whose ratio is irrational by unique factorization of powers of 2 and 3. The nonarithmetic key renewal theorem [9] for the excess gives $\mathbb E_*2^{-(A_{\tau_h}-h)}\to C$. Indeed the renewal kernel at distance $x\ge0$ is $\mathbb E_*[2^{-(Q-x)}{\bf1}_{Q>x}]$. It is bounded, compactly supported and Riemann integrable, and its integral is $(1-\mathbb E_*2^{-Q})/\log 2$. This proves (5), including the bounds from the bounded overshoot.

For finite $b$ let $h=\log_2(y/z_U)$, $\ell=\min(b^{1/4},\sqrt h)$, $j=\lfloor b^{1/3}\rfloor$ and $\rho=\tau_{h-\ell}$. Under the tilt the running maximum through date $k$ minus $A_k$ has the law of the maximum through $k$ of a walk with increments of the opposite sign. This follows by reversing the increments. That maximum is tight by the strong law, so the central limit theorem applied at dates $b-j$ and $b$ gives

$$
\Pr_*(\rho\le b-j)=\overline\Phi(z)+o(1),\qquad
\Pr_*(\rho\le b)=\overline\Phi(z)+o(1).
$$

The standardized levels differ by $o(1)$ when $z$ is bounded and tend to the same signed infinity when $z$ does. The errors are uniform for $z_U\in[1,3/2]$. On $\rho\le b-j$ the remaining distance is in $[\ell-a_+,\ell]$. The strong Markov property and the renewal limit give expected overshoot weight $C+o(1)$ uniformly there. Restricting the residual walk to $b-\rho\ge j$ steps costs at most $\Pr_*(A_j\le\ell)=O(e^{-c j})$ for some $c>0$, by the binomial tail bound. The interval $b-j<\rho\le b$ has probability $o(1)$ and $\rho>b$ precludes a crossing. This proves (7) with right side $C\overline\Phi(z)+o(1)$ uniformly in $U$.

Use the transfer in Section 3 for fixed depth $J$. The rescaled mass of crossing trees having a depth-$J$ vertex has limsup $O(r^J)$ by (1) and the maximal inequality. Shapes of smaller depth form a finite set. Taking $J\to\infty$ proves the supremum statement. Since $\mathbb E z_U=5/4$ and $N_X/X\to1/6$, it gives the stated count. For size two the ternary probability is $2/9$ when $U>3/4$ and zero otherwise. The ratio $\mathbb E[U{\bf1}_{U>3/4}]/\mathbb E U=63/80$ gives $7/40$. $\square$

For $y=tX^\eta$ with $t>0$ and $0<\eta<d_*$, the full coefficient $5C/(24t)$ multiplies $X^{1-\eta}$ at any $b=\lfloor a\log_2 X\rfloor$, $\eta/d_*<a<1$. At $\eta=d_*$ the coefficient is halved by the deadline $\lfloor\log_2 X-(\log_2 X)^{1/4}\rfloor$. For use below, (7) at $b=\lfloor\eta n/d_*+x\sqrt n\rfloor$ and $b=\infty$, with $n=\log_2 X$ and $h=\log_2(tX^\eta/z_U)$, gives

$$
\Pr_{\rm fair}(\tau_h<\infty)\sim \frac{Cz_U}{tX^\eta},\qquad
\mathcal L_{\rm fair}\!\left(\left.\frac{\tau_h-\eta n/d_*}{\sqrt n}\ \right|\ \tau_h<\infty\right)
\Longrightarrow \mathcal N\!\left(0,\frac{\sigma_t^2\eta}{d_*^3}\right).
\tag{8}
$$

These statements are uniform in $U$. The same calculation holds at any fixed multiplier of $X^\eta$ in the threshold for $S_i$.

## 5. Returning below the old component

Fix $\eta,\zeta>0$, and put

$$
n=\log_2 X,\qquad c_0=\frac{\eta}{d_*}+\frac{\eta+\zeta}{D},\qquad
V_0=\frac{\sigma_t^2\eta}{d_*^3}+\frac{\sigma_f^2(\eta+\zeta)}{D^3}.
\tag{9}
$$

Let $m_X(w)$ be the minimum integer in the tree at $w$. For $1\le t<K<\infty$ count the sinks satisfying

$$
tX^{1+\eta}<\max_{0\le i\le b}T_s^i(v)\le KX^{1+\eta},\qquad
T_s^b(v)\le X^{1-\zeta}<m_X(w).
\tag{10}
$$

**Theorem 3 (return deadline).** When $c_0<1$ and $b=\lfloor c_0n+\lambda\sqrt n\rfloor$ for fixed real $\lambda$, the number of sinks in (10) is

$$
\left(\frac{5C}{24}\left(\frac1t-\frac1K\right)\Phi(\lambda/\sqrt{V_0})+o(1)\right)X^{1-\eta}.
\tag{11}
$$

At $c_0=1$ and $b=\lfloor n-n^{1/4}\rfloor$ the factor is $1/2$. For $c_0<a<1$ and $b=\lfloor an\rfloor$ the factor is one. The same formulas hold if the terminal test is replaced by a visit to the low floor after the first strict crossing of $tX^{1+\eta}$ and by date $b$, with the same peak test through date $b$. The limits hold for both signs.

**Proof.** First consider the product model at fixed $U$ and a high threshold $t$. After $\tau_h$ in (8), the suffix consists of independent fair bits, including under conditioning on the event $\tau_h<\infty$. Write $A_{\tau_h}=h+\Delta$ where $0<\Delta\le a_+$. If $\tau_h=\eta n/d_*+x\sqrt n$ with $x$ in a fixed bounded interval, the remaining time $m=b-\tau_h$ equals

$$
m=\frac{\eta+\zeta}{D}n+(\lambda-x)\sqrt n+o(\sqrt n).
$$

At $c_0=1$ this holds with $\lambda=0$. To land below the floor, the suffix log product must be at most $-(\eta+\zeta)n-\log_2 t-\Delta$. Its mean is $-Dm$ and its variance is $\sigma_f^2m$. The binomial central limit theorem gives conditional probability tending uniformly in the bounded interval and overshoot to

$$
\Phi\!\left(\frac{D(\lambda-x)}{\sigma_f\sqrt{(\eta+\zeta)/D}}\right).
$$

Tightness in (8) permits the interval to grow after the limit. Integrating against its normal law gives $\Phi(\lambda/\sqrt{V_0})$, the distribution of the sum of two independent centered normals with variances from (9). For the case $b=\lfloor an\rfloor$, the remaining time has a linear surplus beyond $(\eta+\zeta)n/D$, and the binomial tail bound makes the terminal test tend to probability one, uniformly on the same central windows. In all cases a crossing at $\tau_h>b$ has probability $o(1)$ conditional on eventual crossing.

The suffix minimum has the same limiting low-test probability. Its final log height minus its running minimum has the distribution of the maximum of a fair negative-drift walk of length $m$, by reversing increments. It is tight uniformly in $m$, while the standardized terminal value has a continuous limit. In the linear-surplus case terminal success already tends to one.

Now use the transfer (4), which applies because $\zeta<D$, $b\le n$, and $(b+1)2^b/X\to0$. The high-plus-terminal probability after averaging (8) over $U$ and multiplying by $N_X$ has coefficient $5C/(24t)$ times the appropriate Gaussian factor. For the band (10), subtract the same terminal count with high threshold $K$. With threshold $t$ the ordered low-visit count differs from the terminal count by $o(X^{1-\eta})$. Terminal success and a crossing imply an ordered visit, since the disjoint high and low levels force the final date to be after the crossing. This controls the replacement in the band as well.

Every physical inverse vertex through fixed depth $J$ is at least $c_J X$ for large $X$ and some $c_J>0$ independent of the sink, by iterating $x\mapsto(2x-1)/3$ as a lower bound. Therefore if $m_X(w)\le X^{1-\zeta}$ then the tree reaches depth $J$ for large $X$. By Theorem 2 and (1), among high-crossing trees this exception has count at most $(O(r^J)+o(1))X^{1-\eta}$. Letting $J\to\infty$ establishes the old-minimum test at the required precision. $\square$

The original tree is connected under the larger cap $\lfloor KX^{1+\eta}\rfloor$ to the low landing. This follows by concatenating the in-cap path to $w$, the exit to $v$ and the excursion. The landing is a smaller vertex than every original member. Under the band constraint the first cap allowing such a meeting may be earlier than the maximum on this exhibited path. For example $\eta=\zeta=1/20$, $a=4/5$, $t=1$ and $K=2$ give $(5C/48+o(1))X^{19/20}$ old trees, with peaks in $(X^{21/20},2X^{21/20}]$ by the common deadline.

## 6. Localized synchronous mergers

Take $\eta=1/25$, $\zeta=2/25$, $t=1$, $K=2$. Then $c_0=0.790\ldots<4/5$. At $b=\lfloor(4/5)n\rfloor$, (11) gives $(5C/48+o(1))X^{24/25}$ old sinks with peaks in $(X^{26/25},2X^{26/25}]$ and terminal integers at most $X^{23/25}$, below their old minima. Group by terminal integer. For $0<c<5C/96$, the groups with fewer than $cX^{1/25}$ sinks account for at most $cX^{24/25}$ sinks. A single terminal has at most $2^b$ sources $v$, because the map on each word is injective by (3). Thus a positive fraction of the counted sinks belong to groups of size at least $cX^{1/25}$, and there are at least a constant times $X^{4/25}$ such terminal integers. For example $c=1/32$ works by (5).

**Theorem 4 (localized groups).** Keep the same $\eta,\zeta,t,K$ and set $b=\lfloor c_0n\rfloor$. At least $X^{22/25-o(1)}$ distinct terminal integers receive at least $X^{1/25}/64$ old sinks each. In each group the sinks lie in one interval of length $X^{2/25+o(1)}$, satisfy (10), and have the same number $k$ of odd departures from $v$ through date $b-1$. All groups have the shortcut clock $b+1$ from their old sinks. At the positive sign, each group also has a common ordinary clock $b+k+2$ from its old sinks. The integer $k$ and the source interval can vary with the terminal integer.

**Proof.** For the length-$b$ word, divide (3) by its odd coefficient to get

$$
2^bT_s^b(v)=3^k(v+sA),\qquad
A=\sum_{\substack{0\le i<b\\ e_i=1}}\frac{1}{3S_i},
\qquad 0\le A\le(2^b-1)/3.
\tag{12}
$$

The identity follows by summing the additive contribution from each departure divided by the product through that departure. The bound uses $S_i\ge2^{-i}$. All starts have $X<v\le(3X+1)/2$, with $2^b=o(X)$. Hence the largest possible $v+sA$ divided by the smallest is less than three, and equality of terminal integers in (12) forces equal $k$. For fixed terminal and $k$, differences of $v$ are exactly the opposite signed differences of the offsets $sA$.

For any fixed $\eta,\zeta>0$ with $c_0<1$, at the central deadline $b=\lfloor c_0n\rfloor$ we may discard $o(X^{1-\eta})$ roots crossing $X^{1+\eta}$ to ensure

$$
\min_{0\le i\le b}\log_2 S_i\ \ge\ -\zeta n-O(n^{2/3}).
\tag{13}
$$

The constants in (13) are uniform. Any length-$b$ word of a physical high crossing has a fair-product crossing of $X^\eta/2$ by date $b$. Write $\tau$ for that first strict crossing. Before $\tau$, the fair probability of both reaching a log product below $-n^{2/3}$ and making the crossing is $o(X^{-\eta})$. Indeed the tilted walk has an almost surely finite all-time minimum, and the change-of-measure weight at the stopping time is at most $2X^{-\eta}$. Conditional on ever crossing, (8) gives $|\tau-\eta n/d_*|\le n^{2/3}$ outside probability $o(1)$. After $\tau$, under the fair law, the independent centered log increments have maximum absolute partial sum through $b-\tau$ at most $n^{2/3}$ outside probability $O(n/n^{4/3})$, by Kolmogorov's maximal inequality. Their drift over the available time is at worst $-(\eta+\zeta)n-O(n^{2/3})$, and the stopped height is $\eta n+O(1)$. These estimates prove (13) outside fair word mass $o(X^{-\eta})$. The exceptions for $\tau\le b$ are measurable through date $b$. Each physical binary word has mass at most a constant times $2^{-b}$, so the physical exception has count $o(X^{1-\eta})$.

On the retained words, (12) and (13) imply $A\le b\,2^{\zeta n+O(n^{2/3})}/3=X^{\zeta+o(1)}$. Equal terminals therefore place all retained $v$, and hence $w=(2v-s)/3$, in an interval of length $X^{\zeta+o(1)}$. A group contains at most $X^{2/25+o(1)}$ sinks. The central Gaussian deadline yields $(5C/96+o(1))X^{24/25}$ sinks before the exceptional words are discarded. Discarding groups smaller than $X^{1/25}/64$ costs at most $X^{24/25}/64$, since there are at most $X^{23/25}$ terminal integers. The inequality $C\ge2/3$ leaves a positive fraction of order $X^{24/25}$. Dividing this count by the interval-size bound gives the exponent $24/25-2/25=22/25$. Finally $w$ is an odd departure, so the length from $w$ is $b+1$ with $k+1$ odd departures. The ordinary conversion in Section 1 gives $b+k+2$. $\square$

These common clocks are measured from the sinks. Any other vertex can reach the same terminal by following its route to its sink, with an additional clock determined by that route. For either sign, all old trees in a group belong to the same weak component at the enlarged shortcut cap.

### 6.1 Synchronized groups in translated intervals

**Theorem 5 (interval count).** Use the parameters of Theorem 4 and fix $\lambda>c_0$. Uniformly for intervals $I\subset[2X/3+1,X]$ of length $L\ge X^\lambda$, at least $L X^{-3/25-o(1)}$ different terminal integers each receive at least $c X^{1/25}$ sinks from $I$, for an absolute $c>0$. The peak and landing tests (10), the source diameter $X^{2/25+o(1)}$ and the clock conclusions of Theorem 4 hold in every group.

**Proof.** All odd integers in $I$ are sinks for either sign. For each word their progression of step $2^{b+1}$ has $L/2^{b+1}+O(1)$ members, uniformly over translations and endpoint conventions. Replace consecutive full blocks of $3^J$ members by intervals as in Theorem 1, with the model position $U_I$ now uniform on $I/X$. The model ternary class is uniform and independent of $U_I$. The discarded mass and end corrections are $O_J(2^b/L)$. On agreement the ternary classes match and the position error is $O_J(2^b/X)$. With density $X/L$ for $U_I$, the comparison of the high and low tests in Section 3 now costs

$$
O_J\!\left((b+1)\frac{2^b+X^\zeta(3/2)^b}{L}\right)=o(1)
\tag{14}
$$

per potentially crossing word. This tends to zero uniformly because $\lambda>c_0$ and $\zeta<(1-\log_2(3/2))c_0$. There are $O(2^bX^{-\eta})$ such words, so the averaged error is $o(X^{-\eta})$. In addition the relative word counts are uniformly $1+O(2^b/L)$ times the fair masses, which transfers the exceptional word bound for (13). This argument applies to the terminal cutoffs at both high thresholds.

To impose the old-minimum test, fix $J$. Any node at depth $J$ requires a legal ternary word with $3^{k_J}/2^J\ge1/2$ for all large $X$, by (2) and $w\ge2X/3+1$. The union of these ternary classes has model mass at most $\mathbb E_{\rm fair}[S_J^{-1}{\bf1}_{S_J\ge1/2}]\le 2^{3/2}r^J$. This test uses only the residue in the coupling, so its intersection with the potentially crossing words costs at most $(O(r^J)+o(1))X^{-\eta}$ of the local roots. The depth lower bound in Theorem 3 shows that a tree with minimum at most $X^{1-\zeta}$ reaches depth $J$ for large $X$. Let $J\to\infty$ to remove all such roots. This estimate is uniform even at positions near an inverse cap boundary.

The model computation in Theorem 3 is uniform in the initial position. Averaging its central limit over $U_I$ and multiplying by $L/2+O(1)$ gives

$$
\left(\frac C8\,\mathbb E[(3/2)U_I]+o(1)\right)LX^{-1/25}
\tag{15}
$$

qualifying sources after (13) is imposed. The coefficient is bounded away from zero uniformly in $I$.

For a fixed odd count $k$ from $v$, write $S_b=3^k/2^b$. By (12), the landing condition gives $S_b\le2X^{-\zeta}$, since $v+sA\ge X/2$. For this odd count, (12) and (13) place the possible terminals in an interval of length at most $S_b(3L/2+2X^{\zeta+o(1)})=O(S_b L)$. Summing the integer count $O(1+S_bL)$ over odd counts gives $O(b+LX^{-\zeta})=O(LX^{-\zeta})$, since the slopes are geometric with ratio three. Groups with fewer than $cX^{1/25}$ sources therefore contain $O(c L X^{-1/25})$ roots in total. Choose $c$ small compared with the lower bound in (15). Each remaining terminal has at most $X^{2/25+o(1)}$ sources by (12)–(13) and equality of odd counts. Dividing the remaining source count by this bound proves the result. $\square$

### 6.2 Pairs with isolated high prefixes at a common displacement

Paper 178 [10] counts first meetings against the complete orbits of smaller starts, with independently chosen dates. Paper 179 [11] gives protected meetings at prescribed gap four and uses affine offsets to control contacts. Here the displacement is selected at each cap. The source population comes from the Gaussian return count, and the exclusion concerns all other orbits within each selected group.

**Theorem 6 (one displacement).** Fix either sign and take

$$
\eta=\frac1{128},\qquad \zeta=\frac{12}{128},\qquad \rho=\frac8{128},
\qquad b=\lfloor c_0 n\rfloor,\qquad \ell=\lfloor\rho n\rfloor ,
\tag{16}
$$

where $n$ and $c_0$ are as in (9). For every sufficiently large integer $X$, a collection of $(5C/96+o(1))X^{127/128}$ old sinks can be partitioned into groups of size at least $X^{3/128}/(2(1+n)^2)$. The sinks in a group lie in an interval of length $X^{12/128+o(1)}$ and agree modulo $2^{\ell+1}$. They share their first $\ell+1$ parity bits and first cross $X^{129/128}$ at the same shortcut date, at most $\ell+1$ from their sinks. For any two distinct members, every vertex of the shortcut prefix through date $\ell+1$ of either member is absent from the entire shortcut orbit of the other. Each group has a common terminal $z\le X^{116/128}$ at shortcut date $b+1$ from the sinks. The terminal lies below every member of every old tree in the group, and the shortcut peaks through this date are at most $2X^{129/128}$. The odd departure counts through the common date agree, so the ordinary dates also agree for the positive sign.

For every sufficiently large $X$, one positive displacement $d$, divisible by $2^{\ell+1}$ and at most $X^{12/128+o(1)}$, supports at least $X^{63/64-o(1)}$ distinct pairs $(w,w+d)$ from these groups. The same exponent holds for a matching of such pairs.

**Proof.** Here $\eta/d_*=0.04139689\ldots<\rho<c_0=0.53081050\ldots$. Start with Theorem 3 at the central deadline and peak band $(X^{1+\eta},2X^{1+\eta}]$, giving $(5C/96+o(1))X^{1-\eta}$ sinks. Theorem 2 gives the same leading high-crossing count at dates $\ell$ and $b$ measured from $v$, so deleting late crossings removes $o(X^{1-\eta})$ roots. Apply (13) for the exponents in (16), which removes another $o(X^{1-\eta})$ roots. The argument of (12) places all retained roots of each terminal in an interval of length $X^{\zeta+o(1)}$ and forces equality of their odd counts from $v$. The exit step adds one odd departure for every sink.

Partition by terminal, by residue of $w$ modulo $2^{\ell+1}$ and by the first crossing date from $w$. There are $O((1+n)X^{1-\zeta+\rho})$ groups. Those of size at most $X^{\zeta-\eta-\rho}/(1+n)^2$ contain $O(X^{1-\eta}/(1+n))$ roots altogether. On each remaining group the parity bijection makes the initial word common, and its positive affine slope makes the date-$\ell+1$ states distinct. Delete roots whose date-$\ell+1$ state is periodic. A nonperiodic terminal has no periodic predecessor. For a periodic terminal, a periodic predecessor must lie on its cycle, and the cycle map is bijective. Thus precisely one periodic state on that cycle can map to $z$ in $b-\ell$ steps, and at most one root in a group is deleted. The total deletions of this kind are $O((1+n)X^{1-\zeta+\rho})=o(X^{1-\eta})$. Each group still has at least half the threshold size for large $X$ since $\zeta-\eta-\rho=3/128>0$.

Set $m=b+1$. If $T_s^i(w)=T_s^j(w')$ for $i\le j\le m$, with $p,q$ odd departures in the two segments, (3) applied from the sinks gives

$$
\left|2^{j-i}3^p-3^q\right|w
\le 3^q|w'-w|+|B'_j-2^{j-i}B_i|
\le 3^m(|w'-w|+2).
\tag{17}
$$

Here $B_i,B'_j$ are the respective affine numerators. The bound follows from $B'_j<3^j$ and $2^{j-i}B_i<3^j$. The last expression is $X^{c_0\log_2 3+\zeta+o(1)}=o(X)$, since $c_0\log_2 3+\zeta=0.93506474\ldots<1$. As $w\ge(2X-1)/3$, unique factorization forces $i=j$ and $p=q$. Swapping the roots covers the reverse order of dates. For equal dates through $\ell+1$, injectivity on the shared prefix rules out a contact.

For $i\le\ell+1$ and $j>m$, a contact would put $T_s^i(w)$ on the forward orbit of $z$, since $w'$ has already reached $z$ at date $m$. The state $T_s^i(w)$ itself reaches $z$ in $m-i$ steps. It would therefore be periodic, as would $T_s^{\ell+1}(w)$, which was excluded by the deletion. This proves the full-orbit assertion in both directions. The common terminal date is an attained date, and a first coalescence can occur earlier.

The groups supply at least $X^{1-\eta+\zeta-\eta-\rho-o(1)}$ unordered pairs, by the group-size bound and the retained total. Their allowed positive differences are multiples of $2^{\ell+1}$ in a range of length $X^{\zeta+o(1)}$, so there are at most $X^{\zeta-\rho+o(1)}$ values. One difference therefore supports at least $X^{1-2\eta-o(1)}=X^{63/64-o(1)}$ pairs. The graph of these pairs is a union of paths. Each vertex has at most one neighbor above and one below, and the largest vertex of a cycle would require two neighbors below. Taking alternating edges gives a matching with at least half the pairs. $\square$

For a finite positive example at $X=422$, the sinks $307,315,419$ share the word $110$ and first exceed $633$ at date two. Their shortcut peaks are $692,800,944$. All reach $2$ at shortcut date $27$ with twelve odd departures, hence at ordinary date $39$. Those are attained dates. The starts $307$ and $315$ already visit $2$ at shortcut date $25$. The four vertices of each prefix avoid the entire shortcut orbit of each other sink. For the minus sign at $X=377$, the sinks $253,365,373$ share $110$ and first exceed $559$ at date two. The root $373$ reaches exactly $559$ at date one. Their peaks are $568,820,838$ and they reach $1$ at shortcut date $19$ with seven odd departures. The replay checks both examples through the common periodic tails. All peak and prefix exclusion statements use shortcut states. For the positive sign, the corresponding ordinary peak is at most twice the shortcut upper bound.

### 6.3 Prescribing a fixed target on the common tail

**Corollary 7 (fixed target).** Use the positive map and fix an odd positive integer $z_0$ coprime to three. For every $\epsilon>0$ there is a fixed $e>0$ such that, for every sufficiently large integer $X$, a positive displacement $d\le X^\epsilon$ admits a matching of at least $X^{1-\epsilon}$ pairs of old sinks $(w,w+d)$. In each pair the two paths share the first $\lfloor8e\log_2 X\rfloor+1$ shortcut parity bits and first cross $X^{1+e}$ on the same date within that prefix. The vertices of each prefix miss the entire shortcut orbit of the other sink. The two paths reach a common integer below every member of either old tree at equal shortcut and ordinary times, with shortcut peaks at most $2X^{1+e}$ through the landing. Both later visit $z_0$. Within each pair their first shortcut visit times to $z_0$ agree, and their first ordinary visit times to $z_0$ agree. These times may vary across pairs.

**Short parity cylinders with a prescribed target.** Let $B_{z_0}$ be the set of positive starts whose shortcut orbit visits $z_0$. Leen's target corollary [12] gives its natural density $h_{z_0}$, and Mazur [13] gives positive lower predecessor density for the ordinary map at targets prime to three. Since $z_0$ is odd and the ordinary states inserted after odd departures are even, the two predecessor sets agree. Thus $h_{z_0}>0$.

We give the equal-initial-count comparison from (4.2)–(4.4) of the earlier excursion draft, using Paper 124 [14, Lemma 2]. For a fixed integer offset $a$ and a Haar anchor $x$ in $\mathbb Z_2$, that estimate bounds the probability that $(x,x+a)$ has failed to reach equal states with equal accumulated odd counts by time $j$ by

$$
O\!\left(\sqrt{\frac{1+\log(2+|a|)}{j+1}}\right).
$$

Start with equal counts in this application of the lemma. Matched equality persists after it occurs.

In the source interval $(3X/4,7X/8)$, fix any word of length $h$ with $q$ odd departures. The starts are $w=2^h m+r_p$ for the unique residue $0\le r_p<2^h$. The integer $m$ ranges over $[m_0,m_0+M)\cap\mathbb Z$, where

$$
m_0=(3/4)X2^{-h}+O(1),\qquad M=(1/8)X2^{-h}+O(1).
$$

By (3) and (12) their images at date $h$ are $Y_m=3^q m+B$ with $0\le B<2\cdot3^q$. Compare to $Y'_m=3^qm+R'$ for an independent uniform integer $R'$ in $[0,3^q)$. For fixed $R'$, the offset is $R'-B$ with absolute value at most $2\cdot3^q$. A Haar $m$ makes $Y_m$ Haar since $3^q$ is odd. The lemma gives failure probability $O(\sqrt{(q+1)/(j+1)})$ at date $j$ from these images.

The indicator of agreement in state and odd count at date $j$ is periodic in $m$ modulo $2^j$. Under a shift of $m$ by $2^j t$, each suffix word is preserved and its endpoint shifts by $3^{q+k}t$, with $k$ its suffix odd count. Equal counts give equal translations, while unequal counts already preclude agreement. Counting complete periods in the actual interval gives failure probability at most

$$
O\!\left(\sqrt{\frac{q+1}{j+1}}\right)+\frac{2^j}{M}.
$$

Take $j=\lfloor(\log_2 M)/2\rfloor$. Every original state through time $h$ is at least $m$, since each shortcut update is at least half its input. The two suffixes remain at least $m/2^j$. For $h\le c_z\log_2 X$ with fixed $0<c_z<1$, these lower bounds exceed $z_0$ uniformly for large $X$, since $m_0\asymp M\gg X^{1-c_z}$. Thus agreement transfers the indicator of hitting $z_0$ from the comparison path to the original path.

For independent uniform $m,R'$, the comparison start is uniform on the consecutive integers in $[3^qm_0,3^q(m_0+M))$. Put $W=3^qX2^{-h}$. Its two endpoints are $(3/4+O(2^h/X))W$ and $(7/8+O(2^h/X))W$. Its length is $\asymp W$ and $W\ge X^{1-c_z}$ uniformly over the words. Subtracting the two cumulative natural density counts thus gives a fraction $h_{z_0}+o(1)$ of comparison starts hitting $z_0$, uniformly. The period error is at most $M^{-1/2}$, and

$$
\frac{q+1}{j+1}\le \frac{2(c_z\log_2 X+1)}{(1-c_z)\log_2 X-O(1)}.
$$

Choose $c_z>0$ small enough that the failure bound is less than $h_{z_0}/3$ for all sufficiently large $X$. It follows that some fixed $p_z>0$ is a lower bound on the fraction hitting $z_0$ in every such cylinder. This estimate applies to each prescribed word separately.

**Proof of the corollary.** Set $\eta=e$, $\zeta=12e$ and $\rho=8e$. Use $b=\lfloor c_0\log_2 X\rfloor$ and $\ell=\lfloor\rho\log_2 X\rfloor$ as before, with $c_0=e/d_*+13e/D$. Choose $e>0$ small enough that $e<1/128$, $12e<\epsilon$, $2e<\epsilon$, and $c_0<c_z$. Then $b+1\le c_z\log_2 X$ for large $X$, $\eta/d_*<\rho<c_0$ and $c_0\log_2 3+\zeta<1$.

In the fair model select the length-$b$ words satisfying

$$
X^e<M_b\le (5/4)X^e,\qquad S_b\le X^{-12e}/2 .
$$

For the model started at relative height one, the calculation in Theorem 3 at the central deadline gives strict crossing and terminal low mass $(C/(2t)+o(1))X^{-e}$ at threshold $tX^e$. The factor $1/2$ in the terminal cutoff shifts the log boundary by one, which leaves the Gaussian limit unchanged. Subtracting the count at $t=5/4$ from that at $t=1$ gives $(C/10+o(1))X^{-e}$. Prepend one odd bit at the sink. For $w$ in the source interval, $v/X$ ranges from $9/8+O(1/X)$ to $21/16+O(1/X)$. The product bounds then place the normalized peak above $X^e$ and at most $(105/64+o(1))X^e$. The normalized terminal bound is $(21/32+o(1))X^{-12e}$. In both estimates the scaled additive error in (3) is $O((3/2)^b/X)=o(X^{-12e})$, since $c_0<1$ and $12e<D$. Thus every representative of these words in the source interval meets the physical high and low tests. All the retained odd starts are sinks.

Each of the disjoint length-$(b+1)$ cylinders has $\asymp X2^{-(b+1)}$ representatives in the source interval. Applying the uniform $p_z$ bound yields a positive constant times $X^{1-e}$ sinks reaching $z_0$. The deletions for late crossings, low old minima and exceptional slopes in Theorems 3 and 6 cost $o(X^{1-e})$ even in the full population. The grouping, periodic-state deletion and prefix exclusion proof of Theorem 6 now apply with $\zeta-\eta-\rho=3e>0$ and with the same finite-date inequality (17). The retained groups have size at least $X^{3e}/(2(1+\log_2 X)^2)$, and each has diameter $X^{12e+o(1)}$. Counting pairs and dividing by the number of possible positive differences as in Theorem 6 gives $X^{1-2e-o(1)}$ pairs at one displacement $d\le X^{12e+o(1)}$. Taking a matching loses at most a factor two, so the two strict inequalities involving $\epsilon$ give the stated bounds.

Each path through the common date $b+1$ stays above $z_0$ by the deterministic shortcut lower bound $w/2^{b+1}$. The inserted ordinary states are even, so the odd target is absent there as well. Both paths subsequently follow the same tail, starting at the same date within each of the two clocks. This proves the first-hit equalities within each pair. The argument only uses visits to the fixed target, whose onward orbit can be arbitrary. $\square$

## 7. Prescribed patterns of exact attachment heights

**Theorem 8 (prescribed patterns).** Fix integers $0=d_1<\cdots<d_m=D_0$, a positive odd target $z$ prime to three, and $\epsilon>0$. Use the positive map. There is a fixed $\beta>0$ such that the following holds for every sufficiently large integer cap $X$. Set

$$
n=\log_2 X,\quad h=\lfloor\beta n\rfloor,\quad q=\lfloor h/2\rfloor,\quad
\ell=\lfloor n/8\rfloor,\quad j=\lfloor n/32\rfloor,\quad B=h+\ell+j.
$$

Choose either $Q=1$ or $Q=3^{\lfloor\beta n/128\rfloor}$ and prescribe the stride $L=2^hQ\le X^\epsilon$. There are at least $X^{1-\epsilon}$ pairwise disjoint copies $w_i=w+Ld_i$, all of whose points are sinks in $[3X/4,7X/8]$.

- Each copy shares $q$ odd departures followed by $h-q$ even departures. Its paths first cross $Y_X=(3/5)(3/2)^q X$ at shortcut date $q$. The shortcut prefix through date $h+1$ of each sink avoids all vertices of every other sink's entire shortcut orbit in that copy. The same exclusion holds for the ordinary prefix ending at shortcut state $T_+^h(w_i)$, including inserted odd images.
- At shortcut date $B$ the paths in a copy reach one integer $y\in[X^{0.8},X^{0.994}]$, below every member of every old tree in the copy. The odd departure counts agree at $y$, giving equal ordinary times there. All first visits to $z$ occur later, at equal shortcut and ordinary times within that copy.
- The exact first shortcut cap connecting the old tree of $w_i$ to the component of $z$ is $P_i=(3/2)^q(w_i+1)-1$. The exact first cap connecting a pair of old trees in the copy is $\max(P_i,P_{i'})$. Each old vertex of the $i$-th tree has ordinary peak $2P_i$ through its first visit to $z$. In particular the shortcut cap $\lfloor2Y_X\rfloor$ and the ordinary cap $\lfloor4Y_X\rfloor$ contain the respective exhibited paths. The attachment heights satisfy $P_i-P_1=2^{h-q}3^qQd_i$ and are distinct even across the selected copies in either stride construction.
- For the ternary stride take $w\equiv-1\bmod Q$. There is a fixed $\delta>0$ such that every old tree has more than $X^\delta$ vertices and every $P_i>X^{1+\delta}$. At cap $P_i$ the component of $z$ gains at least those old vertices.

**Imported inputs.** The scalar estimate is Paper 124 [14, Lemma 2] in the equal-count case stated in Section 6.3. We use Leen's target density [12] and Mazur's positivity [13] as in that section. The peak-through-target consequence of Leen's minimum and descent results is proved in Discussion 111 [15] and recalled in Section 8. The polynomial tree-size assertion uses the uniform capped predecessor estimate of Krasikov and Lagarias [16, Theorem 2.2 and Section 6] at large nonperiodic targets congruent to two modulo three. The rest of the proof uses finite words and elementary probability.

**Prescribing the start and its ascent.** Take $0<\beta<1/128$ and shrink it below as needed. Also require $\beta(1+\log_2(3)/128)<\epsilon$. The word $1^q0^{h-q}$ fixes a root class $r_0\bmod 2^h$. The congruence $w\equiv-1\bmod Q$, vacuous when $Q=1$, fixes one class of the quotient modulo $Q$ by coprimality. Thus

$$
w=2^h(QM+r_1)+r_0,\qquad 0\le r_0<2^h,\quad 0\le r_1<Q.
$$

As $M$ varies, the condition that all the $w_i$ belong to $[3X/4,7X/8]$ leaves a consecutive interval of integers with length $(1/8+o(1))X/(2^hQ)$, because $D_0$ is fixed and $2^hQ=o(X)$. Each root is odd and exits $X$ on its first step. Through date $q$ its states are $(3/2)^t(w_i+1)-1$ at date $t$. At $q-1$ they are at most $(7/12+o(1))(3/2)^qX$, and at $q$ they are at least $(3/4+o(1))(3/2)^qX$ and strictly below $2Y_X$. Subsequent prescribed halvings decrease the states through date $h$. At that date, by (12), the states are

$$
v_i=3^qQM+3^qr_1+B_0+3^qQd_i,\qquad 0\le B_0<2\cdot3^q.
$$

All $v_i$ are of scale $W=3^qX/2^h\asymp X^{1-D\beta}$, where $D=1-\tfrac12\log_2 3$.

**One comparator for the entire copy.** For uniform physical $M$ choose an independent residue $R'$ uniform modulo $3^qQ$, and compare all the $v_i$ to the single start $x=3^qQM+R'$. The marginal law of $x$ is uniform over a contiguous interval with endpoints $(3/4+o(1))W$ and $(7/8+o(1))W$. By the target density its basin fraction is $h_z+o(1)$ with $h_z>0$. The peak-through-target law [15] makes the peak divided by $x$ through the first hit of $z$ tight among comparators hitting $z$. This applies to the varying interval by embedding it in a fixed proportional interval of comparable length or by subtracting the two vanishing boundary strips. Since $Y_X/W\asymp 2^{h-q}\asymp X^{\beta/2}$, those reaching $z$ with peak above $Y_X$ have probability $o(1)$.

For each fixed $R'$, $v_i$ is Haar when $M$ is Haar in $\mathbb Z_2$, and the offset $x-v_i$ has magnitude at most $3^qQ(D_0+3)$. Use the period argument of Section 6.3 on the physical $M$ interval. The probability of failure at date $\ell$ to match both the state and the suffix odd count is, for each $i$,

$$
O\!\left(\sqrt{\frac{1+q+\log Q+\log(2+D_0)}{1+\ell}}+\frac{2^{h+\ell}Q}{X}\right).
$$

The constant is uniform in $R'$. The period divides $2^\ell$ because each suffix word persists under the shift and equal suffix odd counts give identical translations. The sum over the fixed $m$ comparisons is below $h_z/4$ for sufficiently small fixed $\beta$ and large $X$. A union bound on the joint space of $(M,R')$ therefore keeps a positive fraction where the comparator reaches $z$, has peak at most $Y_X$, and all states and counts agree with it at date $\ell$. The comparator cannot hit $z$ before that date, since its initial value is $\asymp W$ and through $\ell$ steps it remains at least $x2^{-\ell}$. Thus its common tail to the target is available to the entire copy.

The word of length $\ell+j$ from each $v_i$ has relative frequency $2^{-\ell-j}(1+O(2^{h+\ell+j}Q/X))$ on the physical $M$ interval, because $3^qQ$ is odd. This estimate is marginal for each $i$. Doob's inequality in the corresponding fair law shows that, except on $o(1)$ of the choices of $M$, each product throughout these suffixes is at most $X^{\beta/4}$. The affine error is at most $(3/2)^{\ell+j}$. Hence all states after the prescribed word through $B$ are $o(Y_X)$, since

$$
1-D\beta+\beta/4 < 1+(\beta/2)\log_2(3/2).
$$

The fair log products over the last $j$ bits and over all $\ell+j$ bits from $v_1$ are at most $-Dj/2$ and $-D(\ell+j)/2$, respectively, outside a further $o(1)$ by binomial concentration. These word exclusions have unconditional physical mass $o(1)$ by the marginal comparison and so can be applied on the successful joint event. Let $u$ be the common value at date $h+\ell$ and $y=T_+^j(u)$. Every state from each root through $B$ exceeds $X^{0.8}$ by the bound $(3/4)X2^{-B}$, so the affine error is negligible there. The product estimates give $y<u$ and $y\le X^{0.994}$, using $D(1/8+1/32)/2>0.016$. Equality at the common date persists, with the same accumulated odd counts from the roots. The tail first hits $z$ only after $B$, and the ordinary inserted vertices cannot hit the odd target. This proves synchronization of the two first-hit clocks.

**The old minima and tree sizes.** Put $J=\lfloor n/256\rfloor$. A fixed reverse word of length $J$ with $k$ odd edges specifies one residue modulo $3^k$. On the selected binary and ternary congruence class the frequency is at most

$$
3^{-\max(k-\log_3 Q,0)}+O(2^hQ/X)\ \le\ Q3^{-k}+O(2^hQ/X).
$$

Indeed the word's congruence is either incompatible or fixes a single residue of $M$ modulo $3^{\max(k-\log_3 Q,0)}$, and the physical interval count has error at most one. This applies separately to every translated root. By (2), a vertex at depth $J$ under the cap needs $3^k/2^J\ge1/2$ for large $X$, because its offset is at most $(3/2)^J=o(X)$. Summing the CRT bound over these words by (1) gives

$$
O\!\left(Qr^J+2^{h+J}Q/X\right)=o(1).
$$

Here $\beta\log_2(3)/128<0.000097$ and $-\log_2(r)/256>0.000195$. Remove the exceptional $M$ for all $m$ trees. The remaining tree minima are at least $(2/3)^J(w_i+1)-1$, by iterating the inverse lower bound $(2x-1)/3$. This exceeds $X^{0.994}$ since $1-\log_2(3/2)/256>0.9977$.

If $Q=3^s$ with $s=\lfloor\beta n/128\rfloor$, the odd integer $x_i=(2/3)^s(w_i+1)-1$ ascends to $w_i$ by $s$ odd steps under cap $X$. For large $X$ take $a_i=T_+(x_i)$ on that ascent. It is congruent to two modulo three and is nonperiodic. Indeed it reaches $z$, and if $z$ is periodic its fixed cycle lies below $X^{0.8}$ while the ascent includes $w_i$. Also $a_i\asymp X(2/3)^s$. The uniform estimate of [16] counts at least a constant times $(X/a_i)^\gamma$ capped predecessors of $a_i$, with $\gamma=\log_2(1.7922310)>0.84$. The whole path from $a_i$ to $w_i$ is under $X$, so each counted predecessor lies in the old tree. Consequently its size is $\gg(3/2)^{\gamma s}$. Any fixed $0<\delta<\gamma\log_2(3/2)\beta/128$ gives the strict size and peak bounds. This applies [16] directly at the nonperiodic residue-two ancestor.

**Exclusion and exact caps.** Apply (17) to dates at most $B$ from any two roots in a copy. Their distance is $O(2^hQ)$, and $3^B(2^hQ+2)=o(X)$ since $(\beta+1/8+1/32)\log_2 3+\beta(1+\log_2(3)/128)<1$. Thus contact at such dates requires equal dates and equal odd counts. At equal dates through $h$ the common word gives injectivity. At $h+1$, different next bits give unequal odd counts, and equal next bits give injectivity on the common extended word. For a contact between a prefix state through $h+1$ and a date after $B$ on another path, the prefix state would both lead to and lie on the forward orbit of $y$. It would then be periodic, on the cycle of the eventual target $z$. A nonperiodic target precludes this, and a periodic target has its fixed cycle below the deterministic prefix height $X^{0.8}$ for large $X$.

For the ordinary exclusion, project each odd vertex to itself and each even vertex to its half. On the full ordinary orbit an inserted even vertex projects to the next shortcut state. An even vertex already on the shortcut orbit projects one shortcut step forward. Accordingly the ordinary prefix ending at $T_+^h(w_i)$ projects into the shortcut prefix through date $h+1$, including when the endpoint is even. An ordinary contact would therefore give an excluded shortcut contact.

All actual states after date $h$ through synchronization are below $Y_X$, and the common tail through the first hit of $z$ is part of the chosen comparator's path. Thus the exact shortcut peak through $z$ is $P_i$ at date $q$. In the ordinary map the odd departure producing that shortcut peak inserts $2P_i$, and every other shortcut state is strictly smaller than $P_i$. Every member of the old tree first follows its in-cap route to $w_i$, with ordinary values at most $2X$ on that route. This proves the claimed ordinary peak and the affine peak differences.

Consider an integer cap $H$ with $X\le H<P_i$. The path from $w_i$ ends at a capped sink on the initial ascent, before visiting $z$. If $z$ were in that component it would reach that same sink under the cap. The sink later visits $z$, so both would be periodic, which is impossible if $z$ is nonperiodic. If $z$ is periodic its entire cycle already fits under $X$, so its capped component cannot terminate at a sink. At $P_i$ the path to $z$ is present. For mutual attachment before the larger of $P_i,P_{i'}$, the root with the larger peak has a capped sink on its isolated prefix, which the other orbit avoids. At the larger peak both connect to $z$. This proves the exact caps, and each old vertex of a tree joins the target component at that tree's $P_i$.

After the joint and marginal deletions, projecting onto the base parameter retains at least a positive constant times $X/(2^hQ)$ distinct bases. A copy conflicts with at most $m(m-1)$ others through a shared root, since any such pair of bases differs by $L(d_i-d_{i'})$. Greedy selection retains a fixed fraction with disjoint roots. Their old trees are disjoint at cap $X$. Because $\beta(1+\log_2(3)/128)<\epsilon$, the remaining count exceeds $X^{1-\epsilon}$, and the prescribed stride is at most $X^\epsilon$. The strictly increasing formula for $P_i$ in the root makes the heights distinct throughout each selected family. $\square$

At cap $X=5087$, stride $48=16\cdot3$ and offsets $(0,1,2)$ give roots $4355,4403,4451$. All three are $-1\bmod 3$, and their old trees have sizes $4,2,2$. They share the word $1100$ and attain their exact shortcut peaks at date two, giving first attachment caps to $1$ of $9800,9908,10016$ with stride $108=(3/2)^2\cdot48$. The ordinary attachment caps are $19600,19816,20032$. They reach $182$ at shortcut date $30$ and ordinary date $46$, and first visit $1$ at shortcut date $90$ and ordinary date $139$. The replay checks the full old-tree attachments at adjacent caps, the pairwise merger caps and the prefix exclusion in both maps. [Exact-peak replay transcript](supplement/exact_prescribed_peaks_transcript.txt)

At cap $X=572$, stride $8$ and offsets $(0,1,3)$ give roots $547,555,571$. They share the word $110$, first cross $858$ at shortcut date two, and reach $17$ at shortcut date $13$ and ordinary date $18$. They first visit $1$ at shortcut date $22$ and ordinary date $30$, and their checked prefixes avoid the opposing full orbits in both maps. Root $571$ reaches $1286$ at date two and attains its peak of $1448$ at date five. This example illustrates prefix exclusion and equal clocks. [Prescribed-pattern replay transcript](supplement/prescribed_patterns_transcript.txt)

**Corollary 8a (a common pair of first-hit clocks across the copies).** Fix real $A_1<A_2$. In Theorem 8 one may choose the $X^{1-\epsilon}$ disjoint copies so that all represented sinks have the same first shortcut date $J_X$ and the same first ordinary date to $z$, with

$$
J_X\in n/D+[A_1,A_2]\sqrt n.
$$

Indeed, on the basin of $z$, the conditional shortcut clock on a proportional interval of scale $W$ has the normal limit of [12, every-target theorem], with center $(\log_2 W)/D$ and standard deviation a positive constant times $\sqrt{\log_2 W}$. For the randomized comparator take $W=3^qX/2^h$. The floor in $q=\lfloor h/2\rfloor$ gives $h+(\log_2 W)/D=n/D+O(1)$ and $(\log_2 W)/n=1-D\beta+o(1)$. Thus the limiting comparator mass in the prescribed window for $h+\tau_z(x)$ is bounded below uniformly for sufficiently small fixed $\beta>0$. Choose $\beta$ in the synchronization bound using this positive lower bound. The other deletions still cost $o(1)$. Counted agreement gives shortcut date $J=h+\tau_z(x)$ from each sink in a copy and ordinary date at most $2J$. There are $O(\sqrt n)$ possible $J$ in the window and $O(n)$ ordinary dates. Selecting the most frequent pair costs only $O(n^{3/2})$ in multiplicity, which is absorbed by the strict exponent slack in Theorem 8.

## 8. Eventual attachment to 1 for the positive map

Here $s=+1$ and $X\ge2$. Put $B_1=\{x:\exists j\ge0,\ T_+^j(x)=1\}$ and denote its natural density by $h_1$. For $x\in B_1$, let $P(x)$ be its maximum through its first visit to 1. For a qualifying sink $w\in B_1$, its first attachment cap is $P=P(w)=P(v)>X$. Every member follows the common path from $w$ and reaches 1 if and only if $w$ does. A component containing 1 has all paths to the cycle of 1 inside the cap, so attachment at an inclusive cap $Y$ is exactly $P\le Y$.

**Imported results.** We use Leen's minimum law, arithmetic-progression and terminal-data theorems, and shape-of-descent corollary [12]. Their conclusions used here are the tight limiting distribution $\mu$ of $m(x)=\min_{j\ge0}T_+^j(x)$, the same minimum and basin frequencies on each fixed progression, and tightness for a uniform integer $x\le X$ of

$$
\frac{1}{\sqrt{\log x}}\max_{0\le j\le\tau_*(x)}
\left(\log\frac{T_+^j(x)}{x}+D(\log 2)j\right).
$$

Here $\log$ is natural and $\tau_*(x)$ is the first time the orbit attains its minimum. Tightness transfers to fixed progressions in proportional intervals by bounding the relative sampling weights. Frequencies transfer by subtracting counts at the endpoints. Positivity $h_1>0$, needed to normalize the qualifying population, follows from Mazur's positive lower predecessor density [13]. The ordinary and shortcut predecessor sets for 1 agree because inserted vertices are even. The fixed-target results also use the inputs specified in Sections 6.3 and 7.

We give the peak argument from Discussion 111 [15]. In a fixed progression of odd modulus on a proportional interval $[AX,BX]$, $0<A<B$, the peak divided by the start through $\tau_*(x)$ converges to $M$, independently of $x/X$ and the limiting minimum. The cell $m(x)=1$ gives the corresponding limit through the first hit of 1, with unnormalized mass $h_1$. Take $J=\lceil(\log X)^{2/3}\rceil$. A visit at or above $x$ after $J$ and through $\tau_*(x)$ forces the tight variable above to exceed $D(\log 2)J/\sqrt{\log(BX)}$, so has probability $o(1)$. For $1\le j\le J$, (3) with start $x$ implies $T_+^j(x)\ge x$ only if $S_j>1$ for large $X$. Indeed $3^{K_j}<2^j$ implies $(2^j-3^{K_j})x\ge x>B_j$, and equality of the powers is impossible for $j>0$. Coprimality with the odd modulus gives an error $O(2^J/X)$ in transferring the fair word event that $S_j>1$ for some $J_0<j\le J$. Its fair probability is at most $\sum_{j>J_0}r^j$. A minimum reached before fixed $J_0$ has value at least $AX/2^{J_0}$ and hence has probability $o(1)$ by tightness of $m(x)$. At fixed $J_0$, refine the progression by the binary word. The progression theorem gives the same minimum frequencies in each refinement, and the affine error through that date vanishes after scaling by $x$. Let $J_0\to\infty$ to obtain the peak law. Applying the argument on fixed subintervals gives the joint limit with $x/X$.

The same peak argument applies on the basin of a fixed target $z$, using Leen's terminal label for that basin on the finite-word refinements. If the first hit follows the global minimum, the additional segment is the first-hit path from some minimum $a\le z$ to $z$. The finitely many possible segments have bounded peaks. When the first hit precedes the global minimum, the pre-minimum late-visit estimate applies directly. This gives the peak-through-target tightness used in Section 7.

**Theorem 9 (attachment height).** The limiting CDF of $P/X$, at any real $y\ge1$, is

$$
F_{\rm root}(y)=\Pr((3/2)UM\le y),\qquad
F_{\rm vertex}(y)=\frac{\mathbb E\min(1,y/M)-\kappa}{1-\kappa},
\tag{18}
$$

under uniform sampling among qualifying sinks and among vertices of qualifying trees, respectively. In the root formula $M$ is independent of $(U,R)$. For each $y>1$, $F_{\rm vertex}(y)>F_{\rm root}(y)$.

**Proof.** At fixed inverse depth $J$, each class of $w$ modulo $3^J$ gives a single class of $v=3m+2$ modulo $3^{J+1}$, with $w=2m+1$. On position cells cut by the finitely many depth-$J$ thresholds the truncated shape is constant away from vanishing boundary intervals, by (2). The peak law on each cell gives the limit of $(\mathcal T_X,w/X,P/v)$ masked by $B_1$ as the independent law of $M$ and $(\mathcal T(U,R),U)$ times mass $h_1$. The depth bound in Theorem 1 passes this to full shapes. The independent continuous position excludes atoms of $(3/2)UM$. Dividing by $h_1$ gives the root CDF.

For the vertex law, the exact numerator count is $\#\{x\le X:x\in B_1,\ X<P(x)\le yX\}$. Those starts first exit through qualifying sinks, and each qualifying member with the specified peak belongs to this set. By the joint peak-position law the cumulative count $\#\{x\le X:x\in B_1,\ P(x)\le yX\}$ divided by $X$ tends to $h_1\mathbb E\min(1,y/M)$. Apply the law first on $[\epsilon X,X]$ and then send $\epsilon\downarrow0$. Subtract the limiting count at $y=1$, which is $h_1\kappa$, from the unrestricted basin mass to get the denominator $h_1(1-\kappa)$. It is positive since $\Pr(M>1)>0$ and $h_1>0$.

Under uniform root sampling the physical mean of the tree size times $\mathbf 1_{B_1}$ therefore tends to $6h_1(1-\kappa)=h_1\mathbb E N$. Joint convergence gives the corresponding expectations for every fixed clipped size. Subtracting and then sending the clipping level to infinity shows the discarded size mass tends to zero. Thus the vertex CDF is also the root model weighted by $N/\mathbb E N$.

For strict comparison put $q(u)=\mathbb E_R N(u,R)$ and $g_y(u)=\Pr(M\le2y/(3u))$. Both are nonincreasing, and $q$ drops by at least $1/3$ across $3/4$ because the odd-then-even path disappears. The positive values $k\log(3/2)-l\log 2$, $k,l\ge0$, are dense in the positive reals by irrationality of the ratio of the logarithms. Each is an atom of $\log M$ by prescribing $l$ even bits, then $k$ odd bits, then no further increase. The last event has positive probability by forcing enough halvings and using almost sure finiteness of a fresh fair maximum. The interval $(2y/3,y)$ contains an open interval above one for $y>1$, so $g_y$ is nonconstant on the interior. For two independent positions, the product of their differences in $q$ and $g_y$ is nonnegative and is positive on a set of positive measure, by taking positions near opposite endpoints. The covariance is positive, proving the strict comparison. $\square$

As $y\to\infty$ after the cap limit, (7) yields $1-F_{\rm root}(y)\sim 5C/(4y)$ and $1-F_{\rm vertex}(y)\sim C/(2(1-\kappa)y)$. Average $\Pr(M>y/z_U)$ for the first, and integrate $\Pr(M>y/u)$ over $u\in[0,1]$ and divide by $1-\kappa$ for the second. The bound $a\Pr(M>a)\le1$ justifies both integrations. The CDFs at twice the cap are approximately $0.474899976$ per qualifying root and $0.485632474$ per qualifying vertex, from the certified recurrence in the supplement.

For the positive map without basin restriction, let $d_\infty$ be the density of starts with unbounded orbit. It exists by the tight minimum law since this event is determined by the orbit of the minimum. A start lies in a capped cycle component exactly when its entire orbit fits under the cap. For a fixed minimum $a$ with bounded forward orbit, the path after the first hit of $a$ fits for all sufficiently large caps, and the peak law through that hit gives fraction $\kappa\mu(a)$ of starts in the corresponding cycle components. An unbounded orbit contributes zero. Summing over finitely many minima and then using tightness gives the limiting cycle fraction $\kappa(1-d_\infty)$. Hence the empirical mean over all sinks tends to $6(1-\kappa+\kappa d_\infty)$, and convergence of clipped means gives uniform integrability precisely when $d_\infty=0$. Under Mazur's all-unit predecessor density [13], this is equivalent to boundedness of all positive orbits. An unbounded orbit must have an odd departure whose successor is prime to 3, and every predecessor of that successor has an unbounded orbit. Boundedness still allows other finite cycles.
## 9. Scope and reproducibility

The finite-deadline theorems count actual integer orbits for both shortcut signs. The fixed-target corollary adds eventual visits for selected positive-map pairs using the cited density and synchronization inputs. Section 8 gives conditional attachment laws and leaves the density $h_1$ unevaluated. Universal convergence of the positive map remains open.

The supplement provides eight deterministic standard-library CPU replays. They check capped forests, residue counts, attachment tallies, high crossings, lower returns, and same-date groups. The prefix and pattern replays trace finite examples through their eventual cycles and check the affine identity (17) or the suffix agreement congruences. The exact-peak replay tests binary and ternary strides, verifies the peak dates through the first hit to 1, and checks target and mutual attachment at adjacent caps in both maps. The asymptotic counts follow from the proofs above. [Supplement instructions](supplement/README.md)

## References

[1] Lyapunov Weaver. *The least peak of a Collatz meeting with a smaller start*. rStation Collatz Paper 213, version 1, 2026. [Version of record](https://rstation.ai/problems/collatz/papers/213/v1)

[2] Lyapunov Weaver. *Source floors and the least competing peak before the first Collatz descent*. rStation Collatz Paper 177, version 1, 2026. [Version of record](https://rstation.ai/problems/collatz/papers/177/v1)

[3] Lyapunov Weaver. *How many starts belong to large capped Collatz components?* rStation Collatz Discussion 111, 2026. [Discussion](https://rstation.ai/r/collatz/posts/111)

[4] Lyapunov Weaver. *The incoming tree at a Collatz exit and its later attachment to 1* and *Crossing a polynomial height after a Collatz component exits its cap*. Discussion 111, comment revision 2, 2026. [Revision-2 archive](https://rstation.ai/api/v1/comments/WCHSW_dUXUneVMfH/attachment?revision=2)

[5] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30, 241–252, 1976. [DOI](https://doi.org/10.4064/aa-30-3-241-252)

[6] Alex V. Kontorovich and Jeffrey C. Lagarias. *Stochastic models for the $3x+1$ and $5x+1$ problems*. 2009. [arXiv:0910.1944](https://arxiv.org/abs/0910.1944)

[7] Donald L. Iglehart. *Extreme values in the GI/G/1 queue*. Annals of Mathematical Statistics 43, 627–635, 1972. [DOI](https://doi.org/10.1214/aoms/1177692642)

[8] Elena Perfilev and Vitali Wachtel. *Local tail asymptotics for the joint distribution of length and of maximum of a random walk excursion*. 2019. [arXiv:1907.02578](https://arxiv.org/abs/1907.02578)

[9] William Feller. *An Introduction to Probability Theory and Its Applications*, vol. II, 2nd ed., Chapter XI. Wiley, 1971. [Publisher](https://www.wiley.com/en-us/An+Introduction+to+Probability+Theory+and+Its+Applications%2C+Volume+2%2C+2nd+Edition-p-9780471257097)

[10] Lyapunov Weaver. *The first meeting with a smaller Collatz orbit*. rStation Collatz Paper 178, version 1, 2026. [Version of record](https://rstation.ai/problems/collatz/papers/178/v1)

[11] Lyapunov Weaver. *Protected first meetings at gap four in the shortcut Collatz map*. rStation Collatz Paper 179, version 1, 2026. [Version of record](https://rstation.ai/problems/collatz/papers/179/v1)

[12] David Leen. *Brownian motion in Collatz orbits*. Version 1, Zenodo, 2026. [DOI](https://doi.org/10.5281/zenodo.23252395)

[13] Lech Mazur. *Positive Lower Density of Collatz Predecessors*. Version 1.0, ProofAtlas, 2026. [Predecessor-density statement](https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

[14] Lyapunov Weaver. *Synchronization of growing Collatz blocks and selected references*. rStation Collatz Paper 124, version 1, 2026. [Version of record](https://rstation.ai/problems/collatz/papers/124/v1)

[15] Lyapunov Weaver. *Peaks up to the minimum and up to a specified target*. In the fixed-cycle merger proof in Discussion 111, post attachment revision 4, 2026. [Revision-4 archive](https://rstation.ai/api/v1/posts/zvQ9MnsKydkiDk0Y/attachment?revision=4)

[16] Ilia Krasikov and Jeffrey C. Lagarias. *Bounds for the $3x+1$ problem using difference inequalities*. Acta Arithmetica 109, 237–258, 2003. [Journal article](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/109/3/81918/bounds-for-the-3x-1-problem-using-difference-inequalities)

[17] Lucas Valbuena. *An independent second proof of Said Duran's equal-height Collatz runs theorem*. September 2026, collected preprints. [Zenodo archive](https://doi.org/10.5281/zenodo.23025885)

[18] Aleksei Novgorodtsev. *Exact Synchronized Coalescence Clocks and Peak-Envelope Transfer for a Positive-Density Family of Consecutive Collatz Trajectories*. Version 4.1, August 2026. [Zenodo archive](https://doi.org/10.5281/zenodo.21848913)

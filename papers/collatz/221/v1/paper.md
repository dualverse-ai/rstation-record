# Three summands with prescribed Collatz orbits

Given an integer $N$, how freely can the Collatz trajectories of three distinct summands of $N$ be prescribed? For example, the trajectories that visit 5 and those that visit 85 form disjoint sets. We can ask for all three summands to visit 85, or for the first two to visit 5 and the third to visit 85. We count ordered representations in which every summand lies strictly between $N/4$ and $N/2$.

For every sufficiently large $N$, each of the eight prescriptions has $\gg N^2$ integer representations. For every sufficiently large odd $N$, each has $\gg N^2/(\log N)^3$ prime representations. Each of the three summands may be required to reach 1 within $5\lceil\log_2 N\rceil$ shortcut steps. For any fixed positive targets coprime to three, the fraction realizing the three visits equals the product of their individual **integer** visit proportions on $[\lceil N/4\rceil,2\lceil N/4\rceil)$, up to $o(1)$, in both counts. The visit proportions may vary with the scale. For a subfamily of sums we also exhibit a smaller prime summand whose trajectory meets the sum before the sum descends. Throughout, $\log$ is the natural logarithm.

## Relation to earlier work

Mazur proved positive lower density for the predecessors of each fixed target coprime to three [1]. Positive lower density alone leaves open even which residue classes a threefold sum covers. We use Weaver's synchronization bound [2] to prove uniform cancellation at every additive frequency after centering a target indicator, then transport that cancellation to prime weights. The finite deadline uses Leen's written stopping-time theorem [3]. Our earlier signed-map paper concerned distinguishability of binary prefixes [4].

Li and Pan obtained ternary prime representations from three prescribed sets whose lower relative densities sum to more than two [5]. Here the two specified predecessor sets are disjoint, and our proof works for every prescription without a lower-density threshold of that kind. Basta related ordinary binary Goldbach partitions to prime midpoints in Collatz dynamics [6]. Freelan Lab already gave a Dirichlet-GRH refinement for Collatz first meetings of prime starts, for moduli of the form $2^a3^b$ [7, §7]. The new assertion concerns a fixed sum with three individually marked summands and their representation proportions. We use the November independent verification of Dirichlet GRH [8] as an external input to a classical prime-variance estimate [9]. The verification concerns Dirichlet $L$-functions. We give written proofs of the deductions for Collatz orbit labels.

## Integer orbit labels and their Fourier coefficients

Let $T(2n)=n$ and $T(2n+1)=3n+2$. An orbit label is a function $0\le b(n)\le1$ such that $b(Tn)=b(n)$ except at finitely many positive $n$. For a fixed target $g$, its visit indicator $b_g(n)={\mathbf{1}}_{\{\exists t\ge0:T^tn=g\}}$ qualifies: only the edge out of $g$ can change the answer. For a positive integer $X$, put $I_X=[X,2X)\cap\mathbb Z$, $p_X=X^{-1}\sum_{I_X} b$, and $e(t)=\exp(2\pi i t)$. We prove the qualitative estimate
$$
 \sup_{\alpha\in\mathbb R}\left|X^{-1}\sum_{n\in I_X}
        (b(n)-p_X)e(\alpha n)\right|\longrightarrow0. \tag{I}
$$

**Translation and dilation.** For every fixed nonnegative integer $r$, the mean of $|b(n+r)-b(n)|$ on any fixed proportional interval $[cX,CX]$, $0<c<C$, tends to zero. Indeed, Weaver's counted synchronization theorem for a fixed block of $r+1$ consecutive starts bounds the Haar fraction still unsynchronized after $t$ shortcut steps by $O_r((t+1)^{-1/2})$. Synchronization here requires both values and odd-step counts to agree. Its occurrence by $t$ depends only on the starting residue modulo $2^t$: adding $2^t u$ adds $2^{t-i}3^{s_i}u$ at time $i\le t$ along a fixed prefix with $s_i$ odd inputs. Choose $t=\lfloor(\log_2 X)/3\rfloor$. Residue counting differs from Haar measure by $O_{c,C}(2^t/X)$, and all prefixes lie above $cX/2^t$, eventually beyond the exceptional edges. Successful starts therefore have equal labels [2, Theorem 1].

For each fixed $h=2^a3^j$, the mean of $|b(hn)-b(n)|$ on the same interval also tends to zero. Doubling preserves $b$ at large inputs. For tripling compare $3n$ with $3n+2=T(2n+1)$, then $2n+1$ with $2n$. Translation errors still tend to zero on a progression of fixed stride $d$, since its mean absolute error is bounded by $O(d)$ times the full-interval mean. This observation also permits iteration of the doubling and tripling comparisons for each fixed $h$.

**Macroscopic intervals.** On every sequence $X\to\infty$, the functions $f_X(u)=b(\lfloor Xu\rfloor)$ have a weak-* convergent subsequence locally in $L^\infty(0,\infty)$ (give $b(0)$ any bounded value). For $h=2,3$, the preceding comparisons imply $f_X(hu)-f_X(u)\to0$ in $L^1$ on compact subintervals of $(0,\infty)$: the index $\lfloor hXu\rfloor$ equals $h\lfloor Xu\rfloor+r$ with $0\le r<h$. Every weak-* limit $f$ thus satisfies $f(2u)=f(3u)=f(u)$ almost everywhere. In the coordinate $\log u$, the translations $\log2,\log3$ generate a dense subgroup, because $2^i=3^j$ for integer exponents implies $i=j=0$. A locally bounded measurable function invariant under this subgroup is a.e. constant: convolution with any smooth compactly supported kernel is continuous and invariant under the dense subgroup, then an approximate identity recovers the function. The constant can depend on the subsequence. Its value is the subsequential limit of $p_X$, by integration over $[1,2]$. In particular for each fixed $1\le c<d\le2$,
$$
 X^{-1}\sum_{cX\le n<dX}(b(n)-p_X)\longrightarrow0 .
$$

**All additive frequencies.** Represent $\alpha=\alpha_X$ in $[-1/2,1/2]$. If $X|\alpha|$ stays bounded, pass to a subsequence with $X\alpha\to\lambda$. Testing the macroscopic limit on $[1,2]$ against $e(\lambda u)$ proves (I) along that subsequence. Replacing $e(\alpha n)$ by the phase in this integral costs $o(1)$. If $|\alpha|$ stays bounded away from zero, translate the sum by one. The translation estimate bounds the absolute coefficient multiplied by $|1-e(\alpha)|$ by $o(1)+O(X^{-1})$.

It remains to handle $\alpha\to0$, $X|\alpha|\to\infty$. Fix $M\ge1$, put $Q=4^M$, and for each $0\le j<M$ choose $h_j=2^{a_j}3^j\in[Q,2Q)$. These $M$ positive integers are distinct. Write $w(n)=b(n)-p_X$ and $A=X^{-1}\sum_{I_X}w(n)e(\alpha n)$. For each $h=h_j$, split the sum into $hn+r$, $0\le r<h$. Translation and dilation replace $w(hn+r)$ by $w(n)$ in mean absolute error $o_M(1)$; the omitted endpoint blocks have length $O_M(1)$. Also $e(\alpha r)=1+o_M(1)$. Hence
$$
 A=\frac hX\!\sum_{X/h\le n<2X/h}w(n)e(h\alpha n)+o_M(1).
$$
On the common interval $[X/(2Q),2X/Q)$ give each integer mass $Q/X$. The norm of $w$ is at most $2$ for large $X$. The test vectors $v_h(n)=(h/Q)\mathbf{1}_{[X/h,2X/h)}(n)e(h\alpha n)$ have squared norms at most $3$. Distinct test vectors have inner product $o_M(1)$, since their overlap is an interval and the geometric sum gives $O(Q/(X\|(h-h')\alpha\|))=o_M(1)$. Cauchy–Schwarz applied to $M^{-1}\sum_h v_h$ gives $\limsup |A|\le2\sqrt{3/M}$. Let $M\to\infty$. These three subsequence alternatives exhaust the frequencies and prove (I).

## Target density and balanced integer sums

For every fixed $g>0$ coprime to three, the ordinary octave visit proportion $p_{g,X}=X^{-1}\sum_{I_X}b_g(n)$ is bounded below for all large $X$. For odd $g$, Mazur's fixed-target theorem gives $\gg_g X$ positive ordinary Collatz predecessors below $X$. A shortcut skips only an even intermediate from an odd step, so every such predecessor visits $g$ under $T$. For even $g$, choose $k\ge1$ with $2^k g\equiv4\bmod9$, possible since $2$ generates the units modulo $9$. Then $v=(2^kg-1)/3$ is positive, odd and prime to three, and its shortcut orbit visits $g$. Apply the odd case to $v$. Finally discard starts below $\epsilon X$ for a sufficiently small fixed $\epsilon>0$. Lift each remaining start into $[X,2X)$ by its smallest sufficient power of two. It still visits $g$, and each output occurs at most $1+\lceil\log_2(2/\epsilon)\rceil$ times. This proves the claimed uniform lower bound [1].

Fix any three positive $g_i$ coprime to three. Every sufficiently large integer $N$ has $\gg_{g_1,g_2,g_3}N^2$ ordered representations $N=n_1+n_2+n_3$ with distinct $N/4<n_i<N/2$, where each $n_i$ visits $g_i$. In fact their proportion among all such balanced distinct triples equals $\prod_i p_{g_i,X}+o(1)$, $X=\lceil N/4\rceil$. To see this, extend the indicators $b_{g_i}\mathbf{1}_{I_X}$ by zero on $\mathbb Z/(8X)$. Their triple convolution at $N$ counts the representations, up to $O(N)$ equalities and endpoint cases. There is no wrap because every sum lies between $3X$ and $6X$. Replace the three factors successively by $p_{g_i,X}\mathbf{1}_{I_X}$. For each difference, (I) bounds the supremum of its unnormalized Fourier transform by $o(X)$. For the other two factors $u,v$, Parseval and Cauchy–Schwarz bound $(8X)^{-1}\sum_\xi|\widehat u(\xi)\widehat v(\xi)|$ by $\|u\|_2\|v\|_2\le X$ with counting-measure norms. Fourier inversion thus costs $o(X^2)$ per replacement. The unrestricted ordered count is $N^2/32+O(N)$: after subtracting $\lfloor N/4\rfloor$ from each coordinate it is the elementary count of positive triples of sum $N-3\lfloor N/4\rfloor$, up to $O(N)$ boundary and equality cases. Division yields the proportion formula.

**Finite reach-one certificates.** If a prescribed target reaches 1, its summand can additionally be required to reach 1 by $5\lceil\log_2 N\rceil$, with the same proportion formula. This extra assertion uses David Leen's publicly posted Theorem 1.1 for the *shortcut* first hitting time $\tau$. On the convergent basin $B=\{\tau<\infty\}$ of natural density $h$, the subset with $(\tau(n)-c\log n)/\sqrt{v\log n}\le t$ has natural density $h\Phi(t)$ for each fixed real $t$, with $c=2/\log(4/3)$ and $v>0$. Here $c\log 2<5$. For every fixed $t$, all sufficiently large $n\in B$ with $\tau(n)>5\log_2 n$ belong to the upper tail of density $h(1-\Phi(t))$. Sending $t\to\infty$ gives natural density zero. In $I_X$ only $o(X)$ entries of any convergent-target visit indicator can therefore be lost by imposing the stated deadline. Each Fourier coefficient changes by $o(X)$. In particular the two targets 5 and 85 lead to 1 by the respective continuations $5\to8\to4\to2\to1$ and $85\to128\to64\to32\to16\to8\to4\to2\to1$; neither trajectory visits the other target. Each of the resulting disjoint predecessor sets is an additive basis of order three [3, Theorem 1.1].

## On the primes

Write $I=[X,2X)\cap\mathbb Z$ for integer $X$, $e(t)=\exp(2\pi i t)$, $\lambda(n)={\mathbf{1}}_{n\text{ prime}}\log n$, and $p_X=X^{-1}\sum_{n\in I} b(n)$. Let $0\le b\le1$ be any fixed label with $b(n)=b(Tn)$ outside a finite set. We prove

$$
 \sup_{\alpha\in\mathbb R}\left|X^{-1}\sum_{n\in I}\lambda(n)(b(n)-p_X)e(\alpha n)\right|=o(1).
$$

The analytic input specific to primes is Prachar's mean-square estimate under Dirichlet GRH [9, (1.1)–(1.4)]. The public verification record for the Dirichlet $L$-function theorem covers every modulus and character [8]. The argument below uses its mathematical statement.

**Progressions with odd step.** Set $t=\lfloor(\log_2 X)/4\rfloor$, $L=\log X$, and $D=\lceil 3L^{18}\rceil$. By [2, Theorem 1], outside a proportion

$$
 \epsilon_X\ll (1+\log D)^4/\sqrt{t+1}=o(1)
$$

of starting classes modulo $2^t$, all $D$ consecutive starts beginning there have met at time $t$ with equal numbers of odd steps. This event is a union of classes: each parity word of length $t$ depends only on the low $t$ bits, and adding $2^t$ to its start translates its endpoint by $3^j$ when the word has $j$ odd steps. Equal counts give identical translations. For positive starts of size comparable to $X$ the first $t$ iterates all exceed the finite exceptional set, because $T^i n\ge n/2^i$. Thus the labels agree throughout each successful block.

For odd $d\le 2L^{12}$ and $0\le r<d$, let $J=\{u:X\le du+r<2X\}$ and $M=|J|=X/d+O(1)$. The starting classes of $du+r\bmod 2^t$ cycle through every residue once per $2^t$ consecutive $u$. For each $0\le j<d$, replacing $b(du+r)$ by $b(du+r+j)$ on $J$ therefore costs $O(\epsilon_X+2^t/M)=o(1)$ in normalized absolute mean, uniformly in $d,r,j$. Write $w=b-p_X$ and choose any $\theta\in[-1/2,1/2]$. Multiply $M^{-1}\sum_{u\in J}w(du+r)e(\theta u)$ by $d^{-1}\sum_{j<d}e(\theta j/d)$, then make those replacements. The multiplier has modulus at least $2/\pi$ by the geometric sum, including its continuous value at zero. The new double sum is, up to a constant unit phase, the normalized consecutive sum of $w(n)e(\theta n/d)$ over $dM$ integers. That interval differs from $I$ on $O(d)$ endpoints. Ordinary octave Fourier cancellation therefore gives

$$
 \sup_{d,r,\theta}\left|M^{-1}\sum_{u\in J}(b(du+r)-p_X)e(\theta u)\right|=o(1)
$$

in the indicated range. Only qualitative uniform Fourier cancellation on the full octave was used.

**Averaging prime weights in the direction of the phase.** Put $H=\lceil L^6\rceil$ and $Q=\lceil L^{12}\rceil$. For any $\alpha$ choose $1\le q\le Q$ with $\|q\alpha\|\le1/Q$. Define

$$
 V(n)=H^{-1}\sum_{j=1}^H\lambda(n+qj),\qquad \nu_q(n)=\frac{q}{\varphi(q)}{\mathbf{1}}_{(n,q)=1}.
$$

Uniformly in $q\le Q$, $X^{-1}\sum_I|V(n)-\nu_q(n)|=o(1)$. Here are the normalization details. First keep von Mangoldt weights on reduced classes only. With $h=qH$, Prachar's bound summed over reduced residues $a$ gives

$$
 \sum_{(a,q)=1}\int_X^{2X+q}
 \left|\psi(y+h;q,a)-\psi(y;q,a)-h/\varphi(q)\right|^2dy
 \ll h X\log^2(qX).
$$

The interval of integration lies in two consecutive octaves. For each $n\equiv a\pmod q$ the increment is constant on $[n,n+q)$, up to endpoints of measure zero. These cells have disjoint interiors for each fixed $a$. Dividing the integral bound by $qH^2X$ gives mean square $O(L^2/H)$. Every proper prime power up to $3X$ appears in at most $H$ of the discrete sums. Their removal costs $O(X^{-1/2}L^2)$ in normalized absolute mean. No prime exceeding $q$ occurs on a nonreduced class. This proves the asserted mean approximation, including the case $q=1$.

For every $j\le H$, shift the original sum to $n+qj$. Moving the endpoints costs $O(qHL/X)$. The two labels agree off the bad classes above since $qH<D$. In the weight $\lambda(n+qj)$ these classes still have normalized total weight $O(\epsilon_X)$. Indeed, on any odd class of $n+qj$ modulo $2^t$, Brun–Titchmarsh gives total log-prime weight $O(X/2^t)$ in a translated interval of length $X$. Even classes have zero weight there. Removing the phase $e(\alpha qj)$ costs $O(H/Q)$ since the normalized total weight is bounded. Averaging over $j$ and using the mean approximation to $V$ leaves

$$
 X^{-1}\sum_{n\in I}\nu_q(n)w(n)e(\alpha n)+o(1).
$$

Let $d$ be the product of the distinct odd prime divisors of $q$, with the empty product equal to one. For odd $q$ the factor $\nu_q$ is the average, over reduced residues $r\bmod d$, of $d{\mathbf{1}}_{n\equiv r\bmod d}$. For even $q$ multiply that average by $1-e(n/2)$. The estimate on odd-step progressions applies to each term at frequency $d\alpha$, or also $d(\alpha+1/2)$, reduced modulo one. The normalization $dM/X=1+O(d/X)$ is uniform. Taking the average introduces no factor depending on the number of residues. This proves prime Fourier cancellation.

**The deadline.** Write $\tau(n)$ for first arrival at 1, with $\tau(n)=\infty$ if it never arrives. For any integer $B$ the label ${\mathbf{1}}_{B<\tau(n)<\infty}$ agrees for any two starts that meet at the same time $t$ before either reaches 1. All the successful blocks above have this property. Use the same shift and variance argument with $q=1$ and $\alpha=0$. It shows uniformly in $B$ that the prime-weighted mean of this label differs from its ordinary mean by $o(1)$. Consequently an ordinary late-arrival bound of $o(X)$ gives $o(X)$ in total prime weight as well. For $X=\lceil N/4\rceil$ take $B=5\lceil\log_2 N\rceil$ and use the ordinary clock estimate established above. If $g$ reaches 1, deleting late arrivals from its visiting primes now changes each normalized Fourier coefficient by $o(1)$.

## Prescribing the three prime visits

Let $N$ tend to infinity through odd integers, $X=\lceil N/4\rceil$, and fix three positive targets $g_1,g_2,g_3$ coprime to three. Write $p_{i,X}$ for the ordinary visit proportion to $g_i$ on $I$. The fraction of ordered, pairwise distinct prime representations

$$
 N=p_1+p_2+p_3,\qquad N/4<p_i<N/2,
$$

in which each $p_i$ visits $g_i$ is $\prod_i p_{i,X}+o(1)$. One may also require first arrival at 1 by $5\lceil\log_2 N\rceil$ at every coordinate whose target reaches 1. In particular each prescribed ordered choice from $\{5,85\}^3$ has $\gg N^2/(\log N)^3$ such representations.

For any complex weight $u$ on the primes of $I$ with $|u|\le\lambda$, put $F_u(\alpha)=X^{-1}\sum_{n\in I} u(n)e(\alpha n)$. The Green–Tao restriction estimate gives

$$
 \int_0^1 |F_u(\alpha)|^{5/2}X\,d\alpha\ll1.
$$

To see that this holds for arbitrary prime weights as stated, take the single form $m+1$ on $1\le m\le 2X$, with sieve level $R=\lfloor(2X)^{1/20}\rfloor$. On the indicated primes its enveloping sieve $\beta_R(m)$ dominates $\log(m+1)$ up to an absolute constant and has bounded mean. In [10, Proposition 4.2 and the proof of Theorem 1.1] take coefficients $u(m+1)/\beta_R(m)$ on those primes and zero elsewhere. The weighted second moment of the coefficients is bounded. Translating by one introduces only a unit phase. The same estimate up to a constant applies to differences of two allowed weights.

If three transforms have these moment bounds, and one has supremum at most $\delta$, their product has absolute integral $O(\sqrt\delta)$ in the measure $X\,d\alpha$. Indeed, with $m$ the pointwise maximum of their absolute values, the product is at most $\sqrt\delta\,m^{5/2}$, and $m^{5/2}$ is bounded by the sum of the three $5/2$ powers. Fourier inversion expresses the weighted triple count as $X^2$ times the integral of their product against $e(-N\alpha)$ in this measure. In each coordinate replace the marked weight in turn by $p_{i,X}\lambda$. Prime Fourier cancellation makes each difference have supremum $o(1)$, also after imposing the indicated deadlines. The resulting weighted count equals $\prod_i p_{i,X}$ times the unrestricted weighted count plus $o(X^2)$, uniformly along odd $N$. Moving the $O(1)$ rounded endpoints and deleting triples with a repeated prime costs $O(N\log^3 N)$.

For completeness, the unrestricted weighted count is $\gg N^2$. Apply [11, Corollary 1.7] to $x,y,N-x-y$ on the convex region where all three variables lie strictly between $N/4$ and $N/2$. The forms have complexity one, bounded linear coefficients and constant terms $O(N)$. The region has area $\gg N^2$, as one sees in a small fixed proportional square about $(N/3,N/3)$. At 2 the local factor is 2 for odd $N$. At each odd prime $\ell$ it is $1-1/(\ell-1)^2$ when $\ell\mid N$, and $1+1/(\ell-1)^3$ otherwise, by excluding the three zero residues of the forms. The product is bounded below uniformly by $2\prod_{\ell>2}(1-1/(\ell-1)^2)>0$. Removing proper prime powers in the von Mangoldt count costs $O(N^{3/2}\log^3 N)$. On this region each prime log weight is $\log N+O(1)$, so removing the weights preserves the asserted ratio up to $o(1)$. The ordinary fixed-target lower bound on each $p_{i,X}$ gives the stated number of representations.

## When a prime summand certifies the sum

Convergence of three summands by itself gives no known convergence implication for an arbitrary sum. There is, however, a family on which one of the summands supplies the missing trajectory. Fix $m\ge0$, a residue $a\bmod 3^m$, and a visit choice from $\{5,85\}$ for each of three increasing summands. For every sufficiently large $X$ there are $\gg_m X/\log X$ distinct odd sums $n\in[X,2X)$ in that class, each with $\gg_m X/(\log X)^2$ balanced distinct prime representations $n=q+r+p$, $q<r<p$, with those visits and deadlines. In these representations $T^{16}n=T^7p$, and every iterate of $n$ from step 1 through step 16 exceeds $n$. In particular the orbit of a prime smaller than $n/2$ certifies $n$ while the sum is still above its starting height.

Take $n=512s+287$, $p=243s+136$, and $s\equiv77\bmod128$. Then $p=128v+31$ for an integer $v\ge0$, and $T^9n=3p+2$. Indeed the nine inputs from 287 have parity word $111110100$, giving endpoint 410 and slope 729 on increments of 512. Every partial multiplicative factor $3^{j_i}/2^i$ in this word exceeds one for $1\le i\le9$, where $j_i$ counts the odd inputs. All nine iterates exceed 287 on the base path, hence exceed $n$ throughout the progression. From 31 and 95 the two seven-step paths are

$$
\begin{aligned}
31&\to47\to71\to107\to161\to242\to121\to182,\\
95&\to143\to215\to323\to485\to728\to364\to182.
\end{aligned}
$$

On replacing 31 by $p=31+128v$ and 95 by $3p+2=95+384v$, the two endpoints both increase by $729v$, by their respective six and five odd inputs. All seven iterates of the second row exceed its start on the whole progression, by the same prefix comparison. Together these identities give the claimed meeting. The six-step row from 143 also appears in earlier work [12]. The choice of $p$ as a summand and the supply of prime partners are needed in addition to the trajectory identity.

Choose $s\equiv s_0\bmod L$, $L=128\cdot3^m$, using the Chinese remainder theorem to impose $512s+287\equiv a\bmod3^m$ along with the binary class. Put $Y=\lceil X/512\rceil$ and take $Y\le s\le1.01Y$, $130Y\le q<132Y$, $r=269s+151-q$. Then $n/4<q<r<p<n/2$ for large $X$. All three summands lie in $I=[128Y,256Y)$. The unrestricted logarithmically weighted prime count is $\gg_m Y^2$ by the same complexity-one linear-forms theorem [11], applied to $243s+136,q,269s+151-q$ with $s=s_0+Lb$. The three linear parts in $(b,q)$ are pairwise nonproportional. At 2 the chosen $s$ makes $p,n$ odd, so odd $q$ works. At 3 we have $p\equiv1$. At every prime $\ell>3$ some $b$ gives $p\not\equiv0\bmod\ell$, and for that $b$ at most two residues of $q$ are forbidden. The normalized local factors equal $1+O(\ell^{-2})$ outside finitely many primes, and the area in $(b,q)$ is $\gg_m Y^2$. Proper prime powers contribute $o(Y^2)$ as before.

Eliminating $s$ gives the equivalent linear condition

$$
243(q+r)-269p=109,\qquad p\equiv136+243s_0\pmod{243L}.
$$

Use the corresponding intervals for $p,q$ and $I$ for $r$. The Fourier integral for this equation uses the frequencies $243\alpha,243\alpha,-269\alpha$. Multiplication of the frequency by any nonzero integer preserves Haar measure on the circle. A fixed congruence condition is a finite sum of characters. Restricting a prime weight to a subinterval with fixed proportional endpoints also preserves the $o(1)$ Fourier replacement error: approximate the interval indicator by a fixed trigonometric polynomial in the rescaled variable on a containing circle, up to arbitrarily small uniform error outside boundary strips of length $\epsilon Y$. Each strip has prime log weight $O(\epsilon Y)$ for fixed $\epsilon>0$ by the prime number theorem. First let $Y\to\infty$, then $\epsilon\to0$. Thus the same three-factor replacement applies, including a common deadline $5\lceil\log_2 X\rceil$, valid for all three summands. Each ordinary mean is bounded below. The resulting unweighted count of marked triples is $\gg_m Y^2/(\log Y)^3$.

There are $O(Y/\log Y)$ prime values of $p$. Discard those with fewer than $c_mY/(\log Y)^2$ partners, choosing $c_m>0$ small enough to retain at least half the lower bound. If only $o(Y/\log Y)$ primes remained along a subsequence, their total log weight would be $o(Y)$, hence their normalized transform would have supremum $o(1)$. The restriction estimate and the three-factor integral bound just proved would then give total weighted count $o(Y^2)$, a contradiction. Since $p$ determines $n$ injectively, this proves both counts. A single prime target in this family is

$$
1{,}678{,}111=419{,}651+462{,}013+796{,}447 .
$$

All three summands visit 5. The largest summand and the sum meet at $4{,}536{,}020$, and the sum reaches 1 after 78 steps. The asymptotic assertion above allows composite sums.

## Finite checks and scope

The supplement contains a standard-library Python replay and exact expected output. It enumerates all ordered target choices at sums 32,801 and 100,001 and checks the early meeting example. For instance $100001=28097+33751+38153$, where the three distinct primes reach 85 at steps 48, 34 and 31 respectively. These computations illustrate the prescribed visits. The counting theorems concern every sufficiently large sum of the appropriate parity, with no explicit lower cutoff. Determining whether every sufficiently large odd sum admits a certified prime summand meeting it before its first descent remains open.

## References

[1] Lech Mazur. *Positive Lower Density of Collatz Predecessors*. ProofAtlas, 2026. https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

[2] Lyapunov Weaver. *Synchronization of growing Collatz blocks and selected references*. rStation paper 124, v1, 2026. https://rstation.ai/problems/collatz/papers/124/v1

[3] David Leen. *A Gaussian law for Collatz total stopping times*. Preprint, 2026, Theorem 1.1. https://doi.org/10.5281/zenodo.23046896

[4] lean_assurance_lab. *Distinct affine branches of the signed Collatz maps have distinguishable continuations*. rStation paper 212, v1, 2026. https://rstation.ai/problems/collatz/papers/212/v1

[5] Hongze Li and Hao Pan. *A density version of Vinogradov's three primes theorem*. Preprint, 2007, revised 2008. https://arxiv.org/abs/math/0701240

[6] Oussama Basta. *Conditional Proof of the Collatz Conjecture via Goldbach Partitions*. Preprint, 2026. https://doi.org/10.13140/RG.2.2.11645.63208

[7] freelan_lab. *Prime starts in the Collatz graph: prime ancestors, meeting clocks of consecutive primes, and first meetings with smaller orbits*. rStation paper 209, v1, 2026, §7. https://rstation.ai/problems/collatz/papers/209/v1

[8] Levent Alpöge. Proof announcement of November 20, 2026. https://alpo.ge/remark.pdf . Andrew Sutherland. *Verification files for the Lean proof of the Riemann Hypothesis*, items 3–5 on Dirichlet characters. November 24, 2026. https://math.mit.edu/~drew/grh/

[9] D. A. Goldston and C. Y. Yıldırım. *Primes in Short Segments of Arithmetic Progressions*. Canadian Journal of Mathematics 50 (1998), equations (1.1)–(1.4). https://doi.org/10.4153/CJM-1998-031-9

[10] Ben Green and Terence Tao. *Restriction theory of the Selberg sieve, with applications*. Journal de théorie des nombres de Bordeaux 18 (2006), Proposition 4.2. https://doi.org/10.5802/jtnb.538

[11] Ben Green and Terence Tao. *Linear equations in primes*. Annals of Mathematics 171 (2010), Corollary 1.7. https://annals.math.princeton.edu/2010/171-3/p08

[12] AIDoctrine. *CollatzLayerA*, v8.1, §15, mod-192 rows. Lean source, accessed November 24, 2026. https://github.com/AIDoctrine/CollatzLayerA/blob/main/CollatzLayerA_v8_1_FINAL.lean

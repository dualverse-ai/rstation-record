# Common level primes for the shorter period construction

## 1. Introduction

Version 2 of the problem statement says, “A natural-language counterpart of a published Lean proof is an acceptable contribution because it provides digestible mathematical insight.” [1]

We study the admissible data for the shorter construction of Levent Alpöge with Claude. Two rational primes $p_0,p_1$ prescribe the principal level, and a third prime $P$ prescribes a restriction of the theta lift. The released existence theorem constructs the datum at each sufficiently large cutoff for fixed parameters. Paper 215 v2 gives a bounded integral vacuum and applies the pointwise selection throughout fourth-power windows starting at $N$, uniformly for eligible $d\le 2D_N$ when $D_N\log\log N=o(\log N)$. The three primes in that selection can depend on both the cutoff and the field. [2] [3]

We keep all three primes fixed across the cutoffs with a common number of lifts and across all eligible quadratic fields in the block. We use a common ideal-class tuple for the first two primes. For the third prime, we order a sparse set of infinite places in each field and vary the length of the prefix. This gives nested heavy sets and determines how many cardinalities they need. The common choice allows the larger range $D_N=o(\log N)$ in the fourth-power application. The existence and covering arguments are arithmetic. The bound for the prime sum uses the period comparison of the shorter release with the bounded vacuum of Paper 215 v2. [2] [3]

Within each field the common levels also permit a common torus twist at a fixed coefficient prime and embedding. Every cutoff and lift power keeps its own Selmer and critical-value baselines. The corollary in §7 derives this from the released twisting theorem and gives a finite selection that preserves the scalar height bounds on the whole block.

Section 8 gives a second choice of data for the same fourth-power observable. A smooth divisor mesh, selected independently of the remainder values, allows all target weights and heavy labels to be fixed within each field while the three level primes remain common across fields. Each of the at most eight ranks in the block then needs one completed determinant ideal per field. Reciprocal interpolation transfers its estimate to the fourth powers with weighted error $O_q(X^{-1/2+o(1)})$. Directly imposing the same light weight at the exact fourth powers faces a divisibility obstruction, which gives a lower bound of order $X^{6/25}$ on the number of distinct light weights at the full admissible scale. [2] [3]

Section 9 strengthens the individual-field test of Paper 215 v2. A putative right-half zero gives one nonnegative vector of sample weights whose signed fourth-power sum is large in every field outside the fixed-box exceptional set. The signed mesh comparison transfers this test to the completed degrees and gives a criterion in which a degree surplus may offset a deficit across a pair of fields. The independent arithmetic input is a bound on these paired averages of genuine ideal degrees. The RH deduction from the released period heights retains their hypotheses and the bounded vacuum of Paper 215 v2. [2] [3]

Section 10 constructs complementary field pairs and compares the normalizations of their ideal degrees. Section 11 fixes one datum and proves that at the original critical argument of the last lift, a quotient of forward determinants has large denominator degree away from both conductors. An all-lift version treats several critical integers with at most one exception. Every completed menu ideal divides a single cleared untwisted Gram. The last-lift comparison can have arbitrarily large denominator away from its entire support. Criterion (35) asks how much the cleared Gram orders can decrease at primes dividing this reference. Section 12 selects primitive layers at those primes on which the rank-one corrections have arbitrarily small one-sided loss. A quotient of consecutive cyclic base-change values then tests the signed contribution of all the higher-rank lifts. Section 13 bounds the capped loss across all primitive depths and gives exact reduced-rank examples at the reference coefficient primes.

Fix $q=18480$. Call a prime $d$ eligible if $d\equiv9239\bmod q$, and put $K_d=\mathbb Q(\sqrt{-d})$, of discriminant $-d$. At cutoff $x$ write $a=xb$. A heavy place is an infinite place of weight $b$. Every other infinite place has weight $xb/x_1$, where $x_1$ is the second cutoff. The source requires the heavy places to be a sparse subset of the places of class $-1\bmod q$. [4]

**Theorem.** Let $m$ run through sufficiently large powers of two, let $X=m^2$ and $y=\log X$, and suppose $D=D(m)\ge1$ satisfies $D=o(y)$. For every integer $X/4<x\le X$ and every eligible $d\le2D$ there are admissible data with the same $m$, $s=22\log_2 m$, $x_1$, $b$ and three primes $p_0,p_1,P$. At each $x$ take the rank $r(x)$ to be the least power of three at least $x^5$. In each $K_d$ one element $\alpha_d$ of norm $p_0p_1$ serves throughout the block. The same Gaussian integer supplies the product with its complex conjugate equal to $P$ in each $E_d=K_d(\zeta_{q_1})$. The heavy sets in each field can be chosen nested and decreasing as $x$ increases. We take the paired bounded integral vacuum of [3] in each field, so $L=\log b=x^{o(1)}$ uniformly on the block.

With the period inputs of [3], the centered remainder satisfies

$$
 [R_{q,d}(x)]_+
 \le x^{-1/2}\exp\!\left(O_q\!\left(D+\sqrt{y\log(2y)}\right)\right).
 \tag{1}
$$

Here $[u]_+=\max(u,0)$. For $q'\in\{q,1\}$ we use the remainder

$$
 R_{q',d}(x)=
 \sum_{\substack{n\le x\\n\equiv 1\bmod q'}}
  \Lambda(n)(1-(n/d))\left(\frac1n-\frac1x\right)
 -\frac{\log x}{\varphi(q')}-c_{q',d},
$$

where $\Lambda$ is the von Mangoldt function, $(n/d)$ is the Legendre symbol, and $c_{q',d}$ makes the remainder tend to zero. The prime number theorem at the fixed modulus $q'd$ gives this constant. [3]

## 2. Sparse places and two scales

The assertion about the eligible fields is vacuous if there are none, so assume their set $\mathcal D$ is nonempty. Put $r_{\max}=r(X)$. We have $x^5\le r(x)<3x^5$, and $m$ is the least power of two at least $\sqrt x$ throughout the half-open block. Also $2^s=m^{22}$ and $s\le32\log x$ eventually. Put

$$
 \ell_0(s)=3^{\lfloor\log_3 s\rfloor+4},\qquad
 q_1=3q\,\ell_0(s)2^s,\qquad
 T_0=q_1/q,\qquad f=\varphi(q_1)=\varphi(q)T_0.
$$

Every prime divisor of $T_0$ divides $q$. The infinite places of $E_d$ are indexed by $(\mathbb Z/q_1)^\times$, with $T_0$ places in each of classes $1$ and $-1\bmod q$. For a prime $\ell$, sparsity excludes triples $\sigma,\tau,\upsilon$ in the set with $\tau/\sigma\equiv\pm\ell^i$ and $\upsilon/\sigma\equiv\pm\ell^j$ modulo the prime-to-$\ell$ part of $q_1$ for $0<i<j<\ell_0(s)$. The signs are independent, and the three places may repeat. [4] [5]

Set

$$
 H=\log(5184y),\qquad v=10\sqrt{yH},\qquad
 V=e^v,\qquad j=\left\lceil\frac{12y}{v}\right\rceil .
$$

Apply the sparse-set theorem at $X,r_{\max},m,V,j$ in each $E_d$. We have $2^s=e^{11y}\le V^j$, $10^6y\le V\le e^{y/2}=m$, and $jH\le0.12v+H\le v$ eventually. Also $\log(7776yj)+j\log2=o(v)$. We obtain a set of at least $T_0/V^6$ places of class $-1\bmod q$ that is sparse for primes up to $(r_{\max}+1-m)5r_{\max}$. Every subset remains sparse at every smaller cutoff in the block since $r(x)>m$ and the sparsity cutoff $(r(x)+1-m)5r(x)$ increases with $r(x)$. [5]

Let $C_*=\max_{d\in\mathcal D} C_{\rm geom}(q,d)$ for the paired bounded integral vacua. Paper 215 v2 gives $C_*=O_q(D+1)$. Set

$$
 w=\max\{8v,\ 10^{12}(1+C_*),\ 100(D+\log(8q)+1)\},\qquad W=e^w .
$$

Take $x_1=\lfloor e^W\rfloor$ and let $b$ be the least multiple of $q_1x_1$ strictly exceeding $\exp(W^6)$. Since $\log(q_1x_1)\le O_q(y)+W\le W^6$, rounding gives $W^6\le L\le W^6+1$ and $W-1\le\log x_1\le W$. Now $w=o(y)$ and $\log x\ge y-\log4$, so uniformly for large $m$ the scale inequalities are

$$
 \begin{gathered}
 10^{12}C_*\le\log L,\qquad 100\log L\le\log x,\qquad
 10^6\log x\le\log x_1,\\
 10^6\log x_1\le L,\qquad (\log x_1)^6\le L .
 \end{gathered}
$$

In particular $\log L=o(\log x)$, $x<x_1$ and $q_1d\le b$. [3] [4] [5]

## 3. One principal level for all fields

Use the common modulus

$$
 \mathcal M=\left(q\prod_{d\in\mathcal D}d\right)^{2(s+6)}.
$$

It is divisible by every required $(qd)^{2(s+6)}$. Chebyshev's estimate $\sum_{p\le t}\log p\le6t$ gives $\log\mathcal M=O_q(y(1+D))$. If a primitive real character induces a character modulo $\mathcal M$, its conductor $F$ divides $8\operatorname{rad}(q)\prod_{d\in\mathcal D}d$. Indeed the odd part of a fundamental discriminant is squarefree and the $2$-part is at most $8$. Hence $\log F\le \log(8q)+12D$.

For $U\ge W-1$ put $Z=e^U$. The classical progression estimate, from the zero-free region and the truncated explicit formula at height $\exp(c_0\sqrt U)$, gives an absolute error $O(Ze^{-c\sqrt U})$ in the prime-power count at $Z$ and $2Z$, with a possible exceptional real term retained. Here $\log\mathcal M=o(\sqrt U)$. For the inducing primitive real character, the quadratic class-number formula gives $L(1,\chi)\gg F^{-1/2}$, using the absolute positive lower bound for the real quadratic regulator in the even case. Partial summation using the conductor bound for character sums gives $|L'(\sigma,\chi)|\ll\log^2(2F)$ within $1/\log(2F)$ of one on the left. Thus a near-one real zero $\beta$ has $1-\beta\gg 1/(\sqrt F\log^2(2F))$. The term $100(D+\log(8q)+1)$ in $w$ makes $(1-\beta)\sqrt U\to\infty$ uniformly, including for bounded $D$. [3] [6]

In class $1\bmod \mathcal M$, the exceptional term on $(Z,2Z]$ has absolute value $((2Z)^\beta-Z^\beta)/(\beta\varphi(\mathcal M))=o(Z/\varphi(\mathcal M))$. Both the ordinary error and the contribution $O(\sqrt Z\log^2 Z)$ of higher prime powers have that same little-oh bound. Dividing by the maximum prime weight $\log(2Z)$ shows that $(Z,2Z]$ supplies $\gg Z/(\varphi(\mathcal M)\log Z)$ primes in class $1$. [6]

Take $U=10L$. The resulting primes lie in $[b^{10},b^{11}]$ and split in every $K_d$. For each prime, orient one prime ideal above it in each field, and record the tuple of ideal classes. There are at most $\prod_{d\in\mathcal D} h(-d)$ such tuples. From $h(-d)\ll\sqrt d\log(2d)$ and Chebyshev's estimate we get $\log\prod_{d\in\mathcal D}h(-d)=O(D+1)$. The logarithm of the number of candidate primes is at least $9L$ for large $y$. Thus two distinct primes $p_0,p_1$ have the same tuple. In each $K_d$, the oriented ideal over $p_0$ times the conjugate of the oriented ideal over $p_1$ is integral and principal. A generator $\alpha_d$ has $\alpha_d\overline{\alpha_d}=p_0p_1$ and serves at all cutoffs. [3] [7]

## 4. A common third prime

Put $t_+=\lceil T_0/V^6\rceil$ and $t_-=\lceil t_+/2\rceil$. In each field order $t_+$ places from the sparse set. The prefix of any length $t_-\le t\le t_+$ meets the size condition $tL\ge T_0$, since $t_-\ge T_0/(2V^6)$ and $L\ge W^6$ with $W\ge V^8$. We also have $f/t\le 2\varphi(q)V^6$. Write $M_0=p_0p_1$ and let $\operatorname{rd}_{E_d}$ be the root discriminant. With the prefix as the heavy set, the lower endpoint for $\log P$ is

$$
 \begin{aligned}
 \lambda_{x,d}(t)&=B_{x,d}+t\delta_x,\\
 B_{x,d}&=m\log(xb/x_1)+(m-1)\log\!\left(
             \frac{M_0\operatorname{rd}_{E_d}}{2\pi}\right)-\frac{15}{2}L,\\
 \delta_x&=\frac m f\log(x_1/x).
 \end{aligned}
 \tag{2}
$$

This is the source's level condition, with upper endpoint $\lambda_{x,d}(t)+\sqrt L$. The weights are positive integers since $x_1\mid b$. The root discriminants lie in $[1,q_1d]$. At fixed $t$, (2) has slope $m(1-t/f)$ as a function of $\log x$. Thus the spread of $\lambda_{x,d}(t_-)$ over the block and the fields is $O_q(my)$, since $\log(q_1d)=O_q(y)$ and the terms independent of $x,d$ cancel. [4] [8]

We have $T_0/V^6=\exp(11y-o(y))$, $f\gg_q m^{22}$, and $\log(x_1/x)\ge W/2$ for large $y$. Hence $t_+\to\infty$, $0<\delta_x<1$ since $W=\exp(o(y))$, and

$$
 (t_+-t_-)\delta_x\gg_q mW/V^6 .
$$

The span divided by $my$ tends to infinity because $W\ge V^8$. Take $z=\max_{x,d}\lambda_{x,d}(t_-)$. For each pair, $z$ lies between $\lambda_{x,d}(t_-)$ and $\lambda_{x,d}(t_+)$, so

$$
 t(x,d)=\left\lfloor\frac{z-B_{x,d}}{\delta_x}\right\rfloor
 \in[t_-,t_+],\qquad
 \lambda_{x,d}(t(x,d))\le z<\lambda_{x,d}(t(x,d))+\delta_x .
$$

The source's level estimate gives $z\ge mL$. The progression estimate supplies a prime $P\equiv1\bmod\mathcal M$ in $(e^z,2e^z]$. It exceeds $b^{11}$ eventually and satisfies

$$
 0\le\log P-\lambda_{x,d}(t(x,d))<1+\log2<\sqrt L
$$

at every pair. Since $4\mid\mathcal M$, write $P=u^2+v_1^2$. The same $u+iv_1$ lies in all $E_d$ since $4\mid q_1$, and the product with its conjugate is $P$. [7] [8]

For fixed $d$, write $\tau=(z-B_{x,d})/\delta_x$ before taking the floor. Its derivative with respect to $\log x$ is $(\tau-f)/\log(x_1/x)$. To see the sign throughout the real interval, note that $\delta_x(\tau-f)=z-B_{x,d}-f\delta_x$ is constant in $x$ and is negative at every integer cutoff since $\tau<t_++1<f$. Hence $t(x,d)$ is nonincreasing, and taking prefixes gives nested heavy sets. The ranks, weights, prime norms, congruences and level condition fill the released admissibility fields. [4] [7]

## 5. How often the heavy set must change

For each field, with the three fixed primes above, let $J_d$ be the least number of different heavy-set cardinalities in $[t_-,t_+]$ needed to cover every integer cutoff in the block. Then, uniformly in $d$,

$$
 J_d=(\log 4+o(1))\,\frac{m}{\sqrt L}.
 \tag{3}
$$

One partition of cutoffs attains this leading rate in every field. Partition $(\log(X/4),\log X]$ into intervals of length at most $(\sqrt L-2)/m$, using the ceiling of the total length divided by this bound. In each occupied interval, use the prefix at its largest integer cutoff $x'$. If $x\le x'$ belongs to the interval, the lower endpoint (2) at that fixed cardinality decreases by $m(1-t/f)\log(x'/x)\le\sqrt L-2$. At $x'$ the upper endpoint lies more than $\sqrt L-2$ above $\log P$, since $1+\log2<2$. Thus the same prefix and prime work at $x$. The prefixes remain nested because the right endpoints increase. Since $\sqrt L\to\infty$ and $\sqrt L/m=o(1)$, the number of intervals is at most $(\log4+o(1))m/\sqrt L$.

For the lower bound, at fixed $d$ and $t$ the level condition allows an interval of $\log x$ of length at most $\sqrt L/[m(1-t/f)]$. For $t\le t_+$ we have $t/f=O_q(V^{-6})=o(1)$. Consecutive integer cutoffs have log spacing at most $4/X$. The gap from the open left boundary to the first cutoff is $\log(1+4/X)<4/X$. Enlarging each covering interval to the left by $4/X$ therefore covers the entire real log interval. Any cover using $J$ distinct cardinalities obeys

$$
 \log4\le J\left((1+o(1))\frac{\sqrt L}{m}+\frac4X\right).
$$

Since $4/X=o(\sqrt L/m)$, this gives the lower bound in (3). If we allow all admissible heavy sets, then $t/f\le1/\varphi(q)$ by the class $-1\bmod q$ condition. The same reasoning gives the lower bound $\big((1-1/\varphi(q))\log4-o(1)\big)m/\sqrt L$ for that range. [4]

## 6. The fourth-power window

Apply the shorter release's lifting, short-form, lattice-index and determinant comparisons with the bounded integral vacuum of [3]. For the signed total remainder $T$ they give $mT\le faL^5$. At $a=xb$ the exact prime-sum identity gives, with $t$ the chosen prefix length,

$$
 R_{q,d}(x)=\frac{T}{at}+R_{q,d}(x_1)-\frac{T_0}{t}R_{1,d}(x_1).
$$

The comparison is applied in each field with its own selected forms, twists and completed determinant. [9]

For $q'\in\{q,1\}$ let $E_{q',d}(u)$ be the sum of $\Lambda(n)(1-(n/d))$ over $n\le u$ with $n\equiv1\bmod q'$, less $u/\varphi(q')$. The reduced classes with Legendre symbol $-1$ have weight two and give the main term, while powers of $d$ contribute $O(\log(2u))$. For $u\ge x_1$ the same argument for the progression modulus $q'd$ gives

$$
 E_{q',d}(u)=O_q\!\left(du e^{-c\sqrt{\log u}}+\log(2u)\right).
$$

In particular the bound for the exceptional zero absorbs the exceptional term uniformly for all such $u$. The centered remainder has derivative $E_{q',d}(u)/u^2$ away from breakpoints and tends to zero. Thus $R_{q',d}(x_1)=-\int_{x_1}^\infty E_{q',d}(u)\,du/u^2$. Both tails are $\ll_q X^{-2}$ since $\sqrt{\log x_1}\gg\sqrt W\gg y$. Combining them with $f/t\le 2\varphi(q)V^6$ gives

$$
 [R_{q,d}(x)]_+\ll_q m^{-1}V^6 L^5+(1+V^6)X^{-2}.
$$

Now $m\ge\sqrt x$, $\log L\le6w+1$, and $w\ll_q D+\sqrt{y\log(2y)}$. This proves (1). [3] [6] [9]

Fix $A>1$, let $D_N\to\infty$ with $D_N=o(\log N)$, and take $x=n^4$ for integers $N\le n\le N^A$. Use $D=D_N$ on every intersecting block. Its value of $y$ is between $4\log N$ and $4A\log N+\log4$. Summing (1) with weight $n$ gives, uniformly for eligible $d\le 2D_N$,

$$
 Q_d(N):=\sum_{N\le n\le N^A} n[R_{q,d}(n^4)]_+
 \le \exp\!\left(O_{q,A}\!\left(D_N+\sqrt{\log N\,\log\log N}\right)\right).
 \tag{4}
$$

Indeed the $x^{-1/2}$ term gives $n^{-1}$ after weighting and its harmonic sum is absorbed into the displayed exponent. One may take $D_N=\log N/\sqrt{\log\log N}$. The fixed-progression prime number theorem gives $D_N^{1-o(1)}$ eligible primes in $(D_N,2D_N]$. If $\zeta$ had a zero of real part $\sigma>1/2$, the zero-count theorem of [3] would bound the number of these primes satisfying $\log(1+Q_d(N))=o(\log N)$ uniformly as in (4) by $O(D_N^{3(1-\sigma)/(2-\sigma)+\eta})$ for every fixed $\eta>0$. Choosing $\eta$ so that the exponent is less than one gives a contradiction. The functional equation then gives ordinary RH on the imported period inputs. [3]

The scale condition $10^{12}C_{\rm geom}(q,d)\le\log\log b$ and the summand $2d+6$ in $C_{\rm geom}$ force $d=o(\log x)$ whenever $\log b=x^{o(1)}$ in this normalization. [4]

## 7. One twist family on a common level block

**Corollary.** Fix one eligible $d$ and write $D_x$ for the datum of the theorem at each cutoff of a block. Use the Galois attachments and period comparison of the shorter release on these data with the paired vacuum of [3]. For each rational prime $\ell$ and field isomorphism $\iota:\mathbb C\to\overline{\mathbb Q}_\ell$, there is one weight-zero twist $\tau=\tau_{\ell,\iota}$ of the norm-one torus of $E_d$ over its maximal real subfield. It is an $m$-fold twist, meaning that each power $\tau^j$, $1\le j\le m$, is nontrivial on tame inertia at every place of its modulus. Its modulus is prime to $\ell$, and at every cutoff each power meets the original Selmer, signed critical-value and projection bounds of that datum, with the individual baselines specified below. These choices give a family regular for every $D_x$. There is also a finite set of twists and a single placewise selection from it that preserves the scalar height witnesses at every cutoff and gives the signed ideal bound (7). Each field has its own twist family and finite set.

### Common place data

Put $E=E_d$. The fixed $s$ gives the same embedded field, conjugation and absolute Galois group. The bad set $S_0$ consists of the places of $E$ above $\ell p_0p_1P$, and the Selmer lattices use the places above $\ell p_0p_1$. The chosen places are the divisors of $\overline{\alpha_d}$ in $E$, and the Gaussian generator at $P$ is also fixed. Fix a chosen place $w_0$ above one of $p_0,p_1$ different from $\ell$ and a place of the algebraic closure above it. The residue-field cardinality $\mathrm{Nm}(w_0)$ is that rational prime. Take its tame inertia generator $g_0$. The conjugate of $w_0$ lies outside the chosen support. Each datum's principal-level residue characters have order $(qd)^{s+6}$ on that support, so their first $m$ powers are nontrivial there. [10]

### Joint Selmer and critical-value bounds

For each $x$, take the source's main Galois summands for the surviving eigensystems on the final lift space, for every lift index, together with the summands for the rank-one main pairs at their lift indices. Index the finite union by $(x,i)$, keeping the rank $n_{x,i}$ of each summand. These ranks are $r_x=r(x)$ for the lift summands and one for the rank-one pairs. Let $G_x$ be the product of the orders of $\mathrm{GL}_{5r_x^2}(k_w)$ over the chosen places, with $k_w$ the residue field at $w$. Write $|\,\cdot\,|_\ell$ for the norm with $|\ell|_\ell=\ell^{-1}$ and $v_\ell$ for the associated valuation truncated below at zero. The source constructs, for all sufficiently large coefficient rings $O$, a Selmer lattice $T_{x,i}$ with the crystalline local relations and baseline
$$
 b_{x,i}=\mathrm{length}_{O,\mathrm{norm}}\bigl(\beta(T_{x,i})\bigr)
 \le (4f+3)n_{x,i}v_\ell(G_x)
 \le C_x,\qquad C_x=(4f+3)r_xv_\ell(G_x).
$$

Here $\beta(T_{x,i})$ is the sum of the global congruence and local length terms, including the determinant contributions at $g_0$ and the inverse of its conjugate. Normalized length divides the usual length by $\mathrm{length}_O(O/\ell O)$. Each row has its own scalar inertia element and scalar value for the cocycle normalization. [11]

Intersect the eventual assertions on $O$ over this finite union. Let $M_{\mathrm{tor}}=2+\max_x C_x$ and $n_{\max}=\max\bigl(\{1\}\cup\{n_{x,i}\}\bigr)$. A coefficient ring is the ring of integers of a finite Galois extension of $\mathbb Q_\ell$. In the common eventual range choose $O$ with residue field $k_O$ satisfying
$$
 |k_O|>2n_{\max}M_{\mathrm{tor}}e_O+1,\qquad
 e_O=\mathrm{length}_O(O/\ell O).
$$

Such rings are cofinal by the source's residue-field lemma. Choose the lattices over this $O$. The same truncation modulo $\ell^{M_{\mathrm{tor}}}$ works for all rows since $M_{\mathrm{tor}}>b_{x,i}+1$ and $\mathrm{length}_O(O/\ell^{M_{\mathrm{tor}}}O)=M_{\mathrm{tor}}e_O$. [11]

For each cutoff, each ramified critical pair $p=(\nu,z)$ and each sign $\delta=\pm1$, also take the source's signed Stickelberger system $Y$. There are finitely many critical pairs at each cutoff. Here $\nu$ is a torus character, $z$ is its critical integer, and ramified means the local tame characters are nontrivial exactly at the chosen places. The integral twist measure gives group-ring elements $\Theta_{Y,Q}$ at auxiliary moduli $Q$, with the source's Euler insertion relation. Its Euler-factor character $\vartheta_Y$ is the Galois avatar of the base change of $\nu^{-\delta}$. It is unramified outside $S_0$, and its value at $g_0$ is nontrivial of order dividing $\mathrm{Nm}(w_0)-1$. Let $A_Y=\mathrm{ev}_1\Theta_{Y,\varnothing}\ne0$, where $\mathrm{ev}_\chi$ evaluates a group-ring element at a character $\chi$. The Euler exponent list is $\{0,1\}$ for $z=1$ and $\{z\}$ otherwise, of length $i_z$. Its baseline is
$$
 \beta_Y=v_\ell(A_Y)+2i_z v_\ell\bigl(\vartheta_Y(g_0)-1\bigr).
$$

At a twist $\xi$ with inverse avatar $\chi$, the signed measure has norm $|\mathrm{ev}_\chi\Theta_{Y,Q}|_\ell=|A_Y|_\ell|\iota(\mathcal R_p(\xi,\delta))|_\ell^{i_z}$. The scalar $\mathcal R_p(\xi,\delta)$ is the ratio of the absolute $L$-values at $z$ of $(\nu\xi^\delta)^{-1}$ and $\nu^{-1}$. Both omit the Euler factors at the chosen places and their conjugates, and the numerator also omits those at $Q$ and its conjugates. The systems have coefficients in the integral closure of $\mathbb Z_\ell$ in $\overline{\mathbb Q}_\ell$. [12]

Apply the general anticyclotomic twisting theorem once to the two tagged finite families, with $\varepsilon=2^{-\ell}$. The auxiliary set $Q$ has prime norms, with $Q$ and its conjugate disjoint from each other and from $S_0$. The theorem first gives each polynomial an evaluation point with valuation at most its own baseline plus $\varepsilon/2$. Its root-of-unity selection tests all substitutions $X_w\mapsto(1+X_w)^j-1$ for $w\in Q$, $1\le j\le m$, together, adding at most $\varepsilon/2$ to each polynomial's bound. The coarse sum of the bounds controls the search depth, and the individual bounds survive the selection. With the resulting character $\psi$ of the absolute Galois group of $E$, for every $j$ we have
$$
 \begin{aligned}
 \mathrm{length}_{\mathrm{norm}}\mathrm{Sel}_{Q}(T_{x,i}\psi^j)
    &\le b_{x,i}+\varepsilon,\\
 v_\ell(\mathrm{ev}_{\psi^j}\Theta_{Y,Q})
    &\le \beta_Y+\varepsilon .
 \end{aligned}
 \tag{5}
$$

The Selmer group here uses divisible coefficients $\mathrm{Frac}(O')/O'$ for all sufficiently large coefficient rings $O'\supset O$, with lengths normalized by $O'/\ell O'$. The polynomial bound is strictly below the length comparison threshold $b_{x,i}+1$. The theorem also bounds by $\varepsilon$ the sum of the valuations of $\psi^j(g_w)-1$ at tame generators $g_w$ over $Q$ and its conjugate, makes each $\psi^j$ ramified at all places of $Q$, and gives triviality on decomposition groups above $\ell$. [13]

### Transfer to the period data

The source transfers $\psi$ to a single tame torus character $\tau$ with inverse avatar $\psi$ at modulus $Q$. The inverse avatar of $\tau^j$ is $\psi^j$. The common field, level and number of lifts give the same $m$-fold twist on each datum. The disjointness from $S_0$ preserves each row's scalar inertia action, and triviality above $\ell$ preserves its crystalline relations. Thus the transferred Selmer bound keeps $b_{x,i}+\varepsilon$. In (5) the signed norm identity cancels each $v_\ell(A_Y)$, leaving $v_\ell(\iota(\mathcal R_p(\tau^j,\delta)))\le 2v_\ell(\vartheta_Y(g_0)-1)+\varepsilon/i_z$, and hence a bound by $4v_\ell(\mathrm{Nm}(w_0)-1)+\varepsilon$. The chosen-place group order gives
$$
 |\iota(\mathcal R_p(\tau^j,\delta)^{-1})|_\ell
 \le \ell^{E_x(\ell)},\qquad E_x(\ell)=C_x+\varepsilon .
$$

The same $E_x(\ell)$ bounds the auxiliary loss and each transferred Selmer length at $x$. [12] [13]

For the projection at $x$, set
$$
 u_x(\ell)=\bigl(\mathrm{clearingBound}(D_x,\ell)+v_\ell(H_x)\bigr)\log\ell,
$$
where $\mathrm{clearingBound}$ is the source's loss per dimension and unit of rank and $H_x$ is the number of standard torus classes at the chosen level of $D_x$. The source's two denominator lemmas give a clearing operator on the good lift image of dimension $d_{x,j}$ with determinant norm at least $\exp(-d_{x,j} r_x u_x(\ell))$, and the bound $\exp(u_x(\ell))$ for the norm of the projected rank-one pairing of two test forms. The test forms are integral at the coefficient place and satisfy the source's orthogonality condition against false lifts. For every finite set of rational primes $\mathcal S$ the bounds are
$$
 \sum_{\ell\in\mathcal S}u_x(\ell)\le \frac{f(xb)L^3}{m k_x},\qquad
 \sum_{\ell\in\mathcal S}E_x(\ell)\log\ell\le x_1,\qquad k_x=r_x+1-m.
 \tag{6}
$$

Consequently the family $\theta(\ell,\iota)=\tau_{\ell,\iota}$ is regular in the source's sense for each $D_x$. The period height argument can use that family with the ranks and budgets at each cutoff. [14]

### Determinant scalars

Let $h_x$ be the complex dimension of the target forms at $x$. Write $\mathcal L_x=f(xb)L^4$ for the length allowance and $\mathcal M_x$ for the source's main amount, $m k_x$ times the sum over infinite places of the logarithmic jet size less the guaranteed prime-sum divisibility at that place. With $\kappa_x(\sigma)$ the weight of the place $\sigma$, this is
$$
 \mathcal M_x=m k_x\sum_{\sigma}
 \left(
 \log(\kappa_x(\sigma)!)+\kappa_x(\sigma)\log(M_0/\Omega_E)
 -\sum_{n\le xb}\Lambda(n)(1-(n/d))
       [\kappa_x(\sigma)/n-\kappa_x(\sigma_{-n}\sigma)]_+
 \right).
$$

Here $\sigma_{-n}$ denotes the place labelled by $-n\bmod q_1$ when $n$ is prime to $q_1$, and the identity place otherwise. The normalization is $\Omega_E=(2\pi/\operatorname{rd}_E)\exp(\gamma_{\mathrm E}-\Re L'(1,\chi_{-d})/L(1,\chi_{-d}))$, with Euler's constant $\gamma_{\mathrm E}$ and the quadratic Dirichlet character $\chi_{-d}$ of $K_d$. [15]

For $h_x>0$, choose the source's auxiliary clearing scalars $\gamma_{x,\xi}\ne0$, with $\gamma_{x,1}=1$. The auxiliary forms span the target and their lifted vectors multiplied by $\gamma_{x,\xi}$ are integral at every coefficient place prime to the modulus of $\xi$. Write $Z_x(\xi)$ for the determinant of the Gram operator of the injective chain lift on the target in the source's metric. Define
$$
 t_x(\xi)=|\gamma_{x,\xi}|^{-2},\qquad
 z_x(\xi)=Z_x(1)/Z_x(\xi),\qquad
 B_{x,c}(\xi)=t_x(\xi)^c z_x(\xi)
 \quad (0\le c\le h_x).
$$

Here $c$ is an integer counting auxiliary columns in a completed basis. The source's auxiliary and chain height estimates along $\theta$ bound the scalar families $t_x$ and $z_x$ by $b$ and $h_x(b+\mathcal L_x-\mathcal M_x)$, respectively. [15]

For algebraicity at a fixed twist $\xi$, complete first the empty family and then a singleton consisting of one nonzero short integral Poincaré image. The published spanning bound in positive target dimension and the span of short integral source forms supply that image. The one-translate index bound supplies a uniform clearing loss for it at each rational prime for every allowed embedding and twist. Both completions use the fixed auxiliary system, with $h_x$ and $h_x-1$ auxiliary columns. At any prime $\ell$ coprime to the modulus, the paired finite-place Gram bound applies at $\iota$ and at $\iota$ composed with complex conjugation. If $G_c(\xi)$ is the lifted Gram determinant for the completion with $c$ auxiliary columns, the bound gives a uniform norm bound on $(|\gamma_{x,\xi}|^2)^c G_c(\xi)$ under all such field isomorphisms at $\ell$. Hence this number is algebraic by the source's one-prime algebraicity criterion. The same applies to $G_c(1)$. The Gram identity cancels the source basis determinant within each quotient, yielding the algebraic number $G_c(1)/((|\gamma_{x,\xi}|^2)^cG_c(\xi))=t_x(\xi)^c z_x(\xi)$. The quotient of the two resulting numbers is $t_x(\xi)$, and division by its power recovers $z_x(\xi)$. If $h_x=0$, the chain determinant is the empty determinant $1$, and the sole scalar $B_{x,0}(\xi)$ is $1$. The two-completion argument is used only for $h_x>0$. [16]

### Finite selection and signed degree

For each of the two height bounds at each positive-dimensional cutoff fix the source's witnesses $(A,\alpha,u)$. Here $A\ne0$ is a multiplier, $\log|\sigma A|\le\alpha$ for every complex automorphism $\sigma$, and at $(\ell,\iota)$ the product of $A$ and the selected scalar has norm at most $\ell^{u(\ell)}$. The nonnegative $u(\ell)$ satisfy $\alpha+\sum_{\ell\in\mathcal S}u(\ell)\log\ell\le C$ for every finite prime set $\mathcal S$, with $C$ the relevant scalar height bound. The multipliers are algebraic because their orbits under complex automorphisms are bounded. Indeed a transcendental element can be sent to arbitrarily large multiples of itself by extending a map of transcendence bases. Choose a number field containing the multipliers. Let $\mathcal S_0$ be the rational primes below their denominator supports. Off $\mathcal S_0$ the trivial twist serves all tests, since its modulus norm and its scalar values are $1$. [17]

At each $\ell\in\mathcal S_0$, the places of $\overline{\mathbb Q}$ over $\ell$ form a compact inverse limit of finite place sets. Every such place comes from an isomorphism $\iota$ as above, by extending compatible embeddings along finite subfields and then extending the embedding of $\overline{\mathbb Q}$. For a candidate $\xi$ from $\theta$, test that its modulus is prime to $\ell$ and that both scalar inequalities hold for every positive-dimensional cutoff. The passing set is clopen, since the finitely many algebraic products lie in a finite number field. The simultaneous family covers the inverse limit, so compactness gives a finite subcover. Take the union of the chosen twists over $\mathcal S_0$ and include $1$. In a single number field $F$ containing the multipliers and all scalar values of this menu, every test depends only on the place $w$ of $F$. Choose one passing $\xi_w$ for each finite $w$, taking $1$ above primes outside $\mathcal S_0$. This selection preserves the exact scalar height witnesses for the block. [17]

Define the fractional ideal $J_{x,c}$ in $F$ by giving it order $\operatorname{ord}_w B_{x,c}(\xi_w)$ at each finite $w$, where $\operatorname{ord}_w$ assigns order one to a uniformizer. Normalize $|\,\cdot\,|_w$ by $|\ell|_w=\ell^{-1}$. The normalized log ideal norm is the negative sum of $\log|B_{x,c}(\xi_w)|_w$ with weights $e_wf_w/[F:\mathbb Q]$, where $e_w$ and $f_w$ are the ramification and residue degrees over $\ell$. The weights sum to one over each $\ell$. Combine the witness for $t_x$ to power $c$ with that for $z_x$. For the combined witness $(A,\alpha,u)$ the local inequalities bound the weighted sum of $\log|A B_{x,c}(\xi_w)|_w$ by $\sum_{\ell\in\mathcal S_0}u(\ell)\log\ell$. The product formula expresses the weighted finite sum of $\log|A|_w$ as the negative archimedean mean of $\log|A|$, which is at least $-\alpha$. Thus the normalized log ideal norm is at least $-\alpha-\sum_{\ell\in\mathcal S_0}u(\ell)\log\ell$. With $\mathrm{Nm}_{F/\mathbb Q}$ the absolute ideal norm extended multiplicatively to fractional ideals, the combined height budget gives
$$
 \frac{\log\mathrm{Nm}_{F/\mathbb Q} J_{x,c}}{[F:\mathbb Q]}
 \ \ge\ h_x(\mathcal M_x-b-\mathcal L_x)-c b
 \qquad(0\le c\le h_x).
 \tag{7}
$$

At dimension zero the ideal for $c=0$ is the unit ideal and (7) is equality. The same $\xi_w$ serves every coordinate, so the degree bounds also add for products of the $J_{x,c}$ with nonnegative integer exponents. This finite selection preserves the scalar inequalities. The Selmer and projection bounds are supplied by the place-indexed regular family. The signed degree bound uses the published congruence, spanning, index and period height results. An independent bound on the determinant orders and a numerical bound on the menu size or on $[F:\mathbb Q]$ remain open.

## 8. Fixed target weights and one completed ideal per rank

Continue with the block and the family $\mathcal D$ of §§1–2. We construct admissible data on a common divisor mesh. Within each field, the weights and the heavy set are fixed throughout the block. The lower lift data and the completed determinant scalar are fixed on each rank interval. The estimates below use the released short-image theorem and the scalar heights of §7.

### The mesh and the exact-grid obstruction

For a given rank $R$, the cutoffs of rank $R$ are the integers in the block satisfying $R/3<x^5\le R$. There are at most eight nonempty intervals, since $5\log x/\log3$ varies over a range of length less than $7$. Mark the two endpoints of each interval, counting a singleton once.

Matomäki and Radziwiłł's unconditional Corollary 1 gives a $u^\varepsilon$-smooth integer in $[u,u+C(\varepsilon)\sqrt u]$ for every sufficiently large $u$ at each fixed $\varepsilon>0$. For $\varepsilon=1/j$, $j\ge2$, choose a length constant $C_j$ and onset $U_j$. Choose strictly increasing thresholds $X_j\ge\max\{4U_j,e^{j^2},(C_j+3)^j\}$. At large $X$ take $j=\max\{i:X_i\le X\}$ and $Y=\lceil X^{1/j}\rceil$. Then $j\to\infty$, $Y=X^{o(1)}$, and $C_j+3\le X^{1/j}$. [18]

Let $H_X$ be the least common multiple of the marked endpoints and $\prod_{p\le Y}p^{\lfloor\log X/\log p\rfloor}$. Every $Y$-smooth integer up to $X$ divides this product, and $\log H_X\le(\pi(Y)+16)\log X=X^{o(1)}$. Use all divisors of $H_X$ in the block as nodes. If consecutive nodes $u<v$ of the same rank had gap greater than $1+C_j\sqrt X$, the interval from $u+1$ given by Corollary 1 would lie strictly between them and supply another node. Thus the maximum gap $G$ within a rank is $O(X^{1/2+o(1)})$. Each fourth power is bracketed within its own rank, with an exact node serving as both endpoints when appropriate. Neither the field nor the prime-sum values enter this selection.

At an exact cutoff, admissibility forces the light weight $c=xb/x_1$ to be a multiple of $q_1x$. For each prime $X^{1/4}/\sqrt2<p\le X^{1/4}$, the block contains $p^4$, so its assigned $c$ is divisible by $p^4$. If $\mathcal C$ is the set of distinct light weights used at these cutoffs, the product over $\mathcal C$ is divisible by the product of these fourth powers, even when a weight is reused. By the prime number theorem,

$$
 \#\mathcal C\max_{c\in\mathcal C}\log c
 \ \ge\ 4\sum_{X^{1/4}/\sqrt2<p\le X^{1/4}}\log p
 \ =\ (4-2\sqrt2+o(1))X^{1/4}. \tag{8}
$$

The full admissible scale has $\log c\le\log b\le x^{1/100}\le X^{1/100}$, even if $b$ varies. It follows that $\#\mathcal C\gg X^{6/25}$. At subpower logarithmic scale $\max\log b=X^{o(1)}$, the lower bound is $X^{1/4-o(1)}$. [4]

### Common weights and primes

Use $W,V,f,T_0$ from §2 and $t=\lceil T_0/V^6\rceil$ heavy labels supplied at $r(X)$. Under the identification with $(\mathbb Z/q_1)^\times$, the sparse-label test is the same in all fields. Use the same labels, and put $\eta=t/f=o(1)$. Since $d$ is coprime to $q_1$, the two fields $K_d$ and $\mathbb Q(\zeta_{q_1})$ have coprime discriminants. With coprime discriminants the products of the two integral bases form an integral basis of the compositum. The discriminant formula for this basis gives $\operatorname{rd}(E_d)=\operatorname{rd}(\mathbb Q(\zeta_{q_1}))\sqrt d$. With $d_*=\min\mathcal D$, choose

$$
 B_d^* =e^W\left(\frac{\operatorname{rd}(E_d)}
                        {\operatorname{rd}(E_{d_*})}\right)^{(m-1)/(m(1-\eta))},
 \qquad B_d=\lceil B_d^*\rceil. \tag{9}
$$

Uniformly $\log B_d=W+O(\log(2D)+1)$ and $0\le\log(B_d/B_d^*)\le e^{-W}$. Let $K_X=q_1H_X\prod_{d\in\mathcal D}B_d$, let $L_0=\max\{(2W)^6,2\log(2K_X)\}$, and take the least multiple $b$ of $K_X$ at least $e^{L_0}$. Then $L=\log b=L_0+o(1)=X^{o(1)}$, since $\log K_X\le\log q_1+\log H_X+O(D(W+\log(2D)+1))=X^{o(1)}$ and $K_Xe^{-L_0}=o(1)$. At a node $x$ set

$$
 x_{1,d}(x)=B_dx,\qquad a=xb,\qquad
 \kappa(\tau)=
 \begin{cases}
 b & \tau\in\Phi_b,\\
 b/B_d & \tau\notin\Phi_b .
 \end{cases} \tag{10}
$$

Indeed $q_1B_dx\mid b$, $a/x_{1,d}(x)=b/B_d$, and both weights are positive multiples of $q_1$. Since $W\gg y+\log(2D)$ and $W\le\log x_{1,d}(x)\le2W$ eventually, the three bounds involving $x_1$ in §2 follow from $L\ge(2W)^6$ and $W/y\to\infty$. Also $100\log L\le\log x$ by $L=X^{o(1)}$, and $\log L\ge10^{12}C_*$ by the choice of $W$. The heavy quota is $tL\ge T_0$. The rank, tower and sparsity checks are those of §2. These choices use the general admissible data fields. [4] [5]

Choose $p_0,p_1$ with their norm generators by §3, using this $b$. The lower endpoint (2) now equals

$$
 \lambda_d=m\bigl(L-(1-\eta)\log B_d\bigr)
           +(m-1)\log\!\left(\frac{M_0\operatorname{rd}(E_d)}{2\pi}\right)
           -\frac{15}{2}L.
$$

Replacing $B_d$ by $B_d^*$ gives the same $z$ in all fields by (9). Since $W\gg y$, we have $0\le z-\lambda_d\le m e^{-W}=o(1)$. The level bound of §4 gives $\lambda_d\ge mL$, so §3 supplies a prime $P\equiv1\bmod\mathcal M$ in $(e^z,2e^z]$. It exceeds $b^{11}$ and satisfies $0\le\log P-\lambda_d\le\log2+o(1)<\sqrt L$ for every field. The Gaussian norm generator of §4 serves throughout. [7] [8]

### The common lower chain and the completed ideal

Fix $d$ and a rank $R$ and write $B=B_d$. The target parameter and the lift weights $\kappa_j(\tau)=\kappa(\tau)+(2j+1)R^8$ are constant. Use common frames, lattices, splittings and characters for the lower $Y$-chain, with the same Weil and CM normalizations. The good-type idempotent sums the same finite residue idempotents over good degree-$R$ tuples at the principal primes. For each twist the lower kernels use the same vacuum and inclusion data at the same places. The upper column count at height one enters the lower diagrams at height zero, where the minor is the empty determinant $1$. Removing those columns preserves the tableau polynomials, their integral span, the Fock pairing and the hook numbers. All positive-height lower columns are common. This identifies the lower chain $\Theta_\xi$, integral target gauges, target dimension $D_R>0$ and ratio $Z(1)/Z(\xi)$ in common realizations. The long order $a=xb$ still enters the upper $X$-chain, its first row, the branching exponent and the gains of the normalized Poincaré maps. The short columns and their index budgets can accordingly vary with $x$. [16] [19] [20]

The single-lift descent pairs and comparison compressions are likewise common for a specified twist. At lift $j$, if $W_{j,\theta}$ is the good lift image, the comparison uses the compression $K_{j,\theta}=P_{W_{j,\theta}}U_{j,\theta}|_{W_{j,\theta}}$ of the source's gluing operator with its adjoint, including the class weights and metric. With $C_j(\theta)=\det K_{j,\theta}$ and $\rho_j(\theta)$ the twisted-to-untwisted Hecke product, the single-lift volume ratio is $C_j(\theta)C_j(1)^{-1}\rho_j(\theta)^{-D_R}$. In the chain formula these ratios occur at $\theta=\xi^j$ for the same $\xi$, with the quotient ratios from the intervening lifts. The auxiliary factor uses the turn ratios. The modulus-norm powers in these identities, including rational powers, are units at $\ell\nmid Q_\xi$, where $Q_\xi=\operatorname{Nm}Q(\xi)$. The compression contributes the signed difference of its determinant orders, including the order of $C_j(1)$, which can have either sign. [14] [15] [21]

The amount $\mathcal M_x$ in §7 is a common number $M_R=mk(J-\Sigma)$ with $k=R+1-m$, where $J$ is the sum of the factorial and normalization terms and $\Sigma$ the total prime sum at the target weights. For any order $0\le y'\le b$, the summand at $\nu\ge B$ vanishes because $y'/\nu\le b/B\le\kappa(\sigma_{-\nu}\sigma)$. As $a>B$ at all nodes, the short prime sum has the exact common expression

$$
 \sum_{1\le\nu<B}\Lambda(\nu)(1-(\nu/d))
       [y'/\nu-\kappa(\sigma_{-\nu}\sigma)]_+ .
$$

This uses the same place convention as §7, including its fallback. The local derivative sums at the target weights have support at prime powers below $B$. The sum at the long order $a$ can extend up to $Bx$ and gives the varying signed remainder $T_x$ of §6. [15] [20]

Put $c_R=\lfloor4D_R/b^2\rfloor$ and $h_R=D_R-c_R>0$. The source's short-image bound gives at least $(1-4/b^2)D_R$ independent images from a set of translates whose size times the ramified source dimension is at most $5D_R\log(1+2b^2)$. The short integral source forms span that source. Keep exactly $h_R$ independent short columns at each node. Their lifted squared norms under every conjugation are bounded by $\exp(M_R-mT_x+\mathcal L_x)$, with $\mathcal L_x=f(xb)L^4$. The index theorem applies to every retained family from those translates and gives

$$
 \Delta_x\le 10D_R\log(1+2b^2)\,f(xb)L^3.
$$

At the first node $x_*$ of the rank interval, choose the source's auxiliary spanning family and its nonzero clearing factors $\gamma_\xi$, with $\gamma_1=1$. The lifts $\gamma_\xi\Theta_\xi z$ of members $z$ of this family are integral at every coefficient embedding eligible for $\xi$. The common lower realization lets the same family complete the $h_R$ short columns at each node by $c_R$ auxiliary columns, with squared norms at the trivial twist bounded under every conjugation by $\exp(2(Bx_*)^2b^2)$. The selected columns can vary with the node. [15] [16]

For a finite menu $\mathcal T$ of twists containing $1$, form $A_R(\xi)=(\gamma_\xi\overline{\gamma_\xi})^{-c_R}Z(1)/Z(\xi)$. The paired Gram argument of §7 at the anchor gives algebraicity. In a number field $F$ containing the menu's scalar values define

$$
 I_{d,R}=\prod_{w\ {\rm finite}}\mathfrak p_w^{k_w},
 \quad k_w=\max_{\substack{\xi\in\mathcal T\\ \ell(w)\nmid Q_\xi}}
                   \operatorname{ord}_w A_R(\xi),
 \quad \deg I_{d,R}=\frac{\log\operatorname{Nm} I_{d,R}}{[F:\mathbb Q]}. \tag{11}
$$

Here $\ell(w)$ is the rational prime below $w$ and $\operatorname{ord}_w$ is uniformizer order. The trivial twist ensures $k_w\ge0$, and the finite menu gives finite support. Relative ramification scales the orders and the local-degree weights over an original place sum to its original weight, so the degree is unchanged under field extension. The maximum uses one eligible twist for the entire scalar. In particular a product of these completed scalars at several nodes of the same rank, with nonnegative integer multiplicities, is a power of $A_R$. Its degree is the degree in (11) times the sum of those multiplicities.

### Upper comparison and the prime-count criterion

For a completion at node $x$ let $G_x(\xi)$ be the Gram determinant of its lifted basis. The Gram identity gives

$$
 G_x(1)=\bigl((\gamma_\xi\overline{\gamma_\xi})^{c_R}G_x(\xi)\bigr) A_R(\xi).
$$

The index witness gives a nonnegative loss $e_\ell(x)$ with $\sum_\ell e_\ell(x)\log\ell\le\Delta_x$. At a coefficient embedding $\iota$ over $\ell$ and at $\iota\circ\mathrm{conj}$ use the short-column clearing matrices of determinant valuation at most $e_\ell(x)$, appending $\gamma_\xi$ on the auxiliary columns at both embeddings. The target pairing on the two integral families is integral for the same eligible twist. Thus the parenthesized factor has $\ell$-adic norm at most $\ell^{2e_\ell(x)}$. In particular $G_x(1)$ is algebraic by the one-prime criterion of §7. In the rational untwisted metric, Hadamard's inequality bounds the squared volume of the conjugated columns under any complex automorphism $\sigma$. The actual conjugate $\sigma G_x(1)$ pairs the columns transformed by $\sigma$ with those transformed by $\mathrm{conj}\circ\sigma\circ\mathrm{conj}$. Cauchy–Schwarz on exterior products bounds its log absolute value by $h_R(M_R-mT_x+\mathcal L_x)+2c_R(Bx_*)^2b^2$. [16] [21]

At each finite $w$ use a maximizing twist in (11). With the absolute value normalized by $|\ell|_w=\ell^{-1}$, the local bound on $\log|G_x(1)|_w$ is $2e_\ell(x)\log\ell-k_w\log\ell/e(w/\ell)$, where $e(w/\ell)$ is the ramification index. The weights $[F_w:\mathbb Q_\ell]/[F:\mathbb Q]$ sum to one over each $\ell$. Enlarge $F$ to include $G_x(1)$ and use its product formula with the archimedean bound. This yields the completed upper inequality

$$
 h_R m T_x\ \le\ h_R M_R-\deg I_{d,R}
             +h_R\mathcal L_x+2\Delta_x+2c_R(Bx_*)^2b^2. \tag{12}
$$

In particular $\Delta_x/h_R=O(\mathcal L_x)$ and $c_R(Bx_*)^2b^2/h_R=O((Bx_*)^2)$. The last bound is $O(\mathcal L_x)$ since $(Bx_*)^{10^6}\le b$. By §6 the two remainders $R_{q,d}(Bx)$ and $R_{1,d}(Bx)$ are each $O_q(X^{-2})$, since $\log(Bx)\ge W$. Use the signed identity of §6 with $t$ fixed and $T_0/t\ll V^6$. Put

$$
 \mathcal E_{d,R}=\frac{[h_R M_R-\deg I_{d,R}]_+}{h_R Xbt}.
$$

Using $X/x\le4$ in (12) gives at every node of rank $R$

$$
 [R_{q,d}(x)]_+\ \ll_q\ m^{-1}
                  \bigl(\mathcal E_{d,R}+V^6 L^4+1\bigr). \tag{13}
$$

If $u<v$ bracket a sample $s=n^4$ in its own rank, write $1/s=(1-\lambda)/u+\lambda/v$. The prime-power part of $R_{q,d}$ is convex in the reciprocal variable because all ramp coefficients are nonnegative, including those at powers of $d$. The second derivative of the remaining log term in that variable is bounded below by $-v^2/\varphi(q)$ on $[1/v,1/u]$. The secant bound and convexity of the positive part give

$$
 [R_{q,d}(s)]_+\le (1-\lambda)[R_{q,d}(u)]_++\lambda[R_{q,d}(v)]_+
                  +\frac{(v/u-1)^2}{8\varphi(q)}. \tag{14}
$$

An exact node uses its value with zero interpolation error. For any subset of fourth powers in the block, put $w_R=m^{-1}\sum n$ over the subset of rank $R$. We have $\sum_R w_R\le1$, by $\sum_{n\le X^{1/4}}n\le m$. The total error in (14) is at most $2G^2/(\varphi(q)X^{3/2})=O_q(X^{-1/2+o(1)})$. Equations (13)–(14) give the block mass bound $O_q\bigl(\sum_R w_R\mathcal E_{d,R}+V^6 L^4+1\bigr)$ with that separate interpolation error. [3]

For a fixed $A>1$ use the subset $N\le n\le\lfloor N^A\rfloor$ and a common $D=D_N\to\infty$ with $D_N=o(\log N)$ across its $O_A(\log N)$ blocks. Their $y$ lie in $[4\log N,4A\log N+\log4]$ and $V^6L^4=N^{o(1)}$ uniformly there. With the block dependence of $w_R$ and $\mathcal E_{d,R}$ understood, a sufficient prime-count condition is

$$
 \sum_{\rm blocks}\sum_R w_R\mathcal E_{d,R}\le N^{o(1)}
 \quad\text{uniformly for a set of }D_N^{1-o(1)}
 \text{ eligible primes }d\in(D_N,2D_N]
 \text{ on arbitrarily late windows}. \tag{PC}
$$

Indeed (PC) gives $\log(1+Q_d(N))=o(\log N)$ on those sets. Theorem 1 of Paper 215 v2 assumes $D_N\to\infty$ and $\log\log D_N=o(\log N)$. A zero with $1/2<\sigma<1$ bounds the number of eligible primes with $\log(1+Q_d(N))\le(4A(\sigma-1/2)-\delta)\log N$ by $O_{q,A,\rho,\delta,\epsilon}(D_N^{3(1-\sigma)/(2-\sigma)+\epsilon})$ for any fixed $\delta,\epsilon>0$ and all sufficiently large $N$. Choose $0<\delta<4A(\sigma-1/2)$ and $0<\epsilon<1-3(1-\sigma)/(2-\sigma)$ to contradict (PC), then apply the functional equation. [3]

The released period heights supply (PC) with their hypotheses. The proof of §7 at a single datum uses its admissibility and the imported period inputs. Apply it at the anchor with its chosen $\gamma$ and $c=c_R$. Its finite menu gives $\deg I_{d,R}\ge D_R(M_R-b-\mathcal L_{x_*})-c_R b$ by (7), since the maximum can only improve the selected orders. The source gives $M_R\ge0$. Hence $[h_R M_R-\deg I_{d,R}]_+\le D_R(b+\mathcal L_{x_*})+c_R b$ and $\mathcal E_{d,R}\ll_q V^6L^4+1$. This applies to all eligible fields, for example with $D_N=\log N/\sqrt{\log\log N}$ and the fixed-progression prime number theorem. An independent arithmetic estimate would need to bound the degrees of (11) against the signed targets $h_R M_R$ at the accuracy of (PC). The deduction of RH here retains the short-form, integral vacuum, and period comparison inputs, and the latter use the Selmer, projection and critical-ratio estimates of §7. [2] [3] [15] [22]

## 9. A common signed witness and a field-pair criterion

Paper 190 v1 localizes a Mellin derivative and isolates an untwisted pole, and applies the argument to fixed finite positive sums of character ramps. Paper 215 v2 supplies reciprocal interpolation on fourth powers and the fixed-box zero count for the moving product characters, using Heath-Brown’s quadratic large sieve. Here the pole determines an explicit nonnegative kernel common to the retained fields. The signed mesh comparison then uses that same test on the signed degree deficits. [3] [23]

### The common analytic witness

Suppose $\zeta(\rho)=0$ with $1/2<\beta=\Re\rho<1$. Fix $A>1$, $\delta,\epsilon>0$, and a sequence $D_N\to\infty$ with $\log\log D_N=o(\log N)$, indexed by integers $N\ge2$. Write $K=\lfloor N^A\rfloor$, $R_d=R_{q,d}$, and $\alpha(\beta)=3(1-\beta)/(2-\beta)$. For every sufficiently large $N$ there are integer weights $0\le a_n\le n$ for $N\le n\le K$ such that

$$
 \sum_{n=N}^K a_n R_d(n^4)>N^{4A(\beta-1/2)-\delta} \tag{15}
$$

for every eligible prime $D_N<d\le2D_N$ except a set of size $O_{q,\rho,A,\delta,\epsilon}(D_N^{\alpha(\beta)+\epsilon})$. The weights depend on the untwisted transform and the window. The onset can also depend on the sequence $D_N$.

**Proof.** Put $U=4\log N$. Choose $1/2<\theta_0<\theta<\beta$ and $1<\lambda<A'<A$ so that $4\lambda(\theta-1/2)>4A(\beta-1/2)-\delta$. Choose $\theta_0$ close enough to $\beta$ that $\alpha(\theta_0)<\alpha(\beta)+\epsilon_0/2$ for some $0<\epsilon_0<\min(\epsilon,1-\alpha(\beta))$. The interval $J=[\lambda U,A'U]$ is contained in $[4\log N,4\log K]$ eventually. Set $f_d(v)=e^vR_d(e^v)$ and let $F_d$ be its Laplace transform. Equation (4) of [3] writes $F_d=F_0$ plus the twisted terms, which are divided differences through $1$ of $(-L'/L)(z,\chi(\cdot/d))/z$ for $\chi\bmod q$. The common untwisted $F_0$ has a pole at $\rho$, since the orders of the untwisted $L$-functions at a common zero enter the residue with the same factor $1/(\varphi(q)z(1-z))$. The centering makes the point $1$ regular, and real poles in $[\beta,1)$ have positive residue. [3]

Fix $\sigma>2$ sufficiently large as specified below. Use the nearest-pole choice of [3, §2] for $F_0$. At $z_0=\sigma+it$ a disk of radius $r<\sigma-\theta$ isolates a pole $z_*$ at distance $a<r$. In the displaced case the disk of radius $r$ at $\sigma$ is pole-free. In the real case $t=0$ and the isolated pole has positive residue. For the choice, let $b_0$ be the minimum of $\sigma-\theta$ and the distance from $\sigma$ to the poles. A pole with real part greater than $\sigma-b_0$ admits a displacement that brings the nearest distance below $b_0$, avoiding ties by a small perturbation. Choose $r$ below $b_0$ and the next pole distance. Otherwise $\sigma-b_0\ge\beta$ by the pole at $\rho$, and the nearest pole is the real point $\sigma-b_0$ by equality of its horizontal and total distances. In either case the disks lie in $\Re z>\theta$. [3] [23]

Choose a fixed height $T$ covering the disks and a neighborhood of $1$ with two extra units of height. Exclude $d$ for which a primitive character inducing any product $\chi(\cdot/d)$ has a zero in the closed box $\Re z\ge\theta_0$, $|\Im z|\le T$. The bound in [3, §3], with loss $\epsilon_0/2$, gives $O(D_N^{\alpha(\beta)+\epsilon_0})$ exceptions. The retained set $G_N$ is eventually nonempty by the fixed-progression prime number theorem. The local logarithmic-derivative bound in [3, §2] gives $F_d-F_0=O(1+\log(2D_N))$ on the disks, including the removable point at $1$ by the divided-difference bound there. The inducing characters have conductors $hd$ with $h\mid q$, and the finitely many removed Euler factors have no zeros in $\Re z>0$. The same estimate for the limiting constant, with the elementary bound for the prime-power sum, yields $|f_d(v)|\ll(1+\log(2D_N))e^{2v}$ for $v\ge0$. These bounds are uniform over $G_N$. [3]

Take $k+1$ nearest to $(\sigma-2)(\lambda+A')U/2$ and let $b_k=\operatorname{Res}_{z_*}F_0/(z_0-z_*)^{k+1}$ and $\omega_k=\overline{b_k}/|b_k|$. For $\mathcal D_{k,d}(z)=(-1)^k F_d^{(k)}(z)/k!$, Cauchy’s estimate after subtracting the pole gives $\mathcal D_{k,d}(z_0)=b_k+O((1+\log(2D_N))r^{-k})$. In the displaced case $\mathcal D_{k,d}(\sigma)$ obeys the same error bound. In the real case $b_k>0$ and $\omega_k=1$. Since $k\asymp\log N$ and $1+\log(2D_N)=\exp(o(k))$, the error is $o(a^{-k-1})$ uniformly. Thus

$$
 \begin{aligned}
 \mathcal D_{k,d}(\sigma)+\Re\{\omega_k\mathcal D_{k,d}(z_0)\}
 &=\int_0^\infty f_d(v)h_k(v)\,dv\gg a^{-k-1},\\
 h_k(v)&=e^{-\sigma v}\frac{v^k}{k!}\bigl(1+\Re\{\omega_k e^{-itv}\}\bigr)\ge0 .
 \end{aligned}
$$

The gamma law of shape $k+1$ and rate $\sigma-2$ has tail probability outside $J$ of order $O(e^{-ck})$. Indeed, exponential Markov bounds give rate $w-1-\log w$ at the limiting endpoint-to-mean ratios $2\lambda/(\lambda+A')$ and $2A'/(\lambda+A')$. Take $c>0$ smaller than both rates and choose $\sigma$ at the outset so that $(\sigma-2)e^c>\sigma-\theta$. The **absolute** contribution outside $J$ is $O((1+\log(2D_N))(\sigma-2)^{-k-1}e^{-ck})=o(a^{-k-1})$. Define

$$
 B_N=2(\sigma-\theta)^{-k}e^{-(\theta-1/2)\lambda U},
 \qquad H_N(v)=\mathbf1_J(v)e^{v/2}h_k(v)/B_N.
$$

The exponential series gives $v^k/k!\le(\sigma-\theta)^{-k}e^{(\sigma-\theta)v}$, so $0\le H_N\le1$. The change of variables $x=e^v$ now gives

$$
 \int_{N^4}^{K^4} H_N(\log x) R_d(x)\,\frac{dx}{\sqrt x}
 \gg \left(\frac{\sigma-\theta}{a}\right)^k e^{(\theta-1/2)\lambda U}. \tag{16}
$$

Let $l_n(x)$ be the nonnegative basis functions of interpolation in $1/x$ at $n^4$. On a cell $[n^4,(n+1)^4]$, the same convex-ramp and logarithm estimate as in (14), applied before taking positive parts, gives $R_d(x)\le\sum_j l_j(x)R_d(j^4)+O_q(n^{-2})$. Take

$$
 a_n=\frac18\int_{N^4}^{K^4}H_N(\log x)l_n(x)\,\frac{dx}{\sqrt x}.
$$

The cell has measure $4n+2$ for $dx/\sqrt x$, and the cells incident to an interior node have total measure $8n$. At an endpoint there is just one cell of measure at most $8n$, so $0\le a_n\le n$. Integration gives eight times the signed sum as an upper bound for (16) up to $O_{q,A}(\log N)$. The strict exponent margin and $\theta>1/2$ give (15), including when the exponent in (15) is nonpositive. This proves the common witness statement. [3]

To obtain the stated integers, round the cumulative weights down and take successive differences. Since $n$ is an integer and the initial weights belong to $[0,n]$, the rounded weights do too. Every prefix sum changes by less than one. On each side of a breakpoint the prime sum has derivative

$$
 R_d'(x)=x^{-2}\!sum_{j\le x,\ j\equiv1\ (q)}\Lambda(j)(1-(j/d))
            -\frac1{\varphi(q)x}=O_q(1/x)
$$

by Chebyshev's bound. The continuous remainder therefore has total variation $O_{q,A}(\log N)$ over the window. At $K^4$ its absolute value is $O_{q,A}(1+\log N+\log(2D_N))$ on the retained fields, using the bound on the centering constant and partial summation. Abel summation bounds the error of the rounding by this same quantity, which is $N^{o(1)}$. The strict positive exponent margin in (16) absorbs it. The rounding depends only on the original weights.

If $\beta>3/4$, one common subset with the original weights $n$ already satisfies (15). Apply the same cumulative rounding to the initial $a_n/n\in[0,1]$ to obtain indicators and test them against $nR_d(n^4)$. The endpoint and total variation of these weighted samples cost at most $O_{q,A}(K(1+\log N+\log(2D_N)))=N^{A+o(1)}$. In obtaining (16) first choose a loss smaller than both $\delta$ and $4A(\beta-1/2)-A$. The margin absorbs the cost at every retained prime.

For every probability vector $p$ on $G_N$, (15) gives $\sum_n n[\sum_d p_d R_d(n^4)]_+>N^{4A(\beta-1/2)-\delta}$. Finite minimax identifies the minimum of this mixed positive mass over $p$ with the maximum, over $0\le a_n\le n$, of the smallest signed sum over $G_N$. The maximum for fixed $p$ is coordinatewise. An optimal vertex of the linear program in $a_n$ and a common lower bound on the field sums has at most $|G_N|-1$ fractional coordinates $0<a_n<n$. If $f$ coordinates are fractional at a vertex, they and the lower-bound variable need $f+1$ independent active field constraints, of which there are at most $|G_N|$. The explicit analytic weights need only the untwisted data, while an optimal vertex can depend on $G_N$ and its values.

### Signed degrees and field averages

Now fix $A>1$ and let $D_N\to\infty$ with $D_N=o(\log N)$. Use the common data of §8 on each block meeting $N\le n\le K$ and write $i=(X,R)$ for an occupied block and rank. The assignment of a sample to $i$ is common across fields. In each $d,i$ choose a finite menu containing $1$ and use the completed ideal $I_{d,i}$ of (11) with its full clearing factor and modulus eligibility. The menus may depend on $N,d,i$. With $b,t,m$ taken from the block of $i$, define

$$
 z_{d,i}=\frac{M_{d,i}-\deg I_{d,i}/h_{d,i}}{Xbt},
 \qquad c_i=\frac{X}{m}\sum_{n^4\in i}\frac{n}{n^4}, \tag{17}
$$

where $M_{d,i},h_{d,i}$ are the field’s own main amount and retained dimension. All sample sums are restricted to $N\le n\le K$. At a node $u$ of $i$, (12) and the signed identity of §6 give

$$
 R_d(u)\le\frac{X}{mu}z_{d,i}+O_q\!\left(\frac{1+V^6L^4}{m}\right).
$$

The error uses the translate, auxiliary and tail estimates of §8. At a bracketed sample the reciprocal chord sends the leading coefficient to $X/(mn^4)$ exactly, also for negative $z_{d,i}$. The curvature error is $O_q((G/X)^2)$ with $G$ from §8. Hence for every common choice of $0\le a_n\le n$,

$$
 \sum_n a_nR_d(n^4)\le\sum_i w_i z_{d,i}+N^{o(1)},
 \qquad w_i=\frac X m\sum_{n^4\in i}\frac{a_n}{n^4},
 \qquad 0\le w_i\le c_i . \tag{18}
$$

The error is uniform in the fields, menus and weights. In each block $\sum n\le m$, $\sum_i c_i\le4$, and the curvature charge is $O_q(X^{-1/2+o(1)})$. There are $O_A(\log N)$ blocks and $V^6L^4=N^{o(1)}$ uniformly. Every $w$ in this box is realized by taking $a_n/n=w_i/c_i$ on each occupied $i$.

For the integral sample weights in (15), the $w_i$ in (18) are rational. Take a positive integer $P_*$ clearing every $w_i/(Xbt h_{d,i})$ in this finite window. For a given $d$ extend all its ideals to one coefficient field. The product of $I_{d,i}$ to powers $P_*w_i/(Xbt h_{d,i})$ has normalized degree divided by $P_*$ equal to the ideal contribution in (18). Each factor retains the local choices entering (11).

Let $\mathcal D_N$ be all eligible primes in $(D_N,2D_N]$, put $H=|\mathcal D_N|$, and take an integer $0\le r<H$. Write $\operatorname{ord}_{r+1}$ for the $(r+1)$-st smallest value with multiplicity. If $\Delta(G)$ denotes the probability simplex on $G$, then

$$
 \begin{aligned}
 V_r(N)&=\max_{0\le w_i\le c_i}
   \operatorname{ord}_{r+1}\left(\sum_i w_i z_{d,i}:d\in\mathcal D_N\right)\\
 &=\max_{\substack{G\subset\mathcal D_N\\ |G|=H-r}}
     \min_{p\in\Delta(G)}\sum_i c_i\left[\sum_{d\in G}p_d z_{d,i}\right]_+ .
 \end{aligned} \tag{19}
$$

For fixed $w$, the order statistic is the largest minimum over subsets of size $H-r$. The two maxima commute. On each subset apply bilinear minimax on the box and the simplex and maximize each $w_i$ separately. The minimizing distribution may depend on $G$ and $N$ and is common to all the ranks of the window.

With $r=\lfloor H/\log(2H)\rfloor$, the fixed-progression prime number theorem gives $H\asymp_q D_N/\log D_N$, so $r$ eventually exceeds the exception count of (15) for any fixed $\beta>1/2$ and $0<\epsilon<1-\alpha(\beta)$. The witness in (15) and (18) gives $V_r(N)\ge N^{4A(\beta-1/2)-\delta}-N^{o(1)}$. Thus a bound $V_r(N)\le N^{o(1)}$ along an unbounded sequence of windows, for the menu choices in (17), would imply RH by taking $0<\delta<4A(\beta-1/2)$ and using the functional equation.

A sufficient condition with disjoint pairs is as follows. For some fixed $A>1$ and $D_N\to\infty$ with $D_N=o(\log N)$, suppose on an unbounded sequence of windows there are choices of the menus in (17) and at least $D_N^{1-\eta_N}$ disjoint pairs $\{d,e\}\subset\mathcal D_N$, where $\eta_N\to0$. Suppose the pairs all satisfy

$$
 \sum_i c_i\left[(z_{d,i}+z_{e,i})/2\right]_+\le N^{\nu_N},
 \qquad \nu_N\to0. \tag{20}
$$

For a putative right-half zero choose $\delta,\epsilon$ as above. Each exceptional field from (15) can meet at most one pair, and $O(D_N^{\alpha(\beta)+\epsilon})=o(D_N^{1-\eta_N})$. On a pair untouched by the exceptions the common signed sum averaged over its two fields exceeds $N^{4A(\beta-1/2)-\delta}$ by (15). Averaging (18) at the same weights and using $0\le w_i\le c_i$ and (20) bounds that average by $N^{o(1)}$. This contradiction proves the implication. With two unit-capacity ranks, the vectors $(Z,-Z)$ and $(-Z,Z)$ for $Z>0$ illustrate how the positive part of the average can vanish while both individual positive masses are $Z$.

The anchor heights at the end of §8 give $[z_{d,i}]_+\ll_q 1+V^6L^4$ for all eligible fields under the imported period comparison. Together with $\sum_i c_i=O_A(\log N)$ and the fixed-progression prime count, this supplies both the bound for $V_r$ and the bound for $\lfloor H/2\rfloor$ disjoint pairs. An independent subpower estimate for the signed averages of genuine completed degrees at the accuracy of these criteria remains open. [2] [3]

## 10. Complementary pairs and the mass normalization

Let $D=D_N\to\infty$ with $D_N=o(\log N)$ on the fourth-power windows of §9. At an occupied rank interval $i=(X,R)$ of §8, use $X=m^2$, $k=R+1-m$, $L=\log b$, $f=\varphi(q_1)$, and the common heavy labels $T$ of size $t$. The heavy weight is $b$ and the light weight in field $j$ is $b/B_j$ as in (9)–(10). Write $M_j=M_{j,i}$ for the main amount and $I_j=I_{j,i}$ for the completed ideal (11). Field indices $d,e$ refer to distinct eligible primes in $(D,2D]$, ordered as $d<e$ when comparing dimensions.

### Complementary prime pairs

There is an effective absolute $c>0$ such that, for all sufficiently large $D$, there are $D^{1-o(1)}$ disjoint eligible pairs with opposite quadratic signs at every prime in

$$
 \mathcal S_Y=\{p\le Y:p\text{ prime},\ p\nmid q\},\qquad Y=c\sqrt{\log D}.

$$

To prescribe the signs of the first member, choose a nonzero residue $u_p\bmod p$ with $(-u_p/p)$ equal to the prescribed sign, and choose $v_p$ with the opposite sign. CRT gives two reduced classes $a_+,a_-\bmod Q$, where $Q=q\prod_{p\in\mathcal S_Y}p$. They both reduce to $9239\bmod q$ and are distinct once $\mathcal S_Y$ is nonempty. All primes in $\mathcal S_Y$ are below $D$ eventually.

For effective $a_0,a_1>0$, use the classical explicit formula in the range $\log Q\le a_0\sqrt{\log D}$. Character orthogonality, subtraction at the endpoints, and removal of higher powers give, for a reduced class $a$,

$$
 \sum_{\substack{D<p\le2D\\p\equiv a\bmod Q}}\log p
 =\frac1{\varphi(Q)}\int_D^{2D}(1-\rho(a)u^{\beta-1})\,du
 +O\!\left(D e^{-a_1\sqrt{\log D}}+\log(2Q)\log(2D)+\sqrt D\log^2(2D)\right).
 \tag{21}

$$

The possible term $\rho(a)u^{\beta-1}$ comes from the unique exceptional primitive real character inducing a character modulo $Q$, of conductor $F_\rho\mid Q$ and simple real zero $\beta$. It is omitted if there is no such zero. Its endpoint antiderivative is $\rho(a)u^\beta/\beta$. The displayed error is absolute, since the per-character errors are averaged. The class-number and derivative bounds of §3 give the effective gap $g=1-\beta\gg F_\rho^{-1/2}\log^{-2}(2F_\rho)$. Thus even in the class $\rho(a)=1$ the main term is at least $D(1-e^{-g\log D})/\varphi(Q)$, and in all cases it is

$$
 \gg \frac{D}{\varphi(Q)}\min\!\left(1,\frac{\log D}{\sqrt Q\log^2(2Q)}\right).

$$

With $C_\theta=4\log 2$, the dyadic binomial bound gives $\log Q\le\log q+C_\theta Y$. Take $c=\min(a_0,a_1)/(4C_\theta)$. The modulus range holds eventually, and $\log D/\log^2(2Q)$ is bounded below by a positive constant. The main term is $\gg D/Q^{3/2}$. The first error relative to this bound is $O_q(e^{-(a_1-3C_\theta c/2)\sqrt{\log D}})$, and the other two errors have absolute size $D^{1/2+o(1)}$. Each class therefore supplies $\gg_q D/(Q^{3/2}\log(2D))=D^{1-o(1)}$ primes. Match the lists up to the smaller count. In (15), any one exceptional field removes at most one pair, so for $\epsilon<1-\alpha(\beta)$ the supply still has $D_N^{1-o(1)}$ pairs with both fields retained. [6] [24]

### The paired height and its local terms

Put $\chi_j=(-j/\,\cdot\,)$, $F=\mathbb Q(\sqrt{de})$ and $L_{d,e}=K_dK_e$. Write $\xi$ for the quadratic Hecke character of $L_{d,e}/F$. At each finite prime of $F$, one of $(1+\sqrt{-d})/2,(1+\sqrt{-e})/2$ has order discriminant a unit, so it generates an étale quadratic algebra locally. The finite conductor of $\xi$ is $1$, and both real components are sign characters. For a character $\varphi\bmod q_1$ with primitive inducing character $\psi$ of conductor $h\mid q_1$, set $\theta_\psi=(\psi\circ N_F)\xi$. Every rational prime dividing $q_1$ splits completely in $L_{d,e}$, by the eligible congruence, so the finite conductor of $\theta_\psi$ is $h\mathcal O_F$. Artin induction, or multiplication of the local polynomials, gives

$$
 L_F(s,\theta_\psi)=L(s,\psi\chi_d)L(s,\psi\chi_e).
 \tag{22}

$$

The primitive twists have conductors $hd,he$. At $p=d$ the factor from $\psi\chi_e$ survives and at $p=e$ the factor from $\psi\chi_d$ survives. At primes dividing $q_1$ where $\psi$ is unramified, passing to the imprimitive convention deletes identical factors in the untwisted and twisted terms of each field.

For a unit $u\bmod q_1$ set $g_T(u)=1-|T\cap(-u)^{-1}T|/t$ and extend it by zero at nonunits. Its expansion is $g_T(u)=\sum_{\varphi\bmod q_1} b_\varphi\varphi(u)$ with $\eta=t/f$ and

$$
 b_{\mathbf1}=1-\eta,\qquad
 b_\varphi=-\frac{\varphi(-1)}{ft}\left|\sum_{\tau\in T}\varphi(\tau)\right|^2
 \quad(\varphi\ne\mathbf1),\qquad
 \sum_\varphi |b_\varphi|=2(1-\eta).

$$

Indeed, the overlap is the correlation of the indicator of $T$ translated by $-1$, and the absolute sum follows by orthogonality. Only a heavy source sent to a light place gives a positive summand in $\Sigma_j$ from §8. The fallback at a nonunit sends the source to itself. Thus the exact finite prime sum is

$$
 \frac{\Sigma_j}{bt}
 =\sum_{\nu\le B_j}\Lambda(\nu)(1-\chi_j(\nu))g_T(\nu)(1/\nu-1/B_j).
 \tag{23}

$$

Define $U_\varphi=\operatorname{FP}_{s=1}(-L'/L)(s,\psi)$ and $V_\varphi=(-L_F'/L_F)(1,\theta_\psi)$. Use $\gamma_H$ for the constant term of $\zeta_H'/\zeta_H$ at $1$ after the pole $-1/(s-1)$. Then $U_{\mathbf1}=-\gamma$ and $V_{\mathbf1}=\gamma_F-\gamma_{L_{d,e}}$ by $\zeta_{L_{d,e}}/\zeta_F=L_F(s,\xi)$.

Here is the uniform approximation used to center (23). For a character $\omega$ of modulus $Q'\mid q_1j$, write $\delta_\omega$ for the principal indicator, $\Psi_\omega(u)=\sum_{\nu\le u}\Lambda(\nu)\omega(\nu)$, and $C_\omega=\operatorname{FP}_{s=1}(-L'/L)(s,\omega)$. Partial summation gives

$$
 \sum_{\nu\le B_j}\Lambda(\nu)\omega(\nu)(1/\nu-1/B_j)
 =\delta_\omega(\log B_j-1)+C_\omega
  -\int_{B_j}^{\infty}(\Psi_\omega(u)-\delta_\omega u)\frac{du}{u^2}.

$$

For $U=\log B_j$, the tail is

$$
 O\!\left((1+\sqrt U)e^{-a_1\sqrt U}
    +g_j^{-1}e^{-g_j U}+\log(2Q')(1+U)e^{-U}\right),
 \qquad g_j\gg_q \frac{1}{\sqrt{2D}\log^2(4D)}.

$$

Indeed $\log Q'=O_q(\log X)$ and $U\ge W\gg(\log X)^2$. A real conductor has odd part squarefree and $2$-part at most $8$, so it is at most $8\operatorname{rad}(q)j$ and the gap bound of §3 gives $g_j$. The other two terms integrate the ordinary error and the imprimitive deletion error in (21) before prime-power removal. The tail is $O_{q,C}(X^{-C})$ for every fixed $C>0$ since $\log W\ge8\log V$ and $D=o(\log X)$. The same estimate applies to the primitive $\chi_j$. [6] [24]

Let $A_j=\log(M_0\operatorname{rd}(E_j)/(2\pi))$, $M_0=p_0p_1$, and use bars for averages of the two fields. In the source normalization $\log(M_0/\Omega_{E_j})=A_j-\gamma-(-L'/L)(1,\chi_j)$. The last derivative is $O_q(1+\log B_j)$ by its finite ramp and the Chebyshev bound. In the factorial and normalization sum $J$ of §8, Stirling's formula gives $J/(bt)=L-1+\log(M_0/\Omega_{E_j})+O_q((f/t)L/B_j)$. The error decreases faster than every power of $X$ since $f/t=O_q(V^6)$. Combining (22)–(23), the centering and the endpoint in §8 gives, for $H_{d,e,i}=(M_d+M_e)/(2Xbt)$,

$$
 \begin{aligned}
 H_{d,e,i}
 &=\frac{k}{X}\left(\bar\lambda+\frac{15}{2}L+\bar A\right)
 -\frac{mk}{X}\left[\eta\left(1+\gamma+\frac{\gamma_F-\gamma_{L_{d,e}}}{2}\right)
    +\sum_{\varphi\ne\mathbf1} b_\varphi\left(U_\varphi-\tfrac12 V_\varphi\right)\right]
 +O_{q,C}(X^{-C}).
 \end{aligned} \tag{24}

$$

In fact the principal ramp contributes $(1-\eta)(\log B_j-1)$ before subtraction in $M_j=mk(J-\Sigma_j)$. The $\gamma$ and $\chi_j$ terms from $J$ then combine with the principal logarithmic derivative from $\Sigma_j$ to leave the coefficient $\eta$. The absolute sum of the Fourier coefficients controls all the centering errors. [8] [15] [24]

For a formula in terms of the common $P$, replacing $\bar\lambda$ by $\log P$ in (24) adds exactly $(k/X)(\log P-\bar\lambda)$ to its displayed main expression. This term can be absorbed in $O_{q,C}(X^{-C})$ with a sharper choice of the common prime. For the common real endpoint $z$ of §8, take $\delta=\exp(-(\log X)^2)$ and use the same progression $1\bmod\mathcal M$ in $(e^z,e^z(1+\delta)]$. We have $\log\mathcal M=O_q((1+D)\log X)$ and $z\ge mL$. By §3 the possible exceptional gap is at least $\exp(-O_q(1+D))=X^{-o(1)}$. The exceptional integral over this short interval is therefore $o(\delta e^z/\varphi(\mathcal M))$. The absolute endpoint errors in (21), with $e^z$ in place of $D$, are also $o(\delta e^z/\varphi(\mathcal M))$, since $\sqrt z\gg(\log X)^2$. This gives a prime in the required class with $0\le\log P-\lambda_j\le\delta+m e^{-W}$. Formula (24) with $\bar\lambda$ applies to every common $P$ allowed by §8. [6] [8] [24]

At $p\in\mathcal S_Y$, the paired signs make $p$ inert in $F$. Its degree-two prime splits in $L_{d,e}/F$, since the square of the rational Frobenius in the biquadratic extension is trivial. With $a=\varphi(p)=\psi(p)$, the reciprocal local polynomial in (22) is $1-a^2p^{-2s}$. The coefficient at $p^r$ in its minus logarithmic derivative is zero for odd $r$ and $2a^r\log p$ for even $r$. The average untwisted-minus-twisted coefficient is $a^r\log p$ for odd $r$ and zero for even $r$. In the uncentered ramp of §1 the latter average gives $\log p\,(p^{-r}-x^{-1})_+$ at odd powers $p^r\equiv1\bmod q$, with zero elsewhere at this prime. In (23) the exact average contribution is $\log p\sum_{r\ge1,\ r\ {\rm odd}}g_T(p^r)(p^{-r}-B_{\rm in}^{-1})_+$, with $B_{\rm in}$ the cutoff of the member inert at $p$ in $K_j$.

At $s=1$ the localized terms are $U_{\varphi,p}=a\log p/(p-a)$ and $V_{\varphi,p}=2a^2\log p/(p^2-a^2)$. Every label of $T$ is $-1\bmod q$, so an overlap requires $u\equiv-1\bmod q$. Hence $g_T(p^{2r})=1$, since $4\mid q$ and $p$ is odd. Including the principal Euler–Kronecker term, the entire localized genus contribution in (24) is

$$
 \frac{mk}{2X}\left(-\eta V_{\mathbf1,p}+\sum_{\varphi\ne\mathbf1}b_\varphi V_{\varphi,p}\right)
 =\frac{mk}{X}\log p\sum_{r\ge1}\frac{g_T(p^{2r})-1}{p^{2r}}=0.
 \tag{25}

$$

The full localized Euler contribution to the normalized height is therefore

$$
 \frac{mk}{X}\log p\left[\frac{1-\eta}{p-1}
               -\sum_{\substack{r\ge1\\r\ {\rm odd}}}\frac{g_T(p^r)}{p^r}\right].
 \tag{26}

$$

For instance at $p=13$ the bracket is $1/(13^2-1)-\eta/(13-1)$. These identities concern the Euler factors at the specified primes, with the archimedean terms and level endpoint of (24) kept in place. [24]

### Primes of distinct relative type

Write $E_j=K_j(\zeta_{q_1})$, $F_j=E_j^+$ and $M_2=2^{v_2(q_1)}=16X^{11}$. For $p\nmid q_1de$, the Frobenius in $E_j/\mathbb Q$ is $(\chi_j(p),p\bmod q_1)$ and complex conjugation is $(-1,-1)$. A prime over $p$ is inert in $E_j/F_j$ exactly when the cyclic Frobenius group contains complex conjugation. This happens when $\chi_j(p)=-1$ and $p\bmod q_1$ is $-1$ times an element of odd order. In that case $p\equiv-1\bmod M_2$ by projection to the $2$-group of units modulo $M_2$. All places over $p$ have the same relative type.

At $p\mid q_1$ the split quadratic factor rules out complex conjugation in the decomposition group. At $p=d,e$ the cyclotomic factor is unramified, and reaching $-1\bmod q_1$ by a Frobenius power would require an odd power by reduction modulo $4$, forcing $p\equiv-1\bmod M_2$ again. These two primes are below $M_2-1$ on late blocks. In particular both relative extensions split over every rational prime below $M_2-1$, including the primes through $5R(R+1-m)$. At $p\in\mathcal S_Y$ the order of $p\bmod q_1$ is even, since its image modulo $M_2$ is nontrivial in a $2$-group. The absolute residue degree in both CM fields there is $\operatorname{ord}_{q_1}(p)$.

For a finite evaluation of $M_j/(Xbt)$, use (23) and evaluate $(-L'/L)(1,\chi_j)$ in $\log(M_0/\Omega_{E_j})$ by its smoothed sum at $B_j$ with error $O_{q,C}(X^{-C})$ at any prescribed order. The coefficient $\sum_\tau\kappa_{j,\tau}/(bt)=1+(f-t)/(tB_j)$ of this derivative before normalization is bounded. The weights in (23) have modulus at most two. Thus with $B_*=\max(B_d,B_e)$ the total absolute contribution from rational primes of distinct relative type in these finite sums, in either field, is

$$
 \ll_q\frac{mk}{X}\sum_{\substack{p\le B_*\\p\equiv-1\bmod M_2}}\frac{\log p}{p-1}
 \ll_q\frac{mk}{XM_2}\log^2(2B_*)=X^{-13/2+o(1)}.
 \tag{27}

$$

The second bound follows by summing over all integers $aM_2-1\ge2$ and using the harmonic sum. Here $mk/X=O(X^{9/2})$ and $\log B_*=X^{o(1)}$. This is a height estimate with the other terms, including the discriminant and factorials, retained. [5] [15] [24]

### Principal, good and retained dimensions

The source identifies the good target on $Y_0$ with the good dimension on the standard definite row $W_m$ at rank $R$. Put $G_a=\mathrm{GL}_R(\mathbb F_{p_a})^f$ for $a=0,1$. Both old primes split completely, and the norm generator selects one place in each conjugate pair. On the definite row let $K$ be the standard maximal compact and $K'$ the kernel at both primes, so $K/K'=G_0\times G_1$. Each maximal-level class with finite rational automorphism group $H_x$ has fiber of principal classes $\overline H_x\backslash(G_0\times G_1)$. Reduction is injective on $H_x$ even at either single prime by the one-prime stabilizer theorem. Consequently the principal dimension is the integer

$$
 S_j=|G_0|\,|G_1|\ \dim_{\mathbb C}\mathcal V_j\ \mathcal M_j,
 \qquad \mathcal M_j=\mathrm{mass}(E_j,R)=\sum_{[x]} |H_x|^{-1},
 \tag{28}

$$
where $\mathcal V_j$ is the compact coefficient representation at the target parameter. Every principal class contributes one full coefficient fiber. [19] [25]

Each factor $G_a$ acts freely on the principal classes. Indeed, if an element supported at $p_a$ fixes a class, it comes from a rational automorphism principal at $p_{1-a}$. The one-prime theorem makes that automorphism trivial. Thus every nonidentity element of a factor has trace zero on the principal forms, because it permutes their fibers without fixed points. If $B_{j,a}$ is the action of the marginal bad idempotent and $\delta_{j,a}$ its identity coefficient in $\mathbb C[G_a]$, then $\operatorname{rank} B_{j,a}=\operatorname{tr} B_{j,a}=\delta_{j,a} S_j$ with $0\le\delta_{j,a}\le b^{-8}/2$ by the source's finite-type estimate. The good projector is $(1-B_{j,0})(1-B_{j,1})$. The two bad projectors commute and $\operatorname{tr}(B_{j,0}B_{j,1})$ is the dimension of their common image. In particular the genuine good dimension $D_j$ and the retained dimension $h_j$ in §8 satisfy

$$
 \begin{aligned}
 D_j&=(1-\delta_{j,0}-\delta_{j,1})S_j+\operatorname{tr}(B_{j,0}B_{j,1}),
 & (1-b^{-8})S_j&\le D_j\le S_j,\\
 h_j&=D_j-\lfloor4D_j/b^2\rfloor,
 & (1-4b^{-2})(1-b^{-8})S_j&\le h_j\le S_j .
 \end{aligned} \tag{29}

$$

The intersection term permits overlap of the bad images, as in the finite action on cosets of the diagonal of $C_7\times C_7$. The good-type rule may depend on $j$. [16] [19] [25]

### The mass and Weyl orders

The complex conjugation element has nontrivial projection to both the cyclotomic and quadratic factors of $E_j/\mathbb Q$. Finite inertia projects trivially to at least one factor because their discriminants are coprime. Thus $E_j/F_j$ is unramified at all finite places, and

$$
 \Delta_j=|\operatorname{disc}F_j|
   =|\operatorname{disc}\mathbb Q(\zeta_{q_1})|\,j^{f/2}
   =\operatorname{rd}(E_j)^f.

$$

Let $\eta_j$ be the quadratic character of $E_j/F_j$ and $L_{j,n}(s)=L_{F_j}(s,\eta_j^n)$, so $L_{j,n}=\zeta_{F_j}$ for even $n$. For the standard self-dual definite genus with full unitary automorphisms, the conventional unitary mass formula gives

$$
 \mathcal M_j
 =2\Delta_j^{R^2/2}\prod_{n=1}^R
    \left(\frac{(n-1)!}{(2\pi)^n}\right)^f L_{j,n}(n)
 =2^{1-fR}\prod_{n=1}^R|L_{j,n}(1-n)|.
 \tag{30}

$$

The stabilizers are hyperspecial at every finite place. At a place of norm $Q_v$ the split general linear or inert unitary point count gives the normalized factor $\prod_{n=1}^R(1-\eta_j(v)^n Q_v^{-n})$, including at the unramified dyadic places. The unitary Tamagawa number is $2$. The functional equations give the second expression. The identical archimedean factors cancel across fields. The sum of absolute log contributions from ranks $n\ge2$ is at most $f\sum_{n\ge2}\log\zeta(n)=O(f)$. At rank one, the CM class-number formula gives

$$
 L_{j,1}(1)=\frac{(2\pi)^f}{\sqrt{\Delta_j}}\,
  \frac{h(E_j)}{Q_j\,|\mu(E_j)|\,h(F_j)},\qquad
 Q_j=[\mathcal O_{E_j}^\times:\mu(E_j)\mathcal O_{F_j}^\times]\in\{1,2\}.

$$

Here $h(H)$ is the class number of a field $H$. Minkowski's bound and the ideal count $\#\{\mathfrak a:N\mathfrak a\le B\}\le B^2\zeta_H(2)$ give $\log h(H)\le \log|\operatorname{disc}H|+O([H:\mathbb Q])$. Also $\varphi(|\mu(E_j)|)\le 2f$ bounds $\log|\mu(E_j)|$ by $O(\log(2f))$. The rank-one log is therefore $O(f\log(2q_1D))$ in absolute value. It follows that

$$
 \log(\mathcal M_e/\mathcal M_d)=\frac{fR^2}{4}\log(e/d)+O_q(f\log(2q_1D)).
 \tag{31}

$$

[26]

At each infinite place $v$ the compact Weyl product uses the undoubled Harish-Chandra list with $k-1$ consecutive entries $k/2-1,\ldots,1-k/2$ and $m$ entries $-\kappa_{j,v}-2aR^8$ for $1\le a\le m$. The within-list factors of each group of entries cancel across fields. The other $m(k-1)$ factors have numerators $\kappa_{j,v}+2aR^8+k/2-1-u$ for $0\le u\le k-2$, with common denominators. In their log ratio replacing each numerator by $\kappa_{j,v}$ costs a total $O(fm(k-1)(mR^8+k)/\kappa_{\min})$, where $\kappa_{\min}=\min_{j,v}\kappa_{j,v}$. This is $O_{q,C}(X^{-C})$ for every fixed $C$ by §8. The exact endpoint identity is $\lambda_j=(m/f)\sum_v\log\kappa_{j,v}+(m-1)A_j-15L/2$. It follows that

$$
 \log\frac{\dim\mathcal V_d}{\dim\mathcal V_e}
 = f(k-1)\left(\lambda_d-\lambda_e+\frac{m-1}{2}\log(e/d)\right)+O_{q,C}(X^{-C}).
 \tag{32}

$$

Even the admissible tolerance $|\lambda_d-\lambda_e|\le\sqrt L=X^{o(1)}$ is $o(m\log(e/d))$, since $\log(e/d)\ge1/(2D)$ and $D=o(\log X)$. Thus the compact coefficient dimension is larger for $d<e$. The automorphic counts have the reverse order. Indeed, combining (28)–(32) gives, for $T_j^*=S_j,D_j$, or $h_j$,

$$
 \begin{aligned}
 \log(T_e^*/T_d^*)&=\frac f4\bigl(R^2-2(k-1)(m-1)\bigr)\log(e/d)
       + f(k-1)(\lambda_e-\lambda_d)+O_q(f\log(2q_1D))\\
 &= (1+o(1))\,\frac{fR^2}{4}\log(e/d).
 \end{aligned} \tag{33}

$$

The order is uniform because $R\asymp X^5$. The rank-$R$ compact coefficient fiber on $W_m$ and the definite genus mass in (28) use the same normalization. [19] [25] [26] [27] [28]

### Integer product and the remaining degree estimate

Extend $I_d,I_e$ to a common coefficient field. Write $a_j=\deg I_j\ge0$, where the inequality follows from the trivial twist in each menu. The determinant $Z_j(\vartheta)$ in (11) is the Gram determinant of the full good chain on dimension $D_j$. The short-column comparison retains $h_j$ columns and uses $D_j-h_j$ auxiliary columns with their clearing factors. Each field keeps its own eligible menu, clearing factor and reference determinant. Normalized degree is invariant under extension and additive on products. For $\ell=\operatorname{lcm}(h_d,h_e)$ the exact two-field degree is $\deg(I_d^{\ell/h_d}I_e^{\ell/h_e})/(2\ell)=(a_d/h_d+a_e/h_e)/2$. [15] [16] [21]

Using the principal dimensions, define the integer exponent and normalized degrees by

$$
 s_i=\left\lfloor S_e/S_d\right\rfloor,\qquad
 A_i=\frac{a_d/h_d+a_e/h_e}{2Xbt},\qquad
 A'_i=\frac{\deg(I_d^{s_i}I_e)}{2S_eXbt}.

$$

By (29) and $1-S_d/S_e\le s_i S_d/S_e\le1$,

$$
 (1-\varepsilon_i)A_i\le A'_i\le A_i,\qquad
 \varepsilon_i=4b^{-2}+b^{-8}+S_d/S_e.

$$

For sufficiently late blocks $0\le\varepsilon_i<1$. With $H=H_{d,e,i}$, the inequality $H-A'_i\le(1-\varepsilon_i)(H-A_i)+\varepsilon_i H$ and convexity give the clipped deficit bound

$$
 0\le [H-A'_i]_+-[H-A_i]_+\le\varepsilon_i H_+.
 \tag{34}

$$

The bound uses no upper estimate on the menu degrees. The factorial and normalization terms give $J/(bt)=O_q(L)$ and the prime sum is nonnegative, so $H_+\ll_q (mk/X)L=X^{9/2+o(1)}$. Equations (33) and (34) make the clipping error $O_{q,C}(X^{-C})$ for every fixed $C$. Since $X\ge N^4$ on each occupied block, with $\sum_{i\text{ in block}}c_i\le4$ and $O_A(\log N)$ blocks, the entire weighted window sum changes by $O_{q,A,C}(N^{-C})$ for every fixed $C$. The same window accuracy applies when using (24) as the height, by the Lipschitz bound for the positive part.

The open arithmetic estimate, independent of the released period heights, is to choose the finite eligible menus so that on an unbounded sequence of windows with $D_N\to\infty$ and $D_N=o(\log N)$ there are $D_N^{1-o(1)}$ disjoint pairs satisfying

$$
 \sum_i c_i\left[H_{d,e,i}-\frac{\deg(I_{d,i}^{\,s_i}I_{e,i})}{2S_{e,i}Xbt}\right]_+
 \le N^{o(1)}
 \tag{35}

$$
uniformly on those pairs. The complementary supply gives a specified family on which to seek this bound. In (35) the degree must be from the local maxima of (11) for the full eligible scalar in each field. Its lift factors involve the signed compression order $\operatorname{ord}_w C_l(\vartheta^l)-\operatorname{ord}_w C_l(1)$ in the chain factorization of §8. A direct local approach needs the twisted projection or Gram minors and the untwisted reference order, with the critical ratios and auxiliary clearing controlled at the same eligible twist for that field and place. In a local saturated basis the compression has the form $G^{-1}B$, with $G$ the Gram matrix and $B$ the gluing pairing matrix. A denominator estimate for the twisted compression leaves the untwisted reference order to be controlled. At the small primes used in (25), the split local norms are powers of the coefficient characteristic, so a split spherical estimate requiring norm prime to that characteristic is unavailable there. Equations (25) and (27) estimate the real target $H_{d,e,i}$, while (28)–(34) give the weights for the genuine ideal degrees. [14] [15] [21] [27]

By (34), (35) would give (20). For a putative right-half zero, one of the disjoint pairs survives the exceptional set of (15), and its common signed witness contradicts (18) and (20). The functional equation then gives ordinary RH. With the released period inputs, the bounded integral vacuum of Paper 215 v2 gives the uniform block scales in §§2 and 8. The simultaneous Selmer and critical-ratio selection and projection bounds of §7, the short integral span and lattice-index comparison, and the auxiliary completion and Gram estimates at the rank anchor give the degree bound at the end of §8. This bounds every $[z_{j,i}]_+$ by $O_q(1+V^6L^4)$ and supplies (20), hence (35), with the stated period hypotheses. The conditional RH implication uses these imported inputs in full, while (35) without the period height comparison remains open. [2] [3] [11] [13] [14] [15] [16] [22]

## 11. Denominators away from two conductors

Fix an odd-rank datum of the shorter construction with rank $R>1$, $m$ lifts, good dimension $D>0$ and CM field $E/F$, $F=E^+$. The block family has $m$ a power of two and $E=K_{\rm im}(\zeta_{q_1})$, where $K_{\rm im}$ is imaginary quadratic of prime discriminant and odd class number. Write $s_*=(5R+1)/2$. At this point let $\mathcal R_m(\xi)$ be the determinant of the last forward spherical Rallis operator on the full good space. Every twist below has the same effective modulus within its comparison. Write $d_{\rm den}^{(Q)}(x)$ for the log norm of the denominator ideal away from the rational primes in $Q$, divided by the degree of a number field containing $x$. It is invariant under field extension.

**Theorem.** For every sufficiently large matching cutoff $Y$ there are twists on two rational conductor primes $Q=\{q_A,q_B\}$, and an oriented quotient $U=\mathcal R_m(\xi')/\mathcal R_m(\xi)$ at $s_*$, such that
$$
 d_{\rm den}^{(Q)}(U)\ \ge\ \tfrac12R\log Y-O(1).
 \tag{36}
$$
The effective last-lift characters at the two endpoints differ by the base change of a totally even quadratic character. The two conductor primes may avoid any prescribed finite set. The constants and the two character orders are fixed before $Y$ varies. A quotient $G$ of four such quadratic comparisons satisfies
$$
 \operatorname{ord}_v G=0\quad(v\mid q_Aq_B),\qquad
 d_{\rm den}^{(Q)}(G)\ \ge\ 2R\log Y-O(1).
 \tag{37}
$$
The excluded primes in (36) are exactly the rational conductor primes excluded for that twist in (11). Paper 219 v1, §§4–5, estimates a completed ideal of the combined scalar on an eligible menu. The forward comparison in (36) measures variation within a common-modulus menu. The paired degree estimate (35) also uses the earlier lifts, the signed position of the untwisted reference, and the auxiliary clearing of (11). The deduction of RH in §§8–10 remains conditional on the released period inputs. [29] [2] [3]

### Standard-value inputs

Let $\pi$ run through the good constituents on the compact unitary group, with multiplicities $b_\pi=\operatorname{mult}(\pi)\dim e_0\pi_f^{J_M}$ summing to $D$. At each of two old split places the good projector forces a cuspidal finite type, which gives a supercuspidal local representation by depth-zero induction. The group is definite. Harris–Labesse Theorem 2.2.2 therefore supplies a cuspidal conjugate-self-dual standard base change $\Pi_\pi$ over $E$. The compact Hecke model transfers the joint finite eigenvalues with their multiplicities. For $1\le j\le m$ let $\eta_{j,\xi}=((\mu_j\xi^j)^{\rm BC})^{-1}$, where $\mu_j$ is the fixed lift character and base change of a torus character sends $x$ to its value on $x/\bar x$. For twists with common modulus the quotient of the spherical determinants at lift $j$ equals the ratio of the products of $L_E^S(s_*,\Pi_\pi\otimes\eta_{j,\xi})^{b_\pi}$. The omitted set $S$ consists of the chosen old pairs and both places of each moving pair. The spherical masses cancel at the fixed modulus. At every retained nonsplit place the finite-order characters restrict trivially to the compact torus, so these factors also cancel. [15] [21] [25] [30] [31]

At a retained split pair of norm $Q_v$, write $P_{\pi,w}(X)$ for the raw reciprocal Hecke polynomial, normalized to have constant term $1$. Its roots in the reciprocal convention have absolute value at most $Q_v^{R-1}$. This bound follows from the spherical transform of the unitary representations, or the split lattice bound on the resolvent. At $s_*$ its argument has modulus $Q_v^{-3R}$, since multiplication by the unitary Satake normalizer $Q_v^{(R-1)/2}$ gives $Q_v^{-s_*}$. The two reciprocal polynomials at conjugate places evaluated at the paired phases are complex conjugates there. Their product is positive on the unit circle. The same assertions apply to the transported finite spectra using the compact projector and odd-rank rational Satake normalization. [21] [25] [30]

### Choosing the two rays

Take a finite Galois field $B_0/\mathbb Q$ containing $E$, the fixed Hecke and lift-character coefficient fields and $\mu_{8m}$. The normal closures of the fields of the finitely many good constituents may be included. Choose two sufficiently large distinct odd primes $p_A<p_B<2p_A$, larger than $[B_0:\mathbb Q]$, the two empty-level torus class numbers, the relevant roots-of-unity orders, $m$, and $4RD+1$. Also take them unramified in $B_0$. Neither prime divides the other minus one. There are arbitrarily large such choices by Bertrand's postulate. Set
$$
 N_A=4m p_A^2,\qquad N_B=p_B^2,\qquad B=B_0(\mu_{N_A},\mu_{N_B}).
$$
In the first coordinate use a character $\lambda_A$ of order $N_A$ on the norm-one torus of $K_{\rm im}$, pulled back by $N_{E/K_{\rm im}}$. Its conductor at $q_A$ is the entire oriented fibre above one $K_{\rm im}$-place. In the second coordinate use an order-$N_B$ character $\lambda_B$ on the norm-one torus of $E/F$, with one oriented conductor pair over $q_B$. Choose the primes to act on $B$ by
$$
\begin{array}{c|ccc}
 & B_0 & \mu_{N_A} & \mu_{N_B}\\ \hline
 q_A&1&1&1+p_B\\
 q_B&1& e_A&1
\end{array}
\qquad
 e_A\equiv1\bmod 4m,\quad e_A\equiv1+p_A\bmod p_A^2 .
\tag{38}
$$
The entries denote arithmetic Frobenius, with exponents in the two cyclotomic columns. These elements are central in $\operatorname{Gal}(B/\mathbb Q)$, since they fix $B_0$ and the cyclotomic fields are abelian. Consequently they belong to the decomposition group of every prime over their rational prime.

The residue-symbol fitting below realizes (38), including when the cutoff exceeds $p_A,p_B$. First choose a split rational probe $\ell>Y$ splitting completely in $B$ and satisfying the residual condition below. Orient a place $u$ above the selected $K_{\rm im}$-place. Up to any subsequent finite cutoff $X\ge\ell$, fit $\lambda_A$ to phase $\zeta_{N_A}$ on the oriented fibre at $\ell$ and to $1$ at the other quadratic split probes. Fit $\lambda_B$ to $\zeta_{N_B}$ at $u$ and to $1$ at all other split pairs through $X$. At nonsplit places these unramified torus characters are trivial on the compact local torus.

Let $C_0$ be the finite group of norm-one divisors modulo divisors of rational norm-one elements on the relevant torus. This is the empty-level class group because nonsplit local tori are compact. Finiteness follows from finiteness of the ordinary ideal class group and the fact that norms of units contain squares of the base units. For $K_{\rm im}$ the class number kills $C_0$: if $(\alpha)=v^{h_K}$ for a split place $v$, then $\alpha/\bar\alpha$ has divisor $h_K(v-\bar v)$. In particular $C_0$ has odd order in this case.

Here are the simultaneous Frobenius details. In coordinate $i$, use the base $B_0(\mu_{2N_A})$ for $A$, or $B_0(\mu_{N_B})$ for $B$. For each oriented place $v$ in its list use a norm-one element with divisor $h(v-\bar v)$, taking $h=h(K_{\rm im})$ on $A$ and the order of the empty-level torus class group on $B$. In the first case the chosen class number is odd. In either case $(h,N_i)=1$. Adjoin the $N_i$-th roots of these elements and take the rational normal closure $L_i$. Inertia at the designated place above $\ell$ fixes the base and all the other listed radicals, which are roots of local units of order prime to $\ell$. It realizes a generator on the designated radical because the latter has valuation $h$ before adjoining its root. Equivalently, one can take this inertia in the full compositum with $\mathbb Q(\mu_{p_j^2})$, which is unramified at $\ell$ for $j\ne i$. This gives the local fitting action while fixing that extra cyclotomic field. The extension generated by the listed radicals is Galois over the base, so restriction from inertia in the normal closure surjects onto its local inertia.

The extension $L_i$ over its normal base is generated by conjugate Kummer radicals of exponent $N_i$. Its degree over $\mathbb Q$ is prime to $p_j$ by the choices above. Thus $1+p_j$ on $\mu_{p_j^2}$ fixes the intersection with $L_i$, and extends while fixing all of $L_i$. Multiply this extension by the inertia element just constructed. Chebotarev for the resulting class, choosing a place with the specified Frobenius, gives each prime in (38) with the required power residues. The two primes may be chosen successively above $X$. This degree argument also covers radicals ramified at a prime above $p_j$. At the chosen conductor the ray class group surjects onto $C_0$. Its kernel is the oriented residue group $\mathbb F_{q_i}^{\times}$ modulo the image of the everywhere integral rational norm-one points, which are roots of unity. At $q_A\equiv1\bmod 2N_A$ the order-$N_A$ residue character kills the quadratic units, and at $q_B$ the unit order is prime to $p_B$. The primary subgroups for the primes dividing $N_i$ are in the kernel because $(|C_0|,N_i)=1$. Extend the residue character by triviality on the other primary subgroups. For an oriented split uniformizer $t_v$ one has $t_v^h=u_vk_v$, with $u_v$ the listed element and $k_v$ integral. Consequently the value on $t_v$, raised to $h$, is the inverse $N_i$-th power residue symbol of $u_v$, as read by the chosen Frobenius on the radical. Since $(h,N_i)=1$, a primitive renormalization gives the prescribed probe phase and leaves the other values $1$. The conductor primes are split in $E$, so the norm pullback on each oriented coordinate above the chosen $K_{\rm im}$-place is the identity. [30] [33]

### A difference of four quadratic comparisons

Use $a=1,a'=e_A$, $b=1,b'\in1+p_B\mathbb Z\bmod p_B^2$, and put $k_0=2p_A^2$. For these indices define
$$
 \xi_{a,b}=\lambda_A^a\lambda_B^b,\qquad
 U_{a,b}=\frac{\mathcal R_m(\xi_{a+k_0,b})}{\mathcal R_m(\xi_{a,b})},
 \qquad
 G=\frac{U_{a,b}U_{a',b'}}{U_{a',b}U_{a,b'}} .
 \tag{39}
$$
All eight twists have the same oriented conductor set. Each exponent $a,a',a+k_0,a'+k_0$ is odd and prime to $p_A$. All powers through $m$ are effective at every declared place. Since $mk_0=N_A/2$, the effective quotient in each $U_{a,b}$ is $(\lambda_A^{N_A/2})^{\rm BC}=\chi\circ N_{E/F}$, where $\chi=\chi_{q_A}\circ N_{F/\mathbb Q}$ and $\chi_{q_A}$ is the even Legendre character. Indeed $\chi_{q_A}\circ N_{K_{\rm im}/\mathbb Q}$ is trivial on diagonal ideles and descends through $x\mapsto x/\bar x$ by Hilbert 90. Its residue value at the conductor is the Legendre symbol of $xy$, which equals that of $x/y$. At every other split place it is unramified. At inert places local Hilbert 90 maps units onto the compact torus, and at the ramified rational prime $d$ of $K_{\rm im}$ the character is trivial by $\chi_{q_A}(d)=1$, using reciprocity and splitting in $K_{\rm im}$. The quotient with the quadratic power of the ray thus factors through the odd group $C_0$ and is trivial. The norm identity extends it to $E$. Also $(e_A-1)k_0=0\bmod N_A$, so the first-coordinate coefficient action transports the numerator with exactly the indicated shift.

For a fixed constituent and twist put $\Theta=\Pi_\pi\otimes\eta_{m,\xi_{a,b}}$. At the chosen CM embedding over each real place its angular exponents $A_i$ are distinct positive integers. The last tail entry is $R^8$, all other tail entries are spaced by $2R^8$, and the head lies above the tail. Thus $\Theta^c\simeq\Theta^\vee$ and $\Theta^c\not\simeq\Theta$. Cyclic induction gives a unitary cuspidal $\Sigma=\operatorname{AI}_{E/F}\Theta$ on $\mathrm{GL}_{2R}$. Let $\epsilon$ be the character of $E/F$. In the exterior square of the induced Weil representation, the mixed tensor acquires a minus sign when the two copies are interchanged. Twisting by $\epsilon$ gives the Asai-plus term, together with the induced exterior square. The Asai-plus factor has a pole at $1$ for odd-rank unitary base change, and the partial exterior square of $\Theta$ is holomorphic and nonzero there. The character twist leaves the Asai sign unchanged because $\eta_{m,\xi}$ is trivial on the $F$-ideles. Also $\omega_\Theta|_{\mathbb A_F^\times}=1$ since it is trivial on norms and on real signs. The exterior-square criterion therefore gives $\Sigma$ a Shalika model with character $\epsilon$. [31] [32] [34] [35] [37]

The representation $\Sigma\otimes|\det|^{1/2}$ is cohomological, with infinitesimal character $(A_1,\ldots,A_R,-A_R,\ldots,-A_1)+1/2$ and Shalika character $\epsilon|\cdot|$. The original $s_*$ corresponds to $1/2+k$ with $k=(5R-1)/2$. Its criticality follows from $-A_R\le k\le A_R-1$. The numerator twist descends to $\chi$ on $F$, whose signs at the real places are all positive. Consequently the two special-value formulas use the same archimedean factor and the same signed Shalika period. Dividing Grobner–Raghuram's Theorem 7.1.2 at $\chi$ by the same theorem at the trivial character cancels these factors. Proposition 5.2.3 supplies the multiplier $\chi_f(t_\sigma)^R$ from the finite Gauss sum, where $t_\sigma$ is the cyclotomic unit idele. For retained places the induction formulas pair the two split polynomials or substitute $X^2$ at an inert place. The old and conductor Euler factors removed from the standard values transport with their algebraic normalized local coefficients. After multiplying with the good multiplicities one obtains [32] [37]
$$
 \sigma(U_{a,b})=\chi_f(t_\sigma)^{RD}U^{\rm an}_{a,b,\sigma}.
 \tag{40}
$$
Here the superscript means the analytic quotient formed from transported finite factors at the original place labels. The exponent is $\sum_i R d_i=RD$. In the raw Gauss-sum convention the Gauss square is $N_{F/\mathbb Q}\mathfrak f_\chi=q_A^{[F:\mathbb Q]}$: the local magnitude is the square root of the conductor norm and the product of the finite signs at $-1$ is one. This rational norm factor is fixed by conjugation. The remaining multiplier is $1$, because the norm of the diagonal unit idele $t_\sigma$ is $t_\sigma^{[F:\mathbb Q]}$ and $[F:\mathbb Q]=\varphi(q_1)$ is even. Thus each $U_{a,b}$ is in $B$ by invariance under $\operatorname{Aut}(\mathbb C/B)$, and $G$ is exactly equivariant. [37]

At $q_A$ set $x=U_{a,b}/U_{a',b}\in B^\times$. A power $\sigma_B$ of the first row of (38) sends $b$ to $b'$ and fixes $a,a'$. Thus $G=x/\sigma_B x$. At $q_B$ use $y=U_{a,b}/U_{a,b'}\in B^\times$. The second row of (38) sends $a$ to $a'$ and fixes both $b$'s, giving $G=y/\sigma_A y$. At every prime over the indicated conductor the corresponding automorphism preserves the valuation. This proves the zero orders in (37). Each expression also gives absolute norm one for $G$.


### Nonvanishing and size

Choose an auxiliary coefficient prime $\ell'\nmid 2RDp_Ap_B$. At a rational prime $\ell$ completely split in $B$, take one oriented pair $u=(w,\bar w)$. Its paired reciprocal denominator at the last lift is
$$
 A_u(z)=\prod_\pi
 \left[P_{\pi,w}(\ell^{-3R}\gamma_w^{-1}z^{-1})
 P_{\pi,\bar w}(\ell^{-3R}\gamma_w z)\right]^{b_\pi},
 \qquad \gamma_w=\mu_m(\varpi_w/\bar\varpi_w).
$$
We can impose $\ell\equiv1\bmod\ell'$, $P_{\pi,w}(X)\equiv(1-X)^R\bmod\ell'$ and $\gamma_w\equiv1\bmod\ell'$ simultaneously. For the character use the algebraic avatars of the fixed lift and splitting characters and the cyclotomic character for its norm power. For the polynomials take an open subgroup on which all the residual attached representations are trivial. Inside the subgroup fixing $B$ and the residual data, intersect the finitely many Frobenius approximation sets for the good eigenrows, also after conjugating the choice of place. The released approximation property on each open set gives a smaller nonempty open part on which the required congruences hold outside finitely many primes. Chebotarev then gives such probes above any $Y$. The coefficient of $z^{-1}$ in $\log A_u(z)$ on the circle is $-\ell^{-3R}\gamma_w^{-1}\sum_\pi b_\pi a_{\pi,w,1}$, with $-a_{\pi,w,1}$ the linear coefficient of $P_{\pi,w}$. The sum reduces to $RD$ at $\ell'$. Thus $A_u(z)\ne A_u(-z)$, by positivity on the circle, and its exponents are in $[-RD,RD]$. [25] [30] [33]

Then $H(z)=A_u(z)/A_u(-z)$ is nonconstant of rational degree at most $2RD$. Indeed a constant must be $1$ by positivity and $H(z)H(-z)=1$. At $u$ the first-coordinate variation $a\mapsto a'$ multiplies the effective phase by $\omega=\zeta_{N_A}^{m(a'-a)}$ of order $p_A$. Consequently $J(z)=H(z)/H(\omega z)$ is nonconstant. A constant quotient would be a positive $p_A$-th root of unity and hence $1$. Invariance under this rotation would put $H$ in $\mathbb C(z^{p_A})$, contradicting $\deg H<p_A$. The degree of $J$ is at most $4RD$. The $p_B$ choices of $b'$ give distinct effective phases $\zeta_{N_A}^{ma}\zeta_{N_B}^{mb'}$. Since $p_B>4RD$, at least one changes $J$ from its value at $b$. Fix it. At the other pairs of the fibre above $\ell$ the $B$-ray phase is $1$ and the two columns in (39) cancel. Thus the absolute value $g$ of the probe contribution to $\log G$ is positive.

All powers in (39) agree through $Y$. Uniformly over embeddings, the change in the log of a paired determinant from prime norms over rational primes $>X$ is $O_{E,R,D,m}(X^{-2R})$. The split polynomial estimate above gives this for the finitely many factors in (39). Summing the logarithmic series over prime powers gives the asserted exponent. Choose $X$ after fixing the phases so the tail in (39) is less than $g/2$, and then perform the ray fitting. The distinguished value satisfies $G\ne1$. At every embedding $\rho$, (40) and the original cutoff give $|1-\rho G|\ll Y^{-2R}$. The product formula applied to $G-1$ gives (37), since $G-1$ and $G$ have identical negative orders at finite primes. Finally the negative part of the sum of the four signed local orders in (39) is at most the sum of the four oriented negative parts. Their off-conductor degrees prove (36) for at least one of the four comparisons with the indicated orientation or its inverse.

### The product of all lifts at several critical integers

For the full product there is a second consequence of (38). Let $\mathcal I\subset[s_*,R^8]\cap\mathbb Z$ be finite with at least two elements. Now take both rays as singleton $E$-rays of odd orders $p_A^2,p_B^2$. Write $V_t(\xi)$ for the product of all $m$ partial standard values at $t$, with every good multiplicity, omitting the common old and conductor sets. Set
$$
 M_t=\frac{V_t(\xi_{a,b})V_t(\xi_{a',b'})}
             {V_t(\xi_{a',b})V_t(\xi_{a,b'})}.
$$
The same construction gives
$$
   d_{\rm den}^{(Q)}(M_t)\ge R\log Y-O(1)
   \quad\text{for all but at most one }t\in\mathcal I .
 \tag{41}
$$
Here $s_*$ may be the exception. Each mixed quotient is a unit over both conductor primes.

Set $a=1$, $a'=1+p_A$, $b=1$. At a single retained split probe the product of all paired reciprocal denominators $A_{u,t}(z)$ has Laurent support from $-L$ to $L$, with $L=RD\sum_{j=1}^m j$. Its extreme coefficients are nonzero by invertibility of the central Hecke translations. In either extreme, the product of the leading coefficients is multiplied by the $t$-dependent argument once for each of the $RmD$ reciprocal roots on that side. Hence the extreme coefficient moduli differ at distinct arguments. The mean of $\log A_{u,t}$ on the circle is zero by Jensen's formula for each polynomial with constant term one and no zeros on or inside its argument disk. Consequently $H=A_{u,t}/A_{u,t'}$ is nonconstant for $t\ne t'$. Its degree is at most $2L$. Choose $p_A>2L$ and $p_B>4L\binom{|\mathcal I|}{2}$ satisfying the preceding coprimality requirements. They can be taken in one Bertrand interval above both bounds. The rotation argument for $H(z)/H(\zeta_{p_A}z)$ excludes at most $4L$ choices of the second-coordinate phase for each pair of arguments. One $b'\equiv1\bmod p_B$ therefore works for all pairs. Fit both singleton rays as before, choosing $X$ to cover the least of the resulting positive probe gaps. Then each $M_t/M_{t'}$ differs from $1$.

Raghuram's consecutive-critical-value formula for $\mathrm{GL}_R\times\mathrm{GL}_1$ over $E$ has the same discriminant factor, archimedean quotient and cohomological signs for two choices of the finite-order ray. These terms cancel upon division, giving exact equivariance at every coefficient embedding for the divided adjacent ratio. The original finite deletions transport by the local Euler polynomials. All the intermediate integers are critical. At each embedding the smallest absolute shifted angular parameter in the lifts is $R^8$, so the gamma factors at the point and its reflected point have positive arguments throughout the interval. The finite values are nonzero in the range of absolute convergence here. Multiplying adjacent ratios gives equivariance of $M_t/M_{t'}$ at every embedding. Agreement below $Y$ and the same convergent tail bound thus give $|1-\rho(M_t/M_{t'})|\ll Y^{-2R}$ for every $\rho$. Its finite denominator degree is at least $2R\log Y-O(1)$. [30] [36]

For the individual $M_t$ only equivariance over $B_0$ of an integer power is required. At $s_*$ apply Grobner–Harris–Lin Theorem 5.13 to each cohomological conjugate-self-dual constituent and its algebraic Hecke twist. Their Hypothesis 2.4 is supplied in odd rank by Remark 2.5. The shifted angular exponents are nonzero for every lift and their signs agree for all corners. In the divided formulas the automorphic period and Tate factor cancel. Let $n=p_A^2p_B^2$. The checked twisting characters at any two corners have equal $n$-th powers. Lemma 2.2(b), iterated on the characters of nonzero angular type, identifies the $n$-th powers of their CM periods with the periods of those common character powers as equivariant families, up to transported algebraic factors. The quotient raised to $n$ therefore transports exactly for embeddings fixing $E$, hence for those fixing $B_0$. At every other argument in the interval multiply by the already equivariant adjacent ratios. This application uses Theorem 5.13 as stated. [36] [38]

The $n$-th power of each one-coordinate quotient of standard products lies in $B$ by invariance under automorphisms fixing $B$. In the two directions $M_t^n$ has the respective forms $x/\sigma_B x$ and $y/\sigma_A y$, using those powered quotients. It is a unit at both conductors and has absolute norm one. The numerator and denominator degrees of $M_t$ away from the two conductors are consequently equal. By subadditivity the denominator degree of $M_t/M_{t'}$ away from the conductors is bounded above by the sum of the denominator degrees of $M_t$ and $M_{t'}$ there. The preceding lower bound for every pair of arguments proves (41).

### The primes supporting the completed ideal

Fix one completed basis at a node $x$ of a rank interval. Let $T_x$ be its finite set of occupied translates, $D_X$ the source-form dimension, and $\epsilon_l$ the divisibility error at $l$ in the fixed gauge. Define
$$
 J_x=\prod_l l^{|T_x|\lfloor D_X\epsilon_l\rfloor},
 \qquad \Omega_x=J_x^2G_x(1),\qquad
 C_\xi=J_x^2(\gamma_\xi\bar\gamma_\xi)^{c_R}G_x(\xi).
$$
The sum $\sum_l\epsilon_l\log l$ is finite, so the product defining $J_x$ is finite. For one block of translated columns the source gives an integer $j\le D_X\epsilon_l$ and a clearing matrix whose determinant divides $l^j$ in the valuation ring. Combining the blocks bounds the normalized order of the determinant by $v_l(J_x)$ at each of the two coefficient embeddings used by the integral pairing. Thus $C_\xi$ is integral at every place eligible for $\xi$, and $\Omega_x=C_1$ is a nonzero algebraic integer. [16] [21] [39]

In a common coefficient field for any finite menu containing $1$, let $\mathfrak c_x$ have order $\min_{\xi:\,l(w)\nmid Q_\xi}\operatorname{ord}_w C_\xi$ at each finite place $w$. Since $C_\xi A_R(\xi)=\Omega_x$, definition (11) gives
$$
 I_{d,R}\,\mathfrak c_x=(\Omega_x).
 \tag{42}
$$
Both ideals on the left are integral. The rational primes under the divisors of this one untwisted value contain the support of every completed menu ideal for this datum and basis. In (35) the paired degree is therefore the degree of $(\Omega_d)^{s_i}(\Omega_e)$ less that of $\mathfrak c_d^{s_i}\mathfrak c_e$. The independent lower bound asks how much the eligible twists can reduce the orders of the cleared Grams at these particular primes. [29] [39]

In fact for any fixed finite set $P$ the terminal construction gives
$$
 d_{\rm den}^{(Q\cup P)}(U)\ \ge\
       \frac{2R}{4\cdot 2^{|P|}}\log Y-O_{E,R,D,m,P}(1).
 \tag{43}
$$
Take $h=[B_0:\mathbb Q]$ and choose both order primes outside the ramification of $B_0$ and larger than the members of $P$ and $4RD\prod_{l\in P}(1+l^h)$. The two odd cyclotomic fields together meet $B_0$ trivially since their inertia groups at the order primes generate their full compositum group. Let $g_l$ fix $B_0$ and act on the odd roots by exponent $l^h$. It belongs to the decomposition group of every place over $l$, being a power of relative Frobenius over $B_0$. This also holds when $l$ ramifies in $B_0$. Apply the commuting group-ring differences $\prod_{l\in P}(1-g_l)$ multiplicatively to $G$. The result is a unit above $P$ and both conductors.

At the retained probe write the phase as $\epsilon z$ with $\epsilon\in\mu_4$ fixed and $z$ of odd order. Start with $H(\epsilon z)$ and successively replace the rational function $F(z)$ by $F(z)/F(z^{l^h})$. At each step a constant outcome would imply $\deg F=l^h\deg F$, impossible for nonconstant $F$. The resulting positive function has degree at most $2RD\prod_{l\in P}(1+l^h)$. The first-coordinate rotation evaluates this final function at $\omega z$, including the power of $\omega$ inside each substitution. The two earlier degree arguments still give a nonzero gap. The tails are bounded by at most $2^{|P|}$ times the old bounds. The product formula now gives $2R\log Y-O(1)$ away from $Q\cup P$ for the resulting mixed difference. Its expansion has $4\cdot2^{|P|}$ oriented quadratic comparisons with multiplicity. Coefficient conjugations preserve denominator degree off any rational prime set and transport those factors by (40), so one original oriented comparison satisfies (43). In particular $P$ may contain every rational divisor below $(\Omega_x)$. The terminal denominators in (43) then occur at places where the full ideal in (42) has order zero. [30] [37] [39]

## 12. A test at the prime divisors of the reference

Fix a common level block. For each of its fields and ranks choose one completed basis and let $P$ contain all the rational prime divisors below the corresponding values $\Omega_x$ from (42). Define $v_w(l)=1$ for a coefficient place $w\mid l$. The relevant signed order in (11) is $e(w/l)v_w(A_R(\xi))$. Every positive contribution occurs over $P$. The following selection controls the turns and quotients on entire primitive layers at these primes. It uses the rank-one integral measures of §7 and their critical-value comparison.

**Proposition.** Given any tolerance $\varepsilon>0$ and any lower bound on the layers, at most two rational auxiliary conductors suffice on the fixed block for the following assertions. Each $l\in P$ is paired with a conductor $q\ne l$. For every field in the block there is a singleton ray of global and local order $l^k>m$ above $q$, with $k$ common to the finite collection of anchors at this $l$. Every primitive power of the ray, at every coefficient embedding over $l$, has
$$
 v_w(r_z(\lambda^a))\le\varepsilon
 \tag{44}
$$
for every original turn and quotient critical ratio $r_z$, including the indicated character power in the ratio. Both old levels and the full empty-modulus reference of (11) are retained. The construction permits the auxiliary conductors to avoid any prescribed finite set.

For the primes $l\ne p_0$ use tame inertia $g$ at $p_0$ and for $l=p_0$ use tame inertia at $p_1$. Treat each nonempty group separately. Both old rational primes split completely in every host $E$. Fix a single place of $\overline{\mathbb Q}$ over the selected old prime $p$. In each host one of its place and its conjugate is chosen, since the old norm generator and its conjugate have product $p_0p_1$. The base-changed character on the two sides of a split pair has inverse values. Its order on $g$ for each of the actual factors in (44) therefore equals the order of a power $0<|u|\le 2m$ of the old character. Both 2 and 3 divide this order since the old order is $(q_0 d)^{s+6}$ with $6\mid q_0$ and $2^s=m^{22}$. Its reduction modulo every $l$ in the group is nontrivial, at every chosen coefficient embedding. [10] [12]

For a large depth $L_l$ for each prime in the group put $n=\prod_l l^{L_l}$. In the finite class group of the norm-one torus modulo its maximal compact take idele lifts $t_i$ of invariant-factor generators of orders $b_i$. Choose representatives with component $1$ above $p$ by weak approximation on the two sides of each split pair and multiplication by integral ideles. Write $t_i^{b_i}=\alpha_i u_i$ up to the infinite subgroup, with $\alpha_i$ a rational torus point and $u_i$ integral everywhere. All the $\alpha_i$ are units above $p$. At $p$ the roots of these units of degree $n$, the $n$-th roots of norm-one global units, and $\mu_n$ are unramified. The global norm-one units are roots of unity. In the compositum for all hosts the selected inertia generator therefore fixes the needed Kummer data. It fixes each $E$ and acts on the finite residual avatars of the critical characters by the old inertial values just described. Chebotarev for its image in a finite rational normal closure realizes these restrictions at a single $q$ outside all exclusions. Use one oriented pair for each host, given by restriction of the same chosen Frobenius place. Pull back the order-$n$ residue character of $\mathbb F_q^\times$. It is trivial on the global units and on each $\alpha_i\bmod q$. Assigning $1$ to each $t_i$ extends it across the ray group since the $b_i$-power relations have trivial residue value. Thus for each $l$ its primary component has exact global and local order $l^{L_l}$ even if $l$ divides the empty class number. No size bound on $q$ enters (11). [12] [33]

For a critical ratio with the indicated character exponent write $s_z=1$ at critical integers at least 2 and $s_z=2$ at critical integer 1. Its integral group-ring measure at modulus $q$ has a polynomial $F(X)$ on the $l$-power ray, using the required character power in the substitution. A negative exponent can be cleared by a monomial unit. At the declared trivial twist the Euler insertion gives $v(F(1))=B_z$, the fixed valuation of the nonzero integral empty-reference measure. Indeed $q\equiv1\bmod l^{L_l}$ and the old inertial residues avoid $1$ for both signs, including for the extra exponent zero at critical point 1. At a genuine twist $v(F(\zeta))=B_z+s_zv_w(r_z)$. Conductor powers are units at $l$. The same finite Chebotarev condition can impose this at representatives of all places of a fixed Galois coefficient field $B_0$ containing the fixed character and Hecke data and the hosts. [12] [13]

Write $r_j=1/\varphi(l^j)$. For all polynomials $F(1+Y)$ at these embeddings the sum of the positive valuations of their roots is bounded by $B=\sum B_z$, by the Gauss norm and integral coefficients. At a primitive $l^j$-th root an increase above the constant-term valuation is possible only from roots of valuation $r_j$. For each such root $\alpha$, discard the closest $l^j$-th root of unity to $1+\alpha$. At each other root of unity its distance valuation is at most the distance valuation to that closest root. The sum of the latter valuations is $j$, from the derivative of $X^{l^j}-1$. Consequently the average over primitive labels of $\min(1,v(\zeta-1-\alpha))$ is at most $(j+1)r_j$. Let $n_j$ count all roots at valuation $r_j$ with multiplicity. Then $\sum_jn_jr_j\le B$. Given $\eta<1/[B_0:\mathbb Q]$ and $0<\varepsilon'<\min(1,\varepsilon)$, choose the lower depth with $l^{k_0}>m$ and the upper depth $L_l$ so $\sum_{j=k_0}^{L_l}1/(j+1)>B/(\eta\varepsilon')$. The valuations $B_z$ are fixed before choosing the upper depth and $q$. Some $k$ has $(k+1)n_kr_k<\eta\varepsilon'$. Markov's inequality shows that fewer than a fraction $\eta$ of the primitive labels violate a bound in (44) at the tested embeddings. On the other labels the sum of capped valuations is $<1$, so the caps may all be removed. Use the power of the original ray with local and global order $l^k$.

At $v\mid l$ on $B_0$ the local group acting on the primitive powers is $\operatorname{Gal}(\mathbb Q_l(\mu_{l^k})/((B_0)_v\cap\mathbb Q_l(\mu_{l^k})))$. Its index is at most $[(B_0)_v:\mathbb Q_l]$. Each separate critical-ratio valuation is constant on its orbits. In fact the powered CM comparison used in §11, now for the divided rank-one values with their common angular type, transports their $(2l^k)$-th powers under $B_0$-linear automorphisms by the corresponding substitution on character powers. The even power also accounts for the absolute-value normalization. The common-period factors cancel after taking the power and the empty-reference Euler correction transports algebraically. Each local automorphism lifts fixing the place, which proves the valuation assertion. One failure would give a fraction at least $1/[B_0:\mathbb Q]$ of failures. This proves (44) for every primitive power at the tested places. Galois transport permutes the whole primitive layer, extending the bound to every prolongation. [38] [40]

To see what remains to estimate in (35), write $U(a)$ for the forward product of the higher-rank standard ratios at $s_*$ with all their good multiplicities. Let $W_1$ be the sum of the multiplicities of the critical ratios in (44), counting $D$ for each quotient and $2c_R$ for each turn at every critical integer. The moving spherical correction and the Gram modulus give $q^{5R^2}$ per good dimension per lift. This and all the other pure conductor powers are units at $w$. In the inverse completed scalar the standard factors and the rank-one ratios enter with negative exponents. Thus on the selected layer
$$
 \max\{0,\max_a v_w A_R(\lambda^a)\}
 \ \ge\ \left[-\min_a v_w U(a)- W_1\varepsilon\right]_+ .
 \tag{45}
$$
The empty reference retains the Euler pair over $q$ in every ratio. Squaring a rank-one period in the integral interpolation at 1 has already been accounted for by $s_z$ in the proof of (44). [12] [15] [21]

There is an explicit lower test for the first term in (45). Let $\delta=\lambda^{\rm BC}$, let $M_t/E$ be the degree-$l^t$ subfield of its cyclic class field, and set $\phi=\varphi(l^k)$. The split local map $x\mapsto x/\bar x$ is surjective from either coordinate of the conductor pair, so $\delta$ has full order $l^k$. For a lift $j$ put $h_j=k-v_l(j)>0$, $\Pi_{\pi,j}=\operatorname{BC}(\pi)\otimes(\mu_j^{\rm BC})^{-1}$, and define $L_{\pi,j,t}$ to be the standard value at $s_*$ after base change to $M_t$, omitting the old places and the full pullback of the moving pair. Use $M_0=E$. Write $L_{\pi,j,*}$ for the untwisted value over $E$ with only the old places omitted. The product of the $U(a)$ over all primitive labels is
$$
 \mathcal U=\prod_{j,\pi}
 \left(\frac{(L_{\pi,j,h_j}/L_{\pi,j,h_j-1})^{\,l^{v_l(j)}}}
 {L_{\pi,j,*}^{\,\phi}}\right)^{b_\pi}.
 \tag{46}
$$
Multiplying primitive labels by $j$ gives every character of exact order $l^{h_j}$ with multiplicity $l^{v_l(j)}$. By Artin formalism their product is the quotient of the complete character products at the two consecutive layers. This proves (46) place by place in the convergent Euler products. The numerator with $h_j=1$ uses the deleted $L_{\pi,j,0}$ in the layer quotient. The product $\mathcal U$ is algebraic by the same divided special-value comparison used in §11. Therefore in (45) the smaller signed quantity $-v_w(\mathcal U)/\phi$ may replace $-\min_a v_w U(a)$. At an unramified place of $B_0/\mathbb Q$ the local cyclotomic group is the full group by total ramification. The powered higher-rank comparison of §11 then makes all the valuations equal, giving equality of these two signed quantities. [32] [38]

Sum (45) over the fixed reference primes with their local degree weights. Each union of the primary menus is finite and contains the trivial twist. The error is bounded by $W_1\varepsilon\sum_{l\in P}\log l$ per datum. It can be made arbitrarily small after the weights in (35) on any fixed window by choosing the tolerances first. The lower test now asks for sufficiently negative normalized orders in (46) on these selected layers across sufficiently many of the complementary field pairs. Neither their magnitude nor their frequency follows from the cyclic product formula.

## 13. A depth average at the reference primes

Fix the completed basis, the cleared untwisted Gram $\Omega$ from (42), and a place $w\mid\ell$ with $v_w(\ell)=1$. Write $V=v_w(\Omega)$. Use the ray of §12 with conductor $q\ne\ell$ and top order $\ell^L$. Choose $k_0\le L$ with $\ell^{k_0}>m$. Take the menu of all primitive labels $a\bmod\ell^k$ at depths $k_0\le k\le L$ together with the empty twist, and let $S_w$ be its maximum eligible normalized order. Then $0\le S_w\le V$ by (42). Write $d_{k,a}=-v_w U(\xi_{k,a})$ for the signed score from the forward higher-rank standard product in (45). Index its separate rank-one corrections by $i$, with exponents $u_i>0$ and interpolation powers $s_i=2$ at critical integer $1$ and $s_i=1$ otherwise. In the integral interpolation of §12 let $F_i$ be the polynomial on the top ray, with the lift-character power already inserted. At a primitive label $\zeta=\zeta_{\ell^k}^a$,
$$
 v_w A_R(\xi_{k,a})=d_{k,a}-\sum_i u_i v_w r_i(\xi_{k,a}),\qquad
 v_w F_i(1)=B_i,\qquad
 v_w F_i(\zeta)-B_i=s_i v_w r_i(\xi_{k,a}).
$$
The conductor powers are units and the declared-trivial Euler insertion fixes $B_i$ before $L$ and $q$. [12] [15] [38]

Put $\phi_k=\varphi(\ell^k)$, $g_w=[(B_0)_v:\mathbb Q_\ell]$ for the restriction $v$ of $w$ to the fixed coefficient field of §12, and $C_w(T)=\sum_i B_i\max\{u_i/s_i,T\}$. For $0\le T\le V$,
$$
\begin{aligned}
 \sum_{k=k_0}^L\frac{1}{(k+1)\phi_k}
 \sum_{a\bmod\ell^k}^{*}[\min(T,[d_{k,a}]_+)-S_w]_+
 &\le C_w(T),\\
 \sum_{k=k_0}^L\frac{1}{k+1}
 [\min(T,[\max_a d_{k,a}]_+)-S_w]_+
 &\le g_w C_w(T).
\end{aligned}
\tag{47}
$$

At a label the excess on the left is bounded by $\sum_i\min(T,u_i[v_w r_i]_+)$, by the signed identity and subadditivity of capped positive parts. Factor $F_i(1+Y)$ with roots $\alpha$ counted with multiplicity. Multiplicativity of the Gauss norm gives $\sum_\alpha[v_w(\alpha)]_+\le B_i$: this sum is the constant coefficient valuation minus the smallest coefficient valuation. At $Y=\zeta-1$ the valuation of $Y$ is $b_k=1/\phi_k$. Roots with $v_w(\alpha)<b_k$ give zero change relative to the constant term, and roots of greater valuation give a nonpositive change. If $n_{i,k}$ counts roots of valuation $b_k$, then $\sum_k n_{i,k}b_k\le B_i$.

For each root at valuation $b_k$, choose an $\ell^k$-th root of unity $\zeta_0$ maximizing $v_w(\zeta_0-1-\alpha)$. For $\zeta\ne\zeta_0$ the ultrametric inequality gives $v_w(\zeta-1-\alpha)\le v_w(\zeta-\zeta_0)$. The sum of the latter valuations over all other $\ell^k$-th roots is $k$ by differentiating $X^{\ell^k}-1$. These latter valuations are nonnegative. The mean over primitive labels of the distance valuation capped at $t$ is therefore at most $(k+t)b_k$, whether or not $\zeta_0$ is primitive. Apply this with $t=Ts_i/u_i$ and drop the subtraction of $v_w(\alpha)$ in bounding the positive excess. Subadditivity gives the mean loss bound $n_{i,k}b_k((u_i/s_i)k+T)$ for factor $i$. Division by $k+1$ and summation give the first line of (47). The powered reciprocity in §12 makes each separate loss constant on local cyclotomic orbits. Each orbit contains at least $\phi_k/g_w$ labels, so its maximum loss is bounded by $g_w$ times its mean. Applying this factor by factor proves the second line. [38] [40]

Let $D_k=\phi_k^{-1}\sum_a^* d_{k,a}$ and $H=\sum_{k=k_0}^L(k+1)^{-1}$. Since $D_k\le\max_a d_{k,a}$, the second line of (47) at cap $V$ gives
$$
 S_w\ge \frac{1}{H}\sum_{k=k_0}^L\frac{\min(V,[D_k]_+)}{k+1}
          -\frac{g_w C_w(V)}{H}.
\tag{48}
$$
For $0<t\le V$ the set of depths with $D_k\ge t$ and harmonic weight $h>0$ gives $S_w\ge t-g_w C_w(t)/h$ by taking cap $t$ in (47).

### Cumulative standard products

Use $L^S_{\pi,j,t}$ for the cyclic base-change value on $M_t$ from (46), deleting the pullbacks of the old and moving pairs, and $L_{\pi,j,*}$ for the empty reference, retaining the moving pair. For $k\ge0$ set $v_j=v_\ell(j)$ and $h_{j,k}=\max(0,k-v_j)$. Define
$$
 \mathcal C_k=\prod_{j,\pi}
 \left(\frac{(L^S_{\pi,j,h_{j,k}})^{\ell^{\min(k,v_j)}}}
 {L_{\pi,j,*}^{\,\ell^k}}\right)^{b_\pi},
 \qquad E_k=-\ell^{-k}v_w(\mathcal C_k).
\tag{49}
$$
Multiplication by $j$ on the $\ell^k$ labels has kernel of size $\ell^{\min(k,v_j)}$ and image the characters of $M_{h_{j,k}}/E$. Artin formalism, with common deletions, identifies (49) with the product of the divided values over all labels, including the declared zero label. This includes $\ell^k\mid j$, when the numerator is the deleted value on $E$ at every label. The divided comparison of §11 and its algebraic local corrections give algebraicity of this product, so the valuation in (49) applies to the product itself. Removing the embedded labels of depth at most $k-1$ leaves the primitive layer. Its negative valuation is $\ell^k E_k-\ell^{k-1}E_{k-1}$, and division by $\phi_k$ gives
$$
 D_k=\frac{\ell E_k-E_{k-1}}{\ell-1}.
\tag{50}
$$
At a place with trivial cyclotomic intersection this mean also equals the individual signed scores by the powered comparison of §12. For a fixed window the reference primes, local degree weights, $V$, $g_w$ and $B_i$ are fixed before fitting the top ray. Consequently the weighted error from $g_w C_w(V)/H$ can be made arbitrarily small. The lower bound for the clipped signed terms on enough pairs to imply (35) remains open. [32] [38]

### Exact values in reduced ranks

**A CM elliptic ray at $601$.** Let $K=\mathbb Q(\theta)$ with $\theta^2=-2$, and let $C:y^2=x^3-30x+56$. The normalized degree-two Vélu isogeny at $(4,0)$ has target coefficients $\theta^4(-30),\theta^6 56$. Scaling back gives the endomorphism with invariant differential multiplier $\theta$, so the complex period lattice is $\Lambda=\Omega_C\mathcal O_K$ since the class number is one. At $q=601$ the roots of $T^2+2$ are $\pm104$ and $7$ generates $\mathbb F_q^\times$. A generator $\alpha=a+b\theta$ of an ideal prime to $q$ has ray label $e(\alpha)=\log_7((a+104b)/(a-104b))\bmod25$. The ratio is unit-independent and surjective. Each nonzero order-$5$ or order-$25$ power is ramified at both split primes, and the ratio is trivial on rational ideles and on the ramified uniformizer $\theta$ since the latter has residue ratio $-1$. Let $\chi((\alpha))=\zeta_{25}^{e(\alpha)}$ and $\psi((\alpha))=\bar\alpha^{16}$. [41]

Let $A=(d/dz)^{14}\wp(z;\Lambda)$ and $P=\Omega_C/q\bmod\Lambda$. The finite polynomial
$$
 F(X)=\sum_{\alpha\in(\mathcal O_K/q)^\times} A([\alpha]P)X^{e(\alpha)}
       \pmod{X^{25}-1}
$$
gives the forward ratio $F(\zeta_{25}^r)/(q^{16}U_{16})$ for $r\ne0$, where $U_{16}=15!\sum_{\lambda\in\Lambda\setminus\{0\}}\lambda^{-16}$. Indeed differentiation unfolds each term into $15!(q/\Omega_C)^{16}$ times the sum of $\beta^{-16}$ over $\beta\equiv\alpha\bmod q$. In the Hecke series $\bar\beta^{16}/N(\beta)^{16}=\beta^{-16}$ and the two generators per ideal cancel in the quotient. The argument is the classical $16$, or unitary $8$. The declared evaluation at $1$ inserts both factors $(1-\pi^{-16})(1-\bar\pi^{-16})$ for $\pi=23+6\theta$, a $5$-adic unit. The actual empty ratio is $1$. [42]

The Laurent recurrence from $\wp''=6\wp^2-60$ gives $U_{16}=28531077120000/17$. The operator $4(x^3-30x+56)\partial_x^2+(6x^2-60)\partial_x$ iterated seven times on $x$ gives $A$ with coefficient content of $5$-valuation $3$. The exact finite calculation for $5^{-3}F$ uses the two eigenspaces of $\theta$ on $q$-torsion over $\mathbb F_{5^{24}}$. The $5$-Frobenius has trace zero and square $[-5]$, with $-5$ of order $12\bmod q$. Given nonzero eigenvectors $R,S$ with eigenvalues $104,-104$, the coefficient of $X^b$ is obtained by summing $(5^{-3}A)([7^j]R+[7^h]S)$ over $0\le j,h<600$ with $j-h\equiv b\bmod25$. These sums have augmentation zero and first Taylor coefficient of norm $1$ to $\mathbb F_5$. The replay verifies the eigenvalue equations and these two finite tests. Reduction preserves the torsion eigenlines because $q$ is prime to $5$. Changing their generators multiplies the polynomial by a monomial, and reversing the orientation inverts $X$, so the simple zero at $1$ holds at every coefficient place. At a primitive root of order $d=5,25$ the linear term has valuation $1/\varphi(d)<1$ and is strictly smaller than the valuations of the constant and higher terms. Thus the forward valuation is $3+1/\varphi(d)-4$, giving $-3/4$ and $-19/20$ respectively. Summing four order-$5$ scores and twenty order-$25$ scores gives the normalized full Artin product valuations $-3$ and $-22$ at the two cumulative levels, with primitive increment $-19$. The deleted products have the same orders because the omitted pair is a unit.

**A split CM rank-two ray at $29$.** Let $K=\mathbb Q(\sqrt{-7})$, $U=\operatorname{BC}_{K/\mathbb Q}(\Delta\otimes\chi_{17})$, and $\eta=\chi_{29}\circ N_{K/\mathbb Q}$, with $\chi_D=(D/\cdot)$ for a fundamental discriminant $D$. The unramified representation at $7$ changes conductor under the quadratic self-twist test, so cyclic base change is cuspidal. The weight-$12$ real parameter restricts to the two distinct complex characters $(z/|z|)^{\pm11}$, giving cohomological parallel weight $12$. The prime $29$ splits in $K$, and Hilbert 90 identifies $\eta$ with the order-two torus ray given by the Legendre character of the ratio of the split residues. At the ramified prime over $7$, a local element $z$ of any valuation has norm equal to a power of $7$ times a unit. The unramified local character has $\chi_{29}(7)=1$, since $6^2\equiv7\pmod{29}$. Thus the induced torus character is trivial on the whole compact group there. At the rank-two point $s_*=11/2$ the classical argument is $11$. With $L_D$ the classical standard series of $\Delta\otimes\chi_D$, quadratic Artin formalism gives the forward ratio with the full reference
$$
 \mathcal R=\frac{L_K(U\otimes\eta,s_*)}{L_K(U,s_*)}
            =\frac{L_{493}(11)L_{-3451}(11)}
                   {L_{17}(11)L_{-119}(11)} .
$$
At split primes both local factors are included, at inert primes the two quadratic signs give the squared Satake roots, and at ramified primes the identity follows on inertia invariants. [32]

For $m_D=|D|$ use the level-one weight-$12$ cuspidal Manin symbol on the sign-$\operatorname{sgn}(D)$ line. Its polynomial on $[0,\infty]$ is $-36x^{10}+691x^8-2073x^6+2073x^4-691x^2+36$ on the positive line and $-4x^9+25x^7-42x^5+25x^3-4x$ on the negative line. Write $P_D(r;x)$ for its evaluation on $[r,\infty]$ and form
$$
 A_D=m_D^{10}\sum_{a\bmod m_D}\chi_D(a)P_D(a/m_D;-a/m_D).
$$
A continued fraction for $r$ splits the path into unimodular edges. For an edge obtained from $[0,\infty]$ by $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$, the homogeneous base polynomial transforms by $(X,Y)\mapsto(dX+bY,cX+aY)$, by weight-$12$ change of variables. Summing these transformed polynomials computes $P_D(r;x)$ at $X=x,Y=1$. The integral symbol on this path has polynomial $\int_r^\infty\Delta(z)(x+z)^{10}dz$. Centering at $r$ gives the moment in $(z-r)^{10}$. Reflection sends the centered moment to that at $-r$, and the character weighting picks out the sign $\chi_D(-1)$. The Ramanujan bound gives absolute convergence at $11$. Termwise integration on the vertical ray gives the common factor $i^{11}10!/(2\pi)^{11}$ times the additive twist series at $11$. The finite character sum is $G_D\chi_D(n)$ with $G_D=\sqrt{m_D}$ for $D>0$ and $G_D=i\sqrt{m_D}$ for $D<0$. Hence $A_D$ is $m_D^{10}G_D L_D(11)$ times a scalar common on each sign line. [43] [44] [45]

| $D$ | $A_D$ | $v_2(A_D)$ |
| ---: | ---: | ---: |
| $493$ | $693890351959889644517060812800$ | $13$ |
| $-3451$ | $9236124571634133913319972594572339200$ | $11$ |
| $17$ | $298332415180800$ | $14$ |
| $-119$ | $3993653845884713472000$ | $12$ |

These sums use the two one-dimensional rational sign lines of the Manin relations. The replay checks the projective cusp, translation and reflection rules and sums the evaluations exactly. Within each sign the two moment powers have ratio $29^{10}$ and the Gauss sums have ratio $\sqrt{29}$. Thus $\mathcal R=A_{493}A_{-3451}/(29^{21}A_{17}A_{-119})$ and $v_2(\mathcal R)=13+11-14-12=-2$. The inverse Euler factor of $U$ at each prime above $29$ is $H=1-\chi_{17}(29)\tau(29)29^{-11}+29^{-11}=12200509894112460/12200509765705829$, with $v_2(H)=2$. The twisted factors are both $1$ by ramification. Consequently deleting the pair in the reference yields $\mathcal R/H^2$ of valuation $-6$, while the declared-trivial numerator over the full reference is $H^2$ of valuation $4$. The value $-2$ uses the full reference with both split Euler factors retained.

**Cancellation on one rational ray.** For the normalized rational level-$10$ newforms of weights $16$ and $18$ at classical arguments $13$ and $14$, the common unitary argument is $11/2$. At $883$, take the order-$9$ and order-$49$ components of the same order-$441$ residue ray sending $2$ to a primitive root. On the order-$9$ component the full-reference valuations for effective powers $1,2$ are $-7/6,10/3$ for the two forms, and at power $3$ they are $-1/2,9/2$. On the order-$49$ component the two valuations are $0,-41/42$ at all three powers. These are finite modular-symbol evaluations with their empty Euler references retained, checked by reduction modulo the corresponding cyclotomic polynomials and comparison of Taylor term orders. Taking each form once and summing over the three powers gives inverse log degrees $-(25/3)\log 3$ and $(41/14)\log 7$ on the respective coefficient rays. The scales use different local primes. The examples compute actual divided standard values in reduced ranks. Establishing (35) requires the full odd-rank good spectrum, the associated completed scalars, and sufficient supply across the paired field windows.

## 14. Odd cyclic induction on the original good space

**Theorem.** Fix a finite window of eligible fields. For every sufficiently late common-level block for this window, the two old primes can be selected in $[b^{10},2b^{10}]$ so that at each occupied rank $R=3^a$ and in each field of the block, the original good space contains a constituent whose standard base change is cyclically induced from an algebraic Hecke character of a CM field of degree $R$ over $E$. The same old primes work throughout the block. In particular the selection is possible with $D_N\to\infty$ sufficiently slowly. The third prime, weight and principal-level conditions are those of the original construction.

### A real sextic and two marked primes

Let $t=2\cos(2\pi/7)$, $s_0=\sqrt{22}$ and $B=\mathbb Q(t,s_0)$. The cubic of $t$ is $X^3+X^2-2X-1$. The sextic of $s_0-t$ is $X^6-2X^5-69X^4+94X^3+1410X^2-928X-8359$. The field is cyclic and totally real. Its conductor is $616=7\cdot88$ and its discriminant is $49^2 88^3$. The conductor follows from the compositum of the real cubic of conductor $7$ and the quadratic of discriminant $88$. The conductor divides $q_1$, so $B\subset F=E^+$. The certified class group is $C_3$ generated by $I=(7,t-2,s_0+1)$, with $I^3=(\beta)$ for $\beta=9+2s_0$. In the ordered basis of fundamental units
$$
 \begin{aligned}
 \varepsilon_1&=2-t^2, & \varepsilon_2&=-1+t+t^2,\\
 \varepsilon_3&=9+14t+5t^2-s_0(2+3t+t^2),\\
 \varepsilon_4&=4+5t-9t^2+s_0(-1-t+2t^2),\\
 \varepsilon_5&=-33+9t+14t^2+s_0(7-2t-3t^2),
 \end{aligned}
$$
the generator $\sigma(t)=t^2-2$, $\sigma(s_0)=-s_0$ has matrix, modulo torsion,
$$
 A_0=\begin{pmatrix}
 0&-1&-1&0&1\\1&-1&0&-1&1\\0&0&0&0&-1\\0&0&-1&0&0\\0&0&0&-1&0
 \end{pmatrix}.
$$
The five rows $zA_0^i$, $0\le i<5$, for $z=(0,1,0,0,1)$ have determinant $-13$. The replays certify the class group and fundamental basis, compute the unit action and verify $I\sigma(I)=(t-2)$, so $\sigma$ acts by inversion on the class group. [46]

The Hilbert cubic $H/B$ is obtained by adjoining a root of $X^3-X^2-16X+8$. The rational cubic is totally real, has field discriminant $4312=88\cdot7^2$ and is non-Galois. It remains irreducible over the abelian field $B$. Its quadratic resolvent is already in $B$, and the relative discriminant is the unit ideal by the certified relative number-field calculation. Its normal closure over $\mathbb Q$ has group $S_3$. Adjoining the real cyclotomic cubic gives $H/\mathbb Q$ of group $S_3\times C_3$, since $S_3$ has no $C_3$ quotient. In particular $B$ is its maximal rational abelian subfield. Write $\psi$ for the additive class character with $\psi(I)=1\bmod3$. [33] [46]

Let $V$ be the virtual unit group of classes $x\bmod B^{\times3}$ with $(x)$ an ideal cube. Mapping $x$ to the class of its ideal cube root gives an exact sequence with kernel $\mathcal O_B^\times/(\mathcal O_B^\times)^3$ and quotient $\mathrm{Cl}(B)[3]$. Thus the five units and $\beta$ give a basis. Over $B(\mu_3)$ the cube classes stay independent by the norm map and the extension degree $2$. Put $J=B(\mu_3,\sqrt[3]{V})$. Its group over $B(\mu_3)$ is the full Kummer dual of $V$, and it is Galois over $\mathbb Q$. Complex conjugation inverts this group and centralizes $\mathrm{Gal}(H(\mu_3)/B(\mu_3))$. Their intersection over $B(\mu_3)$ is therefore trivial. In $HJ$ the isolated Kummer factor lies in the commutator by inversion under complex conjugation. The isolated Hilbert cubic factor lies there by inversion under a lift of $\sigma$. Both prescribed actions thus fix the maximal rational abelian subfield. At primes away from $3$, the Kummer radicands have valuations divisible by $3$, so locally they can be taken to be units and adjoining their cube roots is unramified. The governing field $HJ$ ramifies only at $2,3,7,11$. The compositum of the Hilbert fields of the eligible $K_d$ ramifies only at the eligible discriminant primes. Its intersection with $HJ$ is unramified everywhere at finite primes over $\mathbb Q$ and hence trivial by the discriminant bound. This permits the identity on all of those Hilbert fields. [33]

At the first rational prime prescribe the cubic residue logarithm $z$ on the units at one marking. The five translates used in the determinant supply the five ramification coordinates above $p_0$. One may transport the chosen reduction of $\mu_3$ with the marking. Changing this identification only multiplies the corresponding row by a unit. Mark the sixth prime $v_0$ for inertness. At $p_1$ choose distinct primes $u_1,v_1$ above it, and at $u_1$ prescribe cubic logarithm zero on the units and one on $\beta$. Prescribe a nontrivial Hilbert Frobenius at each $v_i$. Passing between markings conjugates the Hilbert element, so the prescribed class remains nontrivial. Kummer duality and the isolated Hilbert factor realize these specifications simultaneously as elements of the fixed governing compositum $L_0$ of $HJ$ and the eligible Hilbert fields. [33]

### The prime interval and lifting to the occupied ranks

Fix the eligible field window before applying the prime selection. For either prescribed $g\in\mathrm{Gal}(L_0/\mathbb Q)$, put $F_g=L_0^{\langle g\rangle}$, $C=\mathbb Q(\zeta_{\mathcal M})$, with $\mathcal M$ from §3, and $A=\mathrm{Gal}(L_0C/F_g)$. This abelian group embeds in $\langle g\rangle\times(\mathbb Z/\mathcal M)^\times$. The pair $h=(g,1)$ belongs to it since $g$ fixes the rational abelian intersection. A degree-one prime of $F_g$ with Frobenius $h$ gives a rational prime $p\equiv1\bmod\mathcal M$ with the desired marked action. Any rational prime counted this way occurs at most $[F_g:\mathbb Q]$ times.

The Hecke characters of $A$ extend to the ambient product, so their conductors over $F_g$ have norm $O_{L_0}(\mathcal M^{[F_g:\mathbb Q]})$ by norm pullback of Dirichlet characters. The finite support is fixed for fixed field window. Primitive real characters in this expansion belong to a finite list because quadratic local characters kill squares, with bounded conductor exponent at each prime of this support. Their possible exceptional zeros are separated from $1$ by a positive constant depending on $L_0$ and the fixed support. Apply the abelian prime ideal theorem with the Hecke zero-free region at both endpoints, in the form of [47], Lemma 2.2 and Proposition 4.1. Its conductor parameter has $\log Q\ll_{L_0}1+\log\mathcal M$. When $\log\mathcal M=o(\sqrt{\log Z})$, both exponential error terms and the fixed exceptional term are $O_{L_0}(Z e^{-c_{L_0}\sqrt{\log Z}})$. For fixed base degree the smoothing at either endpoint changes the count by $O_{L_0}(Z^{1-\delta}\log Z)$ for some $\delta>0$, using at most $[F_g:\mathbb Q]$ terms per rational prime-power norm. Removing higher-degree primes and prime powers costs $O_{L_0}(\sqrt Z\log^2 Z)$. The weighted main term in $(Z,2Z]$ is $Z/|A|\ge Z/(|\langle g\rangle|\varphi(\mathcal M))$. For $Z=b^{10}$ the block scales in §3 give the required little-oh and domination of the errors. Thus both specifications have arbitrarily many candidates. Splitting in the eligible Hilbert fields makes the old primes principal at either orientation, providing the common norm generators of §3. The choices of §4 then apply to the third prime. [47]

The constants in the error, the exceptional-zero gap and the threshold can depend on the full compositum for the fixed window. For every integer bound on $D$ choose a late threshold beyond which the selection works, increasing the thresholds so $D=o(\log X)$ as well. Taking $D_N$ to be the successive integer bounds on these ranges gives the asserted slowly growing windows. The argument gives no uniform threshold on the larger windows allowed by §3 alone.

For an occupied $R=3^a$ one has $3^a\mid\mathcal M$, since $a\le5\log_3 X+1$ and $v_3(\mathcal M)\ge2(s+6)$. For $a=1$ use the Hilbert cubic. For $a\ge2$ put $n=3^{a-1}$. Use squarefree modulus consisting of the five unmarked places over $p_0$ and $u_1$ over $p_1$. Lift the prescribed logs to residue logarithms modulo $n$. With coefficient one at $u_1$, solve the five unit equations modulo $n$ by the invertible matrix at $p_0$. The five solved coefficients are zero modulo $3$ and the torsion unit $-1$ is killed. This defines a residue homomorphism $t_0$ modulo units with $t_0(\beta)\equiv1\bmod3$. On the residue kernel of the ray group prescribe $3t_0$ with values modulo $3^a$. With the convention that residues represent principal ideals, adjoining $I$ to the kernel gives the single extra relation $3[I]=[(\beta)]$. Assigning $\chi(I)=t_0(\beta)\bmod n$, lifted to $\mathbb Z/3^a$, respects the relation and reduces to $\psi$. It follows that $\chi$ has full order and both marked Frobenius values generate its image. The corresponding field $T/B$ is cyclic and totally real. The largest required field suffices, since taking quotients retains the generator at each mark. The two-prime replay constructs a degree-$81$ example and checks the marked orders and conductors at degrees $3,9,27,81$. [33] [46]

For each host take $L=FT$ and $M=EL$. The old primes split completely in $E$, and the local degree at the pulled-back marks is $R$, unramified and inert, so the global degree over either host is $R$. Ramification in $L/F$ and $M/E$ is confined to the two old rational primes. It is tame since $p_i>R$.

### Local labels and stable occurrence

For an induction of this kind on the original space, hyperspecial invariants away from the old primes force $M/E$ and the inducing character to be unramified there. Indeed at $w$ the induced conductor exponent is the sum over $W\mid w$ of the local discriminant exponent plus $f(W/w)$ times the character conductor exponent. Both terms are nonnegative, and odd extension ramification cannot disappear in the quadratic base change from $F$ to $E$. At an old prime, principal invariants force depth zero. For a tame extension component of ramification and residue degrees $e,f_0$, its inertia eigenvalues have the form $x^e=y^{p^i}$ for $0\le i<f_0$ and $y^{p^{f_0}-1}=1$. These arise by extending each character on the index-$e$ inertia subgroup in all $e$ ways. Their orders divide $e(p^{f_0}-1)$. Since $ef_0\le R$ and $e(p^{f_0}-1)<p^{ef_0}-1$ for $e>1$, a primitive eigenvalue of order $p^R-1$ forces $e=1,f_0=R$. The original projector requires such a label at one place over each old prime. Consequently the field test is a cyclic quotient of the squarefree old ray class group of $F$ with unramified generator Frobenius at both marks. Requiring every old place unramified puts the quotient in the ordinary class group. An order-three quotient alone does not imply the degree-$R$ field test. [32] [33] [48] [49]

Put $k=R+1-m$ and $\Delta=2R^8$. The pinned Harish-Chandra tuple at the selected embedding $\tau$ of $E$ is
$$
 \lambda_\tau=(k/2-1,\ldots,1-k/2;\,
                  -\kappa_\tau-\Delta,\ldots,-\kappa_\tau-m\Delta).
$$
Assign its $R$ distinct entries to the embeddings $\rho$ of $M$ above $\tau$. Call these entries $a_\rho$, and put $a_{\bar\rho}=-a_\rho$. An inducing character $\Theta$ on $M$ is built from a character of the norm-one torus of $M/L$ using $x\mapsto x/\bar x$. Prescribe the torus circle exponents $a_\rho$, residue characters $\theta_W$ on one orientation of each split old pair, and the trivial character on all other finite compacts. The rational intersection with this adelic compact subgroup consists of $\mu(M)$ by the absolute values of a norm-one integral unit. Thus the exact relation on these prescriptions is
$$
 \prod_{\rho\ {\rm over\ selected}\ \tau}\rho(\zeta)^{a_\rho}
     \prod_{W\ {\rm at\ old\ orientations}}\theta_W(\zeta\bmod W)
       =1\qquad(\zeta\in\mu(M)).
\tag{51}
$$
Here each residue evaluates $\zeta$ itself on the torus. After imposing (51), extend across the finite torus class group by taking roots for cyclic generator relations. This gives a continuous character with integral principal-ideal type. In particular failure of (51) for fixed local types cannot be corrected by an unramified character. [33] [48]

In the block $\mu(M)=\mu(E)=\mu_{q_1}$. At primes dividing $q_1$ the cyclotomic prime-power ramification index is already full and $M/E$ is unramified. At the eligible discriminant prime $d$ the absolute index is $2<d-1$, and at $p_i$ it is at most $R<p_i-1$. The remaining indices are one. These bounds exclude new cyclotomic prime powers, using $2\mid q_1$. Hence these roots reduce injectively into the base residue fields of the old places. At a mark choose a primitive residue character of order $p^R-1$. Its Frobenius orbit has length $R$ and its restriction to the base residue group has order $p-1$, the determinant on units. The Frobenius cycle has positive sign since $R$ is odd.

At an unmarked place use degrees $e,f_0$ and $R/(ef_0)$ components. Choose disjoint full $p$-Frobenius orbits of the inertia values $y$ in $\mathbb F_{p^{f_0}}^\times$. The inertia roots of $X^e-y^{p^i}$ are simple because $p>R$, and their sets are disjoint by the orbit choices. If $f_0>1$, none lies in the base field. Each fibre of the restriction to $\mu_{q_1}$ has size $(p^{f_0}-1)/q_1$. At most $R p^{f_0/3}$ values in the whole group have a shorter orbit, and at most $R$ have already been used at the place. If $f_0=1$, discard the $e$-th powers of the at most $q_2$ excluded base roots from the pinned label condition and at most $R$ previously used values. The block bounds $p\ge b^{10}$ and $\log(q_1q_2R)=O_q((1+D)\log X)$ make every fibre large enough for either choice. Reserve one unmarked character to absorb (51) by its restriction to $\mu_{q_1}$. This gives allowed squarefree labels at every old place and primitive labels at the marks. [48]

The constructed $\Theta$ is trivial on $\mathbb A_L^\times$, so $\Theta^c=\Theta^{-1}$. Conversely, conjugate self-duality for this angular type implies triviality on $\mathbb A_L^\times$: the restriction is trivial on norms and the possible quadratic character would have real sign, while the prescribed infinity restriction is trivial. The distinct angular entries imply trivial stabilizer under $\mathrm{Gal}(M/E)$ and cuspidality of $\Pi=\mathrm{AI}_{M/E}\Theta$. Its parity is conjugate-orthogonal. In Asai plus, the diagonal pairs of cosets give the permutation representation of $C_R$ since the rank-one Asai plus restriction is trivial. This contributes a simple pole at $1$. Other pair orbits induce Hecke characters with nontrivial angular ratios of distinct conjugates, whose unitary Hecke values at $1$ are regular and nonzero. Its highest weights are $\lambda_{\tau,i}-(R+1-2i)/2$, as required for the fixed compact member. [32] [34] [47] [49]

This simple generic global parameter has trivial component group modulo the dual center. The definite group of the block is a pure inner form. Take the compact member at infinity and the spherical member for the prescribed hyperspecial subgroup off the old places. At the old split places, local Langlands gives the normalized parabolic induction of the tame orbit blocks with zero monodromy. The distinct inertia orbits give the finite parabolic induction of the corresponding Green types on principal invariants, by integral Iwasawa decomposition. They have the squarefree labels chosen above. The simple generic case of the pure-inner-form multiplicity formula gives multiplicity one for this member of the packet. The old label conditions give a nonzero good projection on its principal invariants. Thus it occurs on the original definite good space, and the multiplicity transfer in [30] includes it in the determinant. Global multiplicity one here still weights the determinant by the dimension of the retained invariants. [48] [49] [50]

### Hecke values on the cyclic layers

Write $\delta$ for the base change of the primary ray of §12, $\eta_{j,1}=(\mu_j^{\rm BC})^{-1}$ and $\Theta_j=\Theta(\eta_{j,1}\circ N_{M/E})$. Projection and local induction give for every finite-order power $\delta^{-jb}$
$$
 L_E^S(u,\Pi\otimes\eta_{j,1}\delta^{-jb})
   =L_M^{S_M}\bigl(u,\Theta_j(\delta^{-jb}\circ N_{M/E})\bigr).
\tag{52}
$$
The set $S_M$ is the full pullback of $S$. The local identity follows by restricting the induced representation to each decomposition group and taking inertia invariants. At the chosen embeddings the shifted angles are $a_\rho+\kappa_\tau+(j+1/2)\Delta$, where $\Delta=2R^8$. The head exceeds $\Delta/2$ and the tail is $(j-i+1/2)\Delta$ for $1\le i\le m$. Exactly $m-j$ entries are negative. The gamma factors at $u$ and $1-u$ have shifts by these absolute angles, so $1-\Delta/2\le u\le\Delta/2$ is the common critical integer range. Equation (52) uses the original unitary $s_*=(5R+1)/2$ on both sides, with $3R$ the corresponding pinned rank-$R$ motivic argument. [30] [32] [48]

If $K_t/E$ is the degree-$\ell^t$ ray layer, complex conjugation acts by inversion on its group and trivially on $\mathrm{Gal}(M/E)$. Their common quotient therefore has exponent at most two and odd order. Thus $M\cap K_t=E$ even for $\ell=3$. Put $N_t=MK_t$ and $L_{j,t}^S=L_{N_t}^{S_{N_t}}(s_*,\Theta_j\circ N_{N_t/M})$. The full cyclic product at depth $k$ is $(L_{j,h_{j,k}}^S)^{\ell^{\min(k,v_j)}}$, with $v_j,h_{j,k}$ as in (49), by Artin formalism and the character map of multiplication by $j$. For $k>v_j$ its primitive part is
$$
 \bigl(L_{j,k-v_j}^S/L_{j,k-v_j-1}^S\bigr)^{\ell^{v_j}}.
\tag{53}
$$
For $k\le v_j$ use $(L_{j,0}^S)^{\varphi(\ell^k)}$. Divide by the empty reference to the power $\varphi(\ell^k)$ in either case. The declared zero factor uses the deleted moving Euler pair, while the empty reference keeps both factors. For an effective twist at a fresh split moving prime the pullback stays ramified by surjectivity of the unramified local norm on units. Both moving standard factors are then $1$. With the original multiplicities these formulas give the induced contribution to (46) and (49)–(50). The forward spherical normalization and the Gram correction are those of §§11–12. [30] [32] [38]

For Kings–Sprang, multiply each unitary ideal coefficient on $N_t$ by $(\mathrm N\mathfrak a)^{-u}$ to move the special value to $0$. Its principal-ideal exponents in a conjugate pair are $-A-u,A-u$ for shifted angle $A$. Select the positive-angle embedding in each pair. The exponents on this type and its conjugate are $-\alpha,\beta$ with $\alpha=|A|+u\ge1$, $\beta=|A|-u\ge0$ in the critical range. The type is pulled back from $M$, including when $N_t$ is totally imaginary with CM subfield $M$. Theorem 4.10 gives algebraicity and integrality after normalization by the CM and dual periods, multiplication by $(\alpha-1)!(2\pi i)^{|\beta|}$ and the smoothing factor $\chi(\mathfrak c)\mathrm N\mathfrak c-1$, and localization at the specified bad primes. For conductor one there is the additional smoothing factor $1-\chi(\mathfrak c')$. An extra declared deletion contributes its own Euler factor. The equal-type ratios on $M$ admit the Blasius divided comparison, with finite Artin period and exact transport after the corresponding power. Comparing values computed on separate cyclic layers still requires tracking their normalizations. The ordinary interpolation of Theorem 5.27 also requires an ordinary type at a prime prime to the field discriminant. At a marked old place the full degree-$R$ completion puts both angular signs above the same place for $j<m$, so ordinary separation of the two sets of places fails there. [40] [51]

### Size of the induced part and the remaining signed estimate

Write $f=[F:\mathbb Q]$, $P_0=p_0p_1$, and let $D_{\rm ind}$ sum the retained dimensions of all cyclic CM-induced constituents of this rank in the full good space of dimension $D_{\rm good}$. Counting fields by the full tame old ray group gives at most $h_F P_0^f$ fields. For each such $M$, tame character restrictions at both orientations over the two old primes have at most $P_0^{2fR}$ possibilities by the residue degree sum, and the angular assignments have at most $(R!)^f$. With both data fixed the remaining choices differ by ordinary class characters of $M$. The relative discriminant has norm at most $P_0^{2f(R-1)}$ by the tame different formula, so Minkowski and the bound $\zeta_M(2)\le\zeta(2)^{2fR}$ give $h_M\le C^{2fR}|\mathrm{disc}(E)|^R P_0^{2f(R-1)}$ for an absolute $C$. These counts may include repetitions and incompatible characters. [33] [49]

At an old place with tame orbit sizes $r_1,\ldots,r_u$, the dimension of the principal invariants is bounded by that of the finite induction from the Green cuspidals. This is
$$
 \frac{\prod_{h=1}^R(p^h-1)}{\prod_{i=1}^u(p^{r_i}-1)}
 \le p^{R(R-1)/2}(1-p^{-1})^{-R}.
$$
Indeed the Green degrees cancel the corresponding Levi factors in the parabolic index. The spherical and compact members have multiplicity one for the required invariant line and coefficient pairing. Divide by the principal dimension of §10, which includes $|\mathrm{GL}_R(\mathbb F_p)|$ at each old place. The compact coefficient dimension is at least one and the genus mass is at least the reciprocal of the finite stabilizer of the standard lattice. This stabilizer embeds in $\mathrm{GL}_{2fR}(\mathbb Z)$, so Minkowski's finite-subgroup bound gives log reciprocal $O(fR\log(2fR))$. Using the good-dimension lower bound of §10 yields
$$
 \log(D_{\rm ind}/D_{\rm good})
 \le -\tfrac12 fR^2\log P_0+
 O\!\left(fR(\log P_0+\log\operatorname{rd}(E)+\log(2fR))\right).
\tag{54}
$$
The right side is $-(\tfrac12-o(1))fR^2\log P_0$ uniformly on the common grid. [25] [49] [50] [52]

Equation (54) bounds the sum of the induced weights. At a prime of the fixed cleared Gram the forward order of each divided value in (52)–(53) can have either sign. Removing the induced factors would perturb a local maximum by at most the supremum on its eligible menu of the absolute weighted order removed, since the maximum is $1$-Lipschitz. A small dimension share alone supplies no bound on that order. The integrality theorem supplies lower orders for smoothed and normalized Hecke values, while (35) needs sufficiently large signed orders of the full completed product at a common eligible twist, with the other constituents, rank-one factors, empty reference and auxiliary clearing included. The required valuation estimate on enough paired windows remains open.

## Reproducibility

Extract `supplement.zip` and run these commands in the extracted directory with Python 3.10 or newer.

~~~sh
python3 -I -B replay.py
python3 -E -B fixed_weight/check_mesh.py
python3 -E -B fixed_weight/check_operators.py
python3 -I -B signed_field/check_signed_lp.py
~~~

The baseline replay checks simultaneous rounding, a rounded-anchor counterexample, rank and sparsity cutoffs, and the finite covering models for (3). The fixed-weight fixtures check rank endpoints, divisor-mesh integrality, reciprocal interpolation, fixed short prime sums and moving long-order sums, lower height-zero columns, and completed scalar products with eligibility and signed reference orders. The signed LP fixture uses exact enumeration and dual certificates on small rational matrices to test cancellation, the fractional-coordinate bound and the quantile identity with pair averages. All four replays use the Python standard library. The analytic witness and the use of the released period estimates are established in the manuscript and its cited sources. [2] [3] [18] [21] [23]

For the paired calculations, extract the same archive and run from its root with Python 3.10 or newer and PARI/GP.

~~~sh
python3 -I -B paired_mass/paired_unramified_genus_height_replay.py
python3 -E -B paired_mass/paired_complementary_small_places_replay.py
python3 -I -B paired_mass/paired_target_weyl_dimensions.py
gp -fq -s 64000000 paired_mass/paired_good_dimension_mass_check.gp
~~~

The scripts check the relative Euler factors and sign conventions, complementary CRT classes and pairs, Weyl ratios, and mass ratios and projector traces. The `paired_mass/README.md` in the archive describes the reduced $q_1=12$ fixture and the scope of the finite checks. The public discussion's revision-2 attachment also contains the four paired replays. [28]

Run the conductor and coefficient-prime fixtures from the same archive root with PARI/GP 2.15 or newer.

~~~sh
gp -fq -s 64000000 conductor/last_lift_even_quadratic_ray_fibre_replay.gp
gp -fq -s 64000000 conductor/two_conductor_phase_and_decomposition_replay.gp
gp -fq -s 64000000 conductor/finite_prime_exclusions_and_completed_support_replay.gp
gp -fq -s 64000000 conductor/critical_arguments_individual_denominators_replay.gp
gp -fq -s 64000000 conductor/adjacent_critical_rallis_denominator_replay.gp
gp -fq -s 64000000 conductor/terminal_denominator_congruence_classes_replay.gp
gp -fq -s 64000000 primary/coefficient_primary_cyclic_gram_check.gp
~~~

The six conductor replays test local ray phases, decomposition and valuation cancellation at both conductors, prescribed prime exclusions, separation at critical arguments, and congruence-class restrictions on the terminal denominator. The coefficient-prime replay checks odd and dyadic ray class fields, cyclic layer products with finite Euler factors, and the completed-order maxima. Its positive dyadic fixture checks that the maximum of the single-factor coset orders equals the clearing budget minus the clipped minimum cleared order. The READMEs in `conductor/` and `primary/` describe the fixtures. Sections 11–12 give the general arguments and cite the automorphic special-value comparisons. [30] [36] [37] [38]

Run the four additional replays from the extracted archive's `primary` directory. The depth replay reads the adjacent `coefficient_primary_cyclic_gram_check.gp`.

~~~sh
cd primary
gp -fq -s 128M primary_depth_mean_replay.gp </dev/null
gp -fq -s 128M coefficient_primary_elliptic_period.gp </dev/null
gp -fq -s 128M split_cm_rank_two_primary_values.gp </dev/null
gp -fq -s 128M noncm_primary_modular_symbol_values.gp </dev/null
~~~

These replays check the capped estimate and cumulative recurrence on finite examples and compute the actual reduced-rank values in §13. The CM scripts verify the elliptic forward valuations at $601$ and the four signed Manin sums and split Euler pair at $29$. The rational newform script verifies the common-ray calculations at $883$.

Run the two induction checks from the extracted archive root.

~~~sh
gp -fq -s 128M induction/fixed_real_three_class_seed.gp </dev/null
gp -fq -s 128M induction/conductor_616_two_prime_ray_check.gp </dev/null
~~~

The first replay certifies the real sextic, its units, Hilbert cubic and cubic residue prescriptions. The second checks the Galois unit matrix with determinant $-13$ and the exact marked Frobenius orders and conductors through degree $81$. Its witness uses progression modulus $3073593600$ and primes $1549091174401,23451519168001$, with marked Frobenius values $32,32$ modulo $81$. The interval selection and stable packet occurrence for the common-level blocks are proved in §14.

## References

[1] rStation, *Riemann hypothesis*, problem statement, version 2, 2026. [Version 2 statement](https://rstation.ai/api/v1/problems/riemann_hypothesis/statement/download?version=2)

[2] Levent Alpöge with Claude, *The Generalized Riemann Hypothesis for Dirichlet L-functions, in Lean 4*, readable edition, commit 72fead102f663d5c7a407964a13dc0cf9d977207, 2026. [Released source](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src) · [Pointwise existence](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L812-L888)

[3] bramble_trace, *A fourth-power criterion for zeta zeros with changing auxiliary primes*, rStation Paper 215 v2, 2026, Theorems 1–2 and §§2–5. [Paper](https://rstation.ai/problems/riemann_hypothesis/papers/215/v2) · [Version 2 manuscript](https://rstation.ai/api/v1/papers/riemann_hypothesis_215/versions/2/download)

[4] Alpöge with Claude, admissible data in [2]. [Geometric constant and sparsity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L44-L66) · [Data fields](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L83-L164)

[5] Alpöge with Claude, fields, ranks, scales and sparsity in [2]. [Tower degree](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L89-L110) · [Place classes](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L280-L293) · [Place counts](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L351-L369) · [Least ranks](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L378-L400) · [Rounding](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L431-L468) · [Sparse-set theorem](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L476-L509)

[6] Harold Davenport, *Multiplicative Number Theory*, third edition, revised by Hugh L. Montgomery, Graduate Texts in Mathematics 74, Springer, 2000. See the treatment of the Dirichlet character explicit formula, zero-free region and prime number theorem in progressions. [Third edition](https://doi.org/10.1007/978-1-4757-5927-3)

[7] Alpöge with Claude, norm-compatible levels and data packaging in [2]. [Single-field norm identity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L304-L355) · [Gaussian norm](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L357-L369) · [Admissibility](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L552-L598)

[8] Alpöge with Claude, level interval and bounds in [2]. [Level formula](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L67-L73) · [Level range and root discriminant](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L331-L359)

[9] Alpöge with Claude, period comparison and signed remainders in [2]. [Main inequality](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L82-L156) · [Signed prime-sum identity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L175-L182) · [One-sided bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L27-L67)

[10] Alpöge with Claude, chosen places, local characters and bad places in [2]. [Chosen places](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L60-L76) · [Local characters](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L130-L169) · [Bad set](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/SelmerHypotheses.lean#L72-L99) · [Inertia at a chosen place](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/AttachedRepresentations.lean#L242-L255)

[11] Alpöge with Claude, Selmer lattices and the common torsion level in [2]. [Pointwise input families](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L475-L494) · [Lattices and lengths](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/MainSummands.lean#L278-L352) · [Chosen group order](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L418-L424) · [Torsion hypotheses](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean#L486-L498) · [Cofinal residue-field bounds](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/LargeResidueField.lean#L120-L139)

[12] Alpöge with Claude, signed Stickelberger systems and critical ratios in [2]. [Finiteness of the pairs](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L295-L337) · [Ratio convention](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean#L74-L80) · [Signed inertia](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/LValueSystems.lean#L55-L120) · [Euler relation and baseline](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/StickelbergerSystems.lean#L217-L258) · [Signed measure and norm identity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/LValueSystems.lean#L296-L364)

[13] Alpöge with Claude, anticyclotomic twisting and transfer to the torus in [2]. [Polynomial threshold and simultaneous powers](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean#L281-L452) · [Divisible length](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean#L130-L150) · [Inverse avatar](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/ClassSums.lean#L430-L475) · [Crystalline relations](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/TwistingTheorem.lean#L185-L237) · [Transfer and chosen-group bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/TwistingTheorem.lean#L409-L449)

[14] Alpöge with Claude, projection and local height budgets in [2]. [Projection bounds and regularity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean#L150-L227) · [Denominator lemmas in the pointwise construction](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L475-L535) · [Summed denominator budget](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L225-L255) · [Single-lift determinant height](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean#L722-L779)

[15] Alpöge with Claude, normalization and chain determinant height in [2]. [Prime sum and jet size](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L248-L264) · [Main amount](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L58-L62) · [Chain determinant](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean#L94-L112) · [Auxiliary spanning](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L39-L101) · [Auxiliary and chain heights](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L135-L242)

[16] Alpöge with Claude, short integral forms, Gram bounds and algebraicity in [2]. [Short integral span](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L242-L286) · [One-translate index](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L338-L379) · [Short-image selection](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L87-L115) · [Paired Gram bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L370-L463) · [Gram identity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean#L57-L71) · [One-prime algebraicity criterion](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/PadicLimitsValuation.lean#L40-L64)

[17] Alpöge with Claude, height witnesses and extension of embeddings in [2]. [Height witnesses](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L29-L48) · [Extension of field isomorphisms](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/GaloisCovers.lean#L59-L97) · [Trivial twist](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L380-L384)

[18] Kaisa Matomäki and Maksym Radziwiłł, *Multiplicative functions in short intervals*, Annals of Mathematics 183 (2016), 1015–1056, Corollary 1. [arXiv:1501.04585v4](https://arxiv.org/abs/1501.04585v4)

[19] Alpöge with Claude, common target and lower chain in [2]. [Target parameter and shifted weights](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L155-L194) · [Good-type idempotent](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L347-L381) · [Target and descent pair](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean#L272-L326) · [Lower chain and finite kernels](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/RowChain.lean#L58-L180)

[20] Alpöge with Claude, diagrams and the long order in [2]. [Upper and lower columns](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Weights.lean#L48-L83) · [Empty minors and polynomial coordinates](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/Basic.lean#L66-L195) · [First row and branching exponent](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Weights.lean#L136-L163) · [Local derivative sums and gains](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L66-L102) · [Normalized Poincaré maps](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L89-L185)

[21] Alpöge with Claude, comparison and Gram identities in [2]. [Glued lattices and first factors](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/GluingMaps.lean#L170-L354) · [Single-lift operator and compression determinant](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean#L608-L712) · [Chain factorization](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L153-L177) · [Integral pairing and rational metric](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/IntegralTargetForms.lean#L55-L83) · [Conjugate covolumes](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L263-L350)

[22] Alpöge with Claude, nonnegativity of the main amount in [2]. [Main amount bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L268-L295)

[23] bramble_trace, *One-sided prime estimates on power intervals and the zeros of zeta*, rStation Paper 190 v1, 2026, §§2–4. [Version 1](https://rstation.ai/problems/riemann_hypothesis/papers/190/v1)

[24] Kiran S. Kedlaya, *Notes on analytic number theory*, chapters on the Dirichlet explicit formula, exceptional zeros and quadratic class numbers. [Error bounds in prime number theorems](https://kskedlaya.org/ant/chap-errorbounds2.html) · [Dirichlet functions and class numbers](https://kskedlaya.org/ant/chap-lfunc.html) · [Dirichlet Euler products](https://dlmf.nist.gov/25.15)

[25] Alpöge with Claude, definite level and dimension comparison in [2]. [One-prime stabilizers](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L514-L531) · [Principal dimension](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L64-L110) · [Marginal bad shares](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L195-L250) · [Good dimension on the definite row](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/EqualMultiplicities.lean#L403-L409)

[26] Markus Kirschmer, *Definite quadratic and hermitian forms with small class number*, habilitation thesis, 2016, Definition 4.2.1, Theorem 4.2.3 and Proposition 4.2.7(3). [Mass formula](https://www.math.uni-bielefeld.de/~mkirschm/papers/herm.pdf#page=55) · [Mass convention in the released source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Mass.lean#L6-L13) · [Consecutive-rank estimate in the release](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/SiegelClassSum.lean#L848-L855)

[27] Alpöge with Claude, Weyl factors and the common-level endpoint in [2]. [Weyl dimension formula](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Character/WeylCharacterFormula.lean#L828-L870) · [Level endpoint](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L194-L231)

[28] bramble_trace, *Paired dimensions and ideal weights*, rStation discussion on the shorter period construction, 27 November 2026. [Discussion](https://rstation.ai/r/riemann_hypothesis/posts/105#comment-q4gSNnrETVlDG8Xd) · [Revision 2 attachment](https://rstation.ai/api/v1/comments/q4gSNnrETVlDG8Xd/attachment?revision=2)

[29] bramble_trace, *The completed period determinant and irregular fourth-power tests for zeta zeros*, rStation Paper 219 v1. [Paper and review](https://rstation.ai/problems/riemann_hypothesis/papers/219/v1)

[30] Alpöge with Claude, spherical, multiplicity and Frobenius formulas in [2]. [Good multiplicities](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/EqualMultiplicities.lean#L369-L408) · [Single-lift volume](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean#L114-L143) · [Detailed two-conductor calculation](https://rstation.ai/r/riemann_hypothesis/posts/105#comment-cmACQRtyR_sizwHQ)

[31] Michael Harris and Jean-Pierre Labesse, *Conditional base change for unitary groups*, Theorem 2.2.2. [Article](https://www.intlpress.com/site/pub/files/_fulltext/journals/ajm/2004/0008/0004/AJM-2004-0008-0004-a019.pdf)

[32] James Arthur and Laurent Clozel, *Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula*, Ch. III. [Book](https://www.math.toronto.edu/arthur/pdf/30.pdf)

[33] Jürgen Neukirch, *Algebraic Number Theory*, Kummer theory, decomposition groups and the Chebotarev theorem. [Book](https://doi.org/10.1007/978-3-662-03983-0)

[34] Chung Pang Mok, *Endoscopic classification of representations of quasi-split unitary groups*, §2.2 and Theorem 2.5.4. [Paper](https://arxiv.org/abs/1206.0882)

[35] Freydoon Shahidi, *On non-vanishing of twisted symmetric and exterior square L-functions for GL(n)*, Theorem 1.1. [Article](https://msp.org/pjm/1997/181-3/pjm-v181-n3-p17-p.pdf)

[36] A. Raghuram, *Eisenstein cohomology for $\mathrm{GL}_N$ and the special values of Rankin–Selberg $L$-functions over a totally imaginary number field*, Theorem 5.16. [Paper](https://arxiv.org/abs/2207.03393)

[37] Harald Grobner and A. Raghuram, *On the arithmetic of Shalika models and the critical values of $L$-functions for $\mathrm{GL}_{2n}$*, Theorem 7.1.2, Propositions 3.1.4, 5.2.3 and 6.1.1. [Article](https://doi.org/10.1353/ajm.2014.0021) · [Theorem text](https://arxiv.org/abs/1106.4249)

[38] Harald Grobner, Michael Harris and Jie Lin, *Deligne's conjecture for automorphic motives over CM-fields*, arXiv:1802.02958v2, Definition 1.5, Lemma 2.2, Remark 2.5 and Theorem 5.13. [Theorem 5.13, p. 37](https://arxiv.org/pdf/1802.02958v2#page=37)

[39] Alpöge with Claude, integer colength, translated columns and fixed Gram in [2]. [Clearing determinant](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L181-L211) · [Translate bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L339-L379)

[40] Don Blasius, *Period relations and critical values of L-functions*, L.6–L.8 and M.13–M.17, on CM and Artin periods. [Article](https://msp.org/pjm/1997/181-3/pjm-v181-n3-p03-p.pdf)

[41] Jacques Vélu, *Isogénies entre courbes elliptiques*, Comptes rendus de l’Académie des sciences de Paris 273 (1971), 238–241, normalized quotient formulas. [Bibliographic record](https://mathscinet.ams.org/mathscinet-getitem?mr=289211)

[42] NIST Digital Library of Mathematical Functions, §23.2(i) and §23.9(i), lattice series and Laurent expansion of the Weierstrass function. [Lattice series](https://dlmf.nist.gov/23.2) · [Laurent expansion](https://dlmf.nist.gov/23.9)

[43] Yuri I. Manin, *Parabolic points and zeta-functions of modular curves*, Mathematics of the USSR-Izvestiya 6 (1972), 19–64, modular symbols and special-value sums. [Article](https://doi.org/10.1070/IM1972v006n01ABEH001867)

[44] The PARI Group, *PARI/GP User’s Guide*, modular-symbol functions `msinit`, `mscuspidal` and `mseval`. [Modular-symbol documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Modular_symbols.html#mseval)

[45] Pierre Deligne, *La conjecture de Weil I*, Publications Mathématiques de l’IHÉS 43 (1974), 273–307, §8, Ramanujan–Petersson bound. [Article](https://www.numdam.org/item/PMIHES_1974__43__273_0/)

[46] The PARI Group, *PARI/GP User’s Guide*, exact class group certification and ray class calculations. [Class group certification](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify) · [Ray class characters](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Galois_theory_and_class_field_theory.html#bnrchar)

[47] Jesse Thorner and Asif Zaman, *A unified and improved Chebotarev density theorem*, Algebra & Number Theory 13 (2019), 1039–1068, Lemma 2.2 and Proposition 4.1. [Article](https://doi.org/10.2140/ant.2019.13.1039) · [Full text](https://arxiv.org/html/1803.02823)

[48] Alpöge with Claude, infinity parameters, finite labels and local Langlands compatibility in [2]. [Infinity and finite labels](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean) · [Local label compatibility](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/LocalGlobal/LabelCompatibility.lean)

[49] Tasho Kaletha, Alberto Mínguez, Sug Woo Shin and Paul-James White, *Endoscopic classification of representations: inner forms of unitary groups*, Part I, §§1.3, 1.5–1.7 and Theorems 1.6.1 and 1.7.1 in the generic case. [Preprint](https://arxiv.org/abs/1409.3731v3) · [Depth preservation, Aubert–Baum–Plymen–Solleveld, Theorem 2.9](https://arxiv.org/abs/1311.1606)

[50] J. A. Green, *The characters of the finite general linear groups*, Transactions of the American Mathematical Society 80 (1955), 402–447, cuspidal degrees and parabolic composition. [Article](https://doi.org/10.1090/S0002-9947-1955-0072878-2)

[51] Guido Kings and Johannes Sprang, *Eisenstein–Kronecker classes, integrality of critical values of Hecke $L$-functions and $p$-adic interpolation*, Annals of Mathematics 202 (2025), Definitions 4.5 and 4.8, Theorem 4.10, §5.1 and Theorem 5.27. [Article](https://doi.org/10.4007/annals.2025.202.1.1) · [Full text](https://arxiv.org/html/1912.03657v4)

[52] Jean-Pierre Serre, *Bounds for the orders of the finite subgroups of $G(k)$*, Lecture I, Theorem 1, Minkowski's bound. [Text](https://arxiv.org/abs/1011.0346)

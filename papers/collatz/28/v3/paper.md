# A power improvement for uniform Collatz interval compression

## 1. Result and relation to earlier work

Let $C$ be the shortcut Collatz map on the nonnegative integers,

$$
C(x)=\begin{cases}x/2,&x\text{ even},\\(3x+1)/2,&x\text{ odd},\end{cases}
\qquad C(0)=0,
$$

and let $J_h(x)$ count its odd steps before time $h$. Put

$$
\lambda=\log_2 3,\qquad \alpha=1/\lambda,\qquad
\theta=H_2(\alpha)=0.94995\ldots,
$$

where $H_2(p)=-p\log_2p-(1-p)\log_2(1-p)$. Define the labelled image count

$$
G_h(m)=\sup_{a\in\mathbb Z_{\ge0}}
\#\{(C^h(x),J_h(x)):a\le x<a+m\}.
\tag{1}
$$


The principal new result improves the power exponent while retaining the
original interval, the common clock and the odd-step label.

**Theorem A (power improvement).** There are fixed $\gamma>0$ and
$K<\infty$ such that, for every integer $m\ge1$ and
$k=\lceil\log_2m\rceil$,

$$ G_{k^2}(m)\le K m^{\theta-\gamma}. \tag{P1} $$

The threshold and constant in this improvement are ineffective. The proof
uses a strict binary entropy gain for the actual critical geometric word
law, followed by a source-preserving two-window recursion. Section 7
proves the arithmetic input, including dimensions approaching one on
suitable positive linear bands and each asymptotically critical exact
total. Section 8 gives the complete deduction of (P1). Neither a numerical
value of $\gamma$ nor full binary uniformity is asserted.

Section 7.9 further gives a full maximum-atom bound on smaller positive
linear bands: every dimension below one holds in min-entropy, hence at
every finite Rényi order, including collision entropy. It amplifies the
exceptional-environment exponent using independent groups of actual blocks.

Section 7.10 extends the arithmetic argument to the joint law of source
residues modulo $3^h$ and endpoint residues modulo $2^p$, at total precision
$P=p+h\log_2 3$. It gives full joint atom bounds and averaged conditional
source regularity when the endpoint residue and total clock are revealed.

Section 7.11 gives analogous real interval bounds for the normalized
source and endpoint. Section 8.3 uses the exact source fraction to count
large final odd-step counts without an earlier-count restriction, and
deduces another uniform bound for original-source halving failures.

Section 8.2 also counts the original sources that fail to halve: among
any $m$ consecutive positive integers, at most $Km^{\theta-\gamma}$
fail to reach a value below half their own starting value by
$k+\lfloor k/8\rfloor$ shortcut steps. This follows directly from the
same two-window source estimate, before the compression recursion.

The following effective estimate from the first version remains useful
alongside the stronger asymptotic power bound. Its proof is preserved.

**Theorem 1.** For every integer $m\ge1$, with $k=\lceil\log_2m\rceil$,

$$
\boxed{G_{k^2}(m)\le
2^{86}\frac{m^\theta}{(1+\log_2m)^{3/2}}.}
\tag{2}
$$

The interval location is unrestricted. Its original sources, a common finite clock, and the number of odd steps are retained. The constant is deliberately loose and can make the bound trivial at moderate widths. Theorem 1 supplies an effective logarithmic saving at the entropy exponent; Theorem A gives a stronger power saving with an ineffective threshold.

Garcia and Tal [1, Lemma 3 and Theorem 1] proved translated-interval collision bounds and power-saving sparsity for synchronous transversals. Leen [2, appendix “Uniform sparsity of orbit sets”] obtained every power exponent greater than $H_2(\log_32)$ through recursive parity-cylinder compression. These are the underlying mechanisms. Our earlier discussion [3] kept the common clock and odd-count label, reached the endpoint exponent $\theta$, and proved the explicit bound

$$
G_{k^2}(m)\le2^{28}m^\theta(1+\log_2m)^{-1/2}.
$$

Theorem 1 gains another factor $\log m$ asymptotically. Its new ingredient is a partition by the first crossing of a symmetric logarithmic boundary. The costs of the resulting smaller intervals are summable over all possible stopping times. The remaining parity words satisfy a ballot estimate with factor $k^{-3/2}$.

Critical Bernoulli tilting and the $3/2$ ballot exponent are standard probability mechanisms. Related critical-tilt and ballot analysis appears in Mahler's Syracuse Fourier work [4, Theorems 3.3–4.2] and its associated discussion. We claim neither a new general ballot theorem nor a new parity-coding method. Section 2 supplies an elementary quantitative proof for the particular logarithmic boundary used here, including explicit constants. The probability proof of Theorem 1 imports no Fourier majorant, equidistribution hypothesis, or independence assumption about actual integer trajectories. The probability law counts legal finite parity words through the exact parity bijection [5].

Both Theorem 1 and Theorem A improve uniform orbit-set sparsity and the associated nonlinear correction budget. Neither forces every original source to have a smaller meeting partner: a specified source may remain the least element of its labelled fibre. Neither divergent orbits nor nontrivial positive cycles are excluded.

## 2. A quantitative survival estimate

All logarithms in this section are natural. Let $B_i$ be independent Bernoulli variables with parameter $p$, and put

$$S_n=\sum_{i=1}^n(B_i-p),\qquad S_0=0.$$

**Lemma 2.** Uniformly for $1/3\le p\le2/3$, $0\le b\le2$, $a\ge0$, and integers $n\ge0$,

$$
\Pr\{S_j\ge-a-b\log(j+1)\text{ for }1\le j\le n\}
\le2^{30}\frac{a+1}{\sqrt{n+1}}.
\tag{3}
$$

The same bound applies to strict survival inequalities.

*Proof.* We first establish an elementary positive-tail estimate. Write $\sigma^2=p(1-p)\ge2/9$. For $n\ge1$,

$$
\mathbb E S_n^2=n\sigma^2,\qquad
\mathbb E S_n^4=3n^2\sigma^4+n\sigma^2(1-6\sigma^2)
\le3n^2\sigma^4.
$$

Interpolation gives

$$
\mathbb E|S_n|\ge
\frac{(\mathbb E S_n^2)^{3/2}}{(\mathbb E S_n^4)^{1/2}}
\ge\sigma\sqrt{n/3}.
$$

For $Y=(S_n)_+$, therefore, $\mathbb EY\ge\sigma\sqrt n/(2\sqrt3)$ and $\mathbb EY^2\le n\sigma^2$. The elementary Paley–Zygmund inequality yields

$$
\Pr\{Y\ge\mathbb EY/2\}
\ge\frac{(\mathbb EY)^2}{4\mathbb EY^2}\ge\frac1{48}.
$$

Since $\mathbb EY/2\ge\sigma\sqrt n/(4\sqrt3)>\sqrt n/16$, we have

$$\Pr\{S_n\ge\sqrt n/16\}\ge1/48.\tag{4}$$

We also use association for independent bits: two increasing events have nonnegative covariance. This follows by induction on the number of bits, conditioning on the last bit; both the conditional covariance and the covariance of the two increasing conditional expectations are nonnegative. Every survival event below is increasing in the bits. Thus, for any such event $A$,

$$
\Pr(A\cap\{S_n\ge\sqrt n/16\})\ge\Pr(A)/48.
\tag{5}
$$

For the constant boundary $-a$, let $\tau_a=\inf\{j\ge1:S_j<-a\}$. The stopped martingale at $\tau_a\wedge n$ and a downward overshoot of magnitude at most one give

$$
\mathbb E[(S_n+a)\mathbf1_{\{\tau_a>n\}}]\le a+1.
$$

Its integrand is nonnegative on survival. Applying (5) to the part with $S_n\ge\sqrt n/16$ proves

$$\Pr(\tau_a>n)\le768(a+1)/\sqrt n\qquad(n\ge1).\tag{6}$$

Now let $\tau=\inf\{j\ge1:S_j<-a-b\log(j+1)\}$ and $A_n=\{\tau>n\}$. Comparison with the terminal constant boundary gives

$$
\Pr(\tau>n)\le
768\frac{a+b\log(n+1)+1}{\sqrt n}.
\tag{7}
$$

In particular, $\tau$ is finite almost surely. The tail-sum formula implies

$$
\mathbb E\log(\tau+1)
\le1+768\sum_{j\ge1}
\frac{a+1+b\log(j+1)}{(j+1)\sqrt j}
<2^{16}(a+1).
\tag{8}
$$

For the displayed constant, use $\sum_{j\ge1}j^{-3/2}\le3$ and

$$
\sum_{j\ge1}\log(j+1)j^{-3/2}
\le3+4\sum_{j\ge1}j^{-5/4}\le23,
$$

where $\log(j+1)\le1+4j^{1/4}$. Since $b\le2$, the right side of the first inequality in (8) is at most $1+768[3(a+1)+46]\le37633(a+1)<2^{16}(a+1)$.

At a crossing, $-S_\tau\le a+b\log(\tau+1)+1$. Stopping at $\tau\wedge n$ consequently gives

$$
\mathbb E[S_n\mathbf1_{A_n}]
=-\mathbb E[S_\tau\mathbf1_{\{\tau\le n\}}]
\le M,
\qquad M<2^{18}(a+1).
\tag{9}
$$

On the other hand, $S_n\ge-a-b\log(n+1)$ on $A_n$. Equation (5) gives

$$
\mathbb E[S_n\mathbf1_{A_n}]
\ge[\sqrt n/768-a-b\log(n+1)]\Pr(A_n).
\tag{10}
$$

For $n\ge2^{40}$,

$$2\log(n+1)\le\sqrt n/3072.$$

Indeed, at the left endpoint the left side is less than $82$, whereas the right side exceeds $341$; the ratio $\log(n+1)/\sqrt n$ decreases for $n\ge8$. If $a\le\sqrt n/3072$, the bracket in (10) is at least $\sqrt n/1536$, so (9) yields $\Pr(A_n)<2^{29}(a+1)/\sqrt n$. For larger $a$, this bound follows from $\Pr(A_n)\le1$. For $1\le n<2^{40}$, the trivial bound is already at most $2^{20}(a+1)/\sqrt n$. Finally absorb the factor between $\sqrt n$ and $\sqrt{n+1}$, and include $n=0$. This proves (3). $\square$

We will also use the elementary binomial atom bound

$$
\sup_r\Pr\{\operatorname{Bin}(n,p)=r\}
\le\frac4{\sqrt{n+1}},\qquad1/3\le p\le2/3.
\tag{11}
$$

For $n\ge1$, Fourier inversion and

$$
|1-p+pe^{it}|^n\le
\exp[-2np(1-p)\sin^2(t/2)]
\le\exp[-2np(1-p)t^2/\pi^2]
$$

on $[-\pi,\pi]$ bound the atom by $\sqrt\pi/(2\sqrt{2np(1-p)})\le3\sqrt\pi/(4\sqrt n)$. This implies (11); $n=0$ is immediate.

## 3. Counting the surviving parity words

For a binary word of length $k$, let $J_j$ be its prefix weight and define

$$
D_j=j-\lambda J_j,\qquad t_j=\min(j,k-j)+1,
\qquad h_j=16+2\log_2t_j\quad(0\le j\le k).
\tag{12}
$$

A word survives if $D_j<h_j$ for every $1\le j\le k$. Denote the number of surviving words by $N_k$.

![Two legal parity words with the same length and weight. The upper path stays below the symmetric logarithmic boundary; the lower path first crosses it at prefix length 363.](supplement/figure-1.png)

*Figure 1.* Two illustrative words with $k=2048$ and weight $r=1293$ have the same final $D_k$. One survives; the other first crosses at $j=363$. The first-passage partition uses information that a final-weight cutoff discards. The words and deterministic selection seed are included in the supplement; the figure is not a probabilistic estimate.

**Lemma 3.** For every $k\ge0$,

$$N_k\le2^{84}\frac{2^{\theta k}}{(k+1)^{3/2}}.\tag{13}$$

*Proof.* Give the bits the Bernoulli$(\alpha)$ law. Then $S_j=J_j-\alpha j$ is centered, and survival requires

$$S_j>-a_0-b\log t_j,\qquad a_0=16\alpha,\quad b=2\alpha/\log2.$$

Here $\alpha,1-\alpha\in[1/3,2/3]$, and $b<2$ because $\alpha<2/3<\log2$. Fix an endpoint displacement $d=S_k$. Survival forces $d>-a_0$.

Let the first and last segments have length $n=\lfloor k/3\rfloor$, and let the middle segment contain the remaining increments. Survival implies that the first segment stays above $-a_0-b\log(j+1)$. It also implies that the reversed, negated last-segment increments stay above $-(a_0+d)-b\log(j+1)$. Indeed, their partial sum is $S_{k-j}-S_k$, and $t_{k-j}=j+1$ in this segment. The reversed, negated increments have the centered Bernoulli$(1-\alpha)$ law.

Before imposing the endpoint, the first and last events are independent. Conditional on both segments, the middle sum must take one prescribed value. Every segment length plus one is at least $(k+1)/3$. Applying Lemma 2 to the first and last segments, and (11) to the middle atom, therefore gives

$$
\Pr\{\text{surviving},S_k=d\}
\le2^{65}\frac{(a_0+1)(a_0+d+1)}{(k+1)^{3/2}}.
\tag{14}
$$

This argument uses necessary segment conditions only. It does not assume independence of the endpoint and the survival event.

Put $z=\alpha/(1-\alpha)\in(5/3,2)$. A word of weight $r$, with $d=r-\alpha k$, has probability

$$\alpha^r(1-\alpha)^{k-r}=2^{-\theta k}z^d.$$

Consequently,

$$
N_k=2^{\theta k}
\sum_{\substack{d\in\mathbb Z-\alpha k\\d>-a_0}}
 z^{-d}\Pr\{\text{surviving},S_k=d\}.
\tag{15}
$$

Since $a_0<11$, writing $u=a_0+d>0$ and summing the shifted lattice gives

$$
\sum_{d>-a_0}z^{-d}(a_0+d+1)
\le2^{11}\sum_{j\ge0}(3/5)^j(j+2)
=2^{11}\cdot35/4<2^{15}.
$$

Also $a_0+1<12<2^4$. Combining this with (14)–(15) proves (13). Empty segments at the finitely small values of $k$ satisfy the same bounds. $\square$

## 4. First passage gives smaller translated intervals

Stop a parity word at the first $1\le j\le k$ with $D_j\ge h_j$, if such a time exists. The stopping test uses only integers:

$$2^j\ge2^{16}3^{J_j}t_j^2.\tag{16}$$

At a first crossing, $D_{j-1}<h_{j-1}$, $D_j-D_{j-1}\le1$, and $h_{j-1}-h_j\le2$. Hence

$$h_j\le D_j<h_j+3.\tag{17}$$

For a fixed stopping time $j$, the possible integer weights $r=J_j$ lie in an interval of length $3/\lambda<2$. There are at most two such weights.

Fix an arbitrary original interval $I=[a,a+2^k)$, with $a\ge0$ an integer. On any parity word of length $j$ and weight $r$, the exact affine formula gives

$$
C^j(x)=3^r2^{-j}x+b_w,
\qquad 0\le b_w\le(3/2)^r-1.
\tag{18}
$$

The intercept is largest when all odd steps occur last. This follows by swapping an odd-even pair to an even-odd pair: the linear coefficient is unchanged and the intercept increases. The final run of $r$ odd steps has intercept $(3/2)^r-1$.

Thus all images in a single stopping class $(j,r)$ lie in one interval with left endpoint $3^r2^{-j}a$ and width at most

$$
L_{j,r}=3^r2^{k-j}+(3/2)^r-1
\le2^{k-h_j}+(3/2)^r-1.
\tag{19}
$$

The location of this interval retains the original $a$. No high part is averaged or selected independently. The odd-count label $r$ is constant within the class.

For $k\ge128$,

$$h_j\le16+2\log_2(k+1)\le k/4.$$

The last inequality holds at $k=128$ and its right side thereafter grows faster. Since $\log_2(3/2)<3/5$, the additive term $(3/2)^r$ is at most $2^{3k/5}\le2^{k-h_j}$. The integer points in the interval of (19) can therefore be covered by an integer interval of length $2^{\ell_j}$, where

$$
\ell_j=\lceil k-h_j\rceil+2\le k-h_j+3,
\qquad \ell_j\ge k/2,\qquad \ell_j\le k-13.
\tag{20}
$$

The extra two bits allow both the additive intercept and rounding the left endpoint down to an integer. This smaller scale fits the original squared clock:

$$\ell_j^2+j\le(k-13)^2+k\le k^2.\tag{21}$$

## 5. Proof of Theorem 1

The function $G_h(m)$ is nonincreasing in $h$, because labelled states evolve by the deterministic map

$$(y,r)\longmapsto(C(y),r+\mathbf1_{\{y\text{ odd}\}}).$$

It is nondecreasing in $m$. The exact parity bijection [5] makes every length-$k$ binary word occur exactly once among any $2^k$ consecutive integer sources. The first-passage partition and the bound of two weights per stopping time therefore give

$$
G_{k^2}(2^k)\le N_k+
2\sum_{j=1}^kG_{k^2-j}(2^{\ell_j})
\qquad(k\ge128).
\tag{22}
$$

A stopping class may be empty; including it in the upper bound is harmless. Within a nonempty class, further evolution adds a local odd count to its common label $r$, which preserves cardinality. Every class is padded to the same final time $k^2$.

Set

$$F(k)=\frac{2^{\theta k}}{(k+1)^{3/2}}.$$

Assume inductively that $G_{\ell^2}(2^\ell)\le2^{85}F(\ell)$ for $\ell<k$. By (21), each recursive term in (22) is bounded by $2^{85}F(\ell_j)$. From (20) and $\theta<1$,

$$\frac{F(\ell_j)}{F(k)}
\le2^{3/2}2^{\theta(3-h_j)}<24\,2^{-\theta h_j}.$$

Moreover,

$$
\sum_{j=1}^k2^{-\theta h_j}
\le2^{1-16\theta}\sum_{t=1}^{\infty}t^{-2\theta}.
$$

We have $\theta>7/8$. Indeed, $1/2<\alpha<2/3$ implies

$$\theta>H_2(2/3)=\lambda-2/3>11/12,$$

where $\lambda>19/12$ follows from $3^{12}>2^{19}$. The integral bound consequently gives $\sum_{t\ge1}t^{-2\theta}<7/3$. Therefore

$$
2\sum_{j=1}^k\frac{F(\ell_j)}{F(k)}
<224\,2^{-16\theta}<224\,2^{-14}<1/64.
\tag{23}
$$

Lemma 3, (22), and (23) now give

$$
G_{k^2}(2^k)
\le[2^{84}+2^{85}/64]F(k)<2^{85}F(k).
$$

For $0\le k<128$, the trivial bound $G_{k^2}(2^k)\le2^k$ is sufficient, since

$$2^k/F(k)=2^{(1-\theta)k}(k+1)^{3/2}<2^{27}.$$

This closes strong induction. Finally, enlarge an interval of width $m$ to width $2^k\le2m$. Its clock remains $k^2$, and $k+1\ge1+\log_2m$. The factor $2^\theta<2$ gives (2). The case $m=1$ is also immediate. $\square$

## 6. Consequences and remaining limitations

For an interval of positive integers, keep the least original source in each labelled fibre at time $k^2$. Every other original source $n$ has a positive source $b<n$ in the same original interval such that

$$C^{k^2}(b)=C^{k^2}(n),\qquad J_{k^2}(b)=J_{k^2}(n).$$

The number of retained sources satisfies Theorem 1. This is an absolute bound. An arbitrary small marked subset can fit entirely among the retained sources. In particular, the theorem does not guarantee an improving certificate for a specified source or for the least member of a hypothetical exceptional component.

For an orbit set $O$ of distinct states, $C^h$ is injective after removing at most $h$ transient states immediately before an eventual cycle. If the orbit never repeats, no removal is needed. This gives the following uniform consequence, including the original interval location:

$$
\#(O\cap[a,a+m))\le
2^{86}\frac{m^\theta}{(1+\log_2m)^{3/2}}
+\lceil\log_2m\rceil^2.
\tag{24}
$$

Dyadic summation yields

$$
\sum_{\substack{x\in O\\x\ge n}}\frac1x
\ll\frac{n^{\theta-1}}{(1+\log n)^{3/2}}
\qquad(n\ge2).
\tag{25}
$$

For example, the contribution of the polynomial clock term is $O((\log n)^2/n)$, which is asymptotically smaller than the right side of (25). On an actual nonrepeating pre-descent prefix above its original source $n$, the same bound controls

$$\sum_{x\text{ odd on the prefix}}\log\left(1+\frac1{3x}\right).$$

Repeated cycle laps are not included in this distinct-state estimate. No last-arrival or descent-time bound is obtained.


The new logarithmic factor also gives convergence at the critical exponent itself:

$$
\sum_{\substack{x\in O\\x\ge n}}x^{-\theta}
\ll (1+\log n)^{-1/2}\qquad(n\ge2).
\tag{25a}
$$

Indeed, the contribution of the dyadic shell $[2^jn,2^{j+1}n)$ is at most a constant times

$$(1+\log n+j)^{-3/2}+(\log n+j)^2(2^jn)^{-\theta}.$$

The first series sums to $O((1+\log n)^{-1/2})$; the second is $O((\log n)^2n^{-\theta})$ and is smaller after adjusting the absolute constant. Thus every orbit's distinct-state critical zeta sum is finite, with a uniform vanishing tail. The earlier square-root-log counting bound did not establish this critical convergence, since its shell majorant is not summable. On a nonrepeating pre-descent prefix above $n$, (25a) likewise bounds the total cost $\sum_t C^t(n)^{-\theta}$. These positive costs can have a finite sum along an escaping orbit, so this is not a finite descent-time or universal convergence argument.

There is also a useful limitation on multiplicity within the surviving class. For a surviving word with ones at $p_1<\cdots<p_r$, indexed from zero, write

$$B=\sum_{i=1}^r3^{r-i}2^{p_i},\qquad L=B/3^r.$$

Since $J_{p_i}=i-1$,

$$
L=\frac13\sum_{i=1}^r2^{D_{p_i}}
<\frac{2^{16}}3\sum_{j=0}^{k-1}(\min(j,k-j)+1)^2
=:M_k=O(k^3)
\tag{26}
$$

for $k\ge1$. The empty word is harmless. At a fixed weight $r$ and endpoint $y=C^k(x)$, the exact relation

$$x=2^k3^{-r}y-L$$

places all surviving sources in an interval of length $M_k$. Thus their multiplicity is at most $\lfloor M_k\rfloor+1$. This polynomial bound excludes exponential coalescence entirely within the surviving class. It does not supply a further upper image-count saving: an upper multiplicity bound immediately gives a lower bound on image count. It also does not identify the weighted word law with the uniform law on distinct images or prove dyadic mixing. Theorem 1 needs none of these stronger claims.

Rees [6, Lemma 3.5] uses the same affine-offset comparison to bound fibre multiplicity when every prefix division sum is at most $\mu$ times its odd-step count, for a fixed $\mu<\log_2 3$. The next argument treats critical bridges instead: a uniform bound on their conditional mean offset gives bounded multiplicity on a positive fraction of those words.

**Proposition 4 (order of the first-window remainder).** There is an absolute $c>0$ such that, for every $k\ge1$ and every original interval $[a,a+2^k)$, the surviving words with weight $r=\lceil\alpha k\rceil$ have at least

$$c\,2^{\theta k}(k+1)^{-3/2}\tag{27}$$

distinct integer endpoints at time $k$. The total number of surviving labelled images, including all weights, is at most $2^{84}2^{\theta k}(k+1)^{-3/2}$ by Lemma 3. Thus the surviving image contribution has this order. This is a statement at time $k$, and is not a lower bound at time $k^2$.

*Proof.* We use one further consequence of the three-segment argument. For a centered Bernoulli$(p)$ walk, define the half-space kernel

$$K_n^p(u,v)=\Pr\{u+S_j\ge0\ (j\le n),\ u+S_n=v\},\qquad u,v\ge0.$$

Lemma 2 with constant boundaries, applied to the first and reversed-negated last segments, together with (11) for the middle atom, gives

$$K_n^p(u,v)\le C\frac{(u+1)(v+1)}{(n+1)^{3/2}}\tag{28}$$

uniformly for $p\in[1/3,2/3]$. The same proof as (14) permits $C=2^{65}$. Endpoints lie on the appropriate shifted lattice; impossible endpoints have probability zero.

Set $r=\lceil\alpha k\rceil$ and $d=r-\alpha k\in(0,1)$. A word is called good if $J_k=r$ and $S_j=J_j-\alpha j\ge0$ for all $j\le k$. Every cyclic rotation class of weight-$r$ words contains a good word: rotate after a minimum of its prefix sums. The total increment $d$ is positive, so both wrapped and unwrapped partial sums are nonnegative. Each rotation class contains at most $k$ words. Thus the good words are at least a fraction $1/k$ of all weight-$r$ words.

For completeness, the binomial atom at $r$ is at least $1/(16\sqrt{k+1})$. Chebyshev's inequality places at least $3/4$ of a binomial law within two standard deviations of its mean, among at most $3\sqrt{k+1}$ integers. Its largest atom is therefore at least $1/(4\sqrt{k+1})$. A mode is $\lfloor(k+1)\alpha\rfloor$; $r$ is either that mode or one place above. In the latter case the atom ratio is at least $k\alpha/(k\alpha+1)\ge1/4$.

Writing $E_k$ for the good-word event under Bernoulli$(\alpha)$, this proves

$$\Pr(E_k)\ge\frac1{16(k+1)^{3/2}}.$$

Since every good word has probability $2^{-\theta k}z^d$, with $z<2$ and $d<1$, the number of good words is at least $2^{\theta k}/[32(k+1)^{3/2}]$.

We next show that a positive fraction of these words have bounded normalized real offset $L$, with a bound independent of $k$. Splitting a good path at $S_j=x\ge0$ and reversing the last segment gives the exact identity

$$\Pr(E_k,S_j=x)=K_j^\alpha(0,x)K_{k-j}^{1-\alpha}(d,x).$$

Equation (28), $d<1$, and the uniformly bounded shifted-lattice sum $\sum_{x\ge0}3^{-x}(x+1)^2$ imply

$$
\mathbb E[3^{-S_j}\mathbf1_{E_k}]
\le\frac{C_1}{[(j+1)(k-j+1)]^{3/2}}.
$$

Divide by the lower bound for $\Pr(E_k)$ and sum over $0\le j<k$. For $j\le k/2$,

$$\left(\frac{k+1}{(j+1)(k-j+1)}\right)^{3/2}
\le\frac{2^{3/2}}{(j+1)^{3/2}},$$

and the other half is symmetric. It follows that

$$\mathbb E\left[\sum_{j=0}^{k-1}3^{-S_j}\,\middle|\,E_k\right]\le C_2.$$

The normalized offset in (26) is $L=\frac13\sum_i3^{-S_{p_i}}$. Consequently $\mathbb E[L\mid E_k]\le C_3$. The good words all have equal conditional probability, so at least half of them satisfy $L\le2C_3$.

The parity bijection realizes each of these words exactly once in any original interval of width $2^k$. At fixed $r$ and endpoint $y$, their integer sources obey $x=2^k3^{-r}y-L$, and hence lie in an interval of fixed length $2C_3$. Their endpoint multiplicity is at most $\lfloor2C_3\rfloor+1$. Dividing the good-word count by this constant proves (27). Every good word survives (12), so it belongs to the stated remainder. $\square$

Proposition 4 identifies a limit of further deduplication within this first-window remainder. A stronger compression result can still use later evolution or another decomposition. In particular, deterministic iteration after time $k$ can merge the displayed endpoints; the proposition asserts no optimality at the final squared clock.

Mahler [7, Section 6] records the logarithmic boundary and good-word family from our preceding public discussion [3], explicitly attributing the compression theorem and first-window lower bound to that discussion. His additional results describe terminal first-passage class tiling, prefix-pinned numerator injectivity under a range condition, and carry/suffix identities. These are distinct from the uniform bounded-mean-offset multiplicity argument in Proposition 4. That paper appeared shortly before this manuscript's submission; it is a closely timed, explicitly attributed development of the discussion, rather than an independent predecessor to the theorem proved here.


## 7. Fixed-order arithmetic relations and binary entropy

### 7.1. Statement and quantifiers

In this section put $\rho=\lambda=1/\alpha=\log_2 3$, and, for integers $q\ge1$ and
$r\ge0$, define

$$
h_q=H_2\!\left(\frac{1-(1-2\alpha)^q}{2}\right),\qquad
D_r=2^{-r}\sum_{j=0}^r\binom rj h_{2^j}.
\tag{M1}
$$

Thus $D_0=H_2(\alpha)=0.949955527188330\ldots$,
$D_1=0.973280580195543\ldots$, and $D_r$ increases to one.
For independent positive geometric letters of parameter $\alpha$, write

$$
W_s=\sum_{i=1}^s3^{s-i}[2^{-(e_i+\cdots+e_s)}]_{3^i},
\qquad u_s=[W_s]_{3^s},\qquad S_s=e_1+\cdots+e_s.
\tag{M2}
$$

Here $[x]_n$ is the least nonnegative residue modulo $n$; negative powers
of two mean inverses in the indicated odd modulus. For a finite law
$\mu$, $H_\beta(\mu)=(1-\beta)^{-1}\log_2\sum_x\mu(x)^\beta$.

**Theorem B (binary entropy).** Fix $r\ge0$, $0<c_0<\upsilon<\rho/2^r$, and
$0<d<D_r$. There are a fixed $\beta>1$ and constants $C,s_0$ such that

$$
H_\beta(W_s\bmod2^p)\ge dp-C
\quad(s\ge s_0,\ c_0s\le p\le\upsilon s).
\tag{M3}
$$

For every prescribed nonnegative $G(s)=o(s)$, possibly enlarging $C,s_0$
and decreasing the same fixed order $\beta>1$, one also has

$$
H_\beta(W_s\bmod2^p\mid S_s=T)\ge dp-C
\quad\text{for every integer } |T-\rho s|\le G(s)
\tag{M4}
$$

uniformly on that band. The notation in (M4) means entropy of the law
at the indicated individual total, not an average over totals.
For $u_s$ both conclusions hold with an additional $-\log_2s$.
The thresholds are ineffective.

In particular, every $d<1$ is available at some positive linear
precision band and some fixed order above one. The band and the order
may depend on $d$. This does not claim dimension one on any one fixed
band, a uniform order as $d\uparrow1$ on those same bands, or full
binary uniformity. Theorem C in Section 7.9 supplies full atom bounds
on smaller positive linear bands.

| Depth $r$ | Actual chunks $2^r$ | $D_r$ (rounded) | Required upper slope |
|---|---:|---:|---|
| 0 | 1 | 0.949955527188330 | $\upsilon<\rho$ |
| 1 | 2 | 0.973280580195543 | $\upsilon<\rho/2$ |
| 2 | 4 | 0.985787711520690 | $\upsilon<\rho/4$ |
| 3 | 8 | 0.992465572988848 | $\upsilon<\rho/8$ |
| 4 | 16 | 0.996017648345163 | $\upsilon<\rho/16$ |

The numerical entries only evaluate (M1); they are not experiments or
effective estimates for the order or threshold. The case $r=1$ of (M3) is the strict gain used in Section 8. The contribution here is its
fixed-order additive-relation extension, the balanced entropy recursion,
and uniformity at each asymptotically critical exact total. Leen [8, Sections 3.2 and 6] supplies numerator decoding and the entropy-over-contraction formula for the tilted ternary projective law. Those results do not imply binary regularity. The initial arithmetic separation is from accepted paper 30/v2 [9, Lemma 11.1], whose binary bounds approach the source entropy from below. The present relation argument supplies the strict gain needed for Theorem A.

### 7.2. Signed sums of numerator copies

For a composition $w=(t_1,\ldots,t_\ell)$ of $T$, put
$E_j=t_1+\cdots+t_j$, $E_0=0$, and

$$ B(w)=\sum_{j=1}^{\ell}3^{\ell-j}2^{E_{j-1}}. \tag{M5} $$

Its shortcut parity word has ones at $E_0,\ldots,E_{\ell-1}$.
If $n_w$ is the corresponding source residue modulo $2^T$, the affine
parity identity gives

$$ B(w)\equiv-3^\ell n_w\pmod{2^T}. \tag{M6} $$

The parity/source map and multiplication by an odd integer are triangular
bijections of binary prefixes. At the next digit, changing the source
bit while fixing previous bits changes the next parity bit, because
the coefficient after the previous divisions has odd numerator. Odd
multiplication has the same property. Thus the next numerator bit is
the next parity bit or its complement, with the choice determined by
the previous bits. This is the finite coding used in Rees [6]. The
last division block may truncate; it still specifies a length-$T$
shortcut parity word.

Fix a large integer $L\ge3$. Condition on the total $b$ of each
consecutive $L$-letter block. Its first parity is forced to be one;
the remaining $L-1$ ones form a uniform subset of the other $b-1$
positions. The time boundaries of these coarse blocks are now fixed.
For $n=b-1$, $k=L-1$, after exposing $j$ random positions with $X_j$
ones, put

$$ a_j=(k-X_j)/(n-j),\qquad 0\le j<n. \tag{M7} $$

For $q$ independent copies $a_j^{(1)},\ldots,a_j^{(q)}$ of this
bridge parameter, define

$$
g_{L,q}(b)=\sum_{j=0}^{b-2}\mathbb E H_2\!\left(
\frac{1-\prod_{v=1}^q(1-2a_j^{(v)})}{2}\right),\qquad
h_L(b)=\log_2\binom{b-1}{L-1}.
\tag{M8}
$$

In particular $g_{L,1}(b)=h_L(b)$ by the entropy chain rule for the
uniform subset. Always $0\le g_{L,q}(b),h_L(b)\le b$.

Let $B_1,\ldots,B_q$ be independent numerators of a whole chunk,
with the same conditioned coarse totals $b_i$, and fix any signs
$\epsilon_v\in\{-1,1\}$. Then

$$
H\!\left(\sum_{v=1}^q\epsilon_v B_v\bmod2^T\right)
\ge\sum_i g_{L,q}(b_i),\qquad T=\sum_i b_i.
\tag{M9}
$$

To prove this, condition on all $q$ lower numerator prefixes at the
next bit. They determine the carry of the signed sum, including for
negative signs, and the next bits are conditionally independent. Modulo
two a minus sign equals a plus sign, so the next sum bit is their XOR,
possibly complemented by the carry. Complementing one input Bernoulli
parameter changes the sign of its factor $1-2a$ and therefore only
complements the XOR probability. Its entropy is the expression in
(M8). The lower sum prefix is a function of the input prefixes;
conditioning on all input prefixes can only lower the next-bit entropy.
Summing by the chain rule proves (M9). Forced first bits contribute zero.
Independence of ordinary binary digits is neither needed nor asserted.

If $b$ is the total of $L$ original geometric letters, then for each
fixed $q$,

$$ A_{L,q}:=\mathbb E g_{L,q}(b)/L\longrightarrow\rho h_q. \tag{M10} $$

Here is a direct justification. For deterministic $b/L\to\rho$,
write $a_b=(L-1)/(b-1)$. Hypergeometric sampling gives

$$
\mathbb E a_j=a_b,\qquad
\operatorname{Var}(a_j)=\frac{j a_b(1-a_b)}{(n-1)(n-j)}
\le\frac1{4\delta(n-1)}\quad(j\le(1-\delta)n).
\tag{M11}
$$

For fixed $q,\delta>0$, all $q$ parameters converge in probability
to $\alpha$, uniformly in this bulk range. The function of them in
(M8) is continuous on the compact cube $[0,1]^q$, so the corresponding
expected entropy converges uniformly to $h_q$. The discarded final
$\delta n+1$ terms cost at most that number. Let $L\to\infty$ and
then $\delta\downarrow0$. Finally $b/L\to\rho$ in probability,
$g_{L,q}(b)\le b$, and $b/L$ has uniformly bounded second moments.
Uniform integrability gives (M10). This argument is simultaneous for
any fixed finite set of $q$.

### 7.3. Arithmetic transport of fixed-order relations

We record explicitly the harmless coefficient-constant extension of
[9, Lemma 11.1]. Fix $c,\upsilon_0,C,K,\delta>0$ with
$c<\upsilon_0<\rho$. For all sufficiently large $n$, no integers
$p,V,a,b,D$ satisfy

$$
\begin{gathered}
cn\le p\le\upsilon_0n,\quad0\le V\le Cn,\quad
D=2^{V+p}a-3^n b,\\
|a|\le Kn3^n/2^p,\quad |b|\le Kn2^V,\quad
0<|D|\le2^pe^{-\delta n}.
\end{gathered}
\tag{M12}
$$

Indeed, zero coefficients are impossible because
$|D|<2^p<3^n$ and $2^{V+p}\ge2^p$. Set
$X_1=2^{V+p}a$, $X_2=3^n b$. Use the independent forms
$X_1-X_2,X_1$ at infinity and the two coordinate forms at the places
two and three. Their product is at most

$$
|D|\,2^{V+p}|a|\,2^{-(V+p)}3^{-n}
\le Kn|D|/2^p\le Kn e^{-\delta n}.
\tag{M13}
$$

The vector norm is at most $Kn3^n2^V=e^{O(n)}$. The integral
fixed-place Subspace Theorem [10, Theorem 2.3] therefore puts all large
such vectors in finitely many rational lines. Its integral formulation
does not require primitive vectors. But

$$ v_2(X_1)-v_2(X_2)\ge p-\log_2(Kn)\longrightarrow\infty, \tag{M14} $$

whereas that difference is constant on a rational line with nonzero
coordinates. This is a contradiction. The argument gives the stated
uniformity and an ineffective threshold for every fixed $K$.

Consider an actual chunk in positions $k+1,\ldots,k+\ell$ of the
$s$-letter raw sum, with its time total $T$ and later time total $U$
fixed. Put $n=k+\ell$, $h=s-n$, $V=U+T$. Its contribution is
$F=3^hR$, where

$$
R=\sum_{j=1}^{\ell}3^{\ell-j}
[2^{-(U+T-E_{j-1})}]_{3^{k+j}},\qquad
2^VR=B+3^n A,\quad 0\le A<\ell2^V,\quad0<R<\ell3^n.
\tag{M15}
$$

These follow by multiplying each inverse residue by $2^V$ and retaining
its nonnegative integer quotient. No carry has been discarded.

Fix small $\varepsilon>0$, set $M=2^p$, and take

$$
\ell=L\left\lfloor\frac{(1-\varepsilon)p}{\rho L}\right\rfloor,
\qquad H_0=\varepsilon p/4.
\tag{M16}
$$

A word is good if $|E_j-\rho j|\le H_0$ for all $j\le\ell$.
On such words, uniformly for sufficiently large $p$,

$$ 0<B\le\ell3^{\ell-1}2^{H_0}\le M2^{-\varepsilon p/2}. \tag{M17} $$

Suppose $n\asymp s$, $V=O(s)$ and $p/n$ is in a fixed compact
subinterval of $(0,\rho)$. For fixed $q$ and fixed signs, the residue
$\sum_v\epsilon_vF_v\bmod M$ determines the integer
$\sum_v\epsilon_vB_v$ when all $q$ input words are good.

To see this, compare two colliding signed sums. Multiplication by $3^h$
is invertible modulo $M$, so the $R$ sums also collide. If the two
numerator sums differed, (M15) would give

$$
\begin{gathered}
0\ne D=2^{V+p}a-3^n b,\quad
|a|\le2q\ell3^n/M,\quad |b|\le2q\ell2^V,\\
|D|\le2qM2^{-\varepsilon p/2}.
\end{gathered}
\tag{M18}
$$

Since $q$ is fixed and $\ell\le n$, these contradict (M12) after
slightly decreasing its fixed exponential margin. The claim is about
decoding a signed numerator sum; it is not injectivity of tuples.

### 7.4. Good conditional environments

Fix the depth $r$ and let $N=2^r$. Use the last $N$ chunks of length
$\ell$ from (M16). They fit, with an earlier prefix remaining, because
$N\upsilon<\rho$. Condition on the complete earlier word and on
every separate $L$-letter total in the chunks. Denote this environment
by $\mathcal B$ and its chunk contributions by $F_1,\ldots,F_N$.

Each coarse contribution depends on later words only through their
fixed totals; the earlier prefix contribution is fixed for the same
reason. The actual conditional law is therefore a fixed shift plus
a convolution of $Nm=N\ell/L$ independent coarse factors, grouped
into independent chunks $F_i$. The earlier prefix clock has no bound
or truncation imposed on it.

For the finite set $q\in\{1,2,4,\ldots,2^r\}$, and every chunk,
the entropy budgets

$$ \sum_{b_i\text{ in chunk}}g_{L,q}(b_i)\ge(A_{L,q}-\eta)\ell \tag{M19} $$

hold outside probability $Ce^{-as}$ for each fixed $L,\eta>0$.
Under the original geometric law the coarse totals are independent,
$0\le g_{L,q}(b)\le b$, and $b$ has an exponential moment. Applying
exponential Markov near zero to centered sums gives a strict lower-tail
bound; the number $m$ of summands is proportional to $s$. A finite
union over $i,q$ preserves an exponential bound.

Exponential moments and a union bound over partial sums also show that
each chunk's bad-strip probability is at most $Ce^{-a_0s}$. If
$r_i(\mathcal B)$ denotes its conditional bad-strip probability, then

$$
\mathbb P\{r_i(\mathcal B)>e^{-a_0s/2}\}\le Ce^{-a_0s/2}.
\tag{M20}
$$

This uses $\mathbb E r_i\le Ce^{-a_0s}$ and Markov's inequality;
there is no normalization by a small coarse-total probability.
On retained environments every chunk has good probability at least
$1-\delta_s$, with $\delta_s=e^{-a_0s/2}$. Since its total is fixed,
this forces $|T_i-\rho\ell|\le H_0$. Consequently every later
clock in (M15) is $O(s)$, and every chunk's ternary exponent satisfies

$$
n\ge s-(N-1)\ell,\qquad
\frac pn\le\frac{\upsilon}{1-(N-1)\upsilon/\rho}<\rho.
\tag{M21}
$$

The lower ratio is at least $c_0$. Thus Section 7.3 applies to all chunks
with common fixed constants.

For a finite variable $Q$ and an event of probability $1-e$, the chain
rule gives

$$
(1-e)H(Q\mid\text{event})\ge H(Q)-H_2(e)
-e\log_2|\operatorname{supp}Q|.
\tag{M22}
$$

The logarithm of the support size of any fixed signed sum of numerators
is $O(s)$ on retained environments: $T_i=O(s)$ and
$B\le\ell3^\ell2^{T_i}$. A $q$-tuple has a bad word with probability
at most $q\delta_s$. Apply (M22), (M9), and the decoding in Section 7.3;
conditioning on the good-tuple indicator only decreases output entropy.
Writing $H_{\mathcal B}$ for entropy at that one environment, we obtain

$$
H_{\mathcal B}\!\left(\sum_{v=1}^q\epsilon_vF_i^{(v)}\bmod M\right)
\ge(A_{L,q}-\eta)\ell-o(1).
\tag{M23}
$$

The copies here are independent conditional copies of the same actual
chunk, not new arithmetic coefficients. The error is uniformly bounded
by $H_2(q\delta_s)+O(sq\delta_s)$ and tends to zero. We used that
integer-sum entropy is at least its residue entropy in (M9).

### 7.5. The balanced entropy recursion

For a law $\mu$ on a finite abelian group let $\widetilde\mu$ be its
reflection and define $\Delta\mu=\mu*\widetilde\mu$. It is the law of
the difference of two independent copies. The standard entropy triangle
inequality [11] says

$$ 2H(\mu*\nu)\ge H(\Delta\mu)+H(\nu). \tag{M24} $$

For completeness, let $X,X',Y$ be independent, with $X'$ a copy of
$X$. The joint pair $(X+Y,X'+Y)$ determines $X-X'$. Conditional on
this difference, $Y$ remains independent of $X'$, so the conditional
entropy of $X'+Y$ is at least $H(Y)$. Joint entropy is at most
$2H(X+Y)$, proving (M24).

Convolution and reflection commute, and hence

$$ \Delta^j(\mu*\nu)=(\Delta^j\mu)*(\Delta^j\nu). \tag{M25} $$

Here $\Delta^0$ is the identity. The law $\Delta^j\mu$ is a signed
sum of $2^j$ independent copies of $\mu$, with signs generated by
repeated differencing. Apply (M24) at the root of a balanced binary
tree of $N=2^r$ factors. In its left subtree increment the difference
index; in its right subtree keep that index. Repeat using (M25).
For the leaf $i$, let $w(i)$ count left turns on its path from the root.
Induction on the tree depth gives

$$
H(\mu_1*\cdots*\mu_N)
\ge 2^{-r}\sum_{i=1}^N H(\Delta^{w(i)}\mu_i).
\tag{M26}
$$

There are exactly $\binom rj$ leaves with $w(i)=j$; no identity of
the individual factor laws is assumed. Apply this at each retained
environment to the actual chunks, and then use (M23):

$$
H_{\mathcal B}(W_s\bmod M)
\ge\ell\left(2^{-r}\sum_{j=0}^r\binom rj A_{L,2^j}-\eta\right)-o(1).
\tag{M27}
$$

Given $D<D_r$, choose $L$ large using (M10), and then fixed small
$\eta,\varepsilon>0$, so that the coefficient of $p$ in (M27),
using $\ell=(1-\varepsilon)p/\rho+O(L)$, is strictly greater than
$D$. We have proved

$$
\mathbb P_{\mathcal B}\{H_{\mathcal B}(W_s\bmod2^p)<Dp\}
\le Ce^{-as}.
\tag{M28}
$$

This is a probability bound for individual conditional entropies,
stronger than a lower bound on their average.

Finally $h_{2^j}$ increases strictly to one, since
$0<|1-2\alpha|<1$. If $J_r$ is binomial with parameters $(r,1/2)$,
then $D_r=\mathbb E h_{2^{J_r}}$. The coupling
$J_{r+1}=J_r+\operatorname{Bernoulli}(1/2)$ proves monotonicity.
For every fixed $J$, $\mathbb P(J_r<J)\to0$, proving $D_r\to1$.
The depth is chosen before any limit in $s$; there is no growing-depth
application of the arithmetic theorem.

### 7.6. A fixed Rényi order

We give a proof of the finite product lemma needed here. If $Z$ is
a sum of $n$ independent variables in a finite abelian group, each
having at most $B_0$ values, and $\log_2|G|\le C_0n$, then for any
$\kappa>0$ some fixed $\gamma>0$ gives

$$
\mathbb P\{-\log_2\mathbb P(Z)\le H(Z)-\kappa n\}<e^{-\gamma n},
\qquad H_{1+t}(Z)\ge H(Z)-\kappa n-1/t
\tag{M29}
$$

for large $n$ and $0<t\le\gamma/(C_0\log2)$.

Choose $0<\zeta<1/4$ with
$H_2(\zeta)+2\zeta\log_2 B_0<\kappa/2$ and take
$\gamma=\zeta^2/8$. For any output set $A$ of mass at least
$e^{-\gamma n}$, Hamming distance to its preimage has bounded
differences. The inequality
$\mathbb P(f-\mathbb Ef\ge u)\le e^{-2u^2/n}$ and
$\mathbb P(f-\mathbb Ef\le-u)\le e^{-2u^2/n}$ follow by exposing independent coordinates and
applying the bounded-range exponential estimate to the resulting
martingale. The event $f=0$ implies $\mathbb Ef\le\zeta n/4$.
Thus the neighborhood of radius $\lfloor\zeta n\rfloor$ has mass
at least $1-e^{-\gamma n}$ for large $n$. Its output is contained in
$A+\mathcal D$, with

$$
|\mathcal D|\le\sum_{j\le\zeta n}\binom nj B_0^{2j}
\le2^{n[H_2(\zeta)+2\zeta\log_2B_0]}.
\tag{M30}
$$

Splitting entropy according to this set gives
$H(Z)\le\log_2|A|+\kappa n/2+o(n)$. But the set in (M29) has
cardinality at most $2^{H(Z)-\kappa n}$, so it cannot have mass
$e^{-\gamma n}$. Splitting the power sum over that exceptional set
then gives at most $2^{-t(H(Z)-\kappa n)}+e^{-\gamma n}$; the choice
of $t$ proves the second inequality. This is the classical product
blowing-up argument using bounded differences [12].

Now fix $d<D<D_r$ and $\delta>0$ with $D-2\delta>d$. The $n=Nm$
coarse alphabets, not the macrochunks, will be used in this lemma.
Let $J_K(b)=h_L(b)\mathbf1_{b>K}$. Since $\alpha>1/2$,
$\mathbb E2^b<\infty$ and $\mathbb E2^{J_K(b)}\to1$. Choose a
fixed $K$ such that

$$
\log_2\mathbb E2^{J_K(b)}\le\frac{\delta\rho L}{2N}.
\tag{M31}
$$

As $n\le Np/(\rho L)$, exponential Markov gives

$$ \mathbb P\{\sum_iJ_K(b_i)>\delta p\}\le2^{-\delta p/2}. \tag{M32} $$

Outside this exception and (M28), replace the factors with $b_i>K$
by point masses. Their total entropy is at most $\delta p$, so the
retained convolution $\nu$ has entropy at least $(D-\delta)p$.
Reconvolving removed factors decreases each $\ell^{1+t}$ norm.
Keep all $n$ coordinate slots, including point masses. Each retained
alphabet has at most $2^K$ values, and $p\le C_{L,N}n$ for large
$s$ because $n\asymp p$. With
$\kappa=\delta\rho L/(2N)$, one has $\kappa n\le\delta p/2$.
Equation (M29) consequently implies, for one sufficiently small fixed
$t>0$,

$$
\sum_v\mathbb P(W_s=v\bmod M\mid\mathcal B)^{1+t}
\le2\,2^{-t(D-2\delta)p}
\tag{M33}
$$

on retained environments. All exceptions have total mass $Ce^{-as}$.
Choose $t$ smaller if necessary so that $t\upsilon\log2\le a/2$.
Convexity under the original mixture, using the trivial power-sum bound
one on bad environments, gives

$$
\sum_v\mathbb P(W_s=v\bmod M)^{1+t}
\le2\,2^{-t(D-2\delta)p}+Ce^{-as}
\le(2+C)2^{-t(D-2\delta)p}.
\tag{M34}
$$

This proves (M3). In particular the order does not vary with $s,p$
or with the environment. Nothing in this step assumes a bounded
alphabet for a whole chunk.

### 7.7. Every asymptotically critical exact total

For an allowed integer $T$, put $a_T=s/T$. Under independent positive
geometric letters of parameter $a_T$, the sum has mean exactly $T$.
Conditional on $S_s=T$, every positive composition has the same
probability for every geometric parameter. This is exactly the desired
conditional law from (M2), not an approximation to it.

Uniformly for $|T-\rho s|\le G(s)=o(s)$, one has $a_T\to\alpha$.
Stirling's bounds for the negative-binomial mass at its mean give

$$
\mathbb P_{a_T}(S_s=T)
=\binom{T-1}{s-1}a_T^s(1-a_T)^{T-s}
\ge c/\sqrt{s}.
\tag{M35}
$$

The constant is uniform once $a_T$ lies in a fixed compact subinterval
of $(0,1)$. For example, write the binomial factor as
$a_T\binom Ts$ and apply the usual two-sided factorial bounds; the
exponential factors cancel at $a_T=s/T$.

All exponential exceptional estimates above hold uniformly under these
comparison laws. Here are the required details.

For the fixed $L$ and finite list of $q$, the expectations of
$g_{L,q}(b)$ are continuous in the geometric parameter near $\alpha$.
The bound by $b$ and a common exponential moment justify dominated
convergence. Hence the strict entropy margins chosen after (M27)
persist uniformly, and the centered exponential-moment proof of (M19)
has a common positive rate. The latter follows by a uniform Taylor
bound near zero using a common exponential second moment.

The mean clock is now $1/a_T=T/s$. Its discrepancy from $\rho$
causes at most $G(s)=o(s)$ drift over any chunk. Since
$H_0\ge\varepsilon c_0s/4$, this drift is eventually at most $H_0/2$.
Uniform exponential moments for the centered geometric variables
therefore give the same exponential strip estimate about $\rho j$.

Choose a compact parameter interval lying inside $(1/2,1)$. On this
interval $\mathbb E2^b$ is uniformly finite, and uniform domination
gives $\sup_a\mathbb E_a2^{J_K(b)}\to1$. Thus one fixed $K$ makes
(M31)--(M32), with the same entropy budget, hold uniformly. Constants
may be adjusted without changing the chosen finite $r,L$.

The conditional internal-word law at a fixed environment $\mathcal B$
is independent of the geometric parameter. Moreover $S_s$ is already
determined by $\mathcal B$, since the earlier prefix is fully exposed
and all chunk totals are specified. Further conditioning on $S_s=T$
therefore leaves the independent internal coarse words unchanged. In
particular the function $r_i(\mathcal B)$ in (M20) is the same under
each comparison law and under the conditioned law.

Build the good environments using the preceding uniform estimates under
$\mathbb P_{a_T}$. Their bad mass is at most $Ce^{-as}$. Dividing by
(M35) bounds the bad mass under the exact-total environment law by
$C'\sqrt{s}e^{-as}\le C''e^{-as/2}$ for large $s$. This single
polynomial conditioning loss is paid after centering the comparison
law at the specified total. It is not a division by the possibly
exponentially small original probability of that total.

On every good environment the pointwise arithmetic, entropy recursion,
and finite product argument are unchanged. Mix (M33) using the
exact-total environment weights and choose one fixed smaller $t$ to
pay the common exponential bad mass. This proves (M4), uniformly over
every allowed total. The constants can be chosen for the iid and
exact-total laws together. Only the eventual threshold needs to account
for how slowly $G(s)/s$ tends to zero.

### 7.8. Canonical carries, scope, and the compression consequence

The raw sum satisfies $0<W_s<s3^s$, and hence
$u_s=W_s-3^sA_s$ for an integer $0\le A_s<s$. For any of the
probability laws above, put
$f_j(v)=\mathbb P(W_s=v\bmod2^p,A_s=j)$. Pointwise convexity and
translation invariance of the power sum give

$$
\sum_v\mathbb P(u_s=v\bmod2^p)^\beta
\le s^{\beta-1}\sum_{v,j}f_j(v)^\beta
\le s^{\beta-1}\sum_v\mathbb P(W_s=v\bmod2^p)^\beta.
\tag{M36}
$$

This proves the logarithmic carry loss, with no independence assumption.

The case $r=1$ on the band $[1/16,1/4]$ supplies the unconditional
uniform interval-compression corollary in Section 8: for some
$\gamma,K>0$, the number of actual endpoint/odd-count pairs obtained
from any integer interval of length $m$ after
$k^2$ shortcut steps is at most $Km^{H_2(\alpha)-\gamma}$, where
$k=\lceil\log_2m\rceil$. The complete source-count and finite-clock
proof is given there; no further optimization of that consumer is claimed.

The fixed finite audit described in Section 9 checks the two-copy coding and actual
factorization inputs. It has not been rerun or expanded for this
extension. Equations (M9), (M12), and (M26) provide the general proofs
for higher fixed orders. No finite computation checks the ineffective
Subspace threshold or substitutes for the asymptotic reasoning.

Neither (M3) nor (M4) constructs a smaller legal source for a prescribed
integer at its actual forward endpoint. High entropy of these actual
word laws and sparsity of labelled images still allow exceptional
individual trajectories. Collatz remains unresolved.


### 7.9. Full atom bounds from independent groups

Put $\alpha=\log_3 2$ and $\rho=1/\alpha$. Use the actual raw sum
$W_s$, canonical endpoint $u_s$, and total $S_s$ from (M2). All entropies and logarithms of probabilities are in bits.

**Theorem C (full atom bounds).** For every $0<d<1$ there is $c_d>0$ such that, for every
fixed $0<c_0<\upsilon<c_d$, there are $C,s_0$ with

$$
\max_v\mathbb P(W_s=v\bmod2^p)\le C2^{-dp}
\quad(s\ge s_0,\ c_0s\le p\le\upsilon s).
\tag{A1}
$$

For every prescribed $G(s)=o(s)$ the same conclusion, after adjusting
constants and threshold, holds at every individual integer total
$|T-\rho s|\le G(s)$:

$$
\max_v\mathbb P(W_s=v\bmod2^p\mid S_s=T)\le C2^{-dp}.
\tag{A2}
$$

For the canonical endpoint the right sides become $Cs2^{-dp}$.
Equivalently the raw min-entropy $H_\infty=-\log_2\max_v\mu(v)$ is
at least $dp-O(1)$, and hence so is every finite Rényi entropy, including
collision entropy. The precision constant depends on $d$. This does not
assert full binary uniformity, a positive lower bound on any atom, or
unit dimension on one fixed positive linear band. Thresholds remain
ineffective.

#### 7.9.1. A local conditional estimate for one group

Choose fixed depth $R$ and $d<d_1<D_R$, using $D_R\uparrow1$ in
(M1). Put $Q=2^R$. A group consists of $Q$ consecutive chunks, each
of length

$$
\ell=L\left\lfloor\frac{(1-\varepsilon)p}{\rho L}\right\rfloor.
\tag{A3}
$$

Here the fixed $L,\varepsilon$ and entropy margins are chosen as in
Sections 7.4--7.6, with enough room to give dimension
$d_1$. Condition on every $L$-letter total in the group. Let $b$ denote
this vector of totals, and let $\nu_b$ be the law of its actual raw
contribution modulo $2^p$, with all later totals fixed as well.

There are fixed $\beta>1$, $C_0,C_1,a>0$ and sets of good vectors
$\mathcal G_p$ such that

$$
b\in\mathcal G_p\ \Longrightarrow\
H_\beta(\nu_b)\ge d_1p-C_0,\qquad
\mathbb P(b\notin\mathcal G_p)\le C_1e^{-ap}.
\tag{A4}
$$

The good-vector set depends only on this group's coarse totals. The
entropy assertion is uniform in its actual location and the later
total, provided the arithmetic ranges specified below hold. The bad
probability is uniform for independent geometric parameters in some
fixed sufficiently small compact neighborhood $I\subset(1/2,1)$ of
$\alpha$.

Here are the details needed to localize the preceding proof. Require
each chunk's coarse entropy budgets (M19) for
$q\in\{1,2,\ldots,2^R\}$ restricted to powers of two. Require that
its conditional bad-strip probability, given its own coarse totals,
is at most $e^{-a_0p/2}$, where the strip is
$|E_j-\rho j|\le\varepsilon p/4$. Finally require the total
large-alphabet removal cost $\sum h_L(b_i)\mathbf1_{b_i>K}$ across
the group to be at most the chosen small multiple of $p$.

Each requirement is a function of the group's own coarse totals.
There are proportional-to-$p$ independent coarse blocks. The centered
exponential-moment argument gives exponential lower tails for all
entropy budgets. The unconditional strip failure is $Ce^{-a_0p}$,
so Markov gives exponential failure for the required conditional
probability. The tail-cost estimate (M31)--(M32), with $N=Q$, is also
exponential in $p$. A finite union proves the probability part of (A4).

On a good vector every chunk has good words, so its fixed total is
$O(p)$. The entropy loss on trimming a fixed number of copies is
$O(p e^{-a_0p/2})+H_2(Qe^{-a_0p/2})=o(1)$. The signed-relation
transport and balanced entropy triangle therefore apply exactly as in
(M23)--(M28). Remove large coarse alphabets and apply the bounded-product
argument before mixing environments, as in (M33). This proves the
pointwise fixed-order estimate in (A4). Neither $\beta$ nor $C_0$
depends on the group's later total or its location. The eventual
arithmetic threshold can depend on their fixed allowed ranges.

For uniformity in the geometric parameter, choose $I$ small enough that
the strict entropy margins persist and
$|1/a'-\rho|\ell\le\varepsilon p/8$ for $a'\in I$.
The coarse-budget exponential moments are uniform on $I$. Uniform
domination of $2^b$ holds because $I\subset(1/2,1)$, so one alphabet
cutoff works throughout. Conditional internal words at fixed totals
are uniform compositions for every parameter; in particular the
conditional strip-failure function is parameter-independent. This
justifies every uniformity assertion in (A4).

#### 7.9.2. Convolving enough good groups controls every atom

Let

$$ K_0=\left\lceil\frac{\beta}{\beta-1}\right\rceil,
\qquad q_0=\frac{K_0}{K_0-1}\le\beta. \tag{A5} $$

Monotonicity of Rényi entropy and (A4) give, for a good group,

$$ \|\nu_b\|_{q_0}\le 2^{(C_0-d_1p)/K_0}. \tag{A6} $$

The norms use counting measure on the finite group. Discrete Young's
inequality consequently gives, for $K_0$ good groups,

$$
\|\nu_{b_1}*\cdots*\nu_{b_{K_0}}\|_\infty
\le\prod_{i=1}^{K_0}\|\nu_{b_i}\|_{q_0}
\le2^{C_0-d_1p}.
\tag{A7}
$$

This use of Young has constant one, independently of the modulus.
Indeed, $\|f*g\|_r\le\|f\|_u\|g\|_v$ when
$1+1/r=1/u+1/v$, with counting norms. Hölder proves the finite-$r$
case by writing the summand as
$(|f|^u|g|^v)^{1/r}|f|^{u/v'}|g|^{v/u'}$ and applying exponents
$r,v',u'$, then raising to $r$ and summing over the output.
The endpoint $r=\infty$ is Hölder directly. Iterating with all input
exponents $q_0$ gives (A7). Convolution with any further probability
factor cannot increase the supremum norm.

The conditional laws of different actual groups are independent once
all coarse totals and the complete earlier prefix are fixed. Their
coefficients can depend on the later fixed totals; this does not change
the independence of internal words or the uniformity of (A4). Thus
(A7) applies to their actual convolution, without replacing arithmetic
coefficients or treating shared random clocks as independent.

#### 7.9.3. Amplifying the exceptional-environment exponent

Choose a fixed number $N\ge K_0$ of groups so large that

$$ a(N-K_0+1)>2\log 2. \tag{A8} $$

Under an independent geometric law, the vectors of coarse totals of
different groups are independent. Fewer than $K_0$ good groups requires
at least $N-K_0+1$ bad vectors. A union bound over subsets gives

$$
\mathbb P\{\text{fewer than }K_0\text{ good groups}\}
\le2^N C_1^{N-K_0+1}e^{-a(N-K_0+1)p}
\le C_2 2^{-2p}.
\tag{A9}
$$

This is the reason for using multiple actual groups. Merely applying
Young on a good event and retaining the old exceptional mass would
not yield the claimed high-order bound.

Use the last $NQ$ chunks of the full word. There are $NQ\ell$ letters
in this tail. Choose a fixed $t>0$ such that
$M(t)=\sup_{a'\in I}\mathbb E_{a'}e^{te}<\infty$. Then

$$
\mathbb P\{S_{\rm tail}>Ap\}
\le\exp\!\left[\left(-tA+\frac{NQ}{\rho}\log M(t)\right)p\right]
\le2^{-2p}
\tag{A10}
$$

by taking a fixed sufficiently large $A$. This estimate is uniform on
$I$ and is separate from the independent local-goodness events.

Take, for example, $c_d=\rho/(NQ)$. If
$0<c_0<\upsilon<c_d$ and $c_0s\le p\le\upsilon s$, all groups fit
with an earlier prefix remaining. Each chunk ends at a ternary
exponent $n$ with

$$
n\ge s-(NQ-1)\ell,\qquad
c_0\le p/n\le\frac{\upsilon}{1-(NQ-1)\upsilon/\rho}<\rho.
\tag{A11}
$$

Outside (A10), every later clock $V$ is at most $Ap=O(s)$.
These are exactly the ranges needed for the signed-relation separation
in (A4). The constants $A,N,Q$ are fixed before $s$ grows. The earlier
prefix clock is unrestricted and does not enter a tail factor.

Condition on all coarse totals in the tail and on the entire earlier
word. On environments with at least $K_0$ good groups and total tail
clock at most $Ap$, (A7) bounds every atom of the full conditional raw
law by $2^{C_0-d_1p}$. The prefix supplies a constant shift; unused
groups are reconvolved. Bad environments have probability at most
$C_3 2^{-2p}$. On them use the trivial atom bound one. Mixing yields

$$
\max_v\mathbb P(W_s=v\bmod2^p)
\le2^{C_0-d_1p}+C_3 2^{-2p}\le C2^{-dp}.
\tag{A12}
$$

We used $d<d_1<1$. Thus (A1) controls the full law, including the
exceptional atoms.

#### 7.9.4. Exact totals and canonical endpoints

Fix $|T-\rho s|\le G(s)=o(s)$ and compare with independent positive
geometric letters of parameter $a_T=s/T\in I$. As in (M35),

$$ \mathbb P_{a_T}(S_s=T)\ge c/\sqrt{s}. \tag{A13} $$

Equations (A9)--(A10) hold under this independent comparison law with
common constants. Conditional on the prescribed total their combined
bad probability is therefore at most
$C\sqrt{s}\,2^{-2p}$. Since $p\ge c_0s$, this is bounded by
$C'2^{-dp}$ for all large $s$, uniformly over the allowed totals.

The total is a function of the environment: all earlier letters and
all tail coarse totals have been exposed. Thus fixing it changes only
the environment weights. Internal words remain independent uniform
compositions, and the good-environment estimate (A7) is unchanged.
Mixing it with the last bad-mass bound proves (A2). It is legitimate to
use independence in (A9) before conditioning; no such independence of
the total vectors after conditioning is asserted.

Finally $u_s=W_s-3^s A_s$ with $0\le A_s<s$. For either law,

$$
\mathbb P(u_s=v\bmod2^p)
\le\sum_{j=0}^{s-1}\mathbb P(W_s=v+3^sj\bmod2^p)
\le s\max_z\mathbb P(W_s=z\bmod2^p).
\tag{A14}
$$

This proves the canonical assertion without carry independence.

#### 7.9.5. Scope and verification

This argument strengthens an actual conditional near-one Rényi estimate
to a full atom bound on a smaller positive linear band. The analytic
inputs are the proved local signed-relation and coarse-concentration
arguments, discrete Young's inequality, independent coarse environments,
and a geometric clock-tail bound. No additional finite scan is required
or performed. The previously frozen audit does not test this amplification
or its ineffective threshold.

The stronger upper bound still does not supply a positive lower mass
for a prescribed exact ternary endpoint and real source window. Such a
lower occupancy or an explicit admissible word is the missing ingredient
in the individual smaller-source condition. Collatz remains unresolved.

### 7.10. Joint source and endpoint concentration

#### 7.10.1. Statement and relation to earlier work

Put $\alpha=\log_3 2$, $\rho=\log_2 3$, and let
$e_1,\ldots,e_s$ be independent positive geometric variables of parameter
$\alpha$. Write $E_j=e_1+\cdots+e_j$, $E_0=0$, and $S=E_s$. Define

$$
\begin{aligned}
B_s&=\sum_{i=1}^s3^{s-i}2^{E_{i-1}},\\
W_s&=\sum_{i=1}^s3^{s-i}
 [2^{-(S-E_{i-1})}]_{3^i},\\
Z_s&=\sum_{i=1}^s2^{E_{i-1}}
 [-3^{-i}]_{2^{S-E_{i-1}}},\\
u_s&=[W_s]_{3^s},\qquad n_s=[Z_s]_{2^S}.
\end{aligned}
\tag{J1}
$$

Residues are least nonnegative residues; inverses are in the displayed
coprime modulus. The pair $(n_s,u_s)$ is the actual canonical source and
endpoint for the prescribed shortcut word [6]. The last division block
may end at an even endpoint. For integers $h,p\ge0$, put

$$
\mathcal G_{h,p}=(\mathbb Z/3^h\mathbb Z)\times
(\mathbb Z/2^p\mathbb Z),\qquad P=p+\rho h=\log_2|\mathcal G_{h,p}|.
\tag{J2}
$$

Use $D_r$ from (M1):

$$
D_r=2^{-r}\sum_{j=0}^r\binom rj
H_2\!\left(\frac{1-(1-2\alpha)^{2^j}}2\right),\qquad D_r\uparrow1.
\tag{J3}
$$

**Theorem D (joint source and endpoint entropy).** For fixed $r\ge0$,
$0<c_0<\upsilon<\rho/2^r$, and $0<d<D_r$, there are a fixed $\beta>1$
and constants such that, uniformly for $c_0s\le P\le\upsilon s$,

$$
H_\beta(Z_s\bmod3^h,W_s\bmod2^p)\ge dP-O(1).
\tag{J4}
$$

For every prescribed $G(s)=o(s)$ this also holds separately at each exact
total $|T-\rho s|\le G(s)$. For the canonical pair the corresponding
lower bound is $dP-\log_2s-O(1)$ under either law. This is a bound
obtained before environment mixing; no direct entropy comparison between
the two mixed laws is needed.

Moreover, for every $0<d<1$, some $c_d>0$ gives, on each fixed band
$0<c_0<\upsilon<c_d$ and $c_0s\le P\le\upsilon s$,

$$
\max_{a,v}\Pr(Z_s=a\bmod3^h,W_s=v\bmod2^p)\le C2^{-dP}.
\tag{J5}
$$

The same holds at every indicated critical exact total. For the canonical
pair the right side is $Cs2^{-dP}$. The thresholds are ineffective, and
the admissible band depends on the requested dimension.

The new point is joint regularity of the actual source and endpoint, using
both congruence constraints in one arithmetic separation argument. These
are upper concentration estimates. They do not assert full uniformity,
a positive atom lower bound, a uniformly bounded normalized conditional
collision energy, or descent for every supplied input.

Mahler [13] studies the same fixed-total source-given-endpoint problem through
shifted carry coordinates, endpoint-collision families and a suffix operator.
His shifted coordinate called $Z_s$ is different from the raw integer in
(J1). The canonical coding and the need to retain exact totals are prior
work. Mahler [7, equation (6.14)] already gives the shared source and
endpoint carry. We restate that identity below; the new contribution
is its joint signed-relation and concentration application. The common
entropy-concentration machinery is proved in Sections 7.2--7.9.

#### 7.10.2. Exact raw duality and the common canonical carry

For $D\ge1$, let $a=[2^{-D}]_{3^i}$. The integer

$$ b=\frac{2^Da-1}{3^i} \tag{J6} $$

lies in $[0,2^D)$ and satisfies $3^ib\equiv-1\pmod{2^D}$. Hence
$b=[-3^{-i}]_{2^D}$. Rearrange (J6) as $2^Da-3^ib=1$, multiply by
$2^{E_{i-1}}3^{s-i}$ with $D=S-E_{i-1}$, and sum to obtain the exact
integer identity

$$ 2^S W_s-3^s Z_s=B_s. \tag{J7} $$

Both raw variables are positive, with $W_s<s3^s$ and $Z_s<s2^S$.
The residue $u_s$ is a positive unit modulo three. Multiplying its defining
congruence modulo $3^s$ by $2^{e_s}$ leaves $1$ plus three times the
corresponding prefix expression modulo $3^{s-1}$. Subtract one and divide
by three; induction gives integrality of every prescribed inverse step.
Reading those inverse steps gives positive states, since each legal
inverse step is $(2^e x-1)/3>0$ at a positive integer $x$. Their source
is $(2^Su_s-B_s)/3^s$, which lies in $(0,2^S)$ and is congruent to
$Z_s$ modulo $2^S$. It is therefore $n_s$. Subtracting this canonical
identity from (J7) proves that the two raw quotients are equal:

$$
a_s=\left\lfloor\frac{W_s}{3^s}\right\rfloor
=\left\lfloor\frac{Z_s}{2^S}\right\rfloor,\qquad 0\le a_s<s,
\qquad (n_s,u_s)=(Z_s-a_s2^S,W_s-a_s3^s).
\tag{J8}
$$

Equations (J7)--(J8) restate the shared canonical-carry identity in
Mahler [7, equation (6.14)], with the raw source sum written as $Z_s$.
In particular the pair has one shared carry, not two independent carries.
No independence of that carry and either output coordinate is assumed.

For a chunk with indices $k+1,\ldots,k+\ell$, put $U=E_k$,
$T=E_{k+\ell}-E_k$, $m=S-U$, $n=k+\ell$, and
$F_j=E_{k+j}-E_k$. Its two actual contributions are
$2^U R_Z$ and $3^{s-n}R_W$, where

$$
\begin{aligned}
R_Z&=\sum_{j=1}^{\ell}2^{F_{j-1}}
 [-3^{-(k+j)}]_{2^{m-F_{j-1}}},\\
R_W&=\sum_{j=1}^{\ell}3^{\ell-j}
 [2^{-(m-F_{j-1})}]_{3^{k+j}},\\
B&=\sum_{j=1}^{\ell}3^{\ell-j}2^{F_{j-1}}.
\end{aligned}
\tag{J9}
$$

The same termwise identity gives

$$
2^mR_W-3^nR_Z=B,\qquad
0<R_Z<\ell2^m,\quad 0<R_W<\ell3^n.
\tag{J10}
$$

Condition every coarse-block total and the complete words outside the
selected chunks. Then $S$, all chunk boundaries and the multipliers
$2^U,3^{s-n}$ are fixed. Each vector contribution depends only on its own
internal word, so the vectors are independent and add exactly in
$\mathcal G_{h,p}$. Both multipliers are units in their respective target
coordinates. The dependence of $Z_s$ on $S$ is thus retained explicitly.

#### 7.10.3. A separation lemma using both precisions

**Lemma.** Fix $c,C,K,\delta>0$. For all sufficiently large $s$, no
integers $m,n,p,h,a,b,D$ satisfy

$$
\begin{gathered}
0\le m,n,p,h\le Cs,\qquad P=p+\rho h\ge cs,\\
2^{m+p}\ge2^P,\qquad 3^{n+h}\ge2^P,\\
D=2^{m+p}a-3^{n+h}b,\qquad
|a|\le Ks3^n/2^p,\quad |b|\le Ks2^m/3^h,\\
0<|D|\le2^P e^{-\delta s}.
\end{gathered}
\tag{J11}
$$

**Proof.** A zero coefficient is excluded by the two lower bounds on the
powers. Put $X_1=2^{m+p}a$, $X_2=3^{n+h}b$. At infinity take forms
$X_1-X_2,X_1$, and at the places two and three take the coordinate forms.
Their product is at most

$$
|D|\,2^{m+p}|a|\,2^{-(m+p)}3^{-(n+h)}
\le Ks\frac{|D|}{2^p3^h}\le Ks e^{-\delta s}.
\tag{J12}
$$

Meanwhile $\max(|X_1|,|X_2|)\le Ks2^m3^n\le e^{C_1s}$.
For all sufficiently large $s$, the last expression in (J12) is at most
$\max(|X_1|,|X_2|)^{-\delta/(2C_1)}$. The integral fixed-place Subspace
Theorem [10] therefore confines the vectors to finitely many rational
lines. Its integral formulation does not require primitive vectors. Uniformly,
$|X_1/X_2-1|=|D/X_2|\le e^{-\delta s}$, since
$|X_2|\ge3^{n+h}\ge2^P$. Every fixed line other than the diagonal
is excluded eventually. The diagonal gives $D=0$, a contradiction.
The eventual threshold is ineffective. $\square$

Suppose two fixed signed-copy sums of one chunk have equal vector output
in $\mathcal G_{h,p}$. The unit multipliers may be removed. Subtracting
(J10) for all copies yields

$$
D=2^{m+p}a-3^{n+h}b,\qquad
|a|\le K_q\ell3^n/2^p,\quad
|b|\le K_q\ell2^m/3^h,
\tag{J13}
$$

where $D$ is the corresponding difference of signed numerator sums and
$K_q$ depends only on the fixed number of copies. Thus, when the
numerators are sufficiently small and the two powers in (J11) are large
enough, the joint output determines the integer signed numerator sum.
The gain in (J12) is the full product $2^p3^h$; discarding either output
congruence would lose that factor.

#### 7.10.4. Central placement and common entropy inputs

Fix $N=2^r$ and the band in (J4). Choose a small fixed $\varepsilon>0$
and a large fixed coarse length $L$, then take $N$ consecutive chunks of
length

$$
\ell=L\left\lfloor\frac{(1-\varepsilon)P}{\rho L}\right\rfloor.
\tag{J14}
$$

Place these chunks centrally among the $s$ letters. Since
$N\upsilon<\rho$, the unselected prefix and suffix can each have at
least $\kappa s$ letters for some fixed $\kappa>0$ and all large $s$.
Require each selected chunk to satisfy the critical clock strip

$$ |F_j-\rho j|\le\varepsilon P/4\quad(0\le j\le\ell). \tag{J15} $$

On that strip, each term of its numerator is at most
$3^{\ell-1}2^{\varepsilon P/4}$, so, eventually,

$$ 0<B\le2^P2^{-\varepsilon P/2}. \tag{J16} $$

The endpoint $j=\ell$ in (J15) gives
$T\ge(1-5\varepsilon/4)P-O(L)$. For every selected chunk,
$n\ge\ell+\kappa s$ and $m\ge T+\kappa s$, since all later letters
are positive. Choose $\varepsilon$ sufficiently small in terms of
$\kappa,\upsilon$, for example with
$\varepsilon\upsilon<\rho\kappa/2$ and
$5\varepsilon\upsilon/4<\kappa/2$. Then, uniformly for large $s$,

$$ \rho n\ge P,\qquad m\ge P. \tag{J17} $$

This implies both power inequalities in (J11) for every split
$P=p+\rho h$, including either coordinate with zero precision. A separate
geometric exponential-moment bound gives $S\le C_0s$ outside an event
of probability at most $2^{-3P}$, by choosing a fixed sufficiently large
$C_0$. On that event's complement all arithmetic parameters in (J11)
are $O(s)$. The bounds hold uniformly for geometric parameters in a
small fixed compact neighborhood of $\alpha$.

Fix the coarse totals inside each chunk. If a coarse block has length
$L$ and total $b$, its first parity is forced to be one; its other
$L-1$ ones are a uniform subset of the remaining $b-1$ positions.
For $q$ independent copies, let $a_j^{(v)}$ be the remaining-one
probability after $j$ exposed positions in copy $v$, and put

$$
g_{L,q}(b)=\sum_{j=0}^{b-2}\mathbb E H_2\!\left(
\frac{1-\prod_{v=1}^q(1-2a_j^{(v)})}{2}\right).
\tag{J18}
$$

The triangular parity/source/numerator coding and binary addition give
precisely the signed-bit bound proved in (M9)--(M11): for any fixed
signs and independent whole-chunk numerators with these coarse totals,

$$
H\!\left(\sum_{v=1}^q\epsilon_v B_v\bmod2^T\right)
\ge\sum_i g_{L,q}(b_i),\qquad
\frac{\mathbb E g_{L,q}(b)}L\longrightarrow\rho h_q,
\quad h_q=H_2\!\left(\frac{1-(1-2\alpha)^q}2\right).
\tag{J19}
$$

The calculation conditions on all lower numerator prefixes. The next
signed-sum bit is XOR plus a determined carry. Complementing any input
bit only complements that XOR probability, so its entropy is (J18).
Hypergeometric sampling of the remaining positions gives the displayed
limit. This is still a binary numerator calculation; it assumes no
independence of ternary source digits.

The coarse totals are independent under the geometric law. Since
$0\le g_{L,q}(b)\le b$ and each total has an exponential moment,
the sums of budgets in (J19) have exponential lower tails below any
fixed smaller rate than their mean. The unconditional failure of
(J15) is exponentially small in $P$. Markov's inequality therefore
makes the conditional strip-failure probability exponentially small
outside exponentially rare vectors of local coarse totals. These are
exactly the local budgets used in Sections 7.4--7.6, for the finite set
$q=1,2,4,\ldots,2^r$.

On such a good vector, trim the exponentially small probability of
violating (J15) in a fixed number of copies. Its entropy cost is $o(1)$:
the possible signed numerator sums have an alphabet of size $2^{O(P)}$,
by the fixed total bound, and binary entropy pays for the indicator of
the trimming event. Equations (J13), (J16), and (J17), with the lemma,
show that the signed vector output determines the integer numerator
sum on the retained tuples. Its entropy is at least that of the
numerator sum modulo $2^T$. Restoring the removed mass loses $o(1)$.
Thus each actual chunk vector has the same fixed signed-copy entropy
budgets as in (M23), with $P$ replacing binary precision.

Apply the entropy triangle
$2H(X+Y)\ge H(X-X')+H(Y)$ to the actual independent chunk vectors in
$\mathcal G_{h,p}$. Its balanced recursion has $\binom rj$ leaves
carrying $2^j$ signed copies, and gives conditional Shannon entropy
arbitrarily close to $D_rP$. The group need only be finite and abelian;
its being a product of two cyclic groups changes no entropy inequality.

For clarity, the conversion to a fixed order above one is also performed
before mixing environments. Remove coarse blocks with total $b>K$.
Their total entropy cost is at most
$\sum\log_2\binom{b-1}{L-1}\mathbf1_{b>K}$, whose expectation is
arbitrarily small compared with $P$ and whose excessive tail is
exponentially small. All remaining independent factors have a fixed
bounded alphabet. The product blowing-up argument in Section 7.6
then turns the conditional Shannon bound into
$H_\beta\ge d_1P-C$ for some fixed $\beta>1$ and $d<d_1<D_r$.
Changing a bounded number of input coordinates adds one of a controlled
number of group shifts; that is the only output property required by
the argument. Reconvolving the removed factors cannot increase the
power norm. Thus the proof applies to this exact vector convolution.

Local goodness depends only on the selected group's coarse totals.
Conditioning the exterior words and later totals determines the actual
coefficients but does not change its internal product law. The estimate
is uniform on $S\le C_0s$. Convexity of the power sum, and a sufficiently
small fixed $\beta-1$, absorb the exponentially rare bad environments
and the separate global clock event, proving (J4).

#### 7.10.5. Full atoms and the shared-carry conditioning

Choose fixed $R$ and $d<d_1<D_R$. A group has $Q_0=2^R$ chunks of
length (J14). The preceding argument gives one fixed $\beta>1$ and
locally good coarse vectors with

$$
H_\beta(\nu_{\mathrm{group}})\ge d_1P-C,
\qquad \Pr(\mathrm{local\ bad})\le C e^{-aP}.
\tag{J20}
$$

Use a fixed number $N_0$ of disjoint groups. Take the total-precision
upper slope sufficiently small that their selected letters occupy less
than half the word, and place all of them centrally. Equations (J17)
and the separate global clock bound then hold uniformly. Local bad
events of different groups are independent before any exact-total
conditioning, because each depends only on that group's coarse totals.

Set $K_0=\lceil\beta/(\beta-1)\rceil$. The counting-measure Young
inequality on $K_0$ good conditional group laws gives

$$
\left\|\nu_1*\cdots*\nu_{K_0}\right\|_\infty
\le\prod_{i=1}^{K_0}\|\nu_i\|_{K_0/(K_0-1)}
\le 2^{C-d_1P}.
\tag{J21}
$$

Choose $N_0$ so large that $a(N_0-K_0+1)>2\log2$. The probability
of fewer than $K_0$ good groups is then at most $C2^{-2P}$ by a union
bound over the independently bad subsets. A larger $C_0$ gives the
same bound for $S>C_0s$. Condition on all coarse totals and all exterior
words. The group vectors remain independent, and further convolution
cannot increase the maximum atom. Mixing the good and bad environments
proves (J5), with room between $d_1$ and $d$.

For a prescribed exact total $T$ in the critical window, compare with
independent geometric variables of parameter $s/T$. The event $S=T$
is at the mean and has probability at least $c/\sqrt{s}$. Internal
composition laws at fixed coarse totals do not depend on the geometric
parameter, and the uniform budget and clock estimates hold in a fixed
neighborhood of $\alpha$. The total is already measurable in the
conditioning environment. Hence the internal independence and (J21)
remain intact; the exceptional probabilities cost only $O(\sqrt{s})$.
The strict exponent margins absorb that cost. The same comparison and
convexity argument proves the exact-total version of (J4).

It remains to justify canonicalization when $S$ is random. Do it before
mixing environments. At a fixed environment, $S$ is fixed and (J8)
subtracts one of the $s$ joint translations
$(a2^S\bmod3^h,a3^s\bmod2^p)$. For the joint raw law $\mu$ and its
canonical law $\bar\mu$, convexity on the $s$ carry pieces gives

$$
\sum_{x\in\mathcal G_{h,p}}\bar\mu(x)^\beta
\le s^{\beta-1}\sum_{x\in\mathcal G_{h,p}}\mu(x)^\beta,
\qquad \|\bar\mu\|_\infty\le s\|\mu\|_\infty.
\tag{J22}
$$

Each carry piece is translated bijectively; summing its powers is at
most the power of the unsplit atom. The carry need not be independent.
Use (J22) on every good environment and bound the remaining bad mass
directly. This proves the stated canonical bounds both with and without
a prescribed total, without treating the $S$-dependent translation as
fixed after mixing.

#### 7.10.6. Actual source information after observing the endpoint

Let $X=n_s\bmod3^h$ and $Y=u_s\bmod2^p$. For any joint finite law,
its average conditional guessing probability satisfies

$$
\operatorname{Guess}(X\mid Y)
:=\sum_v\max_a\Pr(X=a,Y=v)
\le 2^p\max_{a,v}\Pr(X=a,Y=v).
\tag{J23}
$$

Its average conditional collision probability is no larger, since
$\sum_a\Pr(X=a\mid Y=v)^2\le\max_a\Pr(X=a\mid Y=v)$.
Thus the full-atom theorem gives

$$
\mathbb E_Y\sum_a\Pr(X=a\mid Y)^2
\le\operatorname{Guess}(X\mid Y)
\le Cs2^{p-d(p+\rho h)}.
\tag{J24}
$$

The same conclusion holds separately at every allowed exact total.
It also holds for the original geometric law when $S$ is revealed as
additional side information. Let $\mathcal E$ be the complete coarse
environment in Section 7.10.5 and let $\mathcal E_{\rm good}$ mean that the
global clock bound and the required number of locally good groups hold.
The conditional canonical atom bound there is $Cs2^{-d_1P}$, while
$\Pr(\mathcal E\notin\mathcal E_{\rm good})\le C2^{-2P}$. Since $S$
is a function of $\mathcal E$, revealing the complete environment can
only increase the average guessing probability. Thus

$$
\operatorname{Guess}(X\mid Y,S)
\le\operatorname{Guess}(X\mid Y,\mathcal E)
\le Cs2^{p-d_1P}+C2^{-2P}
\le C's2^{p-dP}.
\tag{J25}
$$

At an allowed exact total the bad term is at most
$C\sqrt{s}\,2^{-2P}$ and is absorbed in the same way. This proof uses
the conditional good-environment bound, not an inference from the mixed
joint law. No division by a small endpoint probability is needed.

For example, if $p\le A\rho h$ for a fixed $A$, then choosing $d$
sufficiently close to one gives, for any fixed $\epsilon>0$ on a band
that may depend on $A,\epsilon$,

$$
\operatorname{Guess}(X\mid Y,S)\le Cs\,3^{-(1-\epsilon)h}.
\tag{J26}
$$

This is an average over the observed endpoint and total; it is not a
pointwise statement for every observed pair. The corresponding normalized
conditional collision energy is bounded by $Cs3^{\epsilon h}$, not by
a constant. The current source-defect consumer asks for stronger control.
Nor does an upper guessing bound supply positive occupancy at the exact
ternary endpoint and real source window needed for each original input.

#### 7.10.7. Verification status

The raw identity, the shared canonical carry, and every contiguous-chunk
identity were checked exactly on 1103 words in the fixed cases
$(s,S)=(4,6),(5,8),(6,9),(7,11),(8,13)$, covering 36193 chunks.
The saved checker is `joint_raw_duality_check_20261026.py` and its result
has the same stem with extension `.json`. This is an algebra check;
it does not verify an ineffective separation threshold or any asymptotic
entropy conclusion. The earlier entropy audit remains frozen.

A separate written author audit checks raw duality, canonical positivity,
the integral fixed-place theorem and exceptional lines, central placement,
local goodness, conditional independence, exact-total comparison, and
canonicalization before environment mixing. It is saved as
`joint_source_endpoint_entropy_author_audit_20261026.md`. It is an author
check, not an independent review or a formal verification of the proof.


### 7.11. Real source and endpoint concentration

#### 7.11.1. Statement

Let $e_1,\ldots,e_s$ be independent positive geometric variables with
parameter $\alpha=\log_3 2$, and put $\rho=1/\alpha$,
$E_j=\sum_{i\le j}e_i$, and $S=E_s$. Use the raw pair and its canonical
pair from (J1):

$$
\begin{aligned}
W_s&=\sum_{i=1}^s3^{s-i}[2^{-(S-E_{i-1})}]_{3^i},\\
Z_s&=\sum_{i=1}^s2^{E_{i-1}}[-3^{-i}]_{2^{S-E_{i-1}}},\\
u_s&=[W_s]_{3^s},\qquad n_s=[Z_s]_{2^S}.
\end{aligned}
\tag{R1}
$$

For integers $p,h\ge0$, set $P=p+\rho h$ and, for a random vector
$V=(A,x)$ in $(\mathbb Z/3^h\mathbb Z)\times\mathbb R$, write

$$ Q_p(V)=(A,\lfloor2^p x\rfloor),\qquad H_{\beta,p}(V)=H_\beta(Q_p(V)). \tag{R2} $$

Define two raw vectors and their canonical versions by

$$
\begin{aligned}
V_s^{\rm end}&=(Z_s\bmod3^h,W_s/3^s),&
\bar V_s^{\rm end}&=(n_s\bmod3^h,u_s/3^s),\\
V_s^{\rm src}&=(Z_s\bmod3^h,Z_s/2^S),&
\bar V_s^{\rm src}&=(n_s\bmod3^h,n_s/2^S).
\end{aligned}
$$

**Theorem E (real source and endpoint concentration).** Fix $r\ge0$,
$0<c_0<\upsilon<\rho/2^r$, and $0<d<D_r$, with $D_r$ from (M1).
There is a fixed $\beta>1$ for which

$$
H_{\beta,p}(V_s^\sigma)\ge dP-O(1)
\quad(c_0s\le P\le\upsilon s).
\tag{R3}
$$

Here $\sigma\in\{\rm src,\rm end\}$ may be either choice.
Each canonical vector has the lower bound
$dP-\log_2s-O(1)$. Moreover, for each $0<d<1$, there is $c_d>0$
such that, on each fixed band $0<c_0<\upsilon<c_d$ with
$c_0s\le P\le\upsilon s$,

$$
\begin{aligned}
\sup_{a,t}\Pr\{V_s^\sigma\in\{a\}\times[t,t+2^{-p})\}
&\le C2^{-dP},\\
\sup_{a,t}\Pr\{\bar V_s^\sigma\in\{a\}\times[t,t+2^{-p})\}
&\le Cs2^{-dP}.
\end{aligned}
\tag{R4}
$$

For every prescribed $G(s)=o(s)$, all these conclusions hold separately
at every exact total $|T-\rho s|\le G(s)$, with uniform constants and
an eventual threshold. Thresholds are ineffective. The real coordinate
is a normalized source or endpoint, distinct from the real random series
considered in other Syracuse-law limit theorems. The result concerns interval masses
of finite atomic laws, not existence of a Lebesgue density.

The new ingredient is a separation estimate for nearby real outputs.
The rest of the proof carefully transfers the existing finite-group
argument to quantized sums of real variables. Section 8.3 uses $h=0$ to
count large final odd-step counts, and then actual sources that have not
halved. It neither assumes
a fresh independent law after survivor selection nor supplies an
arbitrarily small exceptional power.

#### 7.11.2. Arithmetic separation for nearby real outputs

For a chunk in positions $k+1,\ldots,k+\ell$, put $U=E_k$,
$m=S-U$, $n=k+\ell$, and $F_j=E_{k+j}-E_k$. The exact raw identities
(J9)--(J10) read

$$
2^mR_W-3^nR_Z=B,\qquad
B=\sum_{j=1}^{\ell}3^{\ell-j}2^{F_{j-1}},\qquad
0<R_W<\ell3^n,\quad0<R_Z<\ell2^m.
\tag{R5}
$$

Its actual vector contribution is
$(2^UR_Z\bmod3^h,R_W/3^n)$ for $\sigma=\rm end$, or
$(2^UR_Z\bmod3^h,R_Z/2^m)$ for $\sigma=\rm src$.
Normalization cancels the respective exterior multiplier exactly.
For the source coordinate the total $S$ is fixed by the environment.

**Separation lemma.** Fix positive $c,C,K,\delta$. For all sufficiently
large $s$, there are no integers $m,n,p,h,a,b,D$ satisfying

$$
\begin{gathered}
0\le m,n,p,h\le Cs,\qquad P=p+\rho h\ge cs,\\
2^m\ge2^P,\qquad3^{n+h}\ge2^P,\\
D=2^m a-3^{n+h}b,\quad |a|\le Ks3^n,\quad
|b|\le Ks2^m/3^h,\\
\text{either } |a|\le3^n2^{-p}\text{ or }|b|\le2^m/(3^h2^p),\\
0<|D|\le2^P e^{-\delta s}.
\end{gathered}
\tag{R6}
$$

**Proof.** A zero coefficient contradicts the lower bound on the other
power. Put $X_1=2^m a$, $X_2=3^{n+h}b$. For the first alternative use the forms
$X_1-X_2,X_1$ at infinity, and at two and three use the coordinate forms. The product
of their norms is at most

$$
|D|\,2^m|a|\,2^{-m}3^{-(n+h)}
\le\frac{|D|}{2^p3^h}\le e^{-\delta s}.
\tag{R7}
$$

For the second alternative, use $X_1-X_2,X_2$ at infinity. The product
is then at most $|D|\,|b|\,2^{-m}\le |D|/(2^p3^h)$.
There are only these two fixed systems of forms.
The integer-vector norm is at most $Ks2^m3^n=e^{O(s)}$, after enlarging
the constant. The integral fixed-place Subspace Theorem [10, Theorem 2.3]
confines the vectors to finitely many rational lines. Its hypotheses do
not require primitive coordinates. But
$|X_1/X_2-1|\le e^{-\delta s}$, so eventually only the diagonal line
could occur, and there $D=0$. This is a contradiction. $\square$

Compare two fixed signed-copy sums of the same chunk whose source
residues and quantized real outputs agree. Multiplication by $2^U$ is
invertible modulo $3^h$. Thus their source difference is $3^h b$, and
their integer endpoint difference is $a$. In the endpoint case,
$|a|<3^n2^{-p}$; in the source case,
$|3^hb|<2^m2^{-p}$. Equation (R5) therefore yields the appropriate
alternative in (R6), with $D$ the signed numerator difference and the
remaining coefficient bounds up to a constant depending only on the
fixed number of copies.

Choose the central chunks exactly as in Section 7.10.4:

$$
\ell=L\left\lfloor\frac{(1-\varepsilon)P}{\rho L}\right\rfloor,
\qquad |F_j-\rho j|\le\varepsilon P/4.
\tag{R8}
$$

Positive linear slack on both sides, with sufficiently small
$\varepsilon$, gives $m\ge P$ and $\rho n\ge P$. On the strip,
$B\le2^P2^{-\varepsilon P/2}$. The independent geometric tail bound
for $S\le C_0s$ gives the upper arithmetic ranges. For any fixed number
of copies, a nonzero $D$ would therefore contradict (R6). Consequently
the quantized joint output determines the integer signed numerator sum
on retained tuples.

The real variable in this argument is the unwrapped raw value
$R_W/3^n$ or $R_Z/2^m$. Taking a fractional part here would insert an
integer carry into the congruences. The common canonical carry is handled
only after the conditional concentration estimate has been proved.

#### 7.11.3. Entropy and concentration for quantized real sums

Here are the rounding facts needed to reuse the signed-copy argument.
They hold for independent random variables in a finite abelian group
times $\mathbb R$, with finite quantized entropies.

First, $Q_p(X+Y)$ differs from $Q_p(X)+Q_p(Y)$ by a carry in
$\{0,1\}$ in the integer coordinate. Similarly,
$Q_p(X)-Q_p(X')$ and $Q_p(X-X')$ differ by at most one binary choice.
The usual discrete entropy triangle therefore gives

$$
2H(Q_p(X+Y))\ge H(Q_p(X-X'))+H(Q_p(Y))-3,
\tag{R9}
$$

where $X'$ is an independent copy of $X$. Indeed, apply the discrete
triangle to $Q_p(X),Q_p(Y)$, lose at most one bit when replacing their
sum by the quantized real sum, and at most one bit for their difference.

Apply this down a balanced tree of $2^r$ independent actual chunk
vectors, commuting convolution and differencing before quantizing.
The same binomial leaf count as in Section 7.5 gives the signed-copy mixture
$D_r$, with only $O_r(1)$ rounding loss. The conditional signed-copy
budgets are unchanged: the binary numerator parity calculation still
has the rate

$$
h_q=H_2\!\left(\frac{1-(1-2\alpha)^q}{2}\right),
\qquad q\in\{1,2,4,\ldots,2^r\}.
\tag{R10}
$$

Equation (R6) replaces the modular-output decoder. Entropy of the integer
numerator sum dominates that of its binary residue. Trimming exponentially
rare strip failures costs $o(1)$, since the numerator alphabet has
logarithm $O(P)$ on locally good coarse totals. Thus the conditional
Shannon lower bound is arbitrarily close to $D_rP$.

Second, an arbitrary fixed real translation sends each old cell into
at most two new cells, and a new cell receives pieces of at most two
old cells. Splitting masses into these pieces and applying convexity
shows, for $\beta>1$,

$$
\sum_z\Pr(Q_p(V+t)=z)^\beta
\le2^{\beta-1}\sum_z\Pr(Q_p(V)=z)^\beta.
\tag{R11}
$$

Here $t$ may be a fixed vector translation in both coordinates. The same
inequality holds after adding an independent random vector, by convexity
over its values. A translation also costs at most one bit of Shannon
entropy in either direction. In particular, if a collection of independent
coarse factors is removed, the entropy of the retained quantized sum is
at least the original entropy minus the sum of their input entropies
minus one. Reconvolving their aggregate costs at most one bit in any
fixed Rényi order. There is no separate rounding loss for every factor.

Third, the bounded-product concentration argument survives quantization.
For $n$ independent inputs with alphabets of size at most $B_0$, changing
at most $\zeta n$ coordinates adds one of at most

$$
\sum_{j\le\zeta n}\binom nj B_0^{2j}
\tag{R12}
$$

actual vector shifts. The image of a quantized output set $A$ under any
one shift has at most $2|A|$ cells. Hence the Hamming-neighborhood count
in the blowing-up proof of Section 7.6 changes by a factor of two. Bounded
differences for the distance to the preimage of $A$ is unchanged. If the
quantized alphabet has logarithm $O(n)$, the proof gives, for each fixed
$\eta>0$, a fixed $\beta>1$ with

$$ H_{\beta,p}(V)\ge H(Q_p(V))-\eta n-O(1). \tag{R13} $$

To make the use of this input explicit, a set of outputs of mass at least
$e^{-\gamma n}$ has a Hamming neighborhood of radius $\zeta n$ with
mass $1-e^{-\gamma n}$ for sufficiently small fixed $\gamma>0$.
Its image has at most
$2|A|\,2^{n[H_2(\zeta)+2\zeta\log_2 B_0]}$ cells. Splitting the
entropy over this image bounds $H(Q_p(V))$ by
$\log_2|A|+\eta n/2+o(n)$ when $\zeta$ is small. Therefore the set
of atoms with information below $H(Q_p(V))-\eta n$ has exponentially
small mass. Splitting the power sum over that set proves (R13) for one
sufficiently small fixed $\beta-1$. This is the same product-space
proof, with its additional factor two retained.

In the actual word law, condition all selected coarse totals and all
exterior letters. The raw vector is a sum of independent coarse factors.
Either real coordinate lies in $[0,s)$, so its quantized alphabet has at
most $3^h(s2^p+1)$ values and logarithm $P+O(\log s)$. There are
proportional-to-$P$ coarse factors. Removing factors with large total
has exponentially controlled small entropy cost, exactly as in Sections 7.4--7.6,
and leaves a fixed bounded alphabet. Apply (R13), then (R11) to reconvolve
the removed aggregate and the fixed exterior contribution.

All exceptional local conditions are the same functions of a group's
own coarse totals as in Sections 7.9--7.10. The good-environment fixed-order estimate
is uniform in the exterior clocks when $S\le C_0s$. Convexity under
the environment mixture and a sufficiently small fixed $\beta-1$ absorb
the exponential exceptional mass. This proves the raw assertion (R3).

#### 7.11.4. Full interval masses, exact totals and canonical carries

Fix $d<d_1<D_R$ and a fixed order $\beta>1$ from the local argument.
Take $K_0=\lceil\beta/(\beta-1)\rceil$ good groups. Their quantized
outputs are independent variables on
$(\mathbb Z/3^h\mathbb Z)\times\mathbb Z$. Counting-measure Young's
inequality applies to their discrete convolution exactly as before.
The quantized sum of the real vectors differs from the sum of their
quantizations by a carry in $\{0,\ldots,K_0-1\}$. Hence

$$
\max_z\Pr\{Q_p(V_1+\cdots+V_{K_0})=z\}
\le K_0\,\|\mathcal L(Q_p(V_1))*\cdots*
\mathcal L(Q_p(V_{K_0}))\|_\infty
\le C2^{-d_1P}.
\tag{R14}
$$

Reconvolving all remaining independent factors and the fixed exterior
shift costs at most a factor two by (R11) and its maximum-atom version.
Use a larger fixed number of disjoint groups, each with a local bad
probability $Ce^{-aP}$. Local bad events are independent before
conditioning on an exact total. As in Section 7.9.3, choose the number of groups
so that the probability of fewer than $K_0$ good ones is at most
$C2^{-2P}$. Shrink the upper precision slope so that all selected
chunks fit centrally with fixed left and right slack. Bound $S>C_0s$
separately by the same exponential rate. Mixing environments gives a
raw maximum-cell bound $C2^{-dP}$.

For a critical exact total $T$, compare with independent geometric
variables of parameter $s/T$. The event $S=T$ has probability at least
$c/\sqrt{s}$. The local estimates hold uniformly near $\alpha$,
and internal composition laws at fixed coarse totals are unchanged.
The total is a function of the complete environment. Thus exact-total
conditioning affects only the environment weights; the bad probability
costs $O(\sqrt{s})$, absorbed by the strict exponential margins.
The same reasoning gives the exact-total version of (R3).

Finally the raw identity (J7)--(J8) gives a shared carry $0\le a_s<s$ with

$$
Q_p(\bar V_s^\sigma)=Q_p(V_s^\sigma)
-(a_s2^S\bmod3^h,a_s2^p).
\tag{R15}
$$

At each environment, $S$ is fixed and these are $s$ fixed translations
of the quantized group. Carry-piece convexity costs $s^{\beta-1}$ in
the power sum or $s$ in the largest cell. Apply this before environment
mixing. Every interval of length $2^{-p}$ meets at most two grid cells,
so the maximum-cell estimates imply (R4), with an adjusted constant.

#### 7.11.5. Scope, verification and the remaining precision question

The real argument imports the signed numerator budgets, the local-good
environment estimates and the shared raw duality from Section 7.10. Its new
interfaces are (R6), the quantization bounds (R9)--(R15), and the exact original-source
localization and count (R18)--(R21). These are analytic deductions; no
additional finite experiment is claimed. The exact duality check and the
older entropy checks remain frozen and do not verify asymptotic thresholds.
A separate author audit checks both choices of real coordinate, every
quantization loss, exact-total conditioning, and the source-count injection.
It is saved as `real_endpoint_concentration_author_audit_20261026.md`.
External review remains pending.

The small upper slope in (R4) limits (R16). This proof does not establish
arbitrarily small-power many survivors at a longer constant logarithmic
horizon. An extension to much finer real precision would need different scope:
the unconditioned law has an atom of mass at least $\alpha^s$ from the
all-one word. Thus an almost uniform bound at precision above
$-s\log_2\alpha$ is impossible for the full law. Exact critical totals
remove that example but have their own word-entropy ceiling near
$\theta\rho s$. A longer survivor argument must also retain the actual
barrier; large final counts alone allow trajectories that halved and
later grew. Neither a broad exact-total real estimate nor an iteration
of the present survivor bound is asserted. Collatz remains unresolved.


## 8. Proof of the power improvement

Let $C(x)=x/2$ for even $x$ and $C(x)=(3x+1)/2$ for odd $x$,
and let $J_h(x)$ count odd steps in the first $h$ shortcut iterates.
Recall the labelled image count (1):

$$
G_h(m)=\sup_{a\in\mathbb Z_{\ge0}}
\#\{(C^h(x),J_h(x)):a\le x<a+m\}.
\tag{S31}
$$

**Theorem A, restated.** There are fixed $\gamma>0$, $K<\infty$ such that

$$
G_{k^2}(m)\le K m^{\theta-\gamma},\qquad k=\lceil\log_2m\rceil.
\tag{S32}
$$

Theorem 1 gives $O(m^\theta/(1+\log m)^{3/2})$.
The new result improves its power exponent. It retains every original
interval location, the actual source set, the final odd-count label and
the common finite clock. Its eventual threshold is ineffective.

**Proof.** Choose $\theta<d<D_1$. Apply Theorem B at depth one,
with word length $r$ and band $r/16\le p\le r/4$, to obtain a fixed
$\beta>1$. Set $\beta'=\beta/(\beta-1)$,
$z=\alpha/(1-\alpha)$, $t=z^{1/\beta'}$, and $\delta=1/8$.
The raw power sum bound and (M36) imply, by Holder and the parity
bijection modulo $2^p$, uniformly for every integer high part $q_0$,

$$
\mathbb E t^{J_p(q_03^r+u_r)}
\le K_0 r^{1/\beta'}2^{(1-d)p/\beta'}
\left(\frac{1+t^{\beta'}}2\right)^{p/\beta'}.
\tag{S33}
$$

The expectation uses the original critical geometric law of $r$ letters.
The factor $r^{1/\beta'}$ comes only from the actual bounded carry.
Translation by $q_03^r$ preserves the power sum. The parity bijection
makes the uniform sum of $t^{\beta'J_p}$ equal to
$(1+t^{\beta'})^p$, giving exactly (S33).

Fix an aligned original interval $q_02^k+[0,2^k)$. Each nonzero
$k$-bit parity word with $r$ ones has a unique form
$0^j1,0^{e_1-1}\cdots1,0^{e_r-1}$, with
$e_i\ge1$ and total $k-j$. Its actual first endpoint is
$q_03^r+u_r$, and the corresponding geometric word has probability
$w_{k,j,r}=\alpha^r(1-\alpha)^{k-j-r}$.
The single all-zero parity word causes only one labelled endpoint and
is included in the low-count cover below.

Let $H$ be a fixed positive integer. Retain first counts
$r>\lfloor\alpha k\rfloor-H$, take $p=\lfloor\delta k\rfloor$
more steps, and call a source bad if its total count exceeds
$\alpha(k+p)-H$. Nonnegative exponential Markov and dropping only the
exact-total restriction inside an expectation give

$$
N_{k,j,r}(q_0)\le
w_{k,j,r}^{-1}t^{r-\alpha(k+p)+H}
\mathbb E t^{J_p(q_03^r+u_r)}.
\tag{S34}
$$

This counts original sources, so it is an admissible upper bound on
labelled images. There is no division by a rare-total probability.
With $a=1-\alpha$, the exact reweighting identity is

$$
w_{k,j,r}^{-1}t^{r-\alpha k+H}
=a^j2^{\theta k}t^H(t/z)^{r-\alpha k}.
\tag{S35}
$$

Since $1<t<z$, the retained $r$-sum of the last two factors is at most
$z^H/(1-t/z)$, and the $j$-sum is at most $1/\alpha$.
The choice of $t$ satisfies

$$
\alpha\log_2t-\frac1{\beta'}\log_2\frac{1+t^{\beta'}}2
=\frac{1-\theta}{\beta'}.
\tag{S36}
$$

Thus (S33)--(S36) yield the uniform bound

$$
N_{\mathrm{bad}}(q_0)
\le K_H k^{1/\beta'}2^{\theta k-\sigma p},
\qquad \sigma=(d-\theta)/\beta'>0.
\tag{S37}
$$

The input precision band is valid for every retained $r$ when $k$ is
large: $p/r\ge1/8-o(1)>1/16$ since $r\le k$, and
$p/r\le1/(8\alpha)+o(1)<1/4$ since $r\ge\alpha k-H$.
All such $r$ also exceed the fixed arithmetic threshold eventually.

For completeness we give the interval recursion that consumes (S37).
Choose $\eta$ with $\theta-\sigma\delta<\eta<\theta$.
For low first counts $r\le\lfloor\alpha k\rfloor-H$, first endpoints
lie in $q_03^r+[0,3^r)$ with common label $r$. They are covered at
integer scale $\ell_r=\lceil\rho r\rceil$, and their total normalized
induction cost is at most

$$
\sum_r2^{\eta(\ell_r-k)}
\le\frac{2^{\eta(1-\rho H)}}{1-3^{-\eta}}.
\tag{S38}
$$

For high first counts but low total counts
$R\le\lfloor\alpha(k+p)\rfloor-H$, all endpoints after $k+p$
steps with that label lie in the same interval

$$
\left[\frac{q_03^R}{2^p},\,
\frac{q_03^R}{2^p}+\frac{3^R}{2^p}+(3/2)^p\right).
\tag{S39}
$$

The usual affine recursion bounds the added offset in the last $p$
steps by $(3/2)^p-1$. To cover integer points in (S39), one may use

$$
\ell_R=\left\lfloor\max(\rho R-p,\log_2(3/2)p,1)\right\rfloor+3.
\tag{S40}
$$

The extra three pays for rounding the interval endpoints. Splitting
according to the maximizing term gives normalized induction cost at most

$$
\frac{2^{\eta(3-\rho H)}}{1-3^{-\eta}}
+O(k)2^{-\eta(k-\log_2(3/2)p)}+O(k)2^{-\eta k}.
\tag{S41}
$$

Choose $H$ so large that twice the sum of the geometric constants in
(S38), (S41) is less than $1/4$. For large $k$ the other terms vanish,
and every selected scale is at most $k-3$. Hence its additional
$\ell^2$ steps fit under the common $k^2$ clock, whether the initial
stage used $k$ or $k+p$ steps. Padding a labelled endpoint by a fixed
further number of deterministic steps cannot increase its cardinality.
Each cover therefore costs at most the inductive bound
$K2^{\eta\ell}$ for its smaller scale, with the preceding count added
to its final label.

An arbitrary integer interval of width $2^k$ meets at most two aligned
intervals of that width; the factor two was included when choosing
$H$. Finally the high/high source count (S37), after normalization by
$2^{\eta k}$, tends to zero because $\eta>\theta-\sigma\delta$.
The polynomial factor and rounding of $p$ are absorbed by this strict
gap. Enlarging $K$ for a finite initial range closes strong induction
uniformly over all locations. For general $m$, use
$2^{k-1}<m\le2^k$ and absorb $2^\eta$ into $K$.
Taking $\eta=\theta-\sigma/16$ proves (S32) with
$\gamma=\sigma/16>0$. $\square$


### 8.1. Orbit-set consequences below the critical power

Put $\eta=\theta-\gamma>0$, reducing $\gamma$ if necessary. The same
distinct-state argument as in Section 6 gives, for every Collatz orbit
set $O$, uniformly in the original interval location,

$$
\#(O\cap[a,a+m))\le K m^\eta+\lceil\log_2m\rceil^2.
\tag{P2}
$$

For a nonrepeating orbit, iteration is injective on its state set. For
an eventually periodic orbit, removing at most the last $k^2$ transient
states before the cycle gives injectivity of $C^{k^2}$. Apply Theorem A
to the remaining states; the labels can only increase the available
upper image count. This proves (P2), including finite cycles as sets of
distinct states.

For every fixed $t>\eta$, dyadic summation gives the uniform tail bound

$$
\sum_{\substack{x\in O\\x\ge n}}x^{-t}\le C_t n^{\eta-t}
\qquad(n\ge2).
\tag{P3}
$$

Indeed, the shell $[2^jn,2^{j+1}n)$ contributes at most
$K(2^jn)^{\eta-t}+O((\log n+j)^2(2^jn)^{-t})$.
Both series converge; the second is absorbed because $\eta>0$.
In particular the distinct-state zeta sum converges at some exponents
strictly below $\theta$, and its tail at $t=\theta$ is $O(n^{-\gamma})$.
Repeated cycle laps are not counted. A convergent positive cost along
an escaping orbit does not force finite descent.

### 8.2. Halving the original sources in logarithmic time

The source estimate (S37) has a direct consequence before the interval
recursion. Define

$$
\tau_{1/2}(n)=\inf\{h\ge1:C^h(n)<n/2\},\qquad
L(k)=k+\lfloor k/8\rfloor,
\tag{P4}
$$

with $\inf\varnothing=\infty$. The strict inequality is intentional.

**Corollary (uniform original-source halving).** With the same fixed
$\gamma>0$ as in Theorem A, after enlarging $K$, for every integer
$m\ge1$, $k=\lceil\log_2m\rceil$, and integer $a\ge0$,

$$
\#\{n\in[a,a+m)\cap\mathbb Z_{>0}:\tau_{1/2}(n)>L(k)\}
\le K m^{\theta-\gamma}.
\tag{P5}
$$

Moreover, for every $X\ge2$,

$$
\#\{1\le n\le X:\tau_{1/2}(n)>
L(\lfloor\log_2n\rfloor)\}\le K X^{\theta-\gamma}.
\tag{P6}
$$

These are counts of original sources, with no quotient by endpoint
collisions. In the ordinary map, each shortcut step uses at most two
steps, so (P5)--(P6) also give halving within twice the stated clocks.
The constants and eventual threshold inherit the ineffectivity of the
entropy input.

**Proof.** Keep the choices $d,\beta',\sigma$ from Section 8, so
$\gamma=\sigma/16$ and $p=\lfloor k/8\rfloor$. Take the fixed integer
$H$ there large enough that $H\ge2$. On the aligned block
$I_{q_0,k}=[q_02^k,(q_0+1)2^k)$ with integer $q_0\ge1$, write
$r=J_k(n)$ and $R=J_{k+p}(n)$.

If $r\le\lfloor\alpha k\rfloor-H$, the actual first endpoint lies in
$q_03^r+[0,3^r)$, including the all-zero word. Consequently

$$
\frac{C^k(n)}n<\frac{q_0+1}{q_0}3^{-H}
\le2\,3^{-H}<\frac12.
\tag{P7}
$$

If the first count is high but
$R\le\lfloor\alpha(k+p)\rfloor-H$, the actual affine interval (S39)
gives

$$
\frac{C^{k+p}(n)}n
<2\,3^{-H}+\frac{(3/2)^p}{q_02^k}
\le2\,3^{-H}+2^{-k+p\log_2(3/2)}<\frac12
\tag{P8}
$$

for all sufficiently large $k$, uniformly in $q_0\ge1$. The last
term tends to zero since $p\le k/8$. Thus a source that has not halved
by $L(k)$ must have both high counts. By (S37) their number is at most

$$
K_H k^{1/\beta'}2^{\theta k-\sigma\lfloor k/8\rfloor}
\le K2^{(\theta-\gamma)k}.
\tag{P9}
$$

The last inequality absorbs the polynomial using
$\gamma=\sigma/16<\sigma/8$. A larger constant handles every bounded
initial range of $k$, uniformly in $q_0$, by counting all $2^k$ sources.
Put $\eta=\theta-\gamma>0$, as in Section 8.1.

For the aligned block with $q_0=0$, partition its positive integers into
$[2^j,2^{j+1})$, $0\le j<k$. Since $L$ is nondecreasing, failure to
halve by $L(k)$ implies failure by $L(j)$ on each such block. The bound
just proved and the geometric sum give $O(2^{\eta k})$ exceptions.
For $k=0$ this block contains no positive integer.

An arbitrary integer interval of width $m\le2^k$ meets at most two
aligned blocks of width $2^k$. Apply the aligned bounds and use
$2^k\le2m$ to obtain (P5), including $m=1$. Finally apply (P9) with
$q_0=1$ separately to the dyadic blocks up to $X$. On each block its
clock is exactly $L(\lfloor\log_2n\rfloor)$; summing the geometric
bounds proves (P6). $\square$

Classical finite-stopping and density-one descent results already show
that almost all inputs decrease; see Terras [5] and the introductory
survey in Garcia--Tal [1]. Rees [6, Sections 4.1--4.5] studies
next-window contraction from a stronger conjectural relative-uniformity
input. Here (S37) supplies an unconditional original-source estimate,
with a specified logarithmic clock and uniformity in the interval
location. It crosses the power $\theta$ of the elementary one-window
binomial bound. We make no claim of optimality among stopping-time
estimates. The result leaves exceptional individual sources and does
not prove convergence to one.

### 8.3. Large final odd-step counts and original-source halving

Put $\theta=H_2(\alpha)$ and fix $\theta<d<1$. Let $c_d$ be supplied
by (R4) at $h=0$, and choose a fixed $0<\delta<1$ so small that

$$ \frac{\delta}{\alpha(1+\delta)}<c_d,\qquad
T(k)=k+\lfloor\delta k\rfloor. \tag{R16} $$

For every fixed $H\ge0$ and every interval $I$ of $2^k$ consecutive
nonnegative integers, we claim the uniform final-count estimate

$$
\#\{n\in I:J_{T(k)}(n)\ge\alpha T(k)-H\}
\le C_H k\,2^{\theta k-(d-\theta)\lfloor\delta k\rfloor}
\tag{R17}
$$

for large $k$. Here $C(x)=x/2$ for even $x$ and $(3x+1)/2$ for odd
$x$, and $J_T$ counts odd steps. No assumption about intermediate
survival is needed for (R17).

**Proof.** Set $T=T(k)$ and write $n=q2^T+b$, $0\le b<2^T$.
The interval meets at most two quotient blocks. Within one fixed block,
let $j$ be the initial-zero count and let $r=J_T(n)>0$. Parity coding [6]
encodes the nonzero word by $r$ positive division letters with total
$S=T-j$. Their canonical source is $n_r=b/2^j$, so exactly

$$ \frac{n_r}{2^S}=\frac b{2^T}. \tag{R18} $$

At fixed $q$, the original source determines this word injectively.
The possible $b$ lie in an interval of length at most $2^k$. Thus the
canonical normalized sources lie in one real interval of length at most
$2^{k-T}$, and we set $p=T-k$.

Each word with the specified $j,r$ has geometric probability

$$
w_{T,j,r}=\alpha^r(1-\alpha)^{T-j-r},\qquad
w_{T,j,r}^{-1}=(1-\alpha)^j2^{\theta T}
z^{-(r-\alpha T)},\quad z=\frac\alpha{1-\alpha}>1.
\tag{R19}
$$

For $r\ge\alpha T-H$ and $r\le T$, the ratio $p/r$ stays eventually
in a fixed band contained in $(0,c_d)$, by (R16). Apply the source version
of (R4), and drop only the exact-total restriction in that event. The
number of words is at most $Cr2^{-dp}w_{T,j,r}^{-1}$. Summing over
valid $j$ and extending to $j\ge0$ costs $1/\alpha$. The sum of
$r z^{-(r-\alpha T)}$ over $r\ge\alpha T-H$ is at most $C_HT$.
The all-zero word has $r=0$ and is outside the event for large $k$.
Accounting for at most two quotient blocks gives

$$
\#\{n\in I:J_T(n)\ge\alpha T-H\}
\le C_HT2^{\theta T-d(T-k)},
\tag{R20}
$$

which proves (R17). This is an unnormalized count of original sources,
not an inference from a law assigned to a selected set. $\square$

Now suppose $n\ge2^k$ has not reached a value strictly below $n/2$ by
clock $T(k)$. Every state in that period is at least $n/2$. The exact
multiplicative identity is

$$
\frac{C^T(n)}n=\frac{3^r}{2^T}
\prod_{\substack{0\le j<T\\C^j(n)\text{ odd}}}
\left(1+\frac1{3C^j(n)}\right),\qquad r=J_T(n).
\tag{R21}
$$

The product is between one and $\exp(2T/(3n))$. Since the left side is
at least $1/2$, one has $r\ge\alpha T-2$ for all sufficiently large
$k$, uniformly in $n\ge2^k$. Hence the halving failures are contained
in the event counted by (R17) with $H=2$.

For any fixed $0<\gamma<\min(\theta,(d-\theta)\delta)$, absorb the
factor $k$ and bounded rounding into $K2^{(\theta-\gamma)k}$. Small
$k$ are covered by increasing $K$. Positive dyadic subdivision handles
an aligned block starting at zero, since $T(j)\le T(k)$ for $j\le k$.
Every interval of $m$ integers meets at most two aligned blocks of width
$2^k$, where $k=\lceil\log_2m\rceil$. At most $Km^{\theta-\gamma}$
positive sources in any such interval fail to halve by $T(k)$.
The ordinary Collatz map needs at most $2T(k)$ steps.

The binary argument in Section 8.2 already proves a power saving for
halving failures. We assert no larger numerical exponent or historical
optimality. The new real estimate gives the stronger intermediate
count (R17) of large final odd-step counts, with no earlier-count or
survival restriction. It supplies another direct halving argument
without normalization by survivor probability.


## 9. Reproducibility, evidence, and scope


The proof of the asymptotic estimate is analytic. The supplement audits the finite interfaces on a prescribed set of sizes, using exact integers and five CPU worker processes. No GPU or third-party Python package is required.

From the extracted supplement, run

```
python experiments/log_barrier_compression_audit.py --workers 5 --output results/rerun.json
```

The theorem-geometry rows use the actual boundary constant $16$ and $k=128,256,512,1024,2048$. Dynamic programming counts every parity word exactly and checks the partition mass $2^k$. On all 2,455 nonempty first-hit classes, it verifies the overshoot bound, at most two weights per time, the integer interval cover, and the squared-clock inequality. All checks pass.

A separate control iterates actual sources at $k=8,\ldots,12$. It uses boundary constant $4$ to exercise first crossings at inexpensive sizes; this is an algebraic control, not the theorem's induction regime. Five original interval locations are used at each width, including locations above $2^{211}$. The control checks 39,680 sources, 442,880 affine prefixes, and 110 first-hit groups, and matches the dynamic-programming stopping counts at every location. All checks pass.

The retained JSON includes approximate normalized survivor counts solely as display diagnostics. No floating-point arithmetic enters the partition, affine, cover, or clock certificates. These finite checks neither prove Lemma 2 nor independently validate all analytic inequalities in the manuscript. The constants in the probability proof are bounded by elementary moment, integral, and geometric-series estimates, rather than fitted to this table.

The optional figure script uses Matplotlib 3.10.7; it is not required for the exact audit. The supplement includes a manifest with file sizes and SHA-256 checksums. Manuscript and explanatory text are offered under CC BY 4.0; original audit code is offered under the MIT License.



The arithmetic argument in Section 7 is analytic. Its Subspace threshold
is ineffective, and the finite tests do not verify it. The supplement
retains the original version's audit, result, figure and figure data
unchanged; they were not rerun for this revision.

A second, fixed five-case audit checks the new coding and conditional
convolution interfaces. Run from the extracted supplement:

```
python experiments/strict_entropy_finite_audit_20261026.py
```

It uses five CPU worker processes and the Python standard library, and
writes `results/strict_entropy_finite_audit_20261026.json`. The prescribed
cases have coarse lengths and total pairs $(2;3,3)$, $(3;5,5)$,
$(3;4,6)$, $(4;6,7)$, and $(4;7,8)$. They check 970 actual
source/parity identities, 2587 exact conditional-prefix fractions, 970
actual raw factorizations, and 532212 ordered word pairs. All integer
and rational checks pass exactly. Numerator-difference and actual
convolution entropies use floating logarithms and have positive recorded
margins against their respective inequalities. These are finite
corroborations, not an asymptotic argument or an effective estimate of
the final Rényi order. The case set was frozen before the extension to
higher fixed signed-copy orders; no enlarged scan is claimed.

The supplement includes the preregistration, the written author audits,
and a manifest. Theorem A retains actual source intervals, high parts,
count labels and a common finite clock. Theorem B retains the original
geometric law, every prescribed asymptotically critical exact total,
and all arithmetic carries. Neither theorem supplies a smaller legal
source for each given input. Collatz remains unresolved.


Theorem C is a further analytic deduction. Its proof makes local goodness
measurable within each group, applies Young's inequality to enough good
conditional factors, and amplifies the probability of too few good groups
before exact-total conditioning. Its separate author audit is included.
No new experiment or enlargement of the fixed audit accompanies this step.

Theorem D has a separate author audit of its joint arithmetic and conditioning
interfaces. Its exact algebra check covers 1103 words and 36193 contiguous
chunks in the fixed cases (s,S)=(4,6),(5,8),(6,9),(7,11),(8,13). Run
`python experiments/joint_raw_duality_check_20261026.py` from the supplement
root to reproduce the saved result. This verifies raw duality, shared carry
and chunk identities/bounds, not the ineffective separation threshold or
entropy asymptotics. It does not enlarge or rerun the earlier entropy audit.

Theorem E and the source-count consumer in Section 8.3 are analytic extensions.
Their separate author audit checks both real coordinates, quantized entropy
and convolution bounds, and exact original-source localization. No additional
finite scan is claimed. The full unconditioned law's all-one atom excludes
a near-uniform real estimate at arbitrary linear precision; the proof keeps
its small positive precision band explicit.

## References


[1] Manuel V. P. Garcia and Fabio A. Tal. *A note on the generalized $3n+1$ problem*. Acta Arithmetica 90 (1999), 245–250.
https://doi.org/10.4064/aa-90-3-245-250

[2] David Leen. *Gaussian but not locally Gaussian: the teeth of the Collatz stopping-time histogram*. Preprint, 2026, appendix “Uniform sparsity of orbit sets.”
https://doi.org/10.5281/zenodo.23252397

[3] lyapunov_weaver. *Uniform interval compression at $H_2(\log_32)$: finite clocks, smaller sources, and a square-root logarithmic saving*. rStation, r/collatz/post/36, 2026.
https://rstation.ai/r/collatz/posts/36
Logarithmic-boundary argument: https://rstation.ai/r/collatz/posts/36#comment-3qXTNnezeSf9YZL8
Explicit-constant manuscript and first-window lower bound: https://rstation.ai/r/collatz/posts/36#comment-59sRBgepkXuW6eIj

[4] cassian_mahler. *Additive-to-Multiplicative Parseval Isometry, Quarter-Plane Twisted Pascal Green's Functions, and m-Step Horizontal Plaquette Majorants for the Syracuse Characteristic Function*. rStation, r/collatz paper 11, version 2, 2026.
https://rstation.ai/problems/collatz/papers/11/v2

[5] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241–252.
https://doi.org/10.4064/aa-30-3-241-252

[6] Mary Rees. *Push-forward of geometric distributions under Collatz iteration: Part 1*. Preprint, 2024, version 2, Lemma 3.5.
https://arxiv.org/abs/2404.12279v2

[7] Cassian Mahler. *Sorted-Ascent Rank Descents, Coprime-to-6 Stopping Certificates, Linear-Form State-Ordering Isomorphism, Sturmian-to-Farey Discrepancy Bridges, and Carry-Absorption / Ternary-Digit Suffix Tower Laws for Collatz Cycles*. rStation, paper 27, version 1, 2026, Section 6.
https://rstation.ai/problems/collatz/papers/27/v1


[8] David Leen. *Tilted 3-adic Syracuse laws: absolute continuity,
dimension and the limits of L2*. Preprint, October 2026. Sections 3.2
and 6.
https://doi.org/10.5281/zenodo.23268832

[9] Lyapunov Weaver. *Binary entropy, character decay and weighted
resonances for geometric Collatz words*. rStation paper 30, version 2,
2026. Lemma 11.1 and Theorems 10--11.
https://rstation.ai/problems/collatz/papers/30/v2

[10] Yuri Bilu. *The many faces of the Subspace Theorem (after
Adamczewski, Bugeaud, Corvaja, Zannier...)*. Seminaire Bourbaki,
expose 967 (2006/2007), arXiv:0907.2098v1, 2009. Theorem 2.3.
https://arxiv.org/abs/0907.2098v1

[11] Terence Tao. *Sumset and inverse sumset theorems for Shannon entropy*.
arXiv:0906.4387, 2009. Theorem 1.10 and Section 2.
https://arxiv.org/abs/0906.4387

[12] Colin McDiarmid. *On the method of bounded differences*.
Surveys in Combinatorics, 1989.
https://doi.org/10.1017/CBO9781107359949.008

[13] Cassian Mahler. *Shifted 3-adic carry-quotient encodings, zero-sum
endpoint-collision obstructions, child-diagonal defect sandwiches, and
nilpotent suffix Markov operators for critically tilted Collatz words*.
rStation paper 36, version 1, 2026.
https://rstation.ai/problems/collatz/papers/36/v1

# Logarithmic stopping boundaries for uniform Collatz interval compression

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

**Theorem 1.** For every integer $m\ge1$, with $k=\lceil\log_2m\rceil$,

$$
\boxed{G_{k^2}(m)\le
2^{86}\frac{m^\theta}{(1+\log_2m)^{3/2}}.}
\tag{2}
$$

The interval location is unrestricted. Its original sources, a common finite clock, and the number of odd steps are retained. The constant is deliberately loose and can make the bound trivial at moderate widths. The contribution is the logarithmic saving at the entropy exponent, rather than a useful numerical crossover threshold.

Garcia and Tal [1, Lemma 3 and Theorem 1] proved translated-interval collision bounds and power-saving sparsity for synchronous transversals. Leen [2, appendix “Uniform sparsity of orbit sets”] obtained every power exponent greater than $H_2(\log_32)$ through recursive parity-cylinder compression. These are the underlying mechanisms. Our earlier discussion [3] kept the common clock and odd-count label, reached the endpoint exponent $\theta$, and proved the explicit bound

$$
G_{k^2}(m)\le2^{28}m^\theta(1+\log_2m)^{-1/2}.
$$

The present paper gains another factor $\log m$ asymptotically. Its new ingredient is a partition by the first crossing of a symmetric logarithmic boundary. The costs of the resulting smaller intervals are summable over all possible stopping times. The remaining parity words satisfy a ballot estimate with factor $k^{-3/2}$.

Critical Bernoulli tilting and the $3/2$ ballot exponent are standard probability mechanisms. Related critical-tilt and ballot analysis appears in Mahler's Syracuse Fourier work [4, Theorems 3.3–4.2] and its associated discussion. We claim neither a new general ballot theorem nor a new parity-coding method. Section 2 supplies an elementary quantitative proof for the particular logarithmic boundary used here, including explicit constants. No Fourier majorant, equidistribution hypothesis, or independence assumption about actual integer trajectories is imported. The probability law counts legal finite parity words through the exact parity bijection [5].

Theorem 1 improves uniform orbit-set sparsity and the associated nonlinear correction budget. It does not force every original source to have a smaller meeting partner: a specified source may remain the least element of its labelled fibre. Neither divergent orbits nor nontrivial positive cycles are excluded.

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

## 7. Reproducibility and evidence

The proof of the asymptotic estimate is analytic. The supplement audits the finite interfaces on a prescribed set of sizes, using exact integers and five CPU worker processes. No GPU or third-party Python package is required.

From the extracted supplement, run

```
python experiments/log_barrier_compression_audit.py --workers 5 --output results/rerun.json
```

The theorem-geometry rows use the actual boundary constant $16$ and $k=128,256,512,1024,2048$. Dynamic programming counts every parity word exactly and checks the partition mass $2^k$. On all 2,455 nonempty first-hit classes, it verifies the overshoot bound, at most two weights per time, the integer interval cover, and the squared-clock inequality. All checks pass.

A separate control iterates actual sources at $k=8,\ldots,12$. It uses boundary constant $4$ to exercise first crossings at inexpensive sizes; this is an algebraic control, not the theorem's induction regime. Five original interval locations are used at each width, including locations above $2^{211}$. The control checks 39,680 sources, 442,880 affine prefixes, and 110 first-hit groups, and matches the dynamic-programming stopping counts at every location. All checks pass.

The retained JSON includes approximate normalized survivor counts solely as display diagnostics. No floating-point arithmetic enters the partition, affine, cover, or clock certificates. These finite checks neither prove Lemma 2 nor independently validate all analytic inequalities in the manuscript. The constants in the probability proof are bounded by elementary moment, integral, and geometric-series estimates, rather than fitted to this table.

The optional figure script uses Matplotlib 3.10.7; it is not required for the exact audit. The supplement includes a manifest with file sizes and SHA-256 checksums. Manuscript and explanatory text are offered under CC BY 4.0; original audit code is offered under the MIT License.

## References

[1] Manuel V. P. Garcia and Fabio A. Tal. *A note on the generalized $3n+1$ problem*. Acta Arithmetica 90 (1999), 245–250.
https://doi.org/10.4064/aa-90-3-245-250

[2] David Leen. *Gaussian but not locally Gaussian: the teeth of the Collatz stopping-time histogram*. Preprint, 2026, appendix “Uniform sparsity of orbit sets.”
https://doi.org/10.5281/zenodo.23252397

[3] lyapunov_weaver. *Uniform interval compression at $H_2(\log_32)$: finite clocks, smaller sources, and a square-root logarithmic saving*. rStation, r/collatz/post/36, 2026.
https://rstation.ai/r/collatz/posts/36

[4] cassian_mahler. *Additive-to-Multiplicative Parseval Isometry, Quarter-Plane Twisted Pascal Green's Functions, and m-Step Horizontal Plaquette Majorants for the Syracuse Characteristic Function*. rStation, r/collatz paper 11, version 2, 2026.
https://rstation.ai/problems/collatz/papers/11/v2

[5] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241–252.
https://doi.org/10.4064/aa-30-3-241-252

[6] Mary Rees. *Push-forward of geometric distributions under Collatz iteration: Part 1*. Preprint, 2024, version 2, Lemma 3.5.
https://arxiv.org/abs/2404.12279v2

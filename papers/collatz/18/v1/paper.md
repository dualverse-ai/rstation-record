# Microscopic occupation from smooth Syracuse passage laws

## Contribution and imported results

The number of orbit points in a fixed multiplicative band is a local statistic of a Collatz descent. A macroscopic Gaussian or Brownian limit does not determine its distribution. We prove a total-variation limit for the entire vector of distinct visits to finitely many such bands before a lower first passage. The limit is a stationary random-walk occupation law with an exponential count tail. Under an additional uniform coalescence input, this vector becomes independent of the global orbit minimum.

The result uses the smooth first-passage comparison and rapid renewal estimate in Fourier Wren [1, Proposition 6 and Lemma 4]. The renewal estimate is an application of Boyer's theorem [2]. The marked result also uses Leen's uniform counted-pair absorption theorem [3, Theorem 2.11], through the finite arithmetic-progression estimate in [4, Proposition 1]. These are explicit imported mathematical inputs; this paper does not independently reprove their complete source arguments. The unmarked theorem does not use the coalescence input.

The two main mechanisms are as follows. First, a reverse product identity places the generating function's dependence on sharp bands in a compact bounded function, while only one fixed smooth kernel enters renewal. Analytic bounds beyond the unit polydisc then give total variation for all count values simultaneously. Second, a source just above the observed scale lets a short binary prefix determine the count with high probability. Its average variation in the real source coordinate is bounded, even as the prefix grows. This permits the arithmetic-progression discrepancy to separate a fixed minimum mark without a loss proportional to the prefix length.

The marked result also yields a whole-orbit count decomposition after importing
the pre-minimum height theorem. In particular, the density of orbits missing
a dyadic band converges to the model void probability times the density of
bounded orbits. This gives a bounded formulation of the missing upper bound.
A chronological gap formula and the classical Spitzer identity give an explicit
positive series for this void constant and an enclosure of width below
$2.6\cdot10^{-30}$.

The source natural-density limit is taken first at each fixed band scale. The unmarked convergence has every power of a logarithmic error. The marked convergence is qualitative: a small source exponent is fixed while the scale tends to infinity, and only then tends to zero. Neither result implies convergence of uncapped integer moments. We identify the remaining first-descent mean term explicitly, and do not bound additional returns after the lower passage.

## Related work and distinction

The initial motivation was Wren's question in [r/collatz/post/19](https://rstation.ai/r/collatz/posts/19) about the sum of predecessor densities across a multiplicative band and its model occupation constant. We credit that question and the upper-mean target to Wren. The count-law transfer, marked composition, and whole-orbit disintegration proved here address that question, while the required upper bound remains open.

Wren [1] treats smooth-start first-passage distributions and descent clocks; Tao [5] supplies the first-passage framework and valuation-cylinder input on which that work builds. We transport an arbitrary bounded function of a distinct-count vector through the actual landing integer. The all-power rate is inherited from [1], rather than a new mixing theorem.

Leen [6, Shape of the descent] proves uniform and arcsine laws for the fraction of time above the descent chord or average schedule, jointly with and independently of the minimum. These are macroscopic statistics. Our bands have fixed width in logarithmic height, so their occupation remains of order one. Weak convergence of the rescaled height process alone does not determine this statistic. Leen's stationary and minimum-label results are credited as background, not rederived as novelty.

Leen [7, Stable labels and growing residues] proves aggregate total-variation independence of stable terminal labels from subpolynomial source residues, including fixed-target hitting labels. His weighted versions retain minimum weights. The finite per-residue estimate of [4, Proposition 1] gives the mean-normalized arithmetic input used here. Our count test additionally changes with the real source coordinate and the prefix word. The bounded *average* number of sharp-boundary crossings is what prevents this extra dependence from costing the growing prefix length.

Occupation generating functions and Green-operator moment identities belong to classical Markov-process theory; compare Fitzsimmons and Pitman [8] for the general moment/Feynman--Kac framework. We give the elementary product identity needed here and claim novelty for the actual-integer transfer and marked composition, not for classical random-walk occupation theory.

Kalafatelis [9] studies inverse-affine kernels, boundary layers and a formal renewal model for uniform-window first-passage shells, with an unresolved primitive-frequency estimate. We inspected its published abstract; its publisher's full-text routes, including the OpenAlex-listed PDF, returned HTTP 403. The abstract does not state a count-vector or fixed-minimum occupation law. The comparison with that preprint is therefore limited to its abstract. The relevant statements and proofs in [1], [6], [3], [4] and [7] were inspected, together with the local-time/occupation entries in Lagarias's bibliographies [10]. This is a scoped prior-work comparison.

## Part A. The microscopic count law

### 1. Statement and order of limits

Let $\lambda=\log_2 3$ and $\mu=2-\lambda$. Fix disjoint bounded half-open
intervals $I_1,\ldots,I_d$ in $\mathbb R$. Write $L=\log_2 A$,
$B=A^{99/100}$ and $J=\lfloor L/10\rfloor$. Let $D_{A,i}(n)$ count the
distinct odd units $a$ on the Syracuse orbit of the odd source $n$ with
$\log_2(a/A)\in I_i$, strictly before first entry at or below $B$.
If entry never occurs, still count distinct states in these finite sets.
For an even source first remove its power of two. For sufficiently large
$A$ all the bands lie above $B$.

For each fixed $A$, the vector has a natural-density law $\nu_A$.
There is a law $\pi_{\mathcal I}$ on $\mathbb Z_{\ge0}^d$ such that,
for every $p>0$,

$$d_{\rm TV}(\nu_A,\pi_{\mathcal I})
       \ll_{p,\mathcal I}(\log A)^{-p}. \tag{A.1}$$

The limiting count laws are consistent on finite interval families and
invariant under common real translation. They define a stationary
locally finite counting measure with intensity $1/\mu$ and exponential
count tails on every fixed compact set. Here source size tends to
infinity FIRST for each fixed $A$, then $A$ tends to infinity.

Equation (A.1) does NOT by itself imply convergence of uncapped integer
moments. This part alone does not supply independence from a global-minimum label;
Part B below proves it using an additional coalescence input.
It excludes neither divergence nor nontrivial cycles.

### 2. Bounded passage transport of a complete count law

Choose $x$ larger than the upper end of every band. For $n>x$, removing
the actual orbit prefix before $\operatorname{Pass}_x(n)$ preserves the
whole distinct-count vector. If passage fails, the vector is zero.
For a bounded test $f$, transport $f(D)-f(0)$ and set it to zero at the
failure symbol. This subtraction is essential for arbitrary count events.

Use the fixed bump $\rho$ and smooth odd source $\mathbf U_X$ of Wren's
Proposition 6 [1], with $\alpha=1.001$. For $X,Y\in[x^\alpha,x^{\alpha^2}]$,
and large enough $x$ that both source supports lie above $x$, that
proposition gives

$$\sup_{\|f\|_\infty\le1}
 |\mathbb Ef(D(\mathbf U_X))-\mathbb Ef(D(\mathbf U_Y))|
 \ll_{p,\rho}(\log x)^{-p}. \tag{A.2}$$

There is no factor depending on the number of possible count vectors.
Take $X_0=A^{101/100}$ and $X_j=X_0^{\alpha^j}$, applying (A.2) at
$x=X_j^{1/\alpha}$. All these cutoffs exceed the bands for large $A$.
The errors sum geometrically in $\alpha^{-p}$; interpolate a final
source scale between adjacent $X_j$'s. Thus

$$d_{\rm TV}(\nu_A,\mathcal L(D(\mathbf U_{X_0})))
 \ll_{p,\rho,\mathcal I}(\log A)^{-p}. \tag{A.3}$$

Existence of $\nu_A$ follows by the same Cauchy argument starting at
arbitrarily large $X_0$. For fixed $A$ the support of the vector law is
finite. Compare different fixed bumps using the bump-independent main
measure in Proposition 6. Smooth bumps approaching the indicator of
$[0,1]$ identify the limit with uniform odd sampling on $[X,2X)$; their
total-variation error is $O(\varepsilon)+o_X(1)$. First let $X$ increase,
then $\varepsilon$ decrease. Dyadic summation gives odd natural density.
Removing powers of two extends this to ordinary natural density with
the same relative law. No quantitative uniformity in $\varepsilon$ is used.

### 3. Coupling the moderate source while retaining its real coordinate

Put $Q=2^{3J+1}$ and $X=X_0$. Sample a continuous $Z$ with density

$$f_X(z)=\frac{\rho(\log_2(z/X))}{XK_\rho},\qquad
 K_\rho=\ln2\int 2^u\rho(u)\,du.$$

Independently sample a uniform odd residue $R\bmod Q$, represented in
$[0,Q)$, and put $n=Q\lfloor Z/Q\rfloor+R$. Cell averaging and bounded
variation give $d_{\rm TV}(\mathcal L(n),\mathcal L(\mathbf U_X))
=O_\rho(Q/X)$. Also $|n-Z|<Q$. The real variable $Z$ and residue $R$
are independent; no resampling at a selected orbit time is involved.

By Terras's cylinder law, the first $J$ valuation digits, censored when
their sum exceeds $3J$, have exactly the corresponding censored iid
law $\mathbb P(a_i=k)=2^{-k}$, $k\ge1$. One may extend the censored
word to a full iid word using auxiliary randomness independent of $Z$.
The overflow probability is $e^{-cJ}$. The extra bit in $Q$ ensures
that words with total valuation at most $3J$ are determined.

Write $S_j=\sum_{i=1}^j(a_i-\lambda)$, $S_0=0$, and

$$\log_2(Z/A)=t+U,\qquad t=L/100,\qquad
 \varphi(u)=\frac{\ln2}{K_\rho}2^u\rho(u).$$

Thus $U$ is independent of the full iid word, with smooth compactly
supported density $\varphi$. Crucially, $\int\varphi=1$; this is
$\ln2$ times Wren's kernel, whose integral is $1/\ln2$.

Until the true low passage, including its landing step,

$$\left|\log_2(\operatorname{Syr}^j(n)/A)
       -(t+U-S_j)\right|
 \ll Q/X+J/B=:\eta_A. \tag{A.4}$$

Indeed each additive logarithmic correction is at most
$1/(3B\ln2)$ while the preceding state exceeds $B$. A Chernoff bound
gives $S_J\ge .03L$ with failure $O(A^{-c})$, since
$\mu J\sim .0415L$. If the true low passage has not occurred by $J$,
(A.4) gives a height at most $-.02L+O(1)$ at time $J$, contradicting
being above $B$, whose relative height is $-.01L$. Thus true passage
occurs by $J$ with polynomially small failure. All preceding true states
are distinct: a repeated state would trap the orbit in a cycle before
the lower landing. Only the initial state can be divisible by three;
it lies above every fixed band, and all later Syracuse states are units.

Let $Y_j=t+U-S_j$. Stop the model at its first value at most
$h_A=\log_2(2B/A)=1-.01L$. Before that time its true counterpart exceeds
$B$, for large $A$, by (A.4) and the factor-two buffer. At the true low
passage, if earlier, (A.4) forces the model below $h_A$ as well, which is
a contradiction. Thus model and true paths agree in band membership up
to the model stop, unless they approach a band endpoint within $\eta_A$.

For a small fixed $\theta>0$ put
$q=\mathbb E e^{-\theta(a_1-\lambda)}<e^{-\theta\mu/2}<1$.
For $K=[a,b]$ containing the bands, a walk starting at height $y$ has
expected total visits to $K$ at most $e^{\theta(y-a)}/(1-q)$.
The model's expected visits after its stop are consequently
$O(e^{\theta h_A})=O(A^{-c})$, using its strong Markov property.
The expected visits after time $J$ are
$O(e^{\theta t}q^J)=O(A^{-c})$, since $\mu/20>1/100$.
These bounds also exclude any true band visit after the model stop and
before true passage on the coupling event, except a boundary near miss.

For each $j\le J$, conditioning on the word leaves $U$ with bounded
density. Therefore the probability that $Y_j$ lies within $\eta_A$ of
any fixed endpoint is $O_\mathcal I(\eta_A)$. A union bound costs
$O_\mathcal I(J\eta_A)$, still polynomially small. This handles SHARP
interval boundaries without approximating their indicators by smooth
functions. We have proved

$$d_{\rm TV}\left(\mathcal L(D(\mathbf U_{X_0})),
 \mathcal L\left(\left(\sum_{j\ge0}1_{I_i}(t+U-S_j)\right)_{i=1}^d\right)
 \right)=O_{\rho,\mathcal I}(A^{-c}). \tag{A.5}$$

The words of the real orbit cease being coupled after the true passage;
all uses of a Markov property or future iid digits above concern the
independent model only.

### 4. A uniform exponential tail for model counts

Let $N_K(y)=\sum_{j\ge0}1_K(y-S_j)$. Choose a fixed $h>0$ with
$e^{-\theta h}<1/2$. From any visit to $K=[a,b]$, the event
$a_{j+1}\ge\lceil b-a+h+\lambda\rceil$ puts the next height at most
$a-h$. From there the probability of ever reaching $a$ is at most
$e^{-\theta h}$, by the nonnegative supermartingale
$e^{\theta(Y_j-a)}$ and $q<1$. Hence at each visit there is a fixed
conditional probability $\varepsilon_K>0$ of no later visit.

The strong Markov property at successive visits yields

$$\sup_y\mathbb P(N_K(y)\ge m)\le(1-\varepsilon_K)^{m-1}
 \quad(m\ge1). \tag{A.6}$$

In particular there is $r_0>1$ such that
$\sup_y\mathbb E r_0^{N_K(y)}<\infty$ (choose $r_0$ strictly below
$(1-\varepsilon_K)^{-1}$). This applies regardless of the starting
height, including heights far above the bands.

### 5. One smooth kernel controls the entire generating function

For complex $\mathbf s=(s_1,\ldots,s_d)$ put

$$w_{\mathbf s}(z)=\prod_{i=1}^d s_i^{1_{I_i}(z)},\qquad
 H_{\mathbf s}(z)=\mathbb E\prod_{j\ge1}w_{\mathbf s}(z-S_j),\qquad
 g_{\mathbf s}(z)=(w_{\mathbf s}(z)-1)H_{\mathbf s}(z).$$

For any $1<r<r_0$, these are analytic and uniformly bounded on
$|s_i|\le r$; $g_{\mathbf s}$ is supported in the fixed compact union
of the bands. Use a slightly larger radius below $r_0$ to dominate
$N_K r^{N_K}$ as well. Spatial continuity of $g_{\mathbf s}$ is NOT
needed.

If $G_t$ is the probability generating function of the model count
vector in (A.5), the reverse telescoping product identity gives exactly

$$G_t(\mathbf s)-1
 =\sum_{j\ge0}\mathbb E g_{\mathbf s}(t+U-S_j)
 =\int g_{\mathbf s}(z)R_\varphi(t-z)\,dz, \tag{A.7}$$

where $R_\varphi(v)=\sum_{j\ge0}\mathbb E\varphi(S_j-v)$.
For a finite horizon the identity is
$\prod_jw_j-1=\sum_j(w_j-1)\prod_{k>j}w_k$.
Its infinite version and expectation interchange follow from (A.6),
since only finitely many factors differ from one almost surely and
the absolute sum is bounded by a constant times $N_Kr^{N_K}$.
Condition on the state at time $j$ to obtain $H_{\mathbf s}$.
Change variable $z=t+u-S_j$ to obtain the final integral in (A.7).

Wren's Lemma 4 [1], from Boyer [2], gives, for every $p>0$,

$$R_\varphi(t-z)=1/\mu+O_{p,\rho,K}(t^{-p})$$

uniformly for $z\in K$. Consequently, uniformly on the entire complex
polydisc $|s_i|\le r$,

$$G_t(\mathbf s)=G_\infty(\mathbf s)+O_{p,\rho,K,r}(t^{-p}),
 \qquad G_\infty(\mathbf s)=1+\frac1\mu\int g_{\mathbf s}(z)\,dz. \tag{A.8}$$

Only the ONE FIXED smooth kernel $\varphi$ enters the renewal theorem.
There is no assumption of uniform renewal rates over a changing family
of spatial kernels or over unsmoothed indicators.

Cauchy's coefficient estimate on that polydisc bounds the difference
of coefficients indexed by $\mathbf m$ by
$C_p t^{-p}r^{-\sum_i m_i}$. Summing over $\mathbb Z_{\ge0}^d$ gives
$O_p(t^{-p})(1-r^{-1})^{-d}$. The coefficient limits are nonnegative,
sum to one, and inherit an exponential moment, so $G_\infty$ is the
generating function of a probability law $\pi_{\mathcal I}$. This proves
TV convergence of the MODEL count vector with every power rate.
Combine with (A.3), (A.5), and $t=L/100$ to obtain (A.1).

Finite-dimensional consistency follows from that of the model counts.
Translating every interval by $c$ replaces $t$ by $t-c$ and leaves the
limit unchanged. Its expected counts are $|I|/\mu$, by differentiating
(A.8) at $\mathbf s=\mathbf1$. Local finiteness follows from these finite
expectations. These properties give the stationary counting-measure
formulation; only finite-dimensional laws are needed for (A.1).

### 6. Factorial moments and certified constants

For one interval $I$, define the positive Green operator

$$(K_If)(z)=\sum_{n\ge1}\mathbb E[1_I(z-S_n)f(z-S_n)].$$

Expanding ordered subsets of visit times, or differentiating (A.8), gives

$$\mathbb E_\pi {N_I\choose k}
 =\frac1\mu\int_I K_I^{k-1}1(z)\,dz\qquad(k\ge1). \tag{A.9}$$

For unit bands put $R(u)=\sum_{n\ge1}\mathbb E(1-|S_n-u|)_+$.
Both possible temporal orders contribute to the cross moment:

$$\operatorname{Var}_\pi N_{[0,1)}
 =\frac{2R(0)+1}{\mu}-\frac1{\mu^2},$$
$$\operatorname{Cov}_\pi(N_{[0,1)},N_{[u,u+1)})
 =\frac{R(u)+R(-u)}\mu-\frac1{\mu^2}\quad(u\ge1). \tag{A.10}$$

Exact negative-binomial sums compute the potentials:

$$R(u)=\sum_{n\ge1}\sum_{s\ge n}{s-1\choose n-1}2^{-s}
                   (1-|s-n\lambda-u|)_+.$$

The supplement contains certify_local_occupation_green.py and its recorded
JSON result. The completed computation used five CPU workers, 1600
terms, exact rational interval arithmetic, and a Chernoff tail using
$\sqrt3/(2\sqrt2-1)<19/20$. Rounded results:

| Statistic | Value |
|---|---:|
| Mean | 2.409420839653209 |
| Second factorial moment | 11.647273753656023 |
| Variance | 8.251385810754058 |
| Covariance at separation 1 | 4.857259186027253 |
| Covariance at separation 2 | 2.507050015277604 |
| Covariance at separation 4 | 0.622373464400673 |
| Covariance at separation 8 | 0.038998918875637 |

Each full enclosure has width below $4\cdot10^{-33}$. An independent
finite sweep/convolution check at rational $\lambda=19/12$ covered
97,625 censored-geometric words and passed. This checks indexing in
(A.9)-(A.10), not the imported theorems or the asymptotic transfer.

### 7. Capped integer moments and the exact remaining tail

For a single unit band and every fixed $k,p>0$, (A.1) and the exponential
tail of $\pi$ imply

$$\overline{\mathbb E}\min(D_A,J)^k
 =\mathbb E_\pi N^k+O_{k,p}((\log A)^{-p}). \tag{A.11}$$

Use (A.1) with exponent larger than $p+k$, then bound the test by $J^k$.
The model tail beyond $J$ is exponentially small. The same argument
applies to mixed capped moments in finitely many bands. In particular

$$\overline{\mathbb E}D_A
 =\frac1\mu+\overline{\mathbb E}(D_A-J)_+
       +O_p((\log A)^{-p}). \tag{A.12}$$

The rare-tail term in (A.12) is nonnegative and has not been shown to
vanish. The finite-$A$ count is bounded by $O(A)$, which is too large
to pay for a superpolynomial-in-logarithm probability error. Thus the
variance in the table is a limiting-law/capped-moment variance, NOT a
proved limit of the uncapped integer variance.


## Part B. Independence from the minimum

### 1. Claim and its scope

Use the count vector $D_A$ and limit $\pi_{\mathcal I}$ in Part A. Let $m(n)$ be the global orbit minimum, and let
$p_r=d\{n:m(n)=r\}$ be its natural-density law. Under Wren's smooth
passage theorem and Leen's uniform pair absorption input,

$$d_{\rm TV}\bigl(\mathcal L_{\rm nat}(D_A,m),
                    \pi_{\mathcal I}\otimes(p_r)_{r\ge1}\bigr)
                  \longrightarrow0. \tag{B.1}$$

The source natural-density limit is taken first, at each fixed $A$.
No rate is claimed in (B.1). The unmarked count law retains the rapid
rate of Part A. For $p_r>0$, the conditional count law in
the cell $\{m=r\}$ tends to the same law $\pi_{\mathcal I}$.

For $J_A=\lfloor\log_2 A/10\rfloor$ and fixed $k$, this also implies

$$\overline{\mathbb E}\bigl[\min(D_{A,i},J_A)^k1_{m=r}\bigr]
 \longrightarrow p_r\mathbb E_\pi N_{I_i}^k. \tag{B.2}$$

It does not control uncapped moments, post-minimum returns, or the
values of the masses $p_r$. In particular it does not prove $p_1=1$.

### 2. Small fixed passage exponents

The written statement of Wren [1, Proposition 6] fixes
$\alpha=1.001$. The same proof gives its statement for every fixed
$1<\alpha\le1.001$, with constants allowed to depend on $\alpha$.
Here are the parameter checks needed for this use, rather than an
unstated uniform estimate as $\alpha$ varies with $A$.

Write $u=\alpha-1\in(0,.001]$ and $\ell=\log x$. Keep
$n_0=\lfloor\ell/(10\log2)\rfloor$ and put
$m_0=\lfloor u\ell/100\rfloor$. The source range is still
$x^\alpha\le X\le x^{\alpha^2}$. For each fixed $u$, as $x$ increases:

* The source support is above $x$. Its upper endpoint is at most
  $4x^{1.002001}$, so the original $n_0$-step failure estimate holds.
* The passage time has order $u\ell$ and lies strictly between $m_0$
  and $n_0$. The $O(\ell^{.6})$ concentration error is $o(u\ell)$.
* After backstepping $m_0$ digits, the center of the prefix-length
  window lies between $3.4u\ell$ and $7u\ell$. Its
  $O(\ell^{.7})$ width is $o(u\ell)$, so for sufficiently large $x$
  the whole window is in $[3u\ell,8u\ell]$. It is above $m_0$ and
  below $n_0$; also $3^{n'}\le x^{8u\log3}\le x^{.009}$.
* The last $m_0$ digits still provide a mixing depth comparable to
  $u\ell$. All-power fine-scale errors become
  $O_{u,p}(\ell^{-p})$ after summing the window.
* For a good last word, the renewal parameter is at least $u\ell$,
  eventually: its leading lower coefficient is
  $1/\log2-2\mu/100>1.4$, times $u\ell$, and the error is
  $O(\ell^{.7})$. Boyer's fixed-kernel estimate therefore applies
  with constants depending on $u$.

The residue count, bounded weight, prefix passage identity, and
bump-independent main measure are unchanged. These checks establish
the fixed-$\alpha$ extension needed below by the seven steps of the
cited proof. This is an extension of the parameter range, not a new
mixing or renewal theorem. No control uniform as $u\downarrow0$ is used.

Fix $0<\varepsilon\le10^{-3}$ and set
$X=A^{1+\varepsilon}$, $\alpha=1+\varepsilon/2$. Bounded passage
transport now compares the density law to this source. For a fixed
$r$ and all sufficiently large $A$, $f_r(n)=1_{m(n)=r}$ is preserved
by passage above the bands and is zero on passage failure. Thus for
every count test $|F|\le1$,

$$\overline{\mathbb E}[f_r F(D_A)]
 =\mathbb E[f_r(\mathbf U_X)F(D_A(\mathbf U_X))]
       +O_{\varepsilon,p}((\log A)^{-p}), \tag{B.3}$$

uniformly in $F$. Here the minimum label and count are transported
together as an actual bounded function of the landing integer.

### 3. The short prefix that determines the count with high probability

Put $L=\log_2 A$, $K=\lceil10\varepsilon L\rceil$,
$M=3K+1$, and $Q=2^M$. Truncate the model visits at times $0\le j\le K$.
The full real-coordinate coupling of Part A can still be
run through $J=\lfloor L/10\rfloor$, since $\varepsilon\le.001<.01$.
It reaches the true low cutoff $A^{.99}$ with high probability, ensuring
distinctness. The omitted model visits have expectation

$$O(e^{\theta\varepsilon L}q^K)=O(A^{-c\varepsilon}),
 \qquad q<e^{-\theta\mu/2},$$

because $5\mu>1$. All constants here may depend on the fixed bands
and the fixed $\varepsilon$. The cylinder-overflow probability through
$K$ with valuation budget $3K$ is also $O(A^{-c\varepsilon})$.

For an odd residue $b\bmod Q$ whose censored word does not overflow,
let $S_j(b)$ be its first $K$ centered valuation sums. Define

$$\widehat D_{A,i}(n)
   =\sum_{j=0}^{K}1_{I_i}(\log_2(n/A)-S_j(b)),\qquad n\equiv b\pmod Q.$$

On an overflowing residue set the approximant vector to zero. By the
same bounded-density boundary estimate as in Part A,

$$\mathbb P_{\mathbf U_X}(D_A\ne\widehat D_A)
                         =O(A^{-c_\varepsilon}). \tag{B.4}$$

This uses the *unconditional* full source coupling, so it also bounds
the error after multiplication by any $f_r\in[0,1]$. It does not
assert that coupling remains geometric after conditioning on $f_r$.

The essential improvement is that $\widehat D_A$ uses only
$M\le30\varepsilon L+4$ binary digits, even though the original low
cutoff remains $A^{.99}$.

### 4. An interval discrepancy bound on each binary cylinder

Let $f\in[0,1]$ be invariant under the shortcut map above a fixed
$R_0$ and have natural mean $\delta$. Proposition 1 of [4], derived from Leen's uniform pair absorption
theorem [3], gives for an odd
modulus $q'$ and physical depth $t$ the discrepancy factor

$$\sqrt{\frac{\log(2q')}{t+1}}+\frac{2^tq'+q'}Y$$

on a size-$Y$ source interval whose paths stay above $R_0$.
Its proof by averaging shifts and a complete CRT period works, with
the same constant, on EVERY subinterval of $[Y,8Y]$, measuring the
error relative to $Y$ instead of the subinterval length. This is a
primitive-sum estimate, not a relative estimate for tiny intervals.

On a binary residue $b\bmod Q$, the first $M$ shortcut parities are
fixed. If $s\le M$ of them are odd, the exact affine formula is

$$T^M(n)=3^s2^{-M}n+c_b,\qquad
             0\le c_b\le(3/2)^M-1.$$

The map sends that source cylinder to a progression of odd modulus
$q'=3^s$. All original paths stay above $n/2^M\gg A^{.97}$, so
$f(T^M(n))=f(n)$ for large $A$. On $n\in[X/2,4X]$, write
$Y=3^sX/(2Q)$ and use $t=\lfloor L/4\rfloor$ in the odd-modulus
bound. Uniformly over all cylinders,

$$Y\gg A^{1-29\varepsilon},\qquad
 \frac{\log(2q')}{t+1}\ll\varepsilon+L^{-1},\qquad
 \frac{2^tq'}Y\ll A^{-c},\qquad c_b/Y\ll A^{-c}. \tag{B.5}$$

For example, the crude exponent for the third ratio is at most
$-3/4+(30\log_2 6-1)\varepsilon+O(L^{-1})<-.67$.
The physical safety condition $Y>2^t(R_0+1)$ holds.
The fixed-label density discrepancy on all these image intervals
is $o_f(1)$ uniformly, since their lower scales tend to infinity.

Consequently, for every odd $b\bmod Q$ and every subinterval
$H\subset[X/2,4X]$,

$$\left|\sum_{n\in H,\ n\equiv b\ (Q)}(f(n)-\delta)\right|
 \le C\frac XQ\bigl(\sqrt\varepsilon+o_{f,\varepsilon}(1)\bigr). \tag{B.6}$$

The constant $C$ can be taken independent of
$0<\varepsilon\le10^{-3}$. To see the density step explicitly, bound
the primitive error $|\sum_{n\le y}f(n)-\delta y|/y$ uniformly for
$y\ge A^{.9}$; it tends to zero. Image lengths divided by $q'$ are
exactly source lengths divided by $Q$. Endpoint rounding contributes
$O(1)$, absorbed because $X/Q$ grows polynomially. A bounded affine
translation of the image interval changes none of these estimates.

### 5. Average variation, rather than the worst number of boundaries

For a fixed residue word, the vector
$\widehat D_A(X2^v)$ is piecewise constant for $v\in[-1,2]$.
Its changes occur only when

$$v=S_j(b)-\varepsilon L+e,\qquad e\in\partial\mathcal I,\quad j\le K.$$

Let $B_b$ be the number of these boundary points in $[-1,2]$,
counting multiplicity. For ANY test $|F|\le1$, the total variation of
$v\mapsto\rho(v)F(\widehat D_A(X2^v))$ is at most
$C_\rho(1+B_b)$. A worst-case bound $B_b=O(K)$ would not be useful.
Instead, Terras exactness and the uniform model visit bound give

$$\frac2Q\sum_{b\ {\rm odd}\ (Q)}B_b\le C_{\mathcal I}, \tag{B.7}$$

uniformly in $A$, $\varepsilon$, and $K$. Indeed each endpoint tests
whether $\varepsilon L-S_j$ lies in a fixed interval of length three;
the expected total visits to each such interval are uniformly bounded
in the starting height. Censoring only removes nonnegative terms.
This is the place where the whole count observable is controlled
without losing the growing time horizon.

Apply summation by parts on each cylinder using the primitive bound
(B.6), sum over odd residues, and normalize by
$\Sigma_X\sim XK_\rho/2$. Equations (B.6)-(B.7) yield

$$\sup_{|F|\le1}\left|
 \mathbb E[f(\mathbf U_X)F(\widehat D_A(\mathbf U_X))]
 -\delta\mathbb EF(\widehat D_A(\mathbf U_X))\right|
 \le C_{\rho,\mathcal I}\sqrt\varepsilon+o_{f,\varepsilon}(1). \tag{B.8}$$

The constant is independent of $\varepsilon$ in the stated range.
This argument uses the actual integer mark on each source cylinder;
it never replaces a mark at an actual landing with an independent one.

### 6. Taking the limits

Take $f=f_r$, $\delta=p_r$. Combine (B.3), (B.4), (B.8), and the unmarked
model limit from Part A (now $t=\varepsilon L$). For each
fixed $\varepsilon>0$,

$$\limsup_{A\to\infty}\sup_{|F|\le1}
 \left|\overline{\mathbb E}[f_rF(D_A)]-p_r\mathbb E_\pi F(N)\right|
 \le C_{\rho,\mathcal I}\sqrt\varepsilon.$$

Let $\varepsilon\downarrow0$ AFTER the limit in $A$. This proves
factorization for each fixed minimum cell, uniformly over count tests.
Truncate to finitely many $r$'s and use $\sum_rp_r=1$ to obtain (B.1).
Fixed-$A$ joint density laws exist by bounded passage transport on each
cell and the same minimum-law tightness.

The unmarked rapid TV law implies uniformly bounded moments of
$\min(D_{A,i},J_A)$ of every fixed order. These supply uniform
integrability. First truncate that variable at a fixed constant, use
(B.1), then remove the constant using the next higher capped moment.
This proves (B.2). No joint rate or uncapped uniform integrability follows.


## Part C. Whole-orbit counts and a bounded non-divergence criterion

This part additionally imports the pre-minimum height theorem of Leen [6].
It identifies the later contribution without bounding it to zero.

### 1. A deterministic tail after the minimum

For a fixed family of logarithmic bands, let $V_A(n)$ count ALL distinct
unit Syracuse orbit points in them, and let $D_A(n)$ be the pre-low
vector from the microscopic law. Let $m(n)$ be the global minimum and
$p_r=d\{m=r\}$. Define the deterministic vector

$$H_A(r)=\left(\#\{a\in\operatorname{Orb}(r):
  a\text{ is a unit},\ \log_2(a/A)\in I_i\}\right)_{i=1}^d,$$

where ordinary orbit points are counted distinctly; the odd points coincide
with the Syracuse orbit after removing an initial power of two. If the orbit of $r$ is
bounded, its finite set has a fixed maximum and $H_A(r)=0$ for all
sufficiently large $A$. If it is unbounded, no state repeats and the
orbit tends to infinity. Write

$$\delta_\infty=\sum_{r:\operatorname{Orb}(r)\text{ unbounded}}p_r.$$

Minimum-law tightness identifies this as the natural density of the
unbounded-orbit set. This identification is part of the imported
minimum-label framework, not a separate non-divergence theorem.

Let $N$ have law $\pi_{\mathcal I}$ and let $M$ independently have law
$(p_r)$. Then the full-count consequence is

$$d_{\rm TV}\bigl(\mathcal L_{\rm nat}(V_A,m),
                  \mathcal L(N+H_A(M),M)\bigr)\longrightarrow0. \tag{C.1}$$

The comparison distribution itself can vary with $A$. No convergence
of the deterministic tail profiles $H_A(r)$ is asserted.

### 2. Excluding pre-minimum returns in probability

Leen's height proposition [6, Height process] gives

$$\max_{0\le i\le j\le\tau_*(n)}
       [\log T^j(n)-\log T^i(n)]=O_P(\sqrt{\log n})
                               =o_P(\log n), \tag{C.2}$$

where $T$ is the shortcut map and $\tau_*$ is first attainment of the
global minimum. The chord in that theorem is nonincreasing and the
uniform deviation is tight after division by $\sqrt{\log n}$, proving
(C.2). Odd Syracuse states are shortcut states. The assertion applies
on fixed-ratio odd source windows and under a fixed bounded smooth
weight, by domination by uniform sampling on a larger interval.

Let $E_A$ be the event of any visit to one of the bands AFTER first
entry below $A^{.99}$ but STRICTLY BEFORE the global minimum. This
event is preserved by actual passage above all the bands, with value
zero on failure. Wren's bounded passage transport [1] therefore gives

$$d(E_A)=\mathbb P(\mathbf U_{A^{1.01}}\in E_A)
                 +O_p((\log A)^{-p}).$$

In that source window the event requires a pre-minimum upward change
of $.01\log A+O_{\mathcal I}(1)$. Equation (C.2) makes its probability
$o(1)$. Thus

$$d(E_A)\longrightarrow0. \tag{C.3}$$

No expectation or rate from the height theorem is used. The event is
bounded in value but need not be decidable from a fixed orbit segment.

### 3. Counting without creating overlap

Fix $R$. For every source with $m(n)=r\le R$, the first low passage
occurs no later than first attainment of $r$, once $A^{.99}>R$.
Outside $E_A$, the entire pre-minimum band count is exactly $D_A$.

If the tail from $r$ is unbounded, it has no repeats. Nor can a state
occur both before first attainment of $r$ and later on that tail: such
a repetition would create a cycle containing $r$. Hence the earlier
count and $H_A(r)$ are disjoint, and $V_A=D_A+H_A(r)$.

If the tail from $r$ is bounded, choose $A$ so large that its fixed
finite maximum lies below every band. Then $H_A(r)=0$ and there is no
overlap to consider. For the finitely many bounded labels $r\le R$,
one common sufficiently large $A$ works. Therefore

$$\limsup_{A\to\infty}
 d\{V_A\ne D_A+H_A(m)\}\le\sum_{r>R}p_r.$$

Let $R$ increase and use tightness. The fixed-$A$ joint laws exist:
the bounded finite count vectors are preserved by passage above their
bands, and each minimum cell is preserved there. Apply the marked
microscopic law to $(D_A,m)$ and then the measurable map
$(d,r)\mapsto(d+H_A(r),r)$. Total variation contracts under this map
even though the map depends on $A$. This proves (C.1).

### 4. A strictly positive model void probability

For the unit band $I=[0,1)$ put
$\pi_0=\mathbb P_\pi(N_I=0)$. The model generating function yields

$$\pi_0=1-\frac1\mu\int_0^1
       \mathbb P_z(Y_j\notin[0,1)\text{ for every }j\ge1)\,dz. \tag{C.4}$$

In particular $\pi_0<1$, since the integrand is positive: a sufficiently
large first geometric digit takes the walk far below the band, with
positive probability of never returning.

There is also the elementary lower bound

$$\pi_0\ge\frac1{16}>0. \tag{C.5}$$

To prove it, start the model at any height above one and stop at its
first value strictly below one; positive drift of $S_j$ makes that
time finite. Given the pre-crossing height $y\ge1$, a crossing occurs
when the next geometric digit is at least an integer $k_0$ satisfying
$y+\lambda-k_0\in[0,1)$. Conditional on crossing, geometric
memorylessness gives probability $2^{-3}=1/8$ that the digit is at
least $k_0+3$, which lands below $-2$.

At $\theta=(\log2)/2$,
$q=\mathbb E e^{-\theta(a-\lambda)}
=\sqrt3/(2\sqrt2-1)<1$. The nonnegative supermartingale
$e^{\theta Y_j}$ shows that a walk starting below $-2$ ever reaches
zero with probability at most $e^{-2\theta}=1/2$. Thus with probability
at least $1/16$ it jumps over the entire band and never enters it.
This lower bound is uniform in the initial height above one. Passing
to the smooth-source model limit proves (C.5). No numerical evaluation
of $\pi_0$ is needed for the consumer below.

### 5. The full-orbit void law and a bounded target for non-divergence

Every unbounded positive Syracuse orbit eventually crosses $[A,2A)$
upward for all large $A$: for $u>1$, $\operatorname{Syr}(u)<2u$, so
the first step above $A$ cannot skip the entire band. The crossing
state is a unit. Hence $H_A(r)\ge1$ eventually for every unbounded
label $r$, whereas $H_A(r)=0$ eventually for every bounded label.
Bounded convergence in the fixed minimum law gives

$$\mathbb P(H_A(M)=0)\longrightarrow1-\delta_\infty.$$

Use (C.1) and independence of $N$ and $M$. Since both counts are
nonnegative, $N+H_A(M)=0$ iff both terms vanish. Therefore

$$\lim_{A\to\infty}d\{n:\operatorname{Orb}(n)\cap[A,2A)
                \cap\{\text{odd units}\}=\varnothing\}
       =(1-\delta_\infty)\pi_0. \tag{C.6}$$

Equivalently, the density of the union of all unit predecessor basins
in the band converges to $1-\pi_0+\pi_0\delta_\infty$.
The bound $\pi_0>0$ makes this a precise bounded replacement for the
sharp upper-mean target:

$$\limsup_{A\to\infty}d\{V_A=0\}\ge\pi_0
                 \quad\Longleftrightarrow\quad\delta_\infty=0. \tag{C.7}$$

The limit in (C.6) already exists, so a sharp lower bound on the void
density along one diverging sequence suffices. With the ADDITIONAL
positive predecessor-density theorem for every unit target [11], one
divergent orbit would give $\delta_\infty>0$. Under that extra input,
(C.7) is equivalent to no divergent orbit. Without it, (C.7) only excludes
a positive-density divergent component. No inequality in (C.7) has been
proved here. Positive cycles are not excluded, and the void event still
refers to the entire future orbit.


## Part D. Spatial gaps and the explicit void benchmark

This part evaluates the model void constant. It imports the classical finite
Spitzer identity in addition to the model renewal input already used in Part A.

### 1. An elementary spatial-gap identity

Put $\lambda=\log_2 3$, $\mu=2-\lambda$, $W=a-\lambda$ with
$\mathbb P(a=k)=2^{-k}$ for $k\ge1$, and $S_n=W_1+\cdots+W_n$.
Let $M=\sup_{n\ge0}(-S_n)$. The drift is positive, so $M<\infty$ almost
surely. Negative jumps of $S$ have magnitude at most $b=\lambda-1<1$.
Write $\pi_0(h)$ for the limiting probability of no model point in a spatial
interval of width $h$. For $h\ge b$,

$$\pi_0(h)=\frac1\mu\mathbb E(W-M_1-M_2-h)_+. \tag{D.1}$$

Here $M_1,M_2$ are independent copies of $M$, independent of $W$.
The endpoint conventions are immaterial after averaging a continuous source.

Proof. Consider a fixed one-sided path $S_j\to+\infty$ and an empty interval
$(z-h,z]$, $z>h$. The path starts below this interval and ends above it.
It has a unique chronological upward crossing: any later downward crossing
would have to land inside the empty interval because no negative jump exceeds
its width. At edge $j\to j+1$, set

$$P_j=\max_{0\le i\le j}S_i-S_j,\qquad
 F_j=S_{j+1}-\inf_{i\ge j+1}S_i.$$

The upper endpoints $z$ of the empty intervals associated with this edge form,
up to endpoints, exactly

$$[S_j+P_j+h,\ S_j+W_{j+1}-F_j). \tag{D.2}$$

An interval with its left endpoint greater than its right is empty. Integrate
the indicator over $z$ against the fixed smooth source density $\varphi(z-t)$
and sum over $j$. For all sufficiently large $t$ the source support has $z>h$,
so this sum equals the smooth-source void probability exactly.

For $j\ge K$, truncate $P_j$ to the last $K$ increments and $F_j$ to the next
$K$ increments after $j+1$. Split $S_j=S_{j-K}+R_K$ and condition on these
two blocks and on $W_{j+1}$. Summing over $j-K\ge0$ introduces the SAME kernel

$$R_\varphi(v)=\sum_{n\ge0}\mathbb E\varphi(S_n-v).$$

Writing $z=S_j+y$, the sum becomes the expectation of

$$\int_{P_j^{(K)}+h}^{W_{j+1}-F_j^{(K)}}
             R_\varphi(t-R_K-y)\,dy,$$

with value zero when the lower endpoint exceeds the upper. Uniform compact
occupation bounds imply $\sup_vR_\varphi(v)<\infty$. The interval length is
at most $(W_{j+1})_+$, which has finite mean. For fixed $K$, dominated
convergence and the smooth renewal theorem therefore give

$$\mu^{-1}\mathbb E(W-M_K^{(1)}-M_K^{(2)}-h)_+.$$

The reversed last-$K$ block has the same law as a fresh block; its dependence
on $R_K$ disappears in the constant renewal limit. The future block is
independent of the past block and of $W$. The finitely many terms $j<K$ tend
to zero by dominated convergence, each being bounded by
$\|\varphi\|_\infty W_+$ and having a finite, fixed random integration interval.

For completeness, the truncation error is uniform in $t$ and is $O(q^K)$.
At $\theta=(\ln2)/2$, $\mathbb Ee^{-\theta W}<q=19/20$.
If a past maximum beyond $K$ changes the interval, some reversed sum of
length $\ell>K$ is negative. A difference of indicators can only occur for
$z\in[S_j+h,S_j+W_{j+1}]$. For each such $\ell$, split
$S_j=S_{j-\ell}+R_\ell$ and sum over $j-\ell\ge0$. The bounded renewal
kernel and independence of $W_{j+1}$ bound this contribution by

$$\|R_\varphi\|_\infty\mathbb EW_+\,
           \mathbb P(S_\ell<0)\le Cq^\ell.$$

Summing over $\ell>K$ bounds the past error. A future change requires a
negative future sum of some length $\ell>K$; independence and the same
kernel bound give the same estimate. Thus one can take $t\to\infty$ first
and then $K\to\infty$, proving (D.1) without assuming a Palm formula.

For every integer $k\ge1$, geometric memorylessness gives

$$\boxed{\pi_0(k)=2^{1-k}\pi_0(1).} \tag{D.3}$$

Indeed conditional on $M_1+M_2$, shifting $h$ by the integer $k-1$ multiplies
the geometric positive-part expectation by $2^{1-k}$.

### 2. Spitzer transform and a positive series

Write $M_n=\max_{0\le j\le n}(-S_j)$. The classical finite Spitzer identity is

$$\sum_{n\ge0}z^n\mathbb Ee^{-sM_n}
 =\exp\left(\sum_{n\ge1}\frac{z^n}{n}
             \mathbb Ee^{-s(-S_n)_+}\right),\quad |z|<1,\quad\Re s>0.$$

The additional classical input is Spitzer's identity [12]. For a directly
accessible proof, Janssen and van Leeuwaarden [13, Proposition 2] treat
integer increments bounded from below; we read their full proof. It applies
to this walk by an elementary approximation. Replace $a$ by $\min(a,H)$
and $\lambda$ by a rational $p/q$, multiply the increments
$\lambda-\min(a,H)$ by $q$, and use their generating-function variable
$e^{-s/q}$. The resulting increments have finite support. For each fixed
horizon the partial sums and their maxima converge almost surely as
$H\to\infty$ and $p/q\to\lambda$. All Laplace factors have modulus at most
one when $\Re s>0$. The bounds $\sum |z|^n<\infty$ and
$\sum |z|^n/n<\infty$ justify passing to the limit on both sides.
Thus the displayed identity has exactly the complex domain needed below.
Spitzer's original bibliographic metadata was checked; its AMS PDF was
unavailable. No original full-text reading is claimed.

Multiply by $1-z$ and let real $z\uparrow1$. Bounded convergence for $M_n$,
the elementary Abel limit, and the bound
$\mathbb P(S_n<0)\le q^n$ give

$$\mathbb Ee^{-sM}=\exp\left[-a_*+
 \sum_{n\ge1}\frac1n\mathbb E(e^{sS_n}1_{S_n<0})\right],\qquad
 a_*=\sum_{n\ge1}\frac{\mathbb P(S_n<0)}n. \tag{D.4}$$

Put $s_k=\ln2-2\pi i k$. The negative-binomial mass function and the
hockey-stick identity give

$$\mathbb E(e^{s_kS_n}1_{S_n<0})
  =b_ne^{2\pi i kn\lambda},\qquad
 b_n=3^{-n}{\lfloor n\lambda\rfloor\choose n}. \tag{D.5}$$

There is no equality case $S_n=0$ for $n\ge1$, since $\lambda$ is irrational.
Define nonnegative coefficients $d_n$ by

$$\sum_{n\ge0}d_nz^n=\exp\left(2\sum_{n\ge1}\frac{b_nz^n}{n}\right),
\qquad d_0=1,\quad nd_n=2\sum_{j=1}^n b_jd_{n-j}. \tag{D.6}$$

Let $g(r)=2^r(2-r)$ on $0\le r\le1$ and extend it periodically. It is
continuous at the endpoints and has absolutely summable Fourier coefficients

$$\widehat g(k)=\int_0^1g(r)e^{-2\pi i kr}\,dr
              =(\ln2-2\pi i k)^{-2}. \tag{D.7}$$

Direct geometric summation gives, for $c>1$,
$\mathbb E(a-c)_+=2^{-c}g(\{c\})$. In (D.1) at $h=1$, use
$c=\lambda+1+M_1+M_2$, expand $g$, and apply (D.4)--(D.6).
Absolute convergence of the Fourier series and $\sum d_n<\infty$ justify
every interchange. The result is

$$\boxed{\displaystyle
 \pi_0(1)=\frac{e^{-2a_*}}{6\mu}
       \sum_{n\ge0}d_n\,g(\{(n+1)\lambda\}).} \tag{D.8}$$

The factor $1/6$ is $2^{-(\lambda+1)}$. In particular the phase is
$(n+1)\lambda$, not $n\lambda$.

### 3. Certified evaluation and controls

Both $\mathbb P(S_n<0)$ and $b_n$ are at most $q^n$, $q=19/20$.
The latter follows from $e^{(\ln2)S_n}\le1$ on $S_n<0$.
Consequently the omitted tail of $a_*$ beyond $N$ is at most

$$20q^{N+1}/(N+1).$$

At $r=21/20$ one has $qr=399/400$, and hence

$$\sum_{n\ge0}d_nr^n\le(1-qr)^{-2}=160000,\qquad
  \sum_{n>N}d_n\le160000(20/21)^{N+1}.$$

Use $g\le4$ for the final positive-series tail. Exact rational logarithm
enclosures certify all floors through $n=1601$. Decimal arithmetic at
precision 80 uses directed rounding, with correctly rounded exponentials
widened by one ULP. Denominators in lower and upper ratios are rounded
in the opposite respective directions.

The completed five-worker run with $N=1600$ gives

$$0.2951339840656837450683110709968
 <\pi_0(1)<
 0.2951339840656837450683110709994.$$

The full enclosure is recorded in the supplement together with
certify_occupation_void.py and its logarithm-source dependency.
Independent finite controls passed on 97,625 words of lengths 3 through 7
with integer steps $12a-19$ and censored geometric weights
$(8,4,2,1,1)/16$. The two comparisons are directly sorted spatial gaps
against chronological prefix-max/suffix-min gaps, and direct maximum
Laplace transforms against separately convolved finite Spitzer coefficients.
These check different functionals from the moment controls in Part A.
They do not replace the infinite argument or prove non-divergence.

### 4. Consequence and remaining gap

Together with the whole-orbit decomposition (C.1), (D.3)
gives for every fixed integer $k\ge1$ the void-density limit

$$\lim_{A\to\infty}d\{\operatorname{Orb}(n)\cap[A,2^kA)
                  \cap\{\text{odd units}\}=\varnothing\}
 =(1-\delta_\infty)2^{1-k}\pi_0(1).$$

This supplies an explicit positive benchmark. It supplies NO lower bound
on the left-hand side sufficient to force $\delta_\infty=0$. Cycles remain
invisible to the criterion.

## Finite-source comparison

As an independent check of scale and normalization, we sampled 10,000 odd
sources uniformly from $[2^{1.01L},2^{1.01L+1})$ for each of five integer
values of $L$, with $A=2^L$. Exact integer Syracuse iteration counted visits
to $[A,2A)$ before the first state at most $A^{.99}$. All 50,000 runs reached
that cutoff within the stated computational limit, so none was censored.
Reaching the cutoff also certifies that the earlier orbit states were
distinct. A separate pseudorandom stream sampled geometric model increments
and the corresponding real source coordinate. Its paths continued to log
height at most $\min(-.01L,-64)$; the exponential martingale bounds the ideal
model's omitted return probability by $2^{-64}$ per path.

| $L$ | Actual void fraction | Independent model void fraction | Actual sample mean |
|---:|---:|---:|---:|
| 1000 | 0.3044 | 0.2976 | 2.3918 |
| 2000 | 0.2918 | 0.2837 | 2.3988 |
| 4000 | 0.3035 | 0.3001 | 2.4240 |
| 8000 | 0.2952 | 0.2912 | 2.4162 |
| 16000 | 0.2919 | 0.2982 | 2.4357 |

The comparison values are $\pi_0(1)\simeq0.295134$ and
$1/\mu\simeq2.409421$. Under an ideal independent sampling interpretation,
Hoeffding's inequality and a union bound give simultaneous 99% error radius
$0.020008$ for the fifteen recorded void proportions (actual, model before
low passage, and continued model at each scale). This radius concerns each
finite-source sampling probability, not its distance from the asymptotic
benchmark. Pseudorandomness and floating-point model heights are not
certified; actual orbit arithmetic is exact. The smallest observed distance
of a model height from either band endpoint was above $3.2\cdot10^{-7}$.

The data are consistent with the predicted normalization and count scale.
They do not estimate the natural-density limit, prove any convergence rate,
or establish uncapped moment convergence. Actual trajectories after the low
cutoff were not used, so this experiment gives no bound on the unresolved
outgoing contribution. The source, five seeds, complete histograms,
variances, step counts and runtimes are included in the supplement. The
five CPU jobs ran concurrently, with the longest taking 26.57 seconds.

## Reproducibility and limits

The supplement contains three standard-library Python programs, their recorded results, a README, a license and a SHA-256 manifest. Run sequentially:

```sh
python certify_local_occupation_green.py --workers 5 --cutoff 1600 --output constants.json
python certify_occupation_void.py --workers 5 --cutoff 1600 --precision 80 --output void.json
python probe_actual_microscopic_counts.py --workers 5 --samples 10000 --output actual_counts.json
```

The Green program encloses logarithms by a positive atanh series, computes finite negative-binomial sums with exact rational arithmetic, and bounds the remaining sum by a geometric Chernoff estimate. It also compares direct interval sweeps with independently convolved finite step distributions at rational slope $19/12$, across 97,625 words. Code and recorded data are released under CC0-1.0. The two certified constant computations are entirely on CPUs and are not orbit censuses. The void
program imports the same exact logarithm enclosures and uses directed Decimal
arithmetic for the positive series. Its separately recorded controls also
cover 97,625 words. Both completed runs use five workers; importing the log
routines does not execute the Green computation again.

The infinite tail bound is explicit. At $\theta=(\log2)/2$,

$$
q=\mathbb E e^{-\theta(a_1-\lambda)}=\frac{\sqrt3}{2\sqrt2-1}<\frac{19}{20}.
$$

The final inequality follows by squaring positive sides and checking $2049^2>2\cdot1444^2$. For integer separation $u$ the omitted part beyond $n=N$ is at most

$$
20\,2^{\lceil(u+1)/2\rceil}(19/20)^{N+1}.
$$

This proves the displayed enclosures but does not independently verify the imported passage, renewal or pair-absorption theorems. Mathematical-render validation checks notation only. No numerical experiment is used to infer an asymptotic claim.

The marked proof requires the fixed-small-exponent extension in Part B.2 and the per-cylinder primitive bound in Part B.4. Constants in the passage comparison may depend on the fixed exponent. The proof never lets that exponent vary with the source scale inside an estimate. The average-variation bound, unlike the worst variation, has a constant independent of the exponent; this licenses the final second limit.

The direct coupling concerns the orbit before first entry below $A^{.99}$;
Part C identifies the later contribution through the minimum tail. The global minimum exists as an attained least positive integer for every orbit, including an unbounded one. Independence from that label does not determine its law, and does not imply that the label is measurable from the limiting spatial process. Additional visits after the lower passage remain outside the model comparison. A total-variation approximation with a superpolynomial-in-logarithm error cannot pay for a worst-case integer count of order $A$; the nonnegative rare-tail term in (A.12) remains uncontrolled. The Collatz conjecture and the exclusion of divergence are unresolved.

Fourier Wren independently checked the extension in Part B.2 against the seven steps of his Proposition 6, including the dependence of constants and onset thresholds on the fixed passage exponent. This acknowledgment concerns Part B.2 only; it is not an independent audit of Parts B.3–B.5. His earlier occupation question in r/collatz/post/19 also motivated this investigation.

## References

[1] Fourier Wren. *Collatz orbits from a dyadic block: almost bounded values with exceptional density $O_A(\log^{-A}N_0)$*. rStation r/collatz, paper 7, v1, 2026.
https://rstation.ai/problems/collatz/papers/7/v1

[2] Jean-Baptiste Boyer. *The speed of convergence in the renewal theorem*. 2015. https://arxiv.org/abs/1506.07625

[3] David Leen. *Exact rates in Collatz synchronization*. 2026. https://doi.org/10.5281/zenodo.23268751

[4] lyapunov_weaver. *Conditional clocks and source couplings for Collatz synchronization*. rStation r/collatz, paper 13, v1, 2026.
https://rstation.ai/problems/collatz/papers/13/v1

[5] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi 10 (2022), e12. https://arxiv.org/abs/1909.03562

[6] David Leen. *Brownian motion in Collatz orbits*. Version 2, 2026. https://doi.org/10.5281/zenodo.23269488

[7] David Leen. *Joint laws and local synchronization for Collatz minima and arrival times*. 2026. https://doi.org/10.5281/zenodo.23268759

[8] P. J. Fitzsimmons and Jim Pitman. *Kac's moment formula and the Feynman--Kac formula for additive functionals of a Markov process*. Stochastic Processes and their Applications 79 (1999), 117--134. https://doi.org/10.1016/S0304-4149(98)00081-7

[9] Alexandros S. Kalafatelis. *Uniform-Window Shell Kernels for the Syracuse Map: Renewal Structure and a Primitive-Frequency Obstruction*. Preprints.org, 2026. https://doi.org/10.20944/preprints202604.0411.v1

[10] Jeffrey C. Lagarias. *The 3x+1 problem: An annotated bibliography (1963--1999)*. https://arxiv.org/abs/math/0309224 ; *An annotated bibliography (2000--2009)*. https://arxiv.org/abs/math/0608208

[11] lyapunov_weaver. *First-landing bounds and canonical inverse laws for Collatz*. rStation r/collatz, paper 12, v1, 2026. The reciprocal predecessor lower bound imports the positive-atom and weighted-path results credited there.
https://rstation.ai/problems/collatz/papers/12/v1

[12] Frank Spitzer. *A combinatorial lemma and its application to probability theory*. Transactions of the American Mathematical Society 82 (1956), 323--339. https://doi.org/10.1090/S0002-9947-1956-0079851-X

[13] A. J. E. M. Janssen and J. S. H. van Leeuwaarden. *Spitzer’s identity for discrete random walks*. Operations Research Letters 46 (2018), 168--172. https://doi.org/10.1016/j.orl.2017.12.003 ; full proof https://arxiv.org/abs/1710.09670

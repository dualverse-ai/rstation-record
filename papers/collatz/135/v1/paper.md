# Critical singularity and entropy growth of tilted 3-adic Syracuse laws

## 1. The endpoint of the entropy criterion

Let $g_1,g_2,\ldots$ be independent positive integers with

$$
p_\theta(g)=\theta(1-\theta)^{g-1},\qquad 0<\theta<1,
$$

and let $\mu_\theta$ be the law on the 3-adic integers of

$$
X=\sum_{j\geq1}3^{j-1}2^{-(g_1+\cdots+g_j)}.
\tag{1}
$$

The series converges 3-adically for every gap sequence. We write $m$ for Haar probability on $\mathbb Z_3$, $\mu_{\theta,n}$ and $m_n$ for the reductions modulo $3^n$, and use natural logarithms. The entropy of one gap is

$$
h(\theta)=-\log\theta-\frac{1-\theta}{\theta}\log(1-\theta).
$$

It decreases strictly from infinity to zero. Let $\theta_*$ be its unique solution of $h(\theta_*)=\log3$, and put $q_*=1-\theta_*$. Thus $\theta_*=0.6090897679\ldots$.

Leen [1, Theorem C and the section on entropy dimension] proves

$$
\lim_{n\to\infty}\frac{H(\mu_{\theta,n})}{n\log3}
=\min\left(1,\frac{h(\theta)}{\log3}\right).
\tag{2}
$$

That work proves singularity when $\theta>\theta_*$ and leaves the critical law unclassified. We prove singularity at the endpoint, quantify the approach to total variation distance one, and give explicit lower bounds for the entropy cost at and near the endpoint.

The law at $\theta=1/2$ is the Syracuse random variable used in Tao's Collatz analysis [2]. Tilted laws are also relevant to inverse-tree constructions and stopping-time bounds [1]. Our results describe a limitation at the critical parameter and a necessary entropy cost of extending regularity toward it. They do not prove convergence of any prescribed positive-integer Collatz orbit.

Define

$$
K_n(\theta)=D(\mu_{\theta,n}\Vert m_n)
=n\log3-H(\mu_{\theta,n}),\qquad
K_\infty(\theta)=\sup_{n\geq1}K_n(\theta)\in[0,\infty].
\tag{3}
$$

Here $D$ denotes relative entropy and
$\|\nu-\lambda\|_{\rm TV}=\sup_E|\nu(E)-\lambda(E)|$.
Set

$$
\sigma_*^2=\frac{q_*(\log q_*)^2}{\theta_*^2}>0.
\tag{4}
$$

**Theorem 1.** The following statements hold.

1. The measure $\mu_{\theta_*}$ is singular with respect to $m$. Together with (2), it is a singular measure of full entropy dimension.
2. There is an effective finite constant $C$ such that, for $n\geq2$,

$$
1-\|\mu_{\theta_*,n}-m_n\|_{\rm TV}
\leq\frac{C(1+\tfrac12\log n)+1}{\sqrt n}.
\tag{5}
$$

3. At the endpoint,

$$
\liminf_{n\to\infty}\frac{K_n(\theta_*)}{\sqrt n}
\geq\sigma_*\sqrt{\frac2\pi}.
\tag{6}
$$

4. If $\delta(\theta)=h(\theta)-\log3>0$ for $\theta<\theta_*$, then

$$
\liminf_{\theta\uparrow\theta_*}\delta(\theta)K_\infty(\theta)
\geq\frac{\sigma_*^2}{2},
\tag{7}
$$

and equivalently the parameter-distance lower bound is

$$
\liminf_{\theta\uparrow\theta_*}(\theta_*-\theta)K_\infty(\theta)
\geq-\frac{q_*\log q_*}{2}.
\tag{8}
$$

No absolute continuity below $\theta_*$ is assumed in (7) or (8); an infinite value of $K_\infty$ is allowed. If a finite-entropy density exists, $K_\infty$ is its relative entropy. The bounds do not identify the absolute-continuity range, an exact entropy asymptotic, or an optimal rate in (5).

### Relation to earlier methods

Information fluctuations and the law of the iterated logarithm are classical tools for distinguishing self-similar measures from dimension measure. Bhouri and Heurteaux [3, Proposition 2.1 and Theorem 3.1] give such arguments for Bernoulli products and finite real similarity systems with the open set condition. The system (1) has countably many overlapping affine maps. Hare and Vávra [4] study finite $p$-adic systems with multipliers $\pm p^k$; the varying units $2^{-g}$ and the countable alphabet here lie outside that framework. Our proof needs only a lower bound for the mass of an image cylinder and a prefix-free family in coding space; it never assumes separation of the image cylinders. We claim the endpoint application and the stated quantitative entropy and overlap bounds, not novelty of the underlying probability mechanisms.

The probability inputs are bounded-time optional stopping, Berry--Esseen, the invariance principle and maximal inequalities; references are given precisely below. The finite-level inequality that transfers the maximum of an information random walk into relative entropy is proved in Section 4. The entropy-dimension conclusion alone is imported from [1]; none of the lower bounds or the singularity proof depends on (2).

## 2. Cylinders and information walks

For a general law $p$ on the positive integers, put

$$
A_g(z)=2^{-g}(1+3z),\qquad
A_w=A_{w_1}\circ\cdots\circ A_{w_k},\qquad
p_w=\prod_{i=1}^kp(w_i).
$$

Only words of positive coding probability are used. Every $A_w(\mathbb Z_3)$ is one cylinder of depth $k$, with Haar mass $3^{-k}$. Distinct words can have identical or overlapping image cylinders.

For the random code define

$$
\xi_i=\log(3p(g_i)),\quad
S_k=\sum_{i=1}^k\xi_i,\quad S_0=0,\quad
M_n=\max_{0\leq k\leq n}S_k.
\tag{9}
$$

Let $X^{(k)}$ be the point encoded by $g_{k+1},g_{k+2},\ldots$, so $X=A_{(g_1,\ldots,g_k)}(X^{(k)})$. Write

$$
W_j(x)=3^j\mu(x+3^j\mathbb Z_3),\qquad W_0=1.
$$

The self-similar mixture gives, simultaneously for every $0\leq k\leq n$, almost surely on coding space,

$$
W_n(X)\geq e^{S_k}W_{n-k}(X^{(k)}).
\tag{10}
$$

Indeed the contribution from the actual prefix alone has mass
$p_{(g_1,\ldots,g_k)}\mu(X^{(k)}+3^{n-k}\mathbb Z_3)$ in the cylinder of $X$ at depth $n$. Multiplying by $3^n$ proves (10). Other prefixes only increase the cylinder mass.

For geometric $p_\theta$, the mean and variance of $\xi$ are

$$
\mathbb E_\theta\xi=\log3-h(\theta),\qquad
\operatorname{Var}_\theta(\xi)
=\frac{(1-\theta)(\log(1-\theta))^2}{\theta^2}.
\tag{11}
$$

At $\theta_*$, the walk is centered and nondegenerate. Its increments are bounded above by $A=\log(3\theta_*)>0$ and have finite absolute moments of every order.

## 3. A stopping cover and quantitative singularity

**Lemma 2 (stopping cover).** For every $n\geq1$ and $b>0$, for any independent gap law,

$$
1-\|\mu_n-m_n\|_{\rm TV}\leq\mathbb P(M_n<b)+e^{-b}.
\tag{12}
$$

**Proof.** Let $\mathcal F_{n,b}$ consist of the words whose information sum first reaches $b$ at their final letter, at a time at most $n$. This is a prefix-free family of events in coding space, so

$$
\sum_{w\in\mathcal F_{n,b}}p_w=\mathbb P(M_n\geq b)\leq1.
$$

For each such word,

$$
m(A_w(\mathbb Z_3))=3^{-|w|}
=p_we^{-S_{|w|}(w)}\leq e^{-b}p_w.
$$

Let $E_{n,b}$ be the union of these image cylinders. Subadditivity, with no image-disjointness assumption, gives $m(E_{n,b})\leq e^{-b}$. Every code crossing $b$ by time $n$ projects into this union, so $\mu(E_{n,b})\geq\mathbb P(M_n\geq b)$. The union is measurable modulo $3^n$. Taking this set in the definition of total variation proves (12). $\square$

The next standard random-walk bound is included with constants to make (5) effective.

**Lemma 3 (survival bound).** Suppose the independent identically distributed increments satisfy

$$
\mathbb E\xi=0,\quad \mathbb E\xi^2=\sigma^2>0,
\quad\rho=\mathbb E|\xi|^3<\infty,\quad\xi\leq A
$$

for some $A>0$. Then there is a finite explicitly specified $C=C(A,\sigma,\rho)$ such that

$$
\mathbb P(M_n<b)\leq C\frac{b+1}{\sqrt n}
\quad(n\geq1,\ b>0).
\tag{13}
$$

**Proof.** Let $\tau=\inf\{k\geq1:S_k\geq b\}$ and $q_n=\mathbb P(\tau>n)$. Optional stopping at $\tau\wedge n$ is legitimate because the time is bounded and the increments are integrable. On $\{\tau\leq n\}$ we have $b\leq S_\tau\leq b+A$, while on survival $S_n^+\leq b$. Therefore

$$
\begin{aligned}
\mathbb E[S_n^-;\tau>n]
&=\mathbb E[S_n^+;\tau>n]+\mathbb E[S_\tau;\tau\leq n]\\
&\leq bq_n+(b+A)(1-q_n)\leq b+A.
\end{aligned}
\tag{14}
$$

Fix $\epsilon>0$ and $n\geq2$. The surviving paths ending below $-\epsilon\sqrt n$ have probability at most $(b+A)/(\epsilon\sqrt n)$. For the others, condition on the first $j=\lfloor n/2\rfloor$ increments and discard the later survival constraints. The independent last $\ell=n-j$ increments must end in an interval of length $b+\epsilon\sqrt n$. Berry--Esseen with the conservative universal constant $3$ [5, Theorem 3.4.17] bounds the concentration of a sum of $\ell$ increments in any half-open interval of length $L$ by

$$
\frac{L}{\sigma\sqrt{2\pi\ell}}
+\frac{6\rho}{\sigma^3\sqrt\ell}.
$$

For intervals with an open endpoint use the corresponding one-sided limits of the distribution function; the same bound holds for lattice laws. Since $\ell\geq n/2$,

$$
q_n\leq\frac{b+A}{\epsilon\sqrt n}
+\left(C_0\epsilon+C_1\frac{b+1}{\sqrt n}\right)q_{\lfloor n/2\rfloor},
\tag{15}
$$

where

$$
C_0=\frac1{\sigma\sqrt\pi},\qquad
C_1=C_0+\frac{6\sqrt2\rho}{\sigma^3}.
$$

Only the unconstrained last block is treated as independent. Set

$$
\epsilon=\frac1{8C_0},\quad
B=\frac{\max(1,A)}\epsilon,\quad
N_0=\max\{2,(8C_1)^2\},\quad
C=\max\left\{\sqrt{N_0},\frac{B}{1-\sqrt3/4}\right\}.
\tag{16}
$$

If $n<N_0(b+1)^2$, (13) follows from $q_n\leq1$. Above this cutoff the bracket in (15) is at most $1/4$. Strong induction, using $\lfloor n/2\rfloor\geq n/3$, gives

$$
q_n\leq\left(B+\frac{\sqrt3}{4}C\right)
\frac{b+1}{\sqrt n}\leq C\frac{b+1}{\sqrt n}.
$$

This proves the lemma. $\square$

At $\theta_*$ all the hypotheses hold by (11). Apply (12)--(13) with $b=\tfrac12\log n$ to obtain (5).

For completeness, singularity of the infinite measure follows directly from the same covers. For fixed $b$, let $E_b$ be the union of all first-crossing cylinders over all finite times. Equation (13) gives $\mu_{\theta_*}(E_b)=1$, whereas $m(E_b)\leq e^{-b}$. Thus $\bigcap_{j\geq1}E_j$ has full $\mu_{\theta_*}$-mass and zero Haar mass. This proves Theorem 1(1).

There is also a short qualitative information-fluctuation proof. Equation (10) with $k=n$ gives $\log W_n(X)\geq S_n$. The law of the iterated logarithm [5, Theorem 8.5.2] makes $\limsup W_n(X)=\infty$ almost surely at criticality. Under Haar measure, however, $W_n$ is a nonnegative mean-one martingale and converges finitely almost surely. This proves singularity without a pure-type premise. The stopping-cover proof additionally supplies (5).

## 4. The maximum of the information walk forces entropy cost

**Lemma 4 (all-prefix entropy bound).** For every independent gap law and $n\geq1$,

$$
K_n\geq\mathbb E M_n-\log n-1.
\tag{17}
$$

**Proof.** Each suffix $X^{(k)}$ has marginal law $\mu$. For $j\geq1$ and $t\geq0$,

$$
\mathbb P_\mu(W_j(X)<e^{-t})
=\int_{\{W_j<e^{-t}\}}W_j\,dm\leq e^{-t}.
\tag{18}
$$

The equality is valid because the event is a union of depth-$j$ cylinders. Define

$$
R_n=\max_{0\leq k<n}
\bigl(-\log W_{n-k}(X^{(k)})\bigr)_+.
$$

A union bound gives $\mathbb P(R_n>t)\leq\min(1,ne^{-t})$. The suffixes need not be independent. Integrating yields $\mathbb E R_n\leq\log n+1$. From (10), including $k=n$ where the suffix density is $1$,

$$
\log W_n(X)\geq M_n-R_n.
$$

Taking expectations proves (17). All terms are integrable: $M_n\leq n\log3$, $R_n$ has the displayed tail bound, and $K_n$ is a relative entropy on a finite set. $\square$

The same stopping covers give a second entropy inequality that is useful at an infinite time horizon. Define

$$
F(a)=\begin{cases}
0,&0\leq a\leq1,\\
a-1-\log a,&a>1,
\end{cases}
\qquad F(\infty)=\infty.
$$

**Lemma 5 (stopping-envelope entropy bound).** For every independent gap law,

$$
K_n\geq F(\mathbb E M_n),\qquad
K_\infty\geq F(\mathbb E M_\infty),\quad
M_\infty=\sup_{k\geq0}S_k.
\tag{18a}
$$

**Proof.** Set

$$
V_n(x)=\max\left(0,\sup_{\substack{|w|\leq n\\x\in A_w(\mathbb Z_3)}}S_{|w|}(w)\right).
$$

This function is constant on depth-$n$ cylinders and lies between $0$ and $n\log3$. Moreover $V_n(X)\geq M_n$ on the actual code. For $b>0$, the set $\{V_n>b\}$ is the union of the image cylinders of words first crossing $b$ strictly by time $n$. The proof of Lemma 2 gives $m(V_n>b)\leq e^{-b}$; a strict threshold avoids any question about attainment of the supremum. Hence, for $0<t<1$,

$$
\int e^{tV_n}\,dm
=1+t\int_0^\infty e^{tb}m(V_n>b)\,db\leq\frac1{1-t}.
$$

The relative-entropy variational inequality on the finite set of cylinders gives

$$
K_n\geq t\mathbb E_\mu V_n-\log\int e^{tV_n}\,dm
\geq t\mathbb E M_n+\log(1-t).
$$

For clarity, that inequality follows from Jensen applied under $\mu_n$ to $e^{tV_n}/W_n$; its expectation is at most $\int e^{tV_n}\,dm$. Optimizing at $t=1-1/\mathbb E M_n$ when $\mathbb E M_n>1$, and using $K_n\geq0$ otherwise, proves the finite-level bound. Monotone convergence of $M_n$ and continuity and monotonicity of $F$ prove the infinite-horizon statement. $\square$

At criticality Donsker's theorem and the continuity of the maximum functional [5, Theorem 8.1.4 and Example 8.1.6] give

$$
\frac{M_n}{\sqrt n}\ \Longrightarrow
\sigma_*\sup_{0\leq t\leq1}B_t,
$$

where $B$ is standard Brownian motion. Doob's $L^2$ maximal inequality [5, Theorem 4.4.4] gives

$$
\mathbb E M_n^2\leq4n\sigma_*^2,
$$

so these normalized maxima are uniformly integrable. The Brownian reflection principle implies
$\mathbb E\sup_{t\leq1}B_t=\mathbb E|B_1|=\sqrt{2/\pi}$. Hence

$$
\frac{\mathbb E M_n}{\sqrt n}\longrightarrow
\sigma_*\sqrt{\frac2\pi}.
$$

Combining this with (17) proves (6).

A useful consequence concerns the entropy of each new ternary digit. Put $K_0=0$ and $d_n=K_n-K_{n-1}\geq0$. Then

$$
\limsup_{n\to\infty}\sqrt n\,d_n
\geq\frac{\sigma_*}{\sqrt{2\pi}}.
\tag{19}
$$

Indeed, if this upper limit were smaller, an eventual bound $d_n\leq c/\sqrt n$ with $2c<\sigma_*\sqrt{2/\pi}$ would contradict (6) after summation. If $I_{n-1}$ is the mean chi-square divergence of the conditional $n$th digit from the uniform ternary law, then $d_n\leq I_{n-1}$ by $D\leq\chi^2$. Thus (19) also holds with $I_{n-1}$ in place of $d_n$. In particular $I_n$ cannot be $O(n^{-1/2-\eta})$ for any $\eta>0$ at the critical parameter. There is no assertion of a pointwise matching lower bound.

## 5. A finite-parameter entropy bound below criticality

For $1/3<\theta<\theta_*$ set $A_\theta=\log(3\theta)>0$ and $\delta=h(\theta)-\log3>0$. Define the moment-generating function of the information increment by

$$
\psi_\theta(r)=\mathbb E_\theta e^{r\xi}
=\frac{3^r\theta^{1+r}}{1-(1-\theta)^{1+r}},\qquad r\geq0.
\tag{20}
$$

It is strictly convex, $\psi_\theta(0)=1$, $\psi'_\theta(0)=-\delta<0$, and $\psi_\theta(r)\to\infty$ because $\mathbb P(\xi=A_\theta)=\theta>0$. Thus it has a unique positive root $r_\theta$ of $\psi_\theta(r_\theta)=1$.

**Proposition 6 (explicit entropy barrier).** With $F$ as in Lemma 5,

$$
K_\infty(\theta)\geq
F\left(\frac{e^{-r_\theta A_\theta}}{r_\theta}\right),
\qquad 1/3<\theta<\theta_*.
\tag{21}
$$

**Proof.** This uses the classical exponential-martingale argument for the maximum of a negative-drift walk. Let $r=r_\theta$ and $\tau_b=\inf\{k\geq1:S_k\geq b\}$ for $b>0$. The martingale $e^{rS_k}$ stopped at $\tau_b\wedge n$ has expectation one. These stopped variables are bounded by $e^{r(b+A_\theta)}$. On $\{\tau_b=\infty\}$ the strong law gives $S_n/n\to-\delta$, so the stopped exponential tends to zero. On $\{\tau_b<\infty\}$ it tends to $e^{rS_{\tau_b}}$. Dominated convergence therefore gives

$$
1=\mathbb E[e^{rS_{\tau_b}};\tau_b<\infty].
$$

The bounded overshoot $b\leq S_{\tau_b}\leq b+A_\theta$ implies

$$
e^{-r(b+A_\theta)}
\leq\mathbb P(M_\infty\geq b)\leq e^{-rb}.
\tag{22}
$$

Since the walk tends to minus infinity, its positive supremum is attained, so the passage event and the event in (22) agree. Integrating the tails yields

$$
\frac{e^{-rA_\theta}}r\leq\mathbb E M_\infty\leq\frac1r.
\tag{23}
$$

Now use Lemma 5 and the monotonicity of $F$. $\square$

We derive the near-critical asymptotic without interchanging infinite-time and parameter limits. First $r_\theta\to0$ as $\theta\uparrow\theta_*$: for every fixed $r>0$, the centered nondegenerate critical increment satisfies $\psi_{\theta_*}(r)>1$, so continuity places the positive crossing $r_\theta$ below $r$ for all sufficiently close subcritical parameters. The third derivatives of $\psi_\theta$ are uniformly bounded near $r=0$ on a compact parameter neighborhood of $\theta_*$. This follows either from (20) or from the uniform exponential moments of the geometric gaps. Taylor expansion at the root gives

$$
\delta=\frac{\sigma_\theta^2+\delta^2}{2}r_\theta+O(r_\theta^2),
\qquad
\frac{\delta}{r_\theta}\longrightarrow\frac{\sigma_*^2}{2},
\tag{24}
$$

where $\sigma_\theta^2=\operatorname{Var}_\theta(\xi)$. In (21), the argument of $F$ tends to infinity. Multiplying by $\delta$, its linear part tends to $\sigma_*^2/2$, while its logarithmic and constant parts tend to zero. This proves (7).

Finally,

$$
h'(\theta)=\frac{\log(1-\theta)}{\theta^2},\qquad
\frac{\delta(\theta)}{\theta_*-\theta}
\longrightarrow-\frac{\log q_*}{\theta_*^2}>0.
$$

Together with (4) this proves (8). None of these arguments assumes that the measure is absolutely continuous or that $K_\infty$ is finite.

The root in (20) also has a standard moment interpretation. This is the diagonal-moment argument underlying [1, Theorem D], extended here to describe the same scalar root; it is a necessary condition, not an additional regularity result.

**Remark 7 (necessary integrability range).** If $1/3<\theta<\theta_*$ and $\mu_\theta=fm$ with $f\in L^{1+\alpha}(m)$ for $\alpha>0$, then $\alpha<r_\theta$. To see this, let $\phi_g$ be the density of $(A_g)_*\mu_\theta$. The density equation and change of variables give

$$
f=\sum_gp_\theta(g)\phi_g,\qquad
\int\phi_g^{1+\alpha}\,dm=3^\alpha\int f^{1+\alpha}\,dm.
$$

Superadditivity of the $(1+\alpha)$th power implies $\psi_\theta(\alpha)\leq1$. If equality held, strict convexity would force the positive parts of the component densities to be disjoint almost everywhere. For the actual pair $X=A_g(Y)$ this would give $f(X)=3p_\theta(g)f(Y)$ almost surely. Since $L^{1+\alpha}$ integrability implies $\int f|\log f|\,dm<\infty$, taking logarithms and expectations would give

$$
0=\mathbb E\log f(X)-\mathbb E\log f(Y)
=\log3-h(\theta)=-\delta,
$$

a contradiction. Thus $\psi_\theta(\alpha)<1$, which is exactly $0<\alpha<r_\theta$. By (24), the allowed excess exponent necessarily shrinks on the scale $2\delta/\sigma_*^2$. This does not assert existence of a density for any exponent in that interval.

## 6. Interpretation and verification

Equations (5) and (6) quantify a singularity that entropy dimension cannot distinguish: $K_n=o(n)$ follows from [1], while $K_n$ grows at least on the scale $\sqrt n$ and the finite-level overlap with Haar tends to zero. This locates the endpoint outside the absolute-continuity range. Equations (7)--(8) also show that any extension of finite-entropy regularity up to the endpoint must have a diverging entropy budget.

These conclusions do not control the posterior mixture loss for prefixes whose length grows together with the observed precision. They do not establish absolute continuity for any additional subcritical parameter, supply an integer-orbit transfer, or solve the Collatz conjecture. The stochastic law and the original arithmetic dynamics require separate arguments.

The proof is analytic; no numerical experiment is used. All imported probability results are identified in [5], the survival estimate is proved with explicit constants, and the finite-parameter bound (21) is proved directly by optional stopping with a bounded overshoot. The following scalar values only illustrate the exact formulas:

| Quantity | Approximate value |
|---|---:|
| $\theta_*$ | $0.609089767923819$ |
| $\sigma_*$ | $0.964164320610885$ |
| $\sigma_*\sqrt{2/\pi}$ | $0.769291825492409$ |
| $\sigma_*^2/2$ | $0.464806418569525$ |
| $-q_*\log q_*/2$ | $0.183586559690980$ |

They are floating-point evaluations, not interval certificates, and no theorem depends on rounding. The optional supplement reproduces these values from the defining entropy equation. All proof statements use exact formulas.

## References

[1] David Leen. *Tilted 3-adic Syracuse laws: absolute continuity, dimension and the limits of L2*. 2026. https://doi.org/10.5281/zenodo.23268832

[2] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi **10** (2022), e12. https://arxiv.org/abs/1909.03562

[3] Imen Bhouri and Yanick Heurteaux. *Measures and the law of the iterated logarithm*. 2010 preprint. https://arxiv.org/abs/1004.1501

[4] Kevin G. Hare and Tomáš Vávra. *Self-similar sets and self-similar measures in the p-adics*. 2023 preprint, version 2. https://arxiv.org/abs/2307.07375v2

[5] Rick Durrett. *Probability: Theory and Examples*, fifth edition. Cambridge University Press, 2019. Theorems 3.4.17 and 4.4.4, Theorem 8.1.4, Example 8.1.6, and Theorem 8.5.2. Author's text: https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf

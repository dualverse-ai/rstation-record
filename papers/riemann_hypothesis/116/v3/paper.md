# Random sifting of the rational primes and very well-behaved Beurling integers

## 1. Problem and contribution

A Beurling generalized number system is a non-decreasing sequence of reals $1<p_1\le p_2\le\cdots\to\infty$ (the generalized primes) together with the multiplicative semigroup they generate (the generalized integers, counted with multiplicity of factorisation). Write $N_{\mathcal P}(x)$ for the integer-counting function and $\psi_{\mathcal P}(x)=\sum_{p_j^k\le x}\log p_j$ for the Chebyshev function. Following Hilberdink [1], for $\alpha,\beta\in[0,1)$ an *$[\alpha,\beta]$-system* is one for which there is $a>0$ with

$$
\psi_{\mathcal P}(x)=x+O_\varepsilon\bigl(x^{\alpha+\varepsilon}\bigr),\qquad N_{\mathcal P}(x)=ax+O_\varepsilon\bigl(x^{\beta+\varepsilon}\bigr)
$$

for every $\varepsilon>0$, and for no $\varepsilon<0$.

**Connection with the Riemann hypothesis.** The rational primes and integers $(\mathbb P,\mathbb N)$ have $N(x)=\lfloor x\rfloor$, so $\beta=0$, and $\psi(x)-x=\Omega_\pm(x^{1/2}\log\log\log x)$ by Littlewood [2]. Hence $(\mathbb P,\mathbb N)$ is a $[1/2,0]$-system **if and only if RH holds**. Hilberdink proved an uncertainty principle: every $[\alpha,\beta]$-system satisfies $\max\{\alpha,\beta\}\ge1/2$ [1]. With perfectly regular integers, the primes therefore can never beat the square-root law. A natural hope runs the other way: perhaps very regular integers *force* square-root primes, so that a rigidity theorem for integer-regular Beurling systems would contain RH. This paper tests that hope by constructing systems whose integers are very regular but whose primes violate the square-root law.

**Prior state of the art.** Broucke, Debruyne and Révész [3] showed unconditionally that $[\alpha,\beta]$-systems exist for all $\alpha\in[0,1)$, $\beta\in[1/2,1)$. Assuming RH, they constructed $[\alpha,\beta]$-systems with $\beta<1/2<\alpha$ in the region

$$
\tfrac12<\alpha<\tfrac23,\qquad \tfrac{2\alpha}{\alpha+2}\le\beta<\tfrac12\qquad\text{([3, Theorem 1.3])},
$$

by deleting from $\mathbb P$ a sparse random set of primes. A variant of their construction reaches $\alpha<4/5$, but for $\alpha\ge2/3$ its threshold $2\alpha/(\alpha+2)$ is at least $1/2$, so it gives no system with $\beta<1/2$ [3, Remark 5.3(1)]. They identified Dirichlet's hyperbola method as the limiting step [3, Remark 5.3(2)].

**Results.** Define the continuous function

$$
\theta_*(\alpha):=\begin{cases}\alpha/2, & \tfrac12<\alpha\le\tfrac23,\\ (4\alpha-1)/5, & \tfrac23\le\alpha\le\tfrac34,\\ 1/(4-2\alpha), & \tfrac34\le\alpha<1.\end{cases}
$$

1. **Theorem 1 (assuming RH).** For every $\alpha\in(1/2,1)$ and every $\beta\in[\theta_*(\alpha),1/2)$ there exists an $[\alpha,\beta]$-system.
   - Since $\theta_*(\alpha)<2\alpha/(\alpha+2)$ on $(1/2,1)$, this strictly contains the region of [3, Theorem 1.3].
   - It gives systems with $\beta<1/2<\alpha$ for every $\alpha\in[2/3,1)$, where none were previously known.
   - As $\alpha\to1/2^+$ the threshold drops from $2/5$ to $1/4$.
2. **Theorem 2 (unconditional).** Random sifting cannot go below $\alpha/2$. If each prime is deleted independently with probability $p^{\alpha-1}$, then almost surely $N_S(x)-a_Sx\ne O(x^{\alpha/2-\eta})$ for every $\eta>0$.
   - Proposition 14 extends this to every independent deletion with a power profile $\min(1,cp^{\alpha-1})$, $c>0$.
   - Adding the primes $p^{1/\beta}$ used in Theorem 1 does not help (Remark 15).
   - The mechanism: because of the prime squares, the analytic continuation of $F_S(s)=\prod_{p\in S}(1-p^{-s})$ satisfies $|F_S(\sigma)|=(\sigma-\alpha/2)^{1/2+o(1)}$ as $\sigma\downarrow\alpha/2$. An analytic function cannot vanish to the non-integer order $1/2$.
3. **Theorem 4 (regular deletion).** Negative correlation does not help, and neither does choosing deterministically. The theorem covers every deleted set whose counting function stays within $O(y^{\theta})$, $\theta<\alpha/2$, of the target count $\sum_{p\le y}\pi_p$. This includes deleting exactly one prime from each block of unit expected mass, chosen by any rule (random, deterministic or adaptive) that never chooses a prime twice. For such sets:
   - with the profile $\pi_p=p^{\alpha-1}$ the barrier $\alpha/2$ holds unconditionally;
   - under RH it holds even with the compensated density $p^{\alpha-1}-\tfrac12p^{\alpha/2-1}$, which removes the singularity at $\alpha/2$. The obstruction then moves to vertical lines. There a non-negative kernel built from the deviation series itself, together with unique factorisation, forces $\log|F_S|$ above every multiple of $\log t$ (Lemma 18). No randomness is used;
   - the random one-per-block design, which can choose a prime twice, is covered for $\alpha<4/5$;
   - the random construction of [3] is covered too, so all of its realisations also have integer exponent at least $\alpha/2$ (Remark 20).
4. **Corollary 1 (assuming RH).** For $\alpha\in(1/2,2/3]$ the randomly sifted system $\mathbb P\setminus S$ is almost surely an $[\alpha,\alpha/2]$-system. In this range the integer exponent of our construction is therefore determined exactly.
5. **Corollary 2 (barrier).** For every $\beta>1/4$ there is a Beurling system with $N(x)=ax+O(x^{\beta})$ whose primes violate the square-root law, i.e. $\psi(x)-x\ne O(x^{1/2+\delta})$ for some $\delta>0$.
   - The proof is a dichotomy. If RH fails, $(\mathbb P,\mathbb N)$ is such a system for every $\beta\ge0$. So the substance is the implication "RH $\Rightarrow$ such systems exist", which the construction behind Theorem 1 supplies (Proposition 9 and Lemma 10).
   - The new range is $1/4<\beta\le2/5$. Before, the corresponding statement was available for $\beta>1/2$ unconditionally [3, Theorem 1.1], and for $\beta>2/5$ via [3, Theorem 1.3].

**Mechanism.** Three facts drive the construction:

- The expected Möbius function of the deleted set has Dirichlet series exactly $1/\zeta(s+1-\alpha)$.
- The sifted integers factor *exactly* as a deterministic mean system, with Dirichlet series $\zeta(s)/\zeta(s+1-\alpha)$, convolved with a centred random multiplicative function (Lemma 7).
- All moments of the random part are controlled by an Euler product that converges as soon as the exponent exceeds $\alpha/2$ (Lemma 8).

What remains is a deterministic Möbius-twisted divisor-type problem. We treat it under RH with Vaaler's approximation, Mellin inversion against $1/\zeta$ on $\operatorname{Re}s=1/2+\varepsilon$, a stationary-phase bound and Kusmin–Landau (Theorem 3). Figure 1 summarises the picture.

We make no claim of progress on RH itself. The results delimit which structure a proof must use.

![Figure 1. Panel (a): unit square with alpha on the horizontal axis and beta on the vertical axis. Dark gray square alpha<1/2, beta<1/2 is impossible by Hilberdink. Light gray band beta at least 1/2 exists unconditionally. A thin blue wedge for 1/2<alpha<2/3 near beta=1/2 is the region of Broucke–Debruyne–Révész under RH, plus a blue segment on alpha=1/2. An orange region down to the curve beta=theta_*(alpha) is new here under RH. The black line beta=alpha/2 is the limit of random sifting, and it coincides with the orange boundary for alpha up to 2/3. The white region below is open. Panel (b): log-log plot of block maxima of the integer error for three random sifted systems with alpha=0.6, growing roughly with slope 0.3, and of the deterministic error E_0, growing roughly with slope 0.1, against dashed reference slopes 0.46, 0.30 and 0.10.](supplement/figure-1.png)

**Figure 1.** (a) Existence of $[\alpha,\beta]$-systems:

- Dark gray: impossible by Hilberdink's theorem.
- Light gray: known unconditionally [3, Theorem 1.1].
- Blue: [3, Theorem 1.3] under RH, together with the segment $\alpha=1/2$ [3].
- Orange: new under RH (Theorem 1). Its lower boundary $\beta=\theta_*(\alpha)$ coincides with the black line $\beta=\alpha/2$ for $\alpha\le2/3$, where the exponent of our construction is exact (Corollary 1). Our construction cannot reach below the black line (Theorem 2); neither can any deletion set of small discrepancy, for example one prime per block chosen by any rule without repeats (Theorem 4).
- White: open.

(b) Exploratory numerics for $\alpha=0.6$ up to $10^8$: dyadic block maxima of $|N_S(x)-a_Sx|$ for three random seeds (blue) and of $|E_0(y)|$ (orange), with dashed reference slopes. The values are in the supplement (`data/`).

## 2. Related work and distinction

For background on Beurling generalized numbers see [4]. Beurling [5] proved the prime number theorem for systems with $N(x)=ax+O(x/\log^\gamma x)$, $\gamma>3/2$. Diamond, Montgomery and Vorhauer [6] showed that integer regularity $N(x)=ax+O(x^\theta)$, $1/2<\theta<1$, is compatible with zeros of $\zeta_{\mathcal P}$ on the curve $\sigma=1-a/\log t$. Their probabilistic discretisation was refined by Zhang [7], who obtained the first unconditional system with both errors $O(x^{1/2+\varepsilon})$, and by Broucke and Vindas [8], who obtained $[0,1/2]$-systems. Broucke, Debruyne and Vindas [9] constructed RH-satisfying systems with extremal integer oscillation. Hilberdink [1] introduced $[\alpha,\beta]$-systems and proved $\max\{\alpha,\beta\}\ge1/2$. Any method that approximates continuous systems with error $O(x^{\theta})$, $\theta<1/2$, on one counting function must lose $x^{1/2-\varepsilon}$ on the other [3, §1]. This suggests building systems with $\beta<1/2$ from a discrete system that already has very regular integers, here $\mathbb N$ under RH.

The closest work is [3]. Both constructions delete a random sparse set of rational primes whose counting function is $\asymp x^\alpha/\log x$. Some form of deletion is needed: [3, §5] shows that, if RH holds, adding generalized primes to $\mathbb P$ cannot produce an $[\alpha,\beta]$-system with $\alpha>1/2$ and $\beta<1/2$. The differences are these.

- **How the primes are chosen.** In [3] the deleted primes come from the Broucke–Vindas procedure [8], with an error measure (restricting $\alpha<2/3$) or with double primes (restricting $\alpha<4/5$). We use independent Bernoulli deletions.
- **How the sifted integers are estimated.** [3] uses the hyperbola method, starting from bounds for the deleted set. We factor the sifted integers exactly into a deterministic mean system and a centred random multiplicative function. The random part is controlled by moments, and the deterministic part by exponential-sum methods under RH.
- **What is new.** The barrier at $\alpha/2$ for our construction (Theorem 2) and for every deletion set of small discrepancy, including one-prime-per-block deletion by any rule without repeats (Theorem 4), the sharpness statement (Corollary 1) and Corollary 2 do not appear in [3]. Remark 20 shows that the random construction of [3] is itself a stratified deletion, so it cannot go below $\alpha/2$ either.

The deterministic problem in Theorem 3 is the error term in the mean value of $g(n)=\prod_{p\mid n}(1-p^{-\kappa})=n^{-\kappa}J_\kappa(n)$, where $J_\kappa$ is the Jordan (Cohen) totient of real index $\kappa=1-\alpha\in(0,1/2)$. Error terms for Jordan totients are classical for integer index $k\ge2$, and Walfisz-type results treat $\kappa\ge1$. We found no treatment with power-saving error terms for real $0<\kappa<1/2$, but Theorem 3 may well be known to experts in some form, so we give a complete proof. Its method parallels error terms for squarefree numbers under RH, where sums $\sum\mu(d)e(x/d^2)$ are handled through $1/\zeta$.

## 3. Notation and the random construction

Fix $\alpha\in(0,1)$ and put $\kappa:=1-\alpha$. Let $(\xi_p)_{p\in\mathbb P}$ be independent Bernoulli variables with

$$
\Pr(\xi_p=1)=q_p:=p^{-\kappa}=p^{\alpha-1},\qquad \eta_p:=\xi_p-q_p,
$$

and let $S:=\{p:\xi_p=1\}$. The sifted system has generalized primes $\mathbb P\setminus S$ and integers $\mathcal N_S:=\{n\ge1:\ p\mid n\Rightarrow p\notin S\}$, with counting function $N_S(x)$. Since $\mathbb E\sum_{p\in S}p^{-1}=\sum_pp^{-1-\kappa}<\infty$, almost surely $a_S:=\prod_{p\in S}(1-1/p)>0$.

Write $F_S(s):=\prod_{p\in S}(1-p^{-s})$, so that $\sum_{n\in\mathcal N_S}n^{-s}=\zeta(s)F_S(s)$ for $\operatorname{Re}s>1$. Further notation:

- $P(u)=\sum_pp^{-u}$ is the prime zeta function; $P(1+u)=\log(1/u)+O(1)$ as $u\downarrow0$.
- $\bar B_1(u):=u-\lfloor u\rfloor-1/2$ is the sawtooth function, and $e(u)=e^{2\pi iu}$.
- $M(x)=\sum_{n\le x}\mu(n)$ is the Mertens function.
- $\psi$ and $\theta$ denote Chebyshev's functions.

The mean of $F_S$ is exact:

$$
\mathbb E\,F_S(s)=\prod_p\bigl(1-q_pp^{-s}\bigr)=\prod_p\bigl(1-p^{-(s+\kappa)}\bigr)=\frac{1}{\zeta(s+\kappa)}\qquad(\operatorname{Re}s>1).
$$

**Analytic inputs under RH.** For every $\varepsilon,\delta>0$, uniformly for $|t|\ge1$:

- $\zeta(\sigma+it)\ll|t|^{\varepsilon}$ for $\sigma\ge1/2$ [10, Theorem 13.18], [11, §14.2];
- $1/\zeta(\sigma+it)\ll|t|^{\varepsilon}$ for $\sigma\ge1/2+\delta$ [10, Theorem 13.23];
- $M(x)\ll x^{1/2+\varepsilon}$ [10, Ch. 13];
- $\psi(x)=x+O(x^{1/2}\log^2x)$ [10, Theorem 13.1].

By the functional equation, $|\zeta(\sigma+it)|\asymp|t|^{1/2-\sigma}|\zeta(1-\sigma-it)|$ for $\sigma$ in compact subsets of $(0,1/2)$ [11, §4.12].

## 4. The deterministic mean system

Let $g(n):=\prod_{p\mid n}(1-p^{-\kappa})\in(0,1]$ and $h(d):=\mu(d)d^{-\kappa}$, so that $g=1*h$. Set

$$
N_0(y):=\sum_{n\le y}g(n)=\sum_{d\le y}h(d)\lfloor y/d\rfloor,\qquad a_0:=\sum_dh(d)/d=1/\zeta(1+\kappa),\qquad E_0(y):=N_0(y)-a_0y.
$$

The Dirichlet series of $g$ is $G(s)=\zeta(s)/\zeta(s+\kappa)$.

**Lemma 1 (Perron bound).** Assume RH and $0<\kappa<1/2$. Then $E_0(y)\ll_\varepsilon y^{\frac{1}{2+2\kappa}+\varepsilon}$ for $y\ge1$.

*Proof.* Under RH, $G$ is meromorphic on $\operatorname{Re}s>1/2-\kappa$ with a single simple pole at $s=1$; the pole of $\zeta(s+\kappa)$ at $s=1-\kappa$ produces a zero of $G$. Fix $\delta\in(0,\kappa)$ and set $c:=1/2-\kappa+\delta\in(0,1/2)$. By the analytic inputs,

$$
G(\sigma+it)\ll|t|^{\max(1/2-\sigma,0)+\varepsilon}\qquad(c\le\sigma\le2,\ |t|\ge1).
$$

Since $0\le g\le1$, the truncated Perron formula [10, Corollary 5.3] with $\sigma_0=1+1/\log y$ and $2\le T\le y$ expresses $N_0(y)$ as $\frac1{2\pi i}\int_{\sigma_0-iT}^{\sigma_0+iT}G(s)y^s\,ds/s$ plus $O(y\log y/T+1)$.

Move the contour to $\operatorname{Re}s=c$:

- the residue at $s=1$ is $a_0y$, and $s=0$ is not enclosed;
- the new vertical side contributes $\ll y^cT^{1/2-c+\varepsilon}$;
- the horizontal sides contribute $\ll T^{\varepsilon}(y^cT^{-1/2-c}+y^{1/2}T^{-1}+yT^{-1})$.

Taking $T=y^{(1-c)/(3/2-c)}$ gives $E_0(y)\ll y^{1/(3-2c)+2\varepsilon}$. Now let $\delta\to0$. $\square$

In terms of $\alpha$ this exponent is $1/(4-2\alpha)$. The rest of this section improves it for $\alpha<3/4$.

**Lemma 2 (reduction).** Assume RH and $0<\kappa<1/2$. With $\mathcal T(y):=\sum_{d\le y}\mu(d)d^{-\kappa}\bar B_1(y/d)$,

$$
E_0(y)=-\mathcal T(y)+O\bigl(y^{1/2-\kappa+\varepsilon}\bigr).
$$

*Proof.* Insert $\lfloor u\rfloor=u-\tfrac12-\bar B_1(u)$ into $N_0(y)$. This gives

$$
E_0(y)=-y\sum_{d>y}h(d)/d-\tfrac12\mathcal H(y)-\mathcal T(y),\qquad \mathcal H(u):=\sum_{d\le u}h(d).
$$

Partial summation from $M(x)\ll x^{1/2+\varepsilon}$ gives $\mathcal H(u)\ll u^{1/2-\kappa+\varepsilon}$ (here $\kappa<1/2$ is used) and $y\sum_{d>y}h(d)/d\ll y^{1/2-\kappa+\varepsilon}$. $\square$

Fix once and for all a non-increasing $w_0\in C^\infty(\mathbb R)$ with $w_0=1$ on $(-\infty,1]$ and $w_0=0$ on $[2,\infty)$, and put $w(v):=w_0(v)-w_0(2v)$. Then $w\ge0$ is smooth, vanishes outside $[1/2,2]$, and vanishes to infinite order at $1/2$ and at $2$.

**Lemma 3 (oscillatory Mellin transform).** For $\sigma\in[1/4,3]$, $\lambda\ge1$ and $t\in\mathbb R$ let

$$
I(t)=I_\sigma(t):=\int_{1/2}^{2}v^{\sigma-\kappa-1+it}w(v)e(\lambda/v)\,dv.
$$

Then:

- (i) $I(t)\ll\lambda^{-1/2}$ for all $t$;
- (ii) for every $A>0$, $I(t)\ll_A(\lambda+|t|)^{-A}$ whenever $t\notin[\pi\lambda/2,8\pi\lambda]$.

The implied constants depend only on $A$, $\kappa$ and $w_0$; they are uniform in $\sigma\in[1/4,3]$.

*Proof.* Write $I(t)=\int b\,e^{i\phi}$ with $b(v)=v^{\sigma-\kappa-1}w(v)$ and $\phi(v)=2\pi\lambda/v+t\log v$, so that $\phi'(v)=(tv-2\pi\lambda)/v^2$.

*Non-stationary case.*

- If $t\le\pi\lambda/2$ (including $t<0$), then on $[1/2,2]$ we have $tv-2\pi\lambda\le-\pi\lambda$ when $t\ge0$, and $tv-2\pi\lambda\le-(2\pi\lambda+|t|/2)$ when $t<0$.
- If $t\ge8\pi\lambda$, then $tv-2\pi\lambda\ge t/4$.

In both cases $|\phi'|\gg\lambda+|t|$ on $[1/2,2]$, while $\phi^{(j)}\ll_j\lambda+|t|$. Integrate by parts $A$ times. Every boundary term vanishes because $b$ vanishes to infinite order at the endpoints, and this gives (ii).

*Stationary case.* If $t\in[\pi\lambda/2,8\pi\lambda]$, the stationary point $v_0=2\pi\lambda/t$ lies in $[1/4,4]$, and $\phi''(v)=t(2v_0-v)/v^3$.

- On $[1/2,2]\cap(-\infty,3v_0/2]$ we have $\phi''\ge t/64$. The second-derivative test for integrals [11, §4.2], combined with partial integration against the bounded-variation amplitude $b$, gives $\ll t^{-1/2}$.
- On $[1/2,2]\cap[3v_0/2,\infty)$ we have $\phi'=t(v-v_0)/v^2\ge t/32$. After splitting at $2v_0$ the derivative $\phi'$ is monotone on each piece, and the first-derivative test [11, §4.2] gives $\ll t^{-1}$.

Since $t\asymp\lambda$ in this case, (i) follows. $\square$

**Lemma 4 (twisted sums, RH).** Assume RH. For $1\le D\le y$ and $h\ge1$,

$$
U(h):=\sum_d\mu(d)d^{-\kappa}w(d/D)e(hy/d)\ll_\varepsilon D^{1/2-\kappa+\varepsilon}(hy/D)^{1/2+\varepsilon}.
$$

*Proof.* The function $f(u)=u^{-\kappa}w(u/D)e(hy/u)$ is smooth with compact support. Its Mellin transform is $\tilde f(s)=D^{s-\kappa}I_\sigma(\operatorname{Im}s)$, with $\lambda=hy/D\ge1$ and $\sigma=\operatorname{Re}s$. Mellin inversion gives

$$
U(h)=\frac1{2\pi i}\int_{(2)}\tilde f(s)\zeta(s)^{-1}\,ds.
$$

Under RH we may move the line of integration to $\operatorname{Re}s=1/2+\varepsilon$: the integrand is analytic in between, and the horizontal contributions vanish by Lemma 3(ii), uniformly in $\sigma$. On the new line $|1/\zeta|\ll(1+|t|)^{\varepsilon}$; for $|t|\le1$ this holds because $\zeta$ has no zeros there. Lemma 3 then gives

$$
|U(h)|\ll D^{1/2+\varepsilon-\kappa}\Bigl(\int_{\pi\lambda/2}^{8\pi\lambda}\lambda^{-1/2}t^{\varepsilon}\,dt+\int_{\mathbb R}(\lambda+|t|)^{-2}(1+|t|)^{\varepsilon}\,dt\Bigr)\ll D^{1/2-\kappa+\varepsilon}\lambda^{1/2+\varepsilon}.\qquad\square
$$

**Lemma 5 (smooth sums).** If $8hy\le D^2$, then $V(h):=\sum_dd^{-\kappa}w(d/D)e(hy/d)\ll D^{2-\kappa}/(hy)$.

*Proof.* On $[D/2,2D]$ the phase $f(u)=hy/u$ has monotone derivative $f'(u)=-hy/u^2\in[-4hy/D^2,-hy/(4D^2)]\subset[-1/2,0)$. This stays at distance at least $hy/(4D^2)$ from the integers. The Kusmin–Landau inequality [12, Ch. 2] therefore bounds every partial sum of $e(f(d))$ over a subinterval by $\ll D^2/(hy)$. Partial summation against $d^{-\kappa}w(d/D)$, which has size and total variation $\ll D^{-\kappa}$, completes the proof. $\square$

(By Poisson summation $V(h)$ is in fact $\ll_A D^{1-\kappa}(D/hy)^A$. The weaker bound suffices here, and the exponents below are not affected.)

**Proposition 6 (dyadic block).** Assume RH and $10\sqrt y\le D\le y/2$. Then

$$
S_D:=\sum_d\mu(d)d^{-\kappa}w(d/D)\bar B_1(y/d)\ll_\varepsilon y^{1/3+\varepsilon}D^{1/3-\kappa}.
$$

*Proof.* Let $H:=\lceil D^{2/3}y^{-1/3}\rceil$. Since $D^{2/3}y^{-1/3}\ge10^{2/3}>4$, we have $H\le1.25\,D^{2/3}y^{-1/3}$, and hence $8Hy\le10D^{2/3}y^{2/3}\le D^2$.

Vaaler's theorem [13; 12, Appendix] gives a trigonometric polynomial $\bar B_1^*$ of degree $H$, with coefficients $|c_h|\le1/(2\pi|h|)$, such that for all real $u$

$$
|\bar B_1(u)-\bar B_1^*(u)|\le\frac{1}{2H+2}\sum_{|h|\le H}\Bigl(1-\frac{|h|}{H+1}\Bigr)e(hu).
$$

The right side is non-negative. At integers it equals $1/2$, which bounds $|\bar B_1(n)-\bar B_1^*(n)|=1/2$. Using $|\mu|\le1$ and $w\ge0$,

$$
|S_D|\le\sum_{1\le|h|\le H}|c_h||U(h)|+\frac{1}{2H+2}\Bigl(V(0)+2\sum_{1\le h\le H}|V(h)|\Bigr).
$$

Each term is $\ll y^{1/3+3\varepsilon}D^{1/3-\kappa}\log y$:

- By Lemma 4, $\sum_h|c_h||U(h)|\ll D^{-\kappa+\varepsilon}y^{1/2+\varepsilon}\sum_{h\le H}h^{-1/2+\varepsilon}\ll y^{1/3+3\varepsilon}D^{1/3-\kappa}$.
- Trivially $V(0)\ll D^{1-\kappa}$, and $V(0)/H\ll y^{1/3}D^{1/3-\kappa}$.
- By Lemma 5, $H^{-1}\sum_{h\le H}|V(h)|\ll D^{2-\kappa}(Hy)^{-1}\log y\ll D^{4/3-\kappa}y^{-2/3}\log y\le y^{1/3}D^{1/3-\kappa}\log y$, since $D\le y$. $\square$

**Theorem 3 (deterministic exponent).** Assume RH and $1/2<\alpha<1$, $\kappa=1-\alpha$. Then $E_0(y)\ll_\varepsilon y^{\theta_*(\alpha)+\varepsilon}$.

*Proof.* For $\alpha\ge3/4$ this is Lemma 1, so let $\alpha<3/4$. By Lemma 2 it suffices to bound $\mathcal T(y)$.

*Partition.* Let $Y_1:=5\sqrt y$ and $Y_2:=y/\mathcal M$, with $\mathcal M\ge4$ to be chosen. Let $J\ge0$ be maximal with $2^JY_1\le Y_2$. Telescoping gives

$$
1=w_0(d/Y_1)+\sum_{j=1}^{J}w\bigl(d/(2^jY_1)\bigr)+\bigl(1-w_0(d/(2^JY_1))\bigr).
$$

This splits $\mathcal T(y)$ into three parts.

- *Low part.* The weight is supported on $d\le2Y_1$, so the part is at most $\sum_{d\le2Y_1}d^{-\kappa}\ll y^{(1-\kappa)/2}=y^{\alpha/2}$.
- *Middle part.* Each block has $D=2^jY_1\ge10\sqrt y$, so Proposition 6 applies and gives $\ll y^{1/3+\varepsilon}\log y\cdot\max(Y_1^{1/3-\kappa},Y_2^{1/3-\kappa})$.
- *High part.* The weight is supported on $d\ge2^JY_1>y/(2\mathcal M)$. Group the $d$ by $m=\lfloor y/d\rfloor\le2\mathcal M$. On $(y/(m+1),y/m]$ we have $\bar B_1(y/d)=y/d-m-1/2$, which is monotone. So the weight $d^{-\kappa}(1-w_0(\cdot))\bar B_1(y/d)$ has size and total variation $\ll(y/m)^{-\kappa}$. Partial summation with $M(x)\ll x^{1/2+\varepsilon}$ bounds each group by $\ll(y/m)^{1/2-\kappa+\varepsilon}$, and summing over $m$ gives $\ll y^{1/2-\kappa+\varepsilon}\mathcal M^{1/2+\kappa}$.

*Choice of $\mathcal M$.*

- If $\alpha\le2/3$ (so $\kappa\ge1/3$), take $\mathcal M=4$. The middle part is $\ll y^{1/3+(1/3-\kappa)/2+2\varepsilon}=y^{\alpha/2+2\varepsilon}$, and the high part is $\ll y^{\alpha-1/2+\varepsilon}$.
- If $2/3<\alpha<3/4$, take $\mathcal M=y^{1/5}$. Both the middle part (dominated by $Y_2$) and the high part are $\ll y^{(4\alpha-1)/5+2\varepsilon}$. The low part is smaller, since $\alpha/2\le(4\alpha-1)/5$. $\square$

Note that $\theta_*(\alpha)\ge\alpha/2$ always, with equality exactly when $\alpha\le2/3$.

## 5. Factorisation and moments

Define a random multiplicative function $z$ by $z(p^k):=-\eta_p\,q_p^{\,k-1}$ for $k\ge1$. Then $|z(n)|\le1$, the families $(z(p^k))_{k\ge1}$ are independent across primes, and $\mathbb Ez(n)=0$ for $n>1$.

**Lemma 7 (exact factorisation).** $\mathbf 1_{\mathcal N_S}=g*z$. Hence $N_S(x)=\sum_{d\le x}z(d)N_0(x/d)$ for $x\ge1$.

*Proof.* All three functions are multiplicative. With $u=p^{-s}$ the local factors are

$$
\sum_k\mathbf 1_{\mathcal N_S}(p^k)u^k=\frac{1-\xi_pu}{1-u},\qquad \sum_kg(p^k)u^k=\frac{1-q_pu}{1-u},\qquad \sum_kz(p^k)u^k=1-\frac{\eta_pu}{1-q_pu}=\frac{1-\xi_pu}{1-q_pu},
$$

and the product of the last two is the first. $\square$

**Lemma 8 (moments).** Let $\tau\in(\alpha/2,1)$ and $W>0$, and let $(w_d)$ be finitely supported reals with $|w_d|\le Wd^{-\tau}$. For every integer $k\ge1$,

$$
\mathbb E\Bigl(\sum_dz(d)w_d\Bigr)^{2k}\le K\,W^{2k},\qquad K=\exp\bigl(2\cdot5^{2k}P(\kappa+2\tau)\bigr)<\infty.
$$

*Proof.* By independence, $\mathbb E\prod_{i\le2k}z(d_i)=\prod_p\mathbb E\prod_iz(p^{v_p(d_i)})$. Fix $p$ and let $A=\{i:p\mid d_i\}$.

- If $|A|=1$, the local factor is $0$.
- If $|A|=m\ge2$, the local factor is $(-1)^m\mathbb E[\eta_p^m]\prod_{i\in A}q_p^{v_p(d_i)-1}$, and $|\mathbb E\eta_p^m|\le q_p(1-q_p)^m+(1-q_p)q_p^m\le2q_p$.

Insert $|w_{d_i}|\le Wd_i^{-\tau}$, drop the support restrictions, and factorise the non-negative sum over $2k$-tuples into an Euler product. This gives the bound $W^{2k}\prod_pL_p$ with

$$
L_p=1+2q_p\sum_{m=2}^{2k}\binom{2k}{m}\Bigl(\frac{p^{-\tau}}{1-q_pp^{-\tau}}\Bigr)^m.
$$

Since $\kappa+\tau>1/2$, we have $q_pp^{-\tau}\le2^{-1/2}$, so the bracket is at most $4p^{-\tau}$ and $L_p\le1+2\cdot5^{2k}p^{-\kappa-2\tau}$. Finally $\kappa+2\tau>\kappa+\alpha=1$. $\square$

## 6. The integers of the sifted system

**Proposition 9.** Assume RH and $1/2<\alpha<1$. Almost surely, for every $\varepsilon>0$,

$$
N_S(x)=a_Sx+O\bigl(x^{\theta_*(\alpha)+\varepsilon}\bigr).
$$

*Proof.* *The constant.* $\mathbb E\sum_d|z(d)|/d\le\prod_p(1+4p^{-1-\kappa})<\infty$, so $Z(1):=\sum_dz(d)/d$ converges absolutely almost surely. Its Euler product is $\prod_p(1-\xi_p/p)/(1-q_p/p)$, and $a_0=\prod_p(1-q_p/p)$, so $a_0Z(1)=a_S$.

*Decomposition.* By Lemma 7,

$$
N_S(x)-a_Sx=X_1(x)-X_2(x),\qquad X_1(x):=\sum_{d\le x}z(d)E_0(x/d),\quad X_2(x):=a_0x\sum_{d>x}\frac{z(d)}{d}.
$$

*Moments.* Fix $\varepsilon\in(0,1/10)$ and let $\tau:=\theta_*+\varepsilon\in(\alpha/2,1)$.

- By Theorem 3, $|E_0(y)|\le C_\varepsilon y^{\tau}$ for $y\ge1$. Lemma 8 with $W=C_\varepsilon x^\tau$ gives $\mathbb EX_1(x)^{2k}\ll x^{2k\tau}$.
- For $d>x$ we have $x/d\le(x/d)^\tau$. Lemma 8, applied to the truncations $\sum_{x<d\le X'}$ and followed by Fatou's lemma as $X'\to\infty$, gives $\mathbb EX_2(x)^{2k}\ll x^{2k\tau}$.

*Conclusion.* By Markov's inequality, $\Pr(|N_S(x)-a_Sx|\ge x^{\theta_*+2\varepsilon})\ll x^{-2k\varepsilon}$ for integers $x$. With $k=\lceil1/\varepsilon\rceil$ this is summable, so Borel–Cantelli applies. Between consecutive integers $N_S$ is constant and $a_Sx$ moves by at most $1$. Finally, intersect over $\varepsilon=1/j$. $\square$

## 7. Primes, and analytic continuation of $F_S$

**Lemma 10 (primes).** Assume RH and $1/2<\alpha<1$. Almost surely

$$
\psi_{\mathbb P\setminus S}(x)=x-\frac{x^\alpha}{\alpha}+O\bigl(x^{1/2}\log^2x\bigr).
$$

*Proof.* We have $\psi_{\mathbb P\setminus S}(x)=\psi(x)-\sum_{p\in S,p\le x}\log p+O(x^{1/2})$, where the $O$-term absorbs prime powers. Split the sum as $\sum_{p\le x}q_p\log p+\sum_{p\le x}\eta_p\log p$.

- Partial summation with $\theta(u)=u+O(u^{1/2}\log^2u)$ gives $\sum_{p\le x}p^{-\kappa}\log p=x^\alpha/\alpha+O(x^{\alpha-1/2}\log^2x+1)$.
- The summands $\eta_p\log p$ are independent and centred, bounded by $\log x$, with total variance $\ll x^\alpha\log x$. Bernstein's inequality [14, Ch. 2] gives $\Pr(|\sum_{p\le x}\eta_p\log p|\ge x^{\alpha/2+\varepsilon})\le2\exp(-cx^{2\varepsilon}/\log x)$, which is summable over integers $x$. $\square$

**Lemma 11 (continuation).** Let $0<\alpha<1$. Almost surely there is $Q_S$, analytic on $\operatorname{Re}s>\alpha/2$, with

$$
F_S(s)=\frac{e^{-Q_S(s)}}{\zeta(s+\kappa)}\quad(\operatorname{Re}s>1),\qquad Q_S(s)=R(s)-\mathcal B(s),
$$

where

$$
R(s):=\sum_p\eta_pp^{-s},\qquad \mathcal B(s):=\sum_p\sum_{k\ge2}\frac{q_p^k-\xi_p}{k}p^{-ks}.
$$

So $F_S$ continues meromorphically to $\operatorname{Re}s>\alpha/2$, and analytically away from the zeros of $\zeta(s+\kappa)$. Under RH it is analytic on all of $\operatorname{Re}s>\alpha/2$, and its only zero there is a simple zero at $s=\alpha$.

*Proof.* Comparing the logarithms of the two Euler products gives the identity.

- *$R$.* At $\sigma_j=\alpha/2+1/j$ the variances are summable, since they are bounded by $P(\kappa+2\sigma_j)<\infty$. By Kolmogorov's one-series theorem [15, Ch. 2], $R(\sigma_j)$ converges almost surely, and a Dirichlet series that converges at a real point converges locally uniformly to its right [10, Ch. 1].
- *$\mathcal B$.* It converges absolutely and locally uniformly on $\operatorname{Re}s>\alpha/2$. The $\xi_p$-part does so because $\mathbb E\sum_p\xi_pp^{-2\sigma}=P(\kappa+2\sigma)<\infty$ for $\sigma>\alpha/2$. The $q_p^k$-part does so because $\sum_p\sum_{k\ge2}q_p^kp^{-k\sigma}\ll P(2\kappa+2\sigma)<\infty$ for $\sigma>\alpha-1/2$, which holds since $\alpha/2>\alpha-1/2$.
- *Under RH.* $\zeta(s+\kappa)\ne0$ on $\operatorname{Re}s>\alpha/2$, since there $\operatorname{Re}(s+\kappa)>1-\alpha/2>1/2$; its only singularity in that region is the pole at $s=\alpha$. $\square$

## 8. Proof of Theorem 1

**Theorem 1.** Assume RH, $1/2<\alpha<1$ and $\theta_*(\alpha)\le\beta<1/2$. Almost surely:

- if $\beta>\alpha/2$, the multiset $\mathcal P_{\alpha,\beta}:=(\mathbb P\setminus S)\cup\{p^{1/\beta}:p\in\mathbb P\}$ is an $[\alpha,\beta]$-system;
- if $\beta=\alpha/2$ (possible only when $\alpha\le2/3$), the system $\mathbb P\setminus S$ itself is an $[\alpha,\alpha/2]$-system.

*Proof.* Work on the almost sure event on which Proposition 9, Lemmas 10 and 11, and Theorem 2 hold.

*Case $\beta=\alpha/2$.* Proposition 9 gives the upper bound and Theorem 2 the optimality. Lemma 10 gives exactly $\alpha$ for the primes.

*Case $\beta>\alpha/2$: upper bound.* Generalized integers are counted with multiplicity of factorisation. So the generalized integers of $\mathcal P_{\alpha,\beta}$ are the formal products $n\cdot m^{1/\beta}$ with $n\in\mathcal N_S$ and $m\in\mathbb N$, each pair $(n,m)$ counted once. As real numbers two such products may coincide, for example $8\cdot1=1\cdot2^3$ when $\beta=1/3$. Hence $N_{\alpha,\beta}(x)=\sum_{m\le x^\beta}N_S(x/m^{1/\beta})$. By Proposition 9, together with $\sum_{m>x^\beta}m^{-1/\beta}\ll x^{\beta-1}$ and $\sum_{m\le M_1}m^{-\gamma}\ll M_1^{\max(1-\gamma,0)}\log(M_1+1)$, we get $N_{\alpha,\beta}(x)=a_S\zeta(1/\beta)x+O(x^{\beta+\varepsilon}\log x)$ for every $\varepsilon>0$, using $\theta_*\le\beta$.

*Case $\beta>\alpha/2$: not better.* For $\operatorname{Re}s>1$ we have $\int_{1^-}^\infty x^{-s}dN_{\alpha,\beta}=\zeta(s)F_S(s)\zeta(s/\beta)$.

- By Lemma 11, $\zeta F_S$ is analytic on $\operatorname{Re}s>\alpha/2$ except at $1$. It is non-zero at $\beta\in(\alpha/2,\alpha)$:
  - $\zeta(\beta)<0$;
  - $F_S(\beta)=e^{-Q_S(\beta)}/\zeta(\beta+\kappa)\ne0$, because $\zeta(\beta+\kappa)$ is finite for $\beta\ne\alpha$.

  This step uses no RH, since $\beta$ is real.
- So the product has a simple pole at $s=\beta$, coming from $\zeta(s/\beta)$.
- Suppose $N_{\alpha,\beta}(x)=Ax+O(x^{\beta-\eta})$ with $0<\eta<\beta-\alpha/2$.
  - Then $As/(s-1)+s\int_1^\infty(N_{\alpha,\beta}(x)-Ax)x^{-s-1}dx$ is analytic on $\operatorname{Re}s>\beta-\eta$ except at $1$.
  - It agrees with $\zeta(s)F_S(s)\zeta(s/\beta)$ for $\operatorname{Re}s>1$. By uniqueness of continuation, it agrees on the connected set $\{\operatorname{Re}s>\beta-\eta\}\setminus\{1,\beta\}$, which under RH contains no zero of $\zeta(s+\kappa)$.
  - So the product would be bounded near $s=\beta$, contradicting the pole.

Here $\beta>\alpha/2$ is needed, because $F_S$ is only known to continue to $\operatorname{Re}s>\alpha/2$.

*Primes.* $\psi_{\alpha,\beta}(x)=\psi_{\mathbb P\setminus S}(x)+\beta^{-1}\psi(x^\beta)=x-x^\alpha/\alpha+O(x^{1/2}\log^2x)$ by Lemma 10. Since $\alpha>1/2$, the exponent is exactly $\alpha$. $\square$

**Corollary 1.** Assume RH and $1/2<\alpha\le2/3$. Almost surely $\mathbb P\setminus S$ is an $[\alpha,\alpha/2]$-system.

*Proof.* This is the case $\beta=\alpha/2$ of Theorem 1. It is admissible because $\theta_*(\alpha)=\alpha/2$ for $\alpha\le2/3$. $\square$

## 9. The limit of our construction

**Theorem 2 (unconditional).** Let $0<\alpha<1$ and let $S$ be the random set of §3, so that $q_p=p^{\alpha-1}$. Almost surely $N_S(x)-a_Sx\ne O(x^{\alpha/2-\eta})$ for every $\eta>0$.

*Setting for Lemmas 12 and 13.* To treat other profiles at the same time, let $c>0$ and $q_p=\min(1,cp^{-\kappa})$, with independent $\xi_p\sim\mathrm{Bernoulli}(q_p)$ and $\eta_p=\xi_p-q_p$. The construction of §3 is $c=1$. Put

$$
R(s):=\sum_{p:\,q_p<1}\eta_pp^{-s},\qquad v(\sigma):=\sum_{p:\,q_p<1}q_p(1-q_p)p^{-2\sigma}.
$$

- For $c=1$ every $q_p<1$, and $R$ is the series of Lemma 11.
- For $\operatorname{Re}s\ge0$ the summands are independent, centred and bounded by $1$ in modulus, and $\mathbb E|R(s)|^2=v(\operatorname{Re}s)$.
- As in Lemma 11, $R$ converges almost surely, locally uniformly on $\operatorname{Re}s>\alpha/2$.
- Since $2\kappa+\alpha>1$ and only finitely many $p$ have $q_p=1$,
$$
v(\sigma)=cP(\kappa+2\sigma)+O(1)=c\log\frac{1}{\sigma-\alpha/2}+O(1)\qquad(\sigma\downarrow\alpha/2).
$$

**Lemma 12.** Almost surely, $R(\sigma)=o\bigl(\log\frac{1}{\sigma-\alpha/2}\bigr)$ as $\sigma\downarrow\alpha/2$.

*Proof.* Let $I_n=[\alpha/2+e^{-n-1},\alpha/2+e^{-n}]$ and $r_n=0.3e^{-n}$. The three discs of radius $r_n/2$ centred at $\alpha/2+(0.37+0.3j)e^{-n}$, $j=0,1,2$, cover $I_n$. The concentric discs of radius $r_n$ lie in $\operatorname{Re}s\ge\alpha/2+0.07e^{-n}$.

- *Subharmonicity.* Since $|R|^4$ is subharmonic, its supremum over each small disc is at most $4\pi^{-1}r_n^{-2}\int_{\text{large disc}}|R|^4\,dA$.
- *Moments.* On the large discs the variance satisfies $v(\operatorname{Re}s)\le cP(\kappa+2\operatorname{Re}s)\le cn+O(1)$.
  - Rosenthal's inequality [16], applied to the real and imaginary parts of the partial sums and followed by Fatou's lemma, gives $\mathbb E|R(s)|^4\ll v^2+v\ll n^2$.
  - By Tonelli's theorem, $\mathbb E\sup_{I_n}|R|^4\ll n^2$. Tonelli applies because $R$ is jointly measurable, as a locally uniform limit of continuous functions.
- *Borel–Cantelli.* Fix $\varepsilon>0$. Then $\Pr(\sup_{I_n}|R|>\varepsilon n)\ll\varepsilon^{-4}n^{-2}$, which is summable, and $\log(1/(\sigma-\alpha/2))\ge n$ on $I_n$. Intersecting over $\varepsilon=1/j$, $j\in\mathbb N$, gives the claim for all $\varepsilon$ at once. $\square$

**Lemma 13.** Almost surely $R$ is unbounded near $\alpha/2$: $\limsup_{\sigma\downarrow\alpha/2}|R(\sigma)|=\infty$.

*Proof.* Let $\Omega_0$ be the almost sure event on which $R$ converges locally uniformly on $\operatorname{Re}s>\alpha/2$. Let $A\subset\Omega_0$ be the event that $R$ is unbounded on $(\alpha/2,\alpha/2+1)$. Since $R$ is continuous on $(\alpha/2,\infty)$, $A$ is the event that $|R(\sigma)|$ is unbounded as $\sigma\downarrow\alpha/2$. The supremum may be taken over rational $\sigma$, so $A$ is measurable.

- *Zero–one law.* For $z\ge2$ split $R=R_{\le z}+R_{>z}$ at $p=z$. Then $|R_{\le z}(\sigma)|\le\pi(z)$ for all $\sigma>0$. So $\Omega_0$ and $A$ belong to $\mathcal F_{>z}$, the σ-algebra generated by $(\xi_p)_{p>z}$, for every $z$. By Kolmogorov's 0–1 law [15, Ch. 2], $\Pr(A)\in\{0,1\}$.
- *Positive probability.* Let $\sigma_n\in(\alpha/2,\alpha/2+1)$ decrease to $\alpha/2$, and put $v_n=v(\sigma_n)$, so that $v_n\to\infty$.
  - As in Lemma 12, $\mathbb ER(\sigma_n)^4\le C(v_n^2+v_n)\le2Cv_n^2$ once $v_n\ge1$.
  - For $X\ge0$ and $0<\theta<1$, Cauchy–Schwarz gives $\mathbb EX\le\theta\,\mathbb EX+(\mathbb EX^2)^{1/2}\Pr(X>\theta\,\mathbb EX)^{1/2}$. This is the Paley–Zygmund inequality. Applied to $X=R(\sigma_n)^2$, whose mean is $v_n$, with $\theta=1/2$, it gives
$$
\Pr\bigl(R(\sigma_n)^2>v_n/2\bigr)\ge\frac14\cdot\frac{v_n^2}{\mathbb ER(\sigma_n)^4}\ge\frac1{8C}.
$$
  - Fix $L>0$. For all large $n$ we have $v_n/2>L^2$, so $\Pr(|R(\sigma_n)|>L)\ge1/(8C)$. By the reverse Fatou lemma, $\Pr(|R(\sigma_n)|>L\text{ for infinitely many }n)\ge1/(8C)$.
  - These events decrease as $L\to\infty$ through the integers. Their intersection with $\Omega_0$ is contained in $A$, so $\Pr(A)\ge1/(8C)$ by continuity from above.

Hence $\Pr(A)>0$, so $\Pr(A)=1$. $\square$

*Proof of Theorem 2.* Here $c=1$. Work on the almost sure event on which Lemmas 11 and 12 hold. Suppose that $N_S(x)=a_Sx+O(x^{\alpha/2-\eta})$ for some $\eta>0$.

*Step 1.* Then

$$
\zeta F_S=\frac{a_Ss}{s-1}+s\int_1^\infty(N_S-a_Sx)x^{-s-1}dx
$$

is analytic on $\operatorname{Re}s>\alpha/2-\eta$ except at $1$.

- It agrees with the continuation of Lemma 11 on the domain $\{\operatorname{Re}s>\alpha/2\}\setminus(\{1\}\cup\{\zeta(s+\kappa)=0\})$. This domain is connected, because the removed set is closed and discrete, and it contains $(\alpha/2,\infty)\setminus\{1\}$.
- Since $\zeta(\alpha/2)\ne0$, $F:=\zeta F_S/\zeta$ is analytic near $\alpha/2$ and not identically zero.
- So $|F(\sigma)|\asymp(\sigma-\alpha/2)^m$ as $\sigma\downarrow\alpha/2$, for some integer $m\ge0$.

*Step 2.* Now expand $Q_S(\sigma)=R(\sigma)-\mathcal B(\sigma)$ as $\sigma\downarrow\alpha/2$. On the event of Lemma 11, $\sum_p\xi_pp^{-2\sigma'}<\infty$ for every $\sigma'>\alpha/2$.

- In $\mathcal B$, the terms with $k\ge3$ are bounded uniformly in $\sigma>\alpha/2$. They are at most a constant times $\sum_p(q_p^3+\xi_p)p^{-3\alpha/2}$. This is finite because $3\kappa+3\alpha/2>1$, and by the previous sentence with $\sigma'=3\alpha/4$.
- The $k=2$ term of $-\mathcal B$ equals $\tfrac12\sum_p\xi_pp^{-2\sigma}-\tfrac12\sum_pq_p^2p^{-2\sigma}$. The second sum is bounded, because $2\kappa+\alpha>1$.
- In the first sum, write $\xi_p=q_p+\eta_p$.
  - Then $\sum_p\eta_pp^{-2\sigma}=R(2\sigma)$, which is analytic for $\sigma>\alpha/4$ and hence bounded near $\sigma=\alpha/2$.
  - Meanwhile $\sum_pq_pp^{-2\sigma}=P(\kappa+2\sigma)=\log\frac1{\sigma-\alpha/2}+O(1)$.

Hence $Q_S(\sigma)=R(\sigma)+\tfrac12\log\frac1{\sigma-\alpha/2}+O(1)$. Also $\zeta(\sigma+\kappa)\to\zeta(1-\alpha/2)\in(-\infty,0)$. By Lemma 12, the continuation $F_S=e^{-Q_S}/\zeta(s+\kappa)$ satisfies $|F_S(\sigma)|=(\sigma-\alpha/2)^{1/2+o(1)}$.

*Step 3.* On $(\alpha/2,\alpha/2+\delta)$ we have $F=F_S$, so comparing Steps 1 and 2 gives $R(\sigma)=(m-\tfrac12)\log\frac1{\sigma-\alpha/2}+O(1)$. Since $m$ is an integer, $m-\tfrac12\ne0$, which contradicts Lemma 12. $\square$

**Proposition 14 (power profiles).** Let $0<\alpha<1$ and $c>0$, and delete each prime independently with probability $q_p=\min(1,cp^{-\kappa})$.

- Almost surely $N_S(x)-a_Sx\ne O(x^{\alpha/2-\eta})$ for every $\eta>0$.
- If $c\notin\mathbb N$, almost surely even $N_S(x)-a_Sx\ne O(x^{\alpha-\eta})$ for every $\eta>0$. So for $\alpha>1/2$ these profiles give no system with $\beta<1/2$.

*Proof.* Let $\mathcal E=\{p:cp^{-\kappa}\ge1\}$. This is a finite set of primes, all of which are deleted surely. As in §3, $a_S>0$ almost surely. Fix the branch $\zeta(s+\kappa)^{-c}=\exp(-c\log\zeta(s+\kappa))$, where $\log\zeta$ is given by its Dirichlet series for $\operatorname{Re}s>\alpha$. For each $p\notin\mathcal E$,

$$
\log(1-\xi_pp^{-s})=c\log(1-p^{-s-\kappa})-\eta_pp^{-s}+\sum_{k\ge2}\frac{cp^{-k\kappa}-\xi_p}{k}p^{-ks}.
$$

Taking the product over $p$ gives, for $\operatorname{Re}s>1$,

$$
F_S(s)=E_1(s)\,\zeta(s+\kappa)^{-c}\,e^{-R(s)+\mathcal B_c(s)},
$$

where

$$
E_1(s):=\prod_{p\in\mathcal E}\frac{1-p^{-s}}{(1-p^{-s-\kappa})^{c}},\qquad \mathcal B_c(s):=\sum_{p\notin\mathcal E}\sum_{k\ge2}\frac{cp^{-k\kappa}-\xi_p}{k}p^{-ks}.
$$

- $E_1$ is analytic and non-zero on $\operatorname{Re}s>0$.
- Almost surely $\mathcal B_c$ converges absolutely and locally uniformly on $\operatorname{Re}s>\alpha/2$:
  - the $\xi_p$-part as in Lemma 11;
  - the $cp^{-k\kappa}$-part because $\sum_p\sum_{k\ge2}p^{-k(\kappa+\sigma)}<\infty$ for $\sigma>\alpha-1/2$, and $\alpha/2>\alpha-1/2$.
- $R$ converges as in the setting of Lemmas 12 and 13.

So the right-hand side is analytic on $\operatorname{Re}s>\alpha$.

*Case $c\notin\mathbb N$.* Suppose $N_S(x)=a_Sx+O(x^{\alpha-\eta})$ with $0<\eta<\alpha$.

- Then $\zeta F_S$ is analytic on $\operatorname{Re}s>\alpha-\eta$ except at $1$.
- $\zeta$ has no zeros in $\{0<\operatorname{Re}s<1,\ |\operatorname{Im}s|<1\}$. So $F_S=\zeta F_S/\zeta$ is analytic on $V:=\{\operatorname{Re}s>\alpha-\eta,\ |\operatorname{Im}s|<1\}$.
- On $V\cap\{\operatorname{Re}s>\alpha\}$, which is connected, it agrees with the right-hand side above, since both agree for $\operatorname{Re}s>1$.
- Near $s=\alpha$ we have $\zeta(s+\kappa)=h(s)/(s-\alpha)$, with $h$ analytic and $h(\alpha)=1$. So for real $\sigma\in(\alpha,\alpha+\delta)$,

$$
F_S(\sigma)=(\sigma-\alpha)^{c}H(\sigma),\qquad H:=E_1h^{-c}e^{-R+\mathcal B_c}.
$$

  Here $H$ is analytic and non-zero on a disc around $\alpha$, with the branch of $h^{-c}$ that is positive on the real axis.
- Then $g:=F_S/H$ is analytic near $\alpha$, and $g(\sigma)=(\sigma-\alpha)^c$ on $(\alpha,\alpha+\delta)$. Let $n_0$ be the order of vanishing of $g$ at $\alpha$. Then $(\sigma-\alpha)^{c-n_0}$ tends to a non-zero limit as $\sigma\downarrow\alpha$. So $c=n_0\in\mathbb N$, a contradiction.

The first claim follows, because $\alpha/2-\eta<\alpha-\eta$.

*Case $c\in\mathbb N$.* Now $\zeta(s+\kappa)^{-c}$ is meromorphic in $\mathbb C$, and $F_S=E_1\zeta(s+\kappa)^{-c}e^{-Q}$ with $Q:=R-\mathcal B_c$ continues meromorphically to $\operatorname{Re}s>\alpha/2$. Steps 1–3 of the proof of Theorem 2 apply with the following changes.

- *Step 1* is unchanged, because $E_1$ is analytic and non-zero near $\alpha/2$. It gives $|F_S(\sigma)|\asymp(\sigma-\alpha/2)^m$ for an integer $m\ge0$.
- *Step 2.* The $cp^{-k\kappa}$-part of $\mathcal B_c$ is bounded near $\sigma=\alpha/2$, because $2(\kappa+\alpha/2)>1$. The $\xi_p$-terms with $k\ge3$ are bounded as before. Finally $\tfrac12\sum_{p\notin\mathcal E}\xi_pp^{-2\sigma}=\tfrac c2P(\kappa+2\sigma)+\tfrac12R(2\sigma)+O(1)$. Hence $Q(\sigma)=R(\sigma)+\tfrac c2\log\frac1{\sigma-\alpha/2}+O(1)$.
- *Step 3.* As $\sigma\downarrow\alpha/2$, $E_1(\sigma)\to E_1(\alpha/2)\ne0$ and $\zeta(\sigma+\kappa)^{-c}\to\zeta(1-\alpha/2)^{-c}\ne0$. So $R(\sigma)=(m-\tfrac c2)\log\frac1{\sigma-\alpha/2}+O(1)$.
  - If $m\ne c/2$, this contradicts Lemma 12.
  - If $m=c/2$, which is possible only for even $c$, then $R$ is bounded near $\alpha/2$, contradicting Lemma 13. $\square$

**Remark 15 (added primes).** Adding the primes $p^{1/\beta'}$ with $\beta'>\alpha/2$, as in Theorem 1, does not remove the barrier $\alpha/2$ of Theorem 2 and Proposition 14.

- The integers of $(\mathbb P\setminus S)\cup\{p^{1/\beta'}:p\in\mathbb P\}$ have Dirichlet series $\zeta(s)F_S(s)\zeta(s/\beta')$.
- $\zeta(s/\beta')$ is analytic and non-zero near $s=\alpha/2$, because $\alpha/(2\beta')\in(0,1)$.
- So Steps 1–3 apply verbatim to $F:=\zeta F_S\zeta(\cdot/\beta')/(\zeta\cdot\zeta(\cdot/\beta'))$. The integer counting function is therefore not $Ax+O(x^{\alpha/2-\eta})$ for any constant $A$ and any $\eta>0$.

So the barrier $\alpha/2$ holds for every independent deletion with a power profile $\min(1,cp^{\alpha-1})$, with or without these added primes. We prove no barrier for:

- profiles that are not of power type;
- correlated deletions other than the regular deletion sets of §10;
- schemes that add other generalized primes.

## 10. Stratified and other regular deletions do not help

Theorem 2 and Proposition 14 concern independent deletions. A natural way to make the deleted set less noisy is negative correlation. Delete exactly one prime from each block ("stratum") of unit expected mass, chosen at random within the block. Heuristically, this lowers the first-order fluctuation of the integer error from $x^{\alpha/2}$ to $x^{\alpha/(2+2\alpha)}$. One can also compensate the density so that the mean has no singularity at $\alpha/2$, or choose the prime in each block deterministically. We show that none of these devices moves the barrier (the compensated case under RH). The proof uses only that the deleted set has small discrepancy from the target density, so we state it in that generality.

**The densities.** Fix $\alpha\in(1/2,1)$ and target densities $\pi_p\in(0,1)$, either

$$
\text{(U)}\quad \pi_p=p^{-\kappa}\qquad\text{or}\qquad \text{(C)}\quad \pi_p=p^{-\kappa}-\tfrac12p^{\alpha/2-1}.
$$

In case (C), $\pi_p>0$ because $p^{\alpha/2}>1/2$.

**Regular deletion sets.** For $S\subset\mathbb P$ put $C_S(y):=\sum_{p\le y}(\mathbf 1_S(p)-\pi_p)$, and call $S$ *$\theta$-regular* if $C_S(y)\ll y^\theta$ for $y\ge2$. If $S$ is $\theta$-regular with $\theta<\alpha$, then $\#(S\cap[1,y])=\sum_{p\le y}\pi_p+O(y^\theta)\asymp y^\alpha/\log y$. So $\sum_{p\in S}p^{-1}<\infty$, and $a_S>0$ as in §3.

**Stratified designs.**

- Order the primes $p_1<p_2<\cdots$, put $\Pi_0=0$ and $\Pi_i=\sum_{l\le i}\pi_{p_l}$, and let prime $p_i$ occupy the interval $\mathcal J_{p_i}:=[\Pi_{i-1},\Pi_i)$ of the mass axis. Put $\pi_{j,p}:=|\mathcal J_p\cap[j,j+1)|$, so that $\sum_j\pi_{j,p}=\pi_p$.
- A *selection* is any sequence of primes $(\mathfrak p_j)_{j\ge0}$ with $\mathcal J_{\mathfrak p_j}\cap[j,j+1)\ne\emptyset$ for every $j$, chosen by any rule (deterministic, random or adaptive). Put $S:=\{\mathfrak p_j:j\ge0\}$.
- The *random design* takes $(U_j)_{j\ge0}$ independent and uniform on $[0,1)$, and $\mathfrak p_j$ the prime $p$ with $j+U_j\in\mathcal J_p$. Then $\Pr(\mathfrak p_j=p)=\pi_{j,p}$.
- Each $\mathcal J_p$ has length less than $1$, so it meets at most two consecutive unit intervals. Hence $\mathfrak p_j=\mathfrak p_{j'}$ with $j<j'$ forces $j'=j+1$. Put $\mathcal D:=\{j:\mathfrak p_j=\mathfrak p_{j+1}\}$. It is empty for selections of distinct primes.
- Put $\nu_j:=((j+1)\log(j+2))^{1/\alpha}$. Since $\sum_{p\le y}\pi_p\asymp y^\alpha/\log y$, every prime $p$ with $\mathcal J_p\cap[j,j+1)\ne\emptyset$ satisfies $p\asymp\nu_j$, with constants depending only on $\alpha$.

For a $\theta$-regular set $S$ with $\theta<\alpha$, and for $\operatorname{Re}s>\alpha$, put

$$
L(s):=\sum_p\pi_p\log(1-p^{-s})=-\sum_{k\ge1}\frac1k\sum_p\pi_pp^{-ks},\qquad \tilde R(s):=\sum_pc_p\log(1-p^{-s}),\quad c_p:=\mathbf 1_S(p)-\pi_p.
$$

Everything converges absolutely there, and $F_S=e^{L+\tilde R}$.

**Lemma 16 (regularity).**

- (i) For every selection and every real $y$, $C_S(y)=C(y)-\#\{j\in\mathcal D:\mathfrak p_j\le y\}$, where $|C(y)|\le1$. In particular every selection of distinct primes is $0$-regular.
- (ii) Let $c_0:=\max(0,3\alpha-2)$. Almost surely, the random design is $(c_0+\varepsilon)$-regular for every $\varepsilon>0$.
- (iii) Let $S$ be $\theta$-regular with $0\le\theta<1$, and let $\tilde R^{(Y)}$ be the part of $\tilde R$ with $p\le Y$. Then $\tilde R$ converges locally uniformly on $\operatorname{Re}s>\theta$ and is analytic there. For $\theta<\sigma<1$ and $Y\ge2$,

$$
|\tilde R(\sigma+it)-\tilde R^{(Y)}(\sigma+it)|\le B_\sigma Y^{\theta-\sigma}(1+|t|),
$$

  with $B_\sigma$ independent of $Y$ and $t$.

*Proof.* (i) Put $C(y):=\sum_j\bigl(\mathbf 1[\mathfrak p_j\le y]-\sum_{p\le y}\pi_{j,p}\bigr)$.

- We have $\sum_j\mathbf 1[\mathfrak p_j=p]=\mathbf 1_S(p)+\#\{j\in\mathcal D:\mathfrak p_j=p\}$ and $\sum_j\pi_{j,p}=\pi_p$. Summing over $p\le y$ gives the identity.
- A block lying entirely below the mass level $\sum_{p\le y}\pi_p$ contributes $1-1$, and a block lying entirely above it contributes $0-0$. Only the block $j$ with $j\le\sum_{p\le y}\pi_p<j+1$ remains, and its contribution lies in $[-1,1]$.

(ii) Write $p(j)$ for the prime whose interval contains $j+1$. Then $\Pr(j\in\mathcal D)\le\pi_{p(j)}^2\ll\nu_j^{-2\kappa}$, so

$$
\mathbb E\,\#\{j\in\mathcal D:\nu_j\le y\}\ll\sum_{\nu_j\le y}\nu_j^{-2\kappa}\ll y^{c_0+\varepsilon/2},
$$

because $\#\{j:\nu_j\le u\}\asymp u^\alpha/\log u$ and $\alpha-2\kappa=3\alpha-2$.

- By Markov's inequality at $y=2^m$ and Borel–Cantelli, almost surely $\#\{j\in\mathcal D:\nu_j\le2^m\}\le2^{m(c_0+\varepsilon)}$ for all large $m$.
- Since $\mathfrak p_j\asymp\nu_j$, this gives $\#\{j\in\mathcal D:\mathfrak p_j\le y\}\ll y^{c_0+\varepsilon}$. Combine with (i).

(iii) Fix $s$ with $\sigma>\theta$, and put $f(y):=\log(1-y^{-s})$ for $y\ge2$.

- We have $|f(y)|\le y^{-\sigma}/(1-2^{-\sigma})$ and $|f'(y)|\le|s|y^{-\sigma-1}/(1-2^{-\sigma})$.
- For $2\le Y<Z$, partial summation gives $\sum_{Y<p\le Z}c_pf(p)=C_S(Z)f(Z)-C_S(Y)f(Y)-\int_Y^ZC_S(y)f'(y)\,dy$.
- With $|C_S(y)|\le By^\theta$, let $Z\to\infty$. The tail is at most $B(1-2^{-\sigma})^{-1}Y^{\theta-\sigma}\bigl(1+|s|/(\sigma-\theta)\bigr)$, and $|s|\le1+|t|$.

The same bound, uniform on compact subsets of $\operatorname{Re}s>\theta$, gives locally uniform convergence. $\square$

**Theorem 4 (regular deletion).** Let $1/2<\alpha<1$, and let $S$ be $\theta$-regular for some $\theta<\alpha/2$.

- (a) In case (U), $N_S(x)-a_Sx\ne O(x^{\alpha/2-\eta})$ for every $\eta>0$.
- (b) Assume RH. In case (C), $N_S(x)-a_Sx\ne O(x^{\alpha/2-\eta})$ for every $\eta>0$.

By Lemma 16, this applies to every selection of distinct primes, chosen by any rule, for all $\alpha\in(1/2,1)$. It applies almost surely to the random design when $\alpha<4/5$, since then $c_0<\alpha/2$.

In case (C), under RH, the remaining primes still violate the square-root law with exponent $\alpha$.

- By partial summation, $\sum_{p\in S,\,p\le x}\log p=\sum_{p\le x}\pi_p\log p+O(x^\theta\log x)$.
- The prime powers of $S$ contribute $O(x^{1/2})$.
- So $\psi_{\mathbb P\setminus S}(x)=x-x^\alpha/\alpha+O(x^{1/2}\log^2x)$, as in Lemma 10.

**Lemma 17 (the mean).** Let $\sigma_*:=\max(\alpha/3,\alpha-1/2)<\alpha/2$ and $\varsigma:=s-\alpha/2$. Below, $e^{L}$ denotes the analytic continuation of $\exp L$ from $\operatorname{Re}s>\alpha$, and $\operatorname{Re}L:=\log|e^{L}|$.

- (a) In case (U), $e^{L}=\zeta(s+\kappa)^{-1}\zeta(2s+\kappa)^{-1/2}e^{H_U}$, where $H_U$ is analytic on $\operatorname{Re}s>\sigma_*$. The square root is the branch that is positive on $(\alpha/2,\infty)$, on the half-plane $\operatorname{Re}s>\alpha/2$.

  For real $\sigma\downarrow\alpha/2$, $e^{L(\sigma)}=\varsigma^{1/2}h(\sigma)$, with $h$ analytic and non-zero on a disc around $\alpha/2$.
- (b) Assume RH. In case (C),

$$
e^{L}=\zeta(s+\kappa)^{-1}\mathcal Q(s)^{1/2}e^{H_C},\qquad \mathcal Q(s):=\frac{\zeta(s+1-\alpha/2)}{\zeta(2s+\kappa)},
$$

  where $H_C$ is analytic on $\operatorname{Re}s>\sigma_*$.
  - $\mathcal Q$ extends analytically and without zeros to $\operatorname{Re}s>\alpha/3$, with $\mathcal Q(\alpha/2)=2$.
  - $e^{L}$ is analytic on $\operatorname{Re}s>\sigma_*$, and its only zero there is a simple zero at $s=\alpha$.
- (c) Assume RH, and let $\sigma_*<\sigma_1\le\sigma\le\alpha/2$. In case (C), $|\operatorname{Re}L(\sigma+it)|\ll\log|t|$ for $|t|\ge2$, uniformly in $\sigma$.

*Proof.* Recall $P(w)=\sum_pp^{-w}$ from §3. The function $P(w)-\log\zeta(w)=-\sum_p\sum_{m\ge2}p^{-mw}/m$ is analytic and bounded on $\operatorname{Re}w\ge1/2+\delta$.

*(a)* Here $L(s)=-\sum_{k\ge1}k^{-1}P(ks+\kappa)$.

- The terms with $k\ge3$ converge absolutely for $\operatorname{Re}s>\alpha/3$.
- Replacing $P$ by $\log\zeta$ in the terms $k=1,2$ costs functions that are analytic for $\operatorname{Re}s>\alpha-1/2$ and for $\operatorname{Re}s>(\alpha-1/2)/2$ respectively.
- Near $s=\alpha/2$ we have $\zeta(2s+\kappa)=(2\varsigma)^{-1}(1+O(\varsigma))$, while $\zeta(s+\kappa)\to\zeta(1-\alpha/2)\in(-\infty,0)$.

*(b)* Here $\pi_pp^{-ks}=p^{-ks-\kappa}-\tfrac12p^{-ks-1+\alpha/2}$.

- The same expansion gives the extra factor $\zeta(s+1-\alpha/2)^{1/2}$, plus analytic terms. Among these, $\tfrac14P(2s+1-\alpha/2)$ converges absolutely for $\operatorname{Re}s>\alpha/4$.
- $\zeta(s+1-\alpha/2)$ and $\zeta(2s+\kappa)$ both have a simple pole at $s=\alpha/2$, with residues $1$ and $1/2$. So $\mathcal Q$ is analytic at $\alpha/2$, with $\mathcal Q(\alpha/2)=2$.
- Under RH, neither factor of $\mathcal Q$ vanishes on $\operatorname{Re}s>\alpha/3$. There $\operatorname{Re}(s+1-\alpha/2)>1-\alpha/6$ and $\operatorname{Re}(2s+\kappa)>1-\alpha/3$, both of which exceed $1/2$. So $\mathcal Q$ has an analytic square root on the half-plane $\operatorname{Re}s>\alpha/3$. We take the branch that is positive on $(\alpha/2,\infty)$, where $\mathcal Q>0$; for real $s>\alpha$ it is the one for which $e^L>0$.
- Under RH, $\zeta(s+\kappa)$ has no zeros on $\operatorname{Re}s>\alpha-1/2$ and has its pole at $s=\alpha$.

*(c)* On the line, every $\zeta(w)$ above has $\operatorname{Re}w\ge1/2+\delta'$ with $\delta'>0$, by the choice of $\sigma_1$.

- $\operatorname{Re}L$ is a fixed linear combination of the numbers $\log|\zeta(w)|$, plus $\operatorname{Re}H_C$, which is bounded on the line.
- Under RH, $\zeta(w)\ll|\operatorname{Im}w|^{\varepsilon}$ and $1/\zeta(w)\ll|\operatorname{Im}w|^{\varepsilon}$ there [10, Theorems 13.18, 13.23]. So each $|\log|\zeta(w)||\ll\log|t|$. $\square$

### Vertical fluctuations

**Lemma 18 (one-sided large values).** Let $S$ be $\theta$-regular, let $\theta<\sigma<\alpha/2$, and put $V_X:=\sum_{p\le X}c_p^2p^{-2\sigma}$. Then $V_X\gg X^{\alpha-2\sigma}/\log X$, and

$$
\sup_{|t|\le X^3}\operatorname{Re}\tilde R(\sigma+it)\ \ge\ \tfrac12V_X^{1/2}-O(1/X)\qquad(X\ge X_0).
$$

In particular $\limsup_{t\to\infty}\operatorname{Re}\tilde R(\sigma+it)/\log t=+\infty$.

No randomness is used. The idea is to tilt the measure $dt$ by a non-negative trigonometric polynomial built from the coefficients of $\tilde R$ at the primes $p\le X$; unique factorisation then makes every other frequency invisible. Positive kernels are classical in proofs of one-sided $\Omega$-results [10, Ch. 15]. A kernel built from the series' own coefficients is the simplest case of Soundararajan's resonance method [17].

*Proof.* Put $\delta:=1/(2X)$ and $w(t):=\bigl(\sin(\delta t/4)/(\delta t/4)\bigr)^4$.

- $w\ge0$ is even, and $w(t)\le\min(1,(8X/|t|)^4)$.
- Its Fourier transform $\hat w(\xi)=\int w(t)e^{-i\xi t}dt$ is a positive multiple of the fourfold convolution of $\mathbf 1_{[-\delta/4,\delta/4]}$. So it is non-negative, even, continuous and supported in $[-\delta,\delta]$, and $\hat w(0)=\int w=16\pi X/3$.
- Let $\mathcal A:=\{1\}\cup\{p\le X\}$, let $\lambda_a\in\mathbb R$ $(a\in\mathcal A)$ with $\lambda_1=1$, and put $K(t):=|\sum_{a\in\mathcal A}\lambda_aa^{it}|^2=\sum_{a,b\in\mathcal A}\lambda_a\lambda_b(a/b)^{it}\ge0$.

*Separation.* If $u\ne v$ are positive integers with $\min(u,v)\le X$, then $|\log(u/v)|>\delta$. Either $\max(u,v)\ge2\min(u,v)$, or $\max(u,v)<2X$ and $\log(\max/\min)\ge(\max-\min)/\max>1/(2X)$.

*Orthogonality.* For every prime power $n$,

$$
\int\cos(t\log n)K(t)w(t)\,dt=\hat w(0)\,\lambda_n\mathbf 1[n\text{ is a prime}\le X],\qquad \int K(t)w(t)\,dt=\hat w(0)\sum_{a\in\mathcal A}\lambda_a^2.
$$

- Write $\cos(t\log n)(a/b)^{it}=\tfrac12\bigl(e^{it\log(an/b)}+e^{it\log(a/(bn))}\bigr)$. The integral of $e^{i\xi t}w(t)$ is $\hat w(\xi)$.
- The frequency $\log(a/(bn))$ vanishes only if $a=bn\ge2$. Then $a=p$ is a prime $\le X$, $b=1$ and $n=p$.
- Likewise $\log(an/b)=0$ only if $a=1$ and $n=b=p$. Both cannot hold at once, since then $n^2=1$.
- Every other frequency is $\log(u/v)$ with integers $u\ne v$ and $\min(u,v)\le\max(a,b)\le X$, so $\hat w$ vanishes there by the separation.
- The two diagonal cases contribute $\tfrac12\hat w(0)\lambda_p+\tfrac12\hat w(0)\lambda_p$. The second identity is the case $n=1$, where only $a=b$ survives.

*Evaluation.* For $Y\ge X$, $\tilde R^{(Y)}(s)=-\sum_{p\le Y}\sum_{k\ge1}k^{-1}c_pp^{-ks}$ converges absolutely and uniformly on the line.

- By Lemma 16(iii), $|\tilde R-\tilde R^{(Y)}|\le B_\sigma Y^{\theta-\sigma}(1+|t|)$ on the line, which tends to $0$.
- Since $\int(1+|t|)Kw\,dt<\infty$, letting $Y\to\infty$ and integrating $\tilde R^{(Y)}$ termwise gives

$$
\Phi:=\int\operatorname{Re}\tilde R(\sigma+it)\,K(t)w(t)\,dt=-\hat w(0)\sum_{p\le X}c_p\lambda_pp^{-\sigma}.
$$

*Tilting.* Choose $\lambda_p:=-c_pp^{-\sigma}V_X^{-1/2}$; we show below that $V_X>0$ for large $X$. Then $\sum_p\lambda_p^2=1$, $\Phi=\hat w(0)V_X^{1/2}$ and $\int Kw=2\hat w(0)$.

*Comparison.* Let $M_X:=\max\bigl(0,\sup_{|t|\le X^3}\operatorname{Re}\tilde R(\sigma+it)\bigr)$.

- Lemma 16(iii) with $Y=2$ gives $|\tilde R(\sigma+it)|\le C_0(1+|t|)$.
- By Cauchy–Schwarz, $K\le(1+\pi(X)^{1/2})^2\le4X$.
- As $Kw\ge0$,

$$
\hat w(0)V_X^{1/2}=\Phi\le M_X\int Kw+\int_{|t|>X^3}C_0(1+|t|)\cdot4X\Bigl(\frac{8X}{|t|}\Bigr)^4dt=2M_X\hat w(0)+O(1).
$$

- Dividing by $\hat w(0)\asymp X$ gives $M_X\ge\tfrac12V_X^{1/2}-O(1/X)$.

*Size of $V_X$.*

- For $p\in S$ we have $c_p=1-\pi_p\ge\tfrac12$ once $p$ is large.
- Since $\#(S\cap[1,X])\gg X^\alpha/\log X$, we get $V_X\ge\tfrac14X^{-2\sigma}\bigl(\#(S\cap[1,X])-O_\alpha(1)\bigr)\gg X^{\alpha-2\sigma}/\log X$.
- This exceeds every power of $\log X$.

Finally, $\operatorname{Re}\tilde R(\sigma+it)$ is even in $t$ (the coefficients are real) and bounded on compact sets. So the large values at $|t|\le X^3$ occur at $|t|\to\infty$ as $X\to\infty$, and the limsup is $+\infty$. $\square$

### Proof of Theorem 4

*(a)* Let $\mathcal N$ be a simply connected open neighbourhood of $(\alpha/2,\infty)$ inside $\operatorname{Re}s>\alpha/2$ on which $\zeta(s+\kappa)$ has no zeros. On $\mathcal N$, Lemmas 16(iii) and 17(a) give $F_S=e^{L+\tilde R}$, and

$$
F_S(\sigma)=\varsigma^{1/2}\hat H(\sigma)\qquad(\sigma\downarrow\alpha/2),\qquad \hat H:=h\,e^{\tilde R}.
$$

$\hat H$ is analytic and non-zero on a disc around $\alpha/2$, because $\tilde R$ is analytic on $\operatorname{Re}s>\theta$ and $\theta<\alpha/2$.

Suppose $N_S(x)=a_Sx+O(x^{\alpha/2-\eta})$.

- Then $\zeta F_S$ is analytic on $\operatorname{Re}s>\alpha/2-\eta$ except at $1$.
- So $F_S=\zeta F_S/\zeta$ is analytic near $\alpha/2$, because $\zeta(\alpha/2)\ne0$. It agrees with $e^{L+\tilde R}$ on $\mathcal N$ by uniqueness of continuation.
- Then $g:=F_S/\hat H$ is analytic near $\alpha/2$ and equals $\varsigma^{1/2}$ on $(\alpha/2,\alpha/2+\delta)$. This is impossible, as in the proof of Proposition 14.

No RH is used.

*(b)* Fix $\sigma_1\in(\max(\sigma_*,\theta),\alpha/2)$ and a sequence $\sigma_m\uparrow\alpha/2$ in $(\sigma_1,\alpha/2)$.

Suppose $N_S(x)=a_Sx+O(x^{\beta})$ with $\beta<\alpha/2$. Enlarging $\beta$, we may assume $\beta>\sigma_1$. Choose $\sigma_m\in(\beta,\alpha/2)$ and write $s=\sigma_m+it$.

- *Mellin.* $\zeta F_S(s)=a_Ss/(s-1)+s\int_1^\infty(N_S-a_Sx)x^{-s-1}dx$ is analytic on $\operatorname{Re}s>\beta$ except at $1$, and $|\zeta F_S(\sigma_m+it)|\ll|t|$.
- *Identification.* By Lemmas 16(iii) and 17(b), $\zeta\,e^{L+\tilde R}$ is analytic on $\{\operatorname{Re}s>\beta\}\setminus\{1\}$, which is connected. It agrees with $\zeta F_S$ for $\operatorname{Re}s>1$, hence on this whole set.
- *RH.* On $\operatorname{Re}s=\sigma_m<1/2$, $\zeta$ has no zeros and $|1/\zeta(\sigma_m+it)|\ll|t|^{\sigma_m-1/2+\varepsilon}$, by the functional equation and $1/\zeta(1-\sigma_m-it)\ll|t|^{\varepsilon}$ [10, Theorem 13.23]. So $|e^{L+\tilde R}(\sigma_m+it)|\ll|t|^{1/2+\sigma_m+\varepsilon}$.
- *Mean.* By Lemma 17(c), $|\operatorname{Re}L|\ll\log|t|$ on the line.
- Hence $\operatorname{Re}\tilde R(\sigma_m+it)\le C\log|t|$ for $|t|\ge2$, and $\operatorname{Re}\tilde R(\sigma_m+it)$ is bounded for $|t|\le2$ by continuity. This contradicts Lemma 18, since $\sigma_m>\theta$. $\square$

**Remark 19 (which sets are covered; size of the fluctuations).**

- *Coverage.* Randomness enters Theorem 4 only through Lemma 16(ii).
  - Every selection of distinct primes is covered. This includes adaptive rules, such as choosing in each block the prime that best cancels the running sum of $\tilde R$.
  - A rule that repeats primes is covered when its repeats up to $y$ number $O(y^\theta)$ with $\theta<\alpha/2$, and not otherwise. For example, "reuse the previous block's prime whenever allowed" repeats $\asymp y^\alpha/\log y$ primes up to $y$.
- *Height.* Replace $w$ by $(\sin(\delta t/2m)/(\delta t/2m))^{2m}$. Then the tail in the proof of Lemma 18 outside $|t|\le X^{1+\varepsilon}$ is $\ll_mX^{3+2\varepsilon-2m\varepsilon}$.
  - So for $m>(1+\varepsilon)/\varepsilon$, $\sup_{|t|\le T}\operatorname{Re}\tilde R(\sigma+it)\gg T^{(\alpha-2\sigma)/2-\varepsilon}$ for every $\theta$-regular $S$ with $\theta<\sigma$.
  - This lower bound has the order of the mean square that the Montgomery–Vaughan mean value theorem assigns to the primes $p\le T$, which are resolved at height $T$. Nothing chosen above $T$ can cancel it.
- *Random design (heuristic motivation; not used).* For the random design the typical fluctuation is expected to be larger. The block terms $\mathcal X_j(s):=\log(1-\mathfrak p_j^{-s})-\mathbb E\log(1-\mathfrak p_j^{-s})$ are independent. Their sum differs from $\tilde R$ only through the repeated primes, by $O(1)$ on lines $\operatorname{Re}s=\sigma>c_0$. Heuristically, under RH, $\operatorname{Var}\operatorname{Re}\sum_j\mathcal X_j(\sigma+it)\gg t^{(\alpha-2\sigma)/\alpha}/\log t$.
  - The blocks with $\nu_j\asymp t^{1/\alpha}$ spread their phases $t\log p$ over many periods.
  - Selberg's mean-square bound for primes in short intervals [18, 19] suggests that almost all of them do so evenly. Turning this into a proved variance bound needs a precise transfer from short intervals to mass-defined blocks, which we do not give.
  - A Lindeberg CLT [15, Ch. 3] would then give Gaussian fluctuations of this size.
  - The exploratory computation E6 in the supplement agrees.

**Remarks.**

- *What to expect at finite $x$ (heuristic).* For $S=S'\cup\{p\}$ with $p\notin S'$, we have $N_S(x)-a_Sx=(N_{S'}(x)-a_{S'}x)-(N_{S'}(x/p)-a_{S'}x/p)$. So products $d$ of deleted primes enter the error through the mean error at $x/d$.
  - Such a product contributes variance of order $1$ when $x/d$ moves by at least $1$ as each factor ranges over its stratum.
  - Counting such products of $k$ primes suggests variance exponents $k\alpha/(\alpha+k)$. These increase to $\alpha$, with very slow (Dickman-type) convergence.
  - In a pre-registered exploratory experiment at $\alpha=0.55$ (200 seeds, $x\le3\cdot10^6$), the variance of the stratified error grew with fitted exponent $0.45$ ($0.40$ when compensated). Independent deletion gave $0.49$ at a level about ten times higher. In this finite range the fitted exponents differ from the first-order prediction $\alpha/(1+\alpha)=0.355$. The retained uncertainty analysis is rough and not covariance-aware (the same seeds enter every window), so this is a descriptive discrepancy, not a formal rejection.
- *Mechanism.* In case (C) the barrier comes from growth along vertical lines, not from a real singularity. By Lemma 18, the deviation series cannot cancel below the mean square of its own coefficients at the primes up to $X$, at heights up to $X^3$, for every $\theta$-regular $S$ with $\theta<\sigma$. Two inputs suffice. Small discrepancy, $C_S(y)\ll y^\theta$ with $\theta<\sigma$, makes $\tilde R$ converge on the line. Unique factorisation separates the frequencies $\log n$ of $\tilde R$ from those of the kernel by more than $1/(2X)$.
  - What is proved is a necessary condition. Under RH, $N_S-a_Sx=O(x^\beta)$ forces $\log|F_S(\sigma+it)|\le(1/2+\sigma+\varepsilon)\log|t|+O(1)$ for $\beta<\sigma<1/2$.
  - Theorem 4 treats the models (U) and (C). Heuristically, the same argument applies to any density model for which an analogue of Lemma 17 holds.
  - A corner construction therefore needs a deletion set whose discrepancy from every such model is at least $x^{\alpha/2-o(1)}$, yet whose prime zeta function $\sum_{p\in S}p^{-s}$ cancels better than square-root on vertical lines left of $\alpha/2$.
  - Independent deletions with a power profile have the first property but not the second (Theorem 2, Proposition 14).

**Remark 20 (the construction of [3]).** The random deleted sets of [3, §5], used for [3, Theorem 1.3], are selections of distinct primes, but for a modified density.

- Their selected primes have distribution functions $F(x)-j+1$ on $\{j-1<F(x)<j\}$, where $dF=u^{\alpha-1}d(\pi+E)$.
- The error measure $E$ moves excess mass at block boundaries, so that no prime is selected twice. Its total variation on $[1,x]$ is $\ll x^{2\alpha-1}/\log x$ [3, (5.4)].
- So $S$ is a selection of distinct primes for the density $p^{-\kappa}(1+E\{p\})$. Relative to (U), Lemma 16(i) and partial summation against the variation of $E$ give $C_S(y)=O(1)+\sum_{p\le y}p^{-\kappa}E\{p\}\ll y^{\max(0,3\alpha-2)+\varepsilon}$.
- This exponent is less than $\alpha/2$ for $\alpha<4/5$, which covers both their ranges.

So Theorem 4(a) applies to **every** realisation: every system constructed in [3, §5] has integer exponent at least $\alpha/2$. Under RH, Theorem 4(b) gives the same for any variant with the compensated density.

A sharper analysis of that construction could therefore improve its threshold $2\alpha/(\alpha+2)$ at best to $\alpha/2$, which Theorem 1 attains with independent deletion.

## 11. Corollary 2 and what it shows

**Corollary 2.** For every $\beta>1/4$ there exist a Beurling generalized number system and $a>0$ with $N(x)=ax+O(x^\beta)$ and $\psi(x)-x\ne O(x^{1/2+\delta})$ for some $\delta>0$.

*Proof.* There are two cases.

- *RH fails.* Take $(\mathbb P,\mathbb N)$. Then $N(x)=x+O(1)$ and $\psi(x)-x=\Omega(x^{\Theta-\varepsilon})$ for every $\varepsilon>0$, where $\Theta=\sup\operatorname{Re}\rho>1/2$ (Landau; see [10, Ch. 15]). Take any $\delta<\Theta-1/2$.
- *RH holds.* Choose $\alpha\in(1/2,\min(2/3,2\beta))$. By Proposition 9 and Lemma 10, almost surely $N_S(x)=a_Sx+O(x^{\beta})$ and $\psi_{\mathbb P\setminus S}(x)-x\sim-x^\alpha/\alpha$. Take $\delta<\alpha-1/2$. $\square$

The argument is non-constructive, and its first case is trivial. Its substance is the implication "RH $\Rightarrow$ such systems exist", supplied by the construction of Theorem 1 (Proposition 9 and Lemma 10). It refutes the statement

> $\Phi_\beta$: every Beurling system with $N(x)=ax+O(x^\beta)$ has $\psi(x)=x+O(x^{1/2+\varepsilon})$ for all $\varepsilon>0$

for every $\beta>1/4$. $\Phi_\beta$ would imply RH, and refuting it rules out any proof of RH that deduces the square-root law from integer regularity of strength $x^\beta$ by an argument valid for the whole class of Beurling systems. It says nothing about arguments that use further structure of $\mathbb N$.

Previously, $\Phi_\beta$ was refuted for $\beta>1/2$ unconditionally [3, Theorem 1.1], and for $\beta>2/5$ by the same dichotomy applied to [3, Theorem 1.3]. The new range is $1/4<\beta\le2/5$. Whether $\Phi_\beta$ fails for small $\beta>0$ is open.

Our construction cannot decide this below $\beta=1/4$:

- When RH holds, $\mathbb P\setminus S$ violates the square-root law only if $\alpha>1/2$, since the deleted primes contribute about $cx^\alpha/\alpha$ to $\psi$.
- By Theorem 2, Proposition 14 and Remark 15, its integer exponent is then at least $\alpha/2>1/4$.

Theorem 4 shows that stratified deletion cannot decide it either.

## 12. Numerical illustration (exploratory)

These finite computations illustrate the mechanism. They are not evidence for any theorem and say nothing about RH. The predictions were written down before the runs (supplement, `notebook/`), and both programs agree exactly with brute force at small sizes.

**Table 1.** Fitted growth exponents of dyadic maxima up to $10^8$. Each slope is a least-squares fit of $\log\max$ against $\log y$ over the blocks $[2^j,2^{j+1})$ with $j\ge16$.

| quantity | $\alpha$ | observed slope | heuristic | proved exponent (RH) | proved exponent of the construction in [3], for comparison |
|---|---|---|---|---|---|
| $\max\lvert E_0\rvert$ | 0.60 | 0.11 | $\alpha-\tfrac12=0.10$ (mean-square) | $\theta_*=0.30$ | — |
| $\max\lvert E_0\rvert$ | 0.55 | 0.08 | $0.05$ (mean-square) | $0.275$ | — |
| $\max\lvert N_S-a_Sx\rvert$, seed 1 | 0.60 | 0.27 | $\alpha/2=0.30$ | $0.30$ | $0.462$ |
| seed 2 | 0.60 | 0.33 | $0.30$ | $0.30$ | $0.462$ |
| seed 3 | 0.60 | 0.30 | $0.30$ | $0.30$ | $0.462$ |

**$E_0$.** The deterministic error is small: $\max|E_0|\le5.8$ up to $10^8$ (the largest block maximum is $5.79$, at $\alpha=0.6$). The heuristic $y^{\alpha-1/2}$ comes from the poles of $\zeta(s)/\zeta(s+\kappa)$ on $\operatorname{Re}s=\alpha-1/2$. It is only a mean-square heuristic, because the explicit formula does not converge absolutely there. The observed slopes, 0.08–0.11, indicate a small exponent but do not clearly confirm $\alpha-1/2$ at $\alpha=0.55$.

**$N_S$.** The random integer error grows like $x^{\alpha/2}$, consistent with Corollary 1.

*The density $a_S$ is an estimate.*

- The programs compute $\prod_{p\in S,\,p\le X}(1-1/p)$ in floating point. They replace the factor from primes $p>X$ by an approximation of its mean, obtained from a prime-density integral.
- The random part of that factor has standard deviation about $X^{(\alpha-2)/2}/\sqrt{(2-\alpha)\log X}$ in $\log a_S$. This is $4.9\cdot10^{-7}$ at $\alpha=0.6$, $X=10^8$.
- It adds an error with standard deviation about $16$ to $a_Sx$ at $x=X$, and proportionally less at smaller $x$. In the last dyadic block ($j=26$) the plotted maxima are $124.5$, $207.8$ and $172.1$ for seeds 1–3. The largest maximum in the last two blocks, $306.9$, is in block $j=25$ (seed 2).
- So, as an approximate one-standard-deviation scale, the last block carries an uncertainty of about 8–13% of its plotted maxima ($16$ against $124.5$–$207.8$). The block before it carries less, since the standard deviation scales with $x$.
- The variance formula applies to independent deletion. For the independent-deletion runs at $\alpha=0.55$ (E4) the corresponding standard deviation is about $31a_S$ at $x=X$, i.e. 7–23. We do not claim the same standard deviation for the stratified sets of E4.
- We have not quantified the effect on the fitted slopes. They are exploratory and should be read with this uncertainty. At $\alpha=0.55$, the independent-deletion runs of `e4_corner.py` (seeds 1 and 2) give slopes $0.27$ and $0.25$, against $\alpha/2=0.275$.

## 13. Limitations and open problems

- **RH.** Theorem 1, Theorem 3, Proposition 9 and Corollary 1 assume RH. This is inherent to perturbations of $(\mathbb P,\mathbb N)$: unconditionally, not even $\psi(x)-x\ll x^{1-\delta}$ is known. Theorem 2, Proposition 14 and Theorem 4(a) are unconditional; Theorem 4(b) assumes RH. Corollary 2 is unconditional, but its content rests on the construction of Theorem 1 (§11).
- **The range $\alpha>2/3$.** Here $\theta_*(\alpha)>\alpha/2$. The loss has two sources:
  - Proposition 6, where the choice of $H$ balances the twisted-sum bound of Lemma 4 against the term $V(0)/H$; both equal $y^{1/3}D^{1/3-\kappa}$;
  - the crude treatment of the high part in Theorem 3.

  Any improvement there transfers directly to Theorem 1.
- **The corner $\alpha>1/2$, $\beta<\alpha/2$.** Theorem 2, Proposition 14, Remark 15 and Theorem 4 rule it out for:
  - independent deletion with a power profile $\min(1,cp^{\alpha-1})$;
  - every deletion set within $O(y^\theta)$, $\theta<\alpha/2$, of the target count, in particular one-prime-per-block deletion by any rule without repeats: with the plain density unconditionally, and with the compensated density under RH.

  It remains open for other deletion sets, in particular for sets far, in discrepancy, from every tame density model.
  - *What a construction would need.* Heuristically (see the remarks after Theorem 4), such a deletion set, whose prime zeta function $\sum_{p\in S}p^{-s}$ nevertheless cancels better than square-root on vertical lines left of $\alpha/2$. By Lemma 18 no set of small discrepancy from (U) or (C) does this.
  - *Numerics.* Exploratory runs at $\alpha=0.55$ up to $10^8$ used two seeds per design. For the stratified designs, the error maxima in the last dyadic block were 25–45% smaller than for independent deletion in raw terms, and 39–67% smaller after division by $a_S$. The normalisation matters because $a_S$ ranged from $0.24$ to $0.75$ across runs, depending mostly on which small primes were deleted. The fitted slopes (about $0.22$) lie below $\alpha/2=0.275$. This is consistent with the slow approach described in the remarks after Theorem 4, not a counterexample to it.
  - *Compensation.* A "Riemann-type" compensated density $p^{\alpha-1}-\tfrac12p^{\alpha/2-1}$ removes the $k=2$ log-singularity from the mean. It did not change the fitted slopes at this range: $0.225$ and $0.224$ against $0.217$ and $0.229$ for stratified designs.
  - *The deterministic mean.* For any design, the mean contains Möbius-signed sawtooth sums over small $d$. Theorem 3 bounds these only trivially, by $y^{\alpha/2}$. For the analogous sums for squarefree numbers under RH, the best known exponent is $11/35$ [20], against the heuristic $1/4$.
- **Constructiveness.** Corollary 2 is non-constructive.

## 14. Reproducibility

The supplement contains:

- `e1_mean_system.py`: segmented sieve for $E_0$;
- `e2_random_sift.py`: random sifted systems, NumPy seeds 1–3;
- `e3_lemma4_check.py`: comparison of $|U(h)|$ with the Lemma 4 envelope;
- `e4_corner.py`: comparison of deletion designs, and `e4_summary.py`, which computes the raw and $a_S$-normalised ratios quoted in §13;
- `e5_variance.py`: the variance experiment of §§10 and 13, with 200 seeds per design;
- `e6_vertical_variance.py`: exact variance of the random part of $\log F_S$ on vertical lines for the compensated stratified design (an exploratory check of the variance growth sketched in Remark 19);
- `check_exponents.py`: exact rational checks for Lemma 1 and for the comparison with [3, Theorem 1.3];
- `check_thm3_exponents.py`: exact rational checks of the exponent bookkeeping in Proposition 6 and Theorem 3, and of the properties of $\theta_*$ used in §§1 and 8;
- `check_sections_7_9_10_11.py`: exact rational checks of the elementary inequalities used in §§7, 9, 10 and 11;
- `make_figure.py`, which produces Figure 1;
- the raw dyadic maxima, and the pre-registration notes with results.

Most runs take under a minute on 4 cores with Python 3 and NumPy (matplotlib for the figure). E5 takes about four minutes. No proof depends on a computation.

## References

[1] T. W. Hilberdink. Well-behaved Beurling primes and integers. *J. Number Theory* 112 (2005), no. 2, 332–344. https://doi.org/10.1016/j.jnt.2004.09.001

[2] J. E. Littlewood. Sur la distribution des nombres premiers. *C. R. Acad. Sci. Paris* 158 (1914), 1869–1872.

[3] F. Broucke, G. Debruyne, Sz. Gy. Révész. Some examples of well-behaved Beurling number systems. *Trans. Amer. Math. Soc.* 378 (2025), no. 1, 477–501. https://doi.org/10.1090/tran/9274 ; arXiv:2309.01567

[4] H. G. Diamond, W.-B. Zhang. *Beurling Generalized Numbers.* Math. Surveys Monogr. 213, American Mathematical Society, 2016.

[5] A. Beurling. Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. *Acta Math.* 68 (1937), 255–291.

[6] H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer. Beurling primes with large oscillation. *Math. Ann.* 334 (2006), 1–36. https://doi.org/10.1007/s00208-005-0638-2

[7] W.-B. Zhang. Beurling primes with RH and Beurling primes with large oscillation. *Math. Ann.* 337 (2007), no. 3, 671–704. https://doi.org/10.1007/s00208-006-0051-5

[8] F. Broucke, J. Vindas. A new generalized prime random approximation procedure and some of its applications. *Math. Z.* 307 (2024). https://doi.org/10.1007/s00209-024-03526-4 ; arXiv:2102.08478

[9] F. Broucke, G. Debruyne, J. Vindas. Beurling integers with RH and large oscillation. *Adv. Math.* 370 (2020), 107240. arXiv:2004.11501

[10] H. L. Montgomery, R. C. Vaughan. *Multiplicative Number Theory I. Classical Theory.* Cambridge Stud. Adv. Math. 97, Cambridge University Press, 2007.

[11] E. C. Titchmarsh. *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown. Oxford University Press, 1986.

[12] S. W. Graham, G. Kolesnik. *Van der Corput's Method of Exponential Sums.* London Math. Soc. Lecture Note Ser. 126, Cambridge University Press, 1991.

[13] J. D. Vaaler. Some extremal functions in Fourier analysis. *Bull. Amer. Math. Soc. (N.S.)* 12 (1985), no. 2, 183–216.

[14] S. Boucheron, G. Lugosi, P. Massart. *Concentration Inequalities.* Oxford University Press, 2013.

[15] R. Durrett. *Probability: Theory and Examples*, 5th ed. Cambridge University Press, 2019.

[16] H. P. Rosenthal. On the subspaces of $L^p$ $(p>2)$ spanned by sequences of independent random variables. *Israel J. Math.* 8 (1970), 273–303.

[17] K. Soundararajan. Extreme values of zeta and $L$-functions. *Math. Ann.* 342 (2008), no. 2, 467–486.

[18] A. Selberg. On the normal density of primes in small intervals, and the difference between consecutive primes. *Arch. Math. Naturvid.* 47 (1943).

[19] M. Cully-Hugill, A. W. Dudek. An explicit mean-value estimate for the prime number theorem in intervals. *J. Aust. Math. Soc.* 117 (2024), no. 1, 1–15. https://doi.org/10.1017/S1446788723000113

[20] H.-Q. Liu. On the distribution of squarefree numbers. *J. Number Theory* 159 (2016), 202–222. https://doi.org/10.1016/j.jnt.2015.07.013

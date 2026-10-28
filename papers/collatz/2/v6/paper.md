# How fast does the Syracuse characteristic function decay? Exact computation, a renewal identity and a certified conditional bound

## 1. Problem and contribution

Tao's theorem that almost all Collatz orbits attain almost bounded values [1] rests on one Fourier estimate. Let $a_1,a_2,\ldots$ be i.i.d. geometric random variables with $\mathbb{P}(a=k)=2^{-k}$ for $k\geq 1$, let $s_m=a_1+\cdots+a_m$, and define the *Syracuse random variable*

$$
\mathrm{Syrac}_n \;=\; \sum_{m=1}^{n} 3^{m-1}\,2^{-s_m} \pmod{3^n},
$$

with characteristic function $\chi_n(\xi)=\mathbb{E}\, e\!\left(\xi\,\mathrm{Syrac}_n/3^n\right)$, where $e(x)=e^{2\pi i x}$. (Tao indexes the digits in the opposite order; because the $a_i$ are i.i.d., the two laws coincide.) Tao proves $|\chi_n(\xi)|\ll_A n^{-A}$ for every $A$, uniformly in $\xi$ coprime to $3$ [1, Prop. 1.17]. By a remark in [1], this estimate is equivalent to his fine-scale mixing proposition, since $|\chi_n(\xi)|\le\mathrm{Osc}_{n-1,n}$ for $3\nmid\xi$. Tao also remarks that a random-map heuristic predicts mixing at rate $\exp(-cm)$, which he does not attempt to establish. Neither the size of $c$ nor the frequencies and mechanism that set it appear to have been studied.

This paper studies the true size of

$$
M_n \;=\; \max_{3\nmid \xi}\,|\chi_n(\xi)| .
$$

We do not claim any improvement of Tao's Collatz theorem. In his argument the Fourier input already costs less than any power of $\log x$, and the density exponent is limited by archimedean steps (§6, Scope). The interest of $M_n$ is intrinsic: it measures how fast the 3-adic Syracuse law mixes, and the answer differs sharply from the random-map prediction.

Since $2$ is a primitive root modulo $3^n$, every unit is a power $2^j$ (with $-1=2^{3^{n-1}}$), and $\chi_n(-\xi)=\overline{\chi_n(\xi)}$. We write extremal frequencies as $\pm2^j$ with $0\le j<3^{n-1}$. The contributions are:

1. **Exact values.** We compute $\chi_n$ exactly on all $2\cdot 3^{n-1}$ units for $n\le 18$ with an $O(3^n)$ recursion. For individual frequencies we use a new $O(n^2)$ dynamic program, which evaluates $\chi_n(2^ju)$ exactly for $n$ up to $2000$. These are deterministic evaluations of a truncated sum. The truncation is controlled in absolute terms only (§3.4), and float64 arithmetic agrees with a ball-arithmetic recomputation of the same truncated sums for $\ell\le800$ to $5\times10^{-10}$. We call such values exact in this sense. For $n\le18$ the maximum over all units is attained at $\xi=\pm2^{j}$ with $j=\lambda n-O(1)$, $\lambda=\log_2 3$. An exhaustive branch-and-bound over the 3-adic digits of $\xi$ (§4.2; float64, with rigorous truncation control) extends this to every $n\le70$ and to $n=75,80$: the maximiser is unique up to sign, and every unit outside the family $\pm2^j$ is below $0.999\,M_n$. Along this family the maximum $M^*_n$ falls from $1.1\times10^{-2}$ ($n=18$) to $2.2\times10^{-52}$ ($n=2000$). Free fits give exponential rate $\kappa=0.0552$–$0.0553$. With $\kappa=I$ fixed, the effective polynomial exponent rises from $1.0$ to $1.35$ as $n$ grows from $200$ to $2000$. A tilted recursion run to $n=3\times10^5$, matched by a zero-parameter limit formula due to cassian_mahler [9], shows that this drift is pre-asymptotic and that the exponent is $3/2$ (§4.7, numerical).
2. **A renewal identity (Theorem 1).** For all $j\ge0$ and $u$ coprime to $3$, $\chi_n(2^j u)$ equals an explicitly computable "cold-walk" expectation plus a sum $\sum_\ell w_\ell(j,u)\,\chi_\ell(u)$. The term for $\ell$ is weighted by the probability that the partial sums first exceed $j$ at step $n-\ell+1$.
3. **A conditional transfer theorem (Theorem 2).** If $|\chi_\ell(1)|\le B\rho^\ell$ for some $\rho<\lambda-1\approx 0.585$, then $|\chi_n(2^j)|\le C\,e^{-I n+\theta^*(j-\lambda n)}$, where
$$
I=\lambda\bigl(\ln 2-H(1/\lambda)\bigr)\approx 0.05498,\qquad \theta^*=\ln\frac{\lambda}{2(\lambda-1)}\approx 0.3036,
$$
and $H$ is the natural-log binary entropy. The rate $I$ is the Cramér cost for a walk with mean step $2$ to stay below the neutral-growth line $s_m\le\lambda m$.
4. **Certified verification of the hypothesis to $\ell=1000$ (Corollary 3).** Exact values give $|\chi_\ell(1)|\approx e^{-0.565\ell}$, i.e. $\rho_{\rm eff}=0.568$, inside the threshold $\lambda-1=0.585$. Explicitly, $|\chi_\ell(1)|\le 5.70\cdot 0.58^\ell$ for all $\ell\le1000$. This bound is *certified* by ball arithmetic (Corollary 3). So for $n\le1000$ the conclusion of Theorem 2 holds rigorously, with explicit constant $C=39$ for all $j$ simultaneously; it is nontrivial for $67\le n\le1000$ and $j\lesssim1.7n$. Certified lower bounds at the extremal $j^*$ show that it is sharp up to a factor of at most $1.6\times10^4$ at $n=100,\dots,1000$. The margin against the threshold is small: $\ln((\lambda-1)/0.568)=0.029$ nats per level. This explains the long pre-asymptotic regime, in which effective exponents fitted at $n\le62$ are misleading.
5. **Cross-checks.** Exact-integer Monte Carlo ($n\le62$) and a hybrid renewal model (exact weights plus random phases) agree with the exact values to within sampling error and $10\%$ respectively.
6. **Conjecture C1** (§5): $\frac1n\log M_n\to -I$. A stronger form, C1$^+$, asserts $M_n=e^{-In+O(\log n)}$. Empirically, $n\,e^{In}M^*_n$ stays at $0.32\pm0.01$ for $180\le n\le800$ and then decreases to $0.25$ at $n=2000$. So the polynomial correction is not yet determined. The extremal frequencies are $2^{\lambda n-6.5+O(1)}$. These frequencies correspond to the neutral-growth walks $2^{s_m}\approx3^m$, which also govern heuristic models of Collatz cycles. The rate $I$ is ten times smaller than the rate $\tfrac12\ln 3$ of a random-map model that keeps the geometric input weights (§5).

We also explain (Section 6) why renewal-type arguments naturally output decay of the form $n^{-A}$, as in Tao's theorem, rather than an exponential rate: they give $M_n\lesssim c' M_{\approx 0.21n}$.

## 2. Related work and distinction

Tao [1] introduced $\mathrm{Syrac}_n$ and proved the superpolynomial bound $|\chi_n(\xi)|\ll_A n^{-A}$ for every fixed $A$. His proof pairs consecutive digits, which produces factors $|\cos|$ that are bounded away from $1$ whenever a phase $\{\xi 3^{m}2^{-s}/3^n\}$ lies away from $0$. He then shows that the set of "black" positions, where the phase is near zero, is sparse in a renewal sense. Several ingredients used here are already in [1]: the distributional recursion for $\mathrm{Syrac}_n$ [1, Lemma 1.12], which underlies §3.1; the suggestion of exponential mixing [1, Remark 1.15]; the relation between $\chi_n$ and $\mathrm{Osc}$ [1, Remark 1.18]; and a stopping-time (renewal) decomposition of the geometric walk [1, Section 6]. Theorem 1 specialises that decomposition to the first crossing of a fixed level $j$, which isolates a fresh Syracuse variable at the remaining level. The present paper keeps Tao's object and asks a different question: what is the *true* size of $\max|\chi_n|$, which frequencies attain it, and what mechanism sets its rate? An arXiv search (October 2026) found no previous work that computes $M_n$, identifies the extremal frequencies, or proposes an exponential rate with an explicit constant. Tao's method has been extended to generalized maps $x\mapsto(qx+r)/p$ [6]. Siegel and O'Dwyer [7] state an extension of almost-boundedness to Collatz-type maps on rings of integers of number fields, by archimedean methods that, they report, need no Fourier decay estimate. We could not verify their proof of the passage-location comparison as written: the final step bounds $\mathbb P(\mathrm{Pass}_x(\mathcal N_y)\in S)\ll x^{-(\alpha-1)c}$ for every $S$, which for $S$ the whole ball contradicts their own passage-time estimate, and the preceding transference step replaces a sum by one that is termwise smaller by a factor $((p-1)/p)^{p(L-m_x)}$. We therefore do not use [7] as support. Our audit of Tao's argument (§6, Scope) stands on its own. Rees [8] formulates 2-adic equidistribution conjectures for push-forwards of geometric distributions; these are a different (2-adic, not 3-adic) object.

Large-deviation constants for the geometric walk $s_m$ are classical (Cramér; see [4]). The same "neutral-growth" slope $s_m\approx\lambda m$ appears in heuristic and stochastic models of Collatz trajectories and cycles [2,3]. Here it appears for a different reason: it is the slope along which the phases of the cold walk stay real numbers in $[0,1)$ rather than equidistributed residues. Renewal arguments for Fourier decay of self-similar and stationary measures [5] are the closest methodological analogue. There, renewal theory gives polynomial or logarithmic rates unless extra Diophantine input is available, which matches the dichotomy we find (Section 6).

## 3. Methods and proofs

### 3.1 Recursion and exact algorithm

Write $\psi_n(t)=\chi_n(2^t)$ for $t\in\mathbb{Z}/N_n$, with $N_n=2\cdot3^{n-1}$. Peel off the first digit: $\mathrm{Syrac}_n\overset{d}{=}2^{-a}(1+3Y')$, where $Y'\sim\mathrm{Syrac}_{n-1}$ is independent of $a$. Since $e(2^{t-a}\cdot 3Y'/3^n)=e(2^{t-a}Y'/3^{n-1})$, this gives

$$
\psi_n(t)=\sum_{a\ge1}2^{-a}\,e\!\left(\frac{2^{t-a}}{3^n}\right)\psi_{n-1}(t-a),\qquad \psi_0\equiv1 .
$$

The operator $Kf(t)=\sum_{a\ge1}2^{-a}f(t-a)$ on $\mathbb{Z}/N$ satisfies $Kf(t)=\tfrac12\bigl(f(t-1)+Kf(t-1)\bigr)$. It can therefore be applied in $O(N)$ operations: one closed-form initial value from the geometric series, then a linear sweep. All units at level $n$ thus cost $O(3^n)$, and all levels up to $n$ cost $O(3^n)$ in total. We ran this in double precision for $n\le18$ ($N_{18}\approx2.6\times10^8$). We checked it against an independent computation of the exact laws for $n\le 9$; the agreement was $5\times10^{-10}$, limited by the printed precision of the profile.

### 3.2 The renewal identity

Fix $j\ge0$ and $u$ coprime to $3$. Let $\tau=\min\{m\ge1:\ s_m>j\}$; if no $m\le n$ qualifies, $\tau\geq n+1$. Write $\ell=n-\tau+1$, which is $\leq 0$ when $\tau>n$, and set $\chi_\ell\equiv1$ for $\ell\le0$.

**Theorem 1 (renewal identity).** For every $n\ge1$, $j\ge0$ and $3\nmid u$,
$$
\chi_n(2^j u)=\mathbb{E}\Bigl[e\Bigl(u\sum_{m<\min(\tau,n+1)}\frac{2^{\,j-s_m}}{3^{\,n-m+1}}\Bigr)\,\chi_{n-\tau+1}(u)\Bigr]
=\mathcal{M}_n(j,u)+\sum_{\ell=1}^{n}W_\ell(j,u)\,\chi_\ell(u),
$$
where $\mathcal{M}_n(j,u)=\mathbb{E}\bigl[e(u\sum_{m\le n}2^{j-s_m}/3^{n-m+1});\ \tau>n\bigr]$ and $W_\ell(j,u)=\mathbb{E}\bigl[e(u\sum_{m<\tau}2^{j-s_m}/3^{n-m+1});\ \tau=n-\ell+1\bigr]$. In particular,
$$
|\mathcal{M}_n(j,u)|\le\mathbb{P}(s_n\le j),\qquad |W_\ell(j,u)|\le\mathbb{P}(\tau=n-\ell+1)\le\mathbb{P}(s_{n-\ell}\le j).
$$

*Proof.* In forward indexing, $\chi_n(\xi)=\mathbb{E}\,e\bigl(\sum_{m=1}^n\xi\,2^{-s_m}/3^{n-m+1}\bigr)$; here $2^{-s}$ means the inverse modulo $3^{n-m+1}$, which is legitimate because $3^{m-1}$ divides the $m$-th term. Put $\xi=2^ju$. For $m<\tau$ we have $s_m\le j$, so the $m$-th term is the rational number $u2^{j-s_m}/3^{n-m+1}$ with an integer numerator. Now condition on $\mathcal{F}_{\tau-1}=\sigma(a_1,\dots,a_{\tau-1})$ and on the event $\{\tau=m\}=\{s_{m-1}\le j<s_m\}$. By memorylessness, the overshoot $b_1=s_\tau-j$ is again $\mathrm{Geom}(1/2)$ on $\{1,2,\dots\}$ and is independent of $\mathcal{F}_{\tau-1}$. The digits $a_{\tau+1},a_{\tau+2},\ldots$ are i.i.d. and independent of both. With $b_i=s_{\tau+i-1}-j$, the terms $m\ge\tau$ add up to
$$
u\sum_{i=1}^{\ell}\frac{2^{-b_i}}{3^{\ell-i+1}}\ \overset{d}{=}\ \frac{u\,\mathrm{Syrac}_\ell}{3^\ell}\quad(\ell=n-\tau+1).
$$
Its conditional expectation is $\chi_\ell(u)$. The bounds follow from $|e(\cdot)|=1$, $|\chi_\ell|\le 1$ and $\{\tau=n-\ell+1\}\subseteq\{s_{n-\ell}\le j\}$. $\square$

The identity was verified exactly (error $\le 10^{-16}$) for $(n,j,u)\in\{(8,5,1),(8,10,5),(9,7,-7),(9,12,11),(7,3,25),(9,14,1)\}$ against the exact laws (supplement: `check_general_renewal.py`).

**Computing the weights.** For $u=1$, $\mathcal{M}_n$ and all $W_\ell$ come from one forward pass over the cold region $\{(m,s):s\le j\}$. Let $V_m(s)=\mathbb{E}[\,e(\cdot)\,;\ s_1,\ldots,s_m\le j,\ s_m=s]$. Then
$$
W_{n-m+1}=\sum_{s\le j}V_{m-1}(s)\,2^{-(j-s)},\qquad V_m(s)=e\!\left(\frac{2^{j-s}\bmod 3^{n-m+1}}{3^{n-m+1}}\right)\sum_{a\geq 1}2^{-a}V_{m-1}(s-a).
$$
The cost is $O(nj)$ big-integer modular powers, which is feasible for $n\le 500$ at $j\approx\lambda n$. Combined with exact $\chi_\ell(1)$ for $\ell\le18$, Theorem 1 reproduces the exact $\chi_n(2^j)$ for $n\le18$ to $10^{-11}$.

### 3.3 Conditional transfer theorem

Let $\varphi(\theta)=\mathbb{E}e^{-\theta a}=1/(2e^\theta-1)$. Chernoff's inequality gives $\mathbb{P}(s_m\le j)\le e^{\theta j}\varphi(\theta)^m$ for every $\theta>0$. Choose
$$
e^{\theta^*}=\frac{\lambda}{2(\lambda-1)},\qquad\text{so that}\qquad \varphi(\theta^*)=\lambda-1\approx0.58496 .
$$

**Theorem 2.** Suppose $|\chi_\ell(1)|\le B\rho^\ell$ for all $\ell\ge1$, where $\rho<\lambda-1$. Then for all $n\ge1$ and $j\ge0$,
$$
|\chi_n(2^j)|\ \le\ \Bigl(1+\frac{Bq}{1-q}\Bigr)\,e^{\theta^* j}(\lambda-1)^n,\qquad q=\frac{\rho}{\lambda-1}.
$$
Writing $j=\lambda n+d$, the right-hand side is $C_{B,q}\,\exp(-In+\theta^*d)$ with $I=\lambda(\ln2-H(1/\lambda))=0.054980$. Hence the bound is exponentially small whenever $j\le(\lambda+I/\theta^*)n-\omega(1)\approx1.766\,n$.

*Proof.* By Theorem 1,
$$
|\chi_n(2^j)|\le\mathbb{P}(s_n\le j)+\sum_{\ell\ge1}B\rho^\ell\,\mathbb{P}(s_{n-\ell}\le j)\le e^{\theta^*j}\Bigl[(\lambda-1)^n+B\sum_{\ell\ge1}\rho^\ell(\lambda-1)^{n-\ell}\Bigr].
$$
For the exponent, use $\lambda H(1/\lambda)=\lambda\ln\lambda-(\lambda-1)\ln(\lambda-1)$, which gives $\theta^*\lambda+\ln(\lambda-1)=\lambda\ln\lambda-\lambda\ln2-(\lambda-1)\ln(\lambda-1)=-I$. $\square$

*Remarks.* (i) $I$ is exactly the Cramér rate of $\mathbb{P}(s_n\le\lambda n)$. With $\theta^*$ optimal at slope $\lambda$, the main term alone is at most $e^{-In}$. (ii) The same argument with $\chi_\ell(u)$ in place of $\chi_\ell(1)$ treats the frequencies $2^ju$ for any fixed $u$. (iii) The hypothesis is the crux. The renewal identity at $j=0$ is trivial ($\tau=1$), so Theorem 1 cannot bootstrap it. Under square-root cancellation, $|\chi_\ell(1)|\approx3^{-\ell/2}=0.5774^\ell$ and $q\approx 0.987$: the hypothesis would hold, but only by a margin of $0.013$ nats per level. Exact data show slightly more cancellation, since typical units decay like $e^{-0.564\ell}$ (§4.3), and the margin is then about $0.028$. Section 4.3 certifies the hypothesis rigorously for $\ell\le1000$.

**Corollary 3 (computer-assisted).** For all $1\le n\le1000$ and all $j\ge0$,
$$
|\chi_n(2^j)|\ \le\ 39\,e^{\theta^*j}(\lambda-1)^n;\qquad\text{in particular}\qquad |\chi_n(2^j)|\le 39\,e^{-In+\theta^*(j-\lambda n)}.
$$
*Proof.* In the proof of Theorem 2, $\chi_\ell(1)$ enters only for $1\le\ell\le n$. Section 4.3 certifies $|\chi_\ell(1)|\le B\rho^\ell$ for $1\le\ell\le1000$ with $\rho=0.58$ and $B=5.6961$, using rigorous ball arithmetic and an exact bound on the truncated tail. The proof of Theorem 2 gives the constant $1+\sum_{\ell=1}^{n}|\chi_\ell(1)|(\lambda-1)^{-\ell}$. Summing the certified upper bounds for $\ell\le1000$ (all terms are nonnegative) gives $1+\sum_{\ell\le1000}|\chi_\ell(1)|(\lambda-1)^{-\ell}\le38.9468$ (`cert_constant.py`, rounded up). (The uniform bound $B\rho^\ell$ alone gives $q=0.58/(\lambda-1)=0.99152\ldots$ and $1+Bq/(1-q)\le666.8$.) $\square$

**Remark 3.1 (exact weights and a reflection horizon; imported from cassian_mahler [9] and r/collatz post 21).** The two identities below, and their application to the certified bounds of §3.3 and Table 2, are already in [9, Theorem 3.1 and Tables 2–3]; we incorporate them here for completeness. The conditional nonvanishing certificate of §4.7 is a separate addition. The partial sums $s_1<s_2<\cdots$ form a Bernoulli$(1/2)$ subset of $\{1,2,\ldots\}$, and $\tau=n-\ell+1$ means that exactly $n-\ell$ of them lie in $[1,j]$. So the weight bound of Theorem 1 sharpens to
$$|W_\ell(j,u)|\le\mathbb P(\tau=n-\ell+1)=\binom{j}{n-\ell}2^{-j}.$$
- *Sharper certified bounds.* The resulting upper bound, $\mathbb P(s_n\le j)+\sum_{\ell\le n}\binom{j}{n-\ell}2^{-j}\,\overline{|\chi_\ell(1)|}$ with certified $\overline{|\chi_\ell(1)|}$, is within a factor $22.4$–$139.9$ of the certified lower bounds at the six points of Table 2. That is $62$–$111$ times tighter than Corollary 3.
- *Reflection horizon.* For $0\le j<2n$, Pascal symmetry gives $\sum_{\ell>2n-j-1}\binom{j}{n-\ell}2^{-j}=\mathbb P(s_n\le j)$. Bounding those $\chi_\ell$ trivially,
$$|\chi_n(2^ju)|\le2\,\mathbb P(s_n\le j)+2^{-j}\sum_{\ell=1}^{2n-j-1}\binom{j}{n-\ell}|\chi_\ell(u)|.$$
With the certificate for $\ell\le1000$ and the Chernoff bound of Theorem 2, the bound of Corollary 3 with $40$ in place of $39$ holds for every pair with $2n-j-1\le1000$. This range contains the extremal window $j\ge\lfloor\lambda n\rfloor-7$ for all $n\le2395$, and so all of Table 2. Smaller $j$ at $n>1000$ are not covered.

Both identities are checked exactly (`binomial_ub.py`, `check_reflection_horizon.py`: weights for $n\le12$, $j<3n$; the horizon identity holds exactly for $j<2n$).

Corollary 3 bounds the coefficients along the family $\xi=2^j$ only. It is not an upper bound for the global maximum $M_n$, since it says nothing about other units. This is nontrivial (below $1$) when $In-\theta^*(j-\lambda n)>\ln39=3.66$, for example for $j\le\lambda n$ and $n\ge67$. For other units see §5.

### 3.4 Deterministic evaluation at a single frequency in polynomial time

The recursion in §3.1 costs $O(3^n)$ because it produces all units at once. A single coefficient is much cheaper. By the forward formula,
$$
\chi_n(2^ju)=\mathbb{E}\prod_{m=1}^{n}e\!\left(\frac{u\,2^{\,j-s_m}\bmod 3^{n-m+1}}{3^{n-m+1}}\right),
$$
where negative exponents are inverses modulo $3^{n-m+1}$. Each factor depends only on $(m,s_m)$, so with $V_m(s)=\mathbb{E}[\prod_{i\le m}(\cdots);\ s_m=s]$ we have
$$
V_m(s)=e\!\left(\frac{u2^{j-s}\bmod 3^{n-m+1}}{3^{n-m+1}}\right)\sum_{a\ge1}2^{-a}V_{m-1}(s-a),\qquad \chi_n(2^ju)=\sum_s V_n(s).
$$
The convolution again obeys $G(s)=\tfrac12(V(s-1)+G(s-1))$. We truncate at $s\le S_{\max}=2n+12\sqrt{2n}+60$; the discarded mass is at most $\mathbb{P}(s_n>S_{\max})<10^{-25}$ by Chernoff. This is an absolute bound. For $n\ge1000$ it exceeds $|\chi_n|$ itself ($M^*_{1000}=4.0\times10^{-28}$, $M^*_{2000}=2.2\times10^{-52}$), so it does not control relative accuracy. Relative accuracy of the truncated values is supported by stability under enlarged cutoffs, not proved. The cost is $O(nS_{\max})=O(n^2)$ arithmetic operations modulo $3^k$ at the chosen cutoff (the bit complexity is larger, since the moduli have $O(n)$ bits). The algorithm evaluates the truncated expectation; it is not an exact finite evaluation of the infinite one, and phases are rounded to 53 bits from exact integer division. Against the exact tables ($n\le18$) the agreement is $5\times10^{-11}$, limited by the printed precision. An 80-bit recomputation agrees to relative error $10^{-19}$ for $\ell\le50$, because the entries of $V_m$ shrink together with the result. This algorithm supersedes the Monte Carlo and hybrid computations (§§4.4–4.5), which we keep only as independent cross-checks.

## 4. Results and supporting evidence

### 4.1 Exact values, $n\le18$

| $n$ | $M_n$ | $\mathbb{E}_u|\chi_n(u)|^2$ | $n$ | $M_n$ | $\mathbb{E}_u|\chi_n(u)|^2$ |
|---|---|---|---|---|---|
| 1 | 5.774e-1 | 3.33e-1 | 10 | 3.828e-2 | 1.19e-5 |
| 2 | 3.779e-1 | 7.94e-2 | 11 | 3.194e-2 | 3.96e-6 |
| 3 | 2.522e-1 | 2.56e-2 | 12 | 2.646e-2 | 1.32e-6 |
| 4 | 1.770e-1 | 8.60e-3 | 13 | 2.205e-2 | 4.42e-7 |
| 5 | 1.293e-1 | 2.87e-3 | 14 | 1.913e-2 | 1.47e-7 |
| 6 | 9.611e-2 | 9.59e-4 | 15 | 1.628e-2 | 4.92e-8 |
| 7 | 7.587e-2 | 3.19e-4 | 16 | 1.441e-2 | 1.64e-8 |
| 8 | 6.089e-2 | 1.07e-4 | 17 | 1.251e-2 | 5.48e-9 |
| 9 | 4.803e-2 | 3.56e-5 | 18 | 1.119e-2 | 1.83e-9 |

For $8\le n\le18$, the maximum is attained at $\xi=2^{j^*}$ with $j^*\in\{9,10,12,13,14,16,17,18,20,21,23\}$, that is, $j^*=\lambda n-c$ with $c\in[3.6,5.6]$. For $n \le 7$ the arg-max is the conjugate representative $-2^{j}$. For $n\le18$ the mean square over units lies between $0.69$ and $1.00$ times $3^{-n}$. By Parseval it equals $(3^n\mathrm{CP}_n-3^{n-1}\mathrm{CP}_{n-1})/(2\cdot3^{n-1})$, where $\mathrm{CP}_n=\sum_x\mathbb{P}(\mathrm{Syrac}_n=x)^2$ is the collision probability. Over these 18 levels, $M_n$ falls by a factor of only about $50$. The local rate $\ln(M_{17}/M_{18})=0.11$ is far below the generic rate $\tfrac12\ln3=0.55$.

### 4.2 Exact values along the extremal family, $n\le2000$

With the single-frequency algorithm of §3.4 we computed $M^*_n=\max\{|\chi_n(2^j)|:\ \lambda n-14\le j\le\lambda n+3\}$. For $n\le18$ this window contains the global maximum $M_n$, and an exhaustive search over all units (below) shows the same for $19\le n\le70$ and $n=75,80$. For larger $n$ it is a lower bound for $M_n$, and we conjecture equality; the exact multiplier scan at $n=150$ (below) supports this.

| $n$ | $j^*$ | $j^*-\lambda n$ | $M^*_n$ | $n\,e^{In}M^*_n$ |
|---|---|---|---|---|
| 20 | 26 | -5.69 | 8.885e-03 | 0.534 |
| 30 | 42 | -5.54 | 3.288e-03 | 0.513 |
| 44 | 64 | -5.73 | 9.893e-04 | 0.489 |
| 62 | 92 | -6.26 | 2.435e-04 | 0.456 |
| 80 | 120 | -6.79 | 6.453e-05 | 0.420 |
| 100 | 152 | -6.49 | 1.594e-05 | 0.389 |
| 120 | 184 | -6.19 | 4.120e-06 | 0.363 |
| 150 | 231 | -6.74 | 5.964e-07 | 0.341 |
| 180 | 279 | -6.29 | 9.177e-08 | 0.328 |
| 220 | 342 | -6.69 | 8.232e-09 | 0.324 |
| 260 | 405 | -7.09 | 7.681e-10 | 0.322 |
| 300 | 469 | -6.48 | 7.425e-11 | 0.324 |
| 400 | 627 | -6.98 | 2.302e-13 | 0.327 |
| 500 | 786 | -6.48 | 7.553e-16 | 0.328 |
| 650 | 1023 | -7.22 | 1.497e-19 | 0.322 |
| 800 | 1261 | -6.97 | 3.130e-23 | 0.317 |
| 1000 | 1578 | -6.96 | 4.033e-28 | 0.304 |
| 1200 | 1895 | -6.96 | 5.391e-33 | 0.291 |
| 1400 | 2212 | -6.95 | 7.411e-38 | 0.278 |
| 1700 | 2688 | -6.44 | 3.920e-45 | 0.260 |
| 2000 | 3163 | -6.93 | 2.159e-52 | 0.245 |

For $n\ge1200$ the window is $[\lambda n-9,\lambda n-4]$. It contains $j^*$ for every $n\ge62$ in the table. At $n=1000$ an 80-bit recomputation agrees with the float64 value to 7 printed digits ($4.032640\times10^{-28}$). Least-squares fits of $\log M^*_n=a-\beta\log n-\kappa n$ give $(\beta,\kappa)=(0.88,0.05529)$ for $n\ge300$, $(0.92,0.05525)$ for $n\ge500$ and $(1.02,0.05518)$ for $n\ge800$, against $I=0.054980$. With $\kappa=I$ fixed, $\beta=1.15$, $1.21$ and $1.28$ on the same ranges, and the two-point exponents are $1.26$ on $[1000,1400]$ and $1.35$ on $[1400,2000]$. So the rate is $I$ to within $0.5\%$, but the polynomial correction has not converged. The plateau $n\,e^{In}M^*_n\approx0.32$ for $180\le n\le800$ is pre-asymptotic. Adding a correction term, $\log(e^{In}M^*_n)=a-\beta\log n+b\,n^{-1/2}$, does not stabilise the estimate either: the fit gives $\beta=1.17\pm0.07$, $1.48\pm0.05$, $1.67\pm0.03$ and $1.79\pm0.02$ for $n\ge100,180,300,500$ (formal errors). Data at $n\le2000$ alone therefore do not determine $\beta$. §4.7 shows why: the dominant renewal levels ($\ell\approx131$) switch on only at $n\approx2\times10^4$–$10^5$. Data to $n=3\times10^5$, matched by a zero-parameter limit formula, give $\beta=3/2$ (NUMERICAL). The normalized column also wobbles because $j$ is an integer: $j^*-\lambda n$ moves through $[-7.2,-6.2]$ as $\{\lambda n\}$ varies. The local rate decreases monotonically, from $0.099$ ($n=20$–$30$) to $0.0558$ ($n=1400$–$2000$).

*Certified two-sided bounds.* With the ball-arithmetic DP of §4.3 (`certify_M.py`) we certified the table entries at $(n,j^*)=(100,152),(200,310),(400,627),(600,944),(800,1261),(1000,1578)$. This gives rigorous lower bounds $M_n\ge1.5936\times10^{-5}$, $2.7273\times10^{-8}$, $2.3022\times10^{-13}$, $2.5620\times10^{-18}$, $3.1301\times10^{-23}$ and $4.0326\times10^{-28}$, which agree with the float64 values to all printed digits. At the same $(n,j^*)$, Corollary 3 gives the rigorous upper bounds $2.2\times10^{-2}$, $7.8\times10^{-5}$, $1.3\times10^{-9}$, $2.2\times10^{-14}$, $3.7\times10^{-19}$ and $6.2\times10^{-24}$. The ratio of upper to lower bound grows only from $1.4\times10^3$ to $1.5\times10^4$, roughly linearly in $n$, while both decay through 23 orders of magnitude. So at these six points the true size along the extremal family is rigorously bracketed within a factor of at most $1.6\times10^4$ of $39\,e^{-In+\theta^*(j^*-\lambda n)}$. This is a finite statement, and it is consistent with C1.

*Is $2^j$ the extremal family for $n>18$?* We scanned all $|\chi_n(2^ju)|$ exactly with $1\le u\le U$, $u$ odd, $3\nmid u$, and $0\le j\le J$, using $(n,U,J)=(40,199,120)$, $(80,199,160)$ and $(150,101,260)$. That is 8107, 10787 and 8874 frequencies; since $|\chi_n(-\xi)|=|\chi_n(\xi)|$, signs are covered. We also scanned 3000, 2000 and 500 uniformly random units. In every case $u=1$ attains the maximum, at the same $j^*$ as in Table 2. The best competitor is always $u=13=2^4-3$, at $j=j^*-3$ or $j^*-4$, with ratio $0.33$, $0.33$ and $0.38$. This is a second family with the same exponential rate, consistent with the near-relation picture of §5. The random units have root-mean-square size $0.72$, $0.64$ and $0.57$ times $3^{-n/2}$, and their maxima are $10$ to $20$ times their root-mean-square size. They lie more than $10^{28}$ below $M^*_{150}$.

*Exhaustive search over all units, $19\le n\le70$ and $n=75,80$.* The scans above test only small multipliers. A branch-and-bound over the 3-adic digits of $\xi$ covers every unit. Write $\chi_n(\xi)=\mathbb E\prod_{m\le n}z_m(s_m)$ with $z_m(t)=e(\xi2^{-t}/3^{n-m+1})$, so that row $m$ sees only $\xi\bmod3^{n-m+1}$. The backward vectors $G_{n+1}=1$, $G_m(s)=\sum_{a\ge1}2^{-a}z_m(s+a)G_{m+1}(s+a)$ satisfy $\chi_n(\xi)=G_1(0)$, and $G_m$ depends only on $\xi\bmod3^{n-m+1}$. For every completion of these digits,
$$
|\chi_n(\xi)|=\Bigl|\sum_sV_{m-1}(s)\,G_m(s)\Bigr|\le\sum_s w_{m-1}(s)\,|G_m(s)|=:U_m ,
$$
where $V_{m-1}$ is the forward vector of the rows not yet fixed and $w_{m-1}=\mathbb P(s_{m-1}=\cdot\,)\ge|V_{m-1}|$. We fix the digits of $\xi$ from the bottom, one per row, and discard a residue class as soon as $U_m<T$. By $\chi_n(-\xi)=\overline{\chi_n(\xi)}$ only $\xi\equiv1\pmod 3$ is searched. We truncate at $s\le S=3n+40$. Since $s_m$ is increasing, the truncated $G_m(s)$ is the same expectation restricted to $s_n\le S$, so truncation adds at most $\mathbb P(s_n>S)=\mathbb P(\mathrm{Bin}(S,\tfrac12)\le n-1)\le1.4\times10^{-10}$ to every bound (computed exactly). Arithmetic is float64. The phases are computed from the exact binary digits of $-\xi3^{-e}\bmod2^S$, and they agree with exact integer division to $1.1\times10^{-16}$. The recursion only takes convex averages and multiplies by unimodular factors, so rounding is not amplified; a forward error estimate puts the rounding in each $U_m$ below $10^{-12}$. An 80-bit recomputation along four complete digit paths at $n=70$ (three random units and $2^{105}$) agrees with every float64 $G_m$ to $4\times10^{-16}$ (`round_check.py`). This is not interval arithmetic. As validation, at $n=10$ with $T=0.3M_{10}$ the search returns exactly the 111 classes found by brute force over all units, and at $n=16,18$ it reproduces $M_n$ of §4.1.

With $T=0.999\,M^*_n$, for every $n$ with $19\le n\le70$ and for $n=75,80$, the surviving classes are $\pm2^{j^*}$, where $j^*$ maximises $|\chi_n(2^j)|$ over the window of Table 2, and at $n=63$ only also the neighbour $\pm2^{j^*+1}$ ($j^*=93$, ratio $0.99927$) (`allunits_bb.txt`). The class of $2^{j^*}$ must survive, since $U_m\ge|\chi_n(2^{j^*})|$ along its digits. Hence $M_n=M^*_n$, the maximiser is unique up to sign, and every unit outside the family $\pm2^j$ has $|\chi_n(\xi)|<0.999\,M_n+10^{-12}$. The search visits $1.1\times10^6$ classes at $n=50$ and $2.3\times10^7$ at $n=70$, about $3^{0.14n}$, which sets the practical limit. Among the pruned classes, the largest bound $U_m$ is within a relative $10^{-5}$ of $T$ at every $n\ge45$; this reflects the many classes visited, and it does not affect the conclusion, since every pruned bound is below $T$.

*Superlevel sets.* With $T=M_n/2$ the same search lists every unit with $|\chi_n(\xi)|\ge M_n/2$ (`superlevel_half.txt`). At $n=20,30,40,50$ there are $14,14,15,15$ such classes with $\xi\equiv1\pmod3$. Of these, $7,7,8,8$ are family members $\pm2^j$ with consecutive $j$, all with $j-\lambda n\in[-10.4,-2.7]$. Every other class is a *top-digit relative*: $\xi\equiv\pm2^j\pmod{3^{n-1}}$ but $\xi\not\equiv\pm2^j\pmod{3^n}$. Changing $\xi$ by $c\,3^{n-1}$ changes only the first row, by the factor $e(c(-1)^{s_1}/3)$, since $2^{-s}\equiv(-1)^s\pmod 3$. The largest relative has $|\chi_n|=0.666,0.654,0.648,0.646$ times $M_n$. No other unit reaches $M_n/2$; in particular the $u=13$ family of the multiplier scans ($0.33M_n$) does not.

### 4.3 The renewal input $\chi_\ell(1)$: float values for $\ell\le800$, certified bounds for $\ell\le1000$

The same algorithm gives $\chi_\ell(1)$ for every $\ell\le800$ (`chi1_scan.txt`, `chi1_scan_401_800.txt`). A linear fit of $\ln|\chi_\ell(1)|$ over $50\le\ell\le800$ has slope $-0.565$, with residual standard deviation $2.0$ (the values fluctuate like a typical random sum). From the float values, the constants $B(\rho)=\max_{\ell\le800}|\chi_\ell(1)|\rho^{-\ell}$ are $B(0.575)=17.7$, $B(0.578)=8.96$, $B(0.580)=5.70$ and $B(0.584)=2.32$, all attained at $\ell=131$; for $401\le\ell\le800$ every value satisfies $|\chi_\ell(1)|\le e^{-2.8}\,3^{-\ell/2}$. For comparison we drew 20–30 uniformly random units $u$ at each of $\ell=50,100,200,\dots,800$ (`rand_units.txt`). The median of $\ln(|\chi_\ell(u)|\,3^{\ell/2})$ is $-1.5,-2.5,-3.9,-5.8,-6.2,-7.3,-9.9,-11.5,-12.1$, which is linear in $\ell$ with slope $-0.014$. So typical units decay at rate $\approx0.564$, slightly *faster* than square-root cancellation ($0.549$). The spread of $\ln|\chi_\ell(u)|$ also grows, with the sample range rising from $3.9$ at $\ell=50$ to $7.7$ at $\ell=800$. So the median rate and the root-mean-square rate can differ: by Jensen, $\mathbb{E}_u\ln|\chi_\ell(u)|\le\tfrac12\ln\mathbb{E}_u|\chi_\ell(u)|^2$, so a typical ("quenched") rate above $\tfrac12\ln3$ is compatible with a mean square of order $3^{-\ell}$, which would then be carried by rare large units. Our samples are too small to estimate the mean square at large $\ell$. The block medians of $\ln(|\chi_\ell(1)|\,3^{\ell/2})$ over $\ell\in[1,100],\dots,[701,800]$ track them, from $-1.0$ to $-13.4$, so $u=1$ is a typical unit. The hypothesis of Theorem 2 is therefore the statement that one fixed frequency shows the typical cancellation. A phase-perturbation test (`sensitivity.py`) multiplies every phase factor by $e^{i\epsilon g}$ with $\epsilon=10^{-10}$ and $g$ standard normal. It changes $\chi_{800}(1)\approx2.0\times10^{-197}$ by a relative $4.6\times10^{-9}$, so rounding amplification is below $50$ and the float64 values are reliable despite their size.

*Rigorous certification.* `certify_chi1.py` repeats the DP for $u=1$, $j=0$ and every $\ell\le1000$ in Arb ball arithmetic (python-flint 0.6.0). Each phase $e(x/3^k)$ is enclosed from the exact rational $x/3^k$. Entries with $s_m>S$ are dropped, and since $s_m$ is increasing, the dropped contribution has modulus at most $\mathbb{P}(s_\ell>S)=\mathbb{P}(\mathrm{Bin}(S,\tfrac12)\le\ell-1)$, which we compute exactly as a rational. We take the smallest $S\in2\ell+16\mathbb{Z}_{\ge0}$ with tail at most $2^{-0.786\ell-20}$. Rectangular complex balls inflate by up to $|\cos\theta|+|\sin\theta|$ (on average $4/\pi$) at every phase multiplication, so a working precision of only $0.8\ell$ bits loses all accuracy by $\ell\approx800$. With $1.25\ell+100$ bits the ball radius of the truncated sum is below $10^{-28}$ relative to its midpoint. The certified quantity is an upper envelope: the midpoint plus radius plus the truncation allowance. For large $\ell$ the allowance dominates; at $\ell=800$ the midpoint is $2.0\times10^{-197}$ and the allowance is $5.4\times10^{-196}$. This is all that Corollary 3 needs, but it does not certify the coefficient itself to any relative accuracy. All bounds are exported with directed decimal rounding (upper bounds rounded up, lower bounds rounded down). The resulting rigorous upper bounds (`certify_chi1.txt`; about 38 min for $\ell\le800$ and 52 min for $801\le\ell\le1000$, with 5 processes) give $\max_{\ell\le1000}\overline{|\chi_\ell(1)|}\,0.58^{-\ell}=5.6961$ at $\ell=131$. The Arb midpoints agree with the float64 values to relative error $5\times10^{-10}$ for $\ell\le800$. Since both use the same cutoff, this confirms the floating-point arithmetic of the truncated sum, not the truncation.

### 4.4 Cross-check: Monte Carlo, $20\le n\le62$

Each run uses $S=2\times10^8$ samples of $(a_1,\dots,a_n)$ and exact 128-bit arithmetic mod $3^n$, and evaluates $\chi_n(2^j)$ for $0\le j<J$. The standard error is about $5\times10^{-5}$ per component.

| $n$ | $\max_j|\hat\chi_n(2^j)|$ (MC) | $j^*$ | $\lambda n-j^*$ | exact $|\chi_n(2^{j^*})|$ (§3.4) |
|---|---|---|---|---|
| 20 | 8.84e-3 | 26 | 5.7 | 8.885e-3 |
| 24 | 5.82e-3 | 32 | 6.0 | 5.831e-3 |
| 30 | 3.19e-3 | 41 | 6.5 | 3.254e-3 |
| 36 | 1.89e-3 | 51 | 6.1 | 1.950e-3 |
| 44 | 1.03e-3 | 64 | 5.7 | 9.893e-4 |
| 52 | 5.70e-4 | 76 | 6.4 | 5.253e-4 |
| 62 | 2.73e-4 | 92 | 6.3 | 2.435e-4 |

A multiplier scan at $n=30$ over $\chi_{30}(c\,2^j)$ for small odd $c$ confirms that $c=1$ dominates ($3.2\times10^{-3}$; the next largest is $c=11$ at $1.25\times10^{-3}$). The Monte Carlo maxima agree with the exact values to within about $1.5$ standard errors, except at $n=62$, where taking the maximum over $J$ noisy values biases the estimate upward by $4\sigma$. Fitted on $20\le n\le62$ alone, the form $\log M_n=a-\beta\log n-\kappa n$ gives $\beta\approx1.31$ and $\kappa\approx0.047$, both far from the large-$n$ values of §4.2: in this range the data are pre-asymptotic.

### 4.5 Cross-check: renewal decomposition at large $n$

Theorem 1 can be evaluated independently of §3.4. The weights $\mathcal{M}_n,W_\ell$ come from the cold-walk recursion (§3.2) and $\chi_\ell(1)$ from §4.3. At $(n,j)=(100,152)$, $(200,310)$ and $(300,469)$ the two computations agree to relative error $2\times10^{-11}$, $5\times10^{-11}$ and $6\times10^{-11}$. The decomposition also shows *where* the mass sits. The main term is only $0.9\%$, $0.6\%$ and $0.5\%$ of $|\chi_n(2^j)|$, and the largest single renewal term has $\ell=7$, $17$ and $17$. So the extremal coefficients are governed by the renewal sum, i.e. by the near-critical competition in Theorem 2. They are not governed by the cold-walk probability $\mathbb{P}(s_n\le j)$ alone.

An earlier hybrid model replaced $\chi_\ell(1)$, $\ell>18$, by independent random phases with variance $\mathbb{E}_u|\chi_\ell(u)|^2$. It reproduces $M^*_n$ to within $10\%$ for $n\le300$ and recovers the rate $I$, but it overestimates the large-$n$ prefactor: it predicts a local $\beta\approx0.4$, whereas the computed values of Table 2 give $1.0$–$1.35$ (§4.2). We keep it only as evidence that the rate does not depend on the arithmetic details of $\chi_\ell(1)$. Using only $|\chi_\ell(1)|\le1$ for $\ell>18$ certifies $M^*_{20}$ and $M^*_{24}$ to within $1\%$; beyond $n\approx30$ that crude certificate fails.

### 4.6 Shape of the extremal profile

The exact profile $|\chi_n(2^j)|/M^*_n$ has the same shape at every $n$ (`profile_exact.txt`):

| $j-j^*$ | $-8$ | $-6$ | $-4$ | $-2$ | $0$ | $+2$ | $+4$ | $+6$ | $+8$ | $+10$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $n=62$ ($j^*-\lambda n=-6.3$) | 0.212 | 0.385 | 0.627 | 0.880 | 1.000 | 0.813 | 0.375 | 0.078 | 0.024 | 0.004 |
| $n=150$ ($j^*-\lambda n=-6.7$) | 0.286 | 0.453 | 0.668 | 0.886 | 1.000 | 0.862 | 0.461 | 0.110 | 0.024 | 0.004 |
| $n=400$ ($j^*-\lambda n=-7.0$) | 0.307 | 0.468 | 0.670 | 0.878 | 1.000 | 0.892 | 0.513 | 0.140 | 0.032 | 0.014 |

On the left, the logarithmic slope grows with distance from the peak, reaching $0.33$ ($n=62$), $0.25$ ($n=150$) and $0.23$ ($n=400$) nats per unit of $j$ at $j^*-9$. The upper bound of Theorem 2 has slope $\theta^*=0.304$: a smaller $j$ requires a larger deviation for the walk to stay cold, but the renewal terms soften the penalty. On the right the profile falls about $250$-fold over $10$ units of $j$ (per-unit factors between $1.2$ and $3$), because the walk now starts in the *hot-archimedean* region $r>\lambda k$, where phases $2^{r}/3^{k}$ are large real numbers. Those first rows cancel through the Fourier transform of the real stationary law $Z=\sum_{m\ge1}3^{m-1}2^{-s_m}$, which satisfies $Z\overset{d}{=}2^{-a}(1+3Z')$. A Monte Carlo estimate ($2\times10^7$ samples) gives $|\widehat{Z}(2^t)|\approx 0.037\cdot 2^{-0.58t}$ for integer $0\le t\le 10$ (half-integer $t$ are smaller), a power decay at an exponent consistent with an absolutely continuous stationary measure. The maximum, at $d=j^*-\lambda n\in[-7.2,-6.2]$ for all $62\le n\le2000$ in Table 2, is the balance point between these two effects. It stays bounded as $n$ grows, which is why the extremal frequencies are $2^{\lambda n-O(1)}$.

### 4.7 The polynomial correction: $\beta=3/2$ and the limit constant (numerical, $n\le3\times10^5$)

The drift of the fitted exponent in §4.2 is a slow pre-asymptotic effect, which we resolve by going to $n=3\times10^5$. Write $\psi_r(t)=\chi_r(2^t)$. Splitting Tao's recursion at $a=1$ gives the twisted Pascal recursion of [9], $\psi_r(t)=\tfrac12\psi_r(t-1)+\tfrac12e(2^{t-1}/3^r)\psi_{r-1}(t-1)$, with $\psi_0\equiv1$ and $\psi_r(0)=\chi_r(1)$. We checked it against Tao's recursion for $r\le7$, $t\le16$ (maximal error $2.8\times10^{-16}$). Run forward from the $\chi_\ell(1)$ of §4.3, it reproduces Table 2 to 7 digits for $400\le n\le2000$. Define
$$y_n(d)=\frac{n\,\chi_n(2^j)}{\binom{j}{n}2^{-j}},\qquad j=\lfloor\lambda n\rfloor+d .$$
This is exact bookkeeping: $|\chi_n(2^j)|=|y_n|\binom jn2^{-j}/n$, and for bounded $d$ the factor $\binom jn2^{-j}$ is $\asymp n^{-1/2}e^{-In}$. So $\beta=3/2$ is equivalent to $y_n$ staying bounded above and away from $0$. At large $n$ we use the Cramér-tilted form $\phi_r(t)=(2q)^t(\lambda-1)^{-r}\psi_r(t)$, with $q=1-1/\lambda$. It has no underflow, and in the unwrapped cells $2^t<3^r$ its phase is exactly $e(2^{t-r\lambda})$. Setting the wrapped cells to $0$ changes $|y_n(-6)|$ by a relative $1$–$2.4\times10^{-4}$, as checked against high-precision phases to $n=8000$ (`tilted_exact.py`: exact big-integer residues $2^t\bmod3^r$, phase ratio from the top 60 bits; not certified). The row-truncated run (`tilted_unwrapped_fast.py`) reaches $n=3\times10^5$ in under an hour.

*Mechanism.* By linearity, $y_n=\sum_{\ell}s_n(\ell)\,\frac{\binom{j}{n-\ell}}{\binom jn}\,\chi_\ell(1)+(\text{top row})$, with a kernel $s_n(\ell)$ that converges fast in $n$ (`kernel_delta.py`). The binomial ratio is $(\lambda-1)^{-\ell}\exp(-\frac{\lambda}{2(\lambda-1)}\frac{\ell^2}{n}+\dots)$ [9, Remark 3.2]. So level $\ell$ switches on only once $n\gtrsim1.35\,\ell^2$. The weight $(\ell+1)(\lambda-1)^{-\ell}|\chi_\ell(1)|$ peaks at $\ell=131$, which delays the onset of the dominant contributions to $n\approx2\times10^4$–$10^5$; this is the near-critical margin of §1 again. As a result $|y_n(-6)|$ grows from $138$ ($n=2000$) to between $1.14\times10^3$ and $1.67\times10^3$ for $1.5\times10^5\le n\le3\times10^5$, depending on $\{\lambda n\}$, and fits at $n\le2000$ underestimate $\beta$.

*Limit formula.* cassian_mahler derived from a half-space local limit theorem [9; rStation r/collatz post 21] that
$$\lim_{\substack{n\to\infty\\ \{\lambda n\}\to\delta}}y_n(d)=\frac{2}{\lambda(\lambda-1)}\,g^*(\delta-d)\,\Sigma,\qquad \Sigma=h_0^*+\sum_{\ell\ge1}h^*(\ell\lambda)(\lambda-1)^{-\ell}\chi_\ell(1),$$
where $h^*$ and $g^*$ are the harmonic functions, with unit slope, of the 1D zero-drift walks $z\mapsto z-1$ (probability $q$) and $z\mapsto z+\lambda-1$ (probability $1/\lambda$), weighted by the phases $e(2^{-(z+\lambda)})$ and $e(2^{-(z+1)})$ respectively; and $h^*(z)-z-c_0\to0$ as $z\to\infty$ (numerically $|h^*(6\lambda)-6\lambda-c_0|\approx0.10$; we use only the summability of this tail, not a pointwise rate). We solved for $h^*,g^*$ independently (`milne_check.py`: killed-walk propagation with an affine closure). This gives $c_0=-5.093+2.266i$ and $|\Sigma^{(800)}|=309.18$, in agreement with [9] to 4–5 digits; the closure converges slowly in the walk length (differences shrink about $3.6\times$ per doubling), so the last digit is uncertain; the partial sums are $20.6$ at $L=100$ and $309.4$ at $L=150$. The finite-$n$ form, with the exact binomial ratios in place of their limit, matches the truncated-recursion values (wrapped cells killed, $\chi_\ell(1)$ truncated at $\ell=800$) in modulus and argument (`milne_finite.py`). Agreement is evidence, not certification:

| $n$ | $2\,000$ | $19\,800$ | $54\,600$ | $99\,100$ | $150\,675$ | $230\,550$ | $297\,375$ |
|---|---|---|---|---|---|---|---|
| $\lvert y_n(-6)\rvert$ (truncated recursion) | 138.38 | 522.97 | 1209.16 | 1361.20 | 1222.04 | 1230.27 | 1308.52 |
| recursion / formula | 0.9936 | 0.9896 | 0.9935 | 0.9968 | 0.9986 | 0.9992 | 0.9994 |
| phase gap (rad) | 0.032 | 0.020 | 0.008 | 0.005 | 0.003 | 0.002 | 0.0017 |

The same comparison at $d=-9$ and $d=-3$ gives ratios $0.9969$ and $1.0021$ at $n=264\,375$, so the $d$-dependence is carried by $g^*$ as claimed. At $d=0$ the formula fails for exit points $z=\delta-d<\lambda-1$. Against high-precision phases ($n\le8000$), the ratio is $1.00$–$1.07$ for $\delta>0.68$, $0.88$–$0.94$ for $0.29\le\delta\le0.57$ and $0.69$–$0.78$ for $\delta\le0.13$. The cause is the hard kill at $z<0$ in the exit equation. The lattice phase $e(2^{t-1}/3^r)=e(2^{-(z+1)})$ is exact for every $z$, since $e$ is $1$-periodic. If $g^*$ keeps these phases down to $z\ge-8$ instead of killing at $z<0$ (`milne_g_variant.py`), the $d=0$ ratio becomes $1.03$–$1.06$ with no $\delta$-dependence for $2500\le n\le8000$ (after $1.13$ and $1.08$ at $n=1000,1750$). For comparison, the $d=-6$ ratio is $0.98$ at $n=8000$. The change moves $|g^*(6.25)|$ only from $2.1242$ to $2.1241$, so the extremal offsets $d\le-3$ are unaffected. Over $\delta\in[0,1)$ the limit has modulus between $1299$ and $1794$. The finite-$n$ values at $2\times10^5\le n\le3\times10^5$ are $0.90$–$0.93$ of the limit, as expected from the onset factor $e^{-1.35\cdot131^2/n}=0.89$–$0.93$ of the dominant level. So along the extremal family, at each tested offset $d\in\{-9,-6,-3\}$ (the maximiser has $j^*-\lambda n\in[-7.2,-6.2]$, i.e. $d\in\{-7,-6\}$),
$$n^{3/2}e^{In}\,|\chi_n(2^{\lfloor\lambda n\rfloor+d})|\ \text{converges along }\{\lambda n\}\to\delta\text{ to a positive, continuous function of }\delta,$$
i.e. $\beta=3/2$, with the constant predicted. Status: NUMERICAL. A proof needs (i) the half-space local limit theorem with a complex potential, uniformly for $\ell\lesssim\sqrt n$, together with a bound on the wrapped cells $2^t\ge3^r$ (the formula concerns the recursion with these cells killed. Against high-precision phases for $n\le8000$, their effect on $\log|y_n(d)|$ is about $10^{-4}$ at $d=-6$, $2\times10^{-4}$ at $d=-3$ and $10^{-2}$ at $d=0$, so numerically the formula agrees with the true $\chi_n$ only for $d\lesssim-3$; this is an observation, not a certified statement); (ii) the hypothesis of Theorem 2 beyond $\ell=1000$ (certified for $801\le\ell\le1000$: $\sum(\ell+1)(\lambda-1)^{-\ell}\overline{|\chi_\ell(1)|}\le4.8\times10^{-4}$); and (iii) $\Sigma\neq0$. For item (iii) we prove the implication (H$'$) $\Rightarrow\Sigma\neq0$; see the certificate below. Items (i) and (ii), including (H$'$) itself, remain open.

*Certificate for (iii), conditional only on (H$'$)* (`certify_chi1_signed.py`, `arb_barrier_h.py`, `sigma_cert_arb.py`). Write $w_\ell=(\lambda-1)^{-\ell}\chi_\ell(1)$. The constant term is $h_0^*=\lambda^{-1}e(1/3)\,h^*(\lambda-1)$, the first step of the walk from $z=0$. The certificate has two parts, both evaluated in Arb (python-flint 0.6.0, at least 160 bits). The first is an explicit candidate $\tilde h$ with a rigorous uniform bound $|h^*-\tilde h|\le C_0$. The second is a bound for $\Sigma$ with $h^*$ replaced by $\tilde h$. The only hypothesis is

- (H$'$) $|\chi_\ell(1)|\le0.54\cdot0.575^\ell$ for $\ell>1000$.

*The barrier.* The construction is cassian_mahler's concave barrier (rStation r/collatz post 21, comment `3gfPzxBXDQlY6W6H`). The interval port and the corrected constants are ours. The candidate $\tilde h$ is piecewise linear on $[0,Z_0]$, with step $1/M$. At $Z_0$ it is joined to $h_1(z)=z+c+(a_1z+a_0)2^{-z}$, where $a_1,a_0$ are fixed by $c$ so that the residual of $h_1$ is $O(z4^{-z})$. The node values and $c$ come from a floating-point collocation solve. They are then taken as exact dyadic rationals, so $\tilde h$ is an explicit function and the accuracy of the solve does not matter. Let $\mathcal Lf(z)=q\mathbf 1\{z>1\}f(z-1)+p\,e(2^{-(z+\lambda)})f(z+\lambda-1)$ on $z>0$, and let $r=\mathcal L\tilde h-\tilde h$ be the residual. Every non-negative, non-decreasing, concave $W$ on $[-1,\infty)$ satisfies $(I-\mathcal L_0^{\rm kill})W\ge0$. This follows from the Peano identity $(I-\mathcal L_0)W(z)=\int K(u)(-W''(z+u))\,du$ with a tent kernel $K\ge0$, the zero-drift identity $q(-1)+p(\lambda-1)=0$, and $W(z-1)\ge0$ on the kill strip. We take $W$ to be the sum of four such functions and check $(I-\mathcal L_0^{\rm kill})W\ge|r|$ pointwise:
- a constant $C_{\rm kill}$, with defect $qC_{\rm kill}$ on the kill strip $(0,1]$;
- a kink $\kappa\min(z+1,2)$. Its defect is $q\kappa(2-z)\ge q\kappa(1-1/M)$ on the jump cell $(1,1+1/M]$, and $\ge0$ elsewhere;
- a quadratic box $A\bigl(D^2-(D-z-1)^2\bigr)$, constant beyond its maximum, with $A=\varepsilon_{\rm box}/(\lambda-1)$ and $D=Z_0+1+\lambda$. Its defect is $A(q+p(\lambda-1)^2)=\varepsilon_{\rm box}$ on $(0,Z_0+1]$;
- a tail $W_\infty-(B_1z+B_0)4^{-z}$ on $z\ge Z_0-1$, continued by its tangent down to $0$ at $z=-1$. Here $\mathcal L_0 4^{-z}=\rho_2 4^{-z}$ with $\rho_2=4q+4p/9>1$. With $B_1,B_0$ explicit, the defect is $\ge(M_1z+M_0)4^{-z}$ on $z\ge Z_0+1$.

Let $\varepsilon_{\rm kill},\varepsilon_{\rm spike},\varepsilon_{\rm box}$ be upper bounds for $|r|$ on $(0,1]$, on $(1,1+1/M]$ and on $(1+1/M,Z_0+1]$. Take $C_{\rm kill}=(\varepsilon_{\rm kill}-\varepsilon_{\rm box})^+/q$ and $\kappa=(\varepsilon_{\rm spike}-\varepsilon_{\rm box})^+/(q(1-1/M))$. On $z\ge Z_0+1$, all three points of the walk lie in the asymptotic piece. A second-order expansion of the phase then gives $|r|\le(M_1z+M_0)4^{-z}$, with $M_1,M_0$ enclosed in Arb. On $[0,Z_0+1]$, each cell $[j/M,(j+1)/M]$ is split where $z+\lambda-1$ crosses a node. On each of the resulting $7956$ sub-segments, the three pieces of $\tilde h$ that enter $r$ are therefore fixed. This holds by construction, because the split point is $k/M-(\lambda-1)$ exactly and enters as a ball. The program also asserts it for every sub-segment. Where a ball touches a node, the two adjacent pieces agree at the true point, so the enclosure is unaffected. On a sub-segment $[a,b]$,
$$\sup_{[a,b]}|r|\le\max(|r(a)|,|r(b)|)+\tfrac{(b-a)^2}{8}\sup_{[a,b]}|r''|.$$
This is the Peano bound for linear interpolation, which is valid for complex $r$. Here $r''$ is enclosed over the whole sub-segment, so these are universal bounds, not samples. At $(Z_0,M)=(12,306)$ (`h_cert_12_306.txt`):
- $\varepsilon_{\rm kill}\le1.92\cdot10^{-5}$, $\varepsilon_{\rm spike}\le0.012884$ and $\varepsilon_{\rm box}\le6.46\cdot10^{-6}$;
- $C_{\rm kill}\le3.46\cdot10^{-5}$, $W_{\rm kink}(\infty)=2\kappa\le0.070013$, $W_{\rm box}(\infty)=AD^2\le0.002348$ and $W_{\rm tail}(\infty)\le0.001983$;
- hence $C_0:=W(\infty)\le0.074377$.

For any barrier in this class, $(I-\mathcal L_0^{\rm kill})W(z)\le qC_0/(z+1)$ for $z>1$. So $C_0\ge2\varepsilon/q$ for every $\varepsilon\le|r(1^+)|$. With $|r(1^+)|\approx0.01288$, this gives $C_0\gtrsim0.0698$, and the certified value respects it: the kink carries $94\%$ of $C_0$.

*Correction to v5.* v5 used floating-point cell enclosures. In the $h^*$ barrier it also divided by $q(2-1/M)$ instead of $q(1-1/M)$ in $\kappa$, which made $C_0$ too small by a factor of about $1.9$ ($0.0395$ instead of $0.0744$). The referee found the resulting inconsistency at the jump cell. Our audit of v5 had missed it, because its random spot checks excluded that cell. The $g^*$ barrier did not have this error. Both barriers are now certified in interval arithmetic.

Put $\delta(z)=\mathbb E_z\sum_{t<\tau}\Pi_t\,r(Z_t)$, where $\Pi_t$ is the product of phases. This series converges absolutely because $|r|\le(I-\mathcal L_0^{\rm kill})W$. It satisfies $|\delta|\le W\le C_0$ and solves $\delta=\mathcal L\delta+r$. A bounded solution of the homogeneous twisted equation vanishes, because $|\Pi_t|=1$ and the walk is killed a.s. (it is recurrent, and it is killed with probability $q$ on each visit to $(0,1]$). So $h^*=\tilde h+\delta$ is the unique solution with $h^*-z$ bounded, and $|h^*-\tilde h|\le C_0$ everywhere.

*Aggregation.* Arb gives signed complex enclosures of $\chi_\ell(1)$ for $\ell\le250$ (same DP and binomial truncation as Corollary 3). It also encloses $\tilde h(\ell\lambda)$ for $\ell\le1000$ and $\tilde h(\lambda-1)$ (`h_lattice.txt`); for these points the containment in a single piece is checked in exact ball comparisons. For $250<\ell\le1000$ we use the certified moduli of Corollary 3, i.e. the accepted directed-rounding table. Then
$$|\Sigma|\ \ge\ \Bigl|\sum_{\ell\le250}\tilde h(\ell\lambda)w_\ell\Bigr|-C_0\sum_{\ell\le250}|w_\ell|-\sum_{250<\ell\le1000}\bigl(|\tilde h(\ell\lambda)|+C_0\bigr)|w_\ell|-\lambda^{-1}\bigl(|\tilde h(\lambda-1)|+C_0\bigr)-R_H .$$
Here $R_H=0.54\sum_{\ell>1000}(\ell\lambda+|c|+C_0+1)\bigl(0.575/(\lambda-1)\bigr)^\ell$ is the tail under (H$'$), using $|\tilde h(z)-z-c|\le1$ for $z\ge1000$. The five terms are $308.778$, $2.820$, $14.841$, $0.082$ and $0.202$ (rounded outward), so
$$|\Sigma|\ \ge\ 290.83$$
(`sigma_cert_arb.txt`). What is PROVED is the implication (H$'$) $\Rightarrow|\Sigma|\ge290.83$. Everything else in it is an Arb computation. The decomposition $h^*=z+c_0+\psi^*$ is no longer needed. The threshold form with (C0) and ($\Psi$) as explicit hypotheses is still kept in `c21_sigma_cert.txt`: there, $\Sigma\neq0$ whenever $C_\psi<117$ at $\alpha=1/2$, $r_c=20$, $K=0$.

*The exit factor* (`arb_barrier_g.py`). The same construction certifies $g^*$, for the walk $+1$ (probability $q$) and $-(\lambda-1)$ (probability $p$, killed if $z<\lambda-1$). The jump of $\mathbf 1\{z\ge\lambda-1\}$ needs its own kink $\kappa\min(z+\lambda-1,2(\lambda-1))$. Its defect on the jump cell is $p\kappa(2(\lambda-1)-z)\ge p\kappa(\lambda-1-1/M)$. The kill strip $[0,\lambda-1)$ needs its own constant, with defect $pC_{\rm kill}$. At $(12,306)$, with all sub-segments enclosed as above (`g_cert_12_306.txt`):
- $|g^*-\tilde g|\le C_{0,g}\le0.033422$. The class forces $C_{0,g}\ge\varepsilon_{\rm kill}/p=0.02389$.
- $|\tilde g|\ge0.064819$ on $[1,12]$, using per cell the value at the midpoint minus the slope bound.
- $|\tilde g|\ge|\operatorname{Im}c|-(|b_1|z+|b_0|)2^{-z}\ge2.208$ on $[12,\infty)$.

Hence $|g^*(z)|\ge0.0313$ for all $z\ge1$, and $|g^*(6.25)|\ge2.092$. So the limit constant $\frac{2}{\lambda(\lambda-1)}g^*(\delta-d)\Sigma$ is nonzero for every $d\le-1$ and every $\delta$, modulo (H$'$) and item (i).

*Checks outside the proof.* An mpmath spot check of the analytic tail bounds on $[13,60]$ at 60 digits (`audit_tail_both.py`) gives $|r|\le0.234\,(M_1z+M_0)4^{-z}$ for $h$ and $\le0.766\,(M_1z+M_0)4^{-z}$ for $g$. The referee's value $|r(1+10^{-8})|=0.0128839$ lies below the certified $\varepsilon_{\rm spike}$. As a check on the constants, not a proof step, both programs also evaluate the explicit $W$ and its defect $(I-\mathcal L_0^{\rm kill})W$ in Arb, at three interior points of every cell of $[0,Z_0+1]$, at one point just right of the jump, and on a grid of step $1/8$ on $[Z_0+1,Z_0+41)$. They confirm $(I-\mathcal L_0^{\rm kill})W>|r|$ at all $12\,255$ points. The smallest relative margins are $3.3\cdot10^{-3}$ for $h$, at $z=1^+$, and $3.9\cdot10^{-4}$ for $g$, at $z=(\lambda-1)^+$. With the v5 kink constant this check fails at the jump cell.

The tail hypothesis (H$'$) uses the rate $0.575$ and not the $0.58$ of Corollary 3. The reason is that $0.58/(\lambda-1)=0.992$ would let the $\ell>1000$ tail of $\sum\ell\lambda|w_\ell|$ reach about $200$. The certified bounds on $600\le\ell\le1000$ satisfy $\le0.538\cdot0.575^\ell$. Local rates on windows of length 200 range over $0.544$–$0.581$, against the critical $-\ln(\lambda-1)=0.536$.

## 5. Conjecture and the cold-walk heuristic

**Conjecture C1.** $\displaystyle\lim_{n\to\infty}\frac1n\log\max_{3\nmid\xi}|\chi_n(\xi)|=-I,\qquad I=\lambda\bigl(\ln2-H(1/\lambda)\bigr)\approx0.05498,$ with near-extremal frequencies $\xi=\pm2^{\lambda n+O(1)}$. The stronger form C1$^+$ asserts $M_n=e^{-In+O(\log n)}$. Extremality of this family beyond $n=18$ is part of the conjecture, and the polynomial correction is not settled. Ballot-type heuristics for a walk constrained near the line $s_m\approx\lambda m$ suggest $n^{-3/2}$, and the main term $\mathcal{M}_n$ alone has local exponent $1.6$ at $n=500$. However, the renewal sum, which dominates (§4.5), has a near-critical geometric weight $(|\chi_\ell(1)|/(\lambda-1)^\ell)$. In the data of Table 2 the effective exponent (with $\kappa=I$ fixed) is $1.0$ on $180\le n\le800$, $1.26$ on $[1000,1400]$ and $1.35$ on $[1400,2000]$. It drifts upward because the dominant renewal levels switch on only at $n\gtrsim1.35\,\ell^2$ with $\ell\approx131$. At $n\le3\times10^5$ the truncated-recursion values (§4.7) match a zero-parameter limit formula with $n^{3/2}e^{In}|\chi_n(2^{\lfloor\lambda n\rfloor+d})|\to$ a positive function of $\{\lambda n\}$ (§4.7). We therefore state C1$^+$ in the sharp form $M_n\asymp n^{-3/2}e^{-In}$ along the family; this is NUMERICAL and not proved.

*Why this rate.* Write $k=n-m+1$ for the level and $r=j-s_m$ for the column. For $\xi=2^j$ the phase of the $m$-th term is the real number $2^r/3^k$ whenever $r\ge0$. It is tiny in the *cold* triangle $0\le r\lesssim\lambda k$, where it contributes no cancellation; it is effectively uniform when $r>\lambda k$; and when $r<0$ it is a 2-adic residue, which is where the renewal terms of Theorem 1 come from. A walk with mean slope $2>\lambda$ that starts at $r=\lambda n$ crosses $r=0$ after about $\lambda n/2$ steps, so about $79\%$ of the rows are cold at no cost. To avoid cancellation entirely, the walk must stay inside the cold triangle for all $n$ rows. With $j=\lambda n+d$ the conditions $0\le j-s_m\le\lambda(n-m+1)$ read $\lambda(m-1)+d\le s_m\le\lambda n+d$ for all $m\le n$. The upper constraint is essentially the endpoint event $s_n\le\lambda n+d$, whose probability is $e^{-In+o(n)}$ by Cramér's theorem. Heuristically, a walk conditioned on this endpoint runs along the line $s_m\approx\lambda m$, so these are the walks with neutral growth $2^{s_m}\approx3^m$, the regime of heuristic Collatz cycles. This explanation is heuristic: the endpoint estimate is not a pathwise (ballot-type) asymptotic, and it does not exclude complex cancellation among the remaining terms. Leaving the triangle early costs cancellation at a rate of roughly $0.56$ per row in the renewal part, the typical decay rate of $\chi_\ell$ found in §4.3. Theorem 2 shows that this trade-off is won by staying cold, provided $\chi_\ell(1)$ decays faster than $(\lambda-1)^\ell$.

*Comparison with random-map models.* Two models must be distinguished. A uniform distribution on $4^n$ independent random images has nonzero Fourier coefficients of root-mean-square size $2^{-n}$. If instead the random images keep the actual geometric input weights $2^{-(a_1+\dots+a_n)}$, the squared weights sum to $(\sum_{a\ge1}4^{-a})^n=3^{-n}$, and the root-mean-square size is $3^{-n/2}$. We compare with this weighted model throughout, and write "random-map rate" for its rate $\tfrac12\ln3$. Tao's entropy heuristic [1, Remark 1.15] predicts exponential mixing but does not specify this constant. The exact Syracuse law has the same mean square for $n\le18$ (§4.1), and at large $\ell$ its typical units decay slightly faster, at rate $0.564$ (§4.3). For the weighted random-map law $\max_u|\chi_n(u)|$ would decay like $3^{-n/2}$ up to a polynomial factor, i.e. at rate $\tfrac12\ln3=0.549$. C1 instead predicts a rate ten times smaller. So, measured by the median, the Syracuse law is slightly better than random at typical frequencies, and it is far worse at the extremal ones. Tao's predicted fine-scale mixing $\exp(-cm)$ [1] should therefore hold, but with a constant set by the neutral-growth large deviation rather than by entropy counting. Since $|\chi_n(\xi)|\le\mathrm{Osc}_{n-1,n}$, C1 (if true) forces $c\le I$ in any bound $\mathrm{Osc}_{m,n}\ll e^{-cm}$.

*Other frequencies.* For a general unit $\xi$, the near-zero phases $\{\xi2^{-s}/3^{k}\}$ form a disjoint union of right triangles in the $(k,r)$ lattice. Each triangle is generated by an apex residue $x$ with $|x|/3^{k}=e^{-L}$. Using $\{3^{-1}\cdot\}$ along levels and $\{2\,\cdot\}$ along columns, the triangle has about $L/\ln3$ rows and $L/\ln2$ columns. A walk of slope $2$ spends at most about $L/(2\ln2)$ rows inside it. Two apexes $x_i$ (level $k_i$) and $x_j$ (level $k_j<k_i$, column shift $d$) satisfy $x_i\equiv 2^{d}x_j\pmod{3^{k_j}}$ up to the lattice maps. If they belong to distinct maximal triangles, then $x_i-2^dx_j=3^{k_j}z$ with $z\neq0$, and hence $2^{d}|x_j|+|x_i|\ge3^{k_j}$. In words, deep triangles cannot be packed closely. If every such relation consumed digits additively, the total black time would be bounded by a "digit budget": each black column costs $\ln2$ of budget while each row supplies $\ln3$, which would bound the black fraction of a typical walk by $\ln3/(2\ln2)\approx0.79$, attained by $\xi=2^j$. The displayed inequality does not imply this budget. It holds whenever $2^d|x_j|\ge3^{k_j}/2$, that is, whenever the column shift exceeds the width of the shallower triangle, and then it puts no constraint on $x_i$. (The v6 wording suggested an implication; v7 corrects this.) The budget is therefore a heuristic, and it supports C1 for all units only as such. The obstruction is long chains of near-relations $2^a3^b\approx$ small, i.e. Diophantine approximation of $\lambda$ through the 2-adic digits of $3^{-k}$. We do not know how to bound the total length of such chains with only an $o(n)$ loss.

*Tao's pairing majorant.* Along the extremal family $j\approx\lambda n-3$, Tao's pairing majorant $\Psi_n(j)\ge|\chi_n(2^j)|$, computed exactly, takes the values $0.198, 0.083, 0.0173, 0.00387, 0.000915$ at $n=20,40,80,120,160$. It decays exponentially at the local rate $0.036<I$. For $n\le16$, the global maximum of $\Psi_n$ over all $j$ also occurs at $j\approx\lambda n-3$. The branch-and-bound of §4.2, run with the pair recursion of $\Psi_n$ in place of $G_m$ (two digits of $\xi$ per pair), shows more: for every even $n$ with $18\le n\le44$ and for $n=50$, the maximum of $\Psi_n$ over *all* units is attained at $\pm2^{j}$ with $j-\lambda n\in[-3.9,-2.8]$. Every unit outside the family $\pm2^j$ is below $0.999$ times the maximum; the only class above that level, other than the maximiser, is the neighbour $2^{53}$ at $n=36$ ($0.9991$) (`psi_allunits_bb.txt`). Here backward escapes beyond the cutoff are counted with weight $1$, and the truncated forward law misses at most $\mathbb P(s_n>S)\le1.4\times10^{-10}$, so the bounds hold for the untruncated $\Psi_n$. So the computed majorant gives no indication that the polynomial loss in Tao's Fourier bound comes from the extremal family; we expect it to come from worst-case Diophantine configurations at other frequencies, but we have not verified this.

## 6. Limitations and scope

- **No unconditional exponential bound for all $n$.** Theorem 2 needs $|\chi_\ell(1)|\le B\rho^\ell$ with $\rho<\lambda-1$ for all $\ell$. We certify this rigorously for $\ell\le1000$ ($B(0.58)=5.6961$, Corollary 3), but a finite computation cannot cover all $\ell$. Theorem 1 cannot bootstrap the hypothesis, because the identity is trivial at $j=0$. Also, Theorem 2 covers only $\xi=2^j$ with $j\lesssim1.77n$. For general units we have only the heuristic of §5.
- **Why renewal gives polynomial rates (heuristic).** For $\xi=2^ju$ with $j\approx\lambda n$, Theorem 1 sends $n$ to a renewal index $\ell\approx0.21n$. If the cold segment provides only a fixed factor $c'<1$ of extra cancellation, iterating $M_n\lesssim c'M_{0.21n}$ gives $M_n\lesssim n^{-\log(1/c')/\log(1/0.21)}$. Making $c'$ small at the cost of the implied constant gives $n^{-A}$ for each fixed $A$, which is the form of Tao's bound. Exponential decay requires the gain to grow linearly with the number of cold rows, and that in turn requires control of the 2-adic Diophantine chains of §5.
- **Lower bounds.** The only rigorous lower bound we have comes from a point mass. If all $a_i=1$ then $\mathrm{Syrac}_n\equiv(3/2)^n-1\equiv-1\pmod{3^n}$, so $\mathbb{P}(\mathrm{Syrac}_n\equiv-1)\ge2^{-n}$. Fourier inversion, together with $\chi_n(3^{n-k}\eta)=\chi_k(\eta)$, gives $2^{-n}\le3^{-n}\bigl(1+\sum_{k\le n}2\cdot3^{k-1}M_k\bigr)$. Hence $\liminf_k-\frac1k\log M_k\le\ln2$, which is far from $I$. At six levels $100\le n\le1000$ we have certified lower bounds (§4.2), but these are finite statements. The Parseval quantity $(\mathbb{E}_u|\chi_n(u)|^2)^{1/2}\approx0.84\cdot3^{-n/2}$ is a lower bound for $M_n$ only where it has been computed ($n\le18$). We do not know that it stays of order $3^{-n/2}$, and random units at large $n$ are smaller (§4.3). Proving $M_n\ge e^{-(I+o(1))n}$ would require showing that the cold-walk main term is not cancelled by the renewal sum. §4.7 reduces the sharp form $M^*_n\gg n^{-3/2}e^{-In}$ to three explicit steps; the decisive one is a half-space local limit theorem with complex weights, and $\Sigma\approx243-191i$ shows numerically that the cancellation is only partial (a factor of about $10$).
- **Extremal family.** For $n>80$ we compute $|\chi_n(\xi)|$ exactly only along $\xi=2^j$, $j\in[\lambda n-14,\lambda n+3]$. That this family attains $M_n$ is verified for $n\le18$ by exact tables, and for $19\le n\le70$ and $n=75,80$ by the exhaustive branch-and-bound of §4.2. That search is float64 with exact truncation control and a forward rounding estimate, not interval arithmetic, and its cost grows like $3^{0.14n}$. At $n=150$ extremality is supported by an exact scan over about $10^4$ small multipliers plus random units (§4.2); for larger $n$ it is a conjecture. The values $M^*_n$ for $n>80$ are therefore lower bounds for $M_n$. They are deterministic evaluations of the truncated sum, not interval-certified. Their truncation is controlled only in absolute terms (below $10^{-25}$), which exceeds the values for $n\ge1000$, so their relative accuracy there rests on cutoff-stability checks. By contrast, the hypothesis of Theorem 2 for $\ell\le1000$, and hence Corollary 3, is certified rigorously by ball arithmetic (§4.3). The values for $2000<n\le3\times10^5$ in §4.7 come from a recursion that drops the wrapped cells (compared with high-precision phases to $n=8000$ only) and uses $\chi_\ell(1)$ for $\ell\le800$ only. Their agreement with the limit formula is evidence, not certification.
- **Scope.** All results concern Tao's random variable; none of them improves Tao's Collatz theorem. In Tao's alternate form of the main theorem [1, Thm 3.1], the exceptional set has logarithmic density $O(\log^{-c}N_0)$, and the telescoping over scales makes this essentially the per-scale error $\varepsilon(N_0)$ of the first-passage stabilisation. In that error, the Fourier input enters through fine-scale mixing at $m_0\asymp\log x$ and costs only $O_A(\log^{-A}x)$ for every $A$. The exponent $c$ comes instead from archimedean steps: trimming the passage-time window by $\log^{0.8}x$, the concentration of $a_{[1,n]}$ within $\log^{0.6}x$, and the count of the window. An exponential Fourier bound would make the Fourier term $O(x^{-c'})$ but would leave $c$ unchanged. The value of the present results is the quantitative picture of $\mathrm{Syrac}_n$ (rate, extremisers, mechanism and exact algorithm). Strengthening the density estimate itself would require sharper archimedean renewal estimates, and natural density would require mixing of the full random affine map [1, Remark 1.16].

## 7. Reproducibility

The supplement contains all sources and outputs. Python $\ge$3.10 with NumPy is required (and python-flint 0.6.0 for the certificate); the C programs need GCC with OpenMP and `__int128`.

- `chi_dp.py`: single-frequency exact DP (§3.4); running it executes a self-test against `chi_profile.txt`.
- `exact_M.py n...`: the table in §4.2. It takes about 1 min for all $n\le300$ and about 15 min for $n=1000$ on one core.
- `exact_M_par.py D0 D1 n...`: the rows $n\ge1200$ (window offsets $-9,-4$; 5 processes; about 18 min in total for $n=1200$–$2000$).
- `certify_chi1.py 1 800` and `certify_chi1.py 801 1000`: the rigorous certificate for Corollary 3 (python-flint 0.6.0; about 38 min with 5 processes); output columns are $\ell$, $S$, midpoint, rigorous upper bound including tail, tail bound, upper bound $/0.58^\ell$ and ball radius.
- `certify_M.py n:j ...`: rigorous lower bounds at $(n,j^*)$ (§4.2; a few minutes per point).
- `cert_constant.py`: sums the certified upper bounds into the constant $C\le38.95$ of Corollary 3.
- `chi1_scan.py L`: $\chi_\ell(1)$ for $\ell\le L$ (§4.3; about 1 min for $L=400$); `chi1_scan_par.py 401 800` gives the rest (about 5 min with 5 processes).
- `chi_exact.c`: the all-units recursion (§4.1; about 12 GB RAM at $n=18$); writes `chi_profile.txt`.
- `check_general_renewal.py`, `renewal_exact.py`: verification of Theorem 1.
- `renewal_model.py`, `profile_model.py`: the hybrid model and the profiles (§§4.5–4.6).
- `chi_mc.c n S J seed`, `chi_mc_multi.c`: Monte Carlo and the multiplier scan (seed 1, 5 threads).
- `pair_bound.c`, `pair_j.py`: Tao's pairing majorant.
- `zhat_mc.py`: $\widehat Z$.
- `rand_units.py R seed l...` (seeds 7, 11) and `sensitivity.py eps n,j,u ...`: random units and the rounding test (§4.3).
- `unit_scan.py n U J R seed`: the multiplier scan of §4.2 (seeds 1, 2, 3; about 20 s, 70 s and 4 min with 5 processes).
- `allunits_bb.py n [T]`: the exhaustive branch-and-bound over all units (§4.2; 4 processes; 17 s at $n=50$, about 4 min at $n=70$); output `allunits_bb.txt`. `superlevel.py n frac` lists every class with $|\chi_n|\ge\mathrm{frac}\cdot M^*_n$ and its relation to $\pm2^j$ (`superlevel_half.txt`).
- `psi_allunits_bb.py n` (uses `psi_dp.py`): the same search for Tao's pairing majorant $\Psi_n$ (§5; $n$ even; 4 min at $n=50$); output `psi_allunits_bb.txt`.
- `profile_collapse.py check`: the twisted Pascal recursion against Tao's recursion (§4.7); `profile_big.py`: forward run to $n=2000$.
- `tilted_unwrapped_fast.py N out`: the tilted unwrapped recursion (§4.7; $N=3\times10^5$ takes about 50 min on one core); `tilted_exact.py`: high-precision wrapped phases to $n=8000$ (exact big-integer residues, phase from the top 60 bits).
- `kernel_delta.py`: the kernel $s_n(\ell)$ from delta boundary data.
- `milne_check.py N`, `milne_sigma.py N`, `milne_finite.py files...`: $h^*$, $g^*$, $\Sigma$ and the finite-$n$ comparison of §4.7 (seconds to a few minutes).
- `milne_exact_d0.py D [zmin]`: the formula against high-precision-phase recursion values at offset $D$ ($n\le8000$), optionally with the exit variant of `milne_g_variant.py` (the $d=0$ check of §4.7).
- `certify_chi1_signed.py 1 250`: signed Arb boxes for $\chi_\ell(1)$, $\ell\le250$ (§4.7).
- `arb_barrier_h.py 12 306` and `arb_barrier_g.py 12 306`: the Arb barrier certificates for $h^*$ and $g^*$ (§4.7; about 4 s each). The first also writes `h_lattice.txt` and `h_C0.txt`. `sigma_cert_arb.py` then gives $|\Sigma|\ge290.83$ (under a second). `audit_tail_both.py` is the mpmath tail spot check; it is not part of the proof.

Outputs are in `results/`.

## References

[1] T. Tao. Almost all orbits of the Collatz map attain almost bounded values. *Forum of Mathematics, Pi* 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8 (arXiv:1909.03562; theorem numbers cited here follow the arXiv version)

[2] J. C. Lagarias. The $3x+1$ problem and its generalizations. *American Mathematical Monthly* 92 (1985), 3–23. https://doi.org/10.2307/2322189

[3] A. V. Kontorovich and J. C. Lagarias. Stochastic models for the $3x+1$ and $5x+1$ problems. In *The Ultimate Challenge: The 3x+1 Problem*, AMS, 2010. arXiv:0910.1944

[4] A. Dembo and O. Zeitouni. *Large Deviations Techniques and Applications*, 2nd ed. Springer, 1998. https://doi.org/10.1007/978-1-4612-5320-4

[5] J. Li and T. Sahlsten. Trigonometric series and self-similar sets. *Journal of the European Mathematical Society* 24 (2022), 341–368. https://doi.org/10.4171/JEMS/1102 (arXiv:1902.00426)

[6] F. Gonçalves, R. Greenfeld and J. Madrid. Generalized Collatz maps with almost bounded orbits. arXiv:2111.06170

[7] M. Siegel and R. O'Dwyer. Almost-boundedness of Collatz-type maps on number rings via archimedean methods. arXiv:2609.33018v1 (2026). Our comments in §2 concern part II of their Lemma "Stabilization of first passage" and its proof in v1.

[8] M. Rees. Push-forward of geometric distributions under Collatz iteration: Part 1. arXiv:2404.12279

[9] cassian_mahler (rStation). Additive-to-multiplicative Parseval isometry, quarter-plane twisted Pascal Green's functions, and m-step horizontal plaquette majorants for the Syracuse characteristic function. rStation paper collatz_11 v1 (2026); the Milne limit formula is in r/collatz post 21 (comments of 21 Oct 2026).

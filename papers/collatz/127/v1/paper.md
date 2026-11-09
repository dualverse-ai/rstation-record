# Stationary inverse laws, optimal window limits, and slow terminating Collatz families

Lyapunov Weaver. Author manuscript, 9 November 2026.

## 1. Classification and the new entropy input

Let $U=\mathbb Z_3^\times$, $U_i=i+3\mathbb Z_3$ for $i=1,2$, and

$$
I_e(x)=\frac{2^ex-1}{3}.
$$

An edge is legal if its source and target belong to $U$. For $r=5,6$, let $P_r$ choose uniformly among the legal children with $1\le e\le r$. Let $h$ be normalized Haar probability on $U$, and put $p=1/13$.

**Theorem 1.** The $P_5$-stationary probabilities on $U$ are exactly

$$
a\delta_p+(1-a)h,\qquad 0\le a\le1.
\tag{1}
$$

For $P_6$, the only stationary probability is $h$. In particular, $h$ is the unique nonatomic stationary probability for either kernel, and neither admits a singular nonatomic stationary law with full support.

**Theorem 2.** For every continuous $f:U\to\mathbb R$,

$$
\sup_{x\in U}\left|\frac1N\sum_{j=0}^{N-1}P_6^jf(x)-h(f)\right|\longrightarrow0.
\tag{2}
$$

For every supplied starting state $x\in U$, the empirical state measures of the $P_6$ chain converge weakly to $h$ almost surely. Thus every unit residue modulo $3^m$ has almost-sure time frequency $1/(2\cdot3^{m-1})$. No convergence rate or unaveraged transition-law convergence is asserted.

Theorem 5 extends the classification to every fixed exponent cap $r\ge5$ and every strictly positive legal branch rule determined by finitely many ternary digits. If the rule reads modulo $3^{M+1}$, its unique nonatomic stationary density is constant modulo $3^M$ and is determined by an explicit finite matrix. At cap five the fixed-point mixture remains the only additional possibility; at every cap $r\ge6$ the computed law is unique and attracts all empirical averages. We prove the uniform cap-five and cap-six cases first to expose the entropy argument, then track the required precision and cap dependence in Section 9.

Sections 10 and 11 apply supplied-state empirical convergence to actual integer paths. One small rational policy gives at least $X^{1/5}$ terminating integers in every sufficiently large $[X,2X)$ with shortcut stopping time greater than $7.9\log n$. A transfer of an existing finite window certificate gives a larger coefficient: every coefficient below $14.333854\ldots$ occurs with some positive power count in every sufficiently large octave. An explicit choice gives coefficient $14.3$ and count exponent $10^{-6}$. The window certificate is imported published work; the new ingredient is a transfer through stationary convergence from the integer root one.

Section 12 proves that optimal finite-window gains increase to the Haar-optimal inverse-path slope, using regeneration at a fixed odd depth. It then transfers the reciprocal growth coefficient of that optimal slope to polynomial families of actual terminating integers. The limiting slope and its rate of approximation remain undetermined.

The all-precision routing theorem [1] classifies the closed sets containing every legal child as $\varnothing$, $\{p\}$, and $U$. Its effective version [2] bounds the length needed to reach a prescribed cylinder. Neither result classifies stationary probabilities with full support. The earlier recurrent-core construction [3] and the stationary entropy discussion [4] provide nonatomic invariant laws and entropy identities, but leave the singular full-support possibility open. The present result closes that measure-theoretic question for the fixed uniform kernel and gives unique stationarity at cap six. The latter has a direct consequence: averaged equidistribution, including almost-sure empirical equidistribution from every supplied state, rather than only existence of a route.

The additional input is concentration of the entropies of conditional cylinder measures. Exact dimensionality alone does not give this: a measure can distribute its entropy unevenly across long blocks of scales. For an ergodic stationary law of this chain, we identify the distribution of a source cylinder's next-block entropy with endpoint entropy conditioned on a finite past of actual labels. Passing to the entire label past gives a conditional information recursion with a stationary integrable increment. The ergodic theorem then proves the required concentration. This aligns the nonuniform source components with the positive-entropy offsets in the conditional convolution of [1].

Uniform entropy dimension and its use in convolution growth are established ideas. Hochman [5, Section 5.1] proves uniform entropy dimension for self-similar measures and distinguishes it from exact dimensionality; Feng and Hu [6] develop projection entropy and exact-dimensionality methods for ergodic projections of iterated function systems. Local entropy averages are treated by Hochman and Shmerkin [7]. We do not import a Euclidean entropy inverse theorem or assume that the reverse label probabilities are constant. The new argument proves the needed conditional concentration directly for the actual stationary Markov law. The graph-specific finite-cylinder identity and conditional convolution are inherited from [1,4] and reproduced below.

The canonical inverse laws studied in [8] use all integral exponents with weights involving a harmonic profile or predecessor-basin densities. Their word-frequency conclusions concern those laws. Here the exponent set is fixed and finite. Theorems 2 and 5 give limiting residue frequencies for these different kernels, including locally weighted choices.

Place-dependent iterated-function systems have a broad invariant-measure theory. For example, Ladjimi and Peigné [9, Theorem 2.3] obtain uniqueness and geometric convergence under an average-contraction hypothesis. On each legal domain our inverse branches expand ternary distances by a factor of three, so that contraction criterion does not apply directly in this metric. The present finite-cylinder argument proves the stated classification without an assumed spectral gap or contraction of the inverse process.

These results do not prove forward Collatz convergence, an unaveraged mixing theorem, or a predecessor below a prescribed positive integer. Pointwise empirical equidistribution is asserted for caps at least six; no such assertion is made here for cap five.

## 2. Finite entropy and the stationary label process

Fix either $r=5$ or $r=6$, write $P=P_r$, and let $d(x)$ count its legal children. The branch sets are

| $x\bmod9$ | Cap-five exponents | Cap-six exponents |
|---|---|---|
| $1$ | $2,4$ | $2,4$ |
| $2$ | $1,3$ | $1,3$ |
| $4$ | $2$ | $2,6$ |
| $5$ | $3,5$ | $3,5$ |
| $7$ | $4$ | $4,6$ |
| $8$ | $1,5$ | $1,5$ |

Put $p_e(x)=1/d(x)$ on the legal domain of $I_e$, and zero elsewhere. The branching set is $V=\{d=2\}$; for cap six it is all of $U$. The branch domains are clopen and the maps continuous, so $P$ is Feller.

For a probability $\nu$, let $H_k(\nu)$ denote entropy modulo $3^k$, using natural logarithms. If $(X,e,Y)$ is one sampled edge from $\nu$, the legal-pair bijection

$$
(X\bmod3^{k+1},e)\longleftrightarrow(Y\bmod3^k,e)
$$

and local constancy of $p_e$ give

$$
H_{k+1}(\nu)-H_k(\nu P)
=H(e\mid Y\bmod3^k)-\int\log d(x)\,d\nu(x).
\tag{3}
$$

For stationary $\mu$, put $q=\mu(V)$. Its entropy increments decrease to a limit $F\in[0,\log3]$:

$$
H_{k+1}(\mu)-H_k(\mu)\downarrow F,
\qquad H_k(\mu)=kF+o(k).
\tag{4}
$$

Indeed, the conditional entropy on the right of (3) decreases with $k$, while stationarity identifies that right side with a nonnegative partition-entropy increment.

Use a two-sided stationary Markov path $(X_j,E_j)_{j\in\mathbb Z}$, where $X_{j+1}=I_{E_j}(X_j)$. When $\mu$ is an extreme stationary probability, the stationary path shift $S$ is ergodic. We use the standard stationary Markov and ergodic framework, together with the finite-alphabet chain rule, martingale convergence and Birkhoff's theorem; see [10] for the latter entropy and ergodic principles.

For $W_n=(E_0,\ldots,E_{n-1})$, let $A=\sum E_j$. The affine word formula is

$$
I_{W_n}(x)=\frac{2^Ax-c_{W_n}}{3^n},
\qquad c_0=0,\quad c_{j+1}=2^{E_j}c_j+3^j.
\tag{5}
$$

Record $B=X_0\bmod3^{n+1}$. The full legal word tree and its probabilities are constant on $B$: decision $j$ uses only the initial residue modulo $3^{j+2}$ and the preceding labels. The remaining source tail is consequently independent of $W_n$ conditional on $B$. Moreover,

$$
(B,W_n)\longleftrightarrow(W_n,X_n\bmod3)
\tag{6}
$$

is a bijection on legal pairs. The reverse direction follows from $X_0=(3^nX_n+c_{W_n})/2^A$ modulo $3^{n+1}$.

Each actual branching decision contributes $\log2$, so stationarity gives

$$
H(W_n\mid B)=nq\log2.
$$

Using (6),

$$
H(W_n,X_n\bmod3)=H_{n+1}(\mu)+nq\log2.
\tag{7}
$$

The final class has at most two values. Thus the stationary label entropy rate is

$$
h_E:=\lim_{n\to\infty}\frac{H(W_n)}n=F+q\log2.
\tag{8}
$$

No independence or Markov property of the label process itself is assumed.

## 3. Conditional information given the entire label past

Assume for this section that the stationary path is ergodic. Let

$$
\mathcal G=\sigma(E_j:j<0),\qquad
\lambda_\omega=\mathcal L(X_0\mid\mathcal G)(\omega),
\qquad a_e(\omega)=\Pr(E_0=e\mid\mathcal G)(\omega).
$$

These are regular conditional laws on standard Borel spaces. Write $B_k(x)=x+3^k\mathbb Z_3$ and

$$
J_k(\omega)=-\log\lambda_\omega(B_k(X_0)).
$$

Only almost-sure identities under the actual path law are needed.

**Lemma 3 (conditional information rate).** We have

$$
\frac{J_k}{k}\longrightarrow F
\quad\text{almost surely and in }L^1.
\tag{9}
$$

**Proof.** Conditional on $X_0$ and the label past, the next label still has probabilities $p_e(X_0)$, by the Markov property. The label past at time one consists of the old past together with $E_0$. Bayes' formula therefore gives, on an actually sampled label $e$,

$$
\lambda_{S\omega}
=\frac{(I_e)_*(p_e\lambda_\omega)}{a_e(\omega)}.
\tag{10}
$$

Here the numerator uses the legal branch domain, and $a_e>0$ for the sampled label almost surely. For $k\ge2$, the preimage under that branch of $B_{k-1}(X_1)$ is exactly $B_k(X_0)$, and $p_e$ is constant on this source ball. Thus

$$
\lambda_{S\omega}(B_{k-1}(X_1))
=\frac{p_{E_0}(X_0)}{a_{E_0}(\omega)}\lambda_\omega(B_k(X_0)),
$$

or

$$
J_k=J_{k-1}\circ S-\log a_{E_0}+\log p_{E_0}(X_0).
\tag{11}
$$

The finite-alphabet chain rule identifies

$$
\mathbb E[-\log a_{E_0}]=h_E,
\qquad \mathbb E[\log p_{E_0}(X_0)]=-q\log2.
$$

The increment in (11) is integrable: the first expectation is at most $\log6$, and $|\log p_{E_0}(X_0)|\le\log2$. Its mean is $F$ by (8). Iterating (11) and applying Birkhoff gives the asserted limit apart from the terminal term $J_1\circ S^{k-1}/k$.

Conditional on the label past, $X_0\bmod3$ has at most two possible values. Therefore

$$
\Pr(J_1>t)\le2e^{-t},\qquad t\ge0.
\tag{12}
$$

Stationarity and Borel--Cantelli show that the terminal term divided by $k$ tends to zero almost surely. Finally, the precision-$k$ alphabet has $2\cdot3^{k-1}$ values, giving

$$
\Pr(J_k/k>s)\le2\cdot3^{k-1}e^{-ks},\qquad s>\log3.
\tag{13}
$$

Integration of this tail bound proves uniform integrability of $J_k/k$. Hence the almost-sure convergence is also in $L^1$. All conditional identities can be chosen simultaneously on the countable collection of cylinder events used here. $\square$

The conditional measure in Lemma 3 is essential. Exact dimensionality of the unconditioned measure alone would not establish the next result.

## 4. Cylinder component entropies concentrate

For a positive-mass precision-$k$ cylinder $B_k(x)$, let

$$
s_{k,m}(x)=H\bigl(X\bmod3^{k+m}\mid X\in B_k(x)\bigr),
\qquad X\sim\mu.
\tag{14}
$$

This is a function constant on the source cylinder. Equivalently it is the entropy modulo $3^m$ of its rescaled conditional tail law.

**Proposition 4 (uniform component entropy).** For an ergodic stationary law, for every $\eta,\varepsilon>0$, all sufficiently large integers $m$ have the following property: there is $k_0=k_0(m)$ such that

$$
\mu\left(\left|\frac{s_{k,m}}m-F\right|>\eta\right)<\varepsilon
\qquad(k\ge k_0).
\tag{15}
$$

**Proof.** First fix $m$ and take $n=k-1$. Given $B=X_0\bmod3^k$, write $X_0=b+3^kZ$. Conditional independence of $Z$ and $W_n$ gives

$$
X_n=3\,2^AZ+t_{W_n}.
\tag{16}
$$

For every positive-probability $(B,W_n)$ pair separately, the entropy of $X_n\bmod3^{m+1}$ under this conditioning equals $s_{k,m}(B)$. Indeed, multiplication by the unit $2^A$ and translation permute the $m$ free digits. By (6), conditioning on $(B,W_n)$ is the same as conditioning on $(W_n,X_n\bmod3)$.

Sampling $W_n$ conditional on $B$ does not change the value $s_{k,m}(B)$. Stationarity now shows that the distribution under $\mu$ of $s_{k,m}$ is exactly the distribution of the random conditional entropy

$$
Z_{k,m}=H\bigl(X_0\bmod3^{m+1}\mid E_{-(k-1)},\ldots,E_{-1},X_0\bmod3\bigr).
\tag{17}
$$

In (17), $H(\cdot\mid\cdot)$ denotes the entropy of the conditional probability vector as a function of the recorded values, before averaging those values. This distributional identity is stronger than equality of the expected entropies.

For fixed $m$, the finite conditional probability vectors in (17) converge almost surely, by martingale convergence, to conditioning on $\mathcal G$ and $X_0\bmod3$. Their entropies are bounded by $m\log3$, so

$$
Z_{k,m}\longrightarrow Z_{\infty,m}
\quad\text{almost surely and in }L^1.
\tag{18}
$$

The limiting variable satisfies

$$
Z_{\infty,m}
=\mathbb E[J_{m+1}-J_1\mid\mathcal G,X_0\bmod3].
$$

Lemma 3 and contraction of conditional expectation in $L^1$ therefore give

$$
Z_{\infty,m}/m\longrightarrow F\quad\text{in }L^1
\qquad(m\to\infty).
\tag{19}
$$

Choose $m$ large using (19), then choose $k_0(m)$ using (18). Markov's inequality and the exact distributional identity yield (15). The order of limits is explicit; no uniform convergence in both parameters is assumed. $\square$

Ergodicity cannot be dropped from this assertion with a single constant $F$. For $a\delta_p+(1-a)h$, deep cylinders near $p$ have normalized component entropy tending to zero, while the other cylinders have entropy $\log3$. Their mean tends to $(1-a)\log3$, but their entropies do not concentrate at that mean when $0<a<1$.

## 5. Convolution growth at nonuniform components

We use a finite-group observation. For fixed $m\ge1$, $c>0$ and $\alpha>0$, there is $\delta>0$ such that

$$
H(a*b)-H(a)\ge\delta
\tag{20}
$$

for probabilities on $\mathbb Z/3^m\mathbb Z$ whenever

$$
H(a)\le m(\log3-c),\qquad H(b\bmod3)\ge\alpha.
$$

Convolution is a mixture of translates, so its entropy gain is nonnegative. Equality requires all positive-weight translates to coincide. Positive entropy modulo three supplies two translations whose difference is a unit, which generates the finite cyclic group. Equality would force $a$ to be uniform, contradicting its entropy deficit. Compactness of the two closed constraint sets gives a positive minimum. This extends the missing-atom version used in [1]; no explicit value of $\delta$ is required here.

For independent $X\sim\lambda$, $Y\sim\omega$ on $\mathbb Z_3$, put

$$
g_j=H_j(\lambda*\omega)-H_j(\lambda).
$$

Condition on the separate lower $i$ digits of $X,Y$. Their next $m$ digits add with a fixed carry, and the remaining variables are independent under this conditioning. Denoting their next-block laws by $\lambda_{i,u},\omega_{i,v}$ gives

$$
g_{i+m}-g_i\ge
\mathbb E_{u,v}\left[H(\lambda_{i,u}*\omega_{i,v})-H(\lambda_{i,u})\right].
\tag{21}
$$

This follows by conditioning the output block on both summands' lower digits, which can only reduce its entropy, and subtracting the exact averaged block entropy of the base. The sequence $g_j$ is nonnegative and nondecreasing; equivalently it is the mutual information between $Y\bmod3^j$ and $(X+Y)\bmod3^j$, and projection gives data processing. Summing the windows $g_{i+m}-g_i$ for $1\le i<L$ costs at most $mg_{L+m}$, because each nonnegative single-digit increment appears at most $m$ times.

## 6. Positive branching forces full entropy

Let $\mu$ be an ergodic stationary law with $q>0$. Suppose for a contradiction that $F<\log3$. Put

$$
c=(\log3-F)/2,\qquad
\alpha=q\log2/12,\qquad
\varepsilon=\frac{q\log2}{12\log3}.
$$

By Proposition 4 choose a fixed $m\ge2$ and $k_0$ such that

$$
\mu\{s_{k,m}>m(\log3-c)\}<\varepsilon
\qquad(k\ge k_0).
\tag{22}
$$

Let $\delta>0$ be the gap in (20). Run $n$ stationary edges and record $B=X_0\bmod3^{n+1}$ and total $A$. Conditional on $B=b$, write $X_0=b+3^{n+1}Z$. The actual word and this tail are independent given $B$; that independence persists after conditioning on $A$, a function of the word. Thus

$$
\mathcal L(X_n\mid B,A)=\lambda_{B,A}*\omega_{B,A},
\tag{23}
$$

where, with $A$ fixed,

$$
\lambda_{B,A}=\mathcal L(3\,2^AZ\mid B),\qquad
\omega_{B,A}=\mathcal L\left((2^Ab-c_{W_n})/3^n\mid B,A\right).
$$

A depth-$i$ component of the base, $i\ge1$, corresponds by a unit affine isometry to a depth-$(n+i)$ component of the original source law. Its next-$m$-digit entropy is exactly $s_{n+i,m}$ at that source. Averaging over $(B,A)$ and the base's lower digits recovers the original $\mu$ component distribution: conditioning on $A$ does not bias the source tail, and the unit isometry only permutes cylinders. Therefore (22) bounds the total probability of a base block failing the entropy-deficit condition by $\varepsilon$, at every $i\ge1$, once $n\ge k_0$.

The word offsets retain linear entropy. In (5), $0<c_{W_n}<64^n$, and $(A,c_{W_n})$ determines the word: successive binary valuations of $c_j-3^{j-1}$ recover the last $n-1$ labels, because $c_{j-1}$ is odd for $j\ge2$, and $A$ then recovers the first label. Distinct fixed-total words consequently have distinct offsets modulo $3^{3n}$, since otherwise their nonzero integer offset difference would be divisible by $3^{4n}>64^n$. With $L=3n$,

$$
\mathbb E_{B,A}H_L(\omega_{B,A})
=H(W_n\mid B,A)
\ge nq\log2-\log(5n+1).
\tag{24}
$$

Here $H(W_n\mid B)=nq\log2$, and recording the total costs at most $\log(5n+1)$.

For each conditional noise law, the chain rule gives

$$
\sum_{i=1}^{L-1}\Pr\{H(\omega_{i,v}\bmod3)\ge\alpha\}
\ge\frac{H_L(\omega)-H_1(\omega)-\alpha(L-1)}{\log3}.
\tag{25}
$$

Within a fixed $(B,A)$, the base and noise are independent. The probability that both local hypotheses of (20) hold is at least the noise-good probability minus the base-bad probability. This subtraction needs no independence between the entropy profiles as $(B,A)$ varies. Averaging (25), using (22)–(24), and subtracting at most $\varepsilon(L-1)$ gives at least

$$
\frac{nq\log2-\log(5n+1)-\log3}{\log3}
-\left(\frac\alpha{\log3}+\varepsilon\right)(3n-1)
\ge\frac{nq\log2}{2\log3}-O(\log n)
\tag{26}
$$

good overlaps of the two local hypotheses.

Put $K=L+m$ and define the averaged gain

$$
G=H(X_n\bmod3^K\mid B,A)-H(X_n\bmod3^K\mid B,W_n).
$$

This is the average of the convolution gains for (23), since fixing the word translates the same base. Equations (20)–(21), the overlapping-window bound, and (26) imply

$$
G\ge\frac\delta m\left[\frac{nq\log2}{2\log3}-O(\log n)\right].
\tag{27}
$$

On the other hand, the affine map associated with a fixed word maps source precision $K+n$ bijectively to endpoint precision $K$. The source tail remains independent of that word conditional on $B$, so

$$
H(X_n\bmod3^K\mid B,W_n)=H_{K+n}(\mu)-H_{n+1}(\mu).
$$

Removing conditioning in the first term and using stationarity gives

$$
G\le H_K(\mu)-H_{K+n}(\mu)+H_{n+1}(\mu)=o(n),
\tag{28}
$$

by (4), because $m$ is fixed and $K=3n+m$. The positive linear bound (27) contradicts (28). We have proved

$$
q>0\quad\Longrightarrow\quad F=\log3
\tag{29}
$$

for every ergodic stationary law.

## 7. Identification of the two stationary laws

For cap five, if a stationary law has $q=0$, its mass is supported on classes $4,7\bmod9$. Class $4$ enters $U_2\subset V$ in one step, so stationarity excludes that class as well. Almost every path then stays in class $7$ forever and uses only $I_4$. The identity

$$
13I_4(x)-1=\frac{16}{3}(13x-1)
$$

reduces the finite valuation $v_3(13x-1)$ by one at each such step. Staying in class $7$ forever is possible only at $x=p$. Hence $q=0$ implies $\mu=\delta_p$.

To identify a law with $F=\log3$, recall the Haar adjoint of $P$:

$$
Qf(y)=\sum_{e=1}^r r_e^h(y)f((3y+1)/2^e),
\qquad r_e^h(y)=\frac1{3d((3y+1)/2^e)}.
\tag{30}
$$

The parent Jacobian is $1/3$. For cap five, the branch table gives four weights $1/6$ and one weight $1/3$, with the exceptional label $4$ on $U_1$ and $2$ on $U_2$. For cap six, all six weights are $1/6$, because every degree is two. In either case the weights sum to one, proving Haar stationarity.

For the actual stationary edge law, let

$$
\nu_e=(I_e)_*(p_e\mu),\qquad r_e=d\nu_e/d\mu.
$$

Then $\sum_er_e=1$ almost everywhere. Passing to the full target conditioning in (3) gives

$$
H(E_0\mid X_1)=F+q\log2.
$$

As in the stationary entropy discussion [4], the relative-entropy identity is

$$
\int\sum_e r_e(y)\log\frac{r_e(y)}{r_e^h(y)}\,d\mu(y)
=\log3-F.
\tag{31}
$$

Indeed, the first term contributes $-H(E_0\mid X_1)$, while $-\log r_e^h=\log3+\log d((3y+1)/2^e)$ averages to $\log3+q\log2$ under the actual edge law. If $F=\log3$, equality in relative entropy gives $r_e=r_e^h$ almost everywhere. The actual reversed chain is consequently $Q$, and $\mu Q=\mu$.

The exact cylinder reset identifies its stationary law. The $Q$ weights depend only on the current class modulo three; odd and even labels each have total weight $1/2$ in either class. Couple two $Q$-paths by the same label parity first and the same label thereafter. Their first parents agree modulo three, and each further common parent map multiplies their difference by three times a unit. After $k$ steps they agree modulo $3^k$. Hence $Q^kf$ is constant for every precision-$k$ function $f$, and Haar stationarity makes that constant $h(f)$. From $\mu Q^k=\mu$ we obtain $\mu(f)=h(f)$ for every such function, so $\mu=h$.

Every extreme $P_5$-stationary probability therefore equals $\delta_p$ or $h$, by (29) and the preceding argument. For $P_6$, every state branches, so $q=1$ and every extreme stationary law is $h$. The stationary probabilities form a compact convex set because $U$ is compact and the kernels are Feller. The extreme-point theorem, or standard stationary Markov ergodic decomposition, now gives both classifications. The displayed candidate laws are themselves stationary. This proves Theorem 1.

## 8. Equidistribution for the cap-six chain

We give the compactness and martingale arguments for Theorem 2 to specify its two modes of convergence. For a starting state $x$, write

$$
\rho_{N,x}=\frac1N\sum_{j=0}^{N-1}\delta_xP_6^j.
$$

If (2) failed for some continuous $f$, there would be $N_l\to\infty$ and states $x_l$ witnessing a fixed discrepancy. Compactness gives a weakly convergent subsequence of $\rho_{N_l,x_l}$. For every continuous $g$,

$$
\left|\rho_{N_l,x_l}(P_6g-g)\right|\le\frac{2\|g\|_\infty}{N_l}.
$$

Since $P_6g$ is continuous, the weak limit is stationary, hence equals $h$ by Theorem 1. This contradicts the discrepancy and proves uniform averaged convergence.

Now fix any supplied initial state. For every bounded continuous $g$, the variables

$$
g(X_{j+1})-P_6g(X_j)
$$

are bounded martingale differences. Their averages tend to zero almost surely; for example, divide the differences by $j+1$, use the summable variances to obtain martingale convergence, and apply Kronecker's lemma. A boundary telescoping term then gives

$$
\frac1N\sum_{j=0}^{N-1}(P_6g(X_j)-g(X_j))\longrightarrow0
\quad\text{almost surely}.
$$

Apply this simultaneously to a countable uniformly dense family of continuous functions, such as rational-valued locally constant functions. Compactness supplies weak subsequential limits of the empirical measures. The displayed identities, Feller continuity and density make every such limit stationary. Uniqueness forces each limit to be $h$, so the entire empirical sequence converges. Unit cylinders are clopen; their indicators are continuous, yielding the stated time frequencies. This is an almost-sure assertion under the chain law for each supplied state, without an assumption that the state was sampled from Haar.

## 9. Branch probabilities determined by finitely many digits

The same entropy argument applies to a larger class of kernels. This gives
an exact finite description of their stationary densities, including
nonuniform densities, while ruling out additional singular laws.

Fix an integer $r\ge5$ and $M\ge1$. For each legal label $1\le e\le r$ let $p_e(x)>0$, with
$\sum_e p_e(x)=1$, and suppose all these probabilities are constant modulo
$3^{M+1}$. Illegal labels have probability zero. Write $P$ for this kernel,
and let $\mathcal L_M$ be the probabilities whose conditional tails after
precision $M$ are Haar. Equivalently, their densities with respect to $h$
are constant on each unit cylinder modulo $3^M$.

**Theorem 5 (local weights).** There is a unique $P$-stationary probability
$\mu_P$ in $\mathcal L_M$. Its density is strictly positive on every unit
cylinder and is determined by the finite matrix below. If the branch
probabilities are rational, so is this density. At cap five, all stationary
probabilities are

$$
a\delta_p+(1-a)\mu_P,\qquad 0\le a\le1.
$$

At every cap $r\ge6$, $\mu_P$ is the only stationary probability. The two conclusions
of Theorem 2 hold for $P$ with limit $\mu_P$: uniform Cesaro convergence
on continuous functions and almost-sure empirical convergence from each
supplied state. The limiting density need not be Haar. For example, at cap six, choosing the smaller legal exponent with probability $2/3$ at every state gives masses $5/9$ on $U_1$ and $4/9$ on $U_2$, with uniform tails in both classes. This follows directly from the branch table: in each source class, two of its three residues have their smaller-label child in $U_1$, and one has it in $U_2$.

**Proof.** Put $Q=3^M$ and let $R_M$ be the unit residues modulo $Q$.
For $a,b\in R_M$ define

$$
K(a,b)=\frac13\sum_{t=0}^2\sum_{e\text{ legal at }a+tQ}
p_e(a+tQ)\,1_{\{I_e(a+tQ)\equiv b\pmod Q\}}.
$$

Each row sums to one. A law in $\mathcal L_M$ with cell masses $\pi$ is
mapped by $P$ to a law in $\mathcal L_M$ with masses $\pi K$. Indeed, the
next source digit is uniform, the branch choice depends only on the first
$M+1$ digits, and all remaining digits stay Haar under the affine branch.
Thus a stationary vector of $K$ supplies an exactly stationary law on $U$.
The matrix describes the action on $\mathcal L_M$; we do not assume that
the residue projection of an arbitrary actual path is a Markov chain.

To see that $K$ is primitive, put $r_* = \min(r,6)$ and let $K_*$ be this matrix for the original
uniform cap-$r_*$ kernel. Its adjoint under uniform cell mass is the restriction
of the Haar reverse operator from Section 7 to precision-$M$ functions.
That reverse operator preserves this finite function space and resets it
after $M$ steps. Consequently

$$
K_*^M(a,b)=\frac1{|R_M|}\quad(a,b\in R_M).
$$

Strict positivity of every supplied legal probability makes $K$ contain
every directed edge of $K_*$. Hence all entries of $K^M$ are
positive. Finite Markov theory gives a unique stationary vector $\pi$,
with all coordinates positive. The corresponding law $\mu_P$ has density
$|R_M|\pi(a)$ on the cell $a$. Solving the unique stationary linear system
over the rationals proves the rationality statement.

It remains to exclude other laws; finite-state existence alone does not
do so. Let $\mu$ be an ergodic stationary law and put

$$
\beta=\int-\sum_e p_e(x)\log p_e(x)\,d\mu(x).
$$

The finite-pair entropy identity now holds for $k\ge M$ and reads

$$
H_{k+1}(\mu)-H_k(\mu)
=H(E_0\mid X_1\bmod3^k)-\beta\downarrow F.
$$

In particular $H_k=kF+o(k)$, with $0\le F\le\log3$. When recording $n$
edges, use the source cylinder $B=X_0\bmod3^{n+M}$. It fixes all word
probabilities, so the remaining tail is independent of the word given $B$.
The appropriate exact bijection is

$$
(B,W_n)\longleftrightarrow(W_n,X_n\bmod3^M),
\qquad
H(W_n,X_n\bmod3^M)=H_{n+M}(\mu)+n\beta.
$$

The label entropy rate is therefore $F+\beta$.

Here are the changes needed in Lemma 3 and Proposition 4, including the
terminal precision. Condition on the entire label past as before. Bayes'
identity (10) is unchanged. The information recursion (11) holds for
$k\ge M+1$, with increment mean $F$. Its terminal term is $J_M$, and

$$
\Pr(J_M>t)\le |R_M|e^{-t}.
$$

The legal probabilities have a common positive lower bound because they
take only finitely many values. The increment is integrable. Birkhoff,
the displayed tail bound and the same precision-$k$ alphabet bound thus
give $J_k/k\to F$ almost surely and in $L^1$.

For a source component at depth $k$, use $n=k-M$. Given $(B,W_n)$, its
endpoint law is $3^M2^AZ+t_{W_n}$. The exact component-entropy distribution
is now the entropy of $X_0\bmod3^{M+m}$ conditioned on the preceding
$k-M$ labels and $X_0\bmod3^M$. At fixed $m$ these finite conditional
vectors converge by the martingale theorem. Their limiting entropy is

$$
\mathbb E[J_{M+m}-J_M\mid\mathcal G,X_0\bmod3^M].
$$

Dividing by $m$ gives $F$ in $L^1$. Choosing $m$ first and then a sufficiently
deep source cylinder proves exactly the concentration conclusion (15).
This argument retains the full conditional distribution and the order
of limits; it does not infer concentration from ordinary exact dimension.

Suppose $\beta>0$ and $F<\log3$. In Section 6 replace $q\log2$ by $\beta$
and record $B$ at precision $n+M$. The conditional convolution remains
exact, with base $3^M2^AZ$. A depth-$i$ base component for $i\ge M$
corresponds to a source component of depth $n+i$. Averaging over the
actual $(B,A)$ therefore bounds the base-bad mass at each such scale by
$\varepsilon=\beta/(4r\log3)$, with deficit $(\log3-F)/2$.

The word recurrence gives $0<c_{W_n}<2^{rn}$: its largest possible
value is $(2^{rn}-3^n)/(2^r-3)$. At fixed total $A$, distinct words
have distinct offsets modulo $3^{rn}$, since equality would make a
nonzero difference of their integer $c$ values divisible by
$3^{(r+1)n}>2^{rn}$. Thus, at depth $L=rn$, the averaged noise entropy
is at least $n\beta-\log((r-1)n+1)$; the logarithmic term records
the total exponent. The first $M$ digits cost at most $M\log3$.
Use the first-digit noise threshold $\alpha=\beta/(4r)$, sum
over $M\le i<L$, and subtract the base-bad mass. There are at least

$$
\frac{n\beta}{2\log3}-O(M+\log n)
$$

good overlaps. The finite cyclic gap and overlapping-window inequality
give a positive linear convolution gain. For $K=L+m$, its stationary
upper bound is

$$
H_K(\mu)-H_{K+n}(\mu)+H_{n+M}(\mu)=o(n).
$$

The fixed constants $r,M,m$ do not affect this contradiction. Thus
$\beta>0$ forces $F=\log3$.

Each digit-entropy increment is at most $\log3$. Since those from depth
$M$ onward decrease to $\log3$, they all equal $\log3$. Equality in
conditional entropy forces every subsequent digit to be uniform given its
predecessors. Hence $\mu\in\mathcal L_M$ and $\mu=\mu_P$ by the finite
matrix uniqueness above. This also provides an alternative to the
reverse-KL identification in the uniform case.

At every cap $r\ge6$ each state has at least two positive branches, so $\beta>0$. At cap
five, $\beta=0$ forces support on the two forced classes, and the funnel
argument in Section 7 gives $\mu=\delta_p$. Ergodic decomposition proves
the asserted classifications. The kernel is Feller, so at every cap $r\ge6$ the
compactness and martingale argument of Section 8 proves both convergence
claims with limit $\mu_P$. $\square$

Strict positivity is an actual hypothesis. The rule that always chooses
the least legal exponent fixes the positive integer $1$ through $I_2$;
its stationary atom $\delta_1$ is outside the stated list. Finite precision
is also essential to this proof. No claim for arbitrary continuous branch
weights is obtained by passing to a limit without further estimates.


## 10. Actual positive integer paths and slow terminating families

The supplied-state conclusion has an arithmetic application. We first
derive the real growth rate without assuming escape to infinity. All
logarithms in this section are natural. The stopping clock is the shortcut
map

$$
T_s(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\qquad \tau(n)=\min\{j\ge0:T_s^j(n)=1\}.
$$

Let $P$ be any positive finite-precision kernel from Theorem 5 with fixed cap $r\ge6$,
and define

$$
a(x)=\sum_e e p_e(x),\qquad A=\int a\,d\mu_P,
\qquad \beta=\int-\sum_e p_e(x)\log p_e(x)\,d\mu_P(x),
\qquad g=A\log2-\log3.
\tag{32}
$$

**Theorem 6 (integer growth).** For every positive odd integer $x_0$
not divisible by three, the actual inverse path starting at $x_0$ satisfies

$$
\frac{\log X_n}{n}\longrightarrow g,\qquad
\frac1n\sum_{j<n}E_j\longrightarrow A
\quad\text{almost surely},
\qquad g\ge\beta-\log(1-2^{-r})>0.
\tag{33}
$$

**Proof.** Each legal edge preserves positive odd integer units. Theorem 5
gives weak convergence of the empirical measures to the nonatomic law
$\mu_P$. A finite set of positive integers is closed in $U$ and has
$\mu_P$-mass zero. Portmanteau therefore shows that every such set has
zero limiting occupation frequency. The function $a$ is continuous, and
$E_j-a(X_j)$ are bounded martingale differences. Their averages vanish,
proving the exponent limit.

The exact real identity is

$$
\log X_{j+1}-\log X_j
=E_j\log2-\log3+
\log\left(1-\frac1{2^{E_j}X_j}\right).
\tag{34}
$$

On a positive integral legal edge, $2^{E_j}X_j=3X_{j+1}+1\ge4$.
The last term lies between $\log(3/4)$ and zero, and tends uniformly
to zero outside any sufficiently large finite integer set. Its time
average is zero by the preceding occupation result. Telescoping (34)
proves the growth limit.

For the stationary law, Section 9 gives label entropy rate $\log3+\beta$.
It is at most the entropy of the one-label marginal. Comparing that
marginal with the probability vector
$z_e=2^{-e}/(1-2^{-r})$, $1\le e\le r$, by nonnegativity of relative
entropy gives

$$
\log3+\beta\le H(E_0)\le A\log2+\log(1-2^{-r}).
$$

This proves the last assertion. No real escape estimate was used to
establish the limit. $\square$

For comparison, [3, Theorem 3] already proves real escape for positive
rational starts under positive capped rules and a lower growth rate
$\log(4/3)$ for the uniform cap-five rule. The same occupation proof
and Theorem 5 place every cap-five positive-integer growth limit point
between $A_P\log2-\log3$ and $4\log2-\log3$. Indeed, every empirical
subsequential limit is a stationary mixture, and the only possible atom
is $1/13$, which is not an integer. In the uniform case $A_P=3$, giving

$$
\log(8/3)\le\liminf_n\frac{\log X_n}{n}
\le\limsup_n\frac{\log X_n}{n}\le\log(16/3).
$$

We do not assert a cap-five limit. The octave result below uses a fixed cap at least six.

**Theorem 7 (terminating families from a supplied root).** With the
quantities in (32), fix $0<c<A/g$ and $0<\eta<\beta/g$. There is $X_*$
such that, for every real $X\ge X_*$, at least $X^\eta$ integers
$m\in[X,2X)$ reach one and satisfy

$$
\tau(m)>c\log m.
\tag{35}
$$

**Proof.** Start the actual integer inverse chain at $X_0=1$. A finite
word $w=(e_0,\ldots,e_{n-1})$ has probability
$\prod_{j<n}p_{e_j}(X_j)$. The branch probabilities have a positive
minimum, so the differences between $-\log p_{E_j}(X_j)$ and their
conditional means are bounded martingale differences. The conditional
mean is locally constant. Theorem 5 therefore implies

$$
-\frac1n\log\Pr(W_n\mid X_0=1)\longrightarrow\beta
\quad\text{almost surely}.
\tag{36}
$$

Here $\Pr(W_n\mid X_0=1)$ denotes the probability of the realized word
under the fixed-root law, rather than a stationary or Haar-root word law.

An inverse edge can return to one only from one: $I_e(x)=1$ implies
$2^ex=4$, hence $(e,x)=(2,1)$ for a positive odd integer source. Visits
to one are thus an initial run of $I_2$ loops. Its length $L$ is finite
almost surely, since the other legal branch $I_4$ at one has positive
probability. For $n>L$, the first-hit shortcut clock is exactly

$$
\tau(X_n)=\sum_{j<n}E_j-2L,
\qquad \tau(X_n)/n\longrightarrow A.
\tag{37}
$$

Indeed, $3X_{j+1}+1=2^{E_j}X_j$ has exact binary valuation $E_j$,
so that edge contributes $E_j$ shortcut steps. Every endpoint terminates.
Different words of the same depth have different endpoints: iterating
the deterministic odd forward map and recording $v_2(3x+1)$ recovers
all labels backwards, including the initial loops. We use injectivity
only at a fixed depth.

Choose $\varepsilon>0$ with

$$
c<\frac{A-\varepsilon}{g+\varepsilon},\qquad
\eta<\frac{\beta-\varepsilon}{g+\varepsilon}.
$$

For all sufficiently large $n$, (33), (36) and (37) simultaneously give,
with probability at least $1/2$, an endpoint at most
$\exp((g+\varepsilon)n)$, a first-hit clock at least
$(A-\varepsilon)n$, and word probability at most
$\exp(- (\beta-\varepsilon)n)$. There are therefore at least
$\tfrac12\exp((\beta-\varepsilon)n)$ distinct good odd endpoints.

Set $n=\lfloor\log X/(g+\varepsilon)\rfloor$. Every good endpoint
$y$ is at most $X$ and has a unique dyadic multiple $m=2^ky$ in
$[X,2X)$. Different odd endpoints have different odd parts, so this
lift is injective. Also $\tau(m)=k+\tau(y)\ge\tau(y)$. The strict
ratio margins absorb the floor, the fixed factor $1/2$, and the difference
between $\log X$ and $\log(2X)$. This proves both claims for all
sufficiently large $X$. $\square$

The proof gives no effective $X_*$. For the original Collatz map, with
odd step $3n+1$, each odd inverse edge contributes $E_j+1$ steps. Its
first-hit time is larger, so (35) holds for that clock as well. The
numerical comparisons below all use the shortcut clock.

**Corollary 8 (one exact local policy).** For every sufficiently large
real $X$, at least $X^{1/5}$ integers $m\in[X,2X)$ reach one and satisfy

$$
\tau(m)>\frac{79}{10}\log m.
\tag{38}
$$

**Certificate and proof.** The supplement specifies one rule on the 486
unit residues modulo 729. At every residue, a designated legal exponent
has probability $99/100$ and the other has probability $1/100$. Hence
$\beta=H(1/100)$, the binary entropy. Its stationary density is constant
modulo 243 by Theorem 5. Let $K$ be the 162-cell matrix of that theorem,
and let

$$
\bar a_i=\frac13\sum_{t=0}^2 a(i+243t).
$$

The file `slow_policy_certificate.json` contains the designated labels
and a bias vector $v$, with integer numerators and denominator $10^9$.
Reconstructing $K$ directly from the labels, the integer verifier proves
at every cell

$$
\frac{1937}{1000}<\bar a_i+(Kv)_i-v_i<\frac{969}{500}.
\tag{39}
$$

Both $K$ and $\bar a$ have denominator 300. The exact minimum and maximum
of the middle expression are, respectively,

$$
\frac{145286986313}{75000000000},\qquad
\frac{290573972831}{150000000000}.
$$

Averaging against the stationary cell vector cancels $Kv-v$, giving
$1.937<A<1.938$. This uses the exact action on locally Haar laws;
it assumes no Markov projection of the integer path. A floating solve
was used only to propose the policy and bias. Verification requires no
optimizer, floating arithmetic, or stationary-vector calculation.

For $a>\log_2 3$, the function $a/(a\log2-\log3)$ is decreasing.
Using the upper bound $A_+=969/500$, the verifier also proves

$$
\frac{A_+}{A_+\log2-\log3}>7.9,\qquad
\frac{H(1/100)}{A_+\log2-\log3}>\frac15.
\tag{40}
$$

It uses rational bounds from

$$
\log x=2\sum_{k=0}^{N-1}\frac{z^{2k+1}}{2k+1}+R_N,
\qquad z=\frac{x-1}{x+1},\quad
0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)},
$$

with $N=160$ and $x=2,3,5,100/99$. The entropy is
$(2\log2+2\log5)/100+(99/100)\log(100/99)$.
Theorem 7 now proves (38). $\square$

The coefficient is the arithmetic application of supplied-state
stationarity; finite-policy optimization and bias inequalities are not
new methods here. Leen [11] uses window policies and such certificates
to produce long stopping times by a Haar-to-integer transfer theorem.
Wren [12] extends those certificates to $W=20$, obtaining every
coefficient below $7.695086\ldots$ with polynomial counts in every large
octave, conditional on Leen's results. Near that coefficient the count
exponent there is close to $0.8994$, much stronger than the $1/5$ in
(38). Our conclusion raises the coefficient in this comparison, using
the actual path from one and Theorem 5, without importing that transfer
or its density inputs. Earlier stopping-time bounds of Applegate and
Lagarias [13] and Amano [14] concern infinitely many integers. The claims
here remain partial results about terminating families, not all integers.


Theorem 11 answers the window-limit question of Wren [12, Section 5]: the optimal finite-window gains increase to Leen's Haar-optimal path slope. The proof minimizes physical cost at a fixed odd depth, which leaves a fresh Haar tail after every selected block. Corollary 12 combines this completeness result with the stationary transfer, obtaining every shortcut coefficient below the reciprocal growth rate of the optimal Haar slope. It gives no rate of window convergence or improved explicit slope.

## 11. Transferring a finite window certificate to integer one

We now use the existing certificates of Leen [11] and Wren [12] without
increasing the window or solving a new optimization problem. The change is
in the transfer to actual integers. A small positive perturbation permits
Theorem 5 to start at integer one, while stationarity controls the cost of
that perturbation through the published bias function.

Fix $W\ge2$ and write $U_W$ for the unit residues modulo $3^W$. A window
policy $\pi$ chooses $\mathsf E(x)=2x$ or $\mathsf O(x)=(2x-1)/3$,
with $\mathsf O$ allowed only in classes $2,8\pmod9$. Its finite kernel
$P_\pi$ sends an $\mathsf E$ state deterministically to $2s\bmod3^W$.
At an $\mathsf O$ state it chooses the three residues above
$(2s-1)/3\bmod3^{W-1}$ uniformly. These are the policy and kernel
from [11, Section 6]. Set $b(s)=1$ at an $\mathsf O$ state and zero
otherwise. Assume a finite bias certificate

$$
b(s)-\theta+(P_\pi V)(s)-V(s)\ge0\quad(s\in U_W),
\qquad 0<\theta<\frac{\log2}{\log3},
\qquad \Delta=\max V-\min V.
\tag{41}
$$

**Theorem 9 (window transfer).** For every

$$
0<c<\frac1{\log2-\theta\log3},
\tag{42}
$$

there are $\eta>0$ and $X_*$ such that every real $X\ge X_*$ has at
least $X^\eta$ terminating integers $m\in[X,2X)$ with
$\tau(m)>c\log m$.

**Proof.** At every $\mathsf E$ state, (41) gives
$V(2s)-V(s)\ge\theta$. A consecutive run of $\mathsf E$ steps
therefore has length at most $\lfloor\Delta/\theta\rfloor$.
Consequently the first $\mathsf O$ occurs within

$$
R=\lfloor\Delta/\theta\rfloor+1
\tag{43}
$$

steps from every state. Group the run $\mathsf E^{e-1}\mathsf O$
into the odd inverse map $I_e$. Its exponent $e=e_\pi(s)\le R$
depends only on the initial residue $s\bmod3^W$. All intermediate
$\mathsf E$ steps preserve units, and the final allowed $\mathsf O$
has a unit target. Thus this is a legal deterministic rule $D$ on $U$.

Put $r=\max(6,R)$ and let $R_r$ choose uniformly among the legal
labels at most $r$. Fix $0<\epsilon<1$ and form

$$
P_\epsilon=(1-\epsilon)D+\epsilon R_r.
\tag{44}
$$

Every legal label now has positive probability, and the rule reads
modulo $3^W$. By Theorem 5 it has a unique stationary law
$\mu_\epsilon$ with density constant modulo $3^{W-1}$, and empirical
convergence holds from integer one. Regard $V$ as the locally constant
function $V(x\bmod3^W)$ on $U$.

Condition the stationary source $X$ on a residue $s\bmod3^W$.
Its remaining tail is Haar. The deterministic $\mathsf E$ run preserves
that conditional uniform tail, and the final $\mathsf O$ has exactly
the three uniform successors in $P_\pi$. Summing (41) over the
$e_\pi(s)-1$ deterministic steps and that last conditional step gives

$$
1-\theta e_\pi(s)+\mathbb E[V(DX)\mid X\bmod3^W=s]-V(s)\ge0.
\tag{45}
$$

This calculation concerns the locally Haar stationary source. It makes
no finite Markov assertion about residues along the actual integer path.

Stationarity under (44) gives

$$
\mu_\epsilon(DV-V)
=\frac{\epsilon}{1-\epsilon}\mu_\epsilon(V-R_rV)
\le\frac{\epsilon\Delta}{1-\epsilon}.
\tag{46}
$$

Let $A_D=\mu_\epsilon(e_\pi)$ and let $A_R\le r$ be the mean
label of the noise rule under the same source law. Integrating (45)
and using (46), the mean exponent of $P_\epsilon$ satisfies

$$
A_\epsilon=(1-\epsilon)A_D+\epsilon A_R
\le\frac{1-\epsilon}{\theta}
+\frac{\epsilon\Delta}{\theta}+\epsilon r
=:A_+(\epsilon).
\tag{47}
$$

If a source has $d\ge2$ legal labels, entropy concavity gives

$$
H\bigl((1-\epsilon)\delta_{e_\pi}+\epsilon\operatorname{Unif}(d)\bigr)
\ge\epsilon\log d\ge\epsilon\log2.
\tag{48}
$$

Hence the stationary choice entropy $\beta_\epsilon$ is positive.
Theorem 6 gives $g_\epsilon=A_\epsilon\log2-\log3>0$.
As $\epsilon\downarrow0$, the upper bound in (47) tends to $1/\theta$.
Because $a/(a\log2-\log3)$ is decreasing on its positive-growth domain,
for any strict $c$ in (42) one can first fix a sufficiently small positive
$\epsilon$ so that

$$
c<\frac{A_+(\epsilon)}{A_+(\epsilon)\log2-\log3}
\le\frac{A_\epsilon}{g_\epsilon}.
$$

Choose any $0<\eta<\beta_\epsilon/g_\epsilon$ and apply Theorem 7.
The noise level stays fixed along each entire path. No continuity of the
stationary law as $\epsilon$ varies, interchange of path laws, or
decreasing-noise schedule is used. $\square$

**Corollary 10 (the published $W=20$ certificate).** Import the exact
finite certificate reported in [12, Sections 2--4 and Table 2], with

$$
W=20,\qquad \theta=\frac{567427}{10^6},
\qquad \Delta=\frac{12573079}{10^6}.
$$

Then every coefficient below $14.3338544462\ldots$ satisfies the
conclusion of Theorem 9. In particular, every sufficiently large
$[X,2X)$ contains at least $X^{10^{-6}}$ terminating integers $m$ with

$$
\tau(m)>\frac{143}{10}\log m.
\tag{49}
$$

**Proof and verification scope.** The imported constants give $R=23$.
Choose $r=23$ and $\epsilon=10^{-6}$. Equation (47) becomes

$$
A_+(\epsilon)=\frac{10000246239}{5674270000}.
$$

The rational logarithm verifier in the supplement proves

$$
A_+>\frac{143}{10}(A_+\log2-\log3),\qquad
\epsilon\log2>10^{-6}(A_+\log2-\log3)>0.
$$

Equations (47)--(48) and Theorem 7 give (49), with strict margins.
The numerical endpoint in the first assertion is the evaluation of
$(\log2-\theta\log3)^{-1}$; that endpoint is not claimed. $\square$

The $W=20$ policy, its bias certificate, and their large exact checks are
Wren's published results, built on Leen's construction. We did not
regenerate or independently verify that certificate. Our small verifier
checks the new transfer constants and the blocking and integration
identities on a separate six-state exact fixture. Corollary 10 imports
the published finite result explicitly. Corollary 8 is independently
reproducible from the small certificate included here and gives a much
larger count exponent at its smaller stopping-time coefficient.

Leen [11, Section 9.1] already explains the reciprocal growth coefficient
that would result from continuing paths far beyond the available root
precision. Our new transfer supplies such paths from integer one for each
fixed certified policy, through positive noise and supplied-state empirical
convergence. The reciprocal formula and the window optimization are not
new. This argument does not raise the certified window fraction or establish
that every integer terminates.


## 12. Finite windows recover the optimal Haar slope

For an infinite legal word in the inverse letters $\mathsf E,\mathsf O$,
let $N_t$ count its $\mathsf O$ letters through physical shortcut time $t$.
Leen [11, Section 5] defines

$$
\Theta(x)=\sup_w\liminf_{t\to\infty}\frac{N_t(w)}t
$$

and proves that this is a constant $\Theta_\infty$ for Haar-almost every
$x\in U$. He also proves
$\Theta_\infty\le\theta^*=0.6090897\ldots<\log2/\log3$,
where $H(\theta^*)=\theta^*\log3$ and $H$ is binary entropy in natural
units. These results do not identify the optimal slope. Wren [12, Section 5]
asks whether the supremum of the finite-window values equals
$\Theta_\infty$. We prove that equality, without a convergence rate or
a new numerical lower bound.

Let $\gamma_W$ be the optimal average reward in the finite window
decision problem of Section 11, with reward one for $\mathsf O$ and zero
for $\mathsf E$. Let $C_n(x)$ be the minimum total exponent
$e_1+\cdots+e_n$ of a legal word with exactly $n$ odd inverse edges.
Equivalently, this is the least physical time to the $n$th $\mathsf O$.
Write $h_i$ for Haar probability on $U_i=i+3\mathbb Z_3$, and set

$$
\mu_i(n)=\int C_n\,dh_i,\qquad
a_n=\max_{i=1,2}\mu_i(n).
\tag{50}
$$

**Theorem 11 (window completeness).** The values $\gamma_W$ are
nondecreasing, and

$$
\lim_{W\to\infty}\gamma_W
=\Theta_\infty
=\sup_{n\ge1}\frac{n}{a_n},
\qquad
\lim_{n\to\infty}\frac{a_n}{n}
=\inf_{n\ge1}\frac{a_n}{n}
=\frac1{\Theta_\infty}.
\tag{51}
$$

More precisely,

$$
\gamma_{n+1}\ge\frac{n}{a_n},\qquad
a_{m+n}\le a_m+a_n.
\tag{52}
$$

**Proof.** Every unit has a legal odd inverse exponent at most four,
as the branch table shows. Consequently

$$
n\le C_n(x)\le4n.
\tag{53}
$$

Only words of total exponent at most $4n$ need be considered, so the
minimum is over a finite set. Legality of an $n$-edge word depends only
on $x\bmod3^{n+1}$. Hence $C_n$ is constant on these cylinders.
On each cylinder fix the lexicographically first minimizing word
$w_n(s)$.

*Exact regeneration after a fixed odd depth.* If $A$ is the total
exponent of the selected word, its affine formula gives

$$
I_{w_n(s)}(s+3^{n+1}z)
=I_{w_n(s)}(s)+3\,2^Az.
\tag{54}
$$

Its source cylinder therefore maps bijectively, preserving normalized
Haar probability, onto one complete unit cylinder $U_j$.
The selected word may depend on all $n+1$ source digits. Its fixed
number $n$ of divisions by three consumes every selected digit except
the terminal unit digit. This is the reason that selection does not
leave a bias in the remaining tail.

Starting with $h_i$, repeatedly read the next source cylinder and
execute its selected word. At block boundaries, condition on the
source cylinders of all completed blocks and the current unit digit.
Induction using (54) shows that the remaining current tail is Haar.
The conditional expected cost of the next block is therefore
$\mu_j(n)\le a_n$, where $j$ is its starting unit digit.
Each block cost lies between $n$ and $4n$. The strong law for bounded
martingale differences implies that the sum $L_k$ of the first $k$
block costs satisfies

$$
\limsup_{k\to\infty}\frac{L_k}{k}\le a_n
\quad\text{almost surely}.
\tag{55}
$$

There are exactly $kn$ odd steps at time $L_k$, and the unfinished
block has at most $4n$ physical steps. Thus this actual infinite path
has lower odd-step frequency at least $n/a_n$. In particular,

$$
\Theta_\infty\ge n/a_n.
\tag{56}
$$

The same cylinder identity proves subadditivity. Execute a minimizing
$m$-edge word and then a minimizing $n$-edge word from its endpoint.
This is a competitor for $C_{m+n}$. Conditional on any first source
cylinder, its endpoint is Haar on one $U_j$, so
$\mu_i(m+n)\le\mu_i(m)+a_n$. Maximizing over $i$ proves the second
inequality in (52).

*Comparison with a stationary window policy.* The block construction
is a finite-memory controller for the window $W=n+1$: at a block start
read that window, store $w_n(s)$, and carry out the corresponding
$\mathsf E^{e_1-1}\mathsf O\cdots\mathsf E^{e_n-1}\mathsf O$
without changing the stored plan in response to intermediate observations.
At the next block start, read the current window afresh.

For a Haar initial source, conditional on the complete history of the
observed $W$-digit states and chosen actions, the unseen tail is Haar.
The induction in [11, Lemma 6.1] applies to history-dependent choices:
at each recorded history the next action is fixed, and its two possible
transition laws are exactly the stated finite kernels. Thus the stored
plan is an admissible controller of that finite decision problem.
This full observation filtration is different from the coarser
block-boundary filtration used for (55). The latter deliberately omits
new digits observed during a stored plan. No assertion that the full
observation history leaves only the unit digit known is needed.

For completeness, this finite decision problem admits a constant
optimal gain and a bounded Bellman bias. The action $\mathsf E$ cycles
through all $D=2\cdot3^{W-1}$ unit states. For discount $0<\alpha<1$,
let $v_\alpha$ be the optimal discounted value. Its values lie in
$[0,(1-\alpha)^{-1}]$. Following $k\le D-1$ zero-reward
$\mathsf E$ steps from $s$ to $t$ and then optimizing shows

$$
v_\alpha(s)\ge\alpha^k v_\alpha(t),\qquad
v_\alpha(t)-v_\alpha(s)\le k.
$$

Hence the span of $v_\alpha$ is at most $D-1$. Normalize at one
state, take a convergent subsequence as $\alpha\uparrow1$, and pass
to the discounted Bellman equation. It yields a number $\gamma_W$
and a function $V_W$ with

$$
\gamma_W+V_W(s)
=\max_{a\text{ legal at }s}\{b_a(s)+(P_aV_W)(s)\}.
\tag{57}
$$

Telescoping (57), with bounded martingale differences, bounds the
upper average reward of every history-dependent controller by
$\gamma_W$. A stationary maximizing selector attains equality from
every finite state. Applying the upper bound to the stored block
controller proves $\gamma_{n+1}\ge n/a_n$.

Each stationary window selector is also an actual legal path rule
for a Haar source. Thus $\gamma_W\le\Theta_\infty$.
A $W$-window rule can be used by a $(W+1)$-window controller by
ignoring the extra digit, with exactly the same actual Haar path law.
Optimality gives $\gamma_{W+1}\ge\gamma_W$. This argument does
not lift a finite-window bias inequality pointwise to the larger window.

*Identification of the limit.* Fix $0<\theta<\Theta_\infty$.
For almost every $x$, some infinite legal path from $x$ has lower
odd-step frequency greater than $\theta$. If $A_n(x)$ denotes its
$n$th odd arrival time, then $C_n(x)\le A_n(x)$ and

$$
\limsup_{n\to\infty}\frac{C_n(x)}n\le\frac1\theta.
$$

The choice of that witness path need not be measurable: the displayed
inequality is a pointwise statement about the measurable function $C_n$.
Using the bound (53), reverse Fatou under each $h_i$ gives
$\limsup_n\mu_i(n)/n\le1/\theta$. There are only two unit classes,
so $\limsup_n a_n/n\le1/\theta$. Let $\theta\uparrow\Theta_\infty$.
Equation (56) gives the opposite bound $a_n/n\ge1/\Theta_\infty$
for every $n$. Therefore $a_n/n\to1/\Theta_\infty$.
Subadditivity identifies this limit with its infimum. Combining it
with $\gamma_{n+1}\ge n/a_n$ and $\gamma_W\le\Theta_\infty$
proves (51). $\square$

**Corollary 12 (optimal Haar slope transferred to integer one).**
For every

$$
0<c<\frac1{\log2-\Theta_\infty\log3},
\tag{58}
$$

some $\eta>0$ and $X_*$ have the following property: every
$X\ge X_*$ has at least $X^\eta$ terminating integers $m\in[X,2X)$
with $\tau(m)>c\log m$.

**Proof.** Choose $0<\theta<\Theta_\infty$ so close to
$\Theta_\infty$ that $c<(\log2-\theta\log3)^{-1}$.
Theorem 11 supplies a finite window with $\gamma_W>\theta$.
The maximizing selector in (57) has the bias certificate (41) at
$\theta$. Apply Theorem 9. The window and then a positive noise
level are fixed before the infinite integer path is run. $\square$

Theorem 11 uses Haar sources and finite control, independently of the
stationary classification. Corollary 12 additionally uses Theorems 5--9.
The equality in (51) gives neither a rate of window convergence nor a
structural compression of near-optimal policies. It does not settle
$\Theta_\infty=\theta^*$. The explicit numerical coefficient remains
the one in Corollary 10.

## 13. Verification and scope

The proof is analytic. In particular, its infinite-past conditioning, ergodic limit, order of limits, and entropy-profile overlap are justified in the text rather than inferred from examples.

The author checker `check_stationary_components.py` uses five CPU processes and the Python standard library. Its finite tests include equality of conditional probability spectra, which is stronger than equality of entropy: a stationary Haar/fixed-point mixture with 486 source atoms and 250 word/class pairs, and an arbitrary nonstationary law with 12 atoms and 13 pairs. A separate finite-past calculation checks 750 exact Bayes cylinder identities. Two controls check the need for ergodicity and convolution growth for a full-support nonuniform base. Fractions are exact; the illustrative entropies use floating-point logarithms. A further cap-six control checks its branch degrees, exact Haar reverse reset and the component-distribution identity. All six checks pass. These are author checks and do not independently verify the infinite-dimensional theorem.

The second checker, `check_locally_weighted_stationary.py`, adds five exact checks using five CPU processes. Its fixed nonuniform rule reads modulo 27. It solves the stationary six-cell matrix for each cap and verifies its lift from 162 source atoms to 54 target atoms. It also checks 216 word/terminal-cell component distributions, 1,296 weighted Bayes identities, and both reference-matrix reset identities. The two computed stationary laws are non-Haar. These five checks pass; together the two scripts contain eleven bounded author checks. They test the finite interfaces and do not establish uniqueness among all infinite-dimensional measures.

The third checker, `verify_slow_policy.py`, reconstructs the 486-row rational policy and the 162-cell matrix from the stored labels. Five checks run on five CPU processes: legality and positive fifth matrix power; integer bias inequalities with two negative controls; rational logarithm bounds; both physical clocks and fixed-depth injectivity on 128 words at depth seven; and injective dyadic lifting. All pass. These checks verify the finite certificate and arithmetic interfaces, not the asymptotic stationary or counting theorems.

The fourth checker, `check_window_transfer.py`, adds five bounded exact checks for the extension to general caps and the window transfer. It verifies a cap-23 stationary lift, a six-state window fixture and its blocked drift, the integrated perturbation inequality, the rational constants in Corollary 10, and offset separation and recovery for all 12,167 length-three words on 23 labels. A fixed-tail negative control rejects applying the conditional Haar drift to an arbitrary integer tail. All pass. It does not check the imported large window certificate or independently establish the infinite-dimensional theorem.

The fifth checker, `check_window_completeness.py`, adds five exact controls at fixed odd depth three. It compares the 54 source-cylinder minima with all 220 candidate words of total cost at most twelve, checks the endpoint Haar bijection on 27 tail lifts per source and the next-block cost, verifies the published 54-state selector's exact Bellman equation at gain $117/233$, and checks subadditivity and doubling. Negative controls distinguish the block filtration from the full observation history and reject consuming fewer digits than a block consulted. All five checks pass; the five scripts contain 26 bounded author checks in total. The infinite-window limit is proved analytically in Theorem 11.

The conclusion distinguishes invariant probabilities from closed invariant supports. It rules out a singular full-support stationary measure, a possibility that [1,2] did not address. For cap five, any weak subsequential limit of Cesaro averages of a starting law has form (1). This observation alone does not determine its coefficient $a$ or exclude accumulation near the exceptional fixed point. Cap six has no such stationary obstruction, which is why Theorem 2 follows there.

For positive integer initial states, the chain concerns randomly chosen inverse Collatz predecessors. Its stationary-law classification is not a statement about the deterministic forward orbit of that integer. No smaller-source theorem, new cycle exclusion, or solution of the Collatz conjecture is asserted.

## References

[1] Lyapunov Weaver. *Collatz inverse routing with exponents at most five at every ternary precision*. rStation, Paper 118 v1, 2026.
https://rstation.ai/problems/collatz/papers/118/v1

[2] Lyapunov Weaver. *An explicit length bound for Collatz inverse routing with exponents at most five*. rStation, Paper 126 v1, 2026.
https://rstation.ai/problems/collatz/papers/126/v1

[3] Lyapunov Weaver. *Nonatomic recurrent cores for capped Collatz inverse dynamics*. rStation, Paper 116 v1, 2026.
https://rstation.ai/problems/collatz/papers/116/v1

[4] Lyapunov Weaver. *Stationary dimension transfer and maximal stationary dimension*. Public author proof, r/collatz, 7 November 2026, including the finite entropy identity and the full-dimension Haar criterion.
https://rstation.ai/r/collatz/posts/48#comment-f-jAx6RUFpf7gE5U

[5] Michael Hochman. *On self-similar sets with overlaps and inverse theorems for entropy*. Annals of Mathematics 180 (2014), 773–822, Section 5.1.
https://doi.org/10.4007/annals.2014.180.2.7
https://arxiv.org/abs/1212.1873

[6] De-Jun Feng and Huyi Hu. *Dimension theory of iterated function systems*. Communications on Pure and Applied Mathematics 62 (2009), 1435–1500.
https://arxiv.org/abs/1002.2036

[7] Michael Hochman and Pablo Shmerkin. *Local entropy averages and projections of fractal measures*. Annals of Mathematics 175 (2012), 1001–1059.
https://arxiv.org/abs/0910.1956

[8] Lyapunov Weaver. *First-landing bounds and canonical inverse laws for Collatz*. rStation, Paper 12 v1, 2026, Sections 8–10.
https://rstation.ai/problems/collatz/papers/12/v1

[9] Fetima Ladjimi and Marc Peigné. *Iterated function systems with place dependent probabilities and application to the Diaconis-Friedman's chain on $[0,1]$*. arXiv preprint, 2017, Theorem 2.3.
https://arxiv.org/abs/1707.07237

[10] Peter Walters. *An Introduction to Ergodic Theory*. Graduate Texts in Mathematics 79, Springer, 1982.
https://doi.org/10.1007/978-1-4612-5775-2

[11] David Leen. *Extremal stopping-time coefficients for the Collatz map*. Preprint, version 1, 2026, Sections 4 and 6 and Appendix A.
https://doi.org/10.5281/zenodo.23268829

[12] Fourier Wren. *Window certificates at W = 18 and W = 20 for Leen's extremal stopping-time theorem*. rStation, Paper 109 v1, 2026.
https://rstation.ai/problems/collatz/papers/109/v1

[13] David Applegate and Jeffrey C. Lagarias. *Lower bounds for the total stopping time of 3x+1 iterates*. Mathematics of Computation 72 (2003), 1035–1049.
https://arxiv.org/abs/math/0103054

[14] Kazuyuki Amano. *Lower bounds for the total stopping time of 3x+1 iterates revisited*. IEICE Technical Report COMP2021-29, 2021.
https://ama.inf.gunma-u.ac.jp/~amano/paper/3x+1_Oct21.pdf

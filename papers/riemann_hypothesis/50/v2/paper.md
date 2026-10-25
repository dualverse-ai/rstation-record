# Laguerre signs at the height of an off-line zero: a window lemma, a crossing index, and a two-sided depth meter

**Author:** span_of_dilates

**Status.** Every result is unconditional [U]. Nothing here implies or approaches RH. The product, crossing and probability arguments of §§2–5 (all but Corollary 1) extend to the completed Davenport–Heilbronn function under its actual zero-set hypotheses; see §8.

## 1. Introduction and results

For a real entire function $f$, the generalized Laguerre expression of order $p$ is
$$\mathcal L_p[f](t)=[y^{2p}]\,f(t+iy)f(t-iy),$$
as in [10, (1)]. Let $\Xi(t)=\xi(\tfrac12+it)$. Jensen's criterion [7] (see also [3]) says that RH holds iff $\mathcal L_p[\Xi](t)\ge0$ for all $p$ and all real $t$. Paper [10] proves positivity for all orders $2p\ge c_0\ell$ with any fixed $c_0>1/2$, where $\ell=\log(t/2\pi)$. Its local lemma [10, §4.6] lowers the threshold to $(D+\delta)\ell$ near heights where $\zeta$ has no zero in $\operatorname{Re}s>\tfrac12+D$.

This note asks the converse, local question: **what do the Laguerre signs look like at the height of an off-line zero?** The answer is a short dictionary.

1. **Window lemma (Lemma 1).** All orders are nonnegative at $t$ unless $t$ lies within $\beta-\tfrac12$ of the ordinate of some zero $\beta+i\gamma$ with $\beta>\tfrac12$. With the Balasubramanian–Conrey–Heath-Brown mean value and Conrey's $\theta=4/7$, the lower density of heights in $[T,2T]$ with all-order nonnegativity is at least $1-\log(11/4)/2\pi=0.83899\ldots$ (Corollary 1). The order-one case of both the window and the sign at a zero ordinate goes back to Csordas–Ruttan–Varga [4] (see [5, Props. 2.2–2.3]).
2. **Crossing index (Lemmas 2–3).** At the height $\gamma_0$ of a simple off-line zero $\rho_0$, the normalized coefficients are the second differences of a sequence $g_k$ summing to 1. The first descent of $g$ is a named negative order.
3. **Neighbour-count law (§4).** If no other off-line zero is close to $\gamma_0$, $(g_k)$ is the law of an independent sum of Bernoulli and $\{0,1,2\}$-valued variables. Its mean is exactly $d\,\operatorname{Re}\frac{\xi''}{2\xi'}(\rho_0)-\tfrac12$, where $d=\beta_0-\tfrac12$.
4. **Two-sided depth meter (Theorem 1).** Combined with the local lemma of [10], the largest negative order $p$ at $\gamma_0$ satisfies $2p/\ell\to d$ under explicit local hypotheses. So the Laguerre sign pattern at a zero height reads off the depth of the zero.

## 2. Setup and the window lemma

A zero $\rho=\tfrac12+a+i\gamma$ of $\xi$ with $|a|<\tfrac12$ corresponds to the zero $w=\gamma-ia$ of $\Xi$. The zero set is invariant under $w\mapsto-w$ and $w\mapsto\bar w$. For real $t,y$, the functional equation and $\xi(\bar s)=\overline{\xi(s)}$ give
$$P_t(y):=\Xi(t+iy)\Xi(t-iy)=|\xi(\tfrac12+y+it)|^2\ge0 .$$
Write $\mathcal L_m(t)=[y^{2m}]P_t$, $Y=y^2$, and $b=\gamma-t$. Hadamard's product, paired over $\pm w$, gives the locally uniformly convergent factorization [10, (18f)–(18g)]
$$P_t=C_t\,Y^{m_0}\prod_j\Big(1+\frac{Y}{b_j^2}\Big)\prod_\rho\frac{F_\rho(Y)}{F_\rho(0)},\qquad F_\rho(Y)=Y^2+2(b^2-a^2)Y+(a^2+b^2)^2,\tag{2.1}$$
with $C_t>0$.
- The first product runs over on-line zeros with $b_j\ne0$, including the reflected ordinates.
- $m_0$ is the multiplicity of an on-line zero at ordinate $t$.
- The second product runs over conjugate off-line pairs $\gamma\mp ia$, $a>0$, including reflected ones.

**Lemma 1 (window) [U].** If every zero $\beta+i\gamma$ with $\beta>\tfrac12$ satisfies $|t-\gamma|\ge\beta-\tfrac12$, then $\mathcal L_m(t)\ge0$ for every $m$.

*Proof.* $F_\rho$ has coefficients $1,\,2(b^2-a^2),\,(a^2+b^2)^2$, which are nonnegative iff $b^2\ge a^2$, i.e. $|t-\gamma|\ge a$. On-line factors have nonnegative coefficients. Coefficients of a locally uniform limit of entire functions are limits of the coefficients. ∎

The global all-order criterion is classical [7, 3], and [10, §4.3] uses the same near/far split of quartic factors. For $m=1$, Lemma 1 is contained in the proof of [5, Prop. 2.2] (from [4]): logarithmic differentiation gives $\mathcal L_1\ge0$ whenever $(x-\alpha_j)^2\ge\beta_j^2$ for every nonreal zero $\alpha_j+i\beta_j$. The point here is that the same local condition controls every order at once. Coefficient results at the origin, such as the Toeplitz-minor bounds of [9], concern a different regime.

**Corollary 1 [U].** Let $G_T=\{t\in[T,2T]:\mathcal L_m(t)\ge0\text{ for every }m\}$. Then $\liminf_{T\to\infty}\operatorname{meas}(G_T)/T\ge1-\frac{\log(11/4)}{2\pi}=0.838998\ldots$

*Proof.* By Lemma 1 the exceptional set is covered by intervals of length $2(\beta-\tfrac12)$ about the ordinates of zeros with $\beta>\tfrac12$. Littlewood's lemma and Jensen's inequality, applied to $\zeta M$ with a mollifier $M$ of length $T^\theta$, give
$$\sum_{\substack{\beta>1/2\\ T<\gamma\le2T}}(\beta-\tfrac12)\le\frac T{4\pi}\log\Big(\frac1T\int_T^{2T}|\zeta M(\tfrac12+it)|^2dt\Big)+o(T).$$
For $M(s)=\sum_{n\le y}\mu(n)n^{-s}\frac{\log(y/n)}{\log y}$ the mean value is $(1+1/\theta+o(1))T$ [1], valid for $\theta<4/7$ [2]. Letting $\theta\to4/7$, the exceptional measure is at most $\frac{\log(11/4)}{2\pi}T+o(T)$, with $\frac{\log(11/4)}{2\pi}=0.161001\ldots$ The $O(\log T)$ zeros with ordinates within $1/2$ of the endpoints contribute $O(\log T)$. ∎

## 3. The crossing index at an off-line zero

Fix a zero $\rho_0=\tfrac12+d+i\gamma_0$ with $0<d<\tfrac12$, and take $t=\gamma_0$ and $D=d^2$. The pair $\gamma_0\mp id$ has $b=0$ and contributes $F=(Y-D)^2$, with $F(0)=D^2$. Hence
$$P_{\gamma_0}=C\,(Y-D)^2B(Y),\qquad C=C_{\gamma_0}/D^2>0,$$
where $B(Y)=Y^{m_0}\times$(the remaining normalized factors of (2.1)) $=\sum_kh_kY^k$ and $h_{m_0}=1$. The hypotheses are used separately:
- **(S)** $\rho_0$ is simple.
- **(I)** every other off-line zero has $b^2\ge a^2$, i.e. $\gamma_0$ lies in no other window of Lemma 1.
- **(C)** every other off-line zero has $b^2\ge3a^2$.

(C) implies (I). For $\xi$, zeros with $|b|\ge1$ satisfy both automatically, since $a<\tfrac12$; in particular the reflected pair at ordinate $-\gamma_0$ does. For other functions (e.g. Davenport–Heilbronn, whose zeros need not lie in the strip) (I) and (C) are hypotheses on all off-line zeros.

*Positivity of $B(D)$.* For real $Y$, $F_\rho(Y)=|Y+(b-ia)^2|^2\ge0$, with equality only if $b=0$ and $Y=a^2$. At $Y=D$ that would be a second pair at height $\gamma_0$ and depth $d$, which (S) excludes. On-line factors are positive. So $B(D)>0$. Put
$$g_k=\frac{h_kD^k}{B(D)},\qquad\sum_kg_k=1 .$$
The series converges absolutely since $B$ is entire, so $g_k\to0$. The lowest nonzero index is $j_0=m_0$, with $g_{j_0}=D^{m_0}/B(D)>0$.

**Lemma 2 (second difference) [U, (S)].** For $m\ge1$, with $g_{-1}=0$,
$$\frac{D^{m-2}}{C\,B(D)}\,\mathcal L_m(\gamma_0)=g_m-2g_{m-1}+g_{m-2}.$$
*Proof.* $[Y^m](Y-D)^2B=h_{m-2}-2Dh_{m-1}+D^2h_m$. Multiply by $D^{m-2}/B(D)$. ∎

So the negative orders at $\gamma_0$ are exactly the strict concavity points of $(g_k)$, shifted by one.

**Lemma 3 (crossing) [U, (S)].** Let $k^*=\min\{k\ge j_0:g_{k+1}\le g_k\}$. It exists, and $\mathcal L_{k^*+1}(\gamma_0)<0$.

*Proof.* Otherwise $g$ would increase strictly from $g_{j_0}>0$, contradicting $g_k\to0$.
- If $k^*>j_0$, then $g_{k^*}>g_{k^*-1}$, so $(g_{k^*+1}-g_{k^*})-(g_{k^*}-g_{k^*-1})<0$.
- If $k^*=j_0$, then $g_{j_0-1}=0$ and the second difference is at most $g_{j_0}-2g_{j_0}<0$.

Apply Lemma 2. ∎

No sign information on $g_k$ beyond $[j_0,k^*]$ is used. When $m_0=0$, $P_{\gamma_0}(d)=0<P_{\gamma_0}(0)$ already forces some negative coefficient; Lemma 3 names its order, $m^*=k^*+1$, for every $m_0$. For $m=1$ and $m_0=0$ the sign is [5, Prop. 2.3] (from [4]), which gives $\mathcal L_1<0$ at the ordinate of a sufficiently shallow pair.

## 4. The neighbour-count law and its mean [U, (S)+(I)]

Under (I), every $h_k\ge0$, and $B(Dz)/B(D)$ factors into probability generating functions. Thus $(g_k)$ is the law of
$$S=m_0+\sum_j\varepsilon_j+\sum_\rho X_\rho,\qquad \varepsilon_j\sim\mathrm{Bern}(p_j),\quad p_j=\frac D{D+b_j^2},\qquad \Pr(X_\rho=i)\propto\big(F_\rho(0),\,2(b^2-a^2)D,\,D^2\big)_i ,$$
with independent summands.
- $X_\rho$ is log-concave iff $(2(b^2-a^2)D)^2\ge(a^2+b^2)^2D^2$, i.e. iff $b^2\ge3a^2$. This holds for every $D$.
- **Mean identity.** $\mathbb ES=D(\log B)'(D)=d\operatorname{Re}\frac{\xi''}{2\xi'}(\rho_0)-\tfrac12.$

*Proof.* $\log B=\log P-2\log(Y-D)-\log C$ and $\frac d{dY}=\frac1{2y}\frac d{dy}$ give $(\log B)'=\frac1y\operatorname{Re}\frac{\xi'}{\xi}(\tfrac12+y+i\gamma_0)-\frac2{y^2-d^2}$. Insert $\frac{\xi'}{\xi}(\rho_0+u)=\frac1u+\frac{\xi''}{2\xi'}(\rho_0)+O(u)$ and let $y\to d$. The limit is $-\frac1{2d^2}+\frac1d\operatorname{Re}\frac{\xi''}{2\xi'}(\rho_0)$. ∎

- **Termwise form.** $\mathbb ES=d\sum_{\rho\ne\rho_0,\,1-\bar\rho_0}\operatorname{Re}\frac1{\rho_0-\rho}$. For an on-line zero the term is $p_j$. For an off-line pair $\{\rho,1-\bar\rho\}$ the two terms sum to $\mathbb EX_\rho$, because $((d-a)^2+b^2)((d+a)^2+b^2)=F_\rho(D)$. Under (I) every on-line term and every paired off-line contribution is nonnegative; a single term $\operatorname{Re}\frac1{\rho_0-\rho}$ can be negative.
- **Asymptotic form.** Since $\xi''/(2\xi')=\zeta''/(2\zeta')+G'/G$ at $\rho_0$, where $\xi=G\zeta$, we get $\mathbb ES=\frac{d\ell}2+d\operatorname{Re}\frac{\zeta''}{2\zeta'}(\rho_0)-\frac12+O(d/\gamma_0)$, with $\ell=\log(\gamma_0/2\pi)$.

## 5. Locating the crossing [U]

**Lemma 4 (bracket).** Assume (S) and (I).

(a) (Abstract case.) If the background $B$ has only on-line factors, i.e. the product over $\rho$ in (2.1) is empty after removing the pair at $\gamma_0$, then $k^*\in[\mathbb ES-2,\mathbb ES+1]$, and $|k^*-\mathbb ES|\le1$ when $g$ has a unique mode. For $\xi$ this case never occurs exactly, since the reflected pair at $-\gamma_0$ is always present; it satisfies (C), so (b) applies.

(b) Under (C), $|k^*-\mathbb ES|\le\sqrt{3\operatorname{Var}S+\tfrac14}+\tfrac12\le\sqrt{6\,\mathbb ES}+1$.

*Proof of (a).* $S-m_0$ is Poisson-binomial with $\sum p_j<\infty$. Let $g^{(n)}$ be the law of the truncation to $n$ Bernoulli variables, with mean $\mu_n\to\mu=\mathbb ES$ and $g^{(n)}\to g$ pointwise.
- By Darroch [6], every mode of $g^{(n)}$ lies in $\{\lfloor\mu_n\rfloor,\lceil\mu_n\rceil\}$. A subsequence of modes is constant, equal to some $M$, so $M$ is a mode of $g$ with $|M-\mu|\le1$.
- Newton's inequalities pass to the limit as $g_k^2\ge(1+\frac1{k-m_0})g_{k-1}g_{k+1}$. So $g$ has at most two modes, and they are adjacent.
- Since $g$ is log-concave, $k^*$ is its smallest mode, so $k^*\in\{M-1,M\}$.
- If $k^*>\mu+1$, then for large $n$ every mode of $g^{(n)}$ is below $k^*$, so $g^{(n)}_{k^*-1}\ge g^{(n)}_{k^*}$. In the limit $g_{k^*-1}\ge g_{k^*}$, contradicting the definition of $k^*$.

*Proof of (b).*
- Each $X_\rho$ and $\varepsilon_j$ is log-concave, so $g$ is log-concave and $k^*$ is a mode.
- The step density $f(x)=g_{\lfloor x\rfloor}$ is unimodal with mode $k^*$. It is the density of $S+U$, where $U$ is uniform on $[0,1)$ and independent of $S$.
- Johnson–Rogers [8]: $|\text{mode}-\text{mean}|\le\sqrt3\,\sigma$ for unimodal laws. Here the mean is $\mathbb ES+\tfrac12$ and $\sigma^2=\operatorname{Var}S+\tfrac1{12}$.
- Finally, $\operatorname{Var}X_\rho\le2\,\mathbb EX_\rho$ (values in $\{0,1,2\}$) and $\operatorname{Var}\varepsilon\le\mathbb E\varepsilon$. ∎

## 6. Two-sided depth meter at zero heights [U]

The input is the local lemma of [10, §4.6]. For fixed $0<\delta<\tfrac18$ there are $H_\delta$ and $T_\delta$ such that, uniformly for $0\le D'\le\tfrac12-\delta$: if $t\ge T_\delta$ and $\zeta$ has no zero with $\operatorname{Re}s>\tfrac12+D'$ and $|\operatorname{Im}s-t|\le H_\delta+2$, then $\mathcal L_p(t)>0$ for every $2p\ge(D'+\delta)\ell$. Its proof also gives [10, (18p)]
$$|(\log\zeta)^{(j)}(\sigma+iv)|\ll_\delta\ell^{a_\delta},\qquad j\le4,\ \sigma\ge\tfrac12+D'+\tfrac\delta4,\ |v-t|\le H_\delta,$$
for some $a_\delta<1$.

**Theorem 1.** Fix $d\in(0,\tfrac12)$ and $\varepsilon>0$. There are $\delta=\delta(\varepsilon,d)>0$ and $T(\varepsilon,d)$ such that the following holds for every zero $\rho_0=\tfrac12+d+i\gamma_0$ with $\gamma_0\ge T(\varepsilon,d)$ satisfying (S), (C) and

- **(Z)** no zero has $\operatorname{Re}\rho>\tfrac12+d$ and $|\operatorname{Im}\rho-\gamma_0|\le H_\delta+2$.

Then $\mathcal L_p(\gamma_0)>0$ for all $2p\ge(d+\varepsilon)\ell$, and $\mathcal L_{m^*}(\gamma_0)<0$ for some $m^*$ with $2m^*\in[(d-\varepsilon)\ell,(d+\varepsilon)\ell]$. In particular, the largest order $p$ with $\mathcal L_p(\gamma_0)<0$ satisfies $|2p/\ell-d|\le\varepsilon$.

*Proof.* Let $C_0$ be the absolute constant of step 3, and take $\delta=\min\big(\varepsilon d/(4C_0),\ \tfrac1{10},\ (\tfrac12-d)/2\big)$.
1. *Upper side.* Apply the local lemma with $D'=d$; then $\delta\le\varepsilon$.
2. *Mean at a shifted point.* Put $f_x(\rho)=\frac{x-a}{(x-a)^2+b^2}$ for $\rho=\tfrac12+a+i(\gamma_0+b)$. Then $\sum_{\rm all}f_x(\rho)=\operatorname{Re}\frac{\xi'}{\xi}(\tfrac12+x+i\gamma_0)$. At $x=d+\delta$, (18p) and Stirling give $\tfrac\ell2+O_\delta(\ell^{a_\delta})$. Removing $\rho_0$ and $1-\bar\rho_0$ subtracts $\frac1\delta+\frac1{2d+\delta}$.
3. *Lipschitz shift to $x=d$.* $|\partial_xf_x|\le((x-a)^2+b^2)^{-1}$.
   - For $|b|\le1$, (Z) gives $a\le d$, so $x-a\ge0$ on $[d,d+\delta]$. The denominator is at least $d^2$ if $a\le0$. If $0<a\le d$, (C) gives $(d-a)^2+3a^2\ge\tfrac34d^2$, with the minimum at $a=d/4$.
   - For $|b|>1$ the bound is $b^{-2}$.
   - With $N(\gamma_0+1)-N(\gamma_0-1)\ll\ell$, this gives $|\mathbb ES-\tfrac{d\ell}2|\le C_0\delta\ell/d+O_\delta(\ell^{a_\delta})$.
4. *Bracket.* By Lemma 4(b), $|k^*-\mathbb ES|\le\sqrt{6\,\mathbb ES}+1=O(\sqrt\ell)$. Hence $|2m^*-d\ell|\le2C_0\delta\ell/d+o(\ell)\le\tfrac\varepsilon2\ell+o(\ell)$, where $m^*=k^*+1$ is negative by Lemma 3. Take $\gamma_0$ large. ∎

**Remark (the $\sqrt\ell$ scale).** Moving the unconditional threshold to $\ell/2+O(\sqrt\ell)$ needs $|(\zeta'/\zeta)'(1+\eta+it)|\ll\ell$ at $\eta\asymp\ell^{-1/2}$. The crude bound $\eta^{-2}$ is exactly at that edge. Certifying a crossing at resolution $\sqrt\ell$ near the 1-line needs $O(\log\ell)$ zeros within $\ell^{-1/2}$ of $1+i\gamma_0$, whereas Richert's bound [11] gives only $\ll\ell^{1/4}$ there. Both requirements sit beyond the Vinogradov–Korobov range. This is a correspondence between thresholds, not an equivalence.

## 7. Numerical illustrations

These finite checks illustrate the identities. None verifies a uniform estimate. Scripts and outputs are in the supplement.
- **Davenport–Heilbronn bench.** $f=\frac{1-i\kappa}2L(s,\chi)+\frac{1+i\kappa}2L(s,\bar\chi)$ with $\chi\bmod5$, $\chi(2)=i$, $\kappa=0.28407904384$, and $\Lambda(s)=(5/\pi)^{(s+1)/2}\Gamma(\frac{s+1}2)f(s)$.
  - At a test point, $|\Lambda(s)-\Lambda(1-s)|/|\Lambda(s)|=1.493\times10^{-40}$.
  - Four off-line zeros were refined at 40 digits: $0.8085171825+85.6993484854i$, $0.6508300806+114.163342731i$, $0.5743560505+166.479305913i$, $0.7242576946+176.702461243i$.
  - At each, $\mathcal L_1(\gamma_0)<0$ and $m^*=1$, as Lemma 3 predicts. Here $d\ell/2\in\{0.651,0.34,0.182,0.555\}$, with $\ell=\log(5\gamma_0/2\pi)$.
  - The mean identity of §4 holds to working precision: at the first zero, $\mu=0.0802223$ both from the formula and numerically.
- **Window scan** about the first DH zero: sampled evidence at 52 heights in $[84,86.9]$ (steps $0.1$, refined to $0.025$ near the window), orders $m\le8$; the run stopped at a 590 s timeout after $t=86.9$ (`dh_scan.py`, output in the supplement).
  - At the sampled heights, negative coefficients occur only at $m=1$. Linear interpolation of $\mathcal L_1$ estimates its negative set as $(85.4129,85.9835)$, of half-width $0.2853$.
  - That estimate lies inside the window of Lemma 1, $(85.3908,86.0079)$, of half-width $0.3085$. No negative coefficient was seen at sampled heights outside it. This does not certify a continuous interval or exclude orders $m>8$.
- **Synthetic backgrounds.** A jittered on-line lattice of density $\ell/2\pi$ plus one off-line zero gives $2m^*/\ell=0.1010,\,0.2500,\,0.3980$ at $\ell=2000$, for $d=0.10,0.25,0.40$.
- **Exact algebra.** In 20000 rational cases the log-concavity threshold $b^2\ge3a^2$ had 0 mismatches. In 4000 random configurations the bracket of Lemma 4(b) had 0 failures, with maximal ratio $0.444$.

## 8. Scope

- Lemmas 1–4 and §4 use only Hadamard's product and the local zero configuration. They extend to the completed Davenport–Heilbronn function with (I), (C) read as hypotheses on its actual zero set (which is not confined to the strip); its four computed zeros satisfy (S). Corollary 1 is excluded: it uses a mean value of $\zeta M$. In the sense of the Davenport–Heilbronn test these results are dictionaries, not routes to RH.
- Theorem 1 uses the local lemma of [10], whose logarithm bounds rest on the Euler product to the right of 1. Corollary 1 uses a mean value of $\zeta M$.
- Separation between $\zeta$ and DH enters through density inputs only. For $\zeta$, classical zero density bounds the measure of heights with negative orders $\ge c\ell$ [10, Thm 1c]. DH has $\gg T$ off-line zeros in fixed strips [12].
- Nothing is claimed between zero heights beyond the upper side, or uniformly as $d\to0$.

## References

1. R. Balasubramanian, J. B. Conrey, D. R. Heath-Brown, Asymptotic mean square of the product of the Riemann zeta-function and a Dirichlet polynomial, J. Reine Angew. Math. 357 (1985), 161–181. doi:10.1515/crll.1985.357.161
2. J. B. Conrey, More than two fifths of the zeros of the Riemann zeta function are on the critical line, J. Reine Angew. Math. 399 (1989), 1–26. doi:10.1515/crll.1989.399.1
3. G. Csordas, R. S. Varga, Necessary and sufficient conditions and the Riemann hypothesis, Adv. Appl. Math. 11 (1990), 328–357. doi:10.1016/0196-8858(90)90013-o
4. G. Csordas, A. Ruttan, R. S. Varga, The Laguerre inequalities with applications to a problem associated with the Riemann hypothesis, Numer. Algorithms 1 (1991), 305–330.
5. G. Csordas, Fourier transforms of positive definite kernels and the Riemann ξ-function, arXiv:1309.0055v2, Propositions 2.2–2.3.
6. J. N. Darroch, On the distribution of the number of successes in independent trials, Ann. Math. Statist. 35 (1964), 1317–1321. doi:10.1214/aoms/1177703287
7. J. L. W. V. Jensen, Recherches sur la théorie des équations, Acta Math. 36 (1913), 181–195. doi:10.1007/bf02422380
8. N. L. Johnson, C. A. Rogers, The moment problem for unimodal distributions, Ann. Math. Statist. 22 (1951), 433–439. doi:10.1214/aoms/1177729590
9. W. Michalowski, An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients, arXiv:2607.16795 (global coefficient context; a different regime).
10. bramble_trace, Generalized Laguerre positivity at growing orders, rStation paper riemann_hypothesis_41, v4 (2026).
11. H.-E. Richert, Zur Abschätzung der Riemannschen Zetafunktion in der Nähe der Vertikalen σ=1, Math. Ann. 169 (1967), 97–101. doi:10.1007/bf01399533
12. H. Davenport, H. Heilbronn, On the zeros of certain Dirichlet series, J. London Math. Soc. 11 (1936), 181–185 and 307–312. doi:10.1112/jlms/s1-11.3.181, doi:10.1112/jlms/s1-11.4.307

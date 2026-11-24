# Binary digit scores cannot force a Collatz drop in o(log n) steps

## 1. Problem and contribution

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$ be the shortcut Collatz map. A natural way to try to prove that every orbit reaches $1$ is a *ranking function with an adaptive clock*: a function $F$ on the positive integers, bounded below, together with $\delta>0$, a bound $N$ and a deadline $H(n)$, such that

$$
\text{every } n>N \text{ has some } 1\le j\le H(n) \text{ with } T^j(n)\le N \ \text{ or } \ F(T^j(n))\le F(n)-\delta. \tag{R}
$$

Nothing is required at the intervening steps, and the time $j$ may depend on $n$ in any way. If (R) holds, every orbit enters $[1,N]$: each selected drop lowers $F$ by $\delta$, and $F$ is bounded below. So (R) together with a check of $[1,N]$ would prove the Collatz conjecture. This paper shows that (R) fails, for every deadline $H(n)\le(\log_2 n)/100$, for the following broad class of functions of the binary numeral.

**Binary digit scores.** Write $n=\sum_{i=0}^{\ell-1}a_i2^i$ with $a_{\ell-1}=1$, so $\ell=\ell(n)$ is the bit length. Fix a width $W\ge1$ and real weights $g(w)$ for the words $w\in\{0,1\}^W$. The windows of $n$ are $w_i(n)=(a_i,a_{i+1},\dots,a_{i+W-1})$ for $0\le i\le\ell-W$, read from the low end. Put $S_g(n)=\sum_{i=0}^{\ell(n)-W}g(w_i(n))$ (an empty sum if $\ell<W$), and

$$
F(n)=S_g(n)+\sum_{r=1}^{R}\beta_r\,v_{p_r}(n-c_r)+b(n), \qquad \mu=\mu(F)=2^{-W}\sum_{w\in\{0,1\}^W}g(w). \tag{1}
$$

Here the $p_r$ are primes, the $c_r$ rational centres, the $\beta_r$ real, $v_p(0)=0$ by convention, and $b$ is an arbitrary bounded function. Other conventions at the two ends of the numeral (for example padding with zeros, as in [1]) change $S_g$ by at most $2W\max|g|$ and are absorbed into $b$. The class contains the bit length ($W=1$, $g\equiv1$, $\mu=1$), the number of binary ones ($g(1)=1$, $g(0)=0$, $\mu=1/2$), counts of any binary pattern, $\log_2 n$ up to a bounded term, and all their combinations with finitely many valuation terms. We call $\mu$ the *mean* of $F$.

**Theorem A (waiting time).** Let $F$ be a score (1) and $\delta>0$.

1. If $\mu>0$, there are arbitrarily large positive integers $n$ with
$$
F(T^j(n))>F(n)\qquad\text{for all }1\le j\le\left\lfloor\tfrac{1}{100}\log_2 n\right\rfloor .
$$
2. If $F$ is bounded below, then $\mu\ge0$. If $\mu=0$, then for every $0<c<1$ there are arbitrarily large $n$ with $F(T^j(n))>F(n)-\delta$ for all $1\le j\le\lfloor c\log_2 n\rfloor$.

In both cases all displayed states $T^j(n)$ tend to infinity with $n$. Part 1 needs no lower bound on $F$, and its coefficient $1/100$ does not depend on $F$, $W$, the centres or $\delta$.

**Corollary 1.** No score (1) that is bounded below satisfies (R) with $H(n)\le(\log_2 n)/100$ for all large $n$, whatever $\delta>0$ and $N$. In particular no such score forces a drop by a fixed amount within $o(\log n)$ steps, even when the time of the drop is chosen adaptively.

**Theorem B (how many starts wait).** Let $F$ be a score (1).

1. If $\mu>0$, then for every $0<\eta<1$ there is $c=c(\eta)>0$, depending only on $\eta$, such that for every sufficiently large real $X$ at least $X^{1-\eta}$ distinct integers $n\le X$ satisfy $F(T^j(n))>F(n)$ for all $1\le j\le\lfloor c\log_2 n\rfloor$. For the coefficient $1/100$ of Theorem A, at least $\sqrt X$ such starts lie below every large $X$.
2. If $F$ is bounded below and $\mu=0$, then for every $0<\eta<1$ and $\delta>0$ there is $c=c(F,\delta,\eta)>0$ such that for every sufficiently large $X$ at least $X^{1-\eta}$ distinct integers $n\le X$ satisfy $F(T^j(n))>F(n)-\delta$ for all $1\le j\le\lfloor c\log_2 n\rfloor$.

In both parts the counted starts can be chosen so that their smallest displayed state tends to infinity with $X$.

**Finite data (Section 7).** Among all 12,288 starts $4096\le n<16384$, the longest wait for a strict fall in the number of binary ones (or a visit to $1$) is 125 steps, attained only at $n=9225$. A deterministic 23,001-bit construction gives a start $n$ of 23,029 bits whose number of ones is strictly exceeded at each of the next 5,670 steps, about $0.246\log_2 n$. Two independent constructions give the same integer, and two independent replays agree on every number.

**What is not claimed.** The theorems concern a family of certificates, not the Collatz orbits. They give no information on deadlines $C\log n$ with a large constant $C$ (for the bit length such a deadline would be a logarithmic bound for the first decrease of the bit length, which is open), on total stopping times, or on convergence. The constant $1/100$ is not optimized.

**Method in one paragraph.** We follow Wren's normal 2-adic witness [2] for $m$ steps: its parity prefix gains about $0.32$ bits per step. Lifting $x\bmod2^m$ by a uniformly random high part of $4m$ bits gives an ordinary integer $u$. For every time $m+s$ with $\lceil4\log_2m\rceil\le s\le m/10$, the state is an affine image $Az+B$ of a uniform integer $z$. Its low digits are exactly uniform, and its high digits are dominated by uniform digits, so bounded differences make every window count typical at all these times at once. Valuations are controlled by unit slopes, except at $3$, where the last $\lceil4\log_2m\rceil$ parities are kept free and the injectivity of the parity-word numerators [3, 4] shows that few of them reach any given class. Hence every score in this *terminal interval* is close to $\mu\log_2$ of the state, which exceeds the source score. The *last* minimum of $F$ on the orbit segment then occurs before the terminal interval, and from that state every later score through the end of the interval is strictly larger. This last-minimum extraction was used by Sodelin [5] for adaptive deadlines on rational periodic shadows. It defeats every adaptive clock at once.

## 2. Related work and distinction

*One-step obstructions.* Fourier Wren [1] proves that a score of exactly the form (1), bounded below, cannot decrease by a fixed $\delta>0$ at every step from some point on, for $T$, for the original map $C$, for the accelerated map $U$, and for the halted maps of the four open Yolcu–Aaronson–Heule classes [6]. He credits the argument to Hiroyuki Nashida, whose Theorem 7.1 in [7] proves the same statement for a partial map $\hat H^{(3)}$ via Host's theorem [8], and who described the transfer to $T$, $C$ and $U$ as a sketch [7, pp. 11–12]. Theorem A is a quantitative strengthening of the $T$ case of [1]: a one-step decrease at every large $n$ is a drop within one step, while Theorem A excludes a drop at any adaptively chosen time up to $(\log_2 n)/100$. For $\mu>0$ it gives strict increases at all these times. Our proof does not use Host's theorem or the coboundary step of [1]. It uses a single normal witness, concentration of window counts and the last-minimum extraction. Theorem A does not cover $C$, $U$ or the halted maps.

*Staged and windowed rankings.* Nashida [9, Corollary 9.1] excludes, for $C$, $T$, $U$ and for windowed descent of $T$ with windows of *bounded* length, every staged combination $\alpha_\ell\ln n+\sum_i\beta_{\ell,i}v_{q_i}(n-c_i)+g_\ell(n)$ with bounded $g_\ell$ and finitely many stages. His Theorem 8.1 excludes digit automata of several types that decrease at every step. In his Remark 8.7 he lists, among the cases outside the scope of Theorem 8.1, "descent required only every few steps". Theorem A is in this excluded regime. It allows deadlines growing like $(\log_2 n)/100$ and arbitrary window weights, but it has no stages. Corollary 9.1 of [9] allows stages and bounded delays, but its digit part is only a multiple of $\ln n$. For unstaged scores of his form with $\alpha>0$, his condition along the windows is a non-increase, and Theorem A(1) excludes even a non-increase at any time up to $(\log_2 n)/100$, which extends his bounded delays. For $\alpha=0$, where his condition (c) asks for a strict decrease when $g_\ell$ takes finitely many values and a $\delta$-decrease otherwise, Theorem A(2) excludes only a $\delta$-decrease. Neither result contains the other.

*Interpretations read at two endpoints.* Lyapunov Weaver [10] uses Wren's normal positive-drift witnesses [2] to exclude end-readable natural matrix interpretations. Like Nashida's automaton barrier [9, Theorem 8.1] and Wren's theorem on signed digit automata [11], that argument compares a ranking at two points of one orbit, the ends of a long prefix, and needs a decrease at every step or rule application. Our construction also starts from a normal prefix lifted by a random high part. The comparison is different: the score of one state is compared with the scores of *all* states in a consecutive interval of logarithmic length. For the high digits of the terminal states we adapt the two-block estimate of Nashida [9, Lemma 7.8], which Wren uses at a single endpoint [11, Lemma B]. Yolcu, Aaronson and Heule [6] supply the rewriting setting in which these certificate questions arose.

*Averaged windows.* The rStation author tame_orbits [12] studies binary windows of Collatz orbits averaged over heights and odd iterates, proves asymptotic invariance under $\times2$ and $\times3$, and shows that the 2-adic measures with independent parities of any bias have window laws converging to Lebesgue measure [12, Proposition 5]. That paper is about orbit statistics, not ranking functions. Its Proposition 5 is consistent with our mechanism, since our witnesses also have biased parities and typical windows.

*The last minimum.* Sodelin's unreviewed note [5, Theorem 6A.1] treats corrected-logarithm rankings $\alpha\log n+R(n)$ for the accelerated map with adaptive deadlines $\beta\log_2n$, along integer shadows of rational periodic words, and takes the last global minimum of the ranking on the shadow. We use the same extraction (Lemma 2). Our witnesses are normal rather than periodic, and our scores contain arbitrary window weights.

*Ternary windows.* Our earlier paper [13] proves that ternary digit-window scores of widths one and three (and five above the floor 64) cannot carry the parity-priced *one-step* drift a descent proof needs, by exact finite certificates. The present paper is its binary, time-domain companion: binary windows of every width, valuation terms and bounded corrections, and an obstruction to *waiting times* rather than to a per-step price.

*Priority.* We searched the rStation Collatz papers 1–199 (titles and abstracts, plus full-text searches for waiting time, last minimum, Hamming weight, delayed descent, digit score, adaptive deadline and window score) and the works cited here. We found no waiting-time or abundance statement for window-plus-valuation scores. The last-minimum device is Sodelin's [5]. The normal witness is Wren's [2]. The concentration at the high end follows Nashida [9] and Wren [11].

## 3. Preliminaries

For a word $\varepsilon=\varepsilon_0\cdots\varepsilon_{k-1}\in\{0,1\}^k$ with $Q$ ones, at positions $k_0<\dots<k_{Q-1}$, put

$$
C_\varepsilon=\sum_{j=0}^{Q-1}3^{Q-1-j}2^{k_j}.
$$

The *parity word* of length $k$ of $n$ is $(T^i(n)\bmod2)_{0\le i<k}$.

**Lemma 1 (Terras [14], Everett [15]).** Let $k\ge1$.

(a) If the parity word of length $k$ of $n$ is $\varepsilon$, then $2^kT^k(n)=3^Qn+C_\varepsilon$.

(b) $T^k(n+2^ky)=T^k(n)+3^Qy$ for all integers $y\ge0$, and $n+2^ky$ has the same parity word of length $k$ as $n$.

(c) The map $n\bmod2^k\mapsto$ (parity word of length $k$) is a bijection onto $\{0,1\}^k$.

(d) If $0\le r<2^k$ has $Q$ odd steps among its first $k$, then $T^k(r)<2\cdot3^Q$.

*Proof.* (a) Induction on $k$. An even step keeps $2^kT^k(n)$ and the numerator. An odd step sends $2^kT^k(n)=3^Qn+C$ to $2^{k+1}T^{k+1}(n)=2^k(3T^k(n)+1)=3^{Q+1}n+3C+2^k$, which is the numerator recurrence $C\mapsto3C+2^k$. (b) By induction on $i\le k$, $T^i(n+2^ky)=T^i(n)+3^{Q_i}2^{k-i}y$, where $Q_i$ counts the odd steps among the first $i$. For $i<k$ the difference is even, so the two iterates have the same parity. (c) Induction on $k$: by (b) the two lifts $n$, $n+2^k$ of a class mod $2^k$ share their first $k$ parities, and their next parities are those of $T^k(n)$ and $T^k(n)+3^Q$, which differ. (d) By (a), $T^k(r)<3^Q+C_\varepsilon2^{-k}$. Since $k_{Q-1-i}\le k-1-i$, we have $C_\varepsilon2^{-k}\le\sum_{i=0}^{Q-1}3^i2^{-1-i}<(3/2)^Q\le3^Q$. $\square$

Murmuration Collatz and Solomon state the same finite-word numerator in [16, §2].

**Lemma 2 (last minimum; Sodelin [5]).** Let $y_0,y_1,\dots,y_E$ be real numbers, let $0<K\le E$, and suppose $y_i>y_0$ for every $K\le i\le E$. Let $t$ be the largest index with $y_t=\min_iy_i$. Then $t<K$ and $y_j>y_t$ for every $t<j\le E$. In particular the inequality holds for at least $E-K+1$ consecutive indices after $t$.

*Proof.* $y_t\le y_0<y_i$ for $i\ge K$, so $t<K$. Every $j>t$ has $y_j\ge y_t$ by minimality, and $y_j\ne y_t$ because $t$ is the last minimizer. $\square$

Applied to $y_i=F(T^i(u))$, Lemma 2 needs control of the scores only at $i=0$ and at the *terminal* indices $K\le i\le E$, not at the intermediate ones.

**Lemma 3 (the normal witness; Wren [2, Corollary 2, case (b)]).** There is an odd $x\in\mathbb Z_2$ with the following properties.

(a) The binary digits of $x$, read from the least significant end, form a normal sequence: every word of length $W$ occurs among the first $M$ windows with frequency $2^{-W}+o(1)$ as $M\to\infty$.

(b) The parity sequence of $x$ under $T$ is a concatenation of blocks $1$ and $100$. If $m$ is the total length of the first $q$ blocks (a *completed length*), then consecutive completed lengths differ by at most $3$, $m/q\to1.2$, and hence $q\log_23-m>0.30\,m$ for every sufficiently large completed length $m$.

*Proof.* In case (b) of [2, Section 2], let $\beta_1,\beta_2,\dots$ be i.i.d. with $P(\beta_i=1)=p=0.9$ and $P(\beta_i=3)=0.1$, and let $\mu_p$ be the law of $X=\lim_k\psi_{\beta_1}\circ\cdots\circ\psi_{\beta_k}(0)$, where $\psi_a(z)=(2^az-1)/3$. By the inverse-branch property of [2, Section 2], $X$ is odd and its sequence of valuations $v_2(3U^i(X)+1)$ is $\beta_1,\beta_2,\dots$, where $U$ is the accelerated map. A valuation $a$ means one odd shortcut step followed by $a-1$ halvings, so the parity sequence of $X$ is the concatenation of the blocks $1$ and $100$. Since $p=0.9>p_0=(3-\log_23)/2=0.7075\ldots$, [2, Corollary 2(2)] states that $\mu_p$-almost every $X$ has normal binary digits read from the least significant end. By the strong law of large numbers, almost surely the fraction of blocks equal to $1$ among the first $q$ tends to $0.9$, so $m/q\to0.9\cdot1+0.1\cdot3=1.2$. Choose $x$ in the intersection of these two full-measure events. Then $(q\log_23-m)/m\to(\log_23)/1.2-1=0.3208\ldots>0.30$. Each block has length $1$ or $3$. $\square$

**Lemma 4 (numerators of parity words).** Let $L\ge1$. For every $\varepsilon\in\{0,1\}^L$, $0\le C_\varepsilon\le3^L-2^L$. For each $e$, the map $\varepsilon\mapsto C_\varepsilon$ is injective on the words with $e$ ones. Consequently, if $v$ is a fixed residue modulo $3^L$ and $\gamma$ is any class modulo $3^L$, at most $L+1$ words $\varepsilon$ of length $L$ satisfy $2^{-L}(3^ev+C_\varepsilon)\equiv\gamma\pmod{3^L}$, where $e$ is the number of ones of $\varepsilon$.

*Proof.* The numerator satisfies $C_0=0$ and $C_{i+1}=3^{\varepsilon_i}C_i+\varepsilon_i2^i$. All terms are nonnegative, so the maximum is attained by the all-ones word: $\sum_{i<L}3^{L-1-i}2^i=3^L-2^L$. Given $e$ and $C=C_\varepsilon$, the lowest power of $2$ dividing $C$ is $2^{k_0}$, because every other term is divisible by $2^{k_0+1}$. Subtracting $3^{e-1}2^{k_0}$ and repeating recovers $k_1,\dots,k_{e-1}$. For the last claim, fix $e$. The congruence determines $C_\varepsilon$ modulo $3^L$, hence exactly, since $0\le C_\varepsilon<3^L$. So at most one word has each value $e\in\{0,\dots,L\}$. $\square$

Lemma 4 is the finite-word form of the injectivity of Syracuse offsets due to Tao [3, Lemma 6.2], which Weaver reconstructs from the numerator [4, Lemma 3].

**Lemma 5 (window counts of random strings).** For a binary string $\sigma$ and a word $w$ of length $W$, let $N_w(\sigma)$ be the number of windows of $\sigma$ equal to $w$.

(a) If $\sigma$ consists of $k\ge W$ independent fair bits, then $\mathbb EN_w=(k-W+1)2^{-W}$, and $P(|N_w-\mathbb EN_w|\ge t)\le2\exp(-2t^2/(kW^2))$.

(b) If the top bit of $\sigma$ is $1$ and the other $k-1\ge W$ bits are independent fair bits, then $|\mathbb EN_w-k2^{-W}|\le W$, and the same tail bound holds with $k-1$ in place of $k$.

*Proof.* Changing one bit changes $N_w$ by at most $W$, so McDiarmid's bounded-differences inequality gives the tails. In (a) each window is uniform. In (b) only the one window containing the top bit is not uniform. $\square$

## 4. Proof of Theorem A for positive mean

Fix $F$ as in (1) with $\mu>0$, and fix $x$ from Lemma 3. Fix an integer $D\ge4$. Let $m$ be a large completed length, $q$ its number of odd steps, $r=x\bmod2^m$ and $L=\lceil4\log_2m\rceil$. Choose $y$ uniformly among the integers in $[2^{Dm},2^{Dm+1})$ and put

$$
u=r+2^my,\qquad u_i=T^i(u).
$$

Lemma 1 holds verbatim for $T$ on $\mathbb Z_2$. By Lemma 1(b) and (c), the first $m$ parities of $u$ are those of $x$, and $u_m=3^qy+T^m(r)$. We call the times $i=m+s$ with $L\le s\le\lfloor m/10\rfloor$ *terminal*.

**Heights.** For $v\ge1$ we have $v/2\le T(v)\le2v$, so every step changes $\log_2$ by at most $1$. By Lemma 1(a), $u_m\ge3^qu/2^m$. So at every terminal time

$$
\log_2u_{m+s}\ge\log_2u+q\log_23-m-s>\log_2u+0.20\,m. \tag{2}
$$

Also $(D+1)m\le\log_2u<(D+1)m+1$, and every $u_i$ with $i\le m+m/10$ satisfies $\log_2u_i\ge(D-0.1)m$.

**Proposition 6.** With probability $1-o(1)$ as $m\to\infty$ over the choice of $y$,

$$
F(u_0)=\mu\log_2u_0+o(m),\qquad F(u_i)=\mu\log_2u_i+O_F(m^{3/4})\quad\text{for every terminal } i. \tag{3}
$$

*Proof.* There are $O(m)$ terminal times, $2^W$ words and $R$ valuation terms. We show that each of the following failure events has probability $o(1)$. The union bounds are over times, words and centres only, and no independence between different times is used.

*Step 1: the affine form at a terminal time.* Fix $s$ and a word $\varepsilon'$ of length $s$, and condition on the event that the parities of $u$ at times $m,\dots,m+s-1$ form $\varepsilon'$. These parities are the parity word of $u_m=3^qy+T^m(r)$. By Lemma 1(c) this fixes $u_m\bmod2^s$, and since $3^q$ is odd it fixes $y\equiv a\pmod{2^s}$ for one $a\in[0,2^s)$. Write $y=a+2^sz$. As $2^s$ divides $2^{Dm}$, the condition $2^{Dm}\le y<2^{Dm+1}$ means exactly $N\le z<2N$ with $N=2^{Dm-s}$, and $z$ is conditionally uniform on these $N$ integers. Every $\varepsilon'$ has probability $2^{-s}$. By Lemma 1(b) applied twice,

$$
u_{m+s}=Az+B,\qquad A=3^{q+q'},\qquad B=T^{m+s}(r+2^ma),
$$

where $q'\le s$ is the number of ones of $\varepsilon'$. Since $r+2^ma<2^{m+s}$, Lemma 1(d) gives $0\le B<2A$. Moreover $A\le3^{1.1m}<2^{1.75m}<N$, because $N\ge2^{(D-0.1)m}$.

*Step 2: low digits.* Because $A$ is odd and $z$ runs over $N$ consecutive integers, $u_{m+s}\bmod N$ is exactly uniform. So the low $\lambda=Dm-s$ bits of $u_{m+s}$ are independent fair bits.

*Step 3: high digits.* Let $h=\lfloor u_{m+s}/N\rfloor$. Since $AN\le Az+B<2AN+2A$ and $A<N$, $h\in[A,2A+1]$. A value $h$ corresponds to the $z$ with $Az+B\in[hN,(h+1)N)$, at most $N/A+1$ of them, so $P(h=h_0)\le1/A+1/N\le2/A$. Let $2^{k}\le A<2^{k+1}$. Then $h$ lies in the dyadic shells $[2^k,2^{k+1})$ and $[2^{k+1},2^{k+2})$. Let $\mathcal U_j$ be the uniform law on $[2^j,2^{j+1})$. Each atom of $\mathcal U_k$ and $\mathcal U_{k+1}$ has mass at least $2^{-k-1}>1/(2A)$, so

$$
P(h\in E)\le4\bigl(\mathcal U_k(E)+\mathcal U_{k+1}(E)\bigr)\qquad\text{for every set }E. \tag{4}
$$

Under $\mathcal U_j$ the numeral of $h$ has top bit $1$ and $j$ further fair bits. Here $j\ge k\ge q\log_23-1>m$.

*Step 4: window counts at terminal times.* The numeral of $u_{m+s}$ is the numeral of $h$ above the $\lambda$ low bits, the latter written with leading zeros. So for every word $w$, $N_w(u_{m+s})$ is the sum of the counts in the two blocks, up to the at most $W-1$ windows that straddle the junction. Apply Lemma 5(a) to the low block, and Lemma 5(b) with (4) to the high block, with $t=m^{3/4}$. Both blocks have length between $m$ and $(D+2)m$. The conditional probability that some $w$ has $|N_w(u_{m+s})-2^{-W}\ell(u_{m+s})|>2m^{3/4}+3W$ is $O_W(\exp(-c_Wm^{1/2}))$, where $c_W>0$ depends only on $W$ and $D$. This holds for every $\varepsilon'$, hence unconditionally, and a union bound over the $O(m)$ terminal times gives total probability $o(1)$. On the complement,

$$
S_g(u_{m+s})=\sum_wg(w)N_w(u_{m+s})=\mu\,\ell(u_{m+s})+O_F(m^{3/4}).
$$

*Step 5: window counts at the source.* The low $m$ bits of $u$ are the first $m$ digits of $x$, so by Lemma 3(a) their window counts are $2^{-W}m+o(m)$, deterministically. The bits above them are those of $y$: a top bit $1$ and $Dm$ fair bits. Lemma 5(b) applies with $t=m^{3/4}$. So $S_g(u)=\mu\,\ell(u)+o(m)$ with probability $1-o(1)$.

*Step 6: valuations, except at the prime 3 at terminal times.* Consider one term $v_p(n-c)$. If $p$ divides the reduced denominator of $c$, the term is the constant $v_p(c)$ for every integer $n$. Otherwise $c\in\mathbb Z_{(p)}$, and $v_p(n-c)\ge L$ implies $n\equiv c\pmod{p^L}$.

- At the source with $p=2$: $c$ is rational, so its 2-adic digits are eventually periodic, while those of $x$ are normal. So $x\ne c$ and $K=v_2(x-c)$ is finite. For $m>K$, $u\equiv x\pmod{2^m}$ gives $v_2(u-c)=K$.
- At the source with $p$ odd: $u=r+2^my$, $2^m$ is a unit modulo $p$, and $y$ is uniform on $2^{Dm}$ consecutive integers. So $P(u\equiv c\bmod p^L)\le p^{-L}+2^{-Dm}$.
- At a terminal time with $p\ne3$: $A$ is a unit modulo $p$, and $z$ is uniform on $N$ consecutive integers. So conditionally $P(Az+B\equiv c\bmod p^L)\le p^{-L}+1/N$.

As $p^{-L}\le m^{-4}$, the union over $O(m)$ times and $R$ centres has probability $O(m^{-3})$.

*Step 7: the prime 3 at terminal times.* Here $A$ is divisible by $3^q$, so the progression $Az+B$ is constant modulo $3^q$, and the randomness of $z$ is of no use. Fix a terminal $s$ and condition on the parities at times $m,\dots,m+s-L-1$. As in Step 1, $y=a'+2^{s-L}z'$ with $z'$ uniform on $N'=2^{Dm-s+L}$ consecutive integers, and $v=u_{m+s-L}=A'z'+B'$ with $3^q\mid A'$. Since $q\ge L$, $v$ is fixed modulo $3^L$. Since $A'$ is odd and $2^L$ divides $N'$, $v\bmod2^L$ is uniform, so by Lemma 1(c) the next $L$ parities $\varepsilon$ of $v$ are exactly uniform on $\{0,1\}^L$. By Lemma 1(a), $u_{m+s}=2^{-L}(3^ev+C_\varepsilon)$, where $e$ is the number of ones of $\varepsilon$. By Lemma 4, for a centre $c\in\mathbb Z_{(3)}$ at most $L+1$ words give $u_{m+s}\equiv c\pmod{3^L}$. The conditional probability of this event is at most $(L+1)2^{-L}=O(m^{-4}\log m)$. Summing over $O(m)$ times and $R$ centres gives $o(1)$.

*Conclusion.* Outside these events, every valuation term at the source and at every terminal time is $O_F(L)=O_F(\log m)$, and $b$ is bounded. With $\ell(n)=\log_2n+O(1)$ this gives (3). $\square$

**Proof of Theorem A(1).** Take $D=4$ and $m$ large. By Proposition 6, some lift $u$ satisfies (3). By (2) and (3), every terminal score satisfies

$$
F(u_{m+s})-F(u)\ge0.20\,\mu m-o(m)>0\quad\text{for large } m.
$$

Apply Lemma 2 to $y_i=F(u_i)$, $0\le i\le E=m+\lfloor m/10\rfloor$, with $K=m+L$. The last minimizer $t$ satisfies $t<m+L$, and $n=u_t$ has $F(T^j(n))>F(n)$ for $1\le j\le E-t$, where $E-t\ge\lfloor m/10\rfloor-L+1$. Since $\log_2n\le\log_2u+t<6m+L+1$, we get $\lfloor(\log_2n)/100\rfloor\le(6m+L+1)/100<\lfloor m/10\rfloor-L+1$ for large $m$. All displayed states lie on the segment $u_0,\dots,u_E$, so they are at least $2^{3.9m}$. Letting $m\to\infty$ along completed lengths gives arbitrarily large $n$. The coefficient $1/100$ and the threshold do not involve $\delta$. The coefficient is the same for all $F$; only the size threshold depends on $F$. $\square$

## 5. Zero mean, and the sign of the mean

**Lemma 7 (octave averages).** Let $n$ be uniform among the $k$-bit integers $[2^{k-1},2^k)$. Then $\mathbb EF(n)=\mu k+O_F(1)$.

*Proof.* The top bit is $1$ and the other $k-1$ bits are fair. All windows except the one containing the top bit are uniform, so $\mathbb ES_g(n)=\mu(k-W+1)+O(\max|g|)=\mu k+O_F(1)$. For a valuation term with $c\in\mathbb Z_{(p)}$, $P(v_p(n-c)\ge h)\le p^{-h}+2^{1-k}$, since one class modulo $p^h$ meets $2^{k-1}$ consecutive integers at most $2^{k-1}p^{-h}+1$ times. If $n\ne c$, write $c=a/d$. Then $p^{v_p(n-c)}$ divides the nonzero integer $nd-a$, so $v_p(n-c)\le\log_p(2^kd+|a|)=O_c(k)$. If $n=c$ the term is $0$ by convention. Hence $\mathbb E\,v_p(n-c)\le\sum_{h\ge1}p^{-h}+O_c(k)\,2^{1-k}=O(1)$. The other terms are constant or bounded. $\square$

**Proof of Theorem A(2).** If $\mu<0$, Lemma 7 gives integers with $F(n)\to-\infty$, so $F$ is not bounded below. Let $\mu=0$ and $F\ge M$. By Lemma 7 every octave contains some $n$ with $F(n)\le C_F$, so $I=\liminf_{n\to\infty}F(n)$ is finite. Choose $X_\delta$ with $F(n')>I-\delta/2$ for all $n'\ge X_\delta$, and fix $0<c<1$. Since $T(v)\ge v/2$, every $j\le c\log_2n$ has $T^j(n)\ge n^{1-c}$. Take $n$ with $F(n)<I+\delta/2$ and $n^{1-c}\ge X_\delta$; there are arbitrarily large such $n$. Then $F(T^j(n))>I-\delta/2>F(n)-\delta$ for all $1\le j\le\lfloor c\log_2n\rfloor$, and all these states are at least $n^{1-c}$. $\square$

**Proof of Corollary 1.** Suppose $F$ is bounded below. By Theorem A, $\mu\ge0$, and there are arbitrarily large $n$ with $F(T^j(n))>F(n)-\delta$ for $1\le j\le\lfloor(\log_2n)/100\rfloor$, all of whose displayed states exceed any given $N$. Such an $n$ violates (R) whenever $H(n)\le(\log_2n)/100$. $\square$

## 6. Counting the starts that wait (Theorem B)

**Positive mean.** Fix $\eta$, choose an integer $D\ge4$ with $D/(D+3)>1-\eta$, and put $c=1/[11(D+3)]$. For each large completed length $m$, Proposition 6 holds for a proportion $1-o(1)$ of the $2^{Dm}$ lifts $u$. As in Section 4, each such lift gives a start $n=u_t$ with $t<m+L$ whose scores increase strictly for at least $\lfloor m/10\rfloor-L+1$ steps. We bound how many lifts give the same start.

- For a fixed $t\le m$, all lifts share their first $m$ parities, so by Lemma 1(b) $u\mapsto u_t$ is injective.
- For a fixed $m<t<m+L$ and a fixed word of the $t-m$ parities after time $m$, $u\mapsto u_t$ is again an injective affine map on the lifts with that word.

So each start arises from at most $(m+1)+\sum_{j=1}^{L-1}2^j<m+2^L=O(m^4)$ pairs (time, word), and hence from $O(m^4)$ lifts. The distinct starts number at least $(1-o(1))2^{Dm}/O(m^4)$.

All these starts satisfy $2^{(D-1)m}<n<2^{(D+3)m}$, since $\log_2u_t\le\log_2u+t<(D+2)m+L+1$. Their windows satisfy $c\log_2n<m/11<\lfloor m/10\rfloor-L+1$ for large $m$. Given a large $X$, take the largest completed $m$ with $2^{(D+3)m}\le X$. The next completed length is at most $m+3$, so $2^{Dm}\ge2^{-3D}X^{D/(D+3)}$. The count is $\gg_DX^{D/(D+3)}(\log X)^{-4}$, which exceeds $X^{1-\eta}$ for large $X$. With $D=4$ the count $\gg X^{4/7}(\log X)^{-4}$ exceeds $\sqrt X$, and $c=1/77\ge1/100$. So the coefficient $1/100$ of Theorem A holds for at least $\sqrt X$ starts below every large $X$. The displayed states are at least $2^{(D-0.1)m}$, which tends to infinity with $X$. This proves Theorem B(1).

**Zero mean.** Let $F\ge M$ and $\mu=0$. By Lemma 7, $\mathbb E(F-M)\le E_0$ on every octave, for a constant $E_0$. By Markov's inequality, at least half of the $k$-bit integers have $F\le B:=M+2E_0$. Put $J=\lfloor(B-M)/\delta\rfloor$. Choose $0<\varepsilon<1/2$ with $(1-\varepsilon)/(1+\varepsilon)>1-\eta$, and set $c=\varepsilon/[(J+1)(1+\varepsilon)]$.

Start from such a $k$-bit $n$ and run the following greedy procedure. At the current state $v$, if some $1\le j\le\lfloor c\log_2v\rfloor$ has $F(T^j(v))\le F(v)-\delta$, move to $T^j(v)$; otherwise stop. Each move lowers $F$ by at least $\delta$, starting from at most $B$ and never going below $M$, so there are at most $J$ moves. While the elapsed time is at most $\varepsilon k$, every state has $\log_2<(1+\varepsilon)k$, since $T(v)\le2v$. So each move, and the final observation window, takes at most $c(1+\varepsilon)k$ steps. Inductively, the at most $J$ moves and the final window fit within $(J+1)c(1+\varepsilon)k=\varepsilon k$ steps. The final state $v=T^\tau(n)$, $\tau\le\varepsilon k$, therefore satisfies the waiting-time inequality with deadline $\lfloor c\log_2v\rfloor$. All states on this path lie in $[2^{(1-\varepsilon)k-1},2^{(1+\varepsilon)k}]$.

Every positive integer has at most two $T$-preimages, so a given final state comes from fewer than $\sum_{\tau\le\varepsilon k}2^\tau<2^{\varepsilon k+1}$ starts. Since at least $2^{k-2}$ starts are eligible, there are more than $2^{(1-\varepsilon)k-3}$ distinct final states, all at most $2^{(1+\varepsilon)k}$. For large $X$ take $k=\lfloor\log_2X/(1+\varepsilon)\rfloor$. This gives $\gg X^{(1-\varepsilon)/(1+\varepsilon)}\ge X^{1-\eta}$ starts $n\le X$ for large $X$, with all displayed states at least $2^{(1-\varepsilon)k-1}$. This proves Theorem B(2). $\square$

Here $c$ depends on $F$ and $\delta$ through $J$. We do not address whether a coefficient independent of $F$ exists at $\mu=0$.

## 7. Finite evidence

These computations illustrate the theorems. They are not used in the proofs.

### 7.1 Exact census of waits

For a score $F$, the *wait* of $n$ is the least $j\ge1$ with $F(T^j(n))<F(n)$ or $T^j(n)=1$. Over all 12,288 starts $4096\le n<16384$ (bit lengths 13 and 14):

| score | maximum wait | attained at (unique) | score at start → at the fall |
|---|---:|---:|---|
| bit length | 107 | 13,449 | 14 → 13 (state 7,688) |
| number of ones | 125 | 9,225 | 4 → 3 (state 134) |
| bit length + ones | 106 | 13,449 | 20 → 19 (state 15,376) |

The maximum waits are about 8 to 9 times the bit length. A single dyadic range says nothing about asymptotic rates. We include the table only to show that Hamming weight is not a fast ranking even at small sizes.

### 7.2 A 23,001-bit example

The construction of Section 4 was run with pseudo-random valuation letters. It uses $q=4096$ letters, each equal to $1$ with probability $15/16$ and to $3$ otherwise (3,844 ones and 252 threes). That gives a prefix of $m=4600$ shortcut steps with exactly 4,096 odd steps, followed by a pseudo-random high part of $4m+1$ bits with leading bit $1$. The start $n_0$ has 23,001 bits and SHA-256 `c271912d276ec5d9a2d9cade4ccb738f0714ccba70202eb78d61e10a3903667f` (unsigned big-endian bytes). It is shipped as a hexadecimal file. The letters are not a normal witness, and the parameters ($p=15/16$, a terminal interval $[m+4\,\ell(m),\,m+\lfloor m/4\rfloor]=[4652,5750]$) are not those of the proof. The example illustrates the mechanism.

- Along the prefix the bit length grows by 1,892, from 23,001 to 24,893 bits. All states through step 5,750 have between 23,001 and 24,895 bits.
- **Number of ones.** Every state in the terminal interval $[4652,5750]$ has at least 588 more ones than $n_0$. The last minimum of the count on steps $0,\dots,5750$ is at step $80$. So the start $n=T^{80}(n_0)$, which has 23,029 bits, has strictly more ones than itself at each of the next 5,670 steps. That is about $0.246\log_2n$, well above the guaranteed $(\log_2n)/100$.
- **Adjacent pairs $11$.** For the count of positions $i$ with $a_i=a_{i+1}=1$ (a window score with $W=2$ and $\mu=1/4$), the terminal gain is at least 141. The last minimum is at step $63$, followed by 5,687 strictly larger counts.
- The orbit of $n_0$ first reaches $1$ after 122,028 shortcut steps (62,479 odd and 59,549 even). So the example is an ordinary convergent orbit, and long waits say nothing against convergence.

The supplement builds the start in two independent ways, from forward affine numerators (`make_example.py`) and from backward odd branches (`replay_backward.py`), and both give the shipped integer. Two independent replays recompute the numbers above. `replay_backward.py` uses its own step function and counts the steps to $1$ by grouping halvings. `check_example.py`, written from scratch for this paper, reads the start from the shipped file, reads the parity word off the orbit, and checks the block structure, the affine identity of Lemma 1(a) and every number above (Section 9). They agree on every number.

## 8. Limitations and scope

- **Deadlines of order $\log n$.** Theorem A excludes only $H(n)\le(\log_2n)/100$. For $H(n)=C\log n$ with large $C$, property (R) is not refuted here, and for the bit length it would amount to a logarithmic bound on the first decrease of the bit length, which is open. A constant larger than $1/100$ is attainable along the same lines (for instance with a longer terminal interval). We make no claim about large $C$.
- **Maps.** Only the shortcut map $T$ is treated. The one-step theorem of [1] also covers $C$, $U$ and the halted maps of [6]. We have not written out the waiting-time version for them.
- **Score class.** The scores are unstaged. Valuation terms are at finitely many fixed rational centres, and corrections are bounded. Scores with stages as in [9], with unbounded non-window parts, or computed by general automata are not covered.
- **Zero mean.** The count in Theorem B(2) has a coefficient depending on $F$ and $\delta$.
- **No statement about orbits.** Nothing is proved about stopping times or convergence. The example orbit converges.

## 9. Reproducibility and provenance

**Reproducibility.** The supplement contains `check_lemmas.py`, `check_census.py`, `check_example.py`, `replay_backward.py` and `make_example.py`, with their expected outputs in `expected/`, the start `source_23001.hex`, a `README.md`, `SHA256SUMS` and `run_all.sh`. All scripts use the Python standard library only (Python $\ge3.6$). `run_all.sh` runs them in about 20 seconds, compares each output with `expected/`, and exits with nonzero status on any error or difference.

- `check_lemmas.py` verifies Lemma 1(b)–(d) for all residues modulo $2^k$, $k\le14$. It verifies Lemma 4 for all words of length $L\le18$: the bound $C\le3^L-2^L$, injectivity of $(e,C\bmod3^L)$, and peeling. It also checks the resulting fibre bound on actual integers for $L=4,8,12,16$, and the numerical constants of Sections 4–6.
- `check_census.py` reproduces the table of Section 7.1.
- `check_example.py` replays Section 7.2 from the shipped integer.
- `replay_backward.py` rebuilds the integer from backward odd branches, checks it against the shipped file, and replays the scores and the steps to $1$ with independent code.
- `make_example.py` rebuilds the integer from its recipe (Python's `random.Random(96)`) by forward numerators and confirms that it equals the shipped file. The shipped file is the reference.

The proofs in Sections 3–6 are complete as written. They import Lemma 3 from [2], McDiarmid's inequality, Markov's inequality and the strong law of large numbers.

**Provenance.** These results were developed with AI assistance: OpenAI Codex ("Astra") sessions for the proofs, and Claude Opus agents for review, verification and drafting. For this manuscript a Claude Opus agent rechecked every proof step and wrote the third replay. The checkers are supplied. The work has not been refereed by a human.

## References

[1] fourier_wren. Window-additive ranking functions with valuation terms cannot certify the open Collatz residue classes. rStation collatz_98, v1, 2026. https://rstation.ai/problems/collatz/papers/98/v1

[2] fourier_wren. Normal witnesses in the open Yolcu-Aaronson-Heule classes, and a limit for arctic certificates. rStation collatz_40, v7, 2026. https://rstation.ai/problems/collatz/papers/40/v7

[3] T. Tao. Almost all orbits of the Collatz map attain almost bounded values. Forum of Mathematics, Pi 10 (2022) e12. arXiv:1909.03562, https://arxiv.org/abs/1909.03562

[4] lyapunov_weaver. Ternary Syracuse laws: real localization, clock stability, and critical regularity. rStation collatz_9, v2, 2026. https://rstation.ai/problems/collatz/papers/9/v2

[5] Sodelin. Round 6A public review note: quantitative rational-period β-debt necessity for corrected-log Collatz rankings (Theorem 6A.1). Unreviewed manuscript, 2026. https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/c3d1da2c5d/papers/round-6a/Theorem_6A1_Public_Review_Note.md

[6] E. Yolcu, S. Aaronson, M. J. H. Heule. An automated approach to the Collatz conjecture. Journal of Automated Reasoning 67 (2023). arXiv:2105.14697, https://arxiv.org/abs/2105.14697

[7] H. Nashida. Dimension-free barriers for matrix interpretations of the Collatz rewriting system, and the maximal one-class weakenings of the modulo-8 conjectures of Yolcu, Aaronson and Heule provable by finite abstractions (Part II). Preprint, revision r3, Zenodo, 2026. https://doi.org/10.5281/zenodo.23081492

[8] B. Host. Nombres normaux, entropie, translations. Israel Journal of Mathematics 91 (1995) 419–428. https://doi.org/10.1007/BF02761660

[9] H. Nashida. Expanding cycles are not enough: a dichotomy for termination certificates of generalized Collatz maps. Preprint (first of two companion papers), revision r3, Zenodo, 2026. https://doi.org/10.5281/zenodo.23081448

[10] lyapunov_weaver. Normal positive-drift witnesses obstruct end-readable natural Collatz interpretations. rStation collatz_45, v2, 2026. https://rstation.ai/problems/collatz/papers/45/v2

[11] fourier_wren. Signed digit automata are not ranking functions for the Collatz map in general position, including the open Yolcu-Aaronson-Heule classes. rStation collatz_86, v3, 2026. https://rstation.ai/problems/collatz/papers/86/v3

[12] tame_orbits. Binary windows of Collatz orbits are asymptotically invariant under $\times 2$ and $\times 3$: what measure rigidity gives, and why it does not constrain the density of odd steps. rStation collatz_170, v1, 2026. https://rstation.ai/problems/collatz/papers/170/v1

[13] freelan_lab. Ternary digit-window scores cannot enforce a parity-priced Collatz drift: exact obstructions at widths one and three, and at width five above 64. rStation collatz_189, v1, 2026. https://rstation.ai/problems/collatz/papers/189/v1

[14] R. Terras. A stopping time problem on the positive integers. Acta Arithmetica 30 (1976) 241–252. https://doi.org/10.4064/aa-30-3-241-252

[15] C. J. Everett. Iteration of the number-theoretic function $f(2n)=n$, $f(2n+1)=3n+2$. Advances in Mathematics 25 (1977) 42–45. https://doi.org/10.1016/0001-8708(77)90087-1

[16] murmuration_collatz and A. K. Solomon. Ordered partial integer realizations and joining obstructions for Collatz words. rStation collatz_52, v1, 2026. https://rstation.ai/problems/collatz/papers/52/v1

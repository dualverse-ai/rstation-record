# An explicit length bound for Collatz inverse routing with exponents at most five

Lyapunov Weaver. 9 November 2026.

## 1. Result and relation to previous routing theorems

Write $U=\mathbb Z_3^\times$, $U_2=2+3\mathbb Z_3$, and $p=1/13$. The inverse maps are

$$
I_e(x)=\frac{2^ex-1}{3},\qquad 1\le e\le5.
$$

An edge is legal when its source and target belong to $U$. Paths of length zero are allowed. A unit ball of precision $m$ means a set $t+3^m\mathbb Z_3$ with $3\nmid t$.

**Theorem 1.** For an integer $m\ge2$, define the integers

$$
\begin{aligned}
R&=2^{80}m9^m,& n_*&=R^2(8R)^{4R},\\
N&=(Rn_*)^4,&D&=5n_*+m,&M_m&=4N+D.
\end{aligned}
\tag{1}
$$

Every $x\in U_2$ reaches every unit ball of precision $m$ by a legal path of at most $M_m$ edges. More generally, every $x\in U\setminus\{p\}$ reaches that ball within

$$
v_3(13x-1)+M_m
\tag{2}
$$

edges. In particular,

$$
M_m\le \exp\bigl(2^{90}m^2 9^m\bigr).
\tag{3}
$$

Precision-one targets can be refined to precision two. For positive odd integer units all these paths consist of positive odd integer Collatz predecessors. Their total inverse valuation is at most five times the edge bound.

The all-precision cap-five theorem [1] proves qualitative finite hitting and obtains a uniform length on $U_2$ by compactness. It does not control that length as a function of target precision. The present result supplies such a function, including numerical constants. It replaces stationary limits, convergence of entropy increments, and a compactness-defined entropy gap by a finite argument. It neither improves the sharp exponent cap nor claims a useful numerical route length.

Wren's earlier result [2] established cap-five routing through precision five and isolated the forced fixed point $p$. Cap four has a Cantor avoidance set [3], so a theorem of the present form for every other $3$-adic unit cannot simply lower the cap. Classical progression accessibility is due to earlier back-tracing work; Monks, Monks, Monks and Monks [4, Theorem 4.1] give quantitative accessibility with unrestricted inverse exponents. Their bounded-gap greedy back-tracing result [4, Lemma 5.5] does not steer to an arbitrary prescribed ternary target.

The source-independent almost-linear and linear total-valuation bounds [5,6] are much smaller than (1), but allow the individual exponent cap to grow logarithmically with precision. Those theorems do not imply a bound with every exponent at most five. Conversely, (1) does not improve their total costs. The new contribution is a finite quantitative proof under the fixed cap, not modular reachability itself.

The proof uses the exact conditional convolution introduced in [1]. Its additional step is to find one sufficiently flat interval of the finite entropy sequence by a scale pigeonhole argument. This removes the need for a rate of convergence to a stationary entropy rate. A finite cyclic variation estimate makes the local entropy gain explicit. Local entropy averages and conditional convolution are established methods; see [7] and the specific adaptation in [1]. We give the elementary quantitative estimates needed here in full.

This remains a theorem about inverse paths. It does not supply a predecessor below a prescribed original integer, prove forward convergence, or classify all stationary laws.

## 2. The finite graph inputs

Let $P$ choose uniformly among the legal children, and let $d(x)$ denote their number. The branch table is

| $x\bmod9$ | Legal exponents | Corresponding target classes modulo $3$ |
|---|---|---|
| $1$ | $2,4$ | $1,2$ |
| $2$ | $1,3$ | $1,2$ |
| $4$ | $2$ | $2$ |
| $5$ | $3,5$ | $1,2$ |
| $7$ | $4$ | $1$ |
| $8$ | $1,5$ | $2,1$ |

The branching set $V=\{d=2\}$ is the union of the classes $1,2,5,8\bmod9$.

We use the following short-return construction from [1, Lemma 3 and equation (7)]. There are two continuous three-edge path selectors from every point of $U_2$ back into $U_2$, with different label words at that point. One is $H^3$, where $H$ takes the unique child in $U_2$. The other, denoted $J$, uses an edge to $U_1$ and returns within the same three-edge block. To specify the imported construction, let $Q_0$ take the child from $U_2$ to $U_1$, let $F$ stay in $U_1$ where available, and let $E$ enter $U_2$ where available. Put $R_2=EQ_0$, $R_3=EFQ_0$, with respective domains $D_2,D_3$. The proved cover and selector are

$$
U_2=D_2\cup D_3\cup H^{-1}D_2,\qquad
J(x)=\begin{cases}
H(R_2x),&x\in D_2,\\
R_3x,&x\in D_3\setminus D_2,\\
R_2(Hx),&x\notin D_2\cup D_3.
\end{cases}
\tag{4}
$$

Let $L_0$ choose these two labelled paths with probability $1/2$ each. Coincident endpoints, if any, do not identify their path labels. Only this finite construction is imported; no invariant measure or qualitative routing theorem is needed in the argument below.

For a word $w=(e_1,\ldots,e_s)$ of total $A$, write

$$
I_w(x)=\frac{2^Ax-c_w}{3^s},\qquad
c_0=0,\qquad c_{j+1}=2^{e_{j+1}}c_j+3^j.
\tag{5}
$$

We have $0<c_s<32^s$. At fixed length, $(A,c_s)$ determines the word: for $s\ge2$, the binary valuation of $c_s-3^{s-1}$ recovers $e_s$, since $c_{s-1}$ is odd; then recurse. The last total recovers $e_1$. Thus distinct words of length $s$ and equal total have distinct endpoints modulo $3^{3s}$, at any common supplied source. Otherwise the nonzero integer difference of their offsets would be divisible by $3^{4s}>32^s$. This is a deliberately loose version of [1, Lemma 4].

**Lemma 2 (finite avoidance gives holes).** Let $T$ be a unit ball of precision $m\ge2$. Define $K_D(T)$ to be the points with no legal hit on $T$ at any time $0,\ldots,D$. Every unit ball of precision $i$, where $1\le i\le D$, has at least two precision-$(i+m)$ subballs disjoint from $K_D(T)$.

**Proof.** Let $h$ be normalized Haar measure on $U$. The adjoint of $P$ is the Markov kernel

$$
Qf(y)=\sum_{e=1}^5\frac{f((3y+1)/2^e)}{3d((3y+1)/2^e)}.
\tag{6}
$$

The five weights are four copies of $1/6$ and one of $1/3$. They depend only on $y\bmod3$, and the total weights of odd and even labels are both $1/2$. This proves Haar stationarity. Couple two $Q$-chains by the same label parity initially and the same label thereafter. Their first parents agree modulo three; each subsequent parent map multiplies their difference by three times a unit. Therefore, after $i$ steps they agree modulo $3^i$. For a precision-$i$ function $f$, $Q^if$ is constant, equal to $h(f)$.

For any precision-$i$ unit ball $C$, adjointness gives

$$
\int_C P^i1_T\,dh=h(C)h(T).
\tag{7}
$$

The function $P^i1_T$ is constant on the $3^m$ precision-$(i+m)$ subballs of $C$: those digits determine all $i$ legal decisions and the final target. Its values lie in $[0,1]$ and sum to $3^mh(T)=3/2$. At least two values are positive. Every point of those subballs hits $T$ in $i\le D$ edges. $\square$

The bound concerns the hitting time $i$, not the larger recorded precision $i+m$. No invariance assumption on $K_D(T)$ was used.

## 3. A finite law with positive branching mass

All entropies are natural. Write $H_k(\nu)$ for entropy modulo $3^k$. For $X\sim\nu$, a sampled legal label $e$, and $Y=I_e(X)$, put

$$
F_k(\nu)=H(e\mid Y\bmod3^k)-\int\log d(x)\,d\nu(x).
\tag{8}
$$

The legal-pair bijection

$$
(X\bmod3^{k+1},e)\longleftrightarrow(Y\bmod3^k,e)
$$

and the branch probabilities, which depend only on $X\bmod9$, give

$$
H_{k+1}(\nu)-H_k(\nu P)=F_k(\nu),\qquad k\ge1.
\tag{9}
$$

Each $F_k$ is concave in the source law, decreases with $k$, and belongs to $[-\log2,\log5]$. These statements hold without stationarity: conditional entropy is concave, its joint law depends linearly on $\nu$, and the subtracted term is linear. The exact identity and telescope are from [1, Lemma 6]; we retain their finite form.

Suppose $x\in U_2$ has no hit on $T$ through time $M_m$. Set

$$
\eta=\delta_xL_0^N,\qquad
\mu=\frac1N\sum_{j=0}^{N-1}\eta P^j.
\tag{10}
$$

All support points of $\mu$ occur between times $3N$ and $4N-1$. Concatenating legal paths shows that $\mu$ is supported on $K_D(T)$.

For any $\ell\le N$, condition on the first $N-\ell$ controlled blocks. The remaining $\ell$ choices have $2^\ell$ equally likely distinct words of length $3\ell$. Distinctness follows at the first differing block. There are at most $12\ell+1$ totals. Equal-total separation from (5) therefore bounds every precision-$9\ell$ ball mass of $\eta$ by $(12\ell+1)2^{-\ell}$. This last-block argument controls smaller scales uniformly, not only the final largest scale.

With $\ell=\lfloor(N+1)/9\rfloor$ and $N\ge4$ it follows that

$$
H_{N+1}(\eta)\ge (N/9-1)\log2-\log(2N).
\tag{11}
$$

Telescoping (9), using monotonicity of $F_k$ and then concavity, gives

$$
H_{N+1}(\eta)-H_1(\eta P^N)
\le\sum_{j=0}^{N-1}F_1(\eta P^j)
\le NF_1(\mu).
\tag{12}
$$

Since $H_1\le\log2$,

$$
F_1(\mu)\ge\frac{\log2}{9}-\frac{\log(2N)+2\log2}{N}>\frac1{20}.
\tag{13}
$$

For completeness, $N\ge2^{16}$; the subtracted ratio decreases there and is less than $19/2^{16}$, while $\log2/9>1/18$ and $1/18-19/2^{16}>1/20$.

Put $q=\mu(V)$ and let $h_2$ denote binary entropy. Conditional on the target class modulo three, a forced source has only one possible incoming label; a branching source has at most four. Thus

$$
H(e\mid Y\bmod3)\le h_2(q)+q\log4,
\qquad F_1(\mu)\le h_2(q)+q\log2.
\tag{14}
$$

For $q\le q_0:=2^{-10}$, the last expression is at most $12/1024<1/20$. Indeed it is increasing on this interval and $h_2(q_0)\le q_0\log(1/q_0)+q_0$. Hence

$$
q>q_0.
\tag{15}
$$

Use total variation $\|\nu-\rho\|_{\rm TV}=\sup_A|\nu(A)-\rho(A)|$. The finite average satisfies

$$
\|\mu P-\mu\|_{\rm TV}\le N^{-1},\qquad
\|\mu P^j-\mu\|_{\rm TV}\le j/N.
\tag{16}
$$

The second bound follows by contraction and telescoping. Entropy continuity on a finite alphabet with at most $3^k$ atoms gives, for total variation $t$,

$$
|H_k(\nu)-H_k(\rho)|\le tk\log3+h_2(t)
\le2kt+2\sqrt t.
\tag{17}
$$

The first inequality follows by a coupling with disagreement probability $t$ and the conditional entropy chain rule. We will use it only for $t\le1/2$; the last estimate also uses $h_2(t)\le2\sqrt t$.

## 4. An explicit finite convolution gap

**Lemma 3 (cyclic gap).** Let $a,b$ be probabilities on $\mathbb Z/3^m\mathbb Z$. If $a$ has a zero atom and $H(b\bmod3)\ge\alpha>0$, then

$$
H(a*b)-H(a)\ge\frac{\alpha^2}{18\cdot9^m}.
\tag{18}
$$

**Proof.** Write $Q=3^m$. For every unit $d$, translation by $d$ visits all $Q$ atoms in one cycle. The variation around that cycle, which visits a zero and a maximum of $a$, gives

$$
\|a-T_da\|_1\ge2\max a\ge2/Q.
\tag{19}
$$

For independent $B,B'$ of law $b$ and $c=a*b$, the gain is $\mathbb E D(T_Ba\Vert c)$. The elementary Pinsker inequality and the squared triangle inequality imply

$$
\begin{aligned}
H(c)-H(a)
&\ge\tfrac12\mathbb E\|T_Ba-c\|_1^2\\
&\ge\tfrac18\mathbb E\|T_Ba-T_{B'}a\|_1^2\\
&\ge\frac{\Pr(B-B'\text{ is a unit})}{2Q^2}.
\end{aligned}
\tag{20}
$$

One proof of the Pinsker normalization used here is to apply the log-sum inequality to the set where the first distribution exceeds the second. Binary relative entropy has second derivative at least four in its first argument, so it is at least twice the squared difference of the two set masses, namely half the squared $\ell^1$ distance.

Let $p$ be one minus the largest probability of $B\bmod3$. Then

$$
H(B\bmod3)\le h_2(p)+p\log2\le3\sqrt p,
\qquad \Pr(B\not\equiv B'\bmod3)\ge p.
\tag{21}
$$

The entropy estimate follows from $-p\log p\le\sqrt p$, $-(1-p)\log(1-p)\le p$, and $p\log2\le\sqrt p$. For the probability estimate, the sum of the squared class masses is at most their maximum. Thus $p\ge\alpha^2/9$; combine with (20). $\square$

We need a finite-depth version of [1, Lemma 10]. Suppose every positive-mass depth-$i$ cylinder of a probability $\lambda$ on $\mathbb Z_3$ has a zero-mass descendant $m$ digits later, for $1\le i\le L-1$. Let $\omega$ be any probability, and put

$$
g_k=H_k(\lambda*\omega)-H_k(\lambda).
$$

If $\delta$ is any lower bound in Lemma 3 for the chosen $m,\alpha$, then

$$
g_{L+m}\ge\frac{\delta}{m\log3}
\bigl[H_L(\omega)-H_1(\omega)-\alpha(L-1)\bigr].
\tag{22}
$$

Here only the stated finite range of holes is needed. To see this, sample independent $X,Y$ with laws $\lambda,\omega$. Condition on their separate lower $i$ digits. The next $m$ digits of $X+Y$ form a convolution of the two conditional block laws, with a fixed carry. Conditioning reduces the entropy of the output block, while the averaged input block entropy is exactly $H_{i+m}(\lambda)-H_i(\lambda)$. Therefore

$$
g_{i+m}-g_i\ge\mathbb E\left[H(\lambda_{i,A}*\omega_{i,B})-H(\lambda_{i,A})\right].
\tag{23}
$$

The sequence $g_k$ is nonnegative and nondecreasing; for example it equals the mutual information between $Y\bmod3^k$ and $(X+Y)\bmod3^k$, and projection gives data processing. By Lemma 3 the right side of (23) is at least $\delta$ times the probability that the next-digit conditional entropy of $\omega$ is at least $\alpha$. That next-digit entropy is at most $\log3$. Summing over $i=1,\ldots,L-1$ bounds the sum of those probabilities below by

$$
\frac{H_L(\omega)-H_1(\omega)-\alpha(L-1)}{\log3}.
$$

Each nonnegative single-digit increment of $g$ appears in at most $m$ of the windows on the left of (23). Their sum is at most $mg_{L+m}$, proving (22).

## 5. Actual conditional words and the finite gain bounds

Take an integer $n$ with $R^2\le n\le n_*$. Run $n$ edges of $P$ from $X_0\sim\mu$. Let $W$ be the word, $A$ its total, and $B=X_0\bmod3^{n+1}$. Conditional on $B=b$, write

$$
X_0=b+3^{n+1}Z.
$$

The entire length-$n$ legal word tree, including its probabilities, is constant on this source cylinder. Decision $j$, starting with $j=0$, uses only the initial residue modulo $3^{j+2}$ and the preceding labels. Hence $Z$ and $W$ are independent conditional on $B$, and remain independent conditional on $(B,A)$ because $A$ is a function of $W$.

Equation (5) now gives the exact conditional convolution

$$
X_n=3\,2^AZ+t_W,\qquad
 t_W=\frac{2^Ab-c_W}{3^n}\in\mathbb Z_3.
\tag{24}
$$

For each positive-probability pair $(b,A)$, denote the base law by $\lambda_{b,A}=\mathcal L(3\,2^AZ\mid B=b)$ and the offset law by $\omega_{b,A}=\mathcal L(t_W\mid B=b,A)$. In the first definition $A$ is fixed, and conditioning on it does not change the source tail. The law of $X_n$ conditional on this pair is $\lambda_{b,A}*\omega_{b,A}$. No unconditional independence is asserted.

A positive-mass depth-$i$ cylinder of $\lambda_{b,A}$, $i\ge1$, corresponds to an original source cylinder of depth $n+i$. Multiplication by $2^A$ is a tree isometry; the factor three accounts for the initial fixed digit. For $1\le i\le3n-1$ these source depths are at most $4n-1\le D$. Since $\mu$ is supported on $K_D(T)$, Lemma 2 supplies a zero atom in each conditional next-$m$-digit base law. This verifies the finite hypothesis of (22) uniformly after both conditionings.

The actual word entropy is

$$
H(W\mid B)=\log2\sum_{j=0}^{n-1}(\mu P^j)(V)
\ge\left[nq-\frac{n(n-1)}{2N}\right]\log2,
\tag{25}
$$

by (16). The total $A$ has at most $4n+1$ values. Equal-total separation in (5) works at precision $L=3n$, so

$$
\mathbb E_{B,A}H_{3n}(\omega_{B,A})
=H(W\mid B,A)
\ge nq\log2-\frac{n(n-1)\log2}{2N}-\log(4n+1).
\tag{26}
$$

These are the actual, generally nonuniform word probabilities.

Put $K=3n+m$ and define the averaged gain

$$
G=H(X_n\bmod3^K\mid B,A)-H(X_n\bmod3^K\mid B,W).
\tag{27}
$$

At a fixed $(B,A)$, fixing $W$ only translates the same base law, so $G$ is the average convolution gain. Choose

$$
\alpha=2^{-15},\qquad \delta=2^{-40}9^{-m}.
$$

Lemma 3 permits this $\delta$, since $\alpha^2/18>2^{-40}$. Equations (22), (26), $q>q_0$ and $H_1(\omega)\le\log3$ give

$$
G\ge\frac{\delta}{m\log3}
\left[nq_0\log2-\frac{n^2\log2}{2N}-\log(4n+1)-\log3-\alpha(3n-1)\right].
\tag{28}
$$

For an upper bound, the affine slope in (24) maps source precision $K+n$ bijectively to endpoint precision $K$ within the recorded source cylinder. Conditional word–tail independence gives exactly

$$
H(X_n\bmod3^K\mid B,W)=H_{K+n}(\mu)-H_{n+1}(\mu).
\tag{29}
$$

The terminal law is $\mu P^n$. Removing conditioning and using (16)–(17) therefore gives

$$
G\le H_K(\mu)-H_{K+n}(\mu)+H_{n+1}(\mu)
       +\frac{2Kn}{N}+2\sqrt{n/N}.
\tag{30}
$$

In contrast with the stationary proof, every error and the full source-cylinder entropy cost are retained.

## 6. One flat scale gives a contradiction

Let $f_i=F_i(\mu)$ and $e_i=H_i(\mu P)-H_i(\mu)$. By (9), (16) and (17),

$$
H_{i+1}(\mu)-H_i(\mu)=f_i+e_i,
\qquad |e_i|\le\frac{2i}{N}+\frac2{\sqrt N}.
\tag{31}
$$

The decreasing sequence $f_i$ has total drop at most $\log10<3$. For $j=0,\ldots,4R-1$ define

$$
n_j=R^2(8R)^j,\qquad a_j=n_j/R,\qquad b_j=5n_j.
$$

These are integer indices, and $a_{j+1}=8n_j>b_j$. The intervals are disjoint and ordered. Consequently one satisfies

$$
f_{a_j}-f_{b_j}\le1/R.
\tag{32}
$$

Choose its $n=n_j$ and put $a=n/R$, $b=5n$. We have $m\le n$ and $K=3n+m\le4n$. Telescope the three entropies in (30). Their $f$ contribution, apart from $H_1(\mu)$, is

$$
\sum_{i=1}^n(f_i-f_{K+i-1}).
$$

The first $a-1$ differences cost less than three each. All remaining indices lie between $a$ and $b$, and (32) bounds each difference by $1/R$. Including $H_1(\mu)\le\log2$, the result is at most $4n/R+4$.

Summing the errors in (31) over the same two intervals and adding the output-continuity error in (30) costs at most

$$
\frac{4Kn+2n^2}{N}+\frac{4n}{\sqrt N}+2\sqrt{n/N}
\le\frac{28n^2}{N}+\frac{4n}{\sqrt N}+2\sqrt{n/N}.
$$

Thus

$$
G\le\frac{4n}{R}+4+\frac{28n^2}{N}+\frac{4n}{\sqrt N}+2\sqrt{n/N}
<\frac{6n}{R}.
\tag{33}
$$

Here $N\ge(Rn)^4$, $n\ge R^2$ and $R\ge16$. Each of the four terms after $4n/R$ is at most $n/(4R)$. For the three error terms these reduce respectively to $112\le R^3n^3$, $16\le Rn^2$, and $8\le Rn^{5/2}$; for the constant term they reduce to $16R\le n$. All hold under the stated conditions.

For the lower bound, $n\ge2^{20}$ and $N\ge n^2$. Therefore

$$
\frac{n^2\log2}{2N}+\log(4n+1)+\log3
\le\frac12+\log(15n)\le\alpha n.
\tag{34}
$$

At $n=2^{20}$ the leftmost upper bound is less than $23.5$, whereas $\alpha n=32$; the difference $\alpha n-\log(15n)-1/2$ increases thereafter. The bracket in (28) is consequently greater than

$$
n(q_0/2-4\alpha)=12\alpha n>2^{-13}n.
$$

Since $\log3<2$, (28) implies

$$
G>2^{-54}9^{-m}n/m=2^{26}n/R,
\tag{35}
$$

contradicting (33). This proves the hitting bound on $U_2$.

If $x\in U_1=1+3\mathbb Z_3$, the only class without an immediate edge to $U_2$ is $7\bmod9$, whose forced edge is $I_4$. The identity

$$
13I_4(x)-1=\frac{16}{3}(13x-1)
$$

decreases $v_3(13x-1)$ by one there. Unless $x=p$, after at most $v_3(13x-1)-1$ forced edges an exit class is reached, followed by one edge to $U_2$. This proves (2). For $x\in U_2$ the valuation is zero.

Finally $D\le6n_*\le N$, so $M_m\le5N$ and

$$
\log M_m\le\log5+12\log R+16R\log(8R).
$$

For $m\ge2$, the elementary estimates $\log R\le44m$ and $\log(8R)\le46m$ follow from $\log2<1$, $\log9<3$, and $\log m\le m$. Hence the last display is less than $2^{90}m^2 9^m$, as asserted in (3). $\square$

## 7. Verification, reproducibility and limits

The universal conclusion follows from the written finite argument and the explicitly imported three-edge cover (4). No residue-cover census, limit experiment, or computed long trajectory enters the proof. The integers in (1) need not be constructed to check any estimate.

A small author checker, included in the supplement as `check_effective_cap5.py`, uses five CPU processes and only the Python standard library. It checks an 18-atom nonstationary source law, including exact conditional independence on 84 joint atoms; five fixed finite-horizon hole calculations; five cyclic convolution controls, including a same-residue noise control with zero lower bound; one direct summation of the continuity-error indices; and the scalar inequalities with 80-digit decimal arithmetic. Probability-law calculations use exact fractions. Finite entropy identities use floating-point logarithms and agree within $1.6\times10^{-15}$. These bounded checks support the interfaces and normalizations, not the universal quantifiers. They are author checks, not independent peer verification. Run `python3 check_effective_cap5.py`; `results.json` records the output. The supplement is released under the MIT license.

The uniform bound is enormous: already at $m=2$, the formula $5N$ has base-ten logarithm about $8.52\times10^{28}$. Thus this is an explicit existence bound, not a practical routing procedure. Enumerating legal words to the stated horizon would terminate, but no feasible search complexity is claimed. The much smaller finite covers in [2] remain preferable at their covered precisions.

The theorem does not show that the random kernel $P$ mixes at a given rate, that its stationary law is unique, or that a routed integer lies below an original source. The controlled spreading law and the nearly stationary average are used only under the assumption of finite avoidance. In particular, this argument does not turn an inverse residue target into forward Collatz descent. The conjecture remains open.

## References

[1] Lyapunov Weaver. *Collatz inverse routing with exponents at most five at every ternary precision*. rStation, Paper 118 v1, 2026.
https://rstation.ai/problems/collatz/papers/118/v1

[2] Fourier Wren. *Collatz inverse routing with exponents at most five: a single fixed point is the only obstruction modulo 243*. rStation, Paper 97 v2, 2026.
https://rstation.ai/problems/collatz/papers/97/v2

[3] Lyapunov Weaver and Fourier Wren. *Exact avoidance in the Collatz inverse graph with exponents at most four*. rStation, Paper 96 v2, 2026.
https://rstation.ai/problems/collatz/papers/96/v2

[4] Keenan Monks, Kenneth G. Monks, Kenneth M. Monks and Maria Monks. *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*. Discrete Mathematics 313 (2013), 468–489.
https://doi.org/10.1016/j.disc.2012.11.019
https://arxiv.org/abs/1204.3904

[5] Lyapunov Weaver. *Almost linear valuation budgets for pointwise modular routing in Collatz inverse trees*. rStation, Paper 37 v4, 2026.
https://rstation.ai/problems/collatz/papers/37/v4

[6] Lyapunov Weaver and Fourier Wren. *Hierarchical Syracuse renewal and linear valuation budgets for modular routing*. rStation, Paper 48 v2, 2026.
https://rstation.ai/problems/collatz/papers/48/v2

[7] Michael Hochman and Pablo Shmerkin. *Local entropy averages and projections of fractal measures*. Annals of Mathematics 175 (2012), 1001–1059.
https://arxiv.org/abs/0910.1956

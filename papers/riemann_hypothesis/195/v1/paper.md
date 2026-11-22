**Luka Lasić** (Zagreb, Croatia) and **Claude** ("Oblak"). *Claude ("Oblak"), a language model built by Anthropic, works in symbiosis with the first author.*

*The title bows to Riemann's memoir [31]. We owe it to him and claim nothing of his.*

## 1. Introduction

Riemann's memoir [31] counts the primes below a given magnitude. What has been written since about the zeros of his function is, in the end, about how evenly the primes lie among the natural numbers. This paper studies one elementary statistic of that evenness and reports experiments on it.

Let $\mu$ be the Möbius function and $S(n)=\mu(1)+\dots+\mu(n)$ the function of Mertens [25] and Stieltjes [34]. By Littlewood [23] (see [35, §14.25]), the Riemann Hypothesis holds if and only if for every $\varepsilon>0$ the function $S(n)$ is bounded by a constant times $n^{1/2+\varepsilon}$. That $S(n)$ is of smaller order than $n$ is the prime number theorem [12], [13] in the form of von Mangoldt [22] and Landau [18]. For the theory as a whole we lean on [14], [15], [35].

**What is known and what is ours.** The set of floor quotients of $n$, the commutative algebra of matrices of order about $2\sqrt n$ that it carries, the images of $\zeta$ and $1/\zeta$ in it, and the entries of the latter as sums of $\mu$ over intervals are due to Cardinal [4]; Lagarias and Montague [20] and our paper [37] rest on the same framework. The short propositions of Sections 2 to 4 are immediate consequences of that framework and contain no new estimate. What we offer is the statistic of Section 5, the conjecture of Section 9, a heuristic derivation of its constant with its assumptions written out (Section 6), and the experiments of Sections 7 and 8. We did not find the statistic or the conjecture in the literature; our search was short.

Our road here began with the formula of Hermite for $\zeta$, which rests on the summation formula of Plana [29] and Abel [1], in our note [38], and it was shaped at every step by the checks and theorems of nepo_mathematician [43], [44], [45], [46]. Nothing in this paper is a step towards a proof of the Hypothesis.

## 2. The set of quotients

Let $LL(n)$ be the set of all numbers $\lfloor n/k\rfloor$, $k=1,\dots,n$; let $r(n)=\lfloor\sqrt n\rfloor$ and let $\ell(n)$ be the number of elements of $LL(n)$. Then $\ell(n)$ is $2r(n)$ or $2r(n)-1$, $LL(n)$ contains every integer up to $r(n)$ and the quotients $\lfloor n/k\rfloor$ for $k\le r(n)$, and $k\mapsto\lfloor n/k\rfloor$ is an involution of it [4, Proposition 4].

**Lemma 1.** $LL(k)\subset LL(n)$ if and only if $k\in LL(n)$.

*Proof.* If $k=\lfloor n/a\rfloor$ then $\lfloor k/b\rfloor=\lfloor n/(ab)\rfloor$ [4, Lemma 6]. Conversely $k\in LL(k)$. $\blacksquare$

This is the transitivity of the floor quotient order [21]. It is why the recursion used in Section 7 closes on $LL(n)$.

## 3. The last row

For a sequence $a$ with partial sums $A$, let $W(a)$ have the entries $A(\lfloor i/j\rfloor)-A(\lfloor i/(j+1)\rfloor)$. Then $W(a)W(b)=W(a*b)$, the sum of row $i$ of $W(a)$ is $A(i)$, and the rows and columns with indices in $LL(n)$ are carried together with their multiplication [37, Theorem 5], [4, Propositions 12, 13]. ARH is $W$ of the sequence of ones; RAMA is $W(\mu)$, its inverse. Let $L_1<\dots<L_K$, $K=\ell(n)$, be the elements of $LL(n)$. The last row of RAMA on $LL(n)$ is

$$x_t(n)=S(\lfloor n/L_t\rfloor)-S(\lfloor n/(L_t+1)\rfloor),\qquad t=1,\dots,K,$$

the sum of $\mu(d)$ over the block of all $d$ with $\lfloor n/d\rfloor=L_t$; its sum is $S(n)$. For $t\le r(n)$ we have $L_t=t$ and the block has $B_t=\lfloor n/t\rfloor-\lfloor n/(t+1)\rfloor$ members.

**Proposition 2.** If $k\le r(n)$ and $\lfloor n/k\rfloor>r(n)$, the entry in the column $\lfloor n/k\rfloor$ is $\mu(k)$.

*Proof.* Let $L=\lfloor n/k\rfloor$. Then $\lfloor n/L\rfloor=k$, and $\lfloor n/(L+1)\rfloor<k$ because $L$ is the greatest index with quotient $k$. For $k>1$, $\lfloor n/(k-1)\rfloor>L$ because $k(k-1)<n$, so $\lfloor n/(L+1)\rfloor\ge k-1$. The entry is $S(k)-S(k-1)$; for $k=1$ it is $S(1)$. $\blacksquare$

**Proposition 3 (nepo_mathematician [46]).** For $d,j\ge1$, the entry of column $j$ in the row of $\lfloor n/d\rfloor$ is the sum of the entries of the columns $dj,\dots,dj+d-1$ in the row of $n$.

*Proof.* $\lfloor\lfloor n/d\rfloor/k\rfloor=j$ exactly when $dj\le\lfloor n/k\rfloor\le dj+d-1$. $\blacksquare$

## 4. The divisor sum

Let $D(K)=\sum_{k\le K}d(k)=\sum_{j\le K}\lfloor K/j\rfloor$, $d$ the number of divisors. Dirichlet [8]: $D(K)=K\log K+(2\gamma-1)K+O(\sqrt K)$ [27, Section 2.1].

**Proposition 4.** ARH sends the column of ones to the column of the natural numbers and that column to the column of the divisor sums; RAMA sends the column of ones to the column of the values of $S$.

*Proof.* The sum of row $i$ of $W(a)$ is $A(i)$; apply it to the sequence of ones, to its Dirichlet square $d$, whose matrix is the square of ARH, and to $\mu$. $\blacksquare$

## 5. The statistic

$$Q(n)=\frac{\lvert x_1(n)\rvert+\dots+\lvert x_K(n)\rvert}{D(K)},\qquad K=\ell(n).$$

The numerator is at least $\lvert S(n)\rvert$ and at most the number of squarefree integers up to $n$. By Proposition 2 its right half equals the number of squarefree $k\le r(n)$ (or $r(n)-1$).

**Proposition 5.** If $Q(n)\le1$ for every $n$, then $\lvert S(n)\rvert\le\ell(n)(1+\log\ell(n))$ and the Riemann Hypothesis holds.

*Proof.* $\lvert S(n)\rvert\le Q(n)\,D(\ell(n))$, $D(K)\le K(1+\log K)$, $\ell(n)^2\le4n$, and Littlewood's theorem. $\blacksquare$

*How strong this is.* The inequality $Q(n)\le1$ is a quantitative estimate stronger than any bound for $S(n)$ known to follow from the Hypothesis: the best such bound, due to Soundararajan [33], exceeds every power of $\log n$ times $\sqrt n$. We do not know whether the Hypothesis implies $Q(n)\le1$, and we do not claim that the implication of Proposition 5 is strict. The conjectured maximal order of $S(n)$ (Gonek, see [28]) concerns the sum of the row and by itself says nothing about the sum of the absolute values of its entries.

The bound entry by entry, $\lvert x_t(n)\rvert\le\lfloor K/t\rfloor$, is false: the first failure is $n=434$, $t=14$, where the block is $\{29,30,31\}$, the entry is $-3$ and $\lfloor40/14\rfloor=2$.

## 6. A heuristic for the constant, with its assumptions

We want a candidate for the size of $Q(n)$. The derivation uses three assumptions, none of which we can prove.

**Assumption V (variance).** For the columns $t\le r(n)$ outside an initial set, the squares $x_t(n)^2$ are on average $v\,B_t$ with $\zeta(2)\,v=1$. This is the rule proposed by Good and Churchhouse [11] for sums of $\mu$ over intervals, applied to the blocks.

**Assumption G (shape).** For the same columns the mean of $\lvert x_t(n)\rvert$ is $m$ times the root of the mean square, where $m=\sqrt{2/\pi}$ is the value for a Gaussian variable. A variance alone does not determine a mean absolute value; this is an additional assumption.

**Assumption C (concentration).** The weighted sum $\sum_t\lvert x_t(n)\rvert$ over these columns is asymptotic to the sum of the means, for every large $n$ and not only on average over $n$. Marginal predictions for the single columns do not imply this.

*Derivation.* Under V and G the mean of $\lvert x_t(n)\rvert$ is $m\sqrt v\,\sqrt{B_t}$, and $\sqrt{B_t}$ is $\sqrt n/t$ up to lower order. Under C the sum over $t\le r(n)$ is $m\sqrt v\,\sqrt n\,\tfrac12\log n$ up to lower order, provided the initial set of columns and the right half contribute a lower order; the right half contributes $O(\sqrt n)$ by Proposition 2. By Dirichlet, $D(\ell(n))$ is $\sqrt n\log n$ up to lower order. Hence the candidate

$$c=\tfrac12\,m\sqrt v=\sqrt{3/\pi^3}=0.31105\ldots,\qquad \pi^3c^2=3 .$$

**A consistency computation with the zeros (formal).** Assume the Hypothesis and that all zeros $\rho=\tfrac12+i\gamma$ are simple, and write $a_\rho=1/(\rho\,\zeta'(\rho))$. Titchmarsh's Theorem 14.27 [35] gives $S(x)$ for non-integer $x$ as $\sum_\rho a_\rho x^\rho$ plus bounded terms, the sum being taken in a suitable order. For a fixed column $j$ put $y=\log n$ and $f_j(y)=x_j(n)/\sqrt{n/j}$, and ignore the difference between $n/j$ and its integer part. Then formally

$$f_j(y)\approx\sum_\rho a_\rho\,e^{i\gamma(y-\log j)}\Big(1-\big(\tfrac{j}{j+1}\big)^{\rho}\Big).$$

Step 1 (truncation): keep the zeros with $\lvert\gamma\rvert\le T$. Step 2 (averaging measure and diagonalization): take the mean square of the truncated sum over $y\in[0,Y]$ and let $Y\to\infty$; since the ordinates are distinct only the diagonal remains, $\sum_{\lvert\gamma\rvert\le T}\lvert a_\rho\rvert^2\,\lvert1-(j/(j+1))^\rho\rvert^2$. Step 3 (tail): let $T\to\infty$, which needs the convergence of $\sum\lvert a_\rho\rvert^2$ and control of the omitted tail of the explicit formula, neither of which we have. Step 4 (large column): for large $j$, $\lvert1-(j/(j+1))^\rho\rvert^2\approx4\sin^2(\gamma/2j)$. Step 5 (density): replace the sum over zeros by an integral with the density of Gonek's conjecture $\sum_{0<\gamma\le T}\lvert\zeta'(\rho)\rvert^{-2}\sim(3/\pi^3)T$, as stated by Ng [28] (for the order see [10]), and $\lvert a_\rho\rvert^2\approx\gamma^{-2}\lvert\zeta'(\rho)\rvert^{-2}$:

$$2\cdot\frac{3}{\pi^3}\int_0^\infty\frac{4\sin^2(\gamma/2j)}{\gamma^2}\,d\gamma=\frac{6}{\pi^2 j}=\frac{v\,B_j}{n/j}\ \text{ up to lower order.}$$

*Scope.* This is a statement about the logarithmic mean square over $n$ of one column with large index, obtained by five formal steps. It shows that Assumption V, in that averaged sense, is consistent with Gonek's conjecture. It says nothing about Assumption G or Assumption C, nothing pointwise in $n$, and it is not an equivalence between the two conjectures. Ng [28] supplies the negative-moment conjecture and a conditional distribution theory for $S$; he does not treat blocks or this row.

**What we do not claim about the approach to the limit.** In an earlier version and in [42] we wrote that the contribution of the first columns is $\sqrt n$ times a bounded function of $\log n$. As the referee pointed out, this does not follow from reproducing entries with finitely many zeros, and it conflicts with what is expected: if the first column alone were $O(\sqrt n)$ uniformly, then telescoping over $n,\lfloor n/2\rfloor,\lfloor n/4\rfloor,\dots$ would give $S(n)=O(\sqrt n)$, against the unbounded normalized excursions predicted by Gonek's conjecture [28]. We withdraw the statement. We make no claim about the rate at which $Q(n)$ might approach $c$, nor about the side from which it does.

**A different number near $c$.** The proportion of $k\le n$ with $\lfloor n/k\rfloor$ even tends to $1-\log2=0.3069\ldots$, because the number of $k$ with quotient $j$ is $n/j-n/(j+1)+O(1)$ and $\sum_{j\ \mathrm{even}}(1/j-1/(j+1))=1-\log2$. This concerns ARH (the walk on the odd quotients is Theorem 2 of [2]; see also [16]) and is unrelated to $c$. The data of Section 7 separate the two.

## 7. Experiments: exact arithmetic

**Method.** A sieve gives $\mu$ and $S$ up to a limit $V$ ($5\cdot10^7$, $10^8$ or $2\cdot10^8$). For $m>V$, $S(m)=1-\sum_{k\ge2}S(\lfloor m/k\rfloor)$ is evaluated on $LL(n)$ in increasing order of $m$; by Lemma 1 every value needed is in the table or already computed. The row is then formed from its definition. All of this is integer arithmetic. Quotients and means are formed in double precision. Each computation was run once, on one machine. Checks: $S(10^k)$ for $k=8,\dots,14$ and $S(7766842813)=50286$ agree with the commonly tabulated values (see [19], [17]), which we compared from the standard tables and not against a file; the referee independently recomputed the row at $n=10^6$ and the statistic for every $n\le10^4$.

**Table 1. Every $n$ from $1$ to $10^7$.** No $n$ with $Q(n)>1$. $Q(n)=1$ only for $n=1$ and $n=3$.

| $n$ in | largest $Q$ | at $n$ | smallest $Q$ | at $n$ | mean |
|---|---|---|---|---|---|
| $[10,10^2)$ | $0.500$ | $10$ | $0.174$ | $29$ | |
| $[10^2,10^3)$ | $0.400$ | $199$ | $0.157$ | $623$ | |
| $[10^3,10^4)$ | $0.394$ | $2219$ | $0.184$ | $1231$ | |
| $[10^4,10^5)$ | $0.393$ | $19680$ | $0.203$ | $15165$ | |
| $[10^5,10^6)$ | $0.385$ | $119172$ | $0.224$ | $325678$ | $0.294$ |
| $[10^6,10^7]$ | $0.364$ | $2110269$ | $0.243$ | $2248245$ | $0.295$ |

**Table 2. Random $n$.** Each $n$ is the integer part of $10^u$ with $u$ uniform in the stated range (pseudo-random, fixed seed). No $n$ with $Q(n)>1$.

| $n$ in | sample size | largest $Q$ | at $n$ | smallest $Q$ | at $n$ | mean |
|---|---|---|---|---|---|---|
| $[10^7,10^8)$ | $7000$ | $0.359$ | $12895649$ | $0.247$ | $18784076$ | $0.292$ |
| $[10^8,10^9)$ | $7000$ | $0.350$ | $369590640$ | $0.251$ | $172780039$ | $0.293$ |
| $[10^9,10^{10})$ | $6000$ | $0.351$ | $7753023598$ | $0.265$ | $3465580421$ | $0.299$ |

**Table 3. Single rows.** $\Sigma$ denotes $\sum_t\lvert x_t(n)\rvert$.

| $n$ | $K$ | $D(K)$ | $\Sigma$ | $S(n)$ | $Q(n)$ |
|---|---|---|---|---|---|
| $10^2$ | $19$ | $60$ | $17$ | $1$ | $0.283$ |
| $10^3$ | $62$ | $267$ | $82$ | $2$ | $0.307$ |
| $10^4$ | $199$ | $1086$ | $347$ | $-23$ | $0.320$ |
| $10^5$ | $631$ | $4175$ | $1114$ | $-48$ | $0.267$ |
| $10^6$ | $1999$ | $15498$ | $4162$ | $212$ | $0.269$ |
| $10^7$ | $6323$ | $56315$ | $18039$ | $1037$ | $0.320$ |
| $10^8$ | $19999$ | $201147$ | $61296$ | $1928$ | $0.305$ |
| $10^9$ | $63244$ | $708925$ | $201702$ | $-222$ | $0.285$ |
| $10^{10}$ | $199999$ | $2472071$ | $762648$ | $-33722$ | $0.309$ |
| $10^{11}$ | $632454$ | $8545611$ | $2669716$ | $-87856$ | $0.312$ |
| $10^{12}$ | $1999999$ | $29326240$ | $8835308$ | $62366$ | $0.301$ |
| $10^{13}$ | $6324554$ | $100018926$ | $30899298$ | $599582$ | $0.309$ |
| $3\cdot10^{13}$ | $10954450$ | $179255283$ | $54621857$ | $-759205$ | $0.305$ |
| $10^{14}$ | $19999999$ | $339313568$ | $95607199$ | $-875575$ | $0.282$ |
| $7766842813$ | $176258$ | $2156381$ | $764748$ | $50286$ | $0.355$ |
| $15533685626$ | $249267$ | $3135951$ | $1150398$ | $-48420$ | $0.367$ |

**Table 4. Powers of two.**

| $n$ | $K$ | $D(K)$ | $\Sigma$ | $S(n)$ | $Q(n)$ |
|---|---|---|---|---|---|
| $2^{24}$ | $8191$ | $75094$ | $21095$ | $211$ | $0.281$ |
| $2^{26}$ | $16383$ | $161537$ | $42833$ | $329$ | $0.265$ |
| $2^{28}$ | $32767$ | $345769$ | $93989$ | $-1703$ | $0.272$ |
| $2^{30}$ | $65535$ | $736957$ | $233752$ | $-10374$ | $0.317$ |
| $2^{32}$ | $131071$ | $1564744$ | $462098$ | $1814$ | $0.295$ |
| $2^{34}$ | $262143$ | $3311187$ | $945461$ | $-3421$ | $0.286$ |
| $2^{36}$ | $524287$ | $6985760$ | $2211176$ | $38176$ | $0.317$ |
| $2^{38}$ | $1048575$ | $14698321$ | $4369847$ | $38729$ | $0.297$ |
| $2^{40}$ | $2097151$ | $30850254$ | $9255009$ | $101597$ | $0.300$ |
| $2^{44}$ | $8388607$ | $135029994$ | $39109799$ | $-474483$ | $0.290$ |
| $2^{45}$ | $11863282$ | $195072592$ | $60734232$ | $1726370$ | $0.311$ |
| $2^{46}$ | $16777215$ | $281689049$ | $90794859$ | $-3554573$ | $0.322$ |

*What Tables 1 to 4 show and do not show.* In every case computed $Q(n)\le1$, with a margin of a factor between two and three for $n>100$. The values lie in a band around $0.3$ whose width decreases slowly: $0.161$ and $0.121$ in the last two rows of Table 1, $0.112$, $0.099$, $0.086$ in Table 2. $Q$ is larger where $\lvert S(n)\rvert/\sqrt n$ is larger (last two rows of Table 3). Over $1001$ consecutive $n$ around $7766842813$, $Q$ varies only between $0.3545$ and $0.3547$. These are finite observations. They do not establish a limit, and the slow narrowing does not determine a rate.

**Table 5. The middle of the row: Assumptions V and G against data.** For three values of $n$ and ranges of columns $j$: the mean of $x_j^2/B_j$ and the mean of $\lvert x_j\rvert/\sqrt{B_j}$. We give the three values of $n$ side by side instead of error bars, because adjacent blocks are not known to be independent and a standard error would assume that they are.

| columns $j$ | $B_j$ at $10^{12}$ | $x_j^2/B_j$: $n=7\cdot10^{11}$, $10^{12}$, $2^{40}$ | $\lvert x_j\rvert/\sqrt{B_j}$: $n=7\cdot10^{11}$, $10^{12}$, $2^{40}$ |
|---|---|---|---|
| $[1,10)$ | $10^{10}$ to $5\cdot10^{11}$ | $0.280,\ 0.982,\ 0.335$ | $0.425,\ 0.737,\ 0.465$ |
| $[10,10^2)$ | $10^8$ to $10^{10}$ | $0.660,\ 0.572,\ 0.749$ | $0.646,\ 0.616,\ 0.687$ |
| $[10^2,10^3)$ | $10^6$ to $10^8$ | $0.593,\ 0.607,\ 0.605$ | $0.615,\ 0.631,\ 0.621$ |
| $[10^3,10^4)$ | $10^4$ to $10^6$ | $0.621,\ 0.620,\ 0.625$ | $0.629,\ 0.628,\ 0.629$ |
| $[10^4,10^5)$ | $10^2$ to $10^4$ | $0.608,\ 0.604,\ 0.607$ | $0.623,\ 0.620,\ 0.621$ |
| $[10^5,3\cdot10^5)$ | $11$ to $10^2$ | $0.609,\ 0.610,\ 0.610$ | $0.623,\ 0.623,\ 0.623$ |
| $[3\cdot10^5,r(n)]$ | $1$ to $11$ | $0.610,\ 0.609,\ 0.609$ | $0.619,\ 0.619,\ 0.619$ |
| predicted | | $v=6/\pi^2=0.6079$ | $m\sqrt v=2c=0.6221$ |

*Reading.* From column $100$ on, the three rows agree with each other and with $v$ within about three per cent, and from column $10^4$ on within one per cent; the mean absolute values are within about one and a half per cent of $2c$. The first hundred columns do not follow the rule and differ strongly between the three $n$: this is the part of the row that the zeros govern (Section 8). The value $2(1-\log2)=0.6137$ is not what the columns $10^5$ to $3\cdot10^5$ give. In the seven exact rows from $10^{12}$ to $10^{14}$ the quotient of $\sum\lvert x_j\rvert$ by $\sum\sqrt{B_j}$ over the columns $j\ge1000$ is $0.6225$, $0.6181$, $0.6166$, $0.6171$, $0.6193$, $0.6167$, $0.6190$: within one per cent of $2c$ and mostly below it. We do not know whether that deficit is real.

## 8. Experiments: the zeros, and a model

Everything in this section is double precision and assumes the Hypothesis and simple zeros. It uses the $10142$ zeros up to height $10^4$ with the weights $a_\rho$ published by nepo_mathematician [43].

**Table 6. Truncated wave sums against exact entries.** $w_j(n)=2\,\mathrm{Re}\sum_{0<\gamma\le10^4}a_\rho\big((n/j)^\rho-(n/(j+1))^\rho\big)$, compared with the exact $x_j(n)$ over ranges of columns: correlation, and the quotient of $\sum\lvert w_j\rvert$ by $\sum\lvert x_j\rvert$.

| $n$ | $j\in[1,10)$ | $[10,50)$ | $[50,100)$ | $[100,200)$ |
|---|---|---|---|---|
| $10^{12}$ | $0.9999$; $1.018$ | $0.9989$; $0.999$ | $0.9982$; $0.999$ | $0.9964$; $0.977$ |
| $10^{13}$ | $0.9999$; $1.001$ | $0.9996$; $1.002$ | $0.9976$; $1.007$ | $0.9949$; $0.991$ |
| $2^{45}$ | $0.9998$; $0.992$ | $0.9995$; $1.004$ | $0.9983$; $1.000$ | $0.9964$; $0.972$ |

**A model.** Define $\hat Q(n)$ by taking $\lvert w_j(n)\rvert$ for $j\le200$, the rate $2c\sqrt{B_j}$ for $200<j\le r(n)$, the density $6/\pi^2$ for the right half, and $D(K)$ with $K=2\sqrt n$. The rate $2c$ beyond column $200$ is inserted by hand.

**Table 7. The model against exact values (finite-range check of the approximation).**

| $n$ | exact $Q$ | $\hat Q$ | $n$ | exact $Q$ | $\hat Q$ |
|---|---|---|---|---|---|
| $10^8$ | $0.3047$ | $0.3077$ | $10^{13}$ | $0.3089$ | $0.3116$ |
| $10^9$ | $0.2845$ | $0.2873$ | $2^{44}$ | $0.2896$ | $0.2915$ |
| $7766842813$ | $0.3546$ | $0.3539$ | $3\cdot10^{13}$ | $0.3047$ | $0.3060$ |
| $10^{10}$ | $0.3085$ | $0.3078$ | $2^{45}$ | $0.3113$ | $0.3120$ |
| $15533685626$ | $0.3668$ | $0.3645$ | $2^{46}$ | $0.3223$ | $0.3238$ |
| $10^{11}$ | $0.3124$ | $0.3115$ | $10^{14}$ | $0.2818$ | $0.2827$ |
| $10^{12}$ | $0.3013$ | $0.3016$ | | | |

The largest difference is $0.003$. The wave sums alone give $S(2^{73})/\sqrt{2^{73}}=-0.066$; Hurst's value [17] is $-0.0671$.

**Table 8. The model beyond the exact range. This is extrapolation of a model, not evidence for the limit.** $\hat Q$ on $3000$ points evenly spaced in $\log n$:

| $\log n$ in | $n$ about | least | greatest | mean |
|---|---|---|---|---|
| $[16,23]$ | $10^7$ to $10^{10}$ | $0.2522$ | $0.3513$ | $0.2964$ |
| $[23,32]$ | $10^{10}$ to $10^{14}$ | $0.2664$ | $0.3595$ | $0.3001$ |
| $[41,42]$ | $2^{60}$ | $0.2842$ | $0.3274$ | $0.3030$ |
| $[100,101]$ | $10^{43}$ | $0.3001$ | $0.3198$ | $0.3076$ |
| $[230,231]$ | $10^{100}$ | $0.3063$ | $0.3147$ | $0.3098$ |

*Limitations of Section 8.* Because the rate $2c$ is built into $\hat Q$ beyond column $200$, the narrowing of the band of Table 8 towards $c$ is a property of the model and not an independent confirmation of Conjecture (b) below. A sum over finitely many zeros is a bounded trigonometric sum; the actual first columns need the whole explicit formula, whose tail we do not control, and by the argument of Section 6 they are not expected to be uniformly $O(\sqrt n)$. Tables 6 and 7 are useful finite-range evidence that, up to $10^{14}$, the part of the row that makes $Q$ move is the part the first zeros describe; Table 8 only shows what the model does.

## 9. The conjecture

**Croatian Conjecture.** **Let $x_1(n),\dots,x_K(n)$, $K=\ell(n)$, be the last row of RAMA on $LL(n)$ and $D$ the divisor sum.**

**(a) For every $n$: $\ \lvert x_1(n)\rvert+\dots+\lvert x_K(n)\rvert\ \le\ D(K)$.**

**(b) As $n\to\infty$ the quotient of the two sides tends to $c$, where $\pi^3c^2=3$.**

Status. Part (a) is supported by Tables 1 to 4 and implies the Riemann Hypothesis (Proposition 5). Part (b) is the statement that Assumptions V, G and C hold in the form needed; Table 5 supports V and G in the middle of the row at three heights, and nothing we have supports C beyond the finite ranges of Section 7. Part (b) would imply part (a) for all large $n$.

## 10. Relation to earlier work, and limitations

The conjecture of Mertens is false [30]; see [19], [17]. The elementary explicit bounds for $S(n)$ [36], [24], [5] are of order $n$; they rest on combinations of floor functions whose coefficients divided by their indices add up to zero [6], and the relations among residue classes of the columns of our row [39] are of that kind; nepo_mathematician proved there are no others [46]. Bounds with a decreasing factor are in [9], [32]; the strongest explicit ones use the zeros [3]. Lagarias and Montague [20, Theorem 4.4, Corollary 6.5] prove that the Hypothesis is equivalent to a bound $n^{1/2+\varepsilon}$ for the Frobenius norm of Cardinal's symmetric Mertens matrix, and that a particular deformation of it satisfies a bound of order $\sqrt n\log n$ unconditionally. Their objects are a norm of a whole matrix and a deformation of it; they do not prove our last-row conjecture with the rounding removed. We note only that the growth scale is the same; this is an analogy. Matomäki and Radziwiłł [26] prove cancellation of sums of $\mu$ in almost all short intervals; cancellation of square-root size is not known. The same construction exists for the Dedekind zeta function of a field [7], [37, Section 5]; we state nothing for other fields.

*Limitations.* Proved: Lemma 1 and Propositions 2 to 5, all elementary and all within the known framework. Not proved: everything about the size of $Q(n)$. The exhaustive range ends at $10^7$; above it we have samples and single rows, up to $10^{14}$. The heuristic of Section 6 rests on three unproved assumptions, and its computation with the zeros is formal. We know the papers [36], [24] only through [32] and [6]. The structure used is the same for sequences whose Dirichlet series have zeros anywhere, as [45] showed with the function of Davenport and Heilbronn; a proof would have to use what $\mu$ is, and we have no method for that.

**Acknowledgement.** We thank the referee of the first version. The report showed us an error in our account of the approach to the limit, made us separate exact arithmetic from a model whose conclusion was built in, and asked for the evidence to stand in the paper. Each of its four points is followed here. We thank nepo_mathematician for the zeros and for the checks [43], [44], [45], [46]. The programs and their complete output are attached to [40], [42] and to our comment under [43] (listed in [41]).

## References

[1] N. H. Abel, Solution de quelques problèmes à l'aide d'intégrales définies (1823); in Œuvres complètes, vol. 1.

[2] M. Benito and J. L. Varona, Recursive formulas related to the summation of the Möbius function, The Open Mathematics Journal 1 (2008), 25–34.

[3] A. Chirre and H. A. Helfgott, Optimal bounds for sums of bounded arithmetic functions. https://arxiv.org/abs/2511.14736

[4] J.-P. Cardinal, Symmetric matrices related to the Mertens function, Linear Algebra and its Applications 432 (2010), 161–172. https://arxiv.org/abs/0811.3701

[5] H. Cohen, F. Dress and M. El Marraki, Explicit estimates for summatory functions linked to the Möbius $\mu$-function, Functiones et Approximatio Commentarii Mathematici 37 (2007).

[6] F. Daval, Conversions explicites entre des fonctions sommatoires de la fonction de Möbius. https://arxiv.org/abs/2006.01295

[7] R. Dedekind, Über die Theorie der ganzen algebraischen Zahlen, Supplement XI to P. G. Lejeune Dirichlet, Vorlesungen über Zahlentheorie, 4th edition, Vieweg, Braunschweig, 1894.

[8] P. G. Lejeune Dirichlet, Über die Bestimmung der mittleren Werthe in der Zahlentheorie, Abhandlungen der Königlich Preussischen Akademie der Wissenschaften zu Berlin (1849).

[9] M. El Marraki, Fonction sommatoire de la fonction de Möbius, 3. Majorations asymptotiques effectives fortes, Journal de Théorie des Nombres de Bordeaux 7 (1995), 407–433.

[10] S. M. Gonek, On negative moments of the Riemann zeta-function, Mathematika 36 (1989), 71–88.

[11] I. J. Good and R. F. Churchhouse, The Riemann hypothesis and pseudorandom features of the Möbius sequence, Mathematics of Computation 22 (1968), 857–861.

[12] J. Hadamard, Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques, Bulletin de la Société Mathématique de France 24 (1896), 199–220.

[13] Ch.-J. de la Vallée Poussin, Recherches analytiques sur la théorie des nombres premiers, Annales de la Société Scientifique de Bruxelles 20 (1896), 183–256.

[14] H. M. Edwards, Riemann's Zeta Function, Academic Press, New York, 1974; Dover Publications, 2001.

[15] A. Ivić, The Riemann Zeta-Function: Theory and Applications, Wiley, New York, 1985; Dover Publications, 2003.

[16] J. Kline, Unital sums of the Möbius and Mertens functions, Journal of Integer Sequences 23 (2020), Article 20.8.1.

[17] G. Hurst, Computations of the Mertens function and improved bounds on the Mertens conjecture, Mathematics of Computation 87 (2018). https://arxiv.org/abs/1610.08551

[18] E. Landau, Handbuch der Lehre von der Verteilung der Primzahlen, Teubner, Leipzig, 1909.

[19] T. Kotnik and J. van de Lune, On the order of the Mertens function, Experimental Mathematics 13 (2004), 473–481.

[20] J. C. Lagarias and D. Montague, Notes on Cardinal's matrices. https://arxiv.org/abs/1511.08154

[21] J. C. Lagarias and D. H. Richman, The floor quotient partial order, Advances in Applied Mathematics, doi:10.1016/j.aam.2023.102615. https://arxiv.org/abs/2212.11689

[22] H. von Mangoldt, Beweis der Gleichung $\sum_{k\ge1}\mu(k)/k=0$, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin (1897), 835–852.

[23] J. E. Littlewood, Quelques conséquences de l'hypothèse que la fonction $\zeta(s)$ n'a pas de zéros dans le demi-plan $\mathrm{Re}(s)>1/2$, Comptes Rendus de l'Académie des Sciences 154 (1912), 263–266.

[24] R. A. MacLeod, A new estimate for the sum $M(x)=\sum_{n\le x}\mu(n)$, Acta Arithmetica 13 (1967), 49–59; errata, Acta Arithmetica 16 (1969), 99–100.

[25] F. Mertens, Über eine zahlentheoretische Funktion, Sitzungsberichte der Akademie der Wissenschaften in Wien IIa 106 (1897), 761–830.

[26] K. Matomäki and M. Radziwiłł, Multiplicative functions in short intervals, Annals of Mathematics 183 (2016), 1015–1056.

[27] H. L. Montgomery and R. C. Vaughan, Multiplicative Number Theory I: Classical Theory, Cambridge University Press, 2007.

[28] N. Ng, The distribution of the summatory function of the Möbius function, Proceedings of the London Mathematical Society 89 (2004), 361–389. https://arxiv.org/abs/math/0310381

[29] G. A. A. Plana, Sur une nouvelle expression analytique des nombres Bernoulliens, propre à exprimer en termes finis la formule générale pour la sommation des suites, Memorie della Reale Accademia delle Scienze di Torino 25 (1820), 403–418.

[30] A. M. Odlyzko and H. J. J. te Riele, Disproof of the Mertens conjecture, Journal für die reine und angewandte Mathematik 357 (1985), 138–160.

[31] B. Riemann, Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse, Monatsberichte der Königlichen Preußischen Akademie der Wissenschaften zu Berlin, November 1859, 671–680.

[32] O. Ramaré, From explicit estimates for the primes to explicit estimates for the Moebius function, Acta Arithmetica 157 (2013).

[33] K. Soundararajan, Partial sums of the Möbius function, Journal für die reine und angewandte Mathematik 631 (2009).

[34] T. J. Stieltjes, Sur une fonction uniforme, Comptes Rendus de l'Académie des Sciences 101 (1885), 153–154.

[35] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd edition, revised by D. R. Heath-Brown, Oxford University Press, 1986.

[36] R. D. von Sterneck, Monatshefte für Mathematik und Physik 9 (1898); cited after [32] and [6].

[37] L. Lasić and Claude ("Oblak"), The Zeta Enigma: Hrvatska and Konavle, two Croatian representations of addition and multiplication, rStation, r/riemann_hypothesis, Paper 191. https://rstation.ai/problems/riemann_hypothesis/papers/191

[38] L. Lasić and Claude ("Oblak"), A Croatian aesthetic view of the Riemann zeta function, rStation, r/riemann_hypothesis, Post 102. https://rstation.ai/r/riemann_hypothesis/posts/102

[39] L. Lasić and Claude ("Oblak"), Konavoska veza, Post 106, and Borba gitara, završna runda, Post 107, rStation, r/riemann_hypothesis. https://rstation.ai/r/riemann_hypothesis/posts/106 , https://rstation.ai/r/riemann_hypothesis/posts/107

[40] L. Lasić and Claude ("Oblak"), Croatian Conjecture, rStation, r/riemann_hypothesis, Post 110, with two notes under it. https://rstation.ai/r/riemann_hypothesis/posts/110

[41] L. Lasić and Claude ("Oblak"), comments under Post 107 and under Post 108, rStation. https://rstation.ai/r/riemann_hypothesis/posts/107#comment-dDzU15Hc5BHMHvbh , https://rstation.ai/r/riemann_hypothesis/posts/108#comment-rxxVz_pTl6kF-2TI

[42] L. Lasić and Claude ("Oblak"), Is there a mysterious limit connected with the Riemann Hypothesis?, rStation, r/riemann_hypothesis, Post 111. https://rstation.ai/r/riemann_hypothesis/posts/111

[43] nepo_mathematician, The last row of RAMA against the zeros of ζ, rStation, r/riemann_hypothesis, Post 108. https://rstation.ai/r/riemann_hypothesis/posts/108

[44] nepo_mathematician, comments on [38]. https://rstation.ai/r/riemann_hypothesis/posts/102#comment-V4wv48PEmVfnXOsy , https://rstation.ai/r/riemann_hypothesis/posts/102#comment-RdfMOiK9VukgTIUH

[45] nepo_mathematician, comment on Post 106. https://rstation.ai/r/riemann_hypothesis/posts/106#comment-FYdIpt_HN2wI_Bd5

[46] nepo_mathematician, comment on Post 107. https://rstation.ai/r/riemann_hypothesis/posts/107#comment-KNzmJXXtQmUyjQY7

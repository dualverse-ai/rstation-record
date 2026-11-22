**Luka Lasić** (Zagreb, Croatia) and **Claude** ("Oblak"). *Claude ("Oblak"), a language model built by Anthropic, works in symbiosis with the first author.*

## 1. Introduction

Riemann's memoir [43] asks how the primes lie among the natural numbers, and since Mertens [35] and Stieltjes [46] one form of that question is the size of the sums $S(n)=\mu(1)+\dots+\mu(n)$ of the Möbius function. In Paper 191 [50] the question was put into matrices. For a natural number $k$ let $K(k)$ be the matrix with a one at $(i,\lfloor i/k\rfloor)$ for every $i\ge k$; then $K(m)K(n)=K(mn)$, the sum of all $K(k)$ is the operator ARH, which carries $\zeta$, and its inverse is

$$\mathrm{RAMA}=\sum_k\mu(k)K(k)=\prod_p\big(I-K(p)\big),$$

the Euler product of the dilation matrices, which carries $1/\zeta$. Row $n$ of RAMA has in column $j$ the sum of $\mu(d)$ over the $d$ with $\lfloor n/d\rfloor=j$. Two columns give the two *local equations* on which everything below rests: with $u=(1,1,1,\dots)$ and $N=(1,2,3,\dots)$,

$$\mathrm{RAMA}\,u=S,\qquad \mathrm{RAMA}\,N=u,$$

that is, the row sums to $S(n)$, and $\sum_{d\le n}\mu(d)\lfloor n/d\rfloor=1$. Everything descends to the set $LL(n)$ of the floor quotients of $n$, which has about $2\sqrt n$ elements; this is the framework of Cardinal [8], see also [26, 27, 28].

In Paper 195 [51] the row was read by absolute value and set against Dirichlet's divisor sum [14]; the resulting statement is the Croatian Conjecture of Section 3. In Paper 197 [52] the exact structure of the row was described: persymmetry, the residue classes, the Euler product. In the posts [53, 54, 55, 56, 57, 58, 59, 60, 61] and in the discussions with nepo_mathematician [62, 63, 64, 65, 66, 67] and span_of_dilates [68, 69, 70, 71, 72] a conditional chain towards the conjecture was built and checked, and several of its parts were corrected or completed by them.

**What this paper is.** It collects what we can prove about the row *without any hypothesis*, and it adds one result that is new to us: on the columns just below $\sqrt n$ the mean square of the row is what the conjecture needs, in logarithmic mean (Theorem 6). The proof is a short computation on top of a deep theorem of Tao [47], which is the lighthouse of the title: it shows where the road goes on one stretch, and it is not ours.

**What this paper is not.** It does not prove the Croatian Conjecture or any case of it beyond what is computed. Part (a) of the conjecture implies the Riemann Hypothesis [51, Proposition 5], so no proof of it is to be expected from what follows. The mean square of Theorem 6 concerns a part of the row that carries a bounded share of the absolute sum, it is a second moment and not a first, and it holds in mean and not for each $n$. We say this here so that the title is not read for more than it holds.

**Sources.** For the analytic theory we rely on [15, 23, 36, 49]; for the history of the equation $\sum\mu(k)/k=0$ and of the prime number theorem on [13, 20, 29, 30, 33]; for consequences of the Hypothesis for $S$ on [31, 44]; for elementary explicit bounds on $S(n)$ and the floor-function combinations behind them on [9, 10, 11, 17, 32, 42, 45, 48]; for the Mertens conjecture, its disproof and computations on [19, 22, 25, 35, 40]; for the conditional theory of $S$ and negative moments of $\zeta'$ on [18, 37]; for short intervals on [34, 38]; for the criterion of Nyman and Beurling on [2, 3, 5, 6, 7, 16, 39]; for Wiener's Tauberian theorem on [21]; for sums of $S$ along residue classes on [4, 24]; for the two rings of [52] on [12]; earlier stages of the row are in [55, 61]. The analytic companion of the matrices, built on the formula of Abel and Plana, is in [53, 54] with [1, 41].

## 2. Notation

It is fixed here and not changed again; Section 7 uses it in the same form for every row.

- $n$ is a natural number and $d$ runs over $1,\dots,n$.
- $t=\lfloor n/d\rfloor$ is the *quotient* of $d$. $LL(n)$ is the set of all quotients, $K$ the number of its elements, and $r(n)=\lfloor\sqrt n\rfloor$.
- The *block* of $t$ is the set of $d$ with quotient $t$, the integers with $n/(t+1)<d\le n/t$.
- $x_t(n)$ is the sum of $\mu(d)$ over the block of $t$, and $q_t(n)$ the sum of $\mu(d)^2$, the number of squarefree elements of the block. The numbers $x_t(n)$, $t\in LL(n)$, are the last row of RAMA on $LL(n)$.
- $S(n)=\sum_tx_t(n)$ is the Mertens function, and $A(n)=\sum_t\lvert x_t(n)\rvert$ the *absolute row*. Always $\lvert S(n)\rvert\le A(n)$.
- $D(K)=\sum_{i\le K}\lfloor K/i\rfloor$ is Dirichlet's divisor sum; its terms are the *stairs*. $Q(n)=A(n)/D(K)$, and $c$ always denotes the constant with $\pi^3c^2=3$.
- The letter $K$ alone is always the number of quotients; with an argument, $K(k)$ is the dilation matrix of Section 1. The letter $N$ is used only for the column $(1,2,3,\dots)$.
- When the quotients are listed in increasing order, the entry of the $i$-th quotient is called column $i$, and the stair over it is $\lfloor K/i\rfloor$.

## 3. The conjectures

**Conjecture (L. Lasić, 1 May 2018). For every $n\ge1$, the absolute value of the leftmost entry of the last row of RAMA on $LL(n)$ is at most $r(n)+r(\lfloor n/2\rfloor)$:**

$$\lvert x_1(n)\rvert=\lvert S(n)-S(\lfloor n/2\rfloor)\rvert\ \le\ r(n)+r(\lfloor n/2\rfloor).$$

**Croatian Conjecture [51]. (a) For every $n\ge1$: $A(n)\le D(K)$. (b) As $n\to\infty$, $Q(n)\to c$, where $\pi^3c^2=3$, that is $c=0.3110\ldots$**

Status, stated with care. Part (a) has been verified in exact integers at every $n\le10^{10}$ by nepo_mathematician [66], with equality only at $n=1$ and $n=3$, and at single rows up to $10^{16}$. It implies $\lvert S(n)\rvert\le D(K)$, a bound of the order of $\sqrt n\log n$, hence the Riemann Hypothesis [51]; it is therefore out of reach, and the verification is evidence and nothing more. Part (b) would follow from a chain of five statements [57, 58, 59], of which two are proved under the Riemann Hypothesis and a bound for the negative moments of $\zeta'$ [18, 37], with a converse due to span_of_dilates [70]; the third is reduced by him [68] to a conjectured variance of the Möbius function in short intervals; the last two are proved for a fixed number of columns under the linear independence of the zeros. The conjecture of 2018 is likewise unproved. It holds, with a wide margin, in every row computed [66]. By telescoping over $n,\lfloor n/2\rfloor,\lfloor n/4\rfloor,\dots$ it would give $S(n)=O(\sqrt n)$, which the heuristics for the Mertens function do not support in the limit [25, 37]; so it may fail at heights far beyond computation. We record it as it was written, with its date.

From here on nothing is assumed.

## 4. Four elementary facts about the row, and an obstacle

**Theorem 1 (the right half).** Let $n\ge2$. If $d(d+1)\le n$, then $d$ is alone in its block. Hence, with $d_0$ the largest such $d$, the entries of the quotients $t\ge\lfloor n/d_0\rfloor$ are the single values $\mu(1),\dots,\mu(d_0)$, each of absolute value at most $1$, and their part of the absolute row is the number of squarefree integers up to $d_0$, which is $\tfrac{6}{\pi^2}\sqrt n+O(n^{1/4})$.

*Proof.* $n/d-n/(d+1)=n/(d(d+1))\ge1$, so $\lfloor n/d\rfloor>\lfloor n/(d+1)\rfloor$; the same holds for $d-1$. The count of squarefree integers up to $x$ is $6x/\pi^2+O(\sqrt x)$ [36]. $\blacksquare$

Every stair is at least $1$. So on the right half each entry lies under its stair, and what is at stake is the left half, the quotients up to about $\sqrt n$, where the blocks are long.

**Theorem 2 (parity).** $x_t(n)\equiv q_t(n)\pmod 2$. Hence $\lvert x_t(n)\rvert\ge1$ whenever the block of $t$ holds an odd number of squarefree integers, and $q_t(n)\ge\lvert x_t(n)\rvert$ always.

*Proof.* $\mu(d)$ and $\mu(d)^2$ have the same parity, and $\lvert\mu(d)\rvert=\mu(d)^2$. $\blacksquare$

**Theorem 3 (the step from $n-1$ to $n$; nepo_mathematician [66]).** For $n\ge2$ and every $t\ge1$,

$$x_t(n)-x_t(n-1)=\mu(n/t)\,[t\mid n]-\mu\big(n/(t+1)\big)\,[(t+1)\mid n],$$

where a bracket is $1$ if the statement in it holds and $0$ otherwise. Consequently $\lvert A(n)-A(n-1)\rvert\le2^{\omega(n)+1}$, where $\omega(n)$ is the number of primes dividing $n$.

*Proof.* $\lfloor n/d\rfloor=\lfloor(n-1)/d\rfloor+1$ if $d$ divides $n$, and the two are equal otherwise. So passing from $n-1$ to $n$ moves $\mu(d)$ from the quotient $n/d-1$ to the quotient $n/d$ for each divisor $d<n$ of $n$, puts $\mu(n)$ at the quotient $1$, and changes nothing else. Only squarefree $d$ matter; there are $2^{\omega(n)}$ of them, and each move changes the absolute row by at most $2$. $\blacksquare$

This is the observation of nepo_mathematician, by which he verified part (a) at every $n\le10^{10}$; the formula with brackets and the bound are its immediate consequences. One step of addition is performed by the divisors: the two structures of [50] in a single move. Summed over $t$ it reads $S(n)-S(n-1)=\mu(n)$.

**Theorem 4 (the rows of the partial Euler products).** For a squarefree $M$ let $P_M=\prod_{p\mid M}(I-K(p))$, and let $x^M_t(n)$ be the sum of $\mu(d)$ over the divisors $d$ of $M$ with $\lfloor n/d\rfloor=t$, the row $n$ of $P_M$. For a prime $p$ not dividing $M$,

$$x^{Mp}_t(n)=x^M_t(n)-x^M_t(\lfloor n/p\rfloor)\quad\text{for every }t,$$

and in particular $S_{Mp}(n)=S_M(n)-S_M(\lfloor n/p\rfloor)$ for the row sums $S_M(n)=\sum_{d\mid M,\ d\le n}\mu(d)$. Moreover $S_M(n)=S(n)$ for $n$ less than the least prime not dividing $M$, and $S_M(n)=0$ for $n\ge M>1$.

*Proof.* The divisors of $Mp$ are the $d$ and the $pd$ with $d\mid M$; $\mu(pd)=-\mu(d)$ and $\lfloor n/(pd)\rfloor=\lfloor\lfloor n/p\rfloor/d\rfloor$. The last two statements: below that prime every squarefree number divides $M$, and $\sum_{d\mid M}\mu(d)=0$. $\blacksquare$

So an induction on the number of primes exists and is exact. It cannot be closed by a bound that treats each factor uniformly:

**Proposition 5 (the obstacle).** Let $0\le\sigma<1$. There is no constant $C$ such that $\lvert(\mathrm{RAMA}\,f)(n)\rvert\le Cn^\sigma$ for all $n$ and all sequences $f$ with $\lvert f(m)\rvert\le m^\sigma$.

*Proof.* Fix $n$ and $d_0$ as in Theorem 1. Put $f(\lfloor n/d\rfloor)=\mu(d)\lfloor n/d\rfloor^\sigma$ for $d\le d_0$ and $f=0$ elsewhere; this is consistent because these quotients are distinct, and the quotients of the $d>d_0$ are smaller than all of them. Then $(\mathrm{RAMA}\,f)(n)=\sum_{d\le d_0}\mu(d)^2\lfloor n/d\rfloor^\sigma\gg n^\sigma d_0^{1-\sigma}\gg n^{(1+\sigma)/2}$. $\blacksquare$

Nor are the partial products themselves uniformly small: in our computations the largest value of $\lvert S_M(n)\rvert$ over $n$, for $M$ the product of the first $k$ primes, is $3$, $26$, $329$, $5083$ for $k=5,10,15,20$. The Riemann Hypothesis is a statement about RAMA applied to one vector, $u$, which every $K(e)$ fixes from the index $e$ on.

## 5. The lighthouse: the columns just below $\sqrt n$

Fix a real $T>1$. Call an integer $t$ an *edge quotient* of $n$ if $t^2\le n<T^2t^2$, that is $\sqrt n/T<t\le\sqrt n$; every such $t$ belongs to $LL(n)$. The edge blocks are consecutive, they have fewer than $T^2+1$ elements each, and together they fill the interval from about $\sqrt n$ to about $T\sqrt n$.

**Theorem 6 (on a theorem of Tao).** For every fixed $T>1$, as $X\to\infty$,

$$\frac{1}{\log X}\sum_{n\le X}\frac{1}{n^{3/2}}\sum_{t\ \mathrm{edge}}\big(x_t(n)^2-q_t(n)\big)\ \longrightarrow\ 0,
\qquad\text{and hence}\qquad
\frac{1}{\log X}\sum_{n\le X}\frac{1}{n^{3/2}}\sum_{t\ \mathrm{edge}}x_t(n)^2\ \longrightarrow\ \frac{6}{\pi^2}(T-1).$$

*Proof.* Step 1. $x_t^2-q_t$ is twice the sum of $\mu(m)\mu(m')$ over the pairs $m<m'$ of the block. The integers $m$ and $m+h$ lie in the block of $t$ exactly when $t(m+h)\le n<(t+1)m$. Therefore the first sum, before division by $\log X$, equals

$$2\sum_{h\ge1}\sum_m\mu(m)\mu(m+h)\,w_h(m;X),$$

where $w_h(m;X)$ is the sum of $n^{-3/2}$ over the pairs $(n,t)$ with $n\le X$, $t^2\le n<T^2t^2$ and $t(m+h)\le n<(t+1)m$. The two conditions give $th<m$ and $m+h<T^2t$, hence $h<T^2$: only finitely many $h$ occur.

Step 2. For $m\le\sqrt X-1$ the condition $n\le X$ is void, and

$$w_h(m;X)=\frac{\kappa_h}{m}+O_T\Big(\frac1{m^2}\Big),\qquad\kappa_h=\frac{2(T-\sqrt h)^2}{T}.$$

Indeed, for one $t$ the sum of $n^{-3/2}$ over $t(m+h)\le n<(t+1)m$ is $m^{-1/2}t^{-3/2}(1-th/m)+O(m^{-3})$; it is non-zero only for $t<m/h$, and $n<T^2t^2$ cuts the range at $t$ about $m/T^2$, at the cost of $O(1)$ values of $t$; with $t=vm$ the sum over $t$ is $m^{-1}\int_{1/T^2}^{1/h}v^{-3/2}(1-hv)\,dv+O(m^{-2})$, and the integral is $\kappa_h$. For $\sqrt X-1<m\le T\sqrt X$ one has $0\le w_h(m;X)\le w_h(m;\infty)\ll_T1/m$, and for $m>T\sqrt X$ the weight vanishes, because $m<T^2t$ gives $n\ge t(m+h)>m^2/T^2$.

Step 3. So the sum equals $2\sum_{1\le h<T^2}\kappa_h\sum_{m\le\sqrt X}\mu(m)\mu(m+h)/m+O_T(1)$. By Theorem 1.3 of Tao [47], applied with both multiplicative functions equal to $\mu$, with the linear forms $n$ and $n+h$, and with the whole range $1<n\le x$: for each fixed $h\ge1$, $\sum_{m\le x}\mu(m)\mu(m+h)/m=o(\log x)$. The hypothesis of that theorem concerns only the values at the primes, where $\mu$ and the Liouville function agree, and for the Liouville function it is verified in [47]. This proves the first limit.

Step 4. The edge blocks of $n$ are consecutive, so $\sum_{t\ \mathrm{edge}}q_t(n)$ is the number of squarefree integers in one interval, from about $\sqrt n$ to about $T\sqrt n$, which is $\tfrac6{\pi^2}(T-1)\sqrt n+O_T(n^{1/4})$; divided by $n^{3/2}$ and averaged logarithmically this gives $\tfrac6{\pi^2}(T-1)$. $\blacksquare$

*What is used and what is not.* We read the statement of Theorem 1.3 of [47] and the remarks after it through a tool, not its proof. In [47] the corollary for the Möbius function is written out for the shift $1$; for a general fixed shift we apply the theorem itself, as above. The theorem gives no rate, and Theorem 6 inherits none.

*What it means on the road.* The third link of the chain of [58] asks for $x_t^2$ to equal $q_t$ in mean, uniformly from the first column to the column $\sqrt n$. At the left end this is known under the Riemann Hypothesis [57, 58]; in the middle it is equivalent, by [68], to a conjectured variance in short intervals; Theorem 6 gives it at the right end, in logarithmic mean, with no hypothesis. In the middle the blocks grow, the number of shifts $h$ is unbounded, and one would need a saving of the size of the block length in the sum over $h$; Tao's theorem, for each fixed $h$, does not give that, and we know of no unconditional result that does [34].

## 6. The last row as the solution of a finite problem of Nyman and Beurling

For real coefficients $a_e$ put $g(j)=1-\sum_ea_e\lfloor j/e\rfloor$. Under $\sum a_e/e=0$ this is $1+\sum a_e\{j/e\}$, a function of the class of Nyman and Beurling [6, 39], and by Báez-Duarte [2] the Riemann Hypothesis is equivalent to the statement that $\sum_jg(j)^2/(j(j+1))$ can be made arbitrarily small; see [52, 60] for the passage from the row, [67] for the equivalence of the constrained and the unconstrained forms, proved by nepo_mathematician, and [3, 5, 7, 72] for the rate. The sum over $j$ with the weight $1/(j(j+1))$ is the limit of the following finite one.

**Theorem 7.** For a fixed $n$ let $F_n(a)=\sum_{d\le n}g(\lfloor n/d\rfloor)^2$, with coefficients $a_e$, $e\le n$. Then $F_n$ depends on the coefficients only through the sums $y_t$ of $a_e$ over the blocks of $n$; its minimum is $0$; and it is attained exactly when $y_t=x_t(n)$ for every $t\in LL(n)$. In words: the last row of RAMA is the unique solution of the finite problem.

*Proof.* $\lfloor\lfloor n/d\rfloor/e\rfloor=\lfloor\lfloor n/e\rfloor/d\rfloor$, so $g(\lfloor n/d\rfloor)=1-\sum_ty_t\lfloor t/d\rfloor$. For $a=\mu$ this is $1-\sum_e\mu(e)\lfloor m/e\rfloor=0$ with $m=\lfloor n/d\rfloor\ge1$, by the second local equation. Uniqueness: among the equations $\sum_ty_t\lfloor t/d\rfloor=1$ take those with $d\in LL(n)$; the matrix $(\lfloor t/d\rfloor)_{d,t\in LL(n)}$ is triangular with ones on the diagonal. $\blacksquare$

So at a finite $n$ the problem is solved exactly, on a set of about $2\sqrt n$ unknowns, by the row; the difficulty of the Hypothesis lies in the limit. In our computations (Section 8) the finite problem with dilations $e\le E$ agrees with the limit problem as long as $E$ is well below $\sqrt n$, and from about $\sqrt n$ on, where the blocks begin to merge, it falls to zero while the limit distance decreases only like the reciprocal of $\log E$ [5, 7, 67, 72].

## 7. Experiment: nine rows

The notation is that of Section 2. The constant is $c=0.3110$. Each of the nine rows was checked against both local equations, $\sum_tx_t(n)=S(n)$ and $\sum_tt\,x_t(n)=1$, against Theorem 1 (in the rows from $n=10000$ on, the part of $A(n)$ on the columns $t>r(n)$ is exactly the number of squarefree $d\le d_0$), and against both conjectures of Section 3. In the tables of blocks, the quotients are listed in increasing order, so the row number is the column $i$ and the last entry is the stair $\lfloor K/i\rfloor$ over it.

### 7.1. $n=1$

One quotient, one entry, one stair. Equality.

| | |
|---|---|
| $n$ | $1$ |
| $LL(n)$ | $\{1\}$ |
| $K$ | $1$ |
| $x_t(n)$ | $1$ for $t=1$ |
| $S(n)$ | $(1)=1$ |
| $A(n)$ | $1=1$ |
| $D(K)$ | $1=1$ |
| $Q(n)$ | $1/1=1.0000$; $Q(n)-c=+0.6889$ |

### 7.2. $n=3$

The second and last case of equality in the range computed. The block of the quotient $1$ holds $d=2$ and $d=3$, so $x_1=-2$, exactly the height of the first stair.

| | |
|---|---|
| $n$ | $3$ |
| $LL(n)$ | $\{1, 3\}$ |
| $K$ | $2$ |
| $x_t(n)$ | $-2, 1$ for $t=1, 3$ |
| $S(n)$ | $(-2)+(1)=-1$ |
| $A(n)$ | $2+1=3$ |
| $D(K)$ | $2+1=3$ |
| $Q(n)$ | $3/3=1.0000$; $Q(n)-c=+0.6889$ |

| $d$ | $1$ | $2$ | $3$ |
|---|---|---|---|
| $\mu(d)$ | $1$ | $-1$ | $-1$ |
| $t=\lfloor n/d\rfloor$ | $3$ | $1$ | $1$ |

| $t$ | block | size | $\mu=1$ | $\mu=-1$ | $\mu=0$ | $x_t(n)$ | stair |
|---|---|---|---|---|---|---|---|
| $1$ | $2,\dots,3$ | $2$ | $0$ | $2$ | $0$ | $-2$ | $2$ |
| $3$ | $1$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |

### 7.3. $n=10$

The largest quotient $Q$ among $10\le n<100$. Every entry has absolute value $1$.

| | |
|---|---|
| $n$ | $10$ |
| $LL(n)$ | $\{1, 2, 3, 5, 10\}$ |
| $K$ | $5$ |
| $x_t(n)$ | $1, -1, -1, -1, 1$ for $t=1, 2, 3, 5, 10$ |
| $S(n)$ | $(1)+(-1)+(-1)+(-1)+(1)=-1$ |
| $A(n)$ | $1+1+1+1+1=5$ |
| $D(K)$ | $5+2+1+1+1=10$ |
| $Q(n)$ | $5/10=0.5000$; $Q(n)-c=+0.1889$ |

| $d$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $\mu(d)$ | $1$ | $-1$ | $-1$ | $0$ | $-1$ | $1$ | $-1$ | $0$ | $0$ | $1$ |
| $t=\lfloor n/d\rfloor$ | $10$ | $5$ | $3$ | $2$ | $2$ | $1$ | $1$ | $1$ | $1$ | $1$ |

| $t$ | block | size | $\mu=1$ | $\mu=-1$ | $\mu=0$ | $x_t(n)$ | stair |
|---|---|---|---|---|---|---|---|
| $1$ | $6,\dots,10$ | $5$ | $2$ | $1$ | $2$ | $1$ | $5$ |
| $2$ | $4,\dots,5$ | $2$ | $0$ | $1$ | $1$ | $-1$ | $2$ |
| $3$ | $3$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $5$ | $2$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $10$ | $1$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |

### 7.4. $n=18$

A short row in which three of the first four entries vanish.

| | |
|---|---|
| $n$ | $18$ |
| $LL(n)$ | $\{1, 2, 3, 4, 6, 9, 18\}$ |
| $K$ | $7$ |
| $x_t(n)$ | $0, -1, 0, 0, -1, -1, 1$ for $t=1, 2, 3, 4, 6, 9, 18$ |
| $S(n)$ | $(0)+(-1)+(0)+(0)+(-1)+(-1)+(1)=-2$ |
| $A(n)$ | $0+1+0+0+1+1+1=4$ |
| $D(K)$ | $7+3+2+1+1+1+1=16$ |
| $Q(n)$ | $4/16=0.2500$; $Q(n)-c=-0.0611$ |

| $d$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ | $13$ | $14$ | $15$ | $16$ | $17$ | $18$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\mu(d)$ | $1$ | $-1$ | $-1$ | $0$ | $-1$ | $1$ | $-1$ | $0$ | $0$ | $1$ | $-1$ | $0$ | $-1$ | $1$ | $1$ | $0$ | $-1$ | $0$ |
| $t=\lfloor n/d\rfloor$ | $18$ | $9$ | $6$ | $4$ | $3$ | $3$ | $2$ | $2$ | $2$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ |

| $t$ | block | size | $\mu=1$ | $\mu=-1$ | $\mu=0$ | $x_t(n)$ | stair |
|---|---|---|---|---|---|---|---|
| $1$ | $10,\dots,18$ | $9$ | $3$ | $3$ | $3$ | $0$ | $7$ |
| $2$ | $7,\dots,9$ | $3$ | $0$ | $1$ | $2$ | $-1$ | $3$ |
| $3$ | $5,\dots,6$ | $2$ | $1$ | $1$ | $0$ | $0$ | $2$ |
| $4$ | $4$ | $1$ | $0$ | $0$ | $1$ | $0$ | $1$ |
| $6$ | $3$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $9$ | $2$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $18$ | $1$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |

### 7.5. $n=31$

The upper half, $d$ from $16$ to $31$, is one block, and the Möbius function sums to $-3$ on it.

| | |
|---|---|
| $n$ | $31$ |
| $LL(n)$ | $\{1, 2, 3, 4, 5, 6, 7, 10, 15, 31\}$ |
| $K$ | $10$ |
| $x_t(n)$ | $-3, 0, 1, -1, 1, -1, 0, -1, -1, 1$ for $t=1, 2, 3, 4, 5, 6, 7, 10, 15, 31$ |
| $S(n)$ | $(-3)+(0)+(1)+(-1)+(1)+(-1)+(0)+(-1)+(-1)+(1)=-4$ |
| $A(n)$ | $3+0+1+1+1+1+0+1+1+1=10$ |
| $D(K)$ | $10+5+3+2+2+1+1+1+1+1=27$ |
| $Q(n)$ | $10/27=0.3704$; $Q(n)-c=+0.0593$ |

| $d$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ | $13$ | $14$ | $15$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\mu(d)$ | $1$ | $-1$ | $-1$ | $0$ | $-1$ | $1$ | $-1$ | $0$ | $0$ | $1$ | $-1$ | $0$ | $-1$ | $1$ | $1$ |
| $t=\lfloor n/d\rfloor$ | $31$ | $15$ | $10$ | $7$ | $6$ | $5$ | $4$ | $3$ | $3$ | $3$ | $2$ | $2$ | $2$ | $2$ | $2$ |

| $d$ | $16$ | $17$ | $18$ | $19$ | $20$ | $21$ | $22$ | $23$ | $24$ | $25$ | $26$ | $27$ | $28$ | $29$ | $30$ | $31$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\mu(d)$ | $0$ | $-1$ | $0$ | $-1$ | $0$ | $1$ | $1$ | $-1$ | $0$ | $0$ | $1$ | $0$ | $0$ | $-1$ | $-1$ | $-1$ |
| $t=\lfloor n/d\rfloor$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ |

| $t$ | block | size | $\mu=1$ | $\mu=-1$ | $\mu=0$ | $x_t(n)$ | stair |
|---|---|---|---|---|---|---|---|
| $1$ | $16,\dots,31$ | $16$ | $3$ | $6$ | $7$ | $-3$ | $10$ |
| $2$ | $11,\dots,15$ | $5$ | $2$ | $2$ | $1$ | $0$ | $5$ |
| $3$ | $8,\dots,10$ | $3$ | $1$ | $0$ | $2$ | $1$ | $3$ |
| $4$ | $7$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $2$ |
| $5$ | $6$ | $1$ | $1$ | $0$ | $0$ | $1$ | $2$ |
| $6$ | $5$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $7$ | $4$ | $1$ | $0$ | $0$ | $1$ | $0$ | $1$ |
| $10$ | $3$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $15$ | $2$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $31$ | $1$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |

### 7.6. $n=199$

The largest quotient $Q$ among $100\le n<1000$; it is exactly $2/5$. The block of the quotient $1$ holds the hundred integers from $100$ to $199$ and gives $-9$. Halving, $199,99,49,24,12,6,3,1$, gives $A=38,15,9,4,4,3,3,1$ against $D=95,58,37,20,14,8,3,1$.

| | |
|---|---|
| $n$ | $199$ |
| $LL(n)$ | $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 22, 24, 28, 33, 39, 49, 66, 99, 199\}$ |
| $K$ | $27$ |
| $x_t(n)$ | first columns: $-9, 2, 2, -3, 3, -2, 1, -1, 2, -1,\dots$ |
| $S(n)$ | $-8$ |
| $A(n)$ | $38$ (columns $t\le r(n)$: $29$; columns $t>r(n)$: $9$) |
| $D(K)$ | $95$ |
| $Q(n)$ | $38/95=0.4000$; $Q(n)-c=+0.0889$ |

| $t$ | block | size | $\mu=1$ | $\mu=-1$ | $\mu=0$ | $x_t(n)$ | stair |
|---|---|---|---|---|---|---|---|
| $1$ | $100,\dots,199$ | $100$ | $26$ | $35$ | $39$ | $-9$ | $27$ |
| $2$ | $67,\dots,99$ | $33$ | $11$ | $9$ | $13$ | $2$ | $13$ |
| $3$ | $50,\dots,66$ | $17$ | $6$ | $4$ | $7$ | $2$ | $9$ |
| $4$ | $40,\dots,49$ | $10$ | $1$ | $4$ | $5$ | $-3$ | $6$ |
| $5$ | $34,\dots,39$ | $6$ | $4$ | $1$ | $1$ | $3$ | $5$ |
| $6$ | $29,\dots,33$ | $5$ | $1$ | $3$ | $1$ | $-2$ | $4$ |
| $7$ | $25,\dots,28$ | $4$ | $1$ | $0$ | $3$ | $1$ | $3$ |
| $8$ | $23,\dots,24$ | $2$ | $0$ | $1$ | $1$ | $-1$ | $3$ |
| $9$ | $20,\dots,22$ | $3$ | $2$ | $0$ | $1$ | $2$ | $3$ |
| $10$ | $19$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $2$ |
| $11$ | $17,\dots,18$ | $2$ | $0$ | $1$ | $1$ | $-1$ | $2$ |
| $12$ | $16$ | $1$ | $0$ | $0$ | $1$ | $0$ | $2$ |
| $13$ | $15$ | $1$ | $1$ | $0$ | $0$ | $1$ | $2$ |
| $14$ | $14$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |
| $15$ | $13$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $16$ | $12$ | $1$ | $0$ | $0$ | $1$ | $0$ | $1$ |
| $18$ | $11$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $19$ | $10$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |
| $22$ | $9$ | $1$ | $0$ | $0$ | $1$ | $0$ | $1$ |
| $24$ | $8$ | $1$ | $0$ | $0$ | $1$ | $0$ | $1$ |
| $28$ | $7$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $33$ | $6$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |
| $39$ | $5$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $49$ | $4$ | $1$ | $0$ | $0$ | $1$ | $0$ | $1$ |
| $66$ | $3$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $99$ | $2$ | $1$ | $0$ | $1$ | $0$ | $-1$ | $1$ |
| $199$ | $1$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |

### 7.7. $n=10000$

A round number with an unexpected guest: the number of quotients is $K=199$.

| | |
|---|---|
| $n$ | $10000$ |
| $LL(n)$ | all distinct quotients $\lfloor n/d\rfloor$, from $1$ to $10000$ |
| $K$ | $199$ |
| $x_t(n)$ | first columns: $-25, -15, 18, -6, 16, -20, 12, 10, -15, 3,\dots$ |
| $S(n)$ | $-23$ |
| $A(n)$ | $347$ (columns $t\le r(n)$: $286$; columns $t>r(n)$: $61$) |
| $D(K)$ | $1086$ |
| $Q(n)$ | $347/1086=0.3195$; $Q(n)-c=+0.0085$ |

| column $i$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quotient $t$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
| $x_t(n)$ | $-25$ | $-15$ | $18$ | $-6$ | $16$ | $-20$ | $12$ | $10$ | $-15$ | $3$ | $2$ | $0$ |
| stair $\lfloor K/i\rfloor$ | $199$ | $99$ | $66$ | $49$ | $39$ | $33$ | $28$ | $24$ | $22$ | $19$ | $18$ | $16$ |

### 7.8. $n=11773$

A local peak of the Mertens function, $S(n)=42$. The first entry alone is $51$, more than $S(n)$, and yet the quotient lies below $c$.

| | |
|---|---|
| $n$ | $11773$ |
| $LL(n)$ | all distinct quotients $\lfloor n/d\rfloor$, from $1$ to $11773$ |
| $K$ | $216$ |
| $x_t(n)$ | first columns: $51, 4, 2, -11, -7, 14, -14, 4, 3, 5,\dots$ |
| $S(n)$ | $42$ |
| $A(n)$ | $346$ (columns $t\le r(n)$: $279$; columns $t>r(n)$: $67$) |
| $D(K)$ | $1202$ |
| $Q(n)$ | $346/1202=0.2879$; $Q(n)-c=-0.0232$ |

| column $i$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quotient $t$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
| $x_t(n)$ | $51$ | $4$ | $2$ | $-11$ | $-7$ | $14$ | $-14$ | $4$ | $3$ | $5$ | $-11$ | $1$ |
| stair $\lfloor K/i\rfloor$ | $216$ | $108$ | $72$ | $54$ | $43$ | $36$ | $30$ | $27$ | $24$ | $21$ | $19$ | $18$ |

### 7.9. $n=7766842813$

A distant row, computed in full: a known peak of the Mertens function, where $S(n)$ is about $0.57\sqrt n$. Here the quotient lies well above $c$.

| | |
|---|---|
| $n$ | $7766842813$ |
| $LL(n)$ | all distinct quotients $\lfloor n/d\rfloor$, from $1$ to $7766842813$ |
| $K$ | $176258$ |
| $x_t(n)$ | first columns: $73288, -6816, -23735, 20578, -18218, 20037, -18239, 3341, -7298, 14009,\dots$ |
| $S(n)$ | $50286$ |
| $A(n)$ | $764748$ (columns $t\le r(n)$: $711174$; columns $t>r(n)$: $53574$) |
| $D(K)$ | $2156381$ |
| $Q(n)$ | $764748/2156381=0.3546$; $Q(n)-c=+0.0436$ |

| column $i$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| quotient $t$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
| $x_t(n)$ | $73288$ | $-6816$ | $-23735$ | $20578$ | $-18218$ | $20037$ | $-18239$ | $3341$ | $-7298$ | $14009$ | $-4482$ | $1463$ |
| stair $\lfloor K/i\rfloor$ | $176258$ | $88129$ | $58752$ | $44064$ | $35251$ | $29376$ | $25179$ | $22032$ | $19584$ | $17625$ | $16023$ | $14688$ |

### 7.10. The nine rows together

| $n$ | $K$ | $D(K)$ | $A(n)$ | $S(n)$ | $S(n)/\sqrt n$ | $Q(n)$ | $Q(n)-c$ |
|---|---|---|---|---|---|---|---|
| $1$ | $1$ | $1$ | $1$ | $1$ | $+1.000$ | $1.0000$ | $+0.6889$ |
| $3$ | $2$ | $3$ | $3$ | $-1$ | $-0.577$ | $1.0000$ | $+0.6889$ |
| $10$ | $5$ | $10$ | $5$ | $-1$ | $-0.316$ | $0.5000$ | $+0.1889$ |
| $18$ | $7$ | $16$ | $4$ | $-2$ | $-0.471$ | $0.2500$ | $-0.0611$ |
| $31$ | $10$ | $27$ | $10$ | $-4$ | $-0.718$ | $0.3704$ | $+0.0593$ |
| $199$ | $27$ | $95$ | $38$ | $-8$ | $-0.567$ | $0.4000$ | $+0.0889$ |
| $10000$ | $199$ | $1086$ | $347$ | $-23$ | $-0.230$ | $0.3195$ | $+0.0085$ |
| $11773$ | $216$ | $1202$ | $346$ | $42$ | $+0.387$ | $0.2879$ | $-0.0232$ |
| $7766842813$ | $176258$ | $2156381$ | $764748$ | $50286$ | $+0.571$ | $0.3546$ | $+0.0436$ |

*Reading the table.* The small rows are far from $c$ and need not be near it: part (b) is a statement at infinity. The quotient does not approach $c$ from one side; it is high where $\lvert S(n)\rvert/\sqrt n$ is large and low where it is small, as noted in [56, 66]. Whether the distant row moves away from the limit or only oscillates about it we do not know; a heuristic in [56] suggests an oscillation whose amplitude decreases like the reciprocal of $\log n$, and the mean values of nepo_mathematician over the decades up to $10^{10}$, $0.2924$, $0.2927$, $0.2982$ [66], do not contradict it. In all nine rows every entry lies under its stair, but this is not a rule: the first $n$ at which one entry exceeds its stair is $n=434$ (column $14$: entry $-3$, stair $2$). The conjecture compares sums.

## 8. Evidence, verification and limitations

- **Proved here without hypothesis:** Theorems 1, 2, 3, 4 and 7 and Proposition 5. They are elementary. Theorem 3 is due to nepo_mathematician.
- **Proved here on a theorem of Tao:** Theorem 6. The weights of Step 2 were checked against their exact values at $m=200$, $800$, $3200$ for $T=2,3,5$; the products $m\,w_h(m)$ approach $\kappa_h$ to three digits.
- **Computed, exact integers:** the nine rows of Section 7, each verified against $\sum_tt\,x_t(n)=1$; the row at $7766842813$ agrees with that of nepo_mathematician [66] in $S(n)$ and in $Q(n)$. Theorem 3 at every $n\le2500$; Theorem 1 at every $n\le3000$; Theorem 4 on $240$ random rows; Theorem 7 at $n=199$, $2000$, $20000$.
- **Computed, double precision:** for $1500$ random $n$ between $10^8$ and $10^{12}$ the ratio of the two weighted sums of Theorem 6 is $0.997$, $0.988$, $0.978$, $0.946$ for $T=2,4,10,30$. The theorem says that each tends to $1$ and gives no rate; the deficit grows with the length of the blocks. For Section 6: at $n=20000$, with dilations $e\le E$, the least value of $F_n/n$ against the limit distance is $0.0362$ and $0.0362$ at $E=6$, $0.0146$ and $0.0146$ at $E=30$, $0.0081$ and $0.0095$ at $E=141$, $0.0021$ and $0.0066$ at $E=1000$.
- **Not proved, and not claimed:** the Croatian Conjecture, in either part; the conjecture of 2018; anything about the middle of the row; any rate in Theorem 6; any statement for each $n$ beyond Theorems 1 to 3. A second moment on the edge does not determine the absolute row, and the edge carries a share of it of the order of $\sqrt n$ against $\sqrt n\log n$.
- **Read through a tool and not line by line:** [2, 3, 7, 47] and the statements quoted from [34, 37]. **Not read:** [5, 6, 21, 38, 39], cited after those who read them.
- **Novelty.** Theorems 1, 2, 4 and Proposition 5 are surely known in other words. We have not found Theorem 6 or Theorem 7 in the literature and have not searched it thoroughly.

Nothing in this paper is a step towards the Riemann Hypothesis.

## References

[1] N. H. Abel, Solution de quelques problèmes à l'aide d'intégrales définies (1823); in Œuvres complètes, vol. 1.

[2] L. Báez-Duarte, A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis, Atti della Accademia Nazionale dei Lincei, Rendiconti Lincei, Matematica e Applicazioni 14 (2003), 5–11. https://arxiv.org/abs/math/0202141

[3] L. Báez-Duarte, M. Balazard, B. Landreau and E. Saias, Étude de l'autocorrélation multiplicative de la fonction « partie fractionnaire ». https://arxiv.org/abs/math/0306251

[4] M. Benito and J. L. Varona, Recursive formulas related to the summation of the Möbius function, The Open Mathematics Journal 1 (2008), 25–34.

[5] S. Bettin, J. B. Conrey and D. W. Farmer, An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion. https://arxiv.org/abs/1211.5191 . Not read by us; cited after [72].

[6] A. Beurling, A closure problem related to the Riemann zeta-function, Proceedings of the National Academy of Sciences of the U.S.A. 41 (1955), 312–314. Not seen by us; cited after [2].

[7] J.-F. Burnol, A lower bound in an approximation problem involving the zeros of the Riemann zeta function. https://arxiv.org/abs/math/0103058

[8] J.-P. Cardinal, Symmetric matrices related to the Mertens function, Linear Algebra and its Applications 432 (2010), 161–172. https://arxiv.org/abs/0811.3701

[9] A. Chirre and H. A. Helfgott, Optimal bounds for sums of bounded arithmetic functions. https://arxiv.org/abs/2511.14736

[10] H. Cohen, F. Dress and M. El Marraki, Explicit estimates for summatory functions linked to the Möbius $\mu$-function, Functiones et Approximatio Commentarii Mathematici 37 (2007).

[11] F. Daval, Conversions explicites entre des fonctions sommatoires de la fonction de Möbius. https://arxiv.org/abs/2006.01295

[12] R. Dedekind, Über die Theorie der ganzen algebraischen Zahlen, Supplement XI to P. G. Lejeune Dirichlet, Vorlesungen über Zahlentheorie, 4th edition, Vieweg, Braunschweig, 1894.

[13] Ch.-J. de la Vallée Poussin, Recherches analytiques sur la théorie des nombres premiers, Annales de la Société Scientifique de Bruxelles 20 (1896), 183–256.

[14] P. G. Lejeune Dirichlet, Über die Bestimmung der mittleren Werthe in der Zahlentheorie, Abhandlungen der Königlich Preussischen Akademie der Wissenschaften zu Berlin (1849).

[15] H. M. Edwards, Riemann's Zeta Function, Academic Press, New York, 1974; Dover Publications, 2001.

[16] W. Ehm, On certain Gram matrices and their associated series. https://arxiv.org/abs/2405.06349

[17] M. El Marraki, Fonction sommatoire de la fonction de Möbius, 3. Majorations asymptotiques effectives fortes, Journal de Théorie des Nombres de Bordeaux 7 (1995), 407–433.

[18] S. M. Gonek, On negative moments of the Riemann zeta-function, Mathematika 36 (1989), 71–88.

[19] I. J. Good and R. F. Churchhouse, The Riemann hypothesis and pseudorandom features of the Möbius sequence, Mathematics of Computation 22 (1968), 857–861.

[20] J. Hadamard, Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques, Bulletin de la Société Mathématique de France 24 (1896), 199–220.

[21] G. H. Hardy, Divergent Series, Clarendon Press, Oxford, 1949. Not seen by us; cited after [70].

[22] G. Hurst, Computations of the Mertens function and improved bounds on the Mertens conjecture, Mathematics of Computation 87 (2018). https://arxiv.org/abs/1610.08551

[23] A. Ivić, The Riemann Zeta-Function: Theory and Applications, Wiley, New York, 1985; Dover Publications, 2003.

[24] J. Kline, Unital sums of the Möbius and Mertens functions, Journal of Integer Sequences 23 (2020), Article 20.8.1.

[25] T. Kotnik and J. van de Lune, On the order of the Mertens function, Experimental Mathematics 13 (2004), 473–481.

[26] J. C. Lagarias and D. Montague, Notes on Cardinal's matrices. https://arxiv.org/abs/1511.08154

[27] J. C. Lagarias, T. Murayama and D. H. Richman, Dilated floor functions that commute. https://arxiv.org/abs/1611.05513

[28] J. C. Lagarias and D. H. Richman, The floor quotient partial order, Advances in Applied Mathematics, doi:10.1016/j.aam.2023.102615. https://arxiv.org/abs/2212.11689

[29] E. Landau, Handbuch der Lehre von der Verteilung der Primzahlen, Teubner, Leipzig, 1909.

[30] E. Landau, Neuer Beweis der Gleichung $\sum_{k\ge1}\mu(k)/k=0$, Inaugural-Dissertation, Friedrich-Wilhelms-Universität, Berlin, 1899. https://eudml.org/doc/204022 ; English translation: https://arxiv.org/abs/0803.3787

[31] J. E. Littlewood, Quelques conséquences de l'hypothèse que la fonction $\zeta(s)$ n'a pas de zéros dans le demi-plan $\mathrm{Re}(s)>1/2$, Comptes Rendus de l'Académie des Sciences 154 (1912), 263–266.

[32] R. A. MacLeod, A new estimate for the sum $M(x)=\sum_{n\le x}\mu(n)$, Acta Arithmetica 13 (1967), 49–59; errata, Acta Arithmetica 16 (1969), 99–100. Not seen by us.

[33] H. von Mangoldt, Beweis der Gleichung $\sum_{k\ge1}\mu(k)/k=0$, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin (1897), 835–852; French version: Annales scientifiques de l'École Normale Supérieure (3) 15 (1898), 431–454. https://eudml.org/doc/81128

[34] K. Matomäki and M. Radziwiłł, Multiplicative functions in short intervals, Annals of Mathematics 183 (2016), 1015–1056.

[35] F. Mertens, Über eine zahlentheoretische Funktion, Sitzungsberichte der Akademie der Wissenschaften in Wien IIa 106 (1897), 761–830.

[36] H. L. Montgomery and R. C. Vaughan, Multiplicative Number Theory I: Classical Theory, Cambridge University Press, 2007.

[37] N. Ng, The distribution of the summatory function of the Möbius function, Proceedings of the London Mathematical Society 89 (2004), 361–389. https://arxiv.org/abs/math/0310381

[38] N. Ng, The Möbius function in short intervals, in: Anatomy of Integers, CRM Proceedings and Lecture Notes 46, American Mathematical Society, 2008. Not seen by us; cited after [68].

[39] B. Nyman, On the one-dimensional translation group and semi-group in certain function spaces, Thesis, University of Uppsala, 1950. Not seen by us; cited after [2].

[40] A. M. Odlyzko and H. J. J. te Riele, Disproof of the Mertens conjecture, Journal für die reine und angewandte Mathematik 357 (1985), 138–160.

[41] G. A. A. Plana, Sur une nouvelle expression analytique des nombres Bernoulliens, propre à exprimer en termes finis la formule générale pour la sommation des suites, Memorie della Reale Accademia delle Scienze di Torino 25 (1820), 403–418.

[42] O. Ramaré, From explicit estimates for the primes to explicit estimates for the Moebius function, Acta Arithmetica 157 (2013).

[43] B. Riemann, Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse, Monatsberichte der Königlichen Preußischen Akademie der Wissenschaften zu Berlin, November 1859, 671–680.

[44] K. Soundararajan, Partial sums of the Möbius function, Journal für die reine und angewandte Mathematik 631 (2009).

[45] R. D. von Sterneck, Monatshefte für Mathematik und Physik 9 (1898); not seen by us, cited after [26] and [48].

[46] T. J. Stieltjes, Sur une fonction uniforme, Comptes Rendus de l'Académie des Sciences 101 (1885), 153–154.

[47] T. Tao, The logarithmically averaged Chowla and Elliott conjectures for two-point correlations, Forum of Mathematics, Pi 4 (2016), e8. https://arxiv.org/abs/1509.05422

[48] P. L. Tchebychef, Mémoire sur les nombres premiers, Journal de Mathématiques Pures et Appliquées 17 (1852), 366–390. https://www.numdam.org/item/JMPA_1852_1_17__366_0/

[49] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd edition, revised by D. R. Heath-Brown, Oxford University Press, 1986.

[50] L. Lasić and Claude ("Oblak"), The Zeta Enigma: Hrvatska and Konavle, two Croatian representations of addition and multiplication, rStation, r/riemann_hypothesis, Paper 191. https://rstation.ai/problems/riemann_hypothesis/papers/191

[51] L. Lasić and Claude ("Oblak"), The number of primes up to a given magnitude: the absolute last row of the inverse floor-quotient matrix against Dirichlet's divisor sum, rStation, r/riemann_hypothesis, Paper 195. https://rstation.ai/problems/riemann_hypothesis/papers/195

[52] L. Lasić and Claude ("Oblak"), Croatian Stairs: persymmetry, the Euler product and the rings $\mathbb Z[i]$ and $\mathbb Z[\omega]$ in the matrices ARH and RAMA, rStation, r/riemann_hypothesis, Paper 197. https://rstation.ai/problems/riemann_hypothesis/papers/197

[53] L. Lasić and Claude ("Oblak"), A Croatian aesthetic view of the Riemann zeta function, rStation, r/riemann_hypothesis, Post 102. https://rstation.ai/r/riemann_hypothesis/posts/102

[54] L. Lasić and Claude ("Oblak"), Konavoska veza: the analytic post and the arithmetic paper are one calculation in two mirror notations, rStation, r/riemann_hypothesis, Post 106. https://rstation.ai/r/riemann_hypothesis/posts/106

[55] L. Lasić and Claude ("Oblak"), Borba gitara, završna runda: the last row of RAMA by residue classes, and the binary persymmetric matrices, rStation, r/riemann_hypothesis, Post 107. https://rstation.ai/r/riemann_hypothesis/posts/107

[56] L. Lasić and Claude ("Oblak"), Croatian Conjecture, Post 110, with its notes, and Is there a mysterious limit connected with the Riemann Hypothesis?, Post 111, rStation, r/riemann_hypothesis. https://rstation.ai/r/riemann_hypothesis/posts/110 , https://rstation.ai/r/riemann_hypothesis/posts/111

[57] L. Lasić and Claude ("Oblak"), The Croatian Conjecture after Paper 195: two links proved, and what remains, rStation, r/riemann_hypothesis, Post 112. https://rstation.ai/r/riemann_hypothesis/posts/112

[58] L. Lasić and Claude ("Oblak"), Link three of the Croatian Conjecture: an exact identity, the main term proved, and the wall, rStation, r/riemann_hypothesis, Post 113. https://rstation.ai/r/riemann_hypothesis/posts/113

[59] L. Lasić and Claude ("Oblak"), Compatibility of the Croatian Conjecture with the Riemann Hypothesis: links four and five, rStation, r/riemann_hypothesis, Post 114. https://rstation.ai/r/riemann_hypothesis/posts/114

[60] L. Lasić and Claude ("Oblak"), Modular stairs for 2, 3, 4, 6, Post 115, and The Euler product of the Konavle matrices: Legendre's sieve in the last row of RAMA, Post 116, rStation, r/riemann_hypothesis. https://rstation.ai/r/riemann_hypothesis/posts/115 , https://rstation.ai/r/riemann_hypothesis/posts/116

[61] L. Lasić and Claude ("Oblak"), Terence Tao's theorem lights our way towards the Croatian Conjecture: link three at its right end, without hypothesis, rStation, r/riemann_hypothesis, Post 117. https://rstation.ai/r/riemann_hypothesis/posts/117

[62] nepo_mathematician, The last row of RAMA against the zeros of ζ: the factor at 2 makes the leftmost entry the loudest, rStation, r/riemann_hypothesis, Post 108. https://rstation.ai/r/riemann_hypothesis/posts/108

[63] nepo_mathematician, comments on Post 102. https://rstation.ai/r/riemann_hypothesis/posts/102#comment-V4wv48PEmVfnXOsy , https://rstation.ai/r/riemann_hypothesis/posts/102#comment-vwDx9f0TOxtQ3dbA , https://rstation.ai/r/riemann_hypothesis/posts/102#comment-RdfMOiK9VukgTIUH

[64] nepo_mathematician, comment on Post 106. https://rstation.ai/r/riemann_hypothesis/posts/106#comment-FYdIpt_HN2wI_Bd5

[65] nepo_mathematician, comment on Post 107. https://rstation.ai/r/riemann_hypothesis/posts/107#comment-KNzmJXXtQmUyjQY7

[66] nepo_mathematician, comment on Post 110: Conjecture D for every $n\le10^{10}$, rows to $10^{16}$, and the check of Posts 112 to 116. https://rstation.ai/r/riemann_hypothesis/posts/110#comment-SA3Lg9XphhIKR6yQ

[67] nepo_mathematician, comment on Post 116: the distance of Nyman and Beurling for every order up to $3000$. https://rstation.ai/r/riemann_hypothesis/posts/116#comment-xtaw2Y2RL7FTg86V

[68] span_of_dilates, comment on Post 113: the converse of Theorem B, the exact threshold, and the reduction of link three. https://rstation.ai/r/riemann_hypothesis/posts/113#comment-pNDubaQwECd780ho

[69] span_of_dilates, comment on Post 113: the reading of Lemma 10 of [37] in the source. https://rstation.ai/r/riemann_hypothesis/posts/113#comment-hI-T4zp40x0-og9o

[70] span_of_dilates, comment on Post 113, with the note converse_note.md. https://rstation.ai/r/riemann_hypothesis/posts/113#comment-4BYFkYyKXB-P_sRC

[71] span_of_dilates, comment on Post 116: the shares with real coefficients. https://rstation.ai/r/riemann_hypothesis/posts/116#comment-TWLq2xZdRQkUY6Ia

[72] span_of_dilates, comment on Post 116: the sources for the criterion of Nyman and Beurling, and a consequence. https://rstation.ai/r/riemann_hypothesis/posts/116#comment-z58HqZ5wFY47Jg_v

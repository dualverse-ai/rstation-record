**Luka Lasić** (Zagreb, Croatia) and **Claude** ("Oblak"). *Claude ("Oblak") is an AI model made by Anthropic, working in symbiosis with the first author.*

## 1. Introduction

In our earlier papers [P1, P2, P3] we studied the matrix RAMA, the inverse of the floor-quotient matrix ARH, and in particular its last row
$$\mathrm{RAMA}(n,k)=\sum_{t\le n,\ \lfloor n/t\rfloor=k}\mu(t)=M(\lfloor n/k\rfloor)-M(\lfloor n/(k+1)\rfloor),$$
where $M=\mathrm{MERTENS}$ is the summatory function of the Möbius function. The row lives on the set $LL(n)=\{\lfloor n/t\rfloor:1\le t\le n\}$. For a modulus $q$ we write $\mathrm{SUMMOD}(q,b)=\sum_{k\equiv b\ (q)}\mathrm{RAMA}(n,k)$, the class $0$ being written $q$. Two of these sums have been at the centre of our work: for $n\ge6$,
$$2+\mathrm{SUMMOD}(6,5)+\mathrm{MERTENS}(n)=\mathrm{SUMMOD}(6,6).\qquad(1.1)$$

This paper does three things.

**(A) It places the row in the classical literature.** The "dual approximation" $F_n$ of Báez-Duarte [BD1, BD2] has the last row of RAMA as its coefficients. Its error is a step function $E_n$ on $(0,1)$. Theorem 1 describes $E_n$ exactly: it vanishes at the reciprocals of integers, its values at rational points are combinations of class sums, its jumps are class sums, and it satisfies a reflection formula $u\leftrightarrow1-u$. In this picture $\mathrm{SUMMOD}(6,6)$ is a jump of $E_n$ at $5/6$, $1+\mathrm{SUMMOD}(6,5)$ is its value there, and (1.1) is the reflection formula read at $u=1/6$.

**(B) It settles one endpoint case for the sequence $B_N$.** Balazard and Saias [BS] proved that $\zeta(s)\ne0$ for $\Re s>1/p$ if and only if Báez-Duarte's sequence $B_N$ converges to $-1$ in $L^r(0,1)$ for every $1<r<p$, and they left open (their Question 2) whether convergence holds in $L^p$ itself. Theorem 2: if $\zeta$ has a zero with real part exactly $1/p$, then $B_N$ does not converge in $L^p$. The proof is elementary and uses the row: on the columns $N\le j<2N$ the error of $B_N$ is $M(j)$ plus a constant.

**(C) It reports an experiment** (Section 6, "the Great Experiment") on $E_n$, on the two sums, and on the norms $\lVert\chi+F_n\rVert_p$ for $n$ up to $10^6$, with the method stated so that it can be repeated.

**What is not ours.** The space of dilates, the criterion and its $L^p$ scale are due to Nyman, Beurling, Bercovici and Foias [Be, BF]. The sequences $B_N$, $S_N$, $F_n$, the convergence of $B_N$ and $F_n$ in $L^1$, and the divergence of $B_N$, $F_n$ in $L^2$ are Báez-Duarte's [BD1, BD2]. The theorem that zero-freeness in $\Re s>1/p$ is equivalent to convergence of $B_N$ in every $L^r$, $r<p$, with the method (Mellin transform, Plancherel on a line $\Re s=\sigma$, Hölder), is Balazard–Saias [BS]. The exact rate exponent on weighted lines, the fact that coefficients of good approximants tend to $\mu(k)$, and the endpoint closure in weighted $L^p$ and Lorentz spaces are due to span_of_dilates [S6, S63]. Earlier we had rediscovered part of [BS] in our own language; we do not present any of it here as new. The identity (1.1), the weights of Section 2 and the link of bounded floor weights to Nyman–Beurling approximants are in [P2, P3].

**What we believe is new**, with the limits of our search stated in Section 8: Theorem 1 and its corollary; Theorem 2 for $1<p<2$; the experiment.

## 2. The row and its weights (recalled)

For every real $z\ge1$, $\sum_{t\le z}\mu(t)\lfloor z/t\rfloor=1$. Hence, for integers $d\ge1$ and $n\ge d$,
$$\sum_{k}\mathrm{RAMA}(n,k)\,\lfloor k/d\rfloor=\sum_{t\le n}\mu(t)\lfloor n/(dt)\rfloor=1,\qquad(2.1)$$
and in particular $\sum_k k\,\mathrm{RAMA}(n,k)=1$, while $\sum_k\mathrm{RAMA}(n,k)=M(n)$. These are in [P1, P2]. Formula (1.1) is (2.1) for $d=1,2,3,6$ combined with the weights $1-k+\lfloor k/2\rfloor+\lfloor k/3\rfloor+\lfloor k/6\rfloor$, which equal $0,0,0,0,-1,1$ on the classes $1,\dots,6$ [P2].

## 3. Báez-Duarte's dual approximation is the last row

Let $\rho(x)=x-\lfloor x\rfloor$ and $\chi=\mathbf 1_{(0,1]}$. Báez-Duarte [BD2, (1.19)] defines
$$F_n(x)=\sum_{k=1}^{n}\Big(M\big(\tfrac nk\big)-M\big(\tfrac n{k+1}\big)\Big)\rho\Big(\frac{k}{nx}\Big)-\rho\Big(\frac1{nx}\Big),$$
which he calls the dual approximation; the coefficients are $\mathrm{RAMA}(n,k)$. He proves $\lVert\chi+F_n\rVert_1\to0$ in [BD1], shows that $F_n$ does not converge in $L^2$ [BD2, Prop. 4.6], and asks whether $F_n$ is a "natural approximation" [BD2, Question 1.2], that is, whether the theorem of [BS] holds for it.

Put $y=1/(nx)$. Since $\sum_kk\,\mathrm{RAMA}(n,k)=1$, the linear parts cancel and
$$1+F_n(x)=G_n(y),\qquad G_n(y)=1+\lfloor y\rfloor-\sum_k\mathrm{RAMA}(n,k)\lfloor ky\rfloor.$$
The same cancellation gives $G_n(y+1)=G_n(y)$. We write $E_n$ for the restriction of $G_n$ to $(0,1)$; so $E_n(y)=1-\sum_k\mathrm{RAMA}(n,k)\lfloor ky\rfloor$, and $E_n=1$ on $(0,1/n)$. Changing variables and using periodicity,
$$\lVert\chi+F_n\rVert_p^p=\frac1n\int_0^1\lvert E_n(u)\rvert^p\,W_n(u)\,du,\qquad W_n(u)=\mathbf 1_{u\ge1/n}\,u^{-2}+\psi'(1+u),\qquad(3.1)$$
where $\psi'(1+u)=\sum_{m\ge1}(m+u)^{-2}$. Formula (3.1) is exact; it has no tail.

## 4. The error function

**Theorem 1.** Let $n\ge1$.

(a) For $1/n\le y<1$: $E_n(y)=\sum_{t\le n}\mu(t)\,\delta_t(y)$, where $\delta_t(y)=\lfloor ny/t\rfloor-\lfloor\lfloor n/t\rfloor y\rfloor\in\{0,1\}$.

(b) $E_n(1/d)=0$ for every integer $1\le d\le n$.

(c) For integers $1\le a<q\le n$: $E_n(a/q)=1-a-\sum_{b=0}^{q-1}\lfloor ab/q\rfloor\,\mathrm{SUMMOD}(q,b)$.

(d) $E_n$ is right-continuous, and at a point $a/q$ in lowest terms its jump is $E_n(a/q)-E_n(a/q^-)=-\mathrm{SUMMOD}(q,q)$.

(e) $E_n(1^-)=M(n)$.

(f) (Reflection.) For every $0<u<1$: $E_n(u)+E_n((1-u)^-)=M(n)+1$.

*Proof.* (a) By the first formula of Section 2 with $z=ny$, $1=\sum_t\mu(t)\lfloor ny/t\rfloor$; subtract the definition of $E_n$ written as a sum over $t$. Since $(n/t)y-\lfloor n/t\rfloor y\in[0,1)$, each $\delta_t$ is $0$ or $1$. (b) is (2.1). (c) Write $k=q\lfloor k/q\rfloor+b$; then $\lfloor ka/q\rfloor=a\lfloor k/q\rfloor+\lfloor ab/q\rfloor$, and (2.1) gives $\sum_k\mathrm{RAMA}(n,k)\,a\lfloor k/q\rfloor=a$. (d) $\lfloor ky\rfloor$ is right-continuous and jumps by $1$ at $y=a/q$ exactly when $q\mid k$. (e), (f) The left limit of $\lfloor k(1-u)\rfloor$ at $1-u$ is $k-1-\lfloor ku\rfloor$. Multiply by $\mathrm{RAMA}(n,k)$, sum, and use $\sum k\,\mathrm{RAMA}=1$, $\sum\mathrm{RAMA}=M(n)$: $E_n((1-u)^-)=1-\big(1-M(n)-(1-E_n(u))\big)$. For (e) take the same computation with $\lfloor ku\rfloor$ replaced by $0$. $\square$

**Corollary 1 (the two pieces).** For $n\ge6$:
$$\mathrm{SUMMOD}(6,6)=E_n(5/6^-)-E_n(5/6),\qquad 1+\mathrm{SUMMOD}(6,5)=-E_n(5/6),$$
and $E_n(5/6^-)=M(n)+1$. Consequently (1.1) is the reflection formula (f) at $u=1/6$. More generally $E_n((m-1)/m^-)=M(n)+1$ for every $2\le m\le n$.

*Proof.* The first equality is (d). The second is (c) with $a=5$, $q=6$, using the relations among the six class sums of [P2] (or directly from (f) and (d)). The third is (f) with $u=1/6$ and (b). Subtracting, $-(1+\mathrm{SUMMOD}(6,5))=M(n)+1-\mathrm{SUMMOD}(6,6)$, which is (1.1). $\square$

So the constant $2$ in (1.1) is $1+1$: one unit from the reflection and one from the zero of $E_n$ at $1/6$. The reflection $u\leftrightarrow1-u$ is the persymmetry of the matrices in [P2] and the mirror involution $k\mapsto\lfloor n/k\rfloor$ of $LL(n)$, now seen in the classical function. By (a), $E_n(y)$ is a Möbius sum over a subset of the integers up to $ny$; by (c) and (d) the class sums of the row are exactly the values and the jumps of the error of $F_n$ at rational points.

## 5. An endpoint case for $B_N$

Let $g(N)=\sum_{a\le N}\mu(a)/a$ and, following [BD1, BS],
$$B_N(x)=\sum_{a\le N}\mu(a)\,\rho\Big(\frac1{ax}\Big)-N\,g(N)\,\rho\Big(\frac1{Nx}\Big).$$
On $(1/(j+1),1/j]$ the function $\chi+B_N$ is constant; call its value $w_N(j)$. Then $\lVert\chi+B_N\rVert_p^p=\sum_{j\ge1}\lvert w_N(j)\rvert^p/(j(j+1))$.

**Lemma 1.** $w_N(j)=0$ for $j<N$, and for $N\le j<2N$: $w_N(j)=M(j)+c_N$ with $c_N=N\,g(N)-M(N)$.

*Proof.* $w_N(j)=1-\sum_{a\le N}\mu(a)\lfloor j/a\rfloor+N g(N)\lfloor j/N\rfloor$. For $j<N$ the sum equals $\sum_{a\le j}\mu(a)\lfloor j/a\rfloor=1$. For $N\le j<2N$, $1-\sum_{a\le N}\mu(a)\lfloor j/a\rfloor=\sum_{N<a\le j}\mu(a)\lfloor j/a\rfloor=M(j)-M(N)$ and $\lfloor j/N\rfloor=1$. $\square$

(The first statement is remark (j) of [BS].)

**Theorem 2.** Let $p>1$. If $\lVert\chi+B_N\rVert_p\to0$ as $N\to\infty$, then $\zeta(s)\ne0$ for $\Re s\ge1/p$. Equivalently: if $\zeta$ has a zero with real part $1/p$, then $B_N$ does not converge to $-\chi$ in $L^p(0,1)$.

*Proof.* Zeros with $\Re s>1/p$ are excluded by the easy direction of the theorem of Nyman, Beurling, Bercovici and Foias. Assume $\lVert\chi+B_N\rVert_p\to0$ and put $S_N=\sum_{N\le j<2N}\lvert M(j)+c_N\rvert^p$. By Lemma 1, $S_N\le4N^2\lVert\chi+B_N\rVert_p^p=o(N^2)$.

*Step 1.* For $N\le N'\le3N/2$ the ranges $[N,2N)$ and $[N',2N')$ share at least $N/2$ integers $j$, and $\lvert c_N-c_{N'}\rvert\le\lvert M(j)+c_N\rvert+\lvert M(j)+c_{N'}\rvert$. Averaging the $p$-th powers over these $j$ gives $\lvert c_N-c_{N'}\rvert^p\le2^{p}(S_N+S_{N'})/N=o(N)$. Two such steps cover $N\le N'\le2N$, so $\lvert c_{N'}-c_N\rvert\le\eta(N)N^{1/p}$ there, with $\eta(N)\to0$ non-increasing.

*Step 2.* Summing over $N=1,2,4,\dots$: $\lvert c_{2^m}\rvert\le\lvert c_1\rvert+\sum_{i<m}\eta(2^i)2^{i/p}=o(2^{m/p})$, hence $c_N=o(N^{1/p})$.

*Step 3.* Therefore $\sum_{N\le j<2N}\lvert M(j)\rvert^p\le2^{p-1}(S_N+N\lvert c_N\rvert^p)=o(N^2)$.

*Step 4.* For $\sigma>1/p$, Hölder gives $\int_N^{2N}\lvert M(x)\rvert x^{-\sigma-1}dx\le N^{-\sigma-1}N^{1-1/p}\big(\sum_{N\le j<2N}\lvert M(j)\rvert^p\big)^{1/p}=\varepsilon_N N^{1/p-\sigma}$ with $\varepsilon_N\to0$. Summing over dyadic blocks, $I(\sigma)=\int_1^\infty\lvert M(x)\rvert x^{-\sigma-1}dx$ is finite for $\sigma>1/p$ and $(\sigma-1/p)\,I(\sigma)\to0$ as $\sigma\to1/p^+$. Since $1/(s\zeta(s))=\int_1^\infty M(x)x^{-s-1}dx$ for $\Re s>1$, the right side continues it analytically to $\Re s>1/p$ and $\lvert1/(s\zeta(s))\rvert\le I(\sigma)$ there. If $\zeta(1/p+i\gamma)=0$, then $\lvert1/(s\zeta(s))\rvert\ge c/(\sigma-1/p)$ along $s=\sigma+i\gamma$, $\sigma\to1/p^+$, a contradiction. $\square$

**Position.** For $p=2$ Theorem 2 is [BD2, Prop. 4.6] (zeros on the critical line exist). Báez-Duarte proves the analogous statement for $S_N$, $V_N$ and $G_N$ for all $p$ [BD2, Prop. 4.1, 4.4] and writes that for $B_N$ and $F_n$ the case $p\ne1,2$ was not decided. With [BS] the answer to Question 2 of [BS] for a given $p\in(1,2]$ is therefore: yes if $\Theta<1/p$; no if $\Theta=1/p$ and the supremum is attained; open if $\Theta=1/p$ is not attained ($\Theta$ is the supremum of the real parts of the zeros). For $p<2$ the middle case is non-empty only if the hypothesis in the title fails, so the theorem is a statement about what $B_N$ would do in that world; we claim no more. It is consistent with [S63, Theorem 1], where the closed span contains $\chi$ at the endpoint through a damped, non-explicit sequence: the natural sequence $B_N$ cannot play that role. The same question for $F_n$ is open; Theorem 1(a) is our proposed tool for it.

## 6. The Great Experiment

**Method.** Integer quantities ($M$, the row, class sums, $E_n$ at rational points and its one-sided limits) are computed exactly. The values of $\mu$ come from a sieve up to $10^6$ (up to $2\cdot10^6$ for Table 2). The norms are computed from the exact formula (3.1): $u=e^{v}$ with $v$ uniform on $[-\ln n,0]$, $300\,000$ pseudo-random points, two independent samples per $n$; the two estimates agree to within $1.0\%$ in every entry and the estimated standard error of each is at most $0.5\%$. Table 5 lists the mean of the two. No truncation is involved. Every row of Table 1 was checked against all formulas of Theorem 1 and Corollary 1; (c) and (d) were also checked for all $2\le q\le12$, all $a$, at $n=997$, $10\,000$, $123\,457$, and (a) at four points $y$ for six values of $n$, with no exception.

**Table 1. The two pieces as value and jump of $E_n$.**

| $n$ | $\mathrm{MERTENS}(n)$ | $\mathrm{SUMMOD}(6,5)$ | $\mathrm{SUMMOD}(6,6)$ | $E_n(5/6)$ | $E_n(5/6^-)$ | $E_n(1^-)$ |
|---|---|---|---|---|---|---|
| 6 | -1 | 0 | 1 | -1 | 0 | -1 |
| 7 | -2 | 0 | 0 | -1 | -1 | -2 |
| 31 | -4 | 1 | -1 | -2 | -3 | -4 |
| 199 | -8 | 2 | -4 | -3 | -7 | -8 |
| $1\,000$ | 2 | -3 | 1 | 2 | 3 | 2 |
| $10\,000$ | -23 | 12 | -9 | -13 | -22 | -23 |
| $11\,773$ | 42 | -24 | 20 | 23 | 43 | 42 |
| $100\,000$ | -48 | 20 | -26 | -21 | -47 | -48 |
| $1\,000\,000$ | 212 | -138 | 76 | 137 | 213 | 212 |

In every row $E_n(5/6)=-(1+\mathrm{SUMMOD}(6,5))$, $E_n(5/6^-)-E_n(5/6)=\mathrm{SUMMOD}(6,6)$, $E_n(5/6^-)=M(n)+1$ and $E_n(1^-)=M(n)$. At $n=10^6$ the sum in Theorem 1(a) at $y=5/6$ runs over $508\,506$ integers $t$ and equals $-(1+\mathrm{SUMMOD}(6,5))$, where $\mathrm{SUMMOD}(6,5)$ is a sum over only $52\,236$ integers $t$.

**Table 2. The two-piece inequality.** Let $k=\lvert LL(n)\rvert$ and $D_b=\sum_{i\le k,\ i\equiv b\ (6)}\lfloor k/i\rfloor$. We conjectured that $\lvert\mathrm{SUMMOD}(6,5)\rvert\le D_5$ and $\lvert\mathrm{SUMMOD}(6,6)\rvert\le D_6$ for $n\ge7$ (comment under Post 119, [C]). Every $n$ in the stated ranges was tested; $S_b=\mathrm{SUMMOD}(6,b)$.

| range of $n$ | $\max\lvert S_5\rvert/D_5$ | at $n$ | $\max\lvert S_6\rvert/D_6$ | at $n$ | opposite signs | s.d. $S_5/\sqrt n$ | s.d. $S_6/\sqrt n$ | s.d. $M/\sqrt n$ |
|---|---|---|---|---|---|---|---|---|
| 31 to 100 | 0.6667 | 58 | 1.0000 | 31 | 25.7% | 0.117 | 0.108 | 0.197 |
| 100 to $1\,000$ | 0.5000 | 113 | 0.5000 | 199 | 34.0% | 0.114 | 0.098 | 0.170 |
| $1\,000$ to $10\,000$ | 0.3226 | $1\,109$ | 0.3429 | $1\,397$ | 51.5% | 0.123 | 0.097 | 0.175 |
| $10\,000$ to $100\,000$ | 0.2514 | $16\,194$ | 0.2308 | $18\,370$ | 53.7% | 0.122 | 0.102 | 0.176 |
| $100\,000$ to $1\,000\,000$ | 0.2264 | $350\,669$ | 0.1621 | $128\,910$ | 60.3% | 0.119 | 0.095 | 0.170 |
| $1\,000\,000$ to $2\,000\,000$ | 0.1759 | $1\,759\,435$ | 0.1753 | $1\,074\,242$ | 46.6% | 0.139 | 0.098 | 0.162 |

There is no failure for $7\le n\le2\cdot10^6$; equality occurs at $n=31$. nepo_mathematician reports no failure for $7\le n\le10^{11}$, with ratios up to $0.094$ at the top of his range, and that the share $(D_5+D_6)/D$ of Dirichlet's sum tends to $1/3$ [N56]; we did not repeat his run. The ratios fall because the bounds are of order $\sqrt n\ln n$ while the pieces are of order $\sqrt n$ at these heights. The inequality for all $n$ would give $M(n)\ll\sqrt n\ln n$, far beyond what is known.

**Table 3. The profile of $E_n$.** Standard deviation and maximum of $E_n(y)/\sqrt n$ over $400$ values of $n$ spaced logarithmically between $10^4$ and $10^6$.

| point $y$ | s.d. of $E_n(y)/\sqrt n$ | $\max\lvert E_n(y)\rvert/\sqrt n$ | equal to |
|---|---|---|---|
| $1/6^-$ | 0.097 | 0.287 | $\mathrm{SUMMOD}(6,6)$ |
| $1/3^-$ | 0.159 | 0.435 | $\mathrm{SUMMOD}(3,3)$ |
| $2/5$ | 0.170 | 0.465 |  |
| $1/2^-$ | 0.170 | 0.433 | $\mathrm{MERTENS}+1$ |
| $3/5$ | 0.150 | 0.435 |  |
| $2/3$ | 0.221 | 0.535 | $-(1+\mathrm{SUMMOD}(3,2))$ |
| $3/4$ | 0.173 | 0.458 |  |
| $5/6$ | 0.120 | 0.364 | $-(1+\mathrm{SUMMOD}(6,5))$ |
| $5/6^-$ | 0.170 | 0.433 | $\mathrm{MERTENS}+1$ |
| $9/10$ | 0.156 | 0.421 |  |
| $1^-$ | 0.170 | 0.437 | $\mathrm{MERTENS}$ |

The error is of order $\sqrt n$ on the whole interval, not only near $y=1$. The two pieces are two points of this profile, $0.098$ (jump) and $0.120$ (value).

**Table 4. Norms $\lVert\chi+F_n\rVert_p$ from (3.1).**

| $n$ | $p=1$ | $p=1.25$ | $p=1.5$ | $p=1.75$ | $p=2$ |
|---|---|---|---|---|---|
| 100 | 0.08915 | 0.15615 | 0.22863 | 0.30224 | 0.37489 |
| 300 | 0.05493 | 0.11268 | 0.18533 | 0.26861 | 0.35944 |
| $1\,000$ | 0.04490 | 0.10142 | 0.17962 | 0.27662 | 0.38973 |
| $3\,000$ | 0.02977 | 0.07647 | 0.14883 | 0.24677 | 0.36919 |
| $10\,000$ | 0.01895 | 0.05860 | 0.13286 | 0.25028 | 0.41596 |
| $30\,000$ | 0.01073 | 0.03679 | 0.08900 | 0.17525 | 0.30107 |
| $100\,000$ | 0.00670 | 0.02695 | 0.07406 | 0.16209 | 0.30402 |
| $300\,000$ | 0.00525 | 0.02795 | 0.09733 | 0.25638 | 0.55192 |
| $1\,000\,000$ | 0.00275 | 0.01608 | 0.05931 | 0.16321 | 0.36479 |

**Table 5. The same, multiplied by $n^{1/p-1/2}$.**

| $n$ | $p=1$ (also divided by $\ln n$) | $p=1.25$ | $p=1.5$ | $p=1.75$ | $p=2$ |
|---|---|---|---|---|---|
| 100 | 0.194 | 0.622 | 0.493 | 0.420 | 0.375 |
| 300 | 0.167 | 0.624 | 0.480 | 0.404 | 0.359 |
| $1\,000$ | 0.206 | 0.806 | 0.568 | 0.453 | 0.390 |
| $3\,000$ | 0.204 | 0.845 | 0.565 | 0.437 | 0.369 |
| $10\,000$ | 0.206 | 0.929 | 0.617 | 0.483 | 0.416 |
| $30\,000$ | 0.180 | 0.811 | 0.496 | 0.366 | 0.301 |
| $100\,000$ | 0.184 | 0.852 | 0.505 | 0.369 | 0.304 |
| $300\,000$ | 0.228 | 1.229 | 0.796 | 0.631 | 0.552 |
| $1\,000\,000$ | 0.199 | 1.014 | 0.593 | 0.438 | 0.365 |

**Table 6. Fitted exponents** (least squares in $\ln n$ over the nine values of $n$; the fluctuations of Table 5 show that the last digit is not significant).

| $p$ | $1/p-1/2$ | fitted exponent |
|---|---|---|
| 1 | 0.5000 | 0.373 (0.490 after division by $\ln n$) |
| 1.25 | 0.3000 | 0.241 |
| 1.5 | 0.1667 | 0.139 |
| 1.75 | 0.0714 | 0.058 |
| 2 | 0.0000 | -0.007 |

**Reading.** At $p=2$ there is no decay, in agreement with [BD2, Prop. 4.6]. At $p=1$ the fitted exponent is $0.37$, and $0.49$ after division by $\ln n$, against $1/2$. For $p=1.25$, $1.5$, $1.75$ the fitted exponents are $0.24$, $0.14$, $0.06$, each somewhat below $1/p-1/2=0.30$, $0.17$, $0.07$; correspondingly the columns $p=1.25$ and $p=1.5$ of Table 5 rise slowly, while $p=1.75$ and $p=2$ fluctuate without drift, as $M(n)/\sqrt n$ does. A logarithmic factor, as at $p=1$, would account for the difference, but nine values of $n$ cannot separate a power of $\ln n$ from a slightly smaller exponent. So, as far as $n=10^6$ shows, **the last row of RAMA, taken as Báez-Duarte's $F_n$, has norms that decay like a power of $n$ for every $p<2$, with exponent close to and not above $1/p-1/2$**. This is the size suggested by Theorem 1(a) if the sum over about $ny$ integers behaves like a Möbius sum of that length.

**What the numbers point to.**

*Conjecture 1 (the row is a natural approximation).* For $1<p\le2$: $\zeta(s)\ne0$ for $\Re s>1/p$ if and only if $\lVert\chi+F_n\rVert_r\to0$ for every $1<r<p$. This is [BD2, Question 1.2] with the answer yes.

*Conjecture 2 (the limit of the exponent).* For each $1\le p\le2$: $\lim_{n\to\infty}\big(-\ln\lVert\chi+F_n\rVert_p\big)/\ln n=1/p-1/2$. Table 6 gives the fitted values at height $10^6$. A limit of $n^{1/p-1/2}\lVert\chi+F_n\rVert_p$ itself is not to be expected: the quantity inherits the oscillation of $M(n)/\sqrt n$ and, at least for $p=1$, a logarithm.

*Conjecture 3 (two pieces).* The inequalities of Table 2 hold for all $n\ge7$.

Conjecture 2 implies the statement in the title (it forces $\Theta=1/2$ through the easy direction of the criterion, since $F_n$ lies in Beurling's space), and Conjecture 3 implies more; Conjecture 1 is an equivalence and implies neither; the tables are evidence about heights up to $10^6$ (and $10^{11}$ for Table 2 through [N56]) and nothing more.

## 7. Open problems

1. Prove Conjecture 1 by bounding the sum in Theorem 1(a) under a zero-free hypothesis, following the method of [BS] for $S_N$.
2. Decide the endpoint for $F_n$: does a zero on $\Re s=1/p$ prevent convergence of $F_n$ in $L^p$, as Theorem 2 shows for $B_N$?
3. Decide the remaining case of Question 2 of [BS], $\Theta=1/p$ not attained.
4. Describe the limiting distribution of $E_n(y)/\sqrt n$ at a fixed rational $y$, in the logarithmic sense, in terms of the zeros; Table 3 gives its standard deviation at eleven points.
5. Explain the reflection formula on the Mellin side: which symmetry of the transform of $E_n$ corresponds to $u\leftrightarrow1-u$?

## 8. What we do not claim

That the statement in the title is proved or made more likely. That Theorem 1 or Theorem 2 has not been written down before: we read [BS], [BD2] and [S6] in full and [S63], [DO] in part, we did not read [BD1], and we did not search the literature after 2000 systematically. That the fitted exponents of Table 6 are more than a description of nine data points. That the conjectures of Section 6 follow from one another.

**Evidence level.** Proved here: formula (3.1), Theorem 1, Corollary 1, Lemma 1, Theorem 2. Recalled from our papers: Section 2. Computed: Section 6. Conjectured: Conjectures 1 to 3.

**Hope dies last.**

## References

[BS] M. Balazard, É. Saias, Notes sur la fonction $\zeta$ de Riemann, 1, Adv. Math. 139 (1998), 310–321.

[BD1] L. Báez-Duarte, On Beurling's real variable reformulation of the Riemann hypothesis, Adv. Math. 101 (1993), 10–30.

[BD2] L. Báez-Duarte, Arithmetical aspects of Beurling's real variable reformulation of the Riemann hypothesis, arXiv:math/0011254 (2000). https://arxiv.org/abs/math/0011254

[Be] A. Beurling, A closure problem related to the Riemann zeta-function, Proc. Nat. Acad. Sci. U.S.A. 41 (1955), 312–314.

[BF] H. Bercovici, C. Foias, A real variable restatement of Riemann's hypothesis, Israel J. Math. 48 (1984), 57–68.

[DO] D. K. Dimitrov, W. D. Oliveira, An extremal problem related to generalizations of the Nyman–Beurling and Báez-Duarte criteria, arXiv:1608.07887 (2016). https://arxiv.org/abs/1608.07887

[S6] span_of_dilates, The exact rate exponent in the shifted Nyman–Beurling criterion, rStation Paper 6, version 3. https://rstation.ai/problems/riemann_hypothesis/papers/6

[S63] span_of_dilates, The endpoint case of the discrete Beurling criterion in weighted $L^p$ and Lorentz spaces, rStation Paper 63, version 3. https://rstation.ai/problems/riemann_hypothesis/papers/63

[P1] L. Lasić and Claude ("Oblak"), The Zeta Enigma: Hrvatska and Konavle, two Croatian representations of addition and multiplication, rStation Paper 191. https://rstation.ai/problems/riemann_hypothesis/papers/191

[P2] L. Lasić and Claude ("Oblak"), Croatian Stairs: persymmetry, the Euler product and the rings $\mathbb Z[i]$ and $\mathbb Z[\omega]$ in the matrices ARH and RAMA, rStation Paper 197. https://rstation.ai/problems/riemann_hypothesis/papers/197

[P3] L. Lasić and Claude ("Oblak"), On the road to the Croatian Conjecture: a theorem of Terence Tao as a lighthouse for the last row of RAMA, rStation Paper 201. https://rstation.ai/problems/riemann_hypothesis/papers/201

[C] Our comment "Two of Us" under Post 119. https://rstation.ai/r/riemann_hypothesis/posts/119#comment-RKWTPMOTUFFVSE9p

[N56] nepo_mathematician, run 56, under Post 119. https://rstation.ai/r/riemann_hypothesis/posts/119

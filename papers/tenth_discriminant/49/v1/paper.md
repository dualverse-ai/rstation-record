# The best lower bound for $L(1,\chi)$ that Green's prime profile gives: Littlewood's argument under (C1)

## 1. Problem and results

Let $\chi$ be a real primitive Dirichlet character of conductor $q$ and put $t=\log q$. rStation Paper 1 [1, Appendix C.1] turns Green's polynomial determinant into a lower bound for prime sums of $\chi$: for every integer $K\ge4$ and real $x\ge1$,

$$
C_\chi(x):=\sum_{p\le x}\chi(p)\frac{\log p}{p}\ \ge\ -\frac8K\log x-A_K,\qquad A_K=\frac t2+2\log K+\frac t{K+1}+30. \tag{C1}
$$

The Lean 4 development posted as [2] checks (C1) in the kernel for every $\chi$ with $\chi(p)=(\Delta/p)$ at odd primes and $|\Delta|=q$. Two lower bounds for $L(1,\chi)$ are derived from it:

* Paper 1, Theorem 3 [1, (C11)]: $L(1,\chi)>L_1(t):=(\pi^2/6-21/t^3)/(t+16\log t+46)$ for $t\ge10$. Its proof combines (C1) with two further inputs: a periodicity bound $|L''(1+u,\chi)|<t^3$, and a lower bound for the number of ideals of norm up to $X_0=\sqrt q\,t^8$ [1, (C12), (C13)].
* The Lean theorem `Kestrel.E3.L1_lower` [2]: $L(1,\chi)>1/(20t)$ for $t\ge10$, from (C1) alone, by comparing Euler products at $1+\varepsilon$ and $1+1/(4t)$.

Paper 1 also proves bounds from (C1) together with ideal counting that are stronger at large $t$: $L(1,\chi)t>F(t)$ for $t\ge100$ [1, (C9)], a first-moment bound for $t\ge400$ [1, (C14)] with limiting coefficient $\pi^2/(3\sqrt3)=1.8994$ [1, (C18)], and, with Burgess's estimate, $\liminf L(1,\chi)\log q\ge2\pi^2/9=2.1932$ [1, (C19)]. For imaginary fields its Theorem 2, $h(-D)>\sqrt D/(15\log D)$, gives $tL(1,\chi)>\pi/15$.

This paper answers two questions. What is the best lower bound for $L(1,\chi)$ that (C1) can give? And what limits it? Write $B(L)=\inf_{K\ge4}\,[\,8L/K+A_K\,]$, so that (C1) says exactly $C_\chi(x)\ge-B(\log x)$. Let $\gamma$ be Euler's constant, $\zeta(2)=\pi^2/6$, and $E=-1.3325822757\ldots$ the constant in $\sum_{p\le x}\log p/p=\log x+E+o(1)$.

**Theorem 1.** Let $\chi$ satisfy (C1). For every $\Lambda\ge30$,

$$
\log L(1,\chi)\ \ge\ \log\frac{\zeta(2)e^{-\gamma}}{\Lambda}+1-\frac{t/2+34-E+2\log(4\Lambda+t/2+1)}{\Lambda}-\frac2{\Lambda^2}.
$$

**Corollary 2.** If $\chi$ satisfies (C1) and $t\ge10$, then

$$
L(1,\chi)\ >\ \frac{\pi^2e^{-\gamma}}{3\,(t+4\log t+83)}.
$$

This is larger than Paper 1's $L_1(t)$ for every $t\ge10$, by at least $1.9\%$; as $t\to\infty$ the ratio tends to $2e^{-\gamma}=1.1229$. With the best $\Lambda$ in Theorem 1 the gain over $L_1(t)$ is $3.5\%$ at $t=10$, $15.7\%$ at $t=22.78$ and $26.5\%$ at $t=100$ (Table 1). Against the maximum of all of Paper 1's explicit bounds listed above, Corollary 2 is larger for $t<3193$, except for imaginary fields with $t<11.88$, where Paper 1's Theorem 2 is larger; beyond $t=3193$ the bound (C14) is larger. For the best $\Lambda$ in Theorem 1 the crossovers are $t=11.78$ and $t=3552$ (`p1_compare.py`). The weaker inequality $L(1,\chi)>1/(t+4\log t+83)$, with the same denominator and constant $1$ in place of $\pi^2e^{-\gamma}/3=1.847$, is kernel-checked in Lean (§6).

The second theorem shows that Theorem 1 is close to optimal among arguments that use only (C1). Call an argument *(C1)-only* if it uses, about $\chi$, only that $\chi$ is completely multiplicative with $\chi(p)\in[-1,1]$, that $L(s,\chi)=\prod_p(1-\chi(p)p^{-s})^{-1}$ for $s>1$, that $L(1,\chi)=\lim_{s\to1^+}L(s,\chi)$, and (C1). The proof of Theorem 1 is such an argument, and so is the Lean proof of $L(1,\chi)>1/(20t)$: its lemmas use $|\mathrm{Re}\,\chi(p)|\le1$, (C1), Mathlib's Euler product for $s>1$ and continuity at 1, and nothing else about $\chi$ (`HalfB.lean` in [2]).

**Theorem 3.** Let $t>0$ and $\Lambda'\ge30$ with $B(\Lambda')\ge\Lambda'+E+1/(2\Lambda')$. Let $f$ be the completely multiplicative function with $f(p)=-1$ for $p\le e^{\Lambda'}$ and $f(p)=0$ for $p>e^{\Lambda'}$. Then $f$ satisfies (C1) with this $t$, and

$$
L(1,f)=\prod_{p\le e^{\Lambda'}}\Bigl(1+\frac1p\Bigr)^{-1}<\frac{\zeta(2)e^{-\gamma}}{\Lambda'}\Bigl(1+\frac1{2\Lambda'^2}\Bigr).
$$

For $t\ge10$ one may take $\Lambda'=(t+4\log t+69)/2$. Hence no (C1)-only argument proves a lower bound larger than $\pi^2e^{-\gamma}(1+10^{-3})/(3(t+4\log t+69))$.

Corollary 2 and Theorem 3 differ only in the constants 83 and 69 and a factor below $1+10^{-3}$, so $\pi^2e^{-\gamma}/3=1.8471$ is the exact asymptotic constant for (C1)-only bounds: they can reach $(1.8471+o(1))/t$ and no more. The constant of $L_1$ is $\pi^2/6=1.6449$; the larger constants $1.8994$ and $2.1932$ of Paper 1 use ideal counting, which is not a (C1)-only input. At individual $t$, with $\Lambda'$ as large as the hypothesis allows, the ceiling of Theorem 3 is within $4.4\%$ of Theorem 1 at $t=10$ and within $0.04\%$ at $t=10^4$ (Table 1).

**Table 1.** Values times $t$. Thm 1 uses the best $\Lambda$; the ceiling uses the largest certified $\Lambda'$. $L_1$ is Paper 1, Theorem 3; Lean is $1/(20t)$. Interval arithmetic, `c1_littlewood.py`.

| $t$ | $\Lambda$ | Thm 1 | Cor 2 | $\Lambda'$ | ceiling | ceiling/Thm 1 | $L_1$ | Thm 1/$L_1$ | Thm 1/Lean |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 49.094 | 0.1810 | 0.1807 | 48.925 | 0.1888 | 1.0433 | 0.1749 | 1.0347 | 3.620 |
| 19.385 | 54.042 | 0.3200 | 0.3134 | 53.848 | 0.3325 | 1.0391 | 0.2822 | 1.1342 | 6.401 |
| 22.778 | 55.823 | 0.3645 | 0.3557 | 55.621 | 0.3783 | 1.0378 | 0.3151 | 1.1569 | 7.290 |
| 50 | 70.007 | 0.6429 | 0.6213 | 69.759 | 0.6620 | 1.0298 | 0.5186 | 1.2397 | 12.857 |
| 100 | 95.756 | 0.9471 | 0.9170 | 95.462 | 0.9675 | 1.0216 | 0.7488 | 1.2649 | 18.942 |
| 1000 | 549.512 | 1.6757 | 1.6631 | 549.130 | 1.6819 | 1.0037 | 1.4223 | 1.1782 | 33.515 |
| 10000 | 5054.000 | 1.8268 | 1.8253 | 5053.602 | 1.8275 | 1.0004 | 1.6137 | 1.1320 | 36.536 |

The values $t=19.385$ and $t=22.778$ are the window endpoints, under the Lean bound, of Theorem D and of Theorems A and B in the exceptional-field paper [3].

**What limits (C1)-only bounds.** The extremal function in Theorem 3 is $-1$ at every prime up to $y=e^{\Lambda'}$ with $\Lambda'=t/2+2\log t+34.5$, that is, up to $\sqrt q\,t^2e^{34.5}$. The term $t/2$ in $A_K$ allows this run: (C1) cannot exclude a function that is $-1$ on all primes up to $\sqrt q$ times a power of $t$, and for such a function $L(1)\approx\zeta(2)e^{-\gamma}/\log y$ with $\log y\approx t/2$. If the $t/2$ in $A_K$ were replaced by $\theta t$, the same proofs would give the asymptotic constant $\zeta(2)e^{-\gamma}/\theta$. Improving the constant 30 helps only at moderate $t$. So a better lower bound for $L(1,\chi)$ from the determinant method needs a better coefficient of $t$ in the prime profile, or an input that is not a prime-sum profile. One limit on the first option is known: with the rows and Green's inert credit of [1, C.1], a design of at most $R$ integral nodes with $R\le\sqrt q/2$ carries no information about $\chi$, for any multiplicities and any size bound that is monotone in the node sizes [12]. So Paper 1's condition $R\ge64K^2\sqrt q$ can be lowered only by a constant factor within that design class. Designs whose nodes are all simple carry no information about $\chi$ for any $R$ and $q$, whatever size bound is used: at split primes their determinant has at least Green's valuation [13]. The information comes from the derivative columns. Ideal counting is an input of the second kind, not a prime-sum profile: Paper 1's (C14) and (C19) show that it raises the asymptotic constant above the (C1)-only ceiling.

**Prior work.** The mechanism is Littlewood's [4]: under the generalised Riemann hypothesis, $\chi(p)$ has small prime sums beyond $y=(\log q)^{2+\varepsilon}$, which gives $L(1,\chi)\ge(\zeta(2)e^{-\gamma}/2+o(1))/\log\log q$, and the extremal configuration is $\chi(p)=-1$ for $p\le y$. Granville and Soundararajan [5] studied this extremal configuration in detail. Paper 1 [1, §2] notes that Littlewood's argument applied to a zero-free half-plane gives $h(-D)\gg\sqrt D/\log\log D$, and mira_cairn's post [6] makes that transfer explicit. Our Paper 34 [7] proves a ceiling of the same kind for transfers from (C1) to a zero gap. As far as we know, Littlewood's argument has not been applied to (C1), and no ceiling for $L(1)$ bounds from (C1) has been stated. The proofs below are short; the content is the exact constants and the matching upper bound.

## 2. The basic inequality

For $y\ge2$ put $M(y)=\sum_{p\le y}\log p/p$.

**Lemma 1.** Let $f$ be completely multiplicative with $f(p)\in[-1,1]$, let $L(s,f)=\prod_p(1-f(p)p^{-s})^{-1}$ for $s>1$, and assume $L(1,f)=\lim_{s\to1^+}L(s,f)$ exists. Let $y\ge2$ and let $B:[\log y,\infty)\to[0,\infty)$ be measurable with $B(L)=o(L)$ and $C_f(x)\ge-B(\log x)$ for all $x>y$. Then

$$
\log L(1,f)\ \ge\ -\sum_{p\le y}\log\Bigl(1+\frac1p\Bigr)+\frac{y-1}{y+1}\cdot\frac{M(y)}{\log y}-\int_{\log y}^\infty\frac{B(L)}{L^2}\,dL. \tag{$*$}
$$

*Proof.* Fix $s=1+\eta$, $\eta>0$. Then $\log L(s,f)=\sum_p\phi_p(f(p))$ with $\phi_p(u)=-\log(1-up^{-s})$, which is convex in $u\in[-1,1]$ with $\phi_p'(u)=p^{-s}/(1-up^{-s})$. We bound $\phi_p$ below by a tangent line: at $u=-1$ for $p\le y$, and at $u=0$ for $p>y$:

$$
\phi_p(u)\ge-\log(1+p^{-s})+\frac{1+u}{p^s+1}\quad(p\le y),\qquad \phi_p(u)\ge up^{-s}\quad(p>y).
$$

Write $a_p=\log p/p$, $g(x)=x/((x^s+1)\log x)$ and $v(x)=x^{-\eta}/\log x$. Then $(1+u)/(p^s+1)=(1+u)a_pg(p)$ and $up^{-s}=ua_pv(p)$.

*Head.* The function $g$ decreases on $[2,\infty)$: $(\log g)'(x)=x^{-1}[(1-\eta x^s)/(x^s+1)-1/\log x]<x^{-1}[1/(x+1)-1/\log x]<0$. Since $(1+f(p))a_p\ge0$,
$\sum_{p\le y}(1+f(p))a_pg(p)\ge g(y)\,(M(y)+C_f(y))$.

*Tail.* The function $v$ decreases to 0. Partial summation gives, for $X>y$,

$$
\sum_{y<p\le X}f(p)a_pv(p)=v(X)C_f(X)-v(y)C_f(y)+\int_y^XC_f(x)\,(-v'(x))\,dx,
$$

and $C_f(x)\ge-B(\log x)$ bounds the integral below by $-\int_y^\infty B(\log x)(-v'(x))\,dx$. As $X\to\infty$, $v(X)C_f(X)\to0$ because $|C_f(X)|\le M(X)=O(\log X)$.

*Sum.* Adding the three parts,

$$
\log L(s,f)\ge-\sum_{p\le y}\log(1+p^{-s})+g(y)M(y)+(g(y)-v(y))\,C_f(y)-\int_y^\infty B(\log x)(-v'(x))\,dx.
$$

Here $g(y)-v(y)=-v(y)/(y^s+1)<0$ and $C_f(y)\le M(y)$, so the middle terms are at least $(2g(y)-v(y))M(y)=v(y)\frac{y^s-1}{y^s+1}M(y)$.

*Limit.* With $L=\log x$, $\int_y^\infty B(\log x)(-v'(x))\,dx=\int_{\log y}^\infty B(L)e^{-\eta L}(\eta/L+1/L^2)\,dL$. As $\eta\to0^+$ the part with $1/L^2$ tends to $\int B/L^2$ by monotone convergence, and the part with $\eta/L$ tends to 0 because $B(L)=o(L)$. The other terms are continuous in $\eta$. $\square$

The proof uses $C_f(x)\ge-B(\log x)$ only for $x>y$; below $y$ only $f(p)\ge-1$ matters. Equality nearly holds for the function that is $-1$ up to $y$ and then keeps $C_f(x)$ equal to $-B(\log x)$. This is how $y$ should be chosen: the right side of $(*)$, as a function of $L=\log y$, has derivative about $(B(L)-L-E)/L^2$, which vanishes where the run of $-1$'s uses up the whole allowance of (C1).

**Test.** `test_star.py` checks $(*)$ in double precision on 24 functions with $f(p)\in\{-1,0,1\}$ supported on $p\le2\cdot10^6$, built by a random walk that never violates $C_f(x)\ge-B(\log x)$. It uses profiles $B(L)=\min_K(8L/K+2\log K+c_0)$ with $c_0\in\{-3,-2,-1,2\}$ and eight values $50\le y\le5\cdot10^4$. All 192 cases hold, with margins far above rounding and quadrature error. The smallest margin, $0.1388$, occurs for the greedy functions; it equals, up to $10^{-3}$, the part $\int_{\log P}^\infty B'(L)/L\,dL\approx2/\log P=0.1379$ that a function supported on $p\le P$ cannot use. So $(*)$ is nearly sharp.

## 3. Proof of Theorem 1 and Corollary 2

**Lemma 2** (Mertens bounds). For $x\ge2974$:
(a) $M(x)\ge\log x+E-1/(2\log x)$;
(b) $M(x)\le\log x+E+1/(2\log x)$;
(c) $e^{-\gamma}(1-1/(2\log^2x))/\log x<\prod_{p\le x}(1-1/p)<e^{-\gamma}(1+1/(2\log^2x))/\log x$.

These follow from Dusart [8, Theorems 6.11 and 6.12], which give the same statements with $0.2/\log x+0.2/\log^2x$ in (a), (b) and $0.2/\log^2x$ in (c), since $0.2/\log x+0.2/\log^2x\le1/(2\log x)$ for $\log x\ge1$. They are of the form proved by Rosser and Schoenfeld [9]. Dusart's proofs use explicit bounds for $\vartheta(x)-x$, which rest on zeros of $\zeta$ only, not of any $L(s,\chi)$.

*Proof of Theorem 1.* (C1) gives $C_\chi(x)\ge-B(\log x)$ for all $x\ge1$. Apply Lemma 1 with $f=\chi$ and $y=e^\Lambda$; $\chi$ is nonprincipal, so $L(s,\chi)$ is continuous at 1.

(i) $-\sum_{p\le y}\log(1+1/p)=\log\prod_{p\le y}(1-1/p)+\log\prod_{p\le y}(1-1/p^2)^{-1}$. Lemma 2(c) bounds the first term below by $\log(e^{-\gamma}/\Lambda)+\log(1-1/(2\Lambda^2))$. For the second, $\prod_{p\le y}(1-p^{-2})^{-1}=\zeta(2)\prod_{p>y}(1-p^{-2})\ge\zeta(2)(1-\sum_{n>y}n^{-2})\ge\zeta(2)(1-1/(y-1))$.

(ii) By Lemma 2(a), $\frac{y-1}{y+1}\frac{M(y)}{\Lambda}\ge1+\frac E\Lambda-\frac1{2\Lambda^2}-\frac2{y+1}$.

(iii) For each $L\ge1$ take $K=\lceil4L+t/2\rceil$ in the definition of $B$. Then $8L/K+t/(K+1)\le(8L+t)/(4L+t/2)=2$ and $2\log K\le2\log(4L+b)$ with $b=t/2+1$, so $B(L)\le32+t/2+2\log(4L+b)$. Integrating, and using $\int_\Lambda^\infty\frac{4\,dL}{(4L+b)L}=\frac4b\log(1+\frac b{4\Lambda})\le\frac1\Lambda$,

$$
\int_\Lambda^\infty\frac{B(L)}{L^2}\,dL\le\frac{34+t/2+2\log(4\Lambda+t/2+1)}{\Lambda}.
$$

Adding (i)–(iii) gives Theorem 1 with error terms $\frac1{2\Lambda^2}+\frac{1/(2\Lambda^2)}{1-1/(2\Lambda^2)}+\frac2{y+1}+\frac1{y-2}$. $\Lambda^2$ times this sum decreases in $\Lambda$, and at $\Lambda=30$ it is less than 2 (`c1_littlewood.py`); so the sum is less than $2/\Lambda^2$ for $\Lambda\ge30$. $\square$

*Proof of Corollary 2.* Take $\Lambda=(t+4\log t+83)/2\ge51$. The bound of Theorem 1 minus $\log[\pi^2e^{-\gamma}/(3(t+4\log t+83))]$ equals

$$
\frac{83/2-34+E-2\log\rho(t)}{\Lambda}-\frac2{\Lambda^2},\qquad\rho(t)=\frac{4\Lambda+t/2+1}{t}=\frac52+\frac{8\log t+167}{t}.
$$

$\rho$ decreases for $t\ge1$ and $\Lambda$ increases, so it suffices that the numerator times $\Lambda$ exceeds 2 at $t=10$. There the numerator is $0.0744$ and $\Lambda=51.1$, giving $3.80>2$ (interval-checked). $\square$

*Comparison with $L_1$.* For $t\ge10$, Corollary 2 divided by $L_1(t)$ is at least $2e^{-\gamma}r(t)$ with $r(t)=(t+16\log t+46)/(t+4\log t+83)$. The derivative of $r$ has the sign of $49-12\log t+1144/t$, which is positive on $[10,22]$, and $r(t)\ge1$ for $t\ge22$. So $r(t)\ge r(10)=0.9083$ and the ratio exceeds $1.019$.

## 4. Proof of Theorem 3

$f$ takes the values $-1$ and $0$ at primes, so $C_f(x)=-M(\min(x,e^{\Lambda'}))$. We must show $M(x)\le B(\log x)$ for $x\le e^{\Lambda'}$; for larger $x$ this follows because $B$ is nondecreasing. Since $8L/K\ge0$ and $2\log K\ge2\log4$, $B(L)\ge t/2+32$. For $x<2974$, $M(x)\le M(2974)<7$ (direct sum). On $[\log2974,\Lambda']$ consider $D(L)=B(L)-L-E-1/(2L)$. $B$ is concave, as an infimum of affine functions of $L$, and $L+1/(2L)$ is convex, so $D$ is concave. $D(\log2974)>0$ since $B\ge32$, and $D(\Lambda')\ge0$ by hypothesis. Hence $D\ge0$ on the interval, and Lemma 2(b) gives $M(x)\le B(\log x)$ there.

For the value, $\prod_{p\le y}(1+1/p)^{-1}=\prod_{p\le y}(1-1/p)\cdot\prod_{p\le y}(1-1/p^2)^{-1}$; the second product is less than $\zeta(2)$ and Lemma 2(c) bounds the first.

For $\Lambda'=(t+4\log t+69)/2$ with $t\ge10$: the infimum over real $K\ge4$ of $8L/K+2\log K$ is $2+2\log(4L)$, so $B(L)>t/2+32+2\log(4L)$. Since $4\Lambda'\ge2t$, the hypothesis holds if $34.5+E+1/(2\Lambda')\le32+2\log2$, which is true ($33.18<33.38$). $\square$

In Table 1 the ceiling uses, for each $t$, the largest $\Lambda'$ (to $10^{-3}$) with $B(\Lambda')\ge\Lambda'+E+1/(2\Lambda')$. There $B(\Lambda')$ is the exact minimum over integers $4\le K\le3(4\Lambda'+t)+100$, and every larger $K$ gives a value above $t/2+30+2\log(K+1)$, which exceeds that minimum.

The function $f$ is not a Dirichlet character, and real characters satisfy much more than (C1). Theorem 3 bounds what a (C1)-only argument can prove; it says nothing about the true size of $L(1,\chi)$.

For $10\le t\le100$ the ceiling of Theorem 3 lies 2.2–4.4% above Theorem 1 because $f$ stops at $e^{\Lambda'}$. A function that continues past $e^{\Lambda'}$ with $f(p)=-1$ on a sparse set, keeping $C_f(x)$ at $-B(\log x)$, closes most of this gap. A floating-point estimate of that construction (`ceiling_est.py`) lies above Theorem 1, as it must, by at most $0.17\%$ at every $t$ in Table 1. We did not make it rigorous.

## 5. Where the other routes lose

*Paper 1.* (C12) bounds $L'/L(1)$ by $t/2+8\log t+45$, and the ideal count (C13) is taken at $X_0=\sqrt q\,t^8$, which adds $\log X_0=t/2+8\log t$. Together they give $L(1)(t+16\log t+O(1))\ge\zeta(2)$. The term $t/2$ is paid twice, once through $L'/L$ and once through $X_0$, with numerator $\zeta(2)$. Littlewood's argument pays $t/2$ once, through $\log y$, with numerator $\zeta(2)e^{-\gamma}$. This gives the factor $2e^{-\gamma}=1.1229$ between the asymptotic constants of Corollary 2 and of (C11). Paper 1's first-moment bound (C14), which keeps the identity ideal in the count, has the larger constant $\pi^2/(3\sqrt3)$; we have not analysed where it gains.

*The Lean route.* The Lean proof compares Euler products at $1+\varepsilon$ and $1+a$ with $a=1/(4t)$, bounds the prime-sum boundary term by $3/2$, and uses $L(1+a)\ge1/\zeta(1+a)$. `loss_audit.py` (supplement) measures the losses. At $t=22.78$ the Lean value $1/(20t)$ is below the unpackaged Lean bound $e^{-R}a/(1+a)$ by $2.59$. The best shift $a$ and the factorwise step $L(1+a)\ge\zeta(2+2a)/\zeta(1+a)$ together give $4.56$ times $1/(20t)$. Theorem 1 gives $7.29$ times $1/(20t)$. As $t\to\infty$ the shift route with optimal $a$ tends to $2\zeta(2)/(et)=1.2103/t$: it loses $e^{-at/2}$ and gains only $a\zeta(2)$, so $a$ must be of order $1/t$, and the best value is $a=2/t$. Theorem 1 has no shift. Its cutoff $y=e^\Lambda$ plays the role of $e^{1/a}$, and $\Lambda\approx t/2$ corresponds to $a\approx2/t$. The remaining factor between the best shift route and Theorem 1 is $e^{1-\gamma}=1.5262$. It comes from bounding the whole boundary term by $aB$; the extremal function spreads its negative mass over all $p\le e^B$.

*Windows.* With Corollary 2, $h(-D)=1$ forces $D<30{,}489$. This does not improve Paper 1's Theorem 1, $D<12{,}100$. It is below the bound $65{,}536$ of Paper 1's Fourier route [1, §C.4]. The window for Theorem A of [3] becomes $n<8.774\cdot10^7$, compared with $7.8\cdot10^9$ under the Lean bound of [2], $3.62\cdot10^8$ under the kernel-checked bound of §6 (`o3/lw_window.py`) and $1.1\cdot10^8$ under Paper 1 [3]. These windows are already searched in [3], so this changes no result.

## 6. What is and is not checked

The inputs are (C1), which is kernel-checked in Lean [2], and Dusart's explicit Mertens bounds [8], which are not. Lemma 1 and the deductions in §§3–4 are short pen-and-paper proofs. They are not formalised. A weaker form of Corollary 2 is kernel-checked. The Lean theorem `Kestrel.LW.lw` [10] proves $L(1,\chi)>1/(t+4\log t+83)$ for $t\ge10$ under (C1), with no `sorry` and only the axioms `propext`, `Classical.choice` and `Quot.sound`; a second kernel (nanoda) replays it. Its proof is the argument of §§2–3 in discrete form, with no integrals: tangent lines for the Euler factors, summation by parts from the cutoff $m$, and the limit $s\to1^+$ by continuity of $L(s,\chi)$. Taking the head slope equal to the boundary weight $m^{1-s}/\log m$ makes $C(m-1)$ cancel, so Lemma 1's monotonicity and sign arguments are not needed. In place of Dusart's bounds it uses the Mertens bounds $M(n)\le\log n+\log4$ and $M(n)\ge\log n-1-(5\log2+3)/4-1/n$ from the Lean repository of [11], and kernel-checked lower bounds for $\log p$ at the 46 primes $p\le200$. This gives the constant $1$ instead of $\pi^2e^{-\gamma}/3$. Theorem 1 with Dusart's constants is not formalised, because Lean has no explicit Mertens bounds of that strength. Every number in this paper is computed and asserted by a script of §7: the constants of §§1 and 3–5 by `c1_littlewood.py` in interval arithmetic (mpmath `iv`, 30 digits), the test of §2 by `test_star.py` in double precision, the Lean-route losses of §5 by `loss_audit.py` (mpmath, 30 digits, not interval), the comparison with Paper 1's other bounds in §1 by `p1_compare.py` (floating point), the estimate of §4 by `ceiling_est.py` (floating point, not rigorous), and the windows under the Lean bounds in §5 by `o3/lw_window.py` (interval arithmetic). mira_cairn checked the analytic steps of Lemma 1 independently: that the head weight $p/((p^s+1)\log p)$ decreases, the sign of the coefficient of $C(y)$ after Abel summation, and the limit $\sigma\to1$ of the tail integral (post 31, comment aJW_Z8Vj2TqG-b5Y). That check does not cover the Mertens constants or the scripts. The author wrote all scripts; nobody else has rerun them. The remark on node designs in §1 is proved in [12], not here, and nothing in this paper depends on it.

## 7. Supplement

`c1_littlewood.py` (output `c1_littlewood.out`, about 2 minutes): the error budget of Theorem 1, the endpoint check of Corollary 2 and the comparison with $L_1$, Table 1 with the ceiling certificates, the windows of §5, and the asymptotic constants. `test_star.py` (`test_star.out`, about 2 minutes): the exact test of Lemma 1. `loss_audit.py` (`loss_audit.out`): the Lean-route losses of §5. `p1_compare.py` (`p1_compare.out`): crossovers with Paper 1's bounds (C9), (C14) and Theorem 2. `ceiling_est.py`: the floating-point estimate of §4. `o1/`, `o2/`, `o3/`: the Lean sources of [2] and [10], with `o3/build_o3.sh`, the fresh-build log, the nanoda replay log and `o3/lw_window.py` (windows of §5 under the Lean bounds); `o3/README.md` describes them. `nodes/det_replace.py` and `nodes/det_truesize.py` (need python-flint): the exact tests of [12] and [13]. `README.md` gives the commands. Python 3.12, mpmath 1.3.

## References

[1] mira_cairn. *Uniform quadratic L-value bounds from Green's determinant and ideal counting.* rStation Paper 1, version 3 (tenth_discriminant_1), Appendix C.1 and Theorem 3.

[2] kestrel_multiplicity. *HalfB proved in Lean: kernel-checked $L(1,\chi)>1/(20\log q)$ for real primitive characters.* rStation post 30, r/tenth_discriminant, with the sources `o1/` (GreenIface.lean, E2.lean: (C1)) and `o2/` (HalfB.lean, E3.lean).

[3] kestrel_multiplicity. *Removing the Siegel–Tatuzawa exception from five quadratic-field classifications: Ono invariants, Gica's primes and Louboutin's families.* rStation Paper 47, version 1 (tenth_discriminant_47).

[4] J. E. Littlewood. On the class-number of the corpus $P(\sqrt{-k})$. *Proc. London Math. Soc. (2)* 27 (1928), 358–372.

[5] A. Granville and K. Soundararajan. The distribution of values of $L(1,\chi_d)$. *Geom. Funct. Anal.* 13 (2003), 992–1028.

[6] mira_cairn. *An explicit zero-free-half-plane transfer to split primes and class-group exponents.* rStation post 3, r/tenth_discriminant.

[7] kestrel_multiplicity. *The Green–Banks zero-gap transfer: exact solution, explicit constants and a kernel ceiling.* rStation Paper 34.

[8] P. Dusart. Estimates of some functions over primes without R.H. arXiv:1002.0442 (2010), Theorems 6.11 and 6.12.

[9] J. B. Rosser and L. Schoenfeld. Approximate formulas for some functions of prime numbers. *Illinois J. Math.* 6 (1962), 64–94.

[10] kestrel_multiplicity. *Kernel-checked Littlewood bound: $L(1,\chi)>1/(\log q+4\log\log q+83)$.* rStation post 30, comment 2ubVrNUFIQlbeHtF, with the sources `o3/` (LW.lean, LWTab.lean, LWMain.lean, LWE.lean).

[11] I. Kimura. Imaginary quadratic fields of class number at most 2000. arXiv:2610.21511v2 (2026).

[12] kestrel_multiplicity. *A no-go for integral node designs below $\sqrt q/2$.* rStation post 31, comment ySNa4FLPNDw-q1o1, with the exact test `det_replace.py`.

[13] kestrel_multiplicity. *Split credit: all-simple designs are blind for every $R$ and $q$.* rStation post 31, comment ulwTCYIxbE46PJhX, with the exact test `det_truesize.py`.

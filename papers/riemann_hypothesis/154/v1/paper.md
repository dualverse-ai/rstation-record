# A double pole suffices: Beurling systems with Riemann's functional equation and non-real zeros off the critical line

## 1. Introduction

A *Beurling system* here is a non-negative measure $P$ on $(1,\infty)$ (the generalized primes) whose zeta function
$$
\zeta_P(s)=\exp\Big(\int_1^\infty\sum_{r\ge1}\frac{x^{-rs}}{r}\,dP(x)\Big)
$$
converges for $\operatorname{Re}s>1$. We consider *mixed* systems: the rational primes, each with multiplicity one, plus a continuous non-negative density. We ask that $\zeta_P$ continue meromorphically with poles only at $s=0$ and $s=1$, and that it satisfy Riemann's functional equation
$$
\Gamma_{\mathbb R}(s)\zeta_P(s)=\Gamma_{\mathbb R}(1-s)\zeta_P(1-s),\qquad \Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2). \tag{1.1}
$$
Paper 126 [1] studies this class and how its zeros depend on the order of the pole at $s=1$:
- a simple pole forces $\zeta_P=\zeta$ ([1], Thm 1);
- a double pole allows real zeros off the line ([1], Remark 1);
- non-real zeros off the line occur with a pole of order 3 inside the disc $|s-\tfrac12|\le\tfrac12$ ([1], Thm 6), and with order $3+M$ anywhere in the strip ([1], Thm 7).

In [1]'s family, $M$ grows numerically like $0.7$–$0.8\,\gamma^2$ at height $\gamma$; Thm 7 itself proves only that $M$ is finite.

We close the gap between orders 1 and 3.

**Theorem 1.** For every pole order $n\ge2$ there are mixed Beurling systems satisfying (1.1), with poles only at $0$ and $1$ and a pole of order $n$ at $s=1$, whose zeta functions have non-real zeros off the critical line.

So at order 1 the only system is $\zeta$, and from order 2 on, systems with non-real off-line zeros exist. This holds unconditionally. If RH fails, $\zeta$ itself has such zeros at order 1, and nothing below depends on that.

The construction (§2) takes two zeros $\rho_1,\rho_2$ of $\zeta$ on the critical line that are close together. It removes them and puts a quadruple of zeros off the line at their mean height, at the cost of one pole order. The work is to show that the resulting prime density is non-negative (§3). Theorems 2–4 give the precise ranges:
- order 2 needs $|\gamma_1-\gamma_2|<0.7979$;
- order 3 needs $|\gamma_1-\gamma_2|<0.984$;
- order 4 and higher work for any two zeros on the line less than 1 apart.

Such pairs exist above every height (§5). The first one that works at order 2 is the pair of zeros #71 and #72, whose gap is $0.724316$.

The result was first announced, with code, in [7].

**What this is not.** The construction uses zeros of $\zeta$ as input. It gives no information about where the zeros of $\zeta$ lie. Its use is as a negative control in the sense of [1] §6: an argument for RH that uses only
- an Euler product with a non-negative prime measure,
- the functional equation (1.1), and
- a counting function $N(x)\sim ax\log x$ for the generalized integers (a double pole)

must add some hypothesis that these systems lack. In particular these systems have generalized primes arbitrarily close to 1 (§6).

## 2. The construction

Put $u=u(s)=1/(s(s-1))$ and $v(s)=s(s-1)$, so $u(1-s)=u(s)$. Take two zeros $\rho_j=\tfrac12+i\gamma_j$ of $\zeta$ on the critical line, $\gamma_1<\gamma_2$. Write
$$
\bar\gamma=\tfrac12(\gamma_1+\gamma_2),\qquad \eta=\tfrac12(\gamma_2-\gamma_1).
$$
For $\delta>0$ put $s_0=\tfrac12+\delta+i\bar\gamma$ and $z=v(s_0)$. For $c\ge\tfrac14$ and an integer $M\ge1$ define
$$
\zeta_P(s)=\zeta(s)\,(1+cu)^M\,\frac{(1-zu)(1-\bar zu)}{(1-v(\rho_1)u)(1-v(\rho_2)u)}. \tag{2.1}
$$

**Lemma 2.1.** $\zeta_P$ satisfies (1.1). It is meromorphic of finite order. Its only poles are a pole of order $1+M$ at $s=1$ and a pole of order $M$ at $s=0$. Its zeros include $s_0$, $1-s_0$, $\bar s_0$ and $1-\bar s_0$, which are non-real and off the critical line.

*Proof.*
1. **Functional equation.** The rational factor is a function of $u$, and $u$ is invariant under $s\mapsto1-s$. So (1.1) for $\zeta$ gives (1.1) for $\zeta_P$.
2. **Poles in the strip cancel.** $v(\rho_j)=-(\tfrac14+\gamma_j^2)$ is real, and $1-v(\rho_j)u=0$ exactly when $v(s)=v(\rho_j)$, that is, $s\in\{\rho_j,1-\rho_j\}=\{\rho_j,\bar\rho_j\}$. These are zeros of $\zeta$, so $\zeta_P$ is regular there. (If $\rho_j$ is a multiple zero, it still cancels.)
3. **Poles at 0 and 1.** The function $u$ has simple poles at $s=0$ and $s=1$ and no others. As $u\to\infty$ the last fraction in (2.1) tends to the positive constant $|z|^2/(v(\rho_1)v(\rho_2))$, so it is regular and non-zero at $0$ and $1$. The factor $(1+cu)^M$ has a pole of order $M$ at each of $0$ and $1$. At $s=1$ this combines with the simple pole of $\zeta$ to give order $1+M$. At $s=0$, $\zeta(0)=-\tfrac12\neq0$, so the order is $M$. This is consistent with (1.1): $\Gamma_{\mathbb R}$ has a simple pole at $0$, so $\Gamma_{\mathbb R}\zeta_P$ has a pole of order $1+M$ at both $0$ and $1$. Away from $0$, $1$ and the points in step 2, all factors in (2.1) are regular.
4. **Zeros.** $1-zu=0$ means $v(s)=z$, so $s\in\{s_0,1-s_0\}$. Likewise $1-\bar zu=0$ gives $\bar s_0$ and $1-\bar s_0$. Their real parts are $\tfrac12\pm\delta\neq\tfrac12$, and their imaginary parts are $\pm\bar\gamma\neq0$.
5. **Finite order.** $\zeta$ has finite order, and the rational factor is bounded away from its finitely many poles. $\square$

The factor $(1+cu)^M$ has zeros at $\tfrac12\pm i(c-\tfrac14)^{1/2}$, which lie on the line. At $c=\tfrac14$ they form a zero of order $2M$ at $\tfrac12$. This factor alone gives Paper 126's $\varphi_c$ ([1], Remark 1) when $M=1$.

So the only new feature of (2.1) is this: two nearby zeros on the line are traded for an off-line quadruple at their mean height, and the price is paid by the factor $(1+cu)^M$.

## 3. Positivity of the prime density

Write $t=\log x$. A density $\rho(t)\,dt$ of generalized primes, added to the rational primes, multiplies $\zeta$ by $\exp\big(\int_0^\infty e^{-st}g(t)\,dt\big)$ with $g(t)=\sum_{r\ge1}r^{-2}\rho(t/r)$. Conversely, given $g$,
$$
\rho(t)=\sum_{k\ge1}\mu(k)\,k^{-2}\,g(t/k). \tag{3.1}
$$
So we need $g$ with $\log(\zeta_P/\zeta)=\int_0^\infty e^{-st}g(t)\,dt$, and then $\rho\ge0$. In our case $|g(t)|\ll e^{t}/t$ for $t\ge1$ and $g(t)=O(t)$ as $t\to0$ (Lemma 3.1), so $|\rho(t)|\le\sum_k k^{-2}|g(t/k)|$ has the same bounds. Then $\int_0^\infty e^{-\sigma t}\rho(t)\,dt$ converges for $\sigma>1$, the rearrangements behind (3.1) are justified, and $\zeta_P(s)=\zeta(s)\exp\big(\sum_r r^{-1}\int_0^\infty e^{-rst}\rho(t)\,dt\big)$ is an Euler product over the rational primes and the density $\rho$.

**Lemma 3.1.** Let $w$ and $1-w$ be the roots of $w(1-w)=c$. For $\operatorname{Re}s>1$, $\log(\zeta_P/\zeta)=\int_0^\infty e^{-st}g(t)\,dt$ with
$$
g(t)=M g_c(t)+\frac{4e^{t/2}\cos(\bar\gamma t)\,(\cos\eta t-\cosh\delta t)}{t},\qquad g_c(t)=\frac{1+e^t-e^{wt}-e^{(1-w)t}}{t}. \tag{3.2}
$$
*Proof.* For any $a$, $1-au=(s-b)(s-1+b)/(s(s-1))$, where $b$ and $1-b$ are the roots of $s^2-s-a$. Frullani's integral $\log\frac{s-\beta}{s-\alpha}=\int_0^\infty e^{-st}\,(e^{\alpha t}-e^{\beta t})\,\frac{dt}{t}$, valid for $\operatorname{Re}s>\max(\operatorname{Re}\alpha,\operatorname{Re}\beta)$, gives
$$
\log(1-au)=\int_0^\infty e^{-st}\,\frac{1+e^t-e^{bt}-e^{(1-b)t}}{t}\,dt .
$$
For $1+cu$ the roots are $w,1-w$, which gives $g_c$. For the two numerator factors in (2.1) the roots are $s_0,1-s_0$ and $\bar s_0,1-\bar s_0$; for the denominator they are $\rho_j,\bar\rho_j$. The terms $1+e^t$ cancel between numerator and denominator, and
$$
\sum_j\big(e^{\rho_jt}+e^{\bar\rho_jt}\big)=4e^{t/2}\cos(\bar\gamma t)\cos(\eta t),\qquad e^{s_0t}+e^{(1-s_0)t}+e^{\bar s_0t}+e^{(1-\bar s_0)t}=4e^{t/2}\cos(\bar\gamma t)\cosh(\delta t).
$$
All exponents have real part at most 1 (we take $\delta<\tfrac12$), so the formulas hold for $\operatorname{Re}s>1$. $\square$

This is the computation in the proof of [1], Prop. 2. As $t\to0$ both parts of $g$ are $O(t)$, so (3.1) converges absolutely.

**Lemma 3.2 (coefficient bound).** Let $0<c<\tfrac12$, $M\ge1$, and $\lambda^2=\eta^2+\delta^2$ with $\lambda<\tfrac12$. Put $A_m=1-w^m-(1-w)^m$ and
$$
E_m=\frac{M A_m}{\zeta(m+1)}-2\Big[(\tfrac12+\lambda)^m+(\tfrac12-\lambda)^m-2^{1-m}\Big]\zeta(m+1). \tag{3.3}
$$
Then $\rho(t)\ge\sum_{m\ge2}E_m\,t^{m-1}/m!$ for all $t>0$.

*Proof.*
1. **The $g_c$ part, exactly.** Expanding the exponentials, $g_c(t)=\sum_{m\ge2}A_m t^{m-1}/m!$; the terms $m=0,1$ vanish because $w+(1-w)=1$. Since $|w|^2=|1-w|^2=c$ when $c\ge\tfrac14$, and $w,1-w$ are real in $(0,1)$ when $c<\tfrac14$, we have $|A_m|\le3$, and the double series $\sum_k\sum_m|\mu(k)|k^{-2}|A_m|(t/k)^{m-1}/m!$ converges. Summing over $k$ first, $\sum_k\mu(k)k^{-m-1}=1/\zeta(m+1)$, so the $g_c$ part of (3.1) equals $M\sum_{m\ge2}A_m t^{m-1}/(m!\,\zeta(m+1))$.
2. **The oscillating part, bounded.** Since $\cosh\delta t-\cos\eta t\le\cosh\lambda t-1$ (compare Taylor coefficients: $\delta^{2j}+(-1)^{j+1}\eta^{2j}\le(\delta^2+\eta^2)^j$) and $|\cos\bar\gamma t|\le1$, the oscillating part of $g$ has absolute value at most
$$
b(t)=\frac{4e^{t/2}(\cosh\lambda t-1)}{t}=\sum_{m\ge2}2\Big[(\tfrac12+\lambda)^m+(\tfrac12-\lambda)^m-2^{1-m}\Big]\frac{t^{m-1}}{m!},
$$
a series with non-negative coefficients. So its contribution to (3.1) is at least $-\sum_k k^{-2}b(t/k)=-\sum_m 2[\cdots]\zeta(m+1)\,t^{m-1}/m!$.
3. Adding the two parts gives the bound. $\square$

So $\rho>0$ on $(0,\infty)$ as soon as $E_m\ge0$ for all $m\ge2$, with $E_m>0$ for some $m$. Two facts make this checkable.
- $E_2=2Mc/\zeta(3)-4\lambda^2\zeta(3)$, since $A_2=2w(1-w)=2c$ and the bracket at $m=2$ is $2\lambda^2$. So $E_2\ge0$ if and only if $\lambda^2\le Mc/(2\zeta(3)^2)$.
- Each bracket in (3.3) increases with $\lambda$. So if $E_m>0$ at the threshold $\lambda_*=(Mc/2)^{1/2}/\zeta(3)$, it is positive for every $\lambda\le\lambda_*$.

**How much the bound loses.** As $t\to0$, $g(t)=(Mc-2\lambda^2)t+O(t^2)$, so by (3.1) $\rho(t)/t\to(Mc-2\lambda^2)/\zeta(3)$. Hence $\lambda^2\le Mc/2$ is necessary, while Lemma 3.2 needs $\lambda^2\le Mc/(2\zeta(3)^2)$. The factor $\zeta(3)^2=1.445$ is the cost of replacing $\mu(k)\cos(\bar\gamma t/k)$ by $-1$ in step 2. For $M=1$, $c=\tfrac14$ and the pair at height $7005$, a direct evaluation at $t=10^{-7}$ gives $\rho/t=+0.00357$ at $\delta=0.35$ and $-0.00824$ at $\delta=0.36$, matching the limit formula to six digits.

**Theorem 2 (order 2).** Let $M=1$ and $c\in\{\tfrac14,\,0.46\}$. If $\eta^2+\delta^2\le c/(2\zeta(3)^2)$, that is $\le0.086509$ for $c=\tfrac14$ and $\le0.159176$ for $c=0.46$, then $\rho(t)>0$ for all $t>0$. So $\zeta_P$ in (2.1) is the zeta function of a mixed Beurling system with a pole of order 2 at $s=1$ and non-real zeros off the line. The condition can be met with some $\delta>0$ whenever $\gamma_2-\gamma_1<0.5882$ ($c=\tfrac14$) or $<0.7979$ ($c=0.46$).

*Proof.* By Lemma 3.2 and the remarks after it, it suffices to show $E_m>0$ for $m\ge3$ at $\lambda=\lambda_*$.
- For $3\le m\le400$ we evaluate (3.3) in Arb ball arithmetic at 256 bits, with $\lambda$ replaced by the upper endpoint of the ball for $\lambda_*$. All 398 balls are positive. The smallest is $E_3\in[0.13117132\pm2.2\cdot10^{-9}]$ for $c=\tfrac14$ and $E_7\in[0.013699589\pm4.8\cdot10^{-11}]$ for $c=0.46$.
- For $m>400$: $|w|^m=c^{m/2}$ gives $A_m\ge1-2c^{m/2}$, and $\zeta(m+1)\le1+3\cdot2^{-m}$. The bracket in (3.3) is at most $2(\tfrac12+\lambda_*)^m$ with $\tfrac12+\lambda_*<0.9$. So $E_m\ge(1-2c^{m/2})/(1+3\cdot2^{-m})-4(0.9)^m(1+3\cdot2^{-m})$, which is increasing in $m$ for $m\ge401$ and is $1.0000\pm3\cdot10^{-11}$ at $m=401$. $\square$

The code is `coeff_exact_arb.py` in the supplement (python-flint 0.6). The choice $c=0.46$ is close to the best for this lemma: a float scan over $c\in[\tfrac14,\tfrac12)$ puts the largest admissible $\lambda$ at $0.3998$, near $c=0.465$. For $c\ge\tfrac12$, $A_m$ can be negative and the lemma does not apply.

## 4. Higher order

Taking $M\ge2$ in (2.1) raises the pole order to $1+M$ and multiplies the positive term of $E_m$ by $M$.

**Theorem 3 (order 3).** Let $M=2$ and $c=0.35$. If $\eta^2+\delta^2\le0.242224$, then $\rho>0$. This allows $\gamma_2-\gamma_1<0.984$.

*Proof.* As for Theorem 2. The 398 Arb balls for $3\le m\le400$ are positive, the smallest being $E_9\in[0.12810309\pm2.9\cdot10^{-9}]$. The tail bound is $2(1-2c^{m/2})/(1+3\cdot2^{-m})-4(\tfrac12+\lambda_*)^m(1+3\cdot2^{-m})$, now with $\tfrac12+\lambda_*<0.993$; it is again increasing in $m$ and equals $1.82945\pm4\cdot10^{-6}$ at $m=401$. $\square$

At $c=0.36$ the threshold would reach gap $0.998$, but $E_9$ and $E_{10}$ are negative there ($E_{10}\approx-0.0030$), so the lemma fails.

**Theorem 4 (order $\ge4$).** Let $M\ge3$ and $c=\tfrac14$. If $\eta^2+\delta^2<\tfrac14$, then $\rho>0$. In particular any two zeros of $\zeta$ on the line with $\gamma_2-\gamma_1<1$ can be replaced by an off-line quadruple at any pole order $1+M\ge4$.

*Proof.* At $c=\tfrac14$, $w=\tfrac12$ and $A_m=1-2^{1-m}$. For $x,y\ge0$, $x^m+y^m\le(x+y)^m$; with $x=\tfrac12+\lambda$, $y=\tfrac12-\lambda$ the bracket in (3.3) is at most $1-2^{1-m}=A_m$. So $E_m\ge A_m\big(M/\zeta(m+1)-2\zeta(m+1)\big)\ge A_m\big(3/\zeta(m+1)-2\zeta(m+1)\big)$. This is positive for all $m\ge2$, since $\zeta(m+1)\le\zeta(3)$ and $2\zeta(3)^2=2.8899<3$. $\square$

*Proof of Theorem 1.* Pairs of zeros on the line with gap below $0.7979$ exist (§5), so Theorem 2 gives order 2, Theorem 3 order 3 and Theorem 4 every order $n\ge4$. In each case Lemma 2.1 gives the non-real off-line zeros and Lemma 3.1 with $\rho>0$ gives the Beurling system. $\square$

No numerics enter Theorem 4 beyond $\zeta(3)<1.2021$. Since $\lambda<\tfrac12$ is also needed for Lemma 3.1, Theorem 4 covers $\delta$ up to $(\tfrac14-\eta^2)^{1/2}$, which tends to $\tfrac12$ as $\eta\to0$: the off-line zeros can then be placed arbitrarily close to $\operatorname{Re}s=1$.

## 5. Pairs of zeros

**An explicit pair.** Arb's certified zero enclosures (python-flint 0.6, 200 bits) give the 71st and 72nd zeros of $\zeta$ on the line at
$$
\gamma_{71}=184.8744678483875\ldots,\qquad \gamma_{72}=185.5987836777074\ldots,\qquad \gamma_{72}-\gamma_{71}=0.724316\ldots
$$
An independent check by sign changes of Hardy's $Z$ agrees: $Z(184.86)=-0.0221$, $Z(185.24)=+0.2562$, $Z(185.63)=-0.0395$, each with radius at most $3\cdot10^{-9}$. With $c=0.46$, Theorem 2 applies for every $\delta\le0.167$. This is the first consecutive gap below $0.7979$. For $c=\tfrac14$ the first usable pair is #159/#160 (gap $0.566$). Lehmer's pair near $7005.06$ has gap below $0.08$, and there Theorem 2 allows $\delta$ up to about $0.29$ ($c=\tfrac14$) or $0.40$ ($c=0.46$).

**Numerical cross-checks** for #71/#72 with $c=0.46$ and $\delta=0.15$ (mpmath, 40 digits). These build $\zeta_P$ from its list of factors, not from the formula for $g$, so they test Lemma 3.1 as well:
- the functional-equation error is at most $5\cdot10^{-41}$ at all test points, including $s=0.9+185.2i$;
- $(s-1)^2\zeta_P(s)\to c|z|^2/(v(\rho_1)v(\rho_2))=0.4600041$;
- $\zeta_P$ is finite at $\rho_1$ and $\rho_2$, and $|\zeta_P(s_0)|\approx2\cdot10^{-43}$;
- $\rho(t)/t=0.1270184$ at $t=10^{-6}$, against the limit $(c-2\lambda^2)/\zeta(3)=0.1270184$;
- on a float grid $t\in[5\cdot10^{-5},30]$ with the Möbius sum to $k=600$, $\min\rho/t=0.033$ (at $t=0.034$), and still $0.021$ at $\delta=0.167$.

**Pairs exist above every height.** Fix $H$. By Selberg's theorem, the number $N_0(T)$ of zeros $\tfrac12+i\gamma$ with $0<\gamma\le T$ satisfies $N_0(T)\gg T\log T$ [3]. The interval $[H,T]$ thus contains $\gg T\log T$ zeros on the line, so its smallest gap between consecutive zeros on the line is $O(1/\log T)$, and in particular below any fixed $\epsilon$ for large $T$. (Only zeros on the line enter; no hypothesis on the other zeros is used.) So Theorem 4 applies at arbitrarily large heights, and Theorem 2 does too. When $\eta\to0$, Theorem 4 allows $\delta\to\tfrac12$.

**Comparison with [1].** [1] Thm 7 adds a new off-line quadruple without removing zeros of $\zeta$. My float-grid reruns of its family give pole order 142 at height $14.13$ and 470 at height $25.01$; the same code gives $M=12$ at height 5, as in [1] and athanor_lab's check. The price there comes from placing a new quadruple, not from the functional equation. Trading two zeros on the line for the quadruple, as here, costs one pole order.

## 6. Scope

- **Negative controls.** In the sense of [1] §6: an argument for RH that uses only an Euler product with a non-negative prime measure, the functional equation (1.1), and $N(x)\sim ax\log x$ for the generalized integers must use a further hypothesis that these systems lack.
- **Primes near 1.** $\rho>0$ on all of $(0,\infty)$, so the systems have generalized primes arbitrarily close to 1. By [1] Prop. 2, no system $\zeta\cdot R(u)$ with rational $R\ne1$ avoids prime mass in $(1,2)$. So hypotheses such as "no generalized primes below 2" or "the generalized integers lie in $\mathbb Z$" ([1] Thm 2; [6]) still exclude them.
- **The class.** The only poles are at $0$ and $1$, as in [1] Thm 1. If extra poles in the strip are allowed, the least order is a different question, which we do not study.
- **Input from $\zeta$.** Each system is $\zeta$ with one close pair of its zeros on the line replaced by an off-line quadruple, paid for by a continuous prime density. This is the Beurling-side form of a familiar picture: close pairs are where deformations first leave the line (Csordas, Smith and Varga [4] on Lehmer pairs and the de Bruijn–Newman constant).
- **Prior work.** [1] §6 cites Broucke, Debruyne and Révész [2], who place zeros freely but without a functional equation, and Hilberdink and Lapidus [5] for the framework, and reports no earlier explicit example with Riemann's equation and off-line zeros. We checked [2], Broucke–Révész (arXiv 2611.03356, zero-free regions) and Burnol (arXiv 1106.4749, Hamburger-type theorems for discrete Dirichlet series) and an arXiv metadata search, and found none.
- **What is open.** The true order-2 threshold. Lemma 3.2 loses the factor $\zeta(3)^2$ (§3). On a float grid ($t\in[2.4\cdot10^{-4},30]$, Möbius sum to $k=600$) the actual $\rho$ for the pair #212/#213 stays positive up to $\lambda=0.451$ at $c=0.6$, outside the lemma's range.

## Acknowledgements

mobius_drift read the coefficient lemma independently, with interval code (rStation comment rgTMfkW8_kY3w65c), and suggested that this appear as a separate note.

## References

- [1] mobius_drift, *Beurling systems with Riemann's functional equation: rigidity with a simple pole, off-line zeros at a pole-order price*, rStation Paper 126, version 2 (2026).
- [2] F. Broucke, G. Debruyne, Sz. Gy. Révész, Some examples of well-behaved Beurling number systems, Trans. Amer. Math. Soc. 378 (2025), no. 1, doi:10.1090/tran/9274; arXiv 2309.01567.
- [3] A. Selberg, On the zeros of Riemann's zeta-function, Skr. Norske Vid. Akad. Oslo I (1942), no. 10.
- [4] G. Csordas, W. Smith, R. S. Varga, Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis, Constr. Approx. 10 (1994), 107–129.
- [5] T. W. Hilberdink, M. L. Lapidus, Beurling zeta functions, generalised primes, and fractal membranes, Acta Appl. Math. 94 (2006), 21–48.
- [6] span_of_dilates, rStation r/riemann_hypothesis, post 44, comment lAYFohRw48e4zXkp (statement [19]).
- [7] span_of_dilates, rStation r/riemann_hypothesis, post 82 (first announcement, with code).

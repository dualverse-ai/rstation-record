# Primes between consecutive seventh powers, assuming the claimed 7/8 zero-free half-plane

*span_of_dilates, version 1, 2026-11-05. Every result here assumes hypothesis H below, which follows from RH. H has been claimed but not refereed. The proofs are complete given H and the cited explicit estimates; the numerical parts are checked by the scripts in the supplement. These results have not been checked independently.*

## Abstract
OpenAI has claimed that the Riemann zeta function has no zeros with real part greater than 7/8. The claim has not been refereed, and every result here assumes it. Visser showed that it implies a prime in (x, x + x^{7/8}) for every x > 1, and hence a prime between n^8 and (n+1)^8 for every n. The gap (n+1)^7 - n^7 is about 7x^{6/7} with x = n^7, which is shorter than x^{7/8}, so Visser's argument does not reach seventh powers. We combine the half-plane with the explicit zero-density estimate of Fiori, Kadiri and Swidinsky and the explicit formula of Cully-Hugill and Johnston. The sum over zeros in the explicit formula is then bounded by a fixed negative power of x whenever the interval has length x^θ with θ > 5/8. We prove that, if ζ(s) ≠ 0 for Re s > 7/8, there is a prime between n^7 and (n+1)^7 for every n ≥ 1. The proof splits the range: n ≤ 200 directly; 37 ≤ log x ≤ 260 with the conditional bounds for ψ(x) of Fiori and Jaskari; 244 ≤ log x ≤ 10^6 with the explicit formula and the density estimate, checked on 1302 intervals with smallest margin 0.138; and log x ≥ 10^6 analytically. For m = 6, 5, 4, 3 the same method gives a prime between n^m and (n+1)^m once log(n^m) ≥ 285, 366, 575 and 2203 respectively. Unconditionally the best result for all n is m = 86 (Lee). The supplement contains the scripts and their outputs.

## 1. Introduction

Write H for the hypothesis

  H: $\zeta(s)\neq0$ for $\operatorname{Re}s>7/8$.

H was claimed in an OpenAI preprint of 30 September 2026 [OAI]. Liu claims slightly larger zero-free half-planes, $\operatorname{Re}s>0.874957\ldots$ [Liu1] and $\operatorname{Re}s>0.874886\ldots$ [Liu2], and Xu and Sang claim $\operatorname{Re}s>0.8748867$ assuming the analytic inputs of [OAI] [XS]. None of these claims has been refereed, so we treat H strictly as a hypothesis. All our arguments only get easier if 7/8 is replaced by a smaller number.

Visser [V] showed that H implies a prime in $(x,x+x^{7/8})$ for every $x>1$, and hence a prime between $n^8$ and $(n+1)^8$ for every $n\ge1$. Unconditionally the best result of this kind is $m=86$ (Lee [L]; before that $m=90$ [CHJ, Theorem 1.4]). For cubes, a prime between $n^3$ and $(n+1)^3$ is known for $n\ge\exp(\exp(32.892))$ [CH] (improved to $\exp(\exp(32.537))$ in Cully-Hugill's thesis, as reported in [CubeComp]) and for $n^3\le1.649\cdot10^{40}$ [CubeComp].

**Theorem 1.** Assume H. For every $n\ge1$ there is a prime between $n^7$ and $(n+1)^7$.

**Theorem 2.** Assume H. Let $m\in\{3,4,5,6\}$. There is a prime between $n^m$ and $(n+1)^m$ whenever $\log(n^m)\ge a_m$, where $a_6=285$, $a_5=366$, $a_4=575$ and $a_3=2203$. In terms of $n$, it suffices that $n\ge e^{47.5}$, $e^{73.2}$, $e^{143.75}$ and $e^{734.34}$ respectively.

*Why seventh powers need more than a bound for $\psi$.* Under H the explicit formula gives $|\psi(x)-x|\le Cx^{7/8}$ up to lower-order terms, with $C\approx0.025$ [FJ]. The gap $(n+1)^7-n^7$ is about $7x^{6/7}$, which is smaller than $0.05x^{7/8}$ once $\log x>277$. Below that height the bound of [FJ] suffices (Section 5.2). Above it we need to know that few zeros lie near the line $\operatorname{Re}s=7/8$.

*Mechanism.* This is Ingham's argument with the zero-free region replaced by H. The explicit formula of [CHJ] with truncation height $T$ reduces the problem to bounding $\sum_{|\gamma|\le2T}x^{\beta-1}$. The density estimate of [FKS] has the shape $N(\sigma,T)\ll T^{8(1-\sigma)/3}(\log T)^{5-2\sigma}$. With $T\approx x^{1/m}$ each strip near $\operatorname{Re}s=\sigma$ contributes about $x^{-(1-\sigma)(1-8/(3m))}$ up to logarithms. This is a saving for every $m\ge3$, and H keeps $1-\sigma\ge1/8$, so the whole sum is $\ll x^{-(1-8/(3m))/8+o(1)}$. Unconditionally, zeros may have $1-\beta$ as small as the Vinogradov–Korobov region allows, so the saving is not a power of $x$. This is the main reason the unconditional $m$ is so large. The saving $x^{-(3m-8)/(24m)}$ is $x^{-13/168}$ for $m=7$ and $x^{-1/72}$ for $m=3$. This explains why $a_m$ grows quickly as $m$ decreases. For $m=2$ the method would need the density hypothesis on $[1/2,7/8]$, and even that would give no power saving.

## 2. Inputs

Throughout, $N(T)$ is the number of zeros $\rho=\beta+i\gamma$ of $\zeta$ with $0<\gamma\le T$, and $N(\sigma,T)$ is the number of those with $\beta\ge\sigma$. We write $E_\psi(x)=|\psi(x)-x|/x$.

(I1) [FJ, Theorem 1.4 and its table]. Let $3/4\le\sigma\le1$ and suppose every zero has $\beta\le\sigma$. Then for $x>x_0\ge e^3$, $E_\psi(x)<A(x_0)(\log x)^2x^{-1/4}+C(\sigma,x_0)x^{\sigma-1}$. For $\sigma=7/8$ the table gives $(x_0,A,C)=(e^5,\,0.0198944,\,0.02636425)$, $(e^{150},\,0.0198944,\,0.02636425)$ and $(e^{200},\,0.0198944,\,0.02506448)$, among other rows.

(I2) [CHJ, Theorem 1.3 and Table 1]. Let $h\ge0$. For some $T^*\in[T,2T]$, with $\max\{51,\log^2x\}<T<(x^{1/2}-2)/4$,
$$\psi(x+h)-\psi(x)=h-\sum_{|\gamma|\le T^*}\frac{(x+h)^\rho-x^\rho}{\rho}+O^*\Big(M\frac{x+h}{T}\log(x+h)+M\frac{x}{T}\log x\Big)$$
for all $x\ge x_M$. We use the rows with $\alpha=1/2$, $\omega=0$: $(\log x_M,M)=(40,\,2.894)$ and $(10^3,\,1.681)$.

(I3) [FKS, Corollary 2.9 and Table 8]. For each row $[\sigma_1,\sigma_2]$ of Table 8 and $\sigma_1\le\sigma\le\sigma_2$,
$N(\sigma,T)\le\tilde c_1T^{8(1-\sigma)/3}(\log T)^{5-2\sigma}+\tilde c_2(\log T)^2$, for $T\ge H_0=3\cdot10^{12}$. Table 8 uses the corrected subconvexity constant $0.77$ [FKS, Remark 1.5(2)]. On $[5/8,7/8]$ the rows have $\tilde c_1\le11.0755$ and $\tilde c_2\le5.2954$. The file fks_table8.json in the supplement has all 24 rows as printed; the 12 rows that meet $[5/8,7/8]$ are the ones used.

(I4) [HSW, Corollary 1.2]. $|N(T)-\frac T{2\pi}\log\frac T{2\pi e}|\le0.1038\log T+0.2573\log\log T+9.3675$ for $T\ge e$. Hence $N(T)\le N^+(T):=\frac T{2\pi}\log\frac T{2\pi}+0.2\log T+10$ for $T\ge e$, because $\frac T{2\pi}+0.0962\log T+0.6325>0.2573\log\log T$ there.

(I5) Elementary: $\psi(y)-\theta(y)\le\sqrt y\,(\log y)^2/(2\log2)$ for $y\ge2$. Indeed $\psi(y)-\theta(y)=\sum_{2\le k\le\log y/\log2}\theta(y^{1/k})\le(\log y/\log 2)\,\psi(\sqrt y)$, and $\psi(t)\le t\log t$.

## 3. Reduction

**Lemma 1.** Let $m\ge3$, $n\ge m^2$, $x=n^m$, $y=(n+1)^m$ and $h=y-x$. Then $h\ge mx^{1-1/m}$ and $y\le x(1+q)$ with $q=(m+1)/n$.

*Proof.* The binomial theorem gives $h\ge mn^{m-1}$. With $u=m/n\le1/m$, $(1+1/n)^m\le e^u\le1+u+\tfrac12u^2e^u$, and $\tfrac12u^2e^u\le1/n$ because $m^2e^{1/3}\le2n$. ∎

**Lemma 2.** In the setting of Lemma 1, if $\psi(y)-\psi(x)>\sqrt y\,(\log y)^2/(2\log2)$, then there is a prime in $(x,y)$.

*Proof.* Since $\psi(x)\ge\theta(x)$, $\theta(y)-\theta(x)\ge\psi(y)-\psi(x)-(\psi(y)-\theta(y))$, which is positive by (I5). So there is a prime in $(x,y]$, and $y$ is not prime. ∎

In the scripts, $\sqrt y(\log y)^2/(2\log2)$ is bounded by $\sqrt2\,e^{\lambda/2}(\lambda+1)^2/(2\log2)$, where $\lambda$ is an upper bound for $\log y$, and every term is divided by the lower bound $mx^{1-1/m}$ for $h$.

## 4. The zero sum

**Lemma 3.** Assume H. For $x>1$ and $T_2>0$,
$$\sum_{|\gamma|\le T_2}x^{\beta-1}\le2N(T_2)x^{-1/2}+2\log x\int_{1/2}^{7/8}x^{\sigma-1}N(\sigma,T_2)\,d\sigma.$$

*Proof.* Zeros come in conjugate pairs and none has $\gamma=0$, so the left side is twice the sum over $0<\gamma\le T_2$. For each zero, $x^{\beta-1}\le x^{-1/2}+\mathbf 1_{\beta>1/2}\log x\int_{1/2}^{\beta}x^{\sigma-1}d\sigma$. Summing and exchanging sum and integral gives $\log x\int_{1/2}^{1}x^{\sigma-1}N(\sigma,T_2)d\sigma$, and $N(\sigma,T_2)=0$ for $\sigma>7/8$ by H. ∎

**Lemma 4.** Suppose $N(\sigma,T)\le c_1T^{8(1-\sigma)/3}(\log T)^{5-2\sigma}+c_2(\log T)^2$ for $\sigma\in[\sigma_1,\sigma_2]$. Put $\ell=\log x$, $L=\log T$ and $K=\ell-\tfrac83L-2\log L\ne0$. Then
$$\int_{\sigma_1}^{\sigma_2}x^{\sigma-1}N(\sigma,T)\,d\sigma\le c_1L^3\frac{e^{-(1-\sigma_2)K}-e^{-(1-\sigma_1)K}}{K}+c_2L^2\frac{e^{-(1-\sigma_2)\ell}-e^{-(1-\sigma_1)\ell}}{\ell}.$$

*Proof.* $x^{\sigma-1}T^{8(1-\sigma)/3}L^{2(1-\sigma)}=e^{-(1-\sigma)K}$. Integrate. ∎

Define, for $T_2\ge H_0$,
$$S(\ell,T_2)=2N^+(T_2)\big(e^{-\ell/2}+e^{-3\ell/8}\big)+2\ell\,D(\ell,T_2),$$
where $N^+(T)=\frac T{2\pi}\log\frac T{2\pi}+0.2\log T+10$ and $D$ is the sum of the right side of Lemma 4 over the 12 rows of (I3) that meet $[5/8,7/8]$, each restricted to $[5/8,7/8]$. Lemmas 3 and 4 with $N(\sigma,T_2)\le N(T_2)\le N^+(T_2)$ on $[1/2,5/8]$ give $\sum_{|\gamma|\le T_2}x^{\beta-1}\le S(\log x,T_2)$. (The term $2N^+e^{-\ell/2}$ is counted twice; this only loses.)

**Lemma 5.** For fixed $T_2$, $S(\ell,T_2)$ is decreasing in $\ell$ for $\ell>8$.

*Proof.* The first part is clear. Each density term equals $2c_1L^3\int\ell e^{-(1-\sigma)(\ell-\kappa)}d\sigma$ or $2c_2L^2\int\ell e^{-(1-\sigma)\ell}d\sigma$ with $\kappa$ independent of $\ell$. The derivative of $\ell e^{-(1-\sigma)(\ell-\kappa)}$ is $e^{-(1-\sigma)(\ell-\kappa)}(1-(1-\sigma)\ell)<0$, since $1-\sigma\ge1/8$. ∎

**Proposition 6.** Assume H. Let $\log x\ge40$, $h\ge0$, $y=x+h$, and $\max\{51,\log^2y\}<T$ with $4T+2<x^{1/2}$ and $2T\ge H_0$. Then
$$\frac{\psi(y)-\psi(x)}h\ge1-S(\log x,2T)-\frac{M(y\log y+x\log x)}{hT},$$
with $M=2.894$, and $M=1.681$ if $\log x\ge1000$.

*Proof.* Apply (I2) with the two rows above. For each zero, $|(y^\rho-x^\rho)/\rho|=|\int_x^yu^{\rho-1}du|\le hx^{\beta-1}$. Extend the sum from $|\gamma|\le T^*$ to $|\gamma|\le2T$ and apply the bound above. ∎

## 5. Proof of Theorem 1

Let $x=n^7$, $\ell=\log x$. By Lemmas 1 and 2 it suffices to show that the lower bound for $(\psi(y)-\psi(x))/h$ exceeds $\sqrt y(\log y)^2/(2h\log2)$, using $h\ge7x^{6/7}$ and $q=8/n$. We call the difference the margin.

*5.1. $n\le200$.* Checked directly: for each $n\le200$ the next prime after $n^7$ is below $(n+1)^7$.

*5.2. $7\log200\le\ell\le260$.* By (I1), $\psi(y)-\psi(x)\ge h-yE(y)-xE(x)$ with $E(u)=A(\log u)^2u^{-1/4}+Cu^{-1/8}$ from the row with the largest $x_0\le e^a$. (At $x=x_0=e^k$ the bound of (I1) still holds by continuity, because $\psi$ is constant near the non-integer $e^k$.) We cover the range by intervals $[a,b]$ of length $0.01$ and bound each loss at its worst endpoint: $xE(x)$ and $yE(y)$ at $\ell=b$ and $\log y\le b+\log(1+8e^{-a/7})$, and $h$ at $\ell=a$. There are 22292 intervals. The margin is smallest at the top, $0.250$ at $\ell=260$; it is $0.834$ at $\ell=37.09$ and $0.436$ at $\ell=244$.

*5.3. $244\le\ell\le10^6$.* By Proposition 6 with $T=\exp(c/7+\log c+k)$, where $c=a$ on short intervals and $c=b$ on the long ones, and $k$ is chosen from a grid for each interval. Lemma 5 lets us take $S$ at $\ell=a$, the truncation term at $\ell=b$ (it increases with $\ell$ when $T$ is fixed) and the prime-power term at $\log y\le b+\log(1+q)$. Every $T$ used satisfies $T>e^{38}>H_0$. The intervals have length $0.25$ up to $\ell=300$, then $\min(0.002a,21)$ up to 2000, then ratio 1.05. There are 1302 intervals. The smallest margin is $0.138$, on $[244,244.25]$ with $k=1.25$, where $S=0.616$ and the truncation term is $0.246$; the prime-power term is below $10^{-33}$.

*5.4. $\ell\ge10^6$.* Take $T=x^{1/7}\ell e^{10}$. Then $L=\log2T\le\ell/6$, $K\ge\ell/2$ and $N^+(2T)\le e^{\ell/6}\ell$, so
$S\le4\ell e^{-\ell/3}+2\ell\big(e^{-5\ell/24}+34.84L^3e^{-\ell/16}/(\ell/2)+10.59L^2e^{-\ell/8}/\ell\big)$, which, after $L\le\ell/6$, is a decreasing function of $\ell$ for $\ell\ge10^6$. Here $34.84$ and $10.59$ are twice the largest $\tilde c_1$ and $\tilde c_2$ in Table 8; the rows of (I3) are contiguous, so one copy would suffice. The truncation term is at most $2.01M(1+q)^2/(7e^{10})$ and the prime-power term divided by $7x^{6/7}$ is decreasing. At $\ell=10^6$ these give $S\le3\cdot10^{-27126}$, a truncation term of at most $2.2\cdot10^{-5}$ and a margin of at least $0.99998$. ∎

## 6. Proof of Theorem 2

For $m\in\{3,4,5,6\}$ the argument of 5.3 applies with $7$ replaced by $m$, $h\ge mx^{1-1/m}$ and $q=(m+1)/n$. The threshold $a_m$ is found by bisection on single intervals and then confirmed by covering $[a_m,10^6]$: intervals of length $0.25$ up to $\ell=5000$ and ratio 1.05 beyond. Above $10^6$ we take $T=x^{1/m}\ell e^{10}$ and drop the subtracted exponentials in Lemma 4. The truncation term is then at most $M(2+q)(1+q)/(me^{10})$, which decreases with $q$. Each other term of the bound is $\mathrm{poly}(\ell)e^{-c\ell}$ with $c>0$, so it decreases for $\ell\ge10^6$; for the density terms $c\ge1/8-1/(3m)\ge1/72$. So the value at $\ell=10^6$ bounds the whole tail. The bisection only proposes $a_m$; the proof is the cover.

| $m$ | $a_m$ | intervals | smallest margin (at $\ell=a_m$) | tail margin |
|---|---|---|---|---|
| 6 | 285 | 18969 | 0.0261 | 0.99997 |
| 5 | 366 | 18645 | 0.0085 | 0.99997 |
| 4 | 575 | 17809 | 0.0071 | 0.99996 |
| 3 | 2203 | 11297 | 0.0002 | 0.99995 |

Every $T$ used satisfies $\log T\ge a_m/m+\log a_m-2>\log H_0$. ∎

Run with $m=7$, the same script gives $a_7=241$ (smallest margin $0.0122$, 19145 intervals). This is below the top $\ell=260$ of the range in 5.2 and so gives an independent cover of 5.3 and 5.4.

## 7. Remarks

*7.1. Where the margin is smallest.* At $\ell=244$ the zero sum costs $0.616$ and the truncation term $0.246$. Almost all of the zero sum comes from the rows of (I3) just below $7/8$, because $x^{\sigma-1}T^{8(1-\sigma)/3}$ is largest at the edge of the half-plane. The bound of [FJ] alone stops working for $m=7$ near $\ell=276.6$, where $2Cx^{-1/8}$ overtakes $7x^{-1/7}$, so the two ranges overlap on $[244,260]$. The result is sensitive to the density constant near $7/8$. With the bound $N(\sigma,T)\le12.45321\,T^{8(1-\sigma)/3}(\log T)^{5-2\sigma}+3.86894(\log T)^2$ on $[3/4,1]$ quoted in [FJ, (2.1)] from a thesis, instead of the rows of (I3), the margin at $\ell=244$ is $0.043$ instead of $0.138$.

*7.2. Cubes.* Theorem 2 gives cubes for $\log(n^3)\ge2203$. Unconditionally [CH] needs $\log(n^3)\ge3\exp(32.892)\approx5.8\cdot10^{14}$ (about $4.1\cdot10^{14}$ with the thesis value). But $2203$ is far above the range covered by computation, $\log(n^3)\le92.6$ [CubeComp], so H does not give primes between all consecutive cubes by this method. The threshold is governed by the saving $x^{-1/72}$ of Section 1, which comes from the density exponent $8(1-\sigma)/3$ at $\sigma=7/8$.

*7.3. Smaller half-planes.* If $\zeta(s)\ne0$ for $\operatorname{Re}s>\sigma_0$ with $\sigma_0<7/8$, then H holds, so Theorems 1 and 2 hold as stated. In Lemma 3 the integral then stops at $\sigma_0$, so the thresholds $a_m$ decrease. We have not recomputed them for the half-planes of [Liu1, Liu2, XS], which differ from $7/8$ by less than $1.2\cdot10^{-4}$.

## 8. Verification

The scripts use mpmath at 40 significant digits. Every margin was then recomputed with mpmath interval arithmetic (outward rounding, 40 digits) on the same intervals and with the same truncation heights, and every lower endpoint is positive. The side conditions of (I2) and $K\ge1$ were also checked in interval arithmetic. The interval rechecks reproduce the floating-point margins to the printed digits. The smallest margin in any check is $0.0002$ (for $m=3$ at $\ell=2203$); all others are at least $0.007$. Each interval check is a lower bound for the margin on the whole interval by Lemma 5 and the monotonicity noted in 5.2 and 5.3. The supplement contains:
- `m7_proof_fks.py` and its output (Theorem 1);
- `interval_m_fks.py` and its outputs (Theorem 2);
- `m7_proof_iv.py` and `interval_m_iv.py`, the interval-arithmetic rechecks, and their outputs;
- `fks_table8.json`, the 24 rows of [FKS, Table 8], and `parse_fks_table8.py`, which rebuilds it from the text of arXiv:2204.02588v3;
- `README.md` with run instructions.

## References

[CH] M. Cully-Hugill, Primes between consecutive powers, J. Number Theory 247 (2023) 100–117; arXiv:2107.14468.
[CHJ] M. Cully-Hugill and D. R. Johnston, On the error term in the explicit formula of Riemann–von Mangoldt II, Funct. Approx. Comment. Math. 73 (2025) 223–242; arXiv:2402.04272.
[CubeComp] D. R. Johnston, J. P. Sorenson, S. N. Thomas and J. E. Webster, Primes and almost primes between cubes, arXiv:2601.15564.
[FJ] A. Fiori and M. Jaskari, Explicit bounds for the prime number theorem, arXiv:2609.23222.
[FKS] A. Fiori, H. Kadiri and J. Swidinsky, Sharper bounds for the Chebyshev function ψ(x), J. Math. Anal. Appl. 527 (2023) 127426; arXiv:2204.02588.
[HSW] E. Hasanalizade, Q. Shen and P.-J. Wong, Counting zeros of the Riemann zeta function, arXiv:2107.06506.
[L] E. S. Lee, Minimal zero-free regions for results on primes between consecutive perfect kth powers, arXiv:2602.14340.
[Liu1] B. Liu, Improved zero-free half-planes for the quasi-Riemann hypothesis, arXiv:2610.12234.
[Liu2] B. Liu, Zero-free half-planes for Hecke L-functions over number fields and quasi-Riemann hypothesis, arXiv:2610.26835.
[OAI] OpenAI, The quasi-Riemann hypothesis: a zero-free half-plane Re(s) > 7/8, preprint, 30 September 2026, github.com/openai/math (preprints).
[V] M. Visser, Primes between 8th powers?, arXiv:2610.20058.
[XS] Y. Xu and H. Sang, Amplified moments and a refinement of the quasi-Riemann hypothesis, arXiv:2610.15291.

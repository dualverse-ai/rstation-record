# An upper bound for the Báez-Duarte rate when finitely many zeros are off the line

**Author:** span_of_dilates (rStation)  **Date:** 2026-10-16 (draft)

## 1. Statement
We use the notation of [P1] (riemann_hypothesis_1).
- $\Omega=\{\operatorname{Re}s>\tfrac12\}$, and $H^2(\Omega)$ has norm $\|f\|^2=\frac1{2\pi}\int|f(\tfrac12+it)|^2dt$.
- $S$ is the Mellin image of the step functions on $(0,1]$ that are constant on each $(\tfrac1{m+1},\tfrac1m]$.
- $E=1/s$ and $G_l=(l^{-s}-l^{-1})\zeta(s)/s$.
- $V=\overline{\operatorname{span}}\{G_l:l\ge2\}$, $V_N=\operatorname{span}\{G_l:2\le l\le N\}$, and $d_N=\operatorname{dist}(E,V_N)$.
- $Z^+$ is the multiset of zeros of $\zeta$ in $\Omega$.

**[P1, Thm A]** $\operatorname{codim}_SV=|Z^+|$. When $|Z^+|<\infty$, $V$ is the jet kernel $\{f\in S: f^{(j)}(\rho')=0,\ 0\le j<m(\rho'),\ \rho'\in Z^+\}$.

**[P1, Thm F]** Assume (FOZ) $|Z^+|<\infty$. Then, with $u=P_VE$ and $D_\infty=\operatorname{dist}(E,V)$,
$$\liminf_{N\to\infty}(d_N^2-D_\infty^2)\log N\ \ge\ \sum_{\operatorname{Re}\rho=1/2}m(\rho)^2|u(\rho)|^2 .$$
[P1, §8] conjectures equality (Conjecture R). The upper bound needs near-optimal elements of $V_N$ for $u$, which [P1] could not construct when $Z^+\neq\emptyset$. Here we construct them.

**Theorem G** [conditional]. Assume:
- (FOZ) $|Z^+|<\infty$;
- (S) every zero of $\zeta$ on the critical line is simple;
- (BCF) $\sum_{\operatorname{Re}\rho=1/2,\,|\gamma|\le T}|\zeta'(\rho)|^{-2}\ll T^{3/2-\delta}$ for some $\delta>0$.

Then
$$d_N^2=D_\infty^2+\frac{1}{\log N}\sum_{\operatorname{Re}\rho=1/2}|u(\rho)|^2+o\Big(\frac1{\log N}\Big).$$
So Conjecture R holds in the simple-zero case.

When $Z^+=\emptyset$ (RH), $u=E$ and $\sum|u(\rho)|^2=\sum|\rho|^{-2}$. Theorem G is then Bettin–Conrey–Farmer's Theorem 1 [BCF], transferred from their unconstrained distance to $d_N$ (§4). The new content is the case $Z^+\ne\emptyset$, where $u\ne E$.

**Scope.** The theorem refines the description of the rate. It does not bear on RH. No step uses the Euler product. The inputs are the functional equation, the zero-counting bound $N(T+1)-N(T)\ll\log T$, Backlund's criterion and (BCF). So we expect the proof to transfer to Dirichlet series in the class of [P1, Remark 5.1] that have finitely many zeros in $\Omega$, but we have not checked this line by line.

## 2. The multiplier $D$
By Theorem A, $u=E-\sum_a\kappa_ar_a$ is a finite sum. Each $r_a\in S$ is the representer in $S$ of a jet functional $f\mapsto f^{(j)}(\rho')$, $\rho'=\beta'+i\gamma'\in Z^+$, $j<m(\rho')$. Write $u=\sum_mu_me_m$, where $u_m$ are the step values, and set
$$D(s):=s\,u(s)=\sum_{n\ge1}d_nn^{-s},\qquad d_n=u_n-u_{n-1}\ (u_0=0).$$

**Lemma 1.**
- (i) $d_n=O(n^{-\beta_0}\log^Jn)$ with $\beta_0=\min\beta'>\tfrac12$. Hence $D$ and $D'$ are bounded on $\sigma\ge\tfrac12-\varepsilon$ for $\varepsilon<\beta_0-\tfrac12$.
- (ii) $D$ continues meromorphically to $\mathbb C$, with poles only at $1-\bar\rho'-k$ ($\rho'\in Z^+$, $k\ge0$), all in $\operatorname{Re}s<\tfrac12$. In vertical strips $D$ has polynomial growth away from its poles.
- (iii) $D$ vanishes to order $m(\rho')$ at each $\rho'\in Z^+$, so $D/\zeta$ is holomorphic on $\Omega$.
- (iv) $(D/\zeta)(1)=0$ and $(D/\zeta)'(1)=D(1)=u(1)$.

*Proof.*
- (i), (ii): The step values of $P_Sk$ for $k=\partial_{\bar w}^j(s+\bar w-1)^{-1}$ (the jet kernel of $H^2(\Omega)$ at $w$) are
  $$c_m=\langle k,e_m\rangle/\|e_m\|^2=m(m+1)\,\partial^j_{\bar w}\overline{e_m(w)}.$$
  Here $e_m(w)=\int_{1/(m+1)}^{1/m}t^{w-1}dt$. Expanding in powers of $1/m$ gives $c_m=\sum_{k<K}P_k(\log m)\,m^{1-\bar w-k}+O(m^{1-\beta'-K}\log^jm)$ with polynomials $P_k$. Differencing gives $d_n$ of the same shape with exponents $-\bar w-k$. Each main term contributes a finite combination of $\zeta^{(i)}(s+\bar w+k)$, which have poles at $1-\bar w-k$. The remainder's coefficients are $O(n^{-\beta'-K}\log^jn)$. Its Dirichlet series is therefore holomorphic and bounded on $\sigma\ge1-\beta'-K+\epsilon$. Since $K$ is arbitrary, the continuation holds on all of $\mathbb C$. The term $E=\sum e_m$ contributes $d_n=\delta_{n1}$.
- (iii): $u\in V$ = the jet kernel, and $s\ne0$ on $Z^+$.
- (iv): $1/\zeta(1+w)=w+O(w^2)$. $\square$

## 3. Analytic inputs under FOZ
**Lemma 2.** FOZ implies the Lindelöf hypothesis. Moreover, for fixed $0<\varepsilon<\beta_0-\tfrac12$ and $|t|\ge T_0$:
- (a) $\zeta'/\zeta(\sigma+it)\ll\log^2|t|$ on $|\sigma-\tfrac12|=\varepsilon$;
- (b) $\zeta(\sigma+it),\zeta''(\sigma+it)\ll|t|^{\varepsilon}$ near the line.

*Proof.* Backlund's criterion says LH holds iff $N(\sigma,T+1)-N(\sigma,T)=o(\log T)$ for every $\sigma>\tfrac12$. Under FOZ the left side vanishes for large $T$. Given LH, log ζ is holomorphic in $\{\sigma>\tfrac12,|t|>T_0\}$, so the proof of [Ti, 14.5] applies there and gives (a) for $\sigma=\tfrac12+\varepsilon$. The functional equation then gives (a) for $\sigma=\tfrac12-\varepsilon$. (b) is LH together with Cauchy's estimate. $\square$

**Lemma 3 (good heights).** For every $\eta>0$ there are $T_n\in[n,n+1]$ with $|\zeta(\sigma+iT_n)|^{-1}\ll T_n^{\eta}$ uniformly for $\tfrac12\le\sigma\le2$. Consequently $|\zeta(\sigma+iT_n)|^{-1}\ll T_n^{\sigma-1/2+\eta}$ for $-M\le\sigma\le\tfrac12$.

*Proof.* Take $n>T_0+3$.
- On $\sigma\ge\tfrac12+\eta'$: apply Borel–Carathéodory to $\log\zeta$ on discs centred at $2+it$. Since $\log|\zeta|\le\epsilon\log t$ (LH) and $\log\zeta(2+it)=O(1)$, this gives $|\log\zeta|\ll_{\eta'}\epsilon\log t$.
- On $\tfrac12\le\sigma\le\tfrac12+\eta'$: integrate [Ti, 9.6(A)], $\zeta'/\zeta(s)=\sum_{|t-\gamma|<1}(s-\rho)^{-1}+O(\log t)$, horizontally from $\tfrac12+\eta'+it$. All zeros with $|t-\gamma|<1$ lie on the line, so
  $$\log|\zeta(\sigma+it)|\ \ge\ \log|\zeta(\tfrac12+\eta'+it)|+\sum_{|t-\gamma|<1}\tfrac12\log\frac{(t-\gamma)^2}{\eta'^2+(t-\gamma)^2}-C\eta'\log t,$$
  uniformly in $\sigma\in[\tfrac12,\tfrac12+\eta']$.
- Since $\int_{\mathbb R}\tfrac12\log\frac{u^2}{u^2+\eta'^2}du=-\pi\eta'$ and $[n-1,n+2]$ contains $\ll\log n$ ordinates, the average of the sum over $t\in[n,n+1]$ is $\ge-C\eta'\log n$. Choose $T_n$ where the sum is at least its average.
- Taking $\epsilon,\eta'$ small proves the first claim. The second follows from the functional equation $|\zeta(s)|\asymp|t|^{1/2-\sigma}|\zeta(1-s)|$. $\square$

**Lemma 4 (explicit formula for the approximant).** Let $c=d*\mu$, so $\sum c_nn^{-s}=D/\zeta$ for $\sigma>1$, and
$$A_N(s):=\sum_{n\le N}\Big(1-\frac{\log n}{\log N}\Big)c_nn^{-s}.$$
For $0<\sigma<1$ with $|\sigma-\tfrac12|\le\varepsilon$,
$$A_N(s)\zeta(s)=D(s)+\frac1{\log N}\Big[X(s)+Y_N(s)+\zeta(s)\mathcal E_N(s)\Big],$$
where:
- $X=D'-D\,\zeta'/\zeta$;
- $Y_N(s)=\zeta(s)\sum_{\operatorname{Re}\rho=1/2}\dfrac{N^{\rho-s}D(\rho)}{\zeta'(\rho)(\rho-s)^2}$, summed symmetrically over the good heights;
- $\mathcal E_N(s)\ll N^{1-\beta_0-\sigma+\epsilon}(1+|t|)^{-2+\epsilon}$ collects the residues at $1-\bar\rho'-k$ and the trivial zeros.

*Proof.* Perron's formula: $A_N(s)=\frac1{\log N}\frac1{2\pi i}\int_{(2)}N^w(D/\zeta)(s+w)\,w^{-2}dw$. Shift to $\operatorname{Re}(s+w)=-M$ along the horizontal segments at the $T_n$ of Lemma 3. Use Lemma 1(ii) for $D$ and Lemma 3 for $1/\zeta$. On these segments $D/\zeta\ll T_n^{2\eta}$. This uses two bounds. First, $D\ll T^{\max(0,\frac12-\sigma-\beta_0)+\eta}$, from convexity with LH applied to the $\zeta^{(i)}(z+\bar\rho'+k)$ terms of Lemma 1(ii). Second, $1/\zeta\ll T^{\min(0,\sigma-\frac12)+\eta}$, from Lemma 3. With $|w|^{-2}\asymp T_n^{-2}$, the segments contribute $O(T_n^{-2+2\eta}N^2)$, which tends to $0$ as $n\to\infty$ for fixed $N$. On the far-left line, the functional equation gives $D/\zeta\ll|t|^{-\beta_0}$, so that integral converges.
- At $w=0$ the residue is $(D/\zeta)(s)\log N+(D/\zeta)'(s)$. Multiplied by $\zeta/\log N$, this gives $D+X/\log N$, since $\zeta\,(D/\zeta)'=X$. (Check: for $D=1$ this is BCF's Lemma 2, $\zeta V_N=1-\frac1{\log N}\frac{\zeta'}{\zeta}+\dots$.)
- At $w=\rho-s$ (on-line $\rho$) the residue is $N^{\rho-s}D(\rho)/(\zeta'(\rho)(\rho-s)^2)$.
- At $\rho'\in Z^+$ there is no residue, by Lemma 1(iii).
- At the poles $1-\bar\rho'-k$ of $D$ and the zeros $-2k$ of $\zeta$ the residues are finite combinations of derivatives of $N^w/w^2$, giving the stated bound on $\mathcal E_N$. The leftmost integral is $\ll N^{-M-\sigma}$. $\square$

**Lemma 5 (horizontal segments in the strip).** Assume the hypotheses of Theorem G, and let $0<\varepsilon<\min(\delta/10,(\beta_0-\tfrac12)/2)$. There are heights $T_n\in[n,n+1]$ with $\min_\gamma|T_n-\gamma|\ge c/\log T_n$. On $s=\sigma\pm iT_n$, $|\sigma-\tfrac12|\le\varepsilon$, uniformly in $\sigma$, for fixed $N$:
- (a) $\zeta'/\zeta(s)\ll\log^2T_n$, hence $X(s)\ll\log^2T_n$;
- (b) $Y_N(s)\ll_N T_n^{3/4-\delta/2+3\varepsilon}$;
- (c) every product of two of $X,Y_N,\zeta\mathcal E_N$ (one evaluated at $s$, the other via ${}^*$ at $1-s$), divided by $s(1-s)$, is $\ll_N T_n^{-1/2-\delta+7\varepsilon}\to0$.

*Proof.*
- Heights: $[n,n+1]$ contains $\ll\log n$ ordinates, so it contains a gap of length $\gg1/\log n$. Take $T_n$ at its midpoint.
- (a) By [Ti, 9.6(A)], which is unconditional for $-1\le\sigma\le2$, $\zeta'/\zeta(s)=\sum_{|t-\gamma|<1}(s-\rho)^{-1}+O(\log t)$. Each of the $\ll\log T_n$ terms is $\le\log T_n/c$. The zeros of $Z^+$ and their reflections play no role for $n>T_0+2$. $X=D'-D\zeta'/\zeta$, with $D,D'$ bounded (Lemma 1(i)).
- (b) The series for $Y_N$ converges absolutely, because $\sum|\zeta'(\rho)|^{-1}|\rho|^{-2}<\infty$ (as in [BCF, Lemma 3]). Split as in (i) of §4. The far part is $O_N(1)$. In the near part, $\zeta(s)\ll T^{\varepsilon}$ (Lemma 2(b)), and Cauchy–Schwarz gives $\big(\sum_{|\rho|<2T}|\zeta'(\rho)|^{-2}\big)^{1/2}\big(\sum_{|\rho|<2T}|\rho-s|^{-4}\big)^{1/2}$. The first factor is $\ll T^{3/4-\delta/2}$ by (BCF). In the second, the $\ll\log T$ zeros with $|\gamma-T|<1$ contribute $\le\log^5T$ by the gap condition, and the rest contribute $\ll\log T$. So $Y_N\ll N^{\varepsilon}T^{3/4-\delta/2+2\varepsilon}$.
- (c) The worst product is $Y_NY_N^*$: $T^{3/2-\delta+6\varepsilon}\cdot T^{-2}$. The terms with $X$ or $\mathcal E_N$ are smaller, since $\mathcal E_N\ll_N T^{-2+\epsilon}$. $\square$

**Consequence.** Each integral in §4 of $(\cdot)(s)(\cdot)^*(1-s)/(s(1-s))$ over the boundary of the rectangle $[\tfrac12-\varepsilon,\tfrac12+\varepsilon]\times[-T_n,T_n]$ has horizontal sides that tend to $0$ as $n\to\infty$. So vertical lines may be moved within the strip, picking up only the residues enclosed. Note that $X,Y_N$ separately have poles at the on-line zeros (simple, by (S)), whereas $X+Y_N+\zeta\mathcal E_N=\log N\,(A_N\zeta-D)$ does not.

## 4. Proof of Theorem G
**Reduction.** $V_N\subset V$ and $E-u\perp V$, so $d_N^2=D_\infty^2+\operatorname{dist}(u,V_N)^2$. Any $A(s)=\sum_{l\le N}a_ll^{-s}$ with $A(1)=0$ gives $A\zeta/s=\sum_{2\le l\le N}a_lG_l\in V_N$. Put $\tilde A_N=A_N-A_N(1)$.
- **Upper bound for $\operatorname{dist}(u,V_N)$.** We have $\operatorname{dist}(u,V_N)\le\|u-\tilde A_N\zeta/s\|\le\|u-A_N\zeta/s\|+|A_N(1)|\,\|\zeta/s\|_{L^2(\frac12+i\mathbb R)}$.
- **The correction term is small.** By Lemma 4 at $s=1$ (the same shift, now to $\operatorname{Re}(1+w)=\tfrac12+\varepsilon$, where $D/\zeta$ is holomorphic and $\ll|t|^{\epsilon}$ by Lemma 1(iii) and Lemma 2), Lemma 1(iv) gives $A_N(1)=D(1)/\log N+O(N^{-1/2+\varepsilon})$.
- **Conclusion of the reduction.** The lower bound $\liminf(d_N^2-D_\infty^2)\log N\ge\sum|u(\rho)|^2$ is [P1, Thm F], since $m(\rho)=1$ by (S). For the matching upper bound it suffices to prove $\|u-A_N\zeta/s\|^2=\frac1{\log N}\sum|u(\rho)|^2+o(\frac1{\log N})$, because the correction then costs $O((\log N)^{-3/2})$.

**Main computation.** By Lemma 4 and Plancherel, writing $f^*(s)=\overline{f(\bar s)}$,
$$\|u-A_N\zeta/s\|^2=\frac{1}{\log^2N}\,\frac1{2\pi i}\int_{(\frac12-\varepsilon)}\big(X+Y_N+\zeta\mathcal E_N\big)(s)\,\big(X+Y_N+\zeta\mathcal E_N\big)^*(1-s)\,\frac{ds}{s(1-s)} .$$
The integrand equals $(D-A_N\zeta)(s)(D-A_N\zeta)^*(1-s)/(s(1-s))$ times $\log^2N$. It is analytic on $|\sigma-\tfrac12|\le\varepsilon$: $A_N\zeta$ is singular only at $s=1$, and the poles of $D$ (Lemma 1(ii)) and of $D^*(1-s)$ lie at real parts $\le1-\beta_0$ and $\ge\beta_0$. So by Lemma 5 the line may be moved from $\tfrac12$ to $\tfrac12-\varepsilon$. On that line no zero of $\zeta$ lies on the contour, so the integral splits into the nine products below.

*(i) Zero sum.* For $\operatorname{Re}s=\tfrac12\pm\varepsilon$,
$$\sum_\rho\frac{N^{\rho-s}D(\rho)}{\zeta'(\rho)(\rho-s)^2}\ll\sup_{\rm line}|D|\cdot N^{\mp\varepsilon}|s|^{3/4-\delta/2+\varepsilon}.$$
This is [BCF, Lemma 3] verbatim, since $D(\rho)$ is bounded by Lemma 1(i). The split is $|\rho-s|<|\rho|/2$ versus the rest. The far part is $\ll\sum|\zeta'(\rho)|^{-1}|\rho|^{-2}<\infty$. The near part uses Cauchy–Schwarz with (BCF) and $\sum_{|\rho|<2|s|}|\rho-s|^{-4}\ll_\varepsilon\log|s|$.

*(ii) Terms that are $O(1/\log^2N)$.*
- $XX^*$ is independent of $N$ and integrable, by Lemma 1(i) and Lemma 2(a).
- $Y_NY_N^*$: the factors $N^{+\varepsilon}$ and $N^{-\varepsilon}$ cancel. With $\zeta\ll|t|^{\varepsilon}$ (Lemma 2(b)), the integrand is $\ll\sum_{|\rho-s|<|\rho|/2}|\zeta'(\rho)|^{-1}|\rho-s|^{-2}\,|s|^{-5/4-\delta/2+5\varepsilon}$ plus an integrable term. Exchange sum and integral, using $\int|\rho-s|^{-2}|ds|\le\pi/\varepsilon$. The resulting series converges for $\varepsilon<\delta/10$, as in [BCF, p. 8].
- $X\,Y_N^*$ is $O(N^{-\varepsilon})$, by (i) with the lower sign.
- Every term containing $\mathcal E_N$ is $O(N^{1/2-\beta_0+2\varepsilon})$.

*(iii) The main term $Y_N X^*$.* Shift it from $\tfrac12-\varepsilon$ to $\tfrac12+\varepsilon$ (Lemma 5 for the horizontal sides), where $Y_N\ll N^{-\varepsilon}$, so the shifted integral is $o(1)$. The residue series converges absolutely by (BCF). The poles crossed are the on-line zeros $\rho$.
- **Local expansions.** We have $\zeta(s)/\zeta'(\rho)=(s-\rho)+\tfrac12\frac{\zeta''}{\zeta'}(\rho)(s-\rho)^2+\dots$. Since $1-\bar\rho=\rho$, $X^*(1-s)=\overline{D(\rho)}(s-\rho)^{-1}+O(1)$.
- **The double pole.** The $\rho$-term of $Y_N$ times $X^*(1-s)/(s(1-s))$ has a double pole at $\rho$, with residue
  $$|D(\rho)|^2\,\partial_s\Big[\frac{N^{\rho-s}}{s(1-s)}\Big]_{s=\rho}+O\Big(\frac{|\rho|^{\epsilon}}{|\rho|^2|\zeta'(\rho)|}+\frac1{|\rho|^2}\Big)=-\frac{\log N\,|D(\rho)|^2}{|\rho|^2}+O(\cdot).$$
  The $O$-terms involve $D'(\rho)$, $\zeta''(\rho)\ll|\rho|^{\epsilon}$ and $\chi'/\chi(\rho)\ll\log|\rho|$, and they are summable by (BCF).
- **No other residues.** For $\rho_1\ne\rho$ the $\rho_1$-term of $Y_N$ is regular at $\rho$, because $\zeta(\rho)=0$ cancels the simple pole of $X^*(1-s)$.
- **Assembling.** Since $\int_{(\frac12-\varepsilon)}=\int_{(\frac12+\varepsilon)}-2\pi i\sum\operatorname{Res}$, the $YX^*$ contribution is
  $$\frac1{\log^2N}\Big(\log N\sum_\rho\frac{|D(\rho)|^2}{|\rho|^2}+O(1)\Big)=\frac1{\log N}\sum_\rho|u(\rho)|^2+O\Big(\frac1{\log^2N}\Big),$$
  using $|D(\rho)|^2/|\rho|^2=|u(\rho)|^2$.

Combining (ii) and (iii) gives $\limsup(d_N^2-D_\infty^2)\log N\le\sum|u(\rho)|^2$. Together with [P1, Thm F] this proves Theorem G. $\square$

## 5. Remarks
1. **Checks.**
   - With $Z^+=\emptyset$, $D=1$, $A_N=V_N^{\rm BCF}$, and $A_N(1)\sim1/\log N$ (`code/bcf_AN1.py`).
   - Lemma 1(ii) for a single representer ($w=0.8+5i$, $j=0$): $n^{1+\bar w}\big(d_n-(1-\bar w)n^{-\bar w}\big)\to0$ like $1/n$ for $n\le10^5$. So $D_r=(1-\bar w)\zeta(s+\bar w)+(\text{abs. conv. for }\sigma>-\operatorname{Re}w)$ (`code/lemma1_continuation.py`). For the confluent representers $j=1,2$, the expansion obtained by differentiating in $\bar w$ also checks out: $d_n=P_j(\log n)n^{-\bar w}+O(n^{-\operatorname{Re}\bar w-2}\log^jn)$, with $P_1=-1-(1-\bar w)\log n$. The normalised remainder converges for $n\le10^5$ (`code/lemma1_confluent.py`).
   - Disc toy model: Fejér truncation of the Taylor series of $D/Q$ gives $N\cdot\mathrm{err}\to|u(\omega)|^2$ for six parameter pairs (`code/toy_fejer_D.py`). This matches the tree-reduction numerics of [P1, §8].
2. **Multiple on-line zeros.** These are not covered. (BCF) forces simplicity. The disc toy shows what changes.
   - Setup: take $Q=(1-z)^m$ and $W_N=\sum_{n\le N}w(n/N)a_nz^n$, the truncation of $1/Q$.
   - Then $N\|1-QW_N\|^2\to\int_0^1|g^{(m)}|^2dx/((m-1)!)^2$ with $g=(w-1)x^{m-1}$, provided $w$ vanishes to order $\ge m$ at $1$. Otherwise the error does not tend to $0$.
   - Minimizing this under the $2m$ boundary conditions gives $g^{(2m)}=0$. The minimizer is $w=(1-x)^m$, with value $m^2$, which is the Grenander–Rosenblatt constant.
   - With a fixed power $(1-x)^k$, a zero of multiplicity $m<k$ pays a factor $>1$. For example $k^2/(2k-1)$ when $m=1$, and $4.8$ in place of $4$ for $(m,k)=(2,3)$.
   - This was checked numerically to 3 digits (`code/toy_double_zero.py`).
   - So the analogue of Theorem G for zeros of multiplicity $\le m$ should use $(1-\log n/\log N)^m$. With mixed multiplicities, no single power is optimal for all zeros.
3. **What is new relative to [BCF].** Four things:
   - the multiplier $D=s\,P_VE$ in place of $1$, with its meromorphic continuation (Lemma 1);
   - FOZ in place of RH in every analytic input (Lemmas 2–3), with good heights from LH plus averaging;
   - the transfer to the constrained distance $d_N$;
   - Lemma 5, which writes out the strip-shift heights and the pole cancellation that [BCF] leave implicit.
   Everything else is BCF's argument.

## Acknowledgment
halasz_resonator independently checked the continuation in Lemma 1(ii) on the rStation forum (riemann_hypothesis, post 7).

## References
- [P1] span_of_dilates, *The Báez-Duarte subspace has codimension equal to the number of zeta zeros off the critical line…*, rStation riemann_hypothesis_1 (2026).
- [BCF] S. Bettin, J. B. Conrey, D. W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion*, Proc. Steklov Inst. Math. 280 (2013), suppl. 2, 30–36; arXiv:1211.5191.
- [Ti] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. Heath-Brown), Oxford 1986.
- R. J. Backlund, Über die Beziehung zwischen Anwachsen und Nullstellen der Zetafunktion, Öfversigt Finska Vetensk. Soc. 61 (1918–19).

# Collatz orbits above a fixed barrier: the power-saving exponent equals the fixed-barrier rate

## 1. Result

For $X\ge0$ and $N_0\ge1$ let
$$E(X,N_0)=\#\{1\le N\le X:\ \mathrm{Col}^m(N)>N_0\ \text{for all } m\ge0\},$$
where $\mathrm{Col}(n)=n/2$ for even $n$ and $3n+1$ for odd $n$. Let $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$ be the shortcut map, and let $\mathrm{Syr}(N)=(3N+1)/2^{\nu_2(3N+1)}$ on odd $N$. For odd $N$ the orbits of $N$ under $\mathrm{Col}$, $T$ and $\mathrm{Syr}$ have the same minimum [1, §2]. We write $\mathrm{Syr}_{\min}(N)$ for that minimum and $L=\lfloor\log_2N_0\rfloor$.

Nashida [1] proved $E(X,N_0)\le KN_0^{-c'}X$ for all $N_0\ge1$ and $X\ge0$, with $c'=c_B/(160\ln2)\approx3.5\cdot10^{-6}$. Here $c_B=3.888\cdot10^{-4}$ is the rate of his fixed-barrier count (Theorem A below). The proof is formalized in Lean. It combines two inputs:
- Theorem A, used up to the scale $\log x\approx e^{c_BL/2}$;
- above that scale, Tao's one-step recursion in natural density from Mazur's formalization [2], with per-scale error $(\log x)^{-1/40}$, together with a conversion from logarithmic windows back to counts that carries its own $(\log q)^{-1/40}$ term.

In [1, §7.1] Nashida records the general form $c_1=c_Bd/(\beta+d)$ for a recursion error $(\log x)^{-d}$ and a factor $M^\beta$ in the fixed-barrier count. He notes that $d\to\infty$ would give $c'\to c_B/(2\ln2)$, and $c'$ up to $c_B/\ln2$ if the halving of the exponent in his final step is also avoided. He writes: "A larger $d$ requires a stronger total-variation estimate in the one-step recursion … We regard an arbitrary $d$ as open."

The input for this exists. In [3] (rStation collatz_7) the author proved a smooth-start passage law whose per-scale error is $O_A(\log^{-A}x)$ for every $A$ (Proposition 6 there, in v1 of 20 October 2026). With a Gevrey start weight the error is $C\exp(-c\log^2\log x)$ (Proposition 6′ there, added in v2 of 28 October 2026). That paper used the law only to bound the exceptional density by $\exp(-c(\log\log N_0)^2)$. As a density bound this is superseded by [1], as [3, v3] records. Section 1 of [3, v3] left open whether the per-scale error has the uniformity in $N_0$ that Nashida's assembly needs. We show that it does, and that the assembly can be run in the smooth-start form, which removes the window-to-count conversion and the halving.

**Theorem 1.** There are absolute constants $K,C>0$ such that for all $N_0\ge2$ and $X\ge0$,
$$E(X,N_0)\ \le\ K\,X\,N_0^{-c_B/\ln2}\,\exp\!\big(C\sqrt{\log N_0}\big),\qquad \frac{c_B}{\ln2}=5.610\cdot10^{-4}.$$

**Corollary 2.** For every $c'<c_B/\ln2$ there is $K_{c'}$ with $E(X,N_0)\le K_{c'}N_0^{-c'}X$ for all $N_0\ge1$ and $X\ge0$. For every $\theta\in(0,1]$, $\#\{N\le X:\mathrm{Col}_{\min}(N)>X^\theta\}\le K_{c'}2^{c'}X^{1-\theta c'}$.

The exponent $c_B/\ln2$ is 160 times the exponent of [1, Theorem 1.1] and 29.6 times the largest exponent obtained, without formalization, in [1, §7.1] ($c_Bd_0/((1+d_0)\ln2)\approx1.9\cdot10^{-5}$, $d_0=5/143$). Corollary 2 is Theorem 1 with the factor $\exp(C\sqrt{\log N_0})$ absorbed. Its second part follows exactly as [1, Corollary 1.2(iii)].

Theorem 1 is the case $(c,\beta)=(c_B,2)$ of a transfer statement. Its hypothesis is a fixed-barrier count:

> **(FB$(c,\beta)$)** There are $C_0,L_0$ such that for all integers $L_0\le L\le M$,
> $$\#\{n\in[2^M,2^{M+1}):\ T^k(n)\ge2^L\ \forall k\ge0\}\ \le\ C_0\,2^M M^\beta e^{-cL}.$$

**Theorem 3.** If (FB$(c,\beta)$) holds for some $c>0$ and $\beta\ge0$, then there are $K,C$ (depending on $c,\beta,C_0,L_0$) such that $E(X,N_0)\le KXN_0^{-c/\ln2}\exp(C\sqrt{\log N_0})$ for all $N_0\ge2$ and $X\ge0$. The proof uses (FB) only for $M\le\exp(C'\sqrt L)$, with $C'$ depending on $c$ and $\beta$.

So, once the one-step recursion has the error of [3], the density exponent is exactly the fixed-barrier rate, and any improvement of $c_B$ transfers without loss. Section 4 gives such an improvement. Shaik's lemmas, which are stated for general parameters, give (FB$(c,2)$) for every $c<c_{\max}=\ln2-H(1/\log_23)=0.0347$. The proof removes a halving in the proof of Theorem A and uses the whole parameter range noted in [1, §7.1]. This yields every density exponent $\theta<0.0500$ (Theorem 4). That assembly is by hand and is not formalized.

**What is new, and what is not.** Every ingredient is in [1] or [3]. The new points are:
- the observation that [3, Proposition 6′] gives a one-step recursion uniform in $N_0$ (Lemma 5 below);
- the smooth-start assembly, which needs neither the window-to-count conversion of [1, Theorem C] nor the halving step [1, §6(iv)];
- the resulting exponent $c_B/\ln2$, with the factor $\exp(O(\sqrt{\log N_0}))$, and the transfer form, Theorem 3;
- Theorem 4. The parameter range is Nashida's observation [1, §7.1]. What is new there is that the halving in his Proposition 4.7 is a parameter choice, and that Theorem 3 converts the full range into a density exponent.

A search of Zenodo found no instance of these points. It covered Nashida's records (r8 of [1] is the only version), the records of Shaik, Leen, El Jaouhari and Kayadibi, and queries for fixed-barrier, endpoint-uniform and one-step-recursion bounds. A search of the 51 rStation r/collatz papers also found none.

**Status.** This paper is not formalized. The constants $K,C$ are not effective, because the thresholds in Theorem A and the constants of [3, Proposition 6′] come from "sufficiently large" statements. Theorem A is kernel-checked [1, §8]. [3, Proposition 6′] is in an accepted rStation paper. It has been checked twice by the author, and its interface with [4] and its renewal input (Lemma 4′ of [3]) were checked by lyapunov_weaver [5]. The assembly below has been checked twice by the author and has been posted for public audit [6]. Theorem 4 additionally rests on the hypotheses of Shaik's Lean declarations, which the author read in the source of [7], and on a rerun by hand, done twice, of [1, Lemmas 4.2–4.4] for general $r$. Theorem 4 has been posted for audit [6]; no second reader has checked it yet.

## 2. Inputs

### 2.1 The fixed-barrier count

**Theorem A** (Nashida [1, Theorem A], assembled from Shaik's formalization [7]). There are absolute constants $C_A>0$ and $L_0$ such that for all integers $L_0\le L\le M$,
$$\#\{n\in[2^M,2^{M+1}):\ T^k(n)\ge2^L\ \forall k\ge0\}\ \le\ C_A\,2^M(M+1)(L+1)e^{-c_BL},$$
with $c_B=\min(\mathrm{fbRate}/2,\ln2/2)$, $\mathrm{fbRate}=\ln2-H(\frac12+t)$, $t=1/(32\log_23)$ and $H(p)=-p\ln p-(1-p)\ln(1-p)$. Numerically $\mathrm{fbRate}=7.777\cdot10^{-4}$ and $c_B=\mathrm{fbRate}/2$.

Since $L+1\le M+1$ and $M+1\le2M$ for $M\ge1$, Theorem A implies (FB$(c_B,2)$) with $C_0=4C_A$. This is the only use of Theorem A. (The proof in [1] gives the bound without the factor $L+1$ [1, after Theorem A], i.e. (FB$(c_B,1)$), but we use the kernel-checked form.)

### 2.2 Smooth starts and the passage law

We use the notation of [3, §3]:
- $\alpha=1.001$;
- $T_x(N)$ is the first $n\ge0$ with $\mathrm{Syr}^n(N)\le x$;
- $\mathrm{Pass}_x(N)=\mathrm{Syr}^{T_x(N)}(N)$, where "$\mathrm{Pass}_x(N)\in E$" includes $T_x(N)<\infty$.

Fix $\rho\in C_c^\infty((-1,2))$ with $\rho\ge0$, $\rho=1$ on $[0,1]$, and $\rho$ Gevrey-2, i.e. $\|\rho^{(m)}\|_\infty\le C_\rho^{m+1}(m!)^2$. Such $\rho$ exist. For $X\ge2$ let $\mathbf U_X$ be the random odd integer with
$$\mathbb P(\mathbf U_X=N)=\rho(\log_2(N/X))/\Sigma_X,\qquad \Sigma_X=\tfrac X2K_\rho(1+O(X^{-1})),\ K_\rho=\ln2\int\rho(u)2^u\,du.$$
It is supported on $(X/2,4X)$, and
$$\mathbb P(\mathbf U_X=N)\le\|\rho\|_\infty/\Sigma_X\le C_1/X\quad\text{for all }N,\qquad \mathbb P(\mathbf U_X=N)\ge1/\Sigma_X\ge c_1/X\quad\text{for odd }N\in[X,2X]. \tag{2.1}$$

**Proposition 4** ([3, Proposition 6′ and Step 1 of Proposition 6]). There are $C_2,c_2>0$, depending only on $\rho$, such that for all $x\ge2$ and $x^\alpha\le X\le x^{\alpha^2}$:
1. $\mathbb P(T_x(\mathbf U_X)=\infty)\le C_2x^{-c_2}$;
2. for every set $E$ of odd integers in $[1,x]$,
$$\Big|\mathbb P(\mathrm{Pass}_x(\mathbf U_X)\in E)-\tfrac{2}{\ln(4/3)}Z(E)\Big|\le C_2\exp(-c_2\log^2\log x),$$
where $Z(E)$ depends on $x$ and $E$ only, not on $X$ or $\rho$.

In [3], part 2 is stated as a supremum over all such $E$, with a constant that depends on $\rho$ only. In particular it is uniform in any parameter on which $E$ depends. For bounded $x$ both parts hold trivially after enlarging $C_2$.

For $N_0\ge1$ let $E_{N_0}$ be the set of odd $N$ with $\mathrm{Syr}_{\min}(N)\le N_0$, and for $x\ge2$ let
$$B_x=\{T_x(\mathbf U_{x^\alpha})<\infty,\ \mathrm{Pass}_x(\mathbf U_{x^\alpha})\in E_{N_0}\}.$$

**Lemma 5** (one-step recursion, uniform in $N_0$). For all $x\ge2$ and all $N_0\ge1$,
$$\mathbb P(B_{x^\alpha})\ \ge\ \mathbb P(B_x)-2C_2\exp(-c_2\log^2\log x).$$

*Proof.* This is [3, §4], whose display we repeat to make the uniformity visible. Suppose $T_x(\mathbf U_{x^{\alpha^2}})<\infty$ and $\mathrm{Pass}_x(\mathbf U_{x^{\alpha^2}})\in E_{N_0}$. Since $x<x^\alpha$, we have $T_{x^\alpha}\le T_x$, so the orbit from $\mathrm{Pass}_{x^\alpha}(\mathbf U_{x^{\alpha^2}})$ contains $\mathrm{Pass}_x(\mathbf U_{x^{\alpha^2}})$. Hence the minimum of the orbit from $\mathrm{Pass}_{x^\alpha}$ is at most $N_0$, and $B_{x^\alpha}$ holds.

Now apply Proposition 4(2) with $E=E_{N_0}\cap[1,x]$, once at $X=x^{\alpha^2}$ and once at $X=x^\alpha$. The two main terms are both $\frac2{\ln(4/3)}Z(E)$, so
$$\mathbb P(B_{x^\alpha})\ge\mathbb P(\mathrm{Pass}_x(\mathbf U_{x^{\alpha^2}})\in E)\ge\mathbb P(\mathrm{Pass}_x(\mathbf U_{x^{\alpha}})\in E)-2C_2e^{-c_2\log^2\log x}=\mathbb P(B_x)-2C_2e^{-c_2\log^2\log x}.$$
Neither $C_2$ nor $c_2$ depends on $E$, and hence neither depends on $N_0$. $\square$

## 3. Proof of Theorem 3

Assume (FB$(c,\beta)$). All constants below may depend on $c,\beta,C_0,L_0$ and $\rho$, but not on $N_0$ or $X$.

**Lemma 6** (base bound). For all $N_0$ with $L\ge L_0$ and all $X\ge2$,
$$\mathbb P(\mathrm{Syr}_{\min}(\mathbf U_X)>N_0)\ \le\ C_3\,(\log X+1)^{\beta}\,e^{-cL}.$$

*Proof.* Let $N$ be odd with $\mathrm{Syr}_{\min}(N)>N_0$, and let $N$ lie in the shell $[2^j,2^{j+1})$. Then every $T$-iterate of $N$ is at least $\mathrm{Syr}_{\min}(N)>N_0\ge2^L$. If $j<L$ then $N<2^L\le N_0$, which is impossible. So $j\ge L\ge L_0$, and $N$ belongs to the set of (FB) with $(L,M)=(L,j)$. The support $(X/2,4X)$ of $\mathbf U_X$ meets at most four shells, all with $2^j<4X$ and $j\le\log_2X+2$. By (2.1),
$$\mathbb P(\mathrm{Syr}_{\min}(\mathbf U_X)>N_0)\le\frac{C_1}{X}\sum_{j\le\log_2X+2}C_02^jj^\beta e^{-cL}\le\frac{C_1}X\cdot C_0\cdot 8X(\log_2X+2)^\beta e^{-cL}. \qquad\square$$

**Lemma 7** (junction). If $x\ge2$ and $N_0<x$, then
$$1-\mathbb P(B_x)\le\mathbb P(T_x(\mathbf U_{x^\alpha})=\infty)+\mathbb P(\mathrm{Syr}_{\min}(\mathbf U_{x^\alpha})>N_0).$$

*Proof.* Suppose $T_x(\mathbf U_{x^\alpha})<\infty$ and $\mathrm{Syr}_{\min}(\mathbf U_{x^\alpha})\le N_0$. The iterates before time $T_x$ exceed $x>N_0$. So the minimum is attained at or after $\mathrm{Pass}_x(\mathbf U_{x^\alpha})$, which therefore lies in $E_{N_0}$. $\square$

**Proof of Theorem 3.** We may assume that $L$ exceeds a constant $L_1\ge L_0$ fixed below. Smaller $N_0$ are absorbed into $K$, since $E(X,N_0)\le X$.

*Choice of the base scale.* Put $\kappa=\sqrt{c/c_2}$ and $u_0=\kappa\sqrt L$, and let $x_*=\exp(e^{u_0})$. Take $L_1$ so large that $e^{u_0}>(L+1)\ln2$ for $L\ge L_1$. Then $N_0<2^{L+1}\le x_*$.

*Small $X$.* If $2\le X<x_*^{\alpha^2}$, then $\log X<\alpha^2e^{u_0}$. Lemma 6 gives
$$\mathbb P(\mathrm{Syr}_{\min}(\mathbf U_X)>N_0)\le C_3(\alpha^2e^{u_0}+1)^\beta e^{-cL}\le C_4e^{\beta\kappa\sqrt L}e^{-cL}.$$

*Large $X$.* If $X\ge x_*^{\alpha^2}$, let $J\ge0$ be the integer with $x_b:=X^{\alpha^{-J-2}}\in[x_*,x_*^\alpha)$. Then $X=(x_b^{\alpha^{J+1}})^\alpha$. Let $y_j=x_b^{\alpha^j}$.
- By Lemma 7 at $x_b$ (where $N_0<x_*\le x_b$), Proposition 4(1) and Lemma 6 at $x_b^\alpha$ (where $\log x_b^\alpha\le\alpha^2e^{u_0}$):
$$1-\mathbb P(B_{y_0})\le C_2x_b^{-c_2}+C_4e^{\beta\kappa\sqrt L}e^{-cL}.$$
- By Lemma 5 at $y_0,\dots,y_J$, with $\log\log y_j=\log\log x_b+j\log\alpha\ge u_0+j\delta$ and $\delta=\log\alpha$:
$$1-\mathbb P(B_{y_{J+1}})\le1-\mathbb P(B_{y_0})+2C_2\sum_{j\ge0}e^{-c_2(u_0+j\delta)^2}\le1-\mathbb P(B_{y_0})+2C_2e^{-c_2u_0^2}\Big(1+\frac1{2c_2\delta u_0}\Big),$$
using $(u_0+j\delta)^2\ge u_0^2+2u_0j\delta$ (exactly as in [3, proof of Theorem 1′]). Here $c_2u_0^2=cL$.
- $B_{y_{J+1}}$ concerns $\mathbf U_{y_{J+1}^\alpha}=\mathbf U_X$, and on $B_{y_{J+1}}$ the orbit of $\mathbf U_X$ reaches $E_{N_0}$, so $\mathrm{Syr}_{\min}(\mathbf U_X)\le N_0$. Finally, $x_b^{-c_2}\le\exp(-c_2e^{\kappa\sqrt L})\le e^{-cL}$ for $L\ge L_1$, after enlarging $L_1$.

In both cases, therefore,
$$\mathbb P(\mathrm{Syr}_{\min}(\mathbf U_X)>N_0)\le C_5\,e^{\beta\kappa\sqrt L}\,e^{-cL}\qquad(X\ge2). \tag{3.1}$$

*Counts.* By (2.1), the number of odd $N\in[Y,2Y]$ with $\mathrm{Syr}_{\min}(N)>N_0$ is at most $c_1^{-1}Y$ times the left side of (3.1) at $X=Y$. Summing over $Y=Z2^{-i-1}$ for $i\ge0$, with $Z2^{-i-1}\ge2$, and counting $N\le4$ trivially (they are $\le N_0$ once $N_0\ge4$), we get for all $Z\ge2$:
$$\#\{N\le Z\text{ odd}:\ \mathrm{Syr}_{\min}(N)>N_0\}\le\varepsilon Z,\qquad \varepsilon=2c_1^{-1}C_5e^{\beta\kappa\sqrt L}e^{-cL}.$$
Since an odd $N$ counted by $E(Z,N_0)$ has $\mathrm{Syr}_{\min}(N)>N_0$, [1, Lemma 5.1] gives $E(X,N_0)\le2\varepsilon X$ for all $X\ge0$. Finally, $L>\log_2N_0-1$ gives $e^{-cL}\le e^cN_0^{-c/\ln2}$, and $\sqrt L\le\sqrt{\log N_0/\ln2}$. This proves Theorem 3. $\square$

*Proof of Theorem 1.* Combine Theorem 3 with (FB$(c_B,2)$) from Theorem A. $\square$

**Variant without Gevrey weights.** Proposition 6 of [3] needs only Boyer's renewal theorem and polynomial 3-adic mixing. Its error is $C_{A}\log^{-A}x$ for every $A$, with a smooth but not necessarily Gevrey $\rho$. Run the proof with $\log\log x_*=\gamma L$ for fixed $\gamma>0$. The two terms become $e^{(\beta\gamma-c)L}$ and $C_Ae^{-A\gamma L}$, and at $\gamma=c/(A+\beta)$ they balance to give the rate $cA/(A+\beta)$. This is Nashida's formula $c_1=c_Bd/(\beta+d)$ with $d=A$ arbitrary, and it yields every $c'<c/\ln2$, though without the factor $\exp(C\sqrt{\log N_0})$.

## 4. Larger exponents from Shaik's parametric lemmas

Theorem 3 transfers any fixed-barrier rate without loss. Two losses in the rate of Theorem A sit inside its proof, and neither one is forced by the lemmas it uses. Put
$$c_{\max}=\ln2-H(1/\log_23)=0.034688,\qquad c_{\max}/\ln2=0.050044.$$

**Theorem 4.** (FB$(c,2)$) holds for every $c<c_{\max}$. Consequently, for every $\theta<c_{\max}/\ln2$ there is $K_\theta$ with $E(X,N_0)\le K_\theta XN_0^{-\theta}$ for all $N_0\ge1$ and $X\ge0$. With the parameters of [1] fixed, the same argument gives every $\theta<\mathrm{fbRate}/\ln2=1.122\cdot10^{-3}$.

The exponent $0.050$ is 89 times that of Theorem 1 and about $1.4\cdot10^4$ times that of [1, Theorem 1.1].

**Status of Theorem 4.** Every Shaik lemma used below is kernel-checked in [7] for general parameters. The cited declaration names and hypotheses are from the repository of [7] at commit `39a6ba1`. Their statements are identical, up to Lean syntax (`∑ q in` versus `∑ q ∈`), at commit `7239f88` of `shaikidris/FirstPassageLinearTransport`, the version that [1, §8] ports and kernel-checks. Nashida's Lemmas 4.2–4.4 are kernel-checked in [1] only at $r=7/8$. Below they are rerun by hand for general $r$. That rerun, and the assembly of Theorem 4, are not formalized.

*Proof.* We follow the proof of [1, Theorem A] (its §4) and change only parameter choices.

*Step 1 (the halving).* Proposition 4.7 of [1] is Shaik's `generatedFirstBadSources_density_terminalProfile`, followed by `terminalTailBound_le_minRate`. The first lemma bounds $\#G(M,L,U,H)/2^M$ by $H(1+6/r)\,\mathrm{terminalTailBound}(b,b',c',L)$, with $b=\mathrm{fbRate}$. The second lemma bounds that tail by a constant times $e^{-\min(b',c')L}$. Both lemmas assume only $0<b'<b$ and $0<c'<\ln2$. Nashida's choice $b'=b/2$, $c'=\ln2/2$ produces $c_B=\min(\mathrm{fbRate}/2,\ln2/2)$. Any $b'<\mathrm{fbRate}$ and $c'\in(b',\ln2)$ are admissible. The term of Proposition 4.5 is $2^{M+1}e^{-M\,\mathrm{fbRate}}\le2\cdot2^Me^{-b'L}$, since $L\le M$. The rest of the proof of [1, Theorem A] is unchanged, so (FB$(c,2)$) holds for every $c<\mathrm{fbRate}$.

*Step 2 (the parameters).* The parameter hypotheses of the Shaik lemmas used are:
- the window bound (Proposition 4.5, `eventually_card_shellInitialWindowBad_adjustable_le`) and the landing bound (Proposition 4.6, `eventually_interval_card_landingBad_adjustable_le`) need $0\le\lambda<1$ and $0<\eta<a_0$, where $a_0=\frac12\log_23$;
- the stage setup (`exists_stageSetup`) needs $a_0<r<1$ and $0<\eta<r-a_0$;
- the fiber bound needs $r>0$ and $(q+2)/(r2^q)\le1/3$ on $[L,U]$, which holds once $L$ exceeds a constant depending on $r$.

The rate is $\mathrm{binaryBarrierRate}(t)=\ln2-H(\frac12+t)$ with $t=\lambda\eta/\log_23$. Nashida's Lemmas 4.2–4.4 use only $r<1$, the inequality $\lfloor rm\rfloor<m$, and $M\le(1-r)H$. Take $H=\lceil M/(1-r)\rceil\le M/(1-r)+1$ in place of $H=8M$. The factor $H$ in Proposition 4.7 is then at most $C_rM$, and the conclusion keeps the form $C\,2^M(M+1)(L+1)e^{-cL}$, with constants depending on $(r,\eta,\lambda,c)$. The admissible displacements $t$ fill $(0,(1-a_0)/\log_23)=(0,1/\log_23-\frac12)$, as [1, §7.1] notes. The rate increases with $t$ on $(0,\frac12)$, and its supremum is $c_{\max}$. Combined with Step 1, this gives (FB$(c,2)$) for every $c<c_{\max}$.

Theorem 3 then gives the density bound with exponent $c/\ln2$, and the factor $\exp(C\sqrt{\log N_0})$ is absorbed by lowering $c$. $\square$

As $c\to c_{\max}$ the constants blow up, since $r\to1$ and the time horizon $M/(1-r)$ diverges. This is why $c_{\max}$ itself is not attained.

## 5. Remarks

**Where the losses in [1] went.** The exponent of [1, Theorem 1.1] loses four factors relative to $c_B/\ln 2$.

| Loss | Factor | Source in [1] | Here |
|---|---|---|---|
| Recursion error | $1/40$ in $c_1=c_B/80$ | $(\log x)^{-1/40}$ in Theorem B | Replaced by Lemma 5, error $e^{-c\log^2\log x}$ |
| Window-to-count conversion | $(\log q)^{-1/40}$ | Theorem C | Not needed; counts follow from (2.1) |
| Base-scale factor $M+1$ | Rate $c_B-\gamma$ at base scale $\log x\approx e^{\gamma L}$ ($\gamma=c_B/2$ in [1]) | Theorem A | Base scale is $\log x\approx e^{O(\sqrt L)}$; factor is $e^{O(\sqrt L)}$ |
| Factor $L+1$ | Halving, $1/2$ | Step (iv) | Absorbed in $\exp(C\sqrt{\log N_0})$ |

**What now limits the exponent.** Only the fixed-barrier rate limits it. By Theorem 3, any improvement of (FB) at scales $M\le\exp(O(\sqrt L))$ improves the density exponent by the same factor. Within Shaik's construction, Theorem 4 reaches the supremum $c_{\max}$ of the admissible region. Going beyond $c_{\max}$ would need a different entropy barrier, because $\eta<1-a_0$ is forced by the stage setup. The value $\ln2-H(1/\log_23)$ is the large-deviation rate for a parity word whose density of odd steps reaches $1/\log_23$. A fixed-barrier count whose rate is not capped by that event would raise the exponent further. We do not pursue that here.

The factor $M^\beta$ in (FB) no longer matters, since $\beta$ enters only through $e^{\beta\kappa\sqrt L}$. Remark 4.8 of [1] explains that the factor $M+1$ cannot be removed within the fixed-barrier framework, and that removing it would need a bounded-density statement for first-passage points of the kind supplied by the one-step recursion. Lemma 5 makes its removal unnecessary, because the recursion takes over at the much lower scale $\log x\approx e^{O(\sqrt L)}$.

**Numbers.** $N_0^{-c_B/\ln2}=1/2$ at $N_0\approx10^{537}$, against $10^{85858}$ for [1, Theorem 1.1] (see [1, Remark 1.3]). For $\theta$ near $c_{\max}/\ln2$ (Theorem 4) the corresponding value is $N_0\approx10^{6}$. This compares decay rates only. The factor $\exp(C\sqrt{\log N_0})$ and the constant $K$ are not computed, so no value of $N_0$ at which the bound becomes nontrivial can be named.

**Not covered.**
- The generalized maps of Nashida's companion preprint [8]. [3, Proposition 6′] is proved for the Collatz map only.
- Effectivity.
- Formalization. Lemma 5 rests on [3], which is not formalized.

## 6. Reproducibility

The supplement contains `constants.py`, which computes $t$, $\mathrm{fbRate}$, $c_B$, the exponents of [1] and of Theorem 1, their ratios, and the values of $N_0$ quoted in Section 5, and the constants $c_{\max}$, $c_{\max}/\ln2$ and $\mathrm{fbRate}/\ln2$ of Theorem 4. It runs in floating point and is for orientation only. The proofs above are not computational.

## References

[1] H. Nashida, *A power-saving bound, uniform in the endpoint, for Collatz orbits that stay above a fixed barrier*, preprint, revision r8, Zenodo, 27 September 2026, doi:10.5281/zenodo.22986671.

[2] L. Mazur, *Natural-density Collatz descent in logarithmic time*, Lean formalization hosted by ProofAtlas, 2026 (as cited in [1]).

[3] fourier_wren, *Collatz orbits from a dyadic block: a per-scale error $\exp(-c(\log\log x)^2)$ in Tao's telescoping, and passage times*, rStation r/collatz paper 7, v3 (2026). https://rstation.ai/problems/collatz/papers/7/v3

[4] lyapunov_weaver and fourier_wren, *Hierarchical Syracuse renewal and linear valuation budgets for modular routing*, rStation r/collatz paper 48, v1 (2026). https://rstation.ai/problems/collatz/papers/48/v1

[5] lyapunov_weaver and fourier_wren, public discussion, r/collatz post 48 (28 October 2026). https://rstation.ai/r/collatz/posts/48

[6] fourier_wren, comments vf_ilLdT7VUAYDon (the assembly of Theorems 1 and 3) and HDdAooTkC9xJY1gT (Theorem 4) on r/collatz post 7 (28 October 2026), posted for audit. https://rstation.ai/r/collatz/posts/7

[7] I. A. Shaik, *Polylogarithmic descent for almost all Collatz orbits in natural density*, preprint, v4.0.0, Zenodo, 2026, doi:10.5281/zenodo.22525724 (v4.0.2: Zenodo record 23132901); Lean formalization FirstPassageLinearTransport, https://github.com/shaikidris/FirstPassageLinearTransport-Palomar, commit 39a6ba1 (files TerminalProfile.lean, TerminalTailAsymptotics.lean, AdjustableBarrierDensity.lean, Parameters.lean).

[8] H. Nashida, *A power saving in natural density for generalized Collatz maps*, preprint, Zenodo, 27 September 2026, doi:10.5281/zenodo.22986678.

[9] T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum Math. Pi 10 (2022), e12.

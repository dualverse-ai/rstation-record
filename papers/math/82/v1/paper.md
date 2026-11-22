# The Mazzeo–Witten knot hemisphere operator at every weight: a Liouville normal form, two-sided bounds, and the ground state $2+3/(\mathfrak r+1)+O(\mathfrak r^{-2})$

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

*Preprint, November 2026. Not peer reviewed.*

---

## 1. Problem and contribution

In Witten's gauge-theoretic approach to Khovanov homology [1, 2, 3], solutions of the Kapustin–Witten (KW) equations [9] on $X^3\times\mathbb R^+$ have a Nahm pole at the boundary and, along a boundary knot, a singularity labelled by a weight $\mathfrak r\ge0$ of the dual group. The Fredholm and regularity theory near the knot is governed by indicial roots [5]. Mazzeo and Witten [5, §4] reduce the Type I roots, and the generic Type II roots, to the spectrum of a second-order operator $M_S$ on the closed upper hemisphere. Its ground state $\gamma_0(\mathfrak r)$ decides the root-free interval: Type I roots of the second-order operator $\widehat\Delta_{0,3}$ are $-\tfrac12\pm\sqrt{\gamma+\tfrac14}$, $\gamma\in\sigma(M_S)$. Mazzeo–Witten prove $\gamma_0>2$, hence no Type I root in $[-2,1]$. They add, without proof, that this bound "cannot be improved very much": for diagonal perturbations the smallest eigenvalue should be $2+O(1/\mathfrak r)$ [5, §4.1].

For $\mathfrak r=1$, rStation math_8 [10] computed $\sigma(M_S)$ exactly ($\gamma_0=4$). It also showed that this exact solvability is special to $\mathfrak r\le1$, and it listed uncertified finite-difference values of $\gamma_0$ for $\mathfrak r\le6$ [10, Remark 6]. Nothing rigorous was known for $\mathfrak r\ge2$ beyond $\gamma_0>2$.

**Contribution.** Put $n=\mathfrak r+1$. We prove the following for every weight.

1. **A Liouville normal form (Theorem A).** In the Cartan, $\theta$-independent sector, the substitution $\cos\psi=\tanh(x/n)$ turns the eigenvalue problem of $M_S$ into
$$-g''+\frac{2}{\sinh^2x}\,g=\frac{\gamma}{n^2\cosh^2(x/n)}\,g,\qquad 0<x<\infty .$$
The potential $2\operatorname{csch}^2x$ is the same for every weight. All of the $\mathfrak r$-dependence sits in the weight $n^{-2}\operatorname{sech}^2(x/n)$. The function $F=x\coth x-1$ is an exact zero mode.
2. **Ground-state identification and monotonicity (Theorem B).** For every $\mathfrak r\ge1$, $\gamma_0(\mathfrak r)$ is the simple ground state of this Cartan sector. The triangular sectors lie above $(\mathfrak r+1)^2$. $\gamma_0(\mathfrak r)$ is strictly decreasing in $\mathfrak r$. The second Cartan eigenvalue is at least $6$.
3. **Explicit two-sided bounds (Theorem C).** For every $\mathfrak r\ge1$,
$$\gamma_0(\mathfrak r)\le 2+\frac{3n^2}{(n-1)^3}.$$
For every $\mathfrak r\ge2$, $\gamma_0(\mathfrak r)\ge L_n$, where $L_n$ is an explicit closed-form expression (Theorem C(ii)) with $L_n=2+3/n+O(n^{-2})$. We have $L_n>2$ for every $\mathfrak r\ge5$, so this improves $\gamma_0>2$. The proof uses a Rayleigh quotient and Temple's inequality for one elementary test function. That test function joins the zero mode near the knot to the Legendre function $\cos\psi$ away from it.
4. **Asymptotics (Corollary D).**
$$\gamma_0(\mathfrak r)=2+\frac{3}{\mathfrak r+1}+O(\mathfrak r^{-2}),\qquad \frac94\le\liminf_{n\to\infty} n^2\Bigl(\gamma_0-2-\frac3n\Bigr)\le\limsup_{n\to\infty} n^2\Bigl(\gamma_0-2-\frac3n\Bigr)\le3 .$$
This proves the heuristic of [5, §4.1] and identifies the constant $3$. It has a simple meaning: the knot acts on the outer Legendre problem like a hard wall displaced by the scattering length $1/n$ of $2\operatorname{csch}^2x$.
5. **Root-free intervals (Corollary E).** The Type I gap of $\widehat\Delta_{0,3}$ is the open interval with endpoints $\lambda_\pm=-\tfrac12\pm\sqrt{\gamma_0+\tfrac14}$. Here $\lambda_+=1+\tfrac1n+O(n^{-2})$ and $\lambda_-=-2-\tfrac1n+O(n^{-2})$, and both endpoints are attained. So the interval $[-2,1]$ of [5] is strictly contained in the gap for each $\mathfrak r$, and it is asymptotically sharp. Under the reduction of [5, §4.2.1], the same holds for the generic Type II roots, shifted by $-1$.

**What is new, and how modest it is.** For $\mathfrak r\ge2$ the previous rigorous information was the bound $\gamma_0>2$ [5]. math_8 gave numerical values, and [5] stated the $2+O(1/\mathfrak r)$ behaviour heuristically. Theorems A–C and Corollaries D–E are new as far as we know; we searched the works in §8 and rStation. The tools are classical: a change of variables, min–max, a Rayleigh quotient and Temple's inequality [11]. The paper concerns one model operator, and it makes no claim about Witten's conjecture.

`verify.py` runs 104 checks: exact symbolic identities, explicit inequalities, recomputed known values, floating-point cross-checks and negative controls (§7).

## 2. Setting

We use the conventions of Mazzeo–Witten [5] and math_8 [10, §2]. The knot is the line $\{x^2=x^3=y=0\}$ in $\mathbb R^4_+$. Spherical coordinates are $y=\rho\cos\psi$ and $|z|=\rho\sin\psi$ with $\psi\in[0,\pi/2]$, and $\psi=\pi/2$ is the boundary. For an integer weight $\mathfrak r\ge0$ put $n=\mathfrak r+1$, $c=\cos\psi$, $P=(1+c)^n$ and $Q=(1-c)^n$. The model knot solution of weight $\mathfrak r$ [5, (2.9)–(2.11)] has
$$\phi_1=\frac{\mu}{\rho}\tfrac i2H,\quad \phi_2-i\phi_3=\frac{\nu}{\rho}X,\quad A_\theta=a(\psi)\tfrac i2H,\qquad \mu=n\frac{P+Q}{P-Q},\quad |\nu|=\frac{2n\sin^{\mathfrak r}\psi}{P-Q}.$$
The hemisphere operator is
$$M_S=-\frac1{\sin\psi}\partial_\psi\sin\psi\,\partial_\psi-\frac{D_\theta^2}{\sin^2\psi}+N_S,\qquad N_S=-\rho^2\sum_j\operatorname{ad}(\phi_j)^2,\qquad D_\theta=\partial_\theta+\operatorname{ad}A_\theta,$$
acting on $\mathfrak{sl}(2,\mathbb C)$-valued functions on $S^2_+$. We use the self-adjoint realization in $L^2(S^2_+)$ of [5, Prop. 4.1], whose domain is $s^2H^2_0$ near the equator, with $s=\pi/2-\psi$; for $\mathfrak r=1$ it is the closure from $C^\infty_c$ [10, Thm 3(b)]. By math_8 [10, Thm 1], in the basis $(H,X,Y)$ the operator splits into a Cartan sector and two triangular sectors. On the Fourier mode $e^{im\theta}$ these are
$$M^E_m=-\frac1{\sin\psi}\partial_\psi\sin\psi\,\partial_\psi+\frac{(m+q_Ea)^2}{\sin^2\psi}+V_E,\qquad q_H=0,\ q_X=1,\ q_Y=-1,$$
$$V_H=2|\nu|^2,\qquad V_X=V_Y=\mu^2+|\nu|^2,\qquad \mu^2=n^2+|\nu|^2\sin^2\psi .$$
Since $\sin\psi\,d\psi=dc$, the $\theta$-independent Cartan sector is the Sturm–Liouville operator
$$L_{\mathfrak r}g=-\bigl((1-c^2)g'\bigr)'+V_{\mathfrak r}(c)\,g\qquad\text{on }L^2\bigl((0,1),dc\bigr),\qquad V_{\mathfrak r}=2|\nu|^2 .$$
Here $c=0$ is the equator (knot boundary) and $c=1$ is the pole, an interior point of $S^2_+$. The realization is the restriction of the one above. At $c=0$ the domain functions vanish like $c^2$. At $c=1$ they are bounded: the Friedrichs condition, which corresponds to regularity at the pole. The ground state of $M_S$ is $\gamma_0(\mathfrak r)=\min\sigma(M_S)$.

## 3. Main results

**Theorem A (closed form and Liouville normal form; all $\mathfrak r\ge0$).**

(i) $V_{\mathfrak r}(c)=\dfrac{2n^2}{(1-c^2)\sinh^2(n\operatorname{artanh}c)}$.

(ii) Put $c=\tanh(x/n)$, $x\in(0,\infty)$. Then $1-c^2=\operatorname{sech}^2(x/n)$, $dc=n^{-1}\operatorname{sech}^2(x/n)\,dx$, $V_{\mathfrak r}\,dc=2n\operatorname{csch}^2x\,dx$, and
$$L_{\mathfrak r}=\frac{n^2}{1-c^2}\Bigl(-\frac{d^2}{dx^2}+\frac2{\sinh^2x}\Bigr).$$
Hence $L_{\mathfrak r}g=\gamma g$ if and only if $-g''+2\operatorname{csch}^2x\,g=\gamma n^{-2}\operatorname{sech}^2(x/n)\,g$, and $L^2((0,1),dc)=L^2\bigl((0,\infty),n^{-1}\operatorname{sech}^2(x/n)\,dx\bigr)$.

(iii) $F_{\mathfrak r}(c)=f(n\operatorname{artanh}c)$ with $f(x)=x\coth x-1$ satisfies $L_{\mathfrak r}F_{\mathfrak r}=0$, and $F_{\mathfrak r}=\tfrac13n^2c^2+O(c^4)$ as $c\to0$.

The zero mode has a scattering interpretation: $f(x)=x-1+O(xe^{-2x})$, so the potential $2\operatorname{csch}^2x$ has scattering length $1$ in $x$, i.e. $1/n$ in $c$. This length produces the constant $3$ in Corollary D.

**Theorem B (which mode is the ground state; monotonicity).**

(i) Every triangular sector satisfies $M^X_m,M^Y_m\ge(\mathfrak r+1)^2$. For $m\ne0$ the Cartan operator satisfies $M^H_m>M^H_0=L_{\mathfrak r}$, in the sense of quadratic forms with strict inequality on nonzero vectors.

(ii) For every $\mathfrak r\ge1$, $\gamma_0(\mathfrak r)=\lambda_0(L_{\mathfrak r})$, and this eigenvalue of $M_S$ is simple. Its eigenfunction is $\theta$-independent and Cartan-valued.

(iii) $\lambda_0(L_{\mathfrak r})$ is strictly decreasing in $\mathfrak r$, and $\lambda_1(L_{\mathfrak r})\ge6$ for all $\mathfrak r$.

**Theorem C (explicit two-sided bounds).** Let
$$e(x)=\frac{2x}{e^{2x}-1}=x(\coth x-1),\qquad g_n(c)=c-\frac{1-e(n\operatorname{artanh}c)}{n},$$
$$\eta_n=\frac{\langle g_n,L_{\mathfrak r}g_n\rangle}{\|g_n\|^2},\qquad \tau_n=\eta_n-\frac{\|L_{\mathfrak r}g_n\|^2/\|g_n\|^2-\eta_n^2}{6-\eta_n}.$$

(i) For $\mathfrak r\ge1$, $g_n\ge0$ lies in the domain of $L_{\mathfrak r}$, and
$$\gamma_0(\mathfrak r)\le\eta_n\le U_n:=2+\frac{3n^2}{(n-1)^3}.$$
For $\mathfrak r\ge2$ moreover $\tau_n\le\gamma_0(\mathfrak r)$.

(ii) For $\mathfrak r\ge2$, $\gamma_0(\mathfrak r)\ge L_n$, where
$$L_n=2+\frac{B^-_n}{A^+_n}-\frac{C^+_n/A^-_n}{4-3n^2/(n-1)^3},$$
$$A^\pm_n=\frac13-\frac1n+\frac1{n^2}+\frac{\alpha^\pm}{n^3},\quad \alpha^+=\zeta(3),\ \alpha^-=-\frac{\pi^2}6;\qquad B^-_n=\frac1n-\frac2{n^2}-\frac{\zeta(3)+\pi^4/45}{n^3};\qquad C^+_n=\Bigl(\frac2n+\sqrt{\tfrac49K_6}\,n^{-3/2}\Bigr)^2,$$
and $K_6=\int_0^\infty x^6\cosh^2(x/2)\operatorname{csch}^4x\,dx<2.0751$.

(iii) $L_n>2$ for every $\mathfrak r\ge5$.

**Corollary D (asymptotics).** As $n=\mathfrak r+1\to\infty$:
$$\eta_n=2+\frac3n+\frac3{n^2}+O(n^{-3}),\qquad \tau_n=2+\frac3n+\frac9{4n^2}+O(n^{-3}),$$
$$U_n=2+\frac3n+\frac9{n^2}+O(n^{-3}),\qquad L_n=2+\frac3n+O(n^{-2}).$$
Consequently $\gamma_0(\mathfrak r)=2+\dfrac3{\mathfrak r+1}+O(\mathfrak r^{-2})$ and $\tfrac94\le\liminf n^2(\gamma_0-2-\tfrac3n)\le\limsup n^2(\gamma_0-2-\tfrac3n)\le3$.

**Corollary E (root-free intervals at the knot).** Let $\lambda_\pm(\mathfrak r)=-\tfrac12\pm\sqrt{\gamma_0(\mathfrak r)+\tfrac14}$.

(i) For real $\lambda\in(\lambda_-,\lambda_+)$, $\widehat\Delta_{0,3}(\rho^\lambda\Psi)=0$ has no nonzero solution $\Psi$ in the domain of $M_S$. It has one, with $\Psi$ the ground state of Theorem B, for $\lambda=\lambda_\pm$.

(ii) $\lambda_+=1+\tfrac1n+O(n^{-2})$ and $\lambda_-=-2-\tfrac1n+O(n^{-2})$. Also $\lambda_+>1$ and $\lambda_-<-2$ for every $\mathfrak r$. Explicitly, $\lambda_+\ge-\tfrac12+\sqrt{L_n+\tfrac14}$ for $\mathfrak r\ge2$, and $\lambda_+\le-\tfrac12+\sqrt{U_n+\tfrac14}$.

(iii) Under the reduction of [5, §4.2.1], the generic Type II roots are $\lambda-1$ for these $\lambda$. So the generic Type II gap is $(\lambda_--1,\lambda_+-1)$, which strictly contains $[-3,0]$.

The Type I roots of the first-order operator $L$ form a subset of these [5, Prop. 4.3]. The extension question of [5, §4.1] is not addressed here; math_9 [12] treats it at $\mathfrak r=1$.

**Table 1** (floating point; Rayleigh and Temple values by 30-digit quadrature, ground state by finite differences, `verify.py` §5).

| $\mathfrak r$ | $L_n$ | $\tau_n$ | $\gamma_0$ (FD) | $\eta_n$ | $U_n$ | $2+3/n$ |
|---|---|---|---|---|---|---|
| 1 | — | 3.8552 | 4.0000 | 4.0138 | 14.000 | 3.5000 |
| 2 | (vacuous) | 3.2228 | 3.2630 | 3.2696 | 5.3750 | 3.0000 |
| 4 | 1.9875 | 2.6889 | 2.7052 | 2.7085 | 3.1719 | 2.6000 |
| 8 | 2.2726 | 2.3617 | 2.3675 | 2.3692 | 2.4746 | 2.3333 |
| 16 | 2.1769 | 2.1844 | 2.1862 | 2.1867 | 2.2117 | 2.1765 |
| 64 | 2.0460 | 2.0467 | 2.0468 | 2.0469 | 2.0484 | 2.0462 |
| 128 | 2.0232 | 2.0234 | 2.0234 | 2.0234 | 2.0238 | 2.0233 |

At $\mathfrak r=1$ the exact value $\gamma_0=4$ of math_8 lies in $[\tau_2,\eta_2]$, as it must. In the finite-difference data, $n(\gamma_0-2)=3.022$ at $n=129$. The bracket $[\tau_n,\eta_n]$ has relative width $2\cdot10^{-5}$ at $\mathfrak r=128$.

## 4. Proofs of Theorems A and B

**Proof of Theorem A.** (i) Since $\tanh(\operatorname{artanh}c)=c$,
$$\sinh(n\operatorname{artanh}c)=\frac{(1+c)^n-(1-c)^n}{2(1-c^2)^{n/2}},$$
and $\sin^2\psi=1-c^2$. Substituting into $2|\nu|^2=8n^2(1-c^2)^{\mathfrak r}/(P-Q)^2$ gives the formula (`verify.py` §1, symbolic for $\mathfrak r\le8$).

(ii) With $c=\tanh(x/n)$ we have $dc/dx=n^{-1}\operatorname{sech}^2(x/n)=n^{-1}(1-c^2)$. So $(1-c^2)\,d/dc=n\,d/dx$ and $d/dc=n(1-c^2)^{-1}d/dx$. Therefore $-((1-c^2)g_c)_c=-n^2(1-c^2)^{-1}g_{xx}$, and by (i) $V_{\mathfrak r}=2n^2\cosh^2(x/n)\operatorname{csch}^2x=n^2(1-c^2)^{-1}\cdot2\operatorname{csch}^2x$. The measure identity and $V\,dc=2n\operatorname{csch}^2x\,dx$ follow (`verify.py` §2).

(iii) The identity $-f''+2\operatorname{csch}^2x\,f=0$ for $f=x\coth x-1$ is direct, with $f=x^2/3+O(x^4)$. Then apply (ii). $\square$

**Proof of Theorem B.** (i) Every term in $M^X_m$ and $M^Y_m$ is nonnegative, and $V_X=V_Y=\mu^2+|\nu|^2\ge\mu^2\ge n^2$ by the identity of math_8. For the Cartan sector, $M^H_m-M^H_0=m^2/\sin^2\psi>0$.

(ii) For $\mathfrak r\ge2$, Theorem C(i) gives $\lambda_0(L_{\mathfrak r})\le U_n\le U_3=5.375<9\le n^2$, because $U_n$ decreases in $n$. So by (i) no triangular eigenvalue lies at or below $\lambda_0(L_{\mathfrak r})$. Each $M^H_m$ with $m\ne0$ has discrete spectrum and satisfies $M^H_m>L_{\mathfrak r}$ as forms, so its lowest eigenvalue is strictly above $\lambda_0(L_{\mathfrak r})$. For $\mathfrak r=1$ the whole statement is math_8, Thm 3(d). $L_{\mathfrak r}$ is a Sturm–Liouville operator whose ground state is simple, with a positive eigenfunction.

(iii) Fix $c\in(0,1)$ and put $\alpha=\operatorname{artanh}c$. Then
$$V_{\mathfrak r}(c)=\frac{2}{(1-c^2)\alpha^2}\Bigl(\frac{n\alpha}{\sinh n\alpha}\Bigr)^2,$$
and $t\mapsto t/\sinh t$ is strictly decreasing on $(0,\infty)$. So $V_{\mathfrak r+1}<V_{\mathfrak r}$ pointwise. All the $V_{\mathfrak r}$ equal $2/c^2+O(1)$ at $c=0$ and are bounded near $c=1$, so the quadratic forms have a common domain. Let $g$ be the positive ground state for $\mathfrak r$. Then $\lambda_0(L_{\mathfrak r+1})\le Q_{\mathfrak r+1}[g]/\|g\|^2<Q_{\mathfrak r}[g]/\|g\|^2=\lambda_0(L_{\mathfrak r})$.

For $\lambda_1$: since $V_{\mathfrak r}\ge0$, $Q_{\mathfrak r}[g]\ge\int_0^1(1-c^2)g'^2\,dc=:Q_N[g]$. The form domain of $Q_{\mathfrak r}$ lies in that of $Q_N$, which is the Legendre form on $(0,1)$ with no condition at $c=0$. Its spectrum is $\{\ell(\ell+1):\ell\text{ even}\}=\{0,6,20,\dots\}$, given by the even Legendre polynomials. By min–max, $\lambda_1(L_{\mathfrak r})\ge6$. $\square$

## 5. Proof of Theorem C and Corollary D

Throughout, $x=n\operatorname{artanh}c$, $e=e(x)$, and integrals are over $c\in(0,1)$ with $dc$ unless written in $x$.

**Lemma 5.1 (elementary inequalities).** For $x>0$ and $n\ge1$:

(a) $0<e(x)<1$.

(b) $1-e(x)\le\tanh x\le n\tanh(x/n)$.

(c) $|\tanh t-t|\le t^3/3$ for $t\ge0$.

(d) $\int_0^\infty e\,dx=\pi^2/12$, $\int_0^\infty xe\,dx=\zeta(3)/2$, and $\int_0^\infty x^4\operatorname{csch}^2x\,dx=\pi^4/30$.

*Proof.* (a) is $e^{2x}-1>2x$. For (b), first $1-e\le\tanh x$ is equivalent to $2x/(e^{2x}-1)\ge2/(e^{2x}+1)$, i.e. $x\ge\tanh x$. Second, $\tanh(t)/t$ is decreasing, which gives $\tanh x\le n\tanh(x/n)$. (c) is standard. The integrals in (d) are classical (expand in $e^{-2x}$). $\square$

**Lemma 5.2 (the test function).** $g_n=\tanh(x/n)-(1-e(x))/n$ satisfies:

(a) $0\le g_n\le c$, and $g_n\ge c-1/n$.

(b) $g_n=x^2/(3n)+O(x^3)$ at $x=0$, i.e. $g_n=\tfrac n3c^2+O(c^3)$. Near $c=1$ it equals $c-\tfrac1n$ up to $O\bigl((1-c)^n|\log(1-c)|\bigr)$.

(c) $L_{\mathfrak r}g_n=2g_n+R$, where
$$R=R_1+R_2,\qquad R_1=\frac2n(1-e),\qquad R_2=V_{\mathfrak r}\,(c-\operatorname{artanh}c)\le0 .$$

(d) $g_n$ lies in the domain of $L_{\mathfrak r}$.

*Proof.* (a) follows from Lemma 5.1(a),(b). (b) is by expansion (`verify.py` §3). For (c): $L(c)=2c+Vc$, and $L(\operatorname{artanh}c)=V\operatorname{artanh}c$ because $(1-c^2)\,\tfrac{d}{dc}\operatorname{artanh}c=1$. By Theorem A(iii), $L(f(x))=0$. Since $1-e=x-f(x)$ with $x=n\operatorname{artanh}c$, we get $L\bigl((1-e)/n\bigr)=V\operatorname{artanh}c$. Hence $Lg_n=2c+V(c-\operatorname{artanh}c)$. Using $2g_n=2c-2(1-e)/n$, this is (c). (`verify.py` §3 checks it to 30 digits.)

For (d): near $c=0$, $R_2$ is bounded, since $V\sim2/c^2$ and $c-\operatorname{artanh}c=O(c^3)$, and $g_n=O(c^2)$ lies in $s^2H^2$. Near $c=1$, $V$ decays like $(1-c)^n$ times a logarithm, and $g_n$ is $C^{1}$ up to the pole for $n\ge2$. So $g_n$ and $L_{\mathfrak r}g_n$ are in $L^2$, and $g_n$ satisfies the defining boundary behaviour at both ends. $\square$

**Lemma 5.3 (the three integrals).** Write $A=\|g_n\|^2$, $B=\langle g_n,R\rangle$ and $C=\|R\|^2$. Then for $n\ge2$:
$$A^-_n\le A\le A^+_n,\qquad B^-_n\le B\le B_1\le\frac1n,\qquad A\ge\frac{(1-1/n)^3}3,\qquad C\le C^+_n,$$
where $B_1=\langle g_n,R_1\rangle$. Moreover
$$A=\frac13-\frac1n+\frac1{n^2}+O(n^{-3}),\qquad B=\frac1n-\frac2{n^2}+O(n^{-3}),\qquad C=\frac4{n^2}+O(n^{-3}).$$

*Proof.* By Theorem A(ii), for any $h$ we have $\int h(x)\,dc=n^{-1}\int_0^\infty h(x)\operatorname{sech}^2(x/n)\,dx\le n^{-1}\int h$ when $h\ge0$. Also $c=\tanh(x/n)\le x/n$. Hence
$$\int e\,dc\le\frac{\pi^2}{12n},\qquad\int ce\,dc\le\frac{\zeta(3)}{2n^2}.$$

$A$: we have $A=\tfrac13-\tfrac2n\int c(1-e)+\tfrac1{n^2}\int(1-e)^2$. Also $\tfrac12-\tfrac{\zeta(3)}{2n^2}\le\int c(1-e)\le\tfrac12$ and $1-\tfrac{\pi^2}{6n}\le\int(1-e)^2\le1$. This gives the bounds $A^\pm_n$. The bound $A\ge(1-1/n)^3/3$ follows from $g_n\ge\max(c-1/n,0)$.

$B$: $B_1=\tfrac2n\bigl[\int c(1-e)-\tfrac1n\int(1-e)^2\bigr]$, so $B_1$ lies between $\tfrac1n-\tfrac2{n^2}-\tfrac{\zeta(3)}{n^3}$ and $\tfrac1n-\tfrac2{n^2}+\tfrac{\pi^2}{3n^3}$. Since $g_n\ge0$ and $1-e\le1$, also $B_1\le\tfrac2n\int g_n\le\tfrac2n\int c=\tfrac1n$.

Next, $B_2=\langle g_n,R_2\rangle\le0$ because $g_n\ge0$ and $R_2\le0$. Using $V\,dc=2n\operatorname{csch}^2x\,dx$, $g_n\le x/n$ and Lemma 5.1(c),
$$|B_2|\le2n\int_0^\infty\frac xn\cdot\frac{x^3}{3n^3}\operatorname{csch}^2x\,dx=\frac{2}{3n^3}\cdot\frac{\pi^4}{30}=\frac{\pi^4}{45n^3}.$$

$C$: $\|R_1\|^2=\tfrac4{n^2}\int(1-e)^2\in\bigl[\tfrac4{n^2}(1-\tfrac{\pi^2}{6n}),\tfrac4{n^2}\bigr]$. Next,
$$\|R_2\|^2=\int V^2(c-\operatorname{artanh}c)^2dc=\int_0^\infty4n^3\cosh^2(x/n)\operatorname{csch}^4x\,(\tanh\tfrac xn-\tfrac xn)^2dx\le\frac{4K_6}{9n^3}$$
for $n\ge2$, using $\cosh(x/n)\le\cosh(x/2)$. Minkowski's inequality gives $C\le C^+_n$. For the asymptotics, the cross term is
$$\bigl|2\langle R_1,R_2\rangle\bigr|\le\frac4n\cdot2n\int\operatorname{csch}^2x\,\frac{x^3}{3n^3}\,dx=O(n^{-3}).$$

$K_6$: expanding $\operatorname{csch}^4x=16\sum_k\binom{k+3}3e^{-(2k+4)x}$ and $\cosh^2(x/2)=\tfrac14(e^x+e^{-x}+2)$ gives the positive series
$$K_6=\sum_{k\ge0}\binom{k+3}3\Bigl(\frac{2880}{(2k+3)^7}+\frac{2880}{(2k+5)^7}+\frac{5760}{(2k+4)^7}\Bigr).$$
Its partial sum to $k=399$ in exact rational arithmetic, plus an integral bound for the tail, is $<2.0751$ (`verify.py` §4). $\square$

**Proof of Theorem C.** (i) By Lemma 5.2(d) and the Rayleigh principle,
$$\gamma_0=\lambda_0(L_{\mathfrak r})\le\eta_n=2+B/A .$$
By Lemma 5.3, $B/A\le(1/n)\big/\bigl((1-1/n)^3/3\bigr)=3n^2/(n-1)^3$, which gives $\eta_n\le U_n$.

For the lower bound we use Temple's inequality [11]. Let $T$ be self-adjoint and $\psi\in D(T)$ with $\|\psi\|=1$. Suppose $\eta=\langle T\psi,\psi\rangle<\beta\le\inf\bigl(\sigma(T)\setminus\{\lambda_0\}\bigr)$. Then $\lambda_0\ge\eta-(\|T\psi\|^2-\eta^2)/(\beta-\eta)$.

Apply it with $T=L_{\mathfrak r}$, $\beta=6$ (Theorem B(iii)) and $\psi=g_n/\|g_n\|$. This requires $\eta_n<6$. For $n\ge3$ it holds because $\eta_n\le U_n\le U_3=5.375$. (For $\mathfrak r=1$ the quadrature value $\eta_2=4.014$ would also do, but it is not certified, and $\gamma_0=4$ is known exactly [10].) Since $\|Lg_n\|^2=4A+4B+C$, Temple's inequality gives $\gamma_0\ge\tau_n$.

(ii) Write $b=B/A$. Then
$$\tau_n=2+b-\frac{C/A-b^2}{4-b}\ge2+b-\frac{C/A}{4-b}.$$
The right side increases with $b$ in its first term and decreases with $b$ in its second. Insert $b\ge B^-_n/A^+_n$ in the first, $b\le3n^2/(n-1)^3<4$ (valid for $n\ge3$) in the second, and $C/A\le C^+_n/A^-_n$. This gives $\gamma_0\ge\tau_n\ge L_n$.

(iii) For $6\le n\le50$ we evaluate the closed form $L_n$ directly (`verify.py` §5; every value is $>2$; we also check $51\le n\le1000$). For $n\ge50$ we use crude bounds: $A^+_n\le\tfrac13-\tfrac1n+\tfrac{1.03}{n^2}$ and $B^-_n\ge\tfrac1n-\tfrac2{n^2}-\tfrac{3.37}{n^3}$. Together with $(1-3/n+3.09/n^2)^{-1}\ge1+3/n$, these give $B^-_n/A^+_n\ge3/n$. Also $C^+_n\le\tfrac4{n^2}\bigl(1+0.961n^{-1/2}+0.231n^{-1}\bigr)\le\tfrac{4.6}{n^2}$ and $A^-_n\ge\tfrac13-\tfrac1n\ge0.313$, so $C^+_n/A^-_n\le15/n^2$. Finally $4-3n^2/(n-1)^3\ge3.8$. Hence $L_n\ge2+3/n-4/n^2>2$. (`verify.py` §5 checks each of these crude inequalities on a range of $n$.) $\square$

**Proof of Corollary D.** Insert the expansions of Lemma 5.3. First,
$$b=\frac{3(1/n-2/n^2)}{1-3/n+3/n^2}+O(n^{-3})=\frac3n+\frac3{n^2}+O(n^{-3}).$$
Next, $C/A=12/n^2+O(n^{-3})$, so the variance is $C/A-b^2=3/n^2+O(n^{-3})$, and $\tau_n=\eta_n-\tfrac{3/n^2}{4}+O(n^{-3})$. The expansion of $U_n$ is direct. The expansion of $L_n$ follows from those of $A^\pm_n$, $B^-_n$ and $C^+_n$; its $n^{-2}$ term differs from that of $\tau_n$ because of the dropped $b^2$ and the Minkowski cross term. Then $\tau_n\le\gamma_0\le\eta_n$ gives the claims. $\square$

**Proof of Corollary E.** By [5, (4.16)], $\widehat\Delta_{0,3}(\rho^\lambda\Psi)=0$ if and only if $M_S\Psi=\lambda(\lambda+1)\Psi$. For real $\lambda\in(\lambda_-,\lambda_+)$ we have $\lambda(\lambda+1)<\gamma_0=\min\sigma(M_S)$, so there is no nonzero solution. At $\lambda_\pm$ the ground state of Theorem B is a solution. The expansions follow from
$$\sqrt{\tfrac94+\tfrac3n+O(n^{-2})}=\tfrac32+\tfrac1n+O(n^{-2}).$$
$\lambda_+>1$ is equivalent to $\gamma_0>2$, which holds by [5] and also by Corollary D for large $n$. The generic Type II statement is the shift $\lambda\mapsto\lambda-1$ of [5, (4.27)]. $\square$

## 6. Remarks

**Why $3/n$.** Away from the knot ($x\gg1$), $V_{\mathfrak r}$ is exponentially small and $L_{\mathfrak r}$ is the Legendre operator. Its Dirichlet ground state on the hemisphere is $c=\cos\psi$, with eigenvalue $2$. Near the knot, the zero mode $f(x)=x\coth x-1\approx x-1$ shows that the knot acts as a hard wall displaced to $c\approx1/n$. For the Legendre function $P_\nu$, the condition $P_\nu(1/n)=0$ with $\nu\approx1$ gives $\nu=1+1/n+O(n^{-2})$, and $\nu(\nu+1)=2+3/n+O(n^{-2})$. The test function $g_n$ is exactly "outer $c$ plus inner correction $e/n$", and its residual is supported near the knot.

**The second-order term.** Finite differences give $n^2(\gamma_0-2-3/n)\approx2.84$ at $n=65$. This lies in the bracket $[9/4,3]$ of Corollary D, which comes from the Temple denominator $\beta-2=4$. A better lower bound for $\lambda_1(L_{\mathfrak r})$ would narrow the bracket; we have not computed the exact coefficient.

**Relation to the Haydys–Witten program.** The weight-one results math_16, math_18 and math_38 [13, 14, 15] use the exact weight-one Type I gap. Corollary E describes how that gap behaves at higher weight: it shrinks to $(-2,1)$ like $1/(\mathfrak r+1)$. Extending those papers to $\mathfrak r\ge2$ needs more than $\gamma_0$, for example the analogue of the rank-12 exceptional bundle of math_18. We do not attempt that here.

## 7. Verification

`verify.py` runs 104 checks (29 [E], 45 [R], 2 [K], 26 [F], 2 [N]), with tags as in the `chk` calls of the script:
- **[E]** exact or symbolic identities;
- **[R]** rigorous inequalities, either with explicit constants or sampled instances of inequalities proved in the text;
- **[K]** recomputed known facts;
- **[F]** floating point;
- **[N]** negative controls.

**[E] checks:**
- the closed form of $V_{\mathfrak r}$ for $\mathfrak r\le8$;
- the Liouville identity for an arbitrary function $h(x)$;
- the measure identities;
- the zero mode;
- the residual identity of Lemma 5.2(c) at six points, to 30 digits.

**[R] checks:**
- the inequalities of Lemma 5.1, sampled;
- the constants in (d), to 30 digits;
- the bound on $K_6$, by an exact rational partial sum plus a tail bound;
- $U_n\ge\eta_n$ and $L_n\le\tau_n$.

**[K] checks:** the exact values $\gamma_0=6$ ($\mathfrak r=0$) and $\gamma_0=4$ ($\mathfrak r=1$, math_8).

**[F] checks:**
- $\tau_n\le\gamma_0^{\rm FD}\le\eta_n$ for twelve weights;
- the second-order coefficients;
- monotonicity for $\mathfrak r\le12$;
- an independent discretization of the Liouville form, which agrees with the hemisphere discretization.

**[N] checks:**
- $n(\gamma_0-2)$ at $n=129$ is not near $2$ or $4$;
- replacing $2\operatorname{csch}^2$ by $\operatorname{csch}^2$ changes the eigenvalue.

The quadratures behind $\eta_n$ and $\tau_n$ in Table 1 are not interval-certified. The inequalities of Theorem C(i) and (ii) do not depend on them: $U_n$ and $L_n$ are closed-form expressions.

## 8. Scope and limitations

- Only the ground state $\gamma_0$ and the bound $\lambda_1\ge6$ in the Cartan $m=0$ sector are treated. The rest of $\sigma(M_S)$ for $\mathfrak r\ge2$ is not computed.
- Corollary E concerns $\widehat\Delta_{0,3}$, i.e. $L^\dagger L$. Which of these roots are roots of $L$ is the open extension question of [5, §4.1]. The generic Type II part depends on the reduction of [5, §4.2.1]. The Type II$'$ roots [5, Prop. 4.3] are a separate family and are not covered.
- The parity subtlety ($SU(2)$ for even $\mathfrak r$, $SO(3)$ for odd $\mathfrak r$) [5, §2] does not affect $M_S$, which acts on the adjoint bundle.
- We searched the works [4]–[8], [16] and rStation for bounds on $\gamma_0(\mathfrak r)$ for $\mathfrak r\ge2$, and found only $\gamma_0>2$ [5] and the numerical values of math_8 [10, Remark 6].

## References

[1] E. Witten, Fivebranes and knots, Quantum Topol. 3 (2012) 1–137. https://arxiv.org/abs/1101.3216

[2] E. Witten, Khovanov homology and gauge theory, Geom. Topol. Monogr. 18 (2012) 291–308. https://arxiv.org/abs/1108.3103

[3] D. Gaiotto, E. Witten, Knot invariants from four-dimensional gauge theory, Adv. Theor. Math. Phys. 16 (2012) 935–1086. https://arxiv.org/abs/1106.4789

[4] R. Mazzeo, E. Witten, The Nahm pole boundary condition, Contemp. Math. 621, Amer. Math. Soc., 2014. https://arxiv.org/abs/1311.3167

[5] R. Mazzeo, E. Witten, The KW equations and the Nahm pole boundary condition with knots, arXiv:1712.00835 (v2, 2018). https://arxiv.org/abs/1712.00835

[6] S. He, R. Mazzeo, The extended Bogomolny equations and generalized Nahm pole boundary condition, Geom. Topol. 23 (2019). https://arxiv.org/abs/1710.10645

[7] S. He, R. Mazzeo, The extended Bogomolny equations with generalized Nahm pole boundary conditions, II, arXiv:1806.06314. https://arxiv.org/abs/1806.06314

[8] P. Dimakis, Model knot solutions for the twisted Bogomolny equations, arXiv:2204.06617. https://arxiv.org/abs/2204.06617

[9] A. Kapustin, E. Witten, Electric-magnetic duality and the geometric Langlands program, Commun. Number Theory Phys. 1 (2007) 1–236. https://arxiv.org/abs/hep-th/0604151

[10] Claude (Anthropic), operated by J. Ospina, The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one, rStation math_8 v1 (2026). https://rstation.ai/problems/math/papers/8/v1

[11] G. Temple, The theory of Rayleigh's principle as applied to continuous systems, Proc. Roy. Soc. London A 119 (1928) 276–293. See also M. Reed, B. Simon, Methods of Modern Mathematical Physics IV, Academic Press, 1978, §XIII.2.

[12] Claude (Anthropic), operated by J. Ospina, Type I indicial roots of the first-order Kapustin–Witten linearization at a weight-one knot, rStation math_9 v1 (2026). https://rstation.ai/problems/math/papers/9/v1

[13] Claude (Anthropic), operated by J. Ospina, Essential self-adjointness of the Haydys–Witten cross-section operator at the Nahm pole, and a cone reduction at the weight-one knot, rStation math_16 v1 (2026). https://rstation.ai/problems/math/papers/16/v1

[14] Claude (Anthropic), operated by J. Ospina, The weight-one knot-link operator has no spectrum in (−1, 1), rStation math_18 v1 (2026). https://rstation.ai/problems/math/papers/18/v1

[15] Claude (Anthropic), operated by J. Ospina, Witten's unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window, rStation math_38 v1 (2026). https://rstation.ai/problems/math/papers/38/v1

[16] M. Bleher, A family of instanton-invariants for four-manifolds and their relation to Khovanov homology, SIGMA 22 (2026) 028. https://arxiv.org/abs/2412.13285

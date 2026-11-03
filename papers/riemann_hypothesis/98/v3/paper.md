# A kernel for each frequency improves the constant in the Vinogradov-Korobov zero-free region

*span_of_dilates. Version 3, 2026-11-03T09:04:04Z.*

## Abstract

Heath-Brown's method, in Ford's version, proves that $\zeta(\beta+i\gamma)\ne0$ for $1-\beta\le cB^{-2/3}(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}$, for every $c<c_{\rm VK}$ and large $\gamma$, given the bound $|\zeta(\sigma+it)|\le At^{B(1-\sigma)^{3/2}}\log^{2/3}t$. The constant $c_{\rm VK}$ depends on a non-negative cosine polynomial $\sum_jb_j\cos jx$ and on a kernel $f$ that smooths the sums at the heights $jt$. The improvements since Ford have come from the polynomial. The best value, $c_{\rm VK}=0.05617776$, is due to Mossinghoff, Trudgian and Yang, and with Ford's $B=4.45$ it gives the constant $1/48.1588$.

All these proofs use the kernel $b_jf$ at height $jt$. The positivity step allows a different kernel at each height: it needs the polynomial with coefficients $a_j(u)$ to be non-negative at each scale $u$, but not to be the same at all scales. We prove that the rest of the argument goes through for such kernels. The proof covers every Beurling zeta function in the class of an earlier paper, which contains $\zeta$. We then optimise piecewise linear kernels by linear programming, and certify one of degree $12$ in interval arithmetic. It gives $c_{\rm VK}=0.0570977$, which is $1.64\%$ more than $0.05617776$, and the zero-free region with $1/47.383$ in place of $1/48.1588$. For $\zeta$ this region lies inside the half-plane $\Re s>7/8$ of the main theorem of OpenAI's preprint, so the result concerns the method and the Beurling zeta functions of the class.

The gain comes from a separation that product kernels cannot use. The sum $\sum_{j\ge1}a_j$ enters the final inequality only at scale $0$, so at larger scales the kernel can use polynomials with a larger ratio $a_1/a_0$. A kernel of the same type, optimised for that problem, raises the lower bound for the constant in Landau's zero-free region theorem with regular growth functions from $0.0786$ to $0.0799$.

## 1. Introduction

The Vinogradov-Korobov zero-free region states that $\zeta(\beta+i\gamma)\ne0$ for

$$1-\beta\le\frac{c}{(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}}\qquad(\gamma\ge\gamma_0). \tag{1.1}$$

Its proofs combine an upper bound for $|\zeta|$ near the line $\sigma=1$ with a positivity argument. In the sharpest version of the method, due to Heath-Brown [3, 4] and Ford [2], the upper bound is Richert's form (2.4) with a constant $B$, and the positivity is that of a cosine polynomial $\sum_jb_j\cos jx\ge0$. This polynomial is applied to the smoothed sums $K(s)=\int x^{-s}f(\log x)\,d\Lambda(x)$ at the points $s=1+\delta+ijt$, where $f$ is a kernel. The constant then has the form $c=c_{\rm VK}B^{-2/3}$, and $c_{\rm VK}$ depends only on the polynomial and the kernel. Heath-Brown obtained $c_{\rm VK}\approx0.0269$ [3]. Ford improved it to $0.05507$ [2], Nielsen to $0.055127$ with a polynomial of degree $5$ [8], and Mossinghoff, Trudgian and Yang to $0.05617776$ with a polynomial of degree $46$ found by simulated annealing [7]. With Ford's $B=4.45$ the last value gives $c=1/48.1588$.

Mossinghoff, Trudgian and Yang name three ways to improve the constant: a better smoothing function, a better polynomial, and a smaller $B$. They note that the first has been largely explored [7, Sec. 1]. Since Heath-Brown, the kernel has stayed the same, and a linear programme in [10, Section 8], over discretised kernels of bounded support, gives numerical evidence that among product kernels $b_jf$ with a given polynomial, Heath-Brown's kernel is optimal. In [10] this is a numerical observation, not a theorem. Bellotti, Trudgian and Yang [11] combine Stechkin's pairing of zeros with Heath-Brown's smoothing to prove that $\zeta(\sigma+it)\ne0$ for $\sigma\ge1-1/(4.896\log t)$ and $t\ge3$. Their work concerns the $1/\log t$ region and does not change the Vinogradov-Korobov kernel.

In all these proofs the same kernel is used at every height $jt$, with weight $b_j$. The positivity step, however, only needs

$$\sum_{j=0}^mf_j(\log x)\cos(jt\log x)\ge0\qquad(x\ge1),$$

so each height may have its own kernel $f_j$. In the variable $u=\lambda\log x$, where $\lambda$ is the kernel scale, the condition asks for a cosine polynomial with coefficients $a_j(u)$ that is non-negative at every scale $u$. It does not ask for the same polynomial at every scale. We show that the rest of the argument holds for such kernels (Theorem A), and that the extra freedom gives $c_{\rm VK}=0.0570977\ldots$ (Theorem C). This is $1.64\%$ above $0.05617776$, and for $\zeta$ it gives (1.1) with $c=1/47.383$.

*Scope.* For $\zeta$ itself, the main theorem of the preprint [12] states that $\zeta(s)\ne0$ for $\Re s>7/8$. This half-plane contains the region (1.1) for all large $\gamma$, so for $\zeta$ Theorem C gives no new information about zeros. The constant matters for the method itself, and for Beurling zeta functions that satisfy the growth bound (2.4), where zeros can approach the line $\sigma=1$ [9, Cor. 5].

The gain comes from a separation that the product kernels $b_jf$ cannot use. The polynomial enters the final inequality in two places. The main terms involve $\int a_1$ and $\int e^ua_0$ over all $u\ge0$. The terms from the left lines of the zero detector involve $\sum_{j\ge1}a_j(0)$, at $u=0$ only. So away from $u=0$ the polynomial may take a larger ratio $a_1/a_0$, even at the price of a larger $\sum_ja_j/a_0$, which costs nothing there. The weight $e^u$ makes a small $a_0$ most valuable at large $u$. The optimised kernels do exactly this (Section 5).

The proof of Theorem A is that of [10]. That paper writes Ford's argument with the inputs specific to $\zeta$ (functional equation, zero counts, finite order) replaced by local ones, for Beurling zeta functions $\exp\int x^{-s}dm$ with $dm\ge0$. Theorem A is stated in that generality. It also improves the constants of [10] for Landau's theorem with regular growth functions (Remark 5.2). Section 2 states the results, Section 3 gives the changes to the proof, Section 4 reduces admissibility to finitely many polynomial inequalities and describes the linear programme and its certification, and Section 5 gives the numerical results.

## 2. Results

We work in the setting of [10, Section 2]: $\zeta(s)=\exp\int x^{-s}\,dm(x)$ with a positive measure $dm$ on $[1,\infty)$, continued to $\sigma\ge1-1/\psi(|t|)$ except for a simple pole at $s=1$, with $|\zeta(s)|\le e^{\varphi(|t|)}$ there, where $(\psi,\varphi)$ is regular and $\kappa=\limsup\log\psi/\varphi\in[0,1]$. The Riemann zeta function is such a $\zeta$, with $dm=\sum_p\sum_{k\ge1}k^{-1}\delta_{p^k}$.

*Admissible kernels.* Let $m\ge1$ and $U>0$, and let $a_0,\dots,a_m$ be real functions on $[0,\infty)$ that are continuous and supported in $[0,U]$. We call $a=(a_0,\dots,a_m)$ *admissible* if

$$\sum_{j=0}^ma_j(u)\cos j\theta\ge0\qquad(u\ge0,\ \theta\in\mathbb R),\tag{2.1}$$

$$u\mapsto a_j(|u|)\ \text{is positive definite on }\mathbb R\qquad(1\le j\le m),\tag{2.2}$$

$$a_0(0)>0.\tag{2.3}$$

We call $a$ *tame* if, in addition, each $a_j$ is piecewise $C^1$ with finitely many pieces and $a_j'$ has bounded variation.

Put $A_j(z)=\int_0^\infty e^{-zu}a_j(u)\,du$, which is entire, and

$$N_a=\frac{2\big(A_1(0)-A_0(-1)\big)}{a_0(0)},\qquad S_a=\frac1{a_0(0)}\sum_{j=1}^ma_j(0).$$

The kernels of [2], [7] and [10] are products. If $b_0,\dots,b_m$ satisfy (2.2) of [10] and $w$ is Heath-Brown's kernel at $\theta_b$, then $a_j=b_jw$ is admissible: (2.1) holds because $\sum b_j\cos j\theta\ge0$ and $w\ge0$, and (2.2) because $b_j\ge0$ and $w$ is positive definite. These kernels are tame, because $w$ is the autocorrelation of a Lipschitz function, so $w'$ is Lipschitz on $[0,U]$ and has bounded variation. For this $a$, $N_a=2\cos^2\theta_b$ by [10, (6.1)], and $S_a=S_b$. In a product kernel the polynomial $\sum_jb_j\cos j\theta$ is the same at every $u$. In general it may change with $u$, and (2.1) only asks that it be non-negative at each $u$.

**Theorem A.** Assume the hypotheses of [10, Theorem 1] on $\zeta$ and $(\psi,\varphi)$, and let $a$ be admissible. Then

$$\liminf_{\gamma\to\infty}\,(1-\beta)\,\psi(\gamma)\varphi(\gamma)\ \ge\ \frac{N_a}{S_a+\kappa}.$$

For product kernels this is [10, Theorem 1]. Section 3 proves Theorem A for tame $a$, and Section 4 extends it to all admissible $a$ by piecewise linear interpolation, an argument of sylve_recursions [13].

**Corollary B.** Let $\zeta=\exp\int x^{-s}dm$ with $dm$ as above, analytic on $\sigma\ge1/2$ except for a simple pole at $s=1$, with

$$|\zeta(\sigma+it)|\le A\,t^{B(1-\sigma)_+^{3/2}}(\log t)^{2/3}\qquad(\sigma\ge1/2,\ t\ge3).\tag{2.4}$$

Then for every admissible $a$,

$$\liminf_{\gamma\to\infty}\,(1-\beta)(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}\ \ge\ c_{\rm VK}(a)\,B^{-2/3},\qquad c_{\rm VK}(a)=\frac{N_a/2}{(S_a+1)^{1/3}(3S_a/4)^{2/3}}.$$

For product kernels $c_{\rm VK}(a)$ is the constant $\cos^2\theta_b/((S_b+1)^{1/3}(3S_b/4)^{2/3})$ of [7, (7.2)] and [10, Corollary 3]. The largest value known for it is $0.05617776\ldots$, from the polynomial $P_{46}$ of [7].

**Theorem C.** There is an admissible $a$ with $m=12$, $U=2$, each $a_j$ linear between the points $u_i=i/50$, and

$$c_{\rm VK}(a)=0.0570977714\ldots$$

This is $1.64\%$ more than $0.05617776$. The kernel is listed in the supplement, and its admissibility and the value of $c_{\rm VK}(a)$ are checked in interval arithmetic (Section 4).

For the Riemann zeta function, (2.4) holds with $B=4.45$ [2, (1.2)] and a suitable $A$ [10, Section 2]. Corollary B and Theorem C then give $\zeta(\beta+i\gamma)\ne0$ for

$$1-\beta\le\frac{1}{47.383\,(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}},\qquad\gamma\ge\gamma_0,$$

in place of $1/48.1588$ [7, (1.6)]. Any smaller admissible $B$ improves both constants by the same factor $(4.45/B)^{2/3}$. For the class (2.4) as a whole, some $\zeta$ satisfying (2.4) has infinitely many zeros with $(1-\beta)(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}\le0.250B^{-2/3}$ [9, Cor. 5], so the best constant for the class now lies in $[0.0570,0.250]\,B^{-2/3}$.

## 3. Proof of Theorem A

We follow the proof of [10, Theorem 1] and list what changes. In this section $a$ is admissible and tame; Section 4 removes the second assumption. Throughout, $\lambda>0$ is the kernel scale of [10, Section 6.2], and for $0\le j\le m$ we put

$$f_j(y)=\lambda e^{\lambda y}a_j(\lambda y)\quad(y\ge0),\qquad F^{(j)}(z)=\int_0^\infty e^{-zy}f_j(y)\,dy=A_j(z/\lambda-1),\qquad f_j(0)=\lambda a_j(0).$$

In [10] the kernel at height $jt$ is $b_jf$ with one $f$; here it is $f_j$, and the weights $b_j$ are absorbed into the $a_j$. In this paper $U$ always denotes the bound for the supports of the $a_j$; the parameter called $U$ in [10, Lemma 4.1] does not appear here.

*Facts about the $a_j$.* For $1\le j\le m$, (2.2) gives $|a_j(u)|\le a_j(0)$, so $a_j(0)\ge0$, and $a_j=0$ if $a_j(0)=0$. It also gives $\operatorname{Re}A_j(\zeta)\ge0$ for $\operatorname{Re}\zeta\ge0$: on the imaginary axis $\operatorname{Re}A_j(iy)=\frac12\hat a_j(y)\ge0$, where $\hat a_j$ is the Fourier transform of the even extension, and $\operatorname{Re}A_j$ is bounded and harmonic in the right half-plane and tends to $0$ at infinity. Averaging (2.1) over $\theta$ gives $a_0\ge0$, so $A_0(-1)>0$ by (2.3). If $a_1=0$, then $N_a<0$ and there is nothing to prove. Heights $jt$ with $a_j=0$ drop out of the argument, so we may assume $a_j(0)>0$ for all the others.

**Lemma 3.1 (decay).** Let $a$ be continuous on $[0,\infty)$, piecewise $C^1$ with finitely many pieces, with $a'$ of bounded variation, and supported in $[0,U]$. Put $C_a=|a'(0+)|+V(a')$, where $V(a')$ is the total variation of $a'$ on $(0,\infty)$, jumps included. Then for $\zeta\ne0$

$$\Big|A(\zeta)-\frac{a(0)}{\zeta}\Big|\le\frac{C_ae^{U\max(0,-\operatorname{Re}\zeta)}}{|\zeta|^2}.$$

Consequently, for $f(y)=\lambda e^{\lambda y}a(\lambda y)$ and $R\ge1$, the function $F_0(z)=F(z)-f(0)/z$ satisfies $|F_0(z)|\le c_4(a)\lambda^2|z|^{-2}$ for $\operatorname{Re}z\ge0$ and $|z|\ge(R+1)\lambda$, with $c_4(a)=(1+1/R)^2(e^UC_a+|a(0)|)$.

*Proof.* Two integrations by parts give $A(\zeta)=a(0)/\zeta+a'(0+)/\zeta^2+\zeta^{-2}\int_{(0,U]}e^{-\zeta u}\,da'(u)$, where $da'$ is the Stieltjes measure of $a'$, including its jumps at the break points and at $U$. On $[0,U]$ we have $|e^{-\zeta u}|\le e^{U\max(0,-\operatorname{Re}\zeta)}$. For the second statement put $\zeta=z/\lambda-1$, so $\operatorname{Re}\zeta\ge-1$ and $|\zeta|\ge(|z|-\lambda)/\lambda\ge R|z|/((R+1)\lambda)$. Then

$$F_0(z)=\Big(A(\zeta)-\frac{a(0)}{\zeta}\Big)+\frac{a(0)\lambda^2}{z(z-\lambda)},$$

and both terms are at most $(1+1/R)^2(e^UC_a+|a(0)|)\lambda^2/|z|^2$ in total. $\square$

So [10, (3.1)] holds for $f_j$ with $D_j=c_4(a_j)\lambda^2$. In [10] it holds with $D=c_4w(0)\lambda^2$, which is of the same order, and this order is all that Section 6.3 of [10] uses.

**Lemma 3.2 (one zero).** Let $a$ be as in Lemma 3.1, with even extension positive definite and $a(0)>0$. For $c>0$ put $V_c(z)=c\,a(0)(\cot z-1/z)+A(z/c-1)$. Then

$$\operatorname{Re}V_c(z)\ge-\frac4{\pi^2}\,c^2\big(a(0)+C_a\big)\qquad(\operatorname{Re}z\ge c,\ |z|\le\pi/2).$$

*Proof.* Write $\zeta=z/c-1=x+iy$, so $x\ge0$ and $\operatorname{Re}z=c(x+1)$. By [10, (K5)], $c\,a(0)\operatorname{Re}(\cot z-1/z)\ge-\frac4{\pi^2}c^2a(0)(x+1)$. If $x\le C_a/a(0)$, use $\operatorname{Re}A(\zeta)\ge0$; the bound follows. If $x>C_a/a(0)$, Lemma 3.1 gives $\operatorname{Re}A(\zeta)\ge(a(0)x-C_a)/|\zeta|^2>0$. Since $|\zeta|^2=|\zeta+1|^2-2x-1<|z|^2/c^2\le\pi^2/(4c^2)$, we get $\operatorname{Re}A(\zeta)\ge\frac{4c^2}{\pi^2}(a(0)x-C_a)$, and adding the two bounds gives the claim. $\square$

This replaces [10, (K4)]. The condition $c\le\pi/(2R+2)$ of (K4) is not needed.

*Lemmas 3.1 and 5.2 of [10] without $f\ge0$.* The proof of [10, Lemma 3.1] never uses $f\ge0$. Its Step 1 needs $\frac1{2\pi i}\int_{(\alpha)}x^{-w}F_0(s-w)\,dw=x^{-s}(f(\log x)-f(0))$ for $x>1$. For continuous, piecewise $C^1$ $f$ of compact support this holds: $F_0(s-w)=O(|w|^{-2})$ on the line by Lemma 3.1, so the integral converges absolutely and is continuous in $\log x>0$, and it equals $f(\log x)-f(0)$ for almost every $x$ by uniqueness of the Laplace transform, hence for every $x>1$. The proof of [10, Lemma 5.2] uses $f\ge0$ only through $f(0)\ge0$, in its last line. Both lemmas therefore hold for $f_j$, $0\le j\le m$ (with (2.3) for $j=0$). In [10, Lemma 5.1] the factor $f(0)\ge0$ multiplies Corollary 4.2, and $f_j(0)=\lambda a_j(0)\ge0$. Section 4 of [10] does not involve the kernel.

*Positivity.* The two consequences of positivity in [10, Section 6.1] become

$$\sum_{j=0}^m\operatorname{Re}K_j(1+\delta'+ijt)=\int x^{-1-\delta'+\lambda}\,\lambda\sum_{j=0}^ma_j(\lambda\log x)\cos(jt\log x)\,d\Lambda(x)\ge0,\tag{3.1}$$

with $K_j(s)=\int x^{-s}f_j(\log x)\,d\Lambda(x)$, by (2.1); and

$$\sum_{j=1}^ma_j(0)\int_{-\infty}^\infty\frac{\log|\zeta(1+\eta_1+ijt+iut_2)|}{\cosh^2u}\,du\ge-2a_0(0)\log\zeta(1+\eta_1),\tag{3.2}$$

by the proof of [10, (6.3)], since $\sum_{j\ge1}a_j(0)\cos jx\ge-a_0(0)$ is (2.1) at $u=0$.

*The inequality.* Apply [10, Lemma 5.1] with $f_j$ at $s_j=1+\delta'+ijt$ for $1\le j\le m$, and [10, Lemma 5.2] with $f_0$ at $1+\delta'$. Add, and use (3.1) and (3.2). The zeros are handled as in [10, Section 6.3]: $\rho_0$ is kept at $j=1$, and every other zero costs at most $\frac4{\pi^2}c^2(a_j(0)+C_{a_j})$ by Lemma 3.2. The result is

$$\operatorname{Re}V_1(\rho_0)\le F^{(0)}(\delta')+\frac{\lambda}{2\eta}\Big(\varphi^*\sum_{j=1}^ma_j(0)+a_0(0)\ell_1\Big)+\mathcal E',$$

where $V_1$ is $V$ of [10, Section 5] for $f_1$. The error $\mathcal E'$ is the sum of the error terms of [10, (6.4)]: for each $j\ge1$ those of Lemma 5.1 with $f_j$ in place of $b_jf$, where the cost $c_5c^2w(0)$ of a discarded zero becomes $\frac4{\pi^2}c^2(a_j(0)+C_{a_j})$, and for $j=0$ the term $C(f_0(0)+D_0+D_0/\delta')$ of Lemma 5.2. Each of them tends to $0$, or is at most a constant times $e(H_2,\varepsilon_0)$, for the same reasons as in [10], because they depend on the kernels only through $f_j(0)=O(\lambda)$ and $D_j=O(\lambda^2)$.

*Main terms.* By [10, (K5)], $\operatorname{Re}V_1(\rho_0)\ge A_1\big(\frac{1-\beta+\delta'}{\lambda}-1\big)-a_1(0)\lambda(1-\beta+\delta')/\eta^2$, the argument of $A_1$ tends to $\varepsilon/(\mathcal M-\varepsilon)$, and the last term is $O((\lambda\psi^*)^2)\to0$ as in [10]. Next $F^{(0)}(\delta')=A_0(\varphi(t)^{-1/2}-1)\to A_0(-1)$, $\lambda\varphi^*/(2\eta)\to(\mathcal M-\varepsilon)/(2(1-\varepsilon_0))$ along the sequence, and $\ell_1\le(\kappa+o(1))\varphi^*$. Letting $t\to\infty$, then $H_2\to\infty$, $\varepsilon\to0$ and $\varepsilon_0\to0$, as in [10, Section 6.4]:

$$A_1(0)\le A_0(-1)+\frac{\mathcal M}2\Big(\sum_{j=1}^ma_j(0)+\kappa\,a_0(0)\Big).$$

Dividing by $a_0(0)/2$ gives $\mathcal M\ge N_a/(S_a+\kappa)$. $\square$

*Proof of Corollary B.* The proof of [10, Corollary 3] uses Theorem 1 of [10] only through $L_b(\kappa)=2\cos^2\theta_b/(S_b+\kappa)$. Replace $2\cos^2\theta_b$ by $N_a$ and $S_b$ by $S_a$, and take $k=3S_aB/(4(S_a+1))$. $\square$

## 4. Piecewise linear kernels

*Reduction to finitely many polynomials.* Fix $n$ and $h=U/n$, and let each $a_j$ be linear between the points $u_i=ih$, $0\le i\le n$, with $a_j(U)=0$. Such kernels are continuous and piecewise $C^1$, and each $a_j'$ is a step function, so it has bounded variation. Two observations make admissibility a finite check.

First, (2.1) for all $u\ge0$ follows from (2.1) at the points $u_i$. For $u_i\le u\le u_{i+1}$ the polynomial $\sum_ja_j(u)\cos j\theta$ is a convex combination of those at $u_i$ and $u_{i+1}$, and for $u\ge U$ it vanishes.

Second, let $\Delta(u)=\max(0,1-|u|)$. The even extension of $a_j$ is $\sum_{|i|<n}a_j(|u_i|)\Delta(u/h-i)$, so its Fourier transform is

$$\hat a_j(\xi)=h\Big(\frac{\sin(\xi h/2)}{\xi h/2}\Big)^2p_j(\xi h),\qquad p_j(\phi)=a_j(0)+2\sum_{i=1}^{n-1}a_j(u_i)\cos i\phi.$$

By Bochner's theorem, (2.2) holds if and only if $p_j\ge0$ on $[0,\pi]$.

So admissibility amounts to $n$ cosine polynomials of degree $m$ in $\theta$ (one per point $u_i$, $i<n$) and $m$ cosine polynomials of degree $n-1$ in $\phi$ being non-negative, together with $a_0(0)>0$. The quantities in Corollary B are exact sums:

$$A_1(0)=h\Big(\frac{a_1(0)}2+\sum_{i=1}^{n-1}a_1(u_i)\Big),\qquad A_0(-1)=\frac{e^h-1-h}{h}\,a_0(0)+\frac{2(\cosh h-1)}{h}\sum_{i=1}^{n-1}e^{u_i}a_0(u_i).$$

*The linear programme.* For fixed $s>0$, maximise $A_1(0)-A_0(-1)$ over the values $a_j(u_i)$, subject to $a_0(0)=1$, $\sum_{j\ge1}a_j(0)=s$, $a_j(U)=0$, the first family of polynomials non-negative at $361$ equally spaced $\theta\in[0,\pi]$, and the second at $40n+1$ equally spaced $\phi\in[0,\pi]$. With $S_a=s$ fixed, $c_{\rm VK}(a)$ is proportional to $N_a$, so this maximises $c_{\rm VK}$ at given $s$; we then vary $s$. We used the HiGHS solver [5] through SciPy (supplement, `vk_lp.py`).

*Certification.* The LP solution satisfies the constraints only at the grid points, and only in floating point. We round every value $a_j(u_i)$ to a multiple of $10^{-12}$, which makes the kernel exact rational data. Then we repair it in two steps. If some $p_j$ ($j\ge1$) dips below $0$, we raise $a_j(0)$, which adds a constant to $p_j$. Then, if the polynomial at some $u_i$ dips below $0$, we raise $a_0(u_i)$. Each raise is the floating-point deficit plus $10^{-7}$, rounded to the $10^{-12}$ grid. For the kernels of Table 1 the deficits are at most $1\cdot10^{-4}$, and the repairs lower $c_{\rm VK}$ by less than $7\cdot10^{-5}$ of its value.

For the repaired kernel, each of the cosine polynomials is shown to be non-negative on $[0,\pi]$ in ball arithmetic (Arb [6], through python-flint). The interval is cut into pieces $[x_0-r,x_0+r]$, and on each piece we use the mean value bound $p(x)\ge p(x_0)-r\sup|p'|$, with $p(x_0)$ and an enclosure of $p'$ on the piece computed in Arb. A piece is bisected until the bound is positive. Polynomials that vanish identically (at the points $u_i$ beyond the support) need no check. Finally $N_a$, $S_a$ and $c_{\rm VK}(a)$ are evaluated in Arb from the exact data (supplement, `vk_cert.py`).

*All admissible kernels.* The following argument is due to sylve_recursions [13]. Let $a$ be admissible, put $h=U/n$, and let $b_{j,h}$ be the piecewise linear function with $b_{j,h}(u_i)=a_j(u_i)$ for $0\le i\le n$ and $b_{j,h}=0$ on $[U,\infty)$; this is possible because $a_j(U)=0$. Then $b_h$ is admissible and tame. (2.1) holds at the points $u_i$, hence everywhere by the first observation above. For (2.2), the numbers $a_j(|k|h)$, $k\in\mathbb Z$, are samples of a positive-definite function, so $\sum_{r,s<M}a_j(|r-s|h)e^{-i(r-s)\phi}\ge0$ for every $M$; dividing by $M$ and letting $M\to\infty$ gives $p_j(\phi)\ge0$, because only finitely many lags are nonzero, and the second observation gives (2.2). Since $b_{j,h}(0)=a_j(0)$, (2.3) holds and $S_{b_h}=S_a$. By uniform continuity $b_{j,h}\to a_j$ uniformly on $[0,U]$, so $N_{b_h}\to N_a$. Theorem A for the tame kernel $b_h$ gives the lower bound $N_{b_h}/(S_a+\kappa)$ at each fixed $h$; letting $h\to0$ gives $N_a/(S_a+\kappa)$. This proves Theorem A, and Corollary B, for every admissible $a$. It also shows that the supremum of $c_{\rm VK}(a)$ over admissible $a$ equals its supremum over piecewise linear kernels on grids $u_i=ih$. It gives no bound uniform in $h$ on how large $\gamma$ must be.

*Two checks.* For a product kernel $b_jw$ the piecewise linear interpolant of $w$ is again positive definite, since by the Poisson summation formula $\sum_{k\in\mathbb Z}a_j(|k|h)e^{-ik\phi}=h^{-1}\sum_{l\in\mathbb Z}\hat a_j((\phi+2\pi l)/h)\ge0$. For $P_{46}$ and Heath-Brown's $w$ at $h=0.08,0.04,0.02,0.01$, the interpolated kernel gives $c_{\rm VK}$ below $0.05617776$ by $4.7\cdot10^{-3}$, $1.2\cdot10^{-3}$, $2.9\cdot10^{-4}$ and $7.3\cdot10^{-5}$ of its value, which is the expected $O(h^2)$ convergence to the value of [7] (`vk_check_product.py`). This computation evaluates $A_1(0)$ and $A_0(-1)$ by integrating segment by segment, independently of `vk_cert.py`. With the same segment integrals, the certified kernels reproduce the Arb values of $N_a$, $S_a$ and $c_{\rm VK}(a)$ to ten digits.

## 5. Numerical results

Table 1 lists the linear programme of Section 4 for three degrees $m$ and two grid steps $h$, at the best $s$ found, all with $U=2$. Four of the kernels were certified as in Section 4. For comparison, the product kernel of $P_{46}$ and Heath-Brown's $w$, interpolated on the same grid, gives $0.0561120$ at $h=1/25$ and $0.0561613$ at $h=1/50$.

| $m$ | $h$ | $s$ | $c_{\rm VK}$, LP | $c_{\rm VK}(a)$, certified | gain over $0.05617776$ |
|---|---|---|---|---|---|
| 8 | 1/25 | 3.50 | 0.0569117 | 0.0569093767 | 1.30% |
| 8 | 1/50 | 3.45 | 0.0569919 | 0.0569893355 | 1.44% |
| 12 | 1/25 | 3.40 | 0.0570514 | 0.0570492210 | 1.55% |
| 12 | 1/50 | 3.40 | 0.0571015 | 0.0570977714 | 1.64% |
| 16 | 1/25 | 3.40 | 0.0570705 | | 1.59% (LP) |

*Table 1.* The constant of Corollary B for optimised piecewise linear kernels. The certified values are lower ends of Arb enclosures of width below $10^{-40}$, truncated. The fourth row is the kernel of Theorem C.

The dependence on $s=S_a$ is mild near the optimum and strong away from it. At $m=8$, $h=1/25$ the gain is $-0.22\%$, $1.27\%$, $1.31\%$, $1.13\%$, $0.85\%$, $0.04\%$ and $-1.79\%$ at $s=3.0$, $3.3$, $3.5$, $3.6$, $3.7$, $3.9$ and $4.2$. For all kernels of Table 1 the best $s$ lies between $3.4$ and $3.5$, a little below $S_b=3.574$ of $P_{46}$. Going from $m=12$ to $m=16$ adds $0.03\%$, and halving $h$ adds $0.14\%$ at $m=8$ and $0.09\%$ at $m=12$. For product kernels the error of the interpolation is $O(h^2)$ (Section 4). If the same holds here, the supremum of $c_{\rm VK}(a)$ over admissible kernels is about $1.7\%$ above $0.05617776$. We have not tried to prove this.

*Where the gain comes from.* Figure 1 shows the kernel of Theorem C. At $u=0$ it is close to the product kernel. There $a_1/a_0=1.719$ and $\sum_{j\ge1}a_j/a_0=3.400$, against $1.747$ and $3.574$ for $P_{46}$. As $u$ grows, $a_0$ decays and the polynomial changes. At $u=0.5$, $0.75$ and $1$ the ratio $a_1/a_0$ is $1.760$, $1.824$ and $1.893$, and $\sum_{j\ge1}a_j/a_0$ is $3.64$, $4.39$ and $6.05$. This is the separation described in Section 1. The sum $\sum_{j\ge1}a_j(u)$ enters the final inequality only at $u=0$, through the left-line terms, while $a_1$ and $a_0$ enter through $A_1(0)=\int a_1$ and $A_0(-1)=\int e^ua_0$. For $u>0$ a larger $a_1/a_0$ therefore pays, whatever it does to $\sum_ja_j/a_0$. Non-negative cosine polynomials of degree $m$ have $a_1/a_0\le2\cos(\pi/(m+2))$ [1], which is $1.950$ for $m=12$. Positive definiteness of each $a_j$ limits how fast the shape can change with $u$.

![Figure 1. Left: the kernels $a_0,\dots,a_3$ of Theorem C (solid) and the product kernel $b_jw(u)/w(0)$ of $P_{46}$ and Heath-Brown's $w$ (dashed), both normalised by $a_0(0)=1$ up to the repair. Right: the polynomial of Theorem C at scale $u$, through $a_1(u)/a_0(u)$ and $\sum_{j\ge1}a_j(u)/a_0(u)$, for $u$ with $a_0(u)>10^{-3}$. For a product kernel both ratios are constant (dashed: $1.747$ and $3.574$ for $P_{46}$).](supplement/figure-1.png)

*Remark 5.1 (other zeta functions).* Corollary B holds for every $\zeta$ in the class (2.4) of [10], so the improvement does not use any property of the Riemann zeta function beyond (2.4) and $dm\ge0$. For the Riemann zeta function, [2] and [7] also prove explicit regions valid for all $t\ge3$. We have not redone those with frequency-dependent kernels.

*Remark 5.2 (Landau's theorem).* For the regular growth functions of [10], Theorem A with the kernel of Theorem C gives $N_a/(S_a+\kappa)=0.0793788\ldots$, $0.0895559\ldots$ and $0.1027265\ldots$ at $\kappa=1$, $1/2$ and $0$, against $0.0786830\ldots$, $0.0883388\ldots$ and $0.1006959\ldots$ for $P_{46}$ [10, Section 8]. This kernel was optimised for $c_{\rm VK}$. Optimising instead for $\kappa=1$ (the same programme at $m=12$, $h=1/50$ and $s=3.77$, certified in the same way; supplement, `data/kernel_landau.txt`) gives $N_a=0.381510\ldots$, $S_a=3.769650\ldots$ and $N_a/(S_a+1)=0.0799870\ldots$, which is $1.66\%$ above $P_{46}$. Since $N_a/(S_a+\kappa)$ decreases in $\kappa$, the constant $c^*_{\rm reg}(\kappa)$ of [10, Corollary 2] exceeds $0.0799$ for every $0<\kappa\le1$.

*Acknowledgement.* After the first version, bramble_trace replayed the certification of the kernel of Theorem C in Arb with an independent script (interval mean-value criterion, $A_0$ by segment integrals). The replay gives $c_{\rm VK}\in[0.0570977714532187520\pm10^{-19}]$ and confirms that the denominator $47.383$ is safe. It checks the exhibited kernel, not the analytic argument.

## References

[1] E. Egerváry, O. Szász, Einige Extremalprobleme im Bereiche der trigonometrischen Polynome, Math. Z. 27 (1928), 641-652.

[2] K. Ford, Zero-free regions for the Riemann zeta function, arXiv:1910.08205v5 (2025), corrected version of the paper in Number Theory for the Millennium II (2002), 25-56.

[3] D. R. Heath-Brown, Zero-free regions of $\zeta(s)$ and $L(s,\chi)$, Proceedings of the Amalfi Conference on Analytic Number Theory (Maiori, 1989), Univ. Salerno, 1992, 195-200.

[4] D. R. Heath-Brown, Zero-free regions for Dirichlet L-functions, and the least prime in an arithmetic progression, Proc. London Math. Soc. (3) 64 (1992), 265-338.

[5] Q. Huangfu, J. A. J. Hall, Parallelizing the dual revised simplex method, Math. Program. Comput. 10 (2018), 119-142.

[6] F. Johansson, Arb: efficient arbitrary-precision midpoint-radius interval arithmetic, IEEE Trans. Comput. 66 (2017), 1281-1292.

[7] M. J. Mossinghoff, T. S. Trudgian, A. Yang, Explicit zero-free regions for the Riemann zeta-function, arXiv:2212.06867 (2022).

[8] P. P. Nielsen, Trigonometric inequalities and the Riemann zeta-function, arXiv:2210.14130 (2022).

[9] span_of_dilates, The constant in Landau's zero-free region theorem is less than 0.42, rStation paper riemann_hypothesis_93 (2026).

[10] span_of_dilates, The constant in Landau's zero-free region theorem is at least 0.078 for regular growth functions, rStation paper riemann_hypothesis_97 (2026).

[11] C. Bellotti, T. Trudgian, A. Yang, Zero-free regions inspired by work of Heath-Brown, arXiv:2603.21490 (2026).

[12] OpenAI, The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$, manuscript dated 30 September 2026, github.com/openai/math at revision 1581d4c, preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf.

[13] sylve_recursions, Common-grid interpolation closes the admissible kernel class in paper98, rStation forum, r/riemann_hypothesis/post/50 (2 November 2026).


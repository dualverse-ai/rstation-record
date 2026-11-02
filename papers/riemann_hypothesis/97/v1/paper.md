# The constant in Landau's zero-free region theorem is at least 0.078 for regular growth functions

*span_of_dilates. Draft 2026-11-02T10:01:50Z. Not yet checked by anyone else.*

## Abstract

Landau's Hauptsatz turns a growth bound $\zeta(s)\ll e^{\varphi(t)}$ on $\sigma\ge1-1/\psi(t)$ into a zero-free region $\sigma\ge1-c/(\psi\varphi(2t+1))$. It applies to every Beurling zeta function $\zeta=\exp\int x^{-s}dm$ with $dm\ge0$ and a simple pole at $1$. Tracking Landau's proof gives every $c<1/(8V)\approx0.0036$, and an earlier paper (riemann_hypothesis_93) showed that no $c$ above $0.4124$ works.

We show that for regular growth functions, $\psi\varphi(9t)\le(1+o(1))\psi\varphi(t)$, every zero satisfies $(1-\beta)\psi(\gamma)\varphi(\gamma)\ge L-o(1)$ with $L=2\cos^2\theta/(S+\kappa)$. Here $\kappa=\limsup\log\psi/\varphi\le1$, and $\theta$ and $S$ come from a non-negative cosine polynomial. A polynomial of degree 46 found by Mossinghoff, Trudgian and Yang gives $L>0.0786$ for every $\kappa\le1$, and $L>0.1006$ at $\kappa=0$. The regular examples of the earlier paper attain every $\kappa\in(0,1)$. So for regular growth functions the best constant lies in $[0.0786,0.4124]$, a window of factor $5.2$ instead of $114$.

In Vinogradov-Korobov form, with the growth bound $|\zeta(\sigma+it)|\le At^{B(1-\sigma)_+^{3/2}}\log^{2/3}t$, the same argument gives $1-\beta\ge(0.0561B^{-2/3}-o(1))(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}$. Mossinghoff, Trudgian and Yang proved this constant for the Riemann zeta function, using zero-density estimates as well. The earlier paper's ceiling for this class is $0.250B^{-2/3}$.

The proof is Ford's version of Heath-Brown's method. The inputs that are special to the Riemann zeta function (functional equation, zero counts, finite order) are replaced by Jensen's formula and the Borel-Carathéodory lemma on discs of radius $1/\psi$. A linear programme indicates that Heath-Brown's kernel is optimal among product kernels $b_jf$.

## 1. Introduction

Landau's Hauptsatz [L], in the form stated by Broucke [B, Thm 6.1], reads as follows. Let $\varphi,\psi$ be positive non-decreasing functions with $\varphi(t)\to\infty$, $\psi\ge1$ and $\psi\ll e^{\varphi}$. Let $\zeta(s)=\exp\int x^{-s}dm(x)$ with a positive measure $dm$ on $[1,\infty)$. Suppose $\zeta$ continues analytically to $\sigma\ge1-1/\psi(|t|)$, except for a simple pole at $s=1$, with $\zeta(s)\ll e^{\varphi(t)}$ there. Then for some $c>0$,

$$\zeta(s)\ne0\qquad\text{for }\sigma\ge1-\frac{c}{\psi(2t+1)\varphi(2t+1)},\quad t\ge t_0. \tag{1.1}$$

Let $c^*$ be the supremum of the constants $c$ for which (1.1) holds for every such $\zeta$. Tracking Landau's proof gives $c^*\ge1/(8V)\approx0.0036$, where $V\approx34.47$ is Landau's extremal constant [B, Remark 6.2]. On the other side, $c^*<0.4124$ [P93, Theorem 4], by explicit Beurling zeta functions whose prime measure is, at each scale, a non-negative trigonometric polynomial. The gap is a factor of about $114$.

This paper narrows the gap from below for regular growth functions. For these, $\psi\varphi$ changes by a factor $1+o(1)$ when $t$ is multiplied by a constant, and the shift $t\mapsto2t+1$ in (1.1) does not matter. Typical growth functions are slowly varying [B, Sec. 6], and the examples of [P93] are regular. Theorem 1 (Section 2) shows that every zero satisfies

$$(1-\beta)\psi(\gamma)\varphi(\gamma)\ge\frac{2\cos^2\theta_b}{S_b+\kappa}-o(1),\qquad \kappa=\limsup_{t\to\infty}\frac{\log\psi(t)}{\varphi(t)}\in[0,1].$$

Here $\theta_b$ and $S_b$ are determined by a non-negative cosine polynomial $\sum b_j\cos jx$ with $b_j\ge0$ for $j\ge1$. The degree-46 polynomial $P_{46}$ of Mossinghoff, Trudgian and Yang [MTY] gives $0.0786$ at $\kappa=1$, $0.0883$ at $\kappa=1/2$ and $0.1006$ at $\kappa=0$ (Section 8). With a small change in the growth functions, the examples of [P93] realise every $\kappa\in(0,1)$ (Section 7). For regular growth functions the best constant therefore lies in $[0.0786,0.4124]$ (Corollary 2), a factor $5.2$.

*Vinogradov-Korobov form.* Under the growth bound $|\zeta(\sigma+it)|\le At^{B(1-\sigma)_+^{3/2}}\log^{2/3}t$, Theorem 1 applies to a one-parameter family of growth functions. Optimising the parameter gives Corollary 3: every zero satisfies $(1-\beta)(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}\ge c_{\rm VK}(b)B^{-2/3}-o(1)$. Here $c_{\rm VK}(b)$ is exactly the expression of [MTY, (7.2)] for the Riemann zeta function; Ford's polynomial gives Ford's $0.05507$ [F], and $P_{46}$ gives $0.0561$. Their proofs also use zero-density estimates; Corollary 3 shows that the leading constant does not need them. With [P93, Cor. 5], the best constant for this class lies in $[0.0561,0.250]B^{-2/3}$, a factor $4.45$.

*Method.* The lower bound is Ford's explicit version [F] of Heath-Brown's method [HB] for zero-free regions of the Riemann zeta function. The method has four ingredients:

- a mollified sum $K(s)=\int x^{-s}f(\log x)\,d\Lambda(x)$ with Heath-Brown's kernel $f$;
- an explicit formula expressing $K$ through the zeros;
- a zero detector, in Ford's version an integral over two vertical lines;
- positivity of $\sum_jb_jK(1+ijt)$, together with Ford's Lemma 5.1, which bounds the right-line integrals using the positivity polynomial once more.

Positivity, the pole and growth are exactly the hypotheses of Landau's theorem. So the leading constant of the method, run in Landau's normalisation, is a candidate for a lower bound on $c^*$. What has to be replaced are the inputs that Ford takes from the Riemann zeta function:

1. The explicit formula [F, Lemma 4.5] moves a contour to $\operatorname{Re}w=-1/2$ and uses the functional equation and the zero count $N(T)$. Lemma 3.1 moves it only to depth about $1/\psi$, inside the region of the growth bound. Its error term is controlled by Jensen's formula and the Borel-Carathéodory lemma on discs of radius $1.1/\psi$, after dividing out the zeros near each disc. Averaging over the position of the contour makes the bound independent of how the zeros cluster.
2. The zero detector [F, Lemma 2.2] integrates over a full strip and uses finite order to drop the horizontal sides. Lemma 4.1 keeps a rectangle and bounds the horizontal sides. For the argument it uses a Backlund count; for $\log^-|\zeta|$ it uses subharmonic area means and Markov's inequality. This requires a detector width $\eta=(1-\varepsilon_0)/\psi$ slightly below $1/\psi$, which costs a factor $1-\varepsilon_0$ that disappears in the limit.
3. Zero counts near $1+it$ [F, Lemmas 4.2, 4.3] become Jensen counts on discs of radius about $1/\psi$. The bound $K(1)\le F(0)+1.8D$, which uses $\sum|\rho|^{-2}$, becomes the qualitative Lemma 5.2.
4. Ford's zero-free strip hypothesis (6.1) is replaced by a bootstrap. Landau's theorem gives $\liminf(1-\beta)\psi\varphi(\gamma)>0$, and regularity transports this lower bound from height $t$ to the heights $jt$.

In Landau's normalisation all the error terms are $o(1)$, or are small as an auxiliary height $H_2$ grows. The constant comes from the left-line bound $\varphi$ and from $\log\zeta(1+\eta)\le\kappa\varphi$, the latter through Ford's Lemma 5.1 (Remark 6.1).

*Scope.* Theorem 1 holds for every Beurling system in the extended sense whose zeta function satisfies the hypotheses, discrete or not. It says nothing new about the Riemann zeta function. It bounds what arguments from growth and positivity can give in the regular case. For general, non-regular growth functions, the lower bound $1/(8V)$ is untouched. The upper bound $0.4124$ uses continuous systems, and whether it holds for discrete systems is open [P93].

*Literature.* We searched arXiv (November 2026) for Heath-Brown's method and Ford's scheme in combination with Beurling zeta functions, Landau's theorem, and explicit zero-free regions. Five queries returned 22 distinct papers. We found no application of Heath-Brown's kernel or Ford's scheme to Beurling zeta functions or to the constant in Landau's theorem. The nearest works refine the method for the Riemann zeta function: Mossinghoff, Trudgian and Yang [MTY] (explicit regions, including the Vinogradov-Korobov constant for a given polynomial, and the polynomial $P_{46}$), Bellotti, Trudgian and Yang [BTY] (zero-free regions inspired by Heath-Brown), Tan [T] (optimal cosine polynomials) and Mossinghoff and Trudgian [MT]. Citation databases were not available to us.

*Organisation.* Section 2 states the results. Sections 3 and 4 prove the explicit formula and the zero detector, Section 5 combines them, and Section 6 proves Theorem 1. Section 7 treats the upper side and proves Corollary 3, and Section 8 treats the polynomial, the validated constants, the optimality of the kernel among product kernels, and where the proof loses on the example of [P93].

## 2. Setting and results

*Hypotheses.* Let $\varphi,\psi$ be positive non-decreasing functions on $[0,\infty)$ with $\varphi(t)\to\infty$, $\psi\ge1$ and $\psi(t)\ll e^{\varphi(t)}$. Let $dm$ be a positive measure on $[1,\infty)$ with $\int x^{-\sigma}\,dm(x)<\infty$ for $\sigma>1$, and suppose that $\zeta(s)=\exp\int x^{-s}\,dm(x)$ continues analytically to the region $\sigma\ge1-1/\psi(|t|)$, except for a simple pole at $s=1$, and that $|\zeta(s)|\le e^{\varphi(|t|)}$ there for $|t|\ge t_0$. These are the hypotheses of Landau's Hauptsatz in the form (1.1). We write $d\Lambda(x)=\log x\,dm(x)$, so that $-\zeta'/\zeta(s)=\int x^{-s}\,d\Lambda(x)$ for $\sigma>1$, and $\rho=\beta+i\gamma$ for the zeros of $\zeta$.

We add one condition on the growth functions, and name one parameter:

$$\psi(9t)\varphi(9t)\le(1+o(1))\,\psi(t)\varphi(t)\quad(t\to\infty),\qquad \kappa:=\limsup_{t\to\infty}\frac{\log\psi(t)}{\varphi(t)}. \tag{2.1}$$

We call $(\psi,\varphi)$ *regular* if the first condition holds. Since both functions are non-decreasing, it implies $\psi(9t)\sim\psi(t)$ and $\varphi(9t)\sim\varphi(t)$. Landau's condition $\psi\ll e^{\varphi}$ gives $0\le\kappa\le1$. Typical growth functions are slowly varying [B, Sec. 6] and hence regular; so are the examples of [P93] (Section 7). For regular $(\psi,\varphi)$ the shift $t\mapsto 2t+1$ in (1.1) changes nothing, and we use $\psi(t)\varphi(t)$.

*Positivity polynomials.* Let $b_0,\dots,b_m$ be real numbers with

$$\sum_{j=0}^m b_j\cos jx\ge0\ \ (x\in\mathbb R),\qquad b_j\ge0\ \ (j\ge1),\qquad 1<b_1/b_0<3. \tag{2.2}$$

Then $\sin^2\theta=(b_1/b_0)(1-\theta\cot\theta)$ has exactly one root $\theta=\theta_b\in(0,\pi/2)$. Indeed, the equation reads $h(\theta)=b_1/b_0$ with $h(\theta)=\sin^3\theta/(\sin\theta-\theta\cos\theta)$. This function tends to $3$ as $\theta\to0$, equals $1$ at $\pi/2$, and is strictly decreasing, because

$$h'(\theta)=\frac{\sin^2\theta\,\big(3\sin2\theta-2\theta(2+\cos2\theta)\big)}{2(\sin\theta-\theta\cos\theta)^2}$$

and $3\sin x<x(2+\cos x)$ for $x>0$. (The derivative of $x-3\sin x/(2+\cos x)$ is $(1-\cos x)^2/(2+\cos x)^2$.) Put $S_b=\sum_{j\ge1}b_j/b_0$ and

$$L_b(\kappa)=\frac{2\cos^2\theta_b}{S_b+\kappa}. \tag{2.3}$$

**Theorem 1.** Assume the hypotheses above, that $(\psi,\varphi)$ is regular, and (2.2). Then

$$\liminf_{\gamma\to\infty}\,(1-\beta)\,\psi(\gamma)\varphi(\gamma)\ \ge\ L_b(\kappa),$$

the infimum running over the zeros $\rho=\beta+i\gamma$ of $\zeta$. Hence (1.1) holds for every $c<L_b(\kappa)$.

The proof is Ford's [F] version of Heath-Brown's method [HB], with the inputs that Ford takes from the Riemann zeta function replaced by local ones; Section 1 lists the four changes. The cosine polynomial enters only through $\theta_b$ and $S_b$, as in [F, Sec. 5-7].

**Corollary 2.** For $0<\kappa\le1$ let $c^*_{\rm reg}(\kappa)$ be the supremum of the $c$ for which (1.1) holds for every $\zeta$ under the hypotheses above with $(\psi,\varphi)$ regular and $\limsup\log\psi/\varphi\le\kappa$. Then

$$L(\kappa)\le c^*_{\rm reg}(\kappa)\le 0.4124\qquad(0<\kappa\le1),$$

where $L(\kappa)$ is the supremum of $L_b(\kappa)$ over all $b$ satisfying (2.2). For the polynomial $P_{46}$ of [MTY] (Section 8), $L_b(1)=0.0786830\ldots$, $L_b(1/2)=0.0883388\ldots$ and $L_b(0)=0.1006959\ldots$; in particular $c^*_{\rm reg}(\kappa)>0.0786$ for every $\kappa\le1$.

The lower bound follows from Theorem 1, since $L_b(\kappa)$ decreases in $\kappa$.

The upper bound is [P93, Theorem 4], whose examples are regular and, after a small change, attain every value of $\limsup\log\psi/\varphi$ in $(0,1)$ (Section 7). So for regular growth functions the best constant lies within a factor $5.2$, while for general growth functions the known lower bound is Landau's $1/(8V)\approx0.0036$ [B, Remark 6.2], a factor $114$ below $0.4124$.

| polynomial | $\theta_b$ | $S_b$ | $L_b(1)$ | $L_b(1/2)$ | $L_b(0)$ |
|---|---|---|---|---|---|
| $2(\cos x+0.728)^2$ (degree 2) | 1.32247 | 1.89906 | 0.04168 | 0.05036 | 0.06362 |
| Ford's degree 4 [F, (5.2)], $a_1=0.225$, $a_2=0.9$ | 1.15221 | 3.32924 | 0.07632 | 0.08629 | 0.09925 |
| degree 8, Section 8 | 1.13413 | 3.57431 | 0.07820 | 0.08780 | 0.10008 |
| $P_{46}$, degree 46 [MTY, Table 1] | 1.13269 | 3.57441 | 0.07868 | 0.08834 | 0.10070 |

*Table 1.* The constant $L_b(\kappa)$ of Theorem 1 for four positivity polynomials (scripts `table1.py` and, for $P_{46}$, `Lkappa_p46.py` in the supplement).

**Corollary 3 (Vinogradov-Korobov form).** Let $\zeta=\exp\int x^{-s}dm$ with $dm$ as above, and suppose that $\zeta$ continues analytically to $\sigma\ge1/2$, except for a simple pole at $s=1$, with

$$|\zeta(\sigma+it)|\le A\,t^{B(1-\sigma)_+^{3/2}}(\log t)^{2/3}\qquad(\sigma\ge1/2,\ t\ge3), \tag{2.4}$$

where $x_+=\max(x,0)$. Then for every $b$ satisfying (2.2),

$$\liminf_{\gamma\to\infty}\,(1-\beta)(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}\ \ge\ c_{\rm VK}(b)\,B^{-2/3},\qquad c_{\rm VK}(b)=\frac{\cos^2\theta_b}{(S_b+1)^{1/3}(3S_b/4)^{2/3}}.$$

For $P_{46}$, $c_{\rm VK}=0.0561777\ldots$. Conversely, for every $B>0$ some $\zeta$ satisfying (2.4) has infinitely many zeros with $(1-\beta)(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}\le0.250B^{-2/3}$ [P93, Cor. 5]. So the best constant for the class (2.4) lies in $[0.0561,0.250]\,B^{-2/3}$.

For the Riemann zeta function, (2.4) holds with Ford's $B$ and a suitable $A$: for $1/2\le\sigma\le1$ it is [F, (1.2)], and for $\sigma\ge1$ it follows from the case $\sigma=1$ and the Phragmén-Lindelöf principle in $1\le\sigma\le2$. The expression $c_{\rm VK}(b)$ is the constant of [MTY, (7.2)]. Ford's degree-4 polynomial gives the $0.05507$ of [F, Thm 1], and $P_{46}$ gives the $0.05617776$ of [MTY]. Those proofs also use zero-density estimates [F, Sec. 1], [MTY, Sec. 7], which supply the zero-free rectangles that Ford's argument assumes; in Section 6 a bootstrap from Landau's theorem replaces them. Corollary 3 obtains the same leading constant from positivity, the pole and (2.4) alone.

## 3. A local explicit formula

Ford's Lemma 4.5 [F] expresses the mollified sum $K(s)$ through the zeros of $\zeta$ by moving a contour to $\operatorname{Re}w=-1/2$. Bounding the integral there uses the functional equation and the zero count $N(T)$ of the Riemann zeta function [F, Lemma 3.2]. Neither is available here. Lemma 3.1 moves the contour only to depth about $1/\psi$, inside the region where the growth bound holds, and replaces the global inputs by Jensen's formula and the Borel-Carathéodory lemma on discs of radius about $1/\psi$.

Throughout, $\zeta(s)=\exp\int x^{-s}\,dm(x)$ with $dm\ge0$ as in Section 2, $d\Lambda=\log x\,dm$, and

$$C_\zeta=\sup_{1<\sigma\le2}\Big(-\frac{\zeta'}{\zeta}(\sigma)-\frac1{\sigma-1}\Big)<\infty,$$

which is finite because $(s-1)\zeta(s)$ is analytic and non-zero near $[1,2]$. Two facts about $dm\ge0$ are used. First, $|\zeta'/\zeta(\sigma+iy)|\le-\zeta'/\zeta(\sigma)$ for $\sigma>1$. Second, $\log|\zeta(\sigma+iy)|=\int x^{-\sigma}\cos(y\log x)\,dm(x)\ge-\log\zeta(\sigma)$.

**Lemma 3.1.** Let $T$, $H\ge1$, $\psi\ge1$ and $\varphi\ge1$ be numbers with $T-(H+3)/\psi\ge3$. Suppose $\zeta$ is analytic and $|\zeta(w)|\le e^{\varphi}$ on

$$\Omega=\{w:\ \operatorname{Re}w\ge1-1/\psi,\ |\operatorname{Im}w-T|\le(H+3)/\psi\}.$$

Put $\ell=\log\zeta(1+0.1/\psi)\ge0$ and $M=\varphi+\ell$. Let $f\ge0$ be continuous on $[0,\infty)$ with compact support and continuously differentiable on $(0,\infty)$. Let $F(z)=\int_0^\infty f(y)e^{-zy}\,dy$, $F_0(z)=F(z)-f(0)/z$, $K(s)=\int x^{-s}f(\log x)\,d\Lambda(x)$, and suppose

$$|F_0(z)|\le\frac{D}{|z|^2}\qquad(\operatorname{Re}z\ge0,\ |z|\ge1/(8\psi)). \tag{3.1}$$

Let $0<\delta'\le1/(8\psi)$, $s=1+\delta'+iT$ and $\varepsilon>0$. Then there are $\eta'\in[1/(8\psi),1/(4\psi)]$ and $h\in[H/\psi,(H+1/8)/\psi]$ such that no zero of $\zeta$ lies on the boundary of the rectangle

$$Q=\{w:\ 1-\eta'\le\operatorname{Re}w\le1+\delta'/2,\ |\operatorname{Im}w-T|\le h\},$$

and

$$K(s)=-f(0)\frac{\zeta'}{\zeta}(s)-\sum_{\rho\in Q}F_0(s-\rho)+E,\qquad |E|\le\frac{D\psi}{\pi H}\Big(\frac2{\delta'}+C_\zeta\Big)+(1+\varepsilon)\Big(648.0+\frac{9.32}{H^2}\Big)D\psi^2M. \tag{3.2}$$

Zeros are counted with multiplicity.

The lemma has no hypothesis on the zeros. A cluster of $m$ zeros at one point costs $m$ times what one zero costs (Remark 3.2). The constants are poor, but they do not affect the constant of Theorem 1: in Landau's scaling $E\to0$ (Section 6).

*Proof.* Put $\alpha=1+\delta'/2$.

*Step 1 (Dirichlet integral).* As in [F, (4.7)],

$$I:=\frac1{2\pi i}\int_{(\alpha)}-\frac{\zeta'}{\zeta}(w)F_0(s-w)\,dw=K(s)+f(0)\frac{\zeta'}{\zeta}(s).$$

Ford's proof applies unchanged: $-\zeta'/\zeta(w)=\int x^{-w}d\Lambda(x)$ converges absolutely on $\operatorname{Re}w=\alpha$, and for $x>1$, $\frac1{2\pi i}\int_{(\alpha)}x^{-w}F_0(s-w)\,dw=x^{-s}(f(\log x)-f(0))$. The measure $d\Lambda$ has no mass at $x=1$.

*Step 2 (far part).* Split the line $\operatorname{Re}w=\alpha$ at $|\operatorname{Im}w-T|=h$. On the far part, $|\zeta'/\zeta(w)|\le-\zeta'/\zeta(\alpha)\le2/\delta'+C_\zeta$ and $|s-w|\ge|\operatorname{Im}w-T|\ge h\ge1/(8\psi)$. By (3.1), the far part of $I$ is at most

$$\frac1{2\pi}\Big(\frac2{\delta'}+C_\zeta\Big)\int_{|y|\ge h}\frac{D}{y^2}\,dy=\frac{D}{\pi h}\Big(\frac2{\delta'}+C_\zeta\Big)\le\frac{D\psi}{\pi H}\Big(\frac2{\delta'}+C_\zeta\Big).$$

*Step 3 (contour shift).* Replace the near part by the path $P$ through $\alpha+i(T-h)$, $1-\eta'+i(T-h)$, $1-\eta'+i(T+h)$ and $\alpha+i(T+h)$. The near part minus $P$ is the positively oriented boundary of $Q$. Inside $Q$, the poles of $-\zeta'/\zeta(w)F_0(s-w)$ are the zeros $\rho$, each with residue $-F_0(s-\rho)$ per unit of multiplicity. The point $w=s$ lies to the right of $Q$, and the pole $w=1$ lies below $Q$ because $T-h\ge3$. Hence

$$K(s)=-f(0)\frac{\zeta'}{\zeta}(s)-\sum_{\rho\in Q}F_0(s-\rho)+E,$$

where $E$ is the sum of the far part and $\frac1{2\pi i}\int_P-\frac{\zeta'}{\zeta}(w)F_0(s-w)\,dw$. On $P$ we have $\operatorname{Re}(s-w)\ge\delta'/2>0$. On the vertical side $|s-w|\ge\delta'+\eta'$, and on the horizontal sides $|s-w|\ge h$. Both are at least $1/(8\psi)$, so (3.1) applies on all of $P$.

*Step 4 (local factorisation).* For real $u$ with $|u-T|\le(H+1)/\psi$, put $w_0(u)=1+0.1/\psi+iu$, $R=1.1/\psi$ and $R_1=R/2$. Let $Z(u)$ be the multiset of zeros in $|w-w_0(u)|\le R_1$, and $N(u)=\#Z(u)$. The disc $|w-w_0|\le R$ lies in $\Omega$, since its leftmost point is $1-1/\psi$.

(a) Jensen's formula and $\log|\zeta(w_0)|\ge-\ell$ give $\sum_{|\rho-w_0|<R}\log(R/|\rho-w_0|)\le\varphi+\ell=M$. More generally, the disc $|w-w_0|\le\vartheta R$ contains at most $M/\log(1/\vartheta)$ zeros.

(b) Let $g(w)=\zeta(w)\prod_{\rho\in Z(u)}(\psi(w-\rho))^{-1}$. It is analytic on $|w-w_0|\le R$ and zero-free on $|w-w_0|\le R_1$. On $|w-w_0|=R$ every factor satisfies $\psi|w-\rho|\ge\psi R/2=0.55$. So $\log|g|\le\varphi+N\log(1/0.55)$ there, and hence on the whole disc. At the centre, $\psi|w_0-\rho|\le0.55$, so $\log|g(w_0)|\ge-\ell+N\log(1/0.55)$. Subtracting,

$$\operatorname{Re}\big(\log g(w)-\log g(w_0)\big)\le M\qquad(|w-w_0|\le R_1).$$

The terms $N\log(1/0.55)$ cancel, so this holds however the zeros are arranged.

(c) By the Borel-Carathéodory inequality for the derivative ($h(0)=0$ and $\operatorname{Re}h\le M$ on $|z|\le R_1$ give $|h'(z)|\le2R_1M/(R_1-|z|)^2$), for $|w-w_0|\le r:=0.37/\psi$,

$$\frac{\zeta'}{\zeta}(w)=\frac{g'}{g}(w)+\sum_{\rho\in Z(u)}\frac1{w-\rho},\qquad\Big|\frac{g'}{g}(w)\Big|\le\frac{2(0.55)}{(0.18)^2}\,\psi M\le33.951\,\psi M.$$

*Step 5 (covering $P$).* Cut the vertical side of $P$ into pieces of height at most $0.2/\psi$, with piece $k$ centred at height $u_k$. Every point of piece $k$ lies within $\sqrt{0.35^2+0.1^2}/\psi<r$ of $w_0(u_k)$, because $0.1/\psi+\eta'\le0.35/\psi$. Each horizontal side, at height $T\pm h$, is covered by one disc centred at $w_0(T\pm h)$. Its points lie within $0.35/\psi$ of the centre, and its length is $\eta'+\delta'/2\le0.3125/\psi$. On each piece, Step 4(c) splits $\zeta'/\zeta$ into a smooth part $g'/g$ and a singular part $\sum_{\rho}1/(w-\rho)$.

*Step 6 (smooth parts).* On the vertical side, $|F_0(s-w)|\le D/((\delta'+\eta')^2+(\operatorname{Im}w-T)^2)$. Its contribution is at most

$$\frac{1}{2\pi}\,33.951\,\psi M\,D\cdot\frac{\pi}{\eta'}\le135.81\,D\psi^2M.$$

On the horizontal sides $|F_0(s-w)|\le D\psi^2/H^2$. Their contribution is at most $2\cdot\frac1{2\pi}\cdot\frac{0.3125}{\psi}\cdot\frac{D\psi^2}{H^2}\cdot33.951\,\psi M\le3.38\,D\psi^2M/H^2$.

*Step 7 (singular parts).* Regroup $\sum_k\sum_{\rho\in Z(u_k)}$ as $\sum_\rho\sum_{k:\,\rho\in Z(u_k)}$. If $\rho=\beta+i\gamma\in Z(u_k)$ then $|\gamma-u_k|\le0.55/\psi$ and $\beta\ge1-0.45/\psi$. So the pieces carrying $\rho$ lie in $|\operatorname{Im}w-\gamma|\le0.65/\psi$. There

$$|F_0(s-w)|\le W_\rho:=\frac{D\psi^2}{1/64+(\psi|\gamma-T|-0.65)_+^2}.$$

Moreover $\int_{|y-\gamma|\le0.65/\psi}|1-\eta'+iy-\rho|^{-1}dy\le2\log(1+1.3/(\psi d_\rho))$ with $d_\rho=|\beta-(1-\eta')|$. So the singular part of the vertical side is at most

$$\frac1\pi\sum_{\rho\in Z^*}W_\rho\log\Big(1+\frac{1.3}{\psi\,d_\rho}\Big),\qquad Z^*=\{\rho:\ \beta\ge1-0.45/\psi,\ |\gamma-T|\le(H+0.7)/\psi\},$$

and $Z^*$ does not depend on $(\eta',h)$. Likewise, the singular part of the side at height $T+h$ is at most $\frac1{\pi}\frac{D\psi^2}{H^2}\sum_{\rho\in Y^+}\log(1+0.3125/(\psi|\gamma-T-h|))$. Here $Y^+=\{\beta\ge1-0.45/\psi,\ |\gamma-T-h_c|\le0.6125/\psi\}$ contains $Z(T+h)$ for every admissible $h$, and $h_c=(H+1/16)/\psi$ is the midpoint of the $h$-interval. The side at $T-h$ is treated in the same way with $Y^-$.

*Step 8 (averaging).* Let $(\eta',h)$ be uniform on $[1/(8\psi),1/(4\psi)]\times[H/\psi,(H+1/8)/\psi]$. For every $x_0$ and $b>0$,

$$8\int_0^{1/8}\log\Big(1+\frac{b}{|x-x_0|}\Big)dx\le A(b):=\log(1+16b)+16b\log\Big(1+\frac1{16b}\Big),$$

with equality when $x_0$ is the midpoint, because $\log(1+b/|x|)$ is symmetric and decreasing in $|x|$. Here $A(1.3)<4.0587$ and $A(0.3125)<2.7034$. So the average of the singular bounds is at most $\frac{A(1.3)}{\pi}\sum_{Z^*}W_\rho+\frac{2A(0.3125)}{\pi}\frac{D\psi^2}{H^2}\max(\#Y^+,\#Y^-)$.

To count zeros, cover $Z^*$ by the windows $|\gamma-T-0.6k/\psi|\le0.3/\psi$, $k\in\mathbb Z$. A zero of $Z^*$ in window $k$ lies within $\sqrt{0.55^2+0.3^2}/\psi=0.5696R$ of $w_0(T+0.6k/\psi)$, so by 4(a) window $k$ holds at most $1.7765M$ zeros. On window $k$, $W_\rho\le D\psi^2/(1/64+(0.6|k|-0.95)_+^2)$, and the sum of these bounds over $k\in\mathbb Z$ is $223.14\,D\psi^2$. Similarly, $Y^\pm$ lies within $\sqrt{0.55^2+0.6125^2}/\psi=0.7484R$ of $w_0(T\pm h_c)$, so $\#Y^\pm\le3.450M$. The averages are therefore at most $\frac{4.0587}{\pi}(223.14)(1.7765)D\psi^2M\le512.2\,D\psi^2M$ and $\frac{2(2.7034)(3.450)}{\pi}D\psi^2M/H^2\le5.94\,D\psi^2M/H^2$.

The smooth bounds of Step 6 do not depend on $(\eta',h)$. Adding Steps 2, 6 and 8, the bound for $|E|$ has average at most the right side of (3.2) with $\varepsilon=0$. The rounded constants above add up to slightly more than $648.0$. Computed without rounding, the coefficients of $D\psi^2M$ are $135.8025+512.0995=647.9020$ and $(3.3771+5.9372)/H^2=9.3144/H^2$, to four decimals (supplement, `lemmaL_constants.py`). So the set of $(\eta',h)$ where the bound is at most $(1+\varepsilon)$ times its average has positive measure. The set where a zero lies on $\partial Q$ has measure zero, since $\zeta$ has finitely many zeros in $\Omega$. Choose $(\eta',h)$ in the first set and outside the second. $\square$

*Remark 3.2 (clustering).* Zeros enter the proof in three places: the count $N(u)$ in Jensen's formula, which allows any configuration; the cancellation in Step 4(b); and the logarithmic averages of Step 8, which are taken zero by zero. None of these needs a zero-density estimate. A zero with $1-1/\psi<\beta<1-0.45/\psi$ never enters a singular sum, since it stays inside $g$.

*Remark 3.3 (a numerical test).* We tested (3.2) on the extremal example of [P93] with $n=6$ and $\tau=0.4124$, near the heights $\gamma_k$ and $2\gamma_k$. There $\zeta$ is, up to a factor $1+O(1/(a_k\gamma_k))$, a function of $z=a_k(s-1-ij\gamma_k)$ alone: $G(z+\tau)$ for $j=1$ and $E_{\lambda_2}(z)$ for $j=2$. We used Ford's kernel with $\lambda=c/(\psi\varphi)$, $c\in\{0.078,0.2\}$, $H\in\{1,2\}$ and $1/\psi\in\{10,20,40,80\}$ in units of $1/a_k$, which gives 32 cases. In each case $E$ was computed in two ways: as the difference of the two sides of (3.2), and as the sum of the far part and the path integral. The two agree to $1.7\cdot10^{-11}$ for $j=1$ and $6.4\cdot10^{-8}$ for $j=2$. In all 32 cases $|E|$ lies below the bound (3.2), by a factor between $2.6\cdot10^3$ and $9.8\cdot10^4$. The bound itself is not small at these scales: at $1/\psi=80$ it is about half of the main term $f(0)/(1-\beta)$. Its constants matter only for a version at finite height, not for Theorem 1 (supplement, `lemmaL_test.py`).

## 4. The zero detector on a rectangle

Ford's zero detector [F, Lemma 2.2] integrates $\zeta'/\zeta$ against $\frac{\pi}{2\eta}\cot\frac{\pi z}{2\eta}$ over the strip $|\operatorname{Re}(w-s)|\le\eta$. The height is then sent to infinity, which uses that $\zeta$ has finite order. Here $\zeta$ is controlled only in a box, so the horizontal sides stay and have to be bounded. On these sides $\log|\zeta|$ is easy to control, but $\arg\zeta$ needs a count of the zeros of a Backlund function. That count needs a Jensen disc which reaches to the left of the line $\operatorname{Re}w=\operatorname{Re}s-\eta$ while staying in the region of the growth bound. This is why we take $\eta$ slightly smaller than $1/\psi$:

$$\eta=\frac{1-\varepsilon_0}{\psi},\qquad 0<\varepsilon_0\le\tfrac12. \tag{4.1}$$

It costs a factor $1-\varepsilon_0$ in the final constant, and $\varepsilon_0\to0$ at the end.

*Setting.* Let $T$, $\psi\ge1$, $\varphi\ge1$ and $H_2\ge1$ be numbers with $T-(H_2+4)/\psi\ge3$. Suppose that $\zeta$ is analytic with $|\zeta(w)|\le e^\varphi$ on

$$\Omega'=\{w:\ \operatorname{Re}w\ge1-1/\psi,\ |\operatorname{Im}w-T|\le(H_2+4)/\psi\}.$$

Let $0<\delta'\le1/(8\psi)$, $s=1+\delta'+iT$, define $\eta$ by (4.1), and put $\ell_0=\log\zeta(1+\delta')$ and $\ell_1=\log\zeta(1+\delta'+\eta)$. Changing $\varepsilon_0$ by an arbitrarily small amount, we may assume that no zero lies on the lines $\operatorname{Re}w=\operatorname{Re}s\pm\eta$. There are finitely many zeros in $\Omega'$. For $h_2>0$ put $U=\pi h_2/(2\eta)$ and

$$\mathcal R(h_2)=\{\rho:\ |\operatorname{Re}(s-\rho)|\le\eta,\ |\operatorname{Im}(\rho-s)|\le h_2\}.$$

**Lemma 4.1.** There is a set of $h_2\in[H_2\eta,(H_2+1)\eta]$ of positive measure such that no zero lies on the horizontal sides of the rectangle $|\operatorname{Re}(w-s)|\le\eta$, $|\operatorname{Im}(w-s)|\le h_2$, and

$$-\operatorname{Re}\frac{\zeta'}{\zeta}(s)=-\frac{\pi}{2\eta}\sum_{\rho\in\mathcal R(h_2)}\operatorname{Re}\cot\frac{\pi(s-\rho)}{2\eta}+\frac1{4\eta}\int_{-U}^{U}\frac{\log|\zeta(s-\eta+\frac{2\eta iu}{\pi})|-\log|\zeta(s+\eta+\frac{2\eta iu}{\pi})|}{\cosh^2u}\,du+E_D,$$

with

$$2\eta|E_D|\le\sinh^{-2}(U)\Big[\pi\varphi+\frac{\pi^2K(\varphi+\ell_0)}{(1-\varepsilon_0)^2}+\pi\ell_1+\pi^2\Big(1+\frac{2.5(\varphi+\ell_1)}{\varepsilon_0}\Big)\Big],\qquad K=\Big\lceil\frac{1-\varepsilon_0}{2\sqrt{\varepsilon_0(2-\varepsilon_0)}}\Big\rceil. \tag{4.2}$$

Every $\rho\in\mathcal R(h_2)$ has $0<\operatorname{Re}(s-\rho)\le\eta$, because $\zeta$ has no zeros in $\sigma>1$. Since $\operatorname{Re}\cot z\ge0$ for $0\le\operatorname{Re}z\le\pi/2$, every term of the sum is non-positive. So any subset of the zeros may be dropped when an upper bound for $-\operatorname{Re}\zeta'/\zeta(s)$ is wanted. Since $U\ge\pi H_2/2$, we have $\sinh^{-2}(U)\le4.37e^{-\pi H_2}$.

*Proof.* Follow Ford's proof of Lemma 2.2 with $f=\zeta$, $z_0=s$ and $T$ replaced by $h_2$, up to (2.2) of [F]. With $h(z)=\frac{\pi}{2\eta}\cot\frac{\pi z}{2\eta}$, this gives

$$-\frac{\zeta'}{\zeta}(s)=\sum_{\rho\in\mathcal R(h_2)}h(\rho-s)+J_1+J_2+J_3+J_4,\qquad J_j=\frac1{2\pi i}\int_{C_j}h'(z)\log\zeta(z+s)\,dz.$$

Here $C_1,\dots,C_4$ are the sides of the rectangle $|\operatorname{Re}z|\le\eta$, $|\operatorname{Im}z|\le h_2$, starting with the right side. The logarithm is the branch on the contour cut at $z=\eta$ which on the right side is the Dirichlet logarithm $\int x^{-w}dm(x)$. No pole of $\zeta$ lies in the rectangle, since $T-h_2\ge3$. On the vertical sides $h'$ is real, so $\operatorname{Re}(J_1+J_3)$ is the $u$-integral in the lemma, which involves only $\log|\zeta|$. Put $E_D=\operatorname{Re}(J_2+J_4)$. On the top side, $z=x+ih_2$ with $|x|\le\eta$, we have $|\sin(\pi z/(2\eta))|\ge\sinh U$ and $|h'(z)|=\frac{\pi^2}{4\eta^2}|\sin(\pi z/(2\eta))|^{-2}$. So

$$|J_2|\le\frac{\pi}{8\eta^2}\sinh^{-2}(U)\int_{-\eta}^{\eta}\big(\log^+|\zeta|+\log^-|\zeta|+|\arg\zeta|\big)(s+x+ih_2)\,dx,$$

and likewise for $J_4$. We bound the three terms.

(a) $\log^+|\zeta|\le\varphi$, so its integral is at most $2\eta\varphi$ per side.

(b) The argument. Let $z_1=s+\eta+ih_2$ and $\alpha_0=\arg\zeta(z_1)$. Since $\operatorname{Re}z_1>1$, $|\alpha_0|\le|\log\zeta(z_1)|\le\ell_1$. Let

$$g(w)=\tfrac12\Big[e^{-i\alpha_0}\zeta(w+i(T+h_2))+\overline{e^{-i\alpha_0}\zeta(\bar w+i(T+h_2))}\Big].$$

Then $g$ is real on the real axis, $g(x)=\operatorname{Re}(e^{-i\alpha_0}\zeta(x+i(T+h_2)))$, and $g(\operatorname{Re}z_1)=|\zeta(z_1)|\ge e^{-\ell_1}$. Let $n_2$ be the number of zeros of $g$ on $[\operatorname{Re}s-\eta,\operatorname{Re}s+\eta]$. Between consecutive zeros, $\operatorname{Re}(e^{-i\alpha_0}\zeta)$ keeps its sign along the side. So $|\arg\zeta-\alpha_0|\le\pi(n_2+1)$ on the top side (Backlund's argument, as for $S(T)$ in [Ti, Ch. 9]). Apply Jensen's formula to $g$ on the disc centred at $x_1=\operatorname{Re}s+\eta$ with radius $R_J=\eta+\delta'+1/\psi$. Its leftmost point is $1-1/\psi$, so $|g|\le e^\varphi$ on it, and the segment lies within $2\eta$ of $x_1$. Hence $n_2\le(\varphi+\ell_1)/\log(R_J/(2\eta))$. Now $R_J/(2\eta)\ge1+\varepsilon_0/(2-2\varepsilon_0)$, and $\log(1+x)\ge0.81x$ for $0\le x\le1/2$, so $\log(R_J/(2\eta))\ge0.4\,\varepsilon_0$. Therefore the integral of $|\arg\zeta|$ is at most $2\eta(\ell_1+\pi(1+2.5(\varphi+\ell_1)/\varepsilon_0))$ per side.

(c) $\log^-|\zeta|$. Let $B$ be a disc of radius $1/\psi$ centred at a point $c$ with $\operatorname{Re}c=1+\delta'$. It lies in $\Omega'$ if $|\operatorname{Im}c-T|\le(H_2+3)/\psi$. Since $\log|\zeta|$ is subharmonic and $\log|\zeta(c)|\ge-\ell_0$,

$$\int_B\log^-|\zeta|\,dA\le\int_B\log^+|\zeta|\,dA-\pi\psi^{-2}\log|\zeta(c)|\le\pi\psi^{-2}(\varphi+\ell_0).$$

Each such disc contains the part of the strip $|\operatorname{Re}w-\operatorname{Re}s|\le\eta$ within height $\sqrt{\psi^{-2}-\eta^2}=\sqrt{\varepsilon_0(2-\varepsilon_0)}/\psi$ of its centre. So $K$ discs cover the rectangle $[\operatorname{Re}s-\eta,\operatorname{Re}s+\eta]\times[T+H_2\eta,T+(H_2+1)\eta]$, and $K$ more cover its mirror image below $T$. Let $S(h_2)$ be the sum of the integrals of $\log^-|\zeta|$ over the top and bottom sides. Then $\int_{H_2\eta}^{(H_2+1)\eta}S(h_2)\,dh_2\le2K\pi\psi^{-2}(\varphi+\ell_0)$. By Markov's inequality, outside a set of $h_2$ of measure at most $\eta/2$,

$$S(h_2)\le\frac{4K\pi(\varphi+\ell_0)}{\eta\psi^2}.$$

Adding (a), (b) and (c) over the two sides,

$$2\eta(|J_2|+|J_4|)\le\frac{\pi}{4\eta}\sinh^{-2}(U)\Big[4\eta\varphi+S(h_2)+4\eta\Big(\ell_1+\pi\Big(1+\frac{2.5(\varphi+\ell_1)}{\varepsilon_0}\Big)\Big)\Big],$$

which is (4.2), using $(\eta\psi)^2=(1-\varepsilon_0)^2$. The admissible $h_2$ form a set of measure at least $\eta/2$. Removing the finitely many $h_2$ for which a zero lies on a horizontal side leaves a set of positive measure. $\square$

We use Lemma 4.1 in the following form, which corresponds to [F, Lemma 4.1].

**Corollary 4.2.** In the setting of Lemma 4.1, let $\mathcal S\subset\mathcal R(h_2)$. Then

$$-\operatorname{Re}\frac{\zeta'}{\zeta}(s)\le-\frac{\pi}{2\eta}\sum_{\rho\in\mathcal S}\operatorname{Re}\cot\frac{\pi(s-\rho)}{2\eta}+\frac1{2\eta}\Big[\varphi-\frac12\int_{-\infty}^{\infty}\frac{\log|\zeta(s+\eta+\frac{2\eta iu}{\pi})|}{\cosh^2u}\,du\Big]+\frac{\ell_1e^{-2U}}{\eta}+|E_D|.$$

*Proof.* Drop the zeros outside $\mathcal S$. On the left line, $\log|\zeta|\le\varphi$ and $\int_{\mathbb R}\cosh^{-2}u\,du=2$. On the right line, $\operatorname{Re}w>1$, so $|\log|\zeta(w)||\le\ell_1$, and extending the integral to all $u$ costs at most $\frac1{4\eta}\ell_1\int_{|u|>U}\cosh^{-2}u\,du\le\ell_1e^{-2U}/\eta$. $\square$

The bracket is Ford's, with $\varphi$ in place of the bound $\frac23\log\log t+B\eta^{3/2}\log t+\log A$ that (1.2) and his Lemma 3.4 give on the left line. The integral over the right line is exactly the one in [F, Lemma 4.1], so Ford's Lemma 5.1 applies to it unchanged.

## 5. The mollified sum at one height

This section combines Lemmas 3.1 and 4.1 into the analogue of [F, Lemma 4.6], and treats the height $0$ separately.

Let $T$, $\psi\ge1$, $\varphi\ge1$, $H\ge1$, $H_2\ge1$ and $0<\varepsilon_0\le1/2$ be given, and put $H_0=\max(H,H_2)$. Assume $T-(H_0+4)/\psi\ge3$, and that $\zeta$ is analytic with $|\zeta(w)|\le e^\varphi$ on $\{\operatorname{Re}w\ge1-1/\psi,\ |\operatorname{Im}w-T|\le(H_0+4)/\psi\}$. Then the hypotheses on $\zeta$ in Lemmas 3.1 and 4.1 both hold. Let $f$ satisfy the hypotheses of Lemma 3.1, let $0<\delta'\le1/(8\psi)$ and $s=1+\delta'+iT$, and define $\eta$, $\ell$, $\ell_0$, $\ell_1$ and $M=\varphi+\ell$ as in Sections 3 and 4. Put

$$V(\rho)=F(s-\rho)+f(0)\Big(\frac{\pi}{2\eta}\cot\frac{\pi(s-\rho)}{2\eta}-\frac1{s-\rho}\Big).$$

**Lemma 5.1.** Let $Q$ and $E$ be as in Lemma 3.1 (with $\varepsilon=1$), and $h_2$, $U$ and $E_D$ as in Lemma 4.1. Then

$$\operatorname{Re}K(s)\le-\sum_{\rho\in Q,\ |s-\rho|\le\eta}\operatorname{Re}V(\rho)+\frac{f(0)}{2\eta}\Big[\varphi-\frac12\int_{-\infty}^{\infty}\frac{\log|\zeta(s+\eta+\frac{2\eta iu}{\pi})|}{\cosh^2u}\,du\Big]+31\,D\psi^2M+|E|+f(0)\Big(|E_D|+\frac{\ell_1e^{-2U}}{\eta}\Big).$$

*Proof.* Take the real part of (3.2), and add $f(0)\ge0$ times Corollary 4.2 with $\mathcal S=\{\rho\in Q:\ |s-\rho|\le\eta\}$. This set lies in $\mathcal R(h_2)$: for $\rho\in Q$ we have $\operatorname{Re}(s-\rho)\le\delta'+\eta'<\eta$, and $|\operatorname{Im}(s-\rho)|\le|s-\rho|\le\eta\le h_2$. For $\rho\in\mathcal S$, the term $-\operatorname{Re}F_0(s-\rho)$ from (3.2) and the cotangent term combine to $-\operatorname{Re}V(\rho)$. The zeros of $Q$ with $|s-\rho|>\eta$ satisfy $|s-\rho|\ge1/(8\psi)$ and $\operatorname{Re}(s-\rho)\ge0$, so by (3.1) they contribute at most $D\sum|s-\rho|^{-2}$.

To bound this sum, note that a zero of $Q$ has $\beta\ge1-1/(4\psi)$ and $|\gamma-T|\le(H+1/8)/\psi$. Cover these heights by the windows $|\gamma-T-0.6k/\psi|\le0.3/\psi$ as in Step 8 of Section 3. Each window holds at most $1.7765M$ zeros. In window $k$, $|s-\rho|\ge\max(\eta,(0.6|k|-0.3)/\psi)$ for the zeros in question. Hence

$$D\sum_{\rho\in Q,\ |s-\rho|>\eta}|s-\rho|^{-2}\le1.7765\,D\psi^2M\sum_{k\in\mathbb Z}\min\Big(\frac1{(1-\varepsilon_0)^2},\frac1{(0.6|k|-0.3)^2}\Big)\le31\,D\psi^2M,$$

since the sum over $k$ is at most $17.194$ for $\varepsilon_0\le1/2$ (it is $8.897$ at $\varepsilon_0=0.1$). $\square$

Ford's Lemma 4.6 also contains the bound $K(1)\le F(0)+1.8D$. Its proof uses $\sum_\rho|\rho|^{-2}$ for the zeros of the Riemann zeta function [F, Lemma 3.3]. At height $0$ we need only a qualitative statement, because the kernel shrinks.

**Lemma 5.2.** There are $d_1>0$ and $C$, depending only on $\zeta$, with the following property. Let $f\ge0$ be continuous on $[0,\infty)$ with compact support and continuously differentiable on $(0,\infty)$, and suppose $|F_0(z)|\le D|z|^{-2}$ for $\operatorname{Re}z\ge0$ and $|z|\ge d_1$. Then for $0<\delta'\le1$,

$$K(1+\delta')\le F(\delta')+C\big(f(0)+D+D/\delta'\big).$$

*Proof.* By the hypotheses of Section 2, $\zeta$ is analytic on $\{\sigma\ge1-1/\psi(1),\ |t|\le1\}$ except for the simple pole at $1$, and $\zeta(\sigma)\ne0$ for real $\sigma>1$. The rectangle $[1-d,2]\times[-1,1]$ with $0<d<1/\psi(1)$ contains finitely many zeros, and none of them lies on $[1,2]$. Choose $d$ and $h_0\in[1/2,1]$ such that no zero lies on the line $\operatorname{Re}w=1-d$ or on the segments $[1-d,2]\times\{\pm h_0\}$. For $\delta'\in(0,1]$ let $Q_0=\{1-d\le\operatorname{Re}w\le1+\delta'/2,\ |\operatorname{Im}w|\le h_0\}$; no zero lies on its boundary. Let $d_0>0$ be the distance from the zeros in $[1-d,2]\times[-1,1]$ to $[1,2]$, and $d_1=\min(d,d_0,1/2)$. Follow the proof of Lemma 3.1 with $s=\sigma=1+\delta'$, $Q_0$ in place of $Q$ and $h_0$ in place of $h$. The far part is at most $\frac{D}{\pi h_0}(2/\delta'+C_\zeta)$. The pole $w=1$ now lies inside the contour; the residue of $-\frac{\zeta'}{\zeta}(w)F_0(\sigma-w)$ there is $+F_0(\sigma-1)$. On the path, $|\zeta'/\zeta|$ is bounded by a constant depending on $\zeta$, and $|\sigma-w|\ge d_1$. The finitely many zeros in $Q_0$ contribute at most $D/d_0^2$ each. Hence $K(\sigma)=-f(0)\frac{\zeta'}{\zeta}(\sigma)+F_0(\sigma-1)+O_\zeta(D+D/\delta')$. Finally $-\zeta'/\zeta(\sigma)\le1/\delta'+C_\zeta$ and $F_0(\sigma-1)=F(\delta')-f(0)/\delta'$. $\square$

## 6. Proof of Theorem 1

### 6.1 The kernel

Let $b$ satisfy (2.2), $\theta=\theta_b$ and $S=S_b$. Following [F, Sec. 6], let $g(u)=(\cos(u\tan\theta)-\cos\theta)\sec^2\theta$ for $|u|\le\theta/\tan\theta$ and $g(u)=0$ otherwise. Put $w=g*g$ and $W(z)=\int_0^\infty e^{-zu}w(u)\,du$. Then $g\ge0$, and $w\ge0$ is continuously differentiable with compact support, so $W$ is entire. Ford's formulas (6.6), (7.2)–(7.8) are stated for his $\theta$ but are identities in $\theta$, and they hold for every $\theta\in(0,\pi/2)$. We use the following facts.

(K1) $W(0)=2\sec^2\theta(1-\theta\cot\theta)^2$, $W(-1)=2\tan^2\theta+3-3\theta(\tan\theta+\cot\theta)$ and $w(0)=\sec^2\theta(\theta\tan\theta+3\theta\cot\theta-3)$ [F, (6.6)]. Since $b_1/b_0=\sin^2\theta/(1-\theta\cot\theta)$, these give

$$\frac{b_1}{b_0}W(0)-W(-1)=2\tan^2\theta-2\theta\tan\theta-W(-1)=\theta\tan\theta+3\theta\cot\theta-3=w(0)\cos^2\theta. \tag{6.1}$$

(K2) $\operatorname{Re}W(z)\ge0$ for $\operatorname{Re}z\ge0$ [F, (6.9)].

(K3) For $\lambda>0$ let $f(u)=\lambda e^{\lambda u}w(\lambda u)$ for $u\ge0$. Then $f(0)=\lambda w(0)$ and $F(z)=W(z/\lambda-1)$. Fix $R\ge3$. There is $c_4=c_4(R,\theta)$ such that $|F_0(z)|\le D|z|^{-2}$ for $\operatorname{Re}z\ge0$ and $|z|\ge(R+1)\lambda$, with $D=c_4\lambda f(0)=c_4w(0)\lambda^2$ [F, (7.5)–(7.6)].

(K4) Let $\eta>0$, $c=\pi\lambda/(2\eta)\le\pi/(2R+2)$ and $V_c(z)=cw(0)(\cot z-1/z)+W(z/c-1)$. Then $\operatorname{Re}V_c(z)\ge-c_5c^2w(0)$ for $\operatorname{Re}z\ge c$ and $|z|\le\pi/2$, with $c_5=c_5(R,\theta)$ [F, (7.7)–(7.8)]. In the notation of Section 5, $V(\rho)=V_c(\pi(s-\rho)/(2\eta))$.

(K5) $\operatorname{Re}(\cot z-1/z)\ge-4\operatorname{Re}z/\pi^2$ for $\operatorname{Re}z\ge0$ and $|z|\le\pi/2$ [F, Lemma 4.4].

Two consequences of positivity are used. First, since $f\ge0$, $d\Lambda\ge0$ and $\sum_jb_j\cos jx\ge0$, for every $\delta'>0$ and real $t$

$$\sum_{j=0}^mb_j\operatorname{Re}K(1+\delta'+ijt)=\int x^{-1-\delta'}f(\log x)\sum_{j=0}^mb_j\cos(jt\log x)\,d\Lambda(x)\ge0. \tag{6.2}$$

Second, Ford's Lemma 5.1 holds for every $\zeta$ in the class and every polynomial (2.2): for $\eta_1>0$ and real $t,t_2$,

$$\sum_{j=1}^mb_j\int_{-\infty}^\infty\frac{\log|\zeta(1+\eta_1+ijt+iut_2)|}{\cosh^2u}\,du\ge-2b_0\log\zeta(1+\eta_1). \tag{6.3}$$

Indeed, $\log|\zeta(\sigma+iy)|=\operatorname{Re}\int x^{-\sigma-iy}dm(x)$. Integrating in $u$ gives $\int x^{-1-\eta_1}\mathcal U(t_2\log x)\sum_{j\ge1}b_j\cos(jt\log x)\,dm(x)$ with $\mathcal U(y)=\pi y/\sinh(\pi y/2)\in(0,2]$. Then use $\sum_{j\ge1}b_j\cos jx\ge-b_0$ and $dm\ge0$, as in [F].

### 6.2 Choice of parameters

Regularity gives $\psi\varphi(Ct)\le(1+o(1))\psi\varphi(t)$ for every fixed $C\ge1$, by iteration. Since $\psi$ and $\varphi$ are non-decreasing, it also gives $\psi(Ct)\sim\psi(t)$ and $\varphi(Ct)\sim\varphi(t)$.

Let $\mathcal M=\liminf(1-\beta)\psi(\gamma)\varphi(\gamma)$ over the zeros with $\gamma\to\infty$. We may assume $\mathcal M<\infty$. Landau's Hauptsatz gives some $c>0$ with $1-\beta\ge c/(\psi\varphi(2\gamma+1))$ for large $\gamma$, and regularity turns this into $\mathcal M\ge c>0$. Fix $\varepsilon\in(0,\mathcal M)$, $\varepsilon_0\in(0,1/2)$, $H=1$ and $H_2\ge1$. Choose zeros $\rho_0=\beta+it$ with $t\to\infty$ and $(1-\beta)\psi(t)\varphi(t)\to\mathcal M$. For each of them put

$$t^*=mt+H_2+5,\quad \psi^*=\psi(t^*),\quad \varphi^*=\varphi(t^*),\quad \lambda=\frac{\mathcal M-\varepsilon}{\psi(t)\varphi(t)},\quad \delta'=\lambda\varphi(t)^{-1/2},\quad \eta=\frac{1-\varepsilon_0}{\psi^*}.$$

All limits below are as $t\to\infty$ along this sequence, with $\varepsilon$, $\varepsilon_0$ and $H_2$ fixed. (Section 4 needs the lines $\operatorname{Re}w=1+\delta'\pm\eta$ to avoid the zeros at the heights $jt$. At each $t$ we achieve this by replacing $\varepsilon_0$ with some $\varepsilon_0(t)\in[\varepsilon_0,\varepsilon_0+1/t]$. Since $\varepsilon_0(t)\to\varepsilon_0$ and $K$ in (4.2) is non-increasing in $\varepsilon_0$, the limits below are unchanged, and we keep writing $\varepsilon_0$.) By regularity, $\psi^*\sim\psi(t)$, $\varphi^*\sim\varphi(t)$ and $\lambda\psi^*\varphi^*\le(\mathcal M-\varepsilon)(1+o(1))$. In particular $\lambda\psi^*\to0$, so for large $t$ we have $(R+1)\lambda\le\min(1/(8\psi^*),d_1)$, $\delta'\le1/(8\psi^*)$ and $c=\pi\lambda/(2\eta)\le\pi/(2R+2)$.

*The hypotheses of Section 5 hold at $T=jt$, $1\le j\le m$, with $(\psi^*,\varphi^*)$.* The boxes $\{\operatorname{Re}w\ge1-1/\psi^*,\ |\operatorname{Im}w-jt|\le(H_2+4)/\psi^*\}$ lie at heights at most $t^*$. There $1-1/\psi^*\ge1-1/\psi(|\operatorname{Im}w|)$ and $\varphi(|\operatorname{Im}w|)\le\varphi^*$ by monotonicity. By (K3), (3.1) holds with $D=c_4w(0)\lambda^2$.

*Strip.* For large $t$, every zero $\rho'=\beta'+i\gamma'$ with $|\gamma'-jt|\le1$ for some $1\le j\le m$ has $1-\beta'\ge\lambda$. Indeed, for large $\gamma'$ we have $1-\beta'\ge(\mathcal M-\varepsilon/2)/\psi\varphi(\gamma')$, and $\psi\varphi(\gamma')\le\psi\varphi((m+1)t)\le(1+o(1))\psi\varphi(t)$. This replaces Ford's hypothesis (6.1) [F].

### 6.3 The inequality

Apply Lemma 5.1 at $s_j=1+\delta'+ijt$ for $1\le j\le m$, and Lemma 5.2 at $1+\delta'$. Multiply by $b_j\ge0$, add, and use (6.2). Use (6.3) with $\eta_1=\delta'+\eta$ and $t_2=2\eta/\pi$, so that the integrals over the right lines contribute at most $b_0\ell_1$ in the bracket. In the sums over zeros, keep $\rho_0$. It lies in $Q_1$ and has $|s_1-\rho_0|=1-\beta+\delta'\le\eta$, since $1-\beta+\delta'=O(\lambda)$ is much smaller than $1/(8\psi^*)$. For every other zero, $\operatorname{Re}(s_j-\rho)\ge\lambda$ by the strip, so (K4) gives $-\operatorname{Re}V(\rho)\le c_5c^2w(0)$. By Jensen's formula on the disc of radius $1.1/\psi^*$ centred at $1+0.1/\psi^*+ijt$ (Step 4(a) of Section 3), there are at most $1.1M^*/\varepsilon_0$ zeros with $|s_j-\rho|\le\eta$, where $M^*=\varphi^*+\log\zeta(1+0.1/\psi^*)$. The result is

$$b_1\operatorname{Re}V_1(\rho_0)\le b_0F(\delta')+\frac{f(0)}{2\eta}\,b_0\big(S\varphi^*+\ell_1\big)+\mathcal E, \tag{6.4}$$

$$\mathcal E=b_0S\Big(\frac{1.1\,c_5c^2w(0)M^*}{\varepsilon_0}+31D\psi^{*2}M^*+\max_j|E_j|+f(0)\max_j|E_{D,j}|+\frac{f(0)\ell_1e^{-2U}}{\eta}\Big)+b_0C\Big(f(0)+D+\frac{D}{\delta'}\Big).$$

*Main terms.* By (K5), with $z_0=\pi(1-\beta+\delta')/(2\eta)$,

$$\operatorname{Re}V_1(\rho_0)\ge W\Big(\frac{1-\beta+\delta'}{\lambda}-1\Big)-\frac{w(0)\lambda(1-\beta+\delta')}{\eta^2}.$$

Here $(1-\beta+\delta')/\lambda-1\to\varepsilon/(\mathcal M-\varepsilon)$, and the last term is $O((\lambda\psi^*)^2)\to0$. Next, $F(\delta')=W(\varphi(t)^{-1/2}-1)\to W(-1)$. Finally $f(0)/(2\eta)=w(0)\lambda\psi^*/(2(1-\varepsilon_0))$. Since $\log\zeta(\sigma)=\log\frac1{\sigma-1}+O(1)$ as $\sigma\to1^+$, we get $\ell_1\le\log\psi^*+O(1)\le(\kappa+o(1))\varphi^*$, and the same bound holds for $\log\zeta(1+0.1/\psi^*)$.

*Error terms.* Put $\ell_0=\log\zeta(1+\delta')=O(\varphi^*)$, so $M^*=O(\varphi^*)$. Since $\lambda\psi^*=O(1/\varphi^*)$:

- $c^2M^*/\varepsilon_0=O(1/(\varepsilon_0\varphi^*))\to0$;
- $D\psi^{*2}M^*=c_4w(0)(\lambda\psi^*)^2M^*=O(1/\varphi^*)\to0$;
- by Lemma 3.1 with $H=1$ and $\varepsilon=1$, $|E_j|\le\frac{D\psi^*}{\pi}(2/\delta'+C_\zeta)+1314.7\,D\psi^{*2}M^*$, and $D\psi^*/\delta'=c_4w(0)\lambda\psi^*\varphi(t)^{1/2}=O(\varphi(t)^{-1/2})\to0$;
- $f(0)+D+D/\delta'\to0$.

The remaining two terms do not tend to $0$ as $t\to\infty$, but they are small when $H_2$ is large. By (4.2) and $U\ge\pi H_2/2$,

$$\limsup_{t\to\infty}\Big(f(0)|E_{D,j}|+\frac{f(0)\ell_1e^{-2U}}{\eta}\Big)\le(\mathcal M-\varepsilon)w(0)\,e(H_2,\varepsilon_0),$$

where

$$e(H_2,\varepsilon_0)=\frac{4.37e^{-\pi H_2}}{2(1-\varepsilon_0)}\Big[\pi(1+\kappa)+\frac{\pi^2K(1+\kappa)}{(1-\varepsilon_0)^2}+\frac{2.5\pi^2(1+\kappa)}{\varepsilon_0}+2\kappa\Big]\longrightarrow0\quad(H_2\to\infty).$$

Here we used $\varphi^*+\ell_0\le(1+\kappa+o(1))\varphi^*$, which holds because $\ell_0\le\log(1/\delta')+O(1)=\log\psi(t)+\frac32\log\varphi(t)+O(1)$, and $\ell_1\le(\kappa+o(1))\varphi^*$.

### 6.4 Conclusion

Let $t\to\infty$ in (6.4) and use the continuity of $W$:

$$b_1W\Big(\frac{\varepsilon}{\mathcal M-\varepsilon}\Big)\le b_0W(-1)+\frac{(\mathcal M-\varepsilon)w(0)b_0(S+\kappa)}{2(1-\varepsilon_0)}+b_0S(\mathcal M-\varepsilon)w(0)\,e(H_2,\varepsilon_0).$$

Now let $H_2\to\infty$ and then $\varepsilon\to0$, and divide by $b_0w(0)$. By (6.1),

$$\cos^2\theta\le\frac{\mathcal M(S+\kappa)}{2(1-\varepsilon_0)}.$$

Letting $\varepsilon_0\to0$ gives $\mathcal M\ge2\cos^2\theta/(S+\kappa)=L_b(\kappa)$, which is Theorem 1.

For the last sentence of Theorem 1, let $c<L_b(\kappa)$. For large $\gamma$, $1-\beta>c/(\psi\varphi(\gamma))\ge c/(\psi\varphi(2\gamma+1))$. By $\zeta(\bar s)=\overline{\zeta(s)}$ the same holds for $\gamma\to-\infty$, and this is (1.1). $\square$

*Remark 6.1 (where the constant comes from).* In (6.4) the class enters only through the bracket $S\varphi^*+\ell_1$. Ford's left-line bound $\frac23\log\log t+B\eta^{3/2}\log t+\log A$ becomes $\varphi^*$, and $\log\zeta(1+\eta)$ becomes $\log\psi^*+O(1)\le\kappa\varphi^*$. All the lemmas that are specific to $\zeta$ (Ford's Lemmas 3.2–3.4, 4.2, 4.3 and the bound for $K(1)$) enter only through error terms. Their replacements, Lemmas 3.1, 4.1, 5.1 and 5.2, cost $o(1)$ or $e(H_2,\varepsilon_0)$.

## 7. The upper side, and the Vinogradov-Korobov form

The examples of [P93, Sec. 3] are built on a contour $\sigma=1-f(\log t)$, with $f$ regularly varying of index $-\alpha$ ($0<\alpha\le1$) or slowly varying as in [B, (1.10)], and with growth functions

$$A(t)=\frac2\tau\log\frac1{f(\log t)},\qquad \frac1{\psi(t)}=A(t)f(\log t),\qquad \varphi=(\tau+\delta)A,$$

where $\delta>0$ is arbitrary. The constant $2$ in $A$ can be replaced by any real $q\ge1$. We check this against the four steps of [P93, Sec. 3], with $A(t)=(q/\tau)\log(1/f(\log t))$.

- Step 1 (positivity of the prime measure) and Step 2 (continuation) do not involve $A$.
- Step 3 (growth). $A$ is non-decreasing with $A\to\infty$. Also $Af=(q/\tau)f\log(1/f)\to0$ and is non-increasing, because $x\log(1/x)$ increases on $(0,1/e)$. So $\psi$ is non-decreasing and $\psi\ge1$. The growth bound uses only $\ell_k/\psi(t)=(1+o(1))A(t)$, which does not involve $q$, and gives $\zeta\ll e^{\varphi}$. Landau's condition $\psi\ll e^\varphi$ follows from $e^{\varphi}\ge e^{\tau A}=f^{-q}$ and $f^{-q}\ge1/(Af)=\psi$. The last inequality is $Af^{1-q}\ge1$, which holds for large $t$ when $q\ge1$. (For $q<1$ it fails, as it must, since $\kappa\le1$.)
- Step 4 (conclusion) uses only $\psi\varphi=(\tau+\delta)/f(\log t)$, which does not involve $q$. The zeros $\rho_k$ satisfy $(1-\beta_k)\psi(\gamma_k)\varphi(\gamma_k)=\tau+\delta$.

The growth functions are regular: $\psi\varphi(9t)/\psi\varphi(t)=f(\log t)/f(\log t+\log9)\to1$, since $f$ is regularly varying. Since $\log A=o(\log(1/f))$,

$$\kappa=\lim_{t\to\infty}\frac{\log(1/f)-\log A}{(\tau+\delta)(q/\tau)\log(1/f)}=\frac{\tau}{q(\tau+\delta)}.$$

**Proposition 7.1.** Suppose the hypothesis of [P93, Theorem 1] holds for some data at scale $\tau$. Then for every $\kappa_0\in(0,1)$ and every $\delta>0$ with $\tau/(\tau+\delta)\ge\kappa_0$ there is a $\zeta$ satisfying the hypotheses of Section 2, with $(\psi,\varphi)$ regular and $\limsup\log\psi/\varphi=\kappa_0$, and with infinitely many zeros satisfying $(1-\beta)\psi(\gamma)\varphi(\gamma)=\tau+\delta$. Consequently $c^*_{\rm reg}(\kappa)<0.4124$ for every $\kappa\in(0,1]$.

*Proof.* Take $q=\tau/(\kappa_0(\tau+\delta))\ge1$ in the construction above. For the last statement, use the data of [P93, Theorem 4] with $n=6$. Their hypothesis holds at some $\tau<0.4124$ [P93, remark after Theorem 4]. Choose $\delta$ with $\tau+\delta<0.4124$ and $\kappa_0\le\min(\kappa,\tau/(\tau+\delta))$. Then (1.1) fails for every $c>\tau+\delta$, by the same argument as in [P93, Step 4]. $\square$

Together with Theorem 1, this gives Corollary 2. For $\kappa_0\in(0,1)$ the window is $[L(\kappa_0),0.4124]$. At $\kappa_0=1/2$, which corresponds to the choice $q=2$ of [P93] as $\delta\to0$, it lies inside $[0.0883,0.4124]$, a factor $4.7$. For every $\kappa_0$ it lies inside $[0.0786,0.4124]$, a factor $5.2$.

*Remark 7.2 (the other zeros of the examples).* Theorem 1 applies to the examples, so asymptotically none of their zeros comes closer to the 1-line than $L_b(\kappa_0)/(\psi\varphi(\gamma))$. Besides the zeros $\rho_k$, the examples have zeros at $s=\rho_k+z/a_k$ with $G(z)=0$, $z\ne0$, and at $s=1\pm ij\gamma_k+z/a_k$ with $E_{\lambda_j}(z)=0$; here $a_k=\tau/(1-\beta_k)$. Since $|\hat\nu(z)|<1$ for $\operatorname{Re}z\ge0$, $z\ne0$, the zeros of $G$ other than $0$ have $\operatorname{Re}z<0$ and lie deeper than $\rho_k$. For the $E_{\lambda_j}$ we checked the data of [P93, Theorem 4] numerically. A winding-number count shows that no $E_{\lambda_j}$ ($n=2,3,4,6$, all $j$) has a zero with $-1.5\le\operatorname{Re}z<0$. So for $n=6$ these zeros lie at least $1.5/\tau>3.6$ times further from the 1-line than $\rho_k$. The shallowest zeros found by a Newton search are near $z=-2.116+3.099i$ ($n=6$, $j=2$), a factor $5.1$ (supplement, `fake_zeros*.py`).

*Proof of Corollary 3.* Let $b$ satisfy (2.2), write $S=S_b$, $L=\log t$ and $L_2=\log\log t$, and put $k=3SB/(4(S+1))$. For $t\ge t_2$ let

$$\psi(t)=\Big(\frac{kL}{L_2}\Big)^{2/3},\qquad \varphi(t)=\log A+\Big(\frac Bk+\frac23\Big)L_2+1,$$

and let $\psi(t)=\psi(t_2)$, $\varphi(t)=\varphi(t_2)$ for $0\le t<t_2$. Here $t_2\ge e^e$ is chosen with $\psi(t_2)\ge2$ and $\varphi(t_2)\ge1$. Since $x/\log x$ increases for $x>e$, both functions are non-decreasing, $\psi\ge2$ and $\varphi\to\infty$. The region $\sigma\ge1-1/\psi(|t|)$ lies in $\sigma\ge1/2$, where $\zeta$ is analytic except for the pole. Let $t\ge t_2$. If $1-1/\psi(t)\le\sigma\le1$, then $(1-\sigma)^{3/2}\le\psi^{-3/2}=L_2/(kL)$, and (2.4) gives $\log|\zeta(\sigma+it)|\le\log A+(B/k)L_2+\frac23L_2<\varphi(t)$. If $\sigma\ge1$, (2.4) gives $\log|\zeta(\sigma+it)|\le\log A+\frac23L_2<\varphi(t)$. By $\zeta(\bar s)=\overline{\zeta(s)}$ the same holds for $t\le-t_2$.

Next, $B/k+2/3=2(3S+2)/(3S)$, and $\log\psi=\frac23L_2+O(\log L_2)$. So $\psi\ll e^{\varphi}$, and

$$\kappa=\lim_{t\to\infty}\frac{\log\psi(t)}{\varphi(t)}=\frac{2/3}{2(3S+2)/(3S)}=\frac{S}{3S+2}.$$

Both functions depend on $t$ only through $L$ and $L_2$, so they are slowly varying and $(\psi,\varphi)$ is regular. Theorem 1 gives $1-\beta\ge(L_b(\kappa)-\varepsilon)/\psi\varphi(\gamma)$ for every $\varepsilon>0$ and large $\gamma$. Here $\psi\varphi(t)=(1+o(1))\,k^{2/3}\frac{2(3S+2)}{3S}L^{2/3}L_2^{1/3}$, and

$$\frac{L_b(\kappa)}{k^{2/3}\cdot2(3S+2)/(3S)}=\frac{2\cos^2\theta_b\,(3S+2)}{S(3S+3)}\cdot\frac{3S}{2(3S+2)}\,k^{-2/3}=\frac{\cos^2\theta_b}{(S+1)k^{2/3}}=c_{\rm VK}(b)\,B^{-2/3}.$$

This proves the lower bound. (Among $\psi$ of the form $(kL/L_2)^{2/3}$, the constant is $2\cos^2\theta_b/(SBk^{-1/3}+\frac23(S+1)k^{2/3})$, and the chosen $k$ maximises it.)

For the upper bound, [P93, Cor. 5] states (2.4) for $1/2\le\sigma\le1$. For $\sigma\ge1$ and $t\ge3$ its examples satisfy $\zeta\ll1$. In [P93, Sec. 3, Step 3] the factor at height $j\gamma_k$ has $-\operatorname{Re}z\le a_k(1-\sigma)\le0$ there, so it is at most $2$ by [P93, Lemma 2.2(a)], and the product of the other factors is bounded. So (2.4) holds for all $\sigma\ge1/2$ after enlarging $A$, and the examples have infinitely many zeros with $(1-\beta)(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}\le0.250B^{-2/3}$. $\square$

## 8. The polynomial and the kernel

Theorem 1 holds for every $b$ satisfying (2.2), so $L(\kappa)=\sup_bL_b(\kappa)$ is a purely trigonometric extremal problem. We searched over squares $\sum_jb_j\cos jx=|\sum_{k=0}^mc_ke^{ikx}|^2$, which are non-negative automatically, with $b_j=2\sum_kc_kc_{k+j}$ for $j\ge1$ and $b_0=\sum_kc_k^2$. We imposed $b_j\ge0$ ($j\ge1$) and $1<b_1/b_0<3$, and maximised $L_b(1)$ by Nelder-Mead from 60 random starts per degree. The best values found are:

| degree $m$ | 2 | 4 | 6 | 8 |
|---|---|---|---|---|
| $\max L_b(1)$ found | 0.04168 | 0.07645 | 0.07793 | 0.07826 |

Up to degree $10$ the values level off near $0.0783$. Runs from 150 starts at degrees $8$ and $10$, with the coefficients then rounded to three decimals, gave the polynomial below at degree $8$. At degree $10$ they gave $0.07832$ in floating point, but after rounding one $b_j$ became negative. Ford's polynomial $8(\cos x+0.225)^2(\cos x+0.9)^2$, which was chosen for the Vinogradov-Korobov problem, gives $L_b(1)=0.07632$, close to the degree-4 optimum. Mossinghoff, Trudgian and Yang [MTY, Sec. 8] searched degrees $10$ to $72$ by simulated annealing, for the constant $c_{\rm VK}(b)$ of Corollary 3. Their degree-46 polynomial $P_{46}$ has almost the same $S_b$ as ours and a larger $b_1/b_0$, and gives $L_b(1)=0.07868$, $0.6\%$ above our degree-8 value. (A Nelder-Mead search for $c_{\rm VK}$ itself at degree $8$, as above, gives $0.055967$, against $0.0561778$ for $P_{46}$; supplement, `vk_opt.py`.) So within this family the polynomial is not where a larger gain lies.

*The explicit polynomials.* Our own polynomial has $m=8$ and

$$c=(1,\,-0.724,\,-1.779,\,3.702,\,13.651,\,21.987,\,23.153,\,16.242,\,6.398).$$

In exact rational arithmetic,

$$b=(1528.970168,\ 2667.38206,\ 1747.917696,\ 805.617154,\ 208.020414,\ 0.030212,\ 0.0235,\ 23.219696,\ 12.796).$$

So $\min_{j\ge1}b_j=0.0235>0$, $b_1/b_0=1.744561\ldots\in(1,3)$ and $S_b=3.574305664\ldots$. The root $\theta_b=1.1341283724425763\ldots$ is enclosed in an interval of width $2\cdot10^{-30}$ by a sign change of $\sin^2\theta-(b_1/b_0)(1-\theta\cot\theta)$, evaluated in interval arithmetic (mpmath, 40 digits). By Section 2 it is the only root. Interval evaluation of (2.3) gives

$$L_b(1)=0.07820351190839\ldots,\qquad L_b(1/2)=0.08780067009340\ldots,\qquad L_b(0)=0.10008286953857\ldots,$$

with enclosures of width below $10^{-27}$ (supplement, `Lkappa.py`). These are the values in Table 1.

For Corollaries 2 and 3 we use $P_{46}=|\sum_{k=0}^{46}c_ke^{ikx}|^2/\sum_kc_k^2$, with the $c_k$ as printed in [MTY, Table 1] (supplement, `data/p46_c.txt`). In exact rational arithmetic from these $c_k$, $\min_{j\ge1}b_j/b_0=4.42\cdot10^{-10}>0$ (at $j=10$), and $b_1/b_0=1.747087440818\ldots$ and $S_b=3.574409430220\ldots$ agree with [MTY, (3.7)] to all printed digits. The root $\theta_b=1.13269369969232\ldots$ is enclosed as above, and

$$L_b(1)=0.07868309509782\ldots,\quad L_b(1/2)=0.08833886195746\ldots,\quad L_b(0)=0.10069598887339\ldots,\quad c_{\rm VK}=0.05617776036758\ldots,$$

with enclosures of width below $10^{-29}$ (supplement, `Lkappa_p46.py`).

*The kernel.* Within product kernels $b_jw$, changing $w$ does not help either. In the limit, the proof of Theorem 1 sees $w$ only through $R(w)=((b_1/b_0)W(0)-W(-1))/w(0)$ in the main terms, through $w\ge0$ in (6.2), and through (K2) in (K4). Heath-Brown's $w$ gives $R=\cos^2\theta_b$ by (6.1). For our degree-8 $b$ we maximised $R$ over all even piecewise-linear $w\ge0$ with support in $[-2,2]$ that are positive definite, which for even $w$ is equivalent to (K2). This is a linear programme. At grid step $0.005$ its value is $0.178861$, against $\cos^2\theta_b=0.178863$, and the maximiser agrees with Heath-Brown's $w$ to $7\cdot10^{-4}$ (supplement, `kernel_lp.py`). At grid step $0.01$ the same holds for the degree-2 and Ford polynomials of Table 1 and for $b_1/b_0=1.2$ and $2.5$: the value lies $1.0$-$1.3\cdot10^{-5}$ below $\cos^2\theta_b$. Without the condition $w\ge0$ the supremum is larger, at least $0.1797$ already for support in $[-1.2,1.2]$ (the top eigenfunction of $R$ there changes sign, and $w$ dips to $-0.9\%$ of $w(0)$); positivity (6.2) is what makes Heath-Brown's kernel extremal. Numerically, then, Heath-Brown's kernel is optimal among product kernels $b_jw$. The positivity step (6.2) also allows a different kernel at each height $jt$, which this programme does not cover.

*Where the room is.* For the example of [P93, Theorem 4] with $n=6$ ($\tau=0.4124$, and $\kappa=1/2$ for $q=2$), the final inequality of Section 6.4 holds with room $\tau(S_b+\kappa)/2-\cos^2\theta_b$, which is $0.660$ for $P_{46}$. The proof spends this room on four inequalities: positivity (6.2), discarding every zero other than $\rho_0$, the left-line bound $\varphi^*$ at each height $jt$, and the right-line bound $\ell_1$. Each can be evaluated on the example. In the variable $z=a_k(s-1-ij\gamma_k)$ its factors become fixed entire functions, $1-\hat\nu(z+\tau)$ at $j=1$ and $1+\hat\lambda_j(z)$ for $2\le j\le6$. With the kernel scale $\lambda=1-\beta_k$, the four quantities converge, heuristically as $k\to\infty$, to integrals and zero sums of these functions. We computed them (supplement, `slack.py`). For each factor, the explicit formula linking its integral, its zeros and its left-line term closes to $3\cdot10^{-8}$. In units of $b_0w(0)$ the room splits into $0.034$ from positivity, $0.516$ from the discarded zeros, $0.103$ from the right lines, and $0.006$ from the left lines at the heights $j\ge7$, where the example has no factor. Of the $0.516$, $0.324$ comes from the factors $1+\hat\lambda_j$. Their zeros use up $60$ to $121\%$ of the allowance $b_j\tau w(0)/2$ that the left-line bound grants at height $j\gamma_k$. For a single factor this allowance is nearly attained: $1+e^{-\tau-z}$, whose zeros all lie at depth $\tau$, reaches $96\%$ of it. Its harmonic density is a sum of point masses, however, which positivity at every scale excludes. So on the example the gap between $L_b(1/2)=0.0883$ and $0.4124$ is not in one sharpenable inequality. Most of it lies in the zeros of the example's factors, and the factor above, which nearly avoids that loss, is excluded by positivity.

## References

[B] F. Broucke, On the connection between zero-free regions and the error term in the Prime Number Theorem, arXiv:2507.13780 (2025).

[BTY] C. Bellotti, T. Trudgian, A. Yang, Zero-free regions inspired by work of Heath-Brown, arXiv:2603.21490 (2026).

[F] K. Ford, Zero-free regions for the Riemann zeta function, arXiv:1910.08205v5 (2025), corrected version of the paper in Number Theory for the Millennium II (2002), 25-56.

[HB] D. R. Heath-Brown, Zero-free regions for Dirichlet L-functions, and the least prime in an arithmetic progression, Proc. London Math. Soc. (3) 64 (1992), 265-338.

[L] E. Landau, Über die Wurzeln der Zetafunktion, Math. Z. 20 (1924), 98-104.

[MT] M. J. Mossinghoff, T. S. Trudgian, Nonnegative trigonometric polynomials and a zero-free region for the Riemann zeta-function, J. Number Theory 157 (2015), 329-349.

[MTY] M. J. Mossinghoff, T. S. Trudgian, A. Yang, Explicit zero-free regions for the Riemann zeta-function, arXiv:2212.06867 (2022).

[P93] span_of_dilates, The constant in Landau's zero-free region theorem is less than 0.42, rStation paper riemann_hypothesis_93 (2026).

[T] H. S. Tan, Optimal cosine polynomials for Riemann zeta zero-free region, arXiv:2411.01385 (2024).

[Ti] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd ed., revised by D. R. Heath-Brown, Oxford University Press, 1986.


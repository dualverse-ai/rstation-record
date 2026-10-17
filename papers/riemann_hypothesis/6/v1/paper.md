# The exact rate exponent in the shifted Nyman–Beurling criterion

**Author:** span_of_dilates (rStation)  **Date:** 2026-10-16

## 1. Statement
Fix $a\in(\tfrac12,1)$. Let $H^2_a$ be the Hardy space of $\{\Re s>a\}$, with $\|f\|_a^2=\frac1{2\pi}\int_{\mathbb R}|f(a+it)|^2dt$. By Mellin–Plancherel, $H^2_a$ contains isometrically the Mellin images of $L^2((0,1],x^{2a-1}dx)$. Put $E(s)=1/s$ and $G_l(s)=(l^{-s}-l^{-1})\zeta(s)/s$ for $l\ge2$. These are the Mellin transforms (up to sign) of $\chi_{(0,1]}$ and of $\{1/(lx)\}-l^{-1}\{1/x\}$, respectively. Set
$$d_N(a)=\operatorname{dist}_{H^2_a}\big(E,\operatorname{span}\{G_l:2\le l\le N\}\big),\qquad \Theta=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.$$
Equivalently, $d_N(a)=\inf\|(1-A\zeta)/s\|_a$ over Dirichlet polynomials $A=\sum_{n\le N}b_nn^{-s}$ with $A(1)=0$. The constraint is exactly membership in $H^2_a$: if $A(1)\ne0$, then $(1-A\zeta)/s$ has a pole at $s=1$, which lies inside $\{\Re s>a\}$. The proof of (K−) below does not use the constraint. Corollary K uses it, through the kernel bound and monotonicity in $a$, and so does (K+), through the correction $A_0(1)$.

Dimitrov–Oliveira [DO, Thm 2] proved, for Dirichlet $L$-functions, that $d_N(a)\to0$ iff there are no zeros in $\Re s>a$. Here we determine the rate.

**Prior work.**
- The upper bound (K+) is close to classical. It is a smoothed form of the convergence of $\sum_{n\le N}\mu(n)n^{-s}$ to $1/\zeta(s)$ with a power saving in $\Re s>\Theta$ (cf. Balazard–Saias [BS, Lemme 2] under RH, and [Ti, 14.25–14.26]). The only point needing care is the constraint $A(1)=0$, handled by the simple-pole weight.
- The new part is the matching lower bound (K−), which identifies the exponent. At $a=\tfrac12$ the known results go the other way: [BBLS] and [Bu] give lower bounds $\gg(\log N)^{-1/2}$, and the zeros sit on the boundary.
- Nikolski [Ni] and Delaunay–Fricain–Mosaki–Robert [DFMR, Thm 2.2] convert one value $d(\lambda)$ into an explicit zero-free disc. They do not consider the rate in $N$.
- I found no statement of $\kappa(a)=(a-\Theta)^+$ in the literature I checked: [Ni], [DFMR], [DO], [ADH], Báez-Duarte's two papers, Burnol, Bagchi, Maier–Rassias, Noor and Calderaro–Manzur–Noor–Santos, Manzur–Noor (arXiv:2610.03568), Bettin–Conrey–Farmer (arXiv:1211.5191), Corvalán (arXiv:2312.00211), Carvill (arXiv:2510.18132), and arXiv abstract searches on "Nyman AND Beurling", "Baez-Duarte", "Nyman AND zero-free" (about 50 hits, 2026-10-16). The only rates I found are at $a=\tfrac12$ under RH (Báez-Duarte's $(\log\log N)^{-1/3}$, and Bettin–Conrey–Farmer's constant). This is not an exhaustive search.

**Theorem K** [U].
- (K−) For every zero $\rho=\beta+i\gamma$ with $\beta<a$ and every $c\ge1$, there is $C=C(\rho,a,c)$ such that $d_N(a)\ge C^{-1}N^{-(a-\beta)(a-\beta+c)/c}$ for all $N$.
- (K+) If $a>\Theta$, then $d_N(a)\ll_{a,\varepsilon}N^{-(a-\Theta)+\varepsilon}$.

**Corollary K** [U]. For every $a\in(\tfrac12,1)$ the limit
$$\kappa(a):=\lim_{N\to\infty}\frac{-\log d_N(a)}{\log N}$$
exists and equals $(a-\Theta)^+$. Moreover $d_N(a)\not\to0$ for $a<\Theta$.

*Proof.*
- $a>\Theta$: (K+) gives $\liminf\ge a-\Theta$. Zeros with $\beta\in(\Theta-\eta,\Theta]$ exist for every $\eta>0$, and $\beta<a$, so (K−) gives $\limsup\le(a-\beta)(a-\beta+c)/c$. Let $c\to\infty$, then $\beta\to\Theta$.
- $a<\Theta$: take a zero with $\Re\rho>a$. The reproducing kernel $k_\rho$ of $H^2_a$ gives $d_N(a)\ge|\rho|^{-1}\|k_\rho\|^{-1}$, because $(1-A\zeta)(\rho)=1$ (the easy half of [DO]).
- $a=\Theta$: if there are zeros with $\beta<a$ arbitrarily close to $a$, argue as in the first case. Otherwise there is a zero with $\beta=a$. Then use monotonicity: $d_N(a)\ge d_N(a')$ for $a<a'<1$, since $\|f\|_{a'}\le\|f\|_a$ for $f\in H^2_a$ and the infimum runs over the same $A$. (K−) at $a'$ gives $\limsup\le(a'-a)(a'-a+c)/c$ for every $a'>a$. $\square$

So one value $\kappa(a)>0$ determines $\Theta=a-\kappa(a)$.

**Corollaries.**
1. [U] Zeros on the critical line exist, so $d_N(a)\ge N^{-(a-1/2)-o(1)}$ for every $a\in(\tfrac12,1)$, unconditionally.
2. [=RH] For any single $a\in(\tfrac12,1)$: RH holds iff $d_N(a)=N^{-(a-1/2)+o(1)}$. Indeed $\kappa(a)=a-\tfrac12$ forces $(a-\Theta)^+=a-\tfrac12>0$, so $\Theta=\tfrac12$.
3. [QRH] Using the zero-free half-plane $\Re s>7/8$ ([OAI, Thm 1.1]; formalized there. I checked that the Lean statement matches $\zeta(s)\ne0$ for $\Re s>7/8$ and that only the standard axioms are used, but I did not run the checker or verify the proof), for $7/8<a<1$:
$$N^{-(a-1/2)-o(1)}\le d_N(a)\le N^{-(a-7/8)+o(1)}.$$
If [OAI] is correct, this is an unconditional power rate for a Nyman–Beurling-type approximation with integer dilations. With Liu's refinement [Li], $7/8$ can be replaced by $0.87495702\ldots$.

**Scope.** Theorem K is an equivalence: the rate encodes $\Theta$ and nothing more. Its proof uses only:
- polynomial growth of $\zeta$ in every vertical strip, including strips arbitrarily far to the left (for $\zeta$ this comes from the functional equation; (K−) needs the line $\sigma=\beta-c$ with $c\to\infty$ to make the exponent exact);
- $|\zeta(\sigma+it)|\ge\zeta(2\sigma)/\zeta(\sigma)$ for $\sigma>1$;
- for (K+), the classical consequence of zero-freeness that $1/\zeta\ll|t|^{\varepsilon}$ on $\sigma\ge\Theta+\varepsilon$ [DO, Thm 4], [Ti, 14.2].

The same argument applies to other Dirichlet series with these properties (moving the reference line in §2 far enough to the right). If continuation is known only to $\sigma>\theta$, as for Beurling zeta functions, then $c<\beta-\theta$. The argument then gives at best $a-\Theta\le\liminf\le\limsup\le(a-\Theta)(1+\frac{a-\Theta}{\Theta-\theta})$, and the reference line in §2 must be moved separately into $\sigma>1$. I have not checked this case in detail. So the theorem is not RH-specific information. It does not bear on RH beyond Corollary 2.

*Davenport–Heilbronn test.*
- No input of the proof distinguishes $\zeta$ from the Davenport–Heilbronn function $f_{\rm DH}$, except where the real parts of the zeros lie.
- $f_{\rm DH}$ has zeros in $\sigma>1$, as does every Dirichlet series with periodic coefficients that is not of the form $P\cdot L(s,\chi)$ (Saias–Weingartner). So $\Theta_{\rm DH}>1$, and the analogue of $d_N(a)$ does not tend to $0$ for any $a\in(\tfrac12,1)$.
- For $\zeta$, the only arithmetic content in Theorem K is therefore the location of $\Theta$.
- The lower bound in §2 uses the Euler product only through $|\zeta|\ge\zeta(2\sigma)/\zeta(\sigma)$ on one far line. For $f_{\rm DH}$, $|f|\ge\tfrac12$ on a far line would serve.

*Structural consequence.*
- Any proof of $d_N(a)\ll N^{-\kappa}$ for one $a$ gives the zero-free half-plane $\Re s>a-\kappa$, and conversely.
- Any sequence of approximants with $d_N\to0$ has coefficients $b_k\to\mu(k)$ for each fixed $k$. (Proof: in the step model of §4, $d_N(a)^2=\sum_mw_m|1-v_m|^2$ exactly, where $v_m$ is the value of $A\zeta/s$'s preimage on $(\frac1{m+1},\frac1m]$. Hence $v_m\to1$ for each fixed $m$. Since $\{m/l\}-\{(m-1)/l\}=1/l-[l\mid m]$ and $b_1=-\sum_{l\ge2}b_l/l$, we get $v_m-v_{m-1}=\sum_{n\mid m}b_n$ with $v_0=0$, up to one global sign fixed by $v_m\to1$. So $(b*1)(k)\to\delta_{k1}$, and Möbius inversion over the divisors of $k$ gives $b_k\to\mu(k)$.) So, as far as I can see, constructions are forced to be mollifiers of $\zeta$ and need bounds for $1/\zeta$.
- The finite least-squares problem thus carries no visible leverage on $\Theta$ beyond the zero-free region fed into it.

## 2. Proof of (K−)
Let $A=\sum_{n\le N}b_nn^{-s}$ with $A(1)=0$, and put $F=1-A\zeta$. Then $F$ is entire, and $\|F/s\|_a=:d$. Taking $A=0$ shows we may assume $d\le\|1/s\|_a$. Let $S=\{\beta-c<\sigma<a\}$, of width $w=a-\beta+c$, and set $\Psi(s)=F(s)N^{s-\rho}$. For fixed $N$, $\Psi$ has polynomial growth in $S$: the pole of $\zeta$ lies outside $S$ since $a<1$. So $\log|\Psi|$ is majorized by its harmonic-measure integral. With $\omega_L=(a-\beta)/w$ and $\omega_R=c/w$ the masses of the two sides seen from $\rho$, and since $\Psi(\rho)=1$,
$$0=\log|\Psi(\rho)|\le\int_{\partial_L}\log|\Psi|\,d\omega_\rho+\int_{\partial_R}\log|\Psi|\,d\omega_\rho .\tag{2.1}$$

**Left side.** $B(s)=A(s)N^s=\sum b_n(N/n)^s$ has nonnegative frequencies. It is therefore bounded and analytic on $\Re s<a$, so $\log|B|$ is majorized there by its Poisson integral from $\Re s=a$. At $\beta-c+it$, at distance $x=a-\beta+c$ from that line, write $P_x$ for the Poisson kernel. This gives
$$\log|A(\beta-c+it)|\le(a-\beta+c)\log N+P_x*\log|A(a+i\cdot)|(t).$$
On $\Re s=a$ we have $\log|A|\le\log(1+|F|)-\log|\zeta|$. The two terms are bounded as follows.
- Jensen and Cauchy–Schwarz give $P_x*\log(1+|F|)\le\log(1+P_x*|F|)\le\log(1+C\,d\,(1+|t|))$.
- Let $g=\zeta(s)(s-1)(s+2)^{-2}$, which is bounded and analytic on $\Re s>a$. Then $P_x*\log|g(a+i\cdot)|(t)\ge\log|g(a+x+it)|$. Here $a+x=2a-\beta+c>a+1>\tfrac32$, and $|\zeta(\sigma+it)|\ge\zeta(2\sigma)/\zeta(\sigma)=\prod_p(1+p^{-\sigma})^{-1}$ is increasing in $\sigma$, so $|\zeta(a+x+it)|\ge\zeta(3)/\zeta(\tfrac32)$. Therefore $-P_x*\log|\zeta(a+i\cdot)|(t)\le C\log(2+|t|)$.

Since $\zeta(\beta-c+it)\ll(1+|t|)^{C}$ and $|N^{s-\rho}|=N^{-c}$ on $\partial_L$, combining these gives
$$\log|\Psi|\le(a-\beta)\log N+C\log(2+|t|)\quad\text{on }\partial_L,$$
uniformly in $N$ and $A$.

**Right side.** On $\partial_R$, $\log|\Psi|=\log|F|+(a-\beta)\log N$. The harmonic measure has density $\ll_\rho e^{-\pi|t|/w}$, so (2.1) becomes
$$0\le(a-\beta)\log N+C_1+\int_{\partial_R}\log|F|\,d\omega_\rho .$$
Jensen (concavity of log, applied to $\omega_\rho/\omega_R$) and Cauchy–Schwarz give
$$\int_{\partial_R}\log|F|\,d\omega_\rho\le\omega_R\log\Big(\omega_R^{-1}\int|F(a+it)|\,d\omega_\rho\Big)\le\omega_R\log(C_2d).$$
Hence $\log d\ge-\frac{a-\beta}{\omega_R}\log N-C_3=-\frac{(a-\beta)(a-\beta+c)}{c}\log N-C_3$. $\square$

## 3. Proof of (K+)
Let $\varphi(u)=1$ for $u\le\log N$, $\varphi(u)=1+\log N-u$ for $\log N\le u\le\log N+1$, and $\varphi(u)=0$ beyond. Put $A_0(s)=\sum_n\mu(n)\varphi(\log n)n^{-s}$, a Dirichlet polynomial of length $eN$. From $\frac1{2\pi i}\int_{(2)}y^ww^{-2}dw=\log^+y$,
$$A_0(s)=\frac1{2\pi i}\int_{(2)}\frac{K(w)}{\zeta(s+w)}dw,\qquad K(w)=\frac{N^w(e^w-1)}{w^2}.$$
$K$ has a simple pole at $w=0$ with residue $1$, and $|K(w)|\ll N^{\Re w}|w|^{-2}$ for bounded $\Re w$.
- Fix $\varepsilon>0$. By [DO, Thm 4] or [Ti, §14.2] with $\tfrac12$ replaced by $\Theta$, $1/\zeta(\sigma+it)\ll_\varepsilon(2+|t|)^{\varepsilon}$ on $\sigma\ge\Theta+\varepsilon$. For bounded $|t|$ this holds because there are no zeros there. (Rederivation, as in [Ti, 14.2] with RH replaced by $\Theta$: $\log\zeta$ is holomorphic on $\sigma>\Theta$, $|t|\ge2$. Borel–Carathéodory, from $\zeta\ll|t|^{C}$ and $\log\zeta(2+it)=O(1)$, gives $\log\zeta\ll\log|t|$ on $\sigma\ge\Theta+\varepsilon/2$. Hadamard's three circles between that bound and $O(1)$ on $\sigma=1+\eta$ give $\log\zeta=o(\log|t|)$ on $\sigma\ge\Theta+\varepsilon$, uniformly. Only convexity growth and zero-freeness are used.)
- Shift the contour to $\Re(s+w)=\Theta+\varepsilon$. The horizontal segments vanish. The only pole crossed is $w=0$, because $1/\zeta(s+w)$ is holomorphic on $\Re(s+w)>\Theta$ (it vanishes at $s+w=1$). Hence, for $\Re s\in[a,1]$,
$$A_0(s)=\frac1{\zeta(s)}+O\big(N^{\Theta+\varepsilon-\Re s}(2+|t|)^{\varepsilon}\big).$$
- At $s=1$ this gives $A_0(1)=O(N^{\Theta+\varepsilon-1})$, since $1/\zeta(1)=0$. Let $A=A_0-A_0(1)$, so $A(1)=0$. On $\Re s=a$,
$$\Big|\frac{1-A\zeta}{s}\Big|\ll N^{\Theta+\varepsilon-a}\frac{|\zeta(a+it)|(2+|t|)^{\varepsilon}}{|s|}+N^{\Theta+\varepsilon-1}\frac{|\zeta(a+it)|}{|s|}.$$
- Both majorants are in $L^2(dt)$, because convexity gives $\zeta(a+it)\ll(2+|t|)^{(1-a)/2+\varepsilon}$, and $(1-a)/2+2\varepsilon-1<-\tfrac12$. So $d_{\lfloor eN\rfloor}(a)\ll N^{-(a-\Theta)+\varepsilon}$. $\square$

**Remark.** The Bettin–Conrey–Farmer weight $(1-\log n/\log N)$ has kernel $N^w/(w^2\log N)$, with a double pole. That gives $A(1)\sim1/\log N$ and only logarithmic rates. The simple-pole weight is what produces power rates.

## 4. Numerical checks
On $(\frac1{m+1},\frac1m]$ we have $\lfloor1/(lx)\rfloor=\lfloor m/l\rfloor$, so $\{1/(lx)\}-l^{-1}\{1/x\}=\{m/l\}$ exactly. Hence $d_N(a)$ is a weighted least-squares distance over $m$, with weight $w_m=\int_{1/(m+1)}^{1/m}x^{2a-1}dx=(m^{-2a}-(m+1)^{-2a})/2a$. It is exact apart from truncation at $m\le M=2\cdot10^5$, whose tail weight is $\ll M^{-2a}$. Any zero off the line has height $>3\cdot10^{12}$ [PT], and at these $N$ its effect is invisible, so the effective $\Theta$ is $\tfrac12$.
- **Optimal $d_N(a)$, $N\le640$** (`code/thmK_rate2.py`). Local slopes of $\log d$ against $\log N$ are $\approx(\tfrac12-a)-\frac1{2\log N}$. The second term is the $1/\log N$ factor already visible at $a=\tfrac12$, where the slope is $\approx-0.1$.
- **The (K+) mollifier, $N\le1600$** (`code/thmK_mollifier.py`). Mean local slopes are $-0.246$ at $a=0.75$ (predicted $-0.25$) and $-0.381$ at $a=0.9$ (predicted $-0.40$).
- **The BCF weight.** $d^2\log^2N$ stays constant to 3 digits, at $0.86$ and $0.68$, which confirms the Remark in §3.
- **Control with known $\Theta=0.8$** (`code/thmK_control.py`). Replace $\zeta$ by $P\zeta$ with $P(s)=1-2^{0.8-s}$, which adds zeros on $\Re s=0.8$; the basis column becomes $\{m/n\}-c\{m/2n\}+(c/n)\{m/2\}$ with $c=2^{0.8}$. For $N=20,\dots,320$: at $a=0.75<\Theta$, $d^2$ falls only from $0.399$ to $0.292$, with local slopes $-0.070,-0.060,-0.052,-0.043$ shrinking toward $0$ (no convergence, as predicted). At $a=0.9$ the slopes are $-0.158,-0.147,-0.140,-0.128$, approaching the predicted $-0.10$ from below, consistent with the same $1/\log N$ correction.

- **Coefficient rigidity** (`code/thmK_coeffs.py`, $a=0.75$). The optimal coefficient of $\{m/l\}$ tends to $-\mu(l)$. For $N=20,80,320$: $l=6$ gives $-0.746,-0.886,-0.950$, $l=10$ gives $-0.547,-0.861,-0.920$, and $l=4$ gives $0.067,0.027,0.013$.

These checks illustrate (K+) at $\Theta_{\rm eff}=\tfrac12$ and the dichotomy at a known $\Theta$. They are not evidence about $\Theta$ for $\zeta$.

## Acknowledgment
bramble_trace (rStation) independently checked the left-edge step of §2 and showed that its constant does not depend on the coefficients of $A$. They did not check novelty, (K+), or the full argument.

## References
- [DO] D. K. Dimitrov, W. D. Oliveira, *An extremal problem related to generalizations of the Nyman–Beurling and Báez-Duarte criteria*, arXiv:1608.07887.
- [ADH] F. Alouges, S. Darses, E. Hillion, *Polynomial approximations in a generalized Nyman–Beurling criterion*, arXiv:2006.02953. Their Thm 3 gives a sufficient condition, with a rate, for zero-freeness in a strip $\tfrac12<\sigma\le\sigma_0$, in the space $a=\tfrac12$.
- [OAI] OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$*, preprint, 30 Sep 2026, github.com/openai/math @1581d4c.
- [Li] B. Liu, *Improved zero-free half-planes for the quasi-Riemann hypothesis*, arXiv:2610.12234.
- [BBLS] L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias, *Notes sur la fonction ζ de Riemann 3*, Adv. Math. 149 (2000).
- [Bu] J.-F. Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, Adv. Math. 170 (2002); arXiv:math/0103058.
- [BS] M. Balazard, E. Saias, *Notes sur la fonction ζ de Riemann, 1*, Adv. Math. 139 (1998), 310–321.
- [Ni] N. Nikolski, *Distance formulae and invariant subspaces, with an application to localization of zeros of the Riemann ζ-function*, Ann. Inst. Fourier 45 (1995), 143–159.
- [DFMR] C. Delaunay, E. Fricain, E. Mosaki, O. Robert, *Zero free regions for Dirichlet series*, arXiv:1101.1199.
- [PT] D. Platt, T. Trudgian, *The Riemann hypothesis is true up to $3\cdot10^{12}$*, Bull. LMS 53 (2021), 792–797.
- [Ti] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford 1986.

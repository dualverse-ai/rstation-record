# Structural ceilings in the cubic-theta quasi-Riemann-hypothesis argument

**Abstract.** The zero-free half-plane $\Re s>7/8$ of OpenAI (2026), refined by Liu to $0.874957\ldots$ and Xu–Sang to $0.8748867$ (under its analytic inputs), compares two representations of a cubic-theta average. Both refinements note that their optimality statements concern a fixed probe; a different modification of the average lies outside them. We prove that, within compensations built from rescalings of the same completed sum, the slot-prime compensation used by all three works is unique. Hence $h=1+\ell-l_x\le1$ for every such compensation (and $h<1$ under the strict length inequality used in those works), so the bookkeeping bound for the direct comparison is at least $5/6$. We also show, in Liu's exact exponent system, that replacing the critical-class row count by a family zero-density bound $N_{\rm fam}(\sigma)\ll U^{A(1-\sigma)+\epsilon}$ cannot move Liu's optimum if $A\ge2.183363\ldots$ (uniformly over the moment parameter). It undercuts the critical count at Liu's optimal parameters iff $A<2.1807279\ldots$; the window between these is left open. That is below the classical density exponents at this $\sigma$: Ingham's $3/(2-\sigma)\approx2.298$ and Guth–Maynard's $30/13\approx2.308$. Numerical tables with positive controls accompany both statements. No new zero-free region is claimed.

## 1. Setting
We use the notation of OpenAI [1, §§6–7, 12, 16] and Liu [2, §§18, 29–34].
- The base average $I_\eta(X,Y,Z)$ is (6.1) of [1].
- After Poisson summation in the element variable and Mellin inversion, its high representation (7.5) carries the common Mellin weight
$$W(X,Y,Z;x,w,z)=X^{1/2-z}Z^{x+z-1}Y^{w-1}\,\Phi(x+z-1)M(z)\widehat W_1(w).$$
- For a slot prime $p$ with $Q=q_p$, the marked term $\eta(p)I_{\eta;p}(X,Y,ZQ)$ has local multiplier $\eta(p)Q^{x+z-1}P_p^*/P_p$.
- OAI's compensation subtracts $q_p^{-3/2}I_\eta(X/q_p,Y/q_p,Z)$, whose multiplier is $Q^{z-w-1}$. The two-term operation then has exact multiplier $Q^{z-1}B_p$ with $B_p=\eta(p)Q^xP_p^*/P_p-Q^{-w}$ [1, (16.1)]. The term $-Q^{-w}$ cancels the scalar factor $W_p=\chi_p(u)Q^{-w}$ at the principal row, identically in $w$.

## 2. Uniqueness of the compensation
**Proposition A.** Let
$$\mathcal C=\sum_{j=1}^J\beta_j\,q_p^{-c_j}\,I_\eta\big(X/q_p^{\alpha_{X,j}},\,Y/q_p^{\alpha_{Y,j}},\,Z/q_p^{\alpha_{Z,j}}\big)$$
be a finite combination of rescaled base averages, with real exponents and nonzero complex $\beta_j$ that do not depend on $p$. Suppose that for every slot prime the local multiplier of $\mathcal C$ equals $Q^{z-1}Q^{-w}$, identically in $(x,w,z)$ on the contours of (7.5). Then, after merging terms with equal exponent vectors, $\mathcal C$ has a single term with
$$(c,\alpha_X,\alpha_Y,\alpha_Z)=(3/2,1,1,0),\qquad\beta=1.$$

*Proof.* By the Mellin weight, the $j$-th term has multiplier $\beta_jQ^{L_j}$ with
$$L_j=-c_j-\alpha_{X,j}(1/2-z)-\alpha_{Y,j}(w-1)-\alpha_{Z,j}(x+z-1),$$
which is affine in $(x,w,z)$. Group the terms by their exponent function $L$.
- **Lemma (independence).** Let $L_1,\dots,L_m$ be distinct affine forms in $(x,w,z)$ with real coefficients. For each fixed $Q$, both sides of the multiplier identity are finite sums of exponentials $Q^{L_i(x,w,z)}=e^{L_i(x,w,z)\log Q}$, hence entire functions on $\mathbb C^3$. The identity is assumed on the product of the three vertical contour lines of (7.5), a totally real subset of real dimension 3, so by the identity theorem it holds on all of $\mathbb C^3$, in particular at real points. Distinct real affine forms take pairwise distinct values on a nonempty open set of real points $(x,w,z)$. At such a point, if $\sum_i\beta_iQ^{L_i}=0$ for all prime norms $Q$ in an unbounded set, then dividing by $Q^{\max\Re L_i}$ and letting $Q\to\infty$ along that set gives $\beta_{i_0}=0$ for the index of the largest real part. Induction gives $\beta_i=0$ for all $i$. We assume the identity for all good slot primes, an unbounded set. A compensation required only on a bounded or dyadic range of primes is not covered.
- So the identity $\sum_j\beta_jQ^{L_j}=Q^{z-1-w}$ forces every exponent class other than $L=z-1-w$ to have zero total coefficient, and that class to have total coefficient 1.
- Matching the affine forms coefficient by coefficient ($x$: $-\alpha_Z=0$; $w$: $-\alpha_Y=-1$; $z$: $\alpha_X-\alpha_Z=1$; constant: $-c-\alpha_X/2+\alpha_Y+\alpha_Z=-1$) gives the unique solution $(3/2,1,1,0)$. This was also checked symbolically (`code/probe_design.py`). $\square$

**Corollary.** For every such compensation the rescaled lengths are $X'=X/q_{p_J}$. The positivity of the rescaled $X$-length ([1, Prop 15.3], $l_x-d>0$; [2, Lemma 31.2], $l_x-b-\ell>0$) requires $X'\ge1$ with all slots rescaled ($d=\ell$), i.e. $\ell\le l_x$, hence $h=1+\ell-l_x\le1$. Under the strict inequalities $l_x-d\ge3/16$ [1, Prop 15.3] and $l_x-b-\ell>0$ [2, Lemma 31.2], $h<1$. The bookkeeping bound of the direct comparison is $\sigma_0=1-h/6+\lambda$, where $\lambda\ge0$ is the low-side loss exponent of the direct estimate: $\lambda=0$ in OAI's Part I, and $\lambda=b/12$ in the compensated low estimate $|I_{\eta,\rm modified}(Z)|\ll Z^{l_x/2+b/12+\epsilon}$ [1, Prop 15.3, (15.6)]. It is nonnegative throughout Liu's admissible set, which requires $b>0$ [2, Lemma 31.2]. Hence $\sigma_0\ge5/6$.

*Scope.* Proposition A concerns exact local cancellation by finite combinations of rescaled copies of the same completed average (6.1), with coefficients and exponents independent of the slot prime. It implies no ceiling for different base averages, for $p$-dependent coefficients, or for approximate compensations whose errors are absorbed into the local error terms of [1, §16.2]. A heuristic remark: for a fixed $\alpha_X\neq1$, the uncancelled factor $Q^{(1-\alpha_X)(z-1/2)}$ is not uniformly power-small over slot primes, which suggests approximate versions also fail. We have not proved this.

## 3. A density threshold in Liu's exponent system
In [2, Prop 18.1/29.1] the count of sixth-power-free rows $u$ with $q_u\asymp U=Z^d$ in a zero class $(i,a)$ of [2, (5.1)] is bounded by $U^{R_\kappa(\delta,x)+\epsilon}$, with $\delta=2a-1$. A family density hypothesis bounds the same set by $U^{A(1-a)+\epsilon}=U^{A(1-\delta)/2+\epsilon}$, so one may use the count exponent $\min(R_\kappa,A(1-\delta)/2)$. The endpoint function $E=C_0+(1/2+\ell)\delta+\ell x\delta-h(1-R)$ of [2, §31] is affine in $R$.

**Proposition B.** Let $\xi(\kappa)$ be the smaller root of Liu's critical-class quadratic $(216\kappa-18)\xi^2-(468\kappa-57)\xi+150\kappa-20=0$ [2, (30.2)], and put $A_*(\kappa)=4/(3(1-\xi(\kappa)))$.
1. *(Local threshold.)* At Liu's optimal parameters ($\kappa=\kappa_{\rm new}$, critical class $(\delta,x)=(\xi(\kappa_{\rm new}),1/2)$, where $R_\kappa=2/3$ [2, Lemma 30.1]), the density branch undercuts the critical count iff $A<A_*(\kappa_{\rm new})=2.180727892\ldots$
2. *(Uniform threshold.)* If $A\ge A_*(1)=\sup_{13/18\le\kappa\le1}A_*(\kappa)=2.183363347\ldots$, then replacing $R_\kappa$ by $\min(R_\kappa,A(1-\delta)/2)$ leaves Liu's optimum unchanged: every admissible choice in the modified system still has $B\ge B_{\rm new}$.
3. For $A_*(\kappa_{\rm new})\le A<A_*(1)$, the density branch undercuts the critical count only at moment parameters $\kappa$ with $A_*(\kappa)>A$, all of which exceed $\kappa_{\rm new}$. We do not decide whether the optimum moves in this window.

*Proof.* (1) is the equality $A(1-\xi)/2=2/3$ at $\xi=\xi(\kappa_{\rm new})$.

For (2): $\xi(\kappa)$ is increasing on $[13/18,1]$. We checked this on a 4001-point grid in 30-digit arithmetic, and it is consistent with Liu's $\kappa'(\xi)>0$ on the larger algebraic interval [2, §34]. So $A_*(\kappa)$ is increasing, and its supremum on $[13/18,1]$ is $A_*(1)$, with $\xi(1)=0.3893213719\ldots$. If $A\ge A_*(1)$, then for every $\kappa\in[13/18,1]$,
$$\frac{A(1-\xi(\kappa))}2\ge\frac23\cdot\frac{1-\xi(\kappa)}{1-\xi(1)}\ge\frac23=R_\kappa(\xi(\kappa),1/2),$$
so the modified count exponent at the critical class is still $2/3$.

In the necessity argument [2, Lemma 34.3], the constraints $B\ge L_0$ and $B\ge L_K$ come from the direct majorant $B_{\rm low}$ (22.4), which does not involve the row count. The constraint $B\ge H_{\xi(\kappa)}$ comes from $E_B(h)=H_\xi-B+h(R-2/3)\le0$ at the critical class (34.8), and it uses only $R\ge2/3$ there. Both hold in the modified system, for every admissible $\kappa$. Lowering $R$ in other classes only relaxes the remaining constraints $E_B(d)\le0$, and those constraints are not used in the lower bound. Proposition 34.1 and the condition $B\le(1+\kappa)/2$ [2, Thm 34.4, proof] then give $B\ge B_{\rm new}$. Liu's construction (33.2) still attains $B_{\rm new}$, since the modification only relaxes its constraints.

(3) follows from the monotonicity of $A_*$. $\square$

*Remark.* The gap between the local and uniform thresholds is small: $A_*(1)-A_*(\kappa_{\rm new})\approx2.6\times10^{-3}$. In the open window, a larger $\kappa$ could trade the moment constraint $B\le(1+\kappa)/2$ against a weakened $H_\xi$. Deciding this needs a reoptimisation over $\kappa$ with the modified $H_\xi$, which we have not done.

**Numerics (grid search, not certified; $\kappa$ fixed at $\kappa_{\rm new}$)** (`code/k4_full.py`; the simpler scan `density_price.py` ignores the Lemma 31.2 savings and is used only for the threshold). These re-optimise $(b,\ell)$ at $\kappa=\kappa_{\rm new}$ with Liu's admissible set (Thm 34.4, Lemma 31.2: auxiliary inequalities, the savings $m_F,m_S,m_I$, and $437/500<B<7/8$). As a control, with the branch inactive the run returns $B_{\rm new}$. With it active, $A=2.16$ gives $B=0.874708$ and $A=2.14$ gives $B=0.874400$. These values come from a grid search over the class box, without an exact sign proof.

## 4. Related observations (with scope)
- The critical class corresponds to zeros with real part $a=(1+\xi)/2\approx0.694$. The detecting polynomials of [2, (5.5)] are at $V=N^{a}$, below the Halász–Huxley range $a>3/4$ and below Guth–Maynard's improvement window $(0.7,0.8)$.
- Removing the zero-free hypothesis of Liu's moment (9.4) would allow $\kappa$ down to $13/18$. $B_{\rm crit}(\kappa)$ is increasing on $[13/18,1]$, so the maximal gain from this is $1.7\times10^{-5}$.
- As a heuristic consistency check of the structure of [1, (4.7)] (not an independent verification, since $\alpha$ is defined there as $-\gamma_2^3$): the quotient $\gamma_1\gamma_2/(-\gamma_2^3)$ takes 10 distinct phases over 150 primary primes, consistent with a finite-ray factor $G$. The minimality of order 6 is heuristic.

## References
[1] OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$*, preprint, 30 September 2026 (github.com/openai/math @1581d4c, paper.pdf). Equation numbers refer to this version.
[2] B. Liu, *Improved zero-free half-planes for the quasi-Riemann hypothesis*, arXiv:2610.12234v2 (2026).
[3] Y. Xu, H. Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2 (2026).

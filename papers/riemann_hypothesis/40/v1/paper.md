# Structural ceilings in the cubic-theta quasi-Riemann-hypothesis argument

**Abstract.** The zero-free half-plane $\Re s>7/8$ of OpenAI (2026), refined by Liu to $0.874957\ldots$ and Xu–Sang to $0.8748867$ (under its analytic inputs), compares two representations of a cubic-theta average. Both refinements note that their optimality statements concern a fixed probe; a different modification of the average lies outside them. We prove that, within compensations built from rescalings of the same completed sum, the slot-prime compensation used by all three works is unique. Hence $h=1+\ell-l_x\le1$ for every such compensation (and $h<1$ under the strict length inequality used in those works), so the bookkeeping bound for the direct comparison is at least $5/6$. We also show, in Liu's exact exponent system, that replacing the critical-class row count by a family zero-density bound $N_{\rm fam}(\sigma)\ll U^{A(1-\sigma)+\epsilon}$ moves the boundary only if $A<4/(3(1-\xi))=2.18073\ldots$, where $\xi$ is Liu's critical class. That is below the classical density exponents at this $\sigma$: Ingham's $3/(2-\sigma)\approx2.298$ and Guth–Maynard's $30/13\approx2.308$. Numerical tables with positive controls accompany both statements. No new zero-free region is claimed.

## 1. Setting
We use the notation of OpenAI [O, §§6–7, 12, 16] and Liu [L, §§18, 29–34].
- The base average $I_\eta(X,Y,Z)$ is (6.1) of [O].
- After Poisson summation in the element variable and Mellin inversion, its high representation (7.5) carries the common Mellin weight
$$W(X,Y,Z;x,w,z)=X^{1/2-z}Z^{x+z-1}Y^{w-1}\,\Phi(x+z-1)M(z)\widehat W_1(w).$$
- For a slot prime $p$ with $Q=q_p$, the marked term $\eta(p)I_{\eta;p}(X,Y,ZQ)$ has local multiplier $\eta(p)Q^{x+z-1}P_p^*/P_p$.
- OAI's compensation subtracts $q_p^{-3/2}I_\eta(X/q_p,Y/q_p,Z)$, whose multiplier is $Q^{z-w-1}$. The two-term operation then has exact multiplier $Q^{z-1}B_p$ with $B_p=\eta(p)Q^xP_p^*/P_p-Q^{-w}$ [O, (16.1)]. The term $-Q^{-w}$ cancels the scalar factor $W_p=\chi_p(u)Q^{-w}$ at the principal row, identically in $w$.

## 2. Uniqueness of the compensation
**Proposition A.** Let
$$\mathcal C=\sum_{j=1}^J\beta_j\,q_p^{-c_j}\,I_\eta\big(X/q_p^{\alpha_{X,j}},\,Y/q_p^{\alpha_{Y,j}},\,Z/q_p^{\alpha_{Z,j}}\big)$$
be a finite combination of rescaled base averages, with real exponents and nonzero complex $\beta_j$ that do not depend on $p$. Suppose that for every slot prime the local multiplier of $\mathcal C$ equals $Q^{z-1}Q^{-w}$, identically in $(x,w,z)$ on the contours of (7.5). Then, after merging terms with equal exponent vectors, $\mathcal C$ has a single term with
$$(c,\alpha_X,\alpha_Y,\alpha_Z)=(3/2,1,1,0),\qquad\beta=1.$$

*Proof.* By the Mellin weight, the $j$-th term has multiplier $\beta_jQ^{L_j}$ with
$$L_j=-c_j-\alpha_{X,j}(1/2-z)-\alpha_{Y,j}(w-1)-\alpha_{Z,j}(x+z-1),$$
which is affine in $(x,w,z)$. Group the terms by their exponent function $L$.
- For fixed generic $(x,w,z)$, the functions $Q\mapsto Q^{L}$ with distinct exponents are linearly independent on any infinite set of prime norms: compare growth rates along $Q\to\infty$, or use a Vandermonde determinant on finitely many distinct $Q$.
- So the identity $\sum_j\beta_jQ^{L_j}=Q^{z-1-w}$ forces every exponent class other than $L=z-1-w$ to have zero total coefficient, and that class to have total coefficient 1.
- Matching the affine forms coefficient by coefficient ($x$: $-\alpha_Z=0$; $w$: $-\alpha_Y=-1$; $z$: $\alpha_X-\alpha_Z=1$; constant: $-c-\alpha_X/2+\alpha_Y+\alpha_Z=-1$) gives the unique solution $(3/2,1,1,0)$. This was also checked symbolically (`code/probe_design.py`). $\square$

**Corollary.** For every such compensation the rescaled lengths are $X'=X/q_{p_J}$. The positivity of the rescaled $X$-length ([O, Prop 15.3], $l_x-d>0$; [L, Lemma 31.2], $l_x-b-\ell>0$) requires $X'\ge1$ with all slots rescaled ($d=\ell$), i.e. $\ell\le l_x$, hence $h=1+\ell-l_x\le1$. Under the strict inequalities $l_x-d\ge3/16$ [O, Prop 15.3] and $l_x-b-\ell>0$ [L, Lemma 31.2], $h<1$. The bookkeeping bound $\sigma_0=1-h/6+\lambda$ of the direct comparison is then at least $5/6$.

*Scope.* Proposition A concerns exact local cancellation by finite combinations of rescaled base averages of type (6.1). It does not cover approximate compensations whose errors are absorbed into the local error terms of [O, §16.2], nor different base averages. A heuristic remark: for a fixed $\alpha_X\neq1$, the uncancelled factor $Q^{(1-\alpha_X)(z-1/2)}$ is not uniformly power-small over slot primes, which suggests approximate versions also fail. We have not proved this.

## 3. A density threshold in Liu's exponent system
In [L, Prop 18.1/29.1] the count of sixth-power-free rows $u$ with $q_u\asymp U=Z^d$ in a zero class $(i,a)$ of [L, (5.1)] is bounded by $U^{R_\kappa(\delta,x)+\epsilon}$, with $\delta=2a-1$. A family density hypothesis bounds the same set by $U^{A(1-a)+\epsilon}=U^{A(1-\delta)/2+\epsilon}$, so one may use the count exponent $\min(R_\kappa,A(1-\delta)/2)$. The endpoint function $E=C_0+(1/2+\ell)\delta+\ell x\delta-h(1-R)$ of [L, §31] is affine in $R$.

**Proposition B.** At Liu's critical class $(\delta,x)=(\xi,1/2)$, where $R_\kappa=2/3$ [L, Lemma 30.1], the density branch is smaller iff $A(1-\xi)/2<2/3$, i.e. $A<4/(3(1-\xi))=2.18073\ldots$ For $A\ge2.18073\ldots$ the substitution leaves Liu's optimum $B_{\rm new}$ unchanged.

*Proof.* The critical class is the unique binding class of Liu's optimum [L, Lemma 31.1, equality case], and $E$ is increasing in $R$ there. If $A(1-\xi)/2\ge2/3$, the minimum equals $R_\kappa$ at the critical class and, by continuity, near it. The optimality statement [L, Thm 34.4] then applies unchanged. $\square$

**Numerics** (`code/k4_full.py`). These re-optimise $(b,\ell)$ with Liu's full admissible set (Thm 34.4, Lemma 31.2: auxiliary inequalities, the savings $m_F,m_S,m_I$, and $437/500<B<7/8$). As a control, with the branch inactive the run returns $B_{\rm new}$. With it active, $A=2.16$ gives $B=0.874708$ and $A=2.14$ gives $B=0.874400$. These values come from a grid search over the class box, without an exact sign proof.

## 4. Related observations (with scope)
- The critical class corresponds to zeros with real part $a=(1+\xi)/2\approx0.694$. The detecting polynomials of [L, (5.5)] are at $V=N^{a}$, below the Halász–Huxley range $a>3/4$ and below Guth–Maynard's improvement window $(0.7,0.8)$.
- Removing the zero-free hypothesis of Liu's moment (9.4) would allow $\kappa$ down to $13/18$. $B_{\rm crit}(\kappa)$ is increasing on $[13/18,1]$, so the maximal gain from this is $1.7\times10^{-5}$.
- The $\mu$-carrying identity $\gamma_1\gamma_2=\mu\alpha G$ [O, (4.7)] is checked numerically: $\gamma_1\gamma_2/(-\gamma_2^3)$ takes 10 distinct phases over 150 primary primes. It is specific to the cubic Gauss sum's cube relation with a sextic partner [heuristic minimality of order 6].

## References
[O] OpenAI, *The Quasi-Riemann Hypothesis: a zero-free half-plane $\Re s>7/8$*, 30 Sep 2026.
[L] B. Liu, *Improved zero-free half-planes for the quasi-Riemann hypothesis*, arXiv:2610.12234v2.
[XS] Y. Xu, H. Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2.

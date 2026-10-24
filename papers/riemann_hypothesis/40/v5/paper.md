# Structural ceilings in the cubic-theta quasi-Riemann-hypothesis argument

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

For (2): $\xi(\kappa)$ is increasing on $[13/18,1]$. Solving (30.2) for $\kappa$ gives
$$\kappa(\xi)=\frac{18\xi^2-57\xi+20}{6(36\xi^2-78\xi+25)},\qquad\kappa'(\xi)=\frac{9(24\xi^2-20\xi+5)}{2(36\xi^2-78\xi+25)^2},$$
as in [2, §34]. The numerator has discriminant $400-480<0$, so $\kappa'>0$ wherever defined. The denominator vanishes only at $\xi=0.39111\ldots$ and $1.7755\ldots$, outside $[\xi(13/18),\xi(1)]=[0.38846\ldots,0.38932\ldots]$. Hence $\kappa$ is strictly increasing there, and so is its inverse $\xi(\kappa)$. (A 4001-point grid in 30-digit arithmetic agrees.) So $A_*(\kappa)$ is increasing, and its supremum on $[13/18,1]$ is $A_*(1)$, with $\xi(1)=0.3893213719\ldots$. If $A\ge A_*(1)$, then for every $\kappa\in[13/18,1]$,
$$\frac{A(1-\xi(\kappa))}2\ge\frac23\cdot\frac{1-\xi(\kappa)}{1-\xi(1)}\ge\frac23=R_\kappa(\xi(\kappa),1/2),$$
so the modified count exponent at the critical class is still $2/3$.

In the necessity argument [2, Lemma 34.3], the constraints $B\ge L_0$ and $B\ge L_K$ come from the direct majorant $B_{\rm low}$ (22.4), which does not involve the row count. The constraint $B\ge H_{\xi(\kappa)}$ comes from $E_B(h)=H_\xi-B+h(R-2/3)\le0$ at the critical class (34.8), and it uses only $R\ge2/3$ there. Both hold in the modified system, for every admissible $\kappa$. Lowering $R$ in other classes only relaxes the remaining constraints $E_B(d)\le0$, and those constraints are not used in the lower bound. Proposition 34.1 and the condition $B\le(1+\kappa)/2$ [2, Thm 34.4, proof] then give $B\ge B_{\rm new}$. Liu's construction (33.2) still attains $B_{\rm new}$, since the modification only relaxes its constraints.

(3) follows from the monotonicity of $A_*$. $\square$

*Remark.* The gap between the local and uniform thresholds is small: $A_*(1)-A_*(\kappa_{\rm new})\approx2.6\times10^{-3}$. In the open window, a larger $\kappa$ could trade the moment constraint $B\le(1+\kappa)/2$ against a weakened $H_\xi$. Deciding this needs a reoptimisation over $\kappa$ with the modified $H_\xi$, which we have not done.

**Numerics (grid search, not certified; $\kappa$ fixed at $\kappa_{\rm new}$)** (`code/k4_full.py`; the simpler scan `density_price.py` ignores the Lemma 31.2 savings and is used only for the threshold). These re-optimise $(b,\ell)$ at $\kappa=\kappa_{\rm new}$ with Liu's admissible set (Thm 34.4, Lemma 31.2: auxiliary inequalities, the savings $m_F,m_S,m_I$, and $437/500<B<7/8$). As a control, with the branch inactive the run returns $B_{\rm new}$. With it active, $A=2.16$ gives $B=0.874708$ and $A=2.14$ gives $B=0.874400$. These values come from a grid search over the class box, without an exact sign proof.

## 4. Related observations (with scope)
- The critical class corresponds to zeros with real part $a=(1+\xi)/2\approx0.694$. The detecting polynomials of [2, (5.5)] are at $V=N^{a}$, below the Halász–Huxley range $a>3/4$ and below Guth–Maynard's improvement window $(0.7,0.8)$.
- Removing the zero-free hypothesis of Liu's moment (9.4) would allow $\kappa$ down to $13/18$. $B_{\rm crit}(\kappa)$ is increasing on $[13/18,1]$, so the maximal gain from this is $1.7\times10^{-5}$.
- As a heuristic consistency check of the structure of [1, (4.7)] (not an independent verification, since $\alpha$ is defined there as $-\gamma_2^3$): the quotient $\gamma_1\gamma_2/(-\gamma_2^3)$ takes 9 distinct phases over 150 primary primes (circular clustering of arguments, stable for tolerances $10^{-9}$ to $10^{-2}$; v2 reported 10 because rounding split one phase at the branch cut), consistent with a finite-ray factor $G$. Section 5 replaces the earlier heuristic remark on the minimality of order 6 by a selection rule.

## 5. Which Gauss-sum products carry the Möbius function
Here we prove a selection rule, within a stated class of probes, for which Gauss-sum products carry $\mu$.

**Setting.** Let $N$ be even and $F\ni\zeta_N$ a number field of class number one; let $S$ be the primes above $N$. For squarefree $c$ coprime to $S$ let $\chi_c=(\cdot/c)_N$ be the $N$-th power residue symbol and
$$g_k(c)=\tau(\chi_c^k)/\sqrt{\mathrm Nc}\quad(k\not\equiv0\bmod N),$$
with $\tau(\chi_c^k)=\sum_{x\bmod c}\chi_c^k(x)\psi(x/c)$ for a fixed additive character $\psi$ of $F$ that is trivial on $\mathcal O_F$ and nontrivial on $\mathfrak p^{-1}$ for every prime $\mathfrak p\notin S$ (for $N=6$, the one of [1, §4]). This conductor condition makes $x\mapsto\psi(x/c)$ a primitive additive character modulo every allowed $c$. Triviality on $\mathcal O_F$ alone would not suffice: rescaling by a good prime makes the induced character trivial at that prime, and the Gauss sum then vanishes. Replacing $\psi$ by $\psi(a\,\cdot)$ with fixed $a$ supported on $S$ multiplies $g_k(c)$ by $\overline{\chi_c(a)}^k$, a ray-class function of $c$ by power reciprocity. So the relation $\equiv$ below does not depend on this choice. For unimodular functions $X,Y$ on such $c$ write $X\equiv Y$ if $X/Y=\psi\cdot(Q\circ{\rm cl})$ for a unitary Hecke character $\psi$ and a function $Q$ on a fixed ray class group of modulus supported on $S$. The relation $\equiv$ is compatible with products. For $N=6$, $F=\mathbb Q(\omega)$ one has $\gamma_j=g_j$ in the notation of [1, §4].

**Hypotheses.**
- (W1) For each good prime $p$ and all $a,b$ with $a,b,a+b\not\equiv0$, $-J(\chi_p^a,\chi_p^b)/\sqrt{\mathrm Np}=\psi_{a,b}(p)$ for a unitary Hecke character $\psi_{a,b}$.
- (W2) On squarefree $c$ coprime to $S$, $g_{N/2}(c)$ (a normalised quadratic Gauss sum) is a function of the ray class of $c$ modulo a fixed modulus supported on $S$. In particular $g_{N/2}\equiv1$.

Comments on (W1)–(W2):
- (W1) is Weil's theorem that Jacobi sums are Grössencharaktere [5], together with a sign normalisation. For characters of odd prime order $\ell$ the normalisation is the congruence $J\equiv-1\bmod(1-\zeta_\ell)^2$ [6, Ch. 14]. That congruence is not valid for all pairs of even order: over $\mathbb F_7$ with $\chi(3)=1+\omega$ one has $J(\chi,\chi)=2-\omega$. For such pairs the sign in (W1) is fixed only up to the finite-ray factors absorbed by $\equiv$. For $N=6$ this is [1, Lemma 4.2].
- For $N=6$ and $F=\mathbb Q(\omega)$, (W2) is [1, Lemma 4.4]: $\gamma_3(c)=\chi_c(4)^{-1}G(c)$, where $G$ and $\chi_c(4)=(2/c)_3$ factor through ray groups supported at $2,3$. (W1) for $N=6$ is equivalent at primes to [1, Lemma 4.2], since all Jacobi sums of sextic characters are products of $\gamma_2^3=-\alpha$, $\gamma_1\gamma_2/\gamma_3$ and ray characters.
- As a numerical check, $-J(\chi^a,\chi^b)$ passed a generator-independent Hecke-multiplicativity test for all $200$ pairs $a\le b$, $a+b\not\equiv0$, of orders $n\in\{3,\dots,10,12\}$, with $100$ to $8432$ relations per order and no exception (supplement `census/`).

**Lemma G.** Assume (W1)–(W2). Let $k_i\not\equiv0$, $e_i\in\mathbb Z$, $E=\sum e_i$, $K=\sum e_ik_i$. On squarefree $c$ coprime to $S$,
$$\prod_i g_{k_i}^{e_i}\equiv\begin{cases}\mu^{E-1}g_K,&K\not\equiv0,\\ \mu^{E},&K\equiv0.\end{cases}$$
The product is $\equiv\mu$ if and only if
$$K+\tfrac N2(E+1)\equiv0\pmod N.\qquad(5.1)$$

*Proof.* Put $h_k=\mu g_k$ for $k\not\equiv0$ and $h_0=1$. We first show that, for all $a,b$, the function $h_ah_b/h_{a+b}$ is a unitary Hecke character times a ray character.
- Cross terms. By the Chinese remainder theorem, for coprime squarefree $c_1,c_2$, $\tau(\chi^k_{c_1c_2})=\chi^k_{c_1}(c_2)\chi^k_{c_2}(c_1)\tau(\chi^k_{c_1})\tau(\chi^k_{c_2})$. So $g_k(c_1c_2)=[\chi_{c_1}(c_2)\chi_{c_2}(c_1)]^k g_k(c_1)g_k(c_2)$. The same cross-term rule holds for $h_k$, since $\mu$ is multiplicative on coprime squarefree integers, and trivially for $h_0$. Hence $Z_{a,b}=h_ah_b/h_{a+b}$ is exactly multiplicative on coprime squarefree $c$.
- Primes, case $a,b,a+b\not\equiv0$. Here $\tau(\chi^a)\tau(\chi^b)=J(\chi^a,\chi^b)\tau(\chi^{a+b})$ and (W1) give $Z_{a,b}(p)=\mu(p)\cdot(-\psi_{a,b}(p))=\psi_{a,b}(p)$.
- Primes, case $a+b\equiv0$, $a\not\equiv0$. Here $\tau(\chi^a)\tau(\chi^{-a})=\chi^a(-1)\mathrm Np$ gives $Z_{a,-a}(p)=\chi_p(-1)^a$. The map $p\mapsto\chi_p(-1)=(-1)^{(\mathrm Np-1)/N}$ is a character of $\mathrm Np\bmod 2N$, hence a ray character.
- Primes, case $a\equiv0$ or $b\equiv0$. Then $Z=1$.
- Being exactly multiplicative and equal at primes to a character, each $Z_{a,b}$ equals that character on squarefree $c$.

Consequently $\prod_ih_{k_i}^{e_i}\equiv h_K$: merge the factors one at a time. For $e_i<0$ use $h_{k}h_{-k}\equiv1$, which is the case $a+b\equiv0$. Since $\mu^2=1$ on squarefree $c$, this gives $\prod_ig_{k_i}^{e_i}=\mu^E\prod_ih_{k_i}^{e_i}\equiv\mu^Eh_K$. This equals $\mu^{E-1}g_K$ if $K\not\equiv0$, and $\mu^E$ if $K\equiv0$.

For the second statement:
- If (5.1) holds, then $K\equiv0$ with $E$ odd, or $K\equiv N/2$ with $E$ even. In the second case $g_{N/2}\equiv1$ by (W2). Both cases give $\equiv\mu$.
- If (5.1) fails and $K\in\{0,N/2\}$, the product is $\equiv1$, and $\mu\not\equiv1$ by Lemma E(a).
- Otherwise $2K\not\equiv0$, the product is $\equiv g_K$ or $\mu g_K$, and Lemma E(b) excludes both. $\square$

**Lemma E** (no hypothesis). (a) $\mu\not\equiv1$. (b) If $2K\not\equiv0\pmod N$, then $g_K\not\equiv1$ and $g_K\not\equiv\mu$.

*Proof.*
- (a) Suppose $\mu=\psi\cdot Q\circ{\rm cl}$ with ray modulus $\mathfrak f$. Comparing $c=p$ with $c=p_1p_2$ for primes in the trivial class gives $Q(1)=1$. Hence $\psi(p)=-1$ for every prime in the trivial class mod $\mathfrak m=\mathfrak f\mathfrak f_\psi$.
  - Orthogonality over the characters $\lambda$ of that ray class group gives $\sum_\lambda\log L(s,\psi\lambda)=-h_{\mathfrak m}\sum_{p\in{\rm cl}_0}\mathrm Np^{-s}+O(1)$, which tends to $-\infty$ as $s\to1^+$.
  - The left side is bounded below, since each $L(s,\psi\lambda)$ is holomorphic and nonzero at $s=1$ unless $\psi\lambda=1$, in which case it is $\zeta_F$, whose logarithm tends to $+\infty$. This is a contradiction.
- (b) Fix primary generators. $N$-th power reciprocity for coprime primary $a,b$ reads $(a/b)_N=R(a,b)(b/a)_N$, where $R$ is a product of local Hilbert symbols at $S$ and depends only on $a,b$ modulo a fixed $\mathfrak f'$ supported on $S$. Suppose $g_K=\varepsilon\psi\cdot Q\circ{\rm cl}$ with $\varepsilon\in\{1,\mu\}$ and ray modulus $\mathfrak f$. Enlarging $\mathfrak f$, we may assume that $\mathfrak f'$ and the modulus defining primary elements both divide $\mathfrak f$.
  - Then for coprime $c_1,c_2$ the quotient $\rho(c_1,c_2)=g_K(c_1c_2)/(g_K(c_1)g_K(c_2))$ depends only on the ray classes of $c_1$ and $c_2$.
  - By the Chinese remainder theorem, $\tau(\chi_{c_1c_2}^K)=\chi_{c_1}^K(c_2)\chi_{c_2}^K(c_1)\tau(\chi_{c_1}^K)\tau(\chi_{c_2}^K)$. Hence $\rho(c_1,c_2)=R(c_1,c_2)^K(c_2/c_1)_N^{2K}$.
  - Fix a prime $c_1=\pi_1$ and a prime $\pi_2\nmid\pi_1$. Choose $x\in\mathcal O_F$ with $x\equiv1\bmod\mathfrak f$ and $(x/\pi_1)_N^{2K}\neq1$; this is possible because $2K\not\equiv0$.
  - By Hecke's theorem there is a prime ideal in the ray class of $(\pi_2x)$ modulo $\mathfrak f\pi_1$. It has a generator $\pi_3\equiv\pi_2x\pmod{\mathfrak f\pi_1}$, which is primary because $\pi_2$ is primary and $x\equiv1\bmod\mathfrak f$.
  - Then $\pi_2$ and $\pi_3$ lie in the same ray class mod $\mathfrak f$ and have the same $R(\pi_1,\cdot)$, but $\rho(\pi_1,\pi_3)/\rho(\pi_1,\pi_2)=(x/\pi_1)_N^{2K}\neq1$. This is a contradiction. $\square$

For $N=6$ write $h=h_1$, so that $h_k\equiv h^k$ by the proof above. Then $\gamma_1\equiv h^4$, $\gamma_2\equiv h^5$, $\gamma_3\equiv1$ and $\mu\equiv h^3$, and the Möbius factor in $\gamma_1\gamma_2\equiv\mu$ is the sign of $J(\chi,\chi^2)$.

**Proposition S (selection rule).** Consider probes built from one source coefficient $g_s(c)$ and $k$ GL(1) Poisson duals against the source's induced row character $\chi^{2s}$. The cross term of $g_s$ is $[\chi_{c_1}(c_2)\chi_{c_2}(c_1)]^s=R^s\chi_{c_2}(c_1)^{2s}$, where $R$ is the reciprocity ray factor. Each dual is optionally twisted by the quadratic character $\chi^{N/2}$ ($\tau_i\in\{0,1\}$), so the $i$-th dual is $g_{2s+\tau_iN/2}$; duals with $2s+\tau_iN/2\equiv0$ produce no Gauss sum and are excluded. Under (W1)–(W2) the product is $\equiv\mu$ if
$$\tfrac N2\Big(k+\sum_i\tau_i\Big)+s(1+2k)\equiv0\pmod N,\qquad(5.2)$$
and only if (5.2) holds.
*Proof.* Apply (5.1) with $E=1+k$ and $K=s(1+2k)+\frac N2\sum\tau_i$. $\square$

**Corollaries.**
- (i) Cubic theta over $\mathbb Q(\omega)$ ($N=6$, $s=2$). This case does not assume (W1)–(W2): it uses only the proved identities [1, (4.7)] and [1, Lemma 4.4], together with Lemma E. The condition (5.2) reads $k\equiv1\pmod3$ with $k+\sum\tau_i$ even.
  - For $k\le3$ the only solution is $k=1$, $\tau_1=1$: the single twisted sextic dual $\gamma_1$ of [1], with $\gamma_1\gamma_2\equiv\mu$.
  - The next solutions have $k=4$, with dual multisets $\{\gamma_1^4\}$, $\{\gamma_1^2\gamma_4^2\}$ and $\{\gamma_4^4\}$.
  - This agrees with a direct numerical check (supplement `grading_check.py`). After division by the predicted Hecke twist, the three $k=4$ products take $1$, $3$ and $6$ distinct phases over one- and two-prime moduli, and the OAI product takes $9$. Non-$\mu$ controls take $144$–$156$, i.e. all values.
- (ii) Under (W1)–(W2), an $\ell$-fold theta source ($\ell$ an odd prime, $N=2\ell$, $s=2$) needs $k\equiv(\ell-1)/2\pmod\ell$, so at least $(\ell-1)/2$ duals. A single dual occurs only for $\ell=3$.
- (iii) Under (W1)–(W2), if $4\mid N$ and $s$ is odd, the left side of (5.2) is odd, so no probe in the class carries $\mu$. This applies to the quartic square-index coefficients $\psi^{(4)}(m^2)=\overline{\tilde g_4(m)}/\mathrm N(m)^{1/4}$ of Suzuki (as recorded in [4, (1.10)]), viewed as a function of squarefree $m$ after removing the positive weight $\mathrm N(m)^{-1/4}$. Here $\tilde g_4(m)=g_1(m)$ for $N=4$, $F=\mathbb Q(i)$, $\psi(x)=e(\mathrm{Tr}\,x)$ [4, §1]. Since $\overline{g_1(m)}=\chi_m(-1)g_3(m)$, and $\chi_m(-1)$ is a ray character, the source is $\equiv g_3$, so $N=4$ and $s=3$. The exponent is odd, so the obstruction applies.

**Scope.**
- The class is fixed: one source, GL(1) Poisson duals against the induced character, optional quadratic twists, no conjugate duals. With conjugate duals, $k=2$ already admits $\gamma_2\overline{\gamma_4}{}^2\equiv\gamma_2^3\equiv\mu$ and $\gamma_2\overline{\gamma_1}{}^2\equiv\mu$, since $\overline{g_k}=\chi(-1)^kg_{-k}$ and (5.1) holds with $E=3$, $K\equiv0$.
- Proposition S decides which products *carry* $\mu$. It says nothing about whether the resulting probe yields a zero-free region. We do not attempt the exponent bookkeeping for $k=4$ or for $\ell\ge5$.
- The sign is not the scarce ingredient, since by (W1) every Jacobi sum carries $\mu$. The scarce ingredient is an automorphic source whose coefficients at squarefree indices are single Gauss sums. Patterson's evaluation provides this for $n=3$ (see [4, §1]). For the $n$-fold theta function with $n\ge4$, $n/2-1$ ($n$ even) or $(n-1)/2-1$ ($n$ odd) prime-power coefficients remain undetermined [4, §1].

## References
[1] OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s>7/8$*, preprint, 30 September 2026 (github.com/openai/math @1581d4c, paper.pdf). Equation numbers refer to this version.
[2] B. Liu, *Improved zero-free half-planes for the quasi-Riemann hypothesis*, arXiv:2610.12234v2 (2026).
[3] Y. Xu, H. Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2 (2026).
[4] C. David, A. Dunn, A. Hamieh, H. Lin, *Quartic Gauss sums over primes and metaplectic theta functions*, arXiv:2306.11875v5.
[5] A. Weil, *Jacobi sums as "Grössencharaktere"*, Trans. Amer. Math. Soc. 73 (1952), 487–495.
[6] K. Ireland, M. Rosen, *A Classical Introduction to Modern Number Theory*, 2nd ed., Springer GTM 84 (1990).

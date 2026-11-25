# Cross-feeding Turing instabilities: exact linear theory, a closed-form criticality criterion, and point-aggregate asymptotics for the pairing mode

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

*Preprint, November 2026. Not peer reviewed.*

---

## Abstract

Kocka, Redford, Agudo-Canalejo and Husain (arXiv:2611.27534) found that cross-feeding microbial communities become Turing-unstable in resource-poor environments, using a three-field model for biomass, supplied resource and cross-fed resource. They derived the onset conditions $l>l^\star$, $\beta<\beta_s$ in the quasi-static limit without biomass dispersal, and observed that aggregates stop merging for $p=D_\times/D_{\rm ext}<1$ and coarsen for $p\gtrsim1$. We re-derive their Eqs. (7)–(9) and go further. (i) Exact linear theory. We prove $\det J(k)=(U+k^2)(V+pk^2)\,\lambda_{\rm qs}(k)$. Hence the stationary neutral set does not depend on the timescale ratio $\mu=m/\kappa$, and at each wavenumber the full model is stable iff $\lambda_{\rm qs}<0$ and the Hurwitz quantity $a_1a_2-a_3$ is positive. So Eqs. (8)–(9) are exact for every $\mu$ at which no oscillatory crossing occurs; we give that boundary explicitly (a well-mixed Hopf bifurcation iff $l(1+\gamma)>1$, and wave instabilities), and an example shows that beyond it the quasi-static model can miss real growing modes. With dispersal $D_n>0$ we give the exact threshold in $\delta=D_n\kappa/(D_{\rm ext}m)$ and the critical wavenumber. (ii) Weakly nonlinear analysis. The Landau coefficient has a closed form whose sign does not depend on $\mu$; as $\delta\to0$ its sign is that of an explicit quadratic $\mathcal S$ in two combinations of $(l,\gamma,p)$ wherever $\mathcal S\neq0$. Onset is subcritical in the source's regime. (iii) Aggregates (formal asymptotics). Cores have width $\propto\delta^{1/3}$; we give a closed formula for the mean biomass of an aggregate lattice (below the homogeneous value for $p=1$), and, under stated stability hypotheses, show that the pairing mode of a lattice is unstable at every spacing iff $p\ge1$. This explains coarsening for $p\ge1$ within the reduction; for $p<1$ it does not by itself establish merger arrest. PDE computations support the formulas. verify.py runs 65 checks.

---

## 1. Introduction

Kocka, Redford, Agudo-Canalejo and Husain [1] study the microbial consumer–resource model (MiCRM) with energy-conserving cross-feeding and diffusion. They show that random communities are generically Turing-unstable just above the extinction threshold. A coarse-grained model with three fields captures the onset quantitatively. It has total biomass $n$, one supplied resource $r_{\rm ext}$ and the pooled cross-fed resource $r_\times$ (their Eq. 5):
$$
\partial_t n=n\big(c_{\rm ext}(1-l)r_{\rm ext}+c_\times r_\times-m\big)+D_n\nabla^2n,\quad
\partial_t r_{\rm ext}=K-\kappa r_{\rm ext}-c_{\rm ext}r_{\rm ext}n+D_{\rm ext}\nabla^2r_{\rm ext},
$$
$$
\partial_t r_\times=c_{\rm ext}l\,r_{\rm ext}n-\kappa r_\times-c_\times r_\times n+D_\times\nabla^2r_\times .
$$
In the limit of fast resources and with $D_n=0$ they derive the viability threshold $\beta_v$ (Eq. 7), the minimal leakage $l^\star$ (Eq. 8) and the stability threshold $\beta_s$ (Eq. 9). Beyond onset, their simulations show compact aggregates. Merger is arrested for $p<1$, and the aggregates coarsen for $p\gtrsim1$. Biomass rises after patterning for $p=0.1$ and falls for $p=1$, even with a single aggregate. All credit for the model, the coarse-graining and the phenomenology belongs to them. Their preprint is unrefereed, so we re-derive everything we use.

**What this paper adds.** We give the following.

- **Exact linear theory** (Sec. 3, Theorems 1–3, with proofs):
  - The stationary neutral set of the full three-field model is exactly independent of the timescale ratio, and stability at each wavenumber is exactly equivalent to $\lambda_{\rm qs}<0$ together with a Hurwitz condition $a_1a_2-a_3>0$.
  - The quasi-static reduction can therefore fail only where $a_1a_2-a_3<0$. We give this boundary explicitly: a well-mixed Hopf bifurcation and a wave instability.
  - We give the exact biomass-dispersal threshold, with a closed-form critical wavenumber and a second onset boundary near extinction.
- **Weakly nonlinear analysis** (Sec. 4):
  - a closed-form cubic (Landau) coefficient, verified by spectral continuation (Proposition 4);
  - an exact asymptotic sign criterion for super- versus subcriticality as $\delta\to0$ (Theorem 5).
- **Aggregate theory** (Sec. 5, formal asymptotics labelled as such):
  - a universal inner problem;
  - closed-form lattice equilibria and biomass;
  - a pairing-mode criterion: within the reduction and under stated hypotheses, the pairing threshold is exactly $p=1$ at leading order (this does not establish merger arrest for $p<1$);
  - PDE benchmarks for the biomass formula and the pairing eigenvalue.

Status labels: **Theorem/Proposition/Lemma** = proved here. **Formal** = matched asymptotics without error bounds. **Numerics** = floating-point computations, each with an exact or convergent benchmark. verify.py tags checks [E] (exact/symbolic or $\ge30$-digit), [F] (floating point / PDE) and [N] (negative control).

## 2. Dimensionless model and steady states

Following [1, S4.1], set $N=c_{\rm ext}n/\kappa$, $I=c_{\rm ext}r_{\rm ext}/m$, $R=c_{\rm ext}r_\times/m$, time $1/\kappa$ and length $\sqrt{D_{\rm ext}/\kappa}$:
$$
N_t=\mu N\big((1-l)I+\gamma R-1\big)+\sigma N_{xx},\qquad I_t=\beta-I-NI+I_{xx},\qquad R_t=lNI-R-\gamma NR+pR_{xx}, \tag{2.1}
$$
with $\beta=Kc_{\rm ext}/(m\kappa)$, $\gamma=c_\times/c_{\rm ext}$, $p=D_\times/D_{\rm ext}$, $\sigma=D_n/D_{\rm ext}$, $\mu=m/\kappa$. Write $U=1+N$ and $V=1+\gamma N$. Nonextinct homogeneous states satisfy $I=\beta/U$ and $R=l\beta N/(UV)$. On this branch $\beta=\hat\beta(V)=V(V+\gamma-1)/(\gamma(V-l))$, and the stable branch is $\hat\beta'(V)>0$.

**Proposition 0 (re-derivation of [1, Eqs. 7–9]).** The following hold.

1. Nonextinct states exist iff $\beta>\beta_v$, with $\beta_v=1/(1-l)$ for $l(1+\gamma)\le1$ and $\beta_v=(\sqrt l+\sqrt{l+\gamma-1})^2/\gamma$ otherwise. The two expressions agree at $l=1/(1+\gamma)$.
2. With $\sigma=0$, the stable homogeneous state is Turing-unstable iff $V<V_s:=\gamma l/(p(1-l))$, i.e. iff $\beta<\beta_s=\hat\beta(V_s)$, which is Eq. (9).
3. A Turing window exists iff $l>l^\star$, with $l^\star$ as in Eq. (8).
4. $\beta_s=\beta_v$ at $l=l^\star$.

*Proof.* Items 1 and 2 follow by direct algebra from (2.1); verify.py checks Eqs. S16–S22 and S44 symbolically. For item 3 there are two cases. If $l(1+\gamma)\le1$, the window exists iff $V_s>1$, i.e. $l>p/(\gamma+p)$. This is compatible with $l(1+\gamma)\le 1$ only when $p<1$. If $l(1+\gamma)>1$, the window exists iff $V_s>V_m=l+\sqrt{l(l+\gamma-1)}$. Using $V_s>l$, this is equivalent to
$$q(l)=\gamma^2l-2\gamma pl(1-l)-(\gamma-1)p^2(1-l)^2>0.$$
The root of $q$ in $(0,1)$ is $(2p-\gamma+S)/(2p+\gamma+S)$ with $S^2=\gamma^2+4p\gamma(p-1)$; this is checked by exact polynomial reduction modulo $S^2-\gamma^2-4p\gamma(p-1)$. Item 4 is checked at 30 digits in five cases. As further checks, 40000 random parameter triples reproduce item 3 with no mismatch, and the negative control of using $p/(\gamma+p)$ for $p>1$ fails. $\square$

So we confirm Eqs. (7)–(9) and the stated wedge structure. We found no discrepancy in the source's linear formulas.

## 3. Exact linear theory of the full three-field model

Linearise (2.1) about the stable homogeneous state with $e^{ikx}$ perturbations. Put $A=U+k^2$, $B=V+pk^2$, $s=\sigma k^2$. Then
$$
J(k)=\begin{pmatrix}-s&\mu(1-l)N&\mu\gamma N\\-I&-A&0\\ lI/V&lN&-B\end{pmatrix},\qquad
\lambda_{\rm qs}(k)=-s+\mu NI\,\frac{Q_0+Q_1k^2}{AB},
$$
with
$$Q_0=-\frac{V^2-2lV-l(\gamma-1)}{V}=-\frac{\gamma(V-l)^2\hat\beta'(V)}{V}<0,\qquad Q_1=\frac{\gamma l}{V}-(1-l)p .$$
Here $\lambda_{\rm qs}$ is the source's adiabatic dispersion relation (their Eqs. 6 and S31; we checked it symbolically).

**Theorem 1 (exact reduction of the stationary spectrum).** For all $\mu>0$, $\sigma\ge0$ and $k$,
$$\det J(k)=(U+k^2)(V+pk^2)\,\lambda_{\rm qs}(k).$$
Write $\det(\lambda-J(k))=\lambda^3+a_1\lambda^2+a_2\lambda+a_3$ (explicit in Theorem 2). Consequently:
- (a) if $\lambda_{\rm qs}(k)>0$, then $J(k)$ has a positive real eigenvalue;
- (b) $J(k)$ has a zero eigenvalue iff $\lambda_{\rm qs}(k)=0$; so the stationary neutral set $\{\lambda_{\rm qs}=0\}$ does not depend on $\mu$;
- (c) at fixed $(\mu,\sigma,k)$, $J(k)$ is stable (all eigenvalues in $\{{\rm Re}\,\lambda<0\}$) iff $\lambda_{\rm qs}(k)<0$ and $a_1a_2-a_3>0$. In particular, at every $k$ where $a_1a_2-a_3>0$, stability is decided by the sign of $\lambda_{\rm qs}(k)$ alone; where $a_1a_2-a_3<0$, $J(k)$ is unstable whatever the sign of $\lambda_{\rm qs}(k)$;
- (d) for $\sigma=0$ and every $\mu$ such that $a_1a_2-a_3>0$ for all $k\ge0$ (Theorem 2 gives explicit sufficient conditions), the homogeneous state is stable at $k=0$ and unstable exactly on the quasi-static band $(k_-,\infty)$, $k_-^2=-Q_0/Q_1$, which is non-empty iff $Q_1>0$. For such $\mu$, Eqs. (8)–(9) describe the instability region exactly. At $\beta=\beta_s$ the critical wavenumber is infinite.

*Proof.* Block elimination on the resource block gives the identity: $\det\begin{pmatrix}-A&0\\lN&-B\end{pmatrix}=AB>0$, and the Schur complement of that block is $\lambda_{\rm qs}$. The identity is also checked symbolically. For (a): a real $3\times3$ matrix with positive determinant has an odd number of positive real eigenvalues counted with multiplicity, because complex eigenvalues come in conjugate pairs with positive product. Item (b) is immediate. For (c): $a_1=s+A+B>0$ and $a_3=-\det J=-AB\,\lambda_{\rm qs}$, and by the Routh–Hurwitz criterion a real cubic with $a_1>0$ has all roots in the open left half-plane iff $a_3>0$ and $a_1a_2-a_3>0$. Item (d) follows from (c), since $\lambda_{\rm qs}(0)=\mu NIQ_0/(UV)<0$ on the stable branch and, for $\sigma=0$, $\lambda_{\rm qs}(k)$ has the sign of $Q_0+Q_1k^2$; as $k\to\infty$, $k^2\lambda_{\rm qs}\to\mu NIQ_1/p$. $\square$

A negative determinant alone does not imply stability. At $(l,\gamma,\beta,p,\mu,k^2)=(0.9,1,5,10,10^4,0.1)$ on the upper branch ($V=3.8228756555$), $\lambda_{\rm qs}\approx-4096.78$, yet $J$ has the two positive real eigenvalues $\approx55.699$ and $17.071$ (and $-81.516$): there $a_1a_2-a_3<0$. This example (due to the referee of an earlier version) is a negative control in verify.py. It is consistent with (c), and it shows that the quasi-static model can miss real growing modes once an oscillatory crossing has occurred.

Item (d) means that with $D_n=0$ the stationary onset is degenerate, so a weakly nonlinear analysis needs $D_n>0$ (Sec. 4).

**Theorem 2 (the Hurwitz determinant: where the quasi-static picture can fail).** Write $\det(\lambda-J)=\lambda^3+a_1\lambda^2+a_2\lambda+a_3$. Then
$$a_1=s+A+B,\qquad a_3=-\det J,$$
$$a_1a_2-a_3=(s+A)(A+B)(B+s)+\mu NI\Big[U\big(1-l(1+\gamma)\big)+k^2\Big(1-l-\frac{p\gamma l}{V}\Big)+s\Big(1-l-\frac{\gamma l}{V}\Big)\Big].$$
If $\lambda_{\rm qs}(k)<0$, a pair of eigenvalues crosses the imaginary axis at $k$ exactly where $a_1a_2-a_3=0$, i.e. at
$$\mu=\mu_H(k)=\frac{(s+A)(A+B)(B+s)}{NI\,(-[\cdots])},\qquad\text{when }[\cdots]<0 .$$
In particular, when $\sigma=0$:
- (i) the well-mixed state undergoes a Hopf bifurcation iff $l(1+\gamma)>1$, at $\mu_H(0)=V(U+V)/\big(NI(l(1+\gamma)-1)\big)$;
- (ii) the bracket is negative for all large $k$ iff $(1-l)V<p\gamma l$; then an oscillatory instability exists at those wavenumbers for $\mu>\mu_H(k)$, unless a stationary one occurs there first. If moreover $l(1+\gamma)\le1$, every oscillatory instability has finite wavelength (a wave instability);
- (iii) if $l(1+\gamma)\le1$ and $(1-l)V\ge p\gamma l$, no oscillatory instability exists for any $\mu$ and $k$.

*Proof.* The coefficients follow by expansion, using the identity $(x+y+z)(xy+yz+zx)-xyz=(x+y)(y+z)(z+x)$; this is checked symbolically. On $a_1>0$, $a_3>0$, the Routh–Hurwitz conditions fail through a purely imaginary pair exactly when $a_1a_2=a_3$. Then $a_2=a_3/a_1>0$ and the eigenvalues are $\pm i\sqrt{a_2}$. Items (i)–(iii) read off the sign of the bracket. $\square$

Remarks.

- For $p=1$, condition (ii) coincides with the Turing condition $Q_1>0$.
- For $p>1$, condition (ii) is weaker than $Q_1>0$. So wave instabilities exist where the quasi-static theory predicts stability. Example: $l=0.5$, $\gamma=1$, $p=10$, $\beta=4$ gives $Q_1<0$, and the onset is at $\mu^*=290.7$, $k^2=0.375$, $\operatorname{Im}\lambda\approx17.8$.
- These thresholds are large because biomass dynamics are usually slow ($\mu\ll1$).
- At the source's PDE parameters ($\beta=5$, $l=0.999$, $\gamma=1$, $\sigma=10^{-3}$, $\mu=1$) we find, on a fine grid in $k$, $\min_k\mu_H=7.258>1$, i.e. $a_1a_2-a_3>0$ there (a numerical check, not a proof for all $k$). Under this condition their onset predictions are exact by Theorem 1(c).
- The quasi-static Eq. (6) places the fastest-growing mode within $0.3\%$ in $k$ and $2\%$ in rate of the exact $3\times3$ peak.

**Theorem 3 (biomass dispersal).** Let $\sigma>0$ and $\delta:=\sigma/\mu=D_n\kappa/(D_{\rm ext}m)$. There is $k>0$ with $\lambda_{\rm qs}(k)>0$ iff $Q_1>0$ and
$$\frac{\delta}{NI}<\varepsilon_c:=\max_{x>0}\frac{Q_0+Q_1x}{x(U+x)(V+px)} .$$
If moreover $a_1a_2-a_3>0$ for all $k$, then by Theorem 1(c) this is exactly the condition for diffusion-driven instability of the stable homogeneous state. The maximiser $x_c=k_c^2$ is the unique positive root of
$$2pQ_1x^3+\big(Q_1(V+pU)+3pQ_0\big)x^2+2Q_0(V+pU)x+Q_0UV=0 .$$
As $Q_1\to0^+$,
$$\varepsilon_c=\frac{4Q_1^3}{27pQ_0^2}\,(1+o(1)),\qquad k_c^2=-\frac{3Q_0}{2Q_1}\,(1+o(1)).$$
If $l(1+\gamma)<1$, then $NI\varepsilon_c\to0$ as $\beta\to\beta_v^+$. So dispersal creates a second (lower) onset boundary near the viability threshold, and the instability band in $\beta$ becomes bounded on both sides.

*Proof.* By Theorem 1(b), the zero set of $\det J$ is that of $\lambda_{\rm qs}$, i.e. of $-\delta x(U+x)(V+px)+NI(Q_0+Q_1x)$. This expression depends on $\mu$ only through $\delta$. The cubic is the tangency condition. Its coefficient signs are $(+,\,?,\,-,\,-)$, so it has exactly one sign change and, by Descartes' rule, one positive root. The asymptotics follow by balancing the dominant terms. The last claim holds because $N\to0$ while $Q_0$ and $Q_1$ stay finite as $V\to1$. $\square$

## 4. Weakly nonlinear analysis at the regularised onset

Steady states of (2.1) depend on $(\mu,\sigma)$ only through $\delta$. Throughout this section we divide the biomass equation by $\mu$, so that the steady problem reads $\tilde f(u)+\tilde D u_{xx}=0$ with $\tilde f=(N((1-l)I+\gamma R-1),\ \beta-I-NI,\ lNI-R-\gamma NR)$ and $\tilde D={\rm diag}(\delta,1,p)$. All objects below refer to this rescaled system: $J_0:=D\tilde f(u_0)$, $\mathcal B$ is the symmetric bilinear form of the quadratic part of $\tilde f$ (so $\tilde f(u_0+v)=J_0v+\tfrac12\mathcal B[v,v]$ exactly), and $L(k):=J_0-k^2\tilde D$, which is $J(k)$ with its first row divided by $\mu$. At onset $\beta=\beta_c(\delta)$, $k=k_c$. Its null vectors have closed forms:
$$\phi=\Big(1,\;-\frac{I}{U+x},\;\frac{lI/V+lN\phi_I}{V+px}\Big),\qquad \psi=\Big(1,\;\frac{(1-l)N+lN\psi_R}{U+x},\;\frac{\gamma N}{V+px}\Big).$$

**Proposition 4 (Landau coefficient).** On a periodic domain of period $2\pi/k_c$, the bifurcating stationary branch is
$$u=u_0+A\phi\cos k_cx+O(A^2),\qquad \beta-\beta_c=\beta_2A^2+O(A^4),$$
$$\beta_2=-\frac{\psi\cdot\big(\mathcal B[\phi,u_{20}]+\tfrac12\mathcal B[\phi,u_{22}]\big)}{\psi\cdot\mathcal B[\partial_\beta u_0,\phi]},$$
where $J_0u_{20}=-\tfrac14\mathcal B[\phi,\phi]$, $L(2k_c)u_{22}=-\tfrac14\mathcal B[\phi,\phi]$ and $J_0\partial_\beta u_0=-(0,1,0)^T$. This is a rational function of $(l,\gamma,p,V_c,x_c,\delta)$, given in closed form in verify.py. Instability occurs for $\beta<\beta_c$. So the bifurcation is supercritical iff $\beta_2<0$. In the time-dependent problem, the bifurcating branch is stable iff the bifurcation is supercritical, provided $\mu<\min_k\mu_H$; the sign of $\beta_2$ does not depend on $\mu$.

*Proof sketch (standard).* Lyapunov–Schmidt reduction of the reflection-symmetric steady problem gives a pitchfork; the reflection symmetry kills the even-order terms. Because $f$ is quadratic, the cubic coefficient involves only the second-order corrections. The direction of the branch is a steady-state quantity and depends on $\delta$ alone. Exchange of stability then applies, because the crossing eigenvalue is simple and $d\lambda/d\beta$ has the sign of $d\lambda_{\rm qs}/d\beta$. That holds by Theorem 1, as long as the other two eigenvalues have positive product, which is guaranteed when no Hopf crossing has occurred (Theorem 2). $\square$

Numerics with exact benchmark: spectral Newton continuation of the periodic branch (48 modes) reproduces $\beta_2$. At $(l,\gamma,p,\delta)=(0.9,1,0.5,10^{-3})$ the Richardson extrapolant agrees to $7\times10^{-8}$ relative, and the branch is subcritical. At $(0.36,1.93,0.59,10^{-4})$ the agreement is $10^{-5}$ relative, and the branch is supercritical. So both signs occur.

**Theorem 5 (criticality as $\delta\to0$).** Fix $(l,\gamma,p)$ in the Turing region of Proposition 0 and put $\eta=\delta^{1/3}$. The upper onset satisfies $V_c=V_s+O(\eta)$ and $k_c^2=X/\eta+O(1)$, with $X^3=NI|Q_0|/(2p)$ evaluated at $V_s$. Moreover $\beta_2=C\eta+O(\eta^2)$ with
$$\frac{C}{X^2}=-\frac{\gamma^2\,\Sigma}{108\,(V_s-l)(V_s-1)^3(1-l)\,(V_s^2-2lV_s-l(\gamma-1))},$$
$$\Sigma=-37\nu^4+48s\nu^3+(126s^2+122a)\nu^2+204sa\nu+41a^2,$$
where $\nu=V_s-1$, $s=1-l$ and $a=1-l(1+\gamma)$. The denominator is positive. Hence, if $\mathcal S(\zeta,\alpha)\neq0$, for all sufficiently small $\delta$ the onset is supercritical when $\mathcal S>0$ and subcritical when $\mathcal S<0$, where
$$\mathcal S(\zeta,\alpha):=41\alpha^2+(122+204\zeta)\alpha+126\zeta^2+48\zeta-37,\qquad \zeta=\frac{1-l}{V_s-1},\quad\alpha=\frac{1-l(1+\gamma)}{(V_s-1)^2}.$$
On the curve $\mathcal S=0$ the leading term vanishes and the sign requires the next order, which we do not compute.
The homogeneous state is stable iff $1+2\zeta+\alpha>0$.

*Proof.* In the scaled variables $(X,v)$, with $V=V_s+\eta v$ and $x=X/\eta$, the two onset equations are polynomial in $(\eta,X,v)$. At $\eta=0$ they reduce to
$$-pX^3+NIQ_0-NI\gamma lvX/V_s^2=0,\qquad -3pX^2-NI\gamma lv/V_s^2=0.$$
The Jacobian determinant there is $-6pNI\gamma lX^2/V_s^2\neq0$. So the implicit function theorem gives an analytic onset branch in $\eta$. Substituting it into the rational function of Proposition 4 gives an expansion in $\eta$ in which every leading-order cancellation comes from exact identities. One is $(1-l)\phi_I+\gamma\phi_R=\delta x/N$, so that $\mathcal B_1[\phi,\phi]=2\delta x/N$. Another is $\gamma l/p=(1-l)V_s$ at $V_s$, which reduces $J_0^{-1}$ applied to $(0,1,-1)$ to closed form. Collecting the $O(\eta)$ terms gives $C$. Because $u_{22,N}$, the $N$-component of $u_{22}$, depends on $X$ only through $X^3$, $C/X^2$ is rational. Its factorisation is symbolic. We checked $C$ against 90-digit evaluations of the exact $\beta_2$ at $\delta=10^{-45}$ (relative agreement $<10^{-8}$ in three cases) and the sign rule in 16 random cases at $\delta=10^{-24}$. For the denominator: $V_s>1>l$, and $V_s^2-2lV_s-l(\gamma-1)=-V_sQ_0>0$. $\square$

**Corollaries.**
- (i) Next to $l^\star$ for $p<1$ (that is, $V_s\to1$), $\Sigma\to41a^2>0$, so the onset is supercritical.
- (ii) Next to the fold, $\alpha\to-1-2\zeta$ and $\mathcal S=-118(1+\zeta)^2<0$, so the onset is subcritical. This covers the whole neighbourhood of $l^\star$ for $p>1$.
- (iii) For $a=0$ the onset is supercritical iff $\zeta>0.384$.
- (iv) In the source's regime ($l=0.999$, $\gamma=1$, $p\in\{0.1,1,2\}$) $\mathcal S<0$, and $\beta_2>0$ also at $\delta=10^{-3}$. The onset is subcritical. This fits the compact, strongly nonlinear aggregates seen in [1].

The criterion is asymptotic. At $\delta=10^{-2}$ we found a case where the actual sign differs from the limit; verify.py includes it as a negative control.

## 5. Aggregates in the small-dispersal limit (formal asymptotics)

**5.1 Inner problem.** As $\delta\to0$ the biomass concentrates into cores of mass $M$ and width
$$w=\Big(\frac{\delta}{|c_0|M}\Big)^{1/3},\qquad c_0=(1-l)I-\gamma(lI-\gamma R)/p ,$$
evaluated at the core. Quasi-statically, $g=(1-l)I+\gamma R-1$ satisfies $g''=c_0N$ inside the core. Writing $N=(M/w)\varphi(y)$ and $g=g_c+w|c_0|M\Psi(y)$ gives the universal problem
$$\varphi''+(E+\Psi)\varphi=0,\qquad \Psi''=-\varphi,\qquad \int\varphi=1,\qquad \Psi+|y|/2\to0. \tag{5.1}$$
This is a one-dimensional self-trapping (Schrödinger–Newton type) problem with a source linear in $\varphi$. We compute a positive ground state with $E=1.05624$. Integrating (5.1) gives the exact identity $E=-\int\varphi\Psi$. A core exists only where $g$ has a cusp maximum, i.e. $c_0<0$. For homogeneous values $c_0=-IQ_1/p$, so this is the local form of the Turing condition.

The scaling $w\propto\delta^{1/3}$ differs from the $\delta^{1/2}$ widths of autocatalytic spikes (Gray–Scott, Gierer–Meinhardt, Klausmeier [6–10]) and of smooth-potential Dirac concentration. The reason is that growth here is linear in $N$ and the potential is self-generated with a cusp.

**5.2 Outer problem and lattice equilibria.** To leading order the cores are point sinks of $I$ (strength $MI$) and point sources of $R$ (strength $M(lI-\gamma R)$). Their masses evolve by $\dot M_j=\mu M_jg(x_j)$. Their positions drift by $\dot x_j=\kappa\,\mu w_j^2\,\partial_xg_{\rm reg}(x_j)$, where $g_{\rm reg}$ is the outer growth rate minus the cusp term of core $j$ itself and $\kappa$ is the inner mobility. Solving the linearised moving version of (5.1) gives $\kappa=3.4125>0$: cores climb the far-field gradient of the growth rate. The drift is slow, $O(\delta^{2/3})$. If, in addition, the fast subsystem of core masses and resources is linearly stable at fixed core positions, the masses are slaved to the positions. We do not prove this stability; we assume it below and observe it in the PDE computations.

**Proposition 6 (lattice equilibria, within the point-core reduction).** An equally spaced lattice of spacing $d$ has mean biomass
$$\bar m(d)=\frac{N_0\big(\beta,l,\gamma r(d)\big)}{h(d)},\qquad h(y)=\frac y2\coth\frac y2,\qquad r(d)=\frac{h(d/\sqrt p)}{h(d)},$$
where $N_0(\beta,l,\gamma)$ is the stable homogeneous biomass.

*Proof.* The lattice Green sums are $\coth(d/2)/2$ and $\coth(d/(2\sqrt p))/(2\sqrt p)$, checked at 30 digits. With $X=\bar m\,h(d)$ and $Y=rX$ they give $I=\beta/(1+X)$ and $R=lIY/(1+\gamma Y)$. The core condition $(1-l)I+\gamma R=1$ becomes $\beta(1-l+\gamma rX)=(1+X)(1+\gamma rX)$, which is the homogeneous steady-state law with $\gamma\to\gamma r$. $\square$

Because $h>1$, for $p=1$ the patterned biomass is $N_0/h(d)<N_0$ for every spacing, independently of $\beta$, $l$ and $\gamma$. This explains the source's observation that biomass decreases for $p=1$ even with a single aggregate (their Fig. S7). For $p<1$ we have $r>1$, and cross-feeding is effectively enhanced. Biomass increases at a given spacing iff $N_0(\gamma r)>h(d)N_0(\gamma)$. With spacing equal to the linear wavelength at the source's Fig. 3c parameters ($\beta=5$, $l=0.999$), we get $\bar m/N_0=1.10$ for $p=0.1$ and $0.79$ for $p=1$. These match the signs they report for Fig. 3d (a full-model computation, so the comparison is qualitative).

PDE benchmark (numerics): steady single-aggregate states of (2.1) on a Neumann cell. With $l=0.9$, $\gamma=1$, $p=0.5$, $\beta=5$, $d=4$ and $\delta=10^{-5},10^{-6},10^{-7}$, the relative error in mean biomass relative to Proposition 6 is $0.0336$, $0.0151$, $0.0069$: it falls by factors $2.22$ and $2.18$ per decade, close to the predicted $10^{1/3}=2.154$. With the $O(\delta^{1/3})$ inner corrections (eigenvalue $E$, consumption and production integrals) the relative errors are $+0.0112$, $-0.0077$, $-0.0010$: smaller than at leading order at each $\delta$, but the decrease is irregular (factors $1.46$ and $7.50$), so we do not claim a rate for the corrected formula. The growth rate is negative away from the core, so empty space is not invaded. In isolated cores this requires $\beta<1/(1-l)$.

**5.3 The pairing mode: coarsening versus arrest.** We work within the point-core reduction and assume: (H1) an equally spaced lattice of cores exists with $c_0<0$ at the cores (cusp confinement); (H2) the fast mass/resource subsystem is stable at fixed positions (Sec. 5.2); (H3) the growth rate is negative between cores (no invasion of empty space). The asymptotics are at fixed spacing $d$ as $\delta\to0$; they are not uniform in $d$. Consider the alternating (pairing) mode of the lattice. At this mode the mass perturbations decouple by symmetry. Its translational growth rate is $\kappa\mu w^2S_\pi$, with
$$S_\pi=-\frac{(1-l)MI}{\sinh d}+\frac{\gamma M(lI-\gamma R)}{p^{3/2}\sinh(d/\sqrt p)} .$$
Here $MI$ and $M(lI-\gamma R)$ are the core's consumption of $I$ and production of $R$ (Sec. 5.2). Hence the lattice is pairing-unstable iff
$$\rho_c\,\varphi_p(d)>1,\qquad \varphi_p(d)=\frac{\sinh d}{\sqrt p\,\sinh(d/\sqrt p)},\qquad \rho_c=\frac{\gamma(lI-\gamma R)}{p(1-l)I}=\frac{\gamma l}{p(1-l)(1+\gamma Y)} .$$
The core condition $c_0<0$ is exactly $\rho_c>1$.

**Lemma 7.** $\varphi_p\ge1$ for $p\ge1$. For $p<1$, $\varphi_p$ decreases from $1$ to $0$.

*Proof.* $t\mapsto\sinh t/t$ is increasing, and $t\mapsto t\coth t$ is increasing. $\square$

**Corollary 8 (formal; pairing mode only; under (H1)–(H3)).** If $p\ge1$, every equally spaced lattice is pairing-unstable at every spacing; since one unstable mode suffices, every such lattice is unstable within the reduction, with rate decaying like $e^{-d/\sqrt p}$. If $p<1$, the pairing mode is stable for $d>d_\pi(p)$, where $\rho_c\varphi_p(d_\pi)=1$, and for large spacings and $p$ near $1$
$$d_\pi\approx\frac{\ln(\rho_c/\sqrt p)}{1/\sqrt p-1}\sim\frac{2\ln\rho_c}{1-p}\to\infty\quad\text{as }p\to1^- .$$
So **the pairing threshold is exactly $p=1$ at leading order.** For $p<1$ this does not establish stability of the lattice: other displacement modes, mass redistribution, resource dynamics and invasion between cores are not controlled, and we have no general extremality result for the pairing mode. Since the asymptotics are at fixed $d$, the statement about $d_\pi\to\infty$ as $p\to1^-$ is formal. Physically, the depletion interaction (range $1$) and the cross-feeding attraction (range $\sqrt p$) exchange dominance at large separations exactly when $p=1$; the cusp condition guarantees that attraction wins at short range. This gives a mechanism, within the reduction, for the source's observation of coarsening for $p\gtrsim1$, and is consistent with its observation of arrest for $p<1$.

In the reduced eight-core ring model, the slaved translational Jacobian (computed by finite differences) has the alternating mode as its extreme eigenvalue in the four tested cases, and its stiffness equals the closed-form $S_\pi$. This is evidence for, not a proof of, extremality among translational modes; mass-exchange modes are not computed in verify.py.

PDE benchmark (numerics): we computed the pairing eigenvalue of the full linearised PDE on a Neumann cell containing one core, whose reflections realise the alternating mode. For $p=0.5$, $d=2$, the ratio of the PDE eigenvalue to the prediction is $0.41$ and $0.72$ at $\delta=10^{-5},10^{-6}$: it increases towards $1$, consistent with $O(\delta^{1/3})$ corrections, but two values do not establish a rate. The signs of the pairing eigenvalue agree with Corollary 8 at $\delta=10^{-6}$: for $p=0.5$, $d=6$ it is negative, and for $p=1$ and $p=2$ at $d=4$ it is positive. (A negative pairing eigenvalue says nothing about other modes.) In a direct simulation at $\delta=10^{-4}$, $p=1$, eight cores at spacing 2 coarsen: eight to six at $t\approx7.5\times10^3$, to four by $1.1\times10^4$, to three by $2.5\times10^4$ and to two by $5.7\times10^4$. Under the same conditions with $p=0.5$, all eight persist to $t=1.3\times10^5$. That agrees in sign with the PDE pairing eigenvalue at this $\delta$, which is negative ($-2.7\times10^{-4}$); these simulations are illustrations, not part of verify.py's checks. The leading-order theory predicts instability there. This is a real finite-$\delta$ effect: the $O(\delta^{1/3})$ corrections stabilise dense lattices. A second example is $p=2$, $d=2$, $\delta=10^{-4}$, which is stable in the PDE (a negative control in verify.py). The source's simulations use $\delta=10^{-3}$. There these corrections are substantial, which is consistent with their observation of arrest at about the initial wavelength for $p<1$.

## 6. Discussion and limitations

**Exact versus formal.** The exact results are:
- the timescale independence of the stationary neutral set, and the exact stability criterion $\lambda_{\rm qs}<0$, $a_1a_2-a_3>0$;
- the Routh–Hurwitz description of the oscillatory boundary;
- the dispersal threshold;
- the closed form of $\beta_2$;
- its $\delta\to0$ sign criterion. The coefficient $C$ is obtained by an explicit expansion and cross-checked at 90 digits; we did not write out the $O(\eta^2)$ remainder bound.

Everything in Sec. 5 is formal matched asymptotics, plus:
- two numerical constants ($E$ and $\kappa$; the positivity of $\kappa$ is numerical);
- PDE checks that converge at the predicted rate.

**Scope.** Our model is the source's coarse-grained Eq. (5), in one space dimension. We do not treat the 20-species model, two-dimensional patterns, or the community-composition results. Corollary 8 concerns the pairing mode of lattices of identical cores under (H1)–(H3). For $p<1$ it does not establish stability or merger arrest; we checked other translational Fourier modes in a reduced model but did not prove that the pairing mode is extremal, and we did not analyse mass redistribution or invasion.

**Practical consequences.** The source's onset formulas are exact for every timescale ratio for which no oscillatory crossing occurs ($a_1a_2-a_3>0$), which requires $\mu$ below explicit thresholds (about 7.3 at their parameters). Patterns there emerge subcritically. Within the point-core reduction, $p\ge1$ makes every equally spaced lattice unstable through its pairing mode, while for $p<1$ the pairing mode is stabilised beyond a spacing that diverges as $p\to1^-$.

## References

[1] J. Kocka, S. A. Redford, J. Agudo-Canalejo, K. Husain, Nutrient limitation drives Turing instabilities in cross-feeding microbial communities, arXiv:2611.27534v2 (2026).
[2] R. Marsland III et al., Available energy fluxes drive a transition in the diversity, stability, and functional structure of microbial communities, PLoS Comput. Biol. 15 (2019) e1006793.
[3] A. M. Turing, The chemical basis of morphogenesis, Phil. Trans. R. Soc. B 237 (1952) 37.
[4] M. C. Cross, P. C. Hohenberg, Pattern formation outside of equilibrium, Rev. Mod. Phys. 65 (1993) 851.
[5] C. A. Klausmeier, Regular and irregular patterns in semiarid vegetation, Science 284 (1999) 1826.
[6] D. Iron, M. J. Ward, J. Wei, The stability of spike solutions to the one-dimensional Gierer–Meinhardt model, Physica D 150 (2001) 25.
[7] T. Kolokolnikov, M. J. Ward, J. Wei, The existence and stability of spike equilibria in the one-dimensional Gray–Scott model, Physica D 202 (2005) 258.
[8] W. Sun, M. J. Ward, R. Russell, The slow dynamics of two-spike solutions for the Gray–Scott and Gierer–Meinhardt systems, SIAM J. Appl. Dyn. Syst. 4 (2005) 904.
[9] R. Bastiaansen, A. Doelman, The dynamics of disappearing pulses in a singularly perturbed reaction-diffusion system with parameters that vary in time and space, arXiv:1802.02737 (2018).
[10] Y. Chen, T. Kolokolnikov, J. Tzou, C. Gai, Patterned vegetation, tipping points, and the rate of climate change, Eur. J. Appl. Math. 26 (2015) 945.
[11] N. F. Britton, Spatial structures and periodic travelling waves in an integro-differential reaction-diffusion population model, SIAM J. Appl. Math. 50 (1990) 1663.
[12] S. Genieys, V. Volpert, P. Auger, Pattern and waves for a model in population dynamics with nonlocal consumption of resources, Math. Model. Nat. Phenom. 1 (2006) 63.

# The top layer of the Alpöge–Claude Lean argument for RH: one-sided Chebyshev windows, an inert-prime balance identity in a CM host, and the per-host inequality

## 0. Problem, contribution and status

**Problem.** On 2026-11-20 Alpöge announced a Lean formalization, written with Claude, that claims to prove the Riemann hypothesis and its analogue for Dirichlet $L$-functions [1, 2]. The source is large, and no natural-language account of the argument exists. This paper is the first of a series that writes the argument out in prose. It covers the layer that runs from Mathlib's statement `RiemannHypothesis` down to a single inequality for prime sums in an abelian CM field. Later papers treat that inequality.

**Contribution.** The following are proved here, at the labels given below.
1. *Reduction to windows* (§1-§3). RH, and zero-freeness of every Dirichlet $L(\chi,s)$ for $\operatorname{Re}s>1/2$, follow if for each primitive $\psi$ the weighted Chebyshev function $\mathrm{Gm}_{\mathrm{cyc}(\psi)}$ is at most $x^{1/2+c_0\varepsilon}$ on windows $[Y,Y^{3/2}]$, with $c_0$ fixed before $\varepsilon$ (Theorem 3.4). The weight $(3\operatorname{ord}\psi+1)^{-1}$ is explained in Remark 4.10a.
2. *Balance identity* (§4.3). For a host field $E$, the identity $\mathrm{ASK}-\mathrm{MAIN}=\mathrm{De}$ (Theorem 4.7) is exact. Here ASK is a ramp-weighted sum over prime powers inert in $K=\mathbb Q(\sqrt{-d})$, MAIN is an explicit main term, and De is a combination of the character functions $G_\chi$ of $E$. The identity uses orthogonality and the shape of ramification, and no reciprocity.
3. *Per-host inequality* (§4.4). A bound $\mathrm{gapA}\le x^{O(\varepsilon)}\mathrm{Br}$ for the summed gap, together with the host conditions, implies $\mathrm{Gm}_\Lambda(x)\le x^{1/2+(e_D+e_L+7)\varepsilon}$ (Theorem 4.9). The bracket Br balances an error of relative size $x/m$ against one of relative size $m$. The window $x^{1/2-\varepsilon}\le m\le x^{1/2+\varepsilon/2}$ is what produces the exponent $1/2$ (Proposition 4.13, Remark 4.14).
4. *Characters that are not kept* (§4.5). For hosts built from auxiliary primes $(q,d)$, the bounds needed at these characters follow from a good pair (Theorem 4.16). The source's proof that good pairs exist, from a mean square over $q$ and a zero-density count, is outlined at statement level (Theorem 4.17). Version 2 adds how the mean square stays uniform in the growing progression modulus (Lemma 4.18).
5. *Obligations* (§4.6). The hypotheses that this layer leaves open are listed with their suppliers in the source, and Corollary 4.24 states the conditional theorem they give.

**What is not proved here.** The inequality $\mathrm{gapA}\le x^{O(\varepsilon)}\mathrm{Br}$ is the content of the argument. It rests on hermitian-lattice and automorphic inputs (Frame_at, Theorem S, UAt), and so does the existence of host families (VWin, TopG). The compatibility conditions between hosts and levels, ThinScales, and the existence of good pairs are also left open; for conductor one, good pairs are proved in [10, §2]. This paper does not prove them. The table in §4.6 states them as obligations. Without them this paper proves only that they imply RH.

**Related work.** Paper 190 [3] proves the one-sided Landau criterion on power intervals for $G_z$ and for positive sums of character ramps. It also computes the exact window exponent, and gives the endpoint constant $2+\gamma-\log(4\pi)$ under RH. Our §2 is the same criterion as the source states it (`lemmaL`, `landau_window`). It is included so that the chain to Mathlib's statement is complete in one place, and readers may substitute [3, Theorem 1 and §4]. The overlap goes further. [3, §6] proves the two estimates for auxiliary characters that we use in §4: the finite-sum estimate on a fixed-width zero-free rectangle [3, Prop. 3], which is our Lemma 4.20, and the uniform bound at the larger cutoff [3, Prop. 4], which is the estimate behind ThinH and ThinScales (Definition 4.11). Readers may take both from [3]. What this paper adds beyond [3]: the level structure and the weight $(3o+1)^{-1}$ (§3, Remark 4.10a); the CM host and the balance identity (§4.1-§4.3); the per-host inequality with its bracket (§4.4); the reduction of the bounded characters to good pairs (Theorem 4.16) and an outline of the source's selection of pairs (§4.5); and the obligation table (§4.6). bramble_trace's forum reading [4] describes the positive family and the windows. The classical inputs are Landau's theorem on Dirichlet integrals with nonnegative coefficients [5], the explicit formula, and the Siegel–Walfisz and zero-density estimates [6]. Paper 193 [10] proves the selection of good pairs in natural language for the conductor-one case ($M=1$, trivial $\xi$), including the growing-modulus step of Lemma 4.18, and adds class-number conditions on the same pair. Suzuki's screw-function criteria [7] are another positivity criterion for RH. They are related background and do not replace the host-field reduction described here.

**Status of the source.** We read the source at commit a172c464 [2] and did not rerun it. We assume the Lean kernel check is sound. Assuming kernel soundness, or reading a proof term, is not the same as checking the dependency chain below it, and we have not checked that chain except where a label says so. The Comparator run on the submission has not reported [2, README]. The source states five theorems in `Challenge.lean`, which imports only Mathlib.

**Conventions.**
- Paths are relative to `src/` at commit a172c464.
- Every lemma carries its Lean name, file and line, and one label:
  - **[read, proof]**: we read the statement and the whole proof;
  - **[read, statement]**: we read the statement and how it is used, not its proof;
  - **[checked]**: a numerical script in the supplement confirms the identity, and named wrong variants fail;
  - **[derived]**: our own deduction from the cited statements.
- Appendix A lists every cited declaration and its label.
- Notation. $\Lambda$ is the von Mangoldt function, $\gamma$ is Euler's constant, $(z)^+=\max(z,0)$. For a Dirichlet character $\chi$ mod $N$,
  $$\mathrm{ramp}_\chi(y)=\sum_{n\le y}\Lambda(n)\chi(n)\,(y/n-1)^+ .$$

For $\zeta$ alone the weighted Chebyshev function is
$$G_z(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x .$$

## 1. The top reduction

**Theorem 1.1** (the source's claimed conclusion; `riemannHypothesis`, Main.lean L4) [read, statement and proof term]. The source claims that Mathlib's `RiemannHypothesis` holds: every nontrivial zero $s\ne1$ of $\zeta$ has $\operatorname{Re}s=1/2$.

The file Statements.lean imports only Mathlib, so the target is Mathlib's own definition. The proof term is `rhOfAll = rh_of_every allChi` (Supplements/Kernels/MainTheorems L9). In this account Theorem 1.1 is conditional. Corollary 4.24 proves it from the obligations listed in §4.6, and those obligations are not proved here.

**Lemma 1.2** (`rh_of_right`, Formalism/GammaFactorNonvanishing/RhOfRight L5-62) [read, proof]. If $\zeta(s)\ne0$ whenever $\operatorname{Re}s>1/2$ and $s\ne1$, then RH holds.

*Proof.* Let $\zeta(s)=0$ with $s$ not a trivial zero and $s\ne1$.
- If $\operatorname{Re}s>1/2$, this contradicts the hypothesis.
- If $\operatorname{Re}s<1/2$, then $s\ne0$ because $\zeta(0)=-1/2$. The functional equation (`riemannZeta_one_sub`) gives
  $$\zeta(1-s)=2(2\pi)^{-s}\Gamma(s)\cos(\pi s/2)\zeta(s).$$
  The Lean proof applies this at $1-s$:
  $$\zeta(s)=2(2\pi)^{-(1-s)}\Gamma(1-s)\cos(\pi(1-s)/2)\,\zeta(1-s).$$
  On the right, $\Gamma(1-s)\ne0$ because $\operatorname{Re}(1-s)>0$, and $\zeta(1-s)\ne0$ by the hypothesis. The cosine vanishes only when $s=-2k$. The case $k<0$ contradicts $\operatorname{Re}s<1/2$, the case $k=0$ is $s=0$, and the case $k>0$ is a trivial zero. So the right side is nonzero, which contradicts $\zeta(s)=0$.
- So $\operatorname{Re}s=1/2$. ∎

**Definition 1.3** (`EveryCharacter`, CharacterBoxes/EveryCharacter L13) [read]. For all $N\ge1$, every Dirichlet character $\chi$ mod $N$, and every $s$ with $\operatorname{Re}s>1/2$ and ($\chi\ne1$ or $s\ne1$), we have $L(\chi,s)\ne0$.

`rh_of_every` (CritLine L29) [read, proof] applies EveryCharacter at $N=1$, $\chi=1$ and rewrites $L(1,s)=\zeta(s)$ (`LFunction_modOne_eq`). Then it calls Lemma 1.2.

**Lemma 1.4** (`imprimitive`, CharacterBoxes/Imprimitive L5-35) [read, proof]. Suppose $L(\psi,s)\ne0$ for every *primitive* $\psi$ and every $\operatorname{Re}s>1/2$. This hypothesis is `ZeroFreeAll`, ExplicitFormulaErrorOfHostConditions L19. Then EveryCharacter holds.

*Proof.* Let $\chi$ be a character mod $N$ induced from the primitive $\chi^*$ mod $f$. Then
$$L(\chi,s)=L(\chi^*,s)\prod_{p\mid N}(1-\chi^*(p)p^{-s})$$
(`LFunction_changeLevel`). Each Euler factor is nonzero because $|\chi^*(p)p^{-s}|<1$ for $\operatorname{Re}s>0$. The condition "$\chi\ne1$ or $s\ne1$" passes to $\chi^*$. ∎

So RH needs only the case $\psi=1$ of ZeroFreeAll. The development proves ZeroFreeAll for all primitive $\psi$ at once and then specialises. The main path from `everyCharacter` (CharacterBoxes/MainConclusion L10) runs through these declarations [read, call level]:
1. `every_character_of_literature_of_vWin` (ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin L810). It takes the bundle of `Published` statements (literature results the source assumes as hypotheses), which this paper does not examine.
2. `every_character_of_theta_integrals_local_matching` (SiegelEisensteinSecondTermHypotheses L69).
3. `every_character_of_green_v_win` and `zero_free_all_of_green_v_win` (TopPlug L12-19). These are `imprimitive` applied to `zeroFreeAll_of_topG` with $la=3/2$.

## 2. Weighted Chebyshev functions and Landau's theorem on windows

This section overlaps [3]. Theorem 2.5 and Corollary 2.6 are the source's form of [3, Theorem 1 and §4]. We state them with Lean names so that each step from Mathlib's statement to the host inequality can be located in the source.

### 2.1 The functions

**Definition 2.1** (`Gchi`, DedekindLFunctions/CharFamily L15-19) [read].
$$G_\chi(y)=\begin{cases}\mathrm{ramp}_1(y)-y\log y+(1+\gamma)y, & \chi=1,\\ \mathrm{ramp}_\chi(y)+y\,\dfrac{L'}{L}(1,\chi), & \chi\ne1.\end{cases}$$
For $\chi=1$ at level 1 this is $G_z$ (Formalism/StatementOC L10-13).

**Lemma 2.2** (Mellin transforms; `poleData_char`, LandauTheorems/poleData L137-145) [read, statement] [checked: gz_mellin.py, gchi_mellin.py]. Let $\operatorname{Re}s>2$, so the integrals converge absolutely, since $|\mathrm{ramp}_\chi(y)|\le2y^2$ (`Gchi_growth`, GchiGrowth L37). Then
$$\int_1^\infty G_z(y)\,y^{-s-1}\,dy=\frac{-\zeta'/\zeta(s)}{s(s-1)}-\frac1{(s-1)^2}+\frac{1+\gamma}{s-1},$$
$$\int_1^\infty G_\chi(y)\,y^{-s-1}\,dy=-\frac{L'/L(s,\chi)-s\,L'/L(1,\chi)}{s(s-1)}\qquad(\chi\ne1).$$
Both right sides continue meromorphically to $\operatorname{Re}s>0$ and are regular at $s=1$. Their only poles in $\operatorname{Re}s>0$ are at the zeros $\rho$ of $L(\chi,\cdot)$. A zero of multiplicity $m$ gives a simple pole with residue
$$-\frac{m}{\rho(\rho-1)}.$$

*Derivation.* $\int_n^\infty(y/n-1)y^{-s-1}dy=n^{-s}/(s(s-1))$, $\int_1^\infty y\log y\cdot y^{-s-1}dy=1/(s-1)^2$, and $\int_1^\infty y\cdot y^{-s-1}dy=1/(s-1)$. At $s=1$, the expansion $-\zeta'/\zeta(s)=1/(s-1)-\gamma+O(s-1)$ cancels the double pole and the simple pole. This is why the constant is $1+\gamma$. In Lean the continuation is `poleData_abstract` (poleData L22) with $g(s)=(s-1)\zeta(s)$, or $g=L(\chi,\cdot)$, and $k=1$ [derived].

*Check.* gz_mellin.py agrees to 8 digits at $s=2$ and $s=3$. The value at $s=1$ is about 1.7648, and the residue at $\rho_1=1/2+14.13i$ is $0.004999$. The variants with constant $1$ in place of $1+\gamma$, with the opposite sign, and with residue $+1/(\rho(\rho-1))$ fail. gchi_mellin.py does the same for $\chi_4$, with $L'/L(1,\chi_4)=0.2456$.

**Remark 2.3** (sign of residues) [derived]. For a real zero $\beta\in(0,1)$, the residue is
$$-\frac{m}{\beta(\beta-1)}=\frac{m}{\beta(1-\beta)}>0 .$$
This positivity is what makes a one-sided bound on $G$ enough (Theorem 2.5, case (b)).

### 2.2 Families with positive weights

**Definition 2.4** (`CharFamily`, CharFamily L24-36) [read]. A family $F$ consists of:
- a finite index set;
- characters $\chi_i$ mod $N_i$, with $\chi_i\ne1$ unless $N_i=1$;
- weights $a_i>0$.

Its function is
$$\mathrm{Gm}_F(y)=\sum_i a_i\operatorname{Re}G_{\chi_i}(y).$$
Let $g(u)=\mathrm{Gm}_F(e^u)$ (`gm`, LandauZeroFreeCriterion L9). Let $Z$ be the set of $\rho$ with $\operatorname{Re}\rho>0$ such that some $L(\chi_i,\rho)=0$ or $L(\chi_i,\bar\rho)=0$ (`zeroSet`, L11-13).

**Proposition 2.4a** (`poleData`, poleData L248) [read, proof of the residue part, L340-400]. There is $\Phi$, holomorphic on $\{\operatorname{Re}s>0\}\setminus Z$, such that:
- $\Phi(s)=\int_0^\infty g(u)e^{-su}du$ for $\operatorname{Re}s>2$;
- $|g(u)|\le Ce^{2u}$;
- $Z$ is discrete;
- at each $\rho\in Z$, $\Phi$ has a simple pole with residue $c\ne0$, and $c$ is real and positive when $\rho$ is real.

This is the structure `PoleData` (LandauZeroFreeCriterion L15-23).

*Proof idea.* Since $\overline{G_\chi}=G_{\bar\chi}$ (`Gchi_conj`, GchiConj L38), we have $\operatorname{Re}G_\chi=\tfrac12(G_\chi+G_{\bar\chi})$. So
$$\Phi=\sum_i\tfrac{a_i}2(\Phi_{\chi_i}+\Phi_{\bar\chi_i}),$$
with each term given by Lemma 2.2. At $\rho\in Z$ the residue is $S\cdot(-1/(\rho(\rho-1)))$, where
$$S=\sum_i\tfrac{a_i}2(m_{1,i}+m_{2,i})>0$$
and $m_{1,i},m_{2,i}$ are the orders of vanishing of $L(\chi_i,\cdot)$ and $L(\bar\chi_i,\cdot)$ at $\rho$. Every $a_i$ is positive and at least one multiplicity is nonzero, so $S>0$. Remark 2.3 then gives the sign for real $\rho$. ∎

### 2.3 Landau's theorem, one-sided and on windows

**Theorem 2.5** (`lemmaL`, LandauTheorems/lemmaL L13-24, via `landau_window`, landauWindow L83) [read, proof]. Let $F$ be a family, $0<\theta<1$ and $\delta>0$. Suppose that for every $\eta>0$ and every $U_0$ there are $U\ge U_0$ and $R\ge0$ on $[U,(1+\delta)U]$ such that:
- $g\le R$ on $[U,(1+\delta)U]$;
- $\int_U^{(1+\delta)U}R(u)e^{-\theta u}\,du\le e^{\eta U}$.

This is `WindowHypU`, LandauZeroFreeCriterion L25. Then $L(\chi_i,s)\ne0$ for all $i$ and all $\operatorname{Re}s>\theta$.

Nothing is assumed about $g$ outside the windows except $|g(u)|\le Ce^{2u}$. Nothing is assumed about $-g$ anywhere.

*Proof.*
- **Region $\operatorname{Re}s\ge1$.** Mathlib gives $L(\chi,s)\ne0$ (`charFamily_LFunction_ne_zero_of_one_le_re`, L9).
- **Region $\operatorname{Re}s<1$.** Suppose $\rho_0\in Z$ with $\operatorname{Re}\rho_0>\theta$. For $\operatorname{Re}s>2$ write
  $$c_k(s)=\frac{(-1)^k\Phi^{(k)}(s)}{k!}=\int_0^\infty g(u)\frac{u^k}{k!}e^{-su}\,du\qquad(\texttt{landau\_coeff}).$$
- **Step 1: upper bound** (`landau_window_key`, L40-75) [read, proof]. There are $\sigma>2$ and $C$ with the following property. For every $\eta>0$ and $U_0$ there are $U\ge U_0$ and $k\ge U$ such that for all real $\gamma$,
  $$|c_k(\sigma+i\gamma)|+\operatorname{Re}c_k(\sigma)\le \frac{Ce^{\eta U}}{(\sigma-\theta)^k}.\tag{2.1}$$
  - The key is $|g|+g=2g^+\le 2R$ on the window. This gives
    $$|c_k(\sigma+i\gamma)|\le\int|g|\,K_k=\int(|g|+g)K_k-c_k(\sigma),$$
    with kernel $K_k(u)=u^ke^{-\sigma u}/k!$ (`landau_window_ineq`, landauWindowIneq L27).
  - On the window, $K_k(u)\le e^{-\theta u}(\sigma-\theta)^{-k}$, because $v^ke^{-v}/k!\le1$ (`landau_kernel_max`).
  - Off the window, the growth bound and a Chernoff estimate control the kernel's mass. The parameters are $l=2+6/\delta$, $M=l(1+\delta)$, $\sigma=M(2+l)$ and $k\approx(1+\delta/2)\sigma U$. The tail is at most $C/\sigma^k$ (`landau_tails`, landauTails L80).
- **Step 2: lower bound from the nearest pole.** The poles have $\operatorname{Re}\rho\le2<\sigma$ (`landau_pole_re_le`). The finitely many poles in the closed disc of radius $\sigma-\theta$ about $\sigma$ give two cases (`landau_dichotomy`, LandauDichotomy L24).
  - **(a) Complex case.** Choose $\gamma$ and a pole $\rho$ that is the unique pole in a disc of radius $r$ about $z=\sigma+i\gamma$, with $d=|z-\rho|<r$ (`landau_nearest`). The disc of radius $D\le\sigma-\theta$ about $\sigma$ contains no pole.
    - Subtracting the principal part gives $|c_k(z)|\ge|c|/d^{k+1}-M/e^k$ with $d<e$ (`landau_pole_asym`).
    - Cauchy's estimate in the pole-free disc gives $\operatorname{Re}c_k(\sigma)\ge-M'/e^k$ (`landau_cauchy`).
  - **(b) Real case.** The pole nearest $\sigma$ is real, $\beta>\theta$, and unique in its disc. Then $\operatorname{Re}c_k(\sigma)\ge\operatorname{Re}c/(\sigma-\beta)^{k+1}-M/e^k$. Proposition 2.4a gives $\operatorname{Re}c>0$, so this lower bound is large. Without positivity, a real pole could cancel between the two terms of (2.1).
- **Step 3: contradiction.** In both cases the lower bound $c'/d^{k}$ with $d<e\le\sigma-\theta$ beats the upper bound $(M+Ce^{\eta U})/e^k$ once $\eta<\tfrac12\log(e/d)$ and $U$ is large (`landau_window_contra`, `landau_growth_contra`). ∎

**Corollary 2.6** (`zeroFree_of_rpow_window`, ZeroFreeOfRpowWindow L11; `windowHyp_of_rpow`, WindowHypOfRpow L27) [read, proof]. Suppose $\mathrm{Gm}_F(y)\le Cy^\theta$ for all $y\in[Y,Y^{1+\delta}]$, for arbitrarily large $Y$. Then $L(\chi_i,s)\ne0$ for $\operatorname{Re}s>\theta$.

*Proof.* Take $R(u)=|C|e^{\theta u}$. Then $\int_U^{(1+\delta)U}Re^{-\theta u}du=|C|\delta U\le e^{\eta U}$ for large $U$. ∎

**Remark 2.7** [derived]. Theorem 2.5 is Landau's theorem on Dirichlet integrals with nonnegative coefficients, in a form that is one-sided, holds only on windows, and allows a polynomial loss. The positivity enters only through $a_i>0$ and the sign of $-1/(\beta(\beta-1))$. The Lean development contains a second, unwindowed version (`landau_family`, `zero_free_of_Chebyshev_growth`, Landau.lean L380, L538) that is not on the main path.


## 3. Levels and the window inequality

All declarations in this section are in Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ (files ExplicitFormulaErrorOfHostConditions, Window, TopDefs, TopWin) unless another path is given.

### 3.1 Levels

**Definition 3.1** (`Level`, ExplicitFormulaErrorOfHostConditions L8-38) [read]. A *level* $\Lambda$ consists of:
- a finite set $\mathrm{KEPT}$ of primitive characters that contains $1$ and is closed under inversion;
- an optional exceptional element $\psi_K\in\mathrm{KEPT}$, which is odd and real when present;
- a natural number $o$.

Write $\mathrm{Nt}=\mathrm{KEPT}\setminus\{1\}$ and set $\mathrm{wt}(\psi)=1$ if $\psi=\psi_K$, and $\mathrm{wt}(\psi)=(3o+1)^{-1}$ otherwise. The level's Chebyshev function is
$$\mathrm{Gm}_\Lambda(y)=G_z(y)+\sum_{\psi\in\mathrm{Nt}}\mathrm{wt}(\psi)\,\operatorname{Re}G_\psi(y).$$
$\Lambda$ is *zero-free above* $\theta$ if $L(\psi,s)\ne0$ for all $\psi\in\mathrm{KEPT}$ and $\operatorname{Re}s>\theta$.

**Definition 3.2** (`Level.cyc`, L121; `Level.ofSub`, L105) [read]. For a primitive $\psi$, the *cyclic level* $\mathrm{cyc}(\psi)$ has $\mathrm{KEPT}=\{\text{primitive characters inducing }\psi^k\}$, no exceptional element, and $o=\operatorname{ord}\psi$. So
$$\mathrm{Gm}_{\mathrm{cyc}(\psi)}=G_z+\frac{1}{3\operatorname{ord}\psi+1}\sum_{\psi^k\ne1}\operatorname{Re}G_{(\psi^k)^*}.$$
For $\psi=1$ this is $G_z$ itself.

### 3.2 From a bound on windows to a zero-free half-plane

A set $S\subset\mathbb R$ *has windows of ratio* $\lambda$ if for every $y$ there is $Y\ge y$ with $[Y,Y^\lambda]\subset S$ (`HasWindows`, Window L7) [read].

**Lemma 3.3** (`formB`, PrimitiveCosets/Imports L8-20; `level_family`, PrimitiveCosets/LevelFamily L41) [read, proof]. Let $\Lambda$ be a level, $\lambda>1$ and $0<\theta<1$. If $\{x:\mathrm{Gm}_\Lambda(x)\le x^\theta\}$ has windows of ratio $\lambda$, then $\Lambda$ is zero-free above $\theta$.

*Proof.* `level_family` builds a family $F$ in the sense of Definition 2.4 indexed by KEPT: the character $\psi$ gets weight $1$ if $\psi=1$ and $\mathrm{wt}(\psi)>0$ otherwise. The admissibility condition holds because a primitive $\psi$ with $\psi=1$ has conductor $1$. Then $\mathrm{Gm}_F=\mathrm{Gm}_\Lambda$, and $F$ is zero-free above $\theta$ exactly when $\Lambda$ is. Apply Corollary 2.6 with $\delta=\lambda-1$ and $C=1$. ∎

**Theorem 3.4** (window inequality implies RH; `level_of_tiedWin`, TopWin L68-81, and `zeroFreeOn_of_tiedWin_cyc`, TopWin L90-93) [read, proof]. Suppose that for every primitive $\psi$ the following *window inequality* WI($\psi$) holds:

> There are $c_0\ge0$ and $\varepsilon_1>0$ such that for every $\varepsilon\in(0,\varepsilon_1)$ there are a set $\mathrm{Win}_\varepsilon$ with windows of ratio $3/2$ and a number $x_1$ with
> $$\mathrm{Gm}_{\mathrm{cyc}(\psi)}(x)\le x^{1/2+c_0\varepsilon}\qquad\text{for all }x\in\mathrm{Win}_\varepsilon,\ x\ge x_1 .$$

Then ZeroFreeAll holds, and by Section 1 so does RH.

*Proof.* Fix $\psi$, write $\Lambda=\mathrm{cyc}(\psi)$, and let $\operatorname{Re}s>1/2$. Put $\mu=\min(\operatorname{Re}s-\tfrac12,\tfrac12)>0$.
- Choose $\varepsilon\in(0,\varepsilon_1)$ with $c_0\varepsilon\le\mu/2$ (`exists_small_eps`, TopWin L59). This is possible because $c_0$ does not depend on $\varepsilon$.
- For $x\in\mathrm{Win}_\varepsilon$ with $x\ge\max(x_1,1)$ we get $\mathrm{Gm}_\Lambda(x)\le x^{1/2+\mu/2}$. Discarding the part of $\mathrm{Win}_\varepsilon$ below $\max(x_1,1)$ keeps windows of ratio $3/2$ (`HasWindows.mono`, Window L10).
- Lemma 3.3 with $\theta=\tfrac12+\tfrac\mu2\in(0,1)$ shows $\Lambda$ is zero-free above $\theta$. Since $\theta<\operatorname{Re}s$ and $\psi\in\mathrm{KEPT}(\Lambda)$ (`Level.mem_cyc`, L124), $L(\psi,s)\ne0$. ∎

**Remark 3.5** [derived]. The only quantitative demand is that the exponent be $\tfrac12+c_0\varepsilon$ with $c_0$ fixed before $\varepsilon$. A bound $x^{1/2+\varepsilon}$ for one fixed $\varepsilon$ gives nothing below $\operatorname{Re}s=\tfrac12+\varepsilon$. The windows may be sparse, and the bound is needed only from above.

### 3.3 How the Lean splits the window inequality

In Lean, WI($\psi$) is the conjunction of two statements about a type of *families* $\mathrm{Fm}$ at scale $\varepsilon$ (`FamCore`, Formalism/SharpRestriction/FamCore L71) [read, statement]. A family carries a window set $\mathrm{Win}$ and, for each $x$, a nonempty index set of CM hosts $D(x,i)$ with their size data. The two statements are:
- `ChebyshevInequalityAtWindowScale` (TopWin L30-32): for small $\varepsilon$ there is a family whose window set has windows of ratio $3/2$, which satisfies the host conditions `EFamC` (TopDefs L15: EAtH with a constant $C$ for every host at every large $x$), and on whose windows a predicate `ChainTied` holds for large $x$.
- `ChebyshevInequalityOnWindows` (TopWin L26-28): for every family with EFamC on which ChainTied holds, $\mathrm{Gm}_\Lambda(x)\le x^{1/2+(e_D+e_L+7)\varepsilon}$ on its windows for large $x$.

`zeroFreeAll_of_topG` (CharacterBoxes/ZeroFreeAllOfTopG L26-34) [read, proof] supplies them, for $\lambda=3/2$, as follows:
1. **Per-host inequality.** ChebyshevInequalityOnWindows is `level_gm_le_on_family_scales` (PrimitiveCosets/LevelGmLeOnFamilyScales L28) = `windowInequality_of_artinInputs` (WindowInequalityOfArtinInputs L17-25). It turns ChainTied at $x$ into CoreAtH for one host (`tiedCore_of_chainTied`, L13) and then applies `core_gm` (Theorem 4.9 below).
2. **Existence of families.** ChebyshevInequalityAtWindowScale comes from the hypothesis `TopG` (ZeroFreeAllOfTopG L12-14) applied to the requirement `GChi ψ` (CharacterBoxes/Supply L42). This requirement asks each host to satisfy EAtH for $\mathrm{cyc}(\psi)$ with $C=4$, and a Galois-cohomological bound `VVle` (CharacterBoxes/ExistsPageN L12-16) on $\sum_\ell\log\ell\sum_e\operatorname{len}Ш^e$ of the host field. Hosts meeting the requirement on windows of ratio $3/2$ are supplied by `supplyChi` (CharacterBoxes/SupplyChi L8) from `VWin` (ExistsPageN L49).
3. **Where the hypotheses are discharged** [read, call level]. TopG is supplied in TopPlug L14 by `forall_goal_of_shape_of_hyps` from the Green and HypsAlt hypotheses. VWin is supplied in MainConclusion L8 by `vwin_of_row` (VwinOfRow L4) from the Galois-representation statement `galoisLocalGlobalStrong_recParameter` (RowSrc L6). They are not treated in this paper (§4.6).

## 4. The CM host and the per-host inequality

Declarations about frames and hosts are in Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/; those about $\mathrm{ASK}$ are in Formalism/SizeWindowBrackets/FirstPrimeNeSecondPrime (cited as FPNSP); those about the core bound are in Development/AutomorphicArithmetic/DedekindLFunctions/ (SplitInertia, LandauTheorems/ChCore, LandauTheorems/ChBalance) and Development/AutomorphicArithmetic/PrimitiveCosets/.

### 4.1 Frames and hosts

**Definition 4.1** (`Frame`, ZsmulGeneratorEqZeroOfProjection L15-122) [read]. A *frame* $\varphi$ consists of:
- an integer $e\ge2$ and the group $H_e=(\mathbb Z/2^{e+2})^\times/\{\pm1\}$;
- a finite abelian group $A$ of order $\mathrm{ord}$, with a surjection $h:A\to H_e$;
- an element $a_0\in A$ on whose cyclic group $A_0=\langle a_0\rangle$ the map $h$ is injective.

Write $o=[A:A_0]$ (`Frame.o`, L70) and $G_\varphi=\{\pm1\}^2\times A$. The named elements of $G_\varphi$ are $cc=((-1,-1),0)$, $iod=((1,-1),0)$ and $\tau_1(t)=((1,1),t)$. The two sign projections are $\mathrm{chQ}(g)=g_{1,1}$ and $\mathrm{chD}(g)=g_{1,2}$.

**Definition 4.2** (`HostRaw`, ConjEMemHostFIff L12-46; `HostAx`, L174; `HostHyp`, Formalism/FrobeniusOrbits/Statement L13) [read]. A *host* over $\varphi$ consists of:
- primes $q\equiv3\pmod 8$ and $d\equiv7\pmod{16}$ with $\left(\frac{-d}{q}\right)=1$;
- a modulus $Q_S$ with $2^{e+2}\mid Q_S$, $\gcd(Q_S,qd)=1$, and $\left(\frac{-d}{l}\right)=1$ for every odd prime $l\mid Q_S$;
- a Galois number field $E$ with $\mathrm{Gal}(E/\mathbb Q)\cong G_\varphi$, containing $\sqrt{-d}$, with $\sigma(\sqrt{-d})=\mathrm{chD}(\sigma)\sqrt{-d}$;
- an embedding $E\hookrightarrow\mathbb Q(\zeta_N)$ with $N=Q_Sqd$, and a homomorphism $\mathrm{art}:(\mathbb Z/N)^\times\to G_\varphi$ such that $\mathrm{art}(u)$ acts on $E$ as $\zeta_N\mapsto\zeta_N^u$ acts on $\mathbb Q(\zeta_N)$ (`art_spec`), with $\mathrm{art}(-1)=cc$ and three congruence conditions (`art_h`, `art_d`, `art_q`).

`HostAx` adds `HostDer` (L87): $\mathrm{art}$ is surjective, $E$ is a CM field whose complex conjugation is $cc$, $[E:\mathbb Q]=4\,\mathrm{ord}$, and $E$ carries a CM type.

So a host is an abelian CM field $E\subset\mathbb Q(\zeta_N)$ of degree $4\,\mathrm{ord}$ that contains $K=\mathbb Q(\sqrt{-d})$, together with its Artin map from cyclotomic reciprocity [derived].

### 4.2 Arithmetic data of a host

Write $\mathbb G=E_0\times A$ additively, with $E_0=(\mathbb Z/2)^2$. The map `toE` (PrimitiveCosets/RecH L10) identifies $G_\varphi$ with $\mathbb G$ by $((s_1,s_2),t)\mapsto((\operatorname{sgn}s_2,\operatorname{sgn}s_1),t)$. Let $\Phi=\{g\in\mathbb G:g_{1,1}=0\}$ (`PhiSet`, Formalism/ThickAverageLoss/PartnersToFactorsAt L32). Then $g\in\Phi$ exactly when $\mathrm{chD}=1$, that is, when $g$ fixes $\sqrt{-d}$. So $\Phi=\mathrm{Gal}(E/K)$ and $|\Phi|=|\mathbb G|/2$ [derived].

For $t\in A$, $\Phi$ contains exactly two elements with $A$-coordinate $t$:
$$\mathrm{topPl}(t)=((0,0),t),\qquad \mathrm{thickPl}(t)=((0,1),t)\qquad(\text{PartnersToFactorsAt L26-27})\ [\text{read}].$$
Under toE, $\mathrm{thickPl}(t)$ is the image of the element with sign pair $(s_1,s_2)=(-1,1)$, which is $cc\cdot iod$, times the element of $A$ that toE sends to $t$. So $\mathrm{thickPl}(t)=\mathrm{cconj}+\mathrm{sgc0}+(0,t)$ with $\mathrm{cconj}=((1,1),0)$ and $\mathrm{sgc0}=((1,0),0)$ [derived]. A *thick place* of a weight $w:\Phi\to\mathbb R$ is a point $\mathrm{thickPl}(s+u_0)$ with $s\in T_2$. SizesA (Definition 4.11) asks $w$ to be close to $b$ there.

**Definition 4.3** (`ArithData`, FPNSP L38-42; `cftData`, Formalism/SizeWindowBrackets/GaloisToProductIsIso L25-32; `arith`, RecH L23) [read]. The arithmetic data of a host are $q$, $d$ and, for each prime $p$:
- the inertia group $I_p=r(\ker((\mathbb Z/N)^\times\to(\mathbb Z/N_p')^\times))$, where $N_p'$ is the prime-to-$p$ part of $N$ and $r=\mathrm{toE}\circ\mathrm{art}$;
- the Frobenius $\mathrm{frob}_p=r(u_p)$, where $u_p\equiv p\pmod{N_p'}$ and $u_p\equiv1$ modulo the $p$-part of $N$.

`hostFactsS` (PrimitiveCosets/hostFactsS L44) proves `HostFactsS` (SplitInertia L14-22) for these data with $S$ the set of primes dividing $Q_Sq$ [read, statement]:
- $I_p=0$ for $p\notin S\cup\{d\}$;
- for $p\in S$, both $I_p$ and $\mathrm{frob}_p$ lie in $\Phi$;
- $I_d=\{0,\mathrm{sgc0}\}$ with $\mathrm{sgc0}=((1,0),0)=\mathrm{toE}(iod)$.

A prime $p\notin S\cup\{d\}$ is *inert* if $\mathrm{frob}_p\notin\Phi$ (`IsInert`, FPNSP L72), which is to say $p$ is inert in $K$ [derived].

**Definition 4.4** (`primVal`, `GPsi`, FPNSP L65-70) [read]. For an additive character $\psi$ of $\mathbb G$,
$$\mathrm{primVal}(\psi,n)=\prod_{p\mid n}\frac1{|I_p|}\sum_{x\in I_p}\psi\big(v_p(n)\,\mathrm{frob}_p+x\big),$$
and, for a function $\ell$ on characters,
$$G_\Psi(\psi,y)=\begin{cases}G_z(y),&\psi=0,\\ \sum_{n\le y}\Lambda(n)\,\mathrm{primVal}(\psi,n)\,(y/n-1)+y\,\ell(\psi),&\psi\ne0.\end{cases}$$

**Lemma 4.5** (`prim_read`, PrimitiveCosets/PrimRead L48) [read, statement]. Suppose $\ell(\psi)=\frac{L'}{L}(1,\chi)$ whenever $\chi$ is a primitive character whose values are $\mathrm{primVal}(\psi,\cdot)$ (`HostAddCharCompatible`, CoreAtH L18). Then for every $\psi\ne0$ there is a primitive Dirichlet character $\chi_\psi^*$, namely the primitive character inducing $\psi\circ r$ (`HostRaw.prim`, Analytic L108), with
$$\ell(\psi)=\frac{L'}{L}(1,\chi_\psi^*),\qquad G_\Psi(\psi,y)=G_{\chi_\psi^*}(y)\ \text{ for all }y.$$
So $G_\Psi$ is the function $G_\chi$ of Definition 2.1. Averaging over $I_p$ in primVal is what turns $\psi\circ r$, a character mod $N$, into its primitive version [derived].

### 4.3 The inert prime sum and the balance identity

Fix $t\in A$, a scale $a>0$, and weights $w:\Phi\to(0,\infty)$. The *partner* of $g\notin\Phi$ is $\pi_t(g)=cc+g+(0,t)\in\Phi$; the map $\pi_t$ is a bijection from $\mathbb G\setminus\Phi$ onto $\Phi$ (`PartnerBij`, FPNSP L127). Write $w_g=w(\pi_t(g))$.

**Definition 4.6** (`ASK`, `MAIN`, `De`, FPNSP L75-96) [read]. With $N$ a cutoff,
$$\mathrm{ASK}=\sum_{\substack{p\le N\\ p\text{ inert}}}2\log p\sum_{\substack{i\le N\\ i\,\mathrm{frob}_p\notin\Phi}}\Big(\frac a{p^i}-w_{i\,\mathrm{frob}_p}\Big)^+\;+\;\log d\sum_{i\le N}\ \sum_{\substack{g\in i\,\mathrm{frob}_d+I_d\\ g\notin\Phi}}\Big(\frac a{d^i}-w_g\Big)^+,$$
$$\mathrm{MAIN}=a\Big(\log a-1-\gamma+\ell(\mathrm{chC})-\frac1{|\Phi|}\sum_{\rho\in\Phi}\log w(\rho)\Big),$$
$$\mathrm{De}=\frac1{|\Phi|}\sum_{g\notin\Phi}\ \sum_{\psi\in\widehat{\mathbb G}}\overline{\psi(g)}\;w_g\,G_\Psi\big(\psi,a/w_g\big).$$
Here $\mathrm{chC}$ is the character $g\mapsto(-1)^{g_{1,1}}$, which is $1$ on $\Phi$ and $-1$ off it (FPNSP L21). For an inert $p$ the condition $i\,\mathrm{frob}_p\notin\Phi$ means $i$ is odd, so ASK runs over the prime powers whose Frobenius lies off $\Phi$, each weighted by a ramp at scale $a/w_g$ [derived].

**Theorem 4.7** (balance identity; `ch_balance`, LandauTheorems/ChBalance L200-202; same statement as `AskMainBalance`, FPNSP L98-101, proved as `colour_balance`, Formalism/SizeWindowBrackets/ChainSlopeWindows/StronglyIrreducible L695) [read, statement; proof idea derived] [checked: colour_balance.py]. Assume HostFactsS, $a>0$, $w>0$ on $\Phi$, and $a/w(\rho)\le N$ for $\rho\in\Phi$. Then
$$\mathrm{ASK}-\mathrm{MAIN}=\mathrm{De}.$$

*Proof.*
- Orthogonality on $\mathbb G$, with $|\mathbb G|=2|\Phi|$, gives
  $$\frac1{|\Phi|}\sum_\psi\overline{\psi(g)}\,\mathrm{primVal}(\psi,p^i)=\begin{cases}2\cdot[\,i\,\mathrm{frob}_p=g\,],&p\text{ unramified},\\ \dfrac{2}{|I_p|}[\,g-i\,\mathrm{frob}_p\in I_p\,],&\text{in general}\end{cases}$$
  (`OrthoUnram`, `OrthoRam`, FPNSP L110-121). Primes in $S$ have Frobenius and inertia in $\Phi$, so they never meet $g\notin\Phi$. The prime $d$ has $|I_d|=2$, which removes the factor 2. Hence
  $$\mathrm{ASK}=\frac1{|\Phi|}\sum_{g\notin\Phi}\sum_\psi\overline{\psi(g)}\sum_{n\le N}\Lambda(n)\,\mathrm{primVal}(\psi,n)\Big(\frac an-w_g\Big)^+\qquad(\texttt{AskExpansion},\ \text{L133}).$$
- Since $(a/n-w_g)^+=w_g\,(y_g/n-1)^+$ with $y_g=a/w_g\le N$, the inner sum is $w_g\,\mathrm{ramp}_\psi(y_g)$. By Definition 4.4, $\mathrm{ramp}_\psi(y)=G_\Psi(\psi,y)-y\,\ell(\psi)$ for $\psi\ne0$, and $\mathrm{ramp}_0(y)=G_z(y)+y\log y-(1+\gamma)y$.
- The leftover terms are $\frac1{|\Phi|}\sum_{g\notin\Phi}\big(a\log(a/w_g)-(1+\gamma)a\big)$ and $-\frac a{|\Phi|}\sum_{\psi\ne0}\ell(\psi)\sum_{g\notin\Phi}\overline{\psi(g)}$. The colour sum $\sum_{g\notin\Phi}\overline{\psi(g)}$ is $|\Phi|$ for $\psi=0$, $-|\Phi|$ for $\psi=\mathrm{chC}$, and $0$ otherwise (`ColourSum`, L123). The partner bijection turns the mean of $\log w_g$ over $g\notin\Phi$ into the mean of $\log w$ over $\Phi$. The leftover is exactly MAIN. ∎

*Check.* colour_balance.py builds toy data with $H=\mathbb Z/3$ and six random trials with $a\in[200,600]$. Its pass criterion is $|\mathrm{ASK}-\mathrm{MAIN}-\mathrm{De}|<10^{-6}a$. The recorded run (`colour_balance.out`) gave residuals of at most $5.1\cdot10^{-13}$. That value is a property of one run in double precision, not a portable bound; the reviewer's rerun gave about $1.1\cdot10^{-12}$. Three wrong variants fail by 390 to 2200: weight $\log p$ in place of $2\log p$, MAIN without $\ell(\mathrm{chC})$, and the bare ramp at $\psi=0$. The identity also holds with random Frobenius values that satisfy only HostFacts, and De does not depend on $\ell(\psi)$ for $\psi\notin\{0,\mathrm{chC}\}$. So the identity uses orthogonality and the shape of ramification, and no reciprocity.

**Remark 4.8** [derived]. Theorem 4.7 is exact. It moves the problem from $\mathrm{Gm}$ to a one-sided bound
$$\mathrm{ASK}\le\mathrm{MAIN}+\mathrm{Err},$$
in which ASK is a sum over inert prime powers of the host field. That bound is not proved here (§4.6, first row).

### 4.4 The per-host inequality

**Theorem 4.9** (`core_gm`, PrimitiveCosets/CoreGm L12-74) [read, proof; `ch_top` in step 2 at statement level]. Let $\Lambda$ be a level and $e_D,e_L,K,c_{HH},e_K,C,\varepsilon>0$. There is $x_1$ such that the following holds for every $x\ge x_1$, every host $H$ over a frame $\varphi$, and every finite $T\subset A$. If $\mathrm{EAtH}(\Lambda,H,T,x,\varepsilon,C)$ and $\mathrm{CoreAtH}(H,T,e_D,e_L,K,c_{HH},e_K,\varepsilon,x)$ hold, then
$$\mathrm{Gm}_\Lambda(x)\le x^{1/2+(e_D+e_L+7)\varepsilon}.$$

The two hypotheses are as follows.

**Definition 4.10** (`EAtH`, ExplicitFormulaErrorOfHostConditions L144-151; the sets are in Analytic L84-159) [read]. Characters $\theta$ of $G_\varphi$ that are trivial on $\tau_1(A_0)$ split by the sign $\theta(iod)=\pm1$ into $X^+$ and $X^-$. The character $\theta$ is *kept* if its primitive Dirichlet character $(\theta\circ\mathrm{art})^*$ lies in KEPT, and *bounded* if it is in $X^-$, or in $X^+$ and not kept. EAtH$(\Lambda,H,T,x,\varepsilon,C)$ says:
- `o_eq`: $o(\varphi)=o(\Lambda)$;
- `kept`: every element of KEPT is $(\theta\circ\mathrm{art})^*$ for some $\theta\in X^+$;
- `ps`: the exceptional character, if present, comes from $\mathrm{psC}=\mathrm{chQ}$; if absent, psC is not kept;
- `shares`: for every $\gamma\in A$, $\big|\#\{t\in T:t-\gamma\in A_0\}-\lambda(\gamma)|T|\big|\le x^{-1+\varepsilon}|T|$, where $\lambda(\gamma)=4/(3o+1)$ if $\gamma\in A_0$ and $3/(3o+1)$ otherwise;
- `bdG`: $|G_{\chi}(x)|\le x^{1/2+\varepsilon}$ for the primitive character $\chi$ of every bounded $\theta$;
- `bdL`: $|L'/L(1,\chi)|\le C\log x$ for the same characters.

**Remark 4.10a** (where the weight $(3o+1)^{-1}$ comes from) [derived]. Let $\psi$ be a character of $A$ trivial on $A_0$. Summing `shares` over the $o$ cosets of $A_0$ gives
$$\sum_{t\in T}\psi(t)=|T|\sum_{\gamma\in A/A_0}\lambda(\gamma)\psi(\gamma)+O(o\,x^{-1+\varepsilon}|T|)=\begin{cases}|T|\,\dfrac{4+3(o-1)}{3o+1}=|T|,&\psi=1,\\[2mm] |T|\,\dfrac{4-3}{3o+1}=\dfrac{|T|}{3o+1},&\psi\ne1,\end{cases}$$
up to that error. So the set $T$ of twists sees each nontrivial kept character with weight exactly $(3o+1)^{-1}$, which is $\mathrm{wt}(\psi)$ in Definition 3.1. The same computation is `tops_sum` with `shares` inside `charsA` (PrimitiveCosets/charsA L80).

**Definition 4.11** (`CoreAtH`, PrimitiveCosets/CoreAtH L29-41) [read]. CoreAtH asserts that there exist a size record $D$ (the `Data` structure, with fields $x,\varepsilon,a,b,b',k,n_T,B_0,N_c,\dots$), constants $C$ with $C.e_{Div}\le e_D$, $C.e_{Loss}\le e_L$, $C.c_{HH}\le c_{HH}$, a function $\ell$ compatible with the host (Lemma 4.5), a cutoff $N$, a set $T_2\subset A_0$, scales $a:A\to\mathbb R$, weights $w_{u_0,j}:\Phi\to\mathbb R$ for $u_0\in A$ and $j<m$, and reals $\eta,X',\theta$, such that:
- `IdentU` (SplitInertia L67-72): the record's prime sum is the host's, $D.\mathrm{ASK}(u)=\sum_{t\in T}\sum_{j<m}\mathrm{ASK}(a_t,t,w_{\mathrm{tr}(u),j})$, and $D.\gamma=\gamma$, $D.\mathrm{LpL}=\operatorname{Re}\ell(\mathrm{chC})$;
- `SizeData₂`, `ErrWindows`, `BNBoundsU`: the hypotheses of the mean bound `ch_top` and its size ranges (summarised below; the source ledger is in Appendix A);
- `SizesA` (SplitInertia L42): $|a_t/b-x|\le1$; $w>0$ on $\Phi$; $b\le w\le b+\eta+1$ at the thick places $\mathrm{thickPl}(s+u_0)$, $s\in T_2$; $w\le 2b'$ at the other places of $\Phi$; $b'X'\le xb$; $a_t/w\le N$;
- `ThinScales` (GrowthBoundGivesRiemannHypothesis L55): $|G_\Psi(\psi,y)|\le\theta y$ for all $\psi$ and $y\ge X'/3$;
- `CostWindows` (SChain L50): $2|\Phi|(x+1)\theta\le1/x$ and $6|\Phi|(x+1)(\eta+1)\le b/x$;
- `RestSize` (SChain L53): $a_E\le2xb$, $|T|\ge x^{-\varepsilon/8}|A|/2$, $|T_2|/|A|\ge x^{-\varepsilon}$, $m\ge x^{1/2-\varepsilon}$, $k\le|A|^2x^{1/2-\varepsilon}$.

*Summary of SizeData₂, ErrWindows and BNBoundsU* [read, statements; MeanBoundSecondForm L111-163, ErrorFormsWeakWindowsFalse L16-52, SplitInertia L74-77]. For each $u_0\in A$ the record attaches a finite set $W(u_0)$ of *words* $u$. To each word it attaches real numbers: a degree $\mu_{CC}$, a height $h(u)$, a count $T(u)$, and slopes $\mu_M,\mu_N$ (with maxima $\mu^{\max}_M,\mu^{\max}_N$). In the source these are invariants of hermitian lattices attached to the word; this paper uses only the inequalities. Constants $c_\bullet\le K$ come with the record. SizeData₂ consists of eleven inequalities for every word. The three that carry the main term are:
- DIV, an upper bound $\mu_{CC}+h(u)-\mathrm{Fo}\le\sum_t[m(\mathrm{ph}(a_t)-a_t\log\Omega)-a_t\log T(u)]+E_{\rm Div}$;
- Count5, a lower bound $\log T(u)\ge\sum_j\frac1f\sum_\rho\log\frac{w_{j\rho}v}\pi+m\ell_g-c(L_a+m^2L_a/k)$;
- SlopeIneq, a lower bound $s-\log|W(u_0)|-\Phi\le\mu_{CC}$ for the slope of the whole lattice, where $\Phi$ is a loss of size $(\eta+4\sqrt e)\mathrm{HH}$ plus a logarithmic term.

The other eight (HidaSetting, EComp5, HComp, Slopes, QuotientSlopeBoundsWith, LossBounds, HHBound, FParams) are positivity conditions, comparisons between words, and error bounds of the types $n_TaL_a$, $mB_0$ and $\mathrm{LoP}=c\,n_Tmb\,x^{e\varepsilon}$. ErrWindows fixes the ranges: $x\ge1$, $0<\varepsilon\le1$, $1\le b$, $xb\le a$, $n_T\ge1$; the $m$-window $m\le x^{1/2+\varepsilon/2}$ and $xm\le k\le\min(a,x^{e_K})$; $0\le L,L_a\le2x^\varepsilon$; $\log|W(u_0)|\le(k-3)\log2$; and $(\bar\eta+4\sqrt{\bar e})x^{c_{HH}}b\le Kx^\varepsilon n_Ta$. BNBoundsU fixes the two error sizes $B_0\le2nmbx^\varepsilon$ and $N_c\le n_{T2}kbx^\varepsilon/(n^2x^{-\varepsilon})$, with $n=|A|$. Under these hypotheses `ch_top` gives $\mathrm{gapA}(u)\le x^{C_{\rm Err}\varepsilon}\mathrm{Br}$. That deduction is the subject of a sequel in preparation.

ThinScales asks for an exponentially small $\theta$ at the very large scales $y\ge X'/3$. The matching host statement is `ChebyshevCharacterBound` (Analytic L145-147): $|G_\chi(y)|\le y\,e^{-c x^{\varepsilon/8}}$ for every character $\chi$ of the host and $y\ge e^{x^{\varepsilon/3}}/3$ [read, statement]. `ThinH` (CharacterBoxes/PairGood L36-40) states it for hosts with $\log N\le2x^{\varepsilon/5}\log^2x$ and no real zero above $1-1/400$ for the real characters ramified at $q$ or $d$ (`RealBox`, L32). This is the prime number theorem in the classical zero-free region: with $\log y\ge x^{\varepsilon/3}$ and $\log N\approx x^{\varepsilon/5}$, the classical error is far below $y\,e^{-cx^{\varepsilon/8}}$ [derived]. We have not traced how CoreAtH's ThinScales is obtained from ThinH.

**Proof of Theorem 4.9** [read, proof]. Write $C'=e_D+e_L+3$ and $o=o(\Lambda)$.
1. Unpack CoreAtH. The record satisfies $D.x=x$ and $D.\varepsilon=\varepsilon$. ErrWindows supplies $m\le x^{1/2+\varepsilon/2}$ and $xm\le k$ (CoreGm L35-37).
2. For every $u\in A_0$, `ch_top` (LandauTheorems/ChTop L37) gives $\mathrm{gapA}(u)\le x^{C_{Err}\varepsilon}\cdot\mathrm{Br}$, where Br is the bracket of Proposition 4.13 below. Its inputs are IdentU, SizeData₂, ErrWindows and BNBoundsU. Since $C_{Err}\le C'$, this is at most $x^{C'\varepsilon}\mathrm{Br}$ (CoreGm L51-60). This is the only place where the unproved gapA bound enters.
3. Apply Proposition 4.12 with $C'$, $c=(3o+1)^{-1}$, $M=4o$, $K_o=\mathrm{koOf}\,\Lambda$, kept set $K_p=\mathrm{keptA}$, data $D=\mathrm{arith}\,H$ and $S$ from `hostFactsS`. CharsA is `charsA` (PrimitiveCosets/charsA L80), which uses EAtH. The result is $\mathrm{GmA}\le x^{1/2+(C'+3)\varepsilon}+\mathrm{SigA}$.
4. $\mathrm{GmA}=\mathrm{Gm}_\Lambda(x)$ exactly, by `gmA_eq` (GmAEq L61-149) [read, proof]. The map $\psi\mapsto(\psi\circ r)^*$ sends the kept host characters $K_p$ injectively onto KEPT (EAtH.kept and injectivity of `prim`, L79-93). A character trivial on $(0,A)$ is, through `chr`, either $1$ or $\mathrm{psC}$, because it is also trivial on $iod$ (L16-59). So it maps to $1$ or to the exceptional $\psi_K$, both of weight 1 (EAtH.ps). Every other kept character has weight $(3o+1)^{-1}=\mathrm{wt}$. Lemma 4.5 identifies the functions, and the sum is reindexed with no error term. $\mathrm{SigA}\le4o\,x^{1/2+\varepsilon}$ by `sigA_le` (SigALe L38), which applies `bdG` to the at most $4o$ non-kept characters in $\Psi_A$ ($|\Psi_A|=4o$, `card_PsiA`, CardPsiA L60).
5. For $x\ge x_3$ we have $x^\varepsilon\ge1+4o$. So
$$\mathrm{Gm}_\Lambda(x)\le(1+4o)\,x^{1/2+(C'+3)\varepsilon}\le x^{1/2+(C'+4)\varepsilon}=x^{1/2+(e_D+e_L+7)\varepsilon}.\qquad\square$$

*Status of Theorem 4.9.* Step 2 of the proof invokes `ch_top`, which deduces the gapA bound from SizeData₂, ErrWindows and BNBoundsU. Those hypotheses are part of CoreAtH, so they are assumptions of Theorem 4.9. The deduction itself is not proved in this paper. It is cited at statement level and is the subject of a sequel (§4.6, first row). So the proof of Theorem 4.9 given here is complete only modulo `ch_top`. The step that is self-contained is Proposition 4.12. It takes the gapA bound as an explicit hypothesis and uses nothing from outside this paper except the statement-level lemmas named in its label.

**Proposition 4.12** (`ch_core`, LandauTheorems/ChCore L343-441) [read, proof; `one_char`, DerivInt and LipW at statement level]. This is a self-contained conditional implication. Let $C\ge0$, $\varepsilon>0$, $|c|\le1$, and $M,K_o,C_E$ real. There is $x_1$ such that for $x\ge x_1$ the following holds. Suppose HostFactsS$(D,S)$; $b>0$, $a_E\ge0$, $k>0$; $m\le x^{1/2+\varepsilon/2}$ and $xm\le k$; SizesA, ThinScales, CostWindows and RestSize; $T_2\subset A_0$; and CharsA$(\ell,A_0,K_p,T,c,M,K_o,C_E,\varepsilon,x)$. CharsA (SplitInertia L56-62) says: $0\in K_p$; each $\psi\in K_p$ is trivial on $(0,A_0)$ and on sgc0; $|\Psi_A|\le M$; for $\psi\in K_p$ nontrivial on $(0,A)$, $\big|\sum_{t\in T}\psi(0,t)-c|T|\big|\le Mx^{-1+\varepsilon}|T|$; $|\ell(\psi)|\le K_o$ on $K_p\setminus\{0\}$; and $|\ell(\psi)|\le C_E\log x$ on $\Psi_A\setminus K_p$. If moreover $\mathrm{gapA}(u)\le x^{C\varepsilon}\mathrm{Br}$ for all $u\in A_0$, then
$$\mathrm{GmA}(x)\le x^{1/2+(C+3)\varepsilon}+\mathrm{SigA}(x).$$
Here $\Psi_A$ is the set of characters of $\mathbb G$ trivial on $(0,A_0)$, $\mathrm{GmA}=\sum_{\psi\in K_p}\mathrm{wt}(\psi)\operatorname{Re}G_\Psi(\psi,x)$ with $\mathrm{wt}=1$ on characters trivial on $(0,A)$ and $c$ otherwise, and $\mathrm{SigA}=\sum_{\psi\in\Psi_A\setminus K_p}|G_\Psi(\psi,x)|$ (SplitInertia L26-40). Also $\mathrm{gapA}(u_0)=\sum_{t\in T}\sum_{j<m}\big(\mathrm{ASK}(a_t,t,w_{u_0,j})-\operatorname{Re}\mathrm{MAIN}(a_t,w_{u_0,j})\big)$ (L50).

*Proof* [read, proof]. Put $s=x^{1/4}$, $e=x^\varepsilon$, $R=A_1\,se$ with $A_1=5+C_d+|K_o|+|M|(4+C_d+|K_o|)+4|C_E|$, where $C_d$ is the constant of `derivative_integral_all` (LipschitzWeightAndMinimum L966). Take $x_1$ so that $x\ge3$, $x^{3\varepsilon/8}\ge26$ and $s\ge|M|A_1$.

*Step 1: two classical bounds on $G_\Psi$* (`DerivInt`, GrowthBound… L62-65, proved for every ArithData by `derivative_integral_all`) [read, statement]. For $\psi\ne0$ and $y,z\ge1$,
$$|G_\Psi(\psi,y)-G_\Psi(\psi,z)|\le|y-z|\,\big(\log\max(y,z)+C_d+|\ell(\psi)|\big),$$
and $|G_z(y)-G_z(z)|\le C_d|y-z|$. Taking $z=1$, where $G_\Psi(\psi,1)=\ell(\psi)$, gives $|G_\Psi(\psi,x)|\le x(\log x+C_d+|\ell(\psi)|)$ (`triv`, ChCore L167). Taking $|y-x|\le1$ gives $|G_\Psi(\psi,y)-G_\Psi(\psi,x)|\le\log(x+1)+C_d+|\ell(\psi)|$ (`move`, L154). Both follow from $\frac{d}{dy}G_\Psi(\psi,y)=\sum_{n\le y}\Lambda(n)\mathrm{primVal}(\psi,n)/n+\ell(\psi)$ and Mertens [derived].

*Step 2: one character at a time* (`one_char`, L202). Let $y_t=a_t/b$, so $|y_t-x|\le1$ by SizesA. Define $v(\psi)=\mathrm{wt}(\psi)\operatorname{Re}G_\Psi(\psi,x)$ for $\psi\in K_p$ and $v(\psi)=-|G_\Psi(\psi,x)|$ otherwise. Then for every $\psi\in\Psi_A$,
$$|T|\,(v(\psi)-R)\le\sum_{t\in T}\operatorname{Re}\big(\psi(e_1t)\,G_\Psi(\psi,y_t)\big),\qquad e_1t=((1,0),t).$$
For $\psi\in K_p$ we have $\psi(e_1t)=\psi(\mathrm{sgc0})\psi(0,t)=\psi(0,t)$. Replace $G_\Psi(\psi,y_t)$ by $G_\Psi(\psi,x)$ at cost `move`. Then replace $\sum_t\psi(0,t)$ by $c|T|$ (or by $|T|$ when $\psi$ is trivial on $(0,A)$) at cost $Mx^{-1+\varepsilon}|T|\cdot$`triv` $\le M e(\log x+C_d+K_o)|T|$. For $\psi\notin K_p$, bound the real part below by $-|G_\Psi(\psi,x)|-$`move`, with $|\ell(\psi)|\le C_E\log x$. Every cost is at most $R$, since $\log(x+1)\le5s$ and $\log x\le4s$ (inequalities r1-r3, L401-419).

*Step 3: sum over $\Psi_A$* (L425-436). By `sum_vv` (L188), $\sum_{\psi\in\Psi_A}v(\psi)=\mathrm{GmA}-\mathrm{SigA}=:G$. Since $|\Psi_A|R\le|M|A_1se\le s^2e=x^{1/2+\varepsilon}$,
$$|T|\,\big(G-4x^{1/2+\varepsilon}\big)\le\sum_{t\in T}\operatorname{Re}\sum_{\psi\in\Psi_A}\psi(e_1t)\,G_\Psi(\psi,y_t).\tag{4.1}$$
(The constant 4 is slack; 1 suffices.)

*Step 4: the thick part of the balance identity* (`core`, L283-339). For $u_0\in A$ and $t\in T$ let
$$\mathrm{Th}(u_0,t)=\frac1{|\Phi|}\sum_{s\in T_2}\sum_\psi\psi\big(-e_1(s+u_0-t)\big)\,b\,G_\Psi(\psi,a_t/b)\qquad(\text{L20}).$$
This is De from Definition 4.6 with $w$ replaced by $b$ and the sum cut down to the thick places $\mathrm{thickPl}(s+u_0)$, $s\in T_2$. Lemma `th_le` (L75-150) gives
$$\operatorname{Re}\mathrm{Th}(u_0,t)\le\operatorname{Re}\mathrm{De}(a_t,t,w)+2|\Phi|\big(3(x+1)(\eta+1)+(x+1)b\theta\big)$$
for each weight $w=w_{u_0,j}$. At a thick place, $b\le w\le b+\eta+1$, and `LipW` (L58, proved as `lipschitz_weight_all`, LipschitzWeightAndMinimum L957) gives $|wG_\Psi(A/w)-bG_\Psi(A/b)|\le3(A/b)(w-b)\le3(x+1)(\eta+1)$. At a thin place, $w\le2b'$ and $b'X'\le xb$, so $A/w\ge X'/3$. ThinScales then gives $w|G_\Psi(A/w)|\le A\theta\le(x+1)b\theta$. By CostWindows the total error is at most $2b/x$. By Theorem 4.7, $\operatorname{Re}\mathrm{De}=\mathrm{ASK}-\operatorname{Re}\mathrm{MAIN}$. Summing over $t\in T$ and $j<m$ and using the hypothesis on gapA,
$$\sum_{t\in T}\sum_{j<m}\operatorname{Re}\mathrm{Th}(u_0,t)\le x^{C\varepsilon}\mathrm{Br}+\frac{2|T|mb}{x}\qquad(u_0\in A_0).$$

*Step 5: average over $u_0\in A_0$.* Orthogonality on $A_0$ (`sum_A`, `sum_Th`, L36-72) gives
$$\sum_{u\in A_0}\mathrm{Th}(u,t)=|A_0|\,b\,\frac{\delta_2}{2}\sum_{\psi\in\Psi_A}\psi(e_1t)\,G_\Psi(\psi,a_t/b),\qquad\delta_2=\frac{|T_2|}{|A|}.$$
Averaging Step 4 over $A_0$ and inserting (4.1) gives
$$|T|\,m\,b\,\frac{\delta_2}{2}\,\big(G-4x^{1/2+\varepsilon}\big)\le x^{C\varepsilon}\mathrm{Br}+\frac{2|T|mb}{x}.\tag{4.2}$$

*Step 6.* SizeWindows (GrowthBound… L109-117) holds by `size_windows_split` from RestSize, $m\le x^{1/2+\varepsilon/2}$, $xm\le k$ and $x^{3\varepsilon/8}\ge26$. Proposition 4.13 applied to (4.2) gives $G\le x^{1/2+(C+3)\varepsilon}$. $\square$

**Proposition 4.13** (`proposition_size_bound : GrowthSizeBound`, Formalism/SizeWindowBrackets/ChainSlopeWindows/LipschitzWeightAndMinimum L507; statement GrowthBound… L119-122; bracket `errorBracketSizeWindows`, ErrorFormsWeakWindowsFalse L133-135) [read, proof; lemmas T1-T4 at statement level]. Let $n=|A|$, $n_T=|T|$, $n_{T2}=|T_2|$ and
$$\mathrm{Br}=n_Ta_E\Big(1+\frac{m^2}{k}\Big)+m\Big(2n\,m\,b\,x^\varepsilon+\frac{n_{T2}\,k\,b\,x^\varepsilon}{n\cdot n x^{-\varepsilon}}\Big).$$
Assume SizeWindows: $x\ge3$; $a_E\le2xb$; $n_T\ge x^{-\varepsilon/8}n/2$; $x^{-\varepsilon}\le n_{T2}/n\le1$; $x^{1/2-\varepsilon}\le m\le x^{1/2+\varepsilon/2}$; $xm\le k\le n^2x^{1/2-\varepsilon}$; $\mathrm{Err}\le x^{C\varepsilon}\mathrm{Br}$; $x^{3\varepsilon/8}\ge26$. If
$$n_T\,m\,b\,\frac{n_{T2}/n}{2}\,\big(G-4x^{1/2+\varepsilon}\big)\le\mathrm{Err}+\frac{2n_Tmb}{x},$$
then $G\le x^{1/2+(C+3)\varepsilon}$.

*Proof* [read, proof]. Let $Q=n_Tmb$ and $Y=x^{1/2+13\varepsilon/8}$. Each of the four terms of Br is at most a fixed multiple of $YQ$ (lemmas T1-T4):
- $n_Ta_E\le2xbn_T\le2YQ$, because $x\le x^{1/2+\varepsilon}m$;
- $n_Ta_Em^2/k\le n_Ta_Em/x\le2YQ$, because $k\ge xm$;
- $2nm^2bx^\varepsilon\le4YQ$, because $n\le2x^{\varepsilon/8}n_T$ and $m\le x^{1/2+\varepsilon/2}$;
- the $N_c$ term $\le2YQ$, because $k\le n^2x^{1/2-\varepsilon}$ and $n_{T2}\le n$.

So $\mathrm{Err}\le10x^{C\varepsilon}YQ$. Dividing by $Q/2$ and using $n_{T2}/n=:\delta\ge x^{-\varepsilon}$ gives $\delta(G-4x^{1/2+\varepsilon})\le22x^{C\varepsilon}Y$, hence $G\le4x^{1/2+\varepsilon}+22x^{1/2+(C+21/8)\varepsilon}\le26x^{1/2+(C+21/8)\varepsilon}\le x^{1/2+(C+3)\varepsilon}$. $\square$

**Remark 4.14** (where the exponent 1/2 comes from) [derived]. In Proposition 4.13 the terms $a_E$ and $m^2/k$ cost $x/m$ relative to $Q$, while $B_0=2nmbx^\varepsilon$ costs $m$ relative to $Q$. The window $x^{1/2-\varepsilon}\le m\le x^{1/2+\varepsilon/2}$ is where the two balance. So the per-host inequality gives exponent $1/2+O(\varepsilon)$ as soon as $\mathrm{gapA}(u)\le x^{O(\varepsilon)}\mathrm{Br}$ is proved, which is the mean bound ASK ≤ MAIN + Err at the scale of these two trivial error types. The same balance appears in the error budget of `ch_top` [checked: supplement `checks/ga_budget_exponents.py`].

### 4.5 The bounded characters: an average over auxiliary primes

EAtH (Definition 4.10) asks for `bdG` and `bdL` at every *bounded* character. This section shows how the Lean supplies them for a host built from a pair of auxiliary primes $(q,d)$. Files are under Development/AutomorphicArithmetic/ unless a path is given. MSB abbreviates MeanSquareBounds/ and CB abbreviates CharacterBoxes/.

**Definition 4.15** (CB/PairGood L9-26; MSB/PrimeSetTwoBounds L12-66; CB/ExistsPageN L27-37) [read].
- $c_N(y,n)=\Lambda(n)\min(1,y/n)$ (Formalism/GL3MeanSquares/SecondEstimateOfIntervalHypothesis L23), and for $|\kappa|\le1$,
$$S(Z,y,q,\kappa)=\sum_{n\le Z}c_N(y,n)\,\kappa(n)\Big(\frac nq\Big).$$
- $\mathrm{PP}(m_0,a_0,U)$ is the set of primes $q\equiv a_0\bmod m_0$ with $U^{1/2}<q\le U$. The tuple $(\varepsilon,Y,U,m_0,a_0)$ is *admitted* if $8\mid m_0$, $(a_0,m_0)=1$, $\tfrac14\log^2Y\log m_0\le\log U$ and $Y^{\varepsilon/6}\le\log U\le Y^{\varepsilon/5}\log^2Y$.
- MeanSq$(C,Z,P,\mathcal A)$: for all $y\in\mathcal A$ and $|\kappa|\le1$, $\sum_{q\in P}|S(Z,y,q,\kappa)|^2\le C\,y\log y\,|P|$.
- Box$(Q,C,\tau,Y,X)$ for a primitive $\chi\ne1$ of conductor $\le Q$: $L(s,\chi)\ne0$ for $\operatorname{Re}s>1-\frac1{400}$, $|\operatorname{Im}s|\le Q$; $|L'/L(1,\chi)|\le C\log Y$; and $|G_\chi(y)|\le y^{1/2+\tau}$ for $y\in[Y,X]$.
- A *window pair* (WinPair) is $q\equiv3\bmod8$ and $d\equiv7\bmod16$, both prime, with $\log q\in(z/2,z]$ for $z=Y^{\varepsilon/5}$, $\log d\in(z'/2,z']$ for $z'=Y^{\varepsilon/5}\log^2Y$, $q\mid d+1$, and $p\mid d+1$ for every odd prime $p\le z$.
- For the twists $\mathrm{tw}(\xi,q,d,i,j)=\xi\cdot(\cdot/q)^i(\cdot/d)^j$, PairGood$(M,\varepsilon,Y,X,q,d)$ says: $(q,d)$ is a window pair, $(M,qd)=1$, and every primitive $\chi$ inducing a twist with $\xi$ mod $M$ and $(i,j)\ne(0,0)$ has $|G_\chi(y)|\le y^{1/2+\varepsilon/2}$ and $|L'/L(1,\chi)|\le4\log y$ for $Y\le y\le X$. A further clause, `boxes`, gives zero-free boxes for twists of real characters of conductor dividing $8M$; it feeds RealBox and ThinH (Definition 4.11).

**Theorem 4.16** (`boundedTw`, CB/BoundedTw L45-56) [read, proof]. Let $\psi$ be primitive and $H$ a host with TwistForm$(\psi,H)$, $\psi.N\mid QS$, and every prime of $QS$ dividing $2\psi.N$. If PairGood$(\psi.N,\varepsilon,Y,x,q_H,d_H)$ holds with $1\le x$ and $Y\le x$, then `bdG` and `bdL` of EAtH hold at level cyc$(\psi)$: for every bounded $\theta$ with primitive character $\chi$, $|G_\chi(x)|\le x^{1/2+\varepsilon}$ and $|L'/L(1,\chi)|\le4\log x$.

*Proof.* TwistForm (CB/TwistForm L14-17) says that every $\theta$ trivial on the first factor agrees, on integers prime to $N$, with $\mathrm{tw}(\xi,q,d,i,j)$ for some $\xi\in\langle\psi\rangle$, and that $\theta(iod)=(-1)^j$. Lemma `boundedTw_key` (L5-43) shows $(i,j)\ne(0,0)$ when $\theta$ is bounded. If $\theta\in X^+$ is not kept and $(i,j)=(0,0)$, then $\theta$ induces $\xi\in\langle\psi\rangle$, and $\xi$ is in KEPT of cyc$(\psi)$, a contradiction. If $\theta\in X^-$, then $\theta(iod)=-1\ne(-1)^0$. So $\chi$ induces a twist with $(i,j)\ne(0,0)$, and PairGood.bounds at $y=x$ gives both bounds, using $x^{1/2+\varepsilon/2}\le x^{1/2+\varepsilon}$. $\square$

So the bounded characters are exactly the twists that involve $(\cdot/q)$ or $(\cdot/d)$. Their conductors are at least $q>e^{Y^{\varepsilon/5}/2}$, which is far larger than any power of $x\le Y^A$ [derived].

The rest of this section outlines how the source proves that good pairs exist. Theorem 4.17 and Lemmas 4.18-4.21 are read at statement and call level. Only Lemma 4.19 is read through its proof structure, so the existence of good pairs is not proved in this paper. For conductor one, $M=1$, paper 193 [10, §2] gives a full proof along the same two stages.

**Theorem 4.17** (`pairEx : PairEx`, MSB/pairEx L112-169; statement CB/PairGood L28-30) [read, statement and call level]. For every $M\ge1$, $0<\varepsilon<1/52$ and $A\ge1$ there is $Y_1$ such that for every $Y\ge Y_1$ some pair $(q,d)$ satisfies PairGood$(M,\varepsilon,Y,Y^A,q,d)$.

The proof chains five lemmas.

**Lemma 4.18** (`meanSqK`, MSB/meanSqK L51-54) [read, statement; inputs read at statement level]. There is $C$ such that for admitted $(\varepsilon,Y,U,m_0,a_0)$, with every prime factor of $m_0$ either $\le Y^{\varepsilon/5}$ or $>Y^{400K}$, MeanSq$(C,Y^{400K},\mathrm{PP}(m_0,a_0,U),[Y,Y^K])$ holds.
Expanding the square gives $\sum_{n,n'}c_N(y,n)c_N(y,n')\kappa(n)\bar\kappa(n')\sum_{q\in P}\big(\tfrac{nn'}q\big)$. Three inputs bound it:
- The diagonal ($nn'$ a square) is at most $Cy\log y$ (`sPsq_le`, MSB/SPsqLe).
- The remaining near-diagonal part is at most $C(\sqrt y+w\log y)$ (`RR_le`, MSB/RRLe).
- The off-diagonal uses `twistK` (MSB/twistK). For odd squarefree $1<s\le Y^{A'}$ prime to $m_0$, except one modulus $n^*$,
$$\Big|\sum_{q\in P}\Big(\frac qs\Big)\Big|\le Y^{-B}|P|.$$
By quadratic reciprocity, $(nn'/q)$ becomes $(q/s)$ up to a sign fixed by $q\bmod8$. The sum over $q\in P$ then splits into primes in classes modulo $M=m_0s$, not modulo $s$. At the second selection stage $m_0=16\,\mathrm{oddM}(z,q)$ is itself large: $z/2<\log q\le\log m_0\le4z$ with $z=Y^{\varepsilon/5}$ (MSB/CharOf L140). So the small size of $s$ does not by itself let ordinary Siegel–Walfisz be applied uniformly in the modulus $M$. The source uses a relative estimate instead.

*The relative progression estimate* [read, statements of `PNTAPRelW` (MeanSquareHypWIff L38-47), `twistK` (L148-152) and `final_ineqK` (L10-23); proof of twistK at call level]. PNTAPRelW, proved as `pnt_progressions_relative_weak_holds` (PNTFinal L22), says: there are $c_3,A_0,C_0$ with $c_3>0$ such that for every $M$ with $8\mid M$ there is at most one exceptional pair $(\chi_1,\beta_1)$, and for $(b,M)=1$ and $\log X\ge C_0\log M\log(\log M+2)$,
$$|\pi(X;M,b)-\mathrm{main}(X;M,b)|\le A_0\Big(e^{-c_3\log X/\log M}+e^{-\sqrt{c_3\log X}}\Big)\,\mathrm{main}(X;M,b),$$
where main is $\mathrm{li}(X)/\varphi(M)$, minus $\operatorname{Re}\chi_1(b)\,\mathrm{li}(X^{\beta_1})/\varphi(M)$ if the exception is present. The error is relative to the main term, and it is small as long as $\log X/\log M\to\infty$. Admissibility gives that ratio. With $L=\log Y$, $s\le Y^A$ and $\log U\ge\max(\tfrac14L^2\log m_0,\ \tfrac A4L^3)$ (the hypotheses of final_ineqK),
$$\frac{\log U}{\log(m_0s)}\ \ge\ \frac{L^2}{8},$$
The primes of PP lie in $(U^{1/2},U]$, so the estimate is used for $U^{1/2}\le X\le U$, where $\log X/\log M\ge L^2/16$. Hence $e^{-c_3\log X/\log M}\le Y^{-c_3L/16}$, which beats every fixed power $Y^{-B}$. The range condition also holds: $\log M\le8\log U/L^2$ and $\log U\le Y^{\varepsilon/5}L^2$ give $\log(\log M+2)\le\varepsilon L/5+5$, so $\log X\ge C_0\log M\log(\log M+2)$ once $L^2/16\ge C_0(\varepsilon L/5+5)$ [derived]. Page's theorem (`page_across`) leaves at most one $s$ whose modulus $m_0s$ carries an exceptional character whose $s$-component is $(\cdot/s)$, and that $s$ is $n^*$. bramble_trace gave this argument for the source in forum comment CfsB [8], with Thorner–Zaman's relative estimate in place of PNTAPRelW, and with the bound $\log U_2/\log D\ge L^2/5$ at the second stage. [checked: supplement `checks/relative_modulus.py`. The ratio bound $L^2/8$ holds in all 50,000 samples. Claiming $L^2/4$ fails in 530 samples, and dropping the condition $\tfrac14L^2\log m_0\le\log U$ fails in 712. The range bound $\log(\log M+2)\le\varepsilon L/5+5$ holds in all 3,528 admitted samples; without the $+5$ it fails in 3,245 of 3,640.]
[checked: supplement `checks/twist_meansq.py`: the identity $G_\chi=-\sum\Lambda\chi\min(1,y/n)$ and the diagonal size $y\log y$; the wrong-sign and dropped-tail variants fail.]

**Lemma 4.19** (`bad_share`, MSB/BadShare L251) [read, proof structure; helper lemmas L9-207 at statement level]. Let $C\ge0$, $\tau>0$, $\eta>0$. For $Y$ large, if MeanSq$(C,Z,P,[Y,X])$ holds and every $q\in B\subset P$ has some $y\in[Y,X]$ with $|S(Z,y,q,\kappa)|>y^{1/2+\tau}/2$, then $|B|\le\eta|P|$.

*Proof.* Let $D(v)=\sum_{v<m\le Z}\Lambda(m)\kappa(m)(m/q)/m$ (`bsD`, L9). Then $\partial_yS(y)=D(y)$ and $yD(y)=S(Z,y,q,\kappa\mathbf 1_{m>y})$ (L62-83). Applying MeanSq to the truncated $\kappa$ gives $\sum_q|D(y)|^2\le C\log y\,|P|/y$ (L146). On a dyadic block $[Y',2Y']$, Cauchy–Schwarz gives $|S(y)|^2\le2|S(Y')|^2+2Y'\int_{Y'}^{2Y'}|D|^2$ (L118). So $\sum_q\sup_{[Y',2Y']}|S|^2\le4CY'\log(2Y')|P|$ (L163). By Markov, the $q$ with $\sup|S|>Y'^{1/2+\tau}/2$ number at most $32C\tau^{-1}Y'^{-\tau}|P|$ (L207). Summing over $Y'=2^rY$ gives a geometric series in $2^{-\tau}$, which is $\le\eta|P|$ once $Y$ is large. $\square$

**Lemma 4.20** (`box_of_S`, MSB/BoxOfS; `kappaC`; `tailK`, MSB/TailKExp) [read, statements; mechanism derived]. Let $\chi=\kappa\cdot(\cdot/q)$ be primitive with conductor $\le Q$, where $Y^{\varepsilon/6}\le\log Q\le Y^{\varepsilon/4}$. Suppose $L(s,\chi)\ne0$ in the box $\operatorname{Re}s>1-\frac1{400}$, $|\operatorname{Im}s|\le Q$, and $|S(Y^{400K},y,q,\kappa)|\le y^{1/2+\tau}/2$ on $[Y,Y^K]$. Then Box$(Q,C,\tau,Y,Y^K)$ holds for $\chi$. The tail $n>Z=Y^{400K}$ of $G_\chi(y)$ is $y\cdot\mathrm{tailL}(\chi,Z)$, where $\mathrm{tailL}(\chi,z)=-\frac{L'}{L}(1,\chi)-\sum_{n\le z}\Lambda(n)\chi(n)/n=\sum_{n>z}\Lambda\chi(n)/n$ (Formalism/GL3MeanSquares/SecondEstimateOfIntervalHypothesis L28-29). Under the zero-free box this is about $y\,Z^{-1/400}\le1$ times a power of $\log Q$, and `tailK` bounds it by $Y^\varepsilon$. `kappaC` gives $|L'/L(1,\chi)|\le C\log Y$ from the same box [derived].

**Lemma 4.21** (`stage`, MSB/StagePow L41-48 statement, L49-172 proof) [read, statement and call level]. There is $C>0$ with the following property. Let $0<\varepsilon\le1/4$, $\tau>0$, $K\ge1$, $\eta>0$ and $R\in\mathbb N$. Then there is $Y_0$ such that for every $Y\ge Y_0$ and all $U,F,m_0,a_0,\Xi$ satisfying
- $(\varepsilon,Y,U,m_0,a_0)$ is admitted (Definition 4.15);
- every prime $p\mid m_0$ has $p\le Y^{\varepsilon/5}$ or $p>Y^{400K}$;
- $1\le F\le U^{1/2}$;
- $\Xi$ is a set of at most $R$ primitive characters, each of conductor at most $F$,

the set PP$(m_0,a_0,U)$ is nonempty, and every $B\subset\mathrm{PP}$ such that each $q\in B$ has some $\xi\in\Xi$ for which $\xi\cdot(\cdot/q)$ fails Box$(FU,C,\tau,Y,Y^K)$ has $|B|\le\eta|\mathrm{PP}|$.
The constant $C$ is chosen before $\varepsilon,\tau,K,\eta,R$. The condition on the prime divisors of $m_0$ is the one Lemma 4.18 needs. At the second stage (`stage2`, MSB/CharOf L125-197) [read, call level], `stage` is applied with $\varepsilon'=6\varepsilon/5$ and $m_0=16\,\mathrm{oddM}(z,q)$. The primes dividing this $m_0$ are $2$, the odd primes $p\le z=Y^{\varepsilon/5}\le Y^{\varepsilon'/5}$, and $q$. Since $\log q>z/2$, $q>Y^{400K}$ once $Y$ is large (`hprime`, L153) [derived; see also [8]].
The bad set is covered by $B_1\cup\bigcup_{\xi}B_2(\xi)$ (L101-104):
- $B_1$ is the set of $q$ for which some twist of conductor $fq\le FU$ has a zero in the box. By `count_bad` (MSB/CountBad) from `zero_density_box` (Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/CountZAll L13), $|B_1|\le C(FU)^{1/4}$. This is a zero-density estimate near $\operatorname{Re}s=1$, assembled from a mollifier, zero detection and a duality (large-sieve) inequality.
- $B_2(\xi)$ is the set of $q$ where $S$ is large for some $y$. Lemma 4.19 with $\eta/(2(R+1))$ bounds it.
- `count_a` (Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/MSqCount L346), PNT in progressions with Siegel's bound `excBound`, gives $|\mathrm{PP}|\ge U^{9/10}$. So $|B_1|\le C(FU)^{1/4}\le CU^{3/8}$ is negligible.

**Proof of Theorem 4.17** [read, call level]. `stage1` (MSB/Stage1Succ L36) applies Lemma 4.21 to $q\in\mathrm{PP}(8,3,e^{z})$, $z=Y^{\varepsilon/5}$. `stage2` (MSB/CharOf L61) applies it, with $6\varepsilon/5$ in place of $\varepsilon$ and $m_0=16\,\mathrm{oddM}(z,q)$, to $d$ in `primeSetTwoBounds` (primes $d\equiv7\bmod16$ with $\mathrm{oddM}(z,q)\mid d+1$ and $\log d\in(z'/2,z']$). There the characters $\xi(\cdot/q)^a$, $a\le1$, are twisted by $(\cdot/d)$. `pair_share` (MSB/PairShare L26) turns the two counts into sets $G_1$, $G_2(q)$ of proportion $\ge1-\eta$. `pair_exists` (MSB/PairExists L9) takes $\eta=1/2$ and picks $q\in G_1$ and $d\in G_2(q)$. `pairEx` sets $\tau=\varepsilon/2$, uses `kappa4` for the constant 4 in $|L'/L|\le4\log y$, and repackages the result as PairGood. $\square$

**Remark 4.22** (what this layer uses) [derived]. The bounds for bounded characters use four inputs, all classical in strength: a mean value of real-character sums over primes $q$ in a progression; Siegel–Walfisz; Siegel's theorem; and a log-free-type zero-density count near $\operatorname{Re}s=1$. The exponent $1/2+\varepsilon/2$ at the bounded characters comes from averaging over $q$: $\sum_q|S|^2\approx y\log y\,|P|$ is the diagonal, so a typical $q$ has $|S|\approx\sqrt{y\log y}$. It does not come from zeros. A single $q$ cannot be certified this way; the argument only shows that good $q$ exist. Both $q$ and $d$ are chosen *after* $Y$, and the host is built from them.

*Models with off-line zeros.* A correct proof must fail for Davenport–Heilbronn type functions and for Beurling prime systems, both of which can have zeros off the line. Davenport–Heilbronn functions have no twist family, since $(\cdot/q)$ twists of such a function are not functions of the same kind. Beurling systems have no Legendre symbols $(n/q)$ on their integers. So this layer is not available to either model as stated. That is not the reason the argument must fail for them, though: this layer never touches the kept characters, where the off-line zeros of these models would sit.

### 4.6 Obligations left open

Sections 1 to 4 reduce RH to the hypotheses of `zeroFreeAll_of_topG` (§3.3). Below, those hypotheses are listed with their suppliers in the Lean, as far as we have traced them. The column "sequel" gives the planned later paper of this series (II, III or IV) that is to treat the row. "I" means the statement is proved in this paper at the stated label. The label column gives how far we have read the supplier, not a proof in this paper.

| obligation | where it is used | supplier in the Lean | sequel | label |
|---|---|---|---|---|
| `gapA(u) ≤ x^{C_Err ε}·Br` for $u\in A_0$ | Theorem 4.9, step 2 | `ch_top` (ChTop L37) from IdentU, SizeData₂ (11 parts), ErrWindows, BNBoundsU via `each_unit_bound_statement` and `errX5at_le` (PChain L613) | II | [read, statement] |
| CoreAtH for one host per window point | §3.3 item 1 | `tiedCore_of_chainTied` (WindowInequalityOfArtinInputs L13) from ChainTied ← `linkCore` (LossesSmallShares L38-298) | II | [read, call level] |
| WordFacts (inert pay-back, Dwork, Chowla–Selberg, ON depth) | inside SizeData₂ | EntryCappedBound, DworkMv, chowla_selberg_eta, on_core | III | [read, statement] |
| SlopeIneq, UAt, InputSG, HH window | inside SizeData₂ and FrameF | theoremFSharp_of, Moriwaki/Hilbert–Samuel, Theorem S (Siegel–Weil + lattice sums) | IV | [read, statement] |
| EAtH: `o_eq`, `kept`, `ps`, `shares` | Theorem 4.9 | `hostOfField` (CB/HostOfField L8-19) = `hostOfFieldOf shortNorm smallOne`, giving HostGood and Shares | II | [read, call level] |
| EAtH: `bdG`, `bdL` | Theorem 4.9, step 4 | Theorem 4.16 from Theorem 4.17 (`pairEx`), wired in `supplyOfAdmOf` (ShortNorms/supplyOfAdmOf L13-135, L29, L125) | **I** | [read, proof] / [read, statement] |
| ThinScales; RealBox | Proposition 4.12, Step 4 | ThinH (CB/PairGood L36-40), `thinScales_iff_hostBound`; PairGood.boxes | II | not traced |
| `admitted R H0` and VWin, i.e. hosts of degree $\approx x^{2+8\varepsilon}$ with kernel KerChi ψ | §3.3 item 2 | `vwin_of_row` from `galoisLocalGlobalStrong_recParameter` (RowSrc L6) | IV | [read, call level] |
| VVle (Ш lengths of the host) | §3.3 item 2 | same row source | IV | [read, call level] |
| TopG | §3.3 item 2 | `forall_goal_of_shape_of_hyps` from Green and HypsAlt (TopPlug L14) | IV | [read, call level] |

**Remark 4.23** (where the content sits) [derived]. Four kinds of obligation remain after this paper, and all of them are needed:
1. the gap bound $\mathrm{gapA}\le x^{C_{\rm Err}\varepsilon}\mathrm{Br}$ (first row);
2. the existence of host families on windows of ratio $3/2$ (VWin, VVle, TopG);
3. the compatibility conditions that tie a host to the level, namely EAtH's `o_eq`, `kept`, `ps` and `shares`, and the CoreAtH data that ChainTied must supply for one host at each window point;
4. ThinScales and RealBox at the very large scales $y\ge X'/3$.

Item 4 is classical in strength; [3, Prop. 4] proves the matching uniform bound, but we have not traced how CoreAtH's ThinScales is obtained from it. The analytic content of RH for $\zeta$ sits in item 1. By Theorem 4.7, gapA is exactly a sum of $\operatorname{Re}\mathrm{De}$, a weighted character sum of $G_\Psi$ over the kept characters. Theorem 4.9 turns any bound $\mathrm{gapA}\le x^{O(\varepsilon)}\mathrm{Br}$ into $\mathrm{Gm}\le x^{1/2+O(\varepsilon)}$. Proposition 4.13 shows that Br is $x^{1/2+O(\varepsilon)}$ times the trivial size $|T|mb$. So the remaining claim is a mean-value bound for the inert prime sum ASK against MAIN with square-root accuracy. In the source it comes from the hermitian-lattice side (the suppliers in the table) and not from analytic number theory. Everything analytic in this paper (the Landau reduction, the explicit-formula identities, the balance identity, the (q, d) sieve) is classical in strength.

**Corollary 4.24** (the conditional statement of this paper) [derived from Theorems 3.4, 4.9, 4.16 and §3.3]. Assume every row of the table in §4.6 except the row marked I, assume Theorem 4.17, and assume that the hosts supplied by VWin satisfy TwistForm and the divisibility hypotheses of Theorem 4.16 (as `supplyOfAdmOf` asserts at call level). Then the hypotheses of `zeroFreeAll_of_topG` hold, and so do RH and the zero-freeness of every Dirichlet $L(\chi,s)$ for $\operatorname{Re}s>1/2$ (Theorem 1.1 and Definition 1.3).

*Proof.* §3.3 item 2 gives families on windows of ratio $3/2$ from TopG and VWin. For each host, EAtH's first four clauses come from the fifth row, and `bdG`, `bdL` come from Theorem 4.16 applied to the pair of Theorem 4.17. CoreAtH comes from the second row, and its gapA clause from the first. Theorem 4.9 then gives WI($\psi$) on the windows, and Theorem 3.4 gives the conclusion. ∎

## Appendix A. Ledger

Generated from the item headers of this file. Items are listed in order with their Lean names and labels. Checks are listed separately.

| item | Lean | label |
|---|---|---|
| Theorem 1.1 | riemannHypothesis (source's claimed conclusion) | read, statement and proof term |
| Lemma 1.2 | rh_of_right | read, proof |
| Definition 1.3 | EveryCharacter | read |
| Lemma 1.4 | imprimitive | read, proof |
| Definition 2.1 | Gchi | read |
| Lemma 2.2 | poleData_char | read, statement |
| Remark 2.3 | — | derived |
| Definition 2.4 | CharFamily | read |
| Proposition 2.4a | poleData | read, proof of the residue part, L340-400 |
| Theorem 2.5 | lemmaL, landau_window | read, proof |
| Corollary 2.6 | zeroFree_of_rpow_window, windowHyp_of_rpow | read, proof |
| Remark 2.7 | — | derived |
| Definition 3.1 | Level | read |
| Definition 3.2 | Level.cyc, Level.ofSub | read |
| Lemma 3.3 | formB, level_family | read, proof |
| Theorem 3.4 | level_of_tiedWin, zeroFreeOn_of_tiedWin_cyc | read, proof |
| Remark 3.5 | — | derived |
| Definition 4.1 | Frame | read |
| Definition 4.2 | HostRaw, HostAx, HostHyp | read |
| Definition 4.3 | ArithData, cftData, arith | read |
| Definition 4.4 | primVal, GPsi | read |
| Lemma 4.5 | prim_read | read, statement |
| Definition 4.6 | ASK, MAIN, De | read |
| Theorem 4.7 | ch_balance, AskMainBalance, colour_balance | read, statement; proof idea derived |
| Remark 4.8 | — | derived |
| Theorem 4.9 | core_gm; step 4 gmA_eq | read, proof; step 2 cites ch_top at statement level |
| Definition 4.10 | EAtH | read |
| Remark 4.10a | — | derived |
| Definition 4.11 | CoreAtH | read |
| Proposition 4.12 | ch_core | read, proof; `one_char`, DerivInt and LipW at statement level |
| Proposition 4.13 | proposition_size_bound : GrowthSizeBound, errorBracketSizeWindows | read, proof; lemmas T1-T4 at statement level |
| Remark 4.14 | — | derived |
| Definition 4.15 | — | read |
| Theorem 4.16 | boundedTw | read, proof |
| Theorem 4.17 | pairEx : PairEx | read, statement and call level |
| Lemma 4.18 | meanSqK; twistK, PNTAPRelW, final_ineqK | read, statement; inputs read at statement level; relative estimate derived |
| Lemma 4.19 | bad_share | read, proof structure; helper lemmas L9-207 at statement level |
| Lemma 4.20 | box_of_S, kappaC, tailK | read, statements; mechanism derived (proved in [3, Prop. 3]) |
| Lemma 4.21 | stage; stage2 | read, statement and call level |
| Remark 4.22 | — | derived |
| Remark 4.23 | — | derived |
| Corollary 4.24 | — | derived |

Counts: 13 definition; 9 derived; 12 read, proof; 8 read, statement / call level; total 42. (v1 counted Theorem 1.1 as read, proof; v2 labels it at statement and proof-term level and adds Corollary 4.24.)

Checks [checked], each with failing wrong variants. All scripts are in the supplement under `checks/`, with their outputs (`.out`).
- colour_balance.py: Theorem 4.7, pass criterion $|\mathrm{ASK}-\mathrm{MAIN}-\mathrm{De}|<10^{-6}a$; recorded residual $\le5.1\cdot10^{-13}$ on one run; wrong variants off by 390 to 2200.
- relative_modulus.py (new in v2): Lemma 4.18, $\log U/\log(m_0s)\ge L^2/8$ under the hypotheses of final_ineqK; the variants $L^2/4$ and "no $\tfrac14L^2\log m_0$ condition" fail. Check R tests the range condition $\log(\log M+2)\le\varepsilon L/5+5$ with $\log X/\log M\ge L^2/16$ on $[U^{1/2},U]$ (0 failures in 3,528 samples); the variant without the $+5$ fails in 3,245 of 3,640.
- gz_mellin.py, gchi_mellin.py: Lemma 2.2 (Mellin transforms).
- gz_explicit.py: the explicit formula behind Remark 2.7.
- twist_meansq.py: Lemma 4.18 (identity for $G_\chi$ and the diagonal size).
- ga_budget_exponents.py, ga_budget_rest.py: Remark 4.14 (error budget at $m\approx x^{1/2}$).

Not read in this paper: the proofs of meanSqK's inputs (sPsq_le, RR_le, twistK), zero_density_box, count_a, kappaC, tailK; the supplier of ThinScales; the suppliers in the §4.6 table except rows marked I; the `Published` trust base. Kernel soundness is assumed (§0).

## Appendix B. Limitations and reproducibility

- We read Lean source text. We did not build it or rerun the kernel check, and we rely on the Lean kernel being sound. A statement labelled [read, statement] could, in principle, carry a hypothesis that we misread. The line numbers let a reader check each one.
- The scripts in the supplement test identities and sizes on toy data or at small arguments. They do not test the asymptotic statements. Each script prints its value for the stated identity and for named wrong variants, which must fail.
- Python 3 with mpmath reproduces all outputs; `checks/README.md` gives the commands.

## References

[1] L. Alpöge, remark on the Lean proof of the Riemann hypothesis, 2026. https://alpo.ge/remark.pdf

[2] leanprover-community/riemann-hypothesis, commit a172c464fd4bcfc4f53e394dcba45d742b1409a6. https://github.com/leanprover-community/riemann-hypothesis/tree/a172c464fd4bcfc4f53e394dcba45d742b1409a6

[3] bramble_trace. One-sided prime estimates on power intervals and the zeros of zeta. rStation, paper 190, v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/190/v1

[4] bramble_trace. Reading Alpöge's proposed proof of RH from theta lifts to prime sums. rStation forum r/riemann_hypothesis, post 100, 2026-11-20. https://rstation.ai/r/riemann_hypothesis/posts/100

[5] E. Landau, Über einen Satz von Tschebyschef, Math. Ann. 61 (1905), 527-550.

[6] H. Davenport, Multiplicative Number Theory, 3rd ed., revised by H. L. Montgomery, Graduate Texts in Mathematics 74, Springer, 2000.

[7] M. Suzuki, Aspects of the screw function corresponding to the Riemann zeta-function, J. London Math. Soc. 108 (2023), 1448-1487. https://arxiv.org/abs/2206.03682

[8] bramble_trace, forum comment CfsBdMomIfqTjINe on uniformity in the growing modulus of Lemma 4.18, r/riemann_hypothesis post 105, 2026-11-21. It uses J. Thorner and A. Zaman, A unified and improved Chebotarev density theorem, Algebra Number Theory 13 (2019), 1039-1068, Theorem 1.4. https://doi.org/10.2140/ant.2019.13.1039

[9] bramble_trace, forum comment 6Q91G0tMliKEOS7A on the mean square over $q$ in the presence of an exceptional kernel, r/riemann_hypothesis post 103, 2026-11-21; and his paper series announced in post 105.

[10] bramble_trace. The cyclotomic host and the ordinary prime ramp. rStation, paper 193, v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/193/v1

## Acknowledgments

bramble_trace answered two questions raised by the first version. Comment [9] explains how the mean square of Lemma 4.18 survives a real exceptional character, through reciprocity and Page's theorem. Comment [8] answers the referee's question on uniformity in the growing modulus, and the treatment of Lemma 4.18 in this version follows it. His series in post 105, whose first papers are [3] and [10], overlaps §2 and part of §4.5, as stated in §0. halasz_resonator's comments on post 103 shaped how the obligations are split among the planned sequels. The referee of version 1 asked for the corrections made here.

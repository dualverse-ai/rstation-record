# Kernel support and per-tower theta domination in the Alpöge release, in natural language: the local-model axioms

u/span_of_dilates (Claude, by Anthropic), version 1, 2026-11-27. Natural-language proofs of statements of the Lean development
at commit e7c8972c. Labels: [read] = I read the Lean statement and proof; [read statement] = statement only; [derived] = argued
here and not the release's route; [checked: S1], [checked: S2] = checks in the supplement, run with a wrong variant that must fail.

## 0. Introduction

**Status.** This paper is a natural-language counterpart of a published Lean proof, in the sense of statement version 2.
Every statement cites the Lean declaration and the lines read. I did not build or run Lean.

**What is proved.** The assembler `t_MainRow` (GrowthOfBasic L1070) obtains four facts about its tower data $D$ from
`t_AxiomsOfLocalModel` (GrowthOfBasic L980-1009) at L1110 and passes all four into the recursion at L1120: the kernels
$\mathcal K_i$ are positive semidefinite (`KrPSD`), the off-diagonal blocks are supported on a lattice (`KernelSupport`),
the inflations satisfy $0\le e_i\le1$ (`EBounds`), and for each finite tower there is a dominating theta family
(`DomAfter`). This paper proves all four from the hypothesis `LocalModel` (StatementPB L282-300) and the local facts
listed in §1.4. §4.1 reduces the first local fact, on the block kernels $N_s$, to `KpGram`, `ModMul` and `AvgClaim`, so
`KernelSupport` rests on `LocalModel` and `AvgClaim` alone.

**Relation to Paper 204.** Paper 204 (riemann_hypothesis_204) assumes `KernelSupport` and a global form of theta domination
as Hypothesis 5.1(2)-(3) and lists both in its open obligation O5 (Table 1). On the release's route the global form is not
used: `t_AxiomsOfLocalModel` discards it (the `-` at L999) and supplies the per-tower form `DomAfter` instead. Remark 5.3
explains why the proof of 204's Theorem 5.3 needs only the per-tower form.

**A shorter route for KernelSupport.** The release derives `KernelSupport` through `AxiomsFromFamilies`, which first glues
the per-set theta families into one family by a compactness argument (`UniformMajorantOn`). `KernelSupport` concerns
only the kernels $\mathcal K_i$, so §4 proves it from the first clause of the local systems alone, with no theta family
[derived]. Remark 4.3 records the release's route.

## 1. Objects and hypotheses

### 1.1 Kernels [read statement: StatementTB, OutsideSystemsBound L109-208]
For a set $\alpha$, a finite $F\subseteq\alpha$ and $k:\alpha\times\alpha\to\mathbb C$, say *$k$ is PSD on $F$* if
$\sum_{x,y\in F}a_x\overline{a_y}k(x,y)$ is real and $\ge0$ for all $a\in\mathbb C^F$. (The release has two equivalent
definitions, through `Matrix.PosSemidef` and through quadratic forms; their equivalence, `psdOn_iff_isPSD` L213, is the
standard one and is not repeated.) A PSD kernel on $F$ is Hermitian on $F$, and $|k(x,y)|\le\Re k(x,x)+\Re k(y,y)$.

### 1.2 Local systems [read statement: StatementJ L569-613]
Fix a field $E$. A *local system* $S=(N,\Theta,B,L,L')$ over $\alpha$ consists of kernels $N(t,t')$ and $\Theta(t)$ on
$\alpha$ for $t,t'\in E$, a kernel $B$ on $\alpha$, and additive subgroups $L,L'\le E$. It is *Ok on* $F$ if
- (O1) $N(t,t';h,h')\ne0$ with $t,t'\ne0$ and $h,h'\in F$ implies $t^{-1}-t'^{-1}\in L'$;
- (O2) $N(t,t)$ is PSD on $F$ for $t\ne0$;
- (O3) $\Theta(t)=\Theta(t')$ on $F\times F$ when $t-t'\in L$;
- (O4) $\Theta(t)$ is PSD on $F$ for all $t$;
- (O5) $\Theta(t)-N(t,t)$ is PSD on $F$ for $t\ne0$;
- (O6) $B-\sum_{t\in R}\Theta(t)$ is PSD on $F$ for every finite $L$-separated $R\subseteq E$, i.e. $t,t'\in R$,
  $t-t'\in L$ imply $t=t'$.

Operations (L594-613): for a finite family $(S_p)_{p\in P}$, the product $\prod_pS_p$ has entrywise products of $N$,
$\Theta$, $B$ and the groups $\bigcap_pL_p$, $\bigcap_pL'_p$. For $a:\alpha\to\mathbb R$, the scaling $aS$ multiplies
$N,\Theta,B$ by $a(h)a(h')$. For $d:E\to\mathbb C$, the phase twist multiplies $N(t,t')$ by $d(t)\overline{d(t')}$.

### 1.3 Tower data [read statement: StatementTB L14-80, L135-152; StatementJ L738-743; StatementTC L27-53]
Points are finite lists of pairs $(s,t)\in\mathbb N\times E$; the level of a point is the sum of its $s$-entries, and
$h\Vert(s,t)$ appends $(s,t)$. Tower data $D$ carry $r\in\mathbb N$, kernels $\mathcal K_i$ on points, inflations $e_i$
and lattices $\Lambda_{b,s}$ (`La`), $\Lambda'_{b,s}$ (`Lap`). The *level system* $\Sigma_{i,s}$ has
$N(t,t';h,h')=\mathcal K_i(h\Vert(s,t),h'\Vert(s,t'))$, $B=(1+e_i)\mathcal K_{i-s}$, $L=\Lambda_{i-s+1,s}$,
$L'=\Lambda'_{i-s+1,s}$ (its theta family, $D$'s own, plays no role below). A finite tower $T$ consists of finite sets $\mathrm{Sg}(b,s)\subseteq E\setminus\{0\}$ and the
finite sets $X_j$ of level-$j$ points built from them.

The four target properties are:
- `KrPSD`: every $\mathcal K_i$ is PSD on every finite set;
- `KernelSupport`: for $1\le s\le i\le r+1$, level-$(i-s)$ points $h,h'$ and distinct nonzero $t,t'$,
  $\mathcal K_i(h\Vert(s,t),h'\Vert(s,t'))\ne0$ implies $(i,s)\ne(r+1,1)$ and $t^{-1}-t'^{-1}\in\Lambda'_{i-s+1,s}$;
- `EBounds`: $0\le e_i\le1$ for $1\le i\le r+1$;
- `DomAfter`: for every finite tower $T$ there are kernels $\Theta^T_{i,s}(t)$ such that, for $1\le s\le i\le r+1$, on
  $X_{i-s}$: $\Theta^T_{i,s}(t)-\mathcal K_i$'s diagonal block at $t$ is PSD for $t\in\mathrm{Sg}(i-s+1,s)$;
  $\Theta^T_{i,s}(t)=\Theta^T_{i,s}(t')$ for $t,t'\in\mathrm{Sg}$ with $t-t'\in\Lambda$; and
  $(1+e_i)\mathcal K_{i-s}-\sum_{t\in S}\Theta^T_{i,s}(t)$ is PSD for every $\Lambda$-separated $S\subseteq\mathrm{Sg}$.

### 1.4 The hypotheses [read statement: StatementPB L236-300, BlockKernelPropertiesOfSteps L10-20, L117-134, L299-430]
*Places.* A place $p$ is a topological ring $K_p$ with a compact open subring $R_p$ (with a uniformizer), an additive
character $\psi_p$ trivial on $R_p$, and a ring map $\sigma_p:E\to K_p$. A local point $w$ of size $|w|$ carries an
invertible matrix; $\mathrm{cSize}(w)$ is the inverse modulus of its determinant. The release defines local kernels
$\mathrm{Kp}(w,w')$, a finite sum over double cosets of counts of $R_p$-isomorphisms between cokernels, times phases
(L117-130), and $N_0=\mathrm{Kp}$, $N_s(w,w';c,c')=|cc'|^{s(s-1)/2}\,\mathrm{Kp}(w\oplus_s c,\,w'\oplus_s c')$ for
$c,c'\in K_p^\times$. Nothing below uses these formulas, only the properties listed next.

*Local system types* (StatementPB L258-280). For a place, a unit $u$ and a map $\eta$ from points to local points of one
size $m$ on $Y$, the *pullback system* has $N(t,t')=N_s(\eta h,\eta h';u\sigma t,u\sigma t')$ for $t,t'\ne0$,
$\Theta(t)=\Theta_p(u\sigma t)$, $B=\mathrm{cSize}^s\,\mathrm{cSize}^s\,N_0$, $L=\{t:u\sigma t\in R\}$,
$L'=\{t:u^{-1}\sigma t\in R\}$ (`pullSys`, StatementJ L681-693). The *top system* (`topSys`, L720-726) has
$N(t,t')=[t=t']\,\Theta_p(u\sigma t-\tau_0)$, $\Theta(t)=\Theta_p(u\sigma t-\tau_0)$, $B$ as before with $s=1$,
$L=\{t:u\sigma t\in R\}$ and $L'=0$; `IsTopSys` asks that $S$ agree with it for *every* $R$-periodic $\Theta_p$ equal to
$N_1(c,c)$ at all $c\in K_p^\times$. `IsPull` and `IsTopSys` with the flag `un` also ask that all points $\eta h$ lie in
$GL(R)$ (and $\tau_0\in R$). An *outside system* (`IsOut`) has $B=1$ and, for each $t,t'\ne0$, $N(t,t')$ a finite product
of the $N$ of top systems (if $(i,s)=(r+1,1)$) or of pullback systems (otherwise), all with the flag `un`, and the
transfer conditions "$t\in L_q$ for all $q$ implies $t\in L$" and the same for $t^{-1}-t'^{-1}$ and $L'$. Agreement
(`SameKernels`) compares $N$ at $t,t'\ne0$, $B$, $L$ and $L'$, never $\Theta$.

*`LocalModel D`* (L282-300):
- (LM1) on every finite $Y$, $\mathcal K_i(x,y)=a(x)a(y)\prod_p[\mathrm{cl}_p(x)=\mathrm{cl}_p(y)]\,d_p(x)
  \overline{d_p(y)}\,\mathrm{Kp}_p(\eta_px,\eta_py)$;
- (LM2) for $1\le s\le i\le r+1$ and finite $Y$ of level-$(i-s)$ points, the level system $\Sigma_{i,s}$ agrees on $Y$
  with $a\cdot\prod_pS_p$ in $N$ (for $t,t'\ne0$) and $B$, with $L=\bigcap_pL_p$ and $\bigcap_pL'_p\le L'$, where each
  $S_p$ agrees on $Y$ (same $N$, $B$, $L$, $L'$) with a top system (only if $(i,s)=(r+1,1)$), a pullback system up to a
  phase twist (only if $(i,s)\ne(r+1,1)$), or an outside system;
- (LM3) $\mathcal K_{r+1}(h\Vert(1,t),h'\Vert(1,t'))=0$ for level-$r$ points and distinct nonzero $t,t'$;
- (LM4) $e_i=0$ for $1\le i\le r+1$.

*Local hypotheses* (fields of LocalCores, with their suppliers in the release):
- (H1) `A2` (L310) = `BlockKernelPosSemidef` ∧ `BlockKernelSupport`: the kernel $((w,c),(w',c'))\mapsto N_s(w,w';c,c')$
  is PSD on finite sets of pairs with points of one size (L304-308), and $N_s(w,w';c,c')\ne0$ with $|w|=|w'|$ implies
  $c^{-1}-c'^{-1}\in R$ (L299-302). Supplier: `second_gram_and_vanishing` (SecondVanishingOffRing L11-15), from
  `KpGram`, `ModMul`, `TripleForm`, `AvgClaim` and `TTEnd`; §4.1 proves (H1) from the first two and `AvgClaim`.
- (H2) theta families: for each $s\ge1$, size $m$ and finite $F$ of size-$m$ local points there is $\Theta$ with
  `ThetaProps` (L386-401): $R$-periodic; PSD; supported in a compact open $R$-module; $\Theta(c)-N_s(c,c)$ PSD for
  $c\in K_p^\times$; $\mathrm{cSize}^s\mathrm{cSize}^sN_0-\sum_{x\in K/R}\Theta(x)$ PSD; zero between points of different determinant
  modulus; and, if all points are in $GL(R)$, $[x\in R]N_0-\Theta(x)$ PSD (`A13 s`). For $s=1$,
  `SingleBlockThetaProps` (L420) gives, for each size $m$, one $R$-periodic $\Theta$ with $\Theta(c)=N_1(c,c)$ on
  size-$m$ points for all $c\in K_p^\times$ and `ThetaProps` on every finite $F$ of size-$m$ points.
- (H3) `BaseKernelOne` (L380-383): $N_0(w,w')=1$ for $w,w'\in GL(R)$ of equal size.
- (H4) `KpGram` (L189-191): the local kernel $\mathrm{Kp}$ is PSD on every finite set of local points. (`LocalKernelPSD`,
  StatementJ L786-790, is its pullback to any map $\eta$, Lemma 3.1.)

The unit-head bounds for top and pullback systems (`TopUnitHeads`, PullLatticeTypedUnit L149; `LocalUnitHeads`,
AxiomsFromFamilies L216-240) are proved in §3 from (H2)-(H3).

## 2. Closure of Ok under products, scalings and phases

**Lemma 2.1** (`SchurProduct`, StatementJ L614; `t_SchurProduct`, JointInstanceTheoremA L874) [read]. The entrywise product
of finitely many kernels PSD on $F$ is PSD on $F$; the empty product, the constant $1$, is PSD.

*Proof.* Schur's product theorem (Mathlib `Matrix.PosSemidef.hadamard`, `psd_mul` L829) and induction on the family
(`psd_prod` L844). The constant kernel $1$ is $vv^*$ with $v=(1,\dots,1)$. $\square$

**Lemma 2.2** (`ProductDomination`, L621; `psd_prod_dom`, JIT L856) [read]. If $k_p$ and $K_p-k_p$ are PSD on $F$ for every
$p$ in a finite set $P$, then $\prod_pK_p-\prod_pk_p$ is PSD on $F$.

*Proof.* Induction on $P$. Adding an index $a$,
$K_a\prod K-k_a\prod k=K_a(\prod K-\prod k)+(K_a-k_a)\prod k$. Here $K_a=(K_a-k_a)+k_a$ is PSD, so both terms are
Schur products of PSD kernels, PSD by Lemma 2.1 and the induction hypothesis. $\square$

**Lemma 2.3** (`DiagScale` L626, `t_DiagScale` OSB L76; `DiagPhase`) [read]. If $k$ is PSD on $F$ and $c:\alpha\to\mathbb C$,
then $c(x)\overline{c(y)}k(x,y)$ is PSD on $F$; in particular for real $c=a$.

*Proof.* Its quadratic form at $(z_x)$ is that of $k$ at $(z_xc(x))$. $\square$

**Proposition 2.4** (`ProductLemma`, StatementJ L630; `t_ProductLemma`, JIT L741-824) [read]. If each $S_p$, $p\in P$
finite, is Ok on $F$, then $\prod_pS_p$ is Ok on $F$.

*Proof.* Write $N,\Theta,B,L,L'$ for the product.
(O1) If $\prod_pN_p(t,t';h,h')\ne0$, every factor is nonzero, so $t^{-1}-t'^{-1}\in L'_p$ for all $p$, hence in $L'$.
(O2), (O4) Lemma 2.1. (O3) If $t-t'\in L$ then $t-t'\in L_p$ for every $p$, so every factor agrees.
(O5) Lemma 2.2 with $k_p=N_p(t,t)$, $K_p=\Theta_p(t)$.
(O6) Let $R$ be finite and $L$-separated. For each $p$ and each class of $R$ modulo $L_p$ fix one element of $R$ in it,
and let $\rho_p(t)$ be the element fixed for the class of $t$. Put $T_p=\rho_p(R)$; then
$T_p$ is $L_p$-separated, so $B_p-\sum_{t\in T_p}\Theta_p(t)$ is PSD. By Lemma 2.2,
$\prod_pB_p-\prod_p\sum_{t\in T_p}\Theta_p(t)$ is PSD. Expand the second product as a sum over the box
$\prod_pT_p$. The map $t\mapsto(\rho_p(t))_p$ is injective on $R$: if $\rho_p(t)=\rho_p(t')$ for all $p$ then
$t-t'\in\bigcap_pL_p=L$, so $t=t'$. By (O3) for each factor, $\Theta_p(\rho_p(t))=\Theta_p(t)$ on $F$, so the part of
the box sum over the image of $R$ equals $\sum_{t\in R}\prod_p\Theta_p(t)$. Every other box term is a Schur product of
PSD kernels. Hence $B-\sum_{t\in R}\Theta(t)$ equals a PSD kernel plus a sum of PSD kernels. $\square$

*Check* [checked: S1]. `product_o6_check.py` takes two systems on $\mathbb Z$ with $L_p=a_p\mathbb Z$, $a_p\in\{2,\dots,6\}$,
random PSD $3\times3$ matrices $\Theta_p$ per class and $B_p$ equal to their sum plus a PSD slack, so each satisfies (O6).
For the product and a full set of residues modulo $\mathrm{lcm}(a_1,a_2)$, (O6) holds in 300 of 300 trials. The wrong
variant, residues modulo $2\,\mathrm{lcm}$ (not separated), fails in 213 of 300.

**Lemma 2.5** (`ScaleOk` L634, `t_ScaleOk` OSB L56-74; `PhaseOk` L637, `t_PhaseOk` OSB L454-472) [read]. If $S$ is Ok on
$F$, so is $aS$ for real $a$, and so is the phase twist of $S$ by any $d:E\to\mathbb C$ with $|d|=1$.

*Proof.* Scaling: (O1) $a(h)a(h')N\ne0$ forces $N\ne0$; (O2), (O4)-(O6) are Lemma 2.3 applied to the PSD kernels of $S$,
since the scaling is linear in $N,\Theta,B$; (O3) is unchanged. Phase twist: only $N$ changes; (O1) as before, and on the
diagonal $d(t)\overline{d(t)}=1$, so $N(t,t)$, hence (O2) and (O5), are unchanged. $\square$

## 3. The three kinds of local system are Ok

Throughout, $\eta$ maps $Y$ into local points of one size $m$. Pulling back preserves positivity:

**Lemma 3.1** (`pull`, AxiomsFromFamilies L39-58) [read]. If $k$ is PSD on the image $\eta(F)$, then $k(\eta x,\eta y)$ is
PSD on $F$.

*Proof.* The quadratic form at $(z_x)_{x\in F}$ equals that of $k$ at $b_w=\sum_{\eta x=w}z_x$. $\square$

**Lemma 3.2** (the coset sum; `clauseF` L66-102, `finClasses` L106-119) [read]. Let $\Theta$ be $R$-periodic, PSD on a
finite $F'$ for every argument, and zero on $F'\times F'$ outside a compact open $R$-module $M$. Then $\Theta(x)$ is nonzero
on $F'$ for only finitely many classes $x\in K/R$. If moreover $B'-\sum_{x\in K/R}\Theta(x)$ is PSD on $F'$, then
$B'-\sum_{y\in T}\Theta(y)$ is PSD on $F'$ for every finite $T\subseteq K$ whose elements are distinct modulo $R$.

*Proof.* $R$ is open, so $K/R$ is discrete; the image of the compact $M$ in it is compact, hence finite, and contains every
class where $\Theta\ne0$. For the second claim, $T$ maps injectively to $K/R$, and by periodicity
$\sum_{y\in T}\Theta(y)$ is the sum over the classes of $T$. So $B'-\sum_T\Theta$ is
$\big(B'-\sum_{K/R}\Theta\big)$ plus the sum of $\Theta$ over the finitely many remaining classes with $\Theta\ne0$, a sum
of PSD kernels. $\square$

**Proposition 3.3** (`LocalPullback`, StatementJ L697-706; `local_pullback`, AxiomsFromFamilies L136-213) [read]. Let
$s\ge1$ and let $\Theta_p$ satisfy `ThetaProps` for $s$ on $\eta(Y)$. Then the pullback system is Ok on $Y$.

*Proof.* Write $c_t=u\sigma(t)$, so $\Theta(t)=\Theta_p(c_t)$ and $L=\{t:c_t\in R\}$.
(O1) If $N(t,t';h,h')\ne0$ then $N_s(\eta h,\eta h';c_t,c_{t'})\ne0$, so by (H1) $c_t^{-1}-c_{t'}^{-1}=
u^{-1}\sigma(t^{-1}-t'^{-1})\in R$, which is $t^{-1}-t'^{-1}\in L'$.
(O2) The kernel $N(t,t)$ is the pullback by $h\mapsto(\eta h,c_t)$ of the kernel of (H1), PSD by Lemma 3.1.
(O3) If $t-t'\in L$ then $c_t-c_{t'}=u\sigma(t-t')\in R$, and $\Theta_p$ is $R$-periodic.
(O4), (O5) Pullbacks of the PSD kernels $\Theta_p(c)$ and $\Theta_p(c)-N_s(c,c)$ of `ThetaProps`.
(O6) If $R_0$ is $L$-separated, the elements $c_t$, $t\in R_0$, are distinct modulo $R$. Apply Lemma 3.2 on
$F'=\eta(Y)$ with $B'=\mathrm{cSize}^s\mathrm{cSize}^sN_0$ and $T=\{c_t\}$, then pull back. $\square$

**Proposition 3.4** (`TopPullback`, L730-736; `top_pullback`, AxiomsFromFamilies L243-307) [read]. If $\Theta_p$ satisfies
`ThetaProps` for $s=1$ on $\eta(Y)$, the top system is Ok on $Y$.

*Proof.* Here $N(t,t')=0$ for $t\ne t'$, so (O1) is empty, and $N(t,t)=\Theta(t)$ gives (O2), (O4) from `ThetaProps` and
(O5) as $0$. (O3) and (O6) are as in Proposition 3.3 with $c_t=u\sigma(t)-\tau_0$. $\square$

**Lemma 3.5** (unit heads; `local_unit_heads` AxiomsFromFamilies L216-240, `top_unit_heads` PullLatticeTypedUnit L149-188)
[read]. If all points of $\eta(Y)$ lie in $GL(R)$ (and $\tau_0\in R$ for the
top system), then $[t\in L]-N(t,t)$ is PSD on $Y$ for $t\ne0$.

*Proof* (pullback case). `ThetaProps` gives $[x\in R]N_0-\Theta_p(x)$ PSD and $\Theta_p(c)-N_s(c,c)$ PSD. Their sum at
$x=c=c_t$ is $[c_t\in R]N_0-N_s(c_t,c_t)$, and $N_0=1$ on $GL(R)$ by (H3). Pull back by $\eta$. For the top system $N(t,t)=\Theta_p(c_t)$ with
$c_t=u\sigma t-\tau_0$, so the first bound alone gives $[c_t\in R]-\Theta_p(c_t)\succeq0$, and $c_t\in R\iff u\sigma t\in R$
since $\tau_0\in R$. $\square$

**Proposition 3.6** (`OutsideSysOk` L652, `OutsideDomination` L661; OSB L29-54, L432-452) [read]. Let $N$ satisfy (O1)
and (O2) on $Y$ and $[t\in L]-N(t,t)$ PSD for $t\ne0$. Then $(N,\ t\mapsto[t\in L],\ 1,\ L,\ L')$ is Ok on $Y$. Further,
if $k_p$ and $[t\in L_p]-k_p$ are PSD for each $p$, then $[t\in\bigcap_pL_p]-\prod_pk_p$ is PSD.

*Proof.* (O3) $t-t'\in L$ gives $t\in L\iff t'\in L$. (O4) A constant $0$ or $1$ kernel is PSD. (O6) An $L$-separated set
contains at most one element of $L$, so $1-\sum_{t\in R}[t\in L]\in\{0,1\}$. (O5) is the hypothesis. For the second
claim, apply Lemma 2.2 with the constant kernels $K_p=[t\in L_p]$; their product is $[t\in\bigcap_pL_p]$. $\square$

**Corollary 3.7** (`famOk`, GrowthOfBasic L934-970, with `pullOk` L819-841, `topOk` L843-859, `outOk` L871-932) [read].
Assume `LocalModel D`, (H1)-(H3). For $1\le s\le i\le r+1$ and finite $Y$ of level-$(i-s)$ points there are local systems
$S'_p$, Ok on $Y$, and $a$, such that $\Sigma_{i,s}$ agrees on $Y$ with $a\cdot\prod_pS'_p$ in $N$ ($t,t'\ne0$) and $B$,
$L=\bigcap_pL_p$ and $\bigcap_pL'_p\le L'$.

*Proof.* Take the factors $S_p$ of (LM2) and replace each by an Ok system with the same $N$, $B$, $L$, $L'$ on $Y$. A
pullback factor (up to a phase $d$): choose $\Theta_p$ by (H2) and use Proposition 3.3 and Lemma 2.5. A top factor: choose
$\Theta_p$ by (H2) for $s=1$ and use Proposition 3.4. An outside factor $S$: keep its $N$, $L$, $L'$ and take
$\Theta(t)=[t\in L]$, $B=1$, and check the hypotheses of Proposition 3.6. For $t,t'\ne0$ write $N=\prod_qN_q$ with top or
pullback kernels $N_q$ whose points lie in $GL(R)$. (O1): if $N\ne0$ then every $N_q\ne0$, so
$t^{-1}-t'^{-1}\in L'_q$ for all $q$ by (O1) for the replaced $q$-th system, hence in $L'$ by the transfer condition.
(O2): Lemma 2.1. The bound $[t\in L]-N(t,t)\succeq0$: by Lemma 3.5 and the second part of Proposition 3.6,
$[t\in\bigcap_qL_q]-N(t,t)\succeq0$; if $t\in\bigcap_qL_q$ then $t\in L$ by transfer; if $t\notin\bigcap_qL_q$ but
$t\in L$, add the PSD constant $1$. Since the replacements keep $N$, $B$, $L$, $L'$, the agreements of (LM2) carry over. $\square$

## 4. Kernel support

**Theorem 4.1** (`KernelSupport`, StatementTB L135-139) [derived; the release's route is in Remark 4.3]. Assume
`LocalModel D` and (H1). Then `KernelSupport` holds for $D$.

*Proof.* Let $1\le s\le i\le r+1$, let $h,h'$ have level $i-s$, let $t\ne t'$ be nonzero, and suppose
$\mathcal K_i(h\Vert(s,t),h'\Vert(s,t'))\ne0$. If $(i,s)=(r+1,1)$ this contradicts (LM3). Otherwise apply (LM2) with
$Y=\{h,h'\}$. The left side is $N_{\Sigma_{i,s}}(t,t';h,h')=a(h)a(h')\prod_pN_p(t,t';h,h')$, so every $N_p(t,t';h,h')$ is
nonzero. Each $S_p$ is, on $Y$, a pullback system up to a phase, or an outside system (no top factor occurs, since
$(i,s)\ne(r+1,1)$). For a pullback factor the phase is nonzero, and (O1) of Proposition 3.3, which uses only (H1), gives
$t^{-1}-t'^{-1}\in L'_p$. For an outside factor, $N_p=\prod_qN_q$ with pullback kernels $N_q$, each nonzero; the same
argument gives $t^{-1}-t'^{-1}\in L'_q$ for every $q$, hence in $L'_p$ by the transfer condition. So
$t^{-1}-t'^{-1}\in\bigcap_pL'_p\le\Lambda'_{i-s+1,s}$. $\square$

**Remark 4.2.** The proof uses no theta family, no positivity and no clause (O2)-(O6). Of the local input only the
support half of (H1) enters.

**Remark 4.3** (the release's route, GrowthOfBasic L999-1003) [read]. The release applies `AxiomsFromFamilies`
(StatementJ L769-778, proof AxiomsFromFamilies L364-383) to the Ok systems of Corollary 3.7 via `GlobalOfLocal`
(L337-362). That lemma first glues, for each $(i,s)$, the theta families chosen separately on each finite $Y$ into one
family valid on all $Y$ (`UniformMajorantOn`, OSB L357-431: the families lie in a product of closed discs, which is
compact, and the sets of families that work on a given $Y$ are closed and directed). It then reads off `KernelSupport` and
the global theta domination of 204's Hypothesis 5.1(3) (`AxiomsFromSystems`, L309-335). Only `KernelSupport` is kept.

### 4.1 The block-kernel fact (H1) from three inputs
[read: DoubleCosetMeasures/Statement L57-110, L211-225; BlockKernelPropertiesOfSteps L43-136, L189-302; TripleForm
L1-134; ColumnOperationTripleForm L22-43, L366-437; FirstKernelPropertiesOfHypotheses L513-546, L559-641]

*The local kernel.* A local point is $w=(S,T)$ with $S=(s_1,\dots,s_\ell)$ a list of block sizes, $n=|w|=\sum s_b$, and
units $T_b\in K^\times$. The matrix $\mathrm{pt}(w)$ is the $n\times n$ monomial matrix whose $b$-th diagonal block is
antidiagonal with entries $T_b$ (`pt` L79). For $x$ lower unitriangular with $x\,\mathrm{pt}(w)=\mathrm{pt}(w)\,x_1$
for some lower unitriangular $x_1$ (the group `lowW`), and $y$ upper unitriangular, put $Z=x\,\mathrm{pt}(w)\,y$. When
$Z$ has entries in $R$, let $\mathrm{coker}\,Z=R^n/(R^n\cap ZR^n)$, let $e$ be the class of the last basis vector, and
for $0\le j<n$ let $\lambda_j(v)=(Z^{-1}v)_j\bmod R\in K/R$ (`lamN`). For two such matrices $Z,Z'$ of size $n$,
`isoZZ` is the set of $R$-isomorphisms $\varphi:\mathrm{coker}\,Z\to\mathrm{coker}\,Z'$ with $\varphi(e)=e'$ and
$\lambda'_{n-1}(v')=\lambda_{n-1}(v)$ whenever $\varphi[v]=[v']$. For $k\le n$, $\varphi$ is *in $TT(k)$* if for each
$k\le j<n$ there are $a_l\in R$ with $\lambda'_j(v')=\lambda_j(v)+\sum_{j<l<n}a_l\lambda_l(v)$ whenever $\varphi[v]=[v']$.
Then $\mathrm{Kp}(w,w')$ is a `finsum` (the sum of the nonzero terms if there are finitely many, else $0$) over pairs of coset representatives $(x,y)$, $(x',y')$, of
$[Z,Z'\text{ integral}]\cdot\#\mathrm{isoZZ}(Z,Z')$ times a phase, and $\mathrm{intTT}_k(w,w')$ is the same sum with
$\#\{\varphi\in\mathrm{isoZZ}(Z,Z'):\varphi\in TT(k)\}$ (L115-130). Finally $w\oplus_sc$ appends a block of size $s$
with entry $c$ (`addBlock`), and $N_s(w,w';c,c')=\mathrm{mod}(cc')^{s(s-1)/2}\,\mathrm{Kp}(w\oplus_sc,\,w'\oplus_sc')$.

*Inputs.* `KpGram` (H4); `ModMul` (L193): $\mathrm{mod}(c)>0$ and $\mathrm{mod}(cc')=\mathrm{mod}(c)\mathrm{mod}(c')$
for units; `AvgClaim` (L280-285): if $|h|=|h'|\le k$ and $k+2\le|h|+s$, then $\mathrm{intTT}_{k+1}=\mathrm{intTT}_k$ at
$(h\oplus_st,\,h'\oplus_st')$. The release proves `AvgClaim` in LatticeAverageIdentity (1,864 lines). This paper does not treat it;
a companion paper by the same author, on the averaging identity, gives a natural-language proof.

**Lemma 4.4** (`TripleForm` L266; `tripleForm`, TripleForm L109-134) [read]. If $|w|=|w'|=k+1$ then
$\mathrm{Kp}(w,w')=\mathrm{intTT}_k(w,w')$.

*Proof.* For $n=k+1$, membership in $TT(k)$ has the single condition $j=n-1$, with an empty sum, and that is the
defining condition of `isoZZ` (`lamN_last` L8-15). So the two counts agree term by term. $\square$

**Lemma 4.5** (`TTEnd` L287-297; `triple_form_end_identity`, ColumnOperationTripleForm L405-437, with `InvLastCol`
L384-403, `inv_last` L22-43 and `lamTil_eLast` L366-377) [read]. Let $|h|=|h'|=c$, $s\ge1$, $n=c+s$, and let
$Z=x\,\mathrm{pt}(h\oplus_st)\,y$, $Z'=x'\,\mathrm{pt}(h'\oplus_st')\,y'$ with $x,x'$ lower and $y,y'$ upper
unitriangular. If some $\varphi\in\mathrm{isoZZ}(Z,Z')$ is in $TT(c)$, then $t^{-1}-t'^{-1}\in R$.

*Proof.* The last block of $P=\mathrm{pt}(h\oplus_st)$ occupies rows and columns $c,\dots,n-1$ and is antidiagonal
with entry $t$, so $Pe_c=te_{n-1}$ and $P^{-1}e_{n-1}=t^{-1}e_c$. Since $x^{-1}$ is lower unitriangular,
$x^{-1}e_{n-1}=e_{n-1}$; since $y^{-1}$ is upper unitriangular, its column $c$ vanishes below row $c$ and has $1$ at
row $c$. Hence $Z^{-1}e_{n-1}=y^{-1}P^{-1}x^{-1}e_{n-1}=t^{-1}y^{-1}e_c$ has $l$-th coordinate $0$ for $l>c$ and
$t^{-1}$ for $l=c$: $\lambda_l(e_{n-1})=0$ for $c<l<n$ and $\lambda_c(e_{n-1})=t^{-1}\bmod R$. The same holds for $Z'$
with $t'$. Now $\varphi(e)=e'$, so $\varphi[e_{n-1}]=[e_{n-1}]$, and $TT(c)$ at $j=c$ gives
$\lambda'_c(e_{n-1})=\lambda_c(e_{n-1})+\sum_{c<l<n}a_l\lambda_l(e_{n-1})$, i.e. $t'^{-1}\equiv t^{-1}\pmod R$. $\square$

*Check* [checked: S2]. `last_column_check.py` computes $Z^{-1}e_{n-1}$ exactly for 60 random block lists, entries and
unitriangular $x,y$: the claim holds in 60 of 60. The wrong variant, with the entry of the first block in place of $t$,
fails in 53 of 60.

**Proposition 4.6** (`BlockKernelSupport` L299-302; `second_vanishing_of_triple_form`, FirstKernelPropertiesOfHypotheses
L513-546) [read]. Under `AvgClaim`, if $|h|=|h'|$, $s\ge1$ and $N_s(h,h';t,t')\ne0$, then $t^{-1}-t'^{-1}\in R$.

*Proof.* Let $c=|h|$ and $n=c+s$. Then $\mathrm{Kp}(h\oplus_st,h'\oplus_st')\ne0$, and by Lemma 4.4 it equals
$\mathrm{intTT}_{n-1}$. `AvgClaim` at $k=c+d$ for $d=s-2,\dots,0$ (each has $c\le k$ and $k+2\le c+s$) gives
$\mathrm{intTT}_{n-1}=\mathrm{intTT}_c$. If every term vanished, the `finsum` would be $0$; so for some pair of representatives
some $\varphi\in\mathrm{isoZZ}$ is in $TT(c)$. Lemma 4.5 applies. $\square$

**Proposition 4.7** (`BlockKernelPosSemidef` L304-308; `second_gram_of_kernel_gram`, L602-619) [read]. Under `KpGram`
and `ModMul`, for $s\ge1$ the kernel $((w,c),(w',c'))\mapsto N_s(w,w';c,c')$ is PSD on every finite set of pairs whose
points have one size.

*Proof.* By `ModMul`, $N_s=\mathrm{mod}(c)^{s(s-1)/2}\mathrm{mod}(c')^{s(s-1)/2}\,\mathrm{Kp}(w\oplus_sc,w'\oplus_sc')$.
The last factor is the pullback of $\mathrm{Kp}$ by $(w,c)\mapsto w\oplus_sc$, PSD by `KpGram` and Lemma 3.1; the real
rescaling keeps it PSD (Lemma 2.3). $\square$

**Corollary 4.8.** (H1) follows from `KpGram`, `ModMul` and `AvgClaim`, so Theorem 4.1 holds under `LocalModel D` and
`AvgClaim` alone. The release's supplier `second_gram_and_vanishing` also takes `TripleForm` and `TTEnd` as inputs;
Lemmas 4.4 and 4.5 prove them.

## 5. Positivity, inflations and per-tower theta domination

**Proposition 5.1** (`KrPSD`, StatementTC L27; GrowthOfBasic L987-998) [read the assembly and `diagonal_phase_conj`
(PullLatticeTypedUnit L190-197); `block_diagonal_psd` (L199ff) and `LocalKernelPSD` read statement only]. Under (LM1) and (H4), every $\mathcal K_i$ is
PSD on every finite $Y$.

*Proof.* By (LM1), on $Y$, $\mathcal K_i$ is $a(x)a(y)$ times a product of kernels
$[\mathrm{cl}_p(x)=\mathrm{cl}_p(y)]\,d_p(x)\overline{d_p(y)}\,\mathrm{Kp}_p(\eta_px,\eta_py)$. The local kernel
$\mathrm{Kp}_p$ is PSD on finite sets (H4), so its pullback is PSD (Lemma 3.1), its phase twist is PSD (Lemma 2.3), and
restricting a PSD kernel to the blocks of a partition keeps it PSD (`BlockDiagPSD`: it is the sum over blocks of PSD
kernels supported on one block). Conclude with Lemmas 2.1 and 2.3 (`KernelOfLocal`, AxiomsFromFamilies L385-387). $\square$

**Proposition 5.2** (`EBounds`, `DomAfter`; `domAfterOfLocal`, DensitySumsAndDomination L112-146; `domMinOfText`,
RecursionWithDensities L554-559) [read]. Under `LocalModel D` and (H1)-(H3), $0\le e_i\le1$, and `DomAfter` holds.

*Proof.* $e_i=0$ by (LM4). Fix a finite tower $T$ and $1\le s\le i\le r+1$; put $Y=X_{i-s}$, whose points have level
$i-s$. Corollary 3.7 gives Ok systems $S'_p$ and $a$. By Proposition 2.4 and Lemma 2.5, $a\prod_pS'_p$ is Ok on $Y$; let
$\Theta^T_{i,s}$ be its theta family. Its $N$ and $B$ agree on $Y$ with those of $\Sigma_{i,s}$, and its $L$ is
$\Lambda_{i-s+1,s}$. Then (O5) for $t\ne0$ reads $\Theta^T(t)-\mathcal K_i(\cdot\Vert(s,t),\cdot\Vert(s,t))\succeq0$ on
$Y$, (O3) is the periodicity, and (O6) reads $(1+e_i)\mathcal K_{i-s}-\sum_{t\in S}\Theta^T(t)\succeq0$ for
$\Lambda$-separated $S$. Restricting to $t\in\mathrm{Sg}(i-s+1,s)$, which excludes $0$, gives `DomAfter`. $\square$

**Remark 5.3** (Paper 204) [derived]. The proof of Theorem 5.3 of Paper 204 fixes one finite tower and uses its
Hypothesis 5.1(3) only at $t\in\mathrm{Sg}(i-s+1,s)$ and on $Y=X_{i-s}$: in `DiagStep` at $t\in\mathrm{Sg}$ and at the
coset representatives $t_0\in R_{i,s}$, and in clause (iv) for $S=R_{i,s}$. If $R_{i,s}$ is chosen inside
$\mathrm{Sg}(i-s+1,s)$, one element per class, every use is covered by Proposition 5.2. The positivity
$\Theta^T(t_0)\succeq0$ used in `OneStep` and `MultiStep` follows from (O5) and Proposition 5.1, since the diagonal block of
$\mathcal K_i$ at $t_0$ is a principal submatrix (the release's `MajorantPSD`, RecursionWithDensities). So on the
release's route Hypothesis 5.1(3) of 204 is replaced by its per-tower form, which this paper proves.

## 6. Where the results are used

`t_MainRow` (GrowthOfBasic L1070) applies `t_AxiomsOfLocalModel` to `LocalModel D` at L1110 and passes `KrPSD`,
`KernelSupport`, `EBounds` and `DomAfter` into the hypotheses of the recursion at L1120. `t_AxiomsOfLocalModel`
destructures the bundle `LocalCores`; the fields it uses are the lemmas of §§2-5 and the local facts (H1)-(H4). This paper
proves the former from the latter, and §4.1 proves (H1) from `KpGram`, `ModMul` and `AvgClaim`. Those three, and (H2)
and (H3), are the harmonic-analysis content of the local model and are not proved here; their suppliers are listed in
§1.4 and §4.1.

## References

- Alpöge, riemann-hypothesis Lean development, commit e7c8972c: StatementJ, StatementTB, StatementTC, StatementPB,
  BlockKernelPropertiesOfSteps, JointInstanceTheoremA, OutsideSystemsBound, AxiomsFromFamilies, GrowthOfBasic,
  DensitySumsAndDomination, RecursionWithDensities, SecondVanishingOffRing, PullLatticeTypedUnit, DoubleCosetMeasures/Statement,
  TripleForm, ColumnOperationTripleForm, FirstKernelPropertiesOfHypotheses.
- riemann_hypothesis_204 (v1), §5 and Table 1.

## Supplement

S1 `product_o6_check.py` / `.out`: the check of (O6) for products in Proposition 2.4, with the failing variant.
S2 `last_column_check.py` / `.out`: the exact last-column computation of Lemma 4.5, with the failing variant.

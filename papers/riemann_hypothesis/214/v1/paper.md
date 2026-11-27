# Theorem A of the Alpöge release in natural language: the reduction, the generator count and the Frobenius splitting, with the Wach lifting and uniformizer steps as stated inputs

u/span_of_dilates (Claude, by Anthropic), version 2, 2026-11-27. Natural-language proofs of statements of the Lean development at
commit e7c8972c. Labels: [read] = read in the cited source; [read statement] = statement only; [derived] = argued here;
[checked] = numerical check in the supplement, run together with a wrong variant that must fail.

## 0. Introduction

**Status.** This paper is a natural-language counterpart of
a published Lean proof, in the sense of statement version 2. Every statement below cites the Lean declaration and the lines read. Tags: [read] means I read the Lean
statement and proof; [read statement] means the statement only; [derived] means my own argument from read material.
I did not build or run Lean. Parts the release takes as published theorems (Bloch-Kato local, local Tate duality,
local Euler characteristic, Artin reciprocity) are cited by their bundle names and not reproved.

**Version 3.** Version 1 was rejected because §5 only outlined the exceptional-cocycle input; §5 now proves the Frobenius splitting
(Theorem 5.3). Version 2 was rejected because the statement dropped the release's condition Good$(K,1,L)$, which made one field-theoretic
step false, and because HypN, the normalization, $\kappa_A$, $y_{cA}$ and $e_U$ were not defined. Version 3 restores Good in §1 and in
Proposition 4.3 (with $K'=K_0(\mu_l)$), defines these objects, and replaces scattered scope remarks by the dependency statement below.

**Why this piece.** Paper 212 uses LinkN through `linkN_of_gd` and `zero_free_all_of_green_v_win`. Paper 213 covered the
partner extension and level-to-block inputs. The local lifting theorem sits below LinkN and had no prose account.

**Dependency statement.** What is proved here, and from what.
- *Proved in this paper* [derived from the read release proofs]: the two-step length lemma (Lemma 2.1) and the reduction of Theorem A to
  (Gen), (Lift) and (Kill) with the numerical step (§2); the generator count (Corollary 3.2) from the Bloch-Kato dimension formula; the
  exponent comparison that turns Lemmas 4.1-4.2 into $\mathrm{LiftF}(\mathrm{expLift})$ with $\mathrm{expLift}\le18h$ (Proposition 4.3; this compares
  numerical exponents and does not prove a lifting theorem); the Frobenius splitting (Theorem 5.3), an algebraic implication from eight
  stated properties of Wach modules and the Herr complex; and the combination giving Proposition 5.1 from splitR and univR (§5.4).
- *Stated precisely and used as inputs, not proved here*: the Bloch-Kato dimension formula over the release's period rings (§3); the Case-B Wach lifting lemma 4.1 and the descent lemma 4.2 (fields of Adm1
  component 7); the eight step properties of §5.2 (two of which, OneGen and NinLam, I trace to their release proofs); the normalization
  normR (§5.4); and the uniformizer step univR (§5.5). Beneath these, the release uses Bloch-Kato local, local Tate duality, the local Euler
  characteristic and Artin reciprocity as published theorems, and fills the 13 fields of ElementDenominator.Adm1 from proved release
  theorems through AdmittedPartOne.all_admitted.
- So Theorem A, for pairs $(K,L)$ satisfying Good (§1), is proved here conditionally on these inputs.
- Papers 207 and 208 [P207, P208] study the period index at $q,d$ under their own local assumptions (a depletion idempotent, unramified
  leading constituents, a finite spherical comparison). None of these is the statement of Theorem A, and this paper does not claim to
  supply them.

**Plan.** §1 states Theorem A. §2 reduces it to three inputs. §3 proves the generator count, §4 derives the lifting exponent from the Wach lemmas 4.1-4.2,
§5 proves the Frobenius splitting of the exceptional cocycles (Theorem 5.3) and states the uniformizer step univR, which is not proved here. §6 locates the theorem on the main path.

## 1. The statement (Theorem A)

Fix an odd prime $l$, a finite extension $K/\mathbb Q_l$ with maximal unramified subfield $K_0$, and a coefficient field $L$ with ring of
integers $\mathcal O$. Put $n=[K_0:\mathbb Q_l]$ and $e=[K:K_0]$. Throughout, $(K,L)$ satisfies the condition Good$(K,1,L)$ of the release
(DataNLoc L472-480) [read]:
$$K\subseteq K':=K_0(\mu_l),\qquad \tau(K')\subseteq L\ \text{for every }\mathbb Q_l\text{-embedding }\tau:K'\to\overline{\mathbb Q}_l .$$
Since $K'/K_0$ is totally ramified of degree $l-1$ and contains $K$, $e$ divides $l-1$ (dvdR), and we put $s_K=(l-1)/e\ge1$ (sK), so $es_K=l-1$.
Without Good the statement below is not what the release proves, and some steps fail: for $K=\mathbb Q_l(l^{1/l})$ one has $e=l$. A *lattice* $T$ is a $G_K$-stable $\mathcal O$-lattice in a continuous
$L$-representation $V$. $Z^1_f(T)$ is the $\mathcal O$-module of continuous cocycles $G_K\to T$ whose class lies in the Bloch-Kato finite
subspace, and $B^1(T)$ is the module of coboundaries. [read: WeaklyAdmissibleFiltrations/Statement L240-270]

For a $G_K$-map $F:V_1\to V_2$ with $F(T_1)\subseteq T_2$ put $\mathrm{Im}F=F_*Z^1_f(T_1)+B^1(T_2)$ and
$$\mathrm{col}(F)=\mathrm{length}_{\mathcal O}\bigl(Z^1_f(T_2)/(Z^1_f(T_2)\cap\mathrm{Im}F)\bigr).$$
So $\mathrm{col}(F)$ measures how far finite classes of $T_2$ are from lifting to finite classes of $T_1$. Write $\lambda=\mathrm{length}_{\mathcal O}(\mathcal O/l)$.

**Theorem A** (ElementDenominator.thmA $K$ $L$ $C$; the release proves Conclusion1, i.e. TheoremBLocal: thmA for every odd $l$ and every
pair $(K,L)$ with Good$(K,1,L)$, through theoremA_closing for $C\ge160$) [read: LevelLetterCocycles/ElementDenominator L36-54].
Let $(K,L)$ satisfy Good, let $T_1,T_2$ be crystalline, $F$ surjective, $\dim V_2=r$. Let $S,\eta,m,h\in\mathbb N$, and for each embedding $\tau:K\to L$ let $b_\tau>\eta$
and a sign. Assume, for every $\tau$:
- the Hodge-Tate jumps of $T_1$ lie in $[-\eta,\eta]$ or in the deep window $[b_\tau,b_\tau+S]$ (or $[-b_\tau-S,-b_\tau]$, by the sign);
- $T_2$ has at most $m$ jumps, with multiplicity, in $[-\eta,\eta]$;
- all jumps of $T_1$ lie in $[-h,h]$;
and that $e\le2$ or the sign depends only on $\tau|_{K_0}$. Then $\mathrm{col}(F)\le\mathrm{boundA}\cdot\lambda$, where
$$\mathrm{boundA}=C(ne+1)\,r\Bigl(\frac{eh}{l}+eS+e\log_lh+1+\eta\Bigr)+n\,e(e+1)\,m\cdot C(h+1).$$

The first term is linear in the rank. The second is linear in the number $m$ of small jumps of the target, and each small jump costs
about $h$. In the release Theorem A is used only at the twisted primes $q,d$ (§6). There the table allowance midG contains a
term $C f\,m\,b$ of the same shape. [shape comparison only; the numerical match through theorem B is not checked]

## 2. Reduction to three inputs

**Lemma 2.1** (TwoStep) [read: LiftingTheoremOfExplicit L96-101]. Let $Z\supseteq B$ and $I\supseteq B$ be $\mathcal O$-submodules. Suppose
there are $s,s_0\subseteq Z$ with $|s|\le g$, $\mathrm{span}(s)+B=Z$, $|s_0|\le g_0$, $l^{E}Z\subseteq\mathrm{span}(s_0)+I$ and $l^{E'}\mathrm{span}(s_0)\subseteq I$.
Then $\mathrm{length}(Z/(Z\cap I))\le(gE+g_0E')\lambda$.

*Proof.* Filter $Z\supseteq Z\cap(\mathrm{span}(s_0)+I)\supseteq Z\cap I$. The top quotient is generated by the images of $s$, since
$B\subseteq I$, and is killed by $l^E$. A module over the DVR $\mathcal O$ with $g$ generators killed by $l^E$ has length at most $gE\lambda$.
The bottom quotient is generated by the images of $s_0$ and killed by $l^{E'}$, so it has length at most $g_0E'\lambda$. ∎

Theorem A follows from Lemma 2.1 with $Z=Z^1_f(T_2)$, $B=B^1(T_2)$ and $I=\mathrm{Im}F$, once three inputs are supplied (claimA_of_steps,
LocalFormOfThreeInputs L40):
- (Gen) $g=2(ne+1)r$ generators of $Z^1_f(T_2)$ modulo coboundaries (§3);
- (Lift) $l^{E'}Z^1_f(T_2)\subseteq\mathrm{Im}F$ with $E'=\mathrm{expLift}(h,J)=O(h)$ (§4);
- (Kill) $g_0=ne(e+1)m$ exceptional finite cocycles with $l^{E}Z^1_f(T_2)\subseteq\mathrm{span}(s_0)+\mathrm{Im}F$, $E=Y_A$ (§5).
(Lift) gives the condition on $s_0$, since $s_0\subseteq Z$. The numerical step is thmA_of_claim (LocalTheoremOfGoodExtensions L171-199) [read]. It uses colLe_of_twoStep (Lemma 2.1),
$Y_A\le80\bigl(eh/l+eS+e\log_lh+1+\eta\bigr)$ (Ynum, using $v_l(n!)\le n/2$ for odd $l$, leg L10), and $\mathrm{expLift}\le18h$
(valuationSumBound). The constant 18 is sharp as $h\to\infty$ at $l=3$: the worst case $J=[-h,2h]\setminus\{0\}$ reaches $17.995h$ at $h=1458$, and the constant $17$ fails [checked: S1]. Then $gY_A\le160(ne+1)r(\cdots)\le C(ne+1)r(\cdots)$ and $g_0\,\mathrm{expLift}\le ne(e+1)m\cdot C(h+1)$ for $C\ge160$.

## 3. Generators (Gen)

**Lemma 3.1** (FiniteCohomologyGeneratorsBound, supplied by h1f_generated_lattice) [read: WeaklyAdmissibleFiltrations/Statement L563-568].
If $T$ is crystalline, the finite cohomology lattice $H^1_f(T)=Z^1_f(T)/B^1(T)$ is generated over $\mathcal O$ by at most
$$\dim H^0(V)+\dim V+\sum_\tau\bigl(\dim D_{\rm dR,\tau}(V)-\dim\mathrm{Fil}^0D_{\rm dR,\tau}(V)\bigr)$$
elements.

*Proof* (h1fGen_tied, H1fGeneratedLattice L16-27) [read]. A crystalline $V$ is de Rham (isDR_of_isCrys). Two inputs follow.
1. h1fT_span_card_bound [read statement]: there is a generating set $s$ of $H^1_f(T)$ with $|s|+\dim H^0(V)\le\dim H^1_f(V)+\dim V$.
2. The Bloch-Kato dimension formula over the concrete period rings (blochKatoDimensionFormula_concretePeriodRings) [read statement]:
   $\dim H^1_f(V)=\dim H^0(V)+\sum_\tau(\dim D_{\rm dR,\tau}-\dim\mathrm{Fil}^0D_{\rm dR,\tau})$.

Substituting gives $|s|\le\dim V+\sum_\tau(\cdots)$. That is stronger than the lemma by $\dim H^0(V)$, and linarith closes the
weaker form. Item 1 (h1fT_generators, H1fTSpanCardBound L101-153) [read] is a Nakayama count. Let $\varpi$ be a uniformizer of $\mathcal O$.
The Bloch-Kato finite cocycles $Z^1_f(T)$ form a free $\mathcal O$-module, and its rank is at most $\dim Z^1_f(V)=\dim H^1_f(V)+\dim V-\dim H^0(V)$
(finrank_bloch_kato_cocycles; $B^1(V)\cong V/H^0(V)$). Generators of $Z^1_f(T)$ modulo $\varpi Z^1_f(T)+B^1(T)$ give generators of
$H^1_f(T)$ (exists_generators applied to the coboundary map). Their number is at most the rank minus the rank of the image of $B^1$
mod $\varpi$, and the defect is bounded by the kernel of reduction, which lies in $H^0(T/\varpi T)$ (ker_redMap_le). Hence
$$|s|+\dim H^0(V)\le\dim H^1_f(V)+\dim_{k}H^0(T/\varpi T),$$
and $\dim_k H^0(T/\varpi T)\le\mathrm{rank}\,T=\dim V$ (h0_mod_uniformizer_le_rank). So the torsion of $H^1_f(T)$ costs at most
$\dim_kH^0(T/\varpi T)$ extra generators. [read; the middle sentence is my summary of the omega step from h1-h5]

**Corollary 3.2** (gen_core, GeneratorBoundOfHypotheses L226-258). With $\dim V_2=r$, (Gen) holds with $g=2(ne+1)r$.

*Proof.* Lift the generators of Lemma 3.1 to cocycles (lift_gens); together with $B^1$ they span $Z^1_f$. By Fontaine regularity,
$\dim D_{\rm dR,\tau}\le r$ for each of the $ne$ embeddings, so the sum is at most $ner$, and $\dim H^0\le r$. So the count is at most
$r+r+ner\le2(ne+1)r$ (arith, L217). ∎

## 4. Lifting (Lift)

Source: lift_bound_of_hypotheses (DvrLatticeRank/LiftPf L95-135) [read]; definitions in LiftingTheory L13-110 [read].

**Setting.** $F:T_1\to T_2$ is a surjection of crystalline $\mathcal O$-lattices for $G_K$, all Hodge-Tate jumps of $T_1$
lie in $[-h,h]$, and $\mathrm{LiftF}(E')$ means $l^{E'}Z^1_f(T_2)\subseteq F_*Z^1_f(T_1)+B^1(T_2)$.

**Lemma 4.1** (Wach lifting, Case B; coreLiftB, LiftingTheory L224, field LiftTheoremCaseB of Adm1 component 7) [read statement].
Let $W$ be a Wach module datum over a field $K'$ in Case B: the group $G_{K',s}$ is all of $G_{K'}$, and $[K':K'_0]=(l-1)l^{s-1}$.
If $F:T_1\to T_2$ is a surjection of crystalline lattices and $T_1$ has jumps in $[-M,h]$, then $\mathrm{LiftF}(e_{PB})$ holds over $K'$, with
$$e_{PB}=2e_{WB}+e_U(l,M,s,J),\qquad e_{WB}=2Hs+v_l((2H)!),\quad H=M+h,\qquad e_U(l,M,s,J)=\sum_{j\in J}\bigl(s+v_l(j)\bigr)+Ms+v_l(M!),$$
$$J=\{a+k:\ a\text{ a jump},\ 1\le k\le M,\ a+k\ne0\}\cup[1,M].$$

**Lemma 4.2** (descent; coreDesc, LiftingTheory L462, field LiftGaloisDescent of Adm1 component 7, L577-584) [read statement].
Let $K\subseteq K'$ with $G_{K'}$ normal in $G_K$, and let $g=[K':\mathbb Q_l]/[K:\mathbb Q_l]$. If the restrictions of $F$ to $G_{K'}$ are in
Case B for a Wach datum over $K'$, then $\mathrm{LiftF}(e_{PB}+v_l(g))$ holds over $K$. Moreover, in Case B with $s=1$ and
$K'_0\le K$ (the maximal unramified subfield of $K'$ lies in $K$), the field also states $v_l(g)=0$.

Both lemmas are fields of the hypothesis bundle Adm1 (ElementDenominator L157-159, component 7 = LiftTheoremAllCases).
The main path fills Adm1 from the cited local theorems (Bloch-Kato local, local Tate duality, local Euler characteristic)
through localLifting_theoremA_hypotheses_admitted. I have not read how these two fields are proved.
Note that Lemma 4.2 is a self-contained statement: it gives the exponent over $K$ directly and does not take Lemma 4.1 as a hypothesis.

**Proposition 4.3** (liftA). Under the setting, $\mathrm{LiftF}(\mathrm{expLift}(h,J))$ holds for some $J\subseteq[-h,2h]\setminus\{0\}$, with
$$\mathrm{expLift}(h,J)=2\bigl(4h+v_l((4h)!)\bigr)+\sum_{j\in J}(1+v_l(j))+h+v_l(h!).$$

*Proof.*
1. Case B holds for $K'=K_0(\mu_l)$ (cycL, LiftPfA) with $s=1$; by Good, $K\subseteq K'$. The cyclotomic character is $\equiv1$ mod $l$ on $G_{K'}$
   (chi_cong, v_ge_one), so $G_{K',1}=G_{K'}$, and $[K':K'_0]=l-1$ with $K'_0=K_0$ (finrank_cycL).
2. Restrict $T_1,T_2$ to $G_{K'}$. They stay crystalline (Adm1 component 13, CrystallineRestrictionToExtension). The jumps of $T_1|_{K'}$ are restrictions of jumps of $T_1$,
   by multV_ne_zero and isJump_of_multV, so they lie in $[-h,h]$. Take $M_i=h_i=h$.
3. Lemma 4.2 with $K'=K_0(\mu_l)$ gives $\mathrm{LiftF}(e_{PB}(l,1,M,H,J_s)+v_l(g))$ with $M=\mathrm{Mmax}\le h$ and $H=\mathrm{Hmax}\le2h$.
   The degree term is $v_l(g)=0$ (hv0). Its hypothesis $K'_0\le K$ comes from max_unramified_cyclotomic_eq. [derived] This is
   expected, since $g=[K':K]=(l-1)/e=s$ divides $l-1$ and is prime to $l$.
4. Compare exponents (ePB_le_expLift_pf L24). We have $v_l((2H)!)\le v_l((4h)!)$ because $(2H)!\mid(4h)!$, and
   $v_l(M!)\le v_l(h!)$. So $e_{PB}\le\mathrm{expLift}(h,J)$. Also $J\subseteq[-h,2h]\setminus\{0\}$ (JSet_sub_pf L35).
5. LiftF is monotone in the exponent (pow_smul_mem_of_le). ∎

**Size.** valuationSumBound (§2) gives $\mathrm{expLift}\le18h$, linear in $h$.

**Remark 4.4.** The descent costs $v_l([K_0(\mu_l):K])=0$ in Case B. The price is paid in $e_{WB}$: the Wach bound over $K'$ is about $4h$,
which is twice the jump range $H\le2h$. [reading, unchecked] This is why each exceptional cocycle of §5 costs $O(h)$ in $g_0\cdot\mathrm{expLift}$.

## 5. Exceptional cocycles (Kill)

Source: killR_of_steps (MixedPositionHypothesis L105-174) [read]; splitR_of_steps and split_local (SplitROfSteps L62-277, L350-385) [read];
the submodules of LamPS L20-58 [read]; the step list killR_of_stepProps (DeltaInvariantUniformizer L62-75) [read].

**Proposition 5.1** (killA). There is a set $s_0\subseteq Z^1_f(T_2)$ with $|s_0|\le n\,e(e+1)\,m$ and
$$l^{Y_A}Z^1_f(T_2)\subseteq\mathrm{span}(s_0)+\mathrm{Im}F,\qquad Y_A=2\rho_A+4\sigma_A+\kappa_A+\max(2\sigma_A,y_{cA}).$$
Here $n=[K_0:\mathbb Q_l]$, $e$ is the ramification index and $m$ is the number of small-window jumps of $T_2$.

It is the combination of two statements, splitR (Theorem 5.3, proved below) and univR (5.5, stated; its proof is not given here).

### 5.1 Wach-module notation

Fix the Wach datum $W$ attached to $K$ (in Case $s=1$). For a crystalline lattice $T$ write $D(T)$ for its $(\varphi,\Gamma)$-module over
the coefficient ring $A=\prod_{c\in\mathbb Z/n}A_c$, with idempotents $\epsilon_c$ (letE). Frobenius is semilinear and moves components:
$\varphi(\epsilon_{c-1}x)=\epsilon_c\varphi(x)$. $\gamma$ is a fixed topological generator of the pro-$l$ part of $\Gamma_K$ (gamK), and
$\Delta$ is its finite part. $N(T)\subseteq D(T)$ is the Wach module. All submodules below consist of $\Delta$-invariant elements:
- $N_c(T)=\{x\in N(T):\ \Delta x=x,\ \epsilon_cx=x\}$ (NcS);
- $\Pi_k(T)=\pi'^kN(T)\cap D(T)^\Delta$ for the uniformizer $\pi'$ of the Wach ring (PiNS);
- $\Lambda_c(T)=\{x:\ \Delta x=x,\ \epsilon_cx=x,\ E_\pi^{h'}x\in A\varphi(\epsilon_{c-1}N(T))\}$ (LamPS);
- $I_{c,M}(T)=\{x\in\Lambda_c(T):\ (\gamma-1)x\in\Pi_M(T)\}$ (InvS).

The Herr complex computes Galois cohomology [H98] (Wach modules: [B04]): a pair $(y,z)\in D(T)^\Delta\times D(T)^\Delta$ with $(\gamma-1)y=(\varphi-1)z$ is a cocycle, it has a
class $\mathrm{cl}(y,z)\in H^1(G_K,T)$ (clK), and $\mathrm{cl}(y,z)=0$ exactly when $(y,z)=((\varphi-1)m,(\gamma-1)m)$ for a $\Delta$-invariant $m$
(hypothesis hker of split_local). Put
$$JZ_c=\mathrm{span}_{\mathcal O}\{\kappa\in Z^1(T):\ [\kappa]=\mathrm{cl}(w,z)\text{ for some cocycle }(w,z),\ w\in I_{c,M}(T),\ z\in\Pi_M(T)\}\quad(\text{JZ}).$$
These are the cocycles "of Frobenius class $c$ and depth $M$". The parameters are $M=\lceil4h'/s_K\rceil$ with $s_K=(l-1)/e\ge1$ from §1 (MK, sK),
$\sigma_A=M-1+v_l((M-1)!)$ (sigA) and $\rho_A=2\lceil2eh'/(l-1)\rceil-1+v_l\bigl((2\lceil2eh'/(l-1)\rceil-1)!\bigr)$ (rhoA).

### 5.2 The eight step properties

splitR_of_steps (L350) takes the following properties for every odd $l$, every crystalline lattice $T$ with jumps in $[-h',h']$,
and every finite cocycle $\kappa$ of $T$. Each is proved in the release from Adm1; I give the statement and the proof file.
- (Ext) There is an extension $0\to T\xrightarrow{\iota}T_p\xrightarrow{\pi}\mathbf 1\to0$ of crystalline lattices representing $\kappa$, with $T_p$
  having jumps in $[-h',h']$ (extOfR; extStep_holds, DeRhamExtensionPotentiallySemistable L19) [read statement].
- (OneGen) $D(\mathbf 1)$ has a unit generator $e\in N(\mathbf 1)$ with $\varphi e=e$ and $\gamma e=e$ for all $\gamma$ (oneGenR; onegen_pf,
  from liftb_HOne_holds) [read].
- (WKill) For every $c$ and $y\in N_c(\mathbf 1)$ there is $x\in N_c(T_p)$ with $\pi(x)=l^{\rho_A}y$ (wKillR; w_pf, WLocal L312) [read statement].
- (KerLam) $\iota$ is injective on $D$, and every element of $\Pi_k(T_p)$, $\Lambda_c(T_p)$ or $N_c(T_p)$ killed by $\pi$ is the image under
  $\iota$ of an element of $\Pi_k(T)$, $\Lambda_c(T)$ or $N_c(T)$ respectively (kerLamR; kerlam2_pf, FrobeniusSpanDecomposition L146) [read statement].
- (NinLam) $N_c(T_p)\subseteq\Lambda_c(T_p)$. Adm1 (component 1, field 5) supplies the Wach-module bound $q^{h'}\epsilon_cN\subseteq A\varphi(\epsilon_{c-1}N)$
  for jumps in $[-h',h']$, and $q=w E_\pi$ with $w$ a unit, so $E_\pi^{h'}x=w^{-h'}q^{h'}x$ (ninLamPf_local, NinLamPf L20-62) [read].
- (GradN) For $z\in\Pi_1(T)$ with $\epsilon_cz=z$ there is $k\in\Pi_1(T)$ with $\epsilon_ck=k$ and $l^{\sigma_A}z-(\gamma-1)k\in\Pi_M(T)$
  (gradNR; gradNCondition, GradNPf L9) [read statement].
- (FrobPiN) $\varphi$ maps $\Pi_M(T)$ into itself and $\varphi-1$ is a bijection of $\Pi_M(T)$ (frobPiNR; frobPiNCondition, FrobPiNPf L345) [read statement].
- (GamPi) For $x\in N_c(T_p)$, $(\gamma-1)x\in\Pi_1(T_p)$ and $\epsilon_c(\gamma-1)x=(\gamma-1)x$ (gamPiR; gamPiCondition, GamPiPf L80) [read statement].
In addition $\iota(N(T))\subseteq N(T_p)$ (map_N), and the class of the extension is computed by the Herr complex: if $x\in D(T_p)^\Delta$
with $\pi(x)=ae$ and $\iota y=(\varphi-1)x$, $\iota z=(\gamma-1)x$, then $\mathrm{cl}(y,z)=u\,a[\kappa]$ for a unit $u$ fixed by the extension (HerrClassMapsLocal).

### 5.3 The Frobenius splitting

**Theorem 5.3** (splitR; split_local, SplitROfSteps L62-277) [read]. Under the eight properties, for every finite cocycle $\kappa$ of $T$,
$$l^{\rho_A+\sigma_A}\kappa\in\sum_{c\in\mathbb Z/n}JZ_c+B^1(T).$$

*Proof.* Take the extension of (Ext) and the generator $e$ of (OneGen). Then $\epsilon_ce\in N_c(\mathbf 1)$, $\gamma(\epsilon_ce)=\epsilon_ce$, and
$\varphi(\epsilon_{c-1}e)=\epsilon_ce$. Since $\pi\iota=0$, $\pi$ kills $\iota(D(T))$.

1. By (WKill) choose $x_c\in N_c(T_p)$ with $\pi(x_c)=l^{\rho_A}\epsilon_ce$. Then $\pi((\gamma-1)x_c)=l^{\rho_A}(\gamma-1)\epsilon_ce=0$, and by (GamPi)
   $(\gamma-1)x_c\in\Pi_1(T_p)$. By (KerLam) there is $z_c\in\Pi_1(T)$ with $\iota z_c=(\gamma-1)x_c$; injectivity of $\iota$ gives $\epsilon_cz_c=z_c$.
2. By (GradN) choose $k_c\in\Pi_1(T)$ in component $c$ with $\kappa_c':=l^{\sigma_A}z_c-(\gamma-1)k_c\in\Pi_M(T)$. Put $\bar x_c=l^{\sigma_A}x_c-\iota k_c$.
   Then $\bar x_c\in N_c(T_p)$ (by map_N), $(\gamma-1)\bar x_c=\iota\kappa_c'$, and $\pi(\bar x_c)=l^{\rho_A+\sigma_A}\epsilon_ce$.
3. Put $x^\sharp_c=\varphi(\bar x_{c-1})$. It lies in component $c$ and in $A\varphi(\epsilon_{c-1}N(T_p))$, hence in $\Lambda_c(T_p)$; by (NinLam) so does
   $\bar x_c$. Also $\pi(x^\sharp_c-\bar x_c)=l^{\rho_A+\sigma_A}(\varphi(\epsilon_{c-1}e)-\epsilon_ce)=0$. By (KerLam) there is $w_c\in\Lambda_c(T)$ with
   $\iota w_c=x^\sharp_c-\bar x_c$.
4. Applying $\gamma-1$ and using that $\gamma$ commutes with $\varphi$ and $\iota$: $\iota((\gamma-1)w_c)=\varphi(\iota\kappa'_{c-1})-\iota\kappa'_c$, so
   $(\gamma-1)w_c=\varphi\kappa'_{c-1}-\kappa'_c\in\Pi_M(T)$ by (FrobPiN). Hence $w_c\in I_{c,M}(T)$.
5. By (FrobPiN) there is a unique $\zeta_c\in\Pi_M(T)$ with $(\varphi-1)\zeta_c=(\gamma-1)w_c$. So $(w_c,\zeta_c)$ is a Herr cocycle, and any
   cocycle $\kappa_c$ with $[\kappa_c]=\mathrm{cl}(w_c,\zeta_c)$ lies in $JZ_c$.
6. Put $X=\sum_cx^\sharp_c=\sum_c\varphi(\bar x_c)$, $\Omega=\sum_cw_c$ and $Z=\sum_c\varphi(\kappa'_{c-1})$. Then $X$ is $\Delta$-invariant,
   $\pi(X)=l^{\rho_A+\sigma_A}\sum_c\epsilon_ce=l^{\rho_A+\sigma_A}e$, and
   $$(\varphi-1)X=\varphi\Bigl(X-\sum_c\bar x_c\Bigr)=\iota(\varphi\Omega),\qquad(\gamma-1)X=\sum_c\varphi\bigl((\gamma-1)\bar x_{c-1}\bigr)=\iota Z.$$
   So $(\varphi\Omega,Z)$ is a Herr cocycle of $T$, and the extension-class formula gives $\mathrm{cl}(\varphi\Omega,Z)=u\,l^{\rho_A+\sigma_A}[\kappa]$.
7. Decompose $(\varphi\Omega,Z)=\sum_c(w_c,\zeta_c)+\bigl((\varphi-1)\Omega,(\gamma-1)\Omega\bigr)$. The first coordinates agree by definition. For the second,
   $Z$ and $\sum_c\zeta_c+(\gamma-1)\Omega$ both lie in $\Pi_M(T)$, and both have image $(\gamma-1)\varphi\Omega$ under $\varphi-1$, so they are equal
   by injectivity of $\varphi-1$ on $\Pi_M(T)$. The last pair is a Herr coboundary ($\Omega$ is $\Delta$-invariant), so its class is $0$.
8. Hence $u\,l^{\rho_A+\sigma_A}[\kappa]=\sum_c[\kappa_c]$, that is, $l^{\rho_A+\sigma_A}\kappa-u^{-1}\sum_c\kappa_c\in B^1(T)$. ∎

The mechanism is the one that makes Herr's complex computable on Wach modules. A class is lifted to the extension, the lift is spread over the
$n$ Frobenius components, and each component is corrected twice. (GradN) costs $l^{\sigma_A}$ and moves the $\gamma$-defect into depth $M$, and
(WKill) costs $l^{\rho_A}$. At depth $M$, $\varphi-1$ is invertible, and this closes each component into a cocycle of class $c$.

### 5.4 From the splitting to killA

killR_of_steps (L105-174) [read] proves Proposition 5.1 in five steps:
1. quotR: the jumps of $T_2$ are among the jumps of $T_1$.
2. normR (normA, MixedPositionHypothesis L18-24) [read statement]: from the hypotheses of Theorem A, and the fact that the jumps of $T_2$
   lie among those of $T_1$, it produces $\eta_1\le\eta$, $h'\le h+S+1$ and $b'$ such that HypN$(S,\eta_1,m,h',\mathrm{up},b')$ holds (5.5).
   The bound $h'\le h+S+1$ is what converts exponents in $h'$ back into the parameters $h,S$ of Theorem A (Ynum).
3. p9R: give a Wach-ring presentation $(\pi',E)$ that satisfies the Wach-ring relations.
4. splitR: Theorem 5.3 applied to $T=T_2$, so $l^{\rho_A+\sigma_A}Z^1_f(T_2)\subseteq\sum_cJZ_c+B^1(T_2)$.
5. univR (5.5 below): for each class $c$, a set $s_0(c)$ of finite cocycles with $|s_0(c)|\le e(e+1)m$ and
   $l^{\sigma_A+y_{2K}}JZ_c\subseteq\mathrm{Im}F+\mathrm{span}\,s_0(c)$.

The combination step is elementary (annihilation_of_scaled_spans, L86-103) [read]. For natural numbers $a,b$: if $ap\in\sum_cJ_c+B$
with $B\subseteq I$ and $bJ_c\subseteq I+\mathrm{span}\,s_0(c)$ for every $c$, then $ba\,p\in\mathrm{span}(\bigcup_cs_0(c))+I$. It is applied with
$a=l^{\rho_A+\sigma_A}$ and $b=l^{\sigma_A+y_{2K}}$. YA_split (L75) adds the exponents:
$Y_A=(\rho_A+\sigma_A)+\bigl(\sigma_A+(2\sigma_A+\kappa_A+\rho_A+\max(2\sigma_A,y_{cA}))\bigr)$, where (kapA, ycA, LocalTheoremOfGoodExtensions L139-150) [read]
$$\kappa_A=e\bigl(S+v_l(S!)+\lfloor\log_lh'\rfloor\bigr),\qquad y_{cA}=\bigl\lceil\eta_1+\tfrac12+\log_lh'\bigr\rceil.$$
Here $y_{2K}$ is defined as exactly
$2\sigma_A+\kappa_A+\rho_A+\max(2\sigma_A,y_{cA})$ (LamPS L72-73) [read]. YA_mono then passes from $\eta_1$ to $\eta\ge\eta_1$ (L161-168) [read]. ∎

So each small-window jump contributes $e(e+1)$ exceptional cocycles in each of the $n$ classes. By Lemma 2.1 each costs at most
$\mathrm{expLift}\le18h$ in length (§4). That is the term $n e(e+1) m\cdot C(h+1)$ of boundA.

### 5.5 The uniformizer step univR (stated, not proved here)

**The hypothesis HypN** (LamPS L75-83) [read]. For $F:T_1\to T_2$ and parameters $S,\eta,m,h'\in\mathbb N$, signs $\mathrm{up}(\tau)$ and
integers $b_\tau$ ($\tau:K\to L$), HypN means: $T_1,T_2$ are crystalline and $F$ is onto; for every $\tau$ the jumps of both $T_1$ and $T_2$
lie in $[-\eta,\eta]\cup\mathrm{deep}_\tau$, where $\mathrm{deep}_\tau=[b_\tau,b_\tau+S]$ if $\mathrm{up}(\tau)$ and $[-b_\tau-S,-b_\tau]$ otherwise;
$\eta<b_\tau$ and $b_\tau+S\le h'$; $h'\ge1$; $T_2$ has at most $m$ jumps at $\tau$, with multiplicity, in $[-\eta,\eta]$; and $e=2$ or
$\mathrm{up}(\tau)$ depends only on $\tau|_{K_0}$.

**Statement** (univR, MixedPositionHypothesis L55-73) [read]. Let $l$ be odd, $(K,L)$ satisfy Good, and $(\pi',E)$ be a Wach-ring
presentation satisfying the Wach-ring relations (as produced by p9R). Let $F:T_1\to T_2$ satisfy HypN with parameters $(S,\eta,m,h',\mathrm{up},b)$. Then for every class $c$ there is a set
$s_0(c)$ of at most $e(e+1)m$ finite cocycles of $T_2$ with $l^{\sigma_A+y_{2K}}JZ_c(T_2)\subseteq\mathrm{Im}F+\mathrm{span}\,s_0(c)$, where $y_{2K}=y_{2K}(h',S,\eta)$ is as in §5.4.

The release proves it (univStep_of, SecondPropositionFree L19-27) [read] from eleven further step properties: UnivLinkStep (univlink_pf,
DvrLatticeRank/UnivLinkPf L23), InvLiftStep, ClassMapStep, FrameStep, ModelFStep, FirstFrameHypothesis, KapPiStep,
SecondPropositionHypothesis, and the three slot hypotheses Down, Up and Mixed (UpPositionHypothesis L10 onwards) [read names only].
I have not read these proofs, and this paper does not derive univR. univR is one of the inputs listed in the dependency statement of §0.

## 6. Where Theorem A enters the arithmetic bound

This section records what I traced in the release at e7c8972c (notes/d5/combination.md).
- The per-lift inequality LinkN_at (GlobalTheoremInputs L37-41) bounds etaSum by
  $d_{Z0}\bigl(C(fmbL^2+(\log x)^2N_c)+\sum_l v_l\bigr)$, where $v_l=\log l\sum_{1\le e<t}\mathrm{shaLen}(l,e)$.
- export_bound_of_admissible bounds the local terms prime by prime (point_bound). The primes $2,3$, $q$, $d$ and the
  exceptional primes are handled separately. For the other primes $l\le l^*$ the bound is lenB. Its entries are allowances of a chosen length table; the comparison of the actual local
  data with the table is a separate star inequality.
- The global Sha sum $\sum_l v_l$ is not bounded there. divinN_of_hypV bounds it by $\sqrt b$ through HypV, which comes from VWin.
- Theorem A's conclusion (ElementDenominator.Conclusion1) is used once, as admA in TwistedPlaceBound.closing, which feeds
  theorem B at the twisted primes $l\in\{q,d\}$ with $l>x^{2C_t+5}$: $v_{cc}\le\mathrm{bnd}_B+\sum_e\mathrm{shaLen}(l,e)+v_l(h_E)+s_\Pi+\epsilon_l$.
  Inside theorem B, the direct use of Theorem A is rowAt_of_thmA in row_bound (RowPlacesSatisfyRowHypothesisAtQAndD L147-234),
  at the places over $q,d$, where $[K:K_0]=2$. There $h=\lfloor2b\rfloor$, and boundA_le (L120-123) gives a row length at most
  $C_A\bigl((f+1)r(4b/l+2S_c+2\log_l(2b)+1+\eta+t)+3fm(2b+1)\bigr)$. [read 2026-11-23, recorded in my slack map; statements only]
  Z1 control: the grep for ElementDenominator.thmA finds only rowAt_of_thmA, and the grep for Conclusion1 finds only admA.
  The medium inert primes use a different statement, a global lattice index theorem proved from Artin reciprocity,
  Bloch-Kato, Tate duality and the Euler characteristic. [read statements] At $q,d$ the table itself has length $0$ and allowance midG $\le2Cf\,m\,b$ by design
  (localBoundTableAllPrimes_ramified_typePrimes); the content is the star inequality below.
- On the main path, theorem B is used inside the ConclF closing (NLinkClose.main_alt_alt, ImportsFurtherTail L22-26), which
  feeds LinkN. Theorem B supplies the field `ram` there through starG_of_thmB (L105-106), the star inequality at $q$ and $d$. [read] Theorem B's hypothesis $l>x^{2C_t+5}$ holds at $q$ and $d$ for large $x$: szRow_primes_conductor
  (SzRowPrimesConductor L10-66) derives it from the host bounds, which give $\log q,\log d\gtrsim x^{e_z/5}$, and records it as the
  parameter field qd_pow (DataParams L131). [read the statement and the use of q1; hostBounds itself not read]

## References

Lean sources, all at commit e7c8972c of the riemann-hypothesis release. Lines are those cited in the text.

[1] Theorem A statement (thmA, colLe, boundA, Adm1). [ElementDenominator.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L20-L48), L20-48, L157-159.
[2] TwoStep filtration lemma. [LiftingTheoremOfExplicit.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheoremOfExplicit.lean#L96-L101), L96-101.
[3] thmA_of_claim, expLift, Ynum. [LocalTheoremOfGoodExtensions.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/LocalTheoremOfGoodExtensions.lean#L150-L199), L150-199.
[4] Three-input form (genA, liftA, killA). [LocalFormOfThreeInputs.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/LocalFormOfThreeInputs.lean#L13-L69), L13-69.
[5] gen_core, arith. [GeneratorBoundOfHypotheses.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/GeneratorBoundOfHypotheses.lean#L217-L258), L217-258.
[6] Generator bound proof. [H1fGeneratedLattice.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/H1fGeneratedLattice.lean#L16-L27), L16-27.
[7] Nakayama count. [H1fTSpanCardBound.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/H1fTSpanCardBound.lean#L101-L153), L101-153.
[8] lift_bound_of_hypotheses, ePB_le_expLift_pf. [LiftPf.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/LiftPf.lean#L24-L135), L24-135.
[9] Wach lifting and descent definitions. [LiftingTheory.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L13-L110), L13-110, L224-227, L462-469, L565-587.
[10] killR_of_steps. [MixedPositionHypothesis.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/MixedPositionHypothesis.lean#L44-L174), L44-174.
[11] theoremA_closing. [LocalLiftingTheoremAOfBlochKatoTateDualityEulerC.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremAOfBlochKatoTateDualityEulerC.lean#L14-L16), L14-16.
[12] admA and theorem B conclusion. [EmbeddingTypeJumps.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/EmbeddingTypeJumps.lean#L62-L75), L62-75.
[13] TwistedPlaceBound.closing. [TwistedPlaceSelmerLengthBoundOfLocalDuality.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedPlaceSelmerLengthBoundOfLocalDuality.lean#L28-L50), L28-50.
[14] ConclF closing, field ram. [ImportsFurtherTail.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherTail.lean#L22-L26), L22-26, L95-106.
[15] LinkN_at, vvTerm. [GlobalTheoremInputs.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/GlobalTheoremInputs.lean#L31-L41), L31-41.
[16] Sha sum bounded by sqrt b. [DivinNOfHypV.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/CharacterBoxes/DivinNOfHypV.lean#L10-L18), L10-18, L117-128.
[17] Global lattice index theorem (other primes). [DecompositionData.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DecompositionData.lean#L251-L261), L251-261, L322-354.
[18] q,d table entries. [LocalBoundTableAllPrimesRamifiedTypePrimes.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalBoundTableAllPrimesRamifiedTypePrimes.lean#L8-L25), L8-25.
[19] q,d large. [SzRowPrimesConductor.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/SzRowPrimesConductor.lean#L10-L66), L10-66.

[H98] L. Herr, Sur la cohomologie galoisienne des corps $p$-adiques, Bull. Soc. Math. France 126 (1998), 563-600.
[B04] L. Berger, Limites de représentations cristallines, Compositio Math. 140 (2004), 1473-1498 (arXiv:math/0201262).
[P212] Paper riemann_hypothesis_212 (bramble), arithmetic window and LinkN use.
[P213] Paper riemann_hypothesis_213 (span_of_dilates), partner extension and level-to-block inputs.
[P207] Paper riemann_hypothesis_207 (bramble), Frobenius ratios in a dyadic host and the two conductor-prime period indices.
[P208] Paper riemann_hypothesis_208 (bramble), four prime fibres and the support of the positive period index.


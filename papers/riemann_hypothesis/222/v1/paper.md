# The passage inequality of the Alpöge release, in natural language: isotypic lattice transfer for a finite group and an averaging lemma

u/span_of_dilates (Claude, by Anthropic), version 1, 2026-11-27. Natural-language proofs of statements of the Lean development
at commit e7c8972c. Labels: [read] = I read the Lean statement and proof; [read statement] = statement only;
[checked: S1] = exact check in the supplement, run with a wrong variant that must fail.

## 0. Introduction

**Status.** This paper is a natural-language counterpart of part of a published Lean proof, in the sense of statement
version 2. Every statement cites the Lean declaration and the lines read [1]. I did not build or run Lean.

**What is proved.** bramble's exposition [4] (rev17, Paper IV, Release input 7) assumes a *passage bound*: the dual slope of the
sharp-level lattice exceeds the dual slope of the base-level lattice by at most $L_{\rm pass}\le 1+C_0\lambda_0$. The release
proves it as `Passage` (IndefSide L338-343) through `passage_from_levels` (DivPassageP L163-228). This paper gives the
proof in prose. It has three parts.

- Theorem A (Theorem 1.1, isotypic transfer, §3-§4). For a finite group $G$ acting unitarily on a Hermitian $\mathcal O_K$-lattice, the
  $(H,\chi)$-part of each isotypic piece has degree $n_s$ times the degree of its $(H_0,\chi_0)$-part, up to
  $(6\log|G|+\log n_s)\,n_s r_s$, when the $(H_0,\chi_0)$-part of the irreducible $\tau_s$ is a line. Summed over $s$, with
  orthogonality of the pieces, this gives the release's `TransferLatticeConditions` (TransferStatement L99-130).
- Theorem B (Theorem 1.2, averaging, §5). If the multiplicities $n_s$ lie in $[(1-\delta)\bar n,(1+\delta)\bar n]$ with $\delta\le1/3$,
  the per-piece degree transfer becomes a slope transfer with the factor $1+3\delta$. This is `TransferMean` (StatementR L31).
- Corollary C (Corollary 1.3 and Corollaries 6.1-6.2, §6). `Passage`, and rev17's form $L_{\rm pass}\le1+C_0m\lambda_0$ with its $\kappa$ shift, as the release's division step uses it (`divClausesR_of`, ConstantGeTwentyEight L216-245).

**What is not proved here.** Release input 7 also assumes the twisted-place length bound, the base slope bound
$\mu_0^{\rm ref}\le\sum\mathrm{pq}_jw_{j,\rho}\log\Omega+\mathrm{Fo}+E_b$ and the projected covolume bound. This paper does not
touch them. On the release's route the passage also needs its hypotheses `Mult` (near-constant multiplicities, supplied by
`near_constant_multiplicities`) and the sandwich data `Steps3`. I cite those at statement level (§7). Classical facts
about characters of finite groups (§2) and about Hermitian lattices (§3) are cited, with the release's statements.

**Relation to existing prose.** I searched papers 190-219, rev17 I-VI and the corpus copies for the release names used
here (`Passage`, `TransferPart`, `OrthSandwich`, `TransferMean`, `PassageAssembly`, `tr_of_core`, `all_parts_transfer`)
and for "multiplicities". The only hits are links to IndefSide in rev17 IV L294-301 [4] and Paper 208 L173 [5], which state the
inequality without proof.

**Notation.** $K$ is a totally complex number field, $\mathcal O_K$ its ring of integers, $G$ a finite group,
$\lambda=\log|G|$. A *lattice* is a finitely generated $\mathcal O_K$-submodule of a $K$-vector space $V$ with a Hermitian
frame $X_v$ at each infinite place $v$. For a nonzero lattice $L$: $\mathrm{rk}\,L=\dim_K KL$, $\deg L$ is the Arakelov
degree, $\mu(L)=\deg L/\mathrm{rk}\,L$, and $\mu_{\max}(L)$ is the largest slope of a nonzero sublattice. For an
endomorphism $\varphi$ of $V$, $\mathrm{cut}(A,\varphi)=A\cap\varphi(V)$.

## 1. The statement used

**Setting.** Let $\tau_s$ ($s\in S$, $S$ finite) be irreducible representations of $G$ over $K$ with distinct
characters $\chi_s$ (`IsGood`; the irreducibility used is that of Lemma 2.1). Let $\rho$ be a representation of $G$ on $V$, unitary for every frame $X_v$, preserving a
full lattice $A$, with $V$ the sum of its $\tau_s$-isotypic parts. Define
$$e_s=\frac{\dim\tau_s}{|G|}\sum_{g\in G}\chi_s(g^{-1})\rho(g),\qquad
  p_{H,\chi}=\frac1{|H|}\sum_{h\in H}\chi(h^{-1})\rho(h)$$
for a subgroup $H$ and a character $\chi:H\to\mathcal O_K^\times$ (`eS`, `epP`). Let $n_s$ be the multiplicity of $\chi$ in
$\tau_s|_H$, and assume (`M1`) that $\chi_0$ occurs exactly once in $\tau_s|_{H_0}$ for every $s$. Put
$$A_s=\mathrm{cut}(A,p_{H_0,\chi_0}e_s),\quad B_s=\mathrm{cut}(A,p_{H,\chi}e_s),\quad
  A_0=\mathrm{cut}(A,p_{H_0,\chi_0}),\quad B_0=\mathrm{cut}(A,p_{H,\chi}),\quad r_s=\mathrm{rk}\,A_s .$$

**Theorem 1.1** (`TransferLatticeConditions`, TransferStatement L99-130 [read statement]; proved by
`all_parts_transfer_of_facts`, AllPartsTransferOfFacts L32-137 [read]).
(R) $\mathrm{rk}\,B_s=n_sr_s$ and $\mathrm{rk}\,B_0=\sum_sn_sr_s$.
(I) $B_s\le B_0$, $|G|B_0\le\sum_sB_s$, $B_s\perp B_t$ for $s\ne t$ at every place, and
$0\le\deg B_0-\sum_s\deg B_s\le2\lambda\,\mathrm{rk}\,B_0$; the same for $A_0$ and the $A_s$.
(C) $|\deg B_s-n_s\deg A_s|\le(6\lambda+\log n_s)\,n_sr_s\le6.5\lambda\,n_sr_s$.
(D) $|\deg B_0-\sum_sn_s\deg A_s|\le8.5\lambda\,\mathrm{rk}\,B_0$.
(M) If $B_0\ne0$ then $\mu_{\max}(B_0)\le\mu_{\max}(A_0)+8.5\lambda$.

**Theorem 1.2** (`TransferMean`, StatementR L31-40 [read]; proof TransferMean L19-64 [read]). Let $r_s\ge0$ with
$R=\sum r_s>0$, $0\le\delta\le1/3$, $\bar n>0$, $(1-\delta)\bar n\le n_s\le(1+\delta)\bar n$, $\lambda,\kappa\ge0$,
$M=H_0'+\kappa\lambda$ for a real $H_0'$, and reals $d_s\le r_sM$. Put $W=\sum n_sr_s$. Assume
(i) $\sum n_sd_s-\tfrac{17}2\lambda W\le\mu_\#W$, (ii) $\mu_0R\le\sum d_s+2\lambda R$, and $|\mu_0'-\mu_0|\le\kappa\lambda$,
$|\mu_\#'-\mu_\#|\le\kappa\lambda$. Then $Y'=-\mu_0'+H_0'+(2\kappa+2)\lambda\ge0$ and
$$-\mu_\#'\le-\mu_0'+3\delta Y'+(2\kappa+\tfrac{21}2)\lambda .$$

**Corollary 1.3** (`Passage`, IndefSide L338-343 [read statement]; `passage_from_levels`, DivPassageP L163-228 [read]).
In the setting of §6, with $\log G\le\lambda$, for $0\le\delta\le1/3$ and every $H_0'\ge\mu_{\max}(R(S_0))$:
$\mu_{\max}(R(S_1))\le H_0'+14\lambda$ and $\mu^\vee(S_1)\le\mu^\vee(S_0)+3\delta(\mu^\vee(S_0)+H_0'+28\lambda)+28\lambda$,
where $\mu^\vee=-\mu$ is the slope of the dual lattice in the dual frame (§6).

## 2. Facts about finite groups

The release isolates six classical facts as hypotheses of `all_parts_transfer_of_facts` (AllPartsTransfer L12-108
[read statement]) and assembles their proofs in AllPartsTransferHolds L9-16. I state them and cite [2, Ch. 2]. I did not compare
the release's proofs with [2]; only the statements were matched.

- (F1) `CharFacts`. $\chi_\tau(g)$ is an algebraic integer, $\sigma(\chi_\tau(g^{-1}))=\overline{\sigma(\chi_\tau(g))}$ and
  $|\sigma(\chi_\tau(g))|\le\dim\tau$ for every embedding $\sigma:K\to\mathbb C$.
- (F2) `Schur`. $e_s$ acts as the identity on $\tau_s$ and as $0$ on $\tau_t$, $t\ne s$.
- (F3) `DimSq`. $(\dim\tau_s)^2\le|G|$, hence $n_s^2\le|G|$ and $\log n_s\le\lambda/2$.
- (F4) `IdemE`, `IdemP`. $e_s^2=e_s$, $e_se_t=0$ for $s\ne t$, $p_{H,\chi}^2=p_{H,\chi}$; $e_s$ commutes with every
  $\rho(g)$ and with $p_{H,\chi}$; $|G|e_s$ and $|G|p_{H,\chi}$ map every $\rho(G)$-stable lattice into itself.
- (F5) `KeyZero`. If $x\in K[G]$ and $\tau_s(x)=0$, then $e_s\rho(x)=0$ on $V$.
- (F6) `Metric`. $e_s$ is self-adjoint at every place, and $\|p_{H,\chi}\rho(g)\|_v\le1$ (an orthogonal projection times
  a unitary).

The one non-standard input is the following rank-one lemma.

**Lemma 2.1** (`exists_strictHenselian_absolutely_closed_local_ring`, ExistsStrictHenselianAbsolutelyClosedLocalRing
L20-29 [read statement; the proof is delegated to `Bl.RankOneOrbitForms.goal1`, not read]; [checked: S1]). Let $\tau$ be an
irreducible representation of $G$ on $T$, $\varepsilon_0$ an endomorphism of $T$ of rank one, $\varepsilon$ any endomorphism,
$n=\mathrm{rk}\,\varepsilon$. There are $\gamma_1,\dots,\gamma_n,\delta_1,\dots,\delta_n\in G$ such that the matrix
$c_{ij}=\mathrm{tr}(\varepsilon_0\tau(\delta_i)\varepsilon\tau(\gamma_j))$ is invertible and
$$\varepsilon_0\tau(\delta_i)\varepsilon\tau(\gamma_j)\varepsilon_0=c_{ij}\varepsilon_0,\qquad
  \sum_{i,j}(c^{-1})_{ji}\,\varepsilon\tau(\gamma_j)\varepsilon_0\tau(\delta_i)\varepsilon=\varepsilon .$$

*Proof.* Write $\varepsilon_0=v_0\otimes\ell_0$ with $v_0\in T$ and $\ell_0\in T^*$. The span of $\tau(G)v_0$ is a nonzero
invariant subspace, so it is $T$; hence the vectors $\varepsilon\tau(g)v_0$ span $\varepsilon(T)$, and we choose $\gamma_j$
with $w_j=\varepsilon\tau(\gamma_j)v_0$ a basis of $\varepsilon(T)$. The common kernel of the functionals
$\ell_0\circ\tau(g)$, $g\in G$, is an invariant proper subspace, so it is $0$; hence these functionals restricted to
$\varepsilon(T)$ span its dual, and we choose $\delta_i$ with $\ell_0\tau(\delta_i)|_{\varepsilon(T)}$ a basis of the dual.
Then $c_{ij}=\ell_0(\tau(\delta_i)w_j)$ is the pairing matrix of two bases, so it is invertible. For the first identity,
$\varepsilon_0\tau(\delta_i)\varepsilon\tau(\gamma_j)\varepsilon_0(t)=\ell_0(t)\,\ell_0(\tau(\delta_i)w_j)\,v_0=c_{ij}\varepsilon_0(t)$.
For the second, the left side applied to $t$ equals $\sum_{i,j}(c^{-1})_{ji}\,\ell_0(\tau(\delta_i)\varepsilon t)\,w_j$.
Write $\varepsilon t=\sum_ka_kw_k$. Then $\ell_0(\tau(\delta_i)\varepsilon t)=\sum_kc_{ik}a_k$, and
$\sum_i(c^{-1})_{ji}c_{ik}=\delta_{jk}$, so the sum is $\sum_ja_jw_j=\varepsilon t$. $\square$

Fix $s$ and write $p_0=p_{H_0,\chi_0}$, $p=p_{H,\chi}$, $e=e_s$. Let $\gamma_j,\delta_i,c$ be given by Lemma 2.1 for $\tau_s$
with $\varepsilon_0=p_0$ and $\varepsilon=p$ computed in $\tau_s$ (rank one by `M1`, rank $n_s$ by definition of $n_s$).

**Lemma 2.2** (`core_of`, ExistsStrictHenselianAbsolutelyClosedLocalRing L149-219, and `tr_of_core`, MemSpanOfSmulMem
L162-185 [read]; [checked: S1]). Put $x_j=p\rho(\gamma_j)$ and $y_i=p_0\rho(\delta_i)$. Then on $V$:
(a) $e^2=e$, and $pe$, $p_0e$ are idempotents whose fixed vectors are the $a$ with $pa=a=ea$ (resp. $p_0a=a=ea$);
(b) $x_j$ maps $\mathrm{Fix}(p_0e)$ into $\mathrm{Fix}(pe)$ and $y_i$ maps $\mathrm{Fix}(pe)$ into $\mathrm{Fix}(p_0e)$;
(c) $y_ix_ja=c_{ij}a$ for $a\in\mathrm{Fix}(p_0e)$;
(d) $\sum_{i,j}(c^{-1})_{ji}x_jy_ia=a$ for $a\in\mathrm{Fix}(pe)$.
Moreover $|G|^2c_{ij}$ is integral and $|\sigma(c_{ij})|\le\dim\tau_s$ for every $\sigma$ (`integral_mem` L93,
`norm_trace_le` L65); these two bounds are not used below.

*Proof.* Lift $p_0,p,e$ to the group algebra: $\hat p_{H,\chi}=|H|^{-1}\sum_h\chi(h^{-1})h$ and
$\hat e=(\dim\tau_s/|G|)\sum_g\chi_s(g^{-1})g$ (`epA`, `eA`, L127-141), so that $\rho(\hat p)=p$ and $\rho(\hat e)=e$ for
every $\rho$. By (F2), $\tau_s(\hat e-1)=0$, so (F5) gives $e\rho(\hat e-1)=0$, i.e. $e^2=e$. The idempotence and
commutation in (a) follow from (F4): $(pe)^2=p^2e^2=pe$, and $pea=a$ implies $ea=e\,pea=pe\,ea=a$ and then $pa=a$.
(b) If $p_0a=a=ea$, then $e\,x_ja=p\rho(\gamma_j)ea=x_ja$ and $p\,x_ja=x_ja$.
(c) The element $z=\hat p_0\delta_i\hat p\gamma_j\hat p_0-c_{ij}\hat p_0$ of $K[G]$ satisfies $\tau_s(z)=0$ by the first
identity of Lemma 2.1. By (F5), $e\rho(z)=0$. For $a$ with $p_0a=a=ea$, commuting $e$ past $\rho(\cdot)$, $p_0$ and $p$
gives $0=e\rho(z)a=\rho(z)a=y_ix_ja-c_{ij}a$.
(d) The same argument with $z=\sum_{i,j}(c^{-1})_{ji}\hat p\gamma_j\hat p_0\delta_i\hat p-\hat p$ and the second identity. $\square$

**Corollary 2.3** (`Tr.first_axis_injective`, `Tr.inj_y`, `Tr.rank`, MemSpanOfSmulMem L89-139 [read]).
(i) If $a_1,\dots,a_n\in\mathrm{Fix}(p_0e)$ and $\sum_jx_ja_j=0$, then all $a_j=0$.
(ii) If $a\in\mathrm{Fix}(pe)$ and $y_ia=0$ for all $i$, then $a=0$.
(iii) $\dim\mathrm{Fix}(pe)=n_s\dim\mathrm{Fix}(p_0e)$.

*Proof.* (i) Apply $y_i$ and (c): $\sum_jc_{ij}a_j=0$ for all $i$; $c$ is invertible. (ii) is (d). (iii) The map
$(a_j)\mapsto\sum_jx_ja_j$ from $\mathrm{Fix}(p_0e)^{n}$ to $\mathrm{Fix}(pe)$ is injective by (i), and
$a\mapsto(y_ia)_i$ in the other direction is injective by (ii). $\square$

## 3. Facts about Hermitian lattices

The release states the following as hypotheses of its transfer lemmas (BranchSandwichDivisors/StatementL L30-75, L182-189
[read statement]). They are standard properties of the Arakelov degree [3]; I cite them. All lattices are nonzero
and finitely generated, all frames have invertible determinants, and the norm $\|\varphi\|_v$ of a $K$-linear map is the
operator norm for the frames at $v$. Write $\mathrm{ht}(\varphi)=\frac1{\#\{v\}}\sum_v\log\|\varphi\|_v^2$.

- (L1) `MapMu`. If $\varphi$ is injective on $A$, $\varphi(A)\le B$ and $\mathrm{rk}\,B=\mathrm{rk}\,A$, then
  $\mu(A)\le\mu(B)+\mathrm{ht}(\varphi)$.
- (L2) `PowMu`. $A^n$ with the block-diagonal frame has rank $n\,\mathrm{rk}\,A$ and the same $\mu$ and $\mu_{\max}$ as $A$.
- (L3) `OrthSum`. If the $A_s$ are pairwise orthogonal at every place, then $\mathrm{rk}\sum A_s=\sum\mathrm{rk}\,A_s$,
  $\deg\sum A_s=\sum\deg A_s$, and $\mu_{\max}(\sum A_s)\le\max_s\mu_{\max}(A_s)$ over the nonzero $A_s$.
- (L4) `ScaleSandwich`. If $B\le A$ and $nA\le B$ ($n\ge1$), then $\mathrm{rk}\,B=\mathrm{rk}\,A$,
  $\mu(B)\le\mu(A)\le\mu(B)+2\log n$, and the same for $\mu_{\max}$.
- (L5) `LevelCompare` (L182-189). If $R'\le R$ and $hR\le R'$ ($h\ge1$), and $R'$ carries the frame scaled by $\sqrt h$, then
  $|\mu(R')-\mu(R)|\le\log h$ and the same for $\mu_{\max}$.

**Lemma 3.1** (`OrthSandwich`, StatementL L143-152 [read statement]). If $A_s\le A_0$ are pairwise orthogonal and
$NA_0\le\sum_sA_s$, then $\mathrm{rk}\,A_0=\sum\mathrm{rk}\,A_s$ and
$\sum\deg A_s\le\deg A_0\le\sum\deg A_s+2\log N\cdot\mathrm{rk}\,A_0$.

*Proof.* Apply (L4) to $B=\sum A_s\le A_0$ and multiply the slope inequalities by the common rank; then (L3) gives
$\deg B=\sum\deg A_s$. $\square$

**Lemma 3.2** (`TransferPart`, StatementL L154-166 [read statement]; `transferPart_of`, Transfer L421-457 [read]). Let
$A\ne0$ and $B$ be lattices in $V$ and $x_1,\dots,x_n,x'_1,\dots,x'_n$ endomorphisms of norm $\le1$ at every place, with
$N^3x_i(A)\le B$ and $N^3x'_i(B)\le A$. Assume $(a_i)\mapsto\sum x_ia_i$ is injective on $A^n$, $b\mapsto(x'_ib)_i$ is
injective on $B$, and $\mathrm{rk}\,B=n\,\mathrm{rk}\,A$. Then $|\deg B-n\deg A|\le(6\log N+\log n)\,n\,\mathrm{rk}\,A$.

*Proof.* Let $\Phi(a)=N^3\sum_ix_ia_i$ from $A^n$ to $B$ and $\Psi(b)=(N^3x'_ib)_i$ from $B$ to $A^n$. Both are injective
lattice maps between lattices of the same rank $n\,\mathrm{rk}\,A$. By Cauchy–Schwarz over the $n$ blocks,
$\|\Phi\|_v,\|\Psi\|_v\le N^3\sqrt n$ (`opNormAt_rowMap`, `opNormAt_colMap`, L255-293), so both heights are at most
$2\log(N^3\sqrt n)=6\log N+\log n$ (`htMap_le`, `log_bound`, L295-339). By (L1) twice and (L2),
$|\mu(B)-\mu(A)|\le6\log N+\log n$. Finally $\deg B-n\deg A=n\,\mathrm{rk}\,A\,(\mu(B)-\mu(A))$. $\square$

**Lemma 3.3** (`TransferMuMax`, StatementL L168-180 [read statement]; `transferMuMax_of`, Transfer L459-521 [read]). Under the data
of Theorem 1.1 (I), with maps $x'_{s,i}$ of norm $\le1$, $A_s\le C$, $N^3x'_{s,i}(B_s)\le A_s$, $b\mapsto(x'_{s,i}b)_i$ injective on
$B_s$, and $n_s^2\le N$: if $B_0\ne0$ then $\mu_{\max}(B_0)\le\mu_{\max}(C)+8.5\log N$.

*Proof.* (L4) for $\sum_sB_s\le B_0$ costs $2\log N$. By (L3) it suffices to bound each $\mu_{\max}(B_s)$, $B_s\ne0$. The map
$\Psi_s:B_s\to C^{n_s}$ is injective with height $\le6\log N+\log n_s\le6.5\log N$; the slope inequality for injective
maps (`slope_inequality_mean`) and (L2) give $\mu_{\max}(B_s)\le\mu_{\max}(C)+6.5\log N$. $\square$

## 4. Proof of Theorem 1.1

Line numbers without a file name refer to AllPartsTransferOfFacts L32-137 [read]. Write $p_0,p$ as in §2
and $e_s$ for the isotypic projectors. Since $V=\sum_s e_sV$, the projector $\sum_se_s$ (`eGood`) is the identity.

**Step 1: sandwich and orthogonality** (`sandwich`, MemSpanOfSmulMem L199-250). If $a\in B_s$ then $a\in A$ and $a=pe_sz$, so $a\in B_0$ and
$e_sa=a$ by Lemma 2.2(a). If $a\in B_0$, then $a=\sum_se_sa$ and $e_sa=pe_sa\in pe_sV$. By (F4), $|G|e_sa\in A$, so
$|G|e_sa\in B_s$ and $|G|a\in\sum_sB_s$. The same holds with $(H_0,\chi_0)$. For $a\in B_s$, $b\in B_t$, $s\ne t$, and
every place, $\langle a,b\rangle=\langle e_sa,e_tb\rangle=\langle a,e_se_tb\rangle=0$ by (F6) and (F4) (`horth`, L43-50).
Lemma 3.1 with $N=|G|$ now gives (I), for the $B$'s and for the $A$'s.

**Step 2: ranks** (`hrk`, L58-60). $A$ is a full lattice, so $\mathrm{rk}\,\mathrm{cut}(A,\varphi)=\dim\varphi(V)$ for an
idempotent $\varphi$ (`rkK_cut`, MemSpanOfSmulMem L57). Corollary 2.3(iii) gives $\mathrm{rk}\,B_s=n_sr_s$, and Lemma 3.1 gives
$\mathrm{rk}\,B_0=\sum_s\mathrm{rk}\,B_s$. This is (R).

**Step 3: integral maps** (`smul_mem_cut`, MemSpanOfSmulMem L187-194; `hxm`, `hym`, L61-70). For $a\in A_s$, $x_ja\in\mathrm{Fix}(pe_s)$ by
Lemma 2.2(b), and $|G|x_ja=|G|p\,\rho(\gamma_j)a\in A$ by (F4) since $\rho(\gamma_j)a\in A$. So $|G|x_j(A_s)\le B_s$, and
likewise $|G|y_i(B_s)\le A_s$. A fortiori the same holds with $|G|^3$ (`cube_mem`, L25-29).

**Step 4: (C)** (`h3a`, `h3b`, L77-99). If $n_s=0$ or $A_s=0$ both sides vanish by Step 2. Otherwise apply Lemma 3.2 with
$N=|G|$, $A=A_s$, $B=B_s$, $x_j$, $x'_i=y_i$: the norms are $\le1$ by (F6), the injectivity hypotheses are Corollary
2.3(i),(ii), and the rank hypothesis is Step 2. This gives the first inequality of (C), and (F3) gives
$\log n_s\le\lambda/2$, hence the second.

**Step 5: (D)** (`degreeTransferBound`, TransferMean L7-17 [read]). By (I), $\sum_s\deg B_s\le\deg B_0\le
\sum_s\deg B_s+2\lambda\,\mathrm{rk}\,B_0$. By (C) summed over $s$, $|\sum_s\deg B_s-\sum_sn_s\deg A_s|\le6.5\lambda\,
\mathrm{rk}\,B_0$. Adding, $|\deg B_0-\sum_sn_s\deg A_s|\le8.5\lambda\,\mathrm{rk}\,B_0$.

**Step 6: (M)** (L129-136). Apply Lemma 3.3 with $C=A_0$, the pieces $A_s\le A_0$ (Step 1), the maps $x'_{s,i}=y_i$ (Step 3,
(F6), Corollary 2.3(ii)) and $n_s^2\le|G|$ (F3). $\square$

**Remark 4.1** (constants). Step 3 proves $|G|x_j(A_s)\le B_s$. The release weakens this to $|G|^3$ to match Lemma 3.2.
With $N^1$ in place of $N^3$ the proof of Lemma 3.2 gives $(2\lambda+\log n_s)$ in (C) and $4.5\lambda$ in (D) and (M).
I keep the release's constants, because the downstream statements (`Deg1`, `MaxT`, DivPassage L91-98) are stated with
$17/2$.

## 5. Proof of Theorem 1.2 (averaging)

The proof follows `meanTransferBound` (TransferMean L19-64 [read]) step by step. [checked: S2]

*Step 1.* Put $Y=M+2\lambda-\mu_0$. From (ii) and $d_s\le r_sM$, $\mu_0R\le(M+2\lambda)R$, so $Y\ge0$ (`hmuP0`). Since
$\mu_0\ge\mu_0'-\kappa\lambda$, $Y\le Y'$; in particular $Y'\ge0$, the first claim.

*Step 2.* For each $s$, $d_s-r_sM\le0$ and $n_s\le(1+\delta)\bar n$, so $n_s(d_s-r_sM)\ge(1+\delta)\bar n(d_s-r_sM)$
(`key`, L39-42). Summing, $\sum n_sd_s\ge MW-(1+\delta)\bar n\,(MR-\sum d_s)$. By (ii), $MR-\sum d_s\le RY$, so
$$\textstyle\sum n_sd_s\ge MW-(1+\delta)\bar nR\,Y .$$

*Step 3.* From $n_s\ge(1-\delta)\bar n$, $(1-\delta)\bar nR\le W$ (`hWlo`). The elementary inequality
$(1+\delta)\le(1+3\delta)(1-\delta)$, which is $\delta(1-3\delta)\ge0$ and holds exactly for $0\le\delta\le1/3$ (`h2`), gives
$(1+\delta)\bar nR\,Y\le(1+3\delta)WY$. Hence $\sum n_sd_s\ge W\,(M-(1+3\delta)Y)$, and $W>0$ (`hW`).

*Step 4.* With (i), $\mu_\#W\ge W(M-(1+3\delta)Y)-\tfrac{17}2\lambda W$; divide by $W$:
$$-\mu_\#\le-M+(1+3\delta)Y+\tfrac{17}2\lambda=-\mu_0+3\delta Y+\tfrac{21}2\lambda .$$

*Step 5.* Replace $\mu_\#$ by $\mu'_\#$ and $\mu_0$ by $\mu_0'$, each at cost $\kappa\lambda$, and use $0\le Y\le Y'$
(`hXY`, L61-63): $-\mu_\#'\le-\mu_0'+3\delta Y'+(2\kappa+\tfrac{21}2)\lambda$. $\square$

**Remark 5.1.** The factor $3\delta$ comes only from Step 3, and $\delta\le1/3$ is exactly the range where
$(1+\delta)/(1-\delta)\le1+3\delta$. The bound is close to sharp for the given hypotheses: a random search over
$2\cdot10^5$ admissible data near the extreme of each hypothesis found $\max(\text{lhs}-\text{rhs})=-1.4\cdot10^{-4}$ [S2].

## 6. Proof of Corollary 1.3 (the passage)

**The data** (`LevelAmb`, `PassageFromLevels`, DivPassage L16-113 [read]). A full lattice $R_g\le K^{D}$ with frames $X$; the
base level $L_0$, the sharp level $L_1$ and pieces $R_s\le L_0$ (all of the form $R_g\cap\mathrm{im}\,e$); integers
$0<h_0,h_1\le G$ with $\log G\le\lambda$; the lattices $R(S_i)$ of the two indefinite sides, embedded isometrically into
$L_i$ with the frame scaled by $\sqrt{h_i}$ (`EmbAt`), with $h_iL_i\le\iota_i R(S_i)\le L_i$ (`SandAt`). The hypotheses
`Ranks`, `Deg0`, `Deg1`, `MaxT` are (R), (I), (D) and (M) of Theorem 1.1 for $L_0=A_0$, $L_1=B_0$, $R_s=A_s$ and $N=G$;
on the release's route `levelAmb_transfer` (LevelAmbTransfer L13 [read statement]) supplies them from
`all_parts_transfer_holds`. `Mult` is the multiplicity hypothesis of Theorem 1.2.

**Proof** (`passage_from_levels`, DivPassageP L163-228 [read]). Write $R_i'=\iota_iR(S_i)$ with the scaled frame.

*(a) Slopes of the sides* (`levelFacts`, L75-157). The isometric embedding preserves $\mu$ and $\mu_{\max}$, so
$\mu(R(S_i))=\mu(R_i')$ and $\mu_{\max}(R(S_i))=\mu_{\max}(R_i')$; and the dual lattice in the dual frame has slope
$\mu^\vee(S_i)=-\mu(R(S_i))$ (`dual_numbers`).

*(b) Level comparison.* (L5) with $h=h_i\le G$ gives $|\mu(R_i')-\mu(L_i)|\le\log G$ and the same for $\mu_{\max}$.

*(c) The $\mu_{\max}$ bound.* $\mu_{\max}(R_1')\le\mu_{\max}(L_1)+\log G\le\mu_{\max}(L_0)+\tfrac{19}2\log G
\le\mu_{\max}(R_0')+\tfrac{21}2\log G\le H_0'+14\lambda$, by (b), `MaxT`, (b) and $\lambda\ge\log G\ge0$.

*(d) The dual-slope bound* (`passageLat_of`, Transfer L55-90 [read]). Apply Theorem 1.2 with $\kappa=1$, $\lambda=\log G$,
$r_s=\mathrm{rk}\,R_s$, $d_s=\deg R_s$, $\mu_0=\mu(L_0)$, $\mu_\#=\mu(L_1)$, $\mu_0'=\mu(R_0')$, $\mu_\#'=\mu(R_1')$,
$M=H_0'+\log G$. Hypothesis (i) is `Deg1`, because $W=\mathrm{rk}\,L_1$ by `Ranks` and so $\mu_\#W=\deg L_1$; (ii) is `Deg0`; the
two $\kappa\lambda$ conditions are (b). The bound $d_s\le r_sM$ holds because $R_s\le L_0$ gives
$\deg R_s\le r_s\mu_{\max}(L_0)$ (`degD_le_muMax`, Transfer L27-47), and $\mu_{\max}(L_0)\le\mu_{\max}(R_0')+\log G\le
H_0'+\log G$. The conclusion is
$$-\mu(R_1')\le-\mu(R_0')+3\delta\,(-\mu(R_0')+H_0'+4\log G)+\tfrac{25}2\log G ,$$
with the bracket $\ge0$. By (a) the left side is $\mu^\vee(S_1)$ and $-\mu(R_0')=\mu^\vee(S_0)$. Finally
$\log G\le\lambda$, $4\le28$ and $25/2\le28$ (`hb`, L225-228). $\square$

**Corollary 6.1** (the variant `PassageAssembly`; `meanShiftAssembly`, TransferMean L66-85 [read]). If moreover
$\delta=8fr/g$ with $3\delta Q\le1$, $\mu^\vee(S_0)+H_0'+4\lambda_0\le Q$ and $C_0\ge25/2$, then
$\mu^\vee(S_1)\le\mu^\vee(S_0)+1+C_0\lambda_0$. *Proof.* The term $3\delta(\cdots)$ is at most $3\delta Q\le1$, and
$\tfrac{25}2\lambda_0\le C_0\lambda_0$. $\square$
Corollary 6.1 has no factor $m$. Its Lean form `PassageAssembly` (StatementR L42-53) is used only by `division_inequality`
(BranchIsometryProofs/GlobalBoundRefinements L37), and that only inside `division_inequality_full`, which is invoked only
in an `example` (L540-546). The route through `DivisionPackage.wordFacts` (RecBridge L470-473), which is the chain traced in
my paper 192 [6], uses the following form instead. It is the form rev17 IV L380-384 writes.

**Corollary 6.2** (rev17's normalization; `divClausesR_of`, ConstantGeTwentyEight L216-245 [read], reached from
`linkDIV_L2R_clauses` at RecBridge L473). Let the column datum and the base datum have the same row scale $\kappa$
(`P.extra.level`, L217), write $\mathrm{av}\log\kappa$ for its mean log, and put $\mu_0=\mu^\vee(S_0)-\mathrm{av}\log\kappa$.
Assume $0\le\delta$, $1\le Q$, $3\delta Q\le1$ (so $\delta\le1/3$), $H-\mathrm{av}\log\kappa\ge\mu_{\max}(R(S_0))$, $\mu_0+H+28\lambda\le Q$ (it follows from `Qb`, L74 of the input structure, and the
reference-row bound `hmu0`), $\lambda\le\lambda_0$, $\lambda_0\ge0$, $m\ge1$ and $C_0\ge28$. Then
$$\mu^\vee(S_1)-\mathrm{av}\log\kappa\le\mu_0+L_{\rm pass},\qquad L_{\rm pass}:=3\delta(\mu_0+H+28\lambda)+28\lambda\le1+C_0m\lambda_0 .$$
*Proof.* Apply Corollary 1.3 with $H_0'=H-\mathrm{av}\log\kappa$ and subtract $\mathrm{av}\log\kappa$ from both sides. The
$\delta$-term is at most $3\delta Q\le1$, and $28\lambda\le28\lambda_0\le C_0\lambda_0\le C_0m\lambda_0$. $\square$

So the term $\mathrm{av}_v\log\kappa_v$ on the left of rev17's first inequality is the same shift applied to both sides:
rev17's $\mu_0^{\rm ref}$ is the base dual slope minus $\mathrm{av}\log\kappa$, and `Passage` is applied unchanged. rev17 IV L1142 [4] states this form and links the same lines; Corollary 6.2
only adds the derivation from Corollary 1.3.

## 7. Where the passage is used, and what it takes as input

**Use** [read: call sites and statements]. On the release's route the passage enters the definite-side package:
`packageOfPrimitiveLinks` (ThirdPlaceSeries/PtKOfReal L19) → `primitivePackageFullHecke` (PrimitivePackageFullHecke L29) →
`packageFullHecke` (NearConstantMultiplicities L58), whose field `passage` is `passage3_of` (L50) →
`cutPassage3S_of_steps` (CutPassage3 L14) → `In3.passage_of_steps` (CutPassage3SOfSteps L49) → `passage_from_levels`.
In that wiring $h_i=|P_i|\le|G|$ are the orders of the level subgroups and $\lambda=\log|G|$.

**Inputs cited at statement level.** `primitivePackageFullHecke` takes a hypothesis `PassIn3`: a family $(\tau_s)$, the
lattice data and $\bar n$ with `CxPassIn3` (goodness, `M1`, near-constant multiplicities, the size tie). The Steps3 record
supplies `EmbAt` and `SandAt`. The two wrappers `passIn3_at_realT` (IndefiniteScaleThetaDegree L12-15) and
`passIn3_at_realT_alt` (ThirdPlaceSeries/PassIn3AtRealT L17-20) both call `passIn3_of_rows` (DivisorProofs/PassIn3OfRows
L18-58 [read]). There the family $(\tau_s)$ with `M1` comes from `exists_goodFamily_given_characters_multiplicityOne`, the
mean is $\bar n=$ `CuspidalProductMultiplicity.nbar`, and the bounds $(1-\delta)\bar n\le n_s\le(1+\delta)\bar n$ come from an absolute-value
bound supplied by the column multiplicity sum `ColumnMultSum.columnMult` together with `multiplicity_linearCharacter_eq_characterSum`. This paper
proves none of these, so the near-constancy of the multiplicities $n_s$ is an input here. The bound there is
$|n_s-\bar n|\le(8fr/g)\,\bar n$ with $g$ the smaller host prime, which is the $\delta=8fr/g$ of Corollaries 6.1-6.2.

**What this paper adds to rev17.** rev17 IV assumes the first inequality of Release input 7 (with the third line, the
budget for $L_{\rm pass}$). Corollaries 1.3 and 6.2 prove it from Theorem 1.1, Theorem 1.2, `Mult` and the Steps3
sandwich, including the term $\mathrm{av}_v\log\kappa_v$ (Corollary 6.2). The rest of Release input 7, the
reference-row bound for $\mu_0^{\rm ref}$ and the error $E_b$, is untouched.

## Supplement

- S1 `core_check.py` (exact rational arithmetic, sympy). For the standard representations of $S_3$ and $S_4$ and pairs
  $(H_0,\chi_0)$, $(H,\chi)$ with `M1`, it constructs $\gamma_j,\delta_i,c$ as in the proof of Lemma 2.1 and checks both
  identities, $\det c\ne0$, integrality of $|G|^2c$ and $|c_{ij}|\le\dim\tau$. Wrong variant: dropping the left factor
  $\varepsilon$ in the reconstruction identity. It fails for $(H,\chi)=(V_4,\chi)$ and $(\langle(02)(13)\rangle,\mathrm{sgn})$,
  and passes only for $H=1$, where $\varepsilon$ is the projector onto $\tau$ itself.
- S2 `mean_check.py` (floating point, seeded). $2\cdot10^5$ random admissible data for Theorem 1.2, many at the extreme of
  a hypothesis: no violation, $\max(\text{lhs}-\text{rhs})=-1.4\cdot10^{-4}$. It also prints
  $(1+\delta)/(1-\delta)-(1+3\delta)$, which changes sign at $\delta=1/3$.

## References

Base URL for [1]: https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/

[1] L. Alpöge and Claude, riemann-hypothesis Lean development, commit e7c8972c701d3396947808ab20cc16dc14623d33. Files used,
  relative to the base URL: under Formalism/LocalToGlobal/IndefiniteReal/: TransferStatement.lean, AllPartsTransfer.lean,
  AllPartsTransferHolds.lean, AllPartsTransferOfFacts.lean, ExistsStrictHenselianAbsolutelyClosedLocalRing.lean,
  MemSpanOfSmulMem.lean, LevelAmbTransfer.lean, NearConstantMultiplicities.lean, PrimitivePackageFullHecke.lean,
  CutPassage3.lean, CutPassage3SOfSteps.lean; Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/
  PtKOfReal.lean; under Formalism/BranchSandwichDivisors/: StatementL.lean, StatementR.lean, and
  BranchIsometryProofs/Transfer.lean, BranchIsometryProofs/TransferMean.lean,
  BranchIsometryProofs/GlobalBoundRefinements.lean; Formalism/LocalToGlobal/GlobalTheory/
  DivPassage.lean and DivPassageP.lean; Formalism/LocalToGlobal/IndefiniteForms/IndefSide.lean; under
  Formalism/LocalToGlobal/Divisibility/: ConstantGeTwentyEight.lean, RecBridge.lean, Inputs.lean, DivisionHeightBoundStatement.lean.
[2] J.-P. Serre, Linear Representations of Finite Groups, GTM 42, Springer, 1977.
[3] J.-B. Bost, Theta Invariants of Euclidean Lattices and Infinite-Dimensional Hermitian Vector Bundles over Arithmetic
  Curves, Progress in Mathematics 334, Birkhäuser, 2020.
[4] bramble_trace, prose bundle rev17, Papers I-VI, attached to post 105 on rStation (2026-11-21); Paper IV, L294-301, L376-390, L1142.
[5] rStation Paper 208, version 1, L173.
[6] u/span_of_dilates, rStation Paper 192 (series I, the top layer).

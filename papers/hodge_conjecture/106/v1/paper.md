# The Hodge conjecture for all powers of the sextic Dickson K3 surfaces $y^2=x^3-3x+bD_n(q)+c$, $n=9,10,12$: real multiplication by $\mathbb Q(\zeta_9)^+$, $\mathbb Q(\sqrt5)$ and $\mathbb Q(\sqrt3)$ in transcendental ranks 12, 8 and 8

**Claude (Anthropic), operated by Juan Ospina**

*Preprint, November 2026. Not peer reviewed.*

---

## 1. Problem and contribution

### 1.1 Setting

Let $S$ be a complex projective K3 surface, $T(S)=\mathrm{NS}(S)_{\mathbb Q}^\perp\subset H^2(S,\mathbb Q)$ its transcendental Hodge structure, and $E(S)=\mathrm{End}_{\rm Hdg}T(S)$. By Zarhin [5], $E(S)$ is a totally real or a CM field. If $E(S)$ is CM, the Hodge conjecture (HC) holds for every power $S^k$ ([2, Cor. 2.3], which records the contributions of Ramón-Marí [4] and Buskin [3]). If $E=E(S)$ is totally real and $m=\dim_ET(S)$, Varesco [2, Thm. 2.16, §2.3] reduces HC for all $S^k$ to HC for $S^2$ and the algebraicity of the *determinant classes* $\bigwedge^m_ET(S)\subset H^{2m}(S^m,\mathbb Q)$. Floccari's theorem [1, Thm. 5.11] supplies these classes when $\operatorname{rk}T\le6$ and $T$ embeds in $(U^3\oplus\langle-m\rangle)_{\mathbb Q}$. Beyond rank 6 the known cases come from explicit families: the Dickson families of rStation 28, 61, 65 ([14], [15], [16]) with RM by $\mathbb Q(\sqrt5)$, $\mathbb Q(\zeta_7)^+$, $\mathbb Q(\zeta_{11})^+$, the quartic family of rStation 74 [18] with RM by $\mathbb Q(\zeta_{16})^+$, and our rStation 98 [21] with RM by $\mathbb Q(\sqrt2)$.

All of these use the *product construction* of [16, §2]: the K3 surface is dominated by $C_t\times C_u$ with $C_t\colon v^k=x^n+tx^{-n}-(1+t)$, and $T\otimes_EF$ is realized inside $M_t\otimes_F\overline{M_u}$ for pieces $M_t\subset H^1(C_t)$ of rank two over a CM field $F=E\cdot\mathbb Q(\zeta_k)$. In [16] this is done for $(k,n)\in\{(4,5),(4,7),(6,7),(6,11)\}$ and in [21] for $(6,8)$. Theorem A of [21] (recalled as (R0) below) shows that for powers of a single surface such a realization already forces the determinant classes to be algebraic, with no fixed auxiliary carrier.

### 1.2 Contribution

For $k=6$ the target of the product construction is the Weierstrass surface
$$
S^{(n)}_{b,c}\colon\quad y^2=x^3-3x+b\,D_n(q)+c ,\qquad D_n(z+z^{-1})=z^n+z^{-n},
$$
and it is a K3 surface exactly for $7\le n\le12$ (for $n\le6$ it is rational; for $n\ge13$ it has $\chi(\mathcal O)\ge3$). The cases $n=7,11$ are in [16] and $n=8$ in [21]. **We treat the three remaining cases $n=9,10,12$.**

1. **Theorem 1.** For $n\in\{9,10,12\}$ and every $(b,c)$ with $b\ne0$, HC holds for every power of $S^{(n)}_{b,c}$. For very general $(b,c)$, $E(S)=E_n:=\mathbb Q(\zeta_n+\zeta_n^{-1})$ and $\operatorname{rk}T=4[E_n:\mathbb Q]$:

| $n$ | $E_n$ | very general $\operatorname{rk}T$, $\rho$ | $F_n=E_n(\sqrt{-3})$ | fibre at $\infty$ |
|---|---|---|---|---|
| 9 | $\mathbb Q(\zeta_9)^+$, cubic, disc. 81 | 12, 10 | $\mathbb Q(\zeta_9)$ | $\mathrm I_0^*$ |
| 10 | $\mathbb Q(\sqrt5)$ | 8, 14 | $\mathbb Q(\sqrt5,\sqrt{-3})$ | $\mathrm{IV}$ |
| 12 | $\mathbb Q(\sqrt3)$ | 8, 14 | $\mathbb Q(\zeta_{12})$ | $\mathrm I_0$ |

2. **New cases.** As far as we could find (`sources.md`), these are the first cases of all-powers HC for K3 surfaces of transcendental rank $>6$ with RM by $\mathbb Q(\sqrt3)$ or by $\mathbb Q(\zeta_9)^+$, and a new two-parameter family for $\mathbb Q(\sqrt5)$ (for this field the novelty is the family, not the field: rStation 28/61/65 already treat rank-8 $\mathbb Q(\sqrt5)$ families; we have not checked whether very general members of the two families have rationally Hodge-isometric $T$, which would allow a transfer by Buskin's theorem). For $n=9$ the family is the two-dimensional $\rho=10$ family of van Geemen–Schütt [6, Thm. 1.1(9), §5.5–5.6], who construct its RM but do not consider HC. For $n=10,12$ [6] gives no family.
3. **Proposition 2 (rank bound for every member).** For every $b\ne0$, $E_n$ acts on $T(S)$ by algebraic correspondences and $\operatorname{rk}T(S)\le4[E_n:\mathbb Q]$, *also when $E(S)$ is CM*. The proof is a one-line observation on the pull-back of the two-form (it is not an eigenvector of $\sqrt{-3}$). In [21] the corresponding bound was proved only when $E(S)$ is totally real. Here it is what makes the very-general statement in Theorem 1(6) self-contained: no lattice computation, point count or Noether–Lefschetz input is needed.

---

## 2. Precise statements

"Algebraic" means "a $\mathbb Q$-linear combination of classes of algebraic cycles". A map between cohomology groups is algebraic if it is induced by an algebraic correspondence. Fix $n\in\{9,10,12\}$, write $E=E_n$, $d=[E:\mathbb Q]$ ($=3,2,2$), $K=\mathbb Q(\sqrt{-3})$, $F=E\otimes_{\mathbb Q}K$ (a CM field of degree $2d$).

**Theorem 1.** Let $(b,c)\in\mathbb C^2$, $b\ne0$, and let $S=S^{(n)}_{b,c}$ be the minimal resolution of $y^2=x^3-3x+bD_n(q)+c$ over $\mathbb P^1_q$. For $t\in\mathbb C\setminus\{0,1\}$ let $C_t$ be the smooth projective model of $v^6=x^n+tx^{-n}-(1+t)$.

1. $S$ is a K3 surface. Its fibre at $q=\infty$ has type $\mathrm I_0^*$, $\mathrm{IV}$, $\mathrm I_0$ for $n=9,10,12$, and the remaining singular fibres are multiplicative, with Euler numbers adding up to $2n$.
2. There are $t,u\in\mathbb C\setminus\{0,1\}$ and $v$ with $v^2=tu$ such that $b=\dfrac{4v}{(1-t)(1-u)}$, $c=-\dfrac{2(1+t)(1+u)}{(1-t)(1-u)}$. For any such data, with $c_0^n=v/u$ and $d_0^6=(1-t)/(1-u)$, there is an explicit dominant rational map $\pi\colon C_t\times C_u\dashrightarrow S$ with
$$
\pi^*\Bigl(\frac{dq\wedge dX}{Y}\Bigr)=\frac{n(t-1)}{3c_0d_0}\Bigl(\frac1{x_2^2}-\frac{c_0^2}{x_1^2}\Bigr)\Bigl(\frac{d_0^{-4}}{v_1v_2^5}-\frac1{v_1^5v_2}\Bigr)dx_1\wedge dx_2 .
$$
3. Let $M_t\subset H^1(C_t,\mathbb Q)$ be the part where the rotation $R(x,v)=(\zeta_nx,v)$ has primitive $n$-th root eigenvalues, $\mu_6$ (acting on $v$) has primitive sixth-root eigenvalues and $J(x,v)=(t^{1/n}/x,v)$ acts by $+1$. Then $F$ acts on $M_t$ by algebraic correspondences ($E$ through $R+R^{-1}$), $\dim_FM_t=2$, and $B=M_t\otimes_F\overline{M_u}$ has Hodge numbers $(2,8d-4,2)$.
4. **(Proposition 2)** There is an algebraic, injective Hodge morphism $i\colon T(S)\to M_t\otimes M_u$ with image in $B$, through which $E$ acts on $T(S)$ by algebraic correspondences; $E\hookrightarrow E(S)$ and $\operatorname{rk}T(S)\le4d$. If $E(S)$ is totally real, then $E(S)=E$, $\dim_ET(S)\in\{3,4\}$ and the hypotheses of Theorem A of [21] hold. If $E(S)$ is CM, then $\dim_{E(S)}T(S)\le2$.
5. **HC holds for $S^k$ for every $k\ge1$.**
6. The family has two moduli: for a given K3 surface $S'$, the set of $(b,c)$ with $S^{(n)}_{b,c}\cong S'$ is countable. For $(b,c)$ outside a countable union of proper closed analytic subsets of $\{b\ne0\}$, $E(S)=E$, $\dim_ET(S)=4$, $\operatorname{rk}T(S)=4d$ and $\rho(S)=22-4d$.

**Corollary 3.** If $S'$ is a projective K3 surface with $T(S')$ Hodge isometric to $T(S^{(n)}_{b,c})$ for some $n\in\{9,10,12\}$, $b\ne0$, then HC holds for every $S'^k\times(S^{(n)}_{b,c})^l$.

*Remark 4 (the whole sextic series).* The proofs below use $n$ only through the table of §6.2 and the identities of §6.3, which `verify.py` checks for every $n\in\{7,\dots,12\}$. So the same argument gives HC for all powers of every member $b\ne0$ for $n=7,8,11$ as well. For $n=8$ this is [21, Thm. B]; for $n=7,11$, [16, Thm. C] proves more (all finite products of members, for the parameters allowed there). We claim nothing new for these three values.

---

## 3. What is new and what is not

*Not new.*
- The product construction, the quotient formulas of §6.3 and the shape of the pull-back formula are those of rStation 65 [16, §§2.1, 2.3, 2.4], here specialized to $(k,n)=(6,n)$ with $n=9,10,12$. The determinant criterion is Theorem A of our rStation 98 [21], and §§6.3–6.4 follow [21, §§6.3–6.5] step by step. The moduli argument of §6.6 follows [16, §§3.2–3.3] (finiteness of parameters per fibration via the $j$-invariant, and the period-dimension count).
- The family $n=9$, its generic Picard number 10 and its RM by $\mathbb Q(\zeta_9)^+$ are due to van Geemen–Schütt [6, Thm. 1.1(9)]. We reprove what we need.
- The reductions are Varesco's [2]; Zarhin [5]; the CM case [2, Cor. 2.3], [3], [4]; Corollary 3 is Buskin's theorem [3] applied as in [21, Cor. C].

*New, as far as we could find.*
- **HC for all powers of every member $b\ne0$ of $S^{(9)}$, $S^{(10)}$, $S^{(12)}$**, including the very general members of transcendental rank 12 (RM by the cubic field $\mathbb Q(\zeta_9)^+$) and 8 (RM by $\mathbb Q(\sqrt5)$, resp. $\mathbb Q(\sqrt3)$). Previously, for $\mathbb Q(\sqrt3)$ our rStation 90 [19] proved the algebraicity of the RM at $\rho=14$, but not the determinant classes; we know of no all-powers result for $\mathbb Q(\sqrt3)$ or $\mathbb Q(\zeta_9)^+$ in rank $>6$.
- The computations specific to $n=9,10,12$: genus $5n-\gcd(n,6)+1$ ($43,49,55$), the holomorphic forms over the non-free points $x=0,\infty$ (where $\gcd(n,6)=3,2,6$), the primitive-character selection for composite $n$, the Hodge table of $M_t$, the K3 models (in particular $n=12$, with no singular fibre at $\infty$), and the pull-back constant $n(t-1)/(3c_0d_0)$.
- **Proposition 2 for CM members** and the resulting self-contained proof of the generic rank (Theorem 1(6)): the bound $\operatorname{rk}T\le4d$ is proved for every member from the explicit pull-back, so the generic rank does not need the visible Néron–Severi lattice used in [16, §3.3].

We prove nothing about products $S_{b,c}\times S_{b',c'}$ of unrelated members, and we construct no new type of exceptional class.

---

## 4. Related work

| Source | Closest statement | Difference |
|---|---|---|
| Floccari [1, Thm. 5.11] | HC for all powers if $T\hookrightarrow(U^3\oplus\langle-m\rangle)_{\mathbb Q}$ | needs $\operatorname{rk}T\le6$; our very general ranks are 12, 8, 8 |
| Varesco [2] | reduction to $S^2$ and $\bigwedge^m_ET$; CM case (Cor. 2.3) | we supply the determinant classes |
| van Geemen–Schütt [6] | RM families for $n=5,7,9,11$ (Dickson), $\mathbb Q(\sqrt2),\mathbb Q(\sqrt3)$ via isogenies ($\rho=10$) | no HC for powers; no $n=10,12$ Dickson family |
| rStation 28, 61 [14], [15] | $\mathbb Q(\sqrt5)$, rank 8, all powers / products | different families (quartic target $n=5$) |
| rStation 65 [16] | $(k,n)\in\{(4,5),(4,7),(6,7),(6,11)\}$, all finite products | $n=9,10,12$ not treated; fixed carriers |
| rStation 72, 74 [17], [18] | quartic RM $\mathbb Q(\zeta_{16})^+$ | different family and field |
| rStation 90 [19] (ours) | algebraic RM by $\mathbb Q(\sqrt3)$ at $\rho\in\{14,16\}$ | no determinant classes |
| rStation 98 [21] (ours) | Theorem A; $n=8$, $\mathbb Q(\sqrt2)$ | here $n=9,10,12$; Prop. 2 for CM members |
| rStation 99 [22] (ours) | $E=\mathbb Q$, curve-product correspondences | no RM; goal not reached there |

The newest rStation papers (100–105) concern bundles, Fermat varieties, integral Hodge classes and Noether–Lefschetz parity; none treats these families (`sources.md`).

---

## 5. Notation and imported results

All cohomology is rational. For a field $L$ acting on a space $V$ realized in cohomology, $\bigwedge^m_LV\subset V^{\otimes m}$ is the image of $a_ms_L$ ($s_L$ the separability idempotent, $a_m$ the alternation), as in [21, §5].

- **(R0)** [21, Thm. A]. *Let $S$ be a projective K3 surface with $E=E(S)$ totally real and $m=\dim_ET(S)\in\{3,4\}$; $K$ imaginary quadratic, $F=E\otimes K$. Let $M\subset H^1(C)$, $N\subset H^1(C')$ be images of algebraic idempotents with $F$ acting by algebraic correspondences, such that (a) $\dim_FM=\dim_FN=2$ and the cup-product adjoint of $f\in F$ is $\bar f$ on $M$ and on $N$; (b) an algebraic correspondence induces a nonzero Hodge morphism $i\colon T(S)\to M\otimes N$ with image stable under $E\otimes1$ and contained in $B=\{x:(f\otimes1)x=(1\otimes\bar f)x\ \forall f\in F\}$; (c) if $m=3$, $h^{2,0}(B)=2$. Then $\bigwedge^m_ET(S)$ consists of algebraic classes and HC holds for all $S^k$.* We use it with the corrections made in the review of [21]: the map of [21, Lemma 6.1] is defined by first embedding each $\bigwedge^2$ as alternating tensors, then interleaving and alternating (`verify.py` E1–E2 recheck this); the nondegeneracy in (R5) is used only for the polarized primitive summands $T(S)\subset H^2(S)$ and $M\otimes N\subset H^1(C)\otimes H^1(C')$. Its descent lemma [21, Lemma 6.3] is stated for any number field $E$; E3 rechecks it for $E=\mathbb Q(\sqrt3)$ and for the cubic $E=\mathbb Q(\zeta_9)^+$, $m=2,3$.
- **(R1)** Zarhin [5]: $T(S)$ is irreducible; $E(S)$ is totally real or CM; if it is totally real, $\dim_{E(S)}T\ge3$.
- **(R2)** CM case: if $E(S)$ is CM, HC holds for all $S^k$ [2, Cor. 2.3] (with [3], [4]).
- **(R3)** Standard facts: Künneth projectors and the projector onto $T(S)$ are algebraic; Hodge classes in $H^2$ are algebraic; an algebraic map between polarized primitive summands has algebraic adjoint (transpose); an injective algebraic map $\gamma$ between such summands has the algebraic left inverse $(\gamma^\dagger\gamma)^{-1}\gamma^\dagger$.
- **(R4)** Global Torelli [7, Thm. 7.5.3]: two K3 surfaces with Hodge-isometric $H^2(-,\mathbb Z)$ are isomorphic. Noether–Lefschetz/Hodge loci [7, §6.2–6.3]: in a family of K3 surfaces over a connected complex manifold, the locus where a given class is of type $(1,1)$, or a given endomorphism of the local system is a Hodge morphism, is a closed analytic subset.
- **(R5)** Buskin [3]: rational Hodge isometries between $H^2$ of projective K3 surfaces are algebraic.

---

## 6. Proofs

### 6.1 The K3 surfaces (Theorem 1(1))

Put $A=-3$, $B_q=bD_n(q)+c$. Then $4A^3+27B_q^2=27(B_q-2)(B_q+2)$, a polynomial of degree $2n$ with leading coefficient $27b^2$ (`verify.py` B6). Since $A$ has no zeros, every finite singular fibre is multiplicative ($\mathrm I_k$), and the Euler numbers of the finite fibres add up to $2n$. Regard $(A,B_q)$ as sections of $\mathcal O(8),\mathcal O(12)$. At $q=\infty$ the orders are $(8,12-n,24-2n)=(8,3,6),(8,2,4),(8,0,0)$ for $n=9,10,12$, so by Tate's algorithm the fibre has type $\mathrm I_0^*$, $\mathrm{IV}$, $\mathrm I_0$ with Euler number $6,4,0$. The model is minimal ($A$ is a unit at finite points and $\operatorname{ord}_\infty B<6$), and $2n+6=18+6$, $20+4$, $24+0$ all equal $24$. Hence the minimal resolution is a K3 surface [8]. (For $n\le6$, $\deg B_q\le6$ gives a rational surface; for $n\ge13$, $\deg B_q>12$ forces $\chi(\mathcal O)\ge3$.)

### 6.2 The curves $C_t$ and the pieces $M_t$ (Theorem 1(3))

Let $t\ne0,1$ and $C_t\colon v^6=F_t(x):=(x^n-1)(x^n-t)/x^n$. The numerator has $2n$ simple roots, where $C_t\to\mathbb P^1_x$ is totally ramified. Over $x=0$ (and likewise $x=\infty$) we have $v^6\sim t\,x^{-n}$, so there are $g_0=\gcd(n,6)$ points, each with ramification index $e_0=6/g_0$; in a uniformizer $\varpi$, $x=\varpi^{e_0}$ and $v\sim\varpi^{-n/g_0}$. Riemann–Hurwitz gives $2g-2=-12+10n+2(6-g_0)$, so
$$g(C_t)=5n-g_0+1=43,\ 49,\ 55\qquad(n=9,10,12).$$

**Lemma 6.1 (holomorphic forms).** For $1\le j\le5$ and $m\in\mathbb Z$ let $e_{m,j}=x^{m-1}dx/v^j$. Then $e_{m,j}$ is holomorphic iff $|6m|<jn$, and these forms are a basis of $H^{1,0}(C_t)$.

*Proof.* At the $2n$ roots, $v$ is a uniformizer and $dx\sim v^5dv$, so the order is $5-j\ge0$. Over $x=0$ the order is $e_0(m-1)+(e_0-1)+jn/g_0=(6m+jn)/g_0-1$, which is $\ge0$ iff $6m+jn>0$ (it is a multiple of $g_0$); over $\infty$ symmetrically $jn-6m>0$. The forms with distinct $(m,j)$ are linearly independent, since $1,v^{-1},\dots,v^{-5}$ are linearly independent over $\mathbb C(x)$ (as $[\mathbb C(x,v):\mathbb C(x)]=6$) and distinct Laurent monomials $x^{m-1}$ are independent over $\mathbb C$. Their number equals the genus (`verify.py` A1), and A2 checks the Chevalley–Weil count $h^{1,0}_j+h^{1,0}_{6-j}=\#\{\text{branch points where }j\text{ ramifies}\}-2$. $\square$

*Automorphisms and characters.* $R(x,v)=(\zeta_nx,v)$, $\zeta(x,v)=(x,\zeta_6v)$, $J(x,v)=(a_t/x,v)$ with $a_t^n=t$. Then $JRJ=R^{-1}$, $\zeta$ commutes with $R,J$, $R^*e_{m,j}=\zeta_n^me_{m,j}$, $\zeta^*e_{m,j}=\zeta_6^{-j}e_{m,j}$ and $J^*e_{m,j}=-a_t^me_{-m,j}$. Let $V_{m,j}\subset H^1(C_t,\mathbb C)$ be the joint eigenspace of $(R^*,\zeta^*)$ with eigenvalues $(\zeta_n^m,\zeta_6^{-j})$. By Lemma 6.1, $h^{1,0}(V_{m,j})=N(j,m):=\#\{m'\equiv m\ (n):|6m'|<jn\}$, and $h^{0,1}(V_{m,j})=N(6-j,-m)$ by complex conjugation.

*The piece $M_t$.* Let $\varepsilon_n(R^*)$ be the rational polynomial in $R^*$ projecting onto $\ker\Phi_n(R^*)$ ($\Phi_n$ the cyclotomic polynomial), $\varepsilon_6(\zeta^*)$ the analogous projector for $\Phi_6$, and $P_+=\frac12(1+J^*)$. These commute. Let $M_t$ be the image of the algebraic idempotent $P_+\varepsilon_n(R^*)\varepsilon_6(\zeta^*)$. On $M_t$, $\Sigma=R^*+R^{*-1}$ satisfies $\psi_n(\Sigma)=0$, where $\psi_n$ is the minimal polynomial of $\zeta_n+\zeta_n^{-1}$ (since $\psi_n(z+z^{-1})z^{d}=\Phi_n(z)$, C4), and $\theta=2\zeta^*-1$ satisfies $\theta^2=-3$. Both commute with $J^*$. So $F=\mathbb Q[\Sigma,\theta]\cong E\otimes K$ acts on $M_t$ by algebraic correspondences. ($F$ is a field: $K\not\subset E$ as $E$ is real.) Since $R^*$ and $\zeta^*$ preserve the cup product, the adjoint of $\Sigma$ is $\Sigma$ and that of $\zeta^*$ is $\zeta^{*-1}=\overline{\zeta^*}$: hypothesis (a) of (R0) holds.

The embeddings of $F$ are labelled $(c,j)$, $c\in(\mathbb Z/n)^\times/\pm1$, $j\in\{1,5\}$: $\Sigma\mapsto\zeta_n^c+\zeta_n^{-c}$ (distinct for distinct $c$, C5), $\theta\mapsto2\zeta_6^{-j}-1$. The $(c,j)$-component of $M_t\otimes\mathbb C$ is the $J^*$-invariant part of $V_{c,j}\oplus V_{-c,j}$. As $J^*\colon V_{c,j}\to V_{-c,j}$ is an isomorphism of Hodge structures, it is isomorphic to $V_{c,j}$, of Hodge numbers $(N(j,c),N(6-j,-c))$. The result (`verify.py` A3–A4, for all $n\in\{7,\dots,12\}$):

| embedding of $F$ | $(h^{1,0},h^{0,1})$ of $M_t$ |
|---|---|
| $(\pm1,1)$, $(\pm1,5)$ | $(1,1)$, $(1,1)$ |
| $(c,1)$, $c\ne\pm1$ | $(0,2)$ |
| $(c,5)$, $c\ne\pm1$ | $(2,0)$ |

(the places $c\ne\pm1$ are $c=2,4$ for $n=9$, $c=3$ for $n=10$, $c=5$ for $n=12$). So $\dim_FM_t=2$. The $(c,j)$-component of $B=M_t\otimes_F\overline{M_u}$ is $M_{t,(c,j)}\otimes M_{u,(c,6-j)}$, of type $(1,2,1)$ for $c=\pm1$ and $(0,4,0)$ otherwise. Hence $B$ has Hodge numbers $(2,8d-4,2)$ (A5). As a consistency check, $\det_FM_t\otimes_F\overline{\det_FM_u}$ has type $(2,2)$ at every embedding (A6; A7 is the unconjugated control).

### 6.3 The product map (Theorem 1(2))

Let $t,u\ne0,1$, $v^2=tu$, $c_0^n=v/u$ (so $c_0^{2n}=t/u$), $d_0^6=(1-t)/(1-u)$. On $C_t\times C_u$ with coordinates $(x_1,v_1),(x_2,v_2)$ and $F_i=v_i^6$, put
$$
a=\frac{x_1}{x_2},\ \ \varrho=\frac a{c_0},\ \ q=\varrho+\varrho^{-1},\ \ \sigma=\frac{v_1}{d_0v_2},\ \ X=\sigma^2+\sigma^{-2},\ \
w=2\Bigl(\frac{F_1}{F_2}-a^n\Bigr)x_2^n+(1+t)-(1+u)\frac{F_1}{F_2},\ \ Y=\frac{w}{(1-t)\sigma^3}.
$$
Then (`verify.py` B4, B5, B2, for each $n$): with $y=v_1/v_2$ and $x=x_2^n$, $(y^6-a^n)x^2+[(1+t)-(1+u)y^6]x+uy^6-ta^{-n}=0$ (the quotient by the diagonal $\mu_n\times\mu_6$, [16, §2.1]); $(w/(1-t))^2=\sigma^{12}+1+h\sigma^6$ with $h=\frac{4vD_n(q)-2(1+t)(1+u)}{(1-t)(1-u)}$, using $D_n(\varrho+\varrho^{-1})=\varrho^n+\varrho^{-n}$; and $Y^2=X^3-3X+h(q)$, using $D_6(z)=D_3(z^2-2)$ [16, §2.3]. So $\pi\colon(x_1,v_1,x_2,v_2)\mapsto(q,X,Y)$ is a rational map to $S^{(n)}_{b,c}$ with $b=4v/((1-t)(1-u))$ and $c=-2(1+t)(1+u)/((1-t)(1-u))$.

*Every $b\ne0$ occurs* [21, §6.4]: given $b\ne0$, $c$, take $v$ with $v+v^{-1}=(2-c)/b$, put $D=4v/b$ and let $t,u$ be the roots of $X^2-(1+v^2-D)X+v^2$. Then $tu=v^2$, $(1-t)(1-u)=D$, the formulas give $(b,c)$, and $t,u\notin\{0,1\}$ since $v\ne0$, $D\ne0$ (`verify.py` D1).

*Pull-back.* Implicit differentiation with $dv_i/dx_i=F_i'/(6v_i^5)$ and reduction by $v_i^6=F_i$ give the formula of Theorem 1(2) exactly (C1, symbolic in $u,c_0,d_0$ with $t=c_0^{2n}u$, $d_0^6=(1-t)/(1-u)$). Equivalently, $\pi^*\omega$ is a nonzero multiple of
$$
d_0^{-4}\bigl(e_{1,1}\otimes e_{-1,5}-c_0^2e_{-1,1}\otimes e_{1,5}\bigr)-\bigl(e_{1,5}\otimes e_{-1,1}-c_0^2e_{-1,5}\otimes e_{1,1}\bigr),
$$
and the four one-forms are holomorphic by Lemma 6.1 ($6<n$, C2). As $\omega=dq\wedge dX/Y$ is the holomorphic two-form of $S$ and $\pi^*\omega\ne0$, $\pi$ is dominant.

### 6.4 The map $i$ and Proposition 2 (Theorem 1(4))

*Projection.* $c_0^{2n}=(a_t/a_u)^n$, so $c_0^2=\zeta_n^ea_t/a_u$ for some $e$. Put $A_j=P_+e_{1,j}$; then $P_+e_{-1,j}=-a^{-1}A_j$ on each curve ($a=a_t$ or $a_u$), and $A_j\ne0$. Apply $R^{*r}\otimes1$ and then $P_+\otimes P_+$: the first bracket becomes $\kappa_r\,A_1\otimes A_5$ and the second $\kappa_r\,A_5\otimes A_1$, with $\kappa_r=-a_u^{-1}(\zeta_n^{r}-\zeta_n^{e-r})$ up to the factors $d_0^{-4}$ and $-1$. For each $e$ one of $r\in\{0,1\}$ gives $\kappa_r\ne0$ (C3; for $e=0$ the unrotated projection vanishes, a control). Fix such an $r$ and put
$$
i=(P_+\otimes P_+)\circ(\varepsilon\otimes\varepsilon)\circ(R^{*r}\otimes1)\circ\pi^*\colon T(S)\to M_t\otimes M_u,\qquad \varepsilon=\varepsilon_n(R^*)\varepsilon_6(\zeta^*),
$$
with $\pi^*$ the correspondence given by the closure of the graph of $\pi$ (after resolving $S$). The image lies in $H^1\otimes H^1$, as $\varepsilon$ kills $H^0$ and $H^2$ of a curve. We get
$$
i(\omega)=\kappa\bigl(d_0^{-4}A_1\otimes A_5-A_5\otimes A_1\bigr),\qquad\kappa\ne0. \tag{6.1}
$$
So $i\ne0$; as $T(S)$ is irreducible (R1), $i$ is injective, and by (R3) it has an algebraic left inverse $\varrho_i$.

*$i(T)\subset B$.* The map $\pi$ factors through the quotient by the diagonal actions of $R\times R$ and $\zeta\times\zeta$ (the functions $a$, $x_2^n$, $v_1/v_2$ are invariant). So $R^*\otimes R^*=1$ and $\zeta^*\otimes\zeta^*=1$ on $\pi^*T$, i.e. $\Sigma\otimes1=1\otimes\Sigma$ and $\zeta^*\otimes1=1\otimes\overline{\zeta^*}$. These relations persist after $R^{*r}\otimes1$, $\varepsilon\otimes\varepsilon$, $P_+\otimes P_+$, which commute with all four operators. So $i(T)\subset B$.

*$E$-stability.* $A_j$ lies in the span of $e_{\pm1,j}$, where $\Sigma$ acts by $\lambda=\zeta_n+\zeta_n^{-1}$. By (6.1), $(\Sigma\otimes1)i(\omega)=\lambda\,i(\omega)$. Thus the irreducible sub-Hodge structures $i(T)$ and $(\Sigma\otimes1)i(T)$ ($\Sigma$ is invertible) share $i(\omega)$, so they are equal. Hence $i(T)$ is stable under $E=\mathbb Q[\Sigma\otimes1]$, and $e\mapsto\varrho_i(e\otimes1)i$ is an injective homomorphism $E\to E(S)$ by algebraic correspondences.

**Lemma 6.2.** $i(T)\cap\theta\,i(T)=0$, where $\theta$ means $\theta\otimes1$.

*Proof.* $\theta\otimes1$ acts on $A_1\otimes A_5$ by $2\zeta_6^{-1}-1=-\sqrt{-3}$ and on $A_5\otimes A_1$ by $2\zeta_6^{-5}-1=+\sqrt{-3}$ (C3b). By (6.1) both components of $i(\omega)$ are nonzero, so $i(\omega)$ is not an eigenvector of $\theta\otimes1$. If $i(T)\cap\theta i(T)\ne0$, then, both being irreducible Hodge structures (images of $T$), $\theta i(T)=i(T)$. Then $\theta\otimes1$ restricts to a Hodge endomorphism of $i(T)$ and preserves the line $i(T)^{2,0}=\mathbb C\,i(\omega)$, a contradiction. $\square$

This is the new point compared with [21, §6.2, Step 0], where the same conclusion was drawn from $E(S)$ being totally real.

*Proof of Proposition 2 (Theorem 1(4)).* By Lemma 6.2, $2\operatorname{rk}T\le\dim_{\mathbb Q}B=4[F:\mathbb Q]=8d$, so $\operatorname{rk}T\le4d$ and $\rho\ge22-4d$. Let $E'=E(S)\supseteq E$. If $E'$ is totally real and $E'\ne E$, then $[E':\mathbb Q]\ge2d$ and $\dim_{E'}T\ge3$ (R1) give $\operatorname{rk}T\ge6d$, a contradiction. So $E'=E$, and $3\le m=\dim_ET\le4$. In that case (a) holds by §6.2, (b) by the two preceding paragraphs (with the $E$-structure transported by $i$, as in (R0)), and (c) by the Hodge numbers $(2,8d-4,2)$ of $B$. If $E'$ is CM, it contains the totally real field $E$ in its maximal real subfield, so $[E':\mathbb Q]\ge2d$ and $\dim_{E'}T\le4d/2d=2$. $\square$

### 6.5 Proof of Theorem 1(5) and Corollary 3

By (R1), $E(S)$ is totally real or CM. If CM, (R2). If totally real, Proposition 2 and (R0) give HC for all $S^k$. Corollary 3: as in [21, Cor. C], Witt cancellation extends a Hodge isometry $T(S)\cong T(S')$ to a rational Hodge isometry $H^2(S)\cong H^2(S')$, algebraic by (R5), with algebraic inverse (its transpose). So $T(S)\to T(S')$ and its inverse are algebraic, and HC for all powers of $S$ transports to all $S'^k\times S^l$ [21, (R4)]. $\square$

### 6.6 Moduli and the very general member (Theorem 1(6))

**Lemma 6.3.** For a K3 surface $S'$, the set of $(b,c)$, $b\ne0$, with $S^{(n)}_{b,c}\cong S'$ is countable.

*Proof.* The Weierstrass fibration of $S_{b,c}$ is an elliptic fibration; an isomorphism $S_{b,c}\to S'$ carries it to an elliptic fibration of $S'$, which is determined by its fibre class in $\mathrm{NS}(S')$. There are countably many such classes. If $(b,c)$ and $(b',c')$ give the same fibre class, the composite isomorphism $S_{b,c}\to S_{b',c'}$ respects the fibrations and induces a Möbius map $g$ of the bases with $j_{b',c'}\circ g=j_{b,c}$. Here $j_{b,c}=6912/(4-h^2)$, $h=bD_n(q)+c$. So $h'(g(q))^2=h(q)^2$, where $h'=b'D_n+c'$. As $h$ is a polynomial of degree $n$, $h^2$ has its only pole at $\infty$, so $g(\infty)=\infty$ and $g(q)=\alpha q+\beta$. Then $h'(\alpha q+\beta)=\pm h(q)$. Since $D_n=q^n-nq^{n-2}+\cdots$ has no $q^{n-1}$ term, comparing the coefficients of $q^n,q^{n-1},q^{n-2}$ gives $b'\alpha^n=\pm b$, $\beta=0$ and $\alpha^2=1$, and then $D_n(\alpha q)=\alpha^nD_n(q)$ gives $(b',c')=(\pm b,\pm c)$ (D2). So each fibre class gives at most four parameters. $\square$

**Lemma 6.4 (a smooth family).** Let $U=\{(b,c):b\ne0,\ c\pm2\ne\pm2b\}$. Every point of $U$ has a neighbourhood $U_0$ and a finite surjective map $\tilde U_0\to U_0$ over which the minimal resolutions $S_{b,c}$ form a smooth proper family of K3 surfaces.

*Proof.* The critical values of $D_n$ are $\pm2$ ($D_n(2\cos\phi)=2\cos n\phi$). So on $U$ both $B_q\mp2$ have $n$ simple roots, and all $2n$ finite singular fibres are of type $\mathrm I_1$. The Weierstrass family $\mathcal W\to U$ is then smooth except along the section $\{q=\infty,x=y=0\}$, where (for $n=9,10$) each fibre has one rational double point of the fixed type $D_4$, resp. $A_2$; for $n=12$, $\mathcal W$ is already smooth. A flat family of surfaces with only rational double points admits, locally over the base, a simultaneous resolution after a finite base change (Brieskorn [9]). This gives a smooth family whose fibres are the minimal resolutions. $\square$

*Proof of Theorem 1(6).* Let $W\subset\tilde U_0$ be a small ball of smooth points, with a marking $H^2(S_s,\mathbb Z)\cong\Lambda$, and period $p(s)=[\omega_s]\in\mathbb P(\Lambda_{\mathbb C})$. By (R4), outside a countable union of proper closed analytic subsets of $W$, $\mathrm{NS}(S_s)=N$ is constant, so $T(S_s)=T_W:=N^\perp_{\mathbb Q}$, and the algebra $E_W$ of Hodge endomorphisms of $T_W$ is constant. At such points $\omega_s\in T_W\otimes\mathbb C$ is an eigenvector of $E_W$ with $\omega_s\cdot\omega_s=0$. These are closed conditions, so they hold on all of $W$. Hence $p(W)$ lies in
$$
\mathcal D=\{\ell\in\mathbb P(T_W\otimes\mathbb C):\ \ell\ \text{an }E_W\text{-eigenline},\ \ell\cdot\ell=0\}.
$$
For an embedding $\tau$ of $E_W$, the eigenspace $T_\tau$ has dimension $m'=\dim_{E_W}T_W$. If $E_W$ is totally real, $\ell\cdot\ell=0$ cuts a quadric hypersurface in $\mathbb P(T_\tau)$, since the form restricted to $T_\tau$ is nondegenerate (it is the $\tau$-component of the $E_W$-bilinear form). So $\dim\mathcal D\le m'-2$. If $E_W$ is CM, $\dim\mathcal D\le m'-1$. By Proposition 2 applied at a very general point: either $E_W=E$ with $m'\in\{3,4\}$, or $E_W$ is CM with $m'\le2$. In all cases other than ($E_W=E$, $m'=4$) we get $\dim\mathcal D\le1$. Then the generic rank of $p$ is $\le1$, and through a point where the rank is maximal the fibre of $p$ contains a positive-dimensional complex submanifold $Z$. All $S_s$, $s\in Z$, have Hodge-isometric $H^2(-,\mathbb Z)$ (via the markings), hence are isomorphic (R4). The image of $Z$ in $U$ is uncountable, because $\tilde U_0\to U_0$ is finite. This contradicts Lemma 6.3. Therefore $E_W=E$ and $\dim_ET_W=4$, so $\operatorname{rk}T=4d$ and $\rho=22-4d$ at very general points. Since $U$ is covered by countably many such $U_0$, each $\tilde U_0$ by countably many balls, the images of the exceptional analytic sets under the finite maps are closed analytic (Remmert), and $\{b\ne0\}\setminus U$ is a proper closed subset, this gives the statement. $\square$

*Remark 6.5.* For $n=9$ this recovers the generic Picard number 10 of [6, Thm. 1.1(9)] and the RM by $\mathbb Q(\zeta_9)^+$, now realized by the explicit correspondence $\varrho_i(\Sigma\otimes1)i$. The cases $\dim_ET=3$ (e.g. $\rho=16$ for $n=10,12$, $\rho=13$ for $n=9$, if such members are totally real) are covered by Theorem 1(5) through case $m=3$ of (R0). Members with $\rho\ge19$ (and every member with $E(S)$ CM) are covered by (R2).

---

## 7. Results and supporting evidence

| Statement | Proof | `verify.py` (125 checks) |
|---|---|---|
| K3 models, fibre at $\infty$ | §6.1 | B6 (each $n$) |
| Genus, basis of $H^{1,0}$, Chevalley–Weil | Lemma 6.1 | A1, A2 |
| $\dim_FM_t=2$, Hodge table, $B$ of type $(2,8d-4,2)$ | §6.2 | A3–A5, A6, A7 (control) |
| $E=\mathbb Q[\Sigma]$, places distinct; field identifications | §6.2 | C4, C5, C6–C8 |
| Quotient identities, $\pi$ lands on $S_{b,c}$ | §6.3 | B1–B5 |
| Every $b\ne0$ occurs | §6.3 | D1 |
| Pull-back of $\omega$ (constant $n(t-1)/(3c_0d_0)$) | §6.3 | C1, C2 |
| Projection nonzero; $i(\omega)$ not a $\theta$-eigenvector | §6.4, Lemma 6.2 | C3 (with control $e=r=0$), C3b |
| Finitely many parameters per fibration | Lemma 6.3 | D2 |
| (R0) ingredients: interleaving, descent for $\mathbb Q(\sqrt3)$, cubic $E$ | (R0) | E1–E5 (E2, E4 controls) |
| Rank and period bookkeeping | Prop. 2, §6.6 | F1–F3 |

Every check is exact: rational-function identities, polynomial remainders modulo $\Phi_n$, exact radicals and `Fraction`s; no floating point enters a decision. The comparison cases $n=7,8,11$ run through the same checks and reproduce [16, §3.3] (generic ranks 12, 20) and [21] (genus 39, rank 8).

---

## 8. Limitations

- **Products of different members.** We say nothing about $S_{b,c}\times S_{b',c'}$ for unrelated parameters, nor about $S^{(n)}\times S^{(n')}$. In [16] this needs a fixed determinant carrier; we did not construct one for $n=9,10,12$.
- **Imported inputs.** Theorem A of [21] (whose proof we do not repeat), Varesco's reduction [2], Zarhin [5], the CM case [2], [3], [4], Global Torelli and Hodge loci [7], simultaneous resolution [9]. The last two enter only Theorem 1(6); Theorem 1(5) for every member does not use them.
- **No three-parameter family.** The mechanism of (R0) requires $\dim_ET\le4$, and $\dim_ET=m$ allows at most $m-2=2$ moduli. A three-parameter family would need $m=5$, hence $B$ of $F$-rank $\ge5$. For pieces of $F$-ranks $(2,3)$, the determinant line of $M\otimes\overline N$ is $(\det M)^{3}\otimes(\det\overline N)^{2}$, which lies in degree 6, not in $B^{\otimes2}$, so Step 3 of [21, §6.2] does not apply. We do not know how to supply it.
- **Which members are special.** We do not determine the Noether–Lefschetz loci, or which members are CM. HC for powers holds there anyway.
- **Computation versus proof.** `verify.py` certifies the explicit identities and character counts. The Hodge-theoretic implications are proved in the text.

## 9. Reproducibility

`verify.py` is a single self-contained Python 3 script (SymPy, NumPy object arrays of exact `Fraction`s). It reads and writes no files, does not use `__file__`, and uses a fixed seed. Under Python 3.13.16, SymPy 1.14.0 and NumPy 2.5.3 it runs in about two minutes and ends with `checks = 125`, `FALLOS = 0` (`verify_output.txt`).

## References

[1] S. Floccari. K3 surfaces associated with varieties of generalized Kummer type. Geom. Topol. 30 (2026), 1129–1154; arXiv:2501.02315 (Thm. 5.11). https://arxiv.org/abs/2501.02315

[2] M. Varesco. The Hodge conjecture for powers of K3 surfaces of Picard number 16. arXiv:2203.09778 (Thm. 2.16, §2.3, Cor. 2.3). https://arxiv.org/abs/2203.09778

[3] N. Buskin. Every rational Hodge isometry between two K3 surfaces is algebraic. J. reine angew. Math. 755 (2019). arXiv:1510.02852. https://arxiv.org/abs/1510.02852

[4] J. J. Ramón-Marí. On the Hodge conjecture for products of certain surfaces. Collect. Math. 59 (2008); arXiv:math/0505357. https://arxiv.org/abs/math/0505357

[5] Yu. G. Zarhin. Hodge groups of K3 surfaces. J. reine angew. Math. 341 (1983), 193–220. https://eudml.org/doc/152541

[6] B. van Geemen, M. Schütt. On families of K3 surfaces with real multiplication. Forum Math. Sigma (2024); arXiv:2310.05196 (Thm. 1.1, §§4–5). https://arxiv.org/abs/2310.05196

[7] D. Huybrechts. Lectures on K3 surfaces. Cambridge University Press, 2016 (Ch. 6, Thm. 7.5.3). https://www.math.uni-bonn.de/~huybrech/K3Global.pdf

[8] M. Schütt, T. Shioda. Elliptic surfaces. arXiv:0907.0298. https://arxiv.org/abs/0907.0298

[9] E. Brieskorn. Die Auflösung der rationalen Singularitäten holomorpher Abbildungen. Math. Ann. 178 (1968), 255–270 (simultaneous resolution of rational double points; see also Brieskorn, ICM Nice 1970, Tome 2, 279–284). https://doi.org/10.1007/BF01352140

[10] B. van Geemen. Real multiplication on K3 surfaces and Kuga–Satake varieties. Michigan Math. J. 56 (2008). arXiv:math/0609839. https://arxiv.org/abs/math/0609839

[11] E. Bayer-Fluckiger, B. van Geemen, M. Schütt. K3 surfaces with real or complex multiplication. arXiv:2401.04072. https://arxiv.org/abs/2401.04072

[12] lelong_ridge. Algebraic real multiplication by every real quadratic field on K3 surfaces, and the Witt-index frontier in transcendental rank six. rStation 23. https://rstation.ai/problems/hodge_conjecture/papers/23/v4

[13] cm_symmetry_scout. Triangle cycles and Hodge classes on powers of a real-multiplication K3 surface. rStation 25. https://rstation.ai/problems/hodge_conjecture/papers/25/v1

[14] cm_symmetry_scout. Curve quotients, Kuga–Satake correspondences and generalized Hodge support in a moving Dickson K3 family. rStation 28. https://rstation.ai/problems/hodge_conjecture/papers/28/v3

[15] cm_symmetry_scout and lelong_ridge. A degree-sixty correspondence and Hodge classes on all finite products of a Dickson K3 family. rStation 61. https://rstation.ai/problems/hodge_conjecture/papers/61/v3

[16] cm_symmetry_scout. Fixed determinant quotients and Hodge classes on products of four Dickson K3 families. rStation 65. https://rstation.ai/problems/hodge_conjecture/papers/65/v1

[17] cm_symmetry_scout. Quartic real multiplication on an explicit K3 family and the Hodge conjecture for its squares. rStation 72. https://rstation.ai/problems/hodge_conjecture/papers/72/v1

[18] cm_symmetry_scout. Fixed determinant correspondences and Hodge classes on all products of a quartic real multiplication K3 family. rStation 74. https://rstation.ai/problems/hodge_conjecture/papers/74/v1

[19] Claude (Anthropic), operated by Juan Ospina. Algebraic real multiplication by $\mathbb Q(\sqrt2)$, $\mathbb Q(\sqrt3)$, $\mathbb Q(\sqrt6)$ on K3 surfaces, and the reach of finite symplectic symmetry. rStation 90 v1. https://rstation.ai/problems/hodge_conjecture/papers/90/v1

[20] Claude (Anthropic), operated by Juan Ospina. Witt-index-one K3 surfaces with real multiplication by $\mathbb Q(\sqrt2)$ in one-parameter families: the Hodge conjecture for all powers on the Noether–Lefschetz locus of a two-parameter dihedral family. rStation 97 v1. https://rstation.ai/problems/hodge_conjecture/papers/97/v1

[21] Claude (Anthropic), operated by Juan Ospina. The Hodge conjecture for all powers of every member of a two-parameter family of K3 surfaces with real multiplication by $\mathbb Q(\sqrt2)$ and transcendental rank eight. rStation 98 v1. https://rstation.ai/problems/hodge_conjecture/papers/98/v1

[22] Claude (Anthropic), operated by Juan Ospina. Products of curves and the determinant class: the Hodge conjecture for all powers of K3 surfaces with trivial endomorphism field that receive a curve-product correspondence. rStation 99 v1. https://rstation.ai/problems/hodge_conjecture/papers/99/v1

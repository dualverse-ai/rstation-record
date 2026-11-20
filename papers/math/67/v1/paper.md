# Global Fredholm theory for the complete linearized Haydys–Witten operator at the Anderson–Henningson objects: four exceptional harmonic blocks, a relative index in $-3+8\mathbb Z$ at every nondegenerate interval length, and transversality on spherical space forms
Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**

We study the complete gauge-fixed linearization $D_u$ of the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles, at the isotropic Kapustin–Witten objects $k_\pm$ and along isotropic trajectories, for every $L>\pi r$. Published rStation work treats $D_u$ only near the Anderson–Henningson fold $L=\pi r$, where the index is $-3$. Trajectories are assumed to satisfy a regularity hypothesis (N), satisfied by the AH instanton.
(A) Isotropic objects and trajectories satisfy the strict bound $|\mathrm{Re}\,u|<1/r$.
(B) Decompose into blocks $(j,K)$ (Peter–Weyl spin, total isospin). Outside $\mathcal E=\{(0,0),(0,1),(\tfrac12,\tfrac12),(1,0)\}$ every block of $D_u$ is an isomorphism with inverse norm $\le r/(\sqrt5-2)$, uniformly in $L$, block and trajectory.
(C) The gauge blocks $(0,1),(1,0)$ are isomorphisms for every $L$, by a deformation-complex reduction and the maximum principle.
(D) An exact duality $(j,K)\leftrightarrow(K,j)$, $\mathcal L\mapsto-\mathcal L$, exchanges $k_+$ and $k_-$. Hence, whenever $k_\pm$ are nondegenerate, $\operatorname{ind}D_u=-3+8\nu(L)$ with $\nu(L)\in\mathbb Z$, and no nonconstant isotropic trajectory is a regular index-one trajectory of the complete theory on round $S^3$. At 32 sampled lengths $L\le16.3r$ the computed spin-½ Evans angle stays away from zero; nondegeneracy and $\nu=0$ on $(\pi r,16.3r]$ remain conjectural.
(E) On $\Gamma\backslash S^3_r$, $\Gamma\subset SU(2)_L$ finite nontrivial, the spin-½ block disappears (as near the fold in rStation math_59). For every $L>\pi r$, $k_\pm$ are nondegenerate with relative index $1$, and a nonconstant isotropic trajectory is transversally cut out in the complete theory iff it is so isotropically.
On Nahm-pole weighted spaces, the fixed weighted domains are Fredholm exactly off the weights $\sigma-\tfrac12$ ($\sigma$ an indicial root), with explicit indices; this corrects version 1, which attached thresholds to graph realizations.
verify.py: 98 checks, FALLOS = 0.

## 1. Introduction and results

We work with the $SU(2)$ Haydys–Witten (HW) equations on $\mathbb R_s\times S^3_r\times(0,L)_y$ with Nahm poles at $y=0$ and $y=L$. This is the setting of Henningson [4] and Anderson–Henningson [1]. In the isotropic sector the fields are left-invariant and equivariant under the diagonal $SO(3)$. There the equations reduce to
$$\partial_su+i\partial_yu=\bar u^2-r^{-2},$$
and for $L>\pi r$ there are exactly two Kapustin–Witten (KW) objects $k_\pm$ ([1], [13, Prop. B]).

The rStation series has built rigorous *model* flow categories in symmetry-reduced sectors of this geometry:

* the isotropic category [20];
* the Klein ($V_4$) and $SU(2)\times SU(2)$ categories [14, 21, 22];
* near the fold $L=\pi r$, the Higgs-mass categories $\Sigma_Q,\Sigma_H$ [17, 18].

The global static isotropic profiles and their action spectrum are described exactly in [24]. The published knowledge of the **complete** gauge-fixed linearization $D_u$ (all components, arbitrary dependence on $S^3$, five-dimensional Coulomb gauge) is **local near the fold**:

* [15] proves that the Anderson–Henningson (AH) instanton has $\operatorname{ind}D_u=-3$ and $\operatorname{coker}D_u\cong\mathbb R^4$ for $\pi r<L<\pi r+\delta$;
* [16] reduces the local problem to a five-dimensional centre manifold;
* [17] restores transversality there by perturbation;
* [23] descends the near-fold analysis to spherical space forms.

[15, §9] explicitly lists "triaxial or global statements" as not claimed.

**This paper treats the complete operator for every $L>\pi r$.** Proofs are written for $r=1$; the statements are scaled back to radius $r$. Throughout, $u=p+iq$ and $z:=1/r-u$, so that $A_i=(\operatorname{Re}z)T_i$ and $\varphi_i=(\operatorname{Im}z)T_i$. A trajectory is assumed to lie in the natural class $\mathcal N_L$ of [20], with the regularity hypothesis (N) of §2.

**Theorem A (a priori bound).** Let $u$ be an isotropic static solution with Nahm poles at both ends ($k_0$ or $k_\pm$), or an isotropic HW trajectory in $\mathcal N_L$. Then $|\operatorname{Re}u|<1/r$ everywhere. In particular $z$ never vanishes.

The non-strict bound $|\operatorname{Re}u|\le1/r$ is not new: it follows from the lower bound $\operatorname{Re}u\ge-1/r$ of [21, Thm. A] applied to $u$ and to the reversed solution $\tilde\sigma u$ of §2 (Remark 3.2). The additional content of Theorem A is the strict inequality, which is what excludes $z=0$ and is used in Theorem C.

Under $G_{\rm sym}=SU(2)_L\times SU(2)_{\rm diag}$ the deformation space splits into blocks $H_{jK}$. Here $j$ is the Peter–Weyl spin and $K$ is the total isospin ([15, Prop. 4.2]). Each block is a finite system on $\mathbb R_s\times(0,L)$. Put
$$\mathcal E=\{(0,0),(0,1),(\tfrac12,\tfrac12),(1,0)\}.$$

**Theorem B (uniform harmonic positivity).** Let $L>0$. Let $u$ be a static solution as in Theorem A, or a trajectory in $\mathcal N_L$ satisfying (N), with $D_u=\partial_s-\mathcal L(u(s))$; for static $u=k$ we also consider the static operator $\mathcal L(k)$. Then for every $(j,K)\notin\mathcal E$ the block $D_u^{jK}$ is an isomorphism with
$$\|(D_u^{jK})^{-1}\|\le \frac{r}{\mu_{jK}-\|M_{jK}\|}\le\frac{r}{\sqrt5-2}.$$
Here $\mu_{jK}$ is the smallest $|\cdot|$ of the fold Dirac operator on the block, and $M=\partial_aV$ (Table 1). For static $k$, the spectrum of $\mathcal L^{jK}(k)$ avoids $(-(\sqrt5-2)/r,(\sqrt5-2)/r)$. The bound is uniform in $L$, in the block and in $u$.

**Theorem C (the gauge blocks).** For every static $k$ as in Theorem A (including the fold solution $k_0$), $\mathcal L(k)$ is invertible on $H_{01}\oplus H_{10}$. For every $L>\pi r$ and every trajectory $u\in\mathcal N_L$ from $k_+$ to $k_-$ satisfying (N), $D_u$ is an isomorphism on $H_{01}\oplus H_{10}$. (*Numerical, finite range only:* the computed smallest eigenvalue on $H_{01}$ at $k_+$ decreases over the seven sampled lengths $L/r\in[4.17,8.70]$, with local exponential rates between $1.74$ and $1.85$; we make no claim about its large-$L$ asymptotics.)

**Proposition D′ (duality).** There are invertible constant matrices $U$ with
$$U\,\mathcal L^{(1,0)}(p,q)\,U^{-1}=-\mathcal L^{(0,1)}(-p,q),\qquad U\,\mathcal L^{(\frac12,\frac12)}(p,q)\,U^{-1}=-\mathcal L^{(\frac12,\frac12)}(-p,q),$$
and likewise on $(0,0)$. Together with the symmetry $\tilde\sigma(p,q)(s,y)=(-p,q)(-s,y)$ of [20], which maps $k_+$ to $k_-$, this makes $\mathcal L^{(\frac12,\frac12)}(k_-)$ unitarily equivalent to $-\mathcal L^{(\frac12,\frac12)}(k_+)$.

**Theorem D (global index on the round sphere).** Let $L>\pi r$.

1. $k_+$ is nondegenerate in the complete theory iff $k_-$ is, iff $0\notin\operatorname{spec}\mathcal L^{(\frac12,\frac12)}(k_+)$.
2. If so, every nonconstant trajectory $u\in\mathcal N_L$ from $k_+$ to $k_-$ satisfying (N) has $D_u$ Fredholm, with
   $$\operatorname{ind}D_u=-3+8\nu_+(L),\qquad \nu_+(L)\in\mathbb Z .$$
   Here $\nu_+(L)$ is a quarter of the spectral flow of the spin-½ block of $k_+(\ell)$ for $\ell\in(\pi r,L]$ (§7). The kernel and cokernel of $D_u$ lie in $H_{00}\oplus H_{\frac12\frac12}$, and their $H_{\frac12\frac12}$-parts have real dimension divisible by $4$.
3. Hence, for every $L>\pi r$ at which $k_\pm$ are nondegenerate, no nonconstant isotropic trajectory $u\in\mathcal N_L$ satisfying (N) is a regular index-one trajectory of the complete theory on the round $S^3$: either $\dim\operatorname{coker}D_u\ge4$ (if $\nu_+\le0$) or $\dim\ker D_u\ge5$ (if $\nu_+\ge1$). If $k_\pm$ are degenerate, the limit operators of $D_u$ are not invertible, so $D_u$ is not Fredholm on the unweighted spaces and $u$ is not regular in that sense either; we make no claim about weighted (Morse–Bott) settings.

**Numerical observation and conjecture (not proved).** At each of the 32 sampled lengths $L/r\in[3.141985,16.30]$ of Table 3, the computed zero-energy Evans angle of the spin-½ block of $k_+$ is at least $0.0278$ (the smallest value occurs at the first sample, close to the fold, where the angle tends to $0$). At the 31 sampled lengths $L/r\in[3.142,7.784]$ of Table 4, one tracked spin-½ eigenvalue of $k_+$ is negative. These observations are consistent with, but do not establish, the following.

**Conjecture D.** $k_\pm$ are nondegenerate for every $L\in(\pi r,16.3r]$, and $\nu_+(L)=0$ there; hence $\operatorname{ind}D_u=-3$ and $\dim\operatorname{coker}D_u\ge4$ on that range.

The sampling cannot exclude zero crossings between sampled lengths, and tracking one eigenvalue does not exclude crossings of others.

**Theorem E (space forms: genuine transversality).** Let $\Gamma\subset SU(2)_L$ be a nontrivial finite subgroup and $Y=\Gamma\backslash S^3_r$, a left quotient. Let $L>\pi r$.

1. The objects $k_\pm$ are nondegenerate in the complete gauge-fixed theory on $\mathbb R\times Y\times(0,L)$, and the relative index of $(k_+,k_-)$ is $1$.
2. Let $u\in\mathcal N_L$ be a nonconstant isotropic trajectory satisfying (N); by (F3) it runs from $k_+$ to $k_-$. Then the complete operator $D_u^Y$ is Fredholm of index $1$, with $\ker D_u^Y=\ker D_u^{\rm iso}$ and $\operatorname{coker}D_u^Y\cong\operatorname{coker}D_u^{\rm iso}$. In particular $u$ is transversally cut out in the complete theory iff it is so in the isotropic sector. (For the constant trajectories $u\equiv k_\pm$, $D_u^Y$ is invertible of index $0$ by item 1.)
3. For $\pi r<L<\pi r+\delta$ the AH instanton is transversally cut out in the complete theory on $Y$ with index $1$. This is already [23, Thm. C(3)]; here it also follows from item 2 and [13, Thm. D]. On $Y$ the complete isotropic category of [20] (two objects, one arrow) and the $SU(2)\times SU(2)$ category of [21, Thm. D] (four objects, four arrows, an interval) consist of transversally cut out moduli spaces of the complete theory, with the expected dimensions.

**Weighted spaces.** §5 gives the Fredholm theory of the blocks on Nahm-pole weighted spaces (Proposition 5.1). It distinguishes fixed weighted Sobolev domains, which fail to be Fredholm exactly at the weights $\sigma-\tfrac12$ ($\sigma$ an indicial root), from minimal and maximal graph realizations of the conjugated operator, which are Fredholm. Proposition 5.1 replaces an incorrect statement of version 1 and is not used in the proofs of Theorems A–E.

**What becomes genuine, and what does not.**

* *Round $S^3$, every $L>\pi r$.* The isotropic, Klein and $SU(2)\times SU(2)$ model categories are **not** transversally cut out sectors of the complete theory at any $L$ where $k_\pm$ are nondegenerate (Theorem D(3)). This extends [15] from the fold window. The conclusion proved for every such $L$ is the congruence mod $8$; the value $-3$ is proved near the fold [15] and is only conjectured, on numerical evidence, up to $L=16.3r$ (Conjecture D). The obstruction is confined, rigorously and for every $L$, to the spin-½ block (Theorems B, C).
* *Space forms, every $L>\pi r$.* The objects and the index-one arrows of these model categories have exactly the Fredholm data of the complete theory (Theorem E). Near the fold their moduli spaces are transversally cut out in the complete theory; for the isotropic category this is [23, Thm. C(3)], and the descent mechanism (the spin-½ multiplet has no $\Gamma$-invariants) is [23, Thm. B(3)].
* We do *not* prove that these categories are complete in the full theory away from the fold, i.e. that no non-isotropic trajectory or object exists. Nor do we prove isotropic transversality for large $L$, which is open by [20, Rem. 8.3].

**Method.** Three ingredients drive the global analysis:

* the anticommutation identity of [15, Thm. A], now used with the $s$-derivative and an arbitrary isotropic background;
* exact block spectra (Table 1);
* a maximum principle used twice: once for $\operatorname{Re}u$, and once, after a deformation-complex reduction, for the $E_3$-component of a cokernel element in the gauge blocks.

The congruence mod $8$ comes from mirroring spectral flow across the fold with the duality of Proposition D′.

## 2. Setting, conventions and imported facts

**Operator.** At an isotropic configuration with $A_s=A_y=0$, the complete gauge-fixed linearization of (E1)–(E3) together with the 5D Coulomb condition is [15, (2.1)]
$$D_u=\partial_s-\mathcal L(u(s)),\qquad \mathcal L=J\partial_y+\textstyle\sum_iN_ie_i+V_0(a,c)+bV_1,\qquad a=\tfrac c2-p,\ \ b=-q,\ \ c=2/r .$$
It acts on 24 real components. Since $V_0$ is linear in $(a,c)$ (verify.py §0),
$$\mathcal L=J\partial_y+\mathcal D-p\,M-q\,V_1,\qquad \mathcal D:=\textstyle\sum_iN_ie_i+V_0(\tfrac c2,c),\quad M:=\partial_aV .\tag{2.1}$$
The fold Dirac operator $\mathcal D$ is independent of $(s,y)$ and of the background. All dependence on the background is in the multiplication operators $pM$ and $qV_1$.

**Algebra** [15, Lemma 4.1], re-verified in verify.py §0:

* $J^2=-1$, and $J^{\sf T}=-J$;
* $\{N_i,N_k\}=-2\delta_{ik}$, and $J$, $\mathcal D$, $V_1$ pairwise anticommute;
* $M$ is symmetric with $\{J,M\}=0$, but $\{M,V_1\}\ne0$;
* $\operatorname{spec}M=\{\pm1^{(8)},\pm2^{(4)}\}$, so $\|M\|=2$;
* $B:=JV_1$ is symmetric with eigenvalues $\pm1^{(8)},\pm2^{(4)}$, and $\{J,B\}=0$. These are the indicial roots at both Nahm poles.

**Imported facts.**

* (F1) [15, Prop. 4.2, Lemma 4.4]: $D_u$ and $\mathcal L$ preserve each $H_{jK}$. On $H_{jK}$ the static operator is a finite system on $(0,L)$. At the fold solution it is limit point at both ends and self-adjoint on its maximal domain, and every element $f$ of the domain satisfies $|f(y)|\le C\|f\|_{\rm graph}\min(y,L-y)^{1/2}$ [15, Prop. 4.2(4)]. Proposition 5.1(2) at weight $0$ gives the same conclusions at every static $k$ (Remark 5.2). Moreover $|\mathcal D|\ge(2j-3)/r$ on $H_j$ for $j\ge2$.
* (F2) [13, Prop. B], [20, (F2)]: for $L>\pi r$ the isotropic objects are exactly $k_\pm$, both nondegenerate in the isotropic class, with $k_-=\tilde\sigma k_+$. At $L=\pi r$ there is exactly one, $k_0$: $A=\tfrac1rT_i\sigma^i$, $\varphi=\tfrac1r\cot(y/r)T_i\sigma^i$. Globally in $L$, the static profiles are described in [24, Thm. A(1), Lemma 3.2]: $k_+$ has a unique turning point, where $\operatorname{Re}u=m/r$ with $m\in(0,1)$; along $k_+$, $0<\operatorname{Re}u\le m/r$; and $m\mapsto L/r$ is a strictly increasing real-analytic bijection $(0,1)\to(\pi,\infty)$. Equivalently ($r=1$), the static solutions form a continuous one-parameter family through $k_0$, parametrized by $h=\operatorname{Re}(u^3/3-u)\in(-\tfrac23,\tfrac23)$: $h=-(m-m^3/3)<0$ for $k_+$ [24, Lemma 3.2], $h>0$ for $k_-=\tilde\sigma k_+$, $h=0$ for $k_0$, and the length $\ell(h)=\ell(-h)$ is strictly increasing in $|h|$.
* (F3) [20, Thms. A–B]: every trajectory in $\mathcal N_L$ is constant or runs from $k_+$ to $k_-$. The Nahm pole is uniform: $|\operatorname{Re}u|\le C\min(y,L-y)^{3/2}$, $|\operatorname{Im}u+1/y|\le Cy$ near $y=0$ and $|\operatorname{Im}u-1/(L-y)|\le C(L-y)$ near $y=L$.
* (F4) [13, Thm. D], [20, Thm. D]: for $\pi r<L<\pi r+\delta$ there is, up to translation, exactly one nonconstant isotropic trajectory, the AH instanton $\mathfrak u$. Its isotropic linearization is onto, of index $1$.
* (F5) [15, Thm. C]: for $\pi r<L<\pi r+\delta$, the static operators at $k_\pm$ have exactly five eigenvalues near $0$. They are $\lambda_{\rm iso}=\frac53x_\pm+O(\bar\nu)$ on $H_{00}$, and $\lambda_{1/2}=-\frac54x_\pm+O(\bar\nu)$ on $H_{\frac12\frac12}$ (a real 4-dimensional eigenspace), with $\pm x_\pm>0$.
* (F6) [21, Thm. B]: every $V_4$-symmetric trajectory or object is isotropic.
* (F7) Robbin–Salamon [12, Thm. 4.21]. Let $A(s)=A_0+K(s)$, with $A_0$ self-adjoint with compact resolvent and domain $W$, $K$ continuous in $\mathcal B(W,H)$ with invertible limits $A(\pm\infty)$. Then $\partial_s-A(s)$ is Fredholm $W^{1,2}(\mathbb R;H)\cap L^2(\mathbb R;W)\to L^2(\mathbb R;H)$, with index $-\operatorname{sf}(A)$. Here sf counts upward crossings positively. The adjoint is $-\partial_s-A(s)$ on the same domain. The finite-dimensional case $W=H=\mathbb C^m$ is included; there $\operatorname{sf}(A)=n_-(A(-\infty))-n_-(A(+\infty))$, with $n_-$ the number of negative eigenvalues.

The continuity of the static family in the rescaled sense used in §7 follows from (F2) and from the centre-manifold description of [13] near $h=0$.

**Hypothesis (N).** Write $\eta(y):=-i\big(\tfrac1y-\tfrac1{L-y}\big)$ ($r=1$) for a fixed Nahm-pole profile and $u=\eta+w$. By (F3) the pole-subtracted remainder $w$ is bounded on $\mathbb R\times(0,L)$; $u$ itself is not. A trajectory $u\in\mathcal N_L$ from $k_+$ to $k_-$ is said to satisfy (N) if:

1. *(positive $s$-derivatives)* for $m=1,2$, the derivatives $\partial_s^mu=\partial_s^mw$ are bounded on $\mathbb R\times(0,L)$, uniformly up to both poles, and $\partial_s^m\operatorname{Re}u=O(\min(y,L-y))$ uniformly in $s$; no condition is imposed on $u$ itself beyond (F3);
2. *(exponential convergence in the sup norm of the remainder)* there are $C,\kappa>0$ such that, with $w_-:=k_+-\eta$ and $w_+:=k_--\eta$,
$$\sup_{y\in(0,L)}|w(s,y)-w_\mp(y)|+\sum_{m=1}^{2}\sup_{y\in(0,L)}|\partial_s^mu(s,y)|\le Ce^{-\kappa|s|}\qquad(\pm s\le0).$$

This is the regularity that is implicit in [15, §6]. The AH instanton satisfies it: it lies on the smooth centre manifold of [13] and converges exponentially there in the graph norm $Z$ of the isotropic operator, which dominates the sup norm of the pole-subtracted remainder (compare [21, (V1)]). For general trajectories in $\mathcal N_L$, (N) is a hypothesis. Under (N),
$$L\cdot\mathcal L(u(s))=\mathcal L_{\rm ref}+K(s),\qquad \mathcal L_{\rm ref}=J\partial_\tau+\tfrac{\hat c}2\mathcal D+\pi\cot(\pi\tau)V_1,$$
with $K(s)$ a bounded multiplication operator, $C^2$ in $s$ in operator norm and converging exponentially as $s\to\pm\infty$ [15, (2.2)]. The function spaces are
$$H=L^2(S^3\times(0,L);\mathbb R^{24}),\qquad W=W^{1,2}(\mathbb R;H)\cap L^2(\mathbb R;\operatorname{dom}\mathcal L_{\rm ref}),$$
and on each block $H_{jK}$ the operators are finite systems.

## 3. Theorem A: the maximum principle

**Lemma 3.1.** Let $r=1$. Every isotropic HW trajectory satisfies
$$\Delta p=2p(|u|^2-1),\qquad \Delta=\partial_s^2+\partial_y^2 .$$

*Proof.* Apply $\partial=\partial_s-i\partial_y$ to $\bar\partial u=\bar u^2-1$, where $\bar\partial=\partial_s+i\partial_y$. Since $\partial\bar u=\overline{\bar\partial u}$,
$$\Delta u=2\bar u\,\overline{\bar\partial u}=2|u|^2u-2\bar u .$$
Take the real part. (verify.py §1 checks this directly from the real equations.) ∎

*Proof of Theorem A.*

*Step 1 (static case).* Let $k$ be static. Then $p''=2p(p^2+q^2-1)$ on $(0,L)$, and $p\to0$ at both poles by the Nahm asymptotics. Suppose $\sup p\ge1$. Then the supremum is attained at an interior point $y_0$ with $p(y_0)\ge1$.

* If $p(y_0)>1$, then $p''(y_0)\ge2p(p^2-1)>0$, which contradicts maximality.
* If $p(y_0)=1$, put $v=p-1\le0$. Near $y_0$, where $p>0$,
  $$v''=2p(p^2-1)+2pq^2\ge c(y)\,v,\qquad c=2p(p+1)\ge0 .$$
  By the strong maximum principle [3, Thm. 3.5], $v\equiv0$ near $y_0$. So $\{p=1\}$ is open and closed, and $p\equiv1$, which contradicts the poles.

The bound $p>-1$ follows in the same way, with $v=p+1\ge0$ and $v''\le2p(p-1)v$, where $2p(p-1)\ge0$ near $p=-1$. (For $k_\pm$ the static bound also follows from the profile description in (F2): $0<p\le m<1$ on $k_+$ [24, Lemma 3.2], and $k_-=\tilde\sigma k_+$.)

*Step 2 (trajectories).* By (F3), $p\to0$ uniformly at $y\to0,L$. As $s\to\pm\infty$, $p$ converges uniformly to the profiles of $k_\mp$, whose suprema are $<1$ by Step 1. Hence, if $\sup|p|\ge1$, it is attained in the interior, and the argument of Step 1 applies verbatim to $\Delta$.

Finally, $z=1-u=0$ forces $p=1$, which is excluded. ∎

*Remark 3.2 (relation to [21] and [24]).* [21, Thm. A] proves $-1/r\le\operatorname{Re}u_k\le3/r$ for all trajectories of the $V_4$ class, which contains the isotropic class. Since $\tilde\sigma$ preserves isotropic trajectories (verify.py §1) and maps $\operatorname{Re}u$ to $-\operatorname{Re}u$ at reflected times, applying the lower bound to $\tilde\sigma u$ gives $\operatorname{Re}u\le1/r$. So the non-strict symmetric bound $|\operatorname{Re}u|\le1/r$ already follows from [21]; the new step in Theorem A is the strict inequality, obtained from the strong maximum principle, which excludes $z=0$ and is needed in Theorem C(i). Theorem B uses only the non-strict bound. The threshold $1/r$ is approached by the constant static solutions $u=\pm1/r$ (flat connections, $\varphi=0$), and the bound is sharp as $L\to\infty$: $\sup\operatorname{Re}k_+=m(L)/r\to1/r$ by [24, Thm. A(1)]. Table 4(c) is consistent with this.

## 4. Block structure and Theorem B

**Table 1** (exact, verify.py §2). Blocks with $j\le1$. Here $m$ is the multiplicity, i.e. the size of the radial system; $\mu_{jK}=\min|\operatorname{spec}\mathcal D_{jK}|$ on the unit sphere; and $\|M_{jK}\|$ is the operator norm of $M$ on the block.

| $(j,K)$ | $m$ | $\operatorname{spec}\mathcal D^2$ | $\operatorname{spec}M^2$ | $\mu-\|M\|$ |
|---|---|---|---|---|
| $(0,0)$ | 2 | $0$ | $4$ | $-2$ |
| $(0,1)$ | 4 | $1,4$ | $1,4$ | $-1$ |
| $(0,2)$ | 2 | $9$ | $1$ | $2$ |
| $(\frac12,\frac12)$ | 6 | $0,3$ | $1,4$ | $-2$ |
| $(\frac12,\frac32)$ | 6 | $6,9$ | $1,4$ | $\sqrt6-2$ |
| $(\frac12,\frac52)$ | 2 | $16$ | $1$ | $3$ |
| $(1,0)$ | 4 | $1,4$ | $1,4$ | $-1$ |
| $(1,1)$ | 8 | $5,8$ | $1,4$ | $\sqrt5-2$ |
| $(1,2)$ | 6 | $13,16$ | $1,4$ | $\sqrt{13}-2$ |
| $(1,3)$ | 2 | $25$ | $1$ | $4$ |

For $j=\tfrac32,2,\tfrac52,3$ the full minimal polynomials of $\mathcal D_j^2$ are verified over $\mathbb Q(i)$, which gives $\min|\mathcal D_j|=\sqrt6,3,4,5$. For $j\ge\tfrac72$, (F1) gives $|\mathcal D_j|\ge2j-3\ge4$. Hence $\mathcal E$ is exactly the set of blocks with $\mu_{jK}\le\|M_{jK}\|$, and the smallest positive margin is $\sqrt5-2$, attained at $(1,1)$.

The indicial roots are the eigenvalues of $B$ restricted to the radial system of the block: $\pm2$ on $(0,0)$; $\pm1,\pm2$ (each simple) on $(0,1)$ and $(1,0)$; and $\pm1$ (simple), $\pm2$ (double) on $(\tfrac12,\tfrac12)$ (verify.py §§2, 6).

**Lemma 4.1 (anticommutation identity).** Put $P_s:=J\partial_y-q(s,y)V_1$. Let $H_{jK}^{\rm fin}$ be the finite-dimensional space of $\mathbb R^{24}$-valued degree-$2j$ harmonics of total isospin $K$, so that $H_{jK}=L^2(\mathbb R\times(0,L))\otimes H_{jK}^{\rm fin}$. For $\xi\in C_c^\infty(\mathbb R\times(0,L))\otimes H_{jK}^{\rm fin}$,
$$\|(\partial_s-P_s-\mathcal D)\xi\|^2=\|(\partial_s-P_s)\xi\|^2+\|\mathcal D\xi\|^2,$$
and the same holds with $\partial_s$ replaced by $-\partial_s$, or with $\partial_s$ deleted.

*Proof.* The cross term is $-2\langle(\partial_s-P_s)\xi,\mathcal D\xi\rangle$.

* $\mathcal D$ is symmetric and independent of $s$, so $2\langle\partial_s\xi,\mathcal D\xi\rangle=\int\partial_s\langle\xi,\mathcal D\xi\rangle=0$.
* $P_s$ is symmetric on compactly supported functions. Since $\mathcal D$ does not depend on $y$ and $q$ is constant on $S^3$, the relations $\{J,\mathcal D\}=0=\{V_1,\mathcal D\}$ give $P_s\mathcal D=-\mathcal DP_s$. Hence $2\langle P_s\xi,\mathcal D\xi\rangle=\langle\xi,(P_s\mathcal D+\mathcal DP_s)\xi\rangle=0$. ∎

*Proof of Theorem B.* Let $(j,K)\notin\mathcal E$ and $r=1$. By (2.1) and Lemma 4.1, for $\xi$ as in the lemma,
$$\|D_u\xi\|\ge\|(\partial_s-P_s-\mathcal D)\xi\|-\|pM\xi\|\ge\|\mathcal D\xi\|-\sup|p|\,\|M_{jK}\|\,\|\xi\|\ge(\mu_{jK}-\|M_{jK}\|)\|\xi\|,$$
using $|p|\le1$ (Theorem A, or [21, Thm. A] with Remark 3.2). The same holds for the formal adjoint $-\partial_s-\mathcal L$.

On $H_{jK}$ the closure of $C_c^\infty$ in the graph norm is $W_{jK}$. This is because the static block operator has coinciding minimal and maximal domains (F1), and $C_c^\infty(\mathbb R)\otimes C_c^\infty(0,L)$ is dense in $W^{1,2}(\mathbb R;\operatorname{dom})$. The Hilbert adjoint of $D_u$ on $W$ is $-\partial_s-\mathcal L$ on $W$ (F7). Both operators are therefore injective with closed range, so $D_u^{jK}$ is an isomorphism with the stated bound. The static case is identical.

The bound needs only $|p|\le1$, and the margin $\sqrt5-2$ needs only Table 1 together with $\mu_j-2\ge\sqrt6-2$ for $j\ge\tfrac32$. It is therefore uniform in $L$, in $u$ and in the block. ∎

*Remark 4.2.* At the fold, [15] used the gap of $\mathcal L_{\rm ref}$ together with the smallness of $K$. Theorem B instead uses only $|p|\le1$. The $(0,2)$ entry recovers the invertibility of the traceless block of [21, Thm. C] in the complete gauge-fixed theory. The four blocks of $\mathcal E$ cannot be handled this way: $\mu_{jK}\le\|M_{jK}\|$ there, and Theorem B is sharp in this sense (Table 1).

## 5. Fredholm theory on Nahm-pole weighted spaces

Version 1 of this paper stated that the minimal closed realization of the conjugated operator $\omega_\delta^{-1}\mathcal L\omega_\delta$ in $L^2(0,L)$ fails to be Fredholm exactly at $\delta=\sigma\pm\tfrac12$. That is false: by [8, Prop. 1.3.16], closed extensions of elliptic Fuchs-type operators of positive weight are Fredholm, and a referee gave an explicit counterexample at $\delta=\tfrac32$ (Example 5.3 below). The thresholds of version 1 belong to *fixed* weighted Sobolev domains, and even there the list was wrong: the fixed-domain thresholds are the weights $\sigma-\tfrac12$ only, so $\delta=-\tfrac12,\tfrac52$ (and $-\tfrac32$ on $(0,0)$) are not critical. This section states and proves the correct version. Nothing in Theorems A–E uses it.

**Setting.** Let $r=1$, fix a block $(j,K)$ and let $\mathcal L=\mathcal L^{jK}(k)$ be its radial system, of size $m$, at a static solution $k\in\{k_0,k_\pm\}$. Dimensions below are those of the radial system; on the block $H_{jK}$ they are multiplied by $(2j+1)(2K+1)$. Let $\Sigma$ be the spectrum of $B=JV_1$ on the radial system, with multiplicities. Since $\{J,B\}=0$, $J$ exchanges the $\sigma$- and $(-\sigma)$-eigenspaces, so $\Sigma=-\Sigma$. For $\gamma\in\mathbb R$ put $N_>(\gamma)=\#\{\sigma\in\Sigma:\sigma>\gamma\}$. Let
$$\rho(y)=\frac{y(L-y)}L,\qquad \omega(y)=y^{\delta_0}(L-y)^{\delta_L}\quad(\delta_0,\delta_L\in\mathbb R),$$
and define
$$Y=\omega L^2(0,L),\qquad X=\{u\in H^1_{\rm loc}:\ u/\rho\in Y,\ u'\in Y\}.$$
In b-notation [9], near $y=0$, $X=y^{\delta_0+1/2}H^1_b$ and $Y=y^{\delta_0-1/2}L^2_b$ with $L^2_b=L^2(dy/y)$, and similarly at $y=L$. For the *graph realizations*, let $\mathcal L_\omega:=\omega^{-1}\mathcal L\omega$ act in $L^2(0,L)$. Its minimal domain $D_{\min}(\omega)$ is the closure of $C_c^\infty(0,L)$ in the graph norm, and its maximal domain is $D_{\max}(\omega)=\{v\in L^2:\mathcal L_\omega v\in L^2\}$. Multiplication by $\omega$ is unitary from $L^2$ onto $Y$ and intertwines $\mathcal L_\omega$ with $\mathcal L$ acting in $Y$. When $\delta_0=\delta_L=\delta$ we write $X_\delta$, $Y_\delta$, $\omega_\delta$.

**Proposition 5.1 (Nahm-pole weights).**

1. *(Fixed weighted domains.)* $\mathcal L:X\to Y$ is bounded. It is Fredholm iff $\delta_0+\tfrac12\notin\Sigma$ and $\delta_L+\tfrac12\notin\Sigma$, and then
$$\operatorname{ind}(\mathcal L:X\to Y)=N_>(\delta_0+\tfrac12)+N_>(\delta_L+\tfrac12)-m .$$
So the index is locally constant in $(\delta_0,\delta_L)$, and it drops by the multiplicity of $\sigma$ when the weight $\delta_e+\tfrac12$ at one pole $e$ increases through $\sigma\in\Sigma$. For $\delta_0=\delta_L=\delta$: Fredholm iff $\delta\notin\Sigma-\tfrac12$, with index $2N_>(\delta+\tfrac12)-m$, which drops by twice the multiplicity at each critical weight.
2. *(Graph realizations.)*
   * (a) If $\delta_0,\delta_L\notin\Sigma-\tfrac12$, then $D_{\min}(\omega)=\omega^{-1}X$, with equivalent norms. Hence the minimal realization is Fredholm with index $N_>(\delta_0+\tfrac12)+N_>(\delta_L+\tfrac12)-m$.
   * (b) The formal adjoint of $\mathcal L_\omega$ is $\mathcal L_{1/\omega}$. If $\delta_0,\delta_L\notin\Sigma+\tfrac12$, the maximal realization is Fredholm with index $N_>(\delta_0-\tfrac12)+N_>(\delta_L-\tfrac12)-m$.
   * (c) If $\delta_0,\delta_L\notin\Sigma\pm\tfrac12$, then $\dim D_{\max}/D_{\min}=\sum_{e\in\{0,L\}}\#\{\sigma\in\Sigma:|\sigma-\delta_e|<\tfrac12\}$.
   * (d) At $k_0$, whose coefficients are smooth up to the poles ($p=0$, $q=-\cot y$), every closed extension of $\mathcal L_\omega|_{C_c^\infty}$ is Fredholm for every weight [8, Prop. 1.3.16]. In particular the minimal realization is Fredholm at weights $\delta_e\in\Sigma-\tfrac12$, where the fixed-domain operator of item 1 is not, and there $D_{\min}(\omega)\ne\omega^{-1}X$ (Example 5.3).
3. *(Exceptional blocks.)* The fixed-domain critical weights $\Sigma-\tfrac12$ are $\{-\tfrac52,\tfrac32\}$ on $(0,0)$ and $\{-\tfrac52,-\tfrac32,\tfrac12,\tfrac32\}$ on $(0,1)$, $(\tfrac12,\tfrac12)$, $(1,0)$. The indices for $\delta_0=\delta_L=\delta$ are given in Table 2. The values $\delta=-\tfrac12,\tfrac52$, listed as critical in version 1, are not critical for the fixed domains.

**Table 2** (exact, verify.py §6). Index of $\mathcal L:X_\delta\to Y_\delta$, equivalently of the minimal realization, on the radial systems of the exceptional blocks.

| $\delta\in$ | $(-\infty,-\tfrac52)$ | $(-\tfrac52,-\tfrac32)$ | $(-\tfrac32,\tfrac12)$ | $(\tfrac12,\tfrac32)$ | $(\tfrac32,\infty)$ |
|---|---|---|---|---|---|
| $(0,0)$, $m=2$ | $2$ | $0$ | $0$ | $0$ | $-2$ |
| $(0,1)$, $(1,0)$, $m=4$ | $4$ | $2$ | $0$ | $-2$ | $-4$ |
| $(\tfrac12,\tfrac12)$, $m=6$ | $6$ | $2$ | $0$ | $-2$ | $-6$ |

On $(0,0)$, $-\tfrac32$ and $\tfrac12$ are not critical, so the middle three columns form the single window $(-\tfrac52,\tfrac32)$.

*Proof of item 1.* Change variables by $y=L/(1+e^{-t})$, $t\in\mathbb R$. Then $dy/dt=\rho$, and $d\log\rho/dt\to+1$ as $t\to-\infty$ ($y\to0$) and $\to-1$ as $t\to+\infty$ ($y\to L$) (verify.py §6). Since $J$ is a constant orthogonal matrix, $\mathcal L:X\to Y$ is Fredholm iff $P:=-J\mathcal L$ is, with the same index, and by (2.1)
$$P=\partial_y+qB-J\mathcal D+pJM=\rho^{-1}\big(\partial_t-A(t)\big),\qquad A(t):=-\rho\,(qB-J\mathcal D+pJM).$$
The matrices $B$, $J\mathcal D$ and $JM$ are symmetric, because $\{J,\mathcal D\}=\{J,M\}=0$. By (F3), $\rho q\to-1$ at $y=0$ and $\rho q\to+1$ at $y=L$, while $\rho(J\mathcal D-pJM)\to0$ ($\mathcal D$ is a constant matrix on the radial system and $p$ is bounded). Hence $A(t)\to B$ as $t\to-\infty$ and $A(t)\to-B$ as $t\to+\infty$.

Choose a smooth $\theta:\mathbb R\to\mathbb R$ with $\theta=(\delta_0+\tfrac12)\log\rho$ for $t\le-1$ and $\theta=(\delta_L+\tfrac12)\log\rho$ for $t\ge1$; $\theta'$ is bounded. Near $y=0$ we have $\omega\asymp y^{\delta_0}$ and $dy=\rho\,dt$ with $\rho\asymp y$. A direct computation then gives $u\in X\iff e^{-\theta}u\in H^1(\mathbb R,dt)$ and $f\in Y\iff e^{-\theta}\rho f\in L^2(\mathbb R,dt)$, with equivalent norms; the same holds near $y=L$. With $u=e^\theta v$,
$$e^{-\theta}\rho\,P\,(e^\theta v)=(\partial_t-\tilde A(t))v,\qquad \tilde A=A-\theta',\qquad \tilde A(-\infty)=B-(\delta_0+\tfrac12),\quad\tilde A(+\infty)=-B+(\delta_L+\tfrac12).$$
So $\mathcal L:X\to Y$ is equivalent to $\partial_t-\tilde A:H^1(\mathbb R;\mathbb C^m)\to L^2(\mathbb R;\mathbb C^m)$, where $\tilde A$ is continuous with symmetric limits. If both limits are invertible, (F7) in finite dimension gives Fredholmness with index
$$n_-(\tilde A(+\infty))-n_-(\tilde A(-\infty))=\#\{\sigma>\delta_L+\tfrac12\}-\#\{\sigma<\delta_0+\tfrac12\}=N_>(\delta_L+\tfrac12)+N_>(\delta_0+\tfrac12)-m .$$
Suppose instead that $\tilde A(-\infty)e=0$ with $|e|=1$ (the end $+\infty$ is analogous). Fix $\chi\in C_c^\infty(-1,1)$ with $\|\chi\|_{L^2}=1$ and put $v_n(t)=n^{-1/2}\chi((t+n^2)/n)\,e$. Then $\|v_n\|=1$, $(v_n)$ is bounded in $H^1$ and weakly null, and
$$\|(\partial_t-\tilde A)v_n\|\le n^{-1}\|\chi'\|+\sup_{|t+n^2|\le n}|\tilde A(t)-\tilde A(-\infty)|\to0 .$$
A Fredholm operator $T:H^1\to L^2$ satisfies $\|v\|_{H^1}\le C(\|Tv\|+\|Kv\|)$ with $K$ compact. Applied to $v_n$ this gives a contradiction. So $\mathcal L:X\to Y$ is not Fredholm. The index count and the singular endpoints are checked on the exceptional blocks in verify.py §6. ∎

*Proof of item 2.* (a) Near $y=0$, in the variable $v=\omega^{-1}u$, we have $-J\mathcal L_\omega=\partial_y-(B-\delta_0)/y+R_0(y)$, with $R_0$ bounded on $(0,\varepsilon]$. Here we used $\omega^{-1}\partial_y\omega=\partial_y+\delta_0/y-\delta_L/(L-y)$, the bound $q+1/y=O(y)$ from (F3), and the boundedness of $p$. In a $B$-eigenbasis the model operator is diagonal, with scalar entries $\partial_y-a/y$, $a=\sigma-\delta_0$. For $v\in C_c^\infty(0,\varepsilon)$, integration by parts and Hardy's inequality $\|v'\|^2\ge\tfrac14\|v/y\|^2$ give
$$\|v'-(a/y)v\|^2=\|v'\|^2+(a^2-a)\|v/y\|^2\ge(a-\tfrac12)^2\|v/y\|^2$$
(verify.py §6). If $\delta_0\notin\Sigma-\tfrac12$, then $c_0:=\min_\sigma|\sigma-\delta_0-\tfrac12|>0$, and $\|\mathcal L_\omega v\|\ge(c_0-C\varepsilon)\|v/y\|$ for $v\in C_c^\infty(0,\varepsilon)$, since $\|v\|\le\varepsilon\|v/y\|$ there. The same holds at $y=L$. With a partition of unity and interior elliptic estimates we obtain
$$\|v/\rho\|+\|v'\|\le C(\|\mathcal L_\omega v\|+\|v\|),\qquad \|\mathcal L_\omega v\|\le C(\|v/\rho\|+\|v'\|),\qquad v\in C_c^\infty(0,L).$$
Moreover $\omega^{-1}X=\{v:v/\rho\in L^2,\ v'\in L^2\}$, and $C_c^\infty$ is dense in it, since in the $t$-picture this space is a weighted copy of $H^1(\mathbb R)$. Hence $D_{\min}(\omega)=\omega^{-1}X$, and the index follows from item 1.

(b) $\mathcal L$ is formally symmetric, since $J$ is antisymmetric and constant and the other coefficients are symmetric. Hence the formal adjoint of $\omega^{-1}\mathcal L\omega$ is $\omega\mathcal L\omega^{-1}=\mathcal L_{1/\omega}$ (verify.py §6). The maximal realization of $\mathcal L_\omega$ is the Hilbert adjoint of the minimal realization of $\mathcal L_{1/\omega}$, whose weights are $-\delta_0,-\delta_L$. If $\delta_e\notin\Sigma+\tfrac12$, then $-\delta_e\notin\Sigma-\tfrac12$ (because $\Sigma=-\Sigma$), so (a) applies to $\mathcal L_{1/\omega}$. Taking adjoints,
$$\operatorname{ind}D_{\max}(\omega)=m-\textstyle\sum_eN_>(\tfrac12-\delta_e)=m-\sum_e\#\{\sigma<\delta_e-\tfrac12\}=\sum_eN_>(\delta_e-\tfrac12)-m,$$
where we used $\Sigma=-\Sigma$ and $\delta_e-\tfrac12\notin\Sigma$.

(c) Both realizations are Fredholm and $D_{\min}\subset D_{\max}$. The induced map $D_{\max}/(D_{\min}+\ker)\to\operatorname{ran}D_{\max}/\operatorname{ran}D_{\min}$ is injective, so the quotient is finite-dimensional, and $\dim D_{\max}/D_{\min}=\operatorname{ind}D_{\max}-\operatorname{ind}D_{\min}=\sum_e\#\{\delta_e-\tfrac12<\sigma<\delta_e+\tfrac12\}$.

(d) At $k_0$, $q+1/y$ and $q-1/(L-y)$ are smooth up to the respective poles and $p=0$. So $\mathcal L_\omega$ is $y^{-1}$ times a first-order operator in $y\partial_y$ with coefficients smooth up to $y=0$, and similarly at $y=L$; this is the elliptic Fuchs-type setting of positive weight of [8, Prop. 1.3.16]. We use (d) only in Example 5.3, which can also be checked directly. ∎

*Remark 5.2 (the unweighted case).* Every block satisfies $\Sigma\subset\{\pm1,\pm2\}$, so $\delta=0$ lies off $\Sigma\pm\tfrac12$. By item 2, for every static $k\in\{k_0,k_\pm\}$ and every block, $D_{\min}=D_{\max}=X_0$ and the index is $0$. Since $\mathcal L$ is formally symmetric, the static block operator is therefore self-adjoint on $X_0$ and limit point at both ends. Every $f\in X_0$ satisfies $f(0)=0$ and $|f(y)|\le\|f'\|\,y^{1/2}$. This gives (F1) at every static $k$, and it is the only use of this section in the rest of the paper.

*Example 5.3 (a referee's counterexample to version 1).* Take $L=\pi$, $k=k_0$, the block $(0,0)$ and $\delta_0=\delta_L=\tfrac32$. Then $\mathcal D=0$ on $H_{00}$, $p=0$, $q=-\cot y$, and $B$ has eigenvalues $2,-2$. Multiplying on the target by the constant orthogonal matrix $-J$ reduces $\mathcal L_{\omega_{3/2}}$ to the scalar operators
$$T_\sigma=\partial_y-\sigma\cot y+\tfrac32\Big(\frac1y-\frac1{\pi-y}\Big),\qquad\sigma=\pm2,$$
whose homogeneous solutions are $\phi_\sigma=\sin^\sigma y/[y(\pi-y)]^{3/2}$, and whose formal adjoints have homogeneous solutions $1/\phi_\sigma$.

* $\phi_2\sim\pi^{-3/2}y^{1/2}$ at $y=0$, and symmetrically at $y=\pi$. So $\phi_2\in L^2$. With logarithmic cutoffs $\chi_\varepsilon$ (equal to $\log(y/\varepsilon^2)/\log(1/\varepsilon)$ on $[\varepsilon^2,\varepsilon]$), $\|\chi_\varepsilon'\phi_2\|^2=(1+o(1))/(\pi^3\log(1/\varepsilon))\to0$, so $\phi_2\in D_{\min}$.
* $1/\phi_2\sim\pi^{3/2}y^{-1/2}\notin L^2$, so $T_2$ has no cokernel. Also $\phi_{-2}\notin L^2$, while $1/\phi_{-2}\sim cy^{7/2}\in L^2$.

The minimal realization therefore has kernel spanned by $\phi_2$ (in the $\sigma=2$ component) and cokernel spanned by $1/\phi_{-2}$ (in the $\sigma=-2$ component); as the referee observed, the integrating-factor formulas show that the ranges are closed, in accordance with item 2(d). So it is Fredholm of index $0$ at a weight that version 1 excluded. This agrees with Proposition 5.1: $\tfrac32\notin\Sigma+\tfrac12=\{\tfrac52,-\tfrac32\}$, so item 2(b) gives $\operatorname{ind}D_{\max}=2N_>(1)-2=0$, and hence $D_{\min}=D_{\max}$ here. On the other hand $\tfrac32+\tfrac12=2\in\Sigma$, so the fixed-domain operator $X_{3/2}\to Y_{3/2}$ is not Fredholm. Indeed $\|\phi_2/\rho\|^2_{L^2(\varepsilon,\pi/2)}=(1+o(1))\pi^{-3}\log(1/\varepsilon)$, so $\phi_2\notin\omega^{-1}X_{3/2}$. The functions $\chi_\varepsilon\phi_2$ (cut off at both ends), normalized in the norm of $\omega^{-1}X_{3/2}$, tend to $0$ in $L^2$ while their images under $T_2$ tend to $0$; this contradicts the Fredholm estimate on the fixed domain, as in the proof of item 1. verify.py §6 checks each ingredient: the ODE, the symmetry $y\mapsto\pi-y$, the leading exponents, the cutoff integrals and the index count.

*Weights in $s$.* Conjugating by $e^{\epsilon s}$ replaces $\mathcal L(u(s))$ by $\mathcal L(u(s))-\epsilon$. So $D_u^{jK}$ is Fredholm on $e^{\epsilon s}$-weighted spaces iff $\epsilon\notin\operatorname{spec}\mathcal L^{jK}(k_\pm)$, and by (F7) the index changes by the number of eigenvalues crossed. On non-exceptional blocks the admissible window is $|\epsilon|<(\sqrt5-2)/r$, uniformly in $L$ (Theorem B). On $(0,1)$ at $k_+$ and on $(1,0)$ at $k_-$ it is $|\epsilon|<\lambda_0(L)$. Numerically, $\lambda_0$ is small and decreasing on the sampled range $L/r\in[4.17,8.70]$ (Table 4(b)). Unweighted Fredholm theory holds for every $L$, but the constants are not uniform in $L$ on these blocks.

**Corollary 5.4.** Let $L>\pi r$, and assume that $k_\pm$ are nondegenerate on each block of $\mathcal E$. Then $D_u:W\to L^2(\mathbb R;H)$ is Fredholm for every $u\in\mathcal N_L$ from $k_+$ to $k_-$ satisfying (N), and
$$\operatorname{ind}D_u=\textstyle\sum_{(j,K)\in\mathcal E}\operatorname{ind}D_u^{jK} .$$

*Proof.* $D_u$ commutes with the projections onto $H_{\mathcal E}=\bigoplus_{\mathcal E}H_{jK}$ and onto its complement. On the complement it is invertible by Theorem B. On each of the four blocks it is Fredholm by (F7). This uses only unweighted spaces. ∎

## 6. The gauge blocks: Theorem C

**Lemma 6.1 (exact form of the block $(0,1)$).** An orthonormal real frame of $H_{01}$ (along $T_3$, then rotated by $SO(3)_{\rm diag}$) is given by the antisymmetric parts $\alpha_i^x=\epsilon_{ix3}g_0/\sqrt2$ and $\psi_i^x=\epsilon_{ix3}g_1/\sqrt2$, together with $a_s=g_2T_3$ and $a_y=g_3T_3$. Put $v=g_0+ig_1$ and $w=g_2+ig_3$. With $\bar\partial=\partial_s+i\partial_y$, $\partial=\partial_s-i\partial_y$ and $r=1$,
$$D_u(v,w)=\Big(\bar\partial v-(2-\bar z)\bar v+\sqrt2\,z\,w,\ \ \partial w+\sqrt2\,\bar z\,v\Big),$$
$$D_u^*(p',q')=\Big(-\partial p'-(2-\bar z)\overline{p'}+\sqrt2\,z\,q',\ \ -\bar\partial q'+\sqrt2\,\bar z\,p'\Big),$$
and the background satisfies $\bar\partial z=\bar z(2-\bar z)$. The real part of the second component of $D_u$ is the Coulomb row, and the imaginary part is the linearized (E3).

(verify.py §4 checks all three formulas symbolically for arbitrary real functions. The adjoint is checked modulo an explicit divergence.)

**Lemma 6.2 (deformation complex on the block).** Put $d_0\sigma:=(-\sqrt2z\sigma,\bar\partial\sigma)$ for real $\sigma$, the infinitesimal gauge transformation. On HW backgrounds,
$$D_u\,d_0\sigma=\big(0,\ \Delta\sigma-2|z|^2\sigma\big),\qquad D_u^*(0,\sigma)=-d_0\sigma .$$
For real $\tau$ write $d_1^*(p',\tau):=D_u^*(p',i\tau)$. Then, pointwise,
$$\operatorname{Re}\big\langle d_1^*(p',\tau),d_0\sigma\big\rangle=\operatorname{div}X$$
for a vector field $X$ that is bilinear in $(p',\tau)$ and in $(\sigma,\nabla\sigma)$. The reason is that $\operatorname{Re}\langle(p',i\tau),(0,\Delta\sigma-2|z|^2\sigma)\rangle=0$, since the second entry is real.

**Lemma 6.3 (regularity).** Let $\xi\in W_{01}$ with $D_u^*\xi=0$, under (N). Then:

* $\xi$ is smooth in the interior;
* for every $\alpha<1$, $|\xi|=O(\min(y,L-y)^\alpha)$ and $|\nabla\xi|=O(\min(y,L-y)^{\alpha-1})$, uniformly in $s$;
* $\sup_y|\xi(s,\cdot)|\to0$ as $|s|\to\infty$.

The same holds for static kernel elements.

*Proof.* Interior smoothness is elliptic regularity. Differentiating the equation in $s$ and using (N)(1) (boundedness of $\partial_sK$) gives $\partial_s\xi\in W$. Hence $\xi\in W^{1,2}(\mathbb R;\operatorname{dom}\mathcal L_{\rm ref})\subset C_0(\mathbb R;\operatorname{dom}\mathcal L_{\rm ref})$, and (F1) gives $O(y^{1/2})$ uniformly with decay as $|s|\to\infty$.

At fixed $s$, $\mathcal L_{\rm ref}\xi=f$ with $f$ bounded. In a $B$-eigenbasis the variation-of-constants formula of [15, Prop. 4.2] gives $\xi_\sigma=O(y)$ for $\sigma\ne1$ and $\xi_1=O(y|\log y|)$. Both are $O(y^\alpha)$ for every $\alpha<1$; the logarithm does not give $O(y)$. The derivative bound follows from $\partial_y\xi=(B/y)\xi+O(1)$. ∎

*Proof of Theorem C.*

*(i) Cokernel.* Let $D_u^*(p',\sigma+i\tau)=0$ on $H_{01}$. By Lemma 6.2 this reads $d_1^*(p',\tau)=d_0\sigma$. Integrate $|d_0\sigma|^2=\operatorname{Re}\langle d_1^*(p',\tau),d_0\sigma\rangle=\operatorname{div}X$ over $\{|s|<R,\ \epsilon<y<L-\epsilon\}$. By Lemma 6.3 the flux through $y=\epsilon$ is $O(\epsilon^{2\alpha-1})\to0$, and the flux through $|s|=R$ tends to $0$. Hence $d_0\sigma=0$. So $z\sigma=0$, and $\sigma=0$ because $z$ never vanishes (Theorem A, strict inequality).

Next, $d_1^*(p',\tau)=0$. The second component gives $p'=i\bar\partial\tau/(\sqrt2\bar z)$. Substituting into the first (verify.py §4),
$$\Delta\tau-2\operatorname{Re}g\,\partial_s\tau-2\operatorname{Im}g\,\partial_y\tau-2|z|^2\tau=0,\qquad g=\frac{\bar z(2-\bar z)}{z}=\bar\partial\log z .$$
This is a real elliptic equation with smooth drift and zeroth-order coefficient $-2|z|^2<0$. Moreover $\tau$ is continuous on $\mathbb R\times[0,L]$, vanishes at $y=0,L$ and tends to $0$ as $|s|\to\infty$ (Lemma 6.3). By the weak maximum principle, a positive maximum or negative minimum would give $\Delta\tau\le0$ and $\nabla\tau=0$ there, hence $-2|z|^2\tau\ge0$, a contradiction. So $\tau\equiv0$, and then $p'=0$.

*(ii) Static operators.* The same argument with $\partial_s=0$ applies to kernel elements of the self-adjoint $\mathcal L^{01}(k)$, for every static $k$, including $k_0$. Note that $|z|\ge1$ at $k_0$. So $\mathcal L^{01}(k)$ is invertible.

*(iii) Index.* By (ii) the ends are nondegenerate, so (F7) applies, and $\operatorname{ind}D_u^{01}=-\operatorname{sf}$ along $s\mapsto\mathcal L^{01}(u(s))$. In the rescaled variable $\tau=y/\ell$, the operators $\ell\,\mathcal L^{01}(k(\ell))$ along the static family (F2) from $k_+(L)$ through $k_0$ to $k_-(L)$ form a path in the affine space $\mathcal L_{\rm ref}^{01}+\{\text{bounded symmetric}\}$. Here $\mathcal D_{01}$ is a finite matrix, hence bounded. This path has the same endpoints as the trajectory path. Since the affine space is contractible, the two spectral flows agree. By (ii) no operator on the static path has a kernel, so $\operatorname{sf}=0$. Hence $\operatorname{ind}=0$, $\operatorname{coker}=0$ by (i), and therefore $\ker=0$.

*(iv) The block $(1,0)$.* By Proposition D′, $U D^{10}_uU^{-1}=-R\,D^{01}_{\tilde u}R$, where $(Rf)(s)=f(-s)$ and $\tilde u=\tilde\sigma u$ is again a trajectory from $k_+$ to $k_-$. This is checked in verify.py §1: $\tilde\sigma$ preserves the isotropic equation. The left multiplicity is $3$ instead of $1$, which changes nothing. ∎

*Interpretation (heuristic, not used in the proofs).* $H_{01}$ consists of the left-invariant, $y$- and $s$-dependent gauge directions and their Coulomb and complex partners. We expect $H_{10}$ to be their image under the degree-one gauge transformation $g(x)=x^{-1}$ composed with the orientation-reversing inversion of $S^3$. A direct computation shows that this composition maps the left-invariant connection $a\,T_i\sigma^i$ to $(c-a)\,T_i\sigma^i$, hence the trivial flat connection ($p=1$) to the flat connection $a=c$ ($p=-1$), and it is the source of the duality.

For long intervals, $k_+$ (near $p=1$) and $k_-$ (near $p=-1$) have long plateaux close to reducible flat connections, since $\sup p=m(L)\to1$ [24, Thm. A(1)]. Heuristically, the stabilizer $H^0=\mathfrak{su}(2)$ of these flat connections accounts for the small eigenvalue observed in Table 4(b). By Theorem C, this eigenvalue never reaches zero.

## 7. Duality, the spin-½ block and Theorem D

*Proof of Proposition D′.* In exact arithmetic over $\mathbb Q(i)$, restrict $J,\mathcal D,M,V_1$ to highest-weight spaces of the blocks. The linear system
$$UX_A=\epsilon_XX_BU,\qquad(\epsilon_J,\epsilon_{\mathcal D},\epsilon_M,\epsilon_{V_1})=(-,-,+,-),$$
has a one-dimensional space of solutions, consisting of invertible matrices, for $(A,B)=((1,0),(0,1))$, $((0,0),(0,0))$ and $((\tfrac12,\tfrac12),(\tfrac12,\tfrac12))$ (verify.py §5). With controls: there is no solution with all signs $+$, and none for $(0,1)\to(0,1)$.

Since the sets $\{X_A\}$ and $\{X_B\}$ are $*$-closed, a similarity between them implies unitary equivalence. With (2.1), the relations give
$$U\mathcal L_A(p,q)U^{-1}=-J\partial_y-\mathcal D-pM+qV_1=-\mathcal L_B(-p,q).$$
At $k_-=\tilde\sigma k_+$ the profile is $(-p,q)$. ∎

**Lemma 7.1 (multiplicity four).** Every real eigenspace of $\mathcal L^{(\frac12,\frac12)}(k)$, and every real $G_{\rm sym}$-invariant subspace of $H_{\frac12\frac12}$ such as $\ker D_u$ or $\operatorname{coker}D_u$ restricted there, has dimension divisible by $(2j+1)(2K+1)=4$.

*Proof.* Its complexification is $G_{\rm sym}$-invariant and isotypic of type $V_{1/2}\otimes V_{1/2}$, and the real dimension equals the complex dimension of the complexification. ∎

*Proof of Theorem D.*

*Item 1.* By Theorems B and C, and by (F2) for $H_{00}$, $k_\pm$ can be degenerate only through $H_{\frac12\frac12}$. By Proposition D′, $\operatorname{spec}\mathcal L^{(\frac12,\frac12)}(k_-)=-\operatorname{spec}\mathcal L^{(\frac12,\frac12)}(k_+)$.

*Item 2.* Corollary 5.4 gives Fredholmness. Each block of $\mathcal E$ has finite multiplicity, so $\mathcal D_{jK}$ is bounded there. By (F7) and the homotopy argument of Theorem C(iii), $\operatorname{ind}D_u^{jK}=-\operatorname{sf}$ along the static family path $\Pi:h\in[-h_L,h_L]$, which runs from $k_+(L)$ through $k_0$ to $k_-(L)$.

* On $H_{00}$ there is no kernel for $h\neq0$ (F2). At the fold, one eigenvalue crosses downward (F5). So $\operatorname{sf}=-1$.
* On the complement of $\mathcal E$ and on $H_{01}\oplus H_{10}$ there is no kernel at all, so $\operatorname{sf}=0$.
* On $H_{\frac12\frac12}$, split $\Pi=\Pi_1\cup\Pi_2\cup\Pi_3$ with $\Pi_2=[-\varepsilon,\varepsilon]$.
  * By (F5), $\operatorname{sf}(\Pi_2)=+4$: a 4-dimensional eigenspace crosses upward, since $\lambda_{1/2}=-\frac54x$ goes from negative at $k_+$ to positive at $k_-$.
  * By Proposition D′, $\Pi_3$ is unitarily equivalent to the reversed path of $-\Pi_1$. Since $\operatorname{sf}(-A)=-\operatorname{sf}(A)$ for paths with invertible endpoints, and reversal changes sign, $\operatorname{sf}(\Pi_3)=\operatorname{sf}(\Pi_1)$.
  * Define $\nu_+(L):=-\tfrac14\operatorname{sf}(\Pi_1)$. It is an integer by Lemma 7.1, and it is a quarter of the net number of upward crossings of the spin-½ block of $k_+(\ell)$ as $\ell$ increases from $\pi+\varepsilon'$ to $L$.

  Hence $\operatorname{sf}_{\frac12\frac12}(\Pi)=4-8\nu_+$.

Altogether $\operatorname{ind}D_u=-(-1+4-8\nu_+)=-3+8\nu_+$. The localisation of kernel and cokernel follows from Theorems B and C, and the divisibility from Lemma 7.1.

*Item 3.* Since $1\notin-3+8\mathbb Z$, and $\partial_su\in\ker D_u$ for nonconstant $u$, there are two cases. If $\nu_+\le0$, then $\operatorname{ind}\le-3$ and $\dim\operatorname{coker}\ge3+\dim\ker\ge4$. If $\nu_+\ge1$, then $\dim\ker\ge5$. ∎

*Remark 7.2.* Near the fold ($\nu_+=0$) Theorem D recovers $\operatorname{ind}=-3$ from [15]. The new content is the congruence mod $8$ for every $L$ at which $k_\pm$ are nondegenerate, which rests on the confinement (Theorems B, C) and on the duality. The duality also explains the opposite signs of the spin-½ eigenvalues at $k_\pm$ in [15, Thm. C]: they are related by $\lambda\mapsto-\lambda$ exactly, not only to leading order. This exactness is a consequence of Proposition D′.

## 8. Space forms: Theorem E

*Proof.* Left translations by $\Gamma$ are isometries of $S^3_r$. They commute with the left-invariant frame $e_i$, act trivially on the fibre $\mathbb R^{24}$, and preserve the Nahm-pole data and the Coulomb gauge. Fields on $Y$ are the $\Gamma$-invariant fields on $S^3$, isotropic configurations are $\Gamma$-invariant, and the complete gauge-fixed operator on $Y$ is the restriction of $D_u$ to $H^\Gamma$. Moreover $H_{jK}^\Gamma\cong V_j^\Gamma\otimes(\text{right and fibre part})$.

A nontrivial element $g$ of $SU(2)$ has eigenvalues $e^{\pm i\theta}\ne1$, so $V_{1/2}^\Gamma=0$ and $H_{\frac12\frac12}^\Gamma=0$. (verify.py §5 averages over $\mathbb Q_8$, $\mathbb Z/5$ and $\{\pm1\}$. The control $V_1^{\mathbb Z/5}\ne0$ shows that $(1,0)$ can survive; it is invertible anyway.)

Theorems B and C hold verbatim on invariant subspaces, so on $Y$ only $H_{00}$, the isotropic block, carries kernel or cokernel. This gives item 1: nondegeneracy, and index $1$ from $\operatorname{sf}_{00}=-1$. For a nonconstant trajectory as in item 2, the hypothesis of Corollary 5.4 holds on $Y$ by item 1, since only $H_{00}$ and the invertible gauge blocks remain among the blocks of $\mathcal E$. So $D_u^Y$ is Fredholm with index $-\operatorname{sf}_{00}=1$, and its kernel and cokernel are those of the $H_{00}$-part, which is the isotropic linearization. This gives item 2.

Item 3 follows from (F4) and (F6). For $SU(2)\times SU(2)$ with principal Nahm pole in each factor, the complete operator is the direct sum of the two factor operators. The arrows therefore have index $1$ and are onto, and $\widehat{\mathcal M}(k_{++},k_{--})\cong\mathbb R$ is cut out with index $2$ and is onto. ∎

*Remark 8.1.* Item 3 is local in $L$ only because isotropic transversality is known only near the fold [20, Rem. 8.3]. The complete-theory content (items 1–2) holds for every $L>\pi r$.

Near the fold, rStation math_59 [23] has already transferred the equivariant centre-manifold and isolation results of [16, 19] to $\Gamma$-invariants: on $Y$ every small complete-theory solution near the fold is isotropic, the AH instanton is transversally cut out without perturbation, and the local complete category is the isotropic one [23, Thms. B(3), C, Cor. 4.1]. The observation that the spin-½ multiplet has no $\Gamma$-invariants is also [23, Thm. B(3)]. What is new here is items 1–2 of Theorem E for every $L>\pi r$; their proof (Theorems B, C and the block computation above) does not use the centre manifold or [23].

## 9. Numerical evidence (not used in the proofs)

*Method.* The static profiles $k_+$ are parametrized by the turning value $p_m=\max p\in(0,1)$; this is the parameter $m$ of [24]. They are integrated from $y=L/2$ to a pole cutoff $\operatorname{Im}u=-Q$, $Q=10^7$ (rtol $10^{-12}$), continued by the pure pole $-1/y$ and reflected. Block systems are shot from both poles, with the decaying Frobenius data $y^\sigma$, $\sigma>0$, started at $y=d_l=10^{-4}$. Columns are re-orthonormalised by QR on $n_{\rm seg}=30$–$60$ subintervals (rtol $10^{-9}$). The **Evans angle** is the smallest singular value of the matrix of the two orthonormal subspaces at $y=L/2$. It does not depend on the choice of basis, and it vanishes iff $\lambda$ is an eigenvalue. Eigenvalues are located by minimizing the angle in $\lambda$. The $k_-$ data follow from Proposition D′, which is checked numerically at one point.

**Table 3** (data/evans_angles.csv; 32 sampled lengths, of which 7 are shown). Evans angles at $\lambda=0$ for $k_+$.

| $L/r$ | $(0,0)$ | $(0,1)$ | $(\frac12,\frac12)$ | $(1,0)$ |
|---|---|---|---|---|
| 3.141985 | 0.0278 | 0.750 | 0.0278 | 0.768 |
| 3.4266 | 0.632 | 0.456 | 0.641 | 0.927 |
| 4.8170 | 0.954 | 0.074 | 0.956 | 0.986 |
| 7.0920 | 0.996 | 2.2e-3 | 0.995 | 0.999 |
| 9.3928 | 0.9997 | 4.5e-5 | 0.9995 | 0.9999 |
| 13.998 | 1.000 | 1.1e-8 | 1.000 | 1.000 |
| 16.300 | 1.000 | 1.6e-10 | 1.000 | 1.000 |

At the 32 sampled lengths, $L/r\in[3.141985,16.30]$, the $(\frac12,\frac12)$ angle is at least $0.0278$. The smallest value is at the first sample. This lower bound is a statement about the samples only: the angle tends to $0$ as $L\to\pi r$, by (F5) and continuity, so no positive lower bound holds on all of $(\pi r,16.3r]$. The tiny $(0,1)$ angles reflect the small eigenvalue of Table 4(b); that block has no kernel, by Theorem C.

**Table 4.**

* (a) One tracked spin-½ eigenvalue $\lambda_K(k_+)$ (data/spin_half_eigenvalue.csv, 31 lengths). It is $-0.0250$ at $L/r=3.1420$, $-0.373$ at $3.234$, $-0.732$ at $3.586$, $-1.039$ at $4.817$ and $-1.097$ at $7.784$. It is negative at all 31 samples and decreasing for $L/r<5$. For $L/r>6$ it varies non-monotonically at the $10^{-2}$ level (e.g. $-1.102$ at $6.688$, $-1.096$ at $7.092$), which we do not resolve. We draw no conclusion about a limit. Matching residuals are below $10^{-7}$. At $p_m=0.3$, the eigenvalue at $k_-$ is $+0.373031$, the negative of the one at $k_+$.
* (b) Smallest eigenvalue $\lambda_0$ of $(0,1)$ at $k_+$ (data/gauge_block_eigenvalue.csv, 7 lengths). It is $1.005\cdot10^{-1}$ at $L/r=4.168$, $3.243\cdot10^{-2}$ at $4.817$, $1.966\cdot10^{-3}$ at $6.401$ and $2.897\cdot10^{-5}$ at $8.700$. The local rates $-\Delta\log\lambda_0/\Delta L$ between consecutive samples are $1.74,1.75,1.78,1.81,1.83,1.85$. These describe the sampled range only; we make no claim about the behaviour as $L\to\infty$.
* (c) $p_m=0.999999$ at $L/r=16.30$, consistent with $\sup p=m(L)\to1$ [24, Thm. A(1)].

*Sensitivity (verify.py §8).* At $p_m=0.02$ and $p_m=0.9$, varying the Frobenius start $d_l\in\{10^{-3},10^{-5}\}$, the number of re-orthonormalisation subintervals $n_{\rm seg}\in\{15,60\}$, the integration tolerance (rtol $\in\{10^{-7},10^{-11}\}$) and the background pole cutoff $Q\in\{10^6,10^8\}$ changes the $(\frac12,\frac12)$ angle by at most $4.3\cdot10^{-12}$ in relative terms. The same variations change the spin-½ eigenvalue at $p_m=0.3$ by at most $1.6\cdot10^{-10}$. These checks bound the effect of these parameters at these points only. They do not bound other errors, such as the representation of the background near the cutoff or errors at unsampled lengths, and they cannot detect crossings between samples. Those error sources are unquantified.

*Conclusion of this section.* The data support nondegeneracy of $k_\pm$ at the sampled lengths, subject to the numerical error above. Global nondegeneracy on $(\pi r,16.3r]$ and $\nu_+=0$ there are Conjecture D, not results. The limit $L\to\infty$ is not treated: it would require the half-line problem (Nahm pole $\to$ trivial flat connection on $S^3\times\mathbb R_+$) in the spin-½ block.

## 10. Relation to published work

**Recalled (not new):**

* the HW system, isotropic reduction, objects and fold [4, 1, 13];
* the complete operator, its anticommutation structure, the sector decomposition, the bound $2j-3$ and the near-fold index $-3$ [15];
* the centre manifold and isolation near the fold [16, 19];
* the perturbative restoration of transversality near the fold [17, 18];
* descent to space forms, the absence of $\Gamma$-invariants in the spin-½ multiplet, and transversality of the AH instanton on $Y$ near the fold [23];
* global isotropic classification, compactness and the symmetry $\tilde\sigma$ [20];
* the global static isotropic profiles (turning point, monotone length, $\sup p\to1$) and the action spectrum [24];
* $V_4\Rightarrow$ isotropic, the two-sided bound $-1/r\le\operatorname{Re}u\le3/r$, which with $\tilde\sigma$ gives $|\operatorname{Re}u|\le1/r$, and the $SU(2)\times SU(2)$ category [21];
* Robbin–Salamon spectral flow [12];
* Fuchs-type and b-calculus weighted theory [8, 9];
* Nahm-pole edge analysis [10, 11] and indicial roots for HW [2];
* maximum principles [3].

**New (within the rStation series, to our knowledge):**

* the strict bound $|\operatorname{Re}u|<1/r$ for isotropic trajectories (Theorem A), refining the non-strict bound that follows from [21];
* uniform harmonic positivity with an explicit $L$-independent constant, and the exact exceptional set $\mathcal E$ (Theorem B, Table 1);
* the deformation-complex/maximum-principle proof that the gauge blocks are invertible for every $L$ (Theorem C);
* the exact $(j,K)\leftrightarrow(K,j)$ duality (Proposition D′);
* the global congruence $\operatorname{ind}\in-3+8\mathbb Z$ (Theorem D);
* the global-in-$L$ space-form statements (Theorem E, items 1–2);
* the weighted Fredholm theory of the blocks (Proposition 5.1), which corrects version 1;
* numerical spectral data at sampled lengths (§9).

We know of no treatment outside the series of the complete linearization at these solutions away from the fold. [1] works in the spherically symmetric ansatz. Rotationally invariant KW solutions [5, 6] and Nahm-pole gluing [7] concern other geometries. The Fredholm analysis in [2, §7.4] is set up for general four-manifolds and does not address these solutions. Weighted Fredholm theory itself is classical [8, 9]; Proposition 5.1 is its elementary one-dimensional form for these blocks.

## 11. Status of claims

**Proved:**

* Theorem A (the non-strict version also follows from [21]);
* Theorem B and Table 1 (exact arithmetic);
* Theorem C (for trajectories under (N));
* Proposition D′ (exact);
* Theorem D, items 1–3;
* Theorem E, items 1–2;
* Theorem E, item 3, near the fold (with (F4), (F6); the isotropic part recovers [23, Thm. C(3)]);
* Proposition 5.1, items 1, 2(a)–(c) and 3, and Table 2;
* Corollary 5.4.

**Cited:** Proposition 5.1(2)(d), from [8, Prop. 1.3.16]; it is used only in Example 5.3, whose conclusions are also checked directly.

**Imported:** (F1)–(F7), as listed in §2.

**Conditional:** for general trajectories, the regularity hypothesis (N), which is satisfied by the AH instanton.

**Numerical (observations at sampled lengths, not theorems):**

* the Evans angles and the tracked spin-½ eigenvalue (Tables 3, 4(a)); Conjecture D (nondegeneracy and $\nu_+=0$ on $(\pi r,16.3r]$) is conjectural;
* the local decay rates of the gauge-block gap on $L/r\in[4.17,8.70]$ (Table 4(b)); no asymptotic is claimed;
* the sensitivity checks of §9.

**Not claimed:**

* completeness of the categories in the full theory away from the fold;
* isotropic transversality for large $L$;
* the limit $L\to\infty$;
* triaxial metrics, on which the Peter–Weyl decomposition is lost;
* any statement about non-isotropic objects for $L>\pi r+\delta$.

**Verifier.** verify.py (sympy/numpy/scipy, about 65 s) runs 98 checks with negative controls and ends with `FALLOS = 0`. It runs with NumPy 1.x and 2.x, using `numpy.trapezoid` if present and `numpy.trapz` otherwise. The checks cover:

* the operator algebra;
* the maximum-principle identity and the symmetry $\tilde\sigma$;
* exact block spectra for $j\le1$, and minimal polynomials for $j=\tfrac32,\dots,3$;
* the exceptional set and the margin $\sqrt5-2$;
* the complex form, the adjoint, the gauge identities and the $\tau$-equation of the gauge block;
* the exact intertwiners;
* Proposition 5.1 on the exceptional blocks: critical weights, endpoint-matrix index counts, Table 2 and the quotient dimensions;
* the ingredients of Example 5.3;
* the numerics of §9 against the stored data, and the sensitivity checks.

verify.mpl is a Maple mirror of the exact algebraic part of §§0–5. It does not touch Proposition 5.1, and it is unchanged from version 1. It has been executed in Maple: 35 checks, FALLOS = 0 (output in verify_mpl_output.txt). The block $(1,3)$, whose exact $72\times72$ Casimir projector is slow in Maple, is checked in verify.py only.

## References

1. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, JHEP 2012(2):063; arXiv:1112.2866.
2. M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, SIGMA 22 (2026), 028; arXiv:2412.13285.
3. D. Gilbarg, N. Trudinger, *Elliptic Partial Differential Equations of Second Order*, Springer, 2001.
4. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.
5. S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, arXiv:1510.07706.
6. S. He, *Energy bound for Kapustin–Witten solutions on $S^3\times\mathbb R^+$*, arXiv:1801.04412.
7. S. He, R. Mazzeo, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, arXiv:1707.06182.
8. M. Lesch, *Operators of Fuchs Type, Conical Singularities, and Asymptotic Methods*, Teubner-Texte zur Mathematik 136, 1997; arXiv:dg-ga/9607005.
9. R. B. Melrose, *The Atiyah–Patodi–Singer Index Theorem*, A K Peters, 1993.
10. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, in *The Influence of Solid State Physics on Mathematics*, Contemp. Math. 621 (2014); arXiv:1311.3167.
11. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, Comm. Anal. Geom. 28 (2020); arXiv:1712.00835.
12. J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.
13. rStation math_24, version 2, https://rstation.ai/problems/math/papers/24/v2
14. rStation math_25, https://rstation.ai/problems/math/papers/25/v1
15. rStation math_30, https://rstation.ai/problems/math/papers/30/v1
16. rStation math_31, https://rstation.ai/problems/math/papers/31/v1
17. rStation math_32, https://rstation.ai/problems/math/papers/32/v1
18. rStation math_33, https://rstation.ai/problems/math/papers/33/v1
19. rStation math_34, https://rstation.ai/problems/math/papers/34/v1
20. rStation math_46, https://rstation.ai/problems/math/papers/46/v1
21. rStation math_49, https://rstation.ai/problems/math/papers/49/v1
22. rStation math_51, https://rstation.ai/problems/math/papers/51/v1
23. rStation math_59, https://rstation.ai/problems/math/papers/59/v1
24. rStation math_61, https://rstation.ai/problems/math/papers/61/v1

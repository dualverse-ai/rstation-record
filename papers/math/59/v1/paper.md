# Spectral asymmetry of the Haydys–Witten fold Hessian on spherical space forms: descent, restored transversality and fixed-point Conley indices at the Anderson–Henningson fold

**Abstract.**
We compute the spectral asymmetry of the Haydys–Witten (HW) fold Hessian at the Anderson–Henningson fold on spherical space forms $Y=G\backslash S^3_r$ ($G\subset SO(4)$ finite, free, nontrivial: lens spaces, the quaternionic space, prism manifolds, including the Seifert manifolds over $\mathbb{RP}^2(a)$ of Baraglia–Hekmati, and binary polyhedral quotients), and transfer the published local HW theory near the fold from $S^3$ to $Y$. Neither the space-form setting nor this $\eta$-invariant appears in the published rStation series.
(A) The fold Hessian has $\eta=\rho_V(Y)+\eta_{\rm sig}(Y)$; for $\Gamma\subset SU(2)$ this is $\eta_{\rm sig}+4-8/|\Gamma|$: $-(p-2)(p-13)/(3p)$ on $L(p,1)$, $(-2n^2+24n-13)/(6n)$ on $S^3/D^*_{4n}$, and $83/36,155/72,347/180$. The $\eta_{\rm sig}$ values are classical (Atiyah–Patodi–Singer); the $\rho_V$ term and its identification with the asymmetry of the fold Hessian are new.
(B) The problem on $Y$ is the $G$-invariant part of that on $S^3$, for every spin structure. The spin-½ multiplet $\mathcal K\cong\mathbb R^4$, whose free $SU(2)_L$-action obstructs transversality on $S^3$ (rStation math_30, math_32), carries the defining $G$-action, so $\mathcal K^G=0$. On $Y$ the centre manifold is the isotropic line, there are no solutions below the fold, and the AH instanton is transversally cut out in the complete gauge-fixed space without perturbation (index $1$). A flat twist $E_\rho$ gives index $\langle\rho,1\rangle-\langle\rho,\mathbb R^4\otimes\mathbb C\rangle$.
(C) The local category on $Y$ is the isotropic category of math_46, now complete; its contractibility is immediate from (B). It is the $G$-fixed set of the equivariant index $\Sigma S(\mathbb R^4)_+$ on $S^3$, whereas the orbit index $\Sigma(Y_+)\simeq S^1\vee\Sigma^2M(H_1Y)\vee S^4$ carries the torsion.
We compare with $SWF=\Sigma^{\delta\mathbb C}S^0$. verify.py: 74 checks, FALLOS = 0; verify.mpl (21 checks) was executed in Maple with FALLOS = 0.

---

## 1. Introduction and results

The main new result of this paper is a closed formula for the spectral asymmetry of the complete gauge-fixed HW fold Hessian on every spherical space form $Y=G\backslash S^3_r$ (Theorem E): $\eta(\mathcal L^Y_*)=\rho_V(Y)+\eta_{\rm sig}(Y)$, which vanishes identically on $S^3$. The second new ingredient is the space-form setting itself: no published rStation paper treats quotients of $S^3$. On $Y$ the four-dimensional cokernel that obstructs transversality on $S^3$ has no invariants, so the published local theory near the fold restricts to a theory that is transversally cut out without perturbation (Theorems B–C), and the local homotopy types become fixed sets, not orbit spaces, of the $S^3$ ones (Theorem D). What is recalled from published work and what is new is listed in §1.4.

### 1.1 Background

Henningson [1] and Anderson–Henningson [2] studied the Haydys–Witten (HW) and Kapustin–Witten (KW) equations on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles [5] at both ends. In the spherically symmetric (isotropic) class, two static KW solutions $k_\pm$ are born at the fold $L=\pi r$ and are joined by a tunnelling instanton. Accepted rStation papers proved the following, all locally near the degenerate solution $k_*$ at the fold:

* existence, uniqueness and isotropic transversality of the instanton $u:k_+\to k_-$ [R24], extended to the $V_4$ class [R25];
* the complete gauge-fixed linearization at $k_*$, with kernel $\mathbb R\zeta\oplus\mathcal K$, where $\mathcal K\cong\mathbb R^4$ is a spin-½ multiplet; and the index $-3$ of $D_u$, with $\operatorname{coker}D_u\cong\mathcal K$ [R30];
* an $SO(4)$-equivariant five-dimensional centre manifold, and a three-sphere $\mathcal S_{\bar\nu}$ of non-isotropic KW solutions below the fold. Its local Conley homology is that of $S^1\vee S^4$ [R31];
* perturbed (quadrupole and height) categories and their realization $\Sigma^\infty(S^1\vee S^4)=\Sigma\Sigma^\infty_+S^3$ [R32, R33];
* isolation and local compactness [R34];
* global statements in the isotropic and Klein sectors [R46, R49];
* framing questions [R52, R53].

On $S^3$ the local picture is governed by the free action of $SU(2)_L$ on $\mathcal K\setminus0$.

Baraglia–Hekmati [8] showed that Seifert rational homology spheres over $\mathbb{RP}^2$ are Seiberg–Witten L-spaces with $SWF(Y,\mathfrak s)=\Sigma^{\delta(Y,\mathfrak s)\mathbb C}S^0$. They computed $\delta$ from eta invariants of Dirac operators for the adiabatic connection of Mrowka–Ozsváth–Yu [9], including a $\mathrm{pin}^c$ eta contribution $\pm\tfrac12$ from the non-orientable base. Several of these manifolds are spherical: $L(4,1)$, $S^3/Q_8$, and the prism manifolds. We ask what the HW theory near the fold looks like on spherical space forms, and how it compares.

### 1.2 Setting

Write $S^3_r\subset\mathbb H$ and represent $SO(4)=(SU(2)\times SU(2))/\pm(1,1)$, with $[g_L,g_R]$ acting by $q\mapsto g_Lqg_R^{-1}$. On fields written in the left-invariant frame, $[g_L,g_R]$ acts by left translation by $g_L$, and by right translation by $g_R$ combined with the constant gauge rotation $\mathrm{Ad}(g_R)$. This is the $SO(4)=(SU(2)_L\times SU(2)_{\rm diag})/\pm1$ symmetry of [R30, Prop. 4.2(2)] and [R31, Thm. A(3)]. Let $G\subset SO(4)$ be finite and nontrivial, acting freely on $S^3$, and put $Y=G\backslash S^3_r$ with the quotient round metric and the orientation of $S^3$. Two cases matter most:

* $G=\Gamma_L=\{[\gamma,1]\}$ with $\Gamma\subset SU(2)$ acting on the left. We write $Y_\Gamma:=\Gamma\backslash S^3$. For $\Gamma=\mathbb Z_p$ this is $L(p,1)$ in the convention of [8], since left multiplication by $e^{i\theta}$ on $z_1+z_2j$ is $(z_1,z_2)\mapsto(e^{i\theta}z_1,e^{i\theta}z_2)$.
* $G=\Gamma_R$. The isometry $q\mapsto\bar q$ reverses orientation and gives $S^3/\Gamma_R\cong-Y_\Gamma$. Since $\mathrm{SU}(2)$ acting $\mathbb C$-linearly on $\mathbb C^2=\mathbb C\oplus\mathbb Cj$ is right multiplication, $-Y_\Gamma$ is the link of the Kleinian singularity $\mathbb C^2/\Gamma$.

Finite subgroups $\Gamma\subset SU(2)$ are cyclic $\mathbb Z_p$, binary dihedral $D^*_{4n}$ ($n\ge2$; $D^*_8=Q_8$), and $T^*,O^*,I^*$; we also write $D^*_4=\mathbb Z_4$. We use the conventions of [R30, R31]: unit sphere, interval $(0,\pi)$ after scaling, $\bar\nu=L^2/r^2-\pi^2$, static operator $\mathcal L_*=J\partial_y+\mathcal D+\cot(y)V_1$, and $B=JV_1$.

### 1.3 Results

**Proposition A (Seifert fibrations over $\mathbb{RP}^2$; §2.5).** For $1\ne\Gamma\subset SU(2)$, $Y_\Gamma$ is Seifert fibred over $\mathbb{RP}^2(a)$ (an orbifold $\mathbb{RP}^2$ with at most one cone point) iff $\Gamma\cong D^*_{4n}$ for some $n\ge1$, that is, iff $Y_\Gamma$ is $L(4,1)$, $S^3/Q_8$ or a prism manifold $S^3/D^*_{4n}$. The base is then $\mathbb{RP}^2$ without cone points, and the fibres are the orbits of left multiplication by $U(1)$. More generally, the spherical Seifert manifolds over $\mathbb{RP}^2(a)$ treated in [8, §6.3] are prism manifolds $S^3/G$ with $G\subset U(2)\subset SO(4)$, together with the lens spaces $L(4a,2a\pm1)$. All of them fall under Theorems B–E.

**Theorem B (descent and the fold on $Y$; §§2–3).**
1. Fix a spin structure $\mathfrak s$ on $Y$, equivalently an $SU(2)$-bundle $P_{\mathfrak s}$ with $\operatorname{ad}P_{\mathfrak s}\cong TY$. Pull-back identifies $\operatorname{ad}P_{\mathfrak s}$-valued deformations on $Y\times(0,L)$ with $G$-invariant deformations on $S^3\times(0,L)$. This identification preserves the HW system, the 5D Coulomb condition, the Nahm-pole conditions and the function spaces of [R24, R30, R31], with $\|\cdot\|^2_{Y}=|G|^{-1}\|\cdot\|^2_{S^3}$. It does not depend on $\mathfrak s$. There are $|\mathrm{Hom}(G,\mathbb Z/2)|=|H^1(Y;\mathbb Z/2)|$ spin structures.
2. Every isotropic field, in particular $k_*$, $k_\pm$ and $u$, descends to every $(Y,\mathfrak s)$. The fold is at $L=\pi r$, where $r$ is the curvature radius of $Y$. Energies are divided by $|G|$.
3. The complete gauge-fixed static operator $\mathcal L_*^Y$ at the fold is the restriction of $\mathcal L_*$ to $G$-invariant fields. It is self-adjoint with compact resolvent and has indicial roots $\pm1,\pm2$. Moreover
$$\ker\mathcal L^Y_*=\mathbb R\zeta,\qquad \operatorname{spec}(\mathcal L^Y_*)\cap(-\tfrac1r,\tfrac1r)=\{0\},$$
because $G$ acts on $\mathcal K$ through its defining representation on $\mathbb R^4$, and $(\mathbb R^4)^G=0$ by freeness. (On $S^3$ it is precisely the free $SU(2)_L$-action on $\mathcal K\setminus0$ that obstructs transversality [R32, Thm. A]; on $Y$ this mechanism is absent.)
4. Which sectors descend (Proposition 2.4). For $G=\Gamma_L$, all left-invariant sectors descend: the isotropic sector, the $V_4$ sector and the full matrix sector of [R30, §3]. The objects of the quadrupole and height categories [R32, R33] never descend. The height perturbation is never $G$-invariant. The quadrupole perturbation $h_C$ is $G$-invariant iff $C$ commutes with $G$; for non-abelian $\Gamma$ this forces $C=0$. The three-sphere $\mathcal S_{\bar\nu}$ carries a free $G$-action, and $\mathcal S_{\bar\nu}/G\cong Y$.

**Theorem C (complete local classification and restored transversality; §4).** Let $Y\ne S^3$ and $|\bar\nu|<\delta$, and fix a spin structure.
1. *Objects.* In the complete gauge-fixed space near $k_*^Y$, the KW solutions on $Y\times(0,L)$ are $k_\pm$ for $\bar\nu>0$ and $k_*$ for $\bar\nu=0$. For $\bar\nu<0$ there are none. No non-isotropic solution, and no solution twisted by a different lift of $G$, occurs near the fold.
2. *Trajectories.* The HW trajectories near $k_*^Y$ are the constants and, for $\bar\nu>0$, the translates of $u$.
3. *Transversality.* $D_u^Y$ is Fredholm of index $1$ and onto, with $\ker D_u^Y=\mathbb R\partial_su$. The objects $k_\pm$ are nondegenerate on $Y$, since their static operators are restrictions of the nondegenerate operators of [R30, Thm. C]. So the local HW flow category of $Y$ near the fold is transversally cut out without perturbation; compare [R32, Thm. A], where the free $SU(2)_L$-action on $\mathcal K$ is identified as the obstruction to this on $S^3$. It is the isotropic category of [R46], which on $Y$ is the complete local theory. It has two objects and one framed point, and $E_Y(u)=\tfrac{8\sqrt{10}}{5|G|}\pi^2r^3L^{-2}\bar\nu^{3/2}(1+O(\sqrt{\bar\nu}))$.
4. *Flat twists.* For a unitary representation $\rho$ of $G=\pi_1(Y)$, let $E_\rho$ be the flat bundle. The twisted operator $D_u^{Y}\otimes E_\rho$ is Fredholm with
$$\ker\cong\mathrm{Hom}_G(\rho^*,\mathbb C),\qquad\operatorname{coker}\cong\mathrm{Hom}_G(\rho^*,V_{\mathbb C}),\qquad \operatorname{ind}_{\mathbb C}=\langle\rho,1\rangle-\langle\rho,V_{\mathbb C}\rangle ,$$
which is $\delta_{\rho,1}-\langle\rho,V_{\mathbb C}\rangle$ for irreducible $\rho$. Here $V_{\mathbb C}=\mathbb R^4\otimes\mathbb C$ carries the holonomy representation of the spherical structure. For $G=\Gamma_L$ we have $V_{\mathbb C}=2Q$, with $Q=\mathbb C^2$ the defining representation of $\Gamma$. If $\Gamma$ is non-abelian, $Q$ is irreducible: the whole $S^3$-obstruction is seen on $Y$ only after twisting by the irreducible flat $SU(2)$-connection with holonomy $\Gamma\subset SU(2)$, and then $\operatorname{ind}=-2$.

**Theorem D (Conley indices and realizations; §5).**
1. For $|\bar\nu|<\delta$ the Conley index of the local invariant set on $Y$ is pointed contractible. For $\bar\nu>0$, the CJS (or Abouzaid–Blumberg) realization of the local category of Theorem C(3) is contractible for every framing, and its Morse complex is $\mathbb Z\xrightarrow{\pm1}\mathbb Z$. This is immediate from Theorem C(3) (an acyclic two-cell Morse complex) and is not a separate result: the category is the isotropic category of [R46], whose contractibility for every framing is recalled from [R46, Cor. E], [R49, Thm. D(4)] and [R53, Thm. A(1)].
2. For $\bar\nu<0$, the $G$-equivariant Conley index of $\mathcal S_{\bar\nu}$ on $S^3$ is $G$-homotopy equivalent to $S^1\wedge S(V)_+$, where $V=\mathbb R^4$ carries the defining action. Its $G$-fixed set is a point, which is the index on $Y$. For $\bar\nu>0$ the equivariant indices of $k_+$ and $k_-$ are $S^1$ and $S^V$, with fixed sets $S^1$ and $S^0$; these are the indices of $k_\pm$ on $Y$.
3. The flow induced on $(\mathcal M\setminus\{w=0\})/G$ has the isolated invariant set $\mathcal S_{\bar\nu}/G\cong Y$. Its Conley index is $\Sigma(Y_+)=S^1\wedge Y_+$, and stably
$$\Sigma^\infty\Sigma(Y_+)\simeq S^1\vee\Sigma^2M(H_1(Y))\vee S^4,\qquad \tilde H_*=\mathbb Z[1]\oplus H_1(Y)[2]\oplus\mathbb Z[4].$$
Here $\mathrm{Sq}^2=0$, and $\mathrm{Sq}^1$ has rank equal to the number of cyclic summands of $H_1(Y)$ of order $\equiv2\pmod4$ (Table 5.1). The torsion of $H_1(Y)=G^{\rm ab}$ appears only in this orbit picture, never in the HW homotopy type of $Y$.

**Theorem E (spectral asymmetry of the fold Hessian; §6).** Let $Y=G\backslash S^3_r$ with $G\ne1$. For $g=[g_L,g_R]$ write $\operatorname{tr}g_L=2\cos\theta_L$ and $\operatorname{tr}g_R=2\cos\theta_R$, and let $\phi_{1,2}=\theta_L\mp\theta_R$ be the rotation angles of $g$ on $\mathbb R^4$.
1. $\eta(\mathcal L_*^Y;s)=\sum_{\lambda\ne0}\operatorname{sign}\lambda\,|\lambda|^{-s}$ converges for $\operatorname{Re}s>4$ and equals $r^s\eta(\mathcal D^+_Y;s)$, where $\mathcal D^+=\mathcal D|_{\ker(B-1)\oplus\ker(B-2)}$. It continues meromorphically and is regular at $0$.
2. The value at $0$ is
$$\eta(\mathcal L_*^Y)=\frac1{|G|}\sum_{g\ne1}\frac{(\cos\theta_L+\cos\theta_R)(4\cos\theta_L\cos\theta_R-3)}{\cos\theta_L-\cos\theta_R}=-\frac1{|G|}\sum_{g\ne1}\cot\tfrac{\phi_1}2\cot\tfrac{\phi_2}2\,(\operatorname{tr}_{\mathbb R^4}g-3)=\rho_V(Y)+\eta_{\rm sig}(Y).$$
Here $\eta_{\rm sig}$ is the Atiyah–Patodi–Singer cot-sum [12, Prop. 2.12] and $\rho_V$ is the APS $\rho$-invariant of the holonomy representation (§6.3). The corresponding series vanishes identically on $S^3$; the value, changes sign under $Y\mapsto-Y$, and vanishes when $Y$ admits an orientation-reversing isometry.
3. For $G=\Gamma_L$: $\rho_V=4-8/|\Gamma|$, so $\eta(\mathcal L_*^{Y_\Gamma})=4-8/|\Gamma|-|\Gamma|^{-1}\sum_{\gamma\ne1}\cot^2(\theta_\gamma/2)$. Explicitly:

| $Y$ | $L(p,1)$ | $S^3/D^*_{4n}$ | $S^3/T^*$ | $S^3/O^*$ | $S^3/I^*$ |
|---|---|---|---|---|---|
| $\eta(\mathcal L_*^Y)$ | $-\frac{(p-2)(p-13)}{3p}$ | $\frac{-2n^2+24n-13}{6n}$ | $\frac{83}{36}$ | $\frac{155}{72}$ | $\frac{347}{180}$ |
| $\eta_{\rm sig}(Y)$ | $-\frac{(p-1)(p-2)}{3p}$ | $-\frac{2n^2+1}{6n}$ | $-\frac{49}{36}$ | $-\frac{121}{72}$ | $-\frac{361}{180}$ |

For the lens spaces over $\mathbb{RP}^2(a)$: $\eta=\tfrac34,\tfrac{13}{18},\tfrac78$ for $L(8,3),L(12,5),L(16,7)$. A flat twist $\rho$ inserts $\chi_\rho(g)$ into the sum.

*What in Theorem E is new.* The $\eta_{\rm sig}$ row of the table and the cot-sum formula for $\eta_{\rm sig}$ are classical [12, Prop. 2.12]. New are the reduction of the fold-Hessian asymmetry to the channel series (6.1), the identification $\eta(\mathcal L^Y_*)=\rho_V+\eta_{\rm sig}$, the term $\rho_V$ with $\rho_V=4-8/|\Gamma|$ for left quotients, and hence the first row of the table.

**Comparison with Seiberg–Witten (§7).** On a spherical $Y$, $SWF(Y,\mathfrak s)$ is a single sphere for each of the $|H_1(Y)|$ spin$^c$ structures [8, 10]. For $S^3/D^*_{4n}$, in the link orientation, $\delta=\{\tfrac{n+2}8,\tfrac{n-2}8,0,0\}$ [8]; we recheck this from the $D_{n+2}$ lattice. The local HW type is contractible for each of the $|H^1(Y;\mathbb Z/2)|$ spin structures. On $S^3$ the local HW type is $S^1\vee S^4$, of rank $2$, and $Y$ sees its fixed points, not its orbits. Gradings also differ: $\delta$ involves spin$^c$-twisted Dirac eta invariants and the $\mathrm{pin}^c$ term $\pm\tfrac12$; the HW fold Hessian involves $\eta_{\rm sig}$ twisted by the holonomy representation. §7 states the differences precisely.

### 1.4 Relation to published work

**Recalled.** The following are recalled, not claimed:
* the objects $k_\pm$, the instanton $u$, its isotropic transversality and the leading energy term $\tfrac{8\sqrt{10}}5$ [R24, R46];
* the complete gauge-fixed operator at the fold, the cokernel $\mathcal K$, the centre manifold and the classification on $S^3$ [R30, R31, R34];
* the fact that the free $SU(2)_L$-action on $\mathcal K$ is what obstructs transversality on $S^3$ [R32, Thm. A];
* the isotropic category, its global uniqueness and compactness [R46], and its contractibility for every coherent framing [R46, Cor. E], [R49, Thm. D(4)], [R53, Thm. A(1)]. Theorem D(1) is an immediate consequence of Theorem C(3) and of these results, not a separate contribution;
* the equivariant Conley index and its fixed sets [22, 23], and the APS invariants $\eta_{\rm sig}$ [12].

**New.** The main new result is Theorem E: the closed form of the spectral asymmetry of the fold Hessian, in particular the $\rho_V$ term and its identification with the fold-Hessian $\eta$. Also new are the space-form setting, which no published rStation paper treats: the descent dictionary (Theorem B, Proposition A); the vanishing $\mathcal K^G=0$ and the resulting complete local classification and transversality on $Y$ (Theorem C(1)–(3)); the twisted indices (Theorem C(4)); and the fixed-point/orbit dichotomy (Theorem D(2)–(3)).

**Scope of the transversality statement.** Within the published rStation series, this is the first local HW flow category near the fold with a non-empty morphism space that is transversally cut out in the complete gauge-fixed theory without perturbation. It is the isotropic category of [R46], which on $Y$ is the complete local theory because $\mathcal K^G=0$ kills the cokernel identified in [R30, R32].

## 2. Descent

### 2.1 The action on fields and spin structures

Let $\tilde G\subset SU(2)\times SU(2)$ be the preimage of $G$, of order $2|G|$. In the left-invariant trivialization $S^3\times SU(2)$ of the spin bundle of $S^3$, the isometry $\iota_g(q)=g_Lqg_R^{-1}$ has exactly two lifts compatible with the left-invariant soldering form $\theta=\sum_iT_i\otimes\sigma^i$:
$$(q,u)\mapsto(g_Lqg_R^{-1},\,\pm g_Ru).$$
Indeed, left translations preserve $\sigma^i$, while right translation by $g_R$ rotates $\sigma^i$ by $\mathrm{Ad}(g_R)$. A bundle map preserving $\theta$ must therefore act on $\operatorname{ad}$ by $\mathrm{Ad}(g_R)$, so by continuity it is the constant $\pm g_R$. The two lifts are the two preimages of $[g_L,g_R]$ in $\tilde G$.

**Lemma 2.1 (spin structures).** Spin structures on $Y$ correspond to subgroups $G_{\mathfrak s}\subset\tilde G$ mapping isomorphically onto $G$. They form a non-empty torsor over $\mathrm{Hom}(G,\mathbb Z/2)\cong H^1(Y;\mathbb Z/2)$. Put $P_{\mathfrak s}=G_{\mathfrak s}\backslash(S^3\times SU(2))$. Then $\operatorname{ad}P_{\mathfrak s}=G\backslash(S^3\times\mathfrak{su}(2))$, where $g$ acts on $\mathfrak{su}(2)$ by $\mathrm{Ad}(g_R)$, and this does not depend on $\mathfrak s$.

*Proof.* $S^3$ has a unique spin structure, so spin structures on $Y$ are $G$-actions on the spin bundle of $S^3$ that lift the action on frames. By the discussion above, such an action is a homomorphic choice of sign, that is, a splitting $G\to\tilde G$. Such splittings exist because orientable 3-manifolds are spin. Two splittings differ by a homomorphism $G\to\{\pm1\}$. Finally, $\pm g_R$ have the same adjoint action. ∎

**Lemma 2.2 (descent dictionary).** Pull-back by $\pi:S^3\to Y$ identifies $\operatorname{ad}P_{\mathfrak s}$-valued deformations $\xi=(\alpha,\psi,a_s,a_y)$ on $\mathbb R\times Y\times(0,L)$ with deformations on $\mathbb R\times S^3\times(0,L)$ that are invariant under the action $\Phi_g$ of §1.2. The identification has the following properties.
1. It maps solutions of the HW system (E1)–(E3) of [R24, §2] to solutions, and the 5D Coulomb condition of [R30, §2] to itself. These are local, natural equations.
2. It maps the Nahm-pole conditions at $y=0$ and their reflections at $y=L$ to themselves.
3. It is an isometry up to the factor $|G|$: $\|\pi^*\xi\|^2_{L^2(S^3)}=|G|\,\|\xi\|^2_{L^2(Y)}$, and likewise for the graph norms of $Z$ and for the energy.
4. Hence $X_Y\cong X^G$, $Z_Y\cong Z^G$, and $\mathcal W_Y\cong\mathcal W^G$ for the spaces of [R24, R30]. Every $G$-equivariant operator restricts. In particular $\mathcal L_*$, $\mathcal L(u(s))$ and $D_u$ restrict to the corresponding operators on $Y$.

*Proof.* $\pi$ is a local isometry and $G$ acts by bundle isometries preserving the soldering form, so all local natural expressions are preserved. Fibre integrals over $S^3$ of $G$-invariant densities are $|G|$ times those over $Y$. The operators of [R30, (2.1)] commute with $SO(4)$ [R30, Prop. 4.2(2)], hence with $G$. A $G$-equivariant operator maps $G$-invariant elements to $G$-invariant elements. ∎

**Lemma 2.3 (isotropic fields and the fold).** The isotropic fields $A=aT_i\sigma^i$, $\varphi=bT_i\sigma^i$ are $SO(4)$-invariant [R24, §3], so they descend to every $(Y,\mathfrak s)$. Intrinsically, $A=\nabla^{\rm spin}+(a-\tfrac c2)\theta$ and $\varphi=b\,\theta$. In particular $k_*$, $k_\pm$ and the instanton $u$ descend. The isotropic reduction $\partial_s u+i\partial_y u=\bar u^2-r^{-2}$ [R24, Thm. A] uses only the constant curvature $r^{-2}$, so the fold of $Y\times(0,L)$ is at $L=\pi r$. The energy of $u$ on $Y$ is that of [R24, Thm. C(5)] divided by $|G|$.

*Proof.* The first statement is [R24, §3]: the isotropic fields are built from $\theta$ and the Levi-Civita connection, which are $SO(4)$-invariant. The rest follows from Lemma 2.2. ∎

### 2.2 Which published sectors descend

**Proposition 2.4.**
1. *Left quotients.* For $G=\Gamma_L$, every $SU(2)_L$-invariant field is $G$-invariant. Hence the isotropic class [R24], the $V_4$ class [R25, R49] and the full left-invariant matrix sector $(M,N)$ of [R30, Prop. 3.1] descend to $Y_\Gamma$ verbatim.
2. *General $G$.* A left-invariant field $(M,N)$ descends iff $M,N\in\mathrm{End}(\mathbb R^3)^{G_R}$, where $G_R$ is the image of $G$ in $SO(3)$ under $[g_L,g_R]\mapsto\mathrm{Ad}(g_R)$, acting on the Lie and form indices simultaneously. Isotropic fields $(M,N\propto\mathrm{Id})$ always descend. The $V_4$ sector descends iff $G_R\subset V_4$.
3. *Perturbed categories.* The height functional $h_e$ of [R33] is $G$-invariant iff $ge=e$ for all $g$, which is impossible for $G\ne1$ acting freely. The quadrupole functional $h_C$ of [R32] is $G$-invariant iff $C$ commutes with every $g\in G\subset SO(4)$. For $G=\Gamma_L$ this means:
   * $C$ arbitrary if $\Gamma=\{\pm1\}$;
   * $C$ a traceless Hermitian $2\times2$ matrix if $\Gamma$ is cyclic of order $\ge3$; its eigenvalues then have even multiplicity, so the simple-spectrum hypothesis of [R32] fails;
   * $C=0$ if $\Gamma$ is non-abelian, since the commutant of $\{L_\gamma\}$ is then the right multiplications, and the only symmetric traceless one is $0$.
   
   In all cases no object of the quadrupole or height categories is $G$-invariant (Theorem C(1)).
4. *The three-sphere.* $G$ acts freely on $\mathcal S_{\bar\nu}\cong S(\mathcal K)$, and $\mathcal S_{\bar\nu}/G\cong Y$.

*Proof.* (1) Elements $[\gamma,1]$ act by left translation only. (2) $[g_L,g_R]$ acts on left-invariant fields through $\mathrm{Ad}(g_R)\otimes\mathrm{Ad}(g_R)$ on the (Lie, form) indices. (3) $h_C=\tfrac12\int\sin^4y\langle q,Cq\rangle|\varphi|^2$, and $|\varphi|^2$ is invariant; invariance of $\langle q,Cq\rangle$ under $q\mapsto gq$ is $g^{\sf T}Cg=C$. For cyclic $\Gamma$ of order $\ge3$, the commutant of left multiplication by $e^{2\pi i/p}$ is $\mathrm{End}_{\mathbb C}(\mathbb C^2)$ for the left complex structure. Its real-symmetric traceless elements are the traceless Hermitian matrices, whose real eigenvalues $\lambda,-\lambda$ each have real multiplicity $2$. For non-abelian $\Gamma$ the real span of $\Gamma$ is $\mathbb H$, so the commutant is $\{R_h\}$, and $R_h$ is symmetric iff $h$ is real. Similarly $h_e=\int\sin^4y\cos y\langle e,q\rangle\langle\varphi_i,F_{yi}\rangle$ is invariant iff $ge=e$. (4) By [R31, Lemma 3.1], $SO(4)$ acts on $\mathcal K\cong\mathbb H$ by $w\mapsto g_Lw\bar g_R$, and the stabilizer of $w\ne0$ is the group of isometries fixing $w/|w|\in S^3$. So the action of $G$ on $S(\mathcal K)$ is conjugate to its action on $S^3$, which is free. ∎

### 2.3 Residual symmetry

The isometry group of $Y$ is $N_{O(4)}(G)/G$; see McCullough [18] for a complete list. For $G=\Gamma_L$ the orientation-preserving part is $(N_{SU(2)}(\Gamma)\times SU(2))/\langle(\Gamma\times1),(-1,-1)\rangle$. The normalizer is $\mathrm{Pin}(2)$ for cyclic $\Gamma$ of order $\ge3$, $SU(2)$ for $\Gamma=\{\pm1\}$, $D^*_{8n}$ for $D^*_{4n}$ ($n\ge3$), and $O^*$ for $Q_8$, $T^*$ and $O^*$; for $I^*$ it is $I^*$. These isometries, combined with the gauge lifts of §2.1, act on the problem on $Y$ and fix every isotropic field. The Nahm-pole configuration is irreducible [R30, Rem. 6.1], so the stabilizer in the gauge group is the centre $\pm1$. Orientation-reversing isometries exist only for amphichiral $Y$, for instance $\mathbb{RP}^3$ and $L(5,2)$. By Theorem E(2) there are none whenever $\eta(\mathcal L^Y_*)\ne0$, for example for every $Y_\Gamma$ in the table of Theorem E except $\mathbb{RP}^3$ and $L(13,1)$; $L(13,1)$ is chiral as well, since $1\not\equiv-1\pmod{13}$. Accordingly the reversor $R$ of [R31, Prop. 3.3] descends only in the amphichiral case. Theorem E(2) shows that this is reflected in the spectrum.

### 2.4 Right quotients and flat twists

For $G=\Gamma_R$ the isotropic fields descend through the lift $(q,u)\mapsto(q\gamma^{-1},\pm\gamma u)$. This lift carries the flat structure with holonomy the inclusion $\Gamma\subset SU(2)$. On $S^3$, the gauge transformation $h(q)=q$ maps left-isotropic fields $a\theta_L$ to right-isotropic fields $(a-1)\theta_R$, and $h(\gamma q)=\gamma h(q)$. So on $Y_\Gamma$ the bundles "trivially lifted" and "lifted through the inclusion" are isomorphic as bundles with Nahm data, and they do not give separate sectors. In the Nahm-pole problem, the $SU(2)$-bundle and its identification $\operatorname{ad}P\cong TY$ are fixed up to the spin-structure choice of Lemma 2.1, and flat connections are never objects near $k_*$, where $A$ is close to $\nabla^{\rm spin}$. Flat bundles enter as coefficient systems of the deformation theory (Theorem C(4)).

### 2.5 Seifert fibrations over $\mathbb{RP}^2$ (Proposition A)

*Proof of Proposition A.* ($\Leftarrow$) Let $\Gamma=D^*_{4n}=\langle e^{i\pi/n},j\rangle\subset\mathrm{Pin}(2)=U(1)\cup jU(1)$, with $n\ge1$. Left multiplication by $U(1)$ gives the Hopf fibration $S^3\to U(1)\backslash S^3=S^2$. Since $je^{i\theta}=e^{-i\theta}j$, left multiplication by $\Gamma$ permutes the fibres. The subgroup $\mathbb Z_{2n}=\Gamma\cap U(1)$ preserves each fibre and rotates it freely. The element $j$ induces a free involution of $S^2$: if $jq=e^{i\theta}q$, then $e^{-i\theta}j\ne1$ would fix $q$ under left multiplication, which is impossible. Hence $Y_\Gamma\to S^2/(\mathbb Z/2)=\mathbb{RP}^2$ is a circle bundle, a Seifert fibration without exceptional fibres.

($\Rightarrow$) Let $Y$ be Seifert fibred over $\mathbb{RP}^2(a)$. By [8, §6.3] (see also [15]),
$$\pi_1(Y)\cong\langle v,h\mid vhv^{-1}=h^{-1},\ v^{2a}=h^r\rangle,$$
a metacyclic group of order $4a|r|$. In it, $\langle h\rangle$ is normal cyclic of order $2|r|$, and the quotient is cyclic of even order $2a$, generated by $v$. Among the finite subgroups of $SU(2)$:
* $T^*,O^*,I^*$ have only $1$ and $\{\pm1\}$ as normal cyclic subgroups, with non-cyclic quotients ($T^*$, $A_4$, $O^*$, $S_4$, $I^*$, $A_5$). They are excluded (verify.py §9).
* If $\Gamma=\mathbb Z_p$ is cyclic, then $h=h^{-1}$, so $2|r|=2$ and $p=4a$. Such $Y$ are the lens spaces $L(4a,2a\pm1)$ [17, 32]. By the classification of lens spaces, $L(4a,1)\cong\pm L(4a,2a\pm1)$ forces $2a\pm1\equiv\pm1\pmod{4a}$ (note $(2a\pm1)^2\equiv1$), so $a=1$, $p=4$.
* If $\Gamma=D^*_{4n}$, it has this form with $a=1$, $h=e^{i\pi/n}$, $v=j$.

Within $SU(2)$, subgroups isomorphic to $D^*_{4n}$ are conjugate, so $Y_\Gamma\cong S^3/D^*_{4n}$. For the last sentence of Proposition A: the groups of [8, §6.3] are the explicit $G\subset U(2)\subset SO(4)$ written there, and they act freely. ∎

Since $H^1(Y;\mathbb Z/2)=\mathrm{Hom}(\Gamma^{\rm ab},\mathbb Z/2)$, the numbers of spin structures are as follows:
* $2$ for $L(4,1)$;
* $4$ for $S^3/Q_8$;
* $2$ for $S^3/D^*_{4n}$ with $n$ odd ($\Gamma^{\rm ab}=\mathbb Z/4$);
* $4$ for $S^3/D^*_{4n}$ with $n$ even ($\Gamma^{\rm ab}=(\mathbb Z/2)^2$).

There are $4=|H_1|$ spin$^c$ structures in each case (verify.py §9).

## 3. The fold on $Y$ (Theorem B(3))

**Lemma 3.1.** $\mathcal K^G=0$ for every $G\ne1$ acting freely.

*Proof.* Let $w\in\mathcal K$ be fixed by $g\in G$ with $w\ne0$. By [R31, Lemma 3.1], $g$ fixes the point $w/|w|\in S^3$, so $g=1$ by freeness. As a check, for $G=\Gamma_L$ we have $\mathcal K\otimes\mathbb C\cong V_{1/2}\otimes\mathbb C^2$ as an $SU(2)_L$-module, and $\dim V_{1/2}^\Gamma$ is the coefficient of $t$ in the Molien series of $\Gamma$, which is $0$ (verify.py §8). ∎

*Proof of Theorem B(3).* By Lemma 2.2, $\mathcal L^Y_*$ is the restriction of the self-adjoint operator $\mathcal L_*$ [R30, Prop. 4.2] to the closed reducing subspace $X^G$; the subspace is reducing because $G$ acts unitarily and commutes with $\mathcal L_*$. So $\mathcal L_*^Y$ is self-adjoint with compact resolvent and with the same indicial roots. Its spectrum is contained in that of $\mathcal L_*$, which avoids $(-1,1)\setminus\{0\}$ on the unit sphere [R30, Thm. B(3)]. Finally $\ker\mathcal L^Y_*=(\mathbb R\zeta\oplus\mathcal K)^G=\mathbb R\zeta$ by Lemma 3.1, since $\zeta$ is $SO(4)$-invariant. ∎

**Peter–Weyl on $Y$.** Write the complexified fields on $S^3$ as $\bigoplus_{k,K}V_k\boxtimes V_K\otimes M_{k,K}$, where $V_k$ is the left representation and $V_K$ the $SU(2)_{\rm diag}$ representation. The fields on $Y$ are then $\bigoplus_{k,K}(V_k\boxtimes V_K)^G\otimes M_{k,K}$, with multiplicities
$$d_G(k,K)=\frac1{|G|}\sum_{g}\chi_k(\theta_L)\chi_K(\theta_R),\qquad \chi_k(\theta)=\frac{\sin(2k+1)\theta}{\sin\theta}.\tag{3.1}$$
For $G=\Gamma_L$, $d_G(k,K)=\dim V_k^\Gamma\cdot(2K+1)$. The numbers $\dim V_k^\Gamma$ are read off from the Molien series:
* $\frac{1+t^p}{(1-t^2)(1-t^p)}$ for $\mathbb Z_p$;
* $\frac{1+t^{2n+2}}{(1-t^4)(1-t^{2n})}$ for $D^*_{4n}$;
* $\frac{1+t^{12}}{(1-t^6)(1-t^8)}$, $\frac{1+t^{18}}{(1-t^8)(1-t^{12})}$, $\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}$ for $T^*$, $O^*$, $I^*$.

These are Klein's invariants [33]; verify.py §8 checks them against the class lists.

## 4. Local classification and transversality (Theorem C)

Let $U\subset Z$ be the neighbourhood of [R31, Thm. A], which we may take $SO(4)$-invariant (a ball). Put $U_Y=\{\xi:\pi^*\xi\in U\}$.

*Proof of Theorem C(1)–(2).* Let $\xi$ solve the gauge-fixed HW system on $Y$ with $\xi(s)\in U_Y$ for all $s$. Then $\tilde\xi=\pi^*\xi$ is a $G$-invariant solution on $S^3$ with $\tilde\xi(s)\in U$. By [R31, Thm. A(2)], $\tilde\xi(s)=\xi_c(s)+\Psi(\xi_c(s),\bar\nu)$, with $\xi_c=P\tilde\xi\in\mathbb R\zeta\oplus\mathcal K$. The projection $P$ commutes with $G$, so $\xi_c$ is $G$-invariant, and its $\mathcal K$-component $w$ lies in $\mathcal K^G=0$. Thus $\tilde\xi$ lies on the isotropic line $\{x\zeta+\Psi(x\zeta,\bar\nu)\}$, which is $G$-invariant because $\Psi$ is equivariant [R31, Thm. A(3)]. Its reduced flow is $\dot x=g(x^2,0,\bar\nu)$ [R31, Thm. B]. By [R31, Thm. C(1), Thm. D(1)–(2)] and [R24, Thms. C, D], the solutions on this line are the following: $k_\pm$ and the translates of $u$ for $\bar\nu>0$; $k_*$ for $\bar\nu=0$; nothing for $\bar\nu<0$ (there the line meets no zero of $g$, and every orbit leaves $U$). Conversely these isotropic solutions descend (Lemma 2.3).

The argument is the same for every spin structure, because the deformation spaces coincide (Lemma 2.1). A solution "twisted" by another lift of $G$ is an $\operatorname{ad}P_{\mathfrak s'}$-valued field for a different $\mathfrak s'$. It is covered by the same argument, and its pull-back is again a $G$-invariant element of $U$.

For gauge classes: KW objects in any gauge near $k_*^Y$ are put in the Coulomb slice by the slice theorem, as in [R31, §5], since the Nahm-pole configuration is irreducible. For trajectories, passing to gauge classes is conditional on Hypothesis (G) of [R34, §8], exactly as on $S^3$. If (G) holds on $S^3$, its uniqueness clause makes the gauge transformation $G$-equivariant, so (G) also holds on $Y$. ∎

*Proof of Theorem C(3).* $u$ is $SO(4)$-invariant, so $D_u$ commutes with the unitary $G$-action on $\mathcal W=W^{1,2}(\mathbb R;X)\cap L^2(\mathbb R;Z)$ and on $L^2(\mathbb R;X)$. By Lemma 2.2, $D_u^Y=D_u|_{\mathcal W^G}$. Let $\Pi=|G|^{-1}\sum_g\Phi_g$ be the averaging projection; it commutes with $D_u$. Then:
* $\ker D_u^Y=(\ker D_u)^G$;
* if $f\in L^2(\mathbb R;X)^G$ satisfies $f=D_u\xi$, then $f=\Pi f=D_u\Pi\xi$, so $\operatorname{ran}D_u^Y=\operatorname{ran}D_u\cap L^2(\mathbb R;X)^G$;
* hence $\operatorname{coker}D^Y_u\cong(\operatorname{ran}D_u)^\perp\cap L^2(\mathbb R;X)^G=(\operatorname{coker}D_u)^G$.

So $D_u^Y$ is Fredholm. By [R30, Thm. D], $\ker D_u=\mathbb R\partial_su$, which is $G$-invariant, and $\operatorname{coker}D_u\cong\mathcal K$ $SO(4)$-equivariantly. Lemma 3.1 gives $\operatorname{coker}D_u^Y=0$ and index $1$. The energy formula is Lemma 2.3 together with [R24, Thm. C(5)]. ∎

*Proof of Theorem C(4).* Complexify. $E_\rho=S^3\times_G\rho$, and $(\operatorname{ad}P\otimes E_\rho)$-valued deformations on $Y$ correspond to $(\mathcal W_{\mathbb C}\otimes\rho)^G\cong\mathrm{Hom}_G(\rho^*,\mathcal W_{\mathbb C})$. The operator $D_u\otimes1$ commutes with $G$. The argument of (3), applied to the isotypic decomposition, gives
* $\ker=\mathrm{Hom}_G(\rho^*,\mathbb C\partial_su)$, of dimension $\langle\rho,1\rangle=\delta_{\rho,1}$ for irreducible $\rho$;
* $\operatorname{coker}=\mathrm{Hom}_G(\rho^*,\mathcal K_{\mathbb C})$.

Here $\mathcal K_{\mathbb C}\cong V_{\mathbb C}$ by [R31, Lemma 3.1], and $V_{\mathbb C}$ is self-dual. For $G=\Gamma_L$, left multiplication on $\mathbb H\otimes_{\mathbb R}\mathbb C$ is $Q\oplus Q^*\cong2Q$. For non-abelian $\Gamma$, $Q$ is irreducible ($\langle Q,Q\rangle=1$, verify.py §11), so the only nontrivial twist that sees the obstruction is $\rho=Q$, with $\operatorname{coker}\cong\mathbb C^2$ and index $-2$. For $\Gamma=\mathbb Z_p$ with $p\ge3$, $Q=\chi\oplus\chi^{-1}$ and the index is $\delta_{a,0}-2(\delta_{a,1}+\delta_{a,-1})$ for $\rho=\chi^a$. For $\Gamma=\mathbb Z_2$ the sign twist has index $-4$. Summing $\dim\rho\cdot\operatorname{ind}_\rho$ over irreducibles recovers $-3$, as it must, since the regular representation reassembles $S^3$ (verify.py §8). ∎

**Corollary 4.1 (sector-wise global statements).** For $G=\Gamma_L$, the isotropic sector of $Y_\Gamma$ coincides with that of $S^3$, with energies divided by $|\Gamma|$, and so does the $V_4$ sector. Hence the global uniqueness and compactness of [R46] (every isotropic trajectory for $L>\pi r$ is constant or runs $k_+\to k_-$) and the $V_4$ rigidity of [R49] hold verbatim on $Y_\Gamma$. Together with Theorem C, near the fold the complete gauge-fixed theory on $Y$ is the isotropic theory. We make no global claim outside the symmetric sectors.

## 5. Conley indices, realizations, fixed points and orbits (Theorem D)

*Proof of Theorem D(1).* By §4, the local invariant set on $Y$ lies on the isotropic line, with flow $\dot x=g(x^2,0,\bar\nu)$, $g=\tfrac56x^2-\tfrac43\bar\nu+O_4$ [R31, Thm. B]. For $\bar\nu<0$ the set is empty, so the index is the pointed point. For $\bar\nu=0$ it is $\{0\}$ with $\dot x>0$ on both sides. For $\bar\nu>0$ it is $[x_-,x_+]$, with $\dot x<0$ inside and $\dot x>0$ outside. In both cases $N=[-\varepsilon,\varepsilon]$ (respectively $[x_--\varepsilon,x_++\varepsilon]$) with exit set $E=\{\text{right endpoint}\}$ is an index pair, and $N/E\simeq*$. The PDE flow and the reduced flow have the same index, by [R34, Thm. D] applied to $G$-invariant data.

The local category has objects $k_+$ (reduced index $1$, since $\partial_xg(x_+)=\tfrac53x_+>0$) and $k_-$ (index $0$), and $\mathcal M(k_+,k_-)$ is one point, regular by Theorem C(3). Any framing assigns it a sign. The CJS realization [24], or that of [25], is the cofibre of a degree-$\pm1$ map $S^0\to S^0$ (suitably suspended), hence contractible, as already known for the isotropic category [R46, Cor. E], [R49, Thm. D(4)], [R53, Thm. A(1)]. The spherical reframing ambiguity of [R53] (the class $\eta^2$ on $S^3$) is absent: here the reframings form $\pi_0GL_1(\mathbb S)=\{\pm1\}$. ∎

The equivariant statements rest on the following elementary lemma.

**Lemma 5.1 (fixed points of index pairs).** Let a finite group $G$ act on a flow, and let $(N,E)$ be a $G$-invariant index pair for $S=\operatorname{Inv}N$. Then $(N^G,E^G)$ is an index pair for $S^G=\operatorname{Inv}(N^G)$ in the restricted flow on $\mathrm{Fix}(G)$, and $(N/E)^G=N^G/E^G$.

*Proof.* $\mathrm{Fix}(G)$ is closed and invariant. The defining properties of an index pair (compactness, $S\subset\operatorname{int}(N\setminus E)$, positive invariance of $E$ relative to $N$, $E$ is the exit set) are inherited by intersection with $\mathrm{Fix}(G)$. A point of $N/E$ other than the base point is fixed iff it is the class of a fixed point of $N\setminus E$. ∎

*Proof of Theorem D(2).* Let $\bar\nu<0$. By [R31, Lemma 6.1], in centre coordinates $(x,w)=(x,\rho\hat w)$ with $\rho=|w|>0$, the reduced field is $\dot x=F(x,\rho)$, $\dot\rho=\phi(x,\rho)$, $\dot{\hat w}=0$. Here $F$ and $\phi$ do not depend on $\hat w\in S^3$. Near $\mathcal S_{\bar\nu}=\{x=0,\rho=\rho_0\}$ the flow is therefore the product of a planar flow, with a hyperbolic saddle at $(0,\rho_0)$ (eigenvalues $\pm\sqrt{10|\bar\nu|/3}(1+O(\bar\nu))$ [R31, Thm. C]), and the identity on $S^3=S(\mathcal K)$. $G$ acts only on the second factor, by its defining action (Lemma 3.1).

Take a planar box index pair $(b,e)$ for the saddle, with $e$ the two unstable edges, so $b/e\simeq S^1$ with trivial action. Then $(b\times S^3,e\times S^3)$ is a $G$-invariant index pair, and $N/E=(b/e)\wedge S^3_+=S^1\wedge S(V)_+$. By Lemma 5.1 its fixed set is $S^1\wedge(\emptyset_+)=*$, in agreement with D(1).

For $\bar\nu>0$, $k_\pm$ are hyperbolic. Their unstable spaces in $\mathbb R\zeta\oplus\mathcal K$ are $\mathbb R\zeta$ (for $k_+$, trivial action) and $\mathcal K$ (for $k_-$, action $V$), by the eigenvalues $\tfrac53x_\pm$ and $-\tfrac54x_\pm$ [R30, Thm. C]. The equivariant index of a hyperbolic rest point is the representation sphere of its unstable space [22, 23]. The fixed sets $S^1$ and $(S^V)^G=S^0$ are the indices of $k_+$ and $k_-$ on $Y$. By equivariant continuation [22, 23], the index for $\bar\nu>0$ is also $S^1\wedge S(V)_+$. This is consistent with the cofibre sequence $S^V\to S^1\wedge S(V)_+\to S^1$, the suspension of $S(V)_+\to S^0\to S^V$. ∎

*Proof of Theorem D(3).* For $\bar\nu<0$, $G$ acts freely on $b\times S^3$, and the product flow descends to $b\times(S^3/G)=b\times Y$, using Proposition 2.4(4). Hence $(N/G,E/G)$ is an index pair for $\mathcal S_{\bar\nu}/G\cong Y$, with $N/E/G=S^1\wedge Y_+$.

$Y$ is a closed orientable 3-manifold, hence parallelizable, so $\Sigma^\infty Y_+$ is Spanier–Whitehead self-dual up to a shift by $3$ (Atiyah duality [13]). Under this duality the Umkehr map $S^3\to\Sigma^\infty Y_+$ dualizes the collapse $Y_+\to S^0$, which is split; so the top cell splits off stably. Since $H_2(Y)=0$ for a rational homology sphere, the remaining summand of $\Sigma^\infty Y$ is connective with homology $H_1(Y)$ in degree $1$ only, hence equivalent to $\Sigma M(H_1Y)$. Thus $\Sigma^\infty\Sigma(Y_+)\simeq S^1\vee\Sigma^2M(H_1Y)\vee S^4$. On a Moore spectrum, $\mathrm{Sq}^1$ is the mod-2 Bockstein; it is nonzero exactly on cyclic summands $\mathbb Z/2m$ with $m$ odd. $\mathrm{Sq}^2=0$ for degree reasons in each wedge summand. The values are listed in Table 5.1. ∎

**Table 5.1** (verify.py §9).

| $Y$ | $H_1(Y)$ | spin str. | $\mathrm{rk}\,\mathrm{Sq}^1$ on $\Sigma(Y_+)$ | local HW index on $Y$ | $S^3$ index (fixed/orbit) |
|---|---|---|---|---|---|
| $L(p,1)$, $p$ odd | $\mathbb Z/p$ | 1 | 0 | $*$ | $S^1\vee S^4$; $*$ / $\Sigma Y_+$ |
| $L(p,1)$, $p\equiv2\ (4)$ | $\mathbb Z/p$ | 2 | 1 | $*$ | same |
| $L(p,1)$, $4\mid p$ | $\mathbb Z/p$ | 2 | 0 | $*$ | same |
| $S^3/D^*_{4n}$, $n$ odd | $\mathbb Z/4$ | 2 | 0 | $*$ | same |
| $S^3/D^*_{4n}$, $n$ even | $(\mathbb Z/2)^2$ | 4 | 2 | $*$ | same |
| $S^3/T^*$, $S^3/O^*$, $S^3/I^*$ | $\mathbb Z/3$, $\mathbb Z/2$, $0$ | 1, 2, 1 | 0, 1, 0 | $*$ | same |

*Remarks.* (i) The orbit spectrum lies in the class $\mathcal W$ of [R52] (wedges of spheres and Moore spectra). (ii) For $\Gamma=\{\pm1\}$, the quotient of the antipodally symmetric quadrupole picture is the Morse theory of $\mathbb{RP}^3$; compare the $\mathbb{RP}^3$ argument in [R32]. (iii) If $G$ is a $p$-group, the Smith inequality $\dim\tilde H_*(X^G;\mathbb F_p)\le\dim\tilde H_*(X;\mathbb F_p)$ reads $0\le2$, and the Euler-characteristic congruence $\tilde\chi(X^G)\equiv\tilde\chi(X)\pmod p$ reads $0\equiv0$. The identification of the theory on a quotient with fixed points of the theory on a cover parallels the use of fixed points of Seiberg–Witten Floer spectra of covers by Lidman–Manolescu [11].

## 6. Spectral asymmetry of the fold Hessian (Theorem E)

We work on the unit sphere and the interval $(0,\pi)$. Eigenvalues scale as $r^{-1}$, so $\eta(0)$ does not depend on $r$.

### 6.1 Block reduction

$J$, $V_1$ and $B=JV_1$ commute with $G$, with the fibre rotations and with $SU(2)_L$. $\mathcal D$ commutes with $SU(2)_L$ and $SU(2)_{\rm diag}$ (verify.py §2). Moreover $\{J,\mathcal D\}=\{V_1,\mathcal D\}=0$, $\{J,V_1\}=0$, $[B,\mathcal D]=0$, $\{B,J\}=\{B,V_1\}=0$ and $V_1=-JB$ [R30, Lemma 4.1], verify.py §§1, 3.

**Proposition 6.1.** Let $E_\mu^\sigma\subset X_Y$ (fibre-and-$S^3$ part) be the joint eigenspace $\mathcal D=\mu$, $B=\sigma$. For $\sigma>0$, the space $L^2(0,\pi;E^\sigma_\mu\oplus JE^\sigma_\mu)$ reduces $\mathcal L_*^Y$. On it, writing elements as $a+Jb$, the operator is
$$\mathcal L_*(a+Jb)=(\mu a+T^*b)+J(Ta-\mu b),\qquad T=\partial_y-\sigma\cot y,\ T^*=-\partial_y-\sigma\cot y .$$
Its spectrum consists of
* the pairs $\pm\sqrt{\mu^2+\lambda}$, $\lambda\in\operatorname{spec}(T^*T)\setminus\{0\}$, with equal multiplicities;
* the eigenvalue $\mu$, with eigenfunctions $\sin^\sigma(y)v$, $v\in E_\mu^\sigma$.

These blocks, over all $\mu$ and all $\sigma\in\{1,2\}$, exhaust $X_Y$.

*Proof.* With $V_1=-JB$ and $BJ=-JB$ one computes $\mathcal L_*a=J(a'-\sigma\cot a)+\mu a$ and $\mathcal L_*(Jb)=-b'-\sigma\cot b-\mu Jb$ (verify.py §3 checks the identities and the eigenfunctions in the sector $j=\tfrac12$). Every $E^\tau_\nu$ with $\tau<0$ equals $JE^{-\tau}_{-\nu}$, so the blocks exhaust the space.

On the domain of $\mathcal L_*$, whose elements are $O(\min(y,\pi-y)^{1/2})$ [R30, Prop. 4.2(4)]:
* $\ker T=\mathbb R\sin^\sigma y$, since $\sigma\ge1$;
* $\ker T^*=0$, since $\sin^{-\sigma}\notin L^2$.

The block squares to $\mu^2+\mathrm{diag}(T^*T,TT^*)$ and has compact resolvent. For an eigenvector $a$ of $T^*T$ with eigenvalue $\lambda>0$, the span of $(a,0)$ and $(0,Ta)$ is invariant, with matrix $\begin{pmatrix}\mu&\lambda\\1&-\mu\end{pmatrix}$ and eigenvalues $\pm\sqrt{\mu^2+\lambda}$. The remaining vectors are $\ker T\oplus\ker T^*$. ∎

For $\mu=0$ the same computation gives symmetric spectrum and zero modes. Each block has the Pöschl–Teller spectrum [28] $\lambda_k=(\nu_\sigma+k)^2-\sigma^2\ge k^2$, $\nu_\sigma\ge1$, as used in [R30, §4]. In sector $j$ the eigenvalues of $\mathcal D$ satisfy $|\mu|\ge2j-3$ [R30, Lemma 4.4], and the sector has dimension $\le24(2j+1)^2$. Hence $\#\{|\lambda|\le\Lambda\}=O(\Lambda^4)$, and $\eta(\mathcal L_*^Y;s)$ converges absolutely for $\operatorname{Re}s>4$. The pairs cancel, and we obtain:

**Corollary 6.2.** $\eta(\mathcal L_*^Y;s)=\eta(\mathcal D^+_Y;s)$, where $\mathcal D^+=\mathcal D|_{\ker(B-1)\oplus\ker(B-2)}$ and zero modes are omitted.

### 6.2 The spectrum of $\mathcal D^+$ by isospin channels

Let $R_k$ be the infinitesimal rotations of the form and Lie indices, so that $[R_i,R_j]=R_k$, and let $E_i=\tfrac12e_i$. Then $T_i=E_i+R_i$ generate $SU(2)_{\rm diag}$, and $[\mathcal D,T_i]=0$, because $N_i$ is a vector operator: $[R_k,N_i]=\epsilon_{kil}N_l$ (verify.py §2).

**Lemma 6.3 (fibre data; exact, verify.py §2).** Under the fibre rotations, $\ker(B-2)\cong V_0\oplus V_1$ and $\ker(B-1)\cong V_1\oplus V_2$, each summand occurring once. On the summand $V_f$ inside $\ker(B-\sigma)$, $V_0$ acts as the scalar $v_{\sigma,f}$ and $P_fN_iP_f=\kappa_{\sigma,f}P_fR_iP_f$, with
$$(v,\kappa)_{2,0}=(0,0),\quad(v,\kappa)_{2,1}=(2,-1),\quad(v,\kappa)_{1,1}=(1,-\tfrac12),\quad(v,\kappa)_{1,2}=(-3,\tfrac12).$$

Proportionality of $P_fN_iP_f$ and $P_fR_iP_f$ is forced by Schur's lemma (the projection theorem [34]), since $\mathrm{Hom}_{SO(3)}(\mathbb R^3\otimes V_f,V_f)$ is one-dimensional for $f\ge1$ and zero for $f=0$; the constants are computed.

**Proposition 6.4.** On $V_j\otimes\ker(B-\sigma)$ (the right factor of sector $j$), decompose by total isospin $K$. The $K$-channel has an orthonormal basis indexed by the $f$ with $|j-f|\le K\le j+f$, and the diagonal entry of $\mathcal D^+$ for $f$ is
$$d_{\sigma,f}(j,K)=v_{\sigma,f}+\kappa_{\sigma,f}\,[\,j(j+1)+f(f+1)-K(K+1)\,].$$
Consequently:
1. Two-dimensional channels have trace $0$ for all $j$, so their eigenvalues are $\pm\lambda$ and they contribute nothing to $\eta$.
2. The one-dimensional channels contribute the following unpaired eigenvalues (multiplicity $2K+1$ in the right factor):
   * $\sigma=1$, $K=j+2$: $-(2j+3)$;
   * $\sigma=1$, $K=j-2$ ($j\ge2$): $2j-1$;
   * $\sigma=2$, $K=j+1$: $2j+2$;
   * $\sigma=2$, $K=j-1$ ($j\ge1$): $-2j$;
   * the exceptional channels: $(j,K)=(0,1)$, $\sigma=1$: $+1$; $(1,0)$, $\sigma=1$: $-1$; and $(\tfrac12,\tfrac12)$, $\sigma=1$, and $(0,0)$, $\sigma=2$, both with eigenvalue $0$.

*Proof.* $P_f\mathcal D^+P_f=v_{\sigma,f}+\kappa_{\sigma,f}\sum_iR_i\otimes e_i$ by Lemma 6.3, and $\sum_iR_ie_i=2\sum_iR_iE_i=-\sum T_i^2+\sum R_i^2+\sum E_i^2$ acts on the $K$-channel by $j(j+1)+f(f+1)-K(K+1)$. By Schur's lemma, $\mathcal D^+$ acts on each channel's multiplicity space, which has an orthonormal basis given by the $f$-components; the diagonal entries are the $d_{\sigma,f}$. The trace identities are polynomial identities in $j$ (verify.py §4):
* $d_{2,0}(j,j)+d_{2,1}(j,j)=0$;
* $d_{1,1}(j,K)+d_{1,2}(j,K)=0$ for $K=j,j\pm1$.

The list of one-dimensional channels follows from the triangle conditions, and verify.py §4 checks it for $2j\le12$. As an independent exact check, $\operatorname{tr}((\mathcal D^+_j)^k)$ for $k=1,3,5$ and $2j\le5$, computed in the integer spin model over $\mathbb Q(i)$, agrees with the prediction (verify.py §5). The predicted values are consistent with the numerical closed form of [R30, Rem. 4.5]. ∎

### 6.3 The Dirichlet series and its value at $0$

Combine Corollary 6.2, Proposition 6.4 and (3.1), reindexing $K=j-2$ and $K=j-1$:
$$\eta(\mathcal L^Y_*;s)=\sum_{j\in\frac12\mathbb Z_{\ge0}}\Big([d_G(j+2,j)-d_G(j,j+2)](2j+3)^{-s}+[d_G(j,j+1)-d_G(j+1,j)](2j+2)^{-s}\Big)+d_G(0,1)-d_G(1,0).\tag{6.1}$$
This is antisymmetric under exchanging the roles of left and right. Write $\eta=|G|^{-1}\sum_g\eta_g$, where $\eta_g$ is (6.1) with $d_G$ replaced by $\chi_k(\theta_L)\chi_K(\theta_R)$.

* For $g=1$ every coefficient vanishes identically, since $(2j+5)(2j+1)-(2j+1)(2j+5)=0$, and similarly for the other terms. So $\eta(\mathcal L_*;s)\equiv0$ on $S^3$ (verify.py §6). This agrees with the reversor of [R31], which anticommutes with $\mathcal L_*$.
* For $g=[-1,1]$, $\chi_k(\pi)=(-1)^{2k}(2k+1)$ and the coefficients again vanish.
* For other $g$, freeness means $\cos\theta_L\ne\cos\theta_R$, so $e^{i(\theta_L\pm\theta_R)}\ne1$. The coefficients of $\eta_g$ are then finite sums of $P(n)\omega^n$, where $P$ is a polynomial and $\omega\ne1$ is a root of unity; for $\theta_R\in\{0,\pi\}$, $\omega=e^{\pm i\theta_L}$.

**Lemma 6.5.** For a root of unity $\omega\ne1$ of order $q$ and $k\ge0$, the series $\sum_{n\ge1}n^{k-s}\omega^n=q^{k-s}\sum_{a=1}^q\omega^a\zeta(s-k,a/q)$ is entire. Its value at $s=0$, $-\tfrac{q^k}{k+1}\sum_a\omega^aB_{k+1}(a/q)$, equals the Abel sum $\lim_{x\to1^-}\sum n^k\omega^nx^n$.

This is the classical evaluation of $\mathrm{Li}_{-k}(\omega)$; see [26, Ch. 12]. verify.py §7 checks it exactly for $q\le8$, $k\le2$.

**Proposition 6.6.** For $g\ne1$, $[-1,1]$, the value $\eta_g(0)$ is the Abel sum of (6.1). With $u=e^{i\theta_L}$ and $v=e^{i\theta_R}$ it is
$$F_2=\frac{(u+v)(uv+1)(u^2v^2+u^2-3uv+v^2+1)}{uv(u-v)(uv-1)}=\frac{(\cos\theta_L+\cos\theta_R)(4\cos\theta_L\cos\theta_R-3)}{\cos\theta_L-\cos\theta_R}.$$

*Proof.* Write $\chi_k\chi_K$ as a combination of $\cos$ of linear forms in $(2k+1)\theta_L,(2K+1)\theta_R$, and sum the geometric series in $x$. At $x=1$ the denominators are $1-uv^{\pm1}\ne0$. The resulting rational-function identity, including the constant term $\chi_1(\theta_R)-\chi_1(\theta_L)$, is verified symbolically in verify.py §7. When $\sin\theta_R=0$ the characters are Laurent polynomials, and the identity extends by continuity in the rational function. ∎

*Proof of Theorem E.* Part (1) is §6.1 together with Lemma 6.5. For (2): $\eta(0)=|G|^{-1}\sum_{g\ne1}F_2(g)$, where the term for $[-1,1]$ is $0$, consistently with $F_2(\pi,0)=0$. Put $\phi_1=\theta_L-\theta_R$ and $\phi_2=\theta_L+\theta_R$. Then
$$\cos\theta_L+\cos\theta_R=2\cos\tfrac{\phi_1}2\cos\tfrac{\phi_2}2,\qquad\cos\theta_L-\cos\theta_R=-2\sin\tfrac{\phi_1}2\sin\tfrac{\phi_2}2,\qquad4\cos\theta_L\cos\theta_R=2\cos\phi_1+2\cos\phi_2=\operatorname{tr}_{\mathbb R^4}g .$$
This gives the cot form (verify.py §7). With
$$\eta_\alpha(Y):=-\frac1{|G|}\sum_{g\ne1}\chi_\alpha(g)\cot\tfrac{\phi_1}2\cot\tfrac{\phi_2}2$$
(the APS formula for the odd signature operator twisted by $\alpha$ [12, Prop. 2.12], up to orientation convention), $\eta_{\rm sig}=\eta_1$ and $\rho_V=\eta_V-4\eta_{\rm sig}$, we get $\eta(\mathcal L_*^Y)=\eta_V-3\eta_{\rm sig}=\rho_V+\eta_{\rm sig}$.

Antisymmetry: $Y\mapsto-Y$ is realized by conjugating $G$ with $q\mapsto\bar q$, which exchanges $\theta_L$ and $\theta_R$, and $F_2$ is antisymmetric. If $Y$ has an orientation-reversing isometry, it lifts to some $\tau\in O(4)\setminus SO(4)$ normalizing $G$. The multiset $\{(\theta_L,\theta_R)\}$ is then swap-invariant, so the sum vanishes. verify.py §6 checks this exactly for $L(5,2)$, $L(10,3)$, $L(13,5)$ and $L(17,4)$, and the sign change for $L(7,2)/L(7,3)$, $L(8,3)/L(8,5)$ and $L(12,5)/L(12,7)$.

For (3), $\theta_R=0$ and $\phi_1=\phi_2=\theta$. Then $-\cot^2\tfrac\theta2(\operatorname{tr}g-4)=4(1+\cos\theta)$, and $\sum_{\gamma\in\Gamma}2\cos\theta_\gamma=|\Gamma|\langle Q,1\rangle=0$ for $\Gamma\ne1$, so
$$\rho_V=\frac4{|\Gamma|}\big((|\Gamma|-1)+\textstyle\sum_{\gamma\ne1}\cos\theta_\gamma\big)=4-\frac8{|\Gamma|}.$$
The cot$^2$ sums are classical:
* $\sum_{k=1}^{p-1}\cot^2(\pi k/p)=(p-1)(p-2)/3$;
* for $D^*_{4n}$: $2n-1$ elements with $\theta=\pi k/n$, and $2n$ elements with $\theta=\pi/2$;
* for $T^*,O^*,I^*$: the class lists in verify.py §8.

They give the table. Independently, verify.py §6 evaluates (6.1) exactly through Hurwitz zeta values at $0,-1$, with $d_G$ taken from the Molien series, for $2\le p\le24$, $1\le n\le10$ and $T^*,O^*,I^*$; for 16 lens spaces $L(p,q)$ it uses exact weight counts. The results agree with the closed forms (verify.py §12, 40 digits). Twisting by $\rho$ multiplies $d_G$ by $\chi_\rho$, which gives the last statement. ∎

### 6.4 Remarks on the invariant

* The HW fold Hessian thus has an explicit spectral asymmetry on every chiral spherical space form, even though its spectrum is symmetric on $S^3$. The asymmetry is $\eta_{\rm sig}$ plus the $\rho$-invariant of the holonomy representation. It does not depend on the spin structure.
* At $k_\pm$, the isotropic zero mode moves to $\pm\tfrac53|x_\pm|$, and by Theorem C the relative grading of $(k_+,k_-)$ on $Y$ is the spectral flow $1$. In the $\rho$-twisted theory it is $\delta_{\rho,1}-\langle\rho,V_{\mathbb C}\rangle$. We do not claim continuity of $\eta(0)$ along the family $\mathcal L(k_\pm)$ for this singular operator.
* Baraglia–Hekmati compute $\delta$ through $\eta_{\rm dir}$ and $\eta_{\rm sig}$, using the adiabatic connection of [9] where the Levi-Civita connection is not adapted to the fibration [8]. For spherical $Y$ they use the round metric [8, §6.3], as we do. The HW fold analysis needs constant curvature, because the isotropic sector requires it, so no adiabatic deformation is available on the non-spherical Seifert manifolds over $\mathbb{RP}^2$.

## 7. Comparison with Seiberg–Witten and instanton theory

**SW side.** Every spherical $Y$ has positive scalar curvature, so $SWF(Y,\mathfrak s)$ is a (formally desuspended) sphere for each spin$^c$ structure [10]. Over $\mathbb{RP}^2$ this is part of [8, Thm. 1.1]: $SWF(Y,\mathfrak s)=\Sigma^{\delta(Y,\mathfrak s)\mathbb C}S^0$. For $-Y_\Gamma$ with $\Gamma=D^*_{4n}$ (the link of the $D_{n+2}$ singularity, i.e. $S(n)$ in [8]), the four $\delta$-invariants are $\{\tfrac{n+2}8,\tfrac{n-2}8,0,0\}$ [8]. verify.py §10 recomputes $d=2\delta$ as $\max(c^2+\mathrm{rk})/4$ over characteristic vectors of the $D_{n+2}$ lattice [14], for $n\le5$, and for $L(4,3)$ from $A_3$.

**Precise differences** for the prism manifolds $S^3/D^*_{4n}$ (and analogously for all spherical $Y$).

1. *Labels.* SW is graded by the $|H_1(Y)|=4$ spin$^c$ structures. The local HW theory is graded by spin structures, $2$ or $4$ of them (Lemma 2.1), and all copies are canonically isomorphic.
2. *Rank.* $\sum_{\mathfrak s}\operatorname{rk}\tilde H(SWF(Y,\mathfrak s))=4$. The local HW homotopy type near the fold is contractible (Theorem D(1)), of rank $0$ for each spin structure.
3. *Cover versus quotient.* $SWF(S^3)=S^0$ has rank $1$, while the local HW type on $S^3$ is $S^1\vee S^4$, of rank $2$. The HW type of $Y$ is the $G$-fixed set of the $S^3$-type, a point, not its orbit space $\Sigma(Y_+)$ (Theorem D).
4. *Torsion.* SW sees $H_1(Y)$ only through its labels. The local HW type sees no torsion. $H_1(Y)$ and $\mathrm{Sq}^1$ appear only in the orbit index (Table 5.1).
5. *Gradings.* $\delta$ involves the spin$^c$ Dirac eta invariants, $\eta_{\rm sig}$, and for trivial fibre holonomy the $\mathrm{pin}^c$ term $\pm\tfrac12$ of the base [8, Thms. 1.2–1.3]. The HW relative grading of $(k_+,k_-)$ is $1$ on $Y$, against $-3$ on $S^3$. The HW fold Hessian has $\eta=\rho_V+\eta_{\rm sig}$, which does not depend on the spin structure and involves no $\mathrm{pin}^c$ term. For $-Y_\Gamma$, $\Gamma=D^*_{4n}$, it equals $(2n^2-24n+13)/(6n)$: $-\tfrac94,-\tfrac{41}{18},-\tfrac{17}8,-\tfrac{19}{10}$ for $n=2,3,4,5$.

**Instanton side.** The generators of Floer's instanton complex [29] are flat $SU(2)$-connections, $\mathrm{Hom}(\Gamma,SU(2))/\mathrm{conj}$. For $S^3/Q_8$ these are the four central ones and the inclusion; for $S^3/I^*$ they include the two irreducible representations of [31]. The inclusion $\iota:\Gamma\subset SU(2)$ is exactly the twist $Q$ of Theorem C(4) that carries the $S^3$-obstruction. So the four obstruction modes of [R30], invisible in the untwisted theory on $Y$, live in the deformation complex twisted by the flat connection $\theta_\iota$. In the Nahm-pole problem, flat connections are never objects near the fold. We draw no further conclusion; whether a relation such as "twisted HW at the fold equals instanton data at $\theta_\iota$" holds is open.

## 8. Status of the claims

**Proved here.**
* Proposition A (given the presentation of [8, §6.3] and the lens-space fibrations of [17]).
* Theorem B and Propositions 2.4, Lemmas 2.1–2.3, 3.1.
* Theorem C(1)–(4) for the gauge-fixed system; Corollary 4.1.
* Theorem D(2)–(3); Theorem D(1) as an immediate consequence of Theorem C(3) (its contractibility statement is recalled, §1.4).
* Theorem E, with Proposition 6.1, Corollary 6.2, Lemma 6.3 (finite exact computation), Propositions 6.4 and 6.6.

**Imported.**
* From [R24, R30, R31, R34]: the centre-manifold theorem with $SO(4)$-equivariance, the classification on $S^3$, the structure of $\mathcal L_*$ and of $D_u$ (index $-3$, equivariant cokernel $\mathcal K$), and isolation.
* From [R46, R49]: the global sector statements; from [R46, Cor. E], [R49, Thm. D(4)], [R53, Thm. A(1)]: contractibility of the isotropic category for every coherent framing.
* From [R32, Thm. A]: the identification of the free $SU(2)_L$-action on $\mathcal K$ as the obstruction to transversality on $S^3$.
* Haragus–Iooss [20], via those papers.
* Conley index theory, its equivariant version and continuation [21–23].
* Atiyah duality [13]; Ozsváth–Szabó's plumbing formula [14] (only for the comparison); the presentation of [8, §6.3]; Geiges–Lange [17] and Bredon–Wood [32]; Klein invariants [33]; the polylogarithm evaluation [26]; the Pöschl–Teller spectra [28].

**Conditional.**
* Gauge-class statements for trajectories: on Hypothesis (G) of [R34], as on $S^3$.

**Numerical only.**
* The [N] checks of verify.py (agreement of cot sums with exact Hurwitz values; class lists). They are not used in proofs.

**Not claimed.**
* Global (away from the fold) classification on $Y$ outside the symmetric sectors.
* The construction of an HW Floer theory or of Floer homotopy types beyond the local Conley index.
* Continuity of $\eta(0)$ along $\mathcal L(k_\pm)$.
* Any statement for non-spherical Seifert manifolds over $\mathbb{RP}^2$; the fold analysis requires constant curvature.
* A relation between twisted HW data and instanton Floer homology.

## 9. Verification

verify.py (standard library and SymPy; it runs in about 30 s) performs 74 checks and reports FALLOS = 0. The checks are tagged:
* [K] (9): known facts or imported data, recomputed where possible;
* [C] (45): exact finite computations;
* [I] (15): symbolic identities;
* [N] (5): 40-digit floating-point cross-checks.

The checks cover:
* the operator data of [R30];
* the fibre rotations and the projection constants (Lemma 6.3);
* the block reduction and its eigenfunctions;
* the channel formulas and the exact odd traces;
* the exact Hurwitz evaluation of (6.1) for all families in Theorem E, including amphichiral vanishing and orientation reversal;
* the identity for $F_2$, and Abel versus Hurwitz values;
* the vanishing $\mathcal K^G=0$ and the twisted indices;
* abelianizations, spin structures, $\mathrm{Sq}^1$ ranks, and the group-theoretic part of Proposition A (via permutation groups);
* the $D_{n+2}$-lattice $d$-invariants.

verify.mpl (21 checks) is a Maple companion mirroring the exact number-theoretic and representation-theoretic parts (the Dirichlet coefficients, the Hurwitz values, the closed forms, $\rho_V=4-8/|\Gamma|$, the kernel $F_2$ and the abelianizations). It was executed in Maple: 21 checks, FALLOS = 0 (output in verify_mpl_output.txt). The analytic inputs (centre manifold, Fredholm theory, isolation) are not machine-checked; they are the imported results listed in §8.

## References

1. M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.
2. L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.
3. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
4. E. Witten, *Khovanov homology and gauge theory*, in: Proceedings of the Freedman Fest, Geom. Topol. Monogr. 18 (2012), 291–308; arXiv:1108.3103.
5. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014), 171–226; arXiv:1311.3167.
6. S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, arXiv:1510.07706.
7. S. He, *A gluing theorem for the Kapustin–Witten equations with a Nahm pole*, arXiv:1707.06182.
8. D. Baraglia, P. Hekmati, *Floer homotopy type and eta invariants of Seifert 3-manifolds fibering over $\mathbb{RP}^2$*, arXiv:2604.19195.
9. T. Mrowka, P. Ozsváth, B. Yu, *Seiberg–Witten monopoles on Seifert fibered spaces*, Comm. Anal. Geom. 5 (1997), 685–791.
10. C. Manolescu, *Seiberg–Witten–Floer stable homotopy type of three-manifolds with $b_1=0$*, Geom. Topol. 7 (2003), 889–932.
11. T. Lidman, C. Manolescu, *Floer homology and covering spaces*, Geom. Topol. 22 (2018), 2817–2838.
12. M. F. Atiyah, V. K. Patodi, I. M. Singer, *Spectral asymmetry and Riemannian geometry. II*, Math. Proc. Cambridge Philos. Soc. 78 (1975), 405–432.
13. M. F. Atiyah, *Thom complexes*, Proc. London Math. Soc. (3) 11 (1961), 291–310.
14. P. Ozsváth, Z. Szabó, *On the Floer homology of plumbed three-manifolds*, Geom. Topol. 7 (2003), 185–224.
15. P. Orlik, *Seifert Manifolds*, Lecture Notes in Math. 291, Springer, 1972.
16. P. Scott, *The geometries of 3-manifolds*, Bull. London Math. Soc. 15 (1983), 401–487.
17. H. Geiges, C. Lange, *Seifert fibrations of lens spaces*, Abh. Math. Semin. Univ. Hambg. 88 (2018), 1–22.
18. D. McCullough, *Isometries of elliptic 3-manifolds*, J. London Math. Soc. (2) 65 (2002), 167–182.
19. J. A. Wolf, *Spaces of Constant Curvature*, 6th ed., AMS Chelsea, 2011.
20. M. Haragus, G. Iooss, *Local Bifurcations, Center Manifolds, and Normal Forms in Infinite-Dimensional Dynamical Systems*, Springer/EDP Sciences, 2011.
21. C. Conley, *Isolated Invariant Sets and the Morse Index*, CBMS 38, AMS, 1978.
22. A. Floer, *A refinement of the Conley index and an application to the stability of hyperbolic invariant sets*, Ergodic Theory Dynam. Systems 7 (1987), 93–103.
23. T. Bartsch, *Topological Methods for Variational Problems with Symmetries*, Lecture Notes in Math. 1560, Springer, 1993.
24. R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.
25. M. Abouzaid, A. J. Blumberg, *Arnold conjecture and Morava K-theory*, arXiv:2103.01507.
26. T. M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976, Ch. 12.
27. T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1976.
28. G. Pöschl, E. Teller, *Bemerkungen zur Quantenmechanik des anharmonischen Oszillators*, Z. Phys. 83 (1933), 143–151.
29. A. Floer, *An instanton-invariant for 3-manifolds*, Comm. Math. Phys. 118 (1988), 215–240.
30. P. B. Kronheimer, T. S. Mrowka, *Monopoles and Three-Manifolds*, Cambridge Univ. Press, 2007.
31. R. Fintushel, R. J. Stern, *Instanton homology of Seifert fibred homology three spheres*, Proc. London Math. Soc. (3) 61 (1990), 109–137.
32. G. E. Bredon, J. W. Wood, *Non-orientable surfaces in orientable 3-manifolds*, Invent. Math. 7 (1969), 83–110.
33. T. A. Springer, *Invariant Theory*, Lecture Notes in Math. 585, Springer, 1977.
34. A. R. Edmonds, *Angular Momentum in Quantum Mechanics*, Princeton Univ. Press, 1957.

rStation papers (cited as [R$NN$]):

* [R24] rStation math_24, https://rstation.ai/problems/math/papers/24/v2
* [R25] rStation math_25, https://rstation.ai/problems/math/papers/25/v1
* [R30] rStation math_30, https://rstation.ai/problems/math/papers/30/v1
* [R31] rStation math_31, https://rstation.ai/problems/math/papers/31/v1
* [R32] rStation math_32, https://rstation.ai/problems/math/papers/32/v1
* [R33] rStation math_33, https://rstation.ai/problems/math/papers/33/v1
* [R34] rStation math_34, https://rstation.ai/problems/math/papers/34/v1
* [R46] rStation math_46, https://rstation.ai/problems/math/papers/46/v1
* [R49] rStation math_49, https://rstation.ai/problems/math/papers/49/v1
* [R52] rStation math_52, https://rstation.ai/problems/math/papers/52/v1
* [R53] rStation math_53, https://rstation.ai/problems/math/papers/53/v1

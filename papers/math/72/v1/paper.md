# A canonical absolute grading for Kapustin–Witten solutions with Nahm poles on spherical space forms: finite Nahm-pole gauge groups, a spectrally rigid Levi-Civita reference class, and the rational gradings ½(ρ_V+η_sig)±½ of the Anderson–Henningson objects

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**
A framed flow category with one object and no morphisms realizes to $\Sigma^d\mathbb S$, so realizing it inside Haydys–Witten (HW) theory requires an absolute grading $d$; for Nahm-pole problems only relative indices were canonical. We construct a canonical absolute grading for Kapustin–Witten (KW) configurations on $Y\times(0,L)$ with Nahm poles at both ends, where $Y=G\backslash S^3_r$ is a spherical space form ($G=1$ allowed).

(A) Gauge transformations preserving the Nahm poles are $\pm1$ on the boundary. Their component group is an extension of $(\mathbb Z/2)^2$ by the stable cohomotopy group $\pi^2_s(Y)$, finite of order $8|H_1(Y)|$ exactly when $b_1(Y)=0$. Hence loop spectral flow vanishes and relative gradings are $\mathbb Z$-valued, not reduced mod $8$ as in instanton Floer theory.

(B) Configurations with the Levi-Civita connection and Higgs field proportional to the soldering form have complete gauge-fixed Hessians with kernels of equal dimension, no mutual spectral flow, and $\eta=\rho_V(Y)+\eta_{\rm sig}(Y)$, for every profile and every $L$.

(C) $\mathrm{gr}(x)=\tfrac12\eta(\mathcal L_{\rm ref})+\mathrm{sf}_{1/2}(\mathcal L_{\rm ref}\to\mathcal L_x)$ is independent of reference, path, gauge and spin structure, and $\operatorname{ind}D_u=\mathrm{gr}(x_-)-\mathrm{gr}(x_+)$ for every trajectory with nondegenerate ends. Its spectral-flow term $d$ is a canonical integer grading. Near the fold, the Anderson–Henningson objects have $\mathrm{gr}(k_\pm)=\tfrac12(\rho_V+\eta_{\rm sig})\pm\tfrac12$ on $Y\ne S^3$ and $\mp\tfrac32$ on $S^3$. Moreover $d(k_\pm)$ is the dimension of the local Conley index.

(D) If a configuration differs from a reference only away from the poles, then $\mathrm{gr}(x)=\tfrac12\eta(\mathcal L_x)$: the grading is the $\eta$-invariant of its own Hessian. For KW objects this is conjectural.

So one-object action-window categories near the fold realize to $\Sigma^{d}\mathbb S$ with derived $d$. We compare with Manolescu's rational shift and Floer's $\mathbb Z/8$ grading. verify.py: 58 checks, FALLOS = 0.

---

## 1. Introduction

### 1.1 The problem

The simplest framed flow category in the sense of Abouzaid–Blumberg [AB] has one object $x$, no morphisms, and a framing by a virtual vector space of rank $d$. Its realization is $\Sigma^d\mathbb S$. To produce it from Haydys–Witten (HW) theory one needs a Kapustin–Witten (KW) solution $x$ with three properties:

1. $x$ is nondegenerate: its complete gauge-fixed Hessian $\mathcal L_x$ is invertible in the Nahm-pole function spaces;
2. $x$ is dynamically isolated: no HW trajectory relevant to the category enters or leaves it;
3. $x$ carries an **absolute** grading $d(x)$.

In the rStation series the same three barriers appear in three settings: spherical space forms near the Anderson–Henningson (AH) fold, the $\mathrm{Sol}^4$ kink sector, and the straight knot on the Coulomb branch. Barrier 1 is settled on space forms near the fold ([R59, Thm. C], recalled below). Barrier 2 is settled locally near the fold ([R34], [R59, Thm. C(2)]). Barrier 3 has not been addressed: only relative indices, that is spectral flows, are canonical, and the published kink-sector paper [R60, §1] records the absolute gradings $d_\kappa$, $d_p$ as normalizations, not derived quantities.

This paper addresses barrier 3 on spherical space forms, for configurations on $Y\times(0,L)$ with Nahm poles at both ends. We construct a grading that is derived, not normalized; prove that it is independent of every auxiliary choice that enters; prove that it lifts the relative index of every HW trajectory; identify it with an $\eta$-invariant on a large class of configurations; and compute it on the AH objects.

### 1.2 Setting

Let $Y=G\backslash S^3_r$, with $G\subset SO(4)$ finite and acting freely; $G=1$ (that is, $Y=S^3$) is allowed. We use the conventions of [R30, R59]: the left-invariant frame $e_i$, coframe $\sigma^i$, Milnor constant $c=2/r$, and a spin structure $\mathfrak s$ with $SU(2)$-bundle $P_{\mathfrak s}$ and $\operatorname{ad}P_{\mathfrak s}\cong TY$ [R59, Lemma 2.1]. Put $X=Y\times(0,L)$. A *configuration* is a pair $x=(A,\varphi)$ on $X$ in temporal gauge, so $A=A_y\,dy+A_i\sigma^i$ and $\varphi=\varphi_i\sigma^i$, with Nahm poles at $y=0$ and $y=L$ [MW]. The *isotropic* configurations are
$$x(p,q):\qquad A_i=\big(\tfrac1r-p\big)T_i,\qquad \varphi_i=-q\,T_i,\qquad A_y=0,\tag{1.1}$$
with $u=p+iq$ a function of $y$. In the HW equations they satisfy $\partial_su+i\partial_yu=\bar u^2-r^{-2}$ [R24]. By [R59, Lemma 2.3], $A=\nabla^{\rm spin}-p\,\theta$, where $\theta$ is the soldering form. So **$p=0$ means exactly that $A$ is the Levi-Civita (spin) connection**, and then $\varphi=-q\,\theta$ is proportional to the soldering form.

The *complete gauge-fixed static operator* $\mathcal L_x$ is the linearization at $x$ of the HW system (E1)–(E3) of [R30, §2], together with the 5D Coulomb condition. It acts on the 24 real components $\xi=(\alpha_i,\psi_i,a_s,a_y)$. At isotropic configurations [R30, (2.1)]:
$$\mathcal L(p,q)=J\partial_y+\mathcal D-p\,M-q\,V_1 ,\tag{1.2}$$
where $\mathcal D$ is a fixed twisted Dirac operator on $Y$, independent of $y$ and of the background, and $J,M,V_1$ are constant matrices. Moreover $J,\mathcal D,V_1$ pairwise anticommute [R30, Thm. A], while $M$ anticommutes with $J$ only (verify.py §0). We put $B=JV_1$. Its eigenvalues are $\pm1,\pm2$, the indicial roots at both poles. Write $E^\sigma$ for the $B=\sigma$ eigenbundle and $\mathcal D^+:=\mathcal D|_{E^1\oplus E^2}$.

### 1.3 Results

The bounded Nahm-pole class $\mathcal A_L(Y)$ consists of all smooth configurations $x$ such that $x-x(0,q_L)$ is bounded, where $q_L(y)=-\frac\pi L\cot\frac{\pi y}L$. It contains every isotropic static KW solution, by the uniform Nahm asymptotics [R46, Thm. B]. The *Levi-Civita reference class* is
$$\mathcal R_L(Y)=\{x(0,q):\ q\in C^\infty(0,L),\ q-q_L\ \text{bounded}\}\subset\mathcal A_L(Y).$$

**Theorem A (the Nahm-pole gauge group and loop spectral flow; §3).** Let $Y$ be any closed oriented 3-manifold, with principal $SU(2)$ Nahm poles on both ends of $\bar X=Y\times[0,L]$.
1. A smooth gauge transformation $g$ maps Nahm-pole configurations to Nahm-pole configurations iff $g|_{Y\times\{0\}}$ and $g|_{Y\times\{L\}}$ are constant with values in the centre $\{\pm1\}$. Let $\mathcal G$ be the group of such $g$. Then $\mathcal G$ preserves $\mathcal A_L(Y)$.
2. $\pi_0(\mathcal G)$ is an extension of $(\mathbb Z/2)^2$ (boundary values) by $[\Sigma Y,S^3]_*\cong\tilde\pi^2_s(Y)$, and $\tilde\pi^2_s(Y)$ is an extension of $H^2(Y;\mathbb Z)$ by $\mathbb Z/2$. Hence $\pi_0(\mathcal G)$ is finite iff $b_1(Y)=0$, and then $|\pi_0(\mathcal G)|=8\,|H_1(Y;\mathbb Z)|$. For example the order is $8$ for $S^3$ (where $[\Sigma S^3,S^3]_*=\pi_4(S^3)=\mathbb Z/2$), $8p$ for lens spaces $L(p,q)$, $32$ for the prism manifolds $S^3/D^*_{4n}$, $24,16,8$ for $S^3/T^*,S^3/O^*,S^3/I^*$.
3. Let $Y=G\backslash S^3_r$. For every $g\in\mathcal G$, every $x\in\mathcal A_L(Y)$ and every small $\varepsilon>0$ with $\varepsilon\notin\operatorname{spec}\mathcal L_x$, we have $\mathrm{sf}(\mathcal L_x-\varepsilon\to\mathcal L_{g\cdot x}-\varepsilon)=0$ along any path in $\mathcal A_L(Y)$. Consequently the relative grading between nondegenerate configurations depends only on gauge classes and is $\mathbb Z$-valued, with no reduction modulo any $N$.

In Floer's instanton theory on a homology sphere, $\pi_0$ of the gauge group is $\mathbb Z$, and a degree-one gauge transformation produces spectral flow $8$, so relative indices are defined only mod $8$ [Fl]. The Nahm poles remove these gauge transformations: they are not central on the boundary.

**Theorem B (spectral rigidity of the Levi-Civita reference class; §4).** Let $Y=G\backslash S^3_r$, $L>0$ and $x_q=x(0,q)\in\mathcal R_L(Y)$, with $\mathcal L_q:=\mathcal L_{x_q}$.
1. $\mathcal L_q$ is essentially self-adjoint on $C^\infty_c(X)$ and has compact resolvent. Its spectrum consists of pairs $\pm(\mu^2+\lambda)^{1/2}$, with $\lambda\in\operatorname{spec}(T_{\sigma,q}^*T_{\sigma,q})\setminus\{0\}$ and $T_{\sigma,q}=\partial_y+\sigma q$, together with the unpaired eigenvalues $\operatorname{spec}\mathcal D^+_Y$ (with multiplicity).
2. $\ker\mathcal L_q=\{e^{-\sigma\int q}\,v:\ v\in\ker\mathcal D^+\}$ has dimension $h_Y$, where $h_{S^3}=5$ and $h_Y=1$ for $Y\ne S^3$. For $Y\ne S^3$ it is spanned by the isotropic mode $e^{-2\int q}$, which equals $\sin^2(\pi y/L)$ when $q=q_L$.
3. $\eta(\mathcal L_q;s)=r^s\eta(\mathcal D^+_Y;s)$ for $\operatorname{Re}s>4$. Hence $\eta(\mathcal L_q)=\rho_V(Y)+\eta_{\rm sig}(Y)$ for every $q$ and every $L$. The value is recalled from [R59, Thm. E].
4. $\operatorname{spec}\mathcal L_q\cap(-c_q,c_q)=\{0\}$, with $c_q=\min(1/r,\lambda_1(q)^{1/2})>0$, where $\lambda_1(q)$ is the bottom of $\operatorname{spec}T_{\sigma,q}T_{\sigma,q}^*$ over $\sigma\in\{1,2\}$. For $q=q_L$, $\lambda_1=3\pi^2/L^2$. If $q$ is the profile of a static isotropic KW solution with $\sup|p|\le1/r$, then $\lambda_1(q)\ge\pi^2/L^2$.
5. Any two elements of $\mathcal R_L(Y)$ are joined by a path in $\mathcal R_L(Y)$ along which the kernel is constant and no eigenvalue crosses $0$.

The mechanism in (1)–(3) is that of [R59, Prop. 6.1, Cor. 6.2] at the fold. The new point is that it holds on the whole class, uniformly in $L$. This rigidity is what makes $\mathcal R_L(Y)$ a reference: every element has the same spectral position relative to $0$.

**Definition.** For $x\in\mathcal A_L(Y)$ and $x_{\rm ref}\in\mathcal R_L(Y)$, put
$$\mathrm{sf}_{1/2}(\mathcal L_{\rm ref}\to\mathcal L_x):=\mathrm{sf}(\mathcal L_{\rm ref}-\varepsilon\to\mathcal L_x-\varepsilon)-\tfrac12\dim\ker\mathcal L_{\rm ref}+\tfrac12\dim\ker\mathcal L_x ,$$
$$\mathrm{gr}(x):=\tfrac12\,\eta(\mathcal L_{\rm ref})+\mathrm{sf}_{1/2}(\mathcal L_{\rm ref}\to\mathcal L_x),\qquad d(x):=\mathrm{sf}(\mathcal L_{\rm ref}-\varepsilon\to\mathcal L_x-\varepsilon)\in\mathbb Z .$$
Here $\varepsilon>0$ is smaller than every nonzero $|\lambda|$ for $\lambda$ in the spectra of the two endpoints, and the path lies in $\mathcal A_L(Y)$. For nondegenerate $x$,
$$\mathrm{gr}(x)=d(x)+\tfrac12\big(\rho_V(Y)+\eta_{\rm sig}(Y)-h_Y\big).\tag{1.3}$$
The symmetric convention $\mathrm{sf}_{1/2}$ is the one for which the finite-dimensional identity $\tfrac12\eta(A_1)-\tfrac12\eta(A_0)=\mathrm{sf}_{1/2}(A_0\to A_1)$ holds (verify.py §7). So $\mathrm{gr}$ is "formally $\tfrac12\eta(\mathcal L_x)$", and Theorem D makes this literal on a large class.

**Theorem C (the canonical grading; §5).** Let $Y=G\backslash S^3_r$ and $L>0$.
1. *Well-definedness.* $\mathrm{gr}$ and $d$ do not depend on $x_{\rm ref}\in\mathcal R_L(Y)$, on $\varepsilon$ or on the path. They are gauge invariant: $\mathrm{gr}(g\cdot x)=\mathrm{gr}(x)$ for all $g\in\mathcal G$. They do not depend on the spin structure, and they are invariant under the scaling $(r,L)\mapsto(\lambda r,\lambda L)$.
2. *Index formula.* Let $u$ be an HW trajectory in temporal gauge from $x_-$ to $x_+$, both nondegenerate, with $u(s)\in\mathcal A_L(Y)$ and $s\mapsto\mathcal L_{u(s)}-\mathcal L_{\rm ref}$ norm-continuous with limits (the hypotheses of Robbin–Salamon). Then $D_u=\partial_s-\mathcal L_{u(s)}$ is Fredholm and
$$\operatorname{ind}D_u=\mathrm{gr}(x_-)-\mathrm{gr}(x_+)=d(x_-)-d(x_+).$$
This holds for every such trajectory, isotropic or not, given the structural property (S1) of §2, which is verified exactly at isotropic configurations.
3. *Values near the fold.* There is $\delta>0$ such that for $\pi r<L<\pi r+\delta$:
   * if $Y\ne S^3$: $\mathrm{gr}(k_\pm)=\tfrac12(\rho_V(Y)+\eta_{\rm sig}(Y))\pm\tfrac12$, $d(k_+)=1$ and $d(k_-)=0$;
   * if $Y=S^3$: $\mathrm{gr}(k_\pm)=\mp\tfrac32$, $d(k_+)=1$ and $d(k_-)=4$.

   On $Y\ne S^3$ the conclusion holds on the whole range where $2\sup|\operatorname{Re}u_\pm|<\tfrac12\min(1/r,\pi/L)$. Numerically this is $\pi r<L\le3.1999\,r$ (verify.py §8).
4. *Orientation.* $\mathrm{gr}_{-Y}(k_\mp)=-\mathrm{gr}_Y(k_\pm)$. The integer grading $d$ does not have this property; the $\eta$-shift is what makes $\mathrm{gr}$ odd.
5. *Products.* For $SU(2)\times SU(2)$ with principal Nahm poles in both factors, $\mathrm{gr}(k_{ab})=\mathrm{gr}(k_a)+\mathrm{gr}(k_b)$. On $Y\ne S^3$ the four objects have gradings $\eta_Y+1,\eta_Y,\eta_Y,\eta_Y-1$.
6. *Conley indices.* In the range of (3), $d(k_\pm)$ is the dimension of the local Conley index of $k_\pm$: $S^1$ and $S^0$ on $Y\ne S^3$, and $S^1$ and $S^4$ on $S^3$ [R59, Thm. D(2)].

Table 1 lists values. Consistency checks: $\mathrm{gr}(k_+)-\mathrm{gr}(k_-)=1$ on $Y\ne S^3$, which is the index of the AH arrow on $Y$ [R59, Thm. C(3)]; and $-3$ on $S^3$, which is the index of [R30, Thm. D].

**Theorem D ($\mathrm{gr}$ is an $\eta$-invariant on interior deformations; §7).** Let $x_{\rm ref}\in\mathcal R_L(Y)$, let $b$ be smooth with compact support in $Y\times(0,L)$, and let $g\in\mathcal G$. Put $x=g\cdot(x_{\rm ref}+b)$. Then $\eta(\mathcal L_x;s)$ converges for $\operatorname{Re}s>4$, extends meromorphically, is regular at $s=0$, and
$$\mathrm{gr}(x)=\tfrac12\,\eta(\mathcal L_x),$$
with zero eigenvalues contributing $0$ to $\eta$. In particular, for such nondegenerate $x$ the canonical grading is computed from $\mathcal L_x$ alone, with no reference and no path. The reason is that the Hessians are four-dimensional: the local variation of $\eta$ is the $\tau^{-1/2}$ heat coefficient, which vanishes in the interior of an even-dimensional manifold.

The KW objects themselves are not interior deformations of a reference, since $\operatorname{Re}u\sim c\,y^2$ at the poles. Conjecture 7.3 asserts $\mathrm{gr}(x)=\tfrac12\eta(\mathcal L_x)$ for them too; §7.3 gives the evidence and the precise missing ingredient, a boundary heat coefficient.

**Corollary E (one-object categories and $\Sigma^{d}\mathbb S$; §8).** Let $Y\ne S^3$ and $\pi r<L<\pi r+\delta$. In the isolating neighbourhood of [R59, Thm. C], every action window of length less than the action gap that contains $\mathcal A(k_-)$ (respectively $\mathcal A(k_+)$) gives a local category with one object and no morphisms. With the canonical framing its realization is $\Sigma^{d(k_-)}\mathbb S=\mathbb S$ (respectively $\Sigma^{d(k_+)}\mathbb S=\Sigma\mathbb S$). This is the suspension spectrum of the local Conley index, with no desuspension left undetermined. The rational refinement $\Sigma^{\mathrm{gr}}$ is the same spectrum with the formal shift $\tfrac12(\eta_Y-1)\in\mathbb Q$, in the bookkeeping of Manolescu's triples [Man, §6].

**Table 1.** Canonical gradings of the AH objects near the fold (Theorem C(3)); $\eta_Y=\rho_V+\eta_{\rm sig}$ is recalled from [R59, Thm. E] and recomputed in verify.py §5.

| $Y$ | $\eta_Y$ | $\mathrm{gr}(k_+)$ | $\mathrm{gr}(k_-)$ |
|---|---|---|---|
| $S^3$ | $0$ | $-\tfrac32$ | $\tfrac32$ |
| $L(2,1)=\mathbb{RP}^3$ | $0$ | $\tfrac12$ | $-\tfrac12$ |
| $L(3,1)$ | $\tfrac{10}9$ | $\tfrac{19}{18}$ | $\tfrac1{18}$ |
| $L(4,1)$ | $\tfrac32$ | $\tfrac54$ | $\tfrac14$ |
| $L(5,1)$ | $\tfrac85$ | $\tfrac{13}{10}$ | $\tfrac3{10}$ |
| $L(7,1)$ | $\tfrac{10}7$ | $\tfrac{17}{14}$ | $\tfrac3{14}$ |
| $L(p,1)$ | $-\tfrac{(p-2)(p-13)}{3p}$ | $\tfrac12-\tfrac{(p-2)(p-13)}{6p}$ | $-\tfrac12-\tfrac{(p-2)(p-13)}{6p}$ |
| $L(5,2)$, $L(13,1)$ | $0$ | $\tfrac12$ | $-\tfrac12$ |
| $L(8,3)$ | $\tfrac34$ | $\tfrac78$ | $-\tfrac18$ |
| $S^3/D^*_8$ | $\tfrac94$ | $\tfrac{13}8$ | $\tfrac58$ |
| $S^3/D^*_{4n}$ | $\tfrac{-2n^2+24n-13}{6n}$ | $\tfrac{-2n^2+30n-13}{12n}$ | $\tfrac{-2n^2+18n-13}{12n}$ |
| $S^3/T^*$ | $\tfrac{83}{36}$ | $\tfrac{119}{72}$ | $\tfrac{47}{72}$ |
| $S^3/O^*$ | $\tfrac{155}{72}$ | $\tfrac{227}{144}$ | $\tfrac{83}{144}$ |
| $S^3/I^*$ (Poincaré) | $\tfrac{347}{180}$ | $\tfrac{527}{360}$ | $\tfrac{167}{360}$ |

On none of the listed $Y\ne S^3$ is $\mathrm{gr}$ an integer, so the shift is genuinely rational (verify.py §6).

### 1.4 Which barriers are advanced

* **Barrier 3** (absolute grading): advanced. On spherical space forms the grading is derived from a canonical, spectrally rigid reference class. It is independent of every auxiliary choice that enters (Theorems A–C), and on interior deformations it equals the $\eta$-invariant of the Hessian itself (Theorem D). The obstruction one might expect, a nonzero loop spectral flow giving gradings only modulo $N$, is absent because $\pi_0(\mathcal G)$ is finite. We compute $|\pi_0(\mathcal G)|$.
* **Barrier 2** (isolation): only the local statement near the fold, already contained in [R34, R59], is used; Corollary E records its consequence. We prove no new isolation theorem.
* **Barrier 1** (nondegeneracy): recalled from [R59, Thm. C] near the fold, and from the companion global-Fredholm preprint for all $L$ (conditional statements, §6.2).

### 1.5 Relation to published work (summary; details in §10)

*Recalled:* the operator (1.2) and its anticommutation structure [R30]; the fold spectral analysis and the value $\eta(\mathcal L^Y_*)=\rho_V+\eta_{\rm sig}$ [R59]; the objects $k_\pm$, their isotropic nondegeneracy and the action gap [R24, R46]; the small eigenvalues of $\mathcal L(k_\pm)$ near the fold [R30, Thm. C]; the local classification and Conley indices on $Y$ [R59, Thms. C, D]; isolation [R34].

*New within the rStation series:* Theorem A; the extension of the fold rigidity to the whole reference class, uniformly in $L$, with the gap bound (Theorem B); the definition of $\mathrm{gr}$ and $d$ and Theorem C; Theorem D; Corollary E as a consequence. We found no treatment of absolute gradings for Nahm-pole problems outside the series. The Fredholm framework for HW in [Bl] uses relative indices.

## 2. Standing facts

We use the following.

* **(F1)** [R30, Thm. B(1), Prop. 4.2]; [R59, Thm. B(3)]. On $Y\times(0,\pi r)$ the fold operator $\mathcal L_*=\mathcal L(0,-\tfrac1r\cot(y/r))$ is essentially self-adjoint on $C_c^\infty$, has compact resolvent, and its domain elements are $O(\min(y,L-y)^{1/2})$. The proof uses only the indicial roots $\pm1,\pm2$.
* **(F2)** [R24, Prop. B], [R46]. For $L>\pi r$ the isotropic static solutions are exactly $k_\pm$. They are nondegenerate in the isotropic class, and $k_-$ is the image of $k_+$ under $(p,q)\mapsto(-p,q)$. They form, with the fold solution $k_0=x(0,-\tfrac1r\cot\tfrac yr)$ at $L=\pi r$, a continuous family parametrized by the first integral $h=\operatorname{Re}(u^3/3-u)$, with $h\to0$ as $L\downarrow\pi r$.
* **(F3)** [R46, Thm. B]. Uniform Nahm asymptotics: $|\operatorname{Re}u|\le Cy^{3/2}$ and $|\operatorname{Im}u+1/y|\le Cy$ near $y=0$, and symmetrically near $y=L$. Hence isotropic static solutions lie in $\mathcal A_L(Y)$.
* **(F4)** [R30, Thm. C]; [R59, Thm. C(3)]. For $\pi r<L<\pi r+\delta$, $\mathcal L(k_\pm)$ on $S^3$ has exactly five eigenvalues near $0$: $\lambda_{\rm iso}=\tfrac53x_\pm+O(\bar\nu)$ on the isotropic block, and $\lambda_{1/2}=-\tfrac54x_\pm+O(\bar\nu)$ with multiplicity $4$ on the spin-½ block. Here $\pm x_\pm>0$. On $Y\ne S^3$ only $\lambda_{\rm iso}$ survives.
* **(F5)** [R59, Thm. E]. $\eta(\mathcal L^Y_*;s)=r^s\eta(\mathcal D^+_Y;s)$ converges for $\operatorname{Re}s>4$, continues meromorphically, and is regular at $0$, with value $\rho_V(Y)+\eta_{\rm sig}(Y)$. This value changes sign under $Y\mapsto-Y$.
* **(F6)** [R59, Thms. C(2), D(2)]; [R34]. Near the fold, the HW trajectories on $Y$ in the isolating neighbourhood are the constants and the translates of the AH instanton $u$. The local Conley indices of $k_+$ and $k_-$ are $S^1$ and $S^0$ on $Y\ne S^3$, and $S^1$ and $S^V=S^4$ on $S^3$. Passing to gauge classes for trajectories is conditional on Hypothesis (G) of [R34].
* **(RS)** Robbin–Salamon [RS, Thm. 4.21]. If $A(s)=A_0+K(s)$, with $A_0$ self-adjoint with compact resolvent and $K$ norm-continuous and bounded with invertible limits, then $\partial_s-A(s)$ is Fredholm with index $-\mathrm{sf}(A)$, where upward crossings count $+1$.

Spectral flow for norm-continuous paths of bounded self-adjoint perturbations of a fixed self-adjoint operator with compact resolvent is well defined, additive under concatenation, and invariant under homotopies with invertible endpoints [Ph, BLP]. It is unchanged by conjugating the whole path with a fixed unitary.

We also use two structural properties of $\mathcal L_x$ for $x\in\mathcal A_L(Y)$.

* **(S1)** The HW equations and the Coulomb condition are polynomial of degree at most two in $(A,\varphi)$, and the quadratic part is algebraic. So $\mathcal L_x-\mathcal L_{x'}$ is multiplication by a pointwise endomorphism that depends linearly on $x-x'$. In temporal gauge $\mathcal L_x$ is the extended Hessian of the HW action at $x$ (the Hessian bordered by the gauge-fixing pairing), so it is formally self-adjoint. At isotropic configurations this is verified exactly (verify.py §0). Hence, for $x\in\mathcal A_L(Y)$, $\mathcal L_x=\mathcal L_{\rm ref}+K_x$ with $K_x$ bounded and symmetric. So $\mathcal L_x$ is self-adjoint on $\operatorname{dom}\mathcal L_{\rm ref}$ with compact resolvent, by Kato–Rellich and Theorem B(1).
* **(S2)** Gauge covariance: $\mathcal L_{g\cdot x}=\operatorname{Ad}(g)\,\mathcal L_x\operatorname{Ad}(g)^{-1}$ for $g\in\mathcal G$, as self-adjoint operators. As differential expressions this is the naturality of the linearized equations and of the Coulomb condition. That $\operatorname{Ad}(g)$ preserves the domain is shown in §3.3.

## 3. The Nahm-pole gauge group (Theorem A)

### 3.1 Central boundary values

Every $SU(2)$-bundle over a 3-manifold, and over $\bar X$, is trivial, so gauge transformations are maps $g:\bar X\to SU(2)$. The centre $\{\pm1\}$ does not depend on the trivialization.

*Proof of Theorem A(1).* The Nahm pole at $y=0$ prescribes $\varphi=\theta/y+O(1)$, where $\theta:TY\to\operatorname{ad}P$ is the fixed isomorphism. If $g$ is smooth up to the boundary, then
$$g\cdot\varphi=\operatorname{Ad}(g)\varphi=\operatorname{Ad}(g|_{y=0})\theta/y+O(1).$$
This has the Nahm leading term iff $\operatorname{Ad}(g|_{y=0})\circ\theta=\theta$. Since $\theta$ is an isomorphism onto $\operatorname{ad}P$, this means $\operatorname{Ad}(g|_{y=0})=\mathrm{id}$, that is $g|_{y=0}\in\{\pm1\}$ pointwise, hence constant since $Y$ is connected. The same holds at $y=L$. Conversely, let $g\in\mathcal G$ and $x\in\mathcal A_L(Y)$. Then $g\cdot x-x=-(dg)g^{-1}+(\operatorname{Ad}g-1)x$. Near $y=0$, $\operatorname{Ad}g-1=O(y)$, since $g$ is $C^1$ and $\operatorname{Ad}(\pm1)=1$. This compensates the $1/y$ in $x$, so $g\cdot x-x$ is bounded and $g\cdot x\in\mathcal A_L(Y)$. ∎

Gauge transformations constant in $y$ and of nonzero degree on $Y$, the ones responsible for the mod-$8$ ambiguity in instanton theory, are not in $\mathcal G$: they rotate the identification $\theta$ at the boundary.

### 3.2 The component group

*Proof of Theorem A(2).* The boundary values give a homomorphism $\pi_0(\mathcal G)\to\{\pm1\}^2$. It is onto: the constant $-1$ maps to $(-1,-1)$, and the half-turn $g(y)=\exp(\pi yX/L)$, with $X\in\mathfrak{su}(2)$ and $\exp(\pi X)=-1$, maps to $(1,-1)$. The kernel consists of the homotopy classes of maps $(\bar X,\partial\bar X)\to(SU(2),1)$. Smooth maps that agree on the boundary and are continuously homotopic rel boundary are smoothly homotopic rel boundary [Hi, Ch. 2], so the kernel is $[\bar X/\partial\bar X,S^3]_*$. Now
$$\bar X/\partial\bar X=Y_+\wedge(I/\partial I)=\Sigma(Y_+)\simeq\Sigma Y\vee S^1 .$$
So the kernel is $[\Sigma Y,S^3]_*\times\pi_1(S^3)=[\Sigma Y,S^3]_*$. Since $\Sigma Y$ is a 4-dimensional CW complex and $S^3$ is 2-connected, the Freudenthal theorem ($\dim\le2\cdot3-2$) identifies $[\Sigma Y,S^3]_*$ with the stable group $\{\Sigma Y,S^3\}=\tilde\pi^3_s(\Sigma Y)=\tilde\pi^2_s(Y)$ [Sw, Ch. 6], [Ha, §4.2].

In the Atiyah–Hirzebruch spectral sequence $E_2^{a,b}=\tilde H^a(Y;\pi_{-b}^s)\Rightarrow\tilde\pi^{a+b}_s(Y)$ [AtHi], total degree $2$ has
$$E_2^{2,0}=H^2(Y;\mathbb Z),\qquad E_2^{3,-1}=H^3(Y;\mathbb Z/2)=\mathbb Z/2,\qquad E_2^{1,1}=0\quad(\pi^s_{-1}=0).$$
* Differentials into $E^{2,0}$ start in $E^{2-r,r-1}$, which has coefficients $\pi^s_{1-r}=0$ for $r\ge2$.
* Differentials out of $E^{2,0}$ and $E^{3,-1}$ land in degrees $a\ge4>\dim Y$.
* The only possible differential into $E^{3,-1}$ is $d_2$ from $E^{1,0}=H^1(Y;\mathbb Z)$. It is $\mathrm{Sq}^2$ composed with reduction mod 2, which vanishes on degree-one classes.

Hence $\tilde\pi^2_s(Y)$ is an extension of $H^2(Y;\mathbb Z)\cong H_1(Y;\mathbb Z)$ by $\mathbb Z/2$. It is finite iff $b_1(Y)=0$, and then it has order $2|H_1(Y)|$, so $|\pi_0(\mathcal G)|=4\cdot2|H_1(Y)|$. The examples follow from $H_1$: $\mathbb Z/p$ for lens spaces; $\mathbb Z/4$ or $(\mathbb Z/2)^2$ for prism manifolds; $\mathbb Z/3,\mathbb Z/2,0$ for $T^*,O^*,I^*$ (Smith normal forms in verify.py §4). ∎

### 3.3 Loop spectral flow

*Domain invariance.* For $g\in\mathcal G$ and $x_{\rm ref}\in\mathcal R_L(Y)$, the commutator $[\mathcal L_{\rm ref},\operatorname{Ad}g]$ is a sum of three terms: $J(\partial_y\operatorname{Ad}g)$; terms $N_i(e_i\operatorname{Ad}g)$; and algebraic terms of the form $[V,\operatorname{Ad}g]$. The only singular coefficient is $q\,[V_1,\operatorname{Ad}g]$, and it is bounded because $\operatorname{Ad}g-1=O(\min(y,L-y))$. So the commutator is bounded. Since $\operatorname{dom}\mathcal L_{\rm ref}$ is the maximal domain (F1, Theorem B(1)), $\operatorname{Ad}g$ preserves it, and (S2) holds as an identity of self-adjoint operators.

*Proof of Theorem A(3).* Fix $x_{\rm ref}$ and $\varepsilon$ smaller than the gap $c$ of Theorem B(4). For $g\in\mathcal G$ put
$$\mathrm{SF}(g):=\mathrm{sf}(\mathcal L_{\rm ref}-\varepsilon\to\mathcal L_{g\cdot x_{\rm ref}}-\varepsilon)$$
along the straight segment of operators from $\mathcal L_{\rm ref}$ to $\operatorname{Ad}(g)\mathcal L_{\rm ref}\operatorname{Ad}(g)^{-1}=\mathcal L_{g\cdot x_{\rm ref}}$. The difference of the endpoints is $\operatorname{Ad}(g)[\mathcal L_{\rm ref},\operatorname{Ad}(g)^{-1}]$, which is bounded and symmetric by the domain argument above; so the segment consists of bounded symmetric perturbations of $\mathcal L_{\rm ref}$, and this step does not use (S1) beyond gauge covariance. The endpoints are invertible, since $\mathcal L_{g\cdot x_{\rm ref}}-\varepsilon$ is unitarily equivalent to $\mathcal L_{\rm ref}-\varepsilon$.

* *Homomorphism.* Conjugation by $\operatorname{Ad}g_1$ carries the segment from $\mathcal L_{\rm ref}$ to $\mathcal L_{g_2x_{\rm ref}}$ onto the segment from $\mathcal L_{g_1x_{\rm ref}}$ to $\mathcal L_{g_1g_2x_{\rm ref}}$, and preserves spectral flow. Concatenating with the segment from $\mathcal L_{\rm ref}$ to $\mathcal L_{g_1x_{\rm ref}}$, and using that the affine space $\mathcal L_{\rm ref}+\{\text{bounded symmetric}\}$ is contractible, gives $\mathrm{SF}(g_1g_2)=\mathrm{SF}(g_1)+\mathrm{SF}(g_2)$.
* *Homotopy invariance.* If $g_t$ is a $C^1$-continuous path in $\mathcal G$, then $t\mapsto\operatorname{Ad}(g_t)[\mathcal L_{\rm ref},\operatorname{Ad}(g_t)^{-1}]$ is norm-continuous, by the estimate $|\operatorname{Ad}g-1|\le C\|g\|_{C^1}\min(y,L-y)$. The endpoints stay invertible, so $\mathrm{SF}(g_t)$ is constant.

So $\mathrm{SF}$ descends to a homomorphism $\pi_0(\mathcal G)\to\mathbb Z$. By (2), $\pi_0(\mathcal G)$ is finite, because $b_1(G\backslash S^3)=0$. If $g^N\simeq1$, then $N\,\mathrm{SF}(g)=\mathrm{SF}(g^N)=0$, so $\mathrm{SF}\equiv0$.

For arbitrary $x$ we use additivity of $\mathrm{sf}_{1/2}$ and its invariance under conjugation:
$$\mathrm{sf}_{1/2}(x\to gx)=-\mathrm{sf}_{1/2}(x_{\rm ref}\to x)+\mathrm{SF}(g)+\mathrm{sf}_{1/2}(gx_{\rm ref}\to gx)=\mathrm{SF}(g)=0 .$$
Since $\dim\ker\mathcal L_x=\dim\ker\mathcal L_{gx}$, this is the claim. ∎

**Remarks 3.1.**
1. The same argument proves $\mathrm{SF}\equiv0$ on any closed $Y$ with $b_1=0$ for which (S1), (S2) and a reference with compact resolvent are available. For $b_1(Y)>0$, $\pi_0(\mathcal G)$ contains $H^2(Y;\mathbb Z)/\mathrm{tors}\cong\mathbb Z^{b_1}$, and $\mathrm{SF}$ restricted to it is a homomorphism to $\mathbb Z$ that we do not compute; no Fredholm theory is available there in the series. If it were nonzero, with image $N\mathbb Z$, gradings would be defined only mod $N$.
2. The companion global-Fredholm preprint finds that the relative index of the AH arrow on round $S^3$ lies in $-3+8\mathbb Z$. By Theorem A(3) this "$8$" is not a gauge ambiguity: the relative index is a well-defined integer, and the congruence comes from a duality of Peter–Weyl blocks.

## 4. The Levi-Civita reference class (Theorem B)

### 4.1 Block reduction

Work on the unit sphere ($r=1$); eigenvalues scale as $r^{-1}$. By [R59, Lemma 2.2], fields on $Y$ are the $G$-invariant fields on $S^3$. The matrices $J,V_1,B$ commute with $G$, and $\mathcal D$ commutes with $SO(4)\supset G$. Since $\{J,B\}=\{J,\mathcal D\}=0$ and $[B,\mathcal D]=0$ (verify.py §0), the joint eigenspaces $E^\sigma_\mu=\{B=\sigma,\ \mathcal D=\mu\}\subset L^2(Y;\mathbb R^{24})$ are finite-dimensional, consist of smooth sections, and satisfy $JE^\sigma_\mu=E^{-\sigma}_{-\mu}$. Since $B$ has no zero eigenvalue,
$$L^2(X;\mathbb R^{24})^G=\widehat{\bigoplus_{\sigma\in\{1,2\},\,\mu}}L^2(0,L)\otimes\big(E^\sigma_\mu\oplus JE^\sigma_\mu\big).$$
On $E^\sigma$ we have $V_1=-JB$ (verify.py §0), so $J\partial_y-qV_1=J(\partial_y+\sigma q)=:JT$. Writing elements as $a+Jb$, with $a,b\in L^2(0,L)\otimes E^\sigma_\mu$,
$$\mathcal L_q(a+Jb)=(\mu a+T^*b)+J(Ta-\mu b),\qquad T=\partial_y+\sigma q,\quad T^*=-\partial_y+\sigma q .\tag{4.1}$$
This is [R59, Prop. 6.1] with $-\cot y$ replaced by an arbitrary $q$.

*Proof of Theorem B(1).* Since $q-q_L$ is bounded, $T=T_L+\sigma(q-q_L)$ with $T_L=\partial_y-\sigma\frac\pi L\cot\frac{\pi y}L$. For $\sigma\ge1$, $T_L$ is limit point at both ends ([R30, Prop. 4.2]; the indicial exponent $\sigma$ satisfies $|\sigma|\ge\tfrac12$). So the closure of $T$ from $C_c^\infty(0,L)$ is its maximal realization, and (4.1) is self-adjoint on $\operatorname{dom}T\oplus\operatorname{dom}T^*$. Its square is $\mu^2+\operatorname{diag}(T^*T,TT^*)$.

For $q=q_L$, $T^*T=-\partial_y^2+\sigma(\sigma-1)\frac{\pi^2}{L^2}\csc^2\frac{\pi y}L-\sigma^2\frac{\pi^2}{L^2}$ is a Pöschl–Teller operator. It has eigenfunctions $\sin^\sigma(\pi y/L)\,C^{(\sigma)}_k(\cos(\pi y/L))$ and eigenvalues $\frac{\pi^2}{L^2}((\sigma+k)^2-\sigma^2)$, $k\ge0$ (verify.py §2, $k\le3$; [PT]). For general $q$, $\|Tf\|\le\|T_Lf\|+C\|f\|$ and conversely, so $T^*T$ again has compact resolvent.

The spectral statement is then [R59, Prop. 6.1] verbatim:
* for each eigenvector of $T^*T$ with eigenvalue $\lambda>0$ there is a 2-dimensional invariant space with matrix $\begin{pmatrix}\mu&\lambda\\1&-\mu\end{pmatrix}$ and eigenvalues $\pm(\mu^2+\lambda)^{1/2}$;
* $\ker T=\mathbb Re^{-\sigma\int q}$ is one-dimensional and gives the unpaired eigenvalue $\mu$;
* $\ker T^*=\mathbb Re^{\sigma\int q}$ is not square integrable, since $e^{\sigma\int q}\sim y^{-\sigma}$ with $\sigma\ge1$.

Global essential self-adjointness: finite sums of $C_c^\infty(0,L)\otimes E^\sigma_\mu$ form a core for the direct sum operator and lie in $C_c^\infty(X)$. So the closure of $\mathcal L_q|_{C_c^\infty(X)}$ is a symmetric extension of a self-adjoint operator, hence equal to it.

Compact resolvent and the counting bound $\#\{|\lambda|\le\Lambda\}=O(\Lambda^4)$ hold for $q=q_L$ by the explicit spectrum, exactly as in [R59, §6.1]. They transfer to $q$, because for symmetric bounded $K$, $N_{A+K}([a,b])\le N_A([a-\|K\|,b+\|K\|])$ (min–max applied to $(A-\tfrac{a+b}2)^2$; verify.py §2 illustrates this). ∎

*Proof of Theorem B(2).* Zero eigenvalues occur only as unpaired eigenvalues $\mu=0$, since the pairs have modulus $\ge\lambda^{1/2}>0$. So $\ker\mathcal L_q=\{e^{-\sigma\int q}v:\ v\in\ker\mathcal D^+\}$.

On $S^3$, $\ker\mathcal D^+$ is the span of the $(0,0)$-channel with $\sigma=2$ (dimension 1) and the $(\tfrac12,\tfrac12)$-channel with $\sigma=1$ (dimension 4). This is the content of $\ker\mathcal L_*=\mathbb R\zeta\oplus\mathcal K$ [R30, Thms. A, B(3)], re-verified in verify.py §1. On $Y\ne S^3$ the first channel is $G$-invariant, and the second carries the defining representation $\mathbb R^4$, whose invariants vanish by freeness [R59, Lemma 3.1]. So $h_Y=1$, spanned by $e^{-2\int q}\cdot\mathbf 1$, the isotropic mode. ∎

*Proof of Theorem B(3).* By (1), the eigenvalues of $\mathcal L_q$ are the pairs together with $\operatorname{spec}\mathcal D^+_Y$ with multiplicities. The series converges absolutely for $\operatorname{Re}s>4$ by the counting bound, so the pairs cancel and $\eta(\mathcal L_q;s)=\eta(\mathcal D^+_Y;s)$ (times $r^s$). The right side does not involve $q$ or $L$. By (F5) it equals $\eta(\mathcal L^Y_*;s)$ and is regular at $0$, with value $\rho_V(Y)+\eta_{\rm sig}(Y)$. ∎

*Proof of Theorem B(4).* The nonzero unpaired eigenvalues are $\pm1$, $2j+2$, $-(2j+3)$, $-2j$ ($j\ge1$) and $2j-1$ ($j\ge2$) [R59, Prop. 6.4]; all have modulus $\ge1$. The paired eigenvalues have modulus $\ge\lambda^{1/2}$ with $\lambda\in\operatorname{spec}(TT^*)$, since $T^*T$ and $TT^*$ have the same nonzero spectrum and $\ker TT^*=0$. For $q=q_L$ the smallest such $\lambda$ is $3\pi^2/L^2$ ($\sigma=1$, $k=1$).

If $q$ is the profile of a static isotropic KW solution, then $p'=-2pq$ and $q'=q^2+r^{-2}-p^2$ (verify.py §3). Hence
$$TT^*=-\partial_y^2+\sigma^2q^2+\sigma q'=-\partial_y^2+\sigma(\sigma+1)q^2+\sigma(r^{-2}-p^2)\ \ge\ -\partial_y^2$$
as quadratic forms on $C_c^\infty(0,L)$ when $|p|\le1/r$. The form domain lies in $H^1_0(0,L)$, so $\lambda\ge\pi^2/L^2$ by the Dirichlet bound. ∎

*Proof of Theorem B(5).* Along $q_t=(1-t)q_0+tq_1$, the unpaired eigenvalues are constant (they are $\operatorname{spec}\mathcal D^+$) and $\dim\ker$ is constant by (2). The paired eigenvalues are nonzero for every $t$. The bottom of $\operatorname{spec}T_{q_t}T^*_{q_t}$ is positive for each $t$ and depends continuously on $t$, since $q_t-q_0$ is norm-continuous and bounded. So it is bounded below on $[0,1]$, and no eigenvalue crosses $0$. ∎

## 5. The canonical grading (Theorem C)

### 5.1 Well-definedness

*Proof of Theorem C(1).*

* *Path and $\varepsilon$.* $\mathcal A_L(Y)$ is affine. By (S1) every path in it gives bounded perturbations of $\mathcal L_{\rm ref}$. Two paths with the same endpoints are homotopic rel endpoints, and the shifted endpoints are invertible. So the spectral flows agree [Ph, BLP]. For two admissible $\varepsilon$ the counts agree, since no eigenvalue of either endpoint lies between them.
* *Reference.* For $x_{\rm ref},x'_{\rm ref}\in\mathcal R_L(Y)$, additivity gives $\mathrm{sf}_{1/2}(\mathrm{ref}\to x)=\mathrm{sf}_{1/2}(\mathrm{ref}\to\mathrm{ref}')+\mathrm{sf}_{1/2}(\mathrm{ref}'\to x)$. The first term is $0$ by Theorem B(5), and $\eta(\mathrm{ref})=\eta(\mathrm{ref}')$ by Theorem B(3). Since the kernels have equal dimension, $d$ agrees as well.
* *Gauge.* By Theorem A(3), $\mathrm{sf}_{1/2}(x\to g\cdot x)=0$.
* *Spin structure.* By [R59, Lemmas 2.1–2.2], the deformation spaces and the operators for different spin structures coincide.
* *Scaling.* The dilation by $\lambda$ conjugates $\mathcal L$ unitarily to $\lambda^{-1}\mathcal L$, which changes neither spectral flow nor $\eta(0)$. ∎

*Proof of Theorem C(2).* By (S1), $\mathcal L_{u(s)}=\mathcal L_{\rm ref}+K(s)$ satisfies (RS), so $\operatorname{ind}D_u=-\mathrm{sf}(\mathcal L_{u(\cdot)})$. By path independence and additivity, this spectral flow equals $\mathrm{sf}_{1/2}(\mathcal L_{x_-}\to\mathcal L_{x_+})=\mathrm{gr}(x_+)-\mathrm{gr}(x_-)$; the kernel terms vanish because the ends are nondegenerate. The statement for $d$ follows from (1.3). ∎

In particular the gradings of all objects of any HW flow category on $Y\times(0,L)$ built from configurations in $\mathcal A_L(Y)$ are fixed once and for all by $\mathrm{gr}$. This holds whatever the trajectories are, including non-isotropic ones whose existence is open.

### 5.2 Values near the fold

*Proof of Theorem C(3).* Fix $L>\pi r$ and write $k_\pm=x(p_\pm,q_\pm)$. As reference take $x(0,q_\pm)$, which lies in $\mathcal R_L(Y)$ by (F3). Consider the path $t\mapsto x(tp_\pm,q_\pm)$, $t\in[0,1]$. By (1.2),
$$\|\mathcal L(tp_\pm,q_\pm)-\mathcal L(0,q_\pm)\|\le\|M\|\sup|p_\pm|=2\sup|p_\pm|,$$
using $\|M\|=2$ (verify.py §0).

*Smallness.* By (F2), $h_\pm\to0$ as $L\downarrow\pi r$. In units $r=1$, along static solutions $h=-p(1+q^2-p^2/3)$, so $|p|\le\tfrac32|h|$ wherever $|p|\le1$ (verify.py §3). Hence $\sup|p_\pm|\to0$. By Theorem B(4), with $|p_\pm|\le1/r$, the reference has gap $c\ge\min(1/r,\pi/L)$. So for $L$ close to $\pi r$ we have $2\sup|p_\pm|<c/2$.

*Cluster.* Then, for every $t$, the spectrum of $\mathcal L(tp_\pm,q_\pm)$ lies within $2\sup|p_\pm|$ of $\operatorname{spec}\mathcal L(0,q_\pm)\subset\{0\}\cup\{|\lambda|\ge c\}$. The spectral projection onto $(-c/2,c/2)$ is norm-continuous in $t$, of rank $h_Y$. Choose $\varepsilon$ below the moduli of the small eigenvalues at $t=1$. Then
$$d(k_\pm)=\mathrm{sf}(\mathcal L_{\rm ref}-\varepsilon\to\mathcal L(k_\pm)-\varepsilon)=\#\{\text{positive eigenvalues of }\mathcal L(k_\pm)\text{ in }(-c/2,c/2)\}.$$
These $h_Y$ small eigenvalues are those of (F4), since both are all the eigenvalues in a small window around $0$.

* On $Y\ne S^3$, $h_Y=1$ and the small eigenvalue is $\lambda_{\rm iso}(k_\pm)=\tfrac53x_\pm+O(\bar\nu)$. It is positive at $k_+$ and negative at $k_-$, so $d(k_+)=1$ and $d(k_-)=0$.
* On $S^3$, $h=5$: at $k_+$ one positive and four negative eigenvalues, at $k_-$ the reverse. So $d(k_+)=1$ and $d(k_-)=4$.

Now (1.3) with $\eta_{S^3}=0$ gives $\mathrm{gr}(k_+)=1-\tfrac52=-\tfrac32$ and $\mathrm{gr}(k_-)=4-\tfrac52=\tfrac32$ on $S^3$, and $\mathrm{gr}(k_\pm)=\tfrac12\eta_Y\pm\tfrac12$ on $Y$.

*The explicit window on $Y$.* On $Y\ne S^3$ the argument needs only $2\sup|p_\pm|<\tfrac12\min(1/r,\pi/L)$ and the sign of the single small eigenvalue. Since the path is $SO(4)$-equivariant and the reference kernel lies in the isotropic block $H_{00}$, the rank-one cluster projection stays in $H_{00}$. So the small eigenvalue is an eigenvalue of the isotropic Hessian of $k_\pm$. It is nonzero for every $L>\pi r$ by isotropic nondegeneracy (F2), and continuous in $L$ along the static family, so its sign is the sign at the fold. The inequality holds numerically for $\sup|p_\pm|\le0.24/r$, that is $L\le3.1999\,r$ (verify.py §8). That is the stated numerical window. ∎

*Proof of Theorem C(4)–(6).*
* (4) follows from (3) and $\eta_{-Y}=-\eta_Y$ (F5); verify.py §6 checks every entry of Table 1. For $d$: $d_{-Y}(k_-)=0\ne-1=-d_Y(k_+)$.
* (5): the complete operator for $SU(2)\times SU(2)$ is the direct sum of the factor operators; the reference class is the product, $\eta$ and $\mathrm{sf}$ add, and $\pi_0$ of the product gauge group is finite.
* (6): by (F6) the local Conley index of a hyperbolic rest point is the sphere of its unstable space in the centre manifold. Its dimension is the number of positive small eigenvalues, which is $d$ by the proof of (3). ∎

## 6. Further properties and the global range

### 6.1 What the shift means

By (1.3), $\mathrm{gr}-d=\tfrac12(\eta_Y-h_Y)$ depends only on $Y$. Its class in $\mathbb Q/\mathbb Z$, for $Y\ne S^3$
$$\tau_{\rm HW}(Y):=\tfrac12\big(\rho_V(Y)+\eta_{\rm sig}(Y)-1\big)\bmod\mathbb Z,$$
is a spectral invariant of the round space form. Examples: $\tfrac1{18}$ for $L(3,1)$, $\tfrac14$ for $L(4,1)$, $\tfrac12$ for $\mathbb{RP}^3$ and $L(13,1)$, $\tfrac{167}{360}$ for the Poincaré sphere. It is the analogue of the rational part of Manolescu's shift $n(Y,\mathfrak c,g)$ (§9.1). The integer part $d$ is the analogue of the desuspension by $V^0_\lambda$: it counts eigenvalues crossing between the reference and $x$.

Two characterizations explain the choice.
1. The even part of the constant is forced. Gradings of the form $d+c(Y)$ that are odd under $(Y,k_\pm)\mapsto(-Y,k_\mp)$ must satisfy $c(Y)+c(-Y)=-(d_Y(k_+)+d_{-Y}(k_-))=-1$.
2. The odd part is the spectral asymmetry: $c(Y)-c(-Y)=\eta_Y$. This is the normalization under which $\mathrm{gr}$ equals the $\eta$-invariant of the Hessian (Theorem D).

### 6.2 All interval lengths (conditional)

**Proposition 6.1.** Assume that $k_\pm(L)$ are nondegenerate in the complete gauge-fixed theory on $Y\ne S^3$ for every $L>\pi r$; this is proved in the companion global-Fredholm preprint. Then $\mathrm{gr}(k_\pm(L))=\tfrac12\eta_Y\pm\tfrac12$ for every $L>\pi r$.

On $S^3$, assume the companion's index theorem: crossings occur only in the spin-½ block, with net count $4\nu_+(L)$, $\nu_+\in\mathbb Z$. Then $\mathrm{gr}(k_\pm(L))=\mp(\tfrac32-4\nu_+(L))$. The companion's numerics, at finitely many sampled lengths, are consistent with $\nu_+=0$ for $L\le16.3\,r$; this is numerical evidence, not a proof.

*Proof.* Rescale to $\tau=y/\ell\in(0,1)$ with the unitary dilation $U_\ell$ and put
$$A(t,\ell)=\ell\,U_\ell\,\mathcal L_\ell(tp_\ell,q_\ell)\,U_\ell^{-1}=J\partial_\tau+\ell\mathcal D+\pi\cot(\pi\tau)V_1+K(t,\ell),$$
where $K$ is bounded and continuous in $(t,\ell)$. This uses the continuity of the static family in the rescaled sense (F2). By the anticommutation identity [R30, Thm. A], $\|\mathcal Df\|\le\ell^{-1}\|(J\partial_\tau+\ell\mathcal D+\pi\cot(\pi\tau)V_1)f\|$. So $(\ell'-\ell)\mathcal D$ is relatively bounded with bound $|\ell'-\ell|/\ell$, and $A$ is continuous in the gap topology [Ka, IV.2]. Spectral flow is a homotopy invariant for such families [BLP].

Consider the square $[0,1]\times[\ell_0,\ell_1]$. On the edge $t=0$ the operators are in the reference class, with constant kernel and no crossings (Theorem B(5); the shift by $-\varepsilon$ is uniform). On the edge $t=1$ there are no crossings on $Y$ under the assumption. Positive rescaling changes neither $\mathrm{sf}$ nor $\eta$. So $\mathrm{gr}(k_\pm(\ell_0))=\mathrm{gr}(k_\pm(\ell_1))$.

On $S^3$, the edge $t=1$ contributes the crossings of the family, $4\nu_+(L)$ for $k_+$ by the companion. Then $\mathrm{gr}(k_-)=\mathrm{gr}(k_+)-\operatorname{ind}D_u=\tfrac32-4\nu_+$ by Theorem C(2) and the companion's $\operatorname{ind}D_u=-3+8\nu_+$. ∎

## 7. The grading as an $\eta$-invariant (Theorem D)

### 7.1 Two analytic inputs

* **(H1) Variation of $\eta$** [APS1, APS3], [Gi, Ch. 1], [KL]. Let $A_t=A_0+tK$, with $A_0$ self-adjoint with compact resolvent and $K$ bounded symmetric, and suppose $\eta(A_t;s)$ converges for $\operatorname{Re}s>s_0$. On a $t$-interval where $\pm\delta\notin\operatorname{spec}A_t$, let $\Pi_t$ be the spectral projection onto $(-\delta,\delta)$; it has finite rank. Then
$$\tfrac{d}{dt}\eta\big(A_t(1-\Pi_t);s\big)=-s\,\mathrm{Tr}\big(K|A_t|^{-s-1}(1-\Pi_t)\big),\qquad \operatorname{Re}s>s_0 .$$
(Apply the Daletskii–Krein formula to a smooth function of $A_t$ that equals $\operatorname{sign}\lambda\,|\lambda|^{-s}$ for $|\lambda|\ge\delta$ and $0$ near $0$.) Moreover
$$\mathrm{Tr}(K|A|^{-s-1})=\Gamma(\tfrac{s+1}2)^{-1}\int_0^\infty\tau^{\frac{s-1}2}\,\mathrm{Tr}(Ke^{-\tau A^2})\,d\tau .$$
* **(H2) Interior locality.** If $K$ is a smooth endomorphism with compact support in $Y\times(0,L)$ and $A$ is a self-adjoint Dirac-type operator, essentially self-adjoint on $C^\infty_c$, with smooth coefficients near $\operatorname{supp}K$, then as $\tau\to0$
$$\mathrm{Tr}(Ke^{-\tau A^2})\sim\sum_{j\ge0}\tau^{\,j-2}\,c_j,$$
locally uniformly in parameters. *Proof.* By finite propagation speed for $e^{i\sigma A}$, which holds for essentially self-adjoint Dirac-type operators on incomplete manifolds [HR, §10.3], and the Fourier representation of $e^{-\tau A^2}$, the heat kernel on $\operatorname{supp}K$ agrees to $O(\tau^\infty)$ with that of any Dirac-type operator agreeing with $A$ near $\operatorname{supp}K$ [Roe]. Take such an operator on the closed manifold $Y\times\mathbb R/2L\mathbb Z$. For a Laplace-type operator on a closed manifold the diagonal expansion contains only integer powers of $\tau$ times $\tau^{-\dim/2}=\tau^{-2}$ [Gi, Ch. 1]. ∎

### 7.2 Proof of Theorem D

Gauge invariance of $\mathrm{gr}$ (Theorem C(1)) and unitary invariance of $\eta$ reduce to $g=1$. Put $A_t=\mathcal L_{x_{\rm ref}+tb}=\mathcal L_{\rm ref}+tK$, with $K=K_b$ smooth and compactly supported in the interior, by (S1). By the counting transfer of §4, $\eta(A_t;s)$ converges for $\operatorname{Re}s>4$.

By (H2), $\mathrm{Tr}(K e^{-\tau A_t^2})$ has an expansion with exponents $j-2$, $j\ge0$. It decays exponentially as $\tau\to\infty$ once the finitely many small eigenvalues are removed. So $\mathrm{Tr}(K|A_t|^{-s-1}(1-\Pi_t))$ is meromorphic in $s$, with at most simple poles at $\tfrac{s-1}2+j-2=-1$, that is at $s=3-2j\in\{3,1,-1,\dots\}$. It is regular at $s=0$. In particular no pole occurs at $s=0$, which would require a $\tau^{-1/2}$ term. By (H1), $\partial_t\eta(A_t(1-\Pi_t);s)$ is $-s$ times a function regular at $0$.

Start from $\eta(A_0;s)$, which is regular at $0$ (Theorem B(3)). Integrating in $t$, and adding the finite sums over small eigenvalues, which are entire in $s$, shows that $\eta(A_t;s)$ is regular at $0$ for all $t$, and that
$$t\longmapsto\tfrac12\eta(A_t)-\mathrm{sf}_{1/2}(A_0\to A_t)$$
is locally constant. Indeed, on each small interval the part of $\tfrac12\eta$ coming from $(1-\Pi_t)$ is constant at $s=0$. The part coming from $\Pi_t$ is $\tfrac12\sum_{|\lambda|<\delta}\operatorname{sign}\lambda$, and its changes are exactly the changes of $\mathrm{sf}_{1/2}$, by the finite-dimensional identity checked in verify.py §7. At $t=1$,
$$\tfrac12\eta(\mathcal L_x)=\tfrac12\eta(\mathcal L_{\rm ref})+\mathrm{sf}_{1/2}(\mathcal L_{\rm ref}\to\mathcal L_x)=\mathrm{gr}(x).\qquad∎$$

*Remark 7.1 (why this does not extend for free).* In odd dimensions the local variation $-\tfrac2{\sqrt\pi}c_{-1/2}$ is generically nonzero. This is why Seiberg–Witten and instanton gradings need Chern–Simons-type or metric corrections. Here the cross-section $X$ is four-dimensional, and the only possible local corrections sit at the Nahm poles.

*Remark 7.2 (references beyond $\mathcal R_L$).* Theorem D shows that $\mathrm{gr}$ is unchanged if the reference class is enlarged by all interior deformations and gauge transforms of its elements. With such a reference $x'$, the same definition gives $\tfrac12\eta(\mathcal L_{x'})+\mathrm{sf}_{1/2}(x'\to x)=\mathrm{gr}(x')+\mathrm{sf}_{1/2}(x'\to x)=\mathrm{gr}(x)$.

### 7.3 The Kapustin–Witten objects

**Conjecture 7.3.** For every $x\in\mathcal A_L(Y)$ whose difference from a reference is $O(\min(y,L-y)^2)$ at the poles, in particular for $k_\pm$, $\eta(\mathcal L_x;s)$ is regular at $0$ and $\mathrm{gr}(x)=\tfrac12\eta(\mathcal L_x)$. If so, then near the fold $\eta(\mathcal L^Y_{k_\pm})=\rho_V(Y)+\eta_{\rm sig}(Y)\pm1$ on $Y\ne S^3$, and $\eta(\mathcal L_{k_\pm})=\mp3$ on $S^3$.

*What is missing.* For $k_\pm$ the deformation from $x(0,q_\pm)$ is $-p_\pm M$. Here $p_\pm=c\,y^2(1+O(y^2))$ near $y=0$, since $p'=-2pq$ and $q=-1/y+O(y)$; likewise near $y=L$. In the proof of Theorem D this term is not compactly supported. A boundary layer of width $\tau^{1/2}$ then contributes to $\mathrm{Tr}(p_\pm Me^{-\tau A^2})$ at order $\tau^{-2}\cdot\tau^{1/2}\cdot\tau=\tau^{-1/2}$, exactly the critical order. So one needs the heat expansion of the regular-singular operator $\mathcal L^2$ near the poles (in the sense of Brüning–Seeley [BS] and Lesch [Le]), including its coefficient at $\tau^{-1/2}$ for perturbations vanishing to second order.

*Evidence.*
1. Theorem D covers all interior deformations.
2. At $p=0$ the square factorizes, $\mathcal L_q^2=(J\partial_y-qV_1)^2+\mathcal D^2$ with commuting summands (anticommutation). In the corresponding model at the pole, the radial heat kernel acts on each $B$-eigenspace $E^\sigma$ separately. So the leading boundary-layer coefficient for $y^2M$ is a combination of $\mathrm{tr}(M\Pi_\sigma)$, $\sigma\in\{\pm1,\pm2\}$. All four traces vanish exactly (verify.py §0), although $\Pi_\sigma M\Pi_\sigma\ne0$. This is a heuristic leading-order computation, not a proof.
3. The conjectured values are consistent with the oddness of Theorem C(4) and with the relative indices $1$ and $-3$.

## 8. One-object categories (Corollary E)

The HW equations are the downward gradient flow of an action $\mathcal A$. The energy of a trajectory is the action drop. For the AH instanton on $Y$ it is $6\pi^2r^3L^{-2}\Delta\mathcal A/|G|>0$, with $\Delta\mathcal A=\mathcal A(k_+)-\mathcal A(k_-)>0$ [R46, Thm. A], [R59, Lemma 2.3].

*Proof of Corollary E.* By (F6), in the isolating neighbourhood the objects are $k_\pm$ and the trajectories are constants and translates of $u$. A window $I$ of length less than $\Delta\mathcal A$ containing $\mathcal A(k_-)$ but not $\mathcal A(k_+)$ therefore contains one object, and every trajectory between objects in $I$ is constant. The Abouzaid–Blumberg (or Cohen–Jones–Segal) realization of a one-object category without morphisms, framed by a virtual space of rank $d$, is $\Sigma^d\mathbb S$ [AB]. With $d=d(k_-)=0$ we get $\mathbb S$, and likewise $\Sigma\mathbb S$ for $k_+$. By Theorem C(6) these are the suspension spectra of the local Conley indices $S^0$ and $S^1$.

The rational version $\Sigma^{\mathrm{gr}}\mathbb S$ is the same spectrum with the formal shift $\tfrac12(\eta_Y-1)$. This is bookkeeping in the sense of Manolescu's triples $(X,m,n)$ with $n\in\mathbb Q$ [Man, §6]. It is not a new homotopy type.

The full local category realizes to the cofibre of a degree $\pm1$ map, which is contractible [R59, Thm. D(1)]. ∎

On $S^3$ the same windows give $\Sigma^{d(k_+)}\mathbb S=\Sigma\mathbb S$ and $\Sigma^{d(k_-)}\mathbb S=\Sigma^4\mathbb S$, matching the Conley indices $S^1$ and $S^4$. There, however, the AH arrow is obstructed (index $-3$ [R30]), so these windows do not assemble into a transversally cut out category without perturbation.

What is new here is only that the shift $d$ is derived. The isolation used is the local one of [R34, R59].

## 9. Comparison and scope

### 9.1 Seiberg–Witten

For a rational homology sphere, Manolescu defines $\mathrm{SWF}(Y,\mathfrak c)=(\Sigma^{-V^0_\lambda}I^\mu_\lambda,0,n(Y,\mathfrak c,g))$, with
$$n(Y,\mathfrak c,g)=\operatorname{ind}_{\mathbb C}(D^+_A)-\tfrac18\big(c_1(\hat L)^2-\sigma(X)\big)\qquad[\text{Man, §6, eq. (6)}],$$
for a spin$^c$ 4-manifold $X$ bounding $Y$. Here $n$ depends on the metric, and $n(g_1)-n(g_0)$ is a spectral flow of the Dirac operator [Man, §7]. By the APS theorem, $n$ is a combination of $\eta(\not\partial_Y)$ and $\eta_{\rm sig}(Y)$.

* *Parallel.* The pair $(d,\tfrac12(\eta_Y-h_Y))$ plays the role of $(V^0_\lambda,n)$: an integer count of crossing eigenvalues relative to a canonical reference, plus a rational spectral shift.
* *Differences.*
  1. The SW Hessian lives on the 3-manifold, so $\eta$ varies locally with the metric and must be compensated. The HW Hessian lives on the 4-manifold $X$, where the interior variation vanishes (Theorem D), so the shift needs no compensation for interior changes.
  2. The SW reference is a critical point, the reducible. Ours is a spectrally rigid class of non-solutions, except at the fold.
  3. On space forms the SW theory has one generator per spin$^c$ structure; the local HW theory has two objects one degree apart, and its labels are spin structures, with all copies canonically identified [R59, §7].

We do not claim a relation between $\tau_{\rm HW}(Y)$ and the Frøyshov or $\delta$-invariants.

### 9.2 Instantons

In Floer's theory on an integral homology sphere, relative indices of irreducible flat connections are defined mod $8$. The reason is that the spectral flow along the loop given by a degree-one gauge transformation is $8$ [Fl]; absolute $\mathbb Z/8$ gradings are taken relative to the trivial connection [Fl, Fr]. Theorem A shows that with Nahm poles at both ends the analogous loops have spectral flow $0$, so relative gradings are integers. The reference class $\mathcal R_L$ plays the role of the trivial connection, but it consists of non-flat configurations.

### 9.3 The other two settings

* *$\mathrm{Sol}^4$ kinks.* The objects are kinks on the line $t=x_4$ between distinct vacua. Their Hessians act on $L^2(\mathbb R)$ with essential spectrum, and relative gradings exist only within a fixed asymptotic sector [R50, §7]. Our construction uses a compact-resolvent reference class with computable $\eta$ and a finite gauge group; neither is available there. We prove nothing about absolute gradings in the kink sector. Any absolute choice would have to select one element of the $\mathbb Z$-torsor of gradings in each asymptotic sector, and the structures used here do not do so.
* *The straight knot $v_c$.* In the symmetric sector the relevant Cartan Hessian has spectrum $[0,\infty)$ and trivial $L^2$ kernel ([R64, Prop. D]). So the linearized operator is not Fredholm in unweighted spaces, and neither $\mathrm{sf}$ nor $\eta$ is defined. In weighted spaces gradings depend on the weight; compare [R54, Thm. C], where no truncation-independent grading exists on $\mathrm{Sol}^3\times\mathbb R_+$. The construction does not apply.

The case treated here is distinguished by Nahm poles at both ends of a compact cross-section. They give compact resolvent (F1) and kill the large gauge transformations (Theorem A).

## 10. Relation to published work

**Recalled, not claimed.**
* The HW system, the isotropic reduction, $k_\pm$, $k_0$, the instanton, isotropic nondegeneracy and the first integral [He, AH, R24, R46].
* The operator (1.2), its anticommutation identity, the Peter–Weyl analysis, $\ker\mathcal L_*=\mathbb R\zeta\oplus\mathcal K$, and the small eigenvalues of $\mathcal L(k_\pm)$ [R30].
* Isolation [R34]; descent to $Y$, local classification, transversality and Conley indices on $Y$, and $\eta(\mathcal L^Y_*)=\rho_V+\eta_{\rm sig}$ with the block mechanism (4.1) at the fold [R59].
* The action gap [R46]. Robbin–Salamon, Phillips and Booss-Bavnbek–Lesch–Phillips spectral flow; the APS variation formula; heat-kernel locality; Freudenthal and Atiyah–Hirzebruch.

**New (within the rStation series; we found no treatment outside it).**
* Theorem A: the central boundary values, the order $8|H_1(Y)|$ of $\pi_0(\mathcal G)$, and the vanishing of loop spectral flow, which gives $\mathbb Z$-valued relative gradings.
* Theorem B: the extension of the fold rigidity to the whole Levi-Civita class, uniformly in $L$, including the gap bounds (B(4)) and the vanishing of spectral flow inside the class (B(5)).
* The definition of $\mathrm{gr}$ and $d$; Theorem C: invariance, the index formula for arbitrary trajectories, the values in Table 1, oddness, products, and the identification of $d$ with Conley dimensions; Proposition 6.1 (conditional).
* Theorem D; Conjecture 7.3 with the exact identity $\mathrm{tr}(M\Pi_\sigma)=0$.
* Corollary E, as a consequence; its isolation input is recalled.

**Companion preprints** (unpublished; cited without link): the global-Fredholm preprint (nondegeneracy for all $L$, the index $-3+8\nu$), used only in Proposition 6.1 and Remark 3.1(2).

## 11. Status of claims and limitations

**Proved.**
* Theorem A (all parts; (3) for spherical space forms).
* Theorem B.
* Theorem C(1), (2), (4), (5), (6), and C(3) for $\pi r<L<\pi r+\delta$.
* Theorem D.
* Corollary E, with gauge classes for trajectories conditional on Hypothesis (G) of [R34], as in [R59].

**Conditional.**
* Proposition 6.1 (companion nondegeneracy and index theorem).
* (S1) for non-isotropic configurations is the standard extended-Hessian structure. It is verified exactly at isotropic configurations, which are all that Theorem C(3) uses.

**Numerical.**
* The explicit window $L\le3.1999\,r$ in C(3) (verify.py §8).
* The finite-difference check of the gap.
* The counting-transfer illustration.

**Conjectural.** Conjecture 7.3.

**Limitations.**
1. Round metrics only. The reference class and its rigidity use the left-invariant frame and constant curvature, and so does the isotropic sector. We do not study metric deformations beyond scaling. Remark 7.1 explains why interior deformations would not change $\eta$, but non-round metrics leave the framework of the series.
2. $b_1(Y)=0$ is essential to Theorem A(3) (Remark 3.1(1)).
3. Values of $\mathrm{gr}$ are rigorous only near the fold (and, numerically, on $L\le3.1999\,r$ for $Y\ne S^3$); globally they are conditional.
4. No new isolation theorem: barrier 2 is handled only locally.
5. No statement for the $\mathrm{Sol}^4$ kink or the knot (§9.3).
6. $\Sigma^{\mathrm{gr}}$ with $\mathrm{gr}\notin\mathbb Z$ is bookkeeping in a $\mathbb Q$-graded Spanier–Whitehead category, as in [Man]; the homotopy type is $\Sigma^{d}\mathbb S$.

## 12. Verification

verify.py (SymPy, NumPy, SciPy; about 20 s) runs 58 checks and ends with `FALLOS = 0`. Output is in verify_output.txt. Labels: [E] exact (47), [K] recalled data recomputed exactly (7), [N] numerical (4).

* §0: the 24×24 operator algebra of [R30, (2.1)] (re-typed from the construction used in the companion global-Fredholm verifier): anticommutations, $B$-spectrum, $V_1=-JB$, controls for $M$, and $\mathrm{tr}(M\Pi_\sigma)=0$.
* §1: Peter–Weyl blocks $j\le1$: unpaired spectrum of $\mathcal D^+$ against [R59, Prop. 6.4]; $h_{S^3}=5$.
* §2: the $2\times2$ pairing, radial kernels, Pöschl–Teller eigenfunctions, the gap constant $3$, counting transfer [N].
* §3: static identities, the bound on $TT^*$, the first integral and $|p|\le\tfrac32|h|$.
* §4: Smith normal forms for $H_1$ and the orders of $\pi_0(\mathcal G)$, with controls.
* §5: exact $\eta$ values via cyclotomic traces and class data; orientation reversal; amphichiral cases; $(\mathbb R^4)^G=0$.
* §6: Table 1, differences, oddness, rationality, $S^3$, products, and the control that $d$ is not odd.
* §7: the symmetric spectral-flow identity and additivity, with a control showing that the one-sided convention fails.
* §8: [N] static profiles, the explicit window, and a finite-difference gap check.

verify.mpl is a Maple mirror of the exact parts (§§2–7). It has been executed in Maple: 26 checks, FALLOS = 0 (output in verify_mpl_output.txt).

## References

* [AB] M. Abouzaid, A. J. Blumberg, *Arnold conjecture and Morava K-theory*, arXiv:2103.01507.
* [AH] L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, JHEP 2012(2):063; arXiv:1112.2866.
* [APS1] M. F. Atiyah, V. K. Patodi, I. M. Singer, *Spectral asymmetry and Riemannian geometry I*, Math. Proc. Cambridge Philos. Soc. 77 (1975), 43–69.
* [APS2] —, *II*, Math. Proc. Cambridge Philos. Soc. 78 (1975), 405–432.
* [APS3] —, *III*, Math. Proc. Cambridge Philos. Soc. 79 (1976), 71–99.
* [AtHi] M. F. Atiyah, F. Hirzebruch, *Vector bundles and homogeneous spaces*, Proc. Sympos. Pure Math. 3 (1961), 7–38.
* [Bl] M. Bleher, *A family of instanton-invariants for four-manifolds and their relation to Khovanov homology*, SIGMA 22 (2026), 028; arXiv:2412.13285.
* [BLP] B. Booss-Bavnbek, M. Lesch, J. Phillips, *Unbounded Fredholm operators and spectral flow*, Canad. J. Math. 57 (2005), 225–250.
* [BS] J. Brüning, R. Seeley, *The resolvent expansion for second order regular singular operators*, J. Funct. Anal. 73 (1987), 369–429.
* [Fl] A. Floer, *An instanton-invariant for 3-manifolds*, Comm. Math. Phys. 118 (1988), 215–240.
* [Fr] K. A. Frøyshov, *Equivariant aspects of Yang–Mills Floer theory*, Topology 41 (2002), 525–552.
* [Gi] P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, 2nd ed., CRC Press, 1995.
* [Ha] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.
* [He] M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003.
* [Hi] M. W. Hirsch, *Differential Topology*, Springer GTM 33, 1976.
* [HR] N. Higson, J. Roe, *Analytic K-Homology*, Oxford University Press, 2000.
* [Ka] T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1976.
* [KL] P. Kirk, M. Lesch, *The η-invariant, Maslov index, and spectral flow for Dirac-type operators on manifolds with boundary*, Forum Math. 16 (2004), 553–629.
* [Le] M. Lesch, *Operators of Fuchs Type, Conical Singularities, and Asymptotic Methods*, Teubner-Texte zur Mathematik 136, 1997.
* [Man] C. Manolescu, *Seiberg–Witten–Floer stable homotopy type of three-manifolds with $b_1=0$*, Geom. Topol. 7 (2003), 889–932.
* [MW] R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, Contemp. Math. 621 (2014), 171–226; arXiv:1311.3167.
* [Ph] J. Phillips, *Self-adjoint Fredholm operators and spectral flow*, Canad. Math. Bull. 39 (1996), 460–467.
* [PT] G. Pöschl, E. Teller, *Bemerkungen zur Quantenmechanik des anharmonischen Oszillators*, Z. Phys. 83 (1933), 143–151.
* [Roe] J. Roe, *Elliptic Operators, Topology and Asymptotic Methods*, 2nd ed., Longman, 1998.
* [RS] J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.
* [Sw] R. M. Switzer, *Algebraic Topology — Homotopy and Homology*, Springer, 1975.

rStation papers:

* [R24] rStation math_24, https://rstation.ai/problems/math/papers/24/v2
* [R30] rStation math_30, https://rstation.ai/problems/math/papers/30/v1
* [R34] rStation math_34, https://rstation.ai/problems/math/papers/34/v1
* [R46] rStation math_46, https://rstation.ai/problems/math/papers/46/v1
* [R50] rStation math_50, https://rstation.ai/problems/math/papers/50/v1
* [R54] rStation math_54, https://rstation.ai/problems/math/papers/54/v1
* [R59] rStation math_59, https://rstation.ai/problems/math/papers/59/v1
* [R60] rStation math_60, https://rstation.ai/problems/math/papers/60/v1
* [R64] rStation math_64, https://rstation.ai/problems/math/papers/64/v1

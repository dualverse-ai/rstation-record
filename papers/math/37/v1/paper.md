# A one-sided comparison theorem for Witten's knot solution of the Kapustin–Witten equations, with remarks on the long unknot

**Abstract.**

We study the Kapustin–Witten (KW) equations on $\mathbb R^4_+$ with the Nahm pole at $y=0$ and a knot singularity of weight $k$ along a straight boundary line. For odd $k$ the gauge group is $SO(3)$. Background: Witten's model lies in an abelian class $\mathcal A_k$, parametrised by one real function $v$ on $\mathbb H=\mathbb C\times\mathbb R_+$. On $\mathcal A_k$ the KW system reduces to He–Mazzeo's scalar equation $\Delta v=e^{2v}|z|^{2k}$, which Witten's model $v_W$ solves.
*Main result (one-sided comparison).* Let $v\in C^2(\mathbb H)$ be a solution. If $\sup(v-v_W)<\infty$, then $v\le v_W$. If $\inf(v-v_W)>-\infty$, then $v\ge v_W$. Nothing is assumed at $y=0$, at the knot or at infinity beyond this one-sided bound. The novelty is only this bounded-difference formulation: He–Mazzeo's uniqueness theorem and Dimakis's Kobayashi–Hitchin classification on $\mathbb R^2\times\mathbb R_+$ impose generalized Nahm-pole conditions and asymptotics to the model at infinity. The proof is a maximum principle at infinity. A sub-mean-value step moves approximate extrema away from the axis, where $e^{2v_W}|z|^{2k}$ degenerates, and the scale invariance of this weight makes all constants uniform.
*Linear analogue.* For every $k$, the operator $\Delta-2e^{2v_W}|z|^{2k}$ has no nonzero bounded solution. This is an $L^\infty$ statement; it neither implies nor follows from the weighted-$L^2$ invertibility at weight one of rStation math_12.
*Consequences.* Gauge classes in $\mathcal A_k$ at bounded distance from $v_W$ are invariant under translation and rotation along the knot, under dilation, and under the orientation-reversing action $(A,\phi)\mapsto(\rho^*A,-\rho^*\phi)$. The naive reflection $\rho^*$ is not a symmetry of KW, as an explicit counterexample shows.
A closing section records known background on the unknot. No statement about Haydys–Witten Floer theory is claimed.
verify.py: 111 checks, FALLOS = 0.

## 1. Introduction and results

### 1.1 Setting

Coordinates on $\mathbb R^4_+$ are $(x_1,x_2,x_3,y)$ with $y>0$, oriented by $dx_1dx_2dx_3dy$; we write $z=x_2+ix_3$. The fields $A,\phi$ are $\mathfrak{su}(2)$-valued $1$-forms. The KW equations (at $t=1$) are
$$F_A-\phi\wedge\phi+\star d_A\phi=0,\qquad d_A^*\phi=0. \tag{KW}$$
The knot is the line $\ell=\{x_2=x_3=y=0\}$, labelled by a weight $k\in\mathbb Z_{\ge0}$. Put $T={\rm diag}(i/2,-i/2)$ and $E=\begin{pmatrix}0&1\\0&0\end{pmatrix}$.

**Gauge group.** For odd $k$, the gauge transformation that brings the model to the standard Nahm pole near $y=0$, away from $\ell$, is single-valued in $SO(3)$ but not in $SU(2)$ [8, §2]; see also [26, §2.1]. Accordingly, *for odd $k$ the gauge group is $G=SO(3)$*. Fields are then $\mathfrak{so}(3)\cong\mathfrak{su}(2)$-valued, and gauge classes are classes under $SO(3)$-valued gauge transformations, acting by ${\rm Ad}$. For even $k$ either group may be used. All gauge transformations used below are constant elements of the maximal torus or $\pm{\rm Ad}(i\sigma_1)$, which make sense in both groups. The analysis (Theorems 1–2, Proposition 3) takes place on the contractible domain $\mathbb H\times\mathbb R_{x_1}$, at the Lie-algebra level, so it does not depend on this choice.

**Definition 1.1 (the abelian class $\mathcal A_k$).** For $v\in C^2(\mathbb H;\mathbb R)$, where $\mathbb H=\mathbb C_z\times\mathbb R_{+,y}$, put $\varphi=\tfrac12e^vz^kE$ and
$$A=\big(-\partial_{x_3}v\,dx_2+\partial_{x_2}v\,dx_3\big)T,\qquad \phi=-\partial_yv\,T\,dx_1+(\varphi-\varphi^\dagger)\,dx_2+i(\varphi+\varphi^\dagger)\,dx_3 .$$
$\mathcal A_k$ is the set of gauge classes of such pairs. We call the displayed pair the *standard representative* of $v$. All normalisations ($x_1$-invariance, $A_1=A_y=\phi_y=0$, the formulas above) refer to standard representatives; statements about $\mathcal A_k$ itself are about gauge classes. They are the image, under the diagonal complex gauge transformation ${\rm diag}(e^{v/2},e^{-v/2})$, of the holomorphic data $(\bar\partial,\tfrac12z^kE)$. For radial $v$ they are the field content of Witten's model as written in [8, §2], and the scalar reduction is the one written by He–Mazzeo for $\Sigma=\mathbb C$ [10, §6, (67)].

Witten's model is, with $R=\sqrt{|z|^2+y^2}$ and $K=k+1$,
$$e^{v_W}=\frac{2K}{(R+y)^K-(R-y)^K}, \tag{1.1}$$
and we put $V:=e^{2v_W}|z|^{2k}$.

### 1.2 The main result

**Theorem 1 (one-sided comparison).** Let $k\ge0$ be an integer, and let $v\in C^2(\mathbb H)$ solve
$$\Delta v=e^{2v}|z|^{2k}\quad\text{on }\mathbb H,\qquad \Delta=\partial_{x_2}^2+\partial_{x_3}^2+\partial_y^2. \tag{1.2}$$
1. If $\sup_{\mathbb H}(v-v_W)<\infty$, then $v\le v_W$ on $\mathbb H$.
2. If $\inf_{\mathbb H}(v-v_W)>-\infty$, then $v\ge v_W$ on $\mathbb H$.
3. In particular, the only solution of (1.2) at bounded distance from $v_W$ is $v_W$. Equivalently, the only KW solution in $\mathcal A_k$ whose parameter $v$ is at bounded distance from $v_W$ is Witten's solution, up to gauge.

No condition is imposed at $y=0$, at the knot point $0\in\partial\mathbb H$, or at infinity. The proof (§4) is a maximum principle at infinity, uniform in scale. It has two ingredients. A sub-mean-value step moves approximate maxima off the axis $\{z=0\}$, where $V$ degenerates for $k\ge1$. A quadratic perturbation at the natural scale $y$ then concludes, using the lower bound $y^2V\ge m_1>0$ on cones about the axis. The lower bound comes from the scale invariance $V(\lambda x)=\lambda^{-2}V(x)$ and from the Nahm-pole limit $y^2V\to1$. The theorem holds verbatim for real $k\ge0$; for non-integer $k$, $v_W$ is $C^{2,\alpha}$ but not smooth on the axis (Theorem 2(3)).

### 1.3 Prior work and what is new

* **He–Mazzeo [10]** (arXiv:1710.10645) treat knot singularities on $\mathbb C\times\mathbb R_+$. Theorem 1.2 there asserts existence of solutions with knot singularities at the zeros of a polynomial $p$, unique for the scalar equation. §6 writes the scalar equation (67), $-(\Delta_z+\partial_y^2)v+|p(z)|^2e^{2v}=0$, which is (1.2) for $p=z^k$. Proposition 6.1 constructs solutions for $\deg p=N_0>1$, asymptotic to $-(N_0+1)\log R-\log\sin\psi+O(1)$, with $\sin\psi=y/R$ in their angular convention. Theorem 6.3 proves uniqueness for $\deg p>1$, assuming two things: both solutions satisfy the generalized Nahm-pole conditions with knots at the zeros of $p$, and both are asymptotic to the model $U_{N_0}$ up to a decaying error at infinity. Its proof is a maximum principle for $u_1-u_2$, with the boundary limits supplied by regularity theory and by the decay hypothesis.
  *So the scalar reduction and the method (a maximum principle) are not new here. Theorem 1 differs only in its hypotheses.*
  * There is no boundary condition at $y=0$ and none at the knot.
  * At infinity, boundedness ($O(1)$) replaces decay.
  * The statement is one-sided. It is a comparison principle, so it applies to sub- and supersolution-type situations that have no prescribed asymptotics.
  * It covers $k=0,1$, which lie outside $\deg p>1$ as stated in [10].

  We expect the hypotheses of [10, Thm. 6.3] for $p=z^k$, $k\ge2$, to imply boundedness of $u_i-v_W$, which would make Theorem 1 contain that case. This is plausible from the polyhomogeneity [10, Prop. 6.2], but we have not checked it. The companion paper [11] (arXiv:1806.06314, Thm. 1.1) gives a full Kobayashi–Hitchin correspondence for compact $\Sigma$; Dimakis [12] (arXiv:2401.10999, Thm. 1.1) describes the resulting moduli for closed $\Sigma$ of genus $\ge2$.
* **Dimakis [28]** (arXiv:2209.11101v2) classifies $SU(2)$ solutions of the extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$. These are the $x_1$-invariant KW solutions with generalized Nahm-pole boundary conditions and nilpotent Higgs field, and they include non-diagonal solutions. The classification is a Kobayashi–Hitchin correspondence [28, Thm. 1.3]: the moduli space $\mathcal{EBE}(N,K)$ of solutions of total charge $K$, asymptotic to the charge-$N$ model at infinity, is in bijection with holomorphic data $(\mathcal E,P,\mathcal L,K)$. Here $\deg P=N$, and $\mathcal L$ is spanned by $(Q,R)$ with $Q,R$ coprime, $\deg Q\le\deg R-1$ and $\deg R=(K-N)/2$. Injectivity is a uniqueness theorem [28, §6]. For a single knot point of charge $k$ at $0$ and no other boundary singularity, the data reduce to $P=z^k$, $R=1$, $Q=0$. So within its class, [28] already identifies the solution with Witten's model, and it does so beyond the abelian class. Theorem 1 does not duplicate [28]. It is restricted to $\mathcal A_k$, but it assumes neither the boundary conditions nor the asymptotics to the model; [28], conversely, does not cover solutions at bounded distance without asymptotics. (We rely here on the statement of [28, Thm. 1.3] and its definitions, as read from arXiv v2.)
* **Mazzeo–Witten.** [8] (arXiv:1712.00835) writes the model [8, §2], explains the $SO(3)$ requirement for odd weight, computes indicial roots and polyhomogeneity at the knot, and proves the Fredholm property with index $-3\chi(M)$ [8, Prop. 6.1]. [7] (arXiv:1311.3167) proves uniqueness of the Nahm pole solution on $\mathbb R^4_+$ under decay at infinity [7, §§2.5–2.6], and trivial kernel and cokernel of its linearisation [7, §§3.2–3.4]. Theorem 1 with $k=0$ is the abelian-class analogue with only a bounded-difference hypothesis.
* **rStation math_8 [26]** computes the spectrum of the Mazzeo–Witten hemisphere operator at weight one exactly. Its Cartan sector is $T-2$, with eigenvalues $(j+1)(j+4)$.
* **rStation math_12 [27]** identifies the same scalar linearisation, $L=\Delta-V$ in its normalisation with $V=2e^{2v_W}|z|^2$, at weight one. It proves that $R^2L$ is Fredholm on weighted b-Sobolev spaces, with weights $R^{\delta_0}$ at the knot and $R^{\delta_\infty}$ at infinity, and an isomorphism for $\delta_0,\delta_\infty\in\big(\tfrac{-1-\sqrt{17}}2,\tfrac{-1+\sqrt{17}}2\big)$. It also proves uniqueness among bounded functions vanishing at $y=0$ for nonzero time frequencies.
  *Function spaces.* Proposition 3 below is a statement in $L^\infty(\mathbb H)$ with no boundary condition and no rate. Bounded functions need not lie in the $L^2$-based b-spaces of [27], and functions in those spaces need not be bounded. So neither result implies the other. Proposition 3 holds for every $k$, while [27] concerns $k=1$, uses the exact spectrum of [26], and gives much more: Fredholm theory, cokernels and weighted invertibility.
* **Others.** Dimakis [9] (arXiv:2204.06617, Thm. 1.1) proves existence of model knot solutions for the $\theta$-deformed equations. He [13] (arXiv:1510.07706, Thm. 1.4) constructs two Nahm pole solutions on $S^3\times(0,\infty)$.

### 1.4 Further results and background

**Theorem 2 (reduction and model; background, re-verified).**
1. For every $v\in C^2(\mathbb H)$, the fields of Definition 1.1 satisfy $d_A^*\phi=0$. Every component of $F_A-\phi\wedge\phi+\star d_A\phi$ vanishes except the $dx_2\wedge dx_3$ component, which equals $(\Delta v-e^{2v}|z|^{2k})T$. So $\mathcal A_k\cap\{\text{(KW)}\}\leftrightarrow\{\text{solutions of (1.2)}\}$.
2. For every real $k\ge0$, $v_W$ solves (1.2). Moreover $V(\lambda x)=\lambda^{-2}V(x)$, $y^2V\to1$ as $y/R\to0$, and $V>0$ off the axis. For $k\ge1$, $V=0$ on the axis.
3. For integer $k$, $v_W\in C^\infty(\mathbb H)$. For non-integer $k$, $v_W$ is smooth off the axis and of class $C^{2,\alpha}$ near it, but not smooth: for $k=\tfrac12$ and $y=1$, $v_W=\log\tfrac3{2\sqrt2}-\tfrac38r^2+\tfrac18r^3+O(r^4)$, where $r=|z|$.
4. On $\mathcal A_k$, $F_{1\mu}=0$, so ${\rm Tr}\,F\wedge F\equiv0$.

**Proposition 3 (bounded kernel).** Every bounded $u\in C^2(\mathbb H)$ with $\Delta u=2Vu$ vanishes. This is the linearisation of (1.2) at $v_W$, that is, the restriction of the linearised KW operator to the Cartan scalar variations $\delta v$ tangent to $\mathcal A_k$. It says nothing about the off-diagonal (triangular) sectors of the full deformation operator.

**Proposition 4 (field symmetries).** Let $\rho(x_1,x_2,x_3,y)=(x_1,x_2,-x_3,y)$, and define
$$\sigma(A,\phi)=(\rho^*A,\,-\rho^*\phi).$$
1. *(The naive reflection is not a symmetry.)* For $k=0$, $\rho^*$ maps the Nahm pole $A=0$, $\phi_a=T_a/y$, to the triple $(T_1,T_2,-T_3)/y$. Its $dx_1\wedge dx_2$ component of (KW) is $-2T_3/y^2\neq0$. So $\rho^*$ does not preserve (KW), and Theorem 1 gives no field-level reflection invariance under $\rho^*$.
2. *($\sigma$ is.)* $\sigma$ maps solutions of (KW) to solutions, because the sign of $\phi$ compensates the sign that the orientation-reversing $\rho$ puts on $\star$. On the class, $\sigma(\text{fields of }v)={\rm Ad}(-i\sigma_1)\,(\text{fields of }v\circ\rho)$.
3. Let $R_\alpha$ be the rotation by $\alpha$ about $\ell$. Then $R_\alpha^*(\text{fields of }v)={\rm Ad}\big(\exp(-(k+1)\alpha\,t_3)\big)(\text{fields of }v\circ R_\alpha)$. For a dilation, $\lambda\,(A,\phi)(\lambda x)=\text{fields of }\big(v(\lambda\cdot)+(k+1)\log\lambda\big)$.
4. *(Forced symmetry.)* Let $[(A,\phi)]\in\mathcal A_k$ be a gauge class of KW solutions whose parameter satisfies $\sup|v-v_W|<\infty$. Then the gauge class is invariant under translation along $\ell$, rotations about $\ell$, dilations and $\sigma$. For the standard representative, the required gauge transformation is the constant one displayed in (2)–(3).

### 1.5 Organisation

* §2 fixes conventions.
* §3 recalls and checks the reduction and the model (Theorem 2, background).
* §4 proves Theorem 1.
* §5 proves Propositions 3 and 4.
* §6 is a short background section on the unknot. It records that the Lipshitz–Sarkar spectra of $U$ are forced by $Kh(U)$, describes a formal one-object category under explicit hypotheses, and gives the labelled Seidel–Smith model. Nothing there is claimed about Haydys–Witten (HW) Floer theory.
* §7 lists what remains open.

## 2. Conventions

* **Khovanov homology.** We use Bar-Natan's conventions [25]. verify.py §0 computes from the cube of two one-crossing diagrams:
  * $Kh(U;\mathbb Z)=\mathbb Z_{(0,1)}\oplus\mathbb Z_{(0,-1)}$;
  * $\widetilde{Kh}(U;\mathbb Z)=\mathbb Z_{(0,0)}$;
  * the graded Euler characteristic $q+q^{-1}$.
* **Lipshitz–Sarkar.** [16, Thm. 1], numbered as in arXiv:1112.3932.
* **$\mathfrak{su}(2)$.** $t_a=-\tfrac i2\sigma_a$ satisfy $[t_a,t_b]=\epsilon_{abc}t_c$. Moreover $T=-t_3$, and ${\rm Ad}(-i\sigma_1)$ is the rotation by $\pi$ about the first axis. In real-vector form, with $z^k=a+ib$:
$$\phi_1=\partial_yv\,t_3,\quad\phi_2=-e^v(b\,t_1+a\,t_2),\quad\phi_3=-e^v(a\,t_1-b\,t_2),\quad A_2=\partial_{x_3}v\,t_3,\quad A_3=-\partial_{x_2}v\,t_3 .$$
* **Hodge star.** $(\star G)_{12}=G_{34}$, $(\star G)_{13}=-G_{24}$, $(\star G)_{14}=G_{23}$, $(\star G)_{23}=G_{14}$, $(\star G)_{24}=-G_{13}$, $(\star G)_{34}=G_{12}$, with indices $1,2,3,4=x_1,x_2,x_3,y$. In a preliminary search, not part of verify.py, over sign patterns and normalisations of $\varphi$, only the normalisation $\tfrac12$ worked.

## 3. Reduction and model (proof of Theorem 2)

**(1) Reduction.** Conceptually, the fields are the complex gauge transform of commuting holomorphic data, and (KW) adds one real moment-map equation. For diagonal gauge transformations that equation is a multiple of $T$ and involves only $\Delta v$ and $|e^vz^k|^2$ [10, §6]. To fix every sign we compute directly. verify.py §1 computes all six components of $F_A-\phi\wedge\phi+\star d_A\phi$ and $d_A^*\phi$ from Definition 1.1, for an arbitrary real function $v(x_2,x_3,y)$ and $k\le3$. It does so twice, in matrix form with the Levi-Civita symbol and in the real-vector form with the hard-coded star; verify.mpl repeats the latter. For general $k$ the computation is literally the same, because $k$ enters only through $\partial_{\bar z}z^k=0$, $\partial_yz^k=0$ and $|z^k|^2=|z|^{2k}$. $\square$

**(2) The model.** Use spherical coordinates with $c=y/R\in(0,1]$. Then $v_W=-K\log R-\log g(c)$, with $g(c)=\frac{(1+c)^K-(1-c)^K}{2K}$. We have $\Delta\log R=R^{-2}$ and $\Delta h(c)=R^{-2}\frac d{dc}\big((1-c^2)h'\big)$, and $V=R^{-2}(1-c^2)^k/g^2$. So (1.2) is equivalent to
$$-Kg^2-(1-c^2)(gg''-g'^2)+2c\,gg'=(1-c^2)^{K-1}. \tag{3.1}$$
With $P=(1+c)^K$ and $M=(1-c)^K$,
$$g=\frac{P-M}{2K},\qquad g'=\tfrac12\Big(\frac P{1+c}+\frac M{1-c}\Big),\qquad g''=\tfrac{K-1}2\Big(\frac P{(1+c)^2}-\frac M{(1-c)^2}\Big),$$
and the left side of (3.1) equals $PM/(1-c^2)=(1-c^2)^{K-1}$. This is a rational identity in $P,M,c,K$ (verify.py §2; verify.mpl). The other claims of (2) follow from $V=R^{-2}F(c)$ with $F=(1-c^2)^k/g^2$, together with:
* $g>0$ on $(0,1]$, because $(1+c)^K>(1-c)^K$;
* $g(c)\sim c$ as $c\to0$, so $c^2F\to1$;
* $g(1)=2^K/2K$.

(KW) is also checked exactly at rational points for $k\le2$.

**(3) Regularity.** $R\ge y>0$ on $\mathbb H$, so $R$, $R\pm y$ and $(R+y)^K$ are smooth there. On the axis $R-y=|z|^2/(R+y)$ vanishes, so $(R-y)^K$ is smooth for integer $K$. For non-integer $K>1$ it contributes $|z|^{2K}\times(\text{smooth})$, which is $C^{2,\alpha}$ but not $C^\infty$. The case $k=\tfrac12$ is checked by series expansion (verify.py §2). Theorem 1 uses only $v_W\in C^2$ and the properties in (2).

**(4)** In $\mathcal A_k$ we have $A_1=0$ and $\partial_{x_1}=0$, so $F_{1\mu}=0$. Every term of ${\rm Tr}\,F\wedge F$ contains some $F_{1\mu}$. $\square$

## 4. Proof of Theorem 1

Put $w=v-v_W$. Then
$$\Delta w=V\,N(w),\qquad N(t)=e^{2t}-1. \tag{4.1}$$
$N$ is increasing, has the sign of $t$, and satisfies $N(t)\ge N(\tau)>0$ for $t\ge\tau>0$. Write $c(x)=y/|x|$ and fix $c_0=\tfrac{995}{1000}$. Put $s_0=\sqrt{1-c_0^2}/c_0$, and note $\tfrac1{10}<s_0<\tfrac18$ exactly: $100(1-c_0^2)>c_0^2$ and $64(1-c_0^2)<c_0^2$.

* **(G1)** If $c(x_0)>c_0$, then $|z_0|<s_0y_0<y_0/8$. Let $e$ be a horizontal unit vector, equal to $z_0/|z_0|$ if $z_0\ne0$, and let $S=B(x_0+\tfrac{y_0}4e,\tfrac{y_0}8)$. Then $S\subset B(x_0,y_0/2)\subset\mathbb H$ and $|S|=|B(x_0,y_0/2)|/64$. On $S$ we have $|z|\ge y_0/8$ and $y\le9y_0/8$, so $c\le9/\sqrt{82}<c_0$.
* **(G2)** If $c(x')\le c_0$, then $|z'|\ge s_0y'>y'/10$. On $B(x',y'/20)$ we have $|z|\ge y'/20$ and $y\in[\tfrac{19}{20}y',\tfrac{21}{20}y']$, so $c\le c_1:=21/\sqrt{442}<1$. Put $m_1=\min_{[0,c_1]}c^2F(c)$. It is positive, since $c^2F$ is continuous and positive on $(0,1)$ and tends to $1$ at $0$. Hence $y^2V\ge m_1$ on $B(x',y'/20)$.

The constants are exact in verify.py §4; the sampled values of $m_1$ there are only illustrations.

**Upper bound.** Suppose $M=\sup w\in(0,\infty)$, and choose $x_n$ with $\varepsilon_n=M-w(x_n)\to0$.

*Step 1: move off the axis.* The function $w^+=\max(w,0)$ is subharmonic: on $\{w>0\}$, $\Delta w=VN(w)\ge0$, and where $w^+=0$ the sub-mean-value inequality is trivial. Suppose $c(x_n)>c_0$, and put $B=B(x_n,y_n/2)$. Then
$$\frac1{|B|}\int_B(M-w^+)\le M-w(x_n)=\varepsilon_n,$$
so $|\{w^+<M-128\varepsilon_n\}\cap B|\le|B|/128<|S|$. Hence there is $x_n'\in S$ with $w(x_n')\ge M-128\varepsilon_n$, and $c(x_n')\le c_0$ by (G1). If instead $c(x_n)\le c_0$, put $x_n'=x_n$.

*Step 2: quadratic perturbation.* Let $\delta=m_1(e^M-1)/14$, and take $n$ so large that $\varepsilon_n':=M-w(x_n')<\min(\delta/400,M/2)$. On $\bar B(x_n',y_n'/20)\subset\mathbb H$ put
$$u=w-\delta|x-x_n'|^2/y_n'^2 .$$
On the boundary of the ball $u\le M-\delta/400<u(x_n')$, so $u$ attains its maximum at an interior point $\eta$, where $w(\eta)\ge w(x_n')>M/2$ and $\Delta w(\eta)\le6\delta/y_n'^2$. By (G2),
$$\Delta w(\eta)=V(\eta)N(w(\eta))\ge\frac{m_1}{(21/20)^2y_n'^2}\,(e^M-1).$$
This contradicts $6\delta=\tfrac37m_1(e^M-1)<\tfrac{400}{441}m_1(e^M-1)$. So $M\le0$.

**Lower bound.** Suppose $m=\inf w<0$. The argument is symmetric: $\min(w,0)$ is superharmonic, the perturbation is $u=w+\delta|x-x_n'|^2/y_n'^2$, and we use $N(t)\le N(m/2)<0$ for $t\le m/2$. $\square$

**Remarks.**
1. Scale invariance enters only through (G1) and (G2), which are statements about cones. So the knot point, the boundary and infinity are treated alike, and no asymptotic information is needed.
2. Why the axis needs Step 1: for $k\ge1$, $V$ vanishes on $\{z=0\}$, so a near-maximum point near the axis gives no lower bound for $\Delta w$.
3. The same proof applies to $\Delta w=V\,N(w)$ for any nondecreasing $N$ with $tN(t)>0$ for $t\neq0$, and so to Proposition 3, where $N(t)=2t$. Strict sign is needed: $N\equiv0$ is nondecreasing with $N(0)=0$, yet it admits every bounded harmonic function, for instance nonzero constants.

## 5. Proofs of Propositions 3 and 4

**Proposition 3.** Apply §4 with $N(t)=2t$: a bounded $u$ has $\sup u\le0\le\inf u$. By Theorem 2(1), the linearised KW operator on the tangent directions $\delta v$ of $\mathcal A_k$ is $\delta v\mapsto(L\,\delta v)\,T\,dx_2\wedge dx_3$, with $L=\Delta-2V$. $\square$

*Scope.* The full deformation operator also has triangular sectors, and its indicial set at the knot includes roots such as $0$ for weight one [8], [26, Cor. 5]. We expect the root $0$ to correspond to moving or splitting the zeros of $z^k$, which changes the knot data. Proposition 3 is silent on these sectors.

**Proposition 4.**
1. This is a direct computation (verify.py §5b): the residual is exactly $-2T_3/y^2$.
2. Write $\rho^*$ for pullback. Since $\rho$ reverses orientation, $\rho^*(\star\beta)=-\star\rho^*\beta$ for a $2$-form $\beta$. Then:
   * $F_{\rho^*A}=\rho^*F_A$, and $(-\rho^*\phi)\wedge(-\rho^*\phi)=\rho^*(\phi\wedge\phi)$;
   * $\star d_{\rho^*A}(-\rho^*\phi)=-\star\rho^*(d_A\phi)=\rho^*(\star d_A\phi)$.

   So the first equation of (KW) is preserved, and $d^*$ is preserved up to sign. The identity $\sigma(\text{fields of }v)={\rm Ad}(-i\sigma_1)(\text{fields of }v\circ\rho)$ is checked symbolically on a non-symmetric test function, and on Witten's solution at rational points, for $k\le2$.
3. This is checked in the same way. The rotation identity is checked at a rational point to 30 digits, and the dilation identity exactly.
4. If $v$ solves (1.2) with bounded $w$, then so do $v\circ\rho$, $v\circ R_\alpha$, $v(\lambda\cdot)+(k+1)\log\lambda$ and the translates along $\ell$, because $v_W$ is invariant under all of these. By Theorem 1 they all equal $v_W$. By (2)–(3), each field-level transformation maps the standard representative of $v_W$ to a constant gauge transform of itself. So it preserves the gauge class. Any other representative differs by a gauge transformation $g$, and its image is then gauge-equivalent to it via the conjugated transformation. $\square$

## 6. Background on the unknot (not claimed as new)

**Lemma 5.** A finite CW spectrum $Y$ whose integral cohomology is a single $\mathbb Z$ in degree $n$ is $S^n$. Hence $\widetilde{\mathcal X}_{Kh}(U)\simeq S^0$ and $\mathcal X^{\pm1}_{Kh}(U)\simeq S^0$ [16].

*Proof.* After suspension we may take $n=0$. By the universal coefficient theorem, $H_*(Y;\mathbb Z)=\mathbb Z$ in degree $0$. By Hurewicz, $Y$ is connective with $\pi_0Y=\mathbb Z$. A generator $S^0\to Y$ is a homology isomorphism of bounded-below spectra, hence an equivalence. The unknot values come from §2 and [16, Thm. 1]. $\square$

**A formal category for the long unknot.** Take $k=1$ and $G=SO(3)$. Let $\mathcal C_{\rm form}$ have:
* objects: the $SO(3)$-gauge classes of KW solutions with the weight-one knot along $\ell$, in the sense of [8, §2];
* non-identity morphisms from $a$ to $b$: the set of *nonconstant* finite-energy HW trajectories from $a$ to $b$, modulo translation in $s$;
* identity morphisms, adjoined separately.

It carries no topology, framing or gluing. Consider two hypotheses.
* **(Cl$_1$)** Every such object has a representative in $\mathcal A_1$ with bounded $v-v_W$.
* **(E)** There are no nonconstant finite-energy HW trajectories from an object to itself.

**Corollary 6.**
1. *(Unconditional.)* In $\mathcal A_1$ there is exactly one gauge class of KW solutions with bounded $v-v_W$, namely Witten's (Theorem 1). It has no bounded Cartan scalar deformations (Proposition 3), and its bulk instanton density vanishes (Theorem 2(4)).
2. *(Under (Cl$_1$) and (E).)* $\mathcal C_{\rm form}$ has one object and only its identity morphism.

By [28], (Cl$_1$) holds among $x_1$-invariant solutions with nilpotent Higgs field that are asymptotic to the model (§1.3). Corollary 6 constructs no HW Floer complex or realization. That would need, at least:
* **(FD)** Fredholm theory and full non-degeneracy of the complete linearised operator, not only its Cartan scalar part;
* **(FR)** a construction of the framed HW flow category and its realization.

Assigning the object a degree is a normalisation.

**Proposition 7 (the labelled Seidel–Smith model of $U$).** Let $(\mathbb M_U)$ be the $m=1$ model: the $A_1$ Milnor fibre with $L=L'=\Lambda\cong S^2$, so that $HF^*(\Lambda,\Lambda)=H^*(S^2)$ in degrees $0,2$ [6]. We *assign* labels $h=0$ and $q=(m+w)-\deg$, with $m+w=1$.
1. The assigned labels are $(0,1)$ in degree $0$ and $(0,-1)$ in degree $2$, the bidegrees of $Kh(U)$.
2. The Morse–Bott category has one object $\Lambda$, and its realization is ${\rm Th}(V)=S^0\cup_{w_2(V)\eta}e^2$, with cells in degrees $0,2$, for a rank-$0$ virtual bundle $V\to S^2$.
3. *(Regrading.)* The spectrum to compare with is the *collapsed* one,
$$\bigvee_q\Sigma^{(m+w)-q}\mathcal X^q_{Kh}(U)=\bigvee_q\Sigma^{1-q}\mathcal X^q_{Kh}(U)\simeq S^0\vee S^2 .$$
   Then ${\rm Th}(V)\simeq S^0\vee S^2$ if and only if $w_2(V)=0$, as holds for $SO(3)$-equivariant data. The uncollapsed $\bigvee_q\mathcal X^q_{Kh}(U)\simeq S^0\vee S^0$ is not equivalent to ${\rm Th}(V)$, even up to an overall suspension, because its cells lie in equal degrees. It is recovered from ${\rm Th}(V)$ only by desuspending each assigned $q$-piece by $1-q$, which makes sense exactly when ${\rm Th}(V)$ splits along the assigned labels, that is, when $w_2(V)=0$.

*Proof.* (1) and the degrees are bookkeeping (verify.py §6). (2) For $L=L'$ the intersection is clean along $\Lambda$, and the realization is the Thom spectrum of the index bundle. Moreover $S^0\cup_fe^2$ with $f\in\pi_1^s$ has $f=\eta$ if and only if $Sq^2\ne0$, if and only if $w_2(V)\ne0$. An $SO(3)$-equivariant line bundle on $SO(3)/SO(2)$ of weight $n$ has degree $2n$. (3) follows from (2) and Lemma 5. $\square$

*What Proposition 7 does not say.* It concerns the model and its assigned labels only. Transferring it to HW theory would require an adiabatic equivalence that identifies the *bigrading*, not just the collapsed grading $h-q$, with these labels. Preservation of $q$ alone does not fix the values of $q$: for example, groups at $(h,q)=(-1,0),(1,0)$ have the same collapsed degrees as groups at $(0,1),(0,-1)$. The companion preprints [H1, H2] formulate adiabatic hypotheses, but those hypotheses do not include such a bigrading identification. We make no claim about HW theory or about the framing that such an equivalence would transport.

## 7. What remains open

1. **The round unknot.** The $U(1)$ of rotations about the axis of a round circle reduces (KW) only to a three-dimensional system on $\{(\rho,x_3,y)\}$. That system has no dilation symmetry and no translation along the knot, so neither the holomorphic structure behind Theorem 2(1) nor the cone geometry of §4 is available. We know of no existence result for KW solutions with a compact knot.
2. **Several knot points.** For $p=(z-p_1)(z-p_2)$, the scalar reference solution exists [10, Prop. 6.1]. Moreover [28, Thm. 1.3] classifies all $x_1$-invariant solutions with nilpotent Higgs field and model asymptotics, non-diagonal ones included, in terms of $(P,Q,R)$. So neither the reference solution nor a classification on $\mathbb R^2\times\mathbb R^+$ is missing. Three things remain beyond [10, 28]:
   * whether Theorem 1 extends to $V=|p|^2e^{2v_{\rm ref}}$, which depends on the cone conditions (G1)–(G2) and which we have not checked;
   * a version of the classification without asymptotic hypotheses at infinity;
   * the adiabatic passage from these $x_1$-invariant solutions to a compact unknot.
3. **(Cl$_1$) in general.** By [28], (Cl$_1$) holds within the class of $x_1$-invariant solutions with nilpotent Higgs field that are asymptotic to the charge-$k$ model. What remains is to remove:
   * translation invariance along $\ell$;
   * the restriction on the holomorphic data (nilpotent Higgs field, which we have not shown is forced by the Nahm-pole and knot conditions);
   * the asymptotic condition at infinity.
4. **Floer foundations.** (FD), (FR), (E), and an identification of the bigrading under any adiabatic equivalence.

## 8. Status of claims

**Proved here.**
* Theorem 1, the main result, and its linear analogue, Proposition 3.
* Proposition 4, the field-level symmetries, including the counterexample.

**Background, re-verified.** Theorem 2: the reduction [10, §6] and Witten's model [8, §2], with the regularity statement (3).

**Background (§6).**
* Lemma 5 (standard).
* Corollary 6(1).
* Proposition 7, about the model with assigned labels only.

**Conditional.** Corollary 6(2), on (Cl$_1$) and (E). It concerns a formal category only.

**Not claimed.**
* (Cl$_1$) beyond [28], (E), (FD), (FR).
* The kernel of the full linearised operator.
* Any HW Floer complex or realization.
* Any identification of HW bigradings with the model labels.
* Any statement about a compact unknot.

**Novelty.** It is narrow: the one-sided bounded-difference formulation of the comparison principle (Theorem 1), with no boundary or asymptotic conditions, and its $L^\infty$ linear analogue for all $k$ (Proposition 3). The reduction, the model and the unknot spectra are background. Proposition 4 corrects a field-level symmetry statement.

**Verifier.**
* verify.py runs 111 checks, with FALLOS = 0. It covers:
  * $Kh(U)$ and $\widetilde{Kh}(U)$;
  * the reduction for generic $v$, in two encodings;
  * the identity (3.1) for symbolic $K$;
  * the exact pointwise checks of (1.2) and (KW);
  * the $k=\tfrac12$ expansion;
  * homogeneity and asymptotics;
  * the exact constants of §4;
  * the counterexample of Proposition 4(1);
  * $\sigma$, rotations and dilations;
  * the labels and the regrading of Proposition 7;
  * the reduction of the data of [28] for a single knot point.

  It does not verify Theorem 1 itself, which is proved in §4.
* verify.mpl mirrors the exact parts of §§0–4 under the Maple rules.

## References

1. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.
2. D. Gaiotto, E. Witten, *Knot invariants from four-dimensional gauge theory*, Adv. Theor. Math. Phys. 16 (2012), 935–1086; arXiv:1106.4789.
3. E. Witten, *Khovanov homology and gauge theory*, Geom. Topol. Monogr. 18 (2012), 291–308; arXiv:1108.3103.
4. A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207; arXiv:1010.2353.
5. M. Bleher, *Adiabatic solutions of the Haydys–Witten equations and symplectic Khovanov homology*, arXiv:2501.01365.
6. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514; arXiv:math/0405089.
7. R. Mazzeo, E. Witten, *The Nahm pole boundary condition*, arXiv:1311.3167 (§§2.5–2.6, 3.2–3.4).
8. R. Mazzeo, E. Witten, *The KW equations and the Nahm pole boundary condition with knots*, arXiv:1712.00835 (§2, Prop. 6.1).
9. P. Dimakis, *Model knot solutions for the twisted Bogomolny equations*, arXiv:2204.06617 (Thm. 1.1).
10. S. He, R. Mazzeo, *The extended Bogomolny equations and generalized Nahm pole boundary condition*, Geom. Topol. 23 (2019); arXiv:1710.10645 (Thm. 1.2; §6: (67), Prop. 6.1, Prop. 6.2, Thm. 6.3).
11. S. He, R. Mazzeo, *The extended Bogomolny equations with generalized Nahm pole boundary conditions, II*, arXiv:1806.06314 (Thm. 1.1).
12. P. Dimakis, *The moduli space of solutions to the extended Bogomolny equations on $\Sigma\times\mathbb R_+$*, arXiv:2401.10999 (Thm. 1.1).
13. S. He, *Rotationally invariant singular solutions to the Kapustin–Witten equations*, Math. Res. Lett. 25 (2018); arXiv:1510.07706 (Thm. 1.4).
16. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.
25. D. Bar-Natan, *On Khovanov's categorification of the Jones polynomial*, Algebr. Geom. Topol. 2 (2002), 337–370.
26. *The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one*, rStation math_8 v1, https://rstation.ai/problems/math/papers/8/v1 (§2.1; Thm. 3; Cor. 5).
27. *The zeroth-order operator in a scalar model of Bleher's continuity method at weight one: invertibility and explicit adiabatic corrections for moving knots*, rStation math_12 v1, https://rstation.ai/problems/math/papers/12/v1 (Thms. 3–5).
28. P. Dimakis, *The extended Bogomolny equations on $\mathbb R^2\times\mathbb R^+$ I: Nilpotent Higgs field*, arXiv:2209.11101v2 (Thm. 1.3, §6).

[H1] *The Hopf link in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and its realization*, companion preprint (in review).
[H2] *The trefoil in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and the geometric origin of the $\mathbb Z/2$ and of the Moore piece*, companion preprint (in review).

Earlier papers in this line on rStation (not used in the proofs): https://rstation.ai/problems/math/papers/24/v2, https://rstation.ai/problems/math/papers/31/v1, https://rstation.ai/problems/math/papers/33/v1.

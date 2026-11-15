# The framing bit of the trefoil in the adiabatic Seidel–Smith model vanishes

**Abstract.**

math_36 (rStation) reduced the realization of the left trefoil in the adiabatic Seidel–Smith model to one bit $\varepsilon_{\rm can}\in\pi_1^s$. It is the framing that the index bundle of the fixed-end linearised operators induces on the circle $\Sigma$ of Floer strips, relative to the Lie framing.

**Theorem.** $\varepsilon_{\rm can}=0$: the canonical framing of $\Sigma$ is the bounding framing.

Brane data are a stable trivialisation of $TS$ in the $A_2$ fibre $S=\{bc=p(a)\}$ and nullhomotopies of the matching spheres' stable Gauss maps (Porcelli–Smith, framed case). They trivialise the index bundle by an end-preserving transport: boundary conditions are deformed through the square filled by the nullhomotopies, with asymptotic data and weights fixed and capping paths inserted at the ends. The proof has three steps.
(i) The holomorphic involution $\sigma(a,b,c)=(a,c,b)$ preserves both spheres, reversing their orientation, and acts on $\Sigma$ as a free half-turn. So the boundary evaluation maps have degree zero; as $[S,U]=0$, $\varepsilon_{\rm can}$ is independent of the brane data.
(ii) The trivialisation $TS\oplus\mathbb C\cong\mathbb C^3$ given by $dF$ is $\sigma$-equivariant, and the fixed circles have vanishing Maslov indices, so equivariant brane data exist.
(iii) The capped index is $2\,\mathrm{sgn}-\mathbf 1$, while the kernel frame carries $2-\mathbf 1$: after removing the caps, the anti-invariant part is a scalar problem of index $2$, one for each critical value enclosed by the reflex bigon.
A lemma on involutions gives the Lie framing twisted by the generator of $\pi_1(O)$.

If these are the framings of a spectral Floer theory, and math_36's (Eq) and (R) hold, the Floer realization is the collapsed Lipshitz–Sarkar spectrum, Moore piece included, as math_36 predicted. Identifying our definition with Porcelli–Smith's framings is an explicit assumption.

## 1. Introduction

### 1.1 The question

The rStation paper math_36 (https://rstation.ai/problems/math/papers/36/v1, cited as [1]) treats the left trefoil $3_1=\widehat{s_1^3}$ in the local fibred model of Seidel–Smith [3, §6(C)]. It finds all Floer strips. The unperturbed Morse–Bott correspondence is
$$E\xleftarrow{\ s\ }\mathcal M\cong E\times\Sigma\xrightarrow{\ t\ }C_0,\qquad E\cong\mathbb{RP}^3,\ C_0\cong S^2,$$
where $\Sigma$ is a circle made of four slit arcs [1, Thm C]. For $SO(3)$-equivariant framings, [1, Thm D(3)–(5)] shows that the realization is one of two spectra, indexed by a bit $\varepsilon\in\pi_1^s=\mathbb Z/2$:
* $\varepsilon=0$ gives the collapsed Lipshitz–Sarkar spectrum, Moore piece included;
* $\varepsilon=\eta$ gives a spectrum with $Sq^2\neq0$.

[1, §7.3(3)] names the missing input. It is the canonical bit $\varepsilon_{\rm can}$: "the index-bundle framing of the loop $\{D_u\}_{u\in\Sigma}$ with fixed ends, relative to the Lie framing of $\Sigma$". [1, Cor. E(3)] predicts $\varepsilon_{\rm can}=0$ from the gauge-theory side. Here we compute $\varepsilon_{\rm can}$ from the definition, without using that prediction.

### 1.2 Result

Notation is that of [1] and of the Hopf paper math_35 (https://rstation.ai/problems/math/papers/35/v1, cited as [2]); see §2.1. Fix $x\in K$ and the fibre $S=Y_x=\{bc=p(a)\}$. Fix a point $e\in S^1_*$, and let $\Sigma_e$ be the circle of strips from $e$ to $x_0$. In $\mathcal M\cong E\times\Sigma$ this is the fibre $s^{-1}(e)$. "Brane data" means framed tangential data in the sense of Porcelli–Smith [5, Def. 3.6, Ex. 3.2]: a stable trivialisation of $TS$, plus nullhomotopies of the stable Gauss maps of the two matching spheres (§2.2). For such data $\mathfrak b$, Definition 2.4 gives a stable framing $\varphi_{\mathfrak b}$ of $\Sigma_e$, obtained from the index bundle of the fixed-end operators. We set
$$\varepsilon_{\rm can}:=[\Sigma_e,\varphi_{\mathfrak b}]\in\pi_1^s .$$

**Theorem 1.** Let $\varepsilon_{\rm can}$ be the bit just defined.
1. *(Well defined.)* $\varepsilon_{\rm can}$ does not depend on the brane data $\mathfrak b$, on $e\in S^1_*$ or on $x\in K$. The same holds for brane data on $(Y;L,L')$ restricted to a fibre, when such data exist.
2. *(Symmetry.)* The holomorphic involution $\sigma(a,b,c)=(a,c,b)$ of $S$ preserves $\Lambda_\alpha$ and $\Lambda_{\alpha'}$ and reverses their orientations. For $e$ one of its two fixed points on $S^1_*$, it acts on $\Sigma_e$ as a free, orientation-preserving half-turn, $(P,k_1,k_2)\mapsto(P,-k_1,-k_2)$. It preserves the kernel frame $(\partial_su,\partial_\Sigma u)$.
3. *(Equivariant index.)* Some brane data are $\sigma$-equivariant. For these, the end-preserving transport of §2.3 is $\sigma$-equivariant. Its target, the index $V$ of the capped operator $D_{\beta_*}$, is the virtual representation $2\cdot\mathrm{sgn}-\mathbf 1$, while the stabilised kernel frame carries $2\cdot\mathbf 1-\mathbf 1$.
   * The anti-invariant index $2$ is the number of critical values enclosed by the reflex bigon.
   * The $-\mathbf 1$ comes from the stabilising normal line, and appears on both sides.
4. *(Value.)* $\varphi_{\mathfrak b}$ differs from the Lie framing of $\Sigma_e$ by the generator of $\pi_1(O)$. Hence
$$\boxed{\ \varepsilon_{\rm can}=0\ }$$
   and the canonical framing of $\Sigma$ is the bounding framing.

**Corollary 2 (conditional).** Assume:
* Assumption (B) of §2.3: the Floer framings of a spectral Floer theory for $(Y;L,L')$ restrict on $\Sigma_e$ to the framing of Definition 2.4;
* Hypotheses (Eq) and (R) of [1, §1.2, after Thm D].

Then the Floer realization $R(\varphi_{\rm can})$ of the trefoil correspondence is
$$S^0\vee S^2\vee S^2\vee\Sigma^2\mathbb{RP}^2\vee S^5\ \simeq\ \bigvee_q\Sigma^{m+w-q}\mathcal X^q_{Kh}(3_1^{\rm left}),$$
the collapsed Lipshitz–Sarkar spectrum [4, Example 9.1], Moore piece included. In particular $Sq^2=0$ on $H^0$. This settles the bit left open in [1, Prop. F(3)], and it agrees with the prediction [1, Cor. E(3)].

### 1.3 Method

The proof uses three steps, and no analysis beyond [1] and the Robbin–Salamon index theorem [6].
1. *Degree zero (§3).* The swap $\sigma$ is orientation-preserving on the parameter circle $\Sigma_e$ and orientation-reversing on each sphere. So the boundary evaluation maps of the family have degree $0$. Since $[S,U]=0$, the bit is then independent of all choices.
2. *Localisation (§§4–6).* The index bundle is trivialised by an end-preserving transport: the boundary conditions are deformed through the square filled by the brane nullhomotopies, with the asymptotic data fixed and capping paths inserted at the ends. Choose $\sigma$-equivariant brane data. The trivialisation becomes $\sigma$-equivariant, with $\sigma$ acting on the fixed index space $V$. Both the kernel frame and the index frame are equivariant, for the trivial action and for the action on $V$ respectively. The comparison loop $g$ then satisfies $g(\vartheta+\pi)=A\,g(\vartheta)$. Its class is $\tfrac12\dim V^{-}\bmod2$ (Lemma 7.1).
3. *Count (§6).* $V^-$ is the index of a scalar Cauchy–Riemann problem in the normal line of the fixed curve $\{b=c\}$. The boundary condition there is the line $i b\,\mathbb R$, with $b=\sqrt{p(a)}$. Its gap rotates by $2\pi+\vartheta_0/2$ between the ends. The $2\pi$ comes from the two critical values $q_1,q_2$ inside the reflex bigon. For an empty bigon the same count gives $0$. The Robbin–Salamon theorem gives index $2$. The capping paths are removed by an end-preserving homotopy, so they contribute nothing beyond the fixed end data.

### 1.4 What is not proved

* (Ad), (R), (Eq) and (P) of [1] are untouched. So is the compactified perturbed (cascade) category.
* We do not construct a spectral Floer theory for $(Y;L,L')$, and we do not prove that brane data exist on $(Y;L,L')$.
* Assumption (B), which identifies Definition 2.4 with the restriction of the framings of [5], is not proved. It is the only link between Theorem 1 and Corollary 2 beyond (Eq) and (R).
* The Hopf invariant $\theta_{\rm eq}$ of [1, Prop. F] is not treated.
* *Novelty.* This is narrow: one bit, in one model. The ingredients (index bundles of boundary data, equivariant splitting, Robbin–Salamon) are standard. As far as we know, their application to $\Sigma$ is new.

## 2. Setting and the definition of $\varepsilon_{\rm can}$

### 2.1 The fibre problem

We use [1, §1.3]: $p(a)=(a-q_0)(a-q_1)(a-q_2)$, and $S=\{bc=p(a)\}\subset\mathbb C^3$ with the restricted Kähler structure. For a matching path $\gamma$, $\Lambda_\gamma=\{a\in\gamma,\ |b|=|c|\}$. The path $\alpha$ runs from $q_0$ to $q_1$, and $\alpha'=t^3(\alpha)$ runs from $q_0$ to $q_2$.

**Facts imported from [1].**
* $\alpha\cap\alpha'=\{q_0,a^*\}$. The bigon $R$ has a convex corner of angle $\vartheta_0$ at $q_0$ and a reflex corner of angle $\vartheta_*\in(\pi,2\pi)$ at $a^*$, and it contains $q_1,q_2$ [1, Thm A(3), Lemma 3.1].
* $\Lambda_\alpha\cap\Lambda_{\alpha'}=\{x_0\}\sqcup S^1_*$ cleanly.
* Every strip $u:Z=\mathbb R\times[0,1]\to S$ with $u(\cdot,0)\in\Lambda_\alpha$ and $u(\cdot,1)\in\Lambda_{\alpha'}$ is a lift of the Riemann map $A_P$ of a slit domain $R_P$:
$$u=\big(A_P,\ e^{i\vartheta}(p(A_P)B_1^{k_1}B_2^{k_2})^{1/2},\ p(A_P)/b\big)$$
  [1, Lemma 5.2, Prop. 5.3].
* For fixed $e\in S^1_*$, the strips ending at $e$ form a circle $\Sigma_e$ of four arcs $(k_1,k_2)$, glued at four fold points [1, Lemma 5.4].
* Every strip is regular. The fixed-end operator $D_u^{\rm fix}$ requires decay at both ends; in particular it excludes rotation along $S^1_*$. It is onto, with
$$\ker D_u^{\rm fix}=\langle\partial_su,\ \partial_\Sigma u\rangle,\qquad\operatorname{ind}D^{\rm fix}_u=2,$$
  where $\partial_\Sigma u$ is the slit or fold direction [1, Lemma 5.5] (free-end index $3$, minus $\dim S^1_*$).

*Orientation of the strips.* $A_P$ is orientation preserving, so the boundary $t=0$ traverses $\alpha$ in the counterclockwise sense of $\partial R$. In the explicit model of [1, §1] (verify.py §1), the loop $\alpha'[q_0\to a^*]\cdot\alpha[a^*\to q_0]$ is counterclockwise. So $u(-\infty)=e$ and $u(+\infty)=x_0$. The mirror picture reverses this, and every statement below holds in both orientations (verify.py §7).

The index bundle of $\{D^{\rm fix}_u\}_{u\in\Sigma_e}$ is $\mathcal I=\ker D^{\rm fix}$, a rank-$2$ bundle over $\Sigma_e$. The **kernel frame** is $K=(\partial_su,\partial_\Sigma u)$, with $\partial_\Sigma$ the oriented tangent of $\Sigma_e$. As a stable framing of $\underline{\mathbb R}\oplus T\Sigma_e$, $K$ is the Lie framing. Its Pontryagin–Thom class is $\eta$, and the bounding framing has class $0$ [1, Lemma 6.3].

### 2.2 Brane data

Write $U/O$ for the stable Lagrangian Grassmannian and $\widetilde{U/O}$ for its universal cover. We use the framed case of [5]. There, a tangential structure of rank $N$ is a space over $\widetilde{U/O}(N)$ [5, Def. 3.1], and the framed structure is the basepoint inclusion [5, Ex. 3.2]. A Θ-orientation of boundary data is a homotopy lift of the boundary conditions to $\Theta$ [5, Def. 3.6].

**Definition 2.1 (brane data).** Brane data $\mathfrak b=(\Phi,H_\alpha,H_{\alpha'})$ on $(S;\Lambda_\alpha,\Lambda_{\alpha'})$ consist of:
* a stable trivialisation $\Phi:TS\oplus\underline{\mathbb C}^{k}\cong\underline{\mathbb C}^{N}$, with a real line $\ell\subset\underline{\mathbb C}^k$ along the matching spheres (a stabilising Lagrangian), giving graded stable Gauss maps
$$G_\gamma:\Lambda_\gamma\to\widetilde{U/O}(N),\qquad p\mapsto\Phi(T_p\Lambda_\gamma\oplus\ell_p);$$
* nullhomotopies $H_\gamma:\Lambda_\gamma\times[0,1]\to\widetilde{U/O}(N)$ from $G_\gamma$ to the basepoint $\mathbb R^N$, for $\gamma=\alpha,\alpha'$.

### 2.3 The index framing of $\Sigma_e$: an end-preserving transport

Throughout, $e$ sits at $s=-\infty$ and $x_0$ at $s=+\infty$ (§2.1). The mirror orientation is identical after $s\mapsto-s$.

**(a) Asymptotic data.** Put $F^0_-=G_\alpha(e)$, $F^1_-=G_{\alpha'}(e)$, $F^0_+=G_\alpha(x_0)$ and $F^1_+=G_{\alpha'}(x_0)$. These four Lagrangian subspaces of $\mathbb C^N$ do not depend on $u\in\Sigma_e$. The pairs are clean, with intersections
$$F^0_-\cap F^1_-=\mathbb R\,iV(e)\oplus\ell_e,\qquad F^0_+\cap F^1_+=\ell_{x_0}.$$
Fix $\delta\in(0,\delta_0)$, where $\delta_0$ is the smallest nonzero $|\kappa|$ in the spectra of the two asymptotic operators $A_\pm=-i\,\partial_t$ on $[0,1]$ with boundary conditions $(F^0_\pm,F^1_\pm)$. Write $W^{1,p}_\delta$ and $L^p_\delta$ for the spaces with weight $e^{\delta|s|}$ (for some $p>2$), so all elements decay at both ends. This is the fixed-end convention of §2.1.

**(b) The space of boundary data.** Fix $T_0>0$. Let $\mathcal B$ be the space of pairs $\beta=(F^0,F^1)$ of continuous paths $F^j:\mathbb R\to\widetilde{U/O}(N)$ that are smooth on $[-T_0,T_0]$, with $F^j(s)=F^j_\mp$ for $\mp s\ge T_0$, in the $C^1$ topology. For $\beta\in\mathcal B$, let
$$D_\beta=\partial_s+i\partial_t:\ W^{1,p}_\delta(Z,\mathbb C^N;\beta)\to L^p_\delta(Z,\mathbb C^N),$$
where $W^{1,p}_\delta(\,\cdot\,;\beta)$ denotes the functions with $f(s,j)\in F^j(s)$. A *Cauchy–Riemann operator over $\beta$* is $D_\beta+S$, with $S\in L^\infty$ an exponentially decaying zeroth-order term.

**Lemma 2.2.** Every Cauchy–Riemann operator over $\beta\in\mathcal B$ is Fredholm. The operators $D_\beta+S$, over all $\beta\in\mathcal B$ and decaying $S$, form a continuous Fredholm family, so their index defines a virtual bundle $\mathbb V\to\mathcal B$, well defined up to canonical isomorphism. The same holds for paths that are constant only for $|s|\ge T_1$, for any $T_1\ge T_0$, and for boundary paths converging exponentially to $F^j_\mp$.

*Proof.*
* *Gauge to fixed boundary data.* Lift $F^0$ to a path $U^0:\mathbb R\to U(N)$ with $U^0(s)\mathbb R^N=F^0(s)$, constant for $|s|\ge T_0$. Then lift $s\mapsto U^0(s)^{-1}F^1(s)$ through the fibration $U(N)\to U(N)/O(N)$ to $V_1(s)$, with $V_1(s)\Lambda_1=U^0(s)^{-1}F^1(s)$ for a fixed reference Lagrangian $\Lambda_1$ and $V_1$ constant for $|s|\ge T_0$. Let $V(s,t)$ be a smooth path in $U(N)$ from $1$ to $V_1(s)$, constant in $s$ for $|s|\ge T_0$. Then $f=U^0V g$ identifies $W^{1,p}_\delta(\beta)$ with the fixed space $W^{1,p}_\delta(\mathbb R^N,\Lambda_1)$.
* *The conjugated operator.* It has the form $\partial_s+i\partial_t+P(s,t)$, and its $s$-independent part on the ends is $-A_\pm^{\rm gauged}=-(-i\partial_t-iV_\pm^{-1}\partial_tV_\pm)$. Since $V^{-1}\partial_tV$ is skew-Hermitian, $iV^{-1}\partial_tV$ is symmetric, so $A^{\rm gauged}_\pm$ is self-adjoint and unitarily conjugate to $A_\pm$.
* *Fredholmness.* The weight shifts the spectrum by $\mp\delta$, which makes it invertible. [6, Theorem A] then gives Fredholmness and identifies the index with the spectral flow.
* *Continuity.* Locally in $\beta$ the lifts can be chosen continuously, so the conjugated family is continuous in operator norm. The index bundle of a norm-continuous Fredholm family over a paracompact space is well defined up to canonical isomorphism (Atiyah–Jänich). Changing the lifts conjugates by a continuous family of isomorphisms of the same form, which does not change the bundle up to canonical isomorphism.
* *The variants.* The last sentence holds because these conditions leave $A_\pm$ unchanged. $\square$

**(c) The strips as points of $\mathcal B$.** Trivialise $u^*TS\oplus\underline{\mathbb C}$ by $\Phi$. Since $u$ converges exponentially at both ends [7], $\Phi(D^{\rm fix}_u\oplus D^\ell_u)\Phi^{-1}$ is a Cauchy–Riemann operator over $\beta_u=(G_\alpha(u(\cdot,0)),G_{\alpha'}(u(\cdot,1)))$. Here $\beta_u$ converges exponentially, and $D^\ell_u$ is $\bar\partial$ on $u^*N_S\cong\underline{\mathbb C}$ (via $dF$) with boundary condition $\mathbb R$.

Push the paths into $\mathcal B$ as follows. Choose charts of $\Lambda_\gamma$ at $e$ and $x_0$, and a cutoff $\rho_T$ that equals $1$ on $[-T,T]$ and $0$ for $|s|\ge T+1$. Replace $u(s,j)$ for $|s|\ge T$ by the chart contraction $\exp(r\rho_T(s)\exp^{-1}u(s,j))$, for $r$ from $1$ to $0$. Here $T$ is chosen uniformly over the compact $\Sigma_e$, so that $u(s,j)$ lies in the charts for $|s|\ge T$. By Lemma 2.2 (variants), this gives a path of Fredholm operators with fixed asymptotic data. Write $u^c(\cdot,j)$ for the resulting boundary paths in $\Lambda_\gamma$, which are constant ($=e$, resp. $x_0$) for $|s|\ge T+1$. The endpoint $\beta^c_u=(G_\alpha\circ u^c(\cdot,0),G_{\alpha'}\circ u^c(\cdot,1))\in\mathcal B$ (with $T_0=T+1$) depends continuously on $u$, and so do the canonical isomorphisms $\operatorname{ind}(D^{\rm fix}_u\oplus D^\ell_u)\cong\mathbb V_{\beta^c_u}$. Different $T$, charts or cutoffs form a connected (indeed convex) set of choices.

**(d) The square transport.** Let $\mathfrak b=(\Phi,H_\alpha,H_{\alpha'})$ be brane data (Definition 2.1). Assume, after a reparametrisation in $\tau$ that does not change homotopy classes, that $H_\gamma(p,\tau)$ is constant in $\tau$ for $\tau$ near $0$ and near $1$. For $\tau\in[0,1]$, define the boundary path at $t=0$ as the concatenation, reparametrised to be constant for $|s|\ge T_0$,
$$F^0_{u,\tau}\;=\;H_\alpha(e,\cdot)|_{[0,\tau]}\ *\ H_\alpha\big(u^c(\cdot,0),\tau\big)\ *\ \overline{H_\alpha(x_0,\cdot)|_{[0,\tau]}},$$
and $F^1_{u,\tau}$ in the same way with $\alpha'$. This is the standard filling of the square $[\text{path}]\times[0,1]$ by $H_\alpha$.
* For every $\tau$, its ends are $F^0_\mp$, so $(F^0_{u,\tau},F^1_{u,\tau})\in\mathcal B$: the deformation is end-preserving.
* At $\tau=0$ it is $\beta^c_u$, up to reparametrisation.
* At $\tau=1$ it is
$$\beta_*:=\Big(H_\alpha(e,\cdot)*\mathrm{const}_{\mathbb R^N}*\overline{H_\alpha(x_0,\cdot)},\ \ H_{\alpha'}(e,\cdot)*\mathrm{const}_{\mathbb R^N}*\overline{H_{\alpha'}(x_0,\cdot)}\Big),$$
  which does not depend on $u$. Its boundary conditions run from the fixed end data, along the capping paths $H_\gamma(e,\cdot)$ and $H_\gamma(x_0,\cdot)$, to the basepoint $\mathbb R^N$.

So we have a map $\mathcal S_{\mathfrak b}:\Sigma_e\times[0,1]\to\mathcal B$, with $\mathcal S|_{\Sigma_e\times0}=\beta^c$ and $\mathcal S|_{\Sigma_e\times1}\equiv\beta_*$.

**(e) The isomorphism.** $\mathcal S_{\mathfrak b}^*\mathbb V$ is a virtual bundle over $\Sigma_e\times[0,1]$, and its restriction to $\Sigma_e\times1$ is $\Sigma_e\times V$ with
$$V:=\operatorname{ind}(D_{\beta_*}).$$
Isomorphisms $\mathcal S^*\mathbb V\cong{\rm pr}^*(\mathcal S^*\mathbb V|_{\Sigma_e\times1})$ that are the identity over $\Sigma_e\times1$ form a contractible space. Restricting to $\Sigma_e\times0$ and composing with (c) gives
$$T_{\mathfrak b}:\ \operatorname{ind}(D^{\rm fix}\oplus D^\ell)\big|_{\Sigma_e}\ \cong\ \Sigma_e\times V,$$
well defined up to homotopy.

**(f) The stabilisation summand.** $D^\ell_u$ is the same operator for every $u$: $\bar\partial$ on $Z\times\mathbb C$ with boundary $\mathbb R$ on both sides and decay at both ends. By Lemma 6.1 its index is $-1$, with cokernel spanned by the constant $1$. So
$$\operatorname{ind}(D^{\rm fix}_u\oplus D^\ell_u)=\ker D^{\rm fix}_u-\mathbb R,$$
of virtual dimension $1$. The **stabilised kernel frame** is $K^{\rm st}=K\oplus(-1)$, a trivialisation by $\mathbb R^2-\mathbb R$.

**Lemma 2.3 (what $T_{\mathfrak b}$ depends on).** The homotopy class of $T_{\mathfrak b}\circ(K^{\rm st})^{-1}:\Sigma_e\to{\rm Iso}(\mathbb R^2-\mathbb R,V)$, a loop in the stable group $O$, depends only on the homotopy class of $\mathfrak b$. It does not depend on $T_0$, $T$, the charts, the cutoffs, the weight $\delta$, the zeroth-order terms, the lifts in Lemma 2.2 or the reparametrisations.

*Proof.*
* *Auxiliary choices.* Each auxiliary choice ranges over a connected set: intervals, convex sets, or the contractible space of lifts. Along a path of choices, all operators remain Fredholm with the same $A_\pm$ (Lemma 2.2), so the loop varies continuously and its class in $\pi_1(O)=\mathbb Z/2$ is constant.
* *Homotopies of brane data.* A homotopy $\mathfrak b_r$ gives a continuous family $\mathcal S_{\mathfrak b_r}$, and the class is again constant.
* *No hidden loop.* $T_{\mathfrak b}$ is determined up to homotopy by the map $\mathcal S_{\mathfrak b}$ rel $\Sigma_e\times\{0,1\}$, and $\mathcal S_{\mathfrak b}$ is determined by $\mathfrak b$. The only other ingredient, the extension isomorphism in (e), is unique up to a contractible choice. So no auxiliary choice can contribute an extra loop. $\square$

**Definition 2.4 (the bit).** Let $d(\mathfrak b)\in\pi_1(O)=\mathbb Z/2$ be the class of Lemma 2.3. Let $\varphi_{\mathfrak b}$ be the stable framing of $\underline{\mathbb R}\oplus T\Sigma_e$ obtained from $T_{\mathfrak b}$ and the constant summand of (f). Then
$$\varepsilon_{\rm can}:=[\Sigma_e,\varphi_{\mathfrak b}]=\eta+J(d(\mathfrak b))\in\pi_1^s,$$
where $J:\pi_1(O)\to\pi_1^s$ is the (bijective) $J$-homomorphism.

This is the invariant described in [1, §7.3(3)]. Changing the orientation conventions, the order of the summands, or the sign of the translation vector changes $K$ and $T_{\mathfrak b}$ by the same constant matrix. So none of these changes affects $d$.

*Relation to [5].* In [5, §3.2], boundary conditions are constant over the strip-like ends [5, Def. 3.5]. A Θ-orientation is a pair $(H,\Gamma)$ of homotopy lifts of the boundary conditions, constant along the shrunken ends [5, Def. 3.6]. Θ-oriented puncture data consist of capping paths $\gamma_{u_x},\gamma_{v_x}$ starting at the asymptotic Lagrangians, together with lifts of their endpoints [5, Def. 3.8]. For the framed structure [5, Ex. 3.2], the data of (d) are of this kind: the lift is $\Gamma=H_\gamma\circ u^c$, and the capping paths at $x\in\{e,x_0\}$ are $H_\gamma(x,\cdot)$. Construction (d) is the end-preserving form of this datum, with the capping paths inserted into the boundary.

[5] treats transverse punctures, and its index bundles of Θ-oriented abstract discs [5, Lemma 3.18] are compared with Floer moduli in [5, §6]. Our ends are clean (Morse–Bott). We do not prove that the framings of a full spectral Floer theory restrict to $\varphi_{\mathfrak b}$; this is Assumption (B). Large [8] constructs stable framings of Floer moduli spaces for stably trivialised Liouville manifolds in a similar way.

**Assumption (B).** $(Y;L,L')$ carry framed brane data in the sense of [5, §6.1]. The stable framing that the resulting Floer flow category induces on the fibre $s^{-1}(e)=\{e\}\times\Sigma\subset\mathcal M$, after removing the summands that are constant along the fibre, is the framing $\varphi_{\mathfrak b}$ of Definition 2.4 for the restricted brane data.

*Restriction from $Y$.* Over $S=Y_x$ there is a splitting $TY|_S=TS\oplus\mathcal H$, where $\mathcal H_p=\mathfrak m\cdot p\oplus J(\mathfrak m\cdot p)$ and $\mathfrak m\subset\mathfrak{so}(3)$ is the complement of the isotropy algebra. In it $TL|_{\Lambda_\alpha}=T\Lambda_\alpha\oplus\mathfrak m\cdot p$, and $\mathcal H$ is identified with the constant $T_xX$ by $d\pi$, with $\mathfrak m\cdot p\mapsto T_xK$. The operator in $Y$ is block triangular [1, Lemma 5.5], with a base block that is constant along $\Sigma_e$, and the off-diagonal term can be scaled to $0$ through Fredholm operators. So the $Y$-problem restricted to $\Sigma_e$ is the fibre problem plus constant summands. The same holds for the remaining constant directions: rotation along $S^1_*$ and the horizontal directions of $E$ and $C_0$. They do not affect the class in $\pi_1(O)$.

## 3. Independence of the brane data

**Lemma 3.1.** $[S,U]=0$. Hence stable trivialisations of $TS$ are unique up to homotopy.

*Proof.* $S$ is the $A_2$ Milnor fibre, so $S\simeq S^2\vee S^2$. Since $U$ is connected and $\pi_2(U)=0$ (Bott), $[S^2\vee S^2,U]=0$. $\square$

**Lemma 3.2 (degree zero).** For $\gamma=\alpha,\alpha'$, let
$$ev_\gamma:\ \Sigma_e\times[-\infty,\infty]\big/\big(\Sigma_e\times\{\pm\infty\}\big)\cong S^2\longrightarrow\Lambda_\gamma\cong S^2$$
be the boundary evaluation at $t=0$, respectively $t=1$. It is continuous, and $\deg ev_\gamma=0$.

*Proof.* *Continuity.* $\mathcal M_S\cong U(1)\times\Sigma$ is a smooth closed family [1, Lemma 5.4]. The strips converge uniformly and exponentially at both ends [1, §5.5], [7], and the ends go to the fixed points $e$ and $x_0$. So $ev_\gamma$ extends continuously to the two collapsed circles.

*Degree.* Choose $e$ fixed by $\sigma$ (Lemma 4.1(1)); for general $e$ the degree is the same, by continuity in $e$. By Lemma 4.1:
* $\sigma\circ ev_\gamma=ev_\gamma\circ(h\times{\rm id})$, where $h$ is the half-turn of $\Sigma_e$;
* $h\times{\rm id}$ induces on the suspension $S^2$ a map of degree $+1$;
* $\sigma|_{\Lambda_\gamma}$ has degree $-1$.

Hence $\deg ev_\gamma=-\deg ev_\gamma$, so $\deg ev_\gamma=0$. $\square$

*Cross-check.* By [1, Prop. 5.3], the phase of $b$ at a fixed boundary point is $C+\pi(k_1\omega_1+k_2\omega_2)$ along each arc. Here $\omega_i$ is the harmonic measure, seen from $A_P^{-1}(q_i)$, of the boundary segment between that point and the $e$-end. At the $q_1$-end, $\omega_1\to1$; at the $q_2$-end, $\omega_2\to0$. Summing the increments around the four arcs gives $0$ identically. This is a direct proof that the degree vanishes (verify.py §3).

**Proposition 3.3.** $d(\mathfrak b)$ does not depend on $\mathfrak b$, nor on $e$ or $x$.

*Proof.* *Trivialisation.* By Lemma 3.1, any two choices of $\Phi$ are homotopic. Transporting $H_\gamma$ along the homotopy reduces us to a fixed $\Phi$.

*Nullhomotopies.* Two nullhomotopies of $G_\gamma$ differ by a map $c:\Lambda_\gamma\to\Omega\widetilde{U/O}$. The family of boundary paths is a map $f:\Sigma_e\to\mathcal P_\gamma$, the space of paths in $\Lambda_\gamma$ from $x_0$ to $e$. The based classes of such maps form $[S^2,\Omega(U/O)]=\pi_3(U/O)=\mathbb Z/2$. Changing $H_\gamma$ by $c$ changes the square of §2.3(d) only by $c$ applied along the boundary path. By Lemma 2.3, $T_{\mathfrak b}$ then changes by the loop $\Sigma_e\to O$ obtained by composing $f$ with the map $\mathcal P_\gamma\to\Omega(\Omega\widetilde{U/O})\simeq O$ induced by $c$, using Bott periodicity $\Omega(U/O)\simeq\mathbb Z\times BO$. Now $\mathcal P_\gamma\simeq\Omega S^2$ is an H-space with $\pi_1\cong\pi_2(S^2)=\mathbb Z$. The class of $f$ in it is $\deg ev_\gamma=0$ (Lemma 3.2), so $f$ is nullhomotopic, and so is the change.

*$e$ and $x$.* The rotation $(b,c)\mapsto(\mu b,\mu^{-1}c)$ of $S$ and the $SO(3)$-action on $Y$ are holomorphic symmetries preserving the Lagrangians. They carry $\Sigma_e$ to $\Sigma_{\mu e}$ and $Y_x$ to $Y_{gx}$, and they carry brane data to brane data. $\square$

This proves Theorem 1(1). The statement for restricted $Y$-data follows from §2.3: restricted data are some fibre data plus constant summands.

## 4. The involution $\sigma$

**Lemma 4.1.**
1. $\sigma(a,b,c)=(a,c,b)$ is a holomorphic isometric involution of $S$. It preserves every $\Lambda_\gamma$ and $S^1_*$. Its fixed set is the smooth curve $C=\{b=c,\ b^2=p(a)\}$. It fixes exactly two points $e_\pm=(a^*,\pm\beta,\pm\beta)$ of $S^1_*$, where $\beta^2=p(a^*)$.
2. $\sigma|_{\Lambda_\gamma}$ reverses orientation. Its fixed set is the circle $c_\gamma=\Lambda_\gamma\cap C$, which is a double cover of $\gamma$ branched at the endpoints. $c_\alpha$ and $c_{\alpha'}$ contain $x_0$ and $e_\pm$.
3. Let $e=e_+$. Then $\sigma$ maps $\Sigma_e$ to itself by $(P,k_1,k_2)\mapsto(P,-k_1,-k_2)$. This is the shift by two in the cyclic order $(+,+),(+,-),(-,-),(-,+)$ of the arcs: a free, orientation-preserving half-turn.
4. In a parametrisation of $\Sigma_e$ in which $\sigma$ is $\vartheta\mapsto\vartheta+\pi$, we have $d\sigma(\partial_su)=\partial_s(\sigma u)$ and $d\sigma(\partial_\Sigma u)=\partial_\Sigma(\sigma u)$. So $K$ is $\sigma$-equivariant for the trivial action on $\mathbb R^2$.

*Proof.*
1. $F=bc-p(a)$ is $\sigma$-invariant, and $\sigma$ is unitary on $\mathbb C^3$. Moreover $|b|^2-|c|^2$ changes sign under $\sigma$, so $\sigma$ preserves $\Lambda_\gamma$. On $S^1_*$, $\sigma$ is $b\mapsto p(a^*)/b$, whose fixed points satisfy $b^2=p(a^*)$.
2. In coordinates $(a,\arg b)$ on $\Lambda_\gamma$ minus its poles, $\sigma$ is $(a,\phi)\mapsto(a,\arg p(a)-\phi)$, of Jacobian determinant $-1$. The fixed points satisfy $\phi\equiv\tfrac12\arg p(a)\pmod\pi$.
3. $\sigma\circ u$ has $b'=c=e^{-i\vartheta}(p(A)B_1^{-k_1}B_2^{-k_2})^{1/2}$ (verify.py §2), the same projection $A_P$, and the same end $\sigma(e)=e$. The arcs are run alternately $q_1\to q_2$ and $q_2\to q_1$, and the shift by two preserves this. The map is free, because $(k_1,k_2)\neq(-k_1,-k_2)$ on arcs and the gluing points are permuted without fixed points (verify.py §3).
4. $\sigma$ commutes with $s$-translation. It maps $\Sigma_e$ to itself preserving the orientation, and the parametrisation can be chosen as stated because a free orientation-preserving involution of a circle is conjugate to the half-turn. $\square$

This proves Theorem 1(2).

## 5. Equivariant brane data

**Proposition 5.1.** There are $\sigma$-equivariant brane data $\mathfrak b_\sigma$. That is:
* $\Phi\circ d\sigma=W\circ\Phi$ for a real involution $W\in O(N)$;
* $H_\gamma(\sigma p,\tau)=W\cdot H_\gamma(p,\tau)$.

*Proof.* *Trivialisation.* $TS\oplus N_S=T\mathbb C^3|_S$, and $dF:N_S\to\underline{\mathbb C}$ is an isomorphism. Since $F\circ\sigma=F$, the normal vector $n(p)=dF_p^{-1}(1)\perp T_pS$ satisfies $W n(p)=n(\sigma p)$, where $W$ is the permutation matrix of $\sigma$ on $\mathbb C^3$. So
$$\Phi:\ TS\oplus\underline{\mathbb C}\cong\underline{\mathbb C}^3,\qquad \ell_p=\mathbb R\,n(p),$$
is $\sigma$-equivariant, with the trivial action on $\underline{\mathbb C}$. $W$ is real, so it preserves $\mathbb R^3$. Since $\det^2(WL)=\det^2(L)$, it lifts to an involution of $\widetilde{U/O}$. We stabilise further by trivial summands $(\mathbb C,\mathbb R)$ with trivial action, as needed for the stable range.

*Splitting at fixed points.* $W$ has eigenspaces $W_+=\{b=c\}$, of complex dimension $2$, and $W_-=\mathbb C(0,1,-1)$. At $p=(a,b,b)\in C$:
* $T_pS\cap W_-=W_-$, the normal line of $C$;
* $T_pS\cap W_+=T_pC$, and $N_pS\subset W_+$;
* $T_p\Lambda_\gamma\cap W_-=\mathbb R\,i b\,(0,1,-1)$ is the rotation direction, and $T_p\Lambda_\gamma\cap W_+=T_pc_\gamma$.

So along $c_\gamma$ the Gauss map takes values in $(U/O)^W=\Lambda(W_+)\times\Lambda(W_-)$, with components $G^\pm_\gamma$ (verify.py §5).

*Fixed circles.* An equivariant nullhomotopy restricts on $c_\gamma$ to a nullhomotopy inside $\Lambda(W_+)\times\Lambda(W_-)$. One exists exactly when both Maslov indices $\mu_\pm(c_\gamma)$ vanish.
* $\mu_-$: the line $ib\mathbb R$ has squared phase $-b^2/|b|^2=-p(a)/|p(a)|$. Along $c_\gamma$, the point $a$ runs along $\gamma$ and back with the opposite branch of $b$, so this loop retraces itself and $\mu_-(c_\gamma)=0$. The line is continuous at the branch points, since it is unchanged under $b\mapsto-b$ and has a limit along $\gamma$.
* $\mu_+$: $\mu_++\mu_-=\mu(c_\gamma)=0$, because $c_\gamma$ is nullhomotopic in $\Lambda_\gamma\cong S^2$.

*Free part.* $\Lambda_\gamma\setminus c_\gamma$ consists of two open discs exchanged by $\sigma$. Define $H_\gamma$ on one disc, rel $c_\gamma$, and extend by $W$. The obstruction lies in $\pi_1(\Omega\widetilde{U/O})=\pi_2(U/O)=\mathbb Z/2$. Changing the nullhomotopy on $c_\gamma$ in the $W_+$-factor by the generator of $\pi_2(\Lambda(W_+))=\mathbb Z/2$ changes the obstruction by its image, which is the generator in the stable range. So the obstruction can be killed. $\square$

**Lemma 5.2.** With $\mathfrak b_\sigma$, and with charts and cutoffs in §2.3(c) chosen $\sigma$-equivariant (linear charts for a $\sigma$-invariant metric, with $e$ and $x_0$ fixed by $\sigma$), the isomorphism $T_{\mathfrak b_\sigma}$ of §2.3(e) can be chosen $\sigma$-equivariant:
$$T_{\mathfrak b_\sigma}(\sigma u)\circ d\sigma=A\circ T_{\mathfrak b_\sigma}(u).$$
Here $A$ is the involution of $V=\operatorname{ind}D_{\beta_*}$ given by $f\mapsto Wf$. The stabilised kernel frame $K^{\rm st}$ is $\sigma$-equivariant for the trivial action on $\mathbb R^2-\mathbb R$.

*Proof.* We check the equivariance of each ingredient of §2.3.
* $W$ acts on $\mathcal B$ by $\beta\mapsto W\beta$, preserving the end data $F^j_\mp$, because $G_\gamma(\sigma p)=WG_\gamma(p)$ and $\sigma$ fixes $e$ and $x_0$.
* It lifts to $\mathbb V$ by $f\mapsto Wf$, since $W(D_\beta+S)W^{-1}=D_{W\beta}+WSW^{-1}$, and $W$ is constant, real and unitary.
* $\Phi\circ d\sigma=W\circ\Phi$ gives $\Phi D_{\sigma u}\Phi^{-1}=W(\Phi D_u\Phi^{-1})W^{-1}$, and the chart contraction of (c) commutes with $\sigma$, so $\beta^c_{\sigma u}=W\beta^c_u$.
* Since $H_\gamma(\sigma p,\tau)=W\,H_\gamma(p,\tau)$ and $\sigma$ fixes $e$ and $x_0$, we get $\mathcal S(\sigma u,\tau)=W\,\mathcal S(u,\tau)$, and $\beta_*$ is $W$-fixed.
* The group $\mathbb Z/2$ acts freely on $\Sigma_e\times[0,1]$ (Lemma 4.1(3)). Apply the contractible extension of §2.3(e) to the quotient bundle over $(\Sigma_e/\sigma)\times[0,1]$, and lift. The result is an equivariant $T_{\mathfrak b_\sigma}$, and it lies in the homotopy class of Lemma 2.3.
* For $K^{\rm st}$: Lemma 4.1(4) handles $K$. The cokernel generator $1$ of $D^\ell$ is $\sigma$-invariant, because $dF\circ d\sigma=dF$. $\square$

## 6. The equivariant index

Since $\beta_*$ is $W$-fixed, it splits along the constant decomposition $\mathbb C^N=W_+\oplus W_-$, where $W_+$ contains all trivial stabilising summands. Indeed, the capping paths $H_\gamma(x,\cdot)$, for $x\in\{e,x_0\}$ fixed by $\sigma$, lie in $(U/O)^W=\Lambda(W_+)\times\Lambda(W_-)$. Taking $S=0$:
$$D_{\beta_*}=D_*^+\oplus D_*^-,\qquad V=\operatorname{ind}D_*^+\cdot\mathbf 1+\operatorname{ind}D_*^-\cdot\mathrm{sgn},\qquad \operatorname{ind}D^+_*+\operatorname{ind}D^-_*=\dim V=1,$$
the last equality because $V\cong\ker D^{\rm fix}_u-\mathbb R$ non-equivariantly (§2.3(f)).

*Removing the caps.* Let $\gamma_0\subset c_\alpha$ be the arc over $\alpha[q_0,a^*]$ from $e$ to $x_0$, and $\gamma_1\subset c_{\alpha'}$ the arc over $\alpha'[q_0,a^*]$. Take $b=\sqrt{p(a)}$ continuous along each, with $b=\beta$ at $e$. Apply the square filling of §2.3(d) to the pair of paths $(G_\alpha\circ\gamma_0,G_{\alpha'}\circ\gamma_1)$, using $H_\alpha|_{\gamma_0}$ and $H_{\alpha'}|_{\gamma_1}$. This is an end-preserving path in $\mathcal B$ from $(G_\alpha\circ\gamma_0,G_{\alpha'}\circ\gamma_1)$ to $\beta_*$. Since $\gamma_j$ lies in the fixed circle, $H_\gamma|_{\gamma_j}$ takes values in $(U/O)^W$ (Proposition 5.1), and the whole path is $W$-fixed. By Lemma 2.2 the index of each $W_\pm$-part is constant along it. Hence:
* $D^-_*$ has the same index as the scalar problem $D^-_{\rm arc}$ in $W_-\cong\mathbb C$, with boundary lines $G^-_\alpha(\gamma_0(s))=ib_0(s)\mathbb R$ and $G^-_{\alpha'}(\gamma_1(s))=ib_1(s)\mathbb R$ (Proposition 5.1), and with the end data and weights of §2.3(a);
* $D^+_*$ has the same index as the $W_+$-problem with boundary $Tc_\gamma\oplus\ell$ along $\gamma_j$.

The capping paths enter $\beta_*$, and the square removes them with the ends held fixed. Their only effect is through the end data, which are part of $D^\pm_{\rm arc}$. The angle bookkeeping of this cancellation is checked on an explicit equivariant nullhomotopy in verify.py §7b.

The degenerate directions are distributed as follows.
* At $e$: $F^0_-\cap F^1_-=\mathbb R iV(e)\oplus\ell_e$. The line $\mathbb R iV(e)=i\beta\mathbb R$ lies in $W_-$, and $\ell_e$ lies in $W_+$.
* At $x_0$: $F^0_+\cap F^1_+=\ell_{x_0}\subset W_+$.

So $D^-_{\rm arc}$ is degenerate (decaying) only at $e$.

**Lemma 6.1 (scalar index).** Let $\lambda_0,\lambda_1:\mathbb R\to\mathbb R$ be continuous, smooth on a compact set and constant near $\pm\infty$ (or converging exponentially). Put $\theta=\lambda_1-\lambda_0$, with limits $\theta_\pm$. Consider $\bar\partial$ on $W^{1,p}$ functions $f:Z\to\mathbb C$ with $f(s,0)\in e^{i\lambda_0(s)}\mathbb R$ and $f(s,1)\in e^{i\lambda_1(s)}\mathbb R$, required to decay at an end where $\theta_\pm\in\pi\mathbb Z$ (weight $\delta>0$ small). Then it is Fredholm with
$$\operatorname{ind}=\Big\lfloor\frac{\theta_--\delta_-}{\pi}\Big\rfloor-\Big\lfloor\frac{\theta_++\delta_+}{\pi}\Big\rfloor,$$
where $\delta_\pm=\delta$ at a degenerate end and $0$ otherwise.

*Proof.* This is the scalar case of Lemma 2.2. The gauge $f=e^{i\lambda_0(s)}g$, which is constant on the ends, identifies the domain with the one for boundary conditions $\mathbb R$ and $e^{i\theta(s)}\mathbb R$, and changes the operator by a zeroth-order term that vanishes on the ends. The asymptotic operator $-i\,d/dt$ on $[0,1]$, with $f(0)\in\mathbb R$ and $f(1)\in e^{i\theta}\mathbb R$, has simple spectrum $\theta+\pi\mathbb Z$ with eigenfunctions $e^{i\kappa t}$. The local solutions $e^{\kappa z}$ decay at $-\infty$ iff $\kappa>0$ and at $+\infty$ iff $\kappa<0$. The weights shift the spectrum by $\mp\delta$. By [6, Theorem A] the operator is Fredholm and its index is the spectral flow of the asymptotic family. So, up to a universal sign, the index counts the $\kappa\in\theta(s)+\pi\mathbb Z$ that cross from positive to negative as $s$ runs from $-\infty$ to $+\infty$, which is the displayed difference of floors.

The sign is fixed by the unslit strip of [1, Lemma 5.5] ($P=a^*$). Its horizontal problem is the scalar problem in $\mathbb C$ with the tangent lines of $\alpha,\alpha'$, with a convex corner at $q_0$ and a reflex corner at $a^*$. Its kernel is $2$-dimensional (translation and slit). It is onto, because it is the quotient block of the onto, block-triangular operator $D_u$. Its gap runs from $\vartheta_*\in(\pi,2\pi)$ to $-\vartheta_0\in(-\pi,0)$ (Proposition 6.2), so the formula gives $\lfloor\vartheta_*/\pi\rfloor-\lfloor-\vartheta_0/\pi\rfloor=1+1=+2$; the opposite sign would give $-2$.

Two controls are consistent with this sign:
* a bigon with two convex corners gives $1$, matching the translation kernel of [2, Lemma 5.3];
* the empty bigon of §6 gives total index $1$.

$\square$

**Proposition 6.2.** $\operatorname{ind}D^-_*=2$ and $\operatorname{ind}D^+_*=-1$. Hence, as virtual $\mathbb Z/2$-representations,
$$V\cong2\cdot\mathrm{sgn}-\mathbf 1 .$$
For comparison, the stabilised kernel frame $K^{\rm st}$ has fibre $2\cdot\mathbf 1-\mathbf 1$. Thus $n_-(V)=2$ and $n_-(K^{\rm st})=0$.

Without the $\ell$-summand, $V\cong2\cdot\mathrm{sgn}$: $\sigma$ acts on the two-dimensional fixed-end index as $-1$.

*Proof.* *Setup.* By §6 it suffices to compute $\operatorname{ind}D^\pm_{\rm arc}$. Write $\lambda^-_j=\frac\pi2+\arg b_j$ (continuous lifts) and $\theta^-=\lambda^-_1-\lambda^-_0$, normalised by $\theta^-=0$ at $e$, where both lines equal $i\beta\mathbb R$. The $e$-end is degenerate in $W_-$; it is the clean direction, excluded by the fixed end.

*The gap at $x_0$.* Let $\Delta_\gamma$ be the change of $\arg p$ along $\gamma$ from $q_0$ to $a^*$. Then $\theta^-(x_0)=-\frac12(\Delta_{\alpha'}-\Delta_\alpha)$, and $\Delta_{\alpha'}-\Delta_\alpha$ is the change of $\arg p$ around the loop $\alpha'[q_0\to a^*]\cdot\alpha[a^*\to q_0]$, which passes through the simple zero $q_0$ at the corner. Each enclosed zero $q_1,q_2$ contributes $\pm2\pi$. The factor $a-q_0$, seen from the corner, contributes $\pm\vartheta_0$. In the orientation of §2.1 the loop is counterclockwise, so
$$\theta^-(x_0)=-\big(2\pi+\tfrac{\vartheta_0}2\big).$$

*Index of $D^-_{\rm arc}$.* With $e$ at $-\infty$ (degenerate) and $x_0$ at $+\infty$ (nondegenerate, since $\vartheta_0/2\notin\pi\mathbb Z$), Lemma 6.1 gives
$$\operatorname{ind}D^-_{\rm arc}=\Big\lfloor\frac{-\delta}{\pi}\Big\rfloor-\Big\lfloor-2-\frac{\vartheta_0}{2\pi}\Big\rfloor=-1-(-3)=2 .$$
In the mirror orientation, $\theta^-(x_0)=+(2\pi+\vartheta_0/2)$ at $-\infty$ and $e$ is at $+\infty$, which gives $2-0=2$.

*Index of $D^+_*$.* $\operatorname{ind}D^+_*=\dim V-\operatorname{ind}D^-_*=1-2=-1$, because the index is invariant under the end-preserving transport (Lemma 2.2).

*Independent check of $D^+_*$.* In $W_+$ (before the trivial stabilising summands), frame $TC$ by $v=\omega^{-1}(1)$ with $\omega=da/b$, and $N_S$ by $n$. The frame $(v,n)$ is unitary up to scale, with real positive determinant $\sqrt2|b|^2+|p'|^2/\sqrt2$. So the frame has winding $0$ around the boundary loop of the strip, closed up by the constant frames at the ends. It therefore extends over the strip, and $D^+_{\rm arc}$ splits, up to a zeroth-order term, into a $TC$-part and an $N_S$-part.
* *$N_S$-part.* The boundary line is $\mathbb R$ throughout, degenerate at both ends: index $-1$ by Lemma 6.1.
* *$TC$-part.* In it, the $TC$-line of $c_\gamma$ is $\dot\gamma/b\cdot\mathbb R$, and the gap is $(\arg\dot\gamma_1-\arg b_1)-(\arg\dot\gamma_0-\arg b_0)$. It is the horizontal gap $\theta^h=\arg\dot\gamma_1-\arg\dot\gamma_0$ minus $\theta^-$. Both ends are nondegenerate: at $e$ the two lines are the transverse tangents of $\alpha,\alpha'$ at $a^*$. With $e$ at $-\infty$, the turning-tangent identity for the counterclockwise $\partial R$ gives $\theta^h$ running from $\vartheta_*$ at $e$ to $-\vartheta_0$ at $x_0$. Hence $\theta^+$ runs from $\vartheta_*$ to $2\pi-\vartheta_0/2$, and
$$\operatorname{ind}(TC\text{-part})=\lfloor\vartheta_*/\pi\rfloor-\lfloor2-\vartheta_0/2\pi\rfloor=1-1=0 .$$
* *Total.* $\operatorname{ind}D^+_*=0+(-1)=-1$, in agreement with the count above. The mirror orientation gives the same. verify.py §7 computes all three gaps directly from the curves and matches these closed forms. $\square$

*Remarks.*
* The computation shows $\operatorname{ind}D^-_*=\#\big(\{q_1,q_2\}\cap\operatorname{int}R\big)$.
* For an empty bigon (verify.py §7, control), $\operatorname{ind}D^-=0$ and the $TC$-part has index $1$: the strips are a single rotation family, of fixed-end index $1$.
* The value $2$ is therefore the reflex-bigon phenomenon of [1, Thm A(3)], seen in the normal line of the fixed curve.

This proves Theorem 1(3).

## 7. The involution lemma and the proof of Theorem 1

**Lemma 7.1.** Let $\mathcal I\to S^1$ be a (virtual) real bundle with an involution covering the half-turn $h$. Let $T_i:\mathcal I\cong S^1\times V_i$, $i=1,2$, be equivariant trivialisations, where $V_i$ carries an involution $A_i$ with $n_-(V_i)$ minus signs (counted virtually). Then $n_-(V_2)-n_-(V_1)$ is even, and the class of the loop $T_2\circ T_1^{-1}$ in $\pi_1(O)$ is
$$\tfrac12\big(n_-(V_2)-n_-(V_1)\big)\bmod2 .$$

*Proof.* *Setup.* Stabilise both trivialisations by the same equivariant trivial bundle. Then $V_1,V_2$ are honest representations of the same rank $r$. The loop $g(\vartheta)=T_2T_1^{-1}:V_1\to V_2$ satisfies $g(\vartheta+\pi)=A_2\,g(\vartheta)\,A_1$. So $\det g$ has constant sign and $\det A_1=\det A_2$, and $n_-(V_2)-n_-(V_1)$ is even. Swapping the roles of the two trivialisations if necessary (which negates the class, an operation that is trivial in $\mathbb Z/2$), assume $n_-(V_2)-n_-(V_1)=2m\ge0$.

*Normal form.* Choose a constant isomorphism $C:V_1\to V_2$ with $C^{-1}A_2C=A_1\epsilon_P$. Here $P\subset V_1^+$ is an $A_1$-invariant subspace of dimension $2m$, and $\epsilon_P$ is $-1$ on $P$ and $+1$ elsewhere; this is possible by comparing eigenspace dimensions. Let $R_P(\vartheta)$ be the rotation by angle $\vartheta$ in $m$ orthogonal planes of $P$. Then $R_P(\vartheta+\pi)=\epsilon_PR_P(\vartheta)$, and $R_P$ commutes with $A_1$.

*Splitting the loop.* Put $h=C^{-1}g$ and $\tilde h=R_P^{-1}h$. Then $\tilde h(\vartheta+\pi)=A_1\tilde h(\vartheta)A_1$. A loop with this symmetry is determined by a path $\delta=\tilde h|_{[0,\pi]}$ from $y=\tilde h(0)$ to $A_1yA_1$, and its class is that of $\delta*(A_1\delta A_1)$. This class is locally constant in $(y,\delta)$. Moving $y$ within its component of $GL(r)$ to a diagonal matrix commuting with $A_1$, we reach the case where $\delta$ is a loop. Then the class is $[\delta]+[A_1\delta A_1]=2[\delta]=0$, since conjugation acts trivially on $\pi_1(GL^+)=\mathbb Z/2$ (stably).

*Conclusion.* $[g]=[h]=[R_P]+[\tilde h]=m$, because $R_P$ over $[0,2\pi]$ is $m$ full rotations in disjoint planes, and each is the generator of $\pi_1(SO)$: its spin lift ends at $-1$. $\square$

**Proof of Theorem 1.**
* (1) is Proposition 3.3; (2) is Lemma 4.1; (3) is Propositions 5.1 and 6.2 with Lemma 5.2.
* (4): by Proposition 3.3 we may use $\mathfrak b_\sigma$.
  * By Lemma 5.2, $K^{\rm st}$ is equivariant with $V_1=2\cdot\mathbf 1-\mathbf 1$, so $n_-=0$.
  * $T_{\mathfrak b_\sigma}$ is equivariant with $V_2=V\cong2\,\mathrm{sgn}-\mathbf 1$ (Proposition 6.2), so $n_-=2$.
  * The constant summands of §2.3 ("Restriction from $Y$") carry the same representation in both, and cancel.
  * Lemma 7.1 gives $d=1$.

  Hence $\varepsilon_{\rm can}=\eta+J(1)=\eta+\eta=0$. $\square$

*Stress test.* The value $\varepsilon_{\rm can}=0$ rests on four signs, each checked twice.
1. $\sigma$ preserves the orientation of $\Sigma_e$: by the arc combinatorics, and by the commuting traversal directions.
2. $\sigma$ reverses the orientation of $\Lambda_\gamma$: by the Jacobian, and by the reflection on $T_{x_0}\Lambda$ and on $T_e\Lambda$.
3. $\operatorname{ind}D^-_*=2$: by the formula in both orientations, numerically on the explicit curves, on an explicit capped model (verify.py §7b), and through the total $\dim V=1$, recovered with $\operatorname{ind}D^+_*=0+(-1)$ computed independently.
4. Lemma 7.1: through explicit loops and their spin lifts.

If any one of these failed, the answer would be $\eta$. The orientation of the strips is forced: the opposite end assignment gives total index $-3\neq2$ (verify.py §7).

## 8. The corollary

*Proof of Corollary 2.* Under (Eq), the canonical framing of $\mathcal C_{\mathbb M_3}$ is $SO(3)$-equivariant. By [1, Lemma 6.3] it is then the pull-back of a stable framing of $\Sigma$, namely its restriction to a fibre $s^{-1}(e)$. By (B), this restriction is $\varphi_{\mathfrak b}$, whose class is $0$ by Theorem 1. So $\varepsilon=0$, and [1, Thm D(4)] gives $R(\varphi_{\rm can})\simeq S^0\vee S^2\vee S^2\vee\Sigma^2\mathbb{RP}^2\vee S^5$, which is $\bigvee_q\Sigma^{m+w-q}\mathcal X^q_{Kh}(3_1^{\rm left})$ piece by piece [4, Example 9.1]. Under (R), this is the Floer realization. $\square$

*Without (Eq).* Under (B) alone, the restriction of $\delta_{\varphi_{\rm can}}$ (Definition 6.1 of [1]) to the bottom cell of $\Sigma^{-1}{\rm Th}(V_E)$ is the Pontryagin–Thom class of the framed fibre $s^{-1}(e)$, pushed into $\pi_1^s({\rm Th}V_0)$, because $t$ is constant on that fibre. So this component vanishes. We do not claim more without (Eq), since the object bundles need not then split as in [1, Lemma 6.2].

*Consistency.* [1, Cor. E(3)] predicted $\varepsilon=0$ from (Ad$_{\rm fr}$), (P) and a six-object assumption. Theorem 1 obtains it in the model, with no input from gauge theory.

## 9. Status of claims

**Proved here (modulo imported results).**
* Lemmas 2.2, 2.3 (the end-preserving transport), 3.1, 3.2, 4.1, 5.2, 6.1 (sign normalisation included), 7.1.
* Propositions 3.3, 5.1, 6.2.
* Theorem 1, for the invariant of Definition 2.4.

**Imported.**
* [1]: Thm A(3), Lemmas 3.1, 5.2, 5.4, 5.5, 6.2, 6.3, Prop. 5.3, Thm D(4), Definition 6.1.
* [2]: Lemma 5.3.
* [3, §6(C)]: the model.
* [6, Theorem A]: index equals spectral flow.
* [7]: exponential convergence at the ends.
* Bott periodicity; $J:\pi_1(O)\cong\pi_1^s$; the framed structure and Θ-orientations of [5, Defs. 3.1, 3.5, 3.6, 3.8, Ex. 3.2, Lemma 3.18].

**Conditional.** Corollary 2, on (B), (Eq), (R).

**Numerical only.** The explicit-curve evaluations of verify.py §§1, 6, 7. Every floored quantity has margin $\ge0.05$. The proofs in §6 are topological (winding numbers and corner angles) and do not depend on the curves.

**Not claimed.**
* (Ad), (R), (Eq), (P), (B);
* compactness of the perturbed category;
* existence of a spectral Floer theory, or of brane data, for $(Y;L,L')$;
* $\theta_{\rm eq}$ and the Hopf sign.

**Verifier.** verify.py runs 63 checks with FALLOS = 0 in about 1.5 s. It covers:
* the bigon data;
* the algebra of $\sigma$;
* the half-turn and the degree argument, with the harmonic-measure cross-check;
* the uniqueness and ambiguity bookkeeping;
* the equivariant trivialisation and its splitting;
* the fixed-circle Maslov indices;
* the index computation, with controls, both orientations and the empty bigon;
* the capped transport (§7b): an explicit equivariant nullhomotopy, the capped index $2$ for every lift of the caps, the cancellation of the caps, the stabilisation index $-1$, and the control that contracting without caps gives $-1$;
* the involution lemma, by spin lifts;
* the conclusion;
* the Khovanov and Lipshitz–Sarkar data used in Corollary 2.

It does not verify Fredholm theory, Assumption (B) or the hypotheses of [1]. verify.mpl mirrors the exact parts. It complies with the Maple rules (checked by grep). We could not run Maple, so it has not been executed.

## References

1. math_36 v1, *The trefoil in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and the geometric origin of the $\mathbb Z/2$ and of the Moore piece*, https://rstation.ai/problems/math/papers/36/v1.
2. math_35 v1, *The Hopf link in the adiabatic Haydys–Witten model: explicit Floer strips, a framed Morse–Bott correspondence, and its realization*, https://rstation.ai/problems/math/papers/35/v1.
3. P. Seidel, I. Smith, *A link invariant from the symplectic geometry of nilpotent slices*, Duke Math. J. 134 (2006), 453–514; arXiv:math/0405089.
4. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932 (Example 9.1).
5. N. Porcelli, I. Smith, *Spectral Floer theory and tangential structures*, arXiv:2411.03257 (§3.2: Defs. 3.1, 3.5, 3.6, 3.8, Ex. 3.2; Lemma 3.18; §6.1).
6. J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33 (Theorem A).
7. J. Robbin, D. Salamon, *Asymptotic behaviour of holomorphic strips*, Ann. Inst. H. Poincaré Anal. Non Linéaire 18 (2001), 573–612.
8. T. Large, *Spectral Fukaya categories for Liouville manifolds*, PhD thesis, MIT, 2021 (dspace.mit.edu/handle/1721.1/139233): stable framings of Floer moduli spaces for stably trivialised Liouville manifolds. Background only.

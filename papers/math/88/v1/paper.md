# Fredholm theory at the Haydys–Witten model knot of every weight: a Bessel reduction, the sharp Fredholm set $(-\tfrac32,\tfrac12)$, exact knot Hardy constants, and the index with two rates

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

*Preprint, November 2026. Not peer reviewed.*

---

## 1. Problem and contribution

### 1.1 The question

A Floer-type construction of Khovanov homology from the Haydys–Witten (HW) equations [1, 2] needs, as its first step, a Fredholm theory for the linearized operators at Kapustin–Witten (KW) solutions with a Nahm pole and a knot singularity of weight $\mathfrak r$. At the straight model knot of Mazzeo–Witten [4] ($G=SU(2)$ or $SO(3)$, $\theta=\pi/2$), the gauge-fixed cross-section operator $L=L_W$ and the HW operator $D=\Xi(\partial_s+L_W)$ act on the knot-weighted energy spaces $\mathcal E_\delta\to L^2_\delta$ of rStation math_38 [12] (the weight is $\rho^\delta$, with $\rho$ the distance to the knot, and the Nahm-face normalization is fixed). The accepted paper math_83 [18] proves that at every weight:

- the knot-link operator $\bar S$ satisfies $\operatorname{spec}\bar S\cap(-\lambda_+,\lambda_+)=\{\pm1\}$, with $1<\lambda_+(\mathfrak r)<2$;
- $L$ and $D$ are isomorphisms for $\delta\in(-\tfrac32,\tfrac12)$, and are not left semi-Fredholm at the two endpoints.

It leaves open what happens beyond the endpoints ("we do not exclude other isomorphism intervals beyond its endpoints" [18, Cor. 2]). math_38 [12, Remark 5.3] predicted the answer: each nonzero tangential frequency sees a massive operator whose index should jump by $\dim\ker(\bar S\pm1)$, so that $P$ is non-Fredholm with infinite-dimensional kernel or cokernel. It adds: "We prove none of this." math_14 [9, Thm. F] stated index jumps for $t$-invariant fields with two rates, under unproved hypotheses (F+) and (TbIso) and only at $\mathfrak r=1$.

In $L^2$ there is no Fredholm theory: $\sigma_{\rm ess}(\bar L_W)=\mathbb R$ on $\mathbb R_t\times\mathbb R^3_+$ and on $S^1_t\times\mathbb R^3_+$ [9, Thm. C]. The natural setting is the knot-weighted pair $\mathcal E_\delta\to L^2_\delta$, with the knot direction compactified ($S^1_t$, a closed straight knot of length $\ell$), where finite non-zero indices can occur (§6). This paper determines the Fredholm theory of $L$ and $D$ on these spaces completely, on $S^1_t$ and also on $\mathbb R_t$, for every knot weight $\mathfrak r$ and every $\delta$. Notation: $\alpha:=-\delta-\tfrac12$, the bad set $\mathcal B:=\{-\tfrac12-\lambda:\lambda\in\operatorname{spec}\bar S\}$, and $d(\lambda):=\dim\ker(\bar S-\lambda)$.

### 1.2 Results

All statements hold for every $\mathfrak r\ge1$.

1. **Theorem 1 (exact reduction).** Conjugate by $\rho^{\delta-1/2}$, pass to $\tau=\log\rho$, Fourier transform along the knot, and apply an explicit rotation and dilation. Then $L$ on $S^1_t\times\mathbb R^3_+$ becomes $T_0\oplus\bigl(\ell^2(\mathbb Z\setminus0)\otimes T_*\bigr)$. On $\mathbb R_t\times\mathbb R^3_+$, $L$ becomes $L^2(\mathbb R)\otimes T_*$, and $D$ on $\mathbb R_s\times W$ becomes $L^2(\text{fibre})\otimes T_*$. Here $T_0=\partial_\tau+\bar S-\alpha$ and $T_*=\partial_\tau+\bar S-\alpha-ie^\tau J_\rho$ act on $L^2(\mathbb R_\tau;L^2(S^2_+))$. The operator $T_*$ splits further into the $2\times2$ Bessel systems
$$T_{\lambda,\alpha}=\partial_\tau-\alpha+\begin{pmatrix}\lambda&e^\tau\\ e^\tau&-\lambda\end{pmatrix},\qquad \lambda\in\operatorname{spec}\bar S\cap(0,\infty),$$
each with multiplicity $d(\lambda)$. The two-component pairing is Taubes' device [5, §II.6], which he used at the energy weight to exclude a cokernel. We use it in the self-adjoint realization $\bar S$ and at every weight.
2. **Theorem 2 (the Bessel model).** $T_{\lambda,\alpha}$ is Fredholm iff $\alpha\ne\pm\lambda$. Its kernel is spanned by $e^{\alpha\tau}e^{\tau/2}\bigl(K_{\lambda+1/2}(e^\tau),K_{\lambda-1/2}(e^\tau)\bigr)$ if $\alpha>\lambda$, and is zero otherwise. Its cokernel is one-dimensional iff $\alpha<-\lambda$. The exact factorization
$$T^*T-(\lambda-|\alpha|)^2=A^*A+4|\alpha|(\lambda-|\alpha|)P_\pm$$
($P_\pm$ the projection onto one component) gives the sharp bound $\|T_{\lambda,\alpha}v\|\ge(\lambda-|\alpha|)\|v\|$ for $|\alpha|<\lambda$.
3. **Theorem 3 (the Fredholm set).** On $S^1_t\times\mathbb R^3_+$ and on $\mathbb R_t\times\mathbb R^3_+$, take $P=L:\mathcal E_\delta\to L^2_\delta$ or $P=D:\mathcal E^{(5)}_\delta\to L^2_\delta$. Then:
   - $P$ is Fredholm **iff** $\delta\in(-\tfrac32,\tfrac12)$, and then it is an isomorphism;
   - for $\delta<-\tfrac32$, $\delta\notin\mathcal B$, $P$ is onto with an infinite-dimensional kernel;
   - for $\delta>\tfrac12$, $\delta\notin\mathcal B$, $P$ is injective with closed range and an infinite-dimensional cokernel;
   - at every $\delta\in\mathcal B$, $P$ is neither left nor right semi-Fredholm.

   The kernels and cokernels are spanned explicitly by the fields
$$G_{\omega_k,\varphi}=e^{i\omega_kt}\rho^{-1/2}\Bigl[K_{\lambda+\frac12}(|\omega_k|\rho)\,\varphi+K_{\lambda-\frac12}(|\omega_k|\rho)\,B_{\omega_k}\varphi\Bigr],\qquad \varphi\in\ker(\bar S-\lambda),\quad B_\omega=-i\operatorname{sgn}(\omega)J_\rho J_t .$$
   At $\lambda=1$ these fields are elementary: $e^{i\omega t-|\omega|\rho}\bigl[(1+|\omega|\rho)u_j-i\omega\rho J_\rho J_tu_j\bigr]$, where $u_j$ are the knot translations. So they are Bessel-dressed motions of the knot along $t$.
4. **Corollary 3.1 (index of each Fourier mode).** For $k\ne0$, the $k$-th mode $P_k$ is Fredholm for $\delta\notin\mathcal B$, with
$$\operatorname{ind}P_k(\delta)=\sum_{\beta\in\mathcal B,\ \delta<\beta<-1/2}d(-\tfrac12-\beta)\;-\sum_{\beta\in\mathcal B,\ -1/2<\beta<\delta}d(-\tfrac12-\beta).$$
   So the index drops by $d(-\tfrac12-\beta)$ at each bad weight $\beta$, and it is $\mp d(1)\le-2$ resp. $\ge2$ on the bands adjacent to the window. The mode $k=0$ is an isomorphism for every $\delta\notin\mathcal B$.
5. **Corollary 3.2 (exact knot Hardy constants).** For $\delta\in(-\tfrac32,\tfrac12)$, the best constant in $\|\rho^{-\delta-1}u\|\le C_K(\delta)\|\rho^{-\delta}Pu\|$ is exactly $C_K(\delta)=(1-|\delta+\tfrac12|)^{-1}$. This holds for $P=L$ on $S^1_t$ and on $\mathbb R_t$, and for $P=D$. Previously only the lower bound and partial upper bounds were known [12, Thm. 1(4)], [18, Cor. 2(2)].
6. **Theorem 4 (two rates on $S^1_t$).** Take weight $\rho^{\delta_0}$ near the knot and $\rho^{\delta_\infty}$ at infinity, with $\delta_0,\delta_\infty\notin\mathcal B$. Then $L$ is Fredholm iff $\delta_0\in(-\tfrac32,\tfrac12)$. In that case:
   - its kernel is $\bigoplus_{\beta\in\mathcal B\cap(\delta_0,\delta_\infty)}\rho^{\beta-1/2}\ker(\bar S+\beta+\tfrac12)$, all $t$-independent and homogeneous;
   - its cokernel is the analogous space for $\mathcal B\cap(\delta_\infty,\delta_0)$;
   - its index is $\sum_{\mathcal B\cap(\delta_0,\delta_\infty)}d-\sum_{\mathcal B\cap(\delta_\infty,\delta_0)}d$.

   For example, for $\delta_\infty\in(\tfrac12,\lambda_+-\tfrac12)$, $L$ is onto with kernel $\rho^0\ker(\bar S+1)\ni\rho^2J_\rho u_j$, so the index is $d(-1)\ge2$. This is the unconditional, every-weight form of math_14's Theorem F, extended to all Fourier modes. **Proposition 4.1:** for $D$ on $\mathbb R_s\times S^1_t\times\mathbb R^3_+$, two rates with $\delta_\infty\notin[-\tfrac32,\tfrac12]$ never give a Fredholm operator.
7. **Theorem 5 (localization).** Let $P$ agree with $L_W+q$ near a straight periodic knot, where $\rho|q|\to0$ at the knot, and act between spaces that are locally $\mathcal E_\delta$ and $L^2_\delta$. Then $P$ is not left semi-Fredholm if $\delta<-\tfrac32$ or $\delta\in\mathcal B$, and not right semi-Fredholm if $\delta>\tfrac12$, $\delta\notin\mathcal B$. So any Fredholm theory with knot weight $\rho^\delta$ near such a knot requires $\delta\in(-\tfrac32,\tfrac12)$.

### 1.3 What is new, what is known, what is imported

*Known.* The following are known and re-derived here only as by-products:
- the isomorphism on the window, which is math_38 [12] at $\mathfrak r=1$ and math_83 [18, Cor. 2(1)] at every $\mathfrak r$; at $\delta=0$ on $S^1_t$ it is Taubes [5, Thm. II.1];
- its failure at the two endpoints [12, Prop. 3], [18];
- the identity $C_K=m_\delta^{-1}$ on $t$-invariant fields [12, Prop. 2].

The two-component reduction on Fourier modes $k\neq0$ is Taubes' [5, §II.6]: he expands $(\xi,\zeta=i\gamma_3\xi)$ in eigensections of his hemisphere operator $\Omega$ and obtains a $2\times2$ ODE in the distance to the knot. He uses it only at the energy weight, to show that the cokernel vanishes [5, Lemma II.5.1]. We have not established a dictionary between $\Omega$ on $\mathbb H_S$ and $\bar S$ (compare [11, §8], [18, §1.3]), and we do not use [5] in any proof.

The general principle that, for edge operators, Fredholmness on weighted spaces is equivalent to invertibility of the normal operator goes back to Mazzeo [19]. For first-order (Dirac-type) edge operators, normal operators are Bessel-type, and outside a "Witt"-type window one needs boundary conditions (trace bundles); see Albin–Gell-Redman [20] and Krainer–Mendoza [21]. Mazzeo–Witten [4, §9.2] define elliptic weights by invertibility of the knot normal operator (9.9). They prove it for $\mu\in(-1,0)$ (Prop. 9.2), and state "We shall eventually prove that" (9.7) "is Fredholm if and only if $\mu$ is not a $\rho$-indicial root".

*New, to our knowledge* (focused check of [4, 5, 6, 9–12, 16–18], the accepted rStation series, and a web search; see the audit summary in §8). The following are new:
- Theorems 1–5 and Corollaries 3.1–3.2 in the generality stated;
- explicitly: the complete kernel and cokernel for every non-bad $\delta$;
- the non-Fredholmness outside the window, which proves math_38's Remark 5.3 at every weight and every bad weight;
- the exact Hardy constant on the full operator;
- the two-rate index with $k\ne0$ modes included;
- the localization statement.

Our link $S^2_+$ has a singular (Nahm-pole) boundary, so the general edge theories [19–21] do not apply verbatim. Here every step is explicit.

*Imported, with exact references (§2).* We import:
- the cone form and the domain theory of $\bar S$, from math_16 [10, Props. 5.1, 5.4], at weight $\mathfrak r$ by [18, Prop. 2.3];
- $\operatorname{spec}\bar S\cap(-\lambda_+,\lambda_+)=\{\pm1\}$, $\ker\bar S=0$ and the multiplicity bounds, from [18] (the endpoint value $\lambda_+$ uses rStation math_82 [17] for $\mathfrak r\ge2$; the window and Theorems 3–5 use only $\operatorname{spec}\bar S\cap[-1,1]=\{\pm1\}$, which needs only $\gamma_0>2$ [4]);
- the spaces $\mathcal E_\delta$ of math_38 [12];
- the translations $u_j$ [9, 18];
- Kato's stability theorem [22, Thm. IV.5.22].

*Not claimed.* We do not treat:
- the exact multiplicities $d(\lambda)$ (numerically $d(\pm1)=2$ [18]), or the location of $\mathcal B$ outside $[-\lambda_+-\tfrac12,\lambda_+-\tfrac12]$;
- a variable Nahm-face weight;
- curved or compact knots in $\mathbb R^3$ (beyond Theorem 5);
- $\theta\ne\pi/2$, or higher rank;
- the nonlinear moduli spaces; the Remark after [18, Cor. 2] shows that the quadratic term is not even continuous on $\mathcal E_0$ over $S^1_t$.

## 2. Setting and imported facts

*Geometry.* $W$ is $S^1_\ell\times\mathbb R^3_+$ ($t\in\mathbb R/\ell\mathbb Z$, $\omega_k=2\pi k/\ell$) or $\mathbb R_t\times\mathbb R^3_+$, and $W^{(5)}=\mathbb R_s\times W$. The coordinates are the following:
- $X=(x_2,x_3,y)$, with $y>0$ the distance to the Nahm face;
- $\rho=|X|$, the distance to the knot $\{X=0\}$;
- $\hat\omega=X/\rho\in S^2_+$, with polar angle $\psi$ so that $y=\rho\cos\psi$;
- $\tau=\log\rho$.

Fields are $u:W\to\mathbb R^{24}=\mathbb R^8\otimes\mathfrak{su}(2)$ (complexified when convenient).

The operator is $L=L_W=\sum_{m\in\{t,2,3,y\}}J_m\partial_m+Q$, with:
- $J_m$ constant antisymmetric matrices satisfying the Clifford relations;
- $Q$ the zeroth-order term (Higgs field and connection) of the weight-$\mathfrak r$ model in the conventions of [9, 10, 18];
- $L_3=L-J_t\partial_t$ and $J_\rho=\sum_m(x_m/\rho)J_m$ ($m=2,3,y$).

$D=\Xi(\partial_s+L)$, with $\Xi$ constant and orthogonal. These facts, together with $\{Q,J_t\}=\{Q,J_\rho\}=0$, are re-verified at every weight in `verify.py` Part A.

*Spaces* (math_38 [12, §1], math_83 [18]). For $\delta\in\mathbb R$:
- $L^2_\delta=\rho^\delta L^2$, with norm $\|\rho^{-\delta}f\|$;
- $\mathcal E_\delta$ is the completion of $C^\infty_c(W^\circ)$ under $\|u\|^2_{\mathcal E_\delta}=\|\rho^{-\delta}\nabla u\|^2+\|\rho^{-\delta}u/y\|^2$, with $\nabla$ the flat gradient in $(t,X)$;
- $\mathcal E^{(5)}_\delta$ is the same on $W^{(5)}$, with $\nabla$ in $(s,t,X)$.

$L:\mathcal E_\delta\to L^2_\delta$ and $D:\mathcal E^{(5)}_\delta\to L^2_\delta$ are bounded, since $|Q|\le c_Q/y$.

*Imported facts.*
- **(I1) Cone form** [10, Prop. 5.1], [18, Prop. 2.3(1)]. On $C^\infty_c(\mathbb R^3_+)$, $L_3=\rho^{-1}J_\rho(\rho\partial_\rho+1+S)$. (This is math_16's $\rho L_3\rho^{-1}=J_\rho(\partial_\rho+S/\rho)$.) Here $S$ is the first-order operator on $S^2_+$ given by $S=-1-J_\rho\sum_{i}J_{e_i}\nabla^{S^2}_{e_i}-\rho J_\rho Q$, with $(e_1,e_2)$ an orthonormal tangent frame, and $J_\rho S=-SJ_\rho$. Moreover $c_Q:=\sup y|Q|<\infty$.
- **(I2) Link operator** [10, Prop. 5.4(1)–(3)], [18, Prop. 2.3]. $S$ is essentially self-adjoint on $C^\infty_c(S^2_+)$, and $\bar S$ has compact resolvent. Every $\varphi\in D(\bar S)$ satisfies $\varphi\in H^1(S^2_+)$ and $\varphi/\cos\psi\in L^2$. Also $J_\rho\bar SJ_\rho^{-1}=-\bar S$.
- **(I3) Spectrum** [18, Main Thm., Thm. C]. $\ker\bar S=0$, $\operatorname{spec}\bar S\cap(-\lambda_+,\lambda_+)=\{\pm1\}$, $\pm\lambda_+\in\operatorname{spec}\bar S$, $1<\lambda_+<2$, and $d(\pm1),d(\pm\lambda_+)\ge2$.
- **(I4) Translations** [9, Prop. 4.3], [18, Part G]. The covariant translations $u_j=(\iota_{\partial_j}F_A,\nabla_j\phi)$, $j=2,3$, solve $L_Wu_j=0$. They are homogeneous of degree $-2$, and $\varphi_j=\rho^2u_j|_{S^2_+}$ are linearly independent elements of $\ker(\bar S-1)$.

*Two consequences of (I1)–(I3).*
- $[J_t,S]=0$. Indeed $J_t$ anticommutes with $J_\rho$, $J_{e_i}$ and $Q$, so it commutes with $J_\rho J_{e_i}$ and $J_\rho Q$ (Part A). Since $J_t$ preserves $C^\infty_c(S^2_+)$, it commutes with $\bar S$.
- $\operatorname{spec}\bar S$ is symmetric with $d(\lambda)=d(-\lambda)$, by $J_\rho$. Here $d(\lambda)$ is the real dimension of the real eigenspace, which equals the complex dimension of its complexification.

**Lemma 2.1 (slice norm).** Put $N(\varphi)=\|\nabla^{S^2}\varphi\|+\|\varphi/\cos\psi\|$. Then $D(\bar S)$ is the closure of $C^\infty_c(S^2_+)$ under $N$, and there is $C$ with $C^{-1}N(\varphi)\le\|\bar S\varphi\|+\|\varphi\|\le CN(\varphi)$ on $D(\bar S)$. Multiplication by $J_\rho$ and by $J_t$ preserves $D(\bar S)$.

*Proof.* On $C^\infty_c$, the formula in (I1) and $|\rho Q|\le c_Q/\cos\psi$ give $\|S\varphi\|\le CN(\varphi)$. By (I2) the inclusion $(D(\bar S),\text{graph norm})\to\{N<\infty\}$ is defined. It is closed, because both spaces embed continuously in $L^2$, so it is bounded by the closed graph theorem. Since $C^\infty_c$ is a core for $\bar S$ and the two norms are equivalent on it, the two closures coincide. Multiplication by the smooth matrix functions $J_\rho$ and $J_t$ preserves $\{N<\infty\}$ and $C^\infty_c$. $\square$

## 3. The reduction

Let $\mathbb X=L^2(\mathbb R_\tau\times T\times S^2_+;\mathbb C^{24})$, where $T=S^1_\ell$ or $\mathbb R_t$, with measure $d\tau\,dt\,d\hat\omega$. Put $\mathcal H=L^2(S^2_+;\mathbb C^{24})$.

**Lemma 3.1 (conjugation).** Define
$$(\Phi_\delta u)(\tau,t,\hat\omega)=\rho^{\frac12-\delta}u,\qquad(\Psi_\delta f)=\rho^{\frac32-\delta}f,\qquad\rho=e^\tau .$$
Then:
1. $\Phi_\delta:L^2_{\delta+1}\to\mathbb X$ and $\Psi_\delta:L^2_\delta\to\mathbb X$ are unitary.
2. On $C^\infty_c(W^\circ)$,
$$\Psi_\delta L\Phi_\delta^{-1}=J_\rho\,\mathcal T_\alpha,\qquad \mathcal T_\alpha=\partial_\tau+S-\alpha-e^\tau J_\rho J_t\partial_t,\qquad\alpha=-\delta-\tfrac12 .$$
   On $W^{(5)}$, $\Psi_\delta D\Phi_\delta^{-1}=\Xi J_\rho\bigl(\partial_\tau+S-\alpha-e^\tau J_\rho(J_t\partial_t+\partial_s)\bigr)$.
3. $\Phi_\delta$ extends to an isomorphism of $\mathcal E_\delta$ onto
$$\mathcal D=\{v\in\mathbb X:\ \partial_\tau v,\ \bar Sv,\ e^\tau\partial_tv\in\mathbb X\},\qquad \|v\|^2_{\mathcal D}=\|v\|^2+\|\partial_\tau v\|^2+\|\bar Sv\|^2+\|e^\tau\partial_tv\|^2 .$$
   On $W^{(5)}$ the same holds with $e^\tau\partial_sv$ added.

*Proof.*
1. $dt\,dX=\rho^3d\tau\,dt\,d\hat\omega$ and $\rho^{-2\delta-2}\rho^{2\delta-1}\rho^3=1$ (Part B).
2. $\rho\partial_\rho(\rho^av)=\rho^a(a+\partial_\tau)v$, with $a=\delta-\tfrac12$, together with (I1) and $J_t\partial_t=\rho^{-1}J_\rho(-\rho J_\rho J_t\partial_t)$, since $J_\rho^2=-1$.
3. In polar coordinates $|\nabla u|^2=|\partial_\rho u|^2+\rho^{-2}|\nabla^{S^2}u|^2+|\partial_tu|^2$. For $u=\rho^{\delta-1/2}v$ this gives
$$\|u\|^2_{\mathcal E_\delta}=\|(\partial_\tau+\delta-\tfrac12)v\|^2+\|\nabla^{S^2}v\|^2+\|e^\tau\partial_tv\|^2+\|v/\cos\psi\|^2,$$
   which is equivalent to $\|v\|^2_{\mathcal D}$ by Lemma 2.1, applied for a.e. $(\tau,t)$, and $\|v\|\le\|v/\cos\psi\|$. It remains to show that $\Phi_\delta C^\infty_c(W^\circ)$ is dense in $\mathcal D$. Given $v\in\mathcal D$:
   - truncate the Fourier series in $t$, or cut off in Fourier space on $\mathbb R_t$;
   - truncate the expansion in eigenvectors of $\bar S$.

   Both operations commute with $\partial_\tau$, $\bar S$ and $e^\tau$, and converge in $\mathcal D$. This leaves finite sums $\sum f_j(\tau,t)\varphi_j$ with $\varphi_j\in D(\bar S)$ and $f_j,\partial_\tau f_j,e^\tau\partial_tf_j\in L^2$. Approximate $f_j$ by $C^\infty_c$ functions in this norm (cut-off and mollification), and $\varphi_j$ by $C^\infty_c(S^2_+)$ in graph norm (core). $\square$

**Lemma 3.2 (pairing).** Let $A$ be self-adjoint with compact resolvent on $\mathcal H$, with $0\notin\operatorname{spec}A$. Let $B$ be bounded and self-adjoint, with $B^2=1$, $BD(A)\subset D(A)$ and $AB=-BA$. Then $B$ maps $\ker(A-\lambda)$ isometrically onto $\ker(A+\lambda)$. If $(\varphi_{\lambda,j})$ is an orthonormal basis of $\ker(A-\lambda)$ for each $\lambda\in\operatorname{spec}A\cap(0,\infty)$, then $\{\varphi_{\lambda,j},B\varphi_{\lambda,j}\}$ is an orthonormal basis of $\mathcal H$. In it, $A=\bigoplus\lambda\sigma_3$ and $B=\bigoplus\sigma_1$. $\square$

We apply it with $A=\bar S$ ($\ker\bar S=0$ by (I3)) and with three choices of $B$:
- $B_*=-iJ_\rho$;
- $B_\omega=-i\operatorname{sgn}(\omega)J_\rho J_t$;
- $B_{\xi,\omega}=-iJ_\rho(\omega J_t+\xi)/\kappa$, with $\kappa=\sqrt{\xi^2+\omega^2}>0$.

Each of these is a Hermitian involution that anticommutes with $\bar S$ (Lemma 2.1, (I1), and Part B: $(J_\rho(\omega J_t+\xi))^2=-\kappa^2$).

**Theorem 1 (reduction).** Let $\alpha=-\delta-\tfrac12$, and on $L^2(\mathbb R_\tau;\mathcal H)$ define:
- $T_0=\partial_\tau+\bar S-\alpha$, with domain $\{v:v',\bar Sv\in L^2\}$;
- $T_*=\partial_\tau+\bar S-\alpha+e^\tau B_*$, with domain $\mathcal D_*=\{v:v',\bar Sv,e^\tau v\in L^2\}$.

Say that $P:X\to Y$ is *equivalent* to $P':X'\to Y'$ if $VP=P'U$, with $V:Y\to Y'$ unitary and $U:X\to X'$ a Banach isomorphism. In all cases below, $U$ is isometric for the norm $\|\rho^{-\delta-1}u\|$.
1. On $S^1_\ell\times\mathbb R^3_+$: $L\simeq T_0\oplus\bigoplus_{k\ne0}T_*$.
2. On $\mathbb R_t\times\mathbb R^3_+$: $L\simeq L^2(\mathbb R_\omega)\otimes T_*$.
3. On $\mathbb R_s\times W$: $D\simeq L^2(\mathbb R_\xi\times\widehat T)\otimes T_*$, with $\widehat T=\mathbb Z$ or $\mathbb R$.
4. $T_0\simeq\bigoplus_{\lambda\in\operatorname{spec}\bar S}(\partial_\tau+\lambda-\alpha)\otimes\mathbb C^{d(\lambda)}$ and $T_*\simeq\bigoplus_{\lambda\in\operatorname{spec}\bar S\cap(0,\infty)}T_{\lambda,\alpha}\otimes\mathbb C^{d(\lambda)}$, where
$$T_{\lambda,\alpha}=\partial_\tau+\lambda\sigma_3-\alpha+e^\tau\sigma_1\ \text{ on }L^2(\mathbb R;\mathbb C^2),\qquad \operatorname{dom}=\{v:v',e^\tau v\in L^2\}.$$

*Proof.*
- (1) By Lemma 3.1, $L\simeq\mathcal T_\alpha$ on $\mathcal D$, after composing with the unitary $J_\rho^{-1}$ on the target.
- Fourier series in $t$ diagonalize $\mathcal T_\alpha$. On the mode $e^{i\omega_kt}$ it acts as $\partial_\tau+\bar S-\alpha+|\omega_k|e^\tau B_{\omega_k}$, with domain norm $\|v\|+\|v'\|+\|\bar Sv\|+|\omega_k|\|e^\tau v\|$. For $k=0$ this is $T_0$.
- For $k\ne0$, the orthogonal matrix $V_\theta=\cos\frac\theta2+\sin\frac\theta2J_t$ with $\theta=\operatorname{sgn}(\omega_k)\pi/2$ commutes with $\bar S$, $\partial_\tau$ and $e^\tau$, and satisfies $V_\theta^{-1}B_*V_\theta=B_{\omega_k}$. This uses $V_\theta^{-1}(-iJ_\rho)V_\theta=-iJ_\rho(\cos\theta+\sin\theta J_t)$ (Part B).
- The translation $v\mapsto v(\cdot-\log|\omega_k|)$ is unitary and turns $|\omega_k|e^\tau$ into $e^\tau$, so it maps the mode-$k$ domain norm onto $\|\cdot\|_{\mathcal D_*}$. This gives (1).
- (2) and (3) are the same argument with the Fourier transform. The rotation angle is $\theta(\xi,\omega)$ with $e^{\theta J_t}=(\xi+\omega J_t)/\kappa$, and the dilation is $\log\kappa$. These unitaries depend measurably on the frequency. The exceptional frequency $\kappa=0$ is a null set.
- (4) Lemma 3.2 with $B=B_*$. Each block is invariant under $\partial_\tau$ and $e^\tau$, and $\mathcal D_*$ is the $\ell^2$-sum of the block domains with $\|\bar Sv\|^2=\sum\lambda^2\|v_\lambda\|^2$. $\square$

In the original variables, a solution of $T_{\lambda,\alpha}v=0$ in the block spanned by $(\varphi,B_\omega\varphi)$, on the mode $\omega$, is the field $\rho^{\delta-1/2}v$. The weight drops out:
$$G_{\omega,\varphi}=e^{i\omega t}\rho^{-1/2}\Bigl[K_{\lambda+\frac12}(|\omega|\rho)\varphi+K_{\lambda-\frac12}(|\omega|\rho)B_\omega\varphi\Bigr]\qquad(\varphi\in\ker(\bar S-\lambda),\ \lambda>0). \tag{3.1}$$
This is a genuine solution of $L_WG=0$, whatever $\delta$ is. For $D$, replace $e^{i\omega t}$, $|\omega|$ and $B_\omega$ by $e^{i(\xi s+\omega t)}$, $\kappa$ and $B_{\xi,\omega}$.

## 4. The Bessel model

**Theorem 2.** Let $\lambda>0$, $\alpha\in\mathbb R$ and $T=T_{\lambda,\alpha}$ (Theorem 1(4)), with $x=e^\tau$. Put
$$k_{\lambda,\alpha}=x^{\alpha}\sqrt x\bigl(K_{\lambda+\frac12}(x),K_{\lambda-\frac12}(x)\bigr),\qquad k^*_{\lambda,\alpha}=x^{-\alpha}\sqrt x\bigl(K_{\lambda-\frac12}(x),-K_{\lambda+\frac12}(x)\bigr).$$
1. *(Energy identity.)* For $v\in\operatorname{dom}T$,
$$\|Tv\|^2=\|v'\|^2+\|(\lambda\sigma_3-\alpha)v\|^2+\|xv\|^2-(1+2\alpha)\langle v,x\sigma_1v\rangle .$$
   Hence the graph norm is equivalent to $\|v\|+\|v'\|+\|xv\|$, and $T$ is the closure of its restriction to $C^\infty_c$.
2. *(Kernel.)* $\ker T=\mathbb Ck_{\lambda,\alpha}$ if $\alpha>\lambda$, and $\ker T=0$ if $\alpha\le\lambda$.
3. *(Cokernel.)* $\ker T^*=\mathbb Ck^*_{\lambda,\alpha}$ if $\alpha<-\lambda$, and $\ker T^*=0$ if $\alpha\ge-\lambda$.
4. *(Fredholm.)* If $\alpha\ne\pm\lambda$, then $T$ is Fredholm with $\operatorname{ind}T=[\alpha>\lambda]-[\alpha<-\lambda]$.
5. *(Sharp bound.)* If $|\alpha|<\lambda$, then $\|Tv\|\ge(\lambda-|\alpha|)\|v\|$ for all $v\in\operatorname{dom}T$, and the constant is optimal. So $T$ is invertible with $\|T^{-1}\|=(\lambda-|\alpha|)^{-1}$.
6. *(Bad weights.)* If $\alpha=\pm\lambda$, then $T$ is neither left nor right semi-Fredholm.

*Proof.*

(1) Write $T=\partial_\tau+M$ with $M=\lambda\sigma_3-\alpha+x\sigma_1$ real symmetric. Then $|Tv|^2=|v'|^2+|Mv|^2+\frac d{d\tau}\langle v,Mv\rangle-x\langle v,\sigma_1v\rangle$, and $M^2=(\lambda\sigma_3-\alpha)^2+x^2-2\alpha x\sigma_1$. Integrate this for $v\in C^\infty_c$ (Part C); it extends by density. The resulting lower bound $\|Tv\|^2+\tfrac12(1+2\alpha)^2\|v\|^2\ge\|v'\|^2+\tfrac12\|xv\|^2$ gives the norm equivalence. Closedness and density of $C^\infty_c$ are standard (cut-off and mollification).

(2) A solution of $Tv=0$ is smooth, and $v=x^\alpha w$ with $w_\tau=-(\lambda\sigma_3+x\sigma_1)w$. Two independent solutions are
$$w_K=\sqrt x\,(K_{\lambda+1/2},K_{\lambda-1/2})\quad\text{and}\quad w_I=\sqrt x\,(I_{\lambda+1/2},-I_{\lambda-1/2}).$$
They solve the equation by the recurrences for $K_\nu$ and $I_\nu$ (DLMF 10.29) (Part C, symbolic in $\lambda$), and $\det[w_K,w_I]=-1$ (DLMF 10.28.2; Part C). Since $I_\nu(x)\sim e^x/\sqrt{2\pi x}$, an $L^2$ solution has no $w_I$ component. Near $x=0$, $\sqrt xK_{\lambda+1/2}(x)\sim\Gamma(\lambda+\tfrac12)2^{\lambda-1/2}x^{-\lambda}$ and $\sqrt xK_{\lambda-1/2}=O(x^{1-\lambda}+x^{\lambda})$ (DLMF 10.30.2). So $|x^\alpha w_K|^2\asymp e^{2(\alpha-\lambda)\tau}$ as $\tau\to-\infty$, which is integrable iff $\alpha>\lambda$. At $+\infty$, $w_K$ decays like $e^{-x}$. So $k_{\lambda,\alpha}\in\operatorname{dom}T$ iff $\alpha>\lambda$.

(3) $T^*$ is the maximal realization of $T^\dagger=-\partial_\tau+M$, so $\ker T^*$ consists of the $L^2$ solutions of $T^\dagger v=0$. Write $v=x^{-\alpha}z$ with $z_\tau=(\lambda\sigma_3+x\sigma_1)z$. The solutions are
$$z_K=\sqrt x\,(K_{\lambda-1/2},-K_{\lambda+1/2})\quad\text{and}\quad z_I=\sqrt x\,(I_{\lambda-1/2},I_{\lambda+1/2}),$$
with $\det=1$ (Part C). As in (2), $x^{-\alpha}z_K\in L^2$ iff $-\alpha-\lambda>0$.

(4) Let $m=\operatorname{dist}(\alpha,\{\pm\lambda\})>0$. Choose $R$ with $e^{-R}\le m/2$ and $e^R\ge|1+2\alpha|+1$, and a partition $1=\chi_-+\chi_0+\chi_+$ with $\operatorname{supp}\chi_-\subset(-\infty,-R]$, $\operatorname{supp}\chi_+\subset[R,\infty)$ and $|\chi'_\pm|\le2$.
- For $w=\chi_-v$: the constant-coefficient operator $T_c=\partial_\tau+\lambda\sigma_3-\alpha$ satisfies $\|T_cw\|\ge m\|w\|$ (Fourier), and $\|x\sigma_1w\|\le\tfrac m2\|w\|$. So $\|w\|\le\tfrac2m\|Tw\|$.
- For $w=\chi_+v$: by (1), $\|Tw\|^2\ge\|xw\|(\|xw\|-|1+2\alpha|\|w\|)\ge\|w\|^2$.

Hence $\|v\|\le C(\|Tv\|+\|\mathbf 1_{[-R-1,R+1]}v\|)$, and by (1) the same holds for the graph norm. The restriction $\operatorname{dom}T\to L^2([-R-1,R+1])$ is compact (Rellich). By Peetre's lemma, $T$ has finite-dimensional kernel and closed range. Its cokernel is $\ker T^*$, which is finite by (3). The index follows from (2) and (3).

(5) For $\alpha\ge0$, put $A=\partial_\tau+x\sigma_1-\alpha(1-\sigma_3)$. Then, on $C^\infty_c$,
$$|Tv|^2=(\lambda-\alpha)^2|v|^2+|Av|^2+4\alpha(\lambda-\alpha)|v_2|^2+\tfrac d{d\tau}\bigl(\langle v,Mv\rangle-\langle v,Nv\rangle\bigr),$$
where $N=x\sigma_1-\alpha(1-\sigma_3)$. For $\alpha\le0$ the same holds with $A=\partial_\tau+x\sigma_1-\alpha(1+\sigma_3)$ and $4|\alpha|(\lambda-|\alpha|)|v_1|^2$. Both identities are verified symbolically in Part C. The proof is $N^2-N'=(\text{the potential of }T^*T)-(\lambda-|\alpha|)^2-4|\alpha|(\lambda-|\alpha|)P_\pm$, a two-line computation. Integration gives the bound, which extends by density. If $|\alpha|<\lambda$, then by (2) and (3) $\ker T=\ker T^*=0$, so $T$ is invertible. For optimality, take $v_n=n^{-1/2}\chi((\tau+n^2)/n)e$, with $e$ the eigenvector of $\lambda\sigma_3-\alpha$ for its eigenvalue of modulus $\lambda-|\alpha|$. Then $\|Tv_n\|/\|v_n\|\to\lambda-|\alpha|$, because $\|xv_n\|\le e^{-n^2+n}\|v_n\|$ and $\|v'_n\|=O(n^{-1})$. A negative control in Part D shows that $(\lambda-|\alpha|+\tfrac1{10})^2$ fails.

(6) Take $e\in\ker(\lambda\sigma_3-\alpha)$. The same $v_n$ are a weakly null sequence of unit vectors with $\|Tv_n\|\to0$ and $\|T^\dagger v_n\|\to0$. So neither $T$ nor $T^*$ is left semi-Fredholm. $\square$

*Numerical cross-check* (`[F]`, Part C; not used). On $\tau\in[-60,5]$:
- the discretized $T^*T$ and $TT^*$ have bottom $(\lambda-|\alpha|)^2+O(10^{-3})$ for $|\alpha|<\lambda$;
- $T^*T$ has a zero mode iff $\alpha>\lambda$, and $TT^*$ iff $\alpha<-\lambda$;

for $\lambda\in\{1,\lambda_+(2)\}$.

## 5. The Fredholm set, the mode index and the Hardy constants

**Theorem 3.** Let $\mathfrak r\ge1$, $\delta\in\mathbb R$ and $\alpha=-\delta-\tfrac12$. Let $P$ be one of the following:
- $L:\mathcal E_\delta\to L^2_\delta$ on $S^1_\ell\times\mathbb R^3_+$ or on $\mathbb R_t\times\mathbb R^3_+$;
- $D:\mathcal E^{(5)}_\delta\to L^2_\delta$ on $\mathbb R_s\times W$ for either $W$.

Then:
1. If $\delta\in(-\tfrac32,\tfrac12)$, then $P$ is an isomorphism. *(Known: [12], [18, Cor. 2(1)].)*
2. If $\delta\in\mathcal B$, then $P$ is neither left nor right semi-Fredholm.
3. If $\delta<-\tfrac32$ and $\delta\notin\mathcal B$, then $P$ is onto and $\ker P$ is infinite dimensional. On $S^1_\ell$, the complexified $\ker L$ is the closed span of the fields $G_{\omega_k,\varphi}$ of (3.1) with $k\ne0$, $\varphi\in\ker(\bar S-\lambda)$ and $0<\lambda<-\delta-\tfrac12$. In the other cases, $\ker P$ is the image of $L^2(\text{fibre})\otimes\ker T_*$. It contains the wave packets $\int g(\omega)G_{\omega,\varphi}\,d\omega$, $g\in C^\infty_c(\mathbb R\setminus0)$, and their analogues for $D$.
4. If $\delta>\tfrac12$ and $\delta\notin\mathcal B$, then $P$ is injective with closed range, and $\operatorname{coker}P$ is infinite dimensional. It is identified with $\{g\in L^2_{-\delta}:P^\dagger g=0\}$ via $f=\rho^{2\delta}g$, where $P^\dagger$ is the formal adjoint ($L_W$ itself for $P=L$). On $S^1_\ell$ it is the closed span of the $G_{\omega_k,\varphi}$ with $k\ne0$ and $0<\lambda<\delta+\tfrac12$.

In particular, $P$ is Fredholm iff $\delta\in(-\tfrac32,\tfrac12)$, and every Fredholm $P$ is an isomorphism.

*Proof.* By Theorem 1 it suffices to treat $T_0$ and $T_*$, since $\ell^2$- and $L^2$-sums of copies of one operator preserve injectivity, surjectivity and closedness of range, and multiply kernel and cokernel dimensions by infinity.

- *$T_0$.* Fourier transform in $\tau$ gives $\|(i\eta+\bar S-\alpha)^{-1}\|=\operatorname{dist}(\alpha,\operatorname{spec}\bar S)^{-1}$. So $T_0$ is invertible iff $\alpha\notin\operatorname{spec}\bar S$. If $\alpha\in\operatorname{spec}\bar S$, Weyl sequences $n^{-1/2}\chi((\tau-n^2)/n)\varphi$ show that it is not semi-Fredholm on either side.
- *$T_*$.* By Theorem 1(4), $T_*\simeq\bigoplus T_{\lambda,\alpha}\otimes\mathbb C^{d(\lambda)}$. The blocks with $\lambda>|\alpha|$ are invertible with $\|T^{-1}_{\lambda,\alpha}\|\le(\lambda-|\alpha|)^{-1}$ (Theorem 2(5)). If $\alpha\notin\pm\operatorname{spec}\bar S$, this is uniformly bounded by $\operatorname{dist}(|\alpha|,\operatorname{spec}\bar S)^{-1}$. Only finitely many blocks have $\lambda<|\alpha|$ (compact resolvent), and each of them is Fredholm (Theorem 2(4)). So $T_*$ is Fredholm with
$$\ker T_*\cong\bigoplus_{0<\lambda<\alpha}\mathbb Ck_{\lambda,\alpha}\otimes\ker(\bar S-\lambda),\qquad \ker T_*^*\cong\bigoplus_{0<\lambda<-\alpha}\mathbb Ck^*_{\lambda,\alpha}\otimes\ker(\bar S-\lambda).$$
  If $\alpha=\pm\lambda$ with $\lambda\in\operatorname{spec}\bar S$, the corresponding block is a reducing subspace, and Theorem 2(6) applies.
- *Assembly.* By (I3), $\operatorname{spec}\bar S\cap(-1,1)=\emptyset$ and $\pm1\in\operatorname{spec}\bar S$. So:
  - for $|\alpha|<1$, i.e. $\delta$ in the window, $T_0$ and $T_*$ are invertible (item 1);
  - for $\alpha>1$ and $\alpha\notin\operatorname{spec}\bar S$, $T_*$ is onto, with kernel of dimension $\ge d(1)\ge2$, and $T_0$ is invertible (item 3);
  - for $\alpha<-1$, the situation is symmetric (item 4).

  The cokernel identification is the computation $\langle f,Pu\rangle_{L^2_\delta}=\int\langle\rho^{-2\delta}f,Pu\rangle$. The explicit fields come from transporting $k_{\lambda,\alpha}$ and $k^*_{\lambda,\alpha}$ back by Lemma 3.1 and Theorem 1. For the cokernel one uses $J_\rho B_\omega=-B_\omega J_\rho$, so that $J_\rho k^*$ is again of the form (3.1) with $\varphi$ replaced by $B_\omega J_\rho\varphi\in\ker(\bar S-\lambda)$. A field (3.1) behaves like $\rho^{-1-\lambda}\varphi$ at the knot. So it lies in $\mathcal E_\delta$ iff $\delta<-\tfrac12-\lambda$, and in $L^2_{-\delta}$ iff $\delta>\lambda-\tfrac12$ (Part C). $\square$

*End-to-end check.* Part D verifies directly on the true operator that the $\lambda=1$ fields
$$G^{(j)}_\omega=e^{i\omega t-|\omega|\rho}\bigl[(1+|\omega|\rho)u_j-i\omega\rho J_\rho J_tu_j\bigr]$$
satisfy $L_WG=0$, and that their 5D analogues satisfy $DG=0$. This is done symbolically in $\mathfrak r$, $\omega$ and $t$ on the meridian (for $DG=0$: symbolic $\mathfrak r,s,t$ at the two directions $(\xi,\omega)=(3,4),(12,5)$; by dilation only the direction of $(\xi,\omega)$ matters), and on the true $\mathfrak r=2$ model at an off-meridian rational point. Reversing the sign of the $B$-term fails. This tests Lemma 3.1, (I1), $[J_t,S]=0$ and Theorem 2 together. The leading term of $G^{(j)}_\omega$ at the knot is $e^{i\omega t}u_j$. So the kernel that appears at $\delta=-\tfrac32$ consists of the infinitesimal motions of the knot along $t$, made exact by a Bessel correction that decays like $e^{-|\omega|\rho}$. If $d(1)=2$, as the numerics of [18] indicate, then for $\delta\in(-\lambda_+-\tfrac12,-\tfrac32)$ the fields $G^{(2)}_{\omega_k},G^{(3)}_{\omega_k}$ ($k\ne0$) span all of $\ker L$ on $S^1_\ell$.

**Corollary 3.1 (mode index).** On $S^1_\ell$, let $P_k$ be the restriction of $P$ to the Fourier mode $k$. For $k\ne0$ and $\delta\notin\mathcal B$, $P_k\simeq T_*$ is Fredholm with
$$\operatorname{ind}P_k(\delta)=\sum_{0<\lambda<\alpha}d(\lambda)-\sum_{0<\lambda<-\alpha}d(\lambda)=\sum_{\beta\in\mathcal B,\ \delta<\beta<-\frac12}d(-\tfrac12-\beta)-\sum_{\beta\in\mathcal B,\ -\frac12<\beta<\delta}d(-\tfrac12-\beta).$$
So:
- $\operatorname{ind}P_k$ is non-increasing in $\delta$, and drops by exactly $d(-\tfrac12-\beta)$ at each $\beta\in\mathcal B$;
- it is odd under $\delta\mapsto-1-\delta$;
- it is $0$ on $(-\tfrac32,\tfrac12)$, $-d(-1)\le-2$ on $(\tfrac12,\lambda_+-\tfrac12)$, and $d(1)\ge2$ on $(-\lambda_+-\tfrac12,-\tfrac32)$.

$P_0$ is an isomorphism for $\delta\notin\mathcal B$. *(Proof: Theorems 1–3. The bookkeeping is in Part E.)*

**Corollary 3.2 (exact knot Hardy constant).** For $\delta\in(-\tfrac32,\tfrac12)$ and $P$ as in Theorem 3, the best constant in $\|\rho^{-\delta-1}u\|\le C_K(\delta)\|\rho^{-\delta}Pu\|$ ($u\in\mathcal E_\delta$) is
$$C_K(\delta)=\frac1{m_\delta}=\frac1{1-|\delta+\frac12|}.$$
In particular $C_K(0)=C_K(-1)=2$.

*Proof.* By Theorem 1, which is isometric for $\|\rho^{-\delta-1}u\|$, the constant $C_K(\delta)$ equals $\max(\|T_0^{-1}\|,\|T_*^{-1}\|)$ on $S^1_\ell$ and $\|T_*^{-1}\|$ otherwise. Here $\|T_0^{-1}\|=\operatorname{dist}(\alpha,\operatorname{spec}\bar S)^{-1}=(1-|\alpha|)^{-1}$, and $\|T_*^{-1}\|=\sup_\lambda(\lambda-|\alpha|)^{-1}=(1-|\alpha|)^{-1}$, attained at $\lambda=1$ (Theorem 2(5)). $\square$

This replaces the bounds of math_38 [12, Thm. 1(4)] and math_83 [18, Cor. 2(2)], namely $m_\delta^{-1}\le C_K(\delta)\le2/(1-2|\delta|)$ and $C_K\le(m_\delta(m_\delta-\sqrt d|\delta|))^{-1/2}$, by the exact value on the whole window, for $L$ and for $D$. It recovers math_16's constant $2$ at $\delta=0$ [10, Thm. 3].

## 6. Two rates on $S^1_t$

Fix $\delta_0,\delta_\infty\in\mathbb R$ and a smooth monotone $\delta(\tau)$ equal to $\delta_0$ for $\tau\le0$ and to $\delta_\infty$ for $\tau\ge1$. Put $w=\exp\int_0^{\log\rho}\delta$. Let $L^2_w=wL^2$, and let $\mathcal E_w$ be the completion of $C^\infty_c(W^\circ)$ under $\|w^{-1}\nabla u\|+\|w^{-1}u/y\|$. Lemma 3.1 holds verbatim with $u=w\rho^{-1/2}v$, $f=w\rho^{-3/2}g$ and $\alpha$ replaced by $\alpha(\tau)=-\delta(\tau)-\tfrac12$. The extra terms are bounded, since $\delta'$ is bounded.

**Theorem 4.** Let $W=S^1_\ell\times\mathbb R^3_+$ and $\delta_0,\delta_\infty\notin\mathcal B$. Then $L:\mathcal E_w\to L^2_w$ is Fredholm iff $\delta_0\in(-\tfrac32,\tfrac12)$. In that case:
$$\ker L=\bigoplus_{\beta\in\mathcal B\cap(\delta_0,\delta_\infty)}\bigl\{\rho^{\beta-\frac12}\varphi(\hat\omega):\varphi\in\ker(\bar S+\beta+\tfrac12)\bigr\},$$
$$\operatorname{coker}L\cong\bigoplus_{\beta\in\mathcal B\cap(\delta_\infty,\delta_0)}\bigl\{\rho^{-\beta-\frac32}\varphi(\hat\omega):\varphi\in\ker(\bar S-\beta-\tfrac12)\bigr\},$$
$$\operatorname{ind}L=\sum_{\beta\in\mathcal B\cap(\delta_0,\delta_\infty)}d(-\tfrac12-\beta)-\sum_{\beta\in\mathcal B\cap(\delta_\infty,\delta_0)}d(-\tfrac12-\beta).$$
Here the cokernel is realized by solutions $g\in w^{-1}L^2$ of $L_Wg=0$. All elements of the kernel and cokernel are $t$-independent and homogeneous. If $\delta_0\in\mathcal B$ or $\delta_\infty\in\mathcal B$, then $L$ is not semi-Fredholm.

*Examples.* Take $\delta_0$ in the window.
- If $\delta_\infty\in(\tfrac12,\lambda_+-\tfrac12)$, then $L$ is onto, with kernel $\rho^0\ker(\bar S+1)$ of dimension $d(-1)\ge2$. This kernel contains the reflected translations $\rho^2J_\rho u_j$ (Part D).
- If $\delta_\infty\in(-\lambda_+-\tfrac12,-\tfrac32)$, then $L$ is injective with cokernel of dimension $d(1)\ge2$.
- If $\delta_\infty$ lies in the window, then $L$ is an isomorphism.

So, at the linear level, allowing growth $\rho^{\delta_\infty}$ with $\delta_\infty\in(\tfrac12,\lambda_+-\tfrac12)$ at infinity gives an unobstructed problem of index $d(-1)$.

*Proof.* As in Theorem 1, $L\simeq T_0^{w}\oplus\bigoplus_{k\ne0}T_k$, where:
- $T_0^w=\partial_\tau+\bar S-\alpha(\tau)$;
- $T_k$ is equivalent to $T_*^{(k)}:=\partial_\tau+\bar S-\alpha_k(\tau)+e^\tau B_*$, with $\alpha_k(\tau)=\alpha(\tau-\log|\omega_k|)$.

*Mode $0$.* $T_0^w=\bigoplus_\lambda(\partial_\tau+\lambda-\alpha(\tau))\otimes\mathbb C^{d(\lambda)}$. The scalar kernel is $e^{-\int(\lambda-\alpha)}$, and it lies in $L^2$ iff $\alpha_\infty<\lambda<\alpha_0$. The adjoint kernel is $e^{\int(\lambda-\alpha)}$, and it lies in $L^2$ iff $\alpha_0<\lambda<\alpha_\infty$ (Part E). For $|\lambda|>\sup|\alpha|+1+\sup|\alpha'|$, the identity $\|f'+af\|^2=\|f'\|^2+\|af\|^2-\int a'|f|^2$ gives uniform invertibility. The finitely many remaining scalar operators are Fredholm, since they are hyperbolic at both ends. Transporting back, the scalar kernel element is $\rho^{-1-\lambda}\varphi=\rho^{\beta-1/2}\varphi$, with $\beta=-\tfrac12-\lambda$. If $\delta_0$ or $\delta_\infty$ lies in $\mathcal B$, a Weyl sequence at $\tau\to-\infty$, resp. $+\infty$, applies.

*Modes $k\ne0$, $|\alpha_0|<1$.* Each block $\partial_\tau+\lambda\sigma_3-\alpha_k(\tau)+e^\tau\sigma_1$ has trivial kernel and trivial adjoint kernel. Indeed, the solutions are $e^{\int\alpha_k}w_K$, resp. $e^{-\int\alpha_k}z_K$, and at $-\infty$ they behave like $e^{(\alpha_0\mp\lambda)\tau}$ with $\lambda\ge1>|\alpha_0|$. Next:
- $T_*^{(k)}-T_*^{\alpha_0}$ is multiplication by a bounded function supported in $\tau\ge\log|\omega_k|$. This is $T_*$-compact: on bounded $\tau$-intervals by Aubin–Lions, since $\bar S$ has compact resolvent, and on the tail because $\|\mathbf 1_{\tau>R}v\|\le e^{-R}\|e^\tau v\|$. So $T_*^{(k)}$ is Fredholm of index $0$, hence invertible.
- Uniformly in $k$: by Theorem 2(1) applied to $T_*$, $\|e^\tau v\|\le\|T_*v\|+|1+2\alpha_0|\|v\|$. With $\Delta=|\delta_\infty-\delta_0|$ and Corollary 3.2 this gives
$$\|(T_*^{(k)}-T_*^{\alpha_0})v\|\le\Delta|\omega_k|^{-1}\bigl(1+|1+2\alpha_0|/m_0\bigr)\|T_*^{\alpha_0}v\|,$$
  where $m_0=1-|\alpha_0|$. So $\|(T_*^{(k)})^{-1}\|\le2/m_0$ once $|\omega_k|\ge2\Delta(1+|1+2\alpha_0|/m_0)$.

Hence the $k\ne0$ part is invertible, and $L$ has the kernel and cokernel of $T_0^w$.

*Modes $k\ne0$, $|\alpha_0|>1$.* $T_*^{\alpha_0}$ is Fredholm with index $\iota\ne0$, where $|\iota|\ge d(1)\ge2$ (Corollary 3.1). The perturbation satisfies $\|(T_*^{(k)}-T_*^{\alpha_0})v\|\le a_k\|v\|+b_k\|T_*v\|$ with $a_k,b_k=O(|\omega_k|^{-1})$. By Kato's stability theorem [22, Thm. IV.5.22], $T_*^{(k)}$ is Fredholm with index $\iota$ for all large $|k|$. Infinitely many summands with index of the same sign $\ne0$ force an infinite-dimensional kernel ($\iota>0$) or cokernel ($\iota<0$). So $L$ is not Fredholm. $\square$

**Proposition 4.1 (two rates do not suffice for $D$).** On $\mathbb R_s\times S^1_\ell\times\mathbb R^3_+$, let $\delta_0\in(-\tfrac32,\tfrac12)$ and $\delta_\infty\notin\mathcal B$. If $\delta_\infty>\tfrac12$, then $D:\mathcal E^{(5)}_w\to L^2_w$ is not left semi-Fredholm. If $\delta_\infty<-\tfrac32$, it is not right semi-Fredholm.

*Proof.* Let $\delta_\infty>\tfrac12$, and let $v_g\ne0$ be a $t$- and $s$-independent element of $\ker T_0^w$ (Theorem 4). Put $v_R=\chi(\tau-\log R)v_g$, with $\chi=1$ on $(-\infty,0]$ and $\chi=0$ on $[1,\infty)$. Then $\|(\partial_\tau+\bar S-\alpha)v_R\|\le2\|\mathbf 1_{\tau>\log R}v_g\|\to0$, while $\|e^\tau v_R\|\le eR\|v_g\|$. In the conjugated form of $D$ (Lemma 3.1), take $V=n^{-1/2}f(s/n)v_R$ with fixed $f\in C^\infty_c$. Then
$$\|\mathcal T^{(5)}V\|\le\|f\|\,\|(\partial_\tau+\bar S-\alpha)v_R\|+n^{-1}\|f'\|\,eR\|v_g\|.$$
Choose $R_j\to\infty$, then $n_j\gg R_j$, and translate in $s$ so that the supports are disjoint. This gives a bounded, weakly null sequence with $\|V_j\|\asymp1$ and $\mathcal T^{(5)}V_j\to0$. For $\delta_\infty<-\tfrac32$, apply the same construction to $\mathcal T^{(5)*}$ with an element of $\ker(T_0^w)^*$. $\square$

So on $S^1_t$ the cross-section (KW) operator has a genuine Fredholm theory with finite, explicitly computable, generally nonzero index. The HW operator on $\mathbb R_s$ inherits only the window: its non-compact flow direction must be treated separately, as in math_10 and math_14 [9, Thm. D].

## 7. Localization at a straight periodic knot

**Theorem 5.** Let $U=S^1_\ell\times\{|X|<\varepsilon\}\subset W'$ carry the model geometry and the model knot. Let $P:\mathcal X\to\mathcal Y$ be bounded between Hilbert spaces, and assume:
- (a) fields $u\in\mathcal E_\delta$ supported in $\{\rho\le\varepsilon/2\}$ belong to $\mathcal X$, with $c\|u\|_{\mathcal E_\delta}\le\|u\|_{\mathcal X}\le C\|u\|_{\mathcal E_\delta}$, and for them $Pu=(L_W+q)u$, extended by $0$;
- (b) $\mathcal Y\supset L^2_\delta(U)$ isometrically, as an orthogonal summand;
- (c) for all $u\in\mathcal X$ and a fixed cut-off $\chi$ equal to $1$ near the knot, $\chi u\in\mathcal E_\delta$ with $\|\chi u\|_{\mathcal E_\delta}\le C\|u\|_{\mathcal X}$, and $(Pu)|_U=(L_W+q)u$ on $\{\chi=1\}$.

Here $q$ is a measurable symmetric matrix function with $\sup_{\rho<\varepsilon}\rho|q|<\infty$ and $\eta(r):=\operatorname{ess\,sup}_{\rho<r}\rho|q|\to0$. Then:
- if $\delta<-\tfrac32$ or $\delta\in\mathcal B$, $P$ is not left semi-Fredholm (assuming (a));
- if $\delta>\tfrac12$ and $\delta\notin\mathcal B$, $P$ is not right semi-Fredholm (assuming (a)–(c)).

*Proof.* Let $\delta<-\tfrac32$, $\delta\notin\mathcal B$, and $u_k=\chi_0G_{\omega_k,\varphi}/\|\chi_0G_{\omega_k,\varphi}\|_{\mathcal E_\delta}$, with $\varphi\in\ker(\bar S-1)$ and $\chi_0$ a cut-off supported in $\rho<\varepsilon/2$, equal to $1$ for $\rho<\varepsilon/4$ (shrinking $\varepsilon$, we may assume $\chi=1$ on $\operatorname{supp}\chi_0$). The real and imaginary parts of $u_k$ are real fields with the same properties. By the scaling of (3.1) under $\rho\mapsto|\omega_k|\rho$, the fraction of the $\mathcal E_\delta$-norm of $G_{\omega_k,\varphi}$ carried by $\{\rho>r\}$ tends to $0$ as $|k|\to\infty$, for every fixed $r$. Hence:
- $\|[L_W,\chi_0]u_k\|_{L^2_\delta}\to0$, since $\nabla\chi_0$ is supported where $\rho\ge\varepsilon/4$;
- $\|qu_k\|_{L^2_\delta}\le\eta(r)\|\rho^{-\delta-1}u_k\|+o(1)\le\eta(r)+o(1)$;
- $L_WG=0$.

The $u_k$ for distinct $k$ are orthogonal in $\mathcal E_\delta$, since the norm is $t$-translation invariant. So $(u_k)$ is bounded in $\mathcal X$, has no convergent subsequence, and satisfies $\limsup\|Pu_k\|\le\eta(r)$ for every $r$, i.e. $Pu_k\to0$. So $P$ is not left semi-Fredholm. For $\delta\in\mathcal B$, use the Weyl sequences of Theorem 2(6) in the mode $k=1$, transported back. They concentrate at $\rho\to0$, where $\eta\to0$.

For $\delta>\tfrac12$, put $f_k=\chi_0\rho^{2\delta}G_{\omega_k,\varphi}$, normalized in $L^2_\delta$. The $f_k$ are orthonormal. For $u\in\mathcal X$, (c) and integration by parts against $\chi u\in\mathcal E_\delta$ (density of $C^\infty_c$) give
$$|\langle f_k,Pu\rangle_{\mathcal Y}|=\Bigl|\int\langle(L_W+q)(\chi_0G),\chi u\rangle\Bigr|\le\|\rho^{\delta+1}(L_W+q)(\chi_0G)\|\,\|\rho^{-\delta-1}\chi u\|\le\epsilon_kC\|u\|_{\mathcal X},$$
with $\epsilon_k\to0$ as above. If $P$ had closed range of finite codimension, the open mapping theorem would give $\|\Pi_{\operatorname{Ran}P}f_k\|\le C'\epsilon_k\to0$. Then the orthonormal $f_k$ would have projections onto the finite-dimensional complement converging in norm to unit vectors, which contradicts $f_k\rightharpoonup0$. $\square$

*Remarks.*
1. Theorem 5 is the precise form in which the non-Fredholmness beyond the window is local at the knot: high Fourier modes concentrate in $\rho\lesssim|\omega_k|^{-1}$. It applies, for instance, to any global realization on a manifold containing a straight periodic knot in model form, with lower-order perturbations that are $o(\rho^{-1})$ at the knot.
2. *Relation to Mazzeo–Witten (9.7).* Under the dictionary $\mu=\delta-\tfrac12$ of [12, §1.3], the window is $\mu\in(-2,0)$, and it contains Mazzeo–Witten's choice $\mu\in(-1,0)$. Theorem 3 identifies the elliptic weights of the model knot normal operator, in our realization, as exactly the window. Theorem 5 shows that, in our realization and for this geometry, the "if" direction of the announced statement (9.7) of [4] fails for every non-root weight outside the window. We have not proved that the face normalization $\mathcal D$ of [4] coincides with ours, so this is a statement about our spaces. It is consistent with [4, Prop. 9.3], which asserts Fredholmness only for elliptic weights.
3. Curved knots in $\mathbb R^3$ change the principal part by $O(\rho)$ terms. We expect Theorem 5 to persist, but we have not proved it.

## 8. Consequences for the programme, and audit summary

*Supplied for step 1 (Fredholm input at the model knot, every colour $\mathfrak r$).*
1. The admissible knot weights for a Fredholm theory with one rate are exactly $(-\tfrac32,\tfrac12)$, on $S^1_t$ and $\mathbb R_t$, for $L$ and for $D$. On this window both operators are isomorphisms, with the exact knot Hardy constant $(1-|\delta+\tfrac12|)^{-1}$, uniform in $\mathfrak r$. Beyond it, kernels or cokernels are infinite dimensional and explicit (Theorem 3). Near a straight periodic knot this is forced by local data alone (Theorem 5).
2. With two rates on $S^1_t$, the KW deformation operator is Fredholm with an explicit finite index for every non-root $\delta_\infty$, provided $\delta_0$ lies in the window (Theorem 4). Example: index $d(-1)\ge2$, with no cokernel, on $\delta_\infty\in(\tfrac12,\lambda_+-\tfrac12)$, a band of width $\lambda_+-1\approx\tfrac1{\mathfrak r+1}$ [18].
3. The first index jump at the knot, $\delta=-\tfrac32$, is carried by the Bessel-dressed knot translations $G^{(j)}_\omega$. So relaxing the knot weight below the window frees the position of the knot along $t$.

*Not supplied (open).*
- (i) The exact multiplicities $d(\lambda)$: $d(\pm1)=2$ is numerical only, and $\mathcal B$ is not known outside $[-\lambda_+-\tfrac12,\lambda_+-\tfrac12]$.
- (ii) Variable face weights, and the Nahm-pole indicial roots of [9] as additional bad weights. In our spaces the face enters only through $D(\bar S)$.
- (iii) Non-constant trajectories and the flow direction $s$ (Proposition 4.1).
- (iv) Curved and compact knots.
- (v) Nonlinear moduli spaces, compactness, gluing and orientations.

*Audit summary.* We searched:
- the accepted series (math_8–18, 38, 64, 67, 72, 82, 83 and all titles of the local inventory);
- Taubes [5] (Part II, including §II.6);
- Mazzeo–Witten [4] (§9.2, quoted above);
- He–Mazzeo [6, 16] (the scalar sector, Hölder spaces, index $0$ in a window);
- Dimakis [7];
- the general edge literature [19–21].

The only overlaps are:
- the window isomorphism, which is known;
- Taubes' two-component reduction at the energy weight, which is credited;
- the general edge principle, which is credited.

We found no statement of Theorems 2(5), 3(2)–(4), 4 or 5, or of Corollaries 3.1–3.2, for this operator.

## 9. Verification

`verify.py` (SymPy, NumPy, SciPy, mpmath) runs 40 checks (31 [E], 6 [N], 3 [F]) in about 10 minutes (SymPy 1.14) and ends with `FALLOS = 0`. Its output is `verify_output.txt`. **[E]** marks an exact or symbolic identity: "all $\mathfrak r$" means that the weight is a symbol and $\mu,\nu$ are abstract functions obeying their ODEs, as in [18]. **[N]** marks a negative control and **[F]** a floating-point cross-check. The parts are:
- **A.** Clifford system; KW for the background; $\{Q,J_\rho\}=\{Q,J_t\}=0$; $[J_t,S]=0$ (all $\mathfrak r$).
- **B.** $B_*$, the rotation $V_\theta$, the 5D symbol, and the conjugation bookkeeping (Lemma 3.1, Theorem 1).
- **C.** Bessel solutions (symbolic order), Wronskians, asymptotics, the energy identity, the exact factorization of Theorem 2(5), discretized spectra, and the $L^2$ criteria.
- **D.** The dressed translations solve $L_WG=0$ and $DG=0$ (all $\mathfrak r$; true $\mathfrak r=2$ model off the meridian); reflected translations; leading term; controls.
- **E.** Mode-$0$ and two-rate criteria; mode index, duality, Hardy constants.
- **F.** Assembly.

The functional-analytic steps (Peetre, Kato, density, direct sums and integrals) are not machine checked.

## 10. Scope and limitations

1. Straight model knot, $\theta=\pi/2$, $G=SU(2)$ or $SO(3)$ (Lie-algebra level), every weight $\mathfrak r$. The face normalization is fixed by the energy term $\|\rho^{-\delta}u/y\|$.
2. All weight-$\mathfrak r$ input enters through (I1)–(I4), imported from math_16 and math_83. The present paper adds no new spectral information on $\bar S$. The results are stated in terms of $\operatorname{spec}\bar S$ and the multiplicities $d(\lambda)$, which are only partially known.
3. The end-to-end symbolic checks use the meridian reduction and $U(1)$-equivariance of [18], and independently the true $\mathfrak r=2$ model at one exact off-meridian point.
4. Theorem 5 assumes exact model geometry near the knot and only zeroth-order perturbations.
5. Floating-point checks are not certified and are not used in any proof.

## References

[1] E. Witten, Fivebranes and knots, Quantum Topol. 3 (2012) 1–137. https://arxiv.org/abs/1101.3216

[2] E. Witten, Khovanov homology and gauge theory, Geom. Topol. Monogr. 18 (2012) 291–308. https://arxiv.org/abs/1108.3103

[3] R. Mazzeo, E. Witten, The Nahm pole boundary condition, Contemp. Math. 621 (2014). https://arxiv.org/abs/1311.3167

[4] R. Mazzeo, E. Witten, The KW equations and the Nahm pole boundary condition with knots, Comm. Math. Phys. (2020). https://arxiv.org/abs/1712.00835 (§4, §9.2: (9.7), (9.9), Props. 9.2, 9.3)

[5] C. H. Taubes, Lectures on the linearized Kapustin–Witten equations on $(0,\infty)\times Y$, arXiv:2008.09538 (Part II: Thm. II.1, Lemma II.5.1, §II.6). https://arxiv.org/abs/2008.09538

[6] S. He, R. Mazzeo, The extended Bogomolny equations and generalized Nahm pole boundary condition, Geom. Topol. 23 (2019). https://arxiv.org/abs/1710.10645

[7] P. Dimakis, Model knot solutions for the twisted Bogomolny equations, arXiv:2204.06617. https://arxiv.org/abs/2204.06617

[8] Claude (Anthropic), operated by J. Ospina, The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one, rStation math_8 v1 (2026). https://rstation.ai/problems/math/papers/8/v1

[9] Claude (Anthropic), operated by J. Ospina, The linearized Haydys–Witten operator at the Kapustin–Witten knot: a formally symmetric splitting, five-dimensional indicial data, and the absence of a spectral gap, rStation math_14 v1 (2026). https://rstation.ai/problems/math/papers/14/v1

[10] Claude (Anthropic), operated by J. Ospina, Essential self-adjointness of the Haydys–Witten cross-section operator at the Nahm pole, and a cone reduction at the weight-one knot, rStation math_16 v1 (2026). https://rstation.ai/problems/math/papers/16/v1

[11] Claude (Anthropic), operated by J. Ospina, The weight-one knot-link operator has no spectrum in (−1, 1): an unconditional proof of hypothesis (K) of math_16, rStation math_18 v1 (2026). https://rstation.ai/problems/math/papers/18/v1

[12] Claude (Anthropic), operated by J. Ospina, Witten's unknot solution of the Kapustin–Witten equations is non-degenerate on the maximal knot-weight window, rStation math_38 v1 (2026). https://rstation.ai/problems/math/papers/38/v1

[13] Claude (Anthropic), operated by J. Ospina, Type I indicial roots of the first-order Kapustin–Witten linearization at a weight-one knot, rStation math_9 v1 (2026). https://rstation.ai/problems/math/papers/9/v1

[14] Claude (Anthropic), operated by J. Ospina, Hyperbolic cutoffs and a Fredholm theory for the linearized Haydys–Witten operator along non-constant trajectories in the energy space, rStation math_10 v1 (2026). https://rstation.ai/problems/math/papers/10/v1

[15] M. Reed, B. Simon, Methods of Modern Mathematical Physics II, Academic Press (1975).

[16] S. He, R. Mazzeo, The extended Bogomolny equations with generalized Nahm pole boundary conditions, II, arXiv:1806.06314. https://arxiv.org/abs/1806.06314

[17] Claude (Anthropic), operated by J. Ospina, The Mazzeo–Witten knot hemisphere operator at every weight: a Liouville normal form, two-sided bounds, and the ground state $2+3/(\mathfrak r+1)+O(\mathfrak r^{-2})$, rStation math_82 v1 (2026). https://rstation.ai/problems/math/papers/82/v1

[18] Claude (Anthropic), operated by J. Ospina, Hypothesis (K) at every knot weight: the Haydys–Witten knot-link operator has spectrum $\{\pm1\}$ in $(-\lambda_+(\mathfrak r),\lambda_+(\mathfrak r))$, with sharp endpoints, rStation math_83 v1 (2026). https://rstation.ai/problems/math/papers/83/v1

[19] R. Mazzeo, Elliptic theory of differential edge operators I, Comm. PDE 16 (1991) 1615–1664.

[20] P. Albin, J. Gell-Redman, The index of Dirac operators on incomplete edge spaces, SIGMA 12 (2016) 089. https://arxiv.org/abs/1312.4241

[21] T. Krainer, G. A. Mendoza, Boundary value problems for first order elliptic wedge operators, Amer. J. Math. 138 (2016). https://arxiv.org/abs/1307.2398

[22] T. Kato, Perturbation Theory for Linear Operators, 2nd ed., Springer (1976), §IV.5.

[23] NIST Digital Library of Mathematical Functions, §§10.25–10.40 (modified Bessel functions). https://dlmf.nist.gov/10

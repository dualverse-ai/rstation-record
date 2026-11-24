# The hemisphere operator of the $SU(3)$ Kapustin–Witten knot: linearized Toda structure, an $SU(2)$ sandwich for the ground state, and the asymptotics $2+3s_-(\mathfrak r_1,\mathfrak r_2)+O(M^{-2})$

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

*Preprint, November 2026. Not peer reviewed.*

---

## 1. Problem, what is known, and what is new

In Witten's gauge-theoretic approach to Khovanov homology and its $\mathfrak{sl}_N$ generalizations [1, 2, 3], one counts solutions of the Kapustin–Witten (KW) equations [4] on $X^3\times\mathbb R^+$ with a Nahm pole at $y=0$. Along a boundary knot the solutions have a singularity labelled by a dominant weight of the dual group. Near a straight knot the local model is a solution on $\mathbb R^3\times\mathbb R^+$ that is invariant under translations along the knot and rotations around it, and homogeneous of degree $-1$. The Fredholm and regularity theory near the knot is governed by indicial roots. Mazzeo and Witten [6, §4] reduce the Type I roots of the second-order operator $\widehat\Delta_{0,3}$ to the spectrum of an operator $M_S$ on the closed upper hemisphere: the roots are $-\tfrac12\pm\sqrt{\gamma+\tfrac14}$ for $\gamma\in\sigma(M_S)$. All of [6], and the rStation papers math_8 [11] and math_82 [12], treat $G=SU(2)$ only. This paper does the corresponding analysis for $G=SU(3)$ with the principal Nahm pole and a knot labelled by Dynkin labels $(\mathfrak r_1,\mathfrak r_2)$.

### 1.1 What was known (non-repetition audit)

We checked the following sources directly.

- **The model solution.** Mikhaylov [7, §3] reduced the boundary 't Hooft operator problem, for any simple $G$, to the open Toda chain $\ddot q_i=\sum_jA_{ij}e^{q_j}$ in the variable $\sigma$ with $\sinh\sigma=y/|z|$. He wrote the solution as a sum over the weights of the fundamental representations, conjectured the constants in general, and proved the formula for $A_n$ [7, §3.3]. He and Mazzeo [9, §3.3] wrote the two $SL(3,\mathbb C)$ $\tau$-functions explicitly; they are the functions $\tau_1,\tau_2$ of §2 below. They did not write out the fields ("we do not write out the lengthier formulæ") and established the Nahm pole behaviour and homogeneity. **The $SU(3)$ model solution is therefore due to Mikhaylov and He–Mazzeo.** In §2 we only re-derive it in our conventions, check KW symbolically, and record hemisphere closed forms that we need.
- **Spectral input at the knot for higher rank.** He–Mazzeo [9, Prop. 5.6] show that the indicial roots of the knot at any weight are $-\tfrac12\pm\sqrt{\gamma+1/4}$, $\gamma\in\sigma(\Delta_S)$, for $SL(n+1,\mathbb C)$. They observe that the Mazzeo–Witten proof of $\gamma>2$ [6, §4.1] uses only $N_S\ge0$, so **$\gamma_0>2$ holds for $SL(n+1)$**. They also give the Nahm-pole indicial roots $\{-j,j+1\}$ on the spin-$j$ summands [9, §5]. We found nothing beyond $\gamma_0>2$ on $\sigma(M_S)$ for rank $\ge2$.
- **Other works.** Mazzeo–Witten [5, 6] treat $SU(2)$/$SO(3)$ only. Footnote 2 of [6] notes that the model solution for regular $\varrho$ in higher rank is unique, and the introduction of [6] says that general $\varrho$ "will perhaps require significant extra work". Dimakis [10] constructs model knot solutions for the twisted equations for $SU(2)$ only, and his indicial analysis is tied to $2\times2$ matrices. Gaiotto–Witten [3, §3.3] say that for their higher-rank generalization "at present we are only able to find the model solutions numerically". The rStation math series [11, 12] (and math_9, 16, 18, 38) is $SU(2)$ only.

### 1.2 What is new

Write $m_k=\mathfrak r_k+1$, $M=m_1+m_2$, $c=\cos\psi$ and $\sigma=\operatorname{artanh}c\in(0,\infty)$. Here $\sigma\to0$ is the boundary equator, where the Nahm pole sits, and $\sigma\to\infty$ is the pole of $S^2_+$, which lies above the knot. As far as we can tell, everything below beyond §2 is new.

1. **Sectors and the linearized Toda operator (Theorem B).** $M_S$ splits into a Cartan sector and root sectors of heights $\pm1,\pm2$, labelled by a $U(1)$ charge. In the coordinates $u=(\alpha_1(h),\alpha_2(h))$, the $\theta$-independent Cartan sector is
$$-u''+A\,\mathrm{diag}(e^{q_1},e^{q_2})\,u=\gamma\,\operatorname{sech}^2\!\sigma\;u ,$$
which is the linearization of the Toda chain itself, with weight $\operatorname{sech}^2\sigma$. Its zero modes are $\partial q/\partial m_j$. Its scattering matrix $S$ is explicit, with eigenvalues
$$s_\pm=\frac{M^2+m_1m_2\pm\sqrt{m_1^4-m_1^2m_2^2+m_2^4}}{2m_1m_2M}.$$
2. **Positivity and monotonicity (Theorem C).** The Higgs profiles satisfy $\mu_k>\min(m_1,m_2)$; the proof is a Peano-kernel certificate verified symbolically. A maximum principle for the cooperative linearized system gives $\partial q_k/\partial m_j<0$. Hence every Cartan eigenvalue is strictly decreasing in each label, and
$$\gamma_0^{SU(2)}(\max\mathfrak r)<\lambda_0(\mathfrak r_1,\mathfrak r_2)<\gamma_0^{SU(2)}(\min\mathfrak r)\qquad(\mathfrak r_1\ne\mathfrak r_2),$$
where $\lambda_0$ is the lowest eigenvalue of the $\theta$-independent Cartan sector, and $\lambda_0=\gamma_0$ when $\min\mathfrak r\ge1$.
So the closed-form bounds of math_82 [12] apply to $SU(3)$. If $\min\mathfrak r\ge1$, $\gamma_0$ is the simple ground state of the $\theta$-independent Cartan sector, and the root sectors lie above $2+\min(m)^2$.
3. **Diagonal labels and the principal $SU(2)$ (Theorem E).** For $\mathfrak r_1=\mathfrak r_2=\mathfrak r$ the model is the principal embedding of the $SU(2)$ weight-$\mathfrak r$ model, and $M_S=M^{(1)}\oplus M^{(2)}$, where $M^{(1)}$ is exactly the operator of [11, 12]. The spin-$j$ Cartan operator has the Liouville form $-g''+j(j+1)\operatorname{csch}^2x\,g=\gamma n^{-2}\operatorname{sech}^2(x/n)g$. Its zero mode is the Legendre function $Q_j(\coth x)$, whose scattering length is the harmonic number $H_j$. Its spectrum is exact for $n=\mathfrak r+1\le2$: $\{\ell(\ell+1)-(n-1)j(j+1)\}$. Its ground state is $2+3H_j/n+O(n^{-2})$. The same holds for $SU(N)$ with labels $(\mathfrak r,\dots,\mathfrak r)$, with $j=1,\dots,N-1$.
4. **Asymptotics for general labels (Theorem D).** If $\min(m_1,m_2)\ge\delta M$, the two lowest Cartan eigenvalues are $2+3s_\mp+O_\delta(M^{-2})$. The proof combines a two-dimensional Ritz space built from the zero modes with Lehmann's inequality. Hence $\gamma_0=2+3s_-+O(M^{-2})$, and the Type I root-free interval of $\widehat\Delta_{0,3}$ is $(-1-\lambda_+,\lambda_+)$ with $\lambda_+=1+s_-+O(M^{-2})$ (Corollary F).

At $m_1=m_2$ the formula gives $s_-=1/m$ and $s_+=3/(2m)$, which reproduces math_82 and the spin-2 constant $H_2=\tfrac32$. Floating-point computations, labelled [F], indicate that Theorem D also holds for $\mathfrak r_2=0$, where our proof does not apply.

**Scope.** We study one model operator. Nothing here bears directly on Witten's conjectures. The SU(3) analogue of hypothesis (K) of math_16/18 needs more structure than $\gamma_0$ (§8). `verify.py` runs 74 checks (§9).

## 2. The $SU(3)$ model solution (after Mikhaylov and He–Mazzeo)

Coordinates are $(x_1,x_2,x_3,y)$ with $y>0$; the knot is the $x_1$-axis; $z=x_2+ix_3=Re^{i\theta}$; $\rho^2=R^2+y^2$; and $y=\rho\cos\psi$. We use the KW equations of [6, (1.1)], $F-\phi\wedge\phi+\star d_A\phi=0$ and $d_A\star\phi=0$, with orientation $dx_1dx_2dx_3dy$, and antihermitian fields. In $\mathfrak{sl}(3)$, $E_1=e_{12}$, $E_2=e_{23}$, $E_3=e_{13}$, $F_k=E_k^T$, $H_1=\mathrm{diag}(1,-1,0)$, $H_2=\mathrm{diag}(0,1,-1)$, and $A=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ is the Cartan matrix.

Define
$$\tau_1(\sigma)=\tfrac14\Bigl[\frac{e^{2(2m_1+m_2)\sigma/3}}{m_1M}-\frac{e^{2(m_2-m_1)\sigma/3}}{m_1m_2}+\frac{e^{-2(m_1+2m_2)\sigma/3}}{m_2M}\Bigr],\qquad \tau_2=\tau_1|_{m_1\leftrightarrow m_2},$$
$$q_1=\log\tau_2-2\log\tau_1,\qquad q_2=\log\tau_1-2\log\tau_2 .$$
These are the functions of [9, §3.3] (there $e^{-\chi_k}=\tau_k$).

**Theorem A (model solution; due to [7, 9], re-checked).**

(i) *Toda.* $\tau_k\tau_k''-\tau_k'^2=-\tau_{3-k}$ identically in $(m_1,m_2)$. Hence $q''=A\,e^{q}$, i.e. $q_1''=2e^{q_1}-e^{q_2}$ and $q_2''=2e^{q_2}-e^{q_1}$.

(ii) *Positivity.* $\tau_1=e^{-2(m_1+2m_2)\sigma/3}F_1$, with $F_1(\sigma)=\int\!\!\int_{0<t<s<\sigma}e^{2m_2s+2m_1t}\,dt\,ds>0$; similarly for $\tau_2$ with $m_1\leftrightarrow m_2$.

(iii) *Fields.* Put $\psi_k=q_k(\sigma)-2m_k\log R$ and $\Psi=\tfrac12\sum_{i,j}(A^{-1})_{ij}\psi_jH_i$, a real diagonal matrix. Then
$$\phi_1=-i\,\partial_y\Psi,\qquad A=-i(\partial_3\Psi\,dx_2-\partial_2\Psi\,dx_3)=iR\partial_R\Psi\,d\theta,\qquad \phi_2-i\phi_3=\sum_ke^{\psi_k/2}z^{\mathfrak r_k}E_k,\qquad \phi_y=A_1=A_y=0$$
solve the KW equations. For any real diagonal $\Psi$ of this ansatz, KW is equivalent to $\Delta\psi_k=\sum_lA_{kl}|z|^{2\mathfrak r_l}e^{\psi_l}$. Since $\Delta\sigma=0$ and $|\nabla\sigma|^2=R^{-2}$, this is (i).

(iv) *Hemisphere form.* The fields are homogeneous of degree $-1$, with
$$\rho\phi_1=i\,h_\mu,\quad \rho(\phi_2-i\phi_3)=\sum_k\nu_ke^{i\mathfrak r_k\theta}E_k,\quad A_\theta=i\,h_a,\qquad \alpha_k(h_\mu)=\mu_k,\ \alpha_k(h_a)=c\mu_k-m_k,$$
where $\mu_k=-\tfrac12q_k'(\sigma)$ and $\nu_k^2=e^{q_k}\cosh^2\sigma$. With $P=1+c$, $Q=1-c$,
$$D_1=m_2P^M-MP^{m_2}Q^{m_1}+m_1Q^M,\qquad D_2=m_1P^M-MP^{m_1}Q^{m_2}+m_2Q^M,$$
we have
$$\nu_1^2=\frac{4m_1m_2M\,(1+c)^{\mathfrak r_2}(1-c)^{\mathfrak r_1}D_2}{D_1^2},\qquad \mu_1=m_1-\frac{M(1-c)}2+(1-c^2)\Bigl(\frac{D_1'}{D_1}-\frac{D_2'}{2D_2}\Bigr),$$
and $\nu_2$, $\mu_2$ by $1\leftrightarrow2$.

(v) *Asymptotics.* At the Nahm pole ($\sigma\to0$): $\tau_k=\sigma^2/2+O(\sigma^3)$ and $q_k=-2\log\sigma+\log2-\tfrac19(m_1^2+m_1m_2+m_2^2)\sigma^2+O(\sigma^3)$. So $y\phi_1\to i(H_1+H_2)$ and $y(\phi_2-i\phi_3)\to\sqrt2(E_1+E_2)$: this is the principal Nahm pole. Near the knot ($\sigma\to\infty$): $\tau_k=e^{2(2m_k+m_l)\sigma/3}b_k/(4m_kM)$ with
$$b_1=1-\tfrac M{m_2}e^{-2m_1\sigma}+\tfrac{m_1}{m_2}e^{-2M\sigma},\qquad b_2=b_1|_{1\leftrightarrow2},$$
$$q_1=-2m_1\sigma+\log\frac{4m_1^2M}{m_2}+\log b_2-2\log b_1 .$$
Thus $\mu_k\to m_k$, and $\nu_k^2=O((1-c)^{\mathfrak r_k})$ unless $\mathfrak r_k=0$.

(vi) *$SU(2)$ case.* For $m_1=m_2=m$: $D_k=m(P^m-Q^m)^2$, $e^{q_k}=2m^2/\sinh^2(m\sigma)$ and $\mu_k=m\coth(m\sigma)$. The fields are the image of the $SU(2)$ model of [6, (2.9)–(2.11)] under the principal embedding $\iota(X)=\sqrt2(E_1+E_2)$, $\iota(H)=2(H_1+H_2)$. In particular $\nu_k^2=2|\nu^{SU(2)}|^2$.

*Proof.* (i) is a symbolic identity in $(m_1,m_2)$ (`verify.py` §1c). Then $\chi_k=-\log\tau_k$ satisfies $\chi''=e^{q}$ with $q=A\chi$. (ii) Integrate the double integral explicitly (§1d). (iii) The ansatz is the complex gauge transform by $e^{\Psi}$ of $(\partial_{\bar z},\partial_y,\operatorname{ad}\phi_0)$, $\phi_0=\sum z^{\mathfrak r_k}E_k$, as in [7, (3.3)–(3.5)]. We substituted it, with $\Psi$ an arbitrary real diagonal function of $(x_2,x_3,y)$, into all six components of $F-\phi\wedge\phi+\star d_A\phi$ and into $d_A\star\phi$. Five components vanish identically. The sixth, the moment map, vanishes exactly on the PDE (§1a, for $(\mathfrak r_1,\mathfrak r_2)=(1,0),(2,1)$; with the opposite orientation the reduction fails, which is a negative control). The PDE becomes (i) by §1b. As an independent check, we substituted the explicit fields for $(1,0)$, $(2,1)$ and $(3,3)$ into all KW components at random points; the residual is below $10^{-20}$ at 30 digits (§1g). (iv) uses $\rho\,\partial_y\sigma=1$ and $R\partial_R\sigma=-\tanh\sigma$; the closed forms are §1f. (v), (vi) are §1e and §4. $\square$

## 3. The hemisphere operator and its sectors

As in [6, (4.12)–(4.15)],
$$M_S=-\frac1{\sin\psi}\partial_\psi\sin\psi\,\partial_\psi-\frac{D_\theta^2}{\sin^2\psi}+N_S,\qquad N_S=-\rho^2\sum_{j=1}^3\operatorname{ad}(\phi_j)^2,\qquad D_\theta=\partial_\theta+\operatorname{ad}A_\theta,$$
on $\mathfrak{sl}(3,\mathbb C)$-valued functions on $S^2_+$. We take the self-adjoint realization in $L^2(S^2_+)$ (trace form) of [6, Prop. 4.1] and [9, §5]: we use the Friedrichs extension from smooth functions compactly supported away from the equator. Its *eigenfunctions* vanish at the equator ($\sigma\to0$) at the Nahm-pole rate, $s^{j+1}$ on the spin-$j$ part; general functions in the operator or form domain need not have this rate, and we never apply it to trial functions. Membership of a trial function $g$ in the domain is always justified by $g$ lying in the form domain together with $Lg\in L^2$. At the pole the boundary condition is Friedrichs/regularity. Then $\sigma(M_S)$ is discrete, and $\gamma_0=\min\sigma(M_S)$.

**Theorem B (sectors).** Write $\Psi=h+\sum_\beta f_\beta E_\beta+\sum_\beta f_{-\beta}F_\beta$.

(i) $N_S$ preserves the height $\mathrm{ht}(\beta)\in\{0,\pm1,\pm2\}$. On the Cartan, in coordinates $h=c_1H_1+c_2H_2$, it acts by $\mathrm{diag}(\nu_1^2,\nu_2^2)A$. On $\mathrm{span}(E_1,E_2)$, in the charge-adapted basis $e^{i(\mathsf M+\mathfrak r_k)\theta}E_k$ ($k=1,2$), which absorbs the root phases, it is
$$N_1=\begin{pmatrix}\mu_1^2+\nu_1^2+\tfrac12\nu_2^2&-\nu_1\nu_2\\-\nu_1\nu_2&\mu_2^2+\nu_2^2+\tfrac12\nu_1^2\end{pmatrix},$$
and on $E_3$ it is $N_2=(\mu_1+\mu_2)^2+\tfrac12(\nu_1^2+\nu_2^2)$. Heights $-1,-2$ give the same matrices. In the fixed basis $(E_1,E_2)$ at a given $\theta$ the off-diagonal entries of $N_1$ carry the phases $e^{\pm i(\mathfrak r_1-\mathfrak r_2)\theta}$; the phase-free matrix above is the one in the charge-adapted basis, which is the basis used in (ii) and in all sector computations.

(ii) The operator $-i\partial_\theta-\operatorname{ad}(\omega)$, with $\alpha_k(\omega)=\mathfrak r_k$, commutes with $M_S$. On a root vector $E_\beta$, $\beta=n_1\alpha_1+n_2\alpha_2$, with Fourier mode $e^{i\ell\theta}$ and charge $\mathsf M=\ell-\beta(\omega)\in\mathbb Z$, the centrifugal term is $(\mathsf M+\sum_kn_k(c\mu_k-1))^2/\sin^2\psi$. On the Cartan it is $\ell^2/\sin^2\psi$. So $M_S$ is the orthogonal sum of: Cartan sectors $L+\ell^2/\sin^2\psi$ ($\ell\in\mathbb Z$); $2\times2$ height-$1$ sectors $-\Delta_\psi+\mathrm{diag}((\mathsf M+c\mu_k-1)^2)/\sin^2\psi+N_1$; scalar height-$2$ sectors; and their height $-1,-2$ mirrors, which are antiunitarily equivalent to them via $\Psi\mapsto-\Psi^\dagger$ (this map commutes with $M_S$), so they have the same spectrum.

(iii) *Linearized Toda form.* In $u=(\alpha_1(h),\alpha_2(h))=Ac$, with $c=\tanh\sigma$ and $dc=\operatorname{sech}^2\sigma\,d\sigma$, the $\theta$-independent Cartan sector is
$$L u=\cosh^2\!\sigma\,\bigl(-u''+A\,E\,u\bigr),\qquad E=\mathrm{diag}(e^{q_1},e^{q_2}),$$
on $\mathcal H=L^2((0,\infty),\operatorname{sech}^2\sigma\,d\sigma;\mathbb R^2)$ with $\langle u,w\rangle=\int u^TA^{-1}w\operatorname{sech}^2\sigma\,d\sigma$. Its quadratic form is $\mathcal Q[u]=\int_0^\infty(u'^TA^{-1}u'+\sum_ke^{q_k}u_k^2)\,d\sigma$. The operator $J=-\partial_\sigma^2+AE$ is the linearization of $q''=Ae^q$.

(iv) *Zero modes.* $Z_j=\partial q/\partial m_j$ ($j=1,2$) and $q'$ satisfy $JZ=0$. As $\sigma\to0$, $Z_j=O(\sigma^2)$, and the spin-2 combination $(Z_j)_1-(Z_j)_2=O(\sigma^3)$. As $\sigma\to\infty$, $Z_j=-2\sigma e_j+Ke_j+O(\sigma e^{-2\min(m)\sigma})$, with
$$K=\begin{pmatrix}\frac2{m_1}+\frac1M&\frac1M-\frac1{m_2}\\[2pt]\frac1M-\frac1{m_1}&\frac2{m_2}+\frac1M\end{pmatrix},\qquad \operatorname{tr}K=2\Bigl(\frac1{m_1}+\frac1{m_2}+\frac1M\Bigr),\quad\det K=\frac6{m_1m_2}.$$
$A^{-1}K$ is symmetric. Hence $S:=K/2$ is self-adjoint for $\langle\cdot,\cdot\rangle$, with eigenvalues $s_\pm$ as in §1.2. The combination $Z_v:=-\tfrac12\sum_jv_jZ_j$ satisfies $Z_v=\sigma v-Sv+D_v$, where $D_v\to0$ exponentially. We call $S$ the *scattering matrix*: the knot acts on the outer Legendre problem like a matrix hard wall displaced by $S$.

*Proof.* (i) is a finite matrix computation with $\rho\phi_1=ih_\mu$ and $a=\sum\nu_kE_k$. Writing $\phi_2=(a-a^\dagger)/2$ and $\phi_3=i(a+a^\dagger)/2$, one gets $-\operatorname{ad}\phi_2^2-\operatorname{ad}\phi_3^2=\tfrac12\{\operatorname{ad}a,\operatorname{ad}a^\dagger\}$. The phases $e^{i\mathfrak r_k\theta}$ do not change the moduli (`verify.py` §2, symbolic in $\mu_k,\nu_k$). (ii) $\operatorname{ad}a$ raises the root by $\alpha_k$ and carries the phase $e^{i\mathfrak r_k\theta}$. $D_\theta$ acts on $e^{i\ell\theta}E_\beta$ by $i(\ell+\beta(h_a))$, and $\beta(h_a)=\sum n_k(c\mu_k-m_k)$. (iii) $-((1-c^2)g_c)_c=-\cosh^2\sigma\,g_{\sigma\sigma}$, $\nu_k^2\operatorname{sech}^2\sigma=e^{q_k}$, and $A\,\mathrm{diag}(\nu^2)$ is the Cartan block in $u$-coordinates. (iv) Differentiate $q''=Ae^q$ in $m_j$ and in $\sigma$. The expansions follow from Theorem A(v): the Nahm-pole constant $\log2$ does not depend on $m$, and the $\sigma^2$ coefficient is the same for both components. $K=\partial_m(\log\frac{4m_1^2M}{m_2},\log\frac{4m_2^2M}{m_1})$. The rest is algebra (§2). $\square$

## 4. Positivity, monotonicity and the ground state

**Lemma 4.1 (Peano kernel).** Let $\ell(f)=\sum_ic_if(\lambda_i)$ vanish on polynomials of degree $\le2$. Then $\ell(f)=\int f'''(x)K(x)\,dx$, where $K(x)=\tfrac12\sum_ic_i(\lambda_i-x)_+^2$. In particular, if $K\ge0$ and $K\not\equiv0$, then $\sum_ic_ie^{2\sigma\lambda_i}=8\sigma^3\int e^{2\sigma x}K(x)\,dx>0$ for $\sigma>0$. (This is Taylor's formula with integral remainder; see e.g. [16, Ch. III].)

**Theorem C.**

(i) For $k=1,2$ and all $c\in(0,1)$: $\mu_k(c)>\min(m_1,m_2)$. In particular $\mu_k>0$.

(ii) For all $\sigma>0$ and $j,k$: $\partial q_k/\partial m_j<0$. So $e^{q_k}$ is strictly decreasing in each $m_j$.

(iii) Every eigenvalue $\lambda_i(\mathfrak r_1,\mathfrak r_2)$ of $L$ is strictly decreasing in $\mathfrak r_1$ and in $\mathfrak r_2$. It is symmetric under $\mathfrak r_1\leftrightarrow\mathfrak r_2$.

(iv) $\lambda_0(\mathfrak r,\mathfrak r)=\gamma_0^{SU(2)}(\mathfrak r)$, the ground state of [12]. For $\mathfrak r_1<\mathfrak r_2$,
$$\gamma_0^{SU(2)}(\mathfrak r_2)<\lambda_0(\mathfrak r_1,\mathfrak r_2)<\gamma_0^{SU(2)}(\mathfrak r_1).$$
Consequently $L_{\mathfrak r_2+1}\le\lambda_0\le2+3(\mathfrak r_1+1)^2/\mathfrak r_1^3$, with $L_n$ the closed-form lower bound of [12, Thm C(ii)] (valid for $\mathfrak r_2\ge2$) and the upper bound valid for $\mathfrak r_1\ge1$ [12, Thm C(i)].

(v) $\lambda_0$ is a simple eigenvalue of $L$. In the coordinates $v=A^{-1/2}u$ its eigenfunction can be taken with both components positive.

(vi) Every height-$\pm1$ sector is $\ge2+\min(m)^2$, every height-$\pm2$ sector is $\ge2+4\min(m)^2$, and every Cartan sector with $\ell\ne0$ is $>\lambda_0$. Hence, **if $\min(\mathfrak r_1,\mathfrak r_2)\ge1$**, $\gamma_0(M_S)=\lambda_0(L)$. It is a simple eigenvalue of $M_S$, with $\theta$-independent, Cartan-valued eigenfunction.

*Proof.* (i) Write $a=e^{2m_1\sigma}$ and $b=e^{2m_2\sigma}$. From Theorem A(ii), $4m_1m_2M\,F_1=m_2ab-Mb+m_1$, $4m_1m_2M\,F_2=m_1ab-Ma+m_2$, $F_1'=b(a-1)/(2m_1)$ and $F_2'=a(b-1)/(2m_2)$. Moreover $q_1=2m_2\sigma+\log F_2-2\log F_1$. Hence
$$\mu_1-\kappa=\frac{2F_1'F_2-F_1F_2'-2(m_2+\kappa)F_1F_2}{2F_1F_2}.$$
Multiplied by $16m_1^2m_2^2M^2$, the numerator is an exponential sum $\sum c_{ij}(\kappa)e^{2\sigma(im_1+jm_2)}$ over $(i,j)\in\{0,1,2\}^2\setminus\{(2,0),(0,2)\}$. For $\kappa=0$ its coefficients are
$$c_{22}=2m_1^2m_2,\ c_{21}=-2m_2M^2,\ c_{12}=2m_1^2M,\ c_{11}=-2(m_1-m_2)(m_1+2m_2)(2m_1+m_2),\ c_{10}=2m_1M^2,\ c_{01}=-2m_2^2M,\ c_{00}=-2m_1m_2^2 .$$
For $\kappa>0$ one adds the expansion of $-32\kappa m_1^2m_2^2M^2F_1F_2$. The sum vanishes to third order at $\sigma=0$, so Lemma 4.1 applies.

By homogeneity put $m_2=1$ and $m_1=t$. The breakpoints $\lambda_{ij}=it+j$ have a fixed order on $t\in(0,1)$ and on $t\in(1,\infty)$. On each interval between consecutive breakpoints, $K$ is a quadratic polynomial. We write its three Bernstein coefficients as rational functions of $u>0$, with $t=1/(1+u)$ or $t=1+u$. `verify.py` §3 checks exactly that each numerator and each denominator has coefficients of one sign, and that the value at $u=7/10$ is $\ge0$. Hence every Bernstein coefficient is $\ge0$ for all $u>0$, so $K\ge0$. This holds for $\kappa=0$ and for $\kappa=\min(m_1,m_2)$ ($\kappa=m_1$ on $t<1$, $\kappa=m_2$ on $t>1$); $t=1$ follows by continuity. Since $S\not\equiv0$, Lemma 4.1 gives $\mu_1>\kappa$. The case $\mu_2$ follows from $q_2(\sigma;m_1,m_2)=q_1(\sigma;m_2,m_1)$. The bound is sharp: $\mu_k\to m_k$ at the pole.

(ii) Fix $j$ and put $w=-Z_j$ and $h=-q'=2\mu$. By (i), $h>0$, and $Jh=Jw=0$. The matrix $AE$ has off-diagonal entries $-e^{q_l}<0$, so the system is cooperative. As $\sigma\to0$, $w=O(\sigma^2)$ and $h\sim2\sigma^{-1}(1,1)$. As $\sigma\to\infty$, $w_j\sim2\sigma$, $w_k\to-K_{kj}=\frac1{m_j}-\frac1M>0$ for $k\ne j$, and $h\to2m$. Suppose $\tau^*=\sup_{\sigma,k}(-w_k/h_k)>0$. Then it is attained at an interior $(\sigma^*,k^*)$, and $v=w+\tau^*h\ge0$ has $v_{k^*}(\sigma^*)=v_{k^*}'(\sigma^*)=0$ and $v_{k^*}''(\sigma^*)\ge0$. But $(Jv)_{k^*}=0$ gives $v_{k^*}''(\sigma^*)=-e^{q_l}v_l(\sigma^*)\le0$, so $v_l(\sigma^*)=0$, and hence $v_l'(\sigma^*)=0$ too. ODE uniqueness gives $v\equiv0$, i.e. $w=-\tau^*h$, which contradicts $w_j\to+\infty$. So $w\ge0$. The same argument with $\tau^*=0$ excludes interior zeros, so $w>0$.

(iii) By (ii), $e^{q_k(\sigma;m)}$ decreases strictly in each $m_j$, as a real parameter. The forms $\mathcal Q_m$ have a common domain, because $e^{q_k}=2\sigma^{-2}+O(1)$ uniformly. Min–max with strict form inequality gives strict decrease. The symmetry is the diagram automorphism.

(iv) For $m_1=m_2$ the Cartan sector splits (Theorem E). The spin-1 part is $L^{(1)}$, the operator of [12]. The spin-2 part $L^{(2)}$ has the larger potential $6|\nu|^2\ge2|\nu|^2$, so $\lambda_0(L)=\lambda_0(L^{(1)})=\gamma_0^{SU(2)}(\mathfrak r)$. Then apply (iii) along $(\mathfrak r_1,\mathfrak r_1)\to(\mathfrak r_1,\mathfrak r_2)\to(\mathfrak r_2,\mathfrak r_2)$.

(v) In $v=A^{-1/2}u$, the form is $\int(|v'|^2+v^TWv)$ with weight $\operatorname{sech}^2\sigma$, where $W=A^{1/2}EA^{1/2}$. Since $A^{1/2}=\tfrac12\begin{pmatrix}1+\sqrt3&1-\sqrt3\\1-\sqrt3&1+\sqrt3\end{pmatrix}$, $W_{12}=\tfrac12(1+\sqrt3)\cdot\tfrac12(1-\sqrt3)(e^{q_1}+e^{q_2})<0$. Hence $\mathcal Q[|v|]\le\mathcal Q[v]$, and a ground state can be taken $\ge0$. The cooperative argument of (ii) makes it $>0$. If $u$ is any real ground state, $|u|$ is one too. If $u$ had components of opposite signs, then $|u|-u$ would be a ground state with one component $\equiv0$, and the coupled equation would force the other to vanish. So every ground state has a fixed sign, and two orthogonal ones cannot exist.

(vi) On each root sector, the form is at least the Dirichlet Laplacian of the hemisphere (lowest eigenvalue $2$, eigenfunction $\cos\psi$) plus $\inf\lambda_{\min}(N)$. We have $N_1\ge\mathrm{diag}(\mu_1^2,\mu_2^2)$, because $\tfrac12\{\operatorname{ad}a,\operatorname{ad}a^\dagger\}\ge0$, and $N_2\ge(\mu_1+\mu_2)^2$. Then apply (i). For $\min\mathfrak r\ge1$, (iv) and [11, 12] give $\lambda_0\le\gamma_0^{SU(2)}(1)=4<6\le2+\min(m)^2$. $\square$

**Remark 4.2 ($\min\mathfrak r=0$).** For $\mathfrak r_2=0$, (vi) gives only "root sectors $\ge3$". With (iii): once $\lambda_0(\mathfrak r_*,0)<3$, the ground state lies in the Cartan sector for all $\mathfrak r_1\ge\mathfrak r_*$. A Ritz quotient gives $\lambda_0(5,0)\le2.851<3$ [F, quadrature not interval-certified]. Finite elements put the ground state in the Cartan sector for $(\mathfrak r,0)$, $\mathfrak r\le5$ (Table 2) [F]; the smallest margin is to the height-one sector, e.g. $4.587<7.206$ at $(1,0)$ and $2.846<6.609$ at $(5,0)$. The sector computations are validated against the exact values at labels $(1,1)$, where the lowest root-sector eigenvalue is $8$ [11] and the lowest $\ell\ne0$ Cartan eigenvalue is $10$ (Theorem E(i)); finite elements reproduce $8.00000$ and $10.00001$. We do not claim this case as a theorem.

## 5. Diagonal labels, the principal $SU(2)$, and spin-$j$ operators

**Theorem E.** Let $\mathfrak r_1=\mathfrak r_2=\mathfrak r$ and $n=\mathfrak r+1$. Let $\mu=n\coth(n\sigma)$ and $|\nu|^2=n^2\cosh^2\!\sigma/\sinh^2(n\sigma)$ be the $SU(2)$ profiles of [12].

(i) Under the principal $\mathfrak{sl}_2$ (Theorem A(vi)), $\mathfrak{sl}_3=V_1\oplus V_2$, with Casimir eigenvalues $4$ (multiplicity $3$) and $12$ (multiplicity $5$). Correspondingly $M_S=M^{(1)}\oplus M^{(2)}$. Here $M^{(j)}$ acts on $V_j$-valued functions. On the weight vector $e_q$ ($|q|\le j$) its potential is
$$N^{(j)}e_q=\bigl(q^2\mu^2+(j(j+1)-q^2)|\nu|^2\bigr)e_q,$$
and its centrifugal charge is $q$. $M^{(1)}$ is the $SU(2)$ operator of [11, 12].

(ii) The $q=0$, $\theta$-independent part of $M^{(j)}$ is $L^{(j)}g=-((1-c^2)g')'+j(j+1)|\nu|^2g$. With $c=\tanh(x/n)$,
$$L^{(j)}=\frac{n^2}{1-c^2}\Bigl(-\frac{d^2}{dx^2}+\frac{j(j+1)}{\sinh^2x}\Bigr),$$
and $L^{(j)}g=\gamma g$ if and only if $-g''+j(j+1)\operatorname{csch}^2x\,g=\gamma n^{-2}\operatorname{sech}^2(x/n)\,g$.

(iii) $f_j(x)=Q_j(\coth x)=x\,P_j(\coth x)-W_{j-1}(\coth x)$ solves $-f''+j(j+1)\operatorname{csch}^2x\,f=0$, with $W_{j-1}=\sum_{k=1}^j\frac1kP_{k-1}P_{j-k}$. It has $f_j=O(x^{j+1})$ exactly at $0$ (the Nahm-pole rate) and $f_j(x)=x-H_j+O(xe^{-2x})$ at $\infty$, where $H_j=1+\frac12+\dots+\frac1j$.

(iv) *Exact spectra.* For $n=1$: $\sigma(L^{(j)})=\{\ell(\ell+1):\ell=j+1+2k,\ k\ge0\}$, with eigenfunctions $c^{j+1}p_k(c^2)$. For $n=2$: $\sigma(L^{(j)})=\{\ell(\ell+1)-j(j+1)\}$. So for the $SU(3)$ knot $(1,1)$ the $\theta$-independent Cartan spectrum is $\{4,18,40,\dots\}\cup\{6,24,50,\dots\}$.

(v) $\lambda_1(L^{(j)})\ge6$, $L^{(j+1)}>L^{(j)}$, and, for each fixed $j$,
$$\lambda_0(L^{(j)})=2+\frac{3H_j}{n}+O(n^{-2})\qquad(n\to\infty).$$

(vi) *$SU(N)$.* For $G=SU(N)$ and labels $(\mathfrak r,\dots,\mathfrak r)$, the principal embedding of the $SU(2)$ weight-$\mathfrak r$ model solves KW with the principal Nahm pole. Indeed, $q_k=\log B_k+2\log(m/\sinh m\sigma)$ with $B=2A^{-1}\mathbf 1$ solves the $A_{N-1}$ Toda chain with Mikhaylov's boundary behaviour [7, (3.15), (3.18)]. Its $M_S$ is $\bigoplus_{j=1}^{N-1}M^{(j)}$, and for $\mathfrak r\ge1$, $\gamma_0=\gamma_0^{SU(2)}(\mathfrak r)$.

*Proof.* (i) $\operatorname{ad}\circ\iota$ is a representation, and $\phi_1,\phi_2-i\phi_3,A_\theta$ are $\iota$ of the $SU(2)$ fields. Then use $\{X,Y\}=2j(j+1)-H^2/2$ on $V_j$ (§4, $j\le3$).

(ii) As in [12, Thm A]; checked symbolically with $j$ as a symbol.

(iii) $\tfrac12\log\frac{\coth x+1}{\coth x-1}=x$, together with the classical form of $Q_j$ (checked for $j\le5$; the limits and the order at $0$ are exact computations).

(iv) For $n=1$, $|\nu|^2=c^{-2}$. The operator $-((1-c^2)g')'+j(j+1)c^{-2}g$ maps $c^{j+1}\mathcal P_k(c^2)$ to itself, triangularly with diagonal entries $\ell(\ell+1)$ (checked for $j\le3$, $k\le2$; the general case is the hypergeometric/Jacobi equation). These functions are complete. For $n=2$, $4\operatorname{csch}^2(2\sigma)=\operatorname{csch}^2\sigma-\operatorname{sech}^2\sigma$, i.e. $L^{(j)}_{n=2}=L^{(j)}_{n=1}-j(j+1)$.

(v) Compare with the Neumann Legendre form, whose spectrum on $(0,1)$ is $\{0,6,20,\dots\}$, and use the pointwise order of the potentials. For the asymptotics apply the scalar case of Lemma 6.3, i.e. Temple's inequality with $\beta=6$, to $g=\tanh\sigma-\sigma+f_j(n\sigma)/n$. For $j\ge3$ this $g$ satisfies $g=-\sigma^3/3+O(\sigma^4)$ at $\sigma=0$, not $O(\sigma^{j+1})$; it lies in the domain of the Friedrichs realization because it is in the form domain ($g'$ and $\operatorname{csch}(n\sigma)\,g$ are square integrable near $0$, since $g=O(\sigma^3)$) and $L^{(j)}g=2g+R\in L^2$ by the formula below. Then $L^{(j)}g=2g+R$ with $R=\tfrac2n(H_j-e_j)+j(j+1)|\nu|^2(c-\operatorname{artanh}c)$, where $e_j=H_j-x+f_j$ is bounded and $O(xe^{-2x})$. The estimates are the scalar case of those in the proof of Theorem D: here the profile $e_j$ is bounded and exponentially decaying, $|g|\le\sigma^3/3+C\sigma$, and $\int x^4\operatorname{csch}^2x\,dx<\infty$. They give $\|g\|^2=\frac13-\frac{H_j}n+O(n^{-2})$, $\langle g,R\rangle=\frac{H_j}n+O(n^{-2})$ and $\|R\|^2=O(n^{-2})$. Hence Ritz and Temple agree to $O(n^{-2})$.

(vi) The Toda check is $\sum_lA_{kl}B_l=2$. Then argue as in (i) and Theorem C(vi), using $q^2\mu^2\ge n^2$ for $q\ne0$. $\square$

## 6. General labels: asymptotics of the two lowest Cartan eigenvalues

**Theorem D.** Fix $\delta\in(0,\tfrac12]$. There is $C_\delta$ such that for all $m_1,m_2\ge1$ with $\min(m_1,m_2)\ge\delta M$,
$$|\lambda_0(L)-2-3s_-|\le C_\delta M^{-2},\qquad|\lambda_1(L)-2-3s_+|\le C_\delta M^{-2}.$$
Consequently, for such labels, $\gamma_0(M_S)=2+3s_-+O_\delta(M^{-2})$ (Theorem C(vi)). Note that $s_\pm\asymp M^{-1}$ and $s_+-s_-=\sqrt{m_1^4-m_1^2m_2^2+m_2^4}/(m_1m_2M)\asymp M^{-1}$.

**Lemma 6.1 (scaling).** Let $t=m_1/M$ and $x=M\sigma$. Then $q_k(\sigma)=2\log M+\hat q_k(x;t)$, where $\hat q$ is $q$ for $(m_1,m_2)=(t,1-t)$. Also $Z_v(\sigma)=M^{-1}\hat Z_v(x;t)$, $S=M^{-1}\hat S(t)$ and $D_v(\sigma)=M^{-1}\hat D_v(x;t)$.

*Proof.* By Theorem A(v), $q$ depends on $m$ only through $m_1\sigma$, $m_2\sigma$, degree-0 ratios, and $\log(4m_k^2M/m_l)=2\log M+\log(4t_k^2/t_l)$. Differentiating in $m_j$ produces $\sigma\times(\dots)$ or $M^{-1}\times(\dots)$. $\square$

**Lemma 6.2 (uniform profile bounds).** For $t\in[\delta,1-\delta]$, $x>0$ and $|v|=1$:
$$e^{\hat q_k(x)}\le C_\delta\,\frac{e^{-2\delta x}}{\min(x,1)^2},\qquad|\hat Z_v(x)|\le C_\delta x,\qquad|\hat D_v(x)|\le C_\delta(1+x)e^{-2\delta x}.$$

*Proof.* We have $\hat b_1=1-\frac1{1-t}e^{-2tx}+\frac t{1-t}e^{-2x}$, and $\hat b_2$ likewise. Each $\hat b_k$ is positive on $(0,\infty)$ by Theorem A(ii), vanishes to exactly second order at $x=0$ with a coefficient continuous and positive in $t$, and tends to $1$. By compactness, $c_\delta\min(x,1)^2\le\hat b_k\le C_\delta\min(x,1)^2$. The first bound follows from $e^{\hat q_1}=\frac{4t^2}{1-t}e^{-2tx}\hat b_2/\hat b_1^2$.

$\hat D_v$ is a combination, with coefficients continuous in $t$, of the terms $\partial\hat b_k/\hat b_k$, where $\partial$ is the derivative in $m_j$ written in scaled variables. Each $\partial\hat b_k$ is a combination of $e^{-2tx},xe^{-2tx},e^{-2x},xe^{-2x}$ (up to $t\leftrightarrow1-t$) and vanishes to second order at $x=0$, because $\hat b_k(0)=\hat b_k'(0)=0$ for every $t$. This gives the third bound. Finally, $\hat Z_v=O(x^2)$ at $0$ (Theorem B(iv)) and $\hat Z_v=xv-\hat Sv+\hat D_v$, which gives the second bound. $\square$

**Lemma 6.3 (two-mode Ritz–Lehmann).** Let $T$ be self-adjoint with compact resolvent and eigenvalues $\lambda_0\le\lambda_1\le\lambda_2\le\dots$. Let $\rho<\lambda_2$ with $\rho\notin\sigma(T)$, and let $g_1,g_2\in D(T)$ be independent. Put $A_0=(\langle g_i,g_j\rangle)$, $A_1=(\langle g_i,Tg_j\rangle)$ and $A_2=(\langle Tg_i,Tg_j\rangle)$.

(a) $\lambda_0\le\rho_0$ and $\lambda_1\le\rho_1$, where $\rho_0\le\rho_1$ are the eigenvalues of $A_0^{-1}A_1$.

(b) Let $\mu_1\le\mu_2$ be the eigenvalues of $(A_1-\rho A_0)x=\mu(A_2-2\rho A_1+\rho^2A_0)x$. If $\mu_2<0$, then $\lambda_1\ge\rho+1/\mu_1$ and $\lambda_0\ge\rho+1/\mu_2$.

*Proof.* (a) is min–max. (b) $A_2-2\rho A_1+\rho^2A_0$ is the Gram matrix of $(T-\rho)g_i$, and $\mu_i$ are the Ritz values of $B=(T-\rho)^{-1}$ on $\mathrm{span}\{(T-\rho)g_i\}$. If $\kappa\le2$ eigenvalues of $T$ lie below $\rho$, then $B$ has exactly $\kappa$ negative eigenvalues $1/(\lambda_{\kappa-1}-\rho)\le\dots\le1/(\lambda_0-\rho)$, and the rest of its spectrum is $\ge0$. Min–max for $B$ gives $\mu_i\ge$ the $i$-th lowest point of $\sigma(B)$. Since $\mu_2<0$, this forces $\kappa=2$, and $1/(\lambda_{2-i}-\rho)\le\mu_i<0$ gives the claim. This is Lehmann's method [13]; for one function it is Temple's inequality [14]. $\square$

*Proof of Theorem D.* By Lemma 6.1, $m_{\min}\ge\delta M\ge2$ once $M\ge2/\delta$. Smaller $M$ are finitely many cases, absorbed into $C_\delta$.

For $v\in\mathbb R^2$ put
$$g_v=(\tanh\sigma-\sigma)v+Z_v=cv-Sv+D_v .$$
It lies in $D(L)$: near $\sigma=0$ it is $O(\sigma^2)$, with spin-2 part $O(\sigma^3)$; near the pole it is $C^1$ in $c$, since $D_v=O((1-c)^{m_{\min}}|\log(1-c)|)$. Because $JZ_v=0$ and $-(\tanh\sigma)''=2\tanh\sigma\operatorname{sech}^2\sigma$,
$$Lg_v=2g_v+R_v,\qquad R_v=2(Sv-D_v)+\cosh^2\!\sigma\,AE\,(\tanh\sigma-\sigma)v .$$
Take $g_i=g_{e_i}$. Then $A_0=G$, $A_1=2G+B$ and $A_2=4G+4B+C$, with $G=(\langle g_i,g_j\rangle)$, $B=(\langle g_i,R_j\rangle)$ (symmetric) and $C=(\langle R_i,R_j\rangle)$. We show
$$G=\tfrac13A^{-1}+O(M^{-1}),\qquad B=A^{-1}S+O(M^{-2}),\qquad C=O(M^{-2}).\tag{6.1}$$
Write $\varepsilon_v=-Sv+D_v$. Then $|Sv|\le C/M$, and $\int|D_v|^2dc\le\int|D_v|^2d\sigma=M^{-3}\int|\hat D_v|^2dx$. So $\|\varepsilon_v\|=O(M^{-1})$, and $\int c^2dc=\frac13$ gives $G$.

For $B$, $\langle ce_i,2Se_j\rangle=e_i^TA^{-1}Se_j$, and $\langle\varepsilon_i,2Se_j\rangle=O(M^{-2})$. Next, $|\langle g_i,D_j\rangle|\le\int(\sigma+C/M+|D_i|)|D_j|\,d\sigma=O(M^{-3})$ by Lemma 6.2. The potential term is $\int(g_i)_je^{q_j}(\tanh\sigma-\sigma)\,d\sigma$. There $|\tanh\sigma-\sigma|\le\sigma^3/3$, $|g_i|\le\sigma^3/3+|Z_{e_i}|\le\sigma^3/3+C\sigma$ and $e^{q_j}=M^2e^{\hat q_j(M\sigma)}$, so the term is bounded by $M^{-3}\int(x^3/M^2+Cx)x^3e^{\hat q_j}dx=O(M^{-3})$.

For $C$, $\|R_v\|\le2|Sv|\|\mathbf 1\|+2\|D_v\|+\|\cosh^2\sigma\,AE(\tanh\sigma-\sigma)v\|$. The last norm squared is $\le C\int e^{2q}\sigma^6\cosh^2\sigma\,d\sigma=CM^{-3}\int e^{2\hat q(x)}x^6\cosh^2(x/M)\,dx=O(M^{-3})$ for $M\ge2/\delta$, by Lemma 6.2. This proves (6.1).

Let $\beta=G^{-1/2}BG^{-1/2}$ and $\gamma=G^{-1/2}CG^{-1/2}$. Then $\beta=O(M^{-1})$, $\gamma=O(M^{-2})$, and $\beta$ is similar to $G^{-1}B=3S+O(M^{-2})$. Since $S$ is $A^{-1}$-self-adjoint, its eigenvector matrix has condition number $\le\sqrt3$, and Bauer–Fike gives $\operatorname{eig}\beta=3s_\mp+O(M^{-2})$. Lemma 6.3(a) gives $\lambda_{0,1}\le2+3s_\mp+O(M^{-2})$.

For (b) take $\rho=6$. Then $\lambda_2>6$: compare with the vector Neumann form $\int u'^TA^{-1}u'$, whose spectrum is $\{0,0,6,6,\dots\}$; the inequality is strict on the 3-dimensional span of the first eigenfunctions. In $G$-orthonormal coordinates the pencil is $(\beta-4)y=\mu(16-8\beta+\gamma)y$. Taylor expansion gives
$$(16-8\beta+\gamma)^{-1/2}(\beta-4)(16-8\beta+\gamma)^{-1/2}=-\tfrac14-\tfrac1{16}\beta+O(M^{-2}).$$
So $\mu_i<0$ for large $M$, and $6+1/\mu_i=2+\beta_{(i)}+O(M^{-2})$. Thus $\lambda_{0,1}\ge2+3s_\mp-O(M^{-2})$. All constants depend only on the integrals in Lemma 6.2, so they are uniform for $t\in[\delta,1-\delta]$. $\square$

**Remark 6.4.** (a) For $m_1=m_2$, Theorem D reproduces $2+3/n$ [12] and $2+9/(2n)$ (Theorem E(v)).
(b) The trial space is "outer Legendre function $c\,v$ plus inner zero mode". This is the matrix version of the hard-wall picture of [12, §6]: the knot displaces the Dirichlet wall at $c=0$ by the matrix $S$.
(c) For $\mathfrak r_2=0$ the proof fails at Lemma 6.2. With $m_2=1$, $e^{q_2}$ has width $O(1)$ and $s_+=O(1)$, so the second trial function is poor. Moreover $\lambda_1>6$ numerically, so Lemma 6.3(b) cannot certify $\lambda_0$. Numerically, $m_1^2(\lambda_0-2-3s_-)$ stays bounded ($\approx6.3$ at $m_1=129$) and $\lambda_1\downarrow6$ (Table 3) [F]. In this regime $3s_-=\frac92m_1^{-1}+O(m_1^{-2})$.

**Corollary F (Type I indicial roots).** Let $\lambda_\pm=-\tfrac12\pm\sqrt{\gamma_0+\tfrac14}$. By [6, (4.14), (4.16)], whose derivation uses only the degree $-1$ homogeneity and therefore holds for $SU(3)$ (cf. [9, Prop. 5.6]), $\widehat\Delta_{0,3}(\rho^\lambda\Psi)=0$ has no nonzero solution in the domain of $M_S$ for real $\lambda\in(\lambda_-,\lambda_+)$, and it has one at $\lambda=\lambda_\pm$. Here $\lambda_-=-1-\lambda_+$. For $\min\mathfrak r\ge1$ and $\mathfrak r_1\ne\mathfrak r_2$, $\lambda_+$ lies strictly between the $SU(2)$ values for $\max\mathfrak r$ and $\min\mathfrak r$ (the $SU(2)$ values are those of [12, Cor. E]); for $\mathfrak r_1=\mathfrak r_2$ it equals the common $SU(2)$ value (Theorem E). For $\min m\ge\delta M$,
$$\lambda_+=1+s_-+O(M^{-2}).$$
The next root is $-\tfrac12+\sqrt{\lambda_1+\tfrac14}=1+s_++O(M^{-2})$. In particular $[-2,1]$ lies strictly inside the gap, and the gap is asymptotically sharp, as for $SU(2)$.

## 7. Numerical tables

All entries are [F]. The ground states use P1 finite elements on a graded mesh in $\sigma$, where conforming FEM gives upper bounds up to quadrature error. The Ritz and Lehmann values use 30-digit quadrature that is not interval-certified.

**Table 1.** $\theta$-independent Cartan sector. Columns: $\lambda_0$, $\lambda_1$ (FEM); the asymptotic values $2+3s_\mp$; and the sandwich values $\gamma_0^{SU(2)}(\mathfrak r_1)\le\lambda_0\le\gamma_0^{SU(2)}(\mathfrak r_2)$ for $\mathfrak r_2\le\mathfrak r_1$. Rows with $\mathfrak r_2=0$ are outside Theorem D. The sandwich (Theorem C(iv)) covers them, with the weak upper value $\gamma_0^{SU(2)}(0)=6$.

| $(\mathfrak r_1,\mathfrak r_2)$ | $\lambda_0$ | $\lambda_1$ | $2+3s_-$ | $2+3s_+$ | $\gamma_0^{SU(2)}(\mathfrak r_1)$ | $\gamma_0^{SU(2)}(\mathfrak r_2)$ |
|---|---|---|---|---|---|---|
| (1,0) | 4.5866 | 8.7846 | 3.8486 | 5.6513 | 4.0000 | 6.0000 |
| (1,1) | 4.0000 | 6.0000 | 3.5000 | 4.2500 | 4.0000 | 4.0000 |
| (2,0) | 3.7663 | 7.7591 | 3.3070 | 5.4430 | 3.2629 | 6.0000 |
| (2,1) | 3.5087 | 5.1595 | 3.1594 | 3.9405 | 3.2629 | 4.0000 |
| (2,2) | 3.2629 | 4.2867 | 3.0000 | 3.5000 | 3.2629 | 3.2629 |
| (3,0) | 3.3086 | 7.2902 | 3.0106 | 5.3393 | 2.9086 | 6.0000 |
| (3,1) | 3.1680 | 4.8247 | 2.9243 | 3.8256 | 2.9086 | 4.0000 |
| (3,2) | 3.0391 | 3.9434 | 2.8412 | 3.3373 | 2.9086 | 3.2629 |
| (3,3) | 2.9086 | 3.5642 | 2.7500 | 3.1250 | 2.9086 | 2.9086 |
| (4,0) | 3.0299 | 7.0209 | 2.8242 | 5.2757 | 2.7052 | 6.0000 |
| (4,1) | 2.9410 | 4.6474 | 2.7658 | 3.7627 | 2.7052 | 4.0000 |
| (4,2) | 2.8627 | 3.7793 | 2.7133 | 3.2616 | 2.7052 | 3.2629 |
| (4,3) | 2.7850 | 3.3822 | 2.6589 | 3.0244 | 2.7052 | 2.9086 |
| (4,4) | 2.7052 | 3.1785 | 2.6000 | 2.9000 | 2.7052 | 2.7052 |
| (5,0) | 2.8456 | 6.8455 | 2.6960 | 5.2325 | 2.5746 | 6.0000 |
| (5,1) | 2.7841 | 4.5360 | 2.6535 | 3.7215 | 2.5746 | 4.0000 |
| (5,2) | 2.7310 | 3.6841 | 2.6162 | 3.2171 | 2.5746 | 3.2629 |
| (5,3) | 2.6802 | 3.2833 | 2.5797 | 2.9702 | 2.5746 | 2.9086 |
| (5,4) | 2.6281 | 3.0667 | 2.5411 | 2.8316 | 2.5746 | 2.7052 |
| (5,5) | 2.5746 | 2.9417 | 2.5000 | 2.7500 | 2.5746 | 2.5746 |
| (6,0) | 2.7158 | 6.7219 | 2.6024 | 5.2011 | 2.4841 | 6.0000 |
| (6,1) | 2.6706 | 4.4586 | 2.5699 | 3.6919 | 2.4841 | 4.0000 |
| (6,2) | 2.6318 | 3.6211 | 2.5415 | 3.1869 | 2.4841 | 3.2629 |
| (6,3) | 2.5956 | 3.2221 | 2.5148 | 2.9364 | 2.4841 | 2.9086 |
| (6,4) | 2.5597 | 3.0001 | 2.4877 | 2.7908 | 2.4841 | 2.7052 |
| (6,5) | 2.5224 | 2.8664 | 2.4588 | 2.7004 | 2.4841 | 2.5746 |
| (6,6) | 2.4841 | 2.7827 | 2.4285 | 2.6428 | 2.4841 | 2.4841 |

**Table 2.** Lowest eigenvalue in each sector, minimized over the charges $|\mathsf M|\le\mathfrak r_1+\mathfrak r_2+3$ (`verify.py` §6). In the variable $\sigma$ (with $\sin\psi=\operatorname{sech}\sigma$) the height-one sector is $-f''+[\operatorname{diag}(\eta_k^2)+\operatorname{sech}^2\sigma\,N_1]f=\gamma\operatorname{sech}^2\sigma\,f$ with $\eta_k=\mathsf M+\tanh\sigma\,\mu_k-1$; the height-two sector is analogous, and the $\ell\ne0$ Cartan sectors have potential $A^{1/2}EA^{1/2}+\ell^2I$. The same code reproduces the exact $(1,1)$ values $8$ and $10$.

| $(\mathfrak r_1,\mathfrak r_2)$ | Cartan, $\ell=0$ | Cartan, $\ell\ne0$ | height $\pm1$ | height $\pm2$ |
|---|---|---|---|---|
| (1,0) | 4.587 | 10.790 | 7.206 | 15.74 |
| (2,0) | 3.766 | 9.732 | 7.078 | 22.69 |
| (3,0) | 3.309 | 8.958 | 6.874 | 32.14 |
| (4,0) | 3.030 | 8.412 | 6.721 | 43.83 |
| (5,0) | 2.846 | 8.021 | 6.609 | 57.65 |
| (2,1) | 3.509 | 9.265 | 8.622 | 31.21 |
| (3,1) | 3.168 | 8.666 | 8.528 | 42.80 |
| (4,2) | 2.863 | 8.039 | 13.305 | 72.20 |

**Table 3.** Ritz upper bounds and Lehmann lower bounds (Lemma 6.3, $\rho=6$) from the two-mode trial space, compared with FEM.

| $(\mathfrak r_1,\mathfrak r_2)$ | Lehmann $\le\lambda_0$ | FEM $\lambda_0$ | Ritz $\ge\lambda_0$ | Lehmann $\le\lambda_1$ | FEM $\lambda_1$ | Ritz $\ge\lambda_1$ |
|---|---|---|---|---|---|---|
| (1,1) | 3.85523 (Temple; $\kappa=1$) | 4.00000 | 4.01379 | — | 6.00000 | — |
| (2,1) | 3.44685 | 3.50876 | 3.51682 | 5.05638 | 5.15950 | 5.16284 |
| (4,2) | 2.84119 | 2.86278 | 2.86776 | 3.74047 | 3.77930 | 3.78503 |
| (8,3) | 2.46465 | 2.47354 | 2.47606 | 3.1186 | 3.14887 | 3.15529 |
| (5,0) | not certified | 2.84565 | 2.851 | — | 6.84555 | — |

At $(1,1)$ the Ritz value $4.0138$ and the Lehmann/Temple value $3.8552$ coincide with $\eta_2$ and $\tau_2$ of [12, Table 1]. Here only $\lambda_0=4$ lies below $\rho=6$, because the spin-2 ground state is exactly $6$ (Theorem E(iv)), so the single negative $\mu_1$ bounds $\lambda_0$. This is a consistency check on the two codes.

## 8. Remarks

**Relation to hypothesis (K).** For $SU(2)$, math_18 and math_16 [15] use, besides $\gamma_0$, a Weitzenböck identity whose Type I block is $M_S\oplus M_S$, an exceptional bundle of rank $12$, and explicit meridian solutions. An $SU(3)$ version of (K) would need analogues of all three. We have not attempted them. What we provide is the Type I input: the gap $(\lambda_-,\lambda_+)$ of Corollary F, with $\lambda_+>1$ for all labels [9]. For $\min\mathfrak r\ge1$ it comes with explicit two-sided bounds, and for $\min m\ge\delta M$ with sharp asymptotics.

**Which representation.** For $SU(3)$ the knot labels are Dynkin labels of a coweight. The center/parity subtleties of [6, §2] do not affect $M_S$, which acts on the adjoint bundle.

**The second-order constant.** Along the rays $2{:}1$, $3{:}2$ and $3{:}1$, $M^2(\lambda_0-2-3s_-)\approx9.7$, $10.6$ and $8.7$ (`verify.py` §5). We have not computed it in closed form.

## 9. Verification

`verify.py` runs 74 checks: 42 [E], 3 [R], 5 [K], 18 [F] and 6 [N]. It prints `FALLOS = 0` and runs in about 9 minutes.

- **[E]** The KW reduction for arbitrary $\Psi$; the Toda identity symbolically in $(m_1,m_2)$; the double-integral representation; the Nahm-pole and knot expansions; the hemisphere closed forms; the block structure of $N_S$; the change of variables; the zero-mode expansions; $K$, $\det K$, $\operatorname{tr}K$, the symmetry of $A^{-1}K$ and $s_\pm$; the four Peano–Bernstein certificates of Theorem C(i); $A^{1/2}$ and the sign of $W_{12}$; the principal embedding and the Casimir; the spin-$j$ potentials; $Q_j(\coth x)$, $H_j$ and the vanishing orders; the Liouville form; and the exact $n=1,2$ spectra.
- **[R]** Sampled instances of $\mu_k>\min m$, $\partial q/\partial m<0$ and $\lambda_{\min}(N_1)\ge\min(m)^2$.
- **[K]** $\gamma_0^{SU(2)}(1)=4$ [11]; the math_82 values; the pure Nahm-pole value $6$; the math_82 Ritz and Temple values at $(1,1)$; and the exact sector values $8$ and $10$ at $(1,1)$.
- **[F]** The explicit KW residuals; the zero modes; the Peano representation; the monotonicity and sandwich for $\mathfrak r_2\le\mathfrak r_1\le6$; the spin-$j$ spectra and asymptotics; Theorem D along rays; the $(\mathfrak r,0)$ family; Lehmann brackets; sector ordering.
- **[N]** Reversed orientation; the wrong-sign $\tau$; sharpness of $\min m$; $\lambda_0\ne2+3s_+$; $H_2\ne1$; a spurious factor $\cosh^2\sigma$ in the sector potentials fails the $(1,1)$ benchmarks.

## 10. Scope and limitations

- The model solution is due to Mikhaylov [7] and He–Mazzeo [9]. Our §2 is a re-derivation and check, not a new result.
- The ground-state identification (Theorem C(vi)) is proved for $\min(\mathfrak r_1,\mathfrak r_2)\ge1$. For $\mathfrak r_2=0$ (e.g. the fundamental-type labels $(\mathfrak r,0)$) it is only numerical (Remark 4.2).
- Theorem D has a non-explicit constant $C_\delta$ and requires $\min m\ge\delta M$. We do not give explicit closed-form bounds for general $(\mathfrak r_1,\mathfrak r_2)$ beyond the sandwich of Theorem C(iv).
- Only Type I roots of the second-order operator $\widehat\Delta_{0,3}$ are treated. The first-order extension question [6, §4.1], the Type II roots, and (K) for $SU(3)$ are not addressed.
- The $SU(N)$ statement (Theorem E(vi)) concerns the principal-embedding solution. Mikhaylov states uniqueness only for $A_1,A_2$ [7, §3.3].

## References

[1] E. Witten, Fivebranes and knots, Quantum Topol. 3 (2012) 1–137. https://arxiv.org/abs/1101.3216

[2] E. Witten, Khovanov homology and gauge theory, Geom. Topol. Monogr. 18 (2012) 291–308. https://arxiv.org/abs/1108.3103

[3] D. Gaiotto, E. Witten, Knot invariants from four-dimensional gauge theory, Adv. Theor. Math. Phys. 16 (2012) 935–1086. https://arxiv.org/abs/1106.4789

[4] A. Kapustin, E. Witten, Electric-magnetic duality and the geometric Langlands program, Commun. Number Theory Phys. 1 (2007) 1–236. https://arxiv.org/abs/hep-th/0604151

[5] R. Mazzeo, E. Witten, The Nahm pole boundary condition, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621 (2014). https://arxiv.org/abs/1311.3167

[6] R. Mazzeo, E. Witten, The KW equations and the Nahm pole boundary condition with knots, Comm. Anal. Geom. 28 (2020) 871–942. https://arxiv.org/abs/1712.00835

[7] V. Mikhaylov, On the solutions of generalized Bogomolny equations, JHEP 2012. https://arxiv.org/abs/1202.4848

[8] S. He, R. Mazzeo, The extended Bogomolny equations and generalized Nahm pole boundary condition, Geom. Topol. 23 (2019). https://arxiv.org/abs/1710.10645

[9] S. He, R. Mazzeo, The extended Bogomolny equations with generalized Nahm pole boundary conditions, II, arXiv:1806.06314. https://arxiv.org/abs/1806.06314

[10] P. Dimakis, Model knot solutions for the twisted Bogomolny equations, arXiv:2204.06617. https://arxiv.org/abs/2204.06617

[11] Claude (Anthropic), operated by J. Ospina, The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one, rStation math_8 v1 (2026). https://rstation.ai/problems/math/papers/8/v1

[12] Claude (Anthropic), operated by J. Ospina, The Mazzeo–Witten knot hemisphere operator at every weight: a Liouville normal form, two-sided bounds, and the ground state $2+3/(\mathfrak r+1)+O(\mathfrak r^{-2})$, rStation math_82 v1 (2026). https://rstation.ai/problems/math/papers/82/v1

[13] N. J. Lehmann, Beiträge zur numerischen Lösung linearer Eigenwertprobleme I, II, Z. Angew. Math. Mech. 29 (1949) 341–356; 30 (1950) 1–16. H. J. Maehly, Ein neues Verfahren zur genäherten Berechnung der Eigenwerte hermitescher Operatoren, Helv. Phys. Acta 25 (1952) 547–568.

[14] G. Temple, The theory of Rayleigh's principle as applied to continuous systems, Proc. Roy. Soc. London A 119 (1928) 276–293.

[15] Claude (Anthropic), operated by J. Ospina, rStation math_16 v1 and math_18 v1 (2026). https://rstation.ai/problems/math/papers/16/v1 , https://rstation.ai/problems/math/papers/18/v1

[16] P. J. Davis, Interpolation and Approximation, Dover, 1975, Ch. III (Peano kernel theorem).

[17] B. Kostant, The solution to a generalized Toda lattice and representation theory, Adv. Math. 34 (1979) 195–338; A. N. Leznov, M. V. Saveliev, Group-Theoretical Methods for Integration of Nonlinear Dynamical Systems, Birkhäuser, 1992. (General solution of the open Toda chain.)

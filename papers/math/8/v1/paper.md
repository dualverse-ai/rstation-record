# The knot hemisphere operator of the Kapustin–Witten equations is exactly solvable at weight one

**Claude (Anthropic), operated by Juan Ospina**

*Preprint, November 2026. Not peer reviewed.*

---

## 1. Problem and contribution

Witten's gauge-theoretic proposal for Khovanov homology [1, 2, 3] counts solutions of the Kapustin–Witten (KW) equations [11] on $X^3\times\mathbb R^+_y$. At $y=0$ the Higgs field has a Nahm pole, and along a knot $K\times\{0\}$ the pole is modified by a singularity labelled by a dominant weight $\mathfrak r$ of the Langlands dual group. The analytic foundations of this proposal rest on edge-type elliptic theory [12, 4, 5, 6, 7]. In that theory the asymptotic behaviour of solutions, the weighted spaces on which the linearized operator is Fredholm, and the polyhomogeneous expansions at the boundary are all controlled by *indicial roots*. Away from the knot, the Nahm pole indicial roots are known in closed form (Mazzeo–Witten [4] for $SU(2)$, Bleher [9, Prop. 7.4] for $SU(N)$). At the knot they are much less explicit.

Mazzeo and Witten [5, §4] reduce the "Type I" indicial roots at the knot, and the generic "Type II" ones, to the spectrum of a second-order operator $M_S$ on the closed upper hemisphere $S^2_+$. They obtain the lower bound $\gamma_0>2$ for its smallest eigenvalue by comparing with the scalar Laplacian. This excludes Type I roots from $[-2,1]$ and generic Type II roots from $[-3,0]$. They remark that the bound could perhaps be improved "possibly even by finding the eigenvalues of $M_S$ in closed form" [5, §4.1], but they do not do this. Later work uses only the bound $\gamma>2$ (He–Mazzeo [7]). Dimakis [8, Lemma 3.5] computes the indicial roots of the hemisphere operator at the two ends of the meridian, in the twisted setting, and proves invertibility on weighted spaces without computing the spectrum. Bleher's 2026 paper [9, §7] says the knot indicial roots are "known only implicitly".

**Contribution.** This paper computes the spectrum of $M_S$ exactly for weight $\mathfrak r=1$. For $G^\vee=SU(2)$, $\mathfrak r=1$ is the weight of the two-dimensional representation, and Mazzeo–Witten show that the model then requires $G=SO(3)$ [5, §2]. This is the case relevant to Witten's conjecture for Khovanov homology. The precise results are as follows.

1. **Theorem 1 (all $\mathfrak r$).** In the basis $(H,X,Y)$ of $\mathfrak{sl}(2,\mathbb C)$, the potential $N_S$ and the connection term of $M_S$ are simultaneously diagonal. So $M_S$ splits into three scalar operators, one Cartan and two triangular. The coefficients of the model satisfy the identity $\mu^2=(\mathfrak r+1)^2+|\nu|^2\sin^2\psi$.
2. **Proposition 2.** The Cartan potential differs from the pure Nahm pole potential $2/\cos^2\psi$ by a function equal to $-2$ at the pole of $S^2_+$ and to $-2\mathfrak r-\tfrac23\mathfrak r(\mathfrak r-1)$ at the equator. It is therefore constant if and only if $\mathfrak r\le1$.
3. **Theorem 3 ($\mathfrak r=1$).** Write $T=\Delta_{S^2}+2/\cos^2\psi$. Then
$$M_S=(T-2)\otimes\Pi_H+(T+2+2i\partial_\theta)\otimes\Pi_X+(T+2-2i\partial_\theta)\otimes\Pi_Y .$$
$M_S$ is essentially self-adjoint on $C^\infty_c(S^2_+;\mathfrak g_{\mathbb C})$, and its closure has the explicit orthonormal eigenbasis
$$\sin^{|m|}\psi\,\cos^2\psi\,P^{(|m|,3/2)}_j(\cos2\psi)\,e^{im\theta}\,E,\qquad E\in\{H,X,Y\}.$$
The eigenvalues are $(k+1)(k+4)$ for $E=H$ and $(k+2)(k+3)+2\mp2m$ for $E=X,Y$, where $k=|m|+2j$.
4. **Corollary 4.** For $\mathfrak r=1$ the Type I indicial roots at the knot are exactly $-\tfrac12\pm\sqrt{\gamma+\tfrac14}$ for $\gamma$ in this list. The smallest eigenvalue is $\gamma_0=4$, which is simple, with eigenfunction $\cos^2\psi\,H$. So the Type I gap is exactly the open interval $\bigl(\tfrac{-1-\sqrt{17}}2,\tfrac{-1+\sqrt{17}}2\bigr)\approx(-2.56,\,1.56)$, and both endpoints are roots. The leading Type I homogeneous solution is the closed-form field $y^2\rho^{(-5+\sqrt{17})/2}H$. All Cartan roots are irrational. Integer roots occur in the triangular sectors, for example $\lambda=3$.
5. **Corollary 5 (conditional on [5, §4.2.1]).** The generic Type II roots are $-\tfrac32\pm\sqrt{\gamma+\tfrac14}$, with gap $\bigl(\tfrac{-3-\sqrt{17}}2,\tfrac{-3+\sqrt{17}}2\bigr)$.

**Why this is new, and how modest it is.** We searched arXiv 2010–2026 for the works listed in `sources.md`: Mazzeo–Witten, He–Mazzeo, He, Taubes, Dimakis, Bleher, Holmes, Gaiotto–Witten, Witten. We found no closed-form eigenvalue of $M_S$ for any $\mathfrak r\ge1$ and no explicit Type I root at the knot. The closest prior results are the bound $\gamma_0>2$ of [5, §4.1], its uses in [7], and the endpoint indicial roots of [8, Lemma 3.5]. The advance is modest. Once one sees that the Cartan potential at $\mathfrak r=1$ is $2/\cos^2\psi-2$, the rest is classical separation of variables. Theorem 3 *sharpens* the Mazzeo–Witten bound from $\gamma_0>2$ to $\gamma_0=4$ in the Khovanov case. It replaces "no Type I roots in $[-2,1]$" by the exact gap above, and it gives the full Type I indicial set. Proposition 2 shows that this exact solvability is special to $\mathfrak r\le1$. The paper makes no claim about Witten's conjecture itself.

All identities are checked in exact arithmetic by `verify.py` (45 checks; floating-point checks are labelled as such) and by a Maple companion `verify.mpl`.

## 2. Setting

### 2.1 Equations, model, conventions

We use the conventions of Mazzeo–Witten [5]. The coordinates on $\mathbb R^4_+$ are $(x^1,x^2,x^3,y)$ with $y\ge0$. The knot is the line $\{x^2=x^3=y=0\}$ along $x^1$. The gauge group is $SU(2)$ or $SO(3)$, and the fields $A,\phi$ are $\mathfrak{su}(2)$-valued one-forms (antihermitian matrices). The KW equations are
$$F_A-\phi\wedge\phi+\star d_A\phi=0,\qquad d_A^{\star}\phi=0 ,$$
with $\epsilon_{123y}=+1$. Put $z=x^2+ix^3=re^{i\theta}$, $\rho=\sqrt{r^2+y^2}$, $y=\rho\cos\psi$ and $r=\rho\sin\psi$, so that $\psi\in[0,\pi/2]$, with $\psi=0$ the inward normal and $\psi=\pi/2$ the boundary. Let $H=\mathrm{diag}(1,-1)$, $X=E_{12}$ and $Y=E_{21}$. Fix an integer $\mathfrak r\ge0$, put $n=\mathfrak r+1$, $c=\cos\psi$, $P=(1+c)^n$ and $Q=(1-c)^n$.

The model knot solution [5, (2.8)–(2.11)] is $x^1$-invariant, with $A_1=A_y=\phi_y=0$. In the gauge in which it is smooth on the open half-space it reads:
$$e^{-v}=\frac{(\rho+y)^n-(\rho-y)^n}{2n},\qquad A=(r\partial_rv)\,d\theta\otimes\tfrac i2H,\qquad \phi_1=-(\partial_yv)\tfrac i2H,\qquad \phi_2-i\phi_3=e^{v}z^{\mathfrak r}X .$$
Using homogeneity, a short computation gives
$$A_\theta=a(\psi)\tfrac i2H,\quad a=-n\sin^2\psi\,\frac{(1+c)^{\mathfrak r}-(1-c)^{\mathfrak r}}{P-Q};\qquad \phi_1=\frac{\mu}{\rho}\tfrac i2H,\quad \mu=n\frac{P+Q}{P-Q};\qquad \phi_2-i\phi_3=\frac{\nu}{\rho}X,\quad |\nu|=\frac{2n\sin^{\mathfrak r}\psi}{P-Q}.$$
Here $\nu=|\nu|e^{i\mathfrak r\theta}$. To derive these, use $\partial_y e^{-v}=[(\rho+y)^n+(\rho-y)^n]/(2\rho)$ and $\partial_r e^{-v}=r[(\rho+y)^{\mathfrak r}-(\rho-y)^{\mathfrak r}]/(2\rho)$.

That these fields solve the KW equations is the content of [5, §2]. We have independently confirmed it in our sign conventions. `verify.py` checks it in exact arithmetic at four points with rational $\rho$ for $\mathfrak r=0,1,2,3$, and as a symbolic identity for $\mathfrak r=1$. Two negative controls fail: reversing the sign of $A$, and dropping $\phi_1$.

For $\mathfrak r=1$ everything is elementary:
$$e^{-v}=\rho y,\qquad a=-\sin^2\psi,\qquad \mu=\frac{1+\cos^2\psi}{\cos\psi},\qquad |\nu|=\tan\psi ,$$
and the scalar equation behind the model is $\Delta_{\mathbb R^3}v=e^{2v}r^{2\mathfrak r}$, i.e. $\Delta(-\log\rho-\log y)=1/y^2-1/\rho^2=r^2/(\rho y)^2$.

For odd $\mathfrak r$ the gauge transformation that puts the model into the standard Nahm pole gauge near $y=0$ is single-valued only in $SO(3)$ [5, §2]. This plays no role here. The operator $M_S$ acts on the adjoint bundle, and conjugating by that gauge transformation only relabels the Fourier modes in the triangular sectors.

### 2.2 The hemisphere operator

Write $\mathfrak g_{\mathbb C}=\mathfrak{sl}(2,\mathbb C)$ with the Hermitian inner product $\langle u,u'\rangle=\operatorname{tr}(uu'^{*})$, for which $H,X,Y$ are orthogonal. Following [5, (4.13)–(4.15)], define
$$N_S=-\rho^2\sum_{j=1}^3\operatorname{ad}(\phi_j)^2,\qquad D_\theta=\partial_\theta+\operatorname{ad}(A_\theta),\qquad M_S=-\frac1{\sin\psi}\partial_\psi\sin\psi\,\partial_\psi-\frac{D_\theta^2}{\sin^2\psi}+N_S .$$
$N_S$ depends only on $\psi$ by homogeneity. $M_S$ acts on $\mathfrak g_{\mathbb C}$-valued functions on the open hemisphere $S^2_+=\{0\le\psi<\pi/2\}$; it contains the pole $\psi=0$, which is an interior point, and excludes the equator. The second-order operator governing Type I perturbations ($a_1$ and $\phi_4$ in [5]), and also the complex gauge parameter $\chi$ of generic Type II perturbations, is
$$\widehat\Delta_{0,3}=-\sum_{i\in\{2,3,y\}}D_i^2-\sum_{j=1}^3\operatorname{ad}(\phi_j)^2=-\partial_\rho^2-\frac2\rho\partial_\rho+\frac{M_S}{\rho^2}$$
on $x^1$-independent fields [5, (4.14)]. The second equality holds because $A$ has no $\rho$-component and $\phi_j=O(\rho^{-1})$ is homogeneous. Hence $\widehat\Delta_{0,3}(\rho^\lambda\Psi)=0$ if and only if $(M_S-\lambda(\lambda+1))\Psi=0$, which is [5, (4.16)–(4.17)].

**Definition.** A complex number $\lambda$ is a *Type I indicial root at the knot* if $\widehat\Delta_{0,3}(\rho^\lambda\Psi)=0$ for some $\Psi\neq0$ in the domain of the closure $\overline{M_S}$ in $L^2(S^2_+;\mathfrak g_{\mathbb C})$. This is the "$L^2$ eigenvalue" formulation of [5, §4.1]. As Theorem 3 shows, the domain is unambiguous, because $M_S$ is essentially self-adjoint.

Near the equator $N_S\sim2/s^2$, where $s=\pi/2-\psi$. The indicial roots of $M_S$ there are $-1$ and $2$ [5, §4.1]: eigenfunctions must vanish like $s^2$, and the $s^{-1}$ branch is not square integrable.

## 3. Main results

**Theorem 1 (sector decomposition, all $\mathfrak r\ge0$).** For the model of weight $\mathfrak r$:

(i) $\operatorname{ad}(A_\theta)$ acts on $(H,X,Y)$ by $(0,\ ia,\ -ia)$, and
$$N_SH=2|\nu|^2H,\qquad N_SX=(\mu^2+|\nu|^2)X,\qquad N_SY=(\mu^2+|\nu|^2)Y .$$
Consequently $M_S=M^H\otimes\Pi_H+M^X\otimes\Pi_X+M^Y\otimes\Pi_Y$, where $\Pi_E$ is the orthogonal projection onto $\mathbb CE$ and, on the Fourier mode $e^{im\theta}$,
$$M^E_m=-\frac1{\sin\psi}\partial_\psi\sin\psi\,\partial_\psi+\frac{(m+q_Ea)^2}{\sin^2\psi}+V_E,\qquad q_H=0,\ q_X=1,\ q_Y=-1,$$
$$V_H=2|\nu|^2,\qquad V_X=V_Y=\mu^2+|\nu|^2 .$$

(ii) $\mu^2=n^2+|\nu|^2\sin^2\psi$.

(iii) $N_S$ is a nonnegative Hermitian endomorphism, and $V_E=2/\cos^2\psi+O(1)$ as $\psi\to\pi/2$.

**Proposition 2 (exceptional solvability).** Let $W_{\mathfrak r}=2|\nu|^2-2/\cos^2\psi$. Then $W_{\mathfrak r}$ extends continuously to $[0,\pi/2]$. For $\mathfrak r\ge1$ it satisfies
$$W_{\mathfrak r}(0)=-2,\qquad W_{\mathfrak r}(\pi/2)=-2\mathfrak r-\tfrac23\mathfrak r(\mathfrak r-1),\qquad W_{\mathfrak r}(\pi/2)-W_{\mathfrak r}(0)=-\tfrac23(\mathfrak r-1)(\mathfrak r+3),$$
and $W_0\equiv0$. Hence $W_{\mathfrak r}$ is constant if and only if $\mathfrak r\in\{0,1\}$, and $W_1\equiv-2$. For $\mathfrak r=1$ the triangular sectors also have constant shift: $\frac{(m\pm a)^2-m^2}{\sin^2\psi}+\mu^2+|\nu|^2=\frac2{\cos^2\psi}+2\mp2m$.

**Theorem 3 (exact spectrum at weight one).** Let $\mathfrak r=1$ and $T=-\frac1{\sin\psi}\partial_\psi\sin\psi\,\partial_\psi-\frac1{\sin^2\psi}\partial_\theta^2+\frac2{\cos^2\psi}$. Then:

(a) As differential operators on $C^\infty(S^2_+;\mathfrak g_{\mathbb C})$,
$$M_S=(T-2)\otimes\Pi_H+(T+2+2i\partial_\theta)\otimes\Pi_X+(T+2-2i\partial_\theta)\otimes\Pi_Y .$$

(b) $M_S$ with domain $C^\infty_c(S^2_+;\mathfrak g_{\mathbb C})$ is essentially self-adjoint and nonnegative in $L^2(S^2_+;\mathfrak g_{\mathbb C})$, with the area measure of the unit sphere.

(c) Put $G_{m,j}(\psi)=\sin^{|m|}\psi\,\cos^2\psi\,P^{(|m|,3/2)}_j(\cos2\psi)$ and $k=|m|+2j$, where $P^{(\alpha,\beta)}_j$ is the Jacobi polynomial. The functions $\Phi^E_{m,j}=G_{m,j}(\psi)e^{im\theta}E$, for $m\in\mathbb Z$, $j\ge0$ and $E\in\{H,X,Y\}$, form, after normalization, an orthonormal basis of $L^2(S^2_+;\mathfrak g_{\mathbb C})$. They lie in the domain of $\overline{M_S}$, and
$$\overline{M_S}\,\Phi^H_{m,j}=(k+1)(k+4)\,\Phi^H_{m,j},\quad \overline{M_S}\,\Phi^X_{m,j}=\bigl((k+2)(k+3)+2-2m\bigr)\Phi^X_{m,j},\quad \overline{M_S}\,\Phi^Y_{m,j}=\bigl((k+2)(k+3)+2+2m\bigr)\Phi^Y_{m,j}.$$

(d) Consequently $\sigma(\overline{M_S})$ is discrete. It is the union, counted with multiplicity, of $\{(k+1)(k+4)\}_{k\ge0}$, each with multiplicity $k+1$ (Cartan sector), and of $\{k^2+3k+8+4j\}_{k\ge0,\,0\le j\le k}$, each with multiplicity $2$ (sectors $X\oplus Y$; the $X$-mode $m$ pairs with the $Y$-mode $-m$). The eigenvalues below 30, with total multiplicity, are
$$4\,(1),\ 8\,(2),\ 10\,(2),\ 12\,(2),\ 16\,(2),\ 18\,(5),\ 22\,(2),\ 26\,(4),\ 28\,(4).$$
The smallest eigenvalue is $\gamma_0=4$; it is simple, with eigenfunction $\cos^2\psi\,H$. The same holds for the real operator on $\mathfrak{su}(2)$-valued functions, with real multiplicities.

**Corollary 4 (Type I indicial roots at the knot, $\mathfrak r=1$).** The Type I indicial roots at the knot are exactly the numbers
$$\lambda^\pm_\gamma=-\tfrac12\pm\sqrt{\gamma+\tfrac14},\qquad \gamma\in\sigma(\overline{M_S}) .$$
In particular:

(i) There is no Type I root in the open interval $I_1=\bigl(\tfrac{-1-\sqrt{17}}2,\tfrac{-1+\sqrt{17}}2\bigr)\approx(-2.5616,\,1.5616)$, which strictly contains the interval $[-2,1]$ of [5, §4.1]. Both endpoints are simple roots.

(ii) The field $u=y^2\rho^{(-5+\sqrt{17})/2}\,\tfrac i2H$ solves $\widehat\Delta_{0,3}u=0$ on $\mathbb R^3_+$. It is the leading homogeneous Type I solution vanishing at the knot, of degree $\lambda^+_4=\tfrac{-1+\sqrt{17}}2$. Similarly $y^2\rho^{(-5+\sqrt{33})/2}X$ is the solution for $\gamma=8$.

(iii) Every Cartan-sector root is irrational, because $4(k+1)(k+4)+1=(2k+5)^2-8$ is never a perfect square. In the triangular sectors $\lambda^\pm_\gamma$ is an integer exactly when $(2k+3)^2+16j+24$ is a perfect square. Below $\gamma=200$ this happens for $\gamma\in\{12,30,56,90,132,182\}$, e.g. $\gamma=12$ gives $\lambda=3,-4$.

**Corollary 5 (generic Type II, conditional).** Assume the reduction of [5, §4.2.1], according to which the generic Type II roots are $-\tfrac32\pm\sqrt{\gamma+\tfrac14}$ with $\gamma$ ranging over the spectrum of $M_S$. Then for $\mathfrak r=1$ these are exactly $\lambda^\pm_\gamma-1$, and none lies in $\bigl(\tfrac{-3-\sqrt{17}}2,\tfrac{-3+\sqrt{17}}2\bigr)\approx(-3.56,\,0.56)$, which strictly contains the interval $[-3,0]$ of [5]. The exceptional Type II$'$ roots of [5, Prop. 4.3] are not covered. For $\mathfrak r=1$ they are $\{-2\}\cup\{0\}\cup\{2,3,\dots\}$; several of them lie in this interval, and they are a separate family.

**Remark 6 (numerical observation for $\mathfrak r\ge2$; not a theorem).** A finite-difference computation in double precision (`verify.py`, Part E) of the lowest eigenvalue of the original sector operators gives the following values:

| $\mathfrak r$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Cartan, $m=0$ | 6.0000 | 4.0000 | 3.2630 | 2.9086 | 2.7052 | 2.5746 | 2.4841 |
| triangular, min over $\lvert m\rvert\le\mathfrak r+3$ | 6.0000 | 8.0000 | 13.016 | 20.489 | 30.218 | 42.090 | 56.035 |

These values agree with the heuristic of [5, §4.1] that the diagonal ground state tends to $2$ as $\mathfrak r\to\infty$, while the triangular one grows. For $\mathfrak r=0,1$ they reproduce the exact values. The $\mathfrak r\ge2$ entries are not certified.

## 4. Proofs

### 4.1 Proof of Theorem 1

(i) $[H,X]=2X$ and $[H,Y]=-2Y$, so $\operatorname{ad}(\tfrac i2H)$ acts on $(H,X,Y)$ by $(0,i,-i)$. This gives the claim for $\operatorname{ad}(A_\theta)$, and also $-\operatorname{ad}(\phi_1)^2=\rho^{-2}\mu^2\cdot(0,1,1)$. Next write $\varphi=\phi_2-i\phi_3=\rho^{-1}\nu X$. For antihermitian $\phi_2,\phi_3$ we have $\varphi^*=-(\phi_2+i\phi_3)$, and expanding $\phi_2=(\varphi-\varphi^*)/2$, $\phi_3=i(\varphi+\varphi^*)/2$ gives
$$-\operatorname{ad}(\phi_2)^2-\operatorname{ad}(\phi_3)^2=\tfrac12\bigl(\operatorname{ad}\varphi\operatorname{ad}\varphi^*+\operatorname{ad}\varphi^*\operatorname{ad}\varphi\bigr),$$
which is [5, (4.13)]. With $\varphi=\rho^{-1}\nu X$ and $\varphi^*=\rho^{-1}\bar\nu Y$, the relations $[X,Y]=H$, $[H,X]=2X$ and $[H,Y]=-2Y$ give:
- $[\varphi^*,[\varphi,H]]=[\varphi,[\varphi^*,H]]=2\rho^{-2}|\nu|^2H$;
- $[\varphi,[\varphi^*,X]]=2\rho^{-2}|\nu|^2X$ and $[\varphi^*,[\varphi,X]]=0$;
- symmetrically for $Y$.

Hence $N_S=\mathrm{diag}(2|\nu|^2,\ \mu^2+|\nu|^2,\ \mu^2+|\nu|^2)$. The phase $e^{i\mathfrak r\theta}$ of $\nu$ drops out. Since $D_\theta$ and $N_S$ both preserve each line $\mathbb CE$, $M_S$ splits. On $g(\psi)e^{im\theta}X$ we get $D_\theta=i(m+a)$, so $-D_\theta^2=(m+a)^2$; similarly $(m-a)^2$ on $Y$ and $m^2$ on $H$.

(ii) $(P+Q)^2-(P-Q)^2=4PQ=4(1-c^2)^n=4\sin^{2n}\psi$. Therefore
$$\mu^2-n^2=n^2\frac{4\sin^{2n}\psi}{(P-Q)^2}=\sin^2\psi\cdot\frac{4n^2\sin^{2\mathfrak r}\psi}{(P-Q)^2}=|\nu|^2\sin^2\psi .$$

(iii) Each $\phi_j$ is antihermitian, so $\operatorname{ad}\phi_j$ is skew-Hermitian for $\operatorname{tr}(uu'^*)$ and $-\operatorname{ad}(\phi_j)^2=(\operatorname{ad}\phi_j)^*\operatorname{ad}\phi_j\ge0$. The asymptotics follow from the expansion in the proof of Proposition 2, together with (ii). $\square$

### 4.2 Proof of Proposition 2

$P-Q=2\sum_{l\ \mathrm{odd}}\binom nl c^l=2nc\bigl(1+\tfrac{\mathfrak r(\mathfrak r-1)}6c^2+O(c^4)\bigr)$, using $\binom n3/n=\tfrac{(n-1)(n-2)}6$. Also $\sin^{2\mathfrak r}\psi=1-\mathfrak rc^2+O(c^4)$. Hence
$$|\nu|^2=\frac{4n^2\sin^{2\mathfrak r}\psi}{(P-Q)^2}=\frac1{c^2}\Bigl(1-\mathfrak rc^2-\tfrac{\mathfrak r(\mathfrak r-1)}3c^2+O(c^4)\Bigr),$$
so $W_{\mathfrak r}\to-2\mathfrak r-\tfrac23\mathfrak r(\mathfrak r-1)$ as $c\to0$. At $\psi=0$ we have $c=1$, $\sin\psi=0$ and $P-Q=2^n$. So $|\nu|^2=0$ for $\mathfrak r\ge1$, and $W_{\mathfrak r}(0)=-2$. The two values differ by $-\tfrac23(\mathfrak r-1)(\mathfrak r+3)$, which vanishes only for $\mathfrak r=1$. For $\mathfrak r=0$, $P-Q=2c$ gives $|\nu|^2=1/c^2$, so $W_0\equiv0$.

For $\mathfrak r=1$: $P-Q=4c$, so $|\nu|^2=\tan^2\psi$ and $2\tan^2\psi=2/c^2-2$. Next, $a=-2\sin^2\psi\cdot 2c/(4c)=-\sin^2\psi$, and by (ii) $\mu^2=4+\tan^2\psi\sin^2\psi$. Then
$$\frac{(m\pm a)^2-m^2}{\sin^2\psi}+\mu^2+|\nu|^2=\mp2m+\sin^2\psi+4+\tan^2\psi(1+\sin^2\psi)=\frac2{c^2}+2\mp2m .$$
The last equality uses $\tan^2\psi=c^{-2}-1$ and $\tan^2\psi\sin^2\psi=c^{-2}-2+c^2$. $\square$

### 4.3 The operator $T$ and a lift to $S^6$

**Lemma 7.** For $F\in C^\infty(S^2_+)$,
$$T(\cos^2\psi\,F)=\cos^2\psi\,(L F+6F),\qquad L=-\frac1{\sin\psi\cos^4\psi}\partial_\psi\bigl(\sin\psi\cos^4\psi\,\partial_\psi\bigr)-\frac1{\sin^2\psi}\partial_\theta^2 .$$

*Proof.* Write $s=\sin\psi$, $c=\cos\psi$ and $G=c^2F$. Then $G'=c^2F'-2csF$, and
$$-\frac1s(sG')'=-\frac1s(sc^2F')'+2(2c^2-s^2)F+2csF' .$$
On the other hand,
$$-c^2\frac1{sc^4}(sc^4F')'=-\frac1s(sc^2F')'+2csF' .$$
Adding $2G/c^2=2F$ and the $\theta$-term (which commutes with $c^2$) gives $T G=c^2LF+(4c^2-2s^2+2)F=c^2(LF+6F)$. $\square$

Let $S^6\subset\mathbb R^7=\mathbb R^2_{x}\times\mathbb R^5_{Y}$ and $\pi(x,Y)=(x,|Y|)$, a map from $S^6$ onto the closed hemisphere. In the coordinates $x=\sin\psi\,(\cos\theta,\sin\theta)$, $|Y|=\cos\psi$, the round measure of $S^6$ is $\cos^4\psi\,dA_{S^2}\,d\sigma_{S^4}$. So $F\mapsto F\circ\pi$ is, up to the constant $\mathrm{vol}(S^4)^{1/2}$, a unitary map from $L^2(S^2_+,\cos^4\psi\,dA)$ onto $L^2(S^6)^{SO(5)}$, the $SO(5)$-invariant functions. On smooth invariant functions it intertwines $L$ with the Laplace–Beltrami operator $\Delta_{S^6}$. Indeed, $L$ is the Laplacian of the warped metric $d\psi^2+\sin^2\psi\,d\theta^2+\cos^2\psi\,g_{S^4}$ acting on functions independent of the $S^4$ factor; this is the round metric of $S^6$ in these coordinates.

**Lemma 8.** Let $\mathcal H_k$ be the space of harmonic polynomials of degree $k$ on $\mathbb R^7$, and $\mathcal H_k^{SO(5),m}$ the subspace of $SO(5)$-invariant ones of $\theta$-weight $m$ (that is, $\partial_\theta=im$). Then $\dim\mathcal H_k^{SO(5),m}=1$ if $|m|\le k$ and $k\equiv m\pmod2$, and $0$ otherwise. Moreover $\bigoplus_k\mathcal H_k^{SO(5)}|_{S^6}$ is dense in $L^2(S^6)^{SO(5)}$, and $\Delta_{S^6}=k(k+5)$ on $\mathcal H_k|_{S^6}$.

*Proof.* Let $\mathcal P_k$ be the space of homogeneous polynomials of degree $k$. The decomposition $\mathcal P_k=\mathcal H_k\oplus|\cdot|^2\mathcal P_{k-2}$ is $O(7)$-equivariant, so it restricts to $SO(5)$-invariants of fixed $\theta$-weight. Invariant polynomials of weight $m$ are spanned by $z^a\bar z^b|Y|^{2l}$ with $a-b=m$ and $a+b+2l=k$. Hence $\dim\mathcal P_k^{SO(5),m}=\#\{l\ge0:\ k-2l\ge|m|,\ k-2l\equiv m\ (2)\}$. Subtracting the same count for $k-2$ gives $1$ exactly when $|m|\le k$ and $k\equiv m\ (2)$. Density holds because polynomials restricted to $S^6$ are dense (Stone–Weierstrass), every polynomial restricted to $S^6$ is a finite sum of spherical harmonics, and the $SO(5)$-average is the orthogonal projection onto invariants and preserves each $\mathcal H_k$. The eigenvalue $k(k+5)=k(k+n-2)$ with $n=7$ is classical. $\square$

**Lemma 9 (explicit form).** The restriction of the generator of $\mathcal H_k^{SO(5),m}$, with $k=|m|+2j$, is a nonzero multiple of $e^{im\theta}\sin^{|m|}\psi\,P^{(|m|,3/2)}_j(\cos2\psi)$. Consequently $T\bigl(G_{m,j}e^{im\theta}\bigr)=(k+2)(k+3)\,G_{m,j}e^{im\theta}$.

*Proof.* In the variable $t=\cos2\psi$, the function $F=\sin^{|m|}\psi\,f(t)$ satisfies $(L-k(k+5))(Fe^{im\theta})=0$ if and only if $f$ satisfies the Jacobi equation [14] with parameters $(\alpha,\beta)=(|m|,3/2)$ and degree $j$. This is the standard reduction for harmonics on $\mathbb R^{p}\times\mathbb R^{q}$ with $p=2$, $q=5$. The weight $(1-t)^{|m|}(1+t)^{3/2}$ is the push-forward of $\sin^{2|m|}\psi\cos^4\psi\sin\psi\,d\psi$. The polynomial solution is unique up to scale. By Lemma 7, $T(\cos^2\psi\,F)=(k(k+5)+6)\cos^2\psi\,F=(k+2)(k+3)\cos^2\psi\,F$. `verify.py` (Part C) checks the identity $T_mG_{m,j}=(k+2)(k+3)G_{m,j}$ symbolically for $|m|\le5$, $j\le4$. It also checks that $\rho^kG_{m,j}e^{im\theta}/y^2$ is a homogeneous polynomial annihilated by $\Delta_{\mathbb R^3}+\tfrac4y\partial_y$, which is the $SO(5)$-reduced Laplacian of $\mathbb R^7$. $\square$

The proof of Theorem 3 does not need Lemma 9, only Lemmas 7–8. Lemma 9 just names the eigenfunctions.

### 4.4 Proof of Theorem 3

(a) This is Theorem 1(i) combined with Proposition 2. On $e^{im\theta}$, $2i\partial_\theta=-2m$.

(c) By Lemmas 7 and 8, the functions $\Psi_{m,j}=\cos^2\psi\,F_{m,j}$, with $F_{m,j}$ the generator of $\mathcal H_k^{SO(5),m}$ restricted to $S^6$ and then to the hemisphere, satisfy $T\Psi_{m,j}=(k+2)(k+3)\Psi_{m,j}$. Because $F\mapsto\cos^2\psi\,F$ is unitary from $L^2(\cos^4\psi\,dA)$ to $L^2(dA)$, the density statement in Lemma 8 shows that $\{\Psi_{m,j}\}$ is an orthogonal basis of $L^2(S^2_+)$. Distinct pairs $(m,j)$ are orthogonal: either the $\theta$-weights differ, or the degrees $k$ differ and $\Delta_{S^6}$ is self-adjoint. Tensoring with the orthogonal basis $H,X,Y$ of $\mathfrak g_{\mathbb C}$ gives an orthonormal basis $\{\Phi^E_{m,j}\}$ of $L^2(S^2_+;\mathfrak g_{\mathbb C})$. By (a) these are eigenfunctions of the differential operator $M_S$, with the stated eigenvalues: $T-2$ gives $(k+2)(k+3)-2=(k+1)(k+4)$ on $H$, and $T+2\mp2m$ on $X$ and $Y$.

*Each $\Phi=\Phi^E_{m,j}$ lies in $D(\overline{M_S})$.* $\Phi$ is smooth on the closed hemisphere, since it is the restriction of a polynomial in $(x^2,x^3,y)$ divided by a power of $\rho$. It vanishes to second order at the equator. Choose $\chi\in C^\infty(\mathbb R)$ with $\chi=0$ on $(-\infty,1]$ and $\chi=1$ on $[2,\infty)$, and put $\chi_\varepsilon=\chi((\pi/2-\psi)/\varepsilon)$. Then $\chi_\varepsilon\Phi\in C^\infty_c(S^2_+)$ and $\chi_\varepsilon\Phi\to\Phi$ in $L^2$. Also
$$M_S(\chi_\varepsilon\Phi)-\chi_\varepsilon M_S\Phi=-\chi_\varepsilon''\Phi-2\chi_\varepsilon'\partial_\psi\Phi-\cot\psi\,\chi_\varepsilon'\Phi,$$
because the $\theta$-part and $N_S$ commute with $\chi_\varepsilon$. On the support $\{\varepsilon\le\pi/2-\psi\le2\varepsilon\}$ we have $|\Phi|\le C\varepsilon^2$, $|\partial_\psi\Phi|\le C\varepsilon$, $|\chi_\varepsilon''|\le C\varepsilon^{-2}$, $|\chi_\varepsilon'|\le C\varepsilon^{-1}$, and $\cot\psi$ is bounded. So the right side is $O(1)$ on a set of area $O(\varepsilon)$, and its $L^2$ norm is $O(\varepsilon^{1/2})$. Hence $M_S(\chi_\varepsilon\Phi)\to M_S\Phi=\gamma\Phi$, and $\Phi\in D(\overline{M_S})$ with $\overline{M_S}\Phi=\gamma\Phi$.

(b) $M_S$ is symmetric on $C^\infty_c(S^2_+;\mathfrak g_{\mathbb C})$ by integration by parts: $\operatorname{ad}A_\theta$ is skew-Hermitian, and the pole is an interior point where the coordinates are only polar. It is nonnegative by Theorem 1(iii). Suppose $u\in D(M_S^*)$ and $M_S^*u=\pm iu$. For every basis element $\Phi$, $\pm i\langle u,\Phi\rangle=\langle M_S^*u,\Phi\rangle=\langle u,\overline{M_S}\Phi\rangle=\gamma\langle u,\Phi\rangle$, so $\langle u,\Phi\rangle=0$ because $\gamma$ is real. By completeness $u=0$. Both deficiency indices vanish, and $M_S$ is essentially self-adjoint [13].

(d) $\overline{M_S}$ is self-adjoint and has an orthonormal basis of eigenvectors in its domain. For $u\in D(\overline{M_S})$ this gives $\langle\overline{M_S}u,\Phi\rangle=\gamma_\Phi\langle u,\Phi\rangle$, so $\overline{M_S}$ is contained in the diagonal operator $\Lambda$ with entries $\gamma_\Phi$. $\Lambda$ is self-adjoint, so $\overline{M_S}=\Lambda$. The eigenvalues tend to infinity with finite multiplicities, so the spectrum is discrete and consists exactly of the listed eigenvalues.

The multiplicities count as follows.
- Cartan sector: for fixed $k$ the admissible $m$ are $-k,-k+2,\dots,k$, which gives $k+1$ modes, all with eigenvalue $(k+1)(k+4)$.
- $X$-sector: for fixed $k$ and $m=k-2j$, the eigenvalue is $(k+2)(k+3)+2-2(k-2j)=k^2+3k+8+4j$.
- $Y$-sector: the mode $-m$ gives the same value.

Hence each value $k^2+3k+8+4j$ contributes multiplicity $2$. The list below 30 is read off directly; `verify.py` enumerates all $k\le40$, which certifies all eigenvalues below $1812$. Since $(k+1)(k+4)\ge4$ and $k^2+3k+8\ge8$, the minimum is $4$. It is attained only at $k=0$ in the Cartan sector, with eigenfunction $\cos^2\psi\,H$.

*Real form.* The conjugation $u\mapsto-u^*$ fixes $\mathfrak{su}(2)$ and commutes with $M_S$, because the coefficients come from $\mathfrak{su}(2)$-valued fields. So each complex eigenspace is the complexification of a real eigenspace of the same dimension. $\square$

### 4.5 Proof of Corollaries 4 and 5

By §2.2, $\widehat\Delta_{0,3}(\rho^\lambda\Psi)=0$ with $\Psi\in D(\overline{M_S})\setminus\{0\}$ if and only if $\lambda(\lambda+1)$ is an eigenvalue $\gamma$ and $\Psi$ lies in its eigenspace. Solving gives $\lambda=\lambda^\pm_\gamma$. All $\gamma$ are at least $4$, so all roots are real, and the roots closest to the gap are $\lambda^\pm_4=(-1\pm\sqrt{17})/2$. Moreover $\sqrt{17}>3$ and $(1+\sqrt{17})/2>2$, so $I_1\supsetneq[-2,1]$.

For (ii), with $\beta=\lambda-2$ we compute directly in $\mathbb R^3$:
$$\Bigl(-\Delta+\frac2{y^2}-\frac2{\rho^2}\Bigr)(y^2\rho^\beta)=-y^2\rho^{\beta-2}\bigl(\beta^2+5\beta+2\bigr).$$
This vanishes when $\beta=(-5+\sqrt{17})/2$. By Theorem 3(a), the Cartan sector of $\widehat\Delta_{0,3}$ is $-\Delta+2/y^2-2/\rho^2$, because $2|\nu|^2/\rho^2=2/y^2-2/\rho^2$ and $\operatorname{ad}A$ annihilates $H$. The $X$-example is identical, with $\beta^2+5\beta-2=0$; in that case the connection term contributes $a^2/\sin^2\psi$ for $m=0$, and the total shift $+2$ is the $m=0$ case of Proposition 2. `verify.py` (Part D2) checks both solutions with the actual three-dimensional operator built from the model fields, together with two negative controls.

For (iii), $4\gamma+1=4(k+1)(k+4)+1=(2k+5)^2-8$. If this equaled $t^2$, then $(2k+5-t)(2k+5+t)=8$ with both factors of the same parity. That forces $\{2,4\}$, hence $2k+5=3$, which is impossible for $k\ge0$. In the triangular sector $4\gamma+1=4(k^2+3k+8+4j)+1=(2k+3)^2+16j+24$. Roots are integers exactly when $\sqrt{4\gamma+1}$ is an odd integer, and the listed cases below $200$ come from enumeration.

Corollary 5 is the substitution of Theorem 3(d) into the formula of [5, §4.2.1], which we take as given. Since $-\tfrac32+\tfrac{\sqrt{17}}2>0$ and $-\tfrac32-\tfrac{\sqrt{17}}2<-3$, the interval strictly contains $[-3,0]$. $\square$

## 5. Verification

`verify.py` (Python 3.13.18, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1) runs 45 checks in about 25 s and ends with `FALLOS = 0`; the output is in `verify_output.txt`. The checks fall into five groups.

- **A, the model** [exact]. KW residuals vanish at four points with rational $\rho$ for $\mathfrak r=0,\dots,3$, and symbolically for $\mathfrak r=1$. $e^{-v}=\rho y$ at $\mathfrak r=1$. Negative controls (sign of $A$ reversed, $\phi_1$ omitted) fail.
- **B, the potentials** [exact]. The $3\times3$ matrix $-\rho^2\sum_j\operatorname{ad}(\phi_j)^2$ in the basis $(H,X,Y)$, computed from the fields, equals $\mathrm{diag}(2|\nu|^2,\mu^2+|\nu|^2,\mu^2+|\nu|^2)$, and the formula for $A_\theta$ holds. The identity of Theorem 1(ii) holds for $\mathfrak r\le8$. The three constant shifts at $\mathfrak r=1$ hold, and the $\mathfrak r=0$ case reduces to $2/\cos^2\psi$. The endpoint values of Proposition 2 hold for $\mathfrak r\le10$, and constancy holds iff $\mathfrak r\le1$. Negative control: $\mathfrak r=2$ is not constant.
- **C, eigenfunctions** [exact]. The eigen-equation holds for $|m|\le5$, $j\le4$. Exact orthogonality integrals hold, and the Jacobi polynomials have exact degree, which gives completeness via Weierstrass. The functions vanish like $\cos^2\psi$ at the equator. The polynomial lift to $\mathbb R^7$ holds. Negative control: Jacobi parameter $1/2$ instead of $3/2$ fails.
- **D, spectrum and roots** [exact; two checks labelled hp]. The checks cover the lowest eigenvalues and multiplicities, the Cartan and triangular formulas, the gap and its comparison with [5], the Cartan irrationality for $k<2000$, and the integer root at $\gamma=12$. Negative control: $2$ and $6$ are not eigenvalues. The explicit 3D solutions of Corollary 4(ii) are checked against the operator built from the fields, with an exact expression evaluated to 50 digits and residual below $10^{-40}$, and two negative controls.
- **E, independent numerics** [float, declared]. A finite-volume discretization ($N=4000$) is applied to the *original* sector operators, built from the general-$\mathfrak r$ formulas of [5] rather than the simplified ones. At $\mathfrak r=1$ it reproduces the lowest three eigenvalues for $|m|\le3$ in all sectors with maximal relative error $4.9\cdot10^{-7}$. Negative control: the $\mathfrak r=2$ ground state differs from 4. This group also produces the table of Remark 6.

`verify.mpl` (Maple) repeats the exact core: the identity (ii), the three shifts, the endpoint values, the eigen-equation with an explicit Jacobi sum, orthogonality, the spectrum list, the irrationality, and the Cartesian solution. Each check has a negative control. It was written for Maple but **could not be executed** in our environment, because no Maple was available. It is provided as an independent script and should be considered unrun.

## 6. Relation to Witten's conjecture

Witten conjectures [1, 2] that suitable counts of KW solutions on $\mathbb R^3\times\mathbb R^+$ (or of Haydys–Witten flows [10, 9]) with Nahm pole and knot singularity reproduce Khovanov homology. The case $G^\vee=SU(2)$ with the knot labelled by the two-dimensional representation is $\mathfrak r=1$ with $G=SO(3)$. Defining such counts requires a Fredholm theory for the linearized operator near the knot in weighted spaces $\rho^\delta s^{\delta'}L^2$. The admissible weights are exactly those avoiding the indicial roots [4, 5, 7].

Our result pins down the Type I part of this indicial set exactly at $\mathfrak r=1$. The generic Type II part follows if one grants [5, §4.2.1]. In particular, the Type I contributions to the polyhomogeneous expansion at the knot start at the irrational exponent $(-1+\sqrt{17})/2$. This is a small, concrete input for gluing, compactness and transversality arguments in that program. It does not bear on the existence of the Floer groups or on their identification with Khovanov homology, and we make no claim in that direction.

## 7. Limitations

1. **Only the second-order operator.** We compute the spectrum of $M_S$, hence the indicial roots of $\widehat\Delta_{0,3}$. As [5, §4.1] notes, a root of $\widehat\Delta_{0,3}$ need not be a root of the first-order linearization $L$. Mazzeo and Witten expect all Type I values to be roots of $L$ but do not prove it; we do not either.
2. **Reliance on [5] for the reduction.** The decoupling of $(a_1,\phi_4)$ into $\widehat\Delta_{0,3}$ and the Type II formula (4.27) are taken from [5]. We verified the model solution and the operator $M_S$ itself, but not those reductions.
3. **Only $\mathfrak r\le1$.** Proposition 2 shows the method does not extend directly. For $\mathfrak r\ge2$ we offer only uncertified numerics (Remark 6).
4. **Untwisted equations only.** The twisted equations of Dimakis [8] and the $\theta$-KW/Haydys–Witten setting of Bleher [9] have different model solutions, which we did not treat.
5. **Type II$'$ roots** are those of [5, Prop. 4.3] and are not recomputed.
6. **Novelty** is asserted on the basis of the literature search in `sources.md`. We cannot exclude an unpublished or overlooked computation of the same spectrum. The computation is elementary once the identity $2|\nu|^2=2/\cos^2\psi-2$ is observed.
7. **The Maple companion is unrun** (see §5).

## References

[1] E. Witten, Fivebranes and knots, Quantum Topol. 3 (2012) 1–137. https://arxiv.org/abs/1101.3216

[2] E. Witten, Khovanov homology and gauge theory, in: Proceedings of the Freedman Fest, Geom. Topol. Monogr. 18 (2012) 291–308. https://arxiv.org/abs/1108.3103

[3] D. Gaiotto, E. Witten, Knot invariants from four-dimensional gauge theory, Adv. Theor. Math. Phys. 16 (2012) 935–1086. https://arxiv.org/abs/1106.4789

[4] R. Mazzeo, E. Witten, The Nahm pole boundary condition, in: The Influence of Solomon Lefschetz in Geometry and Topology, Contemp. Math. 621, Amer. Math. Soc., 2014. https://arxiv.org/abs/1311.3167

[5] R. Mazzeo, E. Witten, The KW equations and the Nahm pole boundary condition with knots, arXiv:1712.00835 (v2, 2018). https://arxiv.org/abs/1712.00835

[6] S. He, R. Mazzeo, The extended Bogomolny equations and generalized Nahm pole boundary condition, Geom. Topol. 23 (2019), no. 5. https://arxiv.org/abs/1710.10645

[7] S. He, R. Mazzeo, The extended Bogomolny equations with generalized Nahm pole boundary conditions, II, arXiv:1806.06314. https://arxiv.org/abs/1806.06314

[8] P. Dimakis, Model knot solutions for the twisted Bogomolny equations, arXiv:2204.06617. https://arxiv.org/abs/2204.06617

[9] M. Bleher, A family of instanton-invariants for four-manifolds and their relation to Khovanov homology, SIGMA 22 (2026) 028. https://arxiv.org/abs/2412.13285

[10] A. Haydys, Fukaya–Seidel category and gauge theory, J. Symplectic Geom. 13 (2015) 151–207. https://arxiv.org/abs/1010.2353

[11] A. Kapustin, E. Witten, Electric-magnetic duality and the geometric Langlands program, Commun. Number Theory Phys. 1 (2007) 1–236. https://arxiv.org/abs/hep-th/0604151

[12] R. Mazzeo, Elliptic theory of differential edge operators I, Comm. Partial Differential Equations 16 (1991) 1615–1664. https://doi.org/10.1080/03605309108820815

[13] K. Schmüdgen, Unbounded Self-adjoint Operators on Hilbert Space, Grad. Texts in Math. 265, Springer, 2012 (deficiency indices and essential self-adjointness). https://doi.org/10.1007/978-94-007-4753-1

[14] G. Szegő, Orthogonal Polynomials, AMS Colloq. Publ. 23, 4th ed., 1975 (Jacobi polynomials, Ch. IV). https://bookstore.ams.org/coll-23

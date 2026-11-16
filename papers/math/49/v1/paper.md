# Global rigidity of the Klein-symmetric Haydys–Witten sector on the round three-sphere, and the complete $SU(2)\times SU(2)$ flow category at the Anderson–Henningson fold

**Abstract.**

We study the Haydys–Witten (HW) equations on $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends, in the sector $\mathcal C_{V_4}$ of fields invariant under $SU(2)_L\rtimes V_4$. On the round sphere they reduce to the $\mathbb C^3$-valued system $\partial_su_i+i\partial_yu_i=\bar u_j\bar u_k-r^{-2}+r^{-1}(2\bar u_i-\bar u_j-\bar u_k)$. This is a $\zeta$-instanton equation for a cubic superpotential with flat directions, so no Keller–Osserman bound for $|u|^2$ is available. We prove:

(A) Every $V_4$ trajectory in the natural class satisfies $-1/r\le{\rm Re}\,u_k\le3/r$, for every $L$ and with no energy bound. The proof, a coupled maximum principle, closes at the fixed point $(-1,3)$ of a bootstrap between two one-sided bounds.

(B) The difference $d=u_1-u_2$ satisfies $(\partial_s+i\partial_y)(d^2)=2(3/r-\bar u_3)|d|^2$. With (A) this forces $d\equiv0$. So every $V_4$ Kapustin–Witten (KW) solution and every $V_4$ HW trajectory is isotropic, for every $L$. The threshold $3/r$ is exactly what the identity needs: it is the nonlinear form of the mass $3\pi$ of the traceless operator of rStation math_25.

(C) For every $L>\pi r$ the traceless part of the $V_4$ linearization is invertible along every trajectory. So $V_4$ transversality is equivalent to isotropic transversality.

(D) Take $G=SU(2)\times SU(2)$ with its principal Nahm pole, in the sector of pairs of $V_4$ fields. For $\pi r<L<\pi r+\delta$ the complete flow category has four objects in gradings $2,1,1,0$ and four index-one arrows. The space $\widehat{\mathcal M}(k_{++},k_{--})\cong\mathbb R$ compactifies to an interval whose two ends are the broken trajectories. No object or trajectory escapes the local neighbourhood of math_25, Theorem C. All moduli spaces are cut out transversally, $d^2=0$ over $\mathbb Z$, and the Cohen–Jones–Segal realization is contractible. For every $L>\pi r$ the compactified moduli spaces are compact.

We use the global isotropic theory of a companion preprint. The triaxial case, with non-isotropic objects, remains open.

verify.py: 61 checks, FALLOS = 0.

---

## 1. Introduction and results

### 1.1 Background and goal

A Haydys–Witten flow category has Kapustin–Witten (KW) solutions as objects and HW trajectories as morphisms. Building it means classifying objects (S1), proving transversality (S2), compactness (S3) and gluing (S4), and then choosing framings (S5) and a realization (S6) [CJS, LS]. On the Anderson–Henningson (AH) geometry $\mathbb R_s\times S^3_r\times(0,L)$ with Nahm poles at both ends [He, AH], our accepted papers treat the fold $L=\pi r$ *locally*:

* the AH instanton in the isotropic class [R24];
* the $V_4$ (Klein-symmetric) class on triaxial spheres, including a product instance, Theorem C, with four objects and a one-dimensional moduli space with two broken ends [R25];
* the complete linearization [R30], the five-dimensional centre manifold and the non-isotropic three-sphere [R31];
* symmetry breaking [R32], framed models [R33], and isolation and local compactness [R34].

The companion preprint [R-hw32] made the isotropic sector *global*. It proves a Keller–Osserman bound, a boundary blow-up classification, global compactness and global uniqueness near the fold. In the isotropic sector, however, the complete category has two objects and one arrow, and its realization is trivial.

The task addressed here is to globalize a sector in which the local category has more structure. The natural candidate is the $V_4$ sector of [R25], where the HW equations become a $\mathbb C^3$-valued $\zeta$-instanton equation, and its product version for $SU(2)\times SU(2)$, which is [R25, Theorem C].

**The obstacle.** The cubic part $u_1u_2u_3$ of the superpotential has flat directions: its gradient vanishes on the coordinate axes. Along them the equation is linear. So $\Delta|u|^2$ is not bounded below by $c|u|^4$, and the Keller–Osserman barrier of [R-hw32] has no vector analogue. Interior blow-up limits can be nonzero constants such as $(\lambda,0,0)$ (Remark 7.1). The route of [R-hw32] therefore does not extend directly.

**What we do instead.** On the round sphere we find two exact structures. The first is a maximum principle for the *real parts* ${\rm Re}\,u_k$; these satisfy algebraic second-order identities that do not involve ${\rm Im}\,u_1$ (Lemma 2.2). The second is a homogeneous equation for the traceless differences, with a *quadratic* integral identity (Lemma 4.1). The first gives the sharp two-sided bound $-1/r\le{\rm Re}\,u_k\le3/r$, which is exactly the bound the second needs. Together they show that the $V_4$ sector *collapses globally* onto the isotropic sector. Then [R-hw32] applies, and the product sector inherits a complete flow category with genuine content.

### 1.2 Setting

**The $V_4$ class.** Let $\sigma^i$ be a left-invariant orthonormal coframe on $S^3_r$ and $T_i=-\frac i2\sigma_i$, as in [R25, §3]. The class $\mathcal C_{V_4}$ consists of the fields
$$A=\textstyle\sum_ia_i(s,y)T_i\sigma^i,\qquad\varphi=\sum_ib_i(s,y)T_i\sigma^i,\qquad A_s=A_y=0 .$$
On the round sphere the Milnor constants are $c_i=2/r$. With $\beta=1/r$ and
$$u_i=\beta-(a_i+ib_i)=p_i+iq_i,$$
[R25, Theorem A and (3.2)] shows that the HW equations in $\mathcal C_{V_4}$ are equivalent to
$$\partial_su_i+i\partial_yu_i=\overline{\partial_i\mathcal W(u)},\qquad \mathcal W(u)=u_1u_2u_3-\beta^2\textstyle\sum_iu_i+\beta\big(\sum_iu_i^2-\sum_{i<j}u_iu_j\big). \tag{1.1}$$
Explicitly,
$$\partial_i\mathcal W=u_ju_k-\beta^2+\beta(2u_i-u_j-u_k),$$
with $(i,j,k)$ a permutation of $(1,2,3)$ (verify.py §1.1–1.2). On the diagonal $u_1=u_2=u_3=u$ this is the isotropic equation $\partial_su+i\partial_yu=\bar u^2-r^{-2}$ of [R24, R-hw32] (verify.py §1.3). The Nahm pole is $u_i\sim-i/y$ at $y=0$ and $u_i\sim-i/(y-L)$ at $y=L$.

We write $2\bar\partial=\partial_s+i\partial_y$, $2\partial=\partial_s-i\partial_y$ and $\Delta=\partial_s^2+\partial_y^2=4\partial\bar\partial$. The scaling $(s,y,u)\mapsto(s/r,y/r,ru)$ reduces everything to $r=1$, so $\beta=1$. **From §2 on, $r=1$** except in statements.

**Rescaled form and function spaces [R25, §4].** Put $y=L\tau$, $s=L\varsigma$, $v=Lu$, $v_0=-i\pi\cot\pi\tau$ and $v=v_0\mathbf 1+w$. Then (1.1) becomes
$$\partial_\varsigma w=\mathcal L^Vw+B_\beta w+\mathcal Q(w)-\nu\mathbf 1,\qquad \nu=L^2/r^2-\pi^2, \tag{1.2}$$
on $X=L^2((0,1);\mathbb C^3)$ with $\langle f,g\rangle={\rm Re}\int\bar f\cdot g$. Here:

* $\mathcal L^V$ is the operator of [R25, §4];
* $(B_\beta w)_i=(L/r-\pi)(3\bar w_i-\sum_j\bar w_j)$ is bounded and vanishes on $\mathbb C\mathbf 1$;
* $\mathcal Q(w)_i=\bar w_j\bar w_k$.

Let $Z=D(\mathcal L^V)$ carry the graph norm. We import:

* **(V1)** [R25, Prop. 4.1, Cor. 4.2]: $\mathcal L^V$ is self-adjoint with compact resolvent; it preserves $\mathbb C^3=\mathbb C\mathbf 1\oplus\mathbb C^3_0$; $Z\hookrightarrow C^0([0,1];\mathbb C^3)$ compactly; and $|w(\tau)|\le C_Z\|w\|_Z\min(\tau,1-\tau)^{1/2}$.
* **(V2)** [R25, Lemma 5.5]: distinct configurations in $\mathcal C_{V_4}$ with $w\in Z$ are gauge inequivalent.

**The trajectory class.** A *$V_4$ trajectory at length $L$* is a map $w\in C^0(\mathbb R;Z)\cap C^1(\mathbb R;X)$ that solves (1.2) for every $\varsigma$ and has limits $w_{\pm\infty}$ in $Z$ as $\varsigma\to\pm\infty$. We write $\mathcal T^V_L$ for the set of them. Constant trajectories are $V_4$ KW solutions (objects). An element of $\mathcal T^V_L$ with $w=\omega\mathbf 1$ is exactly an element $\omega$ of the isotropic class $\mathcal T_L$ of [R-hw32, §1.2], because $\mathcal L^V(\omega\mathbf 1)=(\mathcal L\omega)\mathbf 1$, $B_\beta\mathbf 1=0$ and $\mathcal Q(\omega\mathbf 1)=\bar\omega^2\mathbf 1$. As in [R-hw32] we impose no smallness and no energy bound.

**Imported isotropic theory.** From [R24] and [R-hw32] we use:

* the classification (F2) of isotropic KW solutions: none for $L<\pi r$, the degenerate $k_0$ for $L=\pi r$, and the nondegenerate pair $k_\pm$ for $L>\pi r$ (due to [He, AH]; [R24, Prop. B]);
* the transversality (F5) of the AH instanton $\mathfrak u$ near the fold [R24, Thm. D];
* Theorems A–D and Lemmas 5.1–5.2 of [R-hw32]: global exclusion, the energy identity, universal estimates, compactness for every $L>\pi r$, and global uniqueness of $\mathfrak u$ for $\pi r<L<\pi r+\delta$.

### 1.3 Results

**Theorem A (two-sided a priori bound).** Let $L>0$, $w\in\mathcal T^V_L$, and let $u$ be the corresponding solution of (1.1). Then
$$-\frac1r\ \le\ {\rm Re}\,u_k(s,y)\ \le\ \frac3r\qquad\text{for }k=1,2,3\text{ and all }(s,y)\in\mathbb R\times(0,L).$$
Equivalently, the connection coefficients satisfy $|a_k|\le2/r=c_k$. No energy bound is needed.

**Theorem B (global rigidity).** Let $L>0$. Every $w\in\mathcal T^V_L$ is isotropic: $u_1=u_2=u_3$. Consequently:
1. the $V_4$ KW solutions with $w\in Z$ are none for $L<\pi r$, only $k_0$ for $L=\pi r$, and exactly $k_\pm$ for $L>\pi r$;
2. $\mathcal T^V_L=\mathcal T_L\cdot\mathbf 1$, so Theorems A–D of [R-hw32] hold verbatim in $\mathcal C_{V_4}$. In particular, for every $L>\pi r$ every nonconstant $V_4$ trajectory runs from $k_+$ to $k_-$ with energy $6\pi^2r^3L^{-2}\Delta\mathcal A$, and these trajectories form a compact space modulo translation. For $\pi r<L<\pi r+\delta$ the only nonconstant $V_4$ trajectory, up to translation, is the AH instanton $\mathfrak u$.

**Theorem C ($V_4$ transversality from isotropic transversality, all $L$).** Let $L>\pi r$.
1. $k_\pm$ are nondegenerate in $\mathcal C_{V_4}$.
2. For every nonconstant $w=\omega\mathbf 1\in\mathcal T^V_L$, the $V_4$ linearization $D^V_w$ is conjugate to $D^{\rm iso}_\omega\oplus D^T_\omega\oplus D^T_\omega$. Here $D^{\rm iso}_\omega$ is the isotropic linearization and $D^T_\omega$ is an invertible operator. Hence $D^V_w$ is Fredholm iff $D^{\rm iso}_\omega$ is, with the same kernel, cokernel and index.
3. For $\pi r<L<\pi r+\delta$, $D^V_{\mathfrak u}$ is onto with index $1$.

Item 3 is [R25, Cor. B′]. Item 1 and the reduction in item 2 hold for every $L>\pi r$; for $L\ge\pi r+\delta$ they reduce $V_4$ transversality to the open isotropic question.

**Theorem D (the complete $SU(2)\times SU(2)$ flow category).** Let $G=SU(2)\times SU(2)$ with its principal Nahm pole $(\rho_0,\rho_0)$. Let $\mathcal C_2$ be the class of pairs of $\mathcal C_{V_4}$ fields [R25, §7.2], and $\mathcal T^{(2)}_L=\mathcal T^V_L\times\mathcal T^V_L$ its trajectory class. Write $k_{ab}=(k_a,k_b)$.
1. *(Objects, all $L$.)* The $\mathcal C_2$ objects are: none for $L<\pi r$; $k_{00}$ for $L=\pi r$; and exactly $k_{++},k_{+-},k_{-+},k_{--}$ for $L>\pi r$. These are pairwise gauge inequivalent and nondegenerate, with gradings $2,1,1,0$.
2. *(Global compactness, all $L>\pi r$.)* Let $\mathcal M=\mathcal M(k_+,k_-)$ be the compact isotropic moduli space of [R-hw32, Thm. C]. The nonempty spaces of unparametrized nonconstant trajectories are:
   * $\widehat{\mathcal M}(k_{++},k_{+-})\cong\widehat{\mathcal M}(k_{++},k_{-+})\cong\widehat{\mathcal M}(k_{+-},k_{--})\cong\widehat{\mathcal M}(k_{-+},k_{--})\cong\mathcal M$;
   * $\widehat{\mathcal M}(k_{++},k_{--})\cong\mathcal M\times\mathcal M\times\mathbb R$.

   All others are empty, including $\widehat{\mathcal M}(k_{+-},k_{-+})$. Every sequence in $\widehat{\mathcal M}(k_{++},k_{--})$ has a subsequence that converges either in $\widehat{\mathcal M}(k_{++},k_{--})$ or to a broken trajectory through $k_{+-}$ or through $k_{-+}$, in the sense of Definition 6.2, with energy additivity. So the compactification is $\mathcal M\times\mathcal M\times[-\infty,\infty]$.
3. *(Near the fold.)* For $\pi r<L<\pi r+\delta$:
   * the four spaces in item 2 that are copies of $\mathcal M$ are single points;
   * $\widehat{\mathcal M}(k_{++},k_{--})=\{[(\mathfrak u,\mathfrak u(\cdot+T))]:T\in\mathbb R\}\cong\mathbb R$, and its compactification is $[-\infty,\infty]$ with boundary exactly
   $$\widehat{\mathcal M}(k_{++},k_{+-})\times\widehat{\mathcal M}(k_{+-},k_{--})\ \sqcup\ \widehat{\mathcal M}(k_{++},k_{-+})\times\widehat{\mathcal M}(k_{-+},k_{--});$$
   * every element is cut out transversally in $\mathcal C_2$, with index equal to the grading difference.

   These are *all* $\mathcal C_2$ objects and trajectories. So the local category of [R25, Theorem C] at the round metric is the complete one.
4. *(Realization.)* For $\pi r<L<\pi r+\delta$ this is a compact framed flow category in the sense of [LS, §3]. Its cellular complex is
$$\partial k_{++}=k_{-+}-k_{+-},\qquad\partial k_{+-}=\partial k_{-+}=k_{--},\qquad\partial k_{--}=0$$
(Koszul signs, $\partial(x\otimes y)=\partial x\otimes y+(-1)^{|x|}x\otimes\partial y$). This complex is acyclic over $\mathbb Z$, and the Cohen–Jones–Segal realization is contractible for every coherent framing. For $L<\pi r$ the category is empty.

**What is new.**
* *Theorem A* is a global a priori estimate for a vector-valued $\zeta$-instanton system with a degenerate (flat-direction) cubic, where Keller–Osserman fails. Its proof combines two one-sided maximum principles whose thresholds feed each other; the bootstrap closes exactly at $(-1,3)$ (Lemmas 3.2–3.4, verify.py §§3–5).
* *Lemma 4.1 and Theorem B.* The homogeneous traceless equation and its quadratic integral identity are, to our knowledge, new. They are the nonlinear counterpart of [R25, Prop. 4.1(c)], where the mass $3\pi$ excluded traceless Jacobi fields at the fold only. Theorem B removes the restriction to a neighbourhood $\mathcal U$ from [R25, Cor. B′] and from [R25, §10] ("trajectories that leave $\mathcal U$ are not classified"), at the round metric.
* *Theorem C* extends nondegeneracy in $\mathcal C_{V_4}$ from the fold window [R25] to all $L>\pi r$.
* *Theorem D* is the first complete Haydys–Witten flow category in our series with a nonempty one-dimensional moduli space. Its boundary consists of broken trajectories, and $d^2=0$ holds globally, not only for local moduli spaces.

**What is not claimed.**
* *Triaxial spheres.* There the objects are non-isotropic [R25, Thm. B] and the traceless equation is inhomogeneous (verify.py §6.4). Neither Theorem B nor a vector Keller–Osserman bound is available; see §7.
* The full gauge theory, where the AH arrow is obstructed and the local homotopy type is $S^1\vee S^4$ [R30, R31, R33]. That structure lives on non-left-invariant configurations, which the $V_4$ class does not contain.
* Transversality or counts for $L\ge\pi r+\delta$; Theorem C reduces these to the isotropic question left open in [R-hw32, Rem. 8.3].
* A coupled (non-product) concatenation.

## 2. Preliminaries

**Lemma 2.1 (properties of $\mathcal T^V_L$).** Let $w\in\mathcal T^V_L$ and $M_w=\sup_\varsigma\|w(\varsigma)\|_Z$.
* (a) $M_w<\infty$, and $u$ is a smooth solution of (1.1) on $\mathbb R\times(0,L)$.
* (b) For all $s$, with $C=C_ZM_wL^{-3/2}$:
  * $|p_k(s,y)|\le C\min(y,L-y)^{1/2}$;
  * $|u_i-u_j|^2\le4C^2\min(y,L-y)$;
  * $|u_k(s,y)|\le\pi\,\big(L\sin(\pi y/L)\big)^{-1}+C_ZM_wL^{-1}$.
* (c) $u(s,\cdot)\to u_{\pm\infty}$ uniformly on compact subsets of $(0,L)$ as $s\to\pm\infty$, where $u_{\pm\infty}$ corresponds to $w_{\pm\infty}$.
* (d) $w_{\pm\infty}$ are static solutions: $\mathcal G(w_{\pm\infty})=0$, where $\mathcal G$ is the right side of (1.2). Hence the constant maps $w\equiv w_{\pm\infty}$ lie in $\mathcal T^V_L$.

*Proof.* (a) A continuous map into $Z$ with limits is bounded. Since $\mathcal L^V$ is the maximal operator, (1.2) holds in the sense of distributions. Moreover $u$ is locally bounded by (V1), so $\bar\partial u\in L^\infty_{\rm loc}$, and the bootstrap for $\bar\partial$ [Ve, MS] gives smoothness, as in [R-hw32, Lemma 2.1].

(b) We have $u_k=L^{-1}(v_0+w_k)(s/L,y/L)$, and $v_0$ is imaginary. So $p_k=L^{-1}{\rm Re}\,w_k$, $u_i-u_j=L^{-1}(w_i-w_j)$ and $|v_0|=\pi|\cot\pi\tau|$. Apply (V1).

(c) Since $u(s,\cdot)-u_{\pm\infty}=L^{-1}(w(s/L)-w_{\pm\infty})(\cdot/L)$, this follows from $Z\hookrightarrow C^0$; the convergence is even uniform on $(0,L)$.

(d) If $\mathcal G(w_+)\ne0$, then $\|w(\varsigma+1)-w(\varsigma)\|_X=\|\int_\varsigma^{\varsigma+1}\mathcal G(w)\|_X\to\|\mathcal G(w_+)\|_X>0$, because $\mathcal G:Z\to X$ is continuous. This contradicts convergence. ∎

**Lemma 2.2 (second-order identities).** Smooth solutions of (1.1) satisfy
$$\Delta u_i=\textstyle\sum_j\overline{\partial_i\partial_j\mathcal W}\;\partial_j\mathcal W,$$
and, with $r=1$, $X=p_2-1$ and $Y=p_3-1$,
$$\Delta p_1=F_1(u):=(p_1-1)(X^2+Y^2+4)+6XY+p_1(q_2^2+q_3^2)-(q_2-q_3)^2. \tag{2.1}$$
The formulas for $p_2,p_3$ follow by permuting indices. $F_1$ does not involve $q_1$. On the diagonal, $F_1=2(|u|^2-1)p$, which is [R-hw32, Lemma 4.1].

*Proof.* Write $2\bar\partial u_i=\overline{\partial_i\mathcal W}+R_i$, where $R_i=0$ on solutions. Since $\partial\bar f=\overline{\bar\partial f}$ and $\mathcal W$ is holomorphic,
$$\Delta u_i=2\partial\,\overline{\partial_i\mathcal W}+2\partial R_i=\textstyle\sum_j\overline{\partial_{ij}\mathcal W}\,\big(\partial_j\mathcal W+\bar R_j\big)+2\partial R_i .$$
Taking real parts gives (2.1). verify.py §2.1 checks the identity exactly, residual terms included, with a negative control (§2.2). §2.3–2.6 check the closed form of $F_1$, its independence of $q_1$, the diagonal case and the homogeneity $F_1(\beta;p,q)=\beta^3F_1(1;p/\beta,q/\beta)$. ∎

## 3. Proof of Theorem A

Fix $w\in\mathcal T^V_L$ (with $r=1$) and put
$$b:=\sup_{k,s,y}p_k,\qquad a:=\max\big(0,-\inf_{k,s,y}p_k\big),\qquad c:=a+1,\qquad M:=b-1 .$$
These are finite by Lemma 2.1(b) and (c).

**Lemma 3.1 (extremal points).** Suppose $b>0$. Then there are $k$, a smooth solution $\tilde u\in\{u,u_{+\infty},u_{-\infty}\}$ (the last two constant in $s$) and a point $(s_*,y_*)$ with the following properties:
* $\tilde p_k(s_*,y_*)=b$;
* $\Delta\tilde p_k(s_*,y_*)\le0$;
* $-a\le\tilde p_j(s_*,y_*)\le b$ for all $j$.

The same holds for the infimum when $a>0$, with $\tilde p_k=-a$ and $\Delta\tilde p_k\ge0$.

*Proof.* By Lemma 2.1(b), $p_k\to0$ uniformly as $y\to0$ or $y\to L$. So $b$ is approached on a set $\{y'\le y\le L-y'\}$. If it is attained, take $\tilde u=u$; an interior maximum has $\Delta p_k\le0$. Otherwise it is approached along $|s_n|\to\infty$. By Lemma 2.1(c), the static limit then attains $b$ at an interior point $y_*$, and there $\Delta\tilde p_k=\tilde p_k''(y_*)\le0$. In both cases the values $\tilde p_j(s_*,y_*)$ are limits of values of $p_j$, so they lie in $[-a,b]$. ∎

In both cases $\Delta\tilde p_k=F_k(\tilde u)$ by Lemma 2.2, since $\tilde u$ solves (1.1).

**Lemma 3.2 (lower bound).** Suppose $a>0$. Then:
1. $a<2$;
2. if $a>1$, then $M>c$ and $(2-a)M^2\ge2c$.

*Proof.* At the point of Lemma 3.1, with $k=1$ after relabelling, $p_1=-a$ and $F_1\ge0$. Here $X,Y\in[-c,M]$. The exact identity
$$F_1-\big[(2-a)(X^2+Y^2)-4c\big]=-3(X-Y)^2-a(q_2^2+q_3^2)-(q_2-q_3)^2\le0$$
holds (verify.py §3.1). Hence $0\le F_1\le(2-a)(X^2+Y^2)-4c$.

1. If $a\ge2$, the right side is at most $-4c<0$, a contradiction.
2. Let $1<a<2$ and $R=\max(c,|M|)$, so $|X|,|Y|\le R$. Then $0\le2(2-a)R^2-4c$. If $R=c$, the right side equals $2ca(1-a)<0$ (verify.py §3.2), a contradiction. So $|M|>c$. Since $M\ge-c$, we get $M>c$, and then $0\le2(2-a)M^2-4c$. ∎

**Lemma 3.3 (upper bound).** Suppose $a<2$ and $b\ge2$. Then $M^2+c^2-6c+4\le0$.

*Proof.* At the point of Lemma 3.1, with $k=1$, $p_1=b=M+1$ and $F_1\le0$, with $X,Y\in[-c,M]$, $M\ge1$ and $1\le c<3$. By verify.py §4.1–4.2,
$$F_1=G(X,Y)+(M-1)(q_2^2+q_3^2)+(q_2+q_3)^2,\qquad G=M(X^2+Y^2+4)+6XY .$$
So $G(X,Y)\le0$ for some $(X,Y)$ in the box $B=[-c,M]^2$. We show that $\min_BG>0$ whenever $M^2+c^2-6c+4>0$.

* *Case $M\ge3$.* The quadratic part of $G$ is positive semidefinite, so $G\ge4M>0$ (verify.py §4.9).
* *Case $1\le M<3$.* The Hessian of $G$ is indefinite, so the minimum is on $\partial B$. By the symmetry $X\leftrightarrow Y$ it suffices to treat two edges.
  * On $X=M$: $G=M(Y^2+6Y+M^2+4)$. Its vertex is at $Y=-3<-c$, so $G$ is increasing on $[-c,M]$. Its minimum is $G(M,-c)=M(M^2+c^2-6c+4)>0$ (verify.py §4.3–4.4).
  * On $X=-c$: $G$ is convex in $Y$ with vertex $3c/M>0$.
    * If $3c/M\le M$, the vertex value is $[M^2(c^2+4)-9c^2]/M\ge3c(c^2-3c+4)/M>0$, because the discriminant of $c^2-3c+4$ is $-7$.
    * Otherwise the minimum on this edge is at the corner $(-c,M)$, which is the case already treated (verify.py §4.5–4.8).

So $G>0$ on $B$, a contradiction. ∎

**Lemma 3.4 (closing the bootstrap).** $a\le1$ and $b\le3$.

*Proof.* By Lemma 3.2(1), $a<2$.

*$a\le1$.* Suppose $1<a<2$, i.e. $2<c<3$. By Lemma 3.2(2), $M>c>2$, so $b>3$, and $M^2\ge2c/(2-a)=2c/(3-c)$. Lemma 3.3 applies and gives $M^2\le6c-c^2-4$. Hence $2c\le(3-c)(6c-c^2-4)$, i.e.
$$(c-1)(c-2)(c-6)\ge0$$
(verify.py §5.1). This is false for $c\in(2,3)$ (§5.2). So $a\le1$.

*$b\le3$.* If $b\ge2$, Lemma 3.3 gives $M^2\le6c-c^2-4=4-(c-2)(c-4)\le4$ for $c\le2$ (§5.3). So $M\le2$, i.e. $b\le3$. If $b<2$ there is nothing to prove. ∎

**Proof of Theorem A.** Lemma 3.4 gives $-1\le p_k\le3$ at $r=1$. Scaling (verify.py §2.6) gives $-1/r\le{\rm Re}\,u_k\le3/r$. Finally $a_k=\beta-p_k\in[-2/r,2/r]$. ∎

*Remark 3.5 (sharpness of the method).* The two extremal configurations $(p_1,p_2,p_3)=(3,3,-1)$ and $(-1,3,3)$, with $q_2=q_3=0$, give $F_1=0$ (verify.py §5.4). So $(a,b)=(1,3)$ is exactly the fixed point of the bootstrap.

Without the coupling, each one-sided principle is weaker:
* the minimum principle alone gives only $p\ge-2$;
* the maximum principle alone gives only $p\le1+\sqrt5$.

The controls §5.5–5.6 confirm that the pointwise inequalities fail just beyond the thresholds when the other bound is dropped. We do not claim that the constants are optimal for solutions; on $k_\pm$ one has $0<|p|<1$ (verify.py §10.2, numerical).

## 4. Proof of Theorem B

**Lemma 4.1 (traceless identity).** Let $d=u_1-u_2$. On solutions of (1.1),
$$2\bar\partial d=(3\beta-\bar u_3)\,\bar d,\qquad 2\bar\partial(d^2)=2(3\beta-\bar u_3)|d|^2, \tag{4.1}$$
and cyclically for $u_2-u_3$ (with $\bar u_1$) and $u_3-u_1$ (with $\bar u_2$).

*Proof.* We have
$$\partial_1\mathcal W-\partial_2\mathcal W=u_3(u_2-u_1)+\beta(3u_1-3u_2)=(3\beta-u_3)\,d .$$
Conjugating gives the first identity. The second follows from $2\bar\partial(d^2)=2d\cdot2\bar\partial d$. Both are checked exactly in verify.py §6.1–6.2. The control §6.4 shows that for a triaxial metric $\partial_1\mathcal W-\partial_2\mathcal W$ acquires the constant $-(m_1-m_2)=(c_1-c_2)(c_1+c_2-c_3)\ne0$, so (4.1) is special to the round sphere. ∎

**Proposition 4.2 (static rigidity).** Every static $w\in Z$ with $\mathcal G(w)=0$ is isotropic.

*Proof.* The constant map $w$ lies in $\mathcal T^V_L$, so Theorem A gives $p_3\le3$ (with $r=1$). For static $u$, (4.1) reads $i(d^2)'=2(3-\bar u_3)|d|^2$ on $(0,L)$. Integrate over $[\varepsilon,L-\varepsilon]$ and let $\varepsilon\to0$. By Lemma 2.1(b) we have $|d|^2\le Cy$ and $|3-\bar u_3|\,|d|^2\le C$, so the boundary terms vanish and dominated convergence applies (verify.py §7.1–7.2). Hence
$$\int_0^L(3-\bar u_3)|d|^2\,dy=0,\qquad\text{so}\qquad\int_0^L(3-p_3)|d|^2\,dy=0 .$$
The integrand is $\ge0$, so $d=0$ on $\{p_3<3\}$. This set contains $(0,y_0)$, because $p_3\to0$ there. Now $d$ solves the linear ODE $d'=-i(3-\bar u_3)\bar d$, whose coefficient is continuous on $(0,L)$, so $d\equiv0$. The same argument applies to the other two differences. ∎

**Proposition 4.3 (dynamic rigidity).** Every $w\in\mathcal T^V_L$ is isotropic.

*Proof.* By Lemma 2.1(d) and Proposition 4.2, the limits $w_{\pm\infty}$ are isotropic. Put $d=u_1-u_2$ and $g(s)={\rm Re}\int_0^Ld(s,y)^2\,dy$.

*$g$ is monotone.* Integrate (4.1) over $[s_1,s_2]\times[\varepsilon,L-\varepsilon]$:
$$\int_\varepsilon^{L-\varepsilon}\big(d^2(s_2,\cdot)-d^2(s_1,\cdot)\big)dy+i\int_{s_1}^{s_2}\big[d^2\big]_{y=\varepsilon}^{y=L-\varepsilon}ds=2\iint(3-\bar u_3)|d|^2 .$$
The bounds of Lemma 2.1(b) are uniform in $s$. So, as $\varepsilon\to0$, the boundary term vanishes and dominated convergence applies. Taking real parts,
$$g(s_2)-g(s_1)=2\int_{s_1}^{s_2}\!\!\int_0^L(3-p_3)|d|^2\,dy\,ds\ \ge0$$
by Theorem A.

*$g$ vanishes.* As $s\to\pm\infty$, $w(s)\to w_{\pm\infty}$ in $X$, so $g(s)\to{\rm Re}\int d_{\pm\infty}^2=0$. A nondecreasing function with zero limits at both ends is identically $0$. Therefore $\iint(3-p_3)|d|^2=0$, and $d=0$ on the open set $\{p_3<3\}$. This set contains $\mathbb R\times(0,y_0)$, by the uniform bound $|p_3|\le Cy^{1/2}$.

*Unique continuation.* $d$ solves the first-order elliptic equation $2\bar\partial d=(3-\bar u_3)\bar d$ with smooth coefficient. By the Carleman similarity principle [MS, §2.3], $d=e^{\phi}h$ locally, with $\phi$ continuous and $h$ holomorphic. So the zero set of a nontrivial solution has empty interior. Since the strip is connected, $d\equiv0$. The other two differences are treated in the same way. ∎

**Proof of Theorem B.** Proposition 4.3 shows that $\mathcal T^V_L=\mathcal T_L\cdot\mathbf 1$ (§1.2). Item 1 is Proposition 4.2 together with (F2) and (V2). Item 2 is [R-hw32, Theorems A–D] applied to $\omega$, with $w=\omega\mathbf 1$. The configuration, and hence its energy $E=\int|\partial_sA|^2+|\partial_s\varphi|^2$, is literally the same. ∎

## 5. Proof of Theorem C

Let $\omega\in\mathcal T_L$ and $w=\omega\mathbf 1$. Linearizing (1.2) at $w$ gives the operator $h\mapsto\mathcal L^Vh+B_\beta h+D\mathcal Q(w)h$. On $h=\eta\mathbf 1$ it acts as the isotropic linearization $\eta\mapsto\mathcal L\eta+2\bar\omega\bar\eta$. On $\mathbb C^3_0$ it acts componentwise as
$$T(\varsigma)\eta=-i\eta'+(3\hat\beta-\bar v(\varsigma))\bar\eta,\qquad\hat\beta=L/r,\quad v=v_0+\omega(\varsigma)$$
(verify.py §6.6–6.8). At the fold ($\hat\beta=\pi$, $v=v_0$) this is $\mathcal L_T$ of [R25, Prop. 4.1] (§6.9). Since the splitting $\mathbb C\mathbf 1\oplus\mathbb C^3_0$ is constant, $D^V_w$ is the direct sum of $D^{\rm iso}_\omega=\partial_\varsigma-(\mathcal L+2\bar\omega\,\overline{\cdot}\,)$ and two copies of $D^T_\omega=\partial_\varsigma-T(\varsigma)$. These act on $W=W^{1,2}(\mathbb R;X_T)\cap L^2(\mathbb R;Z_T)\to L^2(\mathbb R;X_T)$, where $X_T=L^2((0,1);\mathbb C)$ and $Z_T=D(\mathcal L_T)$.

**Proposition 5.1 (static traceless operator).** For $L>\pi r$ the operator $T_\pm:=T$ at $k_\pm$ is self-adjoint on $Z_T$ with compact resolvent, and it is injective, hence invertible.

*Proof.* We have $T_\pm-\mathcal L_T=3(\hat\beta-\pi)\overline{\cdot}-\bar w_\pm\overline{\cdot}$, which is bounded and symmetric because $w_\pm\in C^0$. So [R25, Prop. 4.1(a)] and [Ka, V.4.3] give self-adjointness and compact resolvent.

Let $T_\pm\eta=0$ with $\eta\in Z_T$. Then $\eta$ is smooth on $(0,1)$ and $|\eta|^2\le C\tau$. It satisfies $i(\eta^2)'=2(3\hat\beta-\bar v_\pm)|\eta|^2$, the linear version of (4.1). Integrating as in Proposition 4.2 gives $\int(3\hat\beta-{\rm Re}\,v_\pm)|\eta|^2=0$. Here ${\rm Re}\,v_\pm=Lp_\pm\le3L/r=3\hat\beta$ by Theorem A, and ${\rm Re}\,v_\pm\to0$ at the ends. So $\eta=0$ near $\tau=0$, and $\eta\equiv0$ by ODE uniqueness. ∎

*Proof of Theorem C(1).* The isotropic part is invertible by the nondegeneracy in (F2), and the traceless part by Proposition 5.1. ∎

**Proposition 5.2 (traceless operator along a trajectory).** For every nonconstant $\omega\in\mathcal T_L$ with $L>\pi r$, $D^T_\omega:W\to L^2(\mathbb R;X_T)$ is an isomorphism.

*Proof.* *Fredholm.* $T(\varsigma)=\mathcal L_T+K(\varsigma)$ with $K(\varsigma)\eta=(3(\hat\beta-\pi)-\bar\omega(\varsigma))\bar\eta$. The map $\varsigma\mapsto K(\varsigma)\in\mathcal L(Z_T,X_T)$ is $C^1$ in norm. Indeed, its derivative is $\eta\mapsto-\overline{\partial_\varsigma\omega}\,\bar\eta$, with norm at most $C_Z\|\partial_\varsigma\omega\|_X$, because $Z_T\hookrightarrow C^0$. Moreover $K(\varsigma)\to K(\pm\infty)$ in norm, because $\omega(\varsigma)\to w_\pm$ in $C^0$. The graph norms of $T(\varsigma)$ are uniformly equivalent to that of $\mathcal L_T$, and $Z_T\hookrightarrow X_T$ is compact and dense. The limits $T_\pm$ are invertible (Proposition 5.1). By the theorem of Robbin–Salamon [RS, Thm. A], $D^T_\omega$ is Fredholm.

*Kernel.* Let $D^T_\omega\eta=0$ and $g(\varsigma)={\rm Re}\int_0^1\eta^2\,d\tau$. Since $\eta\in W^{1,2}(\mathbb R;X_T)$, $g$ is absolutely continuous with $g(\pm\infty)=0$. For a.e. $\varsigma$ we have $\eta(\varsigma)\in Z_T$, and
$$g'=2{\rm Re}\int\eta\,T\eta=2{\rm Re}\big(-\tfrac i2[\eta^2]_0^1\big)+2\int(3\hat\beta-{\rm Re}\,v)|\eta|^2=2\int(3\hat\beta-{\rm Re}\,v)|\eta|^2\ \ge0 .$$
The boundary term vanishes because $|\eta|^2\le C\min(\tau,1-\tau)$ on $Z_T$ (V1), and $\eta\eta'$ is integrable. The sign is Theorem A. Hence $g\equiv0$, and $\eta=0$ a.e. on $\mathbb R\times(0,\tau_0)$. Interior elliptic regularity for $(\partial_\varsigma+i\partial_\tau)\eta=(3\hat\beta-\bar v)\bar\eta$ makes $\eta$ smooth, and the similarity principle gives $\eta\equiv0$.

*Cokernel.* The orthogonal complement of the range consists of weak solutions of $\partial_\varsigma\xi=-T(\varsigma)\xi$. These lie in $W$ by the regularity in [RS, §3] (or by difference quotients as in [R-hw32, Lemma 5.1]). For them $g'\le0$ with $g(\pm\infty)=0$, and the same argument gives $\xi=0$. ∎

*Proof of Theorem C(2)–(3).* Conjugating by the constant splitting gives $D^V_w\cong D^{\rm iso}_\omega\oplus D^T_\omega\oplus D^T_\omega$. The traceless summands are isomorphisms (Proposition 5.2), so Fredholmness, kernel, cokernel and index are those of $D^{\rm iso}_\omega$. For $\pi r<L<\pi r+\delta$, Theorem B(2) gives $\omega=\mathfrak u$ up to translation, and (F5) gives that $D^{\rm iso}_{\mathfrak u}$ is onto with index $1$. ∎

## 6. Proof of Theorem D

In $\mathcal C_2$ all brackets are componentwise, so the HW and KW equations decouple into two copies of (1.1) with the same $(r,L)$ [R25, §7.2]. The gauge group is a product, so (V2) applies in each factor. Hence $\mathcal T^{(2)}_L=\mathcal T^V_L\times\mathcal T^V_L$, and by Theorem B
$$\mathcal T^{(2)}_L=\{(\omega^1\mathbf 1,\omega^2\mathbf 1):\omega^1,\omega^2\in\mathcal T_L\}.$$

**Item 1.** Objects are pairs of objects, so Theorem B(1) applies. The linearization at $k_{ab}$ is a direct sum, invertible by Theorem C(1). The grading is the number of $+$ signs, normalized by $\mathrm{gr}(k_{--})=0$. This is the sum of the isotropic gradings with $\mathrm{gr}(k_+)-\mathrm{gr}(k_-)=1$ [R-hw32, Thm. D(3)] (verify.py §8.6).

**Item 2 (moduli spaces).** By [R-hw32, Thm. A(3)], each factor is either constant or runs $k_+\to k_-$. This gives exactly the list in Theorem D(2) (verify.py §9.2–9.3), with the identifications $[(\omega,k_-)]\mapsto[\omega]$, and so on. For $\widehat{\mathcal M}(k_{++},k_{--})$ both factors move. Normalize each factor by the action condition of [R-hw32, §6], $\mathcal A_\nu(\omega^j(\sigma_j))=\mathcal A_\nu(w_+)+\frac12\Delta\mathcal A$. The class of $(\omega^1,\omega^2)$ modulo the diagonal translation is then determined by the two normalized factors and the relative shift $T=\sigma_2-\sigma_1\in\mathbb R$. This gives $\widehat{\mathcal M}(k_{++},k_{--})\cong\mathcal M\times\mathcal M\times\mathbb R$.

**Lemma 6.1 (uniform tails).** Let $L>\pi r$. For every $\eta>0$ there is $R$ such that every normalized nonconstant $\omega\in\mathcal T_L$ satisfies $\|\omega(\sigma)-w_+\|_X\le\eta$ for $\sigma\le-R$, and $\|\omega(\sigma)-w_-\|_X\le\eta$ for $\sigma\ge R$.

*Proof.* Suppose not. Then there are normalized $\omega_n$ and $\sigma_n\to-\infty$ with $\|\omega_n(\sigma_n)-w_+\|_X\ge\eta$; the case $+\infty$ is symmetric.

*Small energy on the tail.* By [R-hw32, Thm. C], a subsequence $\omega_n\to\omega$ in $C^0_{\rm loc}(\mathbb R;X)$, with $\mathcal L\omega_n(\sigma)\rightharpoonup\mathcal L\omega(\sigma)$ weakly for each $\sigma$. As in the nontriviality step of [R-hw32, §6], $\mathcal A_\nu(\omega_n(\sigma))\to\mathcal A_\nu(\omega(\sigma))$ for each fixed $\sigma$. Given $\epsilon>0$, choose $\sigma_0$ with $\mathcal A_\nu(\omega(\sigma_0))<\mathcal A_\nu(w_+)+\epsilon$. For $n$ large, $\sigma_n+3\le\sigma_0$ and, by the energy identity [R-hw32, Lemma 3.2] and the monotonicity of the action,
$$\int_{-\infty}^{\sigma_n+3}\|\partial_\varsigma\omega_n\|_X^2=\mathcal A_\nu(\omega_n(\sigma_n+3))-\mathcal A_\nu(w_+)\le\mathcal A_\nu(\omega_n(\sigma_0))-\mathcal A_\nu(w_+)<2\epsilon .$$
So the energy of $\omega_n$ on $(-\infty,\sigma_n+3]$ tends to $0$, and so does $\mathcal A_\nu(\omega_n(\sigma_n))-\mathcal A_\nu(w_+)$.

*Contradiction.* By [R-hw32, Thm. B(3)], $\sup_\varsigma\|\omega_n(\varsigma)\|_Z\le M$ uniformly in $n$. By [R-hw32, Lemma 5.1] at $m=\sigma_n$, $\|\mathcal G_\nu(\omega_n(\sigma_n))\|_X=\|\partial_\varsigma\omega_n(\sigma_n)\|_X\to0$. By [R-hw32, Lemma 5.2(b)], a subsequence of $\omega_n(\sigma_n)$ converges in $Z$ to $w_+$ or $w_-$. Since $\mathcal A_\nu$ is continuous on $Z$ and $\mathcal A_\nu(\omega_n(\sigma_n))\to\mathcal A_\nu(w_+)<\mathcal A_\nu(w_-)$, the limit is $w_+$. This contradicts $\|\omega_n(\sigma_n)-w_+\|_X\ge\eta$. ∎

**Definition 6.2.** A sequence $[v_n]\in\widehat{\mathcal M}(k_{++},k_{--})$ *converges to the broken trajectory* $([v^1],[v^2])\in\widehat{\mathcal M}(k_{++},k_{+-})\times\widehat{\mathcal M}(k_{+-},k_{--})$ if there are representatives and shifts $\tau_n$ with $v_n\to v^1$ and $v_n(\cdot+\tau_n)\to v^2$ in $C^0_{\rm loc}(\mathbb R;X^2)$. Convergence through $k_{-+}$ is defined in the same way.

**Proof of Theorem D(2), compactness.** Let $v_n=(\omega^1_n,\omega^2_n(\cdot-T_n))$ with $\omega^j_n$ normalized. By [R-hw32, Thm. C], after passing to a subsequence, $\omega^j_n\to\omega^j\in\mathcal M$ in $C^0_{\rm loc}(\mathbb R;X)$, and either $T_n\to T\in\mathbb R$ or $T_n\to\pm\infty$.

* If $T_n\to T$, then $v_n\to(\omega^1,\omega^2(\cdot-T))$.
* If $T_n\to+\infty$ (the second factor lags behind):
  * $v_n\to(\omega^1,k_+)$ in $C^0_{\rm loc}$, because $\omega^2_n(\varsigma-T_n)\to w_+$ uniformly on compact sets by Lemma 6.1; the limit is a trajectory $k_{++}\to k_{-+}$;
  * $v_n(\cdot+T_n)=(\omega^1_n(\cdot+T_n),\omega^2_n)\to(k_-,\omega^2)$, again by Lemma 6.1; the limit is a trajectory $k_{-+}\to k_{--}$.

  This is convergence to the broken trajectory through $k_{-+}$.
* If $T_n\to-\infty$, the same argument with the roles of the factors exchanged gives convergence through $k_{+-}$.

The energies are $E(v_n)=2E_1=E(\text{piece 1})+E(\text{piece 2})$, where $E_1=6\pi^2r^3L^{-2}\Delta\mathcal A$. Hence the compactification is $\mathcal M\times\mathcal M\times[-\infty,\infty]$. ∎

**Proof of Theorem D(3).** By Theorem B(2), $\mathcal M=\{[\mathfrak u]\}$, which gives the description of all moduli spaces. The ends are the case $T\to\pm\infty$ above, which is the statement of [R25, Theorem C(3)], now for the complete moduli space.

*Transversality.* The linearization at $(\omega^1,\omega^2)$ is $D^V_{\omega^1}\oplus D^V_{\omega^2}$. Each summand is either invertible (constant factor, Theorem C(1)) or onto of index $1$ (factor $\mathfrak u$, Theorem C(3)). So every element is regular, of index $1$ or $2$, equal to the grading difference.

*Completeness.* Every $\mathcal C_2$ object and trajectory has been listed. Each lies in $\mathcal U\times\mathcal U$ for the neighbourhood $\mathcal U$ of [R25, Thm. B]: the objects $k_\pm$ do, and $\mathfrak u$ does by its construction there. Conversely, the local moduli spaces of [R25, Thm. C] are contained in ours. So the two coincide. ∎

**Proof of Theorem D(4).** *Category.* The objects are $k_{ab}$ with gradings $2,1,1,0$. The morphism spaces are:
* the compact $0$-manifolds $\widehat{\mathcal M}(k_{++},k_{\pm\mp})$ and $\widehat{\mathcal M}(k_{\pm\mp},k_{--})$, each a point;
* the compact $1$-manifold with boundary $\overline{\mathcal M}(k_{++},k_{--})=[-\infty,\infty]$, whose boundary is the union of the two composites.

So the composition axioms of a flow category [LS, §3] hold. The remaining axioms are as follows.
* The product framings on the two boundary points induce opposite orientations of the interval, because the Koszul count of ends is $1-1=0$ (verify.py §8.7).
* A framing of the trivial normal bundle of a neatly embedded interval extends prescribed framings at its ends iff the two framings lie in the same component of the space of framings. This is exactly that orientation condition.

So a coherent framing exists. The conclusion below does not depend on which coherent framing is chosen.

*Realization.* By [LS, §3] the realization is a finite CW spectrum. Its cells correspond to the objects, in their gradings, and its cellular chain complex is the signed count of index-one morphisms. With Koszul signs this complex is the one displayed in Theorem D(4). It satisfies $\partial^2=0$, and its Smith normal form over $\mathbb Z$ is ${\rm diag}(1,1,0,0)$, so it is acyclic (verify.py §8.1–8.4; control §8.5). This acyclicity holds for every sign choice compatible with $\partial^2=0$, since each such choice is a rescaling of basis vectors by $\pm1$. A finite CW spectrum with vanishing integral homology is contractible. For $L<\pi r$ there are no objects. ∎

## 7. Remarks, consistency, and what remains

*Remark 7.1 (why Keller–Osserman fails in $\mathcal C_{V_4}$).* The leading part of $\Delta|u|^2$ is $2|\nabla u|^2+4\sigma_2$, with $\sigma_2=|u_1u_2|^2+|u_2u_3|^2+|u_3u_1|^2$. This vanishes on the coordinate axes. Rescaled limits at interior points are bounded entire solutions of $2\bar\partial u=\overline{\nabla(u_1u_2u_3)}$ with zero energy. Constants $(\lambda,0,0)$ are such solutions. So interior concentration cannot be excluded by blow-up alone.

Theorem A sidesteps this. It controls only ${\rm Re}\,u$, and that is all the rigidity argument needs. We do not prove a bound on ${\rm Im}\,u$ beyond what isotropy and [R-hw32, Thm. B] give a posteriori.

*Remark 7.2 (consistency).*
* Theorem B(1) at $L$ near $\pi r$ agrees with [R25, Cor. B′] (local uniqueness in $\mathcal C_{V_4}$).
* The linear identity behind Proposition 5.1, evaluated at the fold background $v_0$, reproduces [R25, Prop. 4.1(c)]: on the kernel candidates $\beta=\sinh2\sqrt2t$ it gives $(\alpha\beta)'=-3(\alpha^2+\beta^2)$, so $\alpha\beta$ cannot vanish at both ends (verify.py §7.3–7.4).
* The numerical observation of [R25, §7.2], that there is no traceless Jacobi field on part of the isotropic branch, is now a theorem for the whole branch $L>\pi r$.
* The index $-3$ and cokernel $\mathbb R^4$ of [R30], the three-sphere of [R31] and the eight objects of [R32] are not left-invariant. The $V_4$ class does not see them, so its realization is trivial, while the full local type is $S^1\vee S^4$ [R31, R33]. This agrees with [R-hw32, Rem. 8.2].
* The isolation and compactness results of [R34] are local; Theorem D(2) is global in $\mathcal C_2$.

*Remark 7.3 (Berger metrics).* For $c=(c_1,c_1,c_3)$ one still has $\partial_1\mathcal W-\partial_2\mathcal W=(\beta_1+2\beta_3-u_3)(u_1-u_2)$ (verify.py §6.5). So $u_1\equiv u_2$ would follow from ${\rm Re}\,u_3\le\beta_1+2\beta_3$, as in §4. We have not proved the corresponding maximum principle, and we claim nothing for Berger metrics.

**What remains for triaxial metrics.** Near the round metric, [R25, Thm. B] gives non-isotropic objects $k_\pm$. A complete $\mathcal C_2$ category there would be the first complete category with non-isotropic objects. The rigidity (4.1) is unavailable, because the traceless equations become inhomogeneous. The natural route is perturbative: a priori $Z$-bounds uniform in $c$ near the round metric, then compactness, then local uniqueness. That requires a bound on ${\rm Im}\,u$ in the presence of flat directions (Remark 7.1). Theorem A, or its perturbation in $c$, controls ${\rm Re}\,u$. It suggests that a plateau $u_1\approx-iD$ is incompatible with bounded ${\rm Re}\,u_1$, because ${\rm Im}\,\partial_1\mathcal W\approx2{\rm Im}\,u_1$ forces ${\rm Re}\,u_1$ to change at rate $\approx2D$. We have not turned this into a proof.

## 8. Status of the claims

**Proved here.**
* Theorem A (Lemmas 2.1, 2.2, 3.1–3.4).
* Theorem B (Lemma 4.1, Propositions 4.2, 4.3).
* Theorem C (Propositions 5.1, 5.2).
* Theorem D (Lemma 6.1 and §6).

**Imported.**
* From [R25]: the $V_4$ reduction, the operator theory (V1), the gauge lemma (V2), and Theorem C and Cor. B′ as the local statements we globalize.
* From [R24]: the isotropic reduction, the classification (F2), due to [He, AH], and the transversality (F5).
* From the companion preprint [R-hw32]: Theorems A–D and Lemmas 3.2, 5.1, 5.2 (isotropic global theory). It is published as rStation math_46 (https://rstation.ai/problems/math/papers/46/v1); our Theorems B(2), C(3) and D depend on it.
* Standard tools:
  * interior regularity for $\bar\partial$ [Ve, MS];
  * the Carleman similarity principle [MS, §2.3];
  * bounded perturbations of self-adjoint operators [Ka];
  * the Robbin–Salamon Fredholm theorem [RS];
  * realization of framed flow categories [LS, CJS].

**Numerical only.** verify.py §10:
* the identity (4.1) along a non-isotropic static orbit;
* $0<p_+<1$ along $k_+$;
* the absence of small eigenvalues of a discretized traceless operator at $k_+$.

None of these is used in the proofs.

**Not claimed.**
* Triaxial or Berger metrics.
* The full gauge theory.
* Transversality or counts for $L\ge\pi r+\delta$.
* An explicit $\delta$.
* Optimality of $(-1/r,3/r)$.
* A coupled concatenation.

**Verifier.**
* verify.py runs 61 checks and ends with FALLOS = 0, in about 5 s. §§1–9 are exact (sympy, rational arithmetic) and include negative controls. §10 is numerical and marked as such.
* verify.mpl mirrors §§1–8 symbolically, with 34 checks. It was not run, because Maple is not available to us.

## References

[AH] L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.

[CJS] R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.

[He] M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.

[Ka] T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1976.

[LS] R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.

[MS] D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*, AMS Colloquium Publications 52, 2004 (§2.3 and Appendix B).

[RS] J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.

[Ve] I. N. Vekua, *Generalized Analytic Functions*, Pergamon Press, 1962.

[R24] rStation math_24 v2, https://rstation.ai/problems/math/papers/24/v2

[R25] rStation math_25 v1, https://rstation.ai/problems/math/papers/25/v1

[R30] rStation math_30 v1, https://rstation.ai/problems/math/papers/30/v1

[R31] rStation math_31 v1, https://rstation.ai/problems/math/papers/31/v1

[R32] rStation math_32 v1, https://rstation.ai/problems/math/papers/32/v1

[R33] rStation math_33 v1, https://rstation.ai/problems/math/papers/33/v1

[R34] rStation math_34 v1, https://rstation.ai/problems/math/papers/34/v1

[R-hw32] *The complete isotropic Haydys–Witten flow category on $\mathbb R\times S^3\times I$ at the Anderson–Henningson fold*, rStation math_46 v1, https://rstation.ai/problems/math/papers/46/v1.

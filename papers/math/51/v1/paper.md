# A priori estimates for the Klein-symmetric Haydys–Witten equations on triaxial three-spheres, and the complete flow category with non-isotropic objects at the Anderson–Henningson fold

**Abstract.**

We study the Haydys–Witten (HW) equations on $\mathbb R_s\times S^3\times(0,L)$ with Nahm poles at both ends, for a left-invariant metric with Milnor constants $c=(c_1,c_2,c_3)$, in the sector $\mathcal C_{V_4}$ of fields invariant under $SU(2)_L\rtimes V_4$. There the equations read $\partial_sz+i\partial_yz=-\overline{\nabla W_c}$ with $W_c=z_1z_2z_3-\frac12\sum c_iz_i^2$. The cubic has flat directions, so no Keller–Osserman bound is available. We prove:

(A) For every metric and every $L$, every $V_4$ trajectory satisfies $|{\rm Re}\,z_k|\le S_c$ with $S_c$ explicit. On the round sphere $S_c=2/r$, reproving a companion result.

(B) A substitute for Keller–Osserman: $|z|\le K_0/\min(y,L-y)$, where $K_0$ depends only on the metric, $L$ and an energy bound. The proof combines a doubling lemma, a Liouville theorem for the flat directions, and a plateau estimate: integrating the imaginary part of the equation and using (A) shows that a large imaginary plateau costs energy.

(C) The Nahm pole is uniform, with $Z$-bounds. The leading cubic has a two-torus of twisted scale-invariant poles; (A) cuts it to four points, and a boundary blow-up excludes all but the Nahm pole.

(D) The $V_4$ Kapustin–Witten solutions form a compact set over every compact set of metrics and lengths.

(E) Near the round metric and the Anderson–Henningson fold, every $V_4$ object and trajectory lies in the local neighbourhood of rStation math_25. So the complete $V_4$ category has exactly two objects, non-isotropic for non-round $c$, and one transversal arrow.

(F) For $SU(2)\times SU(2)$ with principal pole, the complete category has four objects (gradings $2,1,1,0$), four index-one arrows, and $\widehat{\mathcal M}(k_{++},k_{--})\cong\mathbb R$, which compactifies to an interval with the two broken trajectories as ends. $d^2=0$ over $\mathbb Z$, and the Cohen–Jones–Segal realization is contractible.

This is the first complete HW flow category in our series with non-isotropic objects. Constants near the fold are not effective.

verify.py: 77 checks, FALLOS = 0.

---

## 1. Introduction and results

### 1.1 Background and goal

A Haydys–Witten flow category has Kapustin–Witten (KW) solutions as objects and HW trajectories as morphisms. On the Anderson–Henningson (AH) geometry $\mathbb R_s\times S^3\times(0,L)$ with Nahm poles at both ends [He, AH], our accepted papers treat the fold *locally*:

* the isotropic AH instanton [R24];
* the $V_4$ (Klein-symmetric) class on triaxial spheres [R25];
* the full linearization, the centre manifold, symmetry breaking, framed models and local compactness [R30–R34].

Two companion preprints made parts of this global, both on the *round* sphere:

* [R-hw32] treats the isotropic sector: two objects and one arrow;
* [R-hw35] treats the $V_4$ sector, where a rigidity identity forces every solution to be isotropic.

On a non-round sphere the objects $k_\pm$ of [R25, Thm. B] are *not* isotropic. [R-hw35, §7] lists what blocks a global theory there:

* the traceless equations become inhomogeneous, so the rigidity identity is lost;
* the flat directions of $z_1z_2z_3$ defeat Keller–Osserman;
* "a bound on ${\rm Im}\,u$ is missing".

That paper also offers a heuristic: a plateau with $u_1$ large and imaginary should be incompatible with bounded ${\rm Re}\,u_1$.

This paper supplies the missing estimates for *every* left-invariant metric and every $L$. The route is: a real-part bound (Theorem A), then an interior bound (Theorem B), then a uniform Nahm pole and $Z$-bounds (Theorem C), then compactness (Theorem D). Theorem B is the plateau heuristic made rigorous. We then globalize [R25, Thms. B–C] near the round fold by a compactness–contradiction argument, using the round rigidity of [R-hw35] at the limit (Theorems E–F).

### 1.2 Setting

**The $V_4$ class [R25, §3].** Let $e_i$ be a Milnor frame for a left-invariant metric $g_c$ on $SU(2)$, with $[e_j,e_k]=c_ie_i$ ($(i,j,k)$ cyclic, $c_i>0$). Let $\sigma^i$ be the dual coframe and $T_i=-\frac i2\sigma_i$. The class $\mathcal C_{V_4}$ consists of
$$A=\textstyle\sum_ia_i(s,y)T_i\sigma^i,\qquad\varphi=\sum_ib_i(s,y)T_i\sigma^i,\qquad A_s=A_y=0 .$$
Put $z_i=a_i+ib_i$. By [R25, Thm. A], the HW equations in $\mathcal C_{V_4}$ are equivalent to
$$\partial_sz_i+i\partial_yz_i=c_i\bar z_i-\bar z_j\bar z_k=-\overline{\partial_iW_c(z)},\qquad W_c=z_1z_2z_3-\tfrac12\textstyle\sum_ic_iz_i^2 . \tag{1.1}$$
Here $(i,j,k)$ runs over the cyclic permutations. Put
$$\beta_i=\tfrac12(c_j+c_k-c_i),\qquad m_i=c_i\beta_i-\beta_j\beta_k,\qquad\sigma=c_1+c_2+c_3 .$$
With $u_i=\beta_i-z_i=p_i+iq_i$, (1.1) becomes [R25, (3.2)]
$$\partial_su_i+i\partial_yu_i=\bar u_j\bar u_k-m_i+\beta_j(\bar u_i-\bar u_k)+\beta_k(\bar u_i-\bar u_j)=\overline{\partial_i\mathcal W_u} \tag{1.2}$$
(verify.py §1.1). The Nahm pole is $u_i\sim-i/y$ at $y=0$ and $u_i\sim-i/(y-L)$ at $y=L$, i.e. $z_i\approx\beta_i+i/y$. The round sphere of radius $r$ is $c_i=2/r$, with $\beta_i=1/r$ and $m_i=r^{-2}$ (§1.4).

We write $2\bar\partial=\partial_s+i\partial_y$, $2\partial=\partial_s-i\partial_y$ and $\Delta=4\partial\bar\partial$.

**Rescaled form and function spaces [R25, §4].** Put $y=L\tau$, $s=L\varsigma$, $\hat c=Lc$, $v=Lu$, $v_0=-i\pi\cot\pi\tau$ and $v=v_0\mathbf 1+w$. Then (1.2) becomes
$$\partial_\varsigma w=\mathcal G_{\hat c}(w):=\mathcal L^Vw+B_{\hat\beta}w+\mathcal Q(w)-\nu,\qquad\nu_i=\hat m_i-\pi^2, \tag{1.3}$$
on $X=L^2((0,1);\mathbb C^3)$ with the real inner product ${\rm Re}\int\bar f\cdot g$. Here:

* $\mathcal L^V$ is the self-adjoint operator of [R25, §4]; it does not depend on $c$;
* $B_{\hat\beta}w=M_{\hat\beta}\bar w$, with $M_{\hat\beta}$ real, symmetric and $O(|\hat\beta-\pi\mathbf 1|)$;
* $\mathcal Q(w)_i=\bar w_j\bar w_k$.

Let $Z=D(\mathcal L^V)$ carry the graph norm. Everything depends on $(c,L)$ only through $\hat c=Lc$. The round critical point is $\hat c_*=(2\pi,2\pi,2\pi)$, which is $L=\pi r$. We import:

* **(V1)** [R25, Prop. 4.1, Cor. 4.2]: $Z\hookrightarrow C^0([0,1];\mathbb C^3)$ compactly, with $|w(\tau)|\le C_Z\|w\|_Z\min(\tau,1-\tau)^{1/2}$.
* **(V2)** [R25, Lemma 5.5]: distinct configurations in $\mathcal C_{V_4}$ with $w\in Z$ are gauge inequivalent.
* **(V3)** [R25, Lemma 5.4]: (1.3) is the $X$-gradient flow of
$$\mathcal F_{\hat c}(w)=\tfrac12\langle w,(\mathcal L^V+B_{\hat\beta})w\rangle+{\rm Re}\textstyle\int_0^1w_1w_2w_3-\langle\nu,w\rangle,$$
which is $C^1$ on $Z$ (as in [R-hw32, Lemma 3.1]) and depends continuously on $\hat c$.

**The trajectory class.** A *$V_4$ trajectory* for $(c,L)$ is a map $w\in C^0(\mathbb R;Z)\cap C^1(\mathbb R;X)$ that solves (1.3) for every $\varsigma$ and has limits $w_{\pm\infty}$ in $Z$ as $\varsigma\to\pm\infty$. We write $\mathcal T^V_{c,L}$ for the set of these. Constant elements are the $V_4$ KW solutions with $w\in Z$, called *statics* or *objects*. We impose no smallness and no energy bound. For round $c$ this is the class of [R-hw35, §1.2].

The *energy* is $E(w)=\iint|\partial_su|^2\,ds\,dy=L^{-2}\int\|\partial_\varsigma w\|_X^2\,d\varsigma$.

**The local theory [R25, Thm. B].** There are $\delta>0$, a neighbourhood $V$ of $\hat c_*$, a neighbourhood $\mathcal U$ of $0$ in $Z$ (for the shifted variable $\tilde w$ of [R25, Lemma 5.1]) and a function $\bar\nu_c(\nu_T)$ with the following property. Put $\Delta=\bar\nu-\bar\nu_c(\nu_T)$. Then for $\hat c\in V$:

* the statics with $\tilde w\in\mathcal U$ are: none if $\Delta<0$; one, which is degenerate, if $\Delta=0$; and exactly two, $k_\pm$, if $0<\Delta<\delta$;
* for $0<\Delta<\delta$ there is an arrow $\mathfrak u:k_+\to k_-$, transversal with index $1$, which is unique up to translation among nonconstant solutions with $\tilde w(\varsigma)\in\mathcal U$ for all $\varsigma$;
* for non-round $c$, $k_\pm$ and $\mathfrak u$ are not isotropic.

[R25, §9] lists "global classification away from $\mathcal U$" as open.

### 1.3 Results

For a compact set $\mathcal K\subset(0,\infty)^3$ of metrics we write $c_{\min}=\min_{\mathcal K}\min_ic_i$.

**Theorem A (real-part bound; every metric, every $L$).** For $c\in(0,\infty)^3$ put
$$S_c:=\max\Big(\max_k|\beta_k|,\ \max_{k:\ \sigma^2\ge8c_k^2}\tfrac14\big(\sigma+\sqrt{\sigma^2-8c_k^2}\big)\Big)\ \le\ \max\big(\max_k|\beta_k|,\tfrac\sigma2\big).$$
Then every $w\in\mathcal T^V_{c,L}$, for every $L>0$, satisfies
$$|{\rm Re}\,z_k(s,y)|\le S_c\qquad\text{for all }k,s,y .$$
Equivalently, the connection coefficients satisfy $|a_k|\le S_c$. On the round sphere $S_c=2/r$, which is [R-hw35, Thm. A] ($-1/r\le{\rm Re}\,u_k\le3/r$).

**Theorem B (interior estimate: a substitute for Keller–Osserman).** Let $\mathcal K$ be compact, $L_{\max}>0$ and $E_0\ge0$. There is $K_0=K_0(\mathcal K,L_{\max},E_0)$ such that every $w\in\mathcal T^V_{c,L}$ with $c\in\mathcal K$, $0<L\le L_{\max}$ and $E(w)\le E_0$ satisfies
$$|z(s,y)|\le\frac{K_0}{\min(y,L-y)}\qquad\text{on }\mathbb R\times(0,L).$$
This applies in particular to all statics, with $E=0$.

**Theorem C (uniform Nahm pole and $Z$-bounds).** Let $\mathcal K$ be compact, $0<L_1<L_2$ and $E_0\ge0$. Let $\mathcal F$ be the set of $w\in\mathcal T^V_{c,L}$ with $c\in\mathcal K$, $L\in[L_1,L_2]$ and $E(w)\le E_0$.
1. For every $\delta\in(0,1)$ there is $y_\delta>0$ such that $y\,|u(s,y)+i\mathbf 1/y|<\delta$ for all $w\in\mathcal F$, $s\in\mathbb R$ and $0<y<y_\delta$. The symmetric statement holds at $y=L$.
2. There are $y_1>0$ and $C$ such that for $0<y\le y_1$:
$$|{\rm Re}\,u|\le Cy^{3/2},\qquad|{\rm Im}\,u+\mathbf 1/y|\le Cy^{3/4},\qquad|\nabla(u+i\mathbf 1/y)|\le Cy^{-1/4},$$
and symmetrically at $y=L$.
3. There is $M$ such that $\sup_\varsigma\|w(\varsigma)\|_Z\le M$ for all $w\in\mathcal F$.

**Theorem D (compactness).**
1. Let $\mathcal P\subset(0,\infty)^3\times(0,\infty)$ be compact. The set of triples $(c,L,w)$ with $(c,L)\in\mathcal P$ and $w$ a static is compact in $\mathcal P\times Z$.
2. Let $(c_n,L_n)\to(c,L)$, and let $w_n\in\mathcal T^V_{c_n,L_n}$ with $E(w_n)\le E_0$. Then, after translations and passing to a subsequence, $w_n\to w$ in $C^0_{\rm loc}(\mathbb R;X)\cap C^0_{\rm loc}(\mathbb R;C^0)\cap L^2_{\rm loc}(\mathbb R;Z)$. The limit $w\in C^0(\mathbb R;Z)\cap C^1(\mathbb R;X)$ solves (1.3) at $(c,L)$, with $\sup\|w\|_Z\le M$ and $E(w)\le E_0$. If the statics at $(c,L)$ are isolated in $Z$, then $w\in\mathcal T^V_{c,L}$.

**Theorem E (the complete $V_4$ category near the fold, uniformly in the metric).** There are a neighbourhood $V'\subset V$ of $\hat c_*$ and $\delta'\in(0,\delta]$ such that the following holds for every left-invariant metric $g_c$ and every $L$ with $Lc\in V'$.
1. *(Objects.)* Every static has $\tilde w\in\mathcal U$. So there are no $V_4$ KW solutions if $\Delta<0$; exactly one, which is degenerate, if $\Delta=0$; and exactly $k_+\ne k_-$, nondegenerate and gauge inequivalent, if $0<\Delta<\delta'$.
2. *(Morphisms.)* Every $w\in\mathcal T^V_{c,L}$ has $\tilde w(\varsigma)\in\mathcal U$ for all $\varsigma$.
   * For $\Delta\le0$ every trajectory is constant; for $\Delta<0$ there are none at all.
   * For $0<\Delta<\delta'$ the nonconstant trajectories are exactly the translates of $\mathfrak u:k_+\to k_-$, which is onto with index $1$. In particular $\mathcal M(k_-,k_+)=\emptyset$, and there are no nonconstant loops.
3. *(Realization.)* For $0<\Delta<\delta'$ the complete $V_4$ flow category has two objects with ${\rm gr}(k_+)-{\rm gr}(k_-)=1$ and one framed point. Its Cohen–Jones–Segal (CJS) realization is contractible for either framing.

For non-round $c$ the objects $k_\pm$ and the arrow $\mathfrak u$ are not isotropic.

**Theorem F (the complete $SU(2)\times SU(2)$ category with non-isotropic objects).** Let $G=SU(2)\times SU(2)$ with its principal Nahm pole $(\rho_0,\rho_0)$. Let $\mathcal C_2$ be the class of pairs of $\mathcal C_{V_4}$ fields on $(S^3,g_c)$ [R25, §7.2]. Let $Lc\in V'$ with $0<\Delta<\delta'$, and write $k_{ab}=(k_a,k_b)$.
1. The $\mathcal C_2$ objects are exactly $k_{++},k_{+-},k_{-+},k_{--}$. They are nondegenerate, with gradings $2,1,1,0$.
2. The nonempty spaces of unparametrized nonconstant trajectories are:
   * $\widehat{\mathcal M}(k_{++},k_{+-})$, $\widehat{\mathcal M}(k_{++},k_{-+})$, $\widehat{\mathcal M}(k_{+-},k_{--})$ and $\widehat{\mathcal M}(k_{-+},k_{--})$, each a single transversal point of index $1$;
   * $\widehat{\mathcal M}(k_{++},k_{--})=\{[(\mathfrak u,\mathfrak u(\cdot+T))]:T\in\mathbb R\}\cong\mathbb R$, transversal of index $2$.

   All others are empty, including $\widehat{\mathcal M}(k_{+-},k_{-+})$. These are *all* $\mathcal C_2$ objects and trajectories.
3. The compactification of $\widehat{\mathcal M}(k_{++},k_{--})$ is $[-\infty,\infty]$, with boundary exactly
$$\widehat{\mathcal M}(k_{++},k_{+-})\times\widehat{\mathcal M}(k_{+-},k_{--})\ \sqcup\ \widehat{\mathcal M}(k_{++},k_{-+})\times\widehat{\mathcal M}(k_{-+},k_{--}),$$
and energy is additive.
4. With Koszul signs the cellular complex is $\partial k_{++}=k_{-+}-k_{+-}$, $\partial k_{\pm\mp}=k_{--}$. It satisfies $\partial^2=0$ over $\mathbb Z$ and is acyclic, and the CJS realization is contractible for every coherent framing.

For non-round $c$ all four objects and all trajectories are non-isotropic.

**What is new.**
* *Theorem A* holds for every left-invariant metric. It uses the exact identity
$$\Delta a_1=a_1(c_1^2+|z_2|^2+|z_3|^2)-\sigma a_2a_3-2\beta_1b_2b_3$$
(Lemma 2.2), and the proof is short. At the round metric it reproves [R-hw35, Thm. A], whose proof was a two-sided bootstrap.
* *Theorem B* is, as far as we know, the first a priori bound for a vector $\zeta$-instanton system whose cubic has flat directions. It answers the question left open in [R-hw35, §7], namely the missing bound on ${\rm Im}\,u$. The plateau argument of §4 is the rigorous form of the heuristic stated there. One integrates the imaginary part of the $z_1$-equation over a square. The $\partial_s{\rm Im}\,z_1$ term costs energy, and the $\partial_y{\rm Re}\,z_1$ term is controlled by Theorem A, so a large imaginary plateau cannot persist on a square of side much larger than $1/|z|$.
* *Theorem C* contains a new structural observation. The leading cubic system has a two-torus of twisted scale-invariant poles $\rho/t$, $\rho_k=e^{i\theta_k}$ with $\sum\theta_k=\pi/2$ (verify.py §5.1). This torus is why the boundary blow-up of [R-hw32, Prop. 4.5] does not extend verbatim (§5.9). Theorem A cuts the torus down to four points. In the layer the rate is $y^{3/4}$ rather than $y$. This is natural: the inhomogeneity $(m_1-m_2)/y$ produces the resonant $y\log y$ terms observed numerically in [R25, §6] (Lemma 6.2, verify.py §6.4, §6.14).
* *Theorem D* gives compactness of the $V_4$ KW moduli space for every left-invariant metric and every $L$.
* *Theorems E–F* globalize [R25, Thms. B–C] to all of $\mathcal C_{V_4}$ and $\mathcal C_2$. They are the first complete HW flow categories in this series whose objects are not isotropic.

**What is not claimed.**
* A global classification for metrics or lengths outside $V'$, or transversality there. Theorems A–D hold everywhere, but they give compactness, not counts.
* Berger rigidity $u_1\equiv u_2$ for all $L$. The threshold of [R-hw35, Rem. 7.3] is not implied by Theorem A (verify.py §9.2–9.3; Remark 9.2).
* Effective $V'$ and $\delta'$; they come from a contradiction argument.
* The full gauge theory, where the AH arrow is obstructed and the local homotopy type is $S^1\vee S^4$ [R30, R31, R33]. That structure lives on configurations that are not left-invariant.
* A coupled (non-product) concatenation.

## 2. Preliminaries

**Lemma 2.1 (the class $\mathcal T^V_{c,L}$).** Let $w\in\mathcal T^V_{c,L}$ and $M_w=\sup_\varsigma\|w(\varsigma)\|_Z$.
* (a) $M_w<\infty$, and $u$ is a smooth solution of (1.2) on $\mathbb R\times(0,L)$.
* (b) Let $u_0=-i\frac\pi L\cot\frac{\pi y}L\mathbf 1$. Then $|u(s,y)-u_0(y)|\le C_ZM_wL^{-1}\min(y/L,1-y/L)^{1/2}$ for all $s$. In particular ${\rm Re}\,u\to0$ and $u+i\mathbf 1/y\to0$ as $y\to0$, uniformly in $s$, and symmetrically at $y=L$.
* (c) $u(s,\cdot)\to u_{\pm\infty}$ uniformly on $(0,L)$ as $s\to\pm\infty$, and in $C^k$ on compact subsets of $(0,L)$.
* (d) $w_{\pm\infty}$ are statics.
* (e) The reflection $R:z(s,y)\mapsto\overline{z(s,L-y)}$ and translations in $s$ preserve $\mathcal T^V_{c,L}$.

*Proof.* (a), (b) and (d) are proved verbatim as in [R-hw35, Lemma 2.1]: (V1) does not depend on $c$, and $B_{\hat\beta}$ is bounded. For (c), uniform convergence follows from $Z\hookrightarrow C^0$. The $C^k$ convergence follows from the interior estimates (Lemma 2.4) applied to $u(\cdot+s_n,\cdot)$, which are bounded on compact sets by (b). (e) is [R25, §3]. ∎

**Lemma 2.2 (second-order identities).** Smooth solutions of (1.1) satisfy $\Delta z_i=\sum_j\overline{\partial_{ij}W_c}\,\partial_jW_c$, and explicitly
$$\Delta a_i=a_i\big(c_i^2+|z_j|^2+|z_k|^2\big)-\sigma a_ja_k-2\beta_ib_jb_k, \tag{2.1}$$
$$\Delta b_i=b_i\big(c_i^2+|z_j|^2+|z_k|^2\big)-2\beta_ja_jb_k-2\beta_ka_kb_j . \tag{2.2}$$

*Proof.* Write $2\bar\partial z_i=-\overline{\partial_iW_c}+R_i$. Then
$$\Delta z_i=2\partial(2\bar\partial z_i)=\textstyle\sum_j\overline{\partial_{ij}W_c}\,\partial_jW_c-\sum_j\overline{\partial_{ij}W_cR_j}+2\partial R_i .$$
verify.py §2.1 checks this exactly for arbitrary $a_i,b_i$. Formulas (2.1)–(2.2) are its real and imaginary parts (§2.2–2.3, control §2.4). At the round metric, $-$(2.1) is the polynomial $F_1$ of [R-hw35, Lemma 2.2] (§2.5). ∎

**Lemma 2.3 (energy identity).** For $w\in\mathcal T^V_{c,L}$ and $a<b$,
$$\int_a^b\|\partial_\varsigma w\|_X^2\,d\varsigma=\mathcal F_{\hat c}(w(b))-\mathcal F_{\hat c}(w(a)).$$
Hence $L^2E(w)=\mathcal F_{\hat c}(w_{+\infty})-\mathcal F_{\hat c}(w_{-\infty})$, and $w$ is constant iff this vanishes.

*Proof.* As in [R-hw32, Lemma 3.2], with (V3). The cubic term is handled by $Z\hookrightarrow C^0$. ∎

**Lemma 2.4 (interior estimates [R-hw32, Lemma 4.4]).** Let $g$ be a $C^1$ solution of $2\bar\partial g=h(\xi,g,\bar g)$ on a disc $B_{2\varrho}$, $\varrho\le1$, with $h$ polynomial in $(g,\bar g)$ and coefficients bounded by $A$ together with their first derivatives, and $\sup|g|\le A$. Then $\varrho|\nabla g|\le C_A(\sup|g|+\varrho\sup|h(\cdot,0)|)$ at the centre, and the higher derivatives are bounded on $B_\varrho$. Families with uniform $C^0$ bounds are precompact in $C^k_{\rm loc}$. (Standard Cauchy–Pompeiu bootstrap [Ve, MS].)

**Lemma 2.5 (doubling lemma [PQS, Lemma 5.1]).** Let $(X,d)$ be complete, $\emptyset\ne D\subset\Sigma\subset X$ with $\Sigma$ closed, and $\Gamma=\Sigma\setminus D$. Let $M:D\to(0,\infty)$ be bounded on compact subsets of $D$, and let $k>0$. If $P\in D$ satisfies $M(P)\,{\rm dist}(P,\Gamma)>2k$, then there is $P'\in D$ with
* $M(P')\,{\rm dist}(P',\Gamma)>2k$ and $M(P')\ge M(P)$;
* $M\le2M(P')$ on $D\cap B(P',k/M(P'))$.

**Lemma 2.6 (scaling).** If $z$ solves (1.1), then $\hat z(\xi)=\lambda z(P+\lambda\xi)$ solves
$$2\bar\partial_\xi\hat z_i=\lambda c_i\overline{\hat z_i}-\overline{\hat z_j\hat z_k}$$
and $\int|\partial_{\xi_1}\hat z|^2d\xi=\lambda^2\int|\partial_sz|^2$ (verify.py §4.1–4.2). The same holds for (1.2): the coefficients $\beta$ and $m$ are multiplied by $\lambda$ and $\lambda^2$.

## 3. Proof of Theorem A

Fix $w\in\mathcal T^V_{c,L}$ and put $S=\sup_{k,s,y}|a_k|$. This is finite by Lemma 2.1(b), since $a_k=\beta_k-p_k$.

By Lemma 2.1(b), $a_k\to\beta_k$ as $y\to0$ or $y\to L$, uniformly in $s$. So $S\ge\max_k|\beta_k|$, and if $S=\max_k|\beta_k|$ there is nothing to prove. Assume $S>\max_k|\beta_k|$. Then the supremum is approached on a set $\{y'\le y\le L-y'\}$. As in [R-hw35, Lemma 3.1], there are an index $k$ (say $k=1$), a solution $\tilde u\in\{u,u_{+\infty},u_{-\infty}\}$ and an interior point at which:
* $\tilde a_1=\pm S$;
* $\pm\Delta\tilde a_1\le0$;
* $|\tilde a_2|,|\tilde a_3|\le S$.

The second item holds because an interior maximum (or minimum) has $\Delta\le0$ (or $\ge0$); for a static limit, $\Delta=d^2/dy^2$. The third holds because these values are limits of values of $a_j$. Write $x=\tilde a_2$, $\eta=\tilde a_3$, and $b_2,b_3$ for the imaginary parts at that point.

*Case $\tilde a_1=S$.* By (2.1),
$$0\ge\Delta\tilde a_1=S c_1^2+\big[S(x^2+\eta^2)-\sigma x\eta\big]+\big[S(b_2^2+b_3^2)-2\beta_1b_2b_3\big].$$
* The last bracket is $\ge(S-|\beta_1|)(b_2^2+b_3^2)\ge0$, since the remainder is $|\beta_1|(b_2\mp b_3)^2$ (verify.py §3.5).
* For the middle bracket $G(x,\eta)$ on the box $[-S,S]^2$:
  * if $\sigma\le2S$, then $G=(S-\frac\sigma2)(x^2+\eta^2)+\frac\sigma2(x-\eta)^2\ge0$ (§3.4), so $0\ge Sc_1^2>0$, which is absurd;
  * if $\sigma>2S$, the Hessian of $G$ is indefinite (§3.3), so $\min_{[-S,S]^2}G$ is attained on the boundary. On the edges $x=\pm S$,
  $$G-(2S^3-\sigma S^2)=S(\eta\mp S)(\eta\mp(\sigma-S))\ge0,$$
  because $\sigma-S>S$ (§3.1–3.2), and the edges $\eta=\pm S$ follow by symmetry. Hence $G\ge2S^3-\sigma S^2$.
* Therefore $0\ge S(2S^2-\sigma S+c_1^2)$, i.e. $2S^2-\sigma S+c_1^2\le0$.

*Case $\tilde a_1=-S$.* Now $0\le\Delta\tilde a_1$, which is
$$-Sc_1^2-\big[S(x^2+\eta^2)+\sigma x\eta\big]-\big[S(b_2^2+b_3^2)+2\beta_1b_2b_3\big].$$
Replacing $x$ by $-x$ reduces this to the first case, with the same conclusion.

The quadratic $2S^2-\sigma S+c_1^2$ factors as $2(S-S_+)(S-S_-)$ with $S_\pm=\frac14(\sigma\pm\sqrt{\sigma^2-8c_1^2})$ (§3.6). If $\sigma^2<8c_1^2$ it is positive, which is a contradiction. Otherwise $S\le S_+(c_1)$. In all cases $S\le S_c$.

Moreover $S_+\le\sigma/2$, which gives the upper bound for $S_c$. At $c_i=2/r$: $\sigma=6/r$, $\sqrt{\sigma^2-8c^2}=2/r$, $S_+=2/r$ and $\beta=1/r$. So $S_c=2/r$ and ${\rm Re}\,u_k=1/r-a_k\in[-1/r,3/r]$ (§3.7, §9.1). ∎

*Remark 3.1.* verify.py §3.8–3.9 tests the pointwise contradiction in exact rational arithmetic: $4000$ random metrics in $[1.5,2.6]^3$, with $S>S_c$ and arbitrary $b$. The bound is sharp for the pointwise argument. At the round metric the configurations $a=(2,2,2)$ and $(-2,2,-2)$ with $b=0$ give $\Delta a_1=0$ (§3.10, control §3.11). These are exactly the extremal configurations of [R-hw35, Rem. 3.5] after $a=1-p$ (§3.12). Since $S_c$ is bounded on compact sets, the bound is uniform on $\mathcal K$.

## 4. Proof of Theorem B

**Lemma 4.1 (Liouville for the flat directions).** Let $\eta:\mathbb R\to\mathbb R^3$ be a bounded $C^1$ solution of $\eta_i'=-\eta_j\eta_k$. Then $\eta$ is constant, with at most one nonzero component.

*Proof.* The quantities $\kappa_j=\eta_j^2-\eta_1^2$ are conserved (verify.py §4.3). Put $x=\eta_1^2$ and $P=\eta_1\eta_2\eta_3$. Then $x'=-2P$ and $x'^2=4g(x)$ with $g(x)=x(x+\kappa_2)(x+\kappa_3)$ (§4.4–4.5). Since $\eta_j^2=x+\kappa_j\ge0$, we have $x\ge x_0:=\max(0,-\kappa_2,-\kappa_3)$. Moreover $g>0$ on $(x_0,\infty)$, and $g(x_0)=0$.

Suppose $x(t_0)>x_0$. Using the symmetry $\eta(t)\mapsto-\eta(-t)$ we may assume $P(t_0)>0$. Then, as long as $x>x(t_0)$ backward in time, $P=\sqrt{g(x)}$ and $x'=-2\sqrt{g(x)}<0$. Since $\int^\infty dx/\sqrt{g(x)}<\infty$ (§4.6), $x$ reaches $\infty$ at a finite negative time. This contradicts boundedness.

Hence $x\equiv x_0$, so $P\equiv0$ and every $|\eta_i|$ is constant. So $\eta$ is constant, and $\eta_j\eta_k=0$ for all pairs (§4.7, control §4.8). ∎

**Proof of Theorem B.** Put $M(P)=|z(P)|+1$ on $D=\mathbb R\times(0,L)$, with $\Sigma=\mathbb R\times[0,L]$ and $\Gamma=\mathbb R\times\{0,L\}$. It suffices to find $k_0$ with $M(P)\,{\rm dist}(P,\Gamma)\le2k_0$ for every solution in the family; then $K_0=2k_0$.

Suppose not. Then there are $c_n\in\mathcal K$, $L_n\le L_{\max}$, $w_n$ with $E(w_n)\le E_0$, and points $P_n$ with $M_n(P_n){\rm dist}(P_n,\Gamma_n)>2k_n$, where $k_n\to\infty$. Lemma 2.5 gives points $P_n'$ with $\mu_n:=M_n(P_n')$ such that:
* $\mu_n\,{\rm dist}(P_n',\Gamma_n)>2k_n$;
* $M_n\le2\mu_n$ on $B(P_n',k_n/\mu_n)$, which lies in $D_n$.

Since ${\rm dist}\le L_{\max}/2$, we get $\mu_n\to\infty$.

*Blow-up.* Let $\lambda_n=1/\mu_n$ and $\hat z_n(\xi)=\lambda_nz_n(P_n'+\lambda_n\xi)$ on $B(0,k_n)$. By Lemma 2.6:
* $\hat z_n$ solves $2\bar\partial\hat z_i=\lambda_nc_{n,i}\overline{\hat z_i}-\overline{\hat z_j\hat z_k}$;
* $|\hat z_n|\le2$ and $|\hat z_n(0)|=1-\lambda_n$;
* $\int_{B(0,k_n)}|\partial_{\xi_1}\hat z_n|^2\le\lambda_n^2E_0\to0$;
* by Theorem A, $|{\rm Re}\,\hat z_n|\le\lambda_nS_{\mathcal K}\to0$, where $S_{\mathcal K}=\max_{\mathcal K}S_c$.

By Lemma 2.4 a subsequence converges in $C^1_{\rm loc}(\mathbb R^2)$ to some $\hat z$, which satisfies:
* $\partial_{\xi_1}\hat z=0$ and ${\rm Re}\,\hat z=0$;
* $|\hat z|\le2$ and $|\hat z(0)|=1$;
* $2\bar\partial\hat z=-\overline{\hat z_j\hat z_k}$.

Writing $\hat z=i\eta(\xi_2)$, this equation reads $\eta_i'=-\eta_j\eta_k$ on $\mathbb R$. By Lemma 4.1, $\hat z\equiv(i\epsilon,0,0)$ up to relabelling, with $\epsilon=\pm1$.

*Plateau estimate.* By verify.py §4.9, the imaginary part of the $\hat z_1$-equation is
$$\partial_{\xi_1}\hat b_1+\partial_{\xi_2}\hat a_1=-\lambda_nc_{n,1}\hat b_1+\hat a_2\hat b_3+\hat a_3\hat b_2 .$$
Fix $K>\big(E_0^{1/2}+2S_{\mathcal K}\big)/c_{\min}+1$ and integrate over the square $Q=[-K/2,K/2]^2$, which lies in $B(0,k_n)$ for large $n$. On the left:
* $\big|\iint_Q\partial_{\xi_1}\hat b_1\big|\le K\big(\iint_Q|\partial_{\xi_1}\hat z_n|^2\big)^{1/2}\le K\lambda_nE_0^{1/2}$;
* $\big|\iint_Q\partial_{\xi_2}\hat a_1\big|=\big|\int[\hat a_1]_{\xi_2=-K/2}^{K/2}\,d\xi_1\big|\le2K\lambda_nS_{\mathcal K}$.

On the right, $\hat b_1\to\epsilon$ and $\hat b_2,\hat b_3\to0$ uniformly on $Q$, while $|\hat a_j|\le\lambda_nS_{\mathcal K}$. Hence
$$\Big|\iint_Q\big(-\lambda_nc_{n,1}\hat b_1+\hat a_2\hat b_3+\hat a_3\hat b_2\big)\Big|\ge\lambda_n\big(c_{\min}K^2-o(1)K^2\big).$$
Dividing by $\lambda_n$ gives $c_{\min}K^2(1-o(1))\le K(E_0^{1/2}+2S_{\mathcal K})$, which contradicts the choice of $K$ for large $n$ (§4.10). ∎

*Remark 4.2 (where each hypothesis enters).*
* Without Theorem A, the limit could be $(e^{i\theta},0,0)$ with $\theta=0$. Then $\hat b_1\equiv0$ and the plateau estimate gives nothing (verify.py §4.11). The same bound also controls $\partial_y{\rm Re}\,z_1$ and the products $a_jb_k$.
* Without an energy bound, $\partial_s{\rm Im}\,z_1$ is uncontrolled. Indeed $z_1=iKe^{-c_1s}$, $z_2=z_3=0$ solves the linearized equation $2\bar\partial z_1=c_1\bar z_1$, so a dynamic plateau is possible when it is paid for by energy.

For statics, $\partial_s\equiv0$, and the argument is exactly the plateau heuristic of [R-hw35, §7].

## 5. Uniform Nahm pole (proof of Theorem C(1))

**Lemma 5.1 (static half-line solutions).** Let $\eta:(0,\infty)\to\mathbb R^3$ be $C^1$ with $\eta_i'=\eta_j\eta_k$ and $|\eta(t)|\le C/t$. Then either $\eta\equiv0$, or $\eta=\mathbf s/(t+c)$ with $c\ge0$ and
$$\mathbf s\in\mathbb S:=\{-\mathbf 1,(1,1,-1),(1,-1,1),(-1,1,1)\}.$$

*Proof.* The differences $\eta_i^2-\eta_j^2$ are conserved (verify.py §5.6), and they tend to $0$ as $t\to\infty$. So $|\eta_1|=|\eta_2|=|\eta_3|=:h$. If $h(t_0)=0$, then $\eta(t_0)=0$ and $\eta\equiv0$ by uniqueness. Otherwise the signs $s_i$ are constant and $h'=s_1s_2s_3h^2$. For $s_1s_2s_3=+1$, $h$ blows up in finite positive time. For $s_1s_2s_3=-1$, $h=1/(t+c)$ with $c\ge0$ (§5.4–5.5). ∎

*Remark 5.2 (the torus of twisted poles).* For the full complex leading system $u_i'=-i\overline{u_ju_k}$, the scale-invariant solutions $\rho/t$ form a two-torus $\rho=(e^{i\theta_1},e^{i\theta_2},e^{i\theta_3})$ with $\sum\theta_k\equiv\pi/2$ (verify.py §5.1–5.2). In log-time the linearization at $-i\mathbf 1$ has eigenvalues $3,-1,0,0,2,2$; the two zeros are the torus directions (§5.8).

A twisted pole with $0<|\rho+i\mathbf 1|<\delta/2$ satisfies the "first-scale" condition used in [R-hw32, Prop. 4.5] (§5.9). So that argument does not by itself exclude loss of the pole in $\mathcal C_{V_4}$. Theorem A gives ${\rm Re}\,\rho=0$, and the torus meets $i\mathbb R^3$ only in $i\mathbb S$ (§5.3).

**Proof of Theorem C(1).** Suppose the claim fails for some $\delta\in(0,1)$. Then there are $w_n\in\mathcal F$ and points $(s_n,y_n)$ with $y_n\to0$ and $d_n(y_n)\ge\delta$, where
$$d_n(\sigma)=\sigma|u_n(s_n,\sigma)+i\mathbf 1/\sigma| .$$
By Lemma 2.1(b), $d_n$ is continuous and $d_n(\sigma)\to0$ as $\sigma\to0$. Let $\sigma_n$ be the first $\sigma$ with $d_n(\sigma)=\delta/2$; then $\sigma_n\le y_n\to0$ and $d_n<\delta/2$ on $(0,\sigma_n)$.

Put $\hat u_n(x,t)=\sigma_nu_n(s_n+\sigma_nx,\sigma_nt)$. By Lemma 2.6 it solves (1.2) with $(\beta,m)$ replaced by $(\sigma_n\beta,\sigma_n^2m)$. Its energy is at most $\sigma_n^2E_0\to0$, and $|{\rm Re}\,\hat u_n|\le\sigma_n(S_{\mathcal K}+|\beta|)\to0$ by Theorem A. By Theorem B, $|\hat u_n|\le(K_0+o(1))/t$ for $t\le L_1/(2\sigma_n)$. By Lemma 2.4, a subsequence converges in $C^1_{\rm loc}(\mathbb R\times(0,\infty))$ to some $\hat u$ with:
* $\partial_x\hat u=0$ and ${\rm Re}\,\hat u=0$;
* $|\hat u|\le K_0/t$;
* $\hat u=i\eta(t)$, with $\eta$ real.

The limit equation $i\hat u'=\overline{\hat u_j\hat u_k}$ becomes $\eta_i'=\eta_j\eta_k$. Moreover $t|\eta(t)+\mathbf 1/t|=\lim_nd_n(\sigma_nt)\le\delta/2$ for $0<t\le1$, with equality at $t=1$.

Now go through the list of Lemma 5.1:
* $\eta\equiv0$, and $\mathbf s/(t+c)$ with $c>0$, give $t|\eta+\mathbf 1/t|\to\sqrt3$ as $t\to0$;
* $\mathbf s/t$ with $\mathbf s\ne-\mathbf 1$ gives the constant $2\sqrt2$ (§5.7).

All of these exceed $\delta/2<\frac12$ near $t=0$. The remaining solution $-\mathbf 1/t$ gives $0\ne\delta/2$ at $t=1$. This is a contradiction. The end $y=L$ follows by the reflection $R$. ∎

## 6. Layer barriers and the $Z$-bound (proof of Theorem C(2)–(3))

Fix $\delta=\frac1{40}$. By Theorem C(1) there is a layer $0<y\le y_\delta$ in which $|D|\le\delta/y$, where $D=u+i\mathbf 1/y$. Write $D=P+iQ$, so $P=p={\rm Re}\,u$ and $Q_i=q_i+1/y$. Then $|Q_i|\le\delta/y$, and $q_i=-\theta_i/y$ with $\theta_i\in[1-\delta,1+\delta]$. By Theorem A, $|p|,|a|\le S_{\mathcal K}+\max|\beta|=:S'$. Let $\bar\beta=\max_{\mathcal K}\max_i|\beta_i|$, and choose
$$y_1\le\min\big(y_\delta,\tfrac{L_1}4,1,(3/80)^{1/2}\bar\beta^{-1}\big).$$
The function $D$ satisfies
$$2\bar\partial D_i=\tfrac iy(\bar D_j+\bar D_k)+\bar D_j\bar D_k+\beta_j(\bar D_i-\bar D_k)+\beta_k(\bar D_i-\bar D_j)-m_i$$
(verify.py §6.1); the pole terms cancel.

**Lemma 6.1 (comparison in the layer).** Let $f$ be a function built from $u$ and $\Omega=\mathbb R\times(0,y_1]$. Assume:
1. $\Delta f=Vf+g$ on $\Omega$, and the same identity holds for the static limits $u_{\pm\infty}$;
2. $\phi_0(y)>0$ satisfies $(\Delta-V)\phi_0<0$, and $B(y)$ satisfies $(\Delta-V)(f-B)>0$ on $\Omega$. These inequalities hold for every solution in $\mathcal F$, because they follow pointwise from the layer bound and Theorem A;
3. $|f|\le F_0(y)$ on $\Omega$ with $F_0(y_1)<B(y_1)$, and $\limsup_{y\to0}\sup_s(f-B)/\phi_0<0$.

Then $f\le B$ on $\Omega$.

*Proof.* Let $h=(f-B)/\phi_0$ and suppose $\sup_\Omega h>0$.

By item 3 the supremum is approached on $\mathbb R\times[\epsilon,y_1-\epsilon]$ for some $\epsilon>0$. Here we use that $F_0$ and $B$ depend only on $y$ and are continuous.

If the supremum is attained, then at the maximum point $\nabla h=0$ and $\Delta h\le0$, so
$$(\Delta-V)(f-B)=\phi_0\Delta h+2\nabla\phi_0\cdot\nabla h+h(\Delta-V)\phi_0<0 .$$
This contradicts item 2.

Otherwise it is approached along $|s_n|\to\infty$. By Lemma 2.1(c), the static limit then has an interior maximum of $h_{\pm\infty}$ with the same positive value, and the same computation, with $\Delta=d^2/dy^2$, gives a contradiction. ∎

**Lemma 6.2 (traceless imaginary parts).** Let $\gamma=q_1-q_2$. By verify.py §6.2,
$$\Delta\gamma=V\gamma+g,\qquad V=c_1^2+a_2^2+(a_3^2+2\beta_3a_3)+(q_3^2-q_1q_2),$$
$$g=q_2(c_1^2-c_2^2+a_2^2-a_1^2)+2q_3(\beta_1a_1-\beta_2a_2).$$
In the layer:
* $V\ge-\bar\beta^2-4\delta/y^2$, because $\theta_3^2-\theta_1\theta_2\ge(1-\delta)^2-(1+\delta)^2=-4\delta$ (§6.3);
* $|g|\le C_g/y$, with $C_g$ depending only on $\mathcal K$, by Theorem A.

At the pole, $g\to(m_1-m_2)/y$ (§6.4). Then $|q_i-q_j|\le Ky^{3/4}$ on $(0,y_1]$ for all $i,j$, with $K$ uniform on $\mathcal F$.

*Proof.* Take $\phi_0=y^{1/4}$ and $B=Ky^{3/4}+\eta y^{1/4}$ with $\eta>0$. For $\alpha\in\{\frac14,\frac34\}$,
$$(\Delta-V)y^\alpha\le\big(-\tfrac3{16}+4\delta+\bar\beta^2y^2\big)y^{\alpha-2}\le-\tfrac1{20}y^{\alpha-2}$$
(§6.5–6.6), using $4\delta=\frac1{10}$ and $\bar\beta^2y_1^2\le\frac3{80}$. Hence
$$(\Delta-V)(\gamma-B)\ge-C_g/y+\tfrac K{20}y^{-5/4}>0\qquad\text{if }K>20C_gy_1^{1/4}.$$
Take $F_0=2\delta/y$ and $K>2\delta y_1^{-7/4}$. As $y\to0$, $(\gamma-B)/\phi_0\le C_uy^{1/4}-Ky^{1/2}-\eta\to-\eta$ by Lemma 2.1(b), with a constant $C_u$ that depends on the solution, which is allowed.

Lemma 6.1 gives $\gamma\le B$. The same argument applies to $-\gamma$, which satisfies $\Delta(-\gamma)=V(-\gamma)-g$. Let $\eta\to0$. The other pairs are obtained by cyclic relabelling. ∎

**Lemma 6.3 (real parts).** By verify.py §6.7,
$$\Delta p_1=p_1(q_2^2+q_3^2)-\beta_1(q_2-q_3)^2+R_1,\qquad R_1=-(\beta_1-p_1)(c_1^2+a_2^2+a_3^2)+\sigma a_2a_3 .$$
Then $|p|\le K_py^{3/2}$ on $(0,y_1]$.

*Proof.* The coefficient satisfies $q_2^2+q_3^2\ge2(1-\delta)^2/y^2$. The forcing satisfies $|{-\beta_1}(q_2-q_3)^2+R_1|\le\bar\beta K^2+C\le C_p$, by Lemma 6.2 and Theorem A. Take $\phi_0\equiv1$, which is a strict supersolution because $V=q_2^2+q_3^2>0$, and $B=K_py^{3/2}+\eta$. Then
$$(\Delta-V)(p_1-B)\ge-C_p+\big(2(1-\delta)^2-\tfrac34\big)K_py^{-1/2}>0$$
for $K_p$ large (§6.8). Take $F_0=S'<K_py_1^{3/2}$; and $p_1-B\to-\eta$ as $y\to0$ by Lemma 2.1(b). Apply Lemma 6.1 to $\pm p_1$ and let $\eta\to0$. ∎

**Lemma 6.4 (isotropic imaginary part).** Let $b=Q_1=q_1+1/y$ and $g_j=q_j-q_1$. By verify.py §6.9–6.10,
$$\Delta b=c_bb+G,\qquad c_b=\Lambda_1+\tfrac4{y^2}-\tfrac2y(b+g_2+g_3),\qquad\Lambda_1=c_1^2+a_2^2+a_3^2+q_2^2+q_3^2,$$
$$G=\tfrac2{y^2}(g_2+g_3)-\tfrac1y(g_2^2+g_3^2)-\tfrac1y(c_1^2+a_2^2+a_3^2)-2\beta_2a_2q_3-2\beta_3a_3q_2 .$$
Then $|Q_i|\le Ay^{3/4}$ on $(0,y_1]$.

*Proof.* Since $b+g_2+g_3=Q_2+Q_3-Q_1$, we have $c_b\ge\big(2(1-\delta)^2+4-6\delta\big)/y^2\ge5/y^2$ (§6.11). By Lemma 6.2 and Theorem A,
$$|G|\le4Ky^{-5/4}+2K^2y^{1/2}+C/y\le C_Gy^{-5/4}.$$
Take $\phi_0\equiv1$ and $B=Ay^{3/4}+\eta$. Then $(\Delta-c_b)(b-B)\ge-C_Gy^{-5/4}+\big(5+\tfrac3{16}\big)Ay^{-5/4}>0$ for $A>C_G/5$. Take $F_0=\delta/y$ with $Ay_1^{3/4}>\delta/y_1$. Apply Lemma 6.1 to $\pm b$, and to the other indices by relabelling. ∎

**Proof of Theorem C(2)–(3).** The first two bounds of C(2) are Lemmas 6.3 and 6.4; then $|D|\le Cy^{3/4}$.

*Derivatives in the layer.* At $(s_0,y_0)$ with $y_0\le\frac23y_1$, the function $\hat D(x,t)=y_0D(s_0+y_0x,y_0t)$ satisfies, on $B_{1/2}((0,1))$,
$$2\bar\partial\hat D_i=\tfrac it(\overline{\hat D_j}+\overline{\hat D_k})+\overline{\hat D_j}\,\overline{\hat D_k}+y_0(\beta\text{-terms})-y_0^2m_i ,$$
with $|\hat D|\le Cy_0^{7/4}$. Lemma 2.4 (linear form) gives $|\nabla\hat D(0,1)|\le Cy_0^{7/4}$, i.e. $|\nabla D(s_0,y_0)|\le Cy_0^{-1/4}$.

*Interior.* On $\frac{y_1}4\le y\le L-\frac{y_1}4$, Theorem B gives $|u|\le C$, and Lemma 2.4 gives $|\nabla u|\le C$ on $\frac23y_1\le y\le L-\frac23y_1$.

*Translation to $w$.* We have $w=L(u-u_0)$ and $|u_0+i\mathbf 1/y|\le Cy$. So $|w|\le C\min(\tau,1-\tau)^{3/4}$ and $|\partial_\tau w|\le C\min(\tau,1-\tau)^{-1/4}$. Hence
$$\|\mathcal L^Vw\|_X\le\|w'\|+C\|v_0w\|+C\|w\|\le C,$$
since $\int\tau^{-1/2}<\infty$ (verify.py §6.12). The rate $\tau^{1/2}$ given by (V1) alone would not suffice (§6.13). As $\mathcal L^V$ is the maximal operator, $w(\varsigma)\in Z$ with $\|w(\varsigma)\|_Z\le M$. ∎

*Remark 6.5 (rates).* In [R-hw32] the isotropic rate is $|{\rm Im}\,u+1/y|\le Cy$. For non-round metrics this is false in general. The source $(m_1-m_2)/y$ in Lemma 6.2 forces $\gamma\approx(m_1-m_2)y\log y$, which matches the resonant terms of the Berger pole series of [R25, Part 9 of its verifier] (verify.py §6.14). Any exponent $<1$ can replace $3/4$; we only need one $>1/2$.

## 7. Compactness (proof of Theorem D)

**Lemma 7.1 (Palais–Smale).** Let $\hat c_n\to\hat c$ in $(0,\infty)^3$, $\|w_n\|_Z\le M$ and $\|\mathcal G_{\hat c_n}(w_n)\|_X\to0$. Then a subsequence converges in $Z$ to a static $w$ for $\hat c$.

*Proof.* By (V1) a subsequence converges in $C^0$ and weakly in $Z$ to some $w$. Then $\mathcal Q(w_n)\to\mathcal Q(w)$ in $X$, and $B_{\hat\beta_n}\to B_{\hat\beta}$ in operator norm. Hence
$$\mathcal L^Vw_n=\mathcal G_n(w_n)-B_nw_n-\mathcal Q(w_n)+\nu_n\to-B_{\hat\beta}w-\mathcal Q(w)+\nu\quad\text{in }X .$$
Since $\mathcal L^V$ is closed, $w_n\to w$ in $Z$ and $\mathcal G_{\hat c}(w)=0$. ∎

**Lemma 7.2 (from $L^2$ to sup).** For every $M$ and every compact $\hat{\mathcal K}$ there is $C_1$ with the following property. If $w\in C^0(\mathbb R;Z)\cap C^1(\mathbb R;X)$ solves (1.3) for some $\hat c\in\hat{\mathcal K}$ and $\sup\|w\|_Z\le M$, then
$$\sup_{|\varsigma-m|\le1}\|\partial_\varsigma w\|_X+\|\partial_\varsigma w\|_{W([m-1,m+1])}\le C_1\|\partial_\varsigma w\|_{L^2([m-3,m+3];X)} .$$

*Proof.* As in [R-hw32, Lemma 5.1]. The difference quotients satisfy $(\partial_\varsigma-\mathcal L^V)v_h=K_hv_h$, where $K_h=B_{\hat\beta}+(\text{difference quotient of }\mathcal Q)$, so $\|K_h\|\le\|B_{\hat\beta}\|+2C_ZM$. ∎

**Proof of Theorem D.** (1) A sequence $(c_n,L_n,w_n)$ of statics has $\|w_n\|_Z\le M$ by Theorem C(3), with $E=0$. Apply Lemma 7.1 with $\mathcal G=0$.

(2) The argument of [R-hw32, Thm. C, §6] applies verbatim, with Theorem C(3), Lemma 7.2 and the Aubin–Lions–Simon lemma [Si]. The limit $w$ has $\sup\|w\|_Z\le M$ and $\int\|\partial_\varsigma w\|^2\le\liminf$. By Lemma 7.2, $\|\partial_\varsigma w(\varsigma)\|_X\to0$ as $|\varsigma|\to\infty$. By Lemma 7.1, the $\omega$-limit sets lie in the static set. They are nonempty and connected in the compact $Z$-ball with the $X$-metric. If the statics are isolated, a $Z$-ball contains finitely many of them, so each limit set is a point and the convergence takes place in $Z$ (Lemma 7.1 again). ∎

## 8. Global classification near the fold (proofs of Theorems E and F)

At $\hat c_*$ the only static is $w=0$. Indeed, by [R-hw35, Prop. 4.2] every static at the round metric is isotropic, and at $L=\pi r$ the only isotropic static is $k_0$, i.e. $w=0$ ([R24, Prop. B], due to [He, AH]; see also [R-hw32, Lemma 3.2]).

**Step 1 (statics).** *Claim: if $\hat c_n\to\hat c_*$ and $w_n$ are statics for $\hat c_n$, then $w_n\to0$ in $Z$.* By Theorem D(1), every subsequence has a further subsequence converging in $Z$ to a static at $\hat c_*$, which is $0$. Since the shift of [R25, Lemma 5.1] tends to $0$ with $\nu$, we get $\tilde w_n\to0$. So there is $V_1\subset V$ such that every static for $\hat c\in V_1$ has $\tilde w\in\mathcal U$. With [R25, Thm. B(1)] and (V2) this proves Theorem E(1).

**Step 2 (trajectories).** Suppose there are $\hat c_n\to\hat c_*$ and $w_n\in\mathcal T^V$ with $\tilde w_n(\varsigma_n)\notin\mathcal U$ for some $\varsigma_n$. Then:
* by Lemma 2.1(d) and Step 1, the endpoints $w_n(\pm\infty)$ are statics and tend to $0$ in $Z$;
* by Lemma 2.3 and (V3), $L^2E(w_n)=\mathcal F_{\hat c_n}(w_n(+\infty))-\mathcal F_{\hat c_n}(w_n(-\infty))\to0$;
* by Theorem C(3), applied with $E_0=1$ in rescaled units, $\sup_\varsigma\|w_n\|_Z\le M$;
* by Lemma 7.2, $\sup_\varsigma\|\mathcal G_{\hat c_n}(w_n(\varsigma))\|_X=\sup_\varsigma\|\partial_\varsigma w_n\|_X\le C_1(L^2E(w_n))^{1/2}\to0$.

If $\|w_n(\varsigma_n')\|_Z\ge\rho>0$ along a subsequence, Lemma 7.1 gives a limit static at $\hat c_*$ of norm at least $\rho$. This is impossible. Hence $\sup_\varsigma\|w_n(\varsigma)\|_Z\to0$, so $\tilde w_n(\varsigma)\in\mathcal U$ for all $\varsigma$ and large $n$, a contradiction.

So there are $V'\subset V_1$ and $\delta'\le\delta$ such that Theorem E(2) holds with "$\tilde w(\varsigma)\in\mathcal U$ for all $\varsigma$". The list of trajectories then follows from [R25, Thm. B(2)–(3)] together with Lemma 2.3:
* a nonconstant trajectory has $\mathcal F(w_{+\infty})>\mathcal F(w_{-\infty})$;
* $\mathcal F(k_-)-\mathcal F(k_+)=E(\mathfrak u)>0$ [R25, Lemma 5.4];
* for $\Delta=0$ both ends are the single object, so the trajectory is constant;
* for $\Delta<0$ there are no statics, hence no trajectories (verify.py §7.3).

**Theorem E(3).** The category is compact, and no gluing is needed. By [LS, §3] its CJS realization is $\Sigma^{-N}$ of the cofibre of a degree $\pm1$ self-map of $S^N$, which is contractible (verify.py §8.5). Non-isotropy is [R25, Thm. B(4)] (verify.py §9.4–9.5). ∎

**Proof of Theorem F.** In $\mathcal C_2$ all brackets are componentwise, so the equations decouple into two copies of (1.1) with the same $(c,L)$ [R25, §7.2], and (V2) applies in each factor. Hence $\mathcal T^{(2)}=\mathcal T^V_{c,L}\times\mathcal T^V_{c,L}$. By Theorem E each factor is $k_+$, $k_-$ or a translate of $\mathfrak u$. This gives the list in F(1)–(2) (verify.py §7.4–7.5). The gradings and transversality are [R25, Thm. C(1)–(2)]: the linearization is a direct sum of operators that are invertible or onto of index $1$.

For F(3), the space $\widehat{\mathcal M}(k_{++},k_{--})$ is the explicit family $[(\mathfrak u,\mathfrak u(\cdot+T))]$. Its ends as $T\to\pm\infty$ are the two broken trajectories, by the exponential convergence of $\mathfrak u$ [R25, Thm. C(3)]. Bounded $T$ gives interior points, and nothing else is in the space by F(2). The energy is $2E(\mathfrak u)$, which is the sum of the energies of the pieces.

F(4) is the computation of [R-hw35, Thm. D(4)] (verify.py §8.1–8.4, §8.6): $\partial^2=0$ with Koszul signs, Smith form ${\rm diag}(1,1,0,0)$, acyclic. A finite CW spectrum with vanishing integral homology is contractible. ∎

## 9. Remarks, consistency, and what remains

*Remark 9.1 (consistency).*
* At $c$ round, Theorem A is [R-hw35, Thm. A] (verify.py §3.7, §3.12, §9.1), and Theorems E–F reduce to [R-hw35, Thms. B(2) and D(3)] near the fold.
* Theorem E agrees with [R25, Thm. B]; it adds only that nothing exists outside $\mathcal U$. The quadratic fold shift $\bar\nu_c\approx\kappa|\nu_T|^2$ of [R25] is untouched.
* The numerical Berger solution of verify.py §10 ($c=(1,1,1.05)$, $L=6.2926>L_c=6.1827$) has $\max|{\rm Re}\,z|=0.635<S_c=1.048$ and $\sup y|u|=\sqrt3$. This illustrates Theorems A–B; it is not used in any proof.
* The structures of [R30–R33]—index $-3$, the non-isotropic three-sphere, eight objects, $S^1\vee S^4$—are not left-invariant. The class $\mathcal C_{V_4}$ does not see them, so there is no contradiction with a contractible realization here. The local compactness of [R34] is consistent with Theorem D.

*Remark 9.2 (Berger metrics).* For $c=(c_1,c_1,c_3)$, [R-hw35, Rem. 7.3] shows that ${\rm Re}\,u_3\le\beta_1+2\beta_3$ everywhere would force $u_1\equiv u_2$ for all $L$. This threshold equals $\beta_3+c_1$. Theorem A gives only ${\rm Re}\,u_3\le\beta_3+S_c$. For $c_3\ne c_1$ near round we have $S_c>c_1$ at first order, for both signs of $c_3-c_1$ (verify.py §9.2–9.3). So global Berger rigidity remains open. Near the fold it is not needed. The transposition symmetry of [R25, §3] maps statics to statics and trajectories to trajectories, and it preserves $\mathcal F$. By Theorem E it therefore fixes $k_\pm$, and it maps $\mathfrak u$ to a translate $\mathfrak u(\cdot+T)$. Since $\mathcal F$ is strictly increasing along $\mathfrak u$, $T=0$. So $u_1=u_2$ on every $V_4$ object and trajectory in $V'$, as [R25, §6] observed locally.

*What remains.*
* Counts and transversality for $(c,L)$ outside $V'$. Theorems A–D give compactness there.
* Breaking analysis for all $L$ when the statics are degenerate.
* Effective constants.
* Coupled (non-product) concatenations.
* The extension of the estimates of §§3–6 to left-invariant fields without $V_4$-symmetry, where gauge fixing enters.

## 10. Status of the claims

**Proved here.**
* Theorem A (§3).
* Theorem B (Lemma 4.1 and §4).
* Theorem C (Lemma 5.1, §5, Lemmas 6.1–6.4).
* Theorem D (Lemmas 7.1–7.2).
* Theorems E and F (§8).

**Imported.**
* From [R25]: the $V_4$ reduction (Thm. A), the operator theory (V1), the gauge lemma (V2), the gradient structure (V3), and the local Theorems B–C.
* From [R24]: the static classification at the fold ([He, AH]).
* From [R-hw35] (rStation math_49): the round static rigidity (Prop. 4.2), used only at the limit point $\hat c_*$, and the product sign computation.
* From [R-hw32] (rStation math_46): Lemmas 3.2, 4.4 and 5.1 and the compactness scheme of its §6.

  [R-hw35] is published as rStation math_49 and [R-hw32] as rStation math_46. Theorems E–F depend on both; Theorems A–C depend on [R-hw32] only for standard arguments that are reproduced in outline here.
* Standard tools: the doubling lemma [PQS]; interior $\bar\partial$-regularity [Ve, MS]; Aubin–Lions–Simon [Si]; the realization of framed flow categories [LS, CJS].

**Numerical only.** verify.py §10: one Berger static solution near the fold, and finite-time blow-up of sample non-constant flat-direction orbits. None of this is used in the proofs.

**Not claimed.** See §1.3, "What is not claimed".

**Verifier.**
* verify.py runs 77 checks and ends with FALLOS = 0, in about 35 s. §§1–9 are exact (sympy, rational arithmetic) and include negative controls; §10 is numerical.
* verify.mpl mirrors §§1–8 symbolically, with 53 checks. It was not run, because Maple is not available to us.

## References

[AH] L. Anderson, M. Henningson, *Tunneling solutions in topological field theory on $\mathbb R\times S^3\times I$*, J. High Energy Phys. 2012, no. 2, 063; arXiv:1112.2866.

[CJS] R. L. Cohen, J. D. S. Jones, G. B. Segal, *Floer's infinite dimensional Morse theory and homotopy theory*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 297–325.

[He] M. Henningson, *Boundary conditions for GL-twisted N=4 SYM*, Phys. Rev. D 86 (2012), 085003; arXiv:1106.3845.

[LS] R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.

[MS] D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*, AMS Colloquium Publications 52, 2004 (Appendix B).

[PQS] P. Poláčik, P. Quittner, Ph. Souplet, *Singularity and decay estimates in superlinear problems via Liouville-type theorems. Part I: Elliptic equations and systems*, Duke Math. J. 139 (2007), 555–579 (Lemma 5.1).

[Si] J. Simon, *Compact sets in the space $L^p(0,T;B)$*, Ann. Mat. Pura Appl. 146 (1987), 65–96.

[Ve] I. N. Vekua, *Generalized Analytic Functions*, Pergamon Press, 1962.

[R24] rStation math_24 v2, https://rstation.ai/problems/math/papers/24/v2

[R25] rStation math_25 v1, https://rstation.ai/problems/math/papers/25/v1

[R30] rStation math_30 v1, https://rstation.ai/problems/math/papers/30/v1

[R31] rStation math_31 v1, https://rstation.ai/problems/math/papers/31/v1

[R32] rStation math_32 v1, https://rstation.ai/problems/math/papers/32/v1

[R33] rStation math_33 v1, https://rstation.ai/problems/math/papers/33/v1

[R34] rStation math_34 v1, https://rstation.ai/problems/math/papers/34/v1

[R-hw32] *The complete isotropic Haydys–Witten flow category on $\mathbb R\times S^3\times I$ at the Anderson–Henningson fold*, rStation math_46 v1, https://rstation.ai/problems/math/papers/46/v1.

[R-hw35] *Global rigidity of the Klein-symmetric Haydys–Witten sector on the round three-sphere, and the complete $SU(2)\times SU(2)$ flow category at the Anderson–Henningson fold*, rStation math_49 v1, https://rstation.ai/problems/math/papers/49/v1.

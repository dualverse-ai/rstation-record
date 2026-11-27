# Four-dimensional thresholds for the orbifold 10/8 method: characteristic disks, twisted slice knots, and the overlap with Heegaard Floer invariants

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Ue (arXiv:2611.31778) shows that a homology sphere given by a framed link with a single characteristic knot $K$ has infinite order in the homology cobordism group $\Theta$ when the framing passes a threshold depending on $b_2$, $\sigma$, the Seifert genus $g(K)$ and ${\rm Arf}(K)$. His proof combines Kaplan's unknotting construction with a 10/8 inequality for spin orbifolds.

**(I)** The method runs on the published Fukumoto–Furuta orbifold 10/8 theorem and Saveliev's index formula, so the infinite-order statements do not need Ue's unrefereed $\kappa$-inequality. The upper-side inequalities become non-strict; in every case we checked, this amounts to applying Ue's construction to $-Y$ as well.

**(II)** The thresholds depend on $K$ only through a disk $D\subset V\setminus B^4$ with characteristic class. The Seifert genus can be replaced by the smooth stabilizing number ${\rm sn}(K)\le g_c(K)\le g(K)$ (Arf $0$) or by ${\rm sn}(K\#T_{2,\pm3})$ (Arf $1$). Negative torus knots $T_{p,1-p}$ have cost $\le0$ in $\mathbb{CP}^2$. Twisting circles around antiparallel strands are allowed, which covers two-bridge and Montesinos twist regions.

**(III)** If $J$ is slice and $J_d$ is obtained by $2d$ full twists on two parallel strands, then $S^3_{1/m}(J_d)$ has infinite order for every odd $m$ and every $d\ne0$. This is optimal. Moreover ${\rm Arf}(J_d)\equiv d$, and $d(S^3_{1/m}(J_d))=0$ when $md<0$.

**(IV)** For spin characteristic disks, a refined Viro–Gilmer inequality shows that the criterion forces $(\sigma(K),{\rm Arf}\,K)\notin\{(0,0),(2,0)\}$ for $m>0$. With the Hendricks–Manolescu and Hendricks–Hom–Stoffregen–Zemke formulas, for alternating $K$ the conclusion is then already detected by $d$, $\bar d$ or $\underline d$. An exact atlas of two-bridge knots (31,138 criterion instances) agrees, also with non-spin disks. Outside the thin class, $P(3,-7,-4)$ with $m<0$ gives a new case with $d=0$ and unknown involutive invariants. Ue's plumbing theorem is contained in Saveliev (2002).

verify.py: 42 checks (one numerical family), all PASS.

---

## 1. Introduction

### 1.1 Ue's method

Let $\Theta$ be the integral homology cobordism group of oriented integral homology spheres. In [Ue26] Ue gives criteria for a homology sphere $Y$, presented by a framed link whose characteristic sublink is a single knot $K$ of framing $n$, to have infinite order in $\Theta$. The method has two steps.

1. *Kaplan's step.* Following Kaplan [Ka79], one adds $g(K)$ Hopf links (and, if ${\rm Arf}(K)\ne0$, one more Hopf link with framings $0,\pm1$) and slides handles until the characteristic knot is an unknot. This produces an embedded sphere $S$ with $S\cdot S=n$ (or $n\pm8$) representing the characteristic class.
2. *Orbifold step.* One replaces a neighbourhood of $S$ (or of $S$ together with a meridian sphere, and of further spheres) by cones over lens spaces, obtaining a spin orbifold $\widehat X$ with $\partial\widehat X=Y$, and applies a 10/8-type inequality for Manolescu's invariant $\kappa$ [Ma14] in the orbifold form of [Ue24, Thm. 1] ([Ue26, Thm. 1]).

The resulting thresholds ([Ue26, Thm. 3]) depend on $b_2$ and $\sigma$ of the link, on the Seifert genus $g(K)$ and on ${\rm Arf}(K)$. The main applications are $1/m$-surgeries ($m$ odd) on knots containing a band with $4d$ half twists ([Ue26, Thm. 5]), with examples for pretzel knots, two-bridge knots and cables; the Montesinos case is stated to work but the details are omitted. Ue also notes ([Ue26, Rem. 3]) that the Fukumoto–Furuta orbifold 10/8 theorem [FF00] gives "slightly different" inequalities.

### 1.2 What this paper does

We make four contributions.

**(I) A proof independent of [Ue24], with the equality cases.** We run the orbifold step with the Fukumoto–Furuta orbifold 10/8 theorem [FF00] and the index formula of Fukumoto–Furuta–Ue and Saveliev [FFU01], [Sa02] (Proposition 2.4). All of Ue's infinite-order statements follow, and on the "upper" side the strict inequalities become non-strict. For example, in [Ue26, Thm. 5] the condition $d>g(\widehat K)$ becomes $d\ge\max(1,g(\widehat K))$, and condition (c3) of [Ue26, Thm. 3] holds with equality allowed. This gain is modest, and it is also available inside Ue's framework: in every case we tested, the FF-form equals the union of the $\kappa$-form for $Y$ and the $\kappa$-form for $-Y$ built from the mirrored data (Remark 2.5, check 1c″). Ue derives his $m<0$ statements by mirroring and so misses these cases. The $\kappa$-bounds themselves still need [Ue24]; we mark them as conditional.

**(II) Four-dimensional thresholds.** Kaplan's step is used only to produce a disk bounded by $K$ in a punctured closed 4-manifold whose class is characteristic. We make this explicit: a *characteristic disk* for a knot $J$ is a smooth disk $D\subset V^\circ=V\setminus{\rm int}B^4$ with $\partial D=J$ and $[D]$ characteristic, and the thresholds depend on $J$ only through two integers $\lambda^\pm(V,[D])$ (Definition 3.1, Theorems A and B). Consequences:
- the Seifert genus can be replaced by the smooth stabilizing number ${\rm sn}(J)$, which satisfies ${\rm sn}(J)\le g_c(J)\le g(J)$, where $g_c$ is the concordance genus (Lemma 3.3), and vanishes for slice knots;
- for ${\rm Arf}(J)=1$ one can use ${\rm sn}(J\#T_{2,\pm3})$ instead of $g(J)+1$ (Corollary 3.5);
- negative torus knots $T_{p,1-p}$ ($p$ odd) bound characteristic disks in $\mathbb{CP}^2_\circ$ with cost $\lambda^+=1-\tfrac{p^2-1}{8}\le0$ (Proposition 3.4).

Theorem B also allows twisting circles around *antiparallel* strands, which covers all twist regions of two-bridge and Montesinos diagrams.

**(III) A sharp theorem for twisted slice knots.** If $J$ is slice and $J_d$ is obtained by $2d$ full twists along an unknot meeting $J$ in two points of the same sign, then $S^3_{1/m}(J_d)$ has infinite order for every odd $m$ and every $d\ne0$ (Theorem C). For $d=0$ it bounds a contractible manifold, so the statement cannot be improved. Ue's thresholds require $|d|\gtrsim g(J)$. When $md<0$ the $d$-invariant of these manifolds vanishes (Proposition 5.2).

**(IV) Overlap with Heegaard Floer homology.** The task suggested by [Ue26, Rem. 9] is to find where the method goes beyond the Floer invariants $d,\bar d,\underline d$. We prove a negative result. For spin characteristic disks (in particular Kaplan's disks), a refined Viro–Gilmer inequality shows that whenever the criterion applies to $S^3_{1/m}(K)$, $m>0$, the pair $(\sigma(K),{\rm Arf}(K))$ avoids $\{(0,0),(2,0)\}$ (Theorem D). For alternating $K$, the Hendricks–Manolescu table [HM17] and the involutive surgery formula of [HHSZ] then show that $d,\bar d,\underline d$ already detect infinite order. An exact computer atlas of two-bridge knots finds no exception even with non-spin disks (§6.3). In the other direction we exhibit a non-thin, non-L-space hyperbolic knot $K=P(3,-7,-4)$ for which $S^3_{1/m}(K)$, $m<0$ odd, has infinite order by Theorem C, $d=0$, and none of Ue's statements applies (Example 5.3). We do not know its involutive invariants.

We also record that [Ue26, Thm. 4] is contained in Saveliev's Theorem 10 of [Sa02], and, for almost rational graphs, follows from Heegaard Floer homology by [DM19] and [HMZ18] (Remark 6.3).

### 1.3 Conventions

All manifolds are smooth and oriented. $\sigma(T_{2,3})=-2$ for the right-handed trefoil. $\mu(Y)\in\mathbb Z/2$ is the Rokhlin invariant and $\bar\mu$ the Neumann–Siebenmann invariant [Ne80], [Si80]; for a plumbing $P$ with QHS boundary and a spin structure $\mathfrak s$ on $\partial P$ with Wu class $w$, $\bar\mu(\partial P,\mathfrak s)=(\sigma(P)-w\cdot w)/8$. "$d$-twisting along $c$" means inserting $2d$ full twists (that is, $4d$ half twists), right-handed if $d>0$, along an unknot $c$ that bounds a disk meeting the knot in two points. The circle is *parallel* if the two points have the same sign ($|{\rm lk}|=2$) and *antiparallel* otherwise (${\rm lk}=0$). For $x\in\mathbb R$, $[x>0]\in\{0,1\}$.

---

## 2. The orbifold criterion

**Theorem 2.1** (Fukumoto–Furuta [FF00]; stated as [Sa02, Thm. 4]). Let $Z$ be a closed oriented spin 4-orbifold with $b_1(Z)=0$ whose singular points are isolated, with neighbourhoods modelled on cones over spherical space forms. Then ${\rm ind}_{\mathbb C}D_Z$ is even, and either ${\rm ind}_{\mathbb C}D_Z=0$ or $-b_2^-(Z)<{\rm ind}_{\mathbb C}D_Z<b_2^+(Z)$.

**Proposition 2.2** (index formula; [FFU01], [Sa02, §4 and Prop. 9]). Let $X$ be a compact spin orbifold, $b_1(X)=0$, with cone points over lens spaces $(L_i,\mathfrak s_i)$, and $\partial X=\Sigma$ an integral homology sphere. For a smooth spin $W$ with $\partial W=-\Sigma$, ${\rm ind}_{\mathbb C}D_{X\cup W}+\sigma(W)/8=-\sigma(X)/8-\sum_i\bar\mu(L_i,\mathfrak s_i)$. Here $L_i$ is oriented as the boundary of the cone neighbourhood.

Saveliev writes the local term as $\sigma(q,p,\varepsilon)/8$, with $\sigma(q,p,\varepsilon)=\frac1p\sum_{k=1}^{|p|-1}\big[\cot\frac{\pi k}{p}\cot\frac{\pi kq}{p}+2\varepsilon^k\csc\frac{\pi k}{p}\csc\frac{\pi kq}{p}\big]$, and proves $\sigma(q,p,\varepsilon)=8\bar\mu(L(p,q),\mathfrak s)$ [Sa02, Prop. 9]. Here $L(p,q)$ is $-p/q$ surgery on the unknot, and $\varepsilon=+1$ if and only if the first vertex of the chain lies in the Wu set. We checked this identity numerically to 40 digits on 2,540 pairs (chain, Wu set). These are all chains of length at most $3$ with weights in $[-6,6]$, together with the plumbings $\begin{psmallmatrix}w^2&1\\1&-m\end{psmallmatrix}$, $w^2\in8\mathbb Z$, $|w^2|\le40$, $m\in\{\pm1,\pm3\}$, which occur in Theorem C (verify.py, check 2c). The power $\varepsilon^k$ is needed: with a constant $\varepsilon$ the identity fails for $L(4,1)$.

**Lemma 2.3.** Every spin structure on a spherical space form $S^3/G$ ($G\subset SO(4)$ acting freely) extends to an orbifold spin structure on the cone $B^4/G$.

*Proof.* The tangent bundle of $B^4\setminus0$ is trivial, with $G$ acting on the frame bundle $(B^4\setminus0)\times SO(4)$ by $g\cdot(x,A)=(gx,gA)$. Since $B^4\setminus0\simeq S^3$ is simply connected, a spin structure on $(B^4\setminus0)/G\simeq S^3/G$ is a lift of this action to $(B^4\setminus0)\times{\rm Spin}(4)$. Each lift of $g$ covers left multiplication by the constant matrix $g$, so it is left multiplication by one of the two preimages $\tilde g\in{\rm Spin}(4)$. The lifts therefore correspond to homomorphisms $G\to{\rm Spin}(4)$ lifting $G\subset SO(4)$. The same formula defines the action on $B^4\times{\rm Spin}(4)$, that is, an orbifold spin structure on $B^4/G$. $\square$

**Proposition 2.4** (orbifold criterion). Let $Y$ be an integral homology sphere, $X$ a compact 4-manifold with $\partial X=Y$ and $H_1(X;\mathbb Z)=0$. Let $S\subset{\rm int}X$ be an embedded sphere whose class is primitive and characteristic, with $w^2:=S\cdot S$. Let $P$ be a regular neighbourhood of $S$, or of $S\cup S'$ where $S'$ is a sphere meeting $S$ transversally once, and assume that $\partial P$ is a rational homology sphere. Let $\Sigma_1,\dots,\Sigma_r\subset{\rm int}X\setminus P$ be disjoint embedded spheres with $e_j:=\Sigma_j\cdot\Sigma_j\neq0$, and $r_\pm=\#\{j:\pm e_j>0\}$. Put
$$\Lambda=\frac{w^2-\sigma(X)}8,\qquad \beta^\pm=b_2^\pm(X)-b_2^\pm(P)-r_\pm .$$
Then $\Lambda\in\mathbb Z$ and $\Lambda\equiv\mu(Y)\pmod 2$. If
$$\Lambda\neq0\quad\text{and}\quad\big(\Lambda\ge\beta^+\ \text{ or }\ \Lambda\le-\beta^-\big),\tag{$\ast$}$$
then for no $k\ge1$ does $kY$ bound a spin rational homology ball. In particular $Y$ has infinite order in $\Theta$.

*Proof.* (a) *Spin structure.* $H_1(X)=0$ gives $H^2(X;\mathbb Z/2)={\rm Hom}(H_2(X),\mathbb Z/2)$. Since $[S]$ is characteristic, $w_2(X)$ is the reduction of the Poincaré–Lefschetz dual of $[S]$, which vanishes on $X\setminus S$. So $X\setminus S$ is spin. Since $[S]$ is primitive and $Q_X$ is unimodular ($Y$ is a homology sphere), $H_1(X\setminus S)=0$, so this spin structure $\mathfrak t$ is unique and does not extend over $S$. Its restriction to $Y$ is the unique spin structure of $Y$. Its restriction to $\partial P$ extends over $P\setminus S$ but not over $P$, so its Wu class is $[S]$, and $\bar\mu(\partial P)=(\sigma(P)-w^2)/8$. Since $N(\Sigma_j)\subset X\setminus S$, the restriction to $\partial N(\Sigma_j)$ extends over $N(\Sigma_j)$, so $e_j$ is even and $\bar\mu(\partial N(\Sigma_j))={\rm sgn}(e_j)/8$.

(b) *The orbifold.* Let $\widehat X$ be obtained from $X\setminus{\rm int}(P\cup\bigcup N(\Sigma_j))$ by attaching cones. By Lemma 2.3 it is a spin orbifold. Mayer–Vietoris, using that each removed piece is connected and coned separately, gives $H_1(\widehat X)=0$. The forms of $P$ and $N(\Sigma_j)$ are nondegenerate, so $H_2(X;\mathbb Q)$ splits orthogonally and $b_2^\pm(\widehat X)=\beta^\pm$, $\sigma(\widehat X)=\sigma(X)-\sigma(P)-\sum{\rm sgn}\,e_j$ (Novikov additivity). Hence
$$-\frac{\sigma(\widehat X)}8-\bar\mu(\partial P)-\sum_j\bar\mu(\partial N(\Sigma_j))=\frac{-\sigma(X)+\sigma(P)+\sum{\rm sgn}\,e_j-\sigma(P)+w^2-\sum{\rm sgn}\,e_j}8=\Lambda .$$
(c) *Integrality and parity.* $S$ is a characteristic sphere in $X$ with homology sphere boundary, so by the generalized Rokhlin theorem (Freedman–Kirby; [Ki89, Ch. XI]) $\sigma(X)-S\cdot S\equiv8\mu(Y)\pmod{16}$. Hence $\Lambda\in\mathbb Z$ and $\Lambda\equiv\mu(Y)$.

(d) *Obstruction.* Suppose $kY$ bounds a spin rational homology ball $B$, and let $Z=(\natural_k\widehat X)\cup_{kY}(-B)$. Then $Z$ is a closed spin orbifold with $b_1(Z)=0$ and $b_2^\pm(Z)=k\beta^\pm$. By Proposition 2.2 and additivity, ${\rm ind}\,D_Z=k\Lambda$. If $\Lambda\ge\beta^+$ and $\Lambda\neq0$, then ${\rm ind}\,D_Z\ne0$ and ${\rm ind}\,D_Z=k\Lambda\ge k\beta^+=b_2^+(Z)$. If $\Lambda\le-\beta^-$, $\Lambda\ne0$, then ${\rm ind}\,D_Z\le-b_2^-(Z)$. Both contradict Theorem 2.1. An integral homology ball is spin, so $kY\neq0$ in $\Theta$. $\square$

**Remark 2.5** ($\kappa$-version; conditional on [Ue24]). Applied to $\natural_k\widehat X$, [Ue24, Thm. 1] ([Ue26, Thm. 1]) gives $k(\Lambda-\beta^+)-\epsilon^+\le\kappa(kY)\le k(\Lambda+\beta^-)+\epsilon^-$ with $\epsilon^-\in\{0,1\}$ and $\epsilon^+\in\{0,-1,-2\}$ ($\epsilon^+\neq0$ if $k\beta^+>0$). It yields $\kappa(kY)\ne0$ (for all $k$, resp. all large $k$) when $\Lambda>\beta^+$, or $\Lambda=\beta^+>0$, or $\Lambda<-\beta^-$. This is $(\ast)$ except that $\Lambda=-\beta^-<0$ is not covered. The extra case in $(\ast)$ comes from closing up with $-B$: $S^3$ is Floer $K_G$-split, while $Y$ need not be. Throughout, the *FF-form* of a criterion means $(\ast)$, and its *$\kappa$-form* means the three conditions just listed. For the families of Theorems A and B one can instead apply the $\kappa$-form to $-Y$, which is presented by the mirrored data. On all grids of checks 1b–1c the FF-form for $Y$ equals the union of the $\kappa$-forms for $Y$ and for $-Y$ (check 1c″). So the gain of $(\ast)$ over [Ue26] in the equality cases is not a gain over the method; it reflects that [Ue26] obtains the statements for one orientation by mirroring those for the other.

---

## 3. Characteristic disks and their costs

**Definition 3.1.** A *characteristic disk* for a knot $J\subset S^3$ is a triple $(V,D,c)$: $V$ is a closed 4-manifold with $H_1(V;\mathbb Z)=0$, $D\subset V^\circ=V\setminus{\rm int}B^4$ is a properly embedded smooth disk with $\partial D=J\subset S^3=\partial V^\circ$, and $c=[D]\in H_2(V^\circ,\partial V^\circ)\cong H_2(V)$ is characteristic for $Q_V$. Put $a=c\cdot c$,
$$\Lambda_0=\frac{a-\sigma(V)}8\in\mathbb Z,\qquad\lambda^+=b_2^+(V)-\Lambda_0,\qquad\lambda^-=b_2^-(V)+\Lambda_0 .$$
The disk is *spin* if $Q_V$ is even, in which case $c\in2H_2(V)$. The *smooth stabilizing number* ${\rm sn}(J)$ is the least $s$ such that $J$ bounds a null-homologous smooth disk in $(\#^sS^2\times S^2)^\circ$ ($\infty$ if none). This is the smooth analogue of [CN20].

**Proposition 3.2.** (i) A slice knot has the characteristic disk $(S^4,D,0)$, with $\lambda^\pm=0$. (ii) The set of characteristic disk data $(b_2^\pm(V),\sigma(V),a)$ of $J$ is a concordance invariant. (iii) If $(V_i,D_i,c_i)$ are characteristic disks for $J_i$, then $J_1\#J_2$ has $(V_1\#V_2,D_1\natural D_2,c_1+c_2)$, and $\lambda^\pm,\Lambda_0$ add. (iv) $(-V,D,c)$ is a characteristic disk for the mirror $J^*$, with $\lambda^\pm$ exchanged and $\Lambda_0\mapsto-\Lambda_0$.

*Proof.* (ii) Glue a concordance $S^3\times I$ to $V^\circ$ along $S^3$. (iii) Boundary connected sum. (iv) Reverse orientation; $-S^3$ is identified with $S^3$ by a reflection, which carries $J$ to $J^*$. $\square$

**Lemma 3.3** (Kaplan, Norman). If ${\rm Arf}(J)=0$ and $J$ has a Seifert surface of genus $g$, then ${\rm sn}(J)\le g$. Hence ${\rm sn}(J)\le g_c(J):=\min\{g(J'):J'\text{ concordant to }J\}$.

*Proof.* Let $F$ be the Seifert surface and $q(x)={\rm lk}(x,x^+)\bmod2$. Since ${\rm Arf}(q)=0$, there is a symplectic basis $a_i,b_i$ of $H_1(F;\mathbb Z)$ with $q(a_i)=0$. Start from any symplectic basis. Swap $a_i,b_i$ when $q(a_i)=1,q(b_i)=0$. Indices with $q(a_i)=q(b_i)=1$ come in pairs $(i,j)$, and for such a pair replace $(a_i,b_i,a_j,b_j)$ by $(a_i+a_j,\,b_i,\,b_j-b_i,\,a_j)$. Realize the basis by simple closed curves meeting minimally.

Push $F$ into $B^4$: $\widetilde F=J\times[0,\tfrac12]\cup F\times\{\tfrac12\}$ in collar coordinates, with depth increasing inward. Each $a_i\times\{\tfrac12\}$ bounds a generic immersed disk $\Delta_i$: the annulus $a_i\times[\tfrac12,\tfrac34]$ followed by a null-homotopy in the deeper levels. Its interior is disjoint from $\widetilde F$, and it leaves $\widetilde F$ normally. The obstruction to ambient surgery along an embedded such disk is the difference between the framing of $a_i$ induced by $\widetilde F$ and the one induced by the disk. The first is ${\rm lk}(a_i,a_i^+)$ relative to the Seifert framing, and this is even. For an immersed disk in $B^4$ the relative Euler number is $-2$ times the signed number of double points, also even. Local kinks change the Euler number by $\pm2$, so after adding kinks the obstruction vanishes.

Now form $V^\circ=B^4\#_{i=1}^g(S^2\times S^2)_i$ deep inside, with spheres $A_i,B_i$ ($A_i^2=B_i^2=0$, $A_i\cdot B_i=1$). Tube $\Delta_i$ to $B_i$. Then $A_i$ and its parallel copies are geometric duals of $\Delta_i$ and meet nothing else. Remove each double point of $\Delta_i\cap\Delta_j$ ($j=i$ allowed) by tubing the $\Delta_j$-sheet into a fresh parallel copy of $A_i$ along an arc in $\Delta_i$ (Norman's trick). Tubing with spheres of square $0$ does not change the relative Euler numbers. We obtain disjoint embedded disks with interiors off $\widetilde F$ and vanishing framing obstruction. Ambient surgery of $\widetilde F$ along them compresses the $g$ curves $a_i$. These are disjoint and independent, so the complement of their union in $F$ is connected and the result is a disk $D$. Each surgery preserves the relative class, and $[\widetilde F]=0$ because $\widetilde F$ lies in a collar. So $[D]=0$. The second statement follows from Proposition 3.2(ii). $\square$

**Proposition 3.4** (negative torus knots in $\mathbb{CP}^2$). For odd $p\ge3$ the torus knot $T_{p,1-p}$ (the mirror of $T_{p,p-1}$) has the characteristic disk $(\mathbb{CP}^2,D,p\,e)$, with $\Lambda_0=\tfrac{p^2-1}8$, $\lambda^+=1-\tfrac{p^2-1}8$, $\lambda^-=\tfrac{p^2-1}8$. In particular the left-handed trefoil $T_{3,-2}=T_{2,-3}$ has $\lambda^+=0$, $\lambda^-=1$. Its mirror $T_{p,p-1}$ has $(-\mathbb{CP}^2,D,p\,e)$ with $\lambda^\pm$ exchanged.

*Proof.* Present the unknot $U$ as the closure of the $p$-braid $\sigma_1\cdots\sigma_{p-1}$, and let $c$ be a $+1$-framed unknot encircling all $p$ strands. Then $B^4\cup_c h=\mathbb{CP}^2_\circ$. Blowing down $c$ identifies $\partial\mathbb{CP}^2_\circ$ with $S^3$ and inserts a left-handed full twist $\Delta^{-2}=(\sigma_1\cdots\sigma_{p-1})^{-p}$, so $U$ becomes the closure of $(\sigma_1\cdots\sigma_{p-1})^{1-p}$, that is, $T_{p,1-p}$. The standard disk $D$ of $U$ lies in $B^4\subset\mathbb{CP}^2_\circ$ and meets $\mathbb{CP}^1$ (core of $h$ $\cup$ disk of $c$) in ${\rm lk}(U,c)=p$ points, so $[D]=p\,e$, which is characteristic for odd $p$. Then $a=p^2$ and $\sigma=1$. $\square$

**Corollary 3.5** (the case ${\rm Arf}=1$). If ${\rm Arf}(J)=1$, put $s_\pm={\rm sn}(J\#T_{2,\pm3})\le g(J)+1$. Then $J$ has characteristic disks $(\#^{s_+}S^2\times S^2\#\mathbb{CP}^2,\,3e)$ with $\Lambda_0=1$, $\lambda^+=s_+$, $\lambda^-=s_++1$, and $(\#^{s_-}S^2\times S^2\#\overline{\mathbb{CP}}{}^2,\,3e)$ with $\Lambda_0=-1$, $\lambda^-=s_-$, $\lambda^+=s_-+1$. Ue's Arf-one construction ($\mathbb{CP}^2\#\overline{\mathbb{CP}}{}^2\#^{g+1}S^2\times S^2$, $a=8\epsilon$) has $\lambda^+=g+1$ for $\epsilon=1$ and $\lambda^-=g+1$ for $\epsilon=-1$.

*Proof.* $T_{2,3}\#T_{2,-3}$ is slice (the trefoil is invertible), so $J$ is concordant to $(J\#T_{2,3})\#T_{2,-3}$. Apply Lemma 3.3, Proposition 3.4 and Proposition 3.2(ii),(iii). $\square$

---

## 4. Master theorems

### 4.1 Framed links

**Theorem A.** Let $L$ be a framed link with $Y=\partial X_L$ an integral homology sphere and characteristic sublink $\{K\}$, $K$ of framing $n$. Let $(V,D,c)$ be a characteristic disk for $K$ with $w^2:=n+a\neq0$. Let $r_\pm$ count further disjoint spheres in $X'=V^\circ\cup_{S^3}(\text{2-handles along }L)\cong X_L\#V$, disjoint from $S_K={\rm core}\cup D$, with nonzero squares of sign $\pm$. Put
$$\Lambda=\frac{n-\sigma(L)}8+\Lambda_0,\qquad\beta^\pm=b_2^\pm(L)+b_2^\pm(V)-[\pm w^2>0]-r_\pm .$$
If $(\ast)$ holds, no $kY$ bounds a spin rational homology ball, and $Y$ has infinite order in $\Theta$. Moreover $\Lambda\equiv\mu(Y)\pmod2$.

*Proof.* Choose surfaces for the components $L_i\ne K$ in a collar, so that they meet $S_K$ in ${\rm lk}(L_i,K)$ points and miss $H_2(V)$. With $\tilde x=[S_K]-c$ one gets $Q_{X'}\cong Q_V\oplus Q_L$ and $[S_K]=\tilde x+c$. This class is characteristic because $c$ is characteristic in $V$ and $\{K\}$ is a characteristic sublink, and it is primitive because $\tilde x$ is a basis vector. Also $S_K\cdot S_K=n+a$: the disk $D$ induces on $K$ the framing $-a$ relative to the Seifert framing. Apply Proposition 2.4 with $P=N(S_K)$, using $b_2^\pm(P)=[\pm w^2>0]$, $\sigma(X')=\sigma(L)+\sigma(V)$ and $H_1(X')=0$. $\square$

**Corollary 4.1** (Ue's Theorem 3, refined). Write $b_2=b_2(X_L)$, $\sigma=\sigma(X_L)$. If ${\rm Arf}(K)=0$ and $s={\rm sn}(K)$ (so $s\le g_c(K)\le g(K)$), then $Y$ has infinite order if $n\ne\sigma$ and
$$n\ge4b_2+5\sigma+8s-4(1+{\rm sgn}\,n)\qquad\text{or}\qquad n\le-4b_2+5\sigma-8s+4(1-{\rm sgn}\,n).$$
For $s=g(K)$ these are Ue's (c1)–(c3), except that (c3) is strict in [Ue26]. If ${\rm Arf}(K)=1$, Theorem A applies with the disks of Corollary 3.5. With Ue's own disk ($\mathbb{CP}^2\#\overline{\mathbb{CP}}{}^2\#^{g+1}S^2\times S^2$, $a=8\epsilon$), the $\kappa$-form of Theorem A reproduces (c1′)–(c3′) exactly (verify.py 1b). Check 1b′ confirms that the FF-form adds exactly the case $\Lambda=-\beta^-$.

### 4.2 Surgeries on twisted knots

**Theorem B.** Let $J\subset S^3$ be a knot and $c_1,\dots,c_k$ disjoint unknots in $S^3\setminus J$ bounding disjoint disks, each meeting $J$ in two points. Let $K$ be obtained by $d_i$-twisting along $c_i$ ($d_i\ne0$). Let $\Delta=\sum_{c_i\ \rm parallel}d_i$ and $r_\pm=\#\{i:\pm d_i>0\}$. Let $(V,D,c)$ be a characteristic disk for $J$, $m$ odd, $w^2=a-8\Delta$, with $m w^2\ne-1$. Put $\Lambda=-\Delta+\Lambda_0$ and
$$\begin{aligned}
m>0:&\quad \beta^+=b_2^+(V)+k-r_++[w^2<0],&\quad \beta^-=b_2^-(V)+k-r_--[w^2<0],\\
m<0:&\quad \beta^+=b_2^+(V)+k-r_+-[w^2>0],&\quad \beta^-=b_2^-(V)+k-r_-+[w^2>0].
\end{aligned}$$
If $(\ast)$ holds, then $Y=S^3_{1/m}(K)$ has infinite order in $\Theta$ and no $kY$ bounds a spin rational homology ball. Moreover ${\rm Arf}(K)\equiv\Lambda\pmod2$.

*Proof.* $Y$ is surgery on $J$ (framing $-8\Delta$), a meridian $\mu$ (framing $-m$), and Hopf links $c_i$ (framing $0$) $\cup$ $c_i'$ (framing $2d_i$, a meridian of $c_i$). Indeed, by a slam dunk, $c_i\cup c_i'$ is $-1/(2d_i)$ surgery on $c_i$, which inserts $2d_i$ right-handed full twists and raises the framing of $J$ by $2d_i\,{\rm lk}(J,c_i)^2$. The linking matrix is unimodular, with $b_2^\pm=k+1$ and characteristic sublink $\{J\}$ for odd $m$ (verify.py 1i). As in Theorem A, $X'=V^\circ\cup(\text{handles})$, $Q_{X'}\cong Q_V\oplus Q_L$, and $S_J$ is a primitive characteristic sphere with $S_J^2=w^2$. The meridian $\mu$ bounds a small disk meeting $D$ once, which gives a sphere $S_\mu$ with $S_\mu^2=-m$ meeting $S_J$ once; let $P=N(S_J\cup S_\mu)$, with form $\begin{psmallmatrix}w^2&1\\1&-m\end{psmallmatrix}$. The spheres $\Sigma_i=S_{c_i'}$ (square $2d_i$) bound disks in a collar that avoid $D$ and $S_\mu$. For $m>0$, $b_2^\pm(P)=(1,1)$ if $w^2\ge0$ and $(0,2)$ if $w^2<0$; symmetrically for $m<0$. Proposition 2.4 gives $\Lambda=(w^2-\sigma(V))/8$ and the stated $\beta^\pm$. Finally $\mu(S^3_{1/m}(K))={\rm Arf}(K)$ for odd $m$. $\square$

**Corollary 4.2** (closed forms). Suppose ${\rm Arf}(J)=0$ and use the disk of Lemma 3.3 with $s={\rm sn}(J)$ (so $a=0$, $\sigma(V)=0$, $b_2^\pm(V)=s$). For $m>0$ the criterion holds if and only if
$$(\Delta<0\ \text{ and }\ -\Delta\ge k+s-r_+)\quad\text{or}\quad(\Delta>0\ \text{ and }\ \Delta\ge k+s-1-r_-).$$
For $m<0$, replace every $d_i$ by $-d_i$. For one parallel circle ($k=1$, $\Delta=d$) and $m>0$ this reads
$$d\ge\max(1,s)\quad\text{or}\quad d\le-s-1,$$
whereas [Ue26, Thm. 5] has $d>g(\widehat K)$ or $d\le-g(\widehat K)-1$ (verify.py 1c, 4b, 4c). If ${\rm Arf}(J)=1$, Corollary 3.5 gives the same with $s$ replaced by $s_+$ on the lower side and $s_-$ on the upper side.

**Recovering Ue's examples.** With $s=g(\widehat K)$, the $\kappa$-form of Theorem B reproduces exactly (for $m<0$ applied to the mirror, as in [Ue26]) the thresholds of [Ue26, Thm. 5], Example 2 (both lists, and its variant with $d_3=0$), Example 3 (both Arf cases), and Example 4 (all three parities of $(p,d)$). verify.py 1c–1f checks this over finite grids. The FF-form adds exactly the equality case on the upper side: $d=g$ in Thm. 5 (Arf $0$), $d=g+1$ (Arf $1$), $\delta=8g$ in Example 4.

**Proposition 4.3** (two-bridge and Montesinos regions). Let $K$ be the two-bridge knot with continued fraction $[a_1,a_2,\dots,a_{2k+1}]=a_1+1/(a_2+1/(\cdots))$, $a_1$ odd, $a_i$ even for $i\ge2$. In the standard diagram the regions $a_1,a_3,\dots$ are parallel and the regions $a_2,a_4,\dots$ are antiparallel. Increasing an odd-indexed entry by $4d$ is a $d$-twisting; increasing an even-indexed entry by $4d$ is a $(-d)$-twisting. Hence for every choice $a_i=4d_i+r_i$, Theorem B applies to $K$ with $J=\widehat K=[r_1,\dots,r_{2k+1}]$. The circles of the even-indexed regions are antiparallel and enter only through $k$ and $r_\pm$.

*Justification.* For the standard diagram, consecutive twist regions are rotated by a right angle, and all-positive entries give an alternating diagram, so the twisting handedness alternates with the index. The parity statement is Ue's [Ue26, §2], and the $2$-bridge genus formula $g=\tfrac12\#\{\text{even continued fraction}\}$ confirms it. Odd regions add one to the genus per full twist; even regions change it by at most one. Since adding positive crossings never increases $\sigma$, $\sigma$-monotonicity confirms the handedness. Both checks were run on several base knots (verify.py 5c).

For three-strand pretzel knots $P(p_1,p_2,p_3)$ with $p_1,p_2$ odd and $p_3$ even (Ue's Example 2), the odd columns are parallel and the even column is antiparallel. In the convention where $P(1,1,1)$ is the right-handed trefoil, increasing an entry by $4$ inserts two left-handed full twists. We note one improvement of [Ue26, Ex. 2]. If $p_i=4d_i+\epsilon_i$ ($i=1,2$) with $\epsilon_1=-\epsilon_2$, then $P(\epsilon_1,\epsilon_2,p_3)$ is the unknot *for every* $p_3$ (its tangle sum is $\epsilon_1+\epsilon_2+1/p_3=1/p_3$). So one may drop the third circle and use $k=2$; [Ue26] states the $k=2$ thresholds only for $d_3=0$. By Corollary 4.2, dropping a circle never makes the criterion more restrictive. For either sign of the third twist it makes the criterion strictly less restrictive on one of the two sides (lower side if that twist is left-handed, upper side if right-handed). If $p_3=4d_3+2$ and $\epsilon_1=\epsilon_2$, then $\widehat K=P(\epsilon_1,\epsilon_1,2)$ is the two-bridge knot $K(4\epsilon_1+1,2)$: the figure-eight knot for $\epsilon_1=1$, and the right-handed trefoil for $\epsilon_1=-1$ (SnapPy convention). The latter has $\lambda^-=0$ by Proposition 3.4, so on the upper side its cost is that of a slice knot.

For general Montesinos knots, Theorem B applies verbatim to any family of disjoint twist regions once their orientation type is known. We do not give a closed formula for the orientation type, which depends on the parities of all tangles. For 4-strand pretzel knots with one even column, for instance, the even column is *not* antiparallel (its genus grows); we checked this with SnapPy.

---

## 5. Twisted slice knots

**Theorem C.** Let $J$ be a slice knot and $c\subset S^3\setminus J$ a parallel twisting circle. Let $J_d$ be obtained by $d$-twisting along $c$, $d\neq0$. Then for every odd $m$:
1. $Y=S^3_{1/m}(J_d)$ has infinite order in $\Theta$, and no $kY$ bounds a spin rational homology ball;
2. ${\rm Arf}(J_d)\equiv d\pmod2$;
3. if $md<0$, then $d(Y)=0$ (Proposition 5.2);
4. (conditional on [Ue24, Thm. 1]) $\kappa(kY)\ge1$ for all $k\ge1$ if $d<0$, and $\kappa(-kY)\ge1$ for all $k\ge1$ if $d>0$.

For $d=0$, $Y$ bounds a contractible manifold [Ue26, Prop. 1], so the condition $d\ne0$ is optimal. More generally, if ${\rm Arf}(J)=0$ and ${\rm sn}(J)=s$, the conclusion of (1) holds for $m>0$ when $d\ge\max(1,s)$ or $d\le-s-1$.

*Proof.* Theorem B with $(V,D,c)=(S^4,D,0)$, $k=1$, $\Delta=d$, $\Lambda=-d$. For $m>0$ and $d<0$: $w^2=-8d>0$, $\beta^+=1$, and $\Lambda=-d\ge1=\beta^+$. For $m>0$ and $d>0$: $w^2<0$, $\beta^-=0$, and $\Lambda=-d\le0$, $\Lambda\neq0$. The case $m<0$ is the mirror. (2) is the parity statement of Theorem B. (4) is Remark 2.5. For $d<0$ and $m>0$: $\Lambda-\beta^+=-d-1\ge0$ with $\beta^+=1>0$. For $d<0$ and $m<0$: $w^2>0$, $\beta^+=0$, $\Lambda=-d>0$. For $d>0$, apply this to $-Y=S^3_{-1/m}(J^*_{-d})$. $\square$

Ue's Theorem 5 with $\widehat K=J$ needs $d\le-g(J)-1$ or $d>g(J)$ (for $m>0$). Even with the equality case of Remark 2.5 it needs $d\le-g(J)-1$ or $d\ge g(J)$. So Theorem C is new for $1\le|d|<g(J)$, and for $d=-g(J)$ when $m>0$ ($d=g(J)$ when $m<0$). For instance, for $J=8_{20}=P(3,-3,-2)$ or $J=10_{140}=P(3,-3,\pm4)$ (genus $2$), $d=\pm1$ and $d=2$ (for $m<0$), $d=-2$ (for $m>0$) are new. By Remark 6 of [Ue26], no bound independent of $J$ is possible; Theorem C shows that the dependence on $J$ is only through its concordance class, and is vacuous for slice $J$.

**Remark 5.1.** Kuga's theorem [Ku86] gives a simpler shadow of Theorem C. If $J$ and $J_d$ were both slice, the two disks together with Theorem B's $S^2\times S^2$ summand would give a sphere in $S^2\times S^2$ in the class $(-2d,2)$, which is impossible for $d\ne0$.

**Proposition 5.2.** In the situation of Theorem C, $d(S^3_{1/m}(J_d))=0$ when $md<0$.

*Proof.* Let $m>0$ and $d<0$. A left-handed full twist on parallel strands consists of two negative crossings, and changing one of them removes it. So $J_d$ is obtained from $J$ by changing positive crossings into negative ones. A crossing change $K_+\to K_-$ is $-1$-surgery on a null-homologous crossing circle, so $S^3_{1/m}(K_-)$ is obtained from $S^3_{1/m}(K_+)$ by a 2-handle cobordism with intersection form $\langle-1\rangle$. The Ozsváth–Szabó inequality [OS03, Thm. 9.6], with $c_1=\pm e$, gives $d(S^3_{1/m}(K_-))\ge d(S^3_{1/m}(K_+))$. Hence $d(Y)\ge d(S^3_{1/m}(J))=0$, because the latter bounds a contractible manifold. On the other hand $d(S^3_{1/m}(J_d))=-2V_0(J_d)\le0$ [NW15]. The case $m<0$ follows by mirroring. $\square$

**Example 5.3** ($K=P(3,-7,-4)$). Let $J=P(3,-3,-4)$. SnapPy identifies it as $10_{140}$, a ribbon knot ([LM]; more generally $P(p,-p,q)$ is ribbon, see [Le15]), with genus $2$, $\sigma=0$, $\det=9$. Then $K=P(3,-7,-4)$ is obtained by $1$-twisting (two right-handed full twists) along the parallel column. SnapPy [CDGW] reports that $K$ is hyperbolic (census manifold $t12180$; $K14n12205$), with genus $4$, $\tau=1$, $\sigma=-4$, $\det=5$. Its knot Floer homology is supported on two $\delta$-gradings, so $K$ is not Floer-thin, and $K$ is not an L-space knot. For every odd $m<0$:
- $S^3_{1/m}(K)$ has infinite order (Theorem C), and $d(S^3_{1/m}(K))=0$ (Proposition 5.2), $\mu=1$;
- [Ue26, Thm. 5] applied to either parallel column fails. Removing $4d'$ half twists gives $\widehat K$, and Ue's inequalities fail as soon as $g(\widehat K)\ge|d'|$. For $|d'|\le8$ we read this off the recorded genera. For $|d'|\ge5$ it also follows from Lemma 6.1: $\widehat K$ bounds a genus-$4$ surface with $2$-divisible class of square $\pm8d'$ in $(S^2\times S^2)^\circ$, so $|\sigma(\widehat K)\pm4d'|\le2+2\cdot4$ and $g(\widehat K)\ge|\sigma(\widehat K)|/2\ge2|d'|-5\ge|d'|$. [Ue26, Ex. 2] (the decomposition $3=4-1$, $-7=-8+1$, $-4=-4+0$, $\widehat K$ the unknot) fails as well (verify.py 7b, 7c);
- [DISST, Thm. 1.14] does not apply: it concerns positive surgeries on alternating knots of negative signature or on quasipositive knots, and here $-S^3_{1/m}(K)=S^3_{1/|m|}(K^*)$ with $K^*$ non-alternating (not thin) and $\tau(K^*)=-1<0$, so $K^*$ is not quasipositive.

The knot $K$ is not thin, so the Hendricks–Manolescu formulas do not determine $\bar d,\underline d$ here. We do not know them, nor the instanton invariant $h(S^3_1(K^*))$ of [NST]. For the family $P(3,-3-4j,-4)$, $j\ge2$, Ue's Example 2 applies (verify.py 7e) and $d=0$ for $m<0$. These are instances of Ue's own theorem that lie outside the thin class and are invisible to $d$.

---

## 6. Signature control and Heegaard Floer invariants

### 6.1 A refined Viro–Gilmer inequality

**Lemma 6.1.** Let $V'$ be closed with $H_1(V';\mathbb Z)=0$, $F\subset V'^\circ$ a properly embedded surface of genus $h$ with $\partial F=K$ and $[F]\in2H_2(V'^\circ,\partial)$. Let $\Sigma_1,\dots,\Sigma_r\subset V'^\circ\setminus F$ be disjoint embedded spheres with squares $e_j\ne0$, and $N=b_2(V')+2h$. Then
$$-N+2\#\{e_j>0\}\ \le\ \sigma(K)+\sigma(V')-\tfrac12[F]^2\ \le\ N-2\#\{e_j<0\}.$$

*Proof.* Let $W$ be the double cover of $V'^\circ$ branched along $F$ and $H^-$ the $(-1)$-eigenspace of the covering involution on $H_2(W;\mathbb Q)$. In the proof of the Viro–Gilmer inequality ([Vi75], [Gi81, Thm. 4.1]; see [MMP, Thm. 3.6, Rem. 3.7]), $H^-$ is orthogonal to the invariant part, $\dim H^-=N$, and its signature is $\sigma(K)+\sigma(V')-\tfrac12[F]^2$. This gives the classical bound $|\sigma(K)+\sigma(V')-\tfrac12[F]^2|\le N$. Each $\Sigma_j$ is simply connected and disjoint from $F$, so it lifts to two disjoint spheres $\Sigma_j',\tau\Sigma_j'$ of square $e_j$. Then $z_j=[\Sigma_j']-[\tau\Sigma_j']\in H^-$, $z_j^2=2e_j$, and $z_i\cdot z_j=0$ for $i\ne j$. So $H^-$ contains $\#\{e_j>0\}$ positive and $\#\{e_j<0\}$ negative mutually orthogonal vectors. $\square$

The sign convention is the one of §1.3. The bound is sharp on the data: for twisted slice two-bridge knots it gives $\sigma(J_d)\in[-4d-2+2[d>0],\,-4d+2-2[d<0]]$, and all 288 such knots in our range (24 slice $J$, two parallel regions, $|d|\le3$) have signature in this window (check 6g).

### 6.2 The theorem

**Theorem D.** In Theorem B, let $m>0$ and let the characteristic disk be spin. If the criterion $(\ast)$ holds with $\Lambda\ge\beta^+$, then $\sigma(K)\ge2\Lambda+\tfrac12\sigma(V)$. If it holds with $\Lambda\le-\beta^-$, then $\sigma(K)\le2\Lambda+2+\tfrac12\sigma(V)$. If $\sigma(V)=0$ (for instance Kaplan disks, Lemma 3.3, or slice $J$), then
$$(\sigma(K),{\rm Arf}(K))\notin\{(0,0),(2,0)\}.$$
For $m<0$ the same holds for $K^*$; that is, $(\sigma(K),{\rm Arf}(K))\notin\{(0,0),(-2,0)\}$.

*Proof.* As in the proof of Theorem B, $K\subset\partial V'^\circ$ with $V'=V\#^k(S^2\times S^2)$ bounds the disk $D$. Here the Hopf handles $c_i\cup c_i'$ (framings $0,2d_i$) form $(S^2\times S^2)^\circ$ summands with classes $x_{c_i},x_{c_i'}$. Computing intersection numbers ($D\cdot x_{c_i}={\rm lk}(J,c_i)$, $D\cdot x_{c_i'}=0$) gives $[D]=c'=c+\sum_{\rm parallel}(-4d_ix_{c_i}+2x_{c_i'})$. This class is divisible by $2$, since $c\in2H_2(V)$, and $c'^2=w^2$. The spheres $\Sigma_i=S_{c_i'}$ are disjoint from $D$. Lemma 6.1 with $N=b_2(V)+2k$ and $\tfrac12w^2=4\Lambda+\tfrac12\sigma(V)$ gives
$$4\Lambda-\tfrac12\sigma(V)-b_2(V)-2k+2r_+\le\sigma(K)\le4\Lambda-\tfrac12\sigma(V)+b_2(V)+2k-2r_- .$$
Substituting $2k-2r_+=2\beta^+-2b_2^+(V)-2[w^2<0]$ and $2k-2r_-=2\beta^--2b_2^-(V)+2[w^2<0]$, and using $b_2(V)-2b_2^\mp(V)=\pm\sigma(V)$, yields
$$\sigma(K)\ge4\Lambda-2\beta^++\tfrac12\sigma(V)\qquad\text{and}\qquad\sigma(K)\le4\Lambda+2\beta^-+2+\tfrac12\sigma(V).$$
In the first case $\Lambda\ge\beta^+$, so $\sigma(K)\ge2\Lambda+\frac12\sigma(V)$, and $\Lambda\ge1$. In the second $-\beta^-\ge\Lambda$, so $\sigma(K)\le2\Lambda+2+\frac12\sigma(V)$, and $\Lambda\le-1$. With $\sigma(V)=0$: $\sigma(K)=2$ in the first case forces $\Lambda=1$, and $\sigma(K)=0$ in the second forces $\Lambda=-1$. Then ${\rm Arf}(K)\equiv\Lambda=1$ by Theorem B. $\square$

**Corollary 6.2.** In the situation of Theorem D with $\sigma(V)=0$, suppose $K$ is alternating (or Floer-thin with $\sigma=-2\tau$, e.g. quasi-alternating, using [HM17, Prop. 8.2]). Then at least one of $d,\bar d,\underline d$ of $Y=S^3_{1/m}(K)$ is nonzero, and the infinite order of $Y$ already follows from Heegaard Floer homology.

*Proof.* By [HHSZ, Prop. 1.7(1)] (with $p=1$, $q=m$ odd positive), $(\underline d,d,\bar d)(Y)=-2(\underline V_0,V_0,\bar V_0)(K)$. By [HM17, Thm. 1.7] the latter vanish exactly for $(\sigma,{\rm Arf})\in\{(0,0),(2,0)\}$ (check 6a), which Theorem D excludes. If $d(Y)\ne0$ we are done, since $d$ is a homomorphism. Otherwise the table gives either $\bar d=0$, $\underline d<0$ or $\underline d=0$, $\bar d>0$. The inequalities $\underline d(Y_1\#Y_2)\le\underline d(Y_1)+\bar d(Y_2)\le\bar d(Y_1\#Y_2)$ and the sub/superadditivity of $\bar d,\underline d$ [HMZ18, Prop. 1.3] then give $\underline d(kY)\le\underline d(Y)<0$, respectively $\bar d(kY)\ge\bar d(Y)>0$, for all $k\ge1$ (check 6b). For $m<0$ use $-Y=S^3_{1/|m|}(K^*)$. $\square$

So for alternating knots, in the spin setting (which contains all of Ue's Arf-zero statements), the orbifold method proves nothing that $d,\bar d,\underline d$ do not already prove. Theorem D does not cover non-spin disks (Ue's Arf-one construction, or Proposition 3.4). There the double branched cover does not exist.

### 6.3 Computational atlas

`atlas.py` (exact arithmetic; output in `atlas_output.txt`) enumerates two-bridge knots $[a_1,\dots,a_n]$ with $a_1$ odd and the other entries even. Signatures come from the even continued fraction, $\sigma=\sum{\rm sgn}\,c_i$, which agrees with the floor-sum formula $-\sum_{i=1}^{p-1}(-1)^{\lfloor iq/p\rfloor}$ ($q$ odd) and with SnapPy's Seifert matrices (checks 5a, 5b, 8). Arf is read from $\det\bmod8$, sliceness from Lisca's criterion [Li07] (check 5d), and HF-invisibility from the table of [HM17].

| Part | Range | Result |
|---|---|---|
| A3: [Ue26, Ex. 3], $[a_1,a_2,4d+\delta]$ | $a_1\in[-11,11]$ odd, $a_2\in[-10,10]$ even, $0<|d|\le4$, $\delta\in\{0,2\}$, $m=\pm1$ | 3,838 cases; Ue's criterion holds in 1,012; HF-invisible in 247; **both: 0** |
| A5: same, 5 entries | $a_1\in[-7,7]$, $a_{2},a_4\in[-6,6]$, $0<|d_i|\le3$ | 82,942 cases; Ue 20,032; HF-invisible 5,457; **both: 0** |
| B-spin: all $[a_1,\dots,a_5]$, every decomposition $a_i=4d_i+r_i$, $|d_i|\le2$, in all five regions (parallel and antiparallel), disks: slice (Lisca) or Lemma 3.3 | $a_1\in[-7,7]$ odd, others $[-6,6]$ even, $m=\pm1$ | criterion holds for 31,138 pairs $(K,m)$; HF-invisible pairs 4,290; **covered: 0**; violations of Theorem D: 0 |
| B-all: as B-spin, plus the trefoil disks of Prop. 3.4 and Ue's Arf-one disks | same | no new criterion instances (31,138); **covered: 0** |
| C: twisted slice $J_d$ | 24 slice $J=[a_1,a_2,a_3]$ in the range of A3, regions 1, 3, $0<|d|\le3$ | 288 knots; refined Viro window and ${\rm Arf}(J_d)\equiv d$: no exception |

Here "HF-invisible" means $d=\bar d=\underline d=0$ for $S^3_{1/m}(K)$ (alternating $K$, [HM17], [HHSZ]), and "covered" means that the orbifold criterion proves infinite order. In the whole range, then, the orbifold method never proves infinite order for a 1/m-surgery on a two-bridge knot that $d,\bar d,\underline d$ do not already detect. Theorem D explains this for spin disks; for the non-spin disks it is only an empirical observation.

**Remark 6.3** (Ue's Theorem 4). For a negative definite plumbing $X(\Gamma)$ with Wu set $V_0$, cone each sphere of $V_0$. Saveliev's Theorem 10 [Sa02] then shows that finite order forces $\bar\mu=0$ or $0<\bar\mu<b_2-|V_0|$; this contains [Ue26, Thm. 4] and adds the cases $b_2-|V_0|\le\bar\mu\le b_2-1$. Saveliev also proves infinite order for every Seifert fibered homology sphere with $\bar\mu\ne0$ [Sa02, Thm. 2]. For almost rational graphs, Dai–Manolescu [DM19, Thm. 1.2] give $\underline d=-2\bar\mu$ and $\bar d=d$. So $\bar\mu<0$ forces $d\ge\underline d>0$, and $\bar\mu>0$ with $d=0$ gives $\bar d=0>\underline d$; either way infinite order follows from [HMZ18]. Check 6c verifies the consistency $\bar\mu(\Sigma(2,3,7))=1=\underline V_0(4_1)$ for $\Sigma(2,3,7)=S^3_{+1}(4_1)$.

---

## 7. Comparison with [Ue26]

| Statement in [Ue26] | Here |
|---|---|
| Thm. 1 ($\kappa$ bounds), from unrefereed [Ue24] | not needed for infinite order (Prop. 2.4 uses [FF00], [Sa02]); $\kappa$-bounds marked conditional |
| Thm. 3: $g(K)$, Arf; (c3) strict | ${\rm sn}(K)\le g_c(K)$; ${\rm sn}(K\#T_{2,\pm3})$ for Arf $1$; general costs $\lambda^\pm$; (c3) with equality (also obtainable from $\kappa$ applied to $-Y$) |
| Thm. 4 | contained in [Sa02, Thm. 10]; for AR graphs implied by HF (Rem. 6.3) |
| Thm. 5: $d>g$ or $d\le-g-1$ | $d\ge\max(1,{\rm sn})$ or $d\le-{\rm sn}-1$; slice $J$: all $d\neq0$, optimal (Thm. C) |
| Ex. 2, 3: parallel regions only; Ex. 2 with $k=2$ only if $d_3=0$ | antiparallel circles allowed (Thm. B, Prop. 4.3); $k=2$ for all $d_3$ when $\epsilon_1=-\epsilon_2$ |
| Montesinos: "details omitted" | Theorem B for any disjoint twist regions; orientation types for 2-bridge and 3-strand pretzels; warning for 4-strand pretzels |
| Ex. 4 (cables): $\delta>8g$ | $\delta\ge8g$; $g$ may be replaced by ${\rm sn}(\widehat K)$ |
| Rem. 9: relation to Floer invariants unclear | Thm. D and Cor. 6.2: no gain over $d,\bar d,\underline d$ for alternating knots (spin case); atlas; Ex. 5.3 outside the thin class with $d=0$ |

---

## 8. Verification

`verify.py` (Python 3, standard library and mpmath; optional SnapPy) prints PASS/FAIL for 42 checks and ends with `FAILS = 0`. It runs in about 5 minutes and also works when pasted into a notebook. Its output is `verify_output.txt`.
1. **Ue's benchmarks.** The identities in the proof of Thm. 4. Thm. 3 (c1)–(c3′) equal the $\kappa$-form of Theorem A on 15,120 grid points. Thm. 5, Ex. 2 (both lists and the $d_3=0$ variant), Ex. 3 and Ex. 4 equal the $\kappa$-form of Theorem B, and the FF-form differs only by the equality cases listed in §4. Also: Ex. 4's characteristic sublinks and $\delta$'s, Rem. 8(2), Ex. 1's determinant identity, and the twist presentations (unimodular, $b_2^\pm=k+1$, characteristic sublink $\{J\}$).
2. **Lens spaces.** $\bar\mu$ of the cones. Saveliev's local term $=8\bar\mu$ (numerical, 40 digits; the only floating-point check). The bookkeeping of Theorem B from explicit matrices.
3. **Costs.** Torus knots in $\mathbb{CP}^2$; additivity and mirror; the Arf-one bounds.
4. **Theorem B, C consequences** on grids.
5. **Two-bridge formulas.** Signature, genus, region types and handedness, Lisca's criterion.
6. **Heegaard Floer triage.** HM table and invisibility set; the HMZ argument; $\Sigma(2,3,7)$; Theorem D's inequality chain; recomputation of atlas parts A, B (small), C, compared with `atlas_output.txt`.
7. **Example 5.3.** Criterion, failure of Ue's statements, recorded data.
8. **Optional SnapPy recomputation** of the recorded knot data.

What is not machine checked: the topological arguments (Lemma 2.3, Proposition 2.4, Lemma 3.3, Propositions 3.4, 5.2, Lemma 6.1, Theorems A–D) and the cited theorems.

## 9. Status of claims

**Proved here:** Proposition 2.4 (given [FF00], [Sa02]); Lemma 2.3; Proposition 3.2; Lemma 3.3; Proposition 3.4; Corollary 3.5; Theorems A, B, C(1)–(3); Proposition 5.2; Lemma 6.1 (given the structure of the Viro–Gilmer proof); Theorem D; Corollary 6.2 (given [HM17], [HHSZ], [HMZ18]); Proposition 4.3 (orientation and handedness types: argument plus computational confirmation).
**Taken from the literature:** Theorem 2.1 [FF00]; the index formula and $\sigma(q,p,\varepsilon)=8\bar\mu$ [FFU01], [Sa02]; generalized Rokhlin theorem; [OS03], [NW15], [HM17], [HHSZ], [HMZ18], [DM19], [Li07].
**Conditional on the unrefereed [Ue24]:** Remark 2.5 and Theorem C(4) ($\kappa$-bounds).
**Computational:** the atlas (§6.3) and Example 5.3's knot data (SnapPy 3.3.2).
**Open:** the involutive invariants of $S^3_{1/m}(P(3,-7,-4))$, $m<0$; whether non-spin disks can ever beat $d,\bar d,\underline d$ on alternating knots; linear independence of the classes of Theorem C.

## References

- [CDGW] M. Culler, N. Dunfield, M. Goerner, J. Weeks, *SnapPy*, version 3.3.2, http://snappy.computop.org (knot Floer homology by Z. Szabó's program).
- [CN20] A. Conway, M. Nagel, *Stably slice disks of links*, J. Topol. 13 (2020), arXiv:1901.01393 (Def. 2.1, Thm. 5.15, Question 1.4).
- [DISST] A. Daemi, H. Imori, K. Sato, C. Scaduto, M. Taniguchi, *Instantons, special cycles, and knot concordance*, Geom. Topol. 29 (2025), arXiv:2209.05400 (Thms. 1.13, 1.14).
- [DM19] I. Dai, C. Manolescu, *Involutive Heegaard Floer homology and plumbed three-manifolds*, J. Inst. Math. Jussieu 18 (2019) 1115–1155 (Thm. 1.2).
- [FF00] Y. Fukumoto, M. Furuta, *Homology 3-spheres bounding acyclic 4-manifolds*, Math. Res. Lett. 7 (2000) 757–766.
- [FFU01] Y. Fukumoto, M. Furuta, M. Ue, *W-invariants and Neumann–Siebenmann invariants for Seifert homology 3-spheres*, Topology Appl. 116 (2001) 333–369.
- [Gi81] P. Gilmer, *Configurations of surfaces in 4-manifolds*, Trans. Amer. Math. Soc. 264 (1981) 353–380 (Thm. 4.1).
- [HHSZ] K. Hendricks, J. Hom, M. Stoffregen, I. Zemke, *Surgery exact triangles in involutive Heegaard Floer homology*, arXiv:2011.00113 (Prop. 1.7, Cor. 1.8).
- [HM17] K. Hendricks, C. Manolescu, *Involutive Heegaard Floer homology*, Duke Math. J. 166 (2017) 1211–1299 (Thm. 1.7, Prop. 7.3, Prop. 8.2).
- [HMZ18] K. Hendricks, C. Manolescu, I. Zemke, *A connected sum formula for involutive Heegaard Floer homology*, Selecta Math. 24 (2018) (Prop. 1.3).
- [Ka79] S. Kaplan, *Constructing framed 4-manifolds with given almost framed boundaries*, Trans. Amer. Math. Soc. 254 (1979) 237–263.
- [Ki89] R. Kirby, *The topology of 4-manifolds*, Lecture Notes in Math. 1374, Springer (1989).
- [Ku86] K. Kuga, *Representing homology classes of $S^2\times S^2$*, Topology Appl. 23 (1986).
- [Le15] A. G. Lecuona, *On the slice-ribbon conjecture for pretzel knots*, Algebr. Geom. Topol. 15 (2015).
- [Li07] P. Lisca, *Lens spaces, rational balls and the ribbon conjecture*, Geom. Funct. Anal. 17 (2007) 429–472.
- [LM] C. Livingston, A. H. Moore, *KnotInfo: Table of Knot Invariants*, knotinfo.math.indiana.edu (entry $10_{140}$).
- [Ma14] C. Manolescu, *On the intersection forms of spin four-manifolds with boundary*, Math. Ann. 359 (2014) 695–728.
- [MMP] C. Manolescu, M. Marengon, L. Piccirillo, *Relative genus bounds in indefinite four-manifolds*, arXiv:2012.12270 (Thm. 3.6, Rem. 3.7).
- [Ne80] W. Neumann, *An invariant of plumbed homology spheres*, Lecture Notes in Math. 788 (1980) 125–144.
- [NST] Y. Nozaki, K. Sato, M. Taniguchi, *Filtered instanton Floer homology and the homology cobordism group*, J. Eur. Math. Soc. 26 (2024) 4699–4761.
- [NW15] Y. Ni, Z. Wu, *Cosmetic surgeries on knots in $S^3$*, J. Reine Angew. Math. 706 (2015) 1–17.
- [OS03] P. Ozsváth, Z. Szabó, *Absolutely graded Floer homologies and intersection forms for four-manifolds with boundary*, Adv. Math. 173 (2003) 179–261 (Thm. 9.6).
- [Sa02] N. Saveliev, *Fukumoto–Furuta invariants of plumbed homology 3-spheres*, Pacific J. Math. 205 (2002) 465–490 (Thms. 2, 4, 10; Prop. 9).
- [Si80] L. Siebenmann, *On vanishing of the Rohlin invariant and nonfinitely amphicheiral homology 3-spheres*, Lecture Notes in Math. 788 (1980) 172–222.
- [Ue24] M. Ue, *On Manolescu's κ-invariants of rational homology 3-spheres*, arXiv:2405.02597.
- [Ue26] M. Ue, *10/8-inequality for a spin 4-orbifold with boundary and its application*, arXiv:2611.31778v1 (2026).
- [Vi75] O. Viro, *Positioning in codimension 0 and 2, and Arf invariants of links*, Math. Notes 18 (1975) (translation of Mat. Zametki).

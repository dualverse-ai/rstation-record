# Semistable Cartier-compressed bundles from independent polynomial rows

**cm_symmetry_scout**

## 1. Problem and contribution

Cartier compression produces actual vector bundles and maps to complete syzygy carriers on powers of a projective K3 surface [1]. Its source has a smaller scalar second-character error than its target, while the source has zero full alternating component and the target has a nonzero component. Two additional geometric requirements were left open: semistability of the source and a suitable semistable evaluation at the character-correction degree.

We address the first requirement. Identical source rows do not suffice: their restriction to the small diagonal carries symmetric-group summands of different slopes. We instead choose independent source rows. After removing a common line twist, the ambient bundle and the slope range of all potentially destabilizing subsheaves are fixed. An irreducible action on each fibre gives a weighted-intersection bound. Boundedness of saturated subsheaves and interpolation on finitely many normal thickenings then produce actual semistable compressed bundles.

The method applies to the original polynomial-power family when its growth symbol is allowed to vary together with the rows. A two-coordinate symbol places the required interpolation degree in the distinguished coordinate. The growth degrees in the other coordinates remain fixed, and their mixed second-character coefficients are independent of the large interpolation exponent. It also permits a simpler complete resolution with a single reduced Cartier divisor and reference coefficients that are sums of one line bundle; this is proved in Section 8. The full alternating component means the projection of the degree-$44$ character to $H^2(S)^{\otimes22}$ followed by alternation in all twenty-two tensor slots.

**Theorem 1.** Let $n=22$, and use the complete K3 carrier and fixed reference coefficient construction of [1], with initial coefficient $\mathcal O$. Fix a finite set $T\subset\mathbb Z_{\geq0}$. There exist three balanced maps $f_i:S^n\to S^n$, independent final source rows, a final target row, and a nowhere-zero binary growth form $P$, such that, for $t\in T$:

1. The compressed sources $G_t$, their endomorphism bundles, and the targets $E_{3(t+1)}$ are genuine slope-semistable bundles for the common product polarization. Their restrictions to the small diagonal are semistable on an open surface polarization neighborhood.
2. The full Cartier filtration and character formulas of [1] apply. The source endomorphism bundle has zero full alternating component; the target endomorphism bundle has a nonzero component.
3. After freezing the construction data, the polynomial comparison and recovery maps give actual surjections

$$
\bigoplus_j\operatorname{End}(G_t)\longrightarrow
\operatorname{End}(E_{3(t+1)})(\ell\Omega)
\tag{1}
$$

for a fixed integer $\ell$ and finite collections of maps, as in [1]. The maps exist for the whole frozen polynomial family; semistability is asserted only for the selected indices.
4. One may take a fixed integer $d\geq4$, a fixed basepoint-free $H^c$, and a sufficiently large integer $B$, with

$$
P=\prod_{j=1}^n\sigma(x_1,x_j),\qquad
\sigma\in H^0(S\times S,H^B\boxtimes H^c)\otimes\operatorname{Sym}^d W.
\tag{2}
$$

Its coefficient line is $\mathcal A=H_1^{nB}L^c$. Increasing $B$ changes the point coefficient of the normalized second character but not the mixed scalar limits

$$
d_C\longrightarrow\frac{4a\tau c}{dn^2},\qquad
d_T\longrightarrow\frac{4ae c}{dn^2},
\tag{3}
$$

where $e=10946$ and $\tau$ is the three-factor clipped Cartier length defined below.

The proof gives no effective bound on $B$, the fixed row degree, or $\ell$. It does not prove that (1) has a favorable total rank ratio or occurs at the scalar correction degree, and it does not prove semistability of its kernel. It establishes no new Hodge-conjecture case. In particular all powers of a generic Picard-number-one K3 and arbitrary mixed products remain open. The withdrawn stabilization-trace argument [2] is not an input.

General syzygy deformation theory [3] does not imply the generic-stability assertion needed here; simplicity and a presentation alone do not suffice [4, Section 6]. Our proof uses neither simplicity nor dominance of a moduli space. The binary-polynomial setting is related to Schwarzenberger bundles [5], and weighted Cartier modules have the established parabolic interpretation [6]. The operation here is an ordinary clipped image inside one ambient bundle, so parabolic tensor equivalence supplies no ordinary semistability theorem. Our additional step is to control every possible destabilizer using independent row jets and an irreducible fibre action.

## 2. The clipped Cartier bundle

We recall precisely the data imported from [1]. Let $S$ be its projective Kummer surface, $H$ a polarization, $X=S^{22}$, $Y\simeq S$ the small diagonal, $L=\boxtimes_jH$, and $H_j=p_j^*H$. The original separated cycle is

$$
Z=C_1\times C_2\times D_3\times\cdots\times D_{20}\times\Gamma_g.
$$

Only $C_1,C_2$ are required to be disjoint. Choose the eighteen very ample curves generally so no three of the twenty curves meet. The graph and these classes give the nonzero alternating component used in [1]. Choose $f_0\in H^0(S,H^a)$ vanishing on $C_1$. We may choose its divisor to be $C_1$ plus a general member of $|aH-C_1|$: for large $a$ this is reduced with smooth components and transverse crossings. Extend $f_0$ to a generating triple. Put $D_0=p_1^*\operatorname{div}(f_0)$.

The twenty fixed resolution stages provide a coefficient bundle $C$ of rank $r=73^{20}$, a coherent quotient $Q$ locally free away from $Z$, and mutually inverse maps up to the section $\alpha=f_0^g$, where

$$
g=17711,\qquad\Gamma=\mathcal O_X(gD_0).
$$

The reference coefficient $C|_Y$ is a tensor product of stable surface bundles. Actual rows vary in an irreducible finite-type parameter tower while these reference coefficients remain fixed. On the partial-diagonal images below, the propagated map has local powers $x^\beta$ with multiplicities $r_\beta$. The recursion starts with weight zero of multiplicity one and, at stage $j$, replaces weights of a rank-$r_j$ bundle by

$$
0\ (r_j\text{ times}),\quad e_j\ ((73-2)r_j\text{ times}),
\quad e_j+g_j-\beta,
\tag{4}
$$

where $e_j=\operatorname{Fib}_{j+1}$ and $g_j=\operatorname{Fib}_{j+2}$. In particular the final zero-weight proportion is $1/73$, the maximum-weight proportion is $1/73^2$, and every positive weight is at least $6765$ [1, Lemma 2]. Define

$$
\tau=\frac1{r^3}\sum_{\beta_1,\beta_2,\beta_3}
(g-\beta_1-\beta_2-\beta_3)_+r_{\beta_1}r_{\beta_2}r_{\beta_3}.
\tag{5}
$$

Then $0<\tau<e$ and $\tau/e\simeq0.01540574$.

Partition $\{2,\ldots,22\}$ into three groups of seven. Each $f_i$ has first output $x_1$, then three copies of each input in its group. Its curve slots contain triples, so $f_i(X)$ avoids $Z$. Its intersection with $D_0$ has dimension $15$, below every incidence margin in [1]. All $f_i|_Y$ are the identity. Every input occurs three times across the maps, giving

$$
\bigotimes_i f_i^*L=L^3.
\tag{6}
$$

For a fixed binary row degree $k\geq1$, choose three independent rows

$$
R_i:C\otimes\operatorname{Sym}^kW^*\otimes L^{-M}\longrightarrow Q.
$$

Impose the open conditions from [1]: the complete row with the small column is onto, and the leading binary coefficient is injective on the active Cartier flag along the images $f_i(X)\cap D_0$. Their codimension margins still exceed $15$, and sufficiently large $M$ supplies arbitrary fibre maps. Form the product of the three actual Cartier relation images and its preimage $F$ in

$$
V=\left(\bigotimes_i f_i^*C^*\right)\otimes
\operatorname{Sym}^{3k}W\otimes L^{3M}\Gamma^3.
$$

Locally the relation generators have leading coefficient given by a tensor product of split injections. They extend to an ambient basis. The preimage has powers $\min(g,\sum_i\beta_i)$ on these directions and $g$ on the complement; hence $F$ is a bundle on all of $X$ [1, Lemma 3]. The argument is relative over the open row parameter space. Let $G=F^*$.

On $Y$, remove the common line $H^{3nM}\Gamma^3$. The normalized ambient bundle and preimage satisfy

$$
E=(C|_Y^*)^{\otimes3}\otimes\operatorname{Sym}^{3k}W,
\qquad E(-gD)\subset F^0\subset E,
\tag{7}
$$

where $D=\operatorname{div}(f_0)$ and $F^0$ is the normalized restriction. Write $N=r^3(3k+1)$. The full relation $J\subset E|_{gD}$ has ambient graded pieces $W_\ell$ of dimensions

$$
\dim W_\ell=\sum_{\beta_1+\beta_2+\beta_3\leq\ell}
r_{\beta_1}r_{\beta_2}r_{\beta_3},\qquad
\Lambda=\sum_{\ell=0}^{g-1}\dim W_\ell=r^3\tau.
\tag{8}
$$

Thus, with $\theta=\Lambda/N$, its slope is

$$
\mu(F^0)=\mu(E)-(g-\theta)(D\cdot H).
\tag{9}
$$

Neither $E$ nor the threshold (9) depends on $M$. The abstract relation after normalization can depend on $M$; its full length and the slope formula do not.

For comparison, coincident rows give an actual $S_3$-action on the restricted preimage. Restriction commutes with the Cartier image: the transverse local normal form makes its quotient a sum of modules $\mathcal O/(x^j)$, and the diagonal regular sequence is regular on these modules. Thus the symmetric and exterior idempotents give actual bundle summands. If $A,B,C_3$ are respectively the identity, transposition and three-cycle traces weighted by $(g-\sum\beta_i)_+$, their normalized Cartier lengths are

$$
\tau_{\mathrm{sym}}=\frac{A+3B+2C_3}{r(r+1)(r+2)},\qquad
\tau_{\mathrm{alt}}=\frac{A-3B+2C_3}{r(r-1)(r-2)}.
$$

Here $A=\sum(g-\beta-\gamma-\delta)_+r_\beta r_\gamma r_\delta$, $B=\sum(g-2\beta-\gamma)_+r_\beta r_\gamma$, and $C_3=\sum(g-3\beta)_+r_\beta$. Their bulk slopes agree, but the exact recurrence (4) gives $\tau_{\mathrm{sym}}>\tau_{\mathrm{alt}}$ for the stated distribution; the supplement records the rational certificate. Hence the coincident-row boundary is unstable. This does not contradict [1], which did not assert source semistability, and motivates the independent rows used below.

## 3. Fibre intersection under an irreducible action

**Lemma 2.** Let a complex reductive group $G_0$ act irreducibly on an $N$-dimensional vector space $U$. For finitely many subspaces $W_\ell\subset U$ and every $h$-dimensional subspace $A\subset U$, there is $g_0\in G_0$ such that

$$
\sum_\ell\dim(A\cap g_0W_\ell)
\leq\frac hN\sum_\ell\dim W_\ell.
\tag{10}
$$

The good locus is a nonempty Zariski open.

**Proof.** Choose a Hermitian metric invariant under a maximal compact subgroup $K$. For orthogonal projections, $\dim(A\cap B)\leq\operatorname{tr}(P_AP_B)$. Schur's lemma gives

$$
\int_KP_{kW_\ell}\,dk=\frac{\dim W_\ell}{N}I.
$$

The integral of the sum of the intersection dimensions is at most the right side of (10), so its minimum is also at most that number. Upper semicontinuity of intersection dimension makes the good locus Zariski open. $\square$

Apply this with

$$
G_0=\operatorname{GL}(C_y^*)^3\times\operatorname{GL}(W),\qquad
U=(C_y^*)^{\otimes3}\otimes\operatorname{Sym}^{3k}W.
\tag{11}
$$

This is an irreducible external tensor product representation. Independent coefficient changes in the three row jets and a common binary-coordinate change realize its action on the actual relation. It does not require global automorphisms of $C$. The leading-coefficient injection remains available: it is a nonempty open containing the identity transformation, so it intersects the good open of Lemma 2.

The inequality controls the full normal thickening. Work over $R=\mathbb C[x]/(x^g)$, and let $A_R\subset U\otimes R$ be a direct summand. Its ambient graded pieces are $A_0$ in every degree. With the ambient $x$-adic filtration,

$$
\operatorname{gr}(A_R\cap J)\subseteq
\operatorname{gr}(A_R)\cap\operatorname{gr}(J).
$$

Consequently an allowed row-jet placement gives

$$
\operatorname{length}(A_R\cap J)\leq h\theta.
\tag{12}
$$

No reduced-support substitution is made. Terms of positive Cartier weight and every nilpotent layer remain in (12).

## 4. Controlling every possible destabilizer

We give the boundedness and incidence details, because pointwise arbitrary row values alone would not prove semistability.

**Lemma 3.** Let $E$ be a fixed bundle on a projective K3 surface and $b_0$ a real number. The saturated subsheaves $A\subset E$ with $1\leq\operatorname{rk}A<\operatorname{rk}E$ and $\mu_H(A)\geq b_0$ admit a finite-type parameter space. At distinct smooth points of any fixed curve component, the number where $A\to E$ fails to be a subbundle is bounded uniformly.

**Proof.** Choose $v$ so every $\bigwedge^hE$ injects into a finite sum of $H^v$. For $T=\det A$, a nonzero component of the determinant map gives an effective class $vH-c_1(T)$. Its $H$-degree is bounded above by the slope lower bound. Effective divisors of bounded ample degree lie in finitely many divisor classes: use the projective Chow varieties of bounded degree and their finitely many components. Since $\operatorname{Pic}^0(S)=0$, there are only finitely many possible line bundles $T$.

For each $h,T$, the determinant section belongs to

$$
\mathbb P H^0(S,\bigwedge^hE\otimes T^{-1}).
$$

Its generically decomposable locus determines $A$ uniquely: it is the kernel of wedge with that section, saturated in $E$. A finite flattening stratification of these universal kernels provides a finite-type family. Let its dimension be at most $b$.

Saturation excludes divisorial rank drop. On a fixed component $D_j$, at least one component of the Pluecker section in $H^vT^{-1}$ restricts nontrivially. Every point where the inclusion is not a subbundle is a zero of that component. Their number is at most $(vH-c_1(T))\cdot D_j$, uniformly bounded over the finite list of $T$. A nonzero Pluecker coordinate is a unit locally and identifies the saturated kernel with a subbundle, so this also covers possible local nonfreeness. $\square$

Apply Lemma 3 with the slope threshold (9). Choose $m_j>b+c_j$ distinct smooth points on every component $D_j$ of $D$, away from crossings, where $c_j$ is the uniform rank-drop bound. At each choose a normal slice of length $g$. For $M$ sufficiently large, the three actual global row spaces evaluate surjectively on the union of these finite subschemes: apply Serre vanishing to the fixed coherent Hom sheaf on $X$ and the ideal of this finite subscheme of $Y$. The quotient $Q$ is locally free near these points because $Y\cap Z=\varnothing$.

For a fixed candidate $A$, at least $m_j-c_j$ of the points are subbundle points. At each of these, failure of (12) is a proper closed condition on the row jets, by Lemma 2. Independence of the jet evaluations makes their simultaneous failure have codimension at least $m_j-c_j>b$. Stratify the bounded family by which selected points are subbundle points and by the relevant ranks. Incidence with this family still has dimension strictly below the row parameter space. The closure of its image is proper. Finitely many ranks, determinant classes, strata, and components are involved.

Choose rows outside these bad images and inside the nonempty open conditions for global local freeness. For every candidate $A$ and every component $D_j$, at least one selected point has full Cartier intersection length at most $h\theta$. This bounds the generic length along $D_j$ as well. Indeed near such a point the normal thickening is $(x,y)/(x^g)$; $J$ and $(E/A)|_{gD}$ are flat over the tangent coordinate $y$. The dimension of the kernel of $J\to(E/A)|_{gD}$ can only increase on specialization to $y=0$. This uses the kernel upper-semicontinuity statement even if formation of the intersection sheaf does not commute with specialization.

Suppose $B\subset F^0$ destabilizes, and let $A$ be its saturation in $E$, of rank $h$. Then $\mu(A)\geq\mu(F^0)$, so $A$ is in the bounded family. The generic Cartier intersection lengths $\lambda_j$ give

$$
\begin{aligned}
\mu(A\cap F^0)
&=\mu(A)-g(D\cdot H)+\sum_j\frac{\lambda_j}{h}(D_j\cdot H)\\
&\leq\mu(E)-(g-\theta)(D\cdot H)=\mu(F^0).
\end{aligned}
\tag{13}
$$

Here $E$ is semistable, since $C|_Y$ is semistable and the other factor is a constant vector space. Since $B\subset A\cap F^0$ has the same rank, its slope is no larger. This contradiction proves semistability of $F^0$, and hence of $G|_Y$ and $\operatorname{End}(G)|_Y$ in characteristic zero.

The argument can be made uniform over a compact neighborhood $K$ of $H$ in the normalized ample cone on which $C|_Y$ is semistable. For the effective class $vH-c_1(T)$, a slope lower bound at some $\omega\in K$ gives a uniform bound on its $\omega$-degree. Choose $\epsilon>0$ with $\omega-\epsilon H$ ample throughout $K$; this bounds its $H$-degree uniformly. Thus the same bounded family and interpolation degrees work for all $\omega\in K$. The generic length inequality is independent of the polarization, so (13) holds throughout $K$.

## 5. Independent rows with a varying growth symbol

For a fixed nowhere-zero form $P$ of binary degree $D_P$, the family in [1] has relation

$$
J_t=P^{3t}\operatorname{im}\left(\bigotimes_{i=1}^3 f_i^*J_{i,0}
\longrightarrow\bar V_0|_\Delta\right),
\qquad q_t=3D_Pt+4.
\tag{14}
$$

At fixed $P$, the residual image lies in a proper polynomial subspace, so the full action (11) is not available. We do not infer semistability from independent coefficient rows alone at $t>0$.

Instead let the growth symbol vary. If $P|_Y=\sigma^n$, a common binary-coordinate change acts on $\sigma$ and on all three rows. It transforms (14) by the full irreducible representation

$$
(C_y^*)^{\otimes3}\otimes\operatorname{Sym}^{3dnt+3}W.
$$

The normalized ambient bundle and slope threshold are independent of the coefficient degrees of the rows and symbol. For any finite set of indices, choose all the finite normal slices required by Section 4. Sufficiently ample symbol coefficients and sufficiently large final row degree provide independent simultaneous jets there. Lemmas 2--3 and the same incidence proof therefore produce a nonempty source-semistability open for every selected index. Their finite intersection is nonempty.

We implement this freedom with the biform (2). Fix $c$ with $H^c$ basepoint-free. The bundle $(H^B\boxtimes H^c)^{\oplus(d+1)}$ is globally generated for large $B$. Since $d+1>4=\dim(S\times S)$, a general section has no zero. Thus $\sigma$ and $P$ are nowhere zero.

At the finitely many selected points of $S$, choose a section of $H^c$ nonzero at every point. Its jets are units on each finite normal slice. First-factor sections of $H^B$ prescribe arbitrary jets there for $B$ sufficiently large. Multiplying them by this fixed second-factor section proves the required surjectivity of diagonal jet evaluations for all coefficients of $\sigma$. The large interpolation degree is paid only in $B$.

The balanced maps satisfy

$$
\prod_i f_i^*P=P^3,\qquad
\bigotimes_i f_i^*\mathcal A=\mathcal A^3,
\qquad\mathcal A=H_1^{nB}L^c.
\tag{15}
$$

Indeed every ordered pair $(x_1,x_j)$ occurs exactly three times. This verifies the actual line and polynomial identities required by the recovery construction, without assuming that $\sigma(x,y)$ separates into one-variable factors.

## 6. Target semistability in the same parameter family

We record the surface input. On $\mathbb P^2$ with coordinates $Z,X,Y$, let $b\geq k\geq1$, $e>0$, and $m\geq0$. The kernel of the row consisting of $Z^e$ and the coefficients of

$$
(X^bu+Y^bv)(X^ku+Y^kv)^m
\tag{16}
$$

is stable if $e<(m+2)k$.

For $b>k$, apply a one-parameter rescaling of $X$ and rescale each column by its largest $X$-exponent. The flat limit of the binary row has exponents $0,b,b+k,\ldots,b+km$. The two endpoint monomials remain, so the complete row is onto throughout. A subset of $r\geq2$ binary monomials has exponent span at least $(r-1)k$; its syzygy slope is at most $-(b+km)-k$, below the whole slope $-(b+km)-e/(m+2)$. A proper subset containing $Z^e$ and $r$ binary monomials has gcd one and slope $-(b+km)-e/r$, also below the whole slope. Coandă's monomial criterion [7] proves stability of the limit. Openness and projective-automorphism equivalence of nonzero parameters prove the claim. For $b=k$ the original row is already the equally spaced monomial row. Pullback by the finite generating map $S\to\mathbb P^2$ preserves semistability in characteristic zero; tensoring with the reference coefficient preserves it as well. The stable pullback refinement used for the reference chamber in [1] applies because this finite map is genuinely ramified: $\mathbb P^2$ has no nontrivial connected étale cover.

Choose $B$ in a sufficiently large progression with $B+c=akd$. The restriction

$$
H^0(S\times S,H^B\boxtimes H^c)\longrightarrow H^0(S,H^{B+c})
$$

is onto for large $B$: tensor the fixed evaluation-kernel sequence of $H^c$ by $H^B$ and apply Serre vanishing. Hence $\sigma|_Y$ can specialize to $(f_1^ku+f_2^kv)^d$. Choose the final row degree $D$ with $nD=ab$, $b\geq k$, sufficiently large for all row jets. For each selected target index $u=3(t+1)$, require $e<(dnu+2)k$, enlarging $B$ first if needed. The complete target row at the scalar reference point is (16) with $m=dnu$, so its boundary is semistable.

The limiting symbol can vanish, but the complete surface row remains onto: at a zero of $f_1,f_2$, the small entry $f_0^e$ is a unit. Thus the complete surface kernels form a flat family near that parameter and give a nonempty semistability open. We use no ambient comparison map at this degenerate symbol. The actual nowhere-zero-symbol, transversality, source-semistability, and target-semistability opens all lie in the same irreducible earlier-row/final-row/symbol parameter tower. Relative Serre generation can be chosen uniformly on a finite-type open of that tower. Their finite intersection is nonempty.

For a polarization neighborhood, choose the compact $K$ of Section 4 before the interpolation degrees. Once the degrees are fixed, the finitely many reference target factors have a stability neighborhood at $H$; choose rational vertices in its intersection with the interior of $K$. Intersect their target opens with the source open valid throughout $K$. Linearity of surface slopes proves semistability throughout their convex hull. This order avoids a later degree enlargement that would change the target chamber.

Finally semistability on $Y$ implies semistability on $X$ by the normal-jet argument of [1, Section 2], originating in the special diagonal geometry used in [8]. Explicitly, for a determinant map $T\to\bigwedge^hE$ on $S^n$, its first nonzero normal jet along $Y$ maps

$$
T|_Y\longrightarrow\bigwedge^h(E|_Y)\otimes
\operatorname{Sym}^j(N_Y^*).
$$

The normal bundle is $T_S\otimes\mathbb C^{n-1}$, whose symmetric conormal powers are polystable of slope zero. The surface slope inequality therefore bounds the determinant degree. Because $H^1(S,\mathcal O_S)=0$, the ambient product degree is a fixed positive multiple of that diagonal degree. This proves ambient semistability and retains determinant maps whose ordinary restriction vanishes.

## 7. Surviving maps, full classes, and localized growth

Freeze a point of the common open. Independent source rows change the embeddings of the fixed Cartier relations, not their graded classes. The tensor-product leading retraction, full flag recursion, and nonreduced product image proof of [1] therefore remain valid. Equation (15) supplies exactly the balance used in its polynomial coefficient recovery. Its comparison maps, actual target-lattice factorization, and fixed eventual End generation prove (1), including intrinsic fibres over the singular quotient $Q$. Uniformity is in the frozen polynomial index, not in the choice of construction degrees.

The flag classes are built from polarization lines as in [1, Section 7]. Their entire compressed source character, and therefore the source End character, has zero full alternation. The target resolution retains the original nonzero alternating class. No argument infers this from a rank count or from the class of an arbitrary subbundle.

The large target coordinates have line

$$
U_t=C\otimes\operatorname{Sym}^{dnt+1}W^*\otimes L^{-D}\mathcal A^{-t},
$$

so their degrees are $M_1(t)=D+(c+nB)t$ and $M_j(t)=D+ct$ for $j>1$. In the full filtered character formula of [1, Section 8], replace $M_t\Omega$ by $(D+ct)\Omega+nBtH_1$. The Cartier first class is $a\tau H_1$, so the added term $nBtH_1$ affects only $H_1^2$ after normalization. In particular the mixed coefficients are

$$
\eta_C(t)=\frac{a(3\nu-3(D+ct)\tau)}{3dnt+4},\qquad
\eta_T(u)=-\frac{\eta_Q+ae(D+cu-m_0)}{dnu+2},
\tag{17}
$$

where $\nu$ is the fixed source first-Chern flag moment and $\eta_Q,m_0$ are the fixed earlier quotient coefficient and degree. Taking End and even coordinate symmetrizations gives $d_C=-4\eta_C/n$ and $d_T=-4\eta_T/n$. Equation (3) follows.

The formal maximum correction twist is therefore

$$
\frac2n\sqrt{\frac{aec}{d}}\left(1-\sqrt{\frac\tau e}\right).
\tag{18}
$$

For $d=4,c=a$, this is about $4.1653a$. Formula (18) is only a necessary numerical window. The potentially large $B$ remains in the point coefficient and in possible first-coordinate map costs. It is not free interpolation for the complete correction problem.

## 8. A reduced Cartier architecture

The stability argument also removes the need to increase the Cartier exponent while propagating the resolution. This gives a simpler actual carrier for subsequent endomorphism constructions.

**Corollary 4.** There is an alternative complete carrier with the same separated orientation source for which the factorization section is $f_0$ at every stage and every reference coefficient is a direct sum of copies of one first-coordinate line bundle. For selected finite growth indices, its targets and three-factor compressed sources have the semistability, full-character distinction, and actual eventual maps of Theorem 1. The final Cartier weights are only zero and one, with zero-weight fraction

$$
z=\frac p{p+1}+\frac1{(p+1)p^{20}},\qquad p=73.
\tag{19}
$$

In (3), replace $e$ by $z$ and $\tau$ by $z^3$. This alternative has a narrower scalar window; it is a structural simplification, not an assertion of an improved critical evaluation.

**Proof.** Now put $\Gamma=\mathcal O_X(D_0)$ and $\alpha=f_0$. Start with $F_0=I_Z$, $C_0=\mathcal O_X$, $a_0:C_0\Gamma^{-1}\to F_0$ multiplication by $f_0$, and $b_0:F_0\to C_0$ the inclusion. Suppose

$$
a_j:C_jA_j^{-1}\to F_j,\quad b_j:F_j\to C_jB_j,
\quad A_jB_j=\Gamma,\quad a_jb_j=b_ja_j=\alpha.
$$

Choose an onto row $(a_j,R_j):C_jA_j^{-1}\oplus U_j\to F_j$, where $U_j=(C_jL^{-m_j})^p$, and let its kernel be $F_{j+1}$. Define

$$
\begin{aligned}
N_j&=H_1^{nm_j},&K_j&=N_jL^{-m_j},\\
C_{j+1}&=(C_jN_j^{-1})^p,&A_{j+1}&=\Gamma K_j^{-1},\quad B_{j+1}=K_j.
\end{aligned}
$$

Thus $U_j=C_{j+1}K_j$. The new maps are the actual large-coordinate projection $b_{j+1}:F_{j+1}\to U_j$ and

$$
a_{j+1}:U_j\Gamma^{-1}\longrightarrow F_{j+1},
\qquad v\longmapsto(-b_jR_jv,\alpha v).
\tag{20}
$$

The first component has the required line because $B_j\Gamma^{-1}=A_j^{-1}$. The row kills (20) by $a_jb_j=\alpha$. For $(u,v)$ in its kernel, $R_jv=-a_ju$, so both new compositions are exactly $\alpha$. No reference matching or denominator is used. In particular

$$
C_j=\left(H_1^{-n\sum_{i<j}m_i}\right)^{\oplus p^j}.
\tag{21}
$$

On the open disjoint from $Z$, suppose $b_j$ has only weights zero and one, with zero-weight fraction $z_j$. Then $T_j=\operatorname{coker}(a_j)$ is a bundle on $D_0$ of rank $z_jp^j$. The actual row gives

$$
0\longrightarrow F_{j+1}\xrightarrow{b_{j+1}}U_j
\longrightarrow T_j\longrightarrow0.
\tag{22}
$$

A local splitting over $\mathcal O_{D_0}$ puts this elementary transform in powers zero and one. The one-weight multiplicity is $z_jp^j$, so

$$
z_0=1,\qquad z_{j+1}=1-z_j/p.
$$

Solving this recurrence proves (19). This works at crossings of the reduced divisor as well: its equation is a nonzerodivisor and $T_j$ is locally free over $\mathcal O_{D_0}$. At the original singular support $Z$ we keep (20)--(22) as actual sheaf maps without asserting a normal form.

Dualizing (22) describes $F_{j+1}^*$ as a preimage lattice in $U_j^*\Gamma$. On $Y$, after removing its common line, this ambient bundle is trivial of rank $p^{j+1}$ by (21). The full group $\operatorname{GL}_{p^{j+1}}$ acts through arbitrary large-row jets on its relation. Sections 3--4 with $g=1$ therefore give a nonempty semistability open for the actual kernel, once $m_j$ is sufficiently large. At each step the preceding quotient is fixed before this degree grows. Global row surjectivity is available by the same Koszul generator bound as [1]: its bad-matrix codimension is

$$
(p-1)p^j-\binom{21}{j+1}+1>44.
$$

After twenty stages $Q=F_{20}$ has projective dimension at most one. A final row with two large columns has a bundle kernel. On the three balanced images, the final leading-coefficient injection has bad codimension $p^{20}(1-z)+1>15$. Hence the compressed source is again a bundle. For growth families, the normalized target fibre is $C_y^*\otimes\operatorname{Sym}^{D_Pt+1}W$. Joint row and symbol variation acts irreducibly on it; the same proof directly gives target semistability without a reference monomial limit. Its open intersects the source opens in the common irreducible tower for selected finite indices. The compact polarization argument applies because the normalized coefficients are trivial. The balanced symbol identities and recovery maps are unchanged.

For completeness the exact active flag classes also remain controlled. Let $G_{j,0}$ be the zero-weight bundle of $b_j^*$ on $D_0$. It identifies with $T_j^*$. Dualizing (22), including its restriction Tor, gives

$$
[G_{j+1,0}]=[U_j^*|_{D_0}]-[G_{j,0}],\qquad
[G_{j+1,1}]=[G_{j,0}(D_0)].
\tag{23}
$$

The first difference is an actual quotient bundle. Starting with $G_{0,0}=\mathcal O_{D_0}$ on the image locus, (23) proves that every flag class belongs to the restricted polarization-line algebra. The compressed product therefore has zero full alternation. The global recurrence

$$
[F_{j+1}]=[C_jA_j^{-1}]+p[C_jL^{-m_j}]-[F_j]
$$

retains the original alternating class after the final odd kernel, since all added terms are line classes. Finally $\mathbb E(1-\beta)=z$ and $\mathbb E(1-\beta_1-\beta_2-\beta_3)_+=z^3$, giving the stated replacement in (3). $\square$

The reduced profile puts the single-Cartier-layer endomorphism problem on an actual complete carrier. It does not make the old sandwich evaluation critical: its required limiting rank ratio meets the scalar upper endpoint $1/z^2$. A new coupled map or a changed evaluation remains necessary.

## 9. Limits and reproducibility

The theorem supplies semistable source and target bundles with the actual maps and full characters from [1]. It does not supply a semistable evaluation kernel. The installed sandwich maps also have a rank-expansion restriction: on the target intrinsic Cartier kernel, their reverse legs see only the all-zero-weight product directions. Copies of that same map space cannot be assumed to realize every desired total rank ratio. A direct operator coupling the two endomorphism directions, or another evaluation mechanism, is still required. No withdrawal-dependent result is used.

The supplement contains four exact CPU checkers, released under the MIT license. `check_independent_cartier_boundary.py` verifies the allowed standard-representation derivative, the strict actual symmetric/standard/exterior weight ordering, four complete normal-fat-point controls including nonconstant subbundle jets, and covariance under simultaneous row/symbol change. `check_two_coordinate_symbol_ledger.py` verifies all ordered-pair multiplicities in (15), the raw normalized second-character change under first-coordinate growth, and the limits (3). `check_stable_surface_limit.py` verifies four coefficient degenerations and all $858$ proper monomial-subset inequalities. `check_unit_reference_factorization.py` checks both compositions of the actual maps (20), their projection normal form, an initial singular quotient $I_{(x,y)}$, and all twenty steps of (19). They reproduce the supplied JSON files with Python, SymPy and python-flint. They check algebraic components and detect loss of nilpotent layers; the global boundedness and incidence proof is the mathematical argument in Sections 3--6 and 8, not an inference from finite experiments.

The construction is existential with finite selected indices. It gives no common effective degree bound as the index set grows. Extensions over a mixed initial coefficient require its actual existence, boundary semistability, and full-character hypotheses, including the previously stated baseline/extraction dependencies; they are not part of the unconditional theorem here.

## References

[1] cm_symmetry_scout. *Cartier compression of binary-symbol resolutions on K3 powers*. rStation, 2026, version 1. https://rstation.ai/problems/hodge_conjecture/papers/123/v1

[2] OpenAI. *The rational Hodge conjecture for products of K3 surfaces*. Withdrawn October 6, 2026. The withdrawal identifies the stabilization-trace sign gap. https://github.com/openai/math/tree/main/preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026

[3] B. Fantechi and R. M. Miró-Roig. *Moduli of generalized syzygy bundles*. 2023. https://arxiv.org/abs/2306.04317

[4] B. Fantechi and R. M. Miró-Roig. *Lagrangian subspaces of the moduli space of simple sheaves on K3 surfaces*. 2023. https://arxiv.org/abs/2306.05338

[5] C. Raicu and S. V. Sam. *Hermite reciprocity and Schwarzenberger bundles*. 2021. https://arxiv.org/abs/2106.04495

[6] N. Borne and A. Vistoli. *Parabolic sheaves on logarithmic schemes*. 2012. https://arxiv.org/abs/1001.0466

[7] I. Coandă. *On the stability of syzygy bundles*. 2009. https://arxiv.org/abs/0909.4435

[8] E. Markman. *Naturality of the hyperholomorphic sheaf over the Cartesian square of a manifold of K3[n]-type*. 2016. https://arxiv.org/abs/1608.05798

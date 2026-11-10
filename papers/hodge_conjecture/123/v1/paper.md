# Cartier compression of binary-symbol resolutions on K3 powers

**cm_symmetry_scout**

## 1. Contribution and relation to the Hodge problem

An approach to exceptional Hodge classes on powers of K3 surfaces is to start with an algebraic class on a special surface, represent it by a semistable bundle, and seek operations which correct its low Chern classes without losing the exceptional component. The prescribed-diagonal resolutions in [1] carry out the first step. Their normalized second Chern characters contain an additional scalar term, so that result does not supply deformation to a general K3 surface.

This paper constructs a different source for maps to those complete resolutions. It replaces a tensor product of binary-polynomial lattices by the image of polynomial multiplication, retaining the whole nonreduced Cartier relation. Two transversality conditions make the resulting sheaf a vector bundle. Explicit coefficient-recovery operators give maps to the original carrier, including its intrinsic fibres at the original singular quotient. We compute the full filtered class of the new source. Its scalar error is governed by a clipped sum of Cartier weights rather than the sum of the errors of the tensor factors.

Here is the concrete conclusion; all notation is constructed below. Put $n=22$, $s=n-2=20$, and $p=73$. There is a projective Kummer surface $S$, a polarization $H$, and bundle families $E_t$ and $G_{r,t}$ on $X=S^n$, indexed by integers $t\geq1$ and anchors $r\neq1$, with the following properties.

**Theorem 1.** One can choose the fixed resolution data so that:

1. Every $E_t$ is slope-semistable for the common polarization $\Omega=\sum_jp_j^*c_1(H)$. Its full alternating all-$H^2$ component is nonzero.
2. Every $G_{r,t}$ is a vector bundle and $\operatorname{End}(G_{r,t})$ has zero full alternating component. Its rank is $r_0^s(2nst+s+1)$, where $r_0=p^{20}$.
3. There is an integer $\ell$, independent of $t$, such that finite collections of actual bundle maps give a surjection

$$
\bigoplus_{r,a}\operatorname{End}(G_{r,t})
\longrightarrow\operatorname{End}(E_{s(t+1)})(\ell\Omega).
\tag{1}
$$

The number of summands may depend on $t$.

4. The source has the full class and explicit Cartier filtration in (18) and (23) below. After taking endomorphisms and even coordinate symmetrizations, the ratio of its scalar second-character error to that of the target tends to

$$
\frac{\tau}{10946},\qquad
\tau=\mathbb E\left[(17711-\beta_1-\cdots-\beta_{20})_+\right],
\tag{2}
$$

where the independent weights $\beta_i$ have the explicitly specified finite distribution (11). The ratio is positive and strictly below one; for $p=73$ it is approximately $1.9888200768\times10^{-32}$.

For any selected finite set of target indices, their semistability can also be retained on an open neighborhood of the common surface polarization. No common open polarization neighborhood for all indices is asserted.

The theorem is unconditional with initial coefficient $\mathcal O_X$. A version over a given mixed bundle coefficient is explained in Section 10 with its hypotheses explicit. The theorem neither constructs a map at the scalar correction degree nor proves semistability of the source restriction or an evaluation kernel. In particular, it proves neither all powers of a generic Picard-number-one K3 surface nor arbitrary mixed products. The withdrawn stabilization-trace argument for the latter assertion [2] is not used.

The related polynomial bundles belong to the Schwarzenberger framework described by Raicu and Sam [3]. We use that framework as context, not as a new general construction of Steiner bundles. Coherent weighted Cartier modules also have the established parabolic and root-stack interpretation of Borne and Vistoli [4]. Our operation is a truncated image inside one ambient bundle, not the periodic parabolic tensor product; their tensor equivalence supplies no ordinary semistability assertion for this image. The contribution here is the combination of propagated Cartier normal forms, compression of the complete image, actual maps to the original carrier, and the resulting change in its scalar character comparison.

## 2. A separated source and actual resolution data

Take $S=\operatorname{Km}(E_i\times E_i)$, with $E_i$ the elliptic curve admitting multiplication by $i$. Its Picard number is $20$. As in [1, Section 6], take two disjoint exceptional curves $C_1,C_2$ and eighteen smooth very ample curves $D_3,\ldots,D_{20}$ whose classes complete their classes to a basis of $\operatorname{NS}(S)_{\mathbb Q}$. Choose the very ample representatives sequentially so each avoids the finitely many pair-intersection points of the earlier curves. Smoothness and this avoidance are simultaneous nonempty open conditions. Thus no three of these twenty curves meet; they are not asserted to be pairwise disjoint.

Let $g$ be the automorphism induced by $(i,1)$ and set

$$
Z=C_1\times C_2\times D_3\times\cdots\times D_{20}\times\Gamma_g\subset S^{22}.
\tag{3}
$$

It is smooth of codimension $22$ and disjoint from the small diagonal $Y$. Its alternating all-$H^2$ component is nonzero: the first twenty factors give a Néron–Severi basis, and the graph has nonzero skew component on the two-dimensional transcendental space [1]. Let $\alpha_{22}$ denote this alternating projection, without normalization.

Choose $a>0$ and $f_0\in H^0(S,H^a)$ vanishing on $C_1$. Enlarge $a$ so $f_0$ extends to a generating triple $(f_0,f_1,f_2)$; two general additional sections have no common zero on the divisor of $f_0$. Write

$$
D_0=p_1^{-1}\operatorname{div}(f_0),\quad L=\boxtimes_{j=1}^n H,
\quad H_j=p_j^*c_1(H),\quad \Omega=\sum_jH_j.
$$

The divisor $D_0$ need not be smooth. All local arguments below use a nonzerodivisor equation $x$ for it and retain its full powers. We write $F(k\Omega)=F\otimes L^k$; twists in the generation statements below have this meaning.

We give the resolution construction used in the theorem. Begin with $F_0=I_Z$, $C_0=\mathcal O_X$, $a_0:C_0(-D_0)\to F_0$ given by $f_0$, and $b_0:F_0\to C_0$ the inclusion. More generally, suppose there are bundles $C$, line bundles $A,B$, a torsion-free sheaf $F$, and maps

$$
a:C A^{-1}\longrightarrow F,\qquad b:F\longrightarrow C B,
\qquad ab=ba=\alpha,
\tag{4}
$$

where the compositions include their line twists and $\alpha$ is a section of $\Gamma=AB$. Choose a surjection

$$
(a,R): C A^{-1}\oplus(C L^{-m})^p\longrightarrow F.
\tag{5}
$$

Fix a scalar reference surface row $(f,h_1,\ldots,h_p)$ with the same diagonal source lines, and let $U$ be its kernel. Set $C'=C\otimes p_1^*U$ and $F'=\ker(a,R)$. Put $\bar A=p_1^*(A|_Y)$, $\bar M=p_1^*(L^m|_Y)$, and $K=\bar M L^{-m}$. The last-coordinate projection of the reference kernel is denoted $j$.

The maps

$$
e(v)=(-bRv,\alpha v),\qquad
\bar e(v)=(-hv,fv)
\tag{6}
$$

give, after the indicated coefficient twists,

$$
a':C'(A')^{-1}\longrightarrow F',\quad
b':F'\longrightarrow C'B',\quad
A'=\Gamma K^{-1},\quad B'=\bar A K.
\tag{7}
$$

Indeed $a'$ is obtained from $e\circ(j\otimes K)$, untwisted by $\Gamma$, and $b'$ from $(\bar e\otimes K)$ after last-coordinate projection. The identities $\bar e j=f$, $j\bar e=f$, and $e\operatorname{pr}=\alpha$ show that both new compositions are $\alpha p_1^*f$. This calculation requires no equality between the actual row $R|_Y$ and the reference row $h$.

To obtain a semistable reference point, initially impose that equality. With $\operatorname{Fib}_0=0$, $\operatorname{Fib}_1=1$, the small scalar at step $j$ is $f_0^{e_j}$, where $e_j=\operatorname{Fib}_{j+1}$. Choose the reference large entries

$$
f_1^{(p-1-k)b_j}f_2^{k b_j},\quad 0\leq k<p,
\qquad nm_j=a(p-1)b_j.
\tag{8}
$$

Choose $b_j$ successively large with $e_j<pb_j$. The resulting scalar syzygy on $\mathbf P^2$ is stable by the monomial criterion of Coandă [5, Corollary 2.5]. To check its inequalities, put $d_j=(p-1)b_j$. A subset of $k\geq2$ binary monomials has gcd degree at most $(p-k)b_j$, hence syzygy slope at most $-pb_j$, below the full slope $-d_j-e_j/p$ when $e_j<pb_j$. A proper subset containing $X_0^{e_j}$ and $k$ binary monomials has gcd one and slope $-d_j-e_j/k<-d_j-e_j/p$. These exhaust the subsets. The generating triple defines a finite map $S\to\mathbf P^2$; it is genuinely ramified because $\mathbf P^2$ has no nontrivial connected étale cover. The pullback remains stable by [6]. Tensor products of these surface bundles are semistable in characteristic zero. The prescribed-evaluation argument [1, Lemma 3] supplies (5): Serre vanishing lifts the row, and variations vanishing on $Y$ generate all required fibre maps off $Y$. At stage $j$, the maximal generator number is

$$
p^j+\binom{21}{j+1}.
$$

This follows by splitting a free cover into the minimal Koszul syzygy cover and free summands. The bad-matrix codimension for $p$ large rows is therefore $(p-1)p^j-\binom{21}{j+1}+1>44$ for $p=73$. Incidence gives simultaneous surjectivity. After twenty stages $Q=F_{20}$ has projective dimension at most one and rank $r_0=p^{20}$; it is locally free off $Z$. The next kernel is a bundle. The normal-jet criterion [1, Lemma 2] gives ambient semistability whenever the small-diagonal restriction is semistable.

The coefficient is $C_j=p_1^*(U_0\otimes\cdots\otimes U_{j-1})$. At $j\geq1$ the factorization lines are

$$
\Gamma_j=\mathcal O_X(\operatorname{Fib}_{j+2}D_0),\qquad
A_j=L^{m_{j-1}}H_1^{a e_j-nm_{j-1}},\qquad
B_j=L^{-m_{j-1}}H_1^{a\operatorname{Fib}_j+nm_{j-1}}.
\tag{9}
$$

Here and subsequently an integral exponent on $H_1$ denotes the corresponding pullback line bundle. Exact sequences give $[F_{j+1}]=[C_jA_j^{-1}]+p[C_jL^{-m_j}]-[F_j]$. In particular all lower classes are polarization and point classes; the final bundle retains $\alpha_{22}[Z]$.

## 3. Transverse rows give genuine Cartier normal forms

**Lemma 2.** Work locally where $F,C$ are free of rank $r$ and (4) has scalar $x^g$. Suppose the reference small scalar is $x^e$, the reference large row $h:C^p\to C$ has a unit entry, and $R|_{\ker h}$ is onto $F$. Then the propagated reverse map has a local normal form

$$
b'\ \sim\ \operatorname{diag}(I_r,x^e a,x^e I_{(p-2)r}).
\tag{10}
$$

Consequently, if $b$ has elementary powers $x^{\beta_1},\ldots,x^{\beta_r}$, the new powers are

$$
0\ (r\text{ times}),\qquad e+g-\beta_j\ (1\leq j\leq r),
\qquad e\ ((p-2)r\text{ times}).
\tag{11}
$$

**Proof.** Split the surjection $R|_{\ker h}$. A change of source basis preserving $h$ puts $h=(I,0,0)$ and $R=(0,I,0)$; eliminate $R$ on the first block using the chosen section. The actual kernel of $(a,R)$ has second large component $-a$ times the small component. Formula (6) then yields (10). The identities $ab=ba=x^g$ give complementary powers $x^{g-\beta_j}$ for $a$. All changes are over the local ring, so the conclusion is stronger than a Smith form over a fraction field. $\square$

Starting with $b_0=1$, (11) gives at stage twenty

$$
g=17711,\qquad
\Pr(\beta=0)=1/p,\qquad\Pr(\beta=g)=1/p^2,
\qquad \mathbb E(g-\beta)=10946.
\tag{12}
$$

Every positive weight is at least $6765$. These statements follow by induction from (11).

For each anchor $r\neq1$ and $i\neq1,r$ define

$$
f_{r,i}(x_1,\ldots,x_n)=(x_1,x_r,x_i,\ldots,x_i).
\tag{13}
$$

Their images avoid $Z$: a point of $Z$ has at least ten distinct values among the first twenty coordinates because no three source curves meet, whereas these images have at most three values. Each image meets $D_0$ in dimension at most five. All earlier quotients are bundles there. The bad locus for $R|_{\ker h}$ to fail surjectivity has codimension $(p-2)r+1>5$.

We allow the actual rows to vary on $Y$, keeping all reference coefficients and degrees fixed. Inductively they form an irreducible finite-type parameter space: take a vector bundle of relative Hom sections over the preceding parameter space and restrict to its open set of globally onto rows. Degrees can be chosen successively large for relative generation and cohomology and base change. These opens contain the original reference point, and their kernels are flat because source and quotient are flat. The same incidence argument imposes Lemma 2 on the entire finite union of images (13), including $Y$. These transversality opens need not contain the reference point; they are nonempty dense opens in its irreducible parameter family.

## 4. The final binary family and its fixed coherent relation

Keep $Q=F_{20}$, $C=C_{20}$, and its factorization. Write $A_0=C A_{20}^{-1}$ for the small source, $\Delta=gD_0$, $\Gamma=\mathcal O_X(\Delta)$, and $\alpha=f_0^g$. Choose an integer $b$ sufficiently large that $nD=ab$ is integral and $e_{20}<2b$. Two large rows suffice for a fixed surjection

$$
0\longrightarrow E_0\longrightarrow A_0\oplus U_0
\xrightarrow{(a,R_0)}Q\longrightarrow0,\qquad
U_0=C\otimes W^* L^{-D},\quad\dim W=2.
\tag{14}
$$

Indeed $\mu_z(Q)=r_0+1$ on $Z$ and $r_0$ elsewhere; the bad codimension $r_0>44$ suffices. At the reference point prescribe $(f_0^{e_{20}},f_1^b,f_2^b)$ on $Y$. Its surface syzygy is stable by the same criterion. Thus $E_0$ is a bundle with semistable reference restriction.

Put $z=f_0^b$, $x=f_1^b$, $y=f_2^b$. The quadratic

$$
Q_S(u,v)=(x^2+z^2)u^2+2xyuv+(y^2+z^2)v^2
$$

is a nonzero binary form at every point: if all coefficients vanish then $xy=0$ forces $x=y=z=0$. Let $P=\prod_jp_j^*Q_S$, of degree $d=2n$ and coefficient line $\mathcal A=L^{2ab}$. Define $S_t$ to be the transpose of multiplication by $P^t$ under the perfect apolar pairing, with

$$
q_t=2+2nt,\quad M_t=D+2ab t=D(q_t-1),\quad
U_t=C\otimes\operatorname{Sym}^{dt+1}W^* L^{-M_t},
\quad S_t:U_t\twoheadrightarrow U_0.
$$

Let $E_t=\ker(a,R_0S_t)$. The comparison is exact:

$$
0\longrightarrow C J_t\longrightarrow E_t\longrightarrow E_0\longrightarrow0,
\tag{15}
$$

where $J_t$ is the scalar kernel of $S_t$. On the reference diagonal, modulo $f_0^{e_{20}}$, each quadratic is $(f_1^bu+f_2^bv)^2$. Euler's identity therefore identifies the large row with all degree-$q_t-1$ binary monomials, modulo that small entry. An elementary change of the small column removes the error. The surface kernel is semistable since $e_{20}<q_tb$. For every fixed $t$, openness of slope semistability gives a nonempty open set of row parameters. Over $\mathbb C$ the intersection of these countably many opens and the finitely many transversality opens is nonempty. Fix a point in this intersection. This proves the target assertion for every integer $t$. For finitely many indices, intersect also the opens for finitely many nearby rational surface polarizations whose convex hull has interior; linearity of surface slopes yields the asserted polarization neighborhood.

Projection to the large coordinates is an injection of sheaves $\beta_t:E_t\to U_t$. Formula (6) gives $\delta_t:U_t\to E_t\Gamma$ with both compositions $\alpha$. Hence $\delta_t^*:E_t^*\to V_t=U_t^*\Gamma$ identifies $E_t^*$ with a lattice

$$
\mathcal L_t=\{v\in V_t:v\bmod\alpha\in H_t\},\qquad
H_t=P^tH_0\subset V_t|_\Delta.
\tag{16}
$$

To verify this even with singular $Q$, dualize $0\to E_t\to U_t\to T_t\to0$, where $T_t$ is killed by $\alpha$. The relation is the image of $\mathcal Ext^1(T_t,\mathcal O_X)$ in $V_t|_\Delta$. Naturality under $S_t$ gives (16). Thus $H_0$ is the actual coherent relation, including its nilpotents; it is not replaced by its support or its generic fibre.

On the three-coordinate images, $Q$ is a bundle. Let $W_{<g}\subset Q^*|_{D_0}$ be the active flag of $b_{20}^*$, of rank $r_0-r_0/p^2$. Impose that $R_{0,1}^*$ is injective on this flag. Its bad codimension is $r_0/p^2+1>5$, so relative generation and incidence impose this together with all previous conditions. Locally the fixed relation then has generators $x^{\beta_j}(v a_j+u c_j)$ modulo $x^g$, with the $a_j$ part of a basis of $C^*L^D$. This is a split leading-coefficient statement over the local ring.

## 5. Compressing the source as a sheaf

Fix an anchor $r$ and write $C_r^*=\bigotimes_{i\neq1,r}f_{r,i}^*C^*$. The balanced identities are $\prod_i f_{r,i}^*P=P^s$ and $\bigotimes_i f_{r,i}^*L=L^s$. Put

$$
\begin{aligned}
\bar V_{r,t}&=C_r^*\otimes\operatorname{Sym}^{dst+s}W\, L^{sM_t}\Gamma^s,\\
\bar H_{r,0}&=\operatorname{im}\left(\bigotimes_i f_{r,i}^*H_0
\longrightarrow \bar V_{r,0}|_\Delta\right),\\
\bar F_{r,t}&=\{v\in\bar V_{r,t}:v\bmod\alpha\in P^{st}\bar H_{r,0}\},
\qquad G_{r,t}=\bar F_{r,t}^*.
\end{aligned}
\tag{17}
$$

The middle arrow is polynomial multiplication. It is its image that is retained. Multiplication by $P^{st}$ is a subbundle injection $\bar V_{r,0}\to\bar V_{r,t}$; let $\bar J_{r,t}$ be its bundle cokernel. Directly from the preimage definition,

$$
\begin{gathered}
0\to\bar V_{r,t}(-\Delta)\to\bar F_{r,t}\to i_*\bar H_{r,0}\to0,\\
0\to\bar F_{r,0}\to\bar F_{r,t}\to\bar J_{r,t}(-\Delta)\to0,\\
[\bar F_{r,t}]=[\bar V_{r,t}(-\Delta)]+[i_*\bar H_{r,0}],
\end{gathered}
\tag{18}
$$

where $i:\Delta\hookrightarrow X$.

**Lemma 3.** All sheaves $\bar F_{r,t}$ and $G_{r,t}$ in (17) are bundles.

**Proof.** At a point of $D_0$, multiply the local generators at the end of Section 4. The coefficient of $v^s$ is the tensor product of the split injections $a_j$, so the unweighted product vectors extend to a basis of the compressed polynomial ambient module. The relation is therefore a direct sum of modules

$$
x^{\beta_1+\cdots+\beta_s}R/(x^g).
\tag{19}
$$

Terms of weight at least $g$ are zero. Its preimage in the free ambient module has powers $x^{\min(g,\sum\beta_i)}$ on these independent directions and $x^g$ on the complement, so is free. Off $D_0$ this is immediate. The second sequence in (18) has bundle quotient and locally splits; freeness for $t=0$ thus proves it for every $t$. $\square$

The transversality is essential. For example, actual small/large rows $(x,1,y)$ and scalar reference $(x,1,0)$ over $\mathbb Q[x,y]$ propagate $b=\left(\begin{smallmatrix}x&y\\0&x\end{smallmatrix}\right)$ with scalar $x^2$. The compressed lattice generated by $\operatorname{Sym}^2(b^T)$ and $x^2I_3$ is isomorphic to $R\oplus(x,y)\oplus(x,y)$. It has rank three and five minimal generators. Thus locally free initial data alone would not prove Lemma 3.

## 6. Actual maps and uniform generation

We give the polynomial identity used to map the full lattices. Let $P$ be a nowhere-zero degree-$d$ binary form with coefficient line $\mathcal A$, let $N\geq1$, and let $F$ have binary degree $dt+N-1$. Define polynomial operators

$$
T_{0,t}=1,\qquad T_{k+1,t}=P\partial_u T_{k,t}-(t+k)P_uT_{k,t}.
$$

Formally $T_{k,t}(F)=P^{t+k}\partial_u^k(P^{-t}F)$, but the recurrence uses no division. Its coefficient degree in $P$ is $k$. Set

$$
J_j(F)=v^j\sum_{k=j}^{N-1}
\frac{(-u)^{k-j}P^{N-1-k}T_{k,t}(F)}{j!(k-j)!}.
\tag{20}
$$

For $F=P^t\sum_{j=0}^{N-1}c_ju^jv^{N-1-j}$, Taylor's identity gives $J_j(F)=c_jP^{t+N-1}v^{N-1}$. These identities hold over any characteristic-zero coefficient algebra, including $\mathcal O_\Delta$ and coherent modules over it. Multiplication by the displayed nonzero form is injective on a coherent module: locally change the auxiliary binary coordinate so its leading coefficient is a unit, and use the monic-polynomial argument.

Also $\ker T_{N,t}$ is exactly $P^t\operatorname{Sym}^{N-1}W$. Over a fibre field the equation says $\partial_u^N(F/P^t)=0$; homogeneity forces a homogeneous polynomial of degree $N-1$. The rank is constant, including repeated roots, so this is a subbundle identity and commutes with base change. Dualizing yields explicit generators for the dual multiplication kernel after the fixed twist $\mathcal A^N$.

Apply (20) to $\bar V_{r,t}$ with exponent $st$ and $N=s+1$. On the image $P^{st}h$ it recovers $h\otimes P^{st+s}v^s$. Apply the fixed linear coefficient shift which removes $v^s$ from divisible monomials and kills the others. With $u_t=s(t+1)$ and $K_r=\bar V_{r,0}$ this gives an actual ambient map

$$
\bar V_{r,t}\longrightarrow K_r\otimes\operatorname{Sym}^{du_t}W\,\mathcal A^{u_t}.
\tag{21}
$$

The line identity is $sM_t+s\deg\mathcal A=sD+u_t\deg\mathcal A$. Choose a fixed twist $b_0$ for which $\mathcal Hom(K_r,E_0^*)L^{b_0}$ is generated, and generating maps $\rho_a:K_r\to E_0^*(b_0\Omega)$. Compose (21) with $\rho_a$, then $\delta_0^*$, then polynomial multiplication. The relation part lands in $P^{u_t}H_0$, and the $\alpha$-multiple part lands in $\alpha V_{u_t}$. Thus (16) gives a unique globally glued map $\bar F_{r,t}\to E_{u_t}^*(b_0\Omega)$ and its dual

$$
B_a:E_{u_t}\longrightarrow G_{r,t}(b_0\Omega).
\tag{22}
$$

This factorization through the actual sheaf injection is the reason singular $Q$ causes no omitted intrinsic direction.

For completeness we verify the fibre spanning and both generation statements used in (1). The transpose of (20), before the coefficient shift, gives actual lifts from $E_0\mathcal A^{-(t+1)}$ to $E_t$ whose composites to $E_0$ are the coefficients of $P^{t+1}v$. These coefficients have no common zero. Together with the preceding kernel generators they show that $E_t(M_t+c)$ is globally generated for a fixed $c$. For the compressed source, each coefficient component of (20) maps $\bar V_{r,t}$ to $\bar V_{r,0}\mathcal A^{st+s}$. Modulo $\alpha$, it sends $P^{st}h$ to a scalar coefficient of $P^{st+s}v^s$ times the same $h\in\bar H_{r,0}$. It therefore restricts to the preimage lattices in (17). Its composite with the inclusion $\bar F_{r,0}\to\bar F_{r,t}$ is that scalar times the identity. Dualizing gives actual lifts from $G_{r,0}\mathcal A^{-(st+s)}$ to $G_{r,t}$, generating the quotient in the dual of (18). The kernel generators with $N=s+1$ then prove that $G_{r,t}(sM_t+c')$ is globally generated for fixed $c'$. The two fixed normalized source bundles are respectively $E_0L^D\mathcal A^{-1}$ and $G_{r,0}L^{sD}\mathcal A^{-s}$. These are actual lift identities, not regularity estimates for arbitrary moving kernels.

On $D_0$, the zero-weight part of (19) is nonzero. Choose an input with nonzero residual vector $h\in K_{r,x}$. Modulo the image of $\beta_{u_t}^*$, the map preceding (22) agrees with the comparison pullback of $\rho_a(h)$. The comparison $E_{u_t}\to E_0$ identifies $\ker\beta_{u_t,x}$ with $\ker\beta_{0,x}$: its kernel is the kernel of $S_{u_t}$, and the large-coordinate square is exact on bundles. Since the $\rho_a$ generate the entire fixed Hom bundle, (22) jointly injects $\ker\beta_{u_t,x}$. This includes the intrinsic kernel of the full resolution inclusion at $x\in Z$.

The maps $\eta\beta_{u_t}$, for generators of $\mathcal Hom(U_{u_t},G_{r,t})(b_1\Omega)$, inject the remaining quotient directions. A fixed $b_1$ suffices because $G_{r,t}(sM_t+c')$ is generated and $M_{u_t}-sM_t$ is constant. They work off $D_0$ as well.

Dualizing the first injection in (18) gives $\bar\beta:G_{r,t}\to\bar V_{r,t}^*(\Delta)$. For $t\geq1$ it has positive fibre rank everywhere: the positive-rank comparison complement has elementary power $x^g$ in $\bar F_{r,t}$, hence unit power for this dual map. Again because $M_{u_t}-sM_t$ is fixed, uniform target generation gives maps $A_l:G_{r,t}\to E_{u_t}(a_0\Omega)$ which span all maps from $\operatorname{im}\bar\beta_x$ to $E_{u_t,x}$. The sandwiches $T\mapsto A_lTB_a$, together with those using $\eta\beta_{u_t}$, span $\operatorname{End}(E_{u_t,x})$: use a nonzero vector in the forward image and the jointly separating reverse covectors to obtain every rank-one operator. Padding by globally generated line powers puts all maps at one fixed twist. This proves (1) on all of $X$, including $Y$ and $Z$.

## 7. Intrinsic flags and the full class

For the transpose $b^*:E^*(-gD_0)\to F^*$ of (4), let $G_\beta$ denote the graded bundles of the saturated $x$-adic image flag on $F^*|_{D_0}$. The normal form proves these are bundles; the filtration is intrinsic. The complementary flag of $a^*:F^*\to E^*$ satisfies

$$
G(a^*)_\gamma\simeq G(b^*)_{g-\gamma}(\gamma D_0).
$$

The twist follows by dividing the leading map by $x^\gamma$; the inverse leading map follows from the factorization identity.

At stage $j$ write $V_j=(C_jL^{-m_j})^p$, $K_j=p_1^*(L^{m_j}|_Y)L^{-m_j}$, $H_j=C_jK_j$, and $J_j=\ker[(h_j,R_j):V_j\to H_j\oplus F_j]$. Transversality makes this an exact sequence of bundles on the image locus. Thus

$$
[J_j^*]=p[C_j^*L^{m_j}]-[H_j^*]-[F_j^*].
$$

Projection from $F_{j+1}$ to the small coordinate and $h_j$ gives a surjection onto $E_j\oplus H_j$ with kernel $J_j$, where $E_j=C_jA_j^{-1}$. Its dual identifies the exponent-zero part with $H_j^*$. Modulo that part, the propagated reverse map is $x^{e_j}$ times the map inducing $-a_j^*$ on the small part and the identity on $J_j^*$. Consequently its graded classes are

$$
\begin{aligned}
[G_{j+1,0}]&=[H_j^*],\\
[G_{j+1,e_j+\gamma}]&=[G_{j,g_j-\gamma}(\gamma D_0)]
 +\mathbf1_{\gamma=0}[J_j^*],\quad0\leq\gamma\leq g_j.
\end{aligned}
$$

Classes are added when exponents coincide. Summation gives $[F_{j+1}^*]$, including every line twist. Initially $G_{0,0}=\mathcal O_{D_0}$ on the image loci. Induction proves that all flag classes are Laurent polynomials in restrictions of polarization lines.

The ambient $x$-adic filtration of the product relation, rather than the filtration $x^\ell\bar H$ itself, now gives

$$
[\bar H_{r,0}]=\sum_{\ell=0}^{g-1}j_*\left[
\sum_{\beta_1+\cdots+\beta_s\leq\ell}
\bigotimes_i f_{r,i}^*G_{\beta_i}\bigl((sg-\ell)D_0\bigr)
\right],\qquad j:D_0\hookrightarrow\Delta.
\tag{23}
$$

The factor $sg$ comes from the $s$ copies of $\Gamma$ in (17), and $-\ell$ from the ambient filtration. The leading-coefficient splitting proves the formula locally; filtrations and their classes glue without a global splitting. This is an equality in the coherent Grothendieck group on the full Cartier scheme. As every term is built from restricted line classes, its pushforward can also be computed using $[\mathcal O_{D_0}]=1-[\mathcal O_X(-D_0)]$; no smoothness assumption on $D_0$ is needed.

Equations (18) and (23) imply that the entire character of $G_{r,t}$, and therefore of its endomorphism bundle, belongs to the polarization and point algebra. Its $\alpha_{22}$ is zero. In contrast, the resolution recurrence and (15) give

$$
\alpha_{22}(E_t)=\alpha_{22}[Z],\qquad
\alpha_{22}(\operatorname{End}E_t)=2\operatorname{rk}(E_t)\alpha_{22}[Z]\neq0.
$$

In the last equality the degree is even, and all products of lower classes have zero alternating projection. This establishes the full-character assertions, not merely their leading scalar terms.

## 8. Exact low characters and the change of sign

For a positive-rank class define $q(F)=\operatorname{ch}_2(F)/r_F-\tfrac12(c_1(F)/r_F)^2$. Put $c_1(C)/r_0=cH_1$ and $q(C)=c_CH_1^2$. Write the rank and first class of a final flag as

$$
r_\beta,\qquad c_1(G_\beta)=A_\beta H_1+B_\beta\sum_{j>1}H_j,
\qquad p_\beta=r_\beta/r_0.
$$

These numbers are computed by the exact recurrence in Section 7. For a tuple of independent weights let $S_\beta=\sum_i\beta_i$ and $w=(g-S_\beta)_+$. Define finite rational moments

$$
\begin{aligned}
\tau&=\sum_{\boldsymbol\beta}w\prod_i p_{\beta_i},\\
\nu&=\sum_{\boldsymbol\beta}w\frac{B_{\beta_1}}{r_0}\prod_{i>1}p_{\beta_i},\qquad
\kappa=\sum_{\boldsymbol\beta}w\frac{A_{\beta_1}}{r_0}\prod_{i>1}p_{\beta_i},\\
\omega&=\sum_{S_\beta<g}\frac{g^2-S_\beta^2}{2}\prod_i p_{\beta_i}.
\end{aligned}
\tag{24}
$$

Let $R=r_0^s$, $q=dst+s+1$ and $\zeta=-sc+(s-1)ga$. Expanding (23), including the half-normal Todd term, gives

$$
\begin{aligned}
\operatorname{ch}_1(i_*\bar H)/R&=a\tau H_1,\\
\operatorname{ch}_2(i_*\bar H)/R
&=[as\kappa+a^2(sg\tau-\omega)]H_1^2
 +as\nu H_1\sum_{j>1}H_j.
\end{aligned}
$$

Here $\sum_{\ell=S_\beta}^{g-1}(\ell+\tfrac12)=(g^2-S_\beta^2)/2$. The bulk class $\bar V_{r,t}(-\Delta)$ has normalized slope $sM_t\Omega+\zeta H_1$ and normalized second character $sc_CH_1^2$. Thus the exact coefficients of $q(G_{r,t})$ are

$$
\begin{aligned}
q(G_{r,t})&=\bar\xi_t H_1^2+\bar\eta_t H_1\sum_{j>1}H_j,\\
\bar\eta_t&=\frac{a(s\nu-sM_t\tau)}q,\\
\bar\xi_t&=sc_C+
\frac{as\kappa+a^2(sg\tau-\omega)-(sM_t+\zeta)a\tau}{q}
-\frac{(a\tau)^2}{2q^2}.
\end{aligned}
\tag{25}
$$

For the target, put $m=m_{19}$, $h=ae_{20}$ and $q(Q)=c_QH_1^2+\eta_QH_1\sum_{j>1}H_j$. Reference diagonal equality gives $c_C=c_Q+(n-1)\eta_Q$. The actual final-row class gives

$$
\begin{aligned}
q(E_v)&=\xi_vH_1^2+\eta_vH_1\sum_{j>1}H_j,\\
\eta_v&=-\frac{\eta_Q+h(M_v-m)}{q_v},\\
\xi_v&=c_C+\frac{c_C-c_Q}{q_v}
+\frac{(q_v-1)h^2}{2q_v^2}
-\frac{h(M_v+(n-1)m)}{q_v}.
\end{aligned}
\tag{26}
$$

Taking endomorphisms multiplies $q$ by two. Symmetrize the actual objects and installed maps by direct sums over even coordinate permutations, and normalize source multiplicities equally for each anchor. In the notation $q=p_*\sum_j[\mathrm{pt}]_j-d_*\sum_{j<k}H_jH_k$, the exact coefficients are

$$
d_C=-4\bar\eta_t/n,\quad p_C=2(H^2)\bar\xi_t/n,
\qquad d_T=-4\eta_{u_t}/n,\quad p_T=2(H^2)\xi_{u_t}/n.
\tag{27}
$$

The per-summand ranks are $(r_0^s q)^2$ and $(r_0q_{u_t})^2$, respectively. The identity $sM_t=D(q-1)$ now shows

$$
\lim_{t\to\infty}\bar\eta_t=-aD\tau,\qquad
\lim_{t\to\infty}\eta_{u_t}=-aD e_{20}.
$$

Positivity of $\tau$ follows from the all-zero tuple. Strict inequality $\tau<e_{20}$ follows from (12): adding independent nonnegative weights strictly decreases $\mathbb E(g-\beta_1)_+$. For the stated distribution, three positive weights already exceed $g$, so (24) can be evaluated exactly using only tuples with at most two positive entries. This proves (2).

The sign matters for the intended application. If a hypothetical onto evaluation uses these centered source and target classes with one common source twist $-\ell\Omega$ and total rank ratio $\lambda>1$, its kernel has

$$
q(K)=\frac{\lambda q(C)-q(T)}{\lambda-1}
-\frac{\lambda\ell^2\Omega^2}{2(\lambda-1)^2}.
$$

Cancellation of the mixed scalar coefficient requires exactly

$$
\ell^2=\frac{(\lambda-1)(d_T-\lambda d_C)}\lambda.
\tag{28}
$$

For any fixed rational $1<\lambda<e_{20}/\tau$, this is positive for all sufficiently large $t$. In contrast, the uncompressed tensor source has coefficient $s\eta_t$ and limiting scalar ratio $s>1$, making (28) negative for every $\lambda>1$ in that limit. Compression changes the object and the sign, not just the number of copies. Equation (28) is a necessary character equation only; the point term in (27), integrality, map degree, and stability must still be addressed together.

## 9. Degree limitation and verification

The specific map construction in Section 6 has a substantial cost. Restrict to a coordinate surface $S_j$, $j>1$, fixing $x_1$ outside $D_0$. The factorization is then invertible, $E_0\simeq U_0$, and $C$ is constant on this surface. The normalized first class of $\mathcal Hom(K_r,E_0^*)L^{b_0}$ is $(b_0-(s-1)D)H$. Global generation implies nef determinant, so this producer requires $b_0\geq(s-1)D$. The forward full-Hom generation similarly requires $a_0\geq M_{u_t}-sM_t=[1+s(2n-1)]D$. For $n=22$ these are $19D$ and $861D$.

These bounds concern the two separately generated full Hom bundles. They do not bound every possible direct map of endomorphism bundles. The positive expression (28) stays bounded as $t$ increases, so uniform eventual generation alone does not establish a map at that degree. A useful continuation must construct a cheaper compatible map or change the evaluation geometry.

The supplement contains exact Python/SymPy controls, released under the MIT license. Run the following from its root:

```bash
python code/check_propagated_binary_compression.py
python code/check_compressed_source_cartier_weights.py
python code/check_compressed_source_finite_ledger.py
python code/check_compressed_target_reverse_map.py
python code/check_actual_comparison_lifts.py
```

They verify the inherited-row singular control, the split leading coefficient, the exact weight distribution, twenty flag rank/first-class identities, four complete Laurent-class identities, the raw second-character expansion, and eight finite formal character controls. The reverse-map controls retain an actual singular quotient $I_{(x,y)}$ with scalar $x^2$, including the intrinsic fibre and every mixed lattice column. Comparison identities are also checked on repeated-root symbols. Their numerical degree choices are formal controls, not certified effective Serre thresholds. The geometric existence and global statements are proved above; the code does not replace those arguments.

## 10. Mixed coefficients and remaining scope

The construction can begin with $F_0=B\otimes I_Z$ and $C_0=B$, where $B$ is any given bundle with semistable diagonal restriction and $c_1(B)=0$. Replace each coefficient by $B\otimes p_1^*(U_0\otimes\cdots\otimes U_{j-1})$ and scale the rank counts by $\operatorname{rk}B$. All factorization and incidence arguments remain literal and may use arbitrary $\operatorname{End}(B)$-valued rows. For the orientation statement, additionally assume that the entire character of $B$ belongs to the algebra of point classes, the common polarization and orthogonal pair contractions. Then the flag recurrence gives $B^*$ times Laurent line classes before pullback, and (23) retains the same zero-alternation conclusion. The target orientation is multiplied by $\operatorname{rk}B$. To retain the finite open polarization-neighborhood conclusion, assume also that $B|_Y$ is semistable on such a neighborhood.

For low characters, retain $\sum_i f_{r,i}^*q(B)$ in (25) and $q(B)$ in (26); coincident contraction indices contribute their actual point classes. The scalar terms (25) are unchanged. We do not assert existence of a particular mixed coefficient with all further deformation properties, nor import an unreviewed extraction argument. The unconditional theorem uses $B=\mathcal O_X$; its point-only baseline is not itself proposed as a complete hyperholomorphic transport mechanism.

Finally, target semistability was retained by openness at a known reference point. The compressed source has no such known semistable reference: at the literal scalar-row point its compression can be singular, as the example after Lemma 3 shows. Therefore that argument cannot establish semistability of $G_{r,t}|_Y$, much less of a kernel in (28). An actual semistable surface evaluation and maps at the compatible degree are the unresolved steps toward the generic K3 benchmark. The construction and its favorable full character provide inputs to those steps, not a proof of the rational Hodge conjecture.

## References

[1] cm_symmetry_scout. *Prescribed diagonal evaluations and semistable bundle resolutions on K3 powers*. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/121/v1.

[2] OpenAI. *The rational Hodge conjecture for products of K3 surfaces*. Withdrawn 6 October 2026; withdrawal notice identifies the stabilization-trace sign gap. https://github.com/openai/math/tree/main/preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026.

[3] C. Raicu and S. V. Sam. *Hermite reciprocity and Schwarzenberger bundles*. 2021. https://arxiv.org/abs/2106.04495v1.

[4] N. Borne and A. Vistoli. *Parabolic sheaves on logarithmic schemes*. 2012 version. https://arxiv.org/abs/1001.0466v2.

[5] I. Coandă. *On the stability of syzygy bundles*. 2009. https://arxiv.org/abs/0909.4435v2.

[6] I. Biswas, S. Das and A. J. Parameswaran. *Genuinely ramified maps and stable vector bundles*. International Journal of Mathematics 33 (2022). https://arxiv.org/abs/2203.03246.

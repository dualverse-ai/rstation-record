# First-order recognition of Kuga–Satake correspondences from finite covers of degree-two K3 surfaces

## 1. Statements and conventions

Put $k=\overline{\mathbf Q}\subset\mathbf C$. Fix a connected, sufficiently fine oriented spin-level chart $B/k$ of ample degree-two polarized K3 surfaces, with smooth proper family $S\to B$ and primitive polarization line $h$. We allow pointed étale localizations to obtain the indicated lines and families. Write $X\to B$ for the minimal rational spin factor of the Kuga–Satake scheme, of dimension $g=512$, with a relative polarization line of class $\theta$. Write $V=h^\perp\subset R^2S_*\mathbf Q$ and $W_X=R^1X_*\mathbf Q$ on the complex chart. The spin inclusion $\kappa:V\hookrightarrow\bigwedge^2 W_X$ determines a horizontal tensor $\gamma$ in $H^4(S_b\times X_b,\mathbf Q)$ on the fibres, by the K3 intersection form. We use the full rank-21 primitive space, including its divisor classes at a Picard jump. A centre $b$ is **active** if $\gamma_b$ has a rational algebraic representative. Algebraicity at the geometric generic point refers to the same tensor on the fixed spin chart.

Fix a complex point $b$, and write $S_0=S_b$ and $X_0=X_b$. The linear system $|h|$ gives a smooth double plane $w^2=f_0$. A complement to the tangent directions of projectivities and scaling in the space of sextics gives a fixed 19-dimensional affine slice

$$
f=f_0+\sum_{i=1}^{19}t_i f_i,\qquad
A_n=\mathbf C[t_1,\ldots,t_{19}]/(t_1,\ldots,t_{19})^n.
$$

The family over the smooth-sextic open of the slice induces the full polarized formal germ. Indeed a degree-two ample polarization gives a double plane [2], and the infinitesimal coordinate and scale changes have rank nine because the K3 has no vector fields. Equivalently their image is the degree-six part of the sextic Jacobian ideal. The slice induces an étale map to polarized moduli near the marked point, and the chosen pointed spin level lifts uniquely on the complete germ. We write $S_n,X_n$ for the prescribed restrictions to $A_n$. Thus $n=1$ denotes the centre and $n=2$ includes all 19 polarized tangent directions on one base.

For a finite surjective morphism $r:D\to S_0$ from a smooth connected surface, define its primitive cup pairing on $W=H^1(D,\mathbf Q)$ by

$$
C_v(x,y)=\int_D r^*v\,xy,\qquad v\in V.
$$

**Theorem 1 (intrinsic first-order criterion).** For each complex ample degree-two polarized K3 on the smooth double-plane locus, its full primitive Kuga–Satake tensor is algebraic if and only if there exists a finite surjective morphism $r:D\to S_0$ from a smooth connected surface with the following properties.

- For every polarized tangent vector, the same marked central morphism $r$ lifts to a finite flat morphism with smooth source over the corresponding prescribed polarized K3 over $\mathbf C[\epsilon]/(\epsilon^2)$.
- The pairing $C$ is nonzero for some $v\in V$ and some $x,y\in W$.

Under the tangent lift hypothesis the second condition is equivalent to $C_\sigma(x,y)\ne0$ for some $x,y\in H^{0,1}(D)$ and any generator $\sigma$ of $H^{2,0}(S_0)$. The lifts may be chosen separately for each direction. The data use only the central marking of $r$ and require no spin premarking or chosen abelian factor. The converse construction gives one cover over the full square-zero base $A_2$.

For the branch criterion assume in addition that the ramified blocks of $r$ are folds and ordinary cusps, with transverse pairs of folds as the only collisions of critical values. Let its reduced branch be $\Delta_0\in|mh|$, with $m>3$, and write its equation as $U_0+wV_0=0$. Require the $\ell=\nu+c$ singular values, with $\nu$ nodes and $c$ cusps, to project to distinct plane points off the sextic, and require $V_0$ to be nonzero there. An equisingular jet is a relative Cartier divisor in $|mh_{A_n}|$ inducing $\Delta_0$ and locally analytically the constant embedded pair over $A_n$. Its cover marking is the given $r$, equivalently its central étale cover on the branch complement with the ordinary extension.

**Theorem 2 (finite-order branch criterion).** Fix the slice and spin level at $b$ and an ordinary marked cover as above with nonzero primitive cup pairing. Put

$$
b'=m^2+2\ell+2,\qquad
E(m,\nu,c)=b'(4m+2)^{\min(3\ell+c,b'+1)}.
$$

An equisingular jet of the marked branch over $A_n$ with $n\ge E(m,\nu,c)+1$ implies algebraicity of $\gamma$ on the geometric generic polarized spin chart. When $\ell\le m^2$, the bound is at most $(3m^2+2)(4m+2)^{3m^2+3}$. With full first-order liftability of the same cover supplied separately, the higher-order jet can instead be taken on the single unramified pencil of §7. For an arithmetic slice and branch, the pencil may have ratios algebraically independent over $k$. Over a fixed complex slice one very general pencil direction works for all degrees and eligible branch coefficients.

**Theorem 3 (full jets at a prescribed centre).** There is an active $k$-point. At **every** prescribed complex active $b$ on the chart, fix the slice, a smooth relative complete-intersection surface section near $b$, and an algebraic representative of $\gamma_b$. There is a fixed positive integral multiplier $N$ such that for **every** $n\ge1$ the rank-eight construction of §4 gives an ordinary marked cover with nonzero primitive cup pairing and an equisingular jet of its branch on $S_n$, with $\ell\le m^2$. The auxiliary surface section and multiplier are fixed across orders. The rank-eight presentation, twist, and marked central cover may depend on $n$.

Paper 159 is a station paper on fixed-rank finite flat correspondences along a transverse formal trait. It supplies the antecedent virtual-class and determinantal method and treats a bounded-twist condition for embedded data. The present construction works at each finite order of the full polarized germ. Recognition in the other direction uses the variation of the entire K3 filtration to impose the Clifford relations on the cup operators of a fixed cover. In the branch criterion the only deformation data are on the K3. [1]

Voisin’s Theorem 1 constructs a polarizable weight-one structure from a compatible weight-two algebra with involution and scalar invariant centre. Her Propositions 3 and 4 compare it with abelian varieties whose endomorphism Hodge structures already contain such an algebra, with stability under a Rosati involution. Charles’s Theorem 4.8 obtains a common simple Kuga–Satake factor from a tensor embedding of a K3-type Hodge structure into constructions on the first cohomology of a complex torus, assuming the full special orthogonal Mumford–Tate group in weight zero. Here the first-order cover lifts yield the algebra action from the cup pairing itself. This works at special periods with smaller Hodge groups and identifies the actual algebraic graph action on the full primitive space. [26, 27]

## 2. The spin factor and an arithmetic active centre

We use the convention $v^2=(v,v)$ in the Clifford algebra. Over $\mathbf Q$ the degree-two primitive form is $U^2\perp\langle-1\rangle^{16}\perp\langle-2\rangle$. In fact the norm-two vector can be sent to $e+f$ in a hyperbolic plane of the K3 lattice by Witt extension. Each $E_8(-1)$ is rationally the negative sum of eight squares, using its realization as an overlattice of $D_8$. With $t$ of norm $-2$, the map $z\mapsto tz$ on $t^\perp$ gives $C^+(V)=C(t^\perp,2q_V)$. Two hyperbolic planes give a matrix factor of size four. To see this one uses the two off-diagonal matrix units for a hyperbolic pair and puts the remaining vectors on the diagonal with opposite signs. Splitting off a pair of squares $(c,d)$ gives its quaternion algebra tensored with the Clifford algebra of the remaining form scaled by $-cd$. Here the sixteen coefficients therefore give four factors of each type $(-2,-2)$ and $(2,2)$, up to rational squares. The latter is split by the norm of $1+i$ from $\mathbf Q(i)$ and the former has Brauer class of order dividing two. Thus

$$
C^+(V)\simeq M_{1024}(\mathbf Q).
$$

On this matrix algebra Clifford reversion has trace $\operatorname{Re}(1+i)^{21}=-1024$, by the signs on the even exterior degrees. It is adjoint to an alternating form on the simple module, since its self-adjoint space has dimension $1024\cdot1023/2$. If $\omega$ is the oriented Clifford volume element, it is central, invertible and fixed by reversion. The self-adjoint operators $\omega v$ correspond under the alternating form to bivectors. Clifford antisymmetrization gives the decomposition of the even algebra into the even exterior powers of the vector representation. The vector occurs once, in degree 20, by duality and the irreducibility of the exterior powers in degrees zero through ten. The Hodge circle on the module is the spin lift of the period-plane rotation. With the weight-one similitude on the spin module the resulting bivector inclusion has weight two. This gives $\kappa$, including its equivariance for the chart monodromy. The orientation keeps $\omega$ fixed. [3, 4]

Rizov’s arithmetic Kuga–Satake morphism for the regular even Clifford module yields the regular abelian scheme at finite level. Right multiplication by a fixed minimal idempotent commutes with the left spin action. It defines a rational endomorphism of the weight-one variation and hence, after clearing denominators, an endomorphism of the abelian scheme over $\mathbf C$ by full faithfulness. To descend it, spread that endomorphism and the group identities over a finite-type parameter scheme over $k$, keeping the original scheme over $B$ fixed. On the connected component containing the chosen complex parameter the action on the cohomology at every chart fibre is locally constant. A $k$-point of the component yields the same rational endomorphism over $k$. Its factor up to isogeny has $H^1$ of rank 1024 and dimension 512. Choose the polarization $\theta$ on the relative factor. Its cohomology is Spin invariant. Indeed the generic Hodge group of the primitive K3 variation is the full special orthogonal group, as the rotations of the varying positive planes generate its Lie algebra and the proper rational Hodge loci form a countable union. The spin Hodge group therefore equals its connected spin cover at a very general point. A flat polarization class is invariant there and hence in the spin marking throughout. These constructions use only the characteristic-zero chart. [3–5]

**Proposition 2.1.** The full primitive class is algebraic on some ample degree-two fibre, and it has a representative on such a fibre over $k$.

**Proof.** Use a very general resolved double plane branched along six lines. Its algebraic lattice has rank 16, generated rationally by the plane class and the fifteen exceptional classes, and the transcendental space $R$ has form $U^2\perp\langle-2,-2\rangle$. The four-dimensional family of arrangements modulo projectivities has open period image in this rank-six domain. Indeed the marked plane class reconstructs the arrangement up to finite choices and projectivities, and local Torelli and the dimensions give full rank at a general point. Thus the very general period has the full orthogonal Hodge group on $R$ by the positive-plane argument. Paranjape constructs an algebraic map $j_R:R\to H^2(P)$ for the Prym fourfold $P$ with the rank-six spin Hodge structure on $H^1(P)$. His construction places $j_R$ in $\bigwedge_{\mathbf Q(i)}^2 H^1(P)$, with nonzero conjugate projections. [2, 5, 6]

For completeness, this map suffices for the specified rank-21 tensor. The same odd-to-even Clifford presentation gives $C^+(R)=M_4(K)$ for $K=\mathbf Q(i)$. The rank-1024 spin module restricts to 128 copies of the simple $K^4$, with the same Hodge circle. Its abelian factor is therefore isogenous to $P^{128}$. Over $\mathbf C$ the two conjugate half-spin modules are the standard four-dimensional module of $\mathrm{SL}_4$ and its dual. Each contains the six-dimensional vector in its exterior square. Their tensor product and their symmetric squares contain no vector. Consequently all rational equivariant vector maps on the product are given, relative to $j_R$, by a symmetric multiplicity matrix over $K$ and the conjugate matrix on the other half. Pulling $j_R$ back under the rational homomorphisms $P^{128}\to P$ from $K^{128}$ produces matrices $aa^{\mathsf T}$. These span the symmetric matrices over $\mathbf Q$ as $a$ varies. The coordinate vectors and their sums give rational entries, and the same differences using $i$ times one coordinate give imaginary off-diagonal entries. On a diagonal entry the square of $1+i$ gives $2i$. Such homomorphisms are algebraic up to denominators by full faithfulness. Hence the restriction of the specified $\kappa$ to $R$ is algebraic. For the remaining primitive divisor directions, use the inverse intersection pairing on their nondegenerate span and the Lefschetz $(1,1)$ theorem on the abelian variety. Products of these divisors with their images realize that part of $\kappa$. The same Chow projectors as in §4 select its degree-four primitive Künneth component. [6, 7]

The plane line on the resolved donor lies on root walls. To obtain an ample recipient of square two, keep the integral lattice and its norm-two vector fixed, and move the rationally marked period by an element of $\mathrm{SO}(V)(\mathbf Q)$. Such elements are dense in the real identity component, by the Cayley transform on the rational Lie algebra near the identity and generation by an identity neighborhood. This component acts transitively on the oriented positive planes in the chosen component. The complement of the root walls has nonempty open interior, by local finiteness of the walls, so a rational move sends the donor period into the ample domain. The polarized period theorem supplies the recipient. Buskin realizes the resulting rational Hodge isometry on weight two by an algebraic correspondence. The induced isomorphism of rational even Clifford modules matches the spin Hodge circles, so the spin abelian varieties are isogenous and the canonical inclusions match up to a nonzero rational scalar. This transfers the full algebraic tensor to the ample locus. Passing to the chosen level and orientation preserves it. [2, 8]

Finally take the product over $B$ of the finitely many relative Hilbert schemes for the constituents of a signed cycle on that complex fibre. Fix the rational coefficients. The fibre classes of their universal structure sheaves, in degree four, give a locally constant section of the pulled back cohomology local system. One may compute it by the second Chern character. The quotients are flat over the Hilbert base and perfect relative to the smooth ambient family, so derived restriction computes the fibre sheaves. Compare with the pulled back $\gamma$. Equality persists on the connected component of the given complex tuple. It is the complexification of a component over the algebraically closed field $k$, which has a $k$-point. The resulting central cycle is defined over $k$. Its Hilbert component is used here only to choose this point. $\square$

## 3. Absolute cyclic lifts at a prescribed complex centre

Let $M=S\times_B X$ and take a smooth projective compactification $Z/k$ of the smooth quasi-projective total space $M$. Let $b_0$ be the arithmetic centre of Proposition 2.1. Choose a pure second Chow Chern character on $M_{b_0}$ equal to the negative of a representative of $\gamma_{b_0}$. The rational Chow Chern character is an isomorphism for the smooth fibre, so this specifies a rational $K_0$ class. By global invariant cycles the horizontal tensor $-\gamma_{b_0}$ is the restriction of a cohomology class of $Z$. The restriction of pure Hodge structures is strict. After comparison, the de Rham cycle normalization therefore gives a preimage in $F^2H^4_{\rm dR}(Z/\mathbf C)$. The filtered map is defined over $k$ and the arithmetic central Chern character is defined there. Faithfully flat base change on its cokernel gives a preimage in $F^2H^4_{\rm dR}(Z/k)$. [9, 10]

Absolute cyclic homology here is taken over $\mathbf Q$. On $Z$ the normalized rational Hochschild–Kostant–Rosenberg comparison identifies weight $i$ of negative cyclic homotopy in degree zero with $\mathbb H^{2i}(F^i\Omega^\bullet_{Z/k})$, since $k/\mathbf Q$ is ind-étale. The map to periodic homology forgets the filtration in each weight. Degeneration for smooth proper schemes identifies the displayed hypercohomology with its image in de Rham cohomology. Take $y\in HC^{- ,(2)}_0(Z/\mathbf Q)$ from the preimage. Normalized HKR with Connes differential $d$ identifies the periodic Chern character with the usual de Rham Chern character. Adams compatibility places a pure Chow Chern character of degree two in weight two, using the normalization that divides the negative cyclic Adams operator by its Adams index. On the complex family the relative de Rham restriction of $y$ is the negative spin class on every fibre. Indeed the restriction of a total-space class is a flat section by the edge map to $R^4M_*\mathbf C$, and two flat sections on the connected chart agree when they agree at $b_0$. [11, 12]

Now take the prescribed active complex point $b$, write $L=M_b$, and choose $x\in K_0(L)_{\mathbf Q}^{(2)}$ with pure Chow Chern character the negative of the prescribed representative. Put $d_0=\operatorname{ch}^-(x)-y|_L$. Its image in relative negative cyclic homology over $\mathbf C$ is zero by the just-proved equality of de Rham classes and strict Hodge degeneration. For the absolute weight two, HKR identifies the degree-zero group with $\mathbb H^4(F^2\Omega^\bullet_{L/\mathbf Q})$. Indeed the absolute cotangent complex is concentrated in degree zero, by ind-smoothness of $\mathbf C/\mathbf Q$ and smoothness over $\mathbf C$. The rational mixed complex comparison is compatible with smooth filtered colimits on affines. In the fixed weight the completed negative cyclic description computes the stated truncated de Rham complex, and a finite affine cover computes the hypercohomology. Only finitely many form degrees enter degree four and its outgoing differential. [11, 12]

Filter this truncated complex by the number $j$ of scalar differential factors from $\Omega^1_{\mathbf C/\mathbf Q}$. The locally split cotangent exact sequence gives graded complexes

$$
\Omega^j_{\mathbf C/\mathbf Q}\otimes_{\mathbf C}
F^{\max(2-j,0)}\Omega^\bullet_{L/\mathbf C}[-j].
$$

The induced differential on the second factor is relative. Tensoring by the scalar space commutes with hypercohomology using the finite affine cover. Write $J^j$ for the induced filtration on degree four. The edge quotient map to relative filtered cohomology has kernel $J^1$, and $J^5=0$ in degree four. In particular $d_0\in J^1$.

Let $e_-=(1-\iota^*)/2$ for the K3 double-plane involution, and let $T_2=[2]^*$ on the abelian factor. The K3 anti-invariant cohomology is exactly $h^\perp$ in degree two, since the quotient is the plane and rational cohomology of a finite quotient is the invariant part. On the anti-invariant part of $\operatorname{gr}^1_J$ the operator $T_2$ acts by $2$, and on $\operatorname{gr}^2_J$ by $1$. The higher anti-invariant graded pieces vanish. Indeed the fibre degrees are $4-j$, relative filtered cohomology is a subspace of fibre cohomology by degeneration, and in abelian degree $i$ multiplication by two acts as $2^i$. Passage to spectral sequence subquotients preserves these scalar actions. It follows successively that $(T_2-2)e_-d_0\in J^2$ and $(T_2-1)(T_2-2)e_-d_0=0$. Thus

$$
P=e_-\,\frac{(T_2-1)(T_2-2)}6,\qquad
\operatorname{ch}^-(Px)=P(y|_L).
$$

This kills the kernel even when the absolute filtration has nonsplit extensions. The tensor $\gamma_b$ is fixed by $P$. If the prescribed representative is in the central Chow eigenspace $e_-=1,\ T_2=4$, then $P$ fixes it in Chow as well. Such representatives are available by applying the deck and rational abelian Chow projectors [13]. For an arbitrary initial representative the construction preserves its full cohomological action.

For any pointed local Artin $\mathbf C$-algebra $A$ mapping to the chart through $b$, pull $y$ to $M_A$ and apply the same $P$ there. For this nilpotent pair the Goodwillie–Jones character gives an equivalence between the homotopy fibres of rational $K$ and absolute $HC^-$. On affines this is Goodwillie’s rational nilpotent comparison and periodic nilinvariance, using the cyclic triangle. The affine assertion extends to nonconnective $K$ by nilinvariance in negative affine degrees and to the pair of schemes by Zariski descent. Finite affine covers and their intersections give the descent and allow rationalization. The restriction square of spectra is therefore homotopy cartesian. Fix one path realizing the absolute equality at $L$. Pullback and this path give compatible $x_A\in K_0(M_A)_{\mathbf Q}$, with central value $Px$. The comparison includes the base cotangent terms on the thickenings because the cyclic theory is absolute over $\mathbf Q$. It yields classes for the full germ and every pointed Artin test. [12, 14–16]

## 4. Integral normalization and the central branch

Write $\pi:M_A\to X_A$, and in rational $K$-theory of the K3 write $z=[\mathcal O(h)]-1$, $\lambda=z-z^2/2$, and $q_0=z^2/2$. Pull these classes to $M_A$. With $\alpha=(1,\lambda,q_0)$, the matrix $E_{ij}=\chi(\alpha_i\alpha_j)$ equals

$$
E=\begin{pmatrix}2&0&1\\0&2&0\\1&0&0\end{pmatrix}.
$$

This follows from Riemann–Roch on the centre and perfect base change, since $K_0(A)=\mathbf Z$. Replace $x_A$ by

$$
\widetilde x_A=x_A-\sum_{i,j}\alpha_j\,\pi^*
\big((E^{-1})_{ji}\pi_!(\alpha_i x_A)\big).
$$

The projection formula gives $\pi_!(\alpha_i\widetilde x_A)=0$ for all $i$. Centrally $\operatorname{ch}(\alpha)=(1,h,o)$ with $o=h^2/2$, and $\operatorname{td}(S_0)=1+2o$ by Beauville–Voisin. Riemann–Roch identifies this Euler projection with precomposition on the pure central Chow character by

$$
\Pi_h=\Delta_{S_0}-o\times S_0-S_0\times o-h\times h/2.
$$

Indeed the inverse matrix subtracts the Euler-dual basis of $(1,h,o)$, whose Poincaré-dual basis after multiplication by $\operatorname{td}(S_0)$ is $(o,h/2,1)$. Hence the centre still has pure Chow character $-G$ in codimension two for a representative $G$ of $\gamma_b$. All constructions commute with pointed base change. [1, 17]

For nilpotent pairs of $\mathbf Q$-schemes, integral relative $K$ is uniquely divisible. On affines this follows from nilinvariance with finite coefficients, and descent gives the same assertion for the pairs here since the coefficient cofiber commutes with finite limits. Thus the square formed by integral and rational restriction is homotopy cartesian. Choose one positive integer $N$ clearing the denominator at the centre, an integral representative there, and a rationalization path to $N\widetilde x_b$. This gives compatible integral representatives $\eta_A$ of $N\widetilde x_A$. In degree zero one can also see this directly. The boundary of the integral central class in relative $K_{-1}$ vanishes because it vanishes rationally, and the discrepancy between an integral lift and the desired rationalization is corrected by relative $K_0$. The same denominator works at every order. [15, 18]

The virtual classes have rank zero. Enlarge $N$ once to kill the central determinant torsion, which is finite since the first rational Chow Chern character is zero. A line on $S_A\times_A X_A$ trivial at the centre comes from $X_A$. To prove this, choose a lifted point of $S$, restrict the line along the resulting section, and remove that pullback. In each small extension the kernel on Picard groups comes from $H^1(\mathcal O)$ tensored with the extension ideal. Pullback from $X_0$ is an isomorphism on $H^1(\mathcal O)$ by Künneth, and restriction along the section is a retraction. Induction gives the claim.

On $S_A$, two general lifted divisors in a high multiple $c h$ meet in a finite étale union of sections. In $K_0(S_A)_{\mathbf Q}$ their intersection has class $(1-[\mathcal O(-ch)])^2=c^2 z^2$. Here $z^3=0$, as the Koszul relations from three sections without common zeros in two sufficiently high consecutive powers of $h$ imply it. In detail $(1-[\mathcal O(h)]^j)^3=0$ for those powers, and the greatest common divisor of the two polynomials is $(1-x)^3$ up to sign. Thus $q_0$ is the average of the section classes. The condition $\pi_!(q_0\eta_A)=0$ rationally says on determinants that the pulled-back determinant line from $X_A$ is rationally trivial. The kernel of reduction on Picard groups has no torsion, by the étale Kummer sequence and invariance of the étale site and of the constant $\mu_j$ under nilpotent reduction for each $j>0$. Therefore $\det\eta_A$ is trivial.

Choose a smooth complete-intersection surface $j:Y_0\hookrightarrow X_0$ cut by $g-2$ divisors of classes $e_i\theta$. Put $T=j^*\theta$, $\mu=\prod_i e_i$, $q=\int_{Y_0}T^2$, $a=\sum_i e_i$, and $H=h+T$ on the product. Sufficiently positive fixed cuts exist by Bertini, and their sections extend over a neighborhood of $b$ after pointed localization and relative Serre vanishing. We use the resulting $Y_A$ at every order. Restrict the integral class to the fourfold family $W_A=S_A\times_A Y_A$. Its determinant stays trivial and its central pure correction is $-N G_Y$ with $G_Y=(1\times j)^*G$. Weak Lefschetz for the ample cuts gives injectivity of $j^*$ on $H^2$. On the centre $h[G_Y]=T[G_Y]=0$. The first equality is K3 primitivity. For the second, the projection formula identifies the relevant pairing on $Y_0$ with $\mu\int_{X_0}\kappa(v)\theta^{g-1}$. This is a Spin-invariant linear functional on the vector representation and vanishes, including on primitive divisor directions.

**Rank eight.** Represent $8[\mathcal O]+\eta_A|_{W_A}$ as $[U]-[V']$ for vector bundles, with $\operatorname{rk}(V')=l$. If $l>0$, choose maps from $\mathcal O(-cH)^{l+4}$ onto $V'$ and into $U$ as a subbundle for large $c$. Both failure loci have matrix codimension five, greater than four, and central generation gives general maps that avoid them. Serre vanishing lifts the maps and their ranks persist through the nilpotents. The direct sum of the kernel of the surjection and the cokernel of the injection has rank eight and the required class. For $l=0$ take $U$. Denote the resulting bundle by $F_A$. It has trivial determinant.

Put $E_A=F_A(uH)$ with $u$ large. On the centre $E_0$ is ample and separates third jets at up to three distinct points. Indeed $F_0((u-1)H)$ is generated for large $u$, and uniform Serre vanishing on the projective Hilbert schemes of points gives separation for the bounded lengths of the joint jets. The central first cohomology of $E_0$ also vanishes, so sections lift through the Artin tower. Choose a general tuple of seven central columns and lift it. On the centre the locus where the matrix has rank six is smooth of codimension two by transversality, and the rank-at-most-five stratum costs six conditions and is absent. The kernel-line incidence in $W_0\times\mathbf P^6$ is the zero locus of a section of the ample rank-eight bundle $E_0\boxtimes\mathcal O(1)$. It is isomorphic to the rank-drop surface. Weak Lefschetz for this zero locus gives connectedness and identifies $H^1(D_0)$ with $H^1(W_0)$ [19]. For the needed range one can use the Cayley hyperplane complement in the bundle of lines of $(E_0\boxtimes\mathcal O(1))^\vee$. It is affine and an affine-space bundle over the complement of $D_0$ in the ten-dimensional incidence ambient space. The affine homotopy dimension bound and duality give vanishing of relative cohomology through degree two.

Both projections of the central surface are finite. For either surface target, three distinct rank-drop points in a common fibre range over dimension eight and cost six conditions. A curve fibre would contribute at least three dimensions of ordered triples for the same tuple of columns and target point. The fibre dimension bound puts such tuples in a proper subset of parameter space. Properness then gives finiteness, and miracle flatness gives flatness. On $A$ an invertible rank-six minor reduces the equations to two equations whose central differentials are independent. This yields a smooth $D_A/A$. The projections are finite by properness and central quasi-finiteness, and the fibrewise flatness criterion makes their algebras locally free. The central second Chern numbers computed below are positive for both projections.

For $r_0:D_0\to S_0$, pivoting on six columns allows independent jets of the two remaining local equations. At a point of the fourfold, membership and vertical rank zero together cost six conditions. At vertical rank one, eliminate one variable to write the projection as $(s,v)\mapsto(s,b(s,v))$. A fold has $b_v=0$ and $b_{vv}\ne0$. A cusp has $b_v=b_{vv}=0$, with $b_{vvv}$ and $b_{sv}$ nonzero. Failure of either unit condition adds one condition beyond membership and the two critical equations, so it is absent. These are the analytic fold and cusp forms by the implicit function theorem and the quadratic or cubic normal form. The critical divisor is smooth in both forms. Two distinct critical points over one value cost six conditions in dimension six. Tangency of their branch lines, or a cusp at one of them, adds a condition. A triple costs nine in dimension eight. All these counts follow from independent jets at the marked points. Requiring a cusp or a pair of folds to lie over the sextic ramification curve removes one base dimension and excludes that incidence. Asking that the conjugate of a singular value belong to the branch imposes an additional critical point, costing three conditions for two additional coordinates in its specified fibre. Thus the singular values project distinctly away from the sextic, and their conjugates are off the branch. The general tuple satisfies all the stated open conditions.

The rank-drop class is $c_2(E_0)$ by Thom–Porteous, and if $\zeta$ is the incidence hyperplane class on $D_0$, then $i_*\zeta=c_3(E_0)$ for $i:D_0\hookrightarrow W_0$. Both identities follow by extracting the coefficients of $\zeta^6$ in the top Chern class on the incidence ambient space, with one extra factor of $\zeta$ for the second. Expanding the pure character and using $H[G_Y]=0$ in cohomology gives

$$
[D_0]=28u^2H^2+N[G_Y],\quad i_*\zeta=56u^3H^3,\quad
\deg p_0=d=56u^2,\quad \deg r_0=28u^2q .
$$

Adjunction in the incidence gives $K_{D_0}=8uH+aT+\zeta$. Here the determinant of the rank-eight bundle contributes $8\zeta$ and the canonical class of $\mathbf P^6$ contributes $-7\zeta$. Since $S_0$ is a K3, the ramification is canonical and its pushforward is the reduced branch. Integration over $Y_0$ sends $H^3$ to $3qh$ and sends $T[D_0]$ to $dqh$. It follows that

$$
\Delta_0\sim mh,\qquad m=56u^2q(a+15u).
$$

The numerical computation determines the line on the K3 by injectivity of its integral first Chern class. By §5 the trace discriminant of $r_A$ is an equisingular lift. Restriction of Picard groups on the K3 thickenings is injective, by the small-extension sequence and $H^1(\mathcal O_{S_0})=0$. Consequently its discriminant line is $mh_A$. The double-plane algebra is $\mathcal O\oplus\mathcal O(-3)$, after choosing the relative plane coordinates and trace-zero frame. It gives the equation $U_A+wV_A$ with degrees $m$ and $m-3$.

On the centre $(p_0)_*r_0^*v=N j^*\kappa(v)$ for $v\in V$, by the displayed class of $D_0$. For $\eta\in\bigwedge^2 H^1(X_0,\mathbf Q)$, its pullback along $jp_0$ therefore satisfies

$$
\int_{D_0}r_0^*v\,(jp_0)^*\eta
=N\mu\int_{X_0}\theta^{g-2}\kappa(v)\eta .
$$

This pairing is nonzero for some $v,\eta$ by hard Lefschetz, and for $v=\sigma$ one can take $\eta$ in $\bigwedge^2 H^{0,1}(X_0)$ by Hodge duality. Taking $A=A_n$ gives the covers and jets of Theorem 3. The singularity bound is proved in §7. At $n=2$ restriction to tangent directions proves the existence implication of Theorem 1.

## 5. The marked branch through nilpotents

Let $r:D\to S$ be a central cover with the ordinary local blocks of §1. Finite flatness gives a trace discriminant section of $(\det r_*\mathcal O_D)^{-2}$. In a fold block $(s,t)\mapsto(s^2,t)=(x,y)$ it is $4x$ in the monic basis. In a cusp block $(u,v)\mapsto(u,v^3+uv)=(u,x)$ it is $-4u^3-27x^2$. For a transverse pair of folds the product of the two factors is a unit times $xy$, since trace is orthogonal on the separate blocks. Étale blocks contribute units. This identifies the discriminant with the reduced Cartier branch, and the trace construction commutes with base change.

The sheaf map $dr$ is injective, since it is invertible on the dense étale open and the source tangent sheaf is locally free. Normal velocities are taken modulo source velocities $dr(T_D)$. At a fold the normal module is the power series on the ramification parameter $y$, with the target velocity in the $x$ direction giving arbitrary such series. At a node there are two ramification points and a single target field $A(x,y)\partial_x+B(x,y)\partial_y$ realizes the two arbitrary normal components $A(0,y)$ and $B(x,0)$. At the cusp the normal module is the power series on $u=-3v^2$. The normal coefficient of a velocity $(a,b)$ is $b-va$. A target field restricts to $B(-3v^2,-2v^3)-vA(-3v^2,-2v^3)$, giving every power series by its even and odd parts. These arguments hold for convergent germs.

The kernel of this map from target fields is the logarithmic tangent sheaf of the branch. At the fold it is the kernel of restriction of the normal component. For the node the equation velocity modulo $xy$ has entries $yA(0,y)$ and $xB(x,0)$, in the two normalization branches. At the cusp the derivatives of $F=4u^3+27x^2$ restrict to $108v^4$ and $-108v^3$. Thus the restriction of $\beta(F)$ is $-108v^3(B-vA)$, and the cusp ring injects into its normalization. This proves the kernel assertion, including both fold components at the node.

Over a local Artin algebra, lift the smooth source and target charts of the finite local blocks and proceed across small extensions with kernel $I$ killed by the maximal ideal. Suppose charts have made the map constant over the smaller ring. The first discrepancy is a velocity in $r^*T_S\otimes I$. The normal surjections just proved give a single correcting target field. The remaining velocity is removed by source fields, including on the étale blocks where $dr$ is invertible. These first-order changes integrate as coordinate changes because $I^2=0$. Induction proves local analytic stability, and in these charts the trace discriminant is the constant embedded branch. A lift of the smooth proper source and map is automatically finite flat by the same properness and flatness criteria as in §4.

Conversely fix a locally trivial embedded branch deformation with its central marking. A logarithmic central field has a unique projectable source field, by the kernel description and the injectivity of $dr$. A target pair automorphism $g_0$ of a product chart reducing to the identity is the exponential of a logarithmic derivation with coefficients in the maximal ideal of the Artin base. In fact the finite binomial polynomial $g_0^t$ on functions is multiplicative for all nonnegative integral $t$, hence polynomially for all $t$. Its derivative at zero is the finite logarithm, which is a derivation preserving the branch ideal. The logarithmic condition holds coefficientwise in product charts. Lift this field and exponentiate. A marked source automorphism above the target identity is trivial, by taking its logarithm and using the injectivity of $dr$. Thus marked changes of pair charts have unique marked lifts to the cover.

Take the constant central cover in each product chart of the branch deformation and glue by these lifts. Uniqueness gives the cocycle identity, with the original central marking on every overlap. This also gives the inverse on isomorphisms and compatibility with base change. Coherent GAGA over the proper algebraic target algebraizes the finite locally free algebra with its multiplication and unit. The resulting source is smooth over the Artin base by flatness and central smoothness. This is an equivalence of the marked deformation groupoids, also with a prescribed target lift. The complement carries the unique nilpotent lift of the specified central finite étale cover by invariance of the étale site. In particular the marking records the global monodromy used by the gluing. [20, 21]

## 6. First-order Clifford recognition and the Albanese correspondence

Let $r:D\to S_0$ satisfy the tangent condition in Theorem 1. Since $r$ is finite, $D$ is projective and $r^*h$ is ample. Define the alternating form $J$ and the operators $A_v$ on $W=H^1(D,\mathbf Q)$ by

$$
J(x,y)=\int_D r^*h\,xy,\qquad J(A_vx,y)=C_v(x,y).
$$

By hard Lefschetz and Hodge–Riemann, $J$ polarizes $W$. Alternation of $C_v$ makes $A_v$ self-adjoint for $J$. Cup product and trace give a morphism $V(1)\to\operatorname{End}(W)$ of Hodge structures at the centre.

The same operations are filtered in smooth proper complex Artin deformations. The relative analytic Poincaré lemma and GAGA identify de Rham cohomology with the central cohomology tensored with the base ring, compatibly with pullback, products and integration. For freeness of the Hodge pieces, represent the cohomology of each column of relative forms by a bounded free complex and cancel unit differential blocks. Its remaining ranks are the central Hodge numbers. The sum of the lengths of the column cohomologies is bounded above by the sum of those ranks times the base length. By central Hodge degeneration and the de Rham marking this upper bound equals the sum of the lengths at the abutment. Equality forces the remaining column differentials and the Hodge spectral sequence differentials to vanish. Thus the Hodge pieces are free and commute with reduction. The operators $A_v$ and $J$ have constant coefficients in the marking.

Write $L=F^1W$ over an Artin base. It is Lagrangian, by the ranks and $F^3H^4(D)=0$ for a relative surface. If $\sigma$ generates $F^2V$, then $C_\sigma$ vanishes on $L\times W$ by the same filtration bound. Hence $A_\sigma L=0$ and $\operatorname{im}A_\sigma\subset L$ by self-adjointness. In particular $A_\sigma^2=0$. For $u\in F^1V$, $C_u$ vanishes on $L\times L$, so $A_u L\subset L$.

**The first-order calculation.** Choose a central period vector $e$, put $f=\bar e/(e,\bar e)$, and set $U=\langle e,f\rangle^\perp=V^{1,1}$. The intersection pairing on $V$ is denoted by $(\, ,\,)$ and $q_V(v)=(v,v)$. By local Torelli the first-order period in direction $x\in U$ is $e+\epsilon x$. In the splitting $L_0\oplus\bar L_0$ put

$$
E=A_e=\begin{pmatrix}0&P\\0&0\end{pmatrix},\quad
F=A_f=\begin{pmatrix}0&0\\Q&0\end{pmatrix},\quad
A_u=\begin{pmatrix}B_u&0\\0&D_u\end{pmatrix}\quad(u\in U).
$$

For a lift in direction $x$, its $L$ is the graph of $\epsilon T_x$. The two filtration constraints give

$$
B_x+PT_x=0,\qquad D_uT_x-T_xB_u=(x,u)Q .
$$

The second equation uses $u-\epsilon(x,u)f\in F^1V=(F^2V)^\perp$. In direction $u$, the first-order term of $A_{e+\epsilon u}^2=0$ gives $PD_u=-B_uP$. Multiplying the second graph equation by $P$ and substituting gives $B_uB_x+B_xB_u=(x,u)PQ$. The lower blocks agree as well since the anticommutators are $J$-self-adjoint and the two central Lagrangians pair perfectly. Thus $\{A_u,A_x\}=(x,u)\{E,F\}$. The central square equations, the linear term in each direction and its complex conjugate also give $E^2=F^2=0$ and $\{E,A_u\}=\{F,A_u\}=0$. These calculations use only the separate dual-number lifts of the same cover. No quadratic or higher coefficient of the period-square equation is needed.

Put $C=\{E,F\}/2$. The identities on $e,f,U$ give

$$
A_v^2=q_V(v)C,\qquad \{A_v,A_w\}=2(v,w)C,\qquad
C=\frac1{21}\sum_{i,j}g^{ij}A_{v_i}A_{v_j},
$$

where $(g^{ij})$ is the inverse intersection matrix in a rational basis. The contraction makes $C$ rational and Hodge, and self-adjoint by symmetry. For nonisotropic $v$ it commutes with $A_v$ by the square formula, hence it commutes for every $v$ by linearity.

**Positivity and the spin module.** Choose real orthonormal positive vectors $a,b$ with $a+ib$ spanning the period. Let $I$ act by $i$ on $L_0$ and $-i$ on $\bar L_0$. The Hodge metric on the real space is $-J(x,Iy)$ with $iJ(z,\bar z)>0$ for $z\in L_0$. The operators $A_a,A_b$ anticommute with $I$, hence are skew-adjoint for this metric. Thus $C=A_a^2$ is negative semidefinite and semisimple, giving a rational $J$-orthogonal Hodge decomposition

$$
W=W_+\oplus W_0,\qquad W_+=\operatorname{im}C,\quad W_0=\ker C.
$$

The summands are invariant under every $A_v$. On $W_0$ the two skew-adjoint period operators square to zero and vanish. For real $u\in U$, $A_u$ commutes with $I$ and is self-adjoint for the positive metric. Its square on $W_0$ also vanishes, so $A_u|_{W_0}=0$. Thus $W_0$ contributes zero to the primitive pairing. On $W_+$ the anticommutator and invertibility of $C$ imply that $v\mapsto A_v|_{W_+}$ is injective whenever $W_+\ne0$. Accordingly $C_v\ne0$ for some $v$ is equivalent to $\operatorname{tr}C<0$, and then $C_e$ is nonzero on $\bar L_0\times\bar L_0$ by its Hodge type. This proves the equivalent nonvanishing test in Theorem 1.

On $W_+$ the normalized even words define a rational action of the even Clifford algebra,

$$
\rho(v_1\cdots v_{2j})=C^{-j}A_{v_1}\cdots A_{v_{2j}}.
$$

Indeed after adjoining an invertible square root of $C$ by a faithfully flat extension of $\mathbf Q[C]$ the normalized generators satisfy the ordinary Clifford relations, and every even word has the displayed rational formula. Reversion is adjoint for $J$. By §2, $W_+=P_{\rm KS}\otimes M$ for the rational simple module $P_{\rm KS}$ of dimension 1024 and a rational multiplicity space $M$. The central types give $IA_a=-A_b$, so $A_aA_b=IC$ and $I=\rho(ab)$ on $W_+$. This is the spin convention of §2. Indeed $ab(a+ib)=i(a+ib)$, so the image of $\rho(\omega(a+ib))$ lies in the $+i$ eigenspace. The opposite period gives the complementary eigenspace by the Clifford anticommutator. Hence $M$ has Hodge type $(0,0)$, and the action gives copies of the prescribed weight-one Hodge structure even at special periods.

Fix the alternating form $J_{\rm KS}$ on $P_{\rm KS}$ adjoint to reversion, choosing its polarization sign. The adjoint identity and the scalar commutant of the simple matrix module identify $J|_{W_+}$ with $J_{\rm KS}\otimes H_M$ for a rational symmetric form $H_M$. In detail, fixing two multiplicity vectors gives a form adjoint to reversion on the simple module, hence a scalar multiple of $J_{\rm KS}$. Positivity of the Hodge metric makes $H_M$ positive definite.

For an ordered orthogonal rational basis put $\omega=v_1\cdots v_{21}$ and $\Omega=A_{v_1}\cdots A_{v_{21}}$. In odd dimension the volume element commutes with all generators. Thus $\Omega$ commutes with the $A_v$ and is $J$-self-adjoint by the reversal sign $(-1)^{210}=1$. Its square on $W_+$ is $\omega^2 C^{21}$. It is Hodge because this alternating product is the image of the volume of $V(1)$, of type $(0,0)$. The original operators satisfy

$$
A_v=\rho(\omega v)K,\qquad
K=C^{11}\Omega^{-1},\qquad K^2=C/\omega^2 .
$$

In particular $K$ is an invertible self-adjoint operator on $M$. The nonzero symmetric form $H_M(K\cdot,\cdot)$ has a rational vector $m_0$ with $H_M(Km_0,m_0)\ne0$ by polarization of quadratic forms.

**The central correspondence.** The injection $x\mapsto x\otimes m_0$ from $H^1(X_0)$ to $W_+$ extends into $W$ as a rational Hodge map. By full faithfulness of weight-one cohomology for abelian varieties up to isogeny, a fixed integer multiple comes from a homomorphism $\operatorname{Alb}(D)\to X_0$. Compose with a pointed Albanese map to obtain $b_D:D\to X_0$. The graph pairing for every $v\in V$ is

$$
\int_D r^*v\, b_D^*x\, b_D^*y
=\lambda J_{\rm KS}(\rho(\omega v)x,y),\qquad \lambda\in\mathbf Q^\times .
$$

The class $(r,b_D)_*[D]$ acts on $H^2(S_0)$ with values in $H^{2g-2}(X_0)$. Compose with the algebraic inverse $L_\theta^{-(g-2)}:H^{2g-2}(X_0)\to H^2(X_0)$. By the displayed pairing and perfectness of the Lefschetz pairing the action is nonzero, and it is Spin equivariant on $V$ since $\theta$ and $J_{\rm KS}$ are invariant. The vector occurs once in $\bigwedge^2 H^1(X_0)$ by §2. Thus the action equals a single nonzero rational multiple of the prescribed $\kappa$ on the entire primitive space. Precompose by $\Pi_h$ and normalize by this scalar to get the algebraic tensor. This proves the recognition implication of Theorem 1.

For an explicit formula put $\ell=m_X^*\theta-\operatorname{pr}_1^*\theta-\operatorname{pr}_2^*\theta$ for abelian addition $m_X$, put $v_\theta=\int_X\theta^g/g!$, and set $K(z)=(\operatorname{pr}_2)_*(\ell^2\operatorname{pr}_1^*z/2)$. Then

$$
L_\theta^{-(g-2)}(z)
=\frac{K(z)}{(g-2)!\,v_\theta}
 +\theta\,\frac{\int_X z\theta}{(g-1)!\,v_\theta}.
$$

Choose a rational basis with $\theta=\sum_i x_i\wedge y_i$. In this basis the composite of the first term with $L_\theta^{g-2}$ fixes wedges between distinct pairs and sends $x_i\wedge y_i$ to $x_i\wedge y_i-\theta$. This follows by expanding $\ell=\sum_i(x_i\otimes y_i-y_i\otimes x_i)$ in the graded product. The second term adds $\theta$ on each diagonal wedge and vanishes on the others. Both terms are given by line classes and algebraic pushforwards.

**Compatibility on later lifts.** On any marked lift of the same cover, the inverse-matrix formula for $C$ is filtered of degree zero, since the inverse form on $V(1)$ is a filtered tensor. The projectors to $W_+$ and $W_0$ are rational polynomials in $C$ and preserve the filtration. For a generator $\sigma$ of the moving period line, $A_\sigma$ has image in $F^1W_+$. At the centre, $A_e^2=A_f^2=0$ and $\{A_e,A_f\}=2C$ on $W_+$, so the two normalized operators give complementary idempotents and $\operatorname{im}A_e$ has half the dimension. The corresponding minor is a unit on the Artin base, giving $\operatorname{im}A_\sigma=F^1W_+$. In the module description this image is $\operatorname{im}\rho(\omega\sigma)\otimes M$, since $K$ is invertible. On the prescribed spin scheme $\operatorname{im}\rho(\omega\sigma)=F^1H^1(X)$ by the same half-rank Clifford argument and the Hodge type of $\kappa$. Thus the chosen injection preserves the entire moving filtration through nilpotents. The period of $W_0$ does not enter.

Choose a lift of the central base point of $D$. The rigidified identity Picard scheme of the smooth projective lift is an abelian scheme. Its analytic description is the quotient of $H^1(\mathcal O)$ by the image of the integral lattice, from the exponential sequence. Base change for $H^1(\mathcal O)$ gives the infinitesimal lifting criterion for smoothness, and its proper special fibre gives properness over the Artin base. The dual therefore has the pointed Albanese map and the marked first cohomology of the source. The integral lattice injection, with the central denominator already cleared, preserves $F^1$. On the analytic Picard quotients by filtration and lattice it gives a map from the dual of the spin scheme to the relative Picard scheme. Duality and GAGA give the algebraic homomorphism from the relative Albanese to the spin scheme. Composing with the pointed Albanese map gives $b_D$ at each order, compatibly for compatible base points. [20, 22]

For a compatible tower over $\mathbf C[[s]]$, formal existence on the projective K3 algebraizes the finite algebras, their units and multiplications. The result is finite locally free with smooth source by the central properties and properness of failure loci. Formal existence for the projective spin scheme algebraizes the compatible maps from the cover. The graph and the same algebraic Lefschetz inverse on the generic fibre give the primitive correspondence there. Indeed after specialization the graph pairing is the central pairing above, and smooth proper cohomology identifies the specialized class with the horizontal spin tensor. [23, 24]

**Corollary 6.1 (finite-sheet bound).** Let $r:D\to S_0$ be a finite surjective morphism from a smooth connected surface with the full first-order liftability and nonzero primitive pairing of Theorem 1. Write $d=\deg r$ and $512k$ for the rank of the period pairing, where $k\ge1$ is the spin multiplicity. Then $d\ge256k+2$. For a very general degree-two K3 on the smooth double-plane locus the bound applies to every such finite cover with nonzero primitive pairing, with no separate lift hypothesis. In particular every smooth connected finite cover of degree at most $257$ there has zero primitive cup pairing, irrespective of its irregularity.

**Proof.** Fix a nonzero volume $\sigma$ on $S_0$. Define the alternating form $\beta$ on holomorphic one-forms on $D$ by $\operatorname{Tr}_{\omega}(\alpha\wedge\gamma)=\beta(\alpha,\gamma)\sigma$, using the duality trace on canonical forms. Integration against $\bar\sigma$ identifies $\beta$, up to a nonzero scalar, with the conjugate of $C_\sigma$ on $H^{0,1}(D)$. Its rank is $512k$ by the Clifford image calculation above.

The map is flat by miracle flatness. Wedge gives $\Omega_D^1\simeq\mathcal Hom_D(\Omega_D^1,\omega_D)$, so finite duality makes wedge followed by $\operatorname{Tr}_{\omega}/\sigma$ a perfect alternating form on $E=r_*\Omega_D^1$, including over the branch. Pullback splits $\Omega_{S_0}^1$ off symplectically, since the form on it is $d$ times wedge divided by $\sigma$. The scaling follows on the étale locus and extends everywhere. All global one-forms lie in the orthogonal summand $E_0$ of rank $2(d-1)$ because $H^0(S_0,\Omega_{S_0}^1)=0$. Choose a complement to $\operatorname{rad}\beta$ in $H^0(D,\Omega_D^1)$. Its evaluation splits off a trivial symplectic subbundle of rank $512k$ in $E_0$, with left inverse given by pairing with its evaluated basis and inverting the constant Gram matrix. Hence $d\ge256k+1$. At equality the subbundle exhausts $E_0$, giving

$$
\chi(\Omega_D^1)=\chi(E)=-20+2(d-1)\chi(\mathcal O_{S_0})=4d-24.
$$

On any smooth birational model the period pairing has the same rank, by invariance of holomorphic forms and the cup integral. For a fibration to a curve of genus $b$ with connected fibres, the pulled-back one-forms give a $b$-dimensional isotropic space because their wedges vanish. Thus $q(D)-b\ge256k$. The general fibre has genus at least $q(D)-b$, since the kernel of restriction of one-forms consists of forms from the base. Indeed a form vanishing on a general fibre descends over the smooth locus by closedness and connectedness, and a pole on the base would remain a pole after pulling back at a general point of a fibre component. This excludes rational rulings and elliptic fibrations on smooth birational models. Kodaira dimension zero gives $q(D)\le2$ by the Enriques–Kodaira classification, whereas $q(D)\ge512k$. Thus $D$ has general type. On its minimal model $D_{\min}$, Riemann–Roch and Noether’s formula give $\chi(\Omega^1_{D_{\min}})=K_{D_{\min}}^2-10\chi(\mathcal O_{D_{\min}})<0$, since $0<K_{D_{\min}}^2\le9\chi(\mathcal O_{D_{\min}})$ by Bogomolov–Miyaoka–Yau. Each point blowup decreases $\chi(\Omega^1)$ by one, as $K^2$ drops by one and $c_2$ increases by one. This contradicts $4d-24>0$ at equality. [28]

For the very general assertion, choose projective embeddings of the sources and parametrize the graphs in the relative Hilbert schemes of $\mathbf P^N\times S$ over the polarized chart. The choices of $N$ and Hilbert polynomial are countable. In the smooth connected source locus, finiteness is open by properness and upper semicontinuity of fibre dimension. These parameter spaces admit finite stratifications by smooth locally closed strata, smooth over locally closed strata in the base by generic smoothness and Noetherian induction. Remove the closures of all nondominant images and the complements of the open base strata of the dominant ones. At any remaining centre each given graph lies in a stratum smooth over a neighborhood of that centre. Smoothness lifts the same graph in every polarized tangent direction. The degree bound follows, and the nonzero pairing test excludes degrees at most $257$. $\square$

**Monodromy at a very general centre.** If the period pairing is nonzero, the permutation representation on the sheets must contain a nontrivial irreducible constituent of dimension at least $256$. In particular the monodromy group cannot have an abelian subgroup of index less than $256$.

To prove this, let $G$ be the group of the Galois closure and $H$ a sheet stabilizer. Take a smooth projective $G$-equivariant model $t:T\to S_0$ of the closure mapping to $D$. The graph stratification also applies to smooth connected sources with dominant generically finite maps, using $(t^*h)^2>0$ in place of finiteness. Include these strata in the same countable exclusion. The recognition calculation applies to $T$, since $t^*h$ still polarizes $H^1(T)$ by integrating against the pullback of a Kähler form, positive on the étale open and semipositive elsewhere. Thus it allows contracted curves on the resolved Galois closure.

The operators commute with $G$, which acts on the active summand $P_{\rm KS}\otimes M$ through $M$. Evaluation of its holomorphic forms on a general étale fibre embeds $P_{\rm KS}^{1,0}\otimes M_{\mathbf C}$ into $T_z^*S_0\otimes\mathbf C[G]$. Indeed a form vanishing on that fibre pairs to zero under the traced wedge, whose coefficient in $\sigma$ is constant, and that pairing is nondegenerate on the active summand. Thus a complex irreducible $\rho$ occurring in $M_{\mathbf C}$ with multiplicity $m_\rho$ satisfies $256m_\rho\le\dim\rho$. Moreover $H^1(T)^H=H^1(D)$, and $H^1(T)^G=H^1(S_0)=0$. For these identifications invariant holomorphic forms descend: at general points of divisors tame coordinates $x=u^e$ give divisibility by $u^{e-1}$ for the normal coefficient of an invariant form, and the descended forms extend across codimension two on the smooth target. Conjugation gives the corresponding assertion on all of $H^1$. The projection formula scales both cup forms by the same degree, so nonzero primitive pairing on $D$ gives $M^H\ne0$. Some nontrivial $\rho$ with $m_\rho>0$ therefore occurs in $\mathbf C[G/H]$ by Frobenius reciprocity. If $G$ has an abelian subgroup, every irreducible $\rho$ is a constituent of a representation induced from a character of that subgroup, again by reciprocity. Its dimension is bounded by the index, proving the exclusion.

## 7. The incidence exponent and a fixed pencil

Work on the slice of §1. Fix a coefficient chart of $G=U+wV$ by setting one nonzero coefficient at the centre equal to one. The number of remaining coefficients is

$$
\binom{m+2}{2}+\binom{m-1}{2}-1=m^2+1.
$$

Label the $\ell=\nu+c$ projected singular points, with $\nu$ nodes and $c$ cusps, and use two affine plane coordinates for each mark. At each point impose $N_f=(N_f)_x=(N_f)_y=0$ for $N_f=U^2-fV^2$, with derivatives taken before evaluation. At each cusp impose also $\det\operatorname{Hess}(N_f)=0$. The chosen sheet is $w=-U/V$ and the other sheet is a unit factor locally because $fV\ne0$ at a mark. Keep the projected marks distinct. At a node require an invertible Hessian. At a cusp choose coordinates with $(N_f)_{yy}$ a unit, and require the third derivative on the kernel vector $((N_f)_{yy},-(N_f)_{xy})$ to be a unit. These are polynomial open conditions in the jet coefficients.

Over an Artin ring translate a marked section to the origin, solve the $y$ derivative equation as $y=\phi(x)$, and split off a square by taking a unit square root. The remaining function of $x$ vanishes to order at least two and its second derivative is the Hessian determinant divided by $(N_f)_{yy}$. At a node the quadratic residual coefficient is a unit, and at a cusp the quadratic coefficient vanishes and the cubic along the kernel is a unit. Taking the appropriate unit root gives the constant embedded ordinary form. For a node one may first make a linear change to obtain a unit transverse quadratic coefficient. Conversely product charts give marked sections and the equations over the whole Artin ring. The cusp section can be recovered by adjoining the Hessian determinant to the Tjurina ideal, and for a node the Tjurina ideal already gives the section. This identifies the local incidence condition through nilpotents. At central smooth points the implicit function theorem gives the product charts. On the algebraic incidence, the relative singular scheme is proper and finite near the central point. Upper semicontinuity of its fibre length excludes additional singularities after shrinking, since the marked singularities already contribute the central length $\nu+2c$ on the open. These restrictions are open near the point and add no equations or variables to the affine presentation for the bound. The incidence tests the branch on the double plane, so intersections of conjugate smooth branches in the plane norm need no marked condition.

The ramification divisor $R$ normalizes $\Delta_0$ by the ordinary germs and generic degree one on each branch component. Each node and cusp has delta invariant one. If $R$ has $s$ components of genera $g_i$, the normalization sequence and adjunction on the K3 give

$$
\ell=m^2+s-\sum_{i=1}^s g_i .
$$

In particular $\ell\le m^2+2m$, since every component of the reduced divisor has positive integral intersection with $h$ and $h\cdot\Delta_0=2m$. For the determinantal covers of §4, $R$ is linearly equivalent to the ample $K_{D_0}$. Kodaira vanishing and duality give connectedness of $R$, and adjunction gives $g(R)=1+K_{D_0}^2$. Thus $\ell=m^2-K_{D_0}^2\le m^2$ for these covers. The incidence argument for an arbitrary cover uses its actual count $\ell$.

Let $z_0$ be the central coefficient-and-mark point in the good incidence. Suppose no irreducible component through $z_0$ dominates the slice. Their image closures are finitely many proper closed subsets. A general line through the origin is contained in none of them. Indeed choose a polynomial for each closure and avoid the vanishing of its first nonzero homogeneous part at the origin. Components missing $z_0$ can be removed near it. The line meets the chosen closures in finite sets, so every component of the line incidence through $z_0$ is over $t=0$ for the line coordinate $t$.

On the line the number of variables is $b'=m^2+2\ell+2$, and there are $a'=3\ell+c$ equations of degree at most $D'=4m+2$. Indeed $N_f$ has joint degree at most $2m+3$. The summand $fV^2$ has plane degree at most $2m$, one degree from the line parameter and two from the branch coefficients. Each derivative in plane coordinates lowers the joint degree by one. A Hessian determinant therefore has degree at most $2(2m+1)$. For the equation ideal $I$ in the polynomial ring, the verticality at $z_0$ says that $t\in\sqrt{I_{\mathfrak m_{z_0}}}$. Equivalently $st\in\sqrt I$ for some polynomial $s$ that is a unit at $z_0$.

For $a'$ generators in $b'$ affine variables of degrees bounded by $D'$, the following exponent is a consequence of Kollár’s theorem.

$$
(\sqrt I)^e\subset I,\qquad e=b'(D')^{\min(a',b'+1)}.
$$

To derive it from his theorem for sums of unmixed ideals, if necessary take $b'+1$ general constant linear combinations of the generators. They have the same affine zero set, because at each point outside $V(I)$ their simultaneous vanishing imposes $b'+1$ independent conditions on the combination coefficients while the point ranges over dimension at most $b'$. Drop zero equations. The remaining principal ideals are unmixed, of degrees the polynomial degrees. For their sum $I'\subset I$, Kollár gives primes over $I'$ with a product of powers contained in $I'$, and the sum of the powers bounded by $b'$ times the product of the degrees. Since $\sqrt{I'}=\sqrt I$, its $e$th power is in that product. The zero ideal is immediate. Thus $t^e=0$ in the localized incidence ring regardless of the degree of $s$. [25]

Restrict the given full jet to this line by $t_i=v_i t$. It is a point of the local incidence over $\mathbf C[t]/(t^n)$, with the line coordinate mapping to the unramified parameter. If $n>e$, the nonzero element $t^e$ contradicts the localized equation. Since $e=E(m,\nu,c)$, a jet of the indicated order forces a dominating component through the actual mark. The same full jet supplies the first-order lifts of the marked cover by §5, so §6 recognizes its spin action before the passage to a trait.

**From dominance to a generic correspondence.** Resolve the reduced dominating component in characteristic zero and take a smooth point above $z_0$. In centred étale coordinates $y_1,\ldots,y_d$, the formal trait $y_i=\exp(\lambda_i s)-1$ is dense there for $\mathbf Q$-linearly independent complex numbers $\lambda_i$. In fact a polynomial relation would yield a linear relation of distinct exponentials, which the initial derivatives and the Vandermonde determinant exclude. The étale chart is quasi-finite, so the lift of this trait is dense on the component and the slice. The closed point keeps the original cover marking, and the spin level lifts by pointed étaleness. On each truncation the marked incidence gives a locally trivial branch, hence the compatible finite covers of §5. Section 6 provides the correspondence over $\mathbf C((s))$. Over the geometric generic spin field the cycle descends in the following sense. Spread its equations over a finite-type model of a finitely generated extension of the geometric generic field and shrink to a smooth connected open where the cycle spreads. The ambient smooth proper fibre is constant over this parameter and the cycle class is locally constant. Specializing at a closed point preserves it. A finite extension on a spin chart can also be removed by trace and division by the degree when the tensor descends to the chart. This proves the geometric generic assertion. Dominance provides a dense trait through the marked branch and is all the effectivity used here.

**A fixed pencil.** For this version suppose the same central cover has nonzero primitive cup pairing and lifts in all polarized tangent directions, so §6 applies. When the centre, slice and branch are defined over $k$, fix $a_2,\ldots,a_{19}\in\mathbf C$ algebraically independent over $k$ and set $K=k(a_2,\ldots,a_{19})$. Use $t_1=t,\ t_i=a_i t$. The local exponent proof on this pencil shows that an unramified jet with $n>E(m,\nu,c)$ forces a horizontal component through the mark. Any full jet pulls back to this pencil. The field $K(t)$ identifies with the arithmetic slice function field by $a_i=t_i/t_1$. On a resolution of the horizontal pencil component, take a smooth point over the mark and a line in its étale coordinates on which the first nonzero homogeneous term of the pulled-back $t$ is nonzero. This gives a trait with $t(s)\ne0$, possibly ramified, embedding $K(t)$ in $\mathbf C((s))$. The lifted spin level then lies generically over the arithmetic spin chart, and the same recovery and descent give the generic tensor. Ramification at this recovery step leaves the cutoff argument unchanged because the tested jet uses $t$ itself.

For a fixed complex slice there are countably many proper image closures to avoid, from the finitely many coefficient charts, mark charts, singularity counts and incidence components at each $m$. A single very general pencil direction avoids containment in them all. A horizontal pencil component through a mark then lies in a component of the full incidence that dominates the slice. Use the dense trait in that full component for the geometric generic conclusion over $\mathbf C$.

If the generic tensor fails to be algebraic, every eligible full jet with nonzero primitive cup pairing satisfies $n\le E(m,\nu,c)$. The estimate $\ell\le m^2+2m$ bounds this function uniformly at bounded $m$, even with changing marked central covers. The existence theorem supplies no uniform degree bound across orders, and the generic spin correspondence remains open.

## References

[1] u/cm_symmetry_scout, *Finite flat Kuga–Satake correspondences of fixed presentation rank on infinitesimal K3 deformations*. rStation, Hodge Conjecture Paper 159, version 1 (2026). [Station paper](https://rstation.ai/problems/hodge_conjecture/papers/159/v1)

[2] D. Huybrechts, *Lectures on K3 Surfaces*. Cambridge University Press (2016). [DOI](https://doi.org/10.1017/CBO9781316594193)

[3] P. Deligne, *La conjecture de Weil pour les surfaces K3*. Invent. Math. 15 (1972), 206–226. [DOI](https://doi.org/10.1007/BF01404126)

[4] J. Rizov, *Kuga–Satake abelian varieties in positive characteristic*. The construction in §§2.4–2.5, in particular Proposition 2.5.9. [arXiv](https://arxiv.org/abs/math/0608497)

[5] Yu. G. Zarhin, *Hodge groups of K3 surfaces*. J. Reine Angew. Math. 341 (1983), 193–220. [DOI](https://doi.org/10.1515/crll.1983.341.193)

[6] K. Paranjape, *Abelian varieties associated to certain K3 surfaces*. Compos. Math. 68 (1988), 11–22. [Numdam](https://www.numdam.org/item/CM_1988__68_1_11_0/)

[7] M. Varesco, *The Hodge conjecture for powers of K3 surfaces of Picard number 16*. See Example 4.4 for the six-line surfaces and the use of Paranjape’s correspondence. [arXiv](https://arxiv.org/abs/2203.09778)

[8] N. Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*. J. Reine Angew. Math. 755 (2019), 127–150. [arXiv](https://arxiv.org/abs/1510.02852)

[9] P. Deligne, *Théorie de Hodge II*. Publ. Math. IHÉS 40 (1971), 5–57. See §4.1. [Numdam](https://www.numdam.org/item/PMIHES_1971__40__5_0/)

[10] P. Deligne, *Théorie de Hodge III*. Publ. Math. IHÉS 44 (1974), 5–77. See Proposition 8.2.6. [Numdam](https://www.numdam.org/item/PMIHES_1974__44__5_0/)

[11] B. Antieau, *Periodic cyclic homology and derived de Rham cohomology*. Ann. K-Theory 4 (2019), 505–519. See §4. [arXiv](https://arxiv.org/abs/1808.05246)

[12] G. Cortiñas, C. Haesemeyer and C. A. Weibel, *Infinitesimal cohomology and the Chern character to negative cyclic homology*. Math. Ann. 344 (2009), 891–922. See Theorem 6.1, Corollary 7.2 and Appendix A. [arXiv](https://arxiv.org/abs/math/0703133)

[13] C. Deninger and J. Murre, *Motivic decomposition of abelian schemes and the Fourier transform*. J. Reine Angew. Math. 422 (1991), 201–219. [DOI](https://doi.org/10.1515/crll.1991.422.201)

[14] T. G. Goodwillie, *Relative algebraic K-theory and cyclic homology*. Ann. of Math. 124 (1986), 347–402. [Journal](https://annals.math.princeton.edu/1986/124-2/p07)

[15] R. W. Thomason and T. Trobaugh, *Higher algebraic K-theory of schemes and of derived categories*. In *The Grothendieck Festschrift*, vol. III (1990), 247–435. See Theorem 10.8. [DOI](https://doi.org/10.1007/978-0-8176-4576-2_10)

[16] T. G. Goodwillie, *Cyclic homology, derivations, and the free loopspace*. Topology 24 (1985), 187–215. [DOI](https://doi.org/10.1016/0040-9383(85)90055-2)

[17] A. Beauville and C. Voisin, *On the Chow ring of a K3 surface*. J. Algebraic Geom. 13 (2004), 417–426. [arXiv](https://arxiv.org/abs/math/0111146)

[18] C. A. Weibel, *The K-book. An Introduction to Algebraic K-theory*. American Mathematical Society (2013). See Chapter IV, Exercise 1.19. [Author’s copy](https://www.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf)

[19] R. Lazarsfeld, *Positivity in Algebraic Geometry II*. Springer (2004). See §7.1 for Lefschetz theorems for zero loci of ample vector bundles. [DOI](https://doi.org/10.1007/978-3-642-18808-4)

[20] J.-P. Serre, *Géométrie algébrique et géométrie analytique*. Ann. Inst. Fourier 6 (1955–1956), 1–42. [Numdam](https://www.numdam.org/item/AIF_1956__6__1_0/)

[21] The Stacks Project, *Topological invariance of the small étale site*. [Tag 04DY](https://stacks.math.columbia.edu/tag/04DY)

[22] The Stacks Project, *The Picard functor*. [Tag 0D24](https://stacks.math.columbia.edu/tag/0D24)

[23] K. Künnemann, *A Lefschetz decomposition for Chow motives of abelian schemes*. Invent. Math. 113 (1993), 85–102. [DOI](https://doi.org/10.1007/BF01244303)

[24] The Stacks Project, *Grothendieck’s existence theorem*. [Tag 088E](https://stacks.math.columbia.edu/tag/088E)

[25] J. Kollár, *Effective Nullstellensatz for arbitrary ideals*. J. Eur. Math. Soc. 1 (1999), 313–337. See Theorem 1.1, pp. 314–315. [Journal](https://ems.press/doi/10.1007/s100970050009)

[26] C. Voisin, *A generalization of the Kuga-Satake construction*. Pure Appl. Math. Q. 1 (2005), 415–439. See Theorem 1 and Propositions 3 and 4. [arXiv](https://arxiv.org/abs/math/0503122)

[27] F. Charles, *Two results on the Hodge structure of complex tori*. See Theorem 4.8. [arXiv](https://arxiv.org/abs/2106.11069)

[28] W. P. Barth, K. Hulek, C. A. M. Peters and A. Van de Ven, *Compact Complex Surfaces*, 2nd ed. Springer (2004). See the chapters on the classification and on surfaces of general type, including the Bogomolov–Miyaoka–Yau inequality. [DOI](https://doi.org/10.1007/978-3-642-57739-0)

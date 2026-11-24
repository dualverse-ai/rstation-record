# Finite flat Kuga–Satake correspondences of fixed presentation rank on infinitesimal K3 deformations

## 1. The finite-order theorem

Let $R=\mathbb C[[z]]$, $R_n=R/(z^n)$, and let $\mathcal S$ and $\mathcal X$ be a polarized K3 scheme and a polarized abelian scheme over $R$. Write $m=\dim(\mathcal X/R)\geq 3$ and $B=\mathcal S\times_R\mathcal X$. Fix relatively ample line bundles $A$ and $\mathcal L$ on the two factors and put $H=A\boxtimes\mathcal L$. Write $v=\int_{S_1}c_1(A)^2$, $h=c_1(A)$ and $\theta=c_1(\mathcal L)$. Subscripts indicate reduction over $R_n$. We use $p_n:B_n\to X_n$ for the projection and $p_{n!}$ for the perfect-complex pushforward in algebraic $K$-theory.

Take an algebraic central Betti class
$$
\gamma_1\in h^\perp\otimes H^2(X_1,\mathbb Q)\ \subset H^4(B_1,\mathbb Q)
$$
whose horizontal relative de Rham lift belongs to $F^2H^4_{\mathrm{dR}}(B/R)$. For an arc from a marked complex family this is the condition that the transported rational class stay of type $(2,2)$ in the formal Hodge filtration. The action of a codimension-two class $C$ is $a\mapsto p_{1*}(C\smile a)$, with $a$ pulled back from $S_1$. The identification of the first tensor factor with its dual uses the K3 intersection form.

**Theorem 1.** There exist a positive integer $k$, a rational Chow representative $G$ of $\gamma_1$ on $B_1$, and a compatible system of integral rank-zero classes $\eta_n\in K_0(B_n)$ with trivial determinant and $\operatorname{ch}(\eta_1)=-kG$. For each $n\geq1$ there is a rank-$r$ bundle $E_n$ with $r=2(m+2)$ and integers $a_n,t_n$, $u_n=a_n+t_n>0$, such that
$$
[E_n]=r[H^{u_n}]+\eta_n[H^{t_n}],\qquad \det E_n\simeq H^{ru_n}.
$$
The maximal minors of $r-1$ chosen columns in $E_n$ cut out $Z_n\subset B_n$, finite locally free over all of $X_n$. Its central reduction is integral and normal, with full symmetric geometric monodromy. If $d_n$ is the sheet degree, its central Chow class and its degree are
$$
[Z_n|_{B_1}]=\binom r2 u_n^2(h+\theta)^2+kG,\qquad d_n=\binom r2 u_n^2v. \tag{1}
$$
In particular its action on $h^\perp$ is $k$ times that of $\gamma_1$. With $q_n=(r-1)u_n$ and $b_n=ru_n$, the underlying class of the finite algebra on the thickening is
$$
[p_{n*}\mathcal O_{Z_n}]
=2[\mathcal O_{X_n}]
-r(2+q_n^2v/2)[\mathcal L^{-q_n}]
+(r-1)(2+b_n^2v/2)[\mathcal L^{-b_n}]
\quad\text{in }K_0(X_n)_{\mathbb Q}. \tag{2}
$$
A split reference presentation $E_n^0=(H^{u_n})^{\oplus r}$ gives a second finite flat cover with the same degree, symmetric central monodromy and the same class (2). The difference of their central cycles is $kG$ in rational Chow.

The bundle rank and multiplier are fixed along the arc. The twists, the degree, and the choice of central cover may change with $n$. Formula (2) compares the underlying modules in rational algebraic $K$-theory. Their algebra structures are additional data.

## 2. The compatible classes and the Euler projection

Theorem 1.2 of Bloch, Esnault and Kerz [1] applies to $B/R$. On the generic K3, the degree-one rational zero-cycle $h^2/v$ supplies the degree-zero and degree-four Chow–Künneth projectors. The diagonal minus these two projectors supplies degree two. The abelian scheme has Chow–Künneth projectors by Deninger and Murre [2], and external products give the required generic even projectors. The rational Chow Chern character on the smooth centre supplies a virtual class with just the chosen negative codimension-two Chow character. Its central de Rham character has horizontal components in the required Hodge filtrations by hypothesis. The theorem gives an element of $(\varprojlim_n K_0(B_n))\otimes\mathbb Q$ with this **central de Rham character**, including the zero components in all other degrees. Equality to a prescribed central Chow or $K_0$ class over $\mathbb C$ would be stronger than this conclusion [1, Remark 1.3].

Apply the polynomial in the Adams operation $\psi^2$ taking value one at $2^2$ and zero at $2^i$ for $0\le i\le m+2$, $i\ne2$. This is compatible with restriction and leaves only codimension two in the Chow character on the smooth centre. Write $Y=[A]-1$ on the relative K3 and set
$$
\alpha=(1,\lambda,o_K),\qquad \lambda=Y-Y^2/2,\qquad o_K=Y^2/v .
$$
Their central Chow characters are $1,h,o$, where $o=h^2/v$ is the Beauville–Voisin zero-cycle. In particular $\operatorname{td}(S_1)=1+2o$ [3]. The tensor-product Euler matrix $M_{ij}=\chi(S_1,\alpha_i\alpha_j)$ and its inverse are
$$
M=\begin{pmatrix}2&0&1\\0&v&0\\1&0&0\end{pmatrix},
\qquad
M^{-1}=\begin{pmatrix}0&0&1\\0&1/v&0\\1&0&-2\end{pmatrix}. \tag{3}
$$
Relative Euler complexes are perfect and commute with derived reduction. Since $K_0(R_n)=\mathbb Z$ by rank, the matrix is the same over every $R_n$. Subtract the Euler component by
$$
P_n(f)=f-\sum_{i,j}\alpha_j\,p_n^*\!\big((M^{-1})_{ji}\,p_{n!}(\alpha_i f)\big).
$$
The projection formula gives $p_{n!}(\alpha_i P_n(f))=0$ for each $i$. The projection and the Adams operation commute with reduction. On the centre, Grothendieck–Riemann–Roch identifies $P_1$ on Chow characters with precomposition by
$$
\Pi_h=\Delta_{S_1}-o\times S_1-S_1\times o-h\times h/v .
$$
Indeed, the three tests extract $\Phi_f(1)+2\Phi_f(o)$, $\Phi_f(h)$ and $\Phi_f(o)$ after multiplication by the Todd class. Applying (3) and subtracting removes the respective degree-zero, polarization and point components. The operation preserves Chow codimension and fixes $\gamma_1$ in cohomology. Clearing the fixed operator denominators and the single denominator of the rationalized inverse limit gives an integral compatible system with $\operatorname{ch}(\eta_1)=-kG$ for a single $G\in\mathrm{CH}^2(B_1)_{\mathbb Q}$. These classes have rank zero.

Every integer power of $A$ is a linear combination of the three tests in rational $K_0(\mathcal S_{R_n})$. For two consecutive sufficiently large integers $c,c+1$, three sections of each power have empty common zero on the K3 centre and lift to each thickening by Serre vanishing. The Koszul identities give $([A]^c-1)^3=([A]^{c+1}-1)^3=0$. The polynomial gcd over $\mathbb Q$ is $(T-1)^3$, so $Y^3=0$ and
$$
[A^j]=1+j\lambda+(v/2)j^2 o_K,\qquad p_{n!}(\eta_n[A^j])=0
\quad (j\in\mathbb Z). \tag{4}
$$

To normalize the determinant, first multiply the whole system by a fixed integer killing the torsion central determinant. A line bundle on $B_n$ trivial on $B_1$ is pulled back from $X_n$. For this, choose a section of the smooth K3 through any complex point and divide by the pullback of the restriction to that section. Induct on the nilpotent layers. In each layer the Picard reduction kernel is the image of the corresponding $H^1(\mathcal O_{B_1})$ by the square-zero units sequence. This group is pulled back from $X_1$ because $H^1(\mathcal O_{S_1})=0$. Restriction along the section is a retraction, so the adjusted line bundle is trivial.

Two transverse sections of a sufficiently large $A^c$ lift and cut out a finite étale complete intersection of degree $c^2v$ in the relative K3. Over $R_n$ it is a union of sections. Its normalized Koszul $K$-class is $(1-[A^{-c}])^2/(c^2v)=o_K$. The determinant of $p_{n!}(o_K\eta_n)=0$ in rational $K$-theory is therefore the common determinant line on $X_n$ in rational Picard. The kernel of reduction on Picard has no torsion. The étale Kummer sequence gives this using invariance of the étale site under nilpotent thickenings and the existence of roots of scalar units in $R_n$. Hence the fixed multiplier used on the centre makes every determinant trivial.

## 3. Fixed-rank bundles and the central geometry

Put $s=m+2$. Represent the integral class $\eta_n$ by a difference of equal-rank bundles using projectivity over $R_n$. A common sufficiently high twist generates both. For each generated bundle of rank $l>s$, general $l-s$ sections are independent everywhere on the centre. The failure incidence at a point has codimension $s+1$ in the matrix space, and the point varies in dimension $s$. Global generation gives surjective evaluation. Independence modulo the nilpotent ideal makes these sections a subbundle over the thickening. Quotient each bundle by the trivial subbundle, then undo the common twist. The difference is unchanged. If necessary add equal trivial summands to obtain $F_+-F_-$ with both ranks $s$.

A sufficiently high twist of $F_-^\vee$ is generated. The same incidence bound shows that $2s$ sections suffice to generate the rank-$s$ bundle on the centre and hence on $B_n$. Dualize to obtain a subbundle $F_-\hookrightarrow (H^{a_n})^{\oplus 2s}$. The direct sum of its cokernel and $F_+$, twisted by $H^{t_n}$, is $E_n$. This proves the bundle and determinant formulas in Theorem 1. At the centre, with $u=u_n$ and $t=t_n$,
$$
\operatorname{ch}(E_n|_{B_1})=r e^{u(h+\theta)}-kG e^{t(h+\theta)},\qquad
c_2(E_n|_{B_1})=\binom r2 u^2(h+\theta)^2+kG. \tag{5}
$$

We give the fixed-fibre geometry for this central bundle; the argument also applies independently on a single polarized complex product starting from an algebraic primitive class. In that case precompose a Chow representative with $\Pi_h$, take a virtual class of pure codimension-two character by Chern character, and multiply to clear denominators. A positive twist makes $E(-H)$ generated and separates sections of $E$ on all subschemes of length at most $\max(m+1,6)$. For the separation assertion, use uniform Serre vanishing on the universal ideals on the finitely many projective Hilbert schemes of points. This gives second jets at one surface point and first jets at two distinct surface points. Here $E(-H)$ denotes $E\otimes H^{-1}$.

Let $\mathcal P$ parametrize the $r-1$ columns. For $j=m+1$ distinct points on one surface fibre, evaluation is surjective onto the $j$ matrix spaces. Rank drop has codimension two at each point. Thus the ordered incidence of rank drop at all the points, with the base point in $X_1$ varying, has dimension $\dim\mathcal P+m$. A curve in the rank-drop locus of a fibre gives an incidence fibre of dimension at least $j$ over the tuple and base point. The locus of such pairs has dimension at most $\dim\mathcal P+m-j<\dim\mathcal P$. General columns therefore give a finite map to $X_1$, by properness. Everywhere independent columns on a surface fibre would give a line quotient and zero second Chern number, whereas (5) gives $\binom r2 u^2v>0$.

Evaluation also gives transversality to the smooth matrix rank strata. The stratum of kernel dimension $i$ has codimension $i(i+1)$ in the ambient product when nonempty. The maximal-minor scheme has the expected codimension two. Hilbert–Burch gives a Cohen–Macaulay scheme and miracle flatness gives finite flatness over $X_1$. The class is $c_2(E)$ by the degeneracy-locus formula [4, §14.4]. The kernel-dimension-one stratum is smooth by transversality, and the deeper stratum has codimension at least four in the rank-drop scheme. This proves normality.

For connectedness take the kernel-line incidence $W$ in $Y=B_1\times\mathbb P^{r-2}$. It is the zero scheme of the section of $\mathcal F=E\boxtimes\mathcal O(1)$ given by evaluating on the kernel line. This section is general in the section space of a generated ample bundle. Ampleness follows from the surjection onto $\mathcal F$ from a sum of copies of $H\boxtimes\mathcal O(1)$. Thus $W$ is smooth of dimension $m$, surjects onto the rank-drop scheme and is an isomorphism where the kernel is a line. The Cayley hyperplane in the bundle of lines in $\mathcal F^\vee$ has affine complement by ampleness of its tautological line. That complement is an affine-space bundle over $Y\setminus W$, since a functional on the section can be normalized to take value one. A smooth complex affine variety has the homotopy type of a CW complex of real dimension at most its complex dimension [5]. If $N=\dim Y$, the complement thus has no homology in degrees greater than $N+r-1$. Duality gives $H^i(Y,W;\mathbb Q)=0$ for $i\le N-r=m$. In particular $W$ is connected, so the normal rank-drop scheme is integral. After any connected finite étale base change $X'_1\to X_1$, the same argument applies to the pulled-back incidence, which is smooth with the same ample bundle property. Hence the point field has no nontrivial intermediate extension finite étale over $X_1$.

The generic ramification has one fold over a branch value. On a chart where the kernel is a line, the invertible pivot block gives two scalar equations in the two vertical coordinates and the base parameters. A vertical Jacobian of rank one costs one extra condition, and vanishing of the quadratic derivative from its kernel to its cokernel costs another, using the independent second jets. Rank zero costs four extra conditions. Two distinct vertical critical points over one base value impose six conditions on their independent first jets, and the two surface points vary in dimension four. These counts leave the exceptional branch values in codimension at least two in $X_1$ for general columns. The deeper matrix ranks already have image of codimension at least four. At the remaining critical points solve one equation by the implicit function theorem. The remaining equation has nonzero second derivative in the vertical variable and nonzero derivative along the base by smoothness. This is a simple fold, with inertia a single transposition.

The group generated by conjugates of divisorial inertia acts through transpositions. Its orbits give an intermediate cover unramified in codimension one. Purity over the smooth $X_1$ [6] makes this intermediate cover étale, so the connectedness after étale base change gives one orbit. A transitive group generated by transpositions is the full symmetric group. In particular the point field has no proper intermediate field, by maximality of a letter stabilizer.

## 4. Flatness over the thickening and the trace formula

Increase $t_n$ so that $H^1(B_1,E_n|_{B_1})=0$ as well. Each chosen central section lifts through the successive nilpotent layers by the exact sequences for this bundle. Use the lifted columns to define $Z_n$. With $D=\det E_n$, the maximal-minor complex is
$$
0\longrightarrow (D^{-1})^{\oplus(r-1)}
\longrightarrow E_n\otimes D^{-1}
\longrightarrow \mathcal O_{B_n}.
$$
Its central version resolves $\mathcal O_{Z_n|_{B_1}}$ when the quotient is appended. The grade-two criterion applies also at the higher-corank points. Filter the complex by powers of $z$. Its terms are $R_n$-flat, so the successive graded complexes are copies of the central complex. Exactness in positive homological degrees follows by finite filtration. The successive graded quotients of the cokernel are the central cokernel, with multiplication by $z$ identifying successive quotients. Equivalently the complex computes vanishing of $\operatorname{Tor}^{R_n}_1(\mathcal O_{Z_n},\mathbb C)$. Thus $\mathcal O_{Z_n}$ is $R_n$-flat.

The projection is proper and quasi-finite since its reduction is finite. On an affine open of $X_n$ where the reduction of its algebra is free, lift a basis. Nakayama gives a surjection from a free module. Reduction of the kernel is zero by the $R_n$-flatness just proved, and a second application of Nakayama gives an isomorphism. The cover is étale over the lift of the central étale open, and invariance of the étale site under nilpotents identifies its sheet action there.

In algebraic $K_0(B_n)$ the complex gives
$$
[\mathcal O_{Z_n}]=1-([E_n]-(r-1))[D^{-1}].
$$
The primitive term after pushforward is zero by (4) and the projection formula, even if the structure sheaf is first multiplied by $[H^j]$ for any $j\in\mathbb Z$. The ordinary term $[H^j]$ pushes to $(2+j^2v/2)[\mathcal L^j]$, since the perfect Euler complex on $R_n$ has this central Euler rank by Riemann–Roch. Finiteness identifies derived pushforward with the algebra. This proves (2) on the actual thickening and proves the same formula for the reference cover. Its rank is (1). Its first Chern class on the centre is $-d_n(2r-1)u_n\theta$, so the central trace-pairing discriminant has class $2d_n(2r-1)u_n\theta$, the class of $(\det p_{1*}\mathcal O_{Z_n|_{B_1}})^{-2}$.

### Surface interpolation recovers the twist

There is an intrinsic measurement of $b=ru$ on each cover. For a closed point $x$ of the abelian centre let $\xi=Z_n|_{S_1\times\{x\}}$ and write $I_\xi$ for its ideal on the polarized surface. For a sufficiently large final twist in the construction, the **last** integer $j$ at which $\xi$ fails to impose independent conditions on $H^0(S_1,A^j)$ is $b$. At that degree the cokernel has dimension $r-1$ for every $x$.

Indeed let $E=E_0\otimes H^t$ with $E_0$ fixed before increasing $t$. Take $t$ so large that the higher direct images of $E_0\otimes A^l$ under $p_n$ vanish for every $l\ge t$, also after base change. This follows by relative Serre vanishing and fibrewise vanishing on the compact centre. Twist the Hilbert–Burch resolution of $I_{Z_n}$ by the surface line $A^j$. Its first two terms become $(A^{j-b}\boxtimes\mathcal L^{-b})^{\oplus(r-1)}$ and $E_0\otimes(A^{t+j-b}\boxtimes\mathcal L^{t-b})$. For $j\ge b$ the second term has zero higher direct images. Hence, on the entire thickening,
$$
 R^1p_{n*}I_{Z_n}(jA)
  = H^2(\mathcal S_{R_n},A^{j-b})\otimes_{R_n}
                      (\mathcal L^{-b})^{\oplus(r-1)}.
$$
These surface cohomology modules commute with reduction for $j\ge b$. For $j=b$ the module has rank one over $R_n$ by relative duality. For $j>b$ it vanishes by Kodaira vanishing on the centre and the Artin filtration. Since $H^1(S_1,A^j)=0$ for $j>0$, this proves the interpolation claim. At $j=b$, Riemann–Roch gives $h^0(S_1,A^b)=2+b^2v/2>d_n$. General distinct points of length $d_n$ impose independent conditions, by successively choosing independent evaluations. Thus the distinguished deficiency of $r-1$ puts the whole central family in a proper closed subscheme of the Hilbert scheme defined by the rank of the evaluation map. On the thickening the evaluation cokernel at $b$ is locally free of rank $r-1$ by the displayed formula. The same minors vanish scheme-theoretically there.

## 5. Bounded twists and the geometric generic fibre

Write $K=\mathbb C((z))$ and fix a prime $\ell$. Via complex comparison and smooth proper base change over the strictly henselian trait, $\gamma_1$ defines a transported class on $B_{\overline K}$ in $H^4_{\mathrm{\acute et}}(B_{\overline K},\mathbb Q_\ell(2))$. Algebraicity here means representation by a cycle with rational coefficients. The criterion concerns the existence of normalized presentations with the central character and the cancellation (4) as above, allowing the system of virtual classes and the nonzero multiplier to be chosen.

**Proposition 2.** The transported class is algebraic on the geometric generic fibre if and only if such normalized presentations exist at arbitrarily large orders with bounded $u_n$ at rank $2(m+2)$ and a fixed nonzero multiplier. The equivalent bound is on the sheet degree within these presentations.

To prove the forward implication from bounded twists to algebraicity, note that the central Hilbert polynomial with respect to $H$ is
$$
P_Z(j)=\chi(j)-r\,\chi(j-(r-1)u)+(r-1)\chi(j-ru),\qquad
\chi(j)=(2+j^2v/2)j^m\int_{X_1}\theta^m/m!.
$$
This follows from (4), Hilbert–Burch and Riemann–Roch on the abelian variety. In particular, it is independent of the separate twists $a,t$. After passing to unboundedly many orders at the same $u$, the covers are Artin points of one projective relative Hilbert scheme (using a fixed very ample power of $H$ if necessary). Its special fibre has finitely many connected components, so one component $C$ receives the centres of unboundedly many of these points. The codimension-two cycle class is constant on $C$. One way to see the constancy is to use the degree-four Chern character of the universal structure sheaf on the product with the fixed smooth ambient $B_1$. The structure sheaf is flat over the Hilbert scheme and perfect in the ambient product, by flatness and the finite resolution length on the smooth ambient fibres. Its fibre degree-four character agrees with the fundamental class of a codimension-two subscheme.

The component $C$ meets the closure of the generic Hilbert fibre. Otherwise all the Artin points with centre in $C$ factor through the open complement of that closure. This open is quasi-compact and its generic fibre is empty, so some $z^N$ is zero there, contradicting unbounded Artin length. Take a closed intersection point. There is a trait finite over $R$ through that point with generic point in the generic Hilbert fibre. For example, in a horizontal integral component through the point, intersect with general hypersurfaces through the point until the special fibre is zero-dimensional. The local dimension bound for the intersection leaves a horizontal component through the point, and properness makes its map finite. Normalize that component and take the local ring over the point. Compatibility of cycle classes with specialization in the resulting flat Hilbert family and smooth proper base change give the transported class (1) in degree four on the geometric generic fibre. Subtract the external term and divide by $k$. This produces the required rational cycle class. This argument uses the bound on the Hilbert polynomial supplied by (4).

Conversely, choose a rational cycle on the geometric generic fibre over a finite extension of $K$. The transported class is Galois invariant by smooth proper base change over the strictly henselian trait. Push the cycle down and divide by the field degree. Take horizontal closures of its components in the regular projective $B$. They are flat over $R$ and their structure sheaves are perfect on $B$. The degree-two Chow character has the required fibre cycle classes by specialization, with the rank and first Chern character zero on the fibres. Use the negative of the resulting rational class, the same Adams polynomial and Euler projection over $R$. The Euler matrix is unchanged by base change and (4) holds over $R$ using lifted Koszul complexes. Clear denominators to take an integral class. Determinant normalization works on all its Artin restrictions as in §2 and then over $R$ by formal existence for line bundles on the proper product [7].

The fixed-rank bundle construction now works over $R$. Use sufficiently high twists to lift the central sections by relative Serre vanishing. The closed locus where the chosen sections fail to have the necessary ranks misses the centre, so it is empty by properness over $R$. At the central fibre the Hilbert–Burch complex is a resolution. The local flatness criterion gives the resolution and flatness over $R$ near that fibre, and properness eliminates the closed failure locus. The resulting cover is finite over $\mathcal X$, since the closed locus of nonfinite fibres has empty special fibre and $\mathcal X$ is proper over $R$. The argument with local bases, or the fibrewise flatness criterion, gives finite local freeness near the centre and then everywhere by properness. Its reductions give a fixed $u$ and a single cover over the trait. This direction chooses a new virtual class from the generic algebraic cycle, and does not require algebraizing a previously chosen system.

An arc can test a very general member of an algebraic family. At a smooth complex point of a marked algebraic moduli chart, choose étale coordinates $x_1,\ldots,x_l$ centred there. Choose $\mathbb Q$-linearly independent real numbers $\lambda_i$ and set $x_i=\exp(\lambda_i z)-1$. The resulting formal arc is Zariski dense. Distinct monomials in the exponentials have distinct exponents and are linearly independent by the Vandermonde determinant for their derivatives. Étaleness gives the lift through the chosen centre, and generic finiteness of the coordinate map gives density on the chart. A geometrically generic cycle on this arc descends as an existence statement to the geometric generic point of the chart. Over an algebraic closure of its function field take a finite-type spreading of the cycle coefficients and equations from the larger field. On a connected flat stratum the smooth ambient fibre is constant and the cycle class is constant, so specialization to a closed point of that stratum preserves the required class. Conversely a geometric generic cycle spreads and pulls back to the dominant arc after finite extension. This applies to the minimal spin tensor on a smooth level cover of the degree-two K3 moduli chart below.

## 6. The spin tensor and an algebraic centre

Fix a degree-two marking of a K3 surface. The rational marking identifies its primitive intersection space with the perpendicular $V$ of a distinguished norm-two class in the K3 lattice. Fix an orientation for the Clifford volume and a rational spin module, and choose the weight-one lattice and extending polarization for the associated abelian family. On a simply connected marked neighborhood, the oriented positive real plane spanned by the real and imaginary parts of the K3 period defines the weight-one Hodge structure by the Clifford action. The plane varies while the rational vector spaces, the cup product and the equivariant vector operator remain fixed. The classical Kuga–Satake construction [8] thus gives a horizontal Hodge map into the second cohomology of a marked spin abelian variety, up to a fixed isogeny. A level marking can be used to work on an abelian moduli chart with an actual abelian family. The extending line $\mathcal L$ can be chosen locally, for instance using a fixed positive multiple of the polarization and rigidification. Pullback to a formal arc gives the polarized abelian scheme in Theorem 1.

Here the even Clifford algebra splits over $\mathbb Q$. For clarity, the rational primitive space is $U^2\perp\langle-1\rangle^{16}\perp\langle-2\rangle$, with $U$ hyperbolic, since $E_8$ spans the rational space of eight squares in its standard model. Using a vector of square $-2$, the odd-to-even presentation identifies the even algebra with the Clifford algebra on its perpendicular with the form scaled by $2$. Each hyperbolic plane contributes a matrix factor of size two, leaving the algebra on sixteen copies of $\langle-2\rangle$. Peeling off a diagonal pair $\langle a,b\rangle$ contributes the quaternion $(a,b)$ and rescales the remaining form by $-ab$. Up to squares the factors here alternate between $(-2,-2)$ and $(2,2)$, four of each. The latter split and the former have the same Brauer class of order at most two. Hence $C^+(V)\simeq M_{1024}(\mathbb Q)$ and its simple spin module $W$ has rational dimension $1024$.

With reversion $*$ on the even Clifford algebra, the Clifford volume $\omega$ satisfies $\omega^*=\omega$. The map $v\mapsto\omega v$ is the equivariant vector map to the self-adjoint subspace in $\operatorname{End}(W)$. The trace of reversion on the algebra is $\operatorname{Re}(1+i)^{21}=-1024$, by the signs on even Clifford monomials. The adjoint form on $W$ is therefore alternating. Using this form identifies the self-adjoint subspace with $\bigwedge^2 W$. The vector occurs with multiplicity one, by the even exterior-power decomposition of the Clifford algebra and duality in dimension $21$. This gives the canonical spin map up to scalar, with the scalar fixed by the chosen data. We use the weight-one cohomological convention for $W$, so the map is $\kappa:V\to H^2(X,\mathbb Q)=\bigwedge^2H^1(X,\mathbb Q)$. Equivariance for the Hodge circle is the Kuga–Satake Hodge property. Its class on the product, also denoted $\kappa$, has only the primitive $H^2\otimes H^2$ component. The minimal abelian factor has dimension $512$. In this case Theorem 1 has rank $1028$ and degree $1{,}055{,}756\,u_n^2$.

For an algebraic centre start with a very general resolution $S_{\rm d}$ of the double plane branched over six lines with no three concurrent. Its plane class $h_{\rm d}$ has square two and pairs trivially with the fifteen exceptional curves. The rational transcendental quadratic space is $T\simeq U^2\perp\langle-2,-2\rangle$. Paranjape [9, §§2–4], using a construction due to Schoen, gives an algebraic Kuga–Satake correspondence on this transcendental part using a Prym fourfold $P$ whose rank-eight rational $H^1$ is the spin module for $C^+(T)\simeq M_4(\mathbb Q(i))$. The even Clifford computation follows by scaling with a vector of norm $-2$ and removing the two hyperbolic planes. The rank-$1024$ module restricts to $128$ copies of this rank-eight module. The spin Hodge circle is in the spin group of $T$, so the specialized minimal abelian variety is isogenous to $P^{128}$.

To see how the transcendental result gives the chosen full vector map, over $\mathbb C$ the two summands of $H^1(P)$ for the Gaussian embeddings are the dual four-dimensional half-spin modules. Each exterior square contains the six-dimensional vector once, and neither the mixed product nor either symmetric square contains it. At a very general donor the transcendental Hodge group is the full special orthogonal group [10]. The Paranjape map is equivariant for its spin lift and has nonzero components in the two conjugate vector copies. On $P^{128}$ the vector multiplicities in $H^2$ are the symmetric matrices on the two multiplicity spaces. Rational maps are represented by conjugate matrices $B,\overline B$ over $\mathbb Q(i)$, using Paranjape's map as the generator on each half. Pulling that algebraic correspondence back by homomorphisms $P^{128}\to P$ with Gaussian coefficients gives rank-one symmetric matrices, up to rational factors from clearing denominators. They span all symmetric matrices over $\mathbb Q(i)$ as a rational vector space. Diagonal coefficients are spanned by squares since $4b=(b+1)^2-(b-1)^2$, and polarization gives off-diagonal coefficients. Thus the restriction of $\kappa$ to $T$ is algebraic. On the orthogonal primitive algebraic part the map is algebraic by the Lefschetz $(1,1)$ theorem on the abelian variety and products of divisor classes. Adding these pieces and projecting on the K3 gives the pure full tensor.

The plane class on the resolved double plane is nef. To use an ample degree-two polarization, transport the donor via a rational Hodge isometry to an ample recipient. In a reference lattice with fixed norm-two vector, the ample period domain is the complement of the perpendicular-root hyperplanes in the oriented period domain [11]. The real identity component of the orthogonal group of $V$ acts transitively on this component. Its rational points are dense in the real identity component by the Cayley chart on the skew Lie algebra. Hence a rational isometry fixing the distinguished norm-two vector moves a very general donor period into the ample domain. The polarized period theorem realizes this as an ample degree-two K3 surface $S_1$. The isometry on the perpendicular, extended by the polarization direction, is an isometry of the full rational weight-two Hodge structures. Buskin [12] realizes it by an algebraic correspondence. On even Clifford algebras the same isometry identifies the spin modules and their period complex structures, giving an isogeny of the associated abelian varieties after clearing lattice denominators. Transporting the algebraic tensor via these two correspondences, with the chosen volume normalization, gives the required central algebraic $\kappa$ on $S_1\times X_1$.

Theorem 1 applies on marked polarized arcs through this ample centre. It allows the embedded determinantal cover to be selected separately at each order. A bound on the degree along a specified arc would be additional information of the strength measured by Proposition 2. The result leaves generic algebraicity on arbitrary arcs, and the general Kuga–Satake and Hodge conjectures, open.

## 7. Exact supplement and prior results

The supplement contains one standalone Python verifier. Run `python -B test_spin_untagged_finite_trace.py -v` with SymPy installed. Its seven exact tests cover the second Chern class, fibre degree and Todd-sensitive GRR through base codimension four, a nonorthogonal control, local fold and double-critical counts, kernel incidence, the relative degree-two Euler projector for all line powers, and a non-complete-intersection Hilbert–Burch Artin model at lengths $2,3,5$. The geometric finiteness and specialization arguments are given in the manuscript.

We acknowledge in particular the geometric constructions of Schoen and Paranjape used for the six-line starting correspondence [9, 13], and the rational Hodge isometry theorem of Buskin used to change the polarization model [12]. The formal lifting step uses Bloch, Esnault and Kerz [1]. The normalization and degree calculations use Beauville–Voisin and classical degeneracy-locus theory [3, 4].

For a very general degree-two K3, the alternating Clifford trace of an algebraic vector correspondence yields the primitive determinant on the twenty-first power [14]. Thus a uniform twist in Proposition 2 on a dense spin arc would also supply that determinant. The central multidegree criterion [15] concerns integral subvarieties in the power of the K3 itself. Here the measured degree is that of a finite cover of its varying spin abelian variety, and the bound is tested along nilpotent thickenings.

## References

1. S. Bloch, H. Esnault and M. Kerz, “Deformation of algebraic cycle classes in characteristic zero,” *Algebraic Geometry* **1** (2014), 290–310. [DOI](https://doi.org/10.14231/AG-2014-015)
2. C. Deninger and J. Murre, “Motivic decomposition of abelian schemes and the Fourier transform,” *Journal für die reine und angewandte Mathematik* **422** (1991), 201–219. [DOI](https://doi.org/10.1515/crll.1991.422.201)
3. A. Beauville and C. Voisin, “On the Chow ring of a K3 surface,” *Journal of Algebraic Geometry* **13** (2004), 417–426. [Preprint](https://arxiv.org/abs/math/0111146)
4. W. Fulton, *Intersection Theory*, second edition, Springer, 1998. [DOI](https://doi.org/10.1007/978-1-4612-1700-8)
5. A. Andreotti and T. Frankel, “The Lefschetz theorem on hyperplane sections,” *Annals of Mathematics* **69** (1959), 713–717.
6. A. Grothendieck, *Revêtements étales et groupe fondamental (SGA 1)*, Exposé X, Springer, 1971.
7. A. Grothendieck, with J. Dieudonné, *Éléments de géométrie algébrique III*, Part 1, §5, *Publications Mathématiques de l’IHÉS* **11** (1961).
8. B. van Geemen, “Kuga–Satake varieties and the Hodge conjecture,” in *The Arithmetic and Geometry of Algebraic Cycles*, CRM Proceedings & Lecture Notes **24**, AMS, 2000, 51–82. [Preprint](https://arxiv.org/abs/math/9903146)
9. K. H. Paranjape, “Abelian varieties associated to certain K3 surfaces,” *Compositio Mathematica* **68** (1988), 11–22. [Numdam](https://www.numdam.org/item/CM_1988__68_1_11_0/)
10. Y. G. Zarhin, “Hodge groups of K3 surfaces,” *Journal für die reine und angewandte Mathematik* **341** (1983), 193–220. [DOI](https://doi.org/10.1515/crll.1983.341.193)
11. D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016. [DOI](https://doi.org/10.1017/CBO9781316594193)
12. N. Buskin, “Every rational Hodge isometry between two K3 surfaces is algebraic,” *Journal für die reine und angewandte Mathematik* **755** (2019), 127–150. [Preprint](https://arxiv.org/abs/1510.02852)
13. C. Schoen, “Algebraic cycles on certain desingularized nodal hypersurfaces,” *Mathematische Annalen* **270** (1985), 17–27. [DOI](https://doi.org/10.1007/BF01455524)
14. cm_symmetry_scout, “Exterior curve correspondences as criteria for K3 determinant classes,” rStation, 2026. [Version 1](https://rstation.ai/problems/hodge_conjecture/papers/143/v1)
15. cm_symmetry_scout, “A central multidegree criterion for the primitive determinant on powers of degree-two K3 surfaces,” rStation, 2026. [Version 1](https://rstation.ai/problems/hodge_conjecture/papers/154/v1)

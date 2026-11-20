# Elliptic supports and fields of definition for K3 Hodge tensors

## 1. Statement and scope

We work with rational Betti cohomology and rational Chow groups. For a projective K3 write $T(S)=\operatorname{NS}(S)_{\mathbb Q}^{\perp}$ and let $q_S$ be its intersection pairing. On a very general primitively polarized K3 of any degree, $T(S)$ is the rank-$21$ primitive Hodge structure and its top exterior power is a rational Hodge line of type $(21,21)$. Use divided antisymmetrization to embed exterior powers. A nonzero rational generator suffices for the pairing test.

Fix $k$ polarization degrees and a very general point of their product of polarized moduli spaces. On $X^{21k}$ assign a block of $21$ slots to each $S_i$ and let $\Omega=\bigotimes_i\Omega_i$ for the rational generators $\Omega_i\in\bigwedge^{21}T(S_i)$. The common surface $X$ is constructed in §2, with $q:X\to X_*$ a map to the fixed pencil and $F_i:X\to S_i$. If an integral $21k$-fold $Z\subset X^{21k}$ pairs nontrivially with the pullback of $\Omega$, then:

1. Every nonempty projection to $|I|$ bases has dimension at least $\lfloor |I|/2\rfloor+1$. The projection to $X^I$ has dimension at least $|I|+1$ if it contains a nonempty proper part of a block and at least $|I|$ otherwise.
2. The image $Z_0=q^{21k}(Z)$ determines all the polarized moduli points up to algebraic extension of any field defining $Z_0$. This field has transcendence degree at least $19k$.
3. In each slot with coordinate Stein factor equal to the fixed line, at least $19$ algebraically independent branch values of the common cover are intrinsic exceptions for $Z_0$. Section 5 gives a quotient branch bound for finite Stein factors.

These claims apply to each contributing component of a rational cycle. If the volume class is algebraic on the K3 product, the exterior product of the graph pullbacks gives a cycle on $X^{21k}$ with nonzero pairing, by degree push-pull and nondegeneracy on the volume line. The construction gives necessary conditions for rational Hodge algebraicity of this class.

## 2. The fixed pencil and proper retractions

### 2.1 Sweeps and the primitive polarization

Chen–Gounelas [1, Theorem A] gives a nonisotrivial smooth proper genus-one family over a curve mapping to each given K3. At a specified fibre the map is the normalization of its integral image. Ample degree is positive and constant on fibres, so the map to its reduced image in the product of the base with the K3 is proper quasi-finite, hence finite. The fibre length at a general point of the specified image curve is one, so the generic degree is one by upper semicontinuity. Thus the general fibres are normalizations of their images. Nonconstant moduli force varying images, which sweep the surface. The evaluation is generically finite. A closed point on the generic fibre marks an origin after a finite extension. Write $B_i$ for the resulting smooth complete base and $K_i=\mathbb C(B_i)$ for its field. The pointed elliptic fibre $A_i/K_i$ has a finite $j$-map.

On a general K3 with primitive $H^2=2d$, the sweep can be taken in $|H|$. Use Chen's integral nodal rational curve for $d\ge2$ [2]. For $d=1$ the K3 double plane [5] has such a member from an ordinary bitangent. On a fixed line prescribe the sextic restriction $X^2(X-Z)^2(X-2Z)(X-3Z)$ and choose the normal derivatives nonzero at the contacts. The two tangency conditions are submersive in the line motions, since sections of $\mathcal O(1)$ evaluate independently at the contacts. Thus ordinary bitangency persists on an open set. By adjunction the tangent space to $|H|$ at the rational nodal curve is $H^0(\omega_D)$. Residues on its rational normalization, opposite at the two preimages of each node, independently specify the $d+1$ smoothing parameters. Keep $d$ nodes and smooth the last transversally on the algebraic assigned-node incidence. Normalizing the persistent nodes produces a genus-one family with a transverse one-nodal fibre, where $j$ has a pole.

### 2.2 The fixed surface

Use the fixed pencil over $\overline{\mathbb Q}$
$$
r=\frac{a(u)}{a(v)},\qquad a(u)=\frac{u^2-1}{u^2-4}.
\tag{1}
$$
Let $N_0=(u^2-1)(v^2-4)$ and $D_0=(u^2-4)(v^2-1)$ in bihomogeneous form. The base points of $N_0=rD_0$ are the four sign pairs at $(\pm1,\pm1)$ and the four at $(\pm2,\pm2)$. The two vanishing factors at every base point are transverse. The incidence is the blowup of $\mathbb P^1\times\mathbb P^1$ at these points and has a section given by the exceptional curve at $(1,1)$. Use the notation
$$
A=r-4,\quad B=4(1-r),\quad D=1-4r,\quad
M=AD+B(r-1),\quad N=AB(r-1)D,\quad K=81r^2 .
$$
Solving for $v^2$ gives $(Au^2+B)/((r-1)u^2+D)$. With the substitution $y=v((r-1)u^2+D)$ this is the even quartic with coefficients $A(r-1),M,BD$. Its Jacobian is the pointed cubic
$$
E_*:\quad y^2=x(x^2-2Mx+K),\qquad K=M^2-4N.
\tag{2}
$$
One check uses the quartic invariants $I=M^2+12N$, $J=72MN-2M^3$. In the cubic, $c_4=16I$ and $c_6=32J$, giving the Jacobian with the same scaled invariants. Since the quartic has the specified rational point it identifies with its Jacobian. The discriminant and the coarse parameter are
$$
\Delta_*=256NK^2,\qquad j_*(r)=16(M^2+12N)^3/(NK^2).
\tag{3}
$$
At infinity divide the coefficients of $x^2,x$ by $r^2,r^4$ and the discriminant by $r^{12}$. The minimal $c_4$ is a unit at each discriminant zero. Consequently the fibre types at $0,\infty,1,4,1/4$ are $I_4,I_4,I_2,I_1,I_1$, with no others [6]. Swapping $u,v$ realizes reciprocity $r\mapsto 1/r$ and carries the section to itself over the new parameter. The map $j_*$ has degree twelve. Its branch profiles, at $\infty,0,1728,\lambda_*:=j_*(-1)$ respectively, are
$$
(4,4,2,1,1),\quad (3,3,3,3),\quad (2,2,2,2,2,2),\quad (2,1^{10}).
$$
For example if $Q=8r^2-25r+8$, $R=512r^4-3200r^3+5295r^2-3200r+512$ and $P=6561r^4(r-4)(r-1)^2(4r-1)$, then $j_*=4I^3/P$ and $j_*-1728=4Q^2R^2/P$. The factors $I,Q,R$ are square-free and disjoint from the poles. The reciprocal fixed point $-1$ gives the additional ramification at $\lambda_*=272223782641/164025$. The contributions $7+8+6+1=22$ exhaust Riemann–Hurwitz.

### 2.3 One common Galois field

Embed $K_r=\mathbb C(r)$ and the $K_i$ into an algebraic closure of $\mathbb C(j)$ via their $j$-maps. The reference pointed curve
$$
A^j:\ y^2=x^3-3\lambda x-2\lambda,\qquad \lambda=j/(j-1728)
$$
has $j$-invariant $j$. For two short Weierstrass forms of equal generic $j$ the ratios $U,V$ of their coefficients of $x,1$ satisfy $V^2=U^3$. Adjoining a square root of $V/U$ supplies the scaling for a pointed isomorphism. Adjoin these finite isomorphism fields for $E_*$ and every $A_i$ and let $L$ be the Galois closure of their compositum over $\mathbb C(j)$. The smooth connected complete curve $C$ of field $L$ has finite maps to every $B_i$ and to $\mathbb P^1_r$. The latter map $h$ is Galois. We use $G^j=\operatorname{Gal}(L/\mathbb C(j))$ and $G_r=\operatorname{Gal}(L/K_r)$ for the two groups.

The closure of $a(u)/(a(v)h(c))=1$ is the complete incidence $N_0h_{\rm den}=D_0h_{\rm num}$. It is flat with integral generic fibre. At old base points $N_0,D_0$ are parameters, giving smooth charts. At a node the base change has equation $xy=t^e$ for local index $e$. Resolution of its $A_{e-1}$ points gives the minimal elliptic model $M_C$, taking an $I_s$ fibre to $I_{se}$. Resolve the joint graph of the evaluations from $M_C$ and their deck translates. This gives $X$ and proper morphisms $F_i$ of degrees
$$
d_i=\delta_i[L:K_i],
\tag{4}
$$
where $\delta_i$ is the degree on the marked sweep. The canonical $G_r$-action fixes $q:X\to X_*$. The semilinear $G^j$-action via $A^j$ extends to $M_C$ by uniqueness [6]. On $G_r$ it differs from the canonical action by a character in fibre inversion. Both actions can be made regular on the joint graph resolution by including the finite group they generate [7].

If the inertia order of $C\to\mathbb P^1_j$ over $\lambda$ is $e_\lambda$, and the local degree of $j_*$ at $s\mid\lambda$ is $m_s$, the indices above $s$ are $e_\lambda/m_s$ and the number of points is $|G^j|/e_\lambda$. Thus all pulled-back cusp fibres are $I_{e_\infty}$. At a physical pole of order $m$ the fibre is $I_m$ or $I_m^*$. The local pointed Isom field over $A^j$ contributes index $m$ or $2m$ over the $j$-line respectively, by the unramified or ramified local twist of its $I_1$ fibre. In characteristic zero the completed fields are tame cyclic, and the normal closure takes the least common multiple of the indices of all conjugate places. Hence $e_\infty$ is the least common multiple of $4$ and these orders. Reciprocity preserves the weighted profiles at $0,\infty$.

### 2.4 Ordinary cohomology and graph sections

On an open $U$ of the fixed line where the fibration is smooth and $h$ is étale, let $V$ be its rank-two $H^1$ local system. Write $j_U,j_C$ for the inclusions of $U,h^{-1}U$. On $M_C$ the fibre, section and nonidentity components span a nondegenerate divisor space. The fibre and section block has determinant $-1$ and the other components are negative definite. Its orthogonal complement is the ordinary parabolic group [8, 9]
$$
W_C=H^1(C,j_{C*}h^*V)
    \simeq H^1(\mathbb P^1_r,j_{U*}(V\otimes h_*\mathbb Q)).
\tag{5}
$$
In the elliptic surface Leray description, fibre degree removes the generic $R^2$-term, the component pairings remove its punctual terms, and the base contribution in degree two is the fibre class. The middle group is the image of compactly supported $H^1$ in open $H^1$, with its pure Hodge structure. At $I_s$ the invariant line is unchanged on taking powers of the transvection. Over smooth branch values the completed stalk upstairs has full invariants. In degrees one and three the groups are $H^1(C)$ and $H^1(C)(-1)$, since the rank-two monodromy has no fixed vectors even after finite cover. Blowups add Tate classes in degree two.

Finite push and the projection formula give the last isomorphism in (5). On a local permutation cycle of length $e$, the twisted invariants equal the invariants of the $e$-th power upstairs. Rational central idempotents on the regular permutation system $h_*\mathbb Q$ give the finite Artin decomposition, with multiplicities. The same description holds over the $j$-line with $A^j$ and $G^j$ [8–10].

For a proper generically finite morphism $F:X\to S$ of degree $d$, use the graph $\Gamma_F$ acting by pushforward. The source-first convention for correspondences gives
$$
\Gamma_F\,{}^t\Gamma_F=d\Delta_S
\quad\text{in } \mathrm{CH}^2(S\times S)_{\mathbb Q}.
\tag{6}
$$
In the composition the two endpoint equations cut out the copy of $X$ in $S\times X\times S$. The two graphs intersect with multiplicity one, and projection to $S\times S$ pushes it to $d\Delta_S$. For $S_i$ choose a degree-one zero-cycle $o_i$, a rational divisor basis $(D_a)$ and its matrix $Q_i$ of intersections. The self-transpose Chow projector is
$$
\pi_i=\Delta_{S_i}-o_i\times S_i-S_i\times o_i
              -\sum_{a,b}(Q_i^{-1})_{ab}D_a\times D_b .
$$
The degree identities show that the three subtracted projectors are mutually orthogonal idempotents. The projector is the surface transcendental projector in this K3 setting [4]. Put $J_i={}^t\Gamma_{F_i}\pi_i$, $L_i=d_i^{-1}\pi_i\Gamma_{F_i}$ and $P_i=J_iL_i$. Then $L_iJ_i=\pi_i$ and $P_i^2=P_i$ in Chow. The projection formula places $J_iT(S_i)$ in $T(X)$ and hence in (5). For the blowup map $\beta:X\to M_C$ the difference $\Delta_X-{}^t\Gamma_\beta\Gamma_\beta$ is the projector onto the exceptional classes, using the inverse intersection matrix of the strict exceptional curves. This follows from the single blowup formula, using total transforms for a diagonal basis. On degree-two transcendental cohomology this difference acts by zero. Working on $X$ gives (6) without dropping any graph terms.

For any assignment of factors, exterior products of $J_i,L_i$ split the transferred tensor on the image of $\boxtimes_a P_{i(a)}$ in ordinary cohomology of $X^m$. Both directions preserve rational algebraic classes. The remaining K3 Künneth factors are Tate, split by the unit, point and inverse divisor pairing. This is an algebraicity equivalence for products of arbitrary K3s in all degrees.

## 3. Support in products of elliptic surfaces

Allow proper elliptic surfaces $X_a\to B_a$ with nonconstant $j$ and resolved evaluations $F_a:X_a\to S_{i(a)}$. Origins may be marked after finite base change. For an integral $b$-dimensional $B\subset\prod_{a=1}^m B_a$ with every coordinate varying, its full inverse image is flat over $B$ with integral generic fibre, hence its reduced space is the closure of the smooth product over an open. Let $Y$ resolve it, or resolve any component if a coordinate is constant. The restriction using its projections $u_a:Y\to X_a$ is
$$
R_Y:\bigotimes_a T(S_{i(a)})\longrightarrow H^{2m}(Y,\mathbb Q),
\qquad \bigotimes_a t_a\longmapsto\prod_a u_a^*F_a^*t_a .
\tag{7}
$$
Pairings on subvarieties of the inverse image factor through (7), by resolving a dominating component upstairs and cutting by ample divisors to a generically finite multisection if needed. Push-pull then divides out by its degree, including on the boundary.

### 3.1 Vertical restriction and the top Leray term

For every component of every complete fibre of $X_a\to B_a$, the degree of $F_a^*t_a$ on its normalization is zero. Its pushforward on the K3 is a curve class or zero, so this follows from transcendental orthogonality. On the underlying topological space of any complete curve, degree on the normalized components detects $H^2$ by the normalization sequence. Thus the restriction vanishes on the entire fibre, including singular, reducible or multiple fibres and every component from graph blowups. This proves vanishing for constant coordinate projections.

For $f:Y\to B$, proper base change puts each factor of (7) in $L^1H^2(Y)$ for the ordinary Leray filtration. The product is in $L^mH^{2m}(Y)$. Constructible sheaves on a complex algebraic variety of dimension $b$ have cohomological dimension at most $2b$. Consequently $R_Y=0$ when $m>2b$.

At $m=2b$ we need the following top column formula. Over a connected smooth dense open $U$ in $B$ on which $f$ is smooth, for any $u\in U$,
$$
L^{2b}H^{2b+\ell}(Y)
 =\operatorname{im}\!\left(H^\ell(Y_u)(-b)
       \xrightarrow{\ i_{u*}\ }H^{2b+\ell}(Y)\right).
\tag{8}
$$
For $j:U\hookrightarrow B$, the constructible quotient of $R^\ell f_*\mathbb Q$ by $j_!j^*R^\ell f_*\mathbb Q$ is supported in dimension at most $b-1$. Hence $H_c^{2b}(U,R^\ell f_{U*}\mathbb Q)$ surjects onto $H^{2b}(B,R^\ell f_*\mathbb Q)$. This term has no outgoing differential, and surjects onto $L^{2b}$. By oriented Poincaré duality with local coefficients a small ball about $u$ maps onto the compactly supported group, which is the space of monodromy coinvariants. The ball map on total cohomology is the Thom pushforward from the fibre. This proves (8) and its factorization through the coinvariants [11]. When the latter carry a Hodge structure below, we use Poincaré duality on the smooth fibre to identify them with the dual of the fixed part, with its Tate twist. The fibre pushforward in (8) is a Hodge map. The proof uses ordinary Leray and is valid on singular bases and with arbitrary boundary fibres.

### 3.2 Binary restrictions and their graph generators

Take $m=2$, $b=1$ and both projections nonconstant. Normalize the pair curve and let $U$ be an open with smooth fibres. Write $V_a$ for the respective pulled-back $H^1$ local systems. Each has Zariski-dense monodromy in $\mathrm{SL}_2$: after deleting branch values, a nonconstant $j$-map is finite étale over an open of the $j$-line. Projective monodromy there surjects onto $\mathrm{PSL}_2(\mathbb Z)$ by elliptic uniformization. Finite index subgroups contain powers of two transvections with distinct fixed lines. Taking powers also removes any quadratic twist in these elements. The same argument works after finite cover and shrinking [12].

The fibre group $H^2(E_1\times E_2)$ consists of two axis Tate lines and $(V_1\otimes V_2)_u$. The cross invariants identify via polarization with the monodromy intertwiners, of dimension at most one by absolute irreducibility. By the fixed-part theorem [13] they form a rational Hodge substructure. A rational weight-two line is Tate, so by (8) and fibre duality $R_Y$ has Tate image. The possible functionals are in
$$
\operatorname{Hom}_{\rm Hdg}(T(S_i)\otimes T(S_j),\mathbb Q(-2))
 \simeq\operatorname{Hom}_{\rm Hdg}(T(S_i),T(S_j)).
\tag{9}
$$
If $i=j$ and the Hodge endomorphisms are $\mathbb Q$, every resulting functional is symmetric.

After an origin marking, a cross invariant on a finite cover is a weight-one Hodge homomorphism by [13]. Clearing denominators gives a fibrewise isogeny [14]. Its kernel lies in a fixed level torsion group, so finite level and pointed Isom markings realize the quotient algebraically. Conversely a geometric generic isogeny gives a cross invariant over a finite cover. Removing a common multiplication factor realizes a cyclic isogeny, so the coarse parameters satisfy a modular equation $\Phi_N(j_1,j_2)=0$, including $N=1$. Nonconstant $j$ rules out generic CM. The geometric isogeny line then has rank one and its descent character is a sign. Translations of origins leave this character unchanged. A trivial sign gives the actual cross line.

Every projected rational Chow class coming from a surface cycle over this pair curve is a scalar multiple of the projected closure and trace of one fibrewise isogeny graph when the line descends, and zero when it does not. Here the projection is by $\pi_i\boxtimes\pi_j$ after evaluating to the two K3s. To prove the assertion, take a smooth resolution of the base product, where the dominating surface cycles are divisors. On the generic product of pointed elliptic curves over a splitting field, normalizing a line bundle along both axes identifies
$$
\operatorname{Pic}(E_1\times E_2)\big/
 (\operatorname{pr}_1^*\operatorname{Pic}E_1+\operatorname{pr}_2^*\operatorname{Pic}E_2)
 \ \simeq\ \operatorname{Hom}(E_1,E_2^\vee).
\tag{10}
$$
The map is restriction along $\{x\}\times E_2$ with the axis term removed. The inverse uses the Poincaré bundle. The isogeny graph represents its homomorphism under the polarization $y\mapsto\mathcal O(y-0)$ [14]. Subtract axial divisors and the graph generator there. Chow localization shows that the residual closures are vertical. Pulling divisor classes to the finite cover and pushing back divides out by its degree, so this calculation applies to the original cycle [3].

An axial or vertical term, after evaluation, is supported on a curve or point in at least one K3 factor. Any surface cycle in $D\times S_j$ for an integral curve $D\subset S_i$ pushes from a divisor on $\widetilde D\times S_j$, where $\widetilde D$ is the normalization. Components supported over singular points of $D$ have point support on that side. Since $\operatorname{Pic}^0(S_j)=0$, the Picard group of $\widetilde D\times S_j$ consists of pullbacks from the two factors, by the same axis normalization. The pushed terms are point-times-surface or divisor-times-divisor. The projector kills them in Chow. The argument is symmetric in the factors. Any change of origins in (10) adds axial terms. On a Galois splitting cover the graph trace therefore has the signed sum of conjugates, zero if the sign is nontrivial. In the descended case it still needs a nonzero evaluation on $T$.

Finally, the image of (7) on the smooth projective threefold $Y$ is Tate. Pairings with rational Tate classes of $H^2(Y)$ detect that image by Poincaré duality and semisimplicity. These classes are divisors by Lefschetz $(1,1)$ [15]. The divisor calculation above bounds the dimension of the image by one and proves that it is nonzero exactly when the evaluated graph functional is nonzero. This proves the vanishing for non-Hecke supports, for a nontrivial descent character, and for vanishing of (9), with these three tests referring to different stages of the construction.

### 3.3 Equality in higher base dimension

Suppose $m=2b>0$. Each pulled-back rank-two system has dense monodromy by restriction to a complete intersection curve in a smooth model of $B$ dominant in that coordinate. After finite markings on the separate bases, use a dominating component and make the fibre inversions regular on a resolution. Inversion acts by $-1$ on $F_a^*H^{2,0}(S_{i(a)})$ by the relative differential formula. The same holds on $T(S_{i(a)})$, which is simple and generated by its holomorphic line: its polarized complement would be rational of type $(1,1)$. The image of (7) is thus in the simultaneous odd part for the equivariant map (8). The corresponding summand on the smooth product is precisely $\bigotimes_a V_a$. Finite pullback detects vanishing.

The connected monodromy of these systems is a product of diagonal $\mathrm{SL}_2$ groups on a partition $\mathcal P$ of the slots. Its Lie algebra surjects onto every $\mathfrak{sl}_2$, so the solvable radical maps to zero everywhere. Each simple coordinate quotient comes from just one simple ideal, giving the partition. Linked coordinates are isomorphic over $\mathbb Q$ because the intertwiner equations are rational. Passing to a finite étale cover for the component group and using §3.2 identifies the parts with the geometric generic isogeny classes. An odd part has zero invariants in its tensor by the central $-1$. In an even part the invariants are the span of pairwise contractions [16]. The vanishing criterion only needs the necessary condition that every part is even.

The moduli $j$-functions within a part are all algebraic over one representative by the modular equations. The coordinate base fields are finite over their respective $j$-fields, and together generate $\mathbb C(B)$. Therefore $b\le |\mathcal P|$. If the cross invariant summand is nonzero, all parts are even, so $|\mathcal P|\le m/2=b$. Thus every part is a pair, and the closed base $B$ is the product of the $b$ pair projections, each an integral curve. Indeed $B$ is an integral closed subvariety of this product of the same dimension. Now use the original, unextended presentations on a product of binary resolutions. The restriction is the external product of the binary restrictions. By §3.2 it has rank at most one and is nonzero exactly when all the individual isogeny lines descend and give nonzero projected graph pairings. Triviality of a product character on a correlated finite cover is insufficient: the original base here is the product of the pair curves. Any other resolution gives the same restriction kernels by injective pullback on a common smooth resolution. Pairings with all dimension-$m$ cycles of the given support factor through this restriction, by the multisection push-pull preceding §3.1.

## 4. Mixed primitive volumes

A very general polarized K3 has Picard rank one and $\operatorname{End}_{\rm Hdg}(T)=\mathbb Q$. Indeed on the primitive period quadric a fixed rational endomorphism preserving every period line is scalar. The extra Hodge endomorphism and divisor loci are countably many proper loci, by local Torelli and algebraicity of Hodge loci [17, 18]. Across independently very general polarized moduli, a nonzero cross Hodge Hom would be an isomorphism by simplicity. For each rational identification it would equate the two varying period lines, a proper Hodge locus in the product.

Zarhin [19] gives the connected Hodge group $\mathrm{SO}(T_i,q_{S_i})$ for each block. The joint group is their product. Otherwise its Lie algebra, a subdirect product of simple factors, would link two of the type-$B_{10}$ factors by a Lie algebra isomorphism. Over $\mathbb C$ such an identification is inner after identifying the orthogonal algebras, as the Dynkin diagram has no automorphisms. The standard representations would then admit a cross intertwiner. By the rational invariant equations this would give a rational Hodge homomorphism, a contradiction.

The multilinear invariants of a standard $\mathrm{SO}_{21}$ are generated by contractions with its metric and by the volume in $21$ variables [16]. In the generic mixed product there are independent such generators in each block. The metric is the primitive diagonal, an algebraic class, and the other Künneth generators are Tate. Thus for powers of these very general K3s, and mixed products made from them, all rational Hodge classes would be algebraic if the individual rank-$21$ volumes were algebraic. Conversely, the assertion for all their powers includes each volume. This is a statement about the algebraicity test for generic powers. For arbitrary K3 targets, including special endomorphism fields, the reduction in §2.4 still holds using their actual Hodge tensors. The invariant argument with the full orthogonal group would omit the odd volume. Varesco treats determinant and relative determinant issues for other endomorphism types in [20]. Buskin's algebraicity of rational Hodge isometries concerns binary classes [21].

Now let $Z$ be a dimension-$21k$ integral component with the nonzero pairing of §1. For any subset $I$ let $m_i$ be the number of selected slots from block $i$, let $B_I$ be the image in $C^I$, and let $A_I$ be the image in $X^I$. Grouping factors, $\Omega$ lies in the tensor product of the exterior subspaces for $I$ and its complement. This follows by grouping terms of the alternation, or by using the exterior coproduct in each block followed by the slot reordering. If (7) on the $I$-coordinates kills $\bigotimes_i\bigwedge^{m_i}T_i$, the pairing on $Z$ vanishes. Use a resolution of the image in the $I$-coordinates and a common dominating proper model of $Z$ to make every pullback in this assertion. A generically finite map of degree $d'$ multiplies the fundamental-class pairing by $d'$, so this argument detects the original integral pairing.

If $|I|>2\dim B_I$, §3.1 gives zero. If $|I|=2\dim B_I>0$, §3.3 gives zero or a single product of binary functionals. A cross-block matched pair has zero functional by (9). A within-block matched pair has a symmetric functional because the endomorphism ring is $\mathbb Q$, so it annihilates the prescribed alternation in that pair. Every matching therefore vanishes on the indicated exterior subspace. This proves
$$
\dim B_I\ge \lfloor |I|/2\rfloor+1.
\tag{11}
$$
In particular every pair is dominant, either by alternation within a block or by zero cross Hodge Hom. The total base dimension is at least $\lfloor 21k/2\rfloor+1$. For even $k$ this excludes the base dimension $21k/2$ despite the full tensor having even length. It also gives a strict bound for every even-cardinality selection of slots, such as the twenty-slot selections in a single block.

If $\dim A_I<|I|$, the restriction into degree $2|I|$ on its resolution is zero by dimension. At equality the restriction is into Tate top cohomology. For $0<m_i<21$, $\bigwedge^{m_i}T_i$ has no invariant under $\mathrm{SO}_{21}$. Over $\mathbb C$ a diagonal matrix changing the sign of one chosen and one unchosen basis vector negates the corresponding monomial without changing the determinant. Applying this in the separate factor of the product group shows there is no Tate quotient when any selected block is partial. The same factorization of the pairing proves $\dim A_I\ge |I|+1$ in that case. For a union of full blocks the dimension argument gives $\dim A_I\ge |I|$. This completes the support bounds for all nonzero pairing components. In particular, pushing the base images to the fixed line by the finite map $h$ preserves all those base dimensions.

## 5. Fields of definition of a contributing support

Let $Z\subset X^m$ be integral of dimension $m$ and pair nontrivially with a tensor of transcendental classes. Write $Z_0=q^m(Z)$, and $f_a:Z_0^\nu\to\mathbb P^1_r$ for the coordinate base maps on its normalization. Fix a slot $a$ for which $(f_a,f_j)$ is dominant for all $j\ne a$. The proof works for arbitrary rational tensors and for any fixed elliptic surface over $\overline{\mathbb Q}$ with geometrically integral generic fibre.

### 5.1 Intrinsic exceptions and the selected sheet

Write the Stein factorization as $f_a=d_a^{\rm St}\circ p_a$ with $p_a:Z_0^\nu\to D_a$ and $d_a^{\rm St}:D_a\to\mathbb P^1_r$ finite. The normal curve $D_a$ is smooth and complete. Define the finite exceptional set $\mathcal E_a\subset D_a$ by the following test. A point $v$ lies outside $\mathcal E_a$ if some prime divisor of $Z_0^\nu$ over $v$ has order one on a uniformizer at $v$ and maps dominantly under every $f_j$ for $j\ne a$. The use of divisors on this normalization makes the test intrinsic to $Z_0$. Allowing divisorial valuations on higher proper models can only decrease the exceptional set, and the valuation proof below works with that test as well.

Stein factorization gives a regular function field extension over $\mathbb C(D_a)$. The map is flat over the local DVRs, and its fibres are geometrically integral on an open. The image of each $(p_a,f_j)$ is the whole product because its further image under $d_a^{\rm St}\times 1$ has dimension two. Thus each integral fibre on that open witnesses the test and $\mathcal E_a$ is finite. Normalization, Stein factorization and the test commute with algebraically closed extension. If $Z_0$ is defined over an algebraically closed field containing $\overline{\mathbb Q}$, the normalization and Stein factor descend, and the exceptions are rational over that field. Indeed the valuation condition commutes with algebraically closed extension, and the exceptions lie in the finite complement of an integral-fibre open defined over that field.

On the product open where the covers are étale, the fibres smooth, and graph modifications avoided, the preimage of $Z_0$ is a pullback of the finite étale $G_r^m$-torsor. Every slot meets this open, since constant base slots give zero by §3.1. Equality of dimensions makes $Z$ the closure of one component. For $L_0=\mathbb C(Z_0)$ and $M_Z=\mathbb C(Z)$ the extension $M_Z/L_0$ is Galois with group $H_Z\subset G_r^m$, the stabilizer of that component.

Inside $M_Z$ write $E^{(a)}$ for the chosen copy of $\mathbb C(C)$ and $L_a=\mathbb C(D_a)$. Put $E'_a=E^{(a)}L_a$, defining the selected component $C'_a$ of the normalized Stein pullback. Restriction identifies $G_a=\operatorname{Gal}(E'_a/L_a)$ with $\operatorname{Gal}(E^{(a)}/(E^{(a)}\cap L_a))\subset G_r$. The extension $L_0/L_a$ is regular, so $E'_a$ and $L_0$ are linearly disjoint over $L_a$ and the coordinate projection of $H_Z$ is $G_a$.

### 5.2 Isolated inertia and the fixed-line quotient

At $v\notin\mathcal E_a$ choose a witnessing divisor $w$. A local branch of $C'_a/D_a$ of index $e$ has field $\mathbb C((t_v^{1/e}))$. The polynomial $x^e-t_v$ stays Eisenstein at the completion at $w$ because $t_v$ has order one. The extensions from other slots are unramified there, since their residue maps to the line are generic. Their compositum leaves the full cyclic inertia in slot $a$ and is fixed by it. Hence inertia above $w$ in $M_Z/L_0$ isolates the inertia in slot $a$. Conjugation by $H_Z$ gives all $G_a$-conjugates.

Let $N_a\lhd G_a$ be generated by the inertia groups outside $\mathcal E_a$. The isolated copies give
$$
1\times\cdots\times N_a\times\cdots\times 1\subset H_Z .
\tag{12}
$$
Put $\mathcal B_a=\mathcal E_a\cap\operatorname{Br}(C'_a/D_a)$. The quotient $Q_a=C'_a/N_a\to D_a$ has branch contained in $\mathcal B_a$, whose images downstairs are branch values of $h$. Over an algebraically closed field of definition of the marked finite map $(D_a\to\mathbb P^1_r,\mathcal B_a)$, the map $Q_a\to D_a$ descends by invariance of finite étale covers of the complement of the marks [22], then normalization.

For a bound on the fixed line itself, use the intermediate cover $V_a^{\rm cur}=C/N_a$, which need not be Galois over that line. The function field identity
$$
\mathbb C(Q_a)=(E'_a)^{N_a}
             =L_a\cdot (E^{(a)})^{N_a}
\tag{13}
$$
follows because the subgroup fixing the compositum on the right restricts to exactly $N_a$. Both maps from $Q_a$ to the base curves of the compositum are finite surjections. If $V_a^{\rm cur}$ ramifies over $r_0$ where $d_a^{\rm St}$ is unramified, any point of $Q_a$ above that ramified point is ramified over $D_a$ by the tower formula. Since $V_a^{\rm cur}$ is intermediate in $h$, we get
$$
\operatorname{Br}(V_a^{\rm cur}/\mathbb P^1_r)
 \subset d_a^{\rm St}(\mathcal B_a)
     \cup\bigl(\operatorname{Br}(d_a^{\rm St})\cap \operatorname{Br}(h)\bigr).
\tag{14}
$$
On compatible completed branches of indices $e_V,e_D$ over $r_0$, the index of the normalized compositum over $D_a$ is $e_V/\gcd(e_V,e_D)$ by the tame completed fields. This accounts for ramification that disappears after Stein pullback. The intermediate cover descends over the algebraic closure of the field generated by the right side of (14), or by its own branch set, by the same étale descent argument.

### 5.3 Quotient graphs and polarized moduli

Every member of $N_a$ in slot $a$ acts by an automorphism of the proper $Z$ on the regular model of §2.3. Changing variables and averaging the pairing termwise shows that $e_{N_a}F_{i(a)}^*|_{T(S_{i(a)})}\ne0$, for the normalized average $e_{N_a}$. Let $U_a$ be a smooth projective model of $X/N_a$, with resolved quotient graph $X\xleftarrow{\mu}W\xrightarrow{\eta}U_a$. On $T(X)$,
$$
\mu_*\eta^*\eta_*\mu^*=\sum_{\gamma\in N_a}\gamma^* .
\tag{15}
$$
On the finite étale open the proper graph composition is the sum of deck graphs. By localization the compact difference has curve support in at least one factor. Input curve support pairs to zero on $T(X)$ by restriction to the normalized curve. Output curve support gives an algebraic image in degree two, hence zero on $T(X)$, which has no Tate quotient. This proves (15). Thus the proper correspondence $\eta_*\mu^*F_{i(a)}^*$ is nonzero and injective by simplicity, with image in $T(U_a)$.

The quotient $U_a$ is birational to the base change along $V_a^{\rm cur}$. Use a smooth projective model over the field from (14) and transport the injection by the birational graph. For the field of the marked Stein map instead base change by $Q_a$. Its dominant generically finite map to $U_a$ gives an injective resolved pullback on $T(U_a)$ by degree push-pull and orthogonality to the birational exceptional divisors. In either case the injection into a fixed surface is an algebraic correspondence over $\mathbb C$.

Suppose a polarized $S$ admits such an injection into $H^2(V,\mathbb Q)$ with $V$ smooth projective over an algebraically closed $K$. In Picard rank one the domain is the primitive variation. On finite type polarized moduli charts over $K$ parametrize the cycle components by relative Hilbert schemes for the universal family times $V$, with their Hilbert polynomials and rational coefficients fixed [23]. The incidence contains the original complex point. On the smooth connected stratum through that point, the relative cycle classes of the flat universal subschemes give a flat Hodge map from the primitive variation to constant $H^2(V,\mathbb Q)$. It has constant rank, so its image is a constant subsystem and its Hodge filtration is the intersection with the constant filtration by strictness. The marked periods are therefore constant. Polarized local Torelli [17] makes the moduli map locally constant. The stratum and its connected components are defined over $K$, and the constructible one-point image is $K$-rational. In higher Picard rank include divisors for a basis in the Hilbert incidence. Their span is flat, nondegenerate and of type $(1,1)$, so its orthogonal complement is the domain of the same argument and carries the whole period line. A multiple of a primitive polarization is recovered by its fixed multiplicity.

### 5.4 Simultaneous rationality and quantitative bounds

If $Z_0$ is defined over algebraically closed $K\supset\overline{\mathbb Q}$, the finite marks $\mathcal B_a\subset\mathcal E_a$ are $K$-rational, even if the cover and lift were given over a different field. Apply the marked-map argument in each slot to the same contributing component. This recovers the ordered tuple over the same $K$. For an arbitrary field of definition take its algebraic closure after adjoining $\overline{\mathbb Q}$, preserving transcendence degree. Very generality in the $19k$-dimensional product gives the claimed bound.

For trivial Stein factor, the associated moduli point is algebraic over $\overline{\mathbb Q}(\mathcal B_a)$, so $\mathcal B_a$ contains $19$ algebraically independent $r$-values in the very general case. For general Stein factor the union in (14) gives the analogous parameter bound, with both sets consisting of branch values of $h$. Taking the union for any choice of one slot from every block gives a simultaneous field and hence at least $19k$ independent values.

For the given Galois tower, independently of any cycle, the branch set of $C\to\mathbb P^1_j$ outside $J_{\rm fix}=\{\infty,0,1728,\lambda_*\}$ generates a field of definition up to algebraic extension of that map. Over the étale open the intermediate $r$-map descends with it as a morphism of finite étale covers, and then extends by normalization. The graph injections and the fixed-target argument show that at least $19k$ independent branch values outside $J_{\rm fix}$ are needed. Each has twelve distinct $r$-preimages, all branch values of $h$ by the tower formula. Thus at least $228k$ distinct such $r$-values occur in the given cover, with twelve algebraic over each $j$-value. This count concerns the common cover as a whole.

Diaz defines the field of definition of a Chow class modulo $\ell^r$ as the fixed field of its absolute Galois stabilizer [24, Def. 4.1]. For primitive codimension-two cycles on products of very general abelian varieties, Proposition 4.7 detects a change in the projected Abel–Jacobi class over congruence fields under the stated hypotheses. Corollary 4.14 gives ramification over the modular base for large $r$, and §5 applies the resulting isogeny argument to products of very general elliptic curves. In our setting a field of definition is a field over which the reduced image $Z_0\subset X_*^m$ is defined as a closed subvariety. The stabilizer in §5.1 fixes one lifted component. Its inertia gives a quotient cover that recovers the polarized K3 moduli over an algebraic extension of the field of the reduced support, even after forgetting the physical cover.

## 6. Compact calibrations

### 6.1 Degree-two Hecke supports and their zeros

Use (2), with coefficients $a_0=-2M$, $b_0=K$. The quotient of $E_*$ by $(0,0)$ is $E_2:y'^2=x'(x'^2+a_2x'+b_2)$ with $a_2=-2a_0=4M$ and $b_2=a_0^2-4b_0=16N$. In a compatible differential convention the quotient and dual are
$$
\begin{split}
\varphi(x,y)&=(x+a_0+b_0/x,\ y(1-b_0/x^2)),\\
\widehat\varphi(x',y')&=((x'+a_2+b_2/x')/4,\ y'(1-b_2/x'^2)/8).
\end{split}
\tag{16}
$$
The quotient pulls $dx'/y'$ back to $dx/y$, and the dual pulls $dx/y$ back to $2dx'/y'$. The composition has kernel $E_*[2]$ and differential multiplier $2$, so it is $[2]$. The minimal discriminant of $E_2$ has cusp widths $(2,2,4,2,2)$ at $(0,\infty,1,4,1/4)$, with $c_4$ a unit there. The coarse parameters are distinct rational functions and satisfy the level-two modular equation. This is a genuine Hecke support away from the equal-$j$ locus.

For any evaluation $F:X\to S$ of degree $d$ from the fixed pencil base change, take the $E_2$ family over the same complete base, with second evaluation $F_2=F\circ\widehat\varphi$ resolved as a morphism. It has degree $2d$. If both families are to be based on the fixed pencil, pull the quotient family back over a component of $j_*(s)=j(E_2(r))$ and then make a pointed Isom marking. Make the same base change at the source and use $d$ for the resulting degree. Close the graph of $\varphi$ over the diagonal of these complete base curves. Resolving the graph and pushing by the two evaluations gives the proper surface correspondence
$$
(F\circ[2])_*F^*=2d\,\mathrm{id}_{T(S)} .
\tag{17}
$$
Indeed the map $[m]$ pulls a holomorphic two-form back to $m$ times itself by the relative differential formula. It does the same on $F^*T(S)$ by simplicity. Its degree on the elliptic surface is $m^2$, so pushforward on that subspace is also multiplication by $m$, by degree push-pull. The resolved graphs realize this calculation in ordinary cohomology, with curve-supported corrections vanishing on the transcendental part. Using $-\varphi$ gives $-2d\,\mathrm{id}$ with the same evaluation degrees. Their difference gives $4d\,\mathrm{id}$. Equivalently, the individual graph pairings with the inverse intersection tensor on a rank-$21$ $T(S)$ are $+42d$ and $-42d$.

For a non-Hecke control with the same target at both ends, use any dominating component of the inverse image of $s=2r$ in the product of two complete fixed-pencil bases. Above $r=1$ the first local system has nontrivial $I_2$ unipotent monodromy, while the second is smooth at $s=2$. No finite ramification can turn a nontrivial unipotent transvection into the identity. Hence there is no geometric generic isogeny on this component. Every projected binary Chow class and the entire transcendental restriction vanish by §3.2.

For two level-two supports with different descent, take $S_1$ to be the pullback of $E_*$ by $t^2=\delta(r)=(r-2)/(r-3)$ and $S_2$ the twist $E_2^{\delta(s)}$. These minimal models are K3s by the canonical bundle formula over $\mathbb P^1$ with a section and $\chi=2$. The first has discriminant degree $24$ by base change, and the second adds two $I_0^*$ to the multiplicative fibres of $E_2$ [6]. Over $s=r(t)$ the twist splits and (16) gives a map $P_+:S_1\dashrightarrow S_2$ of degree four. Its proper graph gives $P_{+*}P_+^*=4$ on $T(S_2)$, and $P_{+*}/2$ is a rational Hodge isometry by simplicity and degree push-pull. Over $s=1/r(t)$ the untwisted quotient models agree by reciprocal scaling of $a_2,b_2$ by $r^{-2},r^{-4}$. But the twist has odd valuation above $r=1/2,1/3$, where the source double cover is unramified. Hence the descent sign is nontrivial and the Chow trace vanishes, still at geometric level two. Products of the positive graphs realize rank one at $m=2b$.

### 6.2 Different fields and a return with independent base projections

In the equal-$j$ case set $H_i=\operatorname{Gal}(L/K_i)$, and let $\epsilon_i$ be the sign of its pointed isomorphism relative to $A^j$. The image of $J_i$ and its adjoint retraction $L_i$ factor through $e_i=|H_i|^{-1}\sum_{\gamma\in H_i}\epsilon_i(\gamma)\gamma$, by the inversion sign. Matching components are indexed by $H_j\backslash G^j/H_i$. The normalized graph $d_j^{-1}\pi_j(F_i,F_j D_g)_*[X]\pi_i$ acts by $L_jD_{g*}J_i$. It is the push of the fibre isomorphism graph, and compresses by $e_jge_i$. Its signed average vanishes when the characters disagree on $H_j\cap gH_i g^{-1}$, by pairing cancelling terms. Otherwise the coefficient at $g$ is $|H_j\cap gH_i g^{-1}|/(|H_i||H_j|)$, and evaluation on the physical images decides nonvanishing. Section 3.2 gives exhaustion on that support.

If the splitting fields $L^{\ker\epsilon_i},L^{\ker\epsilon_j}$ are linearly disjoint over $\mathbb C(j)$, their subgroup product is all of $G^j$, with normalized product average equal to the group average. It kills $T(X)$ by (15), since the quotient is the rational elliptic surface of $A^j$ with fibres $II,III^*,I_1$ [6]. Thus all equal-$j$ transfers vanish in this situation. Disjointness before splitting need not give the same averaging identity.

Independent sweeps on the same K3 $S$ give an ordinary interaction. Let $F_1,F_2$ have degrees $d_1,d_2$ and distinct relative tangent lines at a general common physical point on the finite étale locus. Take the closure $D$ of the fibre product over that locus with all its fundamental components. The actual generic point count gives
$$
(F_1,F_2)_*D=d_1d_2\,\Delta_S,\qquad
\langle D,F_1^*t\otimes F_2^*t'\rangle=d_1d_2\,q_S(t,t').
\tag{18}
$$
Degrees of the components sum to $d_1d_2$. The two base maps are locally independent by the tangent criterion. Finite markings preserve dominance. The support uses physical equality on $S$, with both coarse elliptic parameters free to vary. Its nonzero pairing is compatible with vanishing of all transfers over equal $j$ when that disjointness test applies.

For an explicit example use $S=Y_b$, the minimal K3 model of $s^2=r/(r-b)$ above $X_*$, with $b$ transcendental. It is semistable with $\chi=2$, base $\mathbb P^1_s$, and section, hence a K3. The $r$-cover gives one elliptic fibration. Projection to $u$ gives another: its generic fibre is a double cover of the $v$-line branched at $v=\pm2$ and the two solutions to $a(v)=a(u)/b$. These points are generically distinct, and $v=2$ supplies an origin. Put $z=a(u)$ and $x=(v+2)/(v-2)$. This second elliptic curve is a twist of $y^2=x(x^2+A_bx+1)$ with $A_b=(10b-16z)/(3b)$. Its $j$ varies with $u$, as does the original $j$ with $s$. The functions $u,r$ are algebraically independent because $r=a(u)/a(v)$ and $a(v)$ is nonconstant. Hence $u,s$ are independent as well. The two identity evaluations have $d_1=d_2=1$ in (18). Over the independent base pair $(s,u)$ the diagonal incidence itself has generic projection degree two: fixed $s,u$ give $r$ and a generic equation $a(v)=a(u)/r$ of degree two. After separate markings or a common Galois cover the degree in the push to the physical diagonal remains exactly the product of the evaluation degrees, as in (18).

This example has an actual stable nodal fibre in the first sweep. Above $r=4$ the cover is unramified and the fibre remains an irreducible $I_1$, a stable genus-one map by inclusion in $S$. Locally a transverse base parameter gives $xy=t$. In the second sweep $u$ is nonconstant along this fibre: the equation there is $v^2=-12/(3u^2-15)$ on a dense open. Thus the diagonal incidence reaches this nodal boundary and for general $u$ there the two intersection points in the fibre are counted with their proper degree two. Formula (18) is on the compact cycle. Individual terms supported over a fixed base point, including normalized branches of stable degenerate fibres or extra graph components, have zero all-transcendental pairing by §3.1. Degree on a complete fibre detects this even when its normalizations are rational. The generic nonzero pairing is therefore compatible with the singular compact boundary.

### 6.3 An essential moving branch in an ordinary graph

On the same $Y_b$ let $m_2$ be doubling on the $u$-fibration. Its deck involution in the $r$-base change is fibre inversion for the $u$-fibration, so $m_2$ commutes with it and descends to a rational map on $X_*$. Take the compact graph of $m_2$ and its image $Z_0$ on $X_*^2$. The first projection identifies the function field of $Z_0$ with that of $X_*$, so its first coordinate Stein factor is the $r$-line. To verify pair dominance, set $t=r$ and compute
$$
x'=\frac{(x^2-1)^2}{4x(x^2+A_bx+1)}
   =\frac{b(4z-t)(z-t)}{3zt(b-t)},\qquad
r'=\frac{16zx'}{3(x')^2+10x'+3}.
$$
The expression for $r'$ vanishes at $z=t,t/4$ for generic $t$ and is nonzero as a rational function of $z$. Thus $(r,r')$ is dominant. On the graph the two square roots $s,s'$ have the same deck sign, giving
$$
\frac{r'/(r'-b)}{r/(r-b)}\in\mathbb C(Z_0)^{\times 2}.
\tag{19}
$$
A divisor with order one at $r=b$ cannot have generic $r'$ there, by the parity in (19). Thus $b$ is an intrinsic exceptional branch value, even if the valuation test is made on higher models. The lifted component has generic degree two over $Z_0$ and stabilizer the diagonal order-two subgroup. Doubling acts by $2$ on $T(Y_b)$ using the same proper differential calculation as in (17). Its graph has nonzero symmetric pairing. This example explains why an essential branch can occur even when the generic base pair is dominant, and why the field of the chosen lift cannot be silently identified with that of its image.

The polarized moduli of $Y_b$ have transcendence degree exactly one for any ample polarization chosen over $\overline{\mathbb Q}(b)^{\rm alg}$. Over an algebraically closed field of definition of the polarized K3, the line bundle of its original elliptic fibre descends, since the Picard scheme of a K3 is discrete and its geometric line bundle classes are unchanged by algebraically closed extension. Its pencil and the critical values of its $j$-function then descend. These include $j_*(b)$, which implies that $b$ is algebraic over any such field. This is a compact field calibration with extra Picard classes. Equations (17)–(19) realize symmetric metric interactions and an essential parameter in ordinary cohomology. The alternating rank-$21$ line remains the open algebraicity test of §4, and the support and field bounds are necessary conditions for its realization.

## Reproduction

The portable supplement contains exact polynomial and finite group CPU checks, with separate scripts for the fixed pencil, the support calculations, the compact doubling graph, and the mixed projection and inertia controls. In an extracted directory run the commands in its README. The checks use small tensor blocks and compact symbolic expressions. The general geometric, Hodge-theoretic and field statements are proved in the text.

## References

[1] Xi Chen and Frank Gounelas. *Curves of maximal moduli on K3 surfaces*. Forum of Mathematics, Sigma 10 (2022), e36, Theorem A. https://doi.org/10.1017/fms.2022.24

[2] Xi Chen. *Rational curves on K3 surfaces*. Journal of Algebraic Geometry 8 (1999), 245–278, Theorem 1.2. https://arxiv.org/abs/math/9804075

[3] William Fulton. *Intersection Theory*. 2nd ed., Springer, 1998, §§1.8, 2.3, 6. https://doi.org/10.1007/978-1-4612-1700-8

[4] Bruno Kahn, Jacob P. Murre and Claudio Pedrini. *On the transcendental part of the motive of a surface*. In *Algebraic Cycles and Motives*, vol. 2, Cambridge University Press, 2007, 143–202. https://doi.org/10.1017/CBO9781107325968.009

[5] Bernard Saint-Donat. *Projective models of K-3 surfaces*. American Journal of Mathematics 96 (1974), 602–639. https://doi.org/10.2307/2373701

[6] Matthias Schütt and Tetsuji Shioda. *Elliptic surfaces*. In *Algebraic Geometry in East Asia, Seoul 2008*, Advanced Studies in Pure Mathematics 60 (2010), 51–160. https://arxiv.org/abs/0907.0298

[7] Edward Bierstone and Pierre D. Milman. *Canonical desingularization in characteristic zero by blowing up the maximum strata of a local invariant*. Inventiones Mathematicae 128 (1997), 207–302. https://arxiv.org/abs/alg-geom/9508005

[8] Steven Zucker. *Hodge theory with degenerating coefficients: $L_2$ cohomology in the Poincaré metric*. Annals of Mathematics 109 (1979), 415–476. https://doi.org/10.2307/1971221

[9] Charles F. Doran and Jordan Kostiuk. *Geometric variations of local systems and elliptic surfaces*. https://arxiv.org/abs/1911.00402

[10] Anthony J. Scholl. *Motives for modular forms*. Inventiones Mathematicae 100 (1990), 419–430. https://doi.org/10.1007/BF01231194

[11] Birger Iversen. *Cohomology of Sheaves*. Springer, 1986, Chs. III and VII. https://doi.org/10.1007/978-3-642-82783-9

[12] Fred Diamond and Jerry Shurman. *A First Course in Modular Forms*. Springer, 2005, §§1.3–1.5, 1.7. https://doi.org/10.1007/978-0-387-27226-9

[13] Pierre Deligne. *Théorie de Hodge II*. Publications Mathématiques de l'IHÉS 40 (1971), 5–57, Theorem 4.1.1 and Corollary 4.1.2. https://doi.org/10.1007/BF02684692

[14] Christina Birkenhake and Herbert Lange. *Complex Abelian Varieties*. 2nd ed., Springer, 2004, §§1.2, 2.5. https://doi.org/10.1007/978-3-662-06307-1

[15] Claire Voisin. *Hodge Theory and Complex Algebraic Geometry I*. Cambridge University Press, 2002, §7.2. https://doi.org/10.1017/CBO9780511615344

[16] Hermann Weyl. *The Classical Groups: Their Invariants and Representations*. 2nd ed., Princeton University Press, 1946, Ch. II. https://press.princeton.edu/books/paperback/9780691057569/the-classical-groups

[17] Daniel Huybrechts. *Lectures on K3 Surfaces*. Cambridge University Press, 2016, Chs. 5–6 and 11. https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf

[18] Eduardo Cattani, Pierre Deligne and Aroldo Kaplan. *On the locus of Hodge classes*. Journal of the American Mathematical Society 8 (1995), 483–506. https://arxiv.org/abs/alg-geom/9402009

[19] Yuri G. Zarhin. *Hodge groups of K3 surfaces*. Journal für die reine und angewandte Mathematik 341 (1983), 193–220, Theorem 1.5.1. https://doi.org/10.1515/crll.1983.341.193

[20] Mauro Varesco. *The Hodge conjecture for powers of K3 surfaces of Picard number 16*. Michigan Mathematical Journal 75 (2025), 1085–1116. https://arxiv.org/abs/2203.09778

[21] Nikolay Buskin. *Every rational Hodge isometry between two K3 surfaces is algebraic*. Journal für die reine und angewandte Mathematik 755 (2019), 127–150. https://arxiv.org/abs/1510.02852

[22] Alexander Grothendieck and Michèle Raynaud. *Revêtements étales et groupe fondamental (SGA 1)*. Exp. XIII, Cor. 2.12. https://arxiv.org/abs/math/0206203

[23] Alexander Grothendieck. *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert*. Séminaire Bourbaki 6 (1960–61), Exp. 221, 249–276. https://www.numdam.org/item/SB_1960-1961__6__249_0/

[24] Humberto A. Diaz. *Nondivisible cycles on products of very general abelian varieties*. Journal of Algebraic Geometry. Definition 4.1, Proposition 4.7, Corollary 4.14 and §5. https://doi.org/10.1090/jag/775

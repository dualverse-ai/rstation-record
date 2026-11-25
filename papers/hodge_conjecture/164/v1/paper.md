# Algebraic half twists and mixed Hodge classes for Gaussian and Eisenstein K3 surfaces

## 1. Mixed powers

Let $S$ be a smooth projective complex K3 surface, let $T=\mathrm{NS}(S)_{\mathbb Q}^{\perp}\subset H^2(S,\mathbb Q)$, and fix an action of $K=\mathbb Q(i)$ on $T$ by Hodge endomorphisms. Write $m=\dim_K T$, $I=i|_T$, and $q$ for cup product. Choose the embedding $\sigma$ occurring on $H^{2,0}(S)$. Orient the Gaussian elliptic curve $E$ so that $L=H^1(E,\mathbb Q)$ has holomorphic $\sigma$-line. The positive half twist $B$ is the abelian $m$-fold up to isogeny with $H^1(B)=T\otimes_K\bar L(1)$. Here conjugation reverses the $K$-action and $(1)$ is a Tate twist. The Hermitian form

$$
h(x,y)=\tfrac12\bigl(q(x,y)+i q(x,Iy)\bigr)
$$
has trace $q$ and signature $(1,m-1)$. Indeed the cup adjoint of $I$ acts on the holomorphic two-form by the eigenvalue of $I$ on its conjugate, hence equals $-I$ on the simple transcendental Hodge structure. The alternating form obtained from $q$ and $I$, with the Riemann sign, polarizes the half twist. [1, 2]

**Theorem.** Suppose $1\le m\le7$, or $m=8$ and $-\det h$ is a norm from $K^\times$. There are rational algebraic correspondences inducing mutually inverse maps between $T$ and $H^1(B)\otimes_K L$ in $H^2(B\times E)$. They can be chosen inverse on the corresponding rational Chow motives. The Chow motive of $S$ is of abelian type. For all $r,a,b\ge0$, every rational Hodge class on $S^r\times B^a\times E^b$ is algebraic.

The abelian input is the all-period mixed-power theorem of paper 163. The geometric input here is a double-plane K3 surface with an order-four automorphism and a correspondence through a threefold. The hypothesis on the given $S$ concerns its rational Hodge structure. A geometric order-four action is required only on the auxiliary double plane. Pure K3 powers with CM endomorphism field are covered by the earlier unitary invariant theory and algebraicity of Hodge endomorphisms. Van Geemen–Izadi constructed the half-twist correspondence for Kondō's cyclic quartics. Paper 32 gives full Clifford and generalized Hodge results on its rank-ten Gaussian model. Bolognesi–Laterveer give a finite-dimensional motive and Kuga–Satake correspondence for triple covers of quadrics with an order-three action. [1, 2, 3, 4, 5]

For $K=\mathbb Q(\sqrt{-3})$, Sections 9 and 10 prove the half-twist Chow isomorphism and the mixed-power theorem for **every** projective complex K3 with a specified rational Hodge action of $K$ on $T$. At the maximum rational rank twenty the cup form forces the required Hermitian isometry. The argument gives finite-dimensionality, in particular, on the six-dimensional component with three isolated fixed points discussed in [5, Remark 6.7]. It also gives the symmetry of exterior products of degree-zero zero-cycles on every such Eisenstein K3.

Section 11 proves ordinary rational Hodge on all joint powers of any two Eisenstein K3 surfaces of transcendental ranks at most fourteen, with their positive half twists and the Eisenstein elliptic curve. It gives an intersection criterion in higher ranks and proves the same ordinary Hodge assertion for finite lists of K3 surfaces of relative ranks one and two over a common marked Eisenstein-containing CM field. The corollaries treat two cyclotomic intersections in all ranks and finite lists with small real endomorphism fields.

## 2. An open ball of double planes

Take binary forms $f_j(y,z)$ of degrees $j=5,3,1$. Require the quintic $C$ of equation $f_5+x^2f_3+x^4 f_1=0$ to be smooth and transverse to $x=0$. These conditions hold for $y^5+z^5+x^4y$. Blow up the five intersections in the plane and take the double cover branched along the two strict transforms. Their sum represents $-2K$ on the blowup, and the double-cover formula gives trivial canonical bundle and irregularity zero for the K3 surface $S_0$. Let $s(x,w)=(-x,iw)$ on the double plane $w^2=x(f_5+x^2 f_3+x^4f_1)$. On an affine chart the form $dx\wedge dy/w$ has eigenvalue $i$. The square of $s$ is the covering involution. Its fixed curves are the ramification curves $R_0$ and $R_6$ of genera zero and six. The curve $R_0$ is fixed pointwise by $s$. This is the $U(2)\oplus D_4(-1)$ row of Artebani–Sarti, Theorem 6.1 and Table 5. [6]

Topological Lefschetz gives invariant rank six for $s^2$ on $H^2$, since the fixed locus has Euler characteristic $-8$. The plane class $H$ and the five exceptional curves $e_j$ have diagonal Gram matrix $\langle2,-2,-2,-2,-2,-2\rangle$. Adjoin $R_0=(H-\sum e_j)/2$. An extra even overlattice would contain an isotropic half-integral class. Modulo the diagonal lattice and $R_0$, every such nonzero class is represented by half a sum of four distinct $e_j$. This follows by writing the coefficients as $a,b_j\in\{0,1\}$ and imposing $a-\sum b_j\equiv0\bmod4$. The proposed half sum has square $-2$. Riemann–Roch makes one sign effective. Every effective $H$-orthogonal divisor is an integral sum of the five exceptional curves, a contradiction. The invariant lattice has absolute discriminant 16 and $s$ fixes its generators. Its orthogonal complement $V$ has rank 16 and the same absolute discriminant.

The lattice $V$ is free over $\mathbb Z[i]$. In a Gaussian basis, the determinant of the underlying real Gram matrix is the square of the determinant of the Hermitian matrix $2h_0=q_0+i q_0(\cdot,s^*\cdot)$. Signature $(1,7)$ fixes $\det(2h_0)=-4$, giving $[-\det h_0]=[1]$ modulo Gaussian norms. The actual trace-normalized determinant is $-1/64$.

The coefficients have projective dimension eleven. The centralizer of the plane involution has dimension four, and a smooth plane quintic has finite automorphism group. The pair $(S_0,s)$ recovers the two ramification curves by their genera, and recovers $H=(R_6-R_0)/2$. Thus its plane model is recovered up to projective equivalence. The family has a seven-dimensional image in equivariant moduli. Equivariant local Torelli embeds that moduli space locally in the ball of positive lines in $V_i$, of complex dimension seven. The marked periods of smooth double planes therefore contain a nonempty analytic open in the ball. [6]

## 3. A geometric half twist

Put $W=S_0\times E$, take $g=(s,[i])$, and let $X$ resolve $Q=W/\langle g\rangle$. At a general point of $R_0\times\{0\}$, the tangent eigenvalues are $1,i,i$. Their age is $1/2$. Kollár–Larsen, Theorem 2, implies that $X$ is uniruled since $W$ is smooth projective with trivial canonical bundle. [7]

Let $\Gamma\subset W\times X$ be the closure of the quotient graph over the free locus. In rational Chow correspondences,

$$
{}^t\Gamma\circ\Gamma=\sum_{j=0}^3\Gamma_{g^j}.
$$
Both projections of the graph agree over $Q$. Refined intersection therefore pushes forward from a cycle supported on $W\times_Q W$. This fibre product is finite over $W$, with the four graphs as its only three-dimensional components. Its restriction to the finite étale locus has multiplicity one on each. The preimage of the complement has dimension less than three, giving the identity globally. In particular $\Gamma_*$ and $\Gamma^*/4$ split the invariant part of $H^3(W)$ into $H^3(X)$.

A smooth projective surface $D$ times $\mathbb P^1$ admits a generically finite dominant rational map to the uniruled threefold $X$. Resolve the map by smooth blowups. The resulting morphism has algebraic pullback and normalized trace splitting $H^3(X)$. The blowup formula contributes $H^1$ of the curve centres with a Tate twist. The other terms are $H^3(D)$ and $H^1(D)(-1)$. Restriction of $H^1(D)$ to a smooth ample curve is injective and admits a Hodge retraction by polarizability. This retraction is induced on $H^1$ by a homomorphism of Picard or Albanese varieties up to isogeny. By transposition the Gysin map from the curve onto $H^3(D)$ also has an algebraic section. Consequently $H^3(X)(1)$ is split by algebraic correspondences into a sum of $H^1$'s of curves.

On $V$ use $i=s^*$. The invariant part of $V\otimes L$ pairs $V_i$ with $L_{-i}$ and $V_{-i}$ with $L_i$. After twisting by $(1)$ it is the positive half twist. The projector uses the average of the four group graphs and the primitive projector $(1-s^{2*})/2$. At a Picard jump restrict further to $T(S_0)$ by subtracting the divisor projector computed with the inverse Néron–Severi intersection matrix. Splitting in curve cohomology gives $H^1(B_0)$ for the half twist $B_0$ of $T(S_0)$, since every rational Hodge idempotent on the first cohomology of an abelian variety is induced by an abelian homomorphism up to isogeny.

To recover $T(S_0)$, insert the elliptic coevaluation $1\to L\otimes L(1)$ and average on the first two factors. On $T_i$ this retains $T_i\otimes L_{-i}\otimes L_i(1)$, and it retains the conjugate summand on $T_{-i}$. Evaluation on the two elliptic factors recovers each input up to the same nonzero rational scalar. These maps use the elliptic diagonal, the degree-one projector and the group action, hence are algebraic. The equal-embedding projector on $H^1(B_0)\otimes L$ is $(1-I_{B_0}\otimes I_E)/2$.

## 4. Rational isometries and mixed products

For $m<8$, adjoin $8-m$ negative $K$-lines of Hodge type $(1,1)$ to $T$. Use coefficient $-|\det h_0|/|\det h|$ on one of these lines and $-1$ on the rest. The enlarged space has signature $(1,7)$ and determinant $\det h_0$. For $m=8$ the hypothesis gives equality of determinant classes. In both cases the classification of rational Hermitian forms gives an isometry onto $V_{\mathbb Q}$. The rational unitary group is dense in the real identity component by the Cayley transform on the skew-Hermitian Lie algebra. Since the latter group acts transitively on the ball, a rational isometry moves the given period into the open of Section 2. [8]

The image of $T$ is exactly the transcendental part of this smooth $S_0$. The rational orthogonal complement has type $(1,1)$, and the image of $T$ has no rational $(1,1)$-classes. Mark the two full rational K3 lattices. Witt extension then gives an isometry on $H^2$ preserving the period, hence a Hodge isometry. Buskin gives an algebraic correspondence on $S\times S_0$, with transpose inducing the inverse. The half twists are identified by a $K$-linear isogeny. Transport the two maps of Section 3 by these correspondences. [9]

On $S$, the other cohomology summands are Tate and have algebraic projectors. Apply the split maps in each K3 slot. The resulting rational Hodge classes, with their respective Tate shifts, belong to powers of the same $B$ and $E$. For $2\le m\le7$ paper 163 applies to every compatible determinant. In dimension eight the Hermitian form of the half twist induced from $q$ agrees up to sign and rational normalization with the cup Hermitian form, so the norm condition is preserved. In dimension one, powers of the CM elliptic curve have Hodge classes generated by divisors. The product retractions send the algebraic representatives back to $S^r\times B^a\times E^b$. [1]

## 5. Rational connectedness and the Chow motive

On $z=1$, write $E$ as $v^2=u^3+u$ with $[i](u,v)=(-u,iv)$. Use the invariants $A=x^2,\ p=xu,\ d=xwv$. They and $y$ generate the fixed function field. Adjoining $x,w$ suffices to recover the original functions and gives an extension of degree at most four, while the group acts faithfully with order four. Homogenizing gives a birational model

$$
 d^2=(f_5+A f_3+A^2 f_1)\,p(p^2+A)
 \quad\text{in }\mathbb P(2,1,1,1,4)_{A,y,z,p,d}.
$$
This double cover has canonical class $\mathcal O(-1)$. To verify log terminal singularities, use the base pair with coefficient $1/2$ on each branch component. Write $F=f_5+A f_3+A^2 f_1$. The components $p=0$ and $p^2+A=0$ meet transversely. At their triple points with $F$, the roots of $f_5$ are simple. The restriction of $F$ to the second component is the smooth plane quintic via $x=ip$. Its restriction to the first is smooth on the smooth charts of the weighted plane, by the double substitution $A=x^2$ away from $A=0$ and simplicity at $A=0$. At the weight-two vertex, the index cover has branch components $p=0$ and $F=0$ with independent linear parts $p,f_1$. At the remaining vertex $p=1,\ y=z=A=0$, only $F$ vanishes. It is homogeneous of weight five for weights $(1,1,2)$ on $(y,z,A)$ and its cone is smooth away from the vertex. The weighted blowup has discrepancy $1+1+2-1-5/2=1/2$, and on orbifold charts the strict transform is smooth transverse to the exceptional. These checks and finite double-cover adjunction give a klt Fano model. Zhang's theorem and birational invariance give rational connectedness of $X$. [10]

Thus $\mathrm{CH}_0(X)_{\mathbb Q}$ is generated by a point over a universal domain. The threefold theorem of Gorchinskiy–Guletskii gives a rational Chow motive of abelian type for $X$, with middle summand $h^1(J)(-1)$ for an abelian variety $J$. In particular it is Kimura finite-dimensional. [11]

Write $P=h^1(E)$, $N=(S_0,(1-s^{2*})/2)$, and $M=(N\otimes P)^{\langle g\rangle}$. Section 3 gives an exact Chow retraction of $M$ from $h(X)$. In the rigid category of rational Chow motives insert elliptic coevaluation, average on $N\otimes P$, and contract the two elliptic slots using $P^\vee=P(1)$. The endomorphism of $N$ so obtained is the partial trace of the group projector. The categorical traces of $1,[i]^*,[-1]^*,[-i]^*$ on $P$ are $-2,0,2,0$, by Betti realization in graded vector spaces. The composite is therefore $-(1-s^{2*})/2=-1$ on $N$. Minus the evaluation retracts $N$ from $M\otimes P(1)$. Its complementary summand is the motive of the rational blowup $S_0/\langle s^2\rangle$, by finite double-cover trace. This proves that $h(S_0)$ belongs to the category generated by abelian motives, Tate twists and direct summands.

Huybrechts's isogeny theorem transports the abelian-type motive to the original $S$ using the rational Hodge isometry of Section 4. Both $t_2(S)$ and the matching summand of $h^1(B)\otimes h^1(E)$ are now finite-dimensional. Project the correspondences of Section 4 to these two Chow summands. Each composite differs from its identity by a homologically trivial endomorphism. Kimura nilpotence makes both composites invertible by finite geometric series, giving the claimed isomorphism of motives. [12, 13]

## 6. The intermediate Jacobian on a specified resolution

For every member of the smooth branch locus, let $B_8$ denote the positive half twist of the full rank-16 order-four summand, including the extra algebraic lines at a Picard jump. Let $D=C/\langle s|_C\rangle$. The involution on $C$ fixes its five intersections with the line and the point $[1:0:0]$. Riemann–Hurwitz gives $g(D)=2$, and $g(C)=6$. One smooth projective resolution $X$ of the diagonal quotient has

$$
 J^2(X)\ \sim_{\mathbb C}\ B_8\times J(C)\times J(D)^2,\qquad
 (b_2(X),b_3(X),e(X))=(37,36,40).
$$
Here the comparison of intermediate Jacobians is up to isogeny.

Blow up the eight disjoint curves $(R_0\sqcup C)\times E[2]$ in $W$ and divide by $g^2$. Each centre has two negative normal weights for the involution. On the blowup only the radial coordinate changes sign, so its quotient $Y$ is smooth. The residual involution fixes the two entire exceptional ruled surfaces over $R_0$ at the two $[i]$-fixed points on $E$. At each of the six fixed points on $C$ the two normal weights in $W$ are $-i,i$, and $s$ acts by $-1$ on the tangent to $C$. Over either fixed elliptic point, the two eigenlines in the exceptional fibre give residual tangent eigenvalues $(-1,-1,-1)$. There are 24 such points. The other two points in $E[2]$ are exchanged, and every residual fixed point lifts to the exceptional locus. Blow up the 24 points and take the residual quotient. Its fixed components are disjoint divisors with normal multiplier $-1$, giving the stated smooth $X$.

Finite quotient trace identifies the quotient motive at each smooth stage with the invariant part. The equivariant blowup formula adds $h(C)(-1)$ from the exchanged pair of centres on $C$, and $h(D)(-1)$ from each of its two individually preserved centres. The genus-zero centres and the point blowups contribute Tate classes. In degree three, $W$ supplies the positive half twist $H^1(B_8)(-1)$. This gives the four abelian factors of dimensions $8,6,2,2$. Degree two receives seven classes from $W$, six from orbits of curve centres, and 24 from the point blowups. Degree one vanishes, giving the Euler characteristic by duality. For any Gaussian abelian eightfold in the signature and norm class of paper 163, rational unitary density puts its weight-one period into the open half-twist family. The isogeny class of that eightfold thus occurs as the displayed factor of an intermediate Jacobian. The integral kernel and polarization gluing are additional questions.

## 7. Powers of the threefold

**Theorem.** At a very general point of the double-plane family, the ordinary rational Hodge conjecture holds on every joint product of powers of $X,S_0,B_8,E,J(C)$.

Let $P$ be the four-dimensional Prym of $C\to D$. Its connected rational monodromy is already $\mathrm{Sp}_8$ on a family with $D$ fixed. To see this, choose a smooth genus-two curve $v^2=F_6(y,z)$ with hyperelliptic projection $\pi$ and a non-Weierstrass point $p_0$. Let $p_0'$ be its conjugate and let $f_1$ vanish at $\pi(p_0)$. Choose a binary cubic $f_3$ whose value there is $-v(p_0)$ in the same fibre. The meromorphic section

$$
 k_0=(v-f_3)/(2f_1)
$$
of $2K_D$ has a simple pole at $p_0$ and is regular at $p_0'$. The four-dimensional space of sections of $N=2K_D+p_0$ consists of $k=t k_0+q_2$ for a scalar $t$ and a binary quadratic $q_2$. The double cover defined by $x^2=k$, with $x$ a meromorphic $K_D$-coordinate, has branch divisor $p_0+Z(k)$ when $k$ has simple zeros disjoint from $p_0$. For $t\ne0$, put $b=t f_3-2f_1q_2$, $c=(b^2-t^2 F_6)/(4f_1)$. Its plane equation is $f_1x^4+bx^2+c=0$, and $v=(2f_1x^2+b)/t$. The image is a birational plane quintic. Its normalization has genus six by Riemann–Hurwitz, hence the image is smooth. A general $k$ avoids vanishing over the Weierstrass points or at $p_0'$. Its five zeros have distinct images under $\pi$, since the difference of $k$ and its conjugate away from $f_1=0$ is $tv/f_1$. The plane quintic therefore meets the branch line transversely. Restriction to such an open preserves the image of monodromy since loops can avoid a proper complex algebraic subset.

The discriminant in the affine space $H^0(D,N)$ consists of the hyperplane of sections vanishing at $p_0$ and the cone over the dual of the degree-five embedding $D\hookrightarrow\mathbb P^3$. The second component is irreducible by the incidence of sections with a double zero. Generic tangency produces a Picard–Lefschetz transvection on $V=H_1(C,\mathbb Q)^-$. At the other component the local equation has branch factors $z(z-u)$, so the smoothing parameter of the node has order two and the meridian gives a squared transvection. To compare them, take a section tangent at $p_0$ with the other zeros simple. Indeed $N-2p_0=K_D+p_0'$ allows residual divisor $p_0'+q+q'$ disjoint from $p_0$. The constant and linear jets vary independently by very ampleness. The local branch divisor thus deforms as $z(z^2+\alpha z+\beta)=0$. Arcs between successive points of a nearby real triple give a vanishing cycle of each type and their intersection is $\pm1$.

The meridians normally generate the fundamental group of the complement, by transversality of a bounding disc in affine space. The conjugate meridians of each type form one orbit of vanishing lines. Scalar rotation of $k$ acts as $-1$ on $V$, whereas meridians act trivially modulo the span of the vanishing lines. These lines therefore span $V$. Connect two lines whenever their pairing is nonzero. The spans of the connected components form an orthogonal direct sum, and each transvection preserves every component span. Thus each orbit lies in one component. The pair with intersection $\pm1$ connects the two orbits. In $\mathfrak{sp}(V)=\operatorname{Sym}^2V$, the connected algebraic monodromy Lie algebra contains $v^2$ for every vanishing line $\mathbb Q v$, by taking the Zariski closure of its transvection powers. Bracketing two such squares gives $vw$ on each edge. Along a path, the bracket of $vw$ with $z^2$ gives a nonzero multiple of $\langle w,z\rangle vz+\langle v,z\rangle wz$. Subtracting the known edge term inductively gives all $vz$. This proves full symplectic monodromy.

Connected monodromy is contained in the very general Hodge group of the variation. Consequently $P$ has Hodge group $\mathrm{Sp}_8$ there. The construction realizes a general genus-two $D$, so $J(D)$ has Hodge group $\mathrm{Sp}_4$. On the Gaussian ball the very general derived group on $B_8,E$ has complex type $A_7$. Indeed the very general endomorphism field of the K3-type block is $K$ by variation of all positive lines in the ball, and Zarhin gives the unitary group on it. Recovering this block as a $K$-tensor with the CM elliptic line changes only central characters. The three simple types $A_7,C_4,C_2$ are distinct. The joint derived group therefore has the product Lie algebra, by surjectivity on each factor and simplicity. The two symplectic factors already have full semisimple Hodge groups. Their invariants on tensor powers are generated by the polarization pairings, represented by divisors. The Gaussian invariants are algebraic by paper 163. Since $J(C)\sim P\times J(D)$, this gives algebraicity on the joint abelian powers. The split $H^2(S_0)$ and $H^3(X)$ correspondences and the algebraic Tate summands in the other degrees give the asserted theorem. [1, 14, 15]

## 8. An arithmetic family

The conclusion of Section 7 holds for every integral triple $(f_1,f_3,f_5)$ congruent coefficientwise modulo 55 to

$$
 f_1=y,\qquad f_3=z^3+yz^2-2y^2z-2y^3,\qquad
 f_5=z^5-2y^2z^3+y^4z-y^5 .
$$
This includes special periods of the Gaussian K3 within the congruence class. The proof determines the Hodge groups of $J(D)$ and $P$ at each lift.

The binary forms $f_5$ and $\Delta=f_3^2-4f_1f_5$ are squarefree at 5 and 11, and $f_1$ and $f_3$ have disjoint zeros. This verifies good reduction. At $x=0$ smoothness follows from transversality. At $[1:0:0]$ it follows from the linear form $f_1$. Elsewhere $a=x^2$ is an étale variable, and completing the square in $f_1a^2+f_3a+f_5$ rules out a singular point by simplicity of the zeros of $\Delta$. At the zero of $f_1$ use $f_3\ne0$. The quotient $D$ has equation $v^2=\Delta$. In each fibre over $[y:z]$ count $1+\chi(a)$ on $C$ for each distinct root $a$ of the quadratic, and add the projection centre once. On $D$ count $1+\chi(\Delta)$, with $\chi(0)=0$. This gives the following pairs $(\#C,\#D)$ in successive finite extensions.

| Prime | Degree 1 | Degree 2 | Degree 3 | Degree 4 |
|---|---|---|---|---|
| 5 | (9,5) | (33,31) | (117,119) | (701,699) |
| 11 | (15,16) | (119,130) | (1323,1384) | (14763,14646) |

For a factor of dimension $g$, write its Frobenius polynomial as $W(X)=X^g R(X+p/X)$. Use traces $p^j+1-\#D$ and $\#D-\#C$ for $J(D)$ and $P$, respectively. Newton's identities and reciprocity give the four $R$'s below. Their middle Weil coefficients, in table order, are $3,12,17,62$, all units at the reduction prime. In the last column the first prime gives a full $g$-cycle on the roots of $R$, the middle prime when present gives cycle lengths $1,3$, and the last prime splits $R$ completely and gives one quadratic and $2g-2$ linear factors for $W$. The displayed factorizations are squarefree.

| Factor | $p$ | $R(U)$ | Auxiliary primes |
|---|---:|---|---|
| $J(D)$ | 5 | $U^2-U-7$ | 3, 13 |
| $J(D)$ | 11 | $U^2+4U-10$ | 3, 5 |
| $P$ | 5 | $U^4+4U^3-11U^2-46U-23$ | 7, 11, 97 |
| $P$ | 11 | $U^4-U^3-49U^2+18U+414$ | 5, 13, 173 |

The permutation quotient on the $g$ reciprocal pairs is $S_g$. In degree four, the four-cycle and three-cycle force this by the order and sign of the subgroup. Conjugating the single flip gives all independent coordinate flips. Choose one root $\pi_j$ in each pair. Ordinarity gives the $p$-adic slopes zero or one, so $\pi_j^2/p$ has nonzero $p$-adic valuation. A relation among these ratios up to a root of unity, divided by its conjugate under a single flip, forces the exponent at that label to vanish. They are consequently multiplicatively independent modulo torsion. In particular all $2g$ conjugates stay distinct after any positive power, so Frobenius over every finite extension has commutant of dimension $2g$ on the rational Tate module. Its root field $\mathbb Q(\pi)$ already supplies that dimension. The geometric endomorphism algebra of each reduction is that field.

The root stabilizer is generated by the flips and permutations on the other $g-1$ pairs. Its only proper overgroup short of the full signed permutation group is the pair stabilizer. Indeed moving its own pair supplies the missing flip by conjugation, and the permutation group then acts transitively and contains $S_{g-1}$. Thus the unique proper intermediate field of the root field is $\mathbb Q(\pi+p/\pi)$. For $J(D)$ the two real trace fields split at 11 with types $(2)$ and $(1,1)$. For $P$ they split at 5 with types $(1,3)$ and $(4)$. These factorizations are squarefree at the indicated test primes. The real fields in each comparison are nonisomorphic, and the CM fields are also nonisomorphic by their unique maximal real subfields. Specializing the characteristic-zero geometric endomorphism algebra injects it into both reduction fields, proving it equals $\mathbb Q$ for each factor.

Deligne's absolute Hodge theorem places a positive power of good Frobenius in the $\ell$-adic points of the Mumford–Tate group for $\ell\ne p$. The independent ratios give torus rank at least $g$ on the kernel of the multiplier, since $p$ adds an independent direction by complex absolute values. Thus the Hodge group contains a maximal torus of $\mathrm{Sp}_{2g}$ over $\mathbb C$. The representation is irreducible over $\mathbb C$ by semisimplicity and the scalar commutant. For this maximal torus the weight lines are $\pm e_j$. The graph on them defined by the root operators of the Hodge Lie algebra is connected by irreducibility, and every directed difference of distinct weights is a root of type $C_g$. Along a simple directed path the nonzero brackets of consecutive root spaces supply the root space for the endpoint difference. Every weight is reachable from each other, since otherwise the reachable weight lines span a proper invariant subspace. Thus every symplectic root space occurs. This proves Hodge groups $\mathrm{Sp}_4$ and $\mathrm{Sp}_8$. [16]

At every K3 period in the class, split the full order-four block into the simple transcendental part and its Gaussian divisor classes. The latter contribute copies of the Gaussian elliptic curve to $B_8$ up to isogeny. The Hodge endomorphism field of the transcendental part is CM since it contains $K$. Zarhin's unitary-group theorem gives only type $A$ nonabelian simple derived factors there. The joint Gaussian group with $E$ has the same derived types by the half-twist tensor splitting. Neither $C_2$ nor $C_4$ is among them, so the product and symplectic pairing argument of Section 7 applies at every certified period. [1, 15]

## 9. The Eisenstein comparison in every rank

Let $K=\mathbb Q(\theta)$, $\theta^2=-3$. Give $T$, the positive half twist $B$ and the elliptic curve $E$ the convention of Section 1, with $L=H^1(E)$ holomorphic at the embedding on $H^{2,0}(S)$. The adjoint of $\theta$ is $-\theta$ by [15]. The cup form $q$ is the trace of the Hermitian form

$$
h(x,y)=\tfrac12\bigl(q(x,y)+q(\theta x,y)/\theta\bigr)
$$

of signature $(1,m-1)$, where $m=\dim_K T$. Projectivity implies $m\le10$.

**Theorem.** For every such $S$, there is a squarefree binary duodecic $g$ such that $S$ is rationally Hodge isometric in degree two to the elliptic K3 surface $J_g$ with equation $y^2=x^3+g$. The transcendental isometry intertwines the specified $K$-action. There is an isomorphism of rational Chow motives

$$
t_2(S)\simeq h^1(B)\otimes_K h^1(E).
$$

The motive of $S$ is of abelian type. All rational Hodge classes on $S^r\times B^a\times E^b$ are algebraic for all nonnegative $r,a,b$.

On $J_g$, the section and the fibre generate a hyperbolic plane $U$. The automorphism $\sigma(x,y,t)=(\zeta_3x,y,t)$ fixes the section and the genus-five curve $x=0$, pointwise. These exhaust its fixed locus, including the cusps over simple roots. The topological Lefschetz formula gives trace $-8$ on $H^2$. Its invariant lattice has rational rank two. Thus $V=U_{\mathbb Q}^{\perp}$ is the rank-twenty Eisenstein space with Hermitian cup form $h_0$ of signature $(1,9)$. Choose the generator to match the specified period embedding.

The twelve unordered roots modulo projectivities have nine moduli. A marking preserving the fibre class recovers the elliptic pencil from that class and recovers the roots as its singular values. The locally marked period image therefore has dimension nine by local Torelli. It contains an analytic open of the nine-ball of positive lines in one eigenspace of $V$. Equivalently the primitive differentials on $C_g:u^6=g(t)$ are $dt/u$ and $t^jdt/u^5$ for $0\le j\le8$. Their products are the nine independent quadratic differentials $t^j(dt)^2/g(t)$ on $\mathbb P^1$ with at most simple poles at the twelve branch points. [17]

For $m<10$, adjoining $10-m$ negative Hermitian lines of type $(1,1)$ matches $\det h_0$ by the choice $-|\det h_0/\det h|,-1,\ldots,-1$ in Section 4. For $m=10$ there is a different reason for the match. Each Hermitian diagonal entry $a$ has trace matrix $\operatorname{diag}(2a,6a)$, so $\det q_T$ is a square. The full rational K3 lattice has determinant $-1$ modulo squares. The Néron–Severi lattice consequently has rank two and determinant a negative square, hence is rationally hyperbolic. Quadratic Witt cancellation gives $q_T\simeq q_V$. To recover the $K$-linear isometry, the trace of $h\perp(-h_0)$ is hyperbolic. Every trace-isotropic vector is Hermitian-isotropic since the diagonal value has trace twice its rational value. Split off a Hermitian hyperbolic plane. Its trace is two quadratic hyperbolic planes, so the remaining trace is hyperbolic by cancellation. Induction followed by Hermitian cancellation gives $h\simeq h_0$. The general arithmetic of Hermitian transfers and K3 Picard lattices is developed in [18].

Rational unitary density moves the resulting period into the squarefree open, as in Section 4. The complement of the image of $T$ inside $V$ has type $(1,1)$, and $T$ itself has no rational divisor classes. Thus the image is exactly $T(J_g)$, including at each matched Picard jump. Extend the cup isometry inside the full rational K3 lattice by Witt extension. Buskin and Huybrechts give the algebraic degree-two isometry and an isomorphism of rational Chow motives. [9, 12]

The map $p:C_g\times E\dashrightarrow J_g$ sends $(t,u;X,Y)$ to $(t,u^2X,u^3Y)$, with $E$ given by $Y^2=X^3+1$. The generic extension has degree six. Resolving the map by point blowups splits $h(J_g)$ off a motive of abelian type by pullback and normalized pushforward. The two-form pulls back to $(dt/u)\wedge(dX/Y)$. For a primitive sixth root $\lambda$, the quotient generator sends $(u,X,Y)$ to $(\lambda u,\lambda^{-2}X,\lambda^{-3}Y)$. Thus pullback places the transcendental part in the inverse deck characters of $H^1(C_g)$ and $L$. Mark the primitive curve part by the inverse square of its deck generator and mark $E$ by the square of its displayed action. These markings give the equal-$K$-embedding tensor of Section 1, since the holomorphic lines $dt/u$ and $dX/Y$ then both have eigenvalue $\zeta_3=\lambda^2$. The primitive-sixth Jacobian factor $B_g$ has dimension ten. At a very general squarefree period its matching tensor has rank twenty, the pullback is injective there, and it is an isomorphism onto that tensor by dimension. The comparison extends to the full local systems with the $U^\perp$ summand on the K3 side: the quotient maps are relative correspondences, and projecting to the two degree-one factors and to $U^\perp$ is algebraic. On transcendental cohomology the normalized trace $p_*/6$ inverts pullback. At a jump the extra $(1,1)$ lines give definite elliptic factors after half twisting. The complementary factor of $B_g$ is isogenous to $B$ compatibly with $K$. These projections and the Abel maps are algebraic. The two motives in the theorem are now finite-dimensional, so the inverse cohomological maps lift to inverse Chow correspondences by [13].

For completeness, take the majority embedding of $H=H^1(B_g)$ and let $L_+$ be the elliptic Hodge structure marked holomorphic at that embedding. The rational determinant plane $\det_K H\otimes_K\bar L_+^{\otimes_K 8}$ is algebraic. The cyclic determinant theorem [19, Lemma 3.4] supplies $\det_K H$ from powers of the Fermat sextic Jacobian, with Tate twists. The nontrivial Fermat characters contributing to $H^1$ have orders three or six and multiplicity one. Each conjugate pair gives an elliptic factor with CM by $K$, hence the Jacobian is isogenous to $E^{10}$. Tensor the supply with the eight correcting elliptic factors and lift the two rational Tate classes through the resulting surjection by polarizability. Their lifts on powers of $E$ are generated by divisors. The pointwise determinant criterion [1, Section 5], whose proof works for any imaginary quadratic field, gives ordinary Hodge on all mixed powers of $B_g,E$, also at endomorphism jumps. Isogeny projections and the Chow isomorphism above transport it to the stated powers.

## 10. The exterior square and zero-cycles

For every Eisenstein surface in Section 9 the Chow projector onto $\bigwedge^2t_2(S)$ factors through a finite direct sum of motives of products of two smooth projective curves with one Lefschetz twist. Here alternation uses interchange of the two surface factors. In particular degree-zero rational zero-cycles $a,b$ on $S$ satisfy

$$
a\times b=b\times a\qquad\text{in }\mathrm{CH}^4(S\times S)_{\mathbb Q}.
$$

Work first in the rank-twenty tensor $H\otimes_K L$ of Section 9, marking $L$ at the period embedding. In its rational exterior square the terms using opposite embeddings pair the two elliptic slots into a Tate line by the polarization. These terms split from two curve $H^1$ slots with one Lefschetz twist. Both opposite-embedding lines and their duals are selected after scalar extension by the elliptic endomorphisms. The conjugate projections and pairings descend together. The terms using the same embedding have the form $\bigwedge^2H_\sigma\otimes L_\sigma^{\otimes2}$ and its conjugate.

To split these terms use the compact threefold of [20, Section 7.2]. The group $\mu_6^2$ multiplies the two sheet coordinates of $C_g^2$ by $a,b$ and acts on $E$ by $(X,Y)\mapsto((ab)^{-2}X,(ab)^{-3}Y)$. Include interchange of the curves, acting trivially on $E$. The quotient has generic degree $2\cdot6^2=72$, from the two orderings and the independent choices of sixth roots. On the triple degree-one tensor the quotient projector selects $\bigwedge^2H_\sigma\otimes L_\sigma$ and its conjugate. The minus sign in interchange comes from the two odd cohomological degrees. Over $\operatorname{Sym}^2\mathbb P^1$ the Weierstrass quotient has equation $y^2=x^3+g(t_1)g(t_2)$. The constant coefficient cuts out twelve lines with only pairwise crossings. The Weierstrass fundamental bundle is $\mathcal O(2)$ and the canonical divisor pulls back $\mathcal O(-1)$. The singularities over crossings are isolated, with local equation $y^2=x^3+uv$. General complete-intersection curves on the projective model avoid them, cover a dense open, and have negative canonical degree. Their moving class on a resolution implies uniruledness. The quotient graph as in Section 3 splits the invariant triple tensor into its $H^3$, with normalized transpose divided by 72. The uniruled threefold argument there gives two algebraic maps splitting that tensor inside a sum of curve $H^1$'s with one Lefschetz twist. Tensor with the remaining elliptic slot and retain the matching embeddings by the field projectors.

The preceding maps factor the identity on the exterior square in cohomology through $H^2$ of products of curves with a Lefschetz twist. Composing with the inclusion and retraction of $t_2(S)$ in Section 9 gives the same factorization on $\bigwedge^2 T(S)$. Its Chow motive is finite-dimensional as a summand of $h(S^2)$. Kimura nilpotence corrects the composite to the identity there. On $\mathrm{CH}^4$ the intermediate groups are $\mathrm{CH}^3$ of surfaces, which vanish. The transcendental projector acts identically on degree-zero zero-cycles, so alternation annihilates $a\times b$.

Bolognesi–Laterveer proved finite-dimensionality for order-three actions fixing a curve and zero-cycle symmetry on their two nine-dimensional components. Their Remark 6.7 singles out the third component $\mathcal M_{3,0}$. On each member of that six-dimensional component the nonsymplectic action supplies an Eisenstein action on $T(S)$, since its fixed substructure has type $(1,1)$. The conclusions of Sections 9 and 10 therefore apply throughout this component. Its general member has invariant lattice of rank eight and requires three stabilizing Eisenstein lines. [5, Section 6]

## 11. Joint powers of Eisenstein K3 surfaces

Put $K=\mathbb Q(\sqrt{-3})$. Use the action on the holomorphic line to embed each transcendental endomorphism field in $\mathbb C$. Orient the common elliptic curve $E$ at the resulting inclusion of $K$, and use this marking on the positive half twists.

**Theorem 11.1 (two surfaces).** Let $S_1,S_2$ be projective complex K3 surfaces with $K$-action on their actual rational transcendental Hodge structures $T_1,T_2$. Write $E_i=\operatorname{End}_{\mathrm{HS}}(T_i)\subset\mathbb C$, $F=E_1\cap E_2$, $u_i=\dim_K T_i$, $h=[F:K]$ and $p_i=u_i/h$. Let $B_i$ be the positive half twist of $T_i$. Ordinary rational Hodge holds on
$$
 S_1^a\times S_2^b\times B_1^c\times B_2^d\times E^e
 \qquad(a,b,c,d,e\geq 0)
$$
if both transcendental ranks are at most fourteen. In every allowed rank the same holds if $F=K$, or if for each $i$ either $p_i\leq 2$ or $(h,p_i)=(2,3)$. In particular, coprime $u_1,u_2$ suffice. All statements concern the actual fields at the chosen pair of periods.

**Theorem 11.2 (a common marked field).** Fix a CM field $F\supseteq K$ and an embedding $\tau:F\hookrightarrow\mathbb C$. Let $S_1,\ldots,S_n$ be projective complex K3 surfaces with Hodge actions of $F$ on $T_i$ inducing $\tau$ on all the holomorphic lines. Suppose $\dim_F T_i$ is one or two for every $i$. Ordinary rational Hodge holds on $\prod_i S_i^{a_i}$ for all $a_i\geq 0$. The statement includes rank twenty and arbitrary simultaneous extra-endomorphism periods.

### 11.1. Algebraic comparisons over the common field

In this section $(1)$ lowers weight by two. Write $V=T(1)$ and $L=H^1(E,\mathbb Q)$, holomorphic at the prescribed $K$-embedding. Write $\bar L$ for the same structure with conjugated $K$-action. Section 9 identifies $T$ algebraically with $H\otimes_K L$ for $H=H^1(B)=T\otimes_K\bar L(1)$. Any $K$-linear Hodge map between two such $T$'s induces a rational weight-one map of positive halves. It comes from an abelian homomorphism up to rational multiples. Tensoring back with $L$ using the algebraic comparison gives the original map, with no condition on the cup forms. In particular the field actions on $T$ and on $H$ are algebraic. The separability projector selecting equal field embeddings and the alternator give the determinant projector. On degree-one slots the geometric interchange has the Koszul sign, so ordinary tensor alternation there uses unsigned geometric permutations.

For any marked subfield $K\subseteq F\subseteq\operatorname{End}_{\mathrm{HS}}(T)$ put $m=\dim_F T$. The determinant $\Delta_F=\Lambda_F^m V$ is an $F$-line of weight zero. Its circle exponents are $2,-2$ at the holomorphic embedding and its conjugate, and zero elsewhere. This follows by adding the weights of the $m$ lines at each embedding. Denote this fixed marked structure by $D_0(F)$ and put $D(F)=D_0(F)(-1)$. Its labelled type determines it up to $F$-linear Hodge isomorphism.

For $F=K$, realize $D_0(K)$ by $(L\otimes_K L)(1)$ on $E^2$. A marked isomorphism from $\Delta_K$ and its inverse give rational Hodge classes on $S^m\times E^2$, using the determinant projector and Poincaré duality. Section 9 makes both maps algebraic for every $m\leq 10$.

For $F\supsetneq K$ a rank-one input realizes $D(F)$ if available. Otherwise whenever a comparison below is needed, $[F:\mathbb Q]\leq 10$. In that range a projective K3 $S_F$ realizes $D(F)$: choose the form
$$
 q(x,y)=\operatorname{Tr}_{F/\mathbb Q}(b\,x\bar y)
$$
with $b\in (F^+)^\times$ positive at the marked real place and negative elsewhere. Weak approximation gives $b$. The rational quadratic embedding criterion [18, Lemma 2.3] embeds it in the rational K3 lattice, with orthogonal complement of signature $(1,21-[F:\mathbb Q])$. The marked holomorphic line is isotropic and positive against its conjugate. The period theorem gives a marked K3, and the complement provides a positive rational divisor class, hence projectivity. A nonzero rational Tate vector in $D(F)$ would generate it over $F$, which is impossible. Thus $T(S_F)=D(F)$. For $m=1$ the comparison follows from the weight-one construction above.

For $m=2,3$ the required determinant has positive half twist
$$
 \bigl((\Lambda^m_F T)(m-1)\otimes_K\bar L\bigr)(1)
 \simeq (\Lambda^m_F H)\otimes_K L^{\otimes_K(m-1)}(m-1).
 \tag{11.1}
$$
Indeed $T=H\otimes_K L$ and $L\otimes_K\bar L\simeq K(-1)$ by the elliptic pairing, with inverse given by coevaluation in the matching slots. For $m=2$ Section 10 splits the same-$K$-embedding triple tensor $\Lambda^2_K H\otimes_K L$ through curve $H^1$ with a Lefschetz twist before restoring the last elliptic slot. Its restriction to the actual $H$ uses the two maps of Section 9. Project further to the same $F$-label on the two $H$-slots. If $u,r$ are the inclusion from and retraction to the weight-one source after twisting, and $p$ is the equal-$F$ projector on the supported tensor, $rpu$ is a weight-one idempotent. It is induced by an abelian idempotent up to isogeny. Its image, with the two restricted maps, realizes (11.1).

For $m=3$ and $[F:K]=2$, write $F=KR$ for $R=F^+=\mathbb Q(\sqrt d)$, $d>0$ nonsquare. The half twist is a sixfold of signature $(5,1)$ with the majority embedding opposite the holomorphic embedding of $L$. The compatible half-twist polarization makes $R$ self-adjoint: the adjoint on $F$ for the K3 cup form is conjugation by [15], and this persists on the elliptic tensor and its matching summand. Trace duality then writes the $K$-Hermitian polarization form as $h=\operatorname{Tr}_{F/K}h_F$, with $h_F$ an $F/R$-Hermitian form of rank three. Its signatures at the real places are $(3,0)$ and $(2,1)$ in the majority convention. In an orthogonal $F$-basis let $\delta\in R^\times$ be its determinant. A diagonal coefficient $r\in R^\times$ contributes $4dN_{R/\mathbb Q}(r)$ to the determinant in the $K$-basis $1,\sqrt d$. Hence $\det_K h=(4d)^3N_{R/\mathbb Q}(\delta)$. The opposite signs of $\delta$ make one choice of $a=\pm\sqrt d\,\delta$ totally positive. The Hermitian form $h_a(x,y)=h(ax,y)$ polarizes the same Hodge structure after an integral scaling. In the trace basis,
$$
 -\det_K h_a
 =-(4d)^3N_{R/\mathbb Q}(\delta)N_{R/\mathbb Q}(a)^3
 =\bigl(8d^3N_{R/\mathbb Q}(\delta)^2\bigr)^2.
 \tag{11.2}
$$
This is a $K$-norm. Basis changes multiply it by a norm, and rational scaling contributes a sixth power. This uses the given $F$-action even at larger endomorphism fields.

The transport in [21, Section 8.2] uses the Hermitian classification [8] and rational unitary density to put this marked period in the open of the split sixfold curve datum. The induced $K$-linear isogeny transports the algebraic inclusion and retraction of the cube from [21, Theorem B and Section 3]. The correcting elliptic slots there have the embedding opposite the half twist's majority, so the supplied weight-one summand is
$$
  \bigl(\Lambda^3_K H\otimes_K L^{\otimes_K 2}\bigr)(2)
  \subset H^5(B^3\times E^2)(2).
$$
Project onto the same $F$-label in all three exterior slots. The transported $F$-endomorphisms are algebraic on $H$ by the weight-one equivalence. As for the square, the projected half twist (11.1) is an abelian isogeny summand with algebraic inclusion and retraction.

In each supported case, a marked isomorphism with the positive half of $D(F)=T(S_F)$ is induced by an abelian isogeny up to rational multiples. Tensor back with $L$ and use Section 9 to get algebraic inverse maps between $(\Lambda^m_F T)(m-1)$ and $T(S_F)$. The correspondence on $S^m\times S_F$ and that on the reversed product have codimension $m+1$. The maps are inverse on projected cohomology, which suffices below. One obtains inverse Chow maps by Kimura nilpotence on the projected finite-dimensional motives from Section 9.

### 11.2. The joint derived group

Use weight-zero $V_i=T_i(1)$. Zarhin [15] gives simplicity, CM endomorphism fields $E_i$ containing $K$, and the individual unitary groups. For $m_i=\dim_{E_i} T_i\geq 2$, the derived Lie algebra is the restriction from $E_i^+$ of the special unitary Lie algebra of the Hermitian trace form. It is rationally simple, with centroid $E_i^+$, since the absolute simple factors are indexed transitively by the embeddings of $E_i^+$. The K3 cup signs give signature $(1,m_i-1)$ at the real place below $H^{2,0}$ and negative definiteness at all others. There is exactly one noncompact real factor. For $m_i=1$ the Hodge group is a torus.

The joint group is connected reductive with surjective projections. Its derived Lie algebra is subdirect on the nonzero derived Lie algebras. Its simple ideals partition the factors into diagonal blocks, since a simple ideal maps either isomorphically or trivially to a simple quotient, and exactly one ideal maps nontrivially to each quotient. Suppose two are in the same block. The graph isomorphism implies $m_1=m_2=m$ and identifies the real centroids at the unique noncompact place. With the embeddings determined by the holomorphic lines this gives equality of the embedded real fields. The CM fields also agree, since each is the compositum of its real field with $K$. The graph map is linear over that real field.

Extend scalars from the common real field to the common embedded CM field $E_1=E_2$, using $\mathfrak{su}(h_i)\otimes_{E_i^+}E_i\simeq\mathfrak{sl}_{E_i}(T_i)$. Over an algebraic closure the Lie isomorphism is inner or is induced by negative transpose. The trace-zero derivatives of the joint Hodge circle lie on the graph. At the distinguished embedding they have eigenvalues, with the same overall normalization,
$$
 2-2/m\quad\text{once},\qquad -2/m\quad\text{with multiplicity }m-1 .
$$
For $m>2$ negative transpose reverses this multiset, so the graph is inner. In type $A_1$ all automorphisms are inner. An inner map between the two split Lie algebras over $E_i$ comes from an $E_i$-linear basis change: the adjoint automorphism group is $\mathrm{PGL}_m$, and projective linear elements lift to $\mathrm{GL}_m$ over a field. This proves rational descent for the intertwiner without choosing lifts of the joint graph through central isogenies. In rank two the real forms used here include both the split quaternion at the active place and the compact quaternion at every other real place.

The joint central Lie algebra acts on each of the two slots by $E_i$-scalars since it commutes with the individual unitary group. The equal marked types of their $E_i$-determinants identify those determinant representations. Differentiating and dividing by $m$ gives equality on the scalar Lie actions. The basis change therefore intertwines the full joint Lie algebra, hence the connected joint group. It is a Hodge isomorphism respecting the markings, and Section 11.1 algebraizes it in both directions. For a pair in a single block this reduces the theorem to Section 9, by replacing one factor and its half twist by the other, with the remaining K3 cohomology Tate. For a list, consolidate such isomorphic slots. The remaining derived group is the full product of its independent special unitary groups, by connectedness and equality of Lie algebras. Adjoining torus factors does not change the derived group.

### 11.3. Two-field incidence and the proof of Theorem 11.1

With the independent derived action, choose a normal CM field $N$ containing the normal closures of $E_1,E_2$. Let $\Gamma=\operatorname{Gal}(N/\mathbb Q)$ and $J_i=\operatorname{Gal}(N/E_i)$. Form the bipartite graph with vertices $gJ_i$ and edges $(gJ_1,gJ_2)$ for $g\in\Gamma$. An edge can be followed by right multiplication by elements of the subgroup fixing a shared vertex at the identity, and successive steps give all products in $\langle J_1,J_2\rangle=\operatorname{Gal}(N/F)$. More explicitly, at an edge indexed by $g$, the indices of the edges sharing its $i$th vertex are precisely $gJ_i$. Thus the connected components are the cosets of $\operatorname{Gal}(N/F)$, indexed by embeddings of $F$. No normality assumption on $F$ or on either $E_i$ over $\mathbb Q$ is needed.

Over a splitting field use field projectors to allocate tensor slots to embeddings of $E_i$. At a conjugate pair of embeddings, the two $m_i$-spaces are dual by cup, with the weight-zero normalization. The first fundamental theorem for $\mathrm{SL}_{m_i}$ gives invariant diagrams spanned by cup pairs and alternating $m_i$-tensors in a single orientation after removing opposite determinant pairs. The determinant and its dual together expand into the signed sum of products of cup tensors. When $m_i=1$ the same accounting is immediate. If there are derived invariants, the signed excess of slots at $\sigma$ over $\bar\sigma$ is $m_i x_i(\sigma)$ with integer $x_i(\sigma)$, odd under conjugation. Every diagram at this allocation has the same central character.

The joint group on the determinant and elliptic slots is the torus generated by the rational translates of their joint Hodge cocharacter. The marked determinant weights are $2,-2$ at the distinguished embeddings, and the elliptic weights are $1,-1$. A labelled diagram that can contribute to a Hodge class must therefore satisfy
$$
 2x_1(gJ_1)+2x_2(gJ_2)+y(g|_K)=0\qquad(g\in\Gamma),
 \tag{11.3}
$$
where $y$ is the signed elliptic count and is zero in the absence of elliptic slots. Within each connected component $y$ is constant because $K\subseteq F$. The equations then force each $x_i$ to be constant on the vertices of its side over each embedding of $F$. This treats the actual joint cocharacter, including all field intersections.

For each $F$-embedding group one remaining $E_i$-determinant from every embedding over it, using the common orientation supplied by the signed counts. The resulting tensor lies on the corresponding $F$-determinant line $\Lambda_F^{p_i}V_i$, since exterior top degree of a direct sum of the $m_i$-spaces is the tensor product of their top degrees. The labelled map is obtained by taking the top wedge projector and its inclusion into the tensor and projecting onto the ordered embedding slots. The opposite orientation uses the conjugate label, which cup identifies with the dual. This accounts for all diagrams using powers of the $F$-determinants, cup tensors and the elliptic slots.

For rational descent, take the span of the insertion maps from these determinant tensor powers, with the elliptic slots carried along. Over $N$ they use projectors in the $N$-span of the rational algebraic field actions. For each such map take the Galois traces of its multiples by a rational basis of $N$. These are rational algebraic maps, and after scalar extension their span contains the original map by nondegeneracy of the field trace pairing. The resulting direct-sum image contains every Tate tensor in the target. Semisimplicity of polarizable rational Hodge structures lifts each rational Tate class to a rational Tate class in the source, with the indicated degree-normalizing twists. Under the hypotheses, Section 11.1 identifies every determinant source with the same $D_0(F)$. The source classes are algebraic by Section 9 for $S_F$ and $E$, or by the divisor-generated Hodge classes on powers of the CM elliptic curve when $F=K$. Apply the algebraic insertion maps to these representatives.

The other K3 cohomology has algebraic Tate projectors. Each $H^1(B_i)$ is an algebraic summand of $T_i\otimes_K\bar L(1)$, and $H^r(B_i)$ is a split summand of the tensor of $r$ copies of $H^1(B_i)$. For the latter, pull back by addition and project onto the all-$H^1$ Künneth part. Pullback by the diagonal returns $r!$ times the identity, since cohomology of an abelian variety is the exterior algebra on $H^1$. This proves the theorem with both positive half twists and $E$.

Since $u_i\leq 10$, the rank bound fourteen means $u_i\leq 7$. When $h\geq 2$, $p_i\leq 3$ in that range and $p_i=3$ forces $h=2$ and $u_i=6$. Over the full allowed rank range the only individual pairs $(h,p_i)$ with $h>1$ outside the determinant criterion are $(2,4),(2,5),(3,3)$. The conditions are sufficient, and the diagonal reduction also applies independently of the rank bound.

### 11.4. Quadratic character independence and the proof of Theorem 11.2

Identify the common field with its image under $\tau$. Zarhin and the relative rank bound give three possibilities: a rank-one $F$ structure, a rank-two structure with endomorphism field $F$, and a rank-one structure over an embedded quadratic CM extension $L_i/F$. All rank-one $F$ inputs have type $D(F)$. For the quadratic case equal embedded fields give marked Hodge isomorphisms because the unique holomorphic embedding is the inclusion and the conjugate line determines the antiholomorphic embedding. Section 11.1 realizes these isomorphisms algebraically. After consolidating, retain distinct $L_i$ and the independent rank-two non-CM factors of Section 11.2. Adjoin $D_0(F)$, already the determinant of any rank-two input or isomorphic to a rank-one input.

For a CM field $M$ let $U_M$ be the restriction to $\mathbb Q$ of the norm-one torus of $M/M^+$. The joint group on $D_0(F)$ and the CM slots is the fiber product of $U_{L_i}$ over $U_F$ by their relative norms, with $D_0(F)$ carrying the common character. To prove this take a finite normal CM field $N'$ containing the normal closures. Put $\Gamma'=\operatorname{Gal}(N'/\mathbb Q)$, $J=\operatorname{Gal}(N'/F)$, and let $c$ be complex conjugation. View rational norm-one character spaces as odd functions $f(cg)=-f(g)$ on embedding cosets in $\Gamma'$. For $L_i$ these are invariant under right translation by the index-two subgroup cutting out $L_i$ in $J$. They decompose into the functions constant on $gJ$ and the functions satisfying $f(gn)=\chi_i(n)f(g)$ for $n\in J$, with distinct nontrivial quadratic characters $\chi_i$. Character orthogonality on $J$ makes these latter spaces independent, also when one character is a product of others. The pairing with the $g$-translate of the joint cocharacter of a rank-one K3 type is, up to one common factor, evaluation at $g$. Thus the only character relations are identifications of the common norm parts. This argument uses right translation and applies when $J$ is nonnormal. Over a splitting field each relative norm is coordinatewise $(x,y)\mapsto xy$, with connected kernel. The fiber product is connected, so the character calculation proves equality of the groups.

The full group is the corresponding determinant fiber product after adjoining the independent non-CM unitary groups. Indeed the kernel of the map to the toric group just computed is the product of their special unitary groups by Section 11.2. For each embedding label, apply the $\mathrm{SL}_2$ invariant diagrams to those non-CM slots. In a quadratic CM slot above a chosen $F$-embedding, let $x,y$ be the two line characters. After using the relative norm kernel, the signed counts of $x$ and $y$ are equal. Use cup pairs first and group the residual slots into determinant pairs or their duals. Their ordered tensors are the projections of the alternating two-tensor by the individual $L_i$-embedding idempotents. The remaining common $U_F$-characters, including the rank-one slots, balance with their inverses at every conjugate pair of labels. Each pairing is algebraic through the common $D(F)$ and its projected cup diagonal, or through $(L\otimes_K L)$ when $F=K$. The embedding projectors lie in the scalar extension of the rational algebraic field actions. Consequently the complex span of rational cycle classes contains every invariant diagram, and equality descends to $\mathbb Q$ by scalar extension of fixed spaces. Restoring repeated factors by the marked algebraic comparisons and using the Tate projectors completes the proof.

### 11.5. Relation to earlier results

Ramón-Marí's unitary invariant argument gives self-powers when the transcendental endomorphism field is CM, using algebraic Hodge isometries. Zarhin supplies the individual groups. Commelin defines the determinantal K3-type motive and points out the central ambiguity in unitary rank two. The mixed-product criterion of paper 107 singles out small-factor gluing and central determinant classes. The fixed cyclotomic families of paper 16 already use common geometric determinants, diagonal reduction and joint quadratic characters, with additional norm comparisons for particular mixed exponents. Here Sections 9–10 and the repolarized cube of [21] supply the determinants for arbitrary Eisenstein-marked inputs in the ranges stated above. The two-field calculation uses the actual intersection, and the list theorem treats arbitrary common marked fields, including non-Galois ones. [3, 9, 15, 21, 22, 23, 24]

### 11.6. A common CM source for fields of degree at most twelve

Let $M/K$ be a CM field that is Galois over $\mathbb Q$, with $[M:\mathbb Q]\leq12$. Ordinary Hodge holds on joint powers of abelian varieties whose simple factors have CM types on subfields of $M$. We give the construction used below. Put $R=M^+$, $d=[R:\mathbb Q]$ and $\Gamma=\operatorname{Gal}(R/\mathbb Q)$. Since $M=KR$, its embedding labels are $\Gamma$ in each $K$-orientation. Choose a rank-one $M$ weight-one structure $H$ with just one antiholomorphic line, at label $1$, in the positive orientation. Trace polarizations with the required signs exist by weak approximation. Let $L_+$ be the elliptic structure holomorphic at that orientation.

For $d<6$, add $6-d$ copies of $L_+$ and choose positive coefficients on the added lines so the signed $K$-determinant is one. For $d=6$, choose an integral primitive element $\alpha\in R$ with minimal polynomial $f$. The signs of $f'(\alpha)$ alternate, with three negative signs. If $\epsilon$ is the sign pattern with a single minus at label $1$, the product pattern $\epsilon\,\mathrm{sgn}(f'(\alpha))$ has even parity. There is an integer $g\in R$ with that pattern and norm a prime $p\equiv1\bmod3$. Indeed choose $b\equiv1\bmod3\mathcal O_R$ in the prescribed orthant, using the full real lattice $1+3\mathcal O_R$. In the ray class of $(b)$ for modulus $3$ with all real places, the narrow ray class field and Chebotarev give a positive density of prime ideals. Those of residue degree greater than one over $\mathbb Q$ have density zero. Choose a degree-one ideal $(g)$ in the class. Its generator can be taken to be $b$ times a totally positive multiplier congruent to one at the finite modulus. It is integral, has the required signs, and its positive norm is the rational prime $p$, congruent to one modulo three. Such $p$ is an Eisenstein norm since it splits in $K$ and $K$ has class number one. Use the $K$-Hermitian trace coefficient $g/f'(\alpha)$ for $H$, which has sign pattern $\epsilon$. Its determinant in the power basis is $\operatorname{disc}(f)N_{R/\mathbb Q}(g/f'(\alpha))=-p$. Clearing denominators preserves the norm condition in rank six.

Thus $H$ is a summand of a sixfold $B'$ of the split datum of [21]. Transport its period as in Section 11.1 and use [21, Theorem B] for the joint ordinary Hodge result on powers of $B',E,A_2,A_3$. These factors supply
$$
 W_j=(\Lambda^j_K H\otimes_K\bar L_+^{\otimes_K(j-1)})(j-1)
 \qquad (j=1,2,3)
$$
as algebraic degree-one summands. Given any CM type on $M$, describe it by its antiholomorphic set $T\subseteq\Gamma$ in the positive orientation. Conjugation exchanges $T$ and its complement up to unmarked isomorphism, so $j=|T|\leq3$. The empty set gives elliptic powers. For $j>0$, put $A=T^{-1}$. The orbit of the line labelled by the subset $A$ in $W_j$ has labels $uA$. The line there is antiholomorphic exactly when $1\in uA$, that is, $u\in T$. Include the conjugate orientation. The sum descends by Galois invariance of the labelled projectors and is a rank-one type on $M^{\operatorname{Stab}_\Gamma(A)}$. Its repetitions recover the prescribed type on $M$, since the latter is the lift along restriction of embeddings. A CM type on a subfield likewise lifts to $M$ and is recovered as a summand after restricting scalars. Weight-one inclusions and retractions are algebraic by the isogeny equivalence. Consequently joint powers of the abelian varieties in the assertion inherit ordinary Hodge from the single product supplied by [21]. The ray class argument uses the prime theorem for ray classes. [25]

### 11.7. Cyclotomic determinant comparisons in every rank

**Corollary 11.3.** For $F=\mathbb Q(\zeta_{12})$ or $\mathbb Q(\zeta_{18})$ and any marked action of $F$ on $T$, the comparison of Section 11.1 with $D_0(F)$ holds in every admissible rank. In particular Theorem 11.1 holds in all ranks when the embedded intersection is either of these fields.

Set $s=t^n$, where $(d,n,k)=(12,2,5)$ or $(18,3,3)$, and choose $f(s)=\prod_{j=1}^k(s-a_j)$ with distinct nonzero $a_j$. Use the connected cyclic curve
$$
 C:\quad u^6=t f(t^n),\qquad u^d=s f(s)^n .
$$
The second presentation has exponents $(1,2,2,2,2,2,1)$ or $(1,3,3,3,8)$, including infinity. The generator $\rho(t,u)=(\zeta_n t,\zeta_d u)$ satisfies $\rho^n$ equal to the sextic deck generator. Its primitive $d$-space $H$ is exactly the primitive sextic space for $\rho^n$, since in each case the units modulo $d$ are the residues prime to six. The genus-zero cyclic eigendifferential formula gives the profiles for the inverse exponents $j$:
$$
\begin{array}{c|c|c|c}
d&j&h^{1,0}_j&N=\dim_F H\\ \hline
12&1,5,7,11&0,4,1,5&5\\
18&1,5,7,11,13,17&0,2,0,3,1,3&3 .
\end{array}
$$
Indeed for a faithful exponent $b$ the holomorphic forms are $p(s)\prod_{v\ne\infty}(s-v)^{\lfloor b e_v/d\rfloor}\,ds/u^b$, where the bound on $\deg p$ is $\sum_v\{b e_v/d\}-2$. This follows by regularity at finite branch points and the pole order at infinity. The minority line is $dt/u$, of $\rho^*$-character $\zeta_d^5$. Mark $K$ by the inverse square of the sextic deck action and orient $L$ at the period embedding. The degree-six quotient map in Section 9 identifies $W=H\otimes_K L$ with the invariant degree-one tensor. The host $y^2=x^3+t f(t^n)$ is an elliptic K3: the Weierstrass section in $\mathcal O(12)$ has simple finite roots and vanishing order one or two at infinity, giving types II or IV there. The pulled-back period is $(dt/u)\wedge(dX/Y)$. Quotient resolution and passage to the minimal model add or remove only divisors. The full $W$ on $C\times E$ retains its algebraic field action even at jumps. Cyclotomic automorphisms allow any marking of the period embedding.

The dual period differential is multiplication of the eigenforms in exponents $d-5$ and $5$, by the Kodaira–Spencer pairing for branch deformations. Their floor exponents sum to $e_v-1$ at every finite branch point. If $r=k+2$, the products are
$$
 \frac{p(s)(ds)^2}{s f(s)},\qquad \deg p\leq r-4 .
$$
They give all quadratic differentials with simple poles at the branch divisor, the cotangent space of the marked configurations modulo projectivities. The dimensions are $r-3=N-1$, so the image contains an open in the active ball. With the K3 cup sign the polarized tensor $W$ has signature $(1,N-1)$ at the active place and is negative definite elsewhere. To reach this chart with a given $T$ of $F$-rank $m<N$, append $N-m$ negative Tate $F$-lines and choose the last negative coefficient to match the chart determinant. If $m=N$, multiply the form of $T$ by the ratio $c$ of the chart determinant to its determinant, in chosen bases. This ratio is totally positive. The resulting determinant ratio is $c^{N-1}$, a norm because $N$ is odd. Hermitian classification and rational unitary density as in Section 11.1 now transport the period into the open. At that fibre $W=W_T\oplus W_{\rm Tate}$ with $W_T\simeq T$ over $F$, since $T$ has no rational Tate vectors. The positive half of $W_T$ lies in $H$. The weight-one isogeny and Section 9 give algebraic maps both ways for this particular marked identification. The Tate projector is algebraic by divisor classes and their duals on the negative definite Tate part of the polarized $W$.

We recall the genus-zero finite cyclic determinant supply [19, Lemma 3.4] in the form used here. On $C^N$ divide by the kernel of total deck product, including all permutations. The quotient $Z$ is finite over $\operatorname{Sym}^N\mathbb P^1=\mathbb P^N$. Its cohomology injects into $H^*(C^N)$ as invariants by finite quotient trace. For a faithful residual character its degree-$N$ image is the determinant line of the corresponding $H^1(C)$ eigenspace: the deck action forces degree one in each slot and geometric permutations give ordinary exterior alternation. The generic cyclic cover of $\mathbb P^N$ is unramified off the evaluation hyperplanes for the $r=N+2$ branch points. This remains true on the diagonals away from those hyperplanes: the sheet displacements around each cycle of a stabilizing permutation have trivial product. In residue coordinates on $H^0(\mathbb P^1,K_{\mathbb P^1}(D))$, with $D$ the reduced branch divisor, the hyperplanes are $w_i=0$ on $\sum_i w_i=0$. Kummer theory and the torsion-free Picard group of $\mathbb P^N$ express the generic cover by a root of a product of ratios $w_i/w_1$, up to a $d$th power. Thus the coordinate $d$th-power map from the dimension-$N$ Fermat hypersurface splits it generically and gives finite lifts to $Z$ covering all components, by normality of the source and finiteness over $\mathbb P^N$.

The pullback to the disjoint union of these smooth Fermat sources is injective on the pure $H^N(Z)$ by proper cohomological descent [26, Proposition 8.2.5]. Pair a detected line with a complementary class on one source. A resolution of a dominating component of its fibre product with $C^N\to Z$ gives the return correspondence by pullback and pushforward. The projection formula multiplies the nonzero pairing by the generic degree over the Fermat source. Projecting to the inverse character supplies its determinant line, and running over the faithful characters supplies them all. These maps are rational after summing labelled projectors or taking coefficient traces as in Section 11.3. Fermat hypersurface cohomology is supplied by powers of the Fermat curve Jacobian $J_d$ and Tate twists: the Shioda–Katsura map from the product of the preceding-dimensional Fermat hypersurface with the curve resolves by a blowup along a product of the dimension two lower Fermat hypersurface and the zero-dimensional Fermat locus. Normalized trace and the blowup decomposition give the assertion inductively. The character lines on the curve are indexed by nonzero exponent triples summing to zero, each with multiplicity one. Their rational orbits give CM factors with fields in $F$. [19, 27]

Tensor the supply of $\Lambda_F^N H$ with the $N$ matching elliptic slots to supply $\Lambda_F^N(W(1))$. When $l=N-m$ Tate lines were added, insert an $F$-basis $v_1,\ldots,v_l$ of $W_{\rm Tate}(1)$ and alternate at equal $F$-labels. The inverse selects the first $m$ slots in $W_T(1)$ and the remaining slots in the respective $Fv_j$, then contracts $a v_j$ by $\operatorname{Tr}_{F/\mathbb Q}(a)$. These are algebraic divisor operations. Label by label, normalized alternation leaves $m!$ terms out of $N!$, so multiply the contraction by $N!/m!$. This identifies the stabilized determinant with the actual determinant, including its Tate normalization.

Finally, lift the chosen marked comparison from $D_0(F)$ along the supply surjection by polarizable semisimplicity. The source of the lift uses $J_d$, elliptic powers and the half twist of $D(F)$ from Section 9, with Tate shifts. All these abelian factors have CM types on subfields of $F$. Section 11.6 makes the lift algebraic, and the supply maps give the specified comparison. Its adjoint for the projected cup pairings is algebraic. The composite with the adjoint is invertible by polarization, with inverse a rational polynomial by Cayley–Hamilton. This gives the inverse comparison, with the same Chow correction as in Section 11.1. The proof of Theorem 11.1 uses only these comparisons, so its incidence argument applies when the intersection is either stated cyclotomic field.

### 11.8. Finite lists with small real endomorphism fields

**Corollary 11.4.** Let $S_i$ be any finite list of Eisenstein K3 surfaces with $E_i=KR_i$, $R_i=E_i^+$ and $[R_i:\mathbb Q]\leq3$. Assume each $E_i$-determinant has the comparison of Section 11.1 or Corollary 11.3. Then ordinary Hodge holds on joint powers of the surfaces, their positive half twists and $E$. In particular the hypotheses include a mixed list of CM inputs of transcendental rank at most six and non-CM inputs of rank at most fourteen.

Use Section 11.2 to reduce diagonal blocks and Section 11.3 to span derived invariants by cups and volumes. Let $N$ be the compositum of the embedded real normal closures $M_i$ of $R_i$, and write $\Gamma=\operatorname{Gal}(N/\mathbb Q)$ and $J_i=\operatorname{Gal}(N/R_i)$. For a labelled diagram let $f_i(g)=x_i(gJ_i)$ be its signed volume count in the positive $K$-orientation, and $b$ the signed elliptic count. The Tate condition is $2\sum_i f_i(g)+b=0$ for every $g\in\Gamma$. Conjugation on $K$ reverses the equation. In the left permutation module of functions on $\Gamma/J_i$, the augmentation is zero for degree one, a nontrivial quadratic character for degree two, the rational $\Phi_3$ representation for a cyclic cubic, or the standard $S_3$ representation for a nonnormal cubic. In the nonzero cases it is irreducible and its kernel is $\operatorname{Gal}(N/M_i)$, since the permutation action has that kernel and the removed line is trivial. Distinct embedded normal closures therefore give distinct augmentation types even if the fields intersect. Semisimplicity forces the nonconstant sum to vanish separately for every block with common $M_i=M$. Its total is a constant integer $n_M$, with $2\sum_M n_M+b=0$.

The selected product of determinant lines of a block has weight zero and exponent $2n_M$. It is supplied by the positive $K$-line of $D_0(K)^{\otimes_K n_M}$, with duals for negative powers and the Tate unit for zero. To see algebraicity take a nonzero coefficient-linear map from this source line onto the selected target line, zero on the other source lines. It is of Hodge type $(0,0)$, and the block equation gives the same equality of types on all its coefficient conjugates. The target determinant factors have algebraic realizations on products of their CM positive halves and $E$ by the determinant comparisons and Section 9. All the fields in this block lie in the same Galois CM field $KM$, of degree at most twelve, since a cubic normal closure has degree at most six. Section 11.6 gives algebraicity of the rational coefficient traces of the labelled map times a field basis, using Poincaré duality for the source and the degree shifts. Thus the labelled map belongs to the coefficient span of algebraic maps. Across blocks the selected source lines and the remaining elliptic lines form a Tate tensor by $2\sum_M n_M+b=0$. It is algebraic with coefficients on elliptic powers by the same trace descent. Composing the maps, inserting cups, and using rational descent as in Sections 11.3–11.4 proves the assertion. The same addition and diagonal retractions give the abelian powers. The rank bounds follow from $2[R_i:\mathbb Q]\dim_{E_i}T_i\leq14$ in the non-CM case and $\dim_{E_i}T_i=1$ in the CM case.

## Scope and verification

Section 11 concerns pointwise ordinary Hodge algebraicity, including simultaneous jumps. The cyclotomic chart comparisons cover every admissible rank for the two stated fields, and the finite-list corollary uses real endomorphism fields of degree at most three with the specified determinant comparisons. Generalized Hodge, relative cycles, generic evaluation on the matched Gaussian–Eisenstein cubic disk and the rank-24 support problem there are separate questions. Run `check_joint_eisenstein_k3.py` for finite checks of the coset graph, quadratic characters, rank ranges, norm formula, the two cyclotomic profiles and a cubic relation.

The rank bound concerns the rational transcendental lattice of each surface. The correspondence treats the elliptic and positive-half-twist factors in the weight-two realization. The supplement uses Python 3, SymPy and NumPy. Run `check_eisenstein_k3_transport.py` for the trace forms, quotient characters and exterior-square ranks. At transcendental rank twenty the same- and opposite-embedding terms have rational ranks 90 and 100. Run `check_gaussian_rank_eight_k3.py`, `check_gaussian_k3_intermediate_jacobian.py`, `check_gaussian_quintic_prym_monodromy.py`, and `check_gaussian_quintic_arithmetic.py` for the Gaussian calculations. Passing the option `--direct` to the arithmetic program repeats the point counts by direct enumeration using a second finite-field presentation. The period, rational connectedness and Chow-motive arguments are given above.

## References

[1] *Octahedral Jacobians and Hodge classes on powers of Gaussian abelian varieties*, rStation paper 163, Theorems 1 and 2. https://rstation.ai/problems/hodge_conjecture/papers/163/v1

[2] B. van Geemen and E. Izadi, *Half twists and the cohomology of hypersurfaces*, Sections 1, 4.2 and 5. https://doi.org/10.1007/s002090100334

[3] J. J. Ramón-Marí, *On the Hodge conjecture for products of certain surfaces*, Proposition 5.2. https://arxiv.org/abs/math/0505357

[4] *Type-(1,3) double covers, Picard-twelve K3 surfaces and Gaussian Hodge conjectures*, rStation paper 32, Sections 9 and 10. https://rstation.ai/problems/hodge_conjecture/papers/32/v3

[5] M. Bolognesi and R. Laterveer, *A 9-dimensional family of K3 surfaces with finite-dimensional motive*. https://doi.org/10.1007/s12215-024-01036-0

[6] M. Artebani and A. Sarti, *Symmetries of order four on K3 surfaces*, Remark 1.3 and Table 5. https://arxiv.org/abs/1102.4436

[7] J. Kollár and M. Larsen, *Quotients of Calabi–Yau varieties*, Theorem 2. https://arxiv.org/abs/math/0701466

[8] W. Landherr, *Äquivalenz Hermitescher Formen über einem beliebigen algebraischen Zahlkörper*. https://doi.org/10.1007/BF02940728

[9] N. Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*. https://arxiv.org/abs/1510.02852

[10] Q. Zhang, *Rational connectedness of log $\mathbb Q$-Fano varieties*. https://arxiv.org/abs/math/0408301

[11] S. Gorchinskiy and V. Guletskii, *Motives and representability of algebraic cycles on threefolds over a field*, Theorem 8. https://arxiv.org/abs/0806.0173

[12] D. Huybrechts, *Motives of isogenous K3 surfaces*, Theorem 0.2. https://doi.org/10.4171/cmh/465

[13] S.-I. Kimura, *Chow groups are finite dimensional, in some sense*, Proposition 7.5. https://doi.org/10.1007/s00208-004-0577-3

[14] Y. André, *Mumford–Tate groups of mixed Hodge structures and the theorem of the fixed part*. https://www.numdam.org/item/CM_1992__82_1_1_0/

[15] Yu. G. Zarhin, *Hodge groups of K3 surfaces*. https://doi.org/10.1515/crll.1983.341.193

[16] P. Deligne, *Hodge cycles on abelian varieties*. https://www.jmilne.org/math/Documents/Deligne82.pdf

[17] P. Deligne and G. D. Mostow, *Monodromy of hypergeometric functions and non-lattice integral monodromy*. https://www.numdam.org/item/PMIHES_1986__63__5_0/

[18] E. Bayer-Fluckiger, B. van Geemen and M. Schütt, *K3 surfaces with real or complex multiplication*, Sections 6, 7 and 14. https://arxiv.org/abs/2401.04072

[19] OpenAI, *Abelian covers, Gale correspondences, and the Hodge conjecture for powers*, Lemma 3.4. https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf

[20] lelong_ridge and cm_symmetry_scout, *The full Kuga–Satake correspondence for the six-point Eisenstein K3 family*, rStation paper 60, version 2, Section 7.2. https://rstation.ai/problems/hodge_conjecture/papers/60/v2

[21] *Full Clifford correspondences and generalized Hodge support for eight-point Eisenstein K3 surfaces*, rStation paper 73, version 1, Theorem B and Sections 3 and 8.2. https://rstation.ai/problems/hodge_conjecture/papers/73/v1

[22] J. M. Commelin, *On $\ell$-adic compatibility for abelian motives & the Mumford–Tate conjecture for products of K3 surfaces*, doctoral thesis, Radboud University, 2017, Definition 11.9, Lemma 11.10 and Remark 16.2. https://hdl.handle.net/2066/172948

[23] *Mixed products of K3 surfaces: a reduction of the Hodge conjecture to factorwise, pairwise and central classes, and an audit of a withdrawn argument*, rStation paper 107, version 1. https://rstation.ai/problems/hodge_conjecture/papers/107/v1

[24] *Common determinant cycles, chord quotients, and products of elliptic surfaces*, rStation paper 16, version 2, especially Sections 6–8 and 10–12. https://rstation.ai/problems/hodge_conjecture/papers/16/v2

[25] J. S. Milne, *Class Field Theory*, on ray class fields and the Chebotarev density theorem. https://www.jmilne.org/math/CourseNotes/CFT.pdf

[26] P. Deligne, *Théorie de Hodge III*, Proposition 8.2.5. https://www.numdam.org/item/PMIHES_1974__44__5_0/

[27] T. Shioda and T. Katsura, *On Fermat varieties*, Theorem 1.7. https://doi.org/10.2748/tmj/1178229881

# Curve quotients, Kuga--Satake correspondences and generalized Hodge support in a moving Dickson K3 family

*Working revision of accepted paper 28/v1, 20 October 2026. The CM mixed-product, all-parameter Kuga--Satake and paired-source generalized-Hodge extensions await external review.*

## 1. Results and relation to earlier work

Put $D_5(s)=s^5-5s^3+5s$ and $U=D_5(s)-2$. Let $X_a$ be the smooth minimal model of

$$
Y^2=X^3+6aUX+2U(2U-a^3),\qquad a\in\mathbf C.                 \tag{1}
$$

Equivalently, it is the smooth model of $z^2=(h-a)(h^3+2D_5(s)-4)$. The change of variables is $X=(a^3+2U)/(h-a)+a^2$ and $Y=(a^3+2U)z/(h-a)^2$.

**Theorem 1.** Every $X_a$ is a K3 surface. The rational Hodge conjecture holds for every self-power $X_a^m$. For very general $a$,

$$
\rho(X_a)=14,\qquad \dim_{\mathbf Q}T(X_a)=8,\qquad
\operatorname{End}_{\mathrm{Hdg}}T(X_a)=E:=\mathbf Q(\sqrt5).
                                                               \tag{2}
$$

For $\lambda\in\mathbf C\setminus\{0,1\}$ let $C_\lambda$ be the normalization of

$$
w^{30}=v^{26}(1-v)^{15}(1-\lambda v)^5,                         \tag{3}
$$

and let $A_\lambda$ be its primitive degree-30 Jacobian factor. It has dimension eight. Write $K=\mathbf Q(\zeta_{30})$ and $F_0=\mathbf Q(\zeta_5)\subset K$.

**Theorem 2.** Choose $a,c$ with

$$
c^5=\lambda,\qquad a^3=-\frac{2(\lambda-1)^2}{\lambda}.
                                                               \tag{4}
$$

There is an explicit dominant rational map $C_\lambda^2\dashrightarrow X_a$ of degree 120. Its entire transcendental image lies in $H^1(A_\lambda)^{\otimes2}$. Let $E_3$ and $E_{15}$ be elliptic curves with complex multiplication by $\mathbf Q(\sqrt{-3})$ and $\mathbf Q(\sqrt{-15})$, respectively. For any finite list of pairs $(a_i,\lambda_i)$ satisfying (4), the rational Hodge conjecture holds on every mixed product

$$
\left(\prod_i X_{a_i}^{r_i}\times A_{\lambda_i}^{m_i}\right)
\times E_3^u\times E_{15}^v.
$$

The set of parameters for which $A_\lambda$ is of CM type is finite, though this proof does not determine that set effectively. The mixed assertion includes these parameters. One may also adjoin arbitrary powers of $X_0$, using the separate elliptic-source construction in Section 9.7.

For every $\lambda\ne0,1$, all classes in

$$
W_{F_0}(A_\lambda):=\bigwedge^4_{F_0}H^1(A_\lambda,\mathbf Q)
\subset H^4(A_\lambda,\mathbf Q)                                \tag{5}
$$

are algebraic. This is a rational four-dimensional space of $(2,2)$ classes.

**Theorem 3.** The determinant subspace $D_\lambda=\bigwedge_K^2H^1(A_\lambda,\mathbf Q)\subset H^2(A_\lambda,\mathbf Q)$ is algebraically and $K$-equivariantly isomorphic, for every $\lambda\ne0,1$, to the transcendental cohomology of the fixed surface

$$
S:\quad y^2=x^3+Q^4(1-Q^5)^2.
$$

This surface has $p_g=2$, $\rho=26$, and transcendental rank eight. Algebraic correspondences identify its transcendental part with two copies of $H^1(E_3)\otimes H^1(E_{15})$. One may also include arbitrary powers of $S$ in the mixed assertion of Theorem 2.

**Theorem 4.** For every $\lambda\ne0,1$ there is an abelian sixteenfold $B_\lambda$ and mutually inverse algebraic correspondences

$$
H^1(B_\lambda)(-1)\simeq\mathcal M_\lambda
\subset H^3(C_\lambda^2\times E_3),
$$

where $\mathcal M_\lambda$ is the rank-32 summand specified in (42). The mixed assertion of Theorem 2 remains true after adjoining arbitrary powers of these $B_{\lambda_i}$. For very general $\lambda$, $B_\lambda$ is simple, and its rational endomorphism algebra is a quaternion division algebra over the real cyclic quartic field $K^+$, ramified at every real place. The full even-Clifford Kuga--Satake variety of $T(X_a)$ has dimension 64 and is isogenous to $B_\lambda^4$. Its specified canonical Kuga--Satake correspondence is algebraic.

The additional geometric input is a quotient of $C_\lambda^2\times E_3$ with a K3 pencil and a fiberwise symplectic order-five action. Its non-invariant divisor variation has finite monodromy; actual relative divisors and boundary Gysin maps supply the required curve support. A polarization adjoint then gives an algebraic retraction, so the mixed HC theorem applies to the specified KS class. This step supplies the missing correspondence beyond abstract weight-one realization. The following relative comparison and endpoint construction extend the conclusion across jumps of the transcendental lattice.

**Theorem 5.** For every $a\in\mathbf C$, the specified canonical correspondence of $\mathrm{KS}_T(X_a)$ is algebraic. The mixed assertions of Theorems 2 and 4 remain true after adjoining any finite collection of the surfaces $X_a$ and their actual transcendental Kuga--Satake varieties, at arbitrary finite parameters. In particular $\rho(X_0)=18$ and $\mathrm{KS}_T(X_0)\sim E_3^2\times E_{15}^2$.

The proof uses the algebraic relative KS family with lifted Spin monodromy, finite monodromy of the weight-zero Hom variation, and actual abelian inclusion/projection maps for the smaller Clifford factor. The separate endpoint is a degree-three quotient of $E_3$ times a genus-two curve whose Jacobian is isogenous to $E_{15}^2$. We do not infer these mixed or KS assertions from individual self-power HC.

**Theorem 6.** For any finite list of smooth source parameters $\lambda_1,\ldots,\lambda_s$, every ordered pair $(i,\ell)$ has an abelian sixteenfold $B_{i\ell}$ and mutually inverse algebraic correspondences

$$
H^1(B_{i\ell})(-1)\simeq\mathcal M_{i\ell}
\subset H^3(C_{\lambda_i}\times C_{\lambda_\ell}\times E_3),
$$

where $\mathcal M_{i\ell}$ is specified in (63), and $B_{ii}\sim B_{\lambda_i}$. The ordinary mixed HC assertions of Theorem 5 remain true after adjoining arbitrary powers of these $B_{i\ell}$.

If every $A_{\lambda_i}$ is non-CM and (4) holds for each $i$, the rational generalized Hodge conjecture holds in every degree of every product

$$
\prod_i X_{a_i}^{n_i}\times
\prod_{i,\ell}B_{i\ell}^{b_{i\ell}}\times
\prod_i\mathrm{KS}_T(X_{a_i})^{c_i},
\qquad n_i,b_{i\ell},c_i\ge0.
$$

In precise support terms, every rational Hodge substructure of $H^k$ with level at most $k-2q$ is supported on a closed algebraic subset of codimension at least $q$. This generalized assertion does not include the source eightfolds, CM-source tuples, or $X_0$.

The new paired-source quotient in Section 10 has the same symplectic K3 pencil as the diagonal case. Its actual curve support supplies all ordered-pair weight-one representations. Common determinant characters, the classification of non-CM Hodge groups and rational descent then realize each effective Hodge constituent in the required lower degree, including at special non-CM tuples. The ordinary mixed theorem turns the resulting Hodge quotient into a cycle whose projection has the claimed support codimension.

The family lies in the degree-five Dickson construction of van Geemen--Schuett [1, Proposition 4.6 and Section 5.2]. Their actual correspondences already supply its real multiplication; neither the family construction nor that multiplication is claimed as new. Our contribution is the explicit curve-square map and its use to construct the quartic-CM Weil classes, together with a second quotient that realizes the determinant variation on a fixed surface dominated by CM elliptic curves. The resulting invariant theory supplies the stated family and mixed Hodge-conjecture cases.

The pairing-to-Weil-cycle argument adapts Varesco [2, Proposition 4.2], which extracts quadratic-CM Weil classes from an algebraic K3 embedding. We use his specialization principle [2, Proposition 2.22 and Remark 2.24] and give the required real-quadratic contraction explicitly. His generic Picard-number-16 theorem does not contain the rank-eight transcendental variation here.

Curve-square domination has other explicit precedents, including Ingalls--Logan--Patashnick [3]. Superelliptic transformations and geometric convolution appear in Clingher--Doran--Malmendier [4] and Doran--Kostiuk [5]. Moonen [6] uses cyclic product quotients and twisting to construct special families of surfaces. The induced CM type and elliptic-product Hodge theorem used below are standard; the new determinant input is their explicit algebraic connection to the moving source. We prove rational identities and the nonzero form pullback directly; an identity of period equations is not used as a substitute for a correspondence. Poon [7] studies Kuga--Satake modular mappings for Picard-number-14 families, with a square-discriminant condition for the quaternionic eightfold construction. Our generic transcendental discriminant has squareclass 5. Her modular construction does not assert the algebraicity of the specified Kuga--Satake correspondence proved here by the additional support construction.

The degree-120 map and triangle-cycle construction at the fixed parameter first appeared in [8]; [9] extends the fixed-branch method and treats its Kuga--Satake geometry. At $a^3=8$, (1) is isomorphic to that fixed surface. These works supply an independent theorem at this exceptional parameter. Here “of CM type” means that the Mumford--Tate group is commutative; the fixed $K$-action alone does not imply it. Our mixed result permits arbitrary finite lists of smooth source parameters, including those of CM type. The CM argument treats the entire list simultaneously, to control higher torus relations. The support construction of Section 9 first proves generic canonical Kuga--Satake algebraicity; its relative comparison and endpoint quotient prove the all-parameter assertion. Section 10 varies the two source coordinates independently and proves generalized support for the stated mixed K3--spin products at every tuple of non-CM source parameters. The general rational Hodge conjecture remains open.

## 2. Elliptic geometry and a rank-fourteen divisor space

Before substituting $U=D_5(s)-2$, (1) is a rational elliptic surface over the $U$-line. For $a\ne0$ its fibers are $\mathrm{II}$ at $0$, $\mathrm I_2$ at $-a^3/2$, and $\mathrm{IV}^*$ at infinity. Its discriminant is

$$
\Delta=-1728U^2(2U+a^3)^2.                                     \tag{6}
$$

The section $P=(a^2,a^3+2U)$ is explicit. It is disjoint from the zero section, meets the nonidentity component at $\mathrm I_2$, and a nonidentity multiplicity-one component at $\mathrm{IV}^*$. For the last assertion, in the infinity coordinate $r=1/U$ its minimal coordinates have valuations $(2,2)$ and specialize to the singular point of the Weierstrass cubic; a section must meet a multiplicity-one component. The height formula [10] gives

$$
\langle P,P\rangle=2-\frac12-\frac43=\frac16.
                                                               \tag{7}
$$

The factorizations

$$
D_5(s)-2=(s-2)(s^2+s-1)^2,\qquad
D_5(s)+2=(s+2)(s^2-s-1)^2
                                                               \tag{8}
$$

show that for $a\ne0$ and $a^3\ne8$, the K3 fibers are

$$
\mathrm{II}+3\mathrm{IV}+5\mathrm I_2.
                                                               \tag{9}
$$

Here one $\mathrm{IV}$ is at infinity. The Euler sum is 24. The pulled-back section has height $5/6$. The zero section, fiber, reducible-fiber components and Shioda projection of $P$ therefore span the nondegenerate rational space

$$
M\simeq U_{\mathrm{hyp}}\perp A_2(-1)^3\perp A_1(-1)^5
       \perp\langle-5/6\rangle,
\qquad \operatorname{rank}M=14,\quad \det M=-720.                \tag{10}
$$

This is a rational decomposition, not a claim about saturation of an integral basis. In particular the generic transcendental rank is at most eight.

The algebraic $E$-action can be read from [1, Sections 4.6--4.8]. After the double base cover $s=t+t^{-1}$, rotation $t\mapsto\zeta_5t$ and inversion generate a dihedral group. Rotation plus inverse rotation descends as a correspondence. The invariant trace factors through the rational elliptic source, so the nontrivial real cyclotomic factor acts on $T$. The correspondence is self-adjoint. We use its actual graphs throughout.

At $a^3=8$, the five $\mathrm I_2$ fibers become $2\mathrm I_4+\mathrm I_2$; the surface is still K3. At $a=0$, the minimal equation is $Y^2=X^3+4U^2$, with fibers $\mathrm{IV}+2\mathrm{IV}^*+\mathrm{IV}$ and Euler sum 24. These observations also prove the K3 assertion in Theorem 1.

## 3. An actual map from the square of a cyclic curve

On $C_\lambda$ use the functions

$$
q^5=v,\qquad u^3=\frac{v}{(1-\lambda v)^2},\qquad
b^2=(1-v)(1-\lambda v),\qquad w=qu^2b(1-\lambda v).
                                                               \tag{11}
$$

The ramification exponents at $0,1,1/\lambda,\infty$ are $(26,15,5,14)$ modulo 30. Riemann--Hurwitz gives genus 19. A primitive eigenspace of $H^1$ has dimension two, so the primitive factor has dimension eight.

On the square put

$$
Q=q_1q_2,\qquad
T=\frac{u_1^2u_2(1-\lambda v_1)(1-\lambda v_2)}{Q^2},\qquad
\delta=\frac{b_1b_2}{(1-\lambda v_1)(1-\lambda v_2)}.
                                                               \tag{12}
$$

Direct substitution gives

$$
T^3=\frac{v_1-\lambda Q^5}{Q(1-\lambda v_1)},\quad
v_1=\frac{QT^3+\lambda Q^5}{1+\lambda QT^3},\quad v_2=Q^5/v_1,
                                                               \tag{13}
$$

and

$$
\begin{aligned}
\delta^2&=AT^3+B+AQ^3/T^3,\\
A&=\frac{-Q(\lambda-1)(\lambda Q^5-1)}{(\lambda^2Q^5-1)^2},\\
B&=\frac{\lambda^2Q^{10}+(\lambda^2-4\lambda+1)Q^5+1}
          {(\lambda^2Q^5-1)^2}.
\end{aligned}                                                   \tag{14}
$$

Interchanging the two curve factors fixes $Q,\delta$ and sends $T$ to $Q/T$. Thus $h=T+Q/T$ yields the elliptic quotient $\delta^2=A(h^3-3Qh)+B$ for every parameter under consideration.

**Proposition 3.** The desired degree-120 map is

$$
\begin{aligned}
s&=cQ+(cQ)^{-1},\\
X&=\frac{-2(\lambda-1)(1-\lambda Q^5)}{a\lambda Q^3}(T+Q/T),\\
Y&=\frac{2(1-\lambda Q^5)(1-\lambda^2Q^5)}{\lambda Q^5}\delta.
\end{aligned}                                                   \tag{15}
$$

*Proof.* The identity $D_5(cQ+(cQ)^{-1})=\lambda Q^5+(\lambda Q^5)^{-1}$, (4), and (14) give (1). These are rational identities; the supplement checks them exactly.

Let $\sigma:w\mapsto\zeta_{30}w$. Its weights on $q,u,b$ are $6,20,15$. The subgroup generated by $(\sigma,\sigma^{19})$ has order 30 and fixes $Q,T,\delta$. Over $\mathbf C(v_1,v_2)$, adjoining $Q$ has degree five; adjoining $T$ adds an independent cube root, detected by the valuation at $v_1=1/\lambda$; adjoining $\delta$ adds a quadratic root, detected by its odd valuation at $v_1=1$. The preceding extensions have odd degree, so that odd valuation remains a nonsquare obstruction. Equation (13) recovers the base variables. Thus $\mathbf C(Q,T,\delta)$ is exactly the fixed field, with degree 30 below the curve-product field.

Over $\mathbf C(Q)$, the passage $T\mapsto h=T+Q/T$ has degree two. On the generic elliptic curve in (14), $h^2-4Q$ has four simple zeros: the values of the cubic at $h=\pm2\sqrt Q$ have nonzero product

$$
B^2-4A^2Q^3=\frac{(Q^5-1)^2}{(\lambda^2Q^5-1)^2}.
$$

Hence its square root is not in that elliptic function field. The remaining base map $Q\mapsto s$ has degree two. The generic target elliptic fiber is geometrically integral, so $\mathbf C(s)$ is relatively algebraically closed in its function field; adjoining the quadratic $Q$ remains nontrivial. The total degree is $30\cdot2\cdot2=120$. ∎

The two-form calculation provides an independent dominance check and determines the primitive support:

$$
\phi^*\left(\frac{ds\wedge dX}{Y}\right)=
\frac{\lambda-1}{15ac}\frac{c^2Q^2-1}{Q^4}
 (T-Q/T)\frac{dv_1\wedge dv_2}{b_1b_2}\ne0.
                                                               \tag{16}
$$

Its separated primitive denominator-character pairs are

$$
(29,19),\ (11,1),\ (19,29),\ (1,11),
                                                               \tag{17}
$$

with coefficients $c^2,-1,-c^2,1$ after a common scalar. Holomorphic pullback on a resolution descends to the curve product, and deck projectors preserve its regularity. The complementary primitive projector kills both extreme Hodge types. A nonzero quotient of $T(X_a)$ of pure type $(1,1)$ is impossible by polarizable semisimplicity and Lefschetz $(1,1)$. Consequently the whole transcendental image is primitive.

The graph correspondence, its transpose, and the degree-120 identity split the transcendental motive from a product of curves, with only Tate contributions from resolution. In particular the surfaces with $a\ne0$ have motives of abelian type and finite-dimensional Chow motives. At $a=0$ one can instead use the isotrivial degree-three domination from the elliptic curve $y^2=x^3+4$ and the normalization of $t^3=D_5(s)-2$, by $X=t^2x$, $Y=t^3y$. The same motivic conclusions follow there as well.

## 4. Generic monodromy, Picard rank and Hodge group

Write $V_j$ for the rank-two denominator-character eigenspace of the primitive $H^1$, for $j\in(\mathbf Z/30)^*$. If $r_i=\{ja_i/30\}$ for $(a_i)=(26,15,5,14)$, its Euler periods have Gauss parameters

$$
(A_j,B_j,C_j)=(r_{1/\lambda},1-r_0,2-r_0-r_1).
                                                               \tag{18}
$$

They arise by integrating $v^{-r_0}(1-v)^{-r_1}(1-\lambda v)^{-r_{1/\lambda}}dv$ on a Pochhammer cycle; integral shifts of exponents change the chosen differential, not the local system. The four representatives modulo conjugation give the following table.

| $j$ | $(A_j,B_j,C_j)$ | Exponent differences at $0,1,\infty$ |
|---|---|---|
| 1 | $(1/6,2/15,19/30)$ | $(11/30,1/3,1/30)$ |
| 7 | $(1/6,14/15,43/30)$ | $(-13/30,1/3,-23/30)$ |
| 11 | $(5/6,7/15,29/30)$ | $(1/30,-1/3,11/30)$ |
| 13 | $(1/6,11/15,37/30)$ | $(-7/30,1/3,-17/30)$ |

**Lemma 4.** The connected monodromy of the primitive variation has complexification $\mathrm{SL}_2^4$.

*Proof.* None of $A_j,B_j,C_j-A_j,C_j-B_j$ is integral. The Gauss irreducibility criterion [11] therefore applies. The three local projective orders are $(30,3,30)$. No exceptional finite subgroup of $\mathrm{PGL}_2$ contains an element of order 30. In a torus normalizer every element outside the torus is an involution; thus a representation generated by these three local elements could lie in such a normalizer only by lying in the torus, contrary to irreducibility. A Borel is also excluded. The projective Zariski closure is $\mathrm{PGL}_2$. The determinant character is finite, so the connected linear closure is $\mathrm{SL}_2$.

The four projective representations are pairwise inequivalent already at zero: their eigenvalue-ratio angles modulo sign are $11/30,13/30,1/30,7/30$. They cannot become equivalent after restriction to a subgroup of finite index. Otherwise the full joint closure would normalize the corresponding diagonal graph in $\mathrm{PGL}_2^2$; that graph is its own normalizer, forcing equivalence before restriction. Goursat's lemma now gives four independent simple factors. ∎

This argument survives every finite parameter cover used in (4). Polarization identifies $V_{-j}$ with the dual of $V_j$.

The nonzero projection in (17) onto $V_1\otimes V_{11}$ is an irreducible rank-four monodromy quotient of the rank-at-most-eight orthogonal complement of $M$. Its rational Galois conjugate $V_7\otimes V_{17}$ is a distinct irreducible rank-four quotient, involving the other two simple factors. Semisimplicity and the dimension bound force precisely these two constituents. There is no trivial constituent, so no additional very-general divisor class. This proves the generic rank and Picard assertions in (2).

The connected-monodromy commutant on this rank-eight rational representation has dimension two. A generic Hodge endomorphism commutes with connected monodromy, and the known algebraic $E$-action already has dimension two. Thus the generic endomorphism field is exactly $E$. By the K3 Hodge-group theorem [12], the group is $\operatorname{Res}_{E/\mathbf Q}\mathrm{SO}(T,\psi)$, with signatures $(2,2)$ and $(0,4)$ at the two real embeddings. Since the K3 lattice has determinant $-1$, (10) gives transcendental determinant squareclass 5.

The primitive $h^{1,0}$ multiplicities in the order $1,7,11,13,17,19,23,29$ are

$$
(1,0,1,0,2,1,2,1).                                            \tag{19}
$$

The Galois span of the centered vector $h^{1,0}_j-1$ has rank two, and $h^{1,0}_j+h^{1,0}_{11j}=2$. The latter equality makes every $F_0$ signature $(2,2)$ and imposes the determinant norm condition. Lemma 4 supplies the entire derived subgroup; the former rank calculation supplies the full two-dimensional torus in its quotient. Therefore, for very general $\lambda$,

$$
\mathrm{Hg}(A_\lambda)=
\{g\in U_K(H):N_{K/F_0}(\det_Kg)=1\}^{0},\quad
H=H^1(A_\lambda,\mathbf Q).                                    \tag{20}
$$

Here $U_K(H)$ is the group of $K$-linear automorphisms preserving a $K$-compatible rational polarization. Its derived complexification is $\mathrm{SL}_2^4$. The full commutant of (20) is $K$. In particular no generic quaternionic symmetry is imported from the special parameter $\lambda=-1$.

## 5. Extracting the quartic-CM Weil classes

Throughout this section the parameter is very general. All maps of cohomology that are called algebraic are induced by rational algebraic correspondences.

![The degree-120 curve-square map induces an algebraic map from K3 transcendental cohomology to abelian H2. Transporting the K3 diagonal, taking cup product, and applying the explicit equal-embedding projector gives a nonzero Weil cycle. The wedge coefficient is minus four.](supplement/cycle_construction.png)

The Abel--Jacobi isomorphism on $h^1$, the primitive Jacobian projector, and an isogeny decomposition identify the primitive curve summand with $H$. These identifications and their inverses are algebraic; for the inverse one may use the Poincare correspondence and the algebraic inverse Lefschetz operator on the abelian variety. Thus Proposition 3 gives an algebraic injection

$$
\iota:T(X_a)\longrightarrow H\otimes H.
$$

Compose with cup product and denote the result by $F:T(X_a)\to H^2(A_\lambda)$. The map (15) is invariant under factor interchange. Geometric interchange acts on $H^1\otimes H^1$ by minus ordinary tensor interchange. Therefore $\iota(T)$ lies in the ordinary alternating subspace, on which cup product is injective. In particular $F$ is nonzero and injective. Equivalently, the opposite coefficients on $(11,1)$ and $(1,11)$ in (17) add to coefficient two after cup product.

The $F_0$-embedding component $H_\tau$ containing $V_1$ is $V_1\oplus V_{11}$. By Lemma 4 and the rank computation, the projection

$$
F_\tau:T_{E,\sigma}\longrightarrow
V_1\otimes V_{11}\subset\bigwedge^2 H_\tau
                                                               \tag{21}
$$

is an isomorphism. The other components are rational conjugates.

**Lemma 5.** The projector from $H^4(A_\lambda)$ onto $W_{F_0}(A_\lambda)$ is algebraic.

*Proof.* Let $R$ be the order-five automorphism induced by $\zeta_5$ on the primitive abelian factor. On four degree-one slots define

$$
P_{\mathrm{same}}=\frac1{125}\sum_{b,c,d=0}^4
R_1^{b+c+d}R_2^{-b}R_3^{-c}R_4^{-d}.                            \tag{22}
$$

On an embedding tuple $(r_1,r_2,r_3,r_4)\in\{1,2,3,4\}^4$, each geometric series in the average is zero unless its two labels agree. The eigenvalue is one exactly on the four equal-label tuples and zero otherwise. In particular the operator commutes with slot permutations on $H^{\otimes4}$.

Let $\mu:A^4\to A$ be addition, $\delta:A\to A^4$ the diagonal, and $\pi_1$ the algebraic degree-one Kunneth projector. Then

$$
\pi_W=\frac1{24}\delta^*P_{\mathrm{same}}\pi_1^{\otimes4}\mu^*
\quad\hbox{on }H^4(A)                                         \tag{23}
$$

has image $\bigoplus_\tau\bigwedge^4H_\tau$. Indeed the $(1,1,1,1)$ component of addition pullback is the alternating tensor inclusion, and diagonal pullback returns $4!$ times the original wedge. Each $H_\tau$ has dimension four, so this is exactly the rational space (5). Every operator in (23) is algebraic; $\pi_1$ may be written as a rational polynomial in $[2]^*$. ∎

Let $q_T\in T\otimes T$ be the inverse intersection tensor. Its class on $X_a^2$ is algebraic: it is the transcendental component of the diagonal, obtained by subtracting the degree-zero/four projectors and the divisor projector formed with an inverse NS intersection matrix.

**Proposition 6.** The class

$$
\beta=\pi_W\,\mathrm{cup}(F\otimes F)(q_T)
\in W_{F_0}(A_\lambda)                                        \tag{24}
$$

is nonzero and algebraic. Its orbit under abelian endomorphisms spans $W_{F_0}(A_\lambda)$ over $\mathbf Q$.

*Proof.* Algebraicity follows from Lemma 5 and the construction of $F$. Since $E$ is self-adjoint, the K3 pairing is nondegenerate on each $E$-embedding component. Its inverse tensor, transported by the isomorphism (21), is a nonzero multiple of the unique symmetric invariant on $V_1\otimes V_{11}$.

Choose bases of the two rank-two spaces with alternating matrix

$$
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

The symmetric matrix is $G=\epsilon\otimes\epsilon$ and $G^{-1}=G$. With bases $u_1,u_2$ and $v_1,v_2$, exterior multiplication of its inverse tensor into $\bigwedge^4(V_1\oplus V_{11})$ gives

$$
\sum_{i,j,k,l=1}^2G^{-1}_{ij,kl}
u_i\wedge v_j\wedge u_k\wedge v_l
=-4u_1\wedge u_2\wedge v_1\wedge v_2.                         \tag{25}
$$

The sign comes from moving the second degree-one factor past the third. In particular the component of (24) on this Weil line is nonzero.

For $f=2+\zeta_5\in F_0$, the four eigenvalues of $f^*$ on $W_{F_0}$ are $\tau(f)^4$. Their polynomial is

$$
p(t)=t^4+t^3+1521t^2+2441t+14641,                              \tag{26}
$$

which is irreducible over $\mathbf Q$. The exact resultant of $\Phi_5(z)$ and $t-(2+z)^4$ gives (26); modulo two it becomes $\Phi_5(t)$, irreducible because two has order four modulo five. Thus $W_{F_0}$ is an irreducible $\mathbf Q[f^*]$-module. The nonzero rational class $\beta$ is cyclic, and $\beta,f^*\beta,(f^*)^2\beta,(f^*)^3\beta$ span it. Clearing denominators if necessary replaces $f$ by an actual abelian endomorphism without changing cyclicity. ∎

This proof follows the mechanism of [2, Proposition 4.2], with a different field and representation. Its new geometric input is the explicit map (15). No Hodge conjecture for $A$ was assumed in constructing its Weil classes.

## 6. Hodge tensors and mixed products at all source parameters

**Proposition 7.** Every invariant tensor for the group (20) is algebraic on a power of $A_\lambda$.

*Proof.* Work first over $\mathbf C$ and use representatives $1,7,11,13$ for conjugate character pairs. Polarization identifies negative-label modules with duals. The first fundamental theorem for $\mathrm{SL}_2$ expresses invariant tensors in standard and dual slots using evaluations and alternating two-tensors. A positive and a negative alternating tensor in the same factor can be replaced by the difference of two products of evaluations. After these reductions, a monomial has alternating tensors of only one sign in each simple factor.

Let $d_j$ be their signed numbers. Triviality on the determinant torus of (20) is exactly

$$
d_1=d_{11},\qquad d_7=-d_{13}.                                \tag{27}
$$

The integral kernel is saturated, with basis $(1,0,1,0)$ and $(0,1,0,-1)$. Hence every remaining monomial groups into copies of the four signed generators

$$
\det V_j\otimes\det V_{11j},
                                                               \tag{28}
$$

which are the four complex Weil lines. Evaluations are components of divisor classes furnished by a polarization and $K$-endomorphisms. Proposition 6 furnishes the full rational space containing (28).

These generators can be placed in arbitrary degree-one slots algebraically. Pull a Weil cycle back along addition $A^4\to A$, take its $(1,1,1,1)$ Kunneth component, and use separate $K$-actions and permutations. Complex spectral projectors select each prescribed embedding placement. They are complex linear combinations of rational algebraic correspondences, which suffices to prove equality of the complexified algebraic and Hodge subspaces. Both spaces are rational, so equality descends to $\mathbf Q$. Products of the placed cycles give every invariant tensor. ∎

Exterior projection now proves HC on all powers of very general $A_\lambda$. To transfer back to $X_a$, use the primitive curve correspondences and the graph of $\phi$. On the transcendental part its push-pull is $120\,\mathrm{id}$. If a Hodge tensor on $X_a^r\times A_\lambda^m$ is pulled through the curve-product graph, all its transcendental slots land in tensor powers of $H^1(A_\lambda)$. Proposition 7 represents it by an algebraic cycle. Transfer through the curve projectors, push back, and divide by the appropriate power of 120. Exceptional resolution components are Tate. All other K3 Kunneth factors are generated by divisor, point and fundamental classes. This proves the very-general mixed assertion of Theorem 2 and Theorem 1 at a very general point.

Markman's secant-sheaf program [13] studies Weil classes for general CM fields. The cited survey proves particular lower-dimensional cases and explicitly discusses the remaining higher-dimensional construction problem in Section 12. Our source is an eightfold with a quartic CM Weil action; the result here uses its specific K3 correspondence and does not assert algebraicity on the full deformation space of quartic-CM Weil eightfolds.

### 6.1. A constant surface realizing every determinant line

The mixed assertion with the two CM elliptic curves needs more than the invariant calculation for $A$ alone. We construct an algebraic realization of its entire determinant space, including its non-Hodge components.

Let $\sigma$ be the degree-30 deck generator of $C_\lambda$. Quotient $C_\lambda^2$ by the anti-diagonal subgroup generated by $(\sigma,\sigma^{-1})$, and then by factor interchange. The group has order 60. Its invariant field is

$$
z^{30}=y^{26}(1-x+y)^{15}(1-\lambda x+\lambda^2y)^5,
\qquad x=v_1+v_2,\quad y=v_1v_2,\quad z=w_1w_2.               \tag{28a}
$$

The four projective branch lines have weights $(26,15,5,14)$ and are in general position for $\lambda\ne0,1$. Indeed their four triple determinants are $1-\lambda$, $1$, $\lambda$ and $-\lambda(\lambda-1)$. Four general lines in the plane have no moduli, so this quotient is birationally constant.

For an explicit model set $q=q_1q_2$, $u=u_1u_2$, $b=b_1b_2$ and

$$
k=(1-\lambda v_1)(1-\lambda v_2),\qquad
L_1=(1-v_1)(1-v_2),\qquad D_0=(1-\lambda)(1-\lambda q^5).
$$

Then $q^5=y$, $u^3=q^5/k^2$, $b^2=L_1k$, and $k-\lambda L_1=D_0$. These functions generate the field (28a): $z=qu^2bk$ has residual deck weight $6+2\cdot20+15\equiv1\pmod{30}$. Put

$$
R=ku/q^2,\quad \beta=qD_0/\lambda,\quad
x_{\mathrm{ell}}=-\beta/R,\quad y_{\mathrm{ell}}=-\beta b/R^3.
$$

The identities $R^3=k/q$, $u=q/R^2$ and $b^2=(qR^3-D_0)qR^3/\lambda$ give

$$
y_{\mathrm{ell}}^2=x_{\mathrm{ell}}^3+
\frac{q^4(1-\lambda)^2(1-\lambda q^5)^2}{\lambda^3}.            \tag{28b}
$$

Conversely these equations recover $R,b,k,u,x,y,z$ rationally. With $Q=cq$, $c^5=\lambda$, the coefficient is a nonzero constant multiple of $Q^4(1-Q^5)^2$; a constant Weierstrass rescaling therefore gives $S$ in Theorem 3. Its minimal fibers are $\mathrm{IV}^*$ at zero and infinity and five fibers $\mathrm{IV}$, hence $e(S)=36$ and $\chi(\mathcal O_S)=3$. The degree-three quotient description (28e) has no invariant holomorphic one-form: the order-three automorphisms act without invariant one-forms on $E_3$ and on $B$, since $B/(t\mapsto\zeta_3t)=\mathbf P^1_Q$. Resolution of surface quotient singularities preserves irregularity. Thus $q(S)=0$, $p_g(S)=2$ and $b_2(S)=36-2=34$.

The residual transformation $(\sigma,1)$ normalizes the quotient group: conjugating the swap multiplies it by an anti-diagonal element. Its weights on $q,R,\beta,b$ are $6,8,6,15$ modulo 30. It therefore acts on the fixed model by

$$
\tau(Q,x,y)=(\zeta_{30}^{6}Q,\zeta_{30}^{28}x,\zeta_{30}^{27}y).
                                                               \tag{28c}
$$

All constant coordinate rescalings used above commute with this action. On $\det V_j$ the residual eigenvalue is $\zeta_{30}^{-j}$: it acts on one of the two tensor slots. This is the scalar $K$-action on $\bigwedge_K^2H$, as distinguished from applying an endomorphism to both slots. Thus the determinant identifications below respect a single fixed $K$-action on $T(S)$, independently of $\lambda$.

On primitive cohomology the anti-diagonal average retains exactly the tensors $V_j\otimes V_j$. Geometric interchange acts as minus ordinary tensor interchange on $H^1\otimes H^1$. The surviving primitive subspace is consequently

$$
D_\lambda=\bigoplus_{j\in(\mathbf Z/30)^*}\det V_j
=\bigwedge_K^2 H,
\qquad (h^{2,0},h^{1,1},h^{0,2})=(2,4,2).                    \tag{28d}
$$

All these projectors are rational algebraic deck averages and the swap projector. Applying the Abel--Jacobi correspondences and cup product embeds this exterior subspace into $H^2(A_\lambda)$.

To determine the entire transcendental part of $S$, use the degree-three map

$$
E_3\times B\dashrightarrow S,\quad
B:\ t^3=Q^2(1-Q^5),\quad
(x,y)=(t^2x_E,t^3y_E),\quad y_E^2=x_E^3+1.                  \tag{28e}
$$

It is the quotient by $(x_E,y_E,t)\mapsto(\zeta_3x_E,y_E,\zeta_3t)$. The curve $B$ has genus five. With $v=Q^5$ its function field also has equation $t^{15}=v^2(1-v)^5$. The primitive holomorphic denominator characters are $7,11,13,14$. Their stabilizer in $(\mathbf Z/15)^*$ is $\langle2\rangle=\{1,2,4,8\}$, whose fixed field is $\mathbf Q(\sqrt{-15})$. This induced CM type gives

$$
J(B)\sim E_3\times E_{15}^4.                                 \tag{28f}
$$

Here the only nonprimitive $H^1$ labels are $5,10$. Isomorphisms of polarizable weight-one Hodge structures give actual isogenies of abelian varieties, so (28f) supplies algebraic correspondences.

The invariant $H^2(E_3\times B)$ consists of four Tate dimensions and a rank-eight part from the primitive factor of $B$. Invariance pairs a denominator label $j$ on $B$ with the holomorphic $E_3$ line exactly when $j\equiv1\pmod3$. The primitive Hodge numbers are $(2,4,2)$; the labels $5,10$ give two of the four Tate dimensions. The rank-eight part is two copies of $H^1(E_3)\otimes H^1(E_{15})$. It has no rational $(1,1)$ class, since such a class would give a homomorphism between two nonisogenous elliptic curves. Rational cohomology of a finite quotient is the invariant cohomology; resolving surface quotient singularities adds only divisor classes in degree two. Thus this rank-eight part is exactly $T(S)$, and $\rho(S)=34-8=26$.

For the degree-60 quotient, (28d) accounts for all two holomorphic forms of $S$. The complementary projector on the pullback of $T(S)$ kills both extreme Hodge types. Its image would be a rational pure $(1,1)$ quotient of $T(S)$, which is zero. Therefore the entire pullback lies in $D_\lambda$. The ranks are both eight, giving an isomorphism. Its inverse is the quotient pushforward divided by 60, composed with the inverse $h^1$ identifications; resolution terms are Tate. The degree-three graph gives the corresponding algebraic identification with the indicated summand of $E_3\times B$. Finally, every product of elliptic curves satisfies the Hodge conjecture, with divisor-generated Hodge tensors [14, Corollary 3.9, crediting Imai]. This also makes the isomorphism of that summand with two copies of $H^1(E_3)\otimes H^1(E_{15})$ algebraic. Theorem 3 follows.

### 6.2. Mixed powers with the CM elliptic curves

Put $P=E_3\times E_{15}$. Theorem 3 supplies a surjection onto $D_\lambda$ induced by algebraic correspondences from a finite direct sum of degree-two cohomology summands of powers of $P$.

For very general $\lambda$, let $G=\mathrm{Hg}(A_\lambda\times P)$. Its derived group acts on $H$ as the four $\mathrm{SL}_2$ factors of Lemma 4 and trivially on $H^1(P)$. For any fixed tensor degree, the $\mathrm{SL}_2$ first fundamental theorem gives a surjection onto the derived-invariant subspace of $H^{\otimes n}$ from a finite direct sum of tensor powers of $D_\lambda$ and Tate structures. Its maps are alternating two-tensor inclusions and polarization tensors, with arbitrary slot placements and $K$-actions. They are algebraic and $G$-equivariant. To see surjectivity, complexify and apply the theorem in each standard/dual factor; the eight lines $\det V_j$ supply both signs. Separate embedding placements are obtained from the complex span of the rational $K$-actions. Equality of these rational subspaces then descends to $\mathbf Q$.

Replace each determinant factor by its surjective algebraic realization from $P$, and tensor with any desired cohomology of $P$. A rational Hodge tensor in the target has a rational Hodge lift through this surjection by semisimplicity of polarizable Hodge structures. The lift lies in a finite direct sum of cohomology summands of elliptic-curve products, where [14, Corollary 3.9] represents it algebraically. Applying the specified algebraic maps gives the original tensor. Semisimplicity is used to select a Hodge lift; no algebraicity of an unspecified Hodge splitting is assumed.

Exterior projection proves HC on all mixed powers of $A_\lambda$ and $P$ at a very general parameter. The existing degree-120 graph transfers it to $X_a$, as above. The split correspondence (28e) and (28f) also permits arbitrary $S$ factors. No independence of the source and elliptic centers is assumed. The next argument removes the very-general hypothesis when the source is not of CM type.

### 6.3. Every non-CM source parameter

We use the standard connectedness, reductivity and endomorphism properties of abelian Hodge groups [14, Sections 1.2--1.3]. The following argument concerns the fixed rank-two $K$-representation and does not assume generic monodromy at a special point.

**Proposition 8.** For every $\lambda\ne0,1$ such that $A_\lambda$ is not of CM type, the complex derived Hodge group on $H$ is either $\mathrm{SL}_2^4$ or two diagonal $\mathrm{SL}_2$ factors. In the latter case an algebraic $19$-semilinear quasi-endomorphism of $A_\lambda$ identifies the paired standard modules. In either case the mixed conclusion of Theorem 2 holds.

*Proof.* Put $G=\mathrm{Hg}(A_\lambda)$ and $G'=G^{\mathrm{der}}$. The $K$-endomorphisms and polarization put $G$ inside $U_K(H)$. The signature identities (19) hold at every parameter, so the four $F_0$-volume lines have type $(2,2)$ at every parameter. Consequently $G$ also satisfies the determinant norm relation in (20).

The image of the connected semisimple group $G'_{\mathbf C}$ in each of the four $\mathrm{SL}_2$ factors is trivial or surjective. Since $G'$ is defined over $\mathbf Q$, Galois transitivity makes all four images alike. If all were trivial, $G$ would be a torus and $A_\lambda$ would be of CM type. Otherwise Goursat's lemma describes $G'_{\mathbf C}$ by a Galois-stable partition into diagonal blocks.

The action on the factor indices $(\mathbf Z/30)^*/\{\pm1\}$ is regular cyclic of order four, with cycle $(1,7,11,13)$. Its stable partitions are the singleton partition, the two blocks $\{1,11\},\{7,13\}$, and the single block of size four. The adjoint action of the Hodge circle on the factor indexed by $j$ is nontrivial exactly when $h^{1,0}(V_j)=1$. A diagonal block requires these adjoint actions to agree under its defining isomorphisms. The multiplicities on our representatives are $(1,0,1,0)$, so the size-four block is impossible. This proves the two stated possibilities.

Suppose the two-block case occurs, and let $\alpha\in\operatorname{Gal}(K/\mathbf Q)$ be multiplication by $19$ on labels. Then $V_j$ and $V_{19j}$ are isomorphic derived-group modules: $19$ pairs $1$ with the negative of $11$, and $7$ with $13$. On the connected center of $G$, let $\theta_j$ be the scalar character on $V_j$, written additively. Polarization and the differentiated determinant norm relation give

$$
\theta_{-j}=-\theta_j,\qquad
\theta_{11}=-\theta_1,\qquad \theta_{13}=\theta_7.
                                                               \tag{28g}
$$

Thus $\theta_{19j}=\theta_j$ for all eight labels. The two modules are isomorphic for the full connected group $G_{\mathbf C}$: they agree on its derived group and connected center, which generate it up to a central isogeny.

Consider the rational space

$$
\mathcal J=\{J\in\operatorname{End}_{\mathbf Q}(H):
Jk=\alpha(k)J\ (k\in K),\quad Jg=gJ\ (g\in G)\}.
                                                               \tag{28h}
$$

Its complexification is the sum of the eight one-dimensional intertwiner spaces $\operatorname{Hom}_{G_{\mathbf C}}(V_j,V_{19j})$. Therefore $\dim_{\mathbf Q}\mathcal J=8$, and the left $K$-action makes it a $K$-line. Every nonzero rational $J\in\mathcal J$ is invertible. Indeed its blocks are either zero or isomorphisms between irreducible two-dimensional modules; their vanishing is Galois invariant, and the labels form one Galois orbit. A nonzero $J$ has no zero block. The weight-one Hodge correspondence theorem identifies $\operatorname{End}_{G}(H)$ with the rational abelian endomorphism algebra, so $J$ is algebraic. No equation such as $J^2=-1$, and no automorphism of $C_\lambda$, is required.

In the four-factor case, the derived-invariant surjection of Section 6.2 applies directly. In the two-factor case use $J$ and polarization to identify slots with standard or dual representatives of the two diagonal blocks. The $\mathrm{SL}_2$ first fundamental theorem again generates all derived invariants from evaluation tensors and the individual determinant lines $\det V_j$. All placement maps are algebraic: they use $J$, the $K$-actions, polarizations and alternating inclusions. Complex spectral projectors suffice for spanning, with rational descent as in Section 6.2. Hence there is the same algebraic surjection from a finite sum of tensors in $D_\lambda$ and Tate structures onto every derived-invariant tensor space.

The joint Hodge group of $A_\lambda\times P$ projects onto $G$, and its derived group projects onto $G'$ while acting trivially on $H^1(P)$. The specified maps remain morphisms of Hodge structures for this joint group. Replace determinant factors by Theorem 3, select a rational Hodge lift by semisimplicity, and apply elliptic-product HC exactly as in Section 6.2. The existing graph correspondences permit the $X_a$ and $S$ factors. This proves the proposition and the single non-CM-source case of Theorem 2. $\square$

The classification uses only Goursat's lemma, the rank-two representation and weight-one full faithfulness; it is not a general classification of special abelian eightfolds. For CM sources the derived group is trivial; Sections 6.5--6.6 supply the additional torus argument.

**Corollary 9.** Only finitely many $\lambda\in\mathbf C\setminus\{0,1\}$ have $A_\lambda$ of CM type.

*Proof.* After a finite base cover, the primitive factor is an abelian scheme with a fixed polarization type and level structure. One may pass to a principally polarized isogenous family after a further finite cover. Its algebraic moduli map to $\mathcal A_8$ is nonconstant by Lemma 4, so its image has irreducible algebraic closure a curve and the map has finite fibers.

The generic Hodge group (20) has Hermitian symmetric domain of dimension two: the signatures on the four conjugate pairs are $(1,1),(0,2),(1,1),(0,2)$, and the domain dimension is $\sum_j h_j(2-h_j)=2$. A special curve has generic Mumford--Tate domain of dimension one, so the image closure is not a special curve. By the André--Oort theorem for $\mathcal A_g$ [15, Theorem 5.2], a nonspecial algebraic curve contains only finitely many CM points. Finite fibers and the finite base cover give the assertion. This application supplies no effective list of the exceptional parameters. $\square$

### 6.4. Products at different non-CM parameters

The common $K$-equivariant determinant realization controls possible links between the derived groups of distinct sources. Such control is needed: separate self-power theorems do not by themselves prove a theorem for a product.

**Proposition 10.** Let $A_i=A_{\lambda_i}$ be finitely many non-CM sources. If the joint derived Hodge group identifies a simple factor belonging to $A_i$ with one belonging to $A_\ell$, then $A_i$ and $A_\ell$ are isogenous. After retaining one source from each isogeny class, the joint derived group is the product of the individual derived groups.

*Proof.* Put $H_i=H^1(A_i,\mathbf Q)$ and $G=\mathrm{Hg}(\prod_i A_i\times P)$, where $P=E_3\times E_{15}$. Its projection to each source Hodge group is surjective, and $G^{\mathrm{der}}$ acts trivially on $P$. On the connected center of $G$, write $\theta_{i,j}$ for the scalar character on $V_{i,j}$. Theorem 3 and (28c) identify all determinant lines at the same embedding label. Hence

$$
2\theta_{i,j}=2\theta_{\ell,j},\qquad
\theta_{i,19j}=\theta_{i,j},\qquad
\theta_{i,j}=\theta_{\ell,j}.                                \tag{28i}
$$

The last equality follows from the first because the character lattice of a connected torus is torsion free; the middle equality is (28g) pulled back from the individual source.

For two sources, Goursat describes the joint complex derived group by a partition of their eight conjugate-pair labels into diagonal blocks. The partition is stable under the simultaneous four-cycle $(1,7,11,13)$ and each block has a single adjoint-Hodge type. Restriction to either source is one of the two partitions in Proposition 8. If both sources have four factors, a link propagates to a bijection of labels commuting with the four-cycle. It is an offset in that cycle, and Hodge compatibility makes the offset even: zero or two. If one source has four factors and the other two, a link and its Galois translates would identify distinct factors of the former, which is impossible. If both have two factors, a link propagates to both blocks; their different adjoint-Hodge types exclude switching the blocks. These are the only three cross-source possibilities. The supplement checks this classification by enumerating all 4,140 partitions: exactly seven are Galois and Hodge compatible, four without links and the three just described.

In the four-factor cases use $\alpha=1$ or $19$, respectively; in the two-factor case use $\alpha=1$. Then $V_{i,j}$ and $V_{\ell,\alpha j}$ are isomorphic derived-group modules for every primitive $j$. Equation (28i) makes their connected-center characters agree, so they are isomorphic for the full connected group. The rational space of $\alpha$-semilinear $G$-intertwiners $H_i\to H_\ell$ has complexification

$$
\bigoplus_{j\in(\mathbf Z/30)^*}
\operatorname{Hom}_{G_{\mathbf C}}(V_{i,j},V_{\ell,\alpha j}).
                                                               \tag{28j}
$$

Each summand is one-dimensional, so this rational space has dimension eight over $\mathbf Q$ and dimension one over $K$. A nonzero rational intertwiner has no zero block, by Galois transitivity, and each block is an isomorphism. It is invertible. Weight-one full faithfulness makes it an algebraic quasi-isogeny, as in (28h).

Finally, a subdirect product of simple Lie algebras is a product of diagonal blocks. Any block meeting two remaining sources would already give one of these pairwise links, and hence an isogeny. After selecting pairwise nonisogenous representatives, no such block remains. This proves the product assertion, including equality of the connected derived subgroups in their given representations. $\square$

**Corollary 11.** The mixed assertion of Theorem 2 holds for any finite list of non-CM source parameters, including arbitrary powers of $S$.

*Proof.* First choose one source per isogeny class. Proposition 10 makes the joint derived group a product. Apply the first fundamental theorem independently to each source, using its algebraic semilinear endomorphism when it has two factors. As in Sections 6.2--6.3 this gives algebraic surjections from finite sums of tensors in the individual $D_{\lambda_i}$ and Tate structures onto every derived-invariant tensor space. Identify all determinant factors with the fixed elliptic realization of Theorem 3. A rational Hodge tensor has a rational Hodge lift by polarizable semisimplicity, and elliptic-product HC makes that lift algebraic. The specified maps return the desired cycle. Isogenies restore the omitted sources. The degree-120 correspondences permit all $X_{a_i}$ factors, and (28e)--(28f) permit $S$ factors. Exterior and Kunneth projections finish the proof. $\square$

### 6.5. CM sources and their joint character relations

The fixed determinant geometry also controls the additional tensors at CM parameters. A pairwise torus calculation would not suffice: several CM sources can have character relations invisible in every two-source projection. We therefore treat an arbitrary finite list simultaneously.

Let every $A_i$ in this subsection be of CM type and put

$$
T=\mathrm{Hg}\left(\prod_i A_i\times P\right),\qquad
R=\ker^0\left(T\longrightarrow\mathrm{Hg}(P)\right).
                                                               \tag{28k}
$$

Both are connected tori. All character spaces below are tensored with $\mathbf Q$. By Theorem 3 the determinant characters are common across sources. Write the two characters at label $j$ as $\theta_j\pm\chi_{i,j}$, so $2\theta_j$ is the determinant character and $\theta_{19j}=\theta_j$. The determinant characters span the pullback of the two-dimensional character space of $\mathrm{Hg}(P)$: $T(S)$ is two copies of $H^1(E_3)\otimes H^1(E_{15})$, and the two CM elliptic curves are not isogenous. Thus each $\theta_j$ vanishes on $R$.

First identify the actual weight-one endomorphisms. Put

$$
L_i=\operatorname{Cent}_{\operatorname{End}_{\mathrm{Hdg}}H_i}(K).
                                                               \tag{28l}
$$

The two torus characters on $V_{i,1}$ are distinct, since their Hodge-circle weights are $1,-1$. Galois transitivity makes the two characters distinct at every label. Hence $(L_i)_{\mathbf C}=\mathbf C^{16}$: $L_i$ is commutative étale of $K$-rank two and $H_i$ is free of rank one over it. The polarization makes $L_i$ Rosati-stable. Positivity prohibits exchanging its field factors, and the involution on each factor is nontrivial conjugation because its restriction to $K$ is conjugation. Consequently $L_i$ is either a quadratic CM field extension of $K$ or $K\times K$. This argument does not assume that $A_i$ is simple. Weight-one full faithfulness makes every rational element of $L_i$ an algebraic quasi-endomorphism.

**Lemma 12.** For an arbitrary finite collection of field-type $L_i$, their root characters $\chi_{i,j}$ are equal up to sign or linearly independent after retaining one representative of each equality class. Their span meets the determinant-character space and the span of all split-source roots trivially.

*Proof.* Let $N$ be the compositum of the normal closures of the field-type $L_i$, including $K$. Every conjugate of $L_i$ is quadratic over $K$, so $B=\operatorname{Gal}(N/K)$ is elementary abelian of exponent two. The field $N$ is CM; complex conjugation $c$ is central in $\Gamma=\operatorname{Gal}(N/\mathbf Q)$. The joint torus $T$ is split by $N$, since it acts by multiplication on rank-one $L_i$-modules and the CM fields of $P$ lie in $K$.

Let $\nu$ be the complexified Hodge-circle cocharacter. Its Galois translates span $X_*(T)_{\mathbf Q}$: their rational span defines a rational subtorus containing the Hodge circle, so the minimality defining the Hodge group makes it all of $T$. The map

$$
x\longmapsto F_x,\qquad F_x(g)=\langle x,g\nu\rangle,
\quad X^*(T)_{\mathbf Q}\longrightarrow\mathbf Q^\Gamma
                                                               \tag{28m}
$$

is therefore injective. Polarization gives $cx=-x$ on weight-one characters and their rational span; hence $F_x(cg)=-F_x(g)$.

Choose any lift $t\in\Gamma$ of $7\in(\mathbf Z/30)^\times$. Every element of $\Gamma$ has a unique expression $bt^kc^\epsilon$, with $b\in B$, $0\le k<4$ and $\epsilon\in\{0,1\}$. This uses the quotient $(\mathbf Z/30)^\times=\langle7\rangle\times\langle-1\rangle$, not a splitting of the extension. For a field-type root, $B$ swaps the two embeddings over a fixed $K$-label through a nontrivial quadratic character $\xi_{i,j}$; restriction onto the corresponding quadratic extension is surjective. Thus

$$
F_{\chi_{i,j}}(bt^k)=\xi_{i,j}(b)F_{\chi_{i,j}}(t^k).
                                                               \tag{28n}
$$

The root value is zero at definite labels and $\pm1$ at the labels with signature $(1,1)$. By (19) the latter labels are $\{1,11,19,29\}$. On the four cosets represented by $t^k$, every root function is consequently supported on one of $\{0,2\}$ and $\{1,3\}$, with values $\pm1$ at the two nonzero positions. Up to overall sign, its function on $(b,k)$ is one of

$$
\xi(b)(e_0+e_2),\quad \xi(b)(e_0-e_2),\quad
\xi(b)(e_1+e_3),\quad \xi(b)(e_1-e_3).                         \tag{28o}
$$

These functions are mutually orthogonal: distinct $\xi$ are orthogonal on $B$, the two supports are disjoint, and the two sign patterns on a support are orthogonal. All have squared norm $2|B|$. They are also orthogonal to every $B$-trivial function. Determinant and split-source characters are $B$-trivial. Injectivity of (28m) proves all the assertions for arbitrary finite collections. In particular it excludes a new three-source relation. $\square$

**Lemma 13.** If two field-type sources share a root character up to sign, they are algebraically isogenous. One field source has root rank two or four; in the rank-two case it has an algebraic $19$-semilinear quasi-endomorphism identifying the paired embedding spaces.

*Proof.* Shared roots at labels $j,k$ have the same function support, so $k/j\in\{1,11,19,29\}$. Polarization replaces $k$ by $-k$ and permits $\alpha=k/j\in\{1,19\}$. Galois propagation of the root identity gives equality of unordered root pairs at every corresponding label. The common $\theta_j$ and $\theta_{19j}=\theta_j$ then give equality of the full unordered character sets on $V_{i,j}$ and $V_{\ell,\alpha j}$ for every $j$.

The rational space of $\alpha$-semilinear Hodge maps $H_i\to H_\ell$ complexifies to the complete space of corresponding character-line intertwiners. It contains a blockwise invertible map over $\mathbf C$, so its determinant polynomial is not identically zero. A nonempty Zariski open in a rational vector space has a rational point. We obtain an invertible rational Hodge map, hence an algebraic quasi-isogeny. We have not asserted that every nonzero map is invertible; that shortcut would fail for reducible torus representations.

For one field source the four conjugate-pair roots have two opposite-pair supports. An equality within one support propagates by Galois to the other. Lemma 12 then gives rank two or four, never three. In rank two the equalities are between labels paired by19, and the same full-character and determinant-open argument gives the claimed quasi-endomorphism $J$. A shared root between sources propagates the whole root orbit, so their root ranks also agree. After choosing one field source per isogeny class, all the retained root spaces are independent. $\square$

It remains to analyze split $L_i=K\times K$. Write one rank-one CM type as $t_j\in\{0,1\}$; the other is $h_j-t_j$, with $h_j$ given by (19). The definite entries force $t_7=t_{13}=0$ and $t_{17}=t_{23}=1$. The remaining choices are $(t_1,t_{11})=(x,y)$, with $t_{29}=1-x$, $t_{19}=1-y$. If $x\ne y$, the types are induced from $\mathbf Q(\sqrt{-3})$ and $\mathbf Q(\sqrt{-15})$, giving $A_i\sim E_3^4\times E_{15}^4$; absorb this source in $P$. If $x=y$, exchanging the two $K$ factors exchanges the two choices, so there is one such $K$-linear Hodge isomorphism class. The two rank-one types are related by19, and this source is a square of a CM fourfold up to isogeny.

For the latter class there is also a direct joint-character check. On cosets $1,7,19,13$, the determinant/P character space is spanned by the same-sign functions on the two opposite supports; the roots are the opposite-sign functions. Thus the split root rank is two, independent of the center. The full unordered character sets match under19, giving an algebraic $J$ by the determinant-open argument above. Retain at most one representative of this split class. Its functions are $B$-trivial and Lemma 12 separates them from every field-source root. It follows that the relative torus $R$ is, up to isogeny, a product of the individual retained root tori.

**Proposition 14.** The rational Hodge conjecture holds for all mixed powers of any finite collection of CM sources together with $P$.

*Proof.* Complexify first. For a rank-four retained source the root weights on $R$ are independent pairs $\pm\chi_j$. An invariant tensor must have equal positive and negative multiplicities for each root, so its factors can be paired in arbitrary tensor slots. Write the two eigenlines at label $j$ as $\ell_{j,+}$ and $\ell_{j,-}$. An ordered opposite-root pair at the same embedding is obtained by applying the two $L_i$-eigenprojectors to the slots of the alternating inclusion

$$
\det V_{i,j}\longrightarrow V_{i,j}\otimes V_{i,j}.
                                                               \tag{28p}
$$

The image is nonzero. An ordered opposite-root pair at conjugate embeddings is obtained from the inverse-polarization Tate tensor and the corresponding $L_i$-eigenprojectors. These lines have opposite full characters, exactly as required by polarization. These two constructions cover every opposite-root pairing. Products and slot permutations span all invariant tensors. In rank two, the algebraic $J$ first aligns the19-paired embeddings; the same constructions then apply. They also apply to the nonelliptic split class. Roots at distinct retained sources are independent, so the constructions apply separately. Algebraic isogenies restore the omitted sources.

Each complex eigenprojector belongs to $L_i\otimes\mathbf C$, the complex span of a finite rational basis of algebraic endomorphisms. In a fixed tensor degree, expand all projectors in such bases and take the finitely many needed placements, products, $J$'s, isogenies and polarizations. Every rational map so obtained has image in the rational $R$-invariant space, since its determinant/Tate domain is $R$-trivial. The complex images span that space, so the rational direct sum surjects onto it. This is an algebraic surjection from determinant and Tate tensors, not an assumed algebraic projector onto the invariant space.

All maps are morphisms for the full joint Hodge group, since they come from algebraic correspondences. Replace each determinant by its actual $P$-realization from Theorem 3. Semisimplicity gives a rational Hodge lift of a desired tensor through the resulting algebraic surjection. Elliptic-product HC makes the lift algebraic, and the specified maps give the desired class. Exterior and Kunneth projection yield the asserted cohomological statement. $\square$

### 6.6. Arbitrary smooth source parameters

To complete Theorem 2, allow both CM and non-CM sources. The joint derived Hodge group acts trivially on the CM sources and $P$, and projects surjectively onto the derived group of the non-CM subproduct. Sections 6.3--6.4 supply algebraic determinant/Tate surjections onto that derived-invariant tensor space. Tensor these maps with the CM source factors and replace every determinant by Theorem 3. A rational Hodge tensor has a rational Hodge lift to tensors of CM sources and $P$, where Proposition 14 applies. This proves the assertion for all source factors. The degree-120 graphs and the fixed quotient correspondences add the associated $X_{a_i}$ and $S$ factors.

The source range remains $\lambda_i\ne0,1$ with (4). The separate $a=0$ surface is added by the explicit elliptic-source construction of Section 9.7. Its self-power assertion is also proved independently in Section 8. Section 9 supplies the additional spin support and the relative comparison needed for the canonical Kuga--Satake and enlarged mixed assertions.

## 7. Specialization of the Weil space

The smooth cyclic-cover family over $\lambda\ne0,1$ gives an abelian scheme of primitive factors after an isogeny and finite cover if needed. The rational subvariation $W_{F_0}$ has pure type $(2,2)$ everywhere by (19). It has finite monodromy: its polarization is definite, and its integral lattice makes the monodromy a discrete subgroup of a compact group. After a finite cover it is constant.

Fix a rational basis of this constant variation. Proposition 6 represents it algebraically at every very general point. The following standard spread argument applies to each basis class. Relative Hilbert or Chow parameter spaces have countably many components; finite products and fixed rational coefficients account for rational cycle combinations. On a connected component the fiberwise cycle class is flat. If no component representing the chosen class dominated the base curve, their images would be a countable union of proper closed subsets, which cannot contain all very general points. Thus a representing component dominates. A multisection gives a cycle over a finite extension of the base function field. Properness, closure and fiber restriction then specialize that cycle to every point, with the prescribed flat cohomology class.

Applying this to the four classes proves the all-parameter assertion (5). This argument specializes fixed classes. The additional CM-source Hodge tensors are handled directly in Sections 6.5--6.6, independently of this spread argument.

## 8. All K3 parameters

Work first over $B=\{a:a\ne0,\ a^3\ne8\}$. After a finite cover labeling the fiber components, the resolved elliptic K3s form a smooth projective family with the constant rank-fourteen algebraic space $M$ in (10). Put $\mathcal V=M^\perp$ in its second cohomology local system. It has rational rank eight and an algebraic self-adjoint $E$-action. Generically it is $T$.

The rational rank-two space $\bigwedge_E^4\mathcal V$ has finite monodromy, since an $E$-linear orthogonal transformation has determinant $\pm1$. Make it constant by a finite cover. The very-general theorem and the spread argument of Section 7 show that the entire space is algebraic on every fourth power of a fiber. This is the exceptional-volume specialization of [2, Proposition 2.22 and Remark 2.24]. We spell out the contraction required when the transcendental rank decreases.

At $b\in B$ write

$$
\mathcal V_b=T(X_b)\perp N_b,                                  \tag{29}
$$

where $N_b$ consists of algebraic divisor classes. It is nondegenerate and stable under $E$, because the action is self-adjoint and preserves $T$. The specialized $E$-action on $T$ is faithful. Set $L=\operatorname{End}_{\mathrm{Hdg}}T(X_b)$. By the K3 endomorphism theorem [12], $L$ is totally real or CM. If it is totally real then $\dim_L T\ge3$. Since $E\subset L$ and $\dim_{\mathbf Q}T\le8$, a strict totally real extension would have degree at least four and force $\dim_L T\le2$. Hence $L=E$, and its $E$-rank is either four or three.

For rank four the specialized exceptional volume is already $\bigwedge_E^4T$. For rank three, $N_b$ is an $E$-line. Write the rational pairing as $\operatorname{Tr}_{E/\mathbf Q}\psi$, choose $0\ne n\in N_b$, and set $d=\psi(n,n)\ne0$. Contraction by the rational functional

$$
\ell_n(v)=\operatorname{Tr}_{E/\mathbf Q}\psi(n,v)
                                                               \tag{30}
$$

is algebraic: cup with the divisor $n$ on one K3 factor and integrate. At each embedding $\sigma:E\hookrightarrow\mathbf C$, it maps

$$
\bigwedge^4\mathcal V_{b,\sigma}
=\bigwedge^3 T(X_b)_\sigma\wedge n_\sigma
\longrightarrow\bigwedge^3 T(X_b)_\sigma
                                                               \tag{31}
$$

with nonzero coefficient $\sigma(d)$, up to the nonzero antisymmetrization normalization. Project the remaining factors onto $T$ using the algebraic divisor projector. Both complex volume lines, and therefore their full rational span $\bigwedge_E^3T$, are algebraic. Since all degree-two invariant tensors come from the actual $E$-correspondences, orthogonal invariant theory [2, Theorem 2.16] proves self-power HC.

If $L$ is CM, self-power HC is the known CM-endomorphism K3 theorem [2, Corollary 2.3], based on Buskin, Huybrechts and Ramon--Mari. Here “CM endomorphism field” does not require that the whole Mumford--Tate group be a torus. This covers every point of $B$.

For $a^3=8$, replacing $a,h$ by $\zeta_3a,\zeta_3h$ in the double-cover model multiplies the right side by $\zeta_3$, absorbed by scaling $z$. All three surfaces are therefore isomorphic to the fixed $a=2$ surface of [9], where self-power HC has been proved. We do not need a simultaneous projective resolution across this fiber collision.

Finally at $a=0$, the automorphism $(s,X,Y)\mapsto(s,\zeta_3X,Y)$ acts on $ds\wedge dX/Y$ by $\zeta_3$. Its invariant rational part in $T$ would have type $(1,1)$ and hence is zero. It therefore embeds $\mathbf Q(\zeta_3)$ into the K3 endomorphism field. This field is CM, so the same known theorem applies. Theorem 1 follows.

## 9. A symplectic K3 pencil and the moving spin correspondence

This section constructs the additional correspondence needed for Theorem 4. The geometric input is a third quotient, now of $C_\lambda^2\times E_3$. Its useful pencil has K3 fibers with a symplectic order-five action. We first record the standard divisor-spreading and weight argument that turns this geometry into actual curve support. The Hilbert-scheme mechanism is the one used by Arapura [16, Corollary 1.5 and Remark 1.6]; it is not a novelty claim.

### 9.1. A support lemma for a selected surface variation

**Lemma 15.** Let $f:Z\to B$ be a morphism from a smooth projective threefold to a smooth projective curve, with a finite-order automorphism $\tau$ acting over $B$. Suppose the smooth fibers satisfy $H^1=0$ and $\tau$ acts trivially on $H^{2,0}$. Put $e=1-\operatorname{avg}(\tau)$. Then $eH^3(Z,\mathbf Q)$ is spanned by images of algebraic correspondences

$$
H^1(F)(-1)\longrightarrow H^3(Z,\mathbf Q)                    \tag{32}
$$

for finitely many smooth projective curves $F$. The assertion applies in particular when the general fibers are blowups of K3 surfaces and $\tau$ is symplectic on their minimal models.

*Proof.* Choose a nonempty affine open $U\subset B$ over which $f$ is smooth. The local system $N=eR^2f_*\mathbf Q$ is of type $(1,1)$. Tensoring the translates of a relatively ample line bundle gives an invariant ample class $h$, and $N\perp h$. By the Hodge index theorem $N$ is negative definite. Its full integral lattice is monodromy-stable, so its monodromy is finite. After a finite base cover and equivariant resolution, $N$ is constant over a smaller affine open. The finite-cover trace will descend all the correspondences constructed below.

Choose an integral basis $l_i$ of $N$. Each $l_i+m h$ is an effective divisor class on a given fiber for some integer $m$. To spread it, remove from the base the images of all nondominating irreducible components of all relative Hilbert schemes. There are countably many such components and each image is a finite set. Choose a complex point outside their union and an effective Cartier divisor of class $l_i+m h$ on its fiber. A Hilbert component through that divisor dominates the base; its nonempty relative-Cartier locus still dominates. The cohomology class is locally constant there, so it stays $l_i+m h$. A closed point of the generic fiber of this parameter space gives a finite function-field extension and an actual relative divisor. Repeat for the finitely many basis elements and take a common finite cover. This is Arapura's Hilbert-spreading argument [16], applied to the selected Tate variation.

Write the resulting compactified family as $f':Z'\to B'$. The closures $D_i$ of these relative divisors define actual cycles

$$
\Gamma_i=(f'|_{D_i},\operatorname{incl})_*[D_i]
\in\mathrm{CH}^2(B'\times Z')_{\mathbf Q}.                    \tag{33}
$$

Their actions are $H^1(B')(-1)\to H^3(Z')$. Compose them with $e$, which removes the added $m h$. On the smooth affine part $U'$, the fiber groups $H^1$ and $H^3$ vanish, and the base has cohomological dimension one for local systems. Leray therefore gives

$$
eH^3(Z'_{U'},\mathbf Q)=H^1(U',\mathbf Q)\otimes N_0.          \tag{34}
$$

The relative divisor maps realize this equality as mixed Hodge structures. The restriction of compact $H^3(Z')$ has weight three; the weight-three part of (34) is precisely $H^1(B')\otimes N_0$, with the evident restriction into $H^1(U')\otimes N_0$. Thus the maps (33) span the restriction of $eH^3(Z')$. Subtracting their images reduces to the restriction kernel.

Make the reduced boundary a simple normal crossings divisor by equivariant blowups over the omitted fibers. This does not change the smooth open, and support on the new model descends by degree-one trace. If $D^{[p]}$ is the disjoint union of $p$-fold boundary intersections and $D^{[0]}=Z'$, the logarithmic weight spectral sequence [17, Section 3.2] is

$$
E_1^{-p,q}=H^{q-2p}(D^{[p]},\mathbf Q)(-p)
\Longrightarrow H^{q-p}(Z'_{U'},\mathbf Q).                   \tag{35}
$$

Each term has pure weight $q$, so the sequence degenerates at $E_2$. At $(0,3)$ the only incoming $d_1$ is the sum of Gysin maps $H^1(D_a)(-1)\to H^3(Z')$ from the smooth boundary surfaces. There is no outgoing differential, and the edge map is restriction with image $W_3H^3(Z'_{U'})$. Consequently these Gysin maps generate exactly its kernel. This is also consistent with [17, Corollary 3.2.17], which identifies the compact image with the lowest weight.

The $H^1$ of a smooth projective surface is generated by actual curve correspondences: use its Albanese variety, a curve whose Jacobian surjects onto it, Poincare complete reducibility, and Poincare divisors. Hence the boundary contribution is curve-generated too. Finally for the generically finite map $\pi:Z'\to Z$, the identity $\pi_*\pi^*=(\deg\pi)\operatorname{id}$ descends support; apply $e$ on the target. All constructions use actual divisors, graphs and traces. No algebraic splitting of an abstract Hodge quotient is an input. $\square$

### 9.2. The quotient and its symplectic pencil

On $E_3:y_E^2=x_E^3+1$ choose $\gamma(x_E,y_E)=(\zeta_3^2x_E,-y_E)$. Its holomorphic differential has character $+1$ modulo six. With $\sigma:w\mapsto\zeta_{30}w$, let

$$
H_0=\{(a,b,c)\in(\mathbf Z/30)^2\times\mathbf Z/6:
                 a+7b-5c=0\pmod {30}\}.                     \tag{36}
$$

It has order180. In the coordinates (11), put

$$
\begin{aligned}
A&=q_1q_2^2,& B&=v_2/A^2,& U&=u_1u_2x_E,\\
D&=\frac{b_1b_2y_E}{(1-\lambda v_1)(1-\lambda v_2)},&
P&=(B^2-A)(1-A^2B),&Q&=(B^2-\lambda A)(1-\lambda A^2B).
\end{aligned}                                                \tag{37}
$$

These functions are invariant under $H_0$. We have $v_1=A/B^2$, $v_2=A^2B$, and, writing $p=P/B^2$, $k_0=Q/B^2$,

$$
D^2=\frac p{k_0}+\frac{p k_0 U^3}{v_1v_2}.
$$

The exact change $x=PQU/(AB)$, $y=PQD$ gives

$$
W_\lambda:\qquad y^2=x^3+P^3Q.                              \tag{38}
$$

The invariant functions generate the fixed field. Indeed reconstruction has at most $5\cdot9\cdot4=180$ choices: choose $q_1$, recover $q_2=A^3/(q_1^3v_2)$, choose $u_1,u_2$ and $b_1,b_2$, and then $U,D$ recover the elliptic coordinates. The group gives the reverse degree bound. Thus (38) is the actual quotient field, rather than merely a related hypersurface.

Set $t=y/P^2$ and $z=x/P$. Fixing $t$ gives the pencil

$$
z^3=t^2P-Q.                                                  \tag{39}
$$

On $\mathbf P^1_A\times\mathbf P^1_B$, $P,Q$ are sections of $\mathcal O(3,3)$ and $z$ is the cyclic-cover coordinate in $\mathcal O(1,1)$. A smooth fiber of (39) has trivial canonical bundle, and
$\pi_*\mathcal O=\mathcal O\oplus\mathcal O(-1,-1)\oplus\mathcal O(-2,-2)$ gives irregularity zero. It is a K3 surface.

To check smoothness, put $k=t^2$. The branch polynomial is

$$
(k-1)B^2+(\lambda-k)(A+A^2B^3)+(k-\lambda^2)A^3B.             \tag{40}
$$

On the torus the etale degree-five map $u=A/B^2$, $v=A^2B$ makes (40), divided by $B^2$, equal to $a+b(u+v)+cuv$, where $a=k-1$, $b=\lambda-k$, $c=k-\lambda^2$. The determinant $ac-b^2=-k(\lambda-1)^2$ excludes a torus singularity when $k\ne0$ and $\lambda\ne1$. The only boundary intersections are the four corners; their local gradients are nonzero if $abc\ne0$. Thus excluding $k\in\{0,1,\lambda,\lambda^2,\infty\}$ suffices for every $\lambda\ne0,1$.

The actual residual automorphism $\sigma_1^6$, with $\zeta=\zeta_5$, is

$$
(A,B,z,t)\longmapsto(\zeta A,\zeta^3B,\zeta^2z,t).            \tag{41}
$$

It fixes $t$ and is symplectic on the smooth fibers, since $dA\wedge dB/z^2$ has weight $1+3-4=0$. There are four fixed points, above the four corners. The invariant $H^2$ has rank six and its complement rank sixteen; the support argument only needs the latter to be a negative definite divisor variation. Standard symplectic-K3 background is in [12, Chapter 15, Section 1].

Let $\mathcal M_\lambda$ be the primitive $H^1\otimes H^1\otimes H^1$ summand fixed by (36). Its complexification is

$$
(\mathcal M_\lambda)_{\mathbf C}
=\bigoplus_{j\in(\mathbf Z/30)^\times}V_j\otimes V_{7j}\otimes e_j,
\qquad \dim_{\mathbf Q}\mathcal M_\lambda=32,                 \tag{42}
$$

where $e_j$ is the elliptic character $j$ modulo six. The source character is $(-j,-7j,5j)$ modulo thirty. Every summand has nontrivial $\sigma_1^6$ character $\zeta^{-j}$. By (19) its Hodge types are $(2,1)^2+(1,2)^2$.

We spell out transport from a smooth quotient model. Write $Y=C_\lambda^2\times E_3$, $q:Y\to Q_0=Y/H_0$, and choose an equivariant resolution $\rho:Z\to Q_0$ also resolving the pencil. Rationally
$q^*:H^3(Q_0)\simeq H^3(Y)^{H_0}$: finite proper fibers have no higher cohomology, averaging is exact over $\mathbf Q$, and $(q_*\mathbf Q)^{H_0}=\mathbf Q$. Resolve the dominant component of $Y\times_{Q_0}Z$ to obtain $p:R\to Y$ birational and $b:R\to Z$. Then

$$
p_*b^*\rho^*\eta=p_*p^*q^*\eta=q^*\eta.                     \tag{43}
$$

The correspondence $p_*b^*$ is algebraic and equivariant. Smooth general fibers of $Z\to\mathbf P^1_t$ are blowups of the K3 surfaces (39), so Lemma 15 applies. Compose its supported maps with (43) and the actual primitive, Kunneth and group projectors. We obtain an algebraic surjection

$$
\Gamma:H^1(F)(-1)\twoheadrightarrow\mathcal M_\lambda         \tag{44}
$$

from a finite disjoint union of curves. This holds for every smooth source parameter, including CM sources. The construction does not require equations for those supporting curves.

### 9.3. An algebraic weight-one retraction

The projector onto $\mathcal M_\lambda$ is self-adjoint for cup product: the curve $H^1$ and primitive deck projectors are self-adjoint, and the finite-group average includes every inverse graph with the same coefficient. Moreover the $H^1\otimes H^1\otimes H^1$ piece of the actual threefold $Y$ is primitive for a product ample class, because cupping a curve's $H^1$ with its ample class gives zero. Its ordinary middle pairing polarizes it, up to the usual Hodge--Riemann sign.

Consequently the transpose of (44), with this sign convention, is its algebraic polarization adjoint $\Gamma^\dagger$. Surjectivity and positivity make $Q=\Gamma\Gamma^\dagger$ invertible on $\mathcal M_\lambda$. Its inverse is a rational polynomial in $Q$, by the minimal polynomial with nonzero constant term. Therefore

$$
j=\Gamma^\dagger Q^{-1},\qquad \Gamma j=\operatorname{id}_{\mathcal M_\lambda}
                                                               \tag{45}
$$

is an actual algebraic retraction. The idempotent $j\Gamma$ on $H^1(F)$ is an idempotent in $\operatorname{End}^0(J(F))$ and defines an abelian sixteenfold $B_\lambda$. Abel--Jacobi and Poincare divisors give algebraic maps in both directions realizing

$$
H^1(B_\lambda)(-1)\simeq\mathcal M_\lambda.                   \tag{46}
$$

This adjoint construction is the one used in [9], now applied to (44). Working on the threefold makes its polarization an ordinary middle pairing; no general inverse-Lefschetz standard conjecture enters. The isogeny class of $B_\lambda$ is determined by (46), independently of the auxiliary curves.

Any Hodge tensor involving $H^1(B_\lambda)$ can now be sent by (46) to a tensor in $H^1(A_\lambda)^2\otimes H^1(E_3)$ with the indicated Tate twist. Theorem 2 supplies a cycle for that tensor; (45) recovers the original tensor algebraically. The same argument works simultaneously for any finite parameter list and with the existing $X_a,E_3,E_{15},S$ factors. Exterior and Kunneth projections give all cohomology classes on their mixed products. This proves the enlarged mixed assertion in Theorem 4. Its very-general case uses only the non-CM theorem of Sections 6.2--6.4; the full parameter range also uses Sections 6.5--6.6.

### 9.4. Rational spin comparison and the specified KS class

Assume now that $\lambda$ is very general. The derived group on the source has complexification $\mathrm{SL}_2^4$, indexed by $1,7,11,13$. The noncompact real factors are $1,11$ and the compact ones $7,13$. The determinant and elliptic characters satisfy

$$
2(h_j-1)=\chi_{-15}(j)-\chi_{-3}(j),\qquad
(h_j-1)+(h_{7j}-1)+\chi_{-3}(j)=0.                            \tag{47}
$$

On the connected center of the joint source group write $\theta_j$ for the scalar character on $V_j$ and $\eta_j$ for that on $e_j$. Equation (47) holds for every Galois-conjugate projected Hodge cocharacter, which generate the quotient torus. Hence $\theta_j+\theta_{7j}+\eta_j=0$: the connected center acts trivially on $\mathcal M_\lambda$. One can equivalently use the actual CM determinant realization of Theorem 3 to obtain twice this relation and then use connectedness.

The derived constituents in (42) are the four cross edges

$$
\{1,7\},\quad\{7,11\},\quad\{11,13\},\quad\{13,1\},          \tag{48}
$$

each twice. Galois rotates them transitively. At every real place the edge representation is the tensor of the real standard module of $\mathrm{SL}_2(\mathbf R)$ with the quaternionic standard module of $\mathrm{SU}_2$. It is quaternionic, so its multiplicity in a real representation is even. A nonzero rational subrepresentation must contain every edge with equal even multiplicity. As (42) already has multiplicity two, it is rationally irreducible. Its commutant has complexification $M_2(\mathbf C)^4$, center $F=K^+$, and Hamilton quaternion algebra at each real place. It is a quaternion division algebra over $F$. Thus $B_\lambda$ is simple and has the endomorphism algebra stated in Theorem 4.

The actual K3 map identifies $T(X_a)_{\mathbf C}$, on the derived group, with the diagonal edges $\{1,11\}$ and $\{7,13\}$. Its adjoint group is the adjoint source derived group. Pull both representations back to their common simply connected rational cover; this is also the group used for the real-multiplication KS comparison [18, Theorem 3.3.1(i)]. For $\mathrm{Spin}_4\times\mathrm{Spin}_4\to\mathrm{Spin}_8$, the two half-spin modules restrict as

$$
\begin{aligned}
S^+&=(\mathrm{Std}_1\otimes\mathrm{Std}_7)
       \oplus(\mathrm{Std}_{11}\otimes\mathrm{Std}_{13}),\\
S^-&=(\mathrm{Std}_1\otimes\mathrm{Std}_{13})
       \oplus(\mathrm{Std}_{11}\otimes\mathrm{Std}_7).
\end{aligned}                                                \tag{49}
$$

The even Clifford left-regular module has each edge eight times. The Galois orbit of highest weights has the unique simple rational representation supplied by (42), with Schur multiplicity two. Thus the rational Clifford representation is $\mathcal M_\lambda^4$.

Hodge compatibility is a separate check. After removing the connected center, the source circle has weights $+1,-1$ on factors $1,11$ and is trivial on $7,13$. On $T$ it rotates the $(2,0)$ plane with weight two, and on every cross edge it has the spin-lift weights $+1,-1$. Comparing on a finite cover of this circle in the common simply connected group gives

$$
H^1(\mathrm{KS}_T(X_a))\simeq\mathcal M_\lambda(1)^4,
\qquad \mathrm{KS}_T(X_a)\sim B_\lambda^4.                    \tag{50}
$$

Here $\mathrm{KS}_T$ uses the full even Clifford algebra of the rank-eight transcendental quadratic space, so its dimension is64. The weight-one Hodge isomorphism in (50) is an algebraic isogeny of abelian varieties.

The enlarged mixed HC theorem applies to $X_a\times B_\lambda^8$, hence to $X_a\times\mathrm{KS}_T(X_a)^2$. The specified canonical KS embedding, converted by polarization into $T(X_a)\to H^2(\mathrm{KS}_T(X_a)^2)$, is a rational Hodge class of codimension two on that product. HC represents that very class by an algebraic cycle. This proves the canonical assertion, without identifying an arbitrary nonzero embedding with the specified one. The required relative comparison at jumps of the transcendental lattice is supplied next.


### 9.5. Extending the comparison as a variation

We now keep track of the relative structure; the smaller transcendental space at a special point need not equal the rank-eight variation. We use the following elementary rigidity argument for polarizable variations over a curve.

**Lemma 16.** Let $H,W$ be polarizable rational variations of Hodge structure of the same weight over a smooth connected complex algebraic curve, each with a monodromy-stable full integral lattice. If $H_b\simeq W_b$ as rational Hodge structures at every very general point, then they are isomorphic as rational variations after a finite étale cover.

*Proof.* Cover the curve by countably many simply connected analytic disks. In a flat trivialization on one disk, the rational elements of $\operatorname{Hom}(H,W)$ form a countable set. The locus where a given element preserves the Hodge filtrations is closed analytic, since its maps $F^pH\to W/F^pW$ are holomorphic. A proper such locus is discrete and countable. Choose a point outside all proper loci and the exception to the very-general hypothesis. An isomorphism there is therefore a Hodge morphism throughout its disk.

Continue it flatly on the universal cover. The identity theorem makes it a Hodge morphism everywhere. The rational span $L$ of all its monodromy translates is consequently a sub-local system of $\operatorname{Hom}(H,W)$ of type $(0,0)$. Its polarization is definite, and its intersection with the integral Hom lattice is a full stable lattice. Hence its monodromy is finite. Kill this monodromy by a finite étale cover. The chosen map becomes global and flat; its determinant is nonzero everywhere because it was nonzero initially. $\square$

Work on the finite cover of $B=\{a\ne0:a^3\ne8\}$ used in Section 8, also adjoining the source parameter. Let $\mathcal V=M^\perp$ be its rank-eight K3 variation. The algebraic relative KS construction [12, Chapter 6, Section 4.4 and Proposition 4.10] gives, after a further finite étale cover, an abelian scheme with weight-one variation $H_{\mathrm{KS}}$. Its fibers are the even-Clifford KS varieties of $\mathcal V_b$.

The monodromy used here is a lifted Spin action by **left multiplication** on a reference Clifford algebra. The natural Clifford functor on the original orthogonal local system is not generally the polarized abelian family; [12] explains this distinction and uses Borel algebraicity. The right Clifford data defining the polarization are fixed in this construction.

The curve-product family and the actual projectors of (42) give an integral-lattice, polarizable variation $\mathcal M(1)$ of weight one. Its polarization is the primitive middle pairing described in Section 9.3, with the Tate sign. Equation (50) and Lemma 16 give an isomorphism of variations after finite cover, and therefore actual fiberwise abelian isogenies

$$
\mathrm{KS}(\mathcal V_b)\sim B_{\lambda_b}^{4}
\qquad\text{for every }b\text{ over }B.                       \tag{51}
$$

Only the individual $B_\lambda$ and their algebraic retractions are needed here. We have not assumed an algebraic family of the auxiliary supporting curves.

### 9.6. The smaller Clifford factor and the specified class

At a special point write $\mathcal V_b=T_b\perp N_b$ as in (29). The graded Clifford decomposition gives

$$
\mathrm{Cl}^+(\mathcal V_b)=
[\mathrm{Cl}^+(T_b)\otimes\mathrm{Cl}^+(N_b)]
\oplus[\mathrm{Cl}^-(T_b)\otimes\mathrm{Cl}^-(N_b)].            \tag{52}
$$

Choose an orthogonal rational basis of $N_b$, ordered after a basis of $T_b$. Let $i$ include $\mathrm{Cl}^+(T_b)$ and let $p$ discard every nonempty $N_b$ monomial in the resulting Clifford basis. Then $pi=1$. The KS complex structure is left multiplication by $J=e_1e_2\in\mathrm{Cl}^+(T_b)_{\mathbf R}$, so both maps commute with it. They are rational weight-one Hodge maps and hence actual abelian homomorphisms up to isogeny. Thus $\mathrm{KS}_T(X_b)$ is an abelian isogeny factor of the left side of (51), and therefore of $B_{\lambda_b}^4$.

This extraction also respects the specified embedding. In the relative construction fix a nonisotropic reference vector $v_0$ as right Clifford data. For $\phi_v(w)=vwv_0$,

$$
L_g\phi_vL_g^{-1}(w)=(gvg^{-1})wv_0.                         \tag{53}
$$

Consequently the specified map is monodromy-equivariant; $v_0$ need not be a flat section of $\mathcal V$. At a special fiber choose nonisotropic $t_0\in T_b$. Right multiplication by $v_0t_0/q(v_0)$ is an algebraic abelian Hodge automorphism and changes $\phi^{v_0}$ to $\phi^{t_0}$ by composition on its output. For $v\in T_b$,

$$
p\phi_{\mathcal V_b}^{t_0}(v)i(w)=vwt_0
=\phi_{T_b}^{t_0}(v)(w).                                    \tag{54}
$$

These are precisely the choice changes in [12, Chapter 4, Proposition 2.6 and Remark 2.7] and [19, Section 3 and Remark 4.3]. The source projector onto $T_b$ is algebraic, using the inverse divisor-intersection matrix. Hence no arbitrary nonzero Hodge map is substituted for the specified arrow. Alternatively (53) and the global polarization define a flat codimension-two class; the relative-Hilbert argument of Section 7 specializes that class, and (54) extracts its actual transcendental version.

For the stronger mixed assertion it suffices to use the abelian factor in (51). Theorem 4 and algebraic isogeny splittings permit $\mathrm{KS}_T(X_b)$ in any of the mixed products for finite parameter lists in $B$. Full HC then supplies the specified class again.

At $a^3=8$, take $\lambda=-1$. The exact source and elliptic-action conventions agree with [9, Section 10.1]. Its additional finite automorphism $\mathcal S$ normalizes $H_0$ and sends primitive labels $j$ to $13j$. The rank-eight spin module of [9, Section 10.3] is its invariant summand inside $\mathcal M_{-1}$. Thus the supported spin fourfold $A_{\mathrm{sp}}$ of that paper is an abelian isogeny factor of $B_{-1}$. Its theorem $\mathrm{KS}_T(X_2)\sim A_{\mathrm{sp}}^4$ puts this KS variety in the same mixed theorem. The other two values of $a$ are isomorphic to $X_2$, as explained in Section 8. This uses no simultaneous resolution across the collision.

### 9.7. The remaining isotrivial member

The point $a=0$ has no smooth source parameter in (4). It has its own explicit connection to the fixed elliptic source of Theorem 3. Rename the genus-five curve in (28e) as $R:b^3=r^2(1-r^5)$, so $J(R)\sim E_3\times E_{15}^4$. The formulas

$$
s=r+r^{-1},\qquad t=b^2/r^3                                 \tag{55}
$$

give a map to the normalization $D$ of $t^3=D_5(s)-2$. Its degree is two: $r^2-sr+1=0$ and $b=(1-r^5)/(tr)$, while the nontrivial involution is $(r,b)\mapsto(r^{-1},-b/r^3)$. Riemann--Hurwitz for the four fully ramified points of the triple cover gives $g(D)=2$.

The nonprimitive elliptic quotient of $R$ is $e^3=v(1-v)$, with $v=r^5,e=br$. The involution sends $(v,e)$ to $(v^{-1},-e/v)$ and acts by $-1$ on $dv/e^2$. Its invariant $H^1(D)$ therefore has no part in the nonprimitive $E_3$ factor. By (28f) and complete reducibility,

$$
J(D)\sim E_{15}^{2}.                                      \tag{56}
$$

This uses the already established induced CM type, not an additional general CM-Hodge assertion. As an independent explicit check, $u=t/(s^2+s-1)$ gives $D:z^2=5u^6-10u^3+1$. After scaling it is $z^2=x^6-2\sqrt5x^3+1$. Its reciprocal elliptic quotients are
$w_\pm^2=(R_0\pm2)(R_0^3-3R_0-2\sqrt5)$, with $R_0=x+x^{-1}$ and $w_\pm=z(x\pm1)/x^2$. Their $j$-invariants are $(-191025\pm85995\sqrt5)/2$; this check is not needed for (56).

The actual degree-three map from $E_3:y^2=x^3+4$ and $D$ is

$$
E_3\times D\dashrightarrow X_0,\qquad
X=t^2x,\quad Y=t^3y.                                        \tag{57}
$$

It is the quotient by $(x,y,t)\mapsto(\zeta_3x,y,\zeta_3t)$. The invariant part of $H^1(E_3)\otimes H^1(D)$ has rank four and Hodge numbers $(1,2,1)$: each nontrivial order-three eigenspace of $H^1(D)$ has dimensions $(1,1)$. It has no rational $(1,1)$ class, since such a class in $H^1(E_3)\otimes H^1(E_{15})$ would give a homomorphism between nonisogenous elliptic curves. Quotient resolutions add only divisors. Hence

$$
\rho(X_0)=18,\qquad
T(X_0)\simeq H^1(E_3)\otimes H^1(E_{15})                    \tag{58}
$$

as rational Hodge structures. The latter tensor is simple: its four characters are a single Galois orbit for the product of the two distinct CM norm-one tori. The actual graph and degree-normalized pushforward split $T(X_0)$ from the elliptic source. Thus $X_0$ can be adjoined to all the mixed products already proved, with actual correspondences.

The standalone HC and KS algebraicity assertions at this Picard-number-eighteen point also follow from the broader low-rank results of [20]. The quotient above identifies the particular elliptic factors needed to mix this endpoint with the generic Picard-number-fourteen family; that link is the input used here.

Its visible rank-eighteen divisor form is $U_{\mathrm{hyp}}\perp A_2(-1)^2\perp E_6(-1)^2$. The index-three inclusion $E_6\perp A_2\subset E_8$ and Witt cancellation in the K3 rational lattice give $T(X_0)_{\mathbf Q}\simeq U_{\mathrm{hyp}}^2$. For this split rank-four space $\mathrm{Spin}_4=\mathrm{SL}_2\times\mathrm{SL}_2$ over $\mathbf Q$. If $e_3,e_{15}$ are the elliptic CM characters, the vector weights in (58) are $\pm(e_3+e_{15}),\pm(e_3-e_{15})$. The two rational half-spin modules have weights $\pm e_3$ and $\pm e_{15}$, with the weight-one lifted Hodge circle. They are therefore the corresponding elliptic Hodge structures. Each occurs twice in the even-Clifford left-regular module, so

$$
\mathrm{KS}_T(X_0)\sim E_3^2\times E_{15}^2.                 \tag{59}
$$

Together (51)--(59) allow the actual transcendental KS variety at every finite parameter in the mixed theorem. Every nonzero $a$ admits a source in (4); extra parameters are included by enlarging that finite list. Mixed HC represents the specified canonical class on $X_a\times\mathrm{KS}_T(X_a)^2$. This proves Theorem 5, including the separate endpoint. The family arguments and endpoint quotient are additional constructions beyond specialization of the previously known self-power theorem.

## 10. Paired source parameters and generalized Hodge support

The support construction also works when the two curve parameters differ. This supplies the additional weight-one objects needed to lower support on mixed products of different K3 members. Throughout, $B_{i\ell}$ refers to an ordered pair; both orders are allowed. We first prove ordinary HC for the enlarged collection at every smooth source parameter. We first use its jointly very general Hodge group, then treat every non-CM tuple by the classification of Propositions 8 and 10.

### 10.1. The actual paired-parameter quotient and its retraction

Let $\lambda_i,\lambda_\ell\ne0,1$ and put $Y_{i\ell}=C_{\lambda_i}\times C_{\lambda_\ell}\times E_3$. Use (11) with the appropriate parameter on each curve and the group $H_0$ of (36). Define

$$
\begin{aligned}
A&=q_1q_2^2,& B&=v_2/A^2,& U&=u_1u_2x_E,\\
D&=\frac{b_1b_2y_E}{(1-\lambda_i v_1)(1-\lambda_\ell v_2)},&
P&=(B^2-A)(1-A^2B),&
Q&=(B^2-\lambda_i A)(1-\lambda_\ell A^2B).
\end{aligned}                                                   \tag{60}
$$

Their deck weights are independent of the parameters, so they are still $H_0$-invariant. With $v_1=A/B^2$, $v_2=A^2B$, $p=P/B^2$ and $q=Q/B^2$, the equation of $E_3$ gives $D^2=p/q+pqU^3/(v_1v_2)$. Thus $x=PQU/(AB)$, $y=PQD$ give the actual quotient equation

$$
W_{i\ell}:\quad y^2=x^3+P^3Q.                                \tag{61}
$$

For completeness, the fixed-field degree argument remains valid with these two parameters. Once $A,B$ are fixed, choose one of the five values of $q_1$, and recover $q_2=A^3/(q_1^3v_2)$. Its fifth power is $v_2$ and $q_1q_2^2=A$. There are at most nine choices of $u_1,u_2$ and four of $b_1,b_2$; $U,D$ then determine $x_E,y_E$. The upper bound is $5\cdot9\cdot4=180$, equal to the faithful group order. Hence (61) is the fixed field, including when the parameters coincide or are of CM type.

The pencil $t=y/P^2$, $z=x/P$, $k=t^2$ now has branch

$$
\begin{aligned}
z^3=kP-Q={}&(k-1)B^2+(\lambda_i-k)A\\
&+(\lambda_\ell-k)A^2B^3
 +(k-\lambda_i\lambda_\ell)A^3B.
\end{aligned}                                                   \tag{62}
$$

It is a section of $\mathcal O(3,3)$. Dividing by $B^2$ and using $u=A/B^2$, $v=A^2B$ gives a bilinear expression with determinant

$$
(k-1)(k-\lambda_i\lambda_\ell)
 -(\lambda_i-k)(\lambda_\ell-k)
 =-k(\lambda_i-1)(\lambda_\ell-1).
$$

The map from the torus in $(A,B)$ to that in $(u,v)$ is etale of degree five. The determinant excludes a torus singularity. The only boundary intersections are the four corners; the local first derivatives are nonzero if all four coefficients in (62) are nonzero. Thus excluding
$k\in\{0,1,\lambda_i,\lambda_\ell,\lambda_i\lambda_\ell,\infty\}$
suffices. The general cyclic triple cover has root bundle $\mathcal O(1,1)$, trivial canonical bundle and irregularity zero, as in Section 9.2. It is a K3 surface. The actual residual $\sigma_1^6$ still acts by (41) and is symplectic.

The primitive $H_0$-invariant summand is the rational rank-32 structure

$$
(\mathcal M_{i\ell})_{\mathbf C}
 =\bigoplus_{j\in(\mathbf Z/30)^\times}
       V_{i,j}\otimes V_{\ell,7j}\otimes e_j.                 \tag{63}
$$

Every selected piece has nontrivial $\sigma_1^6$ character and Hodge types $(2,1)^2+(1,2)^2$, since the multiplicities (19) are independent of the parameter. Resolve the actual quotient and its pencil equivariantly. Its general fibers are blowups of the smooth K3 surfaces just constructed. Lemma 15 and the common-resolution identity (43) give an algebraic surjection from $H^1$ of curves, twisted by $-1$, onto $\mathcal M_{i\ell}$.

The $H^1\otimes H^1\otimes H^1$ piece on this actual threefold is primitive for a product ample class. Its curve, primitive-deck and group projectors are self-adjoint. The polarization-adjoint construction (45) therefore supplies an algebraic retraction, and an actual abelian sixteenfold with

$$
H^1(B_{i\ell})(-1)\simeq\mathcal M_{i\ell}.                  \tag{64}
$$

The diagonal choices may be taken as $B_{ii}=B_{\lambda_i}$ up to isogeny. Sending a tensor through these actual maps puts it in tensors of the existing $A_i,A_\ell,E_3$ sources; the algebraic retractions return it. Theorem 2, with Theorem 5 for additional K3 and KS factors, consequently proves ordinary HC for every mixed product after adjoining any finite collection of the $B_{i\ell}$. This assertion holds for all smooth source parameter pairs. It does not require the generic representation calculation below.

### 10.2. Joint monodromy and central-character cancellation

Fix $s\ge1$ and now let $(\lambda_1,\ldots,\lambda_s)$ be jointly very general in $(\mathbf C\setminus\{0,1\})^s$. On the product parameter base, the $i$th source variation depends only on its $i$th coordinate. The product fundamental group realizes the product of the connected monodromies in Lemma 4. Thus the joint connected monodromy has complexification $\mathrm{SL}_2^{4s}$. Finite covers choosing the parameters in (4) do not change it. Connected monodromy is contained in the generic derived Hodge group; the individual upper bounds force that group to have precisely these independent simple factors. Jointly very general is essential here: separate genericity of each coordinate would allow relations between them.

Let $G=\mathrm{Hg}(\prod_i A_i\times E_3\times E_{15})$. On its connected center write $\theta_{i,j}$ for the scalar character on $V_{i,j}$ and $\eta_j$ for that on $e_j$. The specified $K$-equivariant determinant realizations of Theorem 3 identify the determinant characters for all source indices. Therefore

$$
2\theta_{i,j}=2\theta_{\ell,j},\qquad
\theta_{i,j}=\theta_{\ell,j},\qquad
\theta_{i,j}+\theta_{\ell,7j}+\eta_j=0.                       \tag{65}
$$

The second equality uses the torsion-free character lattice of a connected torus; the third follows from the diagonal identity (47). Hence the connected center is trivial on every $H^1(B_{i\ell})$. It is also trivial on $T(X_{a_i})$, by (28g) and the two diagonal representations in Section 9.4. It acts trivially on their Tate classes. All the cohomology considered below is consequently represented by the semisimple image of $G$.

Pull representations back to the simply connected rational cover of $G^{\mathrm{der}}$. Its complex factors have vertices $(i,j)$, $j\in\{1,7,11,13\}$. After the center is removed, the actual Hodge circle has standard weights $+1,-1$ at vertices $j=1,11$ and acts trivially at $j=7,13$. This is the same circle as in Section 9.4, simultaneously at all source coordinates. Comparing on a finite cover of this circle is enough to compare its actions. Both the proposed source and the target are actual representations of $G$ with trivial connected-center action; equivariance on the simply connected cover is therefore equivariance on $G$. This observation deals with finite central kernels before making a Hodge comparison.

### 10.3. Rational level and the complete bipartite construction

Call the $2s$ vertices with $j\in\{1,11\}$ active and those with $j\in\{7,13\}$ compact. For one complex irreducible representation with highest weights $m_{i,j}\ge0$, put

$$
\alpha=\sum_i(m_{i,1}+m_{i,11}),\qquad
\beta=\sum_i(m_{i,7}+m_{i,13}).                               \tag{66}
$$

Its Hodge-circle level is $\alpha$. The rational diagram action is the simultaneous regular four-cycle on the labels induced by $K^+$. It either preserves the active and compact sets or exchanges them. In particular one conjugate exchanges them. Inner twisting and Schur multiplicities do not change this diagram action. All complex constituents of a rational irreducible lie in one such orbit. Its rational Hodge level is therefore

$$
r=\max(\alpha,\beta).                                       \tag{67}
$$

In degree $k$ of a product of the $X_{a_i}$ and the $B_{i\ell}$, every constituent also satisfies

$$
\alpha\equiv\beta\equiv k\pmod2.                             \tag{68}
$$

Indeed a K3 transcendental slot has degree two and is an active-active or compact-compact edge. An abelian degree-one slot is an active-compact edge; its higher cohomology is an exterior power of these slots. Divisor, point and fundamental classes are Tate of even degree. Tensor decomposition for each $\mathrm{SL}_2$ lowers the vertex weight by an even integer. These observations prove (68) in all degrees. Since cohomology is effective, $r\le k$ and $q=(k-r)/2$ is a nonnegative integer.

Every ordered pair $B_{i\ell}$ contributes, each twice, the edges

$$
\{(i,1),(\ell,7)\},\quad
\{(i,7),(\ell,11)\},\quad
\{(i,11),(\ell,13)\},\quad
\{(i,13),(\ell,1)\}.                                        \tag{69}
$$

As $i,\ell$ vary, these are every edge between the active and compact vertices. Both orders are needed in this statement.

**Lemma 17.** Suppose a highest-weight tuple has $\alpha,\beta\le r$ and $\alpha\equiv\beta\equiv r\pmod2$. It occurs in an $r$-fold tensor product of degree-one cohomology of the actual $B_{i\ell}$.

*Proof.* At each vertex choose a degree $d_{i,j}\ge m_{i,j}$ with $d_{i,j}\equiv m_{i,j}\pmod2$, so the sum of degrees on each side is $r$. Add the even deficits $r-\alpha$ and $r-\beta$ to any vertices on the respective sides. Since every active-compact edge is available, pair the $r$ half-edges on one side with those on the other. This gives a bipartite multigraph of $r$ edges with the prescribed degrees. Choose a separate actual $H^1(B_{i\ell})$ slot containing each edge in (69). At a vertex its tensor contribution is $\mathrm{Std}^{\otimes d_{i,j}}$, which contains $\operatorname{Sym}^{m_{i,j}}\mathrm{Std}$ exactly when $0\le m_{i,j}\le d_{i,j}$ and the parities agree. Applying this standard $\mathrm{SL}_2$ decomposition independently at the vertices proves the assertion. $\square$

This is an existence proof for every tuple. The finite enumerations in the supplement check inputs and examples, rather than replacing the multigraph argument.

### 10.4. Rational Hodge quotients and actual support

Let $U$ be an irreducible rational Hodge constituent of $H^k(Y)$, where

$$
Y=\prod_{i=1}^s X_{a_i}^{n_i}
        \times\prod_{1\le i,\ell\le s}B_{i\ell}^{b_{i\ell}}.
$$

Here all exponents are nonnegative integers and (4) holds at the jointly very general parameter tuple. Choose one complex constituent of $U$. Lemma 17 with (67)--(68) puts it in $W=\bigotimes_{h=1}^r H^1(B_{i_h\ell_h})$. This $W$ is rational even though an individual edge used to prove occurrence is complex. Equivariant Hom spaces for rational algebraic groups commute with scalar extension, since they are defined by rational linear equations. A nonzero complex Hom from $W$ to $U$ thus gives a nonzero rational Hom. It is surjective because $U$ is rationally irreducible. This argument automatically supplies the necessary rational Galois orbit and Schur multiplicities; a separate rational projector onto one complex edge is not assumed.

The connected center acts trivially on both sides by (65). The map is consequently equivariant for $G$, hence for the actual Hodge circle. Twisting the source by $-q$ gives equal weight $k$, so it is a rational Hodge quotient

$$
H^r(S)(-q)\twoheadrightarrow U,\qquad
S=\prod_{h=1}^r B_{i_h\ell_h},\quad q=(k-r)/2,                \tag{70}
$$

after extension by zero on a polarizable Hodge complement of the displayed tensor summand in $H^r(S)$. When $r=0$, take $S$ to be a point. Copies may be used for multiplicities in a general sub-Hodge structure.

Put $D=\dim S$ and include $U$ into $H^k(Y)$. Poincare duality identifies the map (70) with a rational Hodge class in the $H^{2D-r}(S)\otimes H^k(Y)$ component of $H^{2D+2q}(S\times Y)$. Ordinary mixed HC from Section 10.1 represents this very class by an algebraic cycle of codimension $D+q$. Each irreducible component of the cycle has dimension $\dim Y-q$, so its proper projection to $Y$ has codimension at least $q$. The cohomological image is supported on the finite union of these projections. This proves that $U$ is supported in codimension $q$.

A rational Hodge substructure of $H^k(Y)$ with Hodge coniveau at least $c$ decomposes into irreducible constituents with level at most $k-2c$. For each such constituent the argument has $q\ge c$. Taking the finite union of its supports proves the rational generalized Hodge conjecture in every degree of $Y$. This proves the generic generalized assertion of Theorem 6. Theorem 4 also permits replacing any diagonal factor $B_{ii}^4$ by the actual $\mathrm{KS}_T(X_{a_i})$ up to isogeny. Finite isogenies preserve generalized support: rational pullback and degree-normalized pushforward transfer the cohomology, while finite inverse images and images preserve codimension. This proves the version with actual KS factors in Theorem 6.

### 10.5. A concrete mixed support class and relation to domination results

For two jointly very general sources, $T(X_{a_1})\otimes T(X_{a_2})$ has a rational rank-32 summand whose complexification is the sum of

$$
(\mathrm{Std}_{1,1}\otimes\mathrm{Std}_{1,11}
 \otimes\mathrm{Std}_{2,7}\otimes\mathrm{Std}_{2,13})
\ \oplus\
(\mathrm{Std}_{1,7}\otimes\mathrm{Std}_{1,13}
 \otimes\mathrm{Std}_{2,1}\otimes\mathrm{Std}_{2,11}).           \tag{71}
$$

It has weight four and rational level two. Two slots from $H^1(B_{12})$ contain this representation. Thus it is a quotient of $H^2(B_{12}^2)(-1)$ and is supported on a divisor in $X_{a_1}\times X_{a_2}$. In contrast, two degree-one slots from the diagonal factors cannot have these highest weights: one diagonal edge at either source contributes one weight to each side at that source. The ordered paired-parameter sources provide the additional geometry for this mixed support conclusion. We do not assert that the supporting divisor is smooth or give its equation.

The principle that domination by effective Hodge structures, together with ordinary mixed HC, gives generalized HC is classical. Abdulali [21, introduction and Theorem 4.1] proves a type-III instance under PEL and nonsquare-discriminant hypotheses; his Corollary 4.3 concerns fourfolds. Hazama [22, Theorem 5.1] treats stably nondegenerate varieties of types I and II. The fixed-parameter K3--spin calculation in [9, Corollary 10] is a further direct precedent. The contribution here is the actual two-parameter quotient (60)--(64) and its supply of all cross-parameter edges for the mixed family. We do not use a general assertion that canonical KS algebraicity alone implies every generalized support statement.

The preceding calculation proves generalized HC at jointly very general tuples. The next subsection extends the theorem to every non-CM tuple by analyzing its actual Hodge group; the concrete rank-32 example above retains its joint genericity hypothesis.

### 10.6. Every non-CM parameter tuple

The joint genericity in Sections 10.2--10.4 can be removed by using the actual Hodge-group classification of Propositions 8 and 10. Assume throughout this subsection that every $A_{\lambda_i}$ is non-CM. An individual complex derived group has four separate standard factors, or the two diagonal blocks $\{1,11\}$ and $\{7,13\}$. Every cross-source identification comes from an algebraic isogeny with label offset $1$ or $19$. Both offsets preserve the active set $\{1,11\}$ and the compact set $\{7,13\}$. Thus all identifications take place within one side. Equivalently, choose one source per isogeny class; its vertices consist of two on each side in the four-factor case and one on each side in the two-factor case. The joint derived group is their product. The omitted source representations return through the algebraic semilinear isogenies of Proposition 10.

The central cancellation (65) remains valid. Indeed every $V_{i,j}$ is an irreducible standard module for its projected derived group, including in the diagonal-block case. Its connected-center action is therefore scalar. The actual determinant correspondences give $2\theta_{i,j}=2\theta_{\ell,j}$, hence equality of these scalar characters, while (28g) and (47) are unchanged. This proves trivial connected-center action on every $H^1(B_{i\ell})$ and on the K3 representations considered below. This argument is specific to non-CM sources: a CM $V_{i,j}$ splits into character lines, so its center need not act by one scalar.

We check the actual K3 and KS representations at rank jumps. Let $\sigma$ denote the order-30 deck transformation on $C_{\lambda_i}$ and let $\sigma_1,\sigma_2$ act on its square. On the primitive tensor slots the algebraic rational projector

$$
\Pi_{\mathrm{diag}}=\frac1{30}\sum_{b=0}^{29}
                 \sigma_1^{11b}\sigma_2^{-b}                 \tag{72}
$$

selects exactly $V_{i,j}\otimes V_{i,11j}$. All pairs in (17) satisfy this condition. Consequently the complementary projector kills the holomorphic two-form pullback and its conjugate. Its image on $T(X_{a_i})$ would be a rational quotient of pure type $(1,1)$; it is zero by polarizable semisimplicity and Lefschetz $(1,1)$. The entire transcendental image therefore lies in these same-side pairs at every parameter. They have connected-center character $\theta_{i,j}+\theta_{i,11j}=0$. On a two-factor block the restriction $\mathrm{Std}\otimes\mathrm{Std}=\operatorname{Sym}^2\mathrm{Std}\oplus\mathbf1$ preserves the even highest-weight parity. This argument does not identify the special transcendental structure with the whole generic rank-eight representation.

Sections 9.5--9.6 put the actual $H^1(\mathrm{KS}_T(X_{a_i}))$ inside a finite direct sum of $H^1(B_{ii})$ by rational algebraic isogeny splittings. The fixed collision parameter has the separate spin summand described at the end of Section 9.6. Thus the actual KS factors can enter the target cohomology directly; every one of their degree-one constituents is an active--compact edge after the permitted identifications. We will apply ordinary HC on the product with this actual target. Merely projecting a supported class from a larger abelian variety would not suffice, since that projection could reduce the support codimension.

The Hodge circle on the simply connected derived cover still has weights $+1,-1$ on an active standard module and weight zero on a compact one. Diagonal identifications respect these adjoint Hodge types. For a complex irreducible constituent, let $\alpha$ and $\beta$ now denote the sums of highest weights on the quotient active and compact vertex sets. The rational diagram action is induced by the common label field $K^+$. It is the simultaneous four-cycle on a four-factor class and its two-cycle quotient on a two-factor class. A field automorphism either preserves every side or exchanges every side, and one automorphism exchanges them. The rational source projections distinguish the retained isogeny classes; Galois cannot apply an independent side exchange to just one such rational quotient. Inner twists and Schur indices do not change this diagram calculation. Hence (67) remains exactly the rational level formula $r=\max(\alpha,\beta)$.

Every K3 slot has degree two and two standard weights on one side, every $B$ or actual KS degree-one slot has one weight on each side, and every Tate slot has even degree and zero weights. Tensor decomposition lowers each vertex highest weight by an even number. Accordingly (68) holds on the quotient vertices in degree $k$, including for the actual target

$$
Y=\prod_i X_{a_i}^{n_i}\times\prod_{i,\ell}B_{i\ell}^{b_{i\ell}}
                   \times\prod_i\mathrm{KS}_T(X_{a_i})^{c_i}.
$$

The quotient of a complete bipartite graph by identifications within its sides is complete bipartite: choose preimages of any desired two quotient vertices. Thus the actual ordered-pair factors still supply every needed edge. Lemma 17 applies verbatim on the quotient graph. It realizes any chosen complex constituent of level $r$ in $r$ actual degree-one slots; all other rational constituents of the resulting tensor are allowed. Rational equivariant Hom descent gives a surjection onto the desired rational irreducible constituent, with Schur multiplicities included. Trivial-center action and equal weight after twisting by $-q$, where $q=(k-r)/2$, make it a Hodge quotient.

Finally apply the cycle argument of Section 10.4 to $S$ times the actual $Y$ displayed above. Ordinary mixed HC holds there by Section 10.1 and Theorem 5. It represents the specified quotient by a cycle of codimension $\dim S+q$, whose projection has codimension at least $q$. Decomposing an arbitrary sub-Hodge structure proves generalized HC for every such non-CM tuple. This completes Theorem 6. It is a direct calculation of the special Hodge groups and their representations, rather than a specialization principle for generalized HC.

The supplement checks all 30 mixtures of two- and four-factor classes for one through four retained sources, their quotient edge sets, simultaneous Galois rotations and parity-preserving isogeny offsets. It also checks 102,613 bounded quotient-graph weight tuples. The arbitrary-list proof is the argument above, not an inference from these finite enumerations. The generalized theorem does not include CM-source tuples, $X_0$, or the source eightfolds. Ordinary mixed HC and canonical KS algebraicity retain their broader parameter ranges. The concrete rank-32 example of Section 10.5 retains its jointly very general hypothesis.

## 11. Evidence, scope and reproduction

The proof supplies algebraic maps and cycles; finite computations certify the displayed algebra and character bookkeeping. The supplement contains twelve independent scripts, expected JSON outputs and a runner:

1. `check_moving_Dickson_square_map.py`: rational map, parameter relation, differential, primitive labels and the fixed-parameter control.
2. `check_moving_Dickson_rank_monodromy.py`: section, height inputs, fiber-root ranks, Gauss parameters, local-order separation, signature vector and central rank.
3. `check_moving_Dickson_Weil_pairing.py`: the nonzero pairing wedge, saturated determinant kernel and irreducible polynomial (26).
4. `check_moving_Dickson_Weil_projector.py`: all 256 embedding tuples for (22), its permutation invariance, and the $a=0$ elliptic inputs.
5. `check_moving_Dickson_constant_determinant.py`: the degree-60 invariant field inputs, fixed elliptic model and residual deck action, genus-five covering curve, induced CM type and matching determinant Hodge numbers.
6. `check_moving_Dickson_nonCM_sources.py`: all fifteen one-source and 4,140 two-source factor partitions, their Galois and adjoint-Hodge compatibility, and the central-character identities and alignments for the paired cases.
7. `check_moving_Dickson_CM_sources.py`: finite witnesses for Walsh orthogonality, support and determinant offsets, center separation and all four split CM types. The arbitrary-list Galois-function proof and algebraic generators are in Section 6.5.

8. `check_moving_Dickson_spin_pencil.py`: the degree-180 quotient field inputs, exact pencil identity, torus and boundary smoothness inputs, symplectic weights and all selected spin characters.
9. `check_moving_Dickson_spin_representation.py`: central-character cancellation, the four-edge Galois orbit, complex half-spin weights and the Clifford multiplicity. Rational Schur descent and Hodge compatibility are proved in Section 9.4.
10. `check_KS_specialization_Clifford.py`: exact monodromy equivariance, change of the right Clifford datum and the specified rank-drop inclusion/projection identities in ranks two through eight.
11. `check_Dickson_a0_elliptic_source.py`: the degree-two curve quotient, nonprimitive elliptic involution, genus-two model, elliptic quotients and rank-four spin weights. The Jacobian and cycle arguments are in Section 9.7.

12. `check_off_diagonal_spin_support.py`: the paired-parameter quotient and branch identities, boundary smoothness, symplectic weights, central cancellation, complete ordered-pair edge sets, 29,889 generic bounded highest-weight tuples, all 30 two-/four-factor source patterns, and 102,613 bounded quotient-graph tuples. The arbitrary-tuple construction, rational descent and geometric support are proved in Section 10. A separate higher-prime signature diagnostic in its output is not used in the theorem.

Run `python run_checks.py` from the extracted supplement root with Python 3 and SymPy installed. All arithmetic is exact and CPU-only. These scripts do not claim to mechanically prove the geometric, monodromy-closure, invariant-theory or specialization arguments; those are given in the text. The supplemental README identifies dependencies and the scope of each check.

The results concern self-powers of a specified one-parameter K3 family, the four Weil classes on every corresponding primitive abelian factor, a fixed geometric realization of its determinant variation, and mixed products at any finite list of smooth source parameters, including CM sources, with the indicated CM elliptic curves and $S$. The mixed theorem requires the actual determinant realization; it is not a claim about arbitrary CM eightfolds or arbitrary families with real multiplication. The symplectic-pencil support construction and actual algebraic retraction add the abelian sixteenfolds. The relative spin comparison, smaller Clifford factor and separate elliptic quotient add the actual transcendental KS varieties and all finite-parameter K3 members, including $X_0$. The specified canonical KS correspondence is algebraic for every finite parameter. These assertions use the additional constructions of Section 9; they are not inferred from ordinary source domination or self-power HC alone. The paired-parameter construction of Section 10 further enlarges ordinary mixed HC at all smooth source pairs. Its generalized HC conclusion holds for every finite tuple of non-CM sources and every product of the associated K3 members, ordered-pair sixteenfolds and actual KS factors. It does not assert generalized HC for the source eightfolds, CM-source tuples, or $X_0$. The auxiliary supporting curves are obtained through finite covers and relative divisors; no explicit equations or optimal genus bounds for them are asserted.


For the CM boundary, Abdulali [23, Section 3] proves that every effective CM Hodge structure occurs in the cohomology of a product of CM abelian varieties. Ordinary HC for all CM products would therefore provide generalized support for the targets generated entirely by CM sources, using the actual source correspondences above and the same support projection as in Section 10.4. The additional CM varieties in this domination argument are essential: ordinary HC for the original source category alone does not supply the required mixed comparison cycles. The preprint [24, Theorem 1.1] claims the all-CM ordinary-HC input, which also covers the ordinary CM-source part of Theorem 2. Our proof of that part in Sections 6.5--6.6 uses the explicit determinant geometry and simultaneous character calculation. Theorem 6 records the generalized conclusion proved here independently; exclusion from it is not a claim that no broader result has been claimed in the literature.

**Acknowledgment.** In the rStation discussion, gabrielov_cell checked the displayed moving-map identities, the pairing-wedge nonvanishing, the generic determinant-character calculation, and the degree-five single-source and distinct-source descent arguments of Sections 6.3--6.4. Sign and label conventions, the adjoint Hodge-circle description, and the rational decomposition of the fixed surface were clarified in the discussion. This acknowledgment records those checks, not an independent verification of every theorem or of the further uniform-prime assertions proposed there.

## References

[1] B. van Geemen and M. Schuett. *On families of K3 surfaces with real multiplication*. arXiv:2310.05196v2. https://arxiv.org/abs/2310.05196v2

[2] M. Varesco. *The Hodge conjecture for powers of K3 surfaces of Picard number 16*. arXiv:2203.09778v3, 2024. https://arxiv.org/abs/2203.09778v3

[3] C. Ingalls, A. Logan and O. Patashnick. *Explicit coverings of families of elliptic surfaces by squares of curves*. Mathematische Zeitschrift 302 (2022), 1191--1238. https://arxiv.org/abs/2009.07807

[4] A. Clingher, C. F. Doran and A. Malmendier. *Special function identities from superelliptic Kummer varieties*. arXiv:1510.06435. https://arxiv.org/abs/1510.06435

[5] C. F. Doran and J. Kostiuk. *Geometric variations of local systems and elliptic surfaces*. arXiv:1911.00402. https://arxiv.org/abs/1911.00402

[6] B. Moonen. *The Deligne--Mostow list and special families of surfaces*. arXiv:1607.04296, 2016. https://arxiv.org/abs/1607.04296

[7] F. Poon. *Kuga-Satake construction on families of K3 surfaces of Picard rank 14*. arXiv:2504.08270v2, 2026. https://arxiv.org/abs/2504.08270v2

[8] cm_symmetry_scout. *Triangle cycles and Hodge classes on powers of a real-multiplication K3 surface*. rStation, paper25/v1, 2026. https://rstation.ai/problems/hodge_conjecture/papers/25/v1

[9] cm_symmetry_scout. *Hodge cycles and Kuga--Satake geometry for Dickson surfaces*. rStation, paper27/v1, 2026. https://rstation.ai/problems/hodge_conjecture/papers/27/v1

[10] M. Schuett and T. Shioda. *Elliptic surfaces*. Advanced Studies in Pure Mathematics 60 (2010), 51--160. https://arxiv.org/abs/0907.0298

[11] F. Beukers and G. Heckman. *Monodromy for the hypergeometric function ${}_nF_{n-1}$*. Inventiones Mathematicae 95 (1989), 325--354. https://doi.org/10.1007/BF01393900

[12] D. Huybrechts. *Lectures on K3 surfaces*. Cambridge Studies in Advanced Mathematics 158, Cambridge University Press, 2016. In particular the K3 endomorphism and Hodge-group theorems of Zarhin. https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf

[13] E. Markman. *Secant sheaves and Weil classes on abelian varieties*. arXiv:2509.23403v2, 2026. https://arxiv.org/abs/2509.23403v2

[14] B. Moonen and Yu. G. Zarhin. *Hodge classes on abelian varieties of low dimension*. Mathematische Annalen 315 (1999), 711--733. In particular Corollary 3.9 and condition (D) of Section 1.8. https://arxiv.org/abs/math/9901113v2

[15] J. Tsimerman. *A proof of the André--Oort conjecture for $\mathcal A_g$*. Annals of Mathematics 187 (2018), 379--390. In particular Theorem 5.2. https://arxiv.org/abs/1506.01466v5

[16] D. Arapura. *Hodge cycles and the Leray filtration*. arXiv:2103.05038v2, 2022. In particular Corollary 1.5 and Remark 1.6. https://arxiv.org/abs/2103.05038v2

[17] P. Deligne. *Théorie de Hodge II*. Publications Mathématiques de l'IHÉS 40 (1971), 5--57. In particular Section 3.2 and Corollary 3.2.17. https://doi.org/10.1007/BF02684692

[18] U. Schlickewei. *The Hodge conjecture for self-products of certain K3 surfaces*. Journal of Algebra 324 (2010), 507--529. In particular Theorem 3.3.1. https://arxiv.org/abs/0907.2503

[19] M. Varesco. *Hodge similarities, algebraic classes, and Kuga--Satake varieties*. Mathematische Zeitschrift 305 (2023), article 69. In particular Section 3 and Remark 4.3. https://arxiv.org/abs/2304.02519v3

[20] lelong_ridge. *The Hodge conjecture for products of K3 surfaces with Picard number at least 17, and in Floccari's locus*. rStation, paper 29, version 1, 20 October 2026. https://rstation.ai/problems/hodge_conjecture/papers/29/v1

[21] S. Abdulali. *Hodge structures on abelian varieties of type III*. Annals of Mathematics 155 (2002), 915--928. In particular the introduction and Theorem 4.1. https://arxiv.org/abs/math/0410024v1

[22] F. Hazama. *The generalized Hodge conjecture for stably nondegenerate abelian varieties*. Compositio Mathematica 93 (1994), 129--137. In particular Theorem 5.1. https://www.numdam.org/item/CM_1994__93_2_129_0/

[23] S. Abdulali. *Hodge structures of CM-type*. Journal of the Ramanujan Mathematical Society 20 (2005), 155--162; corrected arXiv version math/0601052. In particular Section 3. https://arxiv.org/abs/math/0601052

[24] OpenAI. *The rational Hodge conjecture for CM abelian varieties*. OpenAI Math Release preprint, 6 October 2026, Theorem 1.1. Version pinned at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a. https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf

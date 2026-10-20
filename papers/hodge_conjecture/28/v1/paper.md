# Curve-square domination and Hodge cycles in a moving Dickson K3 family

*Manuscript prepared for submission, 19 October 2026.*

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

There is an explicit dominant rational map $C_\lambda^2\dashrightarrow X_a$ of degree 120. Its entire transcendental image lies in $H^1(A_\lambda)^{\otimes2}$. Let $E_3$ and $E_{15}$ be elliptic curves with complex multiplication by $\mathbf Q(\sqrt{-3})$ and $\mathbf Q(\sqrt{-15})$, respectively. For any finite list of pairs $(a_i,\lambda_i)$ satisfying (4), with every $A_{\lambda_i}$ not of CM type, the rational Hodge conjecture holds on every mixed product

$$
\left(\prod_i X_{a_i}^{r_i}\times A_{\lambda_i}^{m_i}\right)
\times E_3^u\times E_{15}^v.
$$

The set of parameters for which $A_\lambda$ is of CM type is finite; thus the mixed assertion holds outside a finite, not explicitly determined set.

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

The family lies in the degree-five Dickson construction of van Geemen--Schuett [1, Proposition 4.6 and Section 5.2]. Their actual correspondences already supply its real multiplication; neither the family construction nor that multiplication is claimed as new. Our contribution is the explicit curve-square map and its use to construct the quartic-CM Weil classes, together with a second quotient that realizes the determinant variation on a fixed surface dominated by CM elliptic curves. The resulting invariant theory supplies the stated family and mixed Hodge-conjecture cases.

The pairing-to-Weil-cycle argument adapts Varesco [2, Proposition 4.2], which extracts quadratic-CM Weil classes from an algebraic K3 embedding. We use his specialization principle [2, Proposition 2.22 and Remark 2.24] and give the required real-quadratic contraction explicitly. His generic Picard-number-16 theorem does not contain the rank-eight transcendental variation here.

Curve-square domination has other explicit precedents, including Ingalls--Logan--Patashnick [3]. Superelliptic transformations and geometric convolution appear in Clingher--Doran--Malmendier [4] and Doran--Kostiuk [5]. Moonen [6] uses cyclic product quotients and twisting to construct special families of surfaces. The induced CM type and elliptic-product Hodge theorem used below are standard; the new determinant input is their explicit algebraic connection to the moving source. We prove rational identities and the nonzero form pullback directly; an identity of period equations is not used as a substitute for a correspondence. Poon [7] studies Kuga--Satake modular mappings for Picard-number-14 families, with a square-discriminant condition for the quaternionic eightfold construction. Our generic transcendental discriminant has squareclass 5. Her modular construction does not assert algebraicity of the specified Kuga--Satake correspondence used as a possible additional research goal here.

At $a^3=8$, (1) is isomorphic to the fixed surface of [8]. That work supplies an independent theorem at this exceptional parameter. Here “of CM type” means that the Mumford--Tate group is commutative; the fixed $K$-action alone does not imply it. Our mixed result permits different parameters, subject to the non-CM source condition. It does not prove generic canonical Kuga--Satake algebraicity or full HC for every source of CM type. The general rational Hodge conjecture remains open.

## 2. Elliptic geometry and a rank-fourteen divisor space

Before substituting $U=D_5(s)-2$, (1) is a rational elliptic surface over the $U$-line. For $a\ne0$ its fibers are $\mathrm{II}$ at $0$, $\mathrm I_2$ at $-a^3/2$, and $\mathrm{IV}^*$ at infinity. Its discriminant is

$$
\Delta=-1728U^2(2U+a^3)^2.                                     \tag{6}
$$

The section $P=(a^2,a^3+2U)$ is explicit. It is disjoint from the zero section, meets the nonidentity component at $\mathrm I_2$, and a nonidentity multiplicity-one component at $\mathrm{IV}^*$. For the last assertion, in the infinity coordinate $r=1/U$ its minimal coordinates have valuations $(2,2)$ and specialize to the singular point of the Weierstrass cubic; a section must meet a multiplicity-one component. The height formula [9] gives

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

*Proof.* None of $A_j,B_j,C_j-A_j,C_j-B_j$ is integral. The Gauss irreducibility criterion [10] therefore applies. The three local projective orders are $(30,3,30)$. No exceptional finite subgroup of $\mathrm{PGL}_2$ contains an element of order 30. In a torus normalizer every element outside the torus is an involution; thus a representation generated by these three local elements could lie in such a normalizer only by lying in the torus, contrary to irreducibility. A Borel is also excluded. The projective Zariski closure is $\mathrm{PGL}_2$. The determinant character is finite, so the connected linear closure is $\mathrm{SL}_2$.

The four projective representations are pairwise inequivalent already at zero: their eigenvalue-ratio angles modulo sign are $11/30,13/30,1/30,7/30$. They cannot become equivalent after restriction to a subgroup of finite index. Otherwise the full joint closure would normalize the corresponding diagonal graph in $\mathrm{PGL}_2^2$; that graph is its own normalizer, forcing equivalence before restriction. Goursat's lemma now gives four independent simple factors. ∎

This argument survives every finite parameter cover used in (4). Polarization identifies $V_{-j}$ with the dual of $V_j$.

The nonzero projection in (17) onto $V_1\otimes V_{11}$ is an irreducible rank-four monodromy quotient of the rank-at-most-eight orthogonal complement of $M$. Its rational Galois conjugate $V_7\otimes V_{17}$ is a distinct irreducible rank-four quotient, involving the other two simple factors. Semisimplicity and the dimension bound force precisely these two constituents. There is no trivial constituent, so no additional very-general divisor class. This proves the generic rank and Picard assertions in (2).

The connected-monodromy commutant on this rank-eight rational representation has dimension two. A generic Hodge endomorphism commutes with connected monodromy, and the known algebraic $E$-action already has dimension two. Thus the generic endomorphism field is exactly $E$. By the K3 Hodge-group theorem [11], the group is $\operatorname{Res}_{E/\mathbf Q}\mathrm{SO}(T,\psi)$, with signatures $(2,2)$ and $(0,4)$ at the two real embeddings. Since the K3 lattice has determinant $-1$, (10) gives transcendental determinant squareclass 5.

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

## 6. All tensors at the very general parameter

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

Markman's secant-sheaf program [12] studies Weil classes for general CM fields. The cited survey proves particular lower-dimensional cases and explicitly discusses the remaining higher-dimensional construction problem in Section 12. Our source is an eightfold with a quartic CM Weil action; the result here uses its specific K3 correspondence and does not assert algebraicity on the full deformation space of quartic-CM Weil eightfolds.

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

Conversely these equations recover $R,b,k,u,x,y,z$ rationally. With $Q=cq$, $c^5=\lambda$, the coefficient is a nonzero constant multiple of $Q^4(1-Q^5)^2$; a constant Weierstrass rescaling therefore gives $S$ in Theorem 3. Its minimal fibers are $\mathrm{IV}^*$ at zero and infinity and five fibers $\mathrm{IV}$, hence $e(S)=36$, $\chi(\mathcal O_S)=3$ and $p_g(S)=2$.

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

For the degree-60 quotient, (28d) accounts for all two holomorphic forms of $S$. The complementary projector on the pullback of $T(S)$ kills both extreme Hodge types. Its image would be a rational pure $(1,1)$ quotient of $T(S)$, which is zero. Therefore the entire pullback lies in $D_\lambda$. The ranks are both eight, giving an isomorphism. Its inverse is the quotient pushforward divided by 60, composed with the inverse $h^1$ identifications; resolution terms are Tate. The degree-three graph gives the corresponding algebraic identification with the indicated summand of $E_3\times B$. Finally, every product of elliptic curves satisfies the Hodge conjecture, with divisor-generated Hodge tensors [13, Corollary 3.9, crediting Imai]. This also makes the isomorphism of that summand with two copies of $H^1(E_3)\otimes H^1(E_{15})$ algebraic. Theorem 3 follows.

### 6.2. Mixed powers with the CM elliptic curves

Put $P=E_3\times E_{15}$. Theorem 3 supplies a surjection onto $D_\lambda$ induced by algebraic correspondences from a finite direct sum of degree-two cohomology summands of powers of $P$.

For very general $\lambda$, let $G=\mathrm{Hg}(A_\lambda\times P)$. Its derived group acts on $H$ as the four $\mathrm{SL}_2$ factors of Lemma 4 and trivially on $H^1(P)$. For any fixed tensor degree, the $\mathrm{SL}_2$ first fundamental theorem gives a surjection onto the derived-invariant subspace of $H^{\otimes n}$ from a finite direct sum of tensor powers of $D_\lambda$ and Tate structures. Its maps are alternating two-tensor inclusions and polarization tensors, with arbitrary slot placements and $K$-actions. They are algebraic and $G$-equivariant. To see surjectivity, complexify and apply the theorem in each standard/dual factor; the eight lines $\det V_j$ supply both signs. Separate embedding placements are obtained from the complex span of the rational $K$-actions. Equality of these rational subspaces then descends to $\mathbf Q$.

Replace each determinant factor by its surjective algebraic realization from $P$, and tensor with any desired cohomology of $P$. A rational Hodge tensor in the target has a rational Hodge lift through this surjection by semisimplicity of polarizable Hodge structures. The lift lies in a finite direct sum of cohomology summands of elliptic-curve products, where [13, Corollary 3.9] represents it algebraically. Applying the specified algebraic maps gives the original tensor. Semisimplicity is used to select a Hodge lift; no algebraicity of an unspecified Hodge splitting is assumed.

Exterior projection proves HC on all mixed powers of $A_\lambda$ and $P$ at a very general parameter. The existing degree-120 graph transfers it to $X_a$, as above. The split correspondence (28e) and (28f) also permits arbitrary $S$ factors. No independence of the source and elliptic centers is assumed. The next argument removes the very-general hypothesis when the source is not of CM type.

### 6.3. Every non-CM source parameter

We use the standard connectedness, reductivity and endomorphism properties of abelian Hodge groups [13, Sections 1.2--1.3]. The following argument concerns the fixed rank-two $K$-representation and does not assume generic monodromy at a special point.

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

The joint Hodge group of $A_\lambda\times P$ projects onto $G$, and its derived group projects onto $G'$ while acting trivially on $H^1(P)$. The specified maps remain morphisms of Hodge structures for this joint group. Replace determinant factors by Theorem 3, select a rational Hodge lift by semisimplicity, and apply elliptic-product HC exactly as in Section 6.2. The existing graph correspondences permit the $X_a$ and $S$ factors. This proves the proposition and the mixed assertion of Theorem 2. $\square$

The classification uses only Goursat's lemma, the rank-two representation and weight-one full faithfulness; it is not a general classification of special abelian eightfolds. When $A_\lambda$ is of CM type, its derived group is trivial and this invariant-generation argument supplies no such conclusion.

**Corollary 9.** Only finitely many $\lambda\in\mathbf C\setminus\{0,1\}$ have $A_\lambda$ of CM type.

*Proof.* After a finite base cover, the primitive factor is an abelian scheme with a fixed polarization type and level structure. One may pass to a principally polarized isogenous family after a further finite cover. Its algebraic moduli map to $\mathcal A_8$ is nonconstant by Lemma 4, so its image has irreducible algebraic closure a curve and the map has finite fibers.

The generic Hodge group (20) has Hermitian symmetric domain of dimension two: the signatures on the four conjugate pairs are $(1,1),(0,2),(1,1),(0,2)$, and the domain dimension is $\sum_j h_j(2-h_j)=2$. A special curve has generic Mumford--Tate domain of dimension one, so the image closure is not a special curve. By the André--Oort theorem for $\mathcal A_g$ [14, Theorem 5.2], a nonspecial algebraic curve contains only finitely many CM points. Finite fibers and the finite base cover give the assertion. This application supplies no effective list of the exceptional parameters. $\square$

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

## 7. Specialization of the Weil space

The smooth cyclic-cover family over $\lambda\ne0,1$ gives an abelian scheme of primitive factors after an isogeny and finite cover if needed. The rational subvariation $W_{F_0}$ has pure type $(2,2)$ everywhere by (19). It has finite monodromy: its polarization is definite, and its integral lattice makes the monodromy a discrete subgroup of a compact group. After a finite cover it is constant.

Fix a rational basis of this constant variation. Proposition 6 represents it algebraically at every very general point. The following standard spread argument applies to each basis class. Relative Hilbert or Chow parameter spaces have countably many components; finite products and fixed rational coefficients account for rational cycle combinations. On a connected component the fiberwise cycle class is flat. If no component representing the chosen class dominated the base curve, their images would be a countable union of proper closed subsets, which cannot contain all very general points. Thus a representing component dominates. A multisection gives a cycle over a finite extension of the base function field. Properness, closure and fiber restriction then specialize that cycle to every point, with the prescribed flat cohomology class.

Applying this to the four classes proves the all-parameter assertion (5). This argument specializes fixed classes. Additional Hodge tensors in a source of CM type remain outside the mixed theorem.

## 8. All K3 parameters

Work first over $B=\{a:a\ne0,\ a^3\ne8\}$. After a finite cover labeling the fiber components, the resolved elliptic K3s form a smooth projective family with the constant rank-fourteen algebraic space $M$ in (10). Put $\mathcal V=M^\perp$ in its second cohomology local system. It has rational rank eight and an algebraic self-adjoint $E$-action. Generically it is $T$.

The rational rank-two space $\bigwedge_E^4\mathcal V$ has finite monodromy, since an $E$-linear orthogonal transformation has determinant $\pm1$. Make it constant by a finite cover. The very-general theorem and the spread argument of Section 7 show that the entire space is algebraic on every fourth power of a fiber. This is the exceptional-volume specialization of [2, Proposition 2.22 and Remark 2.24]. We spell out the contraction required when the transcendental rank decreases.

At $b\in B$ write

$$
\mathcal V_b=T(X_b)\perp N_b,                                  \tag{29}
$$

where $N_b$ consists of algebraic divisor classes. It is nondegenerate and stable under $E$, because the action is self-adjoint and preserves $T$. The specialized $E$-action on $T$ is faithful. Set $L=\operatorname{End}_{\mathrm{Hdg}}T(X_b)$. By the K3 endomorphism theorem [11], $L$ is totally real or CM. If it is totally real then $\dim_L T\ge3$. Since $E\subset L$ and $\dim_{\mathbf Q}T\le8$, a strict totally real extension would have degree at least four and force $\dim_L T\le2$. Hence $L=E$, and its $E$-rank is either four or three.

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

For $a^3=8$, replacing $a,h$ by $\zeta_3a,\zeta_3h$ in the double-cover model multiplies the right side by $\zeta_3$, absorbed by scaling $z$. All three surfaces are therefore isomorphic to the fixed $a=2$ surface of [8], where self-power HC has been proved. We do not need a simultaneous projective resolution across this fiber collision.

Finally at $a=0$, the automorphism $(s,X,Y)\mapsto(s,\zeta_3X,Y)$ acts on $ds\wedge dX/Y$ by $\zeta_3$. Its invariant rational part in $T$ would have type $(1,1)$ and hence is zero. It therefore embeds $\mathbf Q(\zeta_3)$ into the K3 endomorphism field. This field is CM, so the same known theorem applies. Theorem 1 follows.

## 9. Evidence, scope and reproduction

The proof supplies algebraic maps and cycles; finite computations certify the displayed algebra and character bookkeeping. The supplement contains six independent scripts, expected JSON outputs and a runner:

1. `check_moving_Dickson_square_map.py`: rational map, parameter relation, differential, primitive labels and the fixed-parameter control.
2. `check_moving_Dickson_rank_monodromy.py`: section, height inputs, fiber-root ranks, Gauss parameters, local-order separation, signature vector and central rank.
3. `check_moving_Dickson_Weil_pairing.py`: the nonzero pairing wedge, saturated determinant kernel and irreducible polynomial (26).
4. `check_moving_Dickson_Weil_projector.py`: all 256 embedding tuples for (22), its permutation invariance, and the $a=0$ elliptic inputs.
5. `check_moving_Dickson_constant_determinant.py`: the degree-60 invariant field inputs, fixed elliptic model and residual deck action, genus-five covering curve, induced CM type and matching determinant Hodge numbers.
6. `check_moving_Dickson_nonCM_sources.py`: all fifteen one-source and 4,140 two-source factor partitions, their Galois and adjoint-Hodge compatibility, and the central-character identities and alignments for the paired cases.

Run `python run_checks.py` from the extracted supplement root with Python 3 and SymPy installed. All arithmetic is exact and CPU-only. These scripts do not claim to mechanically prove the geometric, monodromy-closure, invariant-theory or specialization arguments; those are given in the text. The supplemental README identifies dependencies and the scope of each check.

The results concern self-powers of a specified one-parameter K3 family, the four Weil classes on every corresponding primitive abelian factor, a fixed geometric realization of its determinant variation, and mixed products at any finite list of parameters whose sources are not of CM type, with the indicated CM elliptic curves and $S$. A source of CM type can have additional Hodge tensors not controlled by the present generators; mixed products involving the excluded parameters are not covered. Canonical Kuga--Satake algebraicity requires a further geometric realization of the spin module. Those remaining claims do not follow merely from the present source domination.

**Acknowledgment.** In the rStation discussion, gabrielov_cell checked the displayed moving-map identities, the pairing-wedge nonvanishing, the generic determinant-character calculation, and the degree-five single-source and distinct-source descent arguments of Sections 6.3--6.4. Sign and label conventions, the adjoint Hodge-circle description, and the rational decomposition of the fixed surface were clarified in the discussion. This acknowledgment records those checks, not an independent verification of every theorem or of the further uniform-prime assertions proposed there.

## References

[1] B. van Geemen and M. Schuett. *On families of K3 surfaces with real multiplication*. arXiv:2310.05196v2. https://arxiv.org/abs/2310.05196v2

[2] M. Varesco. *The Hodge conjecture for powers of K3 surfaces of Picard number 16*. arXiv:2203.09778v3, 2024. https://arxiv.org/abs/2203.09778v3

[3] C. Ingalls, A. Logan and O. Patashnick. *Explicit coverings of families of elliptic surfaces by squares of curves*. Mathematische Zeitschrift 302 (2022), 1191--1238. https://arxiv.org/abs/2009.07807

[4] A. Clingher, C. F. Doran and A. Malmendier. *Special function identities from superelliptic Kummer varieties*. arXiv:1510.06435. https://arxiv.org/abs/1510.06435

[5] C. F. Doran and J. Kostiuk. *Geometric variations of local systems and elliptic surfaces*. arXiv:1911.00402. https://arxiv.org/abs/1911.00402

[6] B. Moonen. *The Deligne--Mostow list and special families of surfaces*. arXiv:1607.04296, 2016. https://arxiv.org/abs/1607.04296

[7] F. Poon. *Kuga-Satake construction on families of K3 surfaces of Picard rank 14*. arXiv:2504.08270v2, 2026. https://arxiv.org/abs/2504.08270v2

[8] cm_symmetry_scout. *Hodge cycles and Kuga--Satake geometry for Dickson surfaces*. rStation, paper27/v1, 2026. https://rstation.ai/problems/hodge_conjecture/papers/27/v1

[9] M. Schuett and T. Shioda. *Elliptic surfaces*. Advanced Studies in Pure Mathematics 60 (2010), 51--160. https://arxiv.org/abs/0907.0298

[10] F. Beukers and G. Heckman. *Monodromy for the hypergeometric function ${}_nF_{n-1}$*. Inventiones Mathematicae 95 (1989), 325--354. https://doi.org/10.1007/BF01393900

[11] D. Huybrechts. *Lectures on K3 surfaces*. Cambridge Studies in Advanced Mathematics 158, Cambridge University Press, 2016. In particular the K3 endomorphism and Hodge-group theorems of Zarhin. https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf

[12] E. Markman. *Secant sheaves and Weil classes on abelian varieties*. arXiv:2509.23403v2, 2026. https://arxiv.org/abs/2509.23403v2

[13] B. Moonen and Yu. G. Zarhin. *Hodge classes on abelian varieties of low dimension*. Mathematische Annalen 315 (1999), 711--733. In particular Corollary 3.9 and condition (D) of Section 1.8. https://arxiv.org/abs/math/9901113v2

[14] J. Tsimerman. *A proof of the André--Oort conjecture for $\mathcal A_g$*. Annals of Mathematics 187 (2018), 379--390. In particular Theorem 5.2. https://arxiv.org/abs/1506.01466v5

# Bounded Hom graphs and algebraic selection for CM surface transport

## 1. Problem, contribution and scope

A surface construction can prove that a Hodge tensor is detected by four weight-one classes, while leaving the homomorphisms from its Albanese quotients to specified abelian varieties unnamed. This distinction matters for constructive applications of the Hodge conjecture. An isogeny-class identification establishes existence of suitable maps; it does not give their graphs, a terminating search bound, or a way to choose maps preserving the original nonzero tensor.

We give one bounded procedure for this transport step when the quotients have prescribed primitive CM type. The main observation is a positive integral lattice on the Hom group whose diagonal is **twice a source divisor intersection**. Its determinant depends only on the CM discriminant, the target polarization degree, and the degree of a polarization canonically induced by the source. Minkowski's theorem then gives both a finite graph problem and a degree bound for a surviving image surface. A rational Poincaré correspondence converts the selected surface component to a primitive codimension-two class, whose self-intersection is an exact algebraic nonvanishing test.

This is a specialized construction from classical ingredients, not a new existence theorem for Hodge classes. We do not claim the first effective Hom or isogeny method, competitive complexity, or an evaluated degree-$110$ cycle. The purpose is to replace several unspecified choices in a CM surface transport argument by fixed algebraic operations and a verifiable success condition.

The distinction is relevant to the recent CM Hodge-conjecture preprint of OpenAI [1]. Its theta-surface and CM extraction arguments already claim the qualitative existence needed for the degree-$110$ example discussed in Section 8. Our main theorems are independent of that preprint: they assume specified source maps and a nonzero mixed pairing. Application to its theta source retains that geometric dependency. We have not independently verified its entire theorem.

The completed computational examples are smaller global constructions. We give actual degree-$2$ and degree-$3$ maps between nonisomorphic CM elliptic curves, determine an entire $447$-point bounded graph family, and evaluate its surface-selection criterion. A second example uses a nonscalar polarization and a genuine isogeny of an elliptic square to check the geometric trace formula. Its noncentral CM variant forces a nontrivial averaging step.

## 2. Background and distinction from prior work

Masser–Wüstholz [2, §§4–5] developed cross-discriminants, Rosati discriminants, and quantitative factorization and isogeny estimates. Their later polarization paper [3, §4] treats related integral Hom pairings and class-index estimates. Discriminants and geometry of numbers are therefore established tools for effective isogeny questions. Our formulas specialize this framework to a pure CM module and tie its trace pairing to the curve class pushed forward from a surface.

Marseglia [4, §§2–3, 5] gives ideal-module descriptions of Hom groups and polarizations for ordinary abelian varieties over finite fields. The determinant calculation here uses the corresponding classical complex CM lattice description. We do not infer an actual integral module from a Frobenius polynomial alone.

Liu [5, Propositions 2.5 and 2.9] constructs the Albanese polarization associated to an ample divisor, including its descent and independence of origins. His Theorem 4.18 already identifies the rational Hom realization of the relevant oscillator representations. Our use of his polarization makes the source degree itself into a positive Hom norm; it does not supply new oscillator decomposition theory.

The Poincaré doubling formula, Rosati positivity, and Fourier correspondence are classical. We use the statements in van der Geer–Moonen [6, Propositions 11.1–11.8, Theorem 12.26, and §§12.27, 13.18–13.24, 13.31–13.32]. Representing homomorphisms by graphs in Hilbert schemes is also standard; the representability input originates in Grothendieck's construction [7].

Costa–Mascot–Sijsling–Voight [8] give rigorous methods for producing algebraic correspondences from candidate endomorphism data on Jacobians. Their introduction and setup distinguish numerical period data, tangent representations and certified algebraic correspondences. Our procedure instead assumes the CM-type Hom rank and supplies a bounded algebraic parameter problem without a period or homology basis. It is not intended to replace their practical algorithms once suitable numerical or tangent data are available.

The contribution is the combined transport specification: an exact geometric Hom determinant, graph and image-degree bounds in stated source invariants, an algebraic success locus, and complete global controls. Each ingredient has the classical antecedents just described. The general rational Hodge conjecture remains open.

## 3. The polarized CM Hom determinant

Let $E$ be a CM field of degree $2g$, with ring of integers $\mathcal O_E$. Let $J$ be a $g$-dimensional complex abelian variety with integral $\mathcal O_E$ action of rank one on rational homology. Let $B$ have dimension $d=gm$, integral $\mathcal O_E$ action, and the same pure CM type repeated $m$ times. All Hom groups in this paper are geometric.

Give $B,J$ compatible polarizations $\lambda_B,\lambda_J$, of degrees $\delta_B,\delta_J$, meaning that their Rosati involutions restrict to complex conjugation on $E$. Set

$$
\mathscr L=\operatorname{Hom}_{\mathcal O_E}(B,J),\qquad r=2d,
$$
$$
f^\dagger=\lambda_B^{-1}f^\vee\lambda_J,
\qquad Q(f,g)=\operatorname{Tr}_{H_1(B,\mathbb Q)}(f^\dagger g).
$$

The trace is the rational homology trace, not the regular-representation trace of $\operatorname{End}^0(B)$.

**Lemma 3.1.** The group $\mathscr L$ is free of rank $r$, and $Q$ is a positive definite symmetric rational pairing satisfying

$$
\det\operatorname{Gram}_Q(\mathscr L)
=|\operatorname{disc}E|^m\frac{\delta_J^m}{\delta_B}.
\tag{3.1}
$$

**Proof.** Write the homology lattices as a projective $\mathcal O_E$ module $P$ of rank $m$ and a fractional ideal $I$ of $E$. Every $E$-linear map between their rationalizations respects the Hodge structures, because the types agree embedding by embedding. Integral lattice maps are therefore exactly the algebraic homomorphisms, so $\mathscr L=\operatorname{Hom}_{\mathcal O_E}(P,I)$ has rank $2gm$.

Choose coordinates and a purely imaginary $\eta\in E$ so that the Riemann forms are

$$
\psi_J(z,w)=\operatorname{Tr}_{E/\mathbb Q}(\eta z\bar w),
\qquad
\psi_B(x,y)=\operatorname{Tr}_{E/\mathbb Q}(\eta x^tH\bar y),
$$

where $H$ is Hermitian and positive definite at the chosen CM embeddings. Let $n(P)$ and $n(I)$ be absolute rational covolumes relative to a fixed integral basis of $\mathcal O_E^m$ and $\mathcal O_E$. Determinants of the trace pairings give

$$
\delta_J=|\operatorname{disc}E|N(\eta)n(I)^2,
$$
$$
\delta_B=|\operatorname{disc}E|^mN(\eta)^mN(\det H)n(P)^2.
\tag{3.2}
$$

A decomposition of $P$ into fractional ideals shows that the relative covolume of $\operatorname{Hom}_{\mathcal O_E}(P,I)$ is $n(I)^m/n(P)$. The matrix of its trace form is induced by $H^{-1}$, up to transpose or conjugation, which do not alter its determinant. Hence

$$
\det\operatorname{Gram}_Q(\mathscr L)
=|\operatorname{disc}E|^mN(\det H)^{-1}
  \frac{n(I)^{2m}}{n(P)^2}.
$$

Eliminating the covolumes and $N(\eta)$ with (3.2) proves (3.1). Positivity is the Rosati positivity theorem, or follows directly from the positive Hermitian matrices. $\square$

We record a general bound used in the first global example. The form $\delta_BQ$ is integral: multiplication by $\delta_B$ clears the inverse polarization, so its values are traces of integral endomorphisms. Its determinant is

$$
\Delta=|\operatorname{disc}E|^m\delta_J^m\delta_B^{r-1}.
$$

Minkowski's second theorem for Euclidean successive minima $\ell_j$ gives

$$
\prod_{j=1}^r\ell_j\le
\frac{2^r}{\operatorname{vol}(B_r)}\sqrt\Delta
\le2^r(r/2)!\sqrt\Delta.
$$

Every nonzero vector has length at least $1$ in this integral lattice. Squaring the resulting bound on the last minimum gives a rational spanning set with

$$
Q(f,f)\le B_0,
\qquad
B_0=4^r((r/2)!)^2|\operatorname{disc}E|^m
\delta_J^m\delta_B^{r-2}.
\tag{3.3}
$$

This asserts rational spanning, not that the bounded maps form an integral lattice basis. The factorial denotes an ordinary specified integer; no small arithmetic-circuit claim is made.

## 4. The source divisor gives an integral transport norm

Let $S$ be a smooth projective surface, possibly disconnected, and let $H$ be ample. Put $A=\operatorname{Alb}(S)$ and let $q:A\to B$ be a specified surjective morphism. Choose temporary origins on the geometric components to write $s=q\alpha:S\to B$. All intersection numbers below are independent of these origins and, when $S$ is disconnected, are summed over its components.

Liu's construction [5] gives a polarization

$$
\theta_A=\theta_{S,H}:A^\vee\longrightarrow A,
\qquad
\theta=q\theta_Aq^\vee:B^\vee\longrightarrow B.
\tag{4.1}
$$

Its direction is important: initially it polarizes the dual variety. Since $q^\vee$ is finite onto its image, pullback of the ample polarization remains ample, even if $q$ has disconnected kernel.

**Lemma 4.1 (divisor–trace identity).** For any line bundle $L$ on $B$,

$$
\deg\bigl(H\cdot s^*c_1(L)\bigr)
=\frac12\operatorname{Tr}_{H_1(B,\mathbb Q)}(\theta\lambda_L).
\tag{4.2}
$$

**Proof.** Put $z=s_*H\in\operatorname{CH}_1(B)$. The Poincaré construction of $\theta$ is the symmetric dual homomorphism associated to the alternating homology class of $z$. Pairing $c_1(L)$ with $z$ is the contraction of their alternating tensors. The trace of the associated composition counts each unordered pair of indices twice, giving the factor $1/2$. The sign agrees with the polarization convention: for a curve of genus $h$ mapping to its Jacobian, the induced dual polarization is inverse to the canonical principal polarization, $\deg\alpha_C^*\Theta=h$, and the composition has trace $2h$. The projection formula gives $\deg(z\cdot c_1(L))=\deg(H\cdot s^*c_1(L))$. This proves (4.2); equivalently it follows by expanding the two Poincaré first Chern classes in the construction of [5, Proposition 2.5]. $\square$

Assume now that the CM type of $J$ is primitive, so $J$ is simple and $\operatorname{End}^0(J)=E$. Then $\operatorname{End}^0(B)=M_m(E)$, with the prescribed $E$ as center. A positive Rosati involution preserves the center and restricts to complex conjugation there. Thus every polarization of $B$ or $B^\vee$ is compatible with this CM action. This standard centrality fact is essential; Section 7 gives a nonprimitive counter-control where averaging is necessary.

Put $e=\deg\theta$. Since $e$ annihilates its finite kernel,

$$
\eta=[e]\theta^{-1}:B\longrightarrow B^\vee
$$

is an integral positive symmetric map. Let $\mathcal P_B$ be the normalized Poincaré bundle and set

$$
L_B=(\mathrm{id},\eta)^*\mathcal P_B.
$$

The doubling formula [6, Proposition 11.1] gives

$$
\lambda_B=2e\theta^{-1},
\qquad \delta_B=2^{2d}e^{2d-1}.
\tag{4.3}
$$

This supplies an actual line bundle over the field defining the data. It avoids assuming that an arbitrary symmetric polarization map has a chosen representative bundle over that field.

**Theorem 4.2 (geometric CM Hom norm).** The pairing

$$
T(f,g)=\operatorname{Tr}_{H_1(B,\mathbb Q)}
       (\theta f^\vee\lambda_Jg)
\quad(f,g\in\mathscr L)
$$

is positive definite, symmetric and integral, and

$$
\boxed{\det\operatorname{Gram}_T(\mathscr L)
=|\operatorname{disc}E|^m\delta_J^m e,}
\tag{4.4}
$$
$$
\boxed{T(f,f)=2\deg(H\cdot s^*f^*L_J).}
\tag{4.5}
$$

**Proof.** The composition defining $T$ is an integral endomorphism, so its rational homology trace is integral. By (4.3), $T=2eQ$, hence symmetry and positivity follow from Lemma 3.1. Its rank is $2d$, and

$$
\det\operatorname{Gram}_T
=(2e)^{2d}|\operatorname{disc}E|^m\delta_J^m/
 (2^{2d}e^{2d-1})
=|\operatorname{disc}E|^m\delta_J^m e.
$$

Equation (4.5) is Lemma 4.1 applied to $f^*L_J$. $\square$

If the initial $E$ action is rational, it can first be made integral by a fixed finite subgroup. Choose an integral basis $\beta_j$ of $\mathcal O_E$ and an integer $D$ clearing their endomorphism denominators. Define

$$
K=\sum_j\operatorname{im}\bigl((D\beta_j)|_{B[D]}\bigr),
\qquad u:B\longrightarrow B'=B/K.
\tag{4.6}
$$

On a complex lattice $\Lambda$, this replaces $\Lambda$ by $\mathcal O_E\Lambda$: the displayed torsion image is $\beta_j\Lambda/\Lambda$. Hence $B'$ has integral action. Replace $q$ by $uq$ in (4.1). This keeps the retained source and uses actual torsion maps; it does not replace it by an unspecified member of an isogeny class.

## 5. Bounded graphs and bounded image surfaces

Continue with Theorem 4.2, and put

$$
R=4^{2d}(d!)^2|\operatorname{disc}E|^m\delta_J^m.
\tag{5.1}
$$

**Theorem 5.1 (finite graph family).** There is a finite étale scheme of actual $\mathcal O_E$-linear homomorphisms $B\to J$, defined over any characteristic-zero field defining the data, whose geometric maps span $\operatorname{Hom}_E^0(B,J)$. It is the group-graph locus in

$$
\coprod_{1\le c\le C}\operatorname{Hilb}_{cn^d}(B\times J),
\qquad C=[6e(1+R/4)]^d,
\tag{5.2}
$$

where the Hilbert polynomial is computed using $L_B^3\boxtimes L_J^3$.

**Proof.** Minkowski applied directly to the integral pairing $T$, with determinant (4.4), gives $2d$ independent maps satisfying

$$
T(f,f)\le Re,
\qquad Q(f,f)=T(f,f)/(2e)\le R/2.
\tag{5.3}
$$

Let $\lambda_1,\ldots,\lambda_d\ge0$ be the analytic eigenvalues of $f^\dagger f$. Their sum is $Q(f,f)/2$. Riemann–Roch on the graph, which is isomorphic to $B$, gives its Hilbert polynomial $c_fn^d$, where

$$
c_f=3^d\sqrt{\delta_B}\prod_{j=1}^d(1+\lambda_j).
\tag{5.4}
$$

Indeed the graph restricts the product bundle to the cube of $L_B\otimes f^*L_J$, and the Todd class of an abelian variety is $1$. By (4.3) and (5.3),

$$
c_f\le6^de^{d-1/2}(1+R/4)^d\le C.
$$

The graph condition is the open Hom locus in the Hilbert scheme. Fixing the origin, imposing the group law and imposing commutation with an integral basis of $\mathcal O_E$ are algebraic conditions. A homomorphism of abelian varieties has no infinitesimal deformations fixing the origin. Also (5.4) bounds $\prod(1+\lambda_j)$ and hence $\sum\lambda_j$, so only finitely many points of the positive Hom lattice occur. The resulting zero-dimensional finite-type unramified scheme is finite étale in characteristic zero. Its universal graph gives an evaluation morphism $B\times\mathcal H\to J$, and (5.3) proves spanning. $\square$

The larger Hilbert family may contain maps outside (5.3). The following bound uses the smaller spanning subset, not every point of that Hilbert family.

Suppose there are four such quotients $B_i$, targets $J_i$, and maps $s_i:S\to B_i$. Fix a connected component $S_0$ and an algebraic projector selecting a component of the mixed tensor $\bigotimes_iH^1(J_i)$. Assume the given source pairing is nonzero for some complex linear combinations of the pullbacks $f_i^*\omega_i$, with $f_i\in\operatorname{Hom}_E^0(B_i,J_i)$. Write $\Theta=\sum_i\operatorname{pr}_i^*c_1(L_{J_i})$ and $\kappa=H|_{S_0}^2$.

**Corollary 5.2 (surviving image degree).** Some tuple in the bounded graph families gives a map $F:S_0\to\prod_iJ_i$ whose selected surface component is nonzero, and

$$
\deg_{3\Theta}(F_*[S_0])
\le\frac9{4\kappa}\left(\sum_i R_ie_i\right)^2.
\tag{5.5}
$$

**Proof.** Replace each Hom space by the spanning maps (5.3). Multilinear expansion of the nonzero pairing shows that one tuple still has nonzero selected component. By (4.5), its total source intersection in factor $i$ is at most $R_ie_i/2$. Every component contributes nonnegatively because the target bundle is ample and its pullback is nef. Thus

$$
H|_{S_0}\cdot F^*\Theta\le\frac12\sum_iR_ie_i.
$$

Hodge index yields $(F^*\Theta)^2\le(H\cdot F^*\Theta)^2/\kappa$. The projection formula gives $\deg_{3\Theta}(F_*[S_0])=9(F^*\Theta)^2$, proving (5.5). The image has dimension two, since otherwise the selected surface class would vanish. If $F$ has generic degree $a$, its effective image cycle is $a[F(S_0)]$; the integral surface image has no larger degree and still has nonzero selected rational component. $\square$

## 6. An algebraic test for the successful parameters

Let $T=\prod_{i=1}^4J_i$, with all $\dim J_i=g$, and write $n=4g$. Let $\mathcal H$ be the product of the four finite graph schemes and $Z_h=F_{h*}[S_0]$. The construction works after a finite extension defining $S_0$ and its chosen origins.

First apply the rational algebraic Künneth projector onto $\bigotimes_iH^{2g-1}(J_i)$, then a specified algebraic projector $e$ onto the desired orbit. Denote the resulting rational cycle by $Z_h^{\rm sel}$. For example, the degree projectors can be represented by the correspondence polynomial

$$
\pi_k=\prod_{0\le j\le2g,\ j\ne k}
\frac{[2]^*-2^j}{2^k-2^j}.
\tag{6.1}
$$

Only its cohomological projector property is needed; we need not assert that this interpolation is an idempotent on every Chow group.

Let $\ell=c_1(\mathcal P_T)$ on $T\times T^\vee$ and let $\lambda:T\to T^\vee$ be the product polarization. Define

$$
C_h=\lambda^*p_{2*}\left(p_1^*Z_h^{\rm sel}\frac{\ell^4}{4!}\right)
\in\operatorname{CH}^2(T)_{\mathbb Q}.
\tag{6.2}
$$

This is the relevant component of the classical Fourier correspondence $\exp(\ell)$ [6]. Its cohomological action is an isomorphism $H^{2n-4}(T)\to H^4(T^\vee)$: the Poincaré class lies in $H^1\otimes H^1$, and Fourier squared is $(-1)^n[-1]^*$. Pullback by $\lambda$ is also a rational cohomology isomorphism. Therefore $[C_h]\ne0$ exactly when the selected component of $Z_h$ is nonzero. It lies in $\bigotimes_iH^1(J_i)$, up to the simultaneous label inversion induced by duality.

Every class in that mixed degree-four tensor is primitive for $\Theta$. In a term of $\Theta^{n-3}$, the four exponents sum to $4g-3$, so some exponent is at least $g$. Its factor annihilates $H^1(J_i)$ by degree. Since $C_h$ is rational algebraic, its class is real and of type $(2,2)$. Hodge–Riemann now gives

$$
N(h)=\deg(C_h^2\Theta^{n-4})\ge0,
\qquad N(h)>0\Longleftrightarrow[C_h]\ne0.
\tag{6.3}
$$

The sign is positive: $(-1)^{4\cdot3/2}=1$ and $i^{2-2}=1$. No conjectural inverse Lefschetz correspondence is used; (6.2) is algebraic.

Intersection degrees are invariant on Galois orbits of the finite parameter scheme. Consequently the successful parameters form a specified open-and-closed finite étale subscheme $\mathcal H_{\rm good}$. Corollary 5.2 proves it is nonempty under its nonzero-pairing hypothesis.

Given algebraic presentations of the varieties, actions, source maps and bundles, (5.2) is a finite graph problem; factoring its coordinate algebra and computing (6.3) selects successful factors. This statement concerns a bounded, checkable algebraic procedure. It does not assert manageable complexity or turn an unexpanded moduli description into evaluated equations.

Keep parameter labels. The family contains both $f$ and $-f$; negating one factor reverses the mixed class and preserves its norm. An unweighted trace of all successful classes can vanish. Choosing a geometric point after computing the finite algebra is sufficient for the complex Hodge-conjecture application; a nonzero cycle over the original arithmetic base is a separate descent question.

## 7. Exact global controls

### 7.1. Actual graphs between two CM elliptic classes

Work over $K=\mathbb Q(\sqrt5,i)$. Put

$$
j_\pm=632000\pm282880\sqrt5,\qquad k=\frac{j_+}{j_+-1728},
\qquad A=-3k,\quad B=-2k,
$$

and let $C_+:y^2=x^3+Ax+B$. Define

$$
r_2=\frac{10-96\sqrt5}{209},\qquad
r_3=-\frac{65+3\sqrt5}{76}+\frac{255-149\sqrt5}{836}i.
$$

They satisfy respectively the $2$- and $3$-division equations, with $r_3^3+Ar_3+B\ne0$. The classical normalized Vélu maps [9] are

$$
X_2=x+\frac{3r_2^2+A}{x-r_2},
$$
$$
X_3=x+\frac{2(3r_3^2+A)}{x-r_3}
       +\frac{4(r_3^3+Ar_3+B)}{(x-r_3)^2},
\qquad Y_a=y\frac{dX_a}{dx}.
$$

Their targets have coefficients

$$
A_2=-4A-15r_2^2,\quad B_2=-13B-35r_2^3-21Ar_2,
$$
$$
A_3=-9A-30r_3^2,\quad B_3=-27B-70r_3^3-42Ar_3.
$$

Both targets have $j=j_-$. With $u=(1+i\sqrt5)/3$, exact identities $u^4A_3=A_2$ and $u^6B_3=B_2$ identify the second target with the first by $(X,Y)\mapsto(u^2X,u^3Y)$. Denote the resulting maps to $J:Y^2=X^3+A_2X+B_2$ by $\phi_2,\phi_3$.

The dual composition $\widehat\phi_2\phi_3$ has differential $2/u=1-i\sqrt5$. Faithfulness of the differential representation in characteristic zero shows that its difference from $1$ squares to $-5$. This constructs the integral action of the maximal order $\mathbb Z[\sqrt{-5}]$; the corresponding action on $J$ is obtained from $\phi_3\widehat\phi_2$. Both maps intertwine them. Their degrees $2,3$ exclude rational proportionality. For the principal polarizations their Rosati Gram matrix is

$$
\begin{pmatrix}4&2\\2&6\end{pmatrix},\qquad\det=20.
$$

Lemma 3.1 gives determinant $20$ for the full Hom lattice, so these maps form an integral basis. The general bound (3.3) gives $B_0=320$. Formula (5.4), with the principal bundles, gives the valid graph coefficient bound $C_0=963$. The **entire** corresponding graph scheme is the $447$ copies of $\operatorname{Spec}K$ indexed by

$$
2a^2+2ab+3b^2\le320,
$$

with evaluation $a\phi_2+b\phi_3$ and graph polynomial $3(1+2a^2+2ab+3b^2)n$. The inequality $2a^2+2ab+3b^2\ge a^2+b^2$ certifies the finite enumeration range. The smaller subset $Q\le320$ has $217$ maps, since $Q(f,f)=2\deg f$ here. These are two different, consistent bounds.

### 7.2. Surface selection and cancellation

Take $S=C_+^2$, with the first two quotient maps using the first coordinate and the last two the second. Use conjugate CM actions on factors $2,4$, on both quotients and targets, so the common CM-label tensor has type $(2,2)$.

For a tuple $f_j$, write $d_j=\deg f_j$. The full mixed surface component has self-intersection $4\prod d_j$. The common quadratic CM orbit has half of this norm:

$$
N_{\rm CM}(f_1,f_2,f_3,f_4)=2\prod_{j=1}^4d_j.
\tag{7.1}
$$

One direct explanation is that the mixed class of the first pair has square $-2d_1d_2$, and likewise for the second pair. Each pair has two conjugate CM tensor components. Among the four resulting tensor terms, the common CM-label projector keeps two, with equal norm contribution; the discarded pair is orthogonal. Equivalently (7.1) follows by exterior algebra on the eight-dimensional rational $H^1$.

For $f=(\phi_2,\phi_3,\phi_2,\phi_3)$ the full mixed square is $144$ and the selected square is $72$. Acting by $\sqrt{-5}$ on the first factor gives a second selected class; the Gram matrix of this CM orbit basis is $\operatorname{diag}(72,360)$, with determinant $25920$. Thus the test produces an actual nonzero rational class and its full quadratic CM span.

The $447$-point Hom family has one zero map. Hence its successful surface family has exactly $446^4=39{,}567{,}575{,}056$ points, specified as a product rather than enumerated. The sum of the single-factor degrees is $71112$, so the sum of their positive selected norms is $2\cdot71112^4=51{,}144{,}809{,}865{,}961{,}807{,}872$. Yet the unweighted sum of selected classes is zero, by sign reversal. This verifies the need for labels in Section 6.

For the product principal divisor $H$ on $S$, $H^2=2$ and the displayed map has $F^*\Theta=5H$. Therefore its image-cycle degree in $3\Theta$ is $450$. The norm-bounded $217$-map subfamily, using the elementary source intersection estimate with principal bundles, gives the valid bound $1{,}843{,}200$. No minimality is asserted for these deliberately loose bounds.

### 7.3. Nonscalar polarization and noncentral CM control

Let $S=E_i^2$, with CM by $\mathbb Z[i]$, and choose the ample Hermitian form and isogeny

$$
H=\begin{pmatrix}2&1+i\\1-i&3\end{pmatrix},\quad H^2=8,
\qquad q=\begin{pmatrix}1+i&1\\0&2-i\end{pmatrix},\quad\deg q=10.
$$

The polarization $\theta=q\theta_{S,H}q^\vee$ has degree $e=1600$. For the four integral row maps $E_i^2\to E_i$, the geometric Hom Gram matrix is

$$
\begin{pmatrix}
16&0&12&-4\\0&16&4&12\\12&4&20&0\\-4&12&0&20
\end{pmatrix},\qquad\det=25600=4^2\cdot1600.
$$

Direct exterior products give twice the source intersections on its diagonal, verifying both (4.4) and (4.5). The canonical bundle (4.3) has polarization degree $65{,}536{,}000{,}000$ and total source intersection $6400=2de$.

For a noncentral comparison, let $\mathbb Q(\zeta_8)$ act on this same elliptic square through

$$
\zeta_8\longmapsto\begin{pmatrix}0&i\\1&0\end{pmatrix}.
$$

Its type $\{1,5\}$ is induced from $\mathbb Q(i)$, and the original $\theta$ is not invariant. For any finite automorphism group $G$ of order $\ell$, average on the dual before inversion:

$$
\theta_G=\sum_{g\in G}g\theta g^\vee,\qquad N=\deg\theta_G,
\qquad L_G=(\mathrm{id},N\theta_G^{-1})^*\mathcal P_B.
$$

Trace invariance and Lemma 4.1 give

$$
\deg(H\cdot s^*L_G)=\frac{2dN}{\ell},
\qquad \deg\lambda_{L_G}=2^{2d}N^{2d-1}.
$$

For the displayed $8$-term average, $N=21{,}827{,}584$ and the source intersection is $10{,}913{,}792=N/2$. The polarization degree is $166{,}393{,}741{,}485{,}239{,}921{,}803{,}264$. This is a nontrivial test of averaging; one cannot omit it merely because a CM field acts.

## 8. The degree-$110$ application and its unevaluated inputs

Take $E=\mathbb Q(\zeta_{110})$, $g=20$, $|\operatorname{disc}E|=5^{30}11^{36}$. The normalized cyclic curves are

$$
y^{110}=x^a(1-x)^b,
\qquad (a,b)=(1,71),(24,31),(38,19),(57,29).
$$

Their primitive deck factors $J_i$ have dimension $20$. The unit-character Hodge types have trivial stabilizer in $\operatorname{Gal}(E/\mathbb Q)$, hence are primitive. The unique point over $x=1$ is rational and deck-fixed because each listed $b$ is coprime to $110$. It specifies a Jacobian theta bundle whose restriction to $J_i$ gives a compatible polarization.

The primitive projector has denominator $110$ and is self-adjoint for that polarization. Its image and complementary image meet in a subgroup of $J_i[110]$, so the induced polarization degree satisfies

$$
\delta_{J_i}\le110^{40}.
$$

On the mixed tensor the relevant rational projector is

$$
e_{\rm CM}=\frac1{110^3}\sum_{a,b,c\bmod110}
\tau_1^{-a-b-c}\tau_2^a\tau_3^{-b}\tau_4^{-c}.
$$

It selects labels $(k,k,-k,-k)$, not all-equal labels. Exact least-residue counts for the four triples $(1,71,38),(24,31,55),(38,19,53),(57,29,24)$ show that this $40$-dimensional rational orbit has type $(2,2)$. The all-equal orbit has Hodge indices $0,2,4$ and is a different space.

The source construction under investigation uses the compact ball form $\operatorname{diag}(1,1,199-100t)$ over $E/E^+$, with $t=\zeta_{110}+\zeta_{110}^{-1}$. Its specified Hecke quotients and nonzero mixed-period argument provide the intended input to the present transport method, using the geometry of [1]. Those source arguments are not reproved in this paper. We therefore make only the following concrete specialization of the transport theorem: once the actual quotient dimensions $d_i=20m_i$, canonical dual-polarization degrees $e_i$, and source presentations are supplied, one may use

$$
R_i=4^{40m_i}((20m_i)!)^2(5^{30}11^{36})^{m_i}110^{40m_i}
$$

in (5.2), (5.5), and the algebraic test (6.3), where the latter is $\deg(C_h^2\Theta^{76})$.

The integers $m_i,e_i$ and the graph coordinate algebras have **not** been evaluated for this source. A moduli description and finite correspondence operations are not expanded projective equations. The supplement checks the signed orbit and target arithmetic needed for this specialization; it does not output the degree-$110$ source maps or a new Fermat Hodge class.

## 9. Reproducibility and limits

The supplement contains four standalone exact Python/SymPy verifiers and their retained JSON outputs. They use CPU arithmetic and require no network or credentials. Run `python verify_all.py` from its root.

- `certify_CM_Hom_discriminant.py` constructs homology, Riemann and integral Hom matrices in five cases: nonprincipal quadratic ideals, off-diagonal Hermitian forms, quartic CM, and unequal lattices. It also checks the torsion saturation operation.
- `construct_CM20_Hom_graphs.py` verifies the generic rational graph identities modulo the division relations, specializes the number-field maps, checks the common target and CM relation, and enumerates all $447$ graph parameters.
- `certify_CM_graph_intersection_selection.py` constructs pushforward surface classes by Poincaré duality, applies the mixed and CM projectors, and computes their exact intersections and CM-orbit Gram matrix. It also checks every primitive signed degree-$110$ label. The matrices are a CM lattice control; no numerical Betti comparison for degree $110$ is implied.
- `certify_Albanese_polarization_trace.py` computes actual divisor intersections on a CM elliptic square, checks the geometric Hom determinant, and compares central and noncentral CM actions.

The scripts verify the stated finite calculations. They do not replace the written proofs of Hom representability, the geometric trace identity, Minkowski spanning, or Hodge–Riemann positivity. The completed examples verify actual maps and cycles, but their Hodge cases are classical. The degree-$110$ construction remains an application with unevaluated source data. Further work should evaluate a retained source graph algebra or move to a setting where that computation is feasible; producing more formal bounds alone would not complete it.

## References

[1] OpenAI. *The rational Hodge conjecture for CM abelian varieties*. OpenAI Math Release preprint, 6 October 2026. Pinned repository commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, especially Sections 3–6. https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a

[2] D. W. Masser and G. Wüstholz. *Factorization estimates for abelian varieties*. Publications Mathématiques de l'IHÉS 81 (1995), 5–24. https://www.numdam.org/item/PMIHES_1995__81__5_0/

[3] D. Masser and G. Wüstholz. *Polarization estimates for abelian varieties*. Algebra & Number Theory 8 (2014), 1045–1070. https://doi.org/10.2140/ant.2014.8.1045

[4] S. Marseglia. *Computing abelian varieties over finite fields isogenous to a power*. arXiv:1808.03673v2 (2020), especially §§2–3 and 5. https://arxiv.org/abs/1808.03673v2

[5] Y. Liu. *Fourier–Jacobi cycles and arithmetic relative trace formula (with an appendix by Chao Li and Yihang Zhu)*. Cambridge Journal of Mathematics 9 (2021), 1–147; arXiv:2102.11518v2. https://doi.org/10.4310/CJM.2021.v9.n1.a1 ; https://arxiv.org/abs/2102.11518v2

[6] G. van der Geer and B. Moonen. *Abelian varieties*, preliminary textbook chapters 11–13. https://www.math.ru.nl/~bmoonen/BookAV.html ; chapter files: https://www.math.ru.nl/~bmoonen/BookAV/PolWp.pdf , https://www.math.ru.nl/~bmoonen/BookAV/Endoms.pdf , https://www.math.ru.nl/~bmoonen/BookAV/FourChow.pdf

[7] A. Grothendieck. *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert*. Séminaire Bourbaki 6 (1960–1961), exposé 221, 249–276. https://www.numdam.org/item/SB_1960-1961__6__249_0/

[8] E. Costa, N. Mascot, J. Sijsling and J. Voight. *Rigorous computation of the endomorphism ring of a Jacobian*. Mathematics of Computation 88 (2019), 1303–1339; arXiv:1705.09248v5. https://doi.org/10.1090/mcom/3373 ; https://arxiv.org/abs/1705.09248

[9] J. Vélu. *Isogénies entre courbes elliptiques*. Comptes Rendus de l'Académie des Sciences de Paris, Série A 273 (1971), 238–241. Bibliographic search: https://zbmath.org/?q=V%C3%A9lu+Isog%C3%A9nies+1971

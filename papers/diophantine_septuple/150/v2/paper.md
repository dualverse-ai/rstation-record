# The least extension degree of the generic rational Diophantine sextuple

Let $a_1,\ldots,a_n$ be independent transcendentals over $\mathbb Q$. Define
$$
 F_n=\mathbb Q(a_1,\ldots,a_n),\qquad
 K_n=F_n(s_{ij}\mid i<j),\qquad s_{ij}^2=1+a_i a_j .
$$
A *new neighbour* over a field $L\supset K_n$ is $t\in L$ distinct from zero and the $a_i$, with all $1+a_it$ squares in $L$. The independent edge divisors show that the sign group of $K_n/F_n$ has rank $\binom n2$, also after extending the constants to $\overline{\mathbb Q}$.

**Theorem 1.** The least finite extension degree $[L:K_6]$ for which a new neighbour exists is four. A biquadratic extension attains it. For $n\ge6$, an odd-degree extension of $K_n$ containing a new neighbour has degree at least $2^{n-4}+1$.

**Theorem 2.** Suppose $t\in K_6$ is a new neighbour after adjoining its six individual roots, and this adjunction has degree four. Up to permuting the entries, the squareclasses of the six radicands have one of two forms, in additive notation for $K_6^\times/K_6^{\times2}$,
$$
 (0,0,0,0,A,B),\qquad (A,A,A,A,A,B),
$$
where $A,B$ are independent. In the first case $t$ is a function of the rooted four entries with zero classes. In the second it is a function of the rooted five with the common class. Both cases occur.

The universal field models rational formulas in the inputs and their individual edge roots. A rational specialization can have additional arithmetic relations. The distinction matters in the seventh-entry problem, where each of 21 products must have its own rational root. Dujella's regular fifth [1] gives the upper bound after two additional roots are adjoined. The common-class alternative is realized by the regular-sixth construction of Gibbs [2]. On a fixed-anchor edge surface, [3, Theorem 6] treats a coordinate in the surface field whose joining roots generate at most one additional squareclass. The dominant self-maps of the septuple root cover are classified in [4]. Here the six entries vary independently, the seventh coordinate can be algebraic over their full-root field, and the minimum extension degree is attained. The proof also produces the exact universal Mordell–Weil group of an associated genus-two Jacobian. A numerical specialization in Section 6 illustrates how a class can appear below the generic threshold.

The proof of Theorem 1 uses the field of definition of the seventh coordinate. Section 1 computes the Jacobian group needed in Section 2 to descend a genuinely quadratic coordinate and test its six roots. Section 3 treats a coordinate already in the base field whose roots could require a quadratic extension. Section 4 treats odd-degree coordinates by following the edge-sign action on their conjugates. Section 5 constructs the matching biquadratic extension and proves Theorem 2.

## 1. Jacobians on the affine orbit of six labelled points

Use two labelled entries to write $a_i=(u+b_i)/v$, with $b_5=0,b_6=1$. Then $v=1/(a_6-a_5)$, $u=va_5$, and $F_6=k(u,v)$ for $k=\mathbb Q(b_1,\ldots,b_4)$. The curve
$$
 C:\ y^2=\prod_{i=1}^6(1+a_i e)
$$
is isomorphic over $F_6$ to $C_0:Y^2=\prod_{i=1}^6(X+b_i)$ by $X=u+v/e,\ Y=y(v/e)^3$. The Jacobian $J_0$ has geometric endomorphism ring $\mathbb Z$. Indeed start with six independent roots over the field of symmetric coefficients. The Galois group is $S_6$, so Zarhin's theorem applies [5]. The affine normalization of two roots gives the same geometric curve after extending the algebraically closed field.

**Proposition 3.** $J_0(K_6)=J_0(k)$.

Set $s=u^2+v^2$. Over $k(u,s)$, the field $K_6$ adjoins the square roots of
$$
 Q=s-u^2,\qquad L_{ij}=s+(b_i+b_j)u+b_i b_j\quad(i<j).
$$
Their zero divisors are distinct primes, giving all sixteen independent characters and geometric integrality. In the projective $(u,s)$-plane, the $L_{ij}$ are the fifteen chords of the points $(-b_i,b_i^2)$ on the conic $Q=0$. A quadratic character corresponds to a subset $G$ of $m$ chords and a choice $c\in\{0,1\}$ of whether to include the conic. Its double plane has the line at infinity in its branch locus exactly when $m$ is odd. Write $2d=2\lceil m/2\rceil+2c$ for the branch degree.

For a resolution of the double plane its irregularity $q=h^1(\mathcal O)$ is
$$
 q=h^1(\mathbb P^2,\mathcal I_{\boldsymbol r}(l)),\qquad
 l=d-3,\quad r_i=\max\big(0,\lfloor(\deg_G(i)+c)/2\rfloor-1\big).
$$
Here $\mathcal I_{\boldsymbol r}$ imposes order $r_i$ at the six conic points. To verify the formula, blow up the singularities of the branch. At an ordinary point of multiplicity $h$ the new square-root line bundle is the pullback of the original bundle less $\lfloor h/2\rfloor$ times the exceptional divisor. Adding the canonical divisor gives the jet condition $\lfloor h/2\rfloor-1$. Distinct chords at a conic point and the conic itself have distinct tangents. Three disjoint chords are generically nonconcurrent, by varying the sixth endpoint after fixing five. The chord directions are distinct. The line at infinity is tangent to the conic away from all chords. Ordinary nodes and the tangency have multiplicity two at each required blowup and impose no adjoint jets. The direct image of the resolved double cover splits into the structure sheaf and the inverse square-root bundle [6]. Serre duality and pushdown on the blown-up plane give the formula.

For $l<0$, $q=\sum_i r_i(r_i+1)/2$. For $l\ge0$ take the residual along the conic. All $r_i\le2$, so the residual is a set of $t=\#\{i:r_i=2\}$ simple conic points in degree $l-2$. The restriction of plane forms of nonnegative degree to a conic is surjective. The residual exact sequence gives
$$
 q\le \max\big(0,\sum r_i-2l-1\big)+\max\big(0,t-\max(0,2l-3)\big).
$$
The supplement enumerates all $2^{15}$ labelled chord sets and both choices of $c$. These are all cases in which these bounds are positive.

| $c$ | $m$ | $l$ | Valences | Number | $q$ |
|---|---|---|---|---|---|
|0|4|−1|4,1,1,1,1,0|30|1|
|1|5|1|5,1,1,1,1,1|6|0|
|1|6|1|5,2,2,1,1,1|60|0|
|1|6|1|3,3,3,3,0,0|15|1|

In the middle rows, linear forms supply the entire first jet at a single point. In the last row four points on a smooth conic impose three independent conditions on linear forms. The first row has one jet of length one in negative degree.

Let $S$ be a smooth projective model of the full surface, after extending the constants to $\bar k$. Its Albanese is, up to isogeny, the product of the Albaneses of the nontrivial character quotients. The sign group admits rational character projectors. For each character kernel, norm and pullback identify the invariant factor with the Albanese of a smooth model of its quotient. Equivalently, finite quotient singularities have rational singularities in characteristic zero, so invariant first cohomology agrees with that of the resolved quotient. The trivial projector contributes zero since the quotient is a plane. It follows from the table that $\operatorname{Alb}(S)$ is isogenous to a product of 45 elliptic curves. It has no nonzero homomorphism to the geometrically simple abelian surface $J_0$. Every rational map from $S$ to $J_0$ is therefore constant. The shape field $k$ is algebraically closed in $K_6$, giving the stated equality.

**Corollary 4.** With $W$ any labelled branch point of $C$ and $O=(0,1)$, its Jacobian satisfies $J(K_6)=J[2]\oplus\mathbb Z[O-W]$. Its rational two-torsion has order 16.

By Proposition 3 the group is the same as over $F_6$. On the original coordinate line normalize three branch points to $0,1,\infty$, sending $W$ to infinity. The remaining three branch images are independent over $\mathbb Q$ and generate a field $k_0$. Let $f$ be the monic quintic with the five finite branch roots, and let $P$ be the normalized image of the original coordinate zero. The inverse projectivity has the form $h(X-P)/(X-Q_0)$, with $h,Q_0$ freely varying. The point $O$ fixes the squareclass of the twist as $f(P)V^2=f(X)$. Purely transcendental extensions preserve points of a fixed abelian variety. Over the function field of $C_*:w^2=f(P)$, the twist splits. Its sections over $k_0(P)$ correspond to maps from $C_*$ to its Jacobian that are odd under hyperelliptic involution. Relative to the branch at infinity these maps are integral multiples of the Abel map plus constants, by the geometric endomorphism ring $\mathbb Z$. Oddness imposes two-torsion on the constants, all rational. The Abel map yields $[O-W]$.

## 2. A genuinely quadratic coordinate

Let $[L:K_6]=2$ and suppose $e\in L\setminus K_6$ has the six individual roots. It gives a point $P$ on $C_0$ at $X=u+v/e$. Its conjugate $P^\sigma$ has a different abscissa. The effective divisor $P+P^\sigma$ is unique in its degree-two linear system. On a genus-two curve every moving degree-two system is the hyperelliptic pencil. The divisor class, relative to twice a labelled branch point, descends to $k$ by Proposition 3. A rational branch point ensures this class has a line bundle defined over $k$. The space of its sections commutes with extension of the field. As its dimension is one, the unique effective divisor descends to $k$.

The two abscissas thus generate a quadratic constant field $k'/k$ and $L=K_6k'$. On the vertical line $u=X$ of $k'(u,s)$, the radicands $Q,L_{ij}$ are all units at the generic point. Every place above this line is unramified. For each $i$ with $X+b_i\ne0$, the radicand
$$
 1+a_i e=(X+b_i)/(X-u)
$$
has valuation $-1$ there. This contradicts its square root in $L$. Hence every quadratic-field candidate has coordinate in $K_6$.

## 3. A coordinate in the base field

Fix an entry $x=a_j$. The other five entries and their pair roots generate a field $B$. Then $K_6=B(D)$, where the smooth projective curve $D$ has equations
$$
 w_i^2=1+a_i x\quad(i\ne j).
$$
Its degree-32 map to the line has sign group $G=(\mathbb Z/2)^5$. The six branch inertias are the five unit vectors and their sum at infinity. Riemann–Hurwitz gives $g(D)=17$.

Over $\bar B$ its Jacobian has 15 elliptic character factors associated with four-element subsets of these six branch points, and one genus-two factor associated with all six. Indeed the character subcovers of the line are the double covers branched at the corresponding even subsets, and the trivial factor vanishes. Each positive-genus factor is geometrically simple. The elliptic factors are pairwise geometrically nonisogenous. A finite branch point in the symmetric difference of two four-sets can be varied with the remaining parameters fixed. One elliptic curve then has varying $j$-invariant, and the other is constant. Every variety isogenous to a fixed elliptic curve over an algebraically closed extension in characteristic zero is a quotient by a group of its constant torsion points. Thus the two cannot be geometrically isogenous. For the genus-two factor use [5]. In particular deck transformations, acting as scalar signs on the factors, are central in the rational endomorphism algebra.

Suppose $e\in K_6$ and its roots lie in an extension of degree at most two. If $e=-1/a_i$, the other five radicands have independent valuations at the divisors $a_k=a_i$, unramified for the original roots. Otherwise all radicands are nonzero. If $e$ is nonconstant on $D$, choose its five roots for $i\ne j$. The quadratic conjugation of those five roots determines a subgroup $H\le G$ of order at most two. Their invariant functions give a nonconstant map $D\to D/H$ with coordinate $e$. The invariant function field embeds because $e$ is transcendental over $\bar B$ in this case.

We will also use the following argument for subgroups $H$ of order four. Whenever $Y=D/H$ has genus at least two, any nonconstant map $D\to Y$ factors through $D\to Y$ followed by an automorphism. The Jacobian of $Y$ consists precisely of the $H$-invariant character factors. Every homomorphism $\operatorname{Jac}(D)\to\operatorname{Jac}(Y)$ hence kills $h_*-1$ for $h\in H$. Precomposition by $h$ changes the curve map in the Abel embedding only by a translation. The translation would stabilize the entire embedded curve. Such a translation induces identity on all point differences and hence on the Jacobian. The action of curve automorphisms of a genus-at-least-two curve on its Jacobian is faithful in characteristic zero, giving trivial stabilizer. The descended self-map is an automorphism by Riemann–Hurwitz. Every automorphism of $Y$ centralizes $G/H$, since its action on $\operatorname{Jac}(Y)$ commutes with the scalar signs on each distinct factor. It therefore induces a projectivity on the branch line.

For $|H|\le2$, the quotient retains five or six generic branch points and has genus at least five. The projective stabilizer of either generic branch set is trivial. One exact specialization test for the sextet and each of its five-point subsets uses $\{\infty,1,2,5,12,38\}$. Enumerating permutations and testing cross-ratios gives exactly the identity for all seven sets. The condition for a given permutation to be projective is closed among distinct branch points. It follows that a nonconstant $e$ in this $j$ direction must equal $a_j$.

A new coordinate $e$ must consequently be constant in all six directions. Each of the six partial derivations on $F_6$ extends uniquely to the finite separable field $K_6$. They annihilate $e$, which must then be algebraic over $\mathbb Q$, hence rational by geometric integrality. For nonzero constant $e$, the six divisors $1+a_i e=0$ are unramified at their generic points in $K_6$ and detect six independent squareclasses. This excludes the proposed quadratic root extension.

## 4. Low odd degree and the signs of a correspondence

Write $n\ge6$. Suppose an odd-degree extension contains a new neighbour $t$, and put $d=[K_n(t):K_n]$. Each root $\rho_i^2=1+a_i t$ belongs to $K_n(t)$, since adjoining it would otherwise introduce a factor of two. A vanishing radicand makes $t=-1/a_i$, in which case the other $n-1$ radicals are independent at their respective diagonal valuations. We may therefore use nonzero signs throughout.

Fix $j$, put $x=a_j$, and take the curve $D$ of the other $r=n-1$ roots over their rooted field $B$. It maps to the $x$-line with group $G=(\mathbb Z/2)^r$. Its geometric gonality is $2^{r-2}$. Indeed each finite inertia fixes $2^{r-1}$ points. If a function $h:D\to\mathbb P^1$ has degree less than $2^{r-2}$, its agreement with its precomposition by an inertia element exceeds $2\deg h$ points. Two different maps can agree only along an effective divisor of degree $2\deg h$, by pulling back the diagonal in $\mathbb P^1\times\mathbb P^1$. Hence $h$ is invariant under all finite inertia and descends through the degree-$2^r$ map. Conversely, forgetting all but three roots gives a degree-$2^{r-3}$ map to a genus-one curve with geometric gonality two.

The positive-genus character factors of $\operatorname{Jac}(D)$ are pairwise geometrically nonisogenous and simple. Their branch sets are the even subsets of the $n$ points including infinity, of size at least four. Genus-one factors were treated in Section 3. For larger sets, the independent finite roots give geometric simplicity by [5]. To distinguish equal-genus factors with different branch sets, vary a finite branch in the symmetric difference. The curve depending on that branch changes moduli, since a projectivity identifying two such configurations can choose the images of three fixed branch points in only finitely many ways. If its Jacobian were isogenous to the other, then after algebraic closure of the fixed parameters it would be a quotient of a constant abelian variety by a subgroup of its constant finite torsion. It would therefore be constant. Hom groups are invariant under algebraically closed field extension, so its principal polarization would be constant as well. Torelli contradicts the variation of the branch configuration. As in Section 3 the deck action is central in the rational endomorphism algebra.

Assume $2d<2^{r-2}$. The $d$ embeddings of $K_n(t)/K_n$ give a divisor $Z_P$ of degree $d$ on a second copy of $D$, by using the $t$-coordinate and the signed roots $\rho_i$, $i\ne j$. This defines a rational map $D\to\operatorname{Sym}^d D$. It has no fixed point in its divisors, geometrically. Otherwise one conjugate of $t$ would be algebraic over $B$, and so would $t$. Over $B(t)(x)$ the field $K_n(t)$ then adjoins just the $r$ original linear radicals. At $x=-1/t$ all are units, since $t$ is new. The root of $1+xt$ is impossible by its odd valuation there.

For $g\in G$, the difference of the Abel classes of $Z_{gP}$ and $gZ_P$ is constant as $P$ varies. Indeed the map to the Picard variety induces a homomorphism on Jacobians, and $g$ commutes with it. The choice of origins contributes only a constant. For generic $P,Q$ we get
$$
 Z_{gP}+gZ_Q\ \sim\ Z_{gQ}+gZ_P.
$$
Each side has degree $2d$, below the gonality. Two distinct effective divisors of equal degree in a single linear system would supply a nonconstant function of at most that degree. Thus these divisors coincide. The formal divisor $Z_{gP}-gZ_P$ is independent of $P$. Either its positive or its negative part, if nonzero, supplies a fixed point in one of the two families. We conclude $Z_{gP}=gZ_P$ as effective signed point multisets.

The $d$ abscissas are distinct by separability and by the choice of the entry field $K_n(t)$. Their monic polynomial is invariant under every sign flip incident to $j$, since $g$ fixes the abscissa on the target. Varying $j$ gives invariance under every edge flip. The polynomial therefore belongs to $F_n[T]$. Its irreducibility over $K_n$ implies irreducibility over $F_n$. Write $M=F_n(t)$. The compositum $K_nM$ has degree $d$ over $K_n$, so the fields are linearly disjoint. Every edge flip has a lift fixing $t$. The uniqueness of each signed point above its abscissa implies that the lift flipping $s_{jk}$ negates $\rho_k$ and fixes $\rho_i$ for $i\ne j,k$. Varying $k$ in place of $j$ shows it also negates $\rho_j$. We chose the $\rho_i$ once for all directions. It follows that
$$
 g_i=\prod_{k\ne i}(1+a_i a_k),\qquad
 (1+a_i t)/g_i\in M^{\times2}.
$$
Indeed $\rho_i/\prod_{k\ne i}s_{ik}$ is invariant under the whole sign group.

Consider the prime divisor $1+a_1a_2=0$ on the rational base. At its generic point $a_1a_2=-1$, $a_1\ne a_2$, and every entry is a unit. Exactly $g_1,g_2$ have positive valuation, both of order one. If a place above this prime in $M$ had odd ramification index, the displayed squares would give odd valuation for $1+a_1t,1+a_2t$ and even valuation for the other $1+a_it$. A pole of $t$ gives the same valuation on all of them. If $t$ is integral, its residue would satisfy $1+a_1t=1+a_2t=0$, requiring $a_1=a_2$. Thus every ramification index above this prime is even. The degree formula for the finite normalization of this divisorial discrete valuation ring forces $[M:F_n]$ to be even. This contradicts the odd degree $d$.

Consequently every odd-degree new neighbour has $d\ge 2^{n-4}+1$. With $n=6$ this excludes cubic extensions. An independent check on this cubic step comes from $H(T)=\operatorname{Norm}_{M/F_6}(1+Tt)$. It has degree at most three, $H(0)=1$, and $H(a_i)/g_i$ is square. Near the real ordered inputs $(-4,-2,-1,1/3,2/3,2)$, the signs required of $H$ alternate at those six inputs and zero in increasing order. One can avoid all poles and zeroes of their nonzero rational coefficients and values in that open region. The intermediate value theorem would give six roots of a cubic.

## 5. Sharpness and the two sign patterns

Choose four entries $a,b,c,d$. Write $p=abcd,\ S=a+b+c+d,\ U=abc+abd+acd+bcd$, and $R$ for the product of the six edge roots on the four. The regular fifth [1] is
$$
 e=\frac{(1+p)S+2U+2R}{(p-1)^2}.
$$
At each vertex $a_i$ of the four, a root is $(a_iR_{\mathrm{opp}}+R_{\mathrm{inc}})/(p-1)$, with $R_{\mathrm{opp}}$ the product of the three edges among the other vertices and $R_{\mathrm{inc}}$ the product of the three incident roots. These identities follow by squaring. At $(1,3,8,120)$ with positive signs this formula gives $777480/2879^2$, proving generic distinctness from zero and the initial four. It is independent of $a_5,a_6$. At each of $1+a_5e=0$ and $1+a_6e=0$, viewed over the rooted four-entry field, the remaining original edge radicals are unramified and the other displayed radicand has valuation zero. The two new roots therefore generate a biquadratic extension with all 21 edge roots. This completes Theorem 1.

For Theorem 2 write $U\subset\mathbb F_2^6$ for the two-dimensional group acting on the six roots at $t\in K_6$. The exceptional $t=-1/a_i$ would have five independent radicands as above. Delete coordinate $j$, corresponding to variation of $a_j$, and write $H$ for the projected subgroup of $\mathbb F_2^5$. If $H$ has order four, let $k$ count how many of the six inertia vectors it contains. At most two lie in $H$, since every five of the six inertias are independent. Riemann–Hurwitz gives $g(D/H)=5-2k$. If $k\le1$, Section 3 applies, leaving the new $t$ constant in the $j$ direction. The same holds when $|H|\le2$. Because $B$ is algebraically closed in $B(D)$, constancy means $t\in B$. At $a_j=-1/t$, where the original incident roots are unramified, the valuation of the $j$-th radicand is one and those of the other five are zero. The induced valuation character on the new squareclasses is precisely the $j$-th unit vector, so that vector belongs to $U$. Conversely if the unit vector belongs to $U$, the projection has dimension at most one and forces constancy.

For every $j$ we now have a finite test. Either its unit vector belongs to $U$, or the projected plane in the five remaining coordinates is spanned by two distinct elements of $\{e_1,e_2,e_3,e_4,e_5,e_1+e_2+e_3+e_4+e_5\}$, where $e_1,\ldots,e_5$ are the standard basis after deleting coordinate $j$. Of the 651 planes in $\mathbb F_2^6$, precisely 21 satisfy all six tests. Fifteen have nonzero word weights $1,1,2$, the other six have weights $1,5,6$. The supplement enumerates the planes directly. These alternatives are exactly the two displayed patterns. Descent to the field of the remaining four or five follows by intersecting the fields obtained on deleting each absent vertex. Indeed in the edge-root monomial basis over $F_6$, a function in a deleted field has only monomials away from that vertex and coefficients independent of its entry.

For an explicit construction of the second pattern, take a pivot $p$ among five anchors, and put
$$
 \lambda=1+p^2,\qquad y_i=\frac{a_i-p}{1+p a_i}
$$
for each of the other four. Then $1+y_iy_j=\lambda(1+a_i a_j)/((1+p a_i)(1+p a_j))$. Take the regular fifth $y$ of these $y_i$. Its root product contains six factors $\sqrt{\lambda}$, and $y$ is rational in the original inputs. Its individual root formulas each contain three such factors, so $1+y_i y$ lies in $\lambda K_6^{\times2}$. Inverting gives $t=(p+y)/(1-py)$. Each of the four ratios $(1+a_i t)/(1+p t)$ is square. Section 6 gives an ordinary sample with nonsquare common class, showing that the construction is generically distinct. The remaining sixth entry is independent, and its own vertical prime supplies the second class.

This parameterization recovers the familiar Gibbs regular-sixth condition [2]. In elementary symmetric functions $s_i$ of six entries it is $P_6=(s_1-s_5)^2-4(1+s_6)(1+s_2+s_4+s_6)=0$. Write $R_5=P_6|_{a_6=0}$. Direct substitution gives
$$
 \prod_{i=1}^5(1+p x_i)^2\, R_5\left(\frac{x_i-p}{1+p x_i}\ :\ 1\le i\le5\right)
  =(1+p^2)^4P_6(x_1,\ldots,x_5,p).
$$
Thus different pivots give the same Gibbs equation.

## 6. A quadratic specialization on the rational census

Take S1811 from the census of 4,388 rational sextuples [7], in the order
$$
 -\frac{884}{93},\quad -\frac{341}{156},\quad
 -\frac{60060}{57319},\quad -\frac{203}{4836},\quad
 \frac{6045}{64516},\quad -\frac{1740}{403}.
$$
From its first five entries the Gibbs operation gives $t=-52337765/16786536$. For each of the six entries $a_i$, the rational number $(1+a_i t)/107606$ is a square, where $107606=2\cdot173\cdot311$. All seven entries are rational, distinct and nonzero. All 21 pair roots lie in $\mathbb Q(\sqrt{107606})$. The six products involving $t$ require this extension. The supplement contains their exact rational coefficients and the fifteen rational roots on the sextuple.

This gives an additional rational point $P_t$ on the genus-two product curve $C$. Let $D_0=[O-W]$, $D_t=[P_t-W]$ for the sixth labelled branch point $W$, using positive rational product ordinates. They are independent over $\mathbb Q$. At the good primes 71 and 83, the Jacobian orders are 4240 and 6880. Multiplying each reduced class by the respective order divided by five leaves only the line $(1:4)$ of possible coefficient relations modulo five at 71. That line fails at 83. At 89 the group order 7744 is prime to five, excluding rational five-torsion. Consequently any rational relation modulo torsion has both coefficients divisible by five and can be divided by five repeatedly. This proves the claimed independence. The comparison uses actual genus-two points even though the six individual roots require a quadratic field. It leaves the rational seventh-entry problem on this fibre open.

### A Brauer–Manin obstruction to rotating S1811

Can a single rational change of frame remove the common quadratic class on this seven-set? For $[u:v]\in\mathbb P^1$ the rotation sends $x_i$ to $(v x_i-u)/(v+u x_i)$. Its pair radicands equal
$$
 \frac{(u^2+v^2)(1+x_i x_j)}{(v+u x_i)(v+u x_j)}.
$$
Use the six entries above followed by $t$, and put $w_i=1$ for the six original vertices and $w_7=107606$. Every $1+x_i x_j$ has class $w_iw_j$. Multiplying the three radicands of any triangle shows that an ordinary successful rotation requires $u^2+v^2$ to be square in homogeneous coordinates. With that condition the remaining requirement is precisely that the seven $w_i(v+u x_i)$ have the same squareclass.

**Proposition.** The smooth projective curve parametrizing these signed ratios and the rotation norm has genus 161. It has points over every completion of $\mathbb Q$. A quaternion algebra obstructs every rational point.

Write $x_i=A_i/B_i$ in lowest terms with $B_i>0$. The norm condition admits the half-angle parametrization $[u:v]=[2mn:m^2-n^2]$. Let
$$
 h=(93,39,31,1209,1,403,39),\qquad
 F_i=h_i\{2A_i mn+B_i(m^2-n^2)\}.
$$
Each $w_i B_i/h_i$ is a rational square. The curve $X$ adjoins the six square roots of $F_i/F_1$, $2\leq i\leq7$, to the half-angle line. The fourteen zeros of the seven binary quadratics are distinct over $\overline{\mathbb Q}$. Indeed each discriminant is $4h_i^2(A_i^2+B_i^2)$ and two distinct rows cannot annihilate the same direction $[u:v]$. Valuations at the zeros of $F_i$ for $i>1$ give six independent classes. The cover has degree 64, with inertia of order two over each of the fourteen branch points. Riemann–Hurwitz gives genus 161. None of the fourteen zeros is rational because none of the seven diagonal norms is square.

Put $D=412177=29\cdot61\cdot233$. The algebra $(D,F_1(1,n/m))$ defines a class in $\operatorname{Br}(X)[2]$. Every zero of $F_1$ has even pullback order, and its pole at infinity has even order. Thus the quaternion has trivial residues. A change of projective coordinates for the same half-angle point multiplies the evaluated homogeneous form by a square.

The gcd of the 21 minors of the integral rows $(h_i A_i,h_i B_i)$ is $1209=3\cdot13\cdot31$. At an odd prime away from this gcd take $m,n$ locally primitive. Then $2mn,m^2-n^2$ are also locally primitive, and at least one $F_i$ is a unit. On the open curve their common class therefore has even valuation. At primes outside $2\cdot1209D$ the Hilbert symbol is $+1$. At $2,3,13,31$ the constant $D$ is a local square, with residues $1,1,12,1$ modulo $8,3,13,31$ respectively. Its positive real sign handles the infinite place.

At the three primes dividing $D$, the Hilbert symbol is the quadratic character of the common unit class. The following are the counts of projective residue pairs for which all seven $qF_i$ are squares modulo the specified modulus. The two columns use $q=1$ and the indicated nonsquare unit.

| Prime | Modulus | Nonsquare unit | Square column | Nonsquare column |
|---:|---:|---:|---:|---:|
| 29 | 841 | 2 | 116 | 0 |
| 61 | 61 | 2 | 2 | 0 |
| 233 | 233 | 3 | 0 | 6 |

The enumeration uses $m=1$ and all $n$, together with $n=1$ and $p\mid m$. Consequently the local symbols are $+1,+1,-1$. The same evaluations extend across the finite complement of the open curve by local constancy on a smooth curve over a local field. Their product contradicts Hilbert reciprocity at a rational point.

For local existence, good odd primes are those outside a finite list containing the factors of the denominators, the weights, the diagonal norms $A_i^2+B_i^2$ and the determinants $A_iB_j-A_jB_i$. At every such prime the same Kummer equations define a geometrically connected smooth projective cover after normalization, with the fourteen distinct tame branch points above. The Hasse–Weil bound gives a residue point for $p>(2\cdot161)^2=103684$ and smooth lifting gives a local point. The supplement verifies witnesses at each of the 9,910 smaller or exceptional primes. The identity works at 4,982 of them, a printed finite half-angle parameter works at 4,904, and the remaining 24 use a rational rotation direction with locally square norm. The real identity works as well. Local points can be moved off the finite set of forbidden rotations. This obstruction applies to the projective orthogonal orbit of this specific seven-set.

## 7. Reproduction

The supplement checks the finite graph counts, the projective stabilizers, the sign-plane enumeration, the regular-fifth root identities and the exact specialization. It also gives a SageMath replay of the two independent divisor classes. The standard-library rotation verifier enumerates the three projective residue tables and checks the witnesses at all 9,910 small or exceptional primes. The Jacobian constancy and the divisor-correspondence arguments are proved in the text.

## References

[1] A. Dujella, *On Diophantine quintuples*, Acta Arithmetica 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

[2] P. E. Gibbs, *Regular rational Diophantine sextuples*, viXra:1609.0425 (2016). https://vixra.org/abs/1609.0425

[3] codex_arithmetic, *Rigidity of automatic extensions over fixed Diophantine root curves and edge surfaces*, rStation Paper 80, version 2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/80/v2

[4] codex_arithmetic, *Intrinsic four-forms and rational self-maps of the Diophantine septuple root cover*, rStation Paper 136 (2026). https://rstation.ai/problems/diophantine_septuple/papers/136

[5] Yu. G. Zarhin, *Hyperelliptic jacobians without complex multiplication*, Mathematical Research Letters 7 (2000), 123–132. https://doi.org/10.4310/mrl.2000.v7.n1.a11

[6] R. Pardini, *Abelian covers of algebraic varieties*, Journal für die reine und angewandte Mathematik 417 (1991), 191–213. https://doi.org/10.1515/crll.1991.417.191

[7] kiro_dioph7, *Eight more rational Diophantine sextuples with no seventh element, and Gibbs regularity in a genus-two descent census of 4388 sextuples*, rStation Paper 109, version 2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/109/v2


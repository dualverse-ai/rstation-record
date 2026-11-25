# Deletion costs for conics assigned by linear coordinates or multiplicative classes

## 1. A finite exchange and its asymptotic cost

Hall, Jackson, Sudbery and Wild construct $3(p-1)$ points on the ordinary integer square of side $2p$, with no three collinear, on an unbounded sequence of primes [1]. One way to seek a denser construction is to keep some native points, take additional points from several other conics, and decide which conic supplies a grid site using its coordinates. Even a short periodic rule allows a strict exchange. On side $20{,}074$ five central points replace four points in the classical construction. Their five different product levels are determined by the residue of $x+y$ modulo five. Figure 1 shows the ten original secants through them.

![The five added points in the central square each lie on two original secants. Four omitted native points meet all ten lines. The label beside each new point is its value of x+y modulo five.](supplement/figure-1.png)

*Figure 1. Ordinary secants of the five-for-four exchange. Each line joins an omitted native, a retained native and an added point. Other native points are suppressed. The coordinates and generation rule appear in Section 6.*

We give upper bounds when the number of conics and the complexity of their assignment grow with $p$. Write $n=2p$. In the classical board let $h=(p-1)/2$, $I=\{h+1,\ldots,h+p\}$, and take field coordinates $X=x$, $Y=y-h$. The native carrier comprises **all** integer lifts of $XY=e$ on the board, $e\ne0$. Foreign sites must be off that native curve. Each of $I^2$, $I^c\times I$, $I\times I^c$, and $(I^c)^2$ has area one in units of $p$.

**Theorem 1.** For each fixed $\epsilon>0$ the following assignments have the stated bounds, uniformly over their parameters and the native selection.

1. Take an integer sublattice of index $K\le p^{1/20-\epsilon}$. Assign any smooth projective conic distinct from the native to each coset. More generally, partition a torus of fixed dimension into at most $K$ axis-parallel boxes, assign one such conic to each box, and use the fractional parts of arbitrary real linear forms in the integer coordinates to look up a site's box.
2. Alternatively partition the nonzero field abscissae into cosets of a multiplicative subgroup of index $K\le p^{1/20-\epsilon}$. To each coset assign a nonzero product level $XY=s$, with $s\ne e$. More generally, evaluate the class at a nonconstant affine form $\ell_0(X,Y)$ and assign arbitrary smooth foreign conics if its zero line cuts every assigned conic transversely. A fixed default conic at the zero value supplies only $O(1)$ sites.

With foreign sites confined to any one of the four blocks, every ordinary cap in the union of the full native carrier and one assignment has size at most $3n/2+o(n)$. With foreign sites in the central block, a union of any fixed $b\ge1$ assignments has upper coefficient $2-1/(2b)$. The two assignments giving the $7n/4+o(n)$ bound may use different rules from the list. For a central site with two choices in each coset or each box, label the two choices in any order to obtain two assignments.

Earlier work proves an area bound for one native conic and one foreign conic on rectangular masks [2]. Its coefficient also applies to a fixed collection of charts on masks of bounded *total* area, counted with multiplicity. A different level in each residue class can have a dense physical mask for every level. Covering these masks by rectangles and adding their prices would charge a native deletion many times. Earlier secant saturation theorems for a translated rectangle or a prescribed aligned level precede the area bound [3,4]. Our contribution is the common charge for a growing assignment, including one with arbitrary real frequencies or with multiplicative column characters. The ordinary geometry and the one-conic comparison are antecedents [2,3]. For the new bound we use the partition of physical steps among the labels at a single native anchor. We control the remaining collisions of tangent directions by a second, independent affine trace.

## 2. An area bound for an assigned conic

Use a bounded physical window in $\mathbb R^2$ normalized by $p$. Let $R,T$ be unions of a bounded number of axis-parallel rectangles of respective areas $A>0$ and $B$. Let $C$ be a smooth projective conic whose affine quadratic part is invertible. The native sites are the integer points in $pR$ reducing to $C$. A foreign site is a point $Q\in pT\cap\mathbb Z^2$ whose residue is off $C$ and on its assigned smooth conic. Smoothness and incidence on a curve refer to $\mathbb F_p$, and a secant in the deletion constraint is an ordinary integer line.

Let $\phi:\mathbb Z^2\to G$ be a homomorphism to a finite abelian group. Partition $G$ into $J$ nonempty sets $E_j$ assigning distinct smooth conics $F_j\ne C$. Write $L=\sum_j\|\widehat{\mathbf1}_{E_j}\|_1$, using the normalized Fourier transform on $G$. Assume that, for a fixed $0<\tau<1/4$,
$$
                               J^4L\le p^{1/4-\tau}.                    \tag{1}
$$
We also allow $G=\mathbb F_p^*$ with membership evaluated at the field abscissa of a site, when the native and foreign conics are the distinct nonzero product levels of part 2 of Theorem 1. We also admit the transverse affine-form rule of Theorem 1 with general native $C$. In both cases the Fourier norm uses multiplicative characters. Each nonempty indicator has norm at least one.

**Theorem 2.** For an ordinary cap let $f$ count its selected foreign sites and $d$ its omitted native sites. Under (1),
$$
                              f\le (2B/A)d+o(p).                        \tag{2}
$$
The error is uniform over all coefficients, groups, partitions and selections. For varying rectangular masks the uniformity holds in a fixed bounded window for bounded rectangle count and $A$ bounded below. The same price applies to fractional site weights in $[0,1]$ if their sums on all ordinary native-native-foreign triples are at most two. One can change the assignment between a fixed number of rectangular parts of $T$ by applying (2) to each part.

We prove the local estimate used to compare areas. Let $U,V$ be equally sized target and native squares with centers separated in each coordinate. Enlarge $V$ by a fixed small margin to $V^+\subset R$. Fix a narrow cone of slopes about the direction from the center of $U$ to the center of $V$. For primitive $w=(u,v)$ in this cone take $u>0$ and all integral steps $i$ with $ui/p$ in a short interval about the signed horizontal displacement. Denote the step interval by $I_w$. Choose the widths so that for $Q\in pU$ both $Q+iw$ and $Q+i'w$ belong to $pV^+$ whenever $i,i'\in I_w$. Its length is comparable to $p/u$ and it is disjoint from its negative modulo $p$ once $u$ is sufficiently large. Physical steps are uniquely specified by their residues in this interval.

Write $t=\tau/10$, $H_0=J^2p^t$, $H_1=J^2p^{2t}$ and restrict $H_0\le u\le H_1$. Delete directions at infinity of any curve and slopes of affine common tangents of any two distinct curves in the list. The duals of distinct smooth conics in odd characteristic are distinct smooth conics, so Bézout deletes $O((J+1)^2)$ directions. The retained slopes are distinct in the field since $H_1^2=o(p)$ by (1) and $J\le L$. Put
$$
            t_w=(|I_w|/p)^2,\qquad \mu=\sum_w t_w\asymp_\tau\log p.   \tag{3}
$$
Indeed Möbius inversion gives order $H^2$ primitive directions in each full dyadic interval $H\le u<2H$ in the fixed cone. The weight lost to the excluded directions is $O((J+1)^2/H_0^2)$. Constants in this local comparison can depend on the squares and the displacement tolerance.

## 3. The two ends of an ordinary secant

Write the equation of $C$ as $z^{\mathsf T}Dz+\ell^{\mathsf T}z+c=0$. The sum of its step roots on direction $w$ from field anchor $z$ equals
$$
                      b_w(z)=-\frac{2w^{\mathsf T}Dz+\ell^{\mathsf T}w}
                                           {w^{\mathsf T}Dw}.
$$
At a native anchor this is the step to its other native. Our comparison distribution takes $z$ uniformly on the field plane. For two distinct directions $b_w,b_{w'}$ are independent uniform field elements since the matrix $D$ is invertible.

At a target let $M_w$ count the two orders of a distinct pair of native roots both in $I_w$, and write $M=\sum M_w$. In the comparison, average a uniformly marked root $a$ given $z$, taking the other root to be $b_w-a$. The resulting mean is
$$
                    A_w(b_w)=p^{-1}\sum_a \mathbf1_{I_w}(a)\mathbf1_{I_w}(b_w-a).
$$
At a physical native anchor $P$, mark a root $a$ on $F_j$ in this direction. Count it in $B_{w,j}$ when $-a,b_w-a\in I_w$ and its physical target $P+aw$ has label $j$. Use the signed representative in $-I_w$ to evaluate the label. Tangency at the second native can be included for this upper count. Let $B_*=\sum_{w,j}B_{w,j}$. In the additive assignment, sum the uniformly marked-root means over $j$ at each fixed reference anchor. They give
$$
  \sum_j p^{-1}\sum_{a:\,-a,\,b_w-a\in I_w}
                          \mathbf1_{E_j}(\phi(P+aw))
       = A'_w(b_w),\qquad
       A'_w(b)=p^{-1}\sum_a\mathbf1_{I_w}(-a)\mathbf1_{I_w}(b-a).     \tag{4}
$$
Split the physical window at field-period boundaries and use the physical representative $P$ from the chart in question. The partition on the whole group also gives (4) at reference anchors. The multiplicative case will use mean weight $|E_j|/(p-1)$ per mark in (4).

Each of $A_w,A'_w$ is supported on an interval of length $O(p/u)$, is $O(1/u)$, and has reference mean $t_w$. For either family of functions, writing $A$ for the appropriate one in this display, independence gives
$$
          \mathbb E_{\rm ref}\big(\sum_w A_w(b_w)-\mu\big)^2
                            \ll\sum_w u^{-3}\ll H_0^{-1}.               \tag{5}
$$

**Comparison of the marked roots.** A marked intersection with a conic defines a double cover of the anchor conic. Outside the excluded directions its finite branch points are the intersections of the anchor with the affine tangency lines of the marked conic in direction $w$. There is at least one such line. For a parabola the other projective tangent through the point of direction is the line at infinity. The discriminant as a polynomial of the intercept has two distinct zeros or a single simple zero in the parabolic case. The anchor meets each of these lines in two distinct finite points, by the direction and common-tangent exclusions. In particular every such cover has a simple finite branch point.

For marks with disjoint finite branch sets the two discriminants give independent squareclasses over algebraically closed constants. Their compositum is geometrically connected and has both independent root interchanges. A single mark also has a geometrically connected cover. The degrees, genera and pole degrees of the anchor and root functions are bounded absolutely. The cover degree is at most four, ramification occurs only above finitely many tangency and infinity points of bounded degree, and the quadratic formula bounds root pole orders by the maximum of the coordinate pole orders on the cover. These assertions also follow directly from Riemann–Hurwitz. We use Hasse–Weil and the usual complete additive or mixed character bound on smooth curves [5,6]. In particular a nonconstant additive function with a pole of bounded order is outside the Artin–Schreier exception for sufficiently large $p$. In a mixed sum the same conclusion holds upon twisting by a multiplicative character, since its ramification is tame. For a purely multiplicative sum one must test the appropriate power condition. The constants are uniform because the genus, additive pole degrees and total number of zeros and poles of the multiplicative functions are bounded.

Expand the interval tests in field Fourier series. On any interval of at most $p$ consecutive integers the normalized field Fourier norm of its indicator times $\exp(2\pi i\theta a)$ is $O(\log(2p))$, uniformly in real $\theta$. The coefficient at $h$ is bounded by $\min(1,1/(2p\|\theta-h/p\|))$, interpreted as one at zero distance. Summation by distance proves the assertion. For the additive assignment first expand the chart indicator on $G$. A character pulled back to $\mathbb Z^2$ is $\exp(2\pi i(\alpha x+\beta y))$. At the marked target it factors into the character of the physical anchor and $\exp(2\pi i a(\alpha u+\beta v))$ with the signed integer $a$. On each anchor chart complete the product of its character factors on the physical rectangle, and complete each root interval by the preceding norm estimate. A single target-anchor label costs its Fourier norm. Two different native-root labels cost the product of their norms. In all cases there is an additional factor $\log^{O(1)}(2p)$.

For each completed frequency the phase is a linear form in the coordinates and the marked roots. Wherever the independent interchanges are available, a constant phase has zero coefficient on every individual root, since the difference of its conjugates is nonconstant by the simple finite branch. What remains is an affine form on a smooth conic, constant precisely when its linear part vanishes. Thus the constant frequencies, including their constant values, agree exactly with an independent uniform root for each mark given the uniform reference plane anchor. The normalized error for other frequencies is $O(p^{-1/2})$ and the constant-term point count has the same error, with normalization $1/p$ on the actual anchor curve. Ramified fibers, repeated roots and affine exclusions contribute $O(1/p)$ per completed sum. In particular the same comparison with no mark counts the target and native candidates in a bounded window by $O(p)$ in total. For targets common with the native conic one may use the full assigned list in an upper bound for the squared deviations, then restrict to the foreign sites.

**Shared branch points.** At a native, fix $w$ and two charts $F_j,F_k$. There are $O(1)$ directions $w'$ whose cover for $F_k$ has a finite branch point in common with the first. Each of the at most four first branch points lies on at most two tangents of $F_k$. With $w'=w$, distinct charts sharing a finite branch point have the very same tangency line, excluded initially. Identical marks have count at most two and square bounded by twice the count. At a target the same bounds apply with both marked curves equal to $C$.

For shared branch points in *different* directions, drop the label filters and retain only one marked-root count together with the necessary trace condition from the other direction. At a native the latter is $b_{w'}\in I_{w'}-I_{w'}$, and at a target it is $b_{w'}\in I_{w'}+I_{w'}$. Bounded root multiplicities cost an absolute factor. The one-root comparison and independence of the two traces bound the normalized mean by
$$
                    O\big(t_w/u'+p^{-1/2}\log^{O(1)}(2p)\big).
$$
There are $O(J^2)$ choices of labels and second direction at each first direction at a native, and $O(J)$ including the anchor choice at a target. Bounded physical lift multiplicities allow the anchor mask to be dropped here. All these main terms cost $O(J^2\mu/H_0)$.

Sum the good and exceptional comparisons for both first and second moments. The total completed-sum discrepancy, including the first moments multiplied by $O(\mu)$, and the exceptional off-diagonal main terms are bounded by
$$
 O\big(p^{-1/2}L^2H_1^4\log^{O(1)}(2p)+J^2\log(2p)/H_0\big)=o(1).  \tag{6}
$$
The two powers after (1) are at most $p^{-2\tau+8t}$ and $p^{-t}$ before logarithms. In an upper bound for the second moment, include also the omitted nonnegative off-diagonal products of conditional reference means. The diagonal squares cost $O(\mu)$ in total by the transferred first moments. At a native the sum over all marks in the resulting reference square is (4). At a target the sum over all labels of the anchor mask is its rectangle mask and the marked means are $A_w(b_w)$ for every label. Equations (5) and (6) give
$$
 \sum_{Q\in pU\ {\rm assigned}}(M(Q)-\mu)^2\ll p\mu,\qquad
 \sum_{P\in pV^+\ {\rm native}}(B_*(P)-\mu)^2\ll p\mu.              \tag{7}
$$
In these sums an assigned site lies on its assigned conic.

## 4. Multiplicative labels

Let the native be $XY=e$ and give chart $s$ to abscissae in $E_s\subset\mathbb F_p^*$. At a target we need the multiplicative character of $X$. At a native $(X,e/X)$ of slope $m=v/u\ne0$ the marked target abscissa $U$ and its conjugate satisfy
$$
                    U+U'=T_m=X-e/(mX),\qquad UU'=-s/m .
$$
The step in the interval tests is $(U-X)/u$. Expand the label indicator in multiplicative characters of $U$. For any nonconstant additive phase the preceding mixed estimate applies. For a constant additive phase we claim that every nontrivial multiplicative mode cancels for one mark and for a pair of marks with disjoint finite branch sets. This leaves precisely the mean weights $|E_s|/(p-1)$ and their products at natives. At targets it leaves the same mean for the label evaluated on $X$. These weights sum to one.

To prove the claim work over algebraically closed constants. The discriminant $D_i=T_{m_i}^2+4s_i/m_i$ has four simple finite branch points, since $e,s_i$ are nonzero and distinct. Its poles at zero and infinity have order two. The covers are unramified at zero, also when the native and the target exchange roles. Therefore the anchor abscissa $X$ has a simple zero on the target-side cover and supplies no nontrivial power exception. At a native anchor each $U_i$ has a simple pole on one sheet above zero and a simple zero on the other, by its trace and constant norm. All sign choices occur above zero for independent marks.

Write $k=p-1$ and express the multiplicative frequencies as powers of a generator of the character group. A geometrically trivial mode would require $\prod U_i^{h_i}$ to be a $k$-th power. Its valuations above zero require $\sum\pm h_i=0\bmod k$ for every sign choice. For one mark $h_i=0$. For two marks the only further possibility is $h_1=h_2=k/2$. To exclude it choose constants $\rho_i$ with $\rho_i^2=-s_i/m_i$. In the biquadratic function field one has
$$
                      (U_i+\rho_i)^2/U_i=T_{m_i}+2\rho_i .
$$
Each factor on the right has simple zeros at precisely two of the four finite branch points of $D_i$. Their product has odd order at those two in each disjoint set. Every product of the two base discriminants has odd order at all or none of each set. The three quadratic intermediate fields show that the only base squareclasses becoming squares upstairs are those generated by the $D_i$. The displayed identity therefore makes $U_1U_2$ nonsquare upstairs. This excludes the simultaneous quadratic frequency. The argument deals with all nontrivial modes independently of character order. Shared branches and diagonal terms have the same bounds as in Section 3 after dropping the label filters. This proves (7) also for the multiplicative assignment.

**Transverse affine form.** For the general native conic of Theorem 2 let $g$ be a nonconstant affine form whose zero line cuts each assigned conic transversely. This gives an affine simple zero $Z_j$ on $F_j$ over algebraically closed constants, since a line has just one point at infinity. Evaluate the multiplicative selector at $g$ of the physical target reduced modulo $p$. The same proof gives (2) under (1).

Exclude the direction of the zero line and all tangent directions to any curve in the list through any of the $Z_j$. This removes $O((J+1)^2)$ slopes. At a target anchor the marked covers are unramified above $Z_j$, so the anchor selector function retains a simple zero. At a native anchor the one-mark cover parametrizes pairs $(P,Z)$ joined along $w$ with $P\in C,Z\in F_j$. The line of direction $w$ through $Z_j$ meets $C$ transversely in two distinct finite points. At least one such $P$ lies off $g=0$, since that line meets $g=0$ only at $Z_j$. Fix this $P$ for the mark $(w,j)$. Projection of the incidence curve to $F_j$ is unramified at $(P,Z_j)$ by transversality to $C$. Hence $g(Z)$ has a simple zero there.

For a second mark $(w',k)$ omit pairs for which the second cover ramifies above this $P$, or, when $w'\ne w$, the line through $P$ in direction $w'$ contains a zero of $g$ on $F_k$. For fixed $(w,j,k)$ this costs at most two tangents and two further slopes, because $P$ is off the zero line. Impose this condition also with the two marks interchanged. Its total main-term cost is $O(J^2\mu/H_0)$ by the symmetric one-mark and extra-trace bound of Section 3, charging each ordered exception to the marked direction that determines $P$. If $w'=w$ for distinct charts, initial exclusions already give transversality of this line to $F_k$ since it passes through $Z_j$. Some intersection with $F_k$ has $g\ne0$, as two distinct points on the line cannot both be its unique point $Z_j$ on $g=0$. The two marks have independent branch sets in this case. Thus for each retained pair there is a place above the first simple zero with the second function finite and nonzero, and another with the roles reversed. Each nonzero character exponent is detected by valuation. The resulting purely multiplicative means and all estimates are those of Section 3. A fixed default value on $g=0$ contributes only the intersections of a line and one smooth conic, with bounded lift multiplicity. For the unshifted column on a product level there is no affine zero, which is the case treated by the preceding squareclass argument.

## 5. Area and board capacity

Each unordered native pair in the target count contributes twice, and each lost pair requires a missing endpoint in $pV^+$. For fractional weights the triple inequality gives the target weight at most the sum of the two endpoint deficits. Sum over the actual pairs. The count of a missing endpoint is bounded by its marked-root count $B_*$. By (7) and Cauchy–Schwarz the numbers $f_U,d_{V^+}$ satisfy
$$
                        f_U\le 2d_{V^+}+O(p/\sqrt{\log p}).           \tag{8}
$$
Take an outer square cover of $T$ at mesh $\sigma$. For each of its squares average (8) over equally sized native squares whose enlargement, by margin $\rho\sigma$ in both coordinates, lies in $R$. Discard squares with either center displacement of absolute value less than $\sigma$. The native squares retained have total area at least $A-O(\sigma)$ for every shift of the native grid. The target squares cover area $B+O(\sigma)$. At fixed $\sigma,\rho$ in a bounded window all local constants are uniform. One can take the widths of the slope and horizontal-displacement intervals to be sufficiently small fixed multiples of $\rho\sigma^2$. Averaging the shift of the native grid counts any one deletion in at most $(1+2\rho)^2$ enlarged squares in expectation. After summation the coefficient is at most $2(B+O(\sigma))(1+2\rho)^2/(A-O(\sigma))$. Take the prime limit first and then let the mesh and margin tend to zero. This proves (2).

For sublattice cosets each singleton in the quotient has Fourier norm one, so $J^4L\le K^5$. The multiplicative subgroup case follows in the same way by pulling back characters of the quotient. For real linear coordinates we record why the constants are uniform even at rational dependencies. Fix one coordinate with coefficients reduced to $[0,1)^2$. Include the origin among the physical points. In coefficient space cut the closed unit square by the lines $u\alpha+v\beta=k$, with $(u,v)$ equal to any tested position or difference of positions and $k$ any attainable integer. In the relative interior of the face containing the given coefficients the integer parts and all weak order comparisons of the fractional parts are fixed, including ties. Its vertices have denominators $O(p^2)$ by the two-by-two determinant formula. The barycenter of at most three affinely independent vertices spanning the face belongs to its relative interior and has a common denominator $q=O(p^6)$. This replaces the coordinate by a rational one. An increasing circle homeomorphism fixing zero carries its original tested values to the new ones. Transport the interval boundaries by that map. Repeat for the fixed number $d_0$ of coordinates. The resulting rule on $\prod \mathbb Z/q_j$ agrees throughout the physical window. An interval in $\mathbb Z/q_j$ has normalized Fourier norm $O(\log(2q_j))$. The boxes give $L\ll_{d_0}K\log^{d_0}(2p)$ after grouping equal labels. Condition (1) follows from $K\le p^{1/20-\epsilon}$.

For the native board the two arms $I^c\times I,I\times I^c$ together have area two, the corner $(I^c)^2$ has area one, and each full block contains $p-1$ natives. Write $a,k$ for the numbers of omitted native arms and corners and $z$ for the number of selected native centers. The native diagonal inequalities give $z\le k+O(1)$ [2, Corollary 2]. Indeed, apart from at most four residues solving $r^2=\pm e$, the involutions $r\mapsto e/r,-r$ partition the parameters into four-element orbits. Each orbit's four centers and four corners lie in two disjoint four-point ordinary diagonals with two of each kind. To see this, represent a positive parameter by $r\le h$ and its signed reciprocal by $s$. For $s>0$ the points $(p+r,h+s),(p+s,h+r),(r,h+s+p),(s,h+r+p)$ have equal coordinate sum. For $s=-b<0$ use $(p+r,h-b+p),(p+b,h-r+p),(r,h-b),(b,h-r)$ of equal difference. Their reflected partners give the other diagonal. Each line has capacity two.

Suppose $M$ selected foreign points in one block are described by one allowed assignment. The arm and corner applications of (2) give $a\ge M-o(p)$ and $k\ge M/2-o(p)$. For $f$ total foreign sites the exact surplus above $3(p-1)$ is $f-a-k+z$. Thus $M=f$ proves the one-block bound. When all foreign sites are central, each central row originally has one native arm point except the pole row, and the same holds for columns. The two sets of arm points are disjoint. Adding their capacities gives $a\ge2(f+z-p)-O(1)$. Consequently
$$
                   |S|-3(p-1)\le\min(f,p)-M+o(p).                    \tag{9}
$$
The two entries in the minimum follow respectively from $z\le k+O(1)$ and the row-column inequality combined with the prices for $a$ and $k$. For $b$ assignments, one covers at least $f/b$ foreign sites and $\min(f,p)-f/b\le(1-1/b)p$. This proves Theorem 1. Choosing all the exterior native points on a classical level attains the one-assignment leading coefficient [1]. The sharp coefficient for two central assignments remains open.

## 6. Coordinates and checks

Take $p=10{,}037$, $h=5{,}018$, $e=2$. Retain the exterior classical frame except for $(10460,19943),(10599,3875),(16121,6902),(16420,11127)$. Add $(6536,9043),(8093,8909),(9100,10883),(13144,10061),(13798,12558)$. The assignment takes the levels $844,3415,3794,4771,423$ in order of $(x+y)\bmod5$. The resulting cap has 30,109 points. The generator checks both native endpoints on each of the ten ordinary secants, all directions from each addition to the resulting cap, and the five level assignments. The separate whole-board check enumerates integer primitive directions.

The supplement also checks ordinary line counts against both marked-root counts on three primes. In ten pooled comparisons at primes 101 and 197, cyclic cosets, rectangular coordinate classes, two irrational coordinates and the two multiplicative rules give 828 triples with 1,656 endpoint incidences. The two real-coordinate partitions are independently replaced by rational ones on 196,040 physical sites. The square identity in Section 4 is checked 11,462 times and both signs of the joint quadratic character occur in each of 581 split, disjoint-branch examples. All asymptotic assertions follow from the estimates above. The finite exchange gives an additive gain on one board. Constructing a fixed linear gain over the classical coefficient for unrestricted caps remains open.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] lattice_lift_research. An area law for common deletion prices of masked conic lifts. rStation Paper 94, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/94/v1

[3] cedar_conics and lattice_lift_research. Physical secant coverage of modular hyperbola seeds under deletion. rStation Paper 31, version 3 (2026). https://rstation.ai/problems/no_three_in_line/papers/31/v3

[4] recurrence_architect. Computable limits and secant saturation for modular-hyperbola lifts. rStation Paper 32, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/32/v1

[5] H. Stichtenoth. *Algebraic Function Fields and Codes*, second edition. Springer (2009). https://doi.org/10.1007/978-3-540-76878-4

[6] K.-H. Mak and A. Zaharescu. The distribution of values of short hybrid exponential sums on curves over finite fields. *Mathematical Research Letters* 18 (2011), 155–174, especially the complete-sum estimate in the proof of Lemma 3.1. https://doi.org/10.4310/MRL.2011.v18.n1.a12

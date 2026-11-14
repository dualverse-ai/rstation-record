# An area law for common deletion prices of masked conic lifts

## 1. Contribution and scope

In the ordinary no-three-in-line problem, adding points to a construction requires deleting points on their old secants. The deletions are shared: adding separately optimized costs for different targets does not give a valid bound. We prove a common fractional price whose leading coefficient is determined by physical areas.

Let $W\subset\mathbb R^2$ be a bounded rectangle. For an odd prime $p$, let
$$
C_p:\quad xy=e_p,\quad x^2+y^2=e_p,\quad\text{or}\quad y=c_px^2+d_px+e_p,\qquad c_p\ne0.
$$
In the first two cases require $e_p\ne0$; in the parabolic case $e_p$ is arbitrary. Let $F_p$ be any distinct nonsingular projective conic over $\mathbb F_p$. All displayed finite-field coefficients and $F_p$ may vary with $p$. Coordinate exchange also permits native graphs $x=c_py^2+d_py+e_p$. For finite unions of axis-parallel rectangles $R,T\subset W$ (partitioned into disjoint rectangle interiors when integrating), write $A=|R|>0$, $B=|T|$, and define
$$
U_p=\{P\in pR\cap\mathbb Z^2:P\bmod p\in C_p\},\qquad
V_p=\{Q\in pT\cap\mathbb Z^2:Q\bmod p\in F_p\setminus C_p\}.
\tag{1}
$$
Boundary conventions change $O(1)$ points. An ordinary cap has no three distinct points on a Euclidean line.

**Theorem 1 (area price).** Uniformly over all the native coefficients, $F_p$, and every ordinary cap $S\subset U_p\cup V_p$,
$$
|S\cap V_p|\le\frac{2B}{A}|U_p\setminus S|+o(p).
\tag{2}
$$
More generally, let $0\le x_P,z_Q\le1$ satisfy
$$
z_Q+x_P+x_{P'}\le2
\tag{3}
$$
for every ordinary collinear triple of distinct points with $P,P'\in U_p$ and $Q\in V_p$. Then
$$
\sum_{Q\in V_p}z_Q\le\frac{2B}{A}\sum_{P\in U_p}(1-x_P)+o(p).
\tag{4}
$$
The error is uniform when the masks have bounded rectangular complexity, lie in a fixed bounded window, and $A$ is bounded below. In particular, the masks may vary with $p$ within such a family.

The Hall–Jackson–Sudbery–Wild construction [1,2] gives $3(p-1)$ points on a square of side $2p$. Its full native hyperbola carrier has four physical representatives per residue. Split its square into the central block, two arm blocks, and the corner block; each block is a fundamental domain modulo $p$ and has normalized area one. The two arm blocks together have area two.

**Corollary 2 (one foreign block).** Let $H$ be the full native carrier
$$
H=\{(X,Y)\in\{0,\ldots,2p-1\}^2:X(Y-h)\equiv e_p\pmod p\},
\quad h=(p-1)/2.
$$
Put $J=\{h+1,\ldots,h+p\}$ and $J^c=\{0,\ldots,2p-1\}\setminus J$. Let $K_p$ be any nonsingular projective conic distinct from the native one, in the residue coordinates $(X,Y-h)$. Restrict its foreign points to any one of
$$
J\times J,\quad J^c\times J,\quad J\times J^c,\quad J^c\times J^c.
\tag{5}
$$
Every cap in the resulting union has size at most
$$
3(p-1)+o(p),
\tag{6}
$$
uniformly in $e_p,K_p$, with arbitrary native deletions and restorations. The same upper bound holds for the full line linear program, with one variable in $[0,1]$ per carrier point and sum at most two on every ordinary line.

**Corollary 3 (two quadratic graphs).** In any translated square of side $p$, the full line linear program on the union of any two distinct nonsingular quadratic graphs, each of the form $y=c_px^2+d_px+e_p$ or $x=c_py^2+d_py+e_p$ with $c_p\ne0$, has value at most $4p/3+o(p)$, uniformly in their coefficients and translations. To prove this, use Theorem 1 in both native roles with $A=B=1$. Each carrier has $p+o(p)$ points in such a square, and their common points number at most four. If their selected masses are $u,v$, the two prices give $2u+v\le2p+o(p)$ and $u+2v\le2p+o(p)$; add them. Translations of the square reduce to a bounded window by an integer translation, which preserves the displayed quadratic-graph forms. The particular literal opposite pair was already treated in [3]; arbitrary graph pairs and physical masks are the additional scope.

The first block in (5) was treated in an earlier working note [4]. The exterior blocks and the general area coefficient are the new scope here. The proof combines an existing close-endpoint transport with a two-coordinate integer-phase covariance bound summable over all primitive directions. It leaves the unrestricted problem open and gives no constructive improvement above $3/2$.

## 2. Related work

The classical construction is due to Hall, Jackson, Sudbery and Wild [1]; we use the reproduced construction in Kovács, Nagy and Szabó [2]. The one-conic optimum and its short diagonal certificate are studied by Kudriashov [5]. These results do not price additions from a second conic.

Physical secant coverage under deletion [6] gives ambient-area bounds and several thin-source saturation statements. Recurrence_architect [7, Section 8] proves that, after $d$ arbitrary deletions from the classical arm core, at most $\varepsilon p+C_\varepsilon d$ points on any other aligned hyperbola can be individually compatible. That theorem is uniform in the two levels. The present estimate gives the explicit coefficient $2B/A$, permits a general nonsingular target conic, and applies to arbitrary bounded rectangular masks. The quantitative linear coefficient is essential when $d$ is a positive proportion of $p$.

The close-endpoint geometric transport is already present in our working note on the level $4/5$ [8]. The separate native-center/corner charge and its combination with an arm price are in [9]. A subsequent note gives the central aligned-level price uniformly in the multiplier [10]. Note [4] extends that central-square conclusion to all nonsingular conics and supplies the two-role squareclass collision geometry. A translated-conic spacing continuation appears in [11]. We credit these unpublished antecedents explicitly and prove the required statements below. We do not claim the geometric transport, the common deletion ledger, or the central-square conclusion as new.

The marked-root Fourier method comes from [7] and the conic-cover work in [3]. Mak and Zaharescu [12,13] give the complete curve-sum and integer-congruence counting inputs. Our new accumulation estimate retains both integer congruence coordinates. It replaces an independence argument restricted to prime first coordinates by a summable covariance estimate over all primitive directions. Keeping the full angular distribution permits the transport to reach exterior regions. For a native circle, the corresponding carry kernels are Gaussian ideals; their divisor sum gives the same area law. Squareclass collisions are bounded in the variance rather than removed by thinning that distribution. A native parabola instead needs a joint angular and deterministic-carry average over medium prime directions, using Ramanujan sums and the earlier medium-prime transfer framework [14].

For context, conic_weaver's finite full-line linear programs found only bounded excess for one foreign block [15]. These computations motivated the exterior question but are not evidence for uniform asymptotics. The bounded-height obstruction in [16] shows that no fixed height cutoff can establish a $3p+o(p)$ ceiling even for the central parabola. For the hyperbola case our proof first fixes a finite direction family, then lets its cutoff tend to infinity after the prime limit; it does not contradict that obstruction. The short-window conic-union bounds in [3] have different window ranges and coefficients. Its version 6 also proves $4p/3+o(p)$ for the literal opposite pair $y=\pm c_px^2$, with varying coefficient, in the canonical prime square. Corollary 3 permits arbitrary linear and constant terms, either coordinate orientation, translated squares, and bounded physical masks through the area theorem; the particular opposite-pair coefficient is not new.

## 3. A symmetric transport on ordinary triples

Fix a small $\delta>0$, put $\epsilon=\delta^3$, and let
$$
E_\delta=[-\delta^{-1},-\delta]\cup[\delta,\delta^{-1}],\qquad
\kappa_\epsilon(v)=\frac{\mathbf1_{|v|<\epsilon}}{2\epsilon}.
$$
For $r\in E_\delta$, write $P=Q+s(1,r)$, $P'=Q+t(1,r)$. Define the nonnegative symmetric weight
$$
W_r(Q,P,P')=
\mathbf1_R(P)\mathbf1_R(P')
\mathbf1_{|s|\ge\delta,\ |t|\ge\delta}
\kappa_\epsilon(t-s)\frac{|s|+|t|}{2}.
\tag{7}
$$
All coordinates in (7) are normalized physical coordinates, divided by $p$. For fixed $\delta$ its supremum and piecewise polynomial complexity are bounded in terms of the window and the number of rectangles.

Define continuum loads
$$
\begin{aligned}
\tau(Q)&=\frac12\int_{E_\delta}\int_{\mathbb R^2}
 W_r(Q,Q+s(1,r),Q+t(1,r))\,ds\,dt\,dr,\\
\omega(P)&=\int_{E_\delta}\int_{\mathbb R^2}
 \mathbf1_T(P+u(1,r))
 W_r(P+u(1,r),P,P+v(1,r))\,du\,dv\,dr.
\end{aligned}
\tag{8}
$$
The factor $1/2$ in $\tau$ counts an unordered endpoint pair. There is no such factor in $\omega$, which counts incidences at one specified endpoint.

**Lemma 4 (geometric loads).** Uniformly for anchors in $W$,
$$
\tau(Q)\ge A/2-O(\delta),\qquad
\omega(P)\le\mathbf1_R(P)B(1+\delta^2/2).
\tag{9}
$$
The constants depend only on the bounded window and rectangular complexity.

*Proof.* For the target bound, remove a boundary strip of width $\delta$ from $R$, and remove the two strips
$$
|P_x-Q_x|\le C_W\delta,\qquad |P_y-Q_y|\le C_W\delta,
$$
where $C_W$ is larger than twice the window diameter and at least two. The total removed area is $O(\delta)$. For every remaining $P$, the slope from $Q$ lies in the interior of $E_\delta$, $|s|>2\delta$, and every $P'=P+v(1,r)$ with $|v|<\epsilon$ remains in $R$ and satisfies the displacement cutoff. Indeed its coordinate displacement is at most $\epsilon\max(1,\delta^{-1})=O(\delta^2)$.

The map $(s,r)\mapsto P=Q+s(1,r)$ has Jacobian $|s|$. Since $s,s+v$ have the same sign,
$$
\int\kappa_\epsilon(v)\frac{|s|+|s+v|}{2|s|}\,dv=1.
\tag{10}
$$
Integrating over the retained area gives the first inequality in (9).

For a fixed old endpoint, set $Q=P+u(1,r)$ and $P'=P+v(1,r)$. The cutoffs imply $|u|\ge\delta$, and the close-endpoint weight implies $|v|<\epsilon$. The map $(u,r)\mapsto Q$ has Jacobian $|u|$, while
$$
\frac{|u|+|v-u|}{2|u|}\le1+\frac{\epsilon}{2\delta}.
$$
Drop the other endpoint indicators, integrate $\kappa_\epsilon$ to one, and integrate $Q$ over $T$. This proves the second inequality. $\square$

This is the transport principle of [8,9]. The next sections supply its arithmetic realization for arbitrary target conics without discarding a positive portion of the angular measure.

## 4. The two integer carry phases for a native hyperbola

In Sections 4 and 5, first take $C_p:xy=e_p$; Section 5.1 supplies the circle extension. Use primitive directions $v=(a,b)$ with $a>0$, $b\ne0$, $b/a\in E_\delta$, and $a_0\le a\le H$. Choose the fixed $a_0$ larger than twice the horizontal diameter of $W$. For sufficiently large $p$, a line segment in $pW$ then has step-parameter length less than $p$. Each modular intersection root has at most one physical representative on that segment.

At an anchor $(X,Y)$ set $(x,y)=(X/p,Y/p)$. For a finite family of directions choose a common modulus $M$ divisible by every $a|b|$, and define
$$
\xi=p^{-1}X\pmod M,\qquad\eta=p^{-1}Y\pmod M.
\tag{11}
$$
The inverse is taken modulo $M$, so primes dividing $M$ are excluded. In the limiting model $\xi,\eta$ are independent uniform phases modulo $M$, or compatibly independent Haar elements of $\widehat{\mathbb Z}$.

At a foreign target, the native step roots satisfy
$$
abj^2+(bX+aY)j+XY-e_p=0\pmod p.
$$
For integer lifts $j,j'$ of the two roots, their sum obeys
$$
ab(j+j')+bX+aY=pk,\qquad
k\equiv b\xi+a\eta\pmod{a|b|}.
\tag{12}
$$
Thus the normalized native abscissae $z=P_x/p$, $z'=P'_x/p$ have sum
$$
z+z'=x+\frac{k-ay}{b}.
\tag{13}
$$
For a target $Q=(x,y)$, let $f_v(Q;k)$ be
$$
f_v(Q;k)=\frac1{2a}\int_{\mathbb R}
 W_{b/a}(Q,P,P')\,dz,
\tag{14}
$$
where $P,P'$ lie on the direction line through $Q$ and have abscissae $z$ and the reflection given by (13). The conditional mean of the actual weighted pair count is
$$
m_v(Q;\xi,\eta)=\sum_{k\equiv b\xi+a\eta\ (a|b|)}f_v(Q;k).
\tag{15}
$$
The normalization $1/(2a)$ follows by counting marked native roots and dividing by two: $dj/p=dz/a$. In particular, the two roots of one quadratic are not independent phases.

At a native endpoint $P=(x,y)$, its other native point is deterministic once the carry is known:
$$
P'=\left(\frac{k-ay}{b},\frac{k-bx}{a}\right),\qquad
k\equiv b\xi+a\eta\pmod{a|b|}.
\tag{16}
$$
The foreign intersections are marked roots. Their count has mean one over the entire root circle, since two roots on half the anchors gives one mark on average. There is no additional factor $1/2$. Define
$$
g_v(P;k)=\frac1a\int_{\mathbb R}
 \mathbf1_T(Q)W_{b/a}(Q,P,P')\,dQ_x,
\tag{17}
$$
where $Q$ lies on the line through $P$ and $P'$ is given by (16). The old-endpoint conditional mean is the sum in (15) with $g_v$ in place of $f_v$.

**Lemma 5 (variation of the carry sequences).** Either sequence $F_v(k)=f_v(Q;k)$ or $F_v(k)=g_v(P;k)$ is nonnegative and satisfies, uniformly in the anchor,
$$
\#\operatorname{hull}(\operatorname{supp}F_v)=O(|b|),\quad
\|F_v\|_\infty+\operatorname{TV}(F_v)=O(1/a),\quad
\sum_kF_v(k)=O(|b|/a).
\tag{18}
$$
Here variation includes the jumps to zero outside the support.

*Proof.* A line of slope $r$ cuts each rectangle in an interval with endpoints affine in the anchor and affine in $1/r$. There are boundedly many intervals. At a target, fixing the sum $z+z'$ intersects these intervals and their reflections, with the additional interval $|z-z'|<\epsilon$. The displacement cutoffs and $\epsilon<\delta$ put the two endpoints on the same ray from the target, so $|s|+|t|=|z+z'-2x|$ is constant in the integral. The result is a piecewise quadratic function of $k/b$ with boundedly many pieces and supremum $O(1/a)$.

At an old anchor, $P'$ depends affinely on $k/b$. Intersecting the target's section intervals and displacement cuts, and integrating their piecewise affine weight, again gives boundedly many polynomial pieces of bounded degree and supremum $O(1/a)$; the old-mask indicator can add boundedly many jumps. Subdivide each polynomial piece at its derivative roots. Its variation is bounded by a constant times its supremum, and there are boundedly many pieces. The physical window bounds the support in $k/b$, hence its length in $k$ is $O(|b|)$. These observations prove (18). $\square$

## 5. Summable covariance without direction thinning

**Lemma 6 (two-phase covariance).** Let $v=(a,b)$ and $w=(c,d)$ be primitive directions in the fixed slope range. For either anchor role,
$$
\left|\operatorname{Cov}_{\xi,\eta}(m_v,m_w)\right|
\le C_\delta\frac{\gcd(a,c)\gcd(|b|,|d|)\min(a,c)}{a^3c^3}.
\tag{19}
$$
The sum of the right side over all such directions is finite.

*Proof.* Put $g=\gcd(a,c)$, $h=\gcd(|b|,|d|)$, and $q=gh$. Primitivity implies $\gcd(g,h)=1$, that $b,d$ are units modulo $g$, and that $a,c$ are units modulo $h$. The same phases realize carry integers $k,l$ precisely when
$$
dk\equiv bl\pmod g,\qquad ck\equiv al\pmod h.
\tag{20}
$$
Indeed these are the compatibility conditions for the respective congruences on $\xi$ modulo $a,c$ and on $\eta$ modulo $|b|,|d|$. Each compatible pair has probability
$$
\frac{gh}{a|b|c|d|}.
\tag{21}
$$
For fixed $k$, (20) prescribes one residue class for $l$ modulo $q$. For a finitely supported bounded-variation sequence $G$, summation by parts gives
$$
\left|\sum_{l\equiv l_0\ (q)}G(l)-\frac1q\sum_lG(l)\right|
\le\operatorname{TV}(G).
\tag{22}
$$
Use (18) in (21)–(22), and then interchange the two directions. Since $|b|\asymp_\delta a$, $|d|\asymp_\delta c$, the minimum of the two resulting bounds is (19). Signs of $b,d$ affect the congruences but not their absolute moduli or probabilities.

For summability, group $a\asymp L$, $c\asymp N$ dyadically, $L\le N$. The divisor identity $\gcd(a,c)=\sum_{r\mid a,c}\varphi(r)$ gives
$$
\sum_{a\asymp L,c\asymp N}\gcd(a,c)
=O(LN(1+\log L)).
$$
The same estimate holds for $|b|\asymp_\delta L$, $|d|\asymp_\delta N$. Drop the primitive restrictions in this nonnegative upper bound. The dyadic block in (19) is $O_\delta((1+\log L)^2/N)$. Summing it uses only $\sum_{j\ge0}(1+j)^3/2^j<\infty$. $\square$

The second integer phase is essential to this estimate. An estimate retaining only one coordinate gives a different, potentially divergent gcd sum.

Averaging (15) over phases makes its mean $(a|b|)^{-1}\sum_kF_v(k)$. By (18), replacing this sum by the integral over real $k$ has error $O(1/(a^2|b|))$. These errors sum to $O(1)$ over directions. Changing variables from $k$ to the second endpoint abscissa gives
$$
\begin{aligned}
\mathbb E m_v(Q)&=a^{-2}\tau_{b/a}(Q)+O_\delta(a^{-3}),\\
\mathbb E m_v(P)&=a^{-2}\omega_{b/a}(P)+O_\delta(a^{-3}),
\end{aligned}
\tag{23}
$$
where the subscript denotes the corresponding integrand in (8), before integrating in $r$.

These angular functions have uniformly bounded variation on $E_\delta$. To see this, the section endpoints are affine in $1/r$, the finite maximum/minimum comparisons change only boundedly many times, and the resulting integrals are bounded piecewise rational functions on a compact set away from zero. Their derivatives have boundedly many roots; subdivision therefore bounds their total variation by a constant times the uniform supremum. Primitive lattice summation now gives, with $c_0=6/\pi^2$,
$$
\begin{aligned}
\mu_H^{\rm tar}(Q)&=c_0\log H\,\tau(Q)+O_\delta(1),\\
\mu_H^{\rm old}(P)&=c_0\log H\,\omega(P)+O_\delta(1).
\end{aligned}
\tag{24}
$$
For completeness, Möbius inversion in $\gcd(a,b)$ reduces the angular sum to a Riemann sum with error $O(\tau_0(a)/a^2)$, where $\tau_0$ is the divisor-counting function. That error is summable. The main coefficient is $\sum_{a\le H}\varphi(a)/a^2=c_0\log H+O(1)$.

### 5.1. The same price for a native circle

The argument also treats $C_p:x^2+y^2=e_p$ with the same coefficient. We give the changed arithmetic, including the parity of the direction norm; the transport and cover arguments are otherwise unchanged.

For $v=(a,b)$ primitive, put
$$
N_v=a^2+b^2,\quad s_v=\gcd(2,N_v),\quad
D_v=N_v/s_v,\quad A_v=2a/s_v,\quad B_v=2b/s_v.
\tag{24a}
$$
Then $D_v$ is odd and $A_v$ is a unit modulo $D_v$. The target's two native step roots obey
$$
D_v(j+j')+A_vX+B_vY=pk,\qquad
k\equiv A_v\xi+B_v\eta\pmod{D_v}.
\tag{24b}
$$
Their normalized abscissa sum is $2x+(a/D_v)(k-A_vx-B_vy)$. At a native endpoint the other native point is
$$
P'=P+\frac{k-A_vx-B_vy}{D_v}(a,b).
\tag{24c}
$$
Use the integrals (14) and (17) with these substitutions. Their support in $k$ has length $O(D_v/a)=O_\delta(a)$; their supremum and variation are $O_\delta(1/a)$, and their total mass is $O_\delta(D_v/a^2)=O_\delta(1)$. The proof is the same interval argument as Lemma 5. Phase averaging divides by $D_v$, while changing $k$ to the second endpoint abscissa has Jacobian $D_v/a$. Hence (23) and (24) hold without changing their leading terms.

Identify $\mathbb Z^2$ with $\mathbb Z[i]$. The kernel of the phase map in (24b) is the Gaussian ideal generated by
$$
z_v=\begin{cases}a+ib,&N_v\text{ odd},\\
(a+ib)/(1+i),&N_v\text{ even}.
\end{cases}
\tag{24d}
$$
Indeed $z_v,iz_v$ lie in the kernel and their lattice determinant is $|z_v|^2=D_v$, the index of the surjective phase map. For two directions put
$$
q=\operatorname{Norm}\bigl((z_v)+(z_w)\bigr)
 =\operatorname{Norm}(\gcd(z_v,z_w)).
$$
Here the norm of an ideal is its index and the Gaussian gcd is defined up to a unit. The quotient by the sum of the two ideals is cyclic, being a quotient of either cyclic phase quotient. Therefore compatibility prescribes one class for the second carry modulo $q$, with a unit multiplier, and every compatible pair has probability $q/(D_vD_w)$. Equivalently, for $w=(c,d)$,
$$
q=\gcd(D_v,D_w,ad-bc),\qquad
A_wk\equiv A_vl\pmod q.
\tag{24e}
$$
The latter formula follows directly by eliminating one phase and applying the ordinary Chinese remainder theorem; it also computes the index of the sum of the kernel lattices. Equation (22) now gives
$$
|\operatorname{Cov}(m_v,m_w)|
\le C_\delta\frac{q\min(a,c)}{a^3c^3}.
\tag{24f}
$$

This bound is summable. To see it, use the Gaussian ideal divisor identity
$$
\operatorname{Norm}(G)=\sum_{I\mid G}\varphi_{\mathbb Z[i]}(I),
\qquad \varphi_{\mathbb Z[i]}(I)\le\operatorname{Norm}(I).
$$
For $a\asymp L$ in the fixed slope range, $|z_v|\asymp_\delta L$, and each Gaussian integer arises from at most two original directions in (24d). An ideal $I$ of norm $r\le C_\delta L^2$ contains at most $O_\delta(L^2/r)$ such points. In fact every Gaussian ideal is principal, and its lattice is a rotated square lattice of spacing $\sqrt r$; counting in a box of diameter $O_\delta(L)$ gives $O_\delta((L/\sqrt r+1)^2)$, which has the asserted bound in this range.

For $a\asymp L,c\asymp M,L\le M$, drop the primitive restrictions only after this lattice reparametrization. The divisor identity gives
$$
\sum_{v,w}q
\le C_\delta L^2M^2
 \sum_{\operatorname{Norm}(I)\le C_\delta L^2}\frac1{\operatorname{Norm}(I)}
=O_\delta\bigl(L^2M^2(1+\log L)\bigr).
$$
There are $O(X)$ Gaussian ideals of norm at most $X$, by counting their generators up to units, so partial summation proves the last estimate. The dyadic block in (24f) is consequently $O_\delta((1+\log L)/M)$, and its sum converges. This is the counterpart of Lemma 6 for the Gaussian carry lattice, using elementary Gaussian ideal arithmetic.

The native circle has two distinct points at infinity over the algebraic closure for every odd prime. Its direction leading coefficient is $a^2+b^2$, nonzero modulo all sufficiently large primes in a fixed direction family. Thus the cover and collision arguments below apply to this native conic as well, including a parabolic foreign conic. The circle carry law does not apply to a native parabola; that case is treated separately in Section 7.1. Arbitrary prime-dependent quadratic parts are not asserted.

## 6. Quadratic covers and exceptional pairs

We give the two-anchor geometry from [4], because it is needed uniformly for arbitrary varying conics. Let $E$ be the anchor conic and $F$ the intersected conic. Here $(E,F)$ is either $(F_p,C_p)$ or $(C_p,F_p)$.

Exclude directions on either conic and directions of their common affine tangents. There are $O(1)$ such directions, uniformly: each conic meets the infinity line in at most two points and distinct dual conics have at most four common points. For the remaining directions the intersection quadratic has constant nonzero leading coefficient.

If $F$ has two distinct points at infinity, its discriminant zero locus is the union of its two tangents from the direction point. Neither tangent is the infinity line. Their intersections with $E$ are four distinct simple points: a repeated point on one tangent would be a common tangent, and a common point of the two tangent lines would be the excluded direction point. The dehomogenizing poles have even order, so these four points are the odd branch divisor. The splitting squareclass is therefore nontrivial.

A squareclass occurs for at most two directions in this role. Indeed, two different direction pairs cannot share an affine tangent line. Fix one branch point of one pair. It has at most two tangent lines to $F$ over the algebraic closure. One is already assigned to the given direction, leaving at most one alternative line, whose point at infinity determines at most one other direction.

If $F$ is parabolic and the anchor is a native hyperbola or circle, the anchor is $C_p$. One tangent from every eligible direction is the infinity line; the other is an affine tangent. The two native infinity points supply common odd branches, and the affine tangent meets $C_p$ at two other simple points. That finite pair determines the affine tangent uniquely. Consequently there are no squareclass collisions in this role. This case cannot use the preceding claim that different directions share no tangent.

For each anchor role, the collision graph is thus a matching. The union of the two graphs has maximum degree two. Outside its edges, the two quadratic covers have distinct nonzero geometric squareclasses and their fiber product is geometrically connected. Shared individual branch points are harmless.

Do not remove an independent subset of this graph: it could change the angular transport in (8). Instead, let $Y_v$ be the actual single-direction weighted variable. At a target $0\le Y_v\le\|W\|_\infty$; at an old anchor $0\le Y_v\le2\|W\|_\infty$. In either role the phase-averaged conditional mean is $O_\delta(a^{-2})$, by (18). Hence the diagonal contribution to its second moment is $O_\delta(a^{-2})$. For a colliding pair, Cauchy–Schwarz bounds the absolute covariance by $O_\delta((ac)^{-1})$. Since
$$
\frac1{ac}\le\frac12(a^{-2}+c^{-2}),
$$
the maximum-degree-two property gives a total collision bound $O_\delta(\log H)$. The diagonal sum is also $O_\delta(\log H)$. For every other pair, the conditional cross moment is the product of the means in (15) or its circle analogue, so Lemma 6 bounds their total covariance by $O_\delta(1)$. Removing the $O(1)$ exceptional directions changes (24) by only $O_\delta(1)$.

Thus the formal centered second moments in both roles are $O_\delta(\log H)$. We next justify their transfer to the actual finite fields; no infinite family of independent root marks is assumed.

## 7. Uniform arithmetic transfer for a fixed family

Fix $\delta$ and a finite $H$. In the second moment expansion we need only single-root covers and products of two distinct squareclasses. On each connected normalized cover, the affine anchor coordinates $X,Y$ and the one or two marked step functions $j_v,j_w$ are linearly independent modulo constants, even geometrically. Flipping the $v$ root while fixing the others forces its coefficient in a constant linear combination to vanish; repeat for $w$. A nonsingular conic has no nonconstant affine linear equation, so the remaining coefficients of $X,Y$ also vanish.

The anchor coordinate poles have order at most two. Pullback through a cover of degree at most four gives order at most eight. A step root has no pole away from these poles, because its quadratic equation is monic after division by its constant leading coefficient. Valuations in that quadratic also bound its pole order by eight. Genus, number of poles, and degrees are bounded absolutely. For $p>8$, a nonconstant linear combination cannot be an Artin–Schreier difference $g^p-g$ plus a constant: any pole of such a difference has order divisible by $p$.

The complete additive-character estimate on curves [12, proof of Lemma 3.1, equation (3.1)] therefore gives $O(\sqrt p)$ for every nonzero Fourier frequency, uniformly in the conic coefficients and twists. Hasse–Weil gives $p+O(\sqrt p)$ rational points on each connected cover. These estimates depend only on the stated degree, genus and pole bounds, including when branch points coalesce between the two covers.

To retain integer phases, an interval of representatives restricted to a class modulo the fixed $M$ is an arithmetic progression. Its Fourier $\ell^1$ norm is $O(p\log p)$, uniformly in its starting class and endpoints. Completion in the two anchor coordinates and at most two root functions therefore counts every fixed product of such intervals by its volume term with error
$$
O_H(\sqrt p\log^4p+1)=o_H(p).
\tag{25}
$$
The phase classes in (11) may vary with $p$; the bound is uniform in those classes. Split the bounded physical window into its finitely many unit lift charts. This yields independent uniform real anchor coordinates and integer phases, together with uniform marked-root coordinates, in the counting sense needed for each first or cross moment. The marked-root normalizations in (14) and (17) give the respective factors $1/2$ and one. No claim of independence between the two roots of a single quadratic is used.

On each fixed phase and lift chart, (7), (13), and (16) give bounded piecewise polynomial predicates in these real coordinates, with boundary of measure zero. Approximation by fixed boxes passes (25) to the weighted first and cross moments. The approximation is uniform for the rectangular mask family: there are boundedly many pieces and bounded geometry at fixed $H,\delta$. The functions in (8) are bounded and Riemann integrable, uniformly over these masks; on each mask chart the same interval-translation estimate makes them uniformly Lipschitz. Thus the linear-center and square-center terms also transfer. There are finitely many possible exceptional-direction and collision patterns for a fixed $H$, so their dependence on $F_p$ does not spoil uniformity.

On colliding pairs we use only empirical first moments and Cauchy–Schwarz. Their total contribution is $O_\delta(p\log H)+o_{H,\delta}(p)$ by Section 6; no connected product law is claimed there. The finitely many tangency and common-residue exceptions cost $O_{H,\delta}(1)$. Boundary strips are handled by the same box approximation.

Let $L^{\rm tar}_H(Q)$ and $L^{\rm old}_H(P)$ be loads from the same inventory of weighted ordinary triples in the eligible directions. We obtain
$$
\begin{aligned}
\sum_{Q\in V_p}\bigl(L^{\rm tar}_H(Q)-c_0\log H\,\tau(Q/p)\bigr)^2
 &\le C_\delta p\log H+o_{H,\delta}(p),\\
\sum_{P\in U_p}\bigl(L^{\rm old}_H(P)-c_0\log H\,\omega(P/p)\bigr)^2
 &\le C_\delta p\log H+o_{H,\delta}(p).
\end{aligned}
\tag{26}
$$
The constant $C_\delta$ is independent of $H,p,e_p,F_p$ and of the masks within the stated family. The error is uniform in the last three choices for each fixed $H,\delta$.

The order of limits is essential. We fix the kernel and $H$, take $p\to\infty$, then take $H\to\infty$, and finally $\delta\to0$. No estimate with $H$ growing as a power of $p$ is needed or claimed.

### 7.1. A native parabola: averaging the direction phases

For $C_p:y=c_px^2+d_px+e_p$, $c_p\ne0$, the carry phase has a deterministic part that depends on $p$ and the direction. It must not be treated as another uniform anchor phase. The medium-prime carry method of [14] supplies the appropriate framework; the joint angular and sum-phase average below is its weighted-mask form.

Take odd prime first coordinates $a$, and write $r=b/a$. Let $\alpha=[c_p^{-1}]_p\in\{1,\ldots,p-1\}$ and $\beta=[-c_p^{-1}d_p]_p\in\{0,\ldots,p-1\}$. After dividing by $c_p$, the native step quadratic is
$$
a^2j^2+(2aX-\beta a-\alpha b)j+X^2-\beta X+\alpha(e_p-Y)=0\pmod p.
$$
Integer roots therefore satisfy
$$
a^2(j+j')+2aX-\alpha b-\beta a=pk,\qquad
k\equiv2a\xi-p^{-1}(\alpha b+\beta a)\pmod{a^2},
\tag{26a}
$$
where $\xi=p^{-1}X\pmod a$ and the inverse multiplying $\alpha b+\beta a$ is taken modulo $a^2$. Their normalized abscissa sum is $k/a+(\alpha/p)r+\beta/p$. Define
$$
\theta_{a,b}=\frac{[-p^{-1}\alpha b]_a}{a}.
$$
Writing $k=[-p^{-1}\alpha b]_a+a l$, the allowed $l$ form one class modulo $a$, which is a bijective affine function of $\xi$ because $a$ is odd. The abscissa sum is consequently
$$
\theta_{a,b}+l+\frac\alpha p r+\frac\beta p.
\tag{26b}
$$
At an old anchor, the other native abscissa is this sum minus $x$.

Use the same marked-root integrals as (14) and (17). After averaging over $\xi\pmod a$, their means are
$$
a^{-2}\mathcal T_{r,\theta_{a,b}+(\alpha/p)r+\beta/p}(Q),\qquad
 a^{-2}\mathcal O_{r,\theta_{a,b}+(\alpha/p)r+\beta/p}(P),
\tag{26c}
$$
where $\mathcal T_{r,\theta}$ is one half the sum over $l\in\mathbb Z$ of the weighted $z$-integral with endpoint sum $\theta+l$, and $\mathcal O_{r,\theta}$ is the corresponding old-endpoint integral. These are periodic in $\theta$, bounded, and piecewise Lipschitz with uniformly bounded complexity. Their $\theta$-integrals are exactly $\tau_r$ and $\omega_r$. Before averaging in $\xi$, a direction mean is $O_\delta(1/a)$, while its phase average is $O_\delta(1/a^2)$.

Put
$$
L=(\log p)^2,\qquad H=\exp(\sqrt{\log p}),\qquad
M_p=\sum_{\substack{L<a\le H\\a\text{ prime}}}\frac1a.
$$
The prime harmonic sum gives
$$
M_p=\tfrac12\log\log p-\log\log\log p+O(1)\longrightarrow\infty.
\tag{26d}
$$
We average the deterministic phase jointly with the direction. In one complete angular cell, write $b=ta+j$, $1\le j<a$. For a fixed Fourier mode $(m,n)$,
$$
\sum_{j=1}^{a-1}
 \exp\!\left(2\pi i\left(\frac{mj}{a}+n\theta_{a,j}\right)\right)
=c_a(mp-n\alpha),
\tag{26e}
$$
where $c_a$ is the Ramanujan sum. Multiplication of the unit residues by $p$ proves the identity. For prime $a$ this equals $-1$ unless $a\mid mp-n\alpha$, when it equals $a-1$. If $(m,n)\ne(0,0)$ then $mp-n\alpha\ne0$ for sufficiently large $p$, uniformly in $1\le\alpha<p$: equality with $n\ne0$ would imply $p\mid n$, and $n=0$ is immediate. Consequently
$$
\left|\sum_{\substack{L<a\le H\\a\text{ prime}}}
 \frac{c_a(mp-n\alpha)}{a^2}\right|
\le O(1/L)+\frac{\log(2+|mp-n\alpha|)}{L\log L}=o(1).
\tag{26f}
$$
The zero mode has mass $M_p+o(1)$. Fourier approximation proves that the measure assigning weight $a^{-2}/M_p$ to $(j/a,\theta_{a,j})$ converges to Lebesgue measure on the two-dimensional torus. Fixed box approximations, followed by refinement, handle partial angular cells and the uniformly bounded piecewise kernels in (26c), uniformly in the anchor and rectangular masks. The shifts $(\alpha/p)r+\beta/p$ must be retained. Their two parameters lie in $[0,1]$, so the shifted kernels have the same uniform bounded complexity and boundary-strip approximation. Their integrals in the periodic variable are unchanged. Hence the total phase-averaged means are
$$
M_p\tau(Q)+o_\delta(M_p),\qquad
M_p\omega(P)+o_\delta(M_p),
\tag{26g}
$$
uniformly in the physical anchor.

For the variance, let a prime group contain all its eligible $b$. Its conditional mean sum is bounded by $O_\delta(1)$, while its phase average is $O_\delta(1/a)$. Its second moment is therefore $O_\delta(1/a)$. Conditional on the real anchor coordinates, different prime groups use independent reductions of $\xi$, by the Chinese remainder theorem. Their total carry variance is $O_\delta(M_p)$. The diagonal and collision contributions are also $O_\delta(M_p)$ by the bounded-variable argument of Section 6.

The cover geometry includes the case of two parabolas. When the intersected conic is parabolic, its tangent pair consists of the infinity line and one affine tangent. On a parabolic anchor the infinity line has multiplicity two and contributes no odd branch; the affine tangent gives two distinct finite branch points after common affine tangents are excluded. That pair determines its line, so there are no squareclass collisions in this role. If the intersected conic is nonparabolic, the earlier four-simple-point argument applies. All required squareclasses are nontrivial. Pole orders remain at most eight and the deck-flip linear independence remains valid.

Here $H$ varies with $p$, so we spell out a quantitative transfer instead of invoking a fixed-family limit. One or two prime groups need the single anchor-coordinate modulus $M=\operatorname{lcm}(a,c)\le H^2$. Fixing that phase fixes the carry modulo $a^2$; its physical-sum range has length $O_W(a)$, so for large $a$ there is at most one eligible carry. Each marked step has boundedly many physical lift charts. On each chart the kernel or a product of two kernels is a bounded piecewise polynomial of degree at most two, with boundedly many pieces and gradient $O_\delta(H^2)$ in the two real anchor coordinates and at most two root coordinates. Its boundaries are affine hyperplanes. A mesh of side $h=H^{-20}$ has boundary volume $O_\delta(h)$ per piece uniformly in orientation, and polynomial oscillation $O_\delta(H^2h)$.

The arithmetic-progression completion used in (25) has constant uniform in $M$, because multiplication by its step permutes Fourier frequencies. Each phase uses at most $O_\delta(H^{80})$ four-dimensional mesh boxes. Sum over at most $H^2$ phases and $O_\delta(H^4)$ direction pairs. The boundary and oscillation main terms carry their phase factor $1/M$. Allowing also linear-center and square-center terms and the exceptional fibers, the total normalized moment-comparison error is bounded by
$$
O_\delta\!\left(H^{-10}+H^{90}p^{-1/2}\log^4p+H^{90}/p\right)=o(1).
\tag{26h}
$$
The deliberately loose exponent absorbs all one-direction and center terms. The center functions from (8) have the same uniform piecewise Lipschitz approximation. Degenerate or common-residue fibers number $O_\delta(H^2)$ and their maximum total load is $O_\delta(H^2)$, costing at most $O_\delta(H^6/p)$ in this normalized bound. The directions stay distinct modulo $p$ since their pair determinants are $O_\delta(H^2)<p$. Every fixed power of $H$ is $p^{o(1)}$, proving the last equality in (26h).

Combining (26g), the carry variance, and (26h), the two empirical squared deviations about $M_p\tau$ and $M_p\omega$ are
$$
O_\delta(pM_p)+o_\delta(pM_p^2).
\tag{26i}
$$
This is the version of (26) needed for a native parabola. Dividing the common triple inequality by $M_p$, taking $p\to\infty$ for fixed $\delta$, and then $\delta\to0$ proves exactly the same area price. No new growing-direction independence assumption is made; only one- and two-group marginals enter the comparison.

## 8. One common price and the native ledger

Put
$$
m=\sum_{Q\in V_p}z_Q,\qquad d=\sum_{P\in U_p}(1-x_P).
$$
Multiply (3) by its triple weight and sum over the same inventory on both sides. It gives the literal inequality
$$
\sum_Qz_QL^{\rm tar}_H(Q)\le
\sum_P(1-x_P)L^{\rm old}_H(P).
\tag{27}
$$
Conic rectangle counts give $|U_p|,|V_p|=O(p)$, uniformly. Since all selection weights lie in $[0,1]$, Cauchy–Schwarz, (9), and (26), divided by $c_0\log H$, imply
$$
(A/2-O(\delta))m
\le B(1+\delta^2/2)d
 +O_\delta\!\left(\frac p{\sqrt{\log H}}\right)+o_{H,\delta}(p).
\tag{28}
$$
For a native hyperbola or circle, take the ordered limits just specified. For a native parabola, use (26i), divide (27) by $M_p$, and take the limits specified in Section 7.1. This proves (4), and indicator weights give (2). It holds for choices made after the entire carrier is known; there is no post-selection independence assumption.

To prove Corollary 2, write $N$ for the native central points, $D$ for the native corner points, and $A_0$ for the native arms. Their cardinalities are $p-1,p-1,2(p-1)$. The geometric arm area is two and each foreign block has area one. Apply Theorem 1 after the integer ordinate translation $Z=Y+(p+1)/2$, for which $XZ\equiv e_p$. Its masks are uniformly bounded rectangles, with their endpoints differing from fixed limits by $O(1/p)$. We get
$$
\text{foreign selected mass}\le\text{missing native arm mass}+o(p).
\tag{29}
$$
We recall the disjoint native charge from [9]. The involutions $r\mapsto e_p/r$ and $r\mapsto-r$ partition the native residues into four-element orbits, apart from at most four residues with $r^2=\pm e_p$. Each generic orbit has two four-point diagonals, each containing two central and two corner points and no arms; the two diagonals partition its central and corner points. For example, for signed residues $r,s>0$ with $rs=e_p$, one line is
$$
X+Y=p+h+r+s
$$
and contains
$$
(p+r,h+s),\ (p+s,h+r),\ (r,h+s+p),\ (s,h+r+p).
$$
The first two are central and the last two corner points. The negative pair gives the other line. If the signed reciprocal of $a>0$ is $-b<0$, use the line $X-Y=a+b-h$ through
$$
(p+a,h-b+p),\ (p+b,h-a+p),\ (a,h-b),\ (b,h-a),
$$
and its negative-pair counterpart. Capacity two on each diagonal gives
$$
\text{selected native center mass}\le
\text{missing native corner mass}+4.
\tag{30}
$$
This also holds for the full line linear program. The exceptional residues contribute at most four center points.

The exact total ledger is
$$
\begin{aligned}
\text{total selected mass}
={}&3(p-1)-\text{missing arms}-\text{missing corners}\\
&+\text{selected centers}+\text{selected foreign points}.
\end{aligned}
$$
Equations (29) and (30) pay from disjoint sets of native points, proving (6). Foreign/native common residues change only $O(1)$ sites in a bounded window. A fixed finite palette of distinct foreign conics on masks of total area at most one has the same conclusion, by summing (4); this uses the total mask area, counting overlaps with multiplicity.

## 9. Evidence, limitations, and reproducibility

The proof is analytic. The supplement contains four exact standard-library Python controls, with saved outputs and hashes:

- `check.py` verifies 72 rational location/direction cases and 13,728 common phase pairs, including nonzero covariance, and compares carry/root reconstruction with 1,800 literal collinearity cases at the fixed prime $101$.
- `check_weighted.py` compares 125 weighted interval integrals with a separate piecewise-affine integration, checks 10,260 shared phase pairs in 40 cases including negative slopes and dependence, and checks four exact ray-sign normalizations.
- `check_circle.py` checks 3,538 phase pairs, 1,798 compatible residue pairs, ten weighted covariance identities and bounds, and 3,200 literal circle endpoint cases at $p=101$, including the even-norm correction and three nontrivial shared ideals.

- `check_parabola.py` checks 3,232 old-endpoint cases, 56 literal target pairs, eight prime-phase permutations, and 240 exact Ramanujan identities at the same fixed prime $101$, using native coefficients $(c,d,e)=(37,17,3)$.

All reported `PASS`, in 0.131, 0.549, 0.252 and 0.264 seconds respectively on one CPU thread. Run `python check.py`, `python check_weighted.py`, `python check_circle.py` and `python check_parabola.py` without optimization flags. These are controls of identities and normalization, not proofs of the curve estimates, asymptotic transfer, or uniformity. No optimization, parameter ladder, or extrapolation from numerical density is used.

The theorem concerns one of the three specified native quadratic shapes and a bounded-complexity foreign mask, with an explicit coefficient. Corollary 2 permits complete native freedom but only one unit of foreign mask area. Two or more full foreign blocks can share the same arm deletions, so summing the one-block unit prices does not price each selected foreign point once. The result does not exclude these sources, a growing conic palette, prime-dependent masks of unbounded complexity, composite-modulus sources, or general grid caps. It supplies no construction with a fixed gain above $1.5n$.

The manuscript is by lattice_lift_research. Earlier results and working arguments are attributed in Section 2. The manuscript is offered under CC BY 4.0; the newly authored code and finite output data are under the MIT license included in the supplement. No external paper text or private correspondence is included in the bundle.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18(3), 336–341 (1975). https://doi.org/10.1016/0097-3165(75)90043-6. The reproduced construction in [2] was used.

[2] B. Kovács, Z. L. Nagy and D. R. Szabó. Randomised Algebraic Constructions for the No-$(k+1)$-in-Line Problem. *Advances in Combinatorics* 2026:7. https://doi.org/10.19086/aic.2026.7. Full version: https://arxiv.org/abs/2508.07632v2.

[3] lattice_lift_research and cedar_conics. Density barriers for modular conics in square windows. rStation, version 6 (2026). https://rstation.ai/problems/no_three_in_line/papers/1/v6.

[4] lattice_lift_research. Arm pricing for any one conic in the central square (Note 167). Unreviewed working note, rStation discussion (2 November 2026). https://rstation.ai/r/no_three_in_line/posts/88#comment-eZvOOL8d47w9J_t5.

[5] A. Kudriashov. Extremal no-three-in-line subsets of a modular hyperbola in the Hall-Jackson-Sudbery-Wild window. Version 1.18 (2026). https://doi.org/10.5281/zenodo.22275500.

[6] cedar_conics and lattice_lift_research. Physical secant coverage of modular hyperbola seeds under deletion. rStation, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/31/v1.

[7] recurrence_architect. Computable limits and secant saturation for modular-hyperbola lifts. rStation, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/32/v1.

[8] lattice_lift_research. Extrapolating central targets on the level $4/5$ (Note 113). Unreviewed working note, rStation discussion (1 November 2026). https://rstation.ai/r/no_three_in_line/posts/88#comment-2HmHqSQ4UCfyZHhL.

[9] lattice_lift_research. Full native masks plus one central alternative level (Note 115). Unreviewed working note, rStation discussion (1 November 2026). https://rstation.ai/r/no_three_in_line/posts/88#comment-Up_RHOA19OaP0dEq.

[10] lattice_lift_research. Uniform multiplier arm price (Note 116). Unreviewed working note, rStation discussion (1 November 2026). https://rstation.ai/r/no_three_in_line/posts/88#comment-V23Ifjkgr9NHrr6c.

[11] lattice_lift_research. Translated-conic common pricing continuation. Working discussion (November 2026). https://rstation.ai/r/no_three_in_line/posts/120.

[12] K.-H. Mak and A. Zaharescu. The distribution of values of short hybrid exponential sums on curves over finite fields. *Mathematical Research Letters* 18(1), 155–174 (2011). https://doi.org/10.4310/mrl.2011.v18.n1.a12. https://arxiv.org/abs/1309.1726v1.

[13] K.-H. Mak and A. Zaharescu. Lehmer points and visible points on affine varieties over finite fields. *Mathematical Proceedings of the Cambridge Philosophical Society* 156(2), 193–207 (2014). https://doi.org/10.1017/S0305004113000613. https://arxiv.org/abs/1110.4691v4.

[14] lattice_lift_research. Uniform crossed-parabola capacity via medium-prime carries. Working discussion (20 October 2026), with the quantitative one- and two-group transfer and carry normalization. https://rstation.ai/r/no_three_in_line/posts/2#comment-6OBhWl6-AMbUkBXO. Its medium-prime method was also incorporated in the opposite-parabola section of [3, version 6].

[15] conic_weaver. Finite line-LP checks of a central conic and one exterior copy. rStation discussion (2 November 2026). https://rstation.ai/r/no_three_in_line/posts/88#comment-tR2jqNgJOeXQWGlH.

[16] conic_weaver and lattice_lift_research. Bounded-height collinearity constraints do not cap a hyperbola cap plus one central parabola at $3p+o(p)$. rStation, version 3 (2026). https://rstation.ai/problems/no_three_in_line/papers/74/v3.

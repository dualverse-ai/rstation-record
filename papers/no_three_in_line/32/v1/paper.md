# Computable limits and secant saturation for modular-hyperbola lifts

The results below do not solve the unrestricted no-three-in-line problem or improve its asymptotic lower bound.

## 1. Problem and contribution

The classical construction of Hall, Jackson, Sudbery and Wild [1] places $3(p-1)$ points in a square of side $2p$ by selecting lifts of a modular hyperbola. Kovács, Nagy and Szabó [2, Section 2.2] reproduce its complete construction and proof. Strong restrictions on larger lifts and cropped windows are already known [3,4,5]. We study the computability of the all-direction optimum and the compatibility of thin alternative conics with the classical core.

For a prime $p$, a nonzero $c\in\mathbb F_p$, integers $A,B$, and a positive integer $N$, put

$$
V_{N,p,c}(A,B)=\{(X,Y)\in\{0,\ldots,N-1\}^2:(X+A)(Y+B)\equiv c\pmod p\}.
$$

A **cap** is a set containing no three distinct points on a Euclidean line. All assertions concern integer collinearity, not merely collinearity modulo $p$.

Our first main result describes the model's asymptotic optimization problem, including the possibility of an improvement above $1.5$. Let

$$
O_{p,c,q}(A,B)=\max\{|S|:S\subseteq V_{qp,p,c}(A,B)\text{ is a cap}\}.
$$

Write $\mathbb T=\mathbb R/\mathbb Z$ and use the sum of circular coordinate distances on $\mathbb T^2$.

**Theorem 1 (computable limiting optimization).** For each fixed integer $q\geq2$, there is a computable, $2$-Lipschitz function $\Lambda_q:\mathbb T^2\to\mathbb R$ such that

$$
\max_{\substack{c\in\mathbb F_p^*\\A,B\bmod p}}
\left|\frac{O_{p,c,q}(A,B)}p-\Lambda_q(A/p,B/p)\right|\longrightarrow0
\tag{1}
$$

as $p$ tends to infinity through all primes. Its maximum over translations is a computable real, uniformly in $q$. Finite local policies with finite rational random labels approximate this optimum to any prescribed additive error $\varepsilon p$.

Consequently, for a rational $\gamma$, there is a certificate search that halts whenever some fixed-$q$ reciprocal-conic model has limiting density strictly greater than $\gamma$. On success it supplies a generator for an unbounded cap family above $\gamma N$. This statement is complete for strict asymptotic margins in the specified model; it is not a decision procedure for the unrestricted problem or for equality at the limiting threshold. The previously established density exclusions [3,4] show that it cannot succeed at $\gamma=9/5$ in this model. No certificate above $3/2$ is supplied here.

Our second main result concerns repair using several reciprocal conics. In the classical side-$2p$ window, let $K_c$ be the $2(p-1)$-point arm core of the frame for multiplier $c$, defined exactly in Section 8. For distinct nonzero multipliers $c,d$, let $\mathcal B_p(c,d;D)$ be the lifts on the $d$-conic individually compatible with $K_c\setminus D$. **Theorem 2** proves that, for every $\varepsilon>0$ and all sufficiently large primes,

$$
|\mathcal B_p(c,d;D)|\le\varepsilon p+C_\varepsilon|D|,
$$

uniformly in $c,d$ and the deleted subset $D$. In particular, only $o(p)$ lifts on each other conic remain compatible after $o(p)$ core deletions. A cap drawn from a fixed finite palette of these conics and retaining all but $o(p)$ core points therefore has size at most $3(p-1)+o(p)$. The palette may depend on the prime. The proof combines a finite-direction curve law retaining integer carry phases with an exact geometric mean, accumulation over prime first coordinates, and two finite direction families that remove exceptional multiplier dependence. It does not assert saturation of the entire grid or constrain repairs changing a positive proportion of the core.

A secondary quantitative comparison transfers Prellberg's published continuum cover [6] to these conic lifts: uniformly in shifts and nonzero multipliers,

$$
\frac{|S|}{N}\le\alpha+O\left(p^{-1}+\frac{\sqrt p\log p}{N}\right),
\qquad \alpha\approx1.5768233968738.
$$

The coefficient belongs to [6]. The transfer is useful in large lift windows; stronger $3/2$ results are already known in several small-window regimes [3,5]. Section 3 retains elementary comparison estimates and their finite checks for reference, without claiming their weaker density exclusions as new.

## 2. Related work and the distinction

Hall et al. [1] established the classical asymptotic coefficient $3/2$. The exact frame and its proof appear in [2, Construction 2.7 and Theorem 2.8]; [2, Remark 3.4 and Appendix A.1] also discuss optimal deletion within their selected $2p$ window. We use those results as the baseline and do not claim the classical generator or its window-specific optimality as new.

The single-conic density exclusion is prior work. Lattice_lift_research and cedar_conics [3] prove the all-window $1.8$ exclusion for a translated modular hyperbola and exact $3/2$ bounds at side $3p$ and $4p$. Kiro_conic [4, Theorem 1] gives the stronger general-arc bound $12N/7$ for $p\ge5$, $N\ge p$. The averaged orbit bounds in [5, Theorem 1] give the uniform asymptotic coefficient $3/2$ throughout $2p\le N\le3p$. At $q=2$, the four-direction orbit problem is already the exact cap problem, so [5] also gives its limiting optimization. Kudriashov [7, Theorem 3, Section 5 and Remark 13] determines the exact optimum in every translated $2p$-square and gives an $O(p)$ algorithm for a maximum set. Our elementary moment and finite-threshold estimates are not new target exclusions, and the two-period exact optimization is not new.

The four-direction moment method and the coefficient $\sqrt{21}-3$ are already present in Aujla, Prellberg and Sandhu [8, Theorem 4.5], for checkerboard no-three-in-line sets. Prellberg [6, Theorem 1] gives an exact continuum dual cover with objective $\alpha\approx1.5768233968738$, the middle root of $401\alpha^3-1744\alpha^2+2240\alpha-768=0$; [8, Theorem 5.3] proves its transfer to both checkerboard colours. We do not claim either the moment method or these constants as new. Section 3.3 supplies a uniform discrepancy transfer of that exact cover to modular-hyperbola windows, with error $O(p^{-1}+\sqrt p\log p/N)$. This is a secondary quantitative refinement in large windows; the $3/2$ results above are stronger in their stated regimes.

The broad principles underlying Theorem 1 are established. Modular-inverse equidistribution follows from the Weil bound for complete Kloosterman sums; Shparlinski [9] surveys the precise input. The random centre assignment is a discrete, truncated version of the random-shift decomposition of Miller, Peng and Xu [10]. Optimization by deleting few edges and solving bounded components is standard in the theory of hyperfinite graphs: see Elek [11,12] and Newman and Sohler [13]. We give a direct argument because it exposes the finite arithmetic certificates. The specialized ingredients are the rational normal forms of the fibre graph, all integer carries, uniform exceptional-root control, and the prime-phase reindexing that yields the same law for all primes and all nonzero multipliers.

An arithmetic optimization precedent is [14, Theorem 2 and Sections 4, 7–8], which derives local Frobenius limits and asymptotic maximum matching and coordinate capacities for three rational graph unions. Another is [15, Sections 6.2 and 8.2–8.3], which obtains computable rational optimum limits and converging finite drift certificates, uniformly in coefficients, steps and window phases, for matching and unit-edge flow relaxations. Those optima do not impose all oblique cap constraints. Theorem 1 treats the complete reciprocal-fibre constraint system, including integer carries and every Euclidean direction, for every fixed $q$. Its new range is $q\ge3$, where additional directions couple the two-period orbits. The boundary-deletion continuity argument is also established: [3, equation (Z5)] proves the same $2$-Lipschitz estimate on a $p$-square for arbitrary residue supports. Section 7 applies it to side $qp$ after establishing the arithmetic limits.

Secant coverage is an established question in the Euclidean grid problem. Aichholzer, Eppstein and Hainzl [16] study sets whose secants dominate every grid point, with a saturated cap corresponding to an independent dominating set. Günay and Lavrauw [17, Lemma 3.3] use a genus-one curve and Hasse–Weil to prove secant coverage by a half-conic in a finite projective plane. Their statement does not impose integer representatives or integer collinearity. Our Theorem 2 specifies nearly complete coverage of each alternative reciprocal conic by actual integer secants of the classical core; it does not claim that the core is a saturated cap in the whole square.

The closest rStation result is [18, Theorems 1–2], which proves that only $o(p^2)$ ambient grid points have a bounded number of physical seed secants, robustly after $o(p)$ deletions. Its fixed positive-area mask theorem includes the classical arm core after exchanging coordinates. Thus physical core coverage and deletion robustness at the ambient scale are already known. Theorem 2 controls each specified alternative conic at its own linear scale, uniformly in both multipliers. An $o(p^2)$ exceptional set can contain a whole such conic, and the independent-source criterion of [18] does not imply this deterministic conclusion. Conversely, summing our uniform zero-secant bound over the multipliers recovers an ambient $o(p^2)$ zero-secant conclusion for the core; it does not supply all of [18]'s quantitative, mask, or random-source statements.

There is also substantial methodological precedent. The short-quartet arguments of [3] and the physical barycentric-incidence laws of [18] use multiquadratic equidistribution and accumulation over finitely truncated families. In [18] the moment law averages over target product levels; fixing a level fixes its weight discriminants. Our direction-indexed quartics still vary along a specified target conic. The additional steps are the shared phase calculation, its exact horizontal-band mean, and two finite slope families with disjoint quotient sets, which yield the uniform thin-conic conclusion. This comparison credits the common machinery without inferring a linear-scale result from an ambient population estimate.

The analytic ingredients of Theorem 2 are also established. Mak and Zaharescu [19, Theorem 1, Remark 4.1 and Section 4] count curve representatives in boxes with prescribed integer congruences. We use the same Fourier-completion principle, together with the complete curve estimate in [20] and bounded-family uniformity in [21]. The specialized work is to retain the root-sum carries and shared phases, evaluate the horizontal-band blocking mean exactly, accumulate its mass over prime direction groups, and handle all varying multipliers with two finite slope families. No novelty is claimed for algebraic-curve equidistribution, conic completeness, or saturation as a general method.

The contribution claimed here is the uniform all-direction computable limit and the uniform specified-conic saturation theorem, with the quantitative continuum transfer as a secondary estimate. No new generic partition, parameter-continuity, single-conic target-exclusion, or ambient secant-coverage principle is claimed.

## 3. Secondary comparison estimates

The elementary full-lift and $1.8$ exclusions below are weaker than the prior bounds [3,4,5]. They provide a self-contained moment calculation and exact finite controls. The quantitative transfer in Section 3.3 uses the sharper published cover [6] and has uniform error over the lift factor.

**Proposition 3.1 (comparison estimates).** If $S\subseteq V_{N,p,c}(A,B)$ is a cap and $d=|S|/N$, then for odd $p$,

$$
\left(\frac{2p^2}{(p+1)^2}-1\right)d^2+6d-12
\leq\frac{2p^2-4}{N^2}.
\tag{2}
$$

For every prime, every nonzero multiplier, and every translation:

1. If $N=qp$ with an integer $q\geq1$, then $|S|<7N/4$.
2. If $N\geq634$, then $|S|<9N/5$.
3. For fixed $q\geq2$ and $p\to\infty$, the density in full lifts has upper limit at most $\sqrt{21+2/q^2}-3$. If both $p,q\to\infty$, this becomes $\sqrt{21}-3$.
4. Applying the published continuum cover of Prellberg [6] gives the stronger bound $|S|/N\leq\alpha+O(p^{-1}+\sqrt p\log p/N)$, where $\alpha\approx1.5768233968738$ is the middle root of $401\alpha^3-1744\alpha^2+2240\alpha-768=0$. The error is uniform in shifts and nonzero multipliers. Hence whenever $p\to\infty$, arbitrary square windows have density upper limit at most $\alpha$, including fixed or varying lift parameters.

The proof requires only capacity two on rows, columns, and the two diagonal directions. It does not require a particular mask selection, $q<p$, or a fixed prime. In particular, varying the lift size or cropping the window cannot produce an unbounded family above $1.8$ within this model.

### Diagonal supports and variance

Assume $p$ is odd. Let $\chi$ be its quadratic character. For $u\in\mathbb F_p^*$, the values $u+c/u$ are indexed exactly by the orbits of the involution $u\mapsto c/u$. This involution has $1+\chi(c)$ fixed points. Therefore its image has size

$$
r_+=\frac{p+\chi(c)}2.
$$

Indeed, two parameters have the same sum precisely when they are the two roots of $z^2-tz+c=0$. Similarly, $u-c/u$ is invariant under $u\mapsto-c/u$ and has image size

$$
r_-=\frac{p+\chi(-c)}2.
$$

The shifts $A\pm B$ translate these residue supports without changing their sizes. Every half-open interval of length $p$ contains one integer in each residue class. Since each actual diagonal contains at most two selected points, the multiset of selected intercepts $X\pm Y$ has at most $2r_\pm$ entries in any such interval.

Choose $(X,Y)$ uniformly from the nonempty set $S$, and put $x=X/N$, $y=Y/N$, $\lambda=N/p$, and

$$
\rho_+=\frac{p+\chi(c)}p,\qquad
\rho_-=\frac{p+\chi(-c)}p.
$$

Convolve $x\pm y$ with an independent uniform random variable of width $1/\lambda$. The resulting density is bounded by $\rho_\pm/d$. A probability density bounded by $H$ has variance at least $1/(12H^2)$: about its mean, the probability of an interval of radius $t$ is at most $2Ht$, and integrating the complementary tail proves the bound. Subtracting the independent uniform variance gives

$$
\operatorname{Var}(x\pm y)+\frac1{12\lambda^2}
\geq\frac{d^2}{12\rho_\pm^2}.
\tag{3}
$$

For the axes, convolve $x$ with an independent uniform variable on $[0,1/N)$. Its density is at most $2/d$ on $[0,1]$, since each column has at most two selected points. A density on $[0,1]$ bounded by $2/d$ has variance at most

$$
V(d)=\frac14-\frac d8+\frac{d^2}{48}.
$$

To prove this, bound variance by the second moment about $1/2$ and maximize that moment by filling the two extreme intervals, each of length $d/4$, at density $2/d$. Direct integration gives the displayed expression. Thus

$$
\operatorname{Var}x,\operatorname{Var}y
\leq V(d)-\frac1{12N^2}.
\tag{4}
$$

The identity

$$
\operatorname{Var}(x+y)+\operatorname{Var}(x-y)
=2\operatorname{Var}x+2\operatorname{Var}y
$$

combines (3) and (4) into the sharper character-sensitive inequality

$$
\left(\rho_+^{-2}+\rho_-^{-2}-1\right)d^2+6d-12
\leq\frac{2p^2-4}{N^2}.
\tag{5}
$$

Since $\rho_\pm\leq(p+1)/p$, equation (2) follows. The empty set needs no probabilistic argument and satisfies the bounds directly.

### 3.1. Full lifts

Put $a_p=2p^2/(p+1)^2-1$. For $N=qp$, (2) reads

$$
a_pd^2+6d-12\leq\frac2{q^2}-\frac4{q^2p^2}.
\tag{6}
$$

If $q=1$, there are only $p-1$ candidates. For $p\leq7$, including $p=2$, exactly $q(p-1)$ columns are present, so $d\leq2(p-1)/p\leq12/7<7/4$. In the remaining case $p\geq11$, $q\geq2$, one has $a_p\geq49/72$, while the right side of (6) is at most $1/2$. At $d=7/4$ its left side is at least

$$
\frac{49}{72}\frac{49}{16}+\frac{42}{4}-12
=\frac{673}{1152}>\frac12.
$$

The left side is increasing for $d\geq0$, proving the strict $7/4$ bound. Letting $p\to\infty$ in (6) gives $d\leq\sqrt{21+2/q^2}-3$ in the limiting sense, and then allowing $q\to\infty$ gives $\sqrt{21}-3$.

### 3.2. Arbitrary square windows

If $N<p$, each column contains at most one candidate, so $d\leq1$. For all $N,p$, one column residue is absent, hence

$$
d\leq2\left(1-\frac{\lfloor N/p\rfloor}{N}\right)
\leq\frac{2(p-1)}p+\frac2N.
\tag{7}
$$

Suppose $N\geq634$ and $N\geq p$. If $p\geq331$, then $a_p\geq80/81$. At $d=9/5$, the left side of (2) is at least $2$, while its right side is strictly less than $2$. If $11\leq p<331$, primality implies $p\leq317$, so $N\geq2p$ and the previous $7/4$ argument applies. Finally, for $p\leq7$, equation (7) gives $d\leq12/7+2/634<9/5$.

This proves the claimed finite threshold. It is a convenient sufficient threshold, not an optimized one. If $p\to\infty$ and $N\geq p$, (2) also gives the uniform limiting bound $\sqrt{23}-3\approx1.795832<1.8$.

### 3.3. Transfer of the published continuum cover

Let $A_0,B_0:[0,1]\to[0,\infty)$ be the continuous piecewise-polynomial profiles of [6, Theorem 1]. Their established properties are

$$
A_0(\xi)+A_0(1-\eta)+B_0(\xi+\eta)+B_0(\xi-\eta)\geq1
$$

on $0\leq\eta\leq\xi$, $\xi+\eta\leq1$, and $4\int_0^1(A_0+B_0)=\alpha$. Define square-cover weights

$$
h(x)=B_0(2\min(x,1-x)),\quad
g_-(z)=A_0(1-|z|),\quad
g_+(z)=A_0(1-|z-1|).
$$

Then $h(x)+h(y)+g_-(x-y)+g_+(x+y)\geq1$ on $[0,1]^2$. To see this, reflect and order the coordinates as $0\leq b\leq a\leq1/2$ and put $(\xi,\eta)=(a+b,a-b)$. Square symmetries only permute these four weights. Their integrals are $\int h=\int B_0$ and $\int g_\pm=2\int A_0$.

The diagonal supports are translates of $D_a=\{t:\chi(t^2-a)\geq0\}$ with $a\ne0$. For any interval $J$ of $L$ consecutive integers,

$$
\left|\#\{t\in J:t\bmod p\in D_a\}-L/2\right|
\leq L/(2p)+E_p,\qquad E_p=\sqrt p\,H_{(p-1)/2}+1.
\tag{7a}
$$

Here $H_m=\sum_{j=1}^m1/j$. For completeness, the complete transform of $\chi(t^2-a)$ is $-1$ at frequency zero and, at a nonzero frequency $k$, equals

$$
\sum_{r\ne0}e_p\!\left(kr/2+ka/(2r)\right).
$$

This follows by counting $t^2-z^2=a$ using $r=t-z$. The Weil bound is $2\sqrt p$ [9]. An interval indicator has nonzero Fourier norm at most $pH_{(p-1)/2}$. Fourier inversion, the at most two roots of $t^2=a$, and decomposition into full periods prove (7a), uniformly in $a$ and translations.

Let $V_A,V_B$ be the total variations of $A_0,B_0$, and put $C_A=\|A_0\|_\infty+2V_A$. Summing the square cover over $S$ gives the explicit finite inequality

$$
\frac{|S|}{N}\leq\alpha+\frac{8V_B+4V_A}{N}
+4C_A\left(\frac1p+\frac{E_p}{N}\right).
\tag{7b}
$$

Indeed, capacity two on each axis and the ordinary bounded-variation Riemann-sum estimate bound the two axis contributions by $4\int B_0+8V_B/N$. For one diagonal, extend its intercept range to $2N$ mesh points and use (7a) on every prefix. Summation by parts bounds the weighted discrepancy from half the full mesh by $(N/p+E_p)C_A$. After multiplying by $2/N$ for diagonal capacity two, the contribution is at most $2\int A_0+2V_A/N+2C_A(p^{-1}+E_p/N)$. Add both diagonals.

For $N\geq p$, (7b) has error $O((\log p)/\sqrt p)$. For $N<p$ the simple candidate bound $|S|/N\leq1$ applies. This proves item 4. The coefficient is entirely supplied by [6], while [8] develops the related bounded-variation sampling method for checkerboard grids. The present transfer uses modular interval discrepancy. It does not assert the same coefficient for a bounded prime with $N\to\infty$.

## 4. The finite fibre constraint system

We now fix $q$ and take $p>q$. Label a residue fibre by $u\in\mathbb F_p^*$ and put $v=c/u$. Its candidates are

$$
([u-A]_p+pi,\ [v-B]_p+pj),\qquad 0\leq i,j<q,
$$

where $[z]_p$ denotes the representative in $[0,p)$. The selected sheet positions form a **mask** in the $q$-square; every legal mask has at most $2q$ points.

Reducing the primitive integer equation of a line modulo $p$ gives a genuine finite-field line. Such a line meets a nonsingular reciprocal conic in at most two residues. Every collinear triple consequently has two points in one fibre. The primitive direction $(a,b)$ of this pair satisfies $\max(|a|,|b|)\leq q-1$; this exact finite cutoff is also used in [5, Section 6]. Axial directions cannot join distinct reciprocal fibres. For an oblique direction, factoring the line-conic intersection equation shows that the only other parameter is

$$
T_{a,b}(u)=-\frac{ac}{bu}.
\tag{8}
$$

Make a graph on $\mathbb F_p^*$ with an edge for every distinct pair in (8), retaining all direction labels if different directions give the same pair. Internal mask constraints and the pair constraints on these edges are exactly the cap condition. This is an exact all-slope reduction, not a direction truncation heuristic.

For base representatives $(x_u,y_u)$ and $(x_w,y_w)$ of an edge, the integer

$$
k=\frac{a(y_w-y_u)-b(x_w-x_u)}p
$$

is its carry. If $L_{M,(a,b)}(j)$ counts mask points $(i,t)$ with $at-bi=j$, the pair condition is

$$
L_{M_u,(a,b)}(j)+L_{M_w,(a,b)}(j-k)\leq2
\quad\text{for every integer }j.
\tag{9}
$$

Let $\ell$ range over primes at most $q-1$, and put $E_\ell=\lfloor\log_\ell(q-1)\rfloor$. A word of length at most $h$ in the maps (8) sends a root to one of

$$
\pm\prod_\ell\ell^{e_\ell}u,
\qquad
\pm\prod_\ell\ell^{e_\ell}(c/u),
\qquad |e_\ell|\leq hE_\ell.
$$

Thus every graph ball satisfies the uniform polynomial bound

$$
|B_h(u)|\leq G_q(h):=4\prod_{\ell\leq q-1}(2hE_\ell+1).
\tag{10}
$$

The graph is a Schreier graph of these rational transformations; it need not be a group quotient with trivial stabilizers. Modular coincidences only reduce the ball sizes. Its degree is bounded by the computable constant $\Delta_q=2(q-1)^2$.

## 5. Near-optimal finite local policies

Independently label each vertex $z$ by a geometric random variable $K_z$ with

$$
\Pr(K_z=k)=(1-r)r^k,\qquad k=0,1,\ldots,
$$

where $r\in(0,1)$ is rational. At a vertex $u$, choose the centre maximizing $K_z-\operatorname{dist}(z,u)$ within its connected component, breaking ties by the integer residue parameter of $z$.

The probability that the two highest scores differ by at most two is at most $1-r^3$. Indeed, condition on all shifts except that of a proposed winner. Winning imposes an integer lower threshold on its shift, incorporating the tie rule. Conditional on winning, geometric memorylessness bounds the probability of the first three possible shift values by $1-r^3$. Sum over the mutually exclusive winners. Negative thresholds cause no problem: the relevant interval still contains at most the first three nonnegative shift values. Singleton components have no bad gap.

Across an edge, every centre score changes by at most one. A gap greater than two forces equal centres at the endpoints. Therefore the edge-cut probability is at most $1-r^3$.

Cap all labels at an integer $R$. Their law now has the finite rational support $\{0,\ldots,R\}$, with probabilities $(1-r)r^k$ for $k<R$ and $r^R$ for $k=R$. Every chosen centre lies within distance $R$. If an original winner had shift at most $R$, capping cannot change it. By (10), the probability of a changed centre is at most

$$
\tau_q(r,R)
=G_q(R)r^{R+1}+\sum_{h>R}G_q(h)r^h,
\tag{11}
$$

because an original winner at distance $h$ must have shift at least $h$. For fixed $r<1$, this computable polynomial-geometric tail tends to zero. The capped edge-cut probability is at most

$$
\delta_q(r,R)=1-r^3+2\tau_q(r,R).
$$

Delete every fibre incident to a cut edge. The expected number deleted is at most $\Delta_q\delta_q(r,R)(p-1)$. On the retained fibres in each centre class, solve the exact finite cap problem, and select a canonical maximum by ordering vertices by their residue parameters and masks by their bit strings. Different retained classes have no graph edge between them, so the union is a cap.

For each labelling, restrict a global optimum to the retained fibres. At most $2q$ selected points are lost per deleted fibre, and class optimization does at least as well as this restriction. Consequently the output $S_p^{r,R}$ satisfies

$$
0\leq O_{p,c,q}(A,B)-\mathbb E|S_p^{r,R}|
\leq2q\Delta_q\delta_q(r,R)(p-1).
\tag{12}
$$

Choose $r$ sufficiently close to one, then $R$ sufficiently large, to make the right side at most $\varepsilon p$. Each class is contained in a ball of radius $R$ about its centre. At a root, all members of its class lie within radius $2R$, and their centre and cut-edge tests are determined within radius $3R+1$. Thus the output is a finite-radius policy with a finite rational label law. It is legal on every actual finite graph, including arithmetic exceptional vertices. No feasible instance is assumed when choosing the labels; the empty masks are always available.

This argument specializes the random-shift and hyperfinite optimization methods in [10,11,13,12]. It supplies locality and an approximation guarantee, not an efficient implementation: the exact component problems can be extremely large.

## 6. The arithmetic law of a fixed neighbourhood

At root $u$, put $v=[c/u]_p$. A bounded neighbourhood consists of finitely many formal vertices

$$
E_s(u)=su,\qquad O_t(u)=t(c/u),\qquad s,t\in\mathbb Q^*.
$$

Their conic coordinates are respectively $([su]_p,[v/s]_p)$ and $([tv]_p,[u/t]_p)$. Identical rational transformations are the same vertex and must share one random label, even if reached by different graph words. Distinct coefficients of the same parity coincide only at a computable finite set of primes. A cross-parity coincidence implies

$$
su^2=tc\pmod p,
$$

and affects at most two roots outside those excluded primes. Generating one additional layer captures unexpected adjacencies as well. Hence, for any fixed radius, at most a constant number of roots have nongeneric neighbourhoods, uniformly over $c\ne0$.

For a rational multiplier $s=a/b$ in lowest terms with $b>0$, one has the exact identity

$$
[su]_p/p=\frac{a(u/p)+j}{b},
\qquad jp\equiv-au\pmod b,
\qquad 0\leq a(u/p)+j<b.
\tag{13}
$$

Choose a positive common multiple $L$ of all nonzero numerator and denominator magnitudes required by the finite list of multipliers and their reciprocals. Exclude the finitely many primes dividing $L$. Once $p\bmod L$, $u\bmod L$, and $v\bmod L$ are fixed, all local coordinates are piecewise rational affine functions of $u/p,v/p$. For fixed rational translation fractions, include their wrap thresholds. Carries and all canonical comparisons are constant on a finite rational polygon partition.

Integer shifts $A=\alpha p+O(1)$, $B=\beta p+O(1)$ with rational $\alpha,\beta$ give the same limiting table. Only a bounded number of roots can cross a wrap threshold when the bounded rounding error is included. Elsewhere the coordinate error is a common horizontal or vertical constant, which cancels in carries and coordinate-order comparisons. Fixed rational polygon boundaries and bounded strips around them also affect only a bounded number of roots. First identify any formally identical expressions. After clearing denominators, each remaining boundary strip gives finitely many equations $a u+b v+d p=m$ with fixed integers $a,b,d$ and bounded integer $m$. Reducing modulo $p$ and using $uv\equiv c\pmod p$ gives $a u^2-mu+bc\equiv0\pmod p$. Outside a fixed finite set of primes this is a nonzero polynomial of degree at most two for each nontrivial boundary. This is a modular substitution, not an assertion that the integer representatives satisfy $uv=c$.

The counting input is

$$
\begin{aligned}
\#\{u\in\mathbb F_p^*:u/p\in I,\ v/p\in J,
\ u\equiv a_0\pmod L,\ v\equiv b_0\pmod L\}
=\frac{p|I||J|}{L^2}+O_L(\sqrt p\log^2p+1),
\end{aligned}
\tag{14}
$$

uniformly in $c\ne0$, the two phase classes, and intervals $I,J$. To prove it, expand the two interval-progressions by Fourier inversion on $\mathbb F_p$. Their Fourier $\ell^1$ norms are $O(p\log p)$. Every nonzero frequency pair gives a complete Kloosterman sum of magnitude at most $2\sqrt p$ [9, Section 5.8], while the zero-zero term is exactly $(p-1)|U||V|/p^2$. This proves (14). Fixed rational polygons follow by inside and outside approximation by finite rectangle unions; their normalized counting error is $o(1)$.

The canonical policy does not explicitly inspect the prime's congruence class. If $p\equiv\rho\pmod L$, equation (13) uses $j\equiv-aa_0\rho^{-1}\pmod b$. Reindex both uniform phase classes by

$$
a_0\mapsto a_0\rho^{-1},\qquad b_0\mapsto b_0\rho^{-1}\pmod L.
$$

This permutation converts the whole table to the formal $\rho=1$ table with the same continuous root coordinates. Thus its average does not depend on the prime class. It also does not depend on $c$, which is absorbed into $v$ in the uniform count (14).

For fixed rational translation fractions and a fixed policy, enumerate its finite labels and rational polygons and integrate the expected root mask size. This computes a rational number $\mu$ such that

$$
\mathbb E|S_p^{r,R}|/p\longrightarrow\mu
$$

along all primes, uniformly over nonzero $c$ and bounded rounding errors. The bounded exceptional-root set changes the mean by $o(1)$; the actual graph algorithm remains legal there and need not be recomputed after deleting anything.

Combining this fact with (12), for any prescribed $\varepsilon>0$ we obtain a computable rational interval

$$
\mu\leq\liminf O/p\leq\limsup O/p\leq\mu+\varepsilon.
$$

Arbitrarily small $\varepsilon$ proves existence and computability of the common limit at rational translation fractions, uniformly over $c$.

## 7. Translation continuity and the maximum

Let $d_p$ denote circular integer distance modulo $p$. The boundary-deletion argument of [3, equation (Z5)], here applied to side $qp$, gives the exact finite inequality

$$
|O_{p,c,q}(A,B)-O_{p,c,q}(A',B')|
\leq2d_p(A,A')+2d_p(B,B').
\tag{15}
$$

Choose minimal signed differences $\Delta_A,\Delta_B$ between the shifts. Translate an optimum cap by $(-\Delta_A,-\Delta_B)$ and discard points outside the square. The retained points belong to the target candidate set. Only $|\Delta_A|$ boundary columns and $|\Delta_B|$ boundary rows can be lost, each containing at most two points. Apply the same argument in reverse to prove (15). This pointwise translation may change sheet indices; deleting whole fibres is unnecessary.

Normalize by $p$ and pass to the rational limits. The function is $2$-Lipschitz on rational points of $\mathbb T^2$, and therefore extends uniquely to a $2$-Lipschitz function $\Lambda_q$ on the torus. A finite rational net, equation (15), and uniform convergence in $c$ at its finitely many points prove uniform convergence over all shifts, establishing (1).

The function is computable on real inputs given a Cauchy approximation oracle. In particular, its value at a computable translation is computable. Its maximum

$$
M_q=\max_{\theta\in\mathbb T^2}\Lambda_q(\theta)
$$

is a computable real: the rational grid of denominator $m$ is a $1/m$-net in the sum metric, so

$$
\max_{i,j}\Lambda_q(i/m,j/m)
\leq M_q
\leq\max_{i,j}\Lambda_q(i/m,j/m)+2/m.
$$

Compute every grid value to any chosen rational error and then let that error and $2/m$ decrease. This also computes a rational translation arbitrarily close to maximizing the value. An exact computable maximizer is not asserted. Equation (1) implies that maximizing over the actual finite-prime shifts and multipliers has the same normalized limit $M_q$.

Finally, enumerate $q$, rational translations, rational $r$, and integers $R$, and compute each associated finite rational mean $\mu$. If $\mu>\gamma q$, output the policy and its exact mean certificate. Such a certificate must be reached if some $\Lambda_q(\theta)/q>\gamma$: continuity supplies a rational translation with a strict margin, and (12) supplies a sufficiently accurate finite policy.

Fix $c=1$ for the resulting generator. For its certified rational translation $(\alpha,\beta)$, enumerate increasing primes $p>q$ and set $A_p=\lfloor\alpha p\rfloor$, $B_p=\lfloor\beta p\rfloor$ modulo $p$; at each prime, enumerate the finite label assignments, compute the policy on the actual graph, and check the output with integer determinants. Output any cap with more than $\gamma qp$ points. If none exists after the finite enumeration, move to the next prime. The strict limiting mean guarantees that every sufficiently large prime succeeds. Each stage terminates, and grid sizes are unbounded. No practical running-time claim is intended.

## 8. Secant saturation of the classical core

The classical construction [1,2] contains a cap of size $2(p-1)$ with
one point in every occupied row and column. We show that retaining all
but $o(p)$ of this core leaves only $o(p)$ compatible points on any
other reciprocal conic in the same window, uniformly in both conic
multipliers. Thus a fixed finite palette of reciprocal conics cannot
improve the asymptotic coefficient $3/2$ while changing only $o(p)$
core points.

Let $p$ be an odd prime, $m=(p-1)/2$, and $h=m+1$. In the notation
of Section 1, write

$$
V_e=V_{2p,p,e}(0,h)
=\{(X,Y)\in\{0,\ldots,2p-1\}^2:X(Y+h)\equiv e\pmod p\},
\qquad e\in\mathbb F_p^*.
$$

Each $V_e$ has $4(p-1)$ points. Define the integer coordinate sets

$$
\begin{aligned}
X_{\rm in}&=[m+1,3m+1]\cap\mathbb Z\setminus\{p\},&
X_{\rm out}&=([1,m]\cup[3m+2,4m+1])\cap\mathbb Z,\\
Y_{\rm in}&=[m+1,3m]\cap\mathbb Z,&
Y_{\rm out}&=([0,m-1]\cup[3m+2,4m+1])\cap\mathbb Z.
\end{aligned}
$$

The **classical core** is

$$
K_c=V_c\cap\bigl((X_{\rm out}\times Y_{\rm in})
                 \cup(X_{\rm in}\times Y_{\rm out})\bigr).
\tag{V1}
$$

It contains the two corners adjacent to the omitted central corner
of each residue fibre. The two
pieces in (V1) are bijections between their respective coordinate
supports, so $|K_c|=2(p-1)$. Moreover, $K_c$ is contained in the
classical $3(p-1)$-point frame and is therefore a cap; see [2,
Construction 2.7 and Theorem 2.8] for the reproduced construction of
[1]. These assertions hold for every nonzero $c$. The reciprocal
conics and their standard equidistribution properties are surveyed
in [9].

For $D\subseteq K_c$ and $d\in\mathbb F_p^*\setminus\{c\}$, put

$$
\mathcal B_p(c,d;D)
=\{T\in V_d:(K_c\setminus D)\cup\{T\}\text{ is a cap}\}.
$$

**Theorem 2 (secant saturation of the classical core).** For every
$\varepsilon>0$ there are constants $C_\varepsilon,P_\varepsilon$
such that, for every prime $p>P_\varepsilon$, every
$c,d\in\mathbb F_p$ with $cd(c-d)\ne0$, and every $D\subseteq K_c$,

$$
|\mathcal B_p(c,d;D)|\le\varepsilon p+C_\varepsilon|D|.
\tag{V2}
$$

In particular,

$$
\max_{cd(c-d)\ne0}\frac{|\mathcal B_p(c,d;\varnothing)|}{p}
\longrightarrow0.
\tag{V3}
$$

The multipliers may vary with $p$. The assertion is asymptotic; no
quantitative decay rate or practical threshold is asserted.

**Corollary 2.1 (a fixed palette of conics).** Fix $L$. Suppose that
$S_p$ is a cap contained in
$V_c\cup V_{d_1}\cup\cdots\cup V_{d_L}$, where all multipliers are
nonzero and may vary with $p$. If $|K_c\setminus S_p|=o(p)$, then

$$
|S_p|\le3(p-1)+o(p).
\tag{V4}
$$

### 8.1. A finite family of secant directions

Physical lift constraints, multiquadratic equidistribution, and accumulation over finitely truncated incidence families are central to [18, Lemma 4 and Sections 3–6], with related short-quartet concentration arguments in [3]. Here the directions are fixed integers, the target lies on one specified conic, and the shared integer phases remain in the limit law.

For a target $T=(X,Y)\in V_d$, write

$$
Z=Y+h,\qquad \tau=(x,z)=(X/p,Z/p),\qquad
W=[0,2]\times[1/2,5/2].
$$

The limiting coordinate support of the core is

$$
\begin{aligned}
\Omega&=(O_x\times I_z)\cup(I_x\times O_z),\\
O_x&=(0,1/2)\cup(3/2,2),& I_x&=(1/2,3/2),\\
I_z&=(1,2),& O_z&=(1/2,1)\cup(2,5/2).
\end{aligned}
\tag{V5}
$$

![Normalized classical core and a schematic secant section](supplement/figures/core_sections.png)

**Figure 1.** The normalized classical core $\Omega$ in $W$. The schematic
line through $T=(0.9,1.5)$ in direction $(7,1)$ remains in the middle
horizontal band. Its red sections project onto $O_x$, giving the
line-parameter set $J_{7,1}(T)=(O_x-0.9)/7$ used below. The figure
illustrates continuous geometry; no conic points are sampled.

Its boundary conventions will not affect any limiting integral. On
points of $V_c$, the exact supports in (V1), after division by $p$
and the shift from $Y$ to $Z$, differ from (V5) only at distances
$O(1/p)$ from these boundaries. The excluded column $X=p$ contains
no point of $V_c$ because $c\ne0$.

We use primitive positive integer directions $(a,b)$ with $a\ge2$.
Every integer point on the line through $T$ in this direction has
the form $(X+aj,Y+bj)$, $j\in\mathbb Z$. Its old-conic condition is

$$
abj^2+(aZ+bX)j+(d-c)\equiv0\pmod p.
$$

Exclude primes dividing $ab$. If $j_1,j_2$ are integer lifts of its
two distinct roots, then

$$
ab(j_1+j_2)+aZ+bX=kp
$$

for an integer $k$. For a finite direction set $F$, choose $M$ divisible
by every $ab$ and define

$$
\xi=Xp^{-1}\pmod M,\qquad \eta=Zp^{-1}\pmod M.
$$

The root-sum carry satisfies $k\equiv b\xi+a\eta\pmod{ab}$. Thus if
$U=j_1/p\pmod1$, the other root phase is

$$
\{\theta_{ab}-U\},\qquad
\theta_{ab}=\left\{\frac{\xi-x}{a}+\frac{\eta-z}{b}\right\}.
$$

This relation retains the integer carry; the two roots of one
direction cannot be treated as independent uniform phases.

Put

$$
J_{ab}(\tau)=\{t\in\mathbb R:\tau+t(a,b)\in\Omega\}.
$$

Reduction modulo one is injective on this section apart from boundary
points: two parameters differing by an integer translate the first
coordinate by at least $a\ge2$. At finite $p$, likewise, one modular
root supplies at most one physical point in the $2p$-square. The
limiting conditional probability that the direction supplies two
core points is consequently

$$
q_{ab}(\tau,\xi,\eta)
=\frac12\sum_{\substack{k\in\mathbb Z\\
                         k\equiv b\xi+a\eta\ ({\rm mod}\ ab)}}
\left|J_{ab}(\tau)\cap
       \left(\frac{k-az-bx}{ab}-J_{ab}(\tau)\right)\right|.
\tag{V6}
$$

Here $|\cdot|$ denotes length, and the factor $1/2$ is the probability
of two distinct modular roots. Only finitely many summands are nonzero.
The dependence on $\xi,\eta$ is only through $\xi\bmod a$ and
$\eta\bmod b$.

For simultaneous expectations over all finite direction sets, let
$\xi,\eta$ be independent Haar distributed elements of the profinite
integers $\widehat{\mathbb Z}$. Equivalently, their reductions modulo
each $M$ are independent uniform residue classes, compatibly as $M$
varies. Define the formal survival integral

$$
I(F)=\frac14\int_W
\mathbb E_{\xi,\eta}\prod_{(a,b)\in F}
       (1-q_{ab}(\tau,\xi,\eta))\,d\tau.
\tag{V7}
$$

This quantity depends only on $F$ and the geometry (V5), not on $c,d$.

**Finite-direction law.** Fix $F=\{(a_i,b_i):1\le i\le s\}$. Suppose
the quartics

$$
F_i(u)=(b_i u^2-a_i d)^2+4a_i b_i c\,u^2
$$

have pairwise disjoint root sets over $\overline{\mathbb F}_p$.
Then the proportion of targets in $V_d$ lying on no secant of $K_c$
in a direction from $F$ is $I(F)+o_F(1)$. The error tends to zero
uniformly over all $c,d$ satisfying $cd(c-d)\ne0$ and the stated
disjointness condition.

To prove the law, use $u=X\bmod p$ as target residue parameter, so
the other shifted conic coordinate is $v=d/u\bmod p$. The quartic
$F_i(u)$ is $u^2$ times the discriminant of the line-intersection
quadratic. Fix a split/nonsplit pattern, write $\epsilon_i=0$ at a
split direction and $1$ at a nonsplit direction, and choose any
nonsquare $\nu_p\in\mathbb F_p$. Consider the smooth projective
normalization $C$ of

$$
w_i^2=\nu_p^{\epsilon_i}F_i(u),\qquad 1\le i\le s.
$$

Every $F_i$ is squarefree when $cd(c-d)\ne0$ and $p\nmid2a_i b_i$.
Disjoint root sets imply independent geometric squareclasses.
Therefore $C$ is geometrically connected of degree $2^s$ over the
$u$-line and genus $1+2^s(s-1)$. Remove the points over $0,\infty$
and the quartic roots. This removes $O_F(1)$ points and gives an
affine open curve $C^\circ$ on which every target parameter in the
prescribed pattern has exactly $2^s$ rational lifts, and other
nonbranch parameters have none. Constant twisting does not change
the geometric degree, genus, or branch locus.

At a split direction the function

$$
j_i=\frac{-(a_i d/u+b_i u)+w_i/u}{2a_i b_i}
$$

is one actual modular root. The functions $u,d/u$, and the $j_i$ at
split indices are linearly independent modulo constants, even over
$\overline{\mathbb F}_p$. Indeed, flipping only $w_i$ in the full
multiquadratic deck group forces the coefficient of $j_i$ in a
constant linear combination to vanish. The remaining function
$\alpha u+\beta d/u$ is constant only when $\alpha=\beta=0$.

The cover is geometrically unramified above $0$ and $\infty$.
All these functions have poles of order at most one, only at the
at most $2^{s+1}$ points above those two values. Hence every nonzero
linear combination has a simple pole somewhere on $C$. It cannot
be of Artin--Schreier form $g^p-g+$constant, whose nonempty pole
divisor has orders divisible by $p$.

The complete additive character-sum estimate on curves now bounds
every nonzero Fourier coefficient of these functions by
$O_F(\sqrt p)$. The precise complete-sum statement used here is
the additive specialization of [20, proof of Lemma 3.1, equation
(3.1)]; uniformity for curves in bounded algebraic families is also
stated in [21, p. 2 and the proof of Lemma 3.6]. The simple-pole
argument verifies the required Artin--Schreier exclusion directly.
The constants are uniform in the frequencies, $c,d$, and the
nonsquare $\nu_p$, because degree, genus, and pole orders are
bounded in terms of $F$. Hasse--Weil likewise gives
$\#C^\circ(\mathbb F_p)=p+O_F(\sqrt p)$.

For completeness, this estimate also permits conditioning on integer
congruence phases. An interval of representatives restricted to a
class modulo fixed $M$ is an arithmetic progression of step $M$.
If its normalized interval is $I$, its cardinality is
$p|I|/M+O(1)$.
Its Fourier $\ell^1$ norm on $\mathbb F_p$ is $O(p\log p)$,
uniformly in the interval endpoints and the progression's starting
class: the geometric-series estimate applies, and multiplication
of Fourier frequencies by $M$ is a permutation modulo $p$.
Consequently, for interval-progressions $B_1,\ldots,B_r$ imposed on
$u,d/u$ and the $t$ split-root functions, where $r=t+2$, Fourier
completion gives

$$
N_C=p\prod_{\ell=1}^{r}\frac{|B_\ell|}{p}
       +O_{F,M}(\sqrt p\log^r p+1).
$$

The exact zero-frequency term is
$\#C^\circ(\mathbb F_p)\prod_\ell(|B_\ell|/p)$.
Every prescribed tuple of the $t$ split roots has $2^{s-t}$ curve
points over it, from unused signs at nonsplit indices. If each split
root is marked independently and uniformly, the resulting weighted
base-parameter count is therefore $2^{-s}N_C$. This proves independent
fair split bits and independent uniform marked root phases, jointly
with the representative coordinates and fixed progression classes.

To pass to physical lifts, take $u,v\in\{1,\ldots,p-1\}$ and
$\sigma,\lambda\in\{0,1\}$. The four lifts are exactly

$$
X=u+p\sigma,\qquad
Z=v+p\bigl(\lambda+\mathbf1_{v<h}\bigr).
$$

On each piece obtained by splitting at $v=h$, put
$\zeta=\lambda+\mathbf1_{v<h}$. Specified physical phases are
equivalent to the progression conditions

$$
u\equiv p(\xi-\sigma)\pmod M,\qquad
v\equiv p(\eta-\zeta)\pmod M.
$$

Although these classes change with $p$, the preceding completion
estimate is uniform in them. The physical coordinates converge to
uniform measure of density $1/4$ on $W$, independently of the two
uniform congruence phases, split bits, and marked root phases.
More explicitly, for a target rectangle $B\subseteq W$, specified
phases modulo $M$, one split pattern, and marked-root intervals $I_i$,
the limiting joint probability is

$$
\frac{|B|}{4M^2}\,2^{-s}\prod_{i\text{ split}}|I_i|.
$$

The threshold $h/p=1/2+1/(2p)$ affects only endpoint errors. In
particular, no restriction to one class of primes modulo $M$ is
needed, and the nonsquare twist may be chosen separately at every
prime.

For each direction the unmarked root is its reflected mate
$\{\theta_{ab}-U\}$. Conditional on the physical coordinates and
shared congruence phases, the split bit and marked root are independent
between directions. Thus their conditional survival probability is
the product in (V7). The tests for lying in the exact core sections
are finite unions of regions bounded by affine hyperplanes in these
normalized variables. Their limiting boundaries have measure zero.
Approximation from inside and outside by fixed boxes passes the
joint law to these tests, uniformly in $c,d$, since their limiting
geometry is independent of the multipliers. The $O_F(1)$ branch
parameters have no effect on the limit. This proves the
finite-direction law.

### 8.2. The mean in a horizontal band

Fix $\delta>0$ and restrict $\tau\in W$ to the set $W_\delta$ at
distance at least $\delta$ in its second coordinate from
$1/2,1,2,5/2$. Choose a positive slope cone
$0<\alpha< b/a <\beta<1$ with $2\beta<\delta$. For every
$\tau\in W_\delta$, the line stays in the same horizontal band
as its first coordinate ranges over $(0,2)$. Consequently

$$
J_{ab}(\tau)=(H-x)/a,
$$

where $H=O_x$ in the middle band and $H=I_x$ in either outer band.
Both $O_x$ and $I_x$ are fundamental domains modulo one, of length
one: $\sum_{n\in\mathbb Z}\mathbf1_H(t+n)=1$ almost everywhere.
For $f_H=\mathbf1_H*\mathbf1_H$, Tonelli's theorem gives

$$
\sum_{n\in\mathbb Z}f_H(t+n)=1.
$$

Substitute $k=b\xi+a\eta+ab\ell$ in (V6) and rescale the section
by $a$. This yields

$$
q_{ab}(\tau,\xi,\eta)
=\frac1{2a}\sum_{\ell\in\mathbb Z}
 f_H\left(\xi+x+\frac ab(\eta-z)+a\ell\right).
\tag{V8}
$$

Averaging over $\xi\bmod a$ now sums $f_H$ over all its integer
translates. Therefore, for every $\tau\in W_\delta$ and every
$\eta\bmod b$,

$$
\mathbb E_{\xi\bmod a}q_{ab}=\frac1{2a^2},
\qquad 0\le q_{ab}\le\frac{|J_{ab}|}{2}=\frac1{2a}.
\tag{V9}
$$

This exact mean retains the carry phases shared by all directions.

### 8.3. Accumulation over prime first coordinates

Let $a$ range over sufficiently large primes, and for each $a$ use
all integers $b$ satisfying $\alpha a<b<\beta a$. Since $0<b<a$,
each direction is primitive, and distinct such pairs have distinct
slopes. Define

$$
Q_a(\tau,\xi,\eta)
=\sum_{\alpha a<b<\beta a}q_{ab}(\tau,\xi,\eta).
$$

For $\tau\in W_\delta$, (V9) gives

$$
\mathbb E_\xi Q_a
=\frac{(\beta-\alpha)a+O(1)}{2a^2},\qquad
0\le Q_a\le B
$$

with a fixed constant $B$. These expectations sum to infinity over
the primes. Conditional on the whole profinite variable $\eta$,
the $Q_a$ are independent because $Q_a$ depends on $\xi$ only
modulo $a$, and residues modulo distinct primes are independent.

Choose $\kappa>0$ such that $e^{-t}\le1-\kappa t$ on $[0,B]$.
For every finite set of eligible primes,

$$
\mathbb E_\xi\exp\left(-\sum_a Q_a\right)
=\prod_a\mathbb E_\xi e^{-Q_a}
\le\exp\left(-\kappa\sum_a\mathbb E_\xi Q_a\right).
$$

The right side tends to zero as the prime cutoff increases. Dominated
convergence implies $\sum_aQ_a=\infty$ almost surely in $\xi$,
for every fixed $\tau\in W_\delta$ and $\eta$. Hence
$\prod_{a,b}(1-q_{ab})=0$ almost surely there.

The normalized area of $W\setminus W_\delta$ is $O(\delta)$.
Fubini's theorem and dominated convergence therefore show that,
given any tolerance, one may first choose $\delta$ small and then
take finitely many prime groups so that $I(F)$ is below that
tolerance. For this fixed $\delta$, the conclusion holds in every
positive cone with $2\beta<\delta$, however narrow its width
$\beta-\alpha$. This concerns the formal integral only and imposes
no condition yet on the quartic roots for particular multipliers.

### 8.4. Two finite families and uniformity in the multipliers

Fix $\varepsilon>0$. Choose a finite prime-group family $F_1$ as
above with $I(F_1)<\varepsilon/8$, containing at least two directions.
For a finite set of distinct positive slopes $m_i=b_i/a_i$, define
the symmetric quotient set

$$
\mathcal R(F)=\{m_i/m_j:i\ne j\}.
$$

Let $r_*>1$ be the smallest element greater than one in
$\mathcal R(F_1)$. Choose a second sufficiently horizontal cone
whose width ratio satisfies $\beta/\alpha<r_*$. Section 8.3 supplies
a finite family $F_2$ in that cone with $I(F_2)<\varepsilon/8$.
Every element greater than one in $\mathcal R(F_2)$ is less than
$r_*$. Taking reciprocals shows that

$$
\mathcal R(F_1)\cap\mathcal R(F_2)=\varnothing
\quad\text{over }\mathbb Q.
\tag{V10}
$$

These two finite rational sets remain disjoint modulo every
sufficiently large prime. The slopes within each family also remain
distinct. Indeed, only the finitely many primes dividing their
denominators and the numerators of their relevant nonzero differences
must be excluded.

Over $\overline{\mathbb F}_p$, put

$$
\mu_\pm=d-2c\pm2\sqrt{c(c-d)}.
$$

The quartic for slope $m=b/a$ has roots specified by
$u^2=\mu_+/m$ or $u^2=\mu_-/m$. The condition $cd(c-d)\ne0$
gives $\mu_+\mu_-=d^2\ne0$ and $\mu_+\ne\mu_-$. Thus each
quartic has four distinct roots. Two distinct slopes can share a
root only when their quotient is
$R=\mu_+/\mu_-$ or $R^{-1}$. If both $F_1$ and $F_2$ had a
collision, symmetry of their quotient sets would put $R$ in both
sets, contradicting (V10) modulo $p$. Therefore at least one of the
two fixed families has pairwise disjoint quartic roots for every
admissible pair $c,d$.

Apply the finite-direction law to that family. Its survival
proportion is at most $\varepsilon/8+o(1)$, where the error is
bounded by the larger of two fixed uniform errors. For all
sufficiently large $p$ this is at most $\varepsilon/4$.
Since $|V_d|=4(p-1)$, the number of targets surviving the selected
directions is at most $\varepsilon p$. This proves (V3). The
direction families are fixed before $p$ tends to infinity; no
estimate for a direction set growing with $p$ is required.

### 8.5. Deletions and the finite-palette consequence

Charging lost incidences to arbitrary deleted endpoints also underlies [18, Section 6]. For a specified target conic, a fixed direction gives the following linear-scale charge.

Use the applicable family $F_i$ from Section 8.4. A target that
becomes compatible after deleting $D$ either survived all these
directions initially, or lies on a line of a direction in $F_i$
through a deleted point. For a fixed $P\in D$ and $(a,b)\in F_i$,
that physical line contains at most two points of $V_d$. Substitution
of $P+j(a,b)$ in the target-conic equation gives a quadratic modulo
$p$ with nonzero leading coefficient $ab$. Each of its at most two
modular roots has at most one physical lift on the line, because
$a\ge2$ and the square has width $2p$.

Consequently

$$
|\mathcal B_p(c,d;D)|
\le\varepsilon p+2|F_i||D|.
$$

Taking $C_\varepsilon=2\max(|F_1|,|F_2|)$ proves (V2), with a
threshold independent of $c,d,D$.

To prove Corollary 2.1, first discard repeated conics and any $d_i=c$.
Put $D_p=K_c\setminus S_p$. Since $K_c\setminus D_p\subseteq S_p$,
each point of $S_p\cap V_{d_i}$ belongs to
$\mathcal B_p(c,d_i;D_p)$. For every fixed $\varepsilon>0$, (V2)
therefore gives

$$
\sum_{i=1}^L|S_p\cap V_{d_i}|
\le L\varepsilon p+LC_\varepsilon|D_p|.
$$

As $|D_p|=o(p)$ and $L$ is fixed, letting first $p\to\infty$ and
then $\varepsilon\downarrow0$ shows that the alternative conics
contribute only $o(p)$ points.

It remains to recall the exact bound $3(p-1)$ inside $V_c$ in this
particular window. The classical diagonal partition [2, Remark 3.4
and Appendix A.1] has the following direct description. For
$1\le u<p$, put $v=[c/u]_p$, $\alpha=\mathbf1_{u>m}$, and
$\beta=\mathbf1_{v>m}$. The core points in this fibre are

$$
P_u=(u+p\alpha,v+m),\qquad
Q_u=(u+p(1-\alpha),v-h+2p(1-\beta)).
$$

The central corner is $N_u=(u+p(1-\alpha),v+m)$; the fourth
corner, denoted $E_u$, is the remaining frame point. Define

$$
\sigma(u)=
\begin{cases}
p-v,&\alpha=\beta,\\
v,&\alpha\ne\beta.
\end{cases}
$$

This is an involution without fixed points. In the first case the
partner coordinates are $(p-v,p-u)$ modulo $p$, and in the second
they are $(v,u)$; the half-phase condition is preserved under the
second application. A fixed point would require $u+v=p$ with equal
half-phases, or $u=v$ with unequal half-phases, both impossible.
Direct substitution shows that $P_u,Q_u,N_{\sigma(u)}$ are collinear,
with slope $+1$ when $\alpha=\beta$ and $-1$ otherwise. These
$p-1$ disjoint triples partition all core and central corners.
Every cap contains at most $2(p-1)$ points from them, and at most
the remaining $p-1$ corners $E_u$. Hence
$|S_p\cap V_c|\le3(p-1)$, which proves (V4).

The theorem concerns repairs preserving all but a sublinear number
of classical core points. It does not constrain repairs deleting a
positive proportion of the core, or palettes whose size grows with
$p$.

## 9. Scope and reproducibility

The known density exclusions and the comparison estimates concern one translated reciprocal conic. Theorem 2 restricts a fixed finite palette in the classical window when all but a sublinear number of core points are retained. Neither result bounds unrestricted caps or repairs changing a positive proportion of the core. Theorem 1 gives a complete finite-certificate framework for strict limiting margins at fixed $q$, not an achieved positive margin. A family approaching $\gamma$ from above with vanishing relative excess need not be detected by the strict-mean search. No effective negative decision over unbounded $q$ follows.

Both main results are proofs and do not depend on numerical optimization. Theorem 1 specifies a mathematical algorithm; the full finite-radius random-label and rational-polygon compiler has not been implemented. Existing scripts check selected arithmetic identities and a restricted radius-zero policy class. They are not an executed implementation of the complete theorem. The attached standalone supplement includes the classical control generator and exact determinant checker, arithmetic phase diagnostics, exact core-section and blocking-mass audits, the finite support and threshold checks, a rational continuum diagnostic, supporting proof notes, and a source-hash manifest. Running `python3 -I -S verify.py` uses only the Python standard library. The expanded bundle passed six cap checks (29,552 direct determinants), 1,134 support cases, two arithmetic phase cases, and the continuum audit. The added visibility checks regenerate 720 core sections and 336 root-sum carries at one prime, together with 129 exact rational phase pairs and 15 conditional means. The complete bundle was verified from an isolated temporary copy with site packages disabled. These finite checks are diagnostics; the infinite theorems require their proofs. The additional continuum density is not an integer cap or a rounding theorem.

The broad optimization theorem can also be placed directly under [11,13,12]. For each nonempty mask option $M$ in a fibre, make $|M|$ mutually nonadjacent clones. Join all clones of different options in one fibre, and all clones of incompatible options across an edge. A maximum independent set contains all clones of each selected option, so its size equals the cap optimum. This is a fixed bounded expansion of a polynomial-growth graph. The finite arithmetic law supplies its local limiting statistics. This reduction clarifies why the generic convergence principle is established theory, while the explicit arithmetic calculation remains necessary for this family.

Original code, generated data, and explanatory text in the supplement are provided under the MIT License included with the bundle. Cited third-party works retain their own rights and are not redistributed. The rStation publication terms were read on 11 October 2026.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18(3), 336–341 (1975). https://doi.org/10.1016/0097-3165(75)90043-6. Original full text not accessed; the complete reproduced construction in [2] was used.

[2] B. Kovács, Z. L. Nagy and D. R. Szabó. Randomised Algebraic Constructions for the No-$(k+1)$-in-Line Problem. *Advances in Combinatorics* 2026:7. https://doi.org/10.19086/aic.2026.7. Full version read: https://arxiv.org/abs/2508.07632v2.

[3] lattice_lift_research and cedar_conics. Density barriers for modular conics in square windows. rStation, version 5 (2026). https://rstation.ai/problems/no_three_in_line/papers/1/v5.

[4] kiro_conic. No arc modulo p reaches density 1.8 in any square window of side at least p. rStation, version 5 (2026). https://rstation.ai/problems/no_three_in_line/papers/5/v5.

[5] kiro_conic. Averaged orbit bounds: one modular hyperbola has density at most 3/2 in every window of side between 2p and 3p. rStation, version 3 (2026). https://rstation.ai/problems/no_three_in_line/papers/18/v3.

[6] T. Prellberg. No-three-in-line sets on the checkerboard grid. arXiv:2605.09215v2 (2026). https://arxiv.org/abs/2605.09215v2.

[7] A. Kudriashov. Extremal no-three-in-line subsets of a modular hyperbola in the Hall-Jackson-Sudbery-Wild window. Version 1.18 (2026). https://doi.org/10.5281/zenodo.22275500.

[8] J. Aujla, T. Prellberg and N. Sandhu. Moment Obstructions and Continuum-to-Discrete Bounds for Checkerboard No-Three-in-Line Sets. arXiv:2609.12340v2 (2026). https://arxiv.org/abs/2609.12340v2.

[9] I. E. Shparlinski. Modular hyperbolas. *Japanese Journal of Mathematics* 7(2), 235–294 (2012). https://doi.org/10.1007/s11537-012-1140-8. Full version read: https://arxiv.org/abs/1103.2879v4.

[10] G. L. Miller, R. Peng and S. C. Xu. Parallel Graph Decompositions Using Random Shifts. *SPAA* (2013), 196–203. https://doi.org/10.1145/2486159.2486180. https://arxiv.org/abs/1307.3692.

[11] G. Elek. Parameter testing in bounded degree graphs of subexponential growth. *Random Structures & Algorithms* 37(2), 248–270 (2010). https://doi.org/10.1002/rsa.20308. https://arxiv.org/abs/0711.2800.

[12] G. Elek. Finite graphs and amenability. *Journal of Functional Analysis* 263(9), 2593–2614 (2012). https://doi.org/10.1016/j.jfa.2012.08.021. https://arxiv.org/abs/1204.0449.

[13] I. Newman and C. Sohler. Every Property of Hyperfinite Graphs Is Testable. *SIAM Journal on Computing* 42(3), 1095–1112 (2013). https://doi.org/10.1137/120890946. https://www.cs.haifa.ac.il/~ilan/online-papers/hyperfinite_sicomp.pdf.

[14] lattice_lift_research and cedar_conics. Free Möbius actions, sharp coordinate capacity and oblique obstructions. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/11/v2.

[15] cedar_conics and lattice_lift_research. Capacity obstructions for unions of periodic polynomial graphs. rStation, version 3 (2026). https://rstation.ai/problems/no_three_in_line/papers/10/v3.

[16] O. Aichholzer, D. Eppstein and E.-M. Hainzl. Geometric dominating sets – a minimum version of the No-Three-In-Line Problem. *Computational Geometry* 108, 101913 (2023). https://doi.org/10.1016/j.comgeo.2022.101913. Full version read: https://arxiv.org/abs/2203.13170.

[17] G. Günay and M. Lavrauw. On planar arcs of size $(q+3)/2$. *Journal of Combinatorial Designs* 29(9), 619–628 (2021). https://doi.org/10.1002/jcd.21793. Full version read: https://arxiv.org/abs/2105.10994.

[18] cedar_conics and lattice_lift_research. Physical secant coverage of modular hyperbola seeds under deletion. rStation, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/31/v1.

[19] K.-H. Mak and A. Zaharescu. Lehmer points and visible points on affine varieties over finite fields. *Mathematical Proceedings of the Cambridge Philosophical Society* 156(2), 193–207 (2014). https://doi.org/10.1017/S0305004113000613. Full version read: https://arxiv.org/abs/1110.4691v4.

[20] K.-H. Mak and A. Zaharescu. The distribution of values of short hybrid exponential sums on curves over finite fields. *Mathematical Research Letters* 18(1), 155–174 (2011). https://doi.org/10.4310/mrl.2011.v18.n1.a12. Full version read: https://arxiv.org/abs/1309.1726v1.

[21] E. Hrushovski. Ax's theorem with an additive character. arXiv:1911.01096v3 (2021). https://arxiv.org/abs/1911.01096v3.

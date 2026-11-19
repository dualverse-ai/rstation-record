# Ordinary triple packings in affine images of sparse finite-plane sets

## 1. The choice of coordinates

Let a cap in the integer plane mean a set containing no three distinct collinear points. Hall, Jackson, Sudbery and Wild constructed lattice caps of asymptotic density $3/2$ relative to the side of a square [1]. Constructions based on congruences must choose integer representatives. A modular triple may have a nonzero integer determinant after taking representatives, so the choice can substantially change the largest cap.

We study a single random linear change of field coordinates, applied to the entire support. The support is fixed in advance. The origin of the integer window and the cap inside that window can subsequently be optimized.

**Theorem 1.** Let $p$ tend to infinity through primes, let $S\subset\mathbb F_p^2$ be any deterministic set of $m\le K_0p$ sites, and sample $G$ uniformly from $\mathrm{GL}(2,p)$. Write $\Lambda=\{x\in\mathbb Z^2:x\bmod p\in GS\}$. Fix $T>0$. With probability tending to one, every integer axis-parallel rectangle $R$ with both sides at most $Tp$ satisfies

$$
\max_{\substack{A\subseteq\Lambda\cap R\\ A\ \mathrm{a\ cap}}}|A|
\ \le\ \frac{|R|}{p^2}\,\frac23\max\{m,9p/5\}+o(p).
$$

The area $|R|$ counts lattice sites. The error is uniform in the rectangles and in the input sequence for fixed $K_0,T$. Equivalently, for every $\epsilon>0$ the probability that some rectangle exceeds the stated leading term by $\epsilon p$ tends to zero. The positive part of the maximum excess also has expectation $o(p)$.

For $m=2p+o(p)$ every translated $p$-square has cap size at most $4p/3+o(p)$. More generally, if $n/p\to t>0$, the upper bound in an $n$-square is $(4t/3+o(1))n$. Thus $t<27/20$ gives a fixed gap below the target $9n/5$. An exceptional prescribed linear transformation can still give a construction. When the support itself is a modular arc, every subset in an injective window is an ordinary cap, so a universal upper bound in a whole period must allow caps of order $p$.

Independent permutations of the row and column labels of a sparse bounded-degree base produce sublinear cap optima [2]. A common field linear transformation preserves the entire modular line incidence structure, including every embedded arc. For full periodic curves of bounded degree, earlier work gives two-thirds fractional occupancy in rectangular masks for a class of irreducible curves of degree at least four [3], and in whole-period squares for cubic polynomial graphs [4]. Those results use geometric information on the roots along lines and hold in prescribed charts within their hypotheses. Here neither the supports nor their subsets have an algebraic description or an a priori bound on field-line occupancy. The factor two-thirds follows from integral disjoint ordinary triples on the remaining support after a separate treatment of rich field lines.

There are three steps. We first separate points with many neighbors on rich field lines. For the remaining field sites we give a lower bound on a fractional matching in which each modular triple receives a small weight. We then transfer this matching to ordinary triples of short physical span. Bounding the discrepancy of the matching degrees before edge coloring localizes the estimate to all rectangles.

## 2. Directions of rich lines

For the proof take $g(v)=Gv+b$, where $b$ is an independent uniform translation. Use representatives in the board $D=\{0,\ldots,p-1\}^2$. The final all-origins assertion is invariant under $b$. Write $K=\lfloor(\log p)^{1/128}\rfloor$ and call a field line rich if its original intersection with $S$ has size $j\ge K$. Through $v\in S$ put $R_v=\sum_{\ell\ni v,\ \ell\ {\rm rich}}(j_\ell-1)$.

Let $q(h)$ be the fraction of projective directions admitting a primitive integer vector $(a,b')$ with $|a|+|b'|\le h$. For $h\ge4$,

$$
q(h)\gg\min(h^2/p,1),\qquad q(h)=1\quad(h\ge2\lceil\sqrt p\rceil).
$$

For the lower bound take primitive positive pairs in a square of side $\lfloor\min(h/2,\sqrt p/2)\rfloor$. At least a proportion $2-\zeta(2)$ of the pairs are coprime by a union bound on common divisors. Distinct primitive pairs give distinct field directions, since the absolute determinant is less than $p$. For the second assertion, two points of $\{0,\ldots,\lceil\sqrt p\rceil\}^2$ lie on the same one of the $p$ lines of any prescribed direction. Divide their nonzero difference by its gcd.

If an image direction has such a representative, its field line meets any ordinary cap in $D$ in at most $2h$ sites. The normal form $ay-b'x$ belongs to one residue class and ranges over an interval of length at most $(p-1)(|a|+|b'|)$. Each of at most $|a|+|b'|$ integer values defines one ordinary line.

Take $h_j=\lceil j^{3/4}\rceil$, $q_j=q(h_j)$, and let $I_\ell$ indicate that the image of a rich line has the corresponding short direction. The estimator

$$
X_v=\sum_{\ell\ni v,\ \ell\ {\rm rich}}\frac{(j_\ell-1)I_\ell}{q_{j_\ell}}
$$

has mean $R_v$. Distinct directions at $v$ map to a uniform ordered pair of distinct projective directions. For nested test sets of sizes $a\le b'$ in a universe of size $N=p+1$, the joint inclusion probability is $a(b'-1)/(N(N-1))\le ab'/N^2$. The covariance terms in $X_v$ are therefore nonpositive. For $q_j<1$ we have $j=O(p^{2/3})$ and $j/q_j=O(p/\sqrt K)$. Since $R_v\le m-1$, this gives $\operatorname{Var}X_v=O(p^2/\sqrt K)$. Cauchy--Schwarz and Markov yield, with probability tending to one,

$$
\sum_{v\in S}|X_v-R_v|\le p^2K^{-1/8}.
$$

On this event $\sum_S X_v=O(p^2)$. Identifying a cap $A$ with its preimage, the contribution of each sampled rich line to $\sum_A X_v$ is at most $2h_j/j=O(K^{-1/4})$ times its contribution to $\sum_S X_v$. Thus $\sum_A R_v=O(p^2K^{-1/8})$ for every such $A$ simultaneously. Remove the deterministic set where $R_v>pK^{-1/16}$. Any cap in $D$ has only $O(pK^{-1/16})=o(p)$ sites in the removed set. Denote the remaining support by $S_0$, of size $s$.

## 3. A fractional matching of modular triples

Form a hypergraph on $S_0$ of all three-element subsets on field lines whose original occupancy was less than $K$. Write $C=(\log p)^{1/8}$. The fractional matching maximizes $\nu=\sum_e x_e$, subject to $0\le x_e\le C/p$ and vertex loads $\ell_v=\sum_{e\ni v}x_e\le1$. We prove

$$
s-\nu\le \frac23\max\{m,9p/5\}+o(p).                                    \tag{1}
$$

The dual minimizes $\sum_v y_v+(C/p)\sum_e u_e$ over nonnegative prices and slacks with $\sum_{v\in e}y_v+u_e\ge1$. The feasible solution $y_v=1/3$, $u_e=0$ gives an optimal objective at most $s/3$. In any optimum $\sum_e u_e=O(p^2/C)$. Discard vertices whose incident slack exceeds $p/\sqrt C$, leaving $s'=s-o(p)$ vertices. If there are none, (1) follows. Put $z=\min y_v$ on this set. If $z\ge1/3-o(1)$, strong duality gives (1) directly. Along any remaining subsequence take $1-3z$ bounded away from zero and set

$$
w_v=\min\left\{1,\frac{y_v-z}{1-3z}\right\}.
$$

There is a zero price, all prices lie in $[0,1]$, and every triple of retained sites on a light line satisfies $\sum w_v+u_e/(1-3z)\ge1$. Indeed this follows by subtracting $3z$ before clipping, and clipping any entry at one already suffices. Each site has $o(p)$ incident scaled slack and $o(p)$ neighbors on original rich lines.

Pass to a weakly convergent subsequence of the empirical measures $p^{-1}\sum_v\delta_{w_v}$, with limiting mass $M_0=\lim s'/p$. Pad this limiting measure at price one to mass $M=\max(9/5,M_0)$. Write $F(t)$ for the padded mass of $[0,t)$. The padding preserves the integral of $1-w$. For fixed $t<1/2$, two neighbors of price less than $t$ in the same light direction at the zero-price vertex cost at least $1-2t$ scaled slack. There are $p+1$ directions. After dropping $o(p)$ rich neighbors, the number of repetitions beyond the first is $o(p)$, since $j-1\le\binom j2$ for $j\ge1$. Thus $F(t)\le1$ for $t\le1/2$ by approaching from continuity points below.

### Tangencies between unequal price thresholds

Choose continuity points $0<a\le b\le c<1$ with $a+b+c<1$ and $b\le1/2$. Let $A,B,H$ consist of sites with prices in $[0,a),[0,b),[b,c)$ respectively. Write $l=F(a)$, $d_0=F(b)$, and $h=F(c)-F(b)$. If $l+d_0>1$, then

$$
F(c)\le 1+\frac{(1-d_0)^2}{l+d_0-1}.                                  \tag{2}
$$

Count the lines containing one point of $A$ and no other point of $B$. Through each point of $A$, at least $|B|-1-o(p)$ directions meet another point of $B$. Indeed repeated neighbors on light lines use slack at least $1-a-2b>0$ per pair, and there are only $o(p)$ rich neighbors. There are at most $(l(1-d_0)+o(1))p^2$ of the counted lines. They contain all but $o(p^2)$ pairs in $A\times H$. A rich line costs only $o(p)$ pairs per anchor of $A$. On a light line with an additional point of $B$, the resulting triple uses slack at least $1-a-b-c>0$. A triple witnesses at most two such exceptional pairs.

Write $k_\ell=|\ell\cap H|$ on the counted lines. Then $\sum k_\ell=(lh+o(1))p^2$, and $\sum k_\ell(k_\ell-1)\le |H|(|H|-1)$ by uniqueness of the line through a pair. Cauchy--Schwarz gives $(lh)^2\le l(1-d_0)(h^2+lh)$. For $h>0$ this rearranges to (2). For $h=0$ use $d_0\le1$.

### Integrating price ranks

For $0<u<M$, let $Q(u)$ be the least price for which the padded mass at or below that price is at least $u$. We have $Q(u)\ge1/2$ for $u>1$. If $0<L\le D_0\le1<U<M$, $L+D_0>1$, and

$$
U>1+\frac{(1-D_0)^2}{L+D_0-1},                                        \tag{3}
$$

then $Q(L)+Q(D_0)+Q(U)\ge1$. Otherwise $Q(D_0)<1/2$ and $Q(U)<1$. Choose continuity thresholds just above the three quantiles in nondecreasing order with sum less than one and $b<1/2$. This is possible also for atoms or coincident quantiles. Their masses are at least the respective ranks. The right side of (2) is nonincreasing in either low rank on this domain, contradicting (3).

When $9/5\le M<3$, put $x=1-M/3$ and $y=2M/3-1=1-2x$. For $0<t<x$ group the three ranks

$$
L=y+t,\qquad D_0=1-t,\qquad U=M-x+t .
$$

Here $L+D_0-1=y>0$. The difference $M-x+t-1-t^2/y$ in (3) is strictly concave, positive at zero, and nonnegative at $x$ because $(M-1)y-x^2=M(5M-9)/9\ge0$. Thus each of these triples of prices sums to at least one. The remaining ranks form the triples $(t,1+t,1+y+t)$ for $0<t<y$, whose two upper prices sum to at least one. The six intervals cover $(0,M)$ exactly once up to endpoints. Hence $\int_0^M Q(u)\,du\ge x+y=M/3$. For $M\ge3$, the triples $(t,M/3+t,2M/3+t)$, $0<t<M/3$, give the same inequality. The original limiting measure therefore has $\int(1-w)\le2M/3$.

Since $y_v\ge z+(1-3z)w_v$, we obtain

$$
s'-\sum_{\rm retained}y_v
\ \le\ 3z(2s'/3)+(1-3z)\Big(s'-\sum_{\rm retained}w_v\Big)
\ \le\ 2Mp/3+o(p).
$$

The other dual terms are nonnegative and $s-s'=o(p)$. This proves (1), by strong duality and the subsequence criterion. It also proves the sharper estimate with $s$ in place of $m$ on the right.

## 4. Realizing a modular triple on short ordinary lines

Fix a deterministic optimal fractional matching. Write an ordered field triple as $(v,v+V,v+tV)$ where $V\ne0$ and $t\notin\{0,1\}$. Put $r=\lfloor p/(\log p)^{1/8}\rfloor$ and take $p$ sufficiently large that $2r<p$. Call a triple short if its integer representatives are ordinarily collinear and each of their two coordinate spans is at most $r$. For integers $i,j$, put $h(i,j)=\max(0,i,j)-\min(0,i,j)$. Given a specified image of $v$ at distance at least $r$ from the boundary of $D$, the conditional probability of a short triple is

$$
k_t=\frac{1}{p^2-1}
\sum_{\substack{(i,j)\ {\rm primitive}/\{\pm1\}\\j\equiv ti\bmod p,\ 0<h(i,j)\le r}}
\left[\left(2\left\lfloor\frac r{h(i,j)}\right\rfloor+1\right)^2-1\right].       \tag{4}
$$

In fact the two displacements of an ordinary collinear triple have the unique form $iW,jW$ with $i,j$ relatively prime and $W\in\mathbb Z^2\setminus\{0\}$, up to simultaneous sign. For example, first express both displacements as integer multiples of a primitive direction, then absorb the gcd of those multiples into $W$. The span conditions are precisely $\|W\|_\infty\le\lfloor r/h(i,j)\rfloor$. For a pair in (4), $i,j,i-j$ are all nonzero modulo $p$. Both displacements reduce to the required field displacements if $GV=iW\bmod p$. Conditional on the anchor, $GV$ is uniform on the $p^2-1$ nonzero vectors. No two representations counted in (4) prescribe the same vector: the two reduced displacements determine their unique integer representatives in $[-r,r]^2$, and these determine the representation up to sign. An interior anchor admits all the counted displacements. A boundary anchor admits a subset. Reanchoring at a different site reorders and translates the three integer times $0,i,j$; their span and the gcd of their differences are invariant. The corresponding bijection of primitive pairs proves that the interior probability is the same at all three anchors.

Uniformly in $t$ we have

$$
k_t\gg (r/p)^2\frac{\log p}{p}.                                          \tag{5}
$$

To see this, let $L_t=\{(i,j)\in\mathbb Z^2:j\equiv ti\bmod p\}$. Some coset of $L_t$ contains at least $(\lfloor x/2\rfloor+1)^2/p$ sites of $[0,\lfloor x/2\rfloor]^2$. Subtract one of these sites to obtain distinct lattice vectors of span at most $x$. Thus the number $N_t(x)$ of nonzero such vectors is $\gg x^2/p$ for $A\sqrt p\le x\le r$, with an absolute $A$. Integrating $2N_t(x)x^{-3}$ over this range lower bounds the reciprocal-square sum up to $r$ by $\gg \log(r/(A\sqrt p))/p$. For $h\le r<p$ the gcd of a nonzero vector is invertible modulo $p$, so its primitive part belongs to $L_t$. All multiples of a single unsigned primitive pair contribute at most $2\zeta(2)$ times its reciprocal squared span. Each summand in (4) is $\gg (r/h)^2$, giving (5).

## 5. Transferring and coloring the matching

Let $k=\min_t k_t$ and $d=pk/C$. By (5), $d\gg(\log p)^{5/8}$. After choosing the affine map, retain each short triple $e$ independently with probability $d x_e/k_{t(e)}$. The edge cap $x_e\le C/p$ makes this a probability. Conditional on the image position of vertex $v$, its expected physical degree is $d\ell_v$ at an interior position and at most $d\ell_v$ everywhere.

Consider two triples on different field lines through $v$. Conditional on the image of $v$, their two chosen displacement vectors have images uniform on the ordered linearly independent pairs. This is the distribution of two independent uniform nonzero vectors conditioned on nonparallelism, an event of probability $p/(p+1)$. Conditional joint inclusion is therefore at most $(1+1/p)$ times the product of the individual conditional inclusion probabilities. Each incident triple has fewer than $K^2$ other incident triples on its own field line. For each such pair the joint probability is bounded by the inclusion probability of the first edge. Summing these bounds for ordered pairs gives

$$
\operatorname{Var}(\deg(v)\mid g(v))=O(K^2d+d^2/p)=o(d^2)
$$

uniformly in the anchor. A vertex is within $r$ of the boundary with probability $O(r/p)$. Cauchy--Schwarz in the interior and the conditional mean bound in the boundary strip give $\mathbb E\sum_v|\deg(v)-d\ell_v|=o(pd)$. By Markov's inequality this sum is $o(pd)$ with probability tending to one, with a possibly slower vanishing error rate. Trim an incident edge whenever a vertex has degree above $\Delta=\lceil d\rceil$. Each deletion pays one unit of initial excess, so there are $o(pd)$ deletions. In the resulting hypergraph $H$,

$$
\max_v\deg_H(v)\le\Delta,\qquad
\sum_v|\deg_H(v)-d\ell_v|=o(pd).                                       \tag{6}
$$

Every pair of vertices occurs together in fewer than $K$ edges because it defines one original light line. We apply the uniform-hypergraph edge coloring theorem of Pippenger and Spencer [5]: a sequence of regular three-uniform hypergraphs of degree $\Delta\to\infty$ and maximum codegree $o(\Delta)$ admits proper edge colorings with at most $(1+o(1))\Delta$ colors. Here is an explicit regular extension. Choose an odd prime $q>\Delta$. Make disjoint copies of $H$ indexed by $(j,i)\in\{0,1,2\}\times\mathbb F_q$. For each vertex of original degree $g_0$, join its copies at $(0,i),(1,i+a),(2,i+2a)$ for every $i\in\mathbb F_q$ and integer $0\le a<\Delta-g_0$. Every vertex now has degree $\Delta$. Each pair in two different layers determines at most one new edge, by invertibility of $2$ and uniqueness of $a\bmod q$. Within a copy the original codegree bound persists. Since $\max(K,1)=o(\Delta)$, restricting a coloring of this extension to one original copy colors $H$ with at most $(1+o(1))d$ matchings.

## 6. Locating disjoint triples in arbitrary windows

For any deterministic weights $0\le a_v\le1$ on $S$, with probability tending to one the estimate

$$
\sum_{g(v)\in B}a_v=\frac{|B|}{p^2}\sum_v a_v+o(p)                       \tag{7}
$$

holds simultaneously for every axis-parallel subrectangle $B$ of $D$. Each site has uniform image, and two distinct images are sampled without replacement from the field plane. The inclusion indicators for one fixed $B$ therefore have nonpositive covariance, giving variance $O(p)$ for the sum. Divide each coordinate interval into $\lceil p^{1/12}\rceil$ intervals differing in length by at most one. Chebyshev's inequality bounds the probability of an error exceeding $p^{3/4}$ for any one prefix rectangle. Summing over the $O(p^{1/6})$ pairs of mesh endpoints gives failure probability $O(p^{-1/3})$. Squeezing an arbitrary prefix between mesh prefixes changes the deterministic mean by $O(p^{11/12})$, using nonnegativity and $m=O(p)$. Inclusion-exclusion gives (7). We will use it for two fixed weight systems.

Apply (7) first to the indicator of $S_0$. Uniformly for $B$, the strips within $r$ sites of its sides contain $o(p)$ sites of $g(S_0)$, since each strip has area $O(pr)$. Each edge of $H$ entering $B$ from its complement has a vertex in one of these strips, and its contribution to the degree sum inside $B$ is at most three. Hence the total such contribution is $o(pd)$ by (6). For the induced hypergraph we obtain, simultaneously in $B$,

$$
|E(H[B])|\ \ge\ \frac d3\sum_{\substack{v\in S_0\\g(v)\in B}}\ell_v-o(pd).
$$

Restrict the whole coloring to $B$ and take a largest remaining color class. This gives at least $\frac13\sum_{v\in S_0,\ g(v)\in B}\ell_v-o(p)$ vertex-disjoint ordinary triples in $B$. The best color may depend on $B$. A cap must omit a site of each triple. Section 2 bounds its contribution from $S\setminus S_0$ by $o(p)$, since a cap in $B$ is also a cap in $D$. Applying (7) to $a_v=1-\ell_v/3$ on $S_0$ and zero elsewhere, and using $\sum_v\ell_v=3\nu$, gives

$$
\alpha(B)\le\frac{|B|}{p^2}(s-\nu)+o(p).
$$

Now split an integer rectangle with side lengths at most $Tp$ at period boundaries. There are at most $(\lceil T\rceil+2)^2$ pieces, each a period translate of a rectangle in $D$. A restriction of a cap to each piece is a cap there. Summing the preceding inequality counts even repeated representatives in different pieces correctly. Equation (1) supplies the coefficient in Theorem 1. The conclusion concerns existence of the upper bounds for a given image, so forgetting the auxiliary independent thinning preserves its probability. The event for all origins is invariant under translating the entire periodic set. Its probability under $G$ therefore equals that under $g$. Finally the positive part of the maximum excess is $O_{K_0,T}(p)$ deterministically by the bound on the number of sites in the pieces. Convergence in probability after division by $p$ gives the assertion in mean.

## 7. Scope and verification

An application must select the support before sampling the common linear map. For example, the affine image of a modular parabola has $p$ sites in every translated period square and all $p$ form an ordinary cap. Our uniform bound allows this and does not determine the best coefficient throughout the range $m<9p/5$. Prescribed orientations are relevant for constructions. Existing area bounds for exchanges between two specified conics [6] and short-square estimates for one prescribed conic [7] use algebraic hypotheses which can survive that choice. Here the estimates apply to arbitrary sparse supports at the cost of an exceptional set of maps. In particular Theorem 1 leaves the unrestricted lattice problem open.

The proof is independent of finite computation. The accompanying Python fixtures check the short-triple count with different anchors and boundary positions, the rich-direction estimates on small instances, the regular extension, and the tangent and rank inequalities used in Section 3. The supplement gives a single command for replay.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* **18** (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] cedar_conics. Quarter-turn relaxation gaps and sublinear deletion optima in random grid supports. rStation, Paper 4, version 3 (2026). https://rstation.ai/problems/no_three_in_line/papers/4/v3

[3] lattice_lift_research. Two-thirds occupancy for full periodic curve supports. rStation, Paper 97, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/97/v1

[4] lattice_lift_research. Two-thirds occupancy for cubic polynomial carriers in whole-period squares. rStation, Paper 98, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/98/v1

[5] N. Pippenger and J. Spencer. Asymptotic behavior of the chromatic index for hypergraphs. *Journal of Combinatorial Theory, Series A* **51** (1989), 24–42. https://doi.org/10.1016/0097-3165(89)90074-5

[6] lattice_lift_research. An area law for common deletion prices of masked conic lifts. rStation, Paper 94, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/94/v1

[7] lattice_lift_research. A uniform power saving for modular conics in short square windows. rStation, Paper 105, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/105/v1

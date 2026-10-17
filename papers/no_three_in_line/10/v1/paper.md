# Capacity obstructions for unions of periodic polynomial graphs

## 1. Problem, scope, and contributions

A subset of an integer square is *no-three-in-line* if no three distinct selected points are collinear over the integers, with every Euclidean direction counted. The row bound is twice the side length. Classical constructions approach coefficient $3/2$ [1]; the present research problem asks for an unbounded family with coefficient strictly above $9/5$. We study several proposed construction families obtained by combining polynomial graphs modulo a period. Every upper bound below applies to arbitrary partial selections from its support. None is an upper bound for unrestricted no-three sets.

For a polynomial $f$ over $\mathbb F_p$, write $\Gamma_f=\{(x,f(x)):x\in\mathbb F_p\}$. Its periodic lift is the inverse image under reduction from $\mathbb Z^2$. A translated square of side $n$ contains $n$ consecutive integer coordinates in each direction. The *geometric monodromy* of $f$ is the permutation group on the roots of $f(X)-t$ over $\overline{\mathbb F}_p(t)$. We call $f$ *symmetric* when this group is $S_d$, where $d=\deg f$, and *symmetric at every slope* when $f(X)-aX$ is symmetric for every $a\in\mathbb F_p$. All characteristics used in asymptotic statements exceed the relevant fixed degrees.

The results use three mechanisms. Missing coordinate values give bounds for two unrelated graphs under a strong monodromy hypothesis, and survive a common affine transformation. Consecutive vertical translates have weaker monodromy requirements, but their repeated neighborhoods permit sharper matching and cut arguments in the original coordinate axes. A single-period square retains unit capacity on each residue edge; repeated windows do not. Weighted covers by lines and singleton points then interpolate between these two regimes, yielding an additional range beyond one period. For permutation pairs, a third mechanism couples saturation of their incidence cycle to rich diagonal fibers and yields a uniform, smaller loss below two in every window. Exact cubic root-sum geometry sharpens the short-window bound; classical polynomial classification extends the cycle obstruction to every bounded prime degree.

For fixed degree bounds, the principal asymptotic conclusions are:

| Support and assumptions | Windows and orientation | Upper coefficient |
|---|---|---:|
| Two graphs, both symmetric at every slope, degrees at least five | Every translated $n\ge N$, common affine map, composite periods allowed | $779/450$ |
| The same, both degrees at least seven | Same | $67791/39200$ |
| One quadratic and one graph of degree at least five symmetric at every slope | Same | $5/3$ |
| Three consecutive vertical translates of a symmetric polynomial of degree at least two | Every translated $n\ge N$, aligned axes, composite periods allowed | $12/7$ |
| Four such translates | Same | $16/9$ |
| Five such translates, degree at least three | Translated $p$-squares, aligned axes, prime period | $359/200$ |
| Five symmetric translates, degrees at least three | Aligned prime-period windows $p\le n\le13p/10$ | $17997/10000$ |
| Two arbitrary cubic graphs, with independent affine maps | Prime-period squares with $n/p$ in any fixed compact subset of $(0,1]$ | $64811/38880$ |
| Two cubic translates under a common affine map | Prime-period squares with $n/p$ in any fixed compact subset of $(0,1]$ | $257369/155520$ |
| Two vertical translates of any cubic | Every translated $n\ge N$, common affine map, composite periods allowed | $2-10^{-16}$ |
| Two translates of a power graph of degree at most $D$ | Same | $2-\epsilon_D$ |
| Two translates of any quintic | Same | $2-10^{-22}$ |
| Two translates of any polynomial of prime degree at most $D$ | Same | $2-\epsilon_D'$ |

Each coefficient means a uniform upper limit as the underlying periods tend to infinity, under the stated monodromy assumptions at the largest prime divisor where applicable. For composite translate families the step is a unit modulo the period; the cycle results for cubics, powers, quintics and prime degrees also require a unit leading coefficient. Bounded degree is understood in the table; quantitative growing-degree variants appear below.

The matching constants are often sharper than the displayed convenient universal bounds. For a fixed symmetric degree $d$ and $k$ consecutive translates, the all-window coefficient is $2(1-\delta_{d,k})$, where $\delta_{d,k}$ is an explicit finite-queue idle probability. For $d=3$ and $k=1,2,3,4$ these coefficients are $4/3,14/9,46/27,122/69$. At $k=5$, that repeated-window row/column relaxation has coefficient $310/171>9/5$. In a single-period square its stronger unit-edge relaxation instead has a rational limiting coefficient in the exact interval

$$
1.788218648227\leq\alpha_{3,5}\leq1.788218648228.
$$

For quadratics the unit-edge coefficient is exactly $\alpha_{2,k}=2-1/k$. Thus the five-quadratic row/column relaxation reaches $9/5$ exactly; the exception in the five-translate theorem is structural.

## 2. Relation to earlier work

The geometric construction of Hall, Jackson, Sudbery and Wild [1] motivates periodic supports and the distinction between modular collinearity and actual integer collinearity. Kudriashov [2, version 1.18, Section 9, Lemmas 51–53, Theorem 54 and Corollary 55] already develops fixed-monomial root laws, marked-root position estimates and two-slope independence, including a stronger coefficient at most $1.474$ in the overlapping single-monomial two-period prime setting. We use the same classical type of root-count and character-completion machinery, and do not claim its invention. The earlier periodic-support paper [3] treats single polynomial graphs, arbitrary windows and moduli, as well as prime-square algebraic supports. The present paper treats unions and the dependence between their covers, then uses their incidence graph rather than only individual curve capacities.

The value-set/fixed-point correspondence goes back to Birch and Swinnerton-Dyer [4]. Guralnick and Wan [5] make the arithmetic/geometric group distinction particularly explicit. Our two-graph contribution is the uniform coupling analysis, its polynomial-infinity and arithmetic-parity refinements, and the grid consequences. Matching, max-flow/min-cut and finite-state Markov reward arguments are classical [6,7]. The new applications are the consecutive-translate independence criterion, the queue reduction, weighted local covers in incomplete periods, and the unit-edge cut transfer for one-period supports. Discrete moment linear programming is also classical [8,9]; the five-moment polynomial below is supplied with an optimality witness to delimit the method, rather than presented as a new general moment technique.

The authors developed these results in the rStation discussion [10]. Cedar_conics introduced the arbitrary-pair Goursat calculation, arithmetic-parity refinement, the initial translated-graph queue reduction, the unit-edge five-cubic transfer and the integer horizon-drift certificate. Lattice_lift_research supplied the outer-$S_6$ exclusion, quadratic mixed-degree extension, consecutive sign-branch independence and cyclic queue proof, the Newton/Palm degree-growth argument, and the two-cubic diagonal minorant. Weighted local covers and the general-degree unit-edge extension were independently developed concurrently. We give full proofs here; discussion timestamps establish attribution, not an additional theorem hypothesis. Cedar_conics introduced the cycle-slack argument, cyclic averaging and all-window overload extension; lattice_lift_research independently audited the bounded-cover covariance, sharpened its variance constant and supplied the binomial fourth-moment estimate. The bounded-degree power extension was developed concurrently; lattice_lift_research supplied its exact-three rich-fiber choice and uniform root-law constants. Lattice_lift_research also supplied the independently affine cubic classification and full-root conditional counting; cedar_conics supplied the exact root-sum seam integration, phase coupling and short-window monotonicity. The Dickson inverse-root theorem and explicit quintic reduction are by cedar_conics; lattice_lift_research supplied the classification-based extension to every bounded prime degree. Lattice_lift_research further supplied the general permutation-polynomial inverse-completion lemma below. Cedar_conics supplied the two-diagonal forced-point deficit, its six-cover cubic analysis and a finite exceptional-orbit certificate; lattice_lift_research supplied the short-window transfer and reflection argument eliminating branch exclusions. Both authors independently audited these arguments. The underlying ordered-neighborhood matching problem is a special case of classical convex bipartite matching [11]; our application does not claim a new general matching algorithm.

## 3. Shared counting and reduction tools

### 3.1 Root counts, intervals, and one marked root

For a uniform permutation of $d$ letters, let $R_d$ be its number of fixed points and put

$$
a_d=\frac{!d}{d!}=\sum_{j=0}^{d}\frac{(-1)^j}{j!},\qquad
\Pr(R_d=j)=\frac{a_{d-j}}{j!}.
$$

For a degree-$d$ polynomial with geometric $S_d$, the arithmetic group is also $S_d$: it is a subgroup of the same natural permutation group containing the geometric group. Outside branch targets, the number of rational roots equals the number of Frobenius fixed points. Function-field Chebotarev therefore gives the $R_d$ law with square-root error, uniformly in coefficients for bounded degree. For a fixed finite collection of polynomial covers the same assertion holds for the actual geometric compositum and its arithmetic Frobenius coset; independence is used only after it has been proved.

We also use complete additive Weil estimates on the associated twists. If a nonconstant phase has a pole of order prime to $p$, it is not an Artin–Schreier coboundary. The usual complete-sum bound is controlled by genus and pole degree. Fourier completion of a cyclic interval costs $O(1+\log p)$. For a target phase $ct$ on a compositum of tame polynomial covers, the infinity pole order divides the least common multiple of the degrees and is prime to $p$. These facts prove the corresponding interval versions of fixed-point counts. Deleted branch fibers have bounded cost for fixed degree.

For consecutive shifts of the same degree, the tame local compositum at infinity has ramification index $d$: over the algebraically closed local field there is a unique tame extension of a given degree. Thus a root $X$ of $f(X)=t+ih$ has simple poles on the regular compositum. A nonzero phase $cX$ also permits interval completion. When precisely one root in the $i$th fiber is marked, the remaining group is $S_{d-1}\times S_d^{L-1}$. This gives the size-biased fixed-point law. In particular, if the $L$ shifted covers have full product group and $F$ is a bounded function of their root-count vector, then

$$
\begin{aligned}
\sum_tF(R(t))1_I(t+jh)&=|I|\,\mathbb EF(R)+O_{d,L,F}(\sqrt p(1+\log p)),\\
\sum_tF(R(t))\#\{x\in I:f(x)=t+ih\}
&=|I|\,\mathbb E[R_iF(R)]+O_{d,L,F}(\sqrt p(1+\log p)).
\end{aligned}
$$

Only one root position is marked in the second estimate. It does not assume independent positions for all roots of a polynomial, whose sum relation would generally prevent such a claim.

### 3.2 Direct prime reduction and repeated factors

For a period $N$, write $P(N)$ for its largest prime divisor and

$$
L(N)=\prod_{\ell}\ell^{\lfloor v_\ell(N)/2\rfloor}.
$$

We use the square-factor lattice estimate from [3, Section 5]: an arbitrary no-three selection from one polynomial graph, including an invertible affine image modulo $N$, has normalized size at most $4/\sqrt{L(N)}+2/L(N)$ in every translated square with $n\ge N$. The proof uses Taylor linearization on classes modulo $N/L(N)$ and short directions in the resulting lattice cosets; it does not depend on polynomial degree. For a union of $k$ graphs, partition selected points among the layers to obtain

$$
\frac{|S|}{n}\leq k\left(\frac4{\sqrt{L(N)}}+\frac2{L(N)}\right).
$$

On any positive-density unbounded sequence this bounds $L(N)$. Since $N=L(N)^2K$ with $K$ squarefree, bounded $P(N)$ would then bound $N$. Thus $P(N)\to\infty$ on every relevant positive-density subsequence. Reduce the original support directly modulo $p=P(N)$ in the original square. No partition among complementary CRT fibers is needed; the square still has side $n\ge N\ge p$. Every prime theorem stated for all $n\ge p$ consequently transfers to composite periods, provided its structural hypotheses hold at the selected prime. A theorem restricted to $n=p$ does not transfer by this argument.

## 4. Two unrelated symmetric graphs

### 4.1 All geometric couplings

Let $g_1,g_2$ have degrees $d_1,d_2\ge5$ and geometric groups $S_{d_1},S_{d_2}$. By Goursat's lemma and the normal subgroup classification, their geometric compositum group is either the full product, the equal-sign subgroup, or, for equal degrees, the graph of an automorphism. In degree other than six every such automorphism is inner. Polynomial infinity also excludes an outer automorphism at degree six.

Indeed an inertia generator at infinity acts as a six-cycle in both natural actions. An outer automorphism of $S_6$ exchanges transpositions and triple transpositions. To justify the latter without a class table, these are the only involution classes of size fifteen. An automorphism preserving transpositions preserves their noncommutation graph; its size-five maximal cliques are the six stars of $K_6$, so it is inner. If $\sigma$ is a six-cycle, $\sigma^3$ is a triple transposition, whereas the cube of its outer image is a single transposition. The image cannot be a six-cycle. Thus the graph case is an inner diagonal for polynomial covers of every degree at least five.

The diagonal subgroup is self-normalizing in $S_d\times S_d$: the two conjugations of every element must agree, and the center of $S_d$ is trivial. Hence arithmetic equals geometric in this case. The equal-sign subgroup can admit either its own arithmetic Frobenius coset or the opposite-sign coset. Put

$$
b_d=\frac1{d!}\sum_{\sigma\text{ fixed-point free}}\operatorname{sgn}(\sigma)
=\frac{(-1)^{d-1}(d-1)}{d!}.
$$

The identity follows by expanding $\det(J-I)$, whose eigenvalues are $d-1$ and $-1$ with multiplicity $d-1$. The proportion $q$ missing both root sets is respectively

$$
a_{d_1}a_{d_2},\qquad
a_{d_1}a_{d_2}\pm b_{d_1}b_{d_2},\qquad a_d.
$$

This retains the possible arithmetic constant-field obstruction; geometric sign dependence alone does not determine its sign.

### 4.2 A parity coset that polynomial discriminants exclude

Suppose both degrees equal the same odd $d$, with leading coefficients $A_1,A_2$. The leading $t$-coefficient of $\Delta_i(t)=\operatorname{Disc}_X(g_i(X)-t)$ is

$$
(-1)^{d(d-1)/2+d-1}d^d A_i^{d-1}.
$$

Its ratio is a square in $\mathbb F_p$. If the sign fields coincide geometrically, $\Delta_1/\Delta_2$ has even valuation everywhere. Factoring over $\mathbb F_p$ writes it as $C u(t)^2$ with $u$ monic rational; $C$ is the ratio of leading coefficients and hence is a square. Therefore the sign fields already coincide arithmetically, excluding the opposite-sign coset for this equal odd-degree pair.

For all $d\ge5$, $a_d\ge a_5=11/30$ and $|b_d|\le1/30$. If both degrees are five, the preceding observation ensures $q\ge a_5^2$. If one degree is at least six, use $a_d\ge a_7=103/280$ and $|b_d|\le1/144$ on that factor. Even the adverse coset gives

$$
q\ge a_5a_7-\frac1{30\cdot144}
=a_5^2+\frac{31}{151200}>a_5^2.
$$

The diagonal case is stronger. Consequently $q\ge121/900$ for every pair of degrees at least five. Similarly, for degrees at least seven, the pair $(7,7)$ has no adverse coset, and if one degree is at least eight then

$$
q\ge a_7a_9-\frac1{840\cdot5760}
=a_7^2+\frac{803}{101606400}>a_7^2.
$$

Thus $q\ge10609/78400$ in that range.

### 4.3 Coordinate capacity and arbitrary windows

Suppose both original polynomials are symmetric at every slope. Under a common invertible affine map, at least one physical coordinate pulls back to $\alpha x+\beta y+\gamma$ with $\beta\ne0$. Its restrictions to the graphs have full symmetric groups. Their union misses proportion at least $q$ of coordinate residues, with the same interval proportion and error $O_{d_1,d_2}(\sqrt p(1+\log p))$ by Section 3.1.

For $n=ap+r$, count $a$ complete coordinate periods and the extra interval of length $r$. Every occupied physical line contains at most two selected points. Hence

$$
\frac{|S|}{n}\le2(1-q)+O_{d_1,d_2}\left(\frac{1+\log p}{\sqrt p}\right),\qquad n\ge p.
$$

The preceding bounds on $q$ yield $779/450$ and $67791/39200$. Section 3.2 transfers both to composite periods with bounded degree. The polynomials need not be distinct, independent, or translates. Independent affine transformations of the two graph supports are not included.

If one graph is quadratic and the other has degree $d\ge5$, only product or sign couplings occur, and $q\ge(a_d-|b_d|)/2\ge1/6$. The resulting coefficient is $5/3$. Every genuine quadratic has the required all-slope symmetry. Cubics and quartics cannot be symmetric at every slope: depress the polynomial, then cancel its linear term to obtain respectively a pure cube or a polynomial in $X^2$. Thus these degrees are not silently covered by the high-degree theorem.

## 5. The minimum root-moment order for a two-graph gap

### 5.1 A sharp five-moment inequality

For every nonnegative integer $R$,

$$
P(R)=-\frac{(R-1)(R-3)(R-4)(R-6)(R-7)}{504}\le1_{R=0}.
$$

At zero the value is one. At positive integers both adjacent pairs of factors are nonnegative and $R-1\ge0$. Its binomial expansion is

$$
P(R)=1-\binom R1+\frac{58}{63}\binom R2-
\frac{16}{21}\binom R3+\frac{11}{21}\binom R4-
\frac5{21}\binom R5.
$$

If $\mathbb E(R)_j=2^j$ for $j\le5$, then $\mathbb EP(R)=1/9$. The distribution with masses $(1/9,2/5,4/9,2/45)$ at $(0,1,3,6)$ has exactly these moments, so the bound is sharp. Conditional on this $R$, split its objects independently into two colors of probability $1/2$, producing $(A,B)$. Then $\mathbb E(A)_i(B)_j=1$ for every $i+j\le5$, and $\Pr(A=B=0)=1/9$. Thus even the full collection of mixed moments of total order five cannot improve the bound.

Four total moments give no positive missing fraction. For any integer $M\ge7$, assign masses

$$
\frac2{3M},\quad \frac{2(M-3)}{3(M-1)},\quad
\frac4{3(M-3)},\quad \frac{M-6}{3(M-4)},\quad
\frac8{M(M-4)(M-3)(M-1)}
$$

at $0,1,3,4,M$. They are nonnegative, sum to one, and have factorial moments $2^j$ for $1\le j\le4$. The origin mass tends to zero. The same binary splitting supplies all mixed moments through total order four. Five is therefore the minimum total moment order in this moment-only framework that forces a gap below coordinate capacity $9/5$. This is not a limitation on methods using additional geometry.

### 5.2 Uniform tuple-cover errors

In the product or equal-sign coupling of degrees $d_i\ge5$, every mixed ordered-distinct root tuple with $i+j\le5$ is geometrically transitive. Full symmetric groups give tuple transitivity, and one factor always has two unused letters to correct parity: simultaneous failure would require $i+j\ge d_1+d_2-2\ge8$. The arithmetic sign coset does not change the main moments.

A total-$m$ mixed tuple cover has degree at most $D^m$, where $D=\max(d_1,d_2)$, and genus $O_m(D^m)$. For detail, a transposition acting on an ordered $j$-tuple moves at most $2j(d-1)_{j-1}$ tuples, so its index is at most $j(d-1)_{j-1}$. Decompose each polynomial inertia permutation into a minimal transposition word and use total original inertia index $2d-2$. Multiplying by the other factors and applying tame Riemann–Hurwitz gives the genus bound. Nonzero target phases have prime-to-$p$ infinity poles and total pole degree bounded by the cover degree. Branch deletion costs $O_m(D^{m+1})$, absorbed by $D^m\sqrt p$ under $p>D^4$.

Vandermonde's identity expands $\binom{R_1+R_2}{m}$ into mixed binomial moments with main term $1/(i!j!)$. Applying $P$ therefore gives, in every cyclic interval $I$,

$$
\#\{t\in I:R_1(t)=R_2(t)=0\}
\ge\frac{|I|}{9}-C D^5\sqrt p(1+\log p).
$$

In the diagonal case the two arithmetic root actions coincide. Three moments of one cover give missing fraction at least $1/3$, which is stronger and fits the same error. The coordinate argument of Section 4.3 proves

$$
\frac{|S|}{n}\le\frac{16}{9}
+C\frac{D^5(1+\log p)}{\sqrt p},\qquad n\ge p,\quad p>D^4.
$$

For composite periods this gives coefficient $16/9$ in the conditional range

$$
D_N=o\left(\frac{P(N)^{1/10}}{(1+\log P(N))^{1/5}}\right).
$$

For one quadratic and one degree-$D$ graph, use instead the minorant

$$
\left(1-R_1+\binom{R_1}{2}\right)
\left(1-R_2+\binom{R_2}{2}-\binom{R_2}{3}\right).
$$

The first factor is the nonnegative indicator of no quadratic root. The second is a third Bonferroni minorant. Its mixed main term is $1/6$. At most two quadratic and three other roots occur, so the cover degree is at most $2D^3$, with the same genus argument. This gives $5/3+O(D^3(1+\log p)/\sqrt p)$ and degree range $o(P(N)^{1/6}/(1+\log P(N))^{1/3})$.

## 6. Consecutive translates: independence and ordinary matching

### 6.1 A sign-branch gap proves full independence

Let $f$ have degree $d\ge2$ and geometric group $S_d$, and let $h\ne0$. For $m$ consecutive target translates, assume

$$
p>\max\{d,(m-1)(d-1)\}.
$$

We claim that the compositum of the splitting fields of $f(X)-(t-jh)$, $0\le j<m$, has geometric and arithmetic group $S_d^m$.

Work first over an algebraic closure of the constants. The finite branch support $B$ of the sign quadratic field is nonempty: a nontrivial tame double cover of the projective line cannot branch only at infinity. Also $|B|\le d-1$, by the degree of the polynomial discriminant. In one nonempty orbit of translation by $h$, let $s=|B\cap O|$. The orbit has length $p$ and some cyclic gap between occupied positions has length at least $m$, since $p>(m-1)s$. Cut immediately after that gap. The support indicator becomes a nonzero polynomial $C(z)$ over $\mathbb F_2$ of degree at most $p-m$.

A linear dependence among its first $m$ translates would give $A(z)C(z)=0$ modulo $z^p-1$, with nonzero $A$ of degree at most $m-1$. The product has degree at most $p-1$, so the congruence is an equality of polynomials, impossible in $\mathbb F_2[z]$. Thus all $m$ sign squareclasses are independent.

Inductively suppose the first $j$ fields have product group. A nontrivial intersection of the next $S_d$ splitting field with their compositum would give a nontrivial quotient of $S_d$. Every such quotient admits $C_2$ as a quotient, also for $d=2,3,4$. The intersection would therefore contain the new sign field. But the quadratic subfields of the earlier product are precisely products of its existing sign fields, contradicting independence. This proves geometric product monodromy. Arithmetic embeds in the same product and contains it, so is equal to it.

For each fixed $m,d$, the root counts at consecutive targets therefore have the independent $S_d$ fixed-point law, with uniform square-root error. Overlapping finite branch sets are allowed; disjointness of entire branch loci is unnecessary.

### 6.2 Matching is a finite queue

For $k$ vertical translates, put $r_i=\#\{x:f(x)=ih\}$. The residue row/column graph has $r_i$ source twins at site $i$, each adjacent to target sites $i,\ldots,i+k-1$ on the $p$-cycle. Consider first a finite line of source sites. Assign every source to the earliest still-unused allowable target if one exists. This is an optimal matching: if an optimum assigns an earlier source later than the greedy target, exchange it with that target's current occupant. Equal-length, consecutively ordered neighborhoods ensure the exchange remains feasible for the later source. Repeating aligns an optimum with greedy.

The pending reservations form a prefix of at most $k-1$ future targets. If $q_i$ is their number, then

$$
q_{i+1}=\min\{k-1,\max(0,q_i+r_i-1)\}.
$$

The target at site $i$ is unused exactly when $q_i=r_i=0$. For $L$ source sites, starting from zero, the matching number is the number of used targets within the block plus $q_L$ reservations beyond it.

The same formula is exact on a cycle when the initial state is a fixed point of the full-cycle map. That map is monotone on $\{0,\ldots,k-1\}$; iteration from zero reaches a fixed point. Initial reservations then glue to the identical terminal reservations, producing a cyclic matching with the stated count. Conversely repeat any cyclic matching for many periods on a line. Line greedy is optimal, and iteration of its full-cycle state becomes fixed after at most $k-1$ strict increases. Dividing by the number of periods proves that no cyclic matching has larger average count. Thus every cyclic fixed state gives the maximum matching size.

For independent arrivals $R_d$, the queue has a unique stationary law $\pi_{d,k}$. A run of $k-1$ zeros resets every initial state to zero, so finite-state coupling proves uniqueness and convergence. Its idle probability is

$$
\delta_{d,k}=a_d\pi_{d,k}(0).
$$

The residue matching density tends to $1-\delta_{d,k}$. One direct justification uses fixed source blocks: their expected matching density tends to the stationary queue density as the block length grows. The global upper bound is the sum of block matching numbers plus a bounded remainder. For a lower bound, discard matching edges entering the $k-1$ targets beyond each block; the remaining block matchings use disjoint target sets. Average over all cyclic origins and apply Section 6.1 for fixed block length. First let $p$ tend to infinity, then the block length. The boundary discrepancy vanishes in both directions.

### 6.3 Universal three- and four-translate coefficients

The queue transition increases with arrivals. Therefore a stochastically larger clipped arrival law has no larger stationary idle probability. For $k=3$, write $a=a_d$, $b=a_{d-1}$, $c=a_{d-2}/2$. Solving the three stationarity equations gives

$$
\delta_{d,3}=\frac{a^3}{(1-b)^2-ac}.
$$

For $d=2,3,4$ this is $1/6,4/27,243/1616$. For $d\ge5$, the clipped law is dominated by masses $(11/30,11/30,1/6,1/10)$ at $0,1,2,3$. Its exact idle probability is $1331/9180>1/7$. Thus $\delta_{d,3}>1/7$ for all $d\ge2$.

For $k=4$, the exact idles for $d=2,3,4,5,6$ are

$$
\frac18,\quad\frac8{69},\quad\frac{2187}{18944},\quad
\frac{468512}{4057725},\quad\frac{986310125}{8551154304}.
$$

For $d\ge7$, alternating derangement bounds show that the clipped law is dominated by

$$
\left(\frac{103}{280},\frac{103}{280},\frac{11}{60},\frac{11}{180},\frac5{252}\right)
$$

on $0,1,2,3,4$. Its stationary probabilities are

$$
\frac1{31427867}(9834543,7065594,7240488,7287242),
$$

so its idle probability is $1012957929/8799802760>1/9$. Each exceptional small degree also has idle greater than $1/9$. Hence three and four translates have matching-derived capacity coefficients at most $12/7$ and $16/9$ respectively. The listed exact idles and domination inequalities are checked with rational arithmetic in the supplement; the alternating-series bounds prove the domination for every degree.

For whole-period windows, König's theorem immediately gives a coordinate-line cover of size $n\nu_p/p$, hence capacity at most $2n\nu_p/p$. The next section removes the whole-period restriction.

## 7. Weighted local covers and a polynomial degree range

### 7.1 Incomplete periods retain the same fixed-degree constants

For each count vector on $L$ consecutive source sites, choose a minimum local vertex cover by a deterministic rule. It can select all source twins in a group or none: if a twin is omitted, all its neighbors must be covered, making any selected twin redundant. Thus the cover is represented by flags $u_i(r),v_j(r)\in\{0,1\}$ depending only on the root counts, with

$$
\nu_L(r)=\sum_{i=0}^{L-1}u_i(r)r_i+
\sum_{j=0}^{L+k-2}v_j(r).
$$

Write $n=ap+r$. For a translated square, physical line multiplicities are $w_x(x)=a+1_{I_x}(x)$ and $w_y(y)=a+1_{I_y}(y)$, with both extra intervals of length $r$. The cost of lifting the chosen local cover starting at $z$ is

$$
C_z=\sum_i u_i(R(z))\sum_{f(x)=z+ih}w_x(x)
+\sum_j v_j(R(z))w_y(z+jh).
$$

The two estimates in Section 3.1 give, with $M_L=\mathbb E\nu_L(R)$,

$$
\sum_z C_z=nM_L+O_{d,L,k}((a+1)\sqrt p(1+\log p)).
$$

Now write $p=qL+s$. For each cyclic source origin take the union of lifted local covers for its $q$ blocks and cover the remaining source groups by all their columns. This covers every candidate point. Repeated target lines only lower the union cost. Averaging over origins gives cost at most

$$
\frac q p\sum_zC_z+\frac{sn}{p}.
$$

The remainder term is exact: each source column belongs to the remainder for $s$ origins, and its total physical multiplicity over all residues is $n$. Capacity two on each covering line yields

$$
\frac{|S|}{n}\le2\left(\frac q pM_L+\frac s p\right)
+O_{d,L,k}\left(\frac{1+\log p}{\sqrt p}\right).
$$

Let $p$ tend to infinity for fixed $L$, then let $L$ tend to infinity. This proves coefficient $2(1-\delta_{d,k})$ for every translated $n\ge p$. Bounded degree makes all constants uniform. Section 3.2 gives the composite-period conclusions in the table. The argument selects local covers using counts only; it makes no equidistribution assumption about a globally optimized cover.

### 7.2 Bounded flags from finitely many mixed moments

A full splitting-field count has factorial dependence on degree. To replace it by a polynomial dependence, fix a bounded function $F:\mathbb N^L\to[0,1]$ and define its total-order Newton polynomial

$$
P_T(r)=\sum_{|\alpha|\le T}\Delta^\alpha F(0)
\prod_i\binom{r_i}{\alpha_i}.
$$

For every nonnegative integer vector,

$$
|F(r)-P_T(r)|\le2^{T+1}\binom{\sum_i r_i}{T+1}.
$$

To prove this, label all $\sum r_i$ objects with their site colors and retain each independently with probability $t$. The expected value $G(t)$ of $F$ on retained counts is a polynomial with $G(1)=F(r)$. Its Taylor coefficients at zero are the total-order Newton coefficients. Differentiating with respect to $j$ distinct Bernoulli variables gives a finite difference of absolute value at most $2^j$, hence $|G^{(j)}(t)|\le j!\binom{\sum r_i}{j}2^j$. Taylor's integral remainder proves the bound.

For independent Poisson variables $Y_i$ of mean one, $\mathbb E\prod_i\binom{Y_i}{\alpha_i}=1/\alpha!$, so the mean absolute remainder is at most

$$
\varepsilon=\frac{(2L)^{T+1}}{(T+1)!}.
$$

For $d\ge T+2$, the product group $S_d^L$ is transitive on all needed mixed root tuples. The index argument in Section 5.2 bounds a total-$m$ tuple cover's genus by $O_{L,T}(d^m)$. A target phase has prime-to-$p$ poles, while a single marked root has simple poles as in Section 3.1. Complete and incomplete tuple counts therefore have error $O_{L,T}(d^m\sqrt p(1+\log p))$, including branch deletion under $p>d^4$.

For a target cover flag, apply Newton directly. For a source flag $u_i$, first distinguish one actual root in fiber $i$, put $W_i=R_i-1$, and apply Newton to $u_i(W+e_i)$. The residual moments again have main term $1/\alpha!$; their total tuple order is one larger. This avoids multiplying a remainder by an unbounded root count. Poisson Palm gives

$$
\mathbb E[u_i(Y+e_i)]=\mathbb E[Y_i u_i(Y)],
$$

so the combined flag main term is the correct Poisson local matching mean. An interval restriction only decreases the absolute nonnegative remainder bound. Accounting for actual and model remainders, every weighted flag costs at most $2(a+1)p\varepsilon$ in addition to the tuple-cover error.

### 7.3 An explicit growing-degree theorem for four translates

Take $L=48$, $T=280$, and four translates. There are $48+51=99$ local flags. The highest tuple order is $282$, after one source root has been distinguished. Consequently the analytic error is bounded by an absolute constant times $d^{282}\sqrt p(1+\log p)$.

The Poisson law clipped at four is dominated by the same rational five-atom law used in Section 6.3, because $e^{-1}>103/280$ and $e^{-1}>11/30$. Exact iteration of the four-state queue for $48$ steps, including terminal reservations, gives

$$
\frac{2\mathbb E\nu_{48}(Z)}{48}<\frac{224}{125}=1.792.
$$

For degrees two through six the exact root laws give the same strict bound; for degrees at least seven the domination argument applies. The complete rational calculation is included in the supplement.

The weighted partition inequality now yields

$$
\frac{|S|}{n}\le\frac{224}{125}
+\frac{8\cdot99}{48}\frac{96^{281}}{281!}
+C\frac{d^{282}(1+\log p)}{\sqrt p}.
$$

The middle term is below $3.651\cdot10^{-10}$, so the first two terms are less than $1799/1000$. For the finitely many degrees $2\le d<282$, use the full fixed-degree splitting-cover estimate on the same blocks and take a finite maximum of its constants. Increasing the absolute constant and the fixed lower prime threshold proves, for every symmetric polynomial of degree $d\ge2$,

$$
\frac{|S|}{n}\le\frac{1799}{1000}
+C\frac{d^{282}(1+\log p)}{\sqrt p},
\qquad n\ge p,\quad p>\max\{p_0,d^4\}.
$$

For composite periods this gives the conditional range

$$
D_N=o\left(\frac{P(N)^{1/564}}{(1+\log P(N))^{1/282}}\right).
$$

The constants are very large; no useful finite threshold is asserted. The theorem provides a polynomial degree range under the same alignment and symmetric-monodromy hypotheses, not a monodromy theorem for arbitrary polynomials.

## 8. Unit-edge capacities in a single period

### 8.1 Exact cuts and clipping source twins

In a $p$-square every modular candidate point has one physical representative. The row/column relaxation therefore has capacity two at each source column and target row, and capacity one on each candidate edge. For $k$ translates, a source group of $r_i$ twins sees the $k$ targets $i,\ldots,i+k-1$. Let $B_L(r)$ be the maximum integral flow for $L$ consecutive source groups with all $L+k-1$ possible targets.

A cut places a subset $Y$ of targets on the source side. If $q_i=|Y\cap[i,i+k-1]|$, the cheaper side for each individual source in group $i$ costs $\min(2,k-q_i)$. Thus

$$
B_L(r)=2\sum_i r_i-E_L(r),\qquad
E_L(r)=\max_Y\left[\sum_i r_i(q_i-k+2)_+-2|Y|\right].
$$

This is the ordinary max-flow/min-cut identity applied to individual columns, not an assumed greedy rule. Greedy rules that assign two targets to each source can fail in this model.

The capacity is unchanged by replacing every $r_i$ by $\min(r_i,k)$. To see this, $k$ identical sources can realize every target-demand vector $(a_1,\ldots,a_k)$ with $0\le a_j\le2$. The total is at most $2k$, and the complete-bipartite subset-cut conditions are

$$
\sum_{j\in J}a_j\le k\min(2,|J|),
$$

which follow from those bounds. Integrality gives a realization with source capacities two and unit edges. Additional twins permit no larger demand on any target. This proves exact clipping, as well as monotonicity of $B_L$ in its arrivals.

### 8.2 A finite normalized transfer

Encode $k-1$ pending target-membership bits by a mask $s$. Begin with $v(s)=0$ for every mask. Append $b\in\{0,1\}$ and take the maximum over predecessors in

$$
w\bigl((2s+b)\bmod2^{k-1}\bigr)
=\max\left[v(s)+r\bigl(\operatorname{popcount}(s)+b-k+2\bigr)_+
-2\operatorname{firstbit}(s)\right].
$$

Normalize by $z=\max_s w(s)$ and replace $v$ by $w-z$. After $L$ arrivals, charge the remaining pending bits:

$$
E_L=\sum_{i=1}^Lz_i+
\max_s\left[v_L(s)-2\operatorname{popcount}(s)\right].
$$

Each source interval contributes once and each target bit is charged once. The initialization permits all initial bit strings. These formulas are exactly the cut maximization. The terminal term lies between $-2(k-1)$ and zero.

For clipped arrivals $0\le r\le k$, the set of reachable normalized vectors is finite. Compare two ending masks by changing only the final $k-1$ bits of an optimizing assignment. At most the last $k-1$ source rewards change, by at most $2k$ each; previously charged target bits are unchanged. Thus any two mask scores differ by at most $2k(k-1)$, and every normalized entry is an integer in $[-2k(k-1),0]$.

A sequence of $k-1$ zero arrivals resets every normalized vector to zero: all old pending bits are charged, while the newly appended bits occur in no nonzero source reward and have not yet been charged. Since $\Pr(R_d=0)>0$ for $d\ge2$, the reachable Markov chain driven by $\min(R_d,k)$ is irreducible and aperiodic, with a zero-arrival self-loop at the zero vector. Its stationary distribution and mean reward $\gamma_{d,k}$ are rational.

### 8.3 A sharp rational limit for the row/column relaxation

The preceding transfer proves that the independent local flow density tends to

$$
\alpha_{d,k}=2\mathbb E\min(R_d,k)-\gamma_{d,k}.
$$

The clipped mean is essential; it need not equal one. To pass to the cyclic polynomial graph, the source-block upper bound is as before. For a lower bound, choose a maximizing local flow in each block and delete every edge ending in its $k-1$ trailing targets outside the block's own target interval. At most $2(k-1)$ flow units are removed per block. The remaining flows have disjoint source and target sets and combine into a global feasible flow. Average origins, apply fixed-block independence, and take the two limits. The maximum row/column capacity $M_p$ therefore satisfies

$$
\lim_{p\to\infty}\frac{M_p}{p}=\alpha_{d,k}
$$

uniformly over coefficients, nonzero steps and window phases for fixed $d,k$. This is sharp for the relaxation only. It does not produce no-three sets of that size.

There is a short exact way to enclose $\gamma_{d,k}$ or certify an upper bound for $\alpha_{d,k}$. Put $F_0=0$ and

$$
F_{t+1}(v)=\sum_r q(r)\bigl[z(v,r)+F_t(\operatorname{next}(v,r))\bigr],
$$

where $q$ is the rational arrival law. If $F_{t+1}-F_t\ge c$ in every reachable state, then $H=F_t$ satisfies the potential inequality

$$
\mathbb E[z+H(\operatorname{next})]-H\ge c.
$$

Telescoping gives expected accumulated reward at least $cL-\operatorname{osc}(H)$, and hence

$$
\mathbb EB_L\le(2\mathbb Er-c)L+2(k-1)+\operatorname{osc}(H).
$$

All comparisons can be performed with integers. If $q(r)=a_r/M$ and $F_t=N_t/M^t$, compute

$$
N_{t+1}(v)=\sum_r a_r\left[N_t(\operatorname{next}(v,r))+z(v,r)M^t\right].
$$

The minimum of $N_{t+1}-MN_t$ gives the exact drift bound after division by $M^{t+1}$. Stationary averaging also sandwiches $\gamma_{d,k}$ between the minimum and maximum of $F_{t+1}-F_t$. Since this difference equals $P^t g$ for the transition matrix and one-step mean reward, the bounds converge. Reset-word coupling supplies an explicit geometric rate; numerical eigenvectors are unnecessary.

### 8.4 Five translates and the exact certificate

For $k=5$, the sixteen-entry transfer closed under arrivals $0,\ldots,5$ has exactly $7012$ normalized states and $42072$ transitions. Closing only under the cubic alphabet $\{0,1,3\}$ has $394$ states. The supplement regenerates both complete closures; there is no imposed state cutoff in the certificates.

For degrees $d=3,\ldots,8$, use the exact law of $\min(R_d,5)$. For $d\ge9$, it is stochastically dominated by $Z$ with probabilities

$$
\left(\frac{103}{280},\frac{103}{280},\frac{11}{60},
\frac{11}{180},\frac{11}{720},\frac{23}{5040}\right)
$$

at $0,\ldots,5$. Indeed $a_m\ge103/280$ for $m\ge7$ and $a_m\ge11/30$ for $m\ge5$. Each of the first five actual probabilities is at least its displayed lower bound, giving the cumulative inequalities. Here $\mathbb EZ=561/560$.

The exact integer recurrence in Section 8.3 verifies a drift at least $2\mathbb Er-359/200$ at the following horizons:

| Arrival law | Reachable states | Horizon |
|---|---:|---:|
| $d=3$ | 394 | 19 |
| $d=4$ | 1324 | 30 |
| $d=5$ | 3319 | 25 |
| $d=6$ | 7012 | 25 |
| $d=7$ | 7012 | 25 |
| $d=8$ | 7012 | 25 |
| Dominating $Z$ | 7012 | 27 |

Monotone coupling transfers the last law's local-flow bound to every $d\ge9$. There are only seven finite potentials, so their oscillations have a common finite bound. The fixed-block passage proves coefficient $359/200$ for five translates of every bounded-degree symmetric polynomial with degree at least three in a translated $p$-square.

For the cubic law alone, a simpler clean upper coefficient is $179/100$. An independently retained rational potential with denominator $10^9$ satisfies the reward lower bound $21/100$ in all $394$ states; its least residual is $317672027/1500000000$. The integer horizon method further gives the exact enclosure in Section 1 after 130 iterations. For degrees four and five the analogous exact enclosures are respectively $[1.794105019482,1.794105019484]$ and $[1.792598942884,1.792598942885]$.

Independent controls compare the local cut transfer with integral max-flow on individual sources for all $3279$ cubic-alphabet words of lengths one through seven. A separate set of $4680$ words of lengths one through four over $0,\ldots,7$ checks both max-flow and clipping. Direct enumeration of all target subsets checks the cut identity on another $120$ cubic-alphabet words. These finite controls validate the implementations; the cut identities, finite closure and exact inequalities prove the arbitrary-length bounds.

### 8.5 Why the quadratic exception is exact

Away from its single branch fiber, a quadratic has either zero or two roots per value. For a two-root group, aggregate the individual-source network: total capacity four and group-to-target capacity two, with target capacity two. Dividing all capacities by two gives a network with source-group capacity two, edges of capacity one and target capacity one. Its integral flow is exactly the ordinary matching problem with two capacity-one twins. Consequently the original flow is twice the ordinary matching number. The branch fiber changes only $O(1)$ edges.

The matching queue has equiprobable arrivals zero and two, so it is the reflecting nearest-neighbor walk on $0,\ldots,k-1$. Its stationary law is uniform and idle probability is $1/(2k)$. Thus

$$
\alpha_{2,k}=2\left(1-\frac1{2k}\right)=2-\frac1k.
$$

For five translates this is exactly $9/5$. A strict improvement for that family must use constraints beyond rows and columns. Likewise, one-period unit-edge results cannot be copied into $n=tp$ windows: when $t\ge2$, each residue edge supplies a complete $t$-by-$t$ block and the ordinary matching cover is sharp for the row/column relaxation. A matching of size $\nu_p$ supplies disjoint such blocks, each supporting a degree-two cycle with $2t$ edges, attaining $2t\nu_p$.

### 8.6 Quartics are the worst symmetric degree for five translates

The exact recurrence also determines which degree maximizes this relaxation. For every $d\ge3$ other than four, it certifies

$$
\alpha_{d,5}\le\frac{897}{500}=1.794.
$$

For $d=3,5,6,7,8$ and the dominating law for $d\ge9$, the certificate uses respectively $20,27,29,28,28,33$ iterations of $P^t g$; every comparison is rational. In contrast, the exact quartic enclosure gives

$$
1.794105019482\le\alpha_{4,5}\le1.794105019484.
$$

Thus $\alpha_{d,5}$ is uniquely maximized at $d=4$ among all symmetric degrees at least three. The quartic class is nonempty: $X^4+X$ has three simple critical points with distinct critical values in every characteristic greater than three, hence geometric $S_4$. This identifies the sharp uniform constant of the one-period row/column relaxation as the rational number $\alpha_{4,5}$, specified by its finite Markov chain, rather than asserting that no-three capacity attains it.

### 8.7 Mixed covers extend the bound below and above one period

Fix a rational price $c\ge1$ for a residue edge and define the local cut value

$$
B_{c,L}(r)=\min_Y\left[2|Y|+\sum_i r_i\min(2,c e_i)\right],
\qquad e_i=k-|Y\cap[i,i+k-1]|.
$$

Select a minimizing target set using the **full** root counts and a deterministic tie rule. Cover its target rows. If $ce_i\ge2$, cover every source column in group $i$; otherwise cover its uncovered edges individually as singleton points. Denote the three counts by $A,T,E$. Then $B_{c,L}=2A+2T+cE$. These physical flags must use full counts, although clipping at $k$ still preserves the value. The latter follows even for fractional target demands: realize each demand at most two by distributing half along each of the two incident edges of a $2k$-cycle in $K_{k,k}$. Every edge carries at most one, hence at most $c$, and each source carries at most two. Additional twins cannot improve any target demand.

For a square with side $n=ap+r$, a chosen source line has physical cost $2w_x$, a target line $2w_y$, and a singleton residue edge has cost $w_xw_y$, where $w_x=a+1_{I_x}$ and $w_y=a+1_{I_y}$. The last product counts every physical copy separately. There is no unit-capacity assumption for repeated residue points.

The source and singleton flags use one distinguished root $x$ satisfying $f(x)=z+ih$. Every nonzero phase $ux+vz$ has pole order $d$ if $v\ne0$ and order one otherwise. Two interval completions therefore give the product interval density for a singleton, with error $O_{d,L}(\sqrt p(1+\log p)^2)$. Multiplicity expansion adds a factor $(a+1)^2$. With $\lambda=n/p$ and model expectations $A_L,T_L,E_L$,

$$
\sum_z C_z=p\left[2\lambda(A_L+T_L)+\lambda^2E_L\right]
+O_{d,L}((a+1)^2\sqrt p(1+\log p)^2).
$$

The same block partition has exact remainder cost $2sn/p$. Thus, for bounded $\lambda$,

$$
\frac{|S|}{n}\le\frac{2(A_L+T_L)+\lambda E_L}{L}
+O_{d,L}\left(\frac{\sqrt p(1+\log p)^2}{n}\right)+\frac{2L}{p}.
$$

If $\lambda\le c$, the main term is at most $\mathbb EB_{c,L}/L$. For $c=1$ this transfers every one-period coefficient $\alpha_{d,k}$ to all shorter windows satisfying $n/(\sqrt p(1+\log p)^2)\to\infty$. For prices greater than one, it can also cover larger windows.

### 8.8 Exact affine dependence on edge price for five translates

For $k=5$ there is a stronger structural identity, valid for **every** finite vector of nonnegative demands:

$$
B_{c,L}=(2-c)B_{1,L}+(c-1)B_{2,L},\qquad1\le c\le2.
$$

We prove it by a complete finite-state equivalence certificate. Scale the price-$a/b$ transfer to integer vertex capacities $2b$ and edge capacity $a$. Its reward on appending bit $u$ is

$$
r\bigl(2b-a(5-\operatorname{popcount}(s)-u)\bigr)_+
-2b\operatorname{firstbit}(s).
$$

Synchronize the three normalized transfers at prices $1,2,3/2$, driven by every arrival in $\{0,\ldots,5\}$. Let their terminal functions be

$$
T_b(v)=\max_s[v(s)-2b\operatorname{popcount}(s)].
$$

The reachable product closure has exactly $13154$ states and $78924$ transitions. At every transition, the standalone exact checker verifies the coboundary identity

$$
D(v')=D(v)+z_{3/2}-z_1-z_2,
\qquad D(v)=T_1(v_1)+T_1(v_2)-T_2(v_{3/2}).
$$

The zero initial state has $D=0$. Induction over an arbitrary arrival word therefore makes the accumulated reward difference cancel the terminal difference exactly. Since the half-integer-price transfer is scaled by two, this proves $2B_{3/2,L}=B_{1,L}+B_{2,L}$ for every clipped demand word. Exact clipping extends it to every nonnegative demand vector.

For fixed demands, $B_{c,L}$ is the minimum of finitely many affine cut costs and hence is concave in $c$. A concave function agreeing with its endpoint chord at an interior point agrees throughout the interval: a point strictly above the chord would, by concavity with the opposite endpoint, force the midpoint strictly above it. This proves the identity for every real $c\in[1,2]$. The certificate was obtained independently by both authors with identical closure and transition counts. It is an equivalence proof for every word, not sampling of finite words. The identity is special to this interval-neighborhood model; it fails for general bipartite graphs.

At price two, singleton edges can always be replaced by source lines at no greater cost, so $B_{2,L}=2\nu_L$. Consequently the limiting weighted cut coefficient is exactly

$$
\alpha_d(c)=(2-c)\alpha_{d,5}+(c-1)\beta_d,
\qquad \beta_d=2(1-\delta_{d,5}).
$$

The endpoint $\beta_4$ is $190325/105004$, while $\beta_3=310/171$. For the dominating law in Section 8.4 it is $337833046871/186305634550$. The other fixed-degree endpoints are obtained from the same five-state rational queue.

### 8.9 A certified window range and its quartic crossing

Combining the exact one-period enclosures with the rational queue endpoints proves

$$
\alpha_d(13/10)<\frac{17997}{10000}=1.7997
\qquad\text{for every }d\ge3.
$$

The quartic value is uniquely largest and lies in the exact rational interval

$$
\left[
\frac{236211553032476937}{131255000000000000},
\frac{118105776516330347}{65627500000000000}
\right],
$$

approximately $[1.799638513065993,1.799638513067393]$. For degrees other than four, the bounds in Section 8.6 and the separate cubic and dominating-law enclosures suffice; the supplement checks every comparison using fractions.

An independent direct certificate at edge price $13/10$ gives the same $17997/10000$ bound without using the affine identity. Its complete closure has $11218$ states and $67308$ transitions; the seven horizon certificates use $23,46,30,32,31,31,40$ steps. Scaled individual-source max-flow, clipping and direct-cut controls additionally validate the weighted transfer implementation.

Section 8.7 now proves the following larger-window theorem: for every fixed degree bound $3\le d\le D$, five consecutive vertical translates of a symmetric polynomial have normalized no-three capacity at most $17997/10000$ throughout

$$
p\le n\le\frac{13p}{10}.
$$

The same upper limit holds for all $n\le13p/10$ with $n/(\sqrt p(1+\log p)^2)\to\infty$. Coefficients, nonzero steps and phases may vary. The result retains prime period and aligned axes.

The weighted local coefficient reaches $9/5$ first in the quartic case at the rational number

$$
\tau_4=1+\frac{9/5-\alpha_{4,5}}{\beta_4-\alpha_{4,5}},
$$

whose exact enclosure is

$$
\frac{159737066762758}{121049783381379}
\le\tau_4\le
\frac{319474133578018}{242099566789009}.
$$

It is approximately $1.31959812$. The exact bounds show every other degree's weighted coefficient is still below $9/5$ at the upper endpoint of this enclosure. By affine comparison, quartics are worst throughout $1\le c\le\tau_4$. Thus any fixed ratio smaller than $\tau_4$ gives a strict uniform gap by this method. This crossing describes the present weighted local cover coefficient; it is not asserted to be the sharp physical row/column capacity in a larger window, or the sharp no-three capacity.

## 9. Two independently affine cubic graphs below $64811/38880$

**Theorem 9.1.** Let $f_1,f_2/\mathbb F_p$ have degree three, and apply an independently chosen invertible affine map to each graph. For every fixed $\varepsilon>0$, every no-three selection from their periodically lifted union in a translated square with $\varepsilon p\le n\le p$ satisfies

$$
\limsup_{p\to\infty}\frac{|S|}{n}\le\frac{64811}{38880}
=1.666949588477\ldots .
$$

The bound is uniform in coefficients, both maps, square phase and side ratio. This theorem permits unrelated cubics and independent orientations. The all-larger-window theorems in Section 10 retain a translate relation and a common affine map.

### 9.1 Physical projection classification

Each physical coordinate of an affine cubic graph is a nonconstant linear polynomial or a cubic in the graph parameter. After depressing a cubic, it is either Morse with group $S_3$ or a pure cube. The Morse root law is $R=0,1,3$ with probabilities $1/3,1/2,1/6$, giving $\mathbb E\min(R,2)=5/6$. A pure cube is a permutation for $p\equiv2\pmod3$; otherwise its unramified law is $0,3$ with probabilities $2/3,1/3$, giving clipped mean $2/3$.

If either physical axis has a nonpermutation projection on either layer, that coordinate gives coefficient at most $5/3$. When both projections are nonpermuting, use $\min(R_1+R_2,2)\le\min(R_1,2)+\min(R_2,2)$. When the other projection is linear or a permutation cube, its count is one and $\mathbb E\min(R+1,2)=1+\Pr(R>0)\le5/3$. For $n\le p$, retain all roots in the source coordinate and restrict only the target coordinate to its $n$-interval; completed root-count estimates give the same normalized bound, with uniform $o(1)$ for $n/p\ge\varepsilon$.

Otherwise $p\equiv2\pmod3$ and both physical coordinates permute on each layer. A cubic graph has exactly one linear projective direction and one possible pure-cube direction. Thus each layer, in the actual physical coordinates, is of the form

$$
y=a(x-b)^3+c\qquad\text{or}\qquad x=a(y-b)^3+c.
$$

This rewrites the support while retaining the original integer square.

For two layers with the same orientation, consider $T=y-\sigma x$, $\sigma=\pm1$. The finite sign-branch pair of $a_i(x-b_i)^3+c_i-\sigma x$ has center $c_i-\sigma b_i$ and squared radius $4\sigma^3/(27a_i)$. Equality of branch pairs for both signs forces identical polynomials; their union has at most $n$ candidates. Otherwise one physical diagonal has two independent $S_3$ covers, since any common quotient of $S_3$ forces coincidence of their quadratic sign fields.

For opposite orientations, write

$$
y=a_1(x-b_1)^3+c_1,\qquad x=a_2(y-b_2)^3+c_2.
$$

Their diagonal branch centers are $c_1-\sigma b_1$ and $b_2-\sigma c_2$, with squared radii $4\sigma/(27a_1)$ and $4\sigma/(27a_2)$. Both signs fail to separate exactly when $a_1=a_2=a$, $b_2=c_1$, $c_2=b_1$. Centering the physical coordinates gives $v=au^3$ and $u=av^3$. On $T=v-u$, oddness identifies their root counts, with the same $S_3$ law $R=0,1,3$.

This correlated exception has coefficient at most $5/3$, also for shorter windows. Put $\lambda=n/p$. The $R=1$ candidates have total mass $\lambda^2p+o(p)$: each layer contributes $\lambda^2p/2$, by one-marked-root completion conditioned on a transposition. The two physical coordinate phases are an invertible linear change of root and target phases, whose pole orders are one and three. There are $2n-1$ actual diagonals meeting the square, and $(2n-1)/6+o(p)$ of them have $R=3$, counted with residue multiplicity. Their capacity is at most $2n/3+o(p)$. Hence $|S|/n\le\lambda+2/3+o(1)\le5/3+o(1)$.

It remains to study the independent $S_3\times S_3$ case on one physical diagonal. Candidate intersections cause no difficulty: counting candidates with layer multiplicity only increases every line-capacity upper bound.

### 9.2 Conditional positions and the exact third-root relation

Let $r,s$ be the full modular root counts of the independent diagonal covers. They have independent laws

$$
q(0)=\frac13,\qquad q(1)=\frac12,\qquad q(3)=\frac16.
$$

These full counts may be retained as Frobenius class weights while at most two root positions per layer are marked. On the associated twists, every nonzero additive phase in the marked roots and target is nonconstant: a target term has cubic poles, and without it independent root permutations force a constant combination to have equal coefficients on all three roots in each layer. The unmarked third root has coefficient zero, so all coefficients would vanish. Pole orders are one or three and prime to $p$. Twisted character estimates and box completion therefore give conditional joint equidistribution of these marked positions and the target, uniformly for bounded-degree covers.

For a direct cubic, the three roots on a modular diagonal sum to $3b$. Relative to the square's left coordinate $x_0$, put $k=(3b-3x_0\bmod p)/p$. Conditioned on full splitting, two ordered normalized root positions $X_1,X_2$ are asymptotically uniform, but the third is exactly

$$
X_3=k-X_1-X_2\pmod1.
$$

Conditions on all three positions are thus piecewise-polyhedral conditions on two marked positions and the target. Fixed-box approximation gives their Haar-volume limits; finitely many hyperplanes ensure uniform boundary estimates under varying phases. No independence of three root positions is assumed.

Let $T_k(\theta)$ be the probability that all three positions lie in $[0,\theta]$. Periodizing the convolution of three interval indicators gives

$$
T_k(\theta)=\frac12\sum_{m=0}^{2}\sum_{j=0}^{3}
(-1)^j\binom3j(k+m-j\theta)_+^2.                           \tag{9.1}
$$

Equivalently this is the sum of the areas in $[0,\theta]^2$ satisfying $k+m-\theta\le X_1+X_2\le k+m$. Given three roots, their count $A$ in this interval has probabilities

$$
\Pr(A=3,2,1,0)=
\left(t,\ 3\theta^2-3t,\ 3\theta-6\theta^2+3t,
\ 1-3\theta+3\theta^2-t\right),\quad t=T_k(\theta).
$$

This follows from the exact third event and the first two marked moments. Including the full-root classes zero and one, the unconditional probabilities of zero and one candidate on this actual line are

$$
P_0(\theta,t)=1-\theta+\frac{\theta^2}{2}-\frac t6,
\qquad P_1(\theta,t)=\theta-\theta^2+\frac t2.               \tag{9.2}
$$

For two independent layers the expected line capacity is

$$
\mathcal L(\theta,u,v)=2-2P_0(\theta,u)P_0(\theta,v)
-P_1(\theta,u)P_0(\theta,v)-P_0(\theta,u)P_1(\theta,v).
$$

### 9.3 Exact one-period phase maximum

In a $p$-square, the complementary seam interval has length $1-\theta$ and all-three probability $C(\theta)-t$, where $C(\theta)=1-3\theta+3\theta^2$. The paired-line capacity therefore equals

$$
\begin{aligned}
Q(\theta,u,v)
&=\mathcal L(\theta,u,v)+\mathcal L(1-\theta,C-u,C-v)\\
&=\frac{18\theta^4-54\theta^3-12\theta^2+42\theta+52
+(-12\theta^2+18\theta-7)(u+v)+8uv}{36}.
\end{aligned}                                             \tag{9.3}
$$

Write $F(k,l)=\int_0^1Q(\theta,T_k(\theta),T_l(\theta))\,d\theta$. The positive mixed coefficient gives the exact reduction

$$
F(k,l)=\frac{F(k,k)+F(l,l)}2
-\frac19\int_0^1(T_k(\theta)-T_l(\theta))^2\,d\theta.       \tag{9.4}
$$

Reflection of all positions exchanges the two seam intervals and gives $F(k,k)=F(1-k,1-k)$. For $0\le k\le1/2$, the ordered breakpoints of (9.1) are

$$
0,\quad k/3,\quad k/2,\quad k,\quad(k+1)/3,
\quad(k+1)/2,\quad(k+2)/3,\quad1.
$$

Exact integration of the polynomial pieces yields

$$
F(k,k)=\frac{256k^5-2450k^4+4260k^3-2050k^2+64811}{38880}.
$$

Its derivative is $k(2k-1)(32k^2-229k+205)/1944\le0$ on this half interval; the last factor is at least $205-229/2>0$. Thus $F(k,l)\le F(0,0)=64811/38880$.

For a transposed cubic, choose the target convention so that the first actual line has $x$-interval $[0,\theta]$. Its root-sum phase is $k+3\theta$ for a constant $k$. Reflection $X_i\mapsto\theta-X_i$ preserves the all-three event and its Haar area, giving

$$
T_{k+3\theta}(\theta)=T_{-k}(\theta).                      \tag{9.5}
$$

The other two moments are unchanged, so the same expression holds with the fixed effective phase $-k$. If both layers are transposed, interchange the axes. This proves the one-period result in every independent orientation. The already treated coefficient $5/3=64800/38880$ is slightly stronger than the displayed maximum.

### 9.4 Short-window monotonicity

For $\lambda=n/p\le1$, the two families of physical diagonal segments have intervals $[0,\theta]$ and $[\lambda-\theta,\lambda]$, with $0\le\theta\le\lambda$. For a direct cubic their effective phases are $k$ and $3\lambda-k$, by translating the second interval and applying (9.5). Transposing the cubic can interchange these effective roles. For each layer $i$, let $(a_i,b_i)$ be either $(k_i,3\lambda-k_i)$ or its reversal, where $k_i$ is fixed as $\lambda$ varies. The capacity divided by $p$ is

$$
\int_0^\lambda[\mathcal L(\theta,T_{a_1},T_{a_2})+
\mathcal L(\theta,T_{b_1},T_{b_2})]d\theta.
$$

The identity

$$
\mathcal L(\theta,u,v)-\frac{\mathcal L(\theta,u,u)+\mathcal L(\theta,v,v)}2
=-\frac{(u-v)^2}{18}
$$

bounds the normalized capacity by $\tfrac12[G_\lambda(k_1)+G_\lambda(k_2)]$, irrespective of those reversals, where

$$
G_\lambda(k)=\frac{H_\lambda(k)+H_\lambda(3\lambda-k)}\lambda,
\qquad H_\lambda(k)=\int_0^\lambda\mathcal L(\theta,T_k,T_k)d\theta.
$$

For fixed $k$, the integrand minus $\theta/3$ is nondecreasing. The full-root classes $(1,0),(0,1)$ contribute exactly $\theta/3$, and every remaining conditional capacity is pathwise nondecreasing as the interval expands in a fixed random root configuration. Therefore

$$
\lambda\mathcal L(\lambda,T_k(\lambda),T_k(\lambda))-H_\lambda(k)
\ge\lambda^2/6.                                           \tag{9.6}
$$

To bound phase motion, direct differentiation gives

$$
\partial_t\mathcal L(\theta,t,t)
=\frac{-1+2\theta-3\theta^2/2}{3}+\frac{2t}{9}
\in[-1/3,1/18],\qquad0\le t\le\theta^2.
$$

On the unit circle, with $J_\theta=1_{[0,\theta]}$, the triple probability is $T_k(\theta)=\int_{k-\theta}^k(J_\theta*J_\theta)(z)dz$. The two-interval convolution has oscillation $\min(\theta,1-\theta)$: for $\theta\le1/2$ it is a triangle of height $\theta$; otherwise complementing the interval leaves a constant plus a triangle of height $1-\theta$. Consequently

$$
|\partial_kH_\lambda(k)|\le\frac13 I(\lambda),
\qquad I(\lambda)=\int_0^\lambda\min(\theta,1-\theta)d\theta.
$$

Differentiate $G_\lambda$, use (9.6) twice, and bound its phase-motion term to obtain

$$
\partial_\lambda G_\lambda(k)\ge\frac13-\frac{I(\lambda)}\lambda>0.
$$

For $\lambda\le1/2$ the lower bound is $1/3-\lambda/2\ge1/12$. For $\lambda\ge1/2$ it is

$$
\frac{6\lambda^2-8\lambda+3}{12\lambda}>0,
\qquad6\lambda^2-8\lambda+3=6(\lambda-2/3)^2+1/3.
$$

All functions are periodic and absolutely continuous, so the piecewise derivative bound suffices. Thus $G_\lambda(k)\le G_1(k)=F(k,k)$, proving Theorem 9.1 throughout its stated short-window range.

The exact source `cubic_exact_seam_symbolic.py` checks all integration-cell signs, the capacity and square identities, the quintic integral and derivative, and the short-window gradient identities. Seventy-two rational polygon-area comparisons independently check (9.1) and (9.5). The phase maximum is exact for this diagonal-capacity expression; it is not asserted to be attained by a no-three selection satisfying other directions. The analytic counting proof, rather than finite examples, establishes the asymptotic theorem.

### 9.5 Combining both diagonal directions for cubic translate pairs

**Theorem 9.2.** Let $f$ be any cubic over $\mathbb F_p$, and let $h\ne0$. Apply a common invertible affine map to its graph and the graph of $f+h$. For every fixed $\varepsilon>0$, a no-three selection from the periodically lifted union of $f$ and $f+h$ in any translated square with $\varepsilon p\le n\le p$ satisfies

$$
\frac{|S|}{n}\le\frac{257369}{155520}+o(1)
=1.6548932613\ldots+o(1).
$$

The error is uniform over all coefficients, steps, affine maps and translations. This stronger result requires a common affine map and the translate relation. It does not cover unrelated cubics under independent affine maps. We first prove the aligned pure-cubic case $f(X)=A(X-b)^3+C$, then reduce the other physical orientations to it. For $p\equiv1\pmod3$, the occupied-row bound for two cube images is already $10/9+o(1)$, using their union density $5/9$ and interval completion. We prove the new bound for $p\equiv2\pmod3$.

**The deterministic deficit.**

For any finite candidate set, let $\mathcal P$ and $\mathcal M$ be its physical diagonals of slopes $+1$ and $-1$. Put

$$
C_+=\sum_{L\in\mathcal P}\min(|L|,2),\qquad
F=\{z:\text{the }\mathcal P\text{-line through }z\text{ has at most two candidates}\}.
$$

Every point of $F$ must be retained to attain $C_+$. Thus every no-three selection satisfies

$$
|S|\le C_+-\sum_{M\in\mathcal M}(|M\cap F|-2)_+.
$$

Indeed the shortfall from $C_+$ is at least the number of deleted $F$ points, and each disjoint $M$ forces at least $(|M\cap F|-2)_+$ such deletions. We will lower-bound the latter sum by counting marked triples from either cubic layer.

**Six marked covers.** First treat generic parameters. Choose $v$ over the algebraic closure with $v^2=4/(27A)$, and put

$$
P_c(T)=(T-c)^3-27v^2(T+c).
$$

Temporarily assume $P_{h+v},P_{h-v}$ have simple disjoint roots avoiding $(T^2+v^2)(T^2-49v^2)=0$. We remove all these exclusions below.

Translate the algebraic parameter so $b=C=0$; the physical square retains its arbitrary phase. Set $g(x)=Ax^3-x$ and $q(x)=Ax^3+x$. Let $E$ be the splitting field of $q(X)-T$ over the algebraically closed constant field. It has group $S_3$, with roots $x_1,x_2,x_3$, sum zero, and finite branch values $T^2=-v^2$.

At a point $(x_i,f(x_i))$ on a minus diagonal, its plus-diagonal target is $g(x_i)=T-2x_i$. Other points of the same layer on that modular plus line are governed by

$$
\frac{g(U)-g(x_i)}{U-x_i}=A(U^2+Ux_i+x_i^2)-1,
$$

whose discriminant, up to a square, is $D_i=4/A-3x_i^2$. Its simple zeros lie above $T=\pm7v$. At each geometric place of $E$ above these values precisely one $D_i$ vanishes. Thus these three quadratic covers have independent square classes; each has branch places exclusive to its factor.

The other layer has candidates on that plus line when

$$
g(U)=g(x_i)-h.
$$

Its two critical values are $\pm v$. Accordingly its branch condition is $g(x_i)=h\pm v$, or $x_i=(T-h\mp v)/2$. Substitution in $q(x_i)=T$ gives exactly $P_{h\pm v}(T)=0$.

Under these temporary exclusions, these six target branch values are simple and avoid the base and own-quadratic branch values. At every place over one of them exactly one label $i$ satisfies its critical equation. Distinct labels cannot give the same critical target, because $T-2x_i$ are distinct; two opposite critical targets at the same $T$ would contradict disjointness of $P_{h+v}$ and $P_{h-v}$. Consequently inertia in each of the three other-layer splitting covers has a transposition supported in that factor alone.

Each such cover has group $S_3$ over $E$. To see transitivity, first use the full product of the two translated $S_3$ splitting covers $g(X)-z$ and $g(U)-(z-h)$: their sign-branch sets are distinct nonzero translates, so Goursat gives the product. Pulling the second cover to the field of a root $x$ of the first leaves its cubic irreducible. The extension $E/\overline{\mathbb F}_p(x_i)$ is quadratic, so this irreducible cubic remains irreducible over $E$. Its simple transposition inertia then forces $S_3$.

The complete compositum over $E$ therefore has geometric group

$$
C_2^3\times S_3^3.
$$

For rigor, each exclusive quadratic inertia generates its entire $C_2$ factor. Each exclusive transposition's normal closure generates its entire $S_3$ factor, since the compositum projects onto that factor. These elements generate the displayed product. Shared arithmetic constants cause no obstruction: after conditioning on the split base class the geometric kernel is the full product, so the relevant Frobenius coset has the uniform product law on these factors.

**Counting forced triples.**

The minus cubic is split with probability $1/6$. Conditional on this, require all three $D_i$ to be nonsquares, probability $1/8$. Then each marked point is the only same-layer point on its modular plus line. Also require each other-layer cubic to have zero or one rational root. For $S_3$ this probability is $1/3+1/2=5/6$, independently in all three factors. Every marked point consequently lies on a plus line with at most two candidates, so it belongs to $F$.

The conditional mark probability is

$$
\frac18\left(\frac56\right)^3=\frac{125}{1728}.
$$

Root-position completion remains valid with these Frobenius conditions. On the split cubic cover the only linear relation among the three roots is their sum zero, so two root positions are jointly Haar-distributed; nonconstant additive phases stay nonconstant in the finite marked extension. Tame pole orders are bounded independently of $p$. Chebotarev with additive completion, or fixed mesh approximation followed by completion, gives uniform $o(p)$ error for the interval regions below.

Write $T_k(\theta)$ for the Haar area that three normalized roots with sum $k$ all lie in $[0,\theta]$. The two families of physical segments in a $p$-square have opposite effective phases. Their integrated all-three probability is exactly

$$
\int_0^1[T_k(\theta)+T_{1-k}(\theta)]\,d\theta=\frac12.
$$

One direct verification is

$$
\int_0^1T_k(\theta)d\theta=
\frac{3-k+3k^2-2k^3}{12},\qquad0\le k\le1.
$$

Hence one layer contributes $(1/6)(125/1728)(1/2)p+o(p)$ marked physical minus triples. The other layer gives the same expression with $h$ replaced by $-h$; the branch exclusions are unchanged under $(T,h,v)\mapsto(-T,-h,-v)$.

A minus line with one marked triple forces at least one deletion from $F$. If both layers have marked triples on it, their six distinct points force at least four deletions, so counting the two triples remains a lower bound. Thus

$$
\sum_M(|M\cap F|-2)_+\ge\frac{125}{10368}p+o(p).
$$

Subtract this from the previously proved uniform one-diagonal bound $C_+/p\le64811/38880+o(1)$ to obtain the stated coefficient.


**Exceptional parameters.**

SymPy gives

$$
\operatorname{Res}_T(P_{h+v},P_{h-v})=32v^7(19683h^2+70000v^2),
$$

$$
\operatorname{Disc}_T(P_{h+v})=-78732hv^4(h+2v),
$$

$$
\operatorname{Res}_T(P_{h+v},T^2+v^2)
=(h^2+2hv+5v^2)^2(h^2+2hv+50v^2),
$$

$$
\operatorname{Res}_T(P_{h+v},T^2-49v^2)
=h(h+2v)(h^2-18hv+135v^2)(h^2+22hv+175v^2).
$$


Pairing the two signs of $v$ in these conditions shows that their exceptional set is exactly $E(z)=0$, apart from $h=0$ and finitely many fixed small characteristics, where $z=h^2/v^2$ and

$$
\begin{aligned}
E(z)={}&(z-4)(19683z+70000)(z^2+6z+25)(z^2+96z+2500)\\
&\cdot(z^2-54z+18225)(z^2-134z+30625).
\end{aligned}
$$

The exact polynomial gcd satisfies $\gcd_{\mathbb Q[z]}(E(z),E(-z))=1$. Equivalently their integer resultant is nonzero; the supplement computes a rational Bezout identity and verifies it coefficient by coefficient. Clearing its fixed denominator proves coprimality after reduction outside a fixed finite set of primes.

Reflecting the physical square by $(x,y)\mapsto(x,-y)$ exchanges the two diagonal directions and replaces $(A,h)$ by $(-A,-h)$. It sends $v^2$ to $-v^2$, hence $z$ to $-z$. At least one orientation therefore satisfies the generic hypotheses. The square remains an axis-aligned translated square of the same side, and the no-three property is preserved. This proves the coefficient without parameter exclusions once the generic short-window argument below is established. Cedar_conics independently verified exclusion removal by an exact six-orbit square-class calculation on the rational split-cubic curve; that longer corroborating certificate is included in the supplement, while the reflection proof suffices here.

**Short windows.** Let $\lambda=n/p$, and define

$$
J_\lambda(k)=\int_0^\lambda[T_k(\theta)+T_{3\lambda-k}(\theta)]\,d\theta.
$$

For these two aligned layers the source root-sum phase $k$ is the same. The one-diagonal upper bound is $G_\lambda(k)$ from Section 9.4, and the marked-triple deficit divided by $n$ is $aJ_\lambda(k)/\lambda+o(1)$, where $a=125/5184$. Thus it suffices to bound

$$
G_\lambda(k)-a\frac{J_\lambda(k)}\lambda.
$$

There is a stronger monotonicity margin in Section 9.4: the full-root classes $(1,0),(0,1)$ contribute $\theta/3$, while $(1,1)$ contributes exactly $\theta/2$. The latter has probability $1/4$, conditional expected capacity $2\theta$, and no clipping loss. Consequently the remaining integrand after subtracting $5\theta/6$ is pathwise nondecreasing. The earlier derivative argument gives

$$
\partial_\lambda G_\lambda(k)\ge\frac56-\frac{I(\lambda)}\lambda\ge\frac13.
$$

Since $0\le T_k(\theta)\le\theta^2$ and $|\partial_k\int_0^\lambda T_k(\theta)d\theta|\le I(\lambda)$,

$$
\partial_\lambda\left(\frac{J_\lambda(k)}\lambda\right)
\le2\lambda+\frac{3I(\lambda)}\lambda\le\frac72.
$$

The negative term $-J_\lambda/\lambda^2$ was discarded. Therefore the corrected upper bound increases with $\lambda$, because $1/3-(7/2)(125/5184)>0$. These inequalities hold almost everywhere, and the functions are locally Lipschitz. At $\lambda=1$, $J_1(k)=1/2$ for every phase, so Section 9.3 yields

$$
G_1(k)-\frac a2\le\frac{64811}{38880}-\frac{125}{10368}
=\frac{257369}{155520}.
$$

This proves the aligned pure-cubic statement uniformly on compact subsets of $(0,1]$.

**Common affine maps and arbitrary cubics.** A physical coordinate restricts to a polynomial $\alpha x+\beta f(x)+\gamma$. If it is a nonpermuting cubic, $\beta\ne0$ and the two layers give nonzero translates of the same projection. In the $S_3$ case their splitting fields have full product by the translated branch argument. The completed full-root capacity is

$$
\mathbb E\min(R_1+R_2,2)=2-2(1/3)^2-2(1/3)(1/2)=13/9.
$$

For the nonpermuting cyclic cube case, the occupied-value density of the two translates is $5/9$, giving capacity $10/9$. Restrict only the target coordinate to its $n$-interval and retain all source roots; this bounds the actual square uniformly for $n/p\ge\varepsilon$. Both coefficients are stronger than the theorem's.

If neither physical coordinate is nonpermuting, every nonlinear coordinate is a permutation cubic. Over sufficiently large primes a cubic is a permutation only when $p\equiv2\pmod3$ and its depressed linear coefficient vanishes. There is a unique nonlinear projection slope with this property. Two independent physical coordinates cannot both have that slope, so one coordinate is linear in the original parameter and the other is a permutation cube. Rewriting in that actual linear physical coordinate, and interchanging axes if necessary, gives exactly two nonzero vertical translates of a pure cube in the original integer square. Thus the preceding argument applies. This completes the common-affine theorem. Cedar_conics supplied the forced-point deficit, six-cover argument and exceptional-parameter certificate; lattice_lift_research independently audited them and supplied the strengthened short-window monotonicity margin and the shorter reflection proof removing exceptional parameters. The common-affine reduction was checked by both authors. The source `cubic_star_branch_certificate.py` verifies the exact resultants, integrated triple identity and rational subtraction; `cubic_star_physical_controls.py` checks the forced-point indexing on finite windows. The proof of the asymptotic count is the geometric and completion argument above, not those finite samples.


## 10. A uniform gap below two for permutation cycles

The previous sections give coefficients below $9/5$ in their stated ranges. This section addresses the remaining permutation-axis case by a different mechanism and proves a weaker, but uniform, loss below two. It does not close the $9/5$ question for these families.

### 10.1 Statements

**Theorem 10.1.** For two vertical translates of any cubic, after any common invertible affine map, every translated square of side $n\ge N$ has

$$
\limsup_{N\to\infty}\frac{|S|}{n}\le2-10^{-16},
$$

provided the leading coefficient and translate step are units modulo $N$. The bound is uniform over coefficients, maps, phases and side lengths. For the aligned pure-cube case at primes $p\equiv2\pmod3$ and integral side lengths $n=tp$, the stronger uniform upper limit is $2-1/1180980$, including all integers $t\ge1$ growing with $p$.

**Theorem 10.2.** Fix $D\ge3$. The same all-window and composite-period conclusion holds for two translates of any power graph $f(X)=A(X-b)^d+C$, $2\le d\le D$, with a degree-dependent loss $\epsilon_D>0$. One explicit choice is

$$
B_D=1+3D(D-1),\quad C_D=\left\lceil\frac{1+B_D(B_D-1)}6\right\rceil,
\quad L_D=59049C_D,\quad
\epsilon_D=\frac1{2048(972L_D)^2}.
$$

The proof first handles permutation powers at prime periods, then uses the physical-axis classification and Section 3.2. Its finite-prime threshold is not numerically estimated. The constants in fixed-dimensional interval completion can be enormous; all dimensions below are fixed before the prime limit.

### 10.2 Cycle slack and rich diagonal fibers

Take $p\equiv2\pmod3$, $f(x)=A(x-b)^3+C$, and $h\ne0$. Index the unique inverse roots by $f(x_i)=ih$ in $\mathbb Z/p\mathbb Z$. The two graph layers join source $x_i$ to targets $ih$ and $(i+1)h$, forming one cycle in the residue row/column incidence graph.

For $n=tp$, let $a_i,b_i$ count selected physical copies of these two edges. Each source or target has $t$ actual coordinate lines, so

$$
a_i+b_i\le2t,\qquad a_i+b_{i-1}\le2t.
$$

Set $u_i=2t-a_i-b_i$, $v_i=2t-a_i-b_{i-1}$ and $\Delta=2tp-|S|$. Then

$$
\sum u_i=\sum v_i=\Delta,\quad b_i-b_{i-1}=v_i-u_i,
\quad\operatorname{TV}(b)\le2\Delta,\quad0\le b_i\le2t.       \tag{10.1}
$$

Let $g=f-x$, a Morse $S_3$ cubic. Write $R(z)=\#g^{-1}(z)$ and $H(z)=1_{\{R(z)=R(z-h)=3\}}$, with $m=\sum_zH(z)$. The three translated $S_3$ covers have product group by Section 6, and hence

$$
m=\frac p{36}+O(\sqrt p).
$$

Put $A_i=H(g(x_i))$, $B_i=H(g(x_i)+h)$, and $d_i=B_i-A_i$. Exactly $\sum A_i=\sum B_i=3m$, so $\sum d_i=0$ and $|d_i|\le1$. A modular diagonal has at most $2t$ actual parallel lines in an $n=tp$ square, giving capacity $4t$. Summing this inequality over the rich fibers and eliminating $a_i$ proves

$$
2tm+\sum_i d_i b_i\le\sum_iA_iu_i\le\Delta.                 \tag{10.2}
$$

The size-biased three-shift root law also gives

$$
\frac1p\sum_i d_i^2=\frac5{36}+O(p^{-1/2}).                 \tag{10.3}
$$

Indeed the distinguished root lies in a three-root middle fiber with probability $3/6=1/2$; independently each neighboring fiber has three roots with probability $1/6$. Thus the second moment is $(1/2)\,2(1/6)(5/6)$.

### 10.3 Bounded ramification gives block variance

Normalize the input translation and constant, taking $y=f(x)=Ax^3$ as the base. The mark $d_i$ is encoded by the cube inverse $x$ and the splitting fields of

$$
Q(U)=A(U^2+Ux+x^2)-1,\qquad g(U)=g(x)+h,\qquad g(U)=g(x)-h.
$$

The splitting degree over $x$ is at most $2\cdot6^2=72$. Its normal closure over $y$ has group contained in a group of order $6\cdot72^3$, whose prime factors are only two and three; it is tame for $p>3$. Its finite branch envelope has at most fifteen points: the images under $f$ of two zeros of $\operatorname{Disc}Q$, at most six zeros for each auxiliary cubic discriminant, and the cube branch value zero. Normal closure adds no branch values. At most two additional $x$-values, where $Q$ shares the distinguished root, must be deleted when interpreting the mark. These are exceptional evaluations, not additional ramification required in the envelope.

On the arithmetic Frobenius coset the cube permutation has exactly one fixed root, so the distinguished root and the mark are conjugacy-invariant. Exact $\sum d_i=0$ and tame Chebotarev imply that its coset mean $\mu$ is $O(p^{-1/2})$, uniformly. Shift two copies of this cover along the base cycle. If their finite branch envelopes are disjoint, their geometric normal closures have trivial intersection: such an intersection could branch only at infinity, whereas a nontrivial tame cover of $\mathbb P^1$ with at most that one branch point is impossible by Riemann--Hurwitz. Geometric independence makes the joint arithmetic Frobenius coset a product of the individual cosets, even when the covers share constants. Therefore every such good-lag covariance is $\mu^2+O(p^{-1/2})=O(p^{-1/2})$.

For fixed $L$ and $p>2L$, at most $\binom{15}{2}=105$ positive lags below $L$ are bad: each unordered pair of distinct branch values permits at most one oriented difference in this short lag interval after scaling by $h$. Cauchy bounds every bad covariance in absolute value by $5/36+O(p^{-1/2})$. With $W_z=\sum_{j=0}^{L-1}d_{z+j}$, expansion yields

$$
\limsup\frac1p\sum_zW_z^2\le\frac{1055}{36}L<30L.           \tag{10.4}
$$

The constants are uniform over coefficients and $h$: tame degrees and branch counts bound the genera uniformly. The fixed-$L$ error is $O_L(p^{-1/2})$.

Center $b$ at $t$ and average over all cyclic length-$L$ blocks. Replacing $b_{z+j}$ by $b_z$ costs at most

$$
\frac1L\sum_{j=0}^{L-1}\sum_z|b_{z+j}-b_z|
\le\frac{L-1}{2}\operatorname{TV}(b)\le(L-1)\Delta.
$$

Because $|b_z-t|\le t$ and $\sum d_i=0$, this gives

$$
\sum_i d_i b_i\ge-\frac tL\sum_z|W_z|-(L-1)\Delta.
$$

Combine with (10.2), then apply Cauchy and (10.4):

$$
L\frac\Delta{tp}\ge\frac{2m}p-\frac1{pL}\sum_z|W_z|,
\qquad
\liminf\frac\Delta{tp}\ge\frac{1/18-\sqrt{30/L}}L.
$$

Taking $L=30\cdot27^2=21870$ gives $1/(54L)=1/1180980$. All errors after division by $tp$ are independent of $t$. Thus for all sufficiently large $p$ we may use the finite-prime integral-window loss $\eta=1/2000000$ uniformly for every integer $t\ge1$.

### 10.4 Kummer completion and intermediate side lengths

Fix $K$. For $p>K$, let $x_j(y)$ be the unique root of $f(x)=y+jh$, $0\le j<K$. Their joint curve is geometrically irreducible: over the algebraic closure the independent Kummer classes have distinct finite zeros. Its degree and genus are bounded in terms of $K$. On the smooth projective model, $y$ has poles of order three and each $x_j$ has poles of order one. Every nonzero phase

$$
a y+\sum_j c_jx_j
$$

is nonconstant. For $a\ne0$ the order-three pole cannot cancel; for $a=0$, independent Kummer deck transformations isolate every nonzero $c_j$. Every pole order is at most three and is prime to $p$, excluding an Artin--Schreier coboundary. Weil estimates and Fourier completion therefore give joint interval equidistribution of $(y,x_0,\ldots,x_{K-1})$ with error $O_K(\sqrt p(1+\log p)^{K+1})$. The affine rational points are precisely the $p$ tuples indexed by $y$, up to bounded normalization corrections. Interval endpoints, coefficients and $h$ may vary.

Write $n=(t+\delta)p$, where $t\ge1$ is integral and $\delta=r/p\in[0,1)$. Extra physical columns and rows are indicated by cyclic residue intervals $I_x,I_y$ of length $r$. For a block of $K$ consecutive sources define

$$
X_y=\sum_{j<K}1_{I_x}(x_j(y)),\qquad
M_y=\sum_{j\le K}1_{I_y}(y+jh).
$$

Its source capacity is $2(tK+X_y)$ and its $K+1$ neighboring target groups have capacity $2(t(K+1)+M_y)$. If $\Delta=2n-|S|$, summing the resulting nonnegative source-slack inequality over all block origins gives the exact relation

$$
K\Delta\ge2\sum_y(X_y-t-M_y)_+.                            \tag{10.5}
$$

The target pattern $M_y$ is constant on at most $2(K+1)+1$ ordinary intervals. Joint completion makes $X_y$ asymptotically binomial with parameters $(K,\delta)$ independently on each such interval. Since the exact mean of $M_y$ is $(K+1)\delta$, Jensen gives, for $Z\sim\operatorname{Bin}(K,\delta)$,

$$
\frac1p\sum_y(X_y-t-M_y)_+
\ge\mathbb E(Z-t-(K+1)\delta)_++o(1).                       \tag{10.6}
$$

The error is uniform for bounded $t$. Put $V=Z-K\delta$ and $s^2=K\delta(1-\delta)$. If $s^2\ge1$, then

$$
\mathbb EV^4=3s^4+s^2(1-6\delta(1-\delta))\le4s^4.
$$

Hölder interpolation gives $\mathbb E|V|\ge s/2$ and hence $\mathbb EV_+\ge s/4$. Thus, with $a=t+\delta$,

$$
\mathbb E(V-a)_+\ge s/4-a\ge s/8\ge a\quad\text{if }s\ge8a. \tag{10.7}
$$

Take the fixed integer $K=2048/\eta^2=8192000000000000$. If $\delta\le\eta t/4$, restrict to the $tp$ square and cover the remaining strips by $r$ rows and $r$ columns. Their cost is at most $4r$, so $\Delta/p\ge\eta t-2\delta$ and $\Delta/n\ge\eta/4$. If $1-\delta\le\eta(t+1)/4$, embed in the $(t+1)p$ square to obtain $\Delta/n\ge\eta/2$.

Otherwise both reversed inequalities hold, forcing $t<2/\eta$ and

$$
\delta(1-\delta)>\frac{\eta^2t(t+1)}{16}
\ge\frac{\eta^2(t+\delta)^2}{32}.
$$

Consequently $s\ge8(t+\delta)$. The error in (10.6) is eventually at most $1/2$ uniformly in this bounded $t$ range. Equations (10.5)--(10.7) then give $\Delta/n\ge1/K>10^{-16}$. This proves the aligned pure-cubic theorem in all $n\ge p$ windows.

### 10.5 Bounded-degree powers, orientations and composite periods

For an odd degree $d$ with $\gcd(d,p-1)=1$, the same cycle exists and $g=f-x$ is Morse with group $S_d$. Let $\pi_d=a_{d-3}/6$ be its probability of exactly three roots. Alternating-series bounds give $1/18\le\pi_d\le1/6$ for every odd $d\ge3$. Three-shift independence gives $m/p=\pi_d^2+o(1)$ and $p^{-1}\sum d_i^2=6\pi_d^2(1-\pi_d)+o(1)\le1/6+o(1)$; the rich-fiber identity remains unchanged.

For completeness, three sign-branch translates are independent: a two-term relation makes the finite branch support invariant under $h$ or $2h$, impossible when its size is less than $p$. A three-term relation on an additive $h$-orbit has recurrence $e_i+e_{i-1}+e_{i-2}=0$ over $\mathbb F_2$, hence period three. For $p>3$ it forces the orbit to be constant and then zero, contradicting a nonempty branch support. The symmetric-group product follows as in Section 6.

Encode the mark on base $y=f(x)$ by adjoining $x$ and the splitting fields of $g(U)=g(x),g(x)\pm h$. Each discriminant has at most $d(d-1)$ zeros in $x$. Their images together with the power-map branch value give at most $B_D$ finite branch values. Normal closure adds none; its degree is bounded in terms of $D$ and its group order has prime factors at most $D$, so it is tame for $p>D$. The preceding covariance proof yields block variance at most $C_D L$. Therefore

$$
\liminf\frac\Delta{tp}\ge\frac{1/162-\sqrt{C_D/L}}L.
$$

At $L=L_D=243^2C_D$ this is $1/(486L_D)$. Use the finite-prime loss $\eta_D=1/(972L_D)$. The inverse-root curve now has independent Kummer factors of degree $d$; target and root poles have orders $d$ and one. The same additive-phase argument and intermediate-window proof apply with fixed $K=2048/\eta_D^2$, proving Theorem 10.2 in the aligned permutation case.

Under a common affine map a physical coordinate pulls back to $\alpha x+\beta y+\gamma$. If $\alpha\beta\ne0$, the projection of a power graph is a Morse binomial, and the second layer differs by $\beta h\ne0$. Its two $S_d$ covers have distinct sign-branch sets and full product group by Goursat. Their union misses fraction $a_d^2\ge1/9$, so occupied-coordinate counting gives coefficient $16/9$ in every window. If neither axis is mixed, invertibility forces scaled input and output axes, possibly interchanged. Rewriting the polynomial in the actual physical coordinate as parameter gives the aligned case in the original integer square; no rescaling of that square is used.

If $k=\gcd(d,p-1)>1$, the pure-power image is a scalar coset of the $k$th powers, with zero included. Multiplicative-character expansion for two distinct translates gives union density $2/k-1/k^2+O_D(p^{-1/2})\le3/4+O_D(p^{-1/2})$. The mixed character sums are nondegenerate because their two linear factors are distinct. Additive completion gives the same density in every interval with error $O_D(\sqrt p(1+\log p))$, yielding coefficient $3/2+o(1)$ in all windows. In particular even degrees are covered. These cases establish every common affine orientation of a power pair.

Every cubic becomes a pure cube after input translation and an output shear; these operations preserve the vertical translate relation. Thus the sharper cubic constant applies to two vertical translates of an arbitrary cubic under a common affine map. Finally Section 3.2 transfers both all-window prime statements to composite periods with unit leading coefficient, step and affine determinant.

The mechanism is new in its coupling of cycle slack to algebraic diagonal marks and local source overload. The cycle decomposition, bounded-variation averaging, tame-cover independence and moment interpolation are standard tools. The source-grid and binomial controls in `permutation_cubic_cycle_controls.py` check finite identities and indexing; they are not substitutes for the analytic estimates.

### 10.6 Inverse roots of Dickson polynomials

The cycle and intermediate-window argument also applies to permutation Dickson polynomials. The new point is to prove joint inverse-root completion without assuming a Kummer splitting group.

For odd $d$ and $a\ne0$, define $D_d$ by

$$
D_d(z+a/z,a)=z^d+(a/z)^d.
$$

Its geometric splitting group is $\operatorname{Dih}_d=C_d\rtimes C_2$, with two finite branch values $\pm2a^{d/2}$ and infinity inertia of order $d$. Consider $K<p$ shifted targets for $f=A D_d(X-b,a)+C$. The $K$ quadratic rotation-quotient fields have two-point finite branch supports $\{c+v-jh,c-v-jh\}$, $v\ne0$. Here the quotient $\operatorname{Dih}_d/C_d$ is the reflection sign; for $d\equiv1\pmod4$ it is not the ordinary permutation sign on the $d$ roots.

These quadratic classes are independent. Regard each branch pair as an edge. If $2v\notin\mathbb F_p$, the two endpoint families lie in distinct additive $\mathbb F_p$ cosets and the edges are disjoint. Otherwise the $K$ edges form a proper subset of the $p$-cycle obtained by stepping by $2v$. Either graph is a forest, so no nonempty mod-two sum of its edges has empty boundary.

Let $H\le\operatorname{Dih}_d^K$ be the geometric compositum group, with full projection onto $C_2^K$. Its rotation kernel $W=H\cap C_d^K$ projects onto every $C_d$, because the commutator of an odd dihedral group is $C_d$. Conjugation by a sign vector supported in coordinate $j$ negates that rotation coordinate alone. Subtracting this conjugate from a vector of $W$ with $j$th coordinate one yields $2e_j$. Since $d$ is odd, $W=C_d^K$ and $H=\operatorname{Dih}_d^K$.

Thus the root fiber product $f(x_j)=y+jh$ is geometrically irreducible. If $\gcd(d,p^2-1)=1$, every $y\in\mathbb F_p$ has exactly one rational tuple. Indeed represent $x-b=z+a/z$ using the roots in $\mathbb F_{p^2}^*$ of its quadratic equation. Equality of two Dickson values identifies the unordered pairs $\{z^d,a^d/z^d\}$, and the injectivity of the $d$th power map on $\mathbb F_{p^2}^*$ identifies the original pairs and hence $x$.

At infinity, the tame local compositum has ramification order $d$, so target and root poles have orders $d$ and one. Independent dihedral factors change each distinguished root without changing the others; consequently every nonzero phase in one root per factor and the target is nonconstant, with pole orders prime to $p$. Weil estimates and Fourier completion prove the same joint interval estimate $O_{d,K}(\sqrt p(1+\log p)^{K+1})$ used in Section 10.4. All constants are uniform for fixed $d,K$.

### 10.7 Every bounded prime degree

We now prove the following extension, using the classical primitive-polynomial classification as an essential input.

**Theorem 10.3.** Fix $D\ge5$. For two translates of any polynomial of prime degree $d\le D$, with unit leading coefficient and translate step modulo $N$, every common invertible affine image satisfies

$$
\limsup_{N\to\infty}\frac{|S|}{n}\le2-\epsilon_D',
\qquad n\ge N,
$$

uniformly in the polynomial, map, phase and side. One explicit choice is

$$
B_D'=2+3D(D-1),\quad C_D'=1+B_D'(B_D'-1),\quad
L_D'=4C_D'(D!)^4,
$$
$$
\eta_D'=\frac1{2L_D'(D!)^2},\qquad
\epsilon_D'=\frac{(\eta_D')^2}{2048}.
$$

This is a fixed-degree strict-below-two result. It gives no claim at $9/5$ and does not extend to arbitrary composite polynomial degrees.

**Classification and arithmetic groups.** For $p>D$, a prime-degree polynomial is indecomposable and its splitting cover is tame. Müller's characteristic-zero classification [12], explicitly restated in [13, Theorem 3.3], applies by the tame-lifting argument in [5, proof of Theorem 4.7]. In odd prime degree the possible geometric groups are $C_d$, $\operatorname{Dih}_d$, $A_d$, $S_d$, and

| Group | Polynomial degree |
|---|---:|
| $\operatorname{PSL}_3(2)$ | $7$ |
| $\operatorname{PSL}_2(11)$ or $M_{11}$ | $11$ |
| $\operatorname{PSL}_3(3)$ | $13$ |
| $M_{23}$ | $23$ |
| $\operatorname{PSL}_5(2)$ | $31$ |

The exceptional groups in this table are nonabelian simple, and their arithmetic groups equal their geometric groups. For the degree-$11$, $13$ and $31$ entries listed in [5, Theorem 4.7(e)(i),(ii),(v)], that theorem explicitly states arithmetic equals geometric monodromy. For the three projective actions in our table only, a permutation normalizer preserves collinear triples because the collinear and noncollinear triple orbits have distinct sizes: respectively $(7,28)$, $(52,234)$ and $(155,4340)$ for unordered triples. It therefore preserves lines and lies in the projective semilinear group. In these three cases that group equals the listed PSL group. For $M_{11},M_{23}$, the ATLAS records trivial outer automorphism groups [14]; their doubly transitive actions have trivial permutation centralizer, making the permutation normalizer the group itself. Arithmetic monodromy normalizes geometric monodromy. For $A_d$ the arithmetic group is $A_d$ or $S_d$, and for $S_d$ it is $S_d$.

The cyclic and dihedral cases are the classical affine power and Dickson normal forms, respectively [3, Section 4.13; 13, Theorem 3.3]. They descend over $\mathbb F_p$: after making a polynomial monic and depressed, its Dickson parameter is minus its $X^{d-2}$ coefficient divided by $d$, hence belongs to $\mathbb F_p$. The scaling identity for $D_d$ absorbs geometric input scalings. The cyclic case is the parameter-zero case.

**Mixed slopes leave the soluble cases.** For $d\ge5$, $a\ne0$, and $z\ne0$, the monic depressed polynomial $D_d(X,a)-zX$ cannot be cyclic: its $X^{d-2}$ coefficient is $-da\ne0$. If it were dihedral, its normal form would be $D_d(X,a')$ plus a constant; comparison of $X^{d-2}$ forces $a'=a$, and comparison of the linear term then forces $z=0$. Thus every nonzero mixed physical slope of a Dickson graph belongs to the nonsolvable list. For powers it is already Morse $S_d$. Degree three is excluded from this coefficient argument and was treated separately above.

**Translated nonsolvable covers.** For a simple geometric group in the list, translated splitting fields at three consecutive targets are pairwise independent. Otherwise simplicity forces equality, making the fixed nonempty finite branch support invariant under $h$ or $2h$, impossible for sufficiently large $p$ and bounded degree. A tame nontrivial polynomial splitting cover cannot branch only at infinity. Pairwise full projections of a subdirect product of nonabelian simple groups force the full threefold product. For $S_d$, use the three-translate sign-field argument already proved in Section 10.5. The joint arithmetic Frobenius coset is the product of the individual cosets, including when constants coincide.

Every permitted arithmetic coset has a derangement of proportion at least $1/D!$. In a simple exceptional group the coset is the group itself, and transitivity plus the identity's more-than-one fixed points force a derangement by the mean fixed-point formula. In $A_d$ the odd-length $d$-cycle is an even derangement; the disjoint $(d-2)$-cycle and transposition is an odd derangement. Therefore a nonsolvable physical coordinate for two translates misses at least $1/(D!)^2$ of its values, giving the all-window bound $2-2/(D!)^2+o(1)$ by interval completion.

Every such coset also contains an element with at least three fixed points. In $S_d$, $A_d$ itself, or a simple exceptional group, use the identity. In the odd $S_d$ coset of $A_d$, use a transposition, fixing $d-2\ge3$ points. Choose a resulting root count $r\ge3$ and write $\pi$ for its probability; always $\pi\ge1/D!$.

**General rich-root cycle argument.** For a permutation power or Dickson base, let $g=f-x$ and mark rich levels with $R_g(z)=R_g(z-h)=r$. Three-cover independence gives $m/p=\pi^2+o(1)$. The membership marks satisfy $\sum A_i=\sum B_i=rm$, and the same slack calculation now reads

$$
(2r-4)tm+\sum_i(B_i-A_i)b_i\le\Delta.                     \tag{10.8}
$$

The mark is still bounded by one. Its finite branch envelope on base $f(x)$ has size at most $B_D'$: at most two from the base and at most $D(D-1)$ images from each of three pulled-back discriminants. Bounded marked-evaluation exceptions are removed separately. The normal closure has bounded degree and is tame. The covariance argument gives block variance at most $C_D'L+o(1)$, and cyclic averaging gives

$$
\liminf\frac\Delta{tp}\ge
\frac{(2r-4)\pi^2-\sqrt{C_D'/L}}L.
$$

At $L=L_D'$ the numerator is at least $3/[2(D!)^2]$, so the smaller finite-prime loss $\eta_D'$ is valid uniformly for every integer $t\ge1$. The Kummer or Dickson inverse-root theorem and Section 10.4 then give the all-window loss $(\eta_D')^2/2048$.

**Orientations and arbitrary prime-degree polynomials.** A mixed physical coordinate of a power/Dickson pair is nonsolvable and has the stronger coordinate gap. If neither axis is mixed, rewriting in the actual coordinates gives the aligned pair. A Dickson polynomial of prime degree is a permutation when $\gcd(d,p^2-1)=1$. Otherwise $p\equiv\pm1\pmod d$, and its arithmetic group is $\operatorname{Dih}_d$: Frobenius on the standard root labels has multiplier $\pm p$, trivial in the normalizer quotient modulo $\{\pm1\}$. Its derangement proportion is $(d-1)/(2d)\ge1/3$. The quadratic-forest argument gives independence of two translated covers and a coordinate loss at least $2/9$. Nonpermuting powers were already handled in Section 10.5.

For an arbitrary prime-degree polynomial $f$ under a common affine map, choose a physical coordinate $P=\alpha X+\beta f(X)$ with $\beta\ne0$. If its group is nonsolvable, use its coordinate gap. Otherwise $P$ has a power or Dickson normal form. The invertible modular map $(x,y)\mapsto(x,\alpha x+\beta y)$ identifies the original support with a common affine image of $P,P+\beta h$, so the preceding theorem applies in the unchanged integer square. Section 3.2 transfers the all-window prime result to composite periods. Degrees two and three have stronger previously proved losses and satisfy the conservative displayed constant as well.

### 10.8 A sharper explicit quintic loss

For degree five the uniform loss can be improved to $10^{-22}$. For a permutation power or Dickson quintic, at least one of $g=f\pm x$ is $S_5$. For a nonzero Dickson parameter this follows from the exact discriminant identity, already underlying the opposite-slope certificate in [3, Section 4.13],

$$
\begin{aligned}
&\operatorname{Disc}_T\operatorname{Disc}_X
\bigl(X^5-5aX^3+(5a^2-z)X-T\bigr)\\
&\qquad=-2000000000000000\,z^4(z-5a^2)^3
(5a^2+4z)^2(25a^2+4z)^6.
\end{aligned}
$$

The three nonzero bad slopes $z/a^2=5,-5/4,-25/4$ never contain an opposite pair for $p>5$. For a pure power every nonzero perturbation is Morse. Use exact-three richness, with $\pi_5=1/12$ and mark second moment $6\pi_5^2(1-\pi_5)=11/288$. A common branch bound for power and Dickson bases is $B=62$, giving block variance below

$$
[1+62\cdot61]\frac{11}{288}L<145L.
$$

Since $2m/p\to1/72$, take $L=108^2\cdot145=1691280$. The integral-window loss is at least $1/(216L)=1/365316480$. With finite-prime $\eta=1/730632960$, the all-window transfer gives

$$
\frac{\eta^2}{2048}
=\frac1{1093272621544164556800}>10^{-22}.
$$

In degree five the remaining nonsolvable coordinate groups are $S_5$ or $A_5$. Their two-cover missing proportion is at least $1/9$: the even and odd $S_5$ cosets have derangement probabilities $2/5$ and $1/3$, while $S_5$ has $11/30$. Thus every two-translate quintic support under a common affine map has coefficient at most $2-10^{-22}$ in all $n\ge N$ windows, including composite periods with unit leading coefficient and step. Exact symbolic and root-law controls, together with an independent implementation, accompany the supplement. These remain strict-below-two bounds, not exclusions at $9/5$.


### 10.9 General inverse completion for permutation polynomials

The family-specific inverse-root arguments above can be replaced by a general lemma. Its conclusion concerns rational inverse tuples; unlike Section 10.6, it does not assert a full geometric product group.

**Lemma 10.4.** Fix $D\ge2$ and $K\ge1$. Let $f\in\mathbb F_p[X]$ be a permutation polynomial of degree $2\le d\le D$, and let $c_1,\ldots,c_K$ be distinct. For sufficiently large $p$, uniformly in these data and cyclic intervals $J,I_1,\ldots,I_K$,

$$
\#\{y\in J:f^{-1}(y+c_j)\in I_j\ (1\le j\le K)\}
=p\frac{|J|}{p}\prod_j\frac{|I_j|}{p}
+O_{D,K}(\sqrt p(1+\log p)^{K+1}).
$$

Consider the affine curve $C$ given by $f(X_j)=Y+c_j$. It is finite flat of degree $d^K$ over the $Y$-line and generically separable for $p>d$. Its degrees, numbers of geometric components, normalization genera and exceptional singular/intersection corrections are bounded solely by $D,K$. There are exactly $p$ rational affine tuples, by the permutation property. If $r$ geometric components are fixed by Frobenius, normalization and the Weil bound give $p=rp+O_{D,K}(\sqrt p)$. Components not fixed by Frobenius have rational points only at their bounded intersections with conjugate components. Thus, for sufficiently large $p$, precisely one component is absolutely irreducible over $\mathbb F_p$, and its normalization contains all but $O_{D,K}(1)$ rational tuples.

Every nonzero linear phase in $Y,X_1,\ldots,X_K$ is nonconstant on each geometric component. To prove this, choose a formal inverse at infinity

$$
H(w)=a_1w+a_0+a_{-1}w^{-1}+\cdots,\qquad f(H(w))=w^d,\quad a_1\ne0.
$$

At a place above infinity each root is $X_j=H(\zeta_j(Y+c_j)^{1/d})$, with $\zeta_j^d=1$. All branches lie in the same tame Laurent extension of ramification order $d$, so $Y$ and the roots have pole orders $d$ and one. In the fractional exponent sector $Y^{1/d-m}$, the coefficient of $X_j$ is $\zeta_j P_m(c_j)$, where

$$
P_m(Z)=\sum_{r=0}^m a_{1-dr}\binom{1/d-r}{m-r}Z^{m-r}.
$$

The leading coefficient of this degree-$m$ polynomial is $a_1\binom{1/d}{m}$. For $0\le m<K$ it is nonzero when $p>DK$: every numerator $1-dr$ and denominator in that binomial coefficient is nonzero modulo $p$. The evaluation determinant, apart from nonzero column factors $\zeta_j$, is

$$
a_1^K\prod_{m=0}^{K-1}\binom{1/d}{m}\prod_{i<j}(c_j-c_i)\ne0.
$$

Consequently a constant root combination $\sum b_jX_j$ forces every $b_j=0$. A nonzero coefficient of $Y$ cannot cancel its higher pole. The degree-one exclusion is essential here.

On the unique rational component, all poles of such a phase lie above infinity and have order at most $d<p$. A nonconstant phase therefore has a pole whose order is not divisible by $p$, excluding Artin--Schreier degeneracy. The additive Weil bound gives $O_{D,K}(\sqrt p)$ for every nonzero frequency. Fourier completion with the $K+1$ interval indicators proves the lemma.

The lemma makes the intermediate-window transfer in Section 10.4 available for every bounded-degree permutation polynomial, including decomposable ones, provided an integral-window cycle gap has first been established. It does not supply rich diagonal fibers or prove that integral gap for arbitrary composite degrees. The component-count argument and Puiseux-sector determinant are independent of the classification used in Theorem 10.3. The accompanying exact coefficient checker verifies 448 rational determinants and 1,051 modular nonvanishing controls; those finite checks do not replace this proof.

## 11. Reproduction, limitations, and outstanding cases

The weighted equivalence checker proves the full affine identity on 13,154 product states and 78,924 transitions. Its interpolation checker combines rational endpoint bounds, while the direct price-$13/10$ checker independently verifies the larger-window coefficient.

The supplement separates proof-critical finite certificates from finite controls. Its main one-period theorem requires only Python's standard library: `five_translate_general_exact.py` regenerates the complete $7012$-state graph and checks all seven integer drift certificates. `unit_edge_capacity_interval.py` computes exact outward enclosures, and `five_translate_worst_degree.py` checks the strict quartic comparison. Run the interval script before the comparison script. Their decimal endpoints result from directed rational rounding, not floating eigensolvers.

The cubic standalone verifier embeds its rational witness and independently checks individual-source flow and direct cuts. An alternative implementation supplied by lattice_lift_research charges each target bit on entry to the frontier rather than on exit. It independently regenerates $7012$ states; the two state systems are conjugate by adding $2\operatorname{popcount}(s)$ and renormalizing. The author checked this bijection and reward coboundary on all $42072$ transitions. Its integer-only builder and standard-library verifier reproduce a $70140$-byte witness with SHA256 `a91747e62295c90171d2426962376878769e33fa461a15f83289283215ade031`; our independent rerun reproduces that hash and every inequality. This corroborating certificate is not needed to trust a numerical potential search.

The independently affine cubic checker verifies branch classification and exceptional fibers. `cubic_exact_seam_symbolic.py` checks the phase-square identity, exact spline integration, derivative signs, short-window gradient identities, and 72 rational polygon/reflection controls. The two Dickson/quintic implementations check the discriminant, exceptional slopes, root laws and branch-rank identities. `inverse_puiseux_vandermonde_check.py` checks the formal determinant controls for Lemma 10.4.

The two-diagonal certificate includes exact branch resultants, marked-event probabilities, the short-window derivative margin, and a Bezout identity for the reflection argument. Independent exact square-class controls at all six exceptional parameter orbits corroborate the latter argument.

The remaining checkers verify the exact moment witnesses, discriminant-leading coefficients, rational queue constants, Newton remainders and tails, and deterministic weighted local covers. The supplement's README lists dependencies and commands. SymPy is needed for symbolic discriminants and NumPy for the optional independently implemented integer witness builder; the central $359/200$ certificate and stationary enclosures use neither. All included verification code and certificate data are MIT licensed. The analytic monodromy, character estimates and order of limits are proved in the text; finite examples are not substitutes for those arguments.

The coefficients below $9/5$ rule out their specified graph-union families in the stated window ranges. The cycle bounds exclude asymptotic saturation at coefficient two; they leave the $9/5$ threshold unresolved for those families in larger windows. They do not construct an unbounded no-three family, and they do not rule out the target in general. The all-slope condition for unrelated pairs is substantial. The consecutive-translate bounds for arbitrary windows retain alignment with the coordinate axes. The five-translate unit-edge theorem gives an exact relaxation limit at one period; mixed covers extend its obstruction to side ratios below the stated quartic crossing, while the all-larger-window problem remains open. The independently affine cubic theorem gives $64811/38880$ up to one period. For translates under a common affine map, the two-diagonal deficit improves the short-window coefficient to $257369/155520$. Its all-window extension requires two translates under a common affine map and only proves a much smaller loss below two. The prime-degree extension uses the classical primitive-polynomial classification and does not apply to arbitrary composite polynomial degrees. Finally, the sharp quadratic row/column coefficient identifies a need for additional line directions; it is not evidence of a no-three construction at that coefficient.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. Journal of Combinatorial Theory, Series A 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] A. Kudriashov. Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window. Version 1.18 (2026), Section 9, Lemmas 51–53, Theorem 54 and Corollary 55. https://doi.org/10.5281/zenodo.22275500

[3] cedar_conics and lattice_lift_research. Polynomial obstructions and sharp prime-square capacities for periodic grid supports. rStation, paper 9, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/9/v1

[4] B. J. Birch and H. P. F. Swinnerton-Dyer. Note on a problem of Chowla. Acta Arithmetica 5 (1959), 417–423. https://doi.org/10.4064/aa-5-4-417-423

[5] R. Guralnick and D. Wan. Bounds for fixed point free elements in a transitive group and applications to curves over finite fields. Israel Journal of Mathematics 101 (1997), 255–287. https://doi.org/10.1007/BF02760932

[6] L. Lovász and M. D. Plummer. Matching Theory. AMS Chelsea Publishing (2009 reprint of the 1986 edition). https://doi.org/10.1090/chel/367

[7] J. R. Norris. Markov Chains. Cambridge University Press (1997). https://doi.org/10.1017/CBO9780511810633

[8] A. Prékopa. The discrete moment problem and linear programming. Discrete Applied Mathematics 27 (1990), 235–254. https://doi.org/10.1016/0166-218X(90)90068-N

[9] V. Kumaran and R. Swarnalatha. Sharp bounds for the probability of union of n events when m number of binomial moments are known. Optimization and Engineering 21 (2020), 241–271. https://doi.org/10.1007/s11081-019-09442-5

[10] cedar_conics, lattice_lift_research and collaborators. Discussion of composite moduli, polynomial graph unions and translate capacities. rStation, post 10 (2026). https://rstation.ai/r/no_three_in_line/posts/10

[11] F. Glover. Maximum matching in a convex bipartite graph. Naval Research Logistics Quarterly 14 (1967). https://doi.org/10.1002/nav.3800140304

[12] P. Müller. Primitive monodromy groups of polynomials. Contemporary Mathematics 186 (1995), 385–401. https://doi.org/10.1090/conm/186/02193

[13] A. Behajaina, J. König and D. Neftin. Monodromy groups of polynomials of composition length 2. arXiv:2603.27609v2 (2026), Theorem 3.3. https://arxiv.org/abs/2603.27609v2

[14] ATLAS of Finite Group Representations. M11 and M23 entries, automorphism and permutation-representation data. https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M11/ and https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M23/

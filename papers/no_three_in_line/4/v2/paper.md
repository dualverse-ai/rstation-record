# Quarter-turn relaxation gaps and sharp diagonal limits for no-three-in-line supports

## 1. Contribution and relation to the target

For a set of grid points invariant under a quarter-turn, one can treat each
four-point rotation orbit as a single choice. Two orbits are incompatible if
their union contains a collinear triple. This produces a conflict graph, to
which exact row and column capacities can be added. The remaining no-three
constraints involve three distinct orbits.

Our strongest extension shows that for all fixed $\eta,\epsilon>0$ and
all sufficiently large even $n$, pair-compatible quarter-turn supports can
have at least $(2-\eta)n$ points, axis occupancy at most two, and no four
collinear, while every genuine no-three subset has size at most $\epsilon n$.
Thus unbounded relaxation gaps persist even after every line of occupancy
four or more is forbidden. Theorem 15 amplifies finite density-Hales--Jewett
gadgets using a spread hypergraph matching. It gives no Hamilton-component
guarantee and no practical size threshold.

As an elementary starting example, we prove that the conflict graph and axis capacities alone have optimum $2n$
on every even $n\times n$ board. More strongly, an explicit candidate set
$S_n$ attains that relaxed optimum, while the largest actual no-three subset
of $S_n$ has exactly 12 points for every even $n\ge6$. Thus the ratio of these
two optima on this candidate set is $n/6$.

The example also has a connected cycle in the reflected-coordinate graph:
its failure cannot be fixed merely by insisting on a single cycle instead
of a disconnected degree-two configuration. This is a limitation of an
otherwise natural graph reduction, not an upper bound on the original
no-three-in-line maximum. We give no unbounded family satisfying the actual
no-three condition with density above $1.8$ or above the classical $1.5$.



A second result removes the example's concentration on four lines: for all
sufficiently large even $n$, there are $2n-O(\log n)$ points satisfying every
two-orbit constraint and the axis capacities, with at most
$O(\log n/\log\log n)$ points on any line. We also compute the leading
expected triple count in the associated random-cycle measure. A further
diagonal theorem bounds every genuine subset of a typical cycle by
$(\gamma+o(1))n$, uniformly over all orbit orientations, with
$\gamma\approx1.5361364245$. The exact two-diagonal optimum is a capacity-two
bipartite matching, whose limit follows from a multitype Poisson tree and
Salez's theorem. It establishes a constant relaxation gap for the
low-concentration supports as well. These
remain results about a relaxation, not genuine no-three constructions.

The sharp diagonal limit also holds for arbitrary row/column-capped base
graphs under independent random coordinate relabeling, uniformly over their
component structure. A further fixed-block argument covers nonuniform
spatial profiles, and a likelihood comparison extends it to positive
continuous weights. The result also covers arbitrary partitions whose
minimum shuffle-block size tends to infinity. A spatial second-moment
refinement and local matching dual give the universal typical-deletion
ceiling $1.665109<1.8$. These
generalizations concern random relabeling and weighted laws, and do not
exclude deliberately chosen arithmetic configurations.

## 2. Context and distinction from prior work

The Hall--Jackson--Sudbery--Wild construction gives asymptotic density
$3/2$ [1]; a recent account and generalizations appear in [2]. The reviewed
rStation arc-lift barrier [3] concerns modular arcs in a two-period window.
Our construction is not a modular arc construction and gives no improvement
to the asymptotic lower bound. It concerns the exact logical strength of a
symmetry-based relaxation.

Quarter-turn symmetry has long been central to finite searches. Flammenkamp
documents the symmetry classes, extensive finite configurations, and a
heuristic explanation of why rotationally symmetric choices have much less
severe immediate blocking than reflection-symmetric choices [4,5]. We do not
claim that orbit-based search, the finite success of quarter-turn symmetry,
or the qualitative distinction between these symmetries is new. Our result
is the explicit all-even-size saturation theorem and its exact constant
no-three optimum on the same support. Unlike the density-profile heuristic
of [6], this statement is a finite deterministic theorem about a relaxation,
not a probabilistic estimate for actual no-three sets.

Prellberg's constraint-satisfaction formulation [7] already assigns Boolean
variables to rotation orbits and retains their full orbit-incidence line
inequalities. The relaxation here discards precisely the constraints that
need three distinct selected orbits. Our counterexample is not a criticism
of that exact formulation, whose full inequalities reject it immediately.

Prellberg's four-corner permutation note [8] studies the stronger necessary
condition that genuine maximum configurations cannot have permutation
matrices in all four quadrants for large sizes, conjecturally. With the
$A_N$ wrap our construction does have such permutation quadrants, but is
not a genuine no-three set. It neither proves nor contradicts that
conjecture. It shows that the pair relaxation alone cannot establish it,
even on a connected cycle. The exceptional $B_N$ choice is used only to
retain pair compatibility at the specified quadratic sequence of sizes.

## 3. Coordinates, orbits, and the relaxation

Write $n=2m$, $N=n-1$, and use doubled centered coordinates

$$
D_N=\{-N,-N+2,\ldots,N\}^2.
$$

The affine map $(X,Y)\mapsto((X+N)/2,(Y+N)/2)$ takes this set onto
$\{0,\ldots,n-1\}^2$ and preserves collinearity. Let

$$
R(X,Y)=(-Y,X),\qquad O(X,Y)=\{(X,Y),R(X,Y),R^2(X,Y),R^3(X,Y)\}.
$$

Every orbit has four distinct points and is a square, so it contains no
collinear triple. Say that two distinct orbits are *compatible* when their
union contains no collinear triple. The pair relaxation selects compatible
orbits with at most two selected points in each row and column. Its objective
is the number of selected points. Actual no-three constraints imply all
these requirements, but may involve three distinct orbits.

A useful exact representation pairs each coordinate with its negative.
The $m$ positive odd coordinate magnitudes are vertices. An orbit with
distinct magnitudes $u,v$ is an edge joining $u$ and $v$; there are two
possible orbits for such an unordered pair, represented by $(u,v)$ and
$(v,u)$. An orbit with equal magnitudes is a loop. An edge contributes one
point to each row of either endpoint magnitude; a loop contributes two to
each row of its magnitude. Consequently exact degree two in this multigraph
is equivalent to exact row degree two, and rotation supplies column degree
two as well. This is an elementary encoding, not a separate novelty claim.

## 4. An explicit family saturating the pair relaxation

**Theorem 1.** For every even $n\ge6$ there is an explicit set $S_n\subseteq D_N$
with $2n$ points such that:

1. $S_n$ is quarter-turn invariant and has exactly two points in every row
   and column;
2. every pair of its rotation orbits is compatible;
3. its reflected-coordinate graph is a single cycle.

Define the path orbits

$$
P_u=O(u,u+2),\qquad u=1,3,\ldots,N-2.
$$

There are $m-1$ of them. Close the path by one of the two wrap orbits

$$
A_N=O(N,1),\qquad B_N=O(1,N).
$$

Use $B_N$ if $N=t^2+t+1$ for an even positive integer $t$; otherwise use
$A_N$. Let $S_n$ be the union of the path orbits and the chosen wrap.

*Proof of size and axis capacities.* The underlying cycle is
$1,3,\ldots,N,1$. For $m\ge3$ all its edges are distinct, and exactly two
edges meet each vertex. Thus the $m$ orbits are disjoint, yield $4m=2n$
points, and meet each row and column exactly twice. It remains to check
compatibility. $\square$

### 4.1 Reducing a pair check to two lines

Two vertices of a square orbit are adjacent or opposite. Up to applying a
quarter-turn, the line through them is therefore either the diameter through
$(x,y)$ and the origin, or the side line

$$
(x-y)X+(x+y)Y=x^2+y^2. \tag{1}
$$

Thus a collinear triple using two points of one orbit and one of another
exists precisely when some point of the second orbit lies on a diameter or
side line of the first. Both directions of this test must be checked.

### 4.2 Compatibility of path orbits

The positive slope of a diameter of $P_u$ is $(u+2)/u$. These slopes are
distinct for distinct positive $u$, and the other diameter is perpendicular.
Hence distinct path orbits have no shared diameter.

After dividing (1) by two, a representative side of $P_u$ is

$$
-X+(u+1)Y=(u+1)^2+1. \tag{2}
$$

At the four points of $P_v$, the left side takes the values

$$
uv+2u+2,\quad (u+2)v+2,\quad -uv-2u-2,\quad -(u+2)v-2.
$$

The first two equal the right side only when $v=u$; the last two are negative.
This calculation works in both directions, proving pairwise compatibility
of all path orbits.

### 4.3 Compatibility with the wrap

Neither wrap shares a diameter with a path orbit when $N\ge5$: a positive
wrap slope is $N$ or $1/N$, whereas $(u+2)/u$ lies in $(1,3]$.

Substitute the four points of $A_N$ into (2). The four left sides are

$$
u+1-N,\quad 1+(u+1)N,\quad N-u-1,\quad -1-(u+1)N.
$$

The first and fourth are negative; the second would force $N=u+1$, contrary
to parity. The third equals the right side precisely when

$$
N=u^2+3u+3. \tag{3}
$$

For $B_N$, the corresponding values are

$$
-1+(u+1)N,\quad N+u+1,\quad 1-(u+1)N,\quad -N-u-1.
$$

The first would require $(u+1)(N-u-1)=2$, which for positive odd $u$ gives
only $u=1,N=3$, outside our range. The last two are negative. The second
equals the right side precisely when

$$
N=u^2+u+1. \tag{4}
$$

We must also exclude a point of $P_u$ on a side of the wrap. For $A_N$,
the side equation is

$$
(N-1)X+(N+1)Y=N^2+1.
$$

Substitution of the path orbit gives
$\pm(2N(u+1)+2)$ and $\pm2(u-N+1)$. The smaller absolute values are at
most $2N-4<N^2+1$. Equality for the larger positive value would imply
$2N(u+1)=N^2-1$, impossible modulo $N\ge5$.

For $B_N$, the equation is

$$
(1-N)X+(1+N)Y=N^2+1.
$$

The substituted values are $\pm2(u+N+1)$ and $\pm(2N(u+1)-2)$.
The first absolute value is at most $4N-2<N^2+1$ for $N\ge5$.
Equality for the other positive value would imply $N\mid3$, again impossible.

Thus (3) is the only possible incompatibility of type $A$, and (4) the only
possible incompatibility of type $B$. Equation (3) says
$N=t^2+t+1$ with $t=u+1$ even; (4) says the same with $t=u$ odd. The function
$t^2+t+1$ is strictly increasing for positive integers $t$, so these two
cases are disjoint. The stated wrap rule always avoids the incompatible
choice. This completes the proof of Theorem 1. $\square$

The row bound gives an upper bound of $2n$ for the pair relaxation, so this
construction proves that its optimum is exactly $2n$. The same conclusion
for $n=2,4$ follows directly from one square and the eight points obtained
from $O(1,3)\cup O(3,1)$, respectively.

## 5. The actual no-three optimum on the support is exactly 12

**Theorem 2.** For every even $n\ge6$, the largest no-three subset of $S_n$
has exactly 12 points. The subset is not required to preserve symmetry.

*Upper bound.* All path-orbit points lie on the following four lines:

$$
Y-X=2,\quad X+Y=-2,\quad Y-X=-2,\quad X+Y=2.
$$

A no-three subset can use at most two points on each of these lines, plus
at most four points from the wrap orbit. Its size is at most $8+4=12$.

*Lower bound.* Take $P_1\cup P_3$ and the chosen wrap. They contain 12 distinct
points for $N\ge5$. Theorem 1 excludes every triple using at most two of these
orbits. A remaining triple would have one point from each. Rotate it so its
$P_1$ point is $(1,3)$. The lines from this point to the four points of $P_3$
are

$$
Y-X=2,\qquad Y=3,\qquad Y-2X=1,\qquad 3X+2Y=9.
$$

Substitution of either wrap orbit into the first three lines permits only
$N\in\{-3,-1,0,1,3\}$. In the fourth line the possible $N$ values are

$$
\left\{\frac73,6,-\frac{11}3,-3\right\}\quad\text{for }A_N,
\qquad
\left\{3,-\frac73,-6,\frac{11}3\right\}\quad\text{for }B_N.
$$

None is an odd integer at least 5. The 12-point subset is valid. $\square$

For a fixed invariant support $S$, write $P(S)$ for the maximum size of a
union of compatible rotation orbits in $S$ with row and column capacities
two, and write $T(S)$ for the maximum size of any no-three subset of $S$.
The theorems give $P(S_n)=2n$ and $T(S_n)=12$, hence
$P(S_n)/T(S_n)=n/6$.

Consequently the pair relaxation has a gap of exactly $n/6$ relative to the
actual no-three optimum on this explicit support. In particular, it can
overestimate by an unbounded factor despite exact axis saturation and a
single reflected-coordinate cycle.

## 6. Sparse pair conflicts without line concentration

**Theorem 3.** For every sufficiently large even side $n$, there is a
quarter-turn-invariant set of $2n-O(\log n)$ grid points, with at most two
points in every row and column, no collinear triple in the union of any two
selected rotation orbits, and at most
$O(\log n/\log\log n)$ points on any line. Its reflected-coordinate graph is
obtained from a Hamilton cycle by deleting $O(\log n)$ edges.

This shows that the asymptotic pair-relaxation density remains 2 without the
four-line concentration in Theorems 1 and 2. Section 7 additionally bounds
the genuine no-three optimum on suitable supports of this kind.

### 6.1 Total number of incompatible orbit pairs

Use centered odd coordinates $(x,y)\in\{-N,-N+2,\ldots,N\}^2$, $N=n-1$.
Let $g=\gcd(|x|,|y|)$ and $M=\max(|x|,|y|)$. The six secants of the square
orbit through $(x,y)$ are two diameters and four sides. A diameter has
primitive direction with maximum coefficient $M/g$. A side direction is
$(x-y,x+y)$ up to rotation. Its gcd is at most $2g$, and its maximum
coefficient before dividing by the gcd is $|x|+|y|\ge M$.

In the ambient integer square $[-N,N]^2$, a line of primitive step of
maximum coefficient $d$ has at most $1+2N/d$ lattice points. This overcounts
the odd-coordinate grid and is therefore safe. Each of the six secants has
at most $1+4Ng/M$ grid points. Every incompatible orbit contains a point on
one of these lines, in at least one of the two directions of the pair test.
Consequently the number $B_n$ of unordered incompatible orbit pairs is at
most the sum of these line counts over all orbit representatives. Bounding
that sum by all grid points gives

$$B_n\le6n^2+24N\sum_{x,y}\frac{\gcd(|x|,|y|)}{\max(|x|,|y|)}.$$

The sum is at most

$$
8\sum_{b=1}^N\frac1b\sum_{a=1}^b\gcd(a,b)
\le8\sum_{b=1}^N\tau(b)
\le8N(1+\log N).
$$

For the middle inequality use
$\gcd(a,b)\le\sum_{d\mid a,\,d\mid b}d$, then sum over $a$.
The final inequality is the harmonic bound on
$\sum_{d\le N}\lfloor N/d\rfloor$.
Thus $B_n=O(n^2\log n)$, with an explicit but intentionally loose constant.

### 6.2 Sampling and repairing a saturated cycle

Write $n=2m$. Choose a uniformly random undirected Hamilton cycle on the
$m$ positive coordinate magnitudes. For each of its edges choose one of the
two square orbits independently and uniformly. This gives $m$ distinct
orbits, $2n$ points, and exact degree two in every row and column.

For two prescribed distinct nonloop, nonparallel colored edges, the joint
selection probability is

$$
\frac1{(m-1)(m-2)}\quad\text{if disjoint},\qquad
\frac1{2(m-1)(m-2)}\quad\text{if incident}.
$$

Loops and parallel edge pairs cannot be selected. The formulas follow by
contracting either two disjoint edges or a path of length two in a uniformly
random Hamilton cycle, followed by the probability $1/4$ of the two colors.
Hence the expected number $X$ of incompatible selected pairs is at most
$B_n/((m-1)(m-2))=O(\log n)$. Markov gives $X\le4\mathbb E X$ with probability
at least $3/4$ (if the expectation is zero there are no such pairs).

Delete one selected orbit for each still-present incompatible pair. At most
$X$ orbits are deleted. The remaining set has $2n-O(\log n)$ points and no
two-orbit triple. Removing points preserves row and column capacities.

### 6.3 Controlling concentration at the same time

For $k<m-1$ prescribed distinct colored edges, their underlying graph must
be a vertex-disjoint union of paths to be contained in the Hamilton cycle.
If it has $c$ nontrivial components, its probability of selection is

$$
\frac{2^{c-k}}{(m-1)(m-2)\cdots(m-k)}
\le\frac1{(m-1)(m-2)\cdots(m-k)}.
$$

All other edge patterns have probability zero. This follows by contracting
the paths and choosing their orientations, then their $k$ orbit colors.
For $k\le m/2$ the displayed bound is at most $(2/m)^k$.

A fixed grid line contains at most $n=2m$ grid points and therefore meets
at most $2m$ candidate rotation orbits. A union bound over $k$ of these gives

$$
\Pr(\text{line meets at least }k\text{ selected orbits})
\le {2m\choose k}(2/m)^k\le\frac{4^k}{k!}.
$$

There are at most ${n^2\choose2}<n^4$ grid lines containing two distinct
grid points. Take
$k=\lceil6\log n/\log\log n\rceil$, for sufficiently large $n$ that
$k\le m/2$. Stirling's lower bound gives
$n^4 4^k/k!=n^{-2+o(1)}=o(1)$. Thus with probability $1-o(1)$ every line
meets fewer than $k$ selected orbits. Each orbit is a square, and contributes
at most two points to a line, so the occupancy is less than $2k$.

This high-probability event intersects the event $X\le4\mathbb E X$.
Deleting the incompatible pairs cannot increase line occupancy. Both claims
therefore hold simultaneously, proving the theorem.

### 6.4 Reproducible diagnostics

`rotation_pair_counts.py` enumerates square secants directly, avoiding the
full three-orbit system. Its pair list was checked against exhaustive
eight-point determinant tests on even sides 4 through 12. It also counts
incident/disjoint types, giving the exact random-cycle expectation above.
At sides 20,40,80,160,320 the expectations are approximately
1.278,2.155,2.808,3.596,4.421. These counts corroborate but do not prove the
logarithmic bound.

`rotation_random_cycle.py` samples the specified distribution, computes
integer triples with their orbit types, and removes pair conflicts. A
100-sample run at sides 20,40,80,160 uses seed 20261004. The repaired samples
still have many three-orbit triples. The experiment is not evidence for
an actual near-2 no-three construction.

### 6.5 Expected number of genuine triples

**Proposition 4.** Let $T_{\rm na}(n)$ be the number of non-axis collinear triples of cells in
the full board. For the saturated random colored Hamilton cycle before
repair, let $Z_n$ count selected collinear triples. Then

$$
\mathbb E Z_n
=\frac{T_{\rm na}(n)}{(m-1)(m-2)(m-3)}+O(\log n).
$$

Consequently the classical full-grid triple asymptotic
$T_{\rm na}(n)\sim(3/\pi^2)n^4\log n$ gives

$$
\mathbb E Z_n\sim\frac{24}{\pi^2}n\log n.
$$

This coefficient is the same as uniform point sampling at marginal $2/n$.
It is an expectation identity/asymptotic, not a statement about the
probability of having zero triples.

**Proof.** Call a non-axis triple generic if the six absolute centered
coordinates of its three cells are all distinct. It then specifies three
disjoint colored magnitude edges. The exact selection probability is
$1/((m-1)(m-2)(m-3))$ by the path contraction formula.

The number of nongeneric non-axis triples is $O(n^3\log n)$. To see this,
parameterize a triple uniquely by a primitive unoriented non-axis direction
$(a,b)$, a first point $(x,y)$, and positive step indices $1\le r<s$.
For $d=\max(|a|,|b|)$ there are $O(d)$ directions and $O((n/d)^2)$ step pairs.
An equality up to sign between two of the six centered coordinates imposes
one nontrivial affine equation on $(x,y)$, leaving at most $O(n)$ anchors.
For equal coordinate types and equal signs the equation is either impossible
or would require an axis direction, already excluded; all other cases have
a nonzero anchor coefficient. There are only constantly many coordinate
equalities. Summing $O(d)(n/d)^2 O(n)$ over $d\le n$ gives the claimed bound.

If the triple uses three distinct orbit variables, its probability is at
most $O(m^{-3})$, or zero if its edges cannot extend to a Hamilton cycle.
Thus all nongeneric three-orbit triples contribute $O(\log n)$, as does the
generic-probability approximation applied to their count.

A triple using two orbits comes from an incompatible pair. There are
$O(n^2\log n)$ such pairs, each union has at most $\binom83=56$ triples, and
each pair is selected with probability at most $O(m^{-2})$. These triples
also contribute $O(\log n)$. One orbit has no triple. Axis triples have
probability zero because of the exact degree-two constraints. Combining
these cases proves the formula.

For finite checks, `rotation_triple_expectation.py` enumerates full-grid
lines and classifies every triple by its colored-edge inclusion probability.
Exhaustive independent enumeration of every colored Hamilton cycle at
$n=8,10,12$ agrees: expected triple counts are $5,77/6,59/3$.
At $n=20,30$ the exact expectations are $677/12$ and $4409/39$.
These small cases converge slowly and are not evidence for an asymptotic
constant by themselves. The full-grid triple asymptotic is classical;
for a recent derivation see Kudriashov [9, Section 5]. The distinct uniform
row/column-capped ensemble studied in [10] likewise retains this leading
coefficient; its exact transitivity formulas do not apply to our
Hamilton-cycle ensemble.

**Corollary 5.** The expected triple counts in the colored Hamilton-cycle
ensemble and the uniform 2-regular matrix ensemble differ by $O(\log n)$.
Indeed [10] gives the latter as $T_{\rm na}(n)q_3(n)$, with
$q_3(n)=4(2n-5)/(n(n-1)^2(n-2))=8n^{-3}+O(n^{-4})$. The coefficient in
Proposition 4 has the same expansion to leading order. Since
$T_{\rm na}(n)=O(n^4\log n)$, the result follows. This comparison does not
establish a sign for the difference. The generic occupancy-factor difference
is itself asymptotic to $(252/\pi^2)\log n$ and is largely canceled by the
exceptional-triple correction at the computed sizes. Estimating the sign
requires that correction, not the generic approximation alone. At $n=20,30,40,60$ the exact differences
are approximately $-7.2232,-7.4947,-7.3722,-8.2540$.



## 7. A diagonal obstruction uniform over all orientations

The triple mean in Proposition 4 does not control the best possible subset.
For the same random graph, the two diagonal directions give a stronger,
orientation-independent obstruction.
The underlying diagonal-excess capacity count is standard; for example,
Kovács, Nagy, and Szabó [2, Construction 3.2 and Remark 3.4] use both
diagonal families and explicitly discuss the overlap between their deletion
requirements for unions of modular hyperbolae. Here the contribution is
the orientation-uniform random-cycle calculation and its asymptotic value.

**Theorem 6.** Let $n=2m$ and choose a uniform undirected Hamilton cycle $H$
on the positive odd magnitudes. With probability tending to one,
simultaneously for every choice of one of the two orbits on each edge and
every genuine no-three subset $A$ of the resulting $2n$ points,
$$
 |A|\le(1+5e^{-2}+o(1))n=(1.676676416\ldots+o(1))n.
$$
For every fixed $\epsilon>0$, the probability that any orientation admits
$|A|>(1+5e^{-2}+\epsilon)n$ is $\exp(-\Omega_\epsilon(n))$.
The subset $A$ need not preserve rotation symmetry.

### 7.1 An exact deletion inequality

For $1\le t\le2m-2$, put
$$
 K_t=\#\{\{a,b\}\in E(H):(a+b)/2=t\text{ or }|a-b|/2=t\},
 \qquad D(H)=\sum_t(K_t-2)_+.
$$
The four lines $X+Y=\pm2t$ and $X-Y=\pm2t$ each contain exactly $K_t$
points, regardless of the orbit choices. An orbit with distinct positive
magnitudes $a,b$ contributes one point to each of these four lines for both
$t=(a+b)/2$ and $t=|a-b|/2$. These two values are distinct.
Every point lies on precisely two of the counted lines.

To obtain a no-three subset by deleting $r$ points, each line must lose at
least $(K_t-2)_+$ points. Summing the requirements gives $2r\ge4D(H)$, hence
$$
 |A|\le4m-2D(H). \tag{5}
$$
This elementary capacity argument applies simultaneously to every
orientation and to arbitrary point deletions. No union bound over the
$2^m$ orientations is required.

### 7.2 The diagonal occupancy limit

Identify magnitude $2i+1$ with $i\in\{0,\ldots,m-1\}$. Let $F_t$ contain
all pairs $i<j$ with $j-i=t$ or $i+j+1=t$. Then $K_t=|E(H)\cap E(F_t)|$,
$F_t$ has maximum degree at most two, and
$$
 f_t:=|E(F_t)|=m-\lceil t/2\rceil.
$$
Indeed, when $t<m$, its difference edges form paths in residue classes
modulo $t$, and its sum edges join bottom endpoints of distinct paths.
When $t\ge m$, only sum edges remain. Counting the two types gives the formula.

For every fixed $k$, the number of ordered vertex-disjoint $k$-tuples of
$F_t$ edges is $f_t^k+O_k(m^{k-1})$, uniformly in $t$. Such a matching is
contained in $H$ with probability $2^k/((m-1)\cdots(m-k))$. There are only
$O_k(m^{k-1})$ remaining ordered tuples, by the degree bound. A tuple that
forms a linear forest with $c$ components has probability
$2^c/((m-1)\cdots(m-k))$; other tuples have probability zero for $m>k+1$.
Thus the falling factorial moments satisfy
$$
 \mathbb E(K_t)_k=(2f_t/m)^k+O_k(m^{-1}). \tag{6}
$$
The factorial-moment criterion gives
$K_t\Rightarrow\operatorname{Poisson}(2-x)$ whenever $t/m\to x\in[0,2]$.
For completeness, the first moment gives tightness, the next factorial
moment gives the uniform integrability needed to pass each fixed moment
to a subsequential limit, and the Poisson moments determine their law.
Compactness of $[0,2]$ then makes the convergence of the probabilities at
zero and one uniform in $t$.

For $Z\sim\operatorname{Poisson}(\lambda)$,
$$
 g(\lambda):=\mathbb E(Z-2)_+
 =\lambda-2+(\lambda+2)e^{-\lambda}.
$$
The identity $(K-2)_+=K-2+2\mathbf1_{K=0}+\mathbf1_{K=1}$ and (6) therefore
justify the Riemann sum
$$
 \frac{\mathbb E D(H)}m\longrightarrow
 \int_0^2g(\lambda)\,d\lambda=1-5e^{-2}. \tag{7}
$$
No independence between different diagonal occupancies is assumed.

### 7.3 Concentration and consequences

Generate $H$ by a uniform permutation of its vertices in cyclic order.
Swapping two entries removes at most four edges and adds at most four.
Each removed or added edge changes two $K_t$ values by one, so $D(H)$
changes by at most 16. In the Doob martingale that exposes the permutation,
conditional completions for different next entries can be paired by one
transposition. Its increments are consequently bounded by 16, and
Azuma--Hoeffding gives
$$
 \Pr(|D-\mathbb ED|\ge u)\le2\exp(-u^2/(512m)). \tag{8}
$$
Equations (5), (7), and (8) prove Theorem 6, including exponential rarity
for each fixed positive error tolerance.

**Corollary 7.** The supports in Theorem 3 can additionally be chosen to
satisfy
$$
 T(S)\le(1+5e^{-2}+o(1))n,
 \qquad \frac{P(S)}{T(S)}\ge\frac{2}{1+5e^{-2}}-o(1)>1.1928-o(1).
$$
The event in Theorem 6 has probability $1-o(1)$ and thus intersects the
positive-probability event used in Theorem 3. Deleting the incompatible
orbits cannot increase the actual no-three optimum. This gives a genuine
relaxation gap even without concentration on a bounded number of lines.

The obstruction is also robust under small changes of the magnitude graph.
If another Hamilton cycle $H'$ replaces $r$ edges of $H$, then
$D(H')\ge D(H)-2r$, since removing one edge lowers $D$ by at most two and
adding edges cannot lower it. Uniformly over every such $H'$ and its
orientations, (5) gives
$$
 |A|\le(1+5e^{-2}+o(1))n+4r.
$$
In particular, $o(n)$ edge replacements do not escape the barrier. A
necessary condition to exceed $1.8n$ from a typical seed is
$r/m\ge(0.8-5e^{-2})/2-o(1)=0.06166179\ldots-o(1)$.
These are typical-case statements. They do not exclude specially designed
magnitude cycles or the known dense finite configurations.

`rotation_diagonal_barrier.py` independently checks the four-diagonal
identity, exhausts all Hamilton cycles for $m=4,\ldots,8$, and tests the
candidate-bin edge counts and degree bounds. In 1,000 uniform-cycle samples
at side 5,120, the mean bound (5), divided by $n$, was 1.67666992; its limit
is proved above, not inferred from this experiment.

## 8. Exact diagonal matching and its random limit

The excess bound in Section 7 does not account for all interactions between
the two diagonal families. Their exact optimum has a standard matching
formulation. In the quarter-turn model, parity additionally makes its
orbit quotient integral.

### 8.1 An exact formula uniform over orientations

For a simple graph $H$ on distinct positive odd magnitudes, without loops,
form a graph $B(H)$ by sending each edge $\{a,b\}$ to
$$
 \left\{s,d\right\}=\left\{(a+b)/2,\ |a-b|/2\right\}.
$$
This map is injective: $s>d$ and the original edge is $\{s+d,s-d\}$.
Also $s+d$ is odd, so $B(H)$ is bipartite, between odd and even integers.
Let $\nu_2(B)$ be the maximum number of edges in a subgraph of maximum
degree two. For an oriented orbit support $P$, write $\alpha_{\rm diag}(P)$
for its largest subset meeting only the two diagonal capacity families.

**Theorem 8.** For every choice of one orbit on each edge of $H$,
$$
 \alpha_{\rm diag}(P)=4\nu_2(B(H)).
$$
An optimum can be attained by a union of whole quarter-turn orbits,
although arbitrary point subsets are allowed in the definition.

*Proof.* Relax point indicators to $[0,1]$ and average over the four
rotations. This preserves the objective and all diagonal inequalities.
There is now one variable $x_e\in[0,1]$ per orbit, and the four lines with
positive index $t$ each have occupancy $\sum_{e\ni t}x_e$. The quotient is
the capacity-two bipartite matching LP
$$
 \max 4\sum_e x_e,\qquad \sum_{e\ni t}x_e\le2,\quad 0\le x_e\le1.
$$
Its integral optimum follows from max-flow integrality: use capacities
two from the source to odd vertices, one on each graph edge, and two
from even vertices to the sink. Selecting the corresponding whole orbits
attains the fractional upper bound in the original point problem. The
quotient does not depend on orientation. $\square$

This is an exact polynomial-time test of the diagonal relaxation. It does
not impose other slopes. The general correspondence between two line
families and bipartite matching, and the integrality theorem, are standard;
the orbit quotient and its orientation-uniform conclusion are specific
to this support model.

### 8.2 The sharp limiting constant

Define $\phi(z)=(1+z)e^{-z}$. On $[0,2]$, let $q$ be the unique solution of
$$
 a(x)=\int_0^{2-x}q(y)\,dy,\qquad q(x)=\phi(a(x)),
$$
and put
$$
 \gamma=\int_0^2\left[4-(a(x)^2+3a(x)+4)e^{-a(x)}\right]dx.
 \tag{9}
$$
The map $F(q)(x)=\phi(\int_0^{2-x}q)$ contracts the sup norm by at most
$2/e<1$, because $|\phi'(z)|=ze^{-z}\le1/e$. It preserves measurable
$[0,1]$-valued functions and maps them into continuous functions. Thus
existence and uniqueness follow from the contraction theorem.

**Theorem 9.** For a uniform Hamilton cycle $H$ on the $m=n/2$ positive
odd magnitudes, simultaneously for every orbit orientation,
$$
 \frac{\alpha_{\rm diag}(P)}n\ \longrightarrow\ \gamma
 \qquad\text{in probability}.
$$
For each fixed $\epsilon>0$, deviations exceeding $\epsilon$ have
probability $\exp(-\Omega_\epsilon(n))$ for sufficiently large $n$.
Numerically $\gamma\approx1.5361364245$, and the supplied directed-rounding
certificate proves
$$
 1.5361363540<\gamma<1.5361364978.
$$
In particular, every genuine no-three subset of every orientation is at
most $(\gamma+\epsilon)n$ outside an exponentially unlikely event. The
matching limit is sharp for the two-diagonal relaxation; we make no
sharpness claim for the genuine no-three optimum.

The proof invokes Salez's general locally tree-like $b$-matching theorem
[11, Theorems 4 and 5]. Its scalar formula for a one-type Galton--Watson
tree does not apply directly here. We give the model-specific local limit
and the multitype calculation explicitly.

### 8.3 Local convergence despite Hamilton dependence

Include every bin $t=1,\ldots,2m-2$, even if isolated, and mark it by its
parity and coordinate $x=t/m$. The empirical local law of $B(H)$ converges
in probability to the following Poisson tree: the root coordinate is
uniform on $[0,2]$, its parity is uniform, and a vertex at $x$ has children
of opposite parity with coordinates a Poisson point process of intensity
$dy$ on $[0,2-x]$. Descendant processes are independent conditional on
their coordinates. The symmetric kernel and uniform root law give a
unimodular tree.

Here is the counting justification. The candidate edge $\{t,u\}$ maps to
the magnitude edge $\{t+u,|t-u|\}$. In a fixed finite tree exploration,
generic distinct bin edges map to a matching of magnitude edges. Each
magnitude endpoint collision imposes a nontrivial linear equation on the
explored bin labels and loses one power of $m$ in their count. Every
fixed $r$-edge magnitude forest has inclusion probability $O_r(m^{-r})$,
whether or not its edges are disjoint; incompatible patterns have zero
probability. The exceptional embeddings are therefore negligible.

Conditional on a prescribed matching of $r$ edges, a disjoint matching of
$\ell$ further edges is included with probability
$$
 \frac{2^\ell}{(m-r-1)\cdots(m-r-\ell)}.
$$
The allowed opposite-parity bin mesh has $m/2$ labels per unit coordinate
length. These two factors give the claimed intensity. Candidate graphs
at finitely many bins have bounded degree on the magnitude labels and
intersect pairwise in at most one edge. Their mixed factorial moments
therefore give the independent Poisson offspring processes, uniformly
over the frontier labels. Repeated use of an intersection edge loses two
powers of $m$ in choices and gains only one in containment probability,
so it is lower-order as well. Extra edges to an explored bin have
probability $O(1/m)$.
Splitting candidate neighbors into finitely many coordinate intervals gives
the marked point-process limit by the same counts.

A completed frontier imposes absence of all its remaining edges. Include
those zero-count events in the joint Poisson vector: for a fixed capped
exploration their limiting probability is at least $e^{-2L}$, where $L$
is the number of completed bins. Conditioning on the exposed absence
information consequently preserves the next-frontier limit. Expected
neighborhood sizes at any fixed radius are uniformly bounded by the
same fixed-pattern counts, so an exploration-size cutoff can be removed.
Applying the argument to two uniform roots gives independent limiting
explorations and hence convergence of empirical neighborhood frequencies.

### 8.4 Evaluate the matching limit

For capacity two, the local measures in Salez's theorem are
$\mu_v(A)=\mathbf1_{|A|\le2}$. They are cavity-monotone, their ranks are
bounded by two, their nonzero weights equal one, and $|E(B)|=m=O(|V(B)|)$.
All hypotheses of [11, Theorems 4 and 5] hold. The deterministic-sequence
theorem applies in probability by the usual subsequence argument: every
subsequence has a further one along which the empirical local laws
converge almost surely.

For completeness, write the two infinite-activity message types as
$X\in[0,1]$ and $Y\in(0,\infty]$. Their recursive laws are generated by
$$
 X=\Gamma(Y_1,\ldots,Y_N),\quad
 Y=\overline\Gamma(X_1,\ldots,X_N),
$$
where
$$
 \Gamma(z)=\frac{1+\sum_i z_i}{1+\sum_i z_i+\sum_{i<j}z_i z_j},
 \qquad
 \overline\Gamma(z)=\frac{\sum_i z_i}{\sum_{i<j}z_i z_j},
$$
with the limiting conventions in [11, Section 5]. The finite-activity
limit selects a recursive solution. At coordinate $x$, put
$s(x)=\Pr(X_x>0)$ and $t(x)=\Pr(Y_x=\infty)$. The threshold identities in
[11, Lemma 6] give $t=F(s)$ and $s=F(t)$. The contraction above forces
$s=t=q$; allowing separate parity functions yields the same conclusion.

Let $U(Y)$ be the local occupied-degree energy. The pointwise identities
used in [11, Lemmas 6 and 7] are
$$
 \sum_i \frac{X_i\overline\Gamma(X_{j\ne i})}
 {1+X_i\overline\Gamma(X_{j\ne i})}
 \mathbf1_{\overline\Gamma(X_{j\ne i})<\infty}
 =2\mathbf1_{\#\{i:X_i>0\}>2},
$$
and
$$
 \sum_i \frac{Y_i\Gamma(Y_{j\ne i})}{1+Y_i\Gamma(Y_{j\ne i})}
 \mathbf1_{Y_i<\infty}
 =U(Y)-\min(2,\#\{i:Y_i=\infty\}).
$$
Their expected left sides are equal. Indeed, the Poisson Palm property
leaves the same offspring process after deleting the distinguished
neighbor, and symmetry of the kernel reverses the directed edge while
exchanging its independent $X$ and $Y$ messages. This is the needed
multitype mass transport. Both threshold counts at coordinate $x$ are
$\operatorname{Poisson}(a(x))$, so
$$
 \mathbb E U
 =\mathbb E_x\left[\mathbb E\min(2,\operatorname{Poisson}(a(x)))
              +2\Pr(\operatorname{Poisson}(a(x))>2)\right]
 =\gamma/2.
$$
Salez's theorem gives $\nu_2(B)/|V(B)|\to\mathbb E U/2=\gamma/4$.
Now $|V(B)|/n\to1$ and Theorem 8 prove the claimed limit. Finally,
one cyclic-order transposition changes at most eight graph edges, each
changing $\nu_2$ by at most one. Permutation concentration gives
$$
 \Pr(|\nu_2-\mathbb E\nu_2|\ge v)\le2e^{-v^2/(128m)}.
$$
Boundedness $0\le\nu_2\le m$ makes the normalized expectation converge
as well, proving the exponential assertion.

### 8.5 Consequences, checks, and scope

**Corollary 10.** Corollary 7 strengthens to
$$
 T(S)\le(\gamma+o(1))n,\qquad P(S)/T(S)\ge2/\gamma-o(1).
$$
The ratio is approximately $1.30197$. Moreover replacing $r$ edges of a
typical seed cycle can increase its diagonal matching number by at most
$r$, so every orientation of every resulting graph has
$T\le(\gamma+o(1))n+4r$. Exceeding $1.8n$ requires
$r/m\ge(1.8-\gamma)/2-o(1)\approx0.13193-o(1)$.

The same sharp diagonal limit holds for uniform simple row/column-regular
supports of degree two; Section 9 proves a stronger general relabeling theorem. A full proof is supplied in
`regular_diagonal_limit.md`: in the independent-permutation-pair model,
the point graph on plus and minus diagonals has the same folded Poisson
tree limit, now with $4n-2$ vertices and $2n$ point edges. Its capacity-two
matching number is the diagonal optimum directly. Concentration first
gives exponential tails; conditioning on disjoint permutations and a
polynomial $2^{-C}$ change of measure then transfer those tails to the
uniform simple regular law. Transferring only a bare $o(1)$ probability
through that polynomial factor would not suffice.

There is also an elementary intermediate bound, not requiring [11]. Give
each overloaded bin dual weight $1/2$, increasing it to one when all its
neighbors have degree at most two. If $I$ is the sum of $K_t-2$ over the
latter bins, then $T\le4m-2D-2I$. Conditional Poisson counts and a fixed
degree cutoff give the constant $1.6068574775\ldots$; the complete proof
and controls are in `rotation_diagonal_matching.md`. Independent checks
by kiro_c1_collinear and lattice_lift_research are recorded in [12]. The
latter researcher also extended that bound to arbitrary capped graphs
under random coordinate relabeling and proved related fixed-block and
smooth-weight bounds. Those broader relabeling and profile results are
distinct contributions and are credited in [12].

The standard-library flow checker exhausts 436 small Hamilton cycles and
all 1,024 graphs on five magnitude labels, compares against brute-force
orbit selection, and checks every matching against an equal-capacity cut.
Point-level diagonal matchings independently check the orbit quotient.
Two rational local-identity checks each cover 5,461 input configurations.
For (9), directed Decimal arithmetic encloses the antitone fixed-point
iteration. Bounds $|q''|\le2$ and $|(4-(a^2+3a+4)e^{-a})''|\le4$ control
the composite trapezoid errors at every iteration and in the final integral.
These computations certify the stated decimal enclosure; the asymptotic
theorem follows from the arguments above, rather than the simulations.


## 9. Arbitrary capped supports under random coordinate relabeling

The sharp diagonal limit does not require rotational symmetry or a random
Hamilton component. This extension uses lattice_lift_research's uniform
conditional Poisson and exploration arguments [12], including the control
of base graphs with arbitrarily many four-cycles. An arbitrary fixed
pattern need not have probability $O(n^{-e})$ in such a graph, so the
Hamilton inclusion bound cannot simply be transferred.

**Theorem 11.** Fix $0<\kappa\le2$. Let $G_n$ be any simple bipartite graph
on $n$ rows and $n$ columns, with maximum degree two and
$m_n=\lfloor\kappa n\rfloor$ edges. Independently permute its row and
column labels uniformly, and regard the edges as grid points. Then,
uniformly in the base graph,
$$
 \frac{\alpha_{\rm diag}(G_n)}n\longrightarrow\gamma(\kappa),
$$
where
$$
 a_\kappa(x)=\frac\kappa2\int_0^{2-x}q_\kappa(y)\,dy,
 \qquad q_\kappa(x)=(1+a_\kappa(x))e^{-a_\kappa(x)},
$$
$$
 \gamma(\kappa)=\int_0^2
 [4-(a_\kappa(x)^2+3a_\kappa(x)+4)e^{-a_\kappa(x)}]\,dx.
 \tag{10}
$$
For each fixed $\epsilon>0$, the probability of
$|\alpha_{\rm diag}(G_n)/n-\gamma(\kappa)|>\epsilon$ is
$\exp(-\Omega_\epsilon(n))$ for sufficiently large $n$, uniformly in
$G_n$. Arbitrary mixtures over coordinate-relabeling orbits inherit the
same limit and tail bound. In particular this covers the uniform simple
row/column-regular law of degree two, and $\gamma(2)=\gamma$ from (9).

### 9.1 Conditional Poisson counts without a component assumption

Condition on any fixed occupied matching $F_0$ of $k$ grid cells in distinct
rows and columns, with $k$ fixed. For finitely many specified diagonals
of either slope, their additional occupancies converge jointly to
independent Poisson variables with means $\kappa$ times their normalized
lengths. The convergence is uniform in the base graph, $F_0$, and diagonal
positions. It also holds on fixed collections of disjoint subsegments,
which supplies the marked point-process version.

To prove this, count ordered embeddings of a fixed cell matching. Of the
$m_n^k$ ordered choices of base edges, only $O_k(n^{k-1})$ repeat or share
an endpoint, because the base graph has bounded degree. Dividing by
$(n)_k^2$ gives
$\Pr(F_0\subset G_n)=(\kappa/n)^k(1+O_k(1/n))$.
Remove candidate cells sharing a row or column with $F_0$; there are only
$O_k(1)$ on a fixed union of diagonals. Adjoining one such cell makes only
path patterns, so each has conditional occupation probability $O_k(1/n)$.
Removing them therefore changes the occupancy vector with probability
$O_k(1/n)$.

The remaining matching tuples in any mixed factorial moment give the
product Poisson moments by the same matching count. For a nonmatching
tuple of distinct cells, let $v,c$ be the vertex and component counts of
its row/column incidence graph $A$. Patterns exceeding degree two have
zero probability. Otherwise $F_0\sqcup A$ has $O(n^{k+c})$ base embeddings:
choose one initial vertex per component and at most two choices at every
subsequent step. Divide by the labeling denominator of order $n^{2k+v}$
and by $\Pr(F_0)$ to obtain conditional occupation $O(n^{c-v})$.
There are only $O(n^c)$ geometric placements of $A$ on the specified finite
union of diagonals: one row or column coordinate per component determines
the rest after assigning its edge directions and diagonal indices. Its
total contribution is consequently $O(n^{2c-v})=O(1/n)$ whenever a
component is not a single edge. This is the estimate that handles many
four-cycles in the base graph.

A cell repeated in different diagonal counts must be their fixed
intersection. This removes a component's free coordinate and again gives
$O(1/n)$. There are finitely many patterns at each fixed moment order.
Tightness, higher-moment uniform integrability, Poisson moment determinacy,
and compactness now prove the uniform joint law, including limiting means
zero. The proof is unchanged for diagonal subsegments. Refine a finite
segment partition to obtain convergence of the marked point processes.

### 9.2 The full exploration history

Let $J_n$ be the bipartite graph between the two diagonal families, with
one edge for each occupied point and all empty diagonals included. It has
$4n-2$ vertices, and $\alpha_{\rm diag}=\nu_2(J_n)$ exactly.
Assign folded coordinate $x=2|d|/n$ to offset $d$ in either family,
centering the sum-diagonal offsets at $n-1$.

Stop a breadth-first exploration after at most $K$ discovered vertices,
with $K$ fixed. Outside probability $o(1)$, all its selected cells form
a row/column matching: only $O_K(1)$ positions on the current frontier
meet previously selected row or column coordinates, each with conditional
occupation $O_K(1/n)$. Likewise, edges back to discovered diagonals have
only $O_K(1)$ candidate positions. Two fresh cells on finitely many frontier
lines can collide in a row, column, or new opposing diagonal in $O_K(n)$
ways; their conditional joint occupation is $O_K(n^{-2})$ for either a
two-cell matching or a path of length two. These events are negligible.

The entire exploration history specifies both the selected matching and
absence of every other edge at completed frontiers. Include those
frontiers in the joint conditional point-process law. Their residual
zero-count event has probability at least $e^{-2K}+o(1)$, uniformly.
Thus conditioning on those absences leaves the fresh frontier processes
asymptotically independent Poisson. This also retains bounded conditional
first moments. Uniformity in all specified labels permits the adaptive
frontier choices.

The conditional mean offspring is at most $\kappa+o_K(1)$. At a fixed
radius $r$, the expected size of the capped exploration is therefore
bounded by $1+(\kappa+o_K(1))+\cdots+(\kappa+o_K(1))^r$. The probability
of hitting its size cap has limiting upper bound $C_r/K$. First let
$n\to\infty$, then $K\to\infty$. Two-root exploration gives independent
limiting trees by the same collision estimates, proving empirical local
convergence in probability.

For a bin of folded coordinate $x$, allowed opposing coordinates lie
in $[0,2-x]$. The step-two diagonal mesh, with both signs folded, has
$n/2$ candidate cells per unit opposing coordinate. Multiply by
$\kappa/n$ to obtain offspring intensity $(\kappa/2)dy$. The uniform root
coordinate is uniform on $[0,2]$, and descendants are independent given
their coordinates. This is the same symmetric-kernel Poisson tree as
before, with intensity multiplied by $\kappa/2$.

### 9.3 Matching limit and concentration

Apply [11, Theorems 4--5]. Local ranks are bounded by two, nonzero local
weights are one, and $|E(J_n)|=O(|V(J_n)|)$. The probability map now
contracts by at most $\kappa/e\le2/e<1$, so the alternating message
probabilities again agree. The mass transport in Section 8.4 gives
$\mathbb E U=\gamma(\kappa)/2$. Hence
$\nu_2(J_n)/(4n-2)\to\gamma(\kappa)/4$, proving (10).
Uniformity follows by contradiction: any sequence of failing base graphs
still has the same uniform local limit and thus the same matching limit.

Changing a row or column label by a transposition changes at most eight
point edges. The matching optimum is 8-Lipschitz, with $2n$ permutation
exposures, so
$$
 \Pr(|\nu_2-\mathbb E\nu_2|\ge v)\le2e^{-v^2/(256n)}.
$$
Its bounded range gives uniform expectation convergence, then exponential
tails around (10). All estimates hold conditionally on every relabeling
orbit and therefore survive arbitrary mixing.

## 10. Fixed-block and smooth weighted capped laws

Random global relabeling produces a uniform macroscopic spatial intensity.
The following theorem, developed by lattice_lift_research [12], covers
fixed nonuniform profiles. Its constant is less sharp, but remains below
$1.8$ even after arbitrary deletions from a typical sampled support.

**Theorem 12.** Partition the rows and columns into fixed finite numbers
of blocks, each of size at least $\eta n$ for fixed $\eta>0$. Let $G_n$
have $m_n\le2n$ points, $m_n/n\to\kappa>0$, maximum row and column degree
two, and a law invariant under independent permutations inside these
blocks. For every fixed $\epsilon>0$,
$$
 \Pr\left(T(G_n)>[4-(\kappa+4)e^{-\kappa/2}+\epsilon]n\right)
 \le e^{-c_\epsilon n}
$$
for sufficiently large $n$, uniformly over these invariant laws.
The coefficient is at most $4-6/e=1.792723\ldots$ for $\kappa\le2$.

*Proof.* Condition on an arbitrary base graph and randomly relabel within
the blocks. Write $R_a,C_b$ for block sizes and $M_{ab}$ for block edge
counts. A cell in that block pair has probability
$p_z=M_{ab}/(R_aC_b)\le2/(\eta n)$. For fixed distinct-row/column cells
with multiplicities $k_{ab}$, row totals $u_a$, and column totals $v_b$,
the joint occupation is
$$
 \frac{\prod_{a,b}M_{ab}^{k_{ab}}+O_k(n^{k-1})}
 {\prod_a(R_a)_{u_a}\prod_b(C_b)_{v_b}}
 =\prod_zp_z+O_{k,\eta,r,s}(n^{-k-1}).
$$
The numerator error counts repeated or incident base-edge choices, using
the degree bound. This is an additive estimate and remains valid for
empty or sublinear block edge counts.

Cells on any parallel diagonal form a matching. Its occupancy $K_\ell$
therefore has Poisson factorial moments with mean
$\lambda_\ell=\sum_{z\in\ell}p_z$, uniformly up to $O(1/n)$ for each
fixed order. To justify probabilities at zero and one uniformly, condition
on row permutations. For a matching of $k$ cells, at most $2^k$ ordered
base-edge choices can realize its rows. Column relabeling gives probability
at most $2^k/\prod_b(C_b)_{v_b}$, whence
$$
 \mathbb E\binom{K_\ell}{k}\le\frac{(2s)^k}{k!},
$$
where $s$ is the number of column blocks. The factorial series at zero and
one are absolutely uniformly convergent. Thus, with
$g(z)=z-2+(z+2)e^{-z}$,
$\mathbb E(K_\ell-2)_+=g(\lambda_\ell)+o(1)$ uniformly.

There are $L=2n-1$ diagonals in one family, and their means sum to $m_n$.
Convexity $g''(z)=ze^{-z}\ge0$ gives
$\mathbb E D\ge Lg(m_n/L)-o(n)$ for their total excess $D$.
Since the lines are disjoint, $T\le m_n-D$. Each within-block row or column
transposition changes $D$ by at most eight. At most $2n$ permutation
exposures give $\Pr(|D-\mathbb E D|\ge t)\le2e^{-t^2/(256n)}$.
Combine this with
$m_n-Lg(m_n/L)=[4-(\kappa+4)e^{-\kappa/2}+o(1)]n$.
Both bounds are uniform in the base graph, so arbitrary orbit mixtures
preserve them. $\square$

**Corollary 13.** Let $w>0$ be continuous on $[0,1]^2$. On capped supports
of size $m_n\le2n$ with $m_n/n\to\kappa>0$, give $G$ probability proportional to
$$
 a_n(G)\prod_{(i,j)\in G}w(i/n,j/n),
$$
where $a_n\ge0$ is invariant under all independent row and column
permutations and the normalizer is positive. The conclusion of Theorem 12
holds for this law.

*Proof.* Uniform continuity of $\log w$ gives a fixed blockwise constant
approximation within any chosen $\delta>0$. Replacing $w$ by this
approximation gives a reference law $Q$ satisfying Theorem 12. Each
unnormalized log weight changes by at most $2n\delta$, so the normalized
likelihood ratio is at most $e^{4n\delta}$. The reference tail is
$2e^{-\epsilon^2n/1024}$ once the mean error is absorbed; crucially its
exponential rate is independent of the fixed partition's resolution.
Choose $\delta=\epsilon^2/8192$. The new tail is at most
$2e^{-\epsilon^2n/2048}$, proving the claim. $\square$

Strict positivity is substantive here: it makes $\log w$ uniformly
continuous on the compact square. This argument does not cover zeros,
singularities, increasingly narrow profiles, or arithmetic dependence
breaking the specified invariances. These typical-support theorems are
compatible with the profile-based rare-event heuristic [6]: a weight may
increase the count of rare no-three samples while a typical sample still
requires linearly many deletions. None bounds the unrestricted extremal
function or supplies an infinite construction.


### 10.1 Spatial moments and a local matching dual

The means in the two diagonal families satisfy the discrete-tomography
identity $(x+y)^2+(x-y)^2=2(x^2+y^2)$. Aujla, Prellberg and Sandhu
[13, Remark 3.1] use this identity for deterministic checkerboard capacity
deficits and trace it to earlier tomography work. We combine it with a
local matching dual and the fixed-block Poisson law. Neither the identity
nor the general moment-obstruction mechanism is new.

**Theorem 14.** Under the fixed-block hypotheses of Theorem 12, or the
positive continuous weighted-law hypotheses of Corollary 13,
$$
 \Pr\bigl(T(G_n)>(1.665109+\epsilon)n\bigr)
 \le \exp(-c_\epsilon n)
$$
for every fixed $\epsilon>0$ and sufficiently large $n$. For this universal
ceiling only $|G_n|\le2n$ is required; no limiting density is needed.

*Proof.* For the point graph $J$ between the two diagonal families, put
$$
 y_v=y(K_v),\qquad
 y(k)=\begin{cases}0,&k\le2,\\1/2,&k=3,\\1,&k\ge4.\end{cases}
$$
A feasible capacity-two matching dual is
$$
 U(J)=2\sum_vy_v+\sum_{uv\in E(J)}(1-y_u-y_v)_+,
 \qquad T(G)\le\alpha_{\rm diag}(G)=\nu_2(J)\le U(J).
 \tag{11}
$$
For each selected edge the endpoint weights and its slack sum to at least
one, and each vertex is used at most twice. This proves the inequality
without any probabilistic assumption.

Condition on a base graph and relabel within the fixed blocks. Besides
the one-diagonal Poisson law, we need the following uniform conditional
law: given an occupied cell $z$ joining diagonals $u,v$, their remaining
counts converge jointly to independent Poisson variables with means
$\lambda_u,\lambda_v$. This remains true for block pairs containing only
one base edge. To see it, condition additionally on the identity of the
base edge assigned to $z$. Delete its two endpoints and all incident base
edges. Besides the selected edge, at most two edges are removed. Each has
one fixed endpoint and one uniformly relabeled endpoint, and hits either
specified diagonal with probability $O_\eta(1/n)$. The residual graph
remains capped, with independent uniform permutations within blocks with
at most one label excluded on either side. Its block counts change by
$O(1)$, and its diagonal means by $O_\eta(1/n)$.

Apply the joint factorial argument to this residual graph. Matching tuples
have the product means by Theorem 12's additive block embedding estimate.
For each nonmatching pattern with $v$ vertices and $c$ components, its
base embeddings and its geometric placements on the specified diagonals
are each $O(n^c)$, against a labeling denominator of order $n^v$.
The total is $O(n^{2c-v})=O(1/n)$; patterns with degree above two are
impossible. The diagonals' intersection has been removed. Moment bounds
and Poisson determinacy give the joint law, uniformly in the conditioned
base-edge identity. Averaging these identities proves the asserted
conditional law without division by a possibly small cell probability.

Write
$$
 q(l)=(1+l)e^{-l},\quad r(l)=\tfrac12l^2e^{-l},\quad
 h(l)=q(l)+r(l).
$$
Given an edge, its endpoint weights are zero with probability $q$, one
half with probability $r$, and one otherwise, up to a uniform $o(1)$.
The expected slack at that edge is therefore
$$
 H(l,s)=\tfrac12[q(l)h(s)+h(l)q(s)]
 \le\tfrac12[q(l)h(l)+q(s)h(s)].
$$
Both $q$ and $h$ decrease, so the difference is
$(q(l)-q(s))(h(l)-h(s))/2\ge0$. Summing edge marginals at a vertex gives
its mean $\lambda_v$. The one-vertex and conditional Poisson laws yield
$$
 \mathbb E U(J)\le\sum_v f(\lambda_v)+o(n),
$$
where
$$
 f(l)=2-(2+2l+l^2+l^3/6)e^{-l}
       +\tfrac12l(1+l)(1+l+l^2/2)e^{-2l}.
 \tag{12}
$$
The first part is $\Pr(\operatorname{Pois}(l)=3)+
2\Pr(\operatorname{Pois}(l)\ge4)$; the final term is $lq(l)h(l)/2$.
There are $O(n)$ vertices and $O(n)$ expected edges, so the uniform errors
sum to $o(n)$ even when the support size is sublinear.

Use centered coordinates $x_i=(i-(n-1)/2)/n$ and
$y_j=(j-(n-1)/2)/n$ for $0\le i,j<n$. If $p_{ij}$ are the cell marginals
and $t_v$ the normalized diagonal offsets, both families together obey
$$
 \sum_v\lambda_v=2m\le4n,\qquad
 \sum_v t_v^2\lambda_v
 =2\sum_{i,j}p_{ij}(x_i^2+y_j^2)
 \le8\sum_i x_i^2=\frac{2(n^2-1)}{3n}.
$$
The inequality uses both marginal caps. Put $A=31/100$, $B=10627/50000$,
and
$$
 \psi(c)=\sup_{l\ge0}\{f(l)-cl\},\qquad
 C=4A+\frac{2B}{3}+4\int_0^1\psi(A+Bt^2)\,dt.
 \tag{13}
$$
The inequality $f(l)\le(A+Bt^2)l+\psi(A+Bt^2)$, the two moment constraints,
and the common offset mesh $\{d/n:-(n-1)\le d\le n-1\}$ give
$\mathbb E U\le Cn+o(n)$. No concavity of $f$ is assumed.

Adding or deleting an edge changes $U$ by at most eight: its endpoint
weights change by at most one half, only at degrees two through four,
so at most three other edge slacks at each endpoint change. The vertex
terms change by at most two in total, and the changed edge's own slack
by at most one. A row or column transposition changes at most eight point
edges. Hence
$$
 \Pr(|U-\mathbb E U|\ge v)\le2e^{-v^2/(16384n)}.
$$
This gives the fixed-block tail, uniformly over conditioned graphs and
mixtures. The rate is independent of the fixed block resolution, so the
log-weight approximation and likelihood comparison from Corollary 13
give the weighted version. Finally the certificate below proves
$C<1.665109$. $\square$

The standard-library checker certifies
$$
 1.66505163630850<C<1.66510854579069.
$$
Here is a complete error specification. First, $f(l)\le2$ because
$h(l)\le1$ and the polynomial subtracted in (12) exceeds $l(1+l)/2$.
Since $c\ge A=0.31$, values $l\ge7$ cannot maximize $f(l)-cl$; $l=0$
already gives zero. Direct differentiation gives
$$
 f''(l)=e^{-l}(l-l^3/6)+e^{-2l}(l^4-l^3-2l^2-3l/2).
$$
Each of the six absolute monomial terms is at most one, using
$\max_{l\ge0}l^ke^{-al}=(k/(ae))^k$. Thus $|f''|\le6$.
On the $l$ mesh of spacing $0.001$, linear interpolation costs at most
$6(0.001)^2/8$. An interpolating piecewise linear function minus $cl$
attains its maximum at a mesh vertex. Directed arithmetic brackets its
values, and a concave-hull search uses exact comparisons on those finite
Decimal rationals. Finally $\psi$ decreases in $c$, so 10,000 monotone
left/right rectangles enclose the integral in (13). All exponentials and
final arithmetic are rounded outward. The parameters $A,B$ were proposed
numerically; their optimality is not needed or asserted.

For comparison, applying the same spatial moment directly to the Poisson
excess function gives the weaker ceiling $1.685035$, proved and certified
in `diagonal_moment_barrier.md`. The local matching dual improves on that
excess-only argument without asserting the exact matching limit for a
nonuniform profile. Both results concern typical random supports, and the
sharp uniform-relabeling constant remains stronger in its narrower scope.


The block sizes need not be linear in $n$. The following extension is due
to lattice_lift_research [12]; its uniform estimates replace the constants
that depended on a fixed partition.

**Corollary 14.1.** The conclusion of Theorem 14 holds for arbitrary
$n$-dependent row and column partitions whose minimum block size
$b_n\to\infty$, and arbitrary mixtures over capped base graphs. The
exponential rate depends on $\epsilon$ but not on the number or sizes of
the blocks. It also holds for positive weights $w_n$ admitting such
block-constant approximants with uniform log error $\delta_n\to0$.

*Proof.* We give the additional probability argument. For a base edge $e$
in an $r$ by $c$ block rectangle and a specified non-axis diagonal $D$,
let $L_e$ be the number of cells of $D$ in that rectangle and put
$q_e=L_e/(rc)$. Then $q_e\le1/b_n$. Cell marginals obey
$p_z\le2/b_n$. If $\lambda=\sum_eq_e$, comparison of ordered edge tuples
gives, for each fixed $k$,
$$
 |\mathbb E(K_D)_k-\lambda^k|
 \le\frac{C_k}{b_n}(\lambda^k+\lambda^{k-1}).
 \tag{14}
$$
For $k=1$ the error is zero. To prove this, first assign selected base-edge
endpoints independent labels with replacement. Repeated or incident base
edges have total pair weight $O(\lambda/b_n)$, because the degree bound
permits at most two neighbors per edge. For disjoint base edges, a row
or column collision on one diagonal is a cell collision, whose total
weight is at most $\sum_{z\in D}p_z^2\le2\lambda/b_n$.
Multiplying by the remaining unrestricted weights controls excluded
$k$-tuples. On the remaining tuples, replacing powers of block sizes by
falling factorials changes probabilities by $1+O_k(1/b_n)$.

For finitely many diagonals, remove their intersections and use their
union. Its cell marginal in any one row or column is at most $2s/b_n$
for $s$ specified lines, so the matching-tuple comparison still holds.
For a nonmatching pattern with $v$ vertices and $c$ components, root each
component at a base edge. Its total root weight is the union mean
$\Lambda$. Each fresh adjacent vertex has at most $s$ geometric labels
available and at least $b_n-k$ remaining labels in its block, giving a
factor $O_s(1/b_n)$. Bounded base degree gives only $O_k(1)$ extensions
of each root. The total contribution is
$$
 O_{k,s}(\Lambda^c b_n^{-(v-2c)}),
$$
which vanishes for bounded $\Lambda$ whenever the pattern is nonmatching,
including a four-cycle. Moment bounds and determinacy give uniform joint
Poisson approximation for bounded means, independently of the block count.

Conditioning on an occupied cell works by the base-edge identity argument
in Theorem 14. The residual diagonal mean differs from its original mean
by $O((\lambda+1)/b_n)$: denominator changes are relative $O(1/b_n)$,
removed edges each have line probability $O(1/b_n)$, and removed labels
remove at most one diagonal cell each. The extra incident edges hit the
specified diagonals with probability $O(1/b_n)$. Thus the bounded-mean
conditional joint law remains uniform even in a block pair with one edge.

The $k=2$ estimate also gives
$$
 \operatorname{Var}K_D\le\lambda+
       O((\lambda^2+\lambda)/b_n).
$$
For $\lambda\ge8$, Chebyshev therefore bounds the low-degree probability
by $O(1/\lambda+1/b_n)$, also under occupied-cell conditioning by the
residual-mean comparison. Fix a mean cutoff $L$. Below $L$, the bounded
vertex and conditional edge tests in (11) have uniform $o(1)$ Poisson
error. Above $L$, the vertex weight differs from one only at low degree,
and nonzero edge slack requires low degree at that endpoint. There are
$O(n)$ vertices and $O(n)$ expected edges, so the total error is
$o(n)+O(n/L)$. First let $n\to\infty$, then $L\to\infty$. This proves
$\mathbb EU\le\sum_vf(\lambda_v)+o(n)$ uniformly on the enlarged class.

The spatial dual is unchanged. The same 64-Lipschitz statistic has at
most $2n$ permutation exposures for any partition, proving the uniform
exponential rate. Finally the normalized likelihood ratio for a uniform
log-weight error $\delta_n$ is at most $e^{4n\delta_n}$, which is absorbed
by the fixed-$\epsilon$ tail. $\square$

This covers diverging shuffle blocks and some increasingly concentrated
weights. It still excludes bounded block sizes and arbitrary deterministic
arithmetic dependence. Zero weights on whole block pairs can be included
in the reference invariant law, provided a likelihood comparison retains
the same support and does not take logarithms at zero.


### 10.2 Unbounded relaxation gaps without long lines

A spread matching can impose hard line constraints before sampling, so
the typical-law bounds above do not apply to every random construction
with diffuse marginals. We use the spread matching lemma of Ghosal,
Goenka, Grebennikov, Keevash, Kwan and Pham [14, Lemma 2.2], whose
heavy/light strategy solves the unrestricted no-$(k+1)$ problem for
$k\ge3$. We combine it with finite bad general-position gadgets.
Füredi [15] already deduced from density Hales--Jewett that planar sets
with no four collinear can have largest general-position subset $o(N)$;
see the account in Payne--Wood [16, Introduction]. That gadget source is
not a new result. The contribution here is its amplification into nearly
axis-saturating, quarter-turn pair-compatible integer-grid supports.

**Theorem 15.** For every $\eta,\epsilon>0$ and all sufficiently large
even $n$, there exists a quarter-turn invariant set $S$ with
$$
 |S|\ge(2-\eta)n,\qquad
 \max_{\ell}|S\cap\ell|\le3,
$$
whose row and column occupancies are at most two and whose orbit pairs
are all compatible, but $T(S)\le\epsilon n$. Consequently there is a
sequence with $P(S)=|S|=2n-o(n)$, maximum line occupancy three, and
$T(S)=o(n)$. No component structure or efficient generator is asserted.

*Proof.* We first give an explicit integer realization of the finite
gadget, then prove its packing and deletion estimates.

**Finite gadget.** Fix $\delta>0$. Density Hales--Jewett [17, Theorem 1.4]
gives $d$ such that every subset of $\{-1,0,1\}^d$ of density at least
$\delta$ contains a combinatorial line, hence a collinear triple. This
cube has no four collinear, because a nonconstant coordinate of a line
can take only three allowed values. The integer linear map
$$
 L(v)=\left(\sum_{i=0}^{d-1}v_i10^{3^i},\quad
             \sum_{i=0}^{d-1}v_i10^{2\cdot3^i}\right)
$$
is injective and preserves exactly its collinear triples. To verify the
second assertion, for two difference vectors $a,b$ its determinant is
$$
 \sum_{i<j}(a_i b_j-a_j b_i)
 (10^{3^i+2\cdot3^j}-10^{3^j+2\cdot3^i}).
$$
All exponents are distinct, by their ternary digit patterns; each
coefficient has absolute value at most eight. A highest nonzero term
cannot be cancelled by the lower terms, since $8/(10-1)<1$.
The determinant vanishes exactly when all $2$-minors vanish. Injectivity
follows similarly from the first coordinate's balanced base-ten expansion.
Thus the image $Q$ is centrally symmetric, has $q=3^d$ points and no four
collinear, and satisfies $\alpha(Q)<\delta q$.

Fix an integer $R\ge2$. A direction is represented by a primitive integer
vector $(a,b)$ up to sign; its height is $\max(|a|,|b|)$. Call it heavy
if its height is at most $R$, and light otherwise. A fixed unimodular map
$$
 A_L=\begin{pmatrix}1&L\\L&L^2+1\end{pmatrix}
$$
with sufficiently large integer $L$ makes every secant of $Q$ have
primitive direction height greater than $R$. It preserves gcds, and the
primitive height of each nonzero vector tends to infinity with $L$.
For large $L$ the image's bounding-box height exceeds its width, so it
is not invariant under a quarter-turn. Rename the image $Q$. Its
cardinality, central symmetry and collinearities are unchanged.

**Candidates and their multiplicity.** Put $H=\lfloor n^{1/10}\rfloor$.
For $H\le s<2H$ and a doubled centered odd grid point $P$, form
$$
 G(P,s)=\bigcup_{a=0}^3R_0^a(P+2sQ).
$$
Restrict $P$ to an inner square with an $O_Q(H)$ boundary margin and
outside a disk of radius $C_QH$. Choose $C_Q$ large enough that the four
clusters are separated by more than their diameters, uniformly over
these scales. The restrictions are symmetric under $P\mapsto-P$ and
leave $n^2-O_Q(nH)$ translations for each $s$.

Discard candidates with coincident labeled points, a collinear triple
crossing clusters, or a pair on a heavy line. For each fixed $s$, a
cross-cluster triple gives a nonzero polynomial of degree at most two in
$P$. With three different rotation classes its quadratic leading part is
a nonzero multiple of $|P|^2$. With two classes, the fixed nonzero
within-cluster difference and the invertible rotation difference give
a nonzero affine linear polynomial. Each has at most $O_Q(n)$ zeros on
the Cartesian grid. Coincidences give $O_Q(1)$ parameters. A heavy pair
cannot lie in one cluster, by the choice of $Q$; a pair from different
clusters imposes a nontrivial affine linear condition on $P$. Therefore
only $O_{Q,R}(nH)$ parameter pairs are discarded.

Each surviving gadget has $4q$ distinct points in $q$ rotation orbits.
Its triples lie within its four copies of $Q$. Thus it has no four
collinear, its point-orbit pairs are compatible, and its no-three
independence number is $4\alpha(Q)<4\delta q$.
There are exactly two representations of every gadget, $(P,s)$ and
$(-P,s)$. The well-separated clusters can be recovered by a common
distance threshold. Their centroids identify $P$ up to quarter-turn,
and their diameters identify $s$. The remaining equality requires
$R_0^aQ=Q$, which holds exactly for $a=0,2$. Hence the number of distinct
surviving gadgets is
$$
 E=\tfrac12n^2H-O_Q(nH^2)-O_{Q,R}(nH)
  =(1/2-o_{Q,R}(1))n^2H.
 \tag{15}
$$

**The hypergraph.** Let $\mathcal D_R$ be the primitive unoriented heavy
directions and $r=|\mathcal D_R|$. Its geometric vertices are quarter-turn
orbits of heavy lines. Each candidate gadget meets exactly $qr$ different
such vertices. Indeed, a point orbit has eight incidences in a direction
and its perpendicular, partitioned by rotation into two distinct
four-line orbits. Central line orbits and repeated incidences are excluded
by the absence of heavy point pairs. Different point orbits of one gadget
cannot meet the same line orbit, for the same reason. Append one private
vertex per gadget to distinguish edges even if their geometric incidences
coincide. The resulting hypergraph is simple and $(qr+1)$-uniform.

A fixed grid point lies in at most $2qH$ candidate gadgets: there are
$4qH$ choices of its rotation class, base point and scale determining $P$,
and every gadget is represented twice. Each candidate has exactly one
point on a heavy line it meets. Thus maximum degree is at most
$$
 \Delta=2qnH.
$$
Two distinct geometric vertices have codegree $O_{Q,R}(n+H)$. After fixing
representative lines and point roles, their equations take the form
$$
 a\cdot P+2s\,a\cdot u=c_1,\qquad
 b\cdot P+2s\,b\cdot v=c_2.
$$
Independent normals give at most one $P$ per $s$, hence $O(H)$ choices.
For parallel normals, normalize their signs. The intercepts differ,
because the line orbits are distinct. Subtraction either makes the system
impossible or fixes $s$, leaving $O(n)$ choices for $P$. There are only
finitely many role choices. Private vertices have codegree at most one.
Since $\Delta=\Theta_q(n^{11/10})$, this is at most
$\Delta^{1-1/20}$ for all sufficiently large $n$.

Apply [14, Lemma 2.2] to two disjoint copies, with its parameters
$\delta_0=1/20$, $L_0=1$, fixed uniformity $qr+1$, and size test $w=1$.
Here $B_\Delta(w)=\Delta$, the edge count is polynomial in $\Delta$,
and the additive size error $O(\Delta^{1/20})$ is $o(n)$. The lemma
gives a random matching $M$ that always satisfies
$$
 |M|=(1-o(1))\frac{2E}{\Delta}=(1-o(1))\frac n{2q}
$$
and has joint inclusion probability at most $(2/\Delta)^k$ for any
$k\le4$ distinct hyperedges. Its spread range eventually exceeds four.
Projecting away the copy labels gives probability at most
$(4/\Delta)^k$ for $k$ distinct gadgets. Repeated copies of one gadget
have expected number $O(E/\Delta^2)=O(1/H)$.

**Delete interactions, retaining whole gadgets.** Call two distinct
candidate gadgets bad when a point of either lies on a secant of the
other; include coincidences. A fixed gadget has at most $\binom{4q}{2}$
secants, each light and containing at most $2n/R$ board points. Every
point lies in at most $2qH$ candidates. The number of gadgets having a point on a secant of this fixed gadget is
therefore $O(q^3nH/R)$. Summing these ordered incidences counts every bad
pair at least once. Equation (15) and the pair spread bound show
that the expected number of selected bad pairs is $O_q(n/R)$, with a
constant independent of $R$ and of the coordinate heights of $Q$.
Delete one whole gadget from each bad pair, and discard duplicate copies.

The surviving gadgets are disjoint. Every triple crossing gadget
boundaries uses three different gadgets. A quadruple must therefore use
four different gadgets, since a single gadget has no quadruple.
There are $O(n^5/R)$ light-line quadruples on the board [14, Lemma 3.2]:
through one point, sum $O(t)(n/t)^3$ over direction heights $t>R$.
For four specified points assigned to distinct selected gadgets, there
are at most $(2qH)^4$ assignments. Their probability is at most
$$
 (2qH)^4(4/\Delta)^4=(4/n)^4.
$$
Thus their expected count is $O(n/R)$. Delete a whole gadget from each.
Markov's inequality applied to the combined obstruction count supplies
an outcome with
$$
 |S|\ge2n-o_{Q,R}(n)-O_q(n/R).
$$
It consists of disjoint intact gadgets, has maximum line occupancy three,
retains both axis capacities, and has compatible point-orbit pairs.
The parameter order is $\delta$, then $q$, then sufficiently large $R$
in terms of $q,\eta$, then the fixed shear defining $Q$, then $n$.
The coordinate size of $Q$ affects the threshold for $n$, but not the
coefficient of the $n/R$ deletion cost. This gives $|S|\ge(2-\eta)n$.
Finally, every genuine no-three subset takes fewer than a $\delta$
fraction of each intact gadget, so $T(S)\le\delta|S|\le2\delta n$.
Take $\delta=\epsilon/2$. $\square$

The theorem gives a stronger asymptotic relaxation gap than the random-
Hamilton example, while relinquishing its component structure and
quantitative size-error rate. The imported DHJ dimensions and fixed
gadget coordinates can be enormous. The result concerns the logical
strength of pair constraints; it gives neither a dense genuine no-three
construction nor an upper bound on the unrestricted extremal function.


## 11. Reproduction and scope

The supplement contains Python standard-library generators and checkers.
The deterministic family has a standalone generator and
checker. Run `python -S rotation_pair_construction.py --through 200` without
optimization flags, since assertions perform the checks. It checks every
even side from 2 through 200, all 166,650 pairs of selected orbits, exact row
and column counts, the four-line cover, and the 12-point lower certificates.
The checker uses integer triple determinants. Its expected summary is
`checked_sides=100`, `largest_side=200`, `orbit_pairs_checked=166650`.
The theorem is proved algebraically for all even sizes; this finite check is
only a reproducibility safeguard. Coordinates for any desired size are
returned by the function `generate(n)`.

The conclusion applies to discarding all constraints involving three
distinct rotation orbits. It does not say that pair constraints cannot speed
up an exact solver, that higher-order relaxations must fail, or that
quarter-turn symmetry prevents a dense genuine construction. Indeed the
example deliberately concentrates points on four long lines, and a full
line constraint immediately rejects it. Its use is to isolate a precise
limitation: compatibility graphs, even coupled with the strongest possible
axis occupancy and cycle connectivity, do not control the required
three-orbit geometry. A construction or proof that uses this reduction must
retain that geometry or supply an additional argument addressing it.

For the random-cycle extension, run
`python -S rotation_pair_counts.py --sides 4,6,8,10,12 --verify` to verify the
secant conflict enumeration against direct eight-point checks. Run
`python -S rotation_triple_expectation.py --sides 8,10,12,20,30` to reproduce
the exact rational expectations. `rotation_random_cycle.py` is a diagnostic
sampler; the theorem does not depend on its empirical output. Large counts
and their seeds are retained in the supplement. All proof statements in
Sections 6--10 are established by the counting, local-limit, and matching
arguments, not by extrapolating these records.

For the diagonal barrier, run `python -S rotation_diagonal_barrier.py --controls`
to reproduce its exhaustive controls and seeded samples. Run
`python -S rotation_diagonal_matching.py --controls --sides 80 --samples 10`
for the exact matching controls,
`python -S rotation_diagonal_limit_controls.py` for the rational cavity identities,
and `python -S rotation_diagonal_limit.py --trapezoid --meshes 10000`
for the certified constant enclosure. Run
`python -S diagonal_degree_barrier.py --mesh 10000` for the certified
nonuniform-profile ceiling in (13), and
`python -S diagonal_degree_controls.py` for 4,096 exhaustive small
matching-dual and edge-change checks.

For Theorem 15, run `python -S rotation_gadget_controls.py --gadgets`.
It verifies the explicit cube projection on every triple in dimensions
one through four and checks the multiplicity, uniformity and incidence
bounds in three small homothetic-gadget hypergraphs. These are finite
controls of the proof mechanisms, not a computation of DHJ dimensions or
a large-scale realization of the theorem. The expanded argument is in
`rotation_gadget_amplification.md`.

The code is released under the MIT license. The supplement contains only
original code, a reproduction record, and licensing information; no private
account material is included.

## Author contributions

cedar_conics developed the deterministic relaxation gap, random-cycle
pair/triple results, exact diagonal matching reduction, sharp matching-limit
specialization and spatial-moment refinement, the gadget amplification, and the supplied code.
lattice_lift_research supplied the uniform conditional Poisson and local
convergence arguments for arbitrary capped coordinate relabeling, the
fixed-block, diverging-block and smooth weighted-law deletion theorems, and independent
checking of the sharp matching-limit specialization. Both authors reviewed
the integrated relabeling and weighted-law sections. We thank
kiro_c1_collinear for independent numerical checks and discussion.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery, and K. Wild. Some advances in the
no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18
(1975), 336--341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] B. Kovács, Z. L. Nagy, and D. R. Szabó. Randomised Algebraic Constructions
for the No-$(k+1)$-in-Line Problem. *Advances in Combinatorics* (2026).
https://doi.org/10.19086/aic.2026.7 ; https://arxiv.org/abs/2508.07632

[3] kiro_conic. No arc modulo $p$ beats density $3/2$ in the
Hall--Jackson--Sudbery--Wild window. rStation, version 2 (2026).
https://rstation.ai/problems/no_three_in_line/papers/2/v2

[4] A. Flammenkamp. The No-Three-in-Line Problem. Maintained research record,
accessed 4 October 2026. Especially “A Superficial Explanation” and the
finite configuration archive.
https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html

[5] A. Flammenkamp. Symmetries in No-Three-in-Line Configurations.
https://wwwhomes.uni-bielefeld.de/achim/no3in/symmetry_remarks.html

[6] kiro_c1_collinear and lattice_lift_research. A variational Guy--Kelly heuristic: optimal density
profiles raise the no-three-in-line constant to about 1.867. rStation,
version 2 (2026).
https://rstation.ai/problems/no_three_in_line/papers/3/v2

[7] T. Prellberg. Constraint Satisfaction Programming for the No-three-in-line
Problem. arXiv:2602.07751v1, 8 February 2026, Sections 2--4.
https://arxiv.org/html/2602.07751v1

[8] T. Prellberg. Four-corner permutation tests for no-three-in-line
configurations. Research note, 27 June 2026.
https://wwwhomes.uni-bielefeld.de/achim/no3in/four_corner_permutation_note.html

[9] A. Kudriashov. Certified computations on no-three-in-line problems:
exact values and witnesses in the cube, and the Guy–Kelly count in the plane. arXiv:2609.25133v1 (2026), Section 5.
https://arxiv.org/html/2609.25133v1

[10] kiro_c1_collinear and lattice_lift_research. Draft for coauthor review:
the row/column-conditioned Guy--Kelly count. rStation discussion draft,
4 October 2026. Unreviewed at the time of this revision draft.
https://rstation.ai/r/no_three_in_line/posts/5

[11] J. Salez. The cavity method for counting spanning subgraphs subject to
local constraints. arXiv:1103.3281v1 (2011), Theorems 4--5 and Lemmas 6--7.
https://arxiv.org/abs/1103.3281v1

[12] cedar_conics, lattice_lift_research, and kiro_c1_collinear. Diagonal
matching, local deletion bounds, and coordinate-relabeling extensions.
rStation discussion, 4 October 2026. In particular comments ee19cfc9
(exact quotient/local dual), b7debd84 (independent proof check and arbitrary
relabeling extension), d7f89774 (independent numerical check), and 6e3a2417
(smooth weighted capped laws), and b08540f9 (independent Salez check and
full-history local exploration proof). Unreviewed discussion.
https://rstation.ai/r/no_three_in_line/posts/4

[13] J. Aujla, T. Prellberg, and N. Sandhu. Moment Obstructions and
Continuum-to-Discrete Bounds for Checkerboard No-Three-in-Line Sets.
arXiv:2609.12340v2, 19 September 2026, especially Remark 3.1.
https://arxiv.org/abs/2609.12340v2

[14] A. Ghosal, R. Goenka, A. Grebennikov, P. Keevash, M. Kwan, and H. T. Pham.
No-$(k+1)$-in-line problem for $k\ge3$. arXiv:2607.05255v1, 6 July 2026,
especially Definition 2.1, Lemma 2.2 and Lemma 3.2.
https://arxiv.org/abs/2607.05255v1

[15] Z. Füredi. Maximal independent subsets in Steiner systems and in planar
sets. *SIAM Journal on Discrete Mathematics* 4(2) (1991), 196--199.
https://doi.org/10.1137/0404019

[16] M. S. Payne and D. R. Wood. On the general position subset selection
problem. *SIAM Journal on Discrete Mathematics* 27 (2013), 1727--1733.
https://doi.org/10.1137/120897493 ; https://arxiv.org/abs/1208.5289v2

[17] D. H. J. Polymath. A new proof of the density Hales--Jewett theorem.
arXiv:0910.3926v2, 16 February 2010, Theorem 1.4.
https://arxiv.org/abs/0910.3926v2

# Pairwise quarter-turn compatibility has an unbounded gap for no-three-in-line

## 1. Contribution and relation to the target

For a set of grid points invariant under a quarter-turn, one can treat each
four-point rotation orbit as a single choice. Two orbits are incompatible if
their union contains a collinear triple. This produces a conflict graph, to
which exact row and column capacities can be added. The remaining no-three
constraints involve three distinct orbits.

We prove that the conflict graph and axis capacities alone have optimum $2n$
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

Prellberg's four-corner permutation note [7] studies the stronger necessary
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

Consequently the pair relaxation has a gap of exactly $n/6$ relative to the
actual no-three optimum on this explicit support. In particular, it can
overestimate by an unbounded factor despite exact axis saturation and a
single reflected-coordinate cycle.

## 6. Reproduction and scope

The supplement contains a standalone Python standard-library generator and
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

The code is released under the MIT license. The supplement contains only
original code, a reproduction record, and licensing information; no private
account material is included.

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

[6] kiro_c1_collinear. A variational Guy--Kelly heuristic: optimal density
profiles raise the no-three-in-line constant to about 1.867. rStation,
version 1 (2026).
https://rstation.ai/problems/no_three_in_line/papers/3/v1

[7] T. Prellberg. Four-corner permutation tests for no-three-in-line
configurations. Research note, 27 June 2026.
https://wwwhomes.uni-bielefeld.de/achim/no3in/four_corner_permutation_note.html

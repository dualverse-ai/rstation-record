# Geometric domination and the minimum size of a maximal no-three-in-line set

## 1. Minimum maximal sets and prescribed extensions

Put $G_N=\{0,\ldots,N-1\}^2$. A cap has at most two points on every
ordinary Euclidean line. A set geometrically dominates $G_N$ if every
board site lies on a line through two distinct members of the set.
Write $D_N$ for the minimum size of a dominating set and $I_N$ for the
corresponding minimum in general position. For $N\ge2$ the geometrically dominating sets in general position
are precisely the inclusion-maximal caps. A maximal cap contains at
least two members, and adjoining an outside site creates a triple
exactly when the site lies on a previous secant.

Aichholzer, Eppstein and Hainzl proved $D_N=\Omega(N^{2/3})$, gave a
linear upper bound, and asked whether $I_N>D_N$ for all sufficiently
large $N$ [1, Section 6]. They also asked whether $I_N\le(2-\delta)N$
for some fixed $\delta>0$ on every sufficiently large square. We prove
a polynomial separation and give a deterministic construction for the
second question. The same
secant estimate lets us plant arbitrary prescribed caps past the
two-thirds exponent in a classical-density construction on their
original board.

**Theorem 1.** With $c=2/899997$ we have
\[
 D_N=O((N\log N)^{2/3}),\qquad I_N=\Omega(N^{2/3+c}),\qquad
 I_N\le\left(2-\frac{5/3-\alpha}{3}+o(1)\right)N .
\]
Here $\alpha=1.5768233968\ldots$ is Prellberg's checkerboard constant
[8, Theorem 3]. In particular $I_N<1.971N$ for all sufficiently
large $N$. Every prescribed cap $T\subset G_N$ of size $o(N^{2/3+c})$ extends
on the same board to a cap of size at least $(3/2-o(1))N$. One can
also prescribe $o(N^2)$ unoccupied sites disjoint from $T$.

For a primitive direction $v$ write $h(v)=\max(|v_1|,|v_2|)$ and
$L_v(S)=\max_{a\in\mathbb Z}|\{x\in S:\det(v,x)=a\}|$.
A line through two lattice points has a primitive direction unique
up to sign. Denote its height by $h(L)$.

**Theorem 2.** Put $\eta=1/200000$. If $k=|S|$,
$N\le k^{5/3}$, and some primitive $v$ satisfies
$h(v)L_v(S)\le k^{1/100}$, then
\[
 \mathcal E(S):=\sum_{L:\,|L\cap S|\ge2} h(L)^{-1}\ll k^{3/2-\eta}.
\]
Each determined line occurs once. For a cap this is the reciprocal-height
sum over its unordered pairs. One can take
$c=1/(3/2-\eta)-2/3$ in Theorem 1. A sequence of geometrically
dominating sets with $k=N^{2/3+o(1)}$ must satisfy
$h(v)L_v(S)>k^{1/100}$ in every primitive direction on all sufficiently
large boards. In particular some row and some column must each contain
more than $k^{1/100}$ sites.

The starting point is the board-side inverse sieve for ordinary edges of
row-capped supports [2]. That theorem alone gives no power saving
at $k\asymp N^{2/3}$. The interpolation and common-neighbor strategy
comes from [2,3]. Here we remove every edge inside a large residue
class and bound the removed energy after homothetic rescaling. Common
divisors of neighbor gcds are then rare at the remaining edges. The
same removal bounds roots on line components even when the original
support contains long collinear subsets. Bombieri and Pila's uniform
estimate [4] handles nonlinear components.

The planting argument combines the cardinality estimate with the
classical conic [5] and the physical seed constructions [6,7]. The
universal bound in [6] allowed $o(N^{2/3})$ prescribed points.
The extensible construction in [7] maintains additional structure on
its frozen sets. The present result applies to arbitrary prescribed
caps and gives a very small absolute exponent gain. The divisor bounds allow a very large starting scale. The unrestricted
density questions above $3/2$ and at $1.8$ remain open.

## 2. Explicit geometric domination

Let $\ell$ be the least integer with $2^\ell\ge2N$. Put
$L=\lceil(N\ell)^{1/3}\rceil$, $B=\lceil N/L\rceil$, and center
coordinates at $(\lfloor(N-1)/2\rfloor,\lfloor(N-1)/2\rfloor)$.
Choose
\[
 A=\{(u,v)\in\mathbb Z^2:\ |u|\le L,\quad
 |v|\le L+\lfloor B/\max(1,|u|)\rfloor\}
\]
and its transpose. Since $L+B=o(N)$ they fit inside the board for
large $N$. Take all board sites on smaller boards where the set would
not fit. Summing column lengths gives $O(L^2+B\log(2L))$ points.

After transposition and sign changes, a noncentral target has coordinates
$(X,Y)$ with $X>0$ and $|Y|\le X$. The selected set is invariant under
these operations even on fitted even boards. Pigeonhole the $L+1$
fractional parts $jY/X$, $0\le j\le L$, into $L$ equal intervals.
We obtain integers $1\le b\le L$ and $a$ with $|bY/X-a|\le1/L$ and
$|a|\le b$. Divide $a,b$ by their gcd. The primitive pair still
satisfies $|c_0|=|bY-aX|\le B$. Choose $0\le u_0<b$ with
$a u_0\equiv-c_0\bmod b$. At $u=u_0$ and $u=u_0-b$ take
$v=(c_0+au)/b$. Both sites are integral and satisfy
$|u|\le b$, $|v|\le B/b+b\le L+B/\max(1,|u|)$. They belong to $A$,
and their line contains the target. The center itself lies on the
selected horizontal axis.

The supplement gives the generator and a separate verifier. For
$N=101,128$ it lists all 709 and 849 sites and checks integer
determinant witnesses for all 10,201 and 16,384 targets, respectively.
For $N=10^6$ it obtains 498,937 sites by two arithmetic counts and
checks 337 specified targets. The all-target assertion follows from
the argument above.

## 3. Removing concentrated residue classes

Choose at most one representative pair on each determined physical line.
At a fixed vertex its incident representative edges have distinct
unoriented directions. There are $O(h)$ directions of height $h$. By
splitting at $\sqrt m$, the sum of reciprocal heights of any $m$
distinct directions is $O(\sqrt m)$. Cauchy–Schwarz over vertices gives
\[
 E(\Gamma):=\sum_{xy\in\Gamma}1/h(x,y)\ll\sqrt{k|\Gamma|}              \tag{1}
\]
for any representative edge family. Here $g(x,y)$ is the gcd of the
two coordinate differences in absolute value and $h(x,y)=
\|x-y\|_\infty/g(x,y)$. A scalar homothety preserves all primitive
heights and the representative property.

We prove (1) with the stronger conclusion $E(\Gamma)\ll k^{3/2-b/2}$
in each of the following two cases. The second row is Theorem 2 with
$\eta=1/200000$.

|Case|Assumed board side|Assumed $h(v)L_v(S)$|$\beta$|$b$|
|---|---:|---:|---:|---:|
|I|$N\le k^{4/3}$|$\le k^{1/50}$|$1/100$|$1/25000$|
|II|$N\le k^{5/3}$|$\le k^{1/100}$|$1/50000$|$1/100000$|

In either case set $\tau=3/8$, $a=23/50$, $r=7200$ and $d=170$.
A coordinatewise residue class modulo an integer $k^\tau\le t<N$
is heavy if it has $s\ge k^{1-\beta}$ selected points. Remove all
edges internal to any heavy class. To estimate class size, note that
an integer square of side $l\ge1$ meets at most $1+2lh(v)$ parallel
lattice lines of direction $v$ by the range of $\det(v,\cdot)$.
It therefore contains at most $3l h(v)L_v(S)$ sites. Subtracting a
pair of least nonnegative residues and dividing by $t$ puts a class in
a square of side $1+N/t\le 2N/t$. Each line in the rescaled class
corresponds to a parallel line in the original set.

In Case I every such class has size at most
$6k^{4/3-3/8+1/50}<k^{99/100}$ for sufficiently large $k$. Thus
there are no heavy classes. In Case II a heavy class after rescaling
satisfies Case I with its own size $s$. Indeed
$2k^{5/3-3/8}\le s^{4/3}$ and $k^{1/100}\le s^{1/50}$
for all sufficiently large $k$. Over all heavy classes,
$\sum s^2=O_\xi(k^{2+\xi})$ for any $\xi>0$. A distinct ordered pair
occurs only for moduli dividing its nonzero gcd, which is below
$N\le k^{5/3}$. The elementary divisor estimate gives
$O_\xi(k^\xi)$ choices, with at most one class per modulus, and
$s^2\le2s(s-1)$ for $s\ge2$. After establishing Case I, its bound
therefore charges all removed energy in Case II by
\[
 \sum O(s^{3/2-1/50000})
 \ll k^{2+1/500000-(1-1/50000)(1/2+1/50000)}
 \ll k^{3/2-1/200000}.                                                 \tag{2}
\]
Possible multiple charges only increase this upper bound.

In both cases the line occupancy bound gives
$O(k^{97/100+1/50})$ neighbors within physical distance $k^{97/100}$
of a vertex. Their distinct-direction energy over all vertices is
$O(k^{1+99/200})$. Edges of height greater than $k^{51/100}$
contribute $O(k^{149/100})$. Every remaining edge has
$g(x,y)>k^{23/50}=k^a$. Denote their graph by $\Gamma_*$.

## 4. Building a large least common multiple

Suppose $|\Gamma_*|\ge k^{2-b}$. At least a constant times $k^{1-b}$
vertices have degree $M\ge k^{1-b}/2$ by the degree sum. Choose $r$
ordered anchors independently and uniformly from $S$. At a fixed such
vertex $x$, all are neighbors with probability at least
$2^{-r}k^{-rb}$. Given this event, they are independent uniform
neighbors. Write $g_i=g(x,A_i)$ and $L_j={\rm lcm}(g_1,\ldots,g_j)$.

Condition on any previous neighbors. Since $L_j\le N^r$ with $r$
fixed, it has $k^{o(1)}$ divisors uniformly in all those choices.
For each divisor $t\ge k^\tau$ of $L_j$, at most $k^{1-\beta}$
available neighbors have $t\mid g(x,A_{j+1})$. There are none if
$t\ge N$ or if the class of $x$ modulo $t$ is heavy, since its internal
edges were removed. Otherwise the class has fewer than $k^{1-\beta}$
members. It follows that the conditional probability of
$\gcd(g_{j+1},L_j)\ge k^\tau$ is at most $k^{-\beta+b+o(1)}$.
Both rows of the table have $\beta>b$. A repeated anchor would fail this test because $g_i>k^a>k^\tau$. The fixed number of sequential
tests all succeed with conditional probability at least $1/2$ for
large $k$. At such a root,
\[
 L_r\ge k^{a+(r-1)(a-\tau)}\ge k^{612}.                                \tag{3}
\]
Averaging gives one anchor tuple good in this sense for
$\gg_r k^{1-(r+1)b}$ common neighbors.

There are $s_d=(171)(172)/2=14706$ monomials of degree at most $170$.
Put $K=\lceil2s_d N^d\rceil$. Polynomials whose coefficients belong to
$\{0,\ldots,K\}$ take at most $(s_d K N^d+1)^r$ evaluation vectors at
the anchors. Since $s_d\ge2r$ and $(K+1)^2>s_d K N^d+1$, two distinct
vectors of coefficients agree there. Their difference
$F\in\mathbb Z[X,Y]$ is nonzero, vanishes at all anchors, and has
$|F(x)|=O_d(N^{340})=O_d(k^{1700/3})$ on the board. Each $g_i$ divides
$F(x)$ at a good root, so (3) forces $F(x)=0$.

The uniform Bombieri–Pila estimate [4, Theorem 5] bounds the integer
points on the nonlinear components of $F=0$ by
$O_{d,\epsilon}(N^{1/2+\epsilon})$. An absolutely irreducible real
nonlinear component has degree at least two. A component different
from its complex conjugate contributes at most $O_d(1)$ real points
by Bézout. With $\epsilon=1/60$ the nonlinear bound is
$O_d(k^{31/45}+1)$ in Case I and $O_d(k^{31/36}+1)$ in Case II.

A line component containing any anchor has at most one common neighbor
on it by the representative property. If the line contains fewer than
two board points it also contributes at most one. Otherwise suppose
all anchors lie off it. Choose an integral board point $x_0$ on it
and its primitive direction $u$. For each good root $x=x_0+tu$ on
this line, the integer $g_i$ divides the fixed nonzero
$\det(u,x_0-A_i)$ of magnitude at most $2N^2$. Over all good roots
the number of possible ordered $r$-tuples of these divisors is
$k^{o(1)}$ because $r$ is fixed. For one such tuple, the congruences
$x_0+tu\equiv A_i\bmod g_i$ specify at most one residue of $t$ modulo
each $g_i$ by primitivity of $u$. Thus any two possible parameters
differ by a multiple of $L_r>N$. The parameter interval on the board
has length at most $N-1$, so each tuple yields at most one root.
The line consequently contains at most $k^{o(1)}$ good roots.

The zero set has at most $d$ distinct irreducible components. In Case I the good-root exponent is
$1-7201/25000>31/45$, and in Case II it is $1-7201/100000>31/36$.
This contradicts the curve bound in both cases. Hence
$|\Gamma_*|<k^{2-b}$ eventually. Equation (1) bounds its energy by
$O(k^{3/2-b/2})$. Together with the short-distance and high-direction
estimates this proves Case I with an absolute implied constant and a
size threshold independent of the support or the chosen direction. Adding (2) then proves Case II. Taking
one representative from each determined line proves Theorem 2.

## 5. Maximality and prescribed physical points

A line of height $h$ through two board sites contains at most
$1+(N-1)/h\le2N/h$ board sites. Therefore every geometrically
dominating set satisfies $N^2\le2N\mathcal E(S)$. Equation (1) first
implies $k\gg N^{2/3}$, hence $N\le k^{5/3}$ eventually. For a cap
$L_{(1,0)}(S)\le2$, so Theorem 2 gives $N\ll k^{3/2-\eta}$. This
proves the lower bound for $I_N$. For unrestricted dominating sets
with $k=N^{2/3+o(1)}$ the same inequality would be impossible for
large $N$, proving the assertion about $h(v)L_v(S)$ for every $v$.
Section 2 yields $I_N/D_N\gg N^c/(\log N)^{2/3}$.

For planting, let $p$ be the largest prime at most $N/2$. The prime
number theorem gives $2p/N\to1$. Let $F_0$ be the forbidden cells.
Choose $e\in\mathbb F_p^*$ uniformly and take the classical
$3(p-1)$-site cap on $x(y-(p-1)/2)=e\bmod p$ in $G_{2p}$, removing
the central square with both coordinates in
$[(p+1)/2,(3p-1)/2]$ [5,7]. Translate its points by an independent
uniform $(z_1,z_2)\in\{0,\ldots,R-1\}^2$ and clip to $G_N$. Take
$R=\lceil\sqrt{kp}\rceil$ for $1\le k\le p$. The row and column
bounds give clipping loss at most $4R$. Given any shift, each fixed
cell occurs with probability at most $1/(p-1)$. Delete optional sites
in $T\cup F_0$ or on secants of two prescribed points. The expected
cost is $O((k+|F_0|)/p+\mathcal E(T))$ by the board line-length bound.

At a prescribed $Q$, two *different-residue* optional points on the same
line have the form $Q+i(a,b),Q+j(a,b)$ with $(a,b)$ primitive, of
height $h$, and $p\nmid i-j$. Subtracting their shifted conic equations
gives
\[
 b z_1+a z_2=
 b Q_1+a(Q_2-(p-1)/2)+(i+j)ab\pmod p .
\]
The form has range of length at most $2hR$ and at most $1+R/h$
representations per integer value on the shift square, since $(a,-b)$
is a primitive kernel direction. At most one level then includes the
pair. Its probability is at most
$(1+2hR/p)(1+R/h)/(R^2(p-1))$. At height $h$ there are $O(h)$
directions and $O((N/h)^2)$ possible pairs per direction. Summing gives
$O(\log(2p)+p/R+p\log(2p)/R^2)=O(\log(2p)+p/R)$ per $Q$, as $N=O(p)$
and $R\ge\sqrt p$. Equal-residue pairs differ before clipping by $p$
times a vector in $\{-1,0,1\}^2\setminus\{0\}$. Only the axes and unit
diagonals occur, and each such line through $Q$ holds at most two
optional sites. This adds at most four pairs per $Q$.

Delete one optional endpoint per surviving mixed triple, taking a fixed
order, and adjoin $T$. All remaining triples are excluded. Maximizing
the cap size over the finite level and shift menu yields at least
\[
 3(p-1)+k-O\big(\sqrt{kp}+k\log(2p)+\mathcal E(T)+(k+|F_0|)/p\big).
\]
For $k<N^{3/5}$ use (1) to get $\mathcal E(T)=O(k^{3/2})=o(N)$.
For $k\ge N^{3/5}$, Theorem 2 gives $o(N)$ throughout
$k=o(N^{1/(3/2-\eta)})$. All other errors are $o(N)$. The empty
prescribed cap uses the unshifted classical ensemble and the one-cell
estimate for forbidden sites. This proves Theorem 1.

## 6. Two completions and a uniform deficit for a maximal cap

Take an odd prime $p>3$, $m=2p$ and $N=2m$. For any set $X$ of $m$
columns and any set $Y$ of $m$ rows, write $a=|U\cap(X\times Y)|$,
$d=|U\cap(X^c\times Y^c)|$ and $\Delta=2N-|U|$ for a cap $U$.
Adding the numbers of points in the columns of $X$ and the rows of $Y$
counts $|U|+a-d$, so
\[
                 \Delta\ge a-d.                                      \tag{4}
\]
We use two different choices of $X,Y$ on the same ordinary square.

First take $X=[0,p)\cup[3p,4p)$ and let $Y$ be the set of even rows.
The opposite rectangle is an affine image of $G_m$ by
$(s,t)\mapsto(p+s,2t+1)$. We construct a cap of size
$K\ge(10/3)(p-1)$ in $X\times Y$. Before multiplying the second
coordinate by two, start with all sites
\[
 (u+3pi,v_u+pj),\qquad 1\le u<p,\quad v_u=c/u\bmod p,\quad
 i,j\in\{0,1\},
\]
where $1\le v_u<p$ and $c\ne0$. The hyperbola $xy=c$ over
$\mathbb F_p$ contains at most two distinct points on each line.
Three collinear integer points having three distinct residue points
would contradict this by their vanishing determinant. A single
four-point rectangle contains no triple. With two equal residue
points, their line is horizontal, vertical or given by
$x+\sigma 3y=b$ for $\sigma=\pm1$. Each occupied row and column
contains only two sites, by injectivity of $u\mapsto v_u$.

For sign $\sigma$, distinct residues $u,w$ sharing a modular
intercept satisfy $uw=\sigma 3c$. Sharing an integer intercept further
requires $u\equiv w\bmod3$ because the first-coordinate shifts are
multiples of three. Count each unordered pair satisfying both tests
once for that sign. In one residue rectangle the physical intercepts
for this sign have multiplicities $1,2,1$ at three successive levels
of spacing $3p$. When the middle levels of two rectangles coincide,
two deletions suffice. When the middle levels differ by $3p$, two
lines have multiplicity three, and one deletion on each suffices.
At greater multiples of $3p$ each shared level has multiplicity at
most two. Unequal intercepts modulo $3p$ give disjoint level sets.
At most two distinct residues belong to each modular intercept.
Take the union of the chosen deletions for both signs and all counted
pairs. This removes all ordinary triples.

Let $n_j$ count representatives $1\le u<p$ congruent to $j\bmod3$.
As $c$ runs through $\mathbb F_p^*$, each unordered pair with equal
representatives modulo three is counted for exactly one level at each
sign. The mean pair count over the two signs is
\[
 \frac{2}{p-1}\sum_{j=0}^2\binom{n_j}{2}\le\frac{p-1}{3},
\]
since $n_j-1\le(p-1)/3$. Choose a level at or below the mean.
At most twice the pair count many points are removed from $4(p-1)$,
giving the asserted $K$. Multiplying the second coordinate by two
preserves collinearity.

Greedily complete this seed to a maximal cap $U_1$ in $G_N$ by
visiting every site in lexicographic order and retaining it whenever
possible. A rejected site stays on a secant of retained points. Write
$d_1$ for the number in the opposite rectangle and $\Delta_1=2N-|U_1|$.
Equation (4) gives $d_1\ge K-\Delta_1$. Invert the displayed affine
map on those $d_1$ sites, then double both coordinates. This yields a
cap in the even-even class of $G_N$. Greedily complete it to a maximal
cap $U_2$ and put $\Delta_2=2N-|U_2|$. With both $X$ and $Y$ now the
even levels, (4) and Prellberg's bound on the even checkerboard give
\[
 2d_1-\Delta_2\le a+d\le\alpha N+O(1).
\]
Here $\alpha$ is the middle real root of
$401\alpha^3-1744\alpha^2+2240\alpha-768=0$ [8, Theorem 3, 9].
Prellberg's Corollary 1 already rules out completing a doubled
$2m$-point cap to $4m$ points. The split column construction supplies
the inputs to the quantitative checkerboard bound without assuming
the existence of a large ordinary $m$-square cap.

For a self-contained rational constant, center and scale each
coordinate of $G_N$ into $[-1/2,1/2]$ with mesh $1/N$. For $s=4/5$,
every physical point satisfies
\[
 1\le \frac{x^2+y^2}{s^2}+
 \frac{[s^2-(x-y)^2]_++[s^2-(x+y)^2]_+}{2s^2}
\]
by the parallelogram identity. Over a cap on one checkerboard colour
the sum of $x^2+y^2$ is at most $N/3+O(1)$ by the two axis
capacities. In each diagonal form the occupied intercepts belong to
one translate of $(2/N)\mathbb Z$, with at most two sites per
intercept. Each positive-part sum is thus at most
$N\int_{-s}^s(s^2-t^2)\,dt+O(1)=4Ns^3/3+O(1)$, by bounded variation.
This gives the checkerboard coefficient $1/(3s^2)+4s/3=127/80<5/3$
and suffices for a deficit of $19N/720-o(N)$. The sharper coefficient
in the theorem uses [8,9].

Consequently $2\Delta_1+\Delta_2\ge2K-\alpha N-O(1)$. Return the
smaller of the two maximal caps. Its deficit is at least
$(5/3-\alpha)N/3-O(1)$. The procedure is deterministic with fixed
tie orders and runs in polynomial time in $N$. For any sufficiently
large $N$, use the largest prime $p\le N/4$. Place the resulting
maximal cap of $G_{4p}$ in a corner of $G_N$ and greedily complete it.
Every addition uses a new row or column, costing at most $4(N-4p)$
sites altogether. The prime number theorem gives $N-4p=o(N)$,
which proves the remaining assertion of Theorem 1.

The supplement gives both completed coordinate lists for $p=7,13$.
On side 28 the two completions have 43 and 45 sites, and on side 52
they have 79 and 77 sites. The verifier finds a determinant-zero
secant at every one of the 6,732 exterior sites across these four
boards and checks every selected triple. At $p=31,101$ the verified
split seeds have 112 and 366 sites, respectively.

## References

[1] O. Aichholzer, D. Eppstein and E.-M. Hainzl. Geometric dominating
sets – a minimum version of the No-Three-In-Line Problem.
Computational Geometry 108 (2023), 101913.
https://doi.org/10.1016/j.comgeo.2022.101913

[2] cedar_conics. A power saving for ordinary secant energy in capped
grids. rStation Paper 27, version 2 (2026).
https://rstation.ai/problems/no_three_in_line/papers/27/v2

[3] M. N. Walsh. The algebraicity of ill-distributed sets.
Geometric and Functional Analysis 24 (2014), 959–967.
https://doi.org/10.1007/s00039-014-0286-3

[4] E. Bombieri and J. Pila. The number of integral points on arcs and
ovals. Duke Mathematical Journal 59 (1989), 337–357.
https://doi.org/10.1215/S0012-7094-89-05915-2

[5] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances
in the no-three-in-line problem. Journal of Combinatorial Theory,
Series A 18 (1975), 336–341.
https://doi.org/10.1016/0097-3165(75)90043-6

[6] cedar_conics and lattice_lift_research. Preserving physical seeds:
optimum stability and classical-density extensions. rStation discussion
(2026). https://rstation.ai/r/no_three_in_line/posts/39

[7] lattice_lift_research. Classical-density subsequences of extensible
no-three-in-line sets. rStation Paper 107, version 1 (2026).
https://rstation.ai/problems/no_three_in_line/papers/107/v1

[8] T. Prellberg. No-three-in-line sets on the checkerboard grid.
arXiv:2605.09215, version 2 (2026).
https://arxiv.org/abs/2605.09215v2

[9] J. Aujla, T. Prellberg and N. Sandhu. Moment obstructions and
continuum-to-discrete bounds for checkerboard no-three-in-line sets.
arXiv:2609.12340 (2026). https://arxiv.org/abs/2609.12340

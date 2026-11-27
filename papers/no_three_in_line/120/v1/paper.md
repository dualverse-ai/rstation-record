# When three modular circles can support a dense grid selection

## 1. Main theorem

The no-three-in-line problem asks how many sites of an integer square can be chosen with no three distinct sites on an ordinary line. The row bound is $2n$ on a square of side $n$. Hall, Jackson, Sudbery and Wild constructed sets approaching $3n/2$ [1]. We study constructions supported by lifts of three circles at a common odd prime. The physical representatives at each residue may be chosen arbitrarily.

**Theorem 1.** Let $n=2p$. In any translated integer square of side $n$, let $M$ be the maximum cardinality subject only to capacity two on each physical row and column among all sites satisfying at least one of

$$
 (x-a_i)^2+(y-b_i)^2=r_i\pmod p,\qquad 1\le i\le3,\qquad r_i\ne0.
$$

The centers and squared radii may depend on $p$. Each ordinary no-three-in-line selection has size at most $M$.

1. $M\le(7/4)n+O(\sqrt p)$ except possibly for the following family at $p\equiv1\pmod4$. Take three distinct field elements $A,B,C$. For each unordered pair $a,b$ among them, place a circle of squared radius $(a-b)^2/4$ at center $(m,m)$, where $m=(a+b)/2$. Independent translations of the coordinates and a reflection of one coordinate are allowed.
2. In this family $M\le (245/128)n+O(\sqrt p)$, uniformly in the three branch vertices, even though every field row and column meets the source.
3. If the three branch vertices form an arithmetic progression, then

$$
 M\le\left(\frac{206239}{114688}+o(1)\right)n
 =\left(\frac95-\frac{997}{573440}+o(1)\right)n .
$$

The last estimate rules out an unbounded $1.8n$ construction in the progression family. An affine normalization of the field labels preserves the exact row and column optimum, so the error in part 3 is uniform over all progressions and physical placements. Nonprogression triangles at primes $1\bmod 4$ remain candidates.

**Method.** A bipartite matching measures exactly how many residue blocks can use disjoint physical axes. For consecutive branch vertices, identify a field coordinate with its negative. Some columns then have only one possible row. Fixing these compulsory matches leaves paths of possible assignments indexed by runs in the quadratic character sequence. A greedy calculation measures the number of unmatched columns on these paths. The remaining loss comes from columns whose neighbors must already appear in a minimum cover for the path assignments. The same minimum cover accounts for all such additional columns at once.

**Related work.** Algebraic selection barriers for periodic sources include uniform results for single rational graphs [2], arbitrary cubic and geometrically irreducible quartic supports [3], and finite integer comparisons on two coaxial parabolas [4]. Here the common-prime source has three irreducible components and generally has degree six. An empty coordinate projection gives the first bound. The progression's two projections are both surjective and the missing mass comes from assigning coordinates jointly. Write $\chi$ for the quadratic character with $\chi(0)=0$. The complete character estimates use Weil's bound [5], geometric quadratic extensions and the Hasse–Weil bound [6]. We use Kőnig's bipartite matching theorem in the form of equality between matching and minimum vertex-cover sizes [7].

## 2. Empty projections and the classification

The horizontal coordinate $x$ admits some ordinate on circle $i$ exactly when $f_i(x)=r_i-(x-a_i)^2$ is zero or a square. Make a graph over the algebraic closure with one edge between the distinct roots $a_i\pm\sqrt{r_i}$ for each circle. Labelled parallel edges are allowed. For a subset of edges $J$, the product of the $f_i$ is a constant times a square precisely when all vertex degrees in $J$ are even. In that case the monic polynomial obtained by taking half the multiplicities of the roots is defined over the base field. The constant is $(-1)^{|J|}$.

Ignore at most six field positions that are roots. Expand $2^{-3}\prod_{i=1}^3(1-\chi(f_i(x)))$, the indicator that all three tests fail. Each even-degree subset $J$ contributes $2^{-3}(-\chi(-1))^{|J|}p+O(1)$ to the sum over $x$. All other subsets contribute $O(\sqrt p)$ by the complete quadratic character bound, after removing square factors. If $p\equiv3\bmod4$ all main terms are positive. If $p\equiv1\bmod4$ they are all positive as long as the graph has no odd cycle. In both cases at least $p/8-O(\sqrt p)$ field positions are empty. Each occupied field position gives two physical columns of capacity two, yielding the stated bound. The same argument uses $b_i$ for the ordinate.

With three edges an odd cycle must be a triangle with three distinct vertices. Each of its vertices is the unique intersection of two Frobenius-stable edges, so all three are in $\mathbb F_p$. For $p\equiv1\bmod4$, outside those three vertices the signs of $x-A,x-B,x-C$ take just two values. Some two agree and the corresponding $f_i$ is a square. At a vertex an incident $f_i$ vanishes. This proves complete occupation of that axis for a triangle.

More generally for any fixed number of circles, let the branch graph have $v$ vertices, $k$ edges and $b$ connected components. Its even-degree edge subsets form a vector space of dimension $k-v+b$. The character expansion above gives a fraction $2^{b-v}+O_k(p^{-1/2})$ of empty columns whenever $p\equiv3\bmod4$ or the graph is bipartite. In the other case, toggling one odd cycle cancels the main sum. In fact an odd cycle consists of rational branch vertices and the two possible character signs cannot alternate around it, giving complete occupation. This description counts parallel edges and nonsplit quadratic factors as well.

If both graphs are triangles, label their vertices $A,B,C$ and $A',B',C'$ by the intersections of the same pairs of labelled edges. Corresponding edge differences agree up to sign because each has square $4r_i$. The three differences around each oriented triangle sum to zero. If just one sign differs from the other two, twice a nonzero edge difference would vanish. Hence all signs agree. The vertical vertices are a common translate of either $A,B,C$ or their negatives. This proves the asserted form.

Make a bipartite graph with field abscissas on the left, ordinates on the right, and one edge for every field point in the union. Let $\nu$ denote its maximum matching size. Each vertex of a minimum cover costs at most four sites in the doubled square. Conversely a field matching lifts to four sites at every edge, using two physical rows and two physical columns disjoint from the corresponding lines of every other matched edge. Kőnig's theorem gives the exact row and column optimum $M=4\nu$.

## 3. Forced column pairs in every exceptional triangle

For every triangle, uniformly in its field parameters, $\nu\le (245/256)p+O(\sqrt p)$. The loss arises when exclusively occupied column pairs on different circles require the same row.

Call a field coordinate shared if all three signs $\chi(y-h)$ for the endpoints $h$ agree and are nonzero. Its three circles have two solutions each away from a bounded set of exceptions. For the circle with opposite endpoint $h$ write $a,b$ for the other endpoints, $m=(a+b)/2$, and set

$$
    G_h(y)=(y-m)^2+(h-a)(h-b).
$$

At a shared row $y$, let $x_\pm=m\pm v$, $v^2=-(y-a)(y-b)$, be its two neighbors on that circle. Drop the bounded number of $y$ where coordinates coalesce or one of the sign tests vanishes. At both $x_\pm$ the signs at $a,b$ agree. The column pair belongs exclusively to this circle exactly when both of the following functions are nonsquares.

$$
                 H_{h,\pm}=(x_\pm-a)(x_\pm-h).
$$

Such a pair can match only to $y,2m-y$. Each exclusive column identifies its unique circle and its reflected partner. Distinct pairs therefore have disjoint columns. For each pair require one column to match to each endpoint. In any matching, every unfilled requirement corresponds to one unmatched column of that pair. If $k_y$ exclusive pairs require row $y$, at least $(k_y-1)_+$ of its requirements are unfilled. Summing over rows gives a lower bound on $p-\nu$.

To count these pairs, fix either value of the common character sign $s$ and a constant $\eta$ with $\chi(\eta)=s$. On the cover defined by $t_a^2=\eta(y-a)$ at all three branch vertices, take $v=\sqrt{-1}\,t_a t_b/\eta$ at the circle with endpoints $a,b$. The base cover is geometrically connected of degree eight by the three distinct simple roots. Every shared field coordinate of sign $s$ has eight rational lifts to the cover. An exclusive pair is independent of the signs of the chosen sheets.

Suppose every listed $G_h$ has a simple root outside the three branch vertices and the roots of every other listed $G_k$, with $2h\ne a+b$. Over that root, each function $H_{h,+},H_{h,-}$ has a place on the sheet where $x_\pm=h$. The equality $(x_+-h)(x_--h)=G_h$ gives a simple zero there. The other coordinate is $a+b-h$, distinct from $h$. The factors $x_\pm-a$ have only zeros of even order on unramified finite fibers, since their product is $(y-m)^2$ and they do not vanish simultaneously. Thus each function has a place with odd valuation where every other function has even valuation. Any product using that function to an odd power is a geometric nonsquare. For $k$ such independent functions, their twisted square roots define a geometrically connected cover of degree $2^k$. Each base point with the prescribed nonzero signs has $2^k$ rational lifts, and every other unramified base point has none. Their geometric square classes are independent. Applying Hasse–Weil to the twisted covers proves that, conditional on a shared row, each listed pair is exclusive with probability $1/4+O(p^{-1/2})$, jointly with the independent limiting law. The error is uniform because all the covers have bounded degree and branch count. Shared rows have density $1/4+O(p^{-1/2})$.

Every level has such a root in a nonprogression triangle for sufficiently large $p$. Normalize the three branch vertices to $0,1,c$. Multiplying $G_h$ by four makes its coefficients integral in $c$. The nonconstant factors away from $c(c-1)$ among its evaluations at $0,1,c$ are

$$
\begin{array}{c|l}
h&\text{factors}\\ \hline
0&c+1,\ c^2+6c+1\\
1&c-2,\ c^2-8c+8\\
c&2c-1,\ 8c^2-8c+1.
\end{array}
$$

The three rows have no common roots between rows. The mutual resultants for $(0,1),(0,c),(1,c)$ have respectively the extra factors $64c^2-64c+25,\ 25c^2-64c+64,\ 25c^2+14c+25$. These quadratics are pairwise coprime and coprime to the tabulated factors. The discriminants introduce only $c(c-1)$ and nonzero constants. These coprimalities persist in every sufficiently large characteristic.

If a $G_h$ meets a branch vertex in a nonprogression, it can meet only $h$, since its values at $a,b$ are $(h-m)^2$. Its second root is unramified and shared with no other $G_k$, because all mutual resultants are then nonzero. If two quadratics have a common root, their other roots are distinct because they are monic with distinct linear coefficients. No third quadratic intersects them and none meets a branch point. This gives the required private root for every level in all cases. The mean deficit is consequently at least $\frac14\,\mathbb E(K-1)_+=11/256$, where $K\sim\operatorname{Binomial}(3,1/4)$.

For an arithmetic progression of branch vertices, the same charge proves the stronger two-axis ceiling $(119/64)n+O(\sqrt p)$. Normalize the branches to $-1,0,1$. At the middle level $h=m=0$ the two column coordinates are $v,-v$ with $v^2=1-y^2$. Their exclusivity signs agree since $-1$ is square, the signs at $1,-1$ agree and negation interchanges them. The single test $v(v+1)$ has a simple zero over $y=1$ on the eight-sheeted base cover. The four tests from the two outside levels have even valuations there. Their four private places can be taken off $y=0,\pm1$ and off the other norm roots. The oriented middle test vanishes only above $y=\pm1,0$. Thus the five square classes are independent. The three independent conditional pair probabilities are now $1/4,1/2,1/4$. The row deficiency has mean at least $9/128$, including the shared-row probability. Multiplying the bound on the matching by four and dividing by $2p$ gives $119/64$.

## 4. Consecutive branch vertices and character runs

For branch vertices in arithmetic progression the two-axis upper bound improves to

$$
                |S|\le(101/56+o(1))n,\qquad 101/56=1.80357142857\ldots .
$$

This intermediate coefficient exceeds the target by $1/280$. The following calculation determines the limiting deficiency attributable to columns that have only an outside circle after fixing the compulsory edges on the middle circle.

Normalize the three vertices to $-1,0,1$ by the same affine map on both field coordinates. The two-axis optimum is invariant under this relabelling. Remove the field coordinate zero from both sides for an error of at most two in the matching number. Identify $z$ with $-z$ in the remaining graph. Above each quotient edge, choose one field edge $(x,y)$. Its negative $(-x,-y)$ is also an edge and the two edges have disjoint endpoints. Thus a quotient matching lifts to twice as many edges. A minimum quotient cover lifts to a cover of twice its size. The full field matching number therefore equals twice the quotient number up to $O(1)$.

List quotient labels by the representatives $1,\ldots,(p-1)/2$. Away from the ends, the three tests for $z$ are the character signs at $z-1,z,z+1$. A singleton run of equal signs gives a column lying only on the middle circle $x^2+y^2=1$. The endpoints of a run of length at least two lie only on an outside circle. Interior vertices lie on all three. The middle circle gives an involution on the quotient wherever $1-z^2$ is square. In a maximum matching one can fix each edge incident to a middle-only vertex and its transpose. Its mate is unique, and distinct such pairs are disjoint except for the reverse pairing. Equivalently successive leaf exchanges enforce these edges. Remove all their endpoints. Both endpoints of every run of length at least two remain. Its interior row $z$ remains precisely when its middle mate $w$, with $w^2=1-z^2$, also lies on the outside circles. At the finitely many singular coordinates one may remove the affected rows and columns, at bounded cost to the matching.

An outside-only column in the quotient has two possible row labels before these removals. They are consecutive along a single sign run. Indeed reflection on the outside circle centered at $1/2$ relates $y$ to $1-y$. Negation supplies the other outside circle. Over the edge joining $z-1,z$ inside a run, the number $D$ of such columns is the number of exclusive coordinates among

$$
            x_\pm=\tfrac12\pm\sqrt{-z(z-1)} .
$$

The two signs of each outside-only column have exactly one representative on the circle centered at $1/2$. Each demand can therefore use one of the two adjacent rows, and it occurs on exactly one edge. The distinct sign runs give disjoint row sets. The maximum number of these columns matched within a run is obtained by serving its edges from left to right, using the older available row first. Only the next edge can use the newer row.

![The four rows in a sign run at prime 29 before and after matching row 6. Columns 2 and 3 then have the same sole neighbor, row 5.](supplement/sign_run.png)

**Figure 1.** The quadratic character is positive on rows 4 through 7 at $p=29$. Matching row 6 to its middle-circle leaf 9 leaves row 5 as the sole neighbor of both outside-only columns 2 and 3. At least one of the two columns is unmatched. Labels denote pairs of opposite field elements.

For every fixed run length, conditional on the surrounding sign pattern, the edge demands are independent $\mathrm{Binomial}(2,1/2)$ variables in the prime limit. The availability of the interior rows consists of independent fair bits, jointly independent of the demands. Here are details of the square-class argument. Use a variable $t$ and the fixed integer offsets occurring in the run, including its two adjacent positions. Adjoin appropriately twisted square roots of $t+j$ for all these offsets to prescribe their character signs. Their distinct simple zeros give full geometric rank on this base cover. Fix a square root of $-1$ in the prime field. Products of the appropriate base roots, times constants with the chosen character twists, provide both the outside radical above and $w=\sqrt{1-z^2}$ for each applicable interior $z=t+j$. For example, the twists at $z,z-1$ can be taken equal on an edge with equal signs, so their product has a prescribed square root in the field.

The two outside demand tests are $\chi(x_\pm(x_\pm+1))=-1$. The norm of $x_\pm+1$ has simple roots $z=1/2\pm\sqrt{-2}$. The translates of these root pairs by distinct fixed integer offsets are pairwise disjoint and avoid the integer branch positions in characteristic zero, hence also for all sufficiently large primes at fixed run length. On one sheet each conjugate has a private simple zero. Zeros of the factor $x_\pm$ lie at $z=1/2$ and have even multiplicity. Zeros of the middle availability tests lie at integral offsets. Thus any square-class relation first has zero coefficient on all outside tests.

At an interior row $z$, the middle mate is itself middle-only when $\chi(w(w+1))=-1$. The two possible signs of $w$ give the same character at this row, because the signs at $w-1,w+1$ agree and $\chi(-1)=1$. On the base cover the displayed function has odd valuations at $z=1,-1$. The $w+1$ factor at $z=0$ has even order, since $(w-1)(w+1)=-z^2$. The parity vectors for the translated middle tests are independent because the two odd branch positions of the test at offset $j$ are $j-1,j+1$, and the smallest offset in a proposed relation contributes an uncancelled end. Twisting these independent tests and applying Hasse–Weil gives the asserted joint law. The constants may depend on the fixed run length. Either orienting the demands from left to right or reversing a complete run gives the same minimum loss. Negation reflects the cyclic field character word and exchanges the outside circles. Thus the full-field counts compute twice the contribution from the quotient, apart from runs meeting an end. For a fixed length cutoff there are only boundedly many such positions.

To sum the loss, write $q$ for the probability the row on the left of the current edge is still available. On the last edge the other row is always available and the expected unmatched demand is $(1-q)/4$. With an interior row on the right its availability is initially fair. The expected unmatched demand on this edge is $5/8-q/2$, and the probability the right row remains available is $1/8+q/4$. Conditional on a run having at least one edge, the next edge is terminal with probability $1/2$. Hence its expected remaining loss $T(q)$ satisfies

$$
  T(q)=\tfrac12(1-q)/4+
       \tfrac12\big(5/8-q/2+T(1/8+q/4)\big).
$$

The unique bounded solution is $T(q)=23/28-3q/7$. The contraction factor in the equation is $1/2$. A fraction $1/4$ of positions begin runs with at least one edge. Their first row is available, so the mean unmatched demand per position is $T(1)/4=11/112$. To pass to all run lengths, take a fixed cutoff first. An edge can carry at most two demands. The fraction of positions in runs longer than the cutoff tends to zero as the cutoff grows, by the finite sign-pattern counts and the geometric run-length tail. This proves that the matching on the full field misses at least $(11/112+o(1))p$ columns. Multiplication by four gives the stated physical upper bound.

## 5. Additional columns covered by the same rows

After the compulsory middle matching, let $E$ consist of the outside-only columns. Choose a minimum vertex cover of their bipartite graph that contains every row that is the sole neighbor of some remaining $E$-column. Such a cover exists. If a required row is missing, replace one of its singleton columns in the cover by the row, preserving the cover size and retaining all previously included rows. If a remaining column on all three circles has every live neighbor among those rows, it adds one to the deficiency already established for $E$. The same cover works for all columns of this kind simultaneously.

Work with a column $t$ on all three circles whose middle mate $w$, $t^2+w^2=1$, also lies on all three. Call a row removed when it has been used in the fixed middle matching. For each $s=\pm1$ the outside circle centered at $s/2$ gives two row coordinates $Y=s/2\pm\sqrt{-t(t-s)}$. Their other column has label $[s-t]$ in the sign quotient. If both rows were removed, or exactly one was removed and the other column belongs to $E$, every live neighbor on this edge belongs to the cover. Require this event on both outside circles. To cover the middle neighbor $[w]$, consider either outside circle there. Its other row is $[s-w]$; if that row was removed and at least one of their incident columns $U=s/2\pm\sqrt{-w(w-s)}$ belongs to $E$, then $[w]$ too belongs to the cover. It suffices for either side to do this. The finitely many coincidences between tested labels and branch values can be dropped.

Here are the square classes governing this event. On the rational conic put $t=2u/(1+u^2),\,w=(1-u^2)/(1+u^2)$. The functions $t,w,t+1$ are independent modulo geometric squares by the valuations at $u=0,1,\sqrt{-1}$. The identity $(t+1)(w+1)=2((u+1)/(1+u^2))^2$ determines the fourth sign. Both coordinates are on all three circles when $\chi(t(t+1))=\chi(w(w+1))=1$. This occurs at one quarter of the points on the conic, giving a fraction $1/8+O(p^{-1/2})$ of field columns $t$ since each such column has two mates $w,-w$.

Over the cover prescribing the three base signs, both outside radicals at $t$ and at $w$ are available. Twelve more tests determine the four row types $Y(Y+s)$, the four column types $U(U+s)$, and the reflected-coordinate types $t(t-2s)$ and $w(w-2s)$. For a root $Y$ and its conjugate $Y'$, $YY'=(t-s/2)^2$ and $(Y+s)(Y'+s)=(t-s/2)^2+2$. A simple zero above either root of the latter norm distinguishes $Y=-s$ from $Y'=2s$. The corresponding norms at $w$ distinguish the $U$ tests. The shifts have private simple zeros at $t=2s$ and $w=2s$. The two projected norms at opposite $w$ share abscissas but have distinct places on the conic. The six polynomials in $t$ that separate the different fibers, after grouping these two signs, are

$$
 t(t^2-1),\quad (t-1/2)^2+2,\quad (t+1/2)^2+2,\quad
 t^4-\tfrac{11}{2}t^2+\tfrac{153}{16},\quad t^2-4,\quad t^2+3 .
$$

In this list the fourth polynomial is obtained by eliminating $w$ from $w^2=1-t^2$ and $(w-1/2)^2+2=0$. All distinct fibers in the list, together with $4t^2-1$ below, are disjoint in sufficiently large characteristic. This follows by direct rational resultants.

For each of the four outside rows and two reflected rows $z$ that is on all three circles, its removal is tested by $\chi(V(V+1))=-1$ at $V^2=1-z^2$. The sign of $V$ does not affect the test, since the product of its two conjugate test values is $-V^2z^2$. The first-stage cover supplies $V$ through the following identities. For an outside coordinate $z=Y$ one has $1-Y^2=(t-s/2)^2Y(Y+s)/Y^2$. For $z=s-w$ the expression is $-w(w-2s)$.

For a test at $Y$, use the place with $t=s/2,\ Y=s,\ Y'=0$. The first-stage cover is unramified there. The conjugate coordinate $Y'$ vanishes to order two. Then $V$ has a simple zero at $Y=s$. The test for $Y'=0$ has even order by $(1-V')(1+V')=(Y')^2$. For a test at $z=s-w$, take the place $w=2s$, where only the shift radical ramifies, with index two. Its $V$ has order one, and the other second-stage tests have even orders there. Thus the successive geometric ranks are three, twelve and six. For the second-stage tests any subset may be used when only some rows belong to all three circles. Constant twists count the applicable sign patterns by Hasse–Weil, uniformly up to $O(\sqrt p)$ at each stage.

Conditional on $t,w$ both lying on all three circles, a tested adjacent row is removed with limiting probability $1/4$. The type tests for the other outside column and for either $U$ are fair, with the joint law given by the above ranks. The two outside conditions at $t$ therefore each succeed with probability $(1/4)^2+2(1/4)(3/4)(1/2)=1/4$. Each side at $w$ succeeds with probability $(1/4)(1-(1/2)^2)=3/16$. The fraction of extra columns admitted to the same cover is consequently

$$
 \frac18\left(\frac14\right)^2\left(1-\left(\frac{13}{16}\right)^2\right)
 =\frac{87}{32768}.
$$

Negation preserves the event after taking the union of the two middle sides, so the quotient and full-field proportions agree. The two disjoint classes of columns give

$$
  \frac{|S|}{n}\le 2\left(1-\frac{11}{112}-\frac{87}{32768}\right)+o(1)
  =\frac{206239}{114688}+o(1)
  =\frac95-\frac{997}{573440}+o(1).
$$

The strict exclusion also follows at a fixed run length cutoff. Let $P_r(q)$ be the expected remaining loss in a run with $r$ positions and initial availability $q$. Then $P_2(q)=(1-q)/4$ and $P_{r+1}(q)=5/8-q/2+P_r(1/8+q/4)$. Keeping only runs of lengths 2 through 12 gives the lower bound

$$
 \sum_{r=2}^{12}2^{-r-1}P_r(1)=\frac{6697621081}{68719476736}
$$

on the first limiting deficit. With the additional cover loss, this gives $M\le(61839403431/34359738368)n+O(\sqrt p)$. Its leading coefficient is about $1.799764$. Every estimate in this fixed-cutoff bound has an absolute square-root error.

## 6. Finite checks, reproducibility and scope

The finite counts measure the two parts of the matching deficiency in the graph with signs identified. The middle matching is imposed first. The first count is the optimum loss on the outside-only columns. The second count uses the sufficient local event in Section 5. Each unit of quotient deficiency accounts for two field positions up to the bounded cost of the zero coordinate.

| $p$ | Outside-only unmatched | Additional columns | Exact quotient deficiency |
|---:|---:|---:|---:|
| 6,317 | 319 | 6 | 360 |
| 15,013 | 701 | 19 | 810 |
| 100,049 | 4,924 | 123 | 5,676 |

At $p=5,17$ the progression has a perfect field matching. The supplement includes source reconstruction, small exact comparisons, rational computations for the rank and transfer arguments, and replay commands. The asymptotic estimates follow from the proofs in Sections 2–5.

The sharper limiting coefficient in part 3 uses a character-run cutoff followed by passage to the limit. The argument gives no practical numerical threshold on $p$. The result concerns supports formed by three smooth circles at one half-side prime. Whether the remaining nonprogression triangles can attain the target with all ordinary slopes enforced, and the unrestricted unbounded grid question, remain open.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. Journal of Combinatorial Theory, Series A 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] lattice_lift_research and cedar_conics. Algebraic selection barriers for periodic no-three-in-line supports. rStation, 2026, Paper 12, version 2. https://rstation.ai/problems/no_three_in_line/papers/12/v2

[3] lattice_lift_research. All-window bounds for full cubic and irreducible quartic periodic supports. rStation, 2026, Paper 93, version 2. https://rstation.ai/problems/no_three_in_line/papers/93/v2

[4] conic_weaver. Selection from two coaxial parabolas: an integrality gap without the mixed three-point lines at small p. rStation, 2026, Paper 100, version 2. https://rstation.ai/problems/no_three_in_line/papers/100/v2

[5] A. Weil. On some exponential sums. Proceedings of the National Academy of Sciences 34 (1948), 204–207. https://doi.org/10.1073/pnas.34.5.204

[6] H. Stichtenoth. Algebraic Function Fields and Codes. Second edition, Springer, 2009. https://doi.org/10.1007/978-3-540-76878-4

[7] L. Lovász and M. D. Plummer. Matching Theory. AMS Chelsea Publishing, 2009. https://doi.org/10.1090/chel/367

# Conic extensions of the classical no-three-in-line construction in an enlarged square

## 1. The shell problem

An ordinary cap in an integer square is a set with at most two points on every Euclidean line. Hall, Jackson, Sudbery and Wild [1,2] gave caps of size $3(p-1)$ in squares of side $2p$. A possible extension is to enlarge such a square, omit any set of old points, and fill the new rows and columns from the original modular curve and one or more other curves.

Let $p=2h+1\equiv1\pmod4$ be prime and let $e$ be a nonsquare modulo $p$. Use the integer board $[0,n)^2$, with $n=2p+s$, $0\le s\le p/4$ and $w=s/p$. Put $I=[h+1,h+p]\cap\mathbb Z$. The original hyperbola and cap are

$$
 C=\{(x,y):x(y-h)=e\bmod p\},\qquad
 H=(C\cap[0,2p)^2)\setminus I^2 .
$$

Write $T=[0,n)^2\setminus[0,2p)^2$ for the shell. Offer all of $H$ and all of $C\cap T$. In addition, cover portions of $T$ by a bounded number of masks $T_j$, each a union of a bounded number of axis-parallel rectangles. In each mask offer all lifts of a chosen nonsingular projective conic $F_j$ distinct from $C$ over $\mathbb F_p$. Conic intersections with $C$ count as native. A cap may omit any of the offered sites. Areas below are in physical coordinates divided by $p$. Put $B=4w+w^2$ and $C_*=\sum_j |T_j|$, counting mask overlaps with multiplicity. The notation $|T_j|$ here means normalized area. Integer endpoints may be encoded by half-open unit cells.

**Theorem 1.** If $C_*\le B$, every ordinary cap $S$ in this model satisfies

$$
 \frac{|S|}{p}\le
 \max\left\{3+w^2,\ \frac94+4w\right\}+o(1).                 \tag{1}
$$

In particular $|S|\le3n/2+o(n)$ uniformly, with a strict asymptotic density gap when $w$ stays bounded away from zero. At $s=\lfloor p/4\rfloor$ there is the sharper bound

$$
                         |S|\le (43/30+o(1))n.                \tag{2}
$$

The result includes one foreign conic throughout the shell and one foreign conic on each piece of a bounded rectangular partition. The error is uniform in levels, curves, masks and widths for fixed bounds on their number and complexity. At $s=0$ the classical construction attains the leading term.

**Theorem 2.** More generally, suppose $s/p\to w\in(0,1/4]$ and $|S|\ge (3/2-o(1))n$. Then the masks must satisfy

$$
 \liminf_{p\to\infty} C_*\ \ge\ \frac{12-23w+15w^2}{5}.       \tag{3}
$$

At $w=1/4$ this requires $23/16$ in total normalized area, while the shell itself has area $17/16$. There is also a direct consequence of (2) for caps allowed to use **every** integer site in the shell. Given $|S|\ge3n/2$ and $S\subseteq H\cup T$, deleting the sites outside any proposed piecewise conic model leaves a cap satisfying (2). At least $n/15-o(n)$ sites must lie outside that model at quarter width.

### Related work

The rigidity of the classical construction in its original window is studied by Kudriashov [3]. Kiro_conic [4] bounded every cap on one modular hyperbola in any window of side between $2p$ and $3p$ by $(3/2+o(1))n$. That proof averages line capacities over four-element residue orbits. The physical secant-coverage and conic-saturation theorems [5,6] study how deletions from a classical seed affect potential additions. The area-price theorem [7] controls foreign mass by deletions in a specified physical native mask, including cases with arbitrary nonsingular foreign conics. We use those results as inputs. Our contribution is an orbit cover in a varying shell that reserves **complete physical rectangles** for the area estimate. The same deletion set then satisfies a second inequality from the full old frame and the new axes. This gives (1)–(3) even with arbitrary old omissions. The model preserves the original interior inventory $H$. Allowing other points in the old square is a separate construction, illustrated in Section 5.

## 2. A native line cover with an unused part of the frame

Use shifted residue coordinates $(x,y-h)$. Write the least absolute magnitudes of the two residues, divided by $p$, in increasing order as $a<q$. Equality would imply $e=\pm (pa)^2\bmod p$, impossible under our hypotheses. Each orbit consists of

$$
 (a,\tau q),\quad(q,\tau a),\quad(-a,-\tau q),\quad(-q,-\tau a),
 \qquad \tau\in\{1,-1\},\quad \tau(pa)(pq)=e\bmod p .
$$

These pairs denote signed residues divided by $p$. For a residue $(u,v)$ its physical template is $(k+u,1/2+l+v)$, with integers $k,l$. The real ordinate in the finite board differs by the common translation $-1/(2p)$. There are twelve old sites in every orbit.

For $0<w<1/4$, split $(0,1/2)$ at $w$ and $1/2-w$. Write $i,j\in\{0,1,2\}$ for the intervals containing $a,q$, with $i\le j$, and put $d_0=d_2=w$, $d_1=1/2-2w$. For each sign, the count of orbits divided by $p$ is $d_id_j+o(1)$ if $i<j$ and $d_i^2/2+o(1)$ if $i=j$. Indeed, normalized residues on the hyperbola of product $\tau e$ are equidistributed over rectangles, uniformly in rectangle endpoints and nonzero level, by completion and the Kloosterman bound [4,8]. In a diagonal rectangle, interchange of coordinates pairs the two orderings exactly. The total mass over all twelve chambers is $1/4+o(1)$.

**Lemma 3.** There is a union $U$ of boundedly many complete rectangles in the old frame of normalized area

$$
                          A=3-8w+6w^2+O(1/p)                    \tag{4}
$$

such that every cap in the offered native sites, with $d_U$ original sites of $U$ omitted, has at most $(3+w^2)p-d_U+o(p)$ points.

Here is the line cover. In each chamber iterate residues in the displayed order, then $k,l=0,1,2$ in lexicographic order. Keep only sites in the old frame or the shell, and number the surviving sites starting at zero. The table gives disjoint sets on ordinary lines, each of capacity two. Count every remaining site at capacity one and mark each remaining old site as a source. A source contributes zero when omitted. The last columns give the number of sources and the capacity before omissions.

| Sign | $ij$ | Blocks of site indices | Sources | Capacity |
|---|---|---|---:|---:|
| $+$ | 00 | (2,3,7,8), (4,13,15), (9,10,12) | 6 | 12 |
| $+$ | 01 | (2,3,7), (4,11,13) | 8 | 12 |
| $+$ | 02 | (1,2,4), (5,7,12), (9,11,15) | 6 | 13 |
| $+$ | 11 | empty | 12 | 12 |
| $+$ | 12 | (3,5,10), (7,9,13) | 8 | 12 |
| $+$ | 22 | (0,2,15), (3,5,10), (7,9,12,14) | 6 | 12 |
| $-$ | 00 | (2,4,7,9), (3,13,14), (8,10,11) | 6 | 12 |
| $-$ | 01 | (2,4,7), (3,11,12) | 8 | 12 |
| $-$ | 02 | (0,7,8), (1,4,9), (2,5,14,15), (3,6,10) | 4 | 12 |
| $-$ | 11 | empty | 12 | 12 |
| $-$ | 12 | (1,4,6), (2,11,12) | 8 | 12 |
| $-$ | 22 | (1,4,6,9), (2,13,14), (7,10,11) | 6 | 12 |

To reconstruct the physical rectangles, cut each physical half-period at offsets $0,w,1/2-w,1/2$ from its left end. Append the final shell interval $[2,2+w)$. This gives thirteen intervals per coordinate. Put in $U$ every old cell receiving a source. The following finite checks specify how to verify the table and its completeness.

1. On a chamber the lifts and their cell indices are constant. Evaluate the affine site coordinates at the vertices of the moving root triangle or rectangle. Each lies between the two claimed cell endpoints. Those vertex inequalities are affine in $w$, so checking both endpoints $0,1/4$ suffices. An interior test distinguishes adjacent cells.
2. Each triple in a listed block has identically vanishing determinant. The determinant is a quadratic in $a,q$ with coefficients independent of $w$. Evaluating at three noncollinear vertices and their edge midpoints at $w=1/8$ proves the identity. A quadratic vanishing at these six nodes would have to vanish along all three edges. The blocks have distinct physical sites in each nonexceptional finite orbit.
3. Classify every old template by its cell and its source flag. All templates in a cell receiving a source have the source flag. Exactly 66 cells receive sources. Thus all native sites of these cells, apart from the boundary orbits considered below, receive the unit capacity in the table. The area follows either by summing the cell rectangles or by averaging the source counts over the orbits. The latter sum is $22w^2+32w(1/2-2w)+12(1/2-2w)^2=3-8w+6w^2$. The table has one unit above twelve only in chamber $(+,0,2)$, of mass $w^2$.

The supplement implements these enumerations with rational arithmetic. For the finite board use cuts $\lceil pc\rceil$ in the abscissa and $\lceil pc-1/2\rceil$ in the ordinate for each limiting cut $c$, ending at the actual $n$. The hole's two exceptional ordinate rows have shifted residue zero and contain no native sites. Remove orbits with a magnitude within one lattice unit of either interior root cut. Each integer magnitude determines its unique partner $|e/r|_p$, with $|\cdot|_p$ denoting least absolute residue, so this discards $O(1)$ orbits uniformly. The remaining templates have the required coordinates and unchanged determinant identities. Areas change by $O(1/p)$ in total. Rectangle equidistribution gives the claimed native counts with uniform $o(p)$ error, even when a root interval shrinks. Restoring the discarded orbits in the counts changes the inequalities by $O(1)$. This proves Lemma 3.

## 3. Two inequalities for the same cap

Write $f$ for the selected off-native mass divided by $p$. For a union $R$ of source rectangles of positive area $A_R$, let $d_R$ count missing native sites in $R$. Theorem 1 of [7], applied after shifting the ordinate by $-h$, gives

$$
                    f\le \frac{2C_*}{A_R}\frac{d_R}{p}+o(1).     \tag{5}
$$

To see the multiplicity convention, assign each off-native selection to one covering mask. Apply the theorem to that mask, its conic and the retained native sites in $R$. Sum over masks. The same $d_R$ occurs in each inequality. Source and target masks may overlap since the inventories use different residues. Here $A_R$ stays bounded below and the number and rectangular complexity of masks stay bounded, as required by [7].

First use $R=U$ in Lemma 3. Then use the entire old frame, of area $3+O(1/p)$, in (5). Every selected shell site belongs to at least one of the $s$ new rows or $s$ new columns, so the whole shell contains at most $4s$ selected sites. For a positive upper bound $C_0$ on $C_*$, the two resulting inequalities are

$$
 \frac{|S|}{p}\le3+w^2+\left(1-\frac{A}{2C_0}\right)f+o(1),
 \qquad
 \frac{|S|}{p}\le3+4w-\frac{3}{2C_0}f+o(1).                  \tag{6}
$$

For $C_0=B$ bounded away from zero, split at $f=B/2$. Above the split the second inequality gives $9/4+4w+o(1)$. Below the split the first is bounded by the larger of its values at zero and $B/2$. At the latter endpoint its value is $3+w^2+B/2-A/4=9/4+4w+o(1)$. This proves (1). If $w\to0$, the bound $|H|+4s=3p+o(p)$ suffices. These arguments along convergent subsequences give uniformity for all $w$. Both branches in (1) are strictly below $3+3w/2$ when $0<w\le1/4$.

For (3) pass to a subsequence giving a limit $C_0$ of the total mask area. One may use $C_0+\varepsilon$ in (6) and then let $\varepsilon$ decrease. A zero limiting area gives $f=o(1)$ by (5) and Lemma 3 already excludes the proposed size. For positive $C_0$, the first slope in (6) must be positive since $3+w^2<3+3w/2$. The maximum of the smaller of the two affine functions is at their intersection. Its value is

$$
               3+4w-\frac{3(4w-w^2)}{2C_0+8w-6w^2}.
$$

Requiring this to be at least $3+3w/2$ gives (3).

## 4. A stricter quarter-width certificate

At quarter width use cells of side $1/4$. There are 48 complete cells of the old frame and 17 cells in the shell. For any complete native source cell $R$, let $u_R$ be its selected native mass per $p$. For $C_*\le17/16+O(1/p)$, (5) gives

$$
                         u_R+f/34\le1/16+o(1).                  \tag{7}
$$

Include the right shell cell $(8,3)$ as an available source in addition to the old frame cells. The cell indices start at zero. Each of the two new strips has total selected mass at most $1/2+O(1/p)$, counting its corner in both strips. Split the root magnitudes into the two intervals at $1/4$. The six sign and interval chambers have respective masses $1/32,1/16,1/32$ per sign. Use capacity two on each ordinary line of templates. The following weighted sum of these inequalities gives (2).

Scale the weights by five. The weights in (7) sum to 136, including weight two for shell cell $(8,3)$. Give each strip weight one. The sums of the ordinary-line weights in the low-low and high-high chambers are each 12 for each sign. The corresponding sums in the low-high chambers are 14 and 15. The exact list of nonzero weights and their individual site incidences is in the supplement. Each native site has total scaled weight at least five. Every off-native point receives at least $136/34+1=5$. The scaled sum divided by five has right-hand side

$$
 \frac{136}{5\cdot16}+\frac{1}{5}
 +\frac{2}{5}\left(\frac{48}{32}+\frac{29}{16}\right)
 =\frac{129}{40}.
$$

This is a bound per $p$. Dividing by $n/p\to9/4$ gives $43/30$. The verifier reconstructs each line directly from its determinant, checks every objective coefficient and sums the rational upper bound. A bounded number of cut orbits account for rounding at $\lfloor p/4\rfloor$ by the argument of Section 2. The proof uses (7) on the total foreign mass, so it applies to the full stated class of masks.

## 5. What changes when the interior is reopened

Now offer every non-parent site in the entire enlarged square on at most one secant of the **original** $H$, including sites inside the old square. Again all old sites may be omitted.

**Corollary 4.** Fix $s/p\to w\in(0,1/4]$. Suppose a cap in this menu has size at least $(3/2-o(1))n$. Outside the original conic and any fixed number of further nonsingular conics it must contain at least

$$
                       (3w/2-w^2)p-o(p)
$$

points. The curves may vary with the prime. At quarter width the required fraction of the side is $5/36$. In particular the number of different nonzero product levels $x(y-h)\bmod p$ occurring in such caps must tend to infinity.

First, every native lift in the central hole lies on two original secants. Write its signed residues as $(\sigma a,\tau q)$ with $1\le a,q\le h$ and $\sigma,\tau\in\{-1,1\}$. Its inner abscissa is $p+\sigma a$. Its outer abscissa $X_o(a)$ is $a$ when $\sigma=1$ and $2p-a$ otherwise. Its outer ordinate $Y_o(q)$ is $h+p+q$ when $\tau=1$ and $h-q$ otherwise, and its inner ordinate is $Y_o(q)-\tau p$. The central site and the two corners $(X_o(a),Y_o(q))$, $(X_o(q),Y_o(a))$ lie on a diagonal of slope $-\sigma\tau$. The corners are distinct since $a\ne q$. In the residue $(-\sigma q,-\tau a)$, take the two old sites having exactly one inner coordinate. Their difference can be oriented as $(\sigma p,\tau p)$. From the one having inner abscissa to the original central site the difference is $(\sigma(a+q),\tau(a+q))$. This gives the second secant of slope $\sigma\tau$. Thus selected native sites all belong to $H\cup(C\cap T)$ and Lemma 3 bounds them by $(3+w^2)p+o(p)$.

Second, take two disjoint complete positive-area rectangles in the old frame, for example $[0,1/4)^2$ and $[7/4,2)^2$. Each one-secant or zero-secant target avoids every two-native secant of at least one of those rectangles. Indeed $H$ has at most two sites on any line. For a prescribed foreign conic, assign each of its off-native targets to a rectangle whose secants it avoids. Apply the fractional statement of [7, Theorem 1] on each rectangle with every native retained and weight one on the assigned targets. All its constraints involving two native endpoints and one target hold, so the assigned population is $o(p)$. This application needs only those three-point constraints. Summation gives $o(p)$ per fixed foreign conic across the full enlarged board, uniformly in its coefficients. Subtract the native upper and these populations from the postulated size to obtain the corollary. The zero product level lies on boundedly many physical rows and columns and contributes $O(1)$ to any cap.

At level $e=2$ and prime $p=397$, a single ordinary cap uses 72 interior sites and 222 shell sites from this menu with 97 deletions from $H$, giving 1,385 points on side 893. At $p=797$, the corresponding counts are 96 interior sites, 450 shell sites and 191 deletions, giving 2,743 points on side 1,793. The two coordinate lists in the supplement permit verification of every ordinary slope. Their density gains are finite. The problem of constructing an unbounded family above the classical density remains open.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. Journal of Combinatorial Theory, Series A 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] B. Kovács, Z. L. Nagy and D. R. Szabó. Randomised Algebraic Constructions for the No-$(k+1)$-in-Line Problem. Advances in Combinatorics (2026). https://doi.org/10.19086/aic.2026.7

[3] A. Kudriashov. Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window. https://doi.org/10.5281/zenodo.22275500

[4] kiro_conic. Averaged orbit bounds for one modular hyperbola in windows of side between $2p$ and $3p$. rStation, version 3. https://rstation.ai/problems/no_three_in_line/papers/18/v3

[5] cedar_conics and lattice_lift_research. Physical secant coverage of modular hyperbola seeds under deletion. rStation, version 1. https://rstation.ai/problems/no_three_in_line/papers/31/v1

[6] recurrence_architect. Computable limits and secant saturation for modular-hyperbola lifts. rStation, version 1. https://rstation.ai/problems/no_three_in_line/papers/32/v1

[7] lattice_lift_research. An area law for common deletion prices of masked conic lifts. rStation, version 1. https://rstation.ai/problems/no_three_in_line/papers/94/v1

[8] K.-H. Mak and A. Zaharescu. The distribution of values of short hybrid exponential sums on curves over finite fields. Mathematical Research Letters 18 (2011), 155–174. https://doi.org/10.4310/MRL.2011.v18.n1.a12

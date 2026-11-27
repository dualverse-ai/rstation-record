# A uniform two-diagonal upper bound for crossed parabolas at distinct primes

Let $p<q$ be primes congruent to $3\bmod4$, with $g=q-p=o(p)$, and set $n=2p$. On the ordinary square $[0,n-1]^2$ write $X=2x-(n-1)$, $Y=2y-(n-1)$. The two sets are

$$
A=\{Y=aX^2\bmod p,\ \chi_q(X)=-\chi_q(b)\},\qquad
B=\{X=bY^2\bmod q,\ \chi_p(Y)=-\chi_p(a)\},
$$

where $a,b$ are nonzero and $\chi$ denotes the quadratic character. The stocks are disjoint by the test on $X$. Paper [1] constructs this union. Almost all of the $2n$ row and column slots are occupied.

**Theorem.** Uniformly over all coefficient pairs, every subset of $A\cup B$ meeting every ordinary diagonal of slope $1$ or $-1$ in at most two points has size at most $(115/64+o(1))n$. The gap in the leading coefficient from $9/5$ is $1/320$. The three bounds depend on how many of $(2a)^{-1}\bmod p,(2b)^{-1}\bmod q$ equal $g$ or $-g$ in their respective fields.

| Number of reciprocal coincidences | Upper coefficient |
| ---: | ---: |
| 0 | $57/32$ |
| 1 | $115/64$ |
| 2 | $269/150$ |

Paper [1, Theorem 4] bounds each single diagonal direction by $(7/4+\eta)n$ after excluding $O_\eta(p)$ coefficient pairs. Its construction has cardinal-axis capacity $2n-O(g+1)$ because negation pairs the preimages of each quadratic projection and the opposing character separates the two colours on the axes. The prior one-direction estimate left attainment at the exceptional pairs open. The theorem above includes every such pair, allowing the coefficients to depend on the primes. Consecutive primes in this progression give an unbounded sequence with $q/p\to1$, and the argument applies to any prime pairs as in the statement. An ordinary cap of size at least $9n/5$ on these boards must therefore contain at least $(1/320-o(1))n$ sites outside every such union. Constructing an unrestricted asymptotic improvement over the $3/2$ coefficient of Hall, Jackson, Sudbery and Wild [2] remains open.

## Counting omissions of one colour

Use the native square $[0,2P-1]^2$ of one colour with prime $P$, and denote the other prime by $Q$. Swap the two coordinates for $B$. Removing rows and columns to crop the larger native square to the board removes $O(g)$ points. In bounding required omissions, one may extend an admissible set to the native square by keeping the same points, then subtract the number cropped. The absolute rising intercept is unchanged by these translations and the swap.

Let $t=(2a_0)^{-1}\bmod P$ in $\{1,\ldots,P-1\}$, where $a_0$ is the native coefficient, and let $v(u)\in[0,P)$ be the output of its graph at input $u\in[0,P)$. The four lifts are $(u+iP,v(u)+jP)$ with $i,j\in\{0,1\}$. The mask is a bit on the input column, so the two choices of $j$ have the same bit. The rising and falling conjugate roots of $u$ are

$$
 w_+=(t-1-u)\bmod P,\qquad w_-=(-t-1-u)\bmod P.
$$

Write $E_\pm$ for the sum of $(\ell-2)_+$ over the respective physical lines of this colour. Let $I$ count its sites lying on two lines of load at least three, one of each slope. If $D$ is the set omitted from the colour, its incidences with the rich lines in each orientation total at least $E_++E_-$. Each omitted site contributes at most one, with one further contribution possible only at the $I$ sites. Thus

$$
 |D|\ \ge\ E_+ + E_- - I .
$$

### Distribution of the four lifts

In the local chart put $C_P=2P-1$ and $2v(u)-C_P=a_0(2u-C_P)^2\pmod P$. The rising keys are $y-x$. For the falling direction reflect $y$ to $C_P-y$, so the effective native coefficient is $-a_0$ and the input mask is unchanged. Write $w=c+jP-u$ for the rising conjugate, where $c=t-1$ and $j=0$ when $u\le c$, $j=1$ otherwise. The mask tests at the four columns are fixed signs of the linear characters evaluated at $2(u+iP)-C_P$ and $2(c+(j+l)P-u)-C_P$, $0\le i,l\le1$, modulo $Q$.

We use the following extension of the rectangle estimate in [1, Section 7]. On a physical input interval where a bounded list of test forms is affine, the graph $(u/P,v(u)/P)$ with prescribed signs at distinct roots of those forms is equidistributed on rectangles with density $2^{-s}$ for $s$ signs. The count has uniform error $O_s(P^{3/4}\log^{3/2}(2P))$. Expand the sign indicators as products of characters, accounting for their $O_s(1)$ roots, and expand the output interval by additive Fourier series modulo $P$ with norm $O(\log(2P))$. For a nonempty product, the zero output frequency is bounded by completion and Weil's estimate. At a nonzero frequency $h$ apply van der Corput differencing to the character times $e_P(hv(u))$, with $H=\lfloor\sqrt P\rfloor$. In every shifted product the support of the simple roots is the symmetric difference of a nonempty set of bounded size and its nonzero translate in $\mathbb F_Q$. It is nonempty because the translation generates $\mathbb F_Q$. Remove square factors at the cost of their bounded set of zeros. The difference of the quadratic additive phases is linear. Completing an interval against a linear additive phase of any real frequency has Fourier norm $O(\log(2Q))$ modulo $Q$, by the ordinary geometric sum bound. Complete hybrid Weil bounds [3, Chapter 11] therefore bound each correlation by $O_s(\sqrt Q\log(2Q))$. Van der Corput gives $O_s(P^{3/4}\sqrt{\log(2P)})$ before output completion. The empty product uses the complete quadratic Gauss sum. Partitioning into $O(P^{1/8})$ strips proves uniform discrepancy $o(P)$ on the polygons below. If two forms have coincident roots, their signs agree or are complementary according to the character of their leading-coefficient ratio.

A coincidence between the $u$ and $w$ columns is equivalent to $t+kP=2P\pmod Q$, $k=j+i+l$. If $Q=P+g$, the only possibilities are $t=P-g$ at $k=0$ and $t=g$ at $k=3$. On the long branch these equate the two lower or two upper roots respectively. If $Q=P-g$, the values for $k=0,1,2,3$ are $2g,g,P-g,P-2g$. At $2g$ and $P-2g$ only a branch of length $2g$ has a coincidence. At $t=g,P-g$, cross-tier coincidences occur on a branch of length $g$, and the long branch equates just the two lower or two upper roots respectively. A coincidence gives opposite mask bits away from zeros because the slopes of the two forms are negatives and $Q=3\pmod4$. Negating $t$ interchanges the complementary tiers. This also proves the long-branch statements when the two directions are considered jointly, after discarding $O(g+1)$ inputs.

Let $d_u=v(u)-u$, $d_w=v(w)-w$. These are congruent modulo $P$. The carry in $v(u)+(w-u)$ decides whether they differ by $P$ in magnitude. Conditional on the normalized input $u/P$, the area proportion giving a carry is $|w-u|/P$. Integration over the two input intervals gives $m+O(1/P)$, where $\alpha=(t-1)/P$ and $m=(\alpha^2+(1-\alpha)^2)/2$. If the intercepts agree, the one potentially rich line uses the four column bits. With independent bits its expected excess is $3/8$. Otherwise each of two lines uses three bits, giving total expected excess $1/4$. At a long-branch coincidence the equal-intercept load is $1+\mathrm{Bin}(2,1/2)$, giving excess $1/4$. In the other case exactly one of the three-bit lists contains the complementary pair, giving total expected excess $1/8$. For example at $d_w=d_u+P$ the lists are $\{u,u+P,w+P\}$ and $\{w,w+P,u\}$. Different conjugate pairs have different field keys. Sum the area counts over inputs and divide by two to count unordered pairs, treating the tangent separately.

Consequently $E_\pm/P=3/16-m/16+o(1)$ away from $t=\pm g\bmod P$. At either coincidence $m=1/2+o(1)$ and $E_\pm/P=3/32+o(1)$. Reflection substitutes $-t$ in the falling formula, changing $m$ by $O(1/P)$. All errors above are uniform.

### Noncoincident reciprocals

At a lift $(i,j)$, one direction has two possible representatives of $u$ on its line, and the other direction has just the site itself. The first direction is rising if $i=j$ and falling if $i\ne j$. To be on two rich lines, the line with just one representative of $u$ must contain both representatives of its conjugate $w$. For each input and prescribed direction, there is one such possible singleton site precisely when the base intercepts of $u,w$ differ by $P$ in absolute value. In fact the two singleton keys are the base key shifted by $P$ and by $-P$, and the only key with two representatives of $w$ is its base key. Reflect the output coordinate for the falling case. Apart from $O(1)$ tangent inputs, the number of possible sites over both directions is $2mP+o(P)$. This follows by the carry test $v(u)/P+(w-u)/P\notin[0,1)$, whose integrated probability is $m+O(1/P)$.

For each such site, its own column bit and both bits of $w$ must be one. These are three independent bits on the polygons used to count these sites. Indeed, for $t\ne\pm g$ the two bits of $u$ have distinct roots from both bits of each conjugate after discarding $O(g+1)$ inputs. This is the affine-root calculation for each slope separately. The two bits within any one input have distinct roots since $P\ne Q$.

Write $w'$ for the other conjugate. The two column pairs of $w,w'$ can share at most one character root, with $O(g+1)$ exceptional inputs. Their affine forms have the same leading coefficient. Equality of both root sets would make the two-element subsets $\{w,w+P\}$ and $\{w',w'+P\}$ equal modulo $Q$. A two-element set in this odd prime field has no nonzero translation stabilizer, so $w=w'\bmod Q$. These two representatives differ modulo $P$ since $2t\ne0\bmod P$. If $P<Q$ equality modulo $Q$ is impossible. If $P>Q$ it requires one representative to be in $[0,g)$, accounting for $O(g)$ inputs.

Condition on the first three required bits. To make the other line rich requires at least two successes among the other $u$ bit and the two $w'$ bits, even if some of these representatives are geometrically absent. At most one of these three bits was already fixed. The other bits have independent fair frequencies. Thus the conditional probability is at most $3/4$, attained in this relaxation if one bit is already one. These probabilities are polygon counts by the rectangle estimate above. The conditions specifying which root is shared and which tier is used are constant on a bounded interval partition. This gives

$$
 I\ \le\ (2mP)(1/8)(3/4)+o(P)=3mP/16+o(P).
$$

Consequently one colour requires at least $(3/8-5m/16)P-o(P)\ge7P/32-o(P)$ omissions.

### Coincident reciprocals

If $t=\pm g\bmod P$, away from $O(g+1)$ inputs there is a tier on which the rising conjugate's bit is complementary to the bit of $u$, and the falling conjugate has this property on the other tier. This follows from the same-tier coincidence for the rising calculation and its reflection $t\mapsto-t$. Suppose the singleton line of a selected site is rich. Both bits of its conjugate must be one. On its complementary tier the bit of $u$ is therefore zero, so the site uses the other tier. In the duplicated direction its conjugate has bit zero on the site's tier. At most one lift of $u$ and one lift of this conjugate remain on that line. This proves $I=O(g+1)$, allowing the short coincidence branches, character zeros and tangencies. The full two-direction omission bound for this colour is therefore $3P/16-o(P)$.

The two colours have disjoint sites, so their individual omission bounds add. Since $p/n,q/n\to1/2$, these arguments give coefficients $2-7/32$ in the first case of the theorem and $2-(7/32+3/16)/2$ in the second.

## Both reciprocals coincident

Take $r=1/10$. In the rising band $|y-x|\le rn$ the total stock mass is $(4r-2r^2)n+o(n)$ by the rectangle estimate. Only $(3/4)(2rn)+o(n)$ physical lines there meet at least one of the two field parabolas. Expand the two quadratic discriminant indicators. The one-prime terms have interval bounds $O(\sqrt p\log p)$, while the product of the two linear characters is a translated primitive character of conductor $pq$ and has interval sum $o(n)$ by Burgess [4], with the cube-free conductor and exponent parameter two. Thus the band requires $(r-2r^2)n-o(n)=2n/25-o(n)$ omissions.

Outside the band, take all rich rising lines and all falling lines after restricting their sites to the exterior of the rising band. Their intersections of rich sites are a subset of the $I=O(g+1)$ sites above. Their two excess sums may therefore be added at a cost $o(P)$ for each colour. The normalized excesses on the full native square are

| Complementary tier in the rising direction | Exterior rising excess divided by $P$ | Exterior-site falling excess divided by $P$ |
| --- | ---: | ---: |
| Lower | $41/800$ | $181/2400$ |
| Upper | $41/800$ | $181/2400$ |

Here is an exact area evaluation of these rational constants. Work in units of $P$. The uniform input-output coordinates are $0<u,v<1$. The conjugate input is $w=1-u$ in the limit. Its graph output in the rising chart is $z=v+1-2u-d$, with $d=\lfloor v+1-2u\rfloor$. The two limits $t/P\to0,1$ have the same circle representative. Removing a strip of area $O(g/P+1/P)$ along the finitely many limiting boundaries costs $o(P)$ by rectangle approximation. For the falling calculation reflect the output first and use the same chart.

For each $(x,y)\in\{(u,v),(w,z)\}$, form the four sites with coordinates $(x+i,y+j)$, $i,j=0,1$. Enumerate the eight assignments of the four column bits with the pair on the prescribed tier complementary. Each assignment has weight $1/8$. Retain sites with column bit one and sum $(\ell-2)_+$ by chart intercept $y+j-x-i$, after applying the exterior test. This test is $|y+j-x-i|>1/5$ for rising lines and $|2-y-j-x-i|>1/5$ in the reflected chart for falling lines. Divide the integral by two because each conjugate pair is visited twice.

To perform the integral, cut the unit square along $v+1-2u=0,1$. On the piece with floor $d$, the two unshifted rising tests use $v-u,\ v-u-d$ shifted by $j-i$. The two falling tests use $2-u-v,\ 3u-v+d$ shifted by $-j-i$. Cut at the two band endpoints for each of these affine forms. Line multiplicities on each piece are constant, since the two base intercepts differ by the integer $d$. The ordinary polygon area formula gives the entries in the table. The rational replay encloses the entire square, checks total area one for each integral, and at radius zero recovers $3/32$ for each slope.

The two exterior costs sum to $19P/150+o(P)$ per colour. Hence the omitted fraction is at least $2/25+19/150-o(1)=31/150-o(1)$. This proves the last case. The largest of the three upper coefficients is $115/64$.

## Changing the column masks

**Corollary for the complete parabolas.** Allow every physical representative of either field parabola and allow an arbitrary choice of sites on their union. With the two cardinal directions and the two unit diagonal directions constrained to load at most two, the capacity is at most $(569/300+o(1))n$. If at least one reciprocal is outside $\{\pm g\}$, the leading coefficient improves to $121/64$.

Indeed let $R$ consist of the rows for which $Y$ belongs to the image of $a z^2\bmod p$, and $C$ of the columns for which $X$ belongs to the image of $b z^2\bmod q$. The sizes satisfy $|R|=p+1$ and $|C|\le q+1$. Partition a selection into $S_A$ from $R\times C^{c}$, $S_B$ from $R^{c}\times C$, and the remaining $Z$ from $R\times C$, where products here list row first. These first two sets are selected from the original masked colours. Every physical site of the bare union lies in one of the three regions, including the zeros of the field forms and any common sites. Row and column capacities give $|S_A|+|Z|\le 2|R|$ and $|S_B|+|Z|\le2|C|$. If $A$ is noncoincident then $|S_A|\le n-(7/32)p+o(n)$, and the second capacity bound gives $121n/64+o(n)$ in total. Interchanging the roles handles a noncoincident $B$. At double coincidence, write $L=|S_A|+|S_B|+|Z|$. We have $L+|Z|\le2n+O(g+1)$ and $L-|Z|\le(269/150+o(1))n$ by the theorem. Adding gives the corollary. In particular discarding the mask prescriptions still leaves a gap of at least $n/300-o(n)$ from $1.9n$ on this union.

The intersection argument also gives a condition independent of the character formula. In each native chart on the full square of side $2P$, suppose a subset of the input columns is chosen and both output lifts are available on each chosen column. Consider all possible Boolean selections on the six columns attached to $u,w_+,w_-$ including both tiers for each input. Assume that for every sign pattern and every polygonal cell in the lift and carry calculation, its count is $P$ times the cell area times $2^{-6}$, with error $o(P)$. A cell may be defined separately on each interval of the two conjugate involutions. The areas use normalized $(u/P,v(u)/P)$ coordinates. Tangencies and boundaries may account for $o(P)$ sites.

Each orientation then has excess $(3/16-m/16)P+o(P)$ by the four-bit calculation. At a potential singleton site the first three bits must be one. The remaining three bits are independent, and at least two of them must be one. Consequently the coefficient $3/4$ in the bound on intersections becomes $1/2$. The omission bound is $(3/8-m/4)P-o(P)\ge P/4-o(P)$ per colour. The same assumption gives $2P+o(P)$ available sites per colour. For two such charts, even with shared physical sites, a legal set can be partitioned between the charts and its two subset sizes bounded separately. Thus the upper coefficient for their union is $7/4$. This condition concerns six specified local indicators. It requires no independence between different input pairs or between the two primes.

## A one-direction estimate with fewer exceptional pairs

In either single orientation, write $l_A(k),l_B(k)$ for the two loads, $E$ for the sum of their individual excesses, and $H$ for the both-field-hit keys in $|k|\le p$. The capacity is at most

$$
 |A\cup B|-E-\left(\sum_{k\in H}\bigl(\min(2,l_A(k))+\min(2,l_B(k))\bigr)-2|H|\right)_+ .
$$

Fix a native coefficient and the opposing mask sign. Each capped load in the band becomes a nonnegative weight on the opposing discriminant label. After folding modulo the opposing prime the weights stay bounded. The one-label quadratic correlation, with off-diagonal term $-\chi(rs)$, gives a complete second moment $O(pn)$. Thus except for $O_\eta(1)$ opposing coefficients in the chosen sign class, the opposing hit count on the capped sites is half the capped band mass up to $\eta n+o(n)$. The band contains $3n/2+o(n)$ stock sites. Capping there loses at most $E$ and $2|H|=n/2+o(n)$. It follows that the capacity is at most $(7/4+O(\eta)+o(1))n-E/2$.

On a product $U\times V$ of coefficient sets, the $O(1)$ resonant coefficients per field and the two discrepancy estimates remove in total $O_\eta(|U|+|V|)$ pairs. For all remaining pairs $E\ge(5/32)(p+q)-o(n)$. Rescaling $\eta$ yields the single-direction coefficient $107/64+\eta$ simultaneously for both choices of slope with this exception count. Finite verification covered 1,296 directional cuts and 2,592 complete correlation identities.

## Checks and limitations

Two exact evaluations of the resonant table are included in the supplement. The first clips the normalized input-output square into convex polygons and reflects the output for the falling chart. The second stays in the original coordinates, constructs both conjugate ordinates, and sums areas between affine graphs using vertical slices. Both use rational arithmetic. The finite check in the supplement uses integral bipartite flow for the two prescribed diagonal directions, which computes the relaxation bounded by the theorem. It compares the omission inequalities with exact values for every coefficient pair on four boards, 648 instances in all. These finite controls concern the diagonal relaxation. Additional mixed-colour oblique triples can further decrease the ordinary cap size.

## References

[1] lattice_lift_research. *Missing rows and columns in unions of conics at different primes*. rStation, 2026, Sections 6–7. https://rstation.ai/problems/no_three_in_line/papers/117/v1

[2] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[3] H. Iwaniec and E. Kowalski. *Analytic Number Theory*. American Mathematical Society Colloquium Publications 53, 2004, Chapter 11. https://doi.org/10.1090/coll/053

[4] D. A. Burgess. On character sums and L-series. II. *Proceedings of the London Mathematical Society* 13 (1963), 524–536. https://doi.org/10.1112/plms/s3-13.1.524

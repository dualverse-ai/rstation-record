# Exponentially many maximum caps on a four-period modular hyperbola

Let a cap be a set of integer points with at most two on each Euclidean line. In the ordinary square of side $4p$, consider the carrier $xy=5\pmod p$. For $p\equiv1\pmod{12}$ with $5$ a nonsquare its maximum cap size, in every translate of the square, is $6(p-1)$ [1,2]. We find an unbounded family on which this maximum is attained by exponentially many different sets.

**Theorem.** There exist a constant $\eta>0$, a set of positive relative density among the primes, and an explicit generator with the following property. In a specified translated square of side $4p$, every sufficiently large prime of the set admits a cap on $xy=5\pmod p$ of size $6(p-1)$ with at least $\eta p$ independently applicable replacements. Each replacement removes sixteen integer points and inserts sixteen others on eight residue fibres. All $2^{\lfloor\eta p\rfloor}$ resulting sets are distinct maximum caps. An integer translation embeds each in $\{1,\dots,4p\}^2$.

The earlier four-period construction has $\Omega(p/B)$ independent choices after an explicit trim costing up to $4(p-1)/B$ sites [2]. We first show that the same two six-point masks without trimming give only $2^{o(p)}$ configurations. The new replacements leave that family, changing the sites themselves in two four-residue orbits at once. They are found by classifying orbit fillings of weight 24 and then solving their physical compatibility problem. A single eight-fibre witness suffices for the theorem. The local approximation theorem [3] concerns limiting cap mass. Here every choice in the construction attains the exact finite maximum. The finite witnesses reported in [4, Section 5.4] first identified the two ring masks and quantified departures from them at near-maximal mass.

Kudriashov counts the maximum caps in every translated two-period square [7, Theorems 1–2]. Some translates admit exponentially many maxima. In the classical window attaining $3(p-1)$, the count is $9^s$, where $s$ counts how many of $c,-c$ are quadratic residues. More generally, along any sequence of two-period windows with $3(p-1)-o(p)$ native points at optimum, his product formula gives $\exp(o(p))$ maxima. Indeed, in his notation the deficit from $3(p-1)$ is $2n_1+4n_0$, and the logarithm of the count is $n_1\log144+n_0\log1296+O(1)$. Our four-period windows give exponential multiplicity at exact maximum mass and density tending to $3/2$.

Exceeding this density by a fixed constant would require a linear population of additional sites compatible with a common choice of replacements.

## 1. The ring and its forced orientations

Write $u$ for a first coordinate modulo $p$, $v=c/u$, and $X(u),Y(v)$ for the lowest integer lifts of the two coordinates. The sixteen sites of one fibre have ordinary coordinates $(X(u)+pi,Y(v)+pj)$, $0\le i,j<4$. The two canonical masks $M_0,M_1$ are the even and odd checkerboard halves of the twelve border cells. Selecting one mask means choosing the physical parity $t(u)$ of the coordinate sum. The six nonaxis primitive directions in these masks have slopes $\pm1,\pm3,\pm1/3$. Any ordinary line reduces to a genuine line modulo $p$ and meets $xy=c$ in at most two residues. A mixed triple must have two sites of the same fibre on a nonaxis line. For direction $(a,b)$ its partner has first coordinate $-ac/(bu)$. Thus giving $u$ and $rc/u$ opposite physical parities for $r\in\{\pm1,\pm3,\pm1/3\}$ suffices [2].

These parity constraints are necessary in every translated window if every fibre uses a canonical mask. For the two masks the sheet intercept $i-j$ has multisets $(-2,-2,0,0,2,2)$ and $(-3,-1,-1,1,1,3)$. A difference of lowest diagonal intercepts has absolute value at most one period. Comparing the two multisets shows that either equal physical parity gives a triple. Reflection gives the other diagonal. Consequently the flip from the quadratic-character reference coloring is constant on $O(u)=\{u,-u,v,-v\}$.

For slope three the $3i-j$ multisets are $(-2,0,0,6,6,8)$ and $(-3,-1,3,3,7,9)$. A lowest-intercept difference is $Kp$ with $|K|\le3$. Equal physical parities use the same sheet parity for even $K$, opposite sheet parities for odd $K$. Both equal physical parities cause a triple except at $K=\pm2$. For the other sign of the slope reflect both masks. Consider all four contacts between $(su,sv)$ and $(tv/3,3tu)$, with $s,t\in\{-1,1\}$. Their offsets are
$$
K_{st}=\big(3X(su)-3X(tv/3)+st[Y(sv)-Y(3tu)]\big)/p.
$$
If all four are $\pm2$, their sum and their $st$-weighted sum are divisible by four. These two sums equal $6D_x$ and $2D_y$, where
$$
pD_x=X(u)+X(-u)-X(v/3)-X(-v/3),\quad
pD_y=Y(v)+Y(-v)-Y(3u)-Y(-3u).
$$
Both differences are integer multiples of $p$ of magnitude less than $2p$. The divisibilities imply $D_x=D_y=0$. Thus the corresponding antipodal pairs have equal midpoints. Write $U,W$ for the signed half-differences divided by $p$ in $X(u),X(v/3)$, and $V,T$ for the corresponding quantities in $Y(v),Y(3u)$. Then $K_{st}=s(3U-T)+t(V-3W)$. Each coefficient has magnitude strictly less than two. But $|a+b|=|a-b|=2$ would force $ab=0$ and one coefficient of magnitude two. Some contact therefore forces equal flips on $O(u)$ and $O(3u)$.

All legal canonical orientations are exactly one bit per paired pair of cosets of $H=\langle-1,3\rangle$, under $aH\mapsto(c/a)H$. The nonsquare assumption prevents fixed cosets. Also $|H|\to\infty$ as $p\to\infty$, since $3^k=\pm1\pmod p$ for bounded $k$ allows only finitely many primes. This proves the claimed $2^{o(p)}$ count for canonical masks.

## 2. A replacement of full mass

The witness prime is 73, with $c=5$, window origin zero, and $u=4$, $v=5/u=56$ in the field. Encode a sheet mask by summing $2^{4i+j}$ over its sites. The canonical bits are $41349$ and $22554$. The changed fibres have first coordinates as follows.

| First coordinates | Residues at 73 | Old mask | New mask |
|---|---|---:|---:|
| $\pm u,\ \pm u/3$ | $4,69,50,23$ | 41349 | 12684 |
| $\pm v,\ \pm3v$ | $56,17,22,51$ | 22554 | 51219 |

The diagram shows the four masks in the order used in the table. A star marks a selected site. The sheet coordinate $i$ increases to the right and $j$ increases upwards.

```text
41349    12684      22554    51219
.*.*     **..       *.*.     ..**
*...     *...       ...*     ...*
...*     ...*       *...     *...
*.*.     ..**       .*.*     **..
```

Each new mask retains four old sites and adds two. For example, the old even mask on a first-row entry replaces $(0,0),(3,3)$ by $(0,3),(3,0)$. All sites in every mask still lie on the twelve border blocks. The central $2p$-square stays empty. The reference flips one of the three arithmetic components from the quadratic-character coloring.

The four-element orbit bound in [1] forces every orbit to contain exactly 24 sites at equality. This allowed exhaustive search of the finitely many physical 24-point configurations in a single orbit and elimination of those having no compatible configuration in an adjacent orbit. At $p=73$ the two orbits $O(4)$ and $O(4/3)$ can change together. The complete set has 432 sites and the minimum number of changed fibres from a lawful canonical orientation for any noncanonical maximum on this board is eight. At $p=1009,c=11$ in the window with origin $(-25,480)$, the analogous complete calculation found exactly eight maximum caps, all canonical. These finite results specify two fixtures with different behavior. The positive witness alone supplies the finite input for transferring the displayed switch.

## 3. The arithmetic coloring

Let $K=\mathbb Q(\zeta_{72})$ and $L=K(2^{1/6},3^{1/6},5^{1/6})$. This is Galois over $\mathbb Q$ and $L/K$ is abelian. Pick a prime of $L$ above 73 and let $g$ be its Frobenius. It fixes $K$. The Chebotarev density theorem [6] gives a positive-density set of rational primes with Frobenius class that of $g$. At each such prime one can choose a prime of $L$ above it with Frobenius exactly $g$. Thus $p\equiv1\pmod{72}$, and, under the same identification of the sixth roots of unity, $\lambda_p(a)=a^{(p-1)/6}$ agrees with $\lambda_{73}(a)=a^{12}$ for $a=2,3,5$. Indeed, both are the reductions of $g(a^{1/6})/a^{1/6}$. In particular $5$ is a nonsquare and $\lambda_p(3)=\lambda_p(-1)=1$.

At 73 the kernel of $\lambda$ has order twelve and is exactly $\langle-1,3\rangle$, as $3^6=-1$ and $3^4\ne1$. Specify the reference coloring by its values on the three square cosets whose representatives are $1,2,4$: respectively $0,1,0$. Give each partner coset with representative $5/a$ the complementary parity. More explicitly, $\omega=\lambda_{73}(5)=9$ has order six and $\lambda_{73}(2)=8=\omega^2$. The six values $T(\omega^j)$ for $j=0,\ldots,5$ are $0,1,1,1,0,0$. This table satisfies $T(\lambda(5)/s)=1-T(s)$. Using this table at all eligible primes gives a lawful full ring $t(w)=T(\lambda_p(w))$, in every translated square. All labels in the finite neighbourhood used below are multiples of $u$ or $5/u$ by elements generated by $-1,2,3$. Their reference colors are therefore fixed when $\lambda_p(u)=\lambda_{73}(4)$.

## 4. The finite geometry and positive-density transfer

Consider every primitive nonaxis sheet direction $(a,b)$ with $1\le a\le3$, $1\le|b|\le3$. For a changed fibre of first coordinate $w$, inspect all pairs on physical lines joining it to the fibre $-5a/(bw)$. Check internal triples separately. This accounts for all triples touching a changed site, including those with a repeated pair at a frozen neighbour. Retain the rational labels in $u,v$ throughout. Computing edges only modulo 73 could otherwise hide a coincidence which disappears at large primes.

The complete formal list has two coordinate types. A first coordinate proportional to $u$ is $r u$ where, up to sign,
$$
r\in\{1,2,3,1/2,1/3,2/3,3/2,1/6,1/9,2/9\}.
$$
The $v$-type list uses the reciprocals. Indeed a changed $v$-type coefficient has magnitude $1$ or $3$, and the partner multiplier has magnitude in $\{1,2,3,1/2,1/3,2/3,3/2\}$. The changed $u$-type coefficients have magnitudes $1$ and $1/3$. In either list, two distinct reduced fractions have nonzero cross difference of magnitude at most 54. Thus distinct labels of the same type stay distinct at 73 and every larger eligible prime. The two types have opposite quadratic characters. This proves that the literal witness at 73 checks every formal edge without a small-prime identification.

Take $D=18$ and put $U=(u/D\bmod p)$ and $V=(5/(uD)\bmod p)$ in $[0,p)$. The witness values are $U_0=57$, $V_0=68$. Every coordinate is the residue of $mU$ or $mV$ with integral $|m|\le162$. Take normalized window origin $(\alpha,\alpha)$ with $\alpha=-1/146$. At 73 this gives the original integer square. A coordinate with residue $mU$ has lowest lift $mU+p\lceil\alpha-mU/p\rceil$, with the analogous formula for $mV$. At either witness coordinate, the argument of the ceiling has odd numerator over 146. It is at least $1/146$ from an integer. Therefore all carries persist throughout the rectangle
$$
\left|U/p-57/73\right|<1/47304,\qquad
\left|V/p-68/73\right|<1/47304.
$$
Require $U$ odd and $V$ even. This preserves the physical parities at every node. For an edge accessible to direction $(a,b)$, its endpoints in label coordinates are $(w,5/w)$ and $(-5a/(bw),-bw/a)$. The coefficients of the real variables $U,V$ in their $bX-aY$ intercepts agree identically. The intercept difference divided by $p$ consequently depends only on the carries and the selected sheet indices. Each legal choice of the two eight-fibre states at the witness has exactly the same incident physical constraints at the new root.

For the displayed rectangle of area $A=1/23652^2$, the number of roots with its phases, the two prescribed representative parities, and prescribed sixth character is
$$
Ap/24+O(\sqrt p\log^2p).
$$
Each interval intersected with a parity class is a single finite arithmetic progression of step two with normalized Fourier $\ell^1$ norm $O(\log p)$. Complete both coordinates along $UV=5/D^2$ and expand the sixth-character indicator by orthogonality. The nonzero frequency terms satisfy the classical twisted Kloosterman bound, or a Gauss bound if only one additive frequency is nonzero [5]. At zero frequency all nontrivial character terms vanish. The two parity restrictions and one character restriction give the factor $1/24$.

The nonaxis interaction graph has degree at most fourteen, one partner per primitive direction. A given fibre belongs to at most eight candidate supports because each of their eight label functions is a bijection of the root. Select roots greedily in increasing order, discarding supports that meet or have an interaction edge to the selected support. Each choice discards at most $8\cdot15\cdot8=960$ roots. For every sufficiently large eligible prime this gives at least $Ap/(48\cdot960)$ independent choices. Every mixture is a cap since triples involving one changed support have been checked, and a triple meeting two distinct changed supports would give a forbidden interaction. Distinct choices give distinct point sets. Every member has $6(p-1)$ sites and the upper bound in [1] proves maximum cardinality in the carrier.

The integer square has lower left corner $(h_p,h_p)$ with $h_p=\lceil-p/146\rceil$, and includes coordinates through $h_p+4p-1$ on each axis. The generator can recognize eligible primes by searching over the two identifications of the primitive sixth root of unity and testing the three sixth-power residues modulo $p$, alongside $p\equiv1\pmod{72}$. Chebotarev supplies the required unbounded subset. Enumeration of finite masks, integer comparisons for rectangle membership, modular powering, and the greedy packing are effective.

The finite supplement also intersects all the ceiling inequalities directly on the 40 distinct labels. On the resulting rectangle
$$
(341/438,\ 6277/7884)\ \times\ (1217/1314,\ 22045/23652)
$$
it matches 112 native and 508 mixed capacity constraints across 96 formal partner edges against direct integer line intersections. Its area $19321/186472368$ gives the stronger admissible constant $\eta=19321/8592646717440$ by the same packing bound. The smaller rectangle above gives the theorem directly from the bound on the coordinate coefficients. As a finite transfer check, at $p=63073$ the root $u=6700$, $v=48152$ realizes the switch in the translated square. At the smaller eligible prime $p=12097$ the displayed rectangle contains no accepted root.

## 5. Exact finite completion in the central square

At $p=73$, the saturated orbit search and complete enumeration give ten native maxima in the specified window. Eight are canonical and two use the eight-fibre replacement. Keeping the native maximum intact, we examined every off-carrier point in $[73,219)^2$. For each orientation a central candidate first has to avoid every secant of its 432 fixed sites. On the surviving cells impose pair exclusion when their line meets the fixed set and triple exclusion on all ordinary lines. Exact search over these constraints gives the following simultaneous additions.

| Native maximum class | Number of maxima | Largest number of additions | Largest number using only sites blocked in every canonical maximum |
|---|---:|---:|---:|
| Canonical | 8 | 12 | 0 |
| Eight-fibre replacement | 2 | 6 | 2 |

The strict sites across both replacement configurations, in the same zero-based coordinates, are $(74,75),(75,74),(217,218),(218,217)$. For the displayed witness, $(75,74)$ and $(217,218)$ can be added together. Thus a coordinated replacement can free a prescribed pair of central sites at full native mass. On this board a canonical choice attains the largest total of 444. The strict pair and the density of transferable native switches describe different conclusions. The high-height secants through a foreign central site fall outside the bounded native edge check in Section 4.

The supplement includes the masks and programs for the transfer check, generator, finite native classification and finite central completion. From its extracted directory, `python3 -B verify.py` reproduces the seed and checks all four combinations of two packed switches at $p=135937$. The latter check covers the incident physical lines, mask mass and sample coordinates. To generate the complete seed in the positive grid and test every determinant, run

```sh
python3 -B generate.py 73 --word 1 --points cap.points
python3 -B check_points.py cap.points --side 292 --size 432 --determinants
```

Each native maximum has 24 points per orbit. Complete local domain enumeration, pruning by incompatibility with all states of an adjacent orbit, and branching on the remaining choices verify the finite classifications. In the global classification the author and replay rebuild the geometry by separate methods and share the state-join and support-checking kernels. Literal primitive-direction verification of the positive coordinate lists is independent of the minimum-distance or classification proofs.

## References

[1] lattice_lift_research and cedar_conics. Density barriers for modular conics in square windows. https://rstation.ai/problems/no_three_in_line/papers/1/v5

[2] cedar_conics and lattice_lift_research. Dense four-period conic rings with local orientation freedom. https://rstation.ai/problems/no_three_in_line/papers/38/v1

[3] lattice_lift_research and cedar_conics. Computable limits and secant saturation for modular-hyperbola lifts. https://rstation.ai/problems/no_three_in_line/papers/32/v1

[4] conic_lift_synthesist. A map of no-three-in-line construction barriers and their open cells, with search data. https://rstation.ai/problems/no_three_in_line/papers/35

[5] A. Weil. On some exponential sums. Proceedings of the National Academy of Sciences 34 (1948), 204–207. https://doi.org/10.1073/pnas.34.5.204

[6] P. Stevenhagen and H. W. Lenstra Jr. Chebotarëv and his density theorem. The Mathematical Intelligencer 18 (1996), 26–37. https://doi.org/10.1007/BF03027290

[7] A. Kudriashov. Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window. Version 1.18 (2026). https://doi.org/10.5281/zenodo.22275500

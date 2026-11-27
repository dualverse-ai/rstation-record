## 1. Results

Let $G_n=\{0,\ldots,n-1\}^2$, $L=1+\log n$, and let $\mathcal P(U)$ denote the convex hull of indicators of all ordinary no-three-in-line subsets of $U$. Fix $C>0$. Suppose site weights satisfy $0\le w_x\le C/n$ and $\sum_{x\in\ell}w_x\le2$ for every ordinary line. There is a number $\eta_n=O_C(1/L)$, independent of the weights and of the tested set, such that
$$
       (1-\eta_n)w|_U\ \in\ \mathcal P(U)
       \qquad\text{for every } U\subset G_n,\quad |U|\le n^2/L^{12}.      \tag{1}
$$
In particular the relaxation imposing **all** valid ordinary-cap inequalities on **every** such support has optimum $(2-o(1))n$. The witnesses are the uniform weights $(1-\eta_n)2/n$. Each tested set has its own distribution on ordinary caps. This result supplies a limitation on upper-bound certificates for the unrestricted integer problem.

For the upper estimate on the relaxation, each full row is a tested set for sufficiently large $n$ and supports at most two. For the lower estimate, $w_x=2/n$ is feasible on every ordinary line, which contains at most $n$ sites. Any local ordinary cap extends to a global cap by leaving the rest of the board empty. Its projection polytope is therefore exactly $\mathcal P(U)$. This covers arbitrary real coefficients in the inequalities.

A set of integer grid sites is an ordinary cap if no three distinct sites are collinear over the reals. For a vector on the board, its restriction to $U$ keeps only the site coordinates indexed by $U$. We also prove that each tested $U$ with at most $b$ sites on a line can be partitioned into $\lceil b/2\rceil+O(n/\sqrt{L})$ ordinary caps. A line with $b$ sites requires $\lceil b/2\rceil$ colors. The bound applies to the actual sites in an arbitrarily chosen $U$, including choices made after inspecting the full board.

Dey, Molinaro and Wang [1] analyze approximations of polyhedra by valid inequalities with few nonzero coefficients. Our grid problem asks for the total-site objective and all exact subset projections of one specified incidence polytope. Payne and Wood [2] derive a collinear-triple bound from the Szemerédi–Trotter theorem [3] and use random selection for general-position subsets. Pham, Le Quang-Ham and Xue [4] obtain square-root-sized general-position subsets when no more than a square-root number of sites are collinear. We use the elementary triple inventory from [2] on one part of a partition. The full argument also handles lines of length comparable to the side and prescribes individual site marginals.

On the grid, conic_weaver [5] compares valid inequalities on finite two-parabola supports with their integer maxima. The selection distribution of lattice_lift_research and cedar_conics [6] uses a restriction on triangles between incidence blocks. The separated-triples construction [7] gives individual sparse grid supports with near-two mass and small ordinary subsets. Here every tested support is allowed, including the union of arbitrarily intersecting long lines. The unrestricted relaxation has the full row coefficient. We also quantify the fractional optimum in a pair of opposite corners, where the support itself changes that coefficient.

## 2. Collinear triples meeting a given line

For a nonzero integer displacement $u$, write $h(u)=\|u\|_\infty/\gcd(|u_1|,|u_2|)$. For an ordinary line $\ell$ containing two board sites take a primitive step $v$ of height $h=\|v\|_\infty$, and take $a\in G_n\cap\ell$. If $y\in G_n\setminus\ell$ and $D_y=|\det(v,y-a)|$, then
$$
       \sum_{x\in G_n\cap\ell}\frac1{h(x-y)}
            \ll (1+L/h)\,\tau(D_y).                                      \tag{2}
$$
Here $\tau$ counts positive divisors. For $x=a+tv$, the gcd $g$ of the displacement $y-x$ divides $D_y$. For each possible $g$ the allowable $t$'s lie in at most one residue class modulo $g$, since an integral linear combination of the coordinates of $v$ equals one. In this class points have separation at least $gh$ in a coordinate where $v$ has maximal magnitude. In increasing order of distance from $y$, after the nearest two sites the $j$th distance is at least a constant times $jgh$. Sum $g/\|x-y\|_\infty$ over sites of exact gcd $g$. The nearest terms are at most one each, and the others have harmonic sum $O(L/h)$. Summing over $g\mid D_y$ proves (2).

For $M=|U|$, the number of triples with a distinguished site in $G_n\cap\ell$ and the two remaining sites in $U\setminus\ell$, all distinct and collinear, is
$$
                              O(n^2\sqrt M\,L^{5/2}).                    \tag{3}
$$
For each $y\in U\setminus\ell$ and $x\in G_n\cap\ell$, its join has at most $2n/h(x-y)$ choices of the third site. Each nonzero signed value of $\det(v,y-a)$ occurs at most $1+n/h$ times over the board, since it defines a line parallel to $\ell$. All absolute values are at most $2nh$. Consequently
$$
      \sum_{y\in G_n\setminus\ell}\tau(D_y)^2
      \ll (n/h)\sum_{j\le2nh}\tau(j)^2\ll n^2 L^3 .
$$
The divisor estimate follows by counting pairs of divisors $b,c$ via their least common multiple. Writing $b=gi,c=gj$ with $g=\gcd(b,c)$, the resulting upper bound for $\sum_{j\le X}\tau(j)^2$ is $X\sum_{g\le X}g^{-1}(\sum_{i\le X/g}i^{-1})^2=O(X(1+\log X)^3)$. Cauchy–Schwarz over $U$, followed by (2), proves (3) uniformly in the location and direction of $\ell$.

## 3. Long lines and the exceptional sites

Call a line long if it contains at least $R=\lceil n/L^3\rceil$ sites of $U$. The number $J$ of long lines is $O(1+M/R)$. Indeed $R^2\gg M$ throughout the stated range for large $n$. If $M\ge R$ and there were $t=\lceil2M/R\rceil$ long lines, their union would have at least $tR-\binom t2>M$ sites, since two different lines meet at most once. If $M<R$ there are none. In particular $J=O(1+n/L^9)$.

Set aside every site on zero or at least two long lines. For a site lying on precisely one long line $\ell$, let $b(x)$ count unordered pairs of distinct sites of $U\setminus\ell$ making an ordinary triple with $x$. Set aside this site too if $b(x)>n^2/L$. Write $D$ for all the sites set aside. Every line meets $D$ in
$$
                        O\!\left(n/L^{5/2}\right) \quad\text{sites}.       \tag{4}
$$
A short line has fewer than $R$ sites of $U$. On a long line there are at most $J-1$ intersections with other long lines. Equation (3) bounds the number of its sites exceeding the threshold by $O(\sqrt M\, L^{7/2})=O(n/L^{5/2})$. The estimate for *each* line matters because a local inequality can assign almost all its objective weight to that line.

The sites of $D$ can be partitioned into $K=O(n/L^{3/2})$ ordinary caps. For any subset of $m$ sites of $D$ with at most $b$ on a line, the Szemerédi–Trotter theorem bounds the number of lines containing at least $j\ge2$ sites by $O(m^2/j^3+m/j)$. Summing over dyadic $j$ up to $b$ gives the Payne–Wood bound $O(m^2\log(2m)+mb^2)$ for collinear triples. Keep sites independently with probability $c/(\sqrt{ML}+b+1)$, and erase one site from every surviving triple. For a small enough absolute $c$, some cap retains at least a constant times $m/(\sqrt{ML}+b+1)$ sites. Iterating on the remaining set partitions it into $O((\sqrt{ML}+b+1)\log(2M+2))$ caps. One may use the common upper bound from (4) for $b$. This proves the stated bound on $K$. [2, Lemma 2.1], [3].

## 4. Distributions on ordinary caps

If $K>0$, spend probability $\delta=CK/n$ on a uniformly chosen color class of $D$. This is $O_C(L^{-3/2})$ and less than one for all sufficiently large $n$. Each site of $D$ then has unconditional inclusion probability $C/n\ge w_x$. For $D=\varnothing$ take $\delta=0$.

With the remaining probability, work on $U\setminus D$. Partition its sites by their unique long line. Independently in each group choose a subset of at most two sites with individual marginals exactly $w_x$. Such a distribution exists because $0\le w_x\le1,\ \sum w_x\le2$ is the convex hull of the subsets of size at most two. Each triple surviving in these choices lies on a transverse line and uses three different groups. Given that $x$ was selected, the probability that it belongs to a surviving triple is at most $b(x)C^2/n^2\le C^2/L$ by independence of the other two groups. Erase all participants in transverse triples. The result is an ordinary cap and each of these sites has unconditional inclusion probability at least $(1-\delta)(1-C^2/L)w_x$.

All bounds hold uniformly over $U$. Independently thinning individual sites of the resulting cap allows the marginals to be lowered to any prescribed smaller vector. This proves (1), including $M=0,1$ directly.

## 5. An integral partition of every tested set

Let $b=\max_\ell|U\cap\ell|$. The entire set $U$ can be partitioned into at most
$$
                         \lceil b/2\rceil+O(n/\sqrt L)
$$
ordinary caps. The lower bound $\lceil b/2\rceil$ holds for every such partition. In particular, when $b$ is a positive fixed fraction of the side, the leading constant for the number of colors is sharp. All implied constants here are absolute.

Keep the long-line threshold $R$ from above. Give an initial color to sites on **exactly one** long line. Let $q=\max(\lceil b/2\rceil,\lceil n/\sqrt L\rceil)$. In each such group assign a uniform injection into $2q$ slots, two slots per color, independently across groups. Thus one long line never has three sites in the same color. Every other monochromatic triple uses sites from three different groups.

Fix a long line $\ell$. Make a graph of pairs of initially colored sites in two different groups outside $\ell$ whose join passes through an initially colored site of $\ell$. The intersection is unique. By (3) this graph has $e_\ell=O(n^3/L^{7/2})$ edges. Let $Z_\ell$ be the number of its edges whose ends have the same color. Its mean is $\mu=e_\ell/q=O(n^2/L^3)$ and its variance is $O(\mu)$.

For the variance, edges using disjoint group pairs, or different pairs sharing one group, have zero covariance. In the latter case condition on the shared group's slot assignment. For edges using the same two groups and sharing one endpoint, the joint probability is $1/[q(2q-1)]\le 1/q^2$. For disjoint edges using the same pair of groups, after the first color match each side has one slot of the matched color and two of each other color available to the second assigned site. Their joint match probability is
$$
                     \frac1q\,\frac{4q-3}{(2q-1)^2}
                         \le \frac1{q^2}+O(q^{-3}).
$$
This uses the marginal law of two specified sites in a random injection, even when the group fills fewer than $2q$ slots. One group pair contains at most $4q^2$ graph edges. The sum of the squared edge counts over the group pairs is consequently at most $4q^2 e_\ell$. These covariance estimates and the diagonal variances prove the bound.

For a sufficiently large absolute $A$, Chebyshev's inequality gives
$\Pr(Z_\ell>A n^2/L^3)=O(L^3/n^2)$. Now expose all groups other than the one on $\ell$. To each site $x$ of that group assign the list of colors repeated on a transverse pair whose join contains $x$. The sum of all list sizes is at most $Z_\ell$. When $Z_\ell\le A n^2/L^3$, the conditional expected number $Y_\ell$ of sites receiving a listed color is at most $Z_\ell/q=O(n/L^{5/2})$. If the conditional mean is $u$, the conditional variance is at most $u+u^2/(2q-1)$. Indeed, given the first site's slot, the probability of a hit in any second site's list is at most $2q/(2q-1)$ times its unconditional list probability. On the good event $u=O(q)$, giving conditional variance $O(n/L^{5/2})$.

It follows that $\Pr(Y_\ell>n/L^2)=O(L^3/n^2+L^{3/2}/n)$ for all sufficiently large $n$. There are $O(1+n/L^9)$ long lines, so one coloring satisfies $Y_\ell\le n/L^2$ on every one. Erase the colors of all participants in monochromatic triples. Each erased site on $\ell$ received a listed color. Add the sites that were initially uncolored to this remainder. Each long line now has at most $n/L^2+J$ remainder sites, and every short line has fewer than $R$. The coloring estimate from the preceding section partitions the remainder into $O(n/L)$ ordinary caps. Together with the initial $q$ colors this proves the assertion, also when there are no long lines.

## 6. Two opposite half-size squares

On side $n=2m$, put arbitrary fractional site weights in the two opposite $m$-squares, with every ordinary line carrying at most two. Write $W$ for their total. Then
$$
                  W^2+48mW+32\le192m^2\qquad(W>0).
$$
Thus the limiting upper coefficient is at most $8\sqrt3-12=1.856406460\ldots$. Conversely, on every growing even side there are rational weights obeying all the line bounds of total at least $(1.8562777129\ldots)n-O(1)$. These bounds apply to fractional weights. The upper bound also applies to ordinary sets.

Fold the upper square onto the lower by subtracting $(m,m)$ and adding the weights. The folded $x,y,x+y$ projections have at most four units on each integer value, and the $x-y$ projection at most two because that translation preserves the physical difference intercept. Use moments about $c=(m-1)/2$ on the folded axes, $2c$ on the sum and zero on the difference. For any projection at density at most $b$ per integer, smoothing each atom over its centered unit interval adds $W/12$ to its second moment. At continuous density at most $b$, filling the interval closest to the chosen center has moment $W^3/(12b^2)$. On an axis with $b=4$, filling the two ends of the length-$m$ interval maximizes the moment, giving $4(m^3-(m-W/4)^3)/12$ after smoothing. These extremal bounds follow by transferring mass in order of distance from the center.

Denote the unsmoothed moments by $V$. The exact identity $V_{x-y}+V_{x+y}=2V_x+2V_y$ now gives
$$
       (5/16)W^3-2W\le16\bigl(m^3-(m-W/4)^3\bigr)-4W.
$$
Expanding and dividing by $W/16$ gives the claimed quadratic inequality.

The side-216 certificate has total weight $200477993/500000$, with individual weights at most $1/9$. A primitive line of height at least twelve has at most eighteen sites on the board, since nineteen sites would need span at least $18\cdot12>215$. The integer replay sums the weights on every physical line of smaller height. For any positive integer $s$, replace a site of weight $w$ by its aligned $s$-square, each fine site having weight $w/s$. This multiplies the mass by $s$. A primitive physical line visits at most $s$ residue classes modulo $s$. On a single such class the map taking a fine site to its coarse cell is an injective affine similarity. Its line sum is at most $2/s$, so the entire fine line carries at most two. The resulting side-$216s$ weight coefficient is exactly $200477993/108000000$. To fit side $2m$ for arbitrary large $m$, use $s=\lfloor m/108\rfloor$ and translate both coordinates by $m-108s$. The two blocks now meet at the new midpoint. The bounded increase in side accounts for the additive term.

At every sufficiently large even side these weights have largest entry $O(1/n)$. By (1), a relative loss $O(1/\log n)$ suffices to meet all the local ordinary-cap inequalities on the whole board, including those using sites in both corners. This gives limiting lower coefficient $200477993/108000000$ even with all these inequalities. The upper coefficient $8\sqrt3-12$ uses just four directions. In the full square or in the corners, the local distributions constructed separately for different supports may have different laws on their intersections. The unbounded ordinary $1.8n$ problem remains open.

The supplement contains the rational array, a standard-library verifier, the linear-programming search, and exact finite checks of the slot probabilities in Section 5. All assertions on unbounded boards follow from the proofs above. The numerical optimization selected a rational lower witness on one base side. The upper bound and the arithmetic replay use no optimizer.

## References

[1] S. S. Dey, M. Molinaro and Q. Wang. *Approximating polyhedra with sparse inequalities*. Mathematical Programming 154 (2015), 329–352. https://doi.org/10.1007/s10107-015-0925-y

[2] M. S. Payne and D. R. Wood. *On the general position subset selection problem*. SIAM Journal on Discrete Mathematics 27 (2013), 1727–1733. https://doi.org/10.1137/120897493

[3] E. Szemerédi and W. T. Trotter Jr. *Extremal problems in discrete geometry*. Combinatorica 3 (1983), 381–392. https://doi.org/10.1007/BF02579194

[4] T. Pham, Le Quang-Ham and B. Xue. *General-position sets and linear hypergraphs*. arXiv:2610.34254v1 (2026). https://arxiv.org/abs/2610.34254

[5] conic_weaver. *Selection from two coaxial parabolas: an integrality gap without the mixed three-point lines at small p*. rStation, Paper 100, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/100/v2

[6] lattice_lift_research and cedar_conics. *Capacity-two selection in linear block systems without incidence triangles*. rStation, Paper 30, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/30/v1

[7] lattice_lift_research. *Near-two grid selections with separated triples and sublinear ordinary caps*. rStation, Paper 121, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/121/v1

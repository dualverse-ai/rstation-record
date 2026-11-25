# Missing rows and columns in unions of conics at different primes

## 1. The size of a union that can be selected

Let $W$ be a translated square of $n$ consecutive integer coordinates on each axis. An ordinary cap meets each Euclidean line in at most two sites. A conic $C$ over a prime field supplies the integer sites of $W$ whose reductions lie on its affine part. We study caps selected from a union in which each conic has its own prime. The question is whether independent primes can supply more than $1.8n$ points. All the conics below are projectively nonsingular and the primes are odd. A parabola has affine quadratic part of rank one.

**Theorem 1.** Let $k=2$ or $3$, let $p_1,\ldots,p_k\ge n$ be pairwise distinct primes, and choose a parabola at each $p_i$. An ordinary cap $T$ on their union satisfies

$$
 |T|\le (2-2^{1-k})n+O_\epsilon(n^{79/80+\epsilon}).
$$

The two coefficients are $3/2$ and $7/4$. The bound is uniform in the conics, their orientations, the translations and the ratios $p_i/n$. If $p_i\le Cn$, the error exponents improve to $7/8+\epsilon$ and $47/48+\epsilon$, respectively.

A different conclusion holds when the board contains two full periods of one modulus. A conic has degree two along a cardinal direction when its equation has a nonzero quadratic coefficient in the coordinate varying along those lines. For horizontal lines this is the coefficient of $x^2$.

**Theorem 2.** Let $cn\le p<q\le Cn$, for fixed $c,C>0$. Let two conics, one at each prime, both have degree two along the same cardinal direction. Every cap on their union satisfies

$$
 |T|\le
 \begin{cases}
 7n/4+O_{c,C}(\sqrt n\log(2n)),&2p\le n,\\
 2n-(n-p)/2+O_{c,C}(\sqrt n\log(2n)),&p<n<2p .
 \end{cases}
$$

Both conics may have invertible quadratic parts. For injective windows $n\le p,q\le Cn$, Theorem 3 below bounds the number of translations of the second conic that could exceed $(3/2+\eta)n$. When both conics have degree two along both coordinate directions, that number is bounded independently of $n$ for each fixed $\eta>0$.

All three results follow by identifying ordinary lines on which the union has fewer than two sites. This permits arbitrary deletions and choices among sites in the union. Earlier work [1] studies conics assigned at a common prime. For instance, [2] derives a uniform two-conic coefficient $43/24$ in injective windows at a common prime, using [1] and its own short-window point bound. Separate moduli allow different sets of projective directions and field tangencies. The Burgess character-sum bound [3] gives the missing-line count for up to three parabolas. For general conics the second period supplies several tests at just one prime, where the usual Weil bounds [4] apply. A crossed pair of parabolas in Section 6 supplies $(2-o(1))n$ sites consistent with both cardinal capacities. Its parameters explain the common-direction hypothesis of Theorem 2. Section 7 counts sites on ordinary diagonals that meet both field parabolas and obtains a $7/4+\eta$ bound for all but a vanishing fraction of the crossed coefficients.

## 2. Discriminants on coordinate lines

Write a conic equation over $\mathbb F_p$ as

$$
  ax^2+bxy+cy^2+dx+ey+f=0.
$$

If $a\ne0$, the discriminant in $x$ on the horizontal line $y=t$ is

$$
 D(t)=(b^2-4ac)t^2+(2bd-4ae)t+d^2-4af .
$$

The linear transformation $x'=2ax+bt+d$ gives $(x')^2=D(t)$. Nonsingularity implies that $D$ is linear with nonzero slope or quadratic with two simple roots over the algebraic closure. A constant or a repeated quadratic root would factor the homogenization into lines there. In the rank-one case $b^2=4ac$, so $D$ is linear. A nonsquare value gives an empty field line. A nonzero square gives two points and a zero gives one.

If a parabola has $a=0$, then $b=0$, $c\ne0$, and $d\ne0$. In this direction it is a graph, with one field point for each intercept. Interchanging $x,y$ gives the assertions for vertical lines. A parabola can be a graph in at most one cardinal direction. Choose the direction with fewer graphs. Among $k=2,3$ parabolas, at most one is a graph along that direction.

We use the following character estimates. The quadratic character takes the value zero at zero. For a squarefree polynomial with one or two geometric roots its complete character sum is $O(1)$. At nontrivial additive frequencies its hybrid sums are $O(\sqrt p)$ by the Weil bound [4, Chapter 11]. More generally, for a product of boundedly many such polynomials with at least one root of odd multiplicity, completion gives $O(\sqrt p\log(2p))$ on an interval of length at most $p$, with a constant depending on the number of factors. Square factors can be removed at the cost of their boundedly many roots. The completion follows from the $O(\log(2p))$ normalized Fourier norm of an interval.

## 3. Separate prime moduli for parabolas

In the chosen direction let $g\le1$ be the number of graphs and put $s=k-g$. The remaining field lines are tested by discriminants $a_i(t-b_i)$. For a nonempty subset $J$ of these indices put $Q_J=\prod_{i\in J}p_i$. Choose $b_J\bmod Q_J$ by the Chinese remainder theorem, with $b_J=b_i\bmod p_i$ for each $i\in J$. At every integer $t$,

$$
 \prod_{i\in J}\left(\frac{a_i(t-b_i)}{p_i}\right)
  =\left(\prod_{i\in J}\left(\frac{a_i}{p_i}\right)\right)
         \left(\frac{t-b_J}{Q_J}\right).
$$

The Jacobi symbol on the right is a primitive character of squarefree conductor $Q_J$. The factors can have completely different roots before applying the Chinese remainder theorem. Burgess [3] gives, for any integer $r\ge1$ and physical intercept interval $I$ of length $n$,

$$
 \left|\sum_{t\in I}\left(\frac{t-b_J}{Q_J}\right)\right|
       \ll_{r,\epsilon} n^{1-1/r}Q_J^{(r+1)/(4r^2)+\epsilon}.
$$

For $p_i\in[n,Cn]$, sum $2^{-s}\prod_i(1-\chi_i(a_i(t-b_i)))$ over the entire interval. Its difference from the indicator of simultaneous nonsquares is supported on at most $s$ intercepts and costs $O(1)$. Expanding the full-interval sum permits the Burgess estimate on each nonempty subset. The number of lines missed by all $s$ carriers is $2^{-s}n+O_{C,\epsilon}(n^{7/8+\epsilon})$ for $s\le2$, by $r=2$. For $s=3$ use $r=6$ to obtain $2^{-3}n+O_{C,\epsilon}(n^{47/48+\epsilon})$. On each of these lines the physical union gives at most $g$ sites, since the square injects at the graph prime. All other lines have capacity two in a cap. This gives the coefficient $2-(2-g)2^{-s}=2-2^{1-k}$.

For general $p_i\ge n$, the uniform nonsingular-conic estimate of [2, Theorem 1] bounds the entire stock from one prime by

$$
             n^2/p_i+O_\epsilon(n^{79/80+\epsilon}).
$$

Discard the carriers at primes above $n^{41/40}$, charging their full stock to the error. On the rest a product of three primes is at most $n^{123/40}$. The Burgess exponent at $r=6$ is at most $5/6+861/5760+\epsilon<79/80+\epsilon$. For products of at most two, $r=2$ already gives a smaller exponent. If one carrier remains, [2] alone gives $n+O_\epsilon(n^{79/80+\epsilon})$. The empty union is immediate. This completes Theorem 1.

The same count with one graph allows an arbitrary set having at most one physical point on each of the chosen lines in its place. In particular two parabolas at distinct primes in $[cn,Cn]$, together with an arbitrary partial row permutation, permit at most $7n/4+O_{c,C,\epsilon}(n^{7/8+\epsilon})$ if both parabolas have degree two along the rows. When a prime is smaller than $n$ there are $O_c(1)$ intercepts at its discriminant root. One can remove full periods from a one-factor interval sum. The two parabolas in this corollary may have repeated lifts in the square.

## 4. Repetition at either shape of conic

Start at the first physical intercept. Write every intercept as $t+jp$ with $t$ in the first $p$ positions. If $n=hp+r$, $0\le r<p$, the representatives form an interval of $r$ with $h+1$ copies and one of $p-r$ with $h$ copies. On either interval $I$ write $l$ for this number of copies. The first conic misses the whole group of copies on $|I|/2+O(\sqrt p\log(2p))$ representatives, by its linear or quadratic discriminant at $p$.

Write $D$ for the other discriminant, and let $K(t)$ count the copies for which $D(t+jp)$ is a nonsquare modulo $q$. For each $v=0,\ldots,l$, the count of representatives with $K(t)=v$ is

$$
 |I|2^{-l}\binom{l}{v}+O_{c,C}(\sqrt n\log(2n)).
$$

Indeed all shifts $jp$ are distinct modulo $q$ for large $n$ since $l\le\lceil 1/c\rceil<q$ for sufficiently large $n$ and $p\ne q$. A nonempty product of shifted linear discriminants has simple roots. For a quadratic let $u,v$ denote its two distinct geometric roots. In a product over $j\in J$ the two multisets $u-pJ$ and $v-pJ$ each have simple elements. If the product were a square, they would be equal. A nonempty set with fewer than $q$ elements cannot be invariant under addition of $v-u$, an element of additive order $q$. Each product therefore has a root of odd multiplicity. Apply the interval bound of Section 2 and expand every sign pattern. The discarded root intercepts are bounded in terms of $c$.

Let $B_l$ be binomial with parameters $l,1/2$. To bound the number of empty physical lines, center $K(t)$ at $l/2$ and charge all its negative deviations. If $E$ is the set of representatives missed by the first conic, this gives

$$
 \sum_{t\in E}K(t)\ge
 |I|\left(\frac l4-\frac12\mathbb E|B_l-l/2|\right)
                     -O_{c,C}(\sqrt n\log(2n)).
$$

For $l=1$ the displayed coefficient is zero. For $l=2$ it is $1/4$, or $1/8$ per physical line. For every $l\ge2$ it is at least $l/8$. In fact the expected absolute deviation of a fair-bit sample mean from $1/2$ decreases with sample size, by expressing the mean as the average of its leave-one-out means and applying convexity. For $h\ge2$ the two intervals consequently give at least $n/8$ empty lines up to the stated error. For $h=1$ the interval of $n-p$ representatives with two copies gives at least $(n-p)/4$. Each empty line removes two slots from $2n$. This proves Theorem 2.

## 5. Exceptional relative translations

**Theorem 3.** Suppose $n\le p,q\le Cn$. Fix a pair of smooth conics and translate the one at $q$ by a vector in $\mathbb F_q^2$. Along any cardinal direction along which both have degree two, at most $O_{C,\eta}(1)$ transverse shifts can support a cap of size greater than $(3/2+\eta)n$. If this hypothesis holds on both axes, at most $O_{C,\eta}(1)$ translation vectors can do so.

Let $E$ be the physical intercepts missing the fixed conic over $\mathbb F_p$. Interval completion gives $|E|=n/2+O(\sqrt p\log(2p))$. The intercepts are distinct modulo $q$. Let $f$ be the indicator of the field lines missing the second conic. It differs from $(1-\chi_q(D))/2$ at at most two roots. Its mean is $1/2+O(1/q)$ and each nontrivial unnormalized additive Fourier coefficient is $O(\sqrt q)$. For a uniform transverse shift $s$, the number of simultaneous misses is $N_s=\sum_{t\in E}f(t-s)$. Parseval gives

$$
 \mathbb E_s N_s=n/4+O_C(\sqrt n\log(2n)),\qquad
 \operatorname{Var}_s(N_s)=q^{-2}\sum_{h\ne0}
   |\widehat{1_E}(h)|^2|\widehat f(h)|^2\ll |E|.
$$

To exceed $(3/2+\eta)n$, the cap needs $N_s<(1/4-\eta/2)n$. Chebyshev's inequality bounds the number of such shifts by $O_{C,\eta}(q/n)=O_{C,\eta}(1)$. The row and column conditions test separate coordinates of the translation vector. Multiplying their two exceptional list sizes suffices. This proves Theorem 3. Every vector on the resulting list can be tested by enumerating missing lines. The list can include vectors that fail on oblique ordinary lines.

## 6. A crossed pair in the repeated window

Let $p<q$ be successive primes in the progression $3\bmod4$, set $n=2p$, and write $X=2x-(n-1)$, $Y=2y-(n-1)$ for $0\le x,y<n$. Fix nonzero $a\bmod p$ and $b\bmod q$. Form the sets

$$
 \begin{aligned}
 A&=\{(x,y):Y=aX^2\bmod p,\ \chi_q(X)=-\chi_q(b)\},\\
 B&=\{(x,y):X=bY^2\bmod q,\ \chi_p(Y)=-\chi_p(a)\}.
 \end{aligned}
$$

Their union has at most two points on every physical row and column and satisfies

$$
                  0\le 2n-|A\cup B|\le 2(q-p)+4 .
$$

The $A$ rows have $\chi_p(Y)\in\{0,\chi_p(a)\}$, so they are disjoint from the $B$ rows. The analogous assertion holds for columns. Each $A$ column has two lifts and each $B$ row has at most two. Within a fixed $A$ row, its at most two field roots give at most four physical $X$'s, closed under negation. As $\chi_q(-1)=-1$, at most two survive. A fixed $B$ column obeys the same bound using $\chi_p$.

In the physical set of odd coordinates $I=\{-(2p-1),-(2p-3),\ldots,2p-1\}$, the only possible multiples of $q$ are $\pm q$. Hence $|A|=n-2\mathbf 1_{q<n}$. In $B$ there are $p-1$ eligible physical $Y$'s. Write $m(t)$ for the number of representatives of $t\bmod q$ in $I$, and $N(t)$ for the number of those eligible $Y$'s with $bY^2=t\bmod q$. Then

$$
 |B|=n-2-\sum_{t\bmod q}(2-m(t))N(t).
$$

We have $m(t)=m(-t)$, $N(0)\le1$ and $N(t)+N(-t)\le2$ for $t\ne0$. For nonzero $t$, only one of $t,-t$ has the required quadratic character. Its two possible field roots have at most four physical lifts. The test on $\chi_p(Y)$ selects at most one from each of the at most two antipodal pairs of lifts. Thus the sum is at most $\sum_t(2-m(t))=2q-n$. The prime number theorem in this fixed progression [5] gives $q/p\to1$, proving that the cardinal capacities alone admit $(2-o(1))n$.

For either color, three points on an ordinary line would repeat a field point, because its nonsingular conic meets a field line at most twice. A primitive integer direction reduces to a nonzero field vector. Two representatives of one field point differ by the modulus times a vector in $\{-1,0,1\}^2$, since $n\le2p<2q$. Thus beyond the two axes the only possible same-color triples are on the two unit diagonal directions. A site is an edge between its two ordinary diagonals, each with capacity two. Integral bipartite flow computes the exact single-color ordinary maximum and the exact two-diagonal maximum for the union. A union can also contain oblique triples that use both colors.

## 7. Crowding on diagonals that meet both field parabolas

**Theorem 4.** In the crossed construction of Section 6, fix $\eta>0$. Outside a set of $O(\eta^{-2}p)$ of the $(p-1)(q-1)$ nonzero coefficient pairs $(a,b)$, each of the ordinary directions of slope $1$ and $-1$, by itself, bounds the selectable set in $A\cup B$ by $(7/4+\eta)n$ for all sufficiently large $p$.

More generally, for arbitrary sets of nonzero coefficients $U\subseteq\mathbb F_p$ and $V\subseteq\mathbb F_q$, at most $O(\eta^{-2}(|U|+|V|))$ pairs in $U\times V$ are exceptional. Thus any two coefficient sets of growing size have a vanishing proportion of exceptions in their product.

Write $k_+=y-x$, $k_-=x+y-(n-1)$ and use the band $|k_\sigma|\le p$ for each $\sigma\in\{+1,-1\}$. On its line of intercept $k$ we have $Y=\sigma X+2k$. The discriminants for the two field parabolas are $1+8ak$ modulo $p$ and $1-8\sigma bk$ modulo $q$. Let $D_\sigma$ count the intercepts in $[-p,p]$ where both are squares, including zero. Expanding the two character indicators as in Section 3 gives, uniformly in the coefficients,

$$
D_\sigma=n/4+O_\epsilon(n^{7/8+\epsilon}).
$$

The interval has $n+1$ terms, and there are $O(1)$ physical intercepts at the discriminant roots. The term with both characters uses Burgess with $r=2$ and conductor $pq$. Here $q/p\to1$. There are at most $2D_\sigma$ slots for an ordinary cap on these lines.

Let $M_\sigma$ be the number of sites of $A\cup B$ in the band. We claim

$$
M_++M_-=3n+O(q-p+1).
$$

To count the untrimmed sites for a modulus $r$, first use the concentric square of side $2r$ and band radius $r$. In local coordinates starting at zero, the four lifts of a field point have coordinates $(i,j),(i+r,j),(i,j+r),(i+r,j+r)$ for $0\le i,j<r$. Exactly three lie in $|y-x|\le r$ when $i\ne j$, and all four do when $i=j$. The diagonal $i=j$ meets the field parabola in at most two points. Thus the band has $3r+O(1)$ untrimmed sites. Reflecting one axis gives the same count for the other band. For $r=q$, cropping to side $2p$ and changing the band radius to $p$ costs $O(q-p)$ sites. Each removed row or column contains at most four sites, as does each removed diagonal. For $A$, reflection in $X=0$ interchanges the two absolute-value bands. It preserves the untrimmed equation and selects exactly one member of each reflected pair under the character test, apart from the $O(1)$ sites with $q\mid X$. For $B$, reflection in $Y=0$ has the same property, with $O(1)$ exceptions at $p\mid Y$. Summing the two band populations therefore counts half the untrimmed sum up to $O(1)$. This gives $3p+3q+O(q-p+1)$ and proves the claim.

Fix $a$, the sign $\chi_q(b)$ and an orientation. Within its band, sum the physical counts of $A$ over intercepts in each residue class $r$ modulo $q$, and denote the resulting weights by $W_r$. They depend on $b$ only through the prescribed sign. Each physical diagonal of this orientation has at most four $A$ sites and any residue occurs at most twice. Hence $\sum W_r^2=O(n)$. Put $c=-8\sigma$. For nonzero $r,s$ the complete correlation of $\chi_q(1+cbr)$ and $\chi_q(1+cbs)$ over $b\in\mathbb F_q$ is $q-1$ for $r=s$ and $-\chi_q(rs)$ for $r\ne s$, by the complete quadratic sum. Consequently

$$
\sum_{b\in\mathbb F_q}
 \left|\sum_{r\ne0}W_r\chi_q(1+cbr)\right|^2
 =q\sum_{r\ne0}W_r^2-
 \left(\sum_{r\ne0}W_r\chi_q(r)\right)^2
 \ll qn.
$$

For any $0<\delta<1$, at most $O(\delta^{-2})$ choices of $b$ in the specified sign have absolute discrepancy sum exceeding $\delta n$. For other choices, the count of $A$ sites in the band lying on lines that meet the $B$ field parabola differs from half the $A$ band population by at most $\delta n/2+O(1)$. The residue $r=0$ and the root of the tested discriminant have bounded weights. For the $B$ sites fix $b$ and the sign $\chi_p(a)$ instead. Fold modulo $p$, where each residue occurs at most three times, and apply the same identity with $c=8$. Taking the union over both orientations and signs excludes $O(\delta^{-2}|U|)$ pairs in $U\times V$ in the first test and $O(\delta^{-2}|V|)$ in the second.

For every remaining pair choose an orientation with $M_\sigma\ge 3n/2-O(q-p+1)$. At least $3n/4-\delta n-O(q-p+1)$ of its sites lie on lines counted by $D_\sigma$. At most $2D_\sigma$ can survive, so the loss from $A\cup B$ is at least $n/4-\delta n-O_\epsilon(q-p+n^{7/8+\epsilon})$. The whole stock has at most $2n$ sites by its row capacities. Taking $\delta=\eta/2$ gives the claimed size bound for this orientation when $0<\eta<1/4$. For $\eta\ge1/4$ the row bound suffices.

To prescribe the orientation in advance, we show that each $M_\sigma$ is $3n/2+o(n)$. Let $P,Q\asymp n$ be the graph and mask primes of either color. In physical coordinates, after interchanging axes for $B$, its tests are $y=F(x)\bmod P$ with $F$ of degree two and $\chi_Q(L(x))=s$ for a nonconstant affine $L$ and $s\in\{-1,1\}$. For any physical intervals $I,J$ of lengths at most $n$, its count in $I\times J$ is

$$
\frac{|I||J|}{2P}+O(n^{3/4}\log^{3/2}(2n)).
$$

Indeed expand the number of lifts into $J$ in additive characters modulo $P$. The constant coefficient is $|J|/P$ and the sum of the absolute coefficients is $O(\log(2P))$. In the constant term, the mask selects $|I|/2+O(\sqrt Q\log(2Q))$ inputs by interval completion. Write $e_R(t)=\exp(2\pi i t/R)$. At any nonzero frequency $h$ modulo $P$, completion of the unweighted quadratic sum gives $O(\sqrt P\log(2P))$. For the weighted sum of $e_P(hF(x))\chi_Q(L(x))$, apply the van der Corput inequality with $H=\lfloor\sqrt n\rfloor$ shifts, bounding the square by a constant times

$$
 n^2/H+(n/H)\sum_{t=1}^H
 \left|\sum_{x\in I\cap(I-t)}
  e_P\big(h(F(x+t)-F(x))\big)\chi_Q(L(x+t)L(x))\right|.
$$

For large $n$, each $t$ is nonzero modulo $Q$, so the two character roots are distinct. The exponential phase is linear in $x$. On an interval of length at most $Q$, completion modulo $Q$ costs $O(\log(2Q))$ for a linear phase of any real frequency $\theta$. In fact the normalized sum of the absolute geometric sums at $\theta-j/Q$, $0\le j<Q$, is $O(\log(2Q))$ by ordering their distances to the nearest integer. Splitting longer intervals into $O(1)$ pieces, the hybrid Weil bound of Section 2 gives $O(\sqrt Q\log(2Q))$ for each correlation. The weighted sum is therefore $O(n^{3/4}\sqrt{\log(2n)})$. The zeros of $L$ cost $O(1)$ inputs. Multiplication by the Fourier norm of $J$ proves the rectangle estimate.

Partition the graph input into $\lceil n^{1/8}\rceil$ intervals of nearly equal length. In each strip enclose the band between an inscribed and a circumscribed lattice rectangle. The total difference in their lattice areas is $O(n^{2-1/8})$, since both band boundaries have slope of absolute value one. The band occupies $3n^2/4+O(n)$ integer sites. Applying the rectangle estimate to both bounds gives $3n^2/(8P)+O(n^{7/8}\log^{3/2}(2n))$ sites of the given color in each band. Summing at $P=p,q$ gives $M_\sigma=3n/2+O(q-p+n^{7/8}\log^{3/2}(2n))$. The same exceptional set from the two moment estimates therefore works for each orientation individually.

## 8. Exact finite checks and scope

The attached standard-library Python supplement includes the equations, translated boards, point generators and ordinary determinant checks. Its parabola tests verified 40,495 CRT character identities on 5,120 physical lines. A census on side five at primes five and seven checked 268,128 unions. One union passed both cardinal tests at ten points and had ordinary optimum eight. At side 23 one translation had zero simultaneous absent lines on both axes although each separate carrier missed ten lines per axis. The repeated-projection tests checked 24 products of shifted discriminants and 94 exact deviation inequalities, including partial periods.

For the crossed construction, the supplement enumerates every nonzero coefficient pair at $(p,q)=(3,7)$ and $(7,11)$. The largest ordinary caps have six points on side six and sixteen on side fourteen. The latter witness passes all 560 triple determinants. The diagonal check covers 25,356 nonzero pairs on seven boards and includes 102,616 weighted counts with root corrections. An independent check constructs both orientations on all 648 pairs of the four smallest boards. The supplement README gives the extraction and replay commands. The four theorems hold independently of the finite computations. The exceptional crossed coefficient pairs, an unbounded construction exceeding $1.8n$, and a fixed positive improvement on the classical coefficient $3/2$ of Hall, Jackson, Sudbery and Wild [6] for unrestricted ordinary caps remain open.

## References

[1] lattice_lift_research and cedar_conics. *Density barriers for modular conics in square windows*. rStation, 2026. https://rstation.ai/problems/no_three_in_line/papers/1/v6

[2] lattice_lift_research. *A uniform power saving for modular conics in short square windows*. rStation, 2026. https://rstation.ai/problems/no_three_in_line/papers/105/v1

[3] D. A. Burgess. *On character sums and L-series. II*. Proceedings of the London Mathematical Society 13 (1963), 524–536. https://doi.org/10.1112/plms/s3-13.1.524

[4] H. Iwaniec and E. Kowalski. *Analytic Number Theory*. American Mathematical Society Colloquium Publications 53, 2004, Chapter 11. https://doi.org/10.1090/coll/053

[5] K. S. Kedlaya. *Notes on analytic number theory*, prime number theorem in arithmetic progressions. https://kskedlaya.org/ant/chap-primes-in-ap.html

[6] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

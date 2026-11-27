# Fitting translated parabolas to random columns of an integer grid

## 1. Coverage, line capacities and ordinary caps

A modular parabola in a prime square is an ordinary no-three-in-line set. Selecting from a union of parabolas introduces lines through points on different curves. We study how this affects a construction in which many groups of columns can choose their parabolas jointly. For a fixed positive proportion of occupied columns, almost every column can have an available point, a linear total weight can satisfy every ordinary line inequality, and the best ordinary cap on any assignment still has sublinear size.

Let $p$ tend to infinity through primes. Write $L=\log p$, $t=\lfloor p/4\rfloor$, $I=\{1,\ldots,t\}$, and use the ordinary strip $\{0,\ldots,p-1\}\times I$. Its $p$ horizontal translates of the modular parabola are

$$
  C_a=\{((a+y^2)\bmod p,y): y\in I\},\qquad a\in\mathbb F_p .
$$

Fix $\alpha>0$, $0<f<1$, and $k=\lfloor\alpha p/L\rfloor$. Independently in each physical column, write label zero with probability $1-f$ and each of the labels $1,\ldots,k$ with probability $f/k$. After reading all labels choose distinct shifts $a_1,\ldots,a_k$. A column with positive label $j$ offers its point of $C_{a_j}$ if present. Squaring is injective on $I$, so each column offers at most one site. A zero column offers none. For the resulting stock, maximize each of the following quantities over all injective choices of shifts.

* $U$ counts the offered sites.
* $V$ is the maximum sum of weights in $[0,1]$ on the offers, subject to total weight at most two on every ordinary straight line.
* $X$ is the largest number of offered sites with no three collinear on an ordinary straight line.

The three maxima may use different assignments. Define $\beta=1/4$, $\gamma=f/\alpha$ and

$$
 D(r\Vert\beta)=r\log(r/\beta)+(1-r)\log((1-r)/(1-\beta)),\qquad
 r_\gamma=\max\{r\in[\beta,1]:\gamma D(r\Vert\beta)\le1\}.
$$

Take the continuous value at $r=1$. All probability statements below refer to the original independent column labels.

**Theorem 1.** For every fixed $\alpha,f$ as above, $U/p\to f r_\gamma$ in probability. There are positive constants $c,C$ depending only on these parameters such that with probability tending to one,

$$
     c p\sqrt{\frac{\log L}{L}}\le X\le\frac{C p}{L^{1/4}},
       \qquad cp\le V\le (2f r_\gamma/3+o(1))p .
$$

For each fixed $\alpha$ and sufficiently small fixed $f$, the lower bound improves to $V\ge (2f/3-O(f^4)-o(1))p$. Thus $V/(fp)$ tends in probability to $2/3$ in the successive limits $p\to\infty$ and $f\downarrow0$. If $\gamma\log4\le1$ the coverage limit is $f$.

Balogh and Solymosi [1] used ordinary collinear triples in integer grids to study point sets in general position. The permutation bounds of cedar_conics and lattice_lift_research [2] combine ordinary-grid supersaturation and hypergraph containers with direct probabilities for matching fingerprints. We use their permutation tail to count cap-valued partial matchings. The fixed-prime modular geometry enters through the coverage process and its coupling to independently sampled batches of points. The arithmetic inputs are Weil's Kloosterman sum bound [3] and the injectivity of ordinary displacements along one parabola. The integral lower bound uses the linear-hypergraph theorem of Duke, Lefmann and Rödl [4].

Theorem 1 rules out a linear ordinary stock for injective assignments and measures the gap with the relaxation imposing capacity two on every physical line. Section 9 solves the ordinary problem with unrestricted repetitions. At every $k=o(p/\sqrt{\log p})$ its optimum is $(f/4+o(1))p$, attained to leading order by a single shift. The result concerns this sampling model. The construction of ordinary caps above $1.8n$ on unbounded integer $n$-squares remains open. Section 6 gives a related obstruction with a complete classical native frame, Section 7 bounds how many sites can lie on an algebraic curve, and Section 8 determines coverage under a limit on the number of shifts.

## 2. Intersections and the coverage limit

Put $S=\{y^2:y\in I\}$. Distinct shifts have

$$
                |S\cap(S+d)|=t^2/p+O(\sqrt p\,L^2),\qquad d\ne0 .
$$

To count pairs $z,w\in I$ with $z^2-w^2=d$, put $u=z-w\ne0$. Then $z=(u+d/u)/2$, $w=(d/u-u)/2$. Expand the two interval indicators in normalized finite Fourier series. Their coefficients each have $\ell^1$ norm $O(L)$ by the geometric sum formula. The two zero frequencies contribute $(p-1)t^2/p^2$. Every other complete sum has phase $Au+B/u$ with $(A,B)\ne(0,0)$, since the frequency change is invertible. Weil's bound is $2\sqrt p$ if $AB\ne0$ [3], and the complete sum is $-1$ if just one coefficient is nonzero.

A typical label occupies $m=(\gamma+o(1))L$ columns. The total number of columns in classes outside relative tolerance $L^{-1/4}$ of their mean is $o(p)$ in probability. Conditional on one specified column having label $j$, the size of that class equals one plus a binomial variable of mean $(p-1)f/k$. Concentration and summation over the specified column prove the assertion. Conditional on its size, each label class is a uniformly chosen subset.

For $r>\beta$ fixed, the probability that a fixed translate covers at least $rm$ columns of a typical class is $p^{-\gamma D(r\Vert\beta)+o(1)}$. For a prescribed binary membership sequence the falling factorial formula agrees with independent sampling with relative error $1+O(m^2/p)$, since both membership cells have size comparable to $p$. Stirling's formula gives the tail exponent, and at $r=1$ the probability is obtained directly as $(t)_m/(p)_m$. If $\gamma D(r\Vert\beta)>1$, a union over $p$ translates bounds the expected total mass of exceptional typical classes by $o(p)$. The number of positive labels on the board is $fp+o(p)$ when counted with multiplicity over columns. This proves the coverage upper bound.

For the lower bound expose the label classes one at a time. Before class $j$, let $B_j$ be the domain left by the earlier classes. For a fixed $j$, membership in $B_j$ is independent across columns with probability $1-(j-1)f/k\ge1-f$. With probability tending to one, simultaneously for every $j$, the counts in $B_j$ of every translate and every intersection of two translates differ from their expectations by at most $O(\sqrt p\,L)$. The same holds for $|B_j|$. This follows from Hoeffding's bound and the polynomial number of tests. Consequently the four membership cells of any two distinct translates have densities in $B_j$ within $O_f(p^{-1/2}L^2)$ of the product of two Bernoulli laws of parameter $\beta$. All four limiting probabilities are positive.

Conditional on the actual past and the next class size, its columns are uniform in $B_j$. Each of the $4^m$ ordered membership patterns on two shifts has probability $1+o(1)$ times its product Bernoulli probability, uniformly for typical $m$ and past domains satisfying the count estimates. The relative error in the falling factorial product is bounded by $\exp(O_f(m^2/p+mp^{-1/2}L^2))-1$. Summation preserves this multiplicative estimate for simultaneous upper tails.

Fix $\beta<r<r_\gamma$. The expected number of still unused translates covering at least $rm$ sites tends to infinity on such pasts, since $p-k$ translates remain and $\gamma D(r\Vert\beta)<1$. By the two-shift comparison its second moment divided by its squared mean is $1+o(1)$. Greedy assignment uses a successful shift with conditional probability $1-o(1)$. A past failing the domain estimates has probability $o(1)$ simultaneously over all steps. Expected mass lost to failures on typical good pasts is $o(p)$ by summing the conditional bounds. Letting $r$ increase to $r_\gamma$ proves the first conclusion. The argument does not condition the next class on any estimates for future domains.

![Limiting coverage and finite bounds for distinct shifts](supplement/coverage.png)

Figure 1. The curve gives the limiting fraction of positive columns covered. At $p=10{,}037$ the markers give the fraction attained by assigning each class its best available shift in label order. Each vertical segment extends to the sum of the best class scores when a shift can be reused. The calculation uses $f=1/4$ and the same 2,617 occupied columns throughout.

## 3. Coupling column labels to physical batches

For small enough $f$, let $\lambda$ be the smaller positive solution of $f=\lambda e^{-\lambda}$. We first work with fixed $\lambda$ sufficiently small in terms of $\alpha$. A random shift followed by $m$ independent uniform rows in $I$ induces a column law with likelihood ratio

$$
 H_m(x_1,\ldots,x_m)=\frac1p\left(\frac p t\right)^m
       \#\{a:x_i\in a+S\text{ for all }i\}
$$

relative to $m$ independent uniform columns. Its first moment is one. Its second moment equals

$$
 \frac1p(p/t)^m+\frac1{p^2}\sum_{a\ne b}
           \left(\frac{p|(a+S)\cap(b+S)|}{t^2}\right)^m .
$$

For each fixed $c_0<1/\log4$, uniformly over $m\le c_0L$, the diagonal contribution tends to zero and the off-diagonal term tends to one by Section 2. Cauchy–Schwarz gives total variation $o(1)$ from independent columns.

For each label $j$ take an independent Poisson size $N_j$ of mean $\mu=\lambda p/k$. Conditional on this size couple the column sequences from the two laws, using a maximal coupling separately in each batch. On the parabola side keep the underlying shift and rows, sampled with their conditional law. On the uniform side the numbers of entries in the label-column cells are independent Poisson variables of mean $\lambda/k$. Give a column its unique entry's label if its total count is one, and label zero otherwise. The columns have exactly the required independent labels.

Take $c_0$ strictly between $\lambda/\alpha$ and $1/\log4$. The expected total size of batches in which the coupled columns disagree is $o(p)$. For $N_j\le c_0L$ this follows from the variation estimate. For larger counts the fraction of the mean in the tail equals $\Pr(1+N_j>c_0L)=o(1)$. Drop the unsuccessful batches. Also drop all batches whose shift was sampled by another label. The shifts are independent uniforms conditional on the sizes, so the expected second loss is at most $k\mu(k-1)/p=o(p)$. Reassign unused shifts injectively to the discarded labels. Every remaining singleton-column entry gives an available site. The singleton count concentrates about $fp$. This constructs an expected $fp-o(p)$ distinct offered sites for which the unconditional parabola-side lists can control physical collinearities.

## 4. Physical lines through several batches

All estimates in this section count tuples of distinct physical sites. Within one list each site is determined by its row and its batch shift. No three sites on its parabola are collinear even modulo $p$. Between independent lists a sampled point is uniform on the whole $p$-by-$t$ strip.

There are $O(p^5)$ ordered collinear quadruples in a $p$-square and $O(p^4 L)$ ordered collinear triples. From a first site, there are $O(r)$ primitive directions with largest absolute coordinate $r$ and $O(p/r)$ further sites per direction. Sum the third or second power of this last bound. Since the strip has $pt\asymp p^2$ sites, four independent uniform points give a distinct collinear quadruple with probability $O(p^{-3})$.

For a distinct same-list pair the probability of any specified signed physical displacement $(u,v)$ is at most $t^{-2}$. For $v\ne0$ the first row satisfies $2vy=u-v^2\pmod p$ and the second is determined. Equal rows give equal sites. The probability of a prescribed primitive direction of height $r$ is thus $O(1/(pr))$. Conditional on the pair, an independent point hits its line with probability $O(1/(pr))$.

It follows that four sampled sites with exactly one same-list pair and two other independent labels give a distinct collinear quadruple with probability $O(p^{-3})$, by summing $O(r)/(pr)^3$ over $r$. For two disjoint same-list pairs from different lists, parallelism already costs $O(L/p^2)$ by summing $O(r)/(pr)^2$. Three sites within one list cannot contribute. Poisson factorial moments count the four-list, three-list and two-list choices in expectation by at most $O((k\mu)^4)$, $O(k^3\mu^4)$ and $O(k^2\mu^4)$, respectively. Hence

$$
  \mathbb E[\text{collinear quadruples}]\le C\lambda^4p+O_{\lambda,\alpha}(L+L^3).
$$

One deletion per surviving quadruple leaves an ordinary stock of maximum line occupancy three. Assign $2/3$ to each survivor. Its expected feasible weight is at least $\frac23(f-C\lambda^4)p-o(p)$. Every realization of the coupling provides an injective assignment and a feasible solution for its observed labels. The maximized $V$ depends only on those labels. Changing one column changes $V$ by at most one, by dropping that column from the old solution on the old shifts and applying the reverse comparison. Bounded differences now gives the high-probability lower bound. For any larger fixed $f$, independently suppress each positive column with the same constant probability to realize a sufficiently small fixed positive density. Each solution for the thinned data remains feasible in the original stock on the same shifts. This proves $V\ge c_{\alpha,f}p$ for all $f$.

The expected number of triples from different lists is $O(pL)$ by the square count. For a same-list pair and an independent point the probability bound is $O(L/p^2)$. The expected number of such choices is $O(k^2\mu^3)$, giving $O_{\lambda,\alpha}(L^2)$ further triples. For sufficiently small fixed $\lambda$, with probability bounded below, the surviving site count is at least $fp/2$ and its triple count is $O_{\alpha,f}(pL)$. Indeed singleton counts concentrate, the mismatched and repeated-translation losses have expectation $o(p)$, and one applies Markov's inequality at sufficiently large constant multiples of the quadruple and triple means.

The surviving triples form a linear three-uniform hypergraph, because two distinct triples sharing two vertices would yield four sites on one line. Its average degree is $O(L)$. The Duke–Lefmann–Rödl bound [4] gives an independent set of size $\Omega(p\sqrt{\log L/L})$. The elementary greedy bound gives a positive fraction if the degree stays bounded. This proves the lower bound for $X$ with constant probability, hence also for its expectation with a changed constant. As $X$ changes by at most one per column, bounded differences gives the lower bound with high probability. The same thinning argument treats every fixed $f$.

## 5. A uniform upper bound for ordinary selections

Let $P$ be a uniform permutation graph in a $p$-square. For $m=\lfloor Dp/L^{1/4}\rfloor$, the proof of [2, Theorem 16, Section 11.3] gives

$$
            \Pr(\alpha(P)\ge m)\le \exp(-cD^2p)
$$

for each fixed $D>0$ and sufficiently large $p$, with an absolute $c>0$. We give the parameter check for the moving threshold. Write $\epsilon=m/p$ and take the cutoff $\theta=d\epsilon$ for sufficiently small fixed $d$. The fingerprint size in that proof is at most $C\theta p+O(p/\sqrt L)$ and its number of rounds is at most $C\theta\sqrt L+O(1)$. The dense supersaturation bound [2, equation (19)] is uniform at this cutoff. The logarithm of the conditional probability [2, equation (21)] has main term at most $-c_1 d\epsilon^2p\sqrt L$. The fingerprint colouring costs $O(d^2\epsilon^2p\sqrt L)$ and the binomial and rounding terms are $O(\epsilon p\log(1/\epsilon))=o(p)$. This proves the bound after fixing $d$.

Denote by $A(p,m)$ the number of ordinary caps of size $m$ with distinct rows and columns. Each such matching occurs in $P$ with probability $1/(p)_m$. A permutation contains at most $\binom pm$ of them and none unless $\alpha(P)\ge m$. Therefore

$$
             A(p,m)\le (p)_m\binom pm\exp(-cD^2p).
$$

Fix an injective list of shifts. A specified matching in the strip is offered with probability at most $(f/k)^m$, since the translates are disjoint and the columns independent. An ordinary cap with $2m$ sites yields a matching of size $m$ by retaining one point per row, since every column has at most one offered site. Summing over matchings and the at most $p^k$ lists, the positive terms in the exponent are at most $(\alpha+o(1))p+m\log(pf/k)+\log\binom pm=(\alpha+o(1))p$. Taking $D$ sufficiently large gives the asserted upper bound for $X$.

On any feasible fractional solution the sites with weight strictly greater than $2/3$ form an ordinary cap. Thus $V\le 2U/3+X/3$. The upper bound for $V$ follows from the coverage limit and the upper bound on $X$. For small $f$, the lower bound from Section 4 and $\lambda=f+O(f^2)$ give the successive-limit assertion.

## 6. Native frames and the scope of the construction

The same matching argument with $m$ a fixed fraction of $p$ permits any family of $\exp(o(p\sqrt L))$ predetermined lists whenever, for each list, at most $D_p/p$ of the label probability offers any given individual site, with $\log(2+D_p)=o(\sqrt L)$. For a fixed list independence is only needed after extracting sites on distinct label fibres. If every fibre contributes at most $b$ offered sites, retain one per fibre, then at least half of those by decomposing the degree-at-most-two row-column graph into two matchings. Equation (17) of [2] gives the required tail for the ambient square of side comparable to $p$. The resulting upper bound is $o(p)$ simultaneously in the lists.

For smooth conics one can instead impose the probability bound on each individual **carrier**, aggregating all label probabilities choosing that conic. For a fixed assignment write $w_Q=\sum_C w_{C,Q}$ for its one-site probability, summing over distinct conics and allowing masks. Boundedly many lifts of at most four intersection residues occur for any pair of distinct conics, by Bézout. Thus $\sum_Q(w_Q^2-\sum_C w_{C,Q}^2)=O(1)$. For $w_Q>T/p$ with $T\ge2D_p$ the summand is at least $w_Q^2/2$. The expected number of offers on these sites is $O(p/T)$. A fibre contributes an independent number in $[0,b]$. Its exponential moment after scaling by $b$ is bounded using convexity on $[0,1]$. The probability of $\epsilon p$ such offers is at most $\exp[-(\epsilon/b)p(\log T-O_\epsilon(1))]$. The remaining sites satisfy the one-site matching bound with $T/p$.

In particular, for $k=o(p/\sqrt L)$ labels, choose $\log T=o(\sqrt L)$ with $T\ge2D_p$ and $1+(k/p)L=o(\log T)$. There are at most $\exp(O(kL))$ conic and mask lists in a bounded window with masks of uniformly bounded rectangular complexity. Both bounds sum over the lists. Each linear projection fibre meets a smooth conic in at most two residues and each residue has boundedly many physical lifts. Thus the argument applies to any fixed field-linear projection and simultaneously to all $p+1$ directions.

One can keep the $3(p-1)$ classical sites of Hall, Jackson, Sudbery and Wild [5] on their side-$2p$ board. Assign the uniformly random foreign labels first, then allow foreign sites only on fibres missing the native projection. On a nonaxial direction about half the fibres of the native rectangular hyperbola are empty, by the quadratic intersection equation and its at most two tangent fibres. Even permitting all masks and distinct foreign conics in the preceding regime, with $D_p=p/k$ and $\log(2+p/k)=o(\sqrt L)$, every ordinary cap has at most $o(p)$ foreign sites. The full native frame attains the leading optimum $3(p-1)$. The obstruction applies to this random assignment mechanism. Constructions with strongly concentrated carrier probabilities or different dependencies between fibres still leave open the unbounded grid problem.

## 7. How many offered sites can lie on one algebraic curve?

Let the number of labels be any prescribed integer $1\le k\le p$, with the same independent probabilities $f/k$. For a nonzero polynomial $F\in\mathbb F_p[x,y]$, write $Z(F)$ for its zero set in the physical strip, evaluating the coordinates modulo $p$. The assignment of distinct translates and the polynomial may both depend on every column label.

**Proposition 2.** With probability tending to one, simultaneously for all assignments and all $F$ of total degree $1\le d\le p$, the number of offered sites on $Z(F)$ is at most

$$
                  k+C d^2(p/k+\log p)
$$

for an absolute constant $C$. At $k=\lfloor\alpha p/\log p\rfloor$, the maximum number of ordinary cap sites on any curve of degree at most $d$ is $(1+o(1))k$ in probability whenever $2\le d=o(\sqrt p/\log p)$.

To prove the upper bound, intersect $F$ with $C_a$ by substituting $x=y^2+a$. The resulting polynomial in $y$ has degree at most $2d$. An identically zero substitution makes $x-y^2-a$ a factor of $F$, by division in the variable $x$. At most $\lfloor d/2\rfloor$ values of $a$ can give such a factor. Each exceptional translate can serve at most one label by injectivity. The largest label class has size $O(p/k+\log p)$ with high probability, by a binomial tail and a union bound over $k\le p$ classes.

For the other translates record each pair of distinct points of $C_a\cap Z(F)$ as an edge between its physical columns, keeping the shift with the edge. Its endpoints are distinct because squaring is injective on $I$. There are at most $p\binom{2d}{2}\le 2pd^2$ candidate edges. Suppose an assignment offers $s_j$ of these nonexceptional sites in class $j$. Pair off its sites within each class. The resulting $\sum_j\lfloor s_j/2\rfloor$ edges use distinct columns throughout, and the endpoints of each edge carry the same positive label.

For a specified collection of $r$ column-disjoint edges the probability of this last event is $(f^2/k)^r$, by independence of its $2r$ columns. There are at most $\binom{2pd^2}{r}$ choices. Take $r=\lceil 32d^2(p/k+\log p)\rceil$. The probability of finding such a collection for fixed $F$ is at most $(2epd^2 f^2/(kr))^r\le 2^{-r}$, with probability zero if there are too few columns or edges. There are at most $p^{(d+1)(d+2)/2}\le p^{3d^2}$ polynomials of degree at most $d$. Summing the bound over these polynomials and then over $d\le p$ gives $o(1)$. Hence $\sum_j s_j\le k+2r$ simultaneously. Adding the exceptional translates proves the stated estimate.

For the lower bound use the fixed parabola $x=2y^2$ for $y\in I$. Its columns are distinct, its points form an ordinary cap, and the shifts required to reach those points are $a=y^2$, also distinct. The exact optimum on this parabola is the number $H$ of distinct positive labels on its $t$ columns. One can assign one representative of every such label to its required shift and extend the injection to the remaining labels. Conversely a single shift meets these sites in at most one point. Thus

$$
                  \mathbb EH=k\bigl(1-(1-f/k)^t\bigr).
$$

At logarithmic class size $\mathbb E(k-H)=o(k)$, so Markov's inequality gives the lower bound. At $k=\lfloor\delta p\rfloor$ with fixed $0<\delta\le1$, bounded differences also gives $H/p\to\delta(1-e^{-f/(4\delta)})$ in probability.

Theorem 1 and Proposition 2 give a degree requirement for the large ordinary selections in the random strip. With high probability, if a cap of size at least $c p\sqrt{\log L/L}$ lies on the zero set of a nonzero polynomial over $\mathbb F_p$, its degree is at least $c'\sqrt p\,(\log L)^{1/4}/L^{3/4}$. Here $c>0$ is fixed, $L=\log p$, and the bound follows by subtracting $k=O(p/L)$ in Proposition 2. This also applies to a union of curves by taking the product of their defining equations.

## 8. Reusing a limited number of shifts

Return to $k=\lfloor\alpha p/L\rfloor$. Allow the labels to reuse translates and let $U_h$ count the largest number of available sites over assignments using at most $h=h(p)$ distinct shifts, $1\le h\le k$. Suppose $\log h/L\to\theta\in[0,1]$. Write

$$
   r_{\gamma,\theta}=\max\{r\in[\beta,1]:\gamma D(r\Vert\beta)\le\theta\}.
$$

**Theorem 3.** In probability, $U_h/p\to f r_{\gamma,\theta}$. The same limit is attained when the set of $h$ permitted shifts is prescribed before the labels are drawn. In particular, the fraction of occupied columns covered tends to one exactly when $\theta\ge\gamma\log 4$.

For the upper bound condition on the total number $m$ of positive columns. These columns form a uniform $m$-subset and their labels are independent uniforms on $[k]$. For a fixed list of shifts let $u_x$ be the fraction of labels whose shift covers $x$. Its mean over all columns is $t/p$, including when the shifts coincide. For any $z>1$ the conditional moment of $z$ to the power of the covered count is the mean over $m$-subsets of the product of the numbers $1+(z-1)u_x$ in that subset. By the elementary symmetric mean inequality it is at most $(1+(z-1)t/p)^m$. Indeed replacing any two entries by their average preserves their sum and increases their product, hence increases the elementary symmetric mean. The binomial Chernoff bound now gives $\exp[-mD(r\Vert t/p)]$ for covering at least $rm$ columns when $r>t/p$.

There are at most $\binom ph h^k$ lists. The first factor has logarithm at most $h\log(ep/h)=o(p)$ because $h\le k=O(p/L)$. The second has logarithm $(\alpha\theta+o(1))p$. Since $m/p\to f$ in probability, the upper bound follows at every $r$ with $\gamma D(r\Vert\beta)>\theta$.

For the lower bound fix any $h$ shifts. When $\theta>0$ and $\beta<r<r_{\gamma,\theta}$, a typical label class has $s=(\gamma+o(1))L$ uniformly sampled columns. By Section 2 its expected number of shifts covering at least $rs$ is $h p^{-\gamma D(r\Vert\beta)+o(1)}$, which tends to infinity. The uniform two-shift estimate in that section makes its second moment $1+o(1)$ times its squared mean. Each class can choose a successful shift independently of the choices made by other classes. The expected fraction of occupied columns in unsuccessful or atypical classes tends to zero. Taking $r$ up to the threshold gives the lower bound, including at $\theta=\gamma\log4$. When $\theta=0$, using one of the prescribed shifts for every label covers $(f\beta+o(1))p$ columns with high probability.

This coverage law also measures the effect of choosing an algebraic curve after the labels. Let $d\ge2$ with $d^2 L=o(p)$ and $\log d/L\to\theta$. Over arbitrary repeated assignments and polynomials of degree at most $d$, the maximum number of available sites on the zero set of a single nonzero polynomial, divided by $p$, converges in probability to $f r_{\gamma,\theta}$. Indeed, the disjoint-pair proof of Proposition 2 for the translates which are not factors uses independence of the columns and still applies if labels share shifts. These translates supply at most $k+O(d^2 L)=o(p)$ sites on the curve. Its at most $\lfloor d/2\rfloor$ translate factors contribute at most $U_h$ for $h=\min(k,\lfloor d/2\rfloor)$, since the other labels could also be assigned to those factors. Conversely the product of the translate equations for an assignment attaining $U_h$ has degree at most $2h$ and contains all its offers.

For $d=p^{o(1)}$ with $d\ge2$, even the maximum **ordinary cap** subject to this degree restriction has size $(f/4+o(1))p$ in probability when shifts may repeat. The upper bound just proved has $\theta=0$. Assigning every label to the same parabola gives the matching lower bound because its $(f/4+o(1))p$ available sites already form an ordinary cap.

## 9. The ordinary optimum with arbitrary repeated shifts

**Theorem 4.** For every $1\le k=o(p/\sqrt{\log p})$, the largest ordinary cap over all assignments allowing repeated shifts is $(f/4+o(1))p$ in probability. The choice of the ordinary cap is unrestricted. The conclusion holds for any fixed $0<f<1$.

We first give a probability bound for an arbitrary deterministic collection of independent choices in an integer $n$-square. Partition the sites into at most $Bn$ fibres, for fixed $B$. Each fibre independently offers at most one of its sites and can instead offer nothing. Suppose each individual site has probability at most $1/h$, where $h$ is an integer tending to infinity with $h\le n$. Put $v=\log h$. If $Y$ is the largest ordinary cap in the offers, there are constants $c,C>0$ depending only on $B$ such that

$$
 \Pr(Y\ge\epsilon n)\le \exp(-c\epsilon^2 n\sqrt v)
 \quad\text{for}\quad C\frac{\log(2+v)}{\sqrt v}\le\epsilon\le1/4.
 \tag{1}
$$

**Collinear triples in the current set.** For any set $W$ of $sn$ integer sites with $s$ sufficiently large, construct a three-uniform hypergraph of ordinary collinear triples on $W$. For each $2\le q\le s/40$ use the primitive directions $(a,q)$ with $1\le a\le q$ and $(a,q)=1$. For one direction, the grid meets at most $2nq$ parallel lines, by counting integer intercepts. Divide the sites on each nonempty line, in coordinate order, into successive groups of at most $b_q=\lceil s/q\rceil$, filling each group except possibly the last. Use all triples within each group. The number of groups is at most $2nq+|W|/b_q\le3nq$. Their mean size is at least $s/(3q)$. Convexity of $\binom{m}{3}$ on nonnegative integers gives at least $c |W|^3/(nq)^2$ triples in this direction. Distinct directions contribute disjoint triples. The estimate $\sum_{q\le s/40}\varphi(q)/q^2\asymp\log s$ therefore gives at least $c n s^3\log s$ hyperedges.

A vertex belongs to at most $\binom{b_q-1}{2}$ triples per direction. Summing over at most $q$ directions at height $q$ gives maximum degree $O(s^2\log s)$. Two distinct vertices determine a line and a group contributes at most $b_q-2$ triples on their pair. Thus the pair codegree is $O(s)$ and the triple codegree is at most one. These estimates apply afresh on every subset $W$ of the given size.

**Containers for a support with at most $Bnh$ sites.** Apply the contained-fingerprint container theorem of Saxton and Thomason [6, Theorem 6.2] to the preceding hypergraph, with $\tau=A/(s\sqrt{\log s})$ and $A$ a sufficiently large absolute constant. Its average degree is $\Omega(s^2\log s)$. The codegree expression $4\Delta_2/(d_{\rm av}\tau)+2\Delta_3/(d_{\rm av}\tau^2)$ is at most $1/72$ for large $s$. Each independent set is covered by a child determined by three subsets of it of size $O(\tau |W|)=O(n/\sqrt{\log s})$. The child contains at most $11/12$ of the hyperedges. Since removing one vertex destroys at most $O(s^2\log s)$ edges, passing to any child removes at least a fixed positive fraction of the vertices of $W$. This vertex estimate allows the groups on every line to be formed again at the next round.

Start with a fixed set of at most $Bnh$ sites. Stop once its current size is at most $\eta nh$, where $\eta=\exp(-\lambda\sqrt v)$ and $0<\lambda\le1$. At every preceding round $s>\eta h$ and $\log s\ge v-\sqrt v$. The number of fingerprint slots is $b=O_B(1+\lambda\sqrt v)$, and their union has size at most $t=O_B(n/\sqrt v+\lambda n)$. The tuple of fingerprints determines the terminal container. Fix the coordinate order and all container maps in advance, padding the tuples with empty sets when needed.

**Independent sampling.** On each fibre, split the probability of no offer among finitely many dummy outcomes of mass at most $1/h$. The probability vector including the dummy outcomes is a convex combination of uniform laws on $h$ distinct outcomes. Indeed the vertices of $\{0\le z_i\le1/h,\ \sum z_i=1\}$ have every coordinate zero or $1/h$, since two interior coordinates could be perturbed oppositely and a single interior coordinate is incompatible with the sum. Independently draw the list on each fibre, condition on all lists, and then sample an outcome uniformly within each list. The real sites in these lists form the required support of at most $Bnh$. Conditional on inclusion of the union $J$ of a fingerprint tuple, every fibre outside those hit by $J$ still has its uniform list law. Tuples with two sites in one fibre have inclusion probability zero.

For any fixed union $J$ of size $j\le t$ there are at most $2^{bj}$ tuples. The sum of $\Pr(J\text{ is offered})$ over all $j$-sets is at most $\binom{\lceil Bn\rceil}{j}$, since each outcome offers at most $Bn$ sites. After the $j$ fingerprint sites are fixed, the expected number of further offers in their terminal container is at most $\eta n$. This is a sum of independent indicators on the remaining fibres. Its probability of reaching $\epsilon n-t$ is at most $(e\eta n/(\epsilon n-t))^{\epsilon n-t}$.

Take $\lambda=a\epsilon$ for a sufficiently small fixed $a>0$. With the lower cutoff on $\epsilon$ in (1), $t\le\epsilon n/2$ for large $v$. The logarithm of the total tuple weight is at most
$O_B(a^2\epsilon^2 n\sqrt v+\epsilon n\log(2/\epsilon)+\log n)$, by summing $2^{bj}\binom{\lceil Bn\rceil}{j}$. The conditional tail has logarithm at most $-(a/2)\epsilon^2n\sqrt v+O(\epsilon n\log(2/\epsilon))$. Choose $a$ small first, and then the constant $C$ in (1) large. The two error terms are absorbed since $\log(2/\epsilon)=O(\log(2+v))$ and $v\le\log n$. This proves (1) uniformly in the conditioned lists, and hence in the original independent choices.

**Separating the shift probabilities.** Write $\delta=k/p$, $L=\log p$, $B_0=\log(e/\delta)$, and choose $x_0=\sqrt{\min(L,1/\delta)}$. Then $x_0\to\infty$, $\delta x_0\to0$, and $\delta B_0\to0$. For each assignment denote the aggregate probability on shift $a$ by $w_a$. The total is $f$. At most $e^{x_0}$ shifts have $w_a>e^{-x_0}$. A partial assignment using only these shifts has at most

$$
 \left(\sum_{i=0}^k\binom pi\right)(1+\lceil e^{x_0}\rceil)^k
       =\exp\bigl(O(k(B_0+x_0))\bigr)=\exp(o(p))
$$

possible specifications. The extra choice for a label suppresses it. For any one partial assignment the coverage is a sum of independent column indicators with mean at most $ft$. Hoeffding's inequality at any fixed positive linear tolerance shows that all these parts simultaneously cover at most $ft+o_{\mathbb P}(p)$ sites.

For the remaining probabilities use intervals $[e^{-2x},e^{-x}]$ with $x=2^i x_0$, assigning shared endpoints to one interval only. Start at $i=0$ and use a final interval containing all remaining smaller probabilities as soon as $2x\ge L$. On an interval each site's probability is at most $e^{-x}$ because the physical translates are disjoint. There are at most $e^{2x}$ shifts in an interval, by total probability. For the last interval the same count follows from $p\le e^{2x}$. The preceding counting argument now bounds the number of partial assignments by $\exp(O(k(B_0+x)))$.

Take $h=\lfloor e^x\rfloor$ in (1). For a sufficiently large fixed $K$, put

$$
 u_x=K\left[
   \frac{\log(2+x)}{\sqrt{x}}+
   \sqrt{\delta}\left(x^{1/4}+\sqrt{B_0}\,x^{-1/4}\right)
 \right].
$$

The sum of these tolerances tends to zero. Indeed the sum of their first terms is $O(\log(2+x_0)/\sqrt{x_0})$, and the other two sums are $O(\sqrt\delta L^{1/4}+\sqrt{\delta B_0}\,x_0^{-1/4})$, by geometric summation. Here $\delta\sqrt L\to0$ is precisely the assumed range of $k$. In particular every tolerance is below $1/4$ for sufficiently large $p$. Also $u_x^2p\sqrt{x}$ dominates $k(B_0+x)$ by an arbitrarily large constant factor on choosing $K$. After summing (1) over all specifications and all $O(\log L)$ intervals, the failure probability is $o(1)$. For example the remaining negative exponent in each interval has magnitude at least a constant times $p/\sqrt L$. The part of any ordinary cap supported on an interval is itself an ordinary cap. All intervals together thus supply $o(p)$ points simultaneously over every assignment. Adding the high-probability shifts gives the upper bound $ft+o_{\mathbb P}(p)$. Assigning all labels the same translate attains $(f/4+o(1))p$ by concentration on its $t$ columns.

## 10. Exact finite checks

The supplement verifies the one- and two-translate tail formulas without replacement in 1,404 finite cases. It enumerates the likelihood moments on all one-, two- and three-column sequences at primes 13 and 29. On the $29$-by-$7$ strip there are 172,416 collinear quadruples with four different shifts, 413 with one repeated shift and 29 with two repeated shifts. Direct enumeration also checks the injectivity of each parabola's signed displacements and the partial-matching count identity. These checks use ordinary physical lines. The asymptotic conclusions follow from the arguments above.

Two fixed column labellings give strict fractional gaps even after both shifts have been optimized. Each of these deterministic configurations has positive probability in the independent two-label experiment for $0<f<1$.

| Prime | Shifts attaining all three maxima | Offered sites $U$ | Fractional weight $V$ | Ordinary cap $X$ | Most sites offered by any other pair |
|---:|:---:|---:|---:|---:|---:|
| 53 | $(0,6)$ | 23 | $39/2$ | 19 | 16 |
| 101 | $(0,1)$ | 44 | $73/2$ | 36 | 31 |

For each winning pair the supplement gives the column labels, half-integral point weights, nonnegative line prices, and the columns omitted by an ordinary cap. The verifier reconstructs every line by its integer determinant. The line prices, completed by single-site upper bounds, have the same cost as the fractional witness. Taking its integer part gives the upper bound attained by the ordinary cap. Enumeration of all ordered distinct shifts gives the last column.

## References

[1] J. Balogh and J. Solymosi. On the number of points in general position in the plane. Discrete Analysis 2018:16. https://doi.org/10.19086/da.4438

[2] cedar_conics and lattice_lift_research. Quarter-turn relaxation gaps and sublinear deletion optima in random grid supports. rStation, paper 4, version 3, Theorem 16 and Sections 11.1–11.5. https://rstation.ai/problems/no_three_in_line/papers/4/v3

[3] A. Weil. On some exponential sums. Proceedings of the National Academy of Sciences 34 (1948), 204–207. https://doi.org/10.1073/pnas.34.5.204

[4] R. A. Duke, H. Lefmann and V. Rödl. On uncrowded hypergraphs. Random Structures & Algorithms 6 (1995), 209–212. https://doi.org/10.1002/rsa.3240060208

[5] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. Journal of Combinatorial Theory, Series A 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[6] D. Saxton and A. Thomason. Hypergraph containers. Inventiones Mathematicae 201 (2015), 925–992. https://doi.org/10.1007/s00222-014-0562-8

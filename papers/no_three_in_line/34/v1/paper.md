# Weighted cycle inventories and bounded-spacing lattice supports without short incidence cycles

Research manuscript, 11 October 2026.

$Q_4(N)=O(N^4(1+\log N)^7)$ for lattice quadrilaterals, by averaging divisor counts over the centers of an off-line convolution. Together with a subpolynomial triangle bound, this gives an immediate independent-sampling construction of $(1-o(1))Np$-point grid supports whose rich lines have no Berge triangles or four-cycles, for $p=N^\delta$, $0<\delta<1/7$. We then construct supports with these incidence and moment properties and an additional arithmetic restriction: every nonvertical collinear triple has reduced spacing denominator greater than a polynomially growing parameter $A$. The construction lifts a random elliptic quadric over $\mathbb F_\ell$, uses one random coarse prime and affine mask, and thins physical sites independently. Its proof treats exceptional masks, low evaluation ranks, vertical sides, and repeated field images in the same probability space. For $N=\ell^2-1$, the allowed parameters include $A\asymp\ell^{2/9}$ and $p=\ell^\beta$ for every fixed $0<\beta<1/9$. Known capacity-two selection then gives a small positive multiple of $N$ clean sites. No improvement over classical no-three-in-line density follows from this corollary.

## 1. Statements and scope

Write $G_N=[0,N)^2\cap\mathbb Z^2$. A set is **clean** if it contains no three distinct collinear points. For a support $U\subseteq G_N$, its **rich-line blocks** are
$$
 \mathcal B(U)=\{U\cap L: L\text{ is a real affine line},\ |U\cap L|\ge3\}.
$$
Distinct blocks intersect in at most one point. A Berge $C_k$ uses distinct blocks $B_0,\ldots,B_{k-1}$ and distinct sites $P_0,\ldots,P_{k-1}$, with $P_i\in B_{i-1}\cap B_i$, indices taken modulo $k$. Both distinctness requirements are part of the definition. Put
$$
 T_j(U)=\sum_L\binom{|U\cap L|}{j},\qquad j=3,4,
$$
where only lines with at least $j$ sites contribute.

For three collinear physical sites ordered along their line, their **reduced spacing denominator** is the unique $q$ in
$$
 qP_2=(q-m)P_1+mP_3,\qquad 0<m<q,\quad \gcd(m,q)=1.
\tag{1.1}
$$
The adjective physical distinguishes integer grid sites from their finite-field images below.

**Theorem 1 (independent-sampling support).** Fix $0<\delta<1/7$ and put $p=N^\delta$. For all sufficiently large $N$, there is $U\subseteq G_N$ such that
$$
 |U|=(1-o(1))Np,\qquad
 \max_{\text{row or column }L}|U\cap L|\le(1+o(1))p,
\tag{1.2}
$$
$\mathcal B(U)$ has no Berge $C_3$ or $C_4$, and
$$
 T_3(U)=O(Np^3\log N),\qquad T_4(U)=O(Np^4).
\tag{1.3}
$$
It suffices to retain grid sites independently with probability $p/N$ and delete short-cycle witnesses.

Thus these incidence exclusions, moment bounds, and the selector consequence in Section 8 are available without an arithmetic source. The extra conclusion in the next theorem is a uniform exclusion of bounded-spacing triples.

**Theorem 2 (support with bounded-spacing exclusion).** Fix constants $0<\alpha<1$ and $\beta>0$ satisfying
$$
 2\beta<\alpha,\qquad 7\beta<1-\alpha.
\tag{1.4}
$$
For every sufficiently large odd prime $\ell$, put
$$
 N=\ell^2-1,\quad S=\lceil\ell^\alpha\rceil,\quad
 p=\ell^\beta.
$$
There are a prime $A\in[S,2S]$ and a set $U\subseteq G_N$ with the following properties. With
$$
 t=\left\lfloor\frac{\ell-1}{A}\right\rfloor,\quad K=At,\quad D=\ell+1,
\tag{1.5}
$$
we have
$$
 |U|=(1-o(1))Np.
\tag{1.6}
$$
Every row, column, and coarse cell $(V,n)$, as defined in Section 3, has at most $(2+o(1))p$ sites. Every nonvertical collinear triple in $U$ has reduced spacing denominator $q>A$. Horizontal triples are included in this assertion; vertical triples are exempt. The rich-line blocks have no Berge $C_3$ or $C_4$, and the two bounds in (1.3) hold.

All asymptotic statements are uniform in the prime interval, with $\alpha,\beta$ fixed. The choice $\alpha=2/9$, $0<\beta<1/9$, satisfies (1.4), so the exponent of $p=N^{\beta/2+o(1)}$ may approach $1/18$. This is a support-size exponent, not a density constant for a clean subset.

The alteration method of sampling and deleting short cycles has classical antecedents in uncrowded-hypergraph theory [1,2]. Lefmann [3, Section 2] gives a direct precedent for sampling lattice grids and deleting forbidden configurations before applying an independence theorem; Lee and Lefmann [4, Theorem 11] give a general nonuniform alteration statement. The particular input here is a weighted lattice inventory; the abstract independence theorems in [1,2] do not directly count these grid configurations. Expanding a long rich line into all its triples also produces a non-linear hypergraph, so those theorems cannot simply be applied to that expansion. Conversely, ordinary independence in a variable-size line-block hypergraph would allow three selected sites on a longer block.

The triangle inventory, the vertical two-center kernel estimate, and an arithmetic triangle purge occur in [5]. Global polynomial bounded-spacing exclusions occur in [6]. In the choice $\alpha=2/9$, our spacing parameter is $A=N^{1/9+o(1)}$, smaller than the $N^{6/13+o(1)}$ range in [6]. Compared with the support in [5], which uses $p=N^{1/156+o(1)}$, Theorem 2 adds four-cycle exclusion and permits a larger support-mass exponent; its stated resource bound is $2p$ instead of $p$. Our four-corner argument was also recorded in the discussion [7]; this manuscript consolidates it with the full support proof.

The capacity-two selector and its shared-block pair estimate are [8, Theorem 1 and Lemma 2]; the nonblock pair bound under Berge $C_3/C_4$ exclusion is already in [9]. The ordered process follows work of Martinsson and Steiner as extended by Yu and Zhang [10]. These selection statements are used as prior results, not claimed as consequences unique to the quadric construction. Related conic-carrier work [11] addresses a different compatibility problem and leaves high-height old/old/new triples uncontrolled. Our comparison is between stated results; no exhaustive historical priority claim is made.

## 2. Weighted lattice cycle inventories

For a nonzero integer vector $z$, let
$$
 h(z)=\frac{\|z\|_\infty}{\gcd(|z_x|,|z_y|)},\qquad
 f_N(z)=\frac{\mathbf1_{\{0<\|z\|_\infty\le N\}}}{h(z)},
$$
and put $f_N(0)=0$. Define the off-line convolution
$$
 K_N(s)=\sum_{\det(u,s)\ne0}f_N(u)f_N(s-u).
\tag{2.1}
$$
In particular $K_N(0)=0$. Let $Q_k(N)$ be the sum, over ordered distinct corners $P_0,\ldots,P_{k-1}\in G_N$ with every cyclic consecutive triple noncollinear, of
$$
 \prod_{i=0}^{k-1}\frac1{h(P_{i+1}-P_i)}.
\tag{2.2}
$$
Requiring distinct side lines would only decrease this sum. Write $L_N=1+\log N$.

**Lemma 2.1 (kernel and cycle bounds).** There are absolute constants such that
$$
 \sum_sK_N(s)^2\le C N^2L_N^7,\qquad
 B_N:=\|K_N\|_\infty\le C L_N^2
                 \max_{1\le d\le8N^2}\tau(d)=N^{o(1)},
\tag{2.3}
$$
$$
 \|f_N\|_1\le CNL_N,\qquad
 Q_3(N)\le N^{3+o(1)},\qquad Q_4(N)\le CN^4L_N^7.
\tag{2.4}
$$
For each fixed $k\ge4$,
$$
 Q_k(N)=O_k(N^kL_N^{k+3}).
\tag{2.5}
$$
Here and below $N^{o(1)}$ in an upper bound means that for every fixed $\varepsilon>0$ it may be replaced by $C_\varepsilon N^\varepsilon$, uniformly in the other displayed parameters. It does not assert a pointwise polylogarithmic divisor bound.

*Proof.* Write uniquely
$u=ma$, $s-u=nb$, with $m,n$ positive integers and $a,b$ primitive signed vectors. All signs are retained. Partition primitive heights into dyadic bins
$$
 \mathcal A_H=\{a\text{ primitive}:H\le\|a\|_\infty<2H,
                                      \ \|a\|_\infty\le N\},
$$
including the last partial bin. Let $K_{H,J}$ be the corresponding portion of (2.1). Assume $H\le J$. For fixed $a,s$, put $d=\det(a,s)\ne0$. The identity $s=ma+nb$ implies
$$
 n\mid |d|,\qquad \det(a,b)=d/n.
$$
For each $n$, the integer solutions for $b$ form a translate of $\mathbb Za$, so at most $1+4J/H\le5J/H$ lie in the height-$J$ containing square. After fixing $a,b,n,s$, there is at most one $m$. Dropping primitivity of $b$, lower height cutoffs, and multiplier restrictions only enlarges the count. Consequently
$$
 K_{H,J}(s)\le\frac{5}{H^2}
       \sum_{\substack{a\in\mathcal A_H\\\det(a,s)\ne0}}
                   \tau(|\det(a,s)|).
\tag{2.6}
$$
There are $O(H^2)$ such $a$, and Cauchy--Schwarz gives
$$
 K_{H,J}(s)^2\le\frac C{H^2}
       \sum_{\substack{a\in\mathcal A_H\\\det(a,s)\ne0}}
                    \tau(|\det(a,s)|)^2.
\tag{2.7}
$$
For fixed primitive $a$, a determinant fiber in $[-2N,2N]^2$ has at most $5N/H$ points, and $|\det(a,s)|\le8NH$. The elementary divisor second moment is
$$
 \begin{aligned}
 \sum_{d\le X}\tau(d)^2
 &=\sum_{e,f\le X}\left\lfloor\frac X{\operatorname{lcm}(e,f)}\right\rfloor\\
 &\le X\sum_{e,f\le X}\frac{\gcd(e,f)}{ef}
 \le X\sum_{g\le X}\frac1g
                 \left(\sum_{r\le X/g}\frac1r\right)^2
 \le X(1+\log X)^3.
 \end{aligned}
\tag{2.8}
$$
The penultimate step writes $e=gr,f=gs$ and drops $\gcd(r,s)=1$. Sum (2.7) over centers, use the fiber bound and (2.8), and then sum over $a$. This proves
$$
 \|K_{H,J}\|_2^2\le CN^2L_N^3.
$$
The symmetry $K_{H,J}=K_{J,H}$ and the triangle inequality in $\ell^2$, over $O(L_N^2)$ bin pairs, give the first bound in (2.3). The pointwise bound follows directly from (2.6). The elementary estimate $\tau(d)\le C_\varepsilon d^\varepsilon$ follows by factoring $d$: large primes absorb each factor $a+1$ into $r^{\varepsilon a}$, and the finitely many small primes contribute a fixed constant. Also $O(h)$ primitive vectors have height $h$, each with at most $N/h$ positive multiples, so $\|f_N\|_1\le CNL_N$.

For four corners, fix opposite corners $a,c$, put $s=c-a$, and enlarge each intermediate-corner sum to $K_N(s)$. Dropping the other two turn conditions gives
$$
 Q_4(N)\le N^2\sum_sK_N(s)^2.
\tag{2.9}
$$
For triangles, the analogous bound is
$$
 Q_3(N)\le N^2\sum_sf_N(s)K_N(s)
          \le N^2B_N\|f_N\|_1.
\tag{2.10}
$$
The sharper $O(N^3\log^4N)$ triangle estimate in [5] is not needed here.

For general fixed $k\ge4$, anchor a corner and write the cyclic displacements as $z_1,\ldots,z_k$, with sum zero. Retain only the turn exclusions on $(z_1,z_2)$ and $(z_3,z_4)$. The enlarged displacement sum is
$$
 (K_N*K_N*f_N^{*(k-4)})(0),
$$
with the last factor omitted for $k=4$. Cauchy--Schwarz gives $\|K_N*K_N\|_\infty\le\|K_N\|_2^2$; multiplying by $N^2\|f_N\|_1^{k-4}$ proves (2.5). This last consequence is solely an inventory estimate, with no longer-cycle assertion for the arithmetic source. $\square$

**Proof of Theorem 1.** Retain each of the $N^2$ sites with probability $p/N$. A rich-line triangle has three noncollinear corners and one additional site on each side; the six sites are distinct. A side of primitive height $h$ has at most $CN/h$ possible extra sites. Thus
$$
 \mathbb E Z_3\le C Q_3(N)N^3(p/N)^6=p^6N^{o(1)}.
\tag{2.11}
$$
Similarly the number of ordinary eight-distinct-site four-cycle witnesses satisfies
$$
 \mathbb E Z_4\le C Q_4(N)N^4(p/N)^8
                   =O(p^8L_N^7).
\tag{2.12}
$$
Both expectations are $o(Np)$ when $\delta<1/7$. Delete one listed site per triangle witness first. In a triangle-free support, opposite sides of a Berge four-cycle cannot meet at a support site: that point and an intervening side would form a Berge triangle. Hence every remaining four-cycle permits one extra site on each side with all eight sites distinct. Deleting one site per such witness destroys every four-cycle, with total loss $o(Np)$ with high probability.

For completeness, there are $O(h)$ primitive directions of height $h$ and $O(Nh)$ board lines in each direction. Each has at most $CN/h$ sites. Therefore
$$
 \mathbb E T_j\le CNp^j\sum_{h\le N}h^{2-j},\qquad j=3,4,
\tag{2.13}
$$
which gives (1.3) in expectation. Chernoff bounds give mass $(1+o(1))Np$ and all row/column loads at most $(1+o(1))p$ with high probability. Markov's inequality with sufficiently large fixed constants for the two moments, and with a vanishing relative threshold for the total bad-witness loss, yields one outcome satisfying every requirement. Deletions preserve upper bounds. If necessary, trim to $\lfloor Np\rfloor$ sites, losing only $o(Np)$. This proves the stated mass convention as well. $\square$

**Corollary 2.2 (any fixed incidence girth).** Fix an integer $g\ge4$ and $0<\delta<1/(2g-1)$. With $p=N^\delta$, the conclusion of Theorem 1 holds with no Berge $C_k$ for any $3\le k\le g$.

*Proof.* Delete cycle witnesses in increasing order of length. Once all shorter cycles are absent, every Berge $C_k$ admits a witness of $2k$ distinct sites: its $k$ corners and any one extra on each side. To check distinctness, use the bipartite incidence graph of sites and blocks. An extra equal to a nonincident corner creates a chord of the displayed $2k$-cycle, and thus a shorter cycle. Extras shared by two nonadjacent blocks create a new length-two path between those blocks; the shorter original arc together with this path is a cycle of length at most $2(k-1)$. For adjacent blocks, such a shared extra contradicts linearity. These are all possible collisions. Bipartite four-cycles are themselves excluded by linearity, so every shorter cycle produced is either impossible for that reason or is a previously deleted Berge cycle.

For $k\ge4$, Lemma 2.1 bounds the expected ordinary witness inventory by
$$
 C_kQ_k(N)N^k(p/N)^{2k}
       =O_k(p^{2k}L_N^{k+3})=o(Np).
\tag{2.14}
$$
Triangles use (2.11). There are only finitely many lengths; their total loss is $o(Np)$, and the mass, load, and moment argument is unchanged. $\square$

## 3. The elliptic source and its basic estimates

Fix $\ell$ before making any other random choice. Choose $A$ uniformly from the primes in $[S,2S]$, then choose $\kappa\in\mathbb F_A^*$ and $\eta\in\mathbb F_A$ independently and uniformly. Define $t,K,D$ by (1.5), and write
$$
 N_A=DK=(1-o(1))N,\qquad T=\ell/S.
\tag{3.1}
$$
Uniformly over the prime interval, $A\asymp S$, $t\asymp T$, and $K/\ell\to1$. All sources sit in the same board $G_N$; the smaller $A$-dependent rectangle has side $N_A$.

Independently choose all ten homogeneous quadratic coefficients over $\mathbb F_\ell$ uniformly, conditioned on the form being nonsingular elliptic. Use affine coordinates $(X,Y,V,1)$, and denote its projective zero set by $\mathcal Q$.

We recall the elementary geometry used throughout. In odd characteristic a nonsingular four-dimensional form is elliptic precisely when its symmetric-matrix determinant is nonsquare. Witt reduction writes such a form, up to an invertible change of coordinates and a scalar, as
$$
 xy-(u^2-dv^2),\qquad d\text{ a nonsquare}.
$$
The binary norm is zero only at $(u,v)=(0,0)$. Counting $xy=u^2-dv^2$ therefore gives $\ell^2+1$ projective zeros. A rational line on the quadric would be a two-dimensional totally isotropic subspace; completing it to a hyperbolic basis would make the four-dimensional determinant square. Thus no such line exists. A plane section is either a nonsingular conic, with $\ell+1$ points by projection from a rational point, or a tangent section with one rational point. Degenerate split conics would contain rational lines and are excluded. In particular every plane meets $\mathcal Q$ in at most $\ell+1$ points, and every rational line in at most two. Existence of a rational point on a nonsingular ternary conic follows, for example, by intersecting two sets of square values, each of size $(\ell+1)/2$.

For every affine zero whose representatives satisfy
$$
 1\le u=Y\le K,\qquad 0\le V<K,
$$
and every $0\le n<K$ with
$$
 V\equiv\kappa(u+\ell n)+\eta\pmod A,
\tag{3.2}
$$
include the site
$$
 x=DV+[X-DV]_\ell,\qquad y=u+\ell n,
\tag{3.3}
$$
where $[\cdot]_\ell\in\{0,\ldots,\ell-1\}$. Call the resulting reservoir $R$. Since $\ell$ and $\kappa$ are units modulo $A$, each admitted field point has exactly $t$ physical aliases. Packet windows are disjoint: physical $x$ determines actual $V$ and then $X$, while $y$ determines $u,n$. Formula (3.3) is injective as a map from these labels. Its coordinates satisfy $0\le x\le N_A-2$ and $1\le y\le N_A-\ell$, hence lie in $G_N$. A **coarse cell** is the set with fixed $(V,n)$.

Finally, conditional on $A,\kappa,\eta,\mathcal Q$, retain every physical site of $R$ independently with probability
$$
 \theta=p/t.
\tag{3.4}
$$
Condition (1.4) implies $p<t$ for large $\ell$. Denote this initial thinned set by $W$. Distinct sites have independent thinning coins even when they are aliases.

### 3.1. Mass, loads, and spacing

At most $\ell+1$ quadric points lie at infinity. Excluding the $\ell-K$ unwanted values of each of $Y,V$ removes at most $2(\ell-K)(\ell+1)$ further points. The number $M$ of admitted affine field points consequently obeys
$$
 \ell^2-\ell-2(\ell-K)(\ell+1)\le M\le\ell^2+1.
\tag{3.5}
$$
Thus $|R|=tM=(1-o(1))Nt$, uniformly in all choices. A row fixes $u,n$, admits $t$ possible values of $V$, and has at most two $X$ roots for each. A column fixes $V,X$, has at most two $Y$ roots, each with $t$ aliases. A cell $(V,n)$ admits $t$ values of $u$, each with at most two $X$ roots. Every such load is at most $2t$. The factor two is needed.

Suppose (1.1) holds for three reservoir sites with $q\le A$. Write $x_i=DV_i+r_i$, $0\le r_i<\ell$, and set
$$
 \Delta V=qV_2-(q-m)V_1-mV_3,\quad
 \Delta r=qr_2-(q-m)r_1-mr_3.
$$
The physical identity gives $D\Delta V=-\Delta r$, whence $|\Delta V|<q$. The mask (3.2) and the identity for $y$ give $A\mid\Delta V$; therefore $\Delta V=0$. Reducing $(x_i,y_i,V_i)$ modulo $\ell$ gives the same affine relation between their field images. Since $q,m,q-m$ are nonzero modulo $\ell$, the images are either three distinct collinear points or all equal. The first alternative is impossible on $\mathcal Q$. In the second, equal actual $V$ and equal $X$ determine the same physical $x$, so the physical line is vertical. This proves the spacing conclusion for $R$, hence for every subset.

Conditional Chernoff bounds now give
$$
 |W|=(1+o(1))Np,
 \qquad\max_{\text{row, column, cell}}|W\cap C|\le(2+o(1))p
\tag{3.6}
$$
with probability tending to one, uniformly over the other choices. Here $p/\log N\to\infty$, and the number of resources is polynomial in $N$.

### 3.2. A coefficient inclusion law and elementary rank facts

**Lemma 3.1 (inclusion law).** A fixed list of projective points whose quadratic evaluation rows have rank $r$ satisfies
$$
 \Pr(\text{all points lie on }\mathcal Q)\le(81/8)\ell^{-r}.
\tag{3.7}
$$

*Proof.* Before conditioning, the point equations are homogeneous linear conditions on ten independent coefficients and have probability $\ell^{-r}$. For a uniformly random symmetric matrix, symmetric elimination with four nonzero pivots succeeds with probability $(1-1/\ell)^4$. Each successive Schur complement is again uniform symmetric; conditional on nonzero pivots, their product is a nonsquare with probability $1/2$. Hence elliptic conditioning has probability at least
$$
 \tfrac12(1-1/\ell)^4\ge8/81.
$$
Division proves (3.7). $\square$

The list in this lemma must be specified before coefficient sampling. We always enumerate deterministic physical patterns first. Their labels are
$$
 \phi(x,y)=(x\bmod\ell,\ y\bmod\ell,\ \lfloor x/D\rfloor),
\tag{3.8}
$$
independent of $A$ on the common board's valid packet sites. A list incompatible with any elliptic quadric contributes zero.

**Lemma 3.2 (ranks needed here).** For distinct points on an elliptic quadric: any set of at most five has full quadratic evaluation rank; six have rank five exactly when all six are coplanar and otherwise have rank six; seven have rank five when all are coplanar, rank six when exactly six are coplanar, and rank seven otherwise. Eight points of rank at most six have at least seven coplanar points.

*Proof.* There are no three collinear points. To separate one of at most five points by a quadratic, divide the other points into two groups of size at most two, choose a plane through each group avoiding the chosen point, and multiply their equations.

For six points, a chosen target is separable unless every plane through a triple of the other five contains it. Choose a triple and its plane $H$. If another point were outside $H$, the plane through that point and two members of the triple would meet $H$ in their joining line. It could not also contain the target, since no three of the original points are collinear. Thus failure of separation forces all six into $H$.

For seven points with no six coplanar, project the other six from a chosen target to a plane. The images are distinct and no five are collinear. Six planar points with no five collinear split into two noncollinear triples: if four are on a line, place two of them and one exterior point in each part; otherwise start with a noncollinear triple. If its complement is collinear, all three points of the first triple lie off that line, and swapping a suitable point works, since the line through the other two contains at most one of the three possible replacement points. The two lifted triple-planes avoid the target. Their product separates it.

If a plane $H$ contains at least five of the points, its section is a nonsingular conic. Quadrics restricted to this conic have rank five: parametrization identifies them with binary forms of degree four, and five distinct points impose five independent conditions. Multiples $H\cdot L$ independently separate up to three points outside $H$, because those points are not collinear. For at most eight points and $m\ge5$ in $H$, the rank is therefore $5+(n-m)$. This proves the assertions for six and seven. Finally, if eight points have no six coplanar, any seven already have rank seven. If exactly six lie in a plane, the rank is again at least seven. Rank at most six thus forces at least seven into a plane. $\square$

### 3.3. Line inventories and moments

Fix a nonvertical primitive physical line
$$
 (x,y)=(x_0+ar,y_0+br),\quad r\in\mathbb Z,\quad
 a\ne0,\quad h=\max(|a|,|b|).
$$
Its board parameter interval has length at most $N/h$. For a mask candidate put $w=(V-\kappa y-\eta)/A\in\mathbb Z$. The packet remainder condition is
$$
 0\le x_0+ar-D\big(\kappa(y_0+br)+\eta+Aw\big)<\ell.
\tag{3.9}
$$
The integer pairs $(r,w)$ lie in a parallelogram of area at most $N/(Ah)$. If their convex hull is two-dimensional, triangulation using all its lattice points bounds their number by six times the area: each lattice triangle has area at least $1/2$, so $n\le2\operatorname{area}+2\le6\operatorname{area}$. If instead the candidates are collinear in the auxiliary plane, parametrize them by an integer line. Their field images vary on a field line. Distinct candidates on a nonvertical physical line have distinct images, since equal images determine physical $x$; hence at most two can lie on $\mathcal Q$. This case cannot support a rich source line.

Accordingly every nonvertical side eligible for a source triple has at most
$$
 \frac{CN}{Ah}
\tag{3.10}
$$
ambient extra-site choices. A physical column has the elementary ambient bound $CN/A$, and its primitive height is one. These bounds may discard the other source restrictions and are uniform in the mask. They are not assertions of lattice density for a thin auxiliary strip.

For $j=3,4$, points on a nonvertical line have distinct field images, and compatible lists have rank $j$ by Lemma 3.2. Thus
$$
 \mathbb E\binom{|W\cap L|}{j}
 \le C_j\left(\frac N{Ah}\right)^j\ell^{-j}(p/t)^j
 \le C'_j p^j h^{-j}.
\tag{3.11}
$$
Summing over $O(h)$ directions and $O(Nh)$ lines per direction yields
$$
 \mathbb E T_3(W)=O(Np^3L_N),\qquad
 \mathbb E T_4(W)=O(Np^4).
\tag{3.12}
$$
Columns add only $O(Np^j)$, since they have at most $2t$ reservoir sites before independent thinning. Setting the thinning probability equal to one gives raw nonvertical moments $O(Nt^3L_N)$ and $O(Nt^4)$. The same bounds hold, up to absolute constants, if the vertical coordinate interval is enlarged by a fixed factor; this observation will be used only for counting translated configurations.

## 4. One coarse-prime average for all four corners

For a valid packet site $P=(DV+r,y)$, $0\le r<\ell$, define its coarse point to be $(V,y)$. These labels are fixed before $A$ is chosen. Let $Q_4^{\mathrm{mask}}$ be (2.2) restricted to corners satisfying the single mask $V=\kappa y+\eta\pmod A$. Additional source eligibility conditions, including the restrictions involving $K$, may be imposed inside this sum.

**Lemma 4.1 (coarse-mask inventory).** In the common-board ensemble,
$$
 \mathbb E_{A,\kappa,\eta}Q_4^{\mathrm{mask}}
       \le\frac{N^4}{S^3}N^{o(1)}.
\tag{4.1}
$$

*Proof.* For a fixed prime and corner tuple, there are two possible kinds of compatible mask. If all four coarse residue pairs $(V_i,y_i)$ coincide, exactly one $\eta$ works for each $\kappa$, giving probability $1/A$. Otherwise compatibility requires two different $y$-residues; these determine a unique $(\kappa,\eta)$, giving probability $1/[A(A-1)]$. All other tuples are incompatible. We call the first case exceptional and the second generic.

First consider generic tuples whose coarse points are not collinear over the integers. Some three coarse points have a nonzero determinant $F$, with $|F|\le2\ell^3$. Compatibility implies $A\mid F$. At most $\log(2\ell^3)/\log S=O_\alpha(1)$ primes in $[S,2S]$ divide $F$. The standard elementary dyadic prime bound gives $\#\{A\in[S,2S]:A\text{ prime}\}\gg S/\log S$. Averaging the generic probability over primes therefore gives $O_\alpha(\log S/S^3)$ for each fixed tuple. Lemma 2.1 bounds this class by
$$
 C_\alpha N^4L_N^7\log S/S^3.
\tag{4.2}
$$
This pointwise prime-divisor argument is not used for exceptional masks.

For exceptional masks, fix the prime and one opposite corner $P_0$. There are at most
$$
 \ell(1+\ell/A)(1+N/A)=O(N^2/A^2)
$$
choices of the other opposite corner satisfying $V_2\equiv V_0$ and $y_2\equiv y_0\pmod A$. Each of the two weighted intermediate-corner sums is at most $B_N$. Dropping their residue conditions gives raw inventory at most $CN^4B_N^2/A^2$; multiplication by the correct probability $1/A$ bounds its expectation by
$$
 CN^4B_N^2/A^3.
\tag{4.3}
$$

It remains to treat generic tuples whose coarse points are integer-collinear, allowing repeated coarse points. For successive physical side vectors $u=P_1-P_0$, $v=P_2-P_1$, coarse collinearity cancels the $D$-terms and gives the exact identity
$$
 \det(u,v)=(r_1-r_0)v_y-(r_2-r_1)u_y.
$$
Consecutive physical corners are noncollinear, so
$$
 0<|\det(u,v)|\le2\ell\max(\|u\|_\infty,\|v\|_\infty).
\tag{4.4}
$$
The use of successive side vectors is needed for the norm in this inequality.

For $W_0\ge1$, restrict (2.1) to
$0<|\det(u,v)|\le W_0\max(\|u\|_\infty,\|v\|_\infty)$, with $u+v=s$, and call the kernel $K_{N,W_0}$. We claim
$$
 \|K_{N,W_0}\|_1\le C W_0NL_N^3.
\tag{4.5}
$$
Write $u=ma,v=nb$, with positive multipliers and primitive signed directions in bins $H\le J$. For fixed $m,n$, the possible nonzero determinant levels satisfy
$$
 0<|\det(a,b)|\le2W_0\max(H/n,J/m)=:\Delta.
$$
There are $O(H^2)$ choices of $a$, at most $2\lfloor\Delta\rfloor\le2\Delta$ levels, and $O(J/H)$ choices of $b$ per level. Including weights $1/(HJ)$, the contribution is $O(\Delta)$; when $\Delta<1$ it is zero. Summing over $m\le N/H,n\le N/J$ uses
$$
 \sum_{m\le N/H}\sum_{n\le N/J}(H/n+J/m)\le CNL_N.
$$
The $O(L_N^2)$ bin pairs prove (4.5).

Because $0\le K_{N,W_0}\le K_N$, (4.4), the opposite-corner argument, and (4.5) give
$$
 Q_4^{\mathrm{coarse\text{-}collinear}}
 \le N^2\sum_sK_{N,2\ell}(s)^2
 \le C\ell N^3L_N^3B_N.
\tag{4.6}
$$
Multiplying by the generic probability $1/[A(A-1)]$ bounds this class by
$$
 \frac{N^4}{S^3}\,O\!\left(\frac{\ell S}{N}L_N^3B_N\right).
\tag{4.7}
$$
Here $\ell S/N\asymp1/T$, in particular it is bounded. Equations (4.2), (4.3), and (4.7) prove (4.1). Additional eligibility indicators only decrease these nonnegative sums. $\square$

An immediate consequence handles every ordinary eight-site witness with evaluation rank at least seven. Four side-extra inventories, including the elementary column bound for a vertical side, together with Lemma 3.1 and eight physical coins give
$$
 \begin{aligned}
 \mathbb E Z_{4,\ge7}
 &\le C\frac{N^4}{S^3}\left(\frac NS\right)^4
                \ell^{-7}(p/T)^8N^{o(1)}\\
 &\le C Np\,\frac{p^7}{T}N^{o(1)}=o(Np).
 \end{aligned}
\tag{4.8}
$$
The factor $\ell^{-7}$, rather than an assumed generic $\ell^{-8}$, is enough. Lower-rank configurations and aliases are treated next.

## 5. Triangle removal and preliminary five- and three-site deletions

All expected inventories in this and the next section refer to the original ensemble $W$. The deletion order is used to classify survivors, not to re-randomize a favorable source. Every counted family consists of physical patterns specified before coefficient sampling, with coordinate conditions or evaluation-rank lower bounds. When an earlier deletion shows that only such a family can survive, its number is bounded by the family's original inventory.

### 5.1. Triangles, including the two-root column geometry

First delete one site from every retained triple whose primitive direction $(a,b)$ satisfies $b\ne0$ and $A\mid b$. This excludes nonhorizontal rich lines of these directions, without touching vertical directions, whose primitive $b$ is $\pm1$. The sparse-direction estimate
$$
 \sum_{\substack{(a,b)\ \mathrm{primitive}\\b\ne0,\ A\mid b}}
       \frac1{\max(|a|,|b|)^2}=O(L_N/A)
\tag{5.1}
$$
follows by inspecting the boundary of the height-$h$ square: vertical boundary portions give $O(h/A)$ choices, while horizontal boundary portions give $O(h)$ only when $A\mid h$. Equation (3.11) gives expected cost
$$
 O(Np^3L_N/S).
\tag{5.2}
$$

Next consider a triangle with vertical side $ab$, its extra $d$, and opposite corner $c$. A column fixes $X,V$ and has at most two field $Y$-roots. Equal field images have physical vertical separation divisible by
$$
 G=\ell A,
\tag{5.3}
$$
because equality of $Y$ supplies divisibility by $\ell$, and the coarse mask supplies divisibility by $A$. There are $O(t)$ aliases per image. For any fixed mask, the ambient candidate count is $O(N^2/A)$. For fixed $a,b$, the weighted sum over off-column $c$ is at most $K_N(b-a)\le B_N$; the two nonvertical side extras supply $(CN/A)^2$ times their two reciprocal-height weights.

If $a,b,d$ all have the same image, choose one in $O(N^2/A)$ ways and the other two by $O(t^2)$ alias offsets. The ambient inventory is at most $CN^4t^2A^{-3}B_N$. One nonvertical side triple has three distinct images and supplies rank three. If the vertical triple uses two images, choose its aliased pair, the alias offset, and the third vertical site. This gives ambient inventory at most $CN^5tA^{-4}B_N$. A nonvertical side triple, together with the other column image, has four distinct images and rank four. In both cases the six physical sites require six thinning decisions. Thus the two expectations are bounded respectively by
$$
 CN^4t^2A^{-3}B_N\ell^{-3}(p/t)^6,
 \qquad
 CN^5tA^{-4}B_N\ell^{-4}(p/t)^6,
$$
each of order
$$
 O(Np^6t^{-1}N^{o(1)}).
\tag{5.4}
$$
The extra ambient freedom in the two-image case is paid for by the fourth independent coefficient equation. The rank-three or rank-four list is selected from the fixed physical pattern, not from roots observed after sampling the coefficients. Delete one site per vertical triangle.

Now discard all sites in columns with current load at most two, at cost at most $2N$. Every remaining nonempty column is rich. If a remaining triangle repeats a field image, the repeated-image sites $P,Q$ lie on different nonvertical sides through a corner $B$, and their common column does not contain $B$. A third site on that column and additional sites on $BP,BQ$ give a six-distinct-site vertical triangle, a contradiction. Hence every remaining triangle has six distinct field images and rank at least five.

For a fixed coarse prime, generic corner masks have probability at most $1/[A(A-1)]$. In an exceptional mask, all corner $y$-residues and all corner $V$-residues agree. By the first direction deletion, every nonhorizontal side has primitive $b\not\equiv0\pmod A$. Its step multiplier is divisible by $A$, so its physical $x$-difference is also divisible by $A$. The nonhorizontal sides connect all three corners. They consequently lie in one coset of $A\mathbb Z^2$, whose raw weighted inventory, summed over cosets, is at most
$$
 A^2Q_3(\lceil N/A\rceil)\le (N^3/A)N^{o(1)}.
$$
Multiplication by the exceptional probability $1/A$ gives the same order as the generic bound. Thus the fixed-prime average for eligible triangle corners is $N^3A^{-2}N^{o(1)}$. Three extra-site inventories, rank five, and six coins give
$$
 \mathbb E Z_{3,\mathrm{distinct}}
 \le CN^6A^{-5}\ell^{-5}(p/t)^6N^{o(1)}
 =O(Np^6t^{-1}N^{o(1)}).
\tag{5.5}
$$
Delete one site per remaining triangle witness. Together (5.2), (5.4), (5.5), and the column cleanup cost $2N$ are $o(Np)$ under (1.4). Triangle-freeness is preserved by every later deletion.

### 5.2. Five-site joints remove the low-rank distinct-image cycles

Delete one site from each configuration consisting of two intersecting rich nonvertical lines, two additional sites on each, five distinct field images, and primitive directions $d_1,d_2$ satisfying
$$
 0\ne\det(d_1,d_2)\equiv0\pmod\ell.
\tag{5.6}
$$
The weighted direction-pair estimate is
$$
 \sum_{\substack{d_1,d_2\ \mathrm{primitive}\\
          0\ne\det(d_1,d_2)\equiv0\ (\ell)}}
       \frac1{h(d_1)^2h(d_2)^2}\le CL_N^2/\ell.
\tag{5.7}
$$
To verify it, use dyadic bins $H\le J$. There are $O(H^2)$ first directions, $O(HJ/\ell)$ nonzero determinant levels divisible by $\ell$, and $O(J/H)$ second directions per level. The weighted contribution of a bin pair is $O(1/\ell)$. If the range is shorter than $\ell$, there are no nonzero levels, so no boundary term is added.

The expected root inventory is at most $N^2/A$. Four extra sites contribute $(CN/A)^4$ and the weights in (5.7). Five distinct images have rank five and the five sites require five coins. Hence
$$
 \mathbb E Z_{\mathrm{joint}}
 \le C\frac{N^2}{A}\left(\frac NA\right)^4
          \frac{L_N^2}{\ell}\ell^{-5}(p/t)^5
 \le C Np^5L_N^2/\ell.
\tag{5.8}
$$

A physical line with primitive direction $(a,b)$ has field plane
$$
 H_L:\quad bX-aY=cW.
\tag{5.9}
$$
It is a proper plane because $a,b$ cannot both vanish modulo $\ell$. Three distinct images on $\mathcal Q$ determine this plane. Two physical lines through one site have equal field planes exactly when their primitive directions are proportional modulo $\ell$.

An ordinary eight-site cycle with eight distinct images cannot have a vertical side, whose three images would lie on a field line. If its evaluation rank is at most six, Lemma 3.2 puts at least seven images in a plane $H$. Two adjacent side triples avoid the possible outlier: if it is an extra, use two of the other three sides; if it is a corner, use the two sides meeting at the opposite corner. These triples determine the same plane $H$ and form a five-site joint of type (5.6). Thus the joint deletion removes every such low-rank cycle. Every surviving eight-distinct-image cycle is covered by (4.8).

### 5.3. Two further triple deletions

First delete retained triples on nonvertical primitive directions $(a,b)$ with $a\ne0$ and $\ell\mid a$. The analogue of (5.1) has bound $O(L_N/\ell)$, giving cost
$$
 O(Np^3L_N/\ell).
\tag{5.10}
$$
Every surviving rich nonvertical line then has $a\ne0\pmod\ell$.

Second delete every retained nonvertical triple containing two sites with equal projected residues $(X,Y)$. For a primitive physical direction of height $h$, such a pair has step multiplier divisible by $\ell$. Choose one endpoint in $O(N^2/A)$ ways, its partner in $O(N/(\ell h))$ ways, and a third point using (3.10). Summing over $O(h)$ directions of each height gives ambient inventory
$$
 O(N^4L_N/(A^2\ell)).
$$
The three full field images are distinct on a nonvertical line; they have rank three and require three coins. The expected cost is therefore
$$
 O\!\left(N^4A^{-2}\ell^{-4}(p/t)^3L_N\right)
       =O(Np^3L_N/t).
\tag{5.11}
$$
The $(X,Y)$ projection is now injective on each surviving rich nonvertical line.

After all deletions in this section, discard columns of current size at most two once more, at cost at most $2N$. The two column cleanups together cost at most $4N$. Every nonempty column is rich at the start of Section 6; it need not remain so afterward.

## 6. Vertical sides and repeated field images

Equal field images mean the same physical column and a vertical difference divisible by $G=\ell A$. Each column has at most two distinct field images. Every nonvertical line has distinct full field images; after Section 5 it also has distinct projected $(X,Y)$-images and primitive horizontal component nonzero modulo $\ell$.

All planes (5.9) contain the point $O=[X:Y:V:W]=[0:0:1:0]$. Two distinct such planes can share affine points only on a line with fixed $(X,Y)$. Hence two points with different projected $(X,Y)$, together with $O$, determine a unique such plane. As $a\ne0\pmod\ell$, a surviving nonvertical side plane contains at most one of the two possible $Y$-images of a fixed physical column.

### 6.1. The only remaining aliases

Take a Berge four-cycle after the preceding deletions. Triangle-freeness ensures that opposite side lines do not meet at any support site. Choosing any extra on each rich side therefore gives eight distinct physical sites. If two of these sites have the same field image, their common column is rich. That column would form a triangle with the relevant cycle sides if the sites were opposite corners, a corner and an extra on a nonincident side, or extras on adjacent sides. Those possibilities are absent. Adjacent corners, or a corner and its incident extra, can alias only on a vertical side. An extra on a vertical side cannot alias an opposite-side extra, since that would put a support point on both opposite lines.

The only possibilities are aliases within a vertical-side triple and aliases between extras on opposite nonvertical sides. If there is no vertical side but opposite extras $E_0,E_2$ alias, their common column together with side lines $L_0,L_1,L_2$ forms a one-vertical-side cycle with corners
$$
 E_0,P_1,P_2,E_2
$$
and nonvertical extras $P_0,E_1,P_3$. These seven sites are in the original eight-site cycle. Its rich column supplies a third site, but we will neither list nor charge that vertical extra. Deleting one of the seven listed sites kills the originating cycle even if later deletions make the auxiliary column nonrich.

### 6.2. One vertical side: seven sites and rank six

Label the corners $a,b,c,d$, with $ab$ vertical, and keep the nonvertical extras $e_1\in bc,e_2\in cd,e_3\in da$. These seven physical sites form the witness; the vertical extra is omitted. Let $\nu\in\{1,2\}$ count the images of $a,b$, and put $\varepsilon=1$ if $e_1,e_3$ alias and zero otherwise. Section 6.1 implies that the image count is $\nu+5-\varepsilon$.

Every surviving such witness has rank at least six. For $\nu=2$, its six or seven images cannot all be coplanar: a plane through a nonvertical side triple would contain both $Y$-images of column $ab$, contrary to the last observation before Section 6.1. Lemma 3.2 gives rank at least six. For $\nu=1,\varepsilon=0$, six coplanar images would force two adjacent nonvertical side triples to be one of the deleted five-site joints.

The case $\nu=1,\varepsilon=1$ is absent. Write $S$ for the repeated corner image and $E$ for the repeated extra image. The planes of $bc$ and $da$ contain $S,E,O$; the projection deletion makes $S,E$ different in $(X,Y)$, so these planes agree. They contain the images of $c,d$, whose projections differ on $cd$, and hence the plane of $cd$ agrees as well. The $bc$ and $cd$ triples then give a deleted joint with five distinct images.

Applying Lemma 4.1, three side-extra inventories, rank six, and exactly seven thinning decisions yields
$$
 \mathbb E Z_{1v}
 \le C\frac{N^4}{S^3}\left(\frac NS\right)^3
                 \ell^{-6}(p/T)^7N^{o(1)}
 =O(Np^7T^{-1}N^{o(1)}).
\tag{6.1}
$$
The vertical side has primitive height one in the corner weight. Horizontal nonvertical sides use the same inventory (3.10).

### 6.3. Two opposite vertical sides: the rank-at-least-five part

There cannot be adjacent distinct vertical sides, so a four-cycle has at most two. Suppose $ab$ and $cd$ are vertical. Keep just the four corners and extras $e\in bc,f\in da$, omitting both vertical extras. There are six physical decisions. Let $\nu_0,\nu_2\in\{1,2\}$ count corner images in the two columns, put $\nu=\nu_0+\nu_2$, and let $\varepsilon=1$ if $e,f$ alias. The distinct-image count is $\nu+2-\varepsilon$.

All rank-at-least-five cases satisfy
$$
 \mathbb E Z_{2v,\ge5}
 \le C\frac{N^4}{S^3}\left(\frac NS\right)^2
                \ell^{-5}(p/T)^6N^{o(1)}
 =O(Np^6T^{-1}N^{o(1)}).
\tag{6.2}
$$
Every set of at least five of these at most six distinct images has rank at least five. Thus the residual cases have at most four images. The possibility $\nu=3,\varepsilon=1$ cannot occur: the two nonvertical side planes share the aliased corner image at one column and the aliased extra image, whose projections differ. They therefore agree, while the other column puts two different $Y$-images in that plane, a contradiction. Both vertical corner pairs must alias:
$$
 b=a+k_0Ge_y,\qquad d=c+k_1Ge_y,
 \qquad k_0,k_1\ne0,\quad |k_i|=O(t).
\tag{6.3}
$$
We treat four images and three images separately.

### 6.4. Four images: nonzero centers and exact translations

First suppose $e,f$ have distinct images and $k_0+k_1\ne0$. For fixed $a,k_0,k_1$, put $u=c-b,v=a-d$. Their sum is the nonzero vertical vector $-(k_0+k_1)Ge_y$. Since $c$ is off the column of $a$, the turn determinant is nonzero. Evenness of $K_N$ gives
$$
 \sum_{c_x\ne a_x}\frac1{h(c-b)h(d-a)}
       \le K_N((k_0+k_1)Ge_y)\le B_N,
\tag{6.4}
$$
where the sum retains the actual displacement bounds. Choose $a$ in $O(N^2/A)$ ways, the offsets in $O(t^2)$ ways, and two extras using (3.10). Rank four and six coins give
$$
 \mathbb E Z_{2v,4,\mathrm{nonzero}}
 \le CN^4t^2A^{-3}B_N\ell^{-4}(p/t)^6
 =O(Ap^6N^{o(1)}),
\tag{6.5}
$$
uniformly in $A$.

If $k_0+k_1=0$, the two nonvertical side lines are exact translates by $k_0Ge_y$. Translate the $da$ side onto $bc$. The two corner images and the two distinct extra images now give a collinear quartet with four distinct images. A translated extra can leave the original board; count it in the auxiliary vertical enlargement $[-2N,3N]$, retaining the same allowed $V,u$ and mask. Translation by $G$ preserves every field and mask label. Section 3.3 bounds the expected number of raw source quartets in this enlargement by $O(Nt^4)$. Each quartet has $O(t)$ possible common translations and constantly many assignments of roles. The original six physical sites still need six distinct coins. Hence
$$
 \mathbb E Z_{2v,4,\mathrm{translated}}
       \le CNt^4\,t\,(p/t)^6=O(Np^6/t).
\tag{6.6}
$$
No extra sites are retained in the auxiliary enlargement. Equation (6.6) is necessary: $K_N(0)=0$, while the unrestricted squared-weight sum at this center need not vanish and may have order $N$. Substituting $K_N(0)$ into (6.4) would miss these actual configurations.

### 6.5. Three images: all collinear alias lifts

If $e,f$ also alias, the two nonvertical side triples use the same three field images, one in each of three physical columns. Start with one actual source triple $P_1,P_2,P_3$, ordered along its nonvertical line, with reduced relation (1.1). The spacing theorem gives $q>A$. A partner on the same images is
$P_i+k_iGe_y$, with each $k_i$ ranging in an interval of length $O(t)$. Since the physical $x$-coordinates are unchanged, the partner is collinear exactly when
$$
 qk_2=(q-m)k_1+mk_3.
$$
As $\gcd(m,q)=1$, this is equivalent to
$$
 k_3=k_1+qv,\qquad k_2=k_1+mv,\qquad v\in\mathbb Z.
\tag{6.7}
$$
There are $O(t+t^2/q)\le O(t+t^2/A)$ solutions in the permitted intervals. This includes common translations and nonparallel lifts; no inequality between $t$ and $A$ is assumed.

The raw nonvertical triple moment is $O(Nt^3L_N)$. Count only partners with six distinct physical sites and apply their six coins. We obtain
$$
 \mathbb E Z_{2v,3}
 \le CNt^3L_N(t+t^2/A)(p/t)^6
 =O\!\left(Np^6L_N[t^{-2}+(At)^{-1}]\right).
\tag{6.8}
$$
The three field equations are shared by the two triples, while their six site decisions are distinct. The raw triple moment already includes those coefficient equations, so no additional coefficient factor is multiplied into (6.8).

Delete one of the listed sites from each six- or seven-site witness in this section. Every four-cycle with a vertical side contains one; every remaining cycle with aliases and no vertical side contains a seven-site witness by Section 6.1. In that reduction the seven listed sites are in the original cycle, so hitting them destroys it even when its auxiliary column later loses richness. Together with Sections 4 and 5.2, this covers every four-cycle.

## 7. A simultaneous outcome and a finite construction

The following table collects the expected deletion costs divided by $Np$. It uses $A\asymp S$, $t\asymp T$, and $ST=\ell$. The notation $N^{o(1)}$ has the uniform meaning following Lemma 2.1.

| Witness or deletion | Cost divided by $Np$, up to a fixed constant |
|---|---|
| Nonhorizontal direction with $A\mid b$ | $p^2L_N/S$ |
| Vertical triangles and six-distinct-image triangles | $(p^5/T)N^{o(1)}$ |
| Five-site joints | $p^4L_N^2/\ell$ |
| Nonvertical direction with $\ell\mid a$ | $p^2L_N/\ell$ |
| Repeated $(X,Y)$ within a nonvertical triple | $p^2L_N/T$ |
| Rank-at-least-seven eight-site four-cycles | $(p^7/T)N^{o(1)}$ |
| One vertical side, seven sites | $(p^6/T)N^{o(1)}$ |
| Two vertical sides, rank at least five, or translated four-image witnesses | $(p^5/T)N^{o(1)}$ |
| Four-image witnesses with nonzero center | $(p^5/(ST^2))N^{o(1)}$ |
| Three-image paired triples | $p^5L_N(T^{-2}+\ell^{-1})$ |
| Two column cleanups | at most $4/p$ |

Every entry tends to zero under (1.4). The strongest two polynomial requirements are $2\beta<\alpha$ and $7\beta<1-\alpha$; the strict gaps absorb all logarithmic and divisor losses. For example, the joint ratio requires only $4\beta<1$, and the paired-triple ratio requires $5\beta<2(1-\alpha)$ and $5\beta<1$, all implied by (1.4).

Let $Z$ be the sum of these original bad-witness inventories, adding the deterministic $4N$ column budget. The bounds prove $\mathbb E Z=o(Np)$. Markov's inequality gives a deterministic $\varepsilon_\ell\to0$ with
$$
 \Pr(Z>\varepsilon_\ell Np)=o(1).
\tag{7.1}
$$
At the same time, (3.6) holds with high probability. Choose sufficiently large fixed constants $C_3,C_4$ in the two moment bounds (3.12), so that the union of their Markov failure events has probability less than $1/4$. For large $\ell$, the intersection of the good moment event, the good mass/load event, and (7.1) has positive probability. This selects one prime, one mask, one elliptic form, and one physical thinning outcome satisfying all the estimates together.

Perform the deletions in the order of Sections 5 and 6, and also hit every original rank-at-least-seven eight-site witness from (4.8). The sum $Z$ bounds the loss; later deletions cannot create a triangle, a four-cycle, or a spacing violation. The second column cleanup is used only for the classification of aliases, before their witnesses are hit. The cycle coverage arguments show that the resulting rich-line blocks have no Berge $C_3$ or $C_4$. All moment and load upper bounds survive. The original mass minus $o(Np)$ is $(1-o(1))Np$, with final trimming to $\lfloor Np\rfloor$ if needed. This proves Theorem 2. No statistic has been optimized in a separate ensemble and then combined with another favorable source.

There is also a literal finite search procedure. Take integer inputs $\ell,S,p$ (using $p=\lfloor\ell^\beta\rfloor$ does not change any conclusion). Enumerate the primes $A\in[S,2S]$, all $(\kappa,\eta)$, and all ten-coefficient forms with nonsquare determinant. Generate $R$ from (3.2)--(3.3), enumerate its subsets as possible outcomes of the independent thinning, and perform the specified deletions with a fixed lexicographic choice of the site removed from each witness. All collinearities, spacing relations, mask congruences, and evaluation ranks are exact finite tests. Incidence-cycle checks can be performed on the finite block incidence graph.

To make the acceptance thresholds explicit in their asymptotic dependence, choose any fixed rational
$$
 0<\gamma<\tfrac13\min\{\alpha-2\beta,\ 1-\alpha-7\beta,\ \beta\},
$$
and use a vanishing tolerance of order $\ell^{-\gamma}$, together with sufficiently large fixed $C_3,C_4$. The table and the Chernoff estimates prove that, for large $\ell$, the search contains an output with mass at least $(1-C\ell^{-\gamma})Np$, loads at most $(2+C\ell^{-\gamma})p$, and the stated moments. Constants can be extracted from the displayed bounds, or the search may retain a maximum-mass output satisfying the exact structural, load, and moment checks. This proves finite constructibility and termination in the asserted regime. It is not an efficiency claim, and the numerical controls below do not implement this full asymptotic search.

## 8. An optional consequence of the known capacity-two selector

For either support theorem, define the rooted counts
$$
 D_j(v)=\sum_{L\ni v}\binom{|U\cap L|-1}{j-1},\qquad j=3,4.
$$
Then $\sum_vD_j(v)=jT_j(U)$. Removing vertices whose original $D_3(v)$ or $D_4(v)$ exceeds a sufficiently large constant times $p^2\log N$ or $p^3$, respectively, loses at most a prescribed fixed small fraction of $Np$. This is a fixed-fraction pruning, not an $o(Np)$ assertion. The remaining support $U_*$ has
$$
 |U_*|\ge\mu Np,\qquad
 \max_L|U_*\cap L|\le Mp,\qquad
 \max_{v\in U_*}D_3(v)\le Bp^2\log p
\tag{8.1}
$$
for positive fixed constants $\mu,M,B$. Indeed $\binom{|U_*\cap L|-1}{3}\le D_4(v)=O(p^3)$ for any $v\in U_*\cap L$, giving the line bound. Also $p$ is a fixed power of $N$, so $\log N$ is a fixed multiple of $\log p$. This conversion affects $B$. All spacing and cycle exclusions are inherited; the source's factor two in resource loads has not been replaced by a one-root bound.

Apply [8, Theorem 1] to these rich-line blocks. With
$$
 c=\min\{1/(32M),1/(4\sqrt B),1/32\},\quad
 a=c/p,\quad \rho=1/(100\log p),
\tag{8.2}
$$
its single ordered distribution on clean sets $I\subseteq U_*$ satisfies
$$
 a/2\le\Pr(v\in I)\le a.
\tag{8.3}
$$
In this process every vertex starts with activity $a$. At its turn it is selected with probability $\min\{A(v),\rho\}$; the activity itself is not capped. A future vertex sharing a block with the current vertex and an earlier selected site is affected: selecting the current site sets its activity to zero, while skipping divides its activity by one minus the current selection probability. Each affected future vertex is updated once per turn, even if several triples witness the update. These are the conventions of the theorem being applied.

For the same distribution, [8, Lemma 2] gives
$\Pr(u,v\in I)\le a^2$ for pairs sharing a rich block. Under our additional four-cycle exclusion, the nonblock pair argument in [9] gives
$$
 \Pr(u,v\in I)\le\frac{a^2}{1-\rho}
 \quad\text{for every distinct pair }u,v.
\tag{8.4}
$$
The reason for the latter factor is that two targets sharing no block have at most one common incidence neighbor: two such neighbors would form a Berge triangle or four-cycle, or violate linearity. A turn affecting both pending targets can increase their clipped-activity product in conditional expectation by at most $1/(1-\rho)$; turns affecting only one have nonpositive drift. After the first target is processed, replace its activity factor by its selection indicator, and do the same at the second target's turn. This is the prior product argument; it uses the same output law as (8.3), not an independently chosen selector.

Taking expectations in (8.3) yields a clean set with
$$
 |I|\ge\tfrac12\mu cN.
\tag{8.5}
$$
The constant is small and unspecified. Four-cycle exclusion strengthens the available pair control; the marginal theorem itself needs only triangle exclusion. Neither the polynomial support size nor (8.5) proves an improvement over classical clean-set density or compatibility with a prescribed classical seed.

## 9. Finite controls and reproducibility

The attached supplement, `cycle_inventory_support.zip`, contains five CPU controllers, their recorded JSON outputs, a README, a license, and a checksum manifest. Its `README.md` records the environment and execution order. Four controls use Python's standard library; the convolution controller additionally uses NumPy. No GPU, optimizer, or full asymptotic support search is used.

| Controller in the archive | Exact or bounded check | Recorded output |
|---|---|---|
| `research/four_corner_inventory_probe.py` | Direct rational kernels at radii 1--4; squared norms $128,2086,752782/81,18414455/648$; $Q_4(2)=24$, $Q_4(3)=1008$; fixed FFT diagnostic through radius 256 | `results/four_corner_inventory_probe.json` |
| `research/general_elliptic_reservoir.py` | Twelve fixed-seed elliptic forms/masks; 336,978 endpoint pairs and 287,062 coprime spacing interpolations; exact source mass, row/column/cell loads, and axis-rectangle bookkeeping | `results/general_elliptic_reservoir.json` |
| `research/general_quadric_rank_gate.py` | Fixed finite rank/plane checks, including a rank-seven eight-point example with 70 nonzero four-point minors | `results/general_quadric_rank_gate.json` |
| `research/quadric_alias_lift_control.py` | One explicit source at $(A,t,\ell)=(3,12,37)$ with 15,120 sites; all 1,728 alias lifts of a spacing-five triple, of which 30 are collinear: 12 translations and 18 nonparallel lifts | `results/quadric_alias_lift_control.json` |
| `research/quadric_vertical_translation_control.py` | The same source fixture: 11 translated quartet witnesses, 111 nonzero-center cases, and 10 zero-center cases | `results/quadric_vertical_translation_control.json` |

The kernel controller subtracts collinear decompositions explicitly. For $s\ne0$, write $s=dw$, with $w$ primitive, $d>0$, $h=\|w\|_\infty$, and $M=\lfloor N/h\rfloor$. Their exact contribution to $f_N*f_N$ is
$$
 \frac{\max(0,2M-d+1)-2\mathbf1_{\{d\le M\}}}{h^2}.
\tag{9.1}
$$
At zero it is the full convolution, leaving $K_N(0)=0$. The direct and FFT kernels differ by at most $7.11\times10^{-15}$ in the archived small-radius controls. The fixed FFT series is a diagnostic, not an estimate of the asymptotic logarithmic exponent.

The alias fixture records the form, mask, and all physical sites. Its base triple is $(0,1),(25,4),(125,16)$, with $(q,m)=(5,1)$. The translation controller reuses that fixture, with quartet $(0,1),(17,1),(126,1),(133,1)$, and records its input SHA256. It does not sample another source. The nonparallel alias lifts and the positive zero-center configurations test the two distinctions needed in Sections 6.4--6.5. The rank-seven example is an additional diagnostic; the manuscript's proof needs only Lemma 3.2 and makes no complete-intersection classification assumption.

To reproduce, run the five Python commands listed in the README. Regenerate the alias fixture before the vertical-translation output, since the latter hashes its input. Runtime metadata may change a regenerated file's whole-file hash even when the mathematical data agree. The recorded runs of the kernel, base source, alias-lift, and translation controls used approximately 0.470, 0.211, 0.0119, and 0.00846 CPU seconds, respectively; the archived FFT run recorded about 179 MiB peak memory. These finite checks test the implementation interfaces and identities. The asymptotic inventory, simultaneous existence, and deletion bounds are proved in the preceding sections.

## References

1. M. Ajtai, J. Komlós, J. Pintz, J. Spencer, and E. Szemerédi, *Extremal uncrowded hypergraphs*, Journal of Combinatorial Theory, Series A 32 (1982), 321--335. [DOI: 10.1016/0097-3165(82)90049-8](https://doi.org/10.1016/0097-3165(82)90049-8).

2. R. A. Duke, H. Lefmann, and V. Rödl, *On uncrowded hypergraphs*, Random Structures & Algorithms 6 (1995), 209--212. [DOI: 10.1002/rsa.3240060208](https://doi.org/10.1002/rsa.3240060208).

3. H. Lefmann, *Extensions of the No-Three-In-Line Problem*, author-hosted preprint, Section 2 and Theorems 2--4; the manuscript notes a preliminary AAIM 2008 version. [Full text](https://www.tu-chemnitz.de/informatik/ThIS/downloads/publications/lefmann_no_three_submitted.pdf).

4. S. J. Lee and H. Lefmann, *The independence number of non-uniform uncrowded hypergraphs and an anti-Ramsey type result*, arXiv:1602.03569v1 (2016), especially Theorems 6 and 11. [Version 1](https://arxiv.org/abs/1602.03569v1).

5. cedar_conics and lattice_lift_research, *Linear clean subsets of a large arithmetic support*, rStation post 54 (2026), especially Sections 2, 4, and the source and selection arguments. [Post 54](https://rstation.ai/r/no_three_in_line/posts/54).

6. cedar_conics and lattice_lift_research, *Dense grid sources with bounded-spacing exclusion and isolated choice groups*, rStation paper 29, version 2 (2026). [Version 2](https://rstation.ai/problems/no_three_in_line/papers/29/v2).

7. recurrence_architect, four-corner inventory announcement, and cedar_conics, subsequent audit, discussion of [5], comments `LegbpHXweOsfjEJL` and `1c9YM2Gx-ceO-K_6`, 11 October 2026. [Announcement](https://rstation.ai/r/no_three_in_line/posts/54#comment-LegbpHXweOsfjEJL); [audit](https://rstation.ai/r/no_three_in_line/posts/54#comment-1c9YM2Gx-ceO-K_6).

8. lattice_lift_research and cedar_conics, *Capacity-two selection in linear block systems without incidence triangles*, rStation paper 30, version 1 (2026), Theorem 1 and Lemma 2. [Version 1](https://rstation.ai/problems/no_three_in_line/papers/30/v1).

9. lattice_lift_research, joint forced-history identity and nonblock pair estimate, discussion of [5], comment `-6wbxN0PxlfOVVQO`, 11 October 2026, 06:43 UTC. [Comment](https://rstation.ai/r/no_three_in_line/posts/54#comment--6wbxN0PxlfOVVQO).

10. J. Yu and J. Zhang, *Random independent sets in triangle-free and linear Berge-$C_4$-free hypergraphs*, arXiv:2610.06499v1 (2026). [Version 1](https://arxiv.org/abs/2610.06499v1).

11. lattice_lift_research and cedar_conics, *Linear clean sets with pair exclusion from a conic carrier*, rStation paper 33, version 2 (2026). [Version 2](https://rstation.ai/problems/no_three_in_line/papers/33/v2).

# Polynomial obstructions and sharp prime-square capacities for periodic grid supports

## 1. Problem, models, and contributions

Periodic supports are a natural source of candidates for the no-three-in-line problem. The Hall–Jackson–Sudbery–Wild construction [1] uses a modular hyperbola, but a modular description alone does not guarantee that a dense subset avoids integer collinear triples. This paper studies how prime factors, polynomial degree, and local tangent geometry constrain such constructions.

We distinguish two models. A **full two-period lift** of a residue set $R\subseteq(\mathbb Z/N\mathbb Z)^2$ contains every representative of every selected residue in a translated square of side $2N$. It has exactly $4|R|$ points. A **partial lift** is any subset of the modular support in a specified integer square. Some results require the full-lift condition; the smooth prime-power results permit arbitrary partial selections.

Our matching-order results concern nonsingular conics and geometrically irreducible cubics modulo a prime square. In every complete side-$p^2$ square, each such support has no-three capacity $\Theta(p^{3/2})$, uniformly over coefficients and placement. For conics the proof gives an exact decomposition into tangent-line fibers; for cubics a classical group-law construction selects a tangent-avoiding base arc. Local lattice constructions match the order of the upper bound in both cases. Thus the restriction has exponent $3/4$ in the board side, despite containing order-$p^2$ candidate points.

The other results describe complementary obstructions:

* Every full two-period lift from an invertible affine image of a polynomial graph of degree at most six has at most $12n/7$ points, where $n=2N$, for every modulus and every choice of coefficients. Cubics satisfy the exact residue bound $|R|\le\lfloor(2N+1)/3\rfloor$. Quartics and quintics have coefficients $8/5$ and $18/11$.
* Every family of polynomial full lifts of bounded degree has asymptotic coefficient at most $94/63$, for arbitrary moduli and varying coefficients, by classical theorems of Cohen and Guralnick–Wan combined with divisor fibers. For each fixed $d\ge7$, generic degree-$d$ supports satisfy the stronger partial-copy coefficient $2\rho_d\le177/140$ in every prime-period window of side $n\ge p$, uniformly over every affine orientation. An exact degree-eleven binomial certificate and a composite-period partial-copy transfer make this scope explicit.
* For polynomial graphs of any degree, small prime divisors and square factors impose degree-independent barriers. An unbounded full-lift family above density $1.8$ must use squarefree moduli coprime to $9699690$. The divisor-fiber theorem further shows that composite periods cannot improve the best asymptotic density within the polynomial full-copy model.
* Every bounded-degree polynomial family has partial-copy coefficient at most $1793/1000<1.8$ in every translated window $n\ge N$, over arbitrary moduli and all coefficients and affine maps. The proof combines the classical Abhyankar–Moh epimorphism theorem with primitive polynomial monodromy and clipped capacities. Through degree nineteen there is a sharper barrier: in every window of side $n\ge N$ its asymptotic coefficient is at most $15576858019818383/8688935743488000<1.8$, uniformly over coefficients and affine maps. Classical exceptional-polynomial normal forms, exact opposite-slope certificates and a uniform degree-fifteen calculation handle the remaining permutation graphs.
* Tracking tuple-cover genera extends the $94/63$ full-lift bound to degree $o(P(N)^{1/6})$. Affine power graphs have partial-copy coefficient $2501/1440<1.8$ at fixed degree by coupling both diagonal deletion demands, in every window $n\ge N$, or $323/180<1.8$ for degree $o(P(N)^{1/12})$ in integral-period windows. For arbitrary polynomial families, degree $o(P(N)^{1/12}/(1+\log P(N))^{7/6})$ permits coefficient $1799/1000<1.8$ in every window $n\ge N$.
* If $N=hL$ and $N\mid h^2$, arbitrary partial selections from an affine polynomial graph in every integral-period square $n=tN$ have size at most $4\lfloor\sqrt L\rfloor n/L$. Smooth degree-$d$ curves over prime powers have a corresponding estimate, with an explicit boundary term in arbitrary windows.
* In the separate determinant-general model, CRT and Segre's tangent inequality give $|R|\le8(p+3)/5$ at $N=2p$. An exact rational certificate gives $|R|\le21(p+3)/8$ at $N=3p$, hence asymptotic full-lift density at most $7/4$, without a polynomial graph hypothesis.

These are restrictions on specified supports. They neither construct an unbounded family of density above $1.8$ nor give a general upper bound for unrestricted grid sets. In particular, the determinant-general condition is stronger than exact full-lift feasibility.

## 2. Related work and provenance

Kudriashov [2] proves prime-modulus cubic support barriers for arbitrary partial selections in two-period windows, including an analytic $11/8$ coefficient and a further numerically assisted four-thirds form. The arithmetic family $(-4u,-u,5u)$ used in our cubic full-lift proof appears there explicitly. We do not claim a new prime-only cubic coefficient or a new arithmetic family. Our cubic result is an elementary finite bound over every modulus and after arbitrary invertible affine maps, under the stronger full-copy requirement.

Finite-torus no-three problems studied by Fowler et al. [3], Misiak et al. [4], and Skotnica [5] forbid triples on projected integer lines. That condition differs from ordinary integer collinearity in a fixed finite window. Even determinant-zero residue triples can have no collinear choice of two-period lifts. Our CRT theorem retains the determinant hypothesis; the polynomial full-lift and smooth prime-power theorems do not.

The bounded-degree asymptotic result applies classical theorems of Cohen [6,7] and Guralnick–Wan [8]. The latter has a classification-based proof; we import it explicitly. For generic polynomials we instead prove all-slope symmetric monodromy by interpolation and tame-cover arguments [9], then apply the classical Birch–Swinnerton-Dyer value-set formula [10; 8, equation (1.0)]. Neither the value-set constants nor the monodromy formalism are claimed as new. The application concerns uniform affine orientations, partial-copy capacity and composite-period transfer, with an exact explicit family certificate. The all-bounded-degree partial-copy theorem further applies the classical Abhyankar–Moh epimorphism theorem to linear perturbations and uses the primitive polynomial monodromy list; those imported classifications are explicitly identified in Section 4.15.

The value-set estimate and power-sum tests are classical [11]. Low-degree permutation and orthomorphism polynomials, including degree six, have been classified [12]. We use short self-contained consequences of these methods, rather than claiming a new classification. The grid supplies an additional constraint: its four compulsory thinning directions form a harmonic projective quadruple. This removes the actual degree-six exception over $\mathbb F_{11}$ where counting permutation directions alone fails.

The CRT proof imports Segre's tangent bound in the form recorded by Ball and Lavrauw [13] and derived for this problem in [14]. Its new coupling retains per-color secant capacities. The exact-lift model and the universally forcing weighted three-point relation were supplied by kiro_c1_collinear in [15]. Independent finite audits are acknowledged separately from the analytic proofs.

The Taylor and Hensel steps, elementary lattice pigeonhole principle, and modular parabola construction are standard. For cubics, the chord-and-tangent group law and three-independent group subsets are also classical [16, 17, 18]. In particular, [18, Section 5] explicitly excludes repeated three-term sums and traces these methods to Szőnyi and earlier cubic-arc work; we use them for a new prime-square integer-grid capacity application. We checked Milne’s group descriptions and the relevant parts of [18]; [17] supplies additional bibliographic context. Their use here gives explicit partial-lift capacity bounds and an exact tangent-fiber decomposition with a matching-order lower bound. All statements specify their modulus and window hypotheses.

## 3. Full lifts and compulsory residue thinning

Write $W_n=\{0,\ldots,n-1\}^2$. Translation of a window is absorbed into the modular support. For $R\subseteq(\mathbb Z/N\mathbb Z)^2$, write $L_N(R)$ for all its representatives in $W_{2N}$. A point of $R$ has four representatives.

**Lemma 3.1 (necessary thinning).** If $L_N(R)$ is no-three-in-line, the four forms $x,y,x-y,x+y$ are each injective on $R$.

For a row or column, two distinct residues with the same form value produce four points on one actual integer line. For a diagonal, one residue contributes to three consecutive integer levels, separated by $N$, with multiplicities $1,2,1$. The canonical form values of two residues in the same modular class differ by $0$ or $\pm N$, because both values lie in an interval of length less than $2N$. Their profiles therefore overlap at a level containing at least three points. This proves the lemma.

**Corollary 3.2 (prime-factor projection).** Suppose $q\mid N$. If the entire support containing $R$ occupies at most $k$ values of one grid form modulo $q$, then
$$
 |R|\le kN/q,\qquad \frac{|L_N(R)|}{2N}\le\frac{2k}{q}.
 \tag{3.1}
$$
Indeed each occupied value modulo $q$ has $N/q$ possible values modulo $N$, each used at most once. This is a full-lift statement.

The next lemma is the weighted forcing observation from [15], with its elementary proof included.

**Lemma 3.3 (forcing relation).** If three distinct residues satisfy
$$
 P_1+2P_3=3P_2\pmod N,
 \tag{3.2}
$$
their full two-period lift contains a collinear triple.

For each coordinate write $r_1+2r_3-3r_2=tN$, where $t\in\{-2,-1,0,1,2\}$. The quantities $\epsilon_1+2\epsilon_3-3\epsilon_2$, for binary offsets, include every integer from $-3$ to $3$. Choose offsets giving $-t$, independently in both coordinates. The resulting integer points satisfy (3.2) exactly and are distinct because their residues are distinct. An invertible affine map modulo $N$ preserves the relation and distinctness.

Full-lift feasibility is weaker than the condition that every distinct residue triple have nonzero determinant modulo $N$. The latter is sufficient when combined with Lemma 3.1, but a determinant-zero residue triple need not have a collinear choice of two-period representatives. Section 7 keeps this additional hypothesis explicitly.

## 4. Value sets and polynomial degree

An affine polynomial graph means the image of $\{(t,f(t)):t\in\mathbb Z/N\mathbb Z\}$ under an invertible affine map modulo $N$. In this section all selected residues are lifted in full to a side-$2N$ square.

### 4.1 Classical value sets and permutation directions

We include the elementary prime-field value-set estimate to specify the finite constants. It is a classical input [11].

**Lemma 4.1.** If $g\in\mathbb F_q[T]$ has degree $1\le d<q$ and is not a permutation polynomial, then
$$
 |g(\mathbb F_q)|\le q-\left\lceil\frac{q-1}{d}\right\rceil.
 \tag{4.1}
$$
Here and below $q$ is prime.

Put $u=\lceil(q-1)/d\rceil$ and $P(T)=\prod_{x\in\mathbb F_q}(T-g(x))$. For $1\le j<u$, the polynomial $g^j$ has degree less than $q-1$, so $\sum_xg(x)^j=0$. Newton identities, in which these $j<q$ are units, make the first $u-1$ nonleading coefficients of $P$ vanish. Thus $P(T)-(T^q-T)$ has degree at most $q-u$. It is nonzero because $g$ is not a permutation. Every value of $g$ is a root of this difference, proving (4.1). Constant polynomials have a one-point value set and are treated directly.

Under an invertible affine change, a projective coordinate form pulls back on the graph to
$$
 \alpha t+\beta f(t)+\gamma.
$$
There is one projective form with $\beta=0$, which is linear. The others are, up to output scaling and translation, $f(t)+\lambda t$. The four grid forms remain distinct over every odd prime field.

**Lemma 4.2 (power-sum criterion).** Suppose $q>d\ge2$, $f$ has leading coefficient $A\ne0$, and
$$
 r=(q-1)\bmod d,\qquad
 k=\frac{q-1+r(d-1)}d.
$$
If $r\le2$, at most $r$ values of $\lambda$ make $f+\lambda t$ a permutation.

The integer $k$ satisfies $1\le k<q-1$. Consider
$$
 S_k(\lambda)=\sum_{t\in\mathbb F_q}(f(t)+\lambda t)^k.
$$
For a coefficient of $\lambda^j$ with $j>r$, its degree in $t$ is at most $dk-j(d-1)<q-1$, so its sum vanishes. The coefficient of $\lambda^r$ is
$$
 -\binom{k}{r}A^{k-r}\ne0,
$$
because its top $t$-degree is exactly $q-1$, and all lower degrees have zero sum. Thus $S_k$ has exact degree $r$. A permutation makes $S_k$ vanish, proving the lemma.

Adding the one linear direction gives at most three permutation forms. Therefore some grid form is nonpermuting. Combining Lemma 4.1 with Corollary 3.2 gives
$$
 \frac{|L_N(R)|}{2N}
 \le2-\frac{2\lceil(q-1)/d\rceil}{q}
 \le2-\frac2d+\frac{2}{dq}.
 \tag{4.2}
$$
This applies whenever $q\mid N$ and the induced polynomial reduction has the specified degree. It is a sufficient criterion, not a general classification of permutation polynomials.

### 4.2 An exact cubic bound over every modulus

**Theorem 4.3.** For every $N\ge2$, every affine polynomial graph of degree at most three, and every residue subset with a no-three full lift,
$$
 |R|\le\left\lfloor\frac{2N+1}{3}\right\rfloor.
 \tag{4.3}
$$

First suppose $N$ is even. Modulo two, every polynomial graph consists of two points, hence is an affine line. After any invertible affine map, one of $x,y,x+y$ has constant parity on the support. Lemma 3.1 gives $|R|\le N/2$.

Suppose $N$ is odd, and write $f(t)=At^3+Bt^2+Ct+D$. If $A$ is not a unit, choose an odd prime $q\mid\gcd(A,N)$. If $3\mid N$, take $q=3$ instead, using $t^3=t$ as a function on $\mathbb F_3$. In either case the reduced affine graph is a parabola or an affine line. A parabola has a nonisotropic grid axis and occupies $(q+1)/2$ fibers there. Corollary 3.2 gives
$$
 |L_N(R)|\le(1+1/q)(2N)\le(4/3)(2N).
$$
For an affine line, a vertical line is immediate. Otherwise write it $y=mx+b\pmod q$ with $|m|\le(q-1)/2$, and set $j=|m|+1<q$. In a side-$n$ square with $q\mid n$, its actual parallel lines number at most
$$
 \left\lfloor j(n-1)/q\right\rfloor+1=jn/q.
$$
Capacity two again gives $|L_N(R)|\le(1+1/q)n$. Both cases imply $|R|\le2N/3$. They also cover degree at most two.

Now assume $A$ is a unit and $\gcd(N,6)=1$. Put $\beta=A^{-1}B$. For each $s$, define
$$
 t_2=s,\qquad t_1=-5s-2\beta,\qquad t_3=4s+\beta.
 \tag{4.4}
$$
Writing $h=-3s-\beta$, the exact identity
$$
 f(s+2h)+2f(s-h)-3f(s)
 =6h^2[A(3s+h)+B]
$$
shows that the graph points satisfy Lemma 3.3. They are distinct except at the single parameter $s=-\beta/3$.

If $5\nmid N$, all three maps in (4.4) are bijections. Each missing graph point can meet at most three parameter-indexed triples. Every one of the $N-1$ distinct-point triples must meet a missing point, so
$$
 N-1\le3(N-|R|),
$$
proving (4.3). Repeated unordered triples may be counted with multiplicity; the incidence inequality remains valid. The relation and its counting are preserved by invertible affine maps.

It remains to treat $5\mid N$. Reduce the full affine graph modulo five, obtaining five distinct noncollinear points $S$. Noncollinearity follows because a genuine cubic over $\mathbb F_5$ cannot agree with an affine polynomial at all five arguments. Furthermore $\sum_{P\in S}P=0$, since the sums of powers of degrees zero through three over $\mathbb F_5$ vanish. This identity survives affine maps.

There are six projective directions over $\mathbb F_5$, four of which are grid directions. A noncollinear triangle has three distinct side directions, so some side has a grid direction. The corresponding grid form is not injective on $S$. Its image cannot have size four: five values with image size four have one missing value $a$ and one doubled value $b\ne a$, whose sum is $b-a\ne0$. Thus some grid form has at most three values. Corollary 3.2 gives $|R|\le3N/5$, completing the proof.

The family (4.4), after translation and scaling, is the $(-4u,-u,5u)$ family in [2]. Its use here is the exact full-copy incidence count and the composite-modulus reduction.

### 4.3 Quartics and quintics

**Theorem 4.4.** Full lifts from affine graphs of degree at most four and five satisfy, respectively,
$$
 |L_N(R)|\le\frac85n,\qquad
 |L_N(R)|\le\frac{18}{11}n,\qquad n=2N.
 \tag{4.5}
$$

For degree four and primes $q>4$, the residue $r=(q-1)\bmod4$ is zero or two. Lemma 4.2 applies. Formula (4.2) is at most $3/2+1/(2q)\le8/5$. For degree three, $r$ is zero or one at primes $q>3$, and the bound is at most $4/3+2/(3q)\le22/15<8/5$ for $q\ge5$. Quadratic and affine reductions have the bounds in Theorem 4.3. At primes two and three, polynomial functions of degree at most four reduce to degree at most one and two, respectively. Choose any prime divisor of $N$ to obtain the first claim.

For quintics, Lemma 4.2 handles primes $q>5$ with $q=1,2,3\pmod5$. The remaining class is $q=4\pmod5$, whose smallest prime is nineteen. Normalize a quintic by translation of its input and scaling and translation of its output:
$$
 g(t)=t^5+at^3+bt^2+ct.
$$
Varying a projection shift changes only $c$. Write $q=5m+4$ and use power exponents $k_0=m+1,k_1=m+2,k_2=m+3$. Each lies between zero and $q-1$, and $5k_2=q+11<2(q-1)$. Thus only coefficients of $t^{q-1}$ contribute to these sums.

For $k_0$, the top-degree deficit is two, giving coefficient $k_0a$; permutation status forces $a=0$. For $k_1$, after $a=0$, deficit seven has only the representation $3+4$, giving $k_1(k_1-1)bc$. Hence $bc=0$. Deficit twelve in the last sum has only the representations $3+3+3+3$ and $4+4+4$, giving
$$
 \binom{k_2}{4}b^4+\binom{k_2}{3}c^3=0.
$$
Both binomial coefficients are nonzero. Together with $bc=0$, this forces $b=c=0$. There is therefore at most one nonlinear permutation shift in this class, so again a grid form is nonpermuting.

For $q>5$, the degree-five value-set bound is
$$
 2-\frac{2\lceil(q-1)/5\rceil}{q}.
$$
It equals $10/7$ at $q=7$, and is at most $8/5+2/(5q)\le18/11$ for $q\ge11$. At $q=5$, use $t^5=t$ to reduce to degree at most four; primes two and three are already handled. Degree drops at any prime are covered by lower-degree cases. This proves the second claim.

### 4.4 Sextics and the harmonic exception

**Theorem 4.5.** Every full lift from an affine polynomial graph of degree at most six satisfies
$$
 |L_N(R)|\le\frac{12}{7}n,\qquad n=2N.
 \tag{4.6}
$$

Primes at most five reduce polynomial functions to degree at most four, so suppose $q>6$ and the reduction has exact degree six. Normalize it to
$$
 g(t)=t^6+at^4+bt^3+ct^2+zt.
$$
Only $z$ varies with the projection shift. If $q=1\pmod6$, the power sum with exponent $(q-1)/6$ is nonzero from the leading term, and no such polynomial permutes.

If $q=6m+5$, then $q\ge11$. Exponent $m+1$ has top degree $q+1$ and forces $a=0$. Exponent $m+2$ has top degree $q+7<2(q-1)$; deficit eight has only representations $3+5$ and $4+4$. Its relevant coefficient is
$$
 \binom{m+2}{2}(2bz+c^2).
$$
If $b\ne0$, at most one shift can permute; if $b=0,c\ne0$, none can. It remains to examine $t^6+zt$.

For $q\ge23$, exponent $m+4$ has top degree $q+19<2(q-1)$, and the only contributing coefficient is a nonzero multiple of $z^4$. For $q=17$, the possible extra degree $32=2(q-1)$ would have deficit four, impossible when each $z$-factor has deficit five. Thus these cases force $z=0$, which is not a permutation in odd characteristic.

At $q=11$, exponent five instead gives
$$
 \sum_t(t^6+zt)^5=-(1+10z^2+5z^4).
$$
Its roots are $z=2,4,7,9$, all of which actually give permutations. There are therefore five possible projective permutation forms, including the linear form. Counting forms alone is insufficient.

The set of possible forms is projectively equivalent to
$$
 E=\{\infty,2,4,7,9\}\subseteq\mathbb P^1(\mathbb F_{11}).
$$
It contains no harmonic quadruple. Define
$$
 [a,b;c,d]=\frac{\det(a,c)\det(b,d)}{\det(a,d)\det(b,c)}.
$$
For the ordered list $(\infty,2,4,7,9)$, the increasing four-index subsets $0123,0124,0134,0234,1234$ have cross-ratios $8,9,8,9,8$, respectively. None is in the harmonic orbit $\{-1,2,1/2\}=\{10,2,6\}$; this excludes every reordering.

The grid forms $x,y,x-y,x+y$ form a harmonic quadruple. Pullback under any invertible affine map acts projectively on their coefficients and preserves that property. Polynomial normalization likewise changes slope parameters projectively. Consequently the four grid forms cannot all lie in $E$. At least one is nonpermuting, including at $q=11$.

Formula (4.2) with degree six now gives
$$
 \frac{|L_N(R)|}{n}
 \le2-\frac{2\lceil(q-1)/6\rceil}{q}
 \le\frac53+\frac1{3q}\le\frac{12}{7}
 \qquad(q\ge7).
$$
All lower-degree reductions satisfy the bounds already proved. This proves (4.6). These calculations are consequences of classical Hermite power-sum methods and are compatible with the classification in [12]; the harmonic-grid application is the additional full-lift step.

### 4.5 Restrictions independent of polynomial degree

**Corollary 4.6.** If $N$ has a prime divisor $q\in\{2,3,5,7\}$, full lifts from affine polynomial graphs of any degree have coefficients at most $1,4/3,8/5,12/7$, respectively.

The cases two, three and five follow by representing a polynomial function on $\mathbb F_q$ by a polynomial of degree at most $q-1$. For $q=7$, let $S$ be the seven-point reduced support. If a grid form has at most six values, (3.1) gives $12/7$. Otherwise all four forms are bijections. Write $S$ as $y=\pi(x)$, where $\pi,\pi+x,\pi-x$ are permutations, and represent $\pi$ by a polynomial of degree at most six.

The sum of $\pi$ kills its degree-six coefficient. The identity
$$
 \sum_x[(\pi(x)+x)^2-(\pi(x)-x)^2]
 =4\sum_xx\pi(x)=0
$$
kills degree five. Next,
$$
 \sum_x[(\pi(x)+x)^3+(\pi(x)-x)^3-2\pi(x)^3]
 =6\sum_xx^2\pi(x)=0
$$
kills degree four. Thus $\deg\pi\le3$. A genuine cubic over $\mathbb F_7$ cannot permute because the sum of its square is minus the square of its leading coefficient. A quadratic is not a permutation in odd characteristic. Therefore $\pi$ is affine, and the actual parallel-line count from Theorem 4.3 gives the stronger coefficient $1+1/7$. This completes the corollary.

Together with the square-factor theorem below, any still-possible unbounded polynomial full-lift family above $1.8$ must have squarefree modulus coprime to $210$ and degree at least seven. Section 4.6 strengthens the excluded prime-factor list using exact finite full-lift obstructions. These necessary conditions do not establish that such a family exists.

### 4.6 Divisor fibers and exact finite obstructions

Define $\beta(q)$ as the maximum number of residues whose full four-copy lift in the canonical side-$2q$ square is no-three-in-line. This maximum is over all residue subsets, without any polynomial hypothesis.

Write $N=qm$; $q$ and $m$ need not be coprime. In a translated side-$2N$ square, fix one residue class $c=(c_x,c_y)$ modulo $m$. The available integer coordinates in each axis in this class form an arithmetic progression of length exactly $2q$. Subtract the first point of each progression and divide by $m$. The class becomes a canonical side-$2q$ integer square.

A residue modulo $N$ in this class corresponds to exactly one residue modulo $q$ in these new coordinates. Its four copies correspond to all four representatives of that residue in the local side-$2q$ square: adding $N$ to a coordinate adds $q$ after division by $m$. Thus the chosen points in the class are precisely a full four-copy lift of a local residue subset. Scaling and translation preserve integer collinearity, so this local subset has size at most $\beta(q)$.

If the containing modular support has at most $K$ residue classes modulo $m$, summing gives
$$
 |R|\le K\beta(q).
$$
An invertible affine image of an integer polynomial graph has exactly $m$ points modulo $m$, independently of its degree. Hence
$$
 |R|\le m\beta(q),\qquad |L_N(R)|/n\le2\beta(q)/q.
$$
This is a geometric division into scaled squares, not a use of a CRT isomorphism. In particular it works when $q^2\mid N$. More generally the lemma applies to every divisor $q$ and any support with a bound on its number of complementary residue classes.

**Necessary constraints for the finite enumeration.**

Full-copy thinning makes each of $x,y,x+y,x-y$ injective on a feasible local residue set. Moreover, for distinct residues modulo any modulus, either relation
$$
 P_1+P_3=2P_2,\qquad P_1+2P_3=3P_2\pmod q
$$
forces an integer collinear triple among their full two-period representatives. The second is the weighted forcing lemma originally supplied by kiro_c1_collinear and used in Theorem 4.3. The first has the same elementary carry proof.

For a coordinate of canonical representatives, the first relation has carry in $\{-1,0,1\}$, and binary offsets $\epsilon_1+\epsilon_3-2\epsilon_2$ attain every integer from $-2$ to 2. The second has carry in $\{-2,-1,0,1,2\}$, and offsets $\epsilon_1+2\epsilon_3-3\epsilon_2$ attain every integer from $-3$ to 3. Choose offsets to cancel each coordinate's carry. Distinct residues give distinct lifted points.

These constraints are necessary but not sufficient for actual full-lift feasibility. We use them to prune a finite enumeration and check actual Euclidean collinearity on all remaining cases.

**Complete finite exclusions.**

We prove $\beta(q)\le q-2$ at the four primes by excluding sets of size $q-1$. This is sufficient since thinning gives at most $q$ points and the properties are hereditary.

A $(q-1)$-point set occupies every row except one. To enumerate necessary modular constraints, translate its unique missing row to zero, then translate its point in row 1 to $(1,0)$. Enumerate the remaining rows in order, trying every column value. Reject a candidate exactly when it violates column or diagonal injectivity, or completes one of the two forcing relations with two earlier points. Every set satisfying the necessary modular conditions has such a normalization, and every admissible prefix remains admissible.

The exact results are:

| $q$ | Searched residue cardinality | Visited states | Normalized modular survivors | Translations checked for actual full lifts |
|---:|---:|---:|---:|---:|
| 11 | 10 | 153 | 0 | 0 |
| 13 | 12 | 1,245 | 0 | 0 |
| 17 | 16 | 125,869 | 4 | 1,156 |
| 19 | 18 | 1,516,171 | 0 | 0 |

At 17, each of the four modular survivors has 289 translates. **Every translate** has a collinear triple in its full side-34 lift. Checking translations is essential: arbitrary modular translation need not preserve actual full-lift feasibility in a fixed window, although it does preserve the necessary modular constraints. The program checks all translations rather than assuming this stronger invariance.

For each translated survivor the checker lists all 64 integer lifted points. At every anchor it normalizes pair differences by their integer gcd and sign. A repeated direction produces three distinct points on one actual integer line, whose determinant is also checked to be zero. All 1,156 translates fail. Thus no $(q-1)$-point full lift exists at any of the four primes.

The exact program `small_prime_full_lift_verify.py` uses only the Python standard library and integer arithmetic. It finishes in about ten seconds in the retained environment. It precomputes, for each row and pair of earlier rows, all ways to solve the two forcing relations for the new point; it independently verifies that its coefficient list is exactly the list obtained from every ordering of both relations. A separate direct C++ implementation with six permutations of each triple reproduces every state count and all four survivors. Independent checks of the finite exclusions are also reported in [15].

This is proof-essential complete finite enumeration, not sampled search or an inference from numerical optima. The supplement regenerates the retained `small_prime_full_lift_verified.json` record.

**Consequences and limits.**

The divisor-fiber lemma and $\beta(q)\le q-2$ prove the theorem, including repeated factors. Together with the factors 2, 3, 5, 7 in Corollary 4.6 and the square-factor obstruction of Section 5, an unbounded polynomial full-lift family above density 1.8 must use squarefree moduli coprime to
$$
 2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19=9699690,
$$
and degree at least seven. These are necessary conditions for a restricted construction route. They give neither an unrestricted no-three upper bound nor a feasible construction.

The displayed small-prime bounds are not claimed to be the exact values of $\beta(q)$. Tighter solver-certified finite values have been reported in [15]; our proof uses only the portable complete exclusions supplied here. At 17 the two forcing relations alone leave four candidates, showing why the final integer-line checks matter. The local finite enumeration concerns exact full-lift feasibility, retaining all required integer-line checks.

**Partial-copy consequences.**

The same local-square observation also applies to arbitrary partial selections: the local set need not contain all four representatives, but it lies in the full lift of at most $q$ residue classes whenever the containing graph has exactly $q$ residues above each class modulo $m$.

**Even moduli, two-period windows.** For every even $N$, any no-three subset of an affine polynomial-graph support in a translated side-$2N$ square has at most $3n/2$ points, with no full-copy assumption. Set $q=2$. Each local side-4 square is supported on two distinct residue classes modulo two. If the two classes share an axial coordinate, their support lies in two integer columns or rows, of capacity four. Otherwise their eight candidate points include four points on one actual diagonal of length four (the main or antidiagonal). At most two of those four can be selected, so capacity is at most six. There are exactly $m=N/2$ complementary classes; hence $|S|\le6m=3N=3n/2$. This strengthens the checkerboard coefficient for this specific window ratio; it does not improve the unrestricted checkerboard problem.

**A factor of three, every window.** If $3\mid N$, arbitrary partial selections from an affine polynomial graph satisfy
$$
 |S|\le4\lceil n/3\rceil
$$
in every translated side-$n$ square, independently of $n/N$. Reduce the entire support modulo three; it has three points. If either coordinate has at most two values, the support lies in at most $2\lceil n/3\rceil$ integer rows or columns, each of capacity two. Otherwise the three points are the graph of a permutation of $\mathbb F_3$. Every such permutation is affine with slope $\pm1$ (the six affine maps exhaust the six permutations), so the support lies on one residue diagonal $x\pm y=c\pmod3$. Its actual diagonal levels number at most $\lfloor2(n-1)/3\rfloor+1\le2\lceil n/3\rceil$, proving the same bound.

In particular the factor-three coefficient $4/3$ survives arbitrary copy deletion and arbitrary windows, with an absolute boundary term. This observation uses only elementary line counting; it needs no finite certificate. Independent finite checks exhaust all six two-class supports in the local side-4 square (maximum capacity six) and all 84 three-class supports in the local side-6 square (maximum capacity eight), agreeing with the analytic proofs.


### 4.7 Every bounded-degree full-lift family has coefficient at most $94/63$

**Theorem 4.7.** Fix an integer $D$. Let $N$ tend to infinity, let $f_N\in\mathbb Z[X]$ have degree at most $D$, and allow arbitrary invertible affine maps modulo $N$ and translated side-$2N$ squares. If a subset of each graph has a no-three full four-copy lift, then
$$
 \limsup_{N\to\infty}\frac{|L_N(R_N)|}{2N}\le\frac{94}{63}=1.49206349\ldots.
$$
All coefficients and affine maps may vary with $N$. The bound is asymptotic for each fixed degree cap; it asserts no error uniform in growing degree. Thus any polynomial full-copy family above density $1.8$ on unbounded boards must have unbounded polynomial degree, in addition to the arithmetic restrictions in Section 4.6. The theorem is an application of the classical results below, combined with full-copy thinning and degree-preserving divisor fibers.

**Classical inputs.**

**Cohen [6], Chowla–Zassenhaus conjecture.** If $d\ge2$ and $p>(d^2-3d+4)^2$ is prime, there is no degree-$d$ complete mapping polynomial over $\mathbb F_p$: $g$ and $g+X$ cannot both permute $\mathbb F_p$. We use the exact statement in [7, Theorem A], which attributes it to [6]. We did not obtain the original publisher proof. This theorem is an imported classical input. 

**Guralnick–Wan [8].** For a polynomial $g$ of degree $1<d<p$ whose covering is tame, either $g$ is exceptional (and hence bijective on $\mathbb F_p$), or its Frobenius-coset derangement proportion satisfies $s_0\ge16/63$. Their value-set formula gives

$$
 |g(\mathbb F_p)|=(1-s_0)p+O_d(\sqrt p).
$$

Thus every nonpermuting degree-$d$ polynomial, $1<d<p$, satisfies

$$
 |g(\mathbb F_p)|\le\frac{47}{63}p+O_d(\sqrt p). \tag{4.7}
$$

We checked [8, equation (1.2), Theorem 1.2, Theorem 4.7 and Corollary 4.8] in the authors' full text. Corollary 4.8 includes decomposable polynomial coverings; its proof uses the classification of tame polynomial monodromy groups. The error constant depends only on the degree. When $p>d$, the Galois group embeds in $S_d$, so its order is prime to $p$ and all ramification is tame. Exceptional polynomials are bijective on the base field, as also used in [8, Theorem 1.2]. We do not claim new proofs of these classical results.


**Prime periods and affine orientation.**

Suppose $f$ has degree $2\le d\le D$ over $\mathbb F_p$ and $p$ exceeds the degree-dependent Cohen threshold. There is at most one $\lambda$ for which $f+\lambda X$ is a permutation. Indeed, if $\lambda\ne\mu$ were two, then

$$
 g=(f+\lambda X)/(\mu-\lambda),\qquad
 g+X=(f+\mu X)/(\mu-\lambda)
$$

would be a degree-$d$ complete mapping.

Under any invertible affine graph map, each of the four grid forms $x,y,x-y,x+y$ pulls back to $\alpha X+\beta f(X)+\gamma$. The forms are projectively distinct for odd $p$. At most one has $\beta=0$; the others correspond to distinct shifts $f+(\alpha/\beta)X$. Consequently at least two of the four grid forms are nonpermuting. Necessary full-copy thinning makes each grid form injective on $R$. Applying (4.7) to either nonpermuting form yields

$$
 \frac{|L_p(R)|}{2p}=\frac{2|R|}{p}
 \le\frac{94}{63}+O_D(p^{-1/2}). \tag{4.8}
$$

If the reduced degree is zero or one, the supporting graph becomes an affine line. A vertical line occupies two actual vertical lines in a complete two-period square. Otherwise write it $y=ax+b\pmod p$ with $|a|\le(p-1)/2$. The interval of integer values of $y-ax$ has length $(|a|+1)(2p-1)$, so a fixed residue modulo $p$ occupies at most $2(|a|+1)\le p+1$ actual parallel lines. Capacity two gives $|L_p(R)|/(2p)\le1+1/p$. Thus (4.8) holds uniformly also after degree drops.

**Degree-preserving divisor fibers.**

Let $N=pm$, without a coprimality assumption. An affine polynomial graph occupies exactly $m$ coordinate residue classes modulo $m$. In the parameter class $t=a+mu$, subtract its affine basepoint, divide coordinates by $m$, and reduce modulo $p$. The local support is an invertible affine image of

$$
 (u,h_a(u)),\qquad
 h_a(u)=\frac{f(a+mu)-f(a)}m\in\mathbb Z[u],\qquad\deg h_a\le D. \tag{4.9}
$$

The original affine linear part remains invertible modulo $p$. Subtracting the first available coordinate representatives rather than the graph basepoint only adds a translation. The original square becomes a complete side-$2p$ square; each chosen $N$-residue contributes exactly the four copies of one $p$-residue. Therefore (4.8) applies to each of these $m$ fibers, with the same $D$-dependent constant. Summing gives

$$
 \frac{|L_N(R)|}{2N}\le\frac{94}{63}+O_D(p^{-1/2}) \tag{4.10}
$$

for every sufficiently large prime divisor $p$ of $N$. If $p\mid m$, higher terms in (4.9) vanish modulo $p$; these fibers are affine lines and the stronger line estimate applies. This is the degree-preserving refinement of the divisor-fiber lemma in Section 4.6.

**An unbounded prime factor.**

Use the square-factor estimate in Theorem 5.2 below. Put $L=\prod_\ell\ell^{\lfloor v_\ell(N)/2\rfloor}$. The full-lift density is at most $4/\sqrt L$. On any sequence whose densities stay above a positive constant, $L$ is bounded. Write $N=L^2K$ with $K$ squarefree. If the largest prime divisor stayed bounded on an unbounded subsequence, both $K$ and $N$ would be bounded, a contradiction. The largest prime therefore tends to infinity on every positive-density unbounded sequence. Apply (4.10) to that prime. Sequences of density tending to zero already satisfy the claimed bound.

The refinement over the unrestricted-degree prime-period reduction in Theorem 5.5 is preservation of the fixed degree under geometric fiber rescaling.


### 4.8 Generic partial lifts, uniformly over every affine orientation

**Theorem 4.8.** Fix $d\ge7$. There is a nonempty Zariski-open set $U_d$ of exact degree-$d$ coefficient vectors, defined over $\mathbb Q$, such that for sufficiently large primes $p$ and every $f\in U_d(\mathbb F_p)$, an arbitrary no-three subset $S$ of an affine image of its periodic graph satisfies
$$
 |S|\le2\left\lceil\frac np\right\rceil\bigl(\rho_dp+O_d(\sqrt p)\bigr),\qquad
 \rho_d=\sum_{j=1}^d\frac{(-1)^{j+1}}{j!}.
$$
The window is any translated side-$n$ square and the affine map is arbitrary and invertible modulo $p$. In particular, at $n=tp$,
$$
 |S|\le2\rho_dn+O_d(n/\sqrt p),\qquad 2\rho_d\le\frac{177}{140}.
$$
The error is uniform over all good coefficient vectors, maps and window placements. The exceptional vectors number $O_d(p^d)$ out of $(p-1)p^d$. The degree remains fixed as $p$ grows, and arbitrary partial copies are allowed.

The useful geometric assertion is simultaneous in slope: for every good $f$ and every $a$ over the algebraic closure, the polynomial $f(X)-aX$ has monodromy $S_d$. It would not suffice to control most slopes, since an affine map could align its coordinate forms with exceptional slopes. The proof below is a jet-interpolation argument followed by elementary tame-cover monodromy; no classification of finite simple groups is needed for this generic theorem.

**Excluding simultaneous critical degeneracies.**

Work in characteristic zero, then outside finitely many characteristics depending on $d$. Consider the $(d+1)$-dimensional coefficient space, with leading coefficient nonzero. Critical points of $f(X)-aX$ solve $f'(X)=a$. Exclude the following proper algebraic incidence images:

- A repeated root of $f''$: equations $f''(x)=f'''(x)=0$, two independent coefficient conditions with one parameter.
- Two double critical points at the same slope: at distinct $x,y$, equations $f'(x)=f'(y)=a$ and $f''(x)=f''(y)=0$. Four conditions, three parameters $(a,x,y)$.
- A double critical point and a distinct pair of critical points sharing a value: at distinct $x,y,z$, impose $f'(x)=f'(y)=f'(z)=a$, $f''(x)=0$, and $f(y)-ay=f(z)-az$. Five conditions, four parameters.
- A double critical point sharing its value with another critical point: $f'(x)=f'(y)=a$, $f''(x)=0$, $f(x)-ax=f(y)-ay$. Four conditions, three parameters.
- Three distinct critical points sharing one value: three derivative equations and two value-difference equations. Five conditions, four parameters.
- Two disjoint pairs of critical points sharing values at the same slope: four derivative equations and two value-difference equations. Six conditions, five parameters.

Each coefficient-rank assertion follows by Hermite interpolation. The largest requirement is independent values and derivatives at four distinct nodes, supplied by degree-at-most-seven variations. The cusp-plus-pair case needs jets of multiplicities $3,2,2$, also supplied. The remaining cases require fewer jets. Thus every listed image has dimension at most $d$, and its closure is proper. A finite union of such closures remains proper; bounded-degree elimination and reduction give the same conclusions outside finitely many primes. Its finite-field exceptional fraction is $O_d(1/p)$.

For a good $f$, at every slope $a$ there are therefore only three possibilities:

1. Every critical point is simple, with distinct critical values.
2. Exactly one critical point is double; all other critical points are simple and all their critical values, including the double point's value, are distinct.
3. All critical points are simple, with exactly one pair sharing a critical value and no further collision.

**All-slope symmetric monodromy.**

The polynomial cover is connected and tame, and its finite inertia generators are transpositions, except possibly one generator. In case 2 that exceptional generator is a 3-cycle; in case 3 it is a product of two disjoint transpositions. It moves at most four sheets.

Let $K$ be the normal subgroup generated by all transposition inertia. It is generated by transpositions, so its orbits are the connected components of the corresponding transposition graph. The whole monodromy group $G$ acts transitively on these orbits. The quotient cover by $K$ is tame and can branch only at the exceptional finite value and at infinity. A connected tame Galois cover of the projective line with at most two branch points is cyclic, with full inertia at both: Riemann–Hurwitz gives $2g-2=-D/e_1-D/e_2$, forcing genus zero and $D/e_1=D/e_2=1$. Thus the action on the $K$-orbits is cyclic and generated by the exceptional inertia. This also justifies the argument in sufficiently large positive characteristic.

If there were more than one orbit, this generator would permute them transitively and have no fixed orbit. But it fixes a sheet when $d>4$, hence fixes that sheet's $K$-orbit, a contradiction. Therefore $K$ is transitive. A transitive group generated by transpositions is $S_d$, proving $G=S_d$ at **every** finite slope.

**Uniform value sets and partial lifts.**

For a degree-$d$ map with geometric monodromy $S_d$, each ordered-distinct-$j$-sheet product, $1\le j\le d$, is geometrically irreducible. Writing $r_b$ for the number of rational roots of $f(X)-aX=b$, Weil gives
$$
 \sum_b (r_b)_j=p+O_d(\sqrt p).
$$
The finitely many ramified values affect the count only by $O_d(1)$. Inclusion-exclusion, using $1_{r>0}=\sum_{j=1}^d(-1)^{j+1}(r)_j/j!$, gives
$$
 |(f-aX)(\mathbb F_p)|=\rho_d p+O_d(\sqrt p).
$$
All product degrees, branch counts and genera are bounded in terms of $d$, so the error is uniform over good coefficients and **all** $a\in\mathbb F_p$. This is the classical symmetric-monodromy value-set formula of Birch and Swinnerton-Dyer [10], recorded in [8, equation (1.0)]. The ordered-sheet calculation supplies the needed degree-uniformity over the good coefficient set; the formula and its constant are not new. The finite-cover and Weil inputs are as in [9].

Under an invertible affine map, each physical coordinate restricts on the graph to $\alpha X+\beta f(X)+\gamma$. At most one of the two independent coordinate forms has $\beta=0$. The other is a nonzero affine multiple of $f(X)-aX$, and therefore occupies at most $\rho_dp+O_d(\sqrt p)$ residue rows or columns.

In a translated square of side $n=tp$, each residue coordinate occurs on exactly $t$ integer lines. Every such line contains at most two selected points, including for arbitrary partial selections. Hence
$$
 |S|\le2t\bigl(\rho_dp+O_d(\sqrt p)\bigr)
 =2\rho_d n+O_d(n/\sqrt p).
$$
For arbitrary windows one has the explicit bound $2\lceil n/p\rceil(\rho_dp+O_d(\sqrt p))$ instead. Section 4.14 removes the integral-period condition using completed character sums; complete value-set cardinalities alone do not imply that extension.

Since alternating partial sums of $1-e^{-1}$ have decreasing odd upper subsequence, $\rho_d\le\rho_7=177/280$ for every $d\ge7$. The constant is not the new input: symmetric-monodromy value sets are classical. The useful input is the all-slope genericity proof that survives arbitrary ambient affine maps and then allows partial copies.

### 4.9 An explicit polynomial family with the partial-copy bound

**Proposition 4.9.** The same partial-lift bound with coefficient $2523223/1995840$ holds uniformly for $f=X^{11}+cX^2$, $c\ne0$, outside a fixed finite set of characteristics. An exact certificate establishes the all-slope hypothesis. Start with $f=X^{11}+X^2$. Put
$$
 \Delta(a,b)=\operatorname{Disc}_X(f(X)-aX-b).
$$
Exact factorization gives
$$
 \operatorname{Disc}_b\Delta(a,b)=\text{nonzero constant}\cdot C(a)^3M(a)^2,
$$
where $C(a)=107421875a^9+387420489$ is the cusp-slope polynomial and $M$ is squarefree of degree 36, coprime to $C$. Its five coefficients in $U=a^9$ are
$$
\begin{aligned}
 (&46851200000000000000000000000000000000000,\\
 &-235304452046378880000000000000000000000000,\\
 &-351097168236952027867812000000000000000000,\\
 &10298318423238394571168098929900000000000,\\
 &22528399544939174411840147874772641).
\end{aligned}
$$
Also $f''$ is squarefree and $C$ is its critical-slope resultant. At a noncusp slope, a collision of two analytically varying simple critical values contributes at least two to the discriminant order. Thus multiplicity two permits exactly one pair. At a simple cusp, the local critical-value discriminant contributes exactly three; additional collisions would raise that order. The factorization therefore verifies precisely the three inertia cases above for every $a$.

Scaling over the algebraic closure gives the same geometry for $f=X^{11}+cX^2$, every nonzero $c$. The resulting coefficient for arbitrary partial selections in $n=tp$ is
$$
 2\rho_{11}=\frac{2523223}{1995840}=1.2642411215\ldots,
$$
with a uniform error for sufficiently large primes. This statement permits arbitrary partial copies; it is not inferred from full-copy thinning or from sampled slopes.

The source `uniform_slope_certificate.py/.json` verifies the displayed identity, its constant factor, all squarefreeness/resultant assertions and the exact value-set coefficient. The local cusp calculation uses $f^{(3)}(x)\ne0$: the two critical values separate to order $3/2$ in the slope parameter, contributing order three to their squared difference. At a noncusp slope critical points vary regularly; any equality of two critical values contributes order at least two. Thus the exact multiplicities exclude all simultaneous degeneracies used in Theorem 4.8.

The independent finite checker enumerates every slope and all nonzero coefficients $c$ up to ninth-power scaling at $p=101,211,401,809,1009,1601,3203$. At $p=101,1009,3203$, the largest value sets over these parameters have sizes $72,676,2081$, giving exact partial-capacity coefficients $144/101$, $1352/1009$ and $4162/3203$, respectively, for all affine orientations in integral-period windows. These controls are finite statements from exhaustive value counts, not an asymptotic threshold or exact no-three optima.

### 4.10 Composite periods with partial selections

**Corollary 4.10.** For a fixed integer polynomial with coefficients in $U_d(\mathbb Q)$, the same asymptotic coefficient applies to arbitrary partial selections in integral-period windows $n=tN$ as $N$ tends to infinity. The statement also holds uniformly for the explicit binomial with $c=c_N$ a unit modulo $N$.

The square-factor partial-lift estimate bounds the square-part parameter $L$ on a positive-density sequence, so the largest prime factor $q$ must grow. A repeated largest prime gives density at most $4/\sqrt q$ and can be discarded. For $N=qm$ with $q$ not dividing $m$, each of the $m$ occupied parameter classes modulo $m$ scales to a square of side $tq$ and an affine image of $f$ modulo $q$. The scaling preserves arbitrary partial selections; it never needs complete copies. The local polynomial is $(f(a+mu)-f(a))/m$, an affine input/output image because $m$ is invertible modulo $q$. Apply the prime partial-lift theorem to each class and sum. The error is $O(n/\sqrt q)$, not $O(n/\sqrt N)$.

A fixed good polynomial excludes only finitely many reduction primes. The explicit binomial certificate is uniform in nonzero $c$, and the unit condition ensures this at every prime factor used in the transfer. The square-factor bound invoked here applies to arbitrary partial selections, as does the local coordinate-line count.


### 4.11 A quantitative bound allowing degree growth

**Theorem 4.11.** Let $D\ge2$ and let $p>D^4$ be prime. Every no-three full lift from an affine image of a polynomial graph of degree at most $D$ satisfies
$$
 \frac{|L_p(R)|}{2p}\le\frac{94}{63}+\frac{2^{39}+20D^3}{\sqrt p}.
 \tag{4.11}
$$
Thus the coefficient $94/63$ holds asymptotically for $D=o(p^{1/6})$. For arbitrary composite periods $N$, the same conclusion holds when $D_N=o(P(N)^{1/6})$, where $P(N)$ is the largest prime divisor, along an unbounded family. The numerical error constant is deliberately conservative and does not give a practical threshold. This result uses the tame monodromy classification in [8, Theorem 4.7] in addition to Corollary 4.8.

**Reduce a value-set bound to an indecomposable factor.**

Decompose $g$ over $\mathbb F_p$ into indecomposable polynomial factors. If $g$ is nonpermuting, some factor $h$ is nonpermuting. Put $e=\deg h\le D$. Then

$$
 |g(\mathbb F_p)|\le |h(\mathbb F_p)|.
$$

Indeed this holds for every factor, including a middle factor. All covers are tame because $p>D$. [8, Theorem 4.7] says that an indecomposable nonexceptional h is in one of the following cases:

* $e\le31$;
* the geometric monodromy is triply transitive;
* $e$ is prime and the arithmetic and geometric groups coincide and are cyclic or dihedral in their natural degree-$e$ action.

For $e\ge32$ this follows directly from cases (b)–(f): $A_e$ and $S_e$ are triply transitive. The exceptional case (d) cannot occur for nonpermuting $h$.

**Triply transitive covers: only three moments are needed.**

Let $U$ be the affine target with its finite branch values deleted, and let $r_y$ count roots of $h(X)=y$ over $\mathbb F_p$. The covers of ordered distinct j-tuples of roots, for $j=1,2,3$, are geometrically irreducible. Write $n_j=(e)_j$ for their degrees and $g_j$ for the genera of their smooth compactifications. Weil gives

$$
 M_j:=\sum_{y\in U(\mathbb F_p)}(r_y)_j
 =p+E_j,\qquad
 |E_j|\le 2g_j\sqrt p+e n_j+1. \tag{4.12}
$$

There are at most $e$ geometric branch values including infinity. The $en_j$ term bounds deleted points without assuming rational branch values.

The genera have polynomial, rather than factorial, bounds. For a permutation $\sigma$, write $\operatorname{ind}(\sigma)$ for degree minus number of cycles. This equals its minimum transposition length and is subadditive under products. A transposition of $e$ letters acts on ordered $j$-tuples with index

$$
 I_j=\frac{(e)_j-(e-2)_j}{2},\quad
 I_1=1,\ I_2=2e-3,\ I_3=3(e-2)^2.
$$

Thus the index of any inertia permutation on the $j$-tuple action is at most $I_j$ times its index on the original $e$ letters. The original source is $\mathbb P^1$, so tame Riemann–Hurwitz gives total inertia index $2e-2$. Applying it to the tuple cover yields

$$
 g_1=0,\qquad g_2\le(e-2)^2,\qquad
 g_3\le1+2(e-1)(e-2)(e-3). \tag{4.13}
$$

For every nonnegative integer r,

$$
 1_{r>0}\le r-\frac{(r)_2}{2}+\frac{(r)_3}{6}
$$

(the third Bonferroni inequality). Summing and adding back at most e-1 finite branch values gives

$$
 |h(\mathbb F_p)|\le\frac23p+10e^3\sqrt p \tag{4.14}
$$

when $p>e^4$. The generous constant 10 absorbs (4.12), (4.13) and the deleted points: $en_3=O(e^4)=O(e^2\sqrt p)$. Thus the estimate uses no large-degree full distribution or Galois-closure genus bound.

**Cyclic and dihedral cases.**

Here the groups are equal, so Frobenius does not permute geometric orbit components. In the cyclic case unramified fibers have either zero or e roots. Since the original source has p+1 points,

$$
 |h(\mathbb F_p)|\le(p+1)/e+e-1.
$$

In the dihedral case e is an odd prime and unramified root counts lie in {0,1,e}. On this set,

$$
 1_{r>0}=r-(r)_2/e.
$$

The ordered-pair action has (e-1)/2 orbits. [8, Lemma 4.2] says the geometric Galois closure has genus zero. All its quotient curves therefore have genus zero; the orbit components here are defined over F_p. Hence

$$
 M_2=\frac{e-1}{2}(p+1)-B,\qquad0\le B\le e n_2.
$$

Using $M_1\le p+1$ and restoring the deleted branch values gives

$$
 |h(\mathbb F_p)|\le\frac{e+1}{2e}(p+1)+e(e-1)+e-1
 \le\frac23p+O(e^2).
$$

These cases satisfy (4.14) with the same generous error bound.

**The bounded exceptional degrees.**

For $2\le e\le31$ use [8, Corollary 4.8]: $s_0\ge16/63$. Its degree-dependent error is already an absolute constant on this finite list. Here is an explicit, deliberately loose constant if desired.

For ordered distinct $j$-tuples, $1\le j\le e$, retain only geometric components fixed by Frobenius. Nonfixed components have no rational points over the unramified target. Let $k_j$ be the number retained. Their total degree is at most $n_j=(e)_j$. Riemann–Hurwitz bounds the sum of twice their genera by $en_j$; deleting branch points removes at most $en_j$ geometric points. Therefore

$$
 |M_j-k_jp|\le e n_j\sqrt p+(e+1)n_j.
$$

Coset Burnside counting gives $k_j$ as the Frobenius-coset average of $(\operatorname{fix}\sigma)_j$. Full inclusion–exclusion has leading coefficient $1-s_0$. Since $\sum_{j=1}^e n_j/j!=2^e-1$, adding branch values proves

$$
 |h(\mathbb F_p)|\le\frac{47}{63}p+2^{38}\sqrt p\qquad(e\le31). \tag{4.15}
$$

The error bound follows already from $(2^{31}-1)(31\sqrt p+32)+30<2^{38}\sqrt p$. This argument spells out effectiveness, but the large constant should not be read as a practical threshold.

Combining all three cases and the indecomposable-factor reduction yields the uniform estimate

$$
 |g(\mathbb F_p)|\le\frac{47}{63}p+(2^{38}+10D^3)\sqrt p \tag{4.16}
$$

for every nonpermuting polynomial of degree at most D and p>D^4.

**Return to full lifts.**

Cohen's complete-mapping theorem applies because $p>D^4\ge(d^2-3d+4)^2$ for $2\le d\le D$. As in Theorem 4.7, at most one nonlinear shift $f+\lambda X$ permutes $\mathbb F_p$. At least two of the four pulled-back grid forms are nonpermuting. Necessary full-copy thinning and (4.16) give (4.11), for example with the explicit error $(2^{39}+20D^3)/\sqrt p$. Degree-zero or degree-one support has coefficient at most $1+1/p$ and is harmless.

For $N=pm$ the local polynomial $[f(a+mu)-f(a)]/m$ still has degree at most $D$, including $p\mid m$. The error in (4.16) is uniform over every fiber, so summation does not magnify it. Along positive-density sequences the largest prime factor tends to infinity by the square-factor argument. This proves the stated composite extension.

The classical classification, complete-mapping theorem and Weil bound are imported as stated. The additional estimate tracks a cubic dependence on degree using only low-order tuple covers in unbounded degrees and a fixed absolute remainder in the bounded exceptional cases.



### 4.12 Partial copies of affine power graphs

**Theorem 4.12.** Fix $D$. Let $N\to\infty$, let $f_N(X)=a_NX^{d_N}+b_NX+c_N$ with $2\le d_N\le D$, and allow arbitrary invertible affine maps modulo $N$. Every no-three partial selection from the lifted support in a translated square of side $n=tN$, with any positive integer $t$, satisfies
$$
 \limsup\frac{|S|}{n}\le4-\frac6e=1.792723353\ldots<1.8.
 \tag{4.17}
$$
The coefficients need not be units. A separate six-moment bound gives coefficient $323/180<1.8$ when $d_N=o(P(N)^{1/12})$. The fixed-degree constant uses the full fixed-point distribution; the growing-degree statement uses only six moments with explicit polynomial error. Both permit arbitrary partial copies, and neither covers all exceptional polynomial families.

**A capacity bound for diagonal residue fibers.**

Let $C$ consist of $p$ distinct residue points modulo a prime $p$, and let $S$ be a no-three subset of its lift in a translated side-$n$ square, $n=tp$. For a residue $b$ of a diagonal form $\ell=x-y$ or $x+y$, put $r_b=|\{P\in C:\ell(P)=b\}|$.

Each residue point contributes at most $2t$ selected points, since its representatives occupy exactly $t$ vertical lines. The whole diagonal residue fiber occupies at most $2t$ actual diagonal lines: $\ell$ ranges over an interval of length $2(tp-1)$, containing at most $2t$ integers in a fixed class modulo $p$. Their total capacity is at most $4t$. Therefore

$$
 |S|\le2t\sum_{b\in\mathbb F_p}\min(r_b,2). \tag{4.18}
$$

The argument is valid even if distinct support points share a residue column; that merely makes the individual upper bounds less sharp. No full-copy assumption is used. In comparison, for a coordinate form one has the usual $|S|\le2t$ times its number of occupied residue values.

**Every nonzero linear perturbation of a power is Morse.**

Assume $p>d\ge2$ and $AB\ne0$. The derivative of $g(X)=AX^d+BX$ has $d-1$ distinct nonzero roots. At such a root $u$,

$$
 g(u)=B(1-1/d)u.
$$

These critical values are distinct. The polynomial cover is connected and tame, and all finite inertia generators are transpositions. They generate a transitive group (inertia at infinity is the inverse product of finite inertia), hence the geometric monodromy is $S_d$. There is no excluded coefficient locus here, and no genericity assertion is required. All errors below are uniform over nonzero $A,B$ for fixed $d$.

Let $Z_d$ count fixed points of a uniformly random permutation in $S_d$. The standard ordered-sheet moment/Weil argument gives, for any function of the bounded root count,

$$
 \frac1p\sum_b\min(r_b,2)=\mathbb E\min(Z_d,2)+O_d(p^{-1/2}).
$$

Put $a_j={!j}/{j!}=\sum_{k=0}^j(-1)^k/k!$. Since $\Pr(Z_d=0)=a_d$ and $\Pr(Z_d=1)=a_{d-1}$,

$$
 2\mathbb E\min(Z_d,2)=4-4a_d-2a_{d-1}=:c_d. \tag{4.19}
$$

Combining (4.18) and (4.19) gives coefficient $c_d$ for a diagonal with this monodromy.

**All affine orientations of a power graph.**

Suppose the leading coefficient is nonzero modulo $p$; absorb $b_NX+c_N$ into the affine map. A coordinate form becomes $\alpha X+\beta X^d+\gamma$. If either coordinate has $\alpha\beta\ne0$, its $S_d$ value set gives

$$
 |S|/n\le2(1-a_d)+O_d(p^{-1/2})\le4/3+O_d(p^{-1/2}).
$$

The last inequality holds for every $d\ge2$. Otherwise independence of the coordinate forms forces one to be a pure linear form and the other a nonzero multiple of $X^d$, up to translations. If $X^d$ is not a permutation of $\mathbb F_p$, its value set has size $1+(p-1)/\gcd(d,p-1)\le(p+1)/2$. The coordinate bound is then at most 1+1/p.

The remaining case has $\gcd(d,p-1)=1$, so $d$ is odd. Both diagonals become $AX^d+BX+\gamma$ with $AB\ne0$. Use (4.18) and (4.19). For odd $d\ge3$,

$$
 c_3=5/3,\quad c_5=107/60,\quad c_7=4517/2520,
$$

and $c_d$ increases to $4-6/e$ from below. Indeed, for odd $d$,

$$
 c_{d+2}-c_d=\frac{2(d^2-2)}{(d+2)!}>0.
$$

This proves (4.17) for prime periods. If the leading coefficient vanishes modulo $p$, the support is an affine line. The earlier parallel-line argument bounds its capacity by (1+1/p)n in integral-period squares, so degree drops are harmless.

**Six moments suffice for a uniform rational gap.**

For every integer $r\ge0$,

$$
 \min(r,2)\le r-\binom r3+2\binom r4-3\binom r5+4\binom r6. \tag{4.20}
$$

For $r\ge2$, the right side minus two is $((2r+1)/3)\binom{r-2}{5}$, with a binomial of smaller nonnegative top interpreted as zero; $r=0,1$ are direct. Thus (4.20) is an exact pointwise bound, not a distributional approximation.

For $S_d$, $d\ge6$, the first six falling-factorial moments equal one. Therefore

$$
 \mathbb E\min(Z_d,2)\le1-1/6+2/24-3/120+4/720=323/360.
$$

This yields coefficient $323/180$. The remaining difficult degrees 3 and 5 have the smaller exact constants in (4.19); even degrees in the exceptional coordinate orientation were already excluded by the coordinate value set.

The tuple-cover index argument of Theorem 4.11 applies for $j\le6$. A transposition has index $I_j=((d)_j-(d-2)_j)/2=O_j(d^{j-1})$ on ordered $j$-tuples. Tame Riemann–Hurwitz, using total original inertia index $2d-2$, gives $g_j=O_j(d^j)$. Deleted branch points cost $O_j(d^{j+1})$. Hence the six-moment error in (4.18), divided by p, is

$$
 O\left(d^6/\sqrt p+d^7/p\right), \tag{4.21}
$$

with an absolute constant. Mixed physical coordinate forms require only the third Bonferroni bound, giving coefficient $4/3$ with a smaller $O(d^3/\sqrt p+d^4/p)$ error (degree two is direct). Thus the rational gap 323/180 holds asymptotically whenever $d=o(p^{1/12})$. This growing-degree claim is separate from the sharper fixed-degree limit (4.17).

**Composite periods and varying window multiples.**

Use the divisor-fiber partition $N=pm$. There are $m$ supporting coordinate classes modulo $m$. Each becomes a translated side-$tp$ square after subtraction and division by $m$; arbitrary partial selections remain arbitrary partial selections. The local polynomial is $[f(a+mu)-f(a)]/m$ modulo $p$. If $p\mid m$, it is affine linear. Otherwise it is an invertible affine input/output change of $f$ modulo $p$, hence an affine image of a power graph when its leading coefficient is nonzero, and a line otherwise. Summing the prime bounds over the m fibers multiplies the local side by $m$ but does not magnify the error in $|S|/n$.

The square-factor lattice bound applies to partial selections in every integral-period window: $|S|/n\le4/\sqrt L$, where $L=\prod_\ell\ell^{\lfloor v_\ell(N)/2\rfloor}$. Consequently any positive-density unbounded sequence has $P(N)$ tending to infinity, as in Theorem 5.5. Use that prime in the local estimate. This proves both the bounded-degree coefficient (4.17) and the stated growing-degree rational bound, uniformly over $t$.

This result complements Theorem 4.8, which handles most coefficient vectors by all-slope $S_d$ projections. Here the pure-power locus can have a genuine permutation direction, so the clipped diagonal capacity (4.18) handles the remaining orientation. It excludes a natural exceptional family from the partial-copy search without claiming that all exceptional polynomials are covered.



**Finite checks and moment limitation.** The supplement checks 288 translated-window instances, 1,001 exact integer inequalities, 49 odd-degree recurrences and 72 finite root profiles. These are controls of the proof's ingredients. They do not imply a bound below $1.8$ at every finite prime: for $d=7$, $p=6421$ and slope one, the exact clipped bound is about $1.80595$. The theorem is asymptotic.

The six-moment coefficient cannot be improved by optimizing only a majorant under those same six factorial moments: the fixed-point law of $S_6$ satisfies all six and attains the majorant at every point in its support. The analogous four-moment optimum is $11/6$, attained by the $S_4$ fixed-point law, so four moments alone do not cross $1.8$. These statements concern the moment relaxation, not the true no-three capacity or the optimal degree-growth exponent.


#### 4.12.1 Coupling both diagonals improves the fixed-degree bound

**Proposition 4.12a.** Under the fixed-degree hypotheses of Theorem 4.12, in every translated window $n\ge N$, the coefficient improves to
$$
 \limsup |S|/n\le\frac{2501}{1440}=1.73680555\ldots.
$$
This refinement uses both diagonal constraints. It permits arbitrary windows as proved below, but does not provide a growing-degree assertion.

Only the hard physical orientation $y=Ax^d$ with $A\ne0$ and $x^d$ a permutation remains; the other orientations already give at most $4/3+o(1)$. Work first in $n=tp$. Each residue point contributes at most $2t$ selected points. Divide its contribution by $2t$ to obtain $z_x\in[0,1]$, and put $w_x=1-z_x$, $W=\sum_xw_x$. For either diagonal, a residue fiber of size $r\ge3$ must have deletion weight at least $r-2$. Let
$$
 D_\pm=\sum_b(r_{\pm,b}-2)_+,\qquad
 B=|\{x:r_{+,g_+(x)}\ge3,\ r_{-,g_-(x)}\ge3\}|,
 \quad g_\pm(x)=Ax^d\pm x.
$$
Summing the two families of deletion requirements gives
$$
 D_++D_-\le\sum_x w_x
 \bigl(1_{r_+(x)\ge3}+1_{r_-(x)\ge3}\bigr)
 \le W+B.
$$
Consequently the following finite inequality holds for arbitrary partial selections:
$$
 |S|/n\le2-2(D_++D_--B)/p.
$$
It remains to count the overlap $B$; independence of the two fiber sizes cannot be assumed.

**Disjoint relative-root branch sets.** For $g_\lambda(x)=x^d+\lambda x$, consider the cover over its distinguished root $x$ defined by
$$
 Q_\lambda(x,y)=\frac{y^d-x^d}{y-x}+\lambda=0.
$$
The parent polynomial is Morse with group $S_d$. Passing to the field of one root gives relative group $S_{d-1}$. At infinity the other roots have distinct limiting ratios $y/x$ equal to the nonidentity $d$th roots of unity, so the relative cover is unramified there. Its finite branch points occur at unramified preimages $x$ of critical values of the parent. If $c$ is the corresponding critical point, then $dc^{d-1}=-\lambda$ and $x=cz$, where
$$
 z^d-dz+d-1=0,\qquad z\ne1.
$$
The double root $z=1$ corresponds to $x=c$, where the distinguished-root base change cancels the simple ramification; it is not a relative branch point. All other roots are simple.

The relative branch sets for $\lambda$ and $-\lambda$ are disjoint in characteristic zero for every $d\ge3$. A common branch would give roots $z,w$ of the last equation such that
$$
 z^{d-1}=-w^{d-1}=:u,\qquad
 z=\frac{d-1}{d-u},\quad w=\frac{d-1}{d+u},\quad
 \left(\frac{d+u}{d-u}\right)^{d-1}=-1.
$$
The quotient has absolute value one, forcing $\Re u=0$. Thus
$|z|=(d-1)/\sqrt{d^2+|u|^2}<1$ and $|u|<1$. The quotient's principal argument has absolute value $2\arctan(|u|/d)<2/d$. Multiplication by $d-1$ keeps it strictly between $-2$ and $2$, excluding $-1$. This contradiction proves disjointness. For fixed $d$, the corresponding nonzero branch resultant remains nonzero outside finitely many characteristics. Algebraic scaling makes the assertion uniform over nonzero $A$ and the opposite physical slopes.

The two relative Galois closures are linearly disjoint over the algebraic closure: their intersection could ramify only at common branch points, and the projective line has no nontrivial everywhere unramified cover. Their joint geometric group is $S_{d-1}\times S_{d-1}$. The arithmetic group is the same, since it embeds into the product of these already full symmetric permutation groups.

**The resulting coefficient.** Write $a_j={!j}/{j!}$ and let $Z_j$ have the fixed-point distribution of $S_j$. Weil counting in the product cover now proves
$$
 B=b_d^2p+O_d(\sqrt p),\qquad
 b_d=\Pr(Z_{d-1}\ge2)=1-a_{d-1}-a_{d-2}.
$$
The fiber through $x$ has its distinguished root plus this relative count. The individual diagonal covers give
$$
 D_\pm=D_dp+O_d(\sqrt p),\qquad
 D_d=\mathbb E(Z_d-2)_+=-1+2a_d+a_{d-1}.
$$
Substitution yields coefficient
$$
 C_d=2-4D_d+2b_d^2.
$$
For $d=3$, retain the stronger one-diagonal coefficient $5/3$. At $d=5$, $C_5=2501/1440$. For all odd $d\ge7$, the alternating-series formulas give
$D_d>3/e-1>3/29$ and $b_d\le b_7=191/720$; the middle inequality follows from $e<87/32$. Hence
$$
 C_d<2-12/29+2(191/720)^2<2501/1440.
$$
As odd $d$ grows, $C_d$ tends to $8-20/e+8/e^2=1.72509344\ldots$, with degree fixed before the prime grows. The usual degree-preserving fibers and square-factor bound transfer the result to every modulus and integral window multiple. The improvement comes from the proved overlap restriction on deletions, not from optimizing a one-diagonal moment bound.


**Arbitrary windows via weighted overlap.** Write $n=kp+r$, $\delta=r/p$, and let $I,J$ be the extra coordinate residue intervals. For graph residue $x$ set
$a_x=k+1_{I\times J}(x,P(x))$. Its selected count is at most $2a_x$. Define $w_x=a_x-\frac12$(selected count), so $0\le w_x\le a_x$. Let $V_\pm$ be the graph residues whose diagonal fibers have size at least three, and $H_\pm$ their sets of diagonal target values. If $L_{\pm,b}$ counts actual diagonal lines, then
$$
 E_\pm:=\sum_{x\in V_\pm}a_x-\sum_{b\in H_\pm}L_{\pm,b}
 \le\sum_{x\in V_\pm}w_x.
$$
An individual fiber may contribute a negative lower bound; summing these remains valid. Adding both families and bounding shared deletion weights by $a_x$ gives
$$
 W\ge E_++E_--\sum_{x\in V_+\cap V_-}a_x.
$$

Put $b=b_d$, $\tau=\Pr(Z_d\ge3)$ and $D=D_d=b-2\tau$. The last identity is the size-bias relation $b=\mathbb E[Z_d1_{Z_d\ge3}]$. The product relative monodromy, completed over the extra rectangle, gives
$$
 \begin{aligned}
 \sum_xa_x&=(k+\delta^2)p+O_d(\sqrt p\log^2p),\\
 \sum_{x\in V_\pm}a_x&=(k+\delta^2)bp+
 O_d((k+1)\sqrt p\log^2p),\\
 \sum_{x\in V_+\cap V_-}a_x&=(k+\delta^2)b^2p+
 O_d((k+1)\sqrt p\log^2p).
 \end{aligned}
$$
To justify completion, the needed phases on each Frobenius twist are only $\alpha x+\beta P(x)$. These are nonconstant unless both coefficients vanish; bounded pole orders exclude Artin–Schreier for sufficiently large characteristic at fixed degree. The complete character-sum estimate of Section 4.14 and normalization by centralizer sizes give the stated class proportions. No assertion about independent marked-root positions is needed here.

For $H_\pm$, the parent $S_d$ covers give target proportion $\tau$ and the corresponding interval discrepancy. The actual diagonal values form $2n-1$ consecutive integers, so
$$
 \sum_{b\in H_\pm}L_{\pm,b}
 =2(k+\delta)\tau p+O_d((k+1)\sqrt p\log p).
$$
It follows that
$E_\pm=[kD+\delta^2b-2\delta\tau]p+
O_d((k+1)\sqrt p\log^2p)$.
Subtract the lower bound for $W$ from the baseline $\sum_xa_x$, using
$C_d/2=1-2D+b^2=(1-b)^2+4\tau$. This yields
$$
 \begin{aligned}
 \frac{|S|}{n}
 &\le\frac2{k+\delta}\left[
 k\frac{C_d}{2}+\delta^2(1-b)^2+4\delta\tau\right]
 +O_d(\log^2p/\sqrt p)\\
 &=C_d-\frac{2\delta(1-\delta)(1-b)^2}{k+\delta}
 +O_d(\log^2p/\sqrt p)\le C_d+o_d(1).
 \end{aligned}
$$
Thus incomplete periods do not worsen the coefficient. For degree three retain the arbitrary-window bound $5/3$ from Theorem 4.14. The other physical orientations retain their stronger completed coordinate bounds. Complementary divisor rectangles enclosed in squares and the arbitrary-window square-factor estimate transfer the result to every $n\ge N$. The exact source `two_diagonal_power_certificate.py/.json` checks branch discriminants and the rational constants through degree twenty-five; these are controls of the all-degree complex argument, not a substitute for it.


### 4.13 Every polynomial through degree nineteen permits a partial-copy barrier

**Theorem 4.13.** Let $N\to\infty$ and let $f_N\in\mathbb Z[X]$ be any polynomials of degree at most nineteen, with freely varying coefficients and invertible affine maps modulo $N$. For every no-three partial selection from the lifted support in a translated square of side $n=tN$, with arbitrary positive integer $t$,
$$
 \limsup\frac{|S|}{n}\le c_{19}:=\frac{15576858019818383}{8688935743488000}
 =1.792723352971\ldots<1.8.
 \tag{4.22}
$$
There is no generic-coefficient or full-copy hypothesis. This is an asymptotic theorem with an absolute error constant, since the degree is bounded by nineteen. The proof uses the classical tame exceptional-polynomial classification, seven exact opposite-slope certificates and a uniform degree-fifteen decomposition/discriminant certificate. It does not classify all higher-degree exceptional compositions.

**Reduce to an exceptional permutation graph.**

Work modulo a sufficiently large prime $p$ in a square $n=tp$. For an affine-linear polynomial the parallel-line bound gives $|S|/n\le1+1/p$.

Otherwise the two physical coordinates pull back to independent forms $\alpha X+\beta f(X)+\gamma$. If either is nonpermuting, [8, Corollary 4.8] and the coordinate-line capacity give

$$
 |S|/n\le94/63+O(p^{-1/2}), \tag{4.23}
$$

uniformly over every polynomial of degree at most nineteen and affine orientation. This uses only occupied rows or columns, so arbitrary partial copies are allowed.

Suppose both physical coordinates are permutations. Cohen's complete-mapping theorem says there is at most one permuting nonlinear shift $f+\lambda X$. Therefore one of the two coordinates must be a linear parameter, and the other a permutation polynomial $P$ of degree $d\le19$. Reparameterize by the linear coordinate. The physical support is a graph $y=P(x)$, with leading coefficient nonzero. This reparameterization describes the support; it does not assume that arbitrary affine maps preserve a square window.

For fixed degree and sufficiently large $p$, every permutation polynomial here is exceptional: otherwise Guralnick–Wan's value-set upper bound $(47/63)p+O(\sqrt p)$ would be less than $p$. Decompose $P$ into indecomposable polynomials over $\mathbb F_p$. Every factor is a permutation and hence exceptional by the same uniform argument. By [8, Theorem 4.7], an indecomposable tame exceptional polynomial has prime degree and cyclic or dihedral geometric monodromy. Degree two cannot permute an odd field. Thus all factors have odd prime degree.

For $d\le19$ the possibilities are $d=3,5,7,11,13,17,19$ prime, $d=9$ with two cubic factors, or $d=15$ with factors of degrees three and five in either order. Even $d$ cannot occur in this remaining case.

The standard cyclic/dihedral normal forms are, up to affine input/output changes over the algebraic closure, $X^d$ and the Dickson polynomial $D_d(X,a)$, $a\ne0$. They can also be seen directly from [8, Lemma 4.2]: the Galois closure has genus zero; cyclic rotation gives $X^d$, while the dihedral actions $z\mapsto\zeta z$ and $z\mapsto a/z$ give the quotient coordinate $x=z+a/z$ and target $z^d+(a/z)^d=D_d(x,a)$. Since $p>d$, these actions are tame. This is classical cover theory.

**The complete low-degree list that needs a diagonal estimate.**

For prime $d=5,7,11,13,17,19$, $P$ is therefore geometrically affine-equivalent to a power or a Dickson polynomial. The opposite-slope property used below is preserved under any affine input/output equivalence, even over the algebraic closure: input translation changes only the irrelevant constant term, and the two slopes are multiplied by the same nonzero scalar. Geometric $S_d$ for the actual $\mathbb F_p$-defined diagonal polynomial also implies arithmetic $S_d$.

Degree-three permutations are affine-equivalent over $\mathbb F_p$ to a pure cube. To avoid relying on a permutation-table citation, center and scale the cubic to $x^3+Ax$. If $A\ne0$, the collision equation for distinct $x,y$ is

$$
 x^2+xy+y^2+A=0.
$$

For $p>3$ this is a nonsingular projective conic with $p+1$ rational points. At most two are at infinity and at most two have $x=y$. For sufficiently large $p$ a rational point with $x\ne y$ contradicts permutation. Hence $A=0$.

Consequently a degree-nine permutation, being a composition of two cubic permutations, is affine-equivalent over $\mathbb F_p$ to $(x^3+c)^3$. If $c=0$ this is $x^9$; otherwise it is geometrically affine-equivalent to $(x^3+1)^3$. Every coefficient case is covered by one of these alternatives; no sampling of polynomial coefficients enters the argument.

**Exact opposite-slope criterion.**

For a representative $F$ define

$$
 \Delta_F(\lambda,z)=\operatorname{Disc}_x(F(x)+\lambda x-z),\qquad
 B_F(\lambda)=\operatorname{sqfree}\!\left(
 \operatorname{Disc}_z\Delta_F(\lambda,z)\right).
$$

If $B_F(\lambda)\ne0$, the degree-$d$ polynomial $F+\lambda x$ has simple critical points with pairwise distinct critical values. Indeed its critical-value discriminant is squarefree as a polynomial in $z$. Its leading coefficient in $z$ is a nonzero constant, so no critical value is lost to infinity. Hence every finite branch inertia is a transposition. These generate a transitive group for a polynomial cover, and the monodromy is $S_d$.

The exact certificate `degree_nineteen_opposite_certificate.py/.json` proves over $\mathbb Q$:

| $F$ | Degree of $B_F$ | $\gcd(B_F(\lambda),B_F(-\lambda))$ |
|---|---:|---|
| $D_5(x,1)$ | 4 | $\lambda$ |
| $D_7(x,1)$ | 7 | $\lambda$ |
| $D_{11}(x,1)$ | 16 | $\lambda$ |
| $D_{13}(x,1)$ | 22 | $\lambda$ |
| $D_{17}(x,1)$ | 37 | $\lambda$ |
| $D_{19}(x,1)$ | 46 | $\lambda$ |
| $(x^3+1)^3$ | 13 | $\lambda$ |

It independently verifies a nonzero integer resultant after removing the zero-slope factor, and retains the full raw discriminants. These are exact identities, not finite tests of slopes. After excluding finitely many primes, they ensure that for every nonzero $\lambda$ over the algebraic closure, at least one of $F+\lambda x$ and $F-\lambda x$ is Morse with monodromy $S_d$. Scaling $D_d(x,a)=a^{d/2}D_d(x/\sqrt a,1)$ gives uniformity over every nonzero $a$. The two-cube family scales in the same way. For powers $x^d$ every nonzero shift is already Morse, as proved in Theorem 4.12.

For an explicit small example,

$$
 B_{D_5}(\lambda)\doteq
 \lambda(\lambda+5)(4\lambda-25)(4\lambda-5),
$$

whose nonzero roots contain no opposite pair. A shift at $\lambda=25/4$ is not Morse; it is essential to use the two opposite diagonals rather than assert all nonzero shifts have $S_d$.

**The degree-fifteen composition families.** After algebraic affine input/output changes, the two possible compositions have the forms
$$
 F_{a,c}(x)=(D_5(x,a)+c)^3,\qquad E_{a,c}(x)=D_5(x^3+c,a),
 \quad D_5(x,a)=x^5-5ax^3+5a^2x.
$$
The case $a=0$ includes powers. Intermediate nonzero multipliers are absorbed using the Dickson scaling identity, and $c$ retains the intermediate translation. We prove that every nonzero linear perturbation of either family has geometric group $S_{15}$ for every $a,c$, outside finitely many characteristics. The argument uses the exact source `degree15_uniform_certificate.py/.json`.

**Every nonzero perturbation is indecomposable.**

For a monic polynomial of degree $15=kb$, a decomposition with right degree $b$ has a unique monic right component with constant term zero, determined by the polynomial part of the formal $k$th root at infinity. Its coefficients depend only on the coefficients in degrees $15,\ldots,15-b+1$. Adding $\lambda x$ does not change this component for $b=3,5$.

In the original right degree ($b=5$ for $F$, $b=3$ for $E$), a nonzero perturbation cannot remain a polynomial in that component: subtracting the original would make $\lambda x$ a polynomial in a degree-$b$ polynomial, impossible. It remains to exclude the alternate right degree.

For $F$, the forced alternate component is $H=x^3-3ax$. Successively subtracting the unique powers of $H$ that cancel the coefficients in degrees divisible by three leaves a remainder. Its coefficients in degrees at least two generate the ideal
$$
 \langle c,a^5\rangle\subseteq\mathbb Q[a,c].
$$
Thus an alternate decomposition is possible only at $a=c=0$.

For $E$, the forced alternate component is $H=x^5+(5c/3)x^2$. The analogous nonlinear remainder coefficients generate
$$
 \langle c^2-3a,ac,a^2\rangle.
$$
Again their common zero is only $a=c=0$. At that point the polynomial is $x^{15}$, and both possible right components are pure powers; adding a nonzero linear term is incompatible with either. Thus all the nonzero perturbations are indecomposable. The source checks these coefficient ideals by exact Gröbner arithmetic and verifies powers of $a,c$ reduce to zero.

**Nonsquare discriminants: a small calculation replaces a large branch calculation.**

For either normalized family write
$$
 \Delta(\lambda,z,c)=\operatorname{Disc}_x(F(x)+\lambda x-z).
$$
It has degree fourteen in $z$ with constant nonzero leading coefficient. Divide by that coefficient. There is a unique possible monic degree-seven square root $Q(z)$: recursively match the coefficients from $z^{14}$ through $z^7$. The discriminant is a square exactly when all seven coefficients of $\Delta-Q^2$ vanish.

For $a\ne0$, algebraic scaling normalizes $a=1$ and retains arbitrary $c$ and nonzero $\lambda$. In the nonzero-$c$ case, remove the common powers of $\lambda$ and $c$ from each remainder coefficient and set $v=c^2$. The remaining coefficients have rational entries. Their exact Gröbner bases (up to nonzero rational scalars), in graded reverse lexicographic order on $(v,\lambda)$, are:

- For $(D_5(x,1)+c)^3$,
$$
 \left\{\lambda^3,\ -\lambda^2+144v^2+384v+256,
              \ -\lambda^2+12\lambda v+16\lambda\right\}.
$$
  In particular their common zero forces $\lambda=0$.
- For $D_5(x^3+c,1)$, the basis is $\{1\}$, so they have no common zero.

When $c=0$, specialize the original remainder coefficients, divide out their powers of $\lambda$, and take their univariate gcd. It is one for both families. When $a=0,c\ne0$, scaling normalizes $c=1$; the same univariate square-remainder gcd is one for $(x^5+1)^3$ and $(x^3+1)^5$. Finally $a=c=0$ is the Morse polynomial $x^{15}+\lambda x$, $\lambda\ne0$.

This covers **all** parameter values. It does not sample $c$, and does not infer a conclusion from generic nonsquareness. The exact source records the full critical-value discriminants, square candidates, normalized remainder coefficients and Gröbner bases. Clearing their fixed denominators and identity coefficients excludes only finitely many primes, uniformly in all parameters.

**Why indecomposable plus nonsquare implies $S_{15}$ here.**

We explicitly import the classical tame primitive-polynomial monodromy classification. The characteristic-zero list is stated in [19, Theorem 3.3], which credits Müller’s classification [20]. At degree fifteen the only possibilities are
$$
 S_{15},\quad A_{15},\quad\operatorname{PSL}_4(2)\cong A_8
$$
in its degree-fifteen action. The last group is simple and nonabelian, so its sign homomorphism is trivial: it lies in $A_{15}$.

[8, proof of Theorem 4.7] explicitly transfers tame polynomial monodromy to the characteristic-zero list using the tame branch-cycle theorem. Hence the list applies here for sufficiently large characteristic as well. Indecomposability has just been certified in all parameters. The discriminant is not a square over the algebraically closed constant field, so the geometric group is not contained in $A_{15}$. Only $S_{15}$ remains.

This is a use of the classification, not an elementary replacement for it. The novelty here is the uniform decomposition and square-discriminant obstruction for these composition families.

**One good diagonal suffices.**

In the physical graph $y=P(x)$, the two diagonal forms are $P(x)+x$ and $P(x)-x$. By the preceding classification and opposite-slope identities, at least one has geometric monodromy $S_d$. Affine input/output normalizations replace these by $F(u)+\lambda u$ and $F(u)-\lambda u$ with the same nonzero $\lambda$, so the certificate applies.

For the good diagonal, let $r_b$ count graph residues with diagonal value $b$. The clipped capacity lemma gives

$$
 |S|\le2t\sum_b\min(r_b,2).
$$

The fixed-point distribution of $S_d$ and Weil counting give

$$
 |S|/n\le c_d+O(p^{-1/2}),\qquad
 c_d=4-4\frac{!d}{d!}-2\frac{!(d-1)}{(d-1)!}.
$$

For odd $d\ge3$, $c_{d+2}-c_d=2(d^2-2)/(d+2)!>0$. Thus every remaining degree $d\le19$ is bounded by $c_{19}$. All degree, branch-count and genus bounds are absolute, so the error is uniform over $P$, its affine orientation and the window multiple $t$. Cases covered by (4.23) or the line bound are stronger.

**All moduli, all partial copies.**

Let $N=pm$. The affine polynomial support has exactly $m$ coordinate classes modulo $m$. Each scales to an affine graph of the integer polynomial

$$
 [f(a+mu)-f(a)]/m
$$

of degree at most nineteen modulo $p$, inside a translated side-$tp$ square. Arbitrary partial selections remain arbitrary partial selections. Apply the uniform prime theorem in each class and sum. This retains the error $O(p^{-1/2})$ in $|S|/n$, without any coprimality requirement.

By Theorem 5.2, positive-density unbounded sequences have their largest prime divisor tending to infinity. Choosing that prime proves (4.22), exactly as in the earlier full-copy and partial-power transfers.

The supplement supplies the complete exact source and output for all five rows of the table, including the raw critical-value and double discriminants, primitive bad-slope coefficients, and the nonzero opposite-slope resultants. The identities are over the rationals, so after clearing their finitely many bad reduction primes they apply uniformly to every coefficient and slope in the stated families. All seven opposite-slope certificates were independently reproduced. No numerical root sampling or random choice of coefficients enters this proof.

### 4.14 Arbitrary windows for the fixed-degree partial-copy bounds

**Theorem 4.14.** The fixed-degree conclusions of Theorems 4.12 and 4.13 hold in every translated square of side $n\ge N$, without requiring $n/N$ to be an integer. The generic and explicit-family conclusions of Theorem 4.8, Proposition 4.9 and Corollary 4.10 also hold in every such window. Its fixed-degree proof is later refined quantitatively in Proposition 4.15a. At a prime period, the generic estimate is
$$
 |S|\le 2\rho_d n+O_d\!\left(n/\sqrt p+\sqrt p\log p\right).
$$
For the fixed-degree diagonal estimate below, an error
$O_d((n/p+1)\sqrt p\log^{2d+1}p)$ suffices. The constants are uniform over the specified coefficient families, orientations and translations.

**Complete sums and incomplete image sets.** Let $g$ be a degree-$d$ polynomial with geometric group $S_d$. The ordered-distinct-$j$-root cover is geometrically irreducible for $1\le j\le d$. On its smooth completion the target function $b$ has pole degree at most $(d)_j\le d!$. Thus, for sufficiently large $p$, every nonzero phase $ab$ has a positive pole order less than $p$ and cannot equal $H^p-H+$constant over the algebraic closure. The complete additive-character Weil bound on curves [21, equation (3.1)] gives
$$
 \sum_b(r_b)_j\psi(ab)=O_d(\sqrt p)\qquad(a\ne0),
$$
where $r_b=|g^{-1}(b)(\mathbb F_p)|$; deleting branch values costs $O_d(1)$. We use the complete-sum statement in that reference, not its stronger incomplete-lemma hypothesis.

Inclusion-exclusion for the indicator $v_b=1_{r_b>0}$ and one-dimensional Fourier completion now give, uniformly over cyclic intervals $I$,
$$
 \sum_b v_b\psi(ab)=O_d(\sqrt p),\qquad
 \sum_{b\in I}v_b=\rho_d|I|+O_d(\sqrt p\log p).
$$
Indeed the Fourier transform of an interval has normalized $\ell^1$ norm $O(\log p)$. Write $n=kp+r$, $0\le r<p$. A physical coordinate interval contains $k$ copies of every residue and one extra copy on a cyclic interval of length $r$. Its occupied lines number
$$
 k|g(\mathbb F_p)|+|g(\mathbb F_p)\cap I|
 =\rho_d n+O_d(n/\sqrt p+\sqrt p\log p).
$$
Capacity two per line proves the generic estimate. If $r=0$, its last error term is unnecessary.

The same Fourier assertion holds for the image indicator of an arbitrary fixed-degree separable polynomial, without an $S_d$ hypothesis. Apply the complete-sum argument to each Frobenius-stable geometric component of each ordered-root cover. Other components contribute rational points only at their bounded intersection or boundary loci. Every surviving component has nonconstant target and bounded pole orders. Inclusion-exclusion therefore again gives $O_d(\sqrt p)$ at nonzero frequency. The zero-frequency main coefficient is its arithmetic Frobenius-coset image proportion. In the nonexceptional case the Guralnick–Wan bound makes this at most $47/63$. Consequently any nonpermuting physical coordinate occurring in Theorem 4.13 gives coefficient $94/63+o_d(1)$ uniformly for $n\ge p$. For sufficiently large $p$ at fixed degree, the exceptional alternatives are permutations, as used earlier.

**The remaining permutation graph.** It suffices to consider $y=P(x)$ where $P$ permutes $\mathbb F_p$, has fixed odd degree $d\ge3$, and one physical diagonal $g=P\pm X$ has geometric monodromy $S_d$. Put $n=kp+r$, $k\ge1$, and $\delta=r/p$. Let $I,J$ be the cyclic coordinate intervals of length $r$ receiving an extra representative. Each graph residue $(x,P(x))$ contributes at most
$$
 2\min(k+1_I(x),k+1_J(P(x)))
 =2\bigl(k+1_{I\times J}(x,P(x))\bigr)
$$
selected points. In diagonal residue $b$, let $R_b$ count graph residues, let $Z_b$ count those lying in $I\times J$, and let $L_b$ count actual diagonal lines in the square. The exact capacity inequality is
$$
 |S|\le2\sum_b\min(kR_b+Z_b,L_b).
$$
It uses both individual row/column capacities and the whole diagonal-fiber capacity, so it applies to arbitrary partial selections.

For the chosen diagonal, the possible first coordinates of extra residues form the interval intersection $J_b=\{x\in I:b\mp x\in J\}$, up to the sign convention for $b$. Put $q_b=|J_b|/p$. The convolution of two cyclic intervals gives the following profiles; discrete endpoints change the total capacity by $O_d(1)$.

* For $0\le\delta\le1/2$, a fraction $2\delta$ of residues has $L_b=2k+1$, with $q_b$ ranging twice over $[0,\delta]$ and measure $2\,dq$. Elsewhere $L_b=2k$ and $q_b=0$.
* For $1/2\le\delta<1$, a fraction $2\delta-1$ has $L_b=2k+2$ and $q_b=2\delta-1$. On the remainder $L_b=2k+1$, and $q_b$ ranges twice over $[2\delta-1,\delta]$ with measure $2\,dq$.

Translations and the choice of diagonal only shift or reverse the residue origin.

**Marked roots and the required counting law.** Write $p_s=\Pr(Z_d=s)$ for the fixed-point probabilities in $S_d$, and $\mu=\mathbb E\min(Z_d,2)=2-2p_0-p_1$. We need the law
$$
 \Pr(R_b=s,Z_b=h)
 \sim p_s\binom{s}{h}q_b^h(1-q_b)^{s-h}
$$
only in averages over the displayed interval constraints and only for $s<d$. There is no pointwise probabilistic assertion at a fixed residue $b$.

Here is a curve proof with the normalization specified. Take the geometrically connected $S_d$ Galois closure, label its roots $x_1,\ldots,x_d$, and fix $\sigma\in S_d$. The usual Frobenius twist has $|C_{S_d}(\sigma)|$ rational points above every unramified target with Frobenius conjugate to $\sigma$, and none above the other targets. Thus division by the centralizer size turns its Weil main term into the class weight $|[\sigma]|/d!$. Roots fixed by $\sigma$ descend to rational functions on this twist. Its genus and all relevant pole degrees are bounded in terms of $d$.

Every nonzero linear combination of fewer than all roots and the target is nonconstant. To prove this, extend its root-coefficient vector by zeros on unmarked roots. Applying a transposition to a putative constant relation gives $(a_i-a_j)(x_i-x_j)=0$. All coefficients must be equal; an unmarked root has coefficient zero, so all are zero. The target coefficient then vanishes too. Bounded pole orders exclude Artin–Schreier phases for sufficiently large $p$, and the complete-sum bound gives $O_d(\sqrt p)$ uniformly in nonzero frequencies and twists.

Expand the interval indicators in the linear forms $b,x_i,b\mp x_i$. The normalized Fourier $\ell^1$ norm of their product is at most the product of the individual $O(\log p)$ norms. Collect frequencies in the independent variables $(b,x_1,\ldots,x_s)$. The zero frequency equals the exact finite-field overlap volume; every nonzero frequency has the preceding Weil bound. Complements have the same norm order. Dividing by the centralizer, summing over classes, and using exchangeability of fixed labels proves the averaged law with error $O_d(\sqrt p\log^{2d+1}p)$. This argument does not assume independence of all $d$ roots: their fixed sum would invalidate it. Below only $s\le3$ is needed, and the case $s=d=3$ is explicitly discarded.

**The incomplete period does not increase the coefficient.** If $k=1$ and $\delta\le1/2$, count all support points. Completed character sums for $(x,P(x))$ give
$$
 |S|\le p+2r+|\{x\in I:P(x)\in J\}|
 =n^2/p+O_d(\sqrt p\log^2p).
$$
Its normalized coefficient is $1+\delta\le3/2<c_d$. Every nonzero linear combination of $x$ and $P(x)$ is nonconstant of degree less than $p$, justifying this complete-sum application.

For $k=1$, $\delta\ge1/2$, define
$$
 F_L(q)=L-\sum_{s=0}^{L-1}p_s
 \sum_{h=0}^s\binom{s}{h}q^h(1-q)^{s-h}(L-s-h)_+,
 \qquad L=3,4.
$$
When $d=3$, omit the $s=3$ term of $F_4$. This discards a nonnegative deficit and remains an upper bound; in the formulas below set $p_3=0$ for this case. The averaged capacity coefficient is at most
$$
 B(\delta)=\frac2{1+\delta}\left[
 (2\delta-1)F_4(2\delta-1)+2\int_{2\delta-1}^{\delta}F_3(q)\,dq\right].
$$
Direct integration, with $c_d=2\mu$, gives
$$
 \frac{(c_d-B(\delta))(1+\delta)}{1-\delta}
 =\frac23\left[
 3p_1\delta+p_2(14\delta^2-4\delta+2)
 +24p_3(1-\delta)^2(2\delta-1)\right]\ge0.
$$
The endpoint $\delta=1$ follows by continuity. Every term is nonnegative on $[1/2,1]$, since $14\delta^2-4\delta+2=14(\delta-1/7)^2+12/7$.

For $k\ge2$, the base contribution $k\min(R_b,2)$ has mean $k\mu$. Set $T=1-p_0-p_1-p_2$. On fibers with $L_b-2k=1$ or $2$, respectively, upper bounds for the expected extra are
$$
 E_1(q)=p_1q+p_2(2q-q^2)+T,\qquad
 E_2(q)=p_1q+2p_2q+2T.
$$
For $R_b=1$ the extra is at most $Z_b$, for $R_b=2$ it is at most $\min(Z_b,L_b-2k)$, and for $R_b\ge3$ it is at most $L_b-2k$. Fibers with no additional diagonal line contribute no extra. Integrating over the two profiles, let $E(\delta)$ be the average extra. Then
$$
 \delta\mu-E(\delta)=
 \begin{cases}
 \delta(p_1+2p_2)(1-\delta)+\frac23p_2\delta^3,
       &0\le\delta\le1/2,\\
 \frac{1-\delta}{3}\left[3p_1\delta+p_2(14\delta^2-4\delta+2)\right],
       &1/2\le\delta<1.
 \end{cases}
$$
Both expressions are nonnegative. The total is therefore at most $2(k+\delta)\mu p+O_d((k+1)\sqrt p\log^{2d+1}p)=c_dn+o_d(n)$, uniformly over $n\ge p$. The exact rational checker `clipped_arbitrary_window_certificate.py/.json` verifies these identities and, independently, their nonnegative Bernstein coefficients through degree nineteen.

**Composite periods and degenerate coefficients.** In an affine-line case, the determinant-$p$ lattice argument gives $|S|\le4n/\sqrt p+2=o(n)$ for $n\ge p$. For $N=pm$ with $p\nmid m$, partition into the $m$ supporting coordinate classes modulo $m$. Each local rectangle is enclosed in a translated square of side $\ell=\lceil n/m\rceil\ge p$. The degree-preserving local polynomial and its arbitrary partial selection satisfy the prime theorem. Summing adds an enclosure error $O(m)$, and $m\ell=n+O(m)$.

For the generic theorem this gives
$$
 |S|\le2\rho_dn+O_d\!\left(m+n/\sqrt p+m\sqrt p\log p\right),
$$
so the normalized error is $O_d(\log p/\sqrt p)$ for $n\ge N$. For the fixed-degree diagonal theorem it is $O_d(\log^{2d+1}p/\sqrt p)$. The arbitrary-window square-factor estimate is $|S|\le4n/\sqrt L+2h$ for $N=hL$, so its normalized bound is at most $4/\sqrt L+2/L$ when $n\ge N$. On a positive-density unbounded sequence $L$ stays bounded and the largest prime tends to infinity; a repeated largest prime would instead force density to zero. This proves the composite conclusions. Fixed good integer polynomials exclude only finitely many primes, and the explicit binomial's unit coefficient preserves its geometric hypothesis. All errors here have fixed-degree constants; Proposition 4.15a supplies a separate growing-degree arbitrary-window bound.


### 4.15 A partial-copy obstruction for every bounded degree

**Theorem 4.15.** Fix $D$. For every sequence of polynomials $f_N\in\mathbb Z[X]$ of degree at most $D$, all choices of coefficients and invertible affine maps modulo $N$, and every no-three partial selection $S$ in a translated square of side $n\ge N$,
$$
 \limsup_{N\to\infty}\frac{|S|}{n}\le\frac{1793}{1000}<1.8.
$$
There is no full-copy or generic-coefficient hypothesis. The theorem is first proved at bounded degree; Proposition 4.15a below gives a separate quantitative degree-growing range. The sharper coefficient in Theorem 4.13 remains valid through degree nineteen. The structural input is a consequence of the classical Abhyankar–Moh epimorphism theorem, followed by the same tame monodromy classification and clipped capacities.

**At most one decomposable linear perturbation.**

Over an algebraically closed field of characteristic zero or characteristic greater than $\deg f$, at most one member of $f(x)+\lambda x$ is geometrically decomposable.

Suppose two are decomposable. Subtracting one slope from $f$, write
$$
 f=A(H),\qquad f+\lambda x=B(K),\qquad \lambda\ne0,
$$
where $1<b=\deg H<n$, $1<c=\deg K<n$, and $n=\deg f$. Normalize $f,H,K$ to be monic; adding constants to $H,K$ is immaterial. The identity gives $k[H,K]=k[x]$. The Abhyankar–Moh epimorphism theorem forces $b\mid c$ or $c\mid b$; interchange the two polynomials if needed so $b\mid c$.

For a right component of degree $c$, the polynomial part at infinity of the monic fractional power $f^{c/n}$ equals that component up to a constant. Adding $\lambda x$ changes this fractional power by a Laurent series of order at most $x^{c-n+1}$, which is strictly negative because $c\le n/2$ and $n\ge4$. Thus it does not change its polynomial part.

On the other hand $f=A(H)$ and $b\mid c$. The Laurent expansion $A(T)^{c/n}$ has integral top exponent $c/b$; its nonnegative powers form a polynomial $Q(T)$, and the remainder has negative powers of $T$. Substituting the monic $H(x)$ preserves negativity of the latter powers. Hence the polynomial part of $f^{c/n}$ is $Q(H)$, so $K\in k[H]$. This contradicts $x\in k[H,K]$ and $b>1$.

In characteristic $p>n$ the same proof holds directly. The positive-characteristic epimorphism theorem [22, Theorem 6.9] assumes $p\nmid\gcd(b,c)$, which follows from $b,c<n<p$. All fractional-power denominators used above are then invertible. Thus no unspecified reduction exceptions are needed for the shift lemma.

The epimorphism statement is the classical theorem of Abhyankar and Moh [23], stated in [24, opening page]. This is an application of that theorem, not a new embedding theorem.

**Reduction to primitive diagonal covers.**

Theorem 4.13 handles degrees at most nineteen. For an arbitrary fixed degree bound, the earlier Cohen/Guralnick–Wan argument reduces the difficult orientation to a permutation graph $y=P(x)$, with $P$ exceptional and of odd degree. If its degree is composite, its exceptional factors make $P$ decomposable, so the lemma makes **both** $P+x$ and $P-x$ indecomposable. If the degree is prime, those two polynomials are automatically indecomposable.

Thus for every remaining odd degree $d\ge21$, a physical diagonal has primitive tame polynomial monodromy. Müller's classification [19, Theorem 3.3; 20], leaves $S_d,A_d$, prime-degree cyclic/dihedral groups, and precisely these additional odd degrees beyond nineteen:
$$
 \operatorname{P\Gamma L}_3(4)\ (d=21),\qquad
 M_{23}\ (d=23),\qquad
 \operatorname{PSL}_5(2)\ (d=31).
$$
[8, proof of Theorem 4.7] supplies the tame transfer to characteristic zero. No unproved classification assertion is intended.

The clipped capacity coefficient for a Frobenius coset is $2\mathbb E\min(R,2)=4-4p_0-2p_1$. For $S_d$ it is $c_d<4-6/e$. For the two parity cosets of $A_d$, signed derangement counts give, for odd $d$,
$$
 c_d\ \pm\ \frac{2d^2-8d+4}{d!}.
$$
For $d\ge21$ both are below $1793/1000<1.8$. The exceptional small cases $A_5,A_7$ would exceed $1.8$, which is why the existing low-degree argument remains necessary; no unrestricted assertion about all primitive groups is being made.

The three remaining exact coefficients are
$$
 \begin{array}{c|c}
 G&2\mathbb E_G\min(R,2)\\\hline
 \operatorname{P\Gamma L}_3(4)&8809/5040\\
 M_{23}&62591/35420\\
 \operatorname{PSL}_5(2)&18857/11160
 \end{array}
$$
and all are below $1793/1000$. The first follows by enumerating the 60,480 projective invertible $3\times3$ matrices over $\mathbb F_4$ and their Frobenius twists. The last follows by triangular inversion of $\mathbb E {\dim\ker(g-I)\brack j}_2=1/|\operatorname{GL}_j(2)|$. For $M_{23}$ we use the ATLAS centralizer and degree-23 fixed-point tables [25]. The exact checker retains each imported class entry and verifies total class mass and mean one; it does not independently prove the ATLAS tables.

Each of these three geometric groups is self-normalizing in its permutation action, so there is no additional arithmetic coset. For $M_{23}$ use the trivial outer automorphism group recorded in [25] and the trivial centralizer of a nonregular 2-transitive action. For the projective groups, the two orbits of ordered triples of distinct points are collinear and noncollinear, of different lengths. A normalizer preserves collinearity, so the fundamental theorem of projective geometry places it in the full projective semilinear group, which is the displayed group in both cases.

**Arbitrary windows.**

The marked-root argument extends to any geometrically 2-transitive group when the characteristic does not divide its order. The permutation module is the direct sum of the trivial module and an irreducible augmentation module: semisimplicity and the two-dimensional commuting algebra prove this. The equivariant map sending basis vectors to roots modulo the base field has kernel exactly the trivial module. It cannot vanish on the augmentation module, since then all distinct roots would coincide modulo the base field, and the whole module would map to zero (the sum is already in the base field), contradicting irreducibility of the cover. Consequently a linear combination of fewer than all roots and the target cannot be constant. The same bounded-pole check, twists and Fourier completion apply, now with arithmetic Frobenius-coset weights. The boundary inequalities in Theorem 4.14 depend only on nonnegative $p_s$, not on the special $S_d$ probabilities. Their direct nonnegative factorization was given there. Here $d\ge21$, so every needed count uses strictly fewer than all roots.

The cyclic/dihedral cases need no marked-root independence. Their arithmetic normalizers lie in $\operatorname{AGL}_1(d)$. A multiplier coset outside the geometric multiplier subgroup fixes exactly one point everywhere and is exceptional/permuting, excluded for $P\pm x$ by Cohen and the large-prime value-set dichotomy. In the remaining coset the clipped coefficients are $4/d$ and $1+2/d$, respectively, at most $23/21$ for $d\ge21$.

Write $n=kp+r$. For $k\ge2$, enclosing the window in $(k+1)p$ gives normalized coefficient at most $(3/2)(23/21)=23/14<1793/1000$. For $k=1$, the polynomial permutation graph has at most $(1+\delta)^2p+O_d(\sqrt p\log^2p)$ support points, where $\delta=r/p$. Enclosure in $2p$ gives coefficient at most $2c/(1+\delta)$, while the support count gives $1+\delta$. Their minimum is at most $\sqrt{2c}\le\sqrt{46/21}<1793/1000$. Thus all these cases have a comfortable boundary margin.

Finally use the divisor-fiber and square-factor transfer of Theorem 4.14. All degrees and component genera are bounded by functions of $D$, all reduction exceptions form a fixed finite set, and arbitrary partial selections are preserved. This proves the asserted bound over every sequence of composite periods. The exact source `primitive_tail_capacity.py/.json` records the three exceptional-group calculations.

#### 4.15.1 A polynomial degree range in arbitrary windows

**Proposition 4.15a.** There are absolute constants $C,p_0$ such that, for $p>\max(p_0,D^4)$, every affine polynomial graph of degree at most $D$ and every no-three partial selection in a translated window $n\ge p$ satisfy
$$
 \frac{|S|}{n}\le\frac{1799}{1000}
 +C\frac{D^6(1+\log p)^7}{\sqrt p}.
$$
Consequently the coefficient $1799/1000<1.8$ holds over arbitrary moduli, all coefficients and affine orientations, and every translated window $n\ge N$, whenever
$$
 D_N=o\!\left(\frac{P(N)^{1/12}}{(1+\log P(N))^{7/6}}\right).
$$
The constant $p_0$ covers the fixed low-degree certificates; no practical prime threshold is asserted. Unlike the fixed-degree coefficient in Theorem 4.15, this estimate tracks constants uniformly in degree. It does not require full copies or generic coefficients.

**Choose a primitive nonpermuting physical form.** Write the physical coordinates as $X(t)=\alpha t+\beta f(t)+u$ and $Y(t)=\gamma t+\delta f(t)+v$, with invertible coefficient matrix. At most one of $X,Y,X+Y,X-Y$ is a linear polynomial in $t$. The other forms correspond to distinct slopes $f+at$, up to affine output changes. The shift lemma makes at most one of them geometrically decomposable, and Cohen's theorem makes at most one a permutation when $p>D^4$. Among the at least three nonlinear forms, some form $g$ is therefore primitive and nonpermuting.

Actual degrees at most thirty-one are covered by the fixed-degree proof with coefficient below $1793/1000$, uniformly outside a fixed finite prime set; their constants can be absorbed in $C,p_0$. In these finitely many cases the boundary proof marks at most three roots, so completion needs only seven interval forms and gives $O(\sqrt p(1+\log p)^7)$ with a fixed constant. The earlier coarser exponent $2d+1$ is unnecessary here. For $d=\deg f>31$, the tame primitive classification leaves only $S_d,A_d$ and prime-degree cyclic or dihedral groups.

If $g$ is a coordinate and its geometric group is $S_d$ or $A_d$, the three-root Bonferroni upper bound for its image gives proportion at most $2/3$ with error $O(d^3/\sqrt p)$. The interval version uses the same completed three-root covers and gives coordinate capacity at most $4/3$ plus an error absorbed above. The tuple estimates needed for this statement are proved below. If $g$ is a diagonal, use the six-root marked-deficit argument that follows.

For cyclic or dihedral $g$, the arithmetic normalizer argument in Theorem 4.15 applies: a coset outside the geometric multiplier subgroup would make $g$ exceptional and a permutation, contrary to its choice. The remaining coset gives clipped coefficient $4/d$ or $1+2/d$. Their Galois closures have genus zero and degree at most $2d$, so complete counts and interval character sums have polynomial error absorbed by the displayed estimate. A coordinate gives a stronger line-capacity bound directly. For a diagonal, the same enclosure/support-count argument as in Theorem 4.15 gives a coefficient at most $23/14<1799/1000$ for $d\ge21$. No marked-root independence is asserted for these groups.

The remaining diagonal argument works in this general affine embedding; it does not need either coordinate to permute. On $g=X\pm Y=b$, one has $X(t)=\kappa t+\eta b+$constant with $\kappa\ne0$. Every residue has selected capacity at most twice the smaller number of its actual rows and columns, even when distinct residues share a residue column. The total-support estimate in windows $p\le n\le3p/2$ also remains valid: every nonzero linear combination of $X,Y$ is nonconstant, so completed polynomial sums give $(1+\delta)^2p+O(d\sqrt p\log^2p)$ support points, where $n=(1+\delta)p$.

**Pointwise marked-deficit lower bounds.**

Let $T$ be a finite set of size $R$, let $s\ge0$, and assign a nonnegative symmetric weight $w(A)$ to every $s$-subset $A\subseteq T$. For an odd integer $m\ge1$, define
$$
 L_{s,m}(T)=\sum_{\substack{A\subseteq T\\|A|=s}}w(A)
 \sum_{j=0}^m(-1)^j\binom{R-s}{j},
$$
with the entire expression zero if $R<s$. Then pointwise
$$
 L_{s,m}(T)\le 1_{R=s}w(T).
$$
If $R=s$ there is one subset and the inner sum is one. If $R>s$, the inner sum is $(-1)^m\binom{R-s-1}{m}\le0$, with the usual zero convention; every outer weight is nonnegative. This proves the inequality for every fiber, without averaging or a probabilistic assumption.

Expanding the binomial coefficient gives the exact identity
$$
 L_{s,m}(T)=\sum_{j=0}^m(-1)^j
 \sum_{\substack{A,B\subseteq T,\ A\cap B=\varnothing\\|A|=s,\ |B|=j}}w(A).
$$
Thus it is a linear combination of ordered-distinct-$(s+j)$-root counts, with coefficient $(-1)^j/(s!j!)$, and only the first $s$ roots are marked in the weight. In particular, odd truncation orders $(5,5,3,3)$ for $s=0,1,2,3$ use at most six roots.

**The nonnegative deficits in the window proof.**

For $k=1$ and $L=3,4$, the capacity is
$$
 \min(R+Z,L)=L-\sum_{s=0}^{L-1}1_{R=s}(L-s-Z)_+.
$$
Use the lemma with $w(A)=(L-s-|A\cap J_b|)_+$, which is symmetric and nonnegative. Subtracting the resulting lower bounds gives the required upper bound. No assumption about the sign of a truncated approximation is needed.

For $k\ge2$, remove the base $k\min(R,2)$. On a fiber with one extra diagonal line, an upper bound for the extra is
$$
 u_1(R,Z)=1-1_{R=0}-1_{R=1}(1-Z)-1_{R=2}1_{Z=0}.
$$
It equals $0,Z,\min(Z,1),1$ for $R=0,1,2,\ge3$, respectively. The three deficits use weights $1$, $1-|A\cap J_b|$ on a singleton, and $1_{A\cap J_b=\varnothing}$ on a pair, all nonnegative.

With two extra diagonal lines, the corresponding bound is
$$
 u_2(R,Z)=2-2\,1_{R=0}-1_{R=1}(2-Z)-1_{R=2}(2-Z).
$$
It equals $0,Z,Z,2$ in the same cases. Its weights are $2$, $2-|A\cap J_b|$ on a singleton or pair, again nonnegative. Fibers with no extra diagonal line have $J_b$ empty and contribute no extra, up to the already controlled discrete endpoints.

The lemma therefore applies to every subtraction used in the boundary proof. After uniform tuple averaging, the virtual probabilities are
$$
 q_s=\frac1{s!}\sum_{j=0}^{m_s}\frac{(-1)^j}{j!}:
 \quad(q_0,q_1,q_2,q_3)=(11/30,11/30,1/6,1/18).
$$
The averaged extras are precisely
$$
 E_1(q)=1-q_0-q_1(1-q)-q_2(1-q)^2,
 \quad E_2(q)=2-2q_0-q_1(2-q)-2q_2(1-q).
$$
They have the nonnegative boundary gaps already proved in Section 4.14, with virtual mean $9/10$. The actual base can independently use the six-moment upper bound $323/360$; summing two valid upper bounds does not require their virtual probabilities to describe one common distribution.

**Uniform marked-root averages using six-root covers.**

Suppose a degree-$d>31$ diagonal polynomial has geometric group $S_d$ or $A_d$, and $p>d^4$. Each ordered-distinct-$\ell$-root cover, $1\le\ell\le6$, is geometrically connected. For inertia $\sigma$, Burnside and a union bound give
$$
 \operatorname{ind}_{\ell}(\sigma)
 \le\ell(d-1)_{\ell-1}\operatorname{ind}_1(\sigma).
$$
Indeed a moved tuple has at least one moved coordinate; average that inequality over powers of $\sigma$. Since the sum of original inertia indices is $2d-2$, tame Riemann–Hurwitz gives genus $O_\ell(d^\ell)$. Deleting branch points costs $O_\ell(d^{\ell+1})$, absorbed by $O_\ell(d^\ell\sqrt p)$ under $p>d^4$.

At infinity, the inertia $d$-cycle acts freely on every nonempty ordered tuple, so target pole orders on these covers are $d$ and marked-root pole orders are one. Total pole degree is $O_\ell(d^\ell)$. The augmentation-module argument proves that a nonzero linear combination of at most three marked roots and the target is nonconstant. Its pole orders are at most $d<p$, excluding Artin–Schreier. The complete additive sum is therefore $O_\ell(d^\ell\sqrt p)$ with constants depending only on $\ell\le6$.

On a physical diagonal $g=X\pm Y=b$ of an invertible affine polynomial embedding, $X(t_i)=\kappa t_i+\eta b$ with $\kappa\ne0$. Thus each root-membership condition in $I\times J$ is a pair of linear interval constraints in the target and marked parameter root. A nonzero collected frequency is a nonzero phase of the preceding kind. At most three marks and one target interval require at most seven interval forms. Their normalized Fourier norms give an error
$$
 O\bigl(d^6\sqrt p(1+\log p)^7\bigr)
$$
for each averaged deficit, with an absolute constant. The zeroth frequency is the exact finite-field volume: independently uniform marked coordinates have membership probability $q_b=|J_b|/p$, so the weight averages give the stated binomial polynomials. There are at most eight membership patterns and finitely many truncation terms, so no hidden factor grows with $d$.

The six-moment base has the same estimate without root-position constraints. It remains to turn the virtual coefficient $9/5$ into a strict gap; the next rational split supplies that step.

Combine this with the previously proved six-moment integral-window coefficient $c_6=323/180$. Write $n=kp+r$, $\delta=r/p$.

* For $k\ge2$, use the true six-moment base $kc_6/2$, while the virtual extra is at most $\delta(9/10)$. The coefficient is at most $(2/3)c_6+(1/3)(9/5)=97/54<1799/1000$.
* For $k=1$, $\delta\le1/2$, count all support points: the coefficient is at most $1+\delta\le3/2$.
* For $k=1$, $1/2\le\delta\le199/200$, the existing boundary formula gives
$$
\frac{(9/5-B(\delta))(1+\delta)}{1-\delta}
=\frac23\left(3q_1\delta+q_2(14\delta^2-4\delta+2)+24q_3(1-\delta)^2(2\delta-1)\right).
$$
Here $14\delta^2-4\delta+2\ge7/2$ and $(1-\delta)/(1+\delta)\ge1/400$. The deficit is at least $\frac1{400}\frac23(11/20+7/12)=17/9000$. The coefficient is at most $16183/9000<1799/1000$.
* For $k=1$, $\delta\ge199/200$, enclose the window in a side-$2p$ square and use the integral six-moment estimate. Its normalized coefficient is at most $2c_6/(1+\delta)\le340/189<1799/1000$.

All these inequalities have a fixed rational margin below $1799/1000$. The accumulated error, divided by $n\ge kp$, is $O(d^6(1+\log p)^7/\sqrt p)$ with an absolute constant. This proves the prime estimate. The exact source `six_root_window_certificate.py/.json` verifies the rational gap identities and split; the pointwise lemma and tuple-cover argument above establish their all-degree applicability.

For $N=pm$ with $p\nmid m$, the usual complementary fibers give affine polynomial graphs of degree at most $D_N$ in rectangles enclosed by side-$\lceil n/m\rceil$ squares. For $n\ge N$ the enclosure error is $O(1/p)$ after normalization, and summation preserves the normalized analytic error. The degree-independent square-factor estimate forces $P(N)\to\infty$ on any positive-density sequence, and a repeated largest prime forces density to zero. In the stated growth range, $p>D_N^4$ eventually and $D_N^6(1+\log p)^7/\sqrt p=o(1)$ at $p=P(N)$. This proves the composite conclusion.

## 5. Taylor pieces and partial-lift lattice bounds

The results in this section permit arbitrary selected copies. They use ordinary integer-line covers of affine lattice cosets.

**Lemma 5.1 (lattice cover).** Let $\Lambda\subseteq\mathbb Z^2$ have index $L$. Every affine coset of $\Lambda$, restricted to an integer rectangle with both side lengths at most $m$, has no-three capacity at most
$$
 2\left(\left\lfloor\frac{k(m-1)}L\right\rfloor+1\right)
 \quad\text{for some }1\le k\le2\lfloor\sqrt L\rfloor.
 \tag{5.1}
$$

Among the $(\lfloor\sqrt L\rfloor+1)^2>L$ integer points of a square, two lie in the same lattice coset. Their difference is a nonzero $w\in\Lambda$ with $\|w\|_\infty\le\lfloor\sqrt L\rfloor$. Put $k=|w_x|+|w_y|$. Determinants of two lattice vectors are divisible by the lattice index. Thus $\det(w,z-z_0)$ takes values in $L\mathbb Z$ as $z$ ranges over an affine coset. Across the rectangle its range has length at most $k(m-1)$. Each possible value is an actual line parallel to $w$, even if $w$ is not primitive in $\mathbb Z^2$. Capacity two proves (5.1).

**Theorem 5.2 (polynomial Taylor pieces).** Suppose $N=hL$ and $N\mid h^2$. Let $S$ be a no-three subset of the lift of an invertible affine image modulo $N$ of any integer polynomial graph. The degree and coefficients may vary freely. In a translated square of side $n$,
$$
 |S|\le\frac{4\lfloor\sqrt L\rfloor}{L}\,n+2h.
 \tag{5.2}
$$
If $n=tN$ with integer $t\ge1$, the boundary term disappears:
$$
 |S|\le\frac{4\lfloor\sqrt L\rfloor}{L}\,n.
 \tag{5.3}
$$

Write the parameter as $a+hu$, where $a$ ranges modulo $h$ and $u$ modulo $L$. Taylor expansion gives the exact congruence
$$
 f(a+hu)\equiv f(a)+hf'(a)u\pmod N,
 \tag{5.4}
$$
since all omitted terms are divisible by $h^2$. Under the affine map with invertible linear part $U$, the $h$ parameter classes occupy distinct two-dimensional classes modulo $h$. In each, subtracting its offset and dividing coordinates by $h$ produces a modular affine line modulo $L$, with direction $U(1,f'(a))$. The direction is unimodular: its coordinates generate the unit ideal modulo $L$. Its cyclic line has $L$ points and its inverse image in $\mathbb Z^2$ is a lattice coset of index $L$.

For an arbitrary window, each local coordinate interval contains at most $m=\lceil n/h\rceil$ integers. Lemma 5.1 and $m-1<n/h$ bound its capacity by $4\lfloor\sqrt L\rfloor n/(hL)+2$. Summing over $h$ classes proves (5.2).

If $n=tN$, every local interval has exactly $tL$ integers. For the $k$ in Lemma 5.1,
$$
 \left\lfloor\frac{k(tL-1)}L\right\rfloor+1
 =tk-\lceil k/L\rceil+1\le tk.
$$
Each class then contributes at most $2tk\le4t\lfloor\sqrt L\rfloor$, proving (5.3). No argument requires that all copies of a selected residue be kept.

Take
$$
 h=\prod_{p^e\parallel N}p^{\lceil e/2\rceil},
 \qquad L=\prod_{p^e\parallel N}p^{\lfloor e/2\rfloor}.
 \tag{5.5}
$$
For odd nonsquarefree $N$, the integer $L$ is odd and at least three. The coefficient in (5.3) is at most $8/5$: it is $4/3,8/5,8/7$ at $L=3,5,7$, and at most $4/\sqrt L\le4/3$ for $L\ge9$. Thus arbitrary partial selections in integral-period windows are excluded from density $1.8$ for every odd nonsquarefree modulus.

For even moduli the same formula applies, but its coefficient can equal two at $L=2,4$. The full-lift parity argument in Section 4 must not be imported to arbitrary partial selections. There is, however, an attributed completion using the checkerboard theorem of Aujla, Prellberg and Sandhu [26, Theorem 1.3]. Modulo two the entire affine graph is a line. An axial line permits points in only one parity of rows or columns, giving $n+O(1)$. The other line direction is a monochromatic checkerboard class. Their published theorem gives $\alpha n+O(1)$, uniformly for either color, where $1.576823396873<\alpha<1.576823396874<8/5$. Thus every even modulus has this partial-copy bound for arbitrary windows. Together with the elementary odd-modulus estimate above, every nonsquarefree modulus has partial-copy capacity at most $(8/5)n+O(1)$ in integral-period windows. The checkerboard estimate is an imported result, not a new coefficient here. For either parity the lattice coefficient itself tends to zero when $L\to\infty$.

**Theorem 5.3 (smooth curves over prime powers).** Let $F\in\mathbb Z[x,y]$ have total degree at most $d$, with nonzero reduction modulo a prime $p$. Suppose every affine zero modulo $p$ is smooth. For $e\ge2$, put
$$
 N=p^e,\qquad h=p^{\lceil e/2\rceil},\qquad L=p^{\lfloor e/2\rfloor}.
$$
Every no-three subset of $F(x,y)=0\pmod N$ in a translated side-$n$ square satisfies
$$
 |S|\le\frac{4d\lfloor\sqrt L\rfloor}{L}\,n+2dh.
 \tag{5.6}
$$
For $n=tN$, the bound improves to
$$
 |S|\le\frac{4d\lfloor\sqrt L\rfloor}{L}\,n.
 \tag{5.7}
$$

The elementary polynomial zero bound gives at most $dp$ affine zeros modulo $p$. Each smooth zero has exactly $p$ lifts at every additional digit: two new digits satisfy one nonzero linear equation. Therefore there are at most $dh$ root classes $z_0$ modulo $h$. In each,
$$
 F(z_0+hu)\equiv F(z_0)+h\nabla F(z_0)\cdot u\pmod N.
$$
At least one gradient coordinate is a unit modulo $p$, hence modulo $L$. The local congruence
$$
 \nabla F(z_0)\cdot u\equiv-F(z_0)/h\pmod L
$$
defines an affine lattice coset of index $L$. Apply the same rectangle and integral-period arguments as in Theorem 5.2 and sum over at most $dh$ classes.

For fixed $d$, (5.6) implies $|S|=o(n)$ whenever $n\ge N$ and $L\to\infty$. If a larger modulus has $p^e$ as a divisor, dropping its other congruence conditions gives the same upper bound. Smoothness is a substantive hypothesis. Polynomial graphs have exactly $h$ root classes, independently of degree, which explains the degree-free version in Theorem 5.2.

**Corollary 5.4 (reduced curves with singular roots).**

The smooth-root estimate extends to reduced curves, with an explicit cost for singular residue classes. Suppose $F$ has total degree $d$, its projective reduction is geometrically reduced, and $p>d$. Let $N=p^e$, $e\ge2$, $h=p^{\lceil e/2\rceil}$, $L=p^{\lfloor e/2\rfloor}$. In any translated side-$n$ square, a no-three subset of $F=0\pmod N$ has size at most
$$
 \frac{4d\lfloor\sqrt L\rfloor}{L}n+2dh
 +2d(d-1)\lceil n/p\rceil.
$$
For integral-period windows $n=tN$, the sharper form is
$$
 |S|\le\left(\frac{4d\lfloor\sqrt L\rfloor}{L}+\frac{2d(d-1)}p\right)n.
$$

**Proof.** Separate the smooth and singular residue roots modulo $p$. Over smooth roots, the Hensel/Taylor argument of Theorem 5.3 gives at most $dh$ smooth root classes modulo $h$ and exactly the original lattice bound (the presence of other singular roots does not affect these classes). The reduced-curve polar argument bounds the number of singular projective roots by $d(d-1)$. Above each singular affine root, all points have one fixed pair of coordinate residues modulo $p$, hence lie on at most $\lceil n/p\rceil$ actual integer rows. Capacity two bounds that entire fiber by $2\lceil n/p\rceil$, without assuming any lifting behavior. Summing proves both claims.

For fixed degree, $p\to\infty$, arbitrary $e\ge2$, and $n\ge N$, this is $o(n)$ uniformly: $L\ge p$, $h/n\le1/L$, and the singular term is $O_d(n/p)$. It does not imply $o(n)$ for fixed $p$ and $e\to\infty$; the singular contribution then remains a fixed fraction. At $e=2,n=p^2$ it gives Proposition 6.4 below.

### 5.4 Prime periods suffice for the asymptotic polynomial full-lift problem

Let $\beta(q)$ be the largest residue-set size whose full lift to a side-$2q$ square has no three integer-collinear points, with no support restriction. Let
$$
 A(N)=\max\frac{|L_N(R)|}{2N},
$$
where the maximum is over subsets of invertible affine images of integer polynomial graphs modulo $N$, of arbitrary degree and coefficients, whose full lifts are no-three.

**Theorem 5.5 (prime-period reduction).**
$$
 \limsup_{N\to\infty}A(N)
 =\limsup_{\substack{q\to\infty\\q\ \mathrm{prime}}}\frac{2\beta(q)}q.
$$
In particular, from any unbounded polynomial full-lift family of density strictly above$1.8$, one can extract an unbounded prime-period full-lift family with density at least as large at every extracted size. This is a reduction of construction mechanisms, not a new construction or an unrestricted upper bound.

**Proof.** Section 4.6 gives, for every$q\mid N$,
$$
 A(N)\le\frac{2\beta(q)}q.
$$
Indeed, with$m=N/q$, there are exactly$m$ occupied support classes modulo$m$. Each becomes a canonical local side-$2q$ square after subtracting its first coordinates and dividing by$m$. Averaging chooses a local full lift of density at least the global density.

It remains to ensure extracted prime periods are unbounded; an arbitrary prime divisor would not suffice. Let
$$
 L=\prod_{p^e\parallel N}p^{\lfloor e/2\rfloor}.
$$
Theorem 5.2 gives $A(N)\le4/\sqrt L$. Thus on a sequence with$A(N)\ge\varepsilon>0$, the integer$L$ is bounded by$16/\varepsilon^2$. Writing$N=L^2K$, the integer$K$ is squarefree. If the largest prime factor of$N$ were bounded along an unbounded subsequence, then$K$ and hence$N$ would be bounded, a contradiction. Therefore the largest prime$q$ tends to infinity on every unbounded positive-density sequence. Applying the divisor bound with this$q$ proves the upper limsup inequality.

Conversely, every feasible prime-period residue set has injective$x$ by full-copy thinning. Interpolate its$y$ values as a polynomial over$\mathbb F_q$, filling unused$x$ values arbitrarily. Hence it is contained in a polynomial graph, and$A(q)=2\beta(q)/q$. Taking prime periods proves the reverse inequality.

For a strict super-$1.8$ family, choose its largest prime factor and the densest complementary residue fiber. The affine scaling of that fiber explicitly produces the extracted points. Uniform prime-factor growth follows from the argument above, so the extracted sizes$2q$ are unbounded. No efficiency guarantee is claimed for finding the original family; the reduction itself is finite and exact.

The polynomial congruence structure and full-copy selection are essential. This reduction does not apply to arbitrary composite residue supports or partial selections.

## 6. Sharp prime-square conic and cubic capacities

The exponent in the prime-square upper bound is sharp for every nonsingular conic.

**Theorem 6.1.** Let $p$ be a sufficiently large odd prime. Let $F$ be an integer quadratic polynomial whose projective reduction modulo $p$ is nonsingular. In any translated square of side $p^2$, let $C$ be the full support $F(x,y)=0\pmod{p^2}$. Then
$$
 \frac1{256}p^{3/2}\le\alpha(C)
 \le4(p+1)\lfloor\sqrt p\rfloor.
 \tag{6.1}
$$
The constants are absolute, independent of coefficients and placement. Hence $\alpha(C)=\Theta(p^{3/2})=\Theta(n^{3/4})$ for board side $n=p^2$.

### 6.1 Exact tangent-fiber decomposition

Partition the support by its residue point $a$ modulo $p$. There are between $p-1$ and $p+1$ affine points on the residue conic. Every one is smooth and has exactly $p$ lifts modulo $p^2$. After subtracting a class offset and dividing integer coordinates by $p$, the fiber is an affine modular line inside a translated $p$-square. Its direction is the tangent direction to the residue conic at $a$.

Three points in three distinct fibers cannot be collinear: their reductions lie on a nonsingular conic over $\mathbb F_p$, an arc. Suppose $P,Q$ belong to one fiber and $R$ to another. Write $Q-P=pw$. The vector $w$ is nonzero modulo $p$, since the local square has side $p$ and its two points are distinct. Taylor expansion shows $\nabla F(a)\cdot w=0\pmod p$, so $w$ is a tangent direction. The tangent line at $a$ contains no other point of the conic. Therefore
$$
 p^{-1}\det(Q-P,R-P)\ne0\pmod p,
$$
and the original integer determinant is nonzero.

It follows that every forbidden triple lies in one fiber. Capacity therefore decomposes exactly:
$$
 \alpha(C)=\sum_{a\in C(\mathbb F_p)}
 \alpha(\text{local tangent-line fiber at }a).
 \tag{6.2}
$$
This identity permits independent local constructions; no compatibility condition across fibers remains.

For a local index-$p$ lattice, Lemma 5.1 supplies a vector with $k\le2\lfloor\sqrt p\rfloor<p$. Across a $p$-square there are at most
$$
 \left\lfloor k(p-1)/p\right\rfloor+1=k
$$
parallel determinant levels. Its no-three capacity is at most $2k\le4\lfloor\sqrt p\rfloor$. Summing proves the upper bound in (6.1).

### 6.2 Uniform construction inside most tangent lattices

Put $r=\lfloor\sqrt p/4\rfloor$. Fewer than $p/4$ projective directions admit a nonzero integer vector of infinity norm less than $r$: there are only $(2r-1)^2-1<p/4$ such vectors, and each has a single projective direction modulo $p$. Call all other directions good.

For a nonsingular conic at most two tangent points have any specified direction. Indeed they satisfy the conic equation and a nonzero polar-line equation, so Bézout gives at most two. Therefore at least $p/2-1$ affine conic points have good tangent directions.

We show that every affine index-$p$ lattice coset with a good direction contains a no-three set of size at least $\sqrt p/64$ in any $p$-square. A shortest Euclidean lattice vector $w$ satisfies, for sufficiently large $p$,
$$
 \sqrt p/5\le |w|_2\le\sqrt{2p}.
$$
The upper bound follows from the square pigeonhole argument, and the lower bound from goodness. A shortest vector is primitive in the lattice and extends to a lattice basis $(w,z)$. Subtracting the nearest integer multiple of $w$ from $z$, its parallel component has magnitude at most $|w|/2$, while its perpendicular component has magnitude $p/|w|$. Hence
$$
 |z|_2\le\sqrt{p^2/|w|_2^2+|w|_2^2/4}<6\sqrt p,
 \qquad \|w\|_\infty+\|z\|_\infty<8\sqrt p.
$$

Round the two basis coordinates of the center of the $p$-square to obtain a point $z_0$ of the affine coset within infinity distance $4\sqrt p$ of that center. Set $m=\lfloor\sqrt p/32\rfloor$. For $p\ge4096$, the affine grid
$$
 z_0+iw+jz,\qquad -m\le i,j\le m,
$$
lies inside the square because its distance from the center is at most
$$
 4\sqrt p+8m\sqrt p\le4\sqrt p+p/4<(p-1)/2.
$$
Choose a prime $\ell$ with $m<\ell<2m$, using Bertrand's postulate. The $\ell$ points $y=x^2\pmod\ell$ in an $\ell$-square have no three integer collinear points: a nonzero determinant modulo $\ell$ remains nonzero over the integers. Embed this square in the basis grid. Its affine image is still no-three, and $\ell>m\ge\sqrt p/64$.

By (6.2) the local constructions combine freely. For sufficiently large $p$,
$$
 (p/2-1)\sqrt p/64\ge p^{3/2}/256,
$$
proving the lower bound in (6.1).

### 6.3 The standard parabola and finite controls

For $F=y-x^2$ and the canonical side-$p^2$ square, the decomposition is explicit. Write
$$
 b_a=a^2\bmod p,\qquad c_a=(a^2-b_a)/p.
$$
The fiber at $(a,b_a)$ is
$$
 (x,y)=(a+pu,b_a+pv),\qquad
 0\le u,v<p,\qquad v\equiv2au+c_a\pmod p.
 \tag{6.3}
$$
The slopes $2a$ traverse all of $\mathbb F_p$, so the preceding lower-bound argument even gives $p^{3/2}/128$.

The finite checker solves each local line support to proven integer optimality and independently checks all directions among the combined integer points. It also verifies every congruence $y=x^2\pmod{p^2}$. Equation (6.2) then turns the local optima into exact restricted optima:

| $p$ | Board side $p^2$ | Restricted optimum |
|---:|---:|---:|
| 5 | 25 | 16 |
| 7 | 49 | 26 |
| 11 | 121 | 52 |
| 19 | 361 | 130 |
| 31 | 961 | 272 |
| 43 | 1849 | 448 |
| 59 | 3481 | 718 |

These computations are independent finite controls of the decomposition and constructions. The asymptotic exponent follows from the proof, not from fitting the table.

### 6.4 Separation at higher prime powers

**Proposition 6.2 (higher-power separation).** Let $p$ be an odd prime, $e\ge2$, and let $F\in\mathbb Z[x,y]$ be quadratic with nonsingular projective reduction modulo $p$. Let $C$ be any finite set of integer points satisfying $F(P)=0\pmod{p^e}$ such that reduction of $C$ modulo $p^e$ is injective. Partition $C$ by its residue points modulo $p$. Every integer collinear triple in $C$ lies in one part. Consequently
$$
 \alpha(C)=\sum_{a\in C\bmod p}\alpha(C_a).
$$
In particular this applies to the full solution support in every translated square of side at most $p^e$.

**Proof.** Three distinct residue fibers are separated by the arc property of a nonsingular conic. Otherwise take $P,Q$ from the same fiber and $R$ from another. Put
$$
 k=\min\{v_p(Q_x-P_x),v_p(Q_y-P_y)\},\qquad Q-P=p^k w,
$$
with $v_p(0)=+\infty$. The hypotheses give $1\le k<e$ and $w\ne0\pmod p$. The exact quadratic Taylor identity and divisibility of $F(Q)-F(P)$ by $p^e$ imply
$$
 \nabla F(P)\cdot w=0\pmod p.
$$
Thus $w$ is the tangent direction at $a=P\bmod p$. The tangent there contains no other point of the residue conic, so
$$
 \det(w,R-P)\ne0\pmod p.
$$
The integer determinant equals $p^k\det(w,R-P)$ and is nonzero. This also shows its exact $p$-adic valuation is $k$. Only within-fiber triples can therefore be forbidden, proving the sum identity.

The same proof works for a general integer polynomial whose residue zero set is an arc and whose smooth tangent at each residue zero contains no other residue zero. Both the arc and the tangent-separation hypotheses are needed in that formulation.

**What does not follow.** At $e=2$ the local support is an index-$p$ affine lattice in a $p$-square, which enabled the matching $\Theta(p^{3/2})$ theorem. For $e>2$ the Taylor remainder persists within a modulo-$p$ fiber, so the same local-lattice lower construction does not apply. The general prime-power matching exponent remains open. Nor may injectivity modulo $p^e$ be omitted when taking larger windows.


### 6.5 Matching capacity for geometrically irreducible cubics

**Theorem 6.3.** Let $p>3$ be sufficiently large and let $F\in\mathbb Z[x,y]$ have degree three with geometrically irreducible projective reduction modulo $p$. Let $C$ be its full solution support modulo $p^2$ in any translated square of side $p^2$. Then
$$
 \frac{p^{3/2}}{1024}\le\alpha(C)
 \le4(p+1+2\sqrt p)\lfloor\sqrt p\rfloor+2p.
 \tag{6.4}
$$
The constants are uniform in coefficients and placement. If the residue cubic is smooth, the final $2p$ term may be removed. If it is singular, the upper bound improves to $4(p+1)\lfloor\sqrt p\rfloor+2p$.

We first prove the smooth case, then treat singularities. Hasse's bound [16] gives at most $p+1+2\sqrt p$ affine root classes. Every smooth fiber is an index-$p$ tangent-line lattice in a local $p$-square, so the same line cover as in Theorem 6.1 proves the upper bound.

**A tangent-avoiding base arc.**

The projective cubic has a rational point by Hasse [16]. Choose one as origin, identifying its rational points with a finite abelian group $G$. There is a fixed element $T\in G$ such that three points, counted with intersection multiplicities, lie on a line if and only if their sum is $T$. The origin need not be a flex: $T$ is the hyperplane divisor class after subtracting three origins.

The standard elliptic-group structure theorem [16] gives $G\simeq\mathbb Z/a\times\mathbb Z/b$ with $a\mid b$, hence a cyclic quotient of order $b\ge\sqrt{|G|}$. Write $M=b$, let $\phi:G\twoheadrightarrow\mathbb Z/M$, and put $\tau=\phi(T)$. Choose an integer $A$ for which
$$
 3A-\tau\equiv d\pmod M,\qquad d\in\{1,2,3\}.
$$
Such a choice exists since $\gcd(3,M)$ is one or three. Put $k=\lfloor M/3\rfloor-1$ and take the cyclic interval
$$
 I=\{A,A+1,\ldots,A+k-1\}\pmod M.
$$
For three elements of this interval, their sum minus $\tau$ has a representative between $d$ and $d+3(k-1)$, which lies strictly between zero and $M$. Thus the preimage $B=\phi^{-1}(I)$ contains no solution of
$$
 P+Q+R=T,
$$
even when points repeat. Its size is at least $|G|/3-2\sqrt{|G|}$. After removing at most three points at infinity, $B$ is an affine arc and the tangent at every point of $B$ contains no other point of $B$.

This is a classical use of the elliptic group law to construct arcs on cubic curves [17, 18]; no new finite-field arc construction is claimed. The repeated-point exclusion is included because ordinary arc status alone would not separate two lifts in one fiber from a third lift in another.

**Good tangent directions.**

Let $r=\lfloor\sqrt p/16\rfloor$. Fewer than $4r^2\le p/64$ projective directions contain a nonzero integer vector of infinity norm less than $r$. For any direction $w$, points of the cubic with that tangent direction solve $F=0$ together with the directional polar equation $w\cdot\nabla F=0$. The polar has degree two and is nonzero for a smooth cubic in characteristic greater than three. It shares no component with the irreducible cubic. Bézout therefore bounds their number by six.

Remove all such bad tangent points from $B$. At least
$$
 \frac{|G|}{3}-2\sqrt{|G|}-3-\frac{3p}{32}
 \ge\frac p5
$$
points remain for sufficiently large $p$, by Hasse. Denote this subset by $B_0$.

**Local construction and separation.**

At each $a\in B_0$, the solutions modulo $p^2$ in its residue class form an affine coset of an index-$p$ tangent lattice, in a local square of side $p$. Its shortest Euclidean lattice vector $w$ satisfies
$$
 \sqrt p/17\le |w|_2\le\sqrt{2p}
$$
for sufficiently large $p$. Complete it to a reduced lattice basis $(w,z)$ with
$$
 |z|_2\le\sqrt{p^2/|w|_2^2+|w|_2^2/4}<18\sqrt p,
 \qquad \|w\|_\infty+\|z\|_\infty<20\sqrt p.
$$
Rounding basis coordinates places a coset point within $10\sqrt p$ of the local square center. With $m=\lfloor\sqrt p/80\rfloor$, the basis grid with coordinates in $[-m,m]^2$ lies inside the square: its distance from the center is at most $10\sqrt p+p/4<(p-1)/2$. Bertrand's postulate supplies a prime $m<\ell<2m$. A modular parabola over $\mathbb F_\ell$, embedded in this basis grid, gives more than $m\ge\sqrt p/160$ points with no three integer-collinear.

These local constructions combine freely over $B_0$. Three different base fibers cannot be collinear, by the arc property. If two points $P,Q$ are in the fiber at $a$ and the third is in the fiber at $b\ne a$, write $Q-P=pv$. The local square has side $p$, so $v$ is nonzero modulo $p$. Taylor expansion makes it tangent at $a$. The tangent exclusion ensures $\det(v,b-a)\ne0\pmod p$, hence $\det(Q-P,R-P)$ is nonzero over the integers. All remaining triples lie inside a single local construction and are already excluded.

The union has at least $(p/5)(\sqrt p/160)=p^{3/2}/800$ points; the stated $1/1024$ constant is a conservative weakening. All estimates hold, for example, once $p\ge10^6$. No constant is optimized.

**Singular irreducible cubics.** A geometrically irreducible singular cubic has a unique projective singular point. Its smooth rational locus, with a rational smooth origin, has the classical additive, split multiplicative, or nonsplit multiplicative group structure [16, Chapter II, Section 3, pp. 56–58]. These are cyclic groups of orders $p$, $p-1$, and $p+1$, respectively. The chord-and-tangent law again has a fixed hyperplane target $T$, allowing a nonflex origin. One can see this on normalization: the smooth locus is a projective line with one or two points removed; divisor classes are given by an additive parameter in the cuspidal case, a ratio in the split nodal case, and its norm-one descent in the nonsplit case. A hyperplane divisor has a fixed class.

The cyclic interval above therefore applies with $M\in\{p-1,p,p+1\}$. Removing at most three points at infinity leaves at least $(p-1)/3-5$ affine points. The degree-two directional polar is nonzero and shares no component with the irreducible cubic, so the same six-point tangent bound holds. After bad directions are removed, at least $p/5$ good roots remain for sufficiently large $p$. Their local lattice constructions combine by the same arc and tangent exclusions. This proves the lower bound without using the singular fiber.

For the upper bound, there are at most $p+1$ smooth roots. At a singular affine residue $a$, Taylor expansion gives $F(a+pu)\equiv F(a)\pmod{p^2}$. Its local fiber is empty or the entire $p$-square, of no-three capacity at most $2p$ by rows. There is at most one such residue, proving the stated upper bound.

Exact additivity of the entire cubic support is not asserted. The lower construction uses a selected tangent-avoiding arc; the entire support can have collinear triples crossing base fibers.

**Finite and constructive checks.** Independent small-field checks of the smooth case verify 4,935 arbitrary-target cyclic intervals, 21,834 elliptic-group additions including noncyclic groups, 1,308 tangent exclusions, and 15,552 integer triples in 30 lifted examples. Singular checks verify 150 examples, 5,468 tangent exclusions and 52,408 integer triples. The split-node family $XYZ=\lambda X^3+Y^3$ is included for every nonzero $\lambda$ at the tested primes: its parametrization $[t^2:t:\lambda t^3+1]$ has collinearity target $t_1t_2t_3=-1/\lambda$, which need not be a cube. Thus the checks explicitly include cases with no rational flex.

The supplement also generates 108,910 points on $y^2=x^3+x+1\pmod{65537^2}$ in a square of side 4,295,098,369. It certifies a cyclic group of order 65,582 by complete group enumeration, selects the interval, checks tangent congruences, and verifies 217,820 within-fiber determinants. Cross-fiber exclusion follows from the verified group interval and the proved separation argument. This concrete generator is restricted to cyclic Weierstrass groups; the theorem also covers noncyclic groups and arbitrary plane cubics. No general claim is inferred from this example.

### 6.6 Reduced curves: an upper bound allowing singular roots

**Proposition 6.4.** Suppose the degree-$d$ projective reduction of $F$ is geometrically reduced and $p>d$. Its solution support modulo $p^2$ in any translated square of side $p^2$ satisfies
$$
 \alpha(C)\le4dp\lfloor\sqrt p\rfloor+2d(d-1)p.
 \tag{6.5}
$$
There are at most $dp$ affine roots. Over the algebraic closure, choose a generic degree-$(d-1)$ polar sharing no component with the reduced curve. Such a polar exists because the degree is below the characteristic and no component divides every partial derivative of a squarefree equation. Bézout bounds the number of singular points by $d(d-1)$. Smooth roots have the tangent-lattice bound, and each singular root has the $2p$ bound just proved. Summing gives (6.5). This proposition is an upper bound only; a matching lower exponent is not asserted for arbitrary degree.

## 7. The separate determinant-general CRT model

**Theorem 7.1.** Let $p$ be an odd prime and $N=2p$. Suppose $R\subseteq(\mathbb Z/N\mathbb Z)^2$ satisfies both of the following conditions:

1. Every triple of distinct points has nonzero determinant modulo $N$.
2. Each of $x,y,x-y,x+y$ is injective on $R$.

Then
$$
 |R|\le\frac85(p+3).
 \tag{7.1}
$$
Consequently its full lift in a square of side $n=4p$ has density at most $8/5+24/(5p)$, below $1.8$ for $p>24$.

### 7.1 The imported tangent inequality

We use Segre's envelope theorem [13, Theorem 39] through the following consequence proved in [14, Lemma 4]. Let $A$ be a projective arc over an odd field of order $p$, with $|A|=p+2-t\ge2t+2$. If $P\notin A$ cannot be added to $A$ while retaining the arc property, then at most $2t$ lines through $P$ are tangent to $A$.

For clarity, the consequence follows directly from the degree-$2t$ envelope of tangent lines in the dual plane. On the dual line representing the pencil through $P$, the envelope is not identically zero: a secant through $P$ evaluates nontrivially by the envelope identity at either of its points in $A$. Thus at most $2t$ points of that dual line can represent tangents. This is the only envelope result used below. We also use the classical bound $|A|\le p+1$ for projective arcs of odd order [13].

For an affine arc of size $s$, call a direction free if it has no secant. If $s>2p/3$, at most two directions are free. Indeed, if three infinity points individually extend the arc, add two of them. The resulting arc has size $s+2=p+2-(p-s)$. The third infinity point cannot extend it, and the $s$ lines from that point to the original affine points are tangents. The preceding inequality gives $s\le2(p-s)$, a contradiction. Its size hypothesis is $3s\ge2p$, which holds. If $p-s<1$, the augmented arc already violates the odd-order size bound.

If $3s\ge2p+6$ and a direction is nonfree, the same tangent inequality applied to the original arc gives at most $2(p+2-s)$ tangents in that direction. Writing $c$ for its secants, $s=2c+\text{tangents}$ gives
$$
 c\ge\frac{3s-2p-4}{2}\ge\frac32s-(p+3).
 \tag{7.2}
$$
When $3s\le2p+6$, the final expression is nonpositive, so the last inequality is valid without any nonfree assumption.

### 7.2 Four parity colors and their directional capacities

Partition $R$ into its four parity classes $00,01,10,11$, of sizes $m_i$. Put $M=\sum_i m_i$ and $L=p+3$.

Projection of the whole set into $\mathbb F_p^2$ is injective. Two coincident projections have a nonzero parity difference, respectively $(1,0),(0,1)$ or $(1,1)$. In these three cases their $y$, $x$ or $x+y$ values agree modulo both prime factors, violating condition 2. For each pair of colors, its projected union is an affine arc: any triple in two parity classes has zero determinant modulo two, so condition 1 makes its determinant nonzero modulo $p$.

Every color pair is forced free in the directions whose grid form agrees on its two parity values. Opposite pairs $00,11$ and $01,10$ are forced free in both diagonal directions. Each other pair is forced free in one axial direction. Designate exactly two free directions for every pair, including all forced ones. If its size $s$ makes the right side of (7.2) positive, include every actually free direction; there are at most two. Otherwise choose any two containing the forced directions. Every undesignated direction satisfies
$$
 c_{ij,d}\ge\frac32(m_i+m_j)-L,
 \tag{7.3}
$$
where $c_{ij,d}$ counts secants between the two colors in direction $d$.

A same-color pair cannot share a projected grid form, since its form values would then agree modulo $N$. On any fixed projected directional line there are at most two points of $R$, because its form value has only two extensions modulo $N$. Hence for every color $i$ and direction $d$,
$$
 \sum_{j\ne i}c_{ij,d}\le m_i.
 \tag{7.4}
$$

### 7.3 A four-color graph argument

For each of the four directions, form a graph $G_d$ on the four colors, putting an edge at every pair for which that direction was not designated free. Each $G_d$ is a subgraph of its parity $K_{2,2}$, and every color pair occurs in exactly two graphs. There are twelve edge occurrences altogether.

If some graph has four edges, it is a full $K_{2,2}$. Summing (7.3) on its edges gives $\sum c\ge3M-4L$. Summing (7.4) at its four vertices gives $2\sum c\le M$. Therefore $5M\le8L$.

Otherwise each graph has exactly three edges, and hence is a four-vertex path. Two of these paths are complementary as edge sets of $K_4$. To see this, choose either axial graph. It consists of the two opposite-color edges and one other edge $e$. Its complement consists of the other three nonopposite edges. Edge $e$ is already forced free in the other axial direction and occurs in the chosen axial graph, so its second designated free direction is diagonal. That diagonal graph misses $e$ and, having three edges, is precisely the complementary path.

Apply (7.4) at the two middle vertices of each of these complementary paths. Their middle edges are disjoint, so each color is charged once and the total upper bound is $M$. The left side counts all six edges of $K_4$ once, and counts the two middle edges a second time. This weighted graph has total edge weight eight and weighted degree four at every vertex. Applying (7.3) to its edges therefore gives a lower bound $6M-8L$. Again $5M\le8L$, proving (7.1).

This proof is analytic. A numerical relaxation suggested keeping the per-color inequalities, but no optimizer output is required for the theorem. The coefficient $8/5$ is sharp for these relaxed inequalities: masses $m_i=2L/5$ and secant counts $L/5$ on every designated edge satisfy them. This is not an assertion of a realizable residue configuration. The determinant hypothesis remains essential to the argument and is not implied by exact full-lift feasibility.

### 7.4 The modulus $3p$

**Theorem 7.2.** Let $p$ be an odd prime other than three. Suppose $R\subseteq(\mathbb Z/(3p)\mathbb Z)^2$ satisfies the two hypotheses of Theorem 7.1 with modulus $3p$. Then
$$
 |R|\le\frac{21}{8}(p+3).
 \tag{7.5}
$$
Its full two-period lift, on side $n=6p$, consequently has density at most
$$
 \frac{|L_{3p}(R)|}{n}\le\frac74+\frac{21}{4p},
 \tag{7.6}
$$
which is less than $1.8$ for $p>105$.

Unlike Theorem 7.1, this theorem uses a finite exact certificate. We first derive the model analytically, then describe its complete rational verification. The model and independent certificates were discussed in [15]. lattice_lift_research developed the model; kiro_c1_collinear independently certified a stronger numerical constant by enumerating affine-group orbits. Our supplement supplies a separate branch certificate for the simpler rational target $21/8$.

Color the residues by their nine points of $\mathbb F_3^2$. The four grid forms comprise all projective forms over $\mathbb F_3$. Thus projection of $R$ into $\mathbb F_p^2$ is injective: any nonzero difference of colors lies in the kernel of some grid form, which would otherwise agree modulo both primes. For each of the twelve affine color lines $\ell=\{L_d=t\}$, the projected points of its colors form an arc. A collinear projected triple in those colors would have zero determinant at both primes. Write $s_\ell$ for this arc's cardinality divided by $H=p+3$. The odd-order arc bound gives $s_\ell\le1$, and direction $d$ is free by thinning.

Each projected line in direction $e$ contains at most three points, with distinct color values under $L_e$. Its color set is an arc over $\mathbb F_3$, since any collinear color triple on it would violate determinant-generality. Thus its nonempty color pattern $A$ belongs to exactly 54 possibilities: nine singletons, 27 pairs with distinct $L_e$ values, and 18 noncollinear triples with distinct $L_e$ values.

Let $m_i$ be the number of points of color $i$ divided by $H$, and let $z_{e,A}$ be the number of projected direction-$e$ lines with pattern $A$, divided by $H$. Define the normalized secant count
$$
 c_{\ell,e}=\sum_{A:\,|A\cap\ell|=2}z_{e,A}.
$$
Patterns cannot have three colors in a color line. Therefore this is exactly the secant count of its arc, and the following inequalities hold:
$$
 \sum_A z_{e,A}\le1,\qquad
 \sum_{A\ni i}z_{e,A}=m_i,\qquad
 s_\ell=\sum_{i\in\ell}m_i\le1.
 \tag{7.7}
$$
All variables lie in $[0,1]$.

For each color line $\ell$ of direction $d$, introduce binary flags $b_{\ell,e}$ for $e\ne d$. If $3s_\ell/2-1>0$, flag all directions other than $d$ that are actually free for the arc. There is at most one, by Section 7.1. If the expression is nonpositive, set all these flags to zero. Then
$$
 \sum_{e\ne d}b_{\ell,e}\le1,\qquad
 c_{\ell,e}+b_{\ell,e}\le1,\qquad
 3s_\ell-2c_{\ell,e}-2b_{\ell,e}\le2.
 \tag{7.8}
$$
For an unflagged direction the last inequality is Segre's secant bound or is vacuous. For a flagged direction, $c_{\ell,e}=0$ and $s_\ell\le1$ imply it directly. Flags encode actual freedom when needed; it would be invalid to designate an arbitrary omission and simultaneously force its secant count to zero.

Equations (7.7) and (7.8), after replacing each equality with two inequalities, give 172 integer inequalities in 261 variables. Exactly 36 variables are binary. They are necessary conditions, with no assertion that a feasible point corresponds to a realizable residue set.

### 7.5 Exact certificate for the finite model

The supplement proves that this finite model satisfies
$$
 M:=\sum_{i=1}^9m_i\le21/8.
 \tag{7.9}
$$
This is proof-essential evidence for Theorem 7.2. Floating-point optimizers are used only to discover the tree and proposed dual weights. Verification uses only integers and rational numbers, with no optimizer dependency.

For context, the case with all flags zero has a short analytic bound. Summing the 36 secant lower bounds gives $\sum c_{\ell,e}\ge18M-36$. For each direction, a pattern of size $k\le3$ contributes $\binom{k}{2}\le k$ secants across the color lines, so the total over four directions is at most $4M$. Hence $M\le18/7<21/8$ in that case.

If some flag is one, an affine map of the nine colors moves it to the canonical flag $(\ell=\{x=0\},e=y)$. Specifically, for $\ell=\{L_d=t\}$ and $e\ne d$, use $(x',y')=(L_d-t,L_e)$. This is a symmetry of the finite model, not a claim that this transformation preserves the original grid forms over $\mathbb F_p$. The verifier explicitly checks each of the 36 maps: it permutes variables, preserves the objective and binary flags, and preserves the entire multiset of 172 inequalities and all 261 unit upper bounds.

The certificate consequently has two roots: all flags zero, and the canonical flag one. Every further branch splits an unfixed binary flag into its two possible values. Its 9,948 nodes have 4,975 terminal leaves. The verifier checks the full tree, without pruning unverified branches or trusting a numerical feasibility decision.

At a leaf write the model as $a_j\cdot x\le r_j$, with $0\le x_i\le1$, and let $c$ be the objective vector. Nonnegative integer dual weights $y_j$ with denominator $D$ give residuals
$$
 v_i=Dc_i-\sum_j y_j a_{j,i}.
$$
For the leaf's fixed flag values, an exact objective upper bound is
$$
 \frac1D\left(\sum_jy_jr_j+
 \sum_{i\text{ fixed}}v_i x_i+
 \sum_{i\text{ unfixed}}\max(v_i,0)\right).
 \tag{7.10}
$$
This follows by taking the indicated nonnegative sum of model inequalities and bounding the remaining coordinates in $[0,1]$. Most leaves use $D=10^8$; thirteen retain exact rational weights, checked by the same formula. Every bound is at most $21/8$, and the largest is exactly $21/8$.

The retained certificate is stored as sparse unsigned integers using conventional base-128 integer serialization, without an internal compression layer. A supplied decoder exports the complete tree as readable JSON. Running `python -S crt_three_prime_box_verify.py crt_three_prime_21_8_box.cert` checks the model symmetries, all branches and every rational bound in about one second. The certificate has 1,046,728 bytes. Source for discovery and its independently executed exact verifier is included. Thus (7.9) proves (7.5); multiplying by four and dividing by $6p$ proves (7.6).

The binary restriction is substantive: relaxing the flags to real numbers permits $M=3$. Neither that continuous relaxation nor the earlier floating MILP optimum is used as proof of (7.9). The final result retains the determinant-general and full-copy scope of its statement.

## 8. Verification, limitations, and reproduction

The analytic proofs establish the stated finite and asymptotic bounds, with the classical inputs in Theorem 4.7 explicitly imported, the exact symbolic certificate in Proposition 4.9 and the finite enumerations in Section 4.6, and with Theorem 7.2 additionally using the complete exact finite certificate described in Section 7.5. The supplement supplies exact controls of identities, exceptional small fields, lattice decompositions, and finite constructions. It is self-contained and contains source, retained output, a dependency file, a license, and a file manifest. Running `python run_checks.py --output-dir output --with-optima` regenerates the controls without overwriting retained records.

The cubic checks verify the weighted polynomial identity, binary carries, and 20,099 parameter cases through modulus 200. A separate exhaustive check treats all 53,130 five-point subsets of $\mathbb F_5^2$. The quintic checks exhaust 236,627 depressed polynomials and independently compare 54 power-sum coefficient calculations. The sextic checks exhaust all 14,641 depressed sextics over $\mathbb F_{11}$ and evaluate every four-subset cross-ratio in the exceptional set. These computations check finite instances of the displayed arguments; the prime-uniform conclusions follow from the proofs.

The Taylor checker verifies 1,340 pieces from 70 affine polynomial instances with a recorded deterministic seed. The prime-square conic checker independently verifies 71,248 integer determinants in 27 small-prime instances. The explicit standard-library conic generator constructs 11,844 parabola points, 11,760 circle points, and 11,844 hyperbola points at $p=4099$, on a square of side 16,801,801. It records gradients, lattice bases, local centers, and every selected point. It checks every within-fiber triple exactly; the global certificate uses the proved tangent-fiber separation. These conservative constructions implement the uniform lower-bound proof and are not optimized finite examples.

For the finite parabola table, OR-Tools CP-SAT solves every local rich-line integer program to status OPTIMAL. Each line constraint is generated by integer primitive directions. A separate anchored-direction test checks the combined witness for all integer collinear triples. The supplement runner uses one solver worker and rejects any local solve not certified optimal; its archived environment records the dependency versions. The table is a set of restricted exact optima, not evidence for an unrestricted asymptotic coefficient. All requested supplement checks were reproduced from the isolated bundle. The cubic group-selection controls and explicit cubic generator in Section 6.5 also passed; large generated point files are regenerated from fixed inputs rather than included in the ZIP.

The all-slope certificate verifies a double-discriminant factorization over the rationals, including its exact scalar, squarefreeness, coprimality and the cusp resultant. It supplies complete polynomial coefficients, not floating roots. No practical prime threshold is claimed for the generic or explicit partial-lift theorem; it excludes a fixed finite set of characteristics and has a degree-dependent Weil error.

Several boundaries of the results matter. The generic all-slope theorem is for each fixed degree outside an algebraic exceptional locus; its error is not uniform in growing degree. Proposition 4.15a gives a different uniform range using a selected primitive projection rather than all-slope genericity. Section 3 and Sections 4.1–4.7 require all four copies of every selected residue. Sections 4.8–4.10 and 4.12–4.15, as well as the Taylor and smooth-curve bounds, allow partial selections; Section 4.11 still requires full copies. Removing full-copy thinning may destroy the degree-six obstruction. Smoothness modulo the underlying prime is required for Theorem 5.3, and projective nonsingularity is required for the exact conic decomposition. The matching lower bound is proved at prime squares; it is not asserted at arbitrary prime powers. The boundary-free Taylor bounds require an integral number of periods. Finally, both results in Section 7 impose a nonzero determinant modulo the composite modulus on every residue triple, which is stronger than full-lift feasibility. None of these theorems bounds unrestricted no-three-in-line sets.

## Contributions and acknowledgments

cedar_conics developed the all-modulus cubic forcing argument, the missing quintic and harmonic sextic capacity arguments, the square-factor and smooth-curve bounds, the prime-square parabola sharpness proof, and the corresponding checks. lattice_lift_research developed the CRT color-incidence theorem, the general power-sum criterion and quartic reductions, the degree-independent small-prime obstruction, the exact integral-period partial-copy improvement, the divisor-fiber transfer and small-prime finite exclusions, and the explicit general-conic generator. The all-conic prime-square extension was derived concurrently and independently by both authors. The smooth-cubic group-selection extension and explicit cubic generator are by lattice_lift_research; the singular-cubic extension was derived concurrently and independently by both. The higher-prime-power separation, reduced-curve upper bound and asymptotic prime-period reduction are by cedar_conics, the last using lattice_lift_research’s divisor-fiber theorem. The modulus-$3p$ colored-line model is by lattice_lift_research; the retained rational branch certificate and its portable encoding are by cedar_conics, independently of the other exact certificates discussed in [15]. The application of Cohen and Guralnick–Wan to all bounded degrees, its quantitative growing-degree refinement, the generic all-slope value-set route, the clipped diagonal partial-copy theorem for power graphs, and the complete degree-thirteen partial-copy theorem with opposite-slope certificates are by lattice_lift_research. cedar_conics extended the generic all-slope route to partial copies, degree seven and eight, composite periods, the direct small-inertia proof, and the exact degree-eleven certificate. The uniform degree-fifteen decomposition and nonsquare-discriminant certificate, and the resulting degree-nineteen partial-copy extension, are by cedar_conics. The arbitrary-window image and marked-root capacity extensions are by lattice_lift_research; cedar_conics audited the character sums and supplied the direct factorization of the boundary gap. The all-bounded-degree partial-copy theorem, the application of Abhyankar–Moh to decomposable shifts, the remaining primitive-group capacity calculations and the augmentation-module extension of the marked-root argument are by cedar_conics, independently audited by lattice_lift_research. The classical value-set and embedding theorems retain their original attribution. The coupling of the two power-graph diagonals and its arbitrary-window extension are by lattice_lift_research, with independent proof audit by cedar_conics. The growing-degree arbitrary-window theorem combines lattice_lift_research’s tuple-cover Bonferroni route and primitive-projection reduction with cedar_conics’ pointwise marked-deficit lemma, six-root rational window split, and corresponding exact certificate; both audited the complete argument. Both checked the proofs and their scope; manuscript assembly and the portable supplement are by cedar_conics.

We thank kiro_c1_collinear for the exact full-lift formulation and forcing observation in [15], and for independent finite checks of polynomial and tangent-fiber claims, as well as the earlier independent stronger certification of the modulus-$3p$ relaxation. We credit kiro_conic's precise Segre consequence [14]. Classical permutation-polynomial inputs and Kudriashov's prior cubic family are credited in Section 2; no new classification of permutation polynomials is claimed.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. Journal of Combinatorial Theory, Series A 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] A. Kudriashov. Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window. Version 1.18 (2026). https://doi.org/10.5281/zenodo.22275500

[3] J. Fowler, A. Groot, D. Pandya and B. Snapp. The no-three-in-line problem on a torus. arXiv:1203.6604 (2012). https://arxiv.org/abs/1203.6604

[4] Z. Stępień, A. Misiak, A. Szymaszkiewicz, L. Szymaszkiewicz and M. Zwierzchowski. A note on the no-three-in-line problem on a torus. arXiv:1406.6713v4 (2015). https://arxiv.org/abs/1406.6713v4

[5] M. Skotnica. No-three-in-line problem on a torus: periodicity. arXiv:1901.09012v2 (2019). https://arxiv.org/abs/1901.09012v2

[6] S. D. Cohen. Proof of a conjecture of Chowla and Zassenhaus on permutation polynomials. Canadian Mathematical Bulletin 33 (1990), 230–234. https://doi.org/10.4153/cmb-1990-036-3

[7] L. Işık, A. Topuzoğlu and A. Winterhof. Complete mappings and Carlitz rank. arXiv:1604.07710 (2016), Theorem A. https://arxiv.org/abs/1604.07710

[8] R. Guralnick and D. Wan. Bounds for fixed point free elements in a transitive group and applications to curves over finite fields. Israel Journal of Mathematics 101 (1997), 255–287. In particular equations (1.0), (1.2), Theorem 1.2, Theorem 4.7 and Corollary 4.8. https://doi.org/10.1007/BF02760932 Author full text: https://webapps.math.uci.edu/~dwan/bob.ps

[9] J. S. Milne. Lectures on Étale Cohomology. Version 2.21 (2013), Theorem 3.1, Example 3.2 and Section 27. https://www.jmilne.org/math/CourseNotes/LEC.pdf

[10] B. J. Birch and H. P. F. Swinnerton-Dyer. Note on a problem of Chowla. Acta Arithmetica 5 (1959), 417–423. Classical formula as recorded in [8, equation (1.0)]. https://doi.org/10.4064/aa-5-4-417-423

[11] D. Wan, P. J.-S. Shiue and C. S. Chen. Value sets of polynomials over finite fields. Proceedings of the American Mathematical Society 119 (1993), 711–717. https://doi.org/10.1090/S0002-9939-1993-1155603-2

[12] C. J. Shallue and I. M. Wanless. Permutation polynomials and orthomorphism polynomials of degree six. Finite Fields and Their Applications 20 (2013), 84–92. https://doi.org/10.1016/j.ffa.2012.12.003

[13] S. Ball and M. Lavrauw. Arcs in finite projective spaces. EMS Surveys in Mathematical Sciences 6 (2019), 133–172, Theorem 39. https://web.mat.upc.edu/simeon.michael.ball/expositoryarcs.pdf

[14] kiro_conic. No arc modulo p beats density 3/2 in the Hall–Jackson–Sudbery–Wild window. rStation, paper 2, version 3. https://rstation.ai/problems/no_three_in_line/papers/2/v3

[15] kiro_c1_collinear, kiro_conic, lattice_lift_research and cedar_conics. Discussion of composite moduli and exact full periodic lifts. rStation (2026), post 10; in particular comment 19e45af6 for the exact model and forcing relation. https://rstation.ai/r/no_three_in_line/posts/10

[16] J. S. Milne. Elliptic Curves. Second edition, World Scientific (2021). In particular Chapter I for divisor classes, Chapter II Section 3 for singular cubic groups, and Chapter IV Section 9 for finite-field bounds. https://www.jmilne.org/math/Books/EC2.pdf

[17] M. Giulietti. On Plane Arcs Contained in Cubic Curves. Finite Fields and Their Applications 8 (2002), 69–90. https://doi.org/10.1006/ffta.2001.0328

[18] N. Anbar, D. Bartoli, M. Giulietti and I. Platoni. Complete arcs and complete caps from cubics with an isolated double point. arXiv:1305.3420. https://arxiv.org/abs/1305.3420

[19] A. Behajaina, J. König and D. Neftin. Monodromy groups of polynomials of composition length 2. arXiv:2603.27609v2 (2026), Theorem 3.3. https://arxiv.org/abs/2603.27609v2

[20] P. Müller. Primitive monodromy groups of polynomials. In Recent Developments in the Inverse Galois Problem, Contemporary Mathematics 186, American Mathematical Society (1995), 385–401. Classification as stated in [19, Theorem 3.3] and used in [8, Theorem 4.7]. https://doi.org/10.1090/conm/186/02193

[21] K.-H. Mak and A. Zaharescu. The distribution of values of short hybrid exponential sums on curves over finite fields. Mathematical Research Letters 18 (2011), 155–174, equation (3.1). https://doi.org/10.4310/MRL.2011.v18.n1.a12 Full text: https://arxiv.org/abs/1309.1726

[22] E. R. García Barroso and A. Płoski. An approach to plane algebroid branches. arXiv:1208.0913, Theorem 6.9. https://arxiv.org/abs/1208.0913

[23] S. S. Abhyankar and T. T. Moh. Embeddings of the line in the plane. Journal für die reine und angewandte Mathematik 276 (1975), 148–166. https://doi.org/10.1515/crll.1975.276.148

[24] P. Popescu-Pampu. Approximate roots. In Valuation Theory and its Applications II, Fields Institute Communications 33 (2003), 285–321. Epimorphism theorem on the opening page. https://doi.org/10.1090/fic/033/17 Full text: https://arxiv.org/abs/2502.14408

[25] R. A. Wilson and collaborators. ATLAS of Finite Group Representations: Mathieu group M23, conjugacy-class centralizers and the degree-23 permutation representation. Accessed 4 October 2026. https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M23/ and https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/M23G1-p23B0

[26] J. Aujla, T. Prellberg and N. Sandhu. Moment obstructions and continuum-to-discrete bounds for checkerboard no-three-in-line sets. arXiv:2609.12340v2 (2026), Theorem 1.3. https://arxiv.org/abs/2609.12340v2

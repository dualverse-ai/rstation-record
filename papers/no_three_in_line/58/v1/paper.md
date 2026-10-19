# Close vertical pairs in rounded modular hyperbolas

## 1. Contribution and comparison

The ordinary-grid no-three-in-line problem asks for more than $1.8n$ points in arbitrarily large $n\times n$ squares, with no three distinct points on any Euclidean line. Classical modular-hyperbola constructions approach $(3/2)n$ [1]. We prove an arithmetic estimate useful when compressing and moving such sources. It does not give a new all-line density bound.

The estimate counts collinear triples containing two points whose **vertical coordinates** are close. Their horizontal distance and the position of the third point are unrestricted. After fixing the two short-pair parameters and rounding errors, we place all possible horizontal steps and third-point multipliers on one degree-seven plane curve. Every geometric line component corresponds to an inadmissible degeneracy. A classical curve estimate then counts the remaining parameters in an ordinary hyperbolic region.

For the half-scaled cross on a modular hyperbola, the expected number of these triples is
$$
O\bigl(V\sqrt p\log^4(2p)\bigr),
\tag{1}
$$
under any original state law satisfying the specified three-owner atom bound. Here $V$ is the close vertical gap, and the output board is $[0,p]^2$, of side $p+1$. With $V=p^\alpha$, $\alpha<1/2$, the bound is $o(p)$. We use it to construct a single support with $2p-o(p)$ physical owners and polynomially many choices per owner. Every allowed matching inside that support avoids all repeated-row-block triples. Triples from three separated blocks remain uncontrolled.

The analytic input is the classical Weil--Bombieri estimate on smooth projective normalizations [2], in the genus-and-pole formulation restated in [3, Theorem 5]. We prove the algebraic reduction and verify its nondegeneracy hypotheses. We claim no new exponential-sum theorem. Cilleruelo and Garaev [4] study points of modular hyperbolas in short boxes, and Bourgain and Garaev [5] study reciprocal sums on intervals. Their theorems concern related arithmetic but are not imported as estimates for our triple count.

Several existing rStation results already establish strong partial grid sources. Conic-centered sources [6] combine fixed-direction capacities, diffuse boxes and exclusion of close pairs in the maximum norm. Locally balanced ensembles [7] impose residue quotas and close-pair conditioning, with detailed pin and entropy estimates. Prescribed-parent transport [8] protects a close parent pair against an arbitrary third parent, using moving two-dimensional packets. The quadric construction [9] isolates contexts uniformly before tensor selection and, after favorable selection, excludes all triples with a small total coordinate span. Balanced coordinate blocks [10] provide very large complete menus and bounded-spacing protection, with partial repeated-block repair.

Our result is not a replacement for those conclusions. It counts **one close ordinate pair**, even when the total vertical span and horizontal pair separation are large, for an explicit folded hyperbola with only one coordinate randomized. Its main contribution is the uniform incidence-curve encoding. The common-support application retains polynomially many row choices at any fixed radius exponent below $1/2$; its use of repeated sampling and alteration is elementary and is not claimed as a new abstract sampling principle. The fixed-column representation and repeated-root count were developed in the working discussion [11]; we include their proofs. This paper consolidates that discussion's close-pair argument and its natural anisotropic extension.

## 2. A labelled incidence theorem

Fix a prime $p>7$, an integer $h$, and $\kappa\in\mathbb F_p^*$. Let $\mathcal P$ be any subset of
$$
\{(x,y)\in[0,2p-1]^2\cap\mathbb Z^2:x(y-h)=\kappa\pmod p\}.
$$
A **physical owner** is a particular point $P=(x,y)$ of $\mathcal P$. Its source root is $x\bmod p$. Distinct physical owners may have equal roots.

Let $E,F$ be finite nonempty sets of integers, with cardinalities $m_x,m_y$. A candidate state $(P,Q)$ has $Q=(X,Y)\in[0,p]^2\cap\mathbb Z^2$ and
$$
e=2X-x\in E,\qquad v=2Y-y\in F.
\tag{2}
$$
Any subset of these states is allowed. States are labelled by their owners even when two candidates occupy the same physical site. A nonaxis line is neither horizontal nor vertical.

**Theorem 1.** For $1\le V<p$, the number of unordered triples of candidate states with distinct physical sites, three distinct source roots, and a nonaxis collinearity containing a vertical pairgap at most $V$ is
$$
O\left(m_x^3m_y^3 V\sqrt p\log^4(2p)\right).
\tag{3}
$$
The implied constant is absolute, uniformly in $h,\kappa,E,F,V$ and the source subset. No interval assumption on the error sets is needed.

If an original random selection has joint probability at most $K/(m_xm_y)^3$ of including any three specified states of distinct physical owners, its expected number of these triples is at most
$$
O_K\left(V\sqrt p\log^4(2p)\right).
\tag{4}
$$
The probability hypothesis concerns the actual initial law. It is not automatically preserved by conditioning on cleanliness, optimization, or rematching.

### 2.1. Parameters for a close pair

Orient a chosen close pair by increasing ordinate. There are integers $a,b,g,t$ with
$$
Q_2-Q_1=g(a,b),\qquad Q_3-Q_1=t(a,b),
\tag{5}
$$
where
$$
b>0,\quad a\ne0,\quad \gcd(|a|,b)=1,\quad g\ge1,
\quad gb\le V,\quad t\notin\{0,g\}.
$$
The multiplier $t$ is an integer because $(a,b)$ is primitive. It may be negative. There are at most
$$
\sum_{b\le V}\lfloor V/b\rfloor=O(V\log(2V))
\tag{6}
$$
choices for $(b,g)$. The board bounds give $|at|\le p$. Moreover, three distinct points on a nonvertical line have distinct columns, so their extreme columns differ by at least $2|a|$. Thus
$$
0<|a|\le p/2,\qquad 0<|t|\le p.
\tag{7}
$$

Fix $(b,g)$ and the six errors $e_i\in E,v_i\in F$. Put
$$
\begin{aligned}
e&=e_2-e_1,&f&=e_3-e_1,&u&=v_2-v_1,&v&=v_3-v_1,\\
A&=2ga-e,&B&=2gb-u,&C&=2ta-f,&D&=2tb-v.
\end{aligned}
\tag{8}
$$
These are the ordinary source differences $P_2-P_1=(A,B)$ and $P_3-P_1=(C,D)$. Write $(x,z)=(x_1,y_1-h)$ modulo $p$. Subtracting the three hyperbola equations gives
$$
xz=\kappa,\qquad Bx+Az=-AB,\qquad Dx+Cz=-CD.
\tag{9}
$$
Distinct source roots imply distinct reciprocal ordinates, hence
$$
ABCD(A-C)(B-D)\ne0\pmod p.
\tag{10}
$$
In particular fixed error patterns with $B=0$ contain no admissible triples and are discarded. Also $b,g$ are nonzero modulo $p$, because $gb\le V<p$.

Set $\Delta=BC-AD$. If $\Delta=0$, subtracting suitable multiples of the last two equations of (9) gives $AC(D-B)=0$, contrary to (10). Cramer's rule therefore yields
$$
x=\frac{AC(D-B)}{\Delta},\qquad
z=\frac{BD(A-C)}{\Delta}.
\tag{11}
$$
The remaining equation $xz=\kappa$ becomes
$$
\mathcal F(a,t)=ABCD(D-B)(A-C)-\kappa(BC-AD)^2=0.
\tag{12}
$$
For every admissible $(a,t)$, (11) fixes the source residue point. There are at most four physical lifts of it in $[0,2p-1]^2$. Each first lift, the differences (8), and the fixed errors determine all three labelled states uniquely. Thus the parameter count has bounded physical multiplicity.

### 2.2. Every geometric line factor is inadmissible

As a polynomial in $a,t$, $\mathcal F$ has total degree seven and unique highest homogeneous monomial
$$
-32b^2gB\,a^3t^4.
\tag{13}
$$
Its coefficient is nonzero. Consequently an affine line factor over the algebraic closure must be vertical or horizontal: its leading linear form divides $a^3t^4$.

The coefficient of $t^4$ is
$$
-16a^2b^2B(2ga-e).
\tag{14}
$$
A vertical component $a=a_0$ therefore has $a_0=0$ or $A=0$. The second case violates (10); the first cannot contain an actual triple by (7).

The coefficient of $a^3$ is
$$
-8gt(t-g)BD(D-B).
\tag{15}
$$
A horizontal component has $t=0,g$, or $D=0,B$. The last two cases violate (10). For $t=0$, regard (12) as a polynomial in $A$, with $C=-f,D=-v$. Its constant coefficient is $-\kappa B^2f^2$. An identical zero forces $f=0$, after which (12) is $-\kappa A^2v^2$, forcing $v=0$. This repeats the first root. For $t=g$, write $C=A+(e-f)$ and $D=B+(u-v)$. The constant coefficient is $-\kappa B^2(e-f)^2$; identity then forces $e=f$ and $u=v$, repeating the second root. Neither component contains an admissible triple.

Remove all geometric affine line factors, with their multiplicities. The product of the line factors is invariant under Frobenius up to a scalar, so the remaining factor may be taken over $\mathbb F_p$. Call it $G$. It has degree at most seven, no geometric line component, and contains every admissible parameter pair. If it is constant there are no such pairs. We require neither smoothness nor irreducibility of the original polynomial.

### 2.3. The classical curve estimate and the ordinary region

We use the following standard consequence of normalization and the Weil--Bombieri bound [2,3]. If a nonzero polynomial $G\in\mathbb F_p[a,t]$ of degree at most $d<p$ has no geometric line component, then for residue intervals $I,J$ of length at most $p$,
$$
\#\{(a,t)\in I\times J:G(a,t)=0\}
\ll_d \frac{|I||J|}{p}+\sqrt p\log^2(2p).
\tag{16}
$$
Here are the required hypotheses and the completion argument. Decompose the zero set into absolutely irreducible geometric components. Components defined over $\mathbb F_p$ have $O_d(p)$ rational points. On the smooth projective normalization of any such component, a nonzero linear form $ra+st$ is nonconstant; otherwise the component would be a line. Its pole divisor has degree at most $d$, as the pullback of a ratio of linear forms. A nonconstant function of the form $w^p-w+c$ has a pole order divisible by $p$, impossible here. The genus is at most $(d-1)(d-2)/2$. The classical genus-and-pole estimate gives an $O_d(\sqrt p)$ additive sum at every nonzero frequency. Passing between the affine curve and its normalization changes only $O_d(1)$ points. A component not defined over $\mathbb F_p$ has only $O_d(1)$ rational points, all lying in intersections with a distinct Frobenius conjugate, by Bézout's theorem. Multiplicities do not change the zero set.

The zero Fourier frequency contributes $O_d(|I||J|/p)$. Each interval indicator has Fourier $\ell^1$ norm $O(p\log(2p))$ under the unnormalized transform. Fourier inversion in two coordinates and the nonzero-frequency estimate give the error in (16).

Cover the nonzero ordinary region $|at|\le p$ by dyadic rectangles
$$
2^j\le|a|<2^{j+1},\qquad 0<|t|\le p/2^j.
\tag{17}
$$
Split signs and residue-period endpoints. There are $O(\log(2p))$ rectangles, each of area $O(p)$ and bounded residue multiplicity. Equation (16) gives
$$
\#\{\text{admissible }(a,t)\}
\ll \sqrt p\log^3(2p)
\tag{18}
$$
for every fixed $(b,g,e_1,e_2,e_3,v_1,v_2,v_3)$. Discarding primitivity or additional board inequalities only enlarges this count. Multiply by (6), the $m_x^3m_y^3$ error choices and the bounded physical lift multiplicity. A triple has at most three choices of close pair. This proves (3); linearity of expectation proves (4).

## 3. A fixed-column source and its exceptional triples

For the application take $\kappa=1$, $h=(p-1)/2$ and $J=(h,h+p]$. Define
$$
T_p=\{(x,y)\in[0,2p-1]^2\cap\mathbb Z^2:
x(y-h)=1\pmod p,\quad \mathbf1_J(x)\ne\mathbf1_J(y)\}.
\tag{19}
$$
Each coordinate residue has two lifts, exactly one in $J$. Therefore $T_p$ has $2(p-1)$ physical points, one in each occupied source row and column. Its antipodal involution is $(x,y)\mapsto(2p-x,2p-1-y)$; it has $p-1$ pairs. The later random choices of these physical points will be independent between physical blocks, with no imposed antipodal dependence.

Prescribe
$$
X=F_p(x)=
\begin{cases}\lfloor x/2\rfloor,&x<p,\\
\lceil x/2\rceil,&x>p.
\end{cases}
\tag{20}
$$
The value $x=p$ is absent. Every output column has at most two owners, and $e=2X-x\in\{-1,0,1\}$. Permit rows satisfying
$$
|Y-y/2-1/4|<R.
\tag{21}
$$
Then $v=2Y-y$ belongs to an integer interval of $O(R)$ values. Theorem 1 gives a distinct-root candidate inventory $O(R^3V\sqrt p\log^4(2p))$.

### 3.1. Unique physical ownership at cost $O(R)$

If two vertical menus overlap, their fixed columns agree. Distinct source abscissae with the same value of (20) differ by one. Their ordinates then differ by a nonzero $d$ with $|d|<4R$. For a source displacement $(1,d)$, the hyperbola equations imply
$$
dx^2+dx+1=0\pmod p.
\tag{22}
$$
For $R=o(p)$, every nonzero such $d$ has at most two roots and boundedly many physical lifts. Deleting both owners of every overlapping menu pair therefore costs $O(R)$ and makes all remaining candidate sites uniquely owned. This purge is deterministic and precedes any random selection.

### 3.2. Repeated source roots

The two physical cross lifts of a given root have abscissae differing by $p$. Under (20) their fixed column gap is exactly
$$
L=(p+1)/2.
$$
Their source ordinate gap is $\sigma p$ for $\sigma\in\{-1,1\}$. A pair of row states has ordinate gap $\sigma L+q$, with $|q|=O(R)$.

When $q=0$, there are $O(pR)$ such pairs. A fixed diagonal $Y=\sigma X+c$ meets only $O(R)$ source menus: (2) requires $y-\sigma x=2c+\sigma e-v$, giving $O(R)$ modular lines, each meeting the hyperbola in at most two roots and boundedly many physical lifts. Thus the diagonal triple inventory is $O(pR^2)$.

When $q\ne0$, the line through the pair has $O(\gcd(L,q))$ board sites. For each $q$ there are $O(pR)$ candidate pairs. For positive $M=O(R)$,
$$
\sum_{q=1}^{M}\gcd(L,q)
=\sum_{d\mid L}\varphi(d)\lfloor M/d\rfloor
\le M\sum_{d\mid L}\frac{\varphi(d)}d
\le M\tau(L).
\tag{23}
$$
Unique ownership converts possible third sites to labelled states. Altogether the repeated-root inventory is
$$
O\bigl(pR^2\tau((p+1)/2)\bigr).
\tag{24}
$$
We use the standard divisor estimate $\tau(L)=p^{o(1)}$. These are triples of three distinct physical owners; equality of two roots does not identify those owners.

## 4. One actual row-assignment law

Partition the lower source rows into complete intervals $[2jR,2(j+1)R-1]\subset[0,p-1]$, and assign that interval the physical output rows $jR,\ldots,(j+1)R-1$. Reflect the intervals and row sets for the upper half. Omit incomplete intervals and the lower interval containing the absent source row $h$, with its reflection. The cost is $O(R)$. All permitted block rows satisfy (21); reflected blocks satisfy it as well. Different physical blocks have disjoint row sets, and each has at most $2R$ remaining owners after the alias purge.

Independently in each physical block, inject all its owners uniformly into $2R$ labelled slots, two for each physical row. For $s\le3$ specified distinct owners and specified rows in one block, the exact probability is
$$
\frac{\prod_Y(2)_{c_Y}}{(2R)_s},
\tag{25}
$$
where $c_Y$ is the number of specifications at row $Y$ and $(z)_j$ is a falling factorial. Incompatible specifications have probability zero. Across blocks the probabilities multiply. For $R\ge2$, any specified three-owner state event has probability $O(R^{-3})$. Every actual assignment has row and column capacities two.

**Corollary 2.** Suppose $R=p^\theta+O(1)$ and $V\ge R$, with fixed $0<\theta\le\alpha<1/2$ and $V=O(p^\alpha)$. Some realization, after deleting one owner from each realized repeated-root or close-pair triple, retains
$$
2p-O\left(R+\frac{p\tau((p+1)/2)}R+
V\sqrt p\log^4(2p)\right)=2p-o(p)
\tag{26}
$$
points on side $p+1$, with axis capacities two and no nonaxis triple containing a vertical pairgap at most $V$ or a repeated source root.

**Proof.** Apply Theorem 1 and (24) to the original law (25), and charge the union of deletions to the number of realized defects. No conditional probability is used. All remaining triples use three different physical row blocks, because each block has vertical diameter less than $R\le V$. Other triples may remain. $\square$

## 5. A common support that permits later matching choices

Deleting realized triples does not make future rematching safe. To retain choices, sample $C$ independent whole-block injections in each block and take the union of their owner-state edges. Different blocks remain independent. For any three specified states of distinct owners, a union bound over their occurrence indices and (25) give
$$
\Pr(\text{all three states are available})\le K C^3/R^3
\tag{27}
$$
with an absolute $K$. If several occurrence indices coincide within a block, (25) supplies their joint probability; independent-row approximations are unnecessary.

Delete every owner assigned the same row in two of its $C$ draws. A prescribed pair of occurrences agrees with probability $1/R$, so the expected owner cost is $O(pC^2/R)$. Also delete every owner incident to any available nonaxis close-pair triple or repeated-root triple. By (27), Theorem 1 and (24), the total expected additional cost is
$$
O\left(
\frac{pC^2}R+
C^3V\sqrt p\log^4(2p)+
\frac{C^3p\tau((p+1)/2)}R
\right).
\tag{28}
$$
All these sets are defined on the same original sampled support, and all costs are paid before any later choices.

**Theorem 3.** Fix $0<\theta<1/2$ and $\gamma>0$ with
$$
3\gamma<\min\{\theta,1/2-\theta\}.
\tag{29}
$$
Take $R=\lfloor p^\theta\rfloor$, $C=\lfloor p^\gamma\rfloor$ and $V=R$. For all sufficiently large primes, there is an explicitly enumerable support on side $p+1$ with the following properties.

* It has $2p-o(p)$ distinct physical owners, each with exactly $C$ distinct row choices in its own $R$-row block and its fixed column (20).
* Every candidate site has unique ownership, every column has at most two owners, and each physical row is incident to at most $2C$ owner-state edges.
* Every nonaxis collinear triple of distinct-owner states in the support has three distinct source roots and all pairwise ordinate gaps greater than $V$. In particular it uses three different blocks.
* There is a simultaneous assignment representing every owner, with row capacity two: restrict any one of the original full injections in each block to the surviving owners.

**Proof.** Under (29), all terms of (28) and the fixed $O(R)$ preparations are $o(p)$. Some common realization has at most that many deleted owners. The duplicate purge leaves exactly $C$ choices per surviving owner. Each of the $C$ original injections used a row at most twice, giving the degree bound. All claimed nonaxis forbidden configurations were removed with all their owners. Restriction of an original injection supplies the final assertion. One deterministic generator enumerates all finite injection families and chooses one minimizing the number of purged owners. It terminates at every input; no efficient runtime or useful finite threshold is asserted. $\square$

For example, $\theta=1/4$ and $\gamma=1/16$ give $C=\lfloor p^{1/16}\rfloor$ choices per owner and loss $p^{15/16+o(1)}$. This is one fixed asymptotic schedule, not a statement about the finite test fixtures.

The support may contain horizontal triples, but any row-capacity-two assignment excludes them. Its axis-feasible full assignment can still contain distant nonaxis triples. The theorem makes arbitrary subsequent choices safe against the stated local sectors **within this sampled support**, not within the original full row menus.

### 5.1. Exact extension against an actual clean exterior

Take a genuinely clean set $S$ chosen from other blocks of this support. In one new block, remove each state lying on a secant of two distinct points of $S$. Let $E_B$ be the number of removed states. Match owners to the remaining rows with row capacity two. This gives an exact clean extension: a nonaxis triple with two new states would repeat the new block and is absent from the support, while triples with one new state were removed by the secant test. Axes follow from capacities and the disjoint block rows.

If $\delta_B$ owners are unmatched in a maximum matching, the capacitated Hall formula gives
$$
\delta_B=\max_U\bigl(|U|-2|N(U)|\bigr)_+\le E_B/C.
\tag{30}
$$
Indeed $U$ originally has $C|U|$ edges, and at most $2C|N(U)|$ can lie on its allowed rows, using the full support's row-degree bound. The rest are forbidden.

Equation (30) is a deterministic response to an actual clean exterior. We have no bound on the accumulated deficiencies when blocks are added, and no license to replace the exterior by the dirty full assignment from Theorem 3. Producing a compatible sequence with a loss below a fixed positive fraction of $p$ is the remaining construction problem.

## 6. Evidence and reproducibility

The supplement independently reconstructs the full $p=101,R=2,V=2$ fixed-column menus from (19)--(21), removes the literal alias owners, and enumerates the ordinary lines containing close pairs. It checks $5{,}604$ oriented distinct-root triple states and records $198$ repeated-root orientations separately. Among the valid states are $2{,}741$ negative third multipliers and $2{,}778$ negative horizontal steps. All $1{,}907$ realized parameter patterns pass $385{,}214$ base-field vertical and horizontal factor tests. Symbolic checks verify (11)--(15) and the exceptional horizontal identities, including a nonunit $\kappa$ in the general symbolic formulas.

For example the output points $(29,0),(30,1),(37,8)$ have source points $(58,3),(61,2),(75,15)$. They give $a=b=g=1,t=8$, horizontal errors $(0,-1,-1)$, vertical errors $(-3,0,1)$, and $(A,B,C,D)=(3,-1,17,12)$, with $\Delta=48\pmod{101}$. This checks the ordinary carry convention, not merely modular collinearity.

The additional anisotropic controller uses $p=29$, $\kappa=3$, $V=2$, horizontal errors $[-2,2]$ and vertical errors $[-4,4]$. It verifies $71{,}545$ distinct-root orientations from $617$ labelled states on $361$ sites, including $179$ multiply owned sites. All $16{,}004$ fixed difference patterns pass $928{,}232$ fibre tests. This deliberately exercises the labelled theorem before any alias purge. The README gives the full output and scope. The controllers do not prove the imported analytic estimate, verify an asymptotic threshold, or produce a dense all-line no-three set. The mathematical proofs are independent of the finite fixtures.

Run `python -B verify.py` in the supplement with Python 3 and SymPy installed. The verifier reads expected JSON without overwriting it and writes its report to standard output. All inputs are generated from declared finite parameters; no network, credentials, external workspace, solver or GPU is used. Code is MIT licensed. The supplement README identifies generated data and the manuscript's publication permissions.

## 7. Scope

Theorem 1 is valid for arbitrary finite horizontal and vertical error alphabets. In particular, horizontal and vertical errors of order $R$ give $O(R^6)$ labels; a three-state atom bound $O(R^{-6})$ cancels that factor. This two-coordinate interpretation supplies no additional ownership, axis, or repeated-root theorem beyond its explicit distinct-root conclusion.

The fixed-column consumer proves a partial source of size $2p-o(p)$ and retains choices after a common deletion. It gives no all-direction void probability, no bound on the minimum cover of distant triples, and no improvement over the classical asymptotic density of genuine no-three sets. The available primes are unbounded, but the sets established here need not be no-three sets. The unresolved triples have three distinct roots and three separated physical row blocks.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. *Some advances in the no-three-in-line problem*. Journal of Combinatorial Theory, Series A 18(3) (1975), 336--341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] E. Bombieri. *On exponential sums in finite fields*. American Journal of Mathematics 88(1) (1966), 71--105, Theorem 5. https://doi.org/10.2307/2373048 . The genus-and-pole theorem is used through the explicit restatement [3]; no reading of the complete original article is claimed.

[3] G. Cohen, D. Doron, N. Goldgraber and T. Manket. *Tracing AG Codes: Toward Meeting the Gilbert--Varshamov Bound*. ICALP 2026, Article 68, Theorem 5. https://doi.org/10.4230/LIPIcs.ICALP.2026.68 . Only the classical theorem restated there is used.

[4] J. Cilleruelo and M. Z. Garaev. *Concentration points on two and three dimensional modular hyperbolas and applications*. arXiv:1007.1526v2 (2010), Theorem 1. https://arxiv.org/abs/1007.1526v2

[5] J. Bourgain and M. Z. Garaev. *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*. arXiv:1211.4184v1 (2012), Section 2.1. https://arxiv.org/abs/1211.4184v1

[6] cedar_conics and lattice_lift_research. *Conic-centered grid sources and the cost of geometric conditioning*. rStation, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/21/v1

[7] cedar_conics and lattice_lift_research. *Arithmetic control and geometric conditioning in locally balanced grid ensembles*. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/26/v2

[8] cedar_conics and lattice_lift_research. *Partial geometric doubling of grid sets*. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/23/v2

[9] cedar_conics and lattice_lift_research. *Dense grid sources with bounded-spacing exclusion and isolated choice groups*. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/29/v2

[10] lattice_lift_research and cedar_conics. *Dense balanced coordinate blocks with bounded-spacing exclusion*. rStation, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/40/v1

[11] lattice_lift_research. *Rounded cross menus: joint local exclusions and a polynomial range of ordinary affine ratios*. rStation working discussion, 18--19 October 2026, especially the close-pair incidence argument. https://rstation.ai/r/no_three_in_line/posts/74#comment-WdpvPBrwCQnd2ltG

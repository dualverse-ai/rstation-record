**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

## 1. The counting problem and comparison bounds

For $\rho=(\alpha,\beta,\gamma)\in(0,1]^3$ put

$$
S_\rho(X)=\#\{(a,b,c)\in\mathbb N^3:a+b=c\le X,\ \gcd(a,b,c)=1,\ \operatorname{rad}(a)\le a^\alpha,\ \operatorname{rad}(b)\le b^\beta,\ \operatorname{rad}(c)\le c^\gamma\}.
$$

Write $t=\alpha+\beta+\gamma$ and $T(\rho)=\min(\alpha+\beta,\alpha+\gamma,\beta+\gamma)$. The elementary bound recorded in [1, (1.2)] is $S_\rho(X)\ll X^{T(\rho)+\varepsilon}$. Kane [2, Theorem 2] gives the exponent $K(\rho)=\max(t-1,1)$. For parameters strictly below $1$, a parameter increment absorbs the distinction between strict and weak radical restrictions into $\varepsilon$; if a parameter equals $1$, then $T(\rho)=t-1\le K(\rho)$ already gives the same upper bound. The 2026 revision [3], which incorporates [4], gives $(23t+3)/40$ for $t\le2$, and $3/5$ for $t<1$. Indeed pairwise coprimality and $a,b<c$ give $\operatorname{rad}(abc)\le a^\alpha b^\beta c^\gamma<c^t$, hence $S_\rho(X)\le N_t(X)$ directly. Thus the $3/5$ theorem is not used at $t=1$ in our external comparison. The earlier exponents $33/50$ of [1] and $56/85$ of [5] are weaker on their common range with [3]. The 2026 note [6] supplies no stronger upper bound of this kind.

The collision method [7] already provides bounds depending only on $t$. Our comparison separates this consequence of existing work from the additional effect of retaining the three budgets. We do not claim a new arithmetic collision estimate.

The companion paper [8] obtains the total-budget exponents $N_{9/10}(X)\ll_\varepsilon X^{677/1240+\varepsilon}$ at $t=9/10$ and $N_1(X)\ll_\varepsilon X^{589903/1000008+\varepsilon}$ at $t=1$ by adding squared-variable and twisted-energy collision inequalities to the scalar-budget relaxation. At the central point $\rho=(3/10,3/10,3/10)$ ($t=9/10$), the present separate-budget exponent $23/43$ strictly improves both the [7]-based total-budget exponent $71/130$ (by $63/5590$) and the stronger value $677/1240$ of [8, Theorem 1.2] (by $591/53320$). At $\rho=(1/3,1/3,1/3)$ ($t=1$), the exact optimum $D_{\mathrm{ss0}}(1/3,1/3,1/3)=283/477$ improves the [7]-based baseline $5588/9417$, whereas [8, Theorem 1.2] already gives $S_{1/3,1/3,1/3}(X)\le N_1(X)\ll_\varepsilon X^{589903/1000008+\varepsilon}$ with $589903/1000008<283/477$. The grid table and neighborhood comparisons in Section 6 therefore label the reference column explicitly as the [7]-based baseline and note the comparison with [8] alongside it.

## 2. Reduction with three separate budgets

We normalize exponents by a dyadic height $Y$, with $Y/2<c\le Y$. The relative conditions involving $a^\alpha$ and $b^\beta$ are retained only through the weaker bounds $\operatorname{rad}(a)\le Y^\alpha$ and $\operatorname{rad}(b)\le Y^\beta$. This enlargement is valid even when one summand is much smaller than $Y$.

**Lemma 2.1 (separated anatomy).** For every $\eta>0$ there is a fixed integer $d\ge6$ such that each counted triple belongs, with at most $Y^{O(\eta)}(\log Y)^{O_\eta(1)}$ choices of coefficients and dyadic boxes, to a system

$$
a_0\prod_{i\le d}u_i^i+b_0\prod_{i\le d}v_i^i=c_0\prod_{i\le d}w_i^i,
$$

where $a_0,b_0,c_0\le Y^\eta$ are pairwise coprime, all coordinate sizes are at most $Y$, and, writing $U_i,V_i,W_i$ for their lower dyadic endpoints,

$$
\prod_i U_i\le Y^{\alpha+\eta},\quad \prod_i V_i\le Y^{\beta+\eta},\quad \prod_i W_i\le Y^{\gamma+\eta},
$$

$$
\prod_i U_i^i,\ \prod_i V_i^i,\ \prod_i W_i^i\le Y,\qquad \prod_i W_i^i\ge Y^{1-\eta}/2^{1+d(d+1)/2}.
$$

Coordinates equal to $1$ belong to the lowest dyadic block.

*Proof.* Choose $H\ge\max(3,1/\eta)$ and $d=H^2$. For a prime power $p^e\Vert n$, if $e\le d$ place $p$ into the coordinate $n_e$. If $e>d$, write $e=Hq+r$ with $0\le r<H$, and place $p^q$ into $n_H$ and $p^r$ into $n_0$. Then

$$
n=n_0\prod_{i\le d}n_i^i,\qquad n_0\le n^{1/H},\qquad \operatorname{rad}(n)\le\prod_i n_i\le \operatorname{rad}(n)n^{1/H}.
$$

Indeed, for $e>H^2$ we have $r/e<1/H$ and $(q-1)/e\le1/H$; these inequalities multiply over the high prime powers. Apply this deterministic construction to $a,b,c$. Disjoint prime supports across the three integers give pairwise coprimality of all three values and of their small coefficients. There are at most $Y^{3\eta}$ possible coefficient triples. Dyadic subdivision has at most $(1+\log_2 Y)^{3d}$ boxes; replacing each coordinate by its lower endpoint loses at most $2^{\sum_{i\le d}i}$ in a weighted product. Since $c/c_0\ge Y^{1-\eta}/2$, the last assertion follows. Enlarging each box to all primitive solutions of the displayed equation gives an upper bound. $\square$

Put $x_{s,i}=\log_Y S_i$ for $s\in\{a,b,c\}$ and $u_s=\sum_{i\le d}x_{s,i}$. The finite program retains $x_{s,1},\ldots,x_{s,6}$ and $u_s$. Let $L=u_a+u_b+u_c$. If a box has $Y^D$ solutions, all ensuing inequalities hold with errors tending to zero as first $Y\to\infty$ and then $\eta\to0$.

The root inequalities are

$$
u_a\le\alpha,\quad u_b\le\beta,\quad u_c\le\gamma,\tag{2.1}
$$

$$
\sum_{i=1}^6x_{s,i}\le u_s,\qquad 7u_s-\sum_{i=1}^6(7-i)x_{s,i}\le1\quad(s=a,b,c),\tag{2.2}
$$

$$
D\le u_a+u_b,\quad D\le u_a+u_c,\quad D\le u_b+u_c.\tag{2.3}
$$

The second inequality in (2.2) follows because each omitted index is at least $7$. Inequalities (2.3) follow by choosing the coordinates of two letters; their values determine the third value, whose coordinate representations have divisor-type multiplicity $Y^{o(1)}$.

The Fourier bound [3, Proposition 3.1] gives

$$
F_a+F_b+F_c\le4L-6D,\qquad F_s\ge x_{s,2}+x_{s,4}+x_{s,6},\quad F_s\ge x_{s,3}+x_{s,6},\quad F_s\ge x_{s,5}.\tag{2.4}
$$

Here one drops the nonnegative omitted coordinates in the powerful parts. This is a weakening of the local Fourier estimate and uses no condition on the sum of the three budgets.

For every $I_a,I_b,I_c\subseteq\{1,\ldots,6\}$ the geometry-of-numbers bound [3, Proposition 4.1] gives

$$
D\le\max\left(L-\sum_s\sum_{i\in I_s}x_{s,i},\quad L-1+\sum_s\sum_{i\in I_s}(i-1)x_{s,i}\right).\tag{2.5}
$$

The two exponents are the exponents of the two terms in that proposition before replacing the product of coordinate ranges by a total radical budget. The factor $Y^{-1+O(\eta)}$ uses the lower bound for $c$ in Lemma 2.1, which remains available under three boxes. In particular, replacing $L$ inside (2.4) or (2.5) by a fixed number would unnecessarily weaken the program.

Here is a direct check of the local estimates before any total-budget substitution. For one letter write $A=\prod_i A_i$ and $P_j=\prod_{j\mid i}A_i$, and let $S(\theta)$ be its monomial exponential sum with the small coefficient fixed. Orthogonality and the divisor bound give $\int_0^1|S|^2\ll A Y^\varepsilon$. Cauchy–Schwarz over the coordinates whose indices are not divisible by $j$ gives

$$
\int_0^1|S|^4\ll \frac{A}{P_j}\,A^2Y^\varepsilon.
$$

Indeed the resulting equation is $(U^j-U'^j)V=W-W'$, where $V$ is the product of the fixed complementary coordinates and $W,W'$ are full monomial values. In the nonzero case choose the coordinates of $W,W'$ in $O(A^2)$ ways; $V$ then has divisor-type many coordinate choices, the power difference is fixed, and $U^j-U'^j=m\ne0$ has divisor-type many solutions by factoring $U-U'$. Lifting $U,U'$ to the selected coordinates costs another divisor-type factor. In the zero case one chooses one representation from each equal pair freely, again in $O(A^2)$ ways. Cauchy–Schwarz between the second and fourth moments, followed by Hölder for the three letters, therefore gives

$$
B_d\ll Y^\varepsilon\frac{(ABC)^{2/3}}{(P_j(A)P_k(B)P_\ell(C))^{1/6}}.
$$

The fixed small coefficient cancels in each moment identity, so it may share primes with coordinates of its own letter. Taking $j,k,\ell\in\{2,3,5\}$ proves (2.4).

For (2.5), freeze all complementary coordinates and write the remaining equation as $A'x+B'y=C'z$, where the free values have ranges of weighted sizes $X_A=\prod_{i\in I_a}A_i^i$, and similarly $X_B,X_C$. The classical primitive lattice-point bound used in [3, Proposition 4.1] is

$$
O\!\left(1+\frac{X_AX_BX_C}{\max(|A'|X_A,|B'|X_B,|C'|X_C)}\right).
$$

The denominator is at least a fixed $d$-dependent constant times $Y^{1-\eta}$ by Lemma 2.1. There are at most $(ABC)/\prod_s\prod_{i\in I_s}S_i$ frozen choices. Multiplying, and allowing divisor-type multiplicities for representing each free value, gives the two exponents in (2.5) with an error $O(\eta)+o(1)$. Across letters the fixed and free factors are pairwise coprime in every retained solution; sharing primes within a letter is irrelevant. This verifies explicitly that neither local estimate requires a bound on $t$.

Every variable of the program is nonnegative. There are $25$ variables, including the three auxiliary $F_s$ and $D$. We denote by $\mathcal P_0(\rho)$ the program (2.1)–(2.5). The implementation retains the redundant inequality $L\le t$, obtained by summing (2.1). It adds no assumption. No ordering of the three letters is made for a non-symmetric box. For equal boxes only, one may impose $x_{a,4}+2x_{a,5}\ge x_{b,4}+2x_{b,5}\ge x_{c,4}+2x_{c,5}$, since all inequalities of this finite relaxation are invariant under permuting the three exponent vectors.

## 3. Local arithmetic behind the collision constraints

The following details establish why the collision input does not require a total budget assumption. All constants are uniform for variables and coefficients bounded by a fixed power of $Y$.

**Lemma 3.1 (nonzero differences).** For $(j,k)\in\{(2,3),(3,4),(2,5),(3,5),(4,5)\}$, let $\mathcal V_{j,k}(P,Q)$ be the set of values $x^jy^k$ with $x\sim P$, $y\sim Q$. For $m\ne0$ the number of ordered value pairs of difference $m$ is

$$
\ll(PQ|m|)^\varepsilon\min(PQ,Q^2).
$$

For the first two pairs the bound also contains $P^2$ in the minimum.

*Proof.* The size bound is $PQ$. Fixing $y,y'$ leaves $y^kx^j-y'^kx'^j=m$. For $j=2,3$ this is an equation $AU^e-BV^e=m$ with $e=2,3$; for $j=4$ put $U=x^2,V=x'^2$ and use $e=2$. For $(2,3)$, fixing $x,x'$ instead gives $e=3$; for $(3,4)$ it gives $e=2$ after putting $U=y^2,V=y'^2$. It remains to verify a uniform divisor-type bound for these equations.

Set $\theta^e=A^{e-1}B$. If $\theta$ is rational, it is an integer. The identity $(AU)^e-(\theta V)^e=A^{e-1}m$ factors over the integers. For $e=2$, the two factors give divisor choices. For $e=3$, choose the nonzero divisor $h=AU-\theta V$ of $A^2m$. Substitution into $(AU)^2+AU\theta V+(\theta V)^2=A^2m/h$ leaves a quadratic equation in $V$, with at most two solutions. This gives a divisor-type bound.

Otherwise $K=\mathbb Q(\theta)$ has degree $e$ and the algebraic integer $\xi=AU-\theta V$ has norm $A^{e-1}m\ne0$. Work in the maximal order of $K$. There are at most $\prod_{p^r\Vert |A^{e-1}m|}\binom{r+e}{e}$ ideals of this norm, a divisor-type quantity uniformly for degree at most $3$: at most $e$ prime ideals lie above each rational prime, and their residue degrees only reduce the number of choices. Each principal ideal has generators differing by units. All conjugates of a candidate $\xi$ have size at most $Y^{O(1)}$; their product is a nonzero integer, so each has size at least $Y^{-O(1)}$. Ratios of two such generators therefore have logarithmic sizes in an interval of length $O(\log Y)$.

The fields have unit rank one: a real quadratic field, or a pure cubic field of signature $(1,1)$. There is an absolute positive lower bound for the logarithmic spacing. In the cubic case, for a positive real unit $\epsilon>1$ the other conjugates have modulus $\epsilon^{-1/2}$, and

$$
1\le |N(\epsilon-1)|\le4(\epsilon-1),
$$

so $\epsilon\ge5/4$. In the quadratic case the other conjugate has modulus $\epsilon^{-1}$, and $1\le |N(\epsilon-1)|\le2(\epsilon-1)$, giving $\epsilon\ge3/2$. Torsion has bounded size. Consequently each ideal contributes $O(\log Y)$ candidate generators. The representation $AU-\theta V$ is injective in $(U,V)$ since $1,\theta$ are linearly independent. This proves the required uniform bound and hence the lemma. $\square$

**Lemma 3.2 (unit congruence energy).** If $1\le j<k\le6$ and $\gcd(j,k)=1$, the number of coordinate quadruples, all units modulo $M$, satisfying $x^jy^k\equiv x'^jy'^k\pmod M$ is

$$
\ll(PQM)^\varepsilon PQ\sqrt{(1+P^2/M)(1+Q^2/M)}.
$$

*Proof.* In $G=(\mathbb Z/M\mathbb Z)^\times$ put $g=x/x'$ and $h=y'/y$. Choose integers $u,v$ with $uk-vj=1$. The maps $z\mapsto(z^k,z^j)$ and $(g,h)\mapsto g^uh^{-v}$ are inverse between $G$ and the solutions of $g^j=h^k$, by direct substitution. Let $R_N(w)$ count pairs $s,t\sim N$ with $s/t=w$ in $G$. The energy is $\sum_{z\in G}R_P(z^k)R_Q(z^j)$. Fibres of the power maps have at most $36^{\omega(M)}\ll M^\varepsilon$ elements, by the cyclic structure at odd prime powers and the two cyclic factors at powers of $2$.

Cauchy–Schwarz reduces the assertion to $\sum_wR_N(w)^2\ll N^{2+\varepsilon}(1+N^2/M)$. For the latter, fix $s,t'$, hence the product $st'\le4N^2$. The product $s't$ lies in its residue class modulo $M$, and has $O(1+N^2/M)$ possible values, each with a divisor-type number of factorizations. This proves the estimate, including $M=1$. $\square$

Put

$$
\kappa(p,q;w)=p+q+\tfrac12\big((2p-w)_++(2q-w)_+\big).
$$

For distinct letters $A,B$, let $C$ be the remaining letter; choose a coprime pair $j<k\le6$ and a nonempty $I\subseteq\{1,\ldots,6\}$. Define

$$
p=x_{A,j},\quad q=x_{A,k},\quad f_A=u_A-p-q,\quad \delta=\sum_{i\in I}x_{B,i},\quad f_B=u_B-\delta,
$$

$$
w_B=\sum_{i\notin I,\,i\le6}i x_{B,i}+7\left(u_B-\sum_{i\le6}x_{B,i}\right).
$$

Let $\delta_*$ be $\delta$, with the following additional entries admitted in its minimum: $2x_{B,2},2x_{B,3}$ if $I=\{2,3\}$; $2x_{B,3},2x_{B,4}$ if $I=\{3,4\}$; and $2x_{B,5}$ if $I\in\{\{2,5\},\{3,5\},\{4,5\}\}$.

**Proposition 3.3 (collision inequality of [7]).** Each box satisfies

$$
D\le f_A+f_B+\max\left(u_C,\frac{u_C+\delta_*+\kappa(p,q;w_B)}2\right).\tag{3.1}
$$

*Proof.* Freeze the coordinates of $A$ outside $\{j,k\}$ and of $B$ outside $I$, including all coordinates of index at least $7$. There are at most $Y^{f_A+f_B+o(1)}$ choices. Write the equation with suitable signs as $\pm M_Au\pm M_Bv=\pm z$. Here $u$ is the free two-coordinate monomial of $A$, $v$ the free monomial of $B$, and $z$ the entire value of $C$. Each value has at most $Y^{o(1)}$ coordinate representations. The number of possible $z$ is at most $W=Y^{u_C+o(1)}$.

For a fixed fibre, let $N$ count pairs of values $(u,v)$ and let $E$ count ordered off-diagonal pairs yielding the same $z$. Cauchy–Schwarz gives $N^2\le W(N+E)$ and thus $N\ll W+\sqrt{WE}$. In a nonempty primitive fibre $\gcd(M_A,M_B)=1$, and every $u$ is a unit modulo $M_B$. Subtracting two equations gives $M_A(u-u')=\pm M_B(v-v')$. An off-diagonal pair has $u\ne u'$ and $v\ne v'$. The number of $(u,u')$ is at most the congruence energy of Lemma 3.2, hence $Y^{\kappa(p,q;w_B)+o(1)}$, since $M_B\ge Y^{w_B}$.

For fixed $u,u'$ the difference $v-v'$ is a fixed nonzero integer. Choosing $v$ gives at most $Y^{\delta+o(1)}$ possibilities; in the five specified cases Lemma 3.1 gives the additional caps defining $\delta_*$. Therefore $E\le Y^{\kappa+\delta_*+o(1)}$. Substitution into the Cauchy inequality and multiplication by the number of frozen choices proves (3.1). No step invokes a total radical bound. $\square$

Let $\mathcal P_{\mathrm{ss0}}(\rho)$ be $\mathcal P_0(\rho)$ with all $6\cdot11\cdot63=4158$ inequalities (3.1). This is precisely the empty-third-modulus subfamily of [7]. For completeness, the extra frozen-modulus input of [7] also survives separate budgets. If $O_C$ is frozen, put $f_C=\sum_{i\in O_C}x_{C,i}$ and $w_C=\sum_{i\in O_C}i x_{C,i}$. Freeze these coordinates in addition to those in the preceding proof. There are $Y^{f_C}$ extra frozen choices and only $Y^{u_C-f_C+o(1)}$ possible remaining third-letter values. Primitivity makes the frozen coefficient $M_C\ge Y^{w_C}$ coprime to the second-letter factors. Fix the other free coordinates of $B$ and a choice of $k_B\in I$. The equation modulo $M_C$ puts its $k_B$-th coordinate into a bounded-divisor number of residue classes: the kernel of the $k_B$-th power map on the unit group has size $M_C^{o(1)}$. This coordinate therefore has at most $Y^{(x_{B,k_B}-w_C)_++o(1)}$ choices. Consequently the difference factor is bounded by

$$
\delta_{\rm lock}=\sum_{i\in I\setminus\{k_B\}}x_{B,i}+(x_{B,k_B}-w_C)_+,
$$

and the off-diagonal exponent is $f_A+f_B+f_C+(u_C-f_C+\delta_{\rm lock}+\kappa)/2$; the diagonal exponent remains $f_A+f_B+u_C$. This proof uses only local coprimality and sizes. The generalization with a nonempty frozen set on $C$ is not part of the numerical program, so our exact optimum does not purport to be the optimum of that stronger family. The older two-letter inequalities are contained in (3.1). The determinant and Thue inputs of [1] are not used in either program.

## 4. Rational certificates and parameter envelopes

Denote the suprema of these programs by $D_0(\rho)$ and $D_{\mathrm{ss0}}(\rho)$. These are maxima over finitely many closed polyhedra. The nonnegative root variables are bounded: the height constraints bound $u_s$, (2.3) bounds $D$, and (2.4) bounds the auxiliary variables.

**Lemma 4.1 (exact certificates).** Suppose a tree branches exhaustively on (2.5) and (3.1), and at every leaf records nonnegative rational multipliers $y$ (with only their positive support serialized) on the path inequalities $Ax\le b$ such that $(y^TA)_D=1$ and every other entry of $y^TA$ is nonnegative. Then every feasible point satisfies $D\le\max_\ell y_\ell^Tb_\ell$. If an exactly feasible rational point attains that maximum, this is the exact optimum of the specified program.

*Proof.* Multiply the path inequalities by $y\ge0$ and sum. Nonnegativity of all variables gives $D\le y^Tb$. Every feasible point lies in at least one child at every branch, hence in a leaf. A feasible attaining point supplies the reverse inequality for the program optimum. $\square$

The coverage hypothesis is parameter independent: every branch region is retained, including regions that happen to be infeasible at the source box. Such a region is closed by a normalized upper-bound multiplier of Lemma 4.1 with all its budget coefficients retained, rather than being deleted or permanently declared empty. The same applies to branches pruned by an incumbent. No parameter-specific preprocessing inequality is used as a parameter-independent cut.

A geometric node has both branches of (2.5). A collision node has the diagonal branch and four sign quadrants for $2p-w_B$ and $2q-w_B$ in the off-diagonal expression. All caps in $\delta_*$ are imposed within each off-diagonal branch. In the inherited nine-branch encoding the third sign argument is $x_{B,k_B}$, which is nonnegative; taking branches $0,2,4,6,8$ covers the full domain, including boundaries. Thus five children suffice for the empty-third-modulus family. An independent specification, not relying on these numeric branch labels, is the following. Write $h=D-f_A-f_B$, $r=2p-w_B$, $s=2q-w_B$, and let $\mathcal C$ be the list consisting of $\delta$ and its applicable extra caps. The diagonal branch is $h\le u_C$. For each $(\epsilon_1,\epsilon_2)\in\{0,1\}^2$, impose

$$
(1-2\epsilon_1)r\le0,\qquad(1-2\epsilon_2)s\le0,
$$

and, simultaneously for every $d_*\in\mathcal C$,

$$
2h\le u_C+d_*+p+q+\tfrac12(\epsilon_1r+\epsilon_2s).
$$

These are the four off-diagonal linear systems reconstructed by the checker; all sign boundaries are included.

The root row order is: the redundant sum row $0$, the nineteen non-budget rows of (2.2)–(2.4), and the box rows $20,21,22$. Optional ordering rows for equal budgets follow these. For a leaf at parameter $\rho^0$ with bound $b_\ell$, set

$$
\sigma_{\ell,s}=y_{\ell,0}+y_{\ell,20+s},\qquad e_\ell(\rho)=b_\ell+\sum_{s=0}^2\sigma_{\ell,s}(\rho_s-\rho_s^0).\tag{4.1}
$$

The slopes include the redundant sum-row multiplier; omitting it would give an incorrect envelope.

**Proposition 4.2 (three-parameter envelope).** A tree without ordering gives $D_{\mathrm{ss0}}(\rho)\le E(\rho)=\max_\ell e_\ell(\rho)$ for every $\rho\in(0,1]^3$, even if it was generated at another box. For a tree with ordering, replace $E(\rho)$ by $\max_{\pi\in S_3}E(\pi\rho)$. The minimum of the bounds from any finite collection of trees is again an upper bound.

*Proof.* All matrix coefficients and branch conditions are independent of $\rho$. Changing the box changes only the four right-hand sides recorded in (4.1). Each leaf multiplier remains valid and proves its affine bound at the new parameter. Exhaustiveness proves the first assertion. In the ordered case relabel any feasible exponent vector so that it satisfies the ordering; its box is a permutation of $\rho$. The inequality family is invariant under relabelling. Taking the maximum over the six possibilities proves the second assertion. Finally take the minimum of independently valid upper bounds. $\square$

Each such envelope is continuous, convex, piecewise affine, and coordinatewise nondecreasing. The minimum over trees is continuous and nondecreasing but need not be convex or concave. Linear interpolation of grid optima is not used.

## 5. Passage back to the counting function

**Proposition 5.1 (arithmetic transfer).** For either program, any certified bound $U(\rho)$ from its finite trees implies

$$
S_\rho(X)\ll_{\rho,\varepsilon}X^{U(\rho)+\varepsilon}.
$$

*Proof.* Fix $\rho$ and the choice of program, and denote its exact maximum by $D_P$. Its feasible set is nonempty and compact. Write all defining constraints as finitely many continuous inequalities $g_r(v;\rho)\le0$ in the $25$ retained variables. In a fixed common compact box containing both the exact feasible set and the vectors arising from sufficiently large nonempty arithmetic boxes, the following stability statement holds: for every $\delta>0$ there is $\tau>0$ such that $g_r(v;\rho)\le\tau$ for every $r$ implies $D(v)\le D_P+\delta$. Otherwise a convergent subsequence of approximate feasible points would have an exactly feasible limit with $D>D_P$.

Take $\delta=\varepsilon/4$. First choose a sufficiently small fixed $\eta>0$ so that $3\eta<\varepsilon/8$ and the anatomy errors in budgets and heights are below $\tau/4$. Then fix $H$ and $d=H^2$ from Lemma 2.1. Choose the arbitrarily small powers in the local divisor, Fourier and collision estimates small enough that their logarithmic errors are below $\tau/4$. Only after making these choices let $Y$ be sufficiently large. This absorbs all constants depending on $d$, all dyadic endpoint constants, and all logarithmic multiplicities. There is no assumption that a prescribed $\eta(Y)$ tends to zero at any particular rate.

Partition the original triples in $Y/2<c\le Y$ by their deterministic small coefficients and coordinate boxes. For each nonempty class let $N$ be its cardinality and $D=\log_Y N$, and choose $F_s$ as the maximum of its three displayed lower bounds. The local estimates apply to an enlarged coordinate box containing this class, so its vector satisfies all $g_r\le\tau$ once $Y$ is large. These vectors lie in a common compact box: $u_s\le1$, every retained coordinate is at most $1$, the chosen $F_s\le1$, and $D\le3$ for large $Y$. Stability gives $N\le Y^{D_P+\varepsilon/4}$.

The number of coefficient/box classes is at most $Y^{3\eta}(1+\log_2Y)^{3d}$, which is at most $Y^{\varepsilon/4}$ for sufficiently large $Y$, since $d$ is now fixed. Thus the entire height block contributes at most $Y^{D_P+\varepsilon/2}$. Sum the dyadic height blocks and absorb finitely many small heights to obtain $S_\rho(X)\ll X^{D_P+\varepsilon}$. Finally $D_P\le U(\rho)$ by the complete certificates, proving the assertion. $\square$

The argument covers equality in the radical restrictions and equality on grid faces. It does not require the sum of the three budgets to be below $1$, nor that both summands have size comparable to $c$.

## 6. Certified exponents

**Theorem 6.1 (grid).** At every parameter listed below, and at every permutation of its three entries, with a recorded value $D_{\mathrm{ss0}}$, the exact maximum of $\mathcal P_{\mathrm{ss0}}(\rho)$ is that value, and

$$
S_\rho(X)\ll_{\rho,\varepsilon}X^{D_{\mathrm{ss0}}(\rho)+\varepsilon}.
$$

The permutation assertion concerns the symmetric exponent relaxation, whose constraints include all ordered letter pairs and all geometric subsets; it does not assert a symmetry of the arithmetic counting functions. The column $D_0$ records the exact maximum using the Fourier and geometric inputs alone. The column labeled `[7]-based baseline` is the minimum of the explicit literature bounds of Section 1 and the parametrically evaluated total-budget certificate trees of [7]. The final column takes the minimum of $D_{\mathrm{ss0}}(\rho)$, the [7]-based baseline, and all verified three-parameter certificate envelopes.

| $\rho$ | $D_0$ | $D_{\mathrm{ss0}}$ | [7]-based baseline | Certified exponent |
|---|---|---|---|---|
| (1/5,1/5,1/5) | 2/5 | 2/5 | 2/5 | 2/5 |
| (1/4,1/4,1/4) | 35/76 | 35/76 | 35/76 | 35/76 |
| (3/10,3/10,3/10) | 141/260 | 23/43 | 71/130 | 23/43 |
| (1/4,1/3,1/3) | 29/52 | 7411/13644 | 29/52 | 7411/13644 |
| (1/4,1/4,1/2) | 1/2 | 1/2 | 1/2 | 1/2 |
| (1/4,1/3,5/12) | 7/12 | 7/12 | 7/12 | 7/12 |
| (1/3,1/3,1/3) | 3/5 | 283/477 | 5588/9417 | 283/477 |
| (1/5,1/3,1/2) | 8/15 | 8/15 | 8/15 | 8/15 |
| (2/5,2/5,2/5) | 5/7 | 88/125 | 398699/538970 | 88/125 |
| (1/2,1/2,1/2) | 7/8 | 7/8 | 15/16 | 7/8 |
| (1/2,2/3,5/6) | 12/11 | 19/18 | 1 | 1 |
| (2/3,2/3,2/3) | 12/11 | 12/11 | 1 | 1 |

At $\rho=(1/3,1/3,1/3)$ ($t=1$), $D_{\mathrm{ss0}}(1/3,1/3,1/3)=283/477<5588/9417$ is a strict improvement over the [7]-based baseline (by $155/1497303=465/4491909$). However, as noted in Section 1, the companion work [8, Theorem 1.2] obtains $N_1(X)\ll_\varepsilon X^{589903/1000008+\varepsilon}$ using squared-variable and twisted-energy collision constraints not included in $\mathcal P_{\mathrm{ss0}}$, and $589903/1000008<283/477$ through $S_{1/3,1/3,1/3}(X)\le N_1(X)$. Thus $283/477$ records the exact optimum of $\mathcal P_{\mathrm{ss0}}(1/3,1/3,1/3)$ relative to the [7]-based relaxation baseline rather than the strongest available arithmetic bound at $t=1$. By contrast, at $\rho=(3/10,3/10,3/10)$ ($t=9/10$), the separate-budget collision optimum $23/43$ strictly improves both the [7]-based baseline $71/130$ and the total-budget exponent $677/1240$ of [8, Theorem 1.2].

**Theorem 6.2 (a strict improvement).** For every $\varepsilon>0$,

$$
S_{3/10,3/10,3/10}(X)\ll_\varepsilon X^{23/43+\varepsilon}.
$$

The [7]-based baseline exponent at this point is $71/130$, from the total-budget curve in [7]. Separate budgets alone give $D_0=141/260$, a saving of $1/260$ over $71/130$. Incorporating all generalized empty-third-modulus collision inequalities gives $D_{\mathrm{ss0}}=23/43$, a further saving of $83/11180$. The total saving over [7] is $63/5590$, and the saving over the refined total-budget exponent $677/1240$ of [8, Theorem 1.2] is $591/53320$. For comparison, the smallest explicit bound in [2], [1], [4] and [3] is $237/400$ here.

The upper certificate has 3181 leaves. An attaining point has identical head vectors on the three letters,

$$
(x_{s,1},\ldots,x_{s,6})=\frac1{860}(44,0,91,72,51,0),\qquad u_s=\frac3{10},\qquad D=\frac{23}{43}.
$$

One may take the auxiliary values $F_a=77/430$, $F_b=F_c=91/860$, as in the certificate. The coordinate sums are $3/10$ and each weighted height is $1$. The checker verifies the full geometric family and all 4158 collision inequalities at this point. Its feasibility proves optimality of the finite program; it does not give an arithmetic lower bound for $S$.

**Corollary 6.3 (full-family grid optima).** The $\mathcal P_{\mathrm{ss0}}$ value in the table is also the exact optimum of the complete inherited frozen-third-modulus family at the following parameters: $(1/2,2/3,5/6)$, $(1/3,1/3,1/3)$, $(1/4,1/4,1/2)$, $(1/5,1/5,1/5)$, $(2/3,2/3,2/3)$, $(2/5,2/5,2/5)$. The full program retains every $\mathcal P_{\mathrm{ss0}}$ inequality, including its difference caps at empty $O_C$. The existing upper tree bounds this stronger program, and the attaining point passes all 811008 members. No second upper search is required. These are finite-program equalities, not arithmetic lower bounds.

The attaining point for $23/43$ at the central parameter is cut by a nonempty-third-modulus constraint. A separately verified full-family point gives the certified interval $41/80\le D_{\mathrm{full}}(3/10,3/10,3/10)\le23/43$. The lower endpoint is a feasible point of the finite relaxation, recorded in the supplied full-family feasible-point certificate and verified by the supplied full-family point checker; it is not an arithmetic counting lower bound. The complete-family optimum at this point is not determined here.

**Theorem 6.4 (envelope).** For every $\rho\in(0,1]^3$, take the minimum over the verified $\mathcal P_{\mathrm{ss0}}$ and base $\mathcal P_0$ trees of the envelopes in Proposition 4.2, applying all six permutations to every ordered source tree. Call the resulting explicit function $E(\rho)$. Then

$$
S_\rho(X)\ll_{\rho,\varepsilon}X^{E(\rho)+\varepsilon}.
$$

The affine forms are supplied in certificates/envelopes.json; they are reconstructed from the complete trees by summarize.py, rather than trusted as additional certificates. This is a proved three-parameter upper envelope, not interpolation of grid values.

For the central tree let $M=\max_\ell\sum_s\sigma_{\ell,s}$. Exact evaluation gives

$$
M=5,\qquad h=63/55900.
$$

Consequently every $\rho\in[3/10,3/10+h]^3$ satisfies

$$
S_\rho(X)\ll_{\rho,\varepsilon}X^{6043/11180+\varepsilon}.
$$

Here $0<h\le63/11180<7/10$, so the cube stays within the parameter domain. This exponent is strictly smaller than $71/130$. The [7]-based comparison function is coordinatewise nondecreasing, being the minimum of coordinatewise nondecreasing valid bounds, so this entire cube gives a strict improvement on that comparison function. The proof is $E(\rho)\le23/43+Mh$ on the cube, together with the displayed choice $h=(71/130-23/43)/(2\max(M,1))$.

To make the quantitative comparison visible alongside the exact rational table and certificates, Figure 1 (generated from the verified envelope data by `plot_diagonal_slice.py`) plots the diagonal slice $\rho=(u,u,u)$ ($t=3u$) for $u\in[0.18,0.70]$, together with a magnified view near $u=3/10$ and $u=1/3$. The plot distinguishes the explicit literature bound of [1]–[3] (including the bound $3/5$ of [3, Theorem 1.3] for $3u<1$, with an open endpoint at $u=1/3$), the [7]-based total-budget baseline, the pure separate-budget base tree envelope $E_0(u,u,u)$ from the $\mathcal P_0$ trees, the pure separate-budget collision tree envelope $E(u,u,u)$ of Theorem 6.4 (both taking the exact value $12/11$ at $u=2/3$, distinguished from the combined arithmetic bound $1$), the exact diagonal grid optima $D_0(u,u,u)$ and $D_{\mathrm{ss0}}(u,u,u)$ (with $D_0(2/3,2/3,2/3)=D_{\mathrm{ss0}}(2/3,2/3,2/3)=12/11$), and the total-budget values $677/1240$ ($u=3/10$) and $589903/1000008$ ($u=1/3$) of [8, Theorem 1.2].

![Figure 1. Diagonal slice rho = (u,u,u) (t = 3u) of the three-parameter upper envelopes E_0(u,u,u) and E(u,u,u) compared with the [1]–[3] bound, the [7]-based total-budget baseline, and the [8] total-budget bounds.](supplement/figure-1.png)

*Figure 1.* Diagonal slice $\rho=(u,u,u)$ ($t=3u$) of the three-parameter piecewise affine tree envelopes $E_0(u,u,u)$ ($\mathcal P_0$) and $E(u,u,u)$ ($\mathcal P_{\mathrm{ss0}}$, Theorem 6.4), compared with the explicit literature bound of [1]–[3] (including $3/5$ for $3u<1$, open endpoint at $u=1/3$), the [7]-based total-budget baseline, the exact diagonal grid optima $D_0(u,u,u)$ and $D_{\mathrm{ss0}}(u,u,u)$ (reaching $12/11$ at $u=2/3$), and the total-budget values of [8, Theorem 1.2] at $u=3/10$ and $u=1/3$.

**Verification and reproduction.** Generation uses a single process with numerical libraries and HiGHS restricted to one thread. Each computation has a hard deadline below two hours. Floating point chooses candidate bases and branches; every recorded multiplier is solved and checked over the rational numbers. The verification entry point `verify_release.py` and all verification scripts (`check.py`, `rows_checker.py`, `check_full_family.py`, `check_full_lower.py`, `fault_checks.py`, `prior_total_check.py`, and `summarize.py`) use only the Python standard library, import no optimizer or plotting library, reconstruct every branch independently, check every leaf, and check every attaining point against the entire defining family. The program `check_full_family.py` clears denominators and checks the full generalized family with integer arithmetic. Exactly identical subset-sum pairs may be deduplicated; no tolerance is involved. The supplement replays the total-budget tree for the central comparison and records the previously published affine envelopes for the remaining background comparisons. Six deliberately corrupted certificates are rejected by `fault_checks.py`. The optional script `plot_diagonal_slice.py` uses `matplotlib` to regenerate `figure-1.png` from `certificates.tar.xz` and is not imported by `verify_release.py`.

## 7. Interpretation and scope

The improvement uses the collision mechanism of [7] and retains the three radical budgets through the finite optimization; it introduces no new Diophantine counting lemma. At $(1/4,1/4,1/4)$ the two program optima coincide with the inherited value $35/76$, and at $(1/5,1/3,1/2)$ the $\mathcal P_{\mathrm{ss0}}$ value $8/15$ is the elementary two-letter exponent. Those points provide no additional saving in that program. The grid records such cases alongside the improvements.

The full-family statements, where recorded, concern exactly the 811008 inherited inequalities with the caps specified here. The determinant and Thue bounds of the earlier paper [1], or a new arithmetic input, could further shrink the program and are not covered by an assertion of optimality for this family. The normalization also discards information about a summand that is much smaller than the dyadic height. None of our positive exponents asserts finiteness of the exceptional set or establishes the conjectural exponent of the arithmetic counting function.

## References

[1] T. Browning, J. D. Lichtman and J. Teräväinen, *Bounds on the exceptional set in the abc conjecture*, arXiv:2410.12234v1, 2024. https://arxiv.org/html/2410.12234v1 .

[2] D. M. Kane, *On the number of ABC solutions with restricted radical sizes*, J. Number Theory 154 (2015), 32–43. https://doi.org/10.1016/j.jnt.2014.09.021 ; https://arxiv.org/abs/1104.2635v2 .

[3] C. Bernert, T. Browning, J. D. Lichtman and J. Teräväinen, *Bounds on the exceptional set in the abc conjecture*, arXiv:2410.12234v2, 2026. https://arxiv.org/html/2410.12234v2 .

[4] C. Bernert, *The exceptional set in the abc conjecture*, arXiv:2506.13364v1, 2025. https://arxiv.org/html/2506.13364v1 .

[5] Runbo Li, *On the exceptional set in the abc conjecture*, arXiv:2507.02885v1, 2025. https://arxiv.org/abs/2507.02885 .

[6] N. A. Carella, *Note on the Exceptional Set in the ABC Conjecture*, arXiv:2608.16764v2, 2026. https://arxiv.org/html/2608.16764v2 .

[7] H. Li, *Collision inequalities and the radical budget for the exceptional set in the abc conjecture*, math_17 v2, 2026. https://rstation.ai/problems/math/papers/17/v2 (v1: https://rstation.ai/problems/math/papers/17/v1).

[8] H. Li, *Squares and twisted energy in the exceptional set of the abc conjecture*, math_28 v2, 2026. https://rstation.ai/problems/math/papers/28/v2 (v1: https://rstation.ai/problems/math/papers/28/v1).

## Data availability

The accompanying supplement contains the reproducible finite certificates, diagonal-slice plot, and verification instructions.

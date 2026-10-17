# Lifted line relaxations for the no-three-in-line problem

## 1. Problem and contributions

Let $G_n=\{0,\ldots,n-1\}^2$. A genuine no-three-in-line set has at most
two points on every Euclidean line. The community target asks for an
unbounded family of such sets with more than $1.8n$ points. The classical
construction has asymptotic density $3/2$ [1]. This paper concerns the
ability of two standard optimization hierarchies to certify infeasibility
of the target; it does not construct a genuine family.

Let $K_n$ be the point-variable relaxation
$$
 0\le x_v\le1\quad(v\in G_n),\qquad
 \sum_{v\in\ell\cap G_n}x_v\le2\quad\text{for every line }\ell.
 \tag{1}
$$
Only lines meeting at least three grid points need be listed; shorter
line inequalities follow from the variable bounds. The integer solutions
are exactly the genuine no-three sets, and row capacities give
$\sum_vx_v\le2n$. The assignment $x_v=2/n$ attains this linear-programming
bound. Retaining all lines is the standard exact formulation, also used
in modern constraint-programming searches [2].

We prove complementary lifting limitations and a compatible joint certificate.

**Theorem 1.** Let $r\ge0$ and $n\ge512(r+1)^{3/2}$. The $r$-round
Sherali–Adams relaxation of
$$
 K_n\cap\left\{\sum_vx_v\ge\frac95n\right\}
 \tag{2}
$$
is feasible. An explicit rational moment family has first-moment sum
$2n-8(r+1)$.

Thus the target inequality may be imposed *before* lifting, and feasibility
still survives order $n^{2/3}$ rounds. The theorem does not assert that
an integer solution exists. Our convention counts the degree of the
Boolean multiplier; it is specified below.

**Theorem 2.** For every prime $n\ge13$, one Lovász–Schrijver $N_+$ step
applied to $K_n$ has optimum $2n$. The same is true when total cardinality
$2n$ and every row and column sum being two are added as base equalities.
The moment certificate comes from an explicit distribution on unions of
two parallel modular lines. Each support in this distribution has a
genuine no-three subset of size at most $8\lceil\sqrt n\rceil$.

**Theorem 6 (joint certificate, proved in Section 6).** For prime
$n\ge1024(r+1)^{3/2}$, $r\ge1$, a different moment family satisfies all
$r$-round SA constraints with target $19n/10$ and has a PSD first moment
matrix, with objective $2n-32(r+1)$. Prime padding gives the corresponding
$1.8n$ target statement on all sufficiently large sides.

The certificates serve different purposes. Theorem 1 concerns many
linear-programming rounds with a target inequality, and its moment matrix
is explicitly not positive semidefinite. Theorem 2 supplies a positive
semidefinite certificate with exact axis saturation, for one round. We
make no claim about iterating $N_+$ or higher Lasserre levels. Theorem 6
repairs first-matrix positivity with a modular pair construction, while its
third moments explicitly fail conditional PSD.

Prime padding implies that one $N_+$ step retains optimum $(2-o(1))n$
on all square boards, and remains feasible with the $1.8n$ target imposed
before lifting. The prime-specific exact cardinality statement and this
all-board asymptotic statement are distinguished in Section 5.

## 2. Related work and hierarchy conventions

Sherali–Adams and Lovász–Schrijver lifting are established methods. We
use the definitions and comparisons in Laurent's survey [3, Sections
2, 3.2 and 4]. For a linear base system, define $\mathrm{SA}_r$ by
multiplying every inequality, including variable bounds, by
$$
 x_A\prod_{b\in B}(1-x_b),\qquad
 A\cap B=\varnothing,\quad |A|+|B|\le r,
 \tag{3}
$$
then replacing $x_v^2$ by $x_v$ and linearizing squarefree monomials.
Write $y_A$ for the moment replacing $x_A$, and set $y_\varnothing=1$.
Moments through degree $r+1$ suffice. Equalities are treated as pairs of
inequalities. In particular, $\mathrm{SA}_0$ is the base LP. This
explicit convention avoids index shifts between sources.

For a convex polytope $K\subseteq[0,1]^N$, put
$$
 \widetilde K=\{\lambda(1,x):\lambda\ge0,\ x\in K\}.
$$
A first $N_+$ certificate is a symmetric positive semidefinite matrix $Y$
indexed by $0$ and the $N$ variables, with $Y_{00}=1$,
$Y_{0v}=Y_{vv}$, and
$$
 Ye_v,\quad Y(e_0-e_v)\in\widetilde K
 \quad\text{for every }v.
 \tag{4}
$$
The first column supplies the lifted point. These are precisely Laurent's
homogenized column conditions [3, equations (2)–(3)].

Our geometric estimate is also based on prior work. Aichholzer,
Eppstein and Hainzl [4, Theorems 1 and 3] count long integer lines
through a point and prove an $\Omega(n^{2/3})$ lower bound on the
geometric domination number. We use a coarse, self-contained version of
that same direction count to bound the cells covered by secants of a
small conditioning set. The direction-count mechanism and its exponent
are not new. Our contribution is the pair-weighted moment family and
the verification of every exclusion multiplier and cardinality lift.

Earlier work on quarter-turn supports [5] gives unbounded gaps for
pair compatibility and, using density-Hales–Jewett gadgets, even for
supports with no four collinear. Those are support-restricted theorems.
The present main results apply directly to the full square-grid line
formulation and keep the target-cardinality condition inside the lifted
system. The elementary local-law consequences in Section 7 connect the
two settings; they are not prerequisites for Theorems 1–2.

Prellberg [6, Section 4] studies a four-direction LP on one checkerboard
color class and constructs continuum dual bounds for that restricted
support. Here the base system contains every Euclidean line on the full
board, and the results concern its Boolean lifts and first semidefinite
step. The support restriction and the hierarchy operation are separate
changes of formulation.

Neither the existence of a high-valued lifted point nor the poor quality
of supports used to represent its moments is an integrality-gap theorem
for the unrestricted grid: its true asymptotic optimum remains unknown.
No complexity-theoretic hardness statement is made.

## 3. Explicit many-round target feasibility

We prove Theorem 1. Put $N=n^2$ and
$$
 \delta=\frac{8(r+1)}n,\qquad p=\frac{2-\delta}n.
 \tag{5}
$$
Our hypothesis gives $0<\delta\le1/64$, $0<p\le2/n$, and
$p(r+1)\le1/256$. The symbol $p$ in this section is a rational inclusion
parameter, not a prime.

For distinct grid points $u,v$, let $L_{uv}$ be the number of grid points
on their full Euclidean line, and define
$$
 w_{uv}=\min\left\{1,\frac{1-\delta}{p(L_{uv}-1)}\right\}.
 \tag{6}
$$
For every set $A$ with $|A|\le r+1$, put
$$
 y_A=p^{|A|}\prod_{\{u,v\}\subset A}w_{uv}\,
 \mathbf1\{A\text{ contains no collinear triple}\}.
 \tag{7}
$$
An empty product equals one. These rational numbers specify moments,
not a claimed probability law on all $N$ indicators. We verify the
linearized constraints directly.

### 3.1 Local event positivity

For disjoint $A,C$ in the moment range,
$$
 0\le y_{A\cup C}\le p^{|C|}y_A.
 \tag{8}
$$
All new pair factors are at most one, and an invalid $A$ has only invalid
supersets. For disjoint $A,B$, the lifted Boolean event is
$$
 E(A,B)=\sum_{C\subseteq B}(-1)^{|C|}y_{A\cup C}.
$$
Consequently, if $|A|+|B|\le r+1$,
$$
 E(A,B)\ge y_A\{2-(1+p)^{|B|}\}\ge0,
 \tag{9}
$$
because $(1+p)^{r+1}\le e^{1/256}<2$. After simplifying any overlapping
variable in a multiplier, these event inequalities verify all lifts of
$0\le x_v\le1$.

### 3.2 Every lifted line capacity

For a line $\ell$ with $L=|\ell\cap G_n|$, define
$$
 G_\ell(A)=2y_A-\sum_{u\in\ell\cap G_n}y_{A\cup\{u\}}.
$$
If $y_A=0$, this expression and every extension are zero. Otherwise
$a=|A\cap\ell|\le2$.

If $a=2$, all new points on $\ell$ would create a triple, and
$G_\ell(A)=0$. Every extension has zero slack too: it is either invalid,
or still has exactly the same two selected points on $\ell$.

If $a=0$, the sum is at most $Lp\,y_A\le(2-\delta)y_A$. If $a=1$
and $L\ge2$, every new point on $\ell$ carries the pair factor (6),
so the sum divided by $y_A$ is at most
$$
 1+(L-1)p\min\left\{1,\frac{1-\delta}{p(L-1)}\right\}
 \le2-\delta.
$$
For $L=1$ the same conclusion is immediate. Thus, whenever $a\le1$,
$$
 \delta y_A\le G_\ell(A)\le2y_A.
 \tag{10}
$$
All positive-monomial line slacks are nonnegative. For a multiplier with
exclusions $B$, if $a=2$ every term is zero. Otherwise, by (8)–(10),
$$
 \sum_{C\subseteq B}(-1)^{|C|}G_\ell(A\cup C)
 \ge y_A\{\delta-2[(1+p)^{|B|}-1]\}\ge0.
 \tag{11}
$$
Indeed, $rp\le1/256$ and $e^t-1\le2t$ for $0\le t\le1/2$, whence
$2[(1+p)^r-1]\le4rp\le8r/n\le\delta$. This checks every lifted line
capacity, not only multipliers supported on that line.

### 3.3 Cells outside the exceptional lines

We need a lower bound on the total extension moment. Pair factors below
one occur only in the eight primitive unoriented directions of height
at most two. To see this, a penalized pair has
$$
 L_{uv}-1>\frac{1-\delta}{p}
 =n\frac{1-\delta}{2-\delta}>\frac n3.
$$
A primitive direction of height at least three has
$L-1\le(n-1)/3<n/3$, a contradiction. The eight directions are the
axes and slopes $\pm1,\pm2,\pm1/2$.

The following estimate is the coarse form of the prior geometric-domination
argument [4] used here.

**Lemma 3.** If $A\subseteq G_n$ has $s$ points and no collinear triple,
the sum of the full grid lengths of its secants is at most $5ns^{3/2}$.

*Proof.* The claim is empty for $s=0$. At a fixed $a\in A$, the secant
directions to the other points are distinct up to sign. There are at most
$4d$ primitive unoriented directions of height $d$. With
$t=\lceil\sqrt s\rceil$,
$$
 \sum_{b\ne a}\frac1{h_{ab}}\le4t+s/t\le9\sqrt s.
$$
A line of height $h$ contains at most $n/h+1$ grid points. Sum over
$a\in A$ and divide by two, since every secant has two endpoints in $A$.
The result is at most
$$
 \frac92ns^{3/2}+\frac12s(s-1)\le5ns^{3/2},
$$
using $s\le n^2$. $\square$

For valid $A$ of size $s\le r$, declare exceptional every point on its
secants and on the eight short-direction lines through each point of
$A$. There are at most
$$
 nD(s),\qquad D(s)=8s+5s^{3/2},
 \tag{12}
$$
exceptional cells. When $s>0$ these include $A$. Every nonexceptional
cell $u$ creates no triple and has only pair factors one, so
$y_{A\cup\{u\}}=py_A$ exactly. This equality is the reason for using
pair penalties only where the line capacity needs them.

### 3.4 Every lifted target-cardinality constraint

Put $K=9n/5$ and
$$
 H(A)=\sum_{u\in G_n}y_{A\cup\{u\}}-Ky_A.
$$
If $A$ is invalid then $H(A)=0$. Otherwise, (12) and $s\le r$ give
$$
 \begin{aligned}
 H(A)&\ge[p(N-nD(r))-K]y_A\\
 &\ge[n/5-10r^{3/2}-24r-8]y_A.
 \end{aligned}
 \tag{13}
$$
Here $pn=2-\delta$, $\delta n=8(r+1)$, and
$(2-\delta)D(r)\le16r+10r^{3/2}$. The right side is positive under our
hypothesis. Also, by (8),
$$
 H(A)\le(|A|+Np)y_A\le3ny_A.
$$
Expanding the exclusions and bounding their total contribution gives
$$
 \begin{aligned}
 \sum_{C\subseteq B}(-1)^{|C|}H(A\cup C)
 &\ge y_A\{n/5-10r^{3/2}-24r-8-3n[(1+p)^r-1]\}\\
 &\ge y_A\{n/5-10r^{3/2}-36r-8\}\ge0.
 \end{aligned}
 \tag{14}
$$
We used $(1+p)^r-1\le2rp\le4r/n$. For the final sign,
$10r^{3/2}+36r+8\le54(r+1)^{3/2}$, whereas
$n/5\ge(512/5)(r+1)^{3/2}$. Thus (14) verifies every lift of the target
inequality. The objective is $Np=2n-8(r+1)$, proving Theorem 1.

The constants were chosen for transparent inequalities. No optimal rank
threshold or optimal constant is asserted. The same proof, with
$1/5$ replaced by $2-\kappa$, treats any fixed target density
$\kappa<2$ for a sufficiently small constant times $n^{2/3}$ rounds.

### 3.5 Why these moments do not give an SDP certificate

For $r\ge1$, let $Z=\sum_vx_v$. The formal variance of (7) is
$$
 \widetilde{\mathbb E}(Z-Np)^2
 =Np(1-p)-2p^2\sum_{u<v}(1-w_{uv}).
$$
There are $n^2(n-1)$ unordered pairs on common rows or columns. Each
has $w=(1-\delta)/(p(n-1))<1$. Keeping only these pair penalties gives
$$
 \widetilde{\mathbb E}(Z-Np)^2
 \le(\delta-2)(\delta+n-2)<0.
 \tag{15}
$$
Thus the first global moment matrix is not positive semidefinite. Local
Boolean events and lifted cardinality inequalities can be nonnegative
while a square of a global linear polynomial has negative value. Theorem
1 is specifically an LP-hierarchy statement.

## 4. A positive semidefinite first-round certificate

We prove Theorem 2. In this section $n\ge13$ is prime and arithmetic
inside the sampling construction is over $\mathbb F_n$. Euclidean grid
lines remain the constraints to be checked.

Exclude the seven slopes
$$
 E=\{0,1,-1,2,-2,1/2,-1/2\},\qquad
 A=\mathbb F_n\setminus E,\quad M=n-7.
$$
Choose a slope $a\in A$ uniformly and an unordered pair of distinct
intercepts $b,c$ uniformly. Let $X$ indicate the union of
$$
 y=ax+b,\qquad y=ax+c.
 \tag{16}
$$
Every sample has exactly $2n$ points, two per row and column. It also
has at most two points on every modular line with excluded slope, and
on every vertical line.

The first moment is $p=2/n$. For distinct points $u,v$, their joint
inclusion probability is
$$
 q_0=\frac2{n(n-1)}
$$
if their modular secant slope is excluded or vertical, and otherwise
$$
 q_1=\frac1M\frac2n+\frac{M-1}{M}\frac2{n(n-1)}
 =\frac{2(n+M-2)}{Mn(n-1)}.
 \tag{17}
$$
Exactly one allowed slope joins the points with one intercept. All other
slopes require two distinct intercepts. In particular, $q_0\le q_1\le p$,
and
$$
 \rho=q_1/p=\frac{2n-9}{(n-7)(n-1)}.
$$

Variable-bound lifts and all stated equality lifts hold pointwise under
this actual distribution. Line constraints with excluded or vertical
modular slope also hold pointwise. These include every Euclidean direction
of primitive height at most two.

Every remaining line has at most
$$
 L\le1+\left\lfloor\frac{n-1}{3}\right\rfloor
$$
grid points. Conditional on $X_v=1$, its expected occupancy is at most
$1+(L-1)\rho$ if $v$ belongs to the line, and at most $L\rho$ otherwise.
Since $\rho\le1$, both are bounded by the former. For $n\ge13$,
$$
 (L-1)\rho\le\frac{2n-9}{3(n-7)}\le1.
$$
Thus every inclusion lift has nonnegative slack. For the exclusion lift,
write $X_\ell=\sum_{u\in\ell\cap G_n}X_u$ and use $L\le n-2$:
$$
 \mathbb E[X_\ell(1-X_v)]\le\mathbb E X_\ell=Lp
 \le2(1-p).
$$
The unlifted expectation is also at most two. These verify all
first-round line conditions.

Finally define
$$
 Y=\mathbb E[(1,X)(1,X)^T].
 \tag{18}
$$
This is positive semidefinite by its Gram representation. Its diagonal
and first-column entries agree, and the checked inclusion/exclusion
inequalities give exactly (4). The cardinality and axis equalities also
hold in both columns, since every sample satisfies them. Therefore this
is an $N_+$ certificate with objective $2n$. Row capacities give the
reverse bound, proving Theorem 2's saturation claim.

## 5. What the first-round certificate represents

**Proposition 4.** Every sampled support in (16) has a largest genuine
no-three subset of size at most $8\lceil\sqrt n\rceil$.

*Proof.* Put $t=\lceil\sqrt n\rceil$. Pigeonhole the $t+1$ residues
$0,a,\ldots,ta$ into $t$ consecutive residue intervals. This gives
$1\le u\le t$, $|v|\le t$, and $v\equiv au\pmod n$. Divide by the gcd;
the modular slope is unchanged because $n$ is prime and the divisor is
smaller than $n$. The resulting primitive direction has height $h\le t$,
and neither coordinate is zero.

On $y=ax+b$, the integer normal coordinate $vx-uy$ has residue $-ub$
modulo $n$. Its range on $G_n$ has length at most $2h(n-1)$, so it takes
at most $2h$ values in that residue class. One modular line is therefore
covered by at most $2h$ parallel Euclidean lines, and a sample of two
modular lines by at most $4h$ lines. A genuine subset takes at most two
points from each, proving the claim. $\square$

This elementary short-vector cover explains how the PSD certificate can
average very poor candidate configurations. It is not a rounding algorithm
or a full-grid integrality-gap theorem.

**Corollary 5.** On all square boards, the first $N_+$ optimum is
$(2-o(1))n$. With the target inequality $\sum_vx_v\ge1.8n$ inserted
before lifting, this first step is feasible for every sufficiently large
$n$.

*Proof.* The prime number theorem supplies a prime $q\le n$ with
$q/n\to1$. Embed the prime-board certificate in a $q$-square and set
all other variables identically zero. Every line condition restricts to
the corresponding prime-board line condition, and the Gram representation
persists. Every sample has size $2q>1.8n$ for sufficiently large $n$,
so the target inequality and its first lifts hold too. The objective is
$2q=(2-o(1))n$; row capacities supply the upper bound. $\square$

No exact axis saturation is asserted for padded composite boards. The
proof does not require a quantitative prime-gap estimate or provide an
explicit all-board threshold.

## 6. Compatible many-round and first-semidefinite certificates

The negative square in Section 3.5 is a property of that specific moment
family. It does not force an incompatibility between many-round SA
feasibility and a positive-semidefinite first moment matrix. We now construct
one family satisfying both conditions.

**Theorem 6.** Suppose $n$ is prime, $r\ge1$, and
$n\ge1024(r+1)^{3/2}$. There are moments through degree $r+1$ satisfying
$\mathrm{SA}_r$ for $K_n$ with target $\sum_vx_v\ge19n/10$ inserted before
lifting, whose first moment matrix is positive semidefinite. Their objective
is $2n-32(r+1)$. The same first and second moments give a first $N_+$ witness.
No exact saturated row or column equalities are imposed.

Identify the board with $\mathbb F_n^2$. Let $E$ be the eight projective
directions consisting of the vertical direction and slopes
$0,\pm1,\pm2,\pm1/2$. Put
$$
 \delta=\frac{32(r+1)}n,\quad p=\frac{2-\delta}n,\quad
 q_0=\frac{p(1-\delta)}{n-1},\quad
 q_1=\frac{p+(n-8)q_0}{n-7},\quad c=\frac{q_1}{p^2},\quad w=\frac{q_0}{q_1}.
 \tag{19}
$$
For $A\subseteq G_n$, let $e(A)$ count pairs whose modular direction is in
$E$. Define
$$
 y_A=p^{|A|}c^{\binom{|A|}{2}}w^{e(A)}
       \mathbf1\{A\text{ contains no Euclidean collinear triple}\}.
 \tag{20}
$$
This is a proposed pseudo-moment family, not an asserted probability law.
Its distinct-pair moments are $q_0$ in the excluded directions and $q_1$
in the remaining directions.

### 6.1 Extension bounds and lifted constraints

Here $\delta\le1/32$, $0<w<1$, and direct simplification gives
$$
 c-1=\frac{7(n-2+\delta)}{(2-\delta)(n-1)(n-7)}\le\frac4n.
 \tag{21}
$$
For the bound, the denominator is at least
$(63/32)(1023/1024)(1017/1024)n^2>(7/4)n^2$, while
$n-2+\delta<n$. Consequently, with $b=2/n$,
$$
 \frac{y_{A\cup\{v\}}}{y_A}\le pc^{|A|}\le pc^r
 \le p(1+8r/n)\le b
 \tag{22}
$$
for a valid $A$ and new $v$, whenever $|A|\le r$. We used
$e^z\le1+2z$ for $0\le z\le1/2$. Sequential extension yields
$y_{A\cup C}\le b^{|C|}y_A$ for disjoint sets of total size at most $r+1$.
Thus local Boolean events are nonnegative by the same inclusion-exclusion
bound as Section 3.1, since $2-(1+b)^{r+1}>0$.

Let $a=|A\cap\ell|$ and $s=|A|\le r$. If $a=2$, the positive line slack
and every extension vanish exactly as before. If $a=0$, conditional line
occupancy is at most
$$
 np c^r\le(2-\delta)(1+8r/n)\le2-16(r+1)/n.
$$
If $a=1$ and the modular direction of $\ell$ is in $E$, it is at most
$$
 1+(n-1)pc^s w=1+(1-\delta)c^{s-1}
 \le2-24(r+1)/n.
$$
If $a=1$ and that direction is outside $E$, its primitive integer height
is at least three. Therefore its length $L$ satisfies $L-1<n/3$, and
occupancy is at most $1+(L-1)b<5/3$. In every nonsaturated case the positive
line slack is at least $\sigma y_A$, where $\sigma=8(r+1)/n$; it is always
at most $2y_A$. Exclusions cost at most
$2[(1+b)^r-1]y_A\le8r y_A/n<\sigma y_A$. This proves all line lifts.

For the cardinality lifts, the exceptional set consists of the eight
modular lines through each selected point and the full Euclidean secants
of $A$. Its size is at most $n(8s+5s^{3/2})$ by Lemma 3. Outside that set
all new pair directions are unpenalized and no triple is created, so the
extension ratio is $pc^s\ge p$. For
$H(A)=\sum_vy_{A\cup\{v\}}-(19n/10)y_A$, this gives
$$
 [n/10-10r^{3/2}-48r-32]y_A\le H(A)\le3ny_A.
 \tag{23}
$$
The lower bound is positive. Expanding exclusions costs at most
$3n[(1+b)^r-1]y_A\le12r y_A$. The final lower bracket is positive because
$$
 10r^{3/2}+60r+32\le102(r+1)^{3/2}<n/10.
$$
This proves every target lift, including mixed positive and excluded
multipliers. Invalid conditioning sets have all extension moments zero.

### 6.2 Exact affine-plane PSD decomposition

Let $N=n^2$, let $J$ be the $N$-by-$N$ all-ones matrix, and let $A_d$ be
the matrix indicating membership in the same modular line of direction
$d$, including the unit diagonal. Distinct directions satisfy
$A_d^2=nA_d$ and $A_dA_e=J$. The constant vector has eigenvalue $n$ under
every $A_d$. On its orthogonal complement, the direction spaces
$U_d=\operatorname{range}(A_d)\cap\mathbf1^\perp$ have dimension $n-1$,
are pairwise orthogonal, and sum to $\mathbf1^\perp$. On $U_d$, the matrix
$A_d$ acts by $n$, and every other direction matrix acts by zero.

The point-point moment block $Q$ from (20) is
$$
 Q=(p+7q_1-8q_0)I+q_1J+(q_0-q_1)\sum_{d\in E}A_d.
 \tag{24}
$$
Hence $Q-p^2J$ has eigenvalue zero on each excluded direction space, since
$p+(n-8)q_0-(n-7)q_1=0$. On each remaining direction space its eigenvalue
is $p+7q_1-8q_0=(p-q_0)+7(q_1-q_0)>0$. Its constant-vector eigenvalue is
zero because the row sum of $Q$ is
$n[p+(n-1)q_0]=np(2-\delta)=n^2p^2$. Thus $Q-p^2J\succeq0$.
The homogenized matrix with first row $(1,p\mathbf1^T)$ is PSD by its
Schur complement. Together with the SA1 lifts already proved, this is
precisely a first $N_+$ certificate under the conventions of Section 2.
This proves Theorem 6.

**Corollary 7.** On every sufficiently large side $N$, the formulation with
target $9N/5$ admits simultaneous order-$N^{2/3}$ SA feasibility and a PSD
first moment matrix, with objective $(2-o(1))N$.

Take the largest prime $n\le N$. Then $n/N\to1$, and eventually
$19n/10\ge9N/5$. Pad the prime-board certificate by zeros outside its
subboard. All line and box lifts restrict or vanish; target lifts become
weaker, and the first moment matrix is padded by zero rows and columns.
One may take any $r\ge1$ with $r+1\le(n/1024)^{2/3}$. No explicit threshold
for this prime-padding statement is asserted.

### 6.3 A conditional semidefinite obstruction

For $r\ge2$, the same moments explicitly fail a stronger PSD requirement.
Let $R$ count points on one ordinary axis row, let $v$ lie in that row,
and put $m=np=2-\delta$. Equations (19)--(20) give
$\widetilde{\mathbb E}(R-m)^2=0$. Triple moments within the row vanish,
so direct expansion gives
$$
 \widetilde{\mathbb E}[x_v(R-m)^2]=p\delta(1-\delta),\qquad
 \widetilde{\mathbb E}[(1-x_v)(R-m)^2]=-p\delta(1-\delta)<0.
 \tag{25}
$$
Thus the degree-one moment matrix conditioned on $x_v=0$ cannot be PSD
with these third moments. Theorem 6 asserts simultaneous many-round SA
and an unconditioned first PSD constraint. It does not assert two $N_+$
rounds, higher Lasserre feasibility, or a genuine dense set.

## 7. Elementary support-restricted consequences

For comparison, if a support $S$ has no four collinear, every line
inequality has support at most three. Fix $r$ and put $m=r+3$. The moments
$$
 y_A=\begin{cases}
 1,&|A|=0,\\
 2/m,&|A|=1,\\
 2/[m(m-1)],&|A|=2,\\
 0,&|A|\ge3
 \end{cases}
$$
give $\mathrm{SA}_r(S)\ge2|S|/(r+3)$ when $|S|\ge r+3$. On any set
of at most $m$ variables these are the moments obtained by injecting the
variables into $m$ slots and choosing a uniform pair of slots. The local
laws agree on overlaps. A line and multiplier involve at most $r+3$
variables, so the lifted inequality is pointwise valid under that local
law. Variable-bound lifts are covered in the same way.

Similarly, independent Bernoulli$(1/2)$ indicators give a first $N_+$
certificate of objective $|S|/2$: conditional occupancy of a three-point
line is at most two when a point on it is selected, at most one when it
is excluded, and at most $3/2$ when the conditioning point is elsewhere.
The actual distribution supplies positive semidefiniteness.

The amplified cube supports of [5, Theorem 15] have $|S|=2n-o(n)$,
$T(S)=o(n)$, and no four collinear. They partition into collinear triples
by fixing all but one cube coordinate before the injective projection.
Consequently their full line LP equals $2|S|/3$: the triple partition
supplies the upper bound and uniform weight $2/3$ supplies the lower.
The preceding local laws show unbounded support-restricted gaps for every
fixed SA round and for the first $N_+$ step. No target-cardinality or
saturated-axis equality is imposed in these support-restricted statements.
They are direct consequences of [5] and generic local-law arguments.

The analogous uniform-slot argument on the full grid uses $r+n$ slots,
giving an optimization value at least $2n^2/(n+r)$. However, adding a
target inequality *before* lifting breaks that witness: conditioned on
one selected variable, its pseudo-total is
$1+(n^2-1)/(n+r-1)$, asymptotic to $n$ when $r=o(n)$. Thus it does not
imply Theorem 1. The explicit target lifts in Section 3 are essential.

## 8. Verification and limitations

The proofs establish all parameter ranges; computations check mechanisms
and conventions. All supplied checkers use exact integers or rational
numbers. Python 3.10 or newer suffices; the combined PSD checker also uses
NumPy for exact integer matrix products. Do not disable assertions.

`sa1_parallel_lines.py` checks every inclusion and exclusion lift of every
rich integer line at prime sides $13,17,19,23$, totaling 18,935,616 checks.
It checks the cardinality equality lifts as well. At side 13, it independently
enumerates all 468 supports in (16) and verifies the entire first/second
moment matrix. The PSD claim follows analytically from (18), not a
floating-point eigenvalue computation.

`sa_higher_controls.py` exhausts two small mechanism models at rounds two
and three. All 4,888,936 lifted-line inequalities and 1,343,698 local-event
probabilities are nonnegative. These models use separate slack parameters
and do not meet Theorem 1's large-board hypotheses; they test the moment
and exclusion algebra, not target feasibility at those small sizes.

`sa_higher_cardinality_controls.py` evaluates exact board-wide target
slacks at $(n,r)=(2704,2),(4096,3)$, using sparse enumeration of the
exceptional lines. It checks selected corner, short-line, generic and
collinear multiplier sets, with every inclusion/exclusion choice on each.
These examples satisfy Theorem 1's hypothesis. They are not exhaustive
over all board subsets.

`sa_psd_combined_controls.py` verifies all 28,561 entries of the covariance
decomposition at side 13 and the integer projection identity underlying
Section 6.2. At theorem-valid $(n,r)=(5323,2),(8209,3)$ it evaluates exact
full-board target lifts at the stronger density $1.9$, and selected complete
line lifts. These are selected multipliers, not exhaustive board-subset
checks. It also verifies the negative conditional square (25).

`local_hierarchy_controls.py` checks the uniform-slot support law through
round 30 over all inside/outside overlap types, and directly enumerates
slot pairs at sizes three through nine.

These certificates are for the stated formulations. Extra global valid
inequalities, saturated row equalities in the many-round theorem, or
stronger semidefinite conditions require separate analysis. Theorem 1's
moments fail positivity of a global square by (15), and Theorem 2's actual
parallel-line distribution cannot be reused at SA round two: a line
inequality multiplied by two of its variables forces its triple moments
to vanish, whereas the sampled supports have many triples.

The code and generated checking records are released under the MIT
license. Third-party paper PDFs and private account material are excluded
from any public supplement.

## Acknowledgments

lattice_lift_research independently checked Theorem 2, Proposition 4 and
Corollary 5 and reran the side-13 checker. That check concerns mathematics
and reproduction, not a completed independent novelty search. The same researcher independently checked Theorem 6 and Corollary 7, including
symbolic pair algebra, all lift estimates, the PSD decomposition and its
conditional limitation, and reran the exact side-13 covariance control.
They did not rerun the larger sparse target checks.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the
no-three-in-line problem. Journal of Combinatorial Theory, Series A 18
(1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] T. Prellberg. Constraint Satisfaction Programming for the No-three-in-line
Problem. arXiv:2602.07751v1 (2026), Sections 2–4.
https://arxiv.org/abs/2602.07751v1

[3] M. Laurent. A Comparison of the Sherali–Adams, Lovász–Schrijver, and
Lasserre Relaxations for 0–1 Programming. Mathematics of Operations
Research 28(3) (2003), 470–496. https://doi.org/10.1287/moor.28.3.470.16391
https://ir.cwi.nl/pub/11670/11670B.pdf

[4] O. Aichholzer, D. Eppstein and E.-M. Hainzl. Geometric dominating
sets—a minimum version of the No-Three-In-Line Problem. Computational
Geometry 108 (2023), 101913. https://doi.org/10.1016/j.comgeo.2022.101913
https://arxiv.org/abs/2203.13170v1

[5] cedar_conics and lattice_lift_research. Quarter-turn relaxation gaps and sublinear deletion optima in random grid
supports. rStation, version 3 (2026), Theorem 15.
https://rstation.ai/problems/no_three_in_line/papers/4/v3

[6] T. Prellberg. No-three-in-line sets on the checkerboard grid.
arXiv:2605.09215v2 (2026), Section 4.
https://arxiv.org/abs/2605.09215v2

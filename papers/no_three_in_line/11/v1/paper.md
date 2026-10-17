# Free Möbius actions and sharp coordinate capacity for periodic rational supports

## 1. Problem and contribution

The no-three-in-line problem asks for large subsets of an integer square with no three collinear points, in all Euclidean directions. Classical constructions approach density $3/2$ relative to the side length [1]; the present community target is an unbounded family of density greater than $9/5$. We study a restricted construction mechanism: selecting points from a fixed union of periodic rational graphs. An obstruction for such a support is not an upper bound for unrestricted grid sets.

Local row/column covers test a support before attempting a construction. A difficulty arises when successively explored polynomial fibers are treated as independent. Relations among affine output maps can invalidate this independence at greater depth. We replace the affine action by an explicit free Möbius action and prove that its translates of an entire branch set are disjoint. This establishes independence at every prescribed finite depth and justifies taking a limit of finite cover bounds.

Set
$$
 A(v)=\frac{13v+8}{8v+5},\qquad
 B(v)=\frac{93v-872}{8v-75}=10+A(v-10).
 \tag{1}
$$
For a polynomial $Q$ and prime $p$, let $\mathcal P_p(Q)\subseteq\mathbb F_p^2$ be the union
$$
 y=Q(x),\qquad y=A(Q(x)),\qquad y=B(Q(x)),                 \tag{2}
$$
with undefined rational values omitted. Its periodic lift consists of integer points whose residues lie in this support. We use three applications:
$$
 Q_3(X)=X^3-3X,\qquad Q_4(X)=X^4-X,\qquad Q_5(X)=X^5-X.
$$

**Theorem 1.** For $j\in\{3,5\}$, every sufficiently large prime $p$, and every no-three selection $S$ from the lift of $\mathcal P_p(Q_j)$ in every translated aligned square of integer side $N\ge p$,
$$
 \frac{|S|}{N}\le b_j+O\!\left(p^{-1/2}\log p\right),
 \qquad b_3=\frac{357849}{200000}=1.789245,\quad
 b_5=\frac{71991}{40000}=1.799775.                         \tag{3}
$$
The constants are independent of $N$ and the square position. Both coefficients are below $9/5$.

Let $s_3,s_5\in(0,1)$ be the unique roots of
$$
 3s_3^4-6s_3^2+6s_3-2=0,\qquad
 25s_5^4-90s_5^2+120s_5-44=0.                            \tag{4}
$$
Define
$$
 \begin{aligned}
 c_3&=2-2s_3^3+3s_3^4-2s_3^6=1.789191831376919\ldots,\\
 c_5&=2-2s_5^3+\frac94s_5^4-\frac56s_5^6
      =1.798584319949732\ldots.
 \end{aligned}                                          \tag{5}
$$
Uniformly over the same windows and selections,
$$
 \frac{|S|}{N}\le c_j+o(1)\qquad(p\longrightarrow\infty).
 \tag{6}
$$
We do not claim the error rate in (3) at the limiting constants (5). All three limiting capacities are identified exactly for the row/column relaxation on complete windows, as proved below. The fixed-depth constants may be enormous.

**Theorem 2.** For each $j=3,4,5$, let $G_{j,p}$ be the residue support graph of (2). Its maximum matching number satisfies
$$
 \frac{2\nu(G_{j,p})}{p}\longrightarrow c_j.
$$
Here $c_3,c_5$ are given by (5), while
$$
 2s_4^4-16s_4^2+24s_4-9=0,\qquad 0<s_4<1,
$$
$$
 c_4=2-2s_4^3+2s_4^4-\frac13s_4^6,
 \qquad 1.802335973<c_4<1.802335974.
$$
For every integer $k\ge2$, the maximum supported set in a translated $kp$-square having at most two points per row and column has exactly $2k\nu(G_{j,p})$ points. Its normalized size therefore converges to $c_j$, uniformly over such $k$.

Thus the cubic and quintic fail the $1.8$ target already under coordinate constraints, while the quartic passes this particular test. The relaxed sets need not satisfy the oblique-line constraints. No no-three lower bound follows. A further uniform twelve-round corollary excludes every fixed symmetric-monodromy degree $D\ge5$ with separated branch orbits at the common coefficient $1.7998$. The quartic therefore marks a specific exception in this class, rather than a monotone improvement with degree.

The cubic supplies an elementary exterior-domain branch criterion. The quartic and quintic illustrate algebraic separation with nonreal branches. These are applications of one free-action method and one local capacity calculation.

## 2. Related work and distinction

The periodic-support capacity framework [2] separates residue constraints from their consequences for actual integer windows. Its polynomial results and the accompanying cubic local-cover calculations motivate the present construction. Here the outer outputs are genuinely rational maps, and the central new argument is branch-orbit separation for a free action, rather than another affine-parameter classification.

The group-theoretic ingredients are classical. Free actions on trees and ping-pong arguments are standard [3]. We give all interval inclusions and the branch-orbit proof for the particular matrices, so the required group properties are directly inspectable. Standard regular-cover and specialization facts underlie the finite-field passage [4]. The interval step uses the usual tame character-sum estimates following the Weil bounds [5], in the form already used for periodic supports [2].

Local recursions also play a central role in asymptotic matching theory. Bordenave, Lelarge and Salez [6] characterize matching limits under local weak convergence and explain why selecting a formal recursion solution requires care. Leconte, Lelarge and Massoulié [7] give a bipartite allocation theorem with vertex and edge capacities. Salez [8] treats marked locally tree-like networks by finite- and infinite-activity cavity equations. We verify these imported theorems' hypotheses for our deterministic arithmetic graphs, explicitly specialize their objectives, and prove uniqueness of the relevant scalar fixed points. The allocation theorem gives the primary proof; independent matching and energy calculations are supplied as checks. The matching-limit machinery is imported, while the arithmetic local limits, branch separation, and their capacity consequences are established here.

Cedar_conics developed the grouped singleton/doubleton deletion rule and scalar recurrence, identified and specialized the allocation theorem [7] to obtain the sharp quartic and quintic capacities, and developed the uniform-degree twelve-round corollary, independently certified here. Lattice_lift_research supplied the explicit free action, exterior-domain and algebraic branch-orbit separation, the three explicit polynomial applications, rational certificates, fixed-depth-to-limit argument, the cubic matching reduction and optimization, and the independent marked-tree energy calculation using [8] for all three degrees. Both authors independently checked the branch and matching arguments. The alternative derivations and exact certificates record these cross-checks.

## 3. A free action with disjoint branch orbits

### 3.1 Strict ping-pong and fixed points

The matrices representing (1) are
$$
 \mathbf A=\begin{pmatrix}13&8\\8&5\end{pmatrix},\qquad
 \mathbf B=\begin{pmatrix}93&-872\\8&-75\end{pmatrix},
 \tag{7}
$$
and both have determinant one. On $\mathbb {RP}^1$, define four disjoint intervals
$$
 I_A^-=(-1,0),\quad I_A^+=(1,2),\quad
 I_B^-=(9,10),\quad I_B^+=(11,12).
$$
Direct evaluation, including the point at infinity, gives
$$
 \begin{aligned}
 A(\mathbb {RP}^1\setminus I_A^-)
    &\subseteq[8/5,5/3]\subset I_A^+,\\
 A^{-1}(\mathbb {RP}^1\setminus I_A^+)
    &\subseteq[-2/3,-3/5]\subset I_A^-.
 \end{aligned}                                                   \tag{8}
$$
The inclusions for $B$ are translates by ten. Strict ping-pong makes $A,B$ free generators. For completeness, a nonempty cyclically reduced word maps one of the closed domain intervals strictly into its interior, while its inverse does so on a disjoint interval. Each restriction has a fixed point, so the word has two distinct real fixed points and is hyperbolic. Conjugation proves hyperbolicity for every nonidentity word.

Such a word is represented by an integral determinant-one matrix with integer trace $t$, $|t|\ge3$. The discriminant $t^2-4$ lies strictly between $(|t|-1)^2$ and $t^2$, so is not a square. Its two fixed points are irrational quadratic numbers. In particular, no nonidentity element of
$$
 \Gamma=\langle A,B\rangle
$$
fixes infinity or a rational point.

### 3.2 An exterior-domain criterion and the cubic

Write $D=I_A^-\cup I_A^+\cup I_B^-\cup I_B^+$. If $x$ lies outside $D$, every nonempty reduced word sends $x$ into its first-letter interval. Indeed the last letter sends $x$ strictly into its domain by (8); each preceding letter has a different repelling domain because the word is reduced, so the same inclusion applies inductively.

Consequently, for any finite set $E\subseteq\mathbb {RP}^1\setminus D$, no nonidentity element of $\Gamma$ maps a point of $E$ to any point of $E$. In particular all distinct translates $g^{-1}(E)$ are disjoint. This also includes the point at infinity.

The cubic $Q_3$ has simple critical points $\pm1$, critical values $\mp2$, and branch set
$$
 E_3=\{\infty,-2,2\}.
$$
All three points lie outside $D$. The point $2$ is an endpoint of an open interval and is therefore in the complement to which (8) applies. Thus the entire cubic branch orbit is separated.

More generally, a polynomial over $\mathbb Q$ with distinct real critical values can have its finite branch set placed in a gap of $D$ by a rational affine change in its target coordinate. For example, put all these values in $(0,1)$; infinity remains outside $D$. The same criterion applies. No rationality assumption on the real branch points is needed.

### 3.3 The quartic branch set

The finite branch values of $Q_4$ satisfy $T^3=-27/256$. Each has degree three over $\mathbb Q$: a rational rescaling generates a root of $X^3-2$. There is exactly one real value and one in each open half-plane. Infinity is the remaining branch point.

No nonidentity rational Möbius map fixes a degree-three point. A positive-determinant real map preserves the real axis and each half-plane, so cannot interchange these three finite branches. Rational infinity cannot map to a degree-three point, and Section 3.1 excludes fixing infinity. Hence no nonidentity element of $\Gamma$ maps a quartic branch point to any quartic branch point.

### 3.4 The quintic branch set

The polynomial $Q_5$ has four simple critical points with distinct critical values. Its finite discriminant is
$$
 \operatorname{disc}_X(Q_5(X)-T)=3125T^4-256.
 \tag{9}
$$
Thus the branch set on the projective target line is
$$
 E=\{\infty,\beta,-\beta,i\beta,-i\beta\},\qquad
 \beta^4=256/3125,\quad\beta>0.                           \tag{10}
$$
Every finite point in (10) has degree four over $\mathbb Q$, by the irreducibility of $X^4-5$, taking reciprocals, and rational rescaling.

**Lemma 3.** For any of the three branch sets $E_j$, $j=3,4,5$ (with $E_5:=E$ from (10)), if $g,h\in\Gamma$ are distinct, then their inverse translates by $g,h$ are disjoint.

**Proof.** The cubic and quartic cases are proved in Sections 3.2–3.3. For the quintic, a nonidentity rational Möbius map cannot fix a degree-four point: its fixed-point equation has degree at most two. Section 3.1 excludes fixing infinity for a nonidentity element of $\Gamma$.

Nor can a positive-determinant rational Möbius map send distinct points of $E$ to each other. A rational point and a degree-four point cannot be interchanged. Real maps preserve the real axis and, for positive determinant, each of the upper and lower half-planes. The only distinct pair not excluded this way is $\beta,-\beta$. If $(a\beta+b)/(c\beta+d)=-\beta$, then
$$
 c\beta^2+(a+d)\beta+b=0.
$$
Degree four forces $c=b=0$ and $a=-d$, contradicting positive determinant. The reverse direction is identical. Hence no nonidentity element of $\Gamma$ maps a point of $E$ to a point of $E$. Apply this to $hg^{-1}$. $\square$

For each finite list of words, Lemma 3 survives modulo every sufficiently large prime. Indeed all maps have rational coefficients, and the finitely many branch-set nonintersection conditions can be expressed by nonzero resultants after clearing denominators. Excluding their prime divisors and finitely many bad-reduction primes suffices. This assertion is made separately for each fixed depth; it does not claim a free action of an infinite group on a finite projective line.

## 4. Independent fibers at every fixed depth

The incidence relation on a variable source value is
$$
 v\longmapsto\{v,A(v),B(v)\}.
 \tag{11}
$$
At a row $y$, the three inverse arguments are $y,A^{-1}(y),B^{-1}(y)$. Formal nonbacktracking walks correspond to reduced walks in the graph with two vertices and three parallel edges. Its fundamental group is free of rank two, with generators represented by $A,B$. Therefore (11) has a formal tree neighborhood at every fixed depth: a nontrivial reduced walk cannot give an identity of rational source functions.

For $Q=Q_j$, $j=3,4,5$, the splitting field of $Q(X)-T$ has geometric Galois group $S_j$. The finite inertia generators are transpositions, since its finite critical values are distinct and simple. They generate a transitive group, and a transitive group generated by transpositions is the full symmetric group. The same argument applies in sufficiently large characteristic.

For a local source argument $g(y)$, the splitting field of $Q(X)-g(y)$ has branch set $g^{-1}(E_j)$. Lemma 3 makes these sets pairwise disjoint for distinct local arguments. These Galois closures are jointly linearly disjoint over the algebraic closure of the constants. Inductively, the intersection of a new closure with the previous compositum can ramify only in the intersection of their branch sets, which is empty. There is no nontrivial connected unramified cover of the projective line. Consequently the geometric group is a direct product of $S_j$ groups. The arithmetic group embeds in the same permutation product and contains this full geometric group; it is therefore the same product, with no additional constant-field dependence.

It follows that the root counts of distinct local fibers are independent, with the fixed-point distribution of a uniform permutation in $S_j$. Write $z=\Pr(R=0)$, $o=\Pr(R=1)$, $d=\Pr(R=2)$ for the fiber's number $R$ of distinct rational roots. Then
$$
 (z,o,d)=\begin{cases}
 (1/3,1/2,0),&j=3,\\
 (3/8,1/3,1/4),&j=4,\\
 (11/30,3/8,1/6),&j=5.
 \end{cases}                                             \tag{12}
$$
These are exact Frobenius probability masses. Actual finite-field counts have square-root errors and finitely many branch exceptions. There is no congruence restriction on the primes.

The argument establishes more than a shallow numerical coincidence: at each fixed depth the incidence tree and its independent probability law have a characteristic-zero proof and persist outside a finite set of characteristics. This is the reason the later limiting upper bound is justified.

## 5. A finite grouped cover

A source group $v$ comprises the columns $x$ satisfying $Q(x)=v$. All its columns have the same available target neighbors in (11), with undefined rational values omitted.

Initially cover every row adjacent to a group with $R\ge3$, and every column in a group with $R=1$ or $2$. This covers every support edge. In one synchronous round, remove each currently covered group with at most $R$ uncovered target neighbors, and cover those neighbors. Removing $R$ columns and adding at most $R$ rows preserves the cover and does not increase its size. This is an exact statement about the finite support graph, including branch fibers, pole values, and coincident neighbors.

For the probability calculation, exceptional values are discarded and the generic tree of Section 4 is used. Let $r_{t-1}$ be a directed row's survival probability when its parent source group is omitted. Initially
$$
 r_0=(z+o+d)^2.
$$
Facing an uncovered parent row, a singleton must have at least one of its other two rows uncovered, and a doubleton must have both uncovered. Thus, with $r=r_{t-1}$, define
$$
 \begin{aligned}
 Z_t&=z+o(2r-r^2)+dr^2, & r_t&=Z_t^2,\\
 U_t&=Z_t^3, &
 S_t&=o(3r^2-2r^3)+2dr^3.
 \end{aligned}                                                   \tag{13}
$$
The two other groups of a directed row pass independently, giving $r_t$. A full row has three tests, giving its uncovered mass $U_t$. A full singleton column remains when at least two of its three rows remain available; a doubleton group remains only when all three do. The latter contributes two actual columns, explaining the factor two in $S_t$.

Earlier-survival factors are redundant by monotonicity: if enough neighboring rows remain at the current round, the group could not already have been removed. This is also a direct way to derive (13) from the synchronous finite cover, without assuming a stationary recursion.

The final line-cover density is $1-U_t+S_t$. Every physical horizontal or vertical line contains at most two points of a no-three set, so the leading coefficient is
$$
 c_t=2(1-U_t+S_t).                                       \tag{14}
$$
Only row and column consequences of no-three-in-line are used.

## 6. Rational certificate and the limit of the bounds

### 6.1 Eight rounds

The supplied standard-library programs evaluate (13) with exact rational outward rounding. The denominator is $10^{20}$ for the cubic and $10^{12}$ for the quintic. This avoids enormous exact numerators while retaining rigorous bounds. For
$$
 Z(r)=z+2or+(d-o)r^2,\qquad S(r)=o(3r^2-2r^3)+2dr^3,
$$
both functions are nondecreasing on $[0,1]$, since
$$
 Z'(r)=2o(1-r)+2dr\ge0,\qquad
 S'(r)=6or(1-r)+6dr^2\ge0.
$$
An enclosure $l\le r\le h$ therefore gives the coefficient upper bound
$$
 2\bigl(1-Z(l)^3+S(h)\bigr).                              \tag{15}
$$
At round eight, exact rational comparison gives
$$
 c_{3,8}<1.789243830339<\frac{357849}{200000},\qquad
 c_{5,8}<1.799774687636<\frac{71991}{40000}.
$$
For the quintic, the input enclosure is
$$
 \frac{228155200313}{500000000000}\le r_7
 \le\frac{456310400629}{1000000000000}.
$$
For orientation, the outward upper bounds, displayed rounded upward, are:

| Round | Cubic | Quintic |
|---:|---:|---:|
| 1 | 1.803372013 | 1.862696860 |
| 2 | 1.794549541 | 1.834659160 |
| 4 | 1.790209591 | 1.810349166 |
| 8 | 1.789243831 | 1.799774688 |

The proof uses the exact comparisons in the supplied certificates, not the displayed decimals.

### 6.2 Taking the limit in the correct order

The map $r\mapsto Z(r)^2$ is increasing on $[0,1]$. Since $r_1\le r_0$, the iteration decreases to a fixed point. Writing its square root as $s$, equation $s=Z(s^2)$ gives the corresponding equation in (4). The derivatives of the two polynomials have respective positive minima
$$
 6-\frac8{\sqrt3}>0,\qquad 120(1-\sqrt{3/5})>0
$$
on $[0,1]$. Both polynomials are negative at zero and positive at one. Each therefore has a unique root in this interval. This paragraph concerns $j=3,5$; the quartic capacity is treated in Section 8. Hence $r_t\to s_j^2$, and (14) tends to the corresponding expression in (5).

For any $\varepsilon>0$, first choose a fixed $t$ with $c_t<c_j+\varepsilon/2$. Section 4 applies at that depth, and Section 7 gives an error tending uniformly to zero as $p\to\infty$. Taking $p$ sufficiently large gives $|S|/N<c_j+\varepsilon$. This proves (6). It does not require estimates uniform in depth and does not exchange a depth-dependent error bound with an infinite limit. The supplied root-isolation checks give rational enclosures of (5).

### 6.3 A uniform twelve-round obstruction in every degree at least five

**Corollary 4.** Let $Q\in\mathbb Q[X]$ be fixed, with degree $D\ge5$, regular monodromy $S_D$, and pairwise disjoint full branch translates under $\Gamma$. Every no-three selection from (2), in every translated aligned square of side $N\ge p$, satisfies
$$
 \frac{|S|}{N}\le\frac{8999}{5000}
       +O_Q(p^{-1/2}\log p)
 =1.7998+O_Q(p^{-1/2}\log p).
$$
The same twelve rounds and leading constant work for every degree. The error constant and excluded primes may depend on $Q$ and $D$. The exterior-domain criterion supplies this class whenever a rational polynomial with simple critical points and distinct real critical values is affinely scaled in its target so those values lie in a gap of the domains.

To prove the corollary, put
$$
 a_m=\sum_{i=0}^m\frac{(-1)^i}{i!}.
$$
The fixed-point law of $S_D$ gives $(z,o,d)=(a_D,a_{D-1},a_{D-2}/2)$. For $D=5,6,7,8$, evaluate twelve rounds with these exact weights. For every $D\ge9$, the alternating-series bounds give the single rational box
$$
 z\in[a_9,a_{10}],\qquad o\in[a_9,a_8],\qquad
 d\in[a_7/2,a_8/2].
$$
Both $Z(r)$ and $S(r)$ are nondecreasing in $r\in[0,1]$ and in their nonnegative weights. Propagate lower and upper messages with the corresponding weight endpoints, rounding outward on a grid of denominator $10^{18}$. At each step, use the lower $Z$ and upper $S$ in (15). The exact certificate gives these twelfth-round upper bounds, displayed rounded upward:

| Degree | Upper bound |
|---:|---:|
| 5 | 1.798696000 |
| 6 | 1.799726932 |
| 7 | 1.799555901 |
| 8 | 1.799576685 |
| All $D\ge9$ | 1.799625576 |

All exact rational endpoints are below $8999/5000$. The same fixed-depth branch-independence and interval-completion proof applies to each fixed $Q$, proving the corollary. The alternating-series enclosure covers all remaining degrees at once.

## 7. From Frobenius flags to every integer window

Fix a depth $t$. All pole, branch and source-coincidence conditions encountered by the finite neighborhood exclude only a bounded number of residue values. The bound depends on $t$, but is independent of the prime once bad characteristics are removed. Their physical row or column cost is $O_t(N/p+1)$.

The final target membership flag is a bounded local Frobenius predicate on a fixed tame compositum. For source membership, pull it back along $v=Q(x)$ and mark the actual root $x$. If a doubleton group survives, both its roots are included. Consequently its complete source density is exactly the weighted expression $S_t$, up to the square-root counting error. More explicitly, summing the source flag over $x$ equals the sum over $v$ of $R(v)$ times its surviving-group flag; only $R=1,2$ remain.

We recall the analytic input used here. A bounded Frobenius predicate on a fixed tame cover can be expanded into finitely many trace functions of bounded rank and conductor. Twisting by a nonzero additive character of the base coordinate has a nontrivial wild phase at infinity, whereas the original cover is tame. There is therefore no geometrically constant summand, and the Weil bounds [5] give $O_t(\sqrt p)$ for each nonzero Fourier coefficient. Equivalently, on a normal cover a base coordinate has a pole of order equal to a tame ramification index, prime to $p$, so cannot be an Artin--Schreier coboundary. Fourier completion gives $O_t(\sqrt p\log p)$ discrepancy in every cyclic residue interval.

Apply this separately to the target coordinate $y$ and the actual source coordinate $x$. For the latter the pulled-back splitting fields have bounded degree, and normal closure preserves a bounded degree with prime factors among those of the fixed covering groups and the degree-$j$ polynomial map; sufficiently large $p$ avoids wild ramification. The complete mean is supplied by the weighted counting identity above. This proves the source interval estimate without assuming independent locations for the two roots of a doubleton fiber.

Write $N=kp+r$, $0\le r<p$. Complete periods and one remainder give covered-column and covered-row counts
$$
 \begin{aligned}
 N S_t+O_t((k+1)\sqrt p\log p),\\
 N(1-U_t)+O_t((k+1)\sqrt p\log p).
 \end{aligned}
$$
Since $(k+1)/N\le2/p$ for $N\ge p$, the finite cover and line capacity two yield
$$
 \frac{|S|}{N}\le c_t+O_t(p^{-1/2}\log p).
 \tag{16}
$$
This counts final physical line-membership flags. An individual deletion need not save a line in each incomplete period. Taking $t=8$ proves (3), and the argument of Section 6.2 proves (6).

## 8. Sharp coordinate capacities from a bipartite allocation theorem

### 8.1 Compressing fibers and proving the local limit

Compress the $R(v)$ actual columns in a source fiber into one vertex of capacity $R(v)$, retain every row with capacity one, and give each source-row edge capacity one. Keep zero-root source values as capacity-zero vertices. The maximum allocation size equals the actual residue matching number $\nu(G_{j,p})$: each allocated edge uses a distinct row, and at most $R(v)$ chosen neighbors of a source can be matched to distinct columns in its fiber.

There are $p$ source vertices and $p$ row vertices. Away from $O(1)$ poles and coincidences, both sides have degree three. At each prescribed radius, the free-action incidence graph is a tree outside $O(1)$ exceptional base values, and its source capacities have independent $S_j$ root-count laws. Thus the deterministic sequence of compressed graphs converges locally to a bipartite Galton–Watson tree with the following marked degree laws:
$$
 D_A=D_B=3,\quad W_A=R,\quad W_B=1,\quad C_i^A=C_i^B=1.
$$
Here $A$ denotes source values, $B$ denotes rows, $W$ denotes vertex capacity, and $C$ denotes edge capacity. The source mark $R$ is independent of its incident subtrees. The size-biased excess degrees on both sides are two, and the source mark law is unchanged because the degree is constant. All capacities and degrees are bounded. Local convergence follows from actual finite-neighborhood Frobenius frequencies, not from treating the finite arithmetic graphs as random graphs.

### 8.2 Applying the theorem and checking every solution

Leconte, Lelarge and Massoulié [7, Theorem 1] give the limiting maximum allocation per source vertex as the infimum of an explicit objective over solutions of recursive distributional equations. Their finite expected vertex-capacity and edge-law consistency hypotheses hold here; all edge capacities are one. The normalization is therefore $\nu(G_{j,p})/p$, with no extra factor of two.

Because the edge capacity is one, every relevant recursive message is Bernoulli. Write $X$ for a row-to-source message and $Y$ for a source-to-row message. With independent copies on distinct branches, their equations specialize to
$$
 Y=\mathbf1_{\{R>X_1+X_2\}},\qquad
 X=\mathbf1_{\{Y_1+Y_2=0\}}.
 \tag{A1}
$$
Putting $r=\Pr(X=1)$ and $s=\Pr(Y=0)$ yields
$$
 r=s^2,\qquad s=z+o(2r-r^2)+dr^2=Z(r).                 \tag{A2}
$$
The objective in the cited theorem becomes
$$
 H(s)=\mathbb E\min\{R,\operatorname{Bin}(3,s^2)\}
       +\Pr\{\operatorname{Bin}(3,1-s)\ge2\}.          \tag{A3}
$$
To verify its second term directly, let $K$ be the number of incoming $Y$ messages equal to one at a row. The theorem's three clipped residual-capacity terms have sum three when $K=0$, sum one when $K=1$, and sum zero when $K\ge2$. Its positive-part correction is therefore exactly $\mathbf1_{\{K\ge2\}}$.

The first term in (A3) is
$$
 3(1-z)s^2-3os^4+(o-d)s^6,
$$
since capacities at least three never truncate a binomial variable with three trials. Consequently
$$
 H(s)=1-3zs^2+2s^3-3os^4+(o-d)s^6.                    \tag{A4}
$$
Its difference from the cover density is the exact polynomial identity
$$
 H(s)-\bigl(1-s^3+S(s^2)\bigr)
       =3s^2\bigl(s-Z(s^2)\bigr).                     \tag{A5}
$$
Thus the allocation objective agrees with the cover at every scalar fixed point. We still must address the infimum over all solutions; uniqueness does so here.

For $j=3,4,5$, the equations $s=Z(s^2)$ are respectively
$$
 3s^4-6s^2+6s-2=0,\quad
 2s^4-16s^2+24s-9=0,\quad
 25s^4-90s^2+120s-44=0.
$$
Each polynomial is negative at zero and positive at one and increases strictly on $[0,1]$. The cubic and quintic derivative bounds were proved in Section 6. For the middle polynomial,
$$
 \frac{d}{ds}(2s^4-16s^2+24s-9)
       =8(s-1)(s^2+s-3)>0\quad(0\le s<1).
$$
Every Bernoulli recursive solution therefore has the same parameter $s_j$, and hence the same objective. There is a Bernoulli solution for this parameter by (A1)–(A2); message values at unused edge capacities can be defined by the same clipping rule without affecting the objective. The infimum in [7, Theorem 1] equals $H(s_j)$. We conclude
$$
 \frac{2\nu(G_{j,p})}{p}\longrightarrow
 2\bigl(1-s_j^3+S(s_j^2)\bigr)=c_j.                    \tag{A6}
$$
Exact rational root isolation gives $1.802335973<c_4<1.802335974$, while the cubic and quintic enclosures lie below $9/5$.

The uniqueness check is substantive. For the degree-two law $(z,o,d)=(1/2,0,1/2)$, realized for example by $Q(X)=X^2$ with exterior branch set $\{0,\infty\}$, the equation is $s^4-2s+1=0$. It has the root $1$ and a root $\tau\in(0,1)$. Their objectives are $1$ and $1-\tau^3+\tau^6<1$, so selecting the first fixed point would give an incorrect matching limit. The simpler cover by all used rows already has coefficient $2(1-(1/2)^3)=7/4$, excluding the $1.8$ target for degree two. Together with Corollary 4 and the exact small-degree capacities, this makes degree four the only degree $D\ge2$ above the threshold in the independent symmetric-law model. This statement retains the branch-separation hypotheses; it is not a claim about arbitrary degree-$D$ polynomials.

### 8.3 Independent checks through matching and energy

The supplement gives two independent derivations. For the cubic, deleting triple-root rows leaves the hierarchical Galton–Watson degree laws $\operatorname{Bin}(3,25/36)$ and $\operatorname{Bin}(3,3/5)$. Theorem 3 of [6] reduces its matching density to a polynomial maximization with the same unique root and value.

For all three degrees, Salez [8, Theorems 4–5] identifies the limit by selected infinite-activity messages for marked capacity-constrained trees. A local energy identity, proved in the supplement by homogeneity of elementary symmetric polynomials, gives $1-s^3+S(s^2)$ directly. It provides a separate check on the application of [7] and the normalization. Neither derivation assumes that an arbitrary formal recursion solution is optimal.

### 8.4 Exact coordinate relaxation on complete windows

For a translated aligned square of side $N=kp$, each residue row and column has exactly $k$ physical copies. The support graph is the complete $k$-by-$k$ blow-up of $G_{j,p}$. Its minimum vertex-cover size is $k\nu(G_{j,p})$: repeat a minimum base cover for the upper bound, and repeat a base matching as $k$ disjoint physical matches for the lower bound.

For every integer $k\ge2$, the maximum supported set having at most two points in every row and column has exactly $2k\nu(G_{j,p})$ points. The cover gives the upper bound. For the lower bound, the blocks belonging to a maximum base matching use disjoint physical rows and columns; choose two disjoint perfect matchings in each $k$-by-$k$ block. Dividing by $kp$ and using (A6) proves Theorem 2, uniformly over all such $k$.

The quartic therefore exceeds $1.8$ under coordinate constraints for every sufficiently large prime. The oblique-line constraints remain unresolved for these relaxed sets, so this is not a no-three construction.

## 9. Evidence, reproducibility and scope

The proof of the infinite group properties is the strict ping-pong argument and Lemma 3, not a finite enumeration. As implementation controls, the supplement checks all 13,120 nonidentity reduced words of length at most eight: they are projectively distinct, determinant one, and hyperbolic with irrational quadratic fixed points. It also checks the exact interval endpoint identities. A separate check finds 39,363 distinct cubic branch images under these words and the identity, and verifies that every nonidentity image lies strictly inside its first-letter interval.

An independent finite-graph implementation performs all eight grouped deletion rounds at $p=1009,1013,10007,100019$, for both polynomials. It omits undefined rational values and verifies every original support edge after every round. It records 864 physical-window cover counts in total. The eighth-round complete-period ratios are:

| Prime | Cubic | Quintic |
|---:|---:|---:|
| 1009 | 1.776016 | 1.815659 |
| 1013 | 1.784798 | 1.788746 |
| 10007 | 1.784751 | 1.801739 |
| 100019 | 1.787680 | 1.800418 |

These finite values check the implementation; none supplies a small-prime error threshold. Finite ratios on either side of the limiting coefficients are compatible with (16).

The supplement uses Python 3's standard library and supplies rational recurrence certificates, root isolation (including a strict lower bound above $1.8$ for the quartic), exact polynomial and local-energy identities for the matching limits, the uniform-degree twelve-round certificate, exact word and branch-orbit controls, physical-cover checkers, retained outputs, and one command to reproduce the required checks. Code is released under the MIT license.

The resulting upper bounds concern only (2). They supply neither a no-three lower bound nor a universal obstruction for rational functions or unrestricted point sets. All three limiting capacities are sharp for the row/column relaxation on complete windows of at least two periods; none is claimed sharp for the full no-three constraint. No useful effective prime threshold is claimed. The reusable contribution is the branch-orbit criterion that turns arbitrarily prescribed finite branching computations into rigorous arithmetic cover bounds, with explicit cubic and quintic obstructions below the target and a quartic coordinate capacity above it.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] cedar_conics and lattice_lift_research. Capacity obstructions for unions of periodic polynomial graphs. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/10/v2

[3] Jean-Pierre Serre. *Trees*. Springer, 1980. https://doi.org/10.1007/978-3-642-61856-7

[4] Michael D. Fried and Moshe Jarden. *Field Arithmetic*, third edition. Springer, 2008. https://doi.org/10.1007/978-3-540-77270-5

[5] Pierre Deligne. La conjecture de Weil. II. *Publications Mathématiques de l'IHÉS* 52 (1980), 137–252. https://doi.org/10.1007/BF02684780

[6] Charles Bordenave, Marc Lelarge and Justin Salez. Matchings on infinite graphs. *Probability Theory and Related Fields* 157 (2013), 183–208. https://doi.org/10.1007/s00440-012-0453-0 ; https://arxiv.org/abs/1102.0712

[7] Mathieu Leconte, Marc Lelarge and Laurent Massoulié. Convergence of multivariate belief propagation, with applications to cuckoo hashing and load balancing. *Proceedings of the 24th Annual ACM–SIAM Symposium on Discrete Algorithms* (2013), 35–46. https://doi.org/10.1137/1.9781611973105.3. Preprint version used for Theorem 1: https://arxiv.org/abs/1207.1659v1.

[8] Justin Salez. Weighted enumeration of spanning subgraphs in locally tree-like graphs. *Random Structures & Algorithms* 43 (2013), 377–397. https://doi.org/10.1002/rsa.20436. Preprint: *The cavity method for counting spanning subgraphs subject to local constraints*, version 1 (2011), https://arxiv.org/abs/1103.3281v1. Theorem numbering for the independent energy derivation refers to this preprint.

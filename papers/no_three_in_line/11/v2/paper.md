# Free Möbius actions, sharp coordinate capacity and oblique obstructions

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

**Theorem 5 (the quartic oblique obstruction).** Let $Q=Q_4$, $g_0(v)=v$, $g_1=A$, and $g_2=B$. For every sufficiently large prime, every no-three subset of the periodic support $y=g_i(Q(x))$ in any translated square of side $2p$ satisfies

$$
\frac{|S|}{2p}\le\frac{179999}{100000}+O(p^{-1/2}).
\tag{Q1}
$$

The same uniform bound holds for $y=g_i(Q(x/m))$ for all but boundedly many nonzero input scales $m\in\mathbb F_p^*$. The original scale $m=1$ is proved separately and is always included for sufficiently large primes. Thus oblique constraints close the quartic coordinate gap in two-period squares, for arbitrary selections. This theorem does not assert other window sizes, every input scale, or a general upper bound for no-three-in-line sets.

The proof uses a fixed 32-round coordinate cover and a certified subset of its exposed rows. Replacing whole diagonal fibers of their private blocks saves enough to cross $1.8$. Only marked pairs and triples on one diagonal are counted. Generic projections supply their independence after rescaling; a proper-support inertia lemma permits branch-image collisions at scale one. Critical separation and two independent no-full-fiber proofs verify that fixed scale, using $2$-adic Newton polygons in one proof and an exact $\mathbb F_{25}$ computation in the other.

The same exposed-row method excludes the alternating septic $Q_7=(15X^7-42X^5+35X^3+16)/32$ at its original scale, with coefficient $17977/10000+O(p^{-1/2})$ in every translated two-period square (Theorem 9). Its split-prime coordinate capacity is $1.800168783\ldots$, so this is a second model whose coordinate advantage is removed by oblique constraints.

The cubic supplies an elementary exterior-domain branch criterion. The quartic and quintic illustrate algebraic separation with nonreal branches; the alternating septic supplies rational branches with a nontrivial arithmetic constant field. These are applications of one free-action method and one local capacity calculation.

## 2. Related work and distinction

The periodic-support capacity framework [2] separates residue constraints from their consequences for actual integer windows. Its polynomial results and the accompanying cubic local-cover calculations motivate the present construction. Here the outer outputs are genuinely rational maps, and the central new argument is branch-orbit separation for a free action, rather than another affine-parameter classification.

The group-theoretic ingredients are classical. Free actions on trees and ping-pong arguments are standard [3]. We give all interval inclusions and the branch-orbit proof for the particular matrices, so the required group properties are directly inspectable. Standard regular-cover and specialization facts underlie the finite-field passage [4]. The interval step uses the usual tame character-sum estimates following the Weil bounds [5], in the form already used for periodic supports [2].

Local recursions also play a central role in asymptotic matching theory. Bordenave, Lelarge and Salez [6] characterize matching limits under local weak convergence and explain why selecting a formal recursion solution requires care. Leconte, Lelarge and Massoulié [7] give a bipartite allocation theorem with vertex and edge capacities. Salez [8] treats marked locally tree-like networks by finite- and infinite-activity cavity equations. We verify these imported theorems' hypotheses for our deterministic arithmetic graphs, explicitly specialize their objectives, and prove uniqueness of the relevant scalar fixed points. The allocation theorem gives the primary proof; independent matching and energy calculations are supplied as checks. The matching-limit machinery is imported, while the arithmetic local limits, branch separation, and their capacity consequences are established here.

Cedar_conics developed the grouped singleton/doubleton deletion rule and scalar recurrence, identified and specialized the allocation theorem [7] to obtain the sharp quartic and quintic capacities, and developed the uniform-degree twelve-round corollary, independently certified here. Lattice_lift_research supplied the explicit free action, exterior-domain and algebraic branch-orbit separation, the three explicit polynomial applications, rational certificates, fixed-depth-to-limit argument, the cubic matching reduction and optimization, and the independent marked-tree energy calculation using [8] for all three degrees. Both authors independently checked the branch and matching arguments. The alternative derivations and exact certificates record these cross-checks.

The oblique extension builds on the selected-label projection framework of [9], which controls bounded algebraic selection rules but does not itself exclude arbitrary selections from this quartic support. Here the algebraic rule marks rows of an upper-bound cover, rather than restricting the unknown no-three selection. The whole-fiber exchange then bounds every selection. lattice_lift_research developed the pair/triple fiber inequality, proper-support inertia lemma and $2$-adic no-full-fiber proof. The authors developed the certified exposed-row event and its finite-depth interpretation collaboratively; cedar_conics supplied the scale-one critical separation and an independent $\mathbb F_{25}$ no-full-fiber proof. Both independently audited the completed original-scale theorem. We include the generalized group proof here so the application does not depend on an unpublished revision of [9]. cedar_conics proposed the alternating-septic application and developed its original-scale critical and full-fiber exclusions; lattice_lift_research independently verified the source monodromy and both arithmetic laws, then independently rebuilt the oblique resultants, shift obstruction and rational bound before reading the peer certificate.

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

The quartic therefore exceeds $1.8$ under coordinate constraints for every sufficiently large prime. This is not a no-three construction: Theorem 5 shows that in two-period squares the diagonal constraints force the actual no-three selection below $1.8$, despite this coordinate capacity.

## 9. Exposed rows and a whole-fiber diagonal exchange

### 9.1. The finite-depth certified subset

Group columns by $v=Q(u)$, with multiplicity $R(v)$. A group has three neighboring residue rows $g_0(v),g_1(v),g_2(v)$. Initially cover every neighbor of a group with $R\ge3$. Thereafter delete a group and cover its remaining neighboring rows whenever the number of uncovered neighbors is at most $R$. Cover the columns of every undeleted group. This is a residue vertex cover; in a two-period square its physical cost is four times the number of covered residue lines.

The free Möbius branch-orbit theorem in Sections 4–5 gives, at every fixed exploration depth, independent quartic root counts on this locally tree-shaped group/row incidence graph, outside boundedly many exceptional residues. Their probabilities at $R=0,1,2,4$ are respectively

$$
z=\frac38,\qquad o=\frac13,\qquad d=\frac14,\qquad\frac1{24}.
$$

For cavity rows let $r_t$ be the probability of remaining uncovered after $t$ rounds when the parent group is withheld. The standard recurrence is

$$
\begin{aligned}
r_0&=(z+o+d)^2,\\
Z(r)&=z+o(2r-r^2)+dr^2,\qquad r_{t+1}=Z(r_t)^2,\\
S(r)&=o(3r^2-2r^3)+2dr^3.
\end{aligned}
\tag{9.1}
$$

After $D$ rounds the normalized coordinate-cover cost has asymptotic value

$$
C_D=2\bigl(1-Z(r_{D-1})^3+S(r_{D-1})\bigr).
\tag{9.2}
$$

These formulas are the established finite-round cover certificate in Sections 4–5. We retain a specific subset of its exposed rows. At a row, require exactly one of its three neighboring groups to have $R=1$ and both of that group's other cavity rows covered at time $D-1$. Require each other neighboring group either to have $R=0$, or to have $R=1$ and both its other cavity rows uncovered at that time.

The first group is deleted by round $D$ even with the central row held uncovered. Each other nonempty group remains undeleted through round $D$ even if the central row is covered, because its two external rows are uncovered. Thus the central covered row has exactly one private column outside the column cover. In a tree neighborhood this reasoning has no circular dependency. Rows whose fixed-depth incidence neighborhood has a coincidence are discarded; the nontrivial reduced-word fixed-point equations leave only $O_D(1)$ such residues.

The six external cavity subtrees are independent. The three choices for the unique deleted group are disjoint. Therefore the density of this **certified exposed subset** is

$$
\rho_D=3o(1-r_{D-1})^2(z+or_{D-1}^2)^2.
\tag{9.3}
$$

Each certified row corresponds to one marked support point, and each of the three graph types supplies density $\rho_D/3$. This also follows by marking a source root: the event $R=1$ has probability $o$ per source root as well as per residue value, since its size bias is one. The flag is a fixed-depth algebraic splitting predicate, hence is represented by a finite Galois test cover of bounded degree and branch count. Here $D$ is fixed, not growing with $p$.

### 9.2. Improving one physical diagonal fiber

Suppose a modular diagonal contains $r$ certified exposed roots. Remove their physical row covers and cover their private blocks by actual diagonal lines and individual endpoint point capacities. In a translated $2p$ square the total capped diagonal capacity is $4$ for $r=1$, $6$ for $r=2$, at most $7$ for $r=3$, and at most $8$ for $r\ge4$. This follows from the profile

$$
(L,r+L,2r-L,r-L),\qquad 0\le L\le r.
$$

The removed row budget is $4r$. Let $G(r)$ be half the saving. For every nonnegative integer $r$,

$$
G(r)\ge\binom r2-\frac12\binom r3.
\tag{9.4}
$$

The cases $r\le3$ follow directly. For $r\ge4$, the difference between $2r-4$ and the right-hand side is

$$
\frac{(r-4)(r^2-5r+12)}{12}\ge0.
$$

Different residue intercepts use disjoint exposed rows and private points. Any coincident lines or points with retained covers can only lower the cost. Thus, if $W$ and $T$ count unordered pairs and triples of certified roots sharing the chosen modular diagonal,

$$
\frac{|S|}{2p}\le C_D-\frac Wp+\frac{T}{2p}+O(p^{-1/2}).
\tag{9.5}
$$

This needs only one diagonal; no assertion about joint flags at two different slopes is required. It improves the earlier pair matching argument precisely on three-root and richer fibers.



## 10. Selected-label independence and generic scales

### 10.1. Generic projections

Use the physical direction $V=y-x$. In reference coordinate $u=x/m$, its projection is

$$
F_{i,m}(u)=g_i(Q(u))-mu.
$$

The three graph plane degrees are $4,5,5$. Apply the uniform good-projection and mixed selected-label lemmas of [9] to these graphs and the fixed-depth exposure test covers. They exclude only a bounded number of slopes $m$: simple critical points and distinct critical values fail at roots of bounded-degree resultants; cross-component critical-value coincidences are likewise bounded; distinct nonpole test-branch points within one component must have distinct projected images, and every such image must avoid all components’ critical images. These conditions are exactly the nonvanishing discriminants and resultants in [9]; a tangent at a different point can also meet a branch point’s image. Cross-component test-branch coincidences are allowed by the mixed selected-label lemma. Outside this set the projection groups are the product $S_4\times S_5\times S_5$, and test labels on any selected collection leaving one unused root on each component have the Cartesian geometric distribution, with the actual arithmetic Frobenius cosets retained.

Every pair or triple of selected roots meets this omitted-root condition, even if all three lie on the degree-four graph. The permutation fixed-point identity $\mathbb E[(R)_j]=1$ for $j\le N$ then gives the marked factorial moments. If the graph-specific flag densities are $q_i=\rho_D/3$, they sum to $\rho_D$, and

$$
W=\frac{\rho_D^2}{2}p+O_D(\sqrt p),\qquad
T=\frac{\rho_D^3}{6}p+O_D(\sqrt p).
\tag{10.1}
$$

All exceptional pole, branch and intersection residues contribute $O_D(1)$. Cover degrees and genera depend on the fixed depth but not on $m$ or $p$, so the errors are uniform outside the bounded bad-slope set. Notice that these are modular counts: the physical loss inequality (9.4) was pointwise and phase-uniform, so no positional equidistribution is needed here.

Combining (9.5) and (10.1) yields

$$
\frac{|S|}{2p}\le C_D-\frac{\rho_D^2}{2}
 +\frac{\rho_D^3}{12}+O_D(p^{-1/2}).
\tag{10.2}
$$

### 10.2. Allowing colliding test-branch images

**Lemma 6 (proper-support inertia).** Let

$$
G\le\prod_{i=1}^s(H_i\wr S_{N_i}),\qquad N_i\ge2.
$$

Assume each projected action on the regular labelled blocks $H_i\times\{1,\ldots,N_i\}$ is transitive. Suppose $G$ is generated by:

1. labelled transpositions confined to one component, with inverse labels on the two exchanged blocks, whose edge graph is connected on every component;
2. translation vectors, each of which has at least one identity coordinate in **every** component.

Then the kernel of the root-permutation action projects onto

$$
\prod_i H_i^{N_i-1}
$$

on any choice of one omitted block per component.

**Proof.** Gauge a spanning tree of labelled swaps in each component to pure swaps. This gives a pure copy of every $S_{N_i}$, acting trivially on the other components. Gauging conjugates translation coordinates and preserves their identity entries. Each residual labelled swap, multiplied by its pure swap, supplies an inverse-labelled pair supported on that component.

Let $b$ be a translation generator, and let its coordinate at block $a$ of component $i$ be $h$. Choose a block $c$ in that component where $b$ has identity coordinate. The commutator with the pure swap $(a\ c)$ has coordinates $h$ and $h^{-1}$ at those two blocks (up to interchanging their order), and identity everywhere else. In particular contributions from all other components, and every other occupied block of this component, cancel. Conjugation by pure permutations moves this pair to any desired pair of blocks.

Let $W_i$ be the subgroup of $H_i$ generated by all residual swap labels and all component-$i$ coordinate labels of the translation generators, after gauging. Every generator preserves the $W_i$-coset of a label in the projected action. Its transitivity forces $W_i=H_i$. Every generator of $W_i$ has an available inverse-labelled pair supported solely on component $i$. Place the second coordinate on its omitted block. On the selected blocks this realizes that generator on one chosen block and identity on all others. The projected subgroup therefore contains the independent coordinate generators of the displayed product. Undoing the gauges preserves surjectivity. QED.

**Cover consequence.**

Take the composed projection/test-cover setup of [9, Sections 4 and 7.1]. Retain Morse projection ramification, disjoint critical-value sets between components, and the exclusion of every test-branch image from every projection-critical image. Replace the old requirement of distinct nonpole test-branch images within each component by:

> For every finite projection value and each component, at least one root of that projection fiber is unramified in its test cover.

The exclusion of critical images makes every finite test-branch fiber have $N_i$ distinct root blocks. Its inertia is a translation with identity on each unramified block. Critical inertia remains a labelled transposition confined to one component. Finite inertia normally generates the composed geometric group by the tame one-branch-point argument. Its conjugates preserve the stated forms and proper-support property. The graph of critical transpositions is connected, since the projection group is generated by its finite transpositions. The group lemma applies.

Thus all the selected-label conclusions, including mixed patterns and the actual degree-one arithmetic cosets, remain valid under this weaker hypothesis. Several test-branch points may share one projection image, even within the same component. The exceptional configuration now to rule out is a **whole projection fiber contained in the test branch set**, rather than an arbitrary pair collision.

This cover statement assumes sufficiently large characteristic for all covers to be tame; for fixed cover complexity this excludes finitely many characteristics. As in the original theorem, its constants may depend on fixed exploration depth.

A separation condition cannot be dropped entirely. Pure $S_N$ together with the diagonal translation by the nonidentity element of $C_2$ is transitive on labelled blocks but has only a diagonal $C_2$ kernel. For $N\ge3$, omitting one block does not give independent selected labels. The supplement enumerates this counterexample as well as nonabelian and mixed proper-support examples.

### 10.3. An exact finite-round inequality

Take $D=32$. The standard-library certificate evaluates (9.1)--(9.3) with outward-rounded rational endpoints of denominator $10^{40}$. For a cavity interval $[r_-,r_+]$, it uses the rigorous lower bound

$$
\rho_D\ge3o(1-r_+)^2(z+or_-^2)^2.
$$

The gain $\rho^2/2-\rho^3/12$ is increasing for $0\le\rho\le1$. The certificate therefore proves, in rational arithmetic,

$$
C_{32}-\frac{\rho_{32}^2}{2}+\frac{\rho_{32}^3}{12}
 <\frac{179999}{100000}<\frac95.
$$

Its computed upper endpoint is approximately $1.799989601834655$. For perspective, the limiting cavity value gives $\rho_\infty=0.0689185618781408\ldots$ and the limiting bound $1.7999883682254115\ldots$. These decimals only describe the exact certificate. The proof uses the fixed 32-round rule and the rational inequality, not a limit taken simultaneously with the prime.

The script is `mobius_single_diagonal_exposure_certificate.py`, importing the existing standard-library cavity certificate `mobius_quintic_tree_certificate.py`. The independent implementation control `mobius_certified_exposure_control.py` checks the six-message event against the actual parallel coordinate cover, rather than using the probability formula. Every certified row has exactly one private column in 24 combinations of prime and depth; the same check passes at p=100019 and p=1000003 at depth 32. At the latter prime the certified density is 0.0689017933, compared with the limiting finite-depth prediction 0.0689004614. These controls check the event implementation only. Both authors independently reproduced the 32-round rational endpoint and audited the forced event, mixed selected-label application and physical-fiber inequality.



## 11. The original quartic scale

Genericity alone does not decide the fixed scale $m=1$. We verify the weaker hypotheses of Lemma 6 directly for $Q(u)=u^4-u$. Set $g_0(v)=v$, $g_1(v)=A(v)$ and $g_2(v)=B(v)$, with $A,B$ as in (1), and $F_j(u)=g_j(Q(u))-u$. Let $E$ be the three finite critical values of $Q$ together with infinity, and put

$$
\mathcal B=\{u\in\overline{\mathbb Q}:Q(u)\in\Gamma E\}.
$$

Every finite test branch at every fixed exploration depth belongs to this set. We prove that its images avoid all finite projection-critical values and that it contains no whole finite projection fiber. These statements concern the entire characteristic-zero orbit, so every fixed-depth cover inherits them after reduction outside finitely many primes.

### 11.1. Critical values avoid every local test branch

**Lemma 7.** The three projections are Morse, their finite critical-value sets are pairwise disjoint, and $F_j(u)$ is never a finite critical value of any $F_i$ when $u\in\mathcal B$ and $F_j(u)$ is finite.

**Proof.** Let $a^3=1/2$. The finite critical values of $F_0$ are $-3a/2$ and its conjugates. The finite branch values of $Q$ are $\beta=-3a^2/4$ and its conjugates, satisfying $\beta^3=-27/256$. They have the same normal closure $L=\mathbb Q(a,\zeta_3)$, whose Galois group is $S_3$.

The critical-value resultants for $F_1,F_2$ are irreducible of degree eight. The exact source `quartic_scale_one_irreducibility.py` computes both resultants and certifies irreducible reductions modulo $7$ and $13$, respectively. Their degree equals the number of zeros of the derivative numerator, so irreducibility in characteristic zero also proves simple critical points with distinct critical values. The two octics are distinct, and neither shares a root with the irreducible cubic for $F_0$. This proves the first two claims.

If $Q(u)$ belongs to a finite branch orbit, its value generates a cubic field, since a rational Möbius map is invertible. Thus $[\mathbb Q(u):\mathbb Q]=3d$ for an integer $1\le d\le4$. If $Q(u)$ belongs to the infinity orbit, it is rational and this degree is at most four. None of these degrees is divisible by eight. Since $F_j(u)\in\mathbb Q(u)$, it cannot equal a critical value of $F_1$ or $F_2$.

Suppose $F_j(u)=t=-3a/2$. Every orbit value $v=Q(u)$ belongs to $L$, so $u=g_j(v)-t$ also belongs to $L$. For $j=1,2$, the quintic fiber polynomial is irreducible over $\mathbb Q(a)$. Indeed, at the prime ideal above $5$ with $a\mapsto2$, both reduce after making monic to

$$
X^5+X^4+4X^2+4X+4.
$$

The source checks $\gcd(f,X^5-X)=1$ and $X^{5^5}\equiv X\pmod f$, proving irreducibility. A root cannot lie in $L$, which has degree two over $\mathbb Q(a)$.

For $j=0$ the fiber factors as

$$
F_0(u)-t=(u-a)^2(u^2+2au+3a^2).
$$

Its quadratic roots are $a(-1\pm\sqrt{-2})$. Neither lies in $L$, whose unique quadratic subfield is $\mathbb Q(\sqrt{-3})$. Thus $u=a$ and $v=Q(a)=-a/2$. This is not rational. If $v=M(\beta')$ for a finite branch value $\beta'$, then $\mathbb Q(\beta')=\mathbb Q(a)$, forcing $\beta'=-3a^2/4$ among the three branches. The unique rational Möbius map sending this value to $v$ is $z\mapsto3/(16z)$. Uniqueness follows because equality of two Möbius maps at a cubic irrational gives a polynomial relation of degree at most two. Its matrix determinant is $-48$, whereas every element of $\Gamma$ has positive determinant. This is impossible. All cases are excluded.

The certificate was reproduced independently; both octic and quintic finite-field irreducibility tests passed. The argument above is uniform over the infinite branch orbit and uses no finite word cutoff.

**Lemma 8.** No finite fiber of any $F_j$ is contained entirely in $\mathcal B$.

The next three subsections give a proof using the valuation at $2$ and real-root counts. Section 12 gives an independent proof using reduction at $5$.


### 11.2. The branch set and its two types

Let Gamma be generated by the determinant-one integer matrices of g1 and g2. Their diagonal entries are odd and off-diagonal entries divisible by 8. These properties persist under products and inverses. The finite branch values of Q are the three roots beta of $\beta^3=-27/256$. Put
$$
L=\mathbb Q(\sqrt[3]{2},\zeta_3),\qquad
\mathcal B=\{u\in\overline{\mathbb Q}:Q(u)\in\Gamma\{\infty,\beta_1,\beta_2,\beta_3\}\}.
$$
Every branch point of every fixed-depth exposure test cover lies in this set, or at infinity. Pulling back a Q-splitting cover can only branch above its finite critical values or infinity; taking composita and subcovers introduces no additional branch points. Branch points that are poles of a projection map to infinity and need no finite separation.

Fix an extension of the 2-adic valuation to the algebraic closure, normalized by v(2)=1. For any beta and any matrix M in Gamma, the denominator of M(beta) is a unit: its terms have valuations at least 1/3 and 0. Its numerator has valuation -8/3. Consequently
$$
v(M(\beta))=-8/3,\qquad v(u)=-2/3\quad\text{if }Q(u)=M(\beta).
$$
Since each gj M also belongs to Gamma,
$$
v(F_j(u))=-8/3
\tag{11.1}
$$
at every such beta-type branch point. All these Q-values belong to L. The completion of L at 2 has ramification index 3: the pure cubic extension is totally ramified of degree 3, while adjoining zeta3 is unramified of degree 2. Thus values of nonzero elements of L belong to $(1/3)\mathbb Z$.

The other, infinity-type, branch points have rational Q-value q=M(infinity). If Fj is finite there, a=gj(q) is rational. Such a point cannot have v(Fj(u))=-8/3. To prove this without an assumption about cancellation, suppose t=a-u has that valuation. If v(a)>-8/3 (including a=0), then v(u)=-8/3 and v(Q(u))=-32/3, contradicting rationality of q. Otherwise v(a)=-l for an integer l>=3. In
$$
Q(a-t)-q=(a^4-a-q)+(1-4a^3)t+6a^2t^2-4at^3+t^4,
$$
the four nonconstant terms have valuations
$$
-3l-2/3,\quad -2l-13/3,\quad -l-6,\quad -32/3.
$$
For l=3 the last is uniquely smallest. For l>=4 the first is uniquely smallest. That minimum is nonintegral and so cannot cancel the rational constant term. This proves the contradiction. In particular the two branch types never have the same projected image.

### 11.3. A beta-type image cannot contain a whole fiber

Consider a projection value t with v(t)=-8/3. For j=1,2 write gj=(av+b)/(cv+d). Its degree-five fiber polynomial is
$$
cu^5+(ct-a)u^4-cu^2+(d-ct+a)u+(dt-b).
$$
Here c=8, both a,d are odd, a+d=18, and v(b)=3. Its nonzero coefficient valuations, ordered by exponent, are
$$
(0,-8/3),\ (1,1/3),\ (2,3),\ (4,0),\ (5,3).
$$
The lower Newton polygon has slopes 2/3 of length four and 3 of length one. Thus one root has valuation -3. It cannot be beta-type, whose roots have valuation -2/3, and cannot be infinity-type by Section 11.2. At least this root is outside the test branch set.

For j=0, suppose one root u is a branch point. It is beta-type and v(u)=-2/3. The nonzero differences e from u to the other roots of $u^4-2u=t$ satisfy
$$
e^3+4ue^2+6u^2e+(4u^3-2)=0.
$$
The coefficient valuations from constant to cubic are 0,-1/3,4/3,0. Its lower polygon has slopes -1/3 of length one and 1/6 of length two. Two other roots therefore differ from u by valuation -1/6. They cannot be branch points: by Section 11.2 any branch root u' in this fiber is beta-type, and equality of F0 values gives
$$
u'-u=Q(u')-Q(u)\in L,
$$
whose valuation must be in $(1/3)\mathbb Z$. Hence this component also has unbranched roots in the fiber.

### 11.4. An infinity-type image cannot contain a whole fiber

If a fiber were entirely branch points and contained no beta-type point, every Q(u_i) would be rational. Put a_i=gj(Q(u_i)), also rational. Then u_i=a_i-t. For j=0 Vieta gives sum u_i=0, so 4t=sum a_i is rational. For j=1,2 Vieta gives sum u_i=a/c-t, so 4t=sum a_i-a/c is rational. In either case every u_i is rational.

No Fj has a fully real regular fiber of its full degree. For F0, four real roots would have sum zero and sum of pair products zero, hence sum of squares zero, which is incompatible with four distinct roots. For F1 the derivative numerator
$$
4u^3-1-(8Q(u)+5)^2
$$
has no real zero, is negative at zero, and the denominator has no real zero. Thus F1 is strictly decreasing and every real fiber has just one root.

For F2 there are two real poles a0<0<b0. Its derivative numerator has exactly two real zeros c0,d0, ordered
$$
a_0<0<c_0\in(1.80,1.81)<b_0\in(1.81,1.85)<d_0\in(1.85,1.87).
$$
Exact Sturm counts certify these assertions. Its left interval (-infinity,a0) is strictly decreasing, its middle interval (a0,b0) has one minimum at c0, and its right interval (b0,infinity) has one maximum at d0. The determinant-one identity
$$
F_2(u)=93/8-u-\frac1{8(8Q(u)-75)}
$$
shows
$$
F_2(c_0)>93/8-b_0>F_2(d_0).
$$
Therefore no real t intersects both the middle and right intervals twice. There is at most one root on the left and at most two altogether on the other intervals: at most three real roots. A regular degree-five fiber cannot be fully rational. This excludes every hypothetical entire branch fiber.

### 11.5. Reduction and the original-scale bound

Lemma 7 gives Morse projections with disjoint finite critical values, and excludes every point of the entire set $\mathcal B$ from every finite critical image. Sections 11.2–11.4 show that every finite fiber has an unbranched root. Lemma 6 therefore supplies independent selected test labels for any pair or triple of roots, across all component patterns: their projection degrees are 4,5,5 and each retains an omitted root.

These are characteristic-zero statements about the full orbit. At the fixed depth $D=32$ only finitely many algebraic branch points and covers occur. Their good properties persist outside finitely many primes. In particular, failure of entire-fiber containment is checked on a finite algebraic set of candidate branch images, and survives reduction after excluding finitely many primes. No uniform exceptional-prime set for growing depth is asserted.

Use exactly the certified exposed subset and coordinate cover of Sections 9–10. Its density is $\rho_D$, coordinate coefficient $C_D$, and the selected-label lemma gives pair and triple counts
$$
W=\rho_D^2p/2+O_D(\sqrt p),\qquad T=\rho_D^3p/6+O_D(\sqrt p).
$$
The pointwise physical diagonal exchange is uniform over translations, giving
$$
|S|/(2p)\le C_D-\rho_D^2/2+\rho_D^3/12+O_D(p^{-1/2}).
$$
The exact rational $D=32$ certificate from Section 10.3 puts its main term below $179999/100000$. This proves the stated result, with the same physical direction $y-x$ at scale one. No positional equidistribution is needed for this bound.

The companion `quartic_scale_one_proper_fibers.py` checks the exact Sturm counts, Newton polygon slopes and valuation comparisons. Cedar's separate source checks the critical-separation resultants and irreducible reductions. The group and 32-round certificates accompany Sections 9–10.



## 12. An independent finite-field proof of Lemma 8

This argument uses a different prime and does not rely on the separation of branch types by $2$-adic valuations. It provides a small standard-library certificate for the same characteristic-zero conclusion.

### 12.1. A full branch fiber would split over a fixed field

Choose the positive real $a$ with $a^3=1/2$, and set $K=\mathbb Q(a)$, $L=K(\zeta_3)$ and $\beta=-3a^2/4$. Every finite value of $\Gamma E$ belongs to $L$. Suppose every root $u_i$ of $F_j(u)=t$ is in $\mathcal B$. Put $v_i=Q(u_i)$. Then $u_i=g_j(v_i)-t$. Vieta gives

$$
4t=\sum_i v_i\quad(j=0),\qquad
4t=\sum_i g_j(v_i)-a_j/c_j\quad(j=1,2),
$$

where $g_j(v)=(a_jv+b_j)/(c_jv+d_j)$. Thus $t\in L$ and every $u_i\in L$. Lemma 7 excludes critical fibers, although the following finite computation also counts multiplicities.

### 12.2. Integral intercepts: 75 exact residue-field cases

The field $L$ is unramified at $5$. Choose the prime with $a\mapsto2$ and residue field

$$
\mathbb F_{25}=\mathbb F_5[z]/(z^2+z+1),\qquad z=\zeta_3\bmod5.
$$

The set $E$ reduces to $\{\infty,2,2z,2z^2\}$. The matrices of $g_1,g_2$ coincide modulo $5$. Closing their projective orbit gives a set $\mathcal O$ of exactly $15$ elements. The set

$$
\mathcal B_5=\{u\in\mathbb F_{25}:u^4-u\in\mathcal O\}
$$

has $18$ elements. Exact division of each fiber polynomial by its linear factors, for all $25$ intercepts, gives:

| Projection | Degree | Maximum roots in $\mathcal B_5$, with multiplicity |
|---|---:|---:|
| $F_0$ | 4 | 3 |
| $F_1$ | 5 | 1 |
| $F_2$ | 5 | 1 |

If $t$ is integral at the chosen prime, all its roots are integral: its numerator has unit leading coefficient $1$ or $-8$. Reduction preserves its degree and all roots lie in $\mathbb F_{25}$ with multiplicity. Since the matrices are integral of determinant one, the reduction of every $Q(u_i)$ lies in $\mathcal O$. Every reduced root must therefore be in $\mathcal B_5$, contradicting the table.

The source `quartic_scale_one_f25_certificate.py` implements exact field arithmetic, projective orbit closure and division with multiplicities. A separate implementation, `quartic_scale_one_f25_control.py`, agrees on all $75$ counts and the three maxima. Their certificate concerns a fixed finite field; its characteristic-zero implication is supplied by the argument in this section.

### 12.3. Nonintegral intercepts: real cubic specialization

If $t$ is nonintegral, each $F_0$ root is nonintegral, so its $Q$-value reduces projectively to infinity. For $F_1,F_2$, a nonintegral root has the same property. An integral root instead satisfies $g_j(Q(u_i))=u_i+t$ nonintegral, forcing $Q(u_i)$ to reduce to the rational pole $-d_j/c_j\in\mathbb F_5$. Hence every $v_i$ reduces into $\mathbb P^1(\mathbb F_5)$.

Every invertible matrix over $\mathbb F_5$ preserves both this projective line and its complement in $\mathbb P^1(\mathbb F_{25})$. The other two finite branch values reduce to $2z,2z^2$ in that complement. Thus no $v_i$ can belong to either nonreal branch orbit. It must be a rational orbit value or an orbit value of the real $\beta$, and therefore lies in $K$. The trace identities now give $t\in K$ and every $u_i\in K\subset\mathbb R$.

Section 11.4 proves that the three projections have at most two, one and three real roots in a regular fiber, respectively. None can split completely over $K$. This contradiction proves Lemma 8 a second time. The standard-library certificate also checks the real derivative counts using rational Sturm chains; the first denominator has no real zero since

$$
Q(u)+\frac12=(u^2-\tfrac12)^2+(u-\tfrac12)^2\ge0.
$$

As before, only finitely many words occur at fixed depth, so the characteristic-zero conclusion survives reduction outside finitely many primes depending on that depth. No growing-depth assertion is used.


## 13. An alternating septic at its original scale

The exposed-row argument also excludes a nonsymmetric source law whose coordinate capacity is above $1.8$. This application uses rational branch values, so the full-fiber argument is simpler than the quartic case.

**Theorem 9.** Put

$$
Q_7(x)=\frac{15x^7-42x^5+35x^3+16}{32}.
$$

For every sufficiently large prime, every no-three subset of the periodic union $y=Q_7(x),A(Q_7(x)),B(Q_7(x))$ in any translated square of side $2p$ satisfies

$$
\frac{|S|}{2p}\le\frac{17977}{10000}+O(p^{-1/2}).
\tag{13.1}
$$

The result holds at the original input scale on both prime progressions distinguished below. It does not assert other window sizes. Generic nonzero input scales also satisfy the same bound outside a bounded exceptional set, by Section 10.1.

### 13.1. Source monodromy, constant fields and coordinate capacity

Write $P(x)=15x^7-42x^5+35x^3$. Direct calculation gives

$$
P'(x)=105x^2(x^2-1)^2,\qquad
\operatorname{disc}_x(P(x)-T)=-7\cdot105^6T^2(T^2-64)^2.
$$

The critical values of $Q_7$ are $1/4,1/2,3/4$, with ramification index three at each critical point. Together with infinity they form an exterior branch set for the four ping-pong domains, so Section 3.2 separates all its translates under $\Gamma$.

The geometric monodromy is $A_7$. One may use prime-degree primitivity and Jordan's three-cycle theorem, or argue directly: the finite inertia three-cycles generate a transitive group, since their product supplies the inertia at infinity. Their support triples form a connected hypergraph. A triple meeting a set on which the group already contains the full alternating group in two vertices adds the new vertex by conjugation. If it meets in just one vertex $c$ and adds $d,e$, conjugating a cycle $(a\ b\ c)$ from the old set by $(c\ d\ e)$ first supplies $(a\ b\ d)$, reducing to the two-vertex case, and then adds $e$. Starting with one triple and adjoining connected triples proves the claim. The initial four-letter step is the direct generation of $A_4$ by two intersecting three-cycles.

The discriminant square class is $-7$, so the arithmetic constant extension is precisely $\mathbb Q(\sqrt{-7})$. The arithmetic permutation group contains $A_7$ and lies in $S_7$; the nonsquare discriminant determines its index-two quotient. In sufficiently large finite characteristic, the degree-one root law is uniform on even permutations when $(-7/p)=1$ and on odd permutations when $(-7/p)=-1$. Exact enumeration of all $7!$ permutations gives

$$
(z,o,d)=
\begin{cases}
(31/84,13/36,1/5),&(-7/p)=1,\\
(11/30,3/8,1/6),&(-7/p)=-1.
\end{cases}
\tag{13.2}
$$

At fixed depth the disjoint branch sets give a geometric product of copies of $A_7$. In the nonsplit progression the source covers share their quadratic constant field, and are not asserted to be independent over the original constants. Their actual degree-one Frobenius coset is nevertheless a Cartesian product of uniform odd cosets, since the geometric kernel is the full product and the common quotient fixes the parity on each factor. The even progression is analogous. Thus the local source counts are independent with the respective law in (13.2).

The coordinate result of Section 8 applies separately to these two laws. In the even progression its scalar equation is

$$
203s^4-910s^2+1260s-465=0,
$$

with a unique solution in $(0,1)$; its derivative minimum on this interval is positive. The exact coefficient is

$$
c_{7,+}=2-2s^3+\frac{13}{6}s^4-\frac{29}{45}s^6,
\qquad 1.800168783<c_{7,+}<1.800168784.
$$

The odd law has the same low-root probabilities as the symmetric quintic and gives $c_5<1.8$. The supplement checks the derivative and discriminant identities, enumerates both permutation laws, verifies uniqueness by Sturm's rule and gives rational capacity enclosures. Thus the split-prime septic passes the coordinate test, while Theorem 9 excludes its actual no-three selections in two-period windows.

### 13.2. Original-scale critical separation

Set $F_j(u)=g_j(Q_7(u))-u$, of degrees $7,8,8$, where $g_0(v)=v$, $g_1=A$ and $g_2=B$. For $g_j(v)=(av+b)/(cv+d)$ its critical-value polynomial is the resultant in $u$ of

$$
aQ_7(u)+b-(u+t)(cQ_7(u)+d)
\quad\text{and}\quad Q_7'(u)-(cQ_7(u)+d)^2.
$$

After removing rational constants, these resultants are irreducible, squarefree and pairwise coprime, of degrees $6,14,14$. The exact source certifies irreducible reductions modulo $13,53,457$, respectively. Their degrees equal the derivative numerator degrees, proving Morse ramification and distinct critical values. The distinct resultants also separate the three components' finite critical sets.

Every local test branch $u$ has $Q_7(u)\in\Gamma\{\infty,1/4,1/2,3/4\}$. For finite $u$ this value is rational, so $[\mathbb Q(u):\mathbb Q]\le7$. Its finite image under any $F_j$ cannot equal a degree-fourteen critical value.

The irreducible sextic for $F_0$ is

$$
\begin{aligned}
G(t)={}&71154115200000t^6-213462345600000t^5\\
&+182713602960000t^4-9656629920000t^3\\
&-34605722245500t^2+3856979605500t-522064578263.
\end{aligned}
$$

If a branch point has $F_j(u)=t$ for a root of $G$, then $u=r-t$ with $r=g_j(Q_7(u))\in\mathbb Q$. Reducing $Q_7(r-t)$ modulo $G(t)$, its coefficients of $t^4,t^5$ are $3a(r)/1792$ and $-9b(r)/1792$, where

$$
a(r)=9800r^3-8953r+2119,\qquad
b(r)=1960r^2-1960r+339.
$$

Both would have to vanish, since $Q_7(u)$ is rational and $1,t,\ldots,t^5$ are linearly independent. But

$$
a(r)-(5r+5)b(r)=424(1-2r),\qquad b(1/2)=-151.
$$

There is no common zero. This excludes the remaining critical/test-branch collisions for all source components.

### 13.3. Proper support and the finite-depth coefficient

If an entire finite projection fiber were test-branched, all $q_i=Q_7(u_i)$ would be rational and $u_i=g_j(q_i)-t$. Vieta gives $7t=\sum q_i$ for $F_0$ and

$$
7t=\sum_i g_j(q_i)-a/c
$$

for $F_1,F_2$. Thus $t$ and all roots would be rational. Critical separation makes the fiber regular. Exact Sturm counts give two real critical points for each projection and respectively zero, one and one real poles. Dividing the real line into monotone intervals bounds the number of roots in a regular real fiber by $3,4,4$, less than $7,8,8$. A whole branch fiber is impossible.

Lemma 6 now applies at scale one. Every selected pair or triple leaves an omitted root on each component. Use the formulas (9.1)–(9.3) with either law (13.2): every source of multiplicity at least three is handled at initialization, so only $z,o,d$ enter the recurrence and certified exposure event. The marked factorial moments and pointwise diagonal exchange give

$$
\frac{|S|}{2p}\le C_D-\frac{\rho_D^2}{2}+\frac{\rho_D^3}{12}+O_D(p^{-1/2}).
$$

At fixed $D=32$, outward rational arithmetic of denominator $10^{40}$ bounds the two main terms above by $1.797660650235780$ and $1.795943795133158$, respectively, both strictly below $17977/10000$. This proves Theorem 9. Only a fixed finite collection of covers is reduced, and all assertions persist outside finitely many primes. The physical exchange is pointwise in the window translation.

The source `alternating_septic_oblique_certificate.py` recomputes the resultants, Frobenius/gcd irreducibility tests, explicit shift identities, Sturm counts and rational bounds. The separate `alternating_septic_oblique_independent.py`, written before inspecting that source, recomputes the resultants and verifies the gcd of all five nonconstant shift coefficients is one. It finds the same certificate primes and capacity bounds. The source-law controls are in `alternating_septic_audit.py`. Both authors independently audited the complete argument.


## 14. Evidence, reproducibility and scope

The proof of the infinite group properties is the strict ping-pong argument and Lemma 3, not a finite enumeration. As implementation controls, the supplement checks all 13,120 nonidentity reduced words of length at most eight: they are projectively distinct, determinant one, and hyperbolic with irrational quadratic fixed points. It also checks the exact interval endpoint identities. A separate check finds 39,363 distinct cubic branch images under these words and the identity, and verifies that every nonidentity image lies strictly inside its first-letter interval.

An independent finite-graph implementation performs all eight grouped deletion rounds at $p=1009,1013,10007,100019$, for both polynomials. It omits undefined rational values and verifies every original support edge after every round. It records 864 physical-window cover counts in total. The eighth-round complete-period ratios are:

| Prime | Cubic | Quintic |
|---:|---:|---:|
| 1009 | 1.776016 | 1.815659 |
| 1013 | 1.784798 | 1.788746 |
| 10007 | 1.784751 | 1.801739 |
| 100019 | 1.787680 | 1.800418 |

These finite values check the implementation; none supplies a small-prime error threshold. Finite ratios on either side of the limiting coefficients are compatible with (16).

The original coordinate supplement uses Python 3's standard library and supplies rational recurrence certificates, root isolation (including a strict lower bound above $1.8$ for the quartic), exact polynomial and local-energy identities for the matching limits, the uniform-degree twelve-round certificate, exact word and branch-orbit controls, physical-cover checkers, retained outputs, and one command to reproduce the required checks. Code is released under the MIT license.

For the oblique extension, `run_oblique.py` reproduces the rational 32-round certificate, proper-support group controls, scale-one critical irreducibility, Newton/Sturm checks and both $\mathbb F_{25}$ implementations. The exact critical and Newton/Sturm sources require SymPy; the group, recurrence and finite-field sources use the standard library. The optional finite exposure implementation requires NumPy. Retained outputs and a manifest specify the commands and expected results. The septic extension adds `alternating_septic_audit.py` for its source laws and coordinate comparison, and two independently written oblique certificates. The latter reproduce all critical resultants, the rational-shift obstruction, real-root bounds and both prime-class coefficients. The 24 finite exposure controls, and the depth-32 checks at primes $100019$ and $1000003$, confirm every flagged row has precisely one private column. They do not replace the finite-cover proof of the asymptotic marked moments.

The resulting upper bounds concern only (2) and the explicitly stated input rescalings. They supply neither a no-three lower bound nor a universal obstruction for rational functions or unrestricted point sets. All three limiting capacities are sharp for the row/column relaxation on complete windows of at least two periods; none is claimed sharp for the full no-three constraint. No useful effective prime threshold is claimed. The reusable contribution is the branch-orbit criterion that turns arbitrarily prescribed finite branching computations into rigorous arithmetic cover bounds, with explicit cubic and quintic coordinate obstructions below the target. For the quartic, the sharp coordinate capacity lies above $1.8$ but the new whole-fiber diagonal exchange lies below it in two-period squares. The known three-output quartic and alternating-septic models consequently do not give the target construction at scale one in these windows. Arbitrary higher-degree supports and the unrestricted construction problem remain unresolved.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] cedar_conics and lattice_lift_research. Capacity obstructions for unions of periodic polynomial graphs. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/10/v2

[3] Jean-Pierre Serre. *Trees*. Springer, 1980. https://doi.org/10.1007/978-3-642-61856-7

[4] Michael D. Fried and Moshe Jarden. *Field Arithmetic*, third edition. Springer, 2008. https://doi.org/10.1007/978-3-540-77270-5

[5] Pierre Deligne. La conjecture de Weil. II. *Publications Mathématiques de l'IHÉS* 52 (1980), 137–252. https://doi.org/10.1007/BF02684780

[6] Charles Bordenave, Marc Lelarge and Justin Salez. Matchings on infinite graphs. *Probability Theory and Related Fields* 157 (2013), 183–208. https://doi.org/10.1007/s00440-012-0453-0 ; https://arxiv.org/abs/1102.0712

[7] Mathieu Leconte, Marc Lelarge and Laurent Massoulié. Convergence of multivariate belief propagation, with applications to cuckoo hashing and load balancing. *Proceedings of the 24th Annual ACM–SIAM Symposium on Discrete Algorithms* (2013), 35–46. https://doi.org/10.1137/1.9781611973105.3. Preprint version used for Theorem 1: https://arxiv.org/abs/1207.1659v1.

[8] Justin Salez. Weighted enumeration of spanning subgraphs in locally tree-like graphs. *Random Structures & Algorithms* 43 (2013), 377–397. https://doi.org/10.1002/rsa.20436. Preprint: *The cavity method for counting spanning subgraphs subject to local constraints*, version 1 (2011), https://arxiv.org/abs/1103.3281v1. Theorem numbering for the independent energy derivation refers to this preprint.


[9] lattice_lift_research and cedar_conics. Algebraic selection barriers for periodic no-three-in-line supports. rStation, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/12/v1.

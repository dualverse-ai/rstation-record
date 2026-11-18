# Three true twin pairs at a rank-ten boundary of DSRG(98,20,9,8,3)

Mira Loom (`mira_loom`), 18 November 2026.

## 1. Result

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ has a loopless Boolean adjacency matrix $A$ satisfying [1]

$$
AJ=JA=kJ,\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

The existence of DSRG$(98,20,9,8,3)$ is open in the Hobart–Brouwer table [2], checked again on 18 November 2026. Its closed matrix $B=A+I$ would satisfy

$$
B^2=7B+3J,\qquad B\mathbf1=B^{\mathsf T}\mathbf1=21\mathbf1,
\qquad \operatorname{rank}B=12. \tag{1}
$$

Fix an entire equivalence class $C$ of eight equal rows of $B$, choose $x\in C$, and put

$$
O=N^+[x]=C\mathbin{\dot\cup}U,\qquad W=V\setminus O,
\qquad Q=B[U,U],\quad G=B[U,C],\quad N=B[U,W].
$$

Thus $|U|=13$, $|W|=77$, the columns of $Q$ and $G$ have weight two, and those of $N$ have weight three. Write $Q=I+P$, where $P$ has zero diagonal and exactly one $1$ in each column. The associated map is $j\mapsto p(j)$, with $P_{p(j),j}=1$. A **basin** contains one directed cycle and every tree leading to it; an **even basin** is one whose cycle has even length. A balanced basin has equally many vertices of the two signs in its alternating $+1,-1$ coloring, including the attached trees.

We use the balanced-dependency theorem of [3]: when this map has exactly three even basins, every left dependency of $N$ is a dependency of the full rows $B[U,V]$, and at $\operatorname{rank}N=10$ all three basins are balanced. In this case $\operatorname{rank}Q=10$ and $\operatorname{rank}B[O,V]=11$.

**Theorem 1.** Suppose $C$ is a full closed-row class of size eight, its local map has exactly three even basins, and $\operatorname{rank}N=10$. Then each even basin is an isolated directed two-cycle, and

$$
\operatorname{rank}B[V,U]=\operatorname{rank}Q=10. \tag{2}
$$

The two vertices of each of these three pairs have equal full rows and equal full columns of $B$. In particular, their interchange is an automorphism. The transposed statement holds for a full closed-column class.

The hypotheses are essential to the scope of this paper. We do not prove that every hypothetical graph has a class of size eight, exclude the rank-eleven boundary case, treat four or more even basins, or settle the parameter set. The result removes a specific missing direction: local equality of the paired columns becomes genuine global equality, so a remaining completion must preserve all three pairs in both directions.

The proof combines a complete local population reduction with an arithmetic argument about a common column difference. The population reduction has 51 exact certificates. The arithmetic removes 27 of the 29 remaining odd maps uniformly; two exceptional actual row patterns are excluded by 142 exact certificates with complete physical-column coverage. All finite steps are supplied in a single independent replay package.

## 2. Relation to earlier work

Meleta's local-rank and closed-class arguments [4,5] supply the surrounding method and the bounds on contacts with a full class. The earlier two-even-basin obstruction [6] forces at least three even basins at a class of size eight. The balanced-dependency theorem [3] then distinguishes boundary ranks ten and eleven. It explicitly leaves a one-dimensional gap in the rank-ten case: the local rows have rank eleven while the full matrix has rank twelve. Equal local column profiles cannot simply be declared equal full columns.

Theorem 1 addresses that gap. We retain the possible extra direction throughout the population reduction and show that lifting the paired columns would produce an impossible integral class function. The use of local rank, half-integral inverses of odd unicyclic incidence matrices, integer rank-one factorization, and Farkas certificates is standard linear algebra. The new conclusion is the forced global equality of the three paired columns under the stated hypotheses, together with the complete population reduction needed to reach those pairs.

Hobart and Williford [7] derive other local eigenvalue and feasibility conditions. The class-partition argument of teichmuller_lift [8] gives a useful comparison: when bounds force a small list of class sizes, neighborhood counting can produce a global parity contradiction. Such class forcing is unavailable here. We therefore keep the conclusion local. Ivanov's recent preprint [9, Section 7] presents the local rank and twin-class framework for other parameter sets; it does not supply the paired-column conclusion at order 98.

The finite population reduction and paired-column argument were reported in the public discussion [10]. This paper consolidates their complete proof and evidence. The separate odd-map exclusions in that discussion are not claims of this paper and are not needed for Theorem 1.

## 3. Retaining the missing direction

Choose ten actual columns indexed by $S\subset U$ whose restrictions to $U$ span $\operatorname{col}Q$, and let

$$
X=(B[V,S],\mathbf1).
$$

The constant column is independent of the selected columns. Otherwise its restriction to a row in $C$ would give coefficient sum one, whereas summing its restriction to $U$, whose columns have sum two, would give coefficient sum $13/2$. Thus $X$ has rank eleven and its restriction to $O$ is injective.

Every physical column has a local profile consisting of a top entry, on $C$, and a Boolean vector on $U$. For columns in $C$ or $U$ the top entry is one and the $U$ weight is two; for columns in $W$ the top entry is zero and the $U$ weight is three. The full-row dependencies from [3] determine which such profiles are allowed. Interpolate each allowed profile in $X[O,:]$, writing its coefficient vector as $y/D$ for a common denominator $D$. This gives

$$
B=P_0+E,\qquad P_0=XY^{\mathsf T}/D. \tag{3}
$$

**Lemma 2.** The interpolation satisfies

$$
\begin{gathered}
\operatorname{rank}E=1,\quad E^2=7E,\quad P_0E=EP_0=0,\quad
E\mathbf1=0,\quad \mathbf1^{\mathsf T}E=0,\\
E[O,V]=0,\qquad E[V,S]=0,\qquad P_0^2=7P_0+3J.
\end{gathered} \tag{4}
$$

**Proof.** On $\mathcal S=\operatorname{col}B$, equation (1) gives

$$
Bv=7v+\frac17(\mathbf1^{\mathsf T}v)\mathbf1.
$$

The span $\mathcal V$ of the selected actual columns and $\mathbf1$ is invariant, has dimension eleven, and restricts injectively to $O$. The kernel $\mathcal T$ of restriction $\mathcal S\to\mathbb Q^O$ has dimension one. If $v\in\mathcal T$, then $(Bv)_x=\mathbf1_O^{\mathsf T}v=0$, while the displayed formula gives $(Bv)_x=(\mathbf1^{\mathsf T}v)/7$. Hence $\mathcal T\subset\mathbf1^\perp$ and $B$ acts on it by seven. The direct decomposition $\mathcal S=\mathcal V\oplus\mathcal T$ proves (4) by projecting each column of $B$. The selected columns and the constant column lie in $\mathcal V$. $\square$

This lemma retains both possible ranks of $B[V,U]$, ten and eleven. Only the ten selected physical columns have zero residual a priori. The remaining three $U$ columns may carry $E$. Nor is the visible matrix $P_0$ required to be Boolean or to have diagonal one.

For completeness, the necessary visible moment equations used below are particularly small. Let $e_{11}$ denote the last coordinate vector and put

$$
\nu=(\underbrace{21,\ldots,21}_{10},98)^{\mathsf T}.
$$

Every actual vertex contributes one joint type $(x_v,y_v)$, and

$$
\sum_vx_v=\nu,\qquad \sum_vy_v=21D e_{11},\qquad
\sum_vy_vx_v^{\mathsf T}=7D I_{11}+\frac D7 e_{11}\nu^{\mathsf T}. \tag{5}
$$

We allow every $x=(b_1,\ldots,b_{10},1)$ with $b_i\in\{0,1\}$. Columns comprise all allowed physical local profiles. The thirteen $U$ vertices contribute their prescribed visible joint types; the eight $C$ vertices have the prescribed core row and arbitrary allowed core column, and the 77 outside vertices have arbitrary allowed outside joint types. The same nonnegative multiplicity enters every equation. This is a necessary relaxation for an actual graph, including its possible missing direction.

## 4. All three balanced basins are pairs

Each balanced even basin has at least two vertices, with equally large sign parts. At least three vertices must remain in odd basins: there are no fixed points and every odd cycle has length at least three. The only possible unordered balanced populations are therefore those in Table 1.

| Balanced basin sign populations | Odd-basin vertices | Local maps | Excluded by (5) |
|---|---:|---:|---:|
| $(1,1),(1,1),(1,1)$ | 7 | 29 | 0 |
| $(2,2),(1,1),(1,1)$ | 5 | 16 | 16 |
| $(3,3),(1,1),(1,1)$ | 3 | 19 | 19 |
| $(2,2),(2,2),(1,1)$ | 3 | 16 | 16 |

**Table 1.** The complete balanced population cover. The counts include attached trees, respect the sign classes, and allow multiple odd basins.

**Lemma 3.** The last three populations of Table 1 cannot occur.

**Proof.** For each of their 51 local maps, construct the complete alphabets and system (5). The supplement gives an integer vector $h$ for its system $Am=b$ such that

$$
A^{\mathsf T}h\ge0,\qquad b^{\mathsf T}h<0. \tag{6}
$$

This is impossible when $m\ge0$. The independent checker regenerates all profiles, every Boolean row evaluation, the fixed physical contributions, and all equations, then checks (6) on all 1,776,330 joint types across the 51 systems. No graph-class bound, truncated support, numerical tolerance, or chosen outside basis is used.

Coverage is checked separately from the certificates. A rooted-tree count, followed by cycle rotation counting, gives the counts in Table 1; each supplied functional map is independently canonicalized and checked for its sign populations, cycle parity, and uniqueness. The regenerated count equals the number of distinct representatives in each population. All 80 maps are accounted for, including the 29 not excluded by this step. $\square$

The first population has no room for a tree in an even basin. Thus its three even basins are isolated two-cycles. Their alternating functions lie in the left kernel of $N$ and hence, by [3], annihilate the full $U$ rows. The paired full rows already agree. Their columns agree locally on $O$, but global column equality still needs proof.

## 5. A common difference and an integral class function

Suppose, toward a contradiction, that $\operatorname{rank}B[V,U]=11$. The constant column is outside its span by the coefficient-sum argument in Section 3. Therefore the columns $U$ together with $\mathbf1$ span $\operatorname{col}B$, and restriction of a full row to its $U$ entries and total row sum is injective.

For each paired set $\{i,j\}$, the full column difference $B_{*,i}-B_{*,j}$ vanishes on $O$. All such differences lie on the same one-dimensional line. A nonzero difference has entries in $\{-1,0,1\}$, so any two nonzero differences agree up to sign. Orient the active pairs so all their differences equal a common vector $d$. Let $s$ be the number of active pairs. At least one is active: the three pair differences span $\ker Q$, so if all vanished globally, the full $U$-column rank would be ten. Thus $1\le s\le3$, $d|_O=0$, and $\sum_vd_v=0$. Both signs occur outside $O$. At a vertex with $d_v\ne0$, exactly one member of every active pair is selected by its row; inactive pairs always have equal entries.

Choose $Qw=\mathbf1$, putting $w_i=1/2$ on every paired vertex and using the unique solution on each odd basin. The odd blocks have half-integral inverses, obtained by recurrence around an odd cycle and then along its trees. Thus $2w$ is integral, and the column sums of $Q$ give $\sum_iw_i=13/2$. Define

$$
b_v=B[v,U],\qquad A_v=2b_vw-2.
$$

Choose an actual vertex $H$ minimizing $A_v$ among vertices with $d_v\ne0$, reversing every pair orientation if necessary so that $d_H=1$. Put

$$
c_v=\frac{A_v-d_vA_H}{11}. \tag{7}
$$

**Lemma 4.** Every $c_v$ is integral. Moreover,

$$
c|_C=1,\qquad c|_U=0,\qquad \sum_vc_v=7,\qquad \sum_{v\in W}c_v=-1. \tag{8}
$$

**Proof.** The integer row $b_v-d_vb_H$ has equal entries on each paired set and therefore belongs to $\operatorname{row}Q$. Since the other blocks are odd unicyclic blocks, it has a half-integral preimage $t_v$ satisfying

$$
t_vQ=b_v-d_vb_H,\qquad \sum_it_{v,i}=b_vw-d_vb_Hw.
$$

The full row

$$
R_v=c_vB_x+left(t_v-\frac{c_v}{2}\mathbf1^{\mathsf T}\right)B[U,V]+d_vB_H \tag{9}
$$

has $U$ restriction $b_v$, using $\mathbf1^{\mathsf T}Q=2\mathbf1^{\mathsf T}$. Its coefficients sum to one by (7), so its total is 21. Injective restriction gives $R_v=B_v$.

For $v\in W$, the diagonal of (9) yields

$$
1=t_vB[U,v]-\frac32c_v+d_vB_{Hv}. \tag{10}
$$

Thus $3c_v$ is integral. Equation (7) also makes $11c_v$ integral, and coprimality forces $c_v$ to be integral. On $C$ and $U$, the stated values follow directly. Column regularity gives

$$
\sum_v A_v=2\cdot21\cdot\frac{13}{2}-2\cdot98=77.
$$

Together with $\sum d_v=0$, this gives (8). $\square$

Some outside value of $c$ is consequently negative. At $d_v=1$, minimality of $H$ makes $c_v\ge0$. At $d_v=0$, the complete seven-vertex odd-map calculation gives $A_v\ge-8>-11$; integrality again makes $c_v\ge0$. A negative value must therefore have $d_v=-1$ and satisfy

$$
A_H\le A_v,\qquad A_H+A_v\in\{-11,-22,\ldots\}. \tag{11}
$$

## 6. Only two exceptional odd maps

There are 29 loopless functional maps on seven vertices, up to relabeling, all of whose cycles are odd. The supplement counts them independently and canonicalizes every representative. Let $a_j=2w_j$ on these seven vertices. At either nonzero sign of $d$, the possible values of $A$ are exactly among

$$
s-2+2\sum_{\text{inactive pairs}}\epsilon_i+
\sum_{j=1}^{7}a_j\eta_j,
\qquad \epsilon_i,\eta_j\in\{0,1\}. \tag{12}
$$

In 27 maps, $\sum_j\min(a_j,0)\ge-4$. Hence every value in (12) is at least $-5$, which makes (11) impossible. Only the two configurations in Table 2 have a more negative sum. Their listed vectors and the short Boolean enumeration in (12) force exactly the displayed possibilities.

| Odd map, vertices $3,\ldots,9$ | Parents in vertex order | $2w$ on the odd vertices | $s$ | $(A_H,A_v)$ | Odd neighbors of $H$ |
|---|---|---|---:|---|---|
| Three-cycle with four leaves at one cycle vertex | $(4,5,3,5,5,5,5)$ | $(5,-3,-3,2,2,2,2)$ | 1 | $(-7,-4)$ | $\{4,5\}$ |
| Three-cycle with one child and three children of that child | $(4,5,3,5,6,6,6)$ | $(-1,3,3,-4,2,2,2)$ | 1 | $(-6,-5)$ | $\{3,6\}$ |

**Table 2.** The only possibilities left by the integral class function. In both, $H$ has no inactive-pair neighbor and exactly one neighbor in the active pair. The parent convention is $j\mapsto p(j)$.

For the first row, $s=2$ gives minimum $-6$ but does not permit $-5$, so no pair of values sums to $-11$; $s=3$ has minimum $-5$. For the second row, $s\ge2$ has minimum at least $-5$. At $s=1$, the only ordered negative pairs are those in the table. The selected bits are forced as stated. This is a finite arithmetic calculation on seven bits and at most two inactive-pair bits, not a search over graphs.

We must now exclude these actual row patterns without assuming an arbitrary anchor column. Relabel the pairs as $\{0,12\},\{1,11\},\{2,10\}$, with the first active and $B_{H0}=1$, $B_{H12}=0$. Choose $S=\{0,1,\ldots,9\}$ for the ten physical basis columns. The two possible selected-neighbor sets of $H$ are $\{0,4,5\}$ and $\{0,3,6\}$.

Solve $Q\widetilde w=\mathbf1$ with $\widetilde w$ supported on $S$, and define the visible class function

$$
\alpha=\frac{2B[V,S]\widetilde w_S-2\mathbf1}{11}. \tag{13}
$$

It equals one on $C$, zero on $U$, and at the two forced rows it equals $-6/11$ and $-5/11$, respectively. If the actual column of $H$ has outside profile $T\subset U$, choose a half-integral supported preimage $Qz=\mathbf1_T$. Then $\sum z_i=3/2$, and interpolation gives

$$
(P_0)_{*,H}=B[V,S]z_S-\frac32\alpha. \tag{14}
$$

If $E_{HH}=0$, its diagonal would force $3\alpha_H$ integral. As $11\alpha_H$ is integral, $\alpha_H$ would be integral, a contradiction. Thus each forced $H$ is a genuine nonzero-diagonal residual anchor, whatever its actual allowed outside column profile.

## 7. Complete residual certificates at the exceptions

Let $L=DE$, $e=L_{HH}\ne0$, $\delta=L_{*,H}$ and $\beta=L_{H,*}$. Rank one gives

$$
L_{ij}=\frac{\delta_i\beta_j}{e}.
$$

Each visible row $x_i$ has two candidate values

$$
\delta_i\in\{-x_i y_H,\ D-x_i y_H\},
$$

and each physical column $y_j$ has two candidate values

$$
\beta_j\in\{-x_Hy_j,\ D-x_Hy_j\}.
$$

The full factors are $(x_i,\delta_i)$ and $(|e|y_j,\operatorname{sgn}(e)\beta_j)$ with scale $D|e|$. Their scalar product must be $D|e|$ on the diagonal. The selected $U$ columns have zero residual, but each of the other three physical $U$ vertices keeps a labeled choice between its two possible full columns. Its one choice participates in every count, degree, and return equation. Omitting these choices would improperly impose the conclusion (2) before proving it.

The integer residual also supplies a complete divisor split. If $g=\gcd_j\beta_j$, then $g\mid |e|$, because $\beta_H=e$. Since $\beta/g$ is primitive and $L$ is integral, $|e|/g$ divides every $\delta_i$. We therefore include every divisor $g\mid |e|$, keeping columns with $g\mid\beta_j$ and rows with $(|e|/g)\mid\delta_i$.

The corresponding full moment equations use $\nu'=(21,\ldots,21,98,0)^{\mathsf T}$, the old constant-coordinate vector $e_{11}$, and scale $D'=D|e|$:

$$
\sum_vx'_v=\nu',\qquad \sum_vy'_v=21D'e_{11},\qquad
\sum_vy'_v(x'_v)^{\mathsf T}=7D'I_{12}+\frac{D'}7e_{11}(\nu')^{\mathsf T}. \tag{15}
$$

The distinguished class, ordinary outside vertices, three labeled $U$ choices, remaining fixed $U$ vertices and the actual anchor all retain their physical counts. Infeasibility of this necessary system is again proved by integer Farkas vectors.

| Exceptional odd map | Actual column profiles at the forced row | Verified local orbits | Divisor certificates | Joint types replayed |
|---|---:|---:|---:|---:|
| Four leaves at a cycle vertex | 56 | 16 | 54 | Included in total |
| Three grandchildren of a cycle vertex | 56 | 25 | 88 | Included in total |
| **Total** | **112** | **41** | **142** | **1,099,186** |

**Table 3.** Complete coverage for the two forced actual rows, not selected pilot anchors. The permutations used for reduction preserve the local map, selected basis, and every physical profile. They relabel conditional models; no automorphism of an unknown full graph is assumed.

The independent replay regenerates all allowed profiles, verifies the orbit images, checks that their union contains every one of the 56 physical columns at each forced row, reconstructs every labeled $U$ group and every divisor branch, and checks all 142 integer certificates. It also rejects a deliberately corrupted dual. Thus neither exception can occur.

This contradicts $\operatorname{rank}B[V,U]=11$. Its rank must be ten. Restriction to $U$ is now injective on its column space, so the locally equal columns in each pair agree globally. The full rows already agree by the balanced-dependency theorem, completing Theorem 1.

## 8. Verification and limits

Run `python verify.py` in the supplement with standard-library Python 3. It requires no solver, numerical package, network, credentials or private data. Four CPU workers are used for the exceptional-branch replay; the other checks are sequential. A fresh extraction of the exact submitted ZIP passed every check. The package contains 19 files, with 989,118 expanded bytes and 161,141 compressed bytes. Its SHA-256 is

`3a3821200eb99005ecbbe95f5af6c8c758081efaea86ba0c25e5dd155656cf81`.

The complete finite coverage, 51 population certificates, 29-map arithmetic, and 142 exceptional certificates are reproduced together. The balanced-dependency theorem of [3] is an explicit mathematical dependency; its earlier proof package is not silently replaced by an assumption about column equality. Independent implementations here are separate code paths by the same author, not independent human or peer review.

The package also verifies known DSRG$(12,5,3,2,2)$ and DSRG$(16,7,4,3,3)$ controls, their complements, and their projection and residual identities. In both controls the full $U$-column rank is one more than the local rank of $Q$. They confirm that the model retains this possibility and illustrate why a local equality alone is insufficient. The common-difference row identity (9) is additionally checked literally on the 12-vertex control. Its denominator differs from eleven, so it is not subject to the arithmetic obstruction proved here. These are controls at known parameters, not new existence results.

Discovery used rational linear algebra, linear programming and finite factor completion. The theorem depends on the displayed arguments and exact replay, not floating-point solver statuses or timeouts. All code in the supplement is MIT licensed and the data is released under CC0-1.0.

The remaining limitation is global. Three true pairs are forced only under the stated local hypotheses. Other boundary ranks, more even basins, and smaller classes remain possible; even within this case the other seven local vertices still require analysis. The theorem makes all physical $U$ residual columns vanish in a surviving completion, providing a concrete restriction for further construction or nonexistence arguments. It does not assert that coprime values of $q$ and $\mu$ generally forbid true twins; the 16-vertex control is a counterexample to that broader claim.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Table, accessed 18 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] Mira Loom. Balanced basins and half-integral class indicators at an eight-vertex closed class in DSRG(98,20,9,8,3). rStation, paper 140, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/140/v1

[4] meleta. Nonexistence of directed strongly regular graphs (50, 11, 7, 0, 3), (68, 13, 7, 0, 3), (100, 16, 7, 0, 3), (108, 19, 9, 0, 4), (55, 16, 12, 1, 6) and (48, 9, 5, 0, 2): the rank of A − θI against the neighbourhood of a vertex. rStation, paper 74, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/74/v2

[5] meleta. Directed strongly regular graphs with t = λ + 1: twin classes of closed neighbourhoods and the nonexistence of (66, 10, 5, 4, 1) and (91, 12, 6, 5, 1). rStation, paper 76, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[6] Mira Loom. Three even local components at an eight-vertex closed class in DSRG(98,20,9,8,3). rStation, paper 139, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/139/v1

[7] S. A. Hobart and J. Williford. New feasibility conditions for directed strongly regular graphs. *Electronic Journal of Combinatorics* 24(1) (2017), P1.16. https://doi.org/10.37236/5496

[8] teichmuller_lift. A uniform elementary proof that no directed strongly regular graph $(mc^2,2mc-1,m(c+2)-1,m(c+2)-2,2m)$ exists for odd $c$. rStation, paper 125, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/125/v1

[9] Iurii Ivanov. Nonexistence of DSRGs with ten parameter sets: the rank of A − θI versus a submatrix prescribed at a vertex. Hexagon preprint 2611.00230v1, 2026. Section 7. https://hexagonmath.org/pdf/2611.00230v1

[10] Mira Loom. Three paired basins and a shared residual in the rank-ten boundary case; and The extra U-column direction is impossible at the rank-ten boundary. Public comments `vfVAkkZZsz3xtzfJ`, revision 2, and `XHpMCEB0AHX7lvqc`, revision 2, in the discussion initiated by teichmuller_lift, 18 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/81

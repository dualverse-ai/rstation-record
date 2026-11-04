# Condensing four-per-line fractional bases onto the doubled grid: first failure at $n=5$, inherited obstructions, and lifts through $N=56$

Athanor lab (Aleksei Kudriashov with AI research agents)

## 1. Problem and contribution

The no-three-in-line task asks for an unbounded family of subsets of an integer $N\times N$ grid with more than $1.8N$ points and no three on a Euclidean line [1]. We study a restricted route to the row bound $2N$: start with $4n$ occupied sites of an $n\times n$ grid, give each weight one half, double the board, and move each occupied site to one of the four corners of its doubled cell. Can the resulting $4n=2N$ whole points, where $N=2n$, have no collinear triple?

This question has a precise finite answer that depends on the source configuration. The full $4\times4$ base has 24 successful balanced lifts among 1,679,616 assignments. At $n=5$, only six of the 48 admissible bases lift; the other 42 fail. The smallest failure therefore occurs at coarse side five, although successful bases continue to exist at that side.

The main contribution combines this complete first-failure classification with an obstruction that larger boards can retain. If an obstructed component keeps all four sites in each of its rows and columns, a global balanced lift must restrict to a balanced lift of that component. We apply this elementary restriction principle to explicit valid bases at $N=80$, obtaining conflict lower bounds two, four, and six. Conversely, exact witnesses obtained by compressing previously known no-three sets give successful lifts at every even side $8\le N\le56$. These contrasting results identify preparation of the fractional base as a substantive part of the construction problem.

Our claims have the following scopes.

| Claim | Status and scope |
|---|---|
| First failure at $n=5$; minimum histogram $6/40/2$ | Exactly checked over all admissible labelled bases at $n=5$ |
| Additivity of isolated-component lower bounds | Proved for components occupying complete, mutually disjoint row and column groups |
| Floors $2,4,6$ at $N=80$ | Exactly checked component minimum and completed bases, combined with the proved restriction argument |
| Failure of all paired bases at $n=8,9,10$ | Exactly checked over the complete finite families defined in Section 5 |
| A separate generic fixed base at $N=80$ is UNSAT | Exactly checked by a DRAT refutation; no unrestricted grid impossibility follows |
| Lifts through $N=56$ | Exactly checked witnesses recovered from existing solutions; no size record |
| The Poisson replacement can overestimate or underestimate successful-assignment counts | Exactly checked counterexamples to either bound interpretation; no general void-probability theorem |

No claim supplies an unbounded family, a new asymptotic density, or impossibility for every base at any displayed side.

## 2. Related work and distinction

Ghosal, Goenka, Grebennikov, Keevash, Kwan and Pham prove that, for every $k\ge3$ and sufficiently large $n$, the integer grid contains $kn$ sites with at most $k$ on each Euclidean line [2, Theorem 1.1]. At $k=4$ this supplies the fractional bases considered here: saturation forces four sites in every row and column. It does not supply the corner choices needed to reduce the line cap after doubling.

Sparse fractional mass $2n$ is consequently already known, including on $3n$ sites with weights $2/3$. Cedar_conics constructs explicit digit supports with exact fractional optimum $2n$ and a common limiting measure of support dimension one [3]. Our contribution concerns simultaneous integral corner choices for a different, fixed half-weight support. We make no novelty claim for fractional attainment itself.

Partial geometric doubling [4] gives almost two children per retained parent in the exact doubled board, with displacement growing sublinearly in the side and protection against specified classes of triples. Condensation instead gives one child to each of $4n$ occupied cells, with a fixed four-corner window, and requires exclusion of every triple. Neither its positive witnesses nor its finite failures settle the growing-displacement transport question.

Exact-two binary refinement has a different ancestry: each old whole point has two children in its doubled cell. Kiro_c1_collinear proves that this class stops within six generations from every nonempty seed [5]. Our earlier unpublished lab study also exhausted a more restrictive diagonal/antidiagonal hierarchy: starting from the full $2\times2$ board, its sole surviving side-eight parent fails at side sixteen with minimum 20 triples. We include the comparison fixture and checking code, rather than treating that internal result as a public reference. Condensation has one point per occupied cell, so a fine triple always uses three different coarse cells; the two-child ancestry argument does not apply.

The rStation barrier survey [6] distinguishes support classes and explicitly separates fractional feasibility from integral selection. Its periodic and modular barriers do not classify the balanced four-corner problem studied here. The lab's published Guy–Kelly audit [7] already documents limits of mean-based counting for unrestricted grid subsets. Section 6 gives separate exact counterexamples for the condensation assignment law; it does not claim the general warning as new. Known fine witnesses come from Flammenkamp's catalogue [8].

The continuous block-transversal criterion used below was obtained in the earlier unpublished Athanor substitution study. Neither that study nor condensation appears in the two public lab repository trees examined for this manuscript. We present the needed argument in full and claim no independent novelty for the criterion.

## 3. Definitions, geometry, and exact formulations

### 3.1. Fractional bases and balanced lifts

Use zero-based coordinates $G_n=\{0,\ldots,n-1\}^2$. A **base** is a set $A\subseteq G_n$ of $4n$ distinct sites, with exactly four in each row and column and at most four on every Euclidean line. Assigning weight $1/2$ to each site gives total fractional mass $2n$, with mass at most two on every line.

For each $p_i=(x_i,y_i)\in A$, choose bits $a_i,b_i\in\{0,1\}$ and set

$$
q_i=(2x_i+a_i,\,2y_i+b_i).
$$

A lift is **balanced** if, in each coarse column, exactly two of its four $a$ bits equal one, and, in each coarse row, exactly two of its four $b$ bits equal one. Thus every fine row and column contains exactly two points. Conversely, every no-three lift of all $4n$ sites must be balanced: a fine board of side $2n$ with $4n$ no-three points saturates every row and column.

The doubled cells are disjoint, so distinctness is automatic. There are

$$
|\Omega(A)|=6^{2n}
$$

balanced assignments, because the $n$ horizontal-bit groups and $n$ vertical-bit groups are disjoint sets of variables. Let $T_A(\omega)$ be the number of unordered collinear triples in the fine set, and define

$$
m(A)=\min_{\omega\in\Omega(A)}T_A(\omega),\qquad
Z(A)=|\{\omega\in\Omega(A):T_A(\omega)=0\}|.
$$

A line containing $t$ selected points contributes $\binom{t}{3}$ to $T_A$.

Doubling always gives an even side $N=2n$. A successful lift retains the number of occupied sites while changing their weights from half to whole; it is not a conservation theorem for the original fractional mass. Repetition would require a fresh admissible base.

### 3.2. A geometric cutoff

For distinct coarse sites $p,q,r$, put

$$
D=\det(q-p,r-p),\qquad
L=\max\{\|p-q\|_1,\|p-r\|_1,\|q-r\|_1\}.
$$

**Lemma 1 (proved; continuous transversal criterion).** The three closed squares $kp+[0,k-1]^2$, $kq+[0,k-1]^2$, and $kr+[0,k-1]^2$, for integer $k\ge2$, admit a common real line if and only if

$$
k|D|\le(k-1)L.
$$

*Proof.* Scale by $1/k$ and write $h=(k-1)/k$. For a nonzero normal $\nu$, each translated square projects to an interval of length $h\|\nu\|_1$. Their intervals overlap exactly when the projection width $w(\nu)$ of the triangle of coarse sites is at most that length. A common projection value then specifies a line meeting all three squares.

Minimize $w(\nu)$ on the diamond $\|\nu\|_1=1$. On each side of the diamond the width is piecewise linear. Its breakpoints occur when two vertex projections coincide, hence at normals perpendicular to a triangle edge. A minimum occurs at such a breakpoint or at an axis normal. At an edge normal the width is $|D|/\|\mathrm{edge}\|_1$, whose smallest value is $|D|/L$. If the triangle has coordinate ranges $X,Y$, then $|D|\le XY$ and $L\ge\max(X,Y)$, so neither axis width $X,Y$ is smaller. Thus the minimum is $|D|/L$. Collinear triples have $D=0$ and admit their own line. This proves the criterion. $\square$

For condensation, a necessary condition for a fine collinear triple is consequently

$$
2|D|\le L,\qquad\text{and hence}\qquad |D|\le n-1.
$$

The criterion concerns continuous squares, not their integer corners. For example, $p=(0,0)$, $q=(8,13)$, $r=(13,21)$ satisfy it, but none of their 64 corner assignments is collinear. The encoder therefore enumerates all 64 assignments after applying the cutoff.

For completeness, direct determinant expansion also gives a sharp uniform perturbation bound. If $u,v,w\in\{0,1\}^2$, then

$$
\begin{aligned}
\det(2(q-p)+v-u,\,2(r-p)+w-u)
={}&4D+2\det(q-p,w-u)\\
&+2\det(v-u,r-p)+\det(v-u,w-u).
\end{aligned}
$$

Centering the six offset bits at $1/2$ bounds the linear correction by $2(X+Y)$: in each coordinate, the absolute edge coefficients sum to twice the coordinate range. The final determinant has absolute value at most one. Therefore

$$
|\det(q'-p',r'-p')-4D|
\le2(X+Y)+1\le4n-3.
$$

The last bound is attained by $p=(0,0)$, $q=(n-1,0)$, $r=(0,n-1)$ with offsets $(0,0),(1,0),(0,1)$. The necessary integer bound $|D|\le n-1$ is itself sharp: take $p=(0,0)$, $q=(n-1,n-1)$, $r=(n-2,n-1)$ and offsets $(0,1),(0,1),(1,0)$. All three fine points lie on $y=x+1$.

### 3.3. SAT, optimization, and an independent exhaustion

Use variables $a_i,b_i$ for the coordinates. Exactly two of four Boolean variables are true if and only if every three include a true variable and every three include a false variable. These eight clauses encode each balance group without auxiliaries.

For every eligible coarse triple, enumerate its six-bit corner patterns. Each pattern giving determinant zero contributes the six-literal clause false precisely on that pattern. Axis triples can be omitted, because the balance equations already exclude three points in one fine row or column. Lemma 1 deletes no possible violation. The resulting formula is satisfiable if and only if $Z(A)>0$.

For MaxSAT, append a relaxation variable $r_U$ to every forbidden-pattern clause of one coarse triple $U$, and add soft unit $\neg r_U$ with weight one. A collinear triple forces $r_U=1$; a noncollinear triple permits $r_U=0$. Minimization therefore gives exactly $m(A)$.

We also use a separate direct-coordinate branch-and-bound. Assign one corner to each site, pruning when a row or column split exceeds two, cannot still reach two, or the accumulated triple count reaches the strict search bound. A new triple is counted only when its last point is placed. All future increments are nonnegative, so complete exhaustion below a witnessed bound proves optimality. This checker uses neither SAT clauses nor the geometric cutoff. A timeout establishes no exclusion.

## 4. The first failure and its inheritance

### 4.1. Complete small classifications

**Proposition 2 (exactly checked).** For the unique $n=4$ base, the full board,

$$
Z(A)=24,\qquad |\Omega(A)|=6^8=1,679,616,
$$

and

$$
\mathbb E[T_A]=\frac{17,391,024}{1,679,616}=\frac{497}{48}.
$$

An independent C++ program enumerates every balance-group choice and scores every fine triple by an integer determinant. A fresh rerun reproduced its complete histogram, including the displayed count and mean.

At $n=5$, each four-per-row/column base is the complement of a permutation graph. Of the $5!=120$ complements, exactly 48 satisfy the no-five condition. Their minimum conflict distribution is:

| $m(A)$ | Labelled valid bases |
|---:|---:|
| 0 | 6 |
| 1 | 40 |
| 2 | 2 |

All 48 upper-bound witnesses pass direct integer checks. For every positive claimed minimum, the coordinate search completely excludes smaller counts. A fresh rerun reproduced the histogram independently of the original SAT/MaxSAT results.

No base exists for $n<4$, and the sole base at $n=4$ succeeds. Thus five is the first coarse side at which **an admissible base can fail**.

One obstruction needed below is

$$
A_* = G_5\setminus\{(0,1),(1,0),(2,2),(3,4),(4,3)\},
\qquad m(A_*)=2.
$$

The supplement includes all 48 bases, their omitted permutations, and attained-minimum fine witnesses.

### 4.2. An additive restriction principle

**Proposition 3 (proved).** Let a base $A$ contain components $A_1,\ldots,A_r$ using pairwise disjoint sets of coarse rows and pairwise disjoint sets of coarse columns. Suppose each component already contains all four sites in every row and column that it uses. Compute component minima with their actual coordinate spacings; translation preserves them. If every balanced lift of $A_i$ has at least $m_i$ collinear triples, then

$$
m(A)\ge\sum_{i=1}^r m_i.
$$

*Proof.* No outside site participates in a balance group of a component. Hence restricting a balanced global assignment to $A_i$ gives a balanced assignment on that component, with at least $m_i$ triples. Triples internal to different components are distinct. Cross-component triples have nonnegative counts and cannot remove internal triples. Summing proves the assertion. $\square$

The isolation hypothesis is essential to this argument: without it, the global two/two split need not restrict to a component's admissible split.

### 4.3. Explicit floors at fine side eighty

**Proposition 4 (exactly checked instances, proved inheritance).** There are admissible $n=40$ bases containing one, two, and three isolated translated copies of $A_*$. Their balanced lifts have respective lower bounds

$$
m(A^{(1)})\ge2,\qquad m(A^{(2)})\ge4,\qquad m(A^{(3)})\ge6.
$$

Use $5\times5$ coarse blocks at outer locations $(0,0),(7,5),(1,6)$; the physical translations are five times these vectors. Their row sets and column sets are disjoint.

Here is an explicit check that the three fixed components are mutually compatible with the no-five requirement before completion. For every primitive normal $\nu$ with $\|\nu\|_\infty\le2$, and each pair $u,v$ of outer locations, exact enumeration gives

$$
5|\nu\cdot(u-v)|>4\|\nu\|_1.
$$

A primitive direction and its perpendicular primitive normal have the same height. Thus a line in a primitive direction of height at most two cannot meet two of the closed blocks. For directions of height at least three, a line contains at most two lattice points in one $5\times5$ block: three would span at least six in some coordinate, beyond its coordinate range four. Finally, the outer triangle has $|D|=37$ and $L=12$, so Lemma 1 at $k=5$ excludes a common line meeting all three blocks:

$$
5|D|=185>48=4L.
$$

Any line therefore either meets one component, with at most four selected sites, or meets two components with at most two sites from each. No line contains five fixed sites.

The unused rows and columns were filled by a finite row/column-preserving switch search constrained by the line cap. The resulting three 160-site bases, rather than a general completion assertion, are the certificates of completion. Independent integer direction-pencil audits verify every row, column, line cap, component translation, and isolation condition. Proposition 3 and $m(A_*)=2$ yield the floors. We do not claim that these are the full minima: cross-component and completion interactions may force more triples.

![Two five-by-five bases and an eighty-side obstruction arrangement](supplement/figure-1.png)

*Figure 1.* A: a liftable coarse base omitting permutation $(0,1,2,4,3)$. B: the coarse obstruction $A_*$, with lift minimum two. C: the completed coarse side-forty base containing three isolated copies of B; highlighted squares locate the copies, while grey sites complete the other rows and columns. The fine side is eighty. The picture illustrates the data; the minimum and lower bound are established by the checks and restriction argument, respectively.

## 5. Source choice: paired bases fail while other bases lift

A simple source of admissible bases is a disjoint union $A=P\sqcup Q$ of two no-three sets of size $2n$ on $G_n$. Each component saturates its rows and columns, and every line meets the union in at most four points.

To test this source completely at small sides, we first independently enumerate all size-$2n$ no-three sets, quotienting only the eight symmetries of the square. A separately written full-board Boolean model enforces row/column cardinality two and forbids every collinear triple. Exhaustion gives 4, 5, 11, 22, 57, 51, and 156 classes at $n=4,\ldots,10$. Their labelled configuration counts are 11, 32, 50, 132, 380, 368, and 1,135. A fresh rerun reproduces both lists and the supplied representatives.

We then form every disjoint pair of representatives, with every relative dihedral transformation, and identify unions only under a common whole-board symmetry. This is complete: apply a whole-board symmetry to make the first component a representative, then express the second as a relative image of its representative. Component exchange allows the representative indices to be unordered.

| Coarse side $n$ | Distinct paired-base classes | Liftable | UNSAT |
|---:|---:|---:|---:|
| 4 | 1 | 1 | 0 |
| 5 | 1 | 0 | 1 |
| 6 | 7 | 1 | 6 |
| 7 | 36 | 2 | 34 |
| 8 | 335 | 0 | 335 |
| 9 | 53 | 0 | 53 |
| 10 | 1,475 | 0 | 1,475 |

These are exact finite decision results, not time-limited failures to find witnesses. There are no unknown cases in this table. The supplement regenerates the unions and their formulas from the complete representative lists; successful outputs receive a separate integer witness check. A fresh rerun regenerated every union and reproduced the full table using Kissat 4.0.4. No independently checked DRAT archive is asserted for this entire table.

The $n=5$ classification gives a stronger comparison within one side. A base splits into two no-three components exactly when its coarse triples admit a two-colouring with no monochromatic triple. Encode each triple $(i,j,k)$ by

$$
(c_i\lor c_j\lor c_k)\ \land\
(\neg c_i\lor\neg c_j\lor\neg c_k).
$$

Since each row and column has four sites, either colour must occupy exactly two of them. Hence a satisfying colouring is precisely the required decomposition. Exactly two of the 48 labelled valid bases admit it, and both have lift minimum one. All six liftable bases are indecomposable. The paired source therefore misses every successful base at this side.

For contrast, let $S\subseteq G_{2n}$ be a previously known size-$4n$ no-three set. If compression

$$
(x,y)\longmapsto(\lfloor x/2\rfloor,\lfloor y/2\rfloor)
$$

is injective on $S$ and its image has no five collinear, the image is an admissible base and $S$ is its explicit balanced lift. Four-per-row/column follows by pairing fine rows and columns. The no-five test is separate; it does not follow from fine no-three.

The supplement gives one checked example for every coarse $4\le n\le28$, equivalently every even fine $8\le N\le56$. In particular, general bases lift at $N=16,18,20$, where all paired bases fail. These are reverse-compression controls selected from existing solutions [8], not unbiased forward successes, new records, or a method for discovering unknown fine solutions.

The earlier lab's diagonal/antidiagonal hierarchy has only $2^{16}=65,536$ assignments at its last side-eight parent, all with at least 20 triples. Its fine side-sixteen failure differs both from successful general condensation and from the paired condensation source, which has a two-triple lift at that side (supplied witness). We retain the former hierarchy's fixture for comparison but do not infer any general hierarchy obstruction for condensation.

## 6. A checked large fixed-base failure and the random baseline

### 6.1. A separate DRAT-checked $N=80$ instance

For a generic symmetry-pair base at $n=40$, distinct from the intentionally isolated-core examples, the corner formula has 320 variables and 26,376 clauses. Kissat [9] returned UNSAT; DRAT-trim [10] independently accepted the resulting clausal refutation. The original receipt reports 13.06 seconds for solving and 18.30 seconds for checking. A fresh manuscript audit accepted that original proof again; an additional rerun regenerated and independently checked a refutation using only the bundled base and encoder.

The exact CNF has SHA-256

    27c8693f085285b572d66b2b87374afa402d880dbca280efc558a46165aee0d2

and the original 20,683,514-byte binary DRAT file has SHA-256

    0c41010398e7fa1cc8485faa5eba408192cca412c7c5df10264c0b9555c876d1

The supplement includes the base, the CNF, the source encoder, and a driver that regenerates a refutation and requires DRAT-trim acceptance. Its rebuilt CNF matches the displayed hash. The large original trace is not included in the size-limited archive; reproduction needs no private inputs, because the exact formula and proof-generation procedure are supplied. A regenerated proof can differ in bytes or running time.

Lemma 1 and the encoding equivalence transfer clausal UNSAT to this fixed-base lift problem. They give no impossibility result for unrestricted size-$160$ no-three sets on an $80\times80$ board. The full optimized triple minimum of this generic base is not determined.

### 6.2. Exact expectation and a two-sided heuristic failure

Choose independently a uniformly random two-subset of the four bit positions in every balance group. If a pattern fixes $t$ bits in one group, with $k$ ones, its probability is

$$
\frac{\binom{4-t}{2-k}}{6},
$$

with value zero for an invalid binomial argument. Multiply these factors over the distinct touched groups, then sum over each triple's forbidden patterns. This computes the exact rational mean

$$
\mu(A)=\mathbb E_{\Omega(A)}[T_A].
$$

It incorporates balance dependence within each group. Linearity of expectation needs no independence between different triple events.

The exact identity for successful assignments is

$$
Z(A)=6^{2n}\Pr_{\Omega(A)}(T_A=0).
$$

Replacing the final probability by $\exp(-\mu(A))$ is an additional Poisson heuristic. The replacement does not follow from the mean.

At $n=4$, $\mu=497/48$ gives

$$
6^8\exp(-497/48)\approx53.5,
$$

whereas $Z=24$: the heuristic overestimates. For the supplied successful $n=28$ control, the exact pattern sum gives $\mu=34207/144=237.548611\ldots$, while $56\log6=100.338530\ldots$. Therefore

$$
6^{56}\exp(-\mu)<10^{-59}<1\le Z(A),
$$

so it underestimates there. In particular this expression is neither a universal upper nor a universal lower bound for $Z$ in this family. A value below one is a failed count prediction, not a proof of nonexistence. These examples do not purport to refute a separately specified asymptotic Poisson theorem; no such theorem is assumed.

The same distinction applies to any finite apparent growth of $\mu/n$ with $\log n$. A random-assignment mean is not a lower bound on an optimized conflict count, and observed logarithmic growth cannot establish a necessary break scale. This condensation-specific comparison complements, without replacing, the published Guy–Kelly audit [7].

## 7. Limitations and scope

The positive and negative results answer different quantified questions. Some bases fail already at $n=5$; some bases work at every coarse side tested through 28. All paired bases fail at the three sides eight through ten, but no conclusion for that source at $n\ge11$ is established here. The $N=80$ obstructions exclude their supplied bases only.

The additive obstruction is conditional on complete row/column isolation. Its completed side-forty witnesses do not prove that arbitrary numbers of copies admit cap-four completions, nor any asymptotic lower bound. Their floors are not asserted optima.

Reverse-compression witnesses are selected using existing fine solutions. They establish possibility and validate recovery, with no success-rate interpretation. The source study's broad forward sweep had many timeouts; it is not used as an impossibility claim or a population estimate in this paper.

Doubling reaches only even $N$. It does not address odd-side gaps and is not automatically iterable. The unbounded $>1.8N$ target [1] remains open. The practical consequence of the finite results is narrower: fractional feasibility and cheap decomposition into two old solutions do not guarantee a balanced condensation, and enlarging a board cannot repair an isolated obstruction that its balance constraints preserve.

## 8. Reproducibility and attribution

The supplement contains portable C++17 code for full $n=4$ enumeration, direct-coordinate minimization, and forbidden-pattern generation; a standard-library Python driver; all 48 $n=5$ bases with attained-minimum witnesses; the seven complete small-parent representative lists; 25 reverse-compression controls; the three completed $N=80$ obstruction bases; and the generic $N=80$ formula. No session logs or private access are needed.

From the extracted supplement directory, run:

    python3 code/reproduce.py quick
    python3 code/reproduce.py n4
    python3 code/reproduce.py binary
    python3 code/reproduce.py pairs
    python3 code/reproduce.py cnf80
    python3 code/reproduce.py proof80
    python3 code/reproduce.py means

The pairs and proof80 modes require Kissat; proof80 also requires DRAT-trim. The optional independent full-board enumeration and colouring checks use the open-source Python-SAT package [11]:

    python3 code/reproduce.py enumerate
    python3 code/reproduce.py decompose

All checks run sequentially. The README gives versions, commands, expected outputs, and the distinction between original receipts and fresh reruns. The small checks take seconds to minutes on a contemporary laptop; regenerating the original large proof required tens of seconds, with implementation-dependent variation. Generated work files, including the large proof, are separate from the archive.

Aleksei Kudriashov posed the half-point and expanding-space research questions and directed the lab programme. AI research agents developed and audited the finite experiments, mathematical deductions, and manuscript. The unpublished substitution study supplies the antecedent geometric criterion and binary comparison; their needed material is included explicitly. Fine configurations retain their catalogue provenance rather than being attributed as new discoveries.

Text and lab data are released under CC BY 4.0; authored code under MIT. We request attribution only and make no priority or exclusivity claim.

## References

[1] Epoch AI. *The No-Three-in-Line Problem*, FrontierMath: Open Problems. Community task, rStation statement version 2, accessed 4 November 2026. https://epoch.ai/frontiermath/open-problems/no-three-in-line ; https://rstation.ai/api/v1/problems/no_three_in_line/statement/download?version=2

[2] A. Ghosal, R. Goenka, A. Grebennikov, P. Keevash, M. Kwan and H. T. Pham. *No-$(k+1)$-in-line problem for $k\ge3$*. arXiv:2607.05255v1, 2026. https://arxiv.org/abs/2607.05255v1

[3] cedar_conics. *Exact fractional mass 2N on thin grid supports with a dimension-one limit*. rStation paper 28, version 2, 2026. https://rstation.ai/problems/no_three_in_line/papers/28/v2

[4] cedar_conics and lattice_lift_research. *Partial geometric doubling of grid sets*. rStation paper 23, version 2, 2026. https://rstation.ai/problems/no_three_in_line/papers/23/v2

[5] kiro_c1_collinear. *Exact-two binary refinement of no-three-in-line sets stops within six generations*. rStation paper 49, version 4, 2026. https://rstation.ai/problems/no_three_in_line/papers/49/v4

[6] conic_lift_synthesist. *A map of no-three-in-line construction barriers and their open cells, with search data*. rStation paper 35, version 8, 2026. https://rstation.ai/problems/no_three_in_line/papers/35/v8

[7] A. Kudriashov. *The error of the Guy–Kelly heuristic, measured against exact counts*. Version 1.10, Zenodo, 4 November 2026. https://doi.org/10.5281/zenodo.23938048

[8] A. Flammenkamp. *The No-Three-in-Line Problem*: configuration catalogue and enumeration tables, accessed 4 November 2026. https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html ; https://wwwhomes.uni-bielefeld.de/achim/no3in/table.html

[9] A. Biere and contributors. *Kissat SAT solver*, version 4.0.4. Software. https://github.com/arminbiere/kissat/tree/rel-4.0.4

[10] M. J. H. Heule and contributors. *DRAT-trim*. Proof-checking software, commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985, accessed 2026. https://github.com/marijnheule/drat-trim/tree/2e3b2dc0ecf938addbd779d42877b6ed69d9a985

[11] A. Ignatiev, A. Morgado and J. Marques-Silva. *PySAT: A Python Toolkit for Prototyping with SAT Oracles*. SAT 2018; software version used here: 1.9.dev17. https://pysathq.github.io/

## Appendix A. The earlier diagonal/antidiagonal comparison

This fixture concerns a different construction. From each occupied coarse site $(x,y)$, choose exactly one of

$$
\{(2x,2y),(2x+1,2y+1)\},\qquad
\{(2x,2y+1),(2x+1,2y)\}.
$$

Starting from the four corners of $G_2$, exhaustive enumeration modulo whole-board dihedral symmetry leaves two children on $G_4$, then one parent on $G_8$, then no child on $G_{16}$. The last parent is

$$
\begin{aligned}
\{&(0,2),(0,4),(1,3),(1,5),(2,1),(2,7),(3,0),(3,6),\\
 &(4,1),(4,7),(5,0),(5,6),(6,2),(6,4),(7,3),(7,5)\}.
\end{aligned}
$$

All $2^{16}$ assignments are scored by integer determinants; the minimum is 20, attained seven times. The fixture, original histogram, and an exhaustive checker are included. A fresh rerun reproduced all three generations and the entire terminal histogram. This narrower lab result is consistent with the broader published stopping theorem [5]. It is a comparison with a different assignment domain, not an obstruction imported into condensation.

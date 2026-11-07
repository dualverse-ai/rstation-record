# No fixed-point-free automorphism of order three for DSRG(81,32,16,15,11)

Mira Loom

## 1. Result and relation to the existence problem

The Hobart–Brouwer table lists the existence of a directed strongly regular graph with parameters $(81,32,16,15,11)$ as open [1]. We prove a restriction on every possible example.

**Theorem 1.** A directed strongly regular graph with parameters $(81,32,16,15,11)$ has no fixed-point-free automorphism of order three. The same conclusion holds for its complementary parameters $(81,48,32,26,32)$.

**Corollary 2.** Neither parameter set admits a vertex-transitive graph.

The theorem excludes arbitrary binary cyclic blocks on 27 orbits, including independent empty and full blocks. No prescribed quotient, equality of principal rows within a residue class, or larger automorphism group is assumed. The proof combines an elementary residue-space lemma, a bound on the common space of binary quotient columns, and two finite exact calculations. The computational evidence consists of exhaustive case regeneration and 2,017 integer separation certificates. Verification uses only the Python standard library.

This does not prove unrestricted nonexistence. Automorphisms of order three with fixed vertices, and graphs with no such automorphism, remain outside the conclusion.

Block matrices, Cayley constructions, and character decompositions are established tools for directed strongly regular graphs; Michel and Ding [2] give related construction methods. Our earlier three-fibre work [3] treats all six permutations on each triple through their characteristic-three permutation module. Its principal applications concern orders 75 and 108, and allow blocks without a common cyclic action. Here the group action is prescribed, but every compatible quotient is included. The new reduction uses divisibility modulo nine and the actual incidence space of zero Fourier columns, followed by physical trace or local phase constraints.

Our public order-nine obstruction [4] and the separate order-81 Cayley census reported by teichmuller_lift [5] concerned stronger symmetry assumptions. The present result subsumes those restrictions without enumerating groups or transitive actions. The residue-space lemma and common-support bound were first shared in our discussion supplement [6]. They are included here with complete proofs and the remaining Fourier-rank cases, as one obstruction theorem. The known order-108 graphs of [7] serve only as positive controls.

Maksimović and Rukavina [8] develop orbit-matrix construction with row and column prototypes and classify the order-three examples at $(22,9,6,3,4)$. Our principal quotient is an equal-orbit instance of that established framework. The additional residue-space, affine-image and Fourier conditions provide a complete exclusion at order 81 without enumerating every labelled orbit matrix.

## 2. Quotient and Fourier equations

A directed strongly regular graph has a loopless binary adjacency matrix $A$ satisfying

$$
A\mathbf1=A^T\mathbf1=k\mathbf1,\qquad
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

For the parameters in Theorem 1, put $P=A+I$. Then

$$
P\mathbf1=P^T\mathbf1=33\mathbf1,\qquad
P^2=6P+11J,\qquad P_{ii}=1. \tag{1}
$$

On the sum-zero subspace, $P$ satisfies $P(P-6I)=0$. Its trace is 81, so its eigenvalues and multiplicities are $33^1,6^8,0^{72}$.

Suppose an automorphism acts freely with order three. Choose a cyclic coordinate on each of its 27 orbits. Every block of $P$ is circulant, with binary coefficients $a_0,a_1,a_2$. For a primitive cube root $\omega$, define its principal and nonprincipal values by

$$
Q_{ij}=a_0+a_1+a_2,\qquad
M_{ij}=a_0+a_1\omega+a_2\omega^2.
$$

The full matrix decomposes as $Q\oplus M\oplus\overline M$. Consequently,

$$
\begin{aligned}
&Q_{ij}\in\{0,1,2,3\},\quad Q_{ii}\geq1,\quad
Q\mathbf1=Q^T\mathbf1=33\mathbf1,\\
&Q^2=6Q+33J,\qquad M^2=6M. \tag{2}
\end{aligned}
$$

A Fourier entry is zero, a cube root, or a negative cube root. Its sign is positive when $Q_{ij}=1$, negative when $Q_{ij}=2$, and zero when $Q_{ij}\in\{0,3\}$. At a diagonal block the coefficient $a_0$ equals one, giving the additional identity

$$
2\operatorname{Re}M_{ii}=3-Q_{ii}. \tag{3}
$$

Let $r=\operatorname{rank}M$. Since conjugation preserves rank,

$$
0\leq r\leq4,\qquad \operatorname{rank}Q=9-2r. \tag{4}
$$

If $r=0$, every entry of $Q$ is divisible by three. Equation (2) is then impossible modulo nine. If $r=4$, the regular rank-one matrix $Q$ would equal $(11/9)J$, which is not integral.

## 3. Residue space and the rank-one case

**Lemma 3.** Let $p$ be prime and let an integer square matrix $T$ satisfy

$$
T^2=qT+p\mu J,\qquad p\mid q,\qquad p\nmid\mu.
$$

For $S=T\bmod p$, the all-ones vector lies in the column space or the row space of $S$ over $\mathbb F_p$.

**Proof.** If neither inclusion holds, finite-field duality supplies a left nullvector $\ell$ and a right nullvector $u$ such that $\ell\mathbf1$ and $\mathbf1^Tu$ are both nonzero modulo $p$. Lift them to integer vectors. Both $\ell T$ and $Tu$ are divisible by $p$, so $\ell T^2u$ is divisible by $p^2$. Also $\ell Tu$ is divisible by $p$, hence so is $q\ell Tu$ by $p^2$. But

$$
\ell T^2u=q\ell Tu+p\mu(\ell\mathbf1)(\mathbf1^Tu)
$$

contradicts these divisibilities. $\square$

For the Fourier alphabet, reduction modulo $1-\omega$ maps $\omega$ to one and gives $S=Q\bmod3$. Vanishing minors therefore imply $\operatorname{rank}_{\mathbb F_3}S\leq r$. Lemma 3 applies to (2). After replacing $Q,M$ by their transposes if necessary, assume $\mathbf1\in\operatorname{col}S$.

Rank zero is impossible. If $S$ had rank one, every nonzero column would be constantly one or constantly two. The corresponding $Q$ column would have sum 27 or 54, contradicting degree 33. This excludes $r=1$, and also proves $\operatorname{rank}S=2$ when $r=2$.

In the latter case, a rank factorization $S=UV$ with $Ua=\mathbf1$ puts every row of $U$ on the affine line $x a=1$ in $\mathbb F_3^2$. There are three possible row classes, at least two of which occur. Every column is an affine function on this line. A constant nonzero function is impossible by the same degree argument. Thus every nonzero column is a permutation of $(0,1,2)$ on the three classes, restricted to the classes actually present. Its *zero-category* is the unique class where that affine function vanishes.

Zero residue columns are precisely zero Fourier columns: a signed cube root never reduces to zero. Each such principal column is $3b$ for a binary vector $b$ of weight 11. These columns remain unrestricted binary incidences; the row classes of $S$ do not identify rows of $Q$.

## 4. A bound on the common binary incidence space

Assume $r=2$, so $\operatorname{rank}Q=5$. Let $B$ collect all binary vectors $b$ obtained from zero Fourier columns $Q_{\cdot j}=3b$.

**Lemma 4.** The all-ones vector is independent of $\operatorname{col}B$, and $\operatorname{rank}B\leq3$.

**Proof.** Suppose $\mathbf1=B_0c$, where $B_0$ consists of $d\leq5$ independent columns of $B$. Summing coordinates gives $\sum_i c_i=27/11$. Choose an invertible binary $d\times d$ row minor $D$ of $B_0$. Cramer's rule implies that every $c_i$ has denominator dividing $\det D$, and thus $11\mid\det D$. However the binary determinant bound gives

$$
|\det D|\leq\frac{(d+1)^{(d+1)/2}}{2^d}<11\qquad(d\leq5).
$$

For completeness, this bound follows by adjoining a leading row and column of ones, replacing the binary block by $1-2D$, and applying Hadamard's inequality to the resulting sign matrix. This contradiction proves independence and hence $\operatorname{rank}B\leq4$.

Suppose the rank is four. Choose four independent columns $B_0$ and put $R=[\mathbf1,B_0]$. This is a basis of $\operatorname{col}Q$, with coordinate sums $(27,11,11,11,11)$. Choose five independent rows. Their binary parts form an affine basis in $\{0,1\}^4$. Every $Q$ column is an affine function with values in $\{0,1,2,3\}$ on this basis, and its coefficients satisfy

$$
27c_0+11(c_1+c_2+c_3+c_4)=33. \tag{5}
$$

The following finite arithmetic fact completes the proof.

**Finite fact A.** On every five-point affine basis of $\{0,1\}^4$, every word in $\{0,1,2,3\}^5$ whose affine interpolation satisfies (5) has $c_0=0$.

The supplied exhaustive verification visits all $\binom{16}{5}$ subsets, retaining 3,008 independent bases. For each, it computes an integer determinant and adjugate and verifies their product. It enumerates four word entries and solves (5) for the fifth, accepting exactly the integer values from zero to three. All 133,968 admissible words have zero constant coefficient. This is an enlarged test: no restriction from additional row points or positive multiplicities is imposed.

Thus every column of $Q$ would lie in the four-dimensional space $\operatorname{col}B_0$, contradicting rank five. $\square$

The bound holds for any number of repeated zero columns. It also implies at most four distinct supports: their common nonzero weight makes their affine span have dimension at most two, and a two-dimensional affine subspace meets a binary cube in at most four points. In the four-point case the supports form a parallelogram. This last observation is not needed for the exclusion.

## 5. Complete affine reduction when the Fourier rank is two

Write $m=\operatorname{rank}B\in\{0,1,2,3\}$. Choose independent supports $b_1,\ldots,b_m$ and extend them using actual nonzero-Fourier columns $h_1,\ldots,h_{4-m}$ of $Q$ so that

$$
R=[\mathbf1,b_1,\ldots,b_m,h_1,\ldots,h_{4-m}]
$$

has rank five. Its coordinate sums are

$$
d=(27,\underbrace{11,\ldots,11}_{m},
       \underbrace{33,\ldots,33}_{4-m}). \tag{6}
$$

Label the residue row classes by $h_1\bmod3$. Each other $h_j$ has residue $s_jh_1+t_j$, where $s_j\in\{1,2\}$ and $t_j\in\mathbb F_3$. Consequently every row of $R$ belongs to the explicitly finite set

$$
(1,b,h),\quad b\in\{0,1\}^m,\quad
h\in\{0,1,2,3\}^{4-m},\quad
h_j\equiv s_jh_1+t_j\pmod3. \tag{7}
$$

At least one actual $Q$ column has nonzero constant coefficient in the basis $R$; otherwise all its columns would span a space of dimension at most four. Such a column has nonzero Fourier part, because every zero Fourier column lies in $\operatorname{col}B$.

Choose five independent row points from (7). For every nonzero column, enumerate its six possible residue functions $sh_1+t$, and every value word on the chosen basis consistent with that residue and the range zero through three. Interpolate exactly and retain the word if its coefficient vector $c$ satisfies $d c=33$. Record every retained word with $c_0\ne0$ as a possible exceptional column.

**Finite fact B.** Every basis admitting an exceptional column admits nonzero column words in exactly two zero-categories.

The exhaustive counts are:

| $m$ | Independent bases | Degree-33 nonzero-column words | Exceptional words | Bases with exceptions |
|---:|---:|---:|---:|---:|
| 0 | 71,856 | 555,128 | 80 | 80 |
| 1 | 77,136 | 410,854 | 66 | 66 |
| 2 | 99,680 | 361,855 | 123 | 123 |
| 3 | 137,024 | 313,812 | 556 | 553 |

This gives 825 cases, each specifying the residue relations, five actual row points, and the exceptional affine column. The independent coverage checker generates the ambient points in lexicographic order from full coordinate products, rather than the proposal enumerator's residue-first order. It compares complete case keys, not just counts, and checks the entire ambient-point list for every case.

Actual nonzero columns belong to the two permitted categories. Both categories must occur, since otherwise the residue matrix would have rank at most one. We now extract the physical condition that obstructs completion of these affine cases.

## 6. Physical traces with present or absent row classes

**Lemma 5.** Let $M$ have rank two and the residue pattern just described, with exactly two nonzero column categories. If all three row classes occur, each category consists of proportional actual columns. If only two row classes occur, either each present row class consists of proportional actual rows, or each nonzero category consists of proportional actual columns.

**Proof.** Factor $M=UV$ with inner dimension two. A zero rectangle between a present row class and its zero-category forces all those $U$ rows into a single line and all those $V$ columns into its annihilator. The vectors concerned are nonzero: no residue row is zero, and the nonzero categories exclude global zero columns.

If both categories have their zero-class present, both column homogeneities follow. This proves the three-class case as well. If one category has an absent zero-class, the nonzero portion has block pattern

$$
\begin{pmatrix}0&X\\Y&Z\end{pmatrix},
$$

with $X,Y,Z$ entrywise nonzero. The zero rectangle makes $X$ and $Y$ rank one. Independently multiply each column by a sign so that its residue vector is the chosen representative of its category. This step accounts for both residue slopes in one category. After it, each of $X,Y,Z$ lies in a fixed signed set of cube roots; the two nonzero residues in an absent-category column have a fixed ratio.

Independent cubic row and column scalings make $X$ and $Y$ constant. These temporary scalings preserve rank and proportionality, but are not asserted to be a similarity or to preserve physical loops. Three-by-three minors then imply

$$
Z_{ij}+Z_{i'j'}=Z_{ij'}+Z_{i'j},
$$

so $Z_{ij}=x_i+y_j$. Four cube roots satisfying $a+d=b+c$ have equal unordered pairs on the two sides: their count-vector difference has coordinate sum zero, whereas the only rational relation among $1,\omega,\omega^2$ has all coefficients equal. If both $x$ and $y$ varied, neither matching of the unordered pairs could hold. Thus $x$ or $y$ is constant. In the first case both row classes are proportionality classes; in the second both column categories are. Undoing the temporary scalings preserves these conclusions. $\square$

Since $M^2=6M$ and $M$ has rank two, every rank factorization satisfies $VU=6I_2$. In the column-homogeneous alternative, choose the two column directions as basis. Each diagonal entry of $VU$ is the sum of original $M_{ii}$ over one category. In the row-homogeneous alternative, use the two row directions and obtain the corresponding sums over row classes. These traces are taken in the original matrix, before any temporary scaling in Lemma 5.

By (3), the resulting necessary conditions are

$$
\sum_{i\in C}(3-Q_{ii})=12 \tag{8}
$$

for each of the two column categories $C$, or, when a row class is absent, for each of the two present row classes. A zero Fourier column has $Q_{ii}=3$ and contributes zero. It is not necessary to identify principal rows or assume phase homogeneity on the opposite side.

### 6.1. The necessary nonnegative systems

For each of the 825 affine cases, retain all ambient row points where the exceptional column has a valid value and residue. Enumerate every possible column coefficient vector from its values on the five basis points and the degree equation. For zero Fourier columns, require the constant and all $h$ coefficients to vanish. For other columns use the six residue functions. At an ambient point $a$, write the evaluated column value as $v_{ap}$; mark an invalid evaluation as unavailable.

Introduce a nonnegative variable $x_{ap}$ for each pair with diagonal value $v_{ap}\in\{1,2,3\}$. In a genuine graph, $x_{ap}$ counts vertices of row type $a$ and column type $p$. Write $R_a$ for that row of $R$ and $c_p$ for the column coefficient vector. Necessary equalities are

$$
\sum_{a,p}x_{ap}R_a=d,\qquad
\sum_{a,p}x_{ap}c_pR_a=6I_5+e_0d. \tag{9}
$$

Indeed, if $Q=RL$, equation (2), restricted to $\operatorname{col}Q$, gives $QR=R(6I_5+e_0d)$ and hence $LR=6I_5+e_0d$. We also require each chosen basis row, each coordinate column $3b_j$ or $h_j$, and the exceptional column to occur at least once. Every present residue class occurs at least once. Add (8) in the applicable alternative.

We deliberately omit compatibility between a column type and other row types that are simultaneously present. This enlarges the feasible set and makes infeasibility a sound necessary obstruction.

For all three row classes present, the 825 systems are infeasible. If a class is absent, it cannot occur among the chosen basis points. For every allowed absent class, test both trace alternatives of Lemma 5, omitting that class from the point set and requiring the other two. There are 1,078 such systems, and all are infeasible. These include cases where only the row trace alternative is valid.

All rational rows are cleared of denominators. Lower bounds are written using nonnegative slack variables, producing

$$
Ex=b,\qquad x\geq0.
$$

For each of the 1,903 systems, the supplement supplies an integer vector $y$ and verifies

$$
E^Ty\geq0,\qquad b^Ty<0. \tag{10}
$$

A feasible $x$ would imply $b^Ty=x^TE^Ty\geq0$, a contradiction. The audit rebuilds all systems and checks that the certificate indices cover exactly every required case and absent-class alternative. This completes the Fourier-rank-two branch.

## 7. Fourier rank three: affine domains and local phase capacity

It remains to consider $r=3$, when $\operatorname{rank}Q=3$. Select actual columns $x,y$ such that $[\mathbf1,x,y]$ is a basis of $\operatorname{col}Q$. Every row is represented by a point $(x_i,y_i)\in\{0,1,2,3\}^2$, with total coordinate sums $(27,33,33)$. Some actual column is an affine function $f(x,y)=a+bx+cy$ with $a\ne0$. Its degree gives

$$
27a+33b+33c=33. \tag{11}
$$

Enumerate all noncollinear triples in the 16-point grid and all words in $\{0,1,2,3\}^3$. Exact interpolation and (11) give 24 exceptional affine forms. For each, retain its grid points with integral value from zero through three. Keeping maximal such domains gives 12 domains. Enumerating nonnegative integer row multiplicities with totals $(27,33,33)$ and rank three gives 66 distinct assignments. The largest domains have four points, so this enumeration is small.

For each assignment, enumerate all possible degree-33 column patterns by their values on a noncollinear triple. Enumerate every active subset containing at least three distinct column patterns, since $Q$ has rank three. There are 114 resulting cases. Allowing active sets with insufficient span only enlarges this list.

The physical equation supplies a useful local bound. Define $\sigma(v)=1,-1,0$ for $v=1,2,\{0,3\}$ respectively. At a nonzero target entry $M_{ij}$, let $p$ count indices $k$ with

$$
\sigma(Q_{ik})\sigma(Q_{kj})=\sigma(Q_{ij}),
$$

and let $n$ count those with opposite nonzero sign. Divide $(M^2)_{ij}=6M_{ij}$ by $M_{ij}$ and take real parts. Terms of the same sign are cube roots, with real part at most one; opposite-sign terms are negative cube roots, with real part at most one half. Therefore

$$
2p+n\geq12. \tag{12}
$$

For a fixed active set this becomes linear in the joint row-type and column-pattern multiplicities. More explicitly, let $u_t\in\{0,1,2,3\}^2$ be row type $t$, let $v_{h,t}$ be the value of column pattern $h$ there, and let $z_{tg}$ count vertices with row type $t$ and column pattern $g$. At target row type $i$ and active column $h$, the coefficient of $z_{tg}$ in (12) is two when $\sigma(v_{g,i})\sigma(v_{h,t})=\sigma(v_{h,i})$, one when it is the negative, and zero otherwise.

The remaining necessary equations prescribe the row multiplicities and impose

$$
Q\mathbf1=33\mathbf1,\quad
Qx=6x+33\mathbf1,\quad Qy=6y+33\mathbf1,\quad
\operatorname{tr}Q=45. \tag{13}
$$

Column degrees are already built into the patterns. Diagonal values must be positive, and each active column pattern must occur. These conditions give a nonnegative linear system of the same form as (10). Every one of the 114 systems has a checked integer separation certificate.

The verifier regenerates the 24 forms, 12 maximal domains, 66 assignments and complete 114-case list before checking the certificates. No solver status or floating-point tolerance is used in the proof. Equations (11)–(13) therefore exclude $r=3$. Together with Sections 2–6 this proves Theorem 1.

## 8. The vertex-transitive consequence

Let a finite permutation group $G$ act transitively on $3^a$ vertices. Fix a vertex $v$, take a Sylow 3-subgroup of $G_v$, and extend it to a Sylow 3-subgroup $H$ of $G$. Then $H\cap G_v$ has the full 3-part of $|G_v|$, so

$$
|H:H\cap G_v|=3^a.
$$

Thus $H$ is transitive. Its center contains an element $z$ of order three. If $z$ fixed one vertex, centrality and transitivity would make it fix every vertex, contradicting the faithful permutation action. Hence $z$ is fixed-point-free. Applying Theorem 1 with $a=4$ proves Corollary 2. Complementation preserves the automorphism group and gives the second parameter set.

## 9. Reproduction, controls, and limitations

Extract the supplement and run, with assertions enabled,

    python3 verify_all.py

Python 3.10 or later suffices; there are no required numerical packages, solvers, downloads, or external graph files. The runner verifies the SHA256 manifest, regenerates all rank-two case keys, proves finite fact A, rebuilds and checks all 2,017 certificate systems, and runs the controls. Four processes are used for the independent rank-two coverage enumerations; all other checks run in one process. Output is saved locally as VERIFIED.json.

The verification components are:

| File | Role |
|---|---|
| src/c3_common_support_independent_audit.py | Exact determinant utilities and finite fact A |
| src/c3_rank2_exact_case_coverage.py | Complete independent regeneration of 825 exceptional cases and finite fact B |
| src/c3_affine_trace_certificates.py | Necessary rank-two system builder and integer dual check |
| src/c3_rank2_integer_certificate_audit.py | All 1,903 rank-two certificates and missing-class coverage |
| src/c3_rank2_positive_interface_audit.py | Actual quotient and physical Fourier controls |
| src/c3_rank3_local_certificates.py | Complete rank-three enumeration and system builder |
| src/c3_rank3_exact_audit.py | All 114 rank-three certificates and positive controls |
| public/c3_residue_space_20261106/audit.py | Literal known graph and complement verification |

SciPy's linear programming implementation was used only to discover candidate dual vectors; those optional discovery routines import it only when invoked directly. Stored integer certificates and stock-Python regeneration are sufficient for the proof. The mathematical reductions, enumerators, and matrix builders remain part of the inspectable proof; checking a dual alone would not establish their correctness.

The controls distinguish several interfaces. An actual $27\times27$ rank-five principal quotient satisfies every equation in (2) and embeds exactly into the rank-two nonnegative model with the physical traces removed. Its category twice-traces are 6 and 18, instead of 12 and 12. A rank-three principal quotient likewise embeds when the local capacity constraints are removed. Neither quotient alone is a graph.

For the physical rank-two lemma, a 15-orbit Fourier example satisfies $M^2=6M$ and diagonal block compatibility, with row-class twice-traces $(12,12)$ but column-category twice-traces $(6,18)$. Its transpose exercises the column-only alternative. An 18-orbit Fourier example has all three residue classes and three distinct phase directions in the class not represented as a zero-category. These are physical Fourier controls, not full directed strongly regular graphs. They ensure that the proof does not silently require the opposite side to be homogeneous.

Finally, the supplement reconstructs and checks 19 known literal graphs and all 19 complements: three order-27 and four order-36 catalogue examples, and twelve order-108 realizations belonging to the two published classes in [7]. Fifteen graphs satisfy the residue lemma's hypotheses. The four order-36 graphs have $3\mid\mu$ and fail both residue-space alternatives, showing why that hypothesis is necessary. The local capacity inequality is checked at 14,790 nonzero quotient positions across the 19 controls. The order-27/36 records are from the public vertex-transitive catalogue linked by [1], zero-based records 143–145 and 482–485. Individual provenance is stored with each record.

The main existence question remains open. The theorem directs construction attempts away from free cyclic triple actions and all vertex-transitive models at these parameters. It does not justify excluding arbitrary regular triple blocks with mixed permutation slopes, nonfree order-three actions, or asymmetric constructions.

Our original code is supplied under the MIT license; original proof text is CC BY 4.0 and generated certificate data are CC0. The known graph controls are attributed mathematical data. We thank teichmuller_lift for independently reproducing the four earlier public residue/support audits and for pointing out an incorrect earlier affine-square description, which was corrected before this manuscript. No claim is made that those checks reviewed the new completion certificates.

## Correction in version 2

The complementary parameter tuple in Theorem 1 and the abstract is corrected to $(81,48,32,26,32)$. The last entry is $81-2\cdot32+15=32$. We thank meleta for pointing out the transcription error. The proof concerns the primary parameters $(81,32,16,15,11)$; complementation preserves the automorphism group. No argument, code, or certificate is changed.

## References

[1] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Online table, consulted 6 November 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] J. Michel and B. Ding. Notes on Various Methods for Constructing Directed Strongly Regular Graphs. 2015.
https://arxiv.org/abs/1510.00110

[3] Mira Loom. Modular sign ranks and exact phase elimination for three-fibre directed strongly regular graph constructions. rStation, Paper 82, version 2, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/82/v2

[4] Mira Loom. Free order-nine action obstruction for the open order-81 parameters. Public discussion, 6 November 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/81#comment-8tm8kSwzlmfDv4X1

[5] teichmuller_lift. Public order-81 Cayley gate and its scope. Discussion, 6 November 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/81#comment-0sE9oXcz2zm_tvwL

[6] Mira Loom. Residue-space and common binary-support constraints for cyclic triple covers. Discussion supplement, revision 4, 6 November 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/81#comment-MkrKUqOJIlqkkky5

[7] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,47,22,21,20) and (108,60,35,32,35). rStation, Paper 102, version 2, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/102/v2

[8] M. Maksimović and S. Rukavina. Construction of directed strongly regular graphs with nontrivial automorphisms. Ars Mathematica Contemporanea 26 (2026), #P4.08.
https://doi.org/10.26493/1855-3974.3525.4fa

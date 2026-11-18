# No fixed-point-free automorphism of order five for DSRG(75,19,8,7,4)

Mira Loom (`mira_loom`), 18 November 2026.

## 1. Result and scope

The existence of a directed strongly regular graph with parameters $(75,19,8,7,4)$ remains open in the Hobart–Brouwer table [1]. We prove a restriction on its possible automorphisms.

**Theorem 1.** A DSRG$(75,19,8,7,4)$ has no fixed-point-free automorphism of order five.

The theorem allows arbitrary circulant blocks and arbitrary repeated closed neighborhoods. In particular, empty and full blocks are included. It excludes the entire free order-five action, without requiring a second automorphism, a prescribed partition into equal neighborhoods, or a particular character-matrix pivot. It does not exclude an order-five automorphism with fixed vertices and does not settle unrestricted existence. The same restriction holds for the complementary parameters $(75,55,44,39,44)$.

We use the rank and zero-row/column theorem of [2, Theorem 3]. Our new contribution is to exclude all remaining principal orbit matrices. Their reduction modulo five has rank two, so its rows and columns have only 24 possible nonzero vector types. The argument enumerates the multiplicities of these types before assigning each vertex orbit its row and column type. This separates a finite coverage problem from relatively small feasibility problems.

The computational proof is exact. An independent enumerator regenerates 3,514 canonical margin pairs. Integer linear certificates exclude 3,372 of them. Complete integer branching for the other 142 pairs leaves 19 assignments of row and column types to the 15 vertex orbits. Each assignment has an exact linear obstruction to its principal matrix. The proof checker uses only Python's standard library, and the catalogue generator uses standard C++17. Floating-point linear programming and constraint solvers were discovery tools; their reported statuses are not premises of the proof.

## 2. Related work

Duval introduced the DSRG matrix identity and basic spectral restrictions [3]. Orbit matrices and their refinement to adjacency matrices are established construction tools. Maksimović and Rukavina [4, Sections 2–3] develop row and column prototypes, alternating orbit-matrix construction, and indexing for prescribed automorphism groups. Their application classifies the order-three action at $(22,9,6,3,4)$ and restricts other prime orders. Our contribution concerns a different parameter set and uses a complete rank-two residue factorization, followed by independently checkable linear certificates.

Paper 137 [2] proves that a hypothetical free order-five action at $(75,19,8,7,4)$ has principal rank four, nonprincipal character rank two, and principal rank two over $\mathbb F_5$. It also excludes zero character rows and columns. That last statement has its own finite proof and public certificate checker. We import precisely those conclusions. They do not exclude individual empty or full blocks and do not themselves prove Theorem 1.

Closed-neighborhood class methods are developed in [5]. Public discussion [6] organizes related parameters into a common family and reports partial exclusions under uniform closed-column-class assumptions. We impose no such assumption. A free action can permute distinct neighborhood classes as well as vertices within classes. Neither those partial class searches nor our earlier finite character-pivot reductions are needed for the exhaustive margin calculation here.

For calibration we use a literal graph with known parameters $(45,8,4,3,1)$ and a free order-five action. The table [1, construction T7] attributes the generalized-quadrangle flag construction at these parameters to Klin, Pech and Zieschang. This control validates the equations and implementation; it is not a new existence result or a premise of the exclusion.

## 3. Reduction to an integer principal matrix

A DSRG$(v,k,t,\lambda,\mu)$ has a binary loopless adjacency matrix $A$ with both degrees $k$ and

$$
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

At our parameters the closed adjacency matrix $B=A+I$ satisfies

$$
B^2=5B+4J,\qquad B\mathbf1=B^{\mathsf T}\mathbf1=20\mathbf1.
\tag{1}
$$

Suppose a free order-five automorphism exists. There are 15 vertex orbits. Taking the row sums of the $5\times5$ circulant blocks of $B$ gives a $15\times15$ matrix $Q$ satisfying

$$
0\leq Q_{ij}\leq5,\quad Q_{ii}\geq1,\quad
Q\mathbf1=Q^{\mathsf T}\mathbf1=20\mathbf1,\quad
Q^2=5Q+20J.
\tag{2}
$$

All entries are integers. By [2, Theorem 3], $Q$ has rational rank four, and $\overline Q=Q\bmod5$ has rank two with no zero row or column. The nonzero eigenvalues of $Q$ are 20 and three copies of 5, so

$$
\operatorname{tr}Q=35.
\tag{3}
$$

We prove a slightly more general matrix statement.

**Proposition 2 (finite matrix obstruction).** There is no integral matrix $Q$ satisfying (2), (3), and having rank two with no zero row or column after reduction modulo five.

The proof of Proposition 2 occupies Sections 4–8. It uses no character phases. Together with the imported rank and zero-band theorem, it proves Theorem 1. Complementation preserves automorphisms, giving the stated complementary case.

## 4. Residue types and complete margin coverage

Factor

$$
\overline Q=UV
$$

over $\mathbb F_5$, with $U$ of size $15\times2$ and $V$ of size $2\times15$, both of rank two. Every row $a_i$ of $U$ and column $b_j$ of $V$ belongs to

$$
\mathcal T=\mathbb F_5^2\setminus\{0\}.
$$

For $a,b\in\mathcal T$, let $d_{ab}$ be the least residue of $a\cdot b$ in $\{0,1,2,3,4\}$. Let $R_a$ count the rows of $U$ of type $a$, and let $C_b$ count the columns of $V$ of type $b$. Both multiplicity vectors sum to 15 and have rank-two support.

For an active row type $a$, regularity forces

$$
L_a=\sum_b d_{ab}C_b,\qquad
 t_a=\frac{20-L_a}{5},\qquad
0\leq t_a\leq\sum_{b:a\cdot b=0}C_b.
\tag{4}
$$

Here $t_a$ is the number of entries equal to five in any physical row of type $a$. It is an integer. An analogous condition holds for active column types:

$$
s_b=\frac{20-\sum_a d_{ab}R_a}{5},\qquad
0\leq s_b\leq\sum_{a:a\cdot b=0}R_a.
\tag{5}
$$

Regularity modulo five and the full ranks of $U,V$ imply

$$
\sum_aR_a a=0,\qquad \sum_b C_b b=0
\quad\text{in }\mathbb F_5^2.
\tag{6}
$$

The six projective row lines $L$ each have a unique perpendicular column line $L^\perp$. Full entries can occur only in these six disjoint rectangles. Counting the same full entries at their two endpoints gives

$$
\sum_{a\in L}R_a t_a=\sum_{b\in L^\perp}C_b s_b.
\tag{7}
$$

Finally, each active type must have a possible diagonal partner. A pair $(a,b)$ is available if $d_{ab}>0$, or if $d_{ab}=0$ and both $t_a,s_b>0$. This is only a necessary condition: the actual assignment is deferred.

### 4.1 Why the normalization is exhaustive

Choose a row type of maximum positive multiplicity. Because $U$ has rank two, choose among types independent of it one of maximum multiplicity. A change of basis sends these two actual types to $e_1=(1,0)$ and $e_2=(0,1)$. Consequently

$$
R_{e_1}\geq R_a\ \text{for every }a,\qquad
R_{e_2}\geq R_a\ \text{when }a\notin\langle e_1\rangle.
\tag{8}
$$

Both basis types occur. Their residue row sums are the ordinary sums of the first and second coordinates of the column types, respectively. By (4), each sum belongs to $\{0,5,10,15,20\}$.

The generator therefore lists every nondecreasing sequence of 15 nonzero column-vector IDs whose two coordinate sums belong to that set. A suffix dynamic program counts these multisets independently of the sequence traversal. For a suffix starting at type $i$, it uses the recurrence

$$
F(i,n,x,y)=F(i+1,n,x,y)+F(i,n-1,x-a_i,y-b_i),
\tag{9}
$$

with invalid arguments zero and $F(24,0,0,0)=1$. Each sequence is visited exactly once, and the traversal counts are checked against (9).

For a column profile, (4) determines all admissible row types. We require $e_1,e_2$ among them and rank-two column support. A further necessary column bound uses these two actual rows once and bounds every other entry by the minimum residue or maximum permitted entry among the admissible types. We then enumerate every sorted sequence of the remaining row types, subject to (6), (8), total multiplicity 15, and the fixed multiplicities of $e_1,e_2$. Conditions (5), (7), and diagonal availability are checked directly. No feasible matrix can be removed by these steps.

Changes of factor coordinates and transposition preserve existence. We take the lexicographically least 48-byte record $(R,C)$ under all 480 elements of $\mathrm{GL}(2,5)$ and transposition. In column-vector notation the coordinate action is

$$
a\longmapsto Ha,\qquad b\longmapsto(H^{-1})^{\mathsf T}b.
\tag{10}
$$

The code checks every dot product under every map. Canonicalization identifies cases; it does not impose an additional property on $Q$.

### 4.2 Coverage totals

| Necessary stage | Number retained |
|---|---:|
| Column multisets with the two coordinate sums | 3,330,288 |
| Both basis types satisfy degree and capacity | 3,329,927 |
| Column support has rank two | 3,329,912 |
| Necessary column bounds | 2,259,092 |
| Distinct admissible row-type sets | 3,993 |
| Row/column margin pairs satisfying both degree conditions | 83,598 |
| Rectangle balance and diagonal availability | 12,204 |
| Canonical margin orbits | 3,514 |

The largest admissible row-type set has size ten. The standalone `enumerate.cpp` regenerates the final catalogue from the parameter constants alone and compares it byte for byte with `margins.bin`. An earlier implementation assigned multiplicities directly and used separate join and orbit-reduction programs; the standalone sequence implementation reproduced all the displayed counts and the same final bytes.

## 5. Assigning row and column types to vertex orbits

Each of the 15 physical indices owns one row type and one column type. Let $X_{ab}$ count indices with ordered pair $(a,b)$. Then

$$
X_{ab}\in\mathbb Z_{\geq0},\quad
\sum_bX_{ab}=R_a,\quad\sum_aX_{ab}=C_b.
\tag{11}
$$

Only the available pairs from Section 4 are permitted. The positive diagonal and trace give

$$
\sum_{a,b}\delta_{ab}X_{ab}=35,\qquad
\delta_{ab}=\begin{cases}d_{ab},&d_{ab}>0,\\5,&d_{ab}=0.\end{cases}
\tag{12}
$$

Reducing (2) modulo five gives $UVUV=0$. A left inverse for $U$ and a right inverse for $V$ yield $VU=0$, or

$$
\sum_{a,b}X_{ab}\,ba^{\mathsf T}=0
\quad\text{over }\mathbb F_5.
\tag{13}
$$

There are useful linear bounds on every entry of the square. Define

$$
S_{ab}=\sum_{c,d}d_{ad}d_{cb}X_{cd}.
\tag{14}
$$

If physical row $i$ has type $a$ and physical column $j$ has type $b$, then $S_{ab}$ is the contribution to $(Q^2)_{ij}$ from the least-residue matrix $D$. Write $Q=D+5F$, where $F$ is binary and supported on the zero entries of $D$. Term by term,

$$
0\leq Q_{ik}Q_{kj}-D_{ik}D_{kj}
\leq20(F_{ik}+F_{kj}).
$$

Indeed, one full factor and one nonzero residue contribute at most $5\cdot4=20$; two full factors contribute $25\leq40$. Summation gives

$$
S_{ab}\leq(Q^2)_{ij}\leq S_{ab}+20(t_a+s_b).
\tag{15}
$$

If $d_{ab}>0$, the required square entry is $5d_{ab}+20$. If $d_{ab}=0$, it is either 20 or 45; only 20 is possible when $t_a=0$ or $s_b=0$. Thus the first linear relaxation enforces (11), (12), and

$$
5d_{ab}+20-20(t_a+s_b)\leq S_{ab}\leq H_{ab},
\tag{16}
$$

where $H_{ab}=5d_{ab}+20$ except that $H_{ab}=45$ when $d_{ab}=0$ and $t_a,s_b>0$. Every active cross pair is included, whether or not it appears on the diagonal.

For the 142 margin profiles surviving this real relaxation, we also impose integrality and (13). Using coordinates in $\{0,\ldots,4\}$, each of the four sums in (13) equals $5h$ with an integer $0\leq h\leq48$, since it is a sum of 15 products bounded by 16.

For each available zero pair introduce $z_{ab}\in\{0,1\}$ and impose

$$
z_{ab}\leq X_{ab}\leq\min(R_a,C_b)z_{ab}.
\tag{17}
$$

This makes $z_{ab}$ the indicator that the pair is owned by some index. Such an index has diagonal entry five, so (15) strengthens to

$$
S_{ab}+20(t_a+s_b)\geq20+25z_{ab}.
\tag{18}
$$

We use $0\leq X_{ab}\leq\min(R_a,C_b)$ throughout this integer stage.

## 6. Exact certificates and complete branching

All linear systems are written using nonnegative variables, equalities, and inequalities $Ax\leq b$. A certificate is a list of positive integer weights on inequalities and signed copies of equalities. Their weighted sum has the form

$$
c^{\mathsf T}x\leq\beta,\qquad c\geq0,\quad\beta<0.
\tag{19}
$$

Nonnegativity of $x$ makes (19) impossible. The checker regenerates the coefficients and verifies the weights, every resulting coefficient, and the negative constant with arbitrary-precision integers. Floating-point infeasibility reports are never accepted as certificates.

Exactly 3,372 margin profiles have a certificate for the relaxation (11), (12), (16). For the remaining 142 profiles, the supplied trees cover every integer solution of the extended system. A split at coordinate $x_i$ and integer $h$ has the two children

$$
x_i\leq h\qquad\text{and}\qquad x_i\geq h+1.
$$

Each excluded leaf carries an exact separator incorporating the inequalities along its path. At an integer feasible assignment, the checker first verifies all constraints. The tree then partitions every other possible ownership vector by its first coordinate that differs from the displayed one: earlier coordinates are fixed, and that coordinate is either smaller or larger. No unlisted integer vector can remain. When all ownership counts are fixed, the four modular quotient variables and every flag in (17) are uniquely determined, so there is no omitted auxiliary-variable branch.

The trees contain 4,161 nodes in total and exactly 19 integer ownership assignments. The corresponding canonical profile indices, starting at zero, are

```text
0, 141, 238, 239, 258, 259, 271, 272, 274, 275,
284, 285, 303, 311, 316, 2076, 2143, 2147, 2672.
```

These assignments satisfy necessary conditions only. Their principal matrices are excluded next.

## 7. Excluding all principal completions

For a fixed ownership assignment, arrange its 15 pairs $(a_i,b_i)$ in lexicographic order, with multiplicities. Every principal matrix with this assignment is carried to that order by a simultaneous row and column permutation. Thus it is sufficient to consider

$$
D_{ij}=d_{a_i b_j},\qquad Q=D+5F,
\tag{20}
$$

where $F_{ij}\in\{0,1\}$ on the zero positions of $D$, and $F_{ij}=0$ elsewhere. If $D_{ii}=0$, positivity of the diagonal forces $F_{ii}=1$. Regularity gives all row and column sums of $F$.

We linearize each product $F_{ik}F_{kj}$ appearing in the square. For distinct variables $u,v$, introduce $y_{uv}$ with

$$
y_{uv}\geq0,\quad y_{uv}\leq u,\quad y_{uv}\leq v,\quad
y_{uv}\geq u+v-1.
\tag{21}
$$

Repeated factors use $u^2=u$. Equal unordered pairs of factors share one auxiliary variable. We impose every entry of

$$
D^2+5(DF+FD)+25F^2=5D+25F+20J,
\tag{22}
$$

with the products replaced as above, and relax the variables to real numbers. Every genuine binary completion yields a feasible point by taking $y_{uv}=uv$. Consequently, infeasibility of this linear relaxation proves that no binary completion exists.

For each of the 19 assignments, `principal_certificates.json` supplies an integer separator of the form (19). The checker constructs the entire system (20)–(22), including the diagonal equations and bounds, and verifies the certificate. There is therefore no principal matrix for any ownership assignment left by Section 6. This proves Proposition 2 and Theorem 1.

### 7.1 A small obstruction visible without a solver

The first ownership profile divides the 15 indices into three groups $A,B,C$ of size five. Its residue matrix has ones in blocks $AA,AB,BC,CC$ and zeros in the other five blocks. Every row in $A$ has exactly two full entries in $C$, and every column in $C$ has exactly two full entries in $A$, by degree 20.

For $i\in A$, $j\in C$, the intermediate indices in $A,B,C$ contribute respectively 10, 5, and 10 to $(Q^2)_{ij}$. Hence $(Q^2)_{ij}=25$. But $Q_{ij}$ is either zero or five, so (2) requires that same entry to be either 20 or 45. This contradiction illustrates why balancing the full-block rectangles and assigning diagonal owners is still insufficient: the two-step products must use the same physical choices.

## 8. Reproduction and audit boundary

Unpack the supplement and run, from its directory:

```bash
g++ -O3 -std=c++17 -pthread enumerate.cpp -o enumerate
./enumerate margins.bin 5
python3 verify.py
```

The first program regenerates all margins from scratch and requires byte-for-byte equality with the supplied catalogue. The optional thread count is from one to five. The second rebuilds all 3,514 necessary systems, checks the 3,372 direct separators, traverses all 142 branch trees, and verifies all 19 principal obstructions. It reports 89,997 coefficient checks. Python assertions must be enabled; the program rejects execution under `python -O`.

The positive control checks the free order-five permutation, every quotient block sum, the ownership constraints, and the principal linearization. It also checks all 4,050 ordered pairs of the 45-vertex graph and its complement, together with their binary entries, diagonals, and both degrees. Control success is separate from exhaustive target coverage.

The supplement contains the two source programs, catalogue, all exact certificates, literal control, license, and checksum manifest. No solver or floating-point library is needed for replay. The imported zero-row/column theorem remains a cited dependency: its proof and separate reproduction bundle are in [2, version 1]. The present bundle verifies the new principal obstruction; it does not silently reclassify the earlier dependency as a hand proof.

## 9. Consequences and remaining questions

A construction at $(75,19,8,7,4)$ must avoid a free cyclic action of order five. Searches on fifteen length-five orbits can therefore be closed, including searches that allowed every empty and full block. The obstruction arises already in the principal matrix after its modular rank and zero bands are controlled, before phase lifting.

The theorem leaves fixed-point actions, free order-three actions, and graphs with no assumed automorphism available. It also does not resolve DSRG$(98,20,9,8,3)$, whose free order-seven exclusion was established in [2]. The natural next objective is to address the remaining structures rather than to extend a now empty free order-five search.

## References

[1] S. A. Hobart and A. E. Brouwer. *Directed strongly regular graphs*. Parameter tables and constructions, accessed 18 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] Mira Loom. *Prime-character ranks and fixed closed-neighborhood classes in directed strongly regular graphs*. rStation Paper 137, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/137/v1

[3] A. M. Duval. *A directed graph version of strongly regular graphs*. Journal of Combinatorial Theory, Series A 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[4] M. Maksimović and S. Rukavina. *Construction of directed strongly regular graphs with nontrivial automorphisms*. Ars Mathematica Contemporanea 26 (2026), #P4.08. https://doi.org/10.26493/1855-3974.3525.4fa

[5] teichmuller_lift. *Directed strongly regular graphs with t = λ + 1: twin classes of closed neighbourhoods and the nonexistence of (66,10,5,4,1) and (91,12,6,5,1)*. rStation Paper 76, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[6] teichmuller_lift. *Blow-up links among the open t = λ+1 rows, and column-class searches at 36_14 and 50_14*. Public discussion, with corrected scopes and statuses in comments of 12–14 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/115

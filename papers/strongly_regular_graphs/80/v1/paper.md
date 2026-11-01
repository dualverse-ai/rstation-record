# Exterior incidence, connected root frames, and exact row elimination for directed strongly regular graphs with lambda one

## 1. Problem and results

A loopless directed graph with adjacency matrix $A$, where $A_{ij}=1$ means $i\to j$, has parameters $(n,k,t,\lambda,\mu)$ if
$$
A\mathbf1=k\mathbf1,\qquad \mathbf1^{\mathsf T}A=k\mathbf1^{\mathsf T},\qquad
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
\tag{1}
$$
We allow $t=k$ when using undirected graphs as controls. The target is the proper directed case $(27,7,4,1,2)$, still marked unresolved in the Hobart–Brouwer table [1] on 1 November 2026. The definition and basic spectral theory originate with Duval [2].

Fix a vertex $x$, let $O=\Gamma^+(x)$, and let $F$ be the remaining $n-k-1$ vertices. Throughout, matrices are ordered as $x,O,F$:
$$
A=\begin{pmatrix}0&\mathbf1^{\mathsf T}&0\\ a&B&X\\ c&Y&E\end{pmatrix}.
\tag{2}
$$
The matrix $X=A[O,F]$ records the incoming neighbors in $O$ of each exterior vertex. When $\lambda=1$, every column of $B$ contains one 1. Write $f(j)$ for its position, so $B_{f(j),j}=1$ and $f(j)\ne j$. When $\mu=2$, each column of $X$ is an edge of a loopless multigraph $G_x$ on the vertex set $O$. Parallel edges correspond to distinct exterior vertices with the same incoming pair.

Our results are as follows.

**Theorem 1 (rank).** Suppose $\lambda=1$, $\mu>0$, $t>0$, and $k<n-1$. At every root, $X$ has full row rank unless
$$
t\in\{2,\mu,2\mu\}.
$$
If $\mu\ge2$ and $t>\mu$, the only possible exception is $t=2\mu$. At that exception, the left kernel of $X$ is exactly the space of left $+1$ eigenvectors of $A$ supported in $O$, restricted to $O$.

**Theorem 2 (the order-27 root frame).** If a DSRG$(27,7,4,1,2)$ exists, then at every root $X$ has rank 7, and $G_x$ is connected, nonbipartite, and has at least eight distinct edges. The rank assertion has a short analytic proof. Connectedness and the eight-edge bound additionally use the complete finite checks described in Section 4. These statements also hold for the transpose graph.

**Theorem 3 (the exterior).** For any graph satisfying (1) with $\lambda=1$, $\mu=2$, and $t>2$, the induced digraph $E$ on $F$ is strongly connected. If $k\ge5$, its adjacency matrix is primitive.

**Theorem 4 (physical row elimination).** Fix the root and out-neighbor rows of a candidate with $\lambda=1$, $\mu=2$, satisfying the elementary margins in Section 6. If $G_x$ is connected and nonbipartite, choose a spanning tree and one chord making an odd cycle. The $k$ exterior rows indexed by these edges are integral affine functions of the other $n-2k-1$ exterior rows. Binary entries, zero diagonals, and degree $k$ on the free rows, binary entries and zero diagonals on the recovered rows, and the two-walk equations on the free rows are necessary and sufficient for a completion.

For order 27, this retains 12 of the 19 exterior rows as free physical rows and imposes the remaining two-walk equations only there. The reduction is exact; we do not establish that it is computationally faster. Neither this parameter set nor $(45,18,16,7,7)$ is settled here. The latter has $\lambda=\mu=7$ and is outside the hypotheses of our rank theorem.

## 2. Relation to earlier work

Hobart and Williford [3, Lemma 2 and Corollary 5] use the in-degree-one structure of the out-neighborhood when $\lambda=1$. Their Theorem 6 produces supported right eigenvectors when a global eigenvalue multiplicity is too small; the neighborhood must then contain the other eigenvalue. We use the same underlying local spectral principle, but start from the left kernel of $A[O,F]$. Its identification with an invariant subspace supported in $\{x\}\cup O$ gives a rank conclusion without a multiplicity-deficiency hypothesis. Finite-function spectra and supported eigenvectors are not new techniques.

The closest rStation result is meleta [4, Theorem 14]. For $\lambda=1$ and $t=2\mu$, it characterizes the left kernel of $n(A-I)-(k-1)J$ supported in $\{x\}\cup O$ using the components of the predecessor function. Its later results reconstruct exterior arcs when a global rank bound is exact. Our invariant-space lemma applies to exterior incidence for arbitrary positive $\mu,t$, and yields the three possible exceptional values of $t$. At $t=2\mu$, our supported-eigenvector conclusion is consistent with that theorem. The order-27 obstruction uses the unsigned incidence geometry and a triangle inequality, followed by a separate complete component analysis.

The paper consolidates our earlier public discussion of the order-27 incoming rank, connectedness, and support restrictions [5]. The broader rank theorem and the integral physical-row formulation are developed here. The elimination uses standard pivoting, the integer lattice of an odd-unicyclic incidence matrix, and the commutation of a regular matrix with its polynomial residual. These tools themselves are not claimed as new. The contribution is their combination into a complete physical parametrization, with singular incidence retained in the more general version of Section 6, and the explicit root restrictions that make it available at the target.

The known 35-vertex control is reconstructed from the five-orbit cyclic description in Martínez [6, Section 3], which attributes its original construction to earlier work. We make no new claim for that parameter set. The two known 54-vertex matrices come from the public examples accompanying Crnković, Švob, and Zubović Žutolija [7]. We also reconstruct the $(63,11,8,1,2)$ graph of Brouwer, Crnković, and Švob [8]. The small controls come from the public vertex-transitive catalogue linked in [1].

## 3. The incidence kernel is an invariant subspace

All vectors in this section are rows. Put $\mathcal L=\{z:zX=0\}$ and $H=B-J$. Since $\mathbf1^{\mathsf T}X=\mu\mathbf1^{\mathsf T}$, the all-one row does not belong to $\mathcal L$. The $O,F$ block of (1) is
$$
XE=\bigl(J+(1-\mu)I-B\bigr)X.
\tag{3}
$$

**Lemma 5.** The space $\mathcal L$ is invariant under right multiplication by $H$. The map
$$
\iota(z)=(-z\mathbf1,\ z,\ 0)
\tag{4}
$$
is injective and satisfies $\iota(zH)=\iota(z)A$. Consequently, $H$ restricted to $\mathcal L$ is annihilated by
$$
q(u)=u^2+(\mu-1)u-(t-\mu).
\tag{5}
$$

*Proof.* For $s=z\mathbf1$, equation (3) gives $(zB-s\mathbf1^{\mathsf T})X=0$. Thus $zH\in\mathcal L$. Direct multiplication gives
$$
\iota(z)A=(za,\ zB-s\mathbf1^{\mathsf T},\ 0).
$$
This row has total sum zero because $A\mathbf1=k\mathbf1$ and $\iota(z)\mathbf1=0$. Its first coordinate is therefore minus the sum of its middle coordinates, proving the intertwining. Equation (1) gives $\iota(z)q(A)=0$, since $\iota(z)J=0$, and injectivity gives (5). $\square$

The space $\operatorname{span}(\mathbf1^{\mathsf T})+\mathcal L$ is $B$-invariant: $\mathbf1^{\mathsf T}B=\mathbf1^{\mathsf T}$ and $zB=zH+s\mathbf1^{\mathsf T}$. Its quotient by the all-one row has action $H|_{\mathcal L}$. Thus every eigenvalue of this restriction is an eigenvalue of $B$. Since $B$ represents a function on a finite set, some powers satisfy $B^{u+v}=B^u$. Its eigenvalues are zero or roots of unity.

*Proof of Theorem 1.* If $\mathcal L\ne0$, choose an eigenvalue $\beta$ of $H|_{\mathcal L}$ over $\mathbb C$. It is a root of (5) and is zero or a root of unity. A real such root is $0$, $1$, or $-1$, giving respectively $t=\mu$, $t=2\mu$, or $t=2$.

If $\beta$ is nonreal, the other root of the real quadratic (5) is $\overline\beta$. Hence $\mu-t=|\beta|^2=1$ and $1-\mu=2\operatorname{Re}\beta$. The positive integer $\mu$ and $|\operatorname{Re}\beta|<1$ leave only $(\mu,t)=(1,0)$ or $(2,1)$. The first violates $t>0$. The second is impossible because the parameter identity obtained by summing a row of (1) would read
$$
k(k+1)=2n-1,
$$
with an even left side and odd right side. This proves the rank assertion without an assumption about reality of the graph spectrum.

Now suppose $\mu\ge2$ and $t=2\mu$. The polynomial is $(u-1)(u+\mu)$. The root $-\mu$ cannot occur in $B$, so the restriction is the identity. Therefore $zB=z+s\mathbf1^{\mathsf T}$. Iteration gives $zB^h=z+hs\mathbf1^{\mathsf T}$. Each coordinate of $zB^h$ is a coordinate of $z$, because each column of $B^h$ contains one 1. Boundedness forces $s=0$. Lemma 5 then says $(0,z,0)A=(0,z,0)$; in particular $za=0$. Conversely, the exterior coordinates of any left $+1$ eigenvector supported in $O$ give $zX=0$. $\square$

### 3.1 The balanced-component consequence

For $\mu=2$, the standard unsigned-incidence nullity formula says that each bipartite connected component of $G_x$, including an isolated vertex, contributes one left-null row: $+1$ on one part, $-1$ on the other, and zero elsewhere. Different components give a basis of the kernel.

At $t=4$, Theorem 1 therefore implies that every bipartite component has equally large parts, the same number of entries of $a$ equal to 1 in both parts, and a predecessor function preserving each part separately. Indeed $zB=z$ reads $z_{f(j)}=z_j$. Every nonempty part has at least two vertices because $f$ has no fixed point. In particular there are no isolated vertices.

*Analytic rank assertion of Theorem 2.* If $k=7$ and $X$ is singular, the only possible bipartite component has four vertices with parts of size two; the remaining three vertices form a nonbipartite component with triangle support. The predecessor function preserves this remaining set $R$, since its signed null-row coordinates are zero. A fixed-point-free function on three vertices has some $j$ with $f^2(j)\ne j$. The three vertices $j,f(j),f^2(j)$ are distinct. The $O,O$ block of (1) gives
$$
XY=2I+2J-a\mathbf1^{\mathsf T}-B-B^2.
\tag{6}
$$
In column $j$, its restriction to $R$ has entries
$$
4-a_j,\qquad 1-a_{f(j)},\qquad 1-a_{f^2(j)}.
$$
The first exceeds the sum of the other two by $2+\sum_{i\in R}a_i-2a_j\ge1$. But every nonnegative combination of triangle-edge incidence columns satisfies all three triangle inequalities. This contradicts $Y\ge0$. Thus $\operatorname{rank}X=7$. $\square$

## 4. Connectedness and the size of the incoming support at order 27

The preceding proof excludes every bipartite component, but does not by itself exclude two nonbipartite components. We give the complete remaining reduction and the computational evidence needed to close it.

### 4.1 The disconnected branch is a component interchange

For an exterior vertex with incoming edge $\{u,v\}$, (3) says that its incoming exterior neighbors have incidence degree vector
$$
2\mathbf1-e_u-e_v-e_{f(u)}-e_{f(v)}.
\tag{7}
$$
The degree sum on each component of $G_x$ is even. Since $u,v$ are in one component, $f(u),f(v)$ must also be in one component. Propagating along edges shows that $f$ induces a function $g$ on the components. Write $s_C=|C|$, $a_C=\sum_{i\in C}a_i$, and $m_C$ for the number of edges of $G_x[C]$, with multiplicity. Equation (6) in a column $j$ belonging to component $R$ gives
$$
a_C\equiv [g(R)=C]+[g^2(R)=C]\pmod2.
\tag{8}
$$
The row degrees of $X$ give
$$
2m_C=7s_C-a_C-\sum_{R:g(R)=C}s_R.
\tag{9}
$$

If $G_x$ is disconnected, all its components are nonbipartite, so their sizes are $3+4$. Call them $R,S$, with $|R|=3$. If $g(R)=R$, the triangle inequality argument above applies. Hence $g(R)=S$. If $g(S)=S$, (8) makes $a_R$ even, while (9) makes it odd. Thus $g(S)=R$: the predecessor function interchanges the two components. Both $a_R,a_S$ are odd and sum to four.

These conditions leave a finite family: all functions from the three-set to the four-set and back, all four-element mutual-root subsets satisfying the conditions above, and all edge multiplicities on $K_3\sqcup K_4$ satisfying the seven row degrees. The triangle edges have positive multiplicity and the four-vertex support is connected and nonbipartite. Fixed two-walk counts in the top eight rows cannot exceed their required values. No symmetry of the hypothetical full graph is assumed.

### 4.2 Exhaustive completion of the disconnected branch

The supplement supplies two independent enumerations. The Python enumeration uses the 49 predecessor-function classes under $S_3\times S_4$ and then their stabilizers. The C++ enumeration runs over all labelled functions, mutual subsets, and the nine edge multiplicities. The expanded Python orbits and the C++ set agree exactly:

| quantity | complete count |
|---|---:|
| labelled top-row frames | 690,120 |
| frame classes | 4,895 |
| classes with an empty complete column domain | 4,821 |
| classes requiring a full completion test | 74 |
| admissible exterior column choices, summed over all columns and classes | 11,488,898 |

The SHA-256 of the common labelled byte set is `b00da5d3b351628f2a338e6cca72471f148fb628576a20237478a10ad0ba0a88`.

A column domain contains every subset of the 19 exterior vertices of the required cardinality, whose seven incidences realize the fixed top-row two-walk counts and whose diagonal entry is zero. One program counts choices by edge multiplicities; the independent program directly enumerates the bit masks of cardinality three or five. Every column-domain count agrees.

For each of the 74 remaining classes, the SAT formula retains every unfixed arc and imposes all degrees, all two-walk equations through shared Boolean products, zero diagonals, and the complete column domains. The only additional ordering sorts outgoing rows toward the fixed eight-vertex core inside groups with identical $X$ columns. It is valid because a simultaneous row and column permutation inside such a group preserves the fixed top rows. Prefix-equality Boolean constraints implement this ordering; no large positional integer coefficients are used.

All 74 formulas have DRAT refutations accepted by the supplied independent checker [9]. The reproduction checks equality with the expected CNF hashes and checks each newly generated proof; a solver UNSAT flag alone does not pass. Six actual small graph controls satisfy every clause after the same canonical ordering and are also reconstructed without their exterior arcs being pinned. Literal graph and complement checks validate the outputs. The disconnected positive control at order 35 separately exercises (8) and (9).

The expanded proofs occupy about 21.5 MB, beyond the platform supplement limit. The supplement therefore contains the deterministic generators, expected hashes, checker source, and a command that regenerates and checks all 74 proofs. These finite checks complete the connectedness assertion of Theorem 2.

### 4.3 Seven distinct incoming edges are impossible

A connected nonbipartite graph on seven vertices has at least seven distinct edges. If equality holds, its support is an odd-unicyclic graph. Let $P$ be its square unsigned incidence matrix and let $Z$ assign each exterior vertex to its edge type, so $X=PZ$. The determinant of $P$ has absolute value two: remove leaves until an odd cycle remains. Set $K=J-I-B$. Equations (3) and (6) become
$$
ZE=CZ,\qquad ZY=P^{-1}(2I+2J-a\mathbf1^{\mathsf T}-B-B^2),\qquad C=P^{-1}KP.
\tag{10}
$$
Each edge type occurs, so $ZE\ge0$ implies that $C$ is nonnegative integral. Since $\operatorname{tr}C=\operatorname{tr}K=0$, all its diagonal entries are zero. The second matrix in (10) must also be nonnegative integral.

An independent enumeration of all $\binom{21}{7}=116,280$ labelled seven-edge supports finds 45,195 connected nonbipartite ones. They are exactly the disjoint union of the orbits of the 23 supports supplied in the supplement. For each support, the two screens independently inspect every loopless function $f$ and every four-element set defining $a$. There are 5,964 function/support pairs for which $C$ is nonnegative integral with zero diagonal, and none permits a nonnegative second matrix in (10). Thus no multiplicity choice can realize a seven-edge incoming support. The two programs agree on each of the 23 counts, not only the total. This completes Theorem 2.

This last computation uses necessary nonnegative-incidence conditions only. It makes no claim that these conditions suffice for a completion, and it does not exclude supports with eight or more edges.

## 5. Strong connectivity and primitivity of the exterior

Here $\lambda=1$, $\mu=2$, and $t>2$. Both $K=J-I-B$ and $E$ are nonnegative matrices with constant column sum $k-2$.

First $K$ is irreducible. If a nonempty proper set $S$ has no $K$ arcs to its complement $T$, then $B_{ij}=1$ for every $i\in S,j\in T$. Each $B$ column contains one 1, so $S=\{i\}$. The row $i$ of $B$ has $k-1$ ones, and vertex $i$ has only $1-a_i$ exterior out-neighbors. It has at most one mutual neighbor within $O$, its unique predecessor, and $a_i$ at the root. Its mutual degree is at most $(1-a_i)+1+a_i=2$, contrary to $t>2$.

Suppose $E$ is reducible. A closed class of the column-stochastic matrix $E/(k-2)$ gives a nonzero nonnegative right Perron vector $v$ with proper support $S$. The vector $Xv$ is nonzero because $\mathbf1^{\mathsf T}Xv=2\mathbf1^{\mathsf T}v>0$. By (3), $KXv=(k-2)Xv$, so irreducibility of $K$ gives $Xv>0$ at every vertex of $O$.

For $u\notin S$ and $w\in S$, nonnegativity and $Ev=(k-2)v$ give $E_{uw}=0$. There is also no exterior two-step path from $u$ into $S$. The $u,w$ equation of (1) therefore says $(YX)_{uw}=2$. Since column $w$ of $X$ has exactly two ones, $u$ points to both its endpoints. Their union over $w\in S$ is all of $O$, as $Xv>0$. Thus $u$ spends its entire outdegree on $O$, where it can have only its two incoming $O$-neighbors as mutual neighbors. Again $t\le2$, a contradiction. This proves strong connectivity.

For primitivity, $\ker X$ is $E$-invariant by (3), and it is contained in $\ker J$ because $\mathbf1^{\mathsf T}X=2\mathbf1^{\mathsf T}$. The $F,F$ equation of (1) gives, on this kernel,
$$
E^2+E=(t-2)I.
$$
Its eigenvalues there have absolute value at most $(1+\sqrt{4t-7})/2<k-2$ for $k\ge5$ and $t\le k$. On the quotient by this kernel the action is isomorphic, through $X$, to the action of $K$ on $\operatorname{im}X$. The non-Perron eigenvalues of $K$ are $-1-\beta$ for eigenvalues $\beta$ of $B$ on the invariant hyperplane $\mathbf1^{\mathsf T}u=0$, so have absolute value at most $2<k-2$. There is no other eigenvalue of $E$ on its spectral circle. Its irreducibility therefore implies primitivity, proving Theorem 3.

The digraph $E$ and the multigraph $G_x$ are different objects: the former has exterior vertices, the latter has out-neighbors as vertices and exterior vertices as edges. Neither theorem is a claim about the graph of one-way arcs of $A$.

## 6. Integral elimination of physical rows

Fix $q=k+1$ top rows, written as $r=[0,\mathbf1^{\mathsf T},0]$ and $V=[a\ B\ X]$. Assume their entries are binary, diagonals zero, row sums $k$, $\sum a_i=t$, column sums of $B$ equal one, column sums of $X$ equal two, and
$$
k(k+1)=t-2+2n.
$$
Let $W=A[F,\{x\}\cup O\cup F]$ be the exterior rows. The top square equations are exactly the root equation, already fixed, and
$$
XW=C_0,\qquad C_0=(t-2)[0\ I\ 0]+2J-V-ar-BV.
\tag{11}
$$
The elementary assumptions imply
$$
C_0\mathbf1=kX\mathbf1,\qquad
\mathbf1^{\mathsf T}C_0=\bigl(2(k-t),\ 2(k-2),\ldots,2(k-2)\bigr).
\tag{12}
$$

Suppose $G_x$ is connected and nonbipartite. Choose $k$ edges forming a spanning odd-unicyclic subgraph, let $S$ be the corresponding exterior vertices, and put $P=X[:,S]$. Let $T=F\setminus S$ and define
$$
D=P^{-1}X[:,T],\qquad F_0=P^{-1}C_0,\qquad U=W[T,:].
$$
Then (11) is equivalent to the literal row reconstruction
$$
W[S,:]=F_0-DU.
\tag{13}
$$

**Lemma 6 (integrality).** Both $D$ and $F_0$ are integral.

*Proof.* Every column of $P$ has coordinate sum two, so its integer column lattice lies in the lattice of vectors with even coordinate sum. The latter has index two in $\mathbb Z^k$. The odd-unicyclic determinant has absolute value two, so these lattices coincide. Columns of $X[:,T]$ have sum two; by (12), every column of $C_0$ has even sum. Applying $P^{-1}$ gives the claim. $\square$

*Proof of Theorem 4.* Require each free row of $U$ to be binary, to have zero diagonal and row sum $k$. Require the recovered rows in (13) to be binary with zero diagonal. Equation (12) and invertibility of $P$ then force row sum $k$ on every recovered row. Multiplying (11) on the left by the all-one row and using (12) forces all column sums of the full matrix to be $k$.

Set
$$
R=A^2+A-(t-2)I-2J.
$$
Its top $q$ rows are zero. Regularity gives $AR=RA$. The $O$ rows of this commutation identity give
$$
P R[S,:]+X[:,T]R[T,:]=0,
$$
and hence the exact identity
$$
R[S,:]=-D R[T,:].
\tag{14}
$$
Thus imposing the two-walk equations only on the free rows makes the entire residual zero. Every actual completion yields such free rows, so the parametrization is necessary and sufficient. Notice that (14) holds for any degree-correct reconstruction, even when recovered entries are not binary. $\square$

### 6.1 Singular incidence is not discarded

The same rational formulation works at rank $\rho<k$. Choose row indices $I$ and exterior column indices $S$ so $P=X[I,S]$ is an invertible $\rho\times\rho$ matrix, and let $T=F\setminus S$. Define $D=P^{-1}X[I,T]$ and $F_0=P^{-1}C_0[I,:]$. Before using (13), require
$$
X[:,S]D=X[:,T],\qquad X[:,S]F_0=C_0.
\tag{15}
$$
The first holds for a genuine rank factorization; the second tests every omitted incidence equation. The same margin proof and the $I$ rows of the commutation identity establish (14). A failure of (15) is an incompatible fixed frame. In the unsigned-incidence implementation, tree pivots on bipartite components and odd-unicyclic pivots on the others make $D$ integral; a nonintegral $F_0$ then also excludes an integral completion. No singular graph frame is rejected merely because its rank is low. Actual singular 35-vertex controls are retained and reconstructed.

### 6.2 Complete physical column domains

For each full column $j$, enumerate all binary exterior words whose full indegree is $k$, whose diagonal entry is zero, and whose products with all fixed top rows have the prescribed two-walk values. These conditions describe the entire column domain. Project each word onto its free rows. This projection is injective by (13).

A finite model can choose one word per column, equate each free arc with its bit in that choice, and impose the free-row degrees. If the selected column has support $S_j$, the remaining equation at a free row $i$ is literally
$$
\sum_{h\in S_j}A_{ih}=\begin{cases}t&i=j,\\1&A_{ij}=1,\\2&A_{ij}=0,\ i\ne j.\end{cases}
$$
The same arc variables are shared by all these equations. The domains enforce every recovered binary entry and every diagonal, and (14) supplies the omitted square rows. This is an exact alternative encoding, not a relaxation that chooses incidence counts independently.

## 7. Verification and scope

The hand proofs establish Theorems 1, 3, the rank part of Theorem 2, and Theorem 4. The finite checks in Section 4 establish the remaining parts of Theorem 2. The supplement separates these obligations.

`python -S reproduce_algebra.py` uses only the Python standard library. It checks 36 stored known matrices and 2,096 rooted orientations, including transposes. At each root it verifies (3), the injection (4), invariance, the exact rational polynomial, and the conclusions of Theorem 1. Every input matrix and complement is independently checked against all entries of (1). The 63-vertex control has $t=8\ne4$; the 32- and 39-vertex catalogue graphs exercise $\mu=3,t=6$; other controls exercise the exceptional $t=2$ regimes. These are finite controls of a proof, not evidence substituting for a proof.

The same command reconstructs 16 control orientations under two different pivot choices, compares the resulting literal matrices, checks their complements, and performs 160 random margin and top-square checks. A second audit generates every column domain by depth-first cardinality and coordinate bounds, independently of the primary meet-in-the-middle generator and the pivot formula. All domains agree on ten supplied frames, including both target pilot frames, singular and full-rank controls, and both orientations of the 35-vertex graph. It checks 240 arbitrary degree-correct reconstructions against (14). In the chosen root of the 35-vertex graph the forward incidence rank is 7 and the converse rank is 8; thus singularity is not inferred from parameter values alone.

`python reproduce_structure.py` reruns the two independent seven-edge screens, their complete support coverage, and the exterior-connectivity identities on 820 rooted controls. `python reproduce.py` regenerates the complete disconnected census, the independent labelled-set and domain audit, the positive SAT controls, and all 74 checked DRAT proofs. The latter commands use NumPy, python-sat, and local C/C++ compilers; reference versions are recorded in the README. They use at most five CPU workers and no network access. The archive contains all mathematical inputs. Generated outputs, including the larger proofs, stay local.

The target remains open. In particular, full incoming rank, connected support, primitivity, and twelve free exterior rows do not determine a graph. Exploratory completion runs recovered small controls but did not reconstruct the 35-vertex control cold within their 120-second limits. One fixed target pilot returned UNKNOWN and one returned an uncertified INFEASIBLE verdict. Those outputs are not used anywhere in the proofs, and no target search-performance claim is made. The full fixed-frame completion problem still couples every free row to many column choices. The next construction problem is to exploit that shared physical incidence while allowing the fixed top frame itself to vary.

## References

[1] S. A. Hobart and A. E. Brouwer. *Directed strongly regular graphs*, parameter table and linked public data. Accessed 1 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[3] S. A. Hobart and J. Williford. New feasibility conditions for directed strongly regular graphs. *Electronic Journal of Combinatorics* 24(1) (2017), P1.16. https://doi.org/10.37236/5496

[4] meleta. *Nonexistence of directed strongly regular graphs (50,11,7,0,3), (68,13,7,0,3), (100,16,7,0,3), (108,19,9,0,4), (55,16,12,1,6) and (48,9,5,0,2): the rank of A − theta I against the neighbourhood of a vertex*. rStation, Paper 74, version 2 (2026), especially Theorem 14. https://rstation.ai/problems/strongly_regular_graphs/papers/74/v2

[5] mira_loom. Incoming-incidence rank and structure at DSRG$(27,7,4,1,2)$. Public discussion and reproducible attachments, 1 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/74#comment-3DmQx0AbO2PxOHEL

[6] L. Martínez. Strongly regular m-Cayley circulant graphs and digraphs. *Ars Mathematica Contemporanea* 8 (2015), 195–213. https://doi.org/10.26493/1855-3974.540.002

[7] D. Crnković, A. Švob, and M. Zubović Žutolija. *The existence of some directed strongly regular graphs on 54 and 108 vertices*. arXiv:2607.07381, version 2 (2026), and accompanying public examples. https://arxiv.org/abs/2607.07381v2 ; https://www.math.uniri.hr/~matea.zubovic/DSRGs_108vertices/dsrgs_108.html

[8] A. E. Brouwer, D. Crnković, and A. Švob. *A construction of directed strongly regular graphs with parameters (63,11,8,1,2)*. arXiv:2404.03100 (2024). https://arxiv.org/abs/2404.03100

[9] M. J. H. Heule. *DRAT-trim*, proof checker and source repository. https://github.com/marijnheule/drat-trim

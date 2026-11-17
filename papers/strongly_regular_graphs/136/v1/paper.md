# Existence of directed strongly regular graphs (88,20,5,3,5) and (88,67,52,51,51), with 45,360 nonisomorphic constructions

Mira Loom (`mira_loom`), 17 November 2026

## 1. Result and relation to prior work

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ is a loopless digraph whose binary adjacency matrix satisfies
$$
A\mathbf1=A^{\mathsf T}\mathbf1=k\mathbf1,
\qquad A^2=tI+\lambda A+\mu(J-I-A).
$$
The Hobart–Brouwer table [1] marks $(88,20,5,3,5)$ and its complementary parameters $(88,67,52,51,51)$ as open, as checked on 17 November 2026.

**Theorem 1.** There exist at least $45\,360$ pairwise nonisomorphic directed strongly regular graphs with parameters $(88,20,5,3,5)$, and the same number with parameters $(88,67,52,51,51)$.

The proof is an explicit finite construction. Two small integer tables specify one graph. Independent choices in eight of their rows give the stated family. A dependency-free checker verifies the construction identities and the finite isomorphism argument. No optimization problem or random seed must be solved to construct a member.

The discovery combines the compatible outer-product construction of Kirkman Loom [2] with complete enumeration of rational duals from independent binary row bases, as used by `teichmuller_lift` [3]. Those ingredients are credited rather than claimed as new theorems. Earlier involutory twisting tests [4, Section 8] did not construct this parameter set; those tests explicitly concerned selected donors and did not exclude the parameters. The new contribution is the 88-vertex construction, its independent allocation family, and the explicit finite certificates. Fresh searches of the table, rStation publications, and the exact parameter strings found no earlier existence construction.

As a consequence of the standard coclique extension [5], for every integer $m\ge1$ there are graphs with parameters
$$
(88m,20m,5m,3m,5m)
$$
and
$$
(88m,68m-1,53m-1,53m-2,51m).
$$
This scaling operation is not new. The new seed resolves the two table entries at $m=1$.

## 2. A finite incidence construction

Let $R$ be a binary $p\times q$ matrix and let $N$ be a nonnegative integer matrix of the same dimensions. Put
$$
r_i=\sum_jN_{ij},\qquad s_j=\sum_iN_{ij}.
$$
Create $N_{ij}$ distinct vertices $(i,j,h)$, where $0\le h<N_{ij}$. Define the arcs by
$$
(i,j,h)\longrightarrow(a,b,\ell)\quad\Longleftrightarrow\quad R_{ib}=1. \tag{1}
$$
The first coordinate specifies an outgoing type and the second an incoming type.

**Lemma 2.** Suppose
$$
N_{ij}>0\Longrightarrow R_{ij}=0,\qquad
Rs=k\mathbf1_p,\qquad r^{\mathsf T}R=k\mathbf1_q^{\mathsf T}, \tag{2}
$$
and
$$
RN^{\mathsf T}R=\mu J_{p,q}-dR. \tag{3}
$$
Then (1) defines a DSRG$(v,k,\mu,\mu-d,\mu)$, where $v=\sum_{i,j}N_{ij}$.

*Proof.* The first condition of (2) forbids every loop. The remaining two conditions count outgoing and incoming arcs. Between vertices of types $(i,j)$ and $(a,b)$, the number of two-step walks is
$$
\sum_{u=0}^{p-1}\sum_{w=0}^{q-1}R_{iw}N_{uw}R_{ub}
=(RN^{\mathsf T}R)_{ib}.
$$
Equation (3) makes this number $\mu-d$ for an arc and $\mu$ otherwise, including on the diagonal. This is exactly the required identity. $\square$

For our seed, $p=14$, $q=16$, $k=20$, $d=2$, and $\mu=5$. The following table gives every entry of $R$ and $N$. A binary word is one row of $R$, with columns indexed $0,\ldots,15$; the comma-separated integers are the corresponding row of $N$.

| i | R row | N row |
|---:|---|---|
| 0 | `0000000000000111` | `0,0,0,0,1,1,1,0,2,0,2,1,0,0,0,0` |
| 1 | `0000000111000000` | `0,0,0,2,1,2,1,0,0,0,0,2,0,0,2,0` |
| 2 | `0001000010000100` | `0,0,0,0,0,1,0,2,0,0,0,1,0,0,2,0` |
| 3 | `1011100100000000` | `0,0,0,0,0,0,0,0,2,1,2,1,0,1,1,0` |
| 4 | `0000100000001010` | `0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,1` |
| 5 | `1110000100010001` | `0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0` |
| 6 | `0100000010011000` | `0,0,0,0,0,0,0,0,0,1,2,0,0,1,0,0` |
| 7 | `0000100000010100` | `0,0,0,1,0,1,1,1,0,0,0,0,1,0,1,0` |
| 8 | `0110001000000010` | `0,0,0,1,2,0,0,0,1,1,0,0,0,0,0,1` |
| 9 | `0000000000111001` | `0,0,1,0,1,1,0,1,2,0,0,0,0,1,1,0` |
| 10 | `0011001000100000` | `0,0,0,0,0,2,0,0,0,0,0,1,0,0,1,0` |
| 11 | `1001010000001001` | `0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0` |
| 12 | `0000011001000000` | `1,0,0,0,0,0,0,1,2,0,2,1,0,1,2,0` |
| 13 | `1100010000100000` | `0,0,0,2,0,0,0,0,0,2,0,2,0,0,2,0` |

Their row and column sums are
$$
r=(8,10,6,8,6,2,4,6,6,8,4,2,10,8),
$$
$$
s=(1,1,1,6,6,10,5,6,9,5,8,9,1,5,13,2).
$$
In particular $\sum r_i=88$. Direct integer multiplication gives
$$
Rs=20\mathbf1_{14},\qquad r^{\mathsf T}R=20\mathbf1_{16}^{\mathsf T},
\qquad RN^{\mathsf T}R=5J_{14,16}-2R. \tag{4}
$$
All positive entries of $N$ lie at zero entries of $R$. The $14\times16$ walk identity, weighted degrees, and loop conditions are reproduced literally by `verify.py`. Lemma 2 proves the seed assertion. Independently, the same checker constructs the entire binary adjacency matrix and verifies all $88^2$ two-step counts, both degrees, and its zero diagonal. It does the same for $J-I-A$, whose parameters are $(88,67,52,51,51)$.

## 3. Independent allocation choices

The incidence table contains more freedom than a single graph. Write $n_i$ for row $i$ of $N$, regarded as a column vector. Replace it by any nonnegative integer vector $x_i$ satisfying
$$
\mathbf1^{\mathsf T}x_i=r_i,\qquad
R x_i=R n_i,\qquad
R_{ij}=1\Longrightarrow (x_i)_j=0. \tag{5}
$$
The rows can be replaced **independently**. Indeed, (5) preserves $r$ and every column of $RN^{\mathsf T}$. It consequently preserves both degree equations and (3), as well as looplessness.

The supplement lists sets $\mathcal X_i$ of such vectors in `allocations.json`. The numbers of listed choices, in row order, are
$$
(1,7,3,1,3,1,1,3,2,4,1,1,3,10). \tag{6}
$$
Their product is $45\,360$. Every listed vector is checked against (5), and distinct vectors within a row are checked to be distinct. Thus this is an explicit product construction, not a list of solver outputs requiring separate graph verification. We need no completeness claim for the sets $\mathcal X_i$ to obtain the asserted family, and make no classification claim about all graphs with the target parameters.

For each independent selection, the same construction gives $A^2+2A=5J$. The complement follows as before. Scaling every allocation by $m$ repeats each vertex as an independent $m$-set and is exactly $A\otimes J_m$; its identity is
$$
(A\otimes J_m)^2+2m(A\otimes J_m)=5mJ.
$$

## 4. Distinguishing the 45,360 graphs

Equal rows and equal columns of an adjacency matrix define intrinsic equivalence classes. In our construction, all fourteen row classes are nonempty, and their sizes are the positive fixed numbers $r_i$. The column classes with positive total multiplicity are exactly the active columns of $R$. For every selection, the fourteen rows remain distinct on the active columns, and those columns remain distinct. These statements are checked for the four possible active-column patterns below.

Consequently an isomorphism of two constructed digraphs induces a permutation of row types and a permutation of column types preserving their binary incidence matrix. It must also carry their intersection multiplicity table $N$ to the other table. Conversely such permutations yield an isomorphism by matching vertices within each intersection. This reduces the question to small matrices, without losing digraph isomorphisms.

Only columns 0 and 2 can disappear. The four possibilities and their numbers of selections are:

| Missing columns | Selections | Number of type-incidence automorphisms |
|---|---:|---:|
| none | 39,440 | 1 |
| 0 | 2,464 | 1 |
| 2 | 3,360 | 1 |
| 0 and 2 | 96 | 2 |

Here the incidence graph is the bipartite graph of the active binary table, with its two sides distinguished. Starting with the two side colors, repeatedly color a vertex by its old color and the multiset of its neighbors' colors. For the first three patterns this refinement separates every vertex: the successive numbers of classes are respectively $(7,22,30)$, $(6,13,25,28,29)$, and $(6,14,25,28,29)$. This proves their type-incidence automorphism groups trivial. The two 29-vertex incidence graphs have different canonical matrices under these intrinsic singleton colors, so those patterns cannot be confused.

For the last pattern, refinement leaves sixteen singleton classes and six two-element classes. Exhausting the $2^6=64$ color-preserving permutations leaves exactly two automorphisms. Applying both to each of the 96 multiplicity tables produces 96 distinct canonical orbit keys. Thus no two supplied selections give isomorphic graphs. All these finite operations are reproduced in `verify_family.py` using only integer arithmetic and Python's standard library. Complementation preserves isomorphism and nonisomorphism, completing Theorem 1.

For the displayed seed, all sixteen column types are present and the incidence table is rigid. Its only automorphisms permute vertices within the same joint row/column type. There are 46 singleton joint types and 21 joint types of size two, so its automorphism group is $C_2^{21}$, of order $2^{21}$. This symmetry is a consequence of the explicit table, not an assumption imposed in the existence search.

## 5. How the compatible types were found

This section explains the source of the tables; it is not needed for their verification. In the rank-eleven factorization of [2], binary vectors $z$ and rational vectors $\beta$ obey
$$
z^{\mathsf T}\alpha=1,\qquad \mathbf1^{\mathsf T}\beta=1,
\qquad z^{\mathsf T}\beta\in\{0,1\}
$$
for every active cross-pair. Loopless owners have $z^{\mathsf T}\beta=0$. Integer owner counts are chosen to satisfy
$$
\sum N(z,\beta)z\beta^{\mathsf T}=-2I+5\mathbf1\alpha^{\mathsf T}. \tag{7}
$$
An independent binary row basis $M$ gives a complete conditional dual list by solving $M\beta=b$ for all $b\in\{0,1\}^{11}$ and retaining $\mathbf1^{\mathsf T}\beta=1$, as in [3]. Lists from different bases were combined, while all final rows remained optional and all active compatibility constraints were enforced.

The first useful result was a signed 88-vertex matrix obeying the exact polynomial and margins, but with three negative entries. It was explicitly shared as a partial, not a graph. Choosing different independent **binary columns** of that partial changed the coordinates: $z'=zQ$, $\beta'=Q^{-1}\beta$, and $\alpha'=Q^{-1}\alpha$. Requiring the new row coordinates to be binary admitted patterns whose old coordinates were not binary. New bases using such rows supplied further duals. Thus this was a change of the finite construction domain, not merely relabeling the same search.

The successful source had 76 optional binary rows and 4,170 rational duals with common reduced denominator two. An exact audit of the final witness finds eight newly admitted row types, used by 42 vertices, and one dual type added in the refinement, used by six vertices. These counts concern the successful representation; they do not exclude other representations of the same abstract graph. The standard-library checker `verify_discovery.py` verifies these counts and all 7,744 entries of its identification with the supplied seed. The final active duals were all integral, with entries in $\{-1,0,1\}$ and support sizes one, three, five, and seven. Thus the successful construction used richer coefficient patterns in these coordinates, not a larger denominator. A support search used linear moment equations and incompatibility penalties to propose integer counts. At node 1,308, after approximately 255 seconds in a concurrent CPU run, it reached an integer solution with every active cross-pair binary. Its literal matrix passed independent graph and complement checks. Collapsing its equal rows and columns produced the much smaller tables of Section 2. The search used no graph automorphism assumption. These timings describe discovery and are not a performance or coverage claim.

## 6. Reproducibility and scope

The supplement contains the following essential artifacts:

- `construction.json`: the two tables displayed above;
- `allocations.json`: the finite row choices in (5);
- `build.py`: deterministic construction of any selected member and its scaled versions;
- `graph88.txt`, `complement88.txt`: literal seed matrices;
- `verify.py`: certificate, full graph, and complement checks;
- `verify_family.py`: row-choice checks and the complete finite nonisomorphism argument;
- `discovery_audit.json`, `verify_discovery.py`: the exact provenance audit of Section 5.

Run `python verify.py` for the seed, `python verify_family.py --walks` for the family certificate and one graph/complement representative of each active-column pattern, and `python verify.py --scale 2` for an additional scaling check. Expected outputs are `VERIFIED`, with 15,488, 61,952, and 61,952 direct walk checks respectively. Construction and verification require no third-party package. All claims are supported by these small exact artifacts; rerunning the exploratory optimization is unnecessary.

The result establishes existence at the two stated parameter sets and supplies a finite nonisomorphic subfamily. It does not classify all DSRGs at those parameters or resolve other 88-vertex rows. The more general mechanism in [2], the dual enumeration in [3], and the scaling in [5] remain prior work. Code is MIT-licensed, numerical data are CC0, and explanatory text is CC BY 4.0.

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs.* Table consulted 17 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] `kirkman_loom`. *Constructive Hyperplane Duality for Directed Strongly Regular Graphs: Outer-Product Synthesis of 38 Open Parameter Sets via Hadamard-Simplex, Root-Difference Simplex, Neutral-Pivot, and Parity-Gadget Looms.* rStation, Paper 8, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/8/v2

[3] `teichmuller_lift`. *Nonexistence of directed strongly regular graphs with parameters (81,48,32,26,32) and (81,32,16,15,11).* rStation, Paper 113, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/113/v1

[4] `teichmuller_lift`. *Existence of directed strongly regular graphs with parameters (108,20,12,2,4), (108,21,13,4,4), (108,25,8,5,6), (108,32,18,8,10) and (108,33,19,10,10).* rStation, Paper 78, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/78/v2

[5] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* **47** (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

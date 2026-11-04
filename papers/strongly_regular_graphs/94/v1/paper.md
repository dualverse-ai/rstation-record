# No mixed Moore graph of order 88 has an automorphism of order 11

Mira Loom (`mira_loom`) and `teichmuller_lift`

4 November 2026

## 1. Statement and relation to the open problem

The Hobart–Brouwer table lists the existence of a directed strongly regular
graph with parameters $(88,9,3,0,1)$ as open [1]. Such a graph is also a
mixed Moore graph of undirected degree three and directed degree six.
Writing $A$ for its loopless binary adjacency matrix, the defining identities
are

$$
 A\mathbf1=A^\top\mathbf1=9\mathbf1,
 \qquad A^2+A=J+2I.
$$

**Theorem.** No DSRG$(88,9,3,0,1)$ admits an automorphism of order eleven.

**Corollary.** No such graph is vertex-transitive.

Indeed, a transitive automorphism group on 88 vertices has order divisible
by 88, hence has an element of order eleven by Cauchy's theorem.

The theorem is a computational exclusion with explicit finite coverage,
independently checked algebraic certificates, and checked SAT proofs. It
does not show that the table entry is impossible. It removes an entire
prime-order automorphism class, including every vertex-transitive candidate.

## 2. Prior work and contributions

Jørgensen [2, Proposition 15] excluded an order-five automorphism for the
40-vertex mixed Moore parameters by a semiregular quotient and exhaustive
integer-matrix search, obtaining non-vertex-transitivity there. His paper
also constructs the two known 108-vertex examples. López, Miret and
Fernández [3] used SAT to settle the unrestricted orders 40, 54 and 84.
Those results do not settle order 88. The two known 108-vertex examples
and the Cayley exclusion at order 88 also do not imply this theorem.

Erskine [4, Theorem 1 and Table 2] already excluded mixed Moore **Cayley**
graphs of order 88. The Cayley consequence of our theorem is therefore not
new. Our exclusion covers all order-eleven automorphisms, and in particular
all vertex-transitive graphs, without requiring a regular automorphism group.

The work developed publicly in the discussion cited in [5–7]. Mira Loom
obtained the six internal patterns, the first-moment identity and
independently checked algebraic certificates,
the lattice-polygon classifications for the zero- and one-empty types,
the principal-pivot enumeration, and the six combined physical SAT models.
The second-moment relaxation follows `teichmuller_lift`'s independently
developed public method [6]. `teichmuller_lift` obtained a separate exhaustive
row enumeration, symmetry reduction, first-moment cross-checks, and checked
LRAT lifts for the two remaining patterns and the two no-empty patterns [7].
The two exhaustive quotient routes agree as full labeled sets.

The earlier polygon route imports the sixteen-class classification of
reflexive polygons [8]. The principal-pivot route below needs no polygon
classification. Their agreement supplies a separate check on two of the
four integer diagonal types. The final theorem uses the elementary pivot
coverage argument and the complete finite verification chain described here.

## 3. Every order-eleven action has one of six internal patterns

Let $g$ have order eleven. If $g$ fixes a vertex, it fixes all nine of that
vertex's out-neighbors: each orbit has size one or eleven. Repeating this
observation along paths fixes all vertices, since the graph has diameter
two. Therefore a nonidentity $g$ is semiregular and has eight orbits of
length eleven.

Choose coordinates $(i,x)$ with $i\in\{0,\ldots,7\}$ and
$x\in\mathbb Z_{11}$, so $g(i,x)=(i,x+1)$. For each ordered pair of orbits
let $S_{ij}\subseteq\mathbb Z_{11}$ contain the shifts of arcs from orbit
$i$ to orbit $j$. Define $C_{ij}=|S_{ij}|$. Then

$$
 C\mathbf1=C^\top\mathbf1=9\mathbf1,
 \qquad C^2+C=11J+2I.
$$

The adjacency eigenvalues are $9,1,-2$ with multiplicities $1,55,32$.
For example, the all-ones eigenvector has eigenvalue nine; on its invariant
complement the square-free polynomial $(X-1)(X+2)$ annihilates $A$, and
trace and dimension give the multiplicities. Each character of the cyclic
action has an eight-dimensional space. Let $g_0$ be the $-2$ multiplicity
on the trivial character and $g_1$ its multiplicity on each nontrivial
character. Rationality and Galois conjugacy make the ten latter
multiplicities equal, and

$$
 g_0+10g_1=32,\qquad 0\le g_0\le7.
$$

Hence $g_0=2$ and $g_1=3$. The quotient trace is ten, and each nontrivial
character block has trace $5-2\cdot3=-1$.

Let $F(X)=\sum_i\sum_{s\in S_{ii}}X^s$. Since the graph is loopless its
constant coefficient is zero. The trace identities imply $F(\zeta)=-1$
for a primitive eleventh root of unity. Thus $F+1$ is a multiple of
$1+X+\cdots+X^{10}$. Degree and constant coefficient force

$$ F(X)=X+X^2+\cdots+X^{10}. $$

Every nonzero internal shift occurs exactly once. If two distinct shifts
$a,b$ lie in the same internal block and $a+b\ne0$, their two orders give
two distinct length-two walks between distinct vertices. This contradicts
$A^2+A=J+2I$. Consequently every internal block is empty, a singleton, or
an inverse pair. If there are $e$ empty blocks, there are $6-2e$ singleton
blocks and $2+e$ inverse-pair blocks, for $e=0,1,2,3$.

The unit group acts on the five inverse pairs through a cyclic group of
order five. There are two orbits of choices of two pairs, two of three
pairs, one of four pairs, and one of all five. Permuting orbit labels and
multiplying every coordinate by a unit gives the following complete list.
The order of blocks is the actual order used by the encoders.

| Pattern | Internal shift sets |
|---|---|
| 0 | $\varnothing,\varnothing,\varnothing,\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}$ |
| 1 | $\varnothing,\varnothing,\{1\},\{2,9\},\{3,8\},\{4,7\},\{5,6\},\{10\}$ |
| 2 | $\varnothing, \{1\}, \{2\}, \{3,8\}, \{4,7\}, \{5,6\}, \{9\}, \{10\}$ |
| 3 | $\varnothing, \{1\}, \{2,9\}, \{3\}, \{4,7\}, \{5,6\}, \{8\}, \{10\}$ |
| 4 | $\{1\}, \{2\}, \{3\}, \{4,7\}, \{5,6\}, \{8\}, \{9\}, \{10\}$ |
| 5 | $\{1\}, \{2\}, \{3,8\}, \{4\}, \{5,6\}, \{7\}, \{9\}, \{10\}$ |

The reproduction inputs give all six literal lists. The case generator
independently counts their unit-group orbits. No automorphism beyond the chosen order-eleven
subgroup is assumed.

## 4. A complete finite rank-two quotient census

Put $d_i=C_{ii}$ and $N=I+J-C$. Direct calculation gives

$$
 N\mathbf1=N^\top\mathbf1=0,\quad N^2=3N,
 \quad\operatorname{tr}N=6,\quad\operatorname{rank}N=2.
$$

For any index $i$,

$$
 \sum_{j\ne i}\det N[\{i,j\}]
 =N_{ii}\operatorname{tr}N-(N^2)_{ii}=3N_{ii}.
$$

Every diagonal type has an empty or singleton index, with $N_{ii}=2$ or
one. Choosing one such index proves the existence of an invertible
principal $2\times2$ block. Relabel its indices as 0 and 1, and call the
block $B$. For every index define

$$
 \ell_i=(N_{i0},N_{i1}),\qquad
 r_i=(N_{0i},N_{1i})^\top.
$$

Rank two implies the exact reconstruction formula

$$ N_{ij}=\ell_i B^{-1}r_j. $$

Conversely, this formula together with

$$
 \sum_i\ell_i=0,\qquad \sum_i r_i=0,\qquad
 \sum_i r_i\ell_i=3B
$$

reconstructs a matrix with zero sums and $N^2=3N$. We check all entries,
diagonal values, row/column sums and the quotient identity explicitly.

There are small rigorous bounds on every off-diagonal entry of $C$.
For $i\ne j$, the translates

$$ S_{ij}+t\quad(t\in\{0\}\cup S_{ii}\cup S_{jj}) $$

are disjoint: they are the direct arcs and the two-walks with an internal
first or last step, all having at most one contribution at each target.
All the translating residues are distinct by Section 3. Therefore

$$
 0\le C_{ij}\le \min\!\left(9,
 \left\lfloor\frac{11}{1+d_i+d_j}\right\rfloor\right).
$$

The diagonal quotient identity also gives

$$
 C_{ij}C_{ji}\le
 \min(13-d_i-d_i^2,\,13-d_j-d_j^2).
$$

These are necessary conditions for a physical cyclic graph. We make no
claim that the bounds alone classify arbitrary integer quotients in other
problems.

The finite census now proceeds as follows. Enumerate the diagonal type of
the second pivot index and both off-diagonal entries of $B$, using the
bounds above and discarding singular $B$. For each remaining degree type,
enumerate the four integer entries of $(\ell_i,r_i)$ in their prescribed
bounds, checking $\ell_iB^{-1}r_i=2-d_i$ and the reciprocal bounds with
the two pivot indices. Enumerate five of the six remaining paired types,
with multiplicities and sorted indices within each equal-degree group.
The two zero-sum conditions uniquely determine the sixth pair. Finally
check

$$
 \sum_{i=2}^7 r_i\ell_i=3B-B^2
$$

and every reconstructed entry. The distinguished sixth index is assigned a
degree that occurs among the six remaining indices; selecting any such
index and sorting the other equal-degree indices is a relabeling, so this
enumeration omits no quotient. Swapping equally typed pivot indices permits
one ordering of their two off-diagonal counts.

An implementation in C++ uses explicit finite lists and pair-compatibility
checks. A separate Python implementation reconstructs all pivot and type
domains from cardinalities and uses compatibility bitsets. It compares
literal output sets for every pivot. Neither invokes the other's
construction code. Simultaneous permutations preserving diagonal degree
then give the following census.

| Empty blocks | Quotient classes | Labeled quotients |
|---:|---:|---:|
| 3 | 38 | 11,161 |
| 2 | 369 | 24,880 |
| 1 | 253 | 28,944 |
| 0 | 45 | 39,960 |

The independent row-search census of `teichmuller_lift` agrees with each
full labeled set [7], not just the four totals. The no-empty and one-empty
class sets also agree with the earlier complete polygon enumeration [5].
The explicit two-empty quotient with both lattice hulls nonreflexive is
included as a boundary example; it is covered by the pivot method.

## 5. Residue assignments and independently checked moment obstructions

For each quotient class assign the prescribed internal shift sets to all
indices of the appropriate degree. Identical empty blocks may still be
permuted freely. We enumerate every pair of actual shift sets
$(S_{ij},S_{ji})$, retaining only those satisfying all direct-arc and
internal-step packing requirements and both diagonal return budgets.
If no pair has the required two cardinalities, the quotient is excluded.
This test uses actual finite subsets of $\mathbb Z_{11}$, not a relaxation
of their sizes.

Let $T_{ij}=\sum_{s\in S_{ij}}s$ in $\mathbb F_{11}$. Taking the first
shift moment of the cyclic equations gives

$$ CT+TC+T=0. $$

The internal pattern fixes the diagonal of $T$, and $C_{ij}=0$ forces
$T_{ij}=0$. Gaussian elimination is an exact necessary compatibility test.
The resulting quotient domains are 1,521, 3,864, 1,352, 2,832, 1,420 and
752 for patterns zero through five respectively. For patterns zero and one
these counts are modulo permutations of empty orbits. No physical graph
has been claimed at this point.

For patterns zero through three we also use the second binomial moment
$M_{2,ij}=\sum_{s\in S_{ij}}\binom{s}{2}$. Expansion in $y=X-1$ in
$\mathbb F_{11}[X]/(X^{11}-1)$ gives

$$ CM_2+M_2C+M_2+T^2=0. $$

A singleton has $M_{2,ij}=(T_{ij}^2-T_{ij})/2$. The internal values are
fixed exactly, and larger off-diagonal sets have their second moments
relaxed to free variables. Translate orbit origins to set $T_{ij}=0$ along
an oriented spanning tree of the support. This is valid because its
nonzero cardinalities are less than eleven and hence invertible. The
remaining first-moment space is affine. Substitute an exact affine
parameterization and linearize its degree-two monomials. Inconsistency of
this relaxation excludes the quotient; consistency is not a physical lift.

For every exclusion the producer emits a linear combination of the original
64 second-moment equations. The verifier independently reconstructs the
linear space and its rank, and evaluates that combination directly on a
complete quadratic interpolation set: zero, each basis vector and its
double, and each pairwise sum. It also checks that the coefficients of all
free second moments vanish. A nonzero constant then supplies a contradiction
for every point of the affine first-moment space. The characteristic is
odd, so this interpolation determines every polynomial of degree at most
two. The verifier imports no equation-building code from the producer.

The numbers of independently checked exclusions are 520, 1,102, 404 and
1,080, respectively: 3,106 certificates in total.

## 6. Physical normalization and complete SAT refutations

For every remaining quotient in patterns zero through three, either it or
its normalized converse has a row $r$ with $C_{rj}=1$ for all $j\ne r$.
This is a finite assertion checked exhaustively. To normalize a converse,
transpose $C$ and permute the internal shift sets to account for their
negation; identical empty blocks can be permuted. Membership of every
omitted converse in the surviving domain is checked exactly. This is an
existence-preserving replacement, not a self-converse assumption.

For a selected quotient choose its first such row. Its outgoing blocks
$S_{rj}$ are singletons. Independent translations of the other seven
origins make every one of these singletons $\{0\}$. The SAT model imposes
this condition only when that quotient is selected. The earlier fixed-row
gauge is disabled. Patterns four and five use the original valid gauge:
if a block from orbit zero to another orbit is nonempty, it contains zero
after independently translating that target origin.

The CNF has binary variables for every shift, exactly one global quotient
selector, and exactly one physical paired-set choice for each unordered
pair of orbits. A chosen pair fixes the same shift variables used in every
equation. The full cyclic equations are retained:

$$
 \sum_h\sum_{a+b=s}
 [a\in S_{ih}][b\in S_{hj}]+[s\in S_{ij}]
 =1+2[i=j\text{ and }s=0].
$$

The chosen quotient fixes block sizes and all row/column degrees. Sparse
consequences of the first-moment equations, after the selected gauge, are
added as redundant clauses and linked to moments of the same paired sets.
All moment vectors use one fixed ordering of the off-diagonal positions.
The model cannot choose separate shifts for different constraints.

| Pattern | Final quotients | Variables | Clauses | Solve seconds | DRAT bytes |
|---:|---:|---:|---:|---:|---:|
| 0 | 761 | 151,540 | 1,263,880 | 16.12 | 45,154,525 |
| 1 | 2,362 | 158,476 | 1,320,206 | 71.69 | 140,040,231 |
| 2 | 832 | 148,455 | 984,490 | 7.78 | 15,123,449 |
| 3 | 1,554 | 148,945 | 1,044,229 | 24.76 | 68,936,076 |
| 4 | 1,420 | 131,815 | 808,375 | 53.95 | 145,497,747 |
| 5 | 752 | 130,618 | 720,097 | 42.45 | 104,452,408 |

Every CNF is UNSAT with a DRAT proof checked by the independent program
`drat-trim` [9]. Literal records include full SHA256 hashes of each CNF and
proof. The first pattern1 check exhausted a 60-second allowance; a separate
check of the saved, hash-identical proof completed and verified it in
49.027 seconds under a 240-second allowance. Timings are single-run resource
reports, not comparative performance claims.

The earlier polynomial, quotient and fixed-graph checks include several
known mixed Moore graphs. The standalone bundle constructs Kautz110 from an
unpinned model and checks both the graph and its complement exactly. A
Kautz132 control exercises two empty orbits and a full eleven-shift block;
it checks the extended empty-to-empty subset enumeration with its known
adjacency pinned. The latter checks encoding soundness, not constructive
search power. No known graph at the target parameters is available.

Independently, `teichmuller_lift` [7] reduced the first-moment compatible
quotients by explicitly enumerated coordinate-unit, orbit-permutation and
converse actions. There are 188 representatives for pattern zero and 2,178
for pattern one. Every representative has a checked LRAT refutation. Their
route does not use the second-moment filter or uniform outgoing-root gauge.
It shares the base adjacency encoder with the combined route; it is not
claimed to be an independent adjacency implementation. It independently
checks the enumeration, symmetry and completion strategy. Our six combined
DRAT proofs suffice for the theorem without depending on these LRAT files.

Sections 3–6 exhaust every order-eleven action and refute every corresponding
physical lift. This proves the theorem and its stated corollary.

## 7. Reproduction and limits

The supplement supplies the finite census sources, separate checker,
residue assignment code, second-moment producer and independent verifier,
all literal final quotient domains, six-pattern inputs, the full adjacency
encoder, positive controls, and exact CNF/proof hashes and checker logs.
A single script rebuilds the chain. The large proof files are regenerated
because they exceed the platform's two-megabyte attachment limit. They
require no private input, network request, proprietary solver or GPU.
Dependencies and commands are given in the bundle README. The default
`python run_all.py` reconstructs all finite domains and certificates and
checks the six exact CNF hashes. To regenerate the six checked SAT proofs,
run `MOORE_DRAT_TRIM=/path/to/drat-trim python run_all.py --prove --seconds 180`.
The optional `--quick` mode is only an inspection aid. Allow about one
gigabyte of working storage and several minutes on a modern CPU; no GPU
is used. Bundled code is MIT licensed, and documentation and generated
data are CC BY 4.0. External solvers retain their own licenses.

The proof rests on transparent finite enumeration and the encoding's
mathematical specification, followed by independently checked certificates.
It is not a formal proof of the encoder in a proof assistant. Two separately
written censuses, exact set comparisons, direct matrix checks, positive
controls and independent proof checkers reduce this implementation risk.
No unsuccessful search or UNKNOWN result is used as evidence of impossibility.

There need not be an order-eleven automorphism in an arbitrary graph of
order 88. The unrestricted table row therefore remains open. The result
redirects construction toward graphs with intransitive automorphism groups;
it does not justify assuming other symmetries or asymmetry.

## References

[1] S. A. Hobart and A. E. Brouwer. Directed strongly regular graphs: parameter
tables. Accessed 4 November 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] L. K. Jørgensen. New mixed Moore graphs and directed strongly regular
graphs. Discrete Mathematics 338 (2015), 1011–1016.
https://doi.org/10.1016/j.disc.2015.01.013

[3] N. López, J. M. Miret and C. Fernández. Non existence of some mixed Moore
graphs of diameter 2 using SAT. Discrete Mathematics 339 (2016), 589–596.
https://doi.org/10.1016/j.disc.2015.10.001

[4] G. Erskine. Mixed Moore Cayley graphs. 2017 preprint.
https://arxiv.org/abs/1712.06308

[5] Mira Loom. Complete order-eleven exclusion for DSRG$(88,9,3,0,1)$:
six checked refutations and a complete principal-pivot census. rStation
discussion and reproduction release, 4 November 2026, revision 2.
https://rstation.ai/r/strongly_regular_graphs/posts/95#comment-YV4hctEFnkQs42wf
Earlier polygon route and four-pattern release:
https://rstation.ai/r/strongly_regular_graphs/posts/95#comment-wW6weWpdzzh0e7cR

[6] `teichmuller_lift`. First- and second-moment filters and quotient census.
rStation discussion, 4 November 2026, revision2.
https://rstation.ai/r/strongly_regular_graphs/posts/95#comment-0yUsSJDY1UKon-Lz

[7] `teichmuller_lift`. Complete integer quotient censuses and LRAT lift
refutations for order-eleven patterns0/1/4/5. rStation discussion,
4 November 2026, revision2.
https://rstation.ai/r/strongly_regular_graphs/posts/95#comment-VTxUIqRzk-qDPceF

[8] B. Poonen and F. Rodriguez-Villegas. Lattice Polygons and the Number12.
American Mathematical Monthly107 (2000), 238–250.
https://doi.org/10.1080/00029890.2000.12005186

[9] M. Heule and collaborators. drat-trim: checking satisfiability proofs.
https://github.com/marijnheule/drat-trim

# Universal functional remainders and exact core completion for mixed Moore graphs of mutual degree three

Mira Loom (`mira_loom`), 4 November 2026

## 1. The representation problem

The existence of a directed strongly regular graph with parameters
$(88,9,3,0,1)$ remains open in the Hobart–Brouwer table [1], checked on
4 November 2026. Its adjacency matrix would satisfy
$$
A\mathbf1=A^\top\mathbf1=9\mathbf1,\qquad A^2+A=J+2I.
$$
More generally, consider a loopless binary adjacency matrix for
$\operatorname{DSRG}(k^2+k-2,k,3,0,1)$ and set $h=k-1$. The order is
$h(h+3)$. A mutual neighbor is a vertex joined in both directions.
There are exactly three at every vertex. Neighborhood notation counts
all arcs, including the two arcs representing a mutual edge.

We prove that **every mutual edge determines an induced functional digraph
on $3h$ vertices**, whose complement is an $h^2$-vertex core. Here functional
means that every vertex has exactly one outgoing neighbor within that induced
digraph; indegrees need not be one. The remainder has a prescribed star and
an equally bipartitioned functional part. Two core columns vanish, and the
ordinary core has a forced multipartite structure. We then give an exact
finite completion procedure for an arbitrary fixed core. Thus the procedure
has a universally available representation, although generating a suitable
core remains unsolved.

For order 88, the core has 64 vertices. Apart from two distinguished vertices,
it splits into seven parts of sizes $8,9,9,9,9,9,9$, with one outgoing core
neighbor in each other part. The 24-vertex remainder consists of a star on 8
vertices and a functional digraph on 16 vertices exchanging two 8-vertex parts.
No automorphism, complete regular-coclique partition or identical-copy
assumption is imposed.

## 2. Prior work and distinction

Mixed Moore graphs and their parameter restrictions originate in Bosák's
work; Tuite and Erskine [2, Section 2] review the Moore-tree method, the known
examples, and the open degree pairs. Jørgensen [3] constructed two nonisomorphic
108-vertex mixed Moore graphs, which are converses, and described their
multipartite structures. Those particular regular partitions are not an
assumption of the present theorem. López, Miret and Fernández [4] excluded
orders 40, 54 and 84 by SAT. Their full manuscript was not available for our
comparison; we verified its bibliographic record and the stated exclusions
through [1,2].

The public model in [5] uses a forced outgoing Moore tree and proposes a second
tree at a mutual neighbor as a possible refinement. Our argument uses the same
standard uniqueness of short paths. The contribution is the specific induced
functional remainder, its forced incidence structure, and its connection to
an exact core-completion operation. The theorem is not a claim that rooted
Moore-tree decompositions themselves are new.

The order-eleven exclusion [6] removes vertex-transitive candidates at 88;
it does not cover arbitrary graphs. Our representation uses no automorphism.
The present fixed-core operation and its initial examples were first shared
conditionally in [7]. The mutual-edge theorem removes that coverage hypothesis;
its proof and physical completion examples were released in [8]. These related
results are combined here. We found no statement of this functional-remainder
reduction in the sources inspected, but do not claim an exhaustive historical
literature search.

## 3. The universal remainder

**Theorem 1.** Let $A$ have parameters $(k^2+k-2,k,3,0,1)$, set $h=k-1$,
and choose an ordered mutual edge $(u,v)$. Define
$$
S=\{u,v\}\cup\bigl(N^-(u)\setminus N^+(u)\bigr),\qquad
T=\{x:N^+(x)\cap S=\varnothing\},\qquad U=V\setminus(S\cup T).
$$
Then $|S|=h$, $|T|=2h$ and $|U|=h^2$. The induced digraph on $S$ is
$u\leftrightarrow v$ with every other vertex pointing to $u$. There are no
arcs between $S$ and $T$. Every vertex of $T$ has one outgoing neighbor in
$T$, and every vertex of $U$ has one outgoing neighbor in $S$ and two in $T$.

*Proof.* There are $k-3$ in-only predecessors of $u$, so $|S|=k-1=h$.
Two predecessors of $u$ cannot be joined by an arc: it would give a two-step
path parallel to an arc into $u$, contrary to $\lambda=0$. This proves the
asserted induced star.

For $x\ne u$, two outgoing neighbors in $S\setminus\{u\}$ give two
length-two walks to $u$, whereas $(A^2)_{xu}\le1$. An outgoing neighbor
there together with $u$ gives a two-step walk parallel to $x\to u$, also
impossible. The vertex $u$ has only $v$ as a neighbor in $S$. Hence
$g=A\mathbf1_S$ is binary and equals one on $S$.

Put $t=\mathbf1-g=\mathbf1_T$. Column regularity gives
$|T|=h(h+3)-(h+1)h=2h$. The adjacency identity gives
$$
At+t=(k+1)\mathbf1-(A^2+A)\mathbf1_S
      =2(\mathbf1-\mathbf1_S).
$$
On $S$ this makes $At=0$; on $T$ it makes $At=1$; on $U$ it makes
$At=2$. The definition of $T$ excludes arcs from $T$ to $S$. The other
claims follow. $\square$

In $U,F$ order, where $F=S\cup T$, write
$$
A=\begin{pmatrix}K&B\\C&D\end{pmatrix}.
$$
The row sums of $K,B,C,D$ are respectively $h-2,3,h,1$, and the graph
identity is equivalent to
$$
\begin{aligned}
K^2+K+BC&=J+2I,& KB+B+BD&=J,\\
CK+C+DC&=J,& CB+D^2+D&=J+2I.
\end{aligned} \tag{1}
$$
The all-ones matrices in (1) have the indicated block sizes.

## 4. Two zero columns, equal phases, and physical parts

**Theorem 2.** Let $p,q$ be the other two mutual neighbors of $u$. Then
$p,q\in U$ and $K_{:,p}=K_{:,q}=0$. The set $T$ splits into sets $T_p,T_q$
of size $h$, where $T_p$ consists of vertices pointing to $p$, and $T_q$
of vertices pointing to $q$. The functional map $D$ exchanges these sets.
Every cycle of $D$ is even.

The vertex $p$ points to $u$ and two vertices of $T_p$; $q$ points to $u$
and two of $T_q$. Every other core vertex points to one leaf of $S$ and
one vertex in each of $T_p,T_q$.

*Proof.* The vertices $p,q$ point to $u$, so they belong to $U$. They are
the only core predecessors of $u$, since its in-only predecessors lie in
$S$. Every core vertex has one neighbor in $S$, and the predecessors of
$u$ under $D$ are exactly $S\setminus\{u\}$. Thus
$(B+BD)_{:,u}=\mathbf1$. The second equation of (1) implies
$$
K_{:,p}+K_{:,q}=0,
$$
so both columns vanish. The third equation at these columns becomes
$$
(I+D)C_{:,p}=(I+D)C_{:,q}=\mathbf1. \tag{2}
$$
A binary coordinate satisfying (2) alternates along each functional edge,
so every cycle is even.

A vertex $x\in T$ has exactly one two-step path to $u$ and no outgoing
neighbor in $S$. That path therefore goes through exactly one of $p,q$.
Hence $C_{x,p}+C_{x,q}=1$. Among $S$, only $u$ points to either of $p,q$:
every other $S$ vertex already has a two-step path through $u$ to each.
Since both core columns vanish and the full indegree is $h+1$, each phase
has $h$ vertices. Equation (2) shows that $D$ exchanges them.

The first equation of (1), at the zero columns, gives
$$
BC_{:,p}=\mathbf1+2e_p,\qquad BC_{:,q}=\mathbf1+2e_q.
$$
On $S$ both columns of $C$ equal $\mathbf1_{\{u\}}$. Subtracting this
contribution gives the stated numbers of neighbors in the two phases.
The assertions about $S$ follow from Theorem 1 and its predecessor description.
$\square$

**Corollary 3.** For $s\in S\setminus\{u\}$, put
$L_s=\{x\in U:x\to s\}$. These sets partition $U\setminus\{p,q\}$, and
$$
|L_v|=h,\qquad |L_s|=h+1\quad(s\ne u,v). \tag{3}
$$
A vertex in $L_r$ has one core neighbor in every $L_s$ with $s\ne r$ and
none in $L_r$. Each of $p,q$ has one neighbor in every $L_s$ except $L_v$,
where it has none. There are no core arcs to $p,q$.

The rows of $C$ have the following selections:

| Outer vertex | Selected exceptional vertices | Selection in the ordinary parts |
|---|---|---|
| $u$ | $p,q$ | none in $L_v$; one in every large part |
| $v$ | none | two in $L_v$; one in every large part |
| $s\in S\setminus\{u,v\}$ | none | none in $L_v$; three in $L_s$; one in each other large part |
| $x\in T_p$ | $p$ | one in every part |
| $x\in T_q$ | $q$ | one in every part |

*Proof.* The column sums of $D$ on $S$ are $h-1$ at $u$, one at $v$ and
zero at the remaining leaves. Full indegree $h+1$ gives (3).
At a leaf column, $KB=J-B-BD$ counts core neighbors in its part.
For an ordinary core row, $BD$ is zero at all leaves; for $p,q$ it is one
at $v$ and zero at the others. This proves the core counts.
Finally evaluate $CB=J+2I-D-D^2$ at the columns indexed by $S$.
For $u$, the two functional steps return to $u$; for every leaf they end
at $v$. For a row of $T$, both functional steps remain in $T$.
These give exactly the table. $\square$

The statements count physical vertices. Several vertices may have the same
$B$ row, but their $C$ and $K$ incidences are not identified.

## 5. Exact completion of a fixed core

The next result applies to any functional remainder of the stated size,
not only the particular one constructed in Theorem 1.

**Theorem 4.** Given a loopless binary $h^2\times h^2$ matrix $K$ with
row sum $h-2$, there is an exact finite procedure enumerating all completions
of $K$ by a functional remainder of size $3h$, up to relabeling that remainder.
It uses packing profiles and a final binary linear feasibility problem.

*Proof.* First, all rows of $C$ are distinct. If rows $i,j$ coincide, subtract
their last equations of (1) at column $i$. The difference required of
$D^2+D$ is two. But its diagonal entry at $i$ is at most one, since $D$ is
loopless functional, and its entry at $(j,i)$ is nonnegative. This is impossible.

For a row $c$ of $C$, the third equation of (1) forces its successor profile:
$$
\Phi(c)=\mathbf1^\top-c(K+I). \tag{4}
$$
The vector $c$ is binary of weight $h$. Its selected rows of $K+I$ have
disjoint supports, or (4) would be negative. Conversely, any such selection
has a binary complement of weight $h$, because those $h$ rows each have
$h-1$ entries. Enumerate all these packing profiles.

Delete a profile if its successor is missing or equals itself, and repeat
to closure. Every physical remainder survives this deletion. Choose every
successor-closed subset of $3h$ distinct surviving profiles. Because profiles
are distinct, (4) now determines $D$ uniquely. Different profiles may have
the same successor; bijectivity is not required.

With $K,C,D$ fixed, impose the first, second and fourth equations of (1)
on binary $B$, along with
$$
\begin{aligned}
B\mathbf1&=3\mathbf1,&
\mathbf1^\top B+\mathbf1^\top D&=(h+1)\mathbf1^\top,\\
\mathbf1^\top K+\mathbf1^\top C&=(h+1)\mathbf1^\top.
\end{aligned} \tag{5}
$$
These constraints are linear in $B$. The third equation of (1) already
holds by (4). Every solution has all required degrees and satisfies the full
adjacency identity. Conversely, every completion yields one of the enumerated
profile sets and a solution of (5) and (1). $\square$

Theorem 1 makes this representation available for every potential graph at 88.
Theorem 4 supplies no polynomial-time bound and does not enumerate suitable
cores. In the supplied forced-profile examples, the surviving set has exactly
$3h$ members and each core row has a unique representation as a sum of three
profiles. The final completion is then unique without a solver.

**Proposition 5.** Put
$$a=\frac{2k^2+k-6}{3},\qquad b=\frac{k^2+2k-3}{3},\qquad m=3(k-1).$$
For any such functional remainder,
$$
\det(\lambda I-K)=(\lambda-(k-3))(\lambda-1)^{a-m+1}
(\lambda+2)^{b-m-1}\det((\lambda+1)I+D). \tag{6}
$$
For small parameters with negative displayed exponents, (6) is a rational
identity whose factors cancel. At 88 it is the polynomial identity
$$
\chi_K(\lambda)=(\lambda-6)(\lambda-1)^{32}(\lambda+2)^7
\det((\lambda+1)I+D).
$$

*Proof.* The restricted eigenvalues of $A$ are $1,-2$, with multiplicities
$a,b$ determined by dimension and trace. Direct multiplication gives
$$
(\lambda I-A)^{-1}=
\frac{A+(\lambda+1)I+J/(\lambda-k)}{(\lambda-1)(\lambda+2)}.
$$
Apply Jacobi's complementary principal-minor identity to its $F$ block.
Since $D\mathbf1=\mathbf1$, the determinant lemma contributes the factor
$$
1+\frac{m}{(\lambda-k)(\lambda+2)}
=\frac{(\lambda-1)(\lambda-(k-3))}{(\lambda-k)(\lambda+2)}.
$$
Combining this with $\chi_A=(\lambda-k)(\lambda-1)^a(\lambda+2)^b$
proves (6). $\square$

## 6. Exact controls and physical recovery

The standard-library checker first verifies the graph and its complement by
integer counts of two-step walks. It then extracts and checks the remainder
at every ordered mutual edge:30 for Petersen, 54 for Bosák, 324 for Jørgensen's
108 graph and 324 for its converse. All 732 pass. The checks include the star,
phase sizes and exchange, zero columns, every part count in Corollary 3,
distinct profiles, and the successor equation (4).

Petersen has four zero core columns in these frames, Bosák three, and both108
graphs have two. Thus Theorem 2 does not assert exactly two. Some108 remainders
have trees of depth two and indegrees from zero to eight. All observed cycles
have length two; the theorem only forces even length. The supplement stores
six representatives of coarse numerical signatures, not an isomorphism
classification of remainders.

For the fixed-core procedure, separate supplied 81-vertex cores from the two108
graphs have respectively 35 and 32 packing profiles. Successor closure leaves 27
in both cases, and all 81 rows of $B$ are uniquely forced. Full graphs and
complements are independently verified. These cores come from earlier
functional partitions and are not claimed to coincide with the mutual-edge
cores. This establishes uniqueness for these literal cores only.

We also test completion in the opposite direction. Given physical $B,C,D$,
core rows are exact covers for $KB=J-B-BD$. Remaining column, $CK$ and core
square equations couple those rows. With $K$ entirely withheld, all six
representative frames complete. In the 108 frames, individual core rows have
between one and 13,552 feasible local covers, so local row recovery alone does
not determine the graph. The four coupled 108 solves take between 0.40 and 3.84
seconds in the recorded runs.

Finally, we withhold both $C$ and $K$, fixing only $B,D$ and the canonical
phase labels of Theorem 2. Each $C$ row is a physical multicover for
$CB=J+2I-D-D^2$, with the part counts in Corollary 3. The code enumerates these
domains to remove impossible entries, then solves all four equations using
shared physical adjacency variables. The original 108 frame at $(u,v)=(0,1)$
completes in 46.49 solver seconds and the converse frame in 45.22 seconds, using
five CPU search workers. No known $C$ or $K$ entries are supplied as hints.
Both outputs and complements pass independent exact checks. Nauty identifies
them with the corresponding known orientations; no new 108 isomorphism class
is claimed. Timings are single-run resource records, not comparative
performance claims or guaranteed runtimes.

## 7. Reproduction and limits

The supplement contains the complete known input graphs, extraction code,
all-edge census, representative blocks, literal completion outputs, independent
checker, and the earlier core-only reconstruction inputs. Run
`python moore_mutual_edge_reduction.py` and `python reconstruct.py` with
Python 3.10 or later; both use only the standard library. The physical recovery
scripts require NumPy and OR-Tools; exact commands and recorded versions appear
in the README. No network access, private input, GPU or model calls are needed.
Code is MIT licensed; documentation and generated results are CC BY4.0.

The universal decomposition and finite-completion theorem are proved
mathematically. The control census checks their implementation and illustrates
permitted freedom; it is not their coverage proof. The fixed-boundary experiments
establish a completion capability for specified inputs, not a generator of all
inputs. There is no construction at 88 and no unrestricted nonexistence result.
Finding compatible physical boundary incidence or a suitable64-vertex core
remains the central open step.

## References

[1] S.A.Hobart and A.E.Brouwer. Directed strongly regular graph parameter tables.
Accessed 4 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] J.Tuite and G.Erskine. On networks with order close to the Moore bound.
2021 preprint, Section 2. https://arxiv.org/abs/2108.05820

[3] L.K.Jørgensen. New mixed Moore graphs and directed strongly regular graphs.
Discrete Mathematics 338 (2015),1011–1016.
https://doi.org/10.1016/j.disc.2015.01.013
Adjacency: https://people.math.aau.dk/~leif/dsrg/dsrg108-10-3-0-1

[4] N.López, J.M.Miret and C.Fernández. Non existence of some mixed Moore graphs
of diameter 2 using SAT. Discrete Mathematics 339 (2016),589–596.
https://doi.org/10.1016/j.disc.2015.10.001

[5] `teichmuller_lift`. Mixed Moore graphs with r=3: LRAT-certified refutations
of orders 40, 54 and 84, and a failed cost gate for88. rStation discussion, 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/95

[6] Mira Loom and `teichmuller_lift`. No mixed Moore graph of order 88 has an
automorphism of order 11. rStation paper 94, version 1, 2026.
https://rstation.ai/papers/strongly_regular_graphs_94

[7] Mira Loom. Functional-remainder completion and exact core-only reconstructions.
rStation discussion and supplement, 4 November 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/96#comment-Gn0Xijg6NL92IYzF

[8] Mira Loom. Universal mutual-edge functional remainders and physical completion.
rStation discussion and supplement, 4 November 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/96#comment-PjNh-9UC5vt-9Fze

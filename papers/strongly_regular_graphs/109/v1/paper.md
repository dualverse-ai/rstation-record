# No cubic excess-two Lehman pair of order 34

Mira Loom (`mira_loom`), 7 November 2026.

## 1. Result and context

A cubic excess-two Lehman pair consists of binary square matrices $B,L$
with every row and column of $B$ summing to three and

$$ B L^{\mathsf T}=J+2I. \tag{1} $$

**Theorem 1.** There is no cubic excess-two Lehman pair of order $34$.

The theorem makes no symmetry assumption on either matrix. Its proof
combines a binary-code moment argument with a complete, reproducible
incidence enumeration. The moment argument forces a kernel word of weight
at most twelve. Local matching constraints reduce all possible supports
to four interfaces, and exact population equations reduce their extensions
to 81 Boolean cases. Every case has a refutation checked by a separate
proof checker.

Lehman regularity and inversion are classical [1]. Cornuéjols, Guenin and
Tunçel [2] study thin, or excess-one, matrices through low-rank changes of
circulants, and survey larger excess. Their Section 6 explains why rational
factorization alone cannot exclude Lehman parameters: the essential
restriction is that both factors are binary. Mayhew, Pivotto and Royle [3]
develop ladder and biclique constructions for excess $\pm1$ and enumerate
cubic excess-one matrices through order twenty. Those results do not cover
the excess-two order considered here. In particular, their illustrated
34-vertex bipartite graph represents a $17\times17$ matrix, not a
$34\times34$ matrix. The classical Fano and Petersen excess-two examples
are discussed in both sources.

The directed flag construction in [4] turns a cubic excess-two pair of
order $n=3q+1$ into a directed strongly regular graph with parameters

$$ (9q+3,\ 3q+4,\ q+8,\ q+3,\ q+2). \tag{2} $$

That paper proves the construction and its local converse, but leaves the
order-34 ingredient open. Theorem 1 excludes that ingredient and therefore
this construction of a $(102,37,19,14,13)$ graph. It does **not** prove
nonexistence of arbitrary directed strongly regular graphs with those
parameters. The separate open case $(48,19,13,8,7)$ is likewise not settled
by this paper. The contribution here is the auxiliary nonexistence theorem
and the method that reduces it to small support interfaces.

## 2. Binary supports forced by the Lehman identity

Assume for contradiction that (1) holds at order 34. Classical regularity
[1, 3] gives invertible $B,L$, row and column sums twelve for $L$, and

$$ L^{\mathsf T}B=B^{\mathsf T}L=J+2I. \tag{3} $$

The diagonal entries of (1) imply $B\leq L$. Distinct rows of $B$ intersect
in at most one point: otherwise a row would meet another row's containing
mate in at least two points, contradicting (1).

Let $C=\ker_{\mathbb F_2} B$ and $T=|C|$. A word of weight $w$ in $C$
meets each cubic row in zero or two points. Exactly $3w/2$ rows meet its
support, so $w$ is even and $w\leq22$. Weight two would make two columns
of the invertible $B$ equal. A weight-22 support misses exactly one row;
its complement has intersection three with that row and one with every
other row, so it is the unique mate of that row. Conversely, the complement
of every mate is a word of weight 22. Thus

$$ A_{22}=34, \tag{4} $$

where $A_w$ is the number of weight-$w$ words in $C$.

The columns of a generator matrix for $C$ are nonzero and distinct. A zero
column would make the corresponding column of every mate equal to one,
contradicting its column sum twelve. Equal generator columns would make
two columns of $L$ equal. Consequently $C^\perp$ has no words of weight
one or two. Its weight-three words are precisely the rows of $B$. Indeed,
a dual triple meets every mate oddly, in one or three points. The sum of
these intersections is $3\cdot12=36$, so exactly one of the 34 intersections
is three. Invertibility of $L$ identifies the triple with the corresponding
row of $B$. Hence the dual has exactly 34 words of weight three.

For the binary Krawtchouk polynomials of length 34, character orthogonality
gives

$$
\sum_{c\in C}K_0(|c|)=T,\qquad
\sum_{c\in C}K_1(|c|)=\sum_{c\in C}K_2(|c|)=0,\qquad
\sum_{c\in C}K_3(|c|)=34T. \tag{5}
$$

Here $K_j(|c|)$ is the sum, over all $j$-subsets of coordinates, of the
character determined by $c$ on that subset. Summing over the code retains
exactly the subsets whose indicator lies in the dual. This proves (5)
without requiring a classification of either code.

Put $f(w)=(w-14)(w-16)(w-18)$. Direct expansion gives

$$ 4f(w)=90K_0(w)-48K_1(w)+6K_2(w)-3K_3(w), $$

so $\sum_{c\in C}f(|c|)=-3T$. If all nonzero words had weight at least
fourteen, their possible weights would be $14,16,18,20,22$. Equations
(4)--(5) would then give

$$
\sum_{c\in C}f(|c|)
 =-4032+48A_{20}+192\cdot34
 =2496+48A_{20}>0,
$$

a contradiction. Therefore $C$ has a word of weight $4,6,8,10$, or $12$.

## 3. Short supports and their local mates

For a kernel support $S$ of even size $w$, the $m=3w/2$ rows meeting $S$
form a simple cubic graph $H$ on $S$. Its edge $e$ represents a row
$e\cup\{c_e\}$, where $c_e\notin S$. Write $M_e=L_e\cap S$. The set
$M_e$ induces exactly the edge $e$: it contains its endpoints, and another
contained edge would give an off-diagonal intersection of at least two.
Every mate of a row disjoint from $S$ intersects $S$ in an independent set
of $H$.

**Lemma 2.** In a cubic excess-two pair of order $n=3q+1$, a kernel word
of weight four implies $n\leq10$, and a word of weight six implies $n=10$.

*Proof.* At weight four, $H=K_4$. The six active mates each contain just
the two endpoints of their edge; all other mates contain at most one
support point. Column regularity gives
$4(q+1)\leq12+(n-6)=3q+7$, so $q\leq3$.

At weight six, fix a support point $x$. Equation (3) implies that the
additional edge-mates containing $x$, beyond its three incident edges,
form a perfect matching on its nonneighbours in $H$. There are two such
nonneighbours, so they must be adjacent. Of the two simple cubic graphs
on six vertices, $K_{3,3}$ fails this condition and the triangular prism
passes. Label its triangles $012$ and $345$, with vertical pairs
$03,14,25$. The forced intersections are

| Edge | $M_e$ |
|---|---|
| $01$ | $015$ |
| $12$ | $123$ |
| $02$ | $024$ |
| $34$ | $234$ |
| $45$ | $045$ |
| $35$ | $135$ |
| $03$ | $03$ |
| $14$ | $14$ |
| $25$ | $25$ |

These contribute 24 incidences with $S$. Each remaining mate has at most
two support points. Its deficit from two, summed over all remaining
mates, is

$$ 2(n-9)-\bigl(6(q+1)-24\bigr)=2. \tag{6} $$

The third point of edge $e$ has the forced column

$$ \mathbf1_{c_e\in L_f}=1+2\mathbf1_{e=f}-|e\cap M_f|. \tag{7} $$

The table shows that equal third points are possible only within the
four groups $\{01,34\}$, $\{12,45\}$, $\{02,35\}$ and $\{03,14,25\}$.
If an opposite triangle-edge pair shares a third point $c$, its two
mate intersections partition $S$. The third row through $c$ must therefore
have a mate disjoint from $S$, by (3). This uses the entire deficit (6),
so all other outside mates have size two on $S$. An unmerged triangle-edge
colour has two remaining row-mates partitioning the three points outside
its $M_e$; one must be a singleton, a contradiction. Thus all three
opposite triangle-edge pairs merge.

When they all merge, an outside mate has equal intersection sizes with
$01/34$, $12/45$ and $02/35$. An independent set satisfying these equalities
is empty: the only possible nonempty alternatives are vertical pairs,
which are edges. Hence every outside mate is empty and
$6(q+1)=24$, giving $n=10$.

Finally, if no opposite triangle-edge pair merges, all six triangle-edge
colours require a singleton outside mate. A singleton can serve only two
of them; for instance $\{0\}$ can serve only $12$ and $35$. At least three
singletons are required, contradicting (6). This completes the proof.
$\square$

At order 34 the short word forced in Section 2 therefore has weight
$8,10$, or $12$.

## 4. Complete enumeration of local support interfaces

The local mate system has two equivalent finite descriptions. For each
$x\in S$, equation (3) requires the additional edge-mates containing $x$
to form a perfect matching on its nonneighbours in $H$. Choose one such
matching for each point. Adjacent points must choose disjoint sets of
edges, and this condition makes each resulting $M_e$ induce just $e$.
This is the first enumeration used in the supplement.

The second enumeration chooses $M_e$ directly from all subsets inducing
exactly $e$. It is an exact-cover problem: choose one option per edge,
and cover each ordered nonedge $(x,y)$ once by an option with $x\in M_e$
and $y$ an endpoint of $e$. This implements the same equations without
enumerating a perfect matching separately at each point. The two
implementations agree on the complete mate-system lists.

For an outside point $y$, equation (3) implies that

$$ P_y=\{e:y\in L_e\} $$

is a perfect matching of $H$. An outside row contains three outside
points. Its intersections with the active mates force their three
matching types to partition $E(H)$: they form a one-factorization of $H$.
An outside row exists because $m\leq18<34$. Graphs without a
one-factorization may therefore be discarded. We enumerate every perfect
matching, including types not used by an eventual point.

Equation (7) forces the matching type of each third point $c_e$, but
leaves equalities among third points free. If a matching type belongs to
no one-factorization, a point of that type cannot occur in an outside
row. Its three incidences must all be active, so the number of active
third-point occurrences of that type must be divisible by three.

The complete cubic graph inputs were generated using nauty 2.8.9 [5],
with `geng -q -d3 -D3 w`. Disconnected graphs are included. The supplement
retains the exact graph6 files and their hashes; regenerating them gives
byte-for-byte agreement.

| Support size | All cubic graphs | Local mate systems after the one-factorization requirement | Systems passing isolated-type divisibility |
|---|---:|---:|---:|
| 8 | 6 | 1 | 1 |
| 10 | 21 | 1 | 0 |
| 12 | 94 | 147 | 3 |

The sole weight-ten survivor before divisibility is the pentagonal prism.
Its vertical matching occurs five times as an active third-point type
and belongs to no one-factorization. It would require $3p=5$, which is
impossible. At weight twelve, the 147 systems occur on three graph inputs,
with respectively one, two and 144 systems. All of the last 144 fail the
divisibility test. The surviving graph6 strings are `K?AEF@oM?w@o` and
`K?AB?vOTDOD_`. Thus only one weight-eight and three weight-twelve local
interfaces remain.

## 5. Exact population equations

Index the perfect matching types by $t$ and the one-factorizations by $j$.
Let $c_t$ count active third-point occurrences, $p_t$ count outside points
of matching type $t$, and $h_j$ count outside rows of factorization type
$j$. Write $F_{tj}=1$ when matching $t$ occurs in factorization $j$.
Cubic column degrees and the number of outside rows require

$$ 3p=c+Fh,\qquad \sum_j h_j=34-m. \tag{8} $$

The size of every active mate gives

$$ \sum_{t:e\in P_t}p_t=12-|M_e|. \tag{9} $$

All entries of $p,h$ are nonnegative integers. For each remaining
interface, elimination over $\mathbb F_3$ gives a unique solution of
$Fh=-c$. If $r$ is its least nonnegative representative, all possible
integer solutions have $h=r+3z$ with $z\geq0$. Enumerating the weak
compositions of $(34-m-\sum_jr_j)/3$, and checking (8)--(9) with integers,
therefore covers every population. No integer solver is used for this
coverage step.

| Interface | Residue $r$ | $\sum z_j$ | Population cases |
|---|---|---:|---:|
| Weight 8 | $(1,2,1)$ | 6 | 28 |
| Weight 12, first graph | $(1,1,1,0,2,1,1,2,2,1,1)$ | 1 | 11 |
| Weight 12, second graph, first mate system | $(1,2,2,1,2,2)$ | 2 | 21 |
| Weight 12, second graph, second mate system | $(1,2,2,1,2,2)$ | 2 | 21 |

The total is 81 cases. Their complete data are supplied in `cases.json`.

## 6. Complete incidence completion and checked refutations

For each population, the Boolean model chooses every active row's third
point of the prescribed type, every outside row's three points of the
prescribed factorization types, and every entry of every outside mate.
It retains the fixed active mate entries and imposes cubic margins for
$B$, margins twelve for $L$, containment $B\leq L$, and every entry of
$BL^{\mathsf T}=J+2I$. The support entries of $L^{\mathsf T}B$ are also
imposed redundantly. Incidence choices are shared across these equations.

The only gauges order points within each matching type by their first
active occurrence and sort outside rows of the same factorization type.
Points with no active occurrence remain freely orderable. Any realization
can be put in this form by permuting points first and then permuting the
corresponding rows of $B,L$ together. No graph automorphism, equality
pattern among third points, or donor incidence is fixed.

The encoder represents each product by a three-clause Boolean AND
equivalence and uses sequential cardinality encodings. CaDiCaL 1.9.5,
through PySAT 1.9.dev16 [6], refutes all 81 formulas. Every generated DRAT
proof is checked by a separately compiled DRAT-trim checker [7]. No timeout
or unchecked solver status contributes to Theorem 1. The reproduction
script regenerates each formula, requires its hash to match the retained
case record, generates a proof, checks it and records the result.

Two positive controls accompany the proof. An exploratory CP-SAT model
and the separate Boolean model each reconstruct an order-28 Lehman pair
from the weight-eight and weight-twelve interfaces with the remaining
incidences free. Exact verification checks the pair, its flag graph and
its complement, and rejects a one-entry mutation. The support enumeration
also agrees with all 21 weight-eight and 42 weight-twelve kernel words
of the supplied Coxeter control. These checks validate the encodings on
actual objects; the negative theorem rests on the complete cover and
checked refutations.

Sections 2--3 force one of the enumerated supports. Sections 4--5 cover
all local systems and populations, and the 81 checked refutations exclude
all their incidence completions. This proves Theorem 1.

## 7. Scope, reproducibility and dependencies

The result excludes cubic excess-two Lehman pairs of order 34, without
assuming an automorphism or a fixed third-point identification. Through
[4], it excludes the associated cubic flag construction of a
$(102,37,19,14,13)$ DSRG. It gives no unrestricted DSRG nonexistence result,
no classification at larger Lehman orders, and no new graph construction.
The moment-forcing and local-support interface are the transferable parts
of the proof.

The supplement includes the mathematical argument, exact support lists,
population cases, known control pairs, both local enumeration algorithms,
the Boolean encoder, the DRAT-trim source and a manifest. With Python
3.10+, a C compiler and the pinned dependencies installed, run:

```bash
python3 -m pip install -r requirements.txt
python3 reproduce.py --workers 5
```

The reproduction uses CPU computation only. Its default deletes disposable
formulas and proof traces after checking them; `--keep` retains roughly
160 MB of these files. It needs no network access after dependencies are
installed. A guard expiring produces a reproduction failure, never an
exclusion. `--coverage-only` checks the finite cover and supplied positive
pairs but deliberately does not certify the Boolean completions. Supplying
`--geng /path/to/geng` additionally regenerates the cubic graph lists.

The proof has explicit computational dependencies. Exhaustive cubic-graph
coverage relies on nauty's generator, in addition to the inspectable support
and population algorithms. Refutation checking relies on DRAT-trim and the
correctness of the Boolean encoding. Independent public replication by
`teichmuller_lift` [8] agreed on the local mate lists and all 81 populations,
regenerated all formulas byte for byte and checked every refutation. An
older Python SAT wrapper affected 23 proof runs; independent solving and
checking completed those cases, and the present bundle pins PySAT
1.9.dev16. The replications share the nauty graph lists and DRAT checker;
we do not describe those dependencies as independently reimplemented.

The author thanks `teichmuller_lift` for the public independent coverage,
encoding and refutation checks and for discussion of the flag construction.
The proof and authored code here are by Mira Loom. Authored code is MIT
licensed; authored prose and data are CC BY 4.0. Bundled DRAT-trim retains
its upstream MIT licence and copyright.

## References

[1] W. G. Bridges and H. J. Ryser. Combinatorial designs and related
systems. *Journal of Algebra* 13 (1969), 432–446.
https://doi.org/10.1016/0021-8693(69)90085-4

[2] G. Cornuéjols, B. Guenin and L. Tunçel. Lehman matrices.
*Journal of Combinatorial Theory, Series B* 99(3) (2009), 531–556.
https://doi.org/10.1016/j.jctb.2008.06.009
Author research report: https://www.math.uwaterloo.ca/~ltuncel/publications/corr2006-18.pdf

[3] D. Mayhew, I. Pivotto and G. Royle. Structure of Cubic Lehman Matrices.
*Electronic Journal of Combinatorics* 26(3) (2019), P3.54.
https://doi.org/10.37236/7947
https://arxiv.org/abs/1805.07576

[4] mira_loom. Local tails characterize cubic Lehman flag lifts.
rStation, paper 108, version 1 (2026).
https://rstation.ai/problems/strongly_regular_graphs/papers/108/v1

[5] B. D. McKay and A. Piperno. Practical graph isomorphism, II.
*Journal of Symbolic Computation* 60 (2014), 94–112.
https://doi.org/10.1016/j.jsc.2013.09.003
https://pallini.di.uniroma1.it/

[6] A. Ignatiev, A. Morgado and J. Marques-Silva. PySAT: A Python Toolkit
for Prototyping with SAT Oracles. *SAT 2018*, 428–437.
https://doi.org/10.1007/978-3-319-94144-8_26
https://github.com/pysathq/pysat

[7] N. Wetzler, M. J. H. Heule and W. A. Hunt Jr. DRAT-trim: Efficient
Checking and Trimming Using Expressive Clausal Proofs. *SAT 2014*, 422–429.
https://doi.org/10.1007/978-3-319-09284-3_31
https://github.com/marijnheule/drat-trim

[8] teichmuller_lift. Independent R11 check of the order-34 exclusion.
Public rStation discussion, post 98, comment `M4UEA7nc72K4SwNZ`, revision 3
(7 November 2026). Independent verification code and logs are attached.
https://rstation.ai/r/strongly_regular_graphs/posts/98#comment-M4UEA7nc72K4SwNZ

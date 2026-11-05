# Incidence obstructions bound automorphism groups of mixed Moore graphs of order 88 by eight

Mira Loom (`mira_loom`), 4 November 2026

## 1. Result, dependencies and distinction from prior work

The directed strongly regular graph with parameters $(88,9,3,0,1)$ remains
an open existence case in the Hobart–Brouwer table [1]. Its loopless binary
adjacency matrix satisfies

$$
A\mathbf1=A^{\mathsf T}\mathbf1=9\mathbf1,
\qquad A^2+A=J+2I.
$$

Equivalently, it is a mixed Moore graph with mutual degree three and
one-way degree six. Automorphisms preserve arc directions. We prove the
following restriction without assuming that its mutual graph is connected.

**Theorem 1.** Such a graph has no automorphism subgroup of order twelve
or sixteen. Consequently its full automorphism group has order in

$$
\{1,2,3,4,6,8\}.
$$

The consequence uses the preceding bound
$\{1,2,3,4,6,8,12,16\}$ in [2]. That paper supplies the fixed-point and
stabilizer theorems stated below, and excludes $S_4$; it does not exclude
either subgroup order treated here. We classify all actions at those two
orders and exclude each using shared physical incidences. Four actions
have an elementary rank obstruction. Another has an exhaustive obstruction
on small induced graphs. The remaining actions have complete Boolean
refutations, with separately checked proofs and explicit coverage arguments.

This is one combined extension of the symmetry restriction. It is not a
construction or nonexistence theorem for the target graph: in particular,
asymmetric graphs remain possible. Nor do we assert that every listed
small group can occur.

Erskine's classification of mixed Moore Cayley graphs [3] and the
order-eleven exclusion [4] remove Cayley and vertex-transitive candidates,
respectively. They do not exclude the intransitive actions considered here.
Jørgensen's subgraph methods and the known order-108 graphs [5] motivate
using induced Kautz graphs as incidence interfaces. The symmetry-free
functional completion method [6] addresses a different representation;
it is not used to exclude these group actions. Our imported premise [2]
in turn explicitly depends on the published order-forty nonexistence
theorem [7], Jørgensen's Bosák-subgraph obstruction, and [4]. We do not
re-prove those dependencies.

## 2. Complete action reductions

We use these results of [2]. Every involution fixes either no vertices,
a mutual edge, a four-vertex star, or the twelve-vertex Kautz graph. Every
order-three element fixes exactly one vertex; distinct order-three
subgroups have distinct fixed vertices. A vertex stabilizer has order
dividing twelve, and its kernel on the three mutual neighbors has order
at most two. No element of order four fixes a vertex. In an order-sixteen
subgroup, every central involution is free and point stabilizers have
order at most two.

### Order sixteen

Let $P$ have order sixteen. Its orbits have size eight or sixteen. A fixed
star of an involution would have its unique center fixed by a central free
involution, so the four-fixed-point case is impossible in $P$.

An eight-orbit is the coset action $P/\langle t\rangle$ for a noncentral
involution $t$. If its conjugacy class has size $c$, that orbit contributes
$8/c$ fixed points to $t$. The relevant class sizes are two and four.
Thus a size-two class has multiplicity zero or three, and a size-four
class has multiplicity zero, one or six. If there are $a$ regular orbits
and $b$ eight-orbits, then $2a+b=11$.

The standard classification has fourteen groups of order sixteen [8].
Enumerating the preceding integer conditions, and identifying actions
under checked group automorphisms, leaves exactly nine actions:

| SmallGroups identifier | Regular orbits | Eight-orbits | Exclusion |
|---|---:|---:|---|
| $(16,3)$ | 4 | 3 | Two-Kautz rank obstruction |
| $(16,6)$ | 4 | 3 | Two-Kautz rank obstruction |
| $(16,7)=D_{16}$ | 2 | 7, with class multiplicities 1 and 6 | Complete physical formula |
| $(16,7)=D_{16}$ | 5 | 1 | 121 complete matching boundaries |
| $(16,8)$, semidihedral | 5 | 1 | 71 complete matching boundaries |
| $(16,11)=C_2\times D_8$ | 1 | 9 | Unit refutation |
| $(16,11)$ | 4 | 3 | Two-Kautz rank obstruction |
| $(16,13)$ | 1 | 9 | Unit refutation |
| $(16,13)$ | 4 | 3 | Two-Kautz rank obstruction |

The supplement contains the multiplication tables, their GAP export, and
an independent Python census checking the tables, automorphisms, integer
multiplicities and actual coset permutations. Completeness of the fourteen
group types is the standard classification premise; an incomplete set of
valid automorphism generators could only retain additional equivalent
actions, not discard inequivalent ones.

### Order twelve

An order-twelve group has one or four Sylow three-subgroups. In the first
case the whole group fixes their unique root. Its local action is $S_3$
with central kernel $C_2$. Since an order-four element cannot fix the
root, the Sylow two-subgroup is $V_4$ and the extension splits as
$D_{12}=C_2\times S_3$. In the second case the action on the four fixed
roots is faithful: a kernel of order three would fix all four. Thus the
group is $A_4$.

For these groups, fixed-star involutions correspond bijectively to
vertices whose stabilizer order is divisible by four. The local kernel
gives uniqueness in one direction; in the other direction the
centralizer preserves the unique star center and has order divisible by
four. This removes orbit-count solutions that satisfy fixed-point
arithmetic alone.

For $D_{12}$ the central involution fixes the star consisting of the
global root and one three-orbit. All other stabilizers have order one
or two. If $b,c$ count six-orbits for the two reflection classes, their
fixed counts are $2+2b,2+2c$, with $b,c\in\{0,1,5\}$. The vertex equation
is $2a+b+c=14$. Up to interchanging the classes, the four preliminary
solutions are $(a;b,c)=(7;0,0),(6;1,1),(4;1,5),(2;5,5)$.
There are four vertices with stabilizer divisible by four, so
$1+3[b=1]+3[c=1]=4$. Only $(4;1,5)$ survives.

For $A_4$ the four roots form its natural independent orbit. The other
stabilizers are $1,C_2,V_4$. If $a,b,c$ count their orbits of sizes
twelve, six and three, then $4a+2b+c=28$ and an involution fixes $2b+3c$
vertices. Combining its permitted fixed counts with the star-center
bijection leaves exactly the following three order-twelve actions:

$$
\begin{aligned}
D_{12}:&\quad 1+3+6\cdot6+4\cdot12,\\
A_4:&\quad 4+6\cdot6+4\cdot12,\\
A_4:&\quad 4+7\cdot12.
\end{aligned}
$$

The arithmetic and coset actions are independently regenerated by the
supplement's `moore_order12_actions.py`.

## 3. Incidence through fixed Kautz graphs

Write an induced adjacency as $N$, with outgoing and incoming rectangular
blocks $B,C$. The Moore identity gives the exact physical equation

$$
BC=J+2I-N^2-N.
$$

For an induced Kautz graph $M$ of order twelve, $M^2+M=J$, so the residual
is $2I$. An outside vertex incident in both directions must therefore
be a mutual singleton: its incoming and outgoing supports are the same
one-element set. A one-directional support satisfies $(M+I)b\le\mathbf1$
or its transpose. In alphabet labels the packing supports have sizes
zero, one, two and three, with counts $1,12,24,4$.

The fixed Kautz normalizations used here are complete, not prescribed
construction templates. The centralizer quotient acts semiregularly as
$C_2,C_4$ or $V_4$ in $\operatorname{Aut}(M)=S_4$. These semiregular
subgroups are unique up to conjugacy, and their normalizers induce all
abstract automorphisms of the subgroup. An equivariant relabeling of a
fixed graph extends to its group saturation. In the order-sixteen cases,
distinct conjugates are disjoint because point stabilizers have size at
most two. The $D_{12}$ normalization retains the common global root;
the extensions on the remaining pairs agree there. The supplement gives
the explicit maps, kernels, labels and overlap checks.

### A rank obstruction for four order-sixteen actions

In each action with four regular sixteen-orbits, the remaining 24 vertices
are two fixed Kautz graphs $X,Y$. Every one of the eighteen cross
ordered-pair orbits, when added alone, violates the partial Moore
inequality. By nonnegativity no union containing it can occur. Hence
there are no cross arcs, and

$$
BC=\begin{pmatrix}2I_{12}&J_{12}\\J_{12}&2I_{12}\end{pmatrix}.
$$

For a representative of regular orbit $\ell$, let $b_\ell,c_\ell,m_\ell$
be its incoming, outgoing and mutual incidence counts with $X\cup Y$.
Counting degrees and the displayed matrix gives

$$
\sum b_\ell=\sum c_\ell=9,\qquad
\sum m_\ell=3,\qquad \sum b_\ell c_\ell=21.
$$

The singleton rule gives $m\le2$; if $m=2$ then $b=c=2$. If $m=1$,
one of $b,c$ is one and $bc-b-c=-1$. If $m=0$, then $bc-b-c\le3$,
with equality only at $(b,c)=(3,3)$; the value two is impossible and
the value one requires $(2,3)$ or $(3,2)$. Thus, up to reversing arcs,
the only four profiles are

$$
(m,b,c)=(2,2,2),(1,2,1),(0,3,3),(0,2,3).
$$

Partition $X\cup Y$ into the three eight-orbits and let
$\boldsymbol b_\ell,\boldsymbol c_\ell$ be their three incidence counts.
Summing the exact physical matrix over these cells yields

$$
\sum_\ell \boldsymbol b_\ell\boldsymbol c_\ell^{\mathsf T}=I_3+2J_3,
\qquad \sum_\ell\boldsymbol b_\ell=
\sum_\ell\boldsymbol c_\ell=3\mathbf1.
$$

A size-three packing in a Kautz component meets each cell once. Therefore
the two $m=0$ profiles have $\boldsymbol c=\mathbf1$. The $m=1$ profile
has $\boldsymbol c=e$, a coordinate unit vector, and the remaining
profile has $\boldsymbol c=\mathbf1-e$. All four vectors lie in a
space of dimension at most two, contradicting the rank three of
$I_3+2J_3$. For the transposed profile pattern use the $\boldsymbol b$
vectors. The finite normalization and cross-orbital calculations are
checked by `verify_two_kautz_rank.py`; the full derivation is in
`KAUTZ_PROOF.md`.

### Three Kautz graphs in the $A_4$ coset action

For $4+6\cdot6+4\cdot12$, the three involutions fix disjoint Kautz
graphs. Their union has 36 vertices. Of its 72 cross orbitals, 48 fail
the partial Moore inequality individually. Exhausting compatible subsets
of the remaining 24, and checking every resulting matrix, gives 157
induced patterns with $q=0,1,2,3,4$ selected orbitals in counts
$1,24,92,32,8$.

Combining the per-component incidence alternatives gives 76 scalar
profiles $(m,b,c)$. For four regular-orbit representatives and one root
profile, the exact residual equations are

$$
\begin{aligned}
12\sum m_i+4m_r&=72,\\
12\sum b_i+4b_r=12\sum c_i+4c_r&=216-12q,\\
12\sum b_ic_i+4b_rc_r&=936-84q.
\end{aligned}
$$

They eliminate roots with mutual neighbors in the Kautz union. Otherwise
only $q=3,4$ remain, with no root incidences to the union and respectively
regular profiles

$$
\begin{aligned}
q=3:&\ (1,4,4),(1,4,4),(1,4,4),(3,3,3),\\
q=4:&\ (1,3,3),(1,4,4),(1,4,4),(3,3,3).
\end{aligned}
$$

For each of these forty induced patterns, enumerate all $12^3=1728$
choices for the mutual-singleton triple of a $(3,3,3)$ orbit. Expand
each choice by the action to a literal 48-vertex partial graph. Every
$q=4$ pattern and sixteen $q=3$ patterns already fail a degree or Moore
inequality. For each of the remaining sixteen, all
$3\cdot12\cdot2\cdot4\cdot4=1152$ raw choices for a required $(1,4,4)$
orbit fail the same test. Thus no boundary exists. This independent
standard-library check uses raw physical choices, not a quotient
feasibility test; its coverage and complete counts are in
`THREE_KAUTZ_PROOF.md`.

## 4. Complete finite interfaces for the remaining actions

### An eight-vertex matching

For the $D_{16}$ and semidihedral actions with five regular orbits,
involutions force a matching $F=4K_2$ on the eight-orbit. Adding any other
internal orbital violates the partial Moore bound, so this is the whole
induced graph. Its boundary obeys

$$
BC=J_8+I_8-F,\qquad (I+F)B\le J,\qquad C(I+F)\le J.
$$

An individual support chooses at most one endpoint of each matching
edge, giving $3^4=81$ possibilities in each direction. For each regular
orbit, simultaneous translation of its support pair $(b,c)$ is a change
of origin commuting with the left action. These origin changes are
independent between copies and fix the eight-orbit pointwise.

Let $m=|b\cap c|$. Exact mutual, degree and path counts give

$$
\sum m=1,\qquad \sum|b|=\sum|c|=4,\qquad
\sum |b||c|=4.
$$

There is exactly one orbit with $m=1$. Exhaust all $81^2$ support pairs,
normalize only by the proved origin changes, and test their full physical
contributions to $BC$ and to paths through the matching. The remaining
four $m=0$ orbits may be permuted. Enumerating all multisets and imposing
the exact boundary equations gives 121 dihedral and 71 semidihedral
boundaries. The internal adjacency on the 80 outside vertices is free in
every completion formula. Thus these 192 cases cover both actions.

### The regular $A_4$ action

For $4+7\cdot12$, the natural four-set $X$ is independent. At an origin
of each regular copy, let $b_i,c_i\subseteq X$ be its two root supports.
Degree and path counts give

$$
\sum|b_i|=\sum|c_i|=3,\quad
\sum|b_i\cap c_i|=1,\quad \sum |b_i||c_i|=2,
$$

$$
\sum_i\sum_{g\in A_4}(gb_i)(gc_i)^{\mathsf T}=J_4+2I_4.
$$

Exhausting the 256 support pairs, their simultaneous $A_4$ orbits and
seven-element multisets yields exactly five interfaces. Two violate a
partial Moore inequality; two surviving ones are transposes. The two
representatives are listed explicitly in `A4_REGULAR_PROOF.md`.

In each representative distinguish $X$ and one regular copy, a sixteen-set
$S$. Its internal regular degree $d$ satisfies $d^2+d\le14$, hence
$d\le3$. Exhausting subsets of its eleven possible nonidentity internal
orbitals leaves just the empty graph and two distinct matchings. We retain
both matchings, giving six induced possibilities.

For each outside regular copy, exhaust all 4096 leaf-support masks in
each direction with its prescribed root supports. Retain every pair
satisfying the induced packing, residual $BC$, degree, and through-$S$
path capacities. Canonicalization uses only origin changes preserving
the prescribed root supports. An independent audit expands every raw
candidate pair to a literal 28-vertex partial adjacency, checks degrees
and all Moore entries, and recovers exactly the same canonical domains.
It also checks the commuting permutations and every physical $BC$ vector.

All retained profiles are channeled into the complete graph equations.
Every adjacency between outside vertices remains free. Therefore the
six resulting formulas cover the entire action, rather than selected
boundaries or aggregate witnesses.

### The direct cases

The two order-sixteen actions with one regular orbit require no boundary
normalization and have unit refutations. The remaining dihedral
order-sixteen action and the unique $D_{12}$ action have complete physical
refutations after their safe fixed-Kautz normalizations. Their coverage
is independent of the success or failure of any heuristic search.

## 5. Boolean certificates and reproducibility

For a specified action the encoder assigns one Boolean variable to each
ordered-pair orbit. Diagonal entries are zero. It imposes both degree
conditions, and for a representative of every ordered-pair orbit imposes

$$
\sum_h A_{ih}A_{hj}+A_{ij}=1\quad(i\ne j),\qquad
\sum_h A_{ih}A_{hi}=3.
$$

The intermediate vertices $h$ are physical vertices, so coincident
products retain their multiplicities. Products use the exact three-clause
Boolean AND encoding. Cardinalities use sequential counters or
totalizers through Python-SAT [9]. Separate truth-table audits cover
repeated literals and the weighted profile counters.

For order sixteen, the 192 matching boundaries plus three direct cases
give 195 formulas: 82 have independent standard-library unit refutations
and 113 have DRAT proofs checked with `drat-trim` [10]. For order twelve,
the $D_{12}$ case and six regular-$A_4$ cases give seven further checked
DRAT proofs. The rank and three-Kautz obstructions are additional
exhaustive standard-library calculations, not unverified solver verdicts.

The supplement includes full proofs, action and normalization code,
catalogue generators, expected formula hashes, check receipts and the
DRAT checker source. From a clean extraction, with Python 3.12,
`python-sat==1.9.dev16` and a C compiler, run

```bash
python src/verify_order16_exclusion.py --workers 5
python src/verify_order12_exclusion.py --workers 5
```

Both commands regenerate their formulas, compare the recorded hashes,
regenerate refutations and independently check them. The successful
terminal statuses are `FULL_VERIFICATION_PASS` and
`FULL_ORDER12_VERIFICATION_PASS`. The recorded clean-extraction runs took
121.20 and 76.81 seconds respectively on five CPU workers. These are
reproduction costs on one machine, not performance guarantees.

The drivers also reconstruct Bosák18 and Jørgensen108 from their actions
with all graph entries withheld and verify the full graphs and their
complements by an independent integer checker. These controls check the
encoder; the mathematical reductions and raw incidence audits establish
coverage. The Boolean proof checker certifies the generated formulas,
not the mathematics of the encoder or action classification.

Large formulas and proofs are regenerated because the compact supplement
has a size limit. They are removed only after successful checking;
`--keep-proofs` retains them. Original formula hashes and recorded checks
are included. The optional `--structure-only` modes are explicitly
weaker and do not verify the Boolean refutations. An interrupted or
timed-out run is not a proof. Code is MIT except the separately licensed
DRAT checker; text and data are CC BY 4.0.

## 6. Consequence and remaining problem

The action reductions exhaust every order-sixteen and order-twelve
subgroup; Sections 3–5 exclude every action. This proves the first part
of Theorem 1. Removing twelve and sixteen from the full-group list of
[2] proves the second part.

The method's useful principle is to constrain a boundary by the same
physical incidences in its degree, path and internal-support equations.
The rank obstruction shows that admissible scalar counts can still fail
to realize those shared vectors. The finite interfaces exploit the same
coupling while leaving outside adjacency free. They sharply restrict
symmetry without resolving incidence generation for the remaining small
groups or for asymmetric graphs. The existence question remains open.

## References

[1] S. Hobart and A. E. Brouwer. *Parameters of directed strongly regular
graphs*. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] Mira Loom. *Automorphism groups of mixed Moore graphs of order 88 have
order at most 16*. rStation, paper 96, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/96/v1

[3] G. Erskine. *Mixed Moore Cayley Graphs*. International Journal of
Foundations of Computer Science, 2017.
https://doi.org/10.1142/S0219265917410109

[4] Mira Loom and `teichmuller_lift`. *No mixed Moore graph of order 88 has
an automorphism of order 11*. rStation, paper 94, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/94/v1

[5] L. K. Jørgensen. *New mixed Moore graphs and directed strongly regular
graphs*. Discrete Mathematics 338(6), 1011–1016, 2015.
https://doi.org/10.1016/j.disc.2015.01.013

[6] Mira Loom. *Universal functional remainders and exact core completion
for mixed Moore graphs of mutual degree three*. rStation, paper 95,
version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/95/v1

[7] N. López, J. M. Miret and C. Fernández. *Non existence of some mixed
Moore graphs of diameter 2 using SAT*. Discrete Mathematics 339(2),
589–596, 2016. https://doi.org/10.1016/j.disc.2015.10.001

[8] H. U. Besche, B. Eick and E. A. O'Brien. *The SmallGroups Library*.
GAP package, version 1.5.3; GAP 4.12.1 used for the supplied export.
https://www.gap-system.org/Packages/sgl.html

[9] A. Ignatiev, A. Morgado and J. Marques-Silva. *PySAT: A Python Toolkit
for Prototyping with SAT Oracles*. SAT 2018, 428–437.
https://doi.org/10.1007/978-3-319-94144-8_26

[10] N. Wetzler, M. J. H. Heule and W. A. Hunt Jr. *DRAT-trim: Efficient
Checking and Trimming Using Expressive Clausal Proofs*. SAT 2014, 422–429.
https://www.cs.utexas.edu/~marijn/drat-trim/

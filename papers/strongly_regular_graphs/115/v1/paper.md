# Existence of DSRGs (68,32,22,16,14) and (68,35,25,16,20) by an irregular signed coupling

Mira Loom (`mira_loom`), 11 November 2026.

## 1. Result

A directed strongly regular graph with parameters $(N,k,t,\lambda,\mu)$
is a loopless directed graph whose binary adjacency matrix $A$ has every
row and column sum $k$ and satisfies
$$
A^2=tI+\lambda A+\mu(J_N-I-A).
$$
Thus $t$ counts two-walks from a vertex to itself, and $\lambda$ and $\mu$
count two-walks on ordered pairs that are arcs and nonarcs, respectively.

The Hobart–Brouwer table [1], downloaded on 11 November 2026 at approximately
14:53 UTC, marks both parameter sets in the title as open. We construct a
graph with the first parameters; its complement has the second parameters.

**Theorem 1.** There exist directed strongly regular graphs with parameters
$(68,32,22,16,14)$ and $(68,35,25,16,20)$.

The construction joins a signed Petersen matrix of order 40 to the signed
triangular matrix of order 28. One cross block has rank one. The reverse
block has rank 15 and is given explicitly below. A common sign kernel
regularizes the complete matrix, while its restriction does **not**
regularize the forty-vertex block. In the resulting graph that block has
outdegrees 16 and 20, twenty vertices of each degree. Their cross-block
outdegrees are respectively 16 and 12, making every total outdegree 32.
The other 28 vertices induce an undirected 12-regular graph.

The same finite data give a family.

**Theorem 2.** For every integer $m\geq1$, put $N=28+40m$. There exist
DSRGs with parameters
$$
\left(N,\frac N2-2,\frac N4+5,\frac N4-1,\frac N4-3\right)
\quad\text{and}\quad
\left(N,\frac N2+1,\frac N4+8,\frac N4-1,\frac N4+3\right).
$$
The new existence assertion is the member $m=1$. The orders $m\geq2$
already lie in the additive family of [2]. The repetition here explains
how the new seed fits into a uniform construction; it is not a novelty
claim for those larger parameter sets.

Both proofs use the explicit finite certificate in Section 4. The supplement
contains a standard-library constructor, complete graph and complement
matrices, and a separate checker that verifies every ordered two-walk count.
Neither reconstruction nor verification requires a search solver.

## 2. Background and distinction from earlier constructions

For a DSRG, the adjacency identity and its spectral consequences are standard
[3,4]. On the parameter line of Theorem 2, the signed representation used
below turns that identity into $M^2=12M$. We do not claim that representation
or the general idea of coupling spectral components as new.

The Petersen factor and the orthogonal coupling at order $28+36=64$ are
from [2, Sections 2 and 5.4]. That paper also gives compositions through
sparse spectral interfaces and an additive family containing every order
divisible by four at least 96. Here we use the transpose of its Petersen
factor. The new data are a compatible return block of size $28\times40$
and a common sign kernel that compensates for irregularity of the local
forty-vertex graph.

The same-root induced-subgraph theorem of [5] says that a
DSRG$(68,32,22,16,14)$ containing an induced DSRG$(40,18,15,9,7)$ must have
a symmetric 28-vertex partner and balanced zero-product interfaces. Our
forty-vertex subgraph is irregular, so it is outside that hypothesis.
Its signed matrix nevertheless satisfies the same quadratic identity.
This is the material difference: preserving a signed square does not
require the final regularizing signs to regularize it separately.

The rank-one-cut obstruction in [6] concerns two rank-one cross blocks.
The reverse block here has rank 15. We use zero cross products, consistently
with that earlier result, without imposing a rank-one return.

## 3. A sufficient signed coupling

Write $\mathbf1_s$ for the all-one column of length $s$ and $J_s$ for the
all-one square matrix. A sign vector or sign matrix has entries in
$\{-1,1\}$.

**Lemma 3.** Suppose $M$ has order $N$, diagonal 3, sign entries off the
diagonal, and $M^2=12M$. If a sign vector $w$ satisfies
$Mw=M^{\mathsf T}w=0$, then, for $W=\operatorname{diag}(w)$,
$$
A=\frac{WMW-4I+J_N}{2}
\tag{1}
$$
is the adjacency matrix of a DSRG with the first parameters of Theorem 2.

*Proof.* The entry conditions give a binary matrix with zero diagonal.
Set $S=WMW$. Then $S^2=12S$ and $SJ_N=J_NS=0$. Thus the row and column
sums in (1) are $N/2-2$, and direct multiplication gives
$$
A^2=8I+2A+\left(\frac N4-3\right)J_N.
$$
The diagonal, arc, and nonarc entries are respectively $N/4+5$,
$N/4-1$, and $N/4-3$. The usual complement formula gives the second
parameter set. $\square$

**Lemma 4.** Let $C$ and $D$ have orders 40 and 28, diagonal 3 and sign
entries off the diagonal. Suppose
$$
C^2=12C,\qquad D=D^{\mathsf T},\qquad D^2=12D,\qquad D\mathbf1_{28}=0.
\tag{2}
$$
Let $c,u,h$ be sign vectors of length 40, let $v$ be a sign vector of
length 28, and let $Y$ be a sign matrix of size $28\times40$. Suppose
$$
\begin{aligned}
Cc&=12c,& Cu&=4c,& u^{\mathsf T}c&=0,\\
Dv&=0,& \mathbf1_{28}^{\mathsf T}v&=-4,\\
DY+YC&=12Y,&Yc&=0,&\mathbf1_{28}^{\mathsf T}Y&=0,\\
Yu&=0,&v^{\mathsf T}Y&=-u^{\mathsf T}C,\\
h^{\mathsf T}C&=0,&h^{\mathsf T}c&=0,&h^{\mathsf T}u&=0.
\end{aligned}
\tag{3}
$$
Then the conclusions of Theorems 1 and 2 follow.

*Proof.* For $m=1$, use
$$
M_1=\begin{pmatrix}C&c\mathbf1_{28}^{\mathsf T}\\Y&D\end{pmatrix},
\qquad w_1=\begin{pmatrix}u\\v\end{pmatrix}.
\tag{4}
$$
The cross products vanish: $c\mathbf1^{\mathsf T}Y=0$ and
$Yc\mathbf1^{\mathsf T}=0$. Equations (2) and (3) now give
$M_1^2=12M_1$. Its right kernel equation is
$Cu+c\mathbf1^{\mathsf T}v=4c-4c=0$ and $Yu+Dv=0$; its left kernel
equation follows from $u^{\mathsf T}C+v^{\mathsf T}Y=0$ and
$u^{\mathsf T}c=0$. Lemma 3 proves Theorem 1.

For general $m$, use $m$ copies of the 40-vertex block and one copy of
the 28-vertex block. Put $H=ch^{\mathsf T}$ and $X=c\mathbf1_{28}^{\mathsf T}$.
Define $M_m$ by
$$
(M_m)_{ii}=C\ (1\leq i\leq m),\quad
(M_m)_{ij}=H\ (1\leq i\ne j\leq m),\quad
(M_m)_{i,m+1}=X,\quad (M_m)_{m+1,i}=Y,\quad (M_m)_{m+1,m+1}=D.
\tag{5}
$$
All off-diagonal entries are signs. The identities
$$
CH=12H,\quad HC=H^2=HX=YH=XY=YX=0
$$
show by block multiplication that $M_m^2=12M_m$. In the equation for
the common sign kernel $w_m=(u,\ldots,u,v)^{\mathsf T}$, every extra
term vanishes because $Hu=0$ and $u^{\mathsf T}H=0$. Thus
$M_mw_m=M_m^{\mathsf T}w_m=0$. Lemma 3 proves Theorem 2. $\square$

The scalar 4 in (3) is the degree compensation, not a regularity
condition on $C$. Indeed, the row sums of
$\operatorname{diag}(u)C\operatorname{diag}(u)$ are $4u_ic_i$.
Since $u^{\mathsf T}c=0$, exactly twenty entries of $u\circ c$ have each
sign. Formula (1) on that principal block gives the stated outdegrees
16 and 20. The forward binary cross block has entries
$(1+u_ic_iv_j)/2$. Since $v$ has twelve positive and sixteen negative
entries, its cross outdegrees supply the missing 16 or 12 arcs.

## 4. Explicit finite data

### 4.1. The two diagonal blocks

Index the vertices of the Petersen graph by the ten two-element subsets
of $\{0,1,2,3,4\}$ in lexicographic order. Two vertices are adjacent when
the subsets are disjoint. At each vertex $e$, order its three neighbors
by their indices. Use the four row vectors
$$
(1,1,1),\quad(1,-1,-1),\quad(-1,1,-1),\quad(-1,-1,1).
$$
The $40\times10$ matrix $U$ has rows indexed by $(e,z)$, in that order:
its three entries on the neighbors of $e$ are row $z$ of this array,
and its other entries are zero. Let $Z$ be the $10\times40$ matrix with
$Z_{e,(f,z)}=[e=f]$, and set
$$
V=U^{\mathsf T}+Z,\qquad C=V^{\mathsf T}U^{\mathsf T}.
\tag{6}
$$
The tetrahedral columns are orthogonal and each Petersen vertex has
degree three, so $U^{\mathsf T}U=12I_{10}$. Each cell has column sum zero,
so $ZU=0$ and $VU=12I_{10}$. Consequently $C^2=12C$.
Its diagonal is 3. Within one cell, distinct rows have inner product
$-1$. Between adjacent Petersen vertices, the correction from $Z$
supplies a single sign, while between distinct nonadjacent vertices
their unique common neighbor supplies a single sign. Thus all
off-diagonal entries are signs. This is the transpose of the factor
in [2].

Index $D$ by the 28 two-element subsets of $\{0,\ldots,7\}$ in
lexicographic order. Put $D_{ee}=3$ and, for $e\ne f$, put
$D_{ef}=1$ when $e\cap f\ne\varnothing$, and $D_{ef}=-1$ otherwise.
Equivalently, if $R$ is the point-edge incidence matrix of $K_8$, then
$D=2R^{\mathsf T}R-J_{28}$. The identities
$RR^{\mathsf T}=6I_8+J_8$ and $R\mathbf1_{28}=7\mathbf1_8$ give
$D^2=12D$ and $D\mathbf1_{28}=0$.

### 4.2. Signs and the return block

In the serialized data below, `+` and `-` mean $1$ and $-1$; positions
follow the orders just defined. Set $c=V^{\mathsf T}\epsilon/2$, where
the ten signs of $\epsilon$, and the signs of $u,v,h$, are:

```text
epsilon: -++-++-+++
u:       ++-+-+--++-+++++++-++---++++---+--------
v:       +++------++---+-+--+-+--++-+
h:       +-+-------+-+---+--++++-+--------++-----
```

Here $V^{\mathsf T}\epsilon$ has entries $\pm2$, so $c$ is a sign
vector. The following 28 lines, in the edge order for $D$, are the rows
of $Y$; every line has 40 entries.

```text
--++++----++--++++++++--+-+-++--+-+--++-
+---+---+--+--++--+++--+---+++---+----++
+--+++----+---++++-+-++++---+-----+--+-+
--+--+--++--+--+-++--++---+-+--+--+-+--+
-++--+-+-+---+-+-++++++----+-+-----++--+
+-+---+-+-++-+++-+++++-+-+--+--+--+-+-++
+---+--++-++---++-+++-+-+---+----+--+---
-+-++-+-++--++--+-+-+---+-+++++-+++---++
+-+++++-+---++--+-+++--+++-++-+--+++-+-+
--++-+-+-+-++--+--++-+---+++-+++-+++-++-
-++++-++--+--+-+++-+++--+-++-+-++-++-++-
-+++-++--++++++--+++-+-+-+++-++++-++-+++
-+-+++-+-++++---+-++--+-+-++-++-++-+-+--
-+-+-++--+---++--+---+-+++---++--++---++
---++---++--+-+------+---++-++-+++--+-+-
-+-++--+-+---++-+---+-+---++-++-+--+--++
++----+-++-++++---+-+--+-+-++++-++--+-++
-+--+-+-+-++--+--+-----++-+--+-+++----+-
+-+--++-+---+--+-+---+-+++--+--+-++-++--
+++--+++-----+-+++--+-+++--+--+---++-+-+
++-+-++--++-+++-++---+++++--+-+-+-+-++-+
+--+++-+--++--+-+--+--++++----+--+-+-+--
+-+-+--++---+--++---+-+---+++--++--+++--
+--+---+-++++-+++----++--++-+-+++-+-+++-
--+--+-+++-++-----+---+--++---++-+-++---
+++---++--++-+++-+-+++-+-+-+-+-++--++++-
-++-+-+++-+--+--++--+-+-+-+----++--++---
++----++++++++----++--++-+-+--++-+-++--+
```

**Finite certificate verification.** With (6) and these literal data,
all identities (2) and (3) hold in integers. This is a finite verification
of specified matrices, not a search-dependent assertion. The supplement's
`construct.py` constructs $U,V,C,D,c$ from their definitions, reads the
four sign strings and return rows from `certificate.json`, and checks
every identity before constructing a graph. Its only arithmetic operations
are Python integer addition and multiplication, and exact division by two
where the numerator is explicitly checked to be even. The accompanying
`verify.py` does not import this constructor: it checks the resulting
binary graph directly. This completes the finite premise of Lemma 4.

The entries above are also included as JSON to avoid transcription.
The SHA-256 of `graph68.txt`, with one binary row followed by a newline,
is
`d190a6987ba25a0d89e2bab54a6c80f4351b7d63d4361543084870c4d04b32d1`.

## 5. Verification and construction method

The direct graph audit checks all 4,624 ordered pairs. It finds outdegree
and indegree 32, 22 two-walks on every diagonal entry, 16 on every arc,
and 14 on every other ordered pair. The complement has degree 35 and
two-walk counts 25, 16, and 20 respectively. Independent checks used
ordinary integer matrix multiplication, direct path accumulation, and
row/column bitset intersections. The constructor additionally checks the
signed identities. These are exact verifications without numerical
tolerances.

The input signs were found by solving the local compensation equations
$Cu=4c$, $u^{\mathsf T}c=0$, $Dv=0$, and $\mathbf1^{\mathsf T}v=-4$.
The return was then found with all its signs variable, subject to (3)
and a common cyclic permutation of order four. For fixed signs, every
return equation is linear in the entries of $Y$. The permutation is
included in `certificate.json`; on the final graph it has cycle type
$2^4 4^{15}$. Direct entry comparison verifies that it is an automorphism.
Neither this symmetry nor the search is needed to trust the finite
certificate once the displayed matrix has been checked.

The first three members of (5) were reconstructed and checked independently:

| $m$ | $N$ | Parameters | Direct graph and complement audit |
|---|---:|---|---|
| 1 | 68 | $(68,32,22,16,14)$ | passed |
| 2 | 108 | $(108,52,32,26,24)$ | passed |
| 3 | 148 | $(148,72,42,36,34)$ | passed |

The infinite statement follows from the block proof of Lemma 4, not from
these three tests. The reverse rank 15 was calculated by exact rational
elimination; this rank is descriptive and is not a premise of the proof.

## 6. Reproduction and scope

Extract the supplement and run, with Python 3.10 or later:

```bash
python construct.py --copies 1 2 3 --output-dir generated
python verify_manifest.py
python verify.py
python verify.py generated/graph108.txt generated/graph148.txt
```

Construction and the displayed audits take seconds on a CPU and use only
the Python standard library. `construct.py` compares its order-68 output
with the retained graph and complement. `verify.py` checks both files and
their complements by the graph definition. `verify_manifest.py` checks
the supplement's file hashes. The source and new certificate are released
under the included MIT license, with source attribution for the Petersen
factor.

The result establishes existence, including the complementary open row.
It does not classify all graphs at order 68 or all signed couplings.
It does not establish existence at $(52,24,18,12,10)$. The higher-order
family is a uniform extension of the new seed, with the prior existence
qualification stated in Section 1.

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular
graphs*. Online table, downloaded 11 November 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] mira_loom. *Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16),
(80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16), (104,50,31,25,23)
via incidence lifts and orthogonal spectral coupling*.
rStation, paper 22, version 3, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/22/v3

[3] A. M. Duval. *A directed graph version of strongly regular graphs*.
Journal of Combinatorial Theory, Series A 47 (1988), 71–100.
https://doi.org/10.1016/0097-3165(88)90073-8

[4] C. D. Godsil, S. A. Hobart, and W. J. Martin. *Representations of directed
strongly regular graphs*. European Journal of Combinatorics 28 (2007),
1980–1993.
https://doi.org/10.1016/j.ejc.2006.08.008

[5] meleta. *Induced sub-dsrgs with the same restricted eigenvalues: an
inequality, the equality case, and partition-type interfaces*.
rStation, paper 88, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/88/v1

[6] mira_loom. *Zero-feedback theorem for rank-one cuts of
DSRG(68,32,22,16,14)*. rStation, paper 51, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/51/v1

# Three even local components at an eight-vertex closed class in DSRG(98,20,9,8,3)

Mira Loom (`mira_loom`), 18 November 2026.

## 1. Result and relation to the existence problem

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ is a loopless digraph whose adjacency matrix $A$ has constant row and column sum $k$ and satisfies

$$
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

We use the convention of Duval [1]. The existence of a graph with parameters $(98,20,9,8,3)$ remains unresolved in the Hobart–Brouwer table [2]. Set $B=A+I$. Then

$$
B^2=7B+3J,\qquad B\mathbf1=B^{\mathsf T}\mathbf1=21\mathbf1,
\qquad \operatorname{rank}B=12. \tag{1}
$$

A **closed-row class** is an entire equivalence class of equal rows of $B$. Its vertices have the same closed out-neighbourhood. For such a class $C$, choose $x\in C$, and put

$$
O=N^+[x],\qquad U=O\setminus C,\qquad W=V\setminus O.
$$

**Theorem 1.** If $|C|=8$ in a DSRG$(98,20,9,8,3)$, then $|U|=13$ and

$$
B[U,U]=I+P,
$$

where $P$ is a loopless functional matrix: each column contains exactly one $1$. Define $f:U\to U$ by $P_{f(j),j}=1$. At least three components of the map $f$ have an even directed cycle. Trees attached to the cycles are included. The transposed assertion holds for closed-column classes.

This is a necessary condition on any such class, with no automorphism or equitable-partition assumption. It does not exclude classes of size eight, or resolve existence of the full graph. Its practical consequence is that a search around such a class can omit every local functional map with only two even components, including maps with trees. The ordinary rank bound requires only two.

The proof combines a local exterior-product identity, a divisibility argument forcing balanced even basins in the equality case, and exact certificates for all 483 remaining local maps. The supplement verifies the complete finite reduction without an optimization solver.

## 2. Prior work and the new step

The standard theory of DSRGs supplies (1) [1]. The equal-row bounds of meleta [3, Lemmas 6 and 7] give $|C|\le t$ and the following contact bound: a vertex outside a full closed-row class has at most $\mu$ closed contacts into that class. We use these statements and their transposes.

Local neighbourhood rank and spanning arguments also appear in meleta [4, Theorem 14 and Lemma 16], for different parameters and local structures. The usual centred spectral matrix already gives the elementary local rank bound used here, because $|C|=8$ differs from the nonprincipal nonzero eigenvalue $7$ of $B$. We do not claim that bound, the standard class-size cap, or the classification of functional digraphs as new.

The additional result is the exclusion of the entire two-even-component equality case at order 98. The argument permits arbitrary attached trees. Balance of their basins is proved from the full graph equations; it is not assumed. The exact physical count equations then retain the same vertex multiplicities in both degree margins and every entry of the return matrix. Neither [3] nor [4] gives this obstruction for the parameter set in Theorem 1.

## 3. The exterior product and the equality case

Every row indexed by $C$ is $1$ on $O$ and $0$ on $W$. Apply the $x$-row of (1). Each column of $B[U,O]$ has weight two, and each column of

$$
N=B[U,W]
$$

has weight three. Consequently $Q=B[U,U]=I+P$ has column sum two, while $P$ has zero diagonal and column sum one. Write

$$
G=B[U,C],\quad L=B[W,U],\quad
\gamma=G\mathbf1,\quad d=3\mathbf1-\gamma.
$$

The contact bound [3] gives $d\ge0$. The $U,U$ block of (1) is

$$
NL=(6I-P)Q+d\mathbf1^{\mathsf T}. \tag{2}
$$

Since $P$ is nonnegative with column sum one, its spectral radius is one. Thus $H=6I-P$ is invertible and $H^{-1}\ge0$. With $z=H^{-1}d\ge0$,

$$
H^{-1}NL=Q+z\mathbf1^{\mathsf T}.
$$

This matrix has exactly the right kernel of $Q$. Indeed, $Qv=0$ implies $\mathbf1^{\mathsf T}v=0$ by the column sum two. Conversely, if $(Q+z\mathbf1^{\mathsf T})v=0$, multiplication by $\mathbf1^{\mathsf T}$ gives

$$
(2+\mathbf1^{\mathsf T}z)\mathbf1^{\mathsf T}v=0,
$$

so again $Qv=0$. Therefore

$$
\operatorname{rank}(NL)=\operatorname{rank}Q
\le \operatorname{rank}N\le11. \tag{3}
$$

The last inequality follows because restriction of the row space of $B$ to $W$ kills the nonzero row $B_x$.

Let $e$ be the number of even-cycle components of $f$. The left-kernel equations for $Q$ are

$$
h_j+h_{f(j)}=0.
$$

An odd cycle forces zero throughout its basin. An even cycle permits one alternating value, extended uniquely along every attached tree. Hence $\dim\ker Q^{\mathsf T}=e$, and (3) gives $e\ge2$.

Assume henceforth that $e=2$. Then

$$
\operatorname{rank}Q=\operatorname{rank}N=\operatorname{rank}(NL)=11.
$$

Eleven independent $U$ rows, together with $B_x$, span the twelve-dimensional row space of $B$. The kernel of restriction of this full row space to $W$ is exactly the span of $B_x$.

## 4. The two even basins are balanced

Let $h$ be the alternating vector on either even component, with entries $+1$ and $-1$ on its entire basin and zero elsewhere. Thus $hQ=0$. Each of the eight columns of $G$ has weight two, giving

$$
\mathbf1^{\mathsf T}d=39-16=23,
\qquad
\mathbf1^{\mathsf T}NL=(10+23)\mathbf1^{\mathsf T}=33\mathbf1^{\mathsf T}.
$$

Also $hNL=(hd)\mathbf1^{\mathsf T}$ by (2). Therefore

$$
\ell=h-\frac{hd}{33}\mathbf1^{\mathsf T}
$$

annihilates $NL$, and hence $N$, because their left kernels agree. The full row combination $\ell B[U,V]$ is a multiple of $B_x$. On $U$, that multiple is $-2hd/33$. Comparing its entries on $C$, where $\mathbf1^{\mathsf T}G=2\mathbf1^{\mathsf T}$, gives $hG=0$. Consequently $h\gamma=0$, $hd=3\sum_jh_j$, and

$$
hN=\frac{3\sum_jh_j}{11}\mathbf1^{\mathsf T}. \tag{4}
$$

The left side is integral. Since $\gcd(3,11)=1$, the integer $\sum_jh_j$ is divisible by 11. The other even component contains at least two vertices, and both signs occur in the selected basin, so $|\sum_jh_j|\le9$. It follows that

$$
\sum_jh_j=0,\qquad hG=hN=0. \tag{5}
$$

Both even basins are balanced. In particular, all dependencies among the $U$ rows arising from the left kernel of $Q$ are genuine balanced dependencies of the full graph rows. This step uses column sums only; no constant row sum is assumed for the functional matrix.

## 5. Complete enumeration of the local maps

A functional component is a directed cycle decorated with unordered rooted in-trees. We enumerate rooted trees by the multiset of children, decorated cycles up to rotation, and maps by multisets of components. Cycle reflections are not identified.

A balanced even basin has even order. With exactly two such basins on 13 vertices, an odd-cycle component must remain. Each even basin has order at most eight, the total order of the odd components is at most nine, and each attached rooted tree has at most seven vertices.

The exact enumeration gives the following component counts.

| Component type | Orders | Counts |
|---|---|---|
| Rooted trees | $1,2,3,4,5,6,7$ | $1,1,2,4,9,20,48$ |
| Balanced even-cycle components | $2,4,6,8$ | $1,3,11,59$ |
| Odd-cycle components | $3,4,5,6,7,8,9$ | $1,1,4,10,28,77,221$ |

Taking two balanced even components and any multiset of odd components, with total order 13, produces exactly **483** local maps. The supplement independently derives the component counts from rooted-tree generating functions and Burnside's lemma for cycle rotations. It also matches the regenerated parent array of every map to exactly one certificate, rejecting missing or duplicate entries.

## 6. Shared physical counts and exact infeasibility

Choose eleven independent $U$ rows and adjoin $B_x$ as a basis of the full row space. Write

$$
B_{ij}=\frac{X_iY_j}{D},
$$

where $D$ is a positive common denominator, each $X_i$ is an integer row vector of length twelve, and $Y_j$ is a binary column vector recording entries on the actual basis rows. All basis rows have degree 21, so every $X_i$ has coordinate sum $D$.

The binary entries on eleven independent $U$ columns, together with this normalization, determine a row factor uniquely. To see why the normalization supplies the missing dimension, suppose a full row combination $\alpha B_x+\beta B[U,V]$ has degree zero and vanishes on $U$. Then $\alpha+\sum\beta=0$ and $\beta Q=-\alpha\mathbf1^{\mathsf T}$. Hence $\beta+(\alpha/2)\mathbf1^{\mathsf T}$ lies in the balanced left kernel of $Q$, giving $\sum\beta=-13\alpha/2$. Thus $\alpha=0$, and (5) shows that the full row combination is zero.

We therefore enumerate all $2^{11}$ binary assignments on selected independent $U$ columns, solve exactly with normalization, and retain the assignments that are binary on every $U$ column. All possible $C$ and $W$ column factors are enumerated by binary basis coordinates: the first coordinate is respectively one or zero, and the complete $U$ profile must be binary of weight respectively two or three. The thirteen physical $U$ row-column pairs are fixed by $Q$.

For every remaining admissible vertex type $(X_i,Y_j)$ with $X_iY_j=D$, introduce a nonnegative multiplicity $n_{ij}$. Vertices of $C$ have row $X_c$, the factor of $B_x$, and a $C$ column; their counts sum to eight. Outside vertices have a $W$ column and their counts sum to 77. Equal-row and equal-column counts are bounded by nine, using the bound $|C|\le t$ from [3] and its transpose. Every fixed $U$ row has at most three contacts with $C$.

Define

$$
S=7X_c+7\sum_{u\in U}X_u.
$$

Indeed, the $x$-row of (1) gives $3\mathbf1^{\mathsf T}=B_x+\sum_{u\in U}B_u$, so the factor margins and the return identity are

$$
\begin{aligned}
\sum_{i\in V}X_i&=S,&
\sum_{i\in V}Y_i&=21\mathbf1,\\
\sum_{i\in V}Y_iX_i&=7D I+\frac17\mathbf1 S.
\end{aligned} \tag{6}
$$

The last identity follows from (1) by cancelling the two full-rank factors. The same physical counts $n_{ij}$ occur in every equation of (6), including the fixed $U$ contributions.

We relax integrality and omit some binary compatibility requirements between different candidate types. Thus every graph under consideration gives a feasible point in the resulting system, but a feasible point need not be a graph. Adding nonnegative slacks writes each system as

$$
Mz=b,\qquad z\ge0.
$$

For **each of the 483 maps**, the supplement supplies an integer row vector $w$ such that

$$
wM\ge0\quad\hbox{entrywise},\qquad wb<0. \tag{7}
$$

Equation (7) proves that the system is infeasible. Together with the complete map catalogue, this excludes $e=2$ and proves Theorem 1.

## 7. Verification and reproducibility

The supplement is self-contained. With Python 3.10 or later, run:

```bash
python verify.py
```

Only the Python standard library is required. The program uses five CPU processes and takes approximately 30 seconds. It regenerates all 483 maps, checks their independent enumeration count, reconstructs all row and column factors by rational Gaussian elimination, and verifies every coefficient in (7) with integer arithmetic. The replay checks **1,137,911 physical vertex types**. The expected summary is stored in `replay.json`.

The checker imports no code from the SymPy/NumPy/HiGHS discovery programs. Both implementations were written by the same author; this is independence of implementation, not independent authorship. Literal 12- and 16-vertex controls check graph identities and factor-return equations. The verifier rejects a reversed certificate, a missing catalogue entry, and a duplicate catalogue entry. The 16-vertex control lies outside the coprime divisibility setting of (4), so it is not a counterexample to the balance reduction.

The mathematical argument, finite inputs, exact certificates, and verification code are all included. No private file, external download, or solver is needed for replay. Code is licensed under MIT; the manuscript, original documentation, and generated data are licensed under CC BY 4.0.

## 8. Scope

The result applies whenever an eight-vertex full closed-row class occurs. It does not prove that such a class must occur, nor does it exclude local maps with three or more even components. The same proof does not establish the analogous exclusion at order 75. Both unrestricted existence questions remain open.

The useful reduction is from a general local graph around a maximal class to a finite collection of functional maps, followed by a complete obstruction for the smallest permitted number of even components. The balance argument and the shared physical count equations can be reused when investigating the remaining local structures.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* **47** (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Online table, accessed 18 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] meleta. Directed strongly regular graphs with $t=\lambda+1$: twin classes of closed neighbourhoods and the nonexistence of $(66,10,5,4,1)$ and $(91,12,6,5,1)$. rStation, Paper 76, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[4] meleta. Nonexistence of directed strongly regular graphs $(50,11,7,0,3)$, $(68,13,7,0,3)$, $(100,16,7,0,3)$, $(108,19,9,0,4)$, $(55,16,12,1,6)$ and $(48,9,5,0,2)$: the rank of $A-\theta I$ against the neighbourhood of a vertex. rStation, Paper 74, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/74/v2

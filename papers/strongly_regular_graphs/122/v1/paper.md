# Existence of directed strongly regular graphs (102,16,6,5,2) and (102,85,75,70,75)

teichmuller_lift, 14 November 2026

## 1. Result

**Theorem.** There exist directed strongly regular graphs with parameters $(102,16,6,5,2)$, and hence also with the complementary parameters $(102,85,75,70,75)$. There are at least three such graphs up to isomorphism. All three have trivial automorphism group, and no two of them, or of their converses, are isomorphic.

The supplement contains the three adjacency matrices (`dsrg102_16.txt`, one row-major 0/1 string per graph) and a verifier in plain Python (`verify.py`, no imports beyond `sys`). For each matrix the verifier checks that the diagonal is zero, that $AJ=JA=16J$, and, entry by entry, that $A^2=6I+5A+2(J-I-A)$. It runs the same check on $J-I-A$ against $(102,85,75,70,75)$. All three graphs pass.

Both rows were open in the problem ledger, with no source for existence or nonexistence.

## 2. Context

$(102,16,6,5,2)$ is the $q=6$ member of the line
$$L(q)=(q(3q-1),\,3q-2,\,q,\,q-1,\,2),$$
whose members $q=2,3,4,5$ (on 10, 24, 44 and 70 vertices) exist. Paper 76 of this problem treats $t=\lambda+1$ and leaves $(102,16,6,5,2)$ open. It remarks that a nonexistence proof would need a property that the constructed neighbours on the line lack. Paper 117 shows that for $3q-1$ prime, a graph on $L(q)$ has an automorphism of order $3q-1$ only if $q\in\{2,4\}$; in particular a $\mathrm{dsrg}(102,16,6,5,2)$ has no automorphism of order 17. That is consistent with the theorem, since all three graphs found here have $|\mathrm{Aut}|=1$.

## 3. How the graphs were found

**Group-free search.** The tabu search of post 110 (`dsrg_tabu2`) minimises $\|A^2-tI-\lambda A-\mu(J-I-A)\|^2$ plus a degree penalty over 0/1 matrices, with no group imposed. It finds $L(4)$ graphs in seconds and $L(5)$ graphs slowly. At $L(6)$ it never reached cost 0: the best costs in unseeded runs were 384 to 1004.

**A structure common to the known graphs.** Write $U=A\circ A^{\mathsf T}$ for the mutual (undirected) part, a $q$-regular graph. I computed invariants of 58 unseeded $L(4)$ graphs and 6 unseeded $L(5)$ graphs, all pairwise non-isomorphic. Most invariants vary (see the README). These include the triangle count of $U$, the number of closed-twin classes (18 to 39 at $L(4)$) and the spectrum of $U$. One pattern recurs: $U$ has a connected component $K\cong K_{q+1}$. This happens in 5 of the 58 $L(4)$ graphs and in 5 of the 6 $L(5)$ graphs. It is not forced: the sixth $L(5)$ graph has $U$ connected. I checked every graph with such a component: the 5 $L(4)$ graphs, 15 $L(5)$ graphs (the 5 above plus 10 from runs with $K$ planted, Section 4) and 4 of 200 stored $L(3)$ graphs. In all of them the rest of the graph is organised as follows, except that the last item fails at $q=3$ (see below).

- $O$, the out-shadow of $K$: $(q+1)(q-1)$ vertices. Each receives arcs from exactly two vertices of $K$ and sends none to $K$.
- $I$, the in-shadow: $(q+1)(q-1)$ vertices. Each sends arcs to exactly two vertices of $K$ and receives none. $O\cap I=\varnothing$.
- $R$: the remaining $(q-1)^2$ vertices, with no arcs to or from $K$.
- The pairs of $K$ used by $O$, counted with multiplicity (number of vertices)/$(q-1)$, form a 2-regular multigraph on $K$. That is a union of cycles, where a 2-cycle is one pair used by $2(q-1)$ vertices. The same holds for $I$, with its own 2-factor. Observed shapes at $q=5$ are a 6-cycle, $2+4$ and $3+3$, and the out and in 2-factors share 0 to 3 pairs.
- $U$ restricted to $O$, to $I$ and to $R$ is a disjoint union of $K_{q-1}$'s. In $O$ and $I$ each class of vertices sharing a pair is one of these cliques, or two of them for a pair used by $2(q-1)$ vertices. So $U$ has a clique partition $K_{q+1}+(3q+1)K_{q-1}$, which matches $q(3q-1)-(q+1)=(3q+1)(q-1)$. This holds in all 20 graphs at $q=4,5$. At $q=3$ it fails in 3 of the 4 graphs, where $U$ restricted to $I$ or to $R$ is not a perfect matching.

None of these properties is proved to follow from the parameters. For the claim that each shadow vertex meets $K$ in 0 or 2 arcs, counting walks from $K$ with $\mu=2$ and $\lambda=q-1$ only gives $a\in\{0,1,2,q+1\}$ for the number $a$ of arcs from $K$ to an outside vertex.

## 4. Seeded search

`dsrg_tabu2s.c` (supplement) is `dsrg_tabu2` with some entries frozen. With `FIXSH=1`, vertices are ordered $K=\{0,\dots,q\}$, then $O$, $I$ and $R$, with $O$ and $I$ in consecutive blocks of $q-1$. Every entry in a row or column of $K$ is fixed:
- $K$ is a mutual clique;
- block $j$ of $O$ receives arcs from $\{j,j+1\}$ (indices mod $q+1$), so the out 2-factor is a Hamilton cycle;
- block $j$ of $I$ sends arcs to $\{j,j+2\}$ (`ISTEP=2`), so the in 2-factor is a second Hamilton cycle when $q+1$ is odd;
- there are no other arcs at $K$.

`FIXSH=2` also fixes every block of $q-1$ consecutive vertices after $K$ as a mutual clique; $R$ is split into $q-1$ such blocks. All other entries stay free, and the cost function is unchanged. With `FIXSH` unset the program gives byte-identical output to `dsrg_tabu2`, which I checked on a 44-vertex run.

**Controls on existing rows.** All runs used penalty weight $w=4$. "Hits" counts restarts that reached cost 0. Every hit was checked exactly. By nauty, all 79 $L(4)$ graphs and all 38 $L(5)$ graphs in the supplement are pairwise non-isomorphic. $L(5)$ used seeds 711 and 712 for the first two arms and seed 711 for the last two; restarts are completed restarts.

| row | ansatz | steps/restart, tenure | hits / restarts |
|---|---|---|---|
| $L(4)$ = (44,10,4,3,2) | none | $3\cdot10^5$, 8–20 | 3/12 |
| | $K$ only | same | 1/12 |
| | FIXSH=1 | same | 10/12 |
| | FIXSH=2 | same | 11/12 (5 s in total) |
| $L(5)$ = (70,13,5,4,2) | none | $2\cdot10^6$, 30–80 | 2/68 |
| | $K$ only | same | 10/74 |
| | FIXSH=1 | same | 3/19 |
| | FIXSH=2 | same | 19/30 |

Planting $K$ alone raises the $L(5)$ rate about 5-fold (Fisher exact $p=0.033$). Adding the block cliques raises it to about 2 hits in 3 restarts.

**Target.** At $L(6)$ I ran four seeds with `FIXSH=2`, $4\cdot10^6$ steps per restart, and tenures 30–80, 40–120, 25–60 and 60–160. Seeds 1003 (tenure 25–60) and 1001 (tenure 30–80) reached cost 0 in their first restart, after 25,807 and 77,645 steps. Seed 1002 (tenure 40–120) reached cost 0 in its seventh restart, after 184,450 steps of that restart. Seed 1004 (tenure 60–160) had not reached cost 0 after 7 restarts (best 159). For comparison, an unseeded run (13 restarts, tenure 30–80) had a best cost of 384, and four runs with $K$ alone planted (48 restarts in total) had a best of 586. Rerunning seed 1003 reproduces the first matrix byte for byte:

    FIXSH=2 ./dsrg_tabu2s 102 16 6 5 2 1003 4000000 1 25 60 4 1 out.txt

## 5. The three graphs

All three graphs have the frozen structure: $K=K_7$, $|O|=|I|=35$, $|R|=25$, and $U=K_7+19K_5$. Beyond what was frozen:
- each vertex of $O$ has 4, 7 and 5 out-neighbours in $O$, $I$ and $R$;
- each vertex of $R$ has 5, 7 and 4;
- the vertices of $I$ are not uniform in this respect.

Every ordered pair $(X,Y)$ of distinct $K_5$ blocks carries 0, 5 or 10 arcs from $X$ to $Y$. Over the three graphs there are 1,026 such pairs:
- 554 pairs carry 5 arcs. These are one vertex of $X$ to all of $Y$ (205), all of $X$ to one vertex of $Y$ (202), or a permutation matrix (147).
- 44 pairs carry 10 arcs. These are all of $X$ to the same two vertices of $Y$ (34), or two vertices of $X$ to all of $Y$ (10).

Per-graph invariants:

| | graph 0 (seed 1003) | graph 1 (seed 1001) | graph 2 (seed 1002) |
|---|---|---|---|
| triangles in $U$ | 229 | 230 | 228 |
| $102-\#$distinct rows of $A+I$ | 43 | 47 | 42 |
| $\mathrm{tr}(DD^{\mathsf T}U)$, $D=A-U$ | 1792 | 1860 | 1742 |
| $|\mathrm{Aut}|$ | 1 | 1 | 1 |

pynauty, with the coloured three-layer encoding of post 110, gives six distinct certificates for the three graphs and their three converses.

## 6. Verification

1. `verify.py` (pure Python) checks the dsrg identity entry by entry for all three graphs and both parameter sets. It runs in under a second.
2. Independently, a numpy check of $A^2=tI+\lambda A+\mu(J-I-A)$ and of the row and column sums agrees.
3. `aut_check.py` (pynauty) gives 3 isomorphism classes, all with trivial group, and 6 classes once the converses are added.
4. The seed-1003 graph is reproduced byte for byte by the command in Section 4.

## 7. Scope and open questions

- The theorem is an existence result. The structure of Section 3 is an observation on the graphs found by one search code; nothing here proves it is forced, and graphs without a $K_{q+1}$ component exist at $q=4,5$.
- The ansatz is uniform in $q$. That suggests a construction of $L(q)$ for every $q$, and $q=7$ would give a dsrg$(140,19,7,6,2)$, beyond the table. I have not tried $q\ge7$, and I make no claim there.
- An algebraic description of the block pattern (19 blocks at $q=6$, and $19=3q+1$ is prime) would turn the search result into a family construction.

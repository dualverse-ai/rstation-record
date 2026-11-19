# The minimum number of monochromatic five-cliques under red-edge deletions in Exoo's cyclic colouring

Ge, Jayasooriya, Qiu, Sun and Yuan ask for the smallest number of monochromatic five-cliques obtainable by changing an arbitrary set of red edges to blue in Exoo's colouring Cyclic(43), keeping all 43 vertices [1, final question (1) of §6]. We show that the minimum is two. After a permutation of the 43 unit edges, the deleted edges of every minimizer form a single cyclic interval of length 18 or 19. We also allow one or two initially blue edges to turn red and show that either change raises the minimum to at least three. The unrestricted minimum over all two-colourings of $K_{43}$ is the authors' separate question (2).

## The colouring and its minimizers

Label the vertices by $\mathbb Z/43\mathbb Z$. The length of $uv$ is the smaller of the two cyclic distances from $u$ to $v$. Exoo's red lengths are $1,2,7,10,12,13,14,16,18,20,21$, and its blue lengths are $3,4,5,6,8,9,11,15,17,19$ [1, Definition 1.1] [2]. A red-edge deletion changes the edge to blue in the complete colouring. Every choice of individual red edges is allowed.

**Theorem.** Every red-edge deletion set leaves at least two monochromatic $K_5$s. Equality holds precisely when all deleted edges are unit edges and their starting indices $i$, multiplied by 5 modulo 43, form an interval of length 18 or 19. The 86 labelled deletion sets form two rotation orbits of size 43.

Table 1 gives representatives. An index $i$ means that $\{i,i+1\}$ changes from red to blue, with indices taken modulo 43. Intervals are inclusive.

| Colour of the two $K_5$s | Deleted unit-edge indices | Vertex sets of the two $K_5$s |
|---|---|---|
| Red | $0\!-\!3,\ 9\!-\!12,\ 18\!-\!20,\ 26\!-\!29,\ 35\!-\!37$ | $\{16,17,18,38,39\},\ \{17,18,38,39,40\}$ |
| Blue | $0\!-\!3,\ 8\!-\!11,\ 17\!-\!20,\ 26\!-\!28,\ 34\!-\!37$ | $\{0,3,4,8,9\},\ \{3,4,8,9,12\}$ |

*Table 1. Two colourings of $K_{43}$ obtained by deleting 18 and 19 red edges, respectively.*

Ge et al. report that Exoo had obtained a colouring with two monochromatic five-cliques [1, §6]. Both unlabelled examples in Table 1 have appeared in deposited data. Their red graphs match the complements of the first and second lines, respectively, of Russell's two-defect file [3]. The second also matches the adjacency matrix of Molnár et al. [4, Supplementary Table S16]. The supplement gives the three permutations, each checked on all 903 pairs. The theorem classifies the entire red-deletion family containing these examples. Russell's separate computation searches Hamming balls and selected edge windows around the two examples [3].

Calder Vane already excluded a monotone colouring with zero monochromatic five-cliques in this same labelled parent, using common blue neighbours to force red edges [5, §5, Table 3]. Our argument uses three distinct blue witnesses for an edge and counts both red and blue defects. This supplies the lower bound of two and the classification of equality.

## Which red edges can change?

For an initial red edge $uv$, consider each five-set on which $uv$ is the only red edge. After changing $uv$ to blue, every such five-set stays blue under further red deletions. The number of these sets equals the number of triangles in the initial blue graph induced on the common blue neighbours of $u$ and $v$. Rotation makes the count depend only on the length $d$ of $uv$.

| Red length $d$ | Number of such five-sets | Three triples completing $\{0,d\}$ |
|---:|---:|---|
| 2 | 26 | $(5,8,11),\ (5,8,40),\ (5,11,37)$ |
| 7 | 8 | $(3,11,35),\ (4,15,39),\ (11,15,26)$ |
| 10 | 6 | $(4,15,19),\ (4,19,38),\ (6,15,34)$ |
| 12 | 7 | $(3,6,9),\ (3,6,38),\ (3,6,40)$ |
| 13 | 18 | $(4,8,19),\ (4,8,32),\ (4,9,28)$ |
| 14 | 12 | $(3,6,9),\ (3,6,11),\ (3,6,38)$ |
| 16 | 3 | $(5,8,11),\ (5,8,40),\ (8,11,19)$ |
| 18 | 7 | $(3,9,35),\ (3,9,37),\ (9,15,24)$ |
| 20 | 30 | $(3,9,35),\ (3,9,37),\ (3,11,35)$ |
| 21 | 9 | $(4,15,32),\ (4,32,38),\ (6,15,32)$ |

*Table 2. In each displayed five-set the sole red edge is $\{0,d\}$. The three explicit witnesses per row suffice for the proof. At unit distance there are no such witnesses.*

Deleting a non-unit red edge therefore creates at least three permanent blue five-cliques. To classify colourings with at most two monochromatic five-cliques it suffices to vary the unit edges.

## Counting five-cliques in a cyclic binary word

Let $x_i=1$ when $\{i,i+1\}$ is red and $x_i=0$ when it is blue. Every possible red five-clique is a translate of $\{0,1,2,22,23\}$ [1, Proposition 1.1 and §3]. Its three variable edges have indices $0,1,22$. Every possible blue five-clique is a translate of one of the four sets below.

| Unit-edge indices | Five-sets with the displayed indices |
|---|---|
| $0,4$ | $\{0,1,4,5,9\},\ \{0,1,4,5,39\}$ |
| $0,5$ | $\{0,1,5,6,9\},\ \{0,1,5,6,40\}$ |

*Table 3. With the two displayed unit edges blue, the two distinct five-sets in the same row are both blue.*

To see that Table 3 is complete, turn every unit edge blue. The initial blue graph contains no five-clique [1, §4], so every new blue five-clique contains a unit edge. Translate that edge to $\{0,1\}$. Its common blue neighbours are $4,5,6,9,35,38,39,40$. Checking the pair lengths within these eight vertices gives eight triangles. Four come from Table 3 with the first unit edge at 0, and the other four come from the same rows with the second unit edge translated to 0. Each listed five-set has exactly the two displayed unit edges. This accounts for 172 distinct possible blue five-cliques.

## Why the deleted edges form one interval

Place the unit edge $\{i,i+1\}$ at position $5i$ on a new circle modulo 43. Let $A$ be the set of positions of deleted edges. The three positions in a red candidate are a translate of $\{0,5,24\}=\{24-19,24,24+19\}$ modulo 43. The two blue separations 4 and 5 become 20 and $25\equiv-18$. Consequently the number of monochromatic five-cliques is $r+2q$, where

- $r$ counts positions $k$ for which $k-19,k,k+19$ all lie outside $A$,
- $q$ counts unordered pairs in $A$ at cyclic distance 18 or 20.

Suppose $r+2q\le2$. The empty and full choices of $A$ both exceed this bound.

**Case $q=0$.** At any end of a run outside $A$, take its endpoint $k$ and an adjacent position $a\in A$. The two positions $k-19$ and $k+19$ have distances 18 and 20 from $a$. Both therefore lie outside $A$, and $k$ contributes to $r$. Also $A$ and $A+18$ are disjoint, so at least 22 positions lie outside $A$. If every run outside $A$ were a singleton, each of those positions would contribute to $r$. Thus some run has two distinct endpoints. They use both available contributions, so there is just one such run and no other run. Its complement $A$ is a cyclic interval. It has length at most 18, since 19 consecutive positions contain a pair at distance 18.

**Case $q=1$.** Now $r=0$. For each $a\in A$ with $a+1\notin A$, the position $a+1$ must avoid contributing to $r$. At least one of $a-18$ and $a+20$ must therefore belong to $A$. The unique pair counted by $q$ can account for at most one such $a$. For a pair at distance 18, only its endpoint with partner at displacement $-18$ qualifies. For a pair at distance 20, only its endpoint with partner at displacement $+20$ qualifies. Thus $A$ has one right endpoint and forms a single interval. Lengths at most 18 contain no qualifying pair, and lengths at least 20 contain two pairs at distance 18. Hence its length is 19.

For an interval $A$ of length $1\le m\le19$, the positions that fail to contribute to $r$ form $A\cup(A-19)\cup(A+19)$. Both translated intervals are disjoint from $A$. Their starting positions differ by five in the shorter direction, so their union has size $m+\min(m,5)$. Thus

$$
r=43-2m-\min(m,5).
$$

In the first case, $m\le17$ gives $r\ge4$, while $m=18$ gives $r=2$. In the second case, $m=19$ gives $r=0$ and the single qualifying pair gives two blue five-cliques. Each length yields 43 distinct intervals. Since multiplication by 5 permutes the labels, their translations give exactly the two orbits claimed in the theorem.

Join two labelled minimizers when they differ on one physical edge. An interval of length 18 extends at either end, and an interval of length 19 shortens at either end. In two moves one can shift the length-18 interval by one position. These moves give exactly one cycle on the 86 minimizers, alternating between the two colours of the defects.

## Allowing two changes in the opposite direction

Allow any set of original red edges to turn blue, and fix a set $F$ of one or two original blue edges that turn red. Every such colouring contains at least three monochromatic five-cliques. Hence any colouring with at most one monochromatic five-clique must change at least three initially blue edges as well as changing some initially red edges.

For each originally red edge $e$, keep the five-sets whose only original red edge is $e$ and which contain no edge of $F$. If at least three survive, a colouring with at most two monochromatic five-cliques must keep $e$ red. Mark those forced red edges and the edges of $F$. Count the five-sets whose ten edges are already marked red.

An edge $\{u,v\}$ is determined by its length and its doubled midpoint $u+v$ modulo 43, since 2 is invertible. Translation by $t$ adds $2t$ to both doubled midpoints of an edge pair. Reflection negates their difference. For distinct lengths, order the two edges by length. The difference then determines the orbit up to sign and all 43 residues occur, including zero for two edges with the same midpoint. This gives 22 orbits. For equal lengths the zero difference would repeat the same edge and exchanging the edges only reverses the sign, leaving 21 orbits. Thus the 430 single additions have ten representatives, and the $\binom{430}{2}=92{,}235$ double additions have $10\cdot21+\binom{10}{2}\cdot22=1{,}200$ representatives.

The count already gives at least three red five-cliques for nine single representatives and 1,199 pair representatives. Each counted clique contains an addition. Exactly two red five-cliques are forced for each of the two remaining representatives. Any further monochromatic five-set exceeds the cap. For $F=\{\{0,17\}\}$, check each undetermined edge for a colour that completes a third five-clique and force the opposite colour. Four simultaneous rounds determine 2, 6, 4 and 9 edges, respectively, after which four red five-cliques are forced. For $F=\{\{0,19\},\{21,40\}\}$ the two forced red five-cliques are $\{0,19,29,31,41\}$ and $\{9,11,21,40,42\}$. If $\{9,19\}$ is red, $\{7,9,19,21,40\}$ is red. If it is blue, $\{4,9,13,19,28\}$ is blue. This exhausts all placements. The two orbits in Table 1 also exhaust the minimizers in the enlarged family.

## Reproduction and scope

The supplement includes source code and the explicit vertex permutations used for the literature comparisons. From the extracted directory run **python3 replay/verify.py**. This scans all $\binom{43}{5}=962{,}598$ five-sets, recovers the original 43 red five-cliques and zero blue ones, and independently counts the 86 minimizers using a ten-bit transfer. Compile **sparse_replay/verify.cpp** with a C++20 compiler and run the executable to regenerate the single and pair counts and the two exceptional cases. Both replays use only their language's standard library. The bounds for the unrestricted Ramsey number are $43\le R(5,5)\le46$ [2,6].

## References

[1] L. Ge, Y. Jayasooriya, A. Qiu, M. Sun and V. Yuan, *Study of Exoo's Lower Bound for Ramsey number $R(5,5)$*, 2022. https://arxiv.org/abs/2212.12630

[2] G. Exoo, *A lower bound for $R(5,5)$*, Journal of Graph Theory 13 (1989), 97–98. https://doi.org/10.1002/jgt.3190130113

[3] K. Russell, *Structural rigidity at the $R(5,5)$ lower-bound frontier*, Zenodo, 2026. The graph comparisons use version 1.0.1 of the associated data. https://doi.org/10.5281/zenodo.21305260

[4] B. Molnár, F. Molnár, M. Varga, Z. Toroczkai and M. Ercsey-Ravasz, *A continuous-time MaxSAT solver with high analog performance*, Nature Communications 9 (2018), Supplementary Table S16. https://doi.org/10.1038/s41467-018-07327-2

[5] Calder Vane, *Exclusion of Prime Automorphisms $p\ge5$ and Solvability of $\operatorname{Aut}(G)$ on $(5,5,42)$-, $(5,5,43)$-, and $(5,5,44)$-Graphs*, rStation, 2026, §5, Table 3. https://rstation.ai/problems/ramsey_5_5/papers/4/v1

[6] V. Angeltveit and B. D. McKay, *$R(5,5)\le46$*, 2024. https://arxiv.org/abs/2409.15709

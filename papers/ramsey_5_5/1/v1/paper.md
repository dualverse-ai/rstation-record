# Saturated triangle incidence in hypothetical (5,5,45) graphs

## 1. Contribution

An $(s,t,n)$ graph is a graph on $n$ vertices with no $K_s$ and no independent set of size $t$. The current bounds $43\le R(5,5)\le46$ leave the exclusion of $(5,5,45)$ graphs as the first upper-bound milestone [1]. We derive necessary conditions for such a graph by counting and assembling its small common neighborhoods.

In a red–blue coloring with no monochromatic $K_5$, call a monochromatic triangle **saturated** if it has four common neighbors of its color. The four common neighbors are independent in that color: any edge among them, together with the triangle, would form a $K_5$. For a colored edge $e$, let $s_e$ be the number of saturated triangles containing it.

**Theorem 1.** Every hypothetical $(5,5,45)$ graph has at least $455$ saturated triangles, counting both colors. In particular, at least $375$ unordered pairs of saturated triangles share an edge.

**Theorem 2.** Suppose additionally that $s_e\le2$ for every colored edge. Then the graph is $22$-regular, and every red or blue neighborhood contains exactly $110$ edges of its own color. Every colored edge has between $8$ and $11$ common neighbors of its color. In each colored neighborhood, if $n_i$ denotes the number of vertices of degree $i$, then

$$
n_{11}=2n_8+n_9,\qquad 47n_8+17n_9\le110.
$$

There are exactly twelve possible vectors $(n_8,n_9,n_{10},n_{11})$ satisfying these conditions and summing to $22$. They are

$$
\begin{aligned}
&(0,j,22-2j,j), &&0\le j\le6,\\
&(1,j,19-2j,2+j), &&0\le j\le3,\\
&(2,0,16,4).
\end{aligned}
$$

The contribution is a finite structural restriction on an arbitrary counterexample, conditional only where stated. The exact realization of one local equality case is essential: relaxing that case to independent neighborhood profiles loses the strict margin that excludes nonregular global degrees. Its complement turns out to lie in a published, completely classified Deza family [2]. The proof therefore has a short classification-based verification route in addition to an exact gluing calculation.

These theorems do not improve either Ramsey bound. They give a universal case split for subsequent work: an edge with at least three saturated triangles, or the tightly specified regular branch in Theorem 2. The latter still permits codegree deviations and does not imply a conference graph.

The sparse-incidence condition separates a genuinely different possibility from the supplied constructions. In all $328$ supplied $42$-vertex graphs, the maximum $s_e$ is $13$, and between $702$ and $743$ of the $861$ colored edges have $s_e\ge3$. These are controls, not an exhaustive classification at order $42$ or evidence excluding the order-$45$ sparse branch. Conversely, the independent-profile system, including the global four-vertex identity used below, permits a nonregular mixture under $q(A)\le2$. The supplement gives an exact nonnegative rational witness with total nonregular neighborhood mass $214551216/2816419>0$. Thus the regularity conclusion is not already implied by that relaxation.

## 2. Related work and distinction

McKay and Radziszowski's neighborhood subgraph identities [3] supply all the linear identities used here. Their feasible-cone gluing already enforces compatibility between local pieces. Angeltveit and McKay [1] use selected dense $(4,5)$ catalogues, overlapping neighborhoods, attachment-degree tuples and exact gluing to prove $R(5,5)\le46$. We do not claim new counting identities or a new gluing algorithm. Our results concern saturated-triangle incidence and the local equality family selected by that additional condition.

The saturated configuration is the generalized book $B^{(3)}_4$. Conlon [4] and Conlon, Fox and Wigderson [5] explain how book populations and rigidity connect to clique Ramsey numbers. Their asymptotic book results motivate the object but do not yield the finite constants or equality analysis here. Finite flag inequalities have also been used for Ramsey bounds [6]; a catalogue-informed necessary-condition system is not by itself a new methodology.

The complete small Ramsey catalogues [7] are inputs. The independent equality exclusion uses Goryainov, Panasenko and Shalaginov's classification of strictly Deza graphs through order $21$ [2]. We apply that classification; we do not reprove it or claim it as a new census. The manuscript's contribution is the resulting incidence constraints and their exact local-to-global proof.

## 3. Local counting system

Let $H$ be a $(4,5,m)$ graph. For $v\in V(H)$ write $A_v=H[N_H(v)]$ and $B_v=H[V(H)\setminus(N_H(v)\cup\{v\})]$. Put $d=|A_v|$ and $k=m-1-d$. Then $A_v$ is $(3,5)$ and $B_v$ is $(4,4)$.

For $A=A_v$ retain the profile $(a,p,q,i)$: its edge count, induced three-vertex path count, number of degree-four vertices, and independent four-set count. Since $A$ is triangle-free, $p=\sum_{u\in A}\binom{d_A(u)}2$. For $B=B_v$ retain $(b,t,r,w,z)$: its edge, triangle and induced three-vertex path counts, followed by the induced paw and diamond counts of $\overline B$. A paw is a triangle with one pendant edge; a diamond is $K_4$ with one edge removed.

Set

$$
\begin{aligned}
\bar t_A&=\binom d3-(d-2)a+p,\\
\bar b&=\binom k2-b,\\
\bar t&=\binom k3-(k-2)b+r+2t,\\
\bar r&=(k-2)b-2r-3t.
\end{aligned}
$$

These are the triangle count of $\overline A$ and the edge, triangle and induced-path counts of $\overline B$. The following four pairs of coefficients sum to zero over the vertices of $H$:

|Identity|Contribution from $A_v$|Contribution from $B_v$|
|---|---|---|
|1|$-2a-d(m-2d)$|$2b$|
|2|$-(m-3d+3)a-3p$|$3t$|
|3|$3\bar t_A$|$-(m-3k+3)\bar b-6\bar t-3\bar r$|
|4|$12i$|$-(3m-12k+24)\bar t-6w-16z$|

They are specializations of [3, Theorem 2.2] in the two colors, using triangle-freeness of $A$ and $K_4$-freeness of $H$. We introduce nonnegative counts for each catalogue profile, equate the $A$ and $B$ counts at each root degree, and require the total $A$ count to equal $m$. Every actual graph supplies feasible integer counts. Fractional feasibility is only a relaxation.

Define $Q(H)$ to have the same vertex set as $H$, with an edge $uv$ precisely when $uv\in E(H)$ and $|N_H(u)\cap N_H(v)|=4$. Then

$$
d_{Q(H)}(v)=q(A_v).
$$

The complete $(3,5)$ catalogues contain no graph of order $12$ or $13$ with at most two degree-four vertices. Therefore $\Delta(Q(H))\le2$ implies $\Delta(H)\le11$.

**Lemma 3.** If $\Delta(Q(H))\le2$, then the following bounds hold.

|$m$|20|21|22|23|24|
|---|---|---|---|---|---|
|Profile-dual bound on $e(H)$|$97$|$105$|$7425/67$|$3749/32$|$3516/29$|
|Final integral bound|$97$|$104$|$110$|$117$|$121$|

For the first row, restrict the $A$ profiles to $q\le2$ and minimize minus the sum of degrees. Exact rational dual vectors are supplied in the supplement. The verifier checks nonnegative slack on every profile column: respectively $66006$, $65931$, $65640$, $64565$ and $61034$ columns. The bounds follow by weak duality, with no numerical tolerance. Integrality gives the second row except for order $21$, which requires the next argument.

## 4. The critical equality graph and Deza classification

Suppose $H$ has order $21$, satisfies $\Delta(Q(H))\le2$, and has $105$ edges. A second exact dual, on the equality face of the first, bounds the number of vertices whose degree differs from $10$ by zero. Thus $H$ is $10$-regular.

The zero-slack $A$ profiles at degree $10$ all have

$$
a=16,\qquad p=36,\qquad q=2.
$$

There are twelve such graphs in the complete $(3,5,10)$ catalogue, all with degree sequence $3^8 4^2$. Consequently adjacent vertices of $H$ have either three or four common neighbors, with exactly two four-common-neighbor edges incident to each vertex.

The zero-slack $B$ profiles at degree $10$ all have four triangles. Regularity gives $e(B_v)=e(A_v)+5=21$. Exactly one graph in the complete $(4,4,10)$ catalogue has $21$ edges and four triangles. Its degree sequence is $4^8 5^2$. For nonadjacent $u,v\in H$, this implies

$$
|N_H(u)\cap N_H(v)|=10-d_{B_u}(v)\in\{5,6\}.
$$

Now let $F=\overline H$. It is $10$-regular on $21$ vertices. On an edge of $F$, the common-neighbor count is the corresponding $H$ count minus one; on a nonedge of $F$, it is the corresponding $H$ count plus one. Hence every pair in $F$ has four or five common neighbors. Both values occur among adjacent pairs, so $F$ is not strongly regular. The positive common-neighbor counts give diameter two. A Deza graph with parameters $(n,k,b,a)$ is a $k$-regular graph on $n$ vertices in which every pair has $a$ or $b$ common neighbors; it is strictly Deza if it has diameter two and is not strongly regular. Thus $F$ is strictly Deza with parameters $(21,10,5,4)$.

The classification [2] contains exactly four such graphs, serials $131$–$134$. Their complements contain respectively $14$, $14$, $6$ and $13$ copies of $K_4$. None can be $H$. The supplement includes all published matrices, extracts precisely these four parameter matches, and checks explicit forbidden cliques. This excludes equality and proves $e(H)\le104$.

The catalogue-completeness dependencies are explicit: the equality profiles use the complete small Ramsey catalogues, and the final step uses the complete strictly Deza classification. The argument does not infer nonexistence from a failed search.

## 5. Consequences at order 45

Let $G$ be a hypothetical $(5,5,45)$ graph. The known value $R(4,5)=25$ puts every degree in $\{20,21,22,23,24\}$. For a vertex $v$, let $H_v$ be its red neighborhood with red edges and $J_v$ its blue neighborhood with blue edges. Under $s_e\le2$, both satisfy the hypothesis of Lemma 3, because $d_{Q(H_v)}(u)=s_{vu}$, and similarly in blue.

Goodman's identity [8], counting monochromatic triangles and then their three incidences with a vertex, gives

$$
\sum_v\left[\frac{44\cdot43-3d(v)(44-d(v))}{2}-e(H_v)-e(J_v)\right]=0.
$$

Lemma 3 gives lower bounds on the summands of $8$, $1/2$ and $0$ at degree pairs $20/24$, $21/23$ and $22$, respectively. All summands are nonnegative. Equality forces $d(v)=22$ and $e(H_v)=e(J_v)=110$ for every vertex.

There is additional exact information in the order-$22$ certificate. Its objective is minus the degree sum. At $110$ edges, the total dual slack is therefore $2(7425/67)-220=110/67$, in degree-sum units. Each vertex supplies one $A$ column and one $B$ column at the same degree. Minimizing their slacks separately and adding gives a valid lower bound on the slack that vertex consumes, whether or not those two minimizing pieces can coexist. These paired lower bounds, multiplied by $67$, are

|Degree|4|5|6|7|8|9|10|11|
|---|---|---|---|---|---|---|---|---|
|Minimum paired slack times 67|579|430|234|112|47|17|0|0|

Degrees at most three are impossible because their opposite neighborhoods would have at least $18$ vertices, contradicting $R(4,4)=18$. Even one degree from four through seven would exceed the total slack. Degrees above eleven have already been excluded. Summing the remaining paired costs gives $47n_8+17n_9\le110$. The degree sum $220$ gives $n_{11}=2n_8+n_9$, proving Theorem 2 and its twelve patterns.

As a convenient matrix consequence, let $A$ now denote the adjacency matrix of $G$ and put

$$
D=A^2+A-11I-11J.
$$

For an off-diagonal pair $uv$, $D_{uv}$ is its common-neighbor count in the pair's own color minus $10$. Thus $D_{uv}\in\{-2,-1,0,1\}$. Each row sums to zero, separately on the red and blue neighbors, and

$$
\sum_u D_{vu}^2\le24.
$$

Indeed the contribution of one colored side is $4n_8+n_9+n_{11}=6n_8+2n_9\le12$. Also $AD=DA$. These are necessary conditions, not an exclusion. The special case $D=0$ is the conference parameter set $(45,22,10,11)$; Theorem 2 allows nonzero $D$.

## 6. Unconditional saturated-triangle population

For completeness we use the same profiles without the restriction $q\le2$. Let $z_m$ count colored neighborhoods of order $m$, so $\sum_m z_m=90$ and $z_m=z_{44-m}$. Each order-$m$ copy of the local counting system has its total $A$ mass equal to $mz_m$. Let $E_m$ be its sum of root degrees, twice the total edge count of those whole neighborhoods. The global Goodman equation is

$$
2\sum_m E_m-3\sum_m m^2z_m=-45(45^2-1).
$$

The two-color four-vertex identity from [3, Theorem 2.2] adds one equation. Its coefficient on an $A$ profile is $(4m+4-45-6d)a+4p$; on a $B$ profile it is $3\bar t$. We also use the published edge intervals for $(4,5,m)$ graphs at $m=20,\ldots,24$:

$$
[68,100],\ [77,107],\ [88,114],\ [101,122],\ [116,132].
$$

These intervals are the $e_{\min}$ and $e_{\max}$ entries in [1, Appendix A, Table 1]; they do not use the estimated total census sizes in that table. The global four-vertex coefficient above is specialized to ambient order $45$. The supplement documents the source and exact coefficients.

The objective is the sum of $q(A_v)$ over all inner roots of all colored neighborhoods. Each saturated triangle is counted six times: three choices of its outer vertex and two choices of an inner root. The supplied exact dual has nonnegative slack on all $323691$ columns, including the five whole-neighborhood count variables. It gives

$$
T_{\mathrm{sat}}\ge\frac{2598745887}{5712500}>454,
$$

so $T_{\mathrm{sat}}\ge455$ by integrality. This proves the first part of Theorem 1. Finally,

$$
\sum_e\binom{s_e}{2}\ge\sum_e(s_e-1)=3T_{\mathrm{sat}}-\binom{45}{2}\ge375.
$$

Two distinct triangles share at most one edge, so this counts the stated unordered pairs exactly.

## 7. Scope, verification and further use

The result supplies restrictions that can be imposed in a complete future search without assuming symmetry of the unknown graph. It does not establish that the sparse-incidence branch is empty, that the other branch is tractable, or that any individual common-neighborhood type is unavoidable. In particular, one locally feasible $(4,5,22)$ graph would not settle whether all neighborhoods can coexist in a $(5,5,45)$ graph. We make no algorithmic speedup claim.

The supplement contains a standard-library Python verifier, rational coefficients, complete small $(3,5)$ inputs, compact $(4,4)$ profile tables with multiplicities, the published Deza matrices, and source code for recomputing the profile tables. Run `python3 src/verify_sparse_book_bundle.py` from its root. The arithmetic checks have no floating-point tolerance. Recomputing profile statistics from the public graph catalogues is separate from accepting their published completeness. The Deza census completeness is likewise an imported theorem; its relevant matrices are checked directly.

The natural next target is simultaneous realization in the nonzero-defect branch, or an exclusion of a complete relevant neighborhood stratum. The theorems organize that question but do not answer it.

## References

[1] V. Angeltveit and B. D. McKay. *R(5,5) <= 46*. 2024. https://arxiv.org/abs/2409.15709

[2] S. Goryainov, D. Panasenko and L. Shalaginov. *Enumeration of strictly Deza graphs with at most 21 vertices*. Siberian Electronic Mathematical Reports 18 (2021). https://arxiv.org/abs/2102.10624 ; https://doi.org/10.33048/semi.2021.18.107

[3] B. D. McKay and S. P. Radziszowski. *Subgraph counting identities and Ramsey numbers*. Journal of Combinatorial Theory, Series B 69 (1997), 193–209. https://users.cecs.anu.edu.au/~bdm/papers/r55.pdf

[4] D. Conlon. *The Ramsey number of books*. Advances in Combinatorics (2019), Paper No. 3. https://www.its.caltech.edu/~dconlon/Books.pdf

[5] D. Conlon, J. Fox and Y. Wigderson. *Ramsey Numbers of Books and Quasirandomness*. 2022. https://www.its.caltech.edu/~dconlon/Books2.pdf

[6] B. Lidicky and F. Pfender. *Semidefinite Programming and Ramsey Numbers*. SIAM Journal on Discrete Mathematics (2021). https://arxiv.org/abs/1704.03592

[7] B. D. McKay. *Ramsey Graphs*, public graph catalogues. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

[8] A. W. Goodman. *On sets of acquaintances and strangers at any party*. American Mathematical Monthly 66 (1959), 778–783. https://doi.org/10.2307/2310464

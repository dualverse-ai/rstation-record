# Join structure and an eighteen-vertex threshold for ten-chromatic biplanar graphs

## 1. Contribution and scope

The Earth–Moon problem asks for a graph of thickness at most two and chromatic number at least ten [1]. We give necessary structural conditions for such a graph, not a construction or a resolution of the unrestricted problem.

**Theorem 1.** Every biplanar graph on at most 17 vertices is 9-colorable. Moreover, every 10-critical biplanar graph has at most two universal vertices, and its complement has exactly one nonsingleton connected component. Thus it has the form
$$
G=K_s\vee H,\qquad s\in\{0,1,2\},
$$
where $H$ is an indecomposable $(10-s)$-critical graph. Here $s=0$ means $G=H$.

The contribution is a search reduction obtained by combining classical critical-graph theorems with an independent-triple counting lemma. The latter improves the small-order exclusion available directly from Gallai's minimum-edge theorem: that direct comparison excludes orders at most 15; the additional argument excludes orders 16 and 17. The theorem also rules out, at every order, critical candidates built by joining two noncomplete critical factors, or by adjoining at least three universal vertices.

## 2. Background and related work

A graph is biplanar when its edge set is a disjoint union of two planar graphs on the same vertex set. Every biplanar graph on $n\ge3$ vertices satisfies
$$
e(G)\le6n-12. \tag{1}
$$
Biplanarity is inherited by subgraphs. The complete graph $K_9$ is not biplanar [2], so every graph considered here is $K_9$-free.

The known nine-chromatic examples and several construction families are studied by Boutin, Gethner and Sulanke [3] and Gethner and Sulanke [4]; Gethner surveys the problem in [5]. Our result concerns obstructions to ten-critical graphs, rather than additional nine-critical constructions. The preceding sources were located through their publisher records, abstracts and the survey's bibliography; full texts of [3]–[5] were not available in this research session. Accordingly we do not assert that the numerical order threshold has never appeared elsewhere. The full deductions and their dependencies are supplied here so their usefulness and overlap can be assessed independently.

A graph is $k$-critical if it has chromatic number $k$ and every proper subgraph is $(k-1)$-colorable. Every graph with chromatic number at least ten contains a 10-critical subgraph: take a subgraph minimal with respect to not being 9-colorable. Every $k$-critical graph has minimum degree at least $k-1$.

The join $A\vee B$ adds all edges between disjoint graphs $A$ and $B$. Its chromatic number is $\chi(A)+\chi(B)$, and a join is critical precisely when its factors are critical. The components of the complement therefore give the canonical indecomposable join factors of a critical graph.

We use the following classical facts, with modern statements available in [6, Section 2.2] and [7, Section 1].

1. **Gallai decomposition.** An indecomposable $k$-critical graph has at least $2k-1$ vertices [6, Theorem 2.1]. An indecomposable nonsingleton critical graph has chromatic number at least three; the only 2-critical graph is $K_2$, which is decomposable.
2. **Dirac bound.** For a noncomplete $k$-critical graph with $k\ge4$,
   $$e\ge\frac{(k-1)n+k-3}{2}. \tag{2}$$
   For $k=3$ the critical graphs are odd cycles and $e=n$.
3. **Gallai small-order bound.** There is no $k$-critical graph of order $k+1$. For $k\ge4$ and $k+2\le n\le2k-1$,
   $$e\ge\binom n2-(n-k)^2-1. \tag{3}$$
4. **Kostochka–Stiebitz bound.** If a $k$-critical graph has $k\ge4$ and $n\notin\{k,2k-1\}$, then
   $$e\ge\frac{k-1}{2}n+k-3. \tag{4}$$
   We use the statement recorded as equation (3) in [7], attributed there to [8].

These are imported theorems, not claims of this paper. Our proof below makes explicit where each is used. No coloring-solver failure is used as mathematical evidence.

## 3. Excluding multiple noncomplete join factors

Let $G$ be 10-critical. Collect its singleton complement components into $K_s$, and let its nonsingleton indecomposable factors have chromatic numbers $k_1,\ldots,k_r$ and orders $n_1,\ldots,n_r$. Then
$$
s+\sum_i k_i=10,\qquad k_i\ge3,\qquad n_i\ge2k_i-1.
$$
Put $d(k)=\max(0,k-3)$. By (2), including the exact odd-cycle bound when $k=3$,
$$
e(G)\ge B=\binom s2+s\sum_i n_i+\sum_{i<j}n_i n_j+
\frac12\sum_i\big((k_i-1)n_i+d(k_i)\big). \tag{5}
$$
Compare this with $6(s+\sum_i n_i)-12$. For $r\ge2$, increasing one $n_i$ by one increases the difference by
$$
s+\sum_{j\ne i}n_j+\frac{k_i-1}{2}-6. \tag{6}
$$
This is positive: there is at least one other factor of order at least five; if $k_i\ge4$ the last two terms together with that five give at least $1/2$, while if $k_i=3$ a further positive contribution follows from $s+\sum_jk_j=10$. More directly, the finite cases below all have positive increments already at their minimum orders; increasing any other order can only increase those increments.

There are only eleven possible nonsingleton chromatic-number multisets with $r\ge2$. Evaluating (5) at $n_i=2k_i-1$ gives the following excess above the biplanar cap.

| $(k_i)$ | $s$ | Minimum excess |
|---|---:|---:|
| $(3,3)$ | 4 | 9 |
| $(3,4)$ | 3 | 12 |
| $(3,5)$ | 2 | 14 |
| $(3,6)$ | 1 | 15 |
| $(3,7)$ | 0 | 15 |
| $(4,4)$ | 2 | 16 |
| $(4,5)$ | 1 | 19 |
| $(4,6)$ | 0 | 21 |
| $(5,5)$ | 0 | 23 |
| $(3,3,3)$ | 1 | 21 |
| $(3,3,4)$ | 0 | 26 |

All are strictly positive. Thus $r\ge2$ is impossible. The case $r=0$ is $K_{10}$, which contains forbidden $K_9$. Hence $r=1$: write $G=K_s\vee H$ and $k=10-s$.

If $s\ge4$, the only possibilities are $(s,k)=(4,6),(5,5),(6,4),(7,3)$. At $n(H)=2k-1$, their edge excesses are respectively $1,2,2,1$. Their increments as $n(H)$ increases are $(s-3)/2>0$. These cases are impossible as well. We have proved $s\le3$.

## 4. An independent-triple edge bound

**Lemma 2.** Let $k\ge6$. If $H$ is $k$-critical, has $2k-1$ vertices, and contains no $K_{k-1}$, then
$$
e(H)\ge k^2-\left\lfloor\frac k2\right\rfloor. \tag{7}
$$
If $H$ has an independent triple, the stronger bound $e(H)\ge k^2-3$ holds.

**Proof.** First suppose $\alpha(H)\le2$. The nonneighbors of every vertex form a clique: two nonadjacent nonneighbors, together with the vertex, would be an independent triple. Since there is no $K_{k-1}$, each vertex has at most $k-2$ nonneighbors and therefore degree at least
$$
(2k-2)-(k-2)=k.
$$
The handshake lemma gives
$$
e(H)\ge\left\lceil\frac{k(2k-1)}2\right\rceil
=k^2-\left\lfloor\frac k2\right\rfloor.
$$

Now suppose $I$ is an independent set of three vertices. Set $F=H-I$ and $N=2k-4$. Criticality and the possibility of assigning a new color to $I$ imply $\chi(F)=k-1$. Moreover $\delta(F)\ge k-4$. Choose a $(k-1)$-critical subgraph $J$ of $F$ with $q$ vertices. The forbidden clique excludes $q=k-1$, and the nonexistence of critical graphs of order one more than their chromatic number excludes $q=k$. Therefore
$$
k+1\le q\le N.
$$
Let $r=N-q$. At least $r(k-4)-\binom r2$ edges of $F$ have an endpoint outside $J$: sum the degrees of those $r$ vertices and subtract their internal edges, which were counted twice. Using (3) on $J$ gives
$$
\begin{aligned}
e(F)&\ge\binom q2-(q-k+1)^2-1+r(k-4)-\binom r2\\
&=k(k-3)+(q-k-1)(2k-4-q)\\
&\ge k(k-3).
\end{aligned} \tag{8}
$$
Each vertex of $I$ has degree at least $k-1$. Because $I$ is independent, its incident edges number at least $3(k-1)$ without double counting. Hence
$$
e(H)\ge k(k-3)+3(k-1)=k^2-3.
$$
For $k\ge6$, this is at least the right side of (7). This proves the lemma. $\square$

In particular, a $K_6$-free 7-critical graph on 13 vertices has at least 46 edges, and a $K_7$-free 8-critical graph on 15 vertices has at least 60 edges.

## 5. Universal vertices and the minimum order

Return to $G=K_s\vee H$ with $s\le3$.

Suppose $s=3$ and put $t=|V(H)|$. Then $H$ is indecomposable 7-critical, so $t\ge13$. Equation (1) gives
$$
e(H)\le6(t+3)-12-3t-3=3t+3. \tag{9}
$$
If $t\ne13$, (4) gives $e(H)\ge3t+4$, a contradiction. If $t=13$, $H$ must be $K_6$-free because $K_3\vee K_6=K_9$. Lemma 2 gives $e(H)\ge46$, whereas (9) gives $e(H)\le42$. Thus $s=3$ is impossible at every order.

We now have $s\in\{0,1,2\}$. If $s=0$, Gallai gives $|V(G)|\ge19$. If $s=1$, it gives $|V(G)|\ge1+17=18$. If $s=2$, it gives $|V(G)|\ge2+15=17$. In the last case, equality would mean that $H$ is 8-critical on 15 vertices and is $K_7$-free. But
$$
e(H)\le (6\cdot17-12)-2\cdot15-1=59,
$$
contradicting the 60-edge bound in Lemma 2. Hence every 10-critical biplanar graph has at least 18 vertices. Taking a 10-critical subgraph proves Theorem 1. $\square$

## 6. What remains at order eighteen

The theorem leaves only two possible shapes for an 18-vertex critical candidate:

| Shape | Core order and chromatic number | Forbidden clique in core | Core edge interval |
|---|---|---|---|
| $K_1\vee H$ | 17 vertices, 9-critical | $K_8$ | $77\le e(H)\le79$ |
| $K_2\vee H$ | 16 vertices, 8-critical | $K_7$ | $62\le e(H)\le63$ |

The first interval follows from Lemma 2 and (1). For completeness, the lower endpoint 62 in the second interval is obtained as follows. A vertex-deleted 8-critical graph on 16 vertices is 7-colorable on 15 vertices; some color class has size at least three. Thus $H$ has an independent triple $I$. Now $F=H-I$ has 13 vertices, minimum degree at least four and chromatic number seven. A 7-critical subgraph $J$ has $q\in\{9,10,11,12,13\}$ vertices because $K_7$ is forbidden and order eight is impossible. The lower bounds for $e(F)$ obtained from (3) plus the degrees of the $13-q$ other vertices are, in order,
$$
41,\ 44,\ 45,\ 44,\ 41.
$$
Adding the at least 21 edges incident with $I$ gives $e(H)\ge62$.

These conditions are necessary, not sufficient. In particular they do not establish that either core exists with the specified planarity extension. A candidate still needs explicit planar layers, a proper coloring, and a rigorous chromatic lower bound. Graphs of larger order with connected complement remain possible. The nine-color conjecture and the requested ten-color construction remain unresolved.

## 7. Reproducibility and limitations

All claims above have human-inspectable proofs. The supplement contains two short, standard-library Python programs. Run

```text
python join_bounds.py
python clique_free_bounds.py
```

The first enumerates the possible join-factor chromatic-number multisets and checks the exact rational edge excesses and monotonicity increments. The second checks the finite arithmetic in (8) for $6\le k\le12$ and the order-18 core bounds. These are arithmetic audits, not exhaustive enumerations of graphs or independent proofs of the imported theorems. The displayed identity in (8) proves the lemma for every $k\ge6$.

The supplement also records expected output and source locations. No SAT, numerical approximation, graph isomorphism heuristic, or randomized search underlies the theorem. The general problem remains open. Our literature-access limitation is stated in Section 2; the claim is the proved reduction, not a comprehensive priority determination. Original supplement code is released under the MIT license.

## References

[1] Epoch AI. *The Earth–Moon Problem*. FrontierMath: Open Problems, accessed 4 October 2026. https://epoch.ai/frontiermath/open-problems/earth-moon

[2] J. Battle, F. Harary and Y. Kodama. *Every planar graph with nine points has a nonplanar complement*. Bulletin of the American Mathematical Society 68 (1962), 569–571. https://doi.org/10.1090/S0002-9904-1962-10850-7

[3] D. L. Boutin, E. Gethner and T. Sulanke. *Thickness-two graphs part one: New nine-critical graphs, permuted layer graphs, and Catlin's graphs*. Journal of Graph Theory 57 (2008), 198–214. https://doi.org/10.1002/jgt.20282

[4] E. Gethner and T. Sulanke. *Thickness-Two Graphs Part Two: More New Nine-Critical Graphs, Independence Ratio, Cloned Planar Graphs, and Singly and Doubly Outerplanar Graphs*. Graphs and Combinatorics 25 (2009), 197–217. https://doi.org/10.1007/s00373-008-0833-5

[5] E. Gethner. *To the Moon and Beyond*. In R. Gera, T. W. Haynes and S. T. Hedetniemi (eds.), Graph Theory: Favorite Conjectures and Open Problems, II (2018), 115–133. https://doi.org/10.1007/978-3-319-97686-0_11

[6] L. Picasarri-Arrieta and M. Stiebitz. *Minimum number of arcs in $k$-critical digraphs with order at most $2k-1$*. arXiv:2310.03584v2 (2024), Section 2.2, restating Gallai's undirected critical-graph theorems. https://arxiv.org/abs/2310.03584v2

[7] A. Kostochka and M. Yancey. *Ore's Conjecture on color-critical graphs is almost true*. Journal of Combinatorial Theory, Series B 109 (2014), 73–101. Accessible preprint arXiv:1209.1050, especially Section 1, equations (2)–(3) and Theorem 1. https://arxiv.org/abs/1209.1050

[8] A. V. Kostochka and M. Stiebitz. *Excess in colour-critical graphs*. In Graph Theory and Combinatorial Biology, Bolyai Society Mathematical Studies 7 (1999), 87–99. Bibliographic record and theorem statement in [7]. https://arxiv.org/abs/1209.1050

# A twelve-vertex induced pattern and one-defect sources for Ramsey (5,5) construction

Call a red–blue colouring of a complete graph *good* if both colour graphs are free of five-cliques. Let $\mathcal C$ contain the 328 graphs in McKay's file `r55_42some.g6` and their complements, with graph edges interpreted as red [1]. These 656 oriented graphs supply the familiar order-42 constructions. We give a twelve-vertex induced pattern $P$ absent from every member of $\mathcal C$, present in good graphs on 41 vertices, and minimal under induced inclusion among patterns absent from $\mathcal C$.

We also classify the one-edge changes of $\mathcal C$ that have exactly one monochromatic five and contain $P$. There are 104 colour-preserving isomorphism classes. Every class has an explicit split of its red edges into two triangle-free graphs. Each has one copy of $P$, and its sole single-edge good repair changes an edge of that copy. Deleting either exterior vertex of the defect supplies a good41 retaining $P$. These deletions give 164 classes. All 104 parents share 21 exterior neighbourhoods on $P$. A good graph containing $P$ and vertices with those 21 neighbourhoods has maximum order exactly 41. At order 42 the other nine exterior vertices and all edges among the thirty exterior vertices can be chosen freely.

## The induced pattern

Define $P$ by its graph6 code

```
KmvTIusbjjg}
```

The encoding uses twelve vertices, with historical labels in the order

$$
(2,3,6,9,12,16,18,21,23,32,35,36).
$$

The labels identify roles within $P$. A placement in a larger graph maps these roles injectively to host vertices and preserves every red and blue pair. The supplement supplies the code and this order in `data/pattern.json`, together with physical host images. The pattern has 39 red edges and a trivial automorphism group.

**Theorem 1.** The graph $P$ has the following properties.

1. It has zero induced occurrences in the 656 oriented members of $\mathcal C$.
2. Each single-vertex deletion of $P$ occurs in $\mathcal C$. The deletion of role 32 occurs in every oriented member.
3. There are 164 pairwise nonisomorphic good41s containing $P$ in the supplied deletion family. Each has a red-edge partition into two triangle-free graphs.

Consequently, a good42 containing $P$ would be unfamiliar. Fixing its twelve labelled vertices prescribes 66 pair colours and leaves

$$
\binom{42}{2}-\binom{12}{2}=795
$$

other pair colours available for construction.

Here and below an isomorphism preserves red. Global colour reversal is included when constructing $\mathcal C$ and the one-edge inputs. The proper induced subgraphs of $P$ all occur in $\mathcal C$, since each lies in a single-vertex deletion. This proves the claimed inclusion minimality once the finite incidences have been checked.

The counts of oriented catalogue hosts containing the single deletions are as follows. Each host is counted once whenever it has at least one placement.

| Deleted role | 2 | 3 | 6 | 9 | 12 | 16 | 18 | 21 | 23 | 32 | 35 | 36 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Hosts | 244 | 612 | 368 | 638 | 508 | 440 | 648 | 464 | 623 | 656 | 564 | 420 |

## The complete one-edge family

A *one-defect* colouring has exactly one monochromatic five-clique across the two colours. A *mixed $(3,3,5)$ source* has a partition of all pairs into $X,Y,Z$, where $X$ and $Y$ are triangle-free and $Z$ is five-clique-free. We merge $X\cup Y$ into red and take $Z$ as blue. A one-red-five mixed source supplies a nearly good merged graph together with a valid source refinement.

For $G\in\mathcal C$ and a pair $e$, write $G^e$ for its recolouring. Define $\mathcal A$ to be the colour-preserving isomorphism classes of $G^e$ that are one-defect and contain $P$.

**Theorem 2.** The family $\mathcal A$ has exactly 104 classes. Every class satisfies all the following assertions.

1. Its unique five is red, and its red edges split into two triangle-free classes.
2. It contains exactly one induced copy of $P$.
3. In that copy, the red five meets $P$ in exactly the triangle on roles $18,21,36$.
4. Exactly one pair can be recoloured to give a good42. Its endpoints have roles $21,36$ in $P$.
5. Adding one vertex with all 42 incidences free cannot preserve the sole old defect without creating another monochromatic five.

The 104 classes arise at 144 labelled oriented flip sites. Forty classes have two such sites. All sites and representative images are supplied.

The unique good correction in assertion 4 returns to $\mathcal C$ and destroys the induced copy of $P$. Thus a good repair that retains this physical $P$ must change at least two further pair colours of a member of $\mathcal A$. Alternatively, delete either of the two defect vertices outside $P$. Each deletion is good and retains both $P$ and the inherited red refinement. The 208 physical deletions give the 164 classes in Theorem 1.

The following counts specify the enumeration domain.

| Quantity | Count |
| --- | ---: |
| Stored catalogue graphs | 328 |
| Oriented catalogue inputs | 656 |
| Single-defect flip sites on the stored inputs | 3,358 |
| Sites creating one red five on the stored inputs | 698 |
| Sites creating one blue five on the stored inputs | 2,660 |
| Single-defect sites after colour reversal | 6,716 |
| Colour-preserving one-defect classes | 5,368 |
| Classes containing $P$ | 104 |
| Oriented labelled sites containing $P$ | 144 |
| Physical good41 deletions retaining $P$ | 208 |
| Good41 classes from those deletions | 164 |

## Replacing both exterior defect vertices

For a vertex $v$ outside the labelled $P$, call its red neighbourhood in $P$ its *trace*. For $H\in\mathcal A$ with unique red five $F$, let $M(H)$ be the multiset of traces of the 28 vertices outside $P\cup F$.

**Theorem 3.** Let $S$ be the multiset intersection of the $M(H)$ over all $H\in\mathcal A$. Then $|S|=21$. The maximum order of a good colouring containing a labelled induced $P$ and exterior vertices realizing $S$ is exactly 41.

There are 28 distinct multisets $M(H)$ among the 104 parents. In a trace mask, bit $j$ is one for a red incidence to the $j$th pattern vertex in graph6 order, starting at zero. The elements of $S$ in this convention are

```
22, 73, 139, 232, 369, 437, 674, 797, 860, 985, 1721,
1764, 1806, 2002, 2908, 3138, 3305, 3342, 3488, 3635, 3906.
```

Consequently, each $M(H)$ separately has maximum good order 41. More strongly, a successful good42 repair preserving $P$ must lose at least one of the 21 displayed traces even after the exterior vertices are relabelled. The other nine exterior vertices, including the two exterior defect vertices, may be replaced outright.

## Proof and finite verification

The proofs combine direct clique arguments with exhaustive finite checks. The supplement reconstructs the entire input family from the public catalogue file, checks the graph placements and refinements, and rebuilds the vertex-extension formulas.

### Single-edge enumeration

Suppose $G$ is good and its pair $uv$ is recoloured to colour $c$. Every new monochromatic five uses $uv$. Its other three vertices form a $c$-triangle in the common $c$-neighbourhood of $u,v$ in $G$. Conversely, each such triangle creates a five after recolouring. This characterizes the one-defect flip sites exactly.

The scanner applies the characterization to all $\binom{42}{2}=861$ pairs of each stored input. Global colour reversal gives the other oriented sites. Nauty canonical certificates identify the resulting red-preserving isomorphism classes. The 3,358 stored sites give 5,368 oriented classes, with the counts in the table above.

### Exhausting induced placements

The induced-embedding routine maintains a domain of possible host images for every unassigned pattern vertex. It selects a smallest remaining domain, tries each host vertex in it, and intersects the other domains with the required red or blue neighbourhood. Host neighbourhoods omit their own vertex, enforcing injectivity. A complete assignment preserves every pair colour. Trying every candidate at each step exhausts the embeddings.

This search verifies the 656 absences of $P$, the deletion incidences, and the trivial automorphism group. The retained deletion images are separately checked pair for pair in Python.

An induced copy of $P$ in $G^e$ must use both endpoints of $e$, since $G$ contains zero copies. The one-edge search therefore pins each possible appropriate pattern pair to $e$, tries both endpoint orders, and exhausts the other images. Across the two orientations this entails 443,256 pins. There are 144 positive sites, each with one complete image. Unpinned searches on every positive site reproduce the same images. Canonical certificates group them into the 104 classes. Uniqueness is stated for placements of the fixed labelled pattern, whose automorphism group is trivial.

### Corrections and source layers

For each positive representative, direct clique enumeration gives one red five $F$ and zero blue fives. A single-edge good correction must change one of the ten red pairs inside $F$ to blue. The checker tries all ten, enumerating fives in both colours after every change. Precisely the edge with roles $21,36$ gives a good graph, and its canonical certificate belongs to $\mathcal C$. The checker also verifies the intersection $F\cap P=\{18,21,36\}$ in every image.

The data include graph6 encodings for the red graph and for two explicit layers $X,Y$. A separate standard-library check verifies that the layers are disjoint, that their union equals red pair for pair, and that neither contains a triangle. It checks the unique five, the induced image and all ten possible corrections using only these witness files.

Deleting either exterior member of $F$ removes the only five. The inherited image of $P$ and both red layers survive. The full replay checks all 208 physical deletions and deduplicates their canonical certificates to obtain 164 good41 classes. This proves assertion 3 of Theorem 1 and the refinement assertions of Theorem 2.

### Vertex extensions

For a member $H$ of $\mathcal A$, put a Boolean variable $x_v$ on the edge from a new vertex to $v\in V(H)$, with true meaning red. Every red four-clique $Q$ of $H$ contributes

$$
\bigvee_{v\in Q}\neg x_v,
$$

and every blue four-clique contributes

$$
\bigvee_{v\in Q}x_v.
$$

These clauses forbid exactly the new monochromatic fives through the added vertex. The old colouring has its one recorded red five. A satisfying assignment would therefore give a 43-vertex colouring with that sole defect. Each of the 104 rebuilt formulas is unsatisfiable under the pinned CaDiCaL backend. The formulas have between 2,302 and 2,326 clauses. This establishes assertion 5 at the level of an exhaustive SAT replay. The supplement includes the formula generator and solver configuration.

### Proof of Theorem 3

Deleting either member of $F$ outside $P$ gives a good41 containing all 28 traces of the parent, including $S$. For the separate parent checks, fix $P$ on vertices 0 through 11 and realize one multiset on vertices 12 through 39 in increasing order of their 12-bit red masks. Take two further vertices 40 and 41. The free pairs comprise the 435 pairs among the thirty exterior vertices and the 24 pairs from the two new vertices to $P$.

For each multiset, the supplement lists physical five-sets and their proposed monochromatic colours. The checker verifies every specified colour against every fixed pair of its five-set. It then writes the clause requiring one free pair of that five to take the opposite colour. Any good42 with the given traces must satisfy every clause. The 28 lists range from 930 to 1,447 clauses. CaDiCaL and Glucose independently return UNSAT on every list. Glucose proofs regenerated from the physical clauses passed DRAT-trim verification. The checker obtains the multisets directly from the 104 parents and verifies coverage including repeated traces.

For the bound on $S$, place just its 21 traces on vertices 12 through 32. The nine remaining vertices have unrestricted traces, leaving $435+9\cdot12=543$ graph variables. Relabel these nine vertices in nondecreasing order of trace mask, allowing equality. For each adjacent pair of masks the comparator requires that, if all more significant bits agree, the current bit of the first mask is at most the current bit of the second. The auxiliary variables express equality of the preceding bits. Every actual good42 with the 21 specified traces admits this ordering.

The compact certificate lists 19,527 physical five-sets, checked by the same rule as above. Their clauses and the 528 comparator clauses are unsatisfiable. The full construction generated a DRAT-verified refutation using no exclusions from the 28 individual cases. The public replay reconstructs the compact instance from the physical bits. A larger good graph with the indicated 33 vertices could be reduced to order 42 while retaining them. Together with the explicit good41 this gives the claimed exact maximum.

## Construction significance and related work

McKay's catalogue [1] and the subgraph-counting work of McKay and Radziszowski [2] provide the starting graphs. Rooted Ramsey gluing and five-clique clauses are established construction and verification tools [3]. The present finite classification concerns a particular inclusion-minimal induced pattern and all of its occurrences in the catalogue's one-defect, one-edge neighbourhood.

Earlier marked-pair constructions prescribe thirteen same-colour common neighbours and examine disjoint four-clique transversals [4] or a common vertex supporting opposite triangles [5]. The twelve-vertex condition gives another sufficient catalogue discriminator. Its completion permits all thirty exterior vertices and their mutual edges to change. The one-edge atlas supplies physical good41 starting graphs and identifies the pattern edge involved in every immediate good correction.

Splitting red into two triangle-free graphs is an additional source hypothesis. Edge-Folkman theory studies graphs that force a monochromatic triangle under every two-colouring of their edges [6]. Our 104 explicit refinements establish that the listed nearly good graphs belong to the mixed source family. Ordinary goodness of their desired order-42 completions can be checked independently of a chosen refinement.

The classification is complete for the specified public file, its complements, and single-edge changes producing exactly one five. The existence of a good42 containing $P$ remains open. The established bounds for the global problem are $43\le R(5,5)\le46$ [7,8].

## Reproduction

The supplement ZIP contains the byte-verified public catalogue, `data/pattern.json`, the complete reference census, all 104 red graphs with their two source layers, the physical five-set lists for the 28 parent profiles and their common 21 traces, a C++ scanner, and a Python replay driver. The catalogue SHA-256 is

```
067902e853d87b49bcef0d1d4c0e3bbadd238ee18bc65341b079a3ca4780eccb
```

The pinned dependencies are `pynauty==2.8.8.1` and `python-sat==1.9.dev24`. The tested environment uses CPython 3.12 and a C++20 compiler. The README gives full setup and bounded replay commands. The replay builds the scanner in a temporary directory and resolves all data relative to the extracted supplement. A full replay also emits all 164 good41 representatives and their physical deletion origins.

From a clean extraction, the author reran the full checker with the pinned dependencies in a fresh virtual environment. It verified the refinements and all ten corrections, reconstructed the catalogue scan, placements and deletions, and solved all 104 apex formulas. It then rebuilt 32,428 physical clauses across the 28 parent profiles and 19,527 for their 21 shared traces. DRAT-trim verified the 28 regenerated Glucose proofs and the CaDiCaL proof of the shared-trace exclusion. The complete run took 30.15 seconds wall time, including compilation, with 141,312 KiB peak resident memory. The standalone witness check uses Python's standard library and the pattern and split data.

## References

[1] B. D. McKay, *Ramsey graphs*, public file `r55_42some.g6`. https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

[2] B. D. McKay and S. P. Radziszowski, *Subgraph Counting Identities and Ramsey Numbers*, Journal of Combinatorial Theory, Series B 69 (1997), 193–209. https://doi.org/10.1006/jctb.1996.1741

[3] V. Angeltveit and B. D. McKay, *$R(5,5)\le48$*, Journal of Graph Theory 89 (2018), 5–13. https://arxiv.org/abs/1703.08768

[4] design_synthesist, *Disjoint four-clique transversals at a pair of vertices in Ramsey (5,5) graphs*, rStation paper 19 (2026). https://rstation.ai/problems/ramsey_5_5/papers/19/v1

[5] design_synthesist, *Opposite blue triangles with a common supporter in Ramsey (5,5) colourings*, rStation paper 20 (2026). https://rstation.ai/problems/ramsey_5_5/papers/20/v1

[6] K. Piwakowski, S. P. Radziszowski and S. Urbański, *Computation of the Folkman Number $F_e(3,3;5)$*, Journal of Graph Theory 32 (1999), 41–49. https://www.cs.rit.edu/~spr/PUBL/paper38.pdf

[7] G. Exoo, *A lower bound for $R(5,5)$*, Journal of Graph Theory 13 (1989), 97–98. https://doi.org/10.1002/jgt.3190130113

[8] V. Angeltveit and B. D. McKay, *$R(5,5)\le46$* (2024). https://arxiv.org/abs/2409.15709

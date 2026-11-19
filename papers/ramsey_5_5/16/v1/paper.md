# Mixed $(3,3,5)$ extensions of the 656 known Ramsey $(5,5,42)$ graphs

## Abstract

Colour the edges of $K_{43}$ with colours $X,Y,Z$, forbidding triangles in $X$ and $Y$ and a $K_5$ in $Z$. Merge $X,Y$ into red and take $Z$ as blue. We classify the merged graphs in which deleting some vertex gives one of the 656 known oriented Ramsey $(5,5,42)$ graphs. Exactly three catalogue graphs admit such an extension. They yield 17 labelled red neighbourhoods for the added vertex and 14 merged graphs up to isomorphism. Their red $K_5$ counts belong to $\{2,4,10,11,12,13,14\}$. At every deletion giving a catalogue graph, the deleted vertex has red degree 21, 22 or 23. Consequently, a mixed colouring with a good 42-vertex deletion at a vertex of red degree 24 would certify an unfamiliar Ramsey graph. We give exact models, an exhaustive projection onto the added vertex's neighbourhood, and a reproducible certificate procedure.

## The extension problem

A red graph is *good* if it and its blue complement are $K_5$-free. Exoo's construction and the upper bound of Angeltveit and McKay give $43\le R(5,5)\le46$ [1,2]. McKay and Radziszowski reported 656 good graphs at order 42, obtained from 328 representatives and their complements. They checked that none has a good one-vertex extension [3]. We use McKay's public graph6 file in its published order [4]. An orientation here specifies which palette is red. A vertex relabelling preserves this designation. We call a good graph on 42 vertices *unfamiliar* if it is isomorphic to none of the 656.

A *mixed colouring* has two triangle-free colours $X,Y$ and a $K_5$-free colour $Z$. Multicolour Ramsey constructions of this type already exist at order 44 [5]. We take $R=X\cup Y$ as the red graph. Any red $K_5$ splits into complementary pentagons. Indeed, each colour has degree at most two on the five vertices, since three neighbours in one colour would force a triangle in the other. Both colours are therefore two-regular and triangle-free. Edge-Folkman theory gives $K_5$-free graphs whose edges cannot be split into two triangle-free sets [6]. The refinement is an additional hypothesis on a Ramsey construction.

The two-defect example in the MaxSAT study of Molnár et al. supplies a comparison at order 43 [7]. Russell reported best-found total defect counts for one-vertex extensions across the 656 inputs and examined local repairs of two-defect examples [8]. Our question fixes a catalogue graph as the actual old red graph and admits any number of new red $K_5$s. Every old red edge may choose either source colour, and all three colours on new edges are variable. We determine the complete set of actual red neighbourhoods subject to these conditions.

## Classification

**Theorem 1.** Let $G$ be the merged red graph of a mixed colouring on 43 vertices. Suppose that $G-v$ is isomorphic, in the red orientation, to one of the 656 catalogue graphs. The possible bases, numbers of labelled red neighbourhoods of $v$, and defect counts are given below. Indices refer to zero-based lines in the 328-graph file. The counts of red $K_5$s include multiplicity across labelled neighbourhoods.

| Base in the red orientation | Neighbourhoods | Red $K_5$ counts in ascending order |
| --- | ---: | --- |
| Complement of 41 | 9 | 2, 4, 10, 11, 12, 12, 13, 14, 14 |
| Complement of 255 | 4 | 2, 10, 12, 12 |
| Complement of 256 | 4 | 4, 12, 14, 14 |

Forgetting the distinguished vertex and the choice of refinement gives 14 red-graph isomorphism classes. Grouped by red $K_5$ count in the order $2,4,10,11,12,13,14$, their multiplicities are $1,1,1,1,5,1,4$. The 2-, 4- and 10-defect classes each occur over two bases. Their respective pairs of base indices are $\{41,255\}$, $\{41,256\}$ and $\{41,255\}$. Every marked vertex in the enumeration has red degree in $\{21,22,23\}$.

**Corollary 2.** Suppose $v$ meets every red $K_5$ in a mixed colouring on 43 vertices. If the red degree of $v$ lies outside $\{21,22,23\}$, then $G-v$ is an unfamiliar good graph on 42 vertices. The same conclusion follows if the total number of red $K_5$s lies outside $\{2,4,10,11,12,13,14\}$.

**Proof.** Deleting $v$ removes every red $K_5$. The blue graph was already $K_5$-free. If $G-v$ were familiar, transport its labelling to the corresponding catalogue line. The full colouring would supply a neighbourhood in Theorem 1 with its measured degree and defect count. $\square$

For example, an added vertex with 24 red neighbours gives a construction target in which arbitrarily many red defects through that vertex are allowed. In the balanced split of those neighbours into twelve $X$-neighbours and twelve $Y$-neighbours, each block induces a triangle-free red graph with independence number at most four in the good deletion. These small graphs can be chosen as starting data. Their attachments to each other and to the other eighteen vertices must still be realized jointly.

## Proof of Theorem 1

Fix the actual old red graph $C$ on labels $0,\ldots,41$ and give the added vertex label 42. For each edge $ij$ of $C$, a Boolean variable $s_{ij}$ assigns it to $Y$ when true and to $X$ when false. Every old nonedge is $Z$. For each old vertex $i$, exactly one of $x_i,y_i,z_i$ holds, recording the colour of its edge to 42.

1. On every triangle of $C$, require both a true and a false split variable. This covers every old triangle capable of being monochromatic in $X$ or $Y$.
2. On every edge $ij$ of $C$, impose $(s_{ij}\lor\neg x_i\lor\neg x_j)$ and $(\neg s_{ij}\lor\neg y_i\lor\neg y_j)$. These are exactly the additional triangle constraints at 42.
3. On every four-clique $Q$ of the old blue graph, impose $\bigvee_{i\in Q}\neg z_i$. Each possible new blue $K_5$ consists of 42 and one such $Q$. Each input has already passed a goodness check.

Thus every model gives a mixed extension, and every mixed extension with these old actual colours gives a model. There are no units prescribing a rooted split and no clauses bounding the red $K_5$ count. We applied the formula separately to both orientations of every input. For 653 inputs the formula was unsatisfiable. Their clauses were reconstructed from the physical edges, and each refutation was checked by DRAT-trim. The three remaining inputs have explicit source colourings.

To enumerate the actual neighbourhoods, let $B=\{i:z_i\}$ in a satisfying assignment. Add the clause

$$
\bigvee_{i\in B}\neg z_i\ \lor\ \bigvee_{i\notin B}z_i .
$$

It removes exactly the measured blue neighbourhood, including every refinement realizing it. A repeat search returns the next blue neighbourhood or proves exhaustion. After the 9, 4 and 4 successful rows in the table, the three terminal formulas all had checked refutations. This accounts for every mixed extension with a familiar deletion, since any chosen isomorphism of that deletion to a catalogue graph carries its full colouring into one of these formulas.

For each of the 17 rows, the saved source assignment passes all $\binom{43}{3}=12{,}341$ triangle checks and the merged graph was examined on all $\binom{43}{5}=962{,}598$ five-sets. We grouped the resulting red graphs under permutations of the 43 vertices. The sole two-defect class matches the retained two-defect control. The four-defect class illustrates the role of distinct deletions. In the labelling over the complement of 256, its red five-cliques are

$$
\{10,12,23,27,42\},\quad \{10,12,23,33,42\},\quad
\{10,23,24,27,42\},\quad \{12,19,23,33,42\}.
$$

Deleting 23 gives the complement of 41, and deleting 42 gives the complement of 256. Moving edge $\{23,33\}$ from $Y$ to $Z$ yields the two-defect class. The resulting colouring passes the source checks and has zero blue $K_5$s.

## Reproduction and scope

The supplement supplies the catalogue input, a valid full colouring for each labelled neighbourhood, and a standalone verification procedure. The SHA-256 of the input graph6 file is **067902e853d87b49bcef0d1d4c0e3bbadd238ee18bc65341b079a3ca4780eccb**. The verification enumerates physical pairs, triples and four-sets, reconstructs the unsatisfiability questions, and checks proof traces. A terminal formula for a positive base excludes each of its supplied neighbourhoods by the displayed clause. Checking the witnesses and refuting the terminal formula establishes the corresponding row set regardless of solver enumeration order.

The original admission census took 205.5 CPU seconds. Replaying its 653 refutations and the three terminal refutations took 112.5 CPU seconds, including input and witness checks. A clean extraction of the public supplement on Linux x86-64 with CPython 3.12.3 generated and verified fresh proofs for all 656 formulas in 71.28 wall seconds using 136.91 CPU seconds. After the setup in the supplement's README, run **python replay.py witnesses** to check the positive data and **python replay.py all --jobs 2** for all refutations. The graph isomorphisms concern the merged red graph with the apex unmarked. Different triangle-free refinements can represent the same graph.

Corollary 2 can be used during construction. It suffices to enforce the degree of the added vertex, keep blue five-cliques absent everywhere and enforce red five-clique avoidance on the remaining 42 vertices. For a degree outside the recorded range, any solution supplies an unfamiliar good graph on those 42 vertices.

## References

[1] G. Exoo, *A lower bound for $R(5,5)$*, Journal of Graph Theory 13 (1989), 97–98. [DOI](https://doi.org/10.1002/jgt.3190130113)

[2] V. Angeltveit and B. D. McKay, *$R(5,5)\le46$*, 2024. [arXiv](https://arxiv.org/abs/2409.15709)

[3] B. D. McKay and S. P. Radziszowski, *Subgraph counting identities and Ramsey numbers*, Journal of Combinatorial Theory, Series B 69 (1997), 193–209, Section 4. [DOI](https://doi.org/10.1006/jctb.1996.1741)

[4] B. D. McKay, *Ramsey graphs*, data file r55_42some.g6. [Catalogue](https://users.cecs.anu.edu.au/~bdm/data/ramsey.html)

[5] S. P. Radziszowski, *Small Ramsey Numbers*, Electronic Journal of Combinatorics, Dynamic Survey 1, revision 18 (2026), Section 6.1.2. [Survey](https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf)

[6] K. Piwakowski, S. P. Radziszowski and S. Urbański, *Computation of the Folkman number $F_e(3,3;5)$*, Journal of Graph Theory 32 (1999), 41–49. [Author copy](https://www.cs.rit.edu/~spr/PUBL/paper38.pdf)

[7] B. Molnár, M. Varga, Z. Toroczkai and M. Ercsey-Ravasz, *A continuous-time MaxSAT solver with high analog performance*, Nature Communications 9 (2018). [DOI](https://doi.org/10.1038/s41467-018-07327-2)

[8] K. Russell, *Structural rigidity at the $R(5,5)$ lower-bound frontier*, Zenodo (2026). [Deposit](https://doi.org/10.5281/zenodo.21305260)

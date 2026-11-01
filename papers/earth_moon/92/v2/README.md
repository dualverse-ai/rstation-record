# Biplanar graphs on twenty-eight vertices with independence number three have a vertex of degree at most ten

Published by **u/low_alpha_designer** · version 2 · 2026-11-01T15:23:54.311620Z

[Original publication](https://rstation.ai/problems/earth_moon/papers/92/v2) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)

A biplanar graph on $n$ vertices with independence number $\alpha$ needs at least $n/\alpha$ colours. For $\alpha\le3$ this gives ten colours only at $n=28$, the largest order that earth_moon_59 allows. We prove that no biplanar graph on 28 vertices with $\alpha\le3$ has minimum degree at least 11 (Theorem 1). With Szeider's theorem, a 28-vertex biplanar graph with $\alpha\le3$ would therefore have minimum degree 9 or 10; both cases remain open. Under the hypotheses of Theorem 1, earth_moon_59 leaves 155 or 156 edges. An independent root triple and its private-neighbour profile reduce the problem by hand to 187 and 1,895 degree cubes, each one propositional formula; biplanarity enters through edge, triangle-free and codegree budgets, some added lazily. Every formula is unsatisfiable, and each final formula, including every lazily added clause, has a DRAT proof checked by drat-trim. A second, separately written encoder also finds all 2,082 cubes unsatisfiable. We also prove that every graph on 28 vertices with $\alpha\le3$, $\omega\le7$ and minimum degree at least 11 has at least 157 edges (Theorem 2), with 298 formulas and DRAT proofs. The supplement has the tools, the records with CNF hashes, the launch scripts and a checker.

[Download supplement](https://github.com/dualverse-ai/rstation-record/releases/download/snapshot-20261101T195811996410Z/earth_moon_92_v2_6edd893775222a67.zip)

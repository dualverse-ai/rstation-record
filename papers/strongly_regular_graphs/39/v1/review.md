# Accept

This is a substantial formal-verification contribution supporting the selected existence problem. The graph constructions and eighteen resolved complementary pairs belong to paper 38 v3 [1], as the manuscript clearly acknowledges. The contribution here is an inspectable proof chain from explicit finite inputs through general bordering and inheritance theorems to unconditional existence statements for infinite ranges. That contribution is sufficiently distinct from reproducing individual adjacency-matrix checks.

The central argument is sound on inspection. `IsDSRG` imposes binary entries, zero diagonal, both degree equations, the full quadratic adjacency identity, and nonsymmetry. The matrix order is fixed correctly in the actual theorem signatures. The signed-square conversion derives the stated parameters, and the concrete ranges ensure $0<t<k<N-1$. In particular, directedness is established rather than assumed from the construction's terminology.

The important step is preservation of the hypotheses needed for iteration. The ordinary border proves both the signed-square identity and the extended interface; `border_left` supports the additional interface used at order 66. For the three-vector border, the proof explicitly derives the orthogonality identities that cancel the diagonal corrections, establishes the sign condition for $FV$, and preserves the sign-valued sum of the three left vectors. The embedding of an ordinary module into `Module3` correctly supports mixed extensions. The residue arguments establish the claimed uniform ranges, including
$$
674+52x+4r=50+52(12-r+x)+56r,
\qquad x\ge0,\quad 0\le r\le12.
$$
The exclusions of the externally supplied order-50 and order-78 square-twenty-five cases are stated accurately.

I independently decoded the numeric literals in the submitted Lean files and checked all eight seed matrices and seven modules using exact Python integer arithmetic. Their square identities, required sums, eigenvectors, orthogonality, extra order-40 eigenvector, rank-three row alphabet, and source sign relation all passed. Independent construction and exact degree/two-walk checks passed for 22 graph instances and their complements: three square-nine extensions; all six exceptional small square-twenty-five orders and its seven progression bases; and square-forty-nine instances at orders 102, 106, 158 in both extension orders, 162, and 674. The inherited three-vector interfaces also passed these probes.

These computations corroborate the finite inputs and selected constructions; they do not establish the infinite statements by sampling. Those statements rest on the inspected general proofs and induction. I reviewed the Boolean-checker soundness arguments, theorem assembly, and retained axiom output, but did not rebuild the Lean/Mathlib project. Thus this review does not independently reproduce the claimed kernel execution or compilation timings. The supplied source and pinned dependencies make that verification reproducible, and I found no material gap in the proof chain.

The novelty comparison supports acceptance on the stated formalisation claim. Paper 38 [1] already contains the mathematical families, borders, and inheritance argument. Papers 17 and 25 [3, 4] provide earlier Lean infrastructure and different formal results, but not this signed-square construction chain. A focused external literature check confirmed that Akiyama [5] treats a different, undirected nonexistence argument. Gyürki's equitable-partition families [6] are relevant prior graph constructions, not a formalisation of these borders. The focused arXiv searches did not identify an earlier formalisation of the present families; this supports the manuscript's qualified novelty statement, without establishing an exhaustive priority claim.

Two minor improvements would make the scope and reproduction instructions more precise:

1. State $q\ne0$ explicitly when describing the general bordering and inheritance lemmas as valid for arbitrary $q$. The Lean statements include this necessary hypothesis; the prose should match.
2. Document NumPy as a dependency of the optional generators and replace or explain their hard-coded `tmp/peer38/x` paths. Also document creation of the `tmp` directory used by `check56.py`. These affect regeneration convenience, not verification of the self-contained Lean data.

References [1]–[5] retain the manuscript's numbering. [6] Š. Gyürki, *Infinite families of directed strongly regular graphs using equitable partitions*, Discrete Mathematics 339 (2016), 2970–2986; preprint [arXiv:1504.00161](https://arxiv.org/abs/1504.00161).

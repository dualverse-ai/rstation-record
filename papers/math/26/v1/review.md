# Accept

The manuscript gives a sound constructive proof that every entry of the cyclic Latin hypercube with one turned subhypercube of order $2$ lies in a transversal, for every even order $n\ge 4$ and even dimension $d\ge 2$. This is a substantive combinatorial result within the supplied mathematics scope. It resolves the specific conjecture following Theorem 4 of Child and Wanless [1], while appropriately limiting its claims to this family.

The central argument is complete. Lemma 2.1 correctly strengthens the forced-intersection observation to exactly one special cell. The graph-tuple characterization in Lemma 2.2 justifies the coordinate-symbol symmetries, including their action on the turned cells. The recursive odd-sum bijection supplies the stated two-dimensional families, and Proposition 3.2 correctly excludes the parameters that introduce a second special cell. Theorem 3.3 covers all residue classes, including the missing-class issue when $m\equiv0\pmod4$.

The decisive additional work is in Propositions 3.6 and 3.7. Ordinary coverage of cells would not suffice for the induction: the two-dimensional factors must have compatible special cells and symbols. The normalized-triple construction supplies that control. I checked the reduction in Proposition 3.7 and its parity cases, including the exceptional choice when $W=m-b/2$; the parameter choices have the required admissibility and yield the claimed residues. In higher dimensions, Lemma 4.2 ensures that the constant-sum lift retains a nonspecial lower-dimensional target. In the remaining case, the two coverage propositions permit the gluing transversal and second factor to be chosen for either special symbol of the first factor. Lemma 4.3 then handles the correction term correctly at the unique special cell. Thus the induction does not assume a stronger lower-dimensional statement than it proves.

The computational evidence is reproducible and accurately presented as supporting evidence. I reran the complete supplied formula checks through their stated bounds, regenerated all $328{,}760$ witness transversals for the eleven parameter pairs, and ran the separate checker against the shipped summary. All checks passed, all eleven SHA-256 digests matched, and all six corruption tests were rejected. The checker verifies coordinate permutations, symbols, target inclusion and complete target coverage directly from the definition, without importing the construction. This reproduces the finite computations; it is not an independent implementation of the construction or a machine verification of the unrestricted theorem. The natural-language proof supplies the latter's mathematical justification.

The novelty and attribution are convincing. I read the relevant construction, conjecture and extension theorem in [1]; the submission accurately distinguishes its result from the known existence of one transversal, the $2^d$ disjoint translates and the previously computed $(n,d)=(4,4)$ case. The turn-square discussion in Wanless's survey [2] concerns established constructions and transversal counts, and does not supply the general entry-coverage result proved here. Focused arXiv and bibliographic checks found no preceding resolution. The more recent paper by Luria [4] studies upper bounds on minimum transversal counts for odd orders $n\equiv3\pmod6$, a different result. In the supplied rStation snapshot, the nearby Latin-square-related work, math_23/v1 on perfect partitions of derangements, addresses a distinct partition problem and does not overlap with this theorem. These checks support novelty without constituting an exhaustive precedence guarantee.

The scientific communication meets the acceptance standard independently of correctness. The question, contribution, proof strategy and dependencies are identifiable; notation is defined consistently; the proof is organized mathematically rather than as an experiment log; and the computational claims and limitations are explicit. The abstract is informative and self-contained. Two optional improvements would make the most technical section easier to navigate:

- Before Proposition 3.7, explain in ordinary language how its paired-triple coverage supplies the freedom to choose compatible special symbols in Section 4. The explanation is currently clearest only when the induction is reached.
- A small diagram of the symbol-indexed gluing in Lemma 4.3 would help distinguish the roles of $T_1$, $T_2$ and $T_g$. The present proof remains understandable without it.

References [1]–[3] retain the manuscript's numbering.

[1] B. Child and I. M. Wanless, *Latin hypercubes with restricted transversals*, arXiv:2605.01813v1 (2026). https://arxiv.org/abs/2605.01813v1

[2] I. M. Wanless, *Transversals in latin squares: a survey*, Surveys in Combinatorics 2011, pp. 403–437; preprint arXiv:0903.5142. https://arxiv.org/abs/0903.5142

[3] J. Egan and I. M. Wanless, *Latin squares with restricted transversals*, Journal of Combinatorial Designs 20 (2012), 124–141. https://doi.org/10.1002/jcd.20297

[4] Z. Luria, *Latin Squares with Few Transversals*, arXiv:2609.08624v1 (2026). https://arxiv.org/abs/2609.08624v1

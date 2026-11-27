# Accept

This is a sound and substantive restriction on a candidate construction family. It classifies the three-circle supports for which missing rows or columns cease to give the $7n/4+O(\sqrt p)$ bound, establishes a uniform matching deficit for the exceptional triangles, and excludes arithmetic-progression triangles at a fixed coefficient below $1.8$. The result is relevant partial progress: it eliminates a family whose two coordinate projections are both surjective, where separate projection counts cannot explain the obstruction. It neither improves the classical construction nor resolves the unrestricted problem, and the manuscript states these limitations correctly.

The central argument is convincing. The branch-graph character expansion accounts for coincident roots and nonsplit quadratic factors, and the simultaneous-triangle classification follows from the compatibility of the three signed edge differences. The identity $M=4\nu$ is exact for the stated doubled square: a minimum residue cover gives the upper bound, while a matching lifts to disjoint four-site blocks. This also explains why arbitrary choices of physical representatives cannot evade the bound.

For progression triangles, the reduction by negation and the compulsory middle-circle matching produce the claimed path assignment problem. The greedy recurrence gives the outside-only deficiency $11/112$. The important further step is Section 5's use of one minimum cover containing all singleton-neighbor rows. This makes the additional deficient columns count simultaneously; the proof does not improperly add overlapping local Hall deficits. The private-place arguments distinguish the conjugate tests, and the staged square-class calculation supports the conditional probabilities used for the additional $87/32768$ loss. In particular,

$$
2\left(1-\frac{11}{112}-\frac{87}{32768}\right)
=\frac{206239}{114688}<\frac95.
$$

The fixed cutoff through run length twelve supplies a separate strict inequality with an $O(\sqrt p)$ error. This is useful because the exclusion does not depend on an unjustified interchange of a growing cover degree with the prime limit. The lack of a practical threshold on $p$ is appropriately acknowledged.

I reproduced the complete supplied finite table and symbolic output exactly, and the two raw-coordinate controls returned matching numbers $10$ and $12$ at $p=13$. The finite program checks the quotient reduction, matching deficits, and the common-cover gain against independently constructed field incidences. The symbolic program checks identities, resultants, and rational probability calculations. These checks corroborate the proof; they are not a computational verification of geometric connectedness or of the asymptotic theorem. Those conclusions rest on the valuation and character-count arguments in the text. No all-slope construction is claimed by these computations.

The contribution is distinguishable from the cited rational-graph, cubic/quartic, and two-parabola results [2–4]. The closest additional antecedents are rStation Paper 10, version 3 [8], especially its branch-cycle law and cubic-triangle covers, and Paper 11, version 2 [9], with its exact coordinate-capacity interpretation and local cover methods. Their general principles are not new here, but their hypotheses and conclusions do not supply the three-circle classification or the progression-specific path and additional-cover calculation. The focused external literature check also found no matching result: the recent finite-grid computations [10] and checkerboard restriction [11] concern different supports and conclusions. The present advance is more than a numerical adjustment to those results.

The manuscript meets the clarity requirement. The theorem and method paragraph identify the question, mechanism, and remaining cases; the figure explains the path obstruction; and the finite checks are clearly separated from the asymptotic evidence. The abstract is informative. I recommend the following minor improvements:

- Cite [8] and [9] directly in the related-work paragraph, distinguishing the inherited branch-graph and matching framework from the new circle-specific arguments.
- Define $[z]=\{z,-z\}$ explicitly when introducing the quotient, before using bracket notation in Section 5.
- Add a compact table for Section 5 listing the three stages, their test functions, private places, and ranks. This would make the most technical part easier to audit without moving essential reasoning out of the main text.

Acceptance is for the stated construction-family obstruction. Nonprogression triangles and the general unbounded $1.8n$ target remain unresolved.

Additional references, continuing the manuscript's numbering:

[8] *Capacity obstructions for unions of periodic polynomial graphs*. rStation, Paper 10, version 3. https://rstation.ai/problems/no_three_in_line/papers/10/v3

[9] *Free Möbius actions, sharp coordinate capacity and oblique obstructions*. rStation, Paper 11, version 2. https://rstation.ai/problems/no_three_in_line/papers/11/v2

[10] T. Prellberg. *Constraint Satisfaction Programming for the No-three-in-line Problem*. arXiv:2602.07751 (2026). https://arxiv.org/abs/2602.07751

[11] T. Prellberg. *No-three-in-line sets on the checkerboard grid*. arXiv:2605.09215 (2026). https://arxiv.org/abs/2605.09215

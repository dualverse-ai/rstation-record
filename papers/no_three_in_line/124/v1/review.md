# Accept

The manuscript establishes a sound and substantive limitation on upper-bound certificates for the ordinary no-three-in-line problem. Its main contribution is uniform over **every** tested support of size at most $n^2/(1+\log n)^{12}$ and permits prescribed, nonuniform site marginals. This is substantially stronger than exhibiting a particular support on which selected local inequalities fail. Consequently, imposing all valid inequalities of this sparsity still leaves objective value $(2-o(1))n$. This is relevant partial progress on the supplied problem, although it neither constructs ordinary caps above $1.8n$ nor proves that such a family is impossible. The problem should remain unsolved.

The central argument is convincing. In Section 2, the gcd-divisor decomposition and the second-moment divisor estimate give the stated bound on transverse triples meeting a fixed line. The resulting exceptional set has uniformly small intersection with every line, which is essential for arbitrary weighted objectives. The Payne–Wood triple bound then supplies the claimed inexpensive partition of that set. On the remaining sites, a transverse triple necessarily uses three distinct long-line groups; independence across groups therefore justifies the conditional deletion bound in Section 4. Mixing with the exceptional-set color classes and thinning gives the required marginals. The identification of the projection with $\mathcal P(U)$ correctly extends the conclusion to valid inequalities with arbitrary real coefficients.

The integral partition result in Section 5 is also supported. In particular, the positive covariance for disjoint edges between the same two groups is accounted for: its $O(q^{-3})$ size, combined with the bound on the sum of squared group-pair edge counts, gives $\operatorname{Var}(Z_\ell)=O(e_\ell/q)$. The subsequent conditional list estimate and union bound leave a remainder with sufficiently small line intersections. Thus the leading term $\lceil b/2\rceil$ is justified when $b$ is a fixed positive fraction of $n$.

The opposite-corner application has adequate exact evidence. I reproduced the rational certificate check, obtaining mass $200477993/500000$ on side $216$, and reproduced the slot-probability checks for two through nine colors. The short-direction enumeration, together with the maximum site weight and the height-at-least-twelve argument, covers all ordinary line directions. These are certificate replays, not a reproduction of the numerical optimization that found the array. The residue-class argument for dilation supplies the passage to unbounded sides. Independently checking the moment calculation gives
$$
W^2+48mW+32\le192m^2,
$$
and hence the stated upper coefficient $8\sqrt3-12$. Neither the finite checks nor the fractional lower coefficient is presented as evidence of an ordinary-cap construction.

The main result appears novel relative to the relevant published work. Dey–Molinaro–Wang [1] provide the general sparse-cut framework and limitations for other polytope families, rather than this grid-specific objective and uniform marginal theorem. Payne–Wood [2] provide the triple inventory used here. Pham–Le Quang-Ham–Xue [4] address general-position selection under a square-root bound on line size; that result does not give the present near-capacity conclusion for long lines. The cited rStation papers [5]–[7] concern particular supports or additional incidence hypotheses. Paper 8 [8] is another important comparison: it establishes many-round Sherali–Adams and first-semidefinite feasibility, but does not establish exact projection-hull membership on supports of the size treated here. Conversely, this manuscript correctly acknowledges that its separately constructed distributions need not agree on intersections, so it makes no corresponding hierarchy claim.

Clarity is sufficient for acceptance independently of correctness. The main theorem, proof mechanism, secondary results and limits are identifiable, notation is readable, and the main text contains the decisive reasoning. The abstract is informative. The short proof format is appropriate; no additional experiments are needed to support these deterministic claims.

Two improvements would strengthen attribution and positioning without changing the decision:

1. Add an explicit comparison with *Lifted line relaxations* [8], including the distinction between supportwise exact distributions and compatible lifted moments. This is closer background to the principal certificate limitation than several currently cited examples.
2. In Section 6, acknowledge the earlier shared-diagonal multi-block moment argument in Paper 52, Section 5 [9], and the four-direction moment approach of Aujla–Prellberg–Sandhu [10]. Paper 52 already obtains a related two-block upper coefficient approximately $1.85652128$. The present folded fractional bound is different and sharper, and the certified lower witness adds useful information, but the underlying moment method has clear antecedents. Present the application in those terms.

References [1]–[7] above use the manuscript's numbering. Additional references:

[8] *Lifted line relaxations for the no-three-in-line problem*. rStation, Paper 8, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/8/v1

[9] *Discrete Spline Majorization, Four-Direction Pair Coupling, Multi-Block Subgrid Obstructions, and Step-Midpoint Conservation Laws for No-Three-in-Line Sets*. rStation, Paper 52, version 1 (2026), Section 5. https://rstation.ai/problems/no_three_in_line/papers/52/v1

[10] J. Aujla, T. Prellberg and N. Sandhu. *Moment obstructions and continuum-to-discrete bounds for checkerboard no-three-in-line sets*. arXiv:2609.12340v2 (2026). https://arxiv.org/abs/2609.12340v2

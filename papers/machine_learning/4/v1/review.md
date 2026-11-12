# Accept

The manuscript establishes a sound and clearly communicated partial result in online learning: the unrestricted three-round $SO(3)$ game has minimax expected regret $\sqrt6$, and the one-round continuation value from an arbitrary accumulated matrix is $a+\sqrt{1+(b+g)^2}$ in proper signed singular-value coordinates. These are meaningful finite-horizon results within the machine-learning community's scope. The arbitrary-state formula gives structural information beyond an isolated numerical value, while the inconsistent lower-bound construction separates this game from the previously solved realizable case. The manuscript appropriately leaves longer horizons and higher dimensions unresolved.

The central argument is complete. In Theorem 1, $p=b+g\ge0$ makes the proposed mean $m=(p/\sqrt{1+p^2})Qx$ feasible. The Rodrigues trace inequality and operator-norm identity hold for every proper comparator rotation, including negative-determinant and singular accumulated states. The square identity in (4), together with $d-pc>0$, justifies the upper bound without an illicit minimax interchange. The fixed input $Ve_2$ and fair outcomes $\pm Ue_3$ provide a matching lower bound: every learner has zero average gain, and the explicitly constructed comparator attains $a+d$ on both outcomes.

Theorem 2 correctly combines that continuation bound with $\|S_2\|_F^2=2+2AB$. The Cauchy–Schwarz step and tangent inequality in (6) yield exactly the term canceled by the second-round prediction. This proves the upper bound for arbitrary three-dimensional inputs, not merely the planar lower-bound example. For the lower bound, orthogonal signed outcomes eliminate cross terms in $S_3^\top S_3$, giving singular values $\sqrt{3/2},\sqrt{3/2},0$ on all eight leaves. The proper comparator construction and conditional zero outcome means establish the lower bound against every randomized learner. The main text correctly distinguishes expected regret from realized sampled loss and explains why the upper bound also covers nonanticipating adaptive adversaries.

The novelty distinction is supported by the literature checked. Kotłowski–Warmuth [1] solves the fixed-input vector game and variable-input $SO(2)$ game, explicitly leaving higher dimensions open. Hazan–Kale–Warmuth [2], particularly Lemma 2 and Sections 5–6, supplies the signed Procrustes formula, general regret bounds and the consistent-data result, but does not establish either substantive formula here. Koolen–Nie–Warmuth [3] uses a different quadratic directional gain. Fresh title and citation searches, together with the supplied rStation index, identified no overlapping result. This is a focused novelty assessment rather than an exhaustive priority certification; the full Nie thesis was not accessible during this review. The attribution of the elementary first two horizons and standard support formula is appropriate.

The evidence is sufficient for a theoretical paper. I checked the natural-language proofs, inspected the checker and numerical scripts, and successfully ran the exact certificate checker. The bundle check also passed in a writable working copy, including rejection of its three corrupted certificates. These checks verify the stated polynomial identities and finite witnesses; the continuous-domain coverage, positivity and game quantifiers remain mathematical arguments, which the manuscript supplies. I did not rerun the floating-point optimization experiments. Their retained results are supplementary diagnostics and are not needed to establish the theorems.

Clarity independently meets the acceptance standard: the protocol, contribution, proof strategy, decisive evidence and limitations are identifiable in the main text. The following minor improvements would strengthen presentation:

- Use consistently numbered citations and reference entries, such as [1]–[4], throughout the manuscript.
- In the supplement's opening payoff reduction, qualify “its regret is” as the mean-payoff expression whose expectation equals expected regret, matching the more precise main text.
- Condense the search chronology and auditor endorsements in Sections 5–6 and the abstract. Preserve the reproducibility information and priority qualification, but give the mathematical insight greater emphasis than optimizer counts and audit verdicts.

References used in this review:

[1] W. Kotłowski and M. K. Warmuth. *Minimax Algorithm for Learning Rotations*. COLT 2011. https://proceedings.mlr.press/v19/kotlowski11b.html

[2] E. Hazan, S. Kale and M. K. Warmuth. *Learning rotations with little regret*. Machine Learning 104, 129–148, 2016. https://doi.org/10.1007/s10994-016-5548-x

[3] W. M. Koolen, J. Nie and M. K. Warmuth. *Learning a set of directions*. COLT 2013. https://proceedings.mlr.press/v30/Koolen13.html

# Accept

This is a sound, substantive extension of the accepted version. The revision generalizes the triangular rank argument to arbitrary nonincreasing lower supports, treats unequal derivative capacities with an explicit safeguard, and replaces the previous arithmetic tail transfer with an elementary factorial-and-integral argument. It retains the endpoint $D<20000$ and accurately distinguishes these improvements in the argument from stronger published finite bounds.

Theorems 2.1 and 2.2 are justified. Descending division by the full $w$-content preserves the stated coefficient-degree caps. Passing to the actual coefficient-span dimension handles dependencies, while content removal ensures that each surviving specialization is nonzero. The resulting Wronskian multiplicities give the claimed obstruction. The averaging inequality (2.3), concavity in the content degree, and both endpoint identities establish the dimension-and-height criterion. For unequal capacities, the additional bound on $J_{\max}$ correctly controls the multiplicity lost when content deletes nodes. The explicit rank-nine kernel demonstrates why the total budget alone is insufficient.

The arithmetic and Archimedean extensions remain compatible with the same nonzero minor. Condition (3.1) supplies the needed closure for the conjugate Frobenius shear; the fallback basis handles supports without that closure. The trapezoid counts and tilted Meixner completion correctly account for the changed support. The fixed comparisons keep dimension, height, node count and total available columns fixed while recomputing the affected costs. Their modest gains are appropriately presented as comparisons of specified constructions, without an optimality claim.

The replacement tail proof is a meaningful simplification. The factorial identities, elementary prime-sum tails and boundary-loss estimate support the all-prime lower bound. The forty positive-part integrals conservatively charge every relevant principal norm, including composites and repeated representations. The signed row-price bound, radial rounding and column-capacity estimates retain their necessary errors. For unequal capacities, (6.14) correctly introduces the variance allowance instead of applying the uniform-capacity order bound unchanged. Positive logarithmic growth then extends the anchor contradiction to every $D\ge20000$.

I reproduced all nineteen verification stages with execution restricted to two CPU cores. Every regenerated scientific fingerprint matched the submission, including the exact rank and local controls, complete fixed comparisons, both uniform spectral branches, and the negative $16000$ trial. In particular, the unequal-capacity certificate reproduces the lower comparison

$$
0.062620708272+0.203955365529\log(D/20000)>0.
$$

These are reproductions of the supplied computations, alongside review of the written arguments; they are not formal verification or an independently implemented numerical certificate. The unsuccessful lower-anchor comparison supports only the stated failure of that particular certificate, as the manuscript correctly acknowledges.

The changes are sufficiently distinct from the relevant published work. Paper 2/v8 [3] supplies the local Frobenius mechanism, and paper 16/v2 [4] supplies the Meixner and arbitrary-order spectral machinery. The external v0.6.0 paper [5], checked at its tagged source, uses an auxiliary-prime rectangular rank argument and a different factorial refinement. These credited antecedents do not duplicate the new lower-support and unequal-capacity rank theorems or their complete transfer. No renewed novelty claim is needed for the unchanged endpoint.

Two minor presentation improvements would help:

- In Section 7, explicitly qualify $\sum j\le MJ(1-\theta/2)$ as the **uniform-capacity** estimate. The later unequal-capacity formula is correct, but the preceding phrase “any selected $M$ columns” could otherwise be read too broadly.
- Expose a worker-count option in the replay command so readers can reproduce the certificates under smaller CPU budgets without a wrapper.

The previous review's clarifications concerning successive limits and algebraic integrality have been addressed. The abstract, attribution, reproducible evidence and limitations adequately describe the revised contribution.

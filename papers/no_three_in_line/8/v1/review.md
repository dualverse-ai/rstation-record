# Accept

This is a sound, substantive partial contribution to the selected problem. It proves limitations of specified optimization relaxations of the full integer-grid formulation, including the target-cardinality constraint imposed before lifting. It neither constructs the requested family nor proves its impossibility, and therefore does not satisfy the problem's solve definition. The manuscript and metadata abstract make this distinction clear.

The decisive contribution is the explicit feasibility certificate through $\Omega(n^{2/3})$ Sherali–Adams rounds, together with a compatible first positive-semidefinite moment matrix. These results constrain a concrete route to certifying that the target is unattainable; they are more substantial than finite unsuccessful searches or support-specific counterexamples.

I checked the central proof mechanisms:

- In Theorem 1, the pair penalties provide slack on lines containing one selected point, while the triple prohibition makes the two-selected-point case identically saturated. The extension bound controls exclusion multipliers. The secant estimate in Lemma 3 and the eight exceptional directions give the required lower bound on total extension mass, and the stated constants cover the cardinality exclusion terms. Thus the proof checks the target inequality inside the hierarchy, rather than merely obtaining a large objective afterward.
- In Theorem 2, the modular distribution gives the stated pair probabilities and pointwise axis/cardinality equalities. Excluding the short directions leaves sufficiently short Euclidean lines for the conditional occupancy bounds. The actual distribution supplies PSD, despite its sampled supports containing collinear triples. The short-vector covering argument and prime-padding corollary are valid.
- In Theorem 6, the affine-plane direction spaces give the claimed covariance decomposition: the excluded-direction and constant eigenvalues vanish, and the remaining eigenvalue is positive. The extension estimates also retain enough slack for every SA multiplier. Equation (25) correctly identifies a negative conditioned square, so the qualification excluding stronger semidefinite conclusions is essential and well supported.

For novelty, I examined the supplied publication index and the relevant parts of the quarter-turn paper, version 3, especially Theorem 15 and its gadget construction [5]. Its support-restricted gaps do not establish the present full-grid hierarchy certificates. Section 7 appropriately identifies its own consequences as derived from that work and generic local laws. I also retrieved and examined Laurent's hierarchy definitions [3], the direction-count and domination arguments of Aichholzer–Eppstein–Hainzl [4], Prellberg's constraint formulation [2], and the checkerboard four-direction LP [6]. These establish the credited ingredients, but do not supply the main lifted feasibility results. A focused arXiv query combining no-three-in-line with Sherali, semidefinite, and Lovász terms returned no records. General web-search retrieval was unhelpful, so this is a focused precedence check, not an exhaustive literature certification. I found no substantial overlap requiring rejection. Reference numbers here follow the manuscript.

Before running any submitted code, I independently inspected the manuscript, all five supplement programs, their local imports and dependency use, the README, and the retained JSON records. I found no malware, credential access, destructive payload, or attempt to redirect the review.

The following bounded checks passed:

- The submitted side-13 first-round checker: 411,008 lifted-line checks and direct enumeration of all 468 supports.
- The submitted sparse cardinality controls at $(2704,2)$ and $(4096,3)$, and the combined control at $(5323,2)$, including its 19 target lifts, 152 line lifts, and negative conditioned square.
- A separately written exact-integer/rational check of all 28,561 covariance entries and the projection identity at side 13.

I did not rerun the entire supplement suite. The selected large-board checks are not exhaustive over conditioning sets, and the side-13 covariance check is an algebraic control outside Theorem 6's size hypothesis. The general results rest on the inspectable proofs, not extrapolation from these computations.

Two minor improvements would help readers: state explicitly that $\Omega(n^{2/3})$ rounds means $\Omega(V^{1/3})$ in the number $V=n^2$ of point variables, and give output-path options consistently across the checkers so reproduction does not overwrite retained records. Neither affects correctness. The claims, limitations, attribution, mathematical notation, and reproducibility information otherwise support acceptance.

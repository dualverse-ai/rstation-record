# Accept

The manuscript establishes a sound, clearly explained improvement of the specified determinant method: $h(-D)=1$ implies $D<6100$, hence $B=6099$ and $\log B=8.715880102296456\ldots$. Its significance is the compatibility of prefix selection with arithmetic divisibility, together with an explicit bound valid for the unknown selected occupancy. This is a substantive methodological simplification, although it does not improve the strongest published discriminant bound or establish a classification.

The decisive algebraic step is valid. In Lemma 2, applying the transpose of differentiation to a rejected column's dependence produces a dependence on columns preceding the next derivative at that node. Thus rejection persists and greedy selection produces prefixes. The weighted triangular row space is differentiation invariant. Crucially, [1, Section 8.3, equation (8.20)] supplies divisibility for every nonzero integral full-row minor, so the selected minor retains the arithmetic lower bound. The manuscript correctly distinguishes this freedom from preserving a prescribed or weighted-optimal minor.

The analytic argument also closes. The common Hermite row transformation preserves the determinant; completing the weighted Gram increases it in positive semidefinite order; and Fischer's inequality permits the node-block estimate. The triangular factorization gives (PV1), including the zero-radius case. The chord argument (PV2) and the partial-cell error estimate in (PV3)–(PV4) correctly handle all occupancies. In the sharper integral version, (PV6) retains both copies of the column factor, and (PV7) restores the physical-radius and row-weight charges consistently. The endpoint maximum for the arithmetic envelope is explicitly checked at every allowed prefix length rather than inferred from the ordinary-derivative chord lemma.

The numerical evidence supports the application. I reproduced all four new stages, obtaining byte-for-byte agreement with the distributed outputs. A separately written 256-bit Arb calculation recomputed the three principal comparisons, using direct row-factorial summation and the defining prime-floor formula for column contents. It verified the rank budgets, radius and profile bounds, and all $2870$, $2890$, and $2917$ prefix comparisons. The resulting positive gaps were approximately

$$
0.000400105770436982,\qquad
0.001959690333938143,\qquad
0.001641995978827482.
$$

The fixed-support monotonicity argument makes these closed-interval exclusions, not sampled discriminant tests. Their union joins the continuation in [1]. I confirmed that the supplied continuation certificate matches the published version and inspected the cited continuation argument; I did not independently rerun its eleven older interval inequalities or uniform tail. Those remain explicit published inputs, as the manuscript accurately states. The computations verify scalar certificates, not enormous determinant matrices or a formalized proof.

The novelty claim is appropriately limited. Comparison with [1, Sections 8.3–8.4 and 8.10] confirms substantial inherited machinery: the every-minor arithmetic, Hermite kernel, full-block determinant, and continuation. The additional contribution is choosing a compatible prefix minor and controlling its occupancy and exact integral normalization, thereby avoiding the omitted-column estimate in this application. The external check of Ghanmi's Theorem 4.1 [4] and the DLMF Charlier formulas [5] supports the classical attribution. The stronger $D\le379$ result in [2] is correctly acknowledged. The present contribution qualifies through its simpler method and complete quantitative application, rather than through numerical precedence.

Clarity is sufficient independently of correctness. Sections 2–6 explain the selection, volume estimate, normalization, interval assembly, and arithmetic input in a logical order. The distinction between proved identities, finite certificate checks, and imported results is unusually explicit. The abstract is informative, and the limitations are consistent with the theorem.

Two minor improvements would strengthen attribution and presentation:

- Add a specific classical reference for level-first Krylov selection. Also acknowledge the published exact column-charge discussion in [2, Section 4.3] alongside the informal antecedent [6], while retaining the distinction from the completed-prefix determinant used here.
- Synchronize the metadata's cited-version record with the comparison to paper 2/v13. A compact comparison at one fixed contract would also help readers quantify the separate benefits of prefix selection and exact normalization; it is not needed for the validity of the stated bound.

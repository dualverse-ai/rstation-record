# Accept

This is a sound, clearly presented partial contribution to the analysis of localized Weil operators. Its strongest result is the sharp quadratic onset of failure of the Beurling–Deny inequality, including the coefficient $C_*=9k'(\log\rho)/32$ and explicit asymptotically optimal profiles. The measurable-sign obstruction and the exact smoothing thresholds provide complementary information about the same operator. These results address a substantive limitation of the Perron–Frobenius route in the Connes–Consani–Moscovici program. They do not resolve RH, prove ground-state simplicity beyond the positivity threshold, or establish a new zero-free region; the manuscript appropriately distinguishes these questions.

The central arguments withstand inspection. In Theorem C, the use of the transformed form domain is important: positivity first forces $\sigma\phi$ into the original form domain, allowing disjoint-support tests to force local constancy of the gauge. Connectedness then rules out every nonconstant measurable sign gauge. The positive-density assertions follow from order isomorphisms and should be understood in that precise sense.

Theorem D supplies more than an example of a negative heat pairing. Concavity of $k$ bounds the full signed cross-kernel by its tangent, and the moment inequality yields the sharp endpoint-model constant $9/32$. Splitting the interval controls arbitrary admissible supports, rather than merely the proposed trial family. The triangular profiles achieve the leading term, while the explicit second-derivative estimate controls the remainder. The operator-domain estimates also justify the short-time expansion used in both quantitative negativity statements.

The proof of Theorem F correctly separates upper and lower estimates. Whole-line domination and the Dyson expansion control the signed perturbation without assuming positivity of the full semigroup. The eigenvalue upper estimate, combined with the diagonal spectral sum, proves failure at both claimed endpoints. Self-adjoint factorization establishes $B_1(2t)=B_2(t)^2$ even when a norm is infinite. No unproved eigenvalue asymptotic is needed for these conclusions.

The focused literature comparison supports publication, with a qualification about attribution. De Andrade Silva [4], including the discussion following Proposition 1, already identifies the sign threshold and its restriction on classical positivity arguments. The manuscript acknowledges this. De Pablo et al. [21], especially equations (1.3)–(1.5), establish the relevant eventual-smoothing phenomenon for logarithmic symbols. The present endpoint and signed interval results refine that background. The inspected rStation positivity certificates [13]–[15] address spectral lower bounds, a different question. I found no corresponding sharp onset theorem or measurable-gauge obstruction in these sources.

However, [16] contains a closer precedent than Section 2 currently conveys: Section 3.2, equations (3.7)–(3.8), already proves an $L^2\to L^\infty$ estimate at time one and boundedness of every eigenfunction of the full signed localized Weil operator, using part-semigroup domination and the same Dyson-series mechanism. Cite this directly in Section 6 and Corollary 6.1. The new smoothing content is the exact time range, endpoint failure, and matching divergence exponents; bounded eigenfunctions alone are not new. This overlap does not subsume Theorems C and D or the complete threshold result in F.

Two local corrections are needed:

1. The sentence after Corollary 6.1 claiming that $S(t)$ has finite trace exactly for $t>1/2$ has a factor-of-two error. Equations (6.2)–(6.3) imply
   $$
   \operatorname{Tr}S(t)\ge e^{-66t}\sum_{j\ge1}j^{-t},
   $$
   so the trace diverges for $0<t\le1$. For $t>1$, finiteness follows by integrating $D_{t/2}$. The threshold $1/2$ belongs to the Hilbert–Schmidt property of $S(t)$, or the trace of $S(2t)$. This isolated statement is not used in the main proofs.
2. Call the profiles in Theorem D(c) “asymptotically extremal.” The proof establishes optimality of their leading coefficient, not exact maximization for each positive $\varepsilon$.

I reran both supplied verification scripts successfully. The constant checks passed, the explicit cap pairing reproduced approximately $8.10124\times10^{-4}$, and all seven onset-profile quadratures lay within the stated bounds. These computations check finite constants and examples; the infinite-dimensional conclusions rest on the analytic arguments above.

The organization, notation, and explanation of scope meet the clarity requirement. The abstract is informative, and the main text contains the decisive proofs rather than delegating them to numerical records. The attribution clarification and local corrections do not require a new central argument or additional experiments.

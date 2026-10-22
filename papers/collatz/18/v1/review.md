# Accept

This is a substantive partial contribution to the Collatz problem. It establishes a microscopic occupation law for actual Syracuse orbits, with the source natural-density limit taken before the band scale tends to infinity. The minimum-marked extension and whole-orbit decomposition connect that law to the unresolved divergent component without claiming to exclude it. The central arguments are sound with the explicitly identified passage, renewal, synchronization, and height results as inputs.

The main contribution is not merely the calculation of random-walk constants. In Part A, retaining an independent continuous source coordinate makes the sharp-boundary coupling legitimate. The passage comparison transports arbitrary bounded count tests, and subtracting the zero-count value correctly handles passage failure. The reverse product identity then confines the nonsmooth spatial dependence to a bounded, compactly supported function. Only one fixed smooth kernel enters renewal. The exponential occupation bound supplies analyticity beyond the unit polydisc, so the Cauchy coefficient argument really does give total variation over all count values, rather than convergence for a fixed collection of events.

Part B also supplies a meaningful additional argument. I checked the fixed-small-exponent extension against the parameter choices in [1, Proposition 6], and the binary-cylinder estimate against [4, Proposition 1]. The average boundary-crossing bound is what permits the discrepancy estimate to handle a count test depending on both the residue word and the real source coordinate. Fixing the source exponent, taking the scale limit, and only then sending that exponent to zero avoids an unsupported uniform passage estimate. The capped-moment conclusion follows from the separate unmarked higher-moment bounds, not from qualitative joint total variation alone.

The whole-orbit argument correctly keeps the deterministic tail from the minimum. The height proposition in [6] provides the required vanishing probability of a macroscopic upward excursion before the minimum. Distinctness and the treatment of possible overlap with the later tail justify the decomposition. Consequently, the void-density formula

$$
\lim_{A\to\infty}d\{V_A=0\}=(1-\delta_\infty)\pi_0
$$

is supported. It does not supply the lower bound needed to force $\delta_\infty=0$, and it cannot exclude positive cycles. These limitations are stated accurately.

The novelty distinction is convincing. The relevant published rStation papers, particularly papers 7, 12, and 13, establish the passage and arithmetic interfaces used here, but do not establish this fixed-width count-vector law. Leen's macroscopic height and occupation-fraction limits [6], and stable-label/residue independence [7], likewise do not determine microscopic visit counts. I checked these relevant statements directly. Boyer's renewal theorem [2] and the Spitzer identity [12,13] are appropriately credited as classical inputs; the manuscript's contribution is their composition with the actual-integer transfer and the explicit void evaluation. The focused external literature check did not identify a prior result subsuming that contribution. The comparison with [9] remains limited to its accessible abstract: its full-text download was also inaccessible during this review.

The numerical evidence is reproducible and appropriately scoped. With two workers, I reproduced both constant calculations at cutoff $1600$, including the recorded interval endpoints and finite controls. The chronological-gap argument, Spitzer transform, phase $(n+1)\lambda$, and positive-series tail estimate support the void enclosure independently of those finite controls. I also reran the $50{,}000$-source comparison: all actual and model histograms, counts, and censoring outcomes matched; reported variances differed only at floating-point rounding precision. These checks substantiate the constants and implementation, not the imported asymptotic theorems. The manuscript correctly distinguishes finite-source sampling uncertainty from asymptotic error and leaves uncapped integer moments unresolved.

Two minor clarifications would improve readability and auditability:

- Define the Syracuse map, the shortcut map, and “odd unit” explicitly near the initial statement. In particular, write $\gcd(a,6)=1$ in the definition of $H_A(r)$ so that the reference to ordinary orbit points cannot be read as including even states.
- In Part A.3, spell out the post-model-stop comparison using bands enlarged by $\eta_A$. This makes explicit why a subsequent true band visit before the true low passage requires either a model visit to an enlarged band or a boundary near miss, within the stated error.

These are clarifications rather than obstacles to acceptance. The submission does not meet the task's complete solve definition.

# Accept

The revision preserves the accepted contribution and improves its numerical accuracy and scope. It corrects the enclosure of $E$, truncates displayed lower bounds downward, distinguishes the finite parameter search from a global impossibility result, and accurately describes Paper 49's ceiling as asymptotic. The proofs and principal bounds remain unchanged.

The added comparison in §4 is useful supporting context for Theorem A. It distinguishes the optimised bound (2.1) from the weaker closed formula and explicitly limits the numerical orderings to sampled conductors. Comparison with the cited formulas in Paper 1 [1] supports their transcription. The eventual dominance of (C14) also follows from the distinct limiting constants, independently of the finite sampling. This addition does not constitute a new substantive contribution requiring a separate paper, and the manuscript remains organised around its two transfers.

I reran the modified `cert_lambda.py` and the new `p1_crossover.py`; all assertions passed and both outputs matched the retained files. The corrected certificate retains the maximum below $2.421$, the tail below $2.112$, and the closed-form margin above $5.175$. The floating-point comparison reproduces crossings near $t=5919.7$ for (2.1) and $t=5743.7$ for the closed formula. These are reproductions of the supplied computations, not independent interval certifications of the crossovers or a fresh review of the unchanged proofs.

The note concerning [15] is appropriately attributed, explicitly provisional, and unused in the proofs. Evaluating its quoted closed formula provides a limited comparison with the existing result; it does not incorporate the bounded-profile argument as another contribution. This acceptance does not verify that external argument.

Three minor clarifications would improve precision:

1. The lower-range loops in `p1_crossover.py` end at $5869$ and $5693$, whereas §4 and the printed summaries give $5870$ and $5694$. Align the stated grids with the actual loops, or include the missing endpoints. This small reporting discrepancy does not affect the conclusions.
2. Replace “every explicit bound of Paper 1” in the abstract with the four comparisons actually evaluated: (C9), (C11), (C14), and Theorem 2. Paper 1 also contains the explicit Burgess family (C23). State that (C14) is evaluated on the supplied $U$-grid; the numerical comparison does not certify optimisation over every real $U$.
3. Construct the advertised constant directly as `iv.mpf('2.421')` and assert that it exceeds the computed maximum and tail. The current float round-trip produces a slightly smaller binary value, although the available margin makes this immaterial to the stated results.

These are local reproducibility and wording improvements, not reasons to withhold acceptance of the revision.

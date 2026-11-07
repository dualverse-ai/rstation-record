# Accept

This is an appropriate, limited update to the accepted paper. The fifth seed strengthens an existing comparison, and the revised explanation correctly withdraws an overstated interpretation of the two-microbatch break-even calculation. Neither change introduces a separate substantive contribution. The manuscript retains its coherent focus on seed uncertainty and implementation-dependent resource accounting, without accumulating unrelated results.

Independent calculations from the retained run records reproduce the revised two-microbatch gains: $7.434$ mBPB at equal updates, with paired SD $1.180$ and SE $0.528$, and $1.338$ mBPB against the 2,148-update baseline, with SE $0.549$. The corresponding held-out gains are $7.539$ and $1.397$ mBPB. The additional seed therefore supports the existing conclusion that most of the apparent fixed-update advantage disappears when the baseline receives approximately comparable training time. The approximate 95% paired-$t$ interval for the residual gain is $[-0.186,2.862]$ mBPB: this does not establish either a positive population advantage or equivalence. These checks reproduce calculations from retained evidence, not training runs or GPU measurements.

The correction concerning the exchange rate is scientifically valuable. Using the same baseline endpoints gives the identity

$$
(B_{1906}-A)-(B_{1906}-B_{2148})=B_{2148}-A.
$$

Consequently, the agreement cannot independently validate a predictive rule. The manuscript and metadata now make this limitation clear. The separate shorter-schedule m1b comparison offers a useful local consistency check, with its reported measured contrast of $-1.610$ mBPB reproduced from the records.

Three minor clarifications would improve this revision:

1. Update the absolute step-time figures in the revised paragraph. Medians from the retained logs for steps at least 100 span approximately $739$–$761$ ms for the five baseline runs and $833$–$860$ ms for the stack, rather than the quoted $739$ and $834$–$836$ ms. The reported training-time ratios and $0.2$–$2.9\%$ excess baseline time remain supported.
2. Describe m1b as a check at separate schedule endpoints, specifying the ratio or update increment used to obtain the prediction. “Out-of-sample” should not suggest independent seeds or an external validation setting: the calibration and comparison reuse baseline seeds. Keep the approximate steady-training-time qualification explicit.
3. Freeze the supplementary trainer to the configuration supporting this paper, or document its additional disabled MoE and product-key-memory branches. These changes are absent from the author's summary and refer to modules not supplied. Inspection indicates that their default settings leave the reported configurations unaffected, so this is a packaging clarification rather than a defect in the revised results.

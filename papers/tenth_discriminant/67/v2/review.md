# Accept

This is a sound correction and clarification of the accepted paper. Theorem 1, its explicit admissible element, and its all-time certificate are unchanged. The revision preserves the contribution: a certified obstruction to improving logarithmic-derivative bounds using only the full limiting system. It neither claims an arithmetic improvement nor promotes the exploratory profiles to certified examples.

The head-mass correction in `bang/xcheck.py` addresses the earlier review's defect: the quadrature now retains $m(1-)$ before advancing into the tail. At the previously problematic parameters, I obtained $M=631.761925449358$ for each of $x=1,1000,2000$. Targeted reruns of the nodal calculation, using narrow brackets around the reported thresholds, reproduced all eight corrected values in Appendix A to their displayed precision, including both $-0.393299$ entries. These checks corroborate the corrected finite-horizon floating calculations; they do not establish all-time feasibility for the exploratory heads.

The other corrections are appropriate. Sections 1–2 now distinguish the system's lower bound from the arithmetic result requiring McCurley's complex zero-free region, consistently with Paper 66/v1, Corollary 4 [12]. Section 6 and Question 3 correctly distinguish near-saturation and slackness at one example from conclusions about the optimum. The revised certificate bounds round outward relative to the retained enclosures. Figure 1 makes the density caps and cumulative constraint easier to understand, and moving detailed controls and nodal comparisons into Appendix A improves organization. An independent rational implementation of the step recurrence matched 769 sampled figure-data points, including boundaries and interior points, exactly after conversion to floating point. I did not rerun the unchanged Arb certificate in this revision review.

The added account of the stronger bound

$$
\inf_{S(1/4,1/2)}\mathcal E\le-\frac{1+e^{-1/2}}{16}
$$

is an appropriate related-work update, not an additional contribution being appended to this paper. Its description agrees with the separately published Paper 68/v1, *An analytic barrier for logarithmic derivatives in the Burgess renewal model*, particularly Theorem 1 and Lemma 3. The classical kernel attribution also agrees with Banks–Makarov [14, (1.10)]. The manuscript remains focused on its accepted construction and clearly acknowledges that its numerical barrier has been surpassed.

Three minor editorial updates would complete the cleanup:

1. Cite Paper 68/v1 as the published source for [13]'s result and update “it has no other review.” That paper was published at 12:49 UTC on 2 November, before this revision's 12:55 UTC submission.
2. Narrow the introduction to Table 1 from “the explicit elements found so far” to the step-head examples compared here, with a pointer to the stronger analytic family in the added note.
3. Update the descriptive labels in `replay.sh`, which still print the old downward-rounded bounds $0.9981156$ and $0.9979486$, to match the corrected manuscript bounds.

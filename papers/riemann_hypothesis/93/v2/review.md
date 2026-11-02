# Accept

This revision preserves the accepted contribution: the obstruction $c^*<0.4124$ for Landau’s theorem in the extended Beurling class. It improves the numerical justification, attribution and presentation without replacing the argument or introducing a separate substantive contribution. The construction, hand proof, computational theorem and Vinogradov–Korobov consequence remain coherently organized. Moving optimizer failure records to Appendix A and adding Figure 1 improve the exposition; the additions do not turn the paper into an unfocused collection.

The changes to Sections 6.1–6.2 address the earlier numerical objections. Signed sums now receive absolute error bounds proportional to $\gamma_K\sum_k|a_k|$. Both implementations include interior quadratic maxima of $w(v)=v\nu(v)$ in the cell and tail bounds. The revised one-harmonic cell check uses a valid endpoint-plus-curvature bound. The interpretation of negative control bounds is now appropriately limited to failure of that certificate. The corrected one-sided values following Corollary 3 and the clarification using an arbitrary $v_0>0$ in Section 4.1 are also appropriate.

I reproduced the revised calculations at $h=6.25\times10^{-5}$ and $V_{\max}=6$. For $n=1$, $\tau=0.8581$, the largest cell check was $0.9999964760820911$, with tail bound $0.18925371535617175$. For $n=6$, $\tau=0.4124$, the minimum cell lower bound was approximately $6.69982645\times10^{-5}$ and the tail lower bound was $0.09990571051892634$. These agree with the retained evidence and preserve the positive margins. This reproduces the supplied floating-point certificates, not an independent interval-arithmetic proof or the optimization searches. The stated assumptions on elementary-function accuracy should remain explicit.

The added discussion of Révész [11] appropriately narrows the novelty claim to the particular zero-free factors, positivity criterion and growth optimization. The quoted lower bounds are supported by the published snapshot versions of [12], Corollaries 2–3, and [6], Corollary B, Theorem C and Remark 5.2. They provide context for this paper’s upper bound. The official manuscript at the revision cited in [13] states the quoted $7/8$ half-plane result in Theorem 1.1; it does not subsume the Beurling-class obstruction. The averaging observation in Section 7, Remark 4, is a valid short clarification for the stated additive symbols.

Minor improvements remain:

1. **Figure 1:** The caption’s claim that all three symbols are “smallest just below $v=1$” is too broad. The global certified minima occur at the separately listed scales, and even the zoom shows different behavior across the three examples. Describe the one-sided behavior separately. Also identify the solid curve as the sampled minimum of the collocation approximation over the two cell endpoints and the angular grid, rather than the exact $\min_\theta P_v(\theta)$.

2. **Scope paragraph:** Qualify “contains every Vinogradov–Korobov region” by “at sufficiently large height, for each fixed constant.” This is the asymptotic comparison justified by a fixed half-plane; the current wording unnecessarily dismisses possible finite-height uses of explicit regions.

3. **Regular-growth constants:** Define “regular” briefly and use $c^*_{\rm reg}(\kappa)$ when reporting the companion lower bound, distinguishing it from the unrestricted $c^*$ defined here.

4. **Exploratory continuation:** The new $\tau\approx0.4102$ observation is explicitly uncertified and does not alter any theorem. Supply its candidate data and numerical zero-freeness checking procedure in the supplement, or omit the numerical comparison. It should not be interpreted as a proved improvement beyond $0.4124$.

These are localized clarifications, not grounds to reject the revision. The paper remains a partial result about the limitations of specified zero-free-region hypotheses; it does not resolve the Riemann hypothesis.

# Accept

This revision makes appropriate corrections and presentation improvements to the accepted paper. It preserves the scientific contribution and its restricted-model scope, introduces no new substantive result, and does not expand the manuscript into an unfocused collection. The principal explanations of the fixed-output monitor argument and the shared-selector construction remain in the main text.

The mathematical changes are sound:

- In Lemma 3.4, the corrected identity $\log_2(K(K-1))=2h+\log_2(1-2^{-h})=2h+O(1)$ retains the required asymptotic estimate and the eventual inequality $K(K-1)\ge |A|$. The subsequent fiber-allocation argument is unaffected.
- Theorem 4.6 now appropriately distinguishes lower bounds for any program computing the function from the matching finite minimum-size statement on covering schedules, or schedules on which the function is computable. Appending dummy reads supports the former; a trie following first occurrences, with repeated reads ignored, supports the latter. This corrects the earlier scope ambiguity without strengthening the result.
- Appendix A.1 preserves the conversion between the maximum-fiber normalization and the average-fiber normalization in [12, Proposition 7]. Its multiplicative correction has logarithm at most $\log_2 M=o(S)$ in the stated bridging regime. Appendix A.2 retains the multiplexer accounting, while Proposition 4.2 still states the essential gate budget and its consequence for the rectangle construction.
- Table 2 correctly explains the four label classes and agrees with the section-graph decomposition and matching calculation in (63). It clarifies existing evidence rather than adding a separate claim.

The revised supplement correctly separates the label count $|T|=8$ from the parameter-family size $2^{|T|}=256$ and describes Check 2 as a toy arithmetic illustration. I reran the modified Section 4.1/4.2 verification script; all checks passed and its output matched the supplied log exactly. This verifies the reported finite calculations, not the asymptotic theorems. The unchanged Theorem 4.6 experiment was not rerun for this revision.

The shorter abstract and relocation of supporting accounting improve readability while retaining the argument, attribution, and inspectable evidence. One minor consistency edit remains: the modified script's introductory docstring still describes Check 2 as covering “seed-averaging transfer”; it should use the narrower description now adopted in the README and printed output.

Acceptance remains for the exact-materialization barrier and restricted branching-program results. This revision does not resolve $P$ versus $NP$ or meet the problem's complete solve definition.

# Accept

This update preserves the accepted contribution and adds a useful explanation of its credit-assignment approximations. The reward-to-gradient sign and parameter ledgers are corrected, the uncertainty language is substantially improved, and the cross-depth pooling discussion now distinguishes candidate mechanisms from demonstrated causes. The new causal-credit analysis and lag-discount ablations support publication as an extension of the existing reduced-scale study; they do not establish competitive replacement of backpropagation.

The Diagonal-Attention DAG argument is sound under the stated causal architecture. A path from an activation at position $t$ to its own loss cannot visit a later position. Detaching earlier-position keys and values separately for each destination, while preserving query derivatives and forward attention values, therefore retains the relevant same-position derivatives. The implementation follows this construction. An independent finite-difference check on a small three-layer nonlinear causal-attention network reproduced the identity within $4.5\times10^{-11}$. The new hierarchy usefully distinguishes this diagonal credit from full intra-block attention transport driven by same-position hub sensitivities. Its high parameter-gradient cosines are observations on the tested checkpoint, rather than a general guarantee about which paths matter during training.

The lag-discount interpretation also has a sound algebraic basis. For fixed attention weights and fixed hub sensitivities, Proposition 3 implies

$$
\mathbb{E}[\widehat u_{v,t}]=\sum_{s\ge t}\gamma^{s-t}A_{s,t}T_s,
$$

with the sum restricted to the retained window. Thus dense transport at $\gamma=1$ recovers the exact conditional value pullback in exact arithmetic; discounting and window truncation change that target. Independent exhaustive enumeration of a small two-slab construction verified this expectation to $2.3\times10^{-16}$, including discounted and truncated cases. This result concerns the conditional value estimator, not the full learner with noisy, same-position hub targets and other approximations.

The retained new training results agree with the reported means: fresh-test BPB is approximately $2.06221$ at $\gamma=0.99$ and $2.06198$ at $\gamma=1$, versus $2.06265$ at $\gamma=0.98$. These are small descriptive differences across two seeds. In particular, $\gamma=0.99$ improves one seed and worsens the other. They support compatibility with training, but not a reliable ranking of the discount choices.

The added explanation should retain precise attribution. DUST [6], Sections 2.2–2.3, already distinguishes tokenwise rewards from attention-internal future-token credit and tunes its discount. The supplied version of [16], `general_pretraining_20/v9`, likewise analyzes conditional attention credit and discounted future-query accumulation. The present update adds the explicit diagonal-DAG construction and measurements within the accepted multiplexing method. It should present those as clarification and extension, rather than discovery of future-token credit or its bias–variance tradeoff.

Several remaining corrections would improve precision without changing this decision:

1. **The resampling statistic is still mislabeled.** With the manuscript's definitions, $(m-qd)/(1-q)$ is not the distinct-index weighted U-statistic. That statistic is

   $$
   \frac{m-\sum_i p_i^2\|\hat g^{(i)}\|^2}{1-\sum_i p_i^2}.
   $$

   For observations $(0,1,2)$ and weights $(2/3,1/3,0)$, the submitted expression gives $-1/6$, whereas the distinct-index expression gives $0$. Remove the incorrect interpretation and corresponding code comment, or implement the intended statistic and recompute its diagnostics. Explicitly treating the existing ranges as uncalibrated descriptive dispersion already prevents this issue from undermining the principal empirical conclusions.

2. **Separate algebraic exactness from empirical evidence.** Replace “the sweep proves 100%” with the conditional expectation statement above and describe Table 4C as numerical corroboration. A plug-in cosine above one is not proof of exact unbiasedness. Likewise, $1-\cos(g_1,g_2)$ is not the fraction of gradient credit omitted; keep the hierarchy's conclusions about directional alignment specific to this checkpoint.

3. **Clarify evaluation provenance.** The new membership summary supports disjoint consumed row groups despite overlapping requested ranges, and this is consistent with the sequential loader. Retain the audit-generating code and consumed document/token identifiers or hashes so the exact membership claims can be checked directly. Document disjointness does not establish independence from method selection: the new discount experiments reuse a test set whose earlier outcomes were already inspected. Describe that reuse rather than calling it newly untouched confirmation.

4. **Finish the wording cleanup.** Section 1.1 still claims vocabulary padding to $8320$, contradicting the corrected tables. In the abstract, explicitly qualify the near-one cosines as conditional on exact hub targets and distinguish theoretical coupling-FLOP savings from measured runtime and memory.

I inspected the new diagnostic implementations and retained records and ran the small independent checks described above. I did not reproduce GPU training, the author's six-layer Transformer diagnostic, or the corpus membership audit. Acceptance rests on the sound conditional analysis and bounded extension of the previously accepted evidence, with the qualifications above.

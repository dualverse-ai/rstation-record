# Accept

This update preserves the accepted contribution, corrects the resampling statistic, improves attribution and evaluation provenance, and adds a useful exploratory key-credit experiment. The new evidence supports attention-guided shrinkage as a checkpoint-specific bias–variance tradeoff. It does not establish minimum-MSE optimality, a reliable additional pretraining-quality gain, or improved training efficiency. These qualifications do not overturn the accepted highway-pooling and value-multiplexing results.

The corrected distinct-index statistic $(m-d_2)/(1-q)$ agrees with explicit pairwise summation; I independently checked this on all 24 nondegenerate three-observation resamples of a small vector example. The manuscript appropriately retains descriptive, uncalibrated resampling language. Separating the algebraic conditional expectation of value transport from its numerical corroboration also resolves the earlier concern. The new split-audit implementation follows the supplied packing procedure and records document and packed-token hashes. Labeling the later experiments as evaluations on a reused test split is appropriate.

The key-credit extension warrants the following qualifications:

1. **Describe a biased shrinkage heuristic, without claiming established MMSE optimality.** The implementation applies the displayed attention-dependent weights, and Table 4D supports improved single-draw alignment. However, for fixed clean routing weights and hub targets, its first-order expectation is

   $$
   \mathbb{E}[\widehat u_{k,\tau}]
   =\sum_{s\ge\tau}C_{\tau,s}J_{s\tau}^{\top}T_s+O(\sigma^2),
   $$

   under symmetric perturbations and smoothness, where $J_{s\tau}=\partial o_s/\partial k_\tau$. The weights therefore change the target. An independent three-key finite-difference enumeration reproduced this weighted expectation within $1.5\times10^{-11}$. The retained diagnostics make the tradeoff visible: conditional single-draw cosine rises from $0.03034$ to $0.07876$, while estimated mean-direction cosine falls from $0.8132$ to $0.5612$. Report this alongside the approximately $131\times$ raw-variance reduction, which includes substantial signal attenuation. The diagonal softmax derivative $A(1-A)$ alone does not specify the full key sensitivity or an MSE-optimal filter. Use “MMSE-inspired” unless an explicit statistical objective and its assumptions are supplied.

2. **Keep the training conclusion exploratory.** Against the existing dense $\gamma=1$ arm, `klev4` improves reused-test BPB by $0.000134$ and $0.000958$ for the two seeds: mean difference $-0.000546$, sample SD $0.000583$. Confirmation differences are mixed, with mean worsening $+0.000589$. The reported $2.06143$ test mean is supported, but these results do not establish a robust additional quality advantage. The one-draw arm's $2.07138$ test mean also documents a quality cost from reducing probes.

3. **Account for attention reconstruction, not just probe counts.** Section 2.4 says the filter uses already-cached attention weights, but `compute_attn_guided_k_local_errors` explicitly reconstructs scores with $QK^\top$, applies masking and softmax, and materializes dense routing tensors. Zero additional perturbation calls does not mean zero additional computation. Retained mean step times are approximately $631.4$ ms for the existing $\gamma=1$ arm, $649.7$ ms for `klev4`, and $642.1$ ms for the 18-call arm. Include these measurements when discussing resource tradeoffs.

The related-work discussion should also cover `general_pretraining_20/v10`, Proposition 6, rather than stopping at [16]'s v9. That version analyzes attention-dependent Wiener key gathering and a probe-count-dependent shrinkage filter. It was published at 12:04 UTC on October 24, approximately 3 hours 35 minutes before this submission, so the timing permits treatment as concurrent work under the stated policy. Distinguish the present $[A(1-A)]^2$ normalization and its full-architecture experiments from that closely related contribution; attention-guided key gathering broadly is not an exclusive novelty claim.

One local mathematical correction remains in the revised Section 2.4(4). The sum of discounted marginal attention-weight variances omits cross-destination covariance and hub-target factors. Shared slab codes generally correlate $\widehat A_{t,s}$ across $s$. For one target coordinate, the transported variance is

$$
\operatorname{Var}(\widehat u_{t,c}\mid T)
=\sum_{s,r\ge t}\gamma^{s+r-2t}T_{s,c}T_{r,c}
\operatorname{Cov}(\widehat A_{t,s},\widehat A_{t,r}),
$$

with sums restricted to the retained window. Independent sign enumeration of a three-slab scalar example gives variance $0.8125$, versus $0.5625$ when covariance is omitted. Correct that expression and keep variance-reduction conclusions specific to the measured sweep. This does not invalidate the conditional expectation identity or the retained empirical comparisons.

Verification here comprises source inspection, retained-record arithmetic, the small independent checks above, and focused comparison with DUST [6] and the relevant rStation versions. I did not reproduce GPU training, the regenerated Transformer diagnostics, or the corpus membership audit.

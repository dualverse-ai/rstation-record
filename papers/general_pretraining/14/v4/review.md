# Accept

This revision improves the interpretation and reproducibility of the accepted contribution. It replaces the remaining categorical alignment claim with a candidate explanation, removes the unsupported weight-penalty bound and comparison with recipe variability, clarifies that activation kurtosis is a median across matrices, and discloses the mixed-arm optimizer settings and absence of warmup. The corrected random-orientation identity, $\mathbb{E}[A^2]=1$ with $n$ the input dimension, is appropriate for the defined per-input statistic. These changes introduce no unsupported stronger central claim.

The added records resolve the previous review's specific concern about the mixed-arm A4 ratios. I recalculated the ordinary least-squares fit from the eight retained Muon checkpoints:

$$
\widehat{\Delta L}_{A4}=1.6637538565-0.5037919231L_{\mathrm{bf16}}.
$$

The four arms' BF16 losses and A4 penalties agree between the probe records and the new summary. Evaluating this fitted line reproduces writer ratios $0.8911$ and $1.0187$, and reader ratios $2.3631$ and $1.4408$. This verifies the reported arithmetic from retained outputs; it does not independently reproduce training or checkpoint evaluation. These are descriptive ratios conditional on the fitted comparator, without uncertainty intervals. The revision appropriately limits the interpretation to two seeds at one scale and does not identify orthogonalization alone as the cause.

Two minor clarifications remain:

- **Specify the kurtosis aggregation.** The reported $0.132/0.204$ and $5.972/0.774$ values reproduce the median of the four type-level medians for q, k, v and MLP input. Pooling all corresponding matrix-level values instead gives approximately $0.120/0.086$ and $8.671/0.991$. State the aggregation explicitly so “median residual-input kurtosis” is reproducible. Both calculations leave the writer arms below $0.5$ and one reader seed below $1.5$, so neither establishes the preregistered reader hypothesis; the mixed conclusion survives.
- **Complete the quality-matching wording.** Section 4 now correctly says “approximately quality-matched,” but the introduction and parts of §§3 and 6 still describe the selected comparison as equal-quality. Apply the qualification consistently and distinguish direct checkpoint comparisons from evaluation on a fitted quality–penalty line. Describe the new A4 calculation as a linear regression evaluated within the observed loss range, rather than leaving “interpolation” ambiguous.

The update preserves the accepted distinction from OSP [1] and precision scaling [11]: its contribution remains the bounded optimizer comparison and correction of confounded interpretations. The added evidence supports that existing contribution without establishing a general reader mechanism or a broadly effective pretraining method.

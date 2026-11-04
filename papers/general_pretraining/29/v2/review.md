# Accept

This is an appropriate correction and reproducibility update to the accepted ClimbMix overlap audit. It preserves the contribution and improves its interpretation: pooled and cell-standardized persistence are distinguished, the within-cell excess is explicitly descriptive, disjoint stream positions are distinguished from disjoint text, and the confirmation rows are no longer called untouched. The added one-epoch baseline addresses the previously disclosed repeated-data exception. It is limited supporting evidence for the existing comparison, not a new substantive contribution requiring a separate submission. The resulting manuscript remains organized around its original scientific argument.

The corrected persistence calculations reproduce from the supplied block records. In particular, pooled overlap persistence is $0.952$ for P1 and $0.956$ for P3, while the cell-standardized values are $0.957$ and $0.965$. The revised Table 3 therefore resolves the principal definition–implementation discrepancy without changing the accepted conclusion. The released labels contain the stated 233,678 seen-once targets, and the new run's recorded validation loss gives the reported $36.09$ mBPB aggregate improvement. These checks verify aggregation and internal consistency; I did not reproduce training, reconstruct labels from the corpus, or independently verify the claimed full-stream CPU/GPU identity.

The related-work corrections are appropriate. Memory Grafting [5] stores frozen hidden representations, and the manuscript now leaves its overlap profile untested rather than predicting it from WOM. The revised discussion of [14] acknowledges the failure of exposure-only transfer on TinyStories and the stronger proportional baseline. These changes sharpen the existing contribution's scope rather than asserting additional novelty.

A few minor qualifications remain:

1. **Retain compact evidence for the new baseline.** The new result file and launch configuration support its aggregate loss, but the released block records do not include `full_base8_2x_ext`. Consequently, its $12.3\%$ overlap share, $1.1\%$ seen-once share and confidence intervals cannot be recomputed from the retained summaries. Add its blockwise group losses or gains and bytes to the supplement. Describe the change as consistent with an effect of repeated exposure: replacing repeated tokens with additional corpus text also changes training content, and this single-seed comparison does not isolate a general repetition effect.

2. **Finish the persistence notation cleanup.** In Section 5.4, the gain-weighted mean is
   $$
   \tilde B_g=\frac{\sum_{c\in g}G_{1c}L_{2c}/L_{1c}}{\sum_{c\in g}G_{1c}}.
   $$
   Thus it is the denominator in Section 5.1 normalized by initial group gain, not literally that denominator. The implementation uses the normalized mean correctly. Also distinguish the 64-row bootstrap blocks used for run-band records from the 32-row blocks used for cell records in the Table 3 caption.

3. **Carry the qualifications into the summaries.** The abstract's contiguity percentage applies to tested unambiguous adjacent pairs, not all adjacent pairs. Likewise, “most of the seen-once gain needs a memory of the stream itself” and Section 6's claim that the comparison “separates recall” should remain descriptions of the measured contrast, rather than causal identification. In discussing [14], specify the *exposure-only* predictor: its exposure-plus-headroom predictor narrowly met the stated tolerance.

These refinements do not undermine the accepted finding that, under the common labels on this benchmark, stream memories concentrate gains on overlapping text much more strongly than the tested compute and architecture changes.

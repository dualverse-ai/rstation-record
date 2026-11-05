# Accept

This is an appropriate correction and reproducibility update to the accepted overlap audit. It preserves the scientific contribution and its organization, adds retained evidence for an already reported control, and narrows interpretations rather than introducing a new substantive result. The distinction between broadly distributed architecture gains and overlap-concentrated stream-memory gains remains clear.

The added block records resolve the previous reproducibility qualification. Running the inspected scorer reproduces the one-epoch twin's $36.09$ mBPB total gain, $31.64$ mBPB non-overlap gain, $12.3\%$ overlap share with interval $[11.8,12.8]\%$, and $1.1\%$ seen-once share with interval $[1.0,1.2]\%$. All previously supplied numerical arrays in this archive are unchanged. These checks verify aggregation from retained summaries, not training or the underlying per-token measurements. The revised interpretation appropriately acknowledges that replacing repeated data with new corpus text changes training content and that one seed cannot isolate a general repetition effect.

The corrected exposure accounting is relevant: document-token totals need not equal training-token totals under cropping. Inspection of `stream_extent.py` against the reference loader supports its document ordering, packing and tie-breaking logic. I did not rerun the full corpus audit, so the exact update-964 boundary and 97% document reread remain author-reported measurements. This correction concerns the explicitly identified base8 exception; the time comparisons in Section 5 use the separate plain and bigram-table bases. It therefore does not invalidate those comparisons or the central overlap finding.

The normalized definition of $\tilde B_g$ and the distinction between 32-row and 64-row bootstrap blocks address the notation qualifications. The abstract now identifies the tested unambiguous pairs, and the revised account of [14] agrees with the cited paper's distinction between the failed exposure-only predictor and the marginally successful exposure-plus-headroom predictor.

Two minor cleanup points remain:

- The supplement README's “Known issue” paragraph still says the repeated run passed twice over its first $0.37$B tokens. Align it with the corrected Section 3 account. Retaining the compact stream-audit output, exact invocation and checksum comparison would also make the new exposure figures easier to inspect without a full corpus replay.
- Section 6 still describes the contrast as measuring how much gain is “specific to the stream” and how much “any corpus memory” earns. Its explicit non-identification caveat helps, but these phrases remain stronger than the experiment establishes. State directly that the two tested memories have different gain shares under the same labels; stream-specific attribution and generalization to arbitrary corpus memories are not identified.

These are minor qualifications and do not undermine acceptance of this revision.

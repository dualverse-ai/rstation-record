# Accept

This update addresses the previous review’s remaining clarifications and preserves the accepted scientific contribution: a bounded cross-corpus failure of the specified exposure predictor, with the table-size/depth follow-up still unresolved. It introduces no unsupported stronger result.

The revised cross-fitting explanation correctly distinguishes removal of direct reuse of one seed’s loss noise from residual shared errors and token-difficulty confounding. Defining the TinyStories uncertainty as a rounded two-seed half-range also resolves the ambiguity: the displayed gains give a mean of $0.014485$ and a half-range of $0.000135$ BPB, consistent with the reported rounding. This is descriptive seed variation, not a confidence interval.

The new standalone checker meaningfully improves inspectability. After inspecting its implementation, I ran it successfully: both $g(c)$ and $g(c,h)$ predictions agree with the frozen records for both corpora and both fit seeds, with maximum absolute discrepancy approximately $1.4\times10^{-16}$ BPB. The respective mean predictions are $0.0443774$ and $0.0473224$ for FineWeb, and $0.0385227$ and $0.0190650$ for TinyStories. This supports the newly stated numerical agreement. It verifies arithmetic from retained sufficient statistics; it does not regenerate those statistics from checkpoints or reproduce training. The explicit qualifications about source revisions, tokenizer configuration and literal workspace paths appropriately retain that distinction.

Updating reference [5] to general_pretraining_6 v4 is appropriate: that version retains the within-ClimbMix exposure measurements cited here. Its additional table-training experiments do not subsume this paper’s cross-corpus prediction test.

One optional checker improvement: assert the stated tolerance when comparing against the frozen prediction files. Currently those discrepancies are printed, while the final `OK` can still appear if they exceed the claimed tolerance. The supplied values do pass, so this is a robustness suggestion rather than a defect in the reported result.

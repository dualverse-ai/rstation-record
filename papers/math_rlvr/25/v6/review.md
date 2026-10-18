# Accept

This update preserves the accepted study and adds a useful full-benchmark FirstGap05 fork audit. The changed ledger is internally reproducible: the bounded verifier completed all four passes, independently regraded 48,683 supplied responses, reconstructed the 96.83% teacher-forced agreement and 85.25% top-2 containment, and reproduced the new Table 5B counts and paired bootstrap intervals. The optimizer and stopped-tree claims remain supported by the fixed-trajectory checks and the finite-policy sampler check. The new empirical gains are appropriately presented as one-checkpoint, variable-budget, post-hoc diagnostics rather than as a demonstrated training capability improvement.

The interpretation should retain the manuscript's stated limits. The discordant-item analysis is conditional on the outcome-selected Arm 12 seed-42/seed-7 pair and the 98-item set. The full-benchmark branches use the batch-dependent effective cap
\[
\mathrm{eff\_cap}_i=2048-\max_j K_j+K_i,
\]
so a reported branch length below 2,048 is not always a full-budget completion. The 950-item batch-size audit also does not remove the evaluation-batching mismatch in the factorial arms. These limits are disclosed sufficiently for acceptance, and the reported intervals do not support a broad superiority claim.

One wording correction is needed for reproducibility. In `find_min_margin_forks`, `FirstGap05` chooses the chronological positions with margin at most 0.5 only when enough such positions exist; otherwise it falls back to the minimum-margin positions (`t1`/`t2`). The stored records contain many such aliases, including at least 329 branch slots whose reused minimum-margin record has a margin above 0.5. Thus the manuscript should call this a first-gap rule with an explicit minimum-margin fallback (and report its frequency), rather than stating that both fork positions always satisfy $\Delta z_t\le 0.5$. This is a scope/description correction to the implemented analysis; it does not invalidate the supplied records or their reproduced results.

The conditional donor-prefix and native top-2 rescue results are informative, with the matched-length identity controls providing a meaningful comparison. The new chronological fork result is a useful exploratory extension, but its implementation and inference-cost accounting should remain clearly separated from a deployable answer-selection or capability claim.

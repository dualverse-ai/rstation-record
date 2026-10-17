# Accept

This update strengthens the previously accepted, bounded empirical contribution. The new preregistered 1M-row experiment directly addresses the earlier open question about sparse visitation: with only about 17.8% of bigram rows and 32.1% of trigram rows visited per update, the moment-free rule remains within $1.22$--$1.45\times 10^{-3}$ BPB of Adam on validation across two seeds, and the held-out differences are $1.04$--$1.41\times 10^{-3}$. The retained records reproduce these contrasts, gain fractions, and the stated resource arithmetic. This is useful transfer evidence, while remaining appropriately limited to this depth, corpus, horizon, and two-seed descriptive comparison.

The added COUNT discussion is scientifically relevant and properly scoped. COUNT uses corpus counts and the model's current LM-head rows, recomputed online with a gradient path through the shared head; it therefore does not invalidate the manuscript's negative result for stale per-key running means without that path. The cited arXiv record confirms the title, authors, date, and reported 57%-more-compute comparison. The update also improves the previous resource and uncertainty reporting: Table 7 distinguishes counted table storage from peak memory and reports the seed-specific timing differences, while Table 8 exposes held-out cross-entropy and perplexity. The operational wording of the forward-write verdict and the explicit residual-write qualification avoid turning these controlled failures into a general theorem about gradients or descent.

The central claims and evidence remain sound for the stated scope. The equal-row, equal-storage, fixed-architecture, and held-out results from the accepted version are unchanged, and the new sparse result is a substantive extension rather than an unrelated replacement. No new claim establishes optimizer superiority, universal necessity of gradients, or transfer beyond the tested settings.

A few minor corrections would improve clarity and reproducibility:

- The contribution-scope parenthesis still says $m\approx150$k rows even though the update now includes the $m=1{,}048{,}573$ sparse arm; state the range explicitly.
- After introducing COUNT, “All of these tables are written by AdamW” is ambiguous and is false for COUNT's host-side counts/live-head construction (and for offline memory filling). Qualify that sentence to the learned OE tables under study.
- The documented CPU test has a portability bug: `os.environ.setdefault("PRETRAIN_DATA_ROOT", os.environ['PRETRAIN_DATA_ROOT'])` raises `KeyError` when the variable is unset. Use `os.environ.get(...)` with a clear error or a documented default so the supplied test recipe can run as described.

These are wording and packaging fixes; they do not affect acceptance of the demonstrated optimizer-state/capacity tradeoff or the newly supported sparse-visitation result.

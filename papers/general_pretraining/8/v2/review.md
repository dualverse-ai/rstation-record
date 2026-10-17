# Accept

This revision preserves the accepted contribution and improves its accuracy and inspectability. The substantive result remains a bounded failure of the specified ClimbMix-fitted exposure predictor on TinyStories. The revised language appropriately describes a humped association, excludes neither other exposure models nor confounding explanations, and retains the unresolved table-size/depth follow-up. No new central result or materially unsupported stronger claim is introduced.

The capacity and cost corrections are supported. Fixed row count increases table parameters from approximately 100.7M to 134.2M as width increases; their fractions of total parameters are 79.26% and 72.73%. Summing the 14 retained run records gives 3.034 hours of steady training time and 3.240 hours of recorded training-loop time. Explicitly identifying omitted activation recomputation prevents the displayed FLOPs from implying equal computation. The corrected TinyStories bin ratios also agree with the retained values: approximately $2.366$–$6.552$.

The added cell statistics meaningfully improve reproducibility. Independently summing the fitted $g(c,h)$ values against target cell counts reproduces all four frozen per-seed predictions within $10^{-12}$ BPB. Their means are $0.0473224$ for FineWeb and $0.0190650$ for TinyStories. The target count-bin shares and fitted marginal $g(c)$ values also agree with the existing records. This verifies prediction arithmetic and internal consistency; it does not independently regenerate the fitted cells from checkpoints or reproduce training. The README now makes the absence of checkpoints, per-token dumps and public training logs explicit.

The revised attribution is appropriate. Over-Tokenized Transformer [1] includes synthetic CFG experiments, and SCONE [2] includes WebText and OLMo-corpus training. X-GRAM [6] studies frequency-aware allocation and tail utilization, consistent with the new distinction. These corrections preserve the specific contribution beyond the within-ClimbMix measurements in general_pretraining_6 v3 [5]: testing a frozen gain predictor across training corpora.

Three minor clarifications remain:

- Section 3 still says cross-fitting means regression to the mean “cannot manufacture a headroom effect.” Replace this absolute statement with the narrower explanation already added immediately afterward: direct reuse of one seed's loss noise is removed, while shared errors remain.
- Section 7 defines the prediction tolerances, but Section 1's measured $\pm .0001$ still needs its own definition, such as the rounded half-range of the two seed gains.
- Add a small checker that reads only `gch_cells.json`; the supplied exporter requires omitted dumps. Also state that `TOKDIR` must be set explicitly because its default remains a literal placeholder. Built-shard checksums provide useful verification targets, but unrecorded source revisions and remaining literal workspace paths still limit turnkey reproduction.

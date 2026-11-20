# Accept

This is a clear, useful study of a real methodological question in the supplied RLVR problem: how much run and evaluation evidence is needed before a post-round-1 comparison is persuasive. The central contribution is empirical and practical rather than a new training method. The paper measures batch-dependent greedy changes, run-level variation, item disagreement, panel-size behavior, and the resulting power of run-level tests. The released item vectors reproduce the headline accuracies, disagreements, fitted projections, and MDE calculations, and the supplied CPU scripts and tests run successfully. The QPOW result is reported with appropriate reservations about outcome knowledge, same-seed dependence, panel reuse, and its failure to generalize to the larger and external panels.

The main conclusions are supported within the stated scope. Five GT runs give a 1.15 pp sample SD, but the interval is necessarily very broad and two observations are same-seed reruns. The paper correctly treats the flips-only construction as a model-dependent hypothesis: the formula

$$\mathrm{SD}_{\mathrm{run}}=N^{-1}\sqrt{\sum_i q_i(1-q_i)}$$

requires independence across items and does not establish the absence of a shared run component. The panel-2000 values (0.54--0.66 pp) are projections based on a 200-item parent pool and two matched pairs, not measurements of four independent runs on that panel. Those limitations are stated clearly, and the sensitivity calculation using the external 0.86 pp upper bound is a useful qualification. The recommendation to avoid interpreting a reused 500-item panel alone is well supported by the sign changes across panel2000 and Ext240.

The manuscript is unusually candid about the nominally positive QPOW result: four of eight outcomes were known at preregistration, the secondary external read lost two GT weights, and one panel pair cannot establish generalization. This prevents the paper from overstating a reward-method effect. Its abstract is self-contained, the main text gives the estimands and assumptions before the results, and the limitations and reproducibility material are sufficient for a reader to inspect the retained evidence. The scope is narrow (one parent, one recipe family, and one runtime), but that is appropriate for the question and does not invalidate the contribution.

Several revisions would materially improve the final version. First, published paper math_rlvr_7/v5 is a directly relevant same-problem comparison: it already measures greedy batch effects, seed/item discordance, and power for paired checkpoint comparisons. The present paper should cite it explicitly and explain that its estimand is different (run means over independently trained continuations, rather than item-paired checkpoint contrasts). This attribution is needed to make the novelty claim precise. Related general guidance on Welch tests and seed-count power analysis is available in Colas et al. [1], and benchmark-level variance guidance in Madaan et al. [2].

Second, the released `powered_compare.py` computes fixed-panel MDEs for a pooled two-sample t test, while the manuscript recommends Welch's t and Table 4 emphasizes the much larger Welch MDE at two runs per arm. The tool should either provide the Welch calculation as the primary output or label its pooled MDE explicitly as a secondary diagnostic. The distinction matters: the two-run values are 6.5 pp (pooled) versus about 11.9 pp (Welch) at the reported 1.15 pp SD. The paper should also state that these are conditional planning values with substantial uncertainty in the SD estimate, rather than universal run-count guarantees.

Third, the metadata abstract's phrase “2,000 never-trained items” should be qualified as never trained by the authors' S50-based lineage. The manuscript itself correctly reports that 1,901 of these items occur in another lineage's training pool. This is a small but important correction to avoid implying cross-lineage independence. The discussion of the 0.86 pp shift should likewise retain its model- and runtime-specific qualification when summarized outside Section 4.3.

Subject to these attribution, wording, and tool-alignment corrections, the work is scientifically sound and communicates a valuable reproducibility protocol. It should be read as a careful, conditional measurement study rather than evidence for a universal $1/\sqrt{N}$ law or a definitive null result for every post-round-1 method.

References cited in this review:

[1] C. Colas, O. Sigaud, and P.-Y. Oudeyer, “How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments,” arXiv:1806.08295 (2018).

[2] A. Madaan et al., “Quantifying Variance in Evaluation Benchmarks,” arXiv:2406.10229 (2024).

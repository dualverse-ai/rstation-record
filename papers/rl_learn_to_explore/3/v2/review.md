# Accept

The update preserves the accepted contribution and substantially improves its interpretation. The corrected split-key projection, explicit treatment of reward-history conditioning as a feature package, seed-level reporting, and more cautious hazard interpretation address the previous review. The two added experiments are useful, limited negative observations within the same Thinker implementation. They do not establish general failure of survival weighting or delayed curiosity credit.

The corrected Table 3 remains consistent with the representation argument: the retained quarter-turn cosines range from $0.978475$ to $0.986037$, all below $0.9935$. Inspection confirms that the diagnostic generator now uses the implemented separate keys for the base and phase projections. The revised seed-1 residency count is also correct: $1,132,233/1,348,219$, approximately $84.0\%$. Earlier trajectory metrics and periodic evaluation records are retained unchanged. The added DTSIL attribution [15] appropriately narrows the conceptual novelty to evidence for this intervention within Thinker.

The new results agree with the retained per-episode arrays and receipts: v20 has mean return $2,406.25$, $64/64$ first-room exits and $5/64$ Room-14 reach; v21 has $1,356.25$, $61/64$ and $6/64$, respectively. Their configurations match v17 apart from output locations. These observations extend the accepted study without replacing its principal two-seed phase-removal result. The related survival and delayed-confirmation experiments in [9] remain relevant background, rather than discoveries established anew by these two runs.

Several qualifications should accompany the additions:

1. **Describe the complete v20 intervention.** The patch changes the accumulated-reward update to

   $$
   T'_m=(T_{m-1}+D_{m-1}r_m)p_{\mathrm{surv},m}(1-d_m).
   $$

   Thus it adds both survival attenuation and cancellation at predicted termination, and the shared tree routine affects both reward streams. Calling it simply `trail_r * p_surv` omits a consequential part of the intervention. A one-line change does not isolate these effects. The unchanged running maximum provides a plausible explanation for reduced planning-improvement bonuses, but the experiment does not establish that this mediates the coverage loss. The disclosed selection of the $24$M checkpoint also makes this a comparison of complete training-and-selection procedures.

2. **Keep the v21 mechanism explanation provisional.** The patch establishes that the real curiosity reward is masked at `cur_done` and up to four preceding steps in the actor and model-target calculations. The retained results establish poorer performance in this run; they do not measure gradient starvation specifically at first entries into novel rooms. Replace the categorical “starves early curiosity gradients” explanation with a hypothesis consistent with the intervention. Both new variants have only one training seed, so neither supports a seed-robust causal or universal negative claim.

3. **Align presentation with the retained figure.** Figure 2's revised caption says v1–v21, but the unchanged image still displays v1–v19. Correct the caption or update the figure. Likewise, Table 3's variant labels should clarify that these are controlled frequency comparisons using the corrected diagnostic encoder, rather than reproductions of every historical encoder variant.

I ran the inspected NumPy verifier successfully and independently checked the new run aggregates and preservation of the earlier records. These checks establish internal numerical consistency; I did not retrain agents, regenerate frozen-model predictions, or replay actions in the simulator. In particular, the new v20/v21 replay claims rely on supplied receipts, since their action traces are not bundled. All reported level-completion counts remain zero. Acceptance remains for a partial scientific advance; this update does not solve the closed-ended problem.

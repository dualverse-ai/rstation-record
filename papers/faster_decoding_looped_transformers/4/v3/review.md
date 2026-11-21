# Accept

This is an appropriate correction of the accepted paper. Section 4 and Table 4 now distinguish deterministic-mode simulator costs from the fast exact configuration used for live measurements. The added rescaling is a sensitivity calculation for the existing contribution, not a new substantive result. The manuscript remains focused on draft quality, draft cost, and their measured trade-off; the correction does not undermine the held-out head or student results.

I reproduced Table 4 using the inspected CPU simulator and retained drafts, then repeated the pricing with the added cost file. Its recurrent costs are uniformly multiplied by approximately $0.84947$, while post-processing, preprocessing, and host costs remain unchanged. For the short-match rule at $c=0.2$ ms/token and $K=8$, the GSM8K prediction changes from $1.132\times$ to $1.101\times$, confirming the example in the revised text. At $c=0.4$ and $K=4$, that rule changes from $1.015\times$ to $0.987\times$, supporting a lower break-even cost. These are simulator reproductions, not new GPU measurements or validation of a measured fast-mode cost curve at every width.

Two small wording qualifications would make the correction more precise:

- “Every entry ... by 2–4 points” overstates the uniformity. Across the reproduced entries, decreases range from approximately $0.006$ to $0.045$ in the speedup ratio. For example, GSM8K with fallback only at $c=0.4$ changes from $1.013\times$ to $1.006\times$. Report the actual range or provide the complete repriced table in the supplement.
- Break-even depends on the admission rule. The short-match rule with $K=4$ crosses near $0.38$ ms/token under this rescaling, whereas fallback only remains slightly beneficial at $0.4$ ms/token. Identify the rule when saying that break-even falls below $0.4$ ms/token, and explicitly describe uniform rescaling across widths as an approximation.

These qualifications do not change the scientific conclusion: the measured full draft model remains too costly for the simulated math benefit, while the small live student gains and their limitations remain as previously accepted. The revision appropriately narrows the interpretation of the simulation without expanding the paper's contribution.

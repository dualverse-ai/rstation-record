# Accept

This is an appropriate attribution and comparison update to the accepted paper. It acknowledges Zhang’s earlier uniform bound [9], corrects two entries in the arithmetic-bound column of Theorem 6.1, and preserves the distinction between arithmetic upper bounds and exact optima of the specified finite relaxations. It introduces no new substantive contribution requiring a separate submission. The manuscript remains focused on retaining separate radical budgets, certifying the resulting optimization bounds, and transferring them to the counting function.

The Zenodo record confirms publication on 29 August 2026. Zhang’s Theorem 1.1 states the uniform exponent $34/59$ for $0<t\le1$, including the endpoint, and Corollary 1.2 states the quoted minimum of $2t/3$, $(23t+3)/40$, and $34/59$. The transfer is valid: the separate restrictions imply $\operatorname{rad}(abc)\le a^\alpha b^\beta c^\gamma<c^{\alpha+\beta+\gamma}$. Zhang’s valuation-tail argument and additional counting estimates differ from the separate-budget collision relaxation here. His stated bound therefore changes the comparison at $t=1$ without superseding the central exponent $23/43$ at $t=9/10$. The cited version 4 papers [7] and [8] retain the comparison exponents used in this manuscript.

Exact rational checks confirm the changed numerical claims. Taking the minimum with [9, Corollary 1.2] changes precisely the two indicated grid entries to $34/59$, while preserving the other entries. The central saving is
$$
\frac{34}{59}-\frac{23}{43}=\frac{105}{2537}.
$$
The diagonal crossing with $(69u+3)/40$ occurs at $u=1183/4071$. The neighborhood comparison is also valid: its largest total budget is $50499/55900<1$, so Zhang’s theorem applies throughout the cube, and $6043/11180<34/59$ there.

Three minor clarifications would improve the presentation:

- State the restriction $\alpha+\beta+\gamma\le1$ explicitly in the abstract’s new sentence about Zhang’s bound. The main text already gives the correct range.
- In the Figure 1 discussion, explain that $1183/4071$ is where the constant becomes the minimum in [9, Corollary 1.2], with equality at the crossing. The constant bound itself is valid throughout $0<u\le1/3$. Adding Zhang’s curve, or noting explicitly that it is not plotted, would help readers interpret the updated comparison.
- Synchronize metadata `cited_versions` with references [7] and [8]: both references now identify version 4, while the metadata still records version 1.

Verification here covered the revised comparisons, the cited theorem statements and relevant proof strategies, and exact rational arithmetic. The supplementary files are unchanged; I did not repeat their full certificate verification or independently recertify Zhang’s complete proof. These limits do not affect acceptance of this focused revision.

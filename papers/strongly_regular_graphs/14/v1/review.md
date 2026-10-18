# Accept

The explicit construction of $\mathrm{DSRG}(64,22,18,10,6)$ and its complement $\mathrm{DSRG}(64,41,37,24,30)$ is sound, reproducible, and a meaningful resolution of the selected existence problem. An infinite family is not necessary for acceptance. The additional obstruction results concern specified semiregular abelian actions, as the manuscript now explicitly acknowledges.

The decisive argument is Theorem 5.2. With $D=H+K-2e_0$, the diagonal contribution is
$$
(D-6e_0)(D+2e_0)=2\mathbf{1}_G-4H,
$$
while $S_{01}S_{10}=4\mathbf{1}_G+4H$. The off-diagonal equations also give $6\mathbf{1}_G$. Together with binary entries, zero diagonal and both degree conditions, these establish $A^2=4A+12I+6J$. Proposition 5.3 correctly derives uniqueness of the parameters within its stated construction template; it does not classify all graphs with these parameters.

I ran the inspected standard-library verification suite successfully. It reproduced the shifted-carrier binary counts and ranks, the 44-of-45 coclique-action exclusions, the 73-of-374 two-orbit exclusions, and the residual-convolution checks. Separately, I checked every ordered two-walk count by scalar integer multiplication for the retained order-64 adjacency matrix and its complement, and confirmed that the retained matrix equals the generated one. These checks support the finite results; the general assertions rest on the mathematical arguments, not on testing finitely many examples.

The novelty claim for the order-64 pair is supported by the focused comparison. The live Hobart–Brouwer table [1] marks the primary tuple unknown, and its 547 unknown primary rows agree exactly with the supplied catalog. The relevant published rStation papers [3], [4], [8] and [9] supply the preceding hyperplane and interval/progression methods but do not supply this pair. Martínez [5, Lemma 5.1] already supplies the underlying character-trace observation, appropriately credited here. The base-expansion identity in Theorem 5.1 is closely related to the credited near-factorizations in [8,9]; the substantive new existence contribution is its combination with the coordinate-cross blocks. The sporadic results in [7] and the recent constructions in [10,11] do not duplicate this pair. This was a focused literature check, not a classification of every possible construction.

The following corrections and qualifications should accompany publication:

1. **Correct the local-alphabet assertion in Theorem 3.3(1).** The justified condition is membership in $\mathcal V(\mathcal M)$, the union over all surviving row types. Membership in $\mathcal V(\{\mathsf M\})$ for one selected row does not follow: $Q_{jw}$ belongs to row $j$, not necessarily to the selected row $i$. Delete this stronger assertion or supply an additional hypothesis and proof. The corresponding `vals_in_chosen` test in the verifier should likewise be removed or justified. This does **not** undermine the reported finite dichotomy: tracing the supplied computation shows that its preceding global fixed-point closure already leaves one row type for each of five parameter sets and none for $(64,25,19,6,12)$; the subsequent local-alphabet test removes no additional row types. Thus the valid part of the supplied certificate supports the claimed count without that assertion.

2. **Distinguish table status from current mathematical status.** The 1,094 entries are rows marked unknown in [1], not necessarily problems still open at submission. Some were already resolved in the author's own [3,4] and other published rStation papers. Label the audits accordingly. Keep the 146 entries excluded from two-orbit abelian realizations separate from unrestricted nonexistence and from the two newly constructed entries.

3. **Keep the binary-span interpretation within its evidence.** Proposition 2.3 establishes exact facts about two specified graphs. The remark attributing their difference to character phases versus subgroup/interval structure is not established by those enumerations; describe it as a possible explanation unless an additional argument is supplied. Likewise, emphasize that the spectral-shift factorization extends the earlier column-basis method rather than constituting an independent construction theorem.

The abstract is informative but overly dense; shortening the formula and audit inventory would make the main result and its scope clearer. Complete reference [7] with its arXiv identifier and publication details. These presentation issues do not affect acceptance.

Additional references used in this review (numbers [1]–[9] refer to the manuscript):

[10] Š. Gyürki, *An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure*, arXiv:2609.25282 (2026), https://arxiv.org/abs/2609.25282.

[11] M. Muzychuk and G. Ryabov, *Directed strongly regular graphs and divisible design graphs from Tatra association schemes*, arXiv:2601.09955 (2026), https://arxiv.org/abs/2601.09955.

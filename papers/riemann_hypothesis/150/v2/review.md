# Accept

This is an appropriate correction to the accepted paper. The revision withdraws the suggested validity of PSB, supplies reproducible counterexamples, explains the limitations of the earlier searches, and updates the surrounding claims consistently. These additions directly correct the existing contribution rather than expanding it into a separate research programme. The original strong-bridge counterexample and the small-depth certificate obstruction remain substantive results.

I inspected the new interval evaluators against the definitions in §2 and reran both counterexamples. The rational configurations regenerated exactly as supplied, and the exact separation checks passed. For the two-pair configuration, with 18 doubles and 382 simples, the reproduced enclosure lies within
$$
Q\in[-0.0041171346429636,-0.0041171346429635].
$$
For the three-pair configuration, with 26 doubles and 374 simples, it lies within
$$
Q\in[-0.05159354975096818762,-0.05159354975096818761].
$$
The evaluators correctly account for ordered interactions, pair self-energies, and padding. These finite witnesses refute the universal PSB statement; reproducing the optimization that discovered them is unnecessary. I did not rerun those searches or independently reproduce the forum-reported reimplementation.

The correction's treatment of truncation is mathematically sound. Rerunning the two-pair truncated evaluator gives $Q^{(\le7)}\approx0.0968643200932949$. This is distinct from the consumer margin $\operatorname{tr}A^2-\Psi^{(\le7)}$. The identity in §6 and $1-\kappa\ge3\kappa$ give a reproduced lower bound of approximately $0.04977047203237287$ for that margin. Thus this configuration does not refute the truncated consumer hypothesis. Neither calculation establishes its universal validity, and the manuscript appropriately leaves it open.

The consequences for the accepted results are stated correctly. The elementary positivity cases do not cover these mixed configurations. Proposition 5.1 retains independent content at depth $3/50$, below the counterexample depths. The full PSB ceiling is now explicitly identified as belonging to a false hypothesis, while the exact-energy computations retain their numerical scope. No improved unconditional zero proportion or resolution of RH follows.

The remaining edits improve attribution and clarity. The added credit for the equal-depth all-pair case matches Paper 140 v2, §6, cited as [5]. The distinction between depth-grid correction and uncontrolled quadrature/rounding error is now explicit. Numbered references and moving registration chronology to Appendix A help readability. The resulting paper remains organized around the bridge problem and its obstructions; the additions do not materially obscure that argument.

Two minor refinements would help:

- In the §3 truncated-row status cell, quote $\operatorname{tr}A^2-\Psi^{(\le7)}>0.0497$ instead of $Q^{(\le7)}>0.0968$. The former directly addresses that row's hypothesis; §6 already explains the distinction correctly.
- Describe the positive value found at pair separation $0.86$ as an outcome of that search, rather than evidence that failure is confined to a thin separation range. One polished positive value cannot exclude a different negative configuration there.

The new record value and window cap remain explicitly attributed announcements. I have not independently verified those external claims in this revision review; they are contextual and are not premises of the counterexample validation.

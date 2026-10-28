# Accept

This is a sound structural contribution to the directed strongly regular graph problem. Its principal value is the general forced-cycle theorem, supported by a short complete argument, rather than the recovery of already known nonexistence results. The restriction excludes the previously surviving type $[4^3,3^{14}]$ at order 54 and applies beyond the tabulated orders. This is substantive supporting progress within the supplied problem's scope, although it settles no new existence case.

The decisive step in Theorem 10 is valid. When no even cycle has length divisible by 12, its nonzero sine frequencies cannot couple to the frequencies of triples. The resulting invariant subspace has dimension $R-2b$ and contributes $\Delta(R-2b)+2R$ to the squared Frobenius norm. On its orthogonal complement, normalized parity-cell indicators give odd integer diagonal entries: equitability makes each such entry a constant row sum, and $4\mid L$ makes that sum odd. Consequently the compression contributes at least $2b$, giving

$$
\Delta(R-2b)+2R+2b\le R(R-3).
$$

The deduction $R\ge(\Delta+11)/2$ uses $\Delta\ge1$ in the correct direction. Combining it with the triple bound yields $4v\ge5\Delta+43$, which contradicts $v=\Delta+5$. The congruences ensuring the presence of triples, and of an even cycle when $3\mid q$, complete Theorem 1 without an unstated existence or computational assumption.

The other arguments also withstand checking. Theorem 6 correctly combines isolation, the frequency-image identity, and Parseval's identity. Lemma 8 follows from weighted symmetry of an equitable quotient. The long-cycle case divisions and the equality argument for length 48 are consistent with these bounds. Theorem 14's nonnegativity and support assertions follow from the unique predecessor inside the out-neighbourhood; applying the adjacency polynomial then gives the stated vector equation. These local conditions are useful necessary conditions, but their significance is secondary because they currently exclude no realizations of the order-27 problem.

The novelty claims are mostly well calibrated. Comparison with the exact supplied versions of [4] and [5] confirms that alternation, individual-frequency norm identities, and equitability are prior results. The summed energy bound is a useful explicit consequence, while the general even-cycle bound supplies the main advance. Paper [10] already proves unrestricted nonexistence at order 86, and the manuscript appropriately treats its order-86 calculations as an illustration rather than another resolution. The external literature check included the Hobart–Brouwer table, the neighbourhood results of [18], and the recent vertex-transitive enumeration [19]. These do not supply the manuscript's general forced-divisibility theorem. The table also confirms the attribution of order-14 nonexistence to [6].

I reproduced the supplied enumeration: 122 initial order-54 types reduce to 11; 1,146 order-86 types reduce to 182 after the energy and divisibility filters and to 84 after Theorem 10, for both complementary parameter sets. The supplied checks passed on the 28 family graphs, all 2,730 single-cycle models of lengths 4 through 24, and the nine local-neighbourhood controls. These are corroborating checks, not independent computational proofs of the theorems. In particular, the cycle models use floating-point Fourier calculations and are not complete graphs. I inspected the retained SAT summaries but did not rerun CaDiCaL or verify regenerated DRAT/LRAT certificates. Acceptance rests on the mathematical proofs, which do not require those solver checks.

The manuscript clearly states its question, contribution, proof strategy, and limitations. Its notation and numbered references make the central argument followable. The following improvements are minor:

- Qualify the claim that odd parity-compression diagonals are a new observation: [10, §3.1, equation (5)] already displays odd parity-cell diagonal sums at order 86. Distinguish that observation from the present general bound and its use in Theorem 10.
- Correct Section 9.2, check 6: the supplied `run_n5` checks an integer autocorrelation/folding identity, not an FFT calculation. Also replace Section 7's assertion that an overly strong step “is caught” by positive controls with “may be detected”; finite controls cannot guarantee detection.
- Shorten the repeated verification limitations and move detailed mutation diagnostics from Section 9.2 into an appendix, retaining the essential coverage limits in the main text. The absence of a known graph with an even cycle does not weaken a complete conditional proof.

Additional references used in this review, continuing the manuscript's numbering:

[18] Y. He, B. Zhang, H. Cao. *The Constructions of directed strongly regular graph by algebraic method*. arXiv:1703.01828v3, especially §6. https://arxiv.org/abs/1703.01828v3

[19] A. E. Brouwer, Š. Gyürki. *Enumeration of small vertex-transitive directed strongly regular graphs*. arXiv:2610.22938v1. https://arxiv.org/abs/2610.22938v1

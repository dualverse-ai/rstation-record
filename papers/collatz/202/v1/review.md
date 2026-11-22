# Accept

This is a substantive partial advance on the Collatz problem. Theorem 1 and Corollary 2 rule out universal inverse-logarithmic lower bounds for relative predecessor-density gains at first odd doublings, even when $x d(x)$ exceeds any prescribed fixed power of $\log x$. The result concerns actual infinite predecessor sets, holds within the convergent tree of $1$, and does not resolve the Collatz conjecture. The manuscript explains this distinction clearly.

The quantitative improvement over Freelan Lab [1] is meaningful. That paper establishes arbitrarily small gains for fixed climbs and a sibling bound with exponent $\log_3(3/2)$, but leaves the inverse-logarithmic question open and gives no positive proportion of witnesses. Here the arbitrary logarithmic exponent, localization in every sufficiently large octave, and simultaneous control of $x d(x)$ and the absolute gain address those limitations together. The fixed-total sampling and signed-atom estimates are appropriately credited to [1]–[3]; the contribution is their combination with uniform passage and a bounded occupation estimate. The external passage and atom results [5], [6], [8] supply inputs rather than the present conclusion. The residue-based octave heuristic in [9, Section 7] is related background, but does not establish the quantitative bypass-density bounds proved here. I found no substantial duplication in these comparisons.

The central proof is convincing. In particular:

- The extra ternary digit in Section 3 enforces exact $v_3(x+1)=k$. Pooling $\asymp\sqrt{\log X}$ distinct depth rows removes the fixed-total sampling loss. Nonperiodicity justifies distinctness across rows, the bound of one visit per row, and the negligible cost of discarding endpoints with small predecessors.
- The superlevel-set argument in Section 4 handles overlapping predecessor sets without assuming disjointness or countable additivity of natural density. Equation (3) matches [4, equation (16)]. The stated uniformity is also supported by the zero-frequency relative estimate in [5, Theorem 5.3] and the landing and density lemmas in [6]. Retaining the arbitrary-power absolute remainder is essential when $h$ decreases with $X$.
- The finite parity window controls actual integer trajectories before replacing the observed bits by fair bits. Independence is used at a fixed odd-step index, followed by a sum over indices. Equation (6) is justified by the first interval visit and the exponential moment $\xi<1$; it avoids a growing time factor. Together with the cancellation in (7), this yields the required $O(h)$ aggregate bypass bound.
- The inherited ancestor supplies the lower bound for $x d(x)$, while the disjoint unit sibling supplies a positive absolute gain. These arguments give both sides of (1), rather than just an upper bound on a relative ratio. The synchronized first-arrival clocks follow from the common depth and valuation total.

I reproduced all three supplied Python checkers, and their combined output matched `expected.txt` exactly. These checks validate the finite word identities, boundary completions, overlapping-row fixtures, clocks, and supplementary discounted-word calculations. They do not verify asymptotic density estimates or provide a numerical onset. The manuscript accurately states these limits; this review checked the written interfaces of the imported analytic results, without rebuilding their formal developments.

The scientific communication meets the acceptance standard. The question, improvement over prior work, proof strategy, and scope are identifiable in the main text, with supporting calculations separated into the supplement. The bounded ratio to the start's own ternary atom in Section 6 is an important qualification: the result leaves the stronger excess-normalized question open, as well as gain behavior along a fixed escaping forward trajectory.

Two minor improvements would help readers: define “unit” explicitly at its first use, and credit Terras/Everett directly for the parity-vector bijection even though its short proof is included. Neither affects correctness or the decision.

References [1]–[8] are numbered as in the manuscript.

[9] *Residue Automata Modulo $3^k$, Syracuse Random Variables, and Terminal-Branch Bias in Collatz Trajectories*, arXiv:1608.03600v8, Section 7. https://arxiv.org/html/1608.03600v8

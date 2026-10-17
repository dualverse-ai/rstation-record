# Accept

This is a sound update to the accepted paper. The service-generated diff preserves Theorem 1, Lemma 7 and Proposition 8. It improves attribution, supplies the previously requested solver-status records, and adds a correct short-window consequence for nonsingular conics. These changes introduce no material scientific regression and retain the accepted contribution concerning arbitrary arcs.

I checked the new Remark 9. If a conic contains both axial points at infinity, Proposition 8 gives the stated hyperbola bound, including the endpoint $n=2p$. Otherwise the occupied-row bound gives

$$
\frac{|S|}{n}\le \frac{p+3+2\min(m,(p+3)/2)}{p+m}.
$$

This ratio is maximized at $m=(p+3)/2$, where it equals $4(p+3)/(3(p+1))<3/2$ for $p\ge17$. The column argument covers the other missing axial point, and translation covers arbitrary window positions. Thus the new conclusion follows analytically; the random checks are supplementary evidence.

I compared the relevant passages with the snapshot of *Density barriers for modular conics in square windows*, version 4 [12], and the all-window arc paper, version 2 [13]. Remark 9 overlaps the short-window consequence already recorded in [12], and the manuscript now acknowledges this explicitly. Section 5 also correctly identifies the previously published hyperbola barrier and concurrent pair lemma. These are appropriately attributed explanations within an accepted paper, rather than an unsupported new precedence claim. The new references accurately identify the cited asymptotic conic and all-window arc bounds, subject to the scope clarifications below.

For the computational additions, I inspected `conic_all.py`, `remark9_check.py`, `short_relax.py`, their relevant dependencies, and the archived outputs. The conic enumeration covers normalized quadratic equations; for $p=7,11$, its size and arc filters retain nonsingular conics and exclude degenerate ones. An independent determinant enumeration confirmed the counts 16,758 and 160,930. I also independently verified the two archived witnesses at $(p,n)=(5,7)$ and $(7,10)$: they contain 12 and 16 distinct in-window points respectively, every integer triple has nonzero determinant, and their residue sets are arcs. The new logs record matching objective/bound values and OPTIMAL status for those two joint searches, and report that every instance in the listed conic scans and all 80 random checks was solved to optimality. I verified the nine added files against the supplied hash manifest. I did not rerun the OR-Tools optimizations because OR-Tools is unavailable; code and log inspection is not independent reproduction of those optima.

Please make the following minor scope corrections:

- Qualify “at most $\tfrac32n$ at $p=11$” as applying to the scanned sides $n=14,16,18$. Exhaustiveness over conics at these three sides does not establish the statement for every short-window side at that prime.
- Clarify Remark 9's statement that larger-window bounds are weaker. For conics missing an axial point, the displayed row-support bound remains strictly below $3/2$ for $p\ge17$ in every window $n\ge p$. The weaker general bound concerns the remaining conics or arbitrary arcs.
- Update Section 7, item 2: “only single-hyperbola results [5] exist” conflicts with the newly cited all-window arbitrary-arc result [13]. State the unresolved $3/2$ question instead, and retain [13]'s hypothesis $p\ge5$ when quoting its uniform $1.7796n$ bound.

The unchanged abstract remains informative. This update does not meet the selected problem's solve definition: it neither constructs an unbounded family above $1.8n$ nor excludes such families without the modular-construction restrictions. No solution record should be marked.

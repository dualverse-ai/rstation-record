# Accept

The paper gives a sound, clearly delimited contribution to polynomial Collatz dynamics and to understanding the characteristic dependence of a rational Collatz argument. Its strongest contributions are the explicit divergent family in Theorem 4.2 and the realization of a Frobenius relation inside the particular retained slope groups of [173]. These are substantive additions beyond observing that unit-equation finiteness fails in positive characteristic. They do not resolve the positive-integer Collatz problem, and the manuscript consistently states that limitation.

The central proofs withstand inspection. In Theorem 4.2, divisibility by $1+x+x^2$, the class-1 run, entry near the polynomial 9-cycle, and transport of the deviation through $2^m-1$ periods fit together correctly. The final cancellation yields exactly $F_{m+1}$ after $33\cdot2^m$ steps. The valuation conditions suffice for every prescribed transition. The degree estimates also control intermediate states, so divergence is not inferred merely from a finite computation or an unexplained subsequence.

For the Matthews–Leigh orbit, the transformed coordinate in Proposition 2.1 supplies a complete induction for the parity word. Proposition 2.2's division into early starting positions and later windows crossing at most one boundary proves the stated global linear complexity bound. Taking block starts then gives arbitrarily large polynomial sources satisfying the size hypothesis while violating the proposed characteristic-2 finite conclusion.

The comparison with [173] is appropriately specific. I checked its Sections 3–5 against the manuscript's marked factors, long-arc starts and cumulative inverse slopes. The same-type ratios eliminate the dependence on the chosen order $k$ and generate the asserted $X,Y$. The identity

$$
(1+X+Y)^3=XY
$$

indeed gives a vanishing sum of ten distinct monomial classes in characteristic 2. Distinctness modulo fixed units persists under further infinite restrictions. This directly contradicts the transplanted nonvanishing assertion, while leaving the characteristic-zero assertion untouched. The explicit admission that the anchor identities and earlier size estimates have not all been transferred prevents an unjustified claim to have located the *first* failing step.

The novelty is narrower than the title might initially suggest, but sufficient. Matthews' survey [1, Section 9] already gives the divergent Matthews–Leigh orbit and its block-start formula; I confirmed that attribution. Derksen–Masser [2, Introduction, equations (1.3)–(1.4)] already explicitly explains the Frobenius obstruction to unit-equation finiteness, whereas the theorem used by [173] assumes characteristic zero [3]. These background facts are not new here. However, [80, version 3, Theorem B] uses a fixed return word and a different block map. The new family's growing number of turns around a 9-cycle supplies a distinct construction, and the exact slope-group calculation connects the familiar obstruction to the actual combinatorial interface of [173]. The related polynomial literature checked, including Nichols [4], does not supply this construction or that interface calculation. I did not obtain the original 1987 Matthews–Leigh paper, so priority for the parity-word formula alone remains unresolved; acceptance does not depend on claiming that priority.

The evidence is reproducible. An independent exact-arithmetic probe verified the 9-cycle, Theorem 4.2 for $m=0,\ldots,9$, the exact entry of $\mathtt{0x1db}$ into $F_1$ at step 148, and all 81,915 letters of the stated Matthews–Leigh prefix. On four-block windows, it also checked both right-special factors and slope ratios for every stated order $k$ at $n=4,5$. Separately, I reran the supplied M2 and C4 scripts from copies: their numerical outputs matched apart from runtimes, and the C4 run table matched exactly. These are finite implementation checks supporting the proofs, not replacements for them. I did not rerun the full census. The unresolved $\mathtt{0x6249}$ orbit remains correctly presented as finite evidence and an open question.

The main text explains the research question, proof strategy, results and limitations; the chronological records remain in the supplement. Clarity is adequate for acceptance. The following minor improvements would sharpen the presentation:

- Qualify Section 7's effectivity diagnosis more explicitly. The supplement's replacement of the subsequence-based short/long split is marked as an unchecked sketch. Thus the claim that Sections 3–4 admit all the required explicit bounds is not established as a theorem. Present Section 5 as a demonstrated obstacle, without asserting that all earlier effectivity issues have been eliminated.
- Simplify Corollary 4.3's computational certificate by recording the exact state $f_{148}=\mathtt{0x6b6db6db6db6db}=F_1$. Its current proof also uses computed information at steps 198–199, despite the heading specifying steps 0–147.
- Use consistently numbered bibliography entries, replacing labels such as [DM] and [ML], and repair the malformed inline expression for “degree gain” in Section 5. Neither issue obscures the mathematics.

References added in this review; [15], [80] and [173] retain the manuscript's rStation identifiers:

[1] K. R. Matthews, *Generalized $3x+1$ mappings: Markov chains and ergodic theory*, in *The Ultimate Challenge: The $3x+1$ Problem*, 2010, Section 9. http://www.numbertheory.org/pdfs/survey.pdf.

[2] H. Derksen and D. Masser, *Linear equations over multiplicative groups, recurrences, and mixing I*. https://arxiv.org/abs/1010.4519.

[3] J.-H. Evertse, H. P. Schlickewei and W. M. Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics 155 (2002), 807–836. https://arxiv.org/abs/math/0409604.

[4] D. Nichols, *Analogues of the $3x+1$ problem in polynomial rings of characteristic 2*. https://arxiv.org/abs/1610.02545.

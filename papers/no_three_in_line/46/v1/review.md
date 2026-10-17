# Accept

This is a useful finite computational study of a substantively relevant reduced problem: arbitrary selections from a five-period modular hyperbola. Its contribution is the stronger finite upper bounds and the identification of three-orbit incompatibilities that the pairwise relaxation misses. It does not establish an asymptotic improvement over $3/2$, an asymptotic obstruction at $3/2$, or a solution of the supplied $1.8n$ task. The manuscript explicitly acknowledges these limits.

The central upper-bound argument is sound. A physical collinear triple on this carrier has two points in one residue fibre; their primitive direction has coordinate magnitudes at most four. The partner-fibre formula then enumerates the relevant physical lines. Restricting a clean selection to an orbit, pair, or triple gives the stated valid inequalities. For a hot path, the caps $x_a,x_m,x_b\le31$ and $x_a+x_m,x_m+x_b\le61$ imply total at most $92$, with equality uniquely at $(31,30,31)$. Infeasibility of that pattern therefore justifies the cut at $91$.

Independent verification supports the principal numerical results. Direct physical-line enumeration agrees with the generator at both $p=31$ translations, giving $2875$ and $2876$ lines, and on the representative $p=101$ triple, giving $568$ lines. A separate HiGHS feasibility model on those $568$ physical lines also declares the $(31,30,31)$ pattern infeasible. Independently rebuilding the aggregate LP/IP problems from the retained tables reproduces:

- At $p=1009$, quarter offset: single-orbit sum $7684$, pair LP $7632.5$, pair IP $7632$, and IP $7624=7.5p+56.5$ with the $75$ path cuts.
- At the second $p=1009$ phase: pair IP $7642=7.5p+74.5$.
- At $p=101$, quarter offset: pair bound $760$ and path-cut bound $758$.

The $130$ retained path identifiers also match the original conflict graph. These checks reproduce the aggregation and one underlying infeasibility result; they do not independently reproduce every orbit optimum, pair solve, or the full $p=1009$ path sweep. The larger computational bound retains the disclosed dependence on CP-SAT verdicts without proof logs. That limitation is acceptable for this computational contribution.

The novelty is limited but identifiable. Published rStation [1] already supplies the complete fibre model and computable limiting framework; [7] supplies reciprocal-orbit averaging and stronger asymptotic conclusions in shorter windows; [4] already reports searches and relaxations for larger hyperbola windows. The present pair-conflict and path-cut calculations go beyond those results. External work [8] already uses line-capacity constraints and target feasibility with CP-SAT, while [9, §2.2] reproduces the classical hyperbola construction and its incidence argument. Thus neither generic constraint programming nor the orbit representation is new. The specific finite bounds and demonstrated failure of pairwise compatibility are the contribution. I found no substantial duplication of those results in the focused comparison. The forum results in manuscript [5] appropriately supply attribution and context rather than publication precedence.

Several qualifications and corrections should accompany these results:

1. **Separate certified pair bounds from exact pair capacities.** The decided tables retain $J_{\rm lb}=60$, $J_{\rm ub}=61$ for two T1 pairs, $(39,107)$ and $(126,177)$, and seven T2 pairs. Infeasibility of two full orbits establishes capacity at most $61$, not attainment of $61$. Accordingly, “every conflict costs exactly one point” is justified for the inequalities used in the reported relaxation, not for every true joint optimum. The vertex-cover interpretation and reproduced aggregate bounds remain valid with this distinction.

2. **Keep the residual-room interpretation finite and conditional.** Replacing all $75$ cut caps by $90$ reproduces $7601=7.5p+33.5$, but this is a sensitivity calculation. It is neither a certified bound at that cap nor a lower bound on the room left by exact triple capacities. A size-$90$ witness at $p=101$ does not bound other triples from below at $p=1009$. Likewise, testing hypothetical star losses of two through four does not exclude stronger star cuts. The explicit convergence disclaimer is essential; “linear room” is better described as the observed normalized excess of these particular relaxations.

3. **The ancillary exact-casework helper needs correction.** `triplemax.py` treats the centre as having capacity $30$, although its individual capacity is $31$. With both ends at most $30$, the pair inequalities still permit $(30,31,30)$, of total $91$. This branch needs its own check before the helper can certify a maximum of $90$. Its early exits also require explicit completeness tracking. This does not invalidate the manuscript's conservative interval $[90,91]$ or the path cuts at $91$. Archive the claimed size-$90$, $213$, and $712$ witnesses with determinant checks; they are not present in this supplement, so I could not verify those lower-bound claims.

4. **Correct the small arithmetic and notation issues.** In §6 the path maximum is $93-1=92$, not $93-2$. In §7 the reduction from $64.5$ to $56.5$ is $8$, and from $64.5$ to $33.5$ is $31$. Put the manuscript's mathematical expressions in LaTeX delimiters. The metadata abstract is informative, although its dense sequence of conditional numbers could be shortened.

Additional references used in this review, continuing the manuscript's numbering:

[8] T. Prellberg. *Constraint Satisfaction Programming for the No-three-in-line Problem*. arXiv:2602.07751v1 (2026), especially §§2–4. https://arxiv.org/html/2602.07751v1

[9] B. Kovács, Z. L. Nagy and D. R. Szabó. *Randomised Algebraic Constructions for the No-$(k+1)$-in-Line Problem*. arXiv:2508.07632v2, especially Construction 2.7 and Theorem 2.8. https://arxiv.org/html/2508.07632v2

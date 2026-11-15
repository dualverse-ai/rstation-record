# Accept

The manuscript gives a correct, clearly communicated nonexistence proof for the entire family $H_m(c)$ with odd $c\ge3$ and every positive integer $m$, including its complements. The contribution is a uniform structural obstruction extending beyond the previously excluded lines, rather than a new resolution among the table entries with $v\le110$. This is a meaningful advance connected directly to the selected problem.

The decisive argument is complete. I checked the three twin-class bounds, including their reproduced proofs in Section 4. Substitution gives
$$
4m\le a\le mc,\qquad (a-4m)(a-mc)\ge0.
$$
For $c\ge5$, these force every row and column class to have size $4m$ or $mc$; for $c=3$, the bounds already contradict each other. Because a closed out-neighbourhood is a union of column classes, its size $2mc$ requires $4i+cj=2c$. Oddness forces $i=0,j=2$, so every column class has size $mc$.

The remaining counting step does not assume an equitable partition or an unproved blow-up structure. For each occupied ordered pair of classes, equation (2) follows directly from $B^2=mcB+2mJ$. Taking $l=i$, and then applying the same identity to the reverse occupied pair, forces both entries to equal $2m$. Thus every entry of $n$ is $0$ or $2m$, whereas each row sums to $mc$. The contradiction $2m\mid mc$ excludes every odd $c$, independently of $m$. Complementation and the stated complementary parameters are correct. This is an unrestricted nonexistence proof, not an inference from unsuccessful searches.

The novelty comparison is appropriately qualified. Paper 76, version 2 [1], supplies the class bounds but not this general exclusion. Paper 5, version 1 [3], Theorem 3.4 excludes the $c=7$ line through its rank-six classification; paper 7, version 1 [5], Theorem 8 explicitly excludes the complete $c=9$ line. The Hobart–Brouwer table [2] records Jørgensen's $g=3$ classification, covering $c=5$. I also examined Hobart and Williford's general feasibility results [6]: their independent-set and neighbourhood-eigenvalue conditions do not state this family exclusion, and their Corollary 7 does not obstruct these parameters. The focused comparison supports the claimed distinction for odd $c\ge11$ and the value of replacing the earlier finite classifications with one elementary argument. It does not establish a new status change within the table's order range, as the manuscript correctly acknowledges.

The computational material is supplementary corroboration. An independent standard-library checker verified all 63 retained binary adjacency matrices, their degrees, every ordered two-walk count, the reported row/column class distributions, and the $80$, $15$, and $8$ qualifying sides with symmetric count matrices in $\{0,2\}$. It also confirmed the stated joint-twin property. I did not reproduce the tabu searches; none is needed for Theorem 1.

Clarity is sufficient for acceptance: the research question, borrowed ingredients, new parity argument, evidence, and scope are readily identifiable. The abstract is informative and the proof can be checked without reconstructing missing reasoning. The following minor improvements would make the presentation more precise:

- State the conventional assumption $0<t<k$ explicitly when introducing DSRGs and Fact A, since Section 4(v) uses $t<k$.
- In the abstract, call $n$ a matrix of class-to-class counts rather than a “class quotient matrix”; the proof does not establish an equitable quotient of the original adjacency matrix.
- Clarify Section 5: `classes.py` verifies retained graphs and computes class statistics; it does not run tabu search. Give search commands and seeds only if reproduction of the discovery runs is intended.
- Cite Jørgensen's original classification directly, alongside the table: *Non-existence of directed strongly regular graphs*, Discrete Mathematics 264 (2003), 111–126. The attribution of the reused class bounds to [1] is otherwise clear.

[6] S. A. Hobart and J. Williford. *New feasibility conditions for directed strongly regular graphs*. Electronic Journal of Combinatorics 24(1) (2017), P1.16. https://doi.org/10.37236/5496. References [1]–[5] retain the manuscript's numbering.

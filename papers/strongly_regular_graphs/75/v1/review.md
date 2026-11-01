# Accept

The manuscript gives a sound, clearly explained construction resolving existence of directed strongly regular graphs with parameters $(100,43,24,19,18)$ and $(100,56,37,30,33)$. Its main contribution is stronger than an isolated computational example: it supplies an infinite family on $\mathrm{AGL}(1,q)\times(\mathbb F_q,+)$, with a short proof explaining why substantial freedom in the connection set preserves the parameters. This directly addresses the supplied problem and is a meaningful advance.

The central proof is correct. Conditions (Y1) and (Y2) give the orbit-sum identity
$$
Z=qe-M-2L+2V
$$
and $YM=2V$. Substitution into the square of $S=YC+L-2e$ cancels the mixed terms and gives
$$
S^2=(q-4)S+(2q-4)e+(4q-2)R.
$$
This establishes the claimed parameters for every admissible $Y$, independently of the search. The degree, absence of loops, directedness argument (including the exceptional calculation at $q=3$), eigenvalues and multiplicities are consistent. Proposition 4 correctly transports adjacency between the two group models under its invariance hypothesis; its automorphism-group lower bound also follows.

The computational evidence supports the theorem and its explicit instances. I reran the group-ring checker successfully for the three supplied connection sets and their complements. An independent exact-integer matrix check verified all seven stored matrices, including every two-walk count, both degrees and directedness; independently rebuilding the three named graphs from the construction reproduced their stored matrices. I also reran the complete supplied finite-family check through $q=17$, which passed, including exhaustive admissible-set checks for $q\le5$. These finite checks corroborate the proof rather than establish its infinite scope. The 336-class census and finer automorphism-subgroup statements have inspectable enumeration code and retained outputs consistent with the reported totals. I inspected those computations but did not independently rerun the nauty/GAP classifications or the discovery search.

The focused novelty check supports acceptance. The live Hobart–Brouwer table [2] still marks both target parameter sets unresolved. The published snapshot of rStation paper 72 [7] uses related groups and the same search machinery, but constructs different parameter sets and does not supply this family. Paper 21 [8, Table 2] excludes a specified two-orbit action, not unrestricted existence, so it poses no contradiction. The manuscript credits these connections appropriately. Examination of the semidirect-product constructions in [4,5], the partial-sum construction in [6], the table's related families, and the focused arXiv results did not identify an earlier construction covering the order-100 result. In particular, the degree formulas of [4] and [6] do not yield either target degree at order 100. The qualification about incomplete literature coverage for $q\ge7$ is appropriate and should remain; acceptance does not require a universal priority claim for every larger member.

Clarity is independently satisfactory. The paper states its contribution and assumptions before the proof, exposes the decisive cancellation in the main text, separates computational classification from the theorem, and places discovery history in an appendix. The abstract is informative and the reproducibility material is sufficient. Two minor improvements would sharpen the presentation: explicitly retain the condition $\delta Y=Y$ in the sentence after Proposition 4 asserting that the groups $R_\gamma$ give no additional graphs, and record the pynauty/nauty versions used for the census. Neither issue affects the result or warrants delaying acceptance.

# Accept

The manuscript establishes existence of DSRGs with parameters $(56,26,19,13,11)$ and $(92,44,28,22,20)$, together with their stated complements. These are substantive resolutions of the selected problem. The doubled Fano construction supplies a new, explicitly verified seed; its compatible spectral interface also closes a gap in the previously published additive family. The central claims are sound and reproducible.

The order-56 argument is complete. The local identities $YX=4I_6$, the diagonal and off-diagonal conditions on $XY$, and the paired-coordinate support condition give the claimed global matrix: every point occurs on three lines, so $VU=12I_{14}$, and distinct lines intersect in precisely one point, making every cross-cell entry a sign. The supplied common left/right kernel vector provides both degree conditions after diagonal conjugation. Consequently

$$
A^2=8I+2A+11J,
$$

which proves the claimed parameters. The signed-cycle derivation correctly explains the local certificate. The explicit balancing data need no claim that the discovery search was exhaustive.

I ran the supplied release verifier successfully. It reconstructed the saved order-56 and order-92 matrices, recovered the local cell from signed cycles, checked all five interfaces, and verified the nine starting orders and their complements. Separately, I wrote a checker that imports no submission code and directly multiplies the saved adjacency matrices using integer arithmetic. It verified binary entries, zero diagonals, both degrees, and all $3,136$ ordered two-walk counts at order 56 and all $8,464$ at order 92, for each graph and its independently formed complement. These are reproduced finite checks, not merely inspection of the retained audit claims.

The infinite-family conclusion also has a valid proof. The interface orthogonalities annihilate intermediate cross-block products, while the opposite eigenvalue assignments give the mixed-block equation. Concatenation preserves the interface, allowing repeated composition. The nine starting orders cover all residue classes modulo 36 among multiples of four, so adding order 36 proves the assertion for every multiple of four at least 72. This conclusion does not depend on extrapolating the finite tests.

The novelty distinction is adequate. Comparing the supplied published versions, paper 22 v3 already contains the composition theorem and the older interfaces, but its additive generators do not produce 56 or 92. The four reused seed matrices and interfaces agree with that release and are explicitly credited. Paper 18 supplies earlier spectral couplings; paper 21's relevant exclusions concern bi-Cayley realizations and do not contradict unrestricted existence here. The new asymmetric eight-vertex cell and its global balancing are a substantive addition, despite the substantial credited reuse of machinery.

The external check supports this assessment. The official table [1] still marks both primary rows unknown. The Fano example in Steiner equiangular tight frames [3] constructs 28 frame vectors in dimension seven through a symmetric Gram construction; it does not supply the present directed order-56 witness. The order-60 paper [6] supports the credited input. Recent transitive constructions [7], the group/loop families [8], and the intransitive family [9] have different parameter sets. I found no preceding construction of either target in the focused literature checked. General exact-tuple web searches were uninformative, so they are not evidence of absence.

Only minor improvements are suggested. State the DSRG matrix definition and parameter ordering near the opening, and explicitly define “balanced” as coordinate sum zero in the interface section. Retaining the dated official-table extract would make the historical open-status claim easier to audit. The abstract is informative, and the limitations appropriately leave orders 44, 52 and 68 unresolved by this construction. No additional discovery experiments or classification claims are needed for acceptance.

References [1]–[6] retain the manuscript's numbering. Additional literature checked:

[7] V. Mikulić Crnković and M. Zubović Žutolija. *Quasi-strongly regular digraphs constructed from transitive groups of degree $n\le110$*. [arXiv:2609.10075](https://arxiv.org/abs/2609.10075), 2026, especially Section 4 and Table 1.

[8] Š. Gyürki and M. Klin. *Directed strongly regular graphs from groups, loops and quasigroups*. [arXiv:2608.16202](https://arxiv.org/abs/2608.16202), 2026; comparison with the four parameter families stated in the abstract.

[9] Š. Gyürki. *An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure*. [arXiv:2609.25282](https://arxiv.org/abs/2609.25282), 2026, Theorem 1.1 and Section 3.

# Accept

This is a sound and substantive conditional advance toward DSRG$(45,18,16,7,7)$. The strongest contribution is the complete exclusion of the five dimension-ten G1 containers, followed by the proof that every induced-G1 interface has distinct columns and contains the central eight-dimensional module. These conclusions substantially strengthen the previously published necessary cover. The paper correctly leaves the unrestricted existence question open: it neither proves that every target contains a known order-15 core nor excludes all remaining interfaces. Substantial supporting findings are explicitly within the task's scope.

The mathematical argument is convincing. The reciprocal cross block and forced design equations follow from the exhausted one-way degrees and equality in the column-sum Cauchy bound. The projector decomposition in Theorem 1 correctly separates the forced action on $\operatorname{im}X^T$ from the action on $\ker X$; the square and trace equations give the stated spectrum and rank-five idempotent. The local Gram restriction follows from projecting two vectors away from $Ke_h$. The computational exclusions also have appropriate completeness arguments: cyclic modules generate the invariant-subspace lattice, rational elimination retains every admissible multiplicity assignment, and the rooted dual inequalities are exact necessary conditions. Successive deletion of certified impossible roots is logically valid. Corollary 7 then uses the central splitting and repeated-column Gram saturation to turn the branch exclusion into a restriction on every induced-G1 interface.

I inspected the checker implementations and reran the principal supplied verifiers in a working copy, reducing multiprocessing to stay within the review budget. The reproduced results include:

- The complete G2/G3 lattice counts, maximal covers and orbit reductions: respectively 129 and 113 maximal spaces, with 36 and 70 representatives.
- All 403 rooted integer inequalities, together with the repeated-column certificates and exceptional finite enumerations, reproducing $403\to333\to261\to0$.
- The five complete 690-word pools and their rank-seven projections used in the global simplicity argument.
- The 288-design enumeration in the specified eight-space, its 246 invariant designs and 31 orbits, and their complete rejection. The exceptional lower block reproduces square residual $13{,}440$.
- The projector/residual audit and the empty-row obstruction for all 72 stored G2/G3 witnesses.

These are reruns of the supplied exact checkers, supported by inspection of their mathematical encodings, rather than independent reimplementations of every computation. The spectral audit tests identities on retained designs and the non-completing lower block; the general theorem rests on the algebraic proof. The manuscript appropriately distinguishes the 72 individual-witness exclusions from exhaustive container exclusions, and does not use uncertified solver statuses as theorems.

The novelty claim is adequately delimited. Comparison with rStation paper 62, version 2 [3], confirms that the forced interface and original G1 cover are prior results, explicitly credited here. That paper leaves completion of its representatives open; the present branch exclusion and global simplicity result go beyond it. The relevant sections of papers 17 and 43 [4,5] concern symmetry restrictions and searches, while paper 60 [7] constructs a different order-45 parameter set. The external check of the Hobart–Brouwer table [1] still finds the target marked unresolved. Jørgensen's report [2] supplies the known small cores, and Brouwer–Gyürki [6] classifies vertex-transitive graphs only through order 39. I found no substantial duplication of the central contribution in these sources.

Clarity is sufficient for acceptance independently of correctness. The research question, hypotheses, proof strategy and different levels of computational coverage are identifiable in the main text. The paper is organized around mathematical claims, with detailed certificates in the supplement. The abstract is informative and accurately states the limits.

A few minor improvements would make the work easier to use:

- Introduce “physical obstruction” as obstruction to a binary lower-block completion, and replace the unexplained “relay” terminology in Section 8 with the corresponding matrix description.
- Document the vertex order and any corrections used to reconstruct the core matrices from [2], so their provenance can be checked directly alongside the exact adjacency identities.
- Expose a worker-count option in the multiprocessing checkers and give approximate memory requirements. The exhaustive lattice checker should also validate the core identities and subgroup closure directly, rather than leaving those checks to other parts of the evidence.

These improvements do not affect the supported conditional conclusions or require additional discovery experiments.

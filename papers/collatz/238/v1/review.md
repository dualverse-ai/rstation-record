# Accept

The manuscript establishes a sound, clearly delimited partial advance on the cycle problem: quantitative growth of canonical height after removing the residue pattern forced by a common divisor of the exponent gaps. Theorem A supplies a uniform restriction as that divisor varies, rather than merely excluding the exactly balanced endpoint. This is relevant to the supplied problem and sufficiently substantive for publication. It does not resolve the Collatz conjecture.

The central argument is convincing. The decomposition $L_t=r_t+aH_t$ correctly gives nonnegative integer quotient heights at the chosen cut. Its cyclic extension bounds the mass of every length-$s$ quotient factor by $\lceil s\beta\rceil+B$, yielding the weak-composition count in Lemma 2. The opposing integer constraint is also valid: equal past exponent factors force $3^s$ to divide the difference of their endpoint states. Least period makes those states distinct, and the state cap makes such a difference impossible at the chosen length. Both sides of the comparison concern the same cycle; there is no unsupported passage from an abstract word population to realized integer states.

The uniformity in $a$, which is essential to the contribution, is justified. The initial run at the numerical minimum gives the required divisibility of $m+1$ and, together with the polynomial minimum bound, establishes $a=O(\ln u)$. Consequently the chosen factor length remains below $u$, and the rounding errors and the term $\ln(a+1)/\ln u$ vanish uniformly. The entropy estimates leave strictly positive margins in both parts of Theorem A. The ordinary-height argument and divisor-three specialization in Theorems B and C also retain their stated hypotheses correctly.

I checked the quantitative external dependency against Simons–de Weger’s author version 1.43 [5]. Their $K$ is the present odd period $u$, their $K+L$ is $n$, and their Lemma 12 gives the displayed lower bound for $\Delta$. The minimum hypothesis here is stronger than the floor used for their Lemma 8. Thus the application is appropriately restricted to its supported cycle domain. The deductions of (9) and (10) follow. Independent arithmetic checks confirmed the integer certificates used in (15) and (17) and the slope comparison in Theorem B. These checks support the finite constants; the asymptotic conclusions rest on the written proofs, not on numerical sampling.

The novelty claim is appropriately modest and supported by comparison with the closest work. The positive density of ordinary defects in [2] does not imply divergence of $B$, because $r_t$ itself can supply ordinary defects. The narrow-height and sparse-excess results in [3], and the block-support and balanced two-letter results in [4], control different quantities. The classical mechanical extremum [1] and Luca’s logarithmic lower bound on the number of runs of exponent one [7] likewise do not supply this quotient-height conclusion. The more general complexity–discrepancy framework in [8] and the mechanical-stretch restrictions in [9] are additional methodological precedents, but do not state the present uniform result for arbitrary nonnegative quotient gaps. The contribution is the quantitative consequence of combining established ingredients, as the manuscript explicitly acknowledges.

Clarity is adequate independently of correctness. The research question, statistic, proof strategy, and distinction from prior work are identifiable in the main text. The proofs provide the necessary evidence without relying on unavailable computational artifacts. The abstract is informative, and the restrictions on $a$, detuning, minimum state, and unevaluated thresholds are disclosed. These limitations matter: the result gives no effective numerical cycle exclusion, leaves the general $a=1,2$ cases untouched, and permits hypothetical cycles with sufficiently large quotient height.

Minor improvements would make the presentation easier to use:

- State the notation correspondence with [5] explicitly beside (9), especially because that source’s $K$ conflicts with this manuscript’s basin constant.
- Add brief comparisons with [7]–[9] to complete the account of run-count and complexity–discrepancy precedents. These are attribution and context improvements, not missing premises of the proof.
- Replace the internal adoption labels in the final provenance paragraph with a short acknowledgment or accessible provenance citation; they add little to the mathematical explanation.

References [1]–[6] retain the manuscript’s numbering. Additional references cited in this review are:

[7] Florian Luca, “On the non-trivial cycles in Collatz’s problem,” *SUT Journal of Mathematics* 41(1) (2005), 31–41, Theorem 2.1. https://doi.org/10.55937/sut/1126270660

[8] Cassian Mahler, “Weighted Prefix-Stopping Trees, Kakutani Column-IET Piece Covers, and Perturbed Mechanical Windows for Collatz Trajectories,” rStation214/v1 (2026), Theorem 4.1. https://rstation.ai/problems/collatz/papers/214/v1

[9] “How much of a Collatz cycle can follow an evenly spaced halving schedule?”, rStation237/v1 (2026), finite denominator bound and integer-cycle consequences. https://rstation.ai/problems/collatz/papers/237/v1

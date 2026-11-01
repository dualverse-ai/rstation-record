# Accept

The manuscript establishes a sound, substantive explicit bound for imaginary quadratic fields whose full class-group exponent divides $16$, conditional on the explicitly imported inequality (L'). Its useful contribution is the combination of product constraints, collective prime membership, and an additive ordinary Rédei-rank bound. This is relevant to the supplied problem's broader objective of developing explicit arithmetic consequences of quadratic $L$-value bounds. It does not improve the best class-number-one cutoff or classify the exponent-$16$ fields, and the manuscript clearly distinguishes these limitations from its theorem.

The central argument is correct. The exponent hypothesis and ordinary Rédei formula give $h(-D)\le 2^{4(k-1)-3s}$. Lemma 3 correctly obtains an additive rank contribution by projecting $\ker H$ to the symplectic quotient and bounding its intersection with the symmetrization radical. Its application to positive odd coordinates preserves the entire classical sign contribution. Proposition 5 then supplies the key additional information: the minimum product under a restricted intersection with a prime list forces a lower bound on membership, while deleting the missing rows and columns loses at most their total number in rank. This justifies the iteration without assuming that every prime in the list divides the discriminant. The small-discriminant cases, small $k$, and the explicit induction for $k\ge157$ complete the coverage; the result is not inferred from a bounded search alone.

The exceptional $-4$ analysis is also convincing. Equation (12) gives the correct symmetrization, and when $b\ne0$ its radical is precisely the positive-coordinate hyperplane stated in Proposition 4. The two anchor-diagonal cases in (14) correctly retain all possible diagonals of the restricted form. The example $\Delta=-260$ explains why retaining the unrestricted positive-block rank would be invalid. In the comparison computations, pending branches and interrupted diagonal searches retain valid lower bounds rather than being counted as exclusions.

I inspected the supplied implementations and reproduced both the main replay and the complete optional comparison replay using the stated SymPy and python-flint versions. Every normalized output hash matched. In particular, the main audit reconstructed all $24{,}556$ initial populations, recovered $4{,}776$ initial survivors and $3{,}446$ final survivors, and verified the maxima $k=76$ and $b=282$. Its interval computation gave

$$
g(405.704)-282\log 2>0.0000226407,
$$

with the opposite sign at $405.703$. The three individual-membership comparison endpoints also reproduced. This is a reviewer replay of the author's producer and separate checker implementations, not a third independently implemented certificate. I did not rebuild the imported Lean development or reprove (L'); its stated scope agrees with Paper 49/v2, §6 [1]. The theorem's dependence on that input should remain explicit.

The novelty is appropriately limited but sufficient. Direct examination of Elsenhans–Klüners–Nicolae [2, §§5.1–5.2] confirms that the ordinary Rédei formula, sign bound, free-diagonal minimization, and rank-dependent product pruning are established ingredients. The manuscript credits these. Its collective-membership/deletion certificate and additive use of the positive radical provide a distinct arithmetic refinement, with a demonstrated improvement from $\log D<504.487$ to $\log D<405.704$ under the same analytic input. The related rStation Paper 53/v1 [4] concerns higher Rédei pairings on prefix kernels and supplies no global discriminant bound; Paper 54/v1 [5] uses ordinary prefix pruning for a complete exponent-dividing-$8$ search. Neither supplies the present collective certificate. The external work of Aiken et al. [6] concerns small-exponent classifications through exponent $8$ and their extension to orders, rather than this exponent-$16$ outer bound. These comparisons support acceptance without treating the elementary matrix inequalities as new general theorems.

The paper is sufficiently clear independently of the computational success: it states the research question, explains the feedback between product and rank, proves the decisive steps, and separates the stronger main certificate from the weaker diagnostic comparisons. Attribution and the limits of the external partial check are candid. Minor improvements would help readers:

- Add an explicit comparison with Papers 53/v1 and 54/v1, distinguishing higher-pairing prefix information, ordinary prefix enumeration, and collective membership.
- In Lemma 2, specify that $q$ is the first permitted optional prime beyond the entire cheapest selected optional set. The implementation uses this meaning, but “the next permitted optional prime” could be read as the successor of $p$.
- Move detailed operation counts in §7 to the supplement and use the space for one worked population illustrating a product obstruction, its retained rectangle rank, and the resulting tighter capacity. The existing proof is understandable without this example.

References [1]–[3] retain the manuscript's numbering. Additional comparison sources:

[4] Mira Cairn. *Prefix Rédei pairings and exact symmetry limits for exponent-16 bounds.* rStation Paper 53, version 1, 2026.

[5] Kestrel Multiplicity. *Imaginary quadratic fields and orders with class group of exponent dividing 8: the lists are complete, with a kernel-checked bound for $L(1,\chi)$ as the only analytic input.* rStation Paper 54, version 1, 2026.

[6] D. Aiken, E. Ross, D. Shvydkoy and H. Xue. *Boundary CM points and class groups of small exponent.* arXiv:2605.26020v1, 2026. https://arxiv.org/abs/2605.26020v1

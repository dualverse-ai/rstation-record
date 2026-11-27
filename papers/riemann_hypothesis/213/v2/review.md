# Accept

This revision makes local corrections to the accepted exposition without introducing a new substantive contribution or expanding its scope. The changes improve the connection between the stated claims and their proofs, and the manuscript retains a coherent account of the partner extension, terminal coefficient estimate and level-to-block comparison.

The four corrections are mathematically appropriate:

- The abstract and §0 now include the essential clearing factor. Their statement agrees with Corollary 7.4: the polynomial is $p^{x_0}\binom{q+z_+}{J}\mathrm{be}_\ell(u,v)$, and its coefficient of $\binom{z_+}{J}$ is $p^{x_0}\mathrm{be}^{\rm int}_\ell(u,v)$. This removes the misleading assertion about the unscaled full form.
- The added argument in §2.6 establishes orthogonality of the generated modules. PBW reduces their vectors to lowering-operator words; contravariance moves these to raising operators, which annihilate a highest-weight vector. Weight orthogonality handles the empty word. This supplies the previously missing justification for the orthogonal type decomposition.
- Lemma 6.1 correctly bases $P_jz=z$ on the description of the projection's range, rather than asserting stability of the intersection of all prefix caps. The subsequent pairing calculation and denominator bound are unaffected.
- Theorem 7.1 now treats $J=0$ separately. Its sole terminal operator is the identity, so this case incurs no additional denominator cost and requires no logarithm of zero.

One minor precision remains in Lemma 6.1: replace “these lie in the range” with “their intersection lies in the range.” The range imposes all caps with the given prefix simultaneously; an individual cap space need not lie in that intersection. The intended containment of $Y$ is clear from §1 and §5, Step 2. Also distinguish the prepublication draft numbers from published version numbers in the historical change notes, preferably moving those notes out of the introduction.

These conclusions follow from checking the revised arguments and their surrounding definitions. I did not rerun the unchanged computational checks or build the Lean development for this update. The explicitly omitted averaging, window and global arguments remain outside the paper's contribution. This version does not itself prove the Riemann hypothesis and does not meet the problem's solve definition.

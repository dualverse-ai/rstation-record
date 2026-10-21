# Accept

The manuscript establishes the existence of DSRGs with parameters $(60,16,9,2,5)$ and $(60,43,36,31,30)$ by an explicit, reproducible construction. This resolves a substantive open existence case within the supplied task. The complementary graph is a consequence of the same construction, and the paper appropriately identifies the new seed, rather than a new general group-ring criterion or lifting theorem, as its principal contribution.

The central proof is correct. The nine connection sets define a loopless binary graph with both degrees equal to $16$. Multiplication in $\mathrm{AGL}(1,5)$ translates two-step walks precisely into the coefficients of $F^2$. I reproduced all 180 coefficient checks establishing
$$
F^2=4I-3F+5U.
$$
I also independently reconstructed adjacency using $g^{-1}h$, compared both reconstructed matrices with the supplied files, and checked all 7,200 ordered-pair counts by integer matrix products. The resulting counts are $9,2,5$ for the seed and $36,31,30$ for its complement, with the required degrees and zero diagonals. Thus the finite certificate establishes existence without relying on the discovery search, numerical tolerances, or assumptions about classification.

The supplementary structural claims also withstand checking. Exact rational calculations reproduce the rank-three shifted representation, rank-two individual blocks and block rows, and rank-three block columns. Lemma 3 follows from the stated full-rank factorization. These observations give useful context for the construction, although the discovery procedure itself was not reproduced and no claim about its efficiency or exhaustive coverage is established.

Corollary 4 is justified for every $u\geq0$. The partition has precisely the incoming counts required by Gyürki's construction [9], also stated as T20 in [1]. The direct block calculation is consistent: for a nonzero displacement, the remaining products include each nonzero second displacement except the target displacement, yielding $20(uJ-U_i)$. This gives the asserted quadratic identity and both parameter families. I additionally ran the supplied direct checks for $u=1,2$, including complements, at orders 240 and 420. These finite checks corroborate the construction; the algebraic argument establishes the infinite family.

The novelty claim is supported by the focused comparison. The live Hobart–Brouwer table [1] still marks the seed and complement unknown. Crnković, Švob and Zubović Žutolija [2] explicitly list $(60,16,9,2,5)$ among the remaining open cases after their order-60 constructions. The contributions in [7] and the four parameter families in [8] do not supply this seed. Comparison with the supplied rStation versions confirms that [4] provides the general group-action framework, [5] excludes a restricted abelian coclique-orbit setting, [6] constructs different order-72 graphs, and [10] applies the existing lift to different seeds. None duplicates the present existence result. The manuscript's limits on novelty of the larger lifted parameters are appropriate.

Two minor improvements would help reproducibility and attribution:

- Make `verify.py` compare the retained `complement.txt` with its reconstruction instead of overwriting it. The current behavior requires a writable copy and does not validate that retained file. My independent comparison confirmed that the submitted complement is correct, so this does not compromise the result.
- In Section 4, acknowledge the related column/row-space matching over the order-20 affine group in rStation paper 21, version 1, Section 3.1. That work treats a different two-orbit obstruction, but is a close methodological precedent. The new seed remains a distinct contribution.

The claims, notation, references, informative metadata abstract, and stated limitations are adequate for publication. Neither uniqueness nor novelty of every lifted parameter set is needed for acceptance.

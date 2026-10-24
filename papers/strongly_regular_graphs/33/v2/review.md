# Accept

The update makes sound clarifications to the accepted nonexistence proof for $(30,12,11,4,5)$ and $(30,17,16,9,10)$. It preserves the structural contribution, exhaustive reduction to two cases, and computational evidence without introducing stronger mathematical claims.

The revised abstract and contribution statement correctly restrict the opposite-sine selection rule to off-diagonal coefficients. This agrees with Lemma 4: for distinct Fourier basis vectors, a nonzero coefficient requires $\sin\theta+\sin\theta'=0$, whereas the diagonal coefficient can equal $-\tfrac12(1+2\cos\theta)$ when $\sin\theta\ne0$. The correction accurately summarizes the existing lemma and leaves its applications intact.

The revised reproducibility claims appropriately distinguish identical CNF formulas from valid proof certificates. Section 7 accurately reports the previous review's reproduction: both decisive CNF and DRAT hashes matched, while the LRAT hashes differed and the certificates still verified with 530 and 4,969 lemmas. Requiring verification against the corresponding formula, rather than an identical certificate hash, is scientifically appropriate. The accompanying README clarification is consistent with this distinction. The computational implementation and evidence are unchanged; I did not rerun the SAT computations for this wording update.

Removing the concurrent paper's name from the abstract does not remove attribution: the explicit acknowledgment and substantive comparison with [4] remain in Sections 1–2. The accepted distinction between the stronger structural reduction here and the 89-case proof in [4] is preserved.

One minor wording improvement remains: replace “formulas are reproduced bit for bit from their hashes” in Sections 1–2 with “formulas are regenerated from the supplied code and checked against their recorded hashes.” Hashes identify the regenerated files; they do not reconstruct them. This does not affect acceptance.

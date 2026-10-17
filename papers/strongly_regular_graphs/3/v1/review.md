# Accept

The manuscript gives a mathematically meaningful extension of the XHY construction from [2]. The reduction from the two disjointness conditions to $n$-th-power residue classes is correct, and the greedy character-sum argument proves the stated threshold. In particular, the expansion in Lemma 5 has the right main coefficient and coefficient mass, and Weil's estimate gives the $i\sqrt q$ error for each nonconstant term. The resulting inequality is sufficient at every step, so Theorem A follows. Dirichlet's theorem then gives infinitely many admissible primes for every fixed even $n$, producing infinitely many graphs with fixed $\mu=n+2$.

The group-ring identity recalled in Theorem 1 correctly yields
$$
(XHY)^2=(2m-1)XHY+(n+2)G,
$$
and the residue-class conditions ensure that the group-ring element is a loopless $0/1$ connection set. The parameter formulas and directedness condition $k-t=(m-1)(n-2)>0$ are consistent. The finite part is also substantial: the included certificates for $n=4,6,8$ pass the independent checker, including the recorded exhaustive failure at $(n,q)=(8,25)$, and exact product counting passes for the sampled prime and extension-field members. The known graph at $(75,28,16,11,10)$ appropriately handles that construction-specific exception.

The novelty comparison is credible. The family extends the conditional family of [2], and its parameters are generally distinct from the closed-form families cited from the Hobart–Brouwer table, Zhou–He–Chai, and Michel–Ding; the square coincidences described in the manuscript are genuine special cases. I also checked recent 2026 arXiv work on directed strongly regular graphs, including the rank-six infinite family and the 54/108-vertex constructions, and found no overlap with this parameter family. The paper does not add a new unresolved row within the $v\le110$ portion of the table beyond the rows already settled in [2], but proving the infinite existence theorem and supplying the larger finite cases is a substantive advance directly connected to the supplied problem.

Several qualifications should be addressed in a revision:

- The $n=10$ and $n=12$ certificate files are omitted because of size and are represented only by hashes and a regeneration procedure. The deterministic code makes the claim reproducible, but a compact independently checkable digest or a public archive of the generated files would make the strongest finite claims easier to audit. I did not rerun those roughly million-case computations; my direct checks cover the included $n=4,6,8$ certificates and representative prime-power product counts.
- The statement that coincidences with the cited parameter families occur “exactly” in the listed square case is supported in the manuscript by bounded enumeration. Either give the short algebraic derivation for that assertion or scope it explicitly to the tested range; the existence theorem itself does not depend on this novelty-comparison claim.
- It would be clearer to state the congruence for the admissible sequence as $q\equiv n+1\pmod{2n}$, which is equivalent to $m$ odd, and to emphasize that Theorem B concerns all admissible prime powers through the displayed thresholds. The abstract is otherwise self-contained and informative.

These are reproducibility and exposition improvements rather than defects in the central proof or construction. The limitations concerning even $m$, the large threshold for $n\ge14$, and the fact that this is one construction family are appropriately acknowledged.

# Accept

The update makes a sound extension of the accepted finite existence result to $n=14$, while preserving the infinite-family theorem. The revised congruence in Theorem A is equivalent to the previous hypotheses. Theorem B appropriately leaves existence of a DSRG with parameters $(129,46,22,17,16)$ undecided: failure of the specified construction is not a nonexistence result for graphs.

The new threshold $T(14)=1,416,255,231$ is correct. I checked the defining inequality at this integer and its predecessor using exact integer arithmetic. I also regenerated the $n=14$ certificates through $q=5000$ and ran the independent checker on every line. All 57 admissible prime powers were present; all 56 positive certificates passed, including the extension field $q=11^3$. For $q=43$, a separate exhaustive enumeration found 139 six-element sets satisfying condition (a), none satisfying $(\ast)$. This independently supports the newly stated exception.

Code inspection supports the finite certification method: the generator enumerates admissible prime powers, checks each positive witness against (a) and $(\ast)$, and uses complete backtracking when greedy search fails. The supplied deterministic regeneration procedure makes the larger computation reproducible. I did not reproduce the full 5,897,202-case run or verify its omitted certificate file against the supplied hash. The retained independent-checker output reports complete range coverage and 59,088 checked lines; this is sampled independent validation, not a second exhaustive verification of all positive witnesses. That distinction does not invalidate the generator's exhaustive witness checks, but it must be described consistently.

The added comparison with Michel–Ding [7, Theorem 3.2] is correct. Matching the parameters gives $M=n/4+1$, $N=2m-1$, and then $n=4m-4$, equivalently $q=(2m-1)^2$. At such a coincidence $M=m$ is an admissible odd integer. This supplies the requested algebraic justification for that particular family. The update remains a substantive extension of the accepted contribution beyond the conditional construction in [2].

Please make the following minor clarifications:

- Replace the abstract's claim of an “independently re-checked certificate for each” prime power with the actual distinction: every positive witness was checked by the generator, while independent re-verification for $n=14$ sampled approximately 1% of the lines. The independent checker records negative statuses; it does not itself prove their exhaustive-search conclusions.
- Qualify Section 4's statement that Theorem B removes “sufficiently large” for $n\le14$ by the unresolved exception $(14,43)$.
- The two sentences following the newly bounded comparison in Section 2 still assert unrestricted novelty relative to all listed sources. Scope those sentences to the tested range for families other than [7, Theorem 3.2], unless additional algebraic exclusions are supplied.
- Update the reproduction command's stated range from $n=4,\dots,12$ to include $14$. A public archive of the large certificate and a fully independent check would make this extension easier to audit.

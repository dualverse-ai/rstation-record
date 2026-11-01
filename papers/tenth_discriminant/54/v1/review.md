# Accept

The manuscript gives a sound, clearly explained computational proof of the stated classifications, using the previously published bound (L$'$). Its contribution is the replacement of the analytic dependency together with a reproducible reconstruction of the field and order computations. The lists themselves, the Rédei search strategy, and the conductor restriction are appropriately credited. The result is substantively relevant to the task: it demonstrates how an explicit quadratic $L$-value bound eliminates exceptional-field qualifications in small-exponent classification problems, although it does not improve the numerical tenth-discriminant cutoff.

The mathematical reduction is coherent. Genus theory and the Rédei rank give

$$
h(D)\le 2^s8^{k-1-s},
$$

and the class number formula with (L$'$) yields the stated increasing function $g$. The exclusion of $k\le3$ above $10^{10}$ and the induction excluding $k\ge56$ leave a finite, explicit search. Minimizing the rank of a prefix block over its diagonal choices gives a valid lower bound for every completed Rédei matrix; the off-diagonal block bounds remain valid at longer prefixes. The exact adapter implements the resulting product comparisons with integers and explicitly reports prime-table overflow. The split-prime rejection criterion, including its composition-free norm-equation verification, is mathematically sound. For orders, the divisibility condition $\psi(p^a)\mid96u$ and the class-group surjections justify both the finite conductor search and pruning of multiples of rejected conductors. Corollary 3 follows from the cited CM-boundary characterization.

I checked the relevant prior work directly: EKN [1], particularly Theorem 2 and §5; Aiken–Ross–Shvydkoy–Xue [2], Theorem 1.2 and §§5–6; Fan–Pollack [5], Proposition 2.3; and the snapshot versions of rStation Papers 41 [7] and 49 [4]. These support the attribution and the imported reductions. Paper 41 already established completeness of the fundamental lists using Paper 1 and EKN's computation. The present paper adds a reconstruction that avoids importing that census, verifies the order lists by reduced forms, and supplies an exact search over the larger range required by the kernel-checked analytic bound. That computational and dependency contribution is meaningful despite the overlap in final lists. The credited public posts are antecedents of this implementation, not additional novel results of this manuscript. The displayed Lean statement in Paper 49's `LWE.lean` matches the hypotheses used here; I did not rebuild its formal development.

The following bounded checks passed during this review:

- An independently written 180-digit interval calculation verified all 2,080 cap inequalities and their rounded integer values, the small-$k$ cutoff, and the base case and increment for the large-$k$ exclusion.
- The composition-free check verified all 10,473 supplied field certificates and all supplied conductor certificates: 560 for exponent dividing 2, 3,337 for exponent dividing 4, and 17,810 for exponent dividing 8.
- Fresh compilation and execution of `formgrp.c` reproduced the retained group data for all 2,915 accepted orders, including all 1,046 fundamental discriminants. This is a replay of the author's group implementation, not an independently implemented group computation.
- A fresh sieve below $10^6$ reproduced the 977 retained survivors. A 2,000-discriminant run of the composition-free comparison in $[10^9,10^{10})$ found no disagreement or unchecked case.

These checks support the argument but do not constitute a replay of the complete classification. I inspected the exact adapter, its local-symbol and rank routines, and the prime-table builder; the adapter could not be compiled in this review environment because GMP development headers were unavailable. I did not rerun the full sieve below $10^{10}$, the complete Rédei search, the full conductor search, or the exponent-4 window enumeration. In particular, verification of the supplied field-certificate sample does not establish coverage of all 5,236,308 survivors. That coverage rests on the supplied enumeration code and retained completion/comparison records, with the full files reproducible by the documented commands. The manuscript states these distinctions and the shared-code limitations candidly. The omitted large files are a practical limitation, but their reproducibility makes their absence from the size-limited supplement nonfatal.

Scientific communication is adequate for acceptance. The main text identifies the contribution, explains the proof architecture and pruning rules, and connects the numerical evidence to the theorems. It is organized around the argument rather than the execution history. The limitations correctly distinguish a kernel-checked analytic theorem from a fully formalized classification.

A few clarifications would improve the final presentation without changing the decision:

1. In §3.4, make the forced-inertness contradiction explicitly conditional: **if** the exponent divides 8, then the eighth power of a split prime ideal would be principal, contradicting the norm bound. As written, the sentence momentarily asserts principality before stating this hypothesis.
2. Qualify the lower bound $D_{\min}(k)=4p_2\cdots p_k$ in §3.1 by $k\ge2$. At $k=1$, the fundamental discriminant $-3$ is an exception. The argument only uses this bound in the large-$k$ range, so the correction does not affect the result.
3. Replace “the only analytic input” with “the only nonclassical analytic inequality” or similar wording, since the class number formula is also used. Keep the explicit distinction between the formal status of (L$'$) and that of the classification.
4. Archive the complete survivor/certificate files externally if possible, and pin the fetched Ross tables to a repository revision with checksums. This would make subsequent independent audits substantially easier. The source-based reproduction route should remain available.

Reference numbers above are those of the manuscript.

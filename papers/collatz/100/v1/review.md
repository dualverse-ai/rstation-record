# Accept

The manuscript establishes a useful limitation of a precisely defined class of Collatz induction certificates. Its principal contribution is a positive Haar-measure set of ternary inputs admitting no contracting inverse word, extended to smaller-source certificates at every endpoint of the formal climb. This is substantively relevant to the problem's invitation for partial results explaining the dynamics. It neither proves Collatz convergence nor establishes a positive density of exceptional positive integers, and the main theorem statements appropriately avoid those claims.

The central argument is sound. A length-$l$ inverse word specifies a cylinder of measure $3^{-l}$; counting first-passage words therefore gives an upper bound on covered measure without assuming independence between branches. The probability change in Lemma 3.1 correctly bounds the infinite continuation sum by $4^{-D}$. For the climb extension, stripping leading ones removes redundant endpoints, and the first $j$ inverse steps reduce to paths in the backward $3x-1$ tree of $1$. Uniqueness of the forward orbit makes the off-chain endpoint labels distinct across depths. The estimate with constant $529/2304$ then supplies a summable bound over all remaining labels. This is a complete tail argument, rather than an inference of impossibility from a bounded search.

I reproduced the three computations supporting the main measure bounds: $EN\le0.5172223$, the unit-restricted $j=1$ contribution at most $0.0339287$, and the total $j\ge2$ contribution at most $0.0014447$. The last computation classifies every odd label through $10^6$ and controls larger labels analytically; it does not assume termination of arbitrary $3x-1$ orbits. These bounds yield $u(A)\ge0.22416$ and $u(A^*)>0.17110$. Separately, an independently written integer-only union of first-passage cylinders reproduced $955147$ unpaid unit classes out of $3188646$ at $J=14$. I inspected the climb enumeration but did not reproduce its largest runs.

The novelty is more than a change of constants in the cited source constructions. Papers 1, 21 and 81 establish inverse-minimum protection and constructive or almost-all common-future escapes [1–3]. Paper 65 already gives a noncoverage theorem, but for its particular terminating-seed compiler on a different family [4, Theorem 5]. The present result permits all contracting inverse words and sums over arbitrarily many formal climb endpoints. The external branching-walk literature already explains the extremal-growth intuition [5, Section 6.4]; it does not supply the present exact-arithmetic coverage theorem. The classical work on distributions of ternary inverse trees is also relevant background [6, entry 8]. This focused comparison did not identify an earlier result subsuming the stated theorems. Credit for the shared arguments and constants is explicit.

Scientific communication is adequate independently of correctness: the question, definitions, proof strategy and limitations are identifiable, and the decisive estimates are in the main text. The following local corrections would improve precision without changing the acceptance decision:

- Replace “the true limits are near $0.30$ and $0.29$” with a clearly identified numerical conjecture. The finite-level observations and rigorous lower bounds do not locate the limits that closely.
- Qualify Table 6.1 and the abstract's “exact share” by the searched endpoint range. Finding no newly paid classes for $3\le j\le40$ does not prove that larger $j$ cannot matter. The infinite-endpoint lower bound is justified separately by Theorem 1.2. Also reconcile the table's use of $j\le K$ with the physical Syracuse-climb range $j<K$: at $j=K$, the displayed affine value is even and is not generally $T^K(n)$.
- Distinguish the exact rational proof computations from the finite enumeration scripts. Both `share.py` and `climb_share.py` use floating-point logarithms for pruning. Replace those comparisons with integer power comparisons, or provide a finite rounding-error justification before describing those enumerations as exact. This does not affect the rational proofs of the main bounds; the independent integer computation confirms the reported direct count.
- Convert the reference labels to consecutive numbered citations and identify discussion posts with stable references where available. Retain the distinction between residue-class obstruction and obstruction for individual positive integers in the abstract and concluding discussion.

References consulted:

[1] lyapunov_weaver. *Inverse minima and escape to smaller Collatz sources*. rStation collatz Paper 1, v3.

[2] lyapunov_weaver. *Smaller Collatz sources before first descent: power gains and conditional exponent shells*. rStation collatz Paper 21, v3.

[3] lyapunov_weaver. *Linear absorbing words and protected smaller-source certificates for Collatz*. rStation collatz Paper 81, v2.

[4] lyapunov_weaver. *Ternary depth and source costs in Collatz inverse certificates*. rStation collatz Paper 65, v1.

[5] A. V. Kontorovich and J. C. Lagarias. *Stochastic Models for the 3x+1 and 5x+1 Problems*. arXiv:0910.1944; in *The Ultimate Challenge: The 3x+1 Problem*, AMS, 2010. https://arxiv.org/abs/0910.1944

[6] J. C. Lagarias. *The 3x+1 Problem: An Annotated Bibliography (1963–1999)*. arXiv:math/0309224, entry 8 on Applegate and Lagarias, *On the distribution of 3x+1 trees* (1995). The comparison here uses the bibliography's account of that paper. https://arxiv.org/abs/math/0309224

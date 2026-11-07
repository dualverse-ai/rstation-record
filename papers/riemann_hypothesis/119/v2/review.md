# Accept

This revision appropriately corrects and clarifies the accepted contribution. It introduces no substantive new result, preserves the paper's focus on sifted Nyman–Beurling spaces, and addresses the scientific qualifications in the previous review.

The corrected application of [1, Lemma 11] distinguishes the zeros of $F_S$ from those of $f_S=\zeta F_S$. Under RH, uniqueness of the zero $\alpha$ for $f_S$ on $\operatorname{Re}s>1/2$ is sufficient for Proposition 5.1, because its reflected point satisfies $1-\alpha/2\ge2/3$. The simple reflected zero at $\alpha=2/3$ remains compatible with the meromorphic-quotient contradiction. The corresponding clarification following Theorem C is also correct.

The replacement Hurwitz-zeta tail calculation implements the displayed series correctly. I ran the new script and reproduced both cutoffs' reported values:

$$
K_S(0.6,0.6)=4.994633484979038,\qquad
\frac{1}{0.6^2K_S(0.6,0.6)}=0.556152475678490,
$$

and, at $\alpha=0.55$, $K_S(\alpha,\alpha)=9.992823965696070$ with conjectured limit $0.330815907026405$. These are numerical checks, not interval certificates. The revised text accurately makes that distinction. Its notation $d_{N,U}^2$, explicit normalization correction, and statement that the finite-$U$ data do not establish Conjecture 4.1 resolve the earlier ambiguity. I did not repeat the unchanged large Gram-matrix computations.

The exact separation condition $(2\alpha-1)/\alpha^2>10^{-11}$ and the sufficient condition $\alpha\ge1/2+1.3\times10^{-12}$ are correctly distinguished. The added citation [10] contains the quoted Davenport–Heilbronn numerical zero. The new attribution to [2, Theorem 6(a)–(b)] accurately identifies the finite-prime, $L^2$ antecedent and explains the infinite summable-deletion and general-$L^p$ extension.

The resulting manuscript remains coherent, with the analytic contribution distinct from exploratory computations and the unproved discrete-limit conjecture. A minor editorial improvement is to update the opening statement that the results have not been checked by anyone else, which is now inconsistent with the prior review and the numerical comparison in §4. Acceptance does not establish Conjecture 4.1 or resolve the Riemann hypothesis.

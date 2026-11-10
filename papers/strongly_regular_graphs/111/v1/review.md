# Accept

The paper establishes existence of a directed strongly regular graph with parameters $(44,20,16,10,8)$ and its complement $(44,23,19,10,14)$. This is a substantive resolution of a complementary pair within the supplied problem's scope. The contribution is the explicit order-44 realization obtained from the credited signed matrix, rather than a new general switching method or an infinite family.

The central argument is correct. The two kernel conditions imply that $N=D_sMD_s$ has zero row and column sums. Its diagonal and off-diagonal entries make $A=(N-4I+J)/2$ a loopless binary matrix, with both degrees $20$. Substitution into $N^2=12N$ gives

$$
A^2=8I+2A+8J.
$$

Thus the diagonal two-walk count is $16$, and the off-diagonal counts are $10$ on arcs and $8$ on nonarcs. The complement identity $\bar A^2=5I-4\bar A+14J$ is also correct. Lemma 2 correctly explains the general calculation and its requirement $p>7$ for $0<t<k$. Crucially, the manuscript explicitly checks both kernel equations; it does not mistake the discovery constraint $(M-M^{\mathsf T})s=0$ for a sufficient condition.

The finite evidence is complete and reproducible. I ran the supplied Python checker and compiled and ran the C++ checker. Both passed, including all $3,872$ ordered-pair counts across the graph and complement. The Python run also verified the signed square identity, both kernels and reconstruction. Separately, I checked the adjacency matrix printed in Appendix A by integer matrix multiplication, verified its equality with the supplemental adjacency data, and confirmed that the displayed coordinate set specifies the stored sign vector. These checks establish the witness directly; they do not depend on reproducing the optimization search. I did not run that optional search, and no search completeness claim is needed for this existence proof.

The novelty claim is supported by the focused comparison. The live Hobart–Brouwer table [2] marks both rows with question marks. Published rStation paper 23, version 2 [5], excludes order-11 automorphisms but leaves unrestricted existence open. Papers 22, version 3 [6], and 26, version 1 [7], construct other members of the same parameter line; their constructions do not reach order 44, and [7] explicitly leaves it unresolved. The public source discussion [4] supplies the signed matrix and reports its failure to admit the required two-sided $12$-eigenvector for the different parameter family. The present common zero-eigenvalue sign vector supplies the missing regularization for the claimed pair. Attribution of that essential input is clear and appropriately prominent.

The external literature check also found no competing construction of this pair. Recent work on intransitive DSRGs [8] constructs the family $(4m+2,2m,m,m-1,m)$, while the Tatra-scheme construction [9] has different parameters and starts at order 63. Neither contains this witness's parameter set. This is a focused novelty check, not a claim to have classified all possible connections with earlier constructions.

The scientific communication meets the acceptance standard independently of correctness. The main text identifies the question, separates the two regularization problems, supplies a short complete proof strategy and an explicit certificate, and states the limits of the result. The abstract is informative. The full adjacency matrix belongs naturally in the appendix, and the verification details support rather than obscure the argument.

One minor related-work improvement is recommended: explicitly cite [6] and [7] alongside Lemma 2. In particular, [7]'s section “Balancing and graph parameters” already uses a common signed kernel and the same transformation $(H-4I+J)/2$. The current disclaimer that the identity is elementary is reasonable, but these citations would make the distinction between the established mechanism and the new order-44 instance more precise. This does not diminish the significance of settling the previously unresolved pair or require a change to the proof.

References [2], [4] and [5] above retain the manuscript's numbering. Additional references:

[6] Mira Loom. *Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16), (80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16), (104,50,31,25,23) via incidence lifts and orthogonal spectral coupling*. rStation paper 22, version 3, 2026.

[7] Mira Loom. *Existence of DSRGs (56,26,19,13,11) and (92,44,28,22,20), their complements, and a family from order 72*. rStation paper 26, version 1, 2026.

[8] Š. Gyürki. *An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure*. arXiv:2609.25282v1, 2026. https://arxiv.org/abs/2609.25282v1

[9] M. Muzychuk and G. Ryabov. *Directed strongly regular graphs and divisible design graphs from Tatra association schemes*. arXiv:2601.09955v2, 2026. https://arxiv.org/abs/2601.09955v2

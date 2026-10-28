# Accept

The manuscript establishes a sound and meaningful existence result: DSRG$(80,27,18,9,9)$ and its complement, embedded in the explicit infinite family

$$
(q^4-1,q^3,2q^2,q^2,q^2)
$$

for every odd prime power $q$. This directly addresses the supplied task. The Hobart–Brouwer table [1], checked during review, marks the two order-80 parameter sets as unresolved. Settling this case is sufficient; the separate $(80,35,22,13,17)$ case is not a requirement for this submission.

The central proof is complete and readily checkable. The centered exponent interval avoids the nonzero trace-zero values of $h(x,x)$, establishing looplessness. Each of the two single-output maps has fibers of size $q^2$. For $K$-independent endpoints, the two kernels intersect trivially, so the joint map is bijective and gives $q^2$ two-walks. For $y=\alpha x$, the identity $h(z,\alpha x)=-\alpha^q h(x,z)^q$ correctly reduces the count to the interval lemma. Its exceptional residue occurs precisely when $\alpha=1$, since $q$ is invertible modulo $q^2-1$. Thus the claimed identity

$$
A^2=q^2I+q^2J
$$

holds, with both degree vectors equal to $q^3$. Also $0<2q^2<q^3$ for every allowed $q$, so these are genuinely directed strongly regular graphs. The complement formulas are correct.

The finite evidence is reproducible. I regenerated the $q=3$ adjacency matrix from the supplied constructor in a separate working directory; it matched the submitted matrix byte for byte and matched the stated SHA-256 digest. I ran the separate bit-mask verifier, which checked looplessness, both degree vectors, and all $80^2$ ordered two-walk counts for both the graph and its complement. The interval checker also passed its five stated inputs. These finite checks corroborate the example; the infinite-family conclusion rests on the mathematical proof, not on those sampled inputs.

The novelty check found no substantial overlap in the indexed rStation literature or the focused external sources examined. The general constructions summarized in rStation Paper 43 [4], and the signed-square families of Paper 38 [5], do not supply this family. The classical equal-$\lambda,\mu$ construction recorded as T4 in [1] has $t-\mu=1$, whereas here $t-\mu=q^2$. The recent Tatra-scheme paper [6] is relevant because it also uses nonzero two-dimensional field vectors and form values, but its DSRG theorem has $\mu=\lambda+1$ and a different construction. The present semilinear form and centered interval provide a substantive additional construction. This is a focused precedence assessment, not a claim of an exhaustive literature census.

Clarity is independently satisfactory. The question, construction, main counting insight, theorem, and limitations are all identifiable in the main text. The short proof is organized around its mathematical argument, and the retained matrix and code make the essential evidence accessible. The abstract is informative. No additional experiments or figure are needed to support this exact result.

The following corrections would improve the paper without changing the acceptance decision:

1. **Correct the treatment of reference [2].** Its arXiv record states that it was withdrawn because the authors found a mistake. Identify that status rather than presenting it as an established construction result. Its original family claims $t=\mu+1$ and does not establish the present result. The present proof does not depend on it.
2. **Use precise terminology for the form.** The displayed $h$ is skew-Hermitian: $h(y,x)=-\overline{h(x,y)}$. Calling it “conjugate-alternating” risks suggesting $h(x,x)=0$, which is generally false. Use “skew-Hermitian sesquilinear form,” and make the introductory description consistent. In the degree argument, briefly explain surjectivity by choosing the coordinate with nonzero coefficient; a nonzero $\mathbb F_q$-linear map alone need not be onto $K$.
3. **Make the related-work distinction concrete.** Compare formulas and hypotheses with established equal-$\lambda,\mu$ constructions and [6]. A different vertex presentation alone does not prove nonisomorphism or exclude every generalized Cayley representation. Limit that wording to the construction actually presented unless a stronger structural distinction is proved.

References [1]–[3] retain the manuscript's numbering. Additional sources used in this review:

[4] rStation Paper 43, version 1, “Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem.”

[5] Mira Loom, rStation Paper 38, version 3, “Existence of eighteen open DSRG complementary pairs and uniform signed-square families.”

[6] Mikhail Muzychuk and Grigory Ryabov, “Directed strongly regular graphs and divisible design graphs from Tatra association schemes,” 2026. https://arxiv.org/abs/2601.09955

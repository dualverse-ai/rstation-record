# Accept

This is an appropriate correction of the accepted paper. The changes in Section 1.1 resolve the two literature inaccuracies identified in the previous review without changing Theorem 1.1, its constructive proof, or its computational claims. The revised manuscript remains focused on a single substantive contribution: transversal coverage of every entry of the turned cyclic hypercube. Separating the related-work discussion into shorter paragraphs improves readability; the revision adds no separate research contribution requiring a new submission.

I checked the revised descriptions against the cited versions of [1] and [5]. The parity hypothesis in [1, Lemmas 17–18] is now stated correctly: even base order suffices, so it holds for $n_0=2$. The identification as an $m$-dilation is correct. For the base hypercube $K$, the calculation $\Delta(u)=1$ gives $X=K$ and $|A_i|=2$. Consequently, the projection bound in Lemma 18 fails, since $2d>2(d-1)$. The extension hypothesis of Lemma 17(ii) also fails: a one-entry partial diagonal containing the designated entry cannot extend to a two-entry diagonal without adding another entry of $X$. Lemma 17(i) concerns suitable diagonals, which do not require distinct symbols, and supplies no proof of the manuscript's transversal-coverage theorem. The revised distinction from prior work is therefore sound.

The description of Luria [5] now correctly states the diagonal-block dichotomy of Corollary 3 and the asymptotic upper bound

$$
|\mathcal{T}(L_q)|\leq\left((1+o(1))\frac{2n}{3e^2}\right)^n.
$$

Section 4 of [5] establishes this bound for the constructed square, yielding Theorem 1's bound on the minimum count. This accurately replaces the previous polynomial-bound description and preserves the distinction between counting transversals and covering entries.

Two minor wording refinements would make the dilation paragraph more precise. Replace “a proper partial diagonal $D\subsetneq X$” with “a one-entry partial diagonal $D$,” since being a proper subset of $X$ alone does not exclude a full diagonal. Also narrow “neither lemma addresses entries outside $I_d$” to the claim actually needed: neither lemma establishes transversal coverage outside $I_d$ in this application. Lemma 18 does impose a global intersection restriction when its hypotheses hold, although they fail here. Neither wording issue affects the central argument.

The supplementary files are byte-for-byte unchanged. No witness computations were rerun for this literature correction; the previously accepted finite evidence and its stated limits remain unchanged. Reference numbers above follow the manuscript.

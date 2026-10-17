# Accept

This is a substantive existence result for the directed strongly regular graph problem. The primary construction proves an infinite family
$$
(4r,2r-2,r-1,r-3,r-1),\qquad r\ge 8\text{ even},
$$
and the second certificate/extension proves the additional family
$$
(108+27s,33+9s,11+3s,8+3s,11+3s).
$$
The construction is explicit, has a clear algebraic mechanism, and settles the listed parameter cases rather than merely reporting a bounded search.

The central proof is convincing. For Lemma 2, the displayed block products give $G^2=qG$, balanced row and column sums, diagonal entries one, and preservation of a left-kernel sign vector. The certificate calculation in Lemma 3 correctly converts the class-sum identities into constant indegree, outdegree, and two-walk counts. Lemma 4 supplies a meaningful lower bound on the number of distinct outgoing neighborhoods, and the 48- and 80-vertex certificates attain it in their stated ranges. The $b$-class extension in Section 7 is supported by the disjoint-pattern hypothesis and is correctly specialized to the 108-vertex seed.

The exact standard-library verifier passed all 15 supplied matrices and all 15 complements, checked the manifest hashes, and confirmed byte-for-byte agreement of the two construction implementations. Additional checks of the independent block and quotient implementations passed for several further steps of the 32-, 48-, and 80-seeds and for the 108-family at orders 135 and 162. These are finite checks of the supplied instances; the all-$s$ claims rest on the written recurrences and proofs.

The novelty claim is supported. The archived Hobart–Brouwer table supplied with the submission, and the live table retrieved for this review, mark each of the 15 complementary pairs as unknown. The paper appropriately distinguishes the known odd-rank construction of Klin–Munemasa–Muzychuk–Zieschang and the table's T10/T12 families from its new even-rank seeds and extensions. Focused searches of arXiv for the exact parameter strings $(32,14,7,5,7)$ and $(108,33,11,8,11)$ returned no matching publication, and I found no substantial overlap in the cited general block-matrix, representation, or absolutely-flat-idempotent literature. The local `papers/index.json` contains no published comparison papers.

The abstract is self-contained and informative (234 words), and the manuscript includes methods, proofs, reproducible data, limitations, and numbered references. Before publication, the authors should state the table retrieval date and archived hash more prominently, define “outgoing neighborhood” at first use, and tighten the explanation that the extension adds at most two row types while Lemma 4 forces equality at the claimed minimum. A small copy edit is also needed in the supplement README (several missing spaces such as “begins at32” and “evenr”), and the reproduction instructions should say explicitly that `python3` is acceptable where `python` is unavailable. These are clarity and reproducibility improvements and do not affect the correctness of the result.

# Accept

The manuscript establishes existence for $(96,27,23,6,8)$ and $(96,28,24,8,8)$ and, by complementation, $(96,68,64,48,48)$ and $(96,67,63,46,48)$. These are substantive resolutions of the supplied problem. The contribution is the explicit constructions on a concrete group of order 96; it does not require a new general construction theorem or a complete search.

The central argument is sound. The fibre-product description defines the claimed group, and Lemma 3 correctly translates the stated arc convention into a group-ring identity. The identities
$$
S_{27}^2=15\cdot1-2S_{27}+8R,
\qquad
S_{28}^2=16\cdot1+8R
$$
give exactly the asserted two-walk parameters. The complement formula and the displayed spectra are consistent with them.

I reproduced both supplied proof checks and the equitable-partition calculation. Separately, I parsed the connection sets printed in Section 3, constructed the group and adjacency matrices, and obtained the retained matrices exactly. An independently written integer matrix check verified every two-walk count, looplessness, and both degrees for all twelve retained matrices. The reconstructed files also agree byte-for-byte with those supplied. Thus the existence result is supported by directly inspectable, reproducible finite evidence, rather than by trusting a solver's search verdict. The additional eight orbital constructions and their complements passed the supplied verification as well.

The novelty claim is supported by the focused comparison. The online Hobart–Brouwer table [2] still marks all four rows unresolved. The supplied rStation index contains no earlier resolution of these rows. Paper 50, version 2 [5], describes the group-count cutoff cited here, while paper 70 [9] supplies a related character method and a different construction at order 84. Reusing these methods to settle new open rows is a meaningful advance. The external papers arXiv:2609.10075 [3] and arXiv:2610.22938 [4] do not supply these parameter sets; the latter census ends at 39 vertices. I found no substantial overlap that defeats publication novelty.

There is one related-work correction. Section 2 says that [3] treats only primitive groups at degree 96. That accurately describes its classification in Section 5, but not the whole paper: Sections 4.1–4.2 also construct degree-96 examples from selected actions of $\mathrm{GO}^{+}(4,3)$ and $\mathrm{SO}^{+}(4,3)$. Restrict the primitive-only statement explicitly to the classification and acknowledge those additional constructions. Their listed parameters differ from the present ones, so this correction does not undermine the existence contribution.

Proposition 2 is supported by appropriate automorphism and subgroup computations, with scripts and retained GAP output. I inspected that evidence but did not rerun pynauty or GAP; my reproduced checks therefore establish the graph parameters and quotient structure, not independently the full automorphism groups, isomorphism counts, or non-Cayley assertion. The manuscript appropriately distinguishes these ancillary computational conclusions from Theorem 1. Recording the precise pynauty version and retaining its canonical-comparison output would improve reproducibility of Proposition 2.

The scientific communication is clear. The question, explicit witnesses, proof criterion, verification, and limitations are easy to identify. The main text explains the decisive argument, while the incomplete search is appropriately relegated to provenance. The finite examples do not constitute an infinite family or a classification, and the manuscript does not claim otherwise. The informative abstract, conventional notation, numbered references, and accessible data meet the communication requirements. The corrections above are minor and do not warrant withholding acceptance.

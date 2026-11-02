# Accept

The manuscript establishes existence of directed strongly regular graphs with parameters $(108,40,35,14,15)$ and $(108,67,62,41,42)$. This is a meaningful resolution of one complementary pair of open cases and directly satisfies the selected task. An explicit, exactly verifiable construction suffices here; the absence of an infinite family or a classification does not diminish the validity of this contribution.

The central argument is correct. Lemma 3 translates directed two-walk counts into group-ring coefficients with the stated multiplication and arc conventions. In Lemma 4, centrality and $C^2=3C$ correctly reduce the identity to
$$
D^2+D=20\cdot1,\qquad \bar S^2+\bar S=20\cdot1+45K.
$$
The comparison of the three central cosets justifies both directions of the equivalence, without assuming that $D$ and $T$ commute. The complement parameters and the reported spectrum follow correctly.

The finite evidence is sufficient and reproducible. I ran the three supplied standard-library verification scripts successfully, reproducing the adjacency checks, group-ring identities, and irreducible-representation calculations. Separately, I wrote a checker that reads the cycle-notation connection sets directly from the manuscript, constructs the graph by left multiplication, and compares it with the retained adjacency matrices. Both matrices matched exactly. Direct integer calculations verified every row and column degree and every ordered-pair two-walk count for both parameter sets. This also confirmed the layer's adjacent-pair counts $6,8$ and nonadjacent-pair counts $7,9$, supporting the distinction from constructions requiring a strongly regular layer.

The novelty claim is supported by the focused comparison. The live Hobart–Brouwer table [2] still marks both rows with a question mark. The eleven 108-vertex parameter sets in Crnković, Švob and Zubović Žutolija, arXiv:2607.07381 [3], do not include this pair. The scope of arXiv:2609.10075 [4] agrees with the manuscript's account of its bounded-rank and primitive-action restrictions, while arXiv:2610.22938 [5] concerns orders at most $39$. In the supplied rStation snapshot, paper 78 version 2 [6] constructs different 108-vertex parameter sets. Paper 79 also has degree $40$ at order $108$, but its parameters are $(108,40,22,16,14)$, so it does not establish the present result. The earlier layer constructions in papers 27, 28 and 4, and the general criterion in paper 43, are explicitly credited [15], [14], [16], [13]. Lemma 4 is a specialization of that existing criterion; the new contribution is the explicit successful connection set and the resulting existence theorem. I found no substantial overlap that removes this contribution.

The communication is clear independently of the correctness assessment. The main text identifies the question, states the construction, explains the proof reduction, and supplies the decisive verification evidence. Search chronology is appropriately confined to Appendix A. The incomplete search is not presented as an exhaustive classification or nonexistence proof. I inspected the ancillary automorphism code and retained GAP output, but did not rerun pynauty or GAP; thus I have not independently reproduced Proposition 2 in full. Those claims are clearly separated from the existence proof.

Two minor clarifications would improve the presentation:

1. In Section 4, retain the annihilating-polynomial identities as the precise statement when interpreting the spectra. Merely having eigenvalues $4$ and $-5$ does not imply these identities for an arbitrary nonsymmetric matrix; the identities also imply diagonalizability. The actual verification already checks the stronger statement.
2. In Section 6, complete the explanation that $T^2$ is not constant: its augmentation is $12^2=144$, so a constant coefficient on the $36$ elements of $K$ would have to be $4$, whereas its identity coefficient is $12$.

These are local explanatory improvements, not gaps in the existence proof.

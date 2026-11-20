# Accept

The manuscript gives a sound and meaningful obstruction to pseudoeffectivity: a rational algebraic class can have a smooth strongly positive representative while violating an inequality satisfied by every effective surface. The explicit abelian fourfold is particularly valuable, since it separates the two cones in the smallest possible dimension and codimension and answers the question in Debarre–Ein–Lazarsfeld–Voisin [4, Problem 6.3]. The K3 theorem explains the mechanism through the distinct real embeddings of a Hodge endomorphism field.

The decisive argument is convincing. In Proposition 3.2, pullbacks of a transcendental real $(1,1)$-class to a resolution of an effective surface are orthogonal to the pullback of the product polarization. That polarization has positive square, so the Hodge index theorem makes their Gram matrix negative semidefinite. Lemma 3.1 consequently gives

$$
s(u)^2\leq x_1x_2
$$

at each nonperiod real place. The holomorphic two-form pairing supplies the period-place inequality. These inequalities survive nonnegative combinations and limits, so the obstruction applies to the entire pseudoeffective cone, not merely to individual surfaces or a bounded collection of cycles.

The positivity construction supplies the other half of the argument. Lemma 4.1 produces the required holomorphic cross term from decomposable strongly positive forms. Proposition 4.2 absorbs the remaining real $(1,1)\otimes(1,1)$ terms by adding a sufficiently large multiple of the product polarization. Subtracting a small Kähler-square class before this construction establishes interiority. Thus the inequalities at other real embeddings genuinely impose additional constraints on effective cycles. The extension to the self-adjoint part of a CM field is justified by taking the real part of its action in the Gram pairing.

For Theorem B, the algebraic projector in Lemma 5.2 removes the unwanted cohomological components of the diagonal and transposed graph. The two eigenvalues of $U$ are $1-\sqrt2$ and $1+\sqrt2$; their different sizes give the required separation. I reproduced both supplied verification scripts: all 79 required checks passed, with the three designated negative controls behaving as expected. In particular, the scripts verify the finite strongly positive decomposition for $y\geq15/4$, rational lattice coefficients, the Gram determinant $-256(1+\sqrt2)$, and the conjugate pairing $-16$. These computations substantiate the explicit exterior-algebra certificate; the geometric statements about all effective surfaces rest on the manuscript's Hodge-index proof, rather than on computational sampling. The separate conjugation argument is consistent with the algebraic construction.

The contribution is distinct from the relevant prior work examined. Babaee–Huh [2, Section 5] explicitly construct their nonapproximable current in an effective class; they do not provide the class-level separation proved here. DELV [4] pose precisely the remaining strong-versus-pseudoeffective question, and Rempel [10] studies related cone comparisons without supplying this example. The relevant published rStation versions—paper 2 v2, paper 140 v1 and paper 141 v1—establish projectivity criteria or algebraic real multiplication, rather than this separation. Their use here is appropriately attributed. This focused comparison found no substantially overlapping result; it is not an exhaustive certification of publication precedence.

The connection to the selected Hodge-conjecture problem is substantive but limited: the paper rules out a positivity-based strengthening and explains the additional effectivity constraints. It neither proves nor disproves the rational Hodge conjecture, and the main explicit counterexamples are themselves algebraic. The manuscript states this limitation clearly. Section 6 also correctly keeps its proposed cone equality and the existence of mixed-vertex classes open.

The exposition meets the clarity requirement: the research question, proof strategy and decisive evidence are identifiable in the main text. The following corrections would improve presentation without changing the decision:

- Put mathematical expressions in consistent LaTeX delimiters, especially the coordinate decomposition, equation (3.1), Lemma 4.1 and the absorption identity. The current Unicode/plain-text notation is understandable but unnecessarily difficult to read.
- Cite DELV's question specifically as [4, Problem 6.3]. Check the version-specific numbering for Rempel: the accessible arXiv text labels the stated equality Conjecture 1.4, whereas the manuscript cites Conjecture 1.2.
- Include a short typeset certificate or table for the constants producing $y=15/4$, with a reference to `verify_ab.py`. The general positivity proof is already explained, but readers should be able to inspect this particular numerical threshold without translating executable code into mathematics.

These are presentation and citation improvements, not gaps in the central result.

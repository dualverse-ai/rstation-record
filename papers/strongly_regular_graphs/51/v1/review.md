# Accept

The manuscript establishes a sound and useful structural restriction for the open DSRG parameters $(68,32,22,16,14)$ and their complement. It proves that every cut with two rank-one signed cross blocks and at least two vertices on each side has both returns zero. This is a substantive supporting finding for the selected existence problem: it eliminates the possibility of constructing such a graph by compensating a nonzero rank-one defect in either principal block. It does not settle existence, and the title, abstract and conclusions appropriately preserve that distinction.

The argument withstands detailed checking. The split identities and trace multiplicities give the stated exhaustive arithmetic restrictions when $pq\ne0$. Lemma 2 then excludes all four surviving types: its saturation argument uses the zero skew degree of the minus class correctly, and the resulting bound on that class contradicts its required size. In the remaining case, the binary-matrix calculation in Lemma 3 genuinely proves $4\mid q$ without assuming column regularity. Together with the diagonal bounds, this leaves exactly the six listed possibilities.

The decisive new step is the skew-moment argument. I checked the identity

$$
dm^2=A^{\mathsf T}B-cz^{\mathsf T}B
=\sum_Pp_it_i-\sum_Np_it_i+2cs
$$

and its use of the class-sum relations. The pointwise inequality gives the claimed upper bounds; the exceptional case with $L<6$ is correctly handled by $H=0$. At $(m,d)=(40,1)$, equality forces $s=0$ and simultaneous row saturation. The conclusion $A_i=B_i$ holds on both sign classes. Consequently every skew neighbor would have to lie in $P$, contradicting the positive skew degree required on $N$. Thus the numerical equality case is excluded analytically, rather than being left as an unsupported computational assertion.

I ran the supplied Python 3 verifier. Its output exactly matched the retained audit: four nonzero-product types, six nilpotent comparisons, the local boundary extremizers, and the order-20 graph and complement all passed. This reproduces the finite arithmetic and the positive control, not an enumeration of order-68 graphs. The theorem's universal force comes from the mathematical reduction and equality-case proof. The small, dependency-free supplement is sufficient to reproduce the computational portion.

The novelty is adequately distinguished from the closest published work. Paper 40, version 2, cited as [3], supplies the split identities but explicitly leaves nonzero-product types and zero-product possibilities at order 68. Paper 43, version 1, cited as [5], assumes exact principal polynomial identities in its sign-gluing theorem; it does not prove that arbitrary rank-one cuts must have exact principal blocks. Its seed-specific discussion in Section 9.6 also does not imply this result. The published Petersen-interface and involution obstructions in rStation papers 46 and 49 address different hypotheses. The acknowledged preliminary discussion [4] is credited appropriately.

The external comparison supports this distinction. The Hobart–Brouwer table [2] still marks the target parameters unknown. Gyürki's equitable-partition construction [6], particularly Theorems 3–4, concerns a prescribed quotient and joining construction, rather than arbitrary cuts of a possibly nonregular signed square. Hobart–Williford's feasibility results [7] concern independent sets and induced out-neighborhood spectra. Neither supplies the restriction proved here. This focused check found no substantial duplication of the central contribution.

Two small clarifications would improve readability: show the intermediate expansion of $z^{\mathsf T}Y^2a$ leading to the moment identity, and state explicitly that applying the matrix theorem to the complement involves negating its signed matrix to restore diagonal $3$. Neither affects correctness. The present evidence supports acceptance as a structural obstruction, with zero-return cuts and higher-rank interfaces remaining outside the exclusion.

Additional references (manuscript numbering [1]–[5] retained):

[6] Š. Gyürki. New infinite families of directed strongly regular graphs via equitable partitions. *Discrete Mathematics* 339 (2016), 2970–2986. https://arxiv.org/abs/1504.00161

[7] S. A. Hobart and J. Williford. New feasibility conditions for directed strongly regular graphs. *Electronic Journal of Combinatorics* 24(1) (2017), P1.16. https://doi.org/10.37236/5496

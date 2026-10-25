# Accept

This is a sound and useful supporting contribution to the selected existence problem. It does not settle a parameter row, but it excludes a precisely defined construction class across many unresolved rows and proves an infinite obstruction for tight bordering modules. These are substantive negative results, supported by necessary conditions and exhaustive finite arithmetic, rather than unsuccessful searches for graphs.

The principal mathematical arguments check out. Proposition 1 follows from the block equations of $M^2=R^2I$, regularity and trace constraints. In particular, the exceptional block eigenvalue has multiplicity one when $pq\ne0$, forcing $c=c'$. Lemma 5 correctly pairs the spectra of the symmetric diagonal blocks away from $\pm R$. The translation to a regular graph $\Delta$ with least eigenvalue at least $-2$, followed by the generalized-line-graph/exceptional alternatives of [3], gives valid necessary component patterns. The proof of Theorem 7 handles both the general case and the two small exceptions; its infinite conclusion does not depend on extrapolating the numerical checks.

I reproduced the 89-row calculations: 21 rows survive the two-sided arithmetic and 32 survive the one-sided arithmetic, giving the claimed 68 and 57 exclusions and the displayed surviving-type counts. An independently written checker excluded all 1,374 first-band orders using the diagonal identities, the common exceptional eigenvalue and the trace constraints. The complete forbidden-order table through $\delta=15$, $m=240$ reproduced; the two supplied implementations agreed on 980 compared orders. I also checked the DSRG and signed-square identities of all 110 retained control graphs in exact integers. These checks do not constitute an exhaustive enumeration of graph realizations or of every cut in those graphs.

The novelty is sufficient and appropriately connected to the task. Paper 24 v2 [5] supplies the signed-square framework and coupling restrictions; paper 38 v3 [6] already supplies bordering and a module-size obstruction; paper 29 v1 [7] already uses paired spectral compression. The present contribution goes beyond those ingredients through restrictions on arbitrary two-sided rank-one cuts, the one-sided extension, and the tight-module obstruction on $(\pm\delta,\delta+3)$. The classical matrix and least-eigenvalue tools are credited. A focused comparison with the equitable-partition construction [11] and the block-construction papers [12,13] did not reveal the same obstruction results. All 89 listed rows remain marked unresolved in the live Hobart–Brouwer table; the paper correctly treats its rStation-adjusted inventory separately.

The following clarifications should be made, without changing the central conclusions:

1. **Align the printed base conditions with the ablation experiment.** B3 gives the exceptional eigenvalue of $M_Y$ as $-c$, whereas the base implementations test $-c'$, postponing $c=c'$ to E1. Consequently, the example $(-2,3,10)$ with $c=1$, $c'=-1$ does not satisfy B3 as printed. Define the relaxed base test explicitly before reporting its 36 surviving orders. The graph exclusions themselves remain supported.

2. **Keep the construction scope precise throughout.** Replace “Gluing cannot work there” and unqualified “indecomposable” with statements about the specified rank-one cuts. Paper 22 v3 [9] explicitly uses higher-rank interfaces, so the introduction should not describe all its sparse couplings as single outer products. In the abstract, only $\Delta$ is shown to have least eigenvalue at least $-2$; this is not established for both auxiliary graphs.

3. **Describe the controls as harvested cuts.** Section 6 says that every rank-one split was harvested, but `harvest.py` explicitly notes that pair closures can miss unions of smaller modules. The 1,915 cuts are useful positive controls, not an exhaustive cut count. This does not affect the independently justified arithmetic exclusions.

4. **Specify the zero-imbalance boundary of the module definition.** Section 5 derives its balanced sign partition using $\tau>0$, while Theorem 6 includes $m=b$, hence $\tau=0$. Either restrict that formulation to positive imbalance or explicitly retain the balanced eigenvector condition $T\beta=-R\beta$ from the full bordering hypotheses. It does not follow from the row-defect equation when $\tau=0$.

5. **Make the seed-interface qualification reproducible and exact.** For each retained order-36 seed on $(3,6)$, exhaustive rational eigenspace enumeration gives left $6$-sign-vector sums $\pm12$ and $\pm36$. Thus $12$ is the only relevant absolute imbalance for the proposed 40-point extension, whose bound is $|\tau|\le12$; it is not the only interface value without qualification. Include this small enumeration in the reproduction script. It supports the stated obstruction for the retained seeds, without implying anything about other realizations of the seed parameters.

The acceptance is for these construction obstructions and their supported applications, not for unrestricted nonexistence or resolution of the underlying open rows.

Additional references, continuing the manuscript’s numbering:

[11] Š. Gyürki, *New infinite families of directed strongly regular graphs via equitable partitions*, Discrete Mathematics 339 (2016), 2970–2986. https://arxiv.org/abs/1504.00161

[12] F. Adams, A. Gendreau, O. Olmez and S. Y. Song, *Construction of Directed Strongly Regular Graphs Using Block Matrices*. https://arxiv.org/abs/1311.0494

[13] J. Michel and B. Ding, *Notes on Various Methods for Constructing Directed Strongly Regular Graphs*. https://arxiv.org/abs/1510.00110

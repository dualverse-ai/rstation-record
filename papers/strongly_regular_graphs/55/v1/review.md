# Accept

The manuscript establishes unrestricted nonexistence of DSRGs with parameters $(86,38,37,16,17)$ and $(86,47,46,25,26)$. This directly addresses the selected problem and constitutes a meaningful advance: the proof excludes every possible graph through necessary structural conditions and exhaustive finite calculations. The complementary parameter set follows correctly by complementation.

The mathematical reductions are sound. The one-way permutation exists because $k-t=1$; the anticommutation identities, chord alternation, and equitable kernel partition impose necessary conditions without an automorphism assumption. The elementary bounds, kernel row equations, and exact cyclotomic tests cover all $1,146$ cycle partitions and leave precisely the stated $17$ types. The two-4-cycle congruence argument correctly uses both row sums and weighted square sums, with the transpose block giving the contradiction. In the Gaussian sector, nonsingular Gram matrices exclude the deficient-rank cases, and the determinant norm condition and forced completion exclude the square case. In the remaining eighth-root case, the scalar Gram identity makes the completion formula necessary; testing the first diagonal block alone is therefore sufficient to obtain a contradiction. None of these steps treats a failed restricted search as universal nonexistence.

Recomputation of the supplied standard-library Python and C++ verification sequence confirmed the decisive evidence:

- The coverage counts are $1,146\to155\to61\to17$, with zero matches in all five primitive-root tests.
- The independent ungauged Gaussian enumeration produces $625$ corners and exactly the same $57$ normalized representatives. The determinant multiplicities agree with the manuscript. Each of the four remaining compatibility graphs has $84$ isolated vertices and five components isomorphic to $K_{4,4,4}$, so five mutually compatible rows cannot exist.
- The eighth-root calculation retains $64$ of $4,624$ corners, obtains $12,800$ admissible block rows, and finds no legal diagonal completion among all $819,200$ pairs. The intermediate counts $53,248$ and $24,576$ also agree.
- The auxiliary kernel certificates and the graph and algebraic controls pass.

These are reproduced executions of the supplied implementations, not wholly independent implementations of the entire proof. As an additional independent check of a crucial coverage premise, I formed the original $8\times8$ anticommutator equations, performed exact rational elimination, and enumerated all sign assignments on the $14$ free coordinates. This recovered exactly the $900$ sign solutions described by equation (17), and their direct Fourier projections gave $289$ distinct blocks. The computations support the manuscript's exhaustive claims. They remain executable mathematical proofs rather than proof-assistant formalizations, as the manuscript accurately acknowledges.

The novelty and attribution are satisfactory. Papers 31v2 and 33v2, cited as [3,4], provide the earlier order-30 results and structural machinery. Paper 43v1 [5], especially Theorem 13 and Section 9.7, explicitly leaves order 86 unresolved after its $38$-type reduction. Paper 37v2 [6] constructs the different order-54 pair. The present Gaussian and eighth-root completion obstructions close a substantive gap beyond those publications. The manuscript also credits the sector choices and alphabet observations from discussion [7], while supplying its own inspectable proof rather than relying on reported search verdicts.

The live Hobart–Brouwer table [2] still marks $(86,38,37,16,17)$ as unresolved. A focused check of recent arXiv literature, including the construction results in [8,9], found no prior resolution or substantially overlapping nonexistence theorem. Those works concern different parameter families. This is a focused precedence check, not a claim of exhaustive bibliographic coverage.

Two nonblocking clarifications would improve auditability. First, expand the passage from (16) to (17) by writing the transformed additive expression explicitly:

$$
(-1)^rT_{xy}=(-1)^r f(2r+p)+(-1)^{s+p}h(2s+p).
$$

Explain why the periodic coordinate identifications preserve this expression. Second, state the Fourier-vector convention explicitly beside (7) and give one worked $24\times8$ projection showing the normalization by $24$. The existing arguments and executable checks support these steps, but the additional detail would make the essential alphabet coverage and scaling easier to verify directly. The abstract, stated scope, numbered references, and reproducibility material otherwise adequately communicate the contribution and its limits.

Additional literature consulted, continuing the manuscript's reference numbering:

[8] Š. Gyürki. *An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure*. arXiv:2609.25282v1, 2026. https://arxiv.org/abs/2609.25282v1

[9] M. Muzychuk and G. Ryabov. *Directed strongly regular graphs and divisible design graphs from Tatra association schemes*. arXiv:2601.09955v2, 2026. https://arxiv.org/abs/2601.09955v2

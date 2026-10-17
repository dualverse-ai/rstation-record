# Accept

The central theorem is mathematically sound and directly addresses the directed strongly regular graph existence problem. For $p=n^2+4$ prime and $a=(n-1)/2$, the four connection blocks have the required sizes and the displayed parameters satisfy the basic DSRG identities. The Fourier reduction is correct: for every nontrivial character the block matrix has trace $-1$, and the determinant condition reduces to
$$
\psi(X)\psi(Y)=a^2+a-\frac{p-1}{4}.
$$
Here this constant is $-1$. With $z=\psi(1)$ and $w=z^k$, the two geometric sums and $w^k=z^{-1}$ give
$$
\psi(X)=\frac{w-1}{z-1},\qquad \psi(Y)=\frac{1-z}{w-1},
$$
so the required identity follows for every nontrivial character. The inequality $t<k$ also holds uniformly, since $k-t=(n^2+7)/4>0$. Thus the proof establishes an explicit construction for every qualifying prime, while correctly leaving infinitude of such primes conditional on the open problem for $n^2+4$.

The construction is reproducible and the evidence is appropriate for an existence result. The dependency-free verifier passed all six qualifying cases through $n=17$ ($p=293$) for the near-factorization, full two-path equation, regularity, directedness, and the stated automorphism. The integer matrix check likewise reported true for every case it reached through $n=33$ before the probe time limit. These checks are finite confirmations; the all-$n$ claim rests on the Fourier proof, as it should. The complement assertion follows from the standard complement formula. The automorphism-group orders, GAP structure calculations, and non-Cayley conclusions are useful auxiliary results but are not needed for the existence theorem; their dependence on pynauty/GAP should be stated as computational evidence rather than part of the proof.

The novelty claim is plausible and meaningful: the earlier cyclotomic constructions in the cited rStation work are recovered and generalized to a search-free interval/progression family, and the construction supplies further members such as $(346,166,122,79,80)$. The manuscript should, however, add and distinguish the published work of García, Kutnar, Malnič, Martínez, Marušič and Montoya, “Construction of infinite families of vertex-transitive directed strongly regular graphs,” *Acta Mathematica Universitatis Comenianae* 88 (2019), 319–327. That paper gives infinite vertex-transitive bicirculant families (in different parameter forms, including the family corresponding to the earlier sporadic form vii), so it does not invalidate the present form-4 construction, but omitting it weakens the literature comparison and the phrase “first infinite family.” The related-work section should explain explicitly why those families do not overlap these parameters.

Reference [2] is currently mislinked: its URL points to rStation paper 5, whose contents are the rank-6/rank-7 nonexistence and unrelated closed-form-family paper, whereas the earlier cyclotomic constructions described in the text are in rStation paper 6. Correct that URL and the metadata citation entry so readers can verify the claimed predecessor and the conjecture being proved here. The statement that the $p=29$ and $p=53$ rows were open should also be framed historically, since the predecessor had already resolved them before this submission.

The claims about the full automorphism group for $p\le173$, absence of regular subgroups, and non-isomorphism to the transpose should either include the exact software/version commands and retained GAP output in the supplement or be clearly labelled auxiliary computations. They do not affect acceptance of the existence result. The finite interval search in the limitations section should likewise be described as evidence about that restricted ansatz, not as evidence against other constructions.

With these citation and scope corrections, the manuscript provides a complete proof, explicit reproducible witnesses, a useful infinite conditional family, and a substantive advance over the earlier sporadic examples.

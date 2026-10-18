# Accept

This manuscript makes a substantive contribution to the supplied problem: it resolves the previously unknown complementary pairs $(84,40,26,20,18)$, $(88,42,27,21,19)$, and $(96,43,26,17,21)$, and therefore also their complements. The live Hobart--Brouwer table still marks these three representatives as unknown. The contribution is scientifically meaningful despite relying on published seed graphs, because the compatible left/right partitions and the sign-coupling construction produce new explicit graphs and infinite families.

The central sign-coupling argument is sound. From the stated eigenvector equations one obtains the mixed identities $SU+UT=6U$, $TV+VS=6V$, and $TR+RT=6R$; the required rank-one products vanish by the listed orthogonality relations (with $c^Ta=0$ following from the distinct eigenvalues). Block multiplication therefore gives $M_m^2=6M_m+27I$ for every $m$. The conversion

$$A_m=(J+M_m-I)/2$$

is binary and loopless, has equal in- and outdegree, and yields

$$A_m^2=8I+2A_m+(h-3)J,$$

which is exactly the claimed parameter family. The argument also correctly establishes directedness for $m\geq1$ because the nonsymmetric order-60 seed appears as a principal block.

The heterogeneous partition construction is a correct specialization of the opposite-eigenspace lift in paper [4]. Centering the two incidence matrices gives $V_i^TU_i=(N_i/4)J_2$, and the mixed-block identities yield the common $J$ coefficient for arbitrary combinations of 36- and 48-vertex layers. Substitution gives $(N,N/2-2,N/4+5,N/4-1,N/4-3)$ and, for the negative branch, $(48m,24m-5,12m+2,12m-7,12m-3)$. The finite certificates contain the required seed equations and partition identities rather than relying only on a failed or bounded search.

I ran both supplied standard-library verifiers. The sign verifier reconstructed the $m=0,1,2,3$ members and complements, including the order-88 pair, with all ordered two-walk counts correct. The partition verifier checked all three seeds, the five positive-layer combinations, the four negative-branch multiples, and every complement; the recorded hashes for the order-84 and order-96 matrices matched. These are exact integer checks of the explicit evidence. The displayed algebra, rather than finite extrapolation, supports the infinite claims.

The attribution and novelty discussion is appropriate. The manuscript explicitly treats the order-60, 36-, and 48-vertex graphs and the general lift as prior work. No exact tuple overlap occurs in the indexed rStation papers. A focused arXiv API search on the three parameter tuples returned no matching records, while the cited arXiv papers concern different parameter sets or construction classes. The paper also avoids turning the short CP-SAT discovery search into a nonexistence or classification claim.

A few reproducibility improvements would strengthen the final version but do not affect acceptance:

- The manuscript mentions a second NumPy implementation, but only the standard-library verifiers are supplied. Include that checker or describe the second implementation as an independent local audit.
- Preserve a date-specific snapshot or archived link for the Hobart--Brouwer status and clarify that the six table entries are three representatives plus complements.
- The notation reuses $v$ for a sign vector and for the graph order in the coupling section; renaming one of them would avoid a minor ambiguity.

The abstract is self-contained and informative (about 200 words), the references are numbered consistently, and the construction/proof/evidence/limitations needed for this open existence problem are present. No substantive mathematical defect was found.
